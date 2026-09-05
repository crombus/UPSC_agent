"""Regression tests for the shared qualifying-language package publisher."""

from __future__ import annotations

import shutil
import unittest
from pathlib import Path

import fitz

import generate_language_master_packages as generator
import publish_language_master_packages as publisher


class LanguageMasterPublisherTests(unittest.TestCase):
    def test_subject_configs_keep_distinct_english_and_hindi_owners(self) -> None:
        english = generator.CONFIGS["Qualifying-English"]
        hindi = generator.CONFIGS["Qualifying-Hindi"]
        self.assertEqual(12, len(english["guide_sources"]))
        self.assertEqual(12, len(hindi["guide_sources"]))
        self.assertEqual(3, len(english["practice_sources"]))
        self.assertEqual(3, len(english["solution_sources"]))
        self.assertNotEqual(english["guide_sources"], hindi["guide_sources"])
        self.assertNotIn(
            "translation where applicable",
            english["guide_introduction"].casefold(),
        )
        self.assertIn(
            "translation where applicable",
            hindi["guide_introduction"].casefold(),
        )

    def test_combiner_adds_navigation_and_preserves_source_bodies(self) -> None:
        config = generator.CONFIGS["Qualifying-English"]
        folder = generator.KNOWLEDGE / "Qualifying-English"
        text = generator.combine(
            folder,
            config["title"],
            config["labels"][0],
            config["guide_sources"],
            config["guide_introduction"],
        )
        self.assertIn("## PACKAGE NAVIGATION", text)
        self.assertIn("Question-only Workbook", text)
        for source in config["guide_sources"]:
            body = generator.strip_h1(
                (folder / source).read_text(encoding="utf-8")
            )
            self.assertIn(body, text)

    def test_renderer_can_add_legacy_contract_index_without_v2_rewrite(self) -> None:
        work = publisher.ROOT / "tools" / ".language-publisher-test"
        shutil.rmtree(work, ignore_errors=True)
        work.mkdir(parents=True)
        source = work / "sample.md"
        output = work / "sample.pdf"
        try:
            source.write_text(
                "# Sample Guide\n\n## First skill\n\n"
                "| Path | Meaning |\n|---|---|\n"
                "| basic/01-test | précis — one-third |\n\n"
                "## Second skill\n\nNo answer leakage.\n",
                encoding="utf-8",
            )
            publisher.render(
                source,
                output,
                "qualifying-language-test",
                document_kind="Complete Skills Guide",
            )
            with fitz.open(output) as document:
                text = "\n".join(page.get_text("text") for page in document)
                self.assertTrue(document.get_toc())
                self.assertIn("CONTENTS / COMPLETE SKILLS GUIDE", text)
                self.assertNotIn("&#8203;", text)
                self.assertNotIn("\ufffd", text)
        finally:
            shutil.rmtree(work, ignore_errors=True)

    def test_unicode_renderer_adds_index_bookmarks_and_page_numbers(self) -> None:
        work = publisher.ROOT / "tools" / ".hindi-language-publisher-test"
        shutil.rmtree(work, ignore_errors=True)
        work.mkdir(parents=True)
        source = work / "sample.md"
        output = work / "sample.pdf"
        try:
            source.write_text(
                "# हिन्दी नमूना\n\n> देवनागरी परीक्षण।\n\n"
                "## पहला कौशल\n\nमात्रा, संयुक्ताक्षर और नुक्ता: माँ, उद्देश्य, फ़िल्म।\n\n"
                "### अभ्यास\n\nप्रश्न केवल अभ्यास के लिए है।\n",
                encoding="utf-8",
            )
            publisher.render(
                source,
                output,
                "qualifying-hindi-test",
                unicode_heavy=True,
                document_kind="Question-Only Practice Workbook",
            )
            with fitz.open(output) as document:
                text = "\n".join(page.get_text("text") for page in document)
                self.assertTrue(document.get_toc())
                self.assertIn(
                    "CONTENTS / QUESTION-ONLY PRACTICE WORKBOOK", text
                )
                self.assertIn("माँ, उद्देश्य, फ़िल्म", text)
                self.assertNotIn("HIDX", text)
                self.assertNotIn("\ufffd", text)
                self.assertIn(f"1/{document.page_count}", text)
        finally:
            shutil.rmtree(work, ignore_errors=True)

    def test_generation_parameter_uses_immutable_generation_folder(self) -> None:
        source = Path(publisher.__file__).read_text(encoding="utf-8")
        self.assertIn('f"g{generation}"', source)
        self.assertIn('"generation": generation', source)
        self.assertIn('g{generation}-{generated_on}-record.json', source)


if __name__ == "__main__":
    unittest.main()
