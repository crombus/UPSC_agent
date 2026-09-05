"""Prove and record completion for one finalised Economy learner-v2 topic."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import fitz  # noqa: E402
import generate_economy_common as economy  # noqa: E402
import notions_style_ascii_master as ascii_master  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


DATE = "2026-09-03"
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
    "upsc-ai-kit\\manifests\\v2\\economy--subject-wide-syllabus.json",
    "upsc-ai-kit\\knowledge\\Economy\\LEARNING-SESSION-COMMAND-INDEX.md",
    "notes\\Economy\\learning-session-v2\\subject-wide-syllabus\\indexes\\TOPIC-COVERAGE-INDEX.md",
    "notes\\Economy\\learning-session-v2\\subject-wide-syllabus\\indexes\\NOTES-PDF-INDEX.md",
    "notes\\Economy\\learning-session-v2\\subject-wide-syllabus\\indexes\\WORKBOOK-PDF-INDEX.md",
]


def tracker_records(topic_key: str) -> list[dict[str, object]]:
    return [
        record
        for record in refresh.load_tracker()["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == topic_key
        and record.get("variant") == refresh.V2_VARIANT
    ]


def latest_tracker_record(topic_key: str) -> dict[str, object]:
    records = tracker_records(topic_key)
    if not records:
        raise SystemExit(f"{topic_key}: no learner-v2 record found.")
    latest_generation = max(int(record.get("generation") or 0) for record in records)
    latest = [
        record
        for record in records
        if int(record.get("generation") or 0) == latest_generation
    ]
    if len(latest) != 1:
        raise SystemExit(
            f"{topic_key}: expected one exact g{latest_generation} record, found {len(latest)}"
        )
    return latest[0]


def prove(topic_key: str, record: dict[str, object]) -> dict[str, object]:
    markdown = refresh.repo_path(str(record["markdown"])).read_text(encoding="utf-8")
    workbook = refresh.repo_path(str(record["workbook_markdown"])).read_text(
        encoding="utf-8"
    )
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    ordered = [item for item in headings if item in REQUIRED_H2]
    register = markdown.split("## CONSOLIDATED REGISTER NOTES", 1)[-1]
    fact_anchors = re.findall(r"(?m)^(\d+)\. \*\*(.+?):\*\*", register)
    title = json.loads(
        (EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json").read_text(
            encoding="utf-8"
        )
    )["title"]
    stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
    answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown)
    workbook_stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
    workbook_answers = re.findall(
        r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook
    )
    mains = [
        int(value)
        for value in re.findall(
            r"(?m)^### ORIGINAL MAINS \d+ — (\d+) MARKS\s*$",
            markdown,
        )
    ]
    sessions = re.findall(r"(?m)^### SESSION (\d+) — ", markdown)
    graphical = json.loads(
        (
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "retrofits"
            / "carvaka-graphical-specs"
            / "Economy"
            / f"{topic_key}.json"
        ).read_text(encoding="utf-8")
    )
    ascii_path = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / f"{topic_key}-{DATE}-sequential.json"
    )
    spec = ascii_master.normalize_manual_spec_file(ascii_path)[topic_key]
    embedded = ascii_master.build_manual_fragment(spec)
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
        "ascii_embedded_equals_spec": embedded in markdown,
        "graphical_stage_count": len(graphical["stages"]),
        "h2_sequence": ordered,
        "register_notes_last": headings[-1] == "CONSOLIDATED REGISTER NOTES",
        "register_notes_body_present": all(
            item in register for item in economy.REGISTER_HEADINGS
        ),
        "register_headings_are_topic_specific": all(
            f"{title}: {item}" in register for item in economy.REGISTER_HEADINGS
        ),
        "ascii_atlas_after_register_body": (
            register.rfind("COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM")
            > max(register.rfind(item) for item in economy.REGISTER_HEADINGS)
        ),
        "live_source_attempt_log_present": (
            "### LIVE OFFICIAL-SOURCE ATTEMPT LOG" in markdown
        ),
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
        "workbook_mirrors_practice": metrics["workbook_mcq_count"] == 80
        and metrics["workbook_mcq_unique_stem_count"] == 80
        and metrics["workbook_strict_abcd_cycle"],
        "six_original_mains_10_10_15_15_20_20": mains
        == [10, 10, 15, 15, 20, 20],
        "twelve_manual_ascii_panels": metrics["ascii_panel_count"] == 12
        and metrics["ascii_spec_panel_count"] == 12
        and metrics["ascii_embedded_equals_spec"],
        "thirteen_graphical_stages": metrics["graphical_stage_count"] == 13,
        "required_h2_sequence_with_register_notes_last": ordered == REQUIRED_H2
        and metrics["register_notes_last"],
        "consolidated_register_notes_survive_publication": metrics[
            "register_notes_body_present"
        ]
        and metrics["ascii_atlas_after_register_body"],
        "register_headings_are_compressed_and_topic_specific": metrics[
            "register_headings_are_topic_specific"
        ],
        "live_official_source_attempts_recorded": metrics[
            "live_source_attempt_log_present"
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
    paths.update(value for value in SHARED_FILES if (ROOT / value).is_file())
    topic_key = str(record["topic_key"])
    generation = int(record["generation"])
    new_spec = json.loads(
        (EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json").read_text(
            encoding="utf-8"
        )
    )
    extra = [
        new_spec["source_markdown"],
        new_spec["workbook_markdown"],
        new_spec["source_canonical"],
        f"upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\{topic_key}-{DATE}-sequential.json",
        f"upsc-ai-kit\\manifests\\retrofits\\carvaka-graphical-specs\\Economy\\{topic_key}.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-new-topic-{DATE}.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-{DATE}-validation.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-{DATE}-staged-records.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-record.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-validation.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-completion.json",
        f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt",
        *(also_changed or []),
    ]
    paths.update(str(value).replace("/", "\\") for value in extra)
    return sorted(paths, key=str.casefold)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic_key")
    parser.add_argument("--also-changed", action="append", default=[])
    args = parser.parse_args()
    record = latest_tracker_record(args.topic_key)
    proof = prove(args.topic_key, record)
    failed = [name for name, ok in proof["hard_gates"].items() if not ok]
    generation = int(record["generation"])
    payload = {
        "schema_version": 1,
        "topic_key": args.topic_key,
        "record_id": record["record_id"],
        "variant": record["variant"],
        "generation": generation,
        "generated_on": DATE,
        "approval": bool(record.get("approved")),
        "result": "failed" if failed else "passed",
        "hard_gates": proof["hard_gates"],
        "metrics": proof["metrics"],
        "errors": failed,
    }
    completion = (
        EXPORT_DIR
        / f"{args.topic_key}-learner-v2-g{generation}-{DATE}-completion.json"
    )
    ledger = completion.with_name(
        completion.name.replace("-completion.json", "-changed-files.txt")
    )
    completion.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    ledger.write_text(
        "\n".join(changed_files(record, also_changed=args.also_changed)) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
