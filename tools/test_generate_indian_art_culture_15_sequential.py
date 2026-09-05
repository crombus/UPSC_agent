"""Regression tests for Indian Art and Culture learner-v2 Topic 15."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_art_culture_13_14_sequential as previous
import generate_indian_art_culture_15_sequential as generator
import validate_v2_export as validator
from indian_art_culture_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class IndianArtCulture15GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-art-and-culture-15"],
            ["Indian Cinema, Film Institutions and Awards"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-art-and-culture-13", "indian-art-and-culture-14"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_cinema_history_institutions_and_award_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-15")
        for phrase in (
            "Sairandhri in 1933",
            "Kisan Kanya in 1937",
            "23 December 2020 decision",
            "Children's and Family Film",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)
        fact_text = " ".join(text for _label, text in generator.TOPICS[0]["facts"])
        self.assertIn("UA7+, UA13+ and UA16+", fact_text)
        self.assertIn("section 5C appeals lie to the High Court", fact_text)
        self.assertIn("section 5D's FCAT was omitted in 2021", fact_text)

    def test_short_advanced_owner_is_preserved_without_fabricated_sections(self) -> None:
        text = session_markdown(generator, "indian-art-and-culture-15")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Cinema is simultaneously an art form, an industry, an archive",
            "*Boong* as a case study",
            "An international award establishes universal cultural superiority",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-art-and-culture-15"),
            topic_key="indian-art-and-culture-15",
        )
        high = [
            item
            for item in audit["defects"]
            if item["severity"] in {"high", "blocker"}
        ]
        self.assertEqual([], high)

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
