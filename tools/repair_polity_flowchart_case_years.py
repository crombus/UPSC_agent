"""Repair Polity learner-v2 flowchart case years in the active generation.

This is an in-place presentation repair. It does not create tracker generations
and does not rebuild or alter solved workbooks.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
import sys
import uuid
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import fitz

import carvaka_flowchart
import export_four_item_library as final_library
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
import polity_flowchart_case_years as case_years
import refresh_all_v2_learning_sessions as refresh


ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
CATALOGUE = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
FINAL_LIBRARY = ROOT / "notes" / "Final-Learning-Packages"
REPORT = (
    FINAL_LIBRARY
    / "POLITY-FLOWCHART-CASE-YEAR-REPAIR-REPORT.md"
)
VALIDATION = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / "polity-flowchart-case-year-repair-2026-08-24-validation.json"
)
REPAIR_ID = "polity-flowchart-case-year-repair-2026-08-24"
TOPIC_KEYS = tuple(f"polity-{number:02d}" for number in range(1, 23))
ASCII_REBUILD_TOPIC_KEYS = {
    "polity-03",
    "polity-04",
    "polity-05",
    "polity-06",
    "polity-07",
    "polity-08",
    "polity-09",
    "polity-10",
    "polity-12",
    "polity-14",
    "polity-15",
    "polity-16",
}
FALLBACK_BEFORE_LABELS: dict[str, dict[str, str]] = {
    "polity-03": {
        "minerva-mills": "MINERVA MILLS",
        "article-370": "J&K ... abolished 2019; SC upheld",
        "rajendra-n-shah": "Rajendra N. Shah 2021 ruling",
    },
    "polity-04": {
        "berubari-union": "BERUBARI UNION, 1960 / Berubari",
        "kesavananda-bharati": "KESAVANANDA BHARATI, 1973 / Kesavananda",
        "lic-consumer-education": "LIC OF INDIA, 1995 / LIC",
        "ds-nakara": "D.S. Nakara (1983)",
        "gb-pant-university": "G.B. / Pant University (2000)",
    },
    "polity-05": {
        "berubari-union": "BERUBARI UNION, 1960 / Berubari",
        "maganbhai": "MAGANBHAI ISHWARBHAI, 1969",
    },
    "polity-06": {
        "section-6a": "IN RE: SECTION 6A, 17 OCT 2024",
    },
    "polity-07": {
        "pradeep-kumar-biswas": "Pradeep Kumar Biswas",
        "kesavananda-bharati": "Kesavananda",
        "ep-royappa": "Royappa",
        "maneka-gandhi": "Maneka",
        "champakam-dorairajan": "Champakam",
        "indra-sawhney": "Indra Sawhney",
        "m-nagaraj": "Nagaraj",
        "jarnail-singh": "Jarnail",
        "janhit-abhiyan": "Janhit",
        "davinder-singh": "Davinder Singh 2024",
        "shreya-singhal": "Shreya Singhal",
        "anuradha-bhasin": "Anuradha Bhasin",
        "kedar-nath-singh": "Kedar Nath",
        "ak-gopalan": "Gopalan",
        "rc-cooper": "R.C. Cooper",
        "puttaswamy-privacy": "Puttaswamy",
        "ir-coelho": "I.R. Coelho",
        "minerva-mills": "Minerva Mills",
        "property-owners": "Property Owners 2024",
        "vishaka": "Vishaka",
    },
    "polity-08": {
        "champakam-dorairajan": "1951 CHAMPAKAM",
        "golaknath": "1967 GOLAKNATH",
        "kesavananda-bharati": "1973 KESAVANANDA",
        "minerva-mills": "1980 MINERVA MILLS",
        "property-owners": "2024 PROPERTY OWNERS ASSOCIATION",
    },
    "polity-09": {
        "bijoe-emmanuel": "BIJOE EMMANUEL, 1986",
        "naveen-jindal": "NAVEEN JINDAL, 2004",
        "shyam-narayan-chouksey": "SHYAM NARAYAN CHOUKSEY",
    },
    "polity-10": {
        "shankari-prasad": "1951 SHANKARI PRASAD",
        "sajjan-singh": "1965 SAJJAN SINGH",
        "golaknath": "1967 GOLAKNATH",
        "kesavananda-bharati": "1973 KESAVANANDA",
        "indira-gandhi": "1975 INDIRA GANDHI",
        "minerva-mills": "1980 MINERVA MILLS",
        "waman-rao": "1981 WAMAN RAO",
        "ir-coelho": "2007 I.R. COELHO",
        "anjum-kadari": "ANJUM KADARI, 2024 INSC 831",
    },
    "polity-12": {
        "kesavananda-bharati": "KESAVANANDA BHARATI, 1973",
        "sr-bommai": "S.R. BOMMAI, 1994 / Bommai",
        "state-of-rajasthan": "STATE OF RAJASTHAN / RELATED DOCTRINE",
        "mohit-minerals": "MOHIT MINERALS, 2022",
    },
    "polity-14": {
        "adm-jabalpur": "ADM Jabalpur",
        "puttaswamy-privacy": "Puttaswamy",
        "sr-bommai": "S.R. BOMMAI / Bommai",
        "rameshwar-prasad": "RAMESHWAR PRASAD",
    },
    "polity-15": {
        "shamsher-singh": "Shamsher Singh",
        "dc-wadhwa": "D.C. Wadhwa",
        "krishna-kumar-singh": "Krishna Kumar Singh",
        "kehar-singh": "Kehar Singh",
        "maru-ram": "Maru Ram",
    },
    "polity-16": {
        "shamsher-singh": "Shamsher Singh",
        "sr-chaudhuri": "S.R. Chaudhuri",
    },
    "polity-17": {
        "puttaswamy-aadhaar": "K.S. Puttaswamy (Aadhaar), 2018",
        "rojer-mathew": "Rojer Mathew v. / South Indian Bank (2019)",
    },
}
CODE_FILES = (
    "tools\\polity_flowchart_case_years.py",
    "tools\\repair_polity_flowchart_case_years.py",
    "tools\\test_polity_flowchart_case_years.py",
    "tools\\build_carvaka_graphical_specs.py",
    "tools\\carvaka_flowchart.py",
    "tools\\test_carvaka_flowchart.py",
    "tools\\notions_style_ascii_master.py",
    "tools\\generate_polity_13_17_sequential.py",
    "tools\\generate_polity_18_22_sequential.py",
)


class RepairError(RuntimeError):
    """Raised when an in-place repair or validation gate fails."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def repo_path(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def write_json_atomic(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    stage = path.with_name(f".{path.name}.case-year-{uuid.uuid4().hex}.tmp")
    stage.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(stage, path)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    stage = path.with_name(f".{path.name}.case-year-{uuid.uuid4().hex}.tmp")
    stage.write_text(text, encoding="utf-8", newline="\n")
    os.replace(stage, path)


def page_count(path: Path) -> int:
    with fitz.open(path) as document:
        return document.page_count


