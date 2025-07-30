import os
import subprocess

import minify_html

def get_git_commit_hash() -> str:
    cwd = os.path.dirname(os.path.abspath(__file__))
    out = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=cwd)
    return out.strip().decode('ascii')

os.makedirs("./dist", exist_ok=True)
with open("./index.html", "r", encoding="utf-8") as f:
    content = f.read().replace("[build]", get_git_commit_hash())
    try:
        minified = minify_html.minify(content.replace("[isMinified]", "true"), minify_js=True, minify_css=True, remove_processing_instructions=True, keep_comments=True)
    except:  # noqa: E722
        minified = content.replace("[isMinified]", "false")
    with open("./dist/index.html", "w", encoding="utf-8") as f:
        f.write(minified)
