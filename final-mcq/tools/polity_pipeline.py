"""Read-only queue and structural gate for the Polity final-MCQ atlas."""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Polity"
INDEX = SUBJECT / "INDEX.md"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*`?polity-(\d+)`?\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$", re.M)
QUESTION = re.compile(r"^### Q(\d+)\. (.+)$", re.M)
ANSWER = re.compile(r"^### Q(\d+) — ([A-D])\s*$", re.M)


def queue() -> dict[int, tuple[str, str, str]]:
    rows = {}
    for order, key, title, status, revision_sets in ROW.findall(INDEX.read_text(encoding="utf-8")):
        number = int(order)
        if int(key) != number or number in rows:
            raise SystemExit("Pipeline error: malformed or duplicate Polity index row")
        rows[number] = (
            f"{title.strip()} | {revision_sets.strip()}",
            status.strip().strip("`").lower(),
            revision_sets.strip(),
        )
    if not rows:
        raise SystemExit("Pipeline error: Polity INDEX.md has no catalogue rows")
    return rows


def catalogue_title(number: int) -> str:
    data = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    entries = data.get("topics", []) if isinstance(data, dict) else data
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        subject = entry.get("subject")
        subject_key = subject.get("key") if isinstance(subject, dict) else subject
        if subject_key == "Polity" and int(entry["topic_order"]) == number:
            return entry["display_title"]
    raise SystemExit(f"Pipeline error: catalogue lacks polity-{number:02d}")


def inspect_bank(folder: Path, minimum: int = 40) -> tuple[int, dict[str, int]]:
    qpath, apath, cpath = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
    if not all(path.is_file() for path in (qpath, apath, cpath)):
        raise SystemExit(f"Pipeline error: missing bank deliverable in {folder}")
    questions = qpath.read_text(encoding="utf-8")
    answers = apath.read_text(encoding="utf-8")
    qmatches = list(QUESTION.finditer(questions))
    amatches = list(ANSWER.finditer(answers))
    qnums = [int(m.group(1)) for m in qmatches]
    anums = [int(m.group(1)) for m in amatches]
    if len(qnums) < minimum:
        raise SystemExit(f"Pipeline error: {folder.name} has only {len(qnums)} questions")
    if qnums != list(range(1, len(qnums) + 1)) or anums != qnums:
        raise SystemExit(f"Pipeline error: {folder.name} numbering/key mapping is not contiguous")
    if re.search(r"\*\*(?:Correct answer|Evidence|Examiner trap|Rationale)|\bAnswer key\b", questions, re.I):
        raise SystemExit(f"Pipeline error: answer leakage in {folder.name}/QUESTIONS.md")
    for i, match in enumerate(qmatches):
        end = qmatches[i + 1].start() if i + 1 < len(qmatches) else len(questions)
        options = re.findall(r"^([A-D])\. ", questions[match.end() : end], re.M)
        if options != list("ABCD"):
            raise SystemExit(f"Pipeline error: {folder.name} Q{match.group(1)} lacks A-D options")
    keys = Counter(m.group(2) for m in amatches)
    for i, match in enumerate(amatches):
        end = amatches[i + 1].start() if i + 1 < len(amatches) else len(answers)
        body = answers[match.end() : end]
        rationales = re.findall(r"(?<![A-Za-z])([A-D]) [✅❌]", body)
        if rationales != list("ABCD"):
            raise SystemExit(f"Pipeline error: {folder.name} Q{match.group(1)} lacks A-D rationales")
        if not re.search(r"\[[^\]]+\]", body):
            raise SystemExit(f"Pipeline error: {folder.name} Q{match.group(1)} lacks evidence citation")
        if not re.search(r"\*\*Trap:\*", body, re.I):
            raise SystemExit(f"Pipeline error: {folder.name} Q{match.group(1)} lacks examiner trap")
    return len(qnums), dict(keys)


def main() -> None:
    rows = queue()
    next_pending = next((number for number in sorted(rows) if rows[number][1] != "complete"), None)
    active = (next_pending - 1) if next_pending is not None and next_pending > 1 else max(rows)
    title, status, revision_sets = rows[active]
    match = re.search(r"\]\(([^)]+/COVERAGE\.md)\)", revision_sets)
    if not match:
        raise SystemExit(f"Pipeline error: polity-{active:02d} has no coverage link")
    topic = (INDEX.parent / Path(match.group(1)).parent).resolve()
    if not topic.is_relative_to(SUBJECT.resolve()):
        raise SystemExit("Pipeline error: active topic escapes Polity folder")
    all_stems: defaultdict[str, list[int]] = defaultdict(list)
    for number in (1, 2, 3):
        count, keys = inspect_bank(topic / f"revision-{number}")
        print(f"revision-{number}: PASS ({count} questions, keys={keys})")
        text = (topic / f"revision-{number}" / "QUESTIONS.md").read_text(encoding="utf-8")
        for stem in QUESTION.findall(text):
            all_stems[stem[1].strip().lower()].append(number)
    duplicates = [stem for stem, banks in all_stems.items() if len(set(banks)) > 1]
    if duplicates:
        raise SystemExit(f"Pipeline error: exact cross-bank stem overlap ({len(duplicates)})")
    later = sorted(
        folder for folder in SUBJECT.glob("[0-9][0-9]-*")
        if folder.resolve() != topic and int(folder.name[:2]) > active
    )
    if later:
        raise SystemExit(f"Pipeline error: later Polity topic folder exists: {later[0]}")
    if status != "complete":
        raise SystemExit(f"Pipeline error: active topic remains {status!r}")
    pending = next_pending
    print(f"POLITY PIPELINE: PASS — polity-{active:02d} is complete")
    if pending is None:
        print("NEXT PENDING: none")
    else:
        print(f"NEXT PENDING: polity-{pending:02d} — {catalogue_title(pending)}")


if __name__ == "__main__":
    main()
