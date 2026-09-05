"""Regression tests for Geography learner-v2 Topic 24."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_23_sequential as previous
import generate_geography_24_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography24GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-24"],
            ["Cool Temperate Eastern Margin Laurentian"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-23"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_laurentian_boundaries(self) -> None:
        text = session_markdown(generator, "geography-24")
        for phrase in ("Laurentian", "Oyashio", "Grand Banks", "Darjeeling"):
            self.assertIn(phrase, text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-24"),
            topic_key="geography-24",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
