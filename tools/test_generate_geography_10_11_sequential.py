"""Regression tests for Geography learner-v2 Topics 10-11."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_09_sequential as previous
import generate_geography_10_11_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography1011GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-10", "geography-11"],
            [
                "Coastal Landforms / India Coast and CRZ",
                "Islands and Coral Reefs / India Islands-Great Nicobar",
            ],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(["geography-09"], [item["key"] for item in previous.TOPICS])

    def test_coast_and_island_boundaries(self) -> None:
        coast = session_markdown(generator, "geography-10")
        islands = session_markdown(generator, "geography-11")
        for phrase in ("wave refraction", "1990-2018", "CRZ Notification 2019", "recommendation is not final approval"):
            self.assertIn(phrase, coast)
        for phrase in ("zooxanthellae", "Ten Degree Channel", "12 February 2026", "Stage-II"):
            self.assertIn(phrase, islands)

    def test_sources_pass_deep_semantic_audit(self) -> None:
        for config in generator.TOPICS:
            audit = validator.deep_content_quality_audit_text(
                session_markdown(generator, str(config["key"])),
                topic_key=str(config["key"]),
            )
            high = [
                defect
                for defect in audit["defects"]
                if defect.get("severity") in {"blocker", "high"}
            ]
            self.assertEqual([], high, str(config["key"]))


if __name__ == "__main__":
    unittest.main()
