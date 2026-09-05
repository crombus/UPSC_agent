"""Regression tests for Indian Society learner-v2 Topic 04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_03_sequential as previous
import generate_indian_society_04_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class IndianSociety04GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-04"],
            ["Family, Marriage and Kinship"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-03"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_kinship_evidence_and_data_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-04")
        for phrase in (
            "Khasi",
            "Nair",
            "gotra exogamy",
            "Special Marriage Act, 1954",
            "Total Fertility Rate of 2.0",
            "29 May 2026",
        ):
            self.assertIn(phrase, text)

    def test_matriliny_is_not_presented_as_matriarchy(self) -> None:
        text = session_markdown(generator, "indian-society-04")
        self.assertIn("must not be equated with matriarchal authority", text)

    def test_four_verified_pyq_demands_are_reproduced(self) -> None:
        text = session_markdown(generator, "indian-society-04")
        for phrase in (
            "Explore and evaluate the impact of 'Work From Home' on family relationships.",
            "Do you think marriage as a sacrament is loosing its value in Modern India?",
            "Child cuddling is now being replaced by mobile phones.",
            "Intercaste marriages between castes which have socio-economic parity",
        ):
            self.assertIn(phrase, text)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-04")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Structural nuclearisation vs functional nuclearisation",
            "Live-in relationship recognition gap",
            "Globalisation-family chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-04"),
            topic_key="indian-society-04",
        )
        high = [
            item
            for item in audit["defects"]
            if item["severity"] in {"high", "blocker"}
        ]
        self.assertEqual([], high)

    def test_generator_has_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
