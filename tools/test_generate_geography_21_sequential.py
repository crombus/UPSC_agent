"""Regression tests for Geography learner-v2 Topic 21."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_20_sequential as previous
import generate_geography_21_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography21GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-21"],
            ["Warm Temperate Eastern Margin China Type"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-20"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_china_type_boundaries(self) -> None:
        text = session_markdown(generator, "geography-21")
        for phrase in ("typhoon", "Bay of Bengal branch", "Tripura", "subcontinental counterpart"):
            self.assertIn(phrase, text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-21"),
            topic_key="geography-21",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
