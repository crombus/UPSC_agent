"""Regression tests for Environment and Ecology learner-v2 Topic 05."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_environment_and_ecology_05_sequential as generator
from environment_and_ecology_generator_test_support import (
    assert_batch_contract,
    assert_no_publish_side_effects,
    session_markdown,
)


class EnvironmentAndEcology05Tests(unittest.TestCase):
    def test_complete_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["environment-and-ecology-05"],
            ["IUCN Red List and Endemism"],
        )

    def test_assessment_and_distribution_boundaries(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-05").casefold()
        for phrase in (
            "threatened collectively covers vulnerable, endangered and critically endangered",
            "category and population trend",
            "category and criterion",
            "global and regional or national assessments",
            "endemic, rare and threatened",
            "green status",
            "no current species assessment was imported",
        ):
            self.assertIn(phrase.casefold(), text)

    def test_live_attempts_are_honest(self) -> None:
        text = session_markdown(generator, "environment-and-ecology-05")
        for phrase in ("HTTP 520", "India Code returned HTTP 403", "no current species"):
            self.assertIn(phrase, text)

    def test_no_publish_side_effects(self) -> None:
        assert_no_publish_side_effects(self, generator)


if __name__ == "__main__":
    unittest.main()
