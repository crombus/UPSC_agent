"""Run one hostile semantic-completeness review for Indian Society Topics 01-15."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import regenerate_indian_society_deep_review as deep
import run_geography_semantic_topic as _base


ROOT = deep.ROOT
REPORT_DATE = "2026-09-05"
TOPIC_CHOICES = range(1, 16)
DEEP_REVIEW_TEST_MODULE = "test_regenerate_indian_society_deep_review"
DRIVER_FILES = {
    "tools\\regenerate_indian_society_deep_review.py",
    "tools\\run_indian_society_semantic_topic.py",
    "tools\\test_run_indian_society_semantic_topic.py",
}
SEMANTIC_STATUS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
REPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "indian-society"
SLUGS = {
    1: "01-salient-features-diversity-indian-society",
    2: "02-caste-system-structure-contemporary-dynamics",
    3: "03-tribe-tribal-society",
    4: "04-family-marriage-kinship",
    5: "05-rural-society-agrarian-change",
    6: "06-population-associated-issues",
    7: "07-women-womens-organisations",
    8: "08-social-empowerment",
    9: "09-poverty-developmental-issues",
    10: "10-urbanisation-problems-remedies",
    11: "11-effects-globalisation-indian-society",
    12: "12-social-change-modernisation",
    13: "13-communalism",
    14: "14-regionalism",
    15: "15-secularism",
}
PYQ_STATUS = {
    1: (
        "direct routes cover 2019 cultural continuity and 2024 diversity-"
        "marginality; two routed 2023 sports items are rejected as ownership "
        "artefacts, and no unavailable 2026 GS-I demand is invented"
    ),
    2: (
        "direct routes cover 2018 associational forms, 2020 continuing "
        "relevance, 2022 sect salience, 2023 fluid/static identity and 2024 "
        "intercaste/interreligious marriage; no 2026 demand is invented"
    ),
    3: (
        "direct routes cover 2021 tribal knowledge, 2022 aggregation contexts "
        "and 2025 displacement/rehabilitation; the unkeyed 2021 language item "
        "stays unsolved and no 2026 demand is invented"
    ),
    4: (
        "direct routes cover 2022 work from home, two 2023 family questions and "
        "the family/kinship side of the 2024 marriage demand; no 2026 demand is "
        "invented"
    ),
    5: (
        "the verified 2018-2025 corpus contains no direct Topic 05 GS-I route; "
        "adjacent Economy/Governance demands stay cross-owned and the unavailable "
        "2026 paper is not reconstructed"
    ),
    6: (
        "direct routes cover 2019 women's empowerment and population growth, "
        "2021 population education and 2024 demographic winter; Geography "
        "cross-ownership is disclosed and no unavailable 2026 demand is invented"
    ),
    7: (
        "direct routes cover 2018 movement reach, 2019 challenges across time "
        "and space, 2021 gig work, 2023 young-women self-harm and 2024 "
        "equality-equity-empowerment; no unsupported cause or 2026 demand is invented"
    ),
    8: (
        "the owner carries 2024 affirmative-action outcomes and 2025 Phule, "
        "while Social Justice and Modern History routing remains disclosed; "
        "no group statistic, scheme success rate or 2026 demand is invented"
    ),
    9: (
        "direct routes cover 2018 persistent poverty, 2020 pandemic/class "
        "inequality, cross-owned 2024 collaboration and 2025 sustainable "
        "growth versus poor needs; no current poverty rate or 2026 demand is invented"
    ),
    10: (
        "direct routes cover 2022 Tier-2 cities and consumption, 2023 "
        "segregation, cross-owned 2024 migrant pull and 2025 smart-city "
        "distributive justice; no unsupported city statistic or 2026 demand is invented"
    ),
    11: (
        "direct routes cover 2018 cultural specificity, 2019 global/local "
        "identity, 2020 pluralism, 2022 technology and scarce resources, 2024 "
        "women's urban migration and 2025 consumer culture; the 2025 fast-food "
        "route remains Social Change-owned and no 2026 demand is invented"
    ),
    12: (
        "direct routes cover 2020 customs and obscurantism, 2021 traditional-"
        "value continuity and 2025 fast-food growth; the 2021 cryptocurrency "
        "instrument remains Economy/Science-owned and no 2026 demand is invented"
    ),
    13: (
        "direct routes cover 2018 power struggle versus relative deprivation "
        "and 2023 post-liberal economy/ethnic identity; no direct 2024-2025 "
        "standalone route, riot statistic or unavailable 2026 demand is invented"
    ),
    14: (
        "direct routes cover 2020 cultural assertiveness and 2024 regional "
        "disparity versus diversity; statehood, autonomy and secession remain "
        "distinct and no unsupported ranking or 2026 demand is invented"
    ),
    15: (
        "direct GS-I routes cover 2018 Indian versus Western secularism, 2019 "
        "practices challenging secularism and 2022 tolerance/assimilation/"
        "pluralism; the France comparison stays Polity-owned and no unavailable "
        "2026 demand is invented"
    ),
}
EXPORT_LIBRARY_TESTS = _base.EXPORT_LIBRARY_TESTS
FORCE_REGENERATE = False
STATUS_TOPIC_KEYS: dict[str, str] = {}


def generator_test_module(number: int) -> str:
    return f"test_generate_indian_society_{number:02d}_sequential"


def run_tests(topic: deep.Topic) -> list[dict[str, Any]]:
    modules = [
        DEEP_REVIEW_TEST_MODULE,
        generator_test_module(topic.number),
        "test_run_indian_society_semantic_topic",
        *[
            "test_export_four_item_library.ExportLibraryTests." + name
            for name in EXPORT_LIBRARY_TESTS
        ],
        "test_sync_deep_review_tracker",
        "test_refresh_all_v2_learning_sessions",
    ]
    tests = [deep.run_unittest(module) for module in modules]
    if any(
        item["exit_code"] or item["failures"] or item["errors"] for item in tests
    ):
        raise RuntimeError(f"Targeted tests failed: {tests}")
    return tests


def prepare_live_source_config(topic: deep.Topic) -> None:
    config = deep.CURRENT_AUTHORING_CONFIGS.get(topic.topic_key)
    if config is None:
        raise ValueError(f"{topic.topic_key}: authoring configuration is absent.")
    sources, note = deep.SOCIETY_LIVE_OFFICIAL_SOURCES[topic.number]
    config["live_sources"] = list(sources)
    config["current_note"] = note


def apply_live_source_provenance(
    topic: deep.Topic,
    result: dict[str, Any],
    changed: set[str],
) -> None:
    sources, note = deep.SOCIETY_LIVE_OFFICIAL_SOURCES[topic.number]
    status = _base.load(deep.STATUS)
    record = next(
        row
        for row in reversed(status["exports"])
        if row.get("record_id") == result["new_record_id"]
    )
    record.setdefault("provenance", {}).update(
        {
            "live_sources": sources,
            "current_linkage_note": note,
            "live_sources_rechecked_on": REPORT_DATE,
        }
    )
    _base.dump(deep.STATUS, status)
    changed.add(_base.rel(deep.STATUS))

    record_path = deep.EXPORTS / (
        f"{topic.topic_key}-learner-v2-g{result['new_generation']}-"
        f"{deep.DATE}-record.json"
    )
    if record_path.is_file():
        payload = _base.load(record_path)
        payload.setdefault("provenance", {}).update(
            {
                "live_sources": sources,
                "current_linkage_note": note,
                "live_sources_rechecked_on": REPORT_DATE,
            }
        )
        _base.dump(record_path, payload)
        changed.add(_base.rel(record_path))

    content_spec = deep.repo(record["provenance"]["content_spec"])
    if content_spec.is_file():
        payload = _base.load(content_spec)
        payload["live_official_sources"] = sources
        payload["current_status_control"] = note
        payload["live_sources_rechecked_on"] = REPORT_DATE
        _base.dump(content_spec, payload)
        changed.add(_base.rel(content_spec))


def report_text(
    topic: deep.Topic,
    result: dict[str, Any],
    validation: dict[str, Any],
    tests: list[dict[str, Any]],
    next_key: str,
) -> str:
    metrics = validation["metrics"]
    return f"""# Indian Society Semantic-Completeness Review {topic.number:02d} — {topic.title}

