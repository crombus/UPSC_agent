"""Focused tests for the Environment and Ecology immutable deep-review driver."""

from __future__ import annotations

import unittest
from pathlib import Path

import regenerate_environment_and_ecology_deep_review as deep


class EnvironmentAndEcologyDeepReviewTests(unittest.TestCase):
    def test_manifest_order_scope_and_provenance_owners_are_exact(self) -> None:
        topics = deep.topics()
        self.assertEqual(28, len(topics))
        self.assertEqual(
            [f"environment-and-ecology-{number:02d}" for number in range(1, 29)],
            [topic.topic_key for topic in topics],
        )
        for topic in topics:
            self.assertGreater(topic.basic_path.stat().st_size, 1)
            self.assertGreater(topic.canonical_path.stat().st_size, 1)
            self.assertGreater(topic.advanced_path.stat().st_size, 1)
            self.assertNotEqual(topic.basic_path, topic.canonical_path)

    def test_review_controls_cover_all_twenty_eight_topics(self) -> None:
        samples = {
            1: "standing crop biomass is not standing state",
            2: "only the energy pyramid is necessarily upright",
            3: "biome is not ecosystem",
            4: "hotspot is not a statutory protected area",
            5: "IUCN category is not Wildlife Protection Act schedule",
            6: "eco-sensitive zone is not a protected area",
            7: "Montreux Record is not the Ramsar List",
            8: "pre-2022 six-schedule memory",
            9: "Appendix I is not a universal trade ban",
            10: "CMS is not CITES",
            11: "Forest cover is not recorded forest area",
            12: "fund collection is not expenditure or restoration",
            13: "Emission is not ambient concentration or exposure",
            14: "BOD is not COD",
            15: "EPR registration or certificate is not physical recycling",
            16: "Terms of Reference are not clearance",
            17: "emission flow is not concentration stock",
            18: "scenario is not forecast",
            19: "Kyoto commitment is not Paris NDC",
            20: "Panchamrit political announcement is not identical",
            21: "avoidance is not removal",
            22: "Basel waste controls are not Stockholm chemical listings",
            23: "Desertification is not desert expansion",
            24: "blue economy is not unrestricted ocean extraction",
            25: "Capacity in MW is not generation in MWh",
            26: "Sendai priorities are not its seven global targets",
            27: "scientific advice is not statutory clearance",
            28: "rediscovery is not discovery",
        }
        by_number = {topic.number: topic for topic in deep.topics()}
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(by_number[number]))

    def test_contract_enforces_environment_precision(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Ecology boundary",
            "Species boundary",
            "Law/status boundary",
            "Treaty boundary",
            "Climate boundary",
            "Pollution boundary",
            "IUCN category never substitutes",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_topic_26_preserves_dedicated_disaster_ownership(self) -> None:
        topic = deep.topics()[25]
        paths = {deep.rel(path) for path in topic.cross_topic_sources}
        for owner in deep.DISASTER_OWNERS:
            self.assertIn(deep.rel(owner), paths)
        contract = deep.source_contract(topic, {"provenance": {}})
        self.assertIn("dedicated Disaster Management cross-owners", contract)

    def test_every_environment_generator_test_is_wired(self) -> None:
        self.assertEqual(25, len(deep.ENVIRONMENT_AND_ECOLOGY_TEST_MODULES))
        self.assertEqual(
            "test_generate_environment_and_ecology_25_28_sequential",
            deep.ENVIRONMENT_AND_ECOLOGY_TEST_MODULES[-1],
        )

    def test_answer_contract_is_exam_executable_and_specific(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse a conservation instrument. Answer in 250 words.
**Model thesis:** Conservation requires mechanism, authority and monitored outcome.
**Claim → named evidence → analysis → qualification:**
- A named Indian statute demonstrates the institution and implementation route.
**Qualified conclusion:** Outcomes depend on ecological fit and accountable enforcement.

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
        self.assertIn("ecological mechanism and scale", repaired)
        self.assertIn("named law/institution/treaty/species", repaired)

    def test_review_lines_and_paths_are_windows_safe(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_live_tracker_scope_is_twenty_four_or_twenty_eight(self) -> None:
        review = deep.load(deep.REVIEW_TRACKER)
        rows = [
            row
            for row in review["topics"]
            if row["topic_key"].startswith("environment-and-ecology-")
        ]
        self.assertIn(len(rows), (24, 28))
        if len(rows) == 28 and all(row["status"] == "pending" for row in rows):
            self.assertTrue(all(row["scores"]["total"] is None for row in rows))
            self.assertTrue(
                all(value is None for row in rows for value in row["hard_gates"].values())
            )

    def test_allocation_and_prepublication_are_race_safe(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        allocation_base = Path(deep.__file__).with_name(
            "regenerate_ancient_history_deep_review.py"
        ).read_text(encoding="utf-8")
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", allocation_base)
        prepublish = source[
            source.index("def _publish_complete_live_library")
            : source.index("_prior_main = main")
        ]
        self.assertIn("selected_keys=None", prepublish)
        self.assertIn("complete live key set", prepublish)
        self.assertIn("fresh REVIEW identity inherited review state", prepublish)
        self.assertNotIn("selected_keys = list(master", prepublish)

    def test_full_library_count_and_identity_guards_are_dynamic(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn("full_count = len(live_ids)", source)
        self.assertIn('final_manifest["topic_count"]', source)
        self.assertIn('final_validation["topic_count"]', source)
        self.assertIn("master_ids == live_ids", source)
        self.assertIn("review_ids == live_ids", source)
        self.assertNotIn("343-topic", source)

    def test_inventory_is_utf8_nul_safe_and_verifies_paths(self) -> None:
        source = Path(deep.__file__).read_text(encoding="utf-8")
        self.assertIn('path.encode("utf-8") + b"\\0"', source)
        self.assertIn('payload.endswith(b"\\0")', source)
        self.assertIn("changed-file inventory contains missing paths", source)


if __name__ == "__main__":
    unittest.main()
