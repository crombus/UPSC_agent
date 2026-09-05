"""Regression tests for Indian Art and Culture learner-v2 Topics 11-12."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_10_sequential as previous
import generate_indian_art_culture_11_12_sequential as generator
import validate_v2_export as validator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture1112GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-11", "indian-art-and-culture-12"],
            [
                "Languages, Scripts, Literature and Manuscripts",
                "Crafts, Textiles, Folk and Tribal Traditions",
            ],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-10"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_language_script_and_manuscript_boundaries_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-11")
        for phrase in (
            "Language family, script, literary register",
            "Kharoshthi ran right-to-left",
            "Sangam corpus, compiled around CE 300-600",
            "Gyan Bharatam National Manuscript Survey",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)

    def test_craft_gi_and_eri_boundaries_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-12")
        for phrase in (
            "origin-linked product name",
            "Patola from Patan uses double ikat",
            "Eri silk is commonly produced in Meghalaya",
            "holds no verified criteria",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        for config in generator.TOPICS:
            audit = validator.deep_content_quality_audit_text(
                session_markdown(generator, str(config["key"])),
                topic_key=str(config["key"]),
            )
            high = [
                item
                for item in audit["defects"]
                if item["severity"] in {"high", "blocker"}
            ]
            self.assertEqual([], high, str(config["key"]))

    def test_generator_has_no_publish_side_effects(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        for forbidden in (
            "markdown_learning_pdf",
            "finalize_v2_topic",
            "generate_export_command_index",
            "EXPORT-PDF-STATUS.json",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
