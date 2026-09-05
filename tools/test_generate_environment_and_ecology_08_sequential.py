"""Regression tests for Environment and Ecology learner-v2 Topic 08."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_environment_and_ecology_08_sequential as generator
from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class EnvironmentAndEcology08Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-08"],
            ["Wildlife Protection Act and Schedules"],
        )

    def test_vintage_schedule_and_authority_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-08").casefold()
        for phrase in (
            "pre-2022 six-schedule structure",
            "post-2022 four-schedule structure",
            "schedule iii is the specified plant schedule",
            "schedule iv covers cites-listed scheduled specimens",
            "baseline is prohibition of hunting",
            "management authority",
            "scientific authority",
            "sections 38y and 38z",
        ):
            self.assertIn(phrase.casefold(), text)

    def test_live_statute_attempts_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-08")
        for phrase in ("India Code returned HTTP 403", "raw or image PDF bytes", "No species schedule"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
