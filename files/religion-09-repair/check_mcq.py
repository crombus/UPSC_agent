"""Validate the 32-item diagnostic block: key sequence, balance and option lengths."""
import re
import statistics
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
TEXT = (BASE / "part-06-mcq-01-12.md").read_text(encoding="utf-8") + \
       (BASE / "part-07-mcq-13-32.md").read_text(encoding="utf-8")

EXPECTED_KEY = "CBACADBDCBDACDBADADCABCBDBACBCAD"

blocks = re.split(r"^#### MCQ (\d+)\. ", TEXT, flags=re.M)[1:]
items = list(zip(blocks[0::2], blocks[1::2]))
print("items found:", len(items))

key = ""
opt_lengths = {"correct": [], "distractor": []}
problems = []
longest_correct = shortest_correct = 0

for num, body in items:
    ans = re.search(r"\*\*Answer: ([A-D])\.\*\*", body)
    if not ans:
        problems.append(f"MCQ {num}: no answer line")
        continue
    letter = ans.group(1)
    key += letter
    opts = dict(re.findall(r"^([A-D])\. (.+)$", body, flags=re.M))
    if len(opts) != 4:
        problems.append(f"MCQ {num}: {len(opts)} options")
        continue
    lens = {k: len(v) for k, v in opts.items()}
    opt_lengths["correct"].append(lens[letter])
    for k, v in lens.items():
        if k != letter:
            opt_lengths["distractor"].append(v)
    if lens[letter] == max(lens.values()):
        longest_correct += 1
    if lens[letter] == min(lens.values()):
        shortest_correct += 1
    expl = re.findall(r"^- \*\*([A-D]):\*\* ", body, flags=re.M)
    if sorted(expl) != list("ABCD"):
        problems.append(f"MCQ {num}: option explanations {expl}")
    trap = re.search(rf"\*\*Examiner trap {num}:\*\*", body)
    if not trap:
        problems.append(f"MCQ {num}: missing/incorrectly numbered examiner trap")

print("key       :", key)
print("expected  :", EXPECTED_KEY)
print("key match :", key == EXPECTED_KEY)
print("counts    :", {c: key.count(c) for c in "ABCD"})
print("blocks    :", [key[i:i + 8] for i in range(0, 32, 8)])
print("block bal :", all(key[i:i + 8].count(c) == 2
                         for i in range(0, 32, 8) for c in "ABCD"))
print("adjacent  :", all(a != b for a, b in zip(key, key[1:])))
grams = [key[i:i + 4] for i in range(len(key) - 3)]
rot = {s for s in ("ABCD", "BCDA", "CDAB", "DABC")}
rot |= {s[::-1] for s in rot}
print("no rotation window:", not any(g in rot for g in grams))
print("no repeated 4-gram:", len(set(grams)) == len(grams))
print("mean correct len  :", round(statistics.mean(opt_lengths["correct"]), 1))
print("mean distractor   :", round(statistics.mean(opt_lengths["distractor"]), 1))
print("correct is longest in :", longest_correct, "of 32")
print("correct is shortest in:", shortest_correct, "of 32")
print("total option explanations:", len(re.findall(r"^- \*\*[A-D]:\*\* ", TEXT, flags=re.M)))
print("total examiner traps     :", len(re.findall(r"\*\*Examiner trap \d+:\*\*", TEXT)))
traps = re.findall(r"\*\*Examiner trap \d+:\*\* (.+)", TEXT)
print("unique traps             :", len(set(traps)))
stems = [re.split(r"\n", b.strip())[0] for _, b in items]
print("unique MCQ titles        :", len(set(n for n, _ in items)))
if problems:
    print("PROBLEMS:")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print("ALL STRUCTURAL CHECKS PASS")
