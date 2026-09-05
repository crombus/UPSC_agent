"""Regression tests for Indian Society learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_indian_society_04_sequential as previous
import generate_indian_society_05_sequential as generator
import validate_v2_export as validator
from indian_society_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
    workbook_markdown,
)


class IndianSociety05GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["indian-society-05"],
            ["Rural Society and Agrarian Change"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["indian-society-04"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_rural_structure_and_measurement_limits_are_preserved(self) -> None:
        text = session_markdown(generator, "indian-society-05")
        for phrase in (
            "jajman",
            "kamin",
            "M.N. Srinivas",
            "Rampura",
            "Green Revolution",
            "Panchayati Raj",
            "rural-urban continuum",
            "Periodic Labour Force Survey Annual Report 2025",
            "January-December",
        ):
            self.assertIn(phrase, text)

    def test_zero_direct_pyq_status_is_transparent_and_unfabricated(self) -> None:
        text = session_markdown(generator, "indian-society-05")
        workbook = workbook_markdown(generator, "indian-society-05")
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", workbook)
        self.assertEqual(0, text.count("### PYQ DEMAND CARD"))
        self.assertEqual([], generator.TOPICS[0]["pyq_solutions"])
        self.assertEqual(6, text.count("### ORIGINAL MAINS"))

    def test_advanced_owner_is_preserved_in_the_optional_block(self) -> None:
        text = session_markdown(generator, "indian-society-05")
        advanced = text.split(
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            1,
        )[1].split("## CONSOLIDATED REGISTER NOTES", 1)[0]
        for phrase in (
            "Jajmani system vs cash-wage labour market",
            "Formal representation vs substantive power",
            "Green Revolution differentiation chain",
        ):
            self.assertIn(phrase, advanced)
        self.assertNotIn("\n## 6.", advanced)

    def test_session_definitions_pass_semantic_quality_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "indian-society-05"),
            topic_key="indian-society-05",
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
