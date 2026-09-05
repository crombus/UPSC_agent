"""Focused tests for the Disaster Management immutable deep-review driver."""

from __future__ import annotations

import importlib
import re
import unittest
from pathlib import Path

import regenerate_disaster_management_deep_review as deep


class DisasterManagementDeepReviewTests(unittest.TestCase):
    def test_manifest_order_scope_and_provenance_owners_are_exact(self) -> None:
        topics = deep.topics()
        self.assertGreaterEqual(len(topics), 18)
        self.assertEqual(
            [
                f"disaster-management-{number:02d}"
                for number in range(1, len(topics) + 1)
            ],
            [topic.topic_key for topic in topics],
        )
        for topic in topics:
            self.assertGreater(topic.basic_path.stat().st_size, 1)
            self.assertGreater(topic.canonical_path.stat().st_size, 1)
            self.assertGreater(topic.advanced_path.stat().st_size, 1)

    def test_all_actual_authoring_generators_pass_self_check(self) -> None:
        self.assertEqual(18, len(deep.DISASTER_MANAGEMENT_GENERATOR_MODULES))
        for number, module_name in enumerate(
            deep.DISASTER_MANAGEMENT_GENERATOR_MODULES, 1
        ):
            module = importlib.import_module(module_name)
            self.assertEqual(1, len(module.TOPICS))
            config = module.TOPICS[0]
            key = f"disaster-management-{number:02d}"
            self.assertEqual(key, config["key"])
            markdown = Path(config["canonical"]).read_text(encoding="utf-8")
            workbook = (
                module.SESSION_DIR / f"{key}_Solved-Workbook.md"
            ).read_text(encoding="utf-8")
            session_count = len(
                re.findall(r"(?m)^### SESSION\s+\d+\b", markdown)
            )
            graphical = module.GRAPHICAL_DIR / f"{key}.json"
            module.self_check(
                config, markdown, workbook, session_count, graphical
            )

    def test_review_controls_cover_all_eighteen_topics(self) -> None:
        samples = {
            1: "four priorities are not its seven global targets",
            2: "NDMA is not NEC",
            3: "Participation is not consultation",
            4: "Observation is not forecast",
            5: "Magnitude is not intensity",
            6: "warning is not evacuation",
            7: "shelter capacity is not occupancy",
            8: "Heavy rainfall is not automatically an urban flood",
            9: "heat-wave criteria are not one universal temperature",
            10: "glacial lake growth is not a GLOF event",
            11: "Hotspot is not confirmed fire",
            12: "on-site plan is not off-site plan",
            13: "Case is not outbreak",
            14: "restored output is not resilience outcome",
            15: "adaptation is not synonymous with DRR",
            16: "allocation is not release",
            17: "NDRF is not NDMA",
            18: "capacity is not deployment",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_disaster_precision_and_cross_ownership(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Risk boundary",
            "Cycle boundary",
            "Law/status boundary",
            "Institutional boundary",
            "Warning boundary",
            "Finance/data boundary",
            "Environment Topic 26",
            "Internal Security",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_answer_contract_is_exam_executable_and_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse India's disaster-risk governance. Answer in 250 words.
**Model thesis:** Risk reduction requires prevention, capacity and accountability.
**Claim → named evidence → analysis → qualification:**
- A named Indian law and institution demonstrate mandate and process.
**Qualified conclusion:** Resilience requires measured implementation.

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
        self.assertIn("hazard -> exposure/vulnerability/capacity", repaired)
        self.assertIn("source/date/unit/status", repaired)

    def test_allocation_reloads_all_three_trackers_with_null_review_state(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation = source[
            source.index("def allocate(") : source.index(
                "def section(", source.index("def allocate(")
            )
        ]
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", allocation)
        self.assertIn("old, master_row, review_row = live_identity(topic)", allocation)
        self.assertIn('"scores": None', source)
        self.assertIn('"hard_gates": None', source)

    def test_publication_inventory_and_counts_are_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn("selected_keys=None", source)
        self.assertIn("full_count = len(live_ids)", source)
        self.assertIn(
            "master_ids == live_ids == review_ids == manifest_ids", source
        )
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn(
            "changed-file inventory contains missing paths", source
        )

    def test_driver_is_static_subprocess_backed_and_not_recursively_wrapped(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertNotIn("exec(compile(", source)
        self.assertNotIn("_prior_main", source)
        self.assertNotIn("def load_tests(", source)
        self.assertNotIn("def _run_subject_review(", source)
        self.assertIn(
            '[sys.executable, "-m", "unittest", "-v", module]', source
        )


if __name__ == "__main__":
    unittest.main()
