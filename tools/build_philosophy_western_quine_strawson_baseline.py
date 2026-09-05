"""Author the topic-11 learner-v2 concurrency baseline before generation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import fitz

ROOT = Path(__file__).resolve().parents[1]
TOPIC_KEY = "philosophy-paper-i-western-philosophy-11"
SNAPSHOT_DATE = "2026-08-27"
OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{TOPIC_KEY}-learner-v2-g2-{SNAPSHOT_DATE}-baseline.json"
)

SHARED_FILES = (
    "EXPORT-PDF-STATUS.json",
    "EXPORT-PDF-COMMAND-INDEX.md",
    "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
    "upsc-ai-kit\\manifests\\v2\\topic-catalog.json",
    "upsc-ai-kit\\manifests\\v2\\philosophy--paper-i-western-philosophy.json",
)
SOURCE_FILES = (
    "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md",
    "upsc-ai-kit\\knowledge\\Philosophy\\README.md",
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\Quine-Strawson.md",
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Western-Philosophy-Dossier.md",
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\_PYQ-Western-Philosophy-2018-2025.md",
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Quine-Strawson\\Quine-Strawson_Layered-Complete-Learning-Session_2026-08-19.md",
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Quine-Strawson\\Quine-Strawson_Layered-Solved-Practice-Workbook_2026-08-19.md",
    "books\\philosphy_books\\2016_Masih_A_critical_history_of_western_philosophy.pdf",
    "books\\philosphy_books\\Robert.Audi_The.Cambridge.Dictionary.of.Philosophy.pdf",
    "books\\philosphy_books\\a_new_history_of_western_philosophy_volume_4.pdf",
    "books\\philosphy_books\\philosophy__the_classics_--_warburton_nigel_--_4_2014_--_"
    "routledge_--_0415534674_--_265dfe84ff25101d59a827ea4091b506_--_anna’s_archive.pdf",
)
OCR_TERMS = (
    "Quine",
    "Strawson",
    "analytic",
    "synonymy",
    "holism",
    "gavagai",
    "basic particular",
    "person",
    "presupposition",
)
OUT_OF_SCOPE_TREES = (
    "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
    "Paper-I-Western-Philosophy\\learning-sessions\\topic-09",
    "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
    "Paper-I-Western-Philosophy\\learning-sessions\\topic-10",
    "notes\\Learner-v2-Refreshed\\Philosophy\\Paper-I-Western-Philosophy\\"
    "learning-sessions\\topic-10",
    "notes\\Learner-v2-Refreshed\\Philosophy\\Paper-I-Western-Philosophy\\"
    "flowcharts\\topic-10",
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Quine-Strawson",
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


def ocr_audit() -> dict[str, Any]:
    audit: dict[str, Any] = {}
    for relative in SOURCE_FILES:
        if not relative.lower().endswith(".pdf"):
            continue
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        hits: dict[str, list[int]] = {}
        text_pages = 0
        with fitz.open(path) as document:
            pages = document.page_count
            for number in range(pages):
                text = document.load_page(number).get_text("text")
                if text.strip():
                    text_pages += 1
                lowered = text.casefold()
                for term in OCR_TERMS:
                    if term.casefold() in lowered and len(hits.get(term, [])) < 8:
                        hits.setdefault(term, []).append(number + 1)
        audit[path.name] = {
            "path": relative,
            "pages": pages,
            "text_pages": text_pages,
            "hits": hits,
            "sha256": sha256(path),
        }
    return audit


def main() -> int:
    tracker = json.loads((ROOT / "EXPORT-PDF-STATUS.json").read_text(encoding="utf-8"))
    existing = [
        record["record_id"]
        for record in tracker["exports"]
        if record.get("topic_key") == TOPIC_KEY
    ]
    knowledge_target = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "Philosophy"
        / "Paper-I-Western-Philosophy"
        / "learning-sessions"
        / "topic-11"
    )
    notes_target = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Philosophy"
        / "Paper-I-Western-Philosophy"
        / "learning-sessions"
        / "topic-11"
    )
    flow_target = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Philosophy"
        / "Paper-I-Western-Philosophy"
        / "flowcharts"
        / "topic-11"
    )
    ascii_spec = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / "philosophy--paper-i-western-philosophy-11-ascii-2026-08-27.json"
    )
    data = {
        "schema_version": 1,
        "snapshot_on": SNAPSHOT_DATE,
        "topic_key": TOPIC_KEY,
        "canonical_sequence_number": 11,
        "planned_generation": 2,
        "approval": False,
        "tracker_resolution": (
            "Latest existing generation is legacy-v1 g1; no learner-v2 record exists, "
            "so the resolved next learner-v2 generation is g2."
        ),
        "existing_records": existing,
        "supersedes": f"{TOPIC_KEY}:legacy-v1:g1",
        "target_absence": {
            "knowledge_g2": not (knowledge_target / "g2").exists(),
            "notes_g2": not (notes_target / "g2").exists(),
            "flow_g2": not (flow_target / "carvaka-g2").exists(),
            "ascii_g2_spec": not ascii_spec.exists(),
        },
        "shared_file_hashes": {
            relative: sha256(ROOT / relative) for relative in SHARED_FILES
        },
        "source_hashes": {
            relative: sha256(ROOT / relative) for relative in SOURCE_FILES
        },
        "out_of_scope_tree_fingerprints": {
            relative: tree_fingerprint(ROOT / relative)
            for relative in OUT_OF_SCOPE_TREES
        },
        "planned_mutable_paths": [
            "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
            "Paper-I-Western-Philosophy\\learning-sessions\\topic-11\\g2",
            "notes\\Learner-v2-Refreshed\\Philosophy\\Paper-I-Western-Philosophy\\"
            "learning-sessions\\topic-11\\g2",
            "notes\\Learner-v2-Refreshed\\Philosophy\\Paper-I-Western-Philosophy\\"
            "flowcharts\\topic-11\\carvaka-g2",
            "upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\"
            "philosophy--paper-i-western-philosophy-11-ascii-2026-08-27.json",
            "upsc-ai-kit\\manifests\\v2\\"
            "philosophy--paper-i-western-philosophy-content-specs\\"
            f"{TOPIC_KEY}-g2.json",
            "upsc-ai-kit\\manifests\\v2\\"
            "philosophy--paper-i-western-philosophy-graphical-specs\\"
            f"{TOPIC_KEY}-g2.json",
            "upsc-ai-kit\\manifests\\v2\\philosophy--paper-i-western-philosophy.json",
            "EXPORT-PDF-STATUS.json",
            "EXPORT-PDF-COMMAND-INDEX.md",
            "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
        ],
        "known_unrelated_warning": (
            "The working tree already contains unrelated pre-existing modifications "
            "and untracked files. Only the planned mutable paths above may change "
            "during this topic generation."
        ),
        "ocr_audit": ocr_audit(),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"WROTE: {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
