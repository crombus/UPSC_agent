from pathlib import Path
from difflib import SequenceMatcher
from collections import Counter
import re

ROOT = Path(__file__).parent
FORBIDDEN = [
    "chronology and constituency cease", "institutionally identical to adjacent",
    "record permits moving", "safest conclusion", "proves a single, internally uniform",
    "with chronology and institutional ownership", "without collapsing method",
    "while separating the immediate programme", "source of authority and social reach treated",
    "coaching key", "reproduction permission", "Topic 09", "PYQ control",
]

def parse_questions(path):
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^### Q(\d+)\. ", text)[1:]
    items = []
    for i in range(0, len(blocks), 2):
        no, body = int(blocks[i]), blocks[i + 1]
        opts = re.findall(r"(?m)^([A-D])\. (.+)$", body)
        stem = body.split("\n\nA. ", 1)[0].strip()
        items.append((no, stem, dict(opts)))
    return text, items

def parse_answers(path):
    text = path.read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^### Q(\d+)\. ([A-D])\s*$", text)[1:]
    items = []
    for i in range(0, len(blocks), 3):
        no, key, body = int(blocks[i]), blocks[i + 1], blocks[i + 2]
        items.append((no, key, body))
    return text, items

all_stems = []
all_options = []
keys_by_rev = {}
findings = []
question_map = {}
answer_map = {}

for rev in ("revision-1", "revision-2", "revision-3"):
    qtext, qs = parse_questions(ROOT / rev / "QUESTIONS.md")
    atext, ans = parse_answers(ROOT / rev / "ANSWERS.md")
    if len(qs) != 45 or len(ans) != 45:
        findings.append(f"{rev}: count {len(qs)}/{len(ans)}")
    amap = {n: (k, b) for n, k, b in ans}
    question_map[rev] = {n: (stem, opts) for n, stem, opts in qs}
    answer_map[rev] = amap
    keys = []
    for n, stem, opts in qs:
        if set(opts) != set("ABCD"):
            findings.append(f"{rev} Q{n}: options {sorted(opts)}")
        if n not in amap:
            findings.append(f"{rev} Q{n}: missing answer")
            continue
        key, body = amap[n]
        keys.append(key)
        if "**Source/evidence:**" not in body or "**Examiner trap:**" not in body:
            findings.append(f"{rev} Q{n}: source/trap missing")
        rats = re.findall(r"(?m)^- \*\*([A-D]):\*\*", body)
        if sorted(rats) != list("ABCD"):
            findings.append(f"{rev} Q{n}: rationales {rats}")
        lengths = [len(opts[x].split()) for x in "ABCD"]
        keyed = lengths[ord(key)-65]
        others = [lengths[j] for j in range(4) if j != ord(key)-65]
        mean = sum(others) / 3
        if keyed >= 8 and mean and (keyed / mean > 2.20 or keyed / mean < 0.40):
            findings.append(f"{rev} Q{n}: keyed-length ratio {keyed/mean:.2f}")
        all_stems.append((rev, n, re.sub(r"\W+", " ", stem.lower()).strip()))
        all_options.extend((rev, n, x, re.sub(r"\W+", " ", t.lower()).strip()) for x, t in opts.items())
    keys_by_rev[rev] = "".join(keys)
    for phrase in FORBIDDEN:
        if phrase.lower() in qtext.lower():
            findings.append(f"{rev}: forbidden phrase {phrase!r}")
    if re.search(r"(?i)\b(answer key|correct option|solution)\b", qtext):
        findings.append(f"{rev}: possible answer leakage word")
    run = max((len(m.group(0)) for m in re.finditer(r"(A+|B+|C+|D+)", "".join(keys))), default=0)
    if run > 2:
        findings.append(f"{rev}: key run {run}")
    for size in range(4, 7):
        seq = "".join(keys)
        for start in range(len(seq) - 2 * size + 1):
            if seq[start:start+size] == seq[start+size:start+2*size]:
                findings.append(f"{rev}: repeated key cycle size {size} at {start+1}")

