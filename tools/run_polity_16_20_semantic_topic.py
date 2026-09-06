"""Run one sequential Polity semantic review for topics 16-20."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_16_20_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(16, 21)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_16_20_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_16_20_deep_review.py",
        "tools\\test_regenerate_polity_16_20_deep_review.py",
        "tools\\run_polity_16_20_semantic_topic.py",
        "tools\\test_run_polity_16_20_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        16: "16-prime-minister-and-council-of-ministers",
        17: "17-parliament",
        18: "18-supreme-court",
        19: "19-governor-cm-and-state-council",
        20: "20-state-legislature",
    }
)
runner.PYQ_STATUS.update(
    {
        16: (
            "direct 2020/2022 objective demands plus the routed 2024 cabinet-"
            "system Mains demand; adjacent parliamentary-system ownership stays labelled"
        ),
        17: (
            "all direct/routed 2018-2025 committee, Speaker, Rajya Sabha, "
            "accountability, finance, privilege and representation demands retained"
        ),
        18: (
            "all direct/routed 2019-2025 jurisdiction, collegium, independence, "
            "PIL, environment and accountability demands retained"
        ),
        19: (
            "direct 2022 ordinance Mains demand plus routed 2018-2025 Governor, "
            "assent, defection and federal-neutrality demands retained"
        ),
        20: (
            "direct 2021 Council and 2023 presiding-officer Mains demands plus "
            "routed 2018-2025 procedure, Bill and assent demands retained"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_16_20_deep_review",
        "test_run_polity_16_20_semantic_topic",
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
        raise ValueError("Polity 16-20 runner accepts only topic numbers 16 through 20.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

