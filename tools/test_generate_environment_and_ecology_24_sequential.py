"""Regression tests for Environment and Ecology learner-v2 Topic 24."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)
import generate_environment_and_ecology_24_sequential as generator


class EnvironmentAndEcology24Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-24"], ["Coastal and Marine Ecology CRZ Blue Economy"])

    def test_ecosystem_crz_iczm_and_blue_economy_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-24").casefold()
        for phrase in (
            "coastal-system boundary", "coral stress distinction",
            "notification-vintage boundary", "crz category boundary",
            "czmp evidence boundary", "classification-clearance distinction",
            "iczm-clearance distinction", "seawater-intrusion chain",
            "blue-economy definition", "sector-outcome boundary",
        ):
            self.assertIn(phrase, text)

    def test_current_coastal_metrics_and_clearances_not_invented(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-24")
        for phrase in ("no coastline", "CRZ category or clearance status", "Blue Economy output", "project outcome"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
