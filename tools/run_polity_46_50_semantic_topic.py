"""Run one sequential Polity semantic review for topics 46-50."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_46_50_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(46, 51)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_46_50_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_46_50_deep_review.py",
        "tools\\test_regenerate_polity_46_50_deep_review.py",
        "tools\\run_polity_46_50_semantic_topic.py",
        "tools\\test_run_polity_46_50_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        46: "46-administrative-tribunals",
        47: "47-comparative-constitutional-design",
        48: "48-ministries-departments-and-central-secretariat",
        49: "49-regulatory-state-and-quasi-judicial-institutions",
        50: "50-concept-of-the-constitution",
    }
)
runner.PYQ_STATUS.update(
    {
        46: (
            "direct 2025 GS-II administrative-tribunal and 2021 rationalisation "
            "demand retained with current Bill-versus-operative-law status explicit"
        ),
        47: (
            "comparative executive, federal, rights, judicial and amendment demands "
            "retained by exact principal owner without mechanical transplantation"
        ),
        48: (
            "ministry, executive-accountability, Cabinet-committee and civil-service "
            "demands retained with dated institutional labels and cross-ownership"
        ),
        49: (
            "statutory-body, regulator, quasi-judicial and natural-justice demands "
            "retained with exact source/function/appeal distinctions"
        ),
        50: (
            "constitutionalism, limited amendment and interpretive-doctrine demands "
            "retained without duplicating the salient-features or amendment owners"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_46_50_deep_review",
        "test_run_polity_46_50_semantic_topic",
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
        raise ValueError("Polity 46-50 runner accepts only topic numbers 46 through 50.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
