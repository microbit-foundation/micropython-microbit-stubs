#!/usr/bin/env python3
import json
import os
import subprocess
import sys


languages = os.listdir("lang")
for language in languages:
    typeshed = f"./lang/{language}/typeshed/"
    print(f"Testing typeshed at {typeshed} for language {language}")
    sys.stdout.flush()
    examples = [d for d in os.listdir("examples") if language == "en" or d != "en-only"]
    example_paths = [os.path.join("examples", d) for d in examples]
    subprocess.check_call(
        [
            "pyright",
            "-p",
            "test-pyrightconfig.json",
            "--typeshed-path",
            typeshed,
            *example_paths,
        ]
    )
