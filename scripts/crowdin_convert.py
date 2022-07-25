"""
    Creates api.en.json file in Crowdin's format
    containing translatable parts of the API
    produced from the type stubs files.
    Inclues first line of docstring (summary),
    parameter names and parameter docs.
"""

import ast
import os
import json
import re
import sys
from common import TypeshedFile, get_stub_files, DIR, get_source, DocStringVisitor


NODE_TYPES_WITH_DOCSTRINGS = (ast.FunctionDef, ast.Module, ast.ClassDef)
EN_JSON_PATH = os.path.join(DIR, "../crowdin/api.en.json")
TRANSLATED_JSON_DIR = os.path.join(DIR, "../crowdin/translated")

modules = [
    "gc",
    "log",
    "machine",
    "math",
    "microbit",
    "micropython",
    "music",
    "neopixel",
    "os",
    "radio",
    "random",
    "speech",
    "struct",
    "sys",
    "time",
]


def typeshed_to_crowdin():
    """Entrypoint to convert from English typeshed files to a JSON file for Crowdin translation."""
    data = {}
    files_to_process = get_stub_files(modules)
    for ts_file in files_to_process:
        if not ts_file.python_file:
            continue
        data.update(get_docstrings_dict(ts_file))
    save_docstrings_as_json(data)


# Translation key to dict with message/description fields.
TranslationJSON = dict[str, dict[str, str]]


def get_docstrings_dict(ts_file: TypeshedFile):
    source = get_source(ts_file.file_path)
    tree = ast.parse(source)

    class DocStringCollector(DocStringVisitor):
        def __init__(self):
            super().__init__(ts_file.module_name)
            self.data: TranslationJSON = {}

        def handle_docstring(self, node: ast.AST, name: str) -> None:
            key_root = ".".join([*self.key, name])
            key = key_root
            suffix = 1
            if isinstance(node, ast.FunctionDef):  # ctx.id
                for decorator in node.decorator_list:
                    if hasattr(decorator, "id"):
                        if decorator.id == "overload":
                            key = f"{key}-{suffix}"
                            while key in self.used_keys:
                                suffix += 1
                                key = f"{key_root}-{suffix}"
            self.used_keys.add(key)
            self.data.update(get_entries(node, name, key))

    collector = DocStringCollector()
    collector.visit(tree)
    return collector.data


def pretty_api_name(name):
    return name.replace("_", " ").strip().lower()


def get_entries(node, name, key):
    entries = {}
    docstring = get_docstring(node)
    summary, param_section = split_docstring(docstring)
    # We don't want to translate param names if we have no summary.
    if not summary:
        return {}
    # Remove prefixed microbit.foo names as it's better just to translate the important part.
    api_name_for_translation = pretty_api_name(name).replace("microbit.", "")
    entries.update(
        format_translation_data(
            key,
            api_name_for_translation,
            f"({get_node_type(node)} name) {summary}",
        )
    )
    summary_key = ".".join([key, "summary"])
    entries.update(format_translation_data(summary_key, summary, summary))
    matched_params = get_matched_params(node, param_section)
    check_param_docs(key, get_params(node), matched_params)

    for param_key in matched_params:
        # Translate param name.
        param_name_key = ".".join([key, "param-name", param_key])
        entries.update(
            format_translation_data(
                param_name_key,
                pretty_api_name(param_key),
                f"(parameter name) {matched_params[param_key]}",
            )
        )
        # Translate param doc.
        param_doc_key = ".".join([key, "param-doc", param_key])
        entries.update(
            format_translation_data(
                param_doc_key, matched_params[param_key], "Parameter docs"
            )
        )
    return entries


def get_docstring(node: ast.AST):
    """Get the docstring, returning string content for constant strings on the assumption they're for preceding fields."""
    docstring = ""
    if isinstance(node, ast.Expr):
        node = node.value
        if isinstance(node, ast.Str):
            docstring = node.s
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            docstring = node.value
    elif isinstance(node, NODE_TYPES_WITH_DOCSTRINGS):
        docstring = ast.get_docstring(node)
    if docstring:
        node.docstring_marker = True  # type: ignore
    return docstring or ""


