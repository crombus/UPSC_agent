"""Tests for the strictly sequential SocialJustice semantic driver."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import regenerate_social_justice_deep_review as deep
import run_social_justice_semantic_topic as subject


class SocialJusticeSemanticTopicRunnerTests(unittest.TestCase):
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

    def test_driver_uses_complete_social_justice_catalogue(self) -> None:
        self.assertEqual(set(range(1, 18)), set(subject.runner.TOPIC_CHOICES))
        self.assertEqual(
            [f"social-justice-{number:02d}" for number in range(1, 18)],
            [topic.topic_key for topic in deep.topics()],
        )
        self.assertEqual("2026-09-06", subject.REPORT_DATE)
        self.assertEqual("2026-09-06", deep.DATE)

    def test_live_sources_and_canonical_controls_cover_every_topic(self) -> None:
        self.assertEqual(set(range(1, 18)), set(deep.LIVE_OFFICIAL_SOURCES))
        self.assertEqual(set(range(1, 18)), set(deep.CANONICAL_OWNER_CONTROLS))
        for number, control in deep.CANONICAL_OWNER_CONTROLS.items():
            self.assertIn("Four-ledger hostile audit", control)
            self.assertIn("Verified PYQ ownership", control)
            self.assertIn("6 September 2026", control)
            self.assertTrue(deep.LIVE_OFFICIAL_SOURCES[number][0])

    def test_reports_and_inventories_use_requested_date(self) -> None:
        source = Path(subject.runner.__file__).read_text(encoding="utf-8")
        self.assertIn("semantic-validation-{REPORT_DATE}", source)
        wrapper = Path(subject.__file__).read_text(encoding="utf-8")
        self.assertIn("Social Justice Semantic-Completeness Review", wrapper)
        self.assertIn("2026-09-06", wrapper)


if __name__ == "__main__":
    unittest.main()


