"""Regression tests for Indian Art and Culture learner-v2 Topics 08-09."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_06_07_sequential as previous
import generate_indian_art_culture_08_09_sequential as generator
import validate_v2_export as validator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture0809GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-08", "indian-art-and-culture-09"],
            ["Indian Music", "Indian Dance"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-06", "indian-art-and-culture-07"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_music_definitions_attribution_and_pyq_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-08")
        for phrase in (
            "unsung Hindustani parent scale",
            "seventy-two sampurna melakarta",
            "does not define a raga",
            "Mallikarjun Mansur",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(
            ["https://sangeetnatak.gov.in/award-honours/awardees"],
            generator.TOPICS[0]["live_sources"],
        )

    def test_dance_recognition_and_form_distinctions_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-09")
        for phrase in (
            "number 108 belongs to karanas",
            "Ministry of Culture list of nine including Chhau",
            "Nagabandha belongs to Manipuri",
            "UNESCO ICH 2023, not SNA classical",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        for config in generator.TOPICS:
            audit = validator.deep_content_quality_audit_text(
                session_markdown(generator, str(config["key"])),
                topic_key=str(config["key"]),
            )
            definition_defects = [
                item
                for item in audit["defects"]
                if item["category"] in {"definition-quality", "definition-alignment"}
            ]
            self.assertEqual([], definition_defects, str(config["key"]))

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
