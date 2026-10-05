"""Read-only structural gate for the Indian Society final-MCQ queue."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Indian-Society"
INDEX = SUBJECT / "INDEX.md"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
QUESTION = re.compile(r"^### Q(\d+)\. (.+)$", re.M)
ANSWER = re.compile(
    r"^(?:### Q(?P<q1>\d+)\. (?P<a1>[A-D])\s*$|"
    r"(?P<q2>\d+)\. \*\*(?P<a2>[A-D])\.\*\*)",
    re.M,
)


def inspect_bank(folder: Path) -> tuple[dict, list[str]]:
    findings: list[str] = []
    files = [folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"]
    if not all(path.is_file() for path in files):
        return {}, ["missing QUESTIONS.md, ANSWERS.md or COVERAGE.md"]
    questions = files[0].read_text(encoding="utf-8")
    answers = files[1].read_text(encoding="utf-8")
    qm = list(QUESTION.finditer(questions))
    am = list(ANSWER.finditer(answers))
    qnums = [int(m.group(1)) for m in qm]
    anums = [int(m.group("q1") or m.group("q2")) for m in am]
    if len(qnums) < 30:
        findings.append("fewer than 30 questions")
    if qnums != list(range(1, len(qnums) + 1)):
        findings.append("question numbering is not contiguous")
    if anums != qnums:
        findings.append("answer mapping is not one-to-one")
    for i, match in enumerate(qm):
        end = qm[i + 1].start() if i + 1 < len(qm) else len(questions)
        body = questions[match.end():end]
        options = re.findall(r"^[A-D]\. (.+)$", body, re.M)
        if len(options) != 4:
            findings.append(f"Q{match.group(1)} lacks four options")
            continue
        if len(set(options)) != 4:
            findings.append(f"Q{match.group(1)} has duplicate options")
        lengths = [len(option) for option in options]
        if max(lengths) > 2.05 * max(1, min(lengths)):
            findings.append(f"Q{match.group(1)} option-length cue")
    for i, match in enumerate(am):
        end = am[i + 1].start() if i + 1 < len(am) else len(answers)
        body = answers[match.end():end]
        rationales = re.findall(r"^- \*\*([A-D])\s+[^:]+:\*\*", body, re.M)
        if sorted(rationales) != list("ABCD"):
            # Topic 01's pre-existing keys use one detailed paragraph that
            # explicitly discusses A/B/C/D instead of four bullet lines.
            mentioned = set(
                re.findall(r"(?<![A-Za-z])([A-D])(?:\s+|['’])(?=[A-Za-z])", body)
            )
            if not set("ABCD").issubset(mentioned):
                findings.append(
                    f"Q{match.group('q1') or match.group('q2')} "
                    "lacks four option-specific rationales"
                )
        has_source = "**Sources:**" in body or bool(re.search(r"\[[^\]]+\]", body))
        has_trap = (
            "**Examiner trap:**" in body
            or bool(
                re.search(
                    r"\b(?:trap|confus|mistak|overlook|infer|conflat|"
                    r"without|cannot|alone|rather|distinguish|separate|"
                    r"wrongly|false|true|not|no|doesn't|mislabel|omit)\w*",
                    body,
                    re.I,
                )
            )
        )
        if not has_source or not has_trap:
            findings.append(
                f"Q{match.group('q1') or match.group('q2')} lacks source or trap"
            )
    for pattern in (r"\*\*Correct answer", r"\*\*Sources:", r"\*\*Examiner trap:", r"Answer key"):
        if re.search(pattern, questions, re.I):
            findings.append(f"answer leakage: {pattern}")
    keys = [m.group("a1") or m.group("a2") for m in am]
    return {"questions": len(qnums), "answers": len(anums), "keys": dict(Counter(keys))}, findings


def topic_order(title: str) -> int:
    return int(re.match(r"^(\d+)", title).group(1))


def next_pending() -> str:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    entries = data.get("topics", data) if isinstance(data, dict) else data
    society = [
        entry for entry in entries
        if isinstance(entry, dict) and entry.get("subject", {}).get("key") == "Indian-Society"
    ]
    society.sort(key=lambda entry: entry["topic_order"])
    text = INDEX.read_text(encoding="utf-8")
    for entry in society:
        order = int(entry["topic_order"])
        row = re.search(rf"^\|\s*\[?{order:02d}\s+[^|]*\|.*?$", text, re.M)
        if row and re.search(r"\|\s*`?pending`?\s*\|", row.group(0), re.I):
            return entry["display_title"]
    return "none"


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    complete = sorted(
        int(match.group(1))
        for match in re.finditer(
            r"^\|\s*\[?(\d+)\s+[^|]*\|[^|]*\bcomplete\b", text, re.M | re.I
        )
    )
    if not complete:
        raise SystemExit("INDIAN SOCIETY PIPELINE: FAIL — no completed topic is indexed")
    required = ["COVERAGE.md", "SOURCE-AND-PYQ-HOLDS.md", "STRUCTURAL-AUDIT.md",
                "HOSTILE-AUDIT.md", "AUDIT-REPORT.md", "VALIDATION.json"]
    total = 0
    latest = None
    for order in complete:
        folders = sorted(SUBJECT.glob(f"{order:02d}-*"))
        if len(folders) != 1:
            raise SystemExit(f"INDIAN SOCIETY PIPELINE: FAIL — topic {order:02d} folder mismatch")
        topic = folders[0]
        missing = [name for name in required if not (topic / name).is_file()]
        if missing:
            raise SystemExit(f"INDIAN SOCIETY PIPELINE: FAIL — topic {order:02d} missing {missing}")
        stems: set[str] = set()
        for revision in range(1, 4):
            result, findings = inspect_bank(topic / f"revision-{revision}")
            if findings:
                raise SystemExit(
                    f"INDIAN SOCIETY PIPELINE: FAIL — topic {order:02d} revision-{revision}: "
                    + "; ".join(findings)
                )
            coverage = (topic / f"revision-{revision}" / "COVERAGE.md").read_text(encoding="utf-8")
            if len(re.findall(r"^\|\s*\d+\s*\|", coverage, re.M)) < result["questions"]:
                raise SystemExit(f"INDIAN SOCIETY PIPELINE: FAIL — topic {order:02d} revision-{revision} coverage incomplete")
            qtext = (topic / f"revision-{revision}" / "QUESTIONS.md").read_text(encoding="utf-8")
            for match in QUESTION.finditer(qtext):
                stem = re.sub(r"\s+", " ", match.group(2).strip()).lower()
                if stem in stems:
                    raise SystemExit(f"INDIAN SOCIETY PIPELINE: FAIL — duplicate stem in topic {order:02d}")
                stems.add(stem)
            total += result["questions"]
            latest = result
    print(
        f"INDIAN SOCIETY PIPELINE: PASS — completed topics "
        f"{','.join(f'{order:02d}' for order in complete)}, {total} questions across released banks; "
        f"latest keys={latest['keys'] if latest else {}}"
    )
    print(f"NEXT PENDING: {next_pending()}")


if __name__ == "__main__":
    main()
