"""Regression tests for Economy learner-v2 Topics 20-23."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_economy_common as common  # noqa: E402
import generate_economy_20_sequential as economy20  # noqa: E402
import generate_economy_21_sequential as economy21  # noqa: E402
import generate_economy_22_sequential as economy22  # noqa: E402
import generate_economy_23_sequential as economy23  # noqa: E402
import notions_style_ascii_master as ascii_master  # noqa: E402
import validate_v2_export as validator  # noqa: E402


EXPECTED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]


class EconomySequentialTests(unittest.TestCase):
    generators = [economy20, economy21, economy22, economy23]

    def test_full_contract_for_every_topic(self) -> None:
        manifest = json.loads(common.SECTION_MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(
            [f"economy-{number:02d}" for number in range(1, 32)],
            [item["topic_key"] for item in manifest["topics"]],
        )
        for generator in self.generators:
            config = generator.TOPICS[0]
            key = str(config["key"])
            markdown = (
                generator.SESSION_DIR / f"{key}_Learning-Session.md"
            ).read_text(encoding="utf-8")
            workbook = (
                generator.SESSION_DIR / f"{key}_Solved-Workbook.md"
            ).read_text(encoding="utf-8")
            self.assertEqual(20, len(config["facts"]), key)
            self.assertEqual(15, len(config["session_plans"]), key)
            covered = {
                index
                for _title, indexes, _caution, _route in config["session_plans"]
                for index in indexes
            }
            self.assertEqual(set(range(20)), covered, key)
            self.assertEqual(15, markdown.count("#### VISUAL FIRST"), key)
            self.assertEqual(80, len(re.findall(r"(?m)^### Q\d+\. ", markdown)), key)
            self.assertEqual(
                list("ABCD") * 20,
                re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown),
                key,
            )
            self.assertEqual(
                list("ABCD") * 20,
                re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook),
                key,
            )
            self.assertEqual([10, 10, 15, 15, 20, 20], [m[0] for m in config["mains"]], key)
            self.assertEqual(6, markdown.count("### ORIGINAL MAINS"), key)
            headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
            self.assertEqual(EXPECTED_H2, [h for h in headings if h in EXPECTED_H2], key)
            self.assertEqual("CONSOLIDATED REGISTER NOTES", headings[-1], key)
            self.assertEqual(12, markdown.count("```ascii-master"), key)
            specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
            self.assertEqual([key], list(specs), key)
            self.assertEqual(12, len(specs[key].panels), key)
            self.assertIn(generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES)
            for item in specs[key].panels:
                self.assertTrue(item.source_references, key)
                self.assertTrue(
                    all(len(line) <= 100 for line in item.body.splitlines()),
                    f"{key}:{item.title}",
                )
                self.assertNotRegex(item.body, r"(?i)\bkey terms\b|\.{3}|…")
            graphical = json.loads(
                (generator.GRAPHICAL_DIR / f"{key}.json").read_text(encoding="utf-8")
            )
            self.assertEqual(13, len(graphical["stages"]), key)
            self.assertEqual("Economy", graphical["subject"], key)
            self.assertEqual(
                Path(config["canonical"]).read_text(encoding="utf-8"),
                markdown,
                key,
            )
            spec = json.loads(
                (generator.EXPORT_DIR / f"{key}-new-topic-2026-09-03.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertTrue(spec["tracker_untouched"], key)
            self.assertFalse(spec["allow_existing_history"], key)
            generator.self_check(
                config,
                markdown,
                workbook,
                15,
                generator.GRAPHICAL_DIR / f"{key}.json",
            )

    def test_measurement_and_status_boundaries_survive(self) -> None:
        expected = {
            "economy-20": ["bound tariff", "signed, ratified", "TRIMS", "December 2019"],
            "economy-21": ["reserve tranche position", "World Bank Group", "Common Framework", "Nature Solutions Finance Hub"],
            "economy-22": ["unemployment rate", "21 November 2025", "May 2026", "certification count is not"],
            "economy-23": ["poverty gap", "MPI equals H", "projected", "allocation, release"],
        }
        for generator in self.generators:
            key = str(generator.TOPICS[0]["key"])
            text = (
                generator.SESSION_DIR / f"{key}_Learning-Session.md"
            ).read_text(encoding="utf-8")
            for phrase in expected[key]:
                self.assertIn(phrase, text, key)

    def test_verified_pyq_concepts_are_in_basic_and_practice(self) -> None:
        expected = {
            "economy-20": ["International Grains Council", "TRIMS"],
            "economy-21": ["Nature Solutions Finance Hub", "reserve tranche position"],
            "economy-22": ["care economy", "structural unemployment"],
            "economy-23": ["financial inclusion", "social services"],
        }
        for generator in self.generators:
            key = str(generator.TOPICS[0]["key"])
            text = (
                generator.SESSION_DIR / f"{key}_Learning-Session.md"
            ).read_text(encoding="utf-8")
            basic, practice = text.split("## BASIC MCQS / REMEDIATION", 1)
            for phrase in expected[key]:
                self.assertIn(phrase.casefold(), basic.casefold(), key)
                self.assertIn(phrase.casefold(), practice.casefold(), key)

    def test_deep_quality_has_no_high_defects(self) -> None:
        for generator in self.generators:
            key = str(generator.TOPICS[0]["key"])
            text = (
                generator.SESSION_DIR / f"{key}_Learning-Session.md"
            ).read_text(encoding="utf-8")
            audit = validator.deep_content_quality_audit_text(text, topic_key=key)
            high = [
                item
                for item in audit["defects"]
                if item.get("severity") in {"blocker", "high"}
            ]
            self.assertEqual([], high, key)


if __name__ == "__main__":
    unittest.main()
