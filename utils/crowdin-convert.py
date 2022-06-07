"""
    Creates api.en.json file in Crowdin's format
    containing translatable parts of the API
    produced from the type stubs files.
    Inclues first line of docstring (summary),
    parameter names and parameter docs.
"""

import ast
from dataclasses import dataclass
import os
import json
import re
import sys

from typing import Any

from typing import Optional

NODE_TYPES_WITH_DOCSTRINGS = (ast.FunctionDef, ast.Module, ast.ClassDef)
DIR = os.path.dirname(__file__)


def typeshed_to_crowdin():
    data = {}
    files_to_process = get_stub_files()
    for ts_file in files_to_process:
        if not ts_file.python_file:
            continue
        data.update(get_docstrings_dict(ts_file))
    save_docstrings_as_json(data)


@dataclass
class TypeshedFile:
    file_path: str
    module_name: str
    python_file: bool


def get_stub_files() -> list[TypeshedFile]:
    top = os.path.join(DIR, "..", "lang/en/typeshed/stdlib")
    files_to_process: list[TypeshedFile] = []
    for root, dirs, files in os.walk(top):
        for name in files:
            file_path = os.path.join(root, name)
            # Skip audio stubs file that imports from microbit audio (so we don't include its docstring)
            if (
                os.path.basename(os.path.dirname(file_path)) != "microbit"
                and name == "audio.pyi"
            ):
                continue
            if name.endswith(".pyi"):
                files_to_process.append(
                    TypeshedFile(
                        file_path=file_path,
                        module_name=module_name_for_path(file_path),
                        python_file=True,
                    )
                )
            else:
                files_to_process.append(
                    TypeshedFile(
                        file_path=file_path,
                        module_name="",
                        python_file=False,
                    )
                )
    return sorted(files_to_process, key=lambda x: x.file_path)


def module_name_for_path(file_path: str):
    """Hacky determination of the module name used as a translation key."""
    name = os.path.basename(file_path)
    in_microbit_package = os.path.basename(os.path.dirname(file_path)) == "microbit"
    if in_microbit_package:
        if name == "__init__.pyi":
            return "microbit"
        return ".".join(["microbit", os.path.splitext(name)[0]])
    return os.path.splitext(name)[0]


def get_docstrings_dict(ts_file: TypeshedFile):
    source = get_source(ts_file.file_path)
    tree = ast.parse(source)

    class DocStringCollector(ast.NodeVisitor):
        def __init__(self):
            self.key = []
            self.used_keys = set()
            self.preceding: Optional[str] = None
            # Translation key to dict with message/description fields.
            self.data: dict[str, dict[str, str]] = {}

        def visit_Module(self, node: ast.Module) -> Any:
            name = ts_file.module_name
            self.add_entries_for_node(node, name)

            self.key.append(name)
            self.generic_visit(node)
            self.key.pop()

        def visit_ClassDef(self, node):
            name = node.name
            self.add_entries_for_node(node, name)

            self.key.append(name)
            self.generic_visit(node)
            self.key.pop()

        def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
            self.preceding = None
            self.add_entries_for_node(node, node.name)

        def visit_AnnAssign(self, node: ast.AnnAssign) -> Any:
            self.preceding = node.target.id  # type: ignore

        def visit_Assign(self, node: ast.Assign) -> Any:
            if len(node.targets) != 1:
                raise AssertionError()
            self.preceding = node.targets[0].id  # type: ignore

        def visit_Expr(self, node: ast.Expr) -> Any:
            if self.preceding:
                self.add_entries_for_node(node, self.preceding)

        def generic_visit(self, node: ast.AST) -> Any:
            self.preceding = None
            return super().generic_visit(node)

        def add_entries_for_node(self, node: ast.AST, name: str) -> None:
            key_root = ".".join([*self.key, name])
            key = key_root
            suffix = 1
            while key in self.used_keys:
                key = f"{key_root}-{suffix}"
                suffix += 1
            self.used_keys.add(key)
            self.data.update(get_entries(node, name, key))

    collector = DocStringCollector()
    collector.visit(tree)
    return collector.data


