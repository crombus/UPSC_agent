"""Focused tests for the Indian Society immutable deep-review driver."""

from __future__ import annotations

import importlib
import unittest
from pathlib import Path

import regenerate_indian_society_deep_review as deep


def load_tests(
    loader: unittest.TestLoader,
    tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    suite = unittest.TestSuite([tests])
    for name in deep.SOCIETY_TEST_MODULES:
        suite.addTests(loader.loadTestsFromModule(importlib.import_module(name)))
    return suite


class IndianSocietyDeepReviewTests(unittest.TestCase):
    def test_manifest_order_and_scope_are_exact(self) -> None:
        topics = deep.topics()
        self.assertEqual(15, len(topics))
        self.assertEqual(
            [f"indian-society-{number:02d}" for number in range(1, 16)],
            [topic.topic_key for topic in topics],
        )
        self.assertEqual(list(range(1, 16)), [topic.number for topic in topics])

    def test_review_controls_cover_all_fifteen_topics(self) -> None:
        samples = {
            1: "Diversity is not inequality",
            2: "Varna is not jati",
            3: "PESA 1996",
            4: "Family is not household",
            5: "Rural is not agricultural",
            6: "demographic dividend is an opportunity",
            7: "Women are not a homogeneous category",
            8: "Welfare is not empowerment",
            9: "poverty is not inequality",
            10: "statutory town is not census town",
            11: "Globalisation is not westernisation",
            12: "Modernisation is not westernisation",
            13: "Religion is not communalism",
            14: "regionalism is not automatically separatism",
            15: "Secularism is not atheism",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_society_boundaries(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Intersectional discipline",
            "correlation",
            "lived social outcome",
            "Non-homogenisation",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_every_generator_test_is_wired(self) -> None:
        self.assertEqual(
            tuple(
                f"test_generate_indian_society_{number:02d}_sequential"
                for number in range(1, 16)
            ),
            deep.SOCIETY_TEST_MODULES,
        )

    def test_answer_contract_is_exam_executable(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse the social mechanism and differentiated outcomes. Answer in 250 words.
**Model thesis:** Institutions and agency interact across unequal locations.
**Claim → named evidence → analysis → qualification:**
- A named Indian community and region demonstrate the bounded mechanism.
**Qualified conclusion:** The pattern is strong but neither uniform nor sufficient.

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
        self.assertIn("correlation-versus-causation", repaired)

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
            if row["topic_key"].startswith("indian-society-")
        ]
        if all(row["status"] == "pending" for row in rows):
            self.assertEqual(15, len(rows))
            self.assertTrue(all(row["scores"]["total"] is None for row in rows))
            self.assertTrue(
                all(value is None for row in rows for value in row["hard_gates"].values())
            )

    def test_allocation_rereads_live_state_and_publish_precedes_sync(self) -> None:
        inherited = Path(deep.__file__).with_name(
            "regenerate_indian_art_culture_deep_review.py"
        ).read_text(encoding="utf-8")
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation_base = Path(deep.__file__).with_name(
            "regenerate_ancient_history_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "Re-read EXPORT, MASTER and REVIEW immediately", allocation_base
        )
        publish_at = source.index(
            "def main() -> int:", source.index("_society_inherited_main")
        )
        self.assertIn("_publish_before_tracker_sync_when_needed", inherited)
        self.assertGreater(publish_at, 0)

    def test_inventory_is_utf8_nul_safe_and_verifies_paths(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("Changed-file inventory contains missing paths", source)

    def test_full_library_count_is_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        inherited = Path(deep.__file__).with_name(
            "regenerate_indian_art_culture_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("259-topic", source)
        self.assertIn("len(selected_keys)", inherited)


if __name__ == "__main__":
    unittest.main()
