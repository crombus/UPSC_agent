"""Regression tests for Geography learner-v2 Topics 12-13."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_10_11_sequential as previous
import generate_geography_12_13_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography1213GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-12", "geography-13"],
            [
                "The Oceans: Currents, Tides, Salinity / Indian Ocean and IOD",
                "Weather Elements / India Jet Stream-Western Disturbances",
            ],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-10", "geography-11"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_ocean_and_weather_boundaries(self) -> None:
        ocean = session_markdown(generator, "geography-12")
        weather = session_markdown(generator, "geography-13")
        for phrase in ("North Indian Ocean", "OMNI", "RAMA", "neither phase guarantees"):
            self.assertIn(phrase, ocean)
        for phrase in ("geostrophic", "subtropical westerly jet", "radiosonde", "no sufficiently stable"):
            self.assertIn(phrase, weather)

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
