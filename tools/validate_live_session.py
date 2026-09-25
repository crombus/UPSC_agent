"""Authoritative mechanical validator for live-session Markdown files.

This tool deliberately does not replace independent semantic review of teaching
quality, doctrine, MCQ keys, distractors, PYQ ownership, or source reliability.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL_ARC = [
    "VERIFIED PYQ LINKAGE AND ANSWER APPROACHES",
    "CUMULATIVE MCQS",
    "ORIGINAL 10-, 15- AND 20-MARK MAINS MODEL PRACTICE",
    "REMEDIATION",
    "MASTER COMPARISON, CAUSAL AND ARGUMENT MAPS",
    "COMPLETE CONSOLIDATED REGISTER NOTES",
    "COVERAGE MATRIX",
    "SOURCE LEDGER",
]
PROHIBITED_PATTERNS = [
    r"This option claims that",
    r"That conflicts with the distinction tested here",
    r"misses MCQ",
    r"controlling distinction",
    r"canonical position is",
    r"\bLAYER [1-5]\b",
    r"five-layer package",
]
SOURCE_CATEGORIES = [
    "canonical markdown",
    "final learner package",
    "layered/complete session",
    "solved workbook",
    "advanced dossier",
    "ocr books",
    "pyqs through 2026",
    "official live sources",
]
SOURCE_STATUSES = {"checked", "not available", "not relevant"}


@dataclass
class ValidationResult:
    path: str
    lessons: int
    lesson_counts: list[int]
    mcqs: int
    explanations: int
    incorrect_explanations: int
    unique_incorrect_explanations: int
    words: int
    lines: int
    sha256: str
    source_manifest: dict[str, str]
    git_status: str


class ValidationFailure(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationFailure(message)


def natural_variation(counts: list[int]) -> bool:
    if not counts or any(count < 2 or count > 4 for count in counts):
        return False
    if len(set(counts)) == 1:
        return False
    for period in (2, 3):
        if len(counts) >= period * 2 and all(
            counts[index] == counts[index % period] for index in range(len(counts))
        ):
            return False
    return True


def parse_source_manifest(raw: str, allow_missing: bool) -> dict[str, str]:
    match = re.search(
        r"(?ms)^## SOURCE-MANIFEST GATE\s*$\n(?P<body>.*?)(?=^#{1,2} |\Z)",
        raw,
    )
    if not match:
        if allow_missing:
            return {}
        fail("missing required `## SOURCE-MANIFEST GATE` section")

    rows: dict[str, tuple[str, str]] = {}
    for line in match.group("body").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        category = cells[0].lower()
        status = cells[1].lower()
        evidence = cells[2]
        if category in SOURCE_CATEGORIES:
            rows[category] = (status, evidence)

    missing = [category for category in SOURCE_CATEGORIES if category not in rows]
    if missing:
        fail(f"source manifest missing categories: {', '.join(missing)}")

    result: dict[str, str] = {}
    for category in SOURCE_CATEGORIES:
        status, evidence = rows[category]
        if status not in SOURCE_STATUSES:
            fail(
                f"source manifest status for {category!r} must be one of "
                f"{sorted(SOURCE_STATUSES)}"
            )
        if len(evidence.strip()) < 8:
            fail(f"source manifest evidence/reason is too short for {category!r}")
        result[category] = status
    return result


def run_git_diff_check(path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    completed = subprocess.run(
        ["git", "diff", "--check", "--", relative],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode:
        fail(f"scoped git diff check failed:\n{completed.stdout}{completed.stderr}")
    status = subprocess.run(
        ["git", "status", "--short", "--", relative],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return status.stdout.strip()


def validate(path: Path, allow_missing_source_manifest: bool = False) -> ValidationResult:
    path = path.resolve()
    try:
        path.relative_to(ROOT)
    except ValueError as error:
        raise ValidationFailure(f"path must be inside repository: {path}") from error
    if not path.is_file():
        fail(f"file does not exist: {path}")

    data = path.read_bytes()
    raw = data.decode("utf-8")
    if raw and not raw.endswith("\n"):
        fail("file must end with a newline")
    trailing = [
        number
        for number, line in enumerate(raw.splitlines(), start=1)
        if line.rstrip() != line
    ]
    if trailing:
        fail(f"trailing whitespace on lines: {trailing[:10]}")

    final_start = raw.find("# VERIFIED PYQ LINKAGE AND ANSWER APPROACHES")
    if final_start < 0:
        fail("missing first required final H1 heading")
    lesson_region = raw[:final_start]
    lesson_matches = list(re.finditer(r"(?m)^## Lesson (\d+)\b", lesson_region))
    if not lesson_matches:
        fail("no `## Lesson N` headings found")
    lesson_numbers = [int(match.group(1)) for match in lesson_matches]
    if lesson_numbers != list(range(1, len(lesson_matches) + 1)):
        fail(f"lesson numbering is not continuous: {lesson_numbers}")

    lesson_counts: list[int] = []
    for index, lesson in enumerate(lesson_matches):
        end = (
            lesson_matches[index + 1].start()
            if index + 1 < len(lesson_matches)
            else len(lesson_region)
        )
        chunk = lesson_region[lesson.start() : end]
        if "PRE-TEACH CHECKLIST" not in chunk:
            fail(f"Lesson {index + 1} lacks PRE-TEACH CHECKLIST")
        if not re.search(r"(?m)^Progress:", chunk):
            fail(f"Lesson {index + 1} lacks a Progress line")
        if "```" not in chunk and not re.search(r"(?m)^\|.+\|$", chunk):
            fail(f"Lesson {index + 1} lacks a visual block")
        lesson_counts.append(
            len(re.findall(r"(?m)^\*\*MCQ \d+: [A-D]\*\*$", chunk))
        )
    if not natural_variation(lesson_counts):
        fail(f"lesson MCQ counts fail natural-variation gate: {lesson_counts}")

    labels = re.findall(r"(?m)^\*\*MCQ (\d+): ([A-D])\*\*$", raw)
    numbers = [int(number) for number, _ in labels]
    answers = [answer for _, answer in labels]
    if numbers != list(range(1, len(labels) + 1)):
        fail("MCQ labels are not continuously numbered from 1")
    expected_answers = ["ABCD"[index % 4] for index in range(len(labels))]
    if answers != expected_answers:
        mismatch = next(
            index + 1
            for index, (actual, expected) in enumerate(
                zip(answers, expected_answers, strict=True)
            )
            if actual != expected
        )
        fail(f"answer rotation fails at MCQ {mismatch}")

    explanation_pattern = re.compile(
        r"(?m)^- \*\*([A-D]) — (Correct|Incorrect):\*\*\s*(.+)$"
    )
    explanations = explanation_pattern.findall(raw)
    if len(explanations) != 4 * len(labels):
        fail(
            f"expected {4 * len(labels)} option explanations, found "
            f"{len(explanations)}"
        )
    correct = [text.strip() for _, state, text in explanations if state == "Correct"]
    incorrect = [
        text.strip() for _, state, text in explanations if state == "Incorrect"
    ]
    if len(correct) != len(labels) or len(incorrect) != 3 * len(labels):
        fail("each MCQ must have one correct and three incorrect explanations")
    if len(set(incorrect)) != len(incorrect):
        fail(
            f"incorrect explanations are not unique: "
            f"{len(set(incorrect))}/{len(incorrect)}"
        )

    h1_headings = re.findall(r"(?m)^# (.+)$", raw)
    if h1_headings[-len(FINAL_ARC) :] != FINAL_ARC:
        fail("final H1 arc does not exactly match the required order")
    prohibited = [
        pattern
        for pattern in PROHIBITED_PATTERNS
        if re.search(pattern, raw, flags=re.IGNORECASE)
    ]
    if prohibited:
        fail(f"prohibited wording found: {prohibited}")
    if raw.count("```") % 2:
        fail("unbalanced fenced code blocks")

    source_manifest = parse_source_manifest(raw, allow_missing_source_manifest)
    git_status = run_git_diff_check(path)
    return ValidationResult(
        path=path.relative_to(ROOT).as_posix(),
        lessons=len(lesson_matches),
        lesson_counts=lesson_counts,
        mcqs=len(labels),
        explanations=len(explanations),
        incorrect_explanations=len(incorrect),
        unique_incorrect_explanations=len(set(incorrect)),
        words=len(re.findall(r"\S+", raw)),
        lines=len(raw.splitlines()),
        sha256=hashlib.sha256(data).hexdigest(),
        source_manifest=source_manifest,
        git_status=git_status,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--allow-missing-source-manifest",
        action="store_true",
        help="Audit a legacy released file; forbidden in release automation.",
    )
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = validate(
            args.path,
            allow_missing_source_manifest=args.allow_missing_source_manifest,
        )
    except (OSError, UnicodeError, subprocess.SubprocessError, ValidationFailure) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    else:
        print("PASS")
        for key, value in asdict(result).items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
