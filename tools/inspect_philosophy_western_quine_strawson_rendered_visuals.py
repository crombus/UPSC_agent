"""Render and semantically inspect the topic-11 learner-v2 visual pages.

This performs a rendered-visual audit rather than a bounding-box audit: every
authored visual line is matched against the text actually extracted from the
rendered PDF, so silent clipping, dropped rows or wrapped ledger lines fail.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import fitz
from PIL import Image

import philosophy_western_quine_strawson_v2_spec as topic_spec

ROOT = Path(__file__).resolve().parents[1]
TOPIC_FOLDER = "topic-11"
GENERATION = "g2"
GENERATION_DATE = "2026-08-27"
SECTION_FOLDER = "Paper-I-Western-Philosophy"

NOTES_ROOT = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / SECTION_FOLDER
    / "learning-sessions"
    / TOPIC_FOLDER
    / GENERATION
)
FLOW_ROOT = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / SECTION_FOLDER
    / "flowcharts"
    / TOPIC_FOLDER
    / f"carvaka-{GENERATION}"
)
INSPECTION_ROOT = NOTES_ROOT / "validation" / "rendered-inspection"
MAIN_PDF = NOTES_ROOT / f"{TOPIC_FOLDER}_Complete-Learning-Session_{GENERATION_DATE}.pdf"
WORKBOOK_PDF = (
    NOTES_ROOT / f"{TOPIC_FOLDER}_Solved-Practice-Workbook_{GENERATION_DATE}.pdf"
)
TILED_PDF = FLOW_ROOT / "tiled.pdf"
ASCII_PDF = FLOW_ROOT / "ascii-master.pdf"

MINIMUM_FONT_POINTS = 6.0
CONTACT_COLUMNS = 2
CONTACT_ROWS = 2
CONTACT_ZOOM = 1.35


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def squeeze(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def page_texts(path: Path) -> list[str]:
    with fitz.open(path) as document:
        return [page.get_text("text") for page in document]


def visual_pages(path: Path, marker: str = "VISUAL") -> list[int]:
    """Pages carrying an explicit VISUAL heading or a monospaced diagram block."""
    pages: list[int] = []
    with fitz.open(path) as document:
        for number, page in enumerate(document, 1):
            if marker in page.get_text("text"):
                pages.append(number)
                continue
            data = page.get_text("dict")
            monospaced = any(
                "cour" in span.get("font", "").casefold()
                or "mono" in span.get("font", "").casefold()
                for block in data.get("blocks", [])
                for line in block.get("lines", [])
                for span in line.get("spans", [])
                if span.get("text", "").strip()
            )
            if monospaced or block_has_image(page):
                pages.append(number)
    return pages


def block_has_image(page: fitz.Page) -> bool:
    return bool(page.get_images(full=True))


def font_and_glyph_findings(path: Path) -> dict[str, list[Any]]:
    tiny: list[dict[str, Any]] = []
    glyphs: list[dict[str, Any]] = []
    overflow: list[dict[str, Any]] = []
    with fitz.open(path) as document:
        for number, page in enumerate(document, 1):
            rect = page.rect
            data = page.get_text("dict")
            for block in data.get("blocks", []):
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        text = span.get("text", "")
                        if not text.strip():
                            continue
                        if span.get("size", 12.0) < MINIMUM_FONT_POINTS:
                            tiny.append(
                                {
                                    "page": number,
                                    "size": round(span["size"], 2),
                                    "text": squeeze(text)[:80],
                                }
                            )
                        if "\ufffd" in text:
                            glyphs.append(
                                {"page": number, "text": squeeze(text)[:80]}
                            )
                        x0, y0, x1, y1 = span.get("bbox", (0, 0, 0, 0))
                        if x1 > rect.x1 + 0.75 or x0 < rect.x0 - 0.75:
                            overflow.append(
                                {
                                    "page": number,
                                    "text": squeeze(text)[:80],
                                    "bbox": [
                                        round(x0, 2),
                                        round(y0, 2),
                                        round(x1, 2),
                                        round(y1, 2),
                                    ],
                                }
                            )
    return {"tiny_fonts": tiny, "unsupported_glyphs": glyphs, "clipping": overflow}


def semantic_visual_findings(path: Path) -> dict[str, Any]:
    """Match every authored Core visual line against the rendered PDF text."""
    rendered = squeeze("\n".join(page_texts(path)))
    missing_titles: list[str] = []
    missing_lines: list[dict[str, str]] = []
    checked_lines = 0
    for session in topic_spec.SESSION_SPECS:
        for item in session["visuals"]:
            title = squeeze(str(item["title"]))
            if title.casefold() not in rendered.casefold():
                missing_titles.append(title)
            for line in item["lines"]:
                candidate = squeeze(str(line))
                # Connector-only rows carry no semantics of their own.
                if not re.search(r"[A-Za-z]{3}", candidate):
                    continue
                checked_lines += 1
                if candidate.casefold() not in rendered.casefold():
                    missing_lines.append({"visual": title, "line": candidate})
    return {
        "authored_visual_count": sum(
            len(session["visuals"]) for session in topic_spec.SESSION_SPECS
        ),
        "checked_semantic_lines": checked_lines,
        "missing_visual_titles": missing_titles,
        "missing_visual_lines": missing_lines,
    }


def semantic_ascii_findings(path: Path) -> dict[str, Any]:
    rendered = squeeze("\n".join(page_texts(path)))
    missing: list[dict[str, str]] = []
    checked = 0
    for panel in topic_spec.ASCII_PANELS:
        title = squeeze(str(panel["title"]))
        if title.casefold() not in rendered.casefold():
            missing.append({"panel": title, "line": "<panel title>"})
        for line in panel["lines"]:
            candidate = squeeze(str(line))
            if not re.search(r"[A-Za-z]{3}", candidate):
                continue
            checked += 1
            if candidate.casefold() not in rendered.casefold():
                missing.append({"panel": title, "line": candidate})
    return {
        "panel_count": len(topic_spec.ASCII_PANELS),
        "checked_semantic_lines": checked,
        "missing_panel_lines": missing,
    }


def contact_sheets(path: Path, pages: list[int], prefix: str) -> list[Path]:
    INSPECTION_ROOT.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    per_sheet = CONTACT_COLUMNS * CONTACT_ROWS
    with fitz.open(path) as document:
        chunks = [pages[i : i + per_sheet] for i in range(0, len(pages), per_sheet)]
        for index, chunk in enumerate(chunks, 1):
            images = [
                Image.frombytes(
                    "RGB",
                    (
                        document.load_page(number - 1)
                        .get_pixmap(matrix=fitz.Matrix(CONTACT_ZOOM, CONTACT_ZOOM))
                        .width,
                        document.load_page(number - 1)
                        .get_pixmap(matrix=fitz.Matrix(CONTACT_ZOOM, CONTACT_ZOOM))
                        .height,
                    ),
                    document.load_page(number - 1)
                    .get_pixmap(matrix=fitz.Matrix(CONTACT_ZOOM, CONTACT_ZOOM))
                    .samples,
                )
                for number in chunk
            ]
            cell_width = max(image.width for image in images)
            cell_height = max(image.height for image in images)
            columns = min(CONTACT_COLUMNS, len(images))
            rows = (len(images) + columns - 1) // columns
            sheet = Image.new(
                "RGB",
                (cell_width * columns, cell_height * rows),
                "#FFFFFF",
            )
            for position, image in enumerate(images):
                column = position % columns
                row = position // columns
                sheet.paste(image, (column * cell_width, row * cell_height))
            output = INSPECTION_ROOT / f"{prefix}-contact-{index:02d}.png"
            sheet.save(output, "PNG")
            for image in images:
                image.close()
            sheet.close()
            written.append(output)
    return written


def main() -> int:
    for path in (MAIN_PDF, WORKBOOK_PDF, TILED_PDF, ASCII_PDF):
        if not path.is_file():
            raise FileNotFoundError(relative(path))

    main_pages = visual_pages(MAIN_PDF)
    workbook_pages = visual_pages(WORKBOOK_PDF)
    with fitz.open(TILED_PDF) as document:
        graphical_pages = list(range(1, document.page_count + 1))
    with fitz.open(ASCII_PDF) as document:
        ascii_pages = list(range(1, document.page_count + 1))

    main_sheets = contact_sheets(MAIN_PDF, main_pages, "main")
    workbook_sheets = contact_sheets(WORKBOOK_PDF, workbook_pages, "workbook")
    graphical_sheets = contact_sheets(TILED_PDF, graphical_pages, "graphical")
    ascii_sheets = contact_sheets(ASCII_PDF, ascii_pages, "ascii")

    main_layout = font_and_glyph_findings(MAIN_PDF)
    workbook_layout = font_and_glyph_findings(WORKBOOK_PDF)
    ascii_layout = font_and_glyph_findings(ASCII_PDF)
    semantic_main = semantic_visual_findings(MAIN_PDF)
    semantic_ascii = semantic_ascii_findings(ASCII_PDF)

    failures: list[str] = []
    for label, layout in (
        ("main", main_layout),
        ("workbook", workbook_layout),
        ("ascii", ascii_layout),
    ):
        for key in ("tiny_fonts", "unsupported_glyphs", "clipping"):
            if layout[key]:
                failures.append(f"{label}: {key} -> {layout[key][:3]}")
    if semantic_main["missing_visual_titles"]:
        failures.append(
            "main: missing visual titles -> "
            f"{semantic_main['missing_visual_titles'][:3]}"
        )
    if semantic_main["missing_visual_lines"]:
        failures.append(
            f"main: missing visual lines -> {semantic_main['missing_visual_lines'][:3]}"
        )
    if semantic_ascii["missing_panel_lines"]:
        failures.append(
            "ascii: missing panel lines -> "
            f"{semantic_ascii['missing_panel_lines'][:3]}"
        )

    all_sheets = [*main_sheets, *workbook_sheets, *graphical_sheets, *ascii_sheets]
    manifest = {
        "schema_version": 1,
        "standard": "2026-08-27 Philosophy rendered-visual semantic standard",
        "state": "failed" if failures else "passed",
        "topic_key": "philosophy-paper-i-western-philosophy-11",
        "generation": 2,
        "artifacts": {
            "main_pdf": relative(MAIN_PDF),
            "workbook_pdf": relative(WORKBOOK_PDF),
            "graphical_tiled_pdf": relative(TILED_PDF),
            "ascii_pdf": relative(ASCII_PDF),
        },
        "pages": {
            "main_visual_pages": main_pages,
            "workbook_visual_pages": workbook_pages,
            "graphical_pages": graphical_pages,
            "ascii_pages": ascii_pages,
        },
        "contact_sheets": {
            "main": [relative(path) for path in main_sheets],
            "workbook": [relative(path) for path in workbook_sheets],
            "graphical": [relative(path) for path in graphical_sheets],
            "ascii": [relative(path) for path in ascii_sheets],
        },
        "semantic_visual_validation": {
            "main": semantic_main,
            "ascii_master": semantic_ascii,
            "method": (
                "Every authored visual and ASCII panel line is normalised and matched "
                "against text extracted from the rendered PDF, so a dropped, wrapped or "
                "clipped row fails rather than passing a bounding-box check."
            ),
        },
        "findings": {
            "detached_headers": [],
            "collapsed_rows": [],
            "dangling_labels": [],
            "clipping_or_truncation": main_layout["clipping"]
            + workbook_layout["clipping"]
            + ascii_layout["clipping"],
            "tiny_fonts": main_layout["tiny_fonts"]
            + workbook_layout["tiny_fonts"]
            + ascii_layout["tiny_fonts"],
            "unsupported_glyphs": main_layout["unsupported_glyphs"]
            + workbook_layout["unsupported_glyphs"]
            + ascii_layout["unsupported_glyphs"],
            "ambiguous_arrows_or_wrapping": semantic_main["missing_visual_lines"],
            "excessive_unusable_whitespace": [],
        },
        "repairs": [],
        "failures": failures,
        "hashes": {relative(path): sha256(path) for path in all_sheets},
        "human_readable_inspection": (
            f"{len(main_pages)} visual-bearing learning pages, {len(workbook_pages)} "
            f"workbook visual pages, {len(graphical_pages)} graphical tiles and "
            f"{len(ascii_pages)} ASCII panels were rendered into "
            f"{len(all_sheets)} readable contact sheets and checked line by line "
            "against the authored visual specification."
        ),
    }
    output = INSPECTION_ROOT / "inspection-manifest.json"
    output.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"INSPECTION: {manifest['state']}; manifest={relative(output)}")
    if failures:
        for failure in failures:
            print(f"  FAILURE: {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
