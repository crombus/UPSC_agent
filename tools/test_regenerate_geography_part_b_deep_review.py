"""Focused tests for the Geography Part B immutable deep-review driver."""

from __future__ import annotations

import importlib
import unittest
from pathlib import Path

import regenerate_geography_part_b_deep_review as deep


def load_tests(
    loader: unittest.TestLoader,
    tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    suite = unittest.TestSuite([tests])
    for name in deep.PART_B_TEST_MODULES:
        suite.addTests(loader.loadTestsFromModule(importlib.import_module(name)))
    return suite


class GeographyPartBDeepReviewTests(unittest.TestCase):
    def test_manifest_order_and_operational_identity_are_exact(self) -> None:
        topics = deep.topics()
        expected = [
            "geography-26",
            "geography-27",
            "geography-28-human-settlements-and-urbanisation",
            "geography-29",
            "geography-30-primary-economic-activities-agriculture",
            "geography-31",
            "geography-32-industries-and-industrial-regions",
            "geography-33",
            "geography-34",
            "geography-35",
            "geography-36",
            "geography-37",
        ]
        self.assertEqual(expected, [topic.topic_key for topic in topics])
        self.assertEqual(list(range(26, 38)), [topic.number for topic in topics])

    def test_legacy_aliases_are_catalogue_and_live_history_backed(self) -> None:
        catalogue = deep._catalogue_rows()
        status = deep.load(deep.STATUS)
        for canonical, operational in deep.CANONICAL_TO_OPERATIONAL.items():
            self.assertEqual(
                [operational], catalogue[canonical]["tracker_topic_keys"]
            )
            self.assertFalse(
                any(
                    row.get("variant") == "learner-v2"
                    and row.get("topic_key") == canonical
                    for row in status["exports"]
                )
            )
            self.assertTrue(
                any(
                    row.get("variant") == "learner-v2"
                    and row.get("topic_key") == operational
                    for row in status["exports"]
                )
            )

    def test_review_controls_cover_all_twelve_topics(self) -> None:
        samples = {
            26: "demographic dividend is a conditional",
            27: "Harris-Todaro",
            28: "statutory town, census town",
            29: "Planning Commission was replaced by NITI Aayog in 2015",
            30: "von Thünen",
            31: "Resource differs from reserve",
            32: "Weber's least-cost theory",
            33: "ISRO from the Department of Space",
            34: "Middle East with West Asia",
            35: "Actual Ground Position Line",
            36: "hazard or pressure × exposure × vulnerability × governance",
            37: "Scheduled Tribe, tribe, indigenous",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_models_maps_data_policy_and_approval(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Model method",
            "Map discipline",
            "reference period, release date and status",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_answer_contract_is_exam_executable(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse the spatial pattern and policy response. Answer in 250 words.
**Model thesis:** The pattern emerges through interacting spatial controls.
**Claim → named evidence → analysis → qualification:**
- A named Indian region demonstrates the mechanism at corridor scale.
**Qualified conclusion:** The relationship is strong but neither sufficient nor uniform.

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired, metrics = deep.repair_answer_contracts(source)
        self.assertEqual(1, metrics["question_count"])
        for marker in (
            "**Demand decoding:**",
            "**Detailed examiner-grade model answer:**",
            "**Executable exam-length answer / compression plan:**",
            "**Why this earns marks:**",
            "**How to improve this answer:**",
        ):
            self.assertIn(marker, repaired)

    def test_visual_gateway_is_human_geography_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION

### SESSION 1 — TEST PATTERN

#### DEFINITION / WHAT THIS IS CALLED

Definition.

## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep.insert_contract(
            source, deep.topics()[0], {"provenance": {}}
        )
        self.assertIn("MODEL / CAUSAL / INSTITUTIONAL MECHANISM", repaired)
        self.assertIn("NAMED INDIA + WORLD MAP / DATA ANCHOR", repaired)
        self.assertNotIn("PHYSICAL MECHANISM OR CIRCULATION", repaired)

    def test_agriculture_legacy_core_is_repaired_to_fifteen_sessions(self) -> None:
        topic = next(item for item in deep.topics() if item.number == 30)
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        source = deep.repo(record["markdown"]).read_text(encoding="utf-8")
        repaired = deep.insert_contract(source, topic, record)
        self.assertGreaterEqual(repaired.count("### SESSION "), 15)
        self.assertGreaterEqual(repaired.count("#### VISUAL FIRST"), 15)
        self.assertIn("MSP ANNOUNCEMENT ≠ PROCUREMENT", repaired)

    def test_long_source_url_table_is_semantically_split(self) -> None:
        source = """Before
| Source | Path / URL | Use and boundary |
|---|---|---|
| MoSPI | https://example.test/a-very-long-path.pdf | Provisional, not final. |
After
"""
        repaired = deep._split_source_url_table(source)
        self.assertNotIn("| Source | Path / URL |", repaired)
        self.assertIn("**MoSPI:** `https://example.test/a-very-long-path.pdf`", repaired)
        self.assertIn("**Use and boundary:** Provisional, not final.", repaired)

    def test_industries_legacy_core_and_answer_contract_are_repaired(self) -> None:
        topic = next(item for item in deep.topics() if item.number == 32)
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        source = deep.repo(record["markdown"]).read_text(encoding="utf-8")
        repaired = deep.insert_contract(source, topic, record)
        self.assertGreaterEqual(repaired.count("### SESSION "), 15)
        self.assertGreaterEqual(repaired.count("#### VISUAL FIRST"), 15)
        repaired, metrics = deep.repair_answer_contracts(repaired)
        self.assertGreaterEqual(metrics["question_count"], 3)
        self.assertIn("**Detailed examiner-grade model answer:**", repaired)
        workbook_path = record.get("workbook_markdown") or record["provenance"][
            "workbook_markdown"
        ]
        workbook = deep.repo(workbook_path).read_text(encoding="utf-8")
        _, workbook_metrics = deep.repair_answer_contracts(workbook)
        self.assertEqual(metrics["question_count"], workbook_metrics["question_count"])

    def test_review_lines_and_paths_are_windows_safe(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_ascii_panels_keep_unique_titles_and_one_body(self) -> None:
        topic = deep.topics()[0]
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        main_path = deep.repo(record["markdown"])
        spec = deep.build_ascii_spec(
            topic,
            record,
            int(record["generation"]) + 100,
            main_path.read_text(encoding="utf-8"),
            main_path,
        )
        titles = [panel["title"].casefold() for panel in spec["topics"][0]["panels"]]
        self.assertEqual(len(titles), len(set(titles)))
        for panel in spec["topics"][0]["panels"]:
            self.assertEqual(
                1, sum(key in panel for key in ("ascii_text", "ascii_lines"))
            )
        self.assertTrue(
            spec["constraints"]["human_economic_regional_spatial_control"]
        )

    def test_allocation_rereads_live_state_and_publish_precedes_sync(self) -> None:
        inherited = Path(deep._BASE).read_text(encoding="utf-8")
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", inherited)
        publish_at = source.index(
            "result = _export_full_library_from_live_snapshot(",
            source.index("def _publish_before_tracker_sync_when_needed"),
        )
        sync_at = source.index("_run_tracker_sync()", publish_at)
        self.assertLess(publish_at, sync_at)
        self.assertIn("set(raw_manifest_keys) != operational_set", source)
        self.assertIn("reverse_alias.get(topic.topic_key, topic.topic_key)", source)
        self.assertIn("return _base_allocate_iac", source)

    def test_inventory_is_utf8_nul_safe_and_verifies_paths(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("Inventory path disappeared", source)
        self.assertIn(
            "Recover a just-written record if a concurrent tracker writer replaced it",
            source,
        )

    def test_full_library_and_validation_counts_are_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('result["topic_count"] != len(selected_keys)', source)
        inherited = Path(deep._BASE).read_text(encoding="utf-8")
        self.assertNotIn("stale unrelated-failure", inherited)


if __name__ == "__main__":
    unittest.main()
