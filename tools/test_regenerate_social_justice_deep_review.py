"""Focused tests for the Social Justice immutable deep-review driver."""

from __future__ import annotations

import importlib
import unittest
from pathlib import Path

import regenerate_social_justice_deep_review as deep


def load_tests(
    loader: unittest.TestLoader,
    tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    suite = unittest.TestSuite([tests])
    for name in deep.SOCIAL_JUSTICE_TEST_MODULES:
        suite.addTests(loader.loadTestsFromModule(importlib.import_module(name)))
    return suite


class SocialJusticeDeepReviewTests(unittest.TestCase):
    def test_manifest_order_scope_and_provenance_owners_are_exact(self) -> None:
        topics = deep.topics()
        self.assertEqual(17, len(topics))
        self.assertEqual(
            [f"social-justice-{number:02d}" for number in range(1, 18)],
            [topic.topic_key for topic in topics],
        )
        for topic in topics:
            self.assertGreater(topic.basic_path.stat().st_size, 1)
            self.assertGreater(topic.canonical_path.stat().st_size, 1)
            self.assertGreater(topic.advanced_path.stat().st_size, 1)
            self.assertNotEqual(topic.basic_path, topic.canonical_path)

    def test_review_controls_cover_all_seventeen_topics(self) -> None:
        samples = {
            1: "welfare is not charity",
            2: "stunting is not wasting",
            3: "UHC is not free hospitalisation alone",
            4: "enrolment is not attendance or learning",
            5: "women are rights-holders",
            6: "rescue is not rehabilitation",
            7: "registration of an offence is not conviction",
            8: "PESA and Forest Rights Act",
            9: "EWS is not an OBC sub-category",
            10: "Article 30 is not immunity",
            11: "accessibility is not reasonable accommodation",
            12: "pension coverage is not adequacy",
            13: "DNT is not a constitutional reservation category",
            14: "prohibition is not eradication",
            15: "enactment is not the same as commencement",
            16: "migrant is not necessarily homeless",
            17: "inclusion error adds ineligible persons",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_social_justice_boundaries(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Rights-holder map",
            "Delivery chain",
            "Prohibition/outcome discipline",
            "Reservation discipline",
            "Data discipline",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_every_social_justice_generator_test_is_wired(self) -> None:
        self.assertEqual(
            tuple(
                f"test_generate_social_justice_{number:02d}_sequential"
                for number in range(1, 18)
            ),
            deep.SOCIAL_JUSTICE_TEST_MODULES,
        )

    def test_answer_contract_is_exam_executable_and_answer_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse exclusion and accountability in welfare delivery. Answer in 250 words.
**Model thesis:** Rights require accessible and accountable implementation.
**Claim → named evidence → analysis → qualification:**
- A named Indian institution demonstrates a bounded delivery mechanism.
**Qualified conclusion:** Inclusion requires entitlement, capacity, remedy and voice.

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
        self.assertIn("rights-holder", repaired)
        self.assertIn("grievance route", repaired)

    def test_review_lines_and_paths_are_windows_safe(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_live_tracker_rows_are_fresh_pending_before_review(self) -> None:
        review = deep.load(deep.REVIEW_TRACKER)
        rows = [
            row
            for row in review["topics"]
            if row["topic_key"].startswith("social-justice-")
        ]
        if all(row["status"] == "pending" for row in rows):
            self.assertEqual(17, len(rows))
            self.assertTrue(all(row["scores"]["total"] is None for row in rows))
            self.assertTrue(
                all(value is None for row in rows for value in row["hard_gates"].values())
            )

    def test_allocation_rereads_live_state_and_publish_precedes_review(self) -> None:
        allocation_base = Path(deep.__file__).with_name(
            "regenerate_ancient_history_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "Re-read EXPORT, MASTER and REVIEW immediately", allocation_base
        )
        self.assertTrue(callable(deep._publish_before_tracker_sync_when_needed))
        self.assertTrue(callable(deep._social_justice_latest_ids))

    def test_inventory_is_utf8_nul_safe_and_verifies_paths(self) -> None:
        inherited = Path(deep.__file__).with_name(
            "regenerate_indian_society_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn('path.encode("utf-8") + b"\\0"', inherited)
        self.assertIn('payload.endswith(b"\\0")', inherited)
        self.assertIn("Changed-file inventory contains missing paths", inherited)

    def test_full_library_count_is_dynamic(self) -> None:
        inherited = Path(deep.__file__).with_name(
            "regenerate_indian_society_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn("len(selected_keys)", inherited)
        self.assertNotIn("352-topic", Path(deep.__file__).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
