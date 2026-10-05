"""Read-only resume and structural checks for the Indian Art and Culture MCQ queue."""

from __future__ import annotations

import re
from pathlib import Path


BASE = Path(__file__).resolve().parents[1]
SUBJECT = BASE / "subjects" / "Indian-Art-and-Culture"
INDEX = SUBJECT / "INDEX.md"
ROW = re.compile(r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", re.M)
QUESTION = re.compile(r"^### Q(\d+)\.", re.M)
ANSWER = re.compile(r"^(\d+)\.\s+\*\*([A-D])\.", re.M)
OPTION = re.compile(r"^([A-D])\. ", re.M)


def inspect_bank(folder: Path) -> str:
    q_path, a_path, c_path = folder / "QUESTIONS.md", folder / "ANSWERS.md", folder / "COVERAGE.md"
    if not all(path.is_file() for path in (q_path, a_path, c_path)):
        return "INVALID missing QUESTIONS.md, ANSWERS.md or COVERAGE.md"
    questions = q_path.read_text(encoding="utf-8")
    answers = a_path.read_text(encoding="utf-8")
    q_ids = [int(value) for value in QUESTION.findall(questions)]
    a_ids = [int(value[0]) for value in ANSWER.findall(answers)]
    if len(q_ids) < 40:
        return f"INVALID fewer than 40 originals ({len(q_ids)})"
    if q_ids != list(range(1, len(q_ids) + 1)) or q_ids != a_ids:
        return f"INVALID question/key numbering ({len(q_ids)} questions, {len(a_ids)} keys)"
    header = '\n'.join(questions.splitlines()[:4])
    if re.search(r"(?i)\b(answer key|solution|sources?:|examiner trap|hint|correct answer|unfinished)\b", header):
        return "INVALID answer leakage in QUESTIONS.md header"
    sections = list(QUESTION.finditer(questions))
    for position, section in enumerate(sections):
        end = sections[position + 1].start() if position + 1 < len(sections) else len(questions)
        if OPTION.findall(questions[section.end() : end]) != list("ABCD"):
            return f"INVALID Q{q_ids[position]} options"
    answer_sections = list(re.finditer(r"(?m)^\d+\.\s+\*\*[A-D]\.", answers))
    for position, section in enumerate(answer_sections):
        end = answer_sections[position + 1].start() if position + 1 < len(answer_sections) else len(answers)
        content = answers[section.end() : end]
        if not all(re.search(rf"(?<![A-Za-z]){letter}(?:\.|\b)", content) for letter in "ABCD"):
            return f"INVALID Q{a_ids[position]} option-specific rationales"
        if not re.search(r"(?i)\bSources?:", content) or not re.search(r"(?i)\bTrap:", content):
            return f"INVALID Q{a_ids[position]} source/trap"
    return f"{len(q_ids)} originals; mapped and structurally clean"


def main() -> None:
    text = INDEX.read_text(encoding="utf-8")
    rows = {}
    for number, title, coverage in ROW.findall(text):
        status = 'complete' if re.search(r'(?i)complete', coverage) else ('blocked' if re.search(r'(?i)blocked', coverage) else 'pending')
        rows[int(number)] = (title.strip(), status)
    if set(rows) != set(range(1, 16)):
        raise SystemExit("Pipeline error: INDEX.md must contain exactly 15 catalogue rows")
    active = next((number for number in range(1, 16) if rows[number][1] != "complete"), None)
    if active is None:
        print("All 15 Indian Art and Culture topics are indexed complete.")
        return
    print(f"NEXT: {active:02} - {rows[active][0]} [{rows[active][1]}]")
    for number in range(1, active):
        folder = next(SUBJECT.glob(f"{number:02d}-*"), None)
        if folder is not None and rows[number][1] == "complete":
            for revision in range(1, 4):
                print(f"  topic {number:02} revision-{revision}: {inspect_bank(folder / f'revision-{revision}')}")
    if rows[active][1] == "pending":
        print("Start from the active topic's Basic/Advanced/workbook/OCR sources; do not open later topics.")
    elif rows[active][1] == "blocked":
        print("Blocked: resolve or document the hold; do not silently skip or mark complete.")


if __name__ == "__main__":
    main()
