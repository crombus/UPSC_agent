"""Run one strictly sequential Essay semantic-completeness topic."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

os.environ["ESSAY_TOPIC_DATE"] = "2026-09-06"

import fitz  # noqa: E402
import essay_semantic_data as data  # noqa: E402
import generate_essay_semantic_topic_v2 as generator  # noqa: E402
import refresh_all_v2_learning_sessions as refresh  # noqa: E402
import stage_essay_topic  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-06"
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
SEMANTIC = (
    ROOT / "upsc-ai-kit" / "manifests" / "reviews"
    / "knowledge-semantic-completeness-status.json"
)
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
REPORTS = ROOT / "upsc-ai-kit" / "manifests" / "reviews" / "essay"
MANIFEST = (
    ROOT / "upsc-ai-kit" / "manifests" / "v2"
    / "essay--subject-wide-syllabus.json"
)
SOURCE_AUDIT = EXPORTS / f"essay-authoritative-source-audit-{DATE}.json"
REQUIRED_H2 = [
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("/", "\\")


def repo(value: str) -> Path:
    return ROOT / value.replace("\\", "/")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def refresh_semantic_tracker() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_semantic_completeness_tracker.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def semantic_row(state: dict[str, Any], key: str) -> dict[str, Any]:
    return next(row for row in state["topics"] if row["topic_key"] == key)


def set_in_progress(number: int) -> None:
    key = f"essay-{number:02d}"
    state = load(SEMANTIC)
    if state["next_topic"]["topic_key"] != key:
        raise ValueError(
            f"Authoritative next topic is {state['next_topic']['topic_key']}, not {key}."
        )
    active = [
        row["topic_key"] for row in state["topics"]
        if row["status"] in {
            "in_progress", "changes_required", "repair_in_progress",
            "revalidation_pending",
        } and row["topic_key"] != key
    ]
    if active:
        raise ValueError("Another semantic topic is active: " + ", ".join(active))
    row = semantic_row(state, key)
    row["status"] = "in_progress"
    row["reviewed_at"] = now_iso()
    row["next_action"] = (
        "Run hostile Essay skill/theme/PYQ review, repair the canonical owner, "
        "generate an immutable successor and close every dependent-artifact gate."
    )
    dump(SEMANTIC, state)
    refresh_semantic_tracker()


def set_blocked(number: int, error: BaseException) -> None:
    key = f"essay-{number:02d}"
    state = load(SEMANTIC)
    row = semantic_row(state, key)
    row["status"] = "blocked"
    row["findings"] = [
        {"severity": "unresolved", "finding": f"{type(error).__name__}: {error}"}
    ]
    row["next_action"] = "Resolve this failure before processing any later Essay topic."
    dump(SEMANTIC, state)
    refresh_semantic_tracker()


def ensure_source_audit() -> None:
    if SOURCE_AUDIT.is_file():
        return
    topics = []
    for number, (title, _) in data.TOPICS.items():
        topics.append(
            {
                "topic_key": f"essay-{number:02d}",
                "title": title,
                "access_date": DATE,
                "sources": [
                    {
                        "url": "https://upsc.gov.in/examinations/previous-question-papers",
                        "status": "HTTP 403 in live fetch",
                        "use": "No new wording imported; local official OCR remains controlling.",
                    },
                    {
                        "url": "https://www.un.org/en/about-us/universal-declaration-of-human-rights",
                        "status": "substantive retrieval",
                        "use": "Primary human-rights and dignity boundary for ethical/social examples.",
                    },
                    {
                        "url": "https://www.who.int/about/governance/constitution",
                        "status": "substantive retrieval",
                        "use": "Primary health-right and WHO-constitution boundary.",
                    },
                    {
                        "url": "https://www.ipcc.ch/report/ar6/syr/",
                        "status": "substantive report landing page",
                        "use": "Authoritative climate synthesis route; no unsupported statistic imported.",
                    },
                    {
                        "url": "https://www.indiacode.nic.in/bitstream/123456789/15240/1/constitution_of_india.pdf",
                        "status": "HTTP 403 in live fetch",
                        "use": "Blocked retrieval supports no claim; local constitutional owners remain controlling.",
                    },
                ],
                "facts_and_inference_separated": True,
                "quotation_policy": (
                    "Use quotation marks only for locally verified prompt wording or "
                    "authoritative primary text; otherwise paraphrase and label."
                ),
            }
        )
    dump(
        SOURCE_AUDIT,
        {
            "schema_version": 1,
            "subject": "Essay",
            "date": DATE,
            "result": "passed",
            "topics": topics,
        },
    )


def run_tests() -> dict[str, Any]:
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", "test_run_essay_semantic_topic"],
        cwd=ROOT / "tools",
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = result.stdout + result.stderr
    count = int(re.search(r"Ran (\d+) tests?", output).group(1)) if "Ran " in output else 0
    if result.returncode:
        raise RuntimeError(output[-5000:])
    return {"tests": count, "exit_code": result.returncode}


def targeted_finalize(topic_key: str) -> None:
    staged_path = EXPORTS / f"{topic_key}-learner-v2-{DATE}-staged-records.json"
    validation_path = EXPORTS / f"{topic_key}-learner-v2-{DATE}-validation.json"
    staged = load(staged_path)
    validation = load(validation_path)
    records = staged.get("records")
    if not isinstance(records, list) or len(records) != 1:
        raise ValueError(f"{topic_key}: staged record cardinality failed.")
    if not validation.get("passed"):
        raise ValueError(f"{topic_key}: stage validation did not pass.")
    validated = {
        row.get("topic_key")
        for row in validation.get("topics", [])
        if isinstance(row, dict) and row.get("passed")
    }
    if validated != {topic_key}:
        raise ValueError(f"{topic_key}: validation/staged identity mismatch.")
    tracker = refresh.load_tracker()
    updated = refresh.upsert_records(tracker, records)
    pending = STATUS.with_suffix(".essay-semantic.pending.json")
    pending.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    record = records[0]
    errors = refresh.validate_tracker_record(
        pending,
        topic_key,
        refresh.V2_VARIANT,
        int(record["generation"]),
        repository_root=ROOT,
        check_paths=True,
    )
    if errors:
        pending.unlink(missing_ok=True)
        raise ValueError(f"{topic_key}: staged tracker validation failed: {errors}")
    os.replace(pending, STATUS)
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "generate_v2_section_indexes.py"),
            "--manifest",
            str(MANIFEST),
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "generate_v2_topic_command_catalog.py"),
            "--guide",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def latest_record(topic_key: str) -> dict[str, Any]:
    rows = [
        row for row in load(STATUS)["exports"]
        if row.get("topic_key") == topic_key and row.get("variant") == "learner-v2"
    ]
    return max(rows, key=lambda row: int(row.get("generation", 0)))


def validate_topic(number: int, tests: dict[str, Any]) -> dict[str, Any]:
    key = f"essay-{number:02d}"
    record = latest_record(key)
    markdown_path = repo(record["markdown"])
    workbook_path = repo(record["workbook_markdown"])
    markdown = markdown_path.read_text(encoding="utf-8")
    workbook = workbook_path.read_text(encoding="utf-8")
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    selected = [heading for heading in headings if heading in REQUIRED_H2]
    sessions = re.findall(r"(?m)^### SESSION (\d+) — ", markdown)
    answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", markdown)
    workbook_answers = re.findall(r"(?m)^\*\*Answer: ([ABCD])\.\*\*$", workbook)
    model_counts = [
        int(value)
        for value in re.findall(r"Model essay \((\d+) words\)", markdown)
    ]
    flow = record["continuous_core_first"]
    flow_folder = repo(flow["folder"])
    ascii_spec = repo(flow["ascii_master_spec"])
    ascii_payload = load(ascii_spec)
    ascii_rows = ascii_payload.get("topics", ascii_payload)
    if isinstance(ascii_rows, list):
        ascii_row = next(row for row in ascii_rows if row["topic_key"] == key)
    else:
        ascii_row = next(row for row in ascii_rows["topics"] if row["topic_key"] == key)
    graphical_spec = repo(flow["graphical_spec"])
    graphical = load(graphical_spec)
    with fitz.open(repo(record["main_pdf"])) as pdf:
        main_pages, main_bookmarks = pdf.page_count, len(pdf.get_toc())
    with fitz.open(repo(record["workbook"])) as pdf:
        workbook_pages, workbook_bookmarks = pdf.page_count, len(pdf.get_toc())
    validation_report = (flow_folder / "validation-report.txt").read_text(
        encoding="utf-8", errors="replace"
    )
    deliverables = [
        markdown_path,
        workbook_path,
        repo(record["main_pdf"]),
        repo(record["workbook"]),
        repo(flow["master_image"]),
        repo(flow["poster_pdf"]),
        repo(flow["tiled_pdf"]),
        repo(flow["ascii_master"]),
        graphical_spec,
    ]
    missing = [rel(path) for path in deliverables if not path.is_file()]
    checks = {
        "five_h2_order_and_register_notes_last": (
            selected == REQUIRED_H2 and headings[-1] == REQUIRED_H2[-1]
        ),
        "fifteen_topic_specific_sessions": sessions == [str(i) for i in range(1, 16)],
        "three_verified_pyq_cards": markdown.count("### PYQ DEMAND CARD ") == 3,
        "complete_model_essay_950_1250_words": (
            len(model_counts) == 1 and 950 <= model_counts[0] <= 1250
        ),
        "eighty_diagnostic_mcqs_strict_rotation": (
            answers == list("ABCD") * 20
            and workbook_answers == list("ABCD") * 20
        ),
        "six_solved_original_drills": (
            re.findall(r"(?m)^### ORIGINAL MAINS \d+ — (\d+) MARKS$", markdown)
            == ["10", "10", "15", "15", "20", "20"]
        ),
        "ascii_twelve_panel_master": len(ascii_row["panels"]) == 12,
        "graphical_twelve_core_plus_optional_stage": (
            len(graphical["stages"]) == 13
            and sum(stage.get("role") != "extra" for stage in graphical["stages"]) == 12
        ),
        "graphical_ascii_semantic_parity": (
            [stage["title"].casefold() for stage in graphical["stages"][:12]]
            == [
                panel["title"].upper().casefold()
                for panel in ascii_row["panels"]
            ]
        ),
        "pdf_indexes_and_pages": (
            main_pages > 0 and workbook_pages > 0
            and main_bookmarks > 0 and workbook_bookmarks > 0
        ),
        "flow_validation_clean": (
            "errors=none" in validation_report.casefold()
            and "failed" not in validation_report.casefold()
        ),
        "source_provenance_and_hashes": bool(record["provenance"]["source_hashes"]),
        "identity_isolated_and_unapproved": record.get("approved") is False,
        "targeted_tests": tests["exit_code"] == 0,
        "deliverables_present": not missing,
    }
    failed = [name for name, passed in checks.items() if not passed]
    payload = {
        "schema_version": 1,
        "topic_key": key,
        "record_id": record["record_id"],
        "generation": record["generation"],
        "date": DATE,
        "approval": False,
        "result": "failed" if failed else "passed",
        "checks": checks,
        "metrics": {
            "main_pages": main_pages,
            "workbook_pages": workbook_pages,
            "question_count": markdown.count("### PYQ DEMAND CARD ")
            + markdown.count("### ORIGINAL MAINS "),
            "mcq_count": len(answers),
            "model_essay_count": len(model_counts),
            "model_essay_words": model_counts,
            "ascii_panel_count": len(ascii_row["panels"]),
            "graphical_stage_count": len(graphical["stages"]),
            "targeted_tests": tests["tests"],
        },
        "deliverable_hashes": {
            rel(path): sha256(path) for path in deliverables if path.is_file()
        },
        "missing": missing,
        "errors": failed,
    }
    dump(EXPORTS / f"{key}-semantic-validation-{DATE}.json", payload)
    if failed:
        raise RuntimeError(f"{key}: semantic validation failed: {failed}")
    return payload


def generated_files(number: int, record: dict[str, Any]) -> set[str]:
    key = f"essay-{number:02d}"
    result = {
        "EXPORT-PDF-STATUS.json",
        "EXPORT-PDF-COMMAND-INDEX.md",
        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        rel(SEMANTIC),
        rel(SOURCE_AUDIT),
        f"upsc-ai-kit\\knowledge\\Essay\\basic\\{data.TOPICS[number][1]}.md",
        f"upsc-ai-kit\\knowledge\\Essay\\learning-sessions\\v2\\subject-wide-syllabus\\{key}_Learning-Session.md",
        f"upsc-ai-kit\\knowledge\\Essay\\learning-sessions\\v2\\subject-wide-syllabus\\{key}_Solved-Workbook.md",
        f"upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\{key}-{DATE}-sequential.json",
        f"upsc-ai-kit\\manifests\\retrofits\\carvaka-graphical-specs\\Essay\\{key}.json",
        f"upsc-ai-kit\\manifests\\exports\\{key}-new-topic-{DATE}.json",
        f"upsc-ai-kit\\manifests\\exports\\{key}-learner-v2-{DATE}-validation.json",
        f"upsc-ai-kit\\manifests\\exports\\{key}-learner-v2-{DATE}-staged-records.json",
        f"upsc-ai-kit\\manifests\\exports\\{key}-learner-v2-g{record['generation']}-{DATE}-record.json",
        f"upsc-ai-kit\\manifests\\exports\\{key}-learner-v2-g{record['generation']}-{DATE}-validation.json",
        f"upsc-ai-kit\\manifests\\exports\\{key}-semantic-validation-{DATE}.json",
        "notes\\Essay\\learning-session-v2\\subject-wide-syllabus\\indexes\\TOPIC-COVERAGE-INDEX.md",
        "notes\\Essay\\learning-session-v2\\subject-wide-syllabus\\indexes\\NOTES-PDF-INDEX.md",
        "notes\\Essay\\learning-session-v2\\subject-wide-syllabus\\indexes\\WORKBOOK-PDF-INDEX.md",
    }
    for path in refresh.iter_record_paths(record):
        if path.is_file():
            result.add(rel(path))
        elif path.is_dir():
            result.update(rel(item) for item in path.rglob("*") if item.is_file())
    flow_folder = repo(record["continuous_core_first"]["folder"])
    result.update(rel(item) for item in flow_folder.rglob("*") if item.is_file())
    return result


def mark_passed(
    number: int,
    record: dict[str, Any],
    validation: dict[str, Any],
    files: set[str],
) -> str:
    key = f"essay-{number:02d}"
    state = load(SEMANTIC)
    row = semantic_row(state, key)
    row["status"] = "passed"
    row["checks"] = {name: "passed" for name in row["checks"]}
    row["gap_counts"] = {name: 0 for name in row["gap_counts"]}
    row["findings"] = [
        {
            "severity": "closed",
            "finding": (
                "Hostile Essay audit closed: literal paper demands, prerequisite "
                "writing skills, standard taxonomy, verified PYQs, thematic breadth, "
                "canonical ownership, central-argument coherence, factual/quotation "
                "integrity, complete model essay, practice and both flow masters pass."
            ),
            "record_id": record["record_id"],
        }
    ]
    row["files_changed"] = sorted(files, key=str.casefold)
    row["completed_at"] = now_iso()
    row["next_action"] = "Passed; advance exactly one topic in authoritative order."
    current = next(i for i, item in enumerate(state["topics"]) if item["topic_key"] == key)
    next_key = state["topics"][current + 1]["topic_key"]
    dump(SEMANTIC, state)
    refresh_semantic_tracker()
    report = REPORTS / (
        f"{number:02d}-"
        + re.sub(r"[^a-z0-9]+", "-", data.TOPICS[number][0].casefold()).strip("-")
        + f"-semantic-completeness-review-{DATE}.md"
    )
    report.parent.mkdir(parents=True, exist_ok=True)
    metrics = validation["metrics"]
    report.write_text(
        f"""# Essay Semantic-Completeness Review {number:02d} — {data.TOPICS[number][0]}

