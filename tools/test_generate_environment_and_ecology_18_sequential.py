"""Regression tests for Environment and Ecology learner-v2 Topic 18."""

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
import generate_environment_and_ecology_18_sequential as generator


class EnvironmentAndEcology18Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-18"], ["IPCC Assessment Reports"])

    def test_ipcc_architecture_and_calibration(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-18").casefold()
        for phrase in (
            "assess-not-research mandate", "working group i", "working group ii",
            "working group iii", "tfi boundary", "synthesis report",
            "approval-acceptance distinction", "confidence-likelihood distinction",
            "scenario-not-forecast", "ar6-ar7 status",
        ):
            self.assertIn(phrase, text)

    def test_ar7_process_is_not_finding(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-18").casefold()
        for phrase in ("planned products were not treated as published findings", "thin response", "cycle in progress"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