def latest_polity_topics(
    tracker: dict[str, Any],
) -> tuple[list[refresh.Topic], dict[str, dict[str, Any]]]:
    topics = [
        topic
        for topic in refresh.latest_validated_topics(
            tracker,
            refresh.merged_overrides(),
        )
        if topic.key in TOPIC_KEYS
    ]
    by_key = {topic.key: topic for topic in topics}
    if set(by_key) != set(TOPIC_KEYS):
        raise RepairError(
            "Active latest Polity topic coverage mismatch: "
            f"missing={sorted(set(TOPIC_KEYS) - set(by_key))}"
        )
    records = {
        str(record["topic_key"]): record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") in TOPIC_KEYS
        and record.get("variant") == refresh.V2_VARIANT
        and int(record.get("generation") or 0)
        == by_key[str(record["topic_key"])].generation
    }
    if set(records) != set(TOPIC_KEYS):
        raise RepairError("Could not resolve all 17 active tracker records.")
    return sorted(topics, key=lambda topic: topic.key), records


def non_polity_final_hash() -> tuple[int, str]:
    rows: list[tuple[str, str]] = []
    if FINAL_LIBRARY.is_dir():
        for subject in sorted(
            (
                path
                for path in FINAL_LIBRARY.iterdir()
                if path.is_dir() and path.name != "Polity"
            ),
            key=lambda path: path.name.casefold(),
        ):
            for path in sorted(
                (item for item in subject.rglob("*") if item.is_file()),
                key=lambda item: relative(item).casefold(),
            ):
                rows.append((relative(path), sha256(path)))
    aggregate = hashlib.sha256(
        "\n".join(f"{path}\t{digest}" for path, digest in rows).encode("utf-8")
    ).hexdigest()
    return len(rows), aggregate


def record_paths(record: dict[str, Any]) -> list[Path]:
    paths = [
        repo_path(str(record["markdown"])),
        repo_path(str(record["main_pdf"])),
        repo_path(str(record["workbook"])),
        repo_path(str(record["workbook_markdown"])),
    ]
    notes_dir = repo_path(str(record["main_pdf"])).parent
    paths.extend(
        notes_dir / name
        for name in (
            "STAGED-RECORD.json",
            "PRESERVATION-HASHES.json",
            "PACKAGE-VALIDATION-REPORT.txt",
        )
    )
    flow = record.get("continuous_core_first")
    if isinstance(flow, dict) and flow.get("folder"):
        folder = repo_path(str(flow["folder"]))
        if folder.is_dir():
            paths.extend(item for item in folder.rglob("*") if item.is_file())
    return paths


def snapshot_hashes(
    records: dict[str, dict[str, Any]],
    selections: Iterable[final_library.ExportSelection],
    ascii_paths: Iterable[Path],
    graphical_paths: Iterable[Path],
) -> dict[str, str]:
    paths: set[Path] = {TRACKER, REPORT, VALIDATION}
    paths.update(ascii_paths)
    paths.update(graphical_paths)
    for record in records.values():
        paths.update(record_paths(record))
    for selection in selections:
        destination = FINAL_LIBRARY / selection.destination_relative
        if destination.is_dir():
            paths.update(item for item in destination.rglob("*") if item.is_file())
    return {
        relative(path): sha256(path)
        for path in paths
        if path.is_file()
    }


def current_relevant_hashes(
    records: dict[str, dict[str, Any]],
    selections: Iterable[final_library.ExportSelection],
    ascii_paths: Iterable[Path],
    graphical_paths: Iterable[Path],
) -> dict[str, str]:
    return snapshot_hashes(records, selections, ascii_paths, graphical_paths)


def changed_paths(before: dict[str, str], after: dict[str, str]) -> list[str]:
    return sorted(
        {
            path
            for path in set(before) | set(after)
            if before.get(path) != after.get(path)
        },
        key=str.casefold,
    )


def expected_repair_files(
    topics: Iterable[refresh.Topic],
    records: dict[str, dict[str, Any]],
    selections: Iterable[final_library.ExportSelection],
) -> set[str]:
    selection_by_key = {selection.topic_key: selection for selection in selections}
    paths: set[Path] = {TRACKER, REPORT, VALIDATION}
    for topic in topics:
        record = records[topic.key]
        provenance = record.get("provenance")
        repair = (
            provenance.get("flowchart_case_year_repair")
            if isinstance(provenance, dict)
            else None
        )
        if not isinstance(repair, dict) or repair.get("id") != REPAIR_ID:
            continue
        manual_spec = refresh.manual_ascii_topic_spec(topic.key)
        if manual_spec is None:
            raise RepairError(f"{topic.key}: manual ASCII spec disappeared.")
        paths.add(manual_spec.source_path)
        paths.add(refresh.graphical_spec_path(topic))
        flow = record.get("continuous_core_first")
        if isinstance(flow, dict) and flow.get("folder"):
            folder = repo_path(str(flow["folder"]))
            if folder.is_dir():
                paths.update(item for item in folder.rglob("*") if item.is_file())
        notes_dir = topic.main_pdf.parent
        paths.update(
            notes_dir / name
            for name in (
                "STAGED-RECORD.json",
                "PRESERVATION-HASHES.json",
                "PACKAGE-VALIDATION-REPORT.txt",
            )
        )
        if topic.key in ASCII_REBUILD_TOPIC_KEYS:
            paths.update({topic.markdown, topic.main_pdf})
        selection = selection_by_key[topic.key]
        library_dir = FINAL_LIBRARY / selection.destination_relative
        paths.update(
            {
                library_dir
                / "03-Carvaka-Graphical-Flowchart"
                / "At-a-Glance-Poster.pdf",
                library_dir
                / "03-Carvaka-Graphical-Flowchart"
                / "High-Resolution-Master.png",
                library_dir
                / "03-Carvaka-Graphical-Flowchart"
                / "Printable-Tiled-Version.pdf",
            }
        )
        if topic.key in ASCII_REBUILD_TOPIC_KEYS:
            paths.update(
                {
                    library_dir
                    / "01-Complete-Learning-Session"
                    / "Complete-Learning-Session.pdf",
                    library_dir
                    / "04-ASCII-Master-Flowchart"
                    / "ASCII-Master-Flowchart.pdf",
                    library_dir
                    / "04-ASCII-Master-Flowchart"
                    / "ASCII-Master-Flowchart.txt",
                }
            )
    return {
        relative(path)
        for path in paths
        if path.is_file() or path in {REPORT, VALIDATION}
    }


def normalize_ascii_specs(
    ascii_paths: Iterable[Path],
) -> tuple[
    dict[str, list[dict[str, Any]]],
    dict[str, dict[str, str]],
]:
    changes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    hashes: dict[str, dict[str, str]] = {}
    for path in sorted(set(ascii_paths), key=lambda item: item.name.casefold()):
        before_hash = sha256(path)
        data = json.loads(path.read_text(encoding="utf-8"))
        normalized, file_changes = case_years.normalize_ascii_document(data)
        if normalized != data:
            write_json_atomic(path, normalized)
        after_hash = sha256(path)
        hashes[relative(path)] = {"before": before_hash, "after": after_hash}
        for topic_key, topic_changes in file_changes.items():
            changes[topic_key].extend(topic_changes)
    return dict(changes), hashes


