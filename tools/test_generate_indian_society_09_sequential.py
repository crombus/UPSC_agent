"""Regression tests for Indian Society learner-v2 Topic 09."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_08_sequential as previous
import generate_indian_society_09_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety09GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-09"],
            ["Poverty and Developmental Issues"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-08"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_deprivation_theory_and_conflict_design_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-09")
        for phrase in (
            "capability deprivation",
            "Amartya Sen",
            "social exclusion",
            "Oscar Lewis",
            "culture of poverty",
            "participatory conservation",
            "exclusionary conservation",
            "Tendulkar",
            "Rangarajan",
        ):
            self.assertIn(phrase, text)

    def test_poverty_estimate_is_dated_and_not_attributed_to_a_programme(self) -> None:
        text = session_markdown(generator, "indian-society-09")
        self.assertIn("11.28", text)
        self.assertIn("24.8 crore", text)
        self.assertIn("2022-23", text)
        self.assertIn("rather than a current headcount", text)

    def test_routed_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-09")
        workbook = workbook_markdown(generator, "indian-society-09")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-09")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Capability-deprivation chain",
            "Development-livelihood conflict chain (2025 PYQ)",
            "Three-actor collaboration chain (2024 PYQ)",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-09"),
            topic_key="indian-society-09",
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
