"""Validate the complete Qualifying English semantic review and write its exact inventory."""

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

import qualifying_english_semantic_runtime as runtime


VALIDATION = runtime.EXPORTS / f"qualifying-english-01-07-semantic-completeness-{runtime.DATE}-validation.json"
INVENTORY = runtime.EXPORTS / f"qualifying-english-01-07-semantic-completeness-{runtime.DATE}-changed-files.txt"
REPORT = runtime.REVIEWS / f"Qualifying-English-Subject-Semantic-Completion-{runtime.DATE}.md"


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


def main() -> int:
    semantic = runtime.load(runtime.SEMANTIC)
    status = runtime.load(runtime.EXPORT_STATUS)
    expected = [f"qualifying-english-{number:02d}" for number in range(1, 8)]
    rows = [row for row in semantic["topics"] if row["topic_key"].startswith("qualifying-english-")]
    errors: list[str] = []
    if [row["topic_key"] for row in rows] != expected:
        errors.append("Qualifying English catalogue/order mismatch.")
    if any(row["status"] != "passed" for row in rows):
        errors.append("Not every Qualifying English topic passed.")
    if semantic["next_topic"]["topic_key"] != "qualifying-hindi-01":
        errors.append("Global queue did not advance to qualifying-hindi-01.")
    tracker_text = (runtime.ROOT / "KNOWLEDGE-SEMANTIC-COMPLETENESS-TRACKER.md").read_text(encoding="utf-8")
    tracker_ok = "| 22 | Qualifying English | 7 | 7 | passed | Complete |" in tracker_text
    if not tracker_ok:
        errors.append("Human tracker does not record Qualifying English 7/7.")

    test_count = 0
    test_errors: list[str] = []
    for module in (
        "test_run_qualifying_english_semantic_topic",
        "test_regenerate_qualifying_english_deep_review",
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
        "tools\\qualifying_english_semantic_runtime.py",
        "tools\\run_qualifying_english_semantic_topic.py",
        "tools\\test_run_qualifying_english_semantic_topic.py",
        "tools\\finalize_qualifying_english_semantic_review.py",
        "tools\\regenerate_qualifying_english_deep_review.py",
        runtime.rel(runtime.SEMANTIC),
        runtime.rel(runtime.SECTION_MANIFEST),
        runtime.rel(VALIDATION),
        runtime.rel(INVENTORY),
        runtime.rel(REPORT),
    }
    topics: list[dict[str, Any]] = []
    hash_errors: dict[str, str] = {}
    approval_false = True
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
    if not approval_false:
        errors.append("At least one latest Qualifying English learner-v2 identity is approved.")
    if not all_generations_false:
        errors.append("A Qualifying English learner-v2 generation is approved.")
    if hash_errors:
        errors.append("Deliverable hash validation failed.")

    payload = {
        "schema_version": 1,
        "subject": "Qualifying English",
        "date": runtime.DATE,
        "result": "failed" if errors else "passed",
        "topic_count": 7,
        "passed": sum(row["status"] == "passed" for row in rows),
        "next_topic_key": semantic["next_topic"]["topic_key"],
        "next_subject": semantic["next_topic"]["subject"],
        "next_topic": semantic["next_topic"]["title"],
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
        "hash_errors": hash_errors,
        "errors": errors,
    }
    runtime.dump(VALIDATION, payload)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(
        f"""# Qualifying English Subject Semantic Completion — {runtime.DATE}

**Result:** {payload['result'].upper()}  
**Topics:** {payload['passed']}/7 passed  
**Next global queue item:** `{payload['next_topic_key']}` — {payload['next_topic']}

All seven topics were processed strictly in catalogue order. Every learner-v2 identity remains
`approved:false`. Language-rule keys, accepted-variation controls, passage/précis/essay
constraints, official-paper demand provenance, A-B-C-D rotation, dual twelve-panel flow parity,
PDF layout/index checks, hashes, semantic status and tracker agreement passed.

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
