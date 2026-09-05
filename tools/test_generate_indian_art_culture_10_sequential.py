"""Regression tests for Indian Art and Culture learner-v2 Topic 10."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_08_09_sequential as previous
import generate_indian_art_culture_10_sequential as generator
import validate_v2_export as validator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture10GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-10"],
            ["Theatre, Puppetry and Performance Traditions"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-08", "indian-art-and-culture-09"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_theatre_puppetry_and_safeguarding_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-10")
        for phrase in (
            "Lokadharmi denotes realistic representation",
            "Dramatic Performances Act of 1876",
            "String, shadow, rod and glove",
            "policy-actionable vulnerability",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(
            ["https://ich.unesco.org/en/RL/kutiyattam-sanskrit-theatre-00010"],
            generator.TOPICS[0]["live_sources"],
        )

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-art-and-culture-10"),
            topic_key="indian-art-and-culture-10",
        )
        definition_defects = [
            item
            for item in audit["defects"]
            if item["category"] in {"definition-quality", "definition-alignment"}
        ]
        self.assertEqual([], definition_defects)

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
