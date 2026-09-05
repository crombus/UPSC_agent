"""Regression tests for Geography learner-v2 Topic 26."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_26_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography26GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-26"],
            ["World Population and Demographic Transition"],
            expected_section="Part-B-Human-Economic-and-Regional-Geography",
            expected_section_key="part-b-human-economic-and-regional-geography",
            expected_generation=3,
            expected_supersedes_template="{key}:learner-v2:g2",
            expect_allow_existing_history=True,
        )

    def test_population_transition_boundaries(self) -> None:
        text = session_markdown(generator, "geography-26")
        for phrase in (
            "demographic transition",
            "population pyramid",
            "Kerala",
            "EAG",
            "SRS 2022",
        ):
            self.assertIn(phrase, text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-26"),
            topic_key="geography-26",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
