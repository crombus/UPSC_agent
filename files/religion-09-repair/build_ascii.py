"""Assemble and validate the ASCII master flow diagram for Philosophy of Religion 09."""
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
a = (BASE / "ascii-part-a.txt").read_text(encoding="utf-8")
b = (BASE / "ascii-part-b.txt").read_text(encoding="utf-8")
text = a.rstrip("\n") + "\n" + b.lstrip("\n")
text = text.rstrip("\n") + "\n"

lines = text.split("\n")
panels = re.findall(r"^ASCII MASTER FLOW — PANEL (\d+)/31: ", text, flags=re.M)
bad = [(i + 1, len(l)) for i, l in enumerate(lines) if len(l) > 100]
nonascii = sorted({c for c in text if ord(c) > 127})
tabs = [i + 1 for i, l in enumerate(lines) if "\t" in l]

print("panels found      :", len(panels))
print("panel numbers ok  :", panels == [str(i) for i in range(1, 32)])
print("total lines       :", len(lines))
print("max line length   :", max(len(l) for l in lines))
print("over-100 lines    :", bad or "none")
print("non-ascii chars   :", nonascii)
print("tab characters    :", tabs or "none")

out = BASE / "ASCII-Master-Flowchart.txt"
out.write_text(text, encoding="utf-8")
print("bytes             :", out.stat().st_size)

if bad or tabs or panels != [str(i) for i in range(1, 32)] or nonascii != ["—"]:
    sys.exit(1)
print("ASCII MASTER OK")
