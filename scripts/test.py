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
    subprocess.check_call(
        ["pyright", "-p", "test-pyrightconfig.json", "--typeshed-path", typeshed]
    )
