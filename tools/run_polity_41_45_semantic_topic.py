"""Run one sequential Polity semantic review for topics 41-45."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_41_45_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(41, 46)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_41_45_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_41_45_deep_review.py",
        "tools\\test_regenerate_polity_41_45_deep_review.py",
        "tools\\run_polity_41_45_semantic_topic.py",
        "tools\\test_run_polity_41_45_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        41: "41-public-services",
        42: "42-anti-defection-law",
        43: "43-political-parties",
        44: "44-pressure-groups",
        45: "45-national-integration-and-foreign-policy",
    }
)
runner.PYQ_STATUS.update(
    {
        41: (
            "adjacent 2020 civil-services-reform demand retained with service-law "
            "ownership and governance-reform cross-ownership explicit"
        ),
        42: (
            "direct 2022 nominated-member and 2025 political-party Tenth-Schedule "
            "demands retained; no direct Mains question fabricated"
        ),
        43: (
            "direct 2022 party-centralisation demand and routed finance, disclosure "
            "and recognition demands retained with official-key discipline"
        ),
        44: (
            "direct 2019 farmer-group, 2021 business-association and 2025 "
            "environmental-pressure-group Mains demands retained"
        ),
        45: (
            "adjacent integration, treaty, federal and foreign-policy demands remain "
            "cross-owned; no direct question is fabricated"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_41_45_deep_review",
        "test_run_polity_41_45_semantic_topic",
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
        raise ValueError("Polity 41-45 runner accepts only topic numbers 41 through 45.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
