"""Regression tests for Indian Society learner-v2 Topic 08."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_07_sequential as previous
import generate_indian_society_08_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety08GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-08"],
            ["Social Empowerment"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-07"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_capability_and_reform_diagnoses_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-08")
        for phrase in (
            "capability approach",
            "Amartya Sen",
            "functionings",
            "Satyashodhak Samaj",
            "Savitribai Phule",
            "graded inequality",
            "annihilation of caste",
            "conversion factor",
            "substantive mobility",
        ):
            self.assertIn(phrase, text)

    def test_multidimensional_estimate_is_dated_and_bounded(self) -> None:
        text = session_markdown(generator, "indian-society-08")
        self.assertIn("11.28", text)
        self.assertIn("24.8 crore", text)
        self.assertIn("2022-23", text)
        self.assertIn("rather than a current headcount", text)

    def test_cross_owned_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-08")
        workbook = workbook_markdown(generator, "indian-society-08")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(2, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(2, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("the conflict is recorded openly", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-08")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Capability-conversion chain (2024 PYQ core)",
            "Phule's diagnostic chain",
            "Ambedkar's diagnostic chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-08"),
            topic_key="indian-society-08",
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