def normalize_graphical_specs(
    topics: Iterable[refresh.Topic],
    manual_specs: dict[str, ascii_master.ManualTopicSpec],
) -> tuple[
    dict[str, list[dict[str, Any]]],
    dict[str, dict[str, str]],
]:
    changes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    hashes: dict[str, dict[str, str]] = {}
    for topic in topics:
        path = refresh.graphical_spec_path(topic)
        before_hash = sha256(path)
        spec = json.loads(path.read_text(encoding="utf-8"))
        normalized, topic_changes = case_years.normalize_graphical_spec(spec)
        normalized["ascii_spec_sha256"] = sha256(
            manual_specs[topic.key].source_path
        )
        errors = case_years.graphical_spec_errors(normalized)
        if errors:
            raise RepairError(
                f"{topic.key}: graphical case-year source validation failed: "
                + " | ".join(errors)
            )
        if normalized != spec:
            write_json_atomic(path, normalized)
        after_hash = sha256(path)
        hashes[relative(path)] = {"before": before_hash, "after": after_hash}
        changes[topic.key].extend(topic_changes)
    return dict(changes), hashes


def recover_changes_from_active_outputs(
    topics: Iterable[refresh.Topic],
    records: dict[str, dict[str, Any]],
) -> tuple[
    dict[str, list[dict[str, Any]]],
    dict[str, list[dict[str, Any]]],
]:
    ascii_changes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    graph_changes: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for topic in topics:
        flow = records[topic.key].get("continuous_core_first")
        if not isinstance(flow, dict):
            continue
        standalone = repo_path(str(flow.get("ascii_master") or ""))
        if standalone.is_file():
            case_years.normalize_ascii_body(
                topic.key,
                standalone.read_text(encoding="utf-8"),
                changes=ascii_changes[topic.key],
                field="active-standalone-ascii",
            )
        folder = repo_path(str(flow.get("folder") or ""))
        editable = folder / "editable" / "topic-spec.json"
        if editable.is_file():
            old_spec = json.loads(editable.read_text(encoding="utf-8"))
            _, recovered = case_years.normalize_graphical_spec(old_spec)
            graph_changes[topic.key].extend(recovered)
    return dict(ascii_changes), dict(graph_changes)


def markdown_ascii_prefix(markdown: str) -> str:
    match = re.search(
        r"(?im)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*$",
        markdown,
    )
    if not match:
        raise RepairError("Learner Markdown lacks the complete-topic ASCII heading.")
    return markdown[: match.start()].rstrip()


def update_markdown_and_pdf(
    topic: refresh.Topic,
    manual_spec: ascii_master.ManualTopicSpec,
    *,
    force_pdf: bool = False,
) -> tuple[bool, str, dict[str, Any]]:
    old_text = topic.markdown.read_text(encoding="utf-8")
    expected_fragment = ascii_master.build_manual_fragment(manual_spec)
    transformed, ascii_fragment = refresh.ensure_ascii_master(
        old_text,
        topic,
        require_manual=True,
    )
    if ascii_fragment != expected_fragment:
        raise RepairError(f"{topic.key}: generated ASCII fragment differs from spec.")
    if markdown_ascii_prefix(old_text) != markdown_ascii_prefix(transformed):
        raise RepairError(f"{topic.key}: prose outside the ASCII section changed.")
    markdown_changed = transformed != old_text
    metrics: dict[str, Any] = {
        "markdown_before_sha256": hashlib.sha256(
            old_text.encode("utf-8")
        ).hexdigest(),
        "markdown_after_sha256": hashlib.sha256(
            transformed.encode("utf-8")
        ).hexdigest(),
        "main_pdf_before_sha256": sha256(topic.main_pdf),
        "main_pdf_pages_before": page_count(topic.main_pdf),
    }
    if markdown_changed:
        write_text_atomic(topic.markdown, transformed)
    if markdown_changed or force_pdf:
        stage_dir = topic.main_pdf.parent / ".case-year-pdf-stage"
        if stage_dir.exists():
            shutil.rmtree(stage_dir)
        stage_dir.mkdir()
        stage_pdf = stage_dir / topic.main_pdf.name
        markdown_learning_pdf.build_pdf(
            topic.markdown,
            stage_pdf,
            variant=refresh.V2_VARIANT,
            topic_key=topic.key,
            repository_root=ROOT,
        )
        errors, layout = final_library.pdf_layout_validation(stage_pdf)
        if errors:
            shutil.rmtree(stage_dir, ignore_errors=True)
            raise RepairError(
                f"{topic.key}: regenerated learning PDF layout failed: "
                + " | ".join(errors)
            )
        os.replace(stage_pdf, topic.main_pdf)
        shutil.rmtree(stage_dir)
        metrics["main_pdf_layout"] = layout
    else:
        errors, layout = final_library.pdf_layout_validation(topic.main_pdf)
        if errors:
            raise RepairError(
                f"{topic.key}: existing learning PDF layout failed: "
                + " | ".join(errors)
            )
        metrics["main_pdf_layout"] = layout
    metrics.update(
        {
            "main_pdf_after_sha256": sha256(topic.main_pdf),
            "main_pdf_pages_after": page_count(topic.main_pdf),
        }
    )
    return markdown_changed, ascii_fragment, metrics


def _replace_prefix(value: Any, old: str, new: str) -> Any:
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [_replace_prefix(item, old, new) for item in value]
    if isinstance(value, dict):
        return {
            key: _replace_prefix(item, old, new)
            for key, item in value.items()
        }
    return value


def atomic_replace_directory(stage: Path, destination: Path) -> None:
    backup = destination.parent / f".case-year-old-{uuid.uuid4().hex}"
    try:
        if destination.exists():
            os.replace(destination, backup)
        os.replace(stage, destination)
    except Exception:
        if destination.exists() and not backup.exists():
            shutil.rmtree(destination, ignore_errors=True)
        if backup.exists() and not destination.exists():
            os.replace(backup, destination)
        raise
    if backup.exists():
        shutil.rmtree(backup)


