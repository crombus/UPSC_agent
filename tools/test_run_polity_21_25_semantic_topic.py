"""Tests for the sequential Polity 21-25 semantic driver."""

from __future__ import annotations

import json
import unittest

import run_polity_21_25_semantic_topic as runner


class Polity2125SemanticTopicRunnerTests(unittest.TestCase):
    def test_driver_is_bounded_to_topics_21_25(self) -> None:
        self.assertEqual(set(range(21, 26)), set(runner.runner.TOPIC_CHOICES))
        self.assertTrue(set(range(21, 26)).issubset(runner.runner.SLUGS))
        self.assertTrue(set(range(21, 26)).issubset(runner.runner.PYQ_STATUS))

    def test_authoritative_queue_remains_sequential(self) -> None:
        state = json.loads(
            runner.runner.SEMANTIC_STATUS.read_text(encoding="utf-8")
        )
        next_key = state["next_topic"]["topic_key"]
        self.assertIn(next_key, {f"polity-{number:02d}" for number in range(21, 27)})
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
        self.assertTrue(set(active).issubset({next_key}))


if __name__ == "__main__":
    unittest.main()
