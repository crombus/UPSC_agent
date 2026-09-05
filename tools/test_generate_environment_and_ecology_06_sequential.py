"""Regression tests for Environment and Ecology learner-v2 Topic 06."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_environment_and_ecology_06_sequential as generator
from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class EnvironmentAndEcology06Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-06"],
            ["Protected Area Network India"],
        )

    def test_category_overlay_and_boundary_distinctions(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-06").casefold()
        for phrase in (
            "national park, wildlife sanctuary, conservation reserve and community reserve",
            "tiger reserve is a species-management overlay",
            "eco-sensitive zone is separately notified",
            "no automatic uniform statutory width",
            "notified protected-area boundary",
            "undated displayed count was not adopted",
        ):
            self.assertIn(phrase.casefold(), text)

    def test_mains_pyq_is_carried(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-06")
        self.assertIn("2023 GS-I Q15", text)
        self.assertIn("model answer independently authored", text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
