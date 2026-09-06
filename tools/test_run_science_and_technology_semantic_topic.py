"""Tests for the strictly sequential Science and Technology semantic driver."""

from __future__ import annotations

import json
import unittest

import run_science_and_technology_semantic_topic as subject


class ScienceSemanticTopicRunnerTests(unittest.TestCase):
    def test_authoritative_queue_has_at_most_one_active_topic(self) -> None:
        state = json.loads(
            subject.runner.SEMANTIC_STATUS.read_text(encoding="utf-8")
        )
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

    def test_driver_uses_complete_authoritative_catalogue(self) -> None:
        self.assertEqual(set(range(1, 27)), set(subject.runner.TOPIC_CHOICES))
        self.assertEqual(
            [f"science-and-technology-{number:02d}" for number in range(1, 27)],
            [topic.topic_key for topic in subject.deep.topics()],
        )
        self.assertEqual("2026-09-06", subject.REPORT_DATE)
        self.assertEqual("2026-09-06", subject.deep.DATE)

    def test_live_audit_covers_every_topic(self) -> None:
        payload = subject.runner.load(subject.LIVE_AUDIT)
        self.assertEqual("passed", payload["result"])
        self.assertEqual(26, len(payload["topics"]))
        for row in payload["topics"]:
            self.assertGreaterEqual(row["attempted"], 3)
            self.assertGreaterEqual(row["substantive_retrievals"], 1)
            self.assertEqual("2026-09-06", row["access_date"])

    def test_topic_configs_and_pyq_notes_are_complete(self) -> None:
        self.assertEqual(set(range(1, 27)), set(subject.CONFIGS))
        self.assertEqual(set(range(1, 27)), set(subject.runner.PYQ_STATUS))
        self.assertTrue(all(subject.runner.PYQ_STATUS.values()))


if __name__ == "__main__":
    unittest.main()