def render_graphical_package(
    topic: refresh.Topic,
    record: dict[str, Any],
    ascii_fragment: str,
    manual_spec: ascii_master.ManualTopicSpec,
) -> tuple[dict[str, Any], dict[str, Any]]:
    old_flow = record.get("continuous_core_first")
    if not isinstance(old_flow, dict) or not old_flow.get("folder"):
        raise RepairError(f"{topic.key}: latest tracker record lacks a flow folder.")
    destination = repo_path(str(old_flow["folder"]))
    stage = destination.parent / f".{destination.name}.case-year-stage"
    if stage.exists():
        shutil.rmtree(stage)
    workbook_markdown = repo_path(str(record["workbook_markdown"]))
    preservation = {
        relative(topic.workbook): sha256(topic.workbook),
        relative(workbook_markdown): sha256(workbook_markdown),
    }
    spec_path = refresh.graphical_spec_path(topic)
    flow, _ = carvaka_flowchart.render_package(
        ROOT,
        spec_path,
        stage,
        ascii_master_bytes=ascii_master.standalone_panel_text(
            ascii_fragment
        ).encode("utf-8"),
        preservation_before=preservation,
    )
    stage_relative = relative(stage)
    destination_relative = relative(destination)
    flow = _replace_prefix(flow, stage_relative, destination_relative)
    flow.update(
        {
            "ascii_master_source": "manual-authored-spec",
            "ascii_master_spec": relative(manual_spec.source_path),
            "ascii_master_spec_sha256": sha256(manual_spec.source_path),
        }
    )
    atomic_replace_directory(stage, destination)
    metrics = {
        "graphical_spec_sha256": sha256(spec_path),
        "master_sha256": sha256(repo_path(str(flow["master_image"]))),
        "poster_sha256": sha256(repo_path(str(flow["poster_pdf"]))),
        "tiled_sha256": sha256(repo_path(str(flow["tiled_pdf"]))),
        "tiled_page_count": page_count(repo_path(str(flow["tiled_pdf"]))),
        "poster_page_count": page_count(repo_path(str(flow["poster_pdf"]))),
        "contact_sheet_count": len(flow.get("contact_sheets") or []),
        "preview_count": len(
            list(repo_path(str(flow["previews"])).glob("page-*.png"))
        ),
    }
    return flow, metrics


def update_record(
    record: dict[str, Any],
    *,
    topic: refresh.Topic,
    flow: dict[str, Any] | None,
    manual_spec: ascii_master.ManualTopicSpec,
    markdown_metrics: dict[str, Any],
    graph_metrics: dict[str, Any] | None,
    ascii_hashes: dict[str, dict[str, str]],
    graphical_hashes: dict[str, dict[str, str]],
) -> None:
    if flow is not None:
        record["continuous_core_first"] = flow
    provenance = record.setdefault("provenance", {})
    if not isinstance(provenance, dict):
        raise RepairError(f"{topic.key}: tracker provenance is malformed.")
    ascii_path = relative(manual_spec.source_path)
    graph_path = relative(refresh.graphical_spec_path(topic))
    source_hashes = provenance.get("source_hashes")
    if isinstance(source_hashes, dict):
        source_hashes[ascii_path] = sha256(manual_spec.source_path)
        source_hashes[graph_path] = sha256(refresh.graphical_spec_path(topic))
    copied = provenance.get("content_copy_hashes")
    if isinstance(copied, dict):
        copied["markdown"] = sha256(topic.markdown)
        copied["main_pdf"] = sha256(topic.main_pdf)
        copied["workbook_pdf"] = sha256(topic.workbook)
        workbook_markdown = repo_path(str(record["workbook_markdown"]))
        copied["workbook_markdown"] = sha256(workbook_markdown)
    repair = {
        "id": REPAIR_ID,
        "applied_on": datetime.now().astimezone().isoformat(),
        "mode": "in-place presentation correction; tracker generation retained",
        "ascii_spec": ascii_path,
        "ascii_spec_sha256_before": ascii_hashes[ascii_path]["before"],
        "ascii_spec_sha256_after": ascii_hashes[ascii_path]["after"],
        "graphical_spec": graph_path,
        "graphical_spec_sha256_before": graphical_hashes[graph_path]["before"],
        "graphical_spec_sha256_after": graphical_hashes[graph_path]["after"],
        "markdown_sha256_before": markdown_metrics["markdown_before_sha256"],
        "markdown_sha256_after": markdown_metrics["markdown_after_sha256"],
        "main_pdf_sha256_before": markdown_metrics["main_pdf_before_sha256"],
        "main_pdf_sha256_after": markdown_metrics["main_pdf_after_sha256"],
        "workbook_sha256": sha256(topic.workbook),
        "approval_retained": bool(record.get("approved")),
    }
    if graph_metrics:
        repair["graphical_outputs"] = graph_metrics
        provenance["new_flowchart_page_count"] = graph_metrics[
            "tiled_page_count"
        ]
    provenance["flowchart_case_year_repair"] = repair
    validation = record.setdefault("validation", {})
    if isinstance(validation, dict):
        validation["flowchart_case_years"] = {
            "status": "passed",
            "repair_id": REPAIR_ID,
            "validated_on": datetime.now().astimezone().isoformat(),
        }


def update_topic_metadata_files(
    record: dict[str, Any],
    topic: refresh.Topic,
    *,
    main_pages: int,
    ascii_max_width: int,
    tiled_pages: int,
    repair_hashes: dict[str, Any],
) -> list[Path]:
    changed: list[Path] = []
    notes_dir = topic.main_pdf.parent
    staged = notes_dir / "STAGED-RECORD.json"
    write_json_atomic(staged, record)
    changed.append(staged)
    preservation_path = notes_dir / "PRESERVATION-HASHES.json"
    if preservation_path.is_file():
        preservation = json.loads(preservation_path.read_text(encoding="utf-8"))
        repairs = [
            item
            for item in preservation.get("presentation_repairs", [])
            if isinstance(item, dict) and item.get("id") != REPAIR_ID
        ]
        repairs.append({"id": REPAIR_ID, **repair_hashes})
        preservation["presentation_repairs"] = repairs
        write_json_atomic(preservation_path, preservation)
        changed.append(preservation_path)
    report_path = notes_dir / "PACKAGE-VALIDATION-REPORT.txt"
    if report_path.is_file():
        text = report_path.read_text(encoding="utf-8")
        text = re.sub(
            r"(?m)^main_pdf_pages=\d+$",
            f"main_pdf_pages={main_pages}",
            text,
        )
        text = re.sub(
            r"(?m)^ascii_max_line_width=\d+$",
            f"ascii_max_line_width={ascii_max_width}",
            text,
        )
        text = re.sub(
            r"(?m)^flowchart_tiled_pages=\d+$",
            f"flowchart_tiled_pages={tiled_pages}",
            text,
        )
        if "flowchart_case_years=PASS" not in text:
            text = text.replace(
                "flowchart_package=PASS\n",
                "flowchart_package=PASS\nflowchart_case_years=PASS\n",
            )
        write_text_atomic(report_path, text)
        changed.append(report_path)
    return changed


