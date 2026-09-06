"""Tests for the strictly sequential Environment and Ecology semantic driver."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

import run_environment_and_ecology_semantic_topic as subject


class EnvironmentSemanticTopicRunnerTests(unittest.TestCase):
    def test_authoritative_queue_has_at_most_one_active_topic(self) -> None:
        state = json.loads(subject.runner.SEMANTIC_STATUS.read_text(encoding="utf-8"))
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

    def test_driver_uses_complete_environment_catalogue(self) -> None:
        self.assertEqual(set(range(1, 29)), set(subject.runner.TOPIC_CHOICES))
        self.assertEqual(
            [f"environment-and-ecology-{number:02d}" for number in range(1, 29)],
            [topic.topic_key for topic in subject.deep.topics()],
        )
        self.assertEqual("2026-09-06", subject.REPORT_DATE)
        self.assertEqual("2026-09-06", subject.deep.DATE)

    def test_live_sources_cover_every_topic(self) -> None:
        self.assertEqual(set(range(1, 29)), set(subject.LIVE_OFFICIAL_SOURCES))
        for sources, note in subject.LIVE_OFFICIAL_SOURCES.values():
            self.assertGreaterEqual(len(sources), 4)
            self.assertIn("6 September 2026", note)

    def test_reports_and_inventories_use_requested_date(self) -> None:
        source = Path(subject.runner.__file__).read_text(encoding="utf-8")
        wrapper = Path(subject.__file__).read_text(encoding="utf-8")
        runtime = Path(subject.__file__).with_name("environment_semantic_runtime.py")
        self.assertIn("semantic-validation-{REPORT_DATE}", source)
        self.assertIn("Environment and Ecology Semantic-Completeness Review", wrapper)
        self.assertIn("2026-09-06", runtime.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
