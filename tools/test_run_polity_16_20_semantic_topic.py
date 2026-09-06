"""Tests for the sequential Polity 16-20 semantic driver."""

from __future__ import annotations

import json
import unittest

import run_polity_16_20_semantic_topic as runner


class Polity1620SemanticTopicRunnerTests(unittest.TestCase):
    def test_driver_is_bounded_to_topics_16_20(self) -> None:
        self.assertEqual(set(range(16, 21)), set(runner.runner.TOPIC_CHOICES))
        self.assertTrue(set(range(16, 21)).issubset(runner.runner.SLUGS))
        self.assertTrue(set(range(16, 21)).issubset(runner.runner.PYQ_STATUS))

    def test_authoritative_queue_remains_sequential(self) -> None:
        state = json.loads(
            runner.runner.SEMANTIC_STATUS.read_text(encoding="utf-8")
        )
        next_key = state["next_topic"]["topic_key"]
        self.assertIn(next_key, {f"polity-{number:02d}" for number in range(16, 22)})
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
