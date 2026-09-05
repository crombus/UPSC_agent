"""Regression tests for Environment and Ecology learner-v2 Topic 10."""

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
import generate_environment_and_ecology_10_sequential as generator


class EnvironmentAndEcology10Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-10"],
            ["CMS Bonn Convention Migratory Species"],
        )

    def test_migration_and_instrument_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-10").casefold()
        for phrase in (
            "cyclically and predictably",
            "range state definition",
            "appendix i",
            "appendix ii",
            "dual listing",
            "agreement versus mou",
            "action plan boundary",
            "concerted action boundary",
            "coordinating unit in india",
            "adoption establishes targets and direction",
        ):
            self.assertIn(phrase, text)

    def test_provisional_amur_falcon_pyq_is_answer_free(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-10")
        for phrase in ("Amur Falcon", "Doyang Lake", "provisional answer key is not recorded or inferred"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
