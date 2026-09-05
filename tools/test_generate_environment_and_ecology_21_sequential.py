"""Regression tests for Environment and Ecology learner-v2 Topic 21."""

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
import generate_environment_and_ecology_21_sequential as generator


class EnvironmentAndEcology21Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-21"], ["Carbon Markets CCUS and Direct Air Capture"])

    def test_market_capture_and_removal_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-21").casefold()
        for phrase in (
            "allowance-credit distinction", "baseline-and-credit boundary",
            "avoidance-reduction-removal", "issuance-transfer-retirement",
            "corresponding adjustment", "ccus chain", "permanence and leakage",
            "dac versus point-source ccus", "residual-emissions role",
        ):
            self.assertIn(phrase, text)

    def test_no_unsupported_live_metrics(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-21")
        for phrase in ("no current carbon price", "capture rate", "storage capacity", "DAC deployment"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
