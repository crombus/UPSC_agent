"""Tests for the sequential Political Theory semantic driver."""

from __future__ import annotations

import json
import unittest

import run_political_theory_semantic_topic as subject


class PoliticalTheorySemanticTopicRunnerTests(unittest.TestCase):
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

    def test_driver_uses_complete_catalogue(self) -> None:
        self.assertEqual(set(range(1, 24)), set(subject.runner.TOPIC_CHOICES))
        self.assertEqual(
            [f"political-theory-{number:02d}" for number in range(1, 24)],
            [topic.topic_key for topic in subject.deep.topics()],
        )
        self.assertEqual("2026-09-06", subject.REPORT_DATE)
        self.assertEqual("2026-09-06", subject.deep.DATE)

    def test_source_audit_covers_every_topic(self) -> None:
        payload = subject.runner.load(subject.LIVE_AUDIT)
        self.assertEqual("passed", payload["result"])
        self.assertEqual(23, len(payload["topics"]))
        for row in payload["topics"]:
            self.assertGreaterEqual(row["attempted"], 2)
            self.assertGreaterEqual(row["substantive_retrievals"], 2)
            self.assertEqual("2026-09-06", row["access_date"])
            self.assertTrue(row["verification_scope"])

    def test_canonical_owners_pass_hostile_markers(self) -> None:
        for topic in subject.deep.topics():
            with self.subTest(topic=topic.topic_key):
                self.assertFalse(subject.deep.ensure_canonical_owner_control(topic))

    def test_pyq_boundaries_cover_every_topic(self) -> None:
        self.assertEqual(set(range(1, 24)), set(subject.runner.PYQ_STATUS))
        self.assertTrue(all(subject.runner.PYQ_STATUS.values()))


if __name__ == "__main__":
    unittest.main()
