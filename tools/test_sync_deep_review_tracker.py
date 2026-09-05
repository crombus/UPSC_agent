"""Targeted tests for safe deep-review tracker check mode."""

from __future__ import annotations

import unittest

import sync_deep_review_tracker as sync


def export_record(key: str, generation: int = 1) -> dict[str, object]:
    return {
        "topic_key": key,
        "variant": "learner-v2",
        "generation": generation,
        "record_id": f"{key}:learner-v2:g{generation}",
    }


def master_row(key: str, generation: int = 1) -> dict[str, object]:
    return {
        "topic_key": key,
        "source_generation": generation,
        "source_record_id": f"{key}:learner-v2:g{generation}",
    }


def review_row(
    key: str,
    generation: int = 1,
    status: str = "pending",
) -> dict[str, object]:
    return {
        **master_row(key, generation),
        "status": status,
    }


class DeepReviewTrackerCheckTests(unittest.TestCase):
    def test_matching_trackers_pass(self) -> None:
        status = {"exports": [export_record("topic-01")]}
        master = {"topic_count": 1, "topics": [master_row("topic-01")]}
        review = {
            "topic_count": 1,
            "topics": [review_row("topic-01")],
            "summary": {"pending": 1},
        }
        errors, latest = sync.tracker_check_errors(status, master, review)
        self.assertEqual([], errors)
        self.assertEqual({"topic-01"}, set(latest))

    def test_key_set_mismatch_is_reported_without_key_error(self) -> None:
        status = {
            "exports": [
                export_record("topic-01"),
                export_record("topic-02"),
            ]
        }
        master = {"topic_count": 1, "topics": [master_row("topic-01")]}
        review = {
            "topic_count": 2,
            "topics": [
                review_row("topic-01"),
                review_row("orphan-topic"),
            ],
            "summary": {"pending": 2},
        }
        errors, _ = sync.tracker_check_errors(status, master, review)
        self.assertIn("MASTER is missing topic keys: topic-02.", errors)
        self.assertIn("REVIEW is missing topic keys: topic-02.", errors)
        self.assertIn(
            "REVIEW has unexpected topic keys: orphan-topic.",
            errors,
        )

    def test_summary_counts_are_compared_by_value(self) -> None:
        status = {"exports": [export_record("topic-01")]}
        master = {"topic_count": 1, "topics": [master_row("topic-01")]}
        review = {
            "topic_count": 1,
            "topics": [review_row("topic-01")],
            "summary": {"pending": 2},
        }
        errors, _ = sync.tracker_check_errors(status, master, review)
        self.assertIn("REVIEW summary differs from topic states.", errors)

    def test_sync_scope_may_ignore_unpublished_export_keys(self) -> None:
        status = {
            "exports": [
                export_record("published-topic"),
                export_record("unpublished-topic"),
            ]
        }
        latest, ignored = sync.latest_exports_for_master(
            status,
            [master_row("published-topic")],
        )
        self.assertEqual({"published-topic"}, set(latest))
        self.assertEqual(["unpublished-topic"], ignored)


if __name__ == "__main__":
    unittest.main()
