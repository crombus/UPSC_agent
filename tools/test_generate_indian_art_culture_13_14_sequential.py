"""Regression tests for Indian Art and Culture learner-v2 Topics 13-14."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_11_12_sequential as previous
import generate_indian_art_culture_13_14_sequential as generator
import validate_v2_export as validator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture1314GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-13", "indian-art-and-culture-14"],
            [
                "Religion, Philosophy and Cultural Synthesis",
                "Heritage Conservation, Institutions and UNESCO",
            ],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-11", "indian-art-and-culture-12"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_religion_philosophy_and_synthesis_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-13")
        for phrase in (
            "Artha, Dharma, Kama and Moksha",
            "Pushtimarg belongs to Vallabhacharya",
            "Sufism cannot be reduced to one uniformly syncretic position",
            "Indian philosophy and tradition played a significant role",
        ):
            self.assertIn(phrase, text)

    def test_heritage_categories_and_institutions_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-14")
        for phrase in (
            "four non-interchangeable systems",
            "generally prohibited first 100 metres",
            "Manas and Hampi were once",
            "Safeguarding the Indian art heritage is the need of the moment",
        ):
            self.assertIn(phrase, text)
        current = str(generator.TOPICS[1]["current_note"])
        self.assertIn("Sarnath as a serial property inscribed on 25 July 2026", current)
        self.assertIn("India's forty-fifth World Heritage property", current)
        self.assertIn("3,679 centrally protected monuments", current)

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
