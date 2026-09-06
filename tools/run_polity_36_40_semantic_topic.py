"""Run one sequential Polity semantic review for topics 36-40."""

from __future__ import annotations

import argparse
import json

import regenerate_polity_36_40_deep_review as deep
import run_polity_semantic_topic as runner


runner.deep = deep
runner.TOPIC_CHOICES = range(36, 41)
runner.DEEP_REVIEW_TEST_MODULE = "test_regenerate_polity_36_40_deep_review"
runner.DRIVER_FILES.update(
    {
        "tools\\regenerate_polity_36_40_deep_review.py",
        "tools\\test_regenerate_polity_36_40_deep_review.py",
        "tools\\run_polity_36_40_semantic_topic.py",
        "tools\\test_run_polity_36_40_semantic_topic.py",
    }
)
runner.SLUGS.update(
    {
        36: "36-cic-and-sic",
        37: "37-cvc-and-cbi",
        38: "38-lokpal-and-lokayuktas",
        39: "39-cooperative-societies",
        40: "40-official-language",
    }
)
runner.PYQ_STATUS.update(
    {
        36: (
            "direct 2020 RTI-amendment and Commission-autonomy demand retained "
            "with the commenced 2025 privacy substitution separately controlled"
        ),
        37: (
            "direct 2021 federal-consent demand and controlled 2026 objective "
            "institutional-matching demand retained without inventing a final key"
        ),
        38: (
            "direct 2025 Prelims Lokpal composition/jurisdiction demand retained; "
            "no direct Mains demand fabricated"
        ),
        39: (
            "adjacent 2020 DCCB, 2021 UCB and 2023 cooperative-production "
            "demands retained with banking/agriculture ownership labels"
        ),
        40: (
            "routed 2024 Eighth-Schedule amendment demand retained; no proposal "
            "or policy statement is relabelled as enacted constitutional law"
        ),
    }
)


def run_tests() -> list[dict[str, object]]:
    modules = [
        "test_regenerate_polity_36_40_deep_review",
        "test_run_polity_36_40_semantic_topic",
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
        raise ValueError("Polity 36-40 runner accepts only topic numbers 36 through 40.")
    return runner.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=runner.TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
