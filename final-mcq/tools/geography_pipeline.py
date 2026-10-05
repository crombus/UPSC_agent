"""Read-only resume and release checks for the Geography final-MCQ queue."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
INDEX = SUBJECT / "INDEX.md"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
ROW = re.compile(r"^\|\s*geography-(\d+)\s*\|\s*(.*?)\s*\|\s*([^|]+?)\s*\|", re.M)
QUESTION = re.compile(r"^### Q(\d+)\. (.+)$", re.M)
ANSWER = re.compile(r"^### Q(\d+) — ([A-D])\s*$", re.M)
OPTION = re.compile(r"^- ([A-D])\. ", re.M)
RATIONALE = re.compile(r"^- \*\*([A-D]):\*\*", re.M)


def subject_rows() -> dict[int, tuple[str, str]]:
    text = INDEX.read_text(encoding="utf-8")
    rows = {
        int(number): (title.strip(), status.strip().strip("`").lower())
        for number, title, status in ROW.findall(text)
    }
    if not rows:
        raise ValueError("Geography INDEX.md has no catalogue rows")
    return rows


def next_catalogue_topic(completed: set[int]) -> tuple[int, str] | None:
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    entries = catalogue.get("topics", []) if isinstance(catalogue, dict) else catalogue
    geography = [
        entry
        for entry in entries
        if isinstance(entry, dict)
        and (
            entry.get("subject") == "Geography"
            or (
                isinstance(entry.get("subject"), dict)
                and entry["subject"].get("key") == "Geography"
            )
        )
    ]
    geography.sort(key=lambda entry: entry["topic_order"])
    for entry in geography:
        number = int(entry["topic_order"])
        if number not in completed:
            return number, entry["display_title"]
    return None


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
    if len(qnums) < 40:
        findings.append(f"only {len(qnums)} questions; minimum is 40")
    if qnums != list(range(1, len(qnums) + 1)):
        findings.append("question numbering is not contiguous from Q1")
    if anums != qnums:
        findings.append("question/key numbering is not one-to-one")

    for position, match in enumerate(qmatches):
        end = qmatches[position + 1].start() if position + 1 < len(qmatches) else len(questions)
        if OPTION.findall(questions[match.end() : end]) != list("ABCD"):
            findings.append(f"Q{match.group(1)} does not have exactly four ordered options")

    for position, match in enumerate(amatches):
        end = amatches[position + 1].start() if position + 1 < len(amatches) else len(answers)
        body = answers[match.end() : end]
        if RATIONALE.findall(body) != list("ABCD"):
            findings.append(f"Q{match.group(1)} lacks four option-specific rationales")
        if not re.search(r"\*\*(?:Source|Evidence)", body, re.I):
            findings.append(f"Q{match.group(1)} lacks source/evidence")
        if not re.search(r"\*\*(?:Examiner )?trap", body, re.I):
            findings.append(f"Q{match.group(1)} lacks an examiner trap")

    leakage_patterns = [
        r"\*\*Correct answer",
        r"\*\*Evidence:",
        r"\*\*Examiner trap:",
        r"\*\*Rationale",
        r"\bAnswer key\b",
    ]
    for pattern in leakage_patterns:
        if re.search(pattern, questions, re.I):
            findings.append(f"answer leakage pattern: {pattern}")

    keys = Counter(match.group(2) for match in amatches)
    return {
        "questions": len(qnums),
        "answers": len(anums),
        "keys": dict(keys),
        "stems": [match.group(2).strip() for match in qmatches],
    }, findings


def simple_cycle(keys: list[str]) -> bool:
    return any(
        all(keys[index] == "ABCD"[(index + offset) % 4] for index in range(len(keys)))
        for offset in range(4)
    )


def main() -> None:
    rows = subject_rows()
    expected = set(range(1, 38))
    if set(rows) != expected:
        raise SystemExit(f"Pipeline error: Geography index must contain exactly topics 01-37, got {sorted(rows)}")

    repository_stems: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    total_questions = 0
    for topic_number in sorted(rows):
        title_cell, status = rows[topic_number]
        if status != "complete":
            raise SystemExit(f"Pipeline error: geography-{topic_number:02d} remains {status!r}")
        link = re.search(r"\]\(([^)]+/COVERAGE\.md)\)", title_cell)
        if not link:
            raise SystemExit(f"Pipeline error: geography-{topic_number:02d} has no coverage link")
        topic = (INDEX.parent / Path(link.group(1)).parent).resolve()
        if not topic.is_relative_to(SUBJECT.resolve()):
            raise SystemExit(f"Pipeline error: geography-{topic_number:02d} escaped Geography folder")
        required = (
            "COVERAGE.md",
            "SOURCE-AND-PYQ-HOLDS.md",
            "STRUCTURAL-AUDIT.md",
            "HOSTILE-AUDIT.md",
            "AUDIT-REPORT.md",
            "VALIDATION.json",
        )
        missing = [name for name in required if not (topic / name).is_file()]
        if missing:
            raise SystemExit(f"Pipeline error: geography-{topic_number:02d} missing {missing}")

        bank_results: dict[int, dict] = {}
        for bank_number in range(1, 4):
            result, findings = inspect_bank(topic / f"revision-{bank_number}")
            if findings:
                raise SystemExit(
                    f"Pipeline error: geography-{topic_number:02d}/revision-{bank_number}: "
                    + "; ".join(findings)
                )
            question_text = (topic / f"revision-{bank_number}" / "QUESTIONS.md").read_text(encoding="utf-8")
            qmatches = list(QUESTION.finditer(question_text))
            for pos, match in enumerate(qmatches):
                end = qmatches[pos + 1].start() if pos + 1 < len(qmatches) else len(question_text)
                options = re.findall(r"^- ([A-D])\. (.+)$", question_text[match.end():end], re.M)
                lengths = [len(value) for _, value in options]
                if len(lengths) != 4 or max(lengths) > 1.65 * max(1, min(lengths)):
                    raise SystemExit(
                        f"Pipeline error: geography-{topic_number:02d}/revision-{bank_number}/Q{match.group(1)} option-length cue"
                    )
            coverage = (topic / f"revision-{bank_number}" / "COVERAGE.md").read_text(encoding="utf-8")
            ledger_rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", coverage, re.M)
            if len(ledger_rows) != 44 or len({row[1].strip() for row in ledger_rows}) < 40:
                raise SystemExit(
                    f"Pipeline error: geography-{topic_number:02d}/revision-{bank_number} incomplete independent coverage ledger"
                )
            explanations = re.findall(r"^\*\*Explanation:\*\*\s*(.+)$", (topic / f"revision-{bank_number}" / "ANSWERS.md").read_text(encoding="utf-8"), re.M)
            if len(set(explanations)) < 40:
                raise SystemExit(
                    f"Pipeline error: geography-{topic_number:02d}/revision-{bank_number} generic/repeated explanations"
                )
            bank_results[bank_number] = result
            total_questions += result["questions"]
            for stem in result["stems"]:
                repository_stems[stem].append((topic_number, bank_number))

        duplicates = [
            stem for stem, locations in repository_stems.items()
            if len(locations) > 1 and any(loc[0] == topic_number for loc in locations)
        ]
        if duplicates:
            raise SystemExit(
                f"Pipeline error: geography-{topic_number:02d} exact cross-bank stem overlap ({len(duplicates)})"
            )
        key_sequence = []
        for bank_number in range(1, 4):
            answer_text = (topic / f"revision-{bank_number}" / "ANSWERS.md").read_text(encoding="utf-8")
            key_sequence.extend(match.group(2) for match in ANSWER.finditer(answer_text))
        if simple_cycle(key_sequence):
            raise SystemExit(f"Pipeline error: geography-{topic_number:02d} combined key sequence is a simple cycle")
        print(
            f"geography-{topic_number:02d}: PASS "
            f"(R1/R2/R3={sum(bank_results[b]['questions'] for b in range(1, 4))}, "
            f"keys={bank_results[1]['keys']}/{bank_results[2]['keys']}/{bank_results[3]['keys']})"
        )

    repository_duplicates = [stem for stem, locations in repository_stems.items() if len(locations) > 1]
    if repository_duplicates:
        raise SystemExit(f"Pipeline error: repository-wide exact stem overlap ({len(repository_duplicates)})")
    print(f"GEOGRAPHY PIPELINE: PASS — 37 topics, {total_questions} questions, all audits valid")
    print("NEXT PENDING: none")


if __name__ == "__main__":
    main()