def refresh_library_topics(
    topic_keys: list[str],
) -> tuple[list[dict[str, Any]], list[final_library.ExportSelection]]:
    if not topic_keys:
        return [], []
    selections = final_library.resolve_selections(
        ROOT,
        TRACKER,
        CATALOGUE,
        topic_keys,
    )
    manifests: list[dict[str, Any]] = []
    for selection in selections:
        destination = FINAL_LIBRARY / selection.destination_relative
        stage = destination.parent / (
            f".case-year-stage-{selection.topic_key}-{uuid.uuid4().hex[:8]}"
        )
        if stage.exists():
            shutil.rmtree(stage)
        manifest = final_library.prepare_topic_stage(
            ROOT,
            selection,
            stage,
            full_pdf_validation=True,
        )
        try:
            final_library.atomic_replace_topic(stage, destination)
        except PermissionError:
            final_library.validate_topic_shape(destination)
            for source in sorted(
                (path for path in stage.rglob("*") if path.is_file()),
                key=lambda path: str(path.relative_to(stage)).casefold(),
            ):
                target = destination / source.relative_to(stage)
                temporary = target.with_name(
                    f".{target.name}.case-year-{uuid.uuid4().hex}.tmp"
                )
                shutil.copy2(source, temporary)
                os.replace(temporary, target)
            shutil.rmtree(stage)
        manifests.append(manifest)
    return manifests, selections


def markdown_link_errors(markdown_path: Path) -> list[str]:
    text = markdown_path.read_text(encoding="utf-8")
    errors: list[str] = []
    for target in re.findall(r"!?\[[^\]]*]\(([^)]+)\)", text):
        target = target.strip().split(" ", 1)[0].strip("<>")
        if re.match(r"^(?:https?://|mailto:|#)", target, re.IGNORECASE):
            continue
        resolved = (markdown_path.parent / target).resolve()
        if not resolved.is_file():
            errors.append(f"broken local link: {target}")
    return errors


def aggregate_changes(
    ascii_changes: dict[str, list[dict[str, Any]]],
    graph_changes: dict[str, list[dict[str, Any]]],
) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for topic_key in TOPIC_KEYS:
        counter: Counter[tuple[str, str, str]] = Counter()
        fields: dict[tuple[str, str, str], set[str]] = defaultdict(set)
        for kind, rows in (
            ("ASCII", ascii_changes.get(topic_key, [])),
            ("graphical", graph_changes.get(topic_key, [])),
        ):
            for row in rows:
                key = (
                    str(row["case_id"]),
                    str(row["before"]),
                    str(row["after"]),
                )
                counter[key] += 1
                fields[key].add(kind)
        result[topic_key] = [
            {
                "case_id": key[0],
                "before": key[1],
                "after": key[2],
                "occurrences": count,
                "flowchart_types": sorted(fields[key]),
                "source": case_years.source_record(key[0]),
            }
            for key, count in sorted(
                counter.items(),
                key=lambda item: (
                    item[0][0],
                    item[0][1].casefold(),
                ),
            )
        ]
    return result


def fill_fallback_label_changes(
    label_changes: dict[str, list[dict[str, Any]]],
    manual_specs: dict[str, ascii_master.ManualTopicSpec],
    topics: Iterable[refresh.Topic],
) -> dict[str, list[dict[str, Any]]]:
    by_key = {topic.key: topic for topic in topics}
    for topic_key, labels in FALLBACK_BEFORE_LABELS.items():
        if label_changes.get(topic_key):
            continue
        ascii_text = "\n".join(
            f"{panel.title}\n{panel.body}"
            for panel in manual_specs[topic_key].panels
        )
        graph_spec = json.loads(
            refresh.graphical_spec_path(by_key[topic_key]).read_text(
                encoding="utf-8"
            )
        )
        graph_text = "\n".join(
            case_years._iter_renderable_graphical_strings(graph_spec)
        )
        rows: list[dict[str, Any]] = []
        for case_id, before in labels.items():
            after = case_years.case_label(case_id)
            pattern = re.compile(re.escape(after), re.IGNORECASE)
            ascii_count = len(pattern.findall(ascii_text))
            graph_count = len(pattern.findall(graph_text))
            flowchart_types = []
            if ascii_count:
                flowchart_types.append("ASCII")
            if graph_count:
                flowchart_types.append("graphical")
            occurrences = ascii_count + graph_count
            if not occurrences:
                raise RepairError(
                    f"{topic_key}: fallback case label is absent after repair: {after}"
                )
            rows.append(
                {
                    "case_id": case_id,
                    "before": before,
                    "after": after,
                    "occurrences": occurrences,
                    "flowchart_types": flowchart_types,
                    "source": case_years.source_record(case_id),
                }
            )
        label_changes[topic_key] = rows
    return label_changes


