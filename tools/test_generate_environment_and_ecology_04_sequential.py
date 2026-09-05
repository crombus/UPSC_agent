"""Regression tests for Environment and Ecology learner-v2 Topic 04."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_environment_and_ecology_04_sequential as generator
from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
)


class EnvironmentAndEcology04Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-04"],
            ["Biodiversity Levels and Hotspots"],
        )

    def test_level_and_status_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-04").casefold()
        for phrase in (
            "genetic diversity",
            "species diversity",
            "ecosystem diversity",
            "alpha diversity",
            "beta diversity",
            "gamma diversity",
            "native species",
            "endemic species",
            "1,500 endemic vascular plant species",
            "30 per cent or less",
            "scientific prioritisation framework",
        ):
            self.assertIn(phrase.casefold(), text)

    def test_live_attempts_are_honest(self) -> None:
        assert_live_source_honesty(self, generator, "environment-and-ecology-04")

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
