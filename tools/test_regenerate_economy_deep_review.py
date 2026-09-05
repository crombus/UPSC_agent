"""Focused tests for the Economy immutable deep-review driver."""

from __future__ import annotations

import unittest
from pathlib import Path

import regenerate_economy_deep_review as deep


class EconomyDeepReviewTests(unittest.TestCase):
    def test_manifest_order_scope_and_provenance_owners_are_exact(self) -> None:
        topics = deep.topics()
        self.assertEqual(31, len(topics))
        self.assertEqual(
            [f"economy-{number:02d}" for number in range(1, 32)],
            [topic.topic_key for topic in topics],
        )
        for topic in topics:
            self.assertGreater(topic.basic_path.stat().st_size, 1)
            self.assertGreater(topic.canonical_path.stat().st_size, 1)
            self.assertGreater(topic.advanced_path.stat().st_size, 1)
            self.assertNotEqual(topic.basic_path, topic.canonical_path)

    def test_review_controls_cover_all_thirty_one_topics(self) -> None:
        samples = {
            1: "accounting identity",
            2: "HDI is not IHDI",
            3: "falling inflation is not falling prices",
            4: "announcement is not complete transmission",
            5: "Bank is not NBFC",
            6: "write-off is not waiver",
            7: "yield is not coupon",
            8: "Bondholder is not owner",
            9: "BE, RE, Actual",
            10: "Council recommendation",
            11: "Land record is not title guarantee",
            12: "MSP coverage is not procurement coverage",
            13: "onboarding, transaction, settlement",
            14: "credit sanction is not disbursement",
            15: "installed capacity is not utilisation",
            16: "privatisation is not every disinvestment",
            17: "approved application is not production",
            18: "PPP is not privatisation",
            19: "reserve stock is not an annual flow",
            20: "tariff binding is not applied tariff",
            21: "SDR is not a currency",
            22: "denominator is labour force",
            23: "Gini is not poverty",
            24: "UPI volume is not value",
            25: "green label is not verified additionality",
            26: "Survey projection is not Budget estimate",
            27: "Registry entry is not land title",
            28: "peace clause is not permanent exemption",
            29: "production change is not mission-attributable",
            30: "Livestock population is a stock",
            31: "Capacity in MW is not generation in MWh",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_economy_precision(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Formula boundary",
            "Transmission method",
            "Current-data method",
            "Programme-status method",
            "External/WTO method",
            "Budget and Economic Survey editions are never mixed",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_every_economy_generator_range_is_wired(self) -> None:
        self.assertEqual(
            (
                "test_generate_economy_01_05_sequential",
                "test_generate_economy_06_10_sequential",
                "test_generate_economy_11_15_sequential",
                "test_generate_economy_16_19_sequential",
                "test_generate_economy_20_23_sequential",
                "test_generate_economy_24_27_sequential",
                "test_generate_economy_28_31_sequential",
            ),
            deep.ECONOMY_TEST_MODULES,
        )

    def test_answer_contract_is_exam_executable_and_answer_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse monetary transmission and its distributional trade-offs. Answer in 250 words.
**Model thesis:** Policy affects activity and inflation through bounded channels and lags.
**Claim → named evidence → analysis → qualification:**
- A named Indian institution demonstrates the instrument and balance-sheet mechanism.
**Qualified conclusion:** Outcomes depend on pass-through, supply conditions and distribution.

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
        self.assertIn("growth, distribution, stability, sustainability", repaired)
        self.assertIn("balance-sheet or incentive", repaired)

    def test_review_lines_and_paths_are_windows_safe(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_live_tracker_scope_is_twenty_seven_or_thirty_one_before_review(self) -> None:
        review = deep.load(deep.REVIEW_TRACKER)
        rows = [
            row for row in review["topics"] if row["topic_key"].startswith("economy-")
        ]
        self.assertIn(len(rows), (27, 31))
        if len(rows) == 31 and all(row["status"] == "pending" for row in rows):
            self.assertTrue(all(row["scores"]["total"] is None for row in rows))
            self.assertTrue(
                all(value is None for row in rows for value in row["hard_gates"].values())
            )

    def test_allocation_rereads_live_state_and_publish_precedes_review(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation_base = Path(deep.__file__).with_name(
            "regenerate_ancient_history_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", allocation_base)
        self.assertIn("_publish_before_tracker_sync_when_needed", source)
        self.assertIn("fresh pending", source)

    def test_inventory_is_utf8_nul_safe_and_verifies_paths(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("changed-file inventory contains missing paths", source)

    def test_full_library_count_is_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        republish = source[
            source.index("def _republish_master_library()")
            : source.index("def _run_tracker_sync()")
        ]
        self.assertIn("expected_count = len(expected_ids)", republish)
        self.assertIn("selected_keys=None", republish)
        self.assertIn("full_pdf_validation=False", republish)
        self.assertIn("_run_tracker_sync()", republish)
        self.assertIn("for attempt in range(1, 4)", republish)
        self.assertIn("master_ids != expected_ids", republish)
        self.assertIn("review_ids != expected_ids", republish)
        self.assertNotIn("selected_keys = [topic.topic_key", republish)
        self.assertNotIn("343-topic", source)

    def test_full_publication_guards_every_live_identity(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn("def _all_latest_ids", source)
        self.assertIn("before = _all_latest_ids(before_status)", source)
        self.assertIn("after = _all_latest_ids(load(STATUS))", source)
        self.assertIn("A learner-v2 identity changed", source)
        self.assertIn("final_manifest[\"topic_count\"]", source)
        self.assertIn("final_validation[\"topic_count\"]", source)
        self.assertIn("master_ids == live_ids", source)
        self.assertIn("review_ids == live_ids", source)
        self.assertIn("final_library_topic_count", source)


if __name__ == "__main__":
    unittest.main()
