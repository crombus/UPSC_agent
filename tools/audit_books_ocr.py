"""Audit searchable text coverage after local PDF OCR remediation."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BOOKS = ROOT / "books"
DEFAULT_STATE = ROOT / "ingestion" / "ocr_completion_state.json"
DEFAULT_REPORT = ROOT / "BOOKS_OCR_AUDIT.md"
DEFAULT_JSON = ROOT / "ingestion" / "ocr_final_audit.json"
RELIABLE_TEXT_CHARS = 50


def ranges(page_numbers: list[int]) -> str:
    if not page_numbers:
        return "-"
    values = sorted(set(page_numbers))
    output: list[str] = []
    start = previous = values[0]
    for value in values[1:]:
        if value == previous + 1:
            previous = value
            continue
        output.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = value
    output.append(str(start) if start == previous else f"{start}-{previous}")
    return ", ".join(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_BOOKS)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    args = parser.parse_args()

    state = json.loads(args.state.read_text(encoding="utf-8"))["books"]
    records: list[dict[str, object]] = []
    failures: list[str] = []

    pdfs = sorted(args.root.rglob("*.pdf"))
    for index, pdf_path in enumerate(pdfs, start=1):
        relative = str(pdf_path.relative_to(args.root))
        book_state = state.get(relative, {})
        expected_blank = set(book_state.get("blank_or_decorative_pages", []))
        try:
            with fitz.open(pdf_path) as doc:
                page_chars = [
                    len((page.get_text("text") or "").strip()) for page in doc
                ]
                if doc.page_count:
                    doc[0].get_pixmap(matrix=fitz.Matrix(0.25, 0.25), alpha=False)
                    if doc.page_count > 1:
                        doc[-1].get_pixmap(
                            matrix=fitz.Matrix(0.25, 0.25), alpha=False
                        )
                page_count = doc.page_count
        except Exception as exc:
            failures.append(f"{relative}: {exc}")
            continue

        zero_pages = [
            page + 1 for page, char_count in enumerate(page_chars) if char_count == 0
        ]
        sparse_pages = [
            page + 1
            for page, char_count in enumerate(page_chars)
            if 0 < char_count < RELIABLE_TEXT_CHARS
        ]
        reliable_pages = sum(
            char_count >= RELIABLE_TEXT_CHARS for char_count in page_chars
        )
        unresolved_zero = [
            page for page in zero_pages if page not in expected_blank
        ]
        sparse_meaningful = [
            page for page in sparse_pages if page not in expected_blank
        ]
        records.append(
            {
                "path": relative,
                "pages": page_count,
                "reliable_pages": reliable_pages,
                "searchable_pages": page_count - len(zero_pages),
                "zero_pages": zero_pages,
                "sparse_pages": sparse_pages,
                "sparse_meaningful_pages": sparse_meaningful,
                "blank_or_decorative_pages": sorted(expected_blank),
                "unresolved_zero_pages": unresolved_zero,
                "ocr_status": book_state.get("status", "not-recorded"),
                "searchable_repaired_pages": book_state.get(
                    "searchable_repaired_pages", 0
                ),
                "rasterized_fallback": book_state.get(
                    "rasterized_fallback", False
                ),
            }
        )
        print(f"[{index}/{len(pdfs)}] {relative}", flush=True)

    total_pages = sum(int(record["pages"]) for record in records)
    reliable_pages = sum(int(record["reliable_pages"]) for record in records)
    searchable_pages = sum(int(record["searchable_pages"]) for record in records)
    unresolved = sum(
        len(record["unresolved_zero_pages"]) for record in records
    )
    repaired_files = sum(
        record["ocr_status"] == "repaired" for record in records
    )
    unchanged_files = sum(
        record["ocr_status"] == "unchanged" for record in records
    )
    blank_only_files = sum(
        record["ocr_status"] == "blank-only" for record in records
    )
    repaired_pages = sum(
        int(record["searchable_repaired_pages"]) for record in records
    )
    blank_classified = sum(
        len(record["blank_or_decorative_pages"]) for record in records
    )
    sparse_meaningful = sum(
        len(record["sparse_meaningful_pages"]) for record in records
    )

    summary = {
        "audited_at": datetime.now().astimezone().isoformat(),
        "pdfs": len(records),
        "pages": total_pages,
        "read_failures": failures,
        "reliable_pages": reliable_pages,
        "searchable_pages": searchable_pages,
        "unresolved_meaningful_zero_text_pages": unresolved,
        "repaired_files": repaired_files,
        "unchanged_files": unchanged_files,
        "blank_only_files": blank_only_files,
        "searchable_repaired_pages": repaired_pages,
        "ocr_classified_blank_or_decorative_pages": blank_classified,
        "sparse_but_searchable_meaningful_pages": sparse_meaningful,
    }
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(
        json.dumps({"summary": summary, "books": records}, indent=2),
        encoding="utf-8",
    )

    lines = [
        "# Books Folder OCR Audit",
        "",
        f"Final audit: **{summary['audited_at']}**",
        "",
        "## Completion summary",
        "",
        f"- PDFs audited and opened successfully: **{len(records)}/{len(pdfs)}**",
        f"- Total pages verified: **{total_pages:,}**",
        f"- PDFs repaired with searchable OCR layers: **{repaired_files}**",
        f"- PDFs already requiring no repair: **{unchanged_files}**",
        (
            "- PDFs whose only low-text pages were blank/decorative: "
            f"**{blank_only_files}**"
        ),
        f"- Pages made reliably searchable by this run: **{repaired_pages:,}**",
        f"- Pages with at least some searchable text: **{searchable_pages:,}**",
        f"- Pages with at least {RELIABLE_TEXT_CHARS} extracted characters: "
        f"**{reliable_pages:,}**",
        (
            "- Sparse but searchable meaningful pages (covers, answer-key grids, "
            f"short labels): **{sparse_meaningful}**"
        ),
        (
            "- OCR-classified blank/decorative/divider pages: "
            f"**{blank_classified}**"
        ),
        f"- Meaningful pages still containing zero searchable text: **{unresolved}**",
        f"- PDF read/render failures: **{len(failures)}**",
        "",
        (
            "**Result:** OCR remediation is complete when the meaningful zero-text "
            "count and PDF failure count are both zero."
        ),
        "",
        "Original PDFs changed by OCR are preserved under:",
        "",
        "`C:\\Users\\pulkitkundra\\Downloads\\pk-workspace\\"
        "upsc-agent-ocr-backups\\2026-07-20\\`",
        "",
        "Page numbers below are PDF page numbers, not printed book page numbers.",
        "",
        "## Residual sparse or blank/decorative pages",
        "",
    ]
    for record in records:
        sparse = record["sparse_meaningful_pages"]
        blank = record["blank_or_decorative_pages"]
        unresolved_pages = record["unresolved_zero_pages"]
        if not sparse and not blank and not unresolved_pages:
            continue
        lines.extend(
            [
                f"### `{record['path']}`",
                f"- Sparse but searchable pages: **{ranges(sparse)}**",
                f"- Blank/decorative/divider pages: **{ranges(blank)}**",
                f"- Unresolved meaningful zero-text pages: "
                f"**{ranges(unresolved_pages)}**",
                "",
            ]
        )

    lines.extend(["## Per-PDF coverage", ""])
    for record in records:
        lines.extend(
            [
                f"### `{record['path']}`",
                (
                    f"- Searchable pages: **{record['searchable_pages']}/"
                    f"{record['pages']}**; reliable-text pages: "
                    f"**{record['reliable_pages']}/{record['pages']}**."
                ),
                (
                    f"- OCR result: **{record['ocr_status']}**; pages made reliably "
                    f"searchable: **{record['searchable_repaired_pages']}**."
                ),
                "",
            ]
        )

    if failures:
        lines.extend(["## Read/render failures", ""])
        lines.extend(f"- {failure}" for failure in failures)
        lines.append("")

    args.report.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 1 if failures or unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