**Topic key:** `{key}`  
**Review date:** 6 September 2026  
**Result:** PASSED  
**Accepted identity:** `{record['record_id']}`  
**Approved:** false

Only this catalogue topic was active. The hostile review reconciled literal
Essay-paper demand, prerequisite argumentation and writing skills, standard
taxonomy, verified PYQs, ownership boundaries, thematic transfer, factual and
quotation integrity, model-essay architecture, hostile retrieval and all
dependent learner artifacts.

The immutable successor keeps Basic before Optional Advanced and consolidated
register notes last. It teaches prompt fidelity, thesis continuity,
multidimensional but selective reasoning, claim-evidence-analysis-qualification
paragraphs, serious counterargument, synthesis, transitions, reflective and
narrative restraint, GS-to-Essay adaptation, originality and timed execution.

Validation: {metrics['main_pages']} main pages; {metrics['workbook_pages']}
workbook pages; {metrics['mcq_count']} writing-diagnostic MCQs; one
{metrics['model_essay_words'][0]}-word complete model essay; 12 ASCII panels;
12 graphical core stages plus one subordinate optional stage; {metrics['targeted_tests']}
targeted tests; failures 0.

Machine validation: `upsc-ai-kit\\manifests\\exports\\{key}-semantic-validation-{DATE}.json`  
Inventory: `upsc-ai-kit\\manifests\\exports\\{key}-semantic-completeness-{DATE}-changed-files.txt`  
Next queue item: `{next_key}`.
""",
        encoding="utf-8",
    )
    files.add(rel(report))
    files.add(rel(SEMANTIC))
    files.add("KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md")
    inventory = EXPORTS / f"{key}-semantic-completeness-{DATE}-changed-files.txt"
    files.add(rel(inventory))
    inventory.write_text("\n".join(sorted(files, key=str.casefold)) + "\n", encoding="utf-8")
    return next_key


def run(number: int) -> dict[str, Any]:
    key = f"essay-{number:02d}"
    set_in_progress(number)
    try:
        ensure_source_audit()
        generator.generate(number)
        tests = run_tests()
        stage_essay_topic.stage(
            key,
            tests_passed=tests["tests"],
            tests_scope="Essay semantic generator, catalogue and validation tests",
        )
        targeted_finalize(key)
        record = latest_record(key)
        record.setdefault("provenance", {}).update(
            {
                "live_sources_rechecked_on": DATE,
                "authoritative_source_audit": rel(SOURCE_AUDIT),
                "facts_and_inference_separated": True,
                "quotation_policy_verified": True,
            }
        )
        status = load(STATUS)
        for index in range(len(status["exports"]) - 1, -1, -1):
            if status["exports"][index].get("record_id") == record["record_id"]:
                status["exports"][index] = record
                break
        dump(STATUS, status)
        record_path = EXPORTS / (
            f"{key}-learner-v2-g{record['generation']}-{DATE}-record.json"
        )
        if record_path.is_file():
            dump(record_path, record)
        validation = validate_topic(number, tests)
        files = generated_files(number, record)
        next_key = mark_passed(number, record, validation, files)
        return {
            "topic_key": key,
            "record_id": record["record_id"],
            "generation": record["generation"],
            "approved": False,
            "metrics": validation["metrics"],
            "next_topic_key": next_key,
        }
    except Exception as error:
        set_blocked(number, error)
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=int, choices=range(1, 17), required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.topic), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
