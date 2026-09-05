"""Prove and record one finalised Essay learner-v2 topic."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import fitz  # noqa: E402
import generate_essay_common as essay  # noqa: E402
import notions_style_ascii_master as ascii_master  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402


DATE = os.environ.get("ESSAY_TOPIC_DATE", "2026-09-04")
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
    "upsc-ai-kit\\manifests\\v2\\essay--subject-wide-syllabus.json",
    "notes\\Essay\\learning-session-v2\\subject-wide-syllabus\\indexes\\TOPIC-COVERAGE-INDEX.md",
    "notes\\Essay\\learning-session-v2\\subject-wide-syllabus\\indexes\\NOTES-PDF-INDEX.md",
    "notes\\Essay\\learning-session-v2\\subject-wide-syllabus\\indexes\\WORKBOOK-PDF-INDEX.md",
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
    maximum = max((int(record.get("generation") or 0) for record in records), default=0)
    latest = [record for record in records if int(record.get("generation") or 0) == maximum]
    if len(latest) != 1:
        raise SystemExit(f"{topic_key}: expected one exact latest learner-v2 record.")
    return latest[0]


def prove(topic_key: str, record: dict[str, object]) -> dict[str, object]:
    markdown = refresh.repo_path(str(record["markdown"])).read_text(encoding="utf-8")
    workbook = refresh.repo_path(str(record["workbook_markdown"])).read_text(encoding="utf-8")
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    ordered = [item for item in headings if item in REQUIRED_H2]
    register = markdown.split("## CONSOLIDATED REGISTER NOTES", 1)[-1]
    register_body = register.split(
        "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM", 1
    )[0]
    title = json.loads(
        (EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json").read_text(
            encoding="utf-8"
        )
    )["title"]
    fact_anchors = re.findall(r"(?m)^(\d+)\. \*\*(.+?):\*\*", register)
    stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
    answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown)
    workbook_stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", workbook)
    workbook_answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook)
    mains = [
        int(value)
        for value in re.findall(
            r"(?m)^### ORIGINAL MAINS \d+ — (\d+) MARKS\s*$", markdown
        )
    ]
    sessions = re.findall(r"(?m)^### SESSION (\d+) — ", markdown)
    pyq_cards = re.findall(r"(?m)^### PYQ DEMAND CARD \d+ — ", markdown)
    register_headings = re.findall(r"(?m)^### (.+?)\s*$", register_body)
    live_block = markdown.split(
        "### LIVE OFFICIAL-SOURCE ATTEMPT LOG", 1
    )[-1].split("## BASIC LEARNING SESSION", 1)[0]
    live_attempts = re.findall(r"(?m)^- (https?://.+)$", live_block)
    graphical = json.loads(
        (
            essay.GRAPHICAL_DIR / f"{topic_key}.json"
        ).read_text(encoding="utf-8")
    )
    ascii_path = (
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits"
        / "ascii-panel-specs" / f"{topic_key}-{DATE}-sequential.json"
    )
    spec = ascii_master.normalize_manual_spec_file(ascii_path)[topic_key]
    embedded = ascii_master.build_manual_fragment(spec)
    with fitz.open(refresh.repo_path(str(record["main_pdf"]))) as pdf:
        main_pages = pdf.page_count
        main_bookmarks = len(pdf.get_toc())
    with fitz.open(refresh.repo_path(str(record["workbook"]))) as pdf:
        workbook_pages = pdf.page_count
        workbook_bookmarks = len(pdf.get_toc())
    distribution = {letter: answers.count(letter) for letter in "ABCD"}
    metrics = {
        "fact_anchor_count": len(fact_anchors),
        "learner_session_count": len(sessions),
        "pyq_application_card_count": len(pyq_cards),
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
        "register_notes_body_present": len(register_headings) == 4
        and all(
            re.search(
                rf"(?ms)^### {re.escape(heading)}\s*$.*?(?=^### |\Z)",
                register_body,
            )
            for heading in register_headings
        ),
        "register_headings_are_topic_specific": len(register_headings) == 4
        and all(heading.startswith(f"{title}: ") for heading in register_headings),
        "ascii_atlas_after_register_body": (
            register.rfind("COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM")
            > max(register.rfind(item) for item in register_headings)
        ),
        "live_source_attempt_log_present": "### LIVE OFFICIAL-SOURCE ATTEMPT LOG" in markdown,
        "live_source_attempt_count": len(live_attempts),
        "live_source_attempts_dated": all(DATE in item for item in live_attempts),
        "live_source_attempts_official": all(
            any(
                domain in item
                for domain in ("upsc.gov.in",)
            )
            for item in live_attempts
        ),
        "notes_contents_index_present": main_bookmarks > 0,
        "workbook_contents_index_present": workbook_bookmarks > 0,
        "main_pdf_pages": main_pages,
        "workbook_pdf_pages": workbook_pages,
        "main_pdf_bookmarks": main_bookmarks,
        "workbook_pdf_bookmarks": workbook_bookmarks,
    }
    gates = {
        "twenty_source_bounded_fact_anchors": metrics["fact_anchor_count"] == 20,
        "exactly_fifteen_learning_sessions": metrics["learner_session_count"] == 15,
        "every_session_has_a_visual": metrics["visual_first_count"] == 15,
        "three_verified_pyq_application_cards": (
            metrics["pyq_application_card_count"] == 3
        ),
        "eighty_unique_mcqs": metrics["mcq_count"] == 80
        and metrics["mcq_unique_stem_count"] == 80,
        "strict_abcd_cycle_a20_b20_c20_d20": metrics["mcq_strict_abcd_cycle"]
        and distribution == {letter: 20 for letter in "ABCD"},
        "workbook_mirrors_practice": metrics["workbook_mcq_count"] == 80
        and metrics["workbook_mcq_unique_stem_count"] == 80
        and metrics["workbook_strict_abcd_cycle"],
        "six_original_mains_10_10_15_15_20_20": mains == [10, 10, 15, 15, 20, 20],
        "twelve_manual_ascii_panels": metrics["ascii_panel_count"] == 12
        and metrics["ascii_spec_panel_count"] == 12
        and metrics["ascii_embedded_equals_spec"],
        "thirteen_graphical_stages": metrics["graphical_stage_count"] == 13,
        "required_h2_sequence_with_register_notes_last": ordered == REQUIRED_H2
        and metrics["register_notes_last"],
        "consolidated_register_notes_survive_publication": metrics["register_notes_body_present"]
        and metrics["ascii_atlas_after_register_body"],
        "register_headings_are_topic_specific": metrics["register_headings_are_topic_specific"],
        "live_official_source_attempts_recorded": (
            metrics["live_source_attempt_log_present"]
            and metrics["live_source_attempt_count"] >= 3
            and metrics["live_source_attempts_dated"]
            and metrics["live_source_attempts_official"]
        ),
        "notes_and_workbook_contents_bookmarks": metrics["notes_contents_index_present"]
        and metrics["workbook_contents_index_present"],
        "real_pdf_pages_present": main_pages > 0 and workbook_pages > 0,
        "approval_false": record.get("approved") is False,
    }
    return {"metrics": metrics, "hard_gates": gates}


def changed_files(record: dict[str, object], also_changed: list[str] | None = None) -> list[str]:
    written_roots = (
        "notes\\Learner-v2-Refreshed\\",
        "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\",
    )
    paths = {
        value
        for value in (
            refresh.relative(path.resolve()) for path in refresh.iter_record_paths(record)
        )
        if value.startswith(written_roots)
    }
    paths.update(value for value in SHARED_FILES if (ROOT / value).is_file())
    topic_key = str(record["topic_key"])
    generation = int(record["generation"])
    spec = json.loads(
        (EXPORT_DIR / f"{topic_key}-new-topic-{DATE}.json").read_text(encoding="utf-8")
    )
    paths.update(
        str(value).replace("/", "\\")
        for value in [
            spec["source_markdown"],
            spec["workbook_markdown"],
            f"upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\{topic_key}-{DATE}-sequential.json",
            f"upsc-ai-kit\\manifests\\retrofits\\carvaka-graphical-specs\\Essay\\{topic_key}.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-new-topic-{DATE}.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-{DATE}-validation.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-{DATE}-staged-records.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-record.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-validation.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-completion.json",
            f"upsc-ai-kit\\manifests\\exports\\{topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt",
            *(also_changed or []),
        ]
    )
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
    completion = EXPORT_DIR / f"{args.topic_key}-learner-v2-g{generation}-{DATE}-completion.json"
    ledger = completion.with_name(completion.name.replace("-completion.json", "-changed-files.txt"))
    completion.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ledger.write_text("\n".join(changed_files(record, args.also_changed)) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
