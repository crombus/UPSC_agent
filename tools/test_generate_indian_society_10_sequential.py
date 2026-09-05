"""Regression tests for Indian Society learner-v2 Topic 10."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_09_sequential as previous
import generate_indian_society_10_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety10GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-10"],
            ["Urbanisation: Problems and Remedies"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-09"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_urban_mechanisms_and_justice_tests_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-10")
        for phrase in (
            "agglomeration",
            "Chain migration",
            "anomie",
            "rural-urban continuum",
            "distributive justice",
            "procedural justice",
            "smart city",
            "in-situ upgrading",
            "informal settlement",
            "Tier-2",
        ):
            self.assertIn(phrase, text)

    def test_urbanisation_share_is_labelled_a_projection(self) -> None:
        text = session_markdown(generator, "indian-society-10")
        self.assertIn("UN World Urbanization Prospects 2025", text)
        self.assertIn("36 per cent", text)
        self.assertIn("Census 2011", text)
        self.assertIn("rather than Census data", text)

    def test_routed_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-10")
        workbook = workbook_markdown(generator, "indian-society-10")
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", workbook)
        self.assertEqual(4, text.count("### PYQ DEMAND CARD"))
        self.assertEqual(4, len(generator.TOPICS[0]["pyq_solutions"]))
        self.assertIn("no verbatim wording is claimed", text)
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-10")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Migrant-pull chain (2024 PYQ)",
            "Slum-formation chain",
            "Smart-city distributive-justice chain (2025 PYQ)",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-10"),
            topic_key="indian-society-10",
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
