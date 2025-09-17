#!/usr/bin/env python
import sys
import nbformat
from pathlib import Path

def fix_widgets(file_path):
    nb = nbformat.read(file_path, as_version=4)
    modified = False
    for cell in nb.cells:
        widgets = cell.metadata.get("widgets")
        if widgets is not None:
            if "state" not in widgets:
                widgets["state"] = {}
                modified = True
    if modified:
        nbformat.write(nb, file_path)
        print(f"Fixed widgets in: {file_path}")

if __name__ == "__main__":
    for file in sys.argv[1:]:
        if file.endswith(".ipynb") and Path(file).exists():
            fix_widgets(file)
