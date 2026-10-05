"""Read-only resume and structural checks for the Medieval History MCQ queue."""

import argparse
import re
from pathlib import Path


INDEX = Path(__file__).resolve().parents[1] / "subjects" / "Medieval-History" / "INDEX.md"
ROW = re.compile(r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", re.M)
LINK = re.compile(r"\]\(([^)]+/COVERAGE\.md)\)")
QUESTION = re.compile(r"^### Q(\d+)\.", re.M)
ANSWER = re.compile(r"^### Q(\d+)\. ([A-D])\s*$", re.M)
OPTION = re.compile(r"^([A-D])\. ", re.M)
RATIONALE = re.compile(r"^- \*\*([A-D]):\*\*", re.M)


def read_queue(index: Path) -> dict[int, tuple[str, str, str | None]]:
    text = index.read_text(encoding="utf-8")
    topics = {}
    for match in ROW.finditer(text):
        number, title, bank, raw_status = match.groups()
        status = raw_status.strip().strip("`").split("`", 1)[0]
        if status not in {"complete", "pending", "in_progress", "blocked"}:
            raise ValueError(f"Topic {number}: unsupported status {status!r}")
        link = LINK.search(bank)
        topic = int(number)
        if topic in topics:
            raise ValueError(f"Duplicate topic {number}")
        topics[topic] = (title.strip(), status, link.group(1) if link else None)
    if set(topics) != set(range(1, 26)):
        raise ValueError("Index must contain exactly the 25 Medieval History topic rows")
    return topics


def inspect_revision(folder: Path) -> str:
    question_file, answer_file = folder / "QUESTIONS.md", folder / "ANSWERS.md"
    if not question_file.is_file() or not answer_file.is_file():
        return "not started (question/answer pair missing)"
    questions = question_file.read_text(encoding="utf-8")
    answers = answer_file.read_text(encoding="utf-8")
    question_sections = list(QUESTION.finditer(questions))
    answer_sections = list(ANSWER.finditer(answers))
    ids = [int(section.group(1)) for section in question_sections]
    keys = [int(section.group(1)) for section in answer_sections]
    if not ids or ids != list(range(1, len(ids) + 1)) or ids != keys:
        return f"INVALID question/key numbering ({len(ids)} questions, {len(keys)} keys)"
    for position, section in enumerate(question_sections):
        end = question_sections[position + 1].start() if position + 1 < len(ids) else len(questions)
        if OPTION.findall(questions[section.end():end]) != list("ABCD"):
            return f"INVALID Q{ids[position]} options"
    for position, section in enumerate(answer_sections):
        end = answer_sections[position + 1].start() if position + 1 < len(keys) else len(answers)
        content = answers[section.end():end]
        if RATIONALE.findall(content) != list("ABCD") or "**Source:**" not in content or "**Examiner trap:**" not in content:
            return f"INVALID Q{keys[position]} explanations/source/trap"
    return f"{len(ids)} structurally mapped originals; editorial/source/release audit still required"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=INDEX, help="Medieval History INDEX.md")
    args = parser.parse_args()
    try:
        topics = read_queue(args.index)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Pipeline error: {exc}\n")
    # Finish the two existing provisional banks before opening Topic 11.
    queue = list(range(9, 26))
    active = next((number for number in queue if topics[number][1] != "complete"), None)
    if active is None:
        print("Topics 09–25 are indexed complete; check independent release holds before ending the schedule.")
        return
    title, status, link = topics[active]
    print(f"NEXT: {active:02} - {title} [{status}]")
    if status == "blocked":
        print("Blocked: resolve or document the hold; do not silently skip or mark complete.")
    if not link:
        if status != "pending":
            parser.exit(1, f"Pipeline error: Topic {active:02} has no coverage-ledger link\n")
        print("Start from Basic/Advanced/workbook/PDF sources; create root and three revision ledgers.")
        return
    folder = (args.index.parent / Path(link).parent).resolve()
    if not folder.is_relative_to(args.index.parent.resolve()) or not (folder / "COVERAGE.md").is_file():
        parser.exit(1, f"Pipeline error: Topic {active:02} ledger is absent or outside subject folder\n")
    for revision in range(1, 4):
        print(f"  revision-{revision}: {inspect_revision(folder / f'revision-{revision}')}")
    print("Review the coverage ledger's first gap; structural counts never certify completion.")


if __name__ == "__main__":
    main()
