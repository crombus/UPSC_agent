"""Regression tests for Economy learner-v2 Topics 11-15."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import generate_economy_common as common  # noqa: E402
import generate_economy_11_sequential as economy11  # noqa: E402
import generate_economy_12_sequential as economy12  # noqa: E402
import generate_economy_13_sequential as economy13  # noqa: E402
import generate_economy_14_sequential as economy14  # noqa: E402
import generate_economy_15_sequential as economy15  # noqa: E402
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
    generators = [economy11, economy12, economy13, economy14, economy15]

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
            self.assertEqual(False, spec["allow_existing_history"], key)
            generator.self_check(
                config,
                markdown,
                workbook,
                15,
                generator.GRAPHICAL_DIR / f"{key}.json",
            )

    def test_agriculture_policy_boundaries_survive(self) -> None:
        expected = {
            "economy-11": ["Operation Barga", "gross cropped area", "automatic sluice", "semi-dwarf"],
            "economy-12": ["announcement alone", "actual stock", "Entitlement versus offtake", "OMSS"],
            "economy-13": ["electronic trading and price-discovery layer", "producer company", "WDRA", "function remains"],
            "economy-14": ["Created irrigation potential", "basin extraction", "Enrolment and claims", "basis risk"],
            "economy-15": ["standalone warehouse", "installed stock", "actual throughput", "value addition"],
        }
        for generator in self.generators:
            key = str(generator.TOPICS[0]["key"])
            text = (
                generator.SESSION_DIR / f"{key}_Learning-Session.md"
            ).read_text(encoding="utf-8")
            for phrase in expected[key]:
                self.assertIn(phrase, text, key)

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