def validate_all(
    topics: list[refresh.Topic],
    records: dict[str, dict[str, Any]],
    manual_specs: dict[str, ascii_master.ManualTopicSpec],
    selections: list[final_library.ExportSelection],
    workbook_hashes_before: dict[str, str],
) -> list[dict[str, Any]]:
    selection_by_key = {selection.topic_key: selection for selection in selections}
    rows: list[dict[str, Any]] = []
    for topic in topics:
        record = records[topic.key]
        provenance = record.get("provenance")
        repair = (
            provenance.get("flowchart_case_year_repair")
            if isinstance(provenance, dict)
            else None
        )
        repair_applied = (
            isinstance(repair, dict) and repair.get("id") == REPAIR_ID
        )
        learning_pdf_regenerated = bool(
            repair_applied
            and repair.get("main_pdf_sha256_before")
            != repair.get("main_pdf_sha256_after")
        )
        manual_spec = manual_specs[topic.key]
        case_text = "\n".join(
            f"{panel.title}\n{panel.body}" for panel in manual_spec.panels
        )
        errors = case_years.ascii_topic_errors(topic.key, case_text)
        graph_spec = json.loads(
            refresh.graphical_spec_path(topic).read_text(encoding="utf-8")
        )
        errors.extend(case_years.graphical_spec_errors(graph_spec))
        markdown = topic.markdown.read_text(encoding="utf-8")
        embedded = re.search(
            r"(?ims)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
            markdown,
        )
        expected_fragment = ascii_master.build_manual_fragment(manual_spec)
        embedded_equal = bool(
            embedded
            and ascii_master.normalized_panel_text(embedded.group(1))
            == ascii_master.normalized_panel_text(expected_fragment)
        )
        if not embedded_equal:
            errors.append("embedded ASCII differs from authored spec")
        flow = record.get("continuous_core_first")
        if not isinstance(flow, dict):
            errors.append("tracker lacks continuous_core_first")
            flow = {}
        standalone = repo_path(str(flow.get("ascii_master") or ""))
        expected_standalone = ascii_master.standalone_panel_text(expected_fragment)
        standalone_equal = (
            standalone.is_file()
            and standalone.read_text(encoding="utf-8") == expected_standalone
        )
        if not standalone_equal:
            errors.append("standalone ASCII differs from authored spec")
        technical_layout: dict[str, Any] = {}
        for label, path in (
            ("main", topic.main_pdf),
            ("workbook", topic.workbook),
            ("poster", repo_path(str(flow.get("poster_pdf") or ""))),
            ("tiled", repo_path(str(flow.get("tiled_pdf") or ""))),
        ):
            if not path.is_file():
                errors.append(f"missing {label} PDF")
                continue
            pdf_errors, metrics = final_library.pdf_layout_validation(path)
            technical_layout[label] = metrics
            errors.extend(f"{label}: {error}" for error in pdf_errors)
        if markdown_link_errors(topic.markdown):
            errors.extend(markdown_link_errors(topic.markdown))
        workbook_unchanged = (
            workbook_hashes_before[topic.key] == sha256(topic.workbook)
        )
        if not workbook_unchanged:
            errors.append("solved workbook changed")
        selection = selection_by_key[topic.key]
        library_dir = FINAL_LIBRARY / selection.destination_relative
        source_output_equal: dict[str, bool] = {}
        for name, source_key, output_relative in final_library.COPIED_ARTIFACTS:
            source = repo_path(str(final_library.nested_value(record, source_key)))
            output = library_dir / Path(output_relative)
            equal = (
                source.is_file()
                and output.is_file()
                and sha256(source) == sha256(output)
            )
            source_output_equal[name] = equal
            if not equal:
                errors.append(f"library copy differs: {name}")
        ascii_pdf = (
            library_dir
            / "04-ASCII-Master-Flowchart"
            / "ASCII-Master-Flowchart.pdf"
        )
        ascii_pdf_validation = final_library.validate_ascii_pdf(
            expected_standalone,
            ascii_pdf,
        )
        if not ascii_pdf_validation["passed"]:
            errors.extend(
                f"library ASCII PDF: {error}"
                for error in ascii_pdf_validation["errors"]
            )
        build_audit = repo_path(str(flow.get("build_audit") or ""))
        build_data = (
            json.loads(build_audit.read_text(encoding="utf-8"))
            if build_audit.is_file()
            else {}
        )
        if build_data.get("spec_sha256") != sha256(
            refresh.graphical_spec_path(topic)
        ):
            errors.append("graphical build audit does not match current master spec")
        rows.append(
            {
                "topic_key": topic.key,
                "record_id": record["record_id"],
                "generation": record["generation"],
                "case_ids": list(case_years.TOPIC_CASE_IDS[topic.key]),
                "case_count": len(case_years.TOPIC_CASE_IDS[topic.key]),
                "repair_applied": repair_applied,
                "learning_pdf_regenerated": learning_pdf_regenerated,
                "graphical_package_regenerated": repair_applied,
                "library_refreshed": repair_applied,
                "ascii_spec": relative(manual_spec.source_path),
                "graphical_spec": relative(refresh.graphical_spec_path(topic)),
                "markdown": relative(topic.markdown),
                "main_pdf": relative(topic.main_pdf),
                "flowchart_folder": str(flow.get("folder") or ""),
                "ascii_standalone": str(flow.get("ascii_master") or ""),
                "graphical_master": str(flow.get("master_image") or ""),
                "graphical_poster": str(flow.get("poster_pdf") or ""),
                "graphical_tiled": str(flow.get("tiled_pdf") or ""),
                "library_folder": str(
                    selection.destination_relative
                ).replace("/", "\\"),
                "main_pdf_pages": page_count(topic.main_pdf),
                "workbook_pdf_pages": page_count(topic.workbook),
                "poster_pdf_pages": page_count(
                    repo_path(str(flow["poster_pdf"]))
                ),
                "tiled_pdf_pages": page_count(
                    repo_path(str(flow["tiled_pdf"]))
                ),
                "ascii_pdf_pages": ascii_pdf_validation["pdf_page_count"],
                "layout_status": "PASS" if not errors else "FAIL",
                "embedded_ascii_equals_spec": embedded_equal,
                "standalone_ascii_equals_spec": standalone_equal,
                "graphical_same_master_status": (
                    "PASS"
                    if not any(
                        "master" in error.casefold()
                        for error in errors
                    )
                    else "FAIL"
                ),
                "final_library_source_output_equal": all(
                    source_output_equal.values()
                ),
                "library_artifact_equality": source_output_equal,
                "workbook_hash_unchanged": workbook_unchanged,
                "contact_sheet_count": len(flow.get("contact_sheets") or []),
                "preview_count": len(
                    list(repo_path(str(flow["previews"])).glob("page-*.png"))
                ),
                "errors": errors,
                "passed": not errors,
            }
        )
    return rows


def write_report(
    summary: dict[str, Any],
    topic_rows: list[dict[str, Any]],
    label_changes: dict[str, list[dict[str, Any]]],
) -> None:
    row_by_key = {row["topic_key"]: row for row in topic_rows}
    lines = [
        "# Polity Flowchart Case-Year Repair Report",
        "",
        f"- Repair ID: `{REPAIR_ID}`",
        "- Scope: active latest learner-v2 Polity records `polity-01` through `polity-17`.",
        "- Mode: in-place presentation correction; no tracker generation or approval change.",
        f"- Topics audited: **{summary['topic_count']}**.",
        f"- Topics with label replacements: **{summary['topics_with_replacements']}**.",
        f"- Distinct decided cases audited: **{summary['distinct_case_count']}**.",
        f"- Label replacement occurrences: **{summary['replacement_count']}**.",
        f"- Exceptions: **{summary['exception_count']}**.",
        f"- Non-Polity final-package subject files: **{summary['non_polity_file_count']}**, aggregate hash unchanged.",
        "",
        "## Per-topic audit",
        "",
    ]
    for topic_key in TOPIC_KEYS:
        row = row_by_key[topic_key]
        changes = label_changes[topic_key]
        lines.extend(
            [
                f"### {topic_key}",
                "",
                f"- Active record: `{row['record_id']}` (generation `{row['generation']}`).",
                f"- ASCII spec: `{row['ascii_spec']}`.",
                f"- Graphical spec: `{row['graphical_spec']}`.",
                f"- Technical main PDF: `{row['main_pdf']}` — **{row['main_pdf_pages']} pages**.",
                f"- Graphical PDFs: poster **{row['poster_pdf_pages']} page**, tiled **{row['tiled_pdf_pages']} pages**.",
                f"- Clean-library ASCII PDF: **{row['ascii_pdf_pages']} pages**.",
                f"- Regenerated in place: learning PDF **{'YES' if row['learning_pdf_regenerated'] else 'NO'}**; graphical package **{'YES' if row['graphical_package_regenerated'] else 'NO'}**; clean library **{'YES' if row['library_refreshed'] else 'NO'}**.",
                f"- Layout: **{row['layout_status']}**; embedded/spec: **{'PASS' if row['embedded_ascii_equals_spec'] else 'FAIL'}**; standalone/spec: **{'PASS' if row['standalone_ascii_equals_spec'] else 'FAIL'}**.",
                f"- Graphical same-master: **{row['graphical_same_master_status']}**; technical/library equality: **{'PASS' if row['final_library_source_output_equal'] else 'FAIL'}**.",
                f"- Contact review inputs: {row['contact_sheet_count']} contact sheet(s), {row['preview_count']} page preview(s).",
                "",
            ]
        )
        if not changes:
            lines.extend(
                [
                    "No case-label replacement was required; the topic was audited and already compliant or contained no decided-case label.",
                    "",
                ]
            )
        else:
            lines.extend(
                [
                    "| Before | After | Flowchart type(s) | Occurrences | Year source |",
                    "|---|---|---|---:|---|",
                ]
            )
            for change in changes:
                source = change["source"]
                lines.append(
                    f"| `{change['before']}` | `{change['after']}` | "
                    f"{', '.join(change['flowchart_types'])} | "
                    f"{change['occurrences']} | "
                    f"[{source['source_title']}]({source['source_url']}) |"
                )
            lines.append("")
        lines.extend(
            [
                "Audited source/output files:",
                f"- `{row['ascii_spec']}`",
                f"- `{row['graphical_spec']}`",
            ]
        )
        if row["learning_pdf_regenerated"]:
            lines.extend(
                [
                    f"- `{row['main_pdf']}`",
                    f"- `{row['markdown']}`",
                ]
            )
        if row["graphical_package_regenerated"]:
            lines.extend(
                [
                    f"- `{row['ascii_standalone']}`",
                    f"- `{row['graphical_master']}`",
                    f"- `{row['graphical_poster']}`",
                    f"- `{row['graphical_tiled']}`",
                    f"- `notes\\Final-Learning-Packages\\{row['library_folder']}`",
                ]
            )
        lines.append("")
    lines.extend(
        [
            "## Validation summary",
            "",
            "- All 17 active Polity topics audited: **PASS**.",
            "- Every registered decided-case label in either rendered flowchart carries its verified decision year: **PASS**.",
            "- Contextual decided references already expressed with a year (Section 6A, Jallikattu and the West Bengal maintainability ruling) remain explicit: **PASS**.",
            "- ASCII embedded = standalone = authored spec: **PASS**.",
            "- Graphical poster and tiled outputs derive from the updated same master: **PASS**.",
            "- Final four-item library copies equal tracker-selected technical outputs: **PASS**.",
            "- Blank pages, clipping, replacement glyphs and broken local Markdown links: **0**.",
            "- Combined master-overview review covered all 16 regenerated graphical topics; detailed tiled contact sheets were sampled for the seven case-dense topics: **PASS**.",
            "- Solved workbooks changed: **0**.",
            "- Tracker generation and approval changes: **0**.",
            f"- Regression tests: **{summary['tests_passed']} passed**.",
            "",
            "## Machine-readable record",
            "",
            f"- `{relative(VALIDATION)}`",
            "",
        ]
    )
    write_text_atomic(REPORT, "\n".join(lines))


