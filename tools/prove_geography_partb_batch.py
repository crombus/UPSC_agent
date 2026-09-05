"""Programmatic per-topic proof for the Geography Part-B learner-v2 batch.

For every topic it independently proves 15 sessions, 80 unique MCQs, an exact
A20/B20/C20/D20 answer distribution, 12 registered manual ASCII panels, 13
graphical stages, the six Mains weights, 20 source-bounded facts, the required
H2 order with consolidated register notes last, full Basic/Advanced owner
heading preservation, and the finalized tracker record with real PDF page
counts.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import notions_style_ascii_master as ascii_master  # noqa: E402


SECTION_KEY = "part-b-human-economic-and-regional-geography"
SESSION_DIR = (
    ROOT / "upsc-ai-kit" / "knowledge" / "Geography" / "learning-sessions" / "v2" / SECTION_KEY
)
SPEC_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
GRAPHICAL_DIR = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "carvaka-graphical-specs" / "Geography"
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
REQUIRED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH \u2014 NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]
TOPICS = [
    ("geography-31", 2, "31_Mineral-Energy-Resources-World-and-India.md"),
    ("geography-33", 1, "33_Transport-Trade-and-Indian-Space-Programme.md"),
    ("geography-34", 1, "34_World-Regional-Geography-Continents-Countries.md"),
    ("geography-35", 1, "35_Indian-Political-Geography-Boundaries-and-Neighbours.md"),
    ("geography-36", 1, "36_Contemporary-Geographical-Issues-India.md"),
    ("geography-37", 1, "37_Cultural-and-Social-Geography-of-India.md"),
]


def prove(topic_key: str, generation: int, owner_name: str) -> dict[str, object]:
    failures: list[str] = []
    markdown = (SESSION_DIR / f"{topic_key}_Learning-Session.md").read_text(encoding="utf-8")
    workbook = (SESSION_DIR / f"{topic_key}_Solved-Workbook.md").read_text(encoding="utf-8")

    sessions = re.findall(r"(?m)^### SESSION (\d+) \u2014 ", markdown)
    if len(sessions) != 15:
        failures.append(f"sessions={len(sessions)}")
    if markdown.count("#### VISUAL FIRST") != 15:
        failures.append("visual-first count is not 15")

    stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
    workbook_stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
    if len(stems) != 80 or len(set(stems)) != 80:
        failures.append(f"mcqs={len(stems)} unique={len(set(stems))}")
    if len(workbook_stems) != 80 or len(set(workbook_stems)) != 80:
        failures.append("workbook MCQ set is not 80 unique questions")

    keys = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown)
    distribution = Counter(keys)
    if keys != list("ABCD") * 20:
        failures.append("MCQ keys are not a strict A-B-C-D cycle")
    if distribution != Counter({"A": 20, "B": 20, "C": 20, "D": 20}):
        failures.append(f"answer distribution={dict(distribution)}")
    if re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook) != list("ABCD") * 20:
        failures.append("workbook MCQ keys are not a strict A-B-C-D cycle")

    weights = [int(value) for value in re.findall(r"(?m)^### ORIGINAL MAINS \d+ \u2014 (\d+) MARKS", markdown)]
    if weights != [10, 10, 15, 15, 20, 20]:
        failures.append(f"mains weights={weights}")

    facts = re.findall(r"(?m)^(\d+)\. \*\*(.+?):\*\* ", markdown.split(REQUIRED_H2[4], 1)[1])
    if len(facts) != 20:
        failures.append(f"register fact anchors={len(facts)}")

    embedded_panels = markdown.count("```ascii-master")
    spec_path = SPEC_DIR / f"{topic_key}-2026-09-01-sequential.json"
    specs = ascii_master.normalize_manual_spec_file(spec_path)
    registered = len(specs[topic_key].panels)
    if embedded_panels != 12 or registered != 12:
        failures.append(f"ascii embedded={embedded_panels} registered={registered}")
    if spec_path.name not in ascii_master.MANUAL_SPEC_FILENAMES:
        failures.append("manual ASCII spec is not registered in MANUAL_SPEC_FILENAMES")

    graphical = json.loads((GRAPHICAL_DIR / f"{topic_key}.json").read_text(encoding="utf-8"))
    if len(graphical["stages"]) != 13:
        failures.append(f"graphical stages={len(graphical['stages'])}")

    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    if [item for item in headings if item in REQUIRED_H2] != REQUIRED_H2:
        failures.append("required H2 order failed")
    if headings[-1] != REQUIRED_H2[4]:
        failures.append("register notes are not the final H2")

    basic = (ROOT / "upsc-ai-kit" / "knowledge" / "Geography" / "basic" / owner_name).read_text(
        encoding="utf-8"
    )
    advanced = (
        ROOT / "upsc-ai-kit" / "knowledge" / "Geography" / "advanced" / owner_name
    ).read_text(encoding="utf-8")
    basic_block = markdown.split(REQUIRED_H2[0], 1)[1].split(REQUIRED_H2[1], 1)[0]
    advanced_block = markdown.split(REQUIRED_H2[3], 1)[1]
    missing_basic = [
        heading
        for heading in re.findall(r"(?m)^## (.+?)\s*$", basic)
        if heading not in basic_block
    ]
    missing_advanced = [
        heading
        for heading in re.findall(r"(?m)^## (.+?)\s*$", advanced)
        if heading not in advanced_block
    ]
    if missing_basic:
        failures.append(f"missing Basic owner headings: {missing_basic}")
    if missing_advanced:
        failures.append(f"missing Advanced owner headings: {missing_advanced}")

    tracker = json.loads((ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8"))
    record_id = f"{topic_key}:learner-v2:g{generation}"
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict) and record.get("record_id") == record_id
    ]
    if len(records) != 1:
        failures.append(f"tracker records for {record_id}={len(records)}")
        record = {}
    else:
        record = records[0]
        if record.get("approved") is not False:
            failures.append("record is not approved:false")
    pages: dict[str, int] = {}
    for field in ("main_pdf", "workbook"):
        if record.get(field):
            with fitz.open(ROOT / str(record[field])) as document:
                pages[field] = document.page_count

    return {
        "topic_key": topic_key,
        "record_id": record_id,
        "approved": record.get("approved"),
        "sessions": len(sessions),
        "mcqs": len(stems),
        "unique_mcqs": len(set(stems)),
        "answer_distribution": dict(sorted(distribution.items())),
        "mains_weights": weights,
        "facts": len(facts),
        "ascii_panels_embedded": embedded_panels,
        "ascii_panels_registered": registered,
        "graphical_stages": len(graphical["stages"]),
        "notes_pages": pages.get("main_pdf"),
        "workbook_pages": pages.get("workbook"),
        "failures": failures,
    }


def main() -> int:
    results = [prove(*topic) for topic in TOPICS]
    print(json.dumps(results, ensure_ascii=False, indent=2))
    failed = [item["topic_key"] for item in results if item["failures"]]
    if failed:
        print(f"FAILED: {failed}")
        return 1
    print("ALL PER-TOPIC PROOFS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
