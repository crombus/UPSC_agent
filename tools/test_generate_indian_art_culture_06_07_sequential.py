"""Regression tests for Indian Art and Culture learner-v2 Topics 06-07."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_05_sequential as previous
import generate_indian_art_culture_06_07_sequential as generator
import validate_v2_export as validator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture0607GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-06", "indian-art-and-culture-07"],
            ["Sculpture, Pottery and Iconography", "Painting Traditions"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-05"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_sculpture_pyqs_and_attribution_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-06")
        for phrase in (
            "cire-perdue",
            "uncontested sole origin",
            "Ravana Phadi",
            "commissioned representations",
            "### PYQ DEMAND CARD 3",
        ):
            self.assertIn(phrase, text)

    def test_painting_routes_and_live_boundary_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-07")
        for phrase in (
            "fresco secco",
            "Hallisalasya",
            "Bani Thani belongs to the Kishangarh school",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
            "64th National Exhibition of Art",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(
            ["https://lalitkala.gov.in/event_details/317"],
            generator.TOPICS[1]["live_sources"],
        )

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
