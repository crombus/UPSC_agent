"""Shared assertions for Science and Technology sequential generators."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Sequence
from unittest import TestCase

import generate_science_and_technology_common as common
import notions_style_ascii_master as ascii_master


EXPECTED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]


def session_markdown(generator: object, key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(encoding="utf-8")


def assert_topic_contract(
    case: TestCase,
    generator: object,
    expected_key: str,
    expected_title: str,
    expected_generation: int,
) -> None:
    case.assertEqual([expected_key], [item["key"] for item in generator.TOPICS])
    case.assertEqual([expected_title], [item["title"] for item in generator.TOPICS])
    case.assertEqual("2026-09-03", generator.DATE)
    manifest = json.loads(generator.SECTION_MANIFEST.read_text(encoding="utf-8"))
    case.assertEqual("Science-and-Technology", manifest["subject"]["key"])
    case.assertEqual(
        [f"science-and-technology-{number:02d}" for number in range(1, 27)],
        [item["topic_key"] for item in manifest["topics"]],
    )

    specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
    case.assertEqual({expected_key}, set(specs))
    case.assertIn(generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES)
    config = generator.TOPICS[0]
    case.assertEqual(20, len(config["facts"]))
    case.assertEqual(20, len({label for label, _ in config["facts"]}))
    case.assertEqual(15, len(config["session_plans"]))
    case.assertEqual(
        set(range(20)),
        {
            index
            for _title, indexes, _caution, _route in config["session_plans"]
            for index in indexes
        },
    )
    case.assertEqual([10, 10, 15, 15, 20, 20], [item[0] for item in config["mains"]])

    markdown = session_markdown(generator, expected_key)
    workbook = (
        generator.SESSION_DIR / f"{expected_key}_Solved-Workbook.md"
    ).read_text(encoding="utf-8")
    case.assertEqual(15, len(re.findall(r"(?m)^### SESSION \d+ — .+? — .+?\s*$", markdown)))
    case.assertEqual(15, markdown.count("#### VISUAL FIRST"))
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    case.assertEqual(EXPECTED_H2, [item for item in headings if item in EXPECTED_H2])
    case.assertEqual("CONSOLIDATED REGISTER NOTES", headings[-1])
    case.assertIn("### COMPLETE BASIC OWNER EVIDENCE BANK", markdown)
    case.assertIn("### LIVE OFFICIAL-SOURCE ATTEMPT LOG", markdown)
    case.assertEqual(80, len(re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)))
    case.assertEqual(80, len(set(re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown))))
    case.assertEqual(80, len(re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)))
    case.assertEqual(
        list("ABCD") * 20,
        re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown),
    )
    case.assertEqual(
        list("ABCD") * 20,
        re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook),
    )
    case.assertEqual(6, markdown.count("### ORIGINAL MAINS"))
    case.assertEqual(12, markdown.count("```ascii-master"))
    case.assertNotRegex(markdown, r"(?i)\b(?:todo|placeholder|lorem ipsum)\b")
    case.assertEqual(Path(config["canonical"]).read_text(encoding="utf-8"), markdown)

    spec = specs[expected_key]
    case.assertEqual(12, len(spec.panels))
    case.assertIn(ascii_master.build_manual_fragment(spec), markdown)
    for item in spec.panels:
        case.assertTrue(item.source_references)
        case.assertGreaterEqual(
            len([line for line in item.body.splitlines() if line.strip()]), 4
        )
        case.assertTrue(all(len(line) <= 100 for line in item.body.splitlines()))
        case.assertNotRegex(item.body, r"(?i)\bkey terms\b|\.{3}|…")

    graphical = json.loads(
        (generator.GRAPHICAL_DIR / f"{expected_key}.json").read_text(encoding="utf-8")
    )
    case.assertEqual(13, len(graphical["stages"]))
    case.assertEqual("Science-and-Technology", graphical["subject"])
    generation = json.loads(
        (
            common.EXPORT_DIR / f"{expected_key}-new-topic-2026-09-03.json"
        ).read_text(encoding="utf-8")
    )
    case.assertEqual(expected_generation, generation["generation"])
    case.assertEqual(expected_generation, generation["expected_generation"])
    case.assertTrue(generation["tracker_untouched"])
    case.assertNotIn("notes_pdf", generation)
    case.assertNotIn("workbook_pdf", generation)
    generator.self_check(config, markdown, workbook, 15, generator.GRAPHICAL_DIR / f"{expected_key}.json")


def assert_no_publish_side_effects(case: TestCase, generator: object) -> None:
    source = Path(generator.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "markdown_learning_pdf",
        "finalize_v2_topic",
        "generate_export_command_index",
        "EXPORT-PDF-STATUS.json",
    ):
        case.assertNotIn(forbidden, source)
