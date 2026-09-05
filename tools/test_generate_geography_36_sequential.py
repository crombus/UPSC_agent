"""Regression tests for Geography learner-v2 Topic 36."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_36_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography36GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-36"],
            ["Contemporary Geographical Issues (India)"],
            expected_section="Part-B-Human-Economic-and-Regional-Geography",
            expected_section_key="part-b-human-economic-and-regional-geography",
            expected_generation=1,
            expected_supersedes_template=None,
            expect_allow_existing_history=False,
        )

    def test_issue_analysis_boundaries(self) -> None:
        text = session_markdown(generator, "geography-36")
        for phrase in (
            "exposure",
            "vulnerability",
            "aquifer",
            "managed recharge",
            "Krishna",
            "Great Nicobar",
            "AMRUT",
        ):
            self.assertIn(phrase, text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)
        self.assertEqual(3, text.count("### PYQ DEMAND CARD"))

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-36"),
            topic_key="geography-36",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
