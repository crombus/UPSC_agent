"""Regression tests for Environment and Ecology learner-v2 Topic 13."""

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
import generate_environment_and_ecology_13_sequential as generator


class EnvironmentAndEcology13Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-13"], ["Air Pollution and CPCB Standards"])

    def test_air_standard_and_metric_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-13").casefold()
        for phrase in (
            "ambient-standard boundary", "source-emission standard", "concentration versus exposure",
            "pollutant versus precursor", "aqi category boundary", "source-apportionment boundary",
            "target versus attainment", "non-attainment boundary",
        ):
            self.assertIn(phrase, text)

    def test_live_air_failures_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-13")
        for phrase in ("title-only response", "404 display route", "No AQI breakpoint", "No monitoring value"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
