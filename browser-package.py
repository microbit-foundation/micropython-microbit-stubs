#!/usr/bin/env python3
"""
Outputs a JSON file containing all the stubs and a Pyright config file.

This is intended for web apps that need the stubs client side.
"""
import os
import json


def create_typeshed_JSON(source_path, lang):
    results = dict(files={})
    for (source, prefix) in ((source_path, "/typeshed/"), ("config", "/src/")):
        for (dirpath, dirnames, filenames) in os.walk(source):
            for f in sorted(filenames):
                path = os.path.join(dirpath, f)
                try:
                    destination = os.path.join(
                        prefix, os.path.join(*path.split(os.path.sep)[3:])
                    )
                except:
                    # Correct destination for config file.
                    destination = os.path.join(
                        prefix, os.path.join(*path.split(os.path.sep)[1:])
                    )
                print(f"{path} -> {destination}")
                text = open(path, "r", encoding="utf-8").read()
                results["files"][destination] = text

    with open(f"typeshed.{lang}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(results, indent=2))


for (dirpath, dirnames, filenames) in os.walk("lang"):
    for dirname in dirnames:
        source_path = os.path.join(dirpath, dirname, "typeshed")
        create_typeshed_JSON(source_path, dirname)
    break
