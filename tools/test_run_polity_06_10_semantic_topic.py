"""Tests for the sequential Polity 06-10 semantic driver."""

from __future__ import annotations

import json
import unittest

import run_polity_06_10_semantic_topic as runner


class Polity0610SemanticTopicRunnerTests(unittest.TestCase):
    def test_driver_is_bounded_to_topics_06_10(self) -> None:
        self.assertEqual(set(range(6, 11)), set(runner.runner.TOPIC_CHOICES))
        self.assertTrue(set(range(6, 11)).issubset(runner.runner.SLUGS))
        self.assertTrue(set(range(6, 11)).issubset(runner.runner.PYQ_STATUS))

    def test_queue_advanced_to_topic_11(self) -> None:
        state = json.loads(
            runner.runner.SEMANTIC_STATUS.read_text(encoding="utf-8")
        )
        self.assertEqual("polity-11", state["next_topic"]["topic_key"])
        active = [
            row["topic_key"]
            for row in state["topics"]
            if row["status"]
            in {
                "in_progress",
                "changes_required",
                "repair_in_progress",
                "revalidation_pending",
                "blocked",
            }
        ]
        self.assertEqual([], active)


if __name__ == "__main__":
    unittest.main()
