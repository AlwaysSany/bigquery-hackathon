#!/usr/bin/env python
import sys
import nbformat
from pathlib import Path

def clean_widgets(file_path):
    nb = nbformat.read(file_path, as_version=4)
    modified = False
    for cell in nb.cells:
        if "widgets" in cell.metadata:
            del cell.metadata["widgets"]
            modified = True
    if modified:
        nbformat.write(nb, file_path)
        print(f"Stripped widgets in: {file_path}")

if __name__ == "__main__":
    for file in sys.argv[1:]:
        if file.endswith(".ipynb") and Path(file).exists():
            clean_widgets(file)
