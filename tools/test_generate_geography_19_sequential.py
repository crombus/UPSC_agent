"""Regression tests for Geography learner-v2 Topic 19."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_17_18_sequential as previous
import generate_geography_19_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography19GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-19"],
            ["Mediterranean Climate"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-17", "geography-18"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_mediterranean_boundaries(self) -> None:
        text = session_markdown(generator, "geography-19")
        for phrase in ("summer drought and winter rain", "Sirocco", "chilling", "India has no extensive classic Mediterranean"):
            self.assertIn(phrase, text)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", text)

    def test_source_passes_deep_semantic_audit(self) -> None:
        audit = validator.deep_content_quality_audit_text(
            session_markdown(generator, "geography-19"),
            topic_key="geography-19",
        )
        high = [
            defect
            for defect in audit["defects"]
            if defect.get("severity") in {"blocker", "high"}
        ]
        self.assertEqual([], high)


if __name__ == "__main__":
    unittest.main()
