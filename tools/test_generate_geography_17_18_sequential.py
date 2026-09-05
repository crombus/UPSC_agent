"""Regression tests for Geography learner-v2 Topics 17-18."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_15_16_sequential as previous
import generate_geography_17_18_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography1718GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-17", "geography-18"],
            ["Savanna Sudan Climate", "Hot and MidLatitude Desert Climate"],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-15", "geography-16"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_savanna_and_desert_boundaries(self) -> None:
        savanna = session_markdown(generator, "geography-17")
        desert = session_markdown(generator, "geography-18")
        for phrase in ("fire and grazing", "Banni", "Aravalli Green Wall", "2021 Prelims GS-I"):
            self.assertIn(phrase, savanna)
        for phrase in ("aridity, not heat", "Benguela", "Great Indian Bustard", "no direct question"):
            self.assertIn(phrase, desert)

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