for i, a in enumerate(all_stems):
    for b in all_stems[i+1:]:
        ratio = SequenceMatcher(None, a[2], b[2]).ratio()
        if a[2] == b[2]:
            findings.append(f"exact stem: {a[:2]} {b[:2]}")
        elif ratio >= 0.90:
            findings.append(f"near stem {ratio:.2f}: {a[:2]} {b[:2]}")

option_counts = Counter(x[3] for x in all_options)
standard_shells = {
    "1 only", "2 only", "both 1 and 2", "neither 1 nor 2", "one only", "two only",
    "three only", "all three", "all four", "none", "1 and 2 only", "1 and 3 only",
    "2 and 3 only", "1 2 and 3", "1 2 and 3 only", "1 2 3 and 4",
    "both a and r are true and r is the correct explanation of a",
    "both a and r are true but r is not the correct explanation of a",
    "a is true but r is false", "a is false but r is true",
}
for text, count in option_counts.items():
    if count > 1 and len(text.split()) >= 6 and text not in standard_shells and not re.fullmatch(r"\d [a-d]( \d [a-d])+", text):
        findings.append(f"repeated full option x{count}: {text[:90]}")

if len(set(keys_by_rev.values())) != len(keys_by_rev):
    findings.append("identical answer-key sequence reused across revisions")

# Semantic regression expectations for the October 2026 audit remediation.
required_question_fragments = {
    ("revision-1", 17): ("Gurukul Kangri",),
    ("revision-1", 23): ("Muhammadan Anglo-Oriental School",),
    ("revision-1", 45): ("Muhammadan Anglo-Oriental School",),
    ("revision-2", 9): ("Self-Respect movement", "Gurukul Kangri"),
    ("revision-2", 13): ("Death of Ramakrishna Paramhansa",),
    ("revision-2", 36): ("scriptural, Vedic or Vedantic authority",),
    ("revision-2", 45): ("Muhammadan Anglo-Oriental School",),
    ("revision-3", 20): ("School opening in 1875", "college status in 1877"),
    ("revision-3", 40): ("newspaper archive",),
    ("revision-3", 41): ("Muhammadan Anglo-Oriental School",),
    ("revision-3", 45): ("Which causal formulation",),
}
for (rev, no), fragments in required_question_fragments.items():
    stem, opts = question_map[rev][no]
    live = stem + "\n" + "\n".join(opts.values())
    for fragment in fragments:
        if fragment.lower() not in live.lower():
            findings.append(f"{rev} Q{no}: missing semantic expectation {fragment!r}")

forbidden_question_fragments = {
    ("revision-1", 17): ("Sadharan Brahmo Samaj in 1905",),
    ("revision-1", 23): ("College was established at Aligarh in",),
    ("revision-1", 45): ("establishment of the MAO College",),
    ("revision-2", 9): ("Satyarth Prakash",),
    ("revision-2", 13): ("Belur Math consolidation",),
    ("revision-2", 36): ("explicitly religious authority",),
    ("revision-2", 45): ("1875 — Arya Samaj and MAO College",),
    ("revision-3", 41): ("1875 for both Arya Samaj and MAO College",),
}
for (rev, no), fragments in forbidden_question_fragments.items():
    stem, opts = question_map[rev][no]
    live = stem + "\n" + "\n".join(opts.values())
    for fragment in fragments:
        if fragment.lower() in live.lower():
            findings.append(f"{rev} Q{no}: retained superseded wording {fragment!r}")

r2_q24_answer = answer_map["revision-2"][24][1]
if "Complete-Topic-Package.md" not in r2_q24_answer or "1925" not in r2_q24_answer:
    findings.append("revision-2 Q24: Self-Respect 1925 source expectation missing")

print("COUNTS")
for rev in keys_by_rev:
    print(rev, "45 questions; keys", dict(Counter(keys_by_rev[rev])), "sequence", keys_by_rev[rev])
print("TOTAL", len(all_stems), "questions;", len(all_options), "options")
print("FINDINGS", len(findings))
for finding in findings:
    print("-", finding)
