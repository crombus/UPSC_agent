"""Focused and aggregate tests for the Geography Part A deep-review driver."""

from __future__ import annotations

import importlib
import unittest
from pathlib import Path

import regenerate_geography_part_a_deep_review as deep


GENERATOR_TEST_MODULES = (
    "test_generate_geography_05_06_sequential",
    "test_generate_geography_07_08_sequential",
    "test_generate_geography_09_sequential",
    "test_generate_geography_10_11_sequential",
    "test_generate_geography_12_13_sequential",
    "test_generate_geography_14_sequential",
    "test_generate_geography_15_16_sequential",
    "test_generate_geography_17_18_sequential",
    "test_generate_geography_19_sequential",
    "test_generate_geography_20_sequential",
    "test_generate_geography_21_sequential",
    "test_generate_geography_22_sequential",
    "test_generate_geography_23_sequential",
    "test_generate_geography_24_sequential",
    "test_generate_geography_25_sequential",
)


def load_tests(
    loader: unittest.TestLoader,
    tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    suite = unittest.TestSuite([tests])
    for name in GENERATOR_TEST_MODULES:
        suite.addTests(loader.loadTestsFromModule(importlib.import_module(name)))
    return suite


class GeographyPartADeepReviewTests(unittest.TestCase):
    def test_manifest_order_is_exact_01_to_25(self) -> None:
        topics = deep.topics()
        self.assertEqual(25, len(topics))
        self.assertEqual(
            [f"geography-{number:02d}" for number in range(1, 26)],
            [topic.topic_key for topic in topics],
        )

    def test_process_spatial_and_causal_controls_cover_sequence(self) -> None:
        samples = {
            1: "82°30′E standard meridian",
            5: "graded-profile adjustment",
            12: "Ekman transport",
            16: "Mascarene High",
            25: "Arctic is mainly an ocean",
        }
        for number, phrase in samples.items():
            self.assertIn(phrase, deep._review_block(deep.topics()[number - 1]))

    def test_close_option_firewalls_are_explicit(self) -> None:
        checks = {
            3: "Magnitude measures source size whereas intensity records effects",
            4: "porosity from permeability",
            9: "Ramsar designation is international recognition",
            12: "spring/neap are alignment effects",
            14: "climate region differs from vegetation biome",
        }
        for number, phrase in checks.items():
            self.assertIn(phrase, deep._review_block(deep.topics()[number - 1]))

    def test_review_lines_fit_ascii_master(self) -> None:
        for topic in deep.topics():
            lines = deep._wrapped_review_lines(topic)
            self.assertTrue(lines)
            self.assertLessEqual(max(map(len, lines)), 100)

    def test_ascii_panels_keep_one_authored_body_field(self) -> None:
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
                1,
                sum(key in panel for key in ("ascii_text", "ascii_lines")),
            )

    def test_paths_remain_windows_safe(self) -> None:
        for topic in deep.topics():
            paths = deep.review_paths(topic, 99)
            for key in ("markdown", "workbook_markdown", "main_pdf", "workbook_pdf"):
                self.assertLess(len(str(paths[key].resolve())), 260)

    def test_answer_contract_is_exam_executable(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION
## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE

### ORIGINAL MAINS 1 — 15 MARKS
**Question:** Analyse the process and spatial pattern. Answer in 250 words.
**Model thesis:** The pattern emerges through interacting physical controls.
**Claim → named evidence → analysis → qualification:**
- A named Indian region demonstrates the mechanism at basin scale.
**Qualified conclusion:** The cause is strong but neither sufficient nor uniform.

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

    def test_contract_enforces_process_map_status_and_approval(self) -> None:
        contract = deep.source_contract(deep.topics()[0], {"provenance": {}})
        for phrase in (
            "Initial condition",
            "Map discipline",
            "official source, observation date and status boundary",
            "approved: false",
        ):
            self.assertIn(phrase, contract)

    def test_visual_gateway_is_added_to_each_named_session(self) -> None:
        source = """# Topic

## BASIC LEARNING SESSION

### SESSION 1 — TEST PROCESS

#### DEFINITION / WHAT THIS IS CALLED

Definition.

## BASIC MCQS / REMEDIATION
## PYQS AND ANSWER PRACTICE
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER
## CONSOLIDATED REGISTER NOTES
"""
        repaired = deep.insert_contract(source, deep.topics()[0], {"provenance": {}})
        self.assertEqual(1, repaired.count("#### VISUAL FIRST"))
        self.assertIn("INITIAL CONDITION / DRIVER", repaired)

    def test_allocation_rereads_live_manifest_and_shared_state(self) -> None:
        source = deep.GEOGRAPHY_PATTERN_PATH.read_text(encoding="utf-8")
        inherited = Path(deep._BASE).read_text(encoding="utf-8")
        self.assertIn("load(SECTION_MANIFEST)", inherited)
        self.assertIn("Re-read EXPORT, MASTER and REVIEW immediately", inherited)
        self.assertIn("_publish_before_tracker_sync_when_needed", source)

    def test_inventory_is_utf8_nul_terminated(self) -> None:
        source = deep.GEOGRAPHY_PATTERN_PATH.read_text(encoding="utf-8")
        self.assertIn('b"\\0"', source)
        self.assertIn('encode("utf-8")', source)
        self.assertIn('endswith(b"\\0")', source)

    def test_full_library_count_is_dynamic(self) -> None:
        source = deep.GEOGRAPHY_PATTERN_PATH.read_text(encoding="utf-8")
        section = source[source.index("def _republish_master_library") :]
        section = section[: section.index("def _rewrite_command_history")]
        self.assertIn("count = len(selected_keys)", section)
        self.assertNotIn("259", section)


if __name__ == "__main__":
    unittest.main()
