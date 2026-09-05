"""Regression tests for World History learner-v2 Topics 01-02."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_world_history_01_02_sequential as generator
from world_history_generator_test_support import (
    assert_batch_contract,
    session_markdown,
)


class WorldHistory0102GeneratorTests(unittest.TestCase):
    def test_complete_batch_contract(self) -> None:
        assert_batch_contract(
            self,
            generator,
            ["world-history-01", "world-history-02"],
            [
                "Enlightenment and Age of Revolutions Overview",
                "American Revolution",
            ],
        )

    def test_topic01_thinker_dates_and_doctrines_are_preserved(self) -> None:
        text = session_markdown(generator, "world-history-01")
        for phrase in (
            "Locke, 1689",
            "Montesquieu, 1748",
            "Rousseau, 1762",
            "liberalism",
            "conservatism",
            "nationalism",
            "capitalism",
            "socialism",
            "communism",
            "social democracy",
            "Beveridge Report",
        ):
            self.assertIn(phrase, text)
        self.assertNotIn("all Enlightenment thinkers were modern democrats", text)

    def test_topic01_keeps_ideas_crisis_and_mobilisation_together(self) -> None:
        text = session_markdown(generator, "world-history-01")
        self.assertIn("ideas supplied legitimacy", text)
        self.assertIn("crises supplied momentum", text)
        self.assertIn("mobilised groups supplied revolutionary force", text)

    def test_topic02_chronology_and_documents_are_not_conflated(self) -> None:
        text = session_markdown(generator, "world-history-02")
        for phrase in (
            "Stamp Act of 1765",
            "Boston Tea Party of 1773",
            "Lexington and Concord in 1775",
            "4 July 1776",
            "Saratoga",
            "Yorktown in 1781",
            "Treaty of Paris of 1783",
            "Constitution came into effect in 1789",
            "Bill of Rights",
        ):
            self.assertIn(phrase, text)
        self.assertIn(
            "Yorktown in 1781 was the decisive military turning point, "
            "but it did not itself constitute legal recognition",
            text,
        )

    def test_topic02_rights_and_exclusions_are_balanced(self) -> None:
        text = session_markdown(generator, "world-history-02")
        for phrase in ("Slavery survived", "women", "Native Americans", "property"):
            self.assertIn(phrase, text)
        self.assertIn("radical in political form", text)
        self.assertIn("conservative in social settlement", text)

    def test_topic02_verified_2019_demand_is_solved(self) -> None:
        text = session_markdown(generator, "world-history-02")
        self.assertIn("2019", text)
        self.assertIn("foundations of the modern world", text)
        self.assertIn("Verified neutral demand", text)

    def test_america250_is_the_only_direct_live_linkage_in_this_batch(
        self,
    ) -> None:
        topic01, topic02 = generator.TOPICS
        self.assertEqual([], topic01["live_sources"])
        self.assertIn("no verified live item", topic01["current_note"])
        self.assertEqual(["https://america250.org/"], topic02["live_sources"])
        self.assertIn("bipartisan initiative", topic02["current_note"])
        self.assertIn("250th anniversary of the United States", topic02["current_note"])
        self.assertIn("Semiquincentennial year", topic02["current_note"])
        self.assertIn("ongoing educational and history events", topic02["current_note"])
        self.assertIn("no decorative event detail", topic02["current_note"])

        text = session_markdown(generator, "world-history-02")
        self.assertIn("America250", text)
        self.assertIn("founding documents", text)
        record = json.loads(
            (
                generator.EXPORT_DIR
                / "world-history-02-new-topic-2026-09-01.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(["https://america250.org/"], record["live_sources"])
        self.assertEqual(topic02["current_note"], record["current_linkage_note"])


if __name__ == "__main__":
    unittest.main()
