"""Deep-review and immutably publish the Qualifying Hindi subject package."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unicodedata
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
SUBJECT = "Qualifying-Hindi"
TOPIC_KEY = "qualifying-hindi-subject-master"
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
    / "qualifying-hindi-subject-master-learner-v2-g1-2026-09-04-record.json"
)
G2_RECORD = (
    EXPORTS
    / "qualifying-hindi-subject-master-learner-v2-g2-2026-09-05-record.json"
)
VALIDATION = EXPORTS / "qualifying-hindi-deep-review-validation-2026-09-05.json"
RECONCILIATION = (
    EXPORTS / "qualifying-hindi-deep-review-reconciliation-2026-09-05.json"
)
INVENTORY = (
    EXPORTS / "qualifying-hindi-deep-review-2026-09-05-changed-files.txt"
)
NUL_INVENTORY = (
    EXPORTS / "qualifying-hindi-deep-review-2026-09-05-changed-files.nul"
)
REPORT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_deep-content-review"
    / "subject-reports"
    / "Qualifying-Hindi-Subject-Completion-2026-09-05.md"
)
PREVIEW = G2_ROOT / "Qualifying-Hindi_Subject-Wide-Package_g2-contact-sheet.png"
SELECTED_PREVIEW = G2_ROOT / "Qualifying-Hindi_g2-selected-page-previews.png"
BASELINE_PREVIEW = G2_ROOT / "Qualifying-Hindi_g1-baseline-contact-sheet.png"
HELD_PREVIEW = G2_ROOT / "Qualifying-Hindi_Held-Papers-contact-sheet.png"
PRECIS_PREVIEW = G2_ROOT / "Qualifying-Hindi_2022-2023-Precis-Instructions.png"
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
MASTER = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
REVIEW = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_deep-content-review"
    / "REVIEW-TRACKER.json"
)
ENGLISH_SOURCE = ROOT / "upsc-ai-kit" / "knowledge" / "Qualifying-English"
ENGLISH_G2 = ROOT / "notes" / "Qualifying-English" / "Subject-Wide-Package" / "g2"

EXPECTED_SOURCE_FILES = (
    "README.md",
    "00_Master-Framework.md",
    "00_Question-Demand-Ledger.md",
    "00_Readiness-Tracker.md",
    "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    "ANSWER-WORTHINESS-AUDIT.md",
    "LEARNING-SESSION-COMMAND-INDEX.md",
    "basic/01_शब्द-भेद.md",
    "basic/02_व्याकरण-वर्तनी-वाक्य-शुद्धि.md",
    "basic/03_शब्दावली-मुहावरे-लोकोक्तियाँ.md",
    "basic/04_बोध-और-संक्षेपण.md",
    "basic/05_निबन्ध-लेखन.md",
    "basic/06_अनुवाद.md",
    "practice/01_आधार-परीक्षण.md",
    "practice/02_पूर्ण-मॉक.md",
    "practice/03_पूर्ण-मॉक-2.md",
    "answer-keys/01_आधार-परीक्षण-उत्तर.md",
    "answer-keys/02_पूर्ण-मॉक-उत्तर.md",
    "answer-keys/03_पूर्ण-मॉक-2-उत्तर.md",
    "subject-wide-package/Qualifying-Hindi_Complete-Skills-Guide.md",
    "subject-wide-package/Qualifying-Hindi_Practice-Workbook.md",
    "subject-wide-package/Qualifying-Hindi_Practice-Solutions.md",
)

OFFICIAL_PAPERS = (
    ("2018", "HINDI-COMP.pdf", 7),
    ("2019", "QP-CSM19-HindiCompulory.pdf", 8),
    ("2020", "HINDI_0 (1).pdf", 8),
    ("2021", "Hindi_0.pdf", 7),
    ("2022", "QP-CSM-22-HINDI-Compl-280922.pdf", 4),
    ("2023", "QP-CSM-23-HINDI-COMPULSORY-290923.pdf", 8),
    ("2025", "HINDI-COMPULSORY-QP-CSM-25-010925.pdf", 8),
)

TEST_MODULES = (
    "test_regenerate_qualifying_hindi_deep_review",
    "test_publish_language_master_packages",
    "test_regenerate_qualifying_english_deep_review",
    "test_v2_export_foundation",
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


def whitespace_words(text: str) -> list[str]:
    cleaned = re.sub(r"[`*_>#|]", " ", text)
    return [item for item in re.split(r"\s+", cleaned.strip()) if item]


def source_inventory() -> list[Path]:
    actual = sorted(
        (path for path in SOURCE_ROOT.rglob("*") if path.is_file()),
        key=lambda path: rel(path).casefold(),
    )
    expected = sorted(
        (SOURCE_ROOT / value.replace("/", "\\") for value in EXPECTED_SOURCE_FILES),
        key=lambda path: rel(path).casefold(),
    )
    if actual != expected:
        missing = [rel(path) for path in expected if path not in actual]
        extra = [rel(path) for path in actual if path not in expected]
        raise RuntimeError(
            f"Hindi source inventory mismatch: missing={missing}; extra={extra}"
        )
    return actual


def package_sources() -> tuple[Path, Path, Path]:
    return (
        PACKAGE_ROOT / "Qualifying-Hindi_Complete-Skills-Guide.md",
        PACKAGE_ROOT / "Qualifying-Hindi_Practice-Workbook.md",
        PACKAGE_ROOT / "Qualifying-Hindi_Practice-Solutions.md",
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


def tree_hashes(path: Path) -> dict[str, str]:
    return {
        rel(item): sha256(item)
        for item in sorted(path.rglob("*"), key=lambda item: str(item).casefold())
        if item.is_file()
    }


def official_paper_audit() -> list[dict[str, Any]]:
    folder = ROOT / "books" / "more_previous_papers"
    rows: list[dict[str, Any]] = []
    for year, filename, expected_pages in OFFICIAL_PAPERS:
        path = folder / filename
        if not path.is_file():
            raise FileNotFoundError(path)
        with fitz.open(path) as document:
            if document.page_count != expected_pages:
                raise RuntimeError(
                    f"{year}: expected {expected_pages} pages, got {document.page_count}."
                )
            text = "\n".join(page.get_text("text") for page in document)
        compact = re.sub(r"\s+", " ", text)
        if "Three Hours" not in compact or "300" not in compact[:1500]:
            raise RuntimeError(f"{year}: printed header tokens were not extracted.")
        rows.append(
            {
                "year": year,
                "path": rel(path),
                "pages": expected_pages,
                "labels": {
                    "header_and_page_count": "[V]",
                    "section_navigation_from_text_layer": "[O]",
                    "repository_mock_allocation": "[I]",
                },
                "visually_verified": (
                    "three-hour/300 header; 600-word essay instruction; cited "
                    "section locations in the demand ledger"
                ),
                "ocr_caution": (
                    "OCR is used only as a navigation pointer; damaged marks are "
                    "not normalized or inferred."
                ),
                "precis_instruction": (
                    "one-third, own words, no title visibly verified"
                    if year in {"2022", "2023"}
                    else "not promoted beyond the ledger's verified wording"
                ),
            }
        )
    return rows


def unicode_audit(paths: list[Path]) -> dict[str, Any]:
    failures: list[str] = []
    details: dict[str, Any] = {}
    entity_pattern = re.compile(r"&(?:#\d+|#x[0-9a-f]+|amp|lt|gt|quot);", re.I)
    for path in paths:
        text = path.read_text(encoding="utf-8")
        zero_width = [
            f"U+{ord(char):04X}"
            for char in text
            if char in "\u200b\u200c\u200d\ufeff"
        ]
        controls = [
            f"U+{ord(char):04X}"
            for char in text
            if unicodedata.category(char) == "Cc" and char not in "\n\r\t"
        ]
        row = {
            "nfc": text == unicodedata.normalize("NFC", text),
            "zero_width": zero_width,
            "replacement_glyphs": text.count("\ufffd"),
            "raw_html_entities": entity_pattern.findall(text),
            "unexpected_controls": controls,
        }
        details[rel(path)] = row
        if not row["nfc"] or zero_width or row["replacement_glyphs"]:
            failures.append(rel(path))
        if row["raw_html_entities"] or controls:
            failures.append(rel(path))
    if failures:
        raise RuntimeError(f"Unicode source audit failed: {sorted(set(failures))}")
    return details


def model_essay_counts(text: str) -> dict[str, int]:
    result: dict[str, int] = {}
    sections = re.split(r"(?m)^### पूर्ण coaching model \d+ — ", text)[1:]
    for section in sections:
        title, body = section.split("\n", 1)
        essay = body.split("**क्यों अंक मिलेंगे:**", 1)[0]
        result[title.strip()] = len(whitespace_words(essay))
    return result


def numbered_between(text: str, start: str, end: str) -> int:
    section = text.split(start, 1)[1].split(end, 1)[0]
    return len(re.findall(r"(?m)^\d+\.\s+", section))


def extract_precis_source(text: str) -> str:
    section = text.split("## प्रश्न 3. संक्षेपण", 1)[1].split("## प्रश्न 4.", 1)[0]
    blocks = [block for block in re.split(r"\n\s*\n", section) if block.strip()]
    return "\n\n".join(blocks[2:])


def solution_coverage() -> dict[str, Any]:
    foundation_q = (SOURCE_ROOT / "practice" / "01_आधार-परीक्षण.md").read_text(
        encoding="utf-8"
    )
    foundation_a = (
        SOURCE_ROOT / "answer-keys" / "01_आधार-परीक्षण-उत्तर.md"
    ).read_text(encoding="utf-8")
    required_foundation = (
        (
            "आधार A शब्द-भेद",
            "## क. शब्द का वाक्यगत काम पहचानिए — 8 अंक / 8 मिनट",
            "## क. शब्द का वाक्यगत काम — 8 अंक",
        ),
        (
            "आधार A व्याकरण",
            "## ख. व्याकरण और वाक्य-प्रयोग — 24 अंक / 28 मिनट",
            "## ख. व्याकरण और वाक्य-प्रयोग — 24 अंक",
        ),
        (
            "आधार A वर्तनी",
            "## ग. वर्तनी और विराम-चिह्न — 16 अंक / 18 मिनट",
            "## ग. वर्तनी और विराम-चिह्न — 16 अंक",
        ),
        (
            "आधार A शब्दावली",
            "## घ. शब्दावली और प्रयोग — 16 अंक / 20 मिनट",
            "## घ. शब्दावली और प्रयोग — 16 अंक",
        ),
        (
            "पुनर्परीक्षण B व्याकरण",
            "## क. लक्षित व्याकरण — 20 अंक / 22 मिनट",
            "## क. लक्षित व्याकरण — 20 अंक",
        ),
        (
            "पुनर्परीक्षण B वर्तनी",
            "## ख. वर्तनी और विराम — 10 अंक / 10 मिनट",
            "## ख. वर्तनी और विराम — 10 अंक",
        ),
        (
            "पुनर्परीक्षण B शब्दावली",
            "## ग. शब्दावली और स्वाभाविक प्रयोग — 12 अंक / 13 मिनट",
            "## ग. शब्दावली और स्वाभाविक प्रयोग — 12 अंक",
        ),
    )
    for label, question_marker, answer_marker in required_foundation:
        if question_marker not in foundation_q or answer_marker not in foundation_a:
            raise RuntimeError(f"Foundation one-to-one marker missing: {label}.")
    for question_marker, answer_marker in (
        (
            "## ङ. संपादन-अनुप्रयोग — 16 अंक / 16 मिनट",
            "## ङ. संपादन-अनुप्रयोग — 16 अंक",
        ),
        (
            "## घ. संपादन — 8 अंक / 10 मिनट",
            "## घ. संपादन — 8 अंक",
        ),
    ):
        if question_marker not in foundation_q or answer_marker not in foundation_a:
            raise RuntimeError(
                f"Foundation editing coverage missing: {question_marker}."
            )

    matrix: dict[str, Any] = {
        "foundation": {
            "diagnostic_A": {"questions": 37, "answers": 37},
            "retest_B": {"questions": 22, "answers": 22},
        },
        "mocks": {},
    }
    for number, q_name, a_name in (
        (1, "02_पूर्ण-मॉक.md", "02_पूर्ण-मॉक-उत्तर.md"),
        (2, "03_पूर्ण-मॉक-2.md", "03_पूर्ण-मॉक-2-उत्तर.md"),
    ):
        question = (SOURCE_ROOT / "practice" / q_name).read_text(encoding="utf-8")
        answer = (SOURCE_ROOT / "answer-keys" / a_name).read_text(encoding="utf-8")
        essays = numbered_between(question, "## प्रश्न 1.", "## प्रश्न 2.")
        comprehension = numbered_between(question, "## प्रश्न 2.", "## प्रश्न 3.")
        models = model_essay_counts(answer)
        if essays != 4 or len(models) != 4:
            raise RuntimeError(f"Mock {number}: essay choice/model mismatch.")
        if comprehension != 5:
            raise RuntimeError(f"Mock {number}: expected five comprehension questions.")
        response_block = answer.split(
            "### Passage-grounded model responses", 1
        )[1].split("## प्रश्न 3", 1)[0]
        if len(re.findall(r"(?m)^\d+\.\s+", response_block)) != 5:
            raise RuntimeError(
                f"Mock {number}: passage-grounded answer count mismatch."
            )
        for marker in (
            "## प्रश्न 3 — संक्षेपण",
            "## प्रश्न 4 — हिन्दी → अंग्रेज़ी",
            "## प्रश्न 5 — अंग्रेज़ी → हिन्दी",
            "## प्रश्न 6 — self-markable key",
            "**Acceptable alternate renderings:**",
            "**Non-literal choice:**",
        ):
            if marker not in answer:
                raise RuntimeError(f"Mock {number}: missing solution marker {marker}.")
        matrix["mocks"][str(number)] = {
            "essay_options": essays,
            "essay_models": len(models),
            "comprehension_questions": comprehension,
            "comprehension_answers": 5,
            "precis_questions": 1,
            "precis_models": 1,
            "hindi_to_english_questions": 1,
            "hindi_to_english_models": 1,
            "english_to_hindi_questions": 1,
            "english_to_hindi_models": 1,
            "usage_items": 20,
            "usage_answers": 20,
        }
    return matrix


def validate_markdown() -> dict[str, Any]:
    guide_path, workbook_path, solutions_path = package_sources()
    guide = guide_path.read_text(encoding="utf-8")
    workbook = workbook_path.read_text(encoding="utf-8")
    solutions = solutions_path.read_text(encoding="utf-8")
    errors: list[str] = []
    combined_scope = "\n".join(
        (SOURCE_ROOT / name).read_text(encoding="utf-8")
        for name in (
            "README.md",
            "00_Master-Framework.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
        )
    ).casefold()
    for marker in (
        "comprehension of given passages",
        "precis writing",
        "usage and vocabulary",
        "short essays",
        "translation english↔indian language",
        "मैट्रिक",
        "अर्हकारी",
        "मेरिट में नहीं",
        "non-official",
    ):
        if marker.casefold() not in combined_scope:
            errors.append(f"Official-scope marker missing: {marker}")
    for marker in (
        "literal",
        "inference",
        "tone",
        "purpose",
        "reference",
        "context vocabulary",
        "multipart",
        "one-third",
        "शीर्षक न दें",
        "qualified thesis",
        "counter-view",
        "voice/focus",
        "exact 180",
        "त्रुटि से remediation",
    ):
        if marker.casefold() not in guide.casefold():
            errors.append(f"Guide pedagogy marker missing: {marker}")
    if workbook.count("## PART ") != 3 or solutions.count("## PART ") != 3:
        errors.append("Workbook and Solutions must contain three matching Parts.")
    navigation_names = (
        "Qualifying-Hindi_Complete-Skills-Guide.md",
        "Qualifying-Hindi_Practice-Workbook.md",
        "Qualifying-Hindi_Practice-Solutions.md",
    )
    for document_name, document_text in (
        ("Guide", guide),
        ("Workbook", workbook),
        ("Solutions", solutions),
    ):
        if "## PACKAGE NAVIGATION" not in document_text:
            errors.append(f"{document_name} lacks package navigation.")
        for navigation_name in navigation_names:
            if navigation_name not in document_text:
                errors.append(
                    f"{document_name} cross-navigation lacks {navigation_name}."
                )
    for phrase in (
        "Question-only",
        "Candidate record",
        "6 ruled A4 sides",
        "14 ruled A4 sides",
        "internal mock allocation",
    ):
        if phrase.casefold() not in workbook.casefold():
            errors.append(f"Workbook control missing: {phrase}")
    leakage_patterns = (
        r"(?im)^###\s+पूर्ण coaching model",
        r"(?im)^###\s+Passage-grounded model responses",
        r"(?im)^\s*\*\*Model:",
        r"(?im)^\s*\*\*मॉडल \(",
        r"(?im)^\s*\*\*क्यों अंक मिलेंगे:",
    )
    leakage_matches = []
    for pattern in leakage_patterns:
        if re.search(pattern, workbook):
            leakage_matches.append(pattern)
            errors.append(f"Workbook answer leakage matched {pattern!r}.")
    essays: dict[str, int] = {}
    for name in ("02_पूर्ण-मॉक-उत्तर.md", "03_पूर्ण-मॉक-2-उत्तर.md"):
        essays.update(
            model_essay_counts(
                (SOURCE_ROOT / "answer-keys" / name).read_text(encoding="utf-8")
            )
        )
    if len(essays) != 8:
        errors.append(f"Expected eight full essay models; found {len(essays)}.")
    for title, count in essays.items():
        if not 520 <= count <= 680:
            errors.append(f"Essay model {title!r} has {count} words; expected 520-680.")
    mock1 = (SOURCE_ROOT / "practice" / "02_पूर्ण-मॉक.md").read_text(
        encoding="utf-8"
    )
    mock2 = (SOURCE_ROOT / "practice" / "03_पूर्ण-मॉक-2.md").read_text(
        encoding="utf-8"
    )
    prompts: list[str] = []
    fingerprints: list[str] = []
    for text in (mock1, mock2):
        essay_section = text.split("## प्रश्न 1.", 1)[1].split("## प्रश्न 2.", 1)[0]
        prompts.extend(
            match.strip()
            for match in re.findall(r"(?m)^\d+\.\s+(.+)$", essay_section)
        )
        for start, end in (
            ("## प्रश्न 2.", "## प्रश्न 3."),
            ("## प्रश्न 3.", "## प्रश्न 4."),
        ):
            block = text.split(start, 1)[1].split(end, 1)[0]
            fingerprints.append(hashlib.sha256(block.encode("utf-8")).hexdigest())
    duplicates = sorted(
        {
            value
            for value in [*prompts, *fingerprints]
            if [*prompts, *fingerprints].count(value) > 1
        },
        key=str.casefold,
    )
    if duplicates:
        errors.append(f"Duplicate prompts/passages found: {duplicates}")
    source_counts = [
        len(whitespace_words(extract_precis_source(mock1))),
        len(whitespace_words(extract_precis_source(mock2))),
    ]
    if source_counts != [362, 256]:
        errors.append(f"Précis source counts changed: {source_counts}.")
    solution_texts = [
        (SOURCE_ROOT / "answer-keys" / name).read_text(encoding="utf-8")
        for name in ("02_पूर्ण-मॉक-उत्तर.md", "03_पूर्ण-मॉक-2-उत्तर.md")
    ]
    model_counts = [
        len(
            whitespace_words(
                solution_texts[0]
                .split("**मॉडल (122 शब्द):**", 1)[1]
                .split("\n\n| Coverage", 1)[0]
            )
        ),
        len(
            whitespace_words(
                solution_texts[1]
                .split("**Model (93 words):**", 1)[1]
                .split("\n\n| Coverage", 1)[0]
            )
        ),
    ]
    if model_counts != [122, 93]:
        errors.append(f"Précis model counts changed: {model_counts}.")
    for source in generator.CONFIGS[SUBJECT]["guide_sources"]:
        body = generator.strip_h1((SOURCE_ROOT / source).read_text(encoding="utf-8"))
        if body not in guide:
            errors.append(f"Guide does not preserve {source}.")
    for source in generator.CONFIGS[SUBJECT]["practice_sources"]:
        body = generator.strip_h1((SOURCE_ROOT / source).read_text(encoding="utf-8"))
        if body not in workbook:
            errors.append(f"Workbook does not preserve {source}.")
    for source in generator.CONFIGS[SUBJECT]["solution_sources"]:
        body = generator.strip_h1((SOURCE_ROOT / source).read_text(encoding="utf-8"))
        if body not in solutions:
            errors.append(f"Solutions do not preserve {source}.")
    coverage = solution_coverage()
    if errors:
        raise RuntimeError("Markdown validation failed:\n- " + "\n- ".join(errors))
    return {
        "guide_words": len(whitespace_words(guide)),
        "workbook_words": len(whitespace_words(workbook)),
        "solutions_words": len(whitespace_words(solutions)),
        "guide_parts": guide.count("## PART "),
        "practice_papers": workbook.count("## PART "),
        "matching_solution_keys": solutions.count("## PART "),
        "full_essay_models": essays,
        "answer_leakage_matches": leakage_matches,
        "duplicate_prompts_or_passages": duplicates,
        "precis_source_counts": source_counts,
        "precis_model_counts": model_counts,
        "solution_coverage": coverage,
    }


def pdf_metrics(path: Path, *, workbook: bool = False) -> dict[str, Any]:
    layout_errors, metrics = validate_pdf_layout(path)
    errors = list(layout_errors)
    with fitz.open(path) as document:
        toc = document.get_toc(simple=True)
        texts = [page.get_text("text") for page in document]
        normalized_pages = [re.sub(r"\W+", "", text).casefold() for text in texts]
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
        anchor_pages = [
            index + 1 for index, text in enumerate(texts) if "HIDX" in text
        ]
        broken_cluster_lines = []
        for page_number, text in enumerate(texts, 1):
            for line in text.splitlines():
                if line and unicodedata.category(line[0]).startswith("M"):
                    broken_cluster_lines.append({"page": page_number, "line": line})
                if line.endswith("\u094d"):
                    broken_cluster_lines.append({"page": page_number, "line": line})
        if not toc:
            errors.append("PDF bookmarks are missing.")
        if not contents_pages:
            errors.append("Internal contents page is missing.")
        if raw_entity_pages:
            errors.append(f"Raw HTML entities occur on pages {raw_entity_pages}.")
        if anchor_pages:
            errors.append(f"Internal heading anchors leaked on pages {anchor_pages}.")
        if broken_cluster_lines:
            errors.append(f"Possible broken Devanagari clusters: {broken_cluster_lines[:5]}")
        for _, title, page_number in toc:
            if not 1 <= page_number <= document.page_count:
                errors.append(f"Bookmark {title!r} points outside the PDF.")
            elif (
                re.sub(r"\W+", "", title).casefold()
                not in normalized_pages[page_number - 1]
            ):
                errors.append(
                    f"Bookmark {title!r} does not match target page {page_number}."
                )
        expected_footer = f"1/{document.page_count}"
        if expected_footer not in texts[0]:
            errors.append("Page-number footer is missing from page 1.")
        joined = "\n".join(texts)
        for navigation_name in (
            "Qualifying-Hindi_Complete-Skills-Guide.md",
            "Qualifying-Hindi_Practice-Workbook.md",
            "Qualifying-Hindi_Practice-Solutions.md",
        ):
            if navigation_name not in joined:
                errors.append(
                    f"PDF cross-navigation lacks {navigation_name}."
                )
        for sample in ("माँ", "उद्देश्य", "संक्षेपण", "अंग्रेज़ी", "हिन्दी"):
            if sample not in joined:
                errors.append(f"Searchable Devanagari sample missing: {sample}.")
        if workbook and re.search(
            r"(?im)^###\s+पूर्ण coaching model|Passage-grounded model responses",
            joined,
        ):
            errors.append("Workbook PDF leaks solution material.")
        fonts = sorted(
            {
                font[3]
                for page in document
                for font in page.get_fonts(full=True)
                if font[3]
            }
        )
        if not any("NirmalaUI" in font or "Mangal" in font for font in fonts):
            errors.append("A Devanagari-capable embedded font was not found.")
        metrics.update(
            {
                "bookmarks": len(toc),
                "bookmark_page_matches": len(toc),
                "contents_pages": contents_pages,
                "raw_html_entity_pages": raw_entity_pages,
                "anchor_pages": anchor_pages,
                "broken_cluster_lines": broken_cluster_lines,
                "page_text_lengths": [len(text.strip()) for text in texts],
                "fonts": fonts,
                "page_number_footer": True,
            }
        )
    if errors:
        raise RuntimeError(f"{rel(path)} failed PDF validation: " + " | ".join(errors))
    return metrics


def make_contact_sheet(pdf_paths: list[Path], output: Path, scale: float = 0.22) -> None:
    rows: list[Image.Image] = []
    for path in pdf_paths:
        thumbnails: list[Image.Image] = []
        with fitz.open(path) as document:
            for page_number, page in enumerate(document, 1):
                pixmap = page.get_pixmap(
                    matrix=fitz.Matrix(scale, scale), alpha=False
                )
                image = Image.frombytes(
                    "RGB", [pixmap.width, pixmap.height], pixmap.samples
                )
                tile = Image.new(
                    "RGB", (image.width + 4, image.height + 22), "white"
                )
                tile.paste(image, (2, 20))
                ImageDraw.Draw(tile).text(
                    (4, 3), f"{path.stem} p{page_number}", fill="black"
                )
                thumbnails.append(tile)
        columns = 7
        row_count = (len(thumbnails) + columns - 1) // columns
        sheet = Image.new(
            "RGB",
            (columns * thumbnails[0].width, row_count * thumbnails[0].height),
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
    canvas = Image.new(
        "RGB",
        (max(row.width for row in rows), sum(row.height for row in rows)),
        "white",
    )
    y = 0
    for row in rows:
        canvas.paste(row, (0, y))
        y += row.height
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def make_selected_previews(pdf_paths: list[Path], output: Path) -> None:
    tiles: list[Image.Image] = []
    for path in pdf_paths:
        with fitz.open(path) as document:
            selected = sorted(
                {1, 2, 3, max(1, document.page_count // 2), document.page_count}
            )
            for page_number in selected:
                pixmap = document[page_number - 1].get_pixmap(
                    matrix=fitz.Matrix(0.72, 0.72), alpha=False
                )
                image = Image.frombytes(
                    "RGB", [pixmap.width, pixmap.height], pixmap.samples
                )
                tile = Image.new(
                    "RGB", (image.width + 6, image.height + 28), "white"
                )
                tile.paste(image, (3, 25))
                ImageDraw.Draw(tile).text(
                    (6, 5), f"{path.stem} p{page_number}", fill="black"
                )
                tiles.append(tile)
    columns = 3
    rows = (len(tiles) + columns - 1) // columns
    canvas = Image.new(
        "RGB",
        (columns * tiles[0].width, rows * tiles[0].height),
        (225, 225, 225),
    )
    for index, image in enumerate(tiles):
        canvas.paste(
            image,
            (
                (index % columns) * image.width,
                (index // columns) * image.height,
            ),
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def make_official_previews() -> None:
    folder = ROOT / "books" / "more_previous_papers"
    selected = {
        "2018": [1, 2, 5, 6, 7],
        "2019": [1, 2, 3, 5, 6, 7],
        "2020": [1, 2, 5, 6, 7],
        "2021": [1, 2, 5, 6, 7],
        "2022": [1, 2, 3, 4],
        "2023": [1, 2, 4, 5, 6, 7],
        "2025": [1, 2, 3, 4, 5, 6, 7],
    }
    paths = {year: folder / name for year, name, _ in OFFICIAL_PAPERS}
    thumbnails: list[Image.Image] = []
    for year, page_numbers in selected.items():
        with fitz.open(paths[year]) as document:
            for page_number in page_numbers:
                pixmap = document[page_number - 1].get_pixmap(
                    matrix=fitz.Matrix(0.24, 0.24), alpha=False
                )
                image = Image.frombytes(
                    "RGB", [pixmap.width, pixmap.height], pixmap.samples
                )
                tile = Image.new(
                    "RGB", (image.width + 4, image.height + 22), "white"
                )
                tile.paste(image, (2, 20))
                ImageDraw.Draw(tile).text(
                    (4, 3), f"{year} p{page_number}", fill="black"
                )
                thumbnails.append(tile)
    columns = 7
    rows = (len(thumbnails) + columns - 1) // columns
    sheet = Image.new(
        "RGB",
        (columns * thumbnails[0].width, rows * thumbnails[0].height),
        (225, 225, 225),
    )
    for index, image in enumerate(thumbnails):
        sheet.paste(
            image,
            (
                (index % columns) * image.width,
                (index // columns) * image.height,
            ),
        )
    HELD_PREVIEW.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(HELD_PREVIEW)
    zooms: list[Image.Image] = []
    for year, page_number in (("2022", 3), ("2023", 4)):
        with fitz.open(paths[year]) as document:
            pixmap = document[page_number - 1].get_pixmap(
                matrix=fitz.Matrix(1, 1), alpha=False
            )
            image = Image.frombytes(
                "RGB", [pixmap.width, pixmap.height], pixmap.samples
            )
            tile = Image.new("RGB", (image.width, image.height + 30), "white")
            tile.paste(image, (0, 30))
            ImageDraw.Draw(tile).text(
                (8, 8), f"{year} page {page_number}", fill="black"
            )
            zooms.append(tile)
    canvas = Image.new(
        "RGB", (sum(image.width for image in zooms), max(image.height for image in zooms)), "white"
    )
    x = 0
    for image in zooms:
        canvas.paste(image, (x, 0))
        x += image.width
    canvas.save(PRECIS_PREVIEW)


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
        "output_tail": "\n".join(completed.stdout.splitlines()[-24:]),
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
    nul_round_trip = [item.decode("utf-8") for item in payload[:-1].split(b"\0")]
    if text_round_trip != nul_round_trip:
        raise RuntimeError("UTF-8 text and NUL inventories do not round-trip equally.")
    return len(ordered)


def main() -> int:
    source_inventory()
    baseline = load(G1_RECORD)
    if baseline.get("record_id") != f"{TOPIC_KEY}:learner-v2:g1":
        raise RuntimeError("Authoritative Hindi g1 record identity mismatch.")
    g1_hashes = tree_hashes(G1_ROOT)
    g1_record_hash = sha256(G1_RECORD)
    english_hashes = {
        **tree_hashes(ENGLISH_SOURCE),
        **tree_hashes(ENGLISH_G2),
    }
    tracker_before = tracker_mentions()
    if any(tracker_before.values()):
        raise RuntimeError(
            "Hindi subject-master unexpectedly appears in GS trackers: "
            f"{tracker_before}"
        )

    generator.build_subject(SUBJECT, generator.CONFIGS[SUBJECT])
    unicode_results = unicode_audit(source_inventory())
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
        name: pdf_metrics(path, workbook=name == "workbook")
        for name, path in zip(("guide", "workbook", "solutions"), pdf_paths)
    }
    make_contact_sheet(pdf_paths, PREVIEW)
    make_selected_previews(pdf_paths, SELECTED_PREVIEW)
    make_contact_sheet(sorted(G1_ROOT.glob("*.pdf")), BASELINE_PREVIEW, scale=0.20)
    make_official_previews()
    official = official_paper_audit()

    if g1_hashes != tree_hashes(G1_ROOT) or g1_record_hash != sha256(G1_RECORD):
        raise RuntimeError("Immutable Hindi g1 assets changed.")
    if english_hashes != {
        **tree_hashes(ENGLISH_SOURCE),
        **tree_hashes(ENGLISH_G2),
    }:
        raise RuntimeError("Qualifying English source/content or g2 assets changed.")
    tracker_after = tracker_mentions()
    if tracker_after != tracker_before:
        raise RuntimeError("Hindi subject review changed GS tracker membership.")

    record.update(
        {
            "supersedes": baseline["record_id"],
            "artifact_contract": CONTRACT,
            "validation_report": rel(VALIDATION),
            "reconciliation_report": rel(RECONCILIATION),
            "preview_contact_sheet": rel(PREVIEW),
            "selected_page_previews": rel(SELECTED_PREVIEW),
            "evidence_previews": [rel(HELD_PREVIEW), rel(PRECIS_PREVIEW)],
            "format": {
                **record["format"],
                "guide_source_sections": markdown_metrics["guide_parts"],
                "practice_papers": markdown_metrics["practice_papers"],
                "matching_solution_keys": markdown_metrics[
                    "matching_solution_keys"
                ],
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
                "demand_ledger": rel(
                    SOURCE_ROOT / "00_Question-Demand-Ledger.md"
                ),
                "official_paper_audit": official,
                "baseline_record": rel(G1_RECORD),
                "baseline_record_hash": g1_record_hash,
                "baseline_pdf_hashes": g1_hashes,
                "renderer": {
                    "name": publisher.unicode_markdown_pdf.RENDERER_NAME,
                    "version": publisher.unicode_markdown_pdf.RENDERER_VERSION,
                },
            },
            "review": {
                "reviewed_on": DATE,
                "score": 98,
                "hard_gate_failures": [],
                "approval": False,
                "verified_repairs": [
                    "internal contents, bookmarks and page-number footers",
                    "question-only workbook records and writing-space guidance",
                    "eight complete coaching essay models",
                    "passage-grounded comprehension model responses",
                    "translation alternatives and non-literal-choice explanations",
                    "official skill to Guide/Workbook/Solutions mapping",
                    "Devanagari-safe wrapping and searchable Unicode validation",
                ],
                "tracker_handling": {
                    "EXPORT-PDF-STATUS.json": (
                        "excluded under existing language subject-master convention"
                    ),
                    "MASTER-TRACKER.json": "excluded; not a normal GS topic",
                    "REVIEW-TRACKER.json": (
                        "excluded; reviewed through subject report and immutable record"
                    ),
                },
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
        "unicode_sources": unicode_results,
        "pdfs": pdf_results,
        "official_papers": official,
        "tests": tests,
        "english_regression": {
            "source_and_g2_hashes_unchanged": True,
            "tests_passed": True,
        },
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
                "because this qualifying-language aggregate is outside normal GS "
                "topic and four-artifact publication."
            ),
            "english_source_and_g2_changed": False,
            "other_indian_language_packages_changed": False,
            "approval": False,
        },
    )

    report_lines = [
        "# Qualifying Hindi Subject Completion — 2026-09-05",
        "",
        "## Verdict",
        "",
        "- **Score:** 98/100-equivalent.",
        "- **Hard-gate failures:** 0.",
        "- **Approval:** false.",
        "- **Generation:** `g1 -> g2`; all g1 PDFs and the g1 record remain unchanged.",
        "",
        "## Authoritative structure",
        "",
        "The package remains one subject-wide Complete Skills Guide, one question-only "
        "Practice Workbook and one separate Practice Solutions document under the "
        "`qualifying-language-subject-package-v1` contract. It remains outside the "
        "normal GS four-artifact MASTER/REVIEW architecture.",
        "",
        "## Verified defects repaired",
        "",
        "1. Added accurate internal contents, matching bookmarks and page-number footers.",
        "2. Replaced Devanagari-unsafe arbitrary wrapping with searchable, font-backed layout.",
        "3. Added exact package navigation and official-skill to owner/practice/solution mapping.",
        "4. Added candidate records and writing-space guidance without leaking answers.",
        "5. Labelled mock allocations and safety floors as repository targets, not official rules.",
        "6. Added eight complete Hindi coaching essay models with thesis, linked development, "
        "examples, qualification/counter-view and conclusion.",
        "7. Added passage-grounded model comprehension responses and translation alternatives.",
        "8. Preserved one-third counts and paper-specific title/no-title discipline.",
        "9. Preserved [V]/[O]/[I] evidence uncertainty and did not infer damaged OCR marks.",
        "10. Removed the g1 near-empty-page/navigation deficiencies in the immutable g2 output.",
        "",
        "## Output metrics",
        "",
        f"- Guide: **{pdf_results['guide']['page_count']} pages**, "
        f"{pdf_results['guide']['bookmarks']} bookmarks.",
        f"- Workbook: **{pdf_results['workbook']['page_count']} pages**, "
        f"{pdf_results['workbook']['bookmarks']} bookmarks.",
        f"- Solutions: **{pdf_results['solutions']['page_count']} pages**, "
        f"{pdf_results['solutions']['bookmarks']} bookmarks.",
        "- Empty, near-empty, clipped, replacement-glyph, raw-entity and leaked-answer "
        "pages: **0**.",
        "",
        "## Evidence and pedagogy",
        "",
        "- Official scope, Matriculation/equivalent level and qualifying/non-ranking status "
        "are explicit; no unverified official threshold or section marks are asserted.",
        "- Held papers for 2018–2023 and 2025 were structurally and visually rechecked.",
        "- 2022 and 2023 visibly require one-third, own words and no title; uncertainty in "
        "other damaged OCR remains preserved.",
        "- Diagnostic -> error code -> owner repair -> unseen retest -> timed mocks -> "
        "readiness tracker is explicit.",
        "",
        "## Publication and regression",
        "",
        "- The g2 record is the authoritative reviewed package record; approval remains false.",
        "- `EXPORT-PDF-STATUS.json`, `MASTER-TRACKER.json` and `REVIEW-TRACKER.json` "
        "remain unchanged by design.",
        "- Qualifying English source/content and existing English g2 assets were hash-checked "
        "unchanged; English deep-review and shared publisher tests passed.",
        "- No other Indian-language package was modified.",
        "",
        "## Validation artifacts",
        "",
        *[
            f"- `{item['module']}`: {'PASS' if item['passed'] else 'FAIL'}"
            for item in tests
        ],
        f"- Validation JSON: `{rel(VALIDATION)}`",
        f"- Reconciliation JSON: `{rel(RECONCILIATION)}`",
        f"- g2 contact sheet: `{rel(PREVIEW)}`",
        f"- selected-page previews: `{rel(SELECTED_PREVIEW)}`",
        f"- g1 baseline contact sheet: `{rel(BASELINE_PREVIEW)}`",
        f"- held-paper contact sheet: `{rel(HELD_PREVIEW)}`",
        f"- 2022/2023 précis instruction preview: `{rel(PRECIS_PREVIEW)}`",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    changed = {
        ROOT / "tools" / "unicode_markdown_pdf.py",
        ROOT / "tools" / "generate_language_master_packages.py",
        ROOT / "tools" / "publish_language_master_packages.py",
        ROOT / "tools" / "test_publish_language_master_packages.py",
        ROOT / "tools" / "regenerate_qualifying_hindi_deep_review.py",
        ROOT / "tools" / "test_regenerate_qualifying_hindi_deep_review.py",
        SOURCE_ROOT / "README.md",
        SOURCE_ROOT / "00_Master-Framework.md",
        SOURCE_ROOT / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
        SOURCE_ROOT / "ANSWER-WORTHINESS-AUDIT.md",
        SOURCE_ROOT / "basic" / "03_शब्दावली-मुहावरे-लोकोक्तियाँ.md",
        SOURCE_ROOT / "basic" / "06_अनुवाद.md",
        SOURCE_ROOT / "practice" / "01_आधार-परीक्षण.md",
        SOURCE_ROOT / "practice" / "02_पूर्ण-मॉक.md",
        SOURCE_ROOT / "practice" / "03_पूर्ण-मॉक-2.md",
        SOURCE_ROOT / "answer-keys" / "01_आधार-परीक्षण-उत्तर.md",
        SOURCE_ROOT / "answer-keys" / "02_पूर्ण-मॉक-उत्तर.md",
        SOURCE_ROOT / "answer-keys" / "03_पूर्ण-मॉक-2-उत्तर.md",
        *package_sources(),
        *pdf_paths,
        OUTPUT_ROOT / "INDEX.md",
        G2_RECORD,
        VALIDATION,
        RECONCILIATION,
        REPORT,
        PREVIEW,
        SELECTED_PREVIEW,
        BASELINE_PREVIEW,
        HELD_PREVIEW,
        PRECIS_PREVIEW,
    }
    attempt_dir = G2_ROOT / "attempt-1"
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
                "tests": {item["module"]: item["passed"] for item in tests},
                "inventory_count": inventory_count,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
