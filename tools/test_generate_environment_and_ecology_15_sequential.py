"""Regression tests for Environment and Ecology learner-v2 Topic 15."""

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
import generate_environment_and_ecology_15_sequential as generator


class EnvironmentAndEcology15Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-15"], ["Solid Plastic and E-Waste Rules"])

    def test_stream_actor_epr_and_vintage_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-15").casefold()
        for phrase in (
            "separate waste streams", "rule-vintage discipline", "plastic actor map",
            "item ban and packaging epr", "epr obligation boundary", "certificate and throughput",
            "e-waste actor map", "legacy stock versus new flow",
        ):
            self.assertIn(phrase, text)

    def test_live_waste_failures_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-15")
        for phrase in ("separate solid-waste", "Centralized EPR Portal", "title-only", "transport level"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
