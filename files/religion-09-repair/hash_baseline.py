"""Hash every Philosophy of Religion file inside the three locked directories.

Topic 09 files are recorded separately (they are the only permitted edits).
All other topic files must remain byte-identical after the repair.
"""
import hashlib
import json
import os
import sys

ROOT = r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent"

LOCKED_DIRS = [
    os.path.join(ROOT, "learning_package_final", "Philosophy-Optional",
                 "Philosophy-Paper-II-\u2014-Philosophy-of-Religion"),
    os.path.join(ROOT, "notes", "Final-Learning-Packages", "Philosophy Optional",
                 "Philosophy Paper II \u2014 Philosophy of Religion"),
    os.path.join(ROOT, "quick_galance", "Philosophy"),
]

TOPIC09_MARKERS = ("09-Religious-Pluralism-and-Absolute-Truth",
                   "09-Religious-7556c0ef-Truth",
                   "philosophy-paper-ii-philosophy-of-religion-09_Tree-Chart.md")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def collect():
    others, topic09 = {}, {}
    for base in LOCKED_DIRS:
        for dirpath, _dirnames, filenames in os.walk(base):
            for name in filenames:
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, ROOT)
                target = topic09 if any(m in rel for m in TOPIC09_MARKERS) else others
                target[rel] = sha256(full)
    return others, topic09


if __name__ == "__main__":
    out = sys.argv[1]
    others, topic09 = collect()
    with open(out, "w", encoding="utf-8") as fh:
        json.dump({"protected": others, "topic09": topic09}, fh,
                  indent=1, sort_keys=True)
    print("protected files:", len(others))
    print("topic09 files  :", len(topic09))
