"""Regression tests for Environment and Ecology learner-v2 Topic 20."""

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
import generate_environment_and_ecology_20_sequential as generator


class EnvironmentAndEcology20Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-20"], ["India Climate Policy NAPCC Panchamrit LTLEDS"])

    def test_india_policy_instrument_and_metric_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-20").casefold()
        for phrase in (
            "original eight missions", "panchamrit status",
            "updated ndc quantified terms", "panchamrit-ndc boundary",
            "lt-leds identity", "intensity-absolute distinction",
            "capacity-generation-energy distinction", "bur-ndc-ltleds distinction",
        ):
            self.assertIn(phrase, text)

    def test_conflicting_current_status_is_not_guessed(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-20")
        for phrase in ("conflicted on India's post-2022 NDC status", "raw bytes", "asserts no new NDC"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
