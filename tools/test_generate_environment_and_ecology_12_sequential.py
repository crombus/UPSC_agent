"""Regression tests for Environment and Ecology learner-v2 Topic 12."""

from __future__ import annotations

import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)
import generate_environment_and_ecology_12_sequential as generator


class EnvironmentAndEcology12Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-12"],
            ["Forest Governance CAMPA and Green India Mission"],
        )

    def test_fund_authority_and_metric_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-12").casefold()
        for phrase in (
            "diversion approval first",
            "net present value",
            "national authority boundary",
            "state authority boundary",
            "accrual",
            "expenditure",
            "ecological outcome",
            "green india mission",
            "these are targets, not verified achievements",
            "green credit",
        ):
            self.assertIn(phrase, text)

    def test_live_fund_failures_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-12")
        for phrase in ("moef.gov.in/campa", "HTTP 404", "host could not be resolved", "contact-only stub"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