def split_docstring(docstring):
    """Split docstring into summary and a params section."""
    parts = docstring.split("\n\n")
    summary = parts.pop(0)
    param_sections = []
    for part in parts:
        if ":param" in part:
            param_sections.append(part)

    param_section = "\n".join(param_sections)
    return (summary, param_section)


def convert_to_placeholders(msg):
    """Convert backticks to Crowdin placeholders."""
    foundIndex = msg.find("``")
    i = 1
    while foundIndex != -1:
        if i % 2 != 0:
            msg = msg[:foundIndex] + "{{" + msg[foundIndex + 2 :]
        else:
            msg = msg[:foundIndex] + "}}" + msg[foundIndex + 2 :]
        i += 1
        foundIndex = msg.find("``")
    return msg


def format_translation_data(key, defaultMessage, description):
    return {
        key: {
            "message": convert_to_placeholders(defaultMessage),
            "description": description,
        }
    }


def get_node_type(node):
    if isinstance(node, ast.Module):
        return "module"
    if isinstance(node, ast.ClassDef):
        return "class"
    if isinstance(node, ast.FunctionDef):
        return "function"
    return "field"


def get_matched_params(node, param_section):
    pattern = re.compile(r":param(.|\n)*?(?=\n\n|:param|:return|\Z)")
    match = pattern.finditer(param_section)
    param_defs = [m.group(0).strip() for m in match]
    param_list = get_params(node)
    return match_params_to_defs(param_list, param_defs)


def get_params(node):
    params = []
    if isinstance(node, (ast.FunctionDef)):
        for arg in node.args.args:
            if arg.arg != "self":
                params.append(arg.arg)
        for arg in node.args.kwonlyargs:
            if arg.arg != "self":
                params.append(arg.arg)
        if node.args.vararg:
            if node.args.vararg.arg != "self":
                params.append("*" + node.args.vararg.arg)
    # Remove duplicates if they exist.
    return sorted(list(set(params)))


def match_params_to_defs(param_list, param_defs):
    matched = {}
    for param in param_list:
        for param_def in param_defs:
            param_def_split = param_def.split(":")
            paramFromDef = param_def_split[1].replace("param ", "")
            definition = ":".join(param_def_split[2:]).strip()
            if param == paramFromDef:
                matched.update({param: definition})
    return matched


def add_module_to_key(key, file):
    module = file.module_name
    if module and key:
        return ".".join([module, key])
    elif module and not key:
        return module
    else:
        return key


def check_param_docs(parent_key, param_list, matched_params):
    """Fail on parameters that do not have docs."""
    if len(param_list) != len(matched_params):
        raise AssertionError(parent_key, param_list, matched_params)


def save_docstrings_as_json(data):
    with open(EN_JSON_PATH, "w") as file:
        file.write(json.dumps(data, indent=2))


def crowdin_to_typeshed():
    """Entrypoint to convert from Crowdin (translated) JSON to individual typeshed files."""
    en_json = read_json(EN_JSON_PATH)
    translations_to_process = get_translated_json_files()
    stubs_to_process = get_stub_files(modules)
    for translated in translations_to_process:
        translated_json = read_json(translated)
        lang = os.path.basename(translated).split(".")[1]
        for stubs_file in stubs_to_process:
            update_docstrings(stubs_file, lang, en_json, translated_json)


def get_translated_json_files() -> list[str]:
    files_to_process: list[str] = []
    for root, dirs, files in os.walk(TRANSLATED_JSON_DIR):
        for name in files:
            if re.match(r"^api.[a-z_-]+.json$", name):
                file_path = os.path.join(root, name)
                files_to_process.append(file_path)
    return sorted(files_to_process)


