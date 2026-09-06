"""Run one sequential Polity semantic review for topics 21-25."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_21_25_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(21, 26)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_21_25_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_21_25_deep_review.py",
        "tools\\test_regenerate_polity_21_25_deep_review.py",
        "tools\\run_polity_21_25_semantic_topic.py",
        "tools\\test_run_polity_21_25_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        21: "21-high-court-and-subordinate-courts",
        22: "22-special-provisions",
        23: "23-panchayati-raj",
        24: "24-municipalities",
        25: "25-union-territories",
    }
)
runner.PYQ_STATUS.update(
    {
        21: (
            "four supporting 2019-2025 High Court, tribunal, Lok Adalat and "
            "collegium routes retained; no direct route fabricated"
        ),
        22: (
            "one direct and four supporting Article 370/371, federalism and "
            "North-East institutional routes retained with ownership boundaries"
        ),
        23: (
            "direct 2018 non-grant finance and 2025 intermediate-tier demands "
            "plus routed women, three-F and local-body merger demands retained"
        ),
        24: (
            "direct 2023 municipal empowerment and routed 2024 rural-urban "
            "merger demand retained with Part IXA ownership"
        ),
        25: (
            "direct 2018 Delhi LG and 2025 J&K Assembly demands retained; "
            "Article 370 doctrine remains cross-owned by Topic 22"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_21_25_deep_review",
        "test_run_polity_21_25_semantic_topic",
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
        raise ValueError("Polity 21-25 runner accepts only topic numbers 21 through 25.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
