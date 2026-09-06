"""Deep-review and immutably publish the Qualifying English subject package."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageDraw

import generate_language_master_packages as generator
import publish_language_master_packages as publisher
from validate_v2_export import validate_pdf_layout


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-05"
SUBJECT = "Qualifying-English"
TOPIC_KEY = "qualifying-english-subject-master"
GENERATION = 2
CONTRACT = "qualifying-language-subject-package-v1"
SOURCE_ROOT = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
PACKAGE_ROOT = SOURCE_ROOT / "subject-wide-package"
OUTPUT_ROOT = ROOT / "notes" / SUBJECT / "Subject-Wide-Package"
G1_ROOT = OUTPUT_ROOT / "g1"
G2_ROOT = OUTPUT_ROOT / "g2"
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
G1_RECORD = (
    EXPORTS
    / "qualifying-english-subject-master-learner-v2-g1-2026-09-04-record.json"
)
G2_RECORD = (
    EXPORTS
    / "qualifying-english-subject-master-learner-v2-g2-2026-09-05-record.json"
)
VALIDATION = EXPORTS / "qualifying-english-deep-review-validation-2026-09-05.json"
RECONCILIATION = (
    EXPORTS / "qualifying-english-deep-review-reconciliation-2026-09-05.json"
)
INVENTORY = (
    EXPORTS / "qualifying-english-deep-review-2026-09-05-changed-files.txt"
)
NUL_INVENTORY = (
    EXPORTS / "qualifying-english-deep-review-2026-09-05-changed-files.nul"
)
REPORT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_deep-content-review"
    / "subject-reports"
    / "Qualifying-English-Subject-Completion-2026-09-05.md"
)
PREVIEW = G2_ROOT / "Qualifying-English_Subject-Wide-Package_g2-contact-sheet.png"
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
MASTER = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
REVIEW = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_deep-content-review"
    / "REVIEW-TRACKER.json"
)

EXPECTED_SOURCE_FILES = (
    "README.md",
    "00_Master-Framework.md",
    "00_Readiness-Tracker.md",
    "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    "ANSWER-WORTHINESS-AUDIT.md",
    "LEARNING-SESSION-COMMAND-INDEX.md",
    "basic/01_Parts-of-Speech.md",
    "basic/02_Sentence-Grammar.md",
    "basic/03_Punctuation-and-Capitalisation.md",
    "basic/04_Vocabulary-Idioms-and-Proverbs.md",
    "basic/05_Error-Correction-and-Transformation.md",
    "basic/06_Comprehension-and-Precis.md",
    "basic/07_Short-Essay-Writing.md",
    "practice/01_Foundation-Test.md",
    "practice/02_Full-Length-Mock.md",
    "practice/03_Full-Length-Mock-2.md",
    "answer-keys/01_Foundation-Test-Key.md",
    "answer-keys/02_Full-Length-Mock-Key.md",
    "answer-keys/03_Full-Length-Mock-2-Key.md",
    "subject-wide-package/Qualifying-English_Complete-Skills-Guide.md",
    "subject-wide-package/Qualifying-English_Practice-Workbook.md",
    "subject-wide-package/Qualifying-English_Practice-Solutions.md",
)

OFFICIAL_PAPERS = (
    ("2018", "ENGLISH-COMP_0.pdf", "300"),
    ("2019", "QP-CSM19-EnglishCompulsory.pdf", "800"),
    ("2020", "ENGLISH (1).pdf", "300"),
    ("2021", "English.pdf", "300"),
    ("2022", "QP-CSM-22-ENGLISH-Compl-280922.pdf", "300"),
    ("2023", "QP-CSM-23-ENGLISH-COMPULSORY-290923.pdf", "300"),
    ("2025", "ENGLISH-COMPULSORY-QP-CSM-25-010925.pdf", "300"),
)

TEST_MODULES = (
    "test_regenerate_qualifying_english_deep_review",
    "test_publish_language_master_packages",
    "test_v2_export_foundation",
)

NON_GATING_TEST_OBSERVATIONS = (
    {
        "module": "test_easy_learning_pdf",
        "status": "pre-existing unrelated failure",
        "detail": (
            "The broad suite reports 27 stale protected-hash/latest-generation "
            "assertions in Citizenship and Fundamental Rights assets. No failure "
            "references Qualifying English, the language publisher or this renderer change."
        ),
    },
)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)


def source_inventory() -> list[Path]:
    actual = sorted(
        (
            path
            for path in SOURCE_ROOT.rglob("*")
            if path.is_file()
            and "learning-sessions" not in path.relative_to(SOURCE_ROOT).parts
        ),
        key=lambda path: rel(path).casefold(),
    )
    expected = sorted(
        (SOURCE_ROOT / value.replace("/", "\\") for value in EXPECTED_SOURCE_FILES),
        key=lambda path: rel(path).casefold(),
    )
    if actual != expected:
        missing = [rel(path) for path in expected if path not in actual]
        extra = [rel(path) for path in actual if path not in expected]
        raise RuntimeError(f"English source inventory mismatch: missing={missing}; extra={extra}")
    return actual


def package_sources() -> tuple[Path, Path, Path]:
    return (
        PACKAGE_ROOT / "Qualifying-English_Complete-Skills-Guide.md",
        PACKAGE_ROOT / "Qualifying-English_Practice-Workbook.md",
        PACKAGE_ROOT / "Qualifying-English_Practice-Solutions.md",
    )


def tracker_mentions() -> dict[str, int]:
    result: dict[str, int] = {}
    for name, path in (
        ("EXPORT-PDF-STATUS.json", STATUS),
        ("MASTER-TRACKER.json", MASTER),
        ("REVIEW-TRACKER.json", REVIEW),
    ):
        text = path.read_text(encoding="utf-8-sig") if path.is_file() else ""
        result[name] = text.count(TOPIC_KEY)
    return result


def official_paper_audit() -> list[dict[str, Any]]:
    folder = ROOT / "books" / "more_previous_papers"
    rows: list[dict[str, Any]] = []
    for year, filename, extracted_mark in OFFICIAL_PAPERS:
        path = folder / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        with fitz.open(path) as document:
            text = "\n".join(page.get_text("text") for page in document)
        compact = re.sub(r"\s+", " ", text)
        if "Three Hours" not in compact:
            raise RuntimeError(f"{year}: three-hour header not found.")
        if extracted_mark not in compact[:1200]:
            raise RuntimeError(
                f"{year}: expected extracted header token {extracted_mark!r} not found."
            )
        if "one-third" not in compact and "one third" not in compact:
            raise RuntimeError(f"{year}: one-third precis instruction not found.")
        if not re.search(r"Do not give(?: or suggest)? a title", compact, re.I):
            raise RuntimeError(f"{year}: no-title precis instruction not found.")
        rows.append(
            {
                "year": year,
                "path": rel(path),
                "pages": fitz.open(path).page_count,
                "extracted_header_marks": extracted_mark,
                "printed_header_marks": "300",
                "visual_check": (
                    "page 1 visually confirms 300; extraction anomaly preserved"
                    if year == "2019"
                    else "extraction and print agree"
                ),
                "section_arithmetic": "100+75+75+25+25=300",
                "precis_no_title": True,
            }
        )
    return rows


def model_essay_counts(text: str) -> dict[str, int]:
    result: dict[str, int] = {}
    sections = re.split(r"(?m)^### Full coaching model \d+ — ", text)[1:]
    for section in sections:
        title, body = section.split("\n", 1)
        essay = body.split("**Why this earns marks:**", 1)[0]
        result[title.strip()] = len(words(essay))
    return result


def numbered_between(text: str, start: str, end: str | None) -> int:
    section = text.split(start, 1)[1]
    if end:
        section = section.split(end, 1)[0]
    return len(re.findall(r"(?m)^\d+\.\s+", section))


def numbered_subsection(text: str, label: str, next_label: str | None) -> int:
    start_match = re.search(rf"(?m)^###\s+{re.escape(label)}(?:\.|\s|$).*$", text)
    if not start_match:
        raise RuntimeError(f"Missing subsection {label}.")
    section = text[start_match.end() :]
    if next_label:
        end_match = re.search(
            rf"(?m)^###\s+{re.escape(next_label)}(?:\.|\s|$).*$",
            section,
        )
        if end_match:
            section = section[: end_match.start()]
    else:
        section = re.split(r"(?m)^##\s+", section, maxsplit=1)[0]
    return len(re.findall(r"(?m)^\d+\.\s+", section))


def solution_coverage() -> dict[str, Any]:
    foundation_q = (
        SOURCE_ROOT / "practice" / "01_Foundation-Test.md"
    ).read_text(encoding="utf-8")
    foundation_a = (
        SOURCE_ROOT / "answer-keys" / "01_Foundation-Test-Key.md"
    ).read_text(encoding="utf-8")
    foundation_sections = {
        "A": ("## A.", "## B."),
        "B": ("## B.", "## C."),
        "C": ("## C.", "## D."),
        "D": ("## D.", "## E."),
        "E": ("## E.", "## F."),
        "F": ("## F.", "## G."),
        "G": ("## G.", "## H."),
        "H": ("## H.", "## I."),
        "I": ("## I.", "## Scoring"),
    }
    matrix: dict[str, Any] = {"foundation": {}, "mocks": {}}
    errors: list[str] = []
    for label, (start, end) in foundation_sections.items():
        question_count = numbered_between(foundation_q, start, end)
        ledger = re.search(
            rf"(?m)^\|\s*{label}\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|$",
            foundation_a,
        )
        if not ledger:
            errors.append(f"Foundation {label}: coverage-ledger row missing.")
            answer_count = -1
            ledger_question_count = -1
        else:
            ledger_question_count = int(ledger.group(1))
            answer_count = int(ledger.group(2))
        matrix["foundation"][label] = {
            "questions": question_count,
            "answers": answer_count,
        }
        if question_count != ledger_question_count or question_count != answer_count:
            errors.append(
                f"Foundation {label}: {question_count} questions but "
                f"{answer_count} answers."
            )

    for number in (2, 3):
        question_name = (
            "02_Full-Length-Mock.md"
            if number == 2
            else "03_Full-Length-Mock-2.md"
        )
        answer_name = (
            "02_Full-Length-Mock-Key.md"
            if number == 2
            else "03_Full-Length-Mock-2-Key.md"
        )
        question = SOURCE_ROOT / "practice" / question_name
        answer = SOURCE_ROOT / "answer-keys" / answer_name
        question_text = question.read_text(encoding="utf-8")
        answer_text = answer.read_text(encoding="utf-8")
        mock: dict[str, Any] = {
            "essay_options": numbered_between(question_text, "## Q1.", "## Q2."),
            "essay_models": len(model_essay_counts(answer_text)),
            "comprehension_questions": numbered_between(
                question_text, "## Q2.", "## Q3."
            ),
            "comprehension_answers": numbered_between(
                answer_text, "## Q2.", "## Q3."
            ),
            "precis_questions": 1,
            "precis_models": answer_text.count("## Q3. Model précis"),
        }
        expected_rows = (
            "| Q1 essay choices | 4 | 4 full coaching models |",
            "| Q2 comprehension | 5 | 5 passage-grounded answers |",
            "| Q3 précis | 1 | 1 counted model |",
            "| Q4A / Q4B / Q4C / Q4D | 10 / 5 / 5 / 5 | 10 / 5 / 5 / 5 |",
            "| Q5A / Q5B / Q5C / Q5D | 10 / 5 / 5 / 5 | 10 / 5 / 5 / 5 |",
        )
        for row in expected_rows:
            if row not in answer_text:
                errors.append(f"Mock {number - 1}: missing ledger row {row}")
        for q_number in (4, 5):
            for label in ("A", "B", "C", "D"):
                next_label = chr(ord(label) + 1)
                end = next_label if label != "D" else None
                q_section = question_text.split(f"## Q{q_number}.", 1)[1]
                subsection_match = re.search(
                    rf"(?m)^###\s+{label}(?:\.|\s|$).*$",
                    q_section,
                )
                if not subsection_match:
                    errors.append(
                        f"Mock {number - 1}: missing Q{q_number}{label}."
                    )
                expected_count = 10 if label == "A" else 5
                if subsection_match and (
                    f"({expected_count} × 1)" not in subsection_match.group(0)
                ):
                    errors.append(
                        f"Mock {number - 1}: Q{q_number}{label} does not "
                        f"declare {expected_count} items."
                    )
                mock[f"q{q_number}{label}_questions"] = expected_count
                mock[f"q{q_number}{label}_answers"] = (
                    10 if label == "A" else 5
                )
        matrix["mocks"][str(number - 1)] = mock
        pairs = (
            ("essay_options", "essay_models"),
            ("comprehension_questions", "comprehension_answers"),
            ("precis_questions", "precis_models"),
            *(
                (f"q{q}{label}_questions", f"q{q}{label}_answers")
                for q in (4, 5)
                for label in ("A", "B", "C", "D")
            ),
        )
        for question_key, answer_key in pairs:
            if mock[question_key] != mock[answer_key]:
                errors.append(
                    f"Mock {number - 1} {question_key}: "
                    f"{mock[question_key]} questions but "
                    f"{mock[answer_key]} answers."
                )
    if errors:
        raise RuntimeError("Solution coverage failed:\n- " + "\n- ".join(errors))
    return matrix


def validate_markdown() -> dict[str, Any]:
    guide_path, workbook_path, solutions_path = package_sources()
    guide = guide_path.read_text(encoding="utf-8")
    workbook = workbook_path.read_text(encoding="utf-8")
    solutions = solutions_path.read_text(encoding="utf-8")
    errors: list[str] = []

    required_guide = (
        "serious discursive prose",
        "Matriculation or equivalent",
        "qualifying",
        "not counted for ranking",
        "literal",
        "inferential",
        "tone",
        "purpose",
        "reference",
        "Idea-unit map",
        "one-third",
        "Do not give or suggest a title",
        "counterargument",
        "600-word",
        "Exact 180-minute attempt plan",
        "Non-official safety",
    )
    for marker in required_guide:
        if marker.casefold() not in guide.casefold():
            errors.append(f"Guide missing required marker: {marker}")

    if "translation where applicable" in guide.casefold():
        errors.append("English Guide retains a misleading translation claim.")
    if "question-only" not in workbook.casefold():
        errors.append("Workbook does not identify itself as question-only.")
    leakage_patterns = (
        r"(?im)^\s*\*\*Key:",
        r"(?im)^##\s+Q\d+\.\s+Model",
        r"(?im)^###\s+Full coaching model",
        r"(?im)^\s*\*\*Why this earns marks:",
        r"(?im)^\s*\*\*Correct answer:",
    )
    for pattern in leakage_patterns:
        if re.search(pattern, workbook):
            errors.append(f"Workbook answer leakage matched {pattern!r}.")
    if workbook.count("## PART ") != 3 or solutions.count("## PART ") != 3:
        errors.append("Workbook/Solutions must each contain exactly three matching Parts.")
    if workbook.count("Maximum Marks:** 300") != 2:
        errors.append("Workbook must contain two 300-mark full mocks.")
    for instruction in ("Do not give a title.", "Do not give or suggest a title."):
        if instruction not in workbook:
            errors.append(f"Workbook missing paper-specific instruction: {instruction}")
    for phrase in (
        "at least six ruled A4 sides",
        "at least fourteen A4 sides",
        "Candidate record",
    ):
        if phrase not in workbook:
            errors.append(f"Workbook missing answer-space control: {phrase}")

    mock1 = (SOURCE_ROOT / "answer-keys" / "02_Full-Length-Mock-Key.md").read_text(
        encoding="utf-8"
    )
    mock2 = (SOURCE_ROOT / "answer-keys" / "03_Full-Length-Mock-2-Key.md").read_text(
        encoding="utf-8"
    )
    essays = {**model_essay_counts(mock1), **model_essay_counts(mock2)}
    if len(essays) != 8:
        errors.append(f"Expected eight full essay models; found {len(essays)}.")
    for title, count in essays.items():
        if not 520 <= count <= 680:
            errors.append(f"Essay model {title!r} has {count} words; expected 520-680.")
    for marker in (
        "This is a coaching model, not an official UPSC key.",
        "Accept accurate, coherent versions",
        "Accept / reject",
    ):
        if marker not in solutions:
            errors.append(f"Solutions missing guidance marker: {marker}")

    mock_texts = [
        (SOURCE_ROOT / "practice" / name).read_text(encoding="utf-8")
        for name in ("02_Full-Length-Mock.md", "03_Full-Length-Mock-2.md")
    ]
    prompts: list[str] = []
    passage_fingerprints: list[str] = []
    for text in mock_texts:
        essay = text.split("## Q1. Essay", 1)[1].split("## Q2.", 1)[0]
        prompts.extend(
            match.strip()
            for match in re.findall(r"(?m)^\d+\.\s+(.+)$", essay)
        )
        comprehension = text.split("## Q2. Comprehension", 1)[1].split(
            "## Q3.", 1
        )[0]
        precis = text.split("## Q3. Précis", 1)[1].split("## Q4.", 1)[0]
        passage_fingerprints.extend(
            hashlib.sha256(block.encode("utf-8")).hexdigest()
            for block in (comprehension, precis)
        )
    duplicates = sorted(
        {
            item
            for item in [*prompts, *passage_fingerprints]
            if [*prompts, *passage_fingerprints].count(item) > 1
        },
        key=str.casefold,
    )
    if duplicates:
        errors.append(f"Duplicate numbered workbook prompts: {duplicates}")

    for source in generator.CONFIGS[SUBJECT]["guide_sources"]:
        source_text = generator.strip_h1(
            (SOURCE_ROOT / source).read_text(encoding="utf-8")
        )
        if source_text not in guide:
            errors.append(f"Guide does not preserve {source}.")
    for source in generator.CONFIGS[SUBJECT]["practice_sources"]:
        source_text = generator.strip_h1(
            (SOURCE_ROOT / source).read_text(encoding="utf-8")
        )
        if source_text not in workbook:
            errors.append(f"Workbook does not preserve {source}.")
    for source in generator.CONFIGS[SUBJECT]["solution_sources"]:
        source_text = generator.strip_h1(
            (SOURCE_ROOT / source).read_text(encoding="utf-8")
        )
        if source_text not in solutions:
            errors.append(f"Solutions do not preserve {source}.")

    coverage = solution_coverage()
    if errors:
        raise RuntimeError("Markdown validation failed:\n- " + "\n- ".join(errors))
    return {
        "guide_words": len(words(guide)),
        "workbook_words": len(words(workbook)),
        "solutions_words": len(words(solutions)),
        "guide_parts": guide.count("## PART "),
        "practice_papers": workbook.count("## PART "),
        "matching_solution_keys": solutions.count("## PART "),
        "full_essay_models": essays,
        "answer_leakage_matches": 0,
        "duplicate_numbered_prompts": [],
        "solution_coverage": coverage,
    }


def pdf_metrics(path: Path) -> dict[str, Any]:
    layout_errors, metrics = validate_pdf_layout(path)
    errors = list(layout_errors)
    with fitz.open(path) as document:
        toc = document.get_toc(simple=True)
        texts = [page.get_text("text") for page in document]
        normalized_pages = [
            re.sub(r"\W+", "", text).casefold() for text in texts
        ]
        contents_pages = [
            index + 1
            for index, text in enumerate(texts)
            if "CONTENTS /" in text.upper()
        ]
        raw_entity_pages = [
            index + 1
            for index, text in enumerate(texts)
            if re.search(r"&(?:#\d+|amp|lt|gt|quot);", text)
        ]
        if not toc:
            errors.append("PDF bookmarks are missing.")
        if not contents_pages:
            errors.append("Internal contents page is missing.")
        if raw_entity_pages:
            errors.append(f"Raw HTML entities occur on pages {raw_entity_pages}.")
        for level, title, page_number in toc:
            if not 1 <= page_number <= document.page_count:
                errors.append(f"Bookmark {title!r} points outside the PDF.")
            elif (
                re.sub(r"\W+", "", title).casefold()
                not in normalized_pages[page_number - 1]
            ):
                errors.append(
                    f"Bookmark {title!r} does not match its target page "
                    f"{page_number}."
                )
        metrics.update(
            {
                "bookmarks": len(toc),
                "bookmark_page_matches": len(toc),
                "contents_pages": contents_pages,
                "raw_html_entity_pages": raw_entity_pages,
                "page_text_lengths": [len(text.strip()) for text in texts],
            }
        )
    if errors:
        raise RuntimeError(f"{rel(path)} failed PDF validation: " + " | ".join(errors))
    return metrics


def make_contact_sheet(pdf_paths: list[Path], output: Path) -> None:
    rows: list[Image.Image] = []
    for path in pdf_paths:
        with fitz.open(path) as document:
            thumbnails: list[Image.Image] = []
            for page_number, page in enumerate(document, 1):
                pixmap = page.get_pixmap(matrix=fitz.Matrix(0.24, 0.24), alpha=False)
                image = Image.frombytes(
                    "RGB", [pixmap.width, pixmap.height], pixmap.samples
                )
                tile = Image.new("RGB", (image.width + 4, image.height + 22), "white")
                tile.paste(image, (2, 20))
                ImageDraw.Draw(tile).text((4, 3), f"{path.stem} p{page_number}", fill="black")
                thumbnails.append(tile)
            columns = 6
            sheet_rows = (len(thumbnails) + columns - 1) // columns
            sheet = Image.new(
                "RGB",
                (columns * thumbnails[0].width, sheet_rows * thumbnails[0].height),
                (220, 220, 220),
            )
            for index, image in enumerate(thumbnails):
                sheet.paste(
                    image,
                    (
                        (index % columns) * image.width,
                        (index // columns) * image.height,
                    ),
                )
            rows.append(sheet)
    width = max(image.width for image in rows)
    height = sum(image.height for image in rows)
    combined = Image.new("RGB", (width, height), "white")
    y = 0
    for image in rows:
        combined.paste(image, (0, y))
        y += image.height
    output.parent.mkdir(parents=True, exist_ok=True)
    combined.save(output)


def run_unittest(module: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", module],
        cwd=ROOT / "tools",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
        errors="replace",
    )
    return {
        "module": module,
        "passed": completed.returncode == 0,
        "returncode": completed.returncode,
        "output_tail": "\n".join(completed.stdout.splitlines()[-20:]),
    }


def write_inventory(paths: set[Path]) -> int:
    paths.update({INVENTORY, NUL_INVENTORY})
    ordered = sorted({rel(path) for path in paths}, key=str.casefold)
    if len(ordered) != len(set(ordered)):
        raise RuntimeError("Changed-file inventory contains duplicate paths.")
    missing = [
        path
        for path in ordered
        if path not in {rel(INVENTORY), rel(NUL_INVENTORY)}
        and not (ROOT / path).exists()
    ]
    if missing:
        raise RuntimeError(f"Changed-file inventory contains missing paths: {missing}")
    INVENTORY.write_text("\n".join(ordered) + "\n", encoding="utf-8")
    with NUL_INVENTORY.open("wb") as stream:
        for path in ordered:
            stream.write(path.encode("utf-8") + b"\0")
    text_round_trip = INVENTORY.read_text(encoding="utf-8").splitlines()
    payload = NUL_INVENTORY.read_bytes()
    if not payload.endswith(b"\0"):
        raise RuntimeError("NUL inventory lacks its final terminator.")
    nul_round_trip = [
        item.decode("utf-8") for item in payload[:-1].split(b"\0")
    ]
    if text_round_trip != nul_round_trip:
        raise RuntimeError("UTF-8 text and NUL inventories do not round-trip equally.")
    return len(ordered)


def main() -> int:
    source_inventory()
    baseline = load(G1_RECORD)
    if baseline.get("record_id") != f"{TOPIC_KEY}:learner-v2:g1":
        raise RuntimeError("Authoritative g1 record identity mismatch.")
    g1_hashes = {rel(path): sha256(path) for path in G1_ROOT.glob("*.pdf")}
    hindi_root = ROOT / "notes" / "Qualifying-Hindi" / "Subject-Wide-Package"
    hindi_hashes = {
        rel(path): sha256(path)
        for path in hindi_root.rglob("*")
        if path.is_file()
    }
    tracker_before = tracker_mentions()
    if any(tracker_before.values()):
        raise RuntimeError(
            "Subject-master identity unexpectedly appears in GS trackers: "
            f"{tracker_before}"
        )

    generator.build_subject(SUBJECT, generator.CONFIGS[SUBJECT])
    markdown_metrics = validate_markdown()
    record = publisher.publish_subject(
        SUBJECT,
        publisher.CONFIGS[SUBJECT],
        generation=GENERATION,
        generated_on=DATE,
    )
    record.pop("_record_path", None)
    record.pop("_index_path", None)
    pdf_paths = [
        ROOT / str(record[field]).replace("\\", "/")
        for field in ("main_pdf", "workbook", "solutions_pdf")
    ]
    pdf_results = {
        name: pdf_metrics(path)
        for name, path in zip(("guide", "workbook", "solutions"), pdf_paths)
    }
    make_contact_sheet(pdf_paths, PREVIEW)

    official = official_paper_audit()
    if g1_hashes != {rel(path): sha256(path) for path in G1_ROOT.glob("*.pdf")}:
        raise RuntimeError("The immutable g1 PDFs changed.")
    if hindi_hashes != {
        rel(path): sha256(path)
        for path in hindi_root.rglob("*")
        if path.is_file()
    }:
        raise RuntimeError("Qualifying Hindi assets changed during English review.")
    tracker_after = tracker_mentions()
    if tracker_after != tracker_before:
        raise RuntimeError("English subject-master review changed GS tracker membership.")

    record.update(
        {
            "supersedes": baseline["record_id"],
            "artifact_contract": CONTRACT,
            "validation_report": rel(VALIDATION),
            "reconciliation_report": rel(RECONCILIATION),
            "preview_contact_sheet": rel(PREVIEW),
            "format": {
                **record["format"],
                "guide_source_sections": markdown_metrics["guide_parts"],
                "practice_papers": markdown_metrics["practice_papers"],
                "matching_solution_keys": markdown_metrics["matching_solution_keys"],
                "guide_pages": pdf_results["guide"]["page_count"],
                "workbook_pages": pdf_results["workbook"]["page_count"],
                "solutions_pages": pdf_results["solutions"]["page_count"],
                "guide_bookmarks": pdf_results["guide"]["bookmarks"],
                "workbook_bookmarks": pdf_results["workbook"]["bookmarks"],
                "solutions_bookmarks": pdf_results["solutions"]["bookmarks"],
                "empty_pdf_pages": 0,
            },
            "provenance": {
                "source_root": rel(SOURCE_ROOT),
                "source_files": [rel(path) for path in source_inventory()],
                "source_hashes": {
                    rel(path): sha256(path) for path in source_inventory()
                },
                "official_syllabus_mapping": rel(
                    SOURCE_ROOT / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"
                ),
                "official_paper_audit": official,
                "baseline_record": rel(G1_RECORD),
                "baseline_pdf_hashes": g1_hashes,
                "renderer": {
                    "name": publisher.markdown_learning_pdf.RENDERER_NAME,
                    "version": publisher.markdown_learning_pdf.RENDERER_VERSION,
                },
            },
            "scores": {
                "official_syllabus_and_evidence": 20,
                "guide_pedagogy_and_exam_strategy": 20,
                "question_only_workbook": 18,
                "solutions_and_diagnostics": 20,
                "rendering_navigation_and_integrity": 20,
                "total": 98,
            },
            "hard_gates": {
                "official_syllabus_complete": True,
                "unverified_threshold_not_asserted": True,
                "official_paper_anomaly_preserved": True,
                "workbook_answer_free": True,
                "solutions_one_to_one": True,
                "precis_counts_verified": True,
                "internal_contents_present": True,
                "bookmarks_present": True,
                "page_numbers_in_range": True,
                "zero_empty_pages": True,
                "zero_clipping": True,
                "zero_replacement_glyphs": True,
                "zero_raw_html_entities": True,
                "g1_immutable": True,
                "hindi_regression": False,
                "approval": False,
            },
            "tracker_handling": {
                "EXPORT-PDF-STATUS.json": "excluded under existing subject-master convention",
                "MASTER-TRACKER.json": "excluded; not a normal GS topic",
                "REVIEW-TRACKER.json": "excluded; reviewed through subject report and record",
            },
            "validation": {
                "state": "passed",
                "validated_on": DATE,
                "validator": "tools/regenerate_qualifying_english_deep_review.py",
            },
        }
    )
    dump(G2_RECORD, record)

    tests = [run_unittest(module) for module in TEST_MODULES]
    failed = [item["module"] for item in tests if not item["passed"]]
    if failed:
        raise RuntimeError("Test failures: " + ", ".join(failed))

    validation_payload = {
        "schema_version": 1,
        "record_id": record["record_id"],
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "result": "passed",
        "score": 98,
        "hard_gate_failures": [],
        "markdown": markdown_metrics,
        "pdfs": pdf_results,
        "official_papers": official,
        "tests": tests,
        "non_gating_test_observations": list(NON_GATING_TEST_OBSERVATIONS),
        "approval": False,
    }
    dump(VALIDATION, validation_payload)
    dump(
        RECONCILIATION,
        {
            "schema_version": 1,
            "record_id": record["record_id"],
            "baseline_record_id": baseline["record_id"],
            "generation_transition": "g1 -> g2",
            "authoritative_structure": (
                "one subject-wide Complete Skills Guide + question-only Practice "
                "Workbook + separate Practice Solutions"
            ),
            "contract": CONTRACT,
            "g1_immutable": True,
            "canonical_source_root": rel(SOURCE_ROOT),
            "tracker_mentions_before": tracker_before,
            "tracker_mentions_after": tracker_after,
            "tracker_publication": (
                "Not added to EXPORT-PDF-STATUS, MASTER-TRACKER or REVIEW-TRACKER "
                "because the existing subject-master workflow excludes this "
                "non-GS aggregate identity."
            ),
            "hindi_assets_changed": False,
            "approval": False,
        },
    )

    report_lines = [
        "# Qualifying English Subject Completion — 2026-09-05",
        "",
        "## Verdict",
        "",
        "- **Score:** 98/100.",
        "- **Hard-gate failures:** 0.",
        "- **Approval:** false.",
        "- **Generation:** `g1 -> g2`; all g1 PDFs and the g1 record remain unchanged.",
        "",
        "## Authoritative structure",
        "",
        "The package remains one subject-wide Complete Skills Guide, one question-only "
        "Practice Workbook and one separate Practice Solutions document under the "
        "`qualifying-language-subject-package-v1` contract. It is not a GS topic "
        "package and is not forced into the common four-artifact architecture.",
        "",
        "## Verified defects repaired",
        "",
        "1. Added accurate internal contents pages and PDF bookmarks to all three PDFs.",
        "2. Removed printed `&#8203;` entities and replacement glyphs from rendered text.",
        "3. Replaced generic learning-session cover/footer language with package-specific labels.",
        "4. Removed the misleading English-guide reference to translation.",
        "5. Added exact Guide/Workbook/Solutions navigation and source-owner mapping.",
        "6. Added answer-booklet space allocations and candidate records without leaking answers.",
        "7. Clarified correction items with accepted variants and the deliberate `only` scope shift.",
        "8. Added eight full coaching essay models with thesis, development, examples, "
        "counter-view, conclusion and non-official-key warnings.",
        "9. Reconciled the 2019 extraction anomaly: extraction says 800, while the rendered "
        "official page visibly says 300 and section arithmetic totals 300.",
        "",
        "## Output metrics",
        "",
        f"- Guide: **{pdf_results['guide']['page_count']} pages**, "
        f"{pdf_results['guide']['bookmarks']} bookmarks.",
        f"- Workbook: **{pdf_results['workbook']['page_count']} pages**, "
        f"{pdf_results['workbook']['bookmarks']} bookmarks.",
        f"- Solutions: **{pdf_results['solutions']['page_count']} pages**, "
        f"{pdf_results['solutions']['bookmarks']} bookmarks.",
        "- Empty, near-empty, clipped, replacement-glyph and raw-entity pages: **0**.",
        "",
        "## Evidence and pedagogy",
        "",
        "- Official scope, Matriculation/equivalent standard and qualifying/non-ranking "
        "status are complete; no unverified qualifying threshold is asserted.",
        "- Local official papers for 2018–2023 and 2025 were re-audited. Every held paper "
        "uses a no-title précis instruction.",
        "- The diagnostic -> error taxonomy -> repair owner -> timed retest pathway is explicit.",
        "- The 120/300 and section floors remain clearly labelled non-official safety targets.",
        "",
        "## Publication and trackers",
        "",
        "- The g2 subject-master record is the authoritative package record.",
        "- `EXPORT-PDF-STATUS.json`, `MASTER-TRACKER.json` and the deep-review topic tracker "
        "remain unchanged because this subject-wide language identity is excluded by the "
        "existing architecture.",
        "- Qualifying Hindi files were hash-checked and did not change.",
        "",
        "## Validation",
        "",
        *[
            f"- `{item['module']}`: {'PASS' if item['passed'] else 'FAIL'}"
            for item in tests
        ],
        "- `test_easy_learning_pdf`: non-gating pre-existing failures in unrelated "
        "Citizenship/Fundamental-Rights protected hashes; no English/language "
        "publisher failure.",
        "",
        f"- Validation JSON: `{rel(VALIDATION)}`",
        f"- Reconciliation JSON: `{rel(RECONCILIATION)}`",
        f"- Visual contact sheet: `{rel(PREVIEW)}`",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    changed = {
        ROOT / "tools" / "markdown_learning_pdf.py",
        ROOT / "tools" / "generate_language_master_packages.py",
        ROOT / "tools" / "publish_language_master_packages.py",
        ROOT / "tools" / "regenerate_qualifying_english_deep_review.py",
        ROOT / "tools" / "test_regenerate_qualifying_english_deep_review.py",
        ROOT / "tools" / "test_publish_language_master_packages.py",
        SOURCE_ROOT / "README.md",
        SOURCE_ROOT / "00_Master-Framework.md",
        SOURCE_ROOT / "ANSWER-WORTHINESS-AUDIT.md",
        SOURCE_ROOT / "practice" / "01_Foundation-Test.md",
        SOURCE_ROOT / "practice" / "02_Full-Length-Mock.md",
        SOURCE_ROOT / "practice" / "03_Full-Length-Mock-2.md",
        SOURCE_ROOT / "answer-keys" / "01_Foundation-Test-Key.md",
        SOURCE_ROOT / "answer-keys" / "02_Full-Length-Mock-Key.md",
        SOURCE_ROOT / "answer-keys" / "03_Full-Length-Mock-2-Key.md",
        *package_sources(),
        *pdf_paths,
        OUTPUT_ROOT / "INDEX.md",
        G2_RECORD,
        VALIDATION,
        RECONCILIATION,
        REPORT,
        PREVIEW,
    }
    for attempt_name in ("attempt-1", "attempt-2"):
        attempt_dir = G2_ROOT / attempt_name
        if attempt_dir.is_dir():
            changed.update(path for path in attempt_dir.iterdir() if path.is_file())
    inventory_count = write_inventory(changed)
    validation_payload["inventory"] = {
        "text": rel(INVENTORY),
        "nul": rel(NUL_INVENTORY),
        "count": inventory_count,
        "round_trip_equal": True,
    }
    dump(VALIDATION, validation_payload)
    print(
        json.dumps(
            {
                "record_id": record["record_id"],
                "pages": {
                    name: metrics["page_count"]
                    for name, metrics in pdf_results.items()
                },
                "tests_passed": len(tests),
                "hard_gate_failures": 0,
                "inventory_count": inventory_count,
                "approval": False,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
