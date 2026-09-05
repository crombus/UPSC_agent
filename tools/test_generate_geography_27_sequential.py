"""Regression tests for Geography learner-v2 Topic 27."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_26_sequential as previous
import generate_geography_27_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography27GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-27"],
            ["Migration Theories and Patterns (India)"],
            expected_section="Part-B-Human-Economic-and-Regional-Geography",
            expected_section_key="part-b-human-economic-and-regional-geography",
            expected_generation=3,
            expected_supersedes_template="{key}:learner-v2:g2",
            expect_allow_existing_history=True,
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-26"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_migration_boundaries(self) -> None:
        text = session_markdown(generator, "geography-27")
        for phrase in ("Ravenstein", "Lee", "intrastate", "marriage", "circular migration"):
            self.assertIn(phrase, text)
        self.assertIn("VERIFIED PYQ OWNERSHIP AUDIT", text)

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-27"),
            topic_key="geography-27",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
