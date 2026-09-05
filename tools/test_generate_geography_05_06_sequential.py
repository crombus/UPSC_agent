"""Regression tests for Geography learner-v2 Topics 05-06."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_geography_05_06_sequential as generator
import validate_v2_export as validator
from geography_generator_test_support import assert_batch_contract, session_markdown


class Geography0506GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["geography-05", "geography-06"],
            [
                "Landforms by Running Water / India Drainage and Interlinking",
                "Landforms of Glaciation / Himalayan Glaciers-GLOF",
            ],
        )

    def test_drainage_and_glacier_boundaries(self) -> None:
        drainage = session_markdown(generator, "geography-05")
        glacier = session_markdown(generator, "geography-06")
        for phrase in ("Ken-to-Betwa", "Panna", "Devprayag", "2020 GS-I"):
            self.assertIn(phrase, drainage)
        for phrase in ("equilibrium-line altitude", "fjord", "South Lhonak", "GLOF"):
            self.assertIn(phrase, glacier)

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

    def test_generator_has_no_publish_side_effects(self) -> None:
        source = Path(generator.__file__).read_text(encoding="utf-8")
        for forbidden in (
            "markdown_learning_pdf",
            "finalize_v2_topic",
            "generate_export_command_index",
            "EXPORT-PDF-STATUS.json",
        ):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
