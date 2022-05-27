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


def get_source(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


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


def get_node_type(node):
    if isinstance(node, ast.ClassDef):
        return "class"
    if isinstance(node, ast.FunctionDef):
        return "function"
    return "field"


def format_translation_data(key, defaultMessage, description):
    return {key: {"message": defaultMessage, "description": description}}


def check_param_docs(parent_key, param_list, matched_params):
    """Finds parameters that do not have docs"""
    if len(param_list) != len(matched_params):
        print(parent_key, param_list, matched_params)


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
    pattern = re.compile(r":param(.|\n)*?(?=\n\n|:param|:return|\Z)")
    match = pattern.finditer(param_section)
    param_defs = [m.group(0).strip() for m in match]
    param_list = get_params(node)
    matched_params = match_params_to_defs(param_list, param_defs)
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


def process_node(file, data, node, key, skip_key, class_name=""):
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
            key, skip_key, data = process_node(file, data, node, key, skip_key)
            class_name = key
            # Walk over nested class methods to retain association
            # with class name.
            for node in node.body:
                key, skip_key, data = process_node(
                    file, data, node, key, skip_key, class_name
                )
        else:
            key, skip_key, data = process_node(file, data, node, key, skip_key)
    return data


def save_docstrings_as_json(data):
    file_name = os.path.join(DIR, "api.en.json")
    with open(file_name, "w") as file:
        file.write(json.dumps(data))


def run():
    data = {}
    files_to_process = get_stub_files()
    for file in files_to_process:
        data = {**data, **get_docstrings_dict(file)}
    save_docstrings_as_json(data)


run()
