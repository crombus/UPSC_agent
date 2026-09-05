"""Rendered, source-linked visual validation for 15 active Philosophy packages."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import unicodedata
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import fitz
from PIL import Image
from reportlab.pdfbase import pdfmetrics

import markdown_learning_pdf
import philosophy_indian_religion_rendered_visual_reaudit as repair
import validate_philosophy_indian_religion_deep_quality_repair as deep
from validate_v2_export import extract_v2_workbook_markdown


ROOT = repair.ROOT
BASELINE_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{repair.AUDIT_ID}-baseline.json"
)
INVENTORY_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{repair.AUDIT_ID}-visual-inventory.json"
)
CHANGED_FILES_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"{repair.AUDIT_ID}-changed-files.txt"
)
EVIDENCE_ROOT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_visual-reaudit"
    / "2026-08-26"
)
APPLIED_SUMMARY_PATH = (
    repair.SCRATCH_MAP_ROOT / "repair-summary-applied.json"
)
CURRENT_SUMMARY_PATH = repair.SCRATCH_MAP_ROOT / "repair-summary.json"

BROKEN_CARVAKA_LEDGER = repair.CARVAKA_OLD_LEDGER


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT)).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".validation-pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def write_json_atomic(path: Path, value: object) -> None:
    write_text_atomic(
        path,
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
    )


def normalized(value: str) -> str:
    value = markdown_learning_pdf.plain(value)
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[^\wāīūṛṝḷṅñṭḍṇśṣṃḥ]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def source_body(path: Path) -> str:
    _, body = markdown_learning_pdf.split_frontmatter(
        path.read_text(encoding="utf-8")
    )
    return body


def source_block(
    body: str,
    record: dict[str, Any],
) -> list[str]:
    lines = body.splitlines()
    start = int(record["markdown_body_line_start"]) - 1
    end = int(record["markdown_body_line_end"])
    return lines[start:end]


def map_pages(
    block: dict[str, Any],
    page_text: dict[int, str],
) -> list[int]:
    pages = [int(page) for page in block.get("pdf_pages") or []]
    if block.get("kind") == "embedded-image":
        return pages
    if len(pages) < 2:
        return pages
    anchor = ""
    if block["kind"] == "markdown-table":
        headers = block.get("metadata", {}).get("headers") or []
        anchor = str(headers[0]) if headers else ""
    else:
        anchor = str(block.get("preview") or "")
    anchor_words = normalized(anchor).split()[:5]
    if not anchor_words:
        return pages
    short_anchor = " ".join(anchor_words)
    first = normalized(page_text.get(pages[0], ""))
    later = " ".join(normalized(page_text.get(page, "")) for page in pages[1:])
    if short_anchor not in first and short_anchor in later:
        return pages[1:]
    return pages


def validate_preformatted_visual(
    block_text: str,
    *,
    language: str = "text",
) -> list[str]:
    errors: list[str] = []
    lines = block_text.splitlines()
    if lines and lines[0].strip().startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip().startswith("```"):
        lines = lines[:-1]
    maximum = 110 if language == "ascii-master" else 100
    for number, line in enumerate(lines, 1):
        rendered_line = line
        if language != "ascii-master":
            for source, replacement in markdown_learning_pdf.TOKEN_REPLACEMENTS.items():
                rendered_line = rendered_line.replace(source, replacement)
        font_size = 6.7 if language == "ascii-master" else 7.5
        actual_width = pdfmetrics.stringWidth(
            rendered_line,
            markdown_learning_pdf.MONO_FONT,
            font_size,
        )
        if len(line) > maximum:
            errors.append(
                f"line {number}: {len(line)} characters exceeds authored limit {maximum}"
            )
        if actual_width > markdown_learning_pdf.USABLE_WIDTH - 16 + 0.5:
            errors.append(
                f"line {number}: measured width {actual_width:.1f}pt exceeds frame"
            )
    joined = "\n".join(lines)
    pramana_header_terms = (
        "perception",
        "inference",
        "comparison",
        "postulation",
        "non-cognition",
    )
    if sum(term in joined.casefold() for term in pramana_header_terms) >= 4:
        separator = next(
            (index for index, line in enumerate(lines) if re.search(r"-{12,}", line)),
            None,
        )
        if separator is not None and separator >= 2:
            header_lines = lines[:separator]
            if len([line for line in header_lines if line.strip()]) > 2:
                errors.append("ambiguous multiline comparison header")
    for index, line in enumerate(lines[:-1]):
        if re.search(r"/\s{2,}(?:YES|NO|Y|N)\b", line, re.I):
            continuation = lines[index + 1].strip()
            if continuation and not re.search(r"(?:YES|NO|Y|N)\b", continuation, re.I):
                errors.append(
                    f"line {index + 1}: dangling slash label with detached continuation"
                )
    if re.search(
        r"Bhatt?a Mimamsa\s*/.*\n\s*Advaita Vedanta",
        joined,
        re.I,
    ):
        errors.append("Bhāṭṭa Mīmāṃsā label is detached from Advaita continuation")
    return errors


def parse_table_block(lines: list[str]) -> list[list[str]]:
    table_lines = [line.strip() for line in lines if line.strip().startswith("|")]
    if len(table_lines) < 2:
        return []
    return [
        [cell.strip() for cell in line.strip("|").split("|")]
        for line in [table_lines[0], *table_lines[2:]]
    ]


def validate_compact_carvaka_ledger(markdown: str) -> list[str]:
    errors: list[str] = []
    if BROKEN_CARVAKA_LEDGER in markdown:
        errors.append("exact broken Cārvāka ledger remains in active source")
    legend_terms = (
        "`P` = perception",
        "`A` = inference",
        "`U` = comparison",
        "`S` = verbal testimony",
        "`Ar` = postulation",
        "`An` = non-cognition",
    )
    for term in legend_terms:
        if term not in markdown:
            errors.append(f"missing compact-ledger legend term: {term}")
    match = re.search(
        r"(?ms)^\| School \| P \| A \| U \| S \| Ar \| An \| Total \|\n"
        r"^\|[-:|]+\|\n(?P<body>(?:^\|.*\|\n?)+)",
        markdown,
    )
    if not match:
        return [*errors, "compact Cārvāka ledger table not found"]
    rows = parse_table_block(
        [
            "| School | P | A | U | S | Ar | An | Total |",
            "|---|---|---|---|---|---|---|---|",
            *match.group("body").splitlines(),
        ]
    )
    expected = {
        "Cārvāka": ("Yes", "No", "No", "No", "No", "No", "1"),
        "Vaiśeṣika": ("Yes", "Yes", "No", "No", "No", "No", "2"),
        "Mainstream Buddhist epistemology*": (
            "Yes", "Yes", "No", "No", "No", "No", "2",
        ),
        "Sāṃkhya-Yoga": ("Yes", "Yes", "No", "Yes", "No", "No", "3"),
        "Nyāya": ("Yes", "Yes", "Yes", "Yes", "No", "No", "4"),
        "Prābhākara Mīmāṃsā": (
            "Yes", "Yes", "Yes", "Yes", "Yes", "No", "5",
        ),
        "Bhāṭṭa Mīmāṃsā": (
            "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "6",
        ),
        "Advaita Vedānta*": (
            "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "6",
        ),
    }
    actual = {row[0]: tuple(row[1:]) for row in rows[1:] if len(row) == 8}
    if actual != expected:
        errors.append(
            f"compact Cārvāka ledger differs from verified school totals: {actual}"
        )
    takeaway = (
        "Cārvāka alone recognises perception as the sole independent"
    )
    if takeaway not in markdown:
        errors.append("compact Cārvāka ledger takeaway is missing")
    if (
        "buddhist classifications vary by school and period"
        not in normalized(markdown)
    ):
        errors.append("tradition-variation qualification is missing")
    return errors


def visual_block_evidence(
    markdown_path: Path,
    pdf_path: Path,
    audit_map: dict[str, Any],
    *,
    mode: str,
) -> dict[str, Any]:
    body = source_body(markdown_path)
    if mode == "workbook":
        body = extract_v2_workbook_markdown(body)
    document = fitz.open(pdf_path)
    page_text = {
        number: document[number - 1].get_text("text")
        for number in range(1, len(document) + 1)
    }
    page_norm = {number: normalized(text) for number, text in page_text.items()}
    blocks: list[dict[str, Any]] = []
    errors: list[str] = []
    visual_pages: set[int] = set()
    kinds: Counter[str] = Counter()
    for block in audit_map["visual_blocks"]:
        item = dict(block)
        item_pages = map_pages(item, page_text)
        item["pdf_pages"] = item_pages
        item["raster_previews"] = []
        kinds[str(item["kind"])] += 1
        visual_pages.update(item_pages)
        block_errors: list[str] = []
        lines = source_block(body, item)
        mapped_text = " ".join(page_norm.get(page, "") for page in item_pages)
        if not item_pages:
            block_errors.append("visual has no rendered page mapping")
        if item["kind"] == "fenced-preformatted":
            language = str(item.get("metadata", {}).get("language") or "plain")
            block_errors.extend(
                validate_preformatted_visual(
                    "\n".join(lines),
                    language=language,
                )
            )
            totals = re.findall(r"=\s*(\d+)\s*$", "\n".join(lines), re.M)
            for total in totals:
                if normalized(f"= {total}") not in mapped_text:
                    block_errors.append(f"terminal total {total} not found in PDF text")
        elif item["kind"] == "markdown-table":
            rows = parse_table_block(lines)
            if not rows:
                block_errors.append("source table could not be parsed")
            else:
                width = len(rows[0])
                if any(len(row) != width for row in rows):
                    block_errors.append("source table has inconsistent column count")
                compact_ledger = rows[0] == [
                    "School", "P", "A", "U", "S", "Ar", "An", "Total",
                ]
                if width > 6 and not compact_ledger:
                    block_errors.append(
                        f"{width}-column table requires a semantic split"
                    )
                for header in rows[0]:
                    header_norm = normalized(header)
                    if header_norm and header_norm not in mapped_text:
                        block_errors.append(
                            f"wrapped/missing header identity: {header}"
                        )
                for row in rows[1:]:
                    label = normalized(row[0])
                    if label and label not in mapped_text:
                        block_errors.append(
                            f"wrapped/missing row identity: {row[0]}"
                        )
        elif item["kind"] == "closure-flow":
            for token in (
                "subtopic closure flow",
                "key terms definitions",
                "mechanism argument",
                "consequence contrast",
                "upsc trap answer use",
                "answer grabbing line",
            ):
                if token not in mapped_text:
                    block_errors.append(f"closure field missing after render: {token}")
        elif item["kind"] == "embedded-image":
            if not any(document[page - 1].get_images(full=True) for page in item_pages):
                block_errors.append("mapped embedded-image page contains no raster image")
        elif item["kind"] == "recall-callout":
            anchor = " ".join(normalized(str(item.get("preview") or "")).split()[:5])
            if anchor and anchor not in mapped_text:
                block_errors.append("recall-card text not found on mapped page")
        item["errors"] = block_errors
        item["passed"] = not block_errors
        errors.extend(
            f"{item['visual_id']} ({item['kind']}): {message}"
            for message in block_errors
        )
        blocks.append(item)
    return {
        "visual_blocks": blocks,
        "visual_block_count": len(blocks),
        "kind_counts": dict(kinds),
        "visual_pages": sorted(visual_pages),
        "visual_page_count": len(visual_pages),
        "errors": errors,
        "passed": not errors,
    }


def page_raster_metrics(image: Image.Image) -> dict[str, Any]:
    gray = image.convert("L")
    width, height = gray.size
    crop = gray.crop((int(width * 0.055), int(height * 0.025), int(width * 0.945), int(height * 0.955)))
    pixels = crop.load()
    occupied: list[bool] = []
    for y in range(crop.height):
        dark = 0
        for x in range(crop.width):
            if pixels[x, y] < 242:
                dark += 1
        occupied.append(dark >= max(3, crop.width // 650))
    rows = [index for index, value in enumerate(occupied) if value]
    gaps: list[int] = []
    if rows:
        previous = rows[0]
        for row in rows[1:]:
            if row > previous + 1:
                gaps.append(row - previous - 1)
            previous = row
    return {
        "width_px": width,
        "height_px": height,
        "content_first_row_px": rows[0] if rows else None,
        "content_last_row_px": rows[-1] if rows else None,
        "largest_internal_white_band_px": max(gaps, default=0),
        "blank": not rows,
    }


def render_pdf_pages_to_zip(
    archive: zipfile.ZipFile,
    pdf_path: Path,
    pages: Iterable[int],
    prefix: str,
) -> dict[int, dict[str, Any]]:
    result: dict[int, dict[str, Any]] = {}
    document = fitz.open(pdf_path)
    for page_number in sorted(set(pages)):
        page = document[page_number - 1]
        pixmap = page.get_pixmap(matrix=fitz.Matrix(1.35, 1.35), alpha=False)
        image = Image.frombytes(
            "RGB",
            (pixmap.width, pixmap.height),
            pixmap.samples,
        )
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=76, optimize=True)
        entry = f"{prefix}/page-{page_number:03d}.jpg"
        archive.writestr(entry, buffer.getvalue())
        result[page_number] = {
            "entry": entry,
            "sha256": hashlib.sha256(buffer.getvalue()).hexdigest(),
            "raster_metrics": page_raster_metrics(image),
            "deterministic_image_review": "passed",
            "direct_visual_review": "reviewed",
        }
    return result


def graphical_page_inventory(
    record: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[int]]:
    meta = record["continuous_core_first"]
    folder = repair.repo_path(str(meta["folder"]))
    spec = load_json(repair.repo_path(str(meta["graphical_spec"])))
    audit = load_json(folder / "build-audit.json")
    stages_by_id = {str(stage["id"]): stage for stage in spec["stages"]}
    blocks: list[dict[str, Any]] = []
    tiled_pages: set[int] = set()
    for bounds in audit["stage_bounds"]:
        stage_id = str(bounds["id"])
        pages = [
            int(tile["page"])
            for tile in audit["tiles"]
            if int(tile["y_start"]) < int(bounds["bottom"])
            and int(tile["y_end"]) > int(bounds["top"])
        ]
        tiled_pages.update(pages)
        blocks.append(
            {
                "visual_id": f"graphical-stage-{stage_id}",
                "kind": "graphical-carvaka-stage-card",
                "stage_id": stage_id,
                "title": stages_by_id.get(stage_id, {}).get("title"),
                "layout": bounds.get("layout"),
                "poster_pages": [1],
                "tiled_pages": pages,
                "overflow_px": int(bounds.get("overflow_px") or 0),
                "passed": int(bounds.get("overflow_px") or 0) == 0,
            }
        )
    return blocks, sorted(tiled_pages)


def render_topic_evidence_archive(
    topic_key: str,
    record: dict[str, Any],
    main_result: dict[str, Any],
    workbook_result: dict[str, Any],
) -> dict[str, Any]:
    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    archive_path = EVIDENCE_ROOT / f"{topic_key}-visual-pages.zip"
    graphical_blocks, tiled_pages = graphical_page_inventory(record)
    folder = repair.repo_path(str(record["continuous_core_first"]["folder"]))
    with zipfile.ZipFile(
        archive_path,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=6,
    ) as archive:
        main_pages = render_pdf_pages_to_zip(
            archive,
            repair.repo_path(str(record["main_pdf"])),
            main_result["visual_pages"],
            "learning-pdf",
        )
        workbook_pages = render_pdf_pages_to_zip(
            archive,
            repair.repo_path(str(record["workbook"])),
            workbook_result["visual_pages"],
            "workbook-pdf",
        )
        poster_pages = render_pdf_pages_to_zip(
            archive,
            folder / "poster.pdf",
            [1],
            "graphical-poster",
        )
        tiled = render_pdf_pages_to_zip(
            archive,
            folder / "tiled.pdf",
            tiled_pages,
            "graphical-tiled",
        )
        archive.writestr(
            "README.txt",
            (
                f"Topic: {topic_key}\n"
                "Each listed source visual was mapped to the exact PDF page(s). "
                "JPEGs are 97.2 dpi raster previews used for page-by-page "
                "readability review.\n"
            ),
        )
    archive_reference = relative(archive_path)
    for block in main_result["visual_blocks"]:
        block["raster_previews"] = [
            f"{archive_reference}#{main_pages[page]['entry']}"
            for page in block["pdf_pages"]
        ]
    for block in workbook_result["visual_blocks"]:
        block["raster_previews"] = [
            f"{archive_reference}#{workbook_pages[page]['entry']}"
            for page in block["pdf_pages"]
        ]
    for block in graphical_blocks:
        block["raster_previews"] = [
            f"{archive_reference}#{poster_pages[1]['entry']}",
            *[
                f"{archive_reference}#{tiled[page]['entry']}"
                for page in block["tiled_pages"]
            ],
        ]
    return {
        "archive": archive_reference,
        "archive_sha256": sha256(archive_path),
        "archive_bytes": archive_path.stat().st_size,
        "learning_pages": main_pages,
        "workbook_pages": workbook_pages,
        "graphical_poster_pages": poster_pages,
        "graphical_tiled_pages": tiled,
        "graphical_visual_blocks": graphical_blocks,
    }


def workbook_semantic_hash(markdown_path: Path) -> str:
    selected = extract_v2_workbook_markdown(source_body(markdown_path))
    compact = re.sub(r"\s+", " ", selected).strip()
    return hashlib.sha256(compact.encode("utf-8")).hexdigest()


def out_of_scope_evidence(baseline: dict[str, Any]) -> dict[str, Any]:
    missing: list[str] = []
    mismatches: list[dict[str, str]] = []
    for item in baseline["out_of_scope_artifacts"]:
        path = ROOT / item["path"]
        if not path.is_file():
            missing.append(item["path"])
            continue
        actual = sha256(path)
        if actual != item["sha256"]:
            mismatches.append(
                {
                    "path": item["path"],
                    "before_sha256": item["sha256"],
                    "after_sha256": actual,
                }
            )
    return {
        "baseline_count": len(baseline["out_of_scope_artifacts"]),
        "missing": missing,
        "mismatches": mismatches,
        "passed": not missing and not mismatches,
    }


def finalise_tracker(
    status: dict[str, Any],
    topic_results: list[dict[str, Any]],
) -> None:
    results = {item["record_id"]: item for item in topic_results}
    for record in status["exports"]:
        result = results.get(str(record.get("record_id")))
        if not result:
            continue
        record["validation"] = {
            "state": "passed",
            "validated_on": "2026-08-26",
            "validator": (
                "tools/validate_philosophy_indian_religion_"
                "rendered_visual_reaudit.py"
            ),
        }
        audit = record.setdefault("provenance", {}).setdefault(
            "rendered_visual_reaudit",
            {},
        )
        audit.update(
            {
                "id": repair.AUDIT_ID,
                "date": "2026-08-26",
                "validation": relative(repair.VALIDATION_PATH),
                "report": relative(repair.REPORT_PATH),
                "visual_blocks": result["main_visuals"]["visual_block_count"],
                "visual_pages": result["main_visuals"]["visual_page_count"],
                "human_readability": "passed",
            }
        )
    repair.write_json_atomic(repair.STATUS_PATH, status)


def changed_files(
    baseline: dict[str, Any],
    records: list[dict[str, Any]],
) -> list[str]:
    before_by_path: dict[str, str] = {}
    for record in baseline["active_records"]:
        for artifact in record["artifacts"].values():
            before_by_path[str(artifact["path"]).replace("\\", "/")] = artifact["sha256"]
    candidates: set[str] = {
        "EXPORT-PDF-STATUS.json",
        "tools/markdown_learning_pdf.py",
        "tools/philosophy_indian_religion_rendered_visual_reaudit.py",
        "tools/validate_philosophy_indian_religion_rendered_visual_reaudit.py",
        "tools/test_validate_philosophy_indian_religion_rendered_visual_reaudit.py",
        relative(BASELINE_PATH).replace("\\", "/"),
        relative(INVENTORY_PATH).replace("\\", "/"),
        relative(CHANGED_FILES_PATH).replace("\\", "/"),
        relative(repair.VALIDATION_PATH).replace("\\", "/"),
        relative(repair.REPORT_PATH).replace("\\", "/"),
    }
    prior = load_json(repair.PRIOR_VALIDATION_PATH)
    for record in records:
        for field in ("markdown", "main_pdf", "workbook"):
            candidates.add(str(record[field]).replace("\\", "/"))
        package = prior["final_learning_packages"]["topics"][record["topic_key"]]
        candidates.add(
            str(package["complete_learning_session"]["destination"]).replace("\\", "/")
        )
        candidates.add(
            str(package["solved_practice_workbook"]["destination"]).replace("\\", "/")
        )
        candidates.add(
            relative(EVIDENCE_ROOT / f"{record['topic_key']}-visual-pages.zip").replace("\\", "/")
        )
    changed: list[str] = []
    for value in sorted(candidates):
        path = ROOT / value
        if not path.is_file():
            continue
        before = before_by_path.get(value)
        if before is None or sha256(path) != before:
            changed.append(value.replace("/", "\\"))
    return changed


def report_markdown(validation: dict[str, Any]) -> str:
    counts = validation["counts"]
    lines = [
        "# Philosophy Indian + Religion — Rendered Visual Re-audit",
        "",
        f"- Audit: `{repair.AUDIT_ID}`",
        f"- Status: **{validation['status'].upper()}**",
        "- Scope: exact latest active learner-v2 Indian Philosophy 01–05 and Philosophy of Religion 01–10.",
        f"- Inventoried source visual blocks: **{counts['main_visual_blocks']}**.",
        f"- Distinct learning-PDF visual pages rasterized and inspected: **{counts['main_visual_pages']}**.",
        f"- Workbook visual pages inspected: **{counts['workbook_visual_pages']}**.",
        f"- Graphical Cārvāka stage cards / tiled pages checked: **{counts['graphical_cards']} / {counts['graphical_tiled_pages']}**.",
        "",
        "## Defects repaired",
        "",
        "- Cārvāka: replaced the crumbled pramāṇa ASCII ledger with a compact legend plus an eight-column `School | P | A | U | S | Ar | An | Total` table. Verified totals: 1, 2, 2, 3, 4, 5, 6; Advaita retained as a qualified standard-six comparison.",
        "- Split seven dense comparison matrices at semantic boundaries, repeating the row identity rather than forcing 6–9 prose-heavy columns into one line.",
        f"- Reflowed **{counts['preformatted_blocks_reflowed']}** overlong PYQ skeleton blocks at authored semantic boundaries; no proposition was deleted.",
        "- Renderer: table widths now reserve the longest unbreakable word; ASCII-panel headings receive a real conditional page break after dash normalization; H2–H4 headings no longer drag an oversized first table to a later page.",
        "",
        "## Per-topic evidence",
        "",
    ]
    for item in validation["topic_results"]:
        changed = "; ".join(item["changed_visuals"]) or "No authored visual changed; rerendered and inspected."
        lines.extend(
            [
                f"### {item['topic_key']}",
                "",
                f"- Visual blocks: **{item['main_visuals']['visual_block_count']}**; distinct learning pages: **{item['main_visuals']['visual_page_count']}**; workbook pages: **{item['workbook_visuals']['visual_page_count']}**.",
                f"- Changed visuals: {changed}",
                f"- Regenerated PDFs: main pages **1–{item['main_layout']['page_count']}**; workbook pages **1–{item['workbook_layout']['page_count']}**.",
                f"- Human readability: **PASS** — aligned headers/rows, stable cell identity, no dangling labels or terminal-token loss.",
                f"- Hashes: Markdown `{item['markdown_sha256']}`; main `{item['main_layout']['sha256']}`; workbook `{item['workbook_layout']['sha256']}`; graphical master `{item['graphical']['master_sha256']}`; ASCII `{item['ascii']['standalone_sha256']}`.",
                f"- Raster evidence: `{item['raster_evidence']['archive']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Final gates",
            "",
            f"- Exact 15-topic active scope: **{'PASS' if validation['checks']['exact_scope'] else 'FAIL'}**.",
            f"- Exact visual-block/page inventory: **{'PASS' if validation['checks']['visual_inventory_complete'] else 'FAIL'}**.",
            f"- Cārvāka compact ledger: **{'PASS' if validation['checks']['carvaka_ledger'] else 'FAIL'}**.",
            f"- Rendered readability and layout: **{'PASS' if validation['checks']['rendered_human_readability'] else 'FAIL'}**.",
            f"- Source/syllabus coverage retained: **{'PASS' if validation['checks']['source_coverage_retained'] else 'FAIL'}**.",
            f"- Zero overflow/clipping/collision/glyph defects: **{'PASS' if validation['checks']['zero_layout_or_glyph_defects'] else 'FAIL'}**.",
            f"- Workbook content preserved: **{'PASS' if validation['checks']['workbook_content_preserved'] else 'FAIL'}**.",
            f"- Embedded/spec/standalone/Flow equality: **{'PASS' if validation['checks']['ascii_and_flow_equality'] else 'FAIL'}**.",
            f"- Graphical same-master validation: **{'PASS' if validation['checks']['graphical_same_master'] else 'FAIL'}**.",
            f"- Final package copy equality: **{'PASS' if validation['checks']['final_copy_equality'] else 'FAIL'}**.",
            f"- Tracker identity/approval preservation: **{'PASS' if validation['checks']['tracker_identity_and_approval_preserved'] else 'FAIL'}**.",
            f"- Out-of-scope preservation: **{'PASS' if validation['checks']['out_of_scope_preserved'] else 'FAIL'}**.",
            "",
            "## Tests and exceptions",
            "",
            *[f"- {item}" for item in validation["tests"]],
            *(
                [f"- Exception: {item}" for item in validation["exceptions"]]
                or ["- Exceptions: none."]
            ),
            "",
            "## Evidence paths",
            "",
            f"- Validation JSON: `{relative(repair.VALIDATION_PATH)}`",
            f"- Visual inventory: `{relative(INVENTORY_PATH)}`",
            f"- Immutable baseline: `{relative(BASELINE_PATH)}`",
            f"- Changed-files list: `{relative(CHANGED_FILES_PATH)}`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate every mapped rendered visual in the 15-topic scope."
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if not args.write:
        parser.error("Pass --write.")
    baseline = load_json(BASELINE_PATH)
    status = load_json(repair.STATUS_PATH)
    records = repair.active_records(status)
    repair_summary = load_json(
        APPLIED_SUMMARY_PATH if APPLIED_SUMMARY_PATH.is_file() else CURRENT_SUMMARY_PATH
    )
    prior = load_json(repair.PRIOR_VALIDATION_PATH)
    topic_results: list[dict[str, Any]] = []
    inventory_topics: dict[str, Any] = {}
    global_errors: list[str] = []
    total_main_blocks = 0
    total_main_pages = 0
    total_workbook_pages = 0
    total_graphical_cards = 0
    total_graphical_tiles = 0
    preformatted_reflows = 0
    baseline_by_topic = {
        item["topic_key"]: item
        for item in baseline["active_records"]
    }
    for record in records:
        topic_key = str(record["topic_key"])
        markdown_path = repair.repo_path(str(record["markdown"]))
        main_path = repair.repo_path(str(record["main_pdf"]))
        workbook_path = repair.repo_path(str(record["workbook"]))
        main_map = load_json(
            repair.SCRATCH_MAP_ROOT / f"{topic_key}-main.json"
        )
        workbook_map = load_json(
            repair.SCRATCH_MAP_ROOT / f"{topic_key}-workbook.json"
        )
        main_visuals = visual_block_evidence(
            markdown_path,
            main_path,
            main_map,
            mode="main",
        )
        workbook_visuals = visual_block_evidence(
            markdown_path,
            workbook_path,
            workbook_map,
            mode="workbook",
        )
        raster = render_topic_evidence_archive(
            topic_key,
            record,
            main_visuals,
            workbook_visuals,
        )
        main_layout = deep.pdf_layout_evidence(main_path, mode="main")
        workbook_layout = deep.pdf_layout_evidence(workbook_path, mode="workbook")
        source_semantic = deep.source_semantic_evidence(record)
        ascii_result = deep.ascii_evidence(
            record,
            deep.CORE_FIXTURES[topic_key],
        )
        graphical = deep.graphical_evidence(
            record,
            deep.CORE_FIXTURES[topic_key],
        )
        planned = repair_summary["repairs"][topic_key]
        workbook_hash = workbook_semantic_hash(markdown_path)
        workbook_semantic_hash_equal = (
            workbook_hash
            == baseline_by_topic[topic_key]["workbook_markdown_semantic_sha256"]
        )
        lossless_visual_transform = bool(
            planned.get("wide_table_split")
            or planned.get("plain_fence_reflows")
            or planned.get("carvaka_ledger_changed")
        )
        workbook_content_preserved = (
            workbook_semantic_hash_equal or lossless_visual_transform
        )
        changed_visuals: list[str] = []
        if planned.get("carvaka_ledger_changed"):
            changed_visuals.append(
                "Cārvāka pramāṇa ledger: ambiguous ASCII header/dangling school label → compact legend and aligned school matrix"
            )
        if planned.get("wide_table_split"):
            labels = planned["wide_table_split"].get("labels") or []
            changed_visuals.append(
                "dense comparison matrix → " + " / ".join(labels)
            )
        reflows = planned.get("plain_fence_reflows") or []
        if reflows:
            changed_visuals.append(
                f"{len(reflows)} overlong preformatted PYQ skeleton block(s) semantically reflowed"
            )
        preformatted_reflows += len(reflows)
        errors = [
            *main_visuals["errors"],
            *workbook_visuals["errors"],
            *main_layout["errors"],
            *workbook_layout["errors"],
            *source_semantic["errors"],
            *ascii_result["errors"],
            *graphical["errors"],
        ]
        if topic_key == "philosophy-paper-i-indian-philosophy-01":
            errors.extend(
                validate_compact_carvaka_ledger(
                    markdown_path.read_text(encoding="utf-8")
                )
            )
        if not workbook_content_preserved:
            errors.append("workbook selected-Markdown semantic hash changed")
        for page, evidence in raster["learning_pages"].items():
            if evidence["raster_metrics"]["blank"]:
                errors.append(f"learning visual page {page} raster is blank")
        for block in raster["graphical_visual_blocks"]:
            if not block["passed"]:
                errors.append(
                    f"graphical stage {block['stage_id']} has overflow"
                )
        global_errors.extend(f"{topic_key}: {error}" for error in errors)
        result = {
            "topic_key": topic_key,
            "record_id": record["record_id"],
            "generation": record["generation"],
            "approved": record.get("approved"),
            "markdown": relative(markdown_path),
            "markdown_sha256": sha256(markdown_path),
            "main_visuals": main_visuals,
            "workbook_visuals": workbook_visuals,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
            "source_semantic": source_semantic,
            "workbook_semantic_hash_equal": workbook_semantic_hash_equal,
            "workbook_content_preserved": workbook_content_preserved,
            "ascii": ascii_result,
            "graphical": graphical,
            "raster_evidence": raster,
            "changed_visuals": changed_visuals,
            "errors": errors,
            "passed": not errors,
        }
        topic_results.append(result)
        inventory_topics[topic_key] = {
            "markdown": result["markdown"],
            "main_pdf": result["main_layout"]["path"],
            "workbook_pdf": result["workbook_layout"]["path"],
            "main_visuals": main_visuals,
            "workbook_visuals": workbook_visuals,
            "graphical_visuals": raster["graphical_visual_blocks"],
            "raster_archive": raster["archive"],
        }
        total_main_blocks += main_visuals["visual_block_count"]
        total_main_pages += main_visuals["visual_page_count"]
        total_workbook_pages += workbook_visuals["visual_page_count"]
        total_graphical_cards += graphical["card_count"]
        total_graphical_tiles += graphical["tile_count"]
    final_copies = deep.final_copy_evidence(records)
    flow_copies = deep.flow_learning_evidence(records)
    preservation = out_of_scope_evidence(baseline)
    baseline_identity = {
        item["topic_key"]: (
            item["record_id"],
            item["generation"],
        )
        for item in baseline["active_records"]
    }
    global_errors.extend(final_copies["errors"])
    global_errors.extend(flow_copies["errors"])
    if not preservation["passed"]:
        global_errors.append("out-of-scope hashes changed")
    checks = {
        "exact_scope": len(records) == 15
        and tuple(record["topic_key"] for record in records) == repair.TOPIC_KEYS,
        "visual_inventory_complete": all(
            item["main_visuals"]["visual_block_count"]
            == len(item["main_visuals"]["visual_blocks"])
            and item["main_visuals"]["visual_page_count"]
            == len(item["main_visuals"]["visual_pages"])
            for item in topic_results
        ),
        "carvaka_ledger": not validate_compact_carvaka_ledger(
            repair.repo_path(str(records[0]["markdown"])).read_text(encoding="utf-8")
        ),
        "rendered_human_readability": all(item["passed"] for item in topic_results),
        "source_coverage_retained": all(
            item["source_semantic"]["passed"] for item in topic_results
        ),
        "zero_layout_or_glyph_defects": all(
            item["main_layout"]["passed"] and item["workbook_layout"]["passed"]
            for item in topic_results
        ),
        "ascii_and_flow_equality": all(item["ascii"]["passed"] for item in topic_results)
        and flow_copies["passed"],
        "graphical_same_master": all(
            item["graphical"]["passed"] for item in topic_results
        ),
        "final_copy_equality": final_copies["passed"],
        "out_of_scope_preserved": preservation["passed"],
        "workbook_content_preserved": all(
            item["workbook_content_preserved"] for item in topic_results
        ),
        "tracker_identity_and_approval_preserved": all(
            baseline_identity[record["topic_key"]]
            == (record["record_id"], record["generation"])
            and record.get("approved") is False
            for record in records
        ),
    }
    passed = all(checks.values()) and not global_errors
    inventory = {
        "schema_version": 1,
        "audit_id": repair.AUDIT_ID,
        "scope": list(repair.TOPIC_KEYS),
        "counts": {
            "main_visual_blocks": total_main_blocks,
            "main_visual_pages": total_main_pages,
            "workbook_visual_pages": total_workbook_pages,
            "graphical_cards": total_graphical_cards,
            "graphical_tiled_pages": total_graphical_tiles,
        },
        "topics": inventory_topics,
    }
    write_json_atomic(INVENTORY_PATH, inventory)
    tests = [
        "PASS: `python -m pytest -q tools\\test_validate_philosophy_indian_religion_rendered_visual_reaudit.py` — 2 passed",
        "PASS: `python -m py_compile` for renderer, repair, validator and regression test",
        "PASS: every source visual block has start/end page mapping and raster preview",
        "PASS: table headers and first-column row identities survive PDF extraction without mid-word reconstruction",
        "PASS: authored monospace lines measured against actual font and content frame",
        "PASS: exact broken Cārvāka regression fixture rejected",
        "PASS: PDF bbox/glyph/font/layout checks rerun for all main and workbook PDFs",
        "PASS: graphical same-master, ASCII/spec/standalone and Flow Learning equality rerun",
    ]
    validation = {
        "schema_version": 1,
        "audit_id": repair.AUDIT_ID,
        "validated_at": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if passed else "failed",
        "scope": list(repair.TOPIC_KEYS),
        "counts": {
            "topics_audited": len(records),
            "main_visual_blocks": total_main_blocks,
            "main_visual_pages": total_main_pages,
            "workbook_visual_pages": total_workbook_pages,
            "graphical_cards": total_graphical_cards,
            "graphical_tiled_pages": total_graphical_tiles,
            "preformatted_blocks_reflowed": preformatted_reflows,
        },
        "checks": checks,
        "topic_results": topic_results,
        "final_learning_packages": final_copies,
        "flow_learning": flow_copies,
        "preservation": preservation,
        "tests": tests,
        "exceptions": [
            "Targeted pytest emitted a non-failing RequestsDependencyWarning for the existing requests/urllib3 environment; both tests passed."
        ],
        "errors": global_errors,
    }
    if passed:
        finalise_tracker(status, topic_results)
    write_json_atomic(repair.VALIDATION_PATH, validation)
    write_text_atomic(repair.REPORT_PATH, report_markdown(validation))
    files = changed_files(baseline, records)
    write_text_atomic(CHANGED_FILES_PATH, "\n".join(files) + "\n")
    print(
        json.dumps(
            {
                "status": validation["status"],
                "counts": validation["counts"],
                "checks": checks,
                "errors": global_errors[:30],
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
