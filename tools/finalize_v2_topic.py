"""Safely validate one known learner-v2 topic and refresh its trackers/indexes."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

from generate_v2_section_indexes import (
    INDEX_FILES,
    ManifestError,
    generate_section_indexes,
    load_manifest,
)
from validate_v2_export import (
    V2_VARIANT,
    validate_pdf,
    validate_tracker_record,
    validate_v2_markdown,
)


ROOT = Path(__file__).resolve().parents[1]


def load_record(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("The record file must contain one JSON object.")
    if data.get("variant") != V2_VARIANT:
        raise ValueError("The record variant must be learner-v2.")
    for field in (
        "topic_key",
        "generation",
        "record_id",
        "main_pdf",
        "workbook",
        "markdown",
    ):
        if not data.get(field):
            raise ValueError(f"The record is missing {field}.")
    return data


def load_validation_result(
    path: Path,
    record: dict[str, object],
) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("The validation result file must contain one JSON object.")
    expected_identity = (
        str(record["topic_key"]),
        int(record["generation"]),
        str(record["record_id"]),
    )
    actual_identity = (
        str(data.get("topic_key")),
        int(data.get("generation") or 0),
        str(data.get("identity")),
    )
    if actual_identity != expected_identity:
        raise ValueError(
            "The validation result identity does not match the standalone record."
        )
    return data


def upsert_record(
    tracker: dict[str, object],
    record: dict[str, object],
) -> dict[str, object]:
    exports = tracker.get("exports")
    if tracker.get("schema_version") != 2 or not isinstance(exports, list):
        raise ValueError("Tracker must use schema v2 with an exports list.")
    identity = (
        record["topic_key"],
        record["variant"],
        int(record["generation"]),
    )
    found = False
    updated: list[object] = []
    for existing in exports:
        if not isinstance(existing, dict):
            updated.append(existing)
            continue
        existing_identity = (
            existing.get("topic_key"),
            existing.get("variant"),
            int(existing.get("generation") or 1),
        )
        if existing_identity == identity:
            if found:
                raise ValueError(f"Tracker already has duplicate identity {identity}.")
            updated.append(record)
            found = True
        else:
            updated.append(existing)
    if not found:
        updated.append(record)
    result = dict(tracker)
    result["exports"] = updated
    return result


def restore_files(snapshots: dict[Path, bytes | None]) -> None:
    for path, content in snapshots.items():
        if content is None:
            if path.exists():
                path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--record-file", type=Path, required=True)
    args = parser.parse_args()

    root = args.repository_root.resolve()
    manifest_path = (
        args.manifest
        if args.manifest.is_absolute()
        else root / args.manifest
    ).resolve()
    record_path = (
        args.record_file
        if args.record_file.is_absolute()
        else root / args.record_file
    ).resolve()
    if not record_path.name.endswith("-record.json"):
        parser.error("The record file name must end with -record.json.")
    validation_result_path = record_path.with_name(
        record_path.name.removesuffix("-record.json") + "-validation.json"
    )
    tracker_path = root / "EXPORT-PDF-STATUS.json"
    global_index = root / "EXPORT-PDF-COMMAND-INDEX.md"
    staged_tracker = root / "EXPORT-PDF-STATUS.pending.json"

    try:
        manifest = load_manifest(manifest_path)
        record = load_record(record_path)
        validation_result = load_validation_result(validation_result_path, record)
        manifest_keys = {
            str(topic["topic_key"])
            for topic in manifest["topics"]
        }
        if str(record["topic_key"]) not in manifest_keys:
            raise ValueError(
                f"Record topic_key {record['topic_key']!r} is not in the section manifest."
            )

        tracker = json.loads(tracker_path.read_text(encoding="utf-8"))
        staged = upsert_record(tracker, record)
        staged_tracker.write_text(
            json.dumps(staged, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        errors = validate_tracker_record(
            staged_tracker,
            str(record["topic_key"]),
            V2_VARIANT,
            int(record["generation"]),
            repository_root=root,
            check_paths=True,
        )
        errors.extend(validate_v2_markdown(root / str(record["markdown"])))
        errors.extend(validate_pdf(root / str(record["main_pdf"])))
        errors.extend(validate_pdf(root / str(record["workbook"])))
        if errors:
            raise ValueError("\n".join(errors))

        record["validation"] = {
            "state": "passed",
            "validated_on": date.today().isoformat(),
            "validator": "tools/validate_v2_export.py",
        }
        validation_result["published"] = True
        staged = upsert_record(tracker, record)
        staged_tracker.write_text(
            json.dumps(staged, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        subject = str(manifest["subject"]["key"])
        section_key = str(manifest["section"]["key"])
        index_dir = (
            root
            / "notes"
            / subject
            / "learning-session-v2"
            / section_key
            / "indexes"
        )
        affected = [
            tracker_path,
            record_path,
            validation_result_path,
            global_index,
            *(index_dir / name for name in INDEX_FILES),
        ]
        snapshots = {
            path: path.read_bytes() if path.is_file() else None
            for path in affected
        }

        try:
            os.replace(staged_tracker, tracker_path)
            temporary_record = record_path.with_name(
                f".{record_path.name}.pending"
            )
            temporary_record.write_text(
                json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            os.replace(temporary_record, record_path)
            temporary_validation = validation_result_path.with_name(
                f".{validation_result_path.name}.pending"
            )
            temporary_validation.write_text(
                json.dumps(validation_result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            os.replace(temporary_validation, validation_result_path)
            subprocess.run(
                [sys.executable, str(root / "tools" / "generate_export_command_index.py")],
                cwd=root,
                check=True,
            )
            generate_section_indexes(root, manifest_path, tracker_path)
        except Exception:
            restore_files(snapshots)
            raise
    except (OSError, ValueError, ManifestError, json.JSONDecodeError) as exc:
        if staged_tracker.exists():
            staged_tracker.unlink()
        parser.error(str(exc))

    print(
        "Finalized "
        f"{record['topic_key']} / learner-v2 / g{int(record['generation'])}; "
        "approval was preserved exactly as supplied."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
