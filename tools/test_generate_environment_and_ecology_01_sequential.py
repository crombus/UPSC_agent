"""Regression tests for Environment and Ecology learner-v2 Topic 01."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_environment_and_ecology_01_sequential as generator
from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_live_source_honesty,
    assert_no_publish_side_effects,
    session_markdown,
)


class EnvironmentAndEcology01Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-01"],
            ["Ecosystem Structure and Function"],
        )

    def test_precision_vocabulary(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-01")
        for phrase in (
            "system boundary",
            "gross primary productivity",
            "net primary productivity",
            "standing crop",
            "standing state",
            "food chain",
            "food web",
            "stability",
            "resilience",
            "carrying capacity",
        ):
            self.assertIn(phrase, text)

    def test_direct_pyq_is_in_basic_and_practice(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-01")
        basic = text.split("## BASIC LEARNING SESSION", 1)[1].split(
            "## BASIC MCQS / REMEDIATION", 1
        )[0]
        practice = text.split("## PYQS AND ANSWER PRACTICE", 1)[1].split(
            "## OPTIONAL ADVANCED DEPTH", 1
        )[0]
        self.assertIn("carrying capacity", basic)
        self.assertIn("2019", practice)
        self.assertIn("PYQ DEMAND CARD", practice)

    def test_live_attempts_are_honest(self) -> None:
        assert_live_source_honesty(self, generator, "environment-and-ecology-01")

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
