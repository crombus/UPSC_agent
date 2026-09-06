"""Tests for the strictly sequential Polity 51-55 semantic driver."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import regenerate_polity_51_55_deep_review as deep
import run_polity_51_55_semantic_topic as runner


class Polity5155SemanticTopicRunnerTests(unittest.TestCase):
    def test_authoritative_queue_stays_sequential_with_one_active_topic(self) -> None:
        state = json.loads(runner.runner.SEMANTIC_STATUS.read_text(encoding="utf-8"))
        next_key = state["next_topic"]["topic_key"]
        self.assertEqual(next_key, state["active_subject"]["next_topic_key"])
        active = [
            row["topic_key"]
            for row in state["topics"]
            if row["status"]
            in {
                "in_progress",
                "changes_required",
                "repair_in_progress",
                "revalidation_pending",
            }
        ]
        self.assertTrue(set(active).issubset({next_key}))

    def test_driver_uses_topics_51_55_configuration(self) -> None:
        self.assertEqual(set(range(51, 56)), set(runner.runner.TOPIC_CHOICES))
        self.assertTrue(set(range(51, 56)).issubset(runner.runner.SLUGS))
        self.assertTrue(set(range(51, 56)).issubset(runner.runner.PYQ_STATUS))
        self.assertEqual("2026-09-05", runner.runner.REPORT_DATE)
        self.assertEqual("2026-09-05", deep.DATE)

    def test_reports_and_inventories_use_requested_date(self) -> None:
        source = Path(runner.runner.__file__).read_text(encoding="utf-8")
        self.assertIn("semantic-validation-{REPORT_DATE}", source)
        self.assertIn("semantic-completeness-", source)
        self.assertIn("5 September 2026", source)


if __name__ == "__main__":
    unittest.main()