def get_source(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_entries(node, name, key):
    entries = {}
    docstring = get_docstring(node)
    summary, param_section = split_docstring(docstring)
    # We don't want to translate param names if we have no summary.
    if not summary:
        return {}
    if not isinstance(node, ast.Module):
        api_call_for_translation = name.replace("_", " ").strip()
        entries.update(
            format_translation_data(
                key,
                api_call_for_translation,
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
                param_key,
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
                matched = {**matched, param: definition}
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
    file_name = os.path.join(DIR, "lang/api.en.json")
    with open(file_name, "w") as file:
        file.write(json.dumps(data, indent=2))


# ==============================================================
# Additional functions for translating stubs files.
en_json = {}
translated_json = {}


def crowdin_to_typeshed():
    global en_json
    global translated_json
    en_json = read_json(os.path.join(DIR, "lang/api.en.json"))
    translations_to_process = get_translated_json_files()
    stubs_to_process = get_stub_files()
    for translated in translations_to_process:
        translated_json = read_json(translated)
        lang = os.path.basename(translated).split(".")[1]
        for stubs_file in stubs_to_process:
            update_docstrings(stubs_file, lang)


def get_translated_json_files() -> list[str]:
    top = os.path.join(DIR, "lang")
    files_to_process: list[str] = []
    for root, dirs, files in os.walk(top):
        for file in files:
            file_path = os.path.join(root, file)
            if file == "api.en.json":
                continue
            files_to_process.append(file_path)
    return sorted(files_to_process)


def read_json(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


# Needs refactoring with get_docstrings_dict
def update_docstrings(file, lang):
    source = get_source(file.file_path)
    if not file.python_file:
        save_file(source, file, lang)
        return
    tree = ast.parse(source)
    key = ""
    skip_key = False
    line_num = 0
    for node in ast.walk(tree):
        if hasattr(node, "lineno"):
            end_of_file = node.lineno < line_num
            line_num = node.lineno
            # Stop when we reach the end of the file.
            if end_of_file:
                break

        if isinstance(node, ast.ClassDef):
            key, skip_key = process_node_write(file, node, key, skip_key)
            class_name = key
            # Walk over nested class methods to retain association
            # with class name.
            for node in node.body:
                key, skip_key = process_node_write(
                    file, node, key, skip_key, class_name
                )
        else:
            key, skip_key = process_node_write(file, node, key, skip_key)
    data = unparse_file(tree)
    save_file(data, file, lang)


# Needs refactoring with process_node_read
def process_node_write(file, node, key, skip_key, class_name=""):
    if not skip_key:
        assignment_key, class_func_key = get_key(node, class_name)
        if assignment_key:
            key = assignment_key
            skip_key = True
            # We get the docstring from the Expr node
            # in the next iteration.
            return key, skip_key
        elif class_func_key:
            key = class_func_key
        elif isinstance(node, ast.Module):
            key = ""
        else:
            # No key, so not something we care about.
            return "", skip_key

    skip_key = False
    update_docstring(node, add_module_to_key(key, file))
    return key, skip_key


def update_docstring(node, parent_key):
    docstring = get_docstring(node)
    if not docstring:
        return {}

    if not isinstance(node, ast.Module):
        docstring = mutate_docstring(docstring, parent_key)

    summary_key = ".".join([parent_key, "summary"])
    docstring = mutate_docstring(docstring, summary_key)
    _, param_section = split_docstring(docstring)
    matched_params = get_matched_params(node, param_section)
    # check_param_docs(parent_key, param_list, matched_params)
    for key in matched_params:
        # Translate param name.
        # We need to know how exactly to place this in the stubs.
        # param_name_key = ".".join([parent_key, "param-name", key])
        # Translate param doc.
        param_doc_key = ".".join([parent_key, "param-doc", key])
        docstring = mutate_docstring(docstring, param_doc_key)
    replace_docstring(node, docstring)


def mutate_docstring(docstring, parent_key):
    string_to_replace = convertFromPlaceholders(get_string_by_key(parent_key, en_json))
    translated_string = convertFromPlaceholders(
        get_string_by_key(parent_key, translated_json)
    )
    return docstring.replace(string_to_replace, translated_string)


def get_string_by_key(key, dict):
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
        def _write_constant(self, value):
            # Hack targetting pseudo docstrings used for constants/fields.
            # Assume all strings are docstrings as we have no others and force triple quotes.
            if isinstance(value, str):
                self._write_str_avoiding_backslashes(
                    value, quote_types=ast._MULTI_QUOTES
                )
            else:
                super()._write_constant(value)

    unparser = UnparseHack()
    return unparser.visit(tree)


def convertFromPlaceholders(data):
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
