"""Run one sequential Polity semantic review for topics 31-35."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_31_35_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(31, 36)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_31_35_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_31_35_deep_review.py",
        "tools\\test_regenerate_polity_31_35_deep_review.py",
        "tools\\run_polity_31_35_semantic_topic.py",
        "tools\\test_run_polity_31_35_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        31: "31-national-commissions-sc-st-bc",
        32: "32-cag",
        33: "33-attorney-general-and-advocate-general",
        34: "34-niti-aayog",
        35: "35-nhrc-and-shrc",
    }
)
runner.PYQ_STATUS.update(
    {
        31: (
            "direct 2018, 2020 and 2022 commission demands plus routed "
            "constitutional-list and sub-classification questions retained"
        ),
        32: (
            "direct 2018 appointment/powers and 2024 legality-propriety demands "
            "retained with parliamentary-accountability routes"
        ),
        33: (
            "direct 2019 chief-adviser and 2025 role-rights-limits demands "
            "retained; State Advocate-General material remains comparative"
        ),
        34: (
            "direct 2018 Planning-Commission comparison and routed 2019 Atal "
            "Innovation Mission demand retained with current composition control"
        ),
        35: (
            "direct 2018 umbrella-commission and 2021 limitations-remedies "
            "demands retained with statutory and accreditation status controls"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_31_35_deep_review",
        "test_run_polity_31_35_semantic_topic",
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
        raise ValueError("Polity 31-35 runner accepts only topic numbers 31 through 35.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
