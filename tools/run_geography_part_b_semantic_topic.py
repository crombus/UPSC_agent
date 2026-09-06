"""Run one strictly sequential Geography Part B semantic-completeness review."""

from __future__ import annotations

import argparse
import json
from typing import Any

import regenerate_geography_part_b_deep_review as deep
import run_geography_semantic_topic as base


SLUGS = {
    26: "26-world-population-and-demographic-transition",
    27: "27-migration-theories-and-patterns-india",
    28: "28-human-settlements-and-urbanisation",
    29: "29-regional-development-and-five-year-plans",
    30: "30-primary-economic-activities-agriculture",
    31: "31-mineral-and-energy-resources-world-and-india",
    32: "32-industries-and-industrial-regions",
    33: "33-transport-trade-and-indian-space-programme",
    34: "34-world-regional-geography-continents-countries",
    35: "35-indian-political-geography-boundaries-neighbours",
    36: "36-contemporary-geographical-issues-india",
    37: "37-cultural-and-social-geography-of-india",
}

PYQ_STATUS = {
    26: (
        "direct routes cover 2024 Prelims TFR definition and ageing/low-birth-"
        "rate countries plus 2024 GS-I Q7 on demographic winter; absent answer "
        "letters are not inferred"
    ),
    27: (
        "direct ownership includes 2024 GS-I Q5 on why large cities attract "
        "more migrants; the 2018 indentured-labour diaspora demand remains "
        "cross-owned with Modern History"
    ),
    28: (
        "the audited ledgers contain no direct Topic 28 route; migrant-city "
        "attraction remains Topic 27-owned and urban-local-body demands retain "
        "Governance/Polity ownership"
    ),
    29: (
        "the audited ledgers contain no direct Topic 29 route; locational "
        "planning, federal finance and implementation questions retain their "
        "routed owners, so no PYQ is fabricated"
    ),
    30: (
        "routes cover 2019 New World crops, 2020 crop-climate, 2022 tea states, "
        "2023 India-China farm statistics, 2025 turmeric and 2025 GS-I Q5 on "
        "non-farm primary activities; unavailable keys stay unpromoted"
    ),
    31: (
        "verified routes cover mineral, energy, petroleum and resource-security "
        "demands; unavailable or provisional objective keys remain unpromoted"
    ),
    32: (
        "industrial-location, region and corridor demands remain bounded by "
        "their routed owners; no missing PYQ wording or answer key is invented"
    ),
    33: (
        "transport, trade-route and space-application routes retain exact paper "
        "ownership and mission status; specialist engineering remains cross-owned"
    ),
    34: (
        "world-region and map demands retain statistical, political and disputed-"
        "status boundaries; no country classification is treated as timeless"
    ),
    35: (
        "boundary, maritime-zone and neighbourhood routes retain exact legal and "
        "control-line terminology; disputed claims are not presented as settled"
    ),
    36: (
        "direct routes include 2019 Indian water-stress variation, 2023 freshwater "
        "availability/access and 2024 Gangetic-groundwater food-security demands; "
        "adjacent Environment, Disaster and Economy ownership stays bounded"
    ),
    37: (
        "direct ownership includes 2019 cultural pockets across India; the 2023 "
        "Purvaiya-cultural-ethos demand is cross-owned with monsoon geography, and "
        "no census category, social identity or unavailable key is inferred"
    ),
}


def generator_test_module(number: int) -> str | None:
    return {
        26: "test_generate_geography_26_sequential",
        27: "test_generate_geography_27_sequential",
        29: "test_generate_geography_29_sequential",
        31: "test_generate_geography_31_sequential",
        33: "test_generate_geography_33_sequential",
        34: "test_generate_geography_34_sequential",
        35: "test_generate_geography_35_sequential",
        36: "test_generate_geography_36_sequential",
        37: "test_generate_geography_37_sequential",
    }.get(number)


def run_tests(topic: deep.Topic) -> list[dict[str, Any]]:
    modules = [
        "test_regenerate_geography_part_b_deep_review",
        "test_run_geography_part_b_semantic_topic",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in base.EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    generator_test = generator_test_module(topic.number)
    if generator_test:
        modules.insert(1, generator_test)
    tests = [deep.run_unittest(module) for module in modules]
    if any(
        item["exit_code"] or item["failures"] or item["errors"] for item in tests
    ):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


def configure() -> None:
    base.deep = deep
    base.ROOT = deep.ROOT
    base.SLUGS = SLUGS
    base.PYQ_STATUS = PYQ_STATUS
    base.TOPIC_CHOICES = range(26, 38)
    base.DEEP_REVIEW_TEST_MODULE = "test_regenerate_geography_part_b_deep_review"
    base.FORCE_REGENERATE = True
    base.STATUS_TOPIC_KEYS = {
        operational: canonical
        for canonical, operational in deep.CANONICAL_TO_OPERATIONAL.items()
    }
    base.DRIVER_FILES = {
        "tools\\regenerate_geography_part_b_deep_review.py",
        "tools\\test_regenerate_geography_part_b_deep_review.py",
        "tools\\run_geography_semantic_topic.py",
        "tools\\test_run_geography_semantic_topic.py",
        "tools\\run_geography_part_b_semantic_topic.py",
        "tools\\test_run_geography_part_b_semantic_topic.py",
    }
    base.generator_test_module = generator_test_module
    base.run_tests = run_tests


def run(topic_number: int) -> dict[str, Any]:
    configure()
    return base.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=range(26, 38), required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
