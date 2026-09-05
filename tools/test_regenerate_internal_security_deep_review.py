"""Focused tests for the Internal Security immutable deep-review driver."""

from __future__ import annotations

import importlib
import unittest
from pathlib import Path

import regenerate_internal_security_deep_review as deep


class InternalSecurityDeepReviewTests(unittest.TestCase):
    def test_manifest_order_and_provenance_owners_are_exact(self) -> None:
        topics = deep.topics()
        self.assertGreaterEqual(len(topics), 12)
        self.assertEqual(
            [f"internal-security-{number:02d}" for number in range(1, len(topics) + 1)],
            [topic.topic_key for topic in topics],
        )
        for topic in topics:
            self.assertGreater(topic.basic_path.stat().st_size, 1)
            self.assertGreater(topic.canonical_path.stat().st_size, 1)
            self.assertGreater(topic.advanced_path.stat().st_size, 1)
            self.assertNotEqual(topic.basic_path, topic.canonical_path)

    def test_all_real_authoring_generators_are_importable(self) -> None:
        self.assertEqual(12, len(deep.INTERNAL_SECURITY_GENERATOR_MODULES))
        for number, module_name in enumerate(
            deep.INTERNAL_SECURITY_GENERATOR_MODULES, 1
        ):
            module = importlib.import_module(module_name)
            self.assertEqual(1, len(module.TOPICS))
            self.assertEqual(
                f"internal-security-{number:02d}", module.TOPICS[0]["key"]
            )
            self.assertTrue(callable(module.self_check))

    def test_review_controls_cover_all_twelve_topics(self) -> None:
        samples = {
            1: "Security output is not development outcome",
            2: "Designation is not conviction",
            3: "security operation is not development delivery",
            4: "Ceasefire is not final settlement",
            5: "reorganisation is not statehood restoration",
            6: "border guarding is not state police law and order",
            7: "Naval defence is not Coast Guard law enforcement",
            8: "Cyber incident is not cybercrime",
            9: "Misinformation is not disinformation",
            10: "attachment is not confiscation",
            11: "trafficking is not smuggling",
            12: "Intelligence is not evidence",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_internal_security_precision(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Threat boundary",
            "Law/status boundary",
            "Institutional boundary",
            "Process boundary",
            "Current-data boundary",
            "designation from conviction",
            "cyber incident from cybercrime",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_answer_contract_is_exam_executable_and_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse India's response to an internal-security threat. Answer in 250 words.
**Model thesis:** Security requires lawful prevention, response and accountability.
**Claim → named evidence → analysis → qualification:**
- A named Indian law and institution demonstrate mandate and process.
**Qualified conclusion:** Durable security combines capacity, legitimacy and rights.

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
        self.assertIn("federal-rights boundary", repaired)
        self.assertIn("implementation bottleneck", repaired)

    def test_review_lines_and_paths_are_windows_safe(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_allocation_reloads_all_three_trackers(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation = source[
            source.index("def allocate(") : source.index(
                "def section(", source.index("def allocate(")
            )
        ]
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", allocation)
        self.assertIn("old, master_row, review_row = live_identity(topic)", allocation)

    def test_driver_is_static_and_subprocess_backed(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertNotIn("exec(compile(", source)
        self.assertNotIn("_prior_main", source)
        self.assertNotIn("def load_tests(", source)
        self.assertIn('[sys.executable, "-m", "unittest", "-v", module]', source)

    def test_publication_inventory_and_counts_are_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn("selected_keys=None", source)
        self.assertIn("full_count = len(live_ids)", source)
        self.assertIn("master_ids == live_ids == review_ids == manifest_ids", source)
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("changed-file inventory contains missing paths", source)


if __name__ == "__main__":
    unittest.main()
