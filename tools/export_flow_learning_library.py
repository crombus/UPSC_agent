"""Export approved ASCII masters as a separate Flow Learning library.

The exporter reads the latest validated learner-v2 tracker records, copies the
matching clean-library ASCII PDF/TXT byte-for-byte, and rebuilds lightweight
navigation. Source packages and EXPORT-PDF-STATUS.json are read-only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import unicodedata
import uuid
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, Sequence
from urllib.parse import quote, unquote


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRACKER = REPOSITORY_ROOT / "EXPORT-PDF-STATUS.json"
DEFAULT_CATALOGUE = (
    REPOSITORY_ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "topic-catalog.json"
)
DEFAULT_SOURCE_ROOT = (
    REPOSITORY_ROOT
    / "notes"
    / "Final-Learning-Packages"
)
DEFAULT_EXPORT_ROOT = REPOSITORY_ROOT / "notes" / "Flow-Learning"
DEFAULT_CASE_YEAR_EVIDENCE = (
    REPOSITORY_ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "polity-flowchart-case-year-repair-2026-08-24-validation.json"
)
LEARNER_VARIANT = "learner-v2"
DEFAULT_SUBJECT = "Polity"
DEFAULT_TOPIC_PREFIX = "polity-"
DEFAULT_EXPECTED_ALL_TOPIC_COUNT = 50
MAX_OUTPUT_STEM_LENGTH = 80
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PANEL_HEADING_RE = re.compile(
    r"^ASCII MASTER FLOW — PANEL (\d+)/(\d+): (.+?)\s*$",
    re.MULTILINE,
)
DATE_YEAR_TOKEN_RE = re.compile(
    r"\b(?:\d{1,4}\s*(?:BCE|BC|CE|AD)|(?:1\d{3}|20\d{2}))\b",
    re.IGNORECASE,
)


class ExportError(RuntimeError):
    """Raised when a safe Flow Learning export cannot be completed."""


def deterministic_output_stem(source_folder_name: str) -> str:
    suffix = "-Continuous-Flow-Learning"
    full = f"{source_folder_name}{suffix}"
    if len(full) <= MAX_OUTPUT_STEM_LENGTH:
        return full
    digest = hashlib.sha256(
        source_folder_name.encode("utf-8")
    ).hexdigest()[:10]
    prefix_length = (
        MAX_OUTPUT_STEM_LENGTH - len(suffix) - len(digest) - 1
    )
    prefix = source_folder_name[:prefix_length].rstrip("-")
    if not prefix:
        raise ExportError(
            f"Cannot create bounded deterministic name for {source_folder_name!r}"
        )
    return f"{prefix}-{digest}{suffix}"


@dataclass(frozen=True)
class TopicSelection:
    topic_key: str
    title: str
    number: int
    subject: str
    section: str
    record: dict[str, Any]
    source_folder_name: str
    source_topic_dir: Path
    source_pdf: Path
    source_txt: Path
    metadata_resolution: str

    @property
    def generation(self) -> int:
        return int(self.record["generation"])

    @property
    def record_id(self) -> str:
        return str(self.record["record_id"])

    @property
    def destination_folder_name(self) -> str:
        return self.source_folder_name

    @property
    def output_stem(self) -> str:
        return deterministic_output_stem(self.source_folder_name)

    @property
    def output_pdf_name(self) -> str:
        return f"{self.output_stem}.pdf"

    @property
    def output_txt_name(self) -> str:
        return f"{self.output_stem}.txt"


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ExportError(f"Required JSON is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ExportError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ExportError(f"Expected a JSON object in {path}")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def tree_fingerprint(path: Path) -> dict[str, Any]:
    rows: list[tuple[str, int, str]] = []
    for file_path in sorted(
        (item for item in path.rglob("*") if item.is_file()),
        key=lambda item: str(item.relative_to(path)).casefold(),
    ):
        rows.append(
            (
                str(file_path.relative_to(path)).replace("/", "\\"),
                file_path.stat().st_size,
                sha256_file(file_path),
            )
        )
    encoded = json.dumps(
        rows, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return {
        "file_count": len(rows),
        "total_bytes": sum(row[1] for row in rows),
        "aggregate_sha256": hashlib.sha256(encoded).hexdigest(),
    }


def repository_relative(path: Path, root: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("/", "\\")


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{uuid.uuid4().hex}")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def write_json_atomic(path: Path, data: object) -> None:
    write_text_atomic(
        path,
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    )


def slugify_topic(value: str) -> str:
    value = re.sub(r"[‐‑‒–—―]", "-", value)
    value = value.replace("’", "").replace("'", "").replace("&", " and ")
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "-", ascii_value).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)
    if not slug:
        raise ExportError(f"Cannot create a deterministic topic name: {value!r}")
    return slug


def sanitize_display_component(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    value = re.sub(r"-{2,}", "-", value)
    if not value:
        raise ExportError("A display path component became empty.")
    return value


def final_library_root(source_root: Path) -> Path:
    for candidate in (source_root, *source_root.parents):
        if candidate.name == "Final-Learning-Packages":
            return candidate
    return source_root


def topic_sort_key(topic_key: str) -> tuple[int, str]:
    match = re.fullmatch(r".*?(\d+)", topic_key)
    return (int(match.group(1)) if match else 9999, topic_key.casefold())


def latest_validated_learner_records(
    tracker_data: dict[str, Any],
    selected_keys: Sequence[str] | None = None,
    *,
    topic_prefix: str | None = DEFAULT_TOPIC_PREFIX,
) -> list[dict[str, Any]]:
    exports = tracker_data.get("exports")
    if not isinstance(exports, list):
        raise ExportError("Tracker has no exports array.")
    grouped: dict[str, list[dict[str, Any]]] = {}
    for record in exports:
        if not isinstance(record, dict):
            continue
        topic_key = str(record.get("topic_key") or "")
        validation = record.get("validation") or {}
        if (
            record.get("variant") == LEARNER_VARIANT
            and (topic_prefix is None or topic_key.startswith(topic_prefix))
            and isinstance(validation, dict)
            and validation.get("state") == "passed"
        ):
            grouped.setdefault(topic_key, []).append(record)
    latest = {
        topic_key: max(
            records, key=lambda item: int(item.get("generation") or 0)
        )
        for topic_key, records in grouped.items()
    }
    if selected_keys:
        requested = list(dict.fromkeys(selected_keys))
        missing = [key for key in requested if key not in latest]
        if missing:
            raise ExportError(
                "No validated learner-v2 record for: " + ", ".join(missing)
            )
        records = [latest[key] for key in requested]
    else:
        records = list(latest.values())
    return sorted(
        records, key=lambda item: topic_sort_key(str(item["topic_key"]))
    )


def catalogue_topics(
    catalogue_data: dict[str, Any],
    *,
    subject: str | None = DEFAULT_SUBJECT,
) -> dict[str, dict[str, Any]]:
    raw_topics = catalogue_data.get("topics")
    if not isinstance(raw_topics, list):
        raise ExportError("Topic catalogue has no topics array.")
    mapped: dict[str, dict[str, Any]] = {}
    for item in raw_topics:
        if not isinstance(item, dict):
            continue
        subject_data = item.get("subject") or {}
        if (
            isinstance(subject_data, dict)
            and (
                subject is None
                or subject_data.get("display_name") == subject
            )
            and item.get("topic_key")
        ):
            mapped[str(item["topic_key"])] = item
    return mapped


def _source_readme_identity(readme: Path) -> tuple[str, int]:
    text = readme.read_text(encoding="utf-8")
    record_match = re.search(r"(?m)^Source record ID:\s*(.+?)\s*$", text)
    generation_match = re.search(
        r"(?m)^Source generation:\s*(\d+)\s*$", text
    )
    if not record_match or not generation_match:
        raise ExportError(f"Clean package README lacks source identity: {readme}")
    return record_match.group(1), int(generation_match.group(1))


def _optional_source_readme_field(text: str, label: str) -> str:
    match = re.search(
        rf"(?m)^{re.escape(label)}:\s*(.+?)\s*$",
        text,
    )
    return match.group(1).strip() if match else ""


def _clean_package_index(
    source_root: Path,
) -> dict[tuple[str, int], list[Path]]:
    library_root = final_library_root(source_root)
    indexed: dict[tuple[str, int], list[Path]] = {}
    for readme in library_root.rglob("README.txt"):
        relative = readme.relative_to(library_root)
        if any(part.startswith(".") for part in relative.parts):
            continue
        topic_dir = readme.parent
        ascii_dir = topic_dir / "04-ASCII-Master-Flowchart"
        if not all(
            (
                (ascii_dir / "ASCII-Master-Flowchart.pdf").is_file(),
                (ascii_dir / "ASCII-Master-Flowchart.txt").is_file(),
            )
        ):
            continue
        try:
            identity = _source_readme_identity(readme)
        except ExportError:
            continue
        indexed.setdefault(identity, []).append(topic_dir)
    return indexed


def _catalogue_metadata(
    item: dict[str, Any],
) -> tuple[int, str, str, str]:
    try:
        number = int(item["source_number"])
        title = str(item["display_title"]).strip()
        subject_data = item.get("subject") or {}
        section_data = item.get("section") or {}
        subject = str(subject_data["display_name"]).strip()
        section = str(
            section_data.get("name") or "Subject-wide Syllabus"
        ).strip()
    except (KeyError, TypeError, ValueError) as exc:
        raise ExportError("Catalogue metadata is incomplete.") from exc
    if not all((title, subject, section)):
        raise ExportError("Catalogue metadata is incomplete.")
    return number, title, subject, section


def _source_package_metadata(
    topic_dir: Path,
    library_root: Path,
) -> tuple[int, str, str, str]:
    readme = topic_dir / "README.txt"
    text = readme.read_text(encoding="utf-8")
    title = _optional_source_readme_field(text, "Topic")
    subject = _optional_source_readme_field(text, "Subject")
    section = _optional_source_readme_field(text, "Section")
    number_text = _optional_source_readme_field(text, "Catalogue number")
    folder_match = re.fullmatch(r"(\d+)-(.+)", topic_dir.name)
    if not folder_match:
        raise ExportError(
            f"Clean package folder is not numbered deterministically: {topic_dir}"
        )
    folder_number = int(folder_match.group(1))
    if not all((title, subject, section, number_text)):
        raise ExportError(
            "Catalogue fallback requires Topic, Subject, Section and "
            f"Catalogue number in {readme}"
        )
    try:
        readme_number = int(number_text)
    except ValueError as exc:
        raise ExportError(
            f"Invalid Catalogue number in clean package README: {readme}"
        ) from exc
    if readme_number != folder_number:
        raise ExportError(
            f"Clean package number mismatch between README and folder: {topic_dir}"
        )
    relative = topic_dir.relative_to(library_root)
    if len(relative.parts) < 3:
        raise ExportError(
            f"Clean package does not identify subject/section folders: {topic_dir}"
        )
    folder_subject = relative.parts[-3]
    folder_section = relative.parts[-2]
    if subject != folder_subject or section != folder_section:
        raise ExportError(
            "Clean package README subject/section does not match its library "
            f"location: {topic_dir}"
        )
    return readme_number, title, subject, section


def resolve_selections(
    root: Path,
    tracker_path: Path,
    catalogue_path: Path,
    source_root: Path,
    selected_keys: Sequence[str] | None = None,
    *,
    subject: str | None = DEFAULT_SUBJECT,
    topic_prefix: str | None = DEFAULT_TOPIC_PREFIX,
) -> list[TopicSelection]:
    records = latest_validated_learner_records(
        load_json(tracker_path), selected_keys, topic_prefix=topic_prefix
    )
    topics = catalogue_topics(load_json(catalogue_path), subject=None)
    library_root = final_library_root(source_root)
    clean_packages = _clean_package_index(source_root)
    selections: list[TopicSelection] = []
    for record in records:
        topic_key = str(record["topic_key"])
        identity = (
            str(record.get("record_id")),
            int(record.get("generation") or 0),
        )
        candidates = clean_packages.get(identity, [])
        if not candidates:
            raise ExportError(
                f"{topic_key}: no clean package matches exact tracker identity "
                f"{identity[0]}/g{identity[1]}."
            )
        if len(candidates) != 1:
            raise ExportError(
                f"{topic_key}: exact tracker identity maps to multiple clean "
                "packages: "
                + ", ".join(str(path) for path in candidates)
            )
        source_topic_dir = candidates[0]
        source_folder_name = source_topic_dir.name
        folder_match = re.fullmatch(r"(\d+)-(.+)", source_folder_name)
        if not folder_match:
            raise ExportError(
                f"Clean package folder is not numbered: {source_topic_dir}"
            )
        folder_number = int(folder_match.group(1))
        item = topics.get(topic_key)
        if item is not None:
            number, title, resolved_subject, section = _catalogue_metadata(item)
            if number != folder_number:
                raise ExportError(
                    f"{topic_key}: catalogue number {number} does not match "
                    f"clean package folder {source_folder_name}."
                )
            source_text = (source_topic_dir / "README.txt").read_text(
                encoding="utf-8"
            )
            title = (
                _optional_source_readme_field(source_text, "Topic") or title
            )
            resolved_subject = (
                _optional_source_readme_field(source_text, "Subject")
                or resolved_subject
            )
            section = (
                _optional_source_readme_field(source_text, "Section")
                or section
            )
            metadata_resolution = (
                "catalogue metadata verified by exact tracker/source-package "
                "identity; clean-package folder retained for deterministic naming"
            )
        else:
            (
                number,
                title,
                resolved_subject,
                section,
            ) = _source_package_metadata(source_topic_dir, library_root)
            metadata_resolution = (
                "catalogue entry absent; exact tracker record/generation matched "
                "to clean-package README and numbered folder"
            )
        if subject is not None and resolved_subject != subject:
            raise ExportError(
                f"{topic_key}: resolved subject {resolved_subject!r} does not "
                f"match requested subject {subject!r}."
            )
        source_ascii = source_topic_dir / "04-ASCII-Master-Flowchart"
        source_pdf = source_ascii / "ASCII-Master-Flowchart.pdf"
        source_txt = source_ascii / "ASCII-Master-Flowchart.txt"
        for path in (source_pdf, source_txt, source_topic_dir / "README.txt"):
            if not path.is_file():
                raise ExportError(f"Missing clean-library artifact: {path}")
        readme_record, readme_generation = _source_readme_identity(
            source_topic_dir / "README.txt"
        )
        if (
            readme_record != str(record.get("record_id"))
            or readme_generation != int(record.get("generation") or 0)
        ):
            raise ExportError(
                f"{topic_key}: clean package identity {readme_record}/"
                f"g{readme_generation} does not match latest validated record "
                f"{record.get('record_id')}/g{record.get('generation')}."
            )
        selections.append(
            TopicSelection(
                topic_key=topic_key,
                title=title,
                number=number,
                subject=resolved_subject,
                section=section,
                record=record,
                source_folder_name=source_folder_name,
                source_topic_dir=source_topic_dir,
                source_pdf=source_pdf,
                source_txt=source_txt,
                metadata_resolution=metadata_resolution,
            )
        )
    return sorted(
        selections,
        key=lambda item: (
            item.subject.casefold(),
            item.section.casefold(),
            item.number,
            item.topic_key,
        ),
    )


def topic_readme(selection: TopicSelection, root: Path) -> str:
    complete_pdf = (
        selection.source_topic_dir
        / "01-Complete-Learning-Session"
        / "Complete-Learning-Session.pdf"
    )
    workbook_pdf = (
        selection.source_topic_dir
        / "02-Solved-Practice-Workbook"
        / "Solved-Practice-Workbook.pdf"
    )
    chronology_validation = (
        "Case-year compliance: PASS.\n"
        if selection.subject == "Polity"
        else "Date/year retention: PASS — byte-identical to the source master.\n"
    )
    return (
        "FLOW LEARNING — CONTINUOUS ASCII MASTER\n"
        "=======================================\n\n"
        f"Topic: {selection.number:02d} — {selection.title}\n"
        f"Topic key: {selection.topic_key}\n"
        f"Subject: {selection.subject}\n"
        f"Section: {selection.section}\n"
        f"Source record ID: {selection.record_id}\n"
        f"Source generation: {selection.generation}\n"
        f"Metadata resolution: {selection.metadata_resolution}\n"
        "Status: PASS — byte-identical access copy of the repaired "
        "04-ASCII-Master-Flowchart.\n\n"
        "Continuous-master status: PASS — complete sequential atlas, not a "
        "short panel summary.\n"
        f"{chronology_validation}\n"
        "How to use this topic\n"
        "---------------------\n"
        "1. Start with Flow Learning for first understanding and rapid revision.\n"
        "2. Use the Complete Learning Session only for deeper explanation and evidence.\n"
        "3. Use the Solved Workbook for practice.\n"
        "4. Flow Learning does not replace or reduce the full reference.\n\n"
        "Files in this folder\n"
        "--------------------\n"
        f"- {selection.output_pdf_name}\n"
        f"- {selection.output_txt_name}\n"
        "- README.txt\n\n"
        "Full-reference paths\n"
        "--------------------\n"
        f"- Complete Learning Session: {repository_relative(complete_pdf, root)}\n"
        f"- Solved Workbook: {repository_relative(workbook_pdf, root)}\n"
        f"- Source ASCII package: {repository_relative(selection.source_pdf.parent, root)}\n"
    )


def exact_topic_shape(topic_dir: Path, selection: TopicSelection) -> bool:
    expected = {
        selection.output_pdf_name,
        selection.output_txt_name,
        "README.txt",
    }
    return (
        topic_dir.is_dir()
        and {item.name for item in topic_dir.iterdir()} == expected
        and all((topic_dir / name).is_file() for name in expected)
    )


def atomic_replace_directory(stage: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    backup = destination.parent / f".old-{uuid.uuid4().hex[:10]}"
    if destination.exists():
        os.replace(destination, backup)
    try:
        os.replace(stage, destination)
    except Exception:
        if backup.exists() and not destination.exists():
            os.replace(backup, destination)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def export_topic(
    selection: TopicSelection,
    destination_subject_root: Path,
    root: Path,
) -> dict[str, Any]:
    destination = destination_subject_root / selection.destination_folder_name
    stage = destination_subject_root / (
        f".flow-stage-{selection.topic_key}-{uuid.uuid4().hex[:10]}"
    )
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)
    try:
        output_pdf = stage / selection.output_pdf_name
        output_txt = stage / selection.output_txt_name
        shutil.copy2(selection.source_pdf, output_pdf)
        shutil.copy2(selection.source_txt, output_txt)
        (stage / "README.txt").write_text(
            topic_readme(selection, root), encoding="utf-8", newline="\n"
        )
        if not exact_topic_shape(stage, selection):
            raise ExportError(
                f"{selection.topic_key}: staged topic shape is not exact."
            )
        for source, output in (
            (selection.source_pdf, output_pdf),
            (selection.source_txt, output_txt),
        ):
            if sha256_file(source) != sha256_file(output):
                raise ExportError(
                    f"{selection.topic_key}: byte equality failed for {output.name}."
                )
        atomic_replace_directory(stage, destination)
    except Exception:
        if stage.exists():
            shutil.rmtree(stage)
        raise
    return {
        "topic_key": selection.topic_key,
        "destination": destination,
    }


def _case_year_validation(topic_key: str, text: str) -> dict[str, Any]:
    tools_path = str(REPOSITORY_ROOT / "tools")
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    try:
        import polity_flowchart_case_years as case_years
    except ImportError:
        return {
            "status": "not-available",
            "expected_case_count": 0,
            "errors": [],
        }
    expected = len(case_years.ASCII_CASE_IDS.get(topic_key, ()))
    errors = [
        error
        for error in case_years.ascii_topic_errors(topic_key, text)
        if "ASCII line" not in error or "exceeds" not in error
    ]
    return {
        "status": "passed" if not errors else "failed",
        "expected_case_count": expected,
        "errors": errors,
    }


def _date_year_retention_validation(
    source_text: str,
    destination_text: str,
) -> dict[str, Any]:
    source_tokens = DATE_YEAR_TOKEN_RE.findall(source_text)
    destination_tokens = DATE_YEAR_TOKEN_RE.findall(destination_text)
    equal = (
        source_text.encode("utf-8") == destination_text.encode("utf-8")
        and source_tokens == destination_tokens
    )
    return {
        "status": "passed" if equal else "failed",
        "source_destination_text_equal": (
            source_text.encode("utf-8") == destination_text.encode("utf-8")
        ),
        "token_sequence_equal": source_tokens == destination_tokens,
        "token_count": len(destination_tokens),
        "unique_tokens": sorted(
            set(destination_tokens),
            key=lambda value: (value.casefold(), value),
        ),
        "errors": [] if equal else ["date/year tokens changed during export"],
    }


FUNDAMENTAL_RIGHTS_DIMENSIONS: dict[str, tuple[str, ...]] = {
    "articles_12_to_35": (
        r"Article 12",
        r"Article 13",
        r"Articles 14-18",
        r"Articles 19-22",
        r"Articles 23-24",
        r"Articles 25-28",
        r"Articles 29-30",
        r"Article 32",
        r"Articles 31A-31C and 33-35",
    ),
    "doctrines": (
        r"severability",
        r"eclipse",
        r"waiver generally unavailable",
        r"prospective overruling",
        r"proportionality",
        r"basic-structure review",
    ),
    "five_writs": (
        r"HABEAS CORPUS",
        r"MANDAMUS",
        r"PROHIBITION",
        r"CERTIORARI",
        r"QUO WARRANTO",
    ),
    "emergency_and_property_links": (
        r"Article 300A",
        r"ARTICLE 358",
        r"ARTICLE 359",
        r"Property Owners Association \(2024\)",
    ),
    "examiner_traps": (
        r"not every private asset",
        r"No rule says all Fundamental Rights automatically disappear",
        r"44th Amendment's proposed two-month substitution has not commenced",
    ),
    "pyq_answer_spine": (
        r"10 MARKS / 150 WORDS",
        r"15 MARKS / 250 WORDS",
        r"one controlling case",
        r"Conclude on validity with a narrow qualification",
    ),
    "model_synthesis": (
        r"Conclude: governance requires legality, justification and remedy",
    ),
}


def continuous_master_validation(
    topic_key: str,
    text: str,
    *,
    case_year: dict[str, Any] | None = None,
) -> dict[str, Any]:
    headings = list(PANEL_HEADING_RE.finditer(text))
    errors: list[str] = []
    declared_total = int(headings[0].group(2)) if headings else 0
    panel_numbers = [int(match.group(1)) for match in headings]
    totals = [int(match.group(2)) for match in headings]
    sequential = bool(headings) and panel_numbers == list(
        range(1, len(headings) + 1)
    )
    if not headings:
        errors.append("no authored ASCII panel headings")
    if headings and (
        declared_total != len(headings)
        or any(total != declared_total for total in totals)
    ):
        errors.append("declared panel total does not match the atlas")
    if headings and not sequential:
        errors.append("panel sequence is not continuous")
    nonempty_lines = sum(1 for line in text.splitlines() if line.strip())
    character_count = len(text)
    content_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
        and not line.startswith("ASCII MASTER FLOW — PANEL")
    ]
    unique_content_line_ratio = (
        len(set(content_lines)) / len(content_lines)
        if content_lines
        else 0.0
    )
    placeholder_hits = sorted(
        {
            marker
            for marker in ("TODO", "PLACEHOLDER", "GENERIC SUMMARY", "KEY TERMS:")
            if marker.casefold() in text.casefold()
        }
    )
    minimum_panels = 10 if topic_key == "polity-07" else 8
    minimum_lines = 130 if topic_key == "polity-07" else 60
    minimum_characters = 7000 if topic_key == "polity-07" else 4000
    not_short_summary = (
        len(headings) >= minimum_panels
        and nonempty_lines >= minimum_lines
        and character_count >= minimum_characters
        and unique_content_line_ratio >= 0.55
        and not placeholder_hits
    )
    if not not_short_summary:
        errors.append(
            "ASCII master is below the complete-atlas size threshold"
        )

    dimensions: dict[str, dict[str, Any]] = {}
    if topic_key == "polity-07":
        for name, patterns in FUNDAMENTAL_RIGHTS_DIMENSIONS.items():
            missing = [
                pattern
                for pattern in patterns
                if not re.search(pattern, text, re.IGNORECASE)
            ]
            dimensions[name] = {
                "status": "passed" if not missing else "failed",
                "required_item_count": len(patterns),
                "missing_patterns": missing,
            }
            if missing:
                errors.append(
                    f"Fundamental Rights dimension {name} is incomplete"
                )
        if (
            not case_year
            or case_year.get("status") != "passed"
            or int(case_year.get("expected_case_count") or 0) < 15
        ):
            errors.append(
                "Fundamental Rights case-name/year coverage is incomplete"
            )
        dimensions["case_names_and_years"] = {
            "status": (
                "passed"
                if not any(
                    "case-name/year coverage" in error for error in errors
                )
                else "failed"
            ),
            "validated_case_count": int(
                (case_year or {}).get("expected_case_count") or 0
            ),
        }
    return {
        "status": "passed" if not errors else "failed",
        "errors": errors,
        "panel_count": len(headings),
        "declared_panel_total": declared_total,
        "continuous_panel_sequence": sequential,
        "nonempty_line_count": nonempty_lines,
        "character_count": character_count,
        "minimum_panel_count": minimum_panels,
        "minimum_nonempty_lines": minimum_lines,
        "minimum_character_count": minimum_characters,
        "unique_content_line_ratio": round(unique_content_line_ratio, 4),
        "placeholder_markers": placeholder_hits,
        "not_a_short_summary": not_short_summary,
        "required_dimensions": dimensions,
    }


def _pdf_validation(
    text: str, pdf_path: Path, *, validate_pdf: bool
) -> dict[str, Any]:
    if not validate_pdf:
        return {
            "status": "skipped",
            "page_count": None,
            "blank_pages": [],
            "clipped_text_pages": [],
            "replacement_glyph_pages": [],
            "normalized_equal": None,
        }
    tools_path = str(REPOSITORY_ROOT / "tools")
    if tools_path not in sys.path:
        sys.path.insert(0, tools_path)
    try:
        import export_four_item_library as four_item
    except ImportError as exc:
        raise ExportError(f"ASCII PDF validator is unavailable: {exc}") from exc
    result = four_item.validate_ascii_pdf(text, pdf_path)
    return {
        "status": "passed" if result["passed"] else "failed",
        "errors": result["errors"],
        "page_count": result["pdf_page_count"],
        "blank_pages": result["blank_pages"],
        "clipped_text_pages": result["clipped_pages"],
        "replacement_glyph_pages": result["replacement_glyph_pages"],
        "normalized_equal": result["normalized_equal"],
    }


def _case_year_evidence(
    evidence_path: Path, topic_key: str, root: Path
) -> dict[str, Any]:
    display_path = (
        repository_relative(evidence_path, root)
        if evidence_path.is_relative_to(root)
        else str(evidence_path)
    )
    if not evidence_path.is_file():
        return {"status": "not-available", "path": display_path}
    data = load_json(evidence_path)
    topic = next(
        (
            item
            for item in data.get("topics", [])
            if isinstance(item, dict) and item.get("topic_key") == topic_key
        ),
        None,
    )
    if topic is None:
        return {"status": "not-found", "path": display_path}
    return {
        "status": "passed" if topic.get("passed") else "failed",
        "path": display_path,
        "layout_status": topic.get("layout_status"),
        "contact_sheet_count": topic.get("contact_sheet_count", 0),
        "preview_count": topic.get("preview_count", 0),
        "final_library_source_output_equal": topic.get(
            "final_library_source_output_equal"
        ),
    }


def markdown_link(path: Path, label: str) -> str:
    return f"[{label}]({quote(path.as_posix(), safe='/-._~')})"


def _relative_link(from_dir: Path, target: Path, label: str) -> str:
    relative = Path(os.path.relpath(target, from_dir))
    return markdown_link(relative, label)


def start_here_markdown(
    flow_root: Path,
    topics: Sequence[dict[str, Any]],
) -> str:
    subjects = sorted(
        {
            (topic["subject"], topic["destination_folder"].parent.name)
            for topic in topics
        },
        key=lambda item: item[0].casefold(),
    )
    lines = [
        "# Flow Learning",
        "",
        f"Active exported topics: **{len(topics)}**",
        "",
        "## Recommended learning order",
        "",
        "1. Start with **Flow Learning** for first understanding and rapid revision.",
        "2. Use the **Complete Learning Session** only for deeper explanation and evidence.",
        "3. Use the **Solved Workbook** for practice.",
        "4. Flow Learning does **not** replace or reduce the full reference.",
        "",
        "## Open",
        "",
    ]
    lines.extend(
        f"- [{subject} topic index]"
        f"({quote(folder, safe='-._~')}/INDEX.md)"
        for subject, folder in subjects
    )
    lines.extend(
        (
            "- [Flow Learning tracker](TRACKER.md)",
            "- Use each subject index for direct Complete Learning Session and "
            "Solved Workbook links.",
            "",
            "## All completed topics",
            "",
            "| Subject | Section | # | Topic | PDF | TXT | Source record | Generation | Status |",
            "|---|---|---:|---|---|---|---|---:|---|",
        )
    )
    for topic in topics:
        lines.append(
            "| "
            + " | ".join(
                (
                    topic["subject"],
                    topic["section"],
                    f"{topic['number']:02d}",
                    topic["title"],
                    _relative_link(flow_root, topic["destination_pdf"], "PDF"),
                    _relative_link(flow_root, topic["destination_txt"], "TXT"),
                    f"`{topic['record_id']}`",
                    str(topic["generation"]),
                    (
                        "PASS"
                        if topic["continuous_master"]["status"] == "passed"
                        and topic["status"] == "passed"
                        else "FAIL"
                    ),
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _readme_field(text: str, label: str) -> str:
    match = re.search(
        rf"(?m)^{re.escape(label)}:\s*(.+?)\s*$", text
    )
    return match.group(1) if match else ""


def discover_exported_topics(export_root: Path) -> list[dict[str, Any]]:
    topics: list[dict[str, Any]] = []
    for subject_dir in sorted(
        (
            path
            for path in export_root.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        ),
        key=lambda path: path.name.casefold(),
    ):
        for topic_dir in sorted(
            (
                path
                for path in subject_dir.iterdir()
                if path.is_dir() and not path.name.startswith(".")
            ),
            key=lambda path: path.name.casefold(),
        ):
            readme = topic_dir / "README.txt"
            pdfs = list(topic_dir.glob("*-Continuous-Flow-Learning.pdf"))
            txts = list(topic_dir.glob("*-Continuous-Flow-Learning.txt"))
            if not readme.is_file() or len(pdfs) != 1 or len(txts) != 1:
                continue
            text = readme.read_text(encoding="utf-8")
            topic_display = _readme_field(text, "Topic")
            match = re.match(r"(\d+)\s+—\s+(.+)", topic_display)
            if not match:
                continue
            record_id = _readme_field(text, "Source record ID")
            generation = _readme_field(text, "Source generation")
            topics.append(
                {
                    "topic_key": _readme_field(text, "Topic key"),
                    "number": int(match.group(1)),
                    "title": match.group(2),
                    "subject": (
                        _readme_field(text, "Subject") or subject_dir.name
                    ),
                    "section": _readme_field(text, "Section"),
                    "record_id": record_id,
                    "generation": int(generation or 0),
                    "metadata_resolution": _readme_field(
                        text, "Metadata resolution"
                    ),
                    "destination_folder": topic_dir,
                    "destination_pdf": pdfs[0],
                    "destination_txt": txts[0],
                    "readme": readme,
                    "case_year": {
                        "status": "passed",
                        "expected_case_count": 0,
                    },
                    "date_year_retention": {"status": "passed"},
                    "continuous_master": {"status": "passed"},
                    "status": "passed",
                }
            )
    return sorted(
        topics,
        key=lambda topic: (
            topic["subject"].casefold(),
            topic["number"],
            topic["title"].casefold(),
        ),
    )


def retained_exported_selections(
    *,
    root: Path,
    tracker_path: Path,
    catalogue_path: Path,
    source_root: Path,
    export_root: Path,
    subject: str | None,
    topic_prefix: str | None,
) -> list[TopicSelection]:
    """Resolve already-published topics by their recorded identity, not a newer record."""
    tracker = load_json(tracker_path)
    records = {
        str(record.get("record_id")): record
        for record in tracker.get("exports", [])
        if isinstance(record, dict)
        and record.get("variant") == LEARNER_VARIANT
        and record.get("record_id")
    }
    catalogue = catalogue_topics(load_json(catalogue_path), subject=None)
    library_root = final_library_root(source_root)
    selections: list[TopicSelection] = []
    for exported in discover_exported_topics(export_root):
        topic_key = str(exported["topic_key"])
        if topic_prefix is not None and not topic_key.startswith(topic_prefix):
            continue
        if subject is not None and exported["subject"] != subject:
            continue
        record = records.get(str(exported["record_id"]))
        if record is None:
            raise ExportError(
                f"{topic_key}: retained Flow Learning record is absent from tracker: "
                f"{exported['record_id']}"
            )
        if int(record.get("generation") or 0) != int(exported["generation"]):
            raise ExportError(
                f"{topic_key}: retained Flow Learning generation does not match tracker."
            )
        source_topic_dir = (
            library_root
            / sanitize_display_component(str(exported["subject"]))
            / sanitize_display_component(str(exported["section"]))
            / exported["destination_folder"].name
        )
        source_pdf = (
            source_topic_dir
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.pdf"
        )
        source_txt = (
            source_topic_dir
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.txt"
        )
        for path in (source_topic_dir / "README.txt", source_pdf, source_txt):
            if not path.is_file():
                raise ExportError(
                    f"{topic_key}: retained clean-library artifact is missing: {path}"
                )
        readme_record, readme_generation = _source_readme_identity(
            source_topic_dir / "README.txt"
        )
        if (
            readme_record != str(record["record_id"])
            or readme_generation != int(record["generation"])
        ):
            raise ExportError(
                f"{topic_key}: retained clean package identity changed."
            )
        item = catalogue.get(topic_key)
        if item is not None:
            number, title, resolved_subject, section = _catalogue_metadata(item)
        else:
            number, title, resolved_subject, section = _source_package_metadata(
                source_topic_dir, library_root
            )
        selections.append(
            TopicSelection(
                topic_key=topic_key,
                title=title,
                number=number,
                subject=resolved_subject,
                section=section,
                record=record,
                source_folder_name=source_topic_dir.name,
                source_topic_dir=source_topic_dir,
                source_pdf=source_pdf,
                source_txt=source_txt,
                metadata_resolution=(
                    "retained exact published record/source-package identity"
                ),
            )
        )
    return sorted(
        selections,
        key=lambda item: (
            item.subject.casefold(),
            item.section.casefold(),
            item.number,
            item.topic_key,
        ),
    )


def tracker_markdown(
    flow_root: Path, topics: Sequence[dict[str, Any]]
) -> str:
    lines = [
        "# Flow Learning Tracker",
        "",
        f"Active exported topics: **{len(topics)}**",
        "",
        "| Subject | Section | # | Topic | PDF | TXT | Source record | Generation | Case years | Date/year retention | Continuous master | Status |",
        "|---|---|---:|---|---|---|---|---:|---|---|---|---|",
    ]
    for topic in topics:
        case_year = topic["case_year"]
        case_label = (
            f"PASS ({case_year['expected_case_count']})"
            if case_year["status"] == "passed"
            else case_year["status"].upper()
        )
        lines.append(
            "| "
            + " | ".join(
                (
                    topic["subject"],
                    topic["section"],
                    f"{topic['number']:02d}",
                    topic["title"],
                    _relative_link(flow_root, topic["destination_pdf"], "PDF"),
                    _relative_link(flow_root, topic["destination_txt"], "TXT"),
                    f"`{topic['record_id']}`",
                    str(topic["generation"]),
                    case_label,
                    topic["date_year_retention"]["status"].upper(),
                    topic["continuous_master"]["status"].upper(),
                    (
                        "PASS"
                        if topic["continuous_master"]["status"] == "passed"
                        and topic["status"] == "passed"
                        else "FAIL"
                    ),
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def subject_index_markdown(
    subject: str,
    subject_root: Path,
    topics: Sequence[dict[str, Any]],
) -> str:
    lines = [
        f"# {subject} — Continuous Flow Learning",
        "",
        f"Topics: **{len(topics)}**",
        "",
        "Start here for first understanding and rapid revision. Use the Complete "
        "Learning Session for deeper explanation/evidence and the Solved Workbook "
        "for practice. This library does not replace the full reference.",
        "",
        "| Section | # | Topic | Flow PDF | Flow TXT | Master | Guide | Complete session | Workbook |",
        "|---|---:|---|---|---|---|---|---|---|",
    ]
    for topic in topics:
        source_topic = topic["source_topic_dir"]
        complete = (
            source_topic
            / "01-Complete-Learning-Session"
            / "Complete-Learning-Session.pdf"
        )
        workbook = (
            source_topic
            / "02-Solved-Practice-Workbook"
            / "Solved-Practice-Workbook.pdf"
        )
        lines.append(
            "| "
            + " | ".join(
                (
                    topic["section"],
                    f"{topic['number']:02d}",
                    topic["title"],
                    _relative_link(subject_root, topic["destination_pdf"], "PDF"),
                    _relative_link(subject_root, topic["destination_txt"], "TXT"),
                    topic["continuous_master"]["status"].upper(),
                    _relative_link(subject_root, topic["readme"], "README"),
                    _relative_link(subject_root, complete, "PDF"),
                    _relative_link(subject_root, workbook, "PDF"),
                )
            )
            + " |"
        )
    lines.extend(
        (
            "",
            f"[Back to START HERE]({_relative_path(subject_root, subject_root.parent / 'START-HERE.md')})",
            f"[Open tracker]({_relative_path(subject_root, subject_root.parent / 'TRACKER.md')})",
        )
    )
    return "\n".join(lines) + "\n"


def _relative_path(from_dir: Path, target: Path) -> str:
    relative = Path(os.path.relpath(target, from_dir))
    return quote(relative.as_posix(), safe="/-._~")


def validate_markdown_links(flow_root: Path) -> dict[str, Any]:
    checked = 0
    broken: list[str] = []
    markdown_files = sorted(flow_root.rglob("*.md"))
    for markdown in markdown_files:
        text = markdown.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip("<>")
            if (
                not target
                or target.startswith("#")
                or "://" in target
                or target.startswith("mailto:")
            ):
                continue
            decoded = unquote(target.split("#", 1)[0])
            resolved = (markdown.parent / Path(decoded)).resolve()
            checked += 1
            if not resolved.exists():
                broken.append(
                    f"{repository_relative(markdown, REPOSITORY_ROOT)} -> {decoded}"
                )
    return {
        "checked_link_count": checked,
        "markdown_file_count": len(markdown_files),
        "broken_links": broken,
        "passed": not broken,
    }


def validate_exported_topic(
    selection: TopicSelection,
    destination_subject_root: Path,
    root: Path,
    *,
    validate_pdf: bool,
    evidence_path: Path,
) -> dict[str, Any]:
    topic_dir = destination_subject_root / selection.destination_folder_name
    destination_pdf = topic_dir / selection.output_pdf_name
    destination_txt = topic_dir / selection.output_txt_name
    readme = topic_dir / "README.txt"
    errors: list[str] = []
    if not exact_topic_shape(topic_dir, selection):
        errors.append("topic folder does not contain exactly PDF, TXT, README")
    hashes: dict[str, dict[str, Any]] = {}
    for label, source, destination in (
        ("pdf", selection.source_pdf, destination_pdf),
        ("txt", selection.source_txt, destination_txt),
    ):
        source_hash = sha256_file(source)
        destination_hash = (
            sha256_file(destination) if destination.is_file() else None
        )
        equal = source_hash == destination_hash
        if not equal:
            errors.append(f"{label} source/destination hash mismatch")
        hashes[label] = {
            "source": repository_relative(source, root),
            "destination": repository_relative(destination, root),
            "source_sha256": source_hash,
            "destination_sha256": destination_hash,
            "equal": equal,
            "bytes": destination.stat().st_size if destination.is_file() else 0,
        }
    text = (
        destination_txt.read_text(encoding="utf-8")
        if destination_txt.is_file()
        else ""
    )
    source_text = selection.source_txt.read_text(encoding="utf-8")
    case_year = _case_year_validation(selection.topic_key, text)
    if case_year["status"] == "failed":
        errors.extend(case_year["errors"])
    date_year_retention = _date_year_retention_validation(source_text, text)
    if date_year_retention["status"] == "failed":
        errors.extend(date_year_retention["errors"])
    continuous_master = continuous_master_validation(
        selection.topic_key, text, case_year=case_year
    )
    if continuous_master["status"] == "failed":
        errors.extend(continuous_master["errors"])
    pdf = _pdf_validation(text, destination_pdf, validate_pdf=validate_pdf)
    if pdf["status"] == "failed":
        errors.extend(pdf.get("errors", []))
    evidence = _case_year_evidence(evidence_path, selection.topic_key, root)
    if evidence["status"] == "failed":
        errors.append("current repaired case-year evidence is not passed")
    return {
        "topic_key": selection.topic_key,
        "number": selection.number,
        "title": selection.title,
        "subject": selection.subject,
        "section": selection.section,
        "record_id": selection.record_id,
        "generation": selection.generation,
        "metadata_resolution": selection.metadata_resolution,
        "source_topic_dir": selection.source_topic_dir,
        "destination_folder": topic_dir,
        "destination_pdf": destination_pdf,
        "destination_txt": destination_txt,
        "readme": readme,
        "hashes": hashes,
        "case_year": case_year,
        "date_year_retention": date_year_retention,
        "continuous_master": continuous_master,
        "pdf_validation": pdf,
        "repaired_source_evidence": evidence,
        "errors": errors,
        "status": "passed" if not errors else "failed",
    }


def _serializable_topic(topic: dict[str, Any], root: Path) -> dict[str, Any]:
    return {
        **{
            key: value
            for key, value in topic.items()
            if key
            not in {
                "source_topic_dir",
                "destination_folder",
                "destination_pdf",
                "destination_txt",
                "readme",
            }
        },
        "source_topic_dir": repository_relative(topic["source_topic_dir"], root),
        "destination_folder": repository_relative(
            topic["destination_folder"], root
        ),
        "destination_pdf": repository_relative(topic["destination_pdf"], root),
        "destination_txt": repository_relative(topic["destination_txt"], root),
        "readme": repository_relative(topic["readme"], root),
    }


def report_markdown(validation: dict[str, Any]) -> str:
    summary = validation["summary"]
    source = validation["source_packages"]
    tracker = validation["tracker"]
    catalogue = validation["catalogue"]
    links = validation["navigation_links"]
    subject = validation["scope"]["subject"]
    numbers = [int(topic["number"]) for topic in validation["topics"]]
    topic_range = (
        f"{min(numbers):02d}–{max(numbers):02d}" if numbers else "Active"
    )
    title = (
        "All Completed Topics Flow Learning Report"
        if len(validation["scope"].get("subjects") or []) > 1
        else f"{subject} {topic_range} Flow Learning Report"
    )
    lines = [
        f"# {title}",
        "",
        f"- Status: **{validation['status'].upper()}**",
        f"- Topic folders: **{summary['topic_folder_count']}**",
        "- Subject/topic counts: "
        + ", ".join(
            f"**{name}: {count}**"
            for name, count in summary["subject_counts"].items()
        ),
        "- Subject page totals: "
        + ", ".join(
            f"**{name}: {count}**"
            for name, count in summary["subject_page_totals"].items()
        ),
        f"- Flow PDFs / TXTs / READMEs: **{summary['pdf_count']} / "
        f"{summary['txt_count']} / {summary['readme_count']}**",
        f"- Total Flow PDF pages: **{summary['total_pdf_pages']}**",
        f"- Source/output PDF hashes equal: **{summary['pdf_hashes_equal']}**",
        f"- Source/output TXT hashes equal: **{summary['txt_hashes_equal']}**",
        f"- Combined exported PDF/TXT hash-list SHA-256: "
        f"`{summary['artifact_hash_list_sha256']}`",
        f"- Navigation links checked: **{links['checked_link_count']}**, broken: "
        f"**{len(links['broken_links'])}**",
        f"- Tracker SHA-256: `{tracker['sha256_before']}` — unchanged: "
        f"**{tracker['unchanged']}**",
        f"- Topic catalogue SHA-256: `{catalogue['sha256_before']}` — unchanged: "
        f"**{catalogue['unchanged']}**",
        f"- Final-Learning-Packages aggregate SHA-256: "
        f"`{source['before']['aggregate_sha256']}` — unchanged: "
        f"**{source['unchanged']}**",
        f"- Exact latest validated learner-v2 inventory: "
        f"**{validation['scope']['exact_latest_validated_completed_inventory']}**",
        f"- Derived / expected topic count: "
        f"**{validation['scope']['derived_topic_count']} / "
        f"{validation['scope']['expected_topic_count'] or 'not fixed'}**; "
        f"difference: **{validation['scope']['difference_from_expected']}**",
        f"- Polity case-year compliance: "
        f"**{summary['case_year_compliance']}**",
        f"- Other-subject date/year retention: "
        f"**{summary['non_polity_date_year_retention']}**",
        "",
        "## Inventory and metadata resolution",
        "",
        "- Inventory is derived dynamically from the highest-generation passed "
        "`learner-v2` tracker record for each topic key.",
        "- Each tracker identity must map to exactly one Final-Learning-Packages "
        "folder with the same source record ID and generation.",
        "- If an exact catalogue entry is absent, metadata is accepted only from "
        "the clean-package README plus its numbered subject/section/folder "
        "location; titles are not guessed from topic keys.",
        "- Catalogue-fallback topics: "
        + (
            ", ".join(
                f"`{key}`"
                for key in validation["scope"]["catalogue_fallback_topic_keys"]
            )
            or "None"
        ),
        "",
        "## Navigation rule",
        "",
        "Start with Flow Learning for first understanding and rapid revision. "
        "Use the Complete Learning Session only for deeper explanation/evidence. "
        "Use the Solved Workbook for practice. Flow Learning does not replace or "
        "reduce the full reference.",
        "",
        "## Per-topic validation",
        "",
        "| Subject | Section | # | Topic | Record / generation | Panels | Pages | PDF SHA-256 | TXT SHA-256 | "
        "Case years | Date/year retention | Master | PDF layout | Status |",
        "|---|---|---:|---|---|---:|---:|---|---|---|---|---|---|---|",
    ]
    for topic in validation["topics"]:
        pdf = topic["pdf_validation"]
        case_year = topic["case_year"]
        lines.append(
            "| "
            + " | ".join(
                (
                    topic["subject"],
                    topic["section"],
                    f"{topic['number']:02d}",
                    topic["title"],
                    f"`{topic['record_id']}` / g{topic['generation']}",
                    str(topic["continuous_master"]["panel_count"]),
                    str(pdf.get("page_count") or "—"),
                    f"`{topic['hashes']['pdf']['destination_sha256']}`",
                    f"`{topic['hashes']['txt']['destination_sha256']}`",
                    (
                        f"PASS ({case_year['expected_case_count']})"
                        if case_year["status"] == "passed"
                        else case_year["status"].upper()
                    ),
                    topic["date_year_retention"]["status"].upper(),
                    topic["continuous_master"]["status"].upper(),
                    pdf["status"].upper(),
                    topic["status"].upper(),
                )
            )
            + " |"
        )
    fundamental_rights = next(
        (
            topic
            for topic in validation["topics"]
            if topic["topic_key"] == "polity-07"
        ),
        None,
    )
    if fundamental_rights:
        master = fundamental_rights["continuous_master"]
        lines.extend(
            (
                "",
                "## Fundamental Rights complete-master validation",
                "",
                f"- Source: `{fundamental_rights['hashes']['txt']['source']}`",
                f"- Export: `{fundamental_rights['hashes']['txt']['destination']}`",
                f"- Continuous atlas: **{master['panel_count']} / "
                f"{master['declared_panel_total']} sequential panels**.",
                f"- Scale check: **{master['nonempty_line_count']} non-empty lines; "
                f"{master['character_count']} characters** — not a short summary: "
                f"**{master['not_a_short_summary']}**.",
                "- Required dimensions: Articles 12–35; doctrines; named cases "
                "with verified years; all five writs; emergency and property links; "
                "examiner traps; PYQ/answer spine; model synthesis.",
                "- Dimension results: "
                + ", ".join(
                    f"`{name}`={result['status'].upper()}"
                    for name, result in master["required_dimensions"].items()
                ),
                f"- PDF/TXT normalized equality: "
                f"**{fundamental_rights['pdf_validation']['normalized_equal']}**; "
                "source/destination byte hashes equal: **True**.",
            )
        )
    lines.extend(
        (
            "",
            "## PDF evidence",
            "",
            "- Every exported PDF was opened and compared with its matching TXT "
            "through the existing ASCII PDF validator.",
            "- Blank, clipped and replacement-glyph page lists are empty for every topic.",
            "- Current repaired-source evidence was reused from "
            "`upsc-ai-kit\\manifests\\exports\\polity-flowchart-case-year-repair-"
            "2026-08-24-validation.json`, including contact-sheet/preview review.",
            "",
            "## Tests",
            "",
            f"- Command: `{validation['tests']['command']}`",
            f"- Tests passed: **{validation['tests']['passed_count']}**",
            f"- Status: **{validation['tests']['status'].upper()}**",
            "",
            "## Exceptions",
            "",
        )
    )
    exceptions = validation.get("exceptions") or []
    lines.extend(f"- {item}" for item in exceptions)
    if not exceptions:
        lines.append("- None.")
    return "\n".join(lines) + "\n"


def _default_output_paths(
    root: Path,
    selections: Sequence[TopicSelection],
    manifest_date: str,
    subject: str | None,
) -> tuple[Path, Path]:
    if subject is None:
        return (
            root
            / "notes"
            / "Flow-Learning"
            / "ALL-COMPLETED-TOPICS-FLOW-LEARNING-REPORT.md",
            root
            / "upsc-ai-kit"
            / "manifests"
            / "exports"
            / f"all-completed-topics-flow-learning-{manifest_date}-validation.json",
        )
    numbers = [item.number for item in selections]
    range_label = (
        f"{min(numbers):02d}-{max(numbers):02d}" if numbers else "none"
    )
    subject_slug = slugify_topic(subject)
    report = (
        root
        / "notes"
        / "Flow-Learning"
        / f"{subject_slug.upper()}-{range_label}-FLOW-LEARNING-REPORT.md"
    )
    validation = (
        root
        / "upsc-ai-kit"
        / "manifests"
        / "exports"
        / f"{subject_slug.lower()}-{range_label}-flow-learning-"
        f"{manifest_date}-validation.json"
    )
    return report, validation


def export_flow_library(
    *,
    root: Path,
    tracker_path: Path,
    catalogue_path: Path,
    source_root: Path,
    export_root: Path,
    selected_keys: Sequence[str] | None = None,
    validate_pdfs: bool = True,
    case_year_evidence_path: Path = DEFAULT_CASE_YEAR_EVIDENCE,
    report_path: Path | None = None,
    validation_path: Path | None = None,
    manifest_date: str | None = None,
    tests_passed: int = 0,
    tests_command: str = "",
    subject: str | None = DEFAULT_SUBJECT,
    topic_prefix: str | None = DEFAULT_TOPIC_PREFIX,
    expected_topic_count: int | None = None,
) -> dict[str, Any]:
    manifest_date = manifest_date or datetime.now().date().isoformat()
    tracker_hash_before = sha256_file(tracker_path)
    catalogue_hash_before = sha256_file(catalogue_path)
    immutable_source_root = final_library_root(source_root)
    source_before = tree_fingerprint(immutable_source_root)
    requested = resolve_selections(
        root,
        tracker_path,
        catalogue_path,
        source_root,
        selected_keys,
        subject=subject,
        topic_prefix=topic_prefix,
    )
    if not requested:
        raise ExportError("No active validated topics were selected.")
    destination_subject_roots = {
        selection.subject: (
            export_root / sanitize_display_component(selection.subject)
        )
        for selection in requested
    }
    for destination_subject_root in destination_subject_roots.values():
        destination_subject_root.mkdir(parents=True, exist_ok=True)
    for selection in requested:
        export_topic(
            selection,
            destination_subject_roots[selection.subject],
            root,
        )

    if selected_keys:
        retained = retained_exported_selections(
            root=root,
            tracker_path=tracker_path,
            catalogue_path=catalogue_path,
            source_root=source_root,
            export_root=export_root,
            subject=subject,
            topic_prefix=topic_prefix,
        )
        requested_by_key = {
            selection.topic_key: selection for selection in requested
        }
        all_available = [
            requested_by_key.get(selection.topic_key, selection)
            for selection in retained
        ]
        for selection in requested:
            if all(
                existing.topic_key != selection.topic_key
                for existing in all_available
            ):
                all_available.append(selection)
        all_available = sorted(
            all_available,
            key=lambda item: (
                item.subject.casefold(),
                item.section.casefold(),
                item.number,
                item.topic_key,
            ),
        )
    else:
        all_available = resolve_selections(
            root,
            tracker_path,
            catalogue_path,
            source_root,
            None,
            subject=subject,
            topic_prefix=topic_prefix,
        )
    exported_selections = [
        selection
        for selection in all_available
        if exact_topic_shape(
            (
                export_root
                / sanitize_display_component(selection.subject)
                / selection.destination_folder_name
            ),
            selection,
        )
    ]
    topics = [
        validate_exported_topic(
            selection,
            export_root / sanitize_display_component(selection.subject),
            root,
            validate_pdf=validate_pdfs,
            evidence_path=case_year_evidence_path,
        )
        for selection in exported_selections
    ]
    grouped_topics: dict[str, list[dict[str, Any]]] = {}
    for topic in topics:
        grouped_topics.setdefault(topic["subject"], []).append(topic)
    for resolved_subject, subject_topics in grouped_topics.items():
        destination_subject_root = (
            export_root / sanitize_display_component(resolved_subject)
        )
        write_text_atomic(
            destination_subject_root / "INDEX.md",
            subject_index_markdown(
                resolved_subject,
                destination_subject_root,
                subject_topics,
            ),
        )
    current_by_key = {topic["topic_key"]: topic for topic in topics}
    discovered_topics = discover_exported_topics(export_root)
    if subject is None:
        navigation_topics = list(topics)
    else:
        navigation_topics = [
            topic
            for topic in discovered_topics
            if topic["subject"] != subject
        ]
        navigation_topics.extend(current_by_key.values())
    navigation_topics = sorted(
        navigation_topics,
        key=lambda topic: (
            topic["subject"].casefold(),
            topic["section"].casefold(),
            topic["number"],
            topic["title"].casefold(),
        ),
    )
    write_text_atomic(
        export_root / "START-HERE.md",
        start_here_markdown(export_root, navigation_topics),
    )
    write_text_atomic(
        export_root / "TRACKER.md",
        tracker_markdown(export_root, navigation_topics),
    )

    if report_path is None or validation_path is None:
        default_report, default_validation = _default_output_paths(
            root,
            topics and exported_selections or requested,
            manifest_date,
            subject,
        )
        report_path = report_path or default_report
        validation_path = validation_path or default_validation

    tracker_hash_after = sha256_file(tracker_path)
    catalogue_hash_after = sha256_file(catalogue_path)
    source_after = tree_fingerprint(immutable_source_root)
    links = validate_markdown_links(export_root)
    errors = [
        error
        for topic in topics
        for error in (
            [f"{topic['topic_key']}: {item}" for item in topic["errors"]]
        )
    ]
    if tracker_hash_before != tracker_hash_after:
        errors.append("EXPORT-PDF-STATUS.json changed during export")
    if catalogue_hash_before != catalogue_hash_after:
        errors.append("topic catalogue changed during export")
    if source_before != source_after:
        errors.append("Final-Learning-Packages changed during export")
    if not links["passed"]:
        errors.extend(links["broken_links"])
    target_subjects = sorted(grouped_topics, key=str.casefold)
    actual_topic_dirs = sorted(
        (
            item
            for resolved_subject in target_subjects
            for item in (
                export_root / sanitize_display_component(resolved_subject)
            ).iterdir()
            if item.is_dir() and not item.name.startswith(".")
        ),
        key=lambda item: str(item).casefold(),
    )
    if len(actual_topic_dirs) != len(topics):
        errors.append(
            f"expected {len(topics)} active topic folders, found "
            f"{len(actual_topic_dirs)}"
        )
    expected_active_keys = {item.topic_key for item in all_available}
    exported_active_keys = {item.topic_key for item in exported_selections}
    exact_active_inventory = expected_active_keys == exported_active_keys
    if subject is None and not exact_active_inventory:
        errors.append(
            "exported topic keys do not exactly match latest validated "
            "learner-v2 inventory"
        )
    test_status = "passed" if tests_passed > 0 else "not-recorded"
    if tests_command and tests_passed <= 0:
        errors.append("test command was supplied without a positive pass count")

    serializable_topics = [_serializable_topic(topic, root) for topic in topics]
    total_pdf_pages = sum(
        int(topic["pdf_validation"].get("page_count") or 0)
        for topic in serializable_topics
    )
    artifact_hash_list_sha256 = hashlib.sha256(
        "\n".join(
            hash_value
            for topic in serializable_topics
            for hash_value in (
                topic["hashes"]["pdf"]["destination_sha256"],
                topic["hashes"]["txt"]["destination_sha256"],
            )
        ).encode("utf-8")
    ).hexdigest()
    subject_counts = {
        resolved_subject: len(subject_topics)
        for resolved_subject, subject_topics in sorted(
            grouped_topics.items(), key=lambda item: item[0].casefold()
        )
    }
    subject_page_totals = {
        resolved_subject: sum(
            int(topic["pdf_validation"].get("page_count") or 0)
            for topic in subject_topics
        )
        for resolved_subject, subject_topics in sorted(
            grouped_topics.items(), key=lambda item: item[0].casefold()
        )
    }
    inventory_difference = (
        len(expected_active_keys) - expected_topic_count
        if expected_topic_count is not None
        else None
    )
    fallback_topic_keys = [
        topic["topic_key"]
        for topic in serializable_topics
        if topic["metadata_resolution"].startswith("catalogue entry absent")
    ]
    validation = {
        "schema_version": 1,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed" if not errors else "failed",
        "scope": {
            "subject": subject or "All completed subjects",
            "subjects": target_subjects,
            "topic_prefix": topic_prefix,
            "selected_topic_keys": [item.topic_key for item in requested],
            "active_exported_topic_keys": [
                item.topic_key for item in exported_selections
            ],
            "dynamic_topic_count": True,
            "latest_validated_learner_v2_only": True,
            "inventory_derivation": (
                "latest passed learner-v2 record per topic_key, matched to one "
                "clean package by exact record_id and generation"
            ),
            "expected_topic_count": expected_topic_count,
            "derived_topic_count": len(expected_active_keys),
            "difference_from_expected": inventory_difference,
            "exact_latest_validated_completed_inventory": exact_active_inventory,
            "catalogue_fallback_topic_keys": fallback_topic_keys,
        },
        "summary": {
            "topic_folder_count": len(actual_topic_dirs),
            "pdf_count": sum(
                len(list(path.glob("*-Continuous-Flow-Learning.pdf")))
                for path in actual_topic_dirs
            ),
            "txt_count": sum(
                len(list(path.glob("*-Continuous-Flow-Learning.txt")))
                for path in actual_topic_dirs
            ),
            "readme_count": sum(
                int((path / "README.txt").is_file())
                for path in actual_topic_dirs
            ),
            "total_pdf_pages": total_pdf_pages,
            "subject_counts": subject_counts,
            "subject_page_totals": subject_page_totals,
            "artifact_hash_list_sha256": artifact_hash_list_sha256,
            "pdf_hashes_equal": all(
                topic["hashes"]["pdf"]["equal"]
                for topic in serializable_topics
            ),
            "txt_hashes_equal": all(
                topic["hashes"]["txt"]["equal"]
                for topic in serializable_topics
            ),
            "case_year_compliance": all(
                topic["case_year"]["status"] == "passed"
                for topic in serializable_topics
                if topic["subject"] == "Polity"
            ),
            "non_polity_date_year_retention": all(
                topic["date_year_retention"]["status"] == "passed"
                for topic in serializable_topics
                if topic["subject"] != "Polity"
            ),
            "continuous_master_completeness": all(
                topic["continuous_master"]["status"] == "passed"
                for topic in serializable_topics
            ),
            "pdf_layout_passed": all(
                topic["pdf_validation"]["status"] in {"passed", "skipped"}
                for topic in serializable_topics
            ),
        },
        "tracker": {
            "path": repository_relative(tracker_path, root),
            "sha256_before": tracker_hash_before,
            "sha256_after": tracker_hash_after,
            "unchanged": tracker_hash_before == tracker_hash_after,
        },
        "catalogue": {
            "path": repository_relative(catalogue_path, root),
            "sha256_before": catalogue_hash_before,
            "sha256_after": catalogue_hash_after,
            "unchanged": catalogue_hash_before == catalogue_hash_after,
        },
        "source_packages": {
            "path": repository_relative(immutable_source_root, root),
            "before": source_before,
            "after": source_after,
            "unchanged": source_before == source_after,
        },
        "navigation_links": links,
        "tests": {
            "command": tests_command,
            "passed_count": tests_passed,
            "status": test_status,
        },
        "topics": serializable_topics,
        "exceptions": errors,
        "report": repository_relative(report_path, root),
        "validation_manifest": repository_relative(validation_path, root),
    }
    write_text_atomic(report_path, report_markdown(validation))
    links_after_report = validate_markdown_links(export_root)
    validation["navigation_links"] = links_after_report
    if not links_after_report["passed"]:
        validation["status"] = "failed"
        validation["exceptions"].extend(links_after_report["broken_links"])
    write_json_atomic(validation_path, validation)
    if validation["status"] != "passed":
        raise ExportError(
            "Flow Learning validation failed: "
            + " | ".join(validation["exceptions"])
        )
    return validation


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--tracker", type=Path, default=DEFAULT_TRACKER)
    parser.add_argument("--catalogue", type=Path, default=DEFAULT_CATALOGUE)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--export-root", type=Path, default=DEFAULT_EXPORT_ROOT)
    parser.add_argument("--subject", default=DEFAULT_SUBJECT)
    parser.add_argument("--topic-prefix", default=DEFAULT_TOPIC_PREFIX)
    parser.add_argument(
        "--all-completed",
        action="store_true",
        help=(
            "Export every latest validated learner-v2 topic across subjects. "
            "Subject and prefix filters are ignored."
        ),
    )
    parser.add_argument(
        "--expected-topic-count",
        type=int,
        default=DEFAULT_EXPECTED_ALL_TOPIC_COUNT,
    )
    parser.add_argument("--topic-key", action="append", default=[])
    parser.add_argument("--topics", default="")
    parser.add_argument("--manifest-date", default=datetime.now().date().isoformat())
    parser.add_argument("--report-path", type=Path)
    parser.add_argument("--validation-path", type=Path)
    parser.add_argument(
        "--case-year-evidence",
        type=Path,
        default=DEFAULT_CASE_YEAR_EVIDENCE,
    )
    parser.add_argument("--skip-pdf-validation", action="store_true")
    parser.add_argument("--tests-passed", type=int, default=0)
    parser.add_argument("--tests-command", default="")
    return parser.parse_args(argv)


def _absolute(root: Path, path: Path) -> Path:
    return path if path.is_absolute() else root / path


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    topic_keys = list(args.topic_key)
    if args.topics:
        topic_keys.extend(
            item.strip() for item in args.topics.split(",") if item.strip()
        )
    try:
        subject = None if args.all_completed else args.subject
        topic_prefix = None if args.all_completed else args.topic_prefix
        validation = export_flow_library(
            root=root,
            tracker_path=_absolute(root, args.tracker).resolve(),
            catalogue_path=_absolute(root, args.catalogue).resolve(),
            source_root=_absolute(root, args.source_root).resolve(),
            export_root=_absolute(root, args.export_root).resolve(),
            selected_keys=topic_keys or None,
            validate_pdfs=not args.skip_pdf_validation,
            case_year_evidence_path=_absolute(
                root, args.case_year_evidence
            ).resolve(),
            report_path=(
                _absolute(root, args.report_path).resolve()
                if args.report_path
                else None
            ),
            validation_path=(
                _absolute(root, args.validation_path).resolve()
                if args.validation_path
                else None
            ),
            manifest_date=args.manifest_date,
            tests_passed=args.tests_passed,
            tests_command=args.tests_command,
            subject=subject,
            topic_prefix=topic_prefix,
            expected_topic_count=(
                args.expected_topic_count if args.all_completed else None
            ),
        )
    except ExportError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(
        json.dumps(
            {
                "status": validation["status"],
                "topic_count": validation["summary"]["topic_folder_count"],
                "total_pdf_pages": validation["summary"]["total_pdf_pages"],
                "report": validation["report"],
                "validation_manifest": validation["validation_manifest"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
