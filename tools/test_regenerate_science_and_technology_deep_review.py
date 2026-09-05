"""Focused tests for the Science and Technology immutable deep-review driver."""

from __future__ import annotations

import unittest
from pathlib import Path

import regenerate_science_and_technology_deep_review as deep


class ScienceAndTechnologyDeepReviewTests(unittest.TestCase):
    def test_manifest_order_scope_and_provenance_owners_are_exact(self) -> None:
        topics = deep.topics()
        self.assertEqual(26, len(topics))
        self.assertEqual(
            [f"science-and-technology-{number:02d}" for number in range(1, 27)],
            [topic.topic_key for topic in topics],
        )
        for topic in topics:
            self.assertGreater(topic.basic_path.stat().st_size, 1)
            self.assertGreater(topic.canonical_path.stat().st_size, 1)
            self.assertGreater(topic.advanced_path.stat().st_size, 1)
            self.assertNotEqual(topic.basic_path, topic.canonical_path)

    def test_review_controls_cover_all_twenty_six_topics(self) -> None:
        samples = {
            1: "payload mass is not mission outcome",
            2: "NavIC is India's regional satellite-navigation system",
            3: "abort test is not an orbital uncrewed mission",
            4: "a programme target is not an achieved stage outcome",
            5: "ITER is not a commercial generator",
            6: "tested is not inducted",
            7: "AoN is not contract",
            8: "UPI is not a wallet or settlement bank",
            9: "Model is not application",
            10: "Qubit is not a faster classical bit",
            11: "fab is not ATMP",
            12: "notified rule is not draft rule",
            13: "Biotechnology is not only genetic engineering",
            14: "contained use is not environmental release",
            15: "emergency authorisation is not full approval",
            16: "Nanoscale is not automatically novel or safer",
            17: "filing is not grant",
            18: "kW is not kWh",
            19: "Drone is not necessarily autonomous",
            20: "Critical is not necessarily rare",
            21: "energy is not power",
            22: "strength is not concentration",
            23: "pathogen is not disease",
            24: "Funder is not research performer",
            25: "IaaS is not PaaS or SaaS",
            26: "nomination is not award",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_science_precision(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "System boundary",
            "Technical boundary",
            "Status boundary",
            "Data boundary",
            "Governance boundary",
            "PYQ contract",
            "Dual-flow contract",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_real_generator_suites_are_enumerated(self) -> None:
        self.assertEqual(
            (
                "test_generate_science_and_technology_01_05_sequential",
                "test_generate_science_and_technology_06_10_sequential",
            ),
            deep.SCIENCE_AND_TECHNOLOGY_TEST_MODULES,
        )
        for module in deep.SCIENCE_AND_TECHNOLOGY_TEST_MODULES:
            self.assertTrue((deep.ROOT / "tools" / f"{module}.py").is_file())

    def test_answer_contract_is_exam_executable_and_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse an Indian technology mission. Answer in 250 words.
**Model thesis:** Capability requires mechanism, institution and verified status.
**Model answer:** A mission must be assessed through mechanism, institution, status and limits.
**Claim → named evidence → analysis → qualification:**
- A named Indian mission demonstrates its operating chain and maturity boundary.
**Qualified conclusion:** Outcomes depend on validation and accountable deployment.

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
        self.assertIn("exact technical mechanism", repaired)
        self.assertIn("named mission/institution/platform", repaired)

    def test_review_lines_and_paths_are_windows_safe(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_ascii_finalizer_injects_science_controls(self) -> None:
        topic = deep.topics()[0]
        record = deep.latest(deep.load(deep.STATUS), topic.topic_key)
        spec = deep.build_ascii_spec(
            topic,
            record,
            99,
            deep.repo(record["markdown"]).read_text(encoding="utf-8"),
            topic.canonical_path,
        )
        text = "\n".join(
            line
            for panel in spec["topics"][0]["panels"]
            for line in panel["ascii_lines"]
        )
        for label in ("MUST REMEMBER:", "CLOSE DISTINCTION:", "EVIDENCE LIMIT:"):
            self.assertIn(label, text)

    def test_live_tracker_scope_is_fourteen_or_twenty_six(self) -> None:
        review = deep.load(deep.REVIEW_TRACKER)
        rows = [
            row
            for row in review["topics"]
            if row["topic_key"].startswith("science-and-technology-")
            and int(row["topic_key"].rsplit("-", 1)[1]) <= 26
        ]
        self.assertIn(len(rows), (14, 26))
        new_rows = [
            row
            for row in rows
            if int(row["topic_key"].rsplit("-", 1)[1]) >= 15
        ]
        if len(rows) == 26 and all(row["status"] == "pending" for row in new_rows):
            self.assertTrue(all(row["scores"]["total"] is None for row in new_rows))
            self.assertTrue(
                all(
                    value is None
                    for row in new_rows
                    for value in row["hard_gates"].values()
                )
            )

    def test_allocation_reloads_all_three_trackers(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation = source[
            source.index("def allocate(") : source.index("def section(", source.index("def allocate("))
        ]
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", allocation)
        self.assertIn("old, master_row, review_row = live_identity(topic)", allocation)

    def test_publication_is_complete_and_race_safe(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        prepublish = source[source.rindex("def _publish_before_tracker_sync_when_needed") :]
        self.assertIn("selected_keys=None", source)
        self.assertIn("complete live key set", source)
        self.assertIn("fresh REVIEW identity inherited", source)
        self.assertIn("science-and-technology-live-status-snapshot", source)
        self.assertIn("expected[14:]", prepublish)

    def test_full_library_and_inventory_guards_are_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn("full_count = len(live_ids)", source)
        self.assertIn('final_manifest["topic_count"]', source)
        self.assertIn("master_ids == live_ids == review_ids == manifest_ids", source)
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("changed-file inventory contains missing paths", source)

    def test_driver_is_static_and_unittests_are_subprocess_backed(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertNotIn("exec(compile(", source)
        self.assertNotIn("_prior_main =", source)
        self.assertIn("[sys.executable, \"-m\", \"unittest\", \"-v\", module]", source)


if __name__ == "__main__":
    unittest.main()
