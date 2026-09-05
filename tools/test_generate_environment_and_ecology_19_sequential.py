"""Regression tests for Environment and Ecology learner-v2 Topic 19."""

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
import generate_environment_and_ecology_19_sequential as generator


class EnvironmentAndEcology19Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(self, generator, ["environment-and-ecology-19"], ["UNFCCC COP Kyoto Paris Agreement"])

    def test_treaty_and_obligation_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-19").casefold()
        for phrase in (
            "unfccc convention identity", "cop-cmp-cma boundary",
            "treaty-status sequence", "annex i historical boundary",
            "procedure-ambition distinction", "global stocktake boundary",
            "article 6 architecture", "decision-pledge-delivery distinction",
        ):
            self.assertIn(phrase, text)

    def test_current_outcomes_are_not_inferred(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-19")
        for phrase in ("Incapsula", "not converted into adopted decisions", "No Party count"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
