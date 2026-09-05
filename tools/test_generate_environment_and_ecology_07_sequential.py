"""Regression tests for Environment and Ecology learner-v2 Topic 07."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_environment_and_ecology_07_sequential as generator
from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class EnvironmentAndEcology07Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-07"],
            ["Biosphere Reserves and Ramsar Sites"],
        )

    def test_designation_and_status_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-07").casefold()
        for phrase in (
            "national status is distinct from unesco world network recognition",
            "core zone",
            "buffer zone",
            "transition zone",
            "international designation does not itself create a new indian statutory land category",
            "montreux record",
            "no latest count or area was asserted",
        ):
            self.assertIn(phrase.casefold(), text)

    def test_mains_pyqs_are_carried(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-07")
        for phrase in ("2018 GS-III Q7", "2021 GS-I Q6", "2023 GS-III Q17"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
