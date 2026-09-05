"""Prove and record completion manifests for one Social Justice learner-v2 topic.

Reads the finalised tracker record, programmatically proves the published
package's counts, answer distribution, section order and real PDF page counts,
then writes the standard completion and changed-files manifests. It is
read-only with respect to `EXPORT-PDF-STATUS.json` and every index.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import fitz  # noqa: E402
import generate_social_justice_common as social_justice  # noqa: E402
import notions_style_ascii_master as ascii_master  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


DATE = "2026-09-02"
SECTION_KEY = "subject-wide-syllabus"
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
REQUIRED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]
SHARED_FILES = [
    "EXPORT-PDF-STATUS.json",
    "EXPORT-PDF-COMMAND-INDEX.md",
    "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
    "upsc-ai-kit\\manifests\\v2\\social-justice--subject-wide-syllabus.json",
    "upsc-ai-kit\\knowledge\\Social-Justice\\LEARNING-SESSION-COMMAND-INDEX.md",
    f"notes\\Social-Justice\\learning-session-v2\\{SECTION_KEY}\\indexes\\TOPIC-COVERAGE-INDEX.md",
    f"notes\\Social-Justice\\learning-session-v2\\{SECTION_KEY}\\indexes\\NOTES-PDF-INDEX.md",
    f"notes\\Social-Justice\\learning-session-v2\\{SECTION_KEY}\\indexes\\WORKBOOK-PDF-INDEX.md",
]


def tracker_records(topic_key: str) -> list[dict[str, object]]:
    tracker = refresh.load_tracker()
    return [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == topic_key
        and record.get("variant") == refresh.V2_VARIANT
    ]


def prove(topic_key: str, record: dict[str, object]) -> dict[str, object]:
    markdown_path = refresh.repo_path(str(record["markdown"]))
    workbook_md_path = refresh.repo_path(str(record["workbook_markdown"]))
    markdown = markdown_path.read_text(encoding="utf-8")
    workbook = workbook_md_path.read_text(encoding="utf-8")

    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    ordered = [item for item in headings if item in REQUIRED_H2]
    register = markdown.split("## CONSOLIDATED REGISTER NOTES", 1)[-1]
    fact_anchors = re.findall(r"(?m)^(\d+)\. \*\*(.+?):\*\*", register)
    register_headings = list(social_justice.REGISTER_HEADINGS)
    register_body_present = all(item in register for item in register_headings)
    title = str(
        (record.get("provenance") or {}).get("title")
        or json.loads(
            (EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json").read_text(
                encoding="utf-8"
            )
        )["title"]
    )
    atlas_is_last = register.rfind("COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM") > max(
        register.rfind(item) for item in register_headings
    )

    stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
    answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown)
    workbook_stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
    workbook_answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook)
    mains = [
        int(value)
        for value in re.findall(r"(?m)^### ORIGINAL MAINS \d+ — (\d+) MARKS\s*$", markdown)
    ]
    sessions = re.findall(r"(?m)^### SESSION (\d+) — ", markdown)

    graphical_path = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "carvaka-graphical-specs"
        / "Social-Justice"
        / f"{topic_key}.json"
    )
    graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
    ascii_spec_path = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / f"{topic_key}-{DATE}-sequential.json"
    )
    spec = ascii_master.normalize_manual_spec_file(ascii_spec_path)[topic_key]
    embedded_fragment = ascii_master.build_manual_fragment(spec)

    with fitz.open(refresh.repo_path(str(record["main_pdf"]))) as pdf:
        main_pages = pdf.page_count
    with fitz.open(refresh.repo_path(str(record["workbook"]))) as pdf:
        workbook_pages = pdf.page_count

    distribution = {letter: answers.count(letter) for letter in "ABCD"}
    metrics = {
        "fact_anchor_count": len(fact_anchors),
        "learner_session_count": len(sessions),
        "visual_first_count": markdown.count("#### VISUAL FIRST"),
        "mcq_count": len(stems),
        "mcq_unique_stem_count": len(set(stems)),
        "mcq_answer_distribution": distribution,
        "mcq_strict_abcd_cycle": answers == list("ABCD") * 20,
        "workbook_mcq_count": len(workbook_stems),
        "workbook_mcq_unique_stem_count": len(set(workbook_stems)),
        "workbook_strict_abcd_cycle": workbook_answers == list("ABCD") * 20,
        "original_mains_weights": mains,
        "ascii_panel_count": markdown.count("```ascii-master"),
        "ascii_spec_panel_count": len(spec.panels),
        "ascii_embedded_equals_spec": embedded_fragment in markdown,
        "graphical_stage_count": len(graphical["stages"]),
        "h2_sequence": ordered,
        "register_notes_last": headings[-1] == "CONSOLIDATED REGISTER NOTES",
        "register_notes_body_present": register_body_present,
        "register_headings_are_topic_specific": all(
            f"{title}: {item}" in register for item in register_headings
        ),
        "ascii_atlas_after_register_body": atlas_is_last,
        "main_pdf_pages": main_pages,
        "workbook_pdf_pages": workbook_pages,
    }
    gates = {
        "twenty_source_bounded_fact_anchors": metrics["fact_anchor_count"] == 20,
        "exactly_fifteen_learning_sessions": metrics["learner_session_count"] == 15,
        "every_session_has_a_visual": metrics["visual_first_count"] == 15,
        "eighty_unique_mcqs": metrics["mcq_count"] == 80
        and metrics["mcq_unique_stem_count"] == 80,
        "strict_abcd_cycle_a20_b20_c20_d20": metrics["mcq_strict_abcd_cycle"]
        and distribution == {letter: 20 for letter in "ABCD"},
        "workbook_mirrors_practice": (
            metrics["workbook_mcq_count"] == 80
            and metrics["workbook_mcq_unique_stem_count"] == 80
            and metrics["workbook_strict_abcd_cycle"]
        ),
        "six_original_mains_10_10_15_15_20_20": mains == [10, 10, 15, 15, 20, 20],
        "twelve_manual_ascii_panels": metrics["ascii_panel_count"] == 12
        and metrics["ascii_spec_panel_count"] == 12
        and metrics["ascii_embedded_equals_spec"],
        "thirteen_graphical_stages": metrics["graphical_stage_count"] == 13,
        "required_h2_sequence_with_register_notes_last": ordered == REQUIRED_H2
        and metrics["register_notes_last"],
        "consolidated_register_notes_survive_publication": register_body_present
        and atlas_is_last,
        "register_headings_are_compressed_and_topic_specific": metrics[
            "register_headings_are_topic_specific"
        ],
        "real_pdf_pages_present": main_pages > 0 and workbook_pages > 0,
        "approval_false": record.get("approved") is False,
    }
    return {"metrics": metrics, "hard_gates": gates}


def changed_files(
    record: dict[str, object],
    *,
    also_changed: list[str] | None = None,
) -> list[str]:
    """List only files this export actually created or modified.

    Read-only inputs such as the OCR-searchable official question papers, the
    Basic/Advanced owners, the PYQ routing ledgers, the topic catalogue and the
    verified official evidence pages are recorded as provenance inside the
    tracker record, but they are never written by an export, so they are
    excluded here. Only paths under the learner-v2 output roots, the shared
    tracker/index state, the authored specs and the export manifests are
    reported.
    """

    written_roots = (
        "notes\\Learner-v2-Refreshed\\",
        "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\",
    )
    paths = {
        value
        for value in (
            refresh.relative(path.resolve())
            for path in refresh.iter_record_paths(record)
        )
        if value.startswith(written_roots)
    }
    for value in SHARED_FILES:
        candidate = ROOT / value
        if candidate.is_file():
            paths.add(value)
    topic_key = str(record["topic_key"])
    generation = int(record["generation"])
    extra = [
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Social-Justice"
        / "learning-sessions"
        / "v2"
        / SECTION_KEY
        / f"{topic_key}_Learning-Session.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Social-Justice"
        / "learning-sessions"
        / "v2"
        / SECTION_KEY
        / f"{topic_key}_Solved-Workbook.md",
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / f"{topic_key}-{DATE}-sequential.json",
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "carvaka-graphical-specs"
        / "Social-Justice"
        / f"{topic_key}.json",
        EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json",
        EXPORT_DIR / f"{topic_key}-learner-v2-{DATE}-validation.json",
        EXPORT_DIR / f"{topic_key}-learner-v2-{DATE}-staged-records.json",
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-record.json",
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-completion.json",
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt",
    ]
    canonical = json.loads(
        (EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json").read_text(encoding="utf-8")
    )["source_canonical"]
    extra.append(ROOT / canonical)
    for value in also_changed or []:
        extra.append(ROOT / value.replace("/", "\\"))
    for path in extra:
        paths.add(refresh.relative(path.resolve()))
    return sorted(paths, key=str.casefold)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    parser.add_argument(
        "--also-changed",
        action="append",
        default=[],
        help=(
            "Repository-relative path of an additional file this command created "
            "or modified, such as an authoring tool or its regression test."
        ),
    )
    args = parser.parse_args()
    topic_key = args.topic_key
    records = tracker_records(topic_key)
    if len(records) != 1:
        raise SystemExit(
            f"{topic_key}: expected exactly one learner-v2 tracker record, "
            f"found {len(records)}."
        )
    record = records[0]
    generation = int(record["generation"])
    proof = prove(topic_key, record)
    failed = [name for name, ok in proof["hard_gates"].items() if not ok]
    payload = {
        "schema_version": 1,
        "topic_key": topic_key,
        "record_id": record["record_id"],
        "variant": record["variant"],
        "generation": generation,
        "generated_on": DATE,
        "approval": bool(record.get("approved")),
        "result": "failed" if failed else "passed",
        "hard_gates": proof["hard_gates"],
        "metrics": proof["metrics"],
        "errors": [f"hard gate failed: {name}" for name in failed],
    }
    record_path = (
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-record.json"
    )
    completion_path = (
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-completion.json"
    )
    changed_path = (
        EXPORT_DIR / f"{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    record_path.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    completion_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    changed_path.write_text(
        "\n".join(changed_files(record, also_changed=args.also_changed)) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