**Topic key:** `{topic.topic_key}`  
**Review date:** 5 September 2026  
**Result:** PASSED  
**Canonical owner:** `{_base.rel(topic.basic_path)}`  
**Accepted identity:** `{result['new_record_id']}`

Topic {topic.number:02d} alone was active. The official syllabus/index,
canonical Basic owner, Optional Advanced owner, master framework, bounded
cross-owner bridges, verified 2018-2026 PYQ ledger, relevant OCR-searchable
official GS-I papers and authoritative live government sources were reconciled
through a hostile four-ledger audit.

Canonical repair adds precise definitions, owned sociological thinkers and
theories, India-specific evidence, intersectional and regional variation,
constitutional/legal boundaries, source-date-status controls and explicit
anti-stereotyping/data limitations. Detailed Social Justice scheme architecture
remains cross-owned rather than imported.

The immutable successor preserves Basic-first/Advanced-last order, final
register notes, examiner-grade answer contracts, strict A-B-C-D rotation and
twelve manually authored ASCII panels agreeing with twelve graphical Core
stages. Approval remains false. PYQ status: {PYQ_STATUS[topic.number]}.

Validation passed: {metrics['main_pages']} main pages,
{metrics['workbook_pages']} workbook pages,
{metrics['question_count']} solved blocks, {metrics['mcq_count']} MCQs,
{metrics['ascii_panel_count']}/12 ASCII panels and
{metrics['graphical_stage_count']}/12 graphical stages. Targeted tests:
{sum(item['tests'] for item in tests)}; failures: 0.

