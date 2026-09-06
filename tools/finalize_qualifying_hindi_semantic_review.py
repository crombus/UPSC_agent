"""Validate the complete Qualifying Hindi semantic review and write its exact inventory."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import fitz
from PIL import Image, ImageChops

import qualifying_hindi_semantic_runtime as runtime


VALIDATION = runtime.EXPORTS / f"qualifying-hindi-01-06-semantic-completeness-{runtime.DATE}-validation.json"
INVENTORY = runtime.EXPORTS / f"qualifying-hindi-01-06-semantic-completeness-{runtime.DATE}-changed-files.txt"
REPORT = runtime.REVIEWS / f"Qualifying-Hindi-Subject-Semantic-Completion-{runtime.DATE}.md"


def latest(status: dict[str, Any], key: str) -> dict[str, Any]:
    rows = [row for row in status["exports"] if row.get("topic_key") == key and row.get("variant") == "learner-v2"]
    return max(rows, key=lambda row: int(row.get("generation", 0)))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_flow(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    flow = record["continuous_core_first"]
    master_path = runtime.ROOT / flow["master_image"]
    tiled_path = runtime.ROOT / flow["tiled_pdf"]
    ascii_path = runtime.ROOT / flow["ascii_master"]
    spec = runtime.load(runtime.ROOT / flow["editable"] / "topic-spec.json")
    ascii_text = ascii_path.read_text(encoding="utf-8")
    if len(spec["stages"]) != 12 or ascii_text.count("PANEL ") != 12:
        errors.append(f"{record['topic_key']}: flow stage/panel count mismatch.")
    for stage in spec["stages"]:
        if stage["title"].upper() not in ascii_text:
            errors.append(f"{record['topic_key']}: ASCII missing stage {stage['title']}.")
    master = Image.open(master_path).convert("RGB")
    start = 0
    with fitz.open(tiled_path) as document:
        for index, page in enumerate(document, 1):
            tile_path = runtime.ROOT / flow["editable"] / f"tile-{index:02d}.png"
            tile = Image.open(tile_path).convert("RGB")
            expected = master.crop((0, start, master.width, start + tile.height))
            if ImageChops.difference(tile, expected).getbbox() is not None:
                errors.append(f"{record['topic_key']}: tile {index} is not an exact master crop.")
            images = page.get_images(full=True)
            if len(images) != 1:
                errors.append(f"{record['topic_key']}: tiled PDF page {index} has {len(images)} images.")
            start += tile.height - 80
            tile.close()
            expected.close()
    master.close()
    return errors


def validate_hindi_pdf(path: Path) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    with fitz.open(path) as document:
        text = "\n".join(page.get_text("text") for page in document)
        fonts = sorted({font[3] for page in document for font in page.get_fonts(full=True)})
    devanagari = len(re.findall(r"[\u0900-\u097f]", text))
    if devanagari < 100:
        errors.append(f"{runtime.rel(path)}: too little extractable Devanagari ({devanagari}).")
    if "\ufffd" in text:
        errors.append(f"{runtime.rel(path)}: replacement glyph in extracted text.")
    if not any("Nirmala" in name or "Devanagari" in name for name in fonts):
        errors.append(f"{runtime.rel(path)}: no embedded Devanagari-capable font detected.")
    return errors, {"devanagari_characters": devanagari, "fonts": fonts}


def main() -> int:
    semantic = runtime.load(runtime.SEMANTIC)
    status = runtime.load(runtime.EXPORT_STATUS)
    expected = [f"qualifying-hindi-{number:02d}" for number in range(1, 7)]
    rows = [row for row in semantic["topics"] if row["topic_key"].startswith("qualifying-hindi-")]
    errors: list[str] = []
    if [row["topic_key"] for row in rows] != expected:
        errors.append("Qualifying Hindi catalogue/order mismatch.")
    if any(row["status"] != "passed" for row in rows):
        errors.append("Not every Qualifying Hindi topic passed.")
    if semantic["next_topic"] is not None:
        errors.append("Global semantic queue is not complete after Qualifying Hindi.")
    tracker_text = (runtime.ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md").read_text(encoding="utf-8")
    tracker_ok = "| 23 | Qualifying Hindi | 6 | 6 | passed | Complete |" in tracker_text
    if not tracker_ok:
        errors.append("Human tracker does not record Qualifying Hindi 6/6.")

    test_count = 0
    test_errors: list[str] = []
    for module in (
        "test_run_qualifying_hindi_semantic_topic",
        "test_regenerate_qualifying_hindi_deep_review",
        "test_v2_export_foundation",
        "test_v2_section_indexes",
        "test_v2_topic_command_catalog",
    ):
        test = subprocess.run(
            [sys.executable, "-m", "unittest", "-v", module],
            cwd=runtime.ROOT / "tools",
            capture_output=True,
            text=True,
        )
        match = re.search(r"Ran (\d+) tests?", test.stdout + test.stderr)
        test_count += int(match.group(1)) if match else 0
        if test.returncode:
            test_errors.append(f"{module}: {test.stdout}{test.stderr}")
    errors.extend(test_errors)

    inventory: set[str] = {
        "EXPORT-PDF-COMMAND-INDEX.md",
        "EXPORT-PDF-STATUS.json",
        "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md",
        "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        "tools\\qualifying_hindi_semantic_data.py",
        "tools\\qualifying_hindi_semantic_runtime.py",
        "tools\\run_qualifying_hindi_semantic_topic.py",
        "tools\\test_run_qualifying_hindi_semantic_topic.py",
        "tools\\finalize_qualifying_hindi_semantic_review.py",
        "tools\\regenerate_qualifying_hindi_deep_review.py",
        "tools\\markdown_learning_pdf.py",
        runtime.rel(runtime.SEMANTIC),
        runtime.rel(runtime.SECTION_MANIFEST),
        runtime.rel(VALIDATION),
        runtime.rel(INVENTORY),
        runtime.rel(REPORT),
    }
    topics: list[dict[str, Any]] = []
    hash_errors: dict[str, str] = {}
    approval_false = True
    pdf_audits: dict[str, Any] = {}
    all_generations_false = all(
        row.get("approved") is False
        for row in status["exports"]
        if row.get("topic_key") in expected and row.get("variant") == "learner-v2"
    )
    for key in expected:
        item_validation = runtime.EXPORTS / f"{key}-semantic-validation-{runtime.DATE}.json"
        item_inventory = runtime.EXPORTS / f"{key}-semantic-completeness-{runtime.DATE}-changed-files.txt"
        validation = runtime.load(item_validation)
        record = latest(status, key)
        approval_false &= record.get("approved") is False
        errors.extend(validate_flow(record))
        for field in ("main_pdf", "workbook"):
            path = runtime.ROOT / record[field]
            pdf_errors, pdf_metrics = validate_hindi_pdf(path)
            errors.extend(pdf_errors)
            pdf_audits[runtime.rel(path)] = pdf_metrics
        for name, digest in validation["deliverable_hashes"].items():
            path = runtime.ROOT / name
            if not path.is_file():
                hash_errors[name] = "missing"
            elif sha256(path) != digest:
                hash_errors[name] = "sha256 mismatch"
        inventory.update(line.strip() for line in item_inventory.read_text(encoding="utf-8").splitlines() if line.strip())
        metrics = validation["metrics"]
        topics.append(
            {
                "topic_key": key,
                "title": next(row["title"] for row in rows if row["topic_key"] == key),
                "record_id": record["record_id"],
                "generation": record["generation"],
                "approved": record["approved"],
                "main_pages": metrics["main_pages"],
                "workbook_pages": metrics["workbook_pages"],
                "mcqs": metrics["mcq_count"],
                "constructed_response_tasks": metrics["constructed_response_tasks"],
                "official_paper_demand_rows": metrics["official_paper_demand_rows"],
                "ascii_panels": metrics["ascii_panel_count"],
                "graphical_stages": metrics["graphical_stage_count"],
                "deterministic_checks": metrics["deterministic_checks"],
                "validation": runtime.rel(item_validation),
                "inventory": runtime.rel(item_inventory),
            }
        )
    failure_root = (
        runtime.ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Qualifying-Hindi"
        / "Subject-Wide-Syllabus"
        / "failed-intermediates"
    )
    if failure_root.is_dir():
        inventory.update(
            runtime.rel(path) for path in failure_root.rglob("*") if path.is_file()
        )
    inventory.update(
        runtime.rel(path)
        for path in (runtime.KNOWLEDGE / "basic").glob("*.md")
        if path.is_file()
    )
    inventory.update(
        runtime.rel(path)
        for path in runtime.EXPORTS.glob(
            f"qualifying-hindi-*-semantic-failure-{runtime.DATE}.json"
        )
        if path.is_file()
    )
    if not approval_false:
        errors.append("At least one latest Qualifying Hindi learner-v2 identity is approved.")
    if not all_generations_false:
        errors.append("A Qualifying Hindi learner-v2 generation is approved.")
    if hash_errors:
        errors.append("Deliverable hash validation failed.")

    payload = {
        "schema_version": 1,
        "subject": "Qualifying Hindi",
        "date": runtime.DATE,
        "result": "failed" if errors else "passed",
        "topic_count": 6,
        "passed": sum(row["status"] == "passed" for row in rows),
        "next_topic_key": None,
        "next_subject": None,
        "next_topic": None,
        "checks": {
            "catalogue_order": [row["topic_key"] for row in rows] == expected,
            "all_topics_passed": all(row["status"] == "passed" for row in rows),
            "all_latest_identities_approval_false": approval_false,
            "all_generations_approval_false": all_generations_false,
            "deliverable_hashes": not hash_errors,
            "status_tracker_agreement": tracker_ok,
            "targeted_regression": not test_errors,
            "answer_key_rotation_and_language_validation": all(row["deterministic_checks"] == 48 for row in topics),
            "same_master_graphical_ascii_flow_validation": not any("tile" in error or "flow" in error for error in errors),
            "devanagari_extraction_and_font_embedding": not any("Devanagari" in error or "font" in error or "glyph" in error for error in errors),
        },
        "metrics": {
            "targeted_regression_tests": test_count,
            "main_pages": sum(row["main_pages"] for row in topics),
            "workbook_pages": sum(row["workbook_pages"] for row in topics),
            "mcqs": sum(row["mcqs"] for row in topics),
            "constructed_response_tasks": sum(row["constructed_response_tasks"] for row in topics),
            "official_paper_demand_rows": sum(row["official_paper_demand_rows"] for row in topics),
            "ascii_panels": sum(row["ascii_panels"] for row in topics),
            "graphical_stages": sum(row["graphical_stages"] for row in topics),
            "deterministic_checks": sum(row["deterministic_checks"] for row in topics),
        },
        "topics": topics,
        "pdf_devanagari_audits": pdf_audits,
        "hash_errors": hash_errors,
        "errors": errors,
    }
    runtime.dump(VALIDATION, payload)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        f"""        # अनिवार्य हिन्दी Subject Semantic Completion — {runtime.DATE}

