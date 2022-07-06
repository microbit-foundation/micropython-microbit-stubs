"""
    Functions, types and variables
    shared with various scripts.
    Including:
        crowdin_convert.py
        export_api_ids.py
"""

from dataclasses import dataclass
import os
import ast
from typing import Any
from typing import Optional

DIR = os.path.dirname(__file__)


@dataclass
class TypeshedFile:
    file_path: str
    module_name: str
    python_file: bool


def get_source(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def module_name_for_path(file_path: str):
    """Hacky determination of the module name."""
    name = os.path.basename(file_path)
    in_microbit_package = os.path.basename(os.path.dirname(file_path)) == "microbit"
    if in_microbit_package:
        if name == "__init__.pyi":
            return "microbit"
        return ".".join(["microbit", os.path.splitext(name)[0]])
    return os.path.splitext(name)[0]


def get_stub_files() -> list[TypeshedFile]:
    top = os.path.join(DIR, "..", "lang/en/typeshed/stdlib")
    files_to_process: list[TypeshedFile] = []
    for root, dirs, files in os.walk(top):
        for name in files:
            file_path = os.path.join(root, name)
            # Skip audio stubs file that imports from microbit audio
            # (so we don't include its docstring)
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


class DocStringVisitor(ast.NodeVisitor):
    def __init__(self, module_name):
        self.module_name = module_name
        self.key = []
        self.used_keys = set()
        self.preceding: Optional[str] = None

    def visit_Module(self, node: ast.Module) -> Any:
        name = self.module_name
        self.handle_docstring(node, name)

        self.key.append(name)
        self.generic_visit(node)
        self.key.pop()

    def visit_ClassDef(self, node):
        name = node.name
        self.handle_docstring(node, name)

        self.key.append(name)
        self.generic_visit(node)
        self.key.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef) -> Any:
        self.preceding = None
        self.handle_docstring(node, node.name)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> Any:
        self.preceding = node.target.id  # type: ignore

    def visit_Assign(self, node: ast.Assign) -> Any:
        if len(node.targets) != 1:
            raise AssertionError()
        self.preceding = node.targets[0].id  # type: ignore

    def visit_Expr(self, node: ast.Expr) -> Any:
        if self.preceding:
            self.handle_docstring(node, self.preceding)

    def generic_visit(self, node: ast.AST) -> Any:
        self.preceding = None
        return super().generic_visit(node)

    def handle_docstring(self, node: ast.AST, name: str) -> None:
        raise NotImplementedError()
