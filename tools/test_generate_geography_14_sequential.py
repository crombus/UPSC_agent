"""Regression tests for Geography learner-v2 Topic 14."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_12_13_sequential as previous
import generate_geography_14_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography14GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-14"],
            ["Climate Classification (Koppen) / India Climatic Regions"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-12", "geography-13"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_climate_classification_boundaries(self) -> None:
        text = session_markdown(generator, "geography-14")
        for phrase in (
            "minus 3 degrees Celsius",
            "climatological normal",
            "no single immutable official Koppen map",
            "TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
        ):
            self.assertIn(phrase, text)

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-14"),
            topic_key="geography-14",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
