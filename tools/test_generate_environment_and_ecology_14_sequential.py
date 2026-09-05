"""Regression tests for Environment and Ecology learner-v2 Topic 14."""

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
import generate_environment_and_ecology_14_sequential as generator


class EnvironmentAndEcology14Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-14"], ["Water Pollution and River Cleaning Missions"])

    def test_water_standard_capacity_and_outcome_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-14").casefold()
        for phrase in (
            "water-quality and effluent boundary", "water class and discharge boundary",
            "sewage quantity chain", "capacity and utilisation", "stp etp and cetp",
            "input output outcome chain", "stretch season indicator", "dilution",
        ):
            self.assertIn(phrase, text)

    def test_live_water_failures_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-14")
        for phrase in ("title 'Status Reports'", "raw PDF bytes", "WATER QUALITY DATA (YEARLY)", "No river-quality value"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