def read_json(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


def update_docstrings(
    ts_file: TypeshedFile,
    lang: str,
    en_json: TranslationJSON,
    translated_json: TranslationJSON,
):
    source = get_source(ts_file.file_path)
    if not ts_file.python_file:
        save_file(source, ts_file, lang)
        return
    tree = ast.parse(source)

    class DocStringUpdater(DocStringVisitor):
        def handle_docstring(self, node: ast.AST, name: str) -> None:
            key_root = ".".join([*self.key, name])
            key = key_root
            suffix = 1
            while key in self.used_keys:
                key = f"{key_root}-{suffix}"
                suffix += 1
            self.used_keys.add(key)
            update_docstring(node, key, en_json, translated_json)

    updater = DocStringUpdater(ts_file.module_name)
    updater.visit(tree)
    data = unparse_file(tree)
    save_file(data, ts_file, lang)


def update_docstring(
    node: ast.AST, key: str, en_json: TranslationJSON, translated_json: TranslationJSON
):
    # This takes a straightforward approach and assumes we can just
    # make repeated text replacements in the docstring.
    docstring = get_docstring(node)
    if not docstring:
        return

    api_name_translated = get_string_by_key(key, translated_json)
    summary_key = ".".join([key, "summary"])
    docstring = replace_english(
        docstring,
        summary_key,
        en_json,
        translated_json,
        suffix=f" ({api_name_translated})",
    )

    _, param_section = split_docstring(docstring)
    matched_params = get_matched_params(node, param_section)
    for param_key in matched_params:
        translated_param = get_string_by_key(
            ".".join([key, "param-name", param_key]), translated_json
        )
        param_doc_key = ".".join([key, "param-doc", param_key])
        docstring = replace_english(
            docstring,
            param_doc_key,
            en_json,
            translated_json,
            prefix=f"({translated_param}) ",
        )
    replace_docstring(node, docstring)


def replace_english(
    docstring,
    parent_key,
    en_json: TranslationJSON,
    translated_json: TranslationJSON,
    prefix="",
    suffix="",
):
    string_to_replace = convert_from_placeholders(
        get_string_by_key(parent_key, en_json)
    )
    translated_string = convert_from_placeholders(
        get_string_by_key(parent_key, translated_json)
    )
    return docstring.replace(string_to_replace, prefix + translated_string + suffix)


def get_string_by_key(key: str, dict: TranslationJSON):
    return dict[key]["message"]


def replace_docstring(node, new_docstring):
    if isinstance(node, ast.Expr):
        node = node.value
        if isinstance(node, ast.Str):
            node.s = new_docstring
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = new_docstring
    elif isinstance(node, NODE_TYPES_WITH_DOCSTRINGS):
        if not (node.body and isinstance(node.body[0], ast.Expr)):
            return
        node = node.body[0].value
        if isinstance(node, ast.Str):
            node.s = new_docstring
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = new_docstring


def unparse_file(tree):
    class UnparseHack(ast._Unparser):
        def visit_Constant(self, node):
            value = node.value
            if isinstance(value, tuple):
                with self.delimit("(", ")"):
                    self.items_view(self._write_constant, value)
            elif value is ...:
                self.write("...")
            else:
                if hasattr(node, "docstring_marker"):
                    self._write_str_avoiding_backslashes(
                        value, quote_types=ast._MULTI_QUOTES
                    )
                    return
                if node.kind == "u":
                    self.write("u")
                self._write_constant(node.value)

    unparser = UnparseHack()
    return unparser.visit(tree)


def convert_from_placeholders(data):
    """Convert Crowdin placeholders to backticks."""
    return data.replace("{{", "``").replace("}}", "``")


def save_file(data, file, lang):
    output_dir = os.path.join(DIR, "..", f"lang/{lang}/typeshed/stdlib")
    file_path = os.path.join(output_dir, file.file_path.split("stdlib/")[-1])
    checked_path_list = []
    for path_segment in file_path.split("/"):
        maybe_dir("/".join(checked_path_list))
        checked_path_list.append(path_segment)

    with open(file_path, "w") as file:
        file.write(data)


def maybe_dir(maybe_path):
    if not maybe_path:
        return
    if not os.path.exists(maybe_path):
        os.mkdir(maybe_path)


if __name__ == "__main__":
    operation = sys.argv[1]
    if operation == "typeshed-to-crowdin":
        typeshed_to_crowdin()
    elif operation == "crowdin-to-typeshed":
        crowdin_to_typeshed()
    else:
        print(f"Invalid operation: {operation}", file=sys.stderr)
        sys.exit(1)
