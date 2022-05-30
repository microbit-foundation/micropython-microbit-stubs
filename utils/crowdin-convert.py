"""
    Creates api.en.json file in CrowdIn's format
    containing translatable parts of the API
    produced from the type stubs files.
    Inclues first line of docstring (summary),
    parameter names and parameter docs.
"""

import ast
import os
import json
import re

NODE_TYPES_WITH_DOCSTRINGS = (ast.FunctionDef, ast.Module, ast.ClassDef)
DIR = os.path.dirname(__file__)


def get_translation_JSON():
    data = {}
    files_to_process = get_stub_files()
    for file in files_to_process:
        data = {**data, **get_docstrings_dict(file)}
    save_docstrings_as_json(data)


def get_stub_files():
    top = os.path.join(DIR, "..", "typeshed/stdlib")
    files_to_process = []
    for root, dirs, files in os.walk(top):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip audio stubs file that imports from microbit audio.
            if (
                os.path.basename(os.path.dirname(file_path)) != "microbit"
                and file == "audio.pyi"
            ):
                continue
            if file.endswith(".pyi"):
                module_name = ""
                file_name = ""

                if file != "__init__.pyi":
                    file_name = file.replace(".pyi", "")
                if (
                    os.path.basename(os.path.dirname(file_path)) == "microbit"
                    and file_name
                ):
                    module_name = ".".join(["microbit", file_name])
                elif (
                    os.path.basename(os.path.dirname(file_path)) == "microbit"
                    and not file_name
                ):
                    module_name = "microbit"
                else:
                    module_name = file_name
                files_to_process.append(
                    {
                        "file_name": file,
                        "file_path": file_path,
                        "module_name": module_name,
                    }
                )
    return files_to_process


def get_docstrings_dict(file):
    source = get_source(file["file_path"])
    tree = ast.parse(source)
    data = {}
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
            key, skip_key, data = process_node_read(file, data, node, key, skip_key)
            class_name = key
            # Walk over nested class methods to retain association
            # with class name.
            for node in node.body:
                key, skip_key, data = process_node_read(
                    file, data, node, key, skip_key, class_name
                )
        else:
            key, skip_key, data = process_node_read(file, data, node, key, skip_key)
    return data


def get_source(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def process_node_read(file, data, node, key, skip_key, class_name=""):
    if not skip_key:
        assignment_key, class_func_key = get_key(node, class_name)
        if assignment_key:
            key = assignment_key
            skip_key = True
            # We get the docstring from the Expr node
            # in the next iteration.
            return key, skip_key, data
        elif class_func_key:
            key = class_func_key
        elif isinstance(node, ast.Module):
            key = ""
        else:
            # No key, so not something we care about.
            return "", skip_key, data

    skip_key = False
    entry = get_entries(node, add_module_to_key(key, file))
    data = {**data, **entry}
    return key, skip_key, data


def get_key(node, class_name):
    """Get field or function name and concatenate with correct
    class name where appropriate."""
    assignmentKey = ""
    classFuncKey = ""
    if isinstance(node, ast.AnnAssign):
        child = ""
        parent = ""
        if hasattr(node.target, "id"):
            child = node.target.id
        if hasattr(node.annotation, "id"):
            parent = node.annotation.id
        if class_name and child:
            assignmentKey = f"{class_name}.{child}"
        elif parent and child:
            assignmentKey = f"{parent}.{child}"
        else:
            assignmentKey = child

    if isinstance(node, ast.Assign):
        child = node.targets[0].id
        if class_name and child:
            assignmentKey = f"{class_name}.{child}"
        else:
            assignmentKey = child
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
        if class_name:
            classFuncKey = f"{class_name}.{node.name}"
        else:
            classFuncKey = node.name
    return assignmentKey, classFuncKey


def get_entries(node, parent_key):
    entries = {}
    docstring = get_docstring(node)
    summary, param_section = split_docstring(docstring)
    # We don't want to translate param names if we have no summary.
    if not summary:
        return {}
    if not isinstance(node, ast.Module):
        parent_message = parent_key.split(".")[-1].replace("_", " ").strip()
        entries = {
            **entries,
            **format_translation_data(
                parent_key, parent_message, f"({get_node_type(node)} name) {summary}"
            ),
        }
    summary_key = ".".join([parent_key, "summary"])
    entries = {**entries, **format_translation_data(summary_key, summary, summary)}
    matched_params = get_matched_params(node, param_section)
    # check_param_docs(parent_key, param_list, matched_params)
    for key in matched_params:
        # Translate param name.
        param_name_key = ".".join([parent_key, "param-name", key])
        entries = {
            **entries,
            **format_translation_data(
                param_name_key, key, f"(parameter name) {matched_params[key]}"
            ),
        }
        # Translate param doc.
        param_doc_key = ".".join([parent_key, "param-doc", key])
        entries = {
            **entries,
            **format_translation_data(
                param_doc_key, matched_params[key], "Parameter docs"
            ),
        }
    return entries


def get_docstring(node):
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


def format_translation_data(key, defaultMessage, description):
    return {key: {"message": defaultMessage, "description": description}}


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
    return params


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
    module = file["module_name"]
    if module and key:
        return ".".join([module, key])
    elif module and not key:
        return module
    else:
        return key


def check_param_docs(parent_key, param_list, matched_params):
    """Finds parameters that do not have docs"""
    if len(param_list) != len(matched_params):
        print(parent_key, param_list, matched_params)


def save_docstrings_as_json(data):
    file_name = os.path.join(DIR, "lang/api.en.json")
    with open(file_name, "w") as file:
        file.write(json.dumps(data))


# ==============================================================
# Additional functions for translating stubs files.
en_json = {}
translated_json = {}


def translate_stubs():
    global en_json
    global translated_json
    en_json = get_JSON_file_content(os.path.join(DIR, "lang/api.en.json"))
    translations_to_process = get_translated_JSON_files()
    stubs_to_process = get_stub_files()
    for translation in translations_to_process:
        translated_json = get_JSON_file_content(translation["file_path"])
        lang = translation["file_name"].split(".")[1]
        for stubs_file in stubs_to_process:
            update_docstrings(stubs_file, lang)


def get_translated_JSON_files():
    top = os.path.join(DIR, "lang")
    files_to_process = []
    for root, dirs, files in os.walk(top):
        for file in files:
            file_path = os.path.join(root, file)
            if file == "api.en.json":
                continue
            files_to_process.append(
                {
                    "file_name": file,
                    "file_path": file_path,
                }
            )
    return files_to_process


def get_JSON_file_content(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)


# Needs refactoring with get_docstrings_dict
def update_docstrings(file, lang):
    source = get_source(file["file_path"])
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

    # So far we should have modules and summary done

    # Now for params:
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
    string_to_replace = get_string_by_key(parent_key, en_json)
    translated_string = get_string_by_key(parent_key, translated_json)
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


def save_file(data, file, lang):
    output_dir = os.path.join(DIR, f"stubs_output_test/{lang}/stdlib")
    file_path = os.path.join(output_dir, file["file_path"].split("stdlib/")[-1])
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


# get_translation_JSON()
translate_stubs()
