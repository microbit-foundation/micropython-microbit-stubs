import shutil
import subprocess
import os.path
import sys

def copy_file(src_path, dest_path, **replacements):
    with open(src_path, "tr") as src:
        with open(dest_path, "tw") as dst:
            content = src.read()
            for key in replacements:
                content = content.replace("{" + key + "}", replacements[key])
            dst.write(content)


dist_dir = os.path.abspath("dist")
all_langs_dir = os.path.join("..", "..", "lang")
template_files = ["pyproject.toml", "README.md"]
for lang in os.listdir(all_langs_dir):
    if lang == ".DS_Store":
        continue

    lang_dir = os.path.join(all_langs_dir, lang)
    for name in template_files:
        copy_file(os.path.join("templates", name), os.path.join(lang_dir, name), lang=lang)

    copy_file("../../LICENSE.md", os.path.join(lang_dir, "LICENSE.md"))

    subprocess.run([sys.executable, "-m", "build", "--wheel", "--outdir", "dist", lang_dir])

    # clean up
    for name in template_files + [
            "LICENSE.md", "build", f"micropython_microbit_stubs_{lang.replace('-', '_')}.egg-info"]:
        full_path = os.path.join(lang_dir, name)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            os.remove(full_path)

