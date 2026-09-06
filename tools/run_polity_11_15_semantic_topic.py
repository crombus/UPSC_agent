"""Run one sequential Polity semantic review for topics 11-15."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_11_15_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(11, 16)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_11_15_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_11_15_deep_review.py",
        "tools\\test_regenerate_polity_11_15_deep_review.py",
        "tools\\run_polity_11_15_semantic_topic.py",
        "tools\\test_run_polity_11_15_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        11: "11-parliamentary-system",
        12: "12-federal-system",
        13: "13-centre-state-and-inter-state-relations",
        14: "14-emergency-provisions",
        15: "15-president-and-vice-president",
    }
)
runner.PYQ_STATUS.update(
    {
        11: (
            "direct 2024 GS-II Q3 plus routed 2020 and 2021 objective demands; "
            "2018/2023 comparative Mains routes remain explicitly cross-owned"
        ),
        12: (
            "direct/routed 2021 GS-II and objective demands plus 2023 prison-"
            "administration route; unavailable historical keys remain labelled"
        ),
        13: (
            "all eleven direct/supporting 2018-2025 legislative, administrative, "
            "fiscal and inter-State demands retained with official-key discipline"
        ),
        14: (
            "direct 2018 Article 356 objective demand; 2023 detention demand remains "
            "a disclosed supporting route and no direct Mains route is fabricated"
        ),
        15: (
            "direct 2025 GS-II pardon comparison and 2025 objective demands plus "
            "2018/2023 election routes; official and unavailable keys stay distinct"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_11_15_deep_review",
        "test_run_polity_11_15_semantic_topic",
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
        raise ValueError("Polity 11-15 runner accepts only topic numbers 11 through 15.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
