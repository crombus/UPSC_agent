"""Regression tests for Environment and Ecology learner-v2 Topic 09."""

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
import generate_environment_and_ecology_09_sequential as generator


class EnvironmentAndEcology09Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self, generator, ["environment-and-ecology-09"], ["CITES and Wildlife Trade"]
        )

    def test_trade_permit_and_status_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-09").casefold()
        for phrase in (
            "international trade in listed wild fauna and flora",
            "appendix i",
            "appendix ii",
            "appendix iii",
            "listing versus trade ban",
            "specimen discipline",
            "source discipline",
            "non-detriment finding",
            "management authority",
            "scientific authority",
            "zero-direct-pyq",
        ):
            self.assertIn(phrase, text)

    def test_failed_cites_pages_are_recorded(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-09")
        for phrase in ("cites.org/eng/disc/how.php", "returned HTTP 403", "No current Party count"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
