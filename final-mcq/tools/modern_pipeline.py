"""Read-only resume and structural checks for the Modern History MCQ queue."""

import argparse
import re
from pathlib import Path


INDEX = Path(__file__).resolve().parents[1] / "subjects" / "Modern-History" / "INDEX.md"
ROW = re.compile(r"^\|\s*(\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|$", re.M)
LINK = re.compile(r"\]\(([^)]+/COVERAGE\.md)\)")
QUESTION = re.compile(r"^### (R([123])-(\d{3}))\.", re.M)
ANSWER = re.compile(r"^### (R([123])-(\d{3})) — ([A-D])\s*$", re.M)
OPTION = re.compile(r"^([A-D])\. ", re.M)
RATIONALE = re.compile(r"^- \*\*([A-D]) — (?:correct|incorrect):\*\*", re.M)


def read_queue(index: Path) -> dict[int, tuple[str, str, str | None]]:
    text = index.read_text(encoding="utf-8")
    topics = {}
    for match in ROW.finditer(text):
        number, title, raw_status, sets = match.groups()
        status_match = re.search(r"`(complete|pending|in_progress|blocked)`|^\s*(pending)\s*$", raw_status)
        if not status_match:
            raise ValueError(f"Topic {number}: unsupported status cell {raw_status.strip()!r}")
        status = next(group for group in status_match.groups() if group)
        link = LINK.search(title)
        topic = int(number)
        if topic in topics:
            raise ValueError(f"Duplicate topic {number}")
        topics[topic] = (title.strip(), status, link.group(1) if link else None)
    if set(topics) != set(range(1, 39)):
        raise ValueError("Index must contain exactly the 38 Modern History topic rows")
    return topics


def inspect_revision(folder: Path, revision: int) -> str:
    question_file, answer_file = folder / "QUESTIONS.md", folder / "ANSWERS.md"
    if not question_file.is_file() or not answer_file.is_file():
        return "not started (question/answer pair missing)"
    questions = question_file.read_text(encoding="utf-8")
    answers = answer_file.read_text(encoding="utf-8")
    question_sections = list(QUESTION.finditer(questions))
    answer_sections = list(ANSWER.finditer(answers))
    qids = [match.group(1) for match in question_sections if int(match.group(2)) == revision]
    aids = [match.group(1) for match in answer_sections if int(match.group(2)) == revision]
    expected = [f"R{revision}-{number:03d}" for number in range(1, len(qids) + 1)]
    if not qids or qids != expected or qids != aids:
        return f"INVALID question/key numbering ({len(qids)} questions, {len(aids)} keys)"
    for position, section in enumerate(question_sections):
        end = question_sections[position + 1].start() if position + 1 < len(question_sections) else len(questions)
        if OPTION.findall(questions[section.end() : end]) != list("ABCD"):
            return f"INVALID {section.group(1)} options"
    for position, section in enumerate(answer_sections):
        end = answer_sections[position + 1].start() if position + 1 < len(answer_sections) else len(answers)
        content = answers[section.end() : end]
        if RATIONALE.findall(content) != list("ABCD"):
            return f"INVALID {section.group(1)} rationales"
        if not re.search(r"\*\*(?:Source|Evidence)", content) or not re.search(
            r"\*\*(?:Trap|Examiner trap):\*\*", content
        ):
            return f"INVALID {section.group(1)} source/trap"
    return f"{len(qids)} structurally mapped originals; editorial/source/release audit still required"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=INDEX, help="Modern History INDEX.md")
    args = parser.parse_args()
    try:
        topics = read_queue(args.index)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Pipeline error: {exc}\n")
    active = next((number for number in range(1, 39) if topics[number][1] != "complete"), None)
    if active is None:
        print("Topics 01–38 are indexed complete; check independent release holds before ending the schedule.")
        return
    title, status, link = topics[active]
    title_text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
    print(f"NEXT: {active:02} - {title_text} [{status}]")
    if status == "blocked":
        print("Blocked: resolve or document the hold; do not silently skip or mark complete.")
    if not link:
        if status != "pending":
            parser.exit(1, f"Pipeline error: Topic {active:02} has no coverage-ledger link\n")
        print("Start from Basic/Advanced/workbook/PDF sources; create root and three revision ledgers.")
        print("Do not open later topics before the active catalogue topic is released or explicitly blocked.")
        return
    folder = (args.index.parent / Path(link).parent).resolve()
    if not folder.is_relative_to(args.index.parent.resolve()) or not (folder / "COVERAGE.md").is_file():
        parser.exit(1, f"Pipeline error: Topic {active:02} ledger is absent or outside subject folder\n")
    for revision in range(1, 4):
        print(f"  revision-{revision}: {inspect_revision(folder / f'revision-{revision}', revision)}")
    print("Review the coverage ledger's first gap; structural counts never certify editorial or source readiness.")


if __name__ == "__main__":
    main()
