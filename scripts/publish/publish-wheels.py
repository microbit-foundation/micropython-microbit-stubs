import subprocess
import sys

subprocess.run([sys.executable, "-m", "twine", "upload", "dist/*.whl", "-u", "__token__"])
