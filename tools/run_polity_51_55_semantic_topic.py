"""Run one sequential Polity semantic review for topics 51-55."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_51_55_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(51, 56)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_51_55_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\build_deep_review_polity_53_55.py",
        "tools\\regenerate_polity_51_55_deep_review.py",
        "tools\\test_regenerate_polity_51_55_deep_review.py",
        "tools\\run_polity_51_55_semantic_topic.py",
        "tools\\test_run_polity_51_55_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        51: "51-rights-and-liabilities-of-the-government",
        52: "52-ncrwc-and-working-of-the-constitution",
        53: "53-special-provisions-relating-to-certain-classes",
        54: "54-lok-adalats-and-other-courts",
        55: "55-constitutional-interpretation-doctrines",
    }
)
runner.PYQ_STATUS.update(
    {
        51: (
            "government-contract, property, compensation, secrecy and remedy "
            "demands remain precisely routed; no direct verified PYQ is fabricated"
        ),
        52: (
            "constitutional-reform, institutional-working and commission-report "
            "demands remain cross-owned; no direct NCRWC PYQ is fabricated"
        ),
        53: (
            "direct 2023 Article 335 and 2024 women's-reservation demands plus "
            "routed commission demands retained with current commencement status"
        ),
        54: (
            "direct 2020 legal-services and 2023-24 access-to-justice demands "
            "retained with ordinary/PLA/mediation source distinctions"
        ),
        55: (
            "direct/routed doctrine, amendment, federal-competence and rights-review "
            "demands retained with case, year, effect and bench-strength discipline"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_51_55_deep_review",
        "test_run_polity_51_55_semantic_topic",
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
        raise ValueError("Polity 51-55 runner accepts only topic numbers 51 through 55.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