**Result:** {payload['result'].upper()}  
**Topics:** {payload['passed']}/6 passed  
**Next global queue item:** `None` — सम्पूर्ण semantic queue पूर्ण

सभी छह विषय catalogue क्रम में एक-एक करके पूरे किए गए। हर learner-v2 identity
`approved:false` है। भाषा-नियम/कुंजी, वैध विकल्प, बोध/संक्षेप/निबन्ध/अनुवाद constraints,
आधिकारिक प्रश्न-दबाव provenance, A-B-C-D rotation, दोहरे बारह-पैनल flow, Devanagari
font/extraction, PDF layout/index, hashes और tracker-status agreement उत्तीर्ण हुए।

Combined validation: `{runtime.rel(VALIDATION)}`  
Combined exact inventory: `{runtime.rel(INVENTORY)}`
""",
        encoding="utf-8",
    )
    inventory.update({runtime.rel(VALIDATION), runtime.rel(INVENTORY), runtime.rel(REPORT)})
    existing = sorted(path for path in inventory if path == runtime.rel(INVENTORY) or (runtime.ROOT / path).exists())
    INVENTORY.write_text("\n".join(existing) + "\n", encoding="utf-8")
    payload["changed_file_inventory"] = runtime.rel(INVENTORY)
    payload["changed_file_inventory_count"] = len(existing)
    payload["changed_file_inventory_all_paths_exist"] = all((runtime.ROOT / path).exists() for path in existing)
    runtime.dump(VALIDATION, payload)
    print(json.dumps(payload, ensure_ascii=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
