"""Regression tests for Indian Society learner-v2 Topic 06."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_05_sequential as previous
import generate_indian_society_06_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety06GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-06"],
            ["Population and Associated Issues"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-05"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_population_determinants_and_data_boundaries_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-06")
        for phrase in (
            "National Population Policy, 2000",
            "Ministry of Health and Family Welfare",
            "Total Fertility Rate",
            "replacement level",
            "NFHS-5",
            "NFHS-6",
            "29 May 2026",
            "son preference",
            "sex ratio at birth",
            "demographic winter",
            "demographic dividend",
            "second demographic transition",
            "population education",
        ):
            self.assertIn(phrase, text)

    def test_no_unsourced_demographic_statistic_is_asserted(self) -> None:
        text = session_markdown(generator, "indian-society-06")
        self.assertIn("provisional", text)
        self.assertIn("Census stock", text)
        self.assertNotIn("Census 2027 caste figure", text)

    def test_routed_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-06")
        workbook = workbook_markdown(generator, "indian-society-06")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(3, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-06")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Demographic winter vs demographic dividend",
            "First versus second demographic transition",
            "Demographic-winter-risk chain (state-level)",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-06"),
            topic_key="indian-society-06",
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
