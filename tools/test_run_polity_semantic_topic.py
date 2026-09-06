"""Tests for the strictly sequential Polity semantic driver."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import regenerate_polity_26_30_deep_review as deep
import run_polity_semantic_topic as runner


class PolitySemanticTopicRunnerTests(unittest.TestCase):
    def test_authoritative_queue_stays_sequential_with_one_active_topic(self) -> None:
        state = json.loads(runner.SEMANTIC_STATUS.read_text(encoding="utf-8"))
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

    def test_driver_uses_topics_26_30_configuration(self) -> None:
        self.assertEqual(set(range(26, 31)), set(runner.TOPIC_CHOICES))
        self.assertEqual(set(range(26, 31)), set(runner.SLUGS))
        self.assertEqual(set(range(26, 31)), set(runner.PYQ_STATUS))
        self.assertEqual("2026-09-05", runner.REPORT_DATE)
        self.assertEqual("2026-09-05", deep.DATE)

    def test_reports_and_inventories_use_requested_date(self) -> None:
        source = Path(runner.__file__).read_text(encoding="utf-8")
        self.assertIn("semantic-validation-{REPORT_DATE}", source)
        self.assertIn("semantic-completeness-", source)
        self.assertIn("5 September 2026", source)


if __name__ == "__main__":
    unittest.main()
