"""Targeted tests for the reusable Easy Learning renderer and finished editions."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
import unittest
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import easy_learning_pdf as renderer


TOPIC_DIR = ROOT / "notes/Easy-Learning/Polity/06-Citizenship"
MARKDOWN = (
    ROOT
    / "upsc-ai-kit/knowledge/Easy-Learning/Polity/06-Citizenship/"
    "Citizenship-Guided-Learning-Edition.md"
)
PDF = TOPIC_DIR / "Citizenship-Guided-Learning-Edition.pdf"
COVERAGE = TOPIC_DIR / "COVERAGE-REPORT.md"
README = TOPIC_DIR / "README.txt"
SOURCE_MD = (
    ROOT
    / "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Polity/"
    "Subject-Wide-Syllabus/learning-sessions/polity-06/g14/"
    "polity-06_Complete-Learning-Session_2026-08-23.md"
)
WORKBOOK_MD = SOURCE_MD.with_name(
    "polity-06_Solved-Practice-Workbook_2026-08-23.md"
)

FR_TOPIC_DIR = ROOT / "notes/Easy-Learning/Polity/07-Fundamental-Rights"
FR_MARKDOWN = (
    ROOT
    / "upsc-ai-kit/knowledge/Easy-Learning/Polity/07-Fundamental-Rights/"
    "Fundamental-Rights-Guided-Learning-Edition.md"
)
FR_PDF = FR_TOPIC_DIR / "Fundamental-Rights-Guided-Learning-Edition.pdf"
FR_COVERAGE = FR_TOPIC_DIR / "COVERAGE-REPORT.md"
FR_README = FR_TOPIC_DIR / "README.txt"
FR_SOURCE_MD = (
    ROOT
    / "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Polity/"
    "Subject-Wide-Syllabus/learning-sessions/polity-07/g15/"
    "polity-07_Complete-Learning-Session_2026-08-23.md"
)
FR_WORKBOOK_MD = FR_SOURCE_MD.with_name(
    "polity-07_Solved-Practice-Workbook_2026-08-23.md"
)
START_HERE = ROOT / "notes/Easy-Learning/START-HERE.md"
TRACKER = ROOT / "notes/Easy-Learning/TRACKER.md"
FR_PREVIEW_DIR = (
    ROOT
    / "upsc-ai-kit/manifests/exports/"
    "easy-learning-fundamental-rights-2026-08-24-preview"
)

EXPECTED_PROTECTED_HASHES = {
    "EXPORT-PDF-STATUS.json":
        "66402036b017f32f0fb234a56e984cd6db70e34d707eabf616ddacf79e20da3c",
    "tools/markdown_learning_pdf.py":
        "c6717f3d7b651210698a10a758aa04b9b17cb32be3e144479eec6804408b7051",
    "tools/export_four_item_library.py":
        "40fa000d78d50acddd065ba3d3afb41e283a7a4bc3c0e972dcad89d2d52ca444",
    "tools/test_export_four_item_library.py":
        "67e0e7d50534a1da4ead3666ad6353a6340e97ff81a8551ebf11d367aad1c21e",
    "upsc-ai-kit/manifests/exports/final-four-item-library-2026-08-23.json":
        "53c32fb79b84e4b23baaa0bdd7830d08f4b6f08b7d21710c02337e46d8a660c0",
    "upsc-ai-kit/manifests/exports/final-four-item-library-2026-08-24-validation.json":
        "45e632c8cb558bbea1bfc38486ed33397d20843d7e60e617bec3183d744553ec",
    "tools/finalize_v2_topic.py":
        "0d5de3ff92de49d9b3a7e4034dcbdaa398834ca05932d8a7f67f60501da3c039",
    "tools/generate_v2_section_indexes.py":
        "ef2db25a49896c90d4b86fea4edd0328a7af0c2dc4ce0f34c29fbfd1eb0c4b3b",
    "tools/refresh_all_v2_learning_sessions.py":
        "c57bba9f63f09a173fa1c6e4e5f6faaf549efe5d8b8d5fc082fa66ba4f66a1c8",
    (
        "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Polity/"
        "Subject-Wide-Syllabus/learning-sessions/polity-06/g14/"
        "polity-06_Complete-Learning-Session_2026-08-23.md"
    ):
        "527ab9bb9be70863f2f872535d6cc779f45067fb95a46807427578d0f5231ee7",
    (
        "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Polity/"
        "Subject-Wide-Syllabus/learning-sessions/polity-06/g14/"
        "polity-06_Solved-Practice-Workbook_2026-08-23.md"
    ):
        "7627a4b45468012035ca415e67256115a5dbbc9cd0de14165ab80812f4ddee37",
    "upsc-ai-kit/knowledge/Polity/basic/Citizenship.md":
        "5a63ab5056f7e111634cd5ddfafcc614100797a1dee93c257b3e762a5ec01656",
    "upsc-ai-kit/knowledge/Polity/advanced/06_Citizenship.md":
        "c54426b83470c669a1fa4642d7db71d1bd191fc878eccd475a673ad4fd687dbc",
    "upsc-ai-kit/knowledge/Polity/06_Citizenship_Complete-Topic-Package.md":
        "b1ffeb37cc7a02741f4adf19003256ec0628479a6d6aced950232ca339812a07",
    (
        "notes/Learner-v2-Refreshed/Polity/Subject-Wide-Syllabus/"
        "learning-sessions/polity-06/g14/"
        "polity-06_Complete-Learning-Session_2026-08-23.pdf"
    ):
        "09a3fca51ea177f9119e7d0a596ad7cb51adca0388094b5716bc5a0c8cde7dd7",
    (
        "notes/Learner-v2-Refreshed/Polity/Subject-Wide-Syllabus/"
        "learning-sessions/polity-06/g14/"
        "polity-06_Solved-Practice-Workbook_2026-08-23.pdf"
    ):
        "c17ca803528ee6826c537676fc493a962e0c430bb8d941f7aaf95fad519b820d",
}

EXPECTED_FR_PROTECTED_HASHES = {
    "EXPORT-PDF-STATUS.json":
        "66402036b017f32f0fb234a56e984cd6db70e34d707eabf616ddacf79e20da3c",
    "tools/markdown_learning_pdf.py":
        "c6717f3d7b651210698a10a758aa04b9b17cb32be3e144479eec6804408b7051",
    "tools/export_four_item_library.py":
        "40fa000d78d50acddd065ba3d3afb41e283a7a4bc3c0e972dcad89d2d52ca444",
    "tools/test_export_four_item_library.py":
        "67e0e7d50534a1da4ead3666ad6353a6340e97ff81a8551ebf11d367aad1c21e",
    "upsc-ai-kit/manifests/exports/final-four-item-library-2026-08-23.json":
        "53c32fb79b84e4b23baaa0bdd7830d08f4b6f08b7d21710c02337e46d8a660c0",
    "upsc-ai-kit/manifests/exports/final-four-item-library-2026-08-24-validation.json":
        "45e632c8cb558bbea1bfc38486ed33397d20843d7e60e617bec3183d744553ec",
    "tools/finalize_v2_topic.py":
        "0d5de3ff92de49d9b3a7e4034dcbdaa398834ca05932d8a7f67f60501da3c039",
    "tools/generate_v2_section_indexes.py":
        "ef2db25a49896c90d4b86fea4edd0328a7af0c2dc4ce0f34c29fbfd1eb0c4b3b",
    "tools/refresh_all_v2_learning_sessions.py":
        "c57bba9f63f09a173fa1c6e4e5f6faaf549efe5d8b8d5fc082fa66ba4f66a1c8",
    (
        "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Polity/"
        "Subject-Wide-Syllabus/learning-sessions/polity-07/g15/"
        "polity-07_Complete-Learning-Session_2026-08-23.md"
    ):
        "35ad4b4563d9a1eb8d2b5ee66f7176cd2c6f05308b6ccba081262277fc1720c3",
    (
        "upsc-ai-kit/knowledge/Learner-v2-Refreshed/Polity/"
        "Subject-Wide-Syllabus/learning-sessions/polity-07/g15/"
        "polity-07_Solved-Practice-Workbook_2026-08-23.md"
    ):
        "de188a4c77774929762118f365c1fb79af7fe2bbc9eb89d29c764568a8d0a411",
    "upsc-ai-kit/knowledge/Polity/basic/Fundamental-Rights.md":
        "39bc9a74719c3f79b8817cbedd40ae46400d75623f4018c7e7f7cc54ac19e7ed",
    "upsc-ai-kit/knowledge/Polity/advanced/07_Fundamental-Rights.md":
        "3a24f3d4ca1caec3d6b1009068381730d4d6de3dddb6e412b0c47ceaf37fafc5",
    "upsc-ai-kit/knowledge/Polity/07_Fundamental-Rights_Complete-Topic-Package.md":
        "c58afaf55d856a8eef81795df214430c7134abf75f3276703d654b3474741f0e",
    (
        "notes/Learner-v2-Refreshed/Polity/Subject-Wide-Syllabus/"
        "learning-sessions/polity-07/g15/"
        "polity-07_Complete-Learning-Session_2026-08-23.pdf"
    ):
        "316c4e16d4dc4ff9770d24f66bcfe788bb267fd4df39749de33ed76ac2ee773c",
    (
        "notes/Learner-v2-Refreshed/Polity/Subject-Wide-Syllabus/"
        "learning-sessions/polity-07/g15/"
        "polity-07_Solved-Practice-Workbook_2026-08-23.pdf"
    ):
        "e0b34765c6f0227f3829374385d808e7f11cdf21d6a749cfa0c4bc070daf1bc0",
    (
        "upsc-ai-kit/knowledge/Easy-Learning/Polity/06-Citizenship/"
        "Citizenship-Guided-Learning-Edition.md"
    ):
        "14f109abedc834ff8a1623bd8fa2b3561c7a67ae0c2c86a16866b507d5b4d596",
    (
        "notes/Easy-Learning/Polity/06-Citizenship/"
        "Citizenship-Guided-Learning-Edition.pdf"
    ):
        "f5110cbb3e518e3c698e99ef59987d296ef4e1045d146267282ff92dd9696c39",
}

MODULE_SEQUENCE = [
    "WHAT ARE WE LEARNING?",
    "TEACHER EXPLAINS",
    "SIMPLE EXAMPLE / ANALOGY",
    "VISUAL FIRST",
    "NOW ADD THE EXACT LAW",
    "COMMON CONFUSION",
    "WHAT MUST I REMEMBER?",
    "CHECK YOUR UNDERSTANDING",
    "EXAM USE",
    "IF YOU WANT THE FULL DETAIL",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def headings(text: str) -> list[str]:
    return [
        match.group(1).strip()
        for match in re.finditer(r"^#{1,4}\s+(.+?)\s*$", text, re.MULTILINE)
    ]


class EasyLearningCitizenshipTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.markdown = MARKDOWN.read_text(encoding="utf-8")
        cls.coverage = COVERAGE.read_text(encoding="utf-8")

    def test_latest_tracker_record_is_g14(self) -> None:
        tracker = json.loads(
            (ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8")
        )
        records = [
            item
            for item in tracker["exports"]
            if item.get("topic_key") == "polity-06"
            and item.get("variant") == "learner-v2"
        ]
        latest = max(records, key=lambda item: item["generation"])
        self.assertEqual("polity-06:learner-v2:g14", latest["record_id"])
        self.assertEqual(str(SOURCE_MD.relative_to(ROOT)).replace("/", "\\"),
                         latest["markdown"])

    def test_protected_sources_trackers_generators_and_old_pdfs_are_unchanged(self) -> None:
        for relative, expected in EXPECTED_PROTECTED_HASHES.items():
            with self.subTest(path=relative):
                self.assertEqual(expected, sha256(ROOT / relative))

    def test_requested_user_facing_files_exist(self) -> None:
        for path in (PDF, README, COVERAGE, MARKDOWN):
            with self.subTest(path=path):
                self.assertTrue(path.is_file())
                self.assertGreater(path.stat().st_size, 100)
        self.assertFalse((TOPIC_DIR / "validation").exists())

    def test_opening_and_four_learning_layers_are_explicit(self) -> None:
        required = [
            "### What this topic means",
            "### Why a citizen and a UPSC candidate need it",
            "### Visual roadmap of modules",
            "### How to use this book",
            "FOUNDATION — MUST UNDERSTAND",
            "EXACT CONSTITUTIONAL/LEGAL LAYER — MUST KNOW",
            "EXAM APPLICATION — MUST PRACTISE",
            "ADVANCED/REFERENCE — READ AFTER THE CORE",
            "First Pass",
            "Exact Law Pass",
            "Exam Pass",
            "Data Vault",
        ]
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.markdown)

    def test_all_twelve_modules_use_the_exact_teacher_led_sequence(self) -> None:
        modules = list(
            re.finditer(r"^## MODULE (\d+)\b.*$", self.markdown, re.MULTILINE)
        )
        self.assertEqual(12, len(modules))
        final_answers = self.markdown.index(
            "## FINAL ANSWERS — CHECK YOUR UNDERSTANDING"
        )
        for index, module in enumerate(modules):
            end = (
                modules[index + 1].start()
                if index + 1 < len(modules)
                else final_answers
            )
            section = self.markdown[module.end():end]
            actual = re.findall(r"^### (.+?)\s*$", section, re.MULTILINE)
            self.assertEqual(MODULE_SEQUENCE, actual)
            check = section.split("### CHECK YOUR UNDERSTANDING", 1)[1]
            check = check.split("### EXAM USE", 1)[0]
            self.assertEqual(2, len(re.findall(r"^\d+\.\s+", check, re.MULTILINE)))
            self.assertNotRegex(check, r"(?im)^\*\*answer")

    def test_answers_are_deferred_and_complete(self) -> None:
        answers_at = self.markdown.index(
            "## FINAL ANSWERS — CHECK YOUR UNDERSTANDING"
        )
        vault_at = self.markdown.index(
            "## COMPLETE DATA VAULT — ADVANCED/REFERENCE"
        )
        self.assertGreater(answers_at, self.markdown.index("## MODULE 12"))
        self.assertGreater(vault_at, answers_at)
        answer_block = self.markdown[answers_at:vault_at]
        self.assertEqual(
            list(range(1, 13)),
            [
                int(number)
                for number in re.findall(
                    r"^### Module (\d+) answers$", answer_block, re.MULTILINE
                )
            ],
        )
        self.assertEqual(
            24,
            len(re.findall(r"^[12]\.\s+", answer_block, re.MULTILINE)),
        )

    def test_required_citizenship_scope_and_precision_are_present(self) -> None:
        required = [
            "citizenship, nationality, domicile and residence",
            "Articles 5-8",
            "Articles 9-11",
            "single citizenship",
            "Citizenship Act, 1955",
            "Renunciation",
            "Termination",
            "Deprivation",
            "OCI is not dual citizenship",
            "Section 6A",
            "Citizenship (Amendment) Act, 2019",
            "Rules notified 11 March 2024",
            "refugee",
            "stateless",
            "Voting is statutory",
            "Article 5(c)",
            "other than Article 6(b)(ii)",
            "Citizens by birth and descent fall outside this gate",
        ]
        lowered = self.markdown.lower()
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker.lower(), lowered)
        self.assertNotIn(
            "citizen-only rights: Articles 15, 16, 19, 29 and 30",
            self.markdown,
        )
        self.assertNotRegex(
            self.markdown,
            r"^## MODULE \d+.*FUNDAMENTAL RIGHTS",
        )
        self.assertNotIn("## Fundamental Rights", self.markdown)
        self.assertNotIn("## FUNDAMENTAL RIGHTS", self.markdown)

    def test_data_vault_has_every_requested_reference_component(self) -> None:
        vault = self.markdown[
            self.markdown.index("## COMPLETE DATA VAULT — ADVANCED/REFERENCE"):
        ]
        expected = [
            "D1. Article-by-Article table",
            "D2. Statute and amendment timeline",
            "D3. Case matrix",
            "D4. Current-affairs and source matrix",
            "D5. Exact PYQ demand map",
            "D6. Exceptions and edge cases",
            "D7. Glossary",
            "D8. Consolidated final register notes",
            "D9. Complete-topic ASCII master",
            "D10. Source-Preservation Annex",
        ]
        positions = [vault.index(item) for item in expected]
        self.assertEqual(sorted(positions), positions)

    def test_coverage_report_maps_every_source_heading(self) -> None:
        source_headings = headings(SOURCE_MD.read_text(encoding="utf-8"))
        workbook_headings = headings(WORKBOOK_MD.read_text(encoding="utf-8"))
        ledger = self.coverage[
            self.coverage.index("## Source heading ledger"):
            self.coverage.index("## Article/reference inventory")
        ]
        self.assertEqual(255, len(source_headings))
        self.assertEqual(63, len(workbook_headings))
        for heading in source_headings + workbook_headings:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.coverage)
        self.assertEqual(
            len(source_headings),
            len(
                re.findall(
                    r"^\| Active learning Markdown \|\s+\d+\s+\|",
                    ledger,
                    re.MULTILINE,
                )
            ),
        )
        self.assertEqual(
            len(workbook_headings),
            len(
                re.findall(
                    r"^\| Paired workbook Markdown \|\s+\d+\s+\|",
                    ledger,
                    re.MULTILINE,
                )
            ),
        )
        self.assertIn("ZERO UNEXPLAINED OMISSIONS", self.coverage)

    def test_pdf_layout_text_toc_and_font_floor(self) -> None:
        result = renderer.validate_pdf(PDF)
        self.assertEqual("passed", result["status"])
        self.assertGreaterEqual(result["page_count"], 40)
        self.assertGreaterEqual(result["bookmarks"], 16)
        self.assertTrue(result["toc_page_targets_valid"])
        self.assertFalse(result["blank_pages"])
        self.assertFalse(result["near_empty_pages"])
        self.assertFalse(result["replacement_glyph_pages"])
        self.assertFalse(result["overflow_pages"])
        self.assertFalse(result["tiny_font_pages"])
        self.assertGreaterEqual(result["observed_min_non_footer_font_pt"], 7.4)
        with fitz.open(PDF) as document:
            text = "\n".join(page.get_text("text") for page in document)
        for marker in (
            "CONTENTS / GUIDED MODULE INDEX",
            "MODULE 12",
            "FINAL ANSWERS",
            "COMPLETE DATA VAULT",
            "GUIDED PROGRESS",
        ):
            self.assertIn(marker, text)

    def test_renderer_is_reusable_on_a_small_markdown_document(self) -> None:
        scratch = TOOLS / ".test-easy-learning-pdf-scratch"
        if scratch.exists():
            shutil.rmtree(scratch)
        scratch.mkdir()
        try:
            source = scratch / "sample.md"
            output = scratch / "sample.pdf"
            source.write_text(
                "---\ntitle: \"Easy Learning Smoke Test\"\n---\n\n"
                "# Easy Learning Smoke Test\n\n"
                "## MODULE 1 — SAMPLE\n\n"
                "### WHAT ARE WE LEARNING?\n\nA focused question.\n\n"
                "### VISUAL FIRST\n\n```ascii-master\nSTART -> LAW -> USE\n```\n\n"
                "## COMPLETE DATA VAULT — ADVANCED/REFERENCE\n\n"
                "| Item | Rule |\n|---|---|\n| Test | Passed |\n",
                encoding="utf-8",
            )
            renderer.build_pdf(source, output)
            result = renderer.validate_pdf(output)
            self.assertEqual("passed", result["status"])
            self.assertGreaterEqual(result["observed_min_non_footer_font_pt"], 7.4)
        finally:
            if scratch.exists():
                shutil.rmtree(scratch)


class EasyLearningFundamentalRightsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.markdown = FR_MARKDOWN.read_text(encoding="utf-8")
        cls.coverage = FR_COVERAGE.read_text(encoding="utf-8")

    def test_latest_tracker_record_is_g15(self) -> None:
        tracker = json.loads(
            (ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8")
        )
        records = [
            item
            for item in tracker["exports"]
            if item.get("topic_key") == "polity-07"
            and item.get("variant") == "learner-v2"
        ]
        latest = max(records, key=lambda item: item["generation"])
        self.assertEqual("polity-07:learner-v2:g15", latest["record_id"])
        self.assertEqual(
            str(FR_SOURCE_MD.relative_to(ROOT)).replace("/", "\\"),
            latest["markdown"],
        )
        self.assertEqual(
            str(FR_WORKBOOK_MD.relative_to(ROOT)).replace("/", "\\"),
            latest["workbook_markdown"],
        )

    def test_protected_trackers_sources_generators_and_old_editions_are_unchanged(self) -> None:
        for relative, expected in EXPECTED_FR_PROTECTED_HASHES.items():
            with self.subTest(path=relative):
                self.assertEqual(expected, sha256(ROOT / relative))

    def test_requested_user_facing_files_exist(self) -> None:
        for path in (FR_PDF, FR_README, FR_COVERAGE, FR_MARKDOWN):
            with self.subTest(path=path):
                self.assertTrue(path.is_file())
                self.assertGreater(path.stat().st_size, 100)
        self.assertFalse((FR_TOPIC_DIR / "validation").exists())

    def test_opening_and_four_learning_layers_are_explicit(self) -> None:
        required = [
            "### What this topic means",
            "### Why it matters",
            "### Visual roadmap of modules",
            "### How to use this book",
            "FOUNDATION — MUST UNDERSTAND",
            "EXACT CONSTITUTIONAL/LEGAL LAYER — MUST KNOW",
            "EXAM APPLICATION — MUST PRACTISE",
            "ADVANCED/REFERENCE — READ AFTER THE CORE",
            "First Pass",
            "Exact Law Pass",
            "Exam Pass",
            "Data Vault",
        ]
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker, self.markdown)

    def test_all_sixteen_modules_use_the_exact_teacher_led_sequence(self) -> None:
        modules = list(
            re.finditer(r"^## MODULE (\d+)\b.*$", self.markdown, re.MULTILINE)
        )
        self.assertEqual(16, len(modules))
        final_answers = self.markdown.index(
            "## FINAL ANSWERS — CHECK YOUR UNDERSTANDING"
        )
        for index, module_match in enumerate(modules):
            end = (
                modules[index + 1].start()
                if index + 1 < len(modules)
                else final_answers
            )
            section = self.markdown[module_match.end():end]
            actual = re.findall(r"^### (.+?)\s*$", section, re.MULTILINE)
            self.assertEqual(MODULE_SEQUENCE, actual)
            check = section.split("### CHECK YOUR UNDERSTANDING", 1)[1]
            check = check.split("### EXAM USE", 1)[0]
            self.assertEqual(
                2,
                len(re.findall(r"^\d+\.\s+", check, re.MULTILINE)),
            )
            self.assertNotRegex(check, r"(?im)^\*\*answer")

    def test_answers_are_deferred_and_complete(self) -> None:
        answers_at = self.markdown.index(
            "## FINAL ANSWERS — CHECK YOUR UNDERSTANDING"
        )
        vault_at = self.markdown.index(
            "## COMPLETE DATA VAULT — ADVANCED/REFERENCE"
        )
        self.assertGreater(answers_at, self.markdown.index("## MODULE 16"))
        self.assertGreater(vault_at, answers_at)
        answer_block = self.markdown[answers_at:vault_at]
        self.assertEqual(
            list(range(1, 17)),
            [
                int(number)
                for number in re.findall(
                    r"^### Module (\d+) answers$", answer_block, re.MULTILINE
                )
            ],
        )
        self.assertEqual(
            32,
            len(re.findall(r"^[12]\.\s+", answer_block, re.MULTILINE)),
        )

    def test_required_fundamental_rights_scope_is_present(self) -> None:
        required = [
            "Articles 12-35",
            "State/instrumentality",
            "citizen versus person",
            "reasonable classification",
            "anti-arbitrariness",
            "affirmative action",
            "Article 21A",
            "legal aid",
            "speedy trial",
            "vertical",
            "horizontal",
            "waiver",
            "severability",
            "eclipse",
            "constitutional morality",
            "proportionality",
            "Article 226",
            "Articles 31A-31C",
            "Article 300A",
            "Articles 358-359",
            "Davinder Singh",
            "Property Owners",
            "Electoral Bonds",
            "DPDP",
            "BNS section 152",
            "INFERRED ANSWER - NOT OFFICIALLY VERIFIED",
            "PROVISIONAL 2026 KEY - NOT OFFICIAL",
        ]
        lowered = self.markdown.lower()
        for marker in required:
            with self.subTest(marker=marker):
                self.assertIn(marker.lower(), lowered)

    def test_data_vault_has_every_requested_reference_component(self) -> None:
        vault = self.markdown[
            self.markdown.index("## COMPLETE DATA VAULT — ADVANCED/REFERENCE"):
        ]
        expected = [
            "D1. Articles 12-35 table",
            "D2. Doctrine and test matrix",
            "D3. Case chronology and holdings matrix",
            "D4. Amendments, Emergency and property timeline",
            "D5. Citizen-only, person-rights and group-rights matrix",
            "D6. Writs and Article 32/226 retrieval table",
            "D7. Current-source matrix",
            "D8. Exact PYQ demand map",
            "D9. Exceptions and edge cases",
            "D10. Glossary",
            "D11. Final consolidated register notes",
            "D12. Latest authored complete-topic ASCII master",
            "D13. Source-Preservation Annex",
        ]
        positions = [vault.index(item) for item in expected]
        self.assertEqual(sorted(positions), positions)

    def test_coverage_report_maps_every_source_heading(self) -> None:
        source_headings = headings(FR_SOURCE_MD.read_text(encoding="utf-8"))
        workbook_headings = headings(
            FR_WORKBOOK_MD.read_text(encoding="utf-8")
        )
        ledger = self.coverage[
            self.coverage.index("## Source heading ledger"):
            self.coverage.index("## Article/reference inventory")
        ]
        self.assertEqual(370, len(source_headings))
        self.assertEqual(85, len(workbook_headings))
        for heading in source_headings + workbook_headings:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.coverage)
        self.assertEqual(
            len(source_headings),
            len(
                re.findall(
                    r"^\| Active learning Markdown \|\s+\d+\s+\|",
                    ledger,
                    re.MULTILINE,
                )
            ),
        )
        self.assertEqual(
            len(workbook_headings),
            len(
                re.findall(
                    r"^\| Paired workbook Markdown \|\s+\d+\s+\|",
                    ledger,
                    re.MULTILINE,
                )
            ),
        )
        self.assertIn("ZERO UNEXPLAINED OMISSIONS", self.coverage)
        self.assertIn("| Unexplained omissions | **0** |", self.coverage)

    def test_pdf_layout_text_toc_and_font_floor(self) -> None:
        result = renderer.validate_pdf(FR_PDF)
        self.assertEqual("passed", result["status"])
        self.assertGreaterEqual(result["page_count"], 100)
        self.assertGreaterEqual(result["bookmarks"], 20)
        self.assertTrue(result["toc_page_targets_valid"])
        self.assertFalse(result["blank_pages"])
        self.assertFalse(result["near_empty_pages"])
        self.assertFalse(result["replacement_glyph_pages"])
        self.assertFalse(result["overflow_pages"])
        self.assertFalse(result["tiny_font_pages"])
        self.assertGreaterEqual(
            result["observed_min_non_footer_font_pt"], 7.4
        )
        with fitz.open(FR_PDF) as document:
            text = "\n".join(page.get_text("text") for page in document)
        for marker in (
            "CONTENTS / GUIDED MODULE INDEX",
            "MODULE 16",
            "FINAL ANSWERS",
            "COMPLETE DATA VAULT",
            "ARTICLES 12-35 TABLE",
            "SOURCE-PRESERVATION ANNEX",
            "GUIDED PROGRESS",
        ):
            self.assertIn(marker, text.upper())

    def test_shared_navigation_links_both_finished_editions(self) -> None:
        start = START_HERE.read_text(encoding="utf-8")
        tracker = TRACKER.read_text(encoding="utf-8")
        for text in (start, tracker):
            self.assertIn(
                "Polity/06-Citizenship/Citizenship-Guided-Learning-Edition.pdf",
                text,
            )
            self.assertIn(
                "Polity/07-Fundamental-Rights/"
                "Fundamental-Rights-Guided-Learning-Edition.pdf",
                text,
            )
            self.assertIn("additional guided layer", text.lower())
            self.assertIn("not a replacement", text.lower())

    def test_technical_previews_are_outside_user_topic_folder(self) -> None:
        self.assertTrue(FR_PREVIEW_DIR.is_dir())
        self.assertTrue(
            (FR_PREVIEW_DIR / "renderer-validation.json").is_file()
        )
        self.assertGreaterEqual(
            len(list(FR_PREVIEW_DIR.glob("contact-sheet-*.png"))),
            1,
        )
        self.assertFalse((FR_TOPIC_DIR / "validation").exists())


if __name__ == "__main__":
    unittest.main()
