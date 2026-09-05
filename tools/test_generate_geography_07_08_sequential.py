"""Regression tests for Geography learner-v2 Topics 07-08."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_05_06_sequential as previous
import generate_geography_07_08_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography0708GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-07", "geography-08"],
            [
                "Arid Desert Landforms / Thar Desertification",
                "Limestone and Karst Landforms / India Caves-Meghalayan Age",
            ],
        )

    def test_previous_batch_identity_is_unchanged(self) -> None:
        self.assertEqual(
            ["geography-05", "geography-06"],
            [item["key"] for item in previous.TOPICS],
        )

    def test_desert_and_karst_boundaries(self) -> None:
        desert = session_markdown(generator, "geography-07")
        karst = session_markdown(generator, "geography-08")
        for phrase in ("saltation", "Aravalli", "Indira Gandhi Canal", "UNCCD"):
            self.assertIn(phrase, desert)
        for phrase in ("Mawmluh", "KM-A", "Meghalayan", "Anthropocene"):
            self.assertIn(phrase, karst)
        self.assertIn("TRANSPARENT ZERO-DIRECT-PYQ AUDIT", karst)
        self.assertIn("Ajanta is routed to Indian Art and Culture", karst)

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
