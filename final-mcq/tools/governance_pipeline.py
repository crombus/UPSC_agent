"""Read-only release gate for the Governance final-MCQ queue."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Governance"
INDEX = SUBJECT / "INDEX.md"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
QUESTION = re.compile(r"^### Q(\d+)\s*$", re.M)
ANSWER = re.compile(r"^(\d+)\.\s+\*\*([A-D])\.", re.M)


def inspect_bank(folder: Path) -> tuple[dict, list[str]]:
    findings: list[str] = []
    qpath, apath, cpath = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
    if not all(path.is_file() for path in (qpath, apath, cpath)):
        return {}, ["missing QUESTIONS.md, ANSWERS.md or COVERAGE.md"]
    questions = qpath.read_text(encoding="utf-8")
    answers = apath.read_text(encoding="utf-8")
    qmatches = list(QUESTION.finditer(questions))
    amatches = list(ANSWER.finditer(answers))
    qnums = [int(match.group(1)) for match in qmatches]
    anums = [int(match.group(1)) for match in amatches]
    if qnums != list(range(1, len(qnums) + 1)):
        findings.append("question numbering is not contiguous")
    if anums != qnums:
        findings.append("answer mapping is not one-to-one")
    if len(re.findall(r"^\|\s*\d+\s*\|", cpath.read_text(encoding="utf-8"), re.M)) < len(qnums):
        findings.append("question-level coverage ledger is incomplete")
    for index, match in enumerate(qmatches):
        end = qmatches[index + 1].start() if index + 1 < len(qmatches) else len(questions)
        body = questions[match.end():end]
        options = re.findall(r"^[A-D]\. (.+)$", body, re.M)
        if len(options) != 4:
            findings.append(f"Q{match.group(1)} lacks four options")
            continue
        if len(options) != len(set(options)):
            findings.append(f"Q{match.group(1)} has duplicate options")
        lengths = [len(option) for option in options]
        if max(lengths) > 1.65 * max(1, min(lengths)):
            findings.append(f"Q{match.group(1)} option-length cue")
    for index, match in enumerate(amatches):
        end = amatches[index + 1].start() if index + 1 < len(amatches) else len(answers)
        body = answers[match.end():end]
        if not all(re.search(rf"\b{letter}\s*:", body) for letter in "ABCD"):
            findings.append(f"Q{match.group(1)} lacks option-specific rationales")
        if not re.search(r"\*\*Sources?:\*\*", body):
            findings.append(f"Q{match.group(1)} lacks source evidence")
        if not re.search(r"(?i)\btrap\b|confus|distinguish|cannot|not |alone|separate|wrong", body):
            findings.append(f"Q{match.group(1)} lacks examiner trap")
    for pattern in (r"\*\*Correct answer", r"\*\*Sources?:", r"\*\*Examiner trap:", r"Answer key"):
        if re.search(pattern, questions, re.I):
            findings.append(f"answer leakage: {pattern}")
    keys = [match.group(2) for match in amatches]
    return {"questions": len(qnums), "answers": len(anums), "keys": dict(Counter(keys))}, findings


def catalogue_entries() -> list[dict]:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    entries = data.get("topics", data) if isinstance(data, dict) else data
    return sorted(
        [entry for entry in entries if isinstance(entry, dict)
         and entry.get("subject", {}).get("key") == "Governance"],
        key=lambda entry: int(entry["topic_order"]),
    )


def folder_for(order: int) -> Path:
    folders = sorted(SUBJECT.glob(f"{order:02d}-*"))
    if len(folders) != 1:
        raise SystemExit(f"GOVERNANCE PIPELINE: FAIL — topic {order:02d} folder mismatch")
    return folders[0]


def indexed_complete_orders() -> list[int]:
    text = INDEX.read_text(encoding="utf-8")
    orders: list[int] = []
    for entry in catalogue_entries():
        order = int(entry["topic_order"])
        row = re.search(rf"^\|.*?\[{order:02d} [^]]+\].*$", text, re.M)
        if row and re.search(r"\bcomplete\b", row.group(0), re.I):
            orders.append(order)
    return orders


def next_pending() -> str:
    complete = set(indexed_complete_orders())
    for entry in catalogue_entries():
        if int(entry["topic_order"]) not in complete:
            return entry["display_title"]
    return "none"


def main() -> None:
    required = [
        "COVERAGE.md",
        "OWNER-MATRIX.md",
        "SOURCE-ROUTING.md",
        "OPTION-AUDIT.md",
        "SOURCE-AND-PYQ-HOLDS.md",
        "STRUCTURAL-AUDIT.md",
        "HOSTILE-AUDIT.md",
        "AUDIT-REPORT.md",
        "VALIDATION.json",
    ]
    complete = indexed_complete_orders()
    if not complete:
        raise SystemExit("GOVERNANCE PIPELINE: FAIL — no completed topic is indexed")
    total = 0
    latest = None
    for order in complete:
        topic = folder_for(order)
        missing = [name for name in required if not (topic / name).is_file()]
        if missing:
            raise SystemExit(f"GOVERNANCE PIPELINE: FAIL — topic {order:02d} missing {missing}")
        stems: set[str] = set()
        results = []
        for revision in range(1, 4):
            result, findings = inspect_bank(topic / f"revision-{revision}")
            if findings:
                raise SystemExit(
                    f"GOVERNANCE PIPELINE: FAIL — topic {order:02d} revision-{revision}: "
                    + "; ".join(findings)
                )
            qtext = (topic / f"revision-{revision}" / "QUESTIONS.md").read_text(encoding="utf-8")
            for match in QUESTION.finditer(qtext):
                stem = re.sub(r"\s+", " ", qtext[match.end():].split("\n\nA.")[0].strip()).lower()
                if stem in stems:
                    raise SystemExit(f"GOVERNANCE PIPELINE: FAIL — duplicate stem in topic {order:02d}")
                stems.add(stem)
            results.append(result)
            total += result["questions"]
        latest = results
    print(
        "GOVERNANCE PIPELINE: PASS — completed topics "
        f"{','.join(f'{order:02d}' for order in complete)}, {total} questions across released banks; "
        f"latest keys={latest[0]['keys']}/{latest[1]['keys']}/{latest[2]['keys']}"
    )
    print(f"NEXT PENDING: {next_pending()}")


if __name__ == "__main__":
    main()
