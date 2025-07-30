import os

import minify_html

os.makedirs("./dist", exist_ok=True)
with open("./index.html", "r", encoding="utf-8") as f:
    minified = minify_html.minify(f.read(), minify_js=True, minify_css=True, remove_processing_instructions=True, minify_doctype=True)
    with open("./dist/index.html", "w", encoding="utf-8") as f:
        f.write(minified)