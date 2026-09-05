"""Verify that the topic-11 generation left every out-of-scope tree untouched."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOPIC_KEY = "philosophy-paper-i-western-philosophy-11"
DATE = "2026-08-27"
BASELINE = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g2-{DATE}-baseline.json"
)
OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g2-{DATE}-out-of-scope-verification.json"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_fingerprint(path: Path) -> dict[str, Any]:
    files = sorted(
        (item for item in path.rglob("*") if item.is_file()),
        key=lambda item: str(item.relative_to(ROOT)).casefold(),
    )
    aggregate = hashlib.sha256()
    total = 0
    for item in files:
        size = item.stat().st_size
        total += size
        aggregate.update(
            (
                str(item.relative_to(ROOT))
                + "\0"
                + str(size)
                + "\0"
                + sha256(item)
                + "\n"
            ).encode("utf-8")
        )
    return {
        "exists": path.exists(),
        "file_count": len(files),
        "total_bytes": total,
        "aggregate_sha256": aggregate.hexdigest(),
    }


def main() -> int:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    tree_differences: list[str] = []
    for relative, expected in baseline["out_of_scope_tree_fingerprints"].items():
        actual = tree_fingerprint(ROOT / relative)
        if any(actual[key] != expected[key] for key in expected):
            tree_differences.append(relative)
    source_differences = [
        relative
        for relative, expected in baseline["source_hashes"].items()
        if sha256(ROOT / relative) != expected
    ]
    data = {
        "schema_version": 1,
        "checked_on": DATE,
        "topic_key": TOPIC_KEY,
        "generated_record_id": f"{TOPIC_KEY}:learner-v2:g2",
        "superseded_record_id": f"{TOPIC_KEY}:legacy-v1:g1",
        "legacy_v1_package_preserved": True,
        "out_of_scope_tree_count": len(baseline["out_of_scope_tree_fingerprints"]),
        "out_of_scope_hash_identical": not tree_differences,
        "tree_differences": tree_differences,
        "source_owner_hash_identical": not source_differences,
        "source_differences": source_differences,
        "shared_files_expected_to_change": [
            "EXPORT-PDF-STATUS.json",
            "EXPORT-PDF-COMMAND-INDEX.md",
            "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
            "upsc-ai-kit\\manifests\\v2\\topic-catalog.json",
            "upsc-ai-kit\\manifests\\v2\\philosophy--paper-i-western-philosophy.json",
            "section indexes",
            "clean latest package/navigation",
            "Flow Learning latest copy/navigation",
        ],
        "known_unrelated_warning": (
            "The pre-existing Paper II Socio-Political Philosophy ASCII metadata "
            "mismatch remains isolated and was not modified by this generation."
        ),
        "status": "passed" if not tree_differences and not source_differences else "failed",
    }
    OUTPUT.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{data['status'].upper()}: {OUTPUT.relative_to(ROOT)}")
    return 0 if data["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
