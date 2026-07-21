"""Add searchable OCR text layers to low-text pages in local PDF books.

The script preserves each changed source in a backup tree, writes replacements
atomically, and records resumable per-book results in JSON.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import sys
import time
import unicodedata
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import fitz
import pytesseract
from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BOOKS = ROOT / "books"
DEFAULT_STATE = ROOT / "ingestion" / "ocr_completion_state.json"
DEFAULT_BACKUP = ROOT.parent / "upsc-agent-ocr-backups" / "2026-07-20"
TESSERACT = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
MIN_EXISTING_CHARS = 50
MIN_OCR_CHARS = 12
MIN_CONFIDENCE = 20.0
MAX_RASTER_DIMENSION = 4000

_WORKER: dict[str, object] = {}


def _worker_init(pdf_path: str, dpi: int) -> None:
    os.environ["OMP_THREAD_LIMIT"] = "1"
    pytesseract.pytesseract.tesseract_cmd = str(TESSERACT)
    _WORKER["doc"] = fitz.open(pdf_path)
    _WORKER["dpi"] = dpi


def _ascii_text(value: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u2026": "...",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", value).strip()


def _ocr_page(page_number: int) -> dict[str, object]:
    doc = _WORKER["doc"]
    dpi = _WORKER["dpi"]
    page = doc[page_number]
    try:
        requested_zoom = dpi / 72.0
        bounded_zoom = min(
            requested_zoom,
            MAX_RASTER_DIMENSION / max(page.rect.width, page.rect.height),
        )
        pix = page.get_pixmap(
            matrix=fitz.Matrix(bounded_zoom, bounded_zoom),
            colorspace=fitz.csRGB,
            alpha=False,
        )
        image = Image.open(io.BytesIO(pix.tobytes("png")))
        data = pytesseract.image_to_data(
            image,
            lang="eng",
            config="--oem 1 --psm 3",
            output_type=pytesseract.Output.DICT,
        )
        words: list[tuple[float, float, float, float, str]] = []
        accepted_text: list[str] = []
        for index, raw_text in enumerate(data["text"]):
            text = _ascii_text(raw_text)
            if not text:
                continue
            try:
                confidence = float(data["conf"][index])
            except (TypeError, ValueError):
                confidence = -1
            if confidence < MIN_CONFIDENCE:
                continue
            x = float(data["left"][index])
            y = float(data["top"][index])
            width = float(data["width"][index])
            height = float(data["height"][index])
            if width <= 0 or height <= 0:
                continue
            words.append((x, y, width, height, text))
            accepted_text.append(text)
        return {
            "page": page_number,
            "pix_width": pix.width,
            "pix_height": pix.height,
            "words": words,
            "chars": len(" ".join(accepted_text)),
            "error": "",
        }
    except Exception as exc:
        return {
            "page": page_number,
            "pix_width": 0,
            "pix_height": 0,
            "words": [],
            "chars": 0,
            "error": str(exc),
        }


def _load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"version": 1, "books": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _save_state(path: Path, state: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    os.replace(temporary, path)


def _low_text_pages(pdf_path: Path) -> tuple[int, list[int]]:
    with fitz.open(pdf_path) as doc:
        pages = [
            index
            for index, page in enumerate(doc)
            if len((page.get_text("text") or "").strip()) < MIN_EXISTING_CHARS
        ]
        return doc.page_count, pages


def _insert_words(page: fitz.Page, result: dict[str, object]) -> int:
    pix_width = int(result["pix_width"])
    pix_height = int(result["pix_height"])
    if pix_width <= 0 or pix_height <= 0:
        return 0

    scale_x = page.rect.width / pix_width
    scale_y = page.rect.height / pix_height
    inserted = 0
    for x, y, width, height, text in result["words"]:
        point = fitz.Point(
            page.rect.x0 + x * scale_x,
            page.rect.y0 + (y + height) * scale_y,
        )
        if page.rotation:
            point = point * page.derotation_matrix
        font_size = max(3.5, min(24.0, height * scale_y * 0.78))
        try:
            page.insert_text(
                point,
                text,
                fontsize=font_size,
                fontname="helv",
                render_mode=3,
                overlay=True,
            )
            inserted += 1
        except (RuntimeError, ValueError):
            continue
    return inserted


def _validate_output(
    source: Path, output: Path, expected_pages: int, repaired_pages: list[int]
) -> dict[str, object]:
    result: dict[str, object] = {
        "valid": False,
        "page_count": 0,
        "searchable_repaired_pages": 0,
        "remaining_low_text_pages": [],
        "error": "",
    }
    try:
        with fitz.open(output) as doc:
            result["page_count"] = doc.page_count
            if doc.page_count != expected_pages:
                result["error"] = (
                    f"page count changed: {expected_pages} -> {doc.page_count}"
                )
                return result
            remaining = [
                page_number + 1
                for page_number in repaired_pages
                if len((doc[page_number].get_text("text") or "").strip())
                < MIN_EXISTING_CHARS
            ]
            result["remaining_low_text_pages"] = remaining
            result["searchable_repaired_pages"] = len(repaired_pages) - len(remaining)
            result["valid"] = True
    except Exception as exc:
        result["error"] = str(exc)
    return result


def _rasterized_output(
    source: Path,
    output: Path,
    results: list[dict[str, object]],
    dpi: int,
) -> int:
    """Rebuild a structurally damaged image-only PDF with clean page resources."""
    by_page = {int(result["page"]): result for result in results}
    inserted_words = 0
    with fitz.open(source) as source_doc, fitz.open() as output_doc:
        output_doc.set_metadata(source_doc.metadata)
        for page_number, source_page in enumerate(source_doc):
            requested_zoom = dpi / 72.0
            bounded_zoom = min(
                requested_zoom,
                MAX_RASTER_DIMENSION
                / max(source_page.rect.width, source_page.rect.height),
            )
            pix = source_page.get_pixmap(
                matrix=fitz.Matrix(bounded_zoom, bounded_zoom),
                colorspace=fitz.csRGB,
                alpha=False,
            )
            output_page = output_doc.new_page(
                width=source_page.rect.width, height=source_page.rect.height
            )
            output_page.insert_image(
                output_page.rect,
                stream=pix.tobytes("jpeg", jpg_quality=88),
            )
            result = by_page.get(page_number)
            if result and int(result["chars"]) >= MIN_OCR_CHARS:
                inserted_words += _insert_words(output_page, result)
            if (page_number + 1) % 25 == 0 or page_number + 1 == source_doc.page_count:
                print(
                    f"  Rebuilding damaged PDF: "
                    f"{page_number + 1}/{source_doc.page_count}",
                    flush=True,
                )
        output_doc.save(output, garbage=2, deflate=True)
    return inserted_words


def repair_pdf(
    pdf_path: Path,
    books_root: Path,
    backup_root: Path,
    workers: int,
    dpi: int,
    force_raster: bool = False,
) -> dict[str, object]:
    relative = pdf_path.relative_to(books_root)
    page_count, low_text_pages = _low_text_pages(pdf_path)
    started = time.time()
    outcome: dict[str, object] = {
        "path": str(relative),
        "page_count": page_count,
        "low_text_before": len(low_text_pages),
        "ocr_meaningful_pages": 0,
        "blank_or_decorative_pages": [],
        "failed_pages": [],
        "searchable_repaired_pages": 0,
        "remaining_low_text_pages": [],
        "status": "unchanged",
        "seconds": 0,
        "completed_at": "",
    }
    if not low_text_pages:
        outcome["completed_at"] = datetime.now(timezone.utc).isoformat()
        return outcome

    print(
        f"\n[OCR] {relative} | {len(low_text_pages)}/{page_count} low-text pages",
        flush=True,
    )
    results: list[dict[str, object]] = []
    with ProcessPoolExecutor(
        max_workers=workers, initializer=_worker_init, initargs=(str(pdf_path), dpi)
    ) as executor:
        for done, result in enumerate(
            executor.map(_ocr_page, low_text_pages, chunksize=1), start=1
        ):
            results.append(result)
            if done % 20 == 0 or done == len(low_text_pages):
                print(f"  OCR pages: {done}/{len(low_text_pages)}", flush=True)

    failed = [int(result["page"]) + 1 for result in results if result["error"]]
    meaningful = [
        result for result in results if int(result["chars"]) >= MIN_OCR_CHARS
    ]
    blank = [
        int(result["page"]) + 1
        for result in results
        if not result["error"] and int(result["chars"]) < MIN_OCR_CHARS
    ]
    outcome["ocr_meaningful_pages"] = len(meaningful)
    outcome["blank_or_decorative_pages"] = blank
    outcome["failed_pages"] = failed

    if failed:
        outcome["status"] = "failed"
        outcome["seconds"] = round(time.time() - started, 1)
        return outcome
    if not meaningful:
        outcome["status"] = "blank-only"
        outcome["remaining_low_text_pages"] = [page + 1 for page in low_text_pages]
        outcome["seconds"] = round(time.time() - started, 1)
        outcome["completed_at"] = datetime.now(timezone.utc).isoformat()
        return outcome

    backup = backup_root / relative
    backup.parent.mkdir(parents=True, exist_ok=True)
    if not backup.exists():
        shutil.copy2(pdf_path, backup)

    temporary = pdf_path.with_name(pdf_path.stem + ".ocr-tmp.pdf")
    if temporary.exists():
        temporary.unlink()
    try:
        repaired_page_indexes = [int(result["page"]) for result in meaningful]
        rasterized_fallback = force_raster
        if force_raster:
            print("  Using requested clean raster rebuild.", flush=True)
            inserted_words = _rasterized_output(
                pdf_path, temporary, results, min(dpi, 180)
            )
            validation = _validate_output(
                pdf_path, temporary, page_count, repaired_page_indexes
            )
        else:
            with fitz.open(pdf_path) as doc:
                inserted_words = 0
                repaired_page_indexes = []
                for result in meaningful:
                    page_number = int(result["page"])
                    inserted = _insert_words(doc[page_number], result)
                    if inserted:
                        inserted_words += inserted
                        repaired_page_indexes.append(page_number)
                doc.save(temporary, garbage=2, deflate=True)

            validation = _validate_output(
                pdf_path, temporary, page_count, repaired_page_indexes
            )
        if (
            not force_raster
            and validation["valid"]
            and meaningful
            and not validation["searchable_repaired_pages"]
            and len(low_text_pages) == page_count
        ):
            print(
                "  Inserted text was discarded by damaged PDF resources; "
                "using clean raster rebuild.",
                flush=True,
            )
            temporary.unlink(missing_ok=True)
            inserted_words = _rasterized_output(
                pdf_path, temporary, results, min(dpi, 180)
            )
            validation = _validate_output(
                pdf_path, temporary, page_count, repaired_page_indexes
            )
            rasterized_fallback = True
        outcome.update(
            {
                "inserted_words": inserted_words,
                "rasterized_fallback": rasterized_fallback,
                "searchable_repaired_pages": validation[
                    "searchable_repaired_pages"
                ],
                "remaining_low_text_pages": validation["remaining_low_text_pages"],
            }
        )
        if not validation["valid"]:
            outcome["status"] = "failed"
            outcome["validation_error"] = validation["error"]
            temporary.unlink(missing_ok=True)
            return outcome
        os.replace(temporary, pdf_path)
        outcome["status"] = "repaired"
    finally:
        temporary.unlink(missing_ok=True)

    outcome["seconds"] = round(time.time() - started, 1)
    outcome["completed_at"] = datetime.now(timezone.utc).isoformat()
    return outcome


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_BOOKS)
    parser.add_argument("--backup-root", type=Path, default=DEFAULT_BACKUP)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--only", default="", help="Case-insensitive path substring")
    parser.add_argument("--dpi", type=int, default=220)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--force-raster",
        action="store_true",
        help="Rebuild selected image-only PDFs with clean page resources",
    )
    args = parser.parse_args()

    if not TESSERACT.exists():
        print(f"Tesseract not found: {TESSERACT}", file=sys.stderr)
        return 2

    books_root = args.root.resolve()
    state = _load_state(args.state)
    state_books = state.setdefault("books", {})
    pdfs = sorted(
        path
        for path in books_root.rglob("*.pdf")
        if ".ocr-tmp." not in path.name
        and (not args.only or args.only.lower() in str(path).lower())
    )
    print(f"PDFs selected: {len(pdfs)} | workers={args.workers} | dpi={args.dpi}")

    failures = 0
    for index, pdf_path in enumerate(pdfs, start=1):
        relative = str(pdf_path.relative_to(books_root))
        previous = state_books.get(relative, {})
        if (
            not args.force
            and previous.get("status") in {"repaired", "unchanged", "blank-only"}
            and previous.get("source_size") == pdf_path.stat().st_size
        ):
            print(f"[{index}/{len(pdfs)}] Skip completed: {relative}")
            continue
        print(f"[{index}/{len(pdfs)}] Inspecting: {relative}", flush=True)
        outcome = repair_pdf(
            pdf_path,
            books_root,
            args.backup_root,
            args.workers,
            args.dpi,
            args.force_raster,
        )
        outcome["source_size"] = pdf_path.stat().st_size
        state_books[relative] = outcome
        state["updated_at"] = datetime.now(timezone.utc).isoformat()
        _save_state(args.state, state)
        print(
            f"  {outcome['status']}: repaired "
            f"{outcome['searchable_repaired_pages']} pages; "
            f"blank/decorative {len(outcome['blank_or_decorative_pages'])}; "
            f"{outcome['seconds']}s",
            flush=True,
        )
        if outcome["status"] == "failed":
            print(f"  Failed pages: {outcome['failed_pages']}", file=sys.stderr)
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