The authoritative queue advanced exactly one topic to `{next_key}`.

Machine validation:
`upsc-ai-kit\\manifests\\exports\\{topic.topic_key}-semantic-validation-{REPORT_DATE}.json`

Inventory:
`upsc-ai-kit\\manifests\\exports\\{topic.topic_key}-semantic-completeness-{REPORT_DATE}-changed-files.txt`
"""


def _configure_base() -> None:
    values = {
        "deep": deep,
        "ROOT": ROOT,
        "REPORT_DATE": REPORT_DATE,
        "TOPIC_CHOICES": TOPIC_CHOICES,
        "DEEP_REVIEW_TEST_MODULE": DEEP_REVIEW_TEST_MODULE,
        "DRIVER_FILES": DRIVER_FILES,
        "FORCE_REGENERATE": FORCE_REGENERATE,
        "STATUS_TOPIC_KEYS": STATUS_TOPIC_KEYS,
        "SEMANTIC_STATUS": SEMANTIC_STATUS,
        "REPORT_DIR": REPORT_DIR,
        "SLUGS": SLUGS,
        "PYQ_STATUS": PYQ_STATUS,
        "EXPORT_LIBRARY_TESTS": EXPORT_LIBRARY_TESTS,
        "generator_test_module": generator_test_module,
        "run_tests": run_tests,
        "apply_live_source_provenance": apply_live_source_provenance,
        "report_text": report_text,
    }
    for name, value in values.items():
        setattr(_base, name, value)


def run(topic_number: int) -> dict[str, Any]:
    if topic_number not in TOPIC_CHOICES:
        raise ValueError("This driver owns only Indian Society Topics 01-15.")
    topic = deep.topics()[topic_number - 1]
    prepare_live_source_config(topic)
    _configure_base()
    return _base.run(topic_number)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=TOPIC_CHOICES, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
