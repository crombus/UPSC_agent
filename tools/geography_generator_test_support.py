"""Shared assertions for Geography Topics 05-19 sequential generators."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Sequence
from unittest import TestCase

import generate_geography_common as common
import notions_style_ascii_master as ascii_master


EXPECTED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]


def session_markdown(generator: object, key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Learning-Session.md").read_text(
        encoding="utf-8"
    )


def workbook_markdown(generator: object, key: str) -> str:
    return (generator.SESSION_DIR / f"{key}_Solved-Workbook.md").read_text(
        encoding="utf-8"
    )


def assert_batch_contract(
    case: TestCase,
    generator: object,
    expected_keys: Sequence[str],
    expected_titles: Sequence[str],
    *,
    expected_section: str = "Part-A-Physical-Geography",
    expected_section_key: str = "part-a-physical-geography",
    expected_generation: int = 2,
    expected_supersedes_template: str | None = "{key}:legacy-v1:g1",
    expect_allow_existing_history: bool = False,
) -> None:
    case.assertEqual(list(expected_keys), [item["key"] for item in generator.TOPICS])
    case.assertEqual(list(expected_titles), [item["title"] for item in generator.TOPICS])
    case.assertEqual("2026-09-01", generator.DATE)
    case.assertEqual("Geography", generator.SUBJECT)
    case.assertEqual(expected_section, generator.SECTION)
    case.assertTrue(generator.SECTION_MANIFEST.is_file())
    case.assertEqual(
        {
            "GC Leong - Certificate Physical and human Geography.pdf",
            "Indian & World Geography - Husain, Majid_Compressed.pdf",
            "Indian-geography-majid-hussain.pdf",
        },
        {path.name for path in generator.LOCAL_BOOKS},
    )

    manifest = json.loads(generator.SECTION_MANIFEST.read_text(encoding="utf-8"))
    case.assertEqual("Geography", manifest["subject"]["key"])
    case.assertEqual(expected_section_key, manifest["section"]["key"])

    specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
    case.assertEqual(set(expected_keys), set(specs))
    case.assertTrue(generator.ASCII_PATH.is_file())
    payload = json.loads(generator.ASCII_PATH.read_text(encoding="utf-8"))
    case.assertEqual("2026-09-01", payload["generated_on"])
    case.assertTrue(payload["constraints"]["manual_topic_specific"])
    case.assertTrue(payload["constraints"]["tracker_untouched"])

    for config in generator.TOPICS:
        key = str(config["key"])
        case.assertEqual(20, len(config["facts"]), key)
        case.assertEqual(20, len({label for label, _ in config["facts"]}), key)
        case.assertGreaterEqual(len(config["traps"]), 12, key)
        case.assertEqual(
            [10, 10, 15, 15, 20, 20],
            [item[0] for item in config["mains"]],
            key,
        )
        case.assertEqual(15, len(config["session_plans"]), key)
        covered = {
            index
            for _title, indexes, _caution, _exam_use in config["session_plans"]
            for index in indexes
        }
        case.assertEqual(set(range(20)), covered, key)

        markdown = session_markdown(generator, key)
        workbook = workbook_markdown(generator, key)
        sessions = re.findall(
            r"(?m)^### SESSION (\d+) — (.+?) — (.+?)\s*$",
            markdown,
        )
        case.assertEqual(15, len(sessions), key)
        case.assertEqual(15, markdown.count("#### VISUAL FIRST"), key)
        case.assertIn("### COMPLETE BASIC OWNER EVIDENCE BANK", markdown)
        headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
        case.assertEqual(
            EXPECTED_H2,
            [heading for heading in headings if heading in EXPECTED_H2],
            key,
        )
        case.assertEqual("CONSOLIDATED REGISTER NOTES", headings[-1], key)

        session_stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
        workbook_stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
        case.assertEqual(80, len(session_stems), key)
        case.assertEqual(80, len(set(session_stems)), key)
        case.assertEqual(80, len(workbook_stems), key)
        case.assertEqual(80, len(set(workbook_stems)), key)
        case.assertEqual(
            list("ABCD") * 20,
            re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown),
            key,
        )
        case.assertEqual(
            list("ABCD") * 20,
            re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook),
            key,
        )
        case.assertEqual(6, markdown.count("### ORIGINAL MAINS"), key)
        case.assertEqual(12, markdown.count("```ascii-master"), key)
        case.assertNotRegex(markdown, r"(?i)\b(?:todo|placeholder|lorem ipsum)\b")
        case.assertNotIn("\ufffd", markdown)
        canonical = Path(config["canonical"]).read_text(encoding="utf-8")
        canonical = re.sub(
            r"\n### Semantic-completeness ownership and PYQ control\n"
            r".*?(?=\n## BASIC MCQS / REMEDIATION)",
            "",
            canonical,
            count=1,
            flags=re.S,
        )
        case.assertEqual(canonical, markdown)

        basic = Path(config["basic"]).read_text(encoding="utf-8")
        basic_block = markdown.split(EXPECTED_H2[0], 1)[1].split(EXPECTED_H2[1], 1)[0]
        for heading in re.findall(r"(?m)^## (.+?)\s*$", basic):
            case.assertIn(heading, basic_block, key)

        advanced = Path(config["advanced"]).read_text(encoding="utf-8")
        advanced_block = markdown.split(EXPECTED_H2[3], 1)[1]
        for heading in re.findall(r"(?m)^## (.+?)\s*$", advanced):
            case.assertIn(heading, advanced_block, key)

        graphical_path = generator.GRAPHICAL_DIR / f"{key}.json"
        graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
        case.assertEqual(13, len(graphical["stages"]), key)
        case.assertIn(f"source generation g{expected_generation}", graphical["status"]["line"], key)

        spec = specs[key]
        case.assertEqual(12, len(spec.panels), key)
        for item in spec.panels:
            case.assertTrue(item.source_references, key)
            case.assertGreaterEqual(
                len([line for line in item.body.splitlines() if line.strip()]),
                4,
                key,
            )
            case.assertTrue(
                all(len(line) <= 100 for line in item.body.splitlines()),
                key,
            )
            case.assertNotRegex(item.body, r"(?i)\bkey terms\b|\.{3}|…")

        generation_path = common.EXPORT_DIR / f"{key}-new-topic-2026-09-01.json"
        generation = json.loads(generation_path.read_text(encoding="utf-8"))
        case.assertEqual(expected_generation, generation["generation"], key)
        case.assertEqual("2026-09-01", generation["generation_date"], key)
        case.assertEqual(expected_section, generation["section"], key)
        case.assertEqual(
            (
                expected_supersedes_template.format(key=key)
                if expected_supersedes_template
                else None
            ),
            generation["supersedes"],
            key,
        )
        case.assertTrue(generation["tracker_untouched"], key)
        if expect_allow_existing_history:
            case.assertTrue(generation.get("allow_existing_history"), key)
        else:
            case.assertNotIn("allow_existing_history", generation, key)
        case.assertNotIn("notes_pdf", generation, key)
        case.assertNotIn("workbook_pdf", generation, key)
        generator.self_check(config, markdown, workbook, 15, graphical_path)
