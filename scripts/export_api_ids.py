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
from crowdin_convert import (
    get_stub_files,
    DIR,
    TypeshedFile,
    get_source,
    DocStringVisitor,
)

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


def export_api_ids():
    data_list = []
    files_to_process = get_stub_files()
    for ts_file in files_to_process:
        if not ts_file.python_file:
            continue
        data_list = data_list + get_api_ids(ts_file)
    # Remove overloads.
    data_list = list(set(data_list))
    data_list.sort()
    data = {"apiIds": data_list}
    save_api_ids(data)
    pass


def save_api_ids(data):
    with open(os.path.join(DIR, "../", "api-ids.json"), "w") as file:
        file.write(json.dumps(data, indent=2))


def checkModuleRequired(module_name):
    if module_name in modules:
        return True
    if "microbit" in module_name:
        return True
    return False


def get_api_ids(ts_file: TypeshedFile):
    source = get_source(ts_file.file_path)
    tree = ast.parse(source)

    class DocStringCollector(DocStringVisitor):
        def __init__(self):
            super().__init__(ts_file.module_name)
            self.data: list[str] = []

        def handle_docstring(self, node: ast.AST, name: str) -> None:
            key = ".".join([*self.key, name])
            if checkModuleRequired(ts_file.module_name):
                self.data.append(key)

    collector = DocStringCollector()
    collector.visit(tree)
    return collector.data


if __name__ == "__main__":
    export_api_ids()