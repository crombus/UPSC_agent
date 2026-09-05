"""Regression tests for Geography learner-v2 Topic 31."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_31_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography31GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-31"],
            ["Mineral and Energy Resources: World and India"],
            expected_section="Part-B-Human-Economic-and-Regional-Geography",
            expected_section_key="part-b-human-economic-and-regional-geography",
            expected_generation=2,
            expected_supersedes_template="{key}:legacy-v1:g1",
            expect_allow_existing_history=False,
        )

    def test_mineral_and_energy_boundaries(self) -> None:
        text = session_markdown(generator, "geography-31")
        for phrase in (
            "four-element petroleum system",
            "Chota Nagpur",
            "Bailadila",
            "Krishna-Godavari",
            "midstream",
            "National Critical Mineral Mission",
        ):
            self.assertIn(phrase, text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertEqual(5, text.count("### PYQ DEMAND CARD"))

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-31"),
            topic_key="geography-31",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