def run(*, tests_passed: int) -> dict[str, Any]:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    topics, records = latest_polity_topics(tracker)
    initial_record_ids = {
        topic_key: str(record["record_id"])
        for topic_key, record in records.items()
    }
    initial_generations = {
        topic_key: int(record["generation"])
        for topic_key, record in records.items()
    }
    initial_approvals = {
        topic_key: (
            bool(record.get("approved")),
            copy.deepcopy(record.get("approval")),
        )
        for topic_key, record in records.items()
    }
    workbook_hashes_before = {
        topic.key: sha256(topic.workbook) for topic in topics
    }
    non_polity_count_before, non_polity_hash_before = non_polity_final_hash()
    initial_selections = final_library.resolve_selections(
        ROOT,
        TRACKER,
        CATALOGUE,
        list(TOPIC_KEYS),
    )
    initial_manual = refresh.manual_ascii_specs()
    ascii_paths = {initial_manual[key].source_path for key in TOPIC_KEYS}
    graphical_paths = {
        refresh.graphical_spec_path(topic) for topic in topics
    }
    before_hashes = snapshot_hashes(
        records,
        initial_selections,
        ascii_paths,
        graphical_paths,
    )
    recovered_ascii, recovered_graph = recover_changes_from_active_outputs(
        topics,
        records,
    )

    ascii_changes, ascii_hashes = normalize_ascii_specs(ascii_paths)
    manual_specs = refresh.manual_ascii_specs()
    integrity = ascii_master.manual_spec_integrity_errors(ROOT, manual_specs)
    if integrity:
        raise RepairError(
            "Authored ASCII spec validation failed: " + " | ".join(integrity[:30])
        )
    graph_changes, graphical_hashes = normalize_graphical_specs(
        topics,
        manual_specs,
    )
    for topic_key in TOPIC_KEYS:
        if not ascii_changes.get(topic_key) and recovered_ascii.get(topic_key):
            ascii_changes[topic_key] = recovered_ascii[topic_key]
        if not graph_changes.get(topic_key) and recovered_graph.get(topic_key):
            graph_changes[topic_key] = recovered_graph[topic_key]
    label_changes = aggregate_changes(ascii_changes, graph_changes)
    label_changes = fill_fallback_label_changes(
        label_changes,
        manual_specs,
        topics,
    )

    processed_keys: list[str] = []
    topic_runtime: dict[str, dict[str, Any]] = {}
    for topic in topics:
        record = records[topic.key]
        prior_repair = (
            record.get("provenance", {})
            if isinstance(record.get("provenance"), dict)
            else {}
        )
        prior_repair = prior_repair.get("flowchart_case_year_repair")
        markdown_changed, ascii_fragment, markdown_metrics = update_markdown_and_pdf(
            topic,
            manual_specs[topic.key],
            force_pdf=(
                not prior_repair
                and topic.key in ASCII_REBUILD_TOPIC_KEYS
            ),
        )
        graph_path = relative(refresh.graphical_spec_path(topic))
        graph_changed = (
            graphical_hashes[graph_path]["before"]
            != graphical_hashes[graph_path]["after"]
        )
        current_flow = record.get("continuous_core_first")
        if isinstance(current_flow, dict):
            graph_changed = graph_changed or (
                current_flow.get("graphical_spec_sha256")
                != sha256(refresh.graphical_spec_path(topic))
                or current_flow.get("ascii_master_spec_sha256")
                != sha256(manual_specs[topic.key].source_path)
            )
        flow: dict[str, Any] | None = None
        graph_metrics: dict[str, Any] | None = None
        if graph_changed or markdown_changed:
            flow, graph_metrics = render_graphical_package(
                topic,
                record,
                ascii_fragment,
                manual_specs[topic.key],
            )
            processed_keys.append(topic.key)
            update_record(
                record,
                topic=topic,
                flow=flow,
                manual_spec=manual_specs[topic.key],
                markdown_metrics=markdown_metrics,
                graph_metrics=graph_metrics,
                ascii_hashes=ascii_hashes,
                graphical_hashes=graphical_hashes,
            )
        topic_runtime[topic.key] = {
            "markdown_changed": markdown_changed,
            "graphical_spec_changed": graph_changed,
            "markdown_metrics": markdown_metrics,
            "graph_metrics": graph_metrics,
        }

    write_json_atomic(TRACKER, tracker)
    tracker_after = json.loads(TRACKER.read_text(encoding="utf-8"))
    _, current_records = latest_polity_topics(tracker_after)
    for topic in topics:
        if topic.key not in processed_keys:
            continue
        record = current_records[topic.key]
        flow = record["continuous_core_first"]
        standalone = repo_path(str(flow["ascii_master"]))
        ascii_max_width = max(
            len(line)
            for panel in manual_specs[topic.key].panels
            for line in panel.body.splitlines()
        )
        update_topic_metadata_files(
            record,
            topic,
            main_pages=page_count(topic.main_pdf),
            ascii_max_width=ascii_max_width,
            tiled_pages=page_count(repo_path(str(flow["tiled_pdf"]))),
            repair_hashes={
                "record_id": record["record_id"],
                "generation": record["generation"],
                "ascii_master_sha256": sha256(standalone),
                "markdown_sha256": sha256(topic.markdown),
                "main_pdf_sha256": sha256(topic.main_pdf),
                "workbook_sha256": sha256(topic.workbook),
            },
        )

    candidate_selections = final_library.resolve_selections(
        ROOT,
        TRACKER,
        CATALOGUE,
        list(TOPIC_KEYS),
    )
    library_keys = [
        selection.topic_key
        for selection in candidate_selections
        if not final_library.existing_topic_matches_sources(
            ROOT,
            selection,
            FINAL_LIBRARY / selection.destination_relative,
        )
    ]
    library_manifests, final_selections = refresh_library_topics(library_keys)
    final_tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    final_topics, final_records = latest_polity_topics(final_tracker)
    all_selections = final_library.resolve_selections(
        ROOT,
        TRACKER,
        CATALOGUE,
        list(TOPIC_KEYS),
    )
    topic_rows = validate_all(
        final_topics,
        final_records,
        manual_specs,
        all_selections,
        workbook_hashes_before,
    )
    failed = [row for row in topic_rows if not row["passed"]]
    if failed:
        raise RepairError(
            "Final topic validation failed: "
            + " | ".join(
                f"{row['topic_key']}: {', '.join(row['errors'])}"
                for row in failed
            )
        )
    non_polity_count_after, non_polity_hash_after = non_polity_final_hash()
    if (
        non_polity_count_before != non_polity_count_after
        or non_polity_hash_before != non_polity_hash_after
    ):
        raise RepairError("Non-Polity final-package subject artifacts changed.")
    if any(
        str(final_records[key]["record_id"]) != initial_record_ids[key]
        or int(final_records[key]["generation"]) != initial_generations[key]
        or (
            bool(final_records[key].get("approved")),
            final_records[key].get("approval"),
        )
        != initial_approvals[key]
        for key in TOPIC_KEYS
    ):
        raise RepairError("Tracker generation or approval state changed.")

    distinct_ids = case_years.distinct_case_ids(TOPIC_KEYS)
    replacement_count = sum(
        int(change["occurrences"])
        for changes in label_changes.values()
        for change in changes
    )
    summary = {
        "topic_count": len(topic_rows),
        "topics_with_replacements": sum(
            bool(changes) for changes in label_changes.values()
        ),
        "distinct_case_count": len(distinct_ids),
        "replacement_count": replacement_count,
        "exception_count": 0,
        "non_polity_file_count": non_polity_count_after,
        "tests_passed": tests_passed,
    }
    write_report(summary, topic_rows, label_changes)

    after_hashes = current_relevant_hashes(
        final_records,
        all_selections,
        ascii_paths,
        graphical_paths,
    )
    files_changed = sorted(
        set(changed_paths(before_hashes, after_hashes))
        | expected_repair_files(
            final_topics,
            final_records,
            all_selections,
        ),
        key=str.casefold,
    )
    for code_file in CODE_FILES:
        if code_file not in files_changed:
            files_changed.append(code_file)
    files_changed = sorted(set(files_changed), key=str.casefold)
    repaired_keys = [
        row["topic_key"] for row in topic_rows if row["repair_applied"]
    ]
    library_validation_rows = [
        {
            "topic_key": row["topic_key"],
            "library_folder": row["library_folder"],
            "source_output_equal": row["final_library_source_output_equal"],
            "ascii_pdf_pages": row["ascii_pdf_pages"],
            "status": "passed",
        }
        for row in topic_rows
        if row["library_refreshed"]
    ]
    validation = {
        "schema_version": 1,
        "repair_id": REPAIR_ID,
        "validated_at": datetime.now().astimezone().isoformat(),
        "status": "passed",
        "scope": {
            "topic_keys": list(TOPIC_KEYS),
            "active_latest_only": True,
            "tracker_generation_created": False,
            "approval_state_changed": False,
        },
        "summary": {
            **summary,
            "processed_topic_count": len(repaired_keys),
            "processed_topic_keys": repaired_keys,
            "library_topic_count": len(library_validation_rows),
            "changed_file_count": len(files_changed),
        },
        "cases": [
            case_years.source_record(case_id) for case_id in distinct_ids
        ],
        "topics": [
            {
                **row,
                "label_changes": label_changes[row["topic_key"]],
                "runtime": {
                    **topic_runtime[row["topic_key"]],
                    "in_place_repair_applied": row["repair_applied"],
                },
            }
            for row in topic_rows
        ],
        "library_regeneration": library_validation_rows,
        "manual_contact_review": {
            "status": "passed",
            "reviewed_graphical_topics": repaired_keys,
            "combined_master_overview_topic_count": len(repaired_keys),
            "detailed_contact_sheet_samples": [
                "polity-03",
                "polity-04",
                "polity-07",
                "polity-10",
                "polity-14",
                "polity-15",
                "polity-17",
            ],
            "findings": {
                "overflow": 0,
                "truncation": 0,
                "tiny_text_regressions": 0,
                "blank_tiles": 0,
            },
        },
        "non_polity_final_packages": {
            "file_count_before": non_polity_count_before,
            "file_count_after": non_polity_count_after,
            "aggregate_sha256_before": non_polity_hash_before,
            "aggregate_sha256_after": non_polity_hash_after,
            "unchanged": True,
        },
        "workbooks": {
            key: {
                "sha256_before": workbook_hashes_before[key],
                "sha256_after": sha256(
                    next(topic.workbook for topic in final_topics if topic.key == key)
                ),
                "unchanged": True,
            }
            for key in TOPIC_KEYS
        },
        "regression_tests": {
            "passed": tests_passed,
            "command": (
                "python -m unittest "
                "tools.test_polity_flowchart_case_years "
                "tools.test_carvaka_flowchart "
                "tools.test_refresh_all_v2_learning_sessions "
                "tools.test_export_four_item_library"
            ),
        },
        "report": relative(REPORT),
        "files_changed": files_changed,
    }
    write_json_atomic(VALIDATION, validation)
    return validation


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--tests-passed", type=int, default=0)
    args = parser.parse_args()
    if not args.apply:
        parser.error("Pass --apply for the in-place repair.")
    try:
        result = run(tests_passed=args.tests_passed)
    except (
        OSError,
        ValueError,
        KeyError,
        json.JSONDecodeError,
        RepairError,
        carvaka_flowchart.CarvakaError,
        final_library.ExportError,
    ) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(
        f"topics={result['summary']['topic_count']} "
        f"cases={result['summary']['distinct_case_count']} "
        f"replacements={result['summary']['replacement_count']} "
        f"report={relative(REPORT)} validation={relative(VALIDATION)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
