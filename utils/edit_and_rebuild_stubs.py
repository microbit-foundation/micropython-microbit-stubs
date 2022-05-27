"""
    File acts as proof of concept for editing docstrings in the simplest way.
    Source file is read, parsed, edited, unparsed and saved.
    ast.unparse() is used to unparse the edited tree and is only available
    in Python 3.9^.
"""

import ast
from os import path

script_dir = path.dirname(__file__)
rel_path = "typeshed/stdlib/microbit/__init__.pyi"
abs_file_path = path.join(script_dir, "..", rel_path)

node_types_with_docstrings = (ast.FunctionDef, ast.Module, ast.ClassDef)


def get_source():
    with open(abs_file_path, "r") as file:
        return file.read()


def walk_tree_update_docstrings():
    tree = ast.parse(get_source())
    for node in ast.walk(tree):
        update_docstring(node, "Docstring replaced by this message for testing.")
    return tree


def update_docstring(node, new_docstring):
    # There is improved logic in get_stubs_as_json.py
    # but not important here.
    if isinstance(node, ast.AnnAssign):
        try:
            parent = node.annotation.id
            child = node.target.id
            return parent + "." + child
        except:
            pass
    if isinstance(node, ast.Expr):
        node = node.value
        if isinstance(node, ast.Str):
            node.s = new_docstring
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = new_docstring
    if isinstance(node, node_types_with_docstrings):
        if not (node.body and isinstance(node.body[0], ast.Expr)):
            return ""
        node = node.body[0].value
        if isinstance(node, ast.Str):
            node.s = new_docstring
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            node.value = new_docstring
    return ""


def compile_python(tree):
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


def save_python_file(string_file):
    file_name = path.join(script_dir, "docstring_edit_test.pyi")
    with open(file_name, "w") as file:
        file.write(string_file)


def save_edited_docstrings():
    tree = walk_tree_update_docstrings()
    string_file = compile_python(tree)
    save_python_file(string_file)


save_edited_docstrings()
