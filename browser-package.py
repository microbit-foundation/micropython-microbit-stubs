"""
Outputs a JSON file containing all the stubs and a Pyright config file.

This is intended for web apps that need the stubs client side.
"""
import os
import json

results = dict(files={})
for (source, prefix) in (("stubs", "/stubs"), ("config", "/")):
  for (dirpath, dirnames, filenames) in os.walk(source):
      for f in sorted(filenames):
        path = os.path.join(dirpath, f)
        destination = os.path.join(prefix, os.path.join(*path.split(os.path.sep)[1:]))
        print(path + " -> " + destination)
        text = open(path, "r").read()
        results["files"][destination] = text

with open("typeshed.json", "w") as f:
  f.write(json.dumps(results))