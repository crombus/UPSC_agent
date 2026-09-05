"""Shared assertions for Governance sequential generator tests."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Sequence
from unittest import TestCase

import generate_governance_common as common
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
) -> None:
    case.assertEqual(list(expected_keys), [item["key"] for item in generator.TOPICS])
    case.assertEqual(
        list(expected_titles),
        [item["title"] for item in generator.TOPICS],
    )
    case.assertEqual("2026-09-02", generator.DATE)
    case.assertTrue(generator.SECTION_MANIFEST.is_file())
    case.assertIn(
        "UPSC Mains 2025 GS Paper 2.pdf",
        [path.name for path in generator.LOCAL_BOOKS],
    )
    case.assertIn(
        "02 UPSC 2024 Paper-II.pdf",
        [path.name for path in generator.LOCAL_BOOKS],
    )
    case.assertTrue(all(path.is_file() for path in generator.LOCAL_BOOKS))
    manifest = json.loads(generator.SECTION_MANIFEST.read_text(encoding="utf-8"))
    case.assertEqual("Governance", manifest["subject"]["key"])
    case.assertEqual(
        [f"governance-{number:02d}" for number in range(1, 17)],
        [item["topic_key"] for item in manifest["topics"]],
    )

    specs = ascii_master.normalize_manual_spec_file(generator.ASCII_PATH)
    case.assertEqual(set(expected_keys), set(specs))
    case.assertIn(generator.ASCII_PATH.name, ascii_master.MANUAL_SPEC_FILENAMES)
    payload = json.loads(generator.ASCII_PATH.read_text(encoding="utf-8"))
    case.assertEqual("2026-09-02", payload["generated_on"])
    case.assertTrue(payload["constraints"]["manual_topic_specific"])
    case.assertTrue(payload["constraints"]["tracker_untouched"])

    for config in generator.TOPICS:
        key = str(config["key"])
        case.assertEqual(20, len(config["facts"]), key)
        case.assertEqual(20, len({label for label, _ in config["facts"]}), key)
        case.assertGreaterEqual(len(config["traps"]), 12, key)
        case.assertEqual([10, 10, 15, 15, 20, 20], [m[0] for m in config["mains"]], key)
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
        case.assertEqual(EXPECTED_H2, [item for item in headings if item in EXPECTED_H2])
        case.assertEqual("CONSOLIDATED REGISTER NOTES", headings[-1])

        register = markdown.split("## CONSOLIDATED REGISTER NOTES", 1)[1]
        for heading in common.REGISTER_HEADINGS:
            case.assertIn(f"{config['title']}: {heading}", register, key)
        case.assertGreater(
            register.rfind("COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"),
            max(register.rfind(item) for item in common.REGISTER_HEADINGS),
            key,
        )

        basic_block = markdown.split(EXPECTED_H2[0], 1)[1].split(EXPECTED_H2[1], 1)[0]
        advanced_block = markdown.split(EXPECTED_H2[3], 1)[1].split(EXPECTED_H2[4], 1)[0]
        for owner_key, block in (("basic", basic_block), ("advanced", advanced_block)):
            owner = Path(config[owner_key]).read_text(encoding="utf-8")
            for heading in re.findall(r"(?m)^## (.+?)\s*$", owner):
                case.assertIn(heading, block, f"{key}:{owner_key}:{heading}")

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
        case.assertEqual(Path(config["canonical"]).read_text(encoding="utf-8"), markdown)

        graphical_path = generator.GRAPHICAL_DIR / f"{key}.json"
        graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
        case.assertEqual(13, len(graphical["stages"]), key)
        case.assertEqual(key, graphical["topic_key"])
        case.assertEqual("Governance", graphical["subject"], key)

        spec = specs[key]
        case.assertEqual(12, len(spec.panels), key)
        expected_fragment = ascii_master.build_manual_fragment(spec)
        case.assertIn(expected_fragment, markdown, key)
        for item in spec.panels:
            case.assertTrue(item.source_references, key)
            case.assertGreaterEqual(
                len([line for line in item.body.splitlines() if line.strip()]),
                4,
                key,
            )
            case.assertTrue(all(len(line) <= 100 for line in item.body.splitlines()), key)
            case.assertNotRegex(item.body, r"(?i)\bkey terms\b|\.{3}|…")

        generation = common.EXPORT_DIR / f"{key}-new-topic-2026-09-02.json"
        record = json.loads(generation.read_text(encoding="utf-8"))
        case.assertEqual(1, record["generation"])
        case.assertEqual("2026-09-02", record["generation_date"])
        case.assertIsNone(record["supersedes"])
        case.assertTrue(record["tracker_untouched"])
        case.assertNotIn("notes_pdf", record)
        case.assertNotIn("workbook_pdf", record)
        case.assertIn(
            "books\\mains\\UPSC Mains 2025 GS Paper 2.pdf",
            record["local_ocr_sources"],
        )
        case.assertIn(
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
            record["pyq_indexes"],
        )
        generator.self_check(config, markdown, workbook, 15, graphical_path)


def assert_no_publish_side_effects(case: TestCase, generator: object) -> None:
    source = Path(generator.__file__).read_text(encoding="utf-8")
    for forbidden in (
        "markdown_learning_pdf",
        "finalize_v2_topic",
        "generate_export_command_index",
        "EXPORT-PDF-STATUS.json",
    ):
        case.assertNotIn(forbidden, source)
