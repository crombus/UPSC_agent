"""Regression tests for Geography learner-v2 Topics 15-16."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_14_sequential as previous
import generate_geography_15_16_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography1516GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-15", "geography-16"],
            ["Hot Wet Equatorial Climate", "Tropical Monsoon and Marine Climate"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(["geography-14"], [item["key"] for item in previous.TOPICS])

    def test_equatorial_and_monsoon_boundaries(self) -> None:
        equatorial = session_markdown(generator, "geography-15")
        monsoon = session_markdown(generator, "geography-16")
        for phrase in ("diurnal temperature range exceeds", "nutrient capital", "India has no extensive true equatorial Af zone"):
            self.assertIn(phrase, equatorial)
        for phrase in ("complete seasonal reversal", "Arabian Sea branch", "Purvaiya", "provisional"):
            self.assertIn(phrase, monsoon)

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
