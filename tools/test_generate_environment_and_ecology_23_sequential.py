"""Regression tests for Environment and Ecology learner-v2 Topic 23."""

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
import generate_environment_and_ecology_23_sequential as generator


class EnvironmentAndEcology23Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-23"], ["Desertification UNCCD and Land Degradation"])

    def test_dryland_ldn_drought_and_quality_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-23").casefold()
        for phrase in (
            "land-degradation umbrella", "desertification dryland boundary",
            "drought-risk components", "ldn baseline boundary",
            "avoid-reduce-reverse hierarchy", "neutrality-not-zero boundary",
            "remote-ground integration", "restoration-quality boundary",
            "rangeland and open-ecosystem boundary",
        ):
            self.assertIn(phrase, text)

    def test_current_land_and_drought_metrics_not_invented(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-23")
        for phrase in ("No degradation extent", "restored area", "drought trend", "COP outcome"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
