"""Regression tests for Environment and Ecology learner-v2 Topic 17."""

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
import generate_environment_and_ecology_17_sequential as generator


class EnvironmentAndEcology17Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-17"], ["Climate Change Science Greenhouse Effect"])

    def test_climate_science_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-17").casefold()
        for phrase in (
            "natural greenhouse effect", "enhanced anthropogenic forcing",
            "emission-concentration distinction", "stock-flow distinction",
            "forcing-feedback distinction", "weather-climate distinction",
            "detection-attribution distinction", "scenario-not-forecast",
            "mitigation-adaptation distinction", "gross-net",
        ):
            self.assertIn(phrase, text)

    def test_live_figure_and_ar7_honesty(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-17")
        for phrase in ("title-only response", "HTTP 404", "process, not findings", "No temperature"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
