"""Reusable hostile audit for the Polity final-MCQ banks.

Checks learner-file leakage, repeated and near-duplicate stems, key mapping,
option-cue bias, keyed-option length bias, answer rationales and item-level
coverage. It exits non-zero on any critical finding and can audit one topic or
the complete Polity atlas.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Polity"
Q_RE = re.compile(r"^### Q(\d+)\. (.+)$", re.M)
A_RE = re.compile(r"^### Q(\d+) — ([A-D])\s*$", re.M)
OPT_RE = re.compile(r"^([A-D])\. (.*)$", re.M)
BAD_QUESTION_PATTERNS = (
    r"✅",
    r"❌",
    r"⚠️",
    r"📰",
    r"🔑",
    r"\[(?:FACT|LIMIT|PYQ|SOURCE|MECHANISM|ANALYSIS)\]",
    r"\b(?:Mechanism|Source|Evidence|Rationale|Examiner trap)\s*:",
    r"\bsource[- ]grounded\b",
    r"\bautomatically overrides every Fundamental Right\b",
    r"\bis an exclusive power of the Union\b",
    r"\bapplies only after a judicial direction\b",
)
CUE_WORDS = re.compile(
    r"\b(?:always|never|only|must|all|none|entirely|exclusively|automatically)\b",
    re.I,
)


def parse_questions(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    matches = list(Q_RE.finditer(text))
    rows = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        options = [value.strip() for _, value in OPT_RE.findall(text[match.end() : end])]
        rows.append({"number": int(match.group(1)), "stem": match.group(2).strip(), "options": options})
    return rows


def parse_answers(path: Path) -> tuple[dict[int, str], dict[int, str]]:
    text = path.read_text(encoding="utf-8")
    matches = list(A_RE.finditer(text))
    keys = {int(number): key for number, key in A_RE.findall(text)}
    bodies: dict[int, str] = {}
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        bodies[int(match.group(1))] = text[match.end() : end]
    return keys, bodies


def sim(left: str, right: str) -> float:
    normalize = lambda value: re.sub(r"[^a-z0-9 ]", "", value.lower())
    return SequenceMatcher(None, normalize(left), normalize(right)).ratio()


def audit_bank(folder: Path, revision: int) -> dict:
    rev = folder / f"revision-{revision}"
    qpath, apath, cpath = rev / "QUESTIONS.md", rev / "ANSWERS.md", folder / "COVERAGE.md"
    findings: list[str] = []
    if not all(path.is_file() for path in (qpath, apath, cpath)):
        return {"revision": revision, "count": 0, "findings": [f"missing deliverable in {rev}"]}
    qtext = qpath.read_text(encoding="utf-8")
    rows = parse_questions(qpath)
    keys, bodies = parse_answers(apath)
    expected = list(range(1, len(rows) + 1))
    numbers = [row["number"] for row in rows]
    if numbers != expected:
        findings.append(f"numbering is not contiguous: {numbers[:5]}...")
    if set(keys) != set(numbers):
        findings.append("question/answer number mapping is incomplete")
    for pattern in BAD_QUESTION_PATTERNS:
        if re.search(pattern, qtext, re.I):
            findings.append(f"answer leakage pattern: {pattern}")
    for row in rows:
        if len(row["options"]) != 4:
            findings.append(f"Q{row['number']} has {len(row['options'])} options")
            continue
        if len(set(option.casefold() for option in row["options"])) != 4:
            findings.append(f"Q{row['number']} has duplicate options")
        if any(not option.strip() for option in row["options"]):
            findings.append(f"Q{row['number']} has an empty option")
        if row["stem"].casefold().startswith("with reference to"):
            findings.append(f"Q{row['number']} retains generic legacy stem")

    stems = [row["stem"] for row in rows]
    seen: set[str] = set()
    for index, stem in enumerate(stems):
        normalized = re.sub(r"[^a-z0-9 ]", "", stem.lower())
        if normalized in seen:
            findings.append(f"exact duplicate stem at Q{index + 1}")
        seen.add(normalized)
    for i, left in enumerate(stems):
        for j in range(i):
            if sim(left, stems[j]) >= 0.90:
                findings.append(f"near-duplicate stems Q{j + 1}/Q{i + 1} ({sim(left, stems[j]):.2f})")
                break

    key_lengths: list[int] = []
    distractor_lengths: list[int] = []
    position_cues = Counter()
    keyed_cues = Counter()
    for row in rows:
        key = keys.get(row["number"])
        if key not in "ABCD":
            findings.append(f"Q{row['number']} has invalid key {key!r}")
            continue
        keyed_index = "ABCD".index(key)
        key_lengths.append(len(row["options"][keyed_index]))
        distractor_lengths.extend(len(row["options"][i]) for i in range(4) if i != keyed_index)
        for index, option in enumerate(row["options"]):
            count = len(CUE_WORDS.findall(option))
            position_cues["ABCD"[index]] += count
            if index == keyed_index:
                keyed_cues["ABCD"[index]] += count
    if key_lengths and statistics.mean(key_lengths) > statistics.mean(distractor_lengths) * 1.12:
        findings.append(
            f"keyed-option length bias: keyed mean {statistics.mean(key_lengths):.1f}, "
            f"distractor mean {statistics.mean(distractor_lengths):.1f}"
        )
    if key_lengths and sum(1 for row in rows if len(row["options"]["ABCD".index(keys[row["number"]])]) > max(map(len, row["options"])) - 1) > len(rows) * 0.78:
        findings.append("keyed option is almost always the longest")
    if position_cues:
        max_cue = max(position_cues.values())
        min_cue = min(position_cues.values())
        if max_cue > min_cue * 1.65 and max_cue - min_cue > 12:
            findings.append(f"option cue-position bias: {dict(position_cues)}")

    for row in rows:
        body = bodies.get(row["number"], "")
        rationales = re.findall(r"(?m)^([A-D])\s+[✅❌]", body)
        if rationales != list("ABCD"):
            findings.append(f"Q{row['number']} lacks exactly four A-D rationales")
        if not re.search(r"\*\*Evidence:\*\*\s*\[[^\]]+\]", body):
            findings.append(f"Q{row['number']} lacks evidence citation")
        if not re.search(r"\*\*Trap:\*\*", body, re.I):
            findings.append(f"Q{row['number']} lacks examiner trap")
        key = keys.get(row["number"])
        if key and not re.search(rf"^{key}\s+✅", body, re.M):
            findings.append(f"Q{row['number']} key {key} is not marked correct in rationale")

    coverage = cpath.read_text(encoding="utf-8")
    for revision_number in (1, 2, 3):
        revision_rows = parse_questions(folder / f"revision-{revision_number}" / "QUESTIONS.md")
        revision_numbers = [row["number"] for row in revision_rows]
        expected_rows = re.findall(rf"^\| R{revision_number} \| Q(\d+) \| .+ \| ([A-D]) \|", coverage, re.M)
        if len(expected_rows) != len(revision_rows):
            findings.append(f"coverage R{revision_number} has {len(expected_rows)} rows, expected {len(revision_rows)}")
        if [int(number) for number, _ in expected_rows] != revision_numbers:
            findings.append(f"coverage R{revision_number} item sequence does not match QUESTIONS.md")
    return {
        "revision": revision,
        "count": len(rows),
        "keys": dict(Counter(keys.values())),
        "keyed_mean": round(statistics.mean(key_lengths), 2) if key_lengths else 0,
        "distractor_mean": round(statistics.mean(distractor_lengths), 2) if distractor_lengths else 0,
        "findings": sorted(set(findings)),
    }


def audit_topic(folder: Path) -> dict:
    banks = [audit_bank(folder, revision) for revision in (1, 2, 3)]
    findings = [f"R{bank['revision']}: {finding}" for bank in banks for finding in bank["findings"]]
    stems_by_revision = []
    for revision in (1, 2, 3):
        stems_by_revision.append([row["stem"] for row in parse_questions(folder / f"revision-{revision}" / "QUESTIONS.md")])
    for left_index in range(3):
        for right_index in range(left_index + 1, 3):
            for i, left in enumerate(stems_by_revision[left_index]):
                for j, right in enumerate(stems_by_revision[right_index]):
                    if sim(left, right) >= 0.90:
                        findings.append(f"cross-bank near-duplicate R{left_index + 1}Q{i + 1}/R{right_index + 1}Q{j + 1}")
    return {"topic": folder.name, "banks": banks, "findings": sorted(set(findings))}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=55)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    folders = sorted(SUBJECT.glob("[0-9][0-9]-*"))
    if args.topic is not None:
        folders = [folder for folder in folders if int(folder.name[:2]) == args.topic]
    folders = [folder for folder in folders if args.start <= int(folder.name[:2]) <= args.end]
    reports = [audit_topic(folder) for folder in folders]
    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        for report in reports:
            status = "PASS" if not report["findings"] else "FAIL"
            print(f"{report['topic']}: {status}")
            for finding in report["findings"]:
                print(f"  - {finding}")
    raise SystemExit(1 if any(report["findings"] for report in reports) else 0)


if __name__ == "__main__":
    main()
