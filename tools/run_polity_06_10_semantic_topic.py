"""Run one sequential Polity semantic review for topics 06-10."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_06_10_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(6, 11)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_06_10_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_06_10_deep_review.py",
        "tools\\test_regenerate_polity_06_10_deep_review.py",
        "tools\\run_polity_06_10_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        6: "06-citizenship",
        7: "07-fundamental-rights",
        8: "08-directive-principles",
        9: "09-fundamental-duties",
        10: "10-amendment-and-basic-structure",
    }
)
runner.PYQ_STATUS.update(
    {
        6: (
            "direct 2021 Prelims Q89; 2018 Aadhaar proof retained only as a "
            "cross-topic route; no direct Mains route fabricated"
        ),
        7: (
            "all routed 2018-2026 Prelims/Mains demands preserved with official, "
            "provisional and unavailable-key labels unchanged"
        ),
        8: (
            "direct 2023 GS-II Q2 plus routed 2020, 2021 and 2025 objective "
            "demands; historical unavailable keys remain explicitly inferred"
        ),
        9: (
            "no direct route fabricated; 2020 and 2025 items remain disclosed "
            "supporting cross-topic PYQs"
        ),
        10: (
            "direct 2019 and 2025 GS-II demands plus eight routed objective "
            "questions; official and unavailable-key status remains explicit"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_06_10_deep_review",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in runner.EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    tests = [deep.run_unittest(module) for module in modules]
    if any(item["exit_code"] or item["failures"] or item["errors"] for item in tests):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


runner.run_tests = run_tests


def run(topic_number: int) -> dict[str, object]:
    if topic_number not in runner.TOPIC_CHOICES:
        raise ValueError("Polity 06-10 runner accepts only topic numbers 6 through 10.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
