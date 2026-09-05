"""Render Unicode-heavy Markdown to PDF through Chromium."""

from __future__ import annotations

import html
import os
import re
import subprocess
from pathlib import Path

import fitz
import markdown


CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
RENDERER_NAME = "unicode-markdown-pdf"
RENDERER_VERSION = "2.0"

CSS = """
@page {
  size: A4;
  margin: 18mm 16mm 18mm 16mm;
}
body {
  color: #172033;
  font-family: "Nirmala UI", "Mangal", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.48;
  word-break: keep-all;
  overflow-wrap: normal;
}
h1 {
  color: #ffffff;
  background: #14243d;
  border-left: 7px solid #dd9414;
  padding: 18px 20px;
  font-size: 23pt;
  page-break-before: always;
}
h1:first-child { page-break-before: avoid; }
h2 {
  color: #15365f;
  border-bottom: 2px solid #dd9414;
  padding-bottom: 4px;
  margin-top: 24px;
  page-break-after: avoid;
}
h3, h4 { color: #1d5c8f; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
.cover {
  min-height: 245mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  page-break-after: always;
}
.cover h1 {
  page-break-before: avoid;
  margin: 0 0 18px 0;
}
.cover .descriptor {
  color: #38536f;
  font-size: 11pt;
  font-weight: 600;
  margin: 0 12px 14px 12px;
}
.contents {
  page-break-after: always;
}
.contents h1 {
  page-break-before: avoid;
  font-size: 18pt;
}
.contents-intro {
  color: #52677d;
  font-size: 8.5pt;
}
.contents-list {
  columns: 2;
  column-gap: 18px;
  column-rule: 1px solid #d5dde6;
}
.contents-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  border-bottom: 1px dotted #9baabd;
  padding: 1px 0;
  font-size: 7.8pt;
  line-height: 1.22;
  break-inside: avoid;
}
.contents-row.level-3 {
  padding-left: 10px;
  font-size: 7.4pt;
}
.contents-row.level-4 {
  padding-left: 20px;
  font-size: 7.1pt;
}
.pdf-anchor {
  color: rgba(255, 255, 255, 0.01);
  font-size: 1px;
  letter-spacing: 0;
}
blockquote {
  background: #eef5fb;
  border-left: 4px solid #2c6da4;
  margin: 12px 0;
  padding: 8px 12px;
}
table {
  border-collapse: collapse;
  width: 100%;
  table-layout: fixed;
  margin: 12px 0;
  font-size: 8.5pt;
}
th {
  background: #245b88;
  color: white;
}
th, td {
  border: 1px solid #b7c5d4;
  padding: 5px;
  overflow-wrap: break-word;
  word-break: keep-all;
  vertical-align: top;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
pre {
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  background: #f3f6f9;
  border: 1px solid #d6dde5;
  padding: 9px;
}
code { font-family: Consolas, "Nirmala UI", monospace; }
"""


def _plain_heading(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value)).strip()


def _split_front_matter(text: str) -> tuple[str, str, str]:
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("Unicode package Markdown must begin with an H1 title.")
    title = lines[0][2:].strip()
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    quote: list[str] = []
    while index < len(lines) and lines[index].lstrip().startswith(">"):
        quote.append(lines[index].lstrip()[1:].strip())
        index += 1
    while index < len(lines) and not lines[index].strip():
        index += 1
    return title, "\n".join(quote), "\n".join(lines[index:])


def _body_with_heading_anchors(
    markdown_text: str,
) -> tuple[str, list[dict[str, object]]]:
    body = markdown.markdown(
        markdown_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
    )
    headings: list[dict[str, object]] = []

    def replace(match: re.Match[str]) -> str:
        level = int(match.group(1))
        rendered = match.group(2)
        title = _plain_heading(rendered)
        token = f"HIDX{len(headings) + 1:04d}"
        headings.append({"level": level, "title": title, "token": token})
        return (
            f'<h{level}>{rendered}'
            f'<span class="pdf-anchor">{token}</span></h{level}>'
        )

    body = re.sub(r"<h([2-4])>(.*?)</h\1>", replace, body, flags=re.DOTALL)
    return body, headings


def _contents_html(
    headings: list[dict[str, object]],
    page_map: dict[str, int],
    title: str,
) -> str:
    rows = []
    for heading in headings:
        if int(heading["level"]) != 2:
            continue
        token = str(heading["token"])
        rows.append(
            f'<div class="contents-row level-{heading["level"]}">'
            f'<span>{html.escape(str(heading["title"]))}</span>'
            f'<span>{page_map.get(token, "?")}</span></div>'
        )
    return (
        '<section class="contents">'
        f"<h1>{html.escape(title)}</h1>"
        '<p class="contents-intro">Page numbers are generated from the final '
        "layout. PDF bookmarks include finer subheadings.</p>"
        + '<div class="contents-list">'
        + "".join(rows)
        + "</div>"
        + "</section>"
    )


def _document_html(
    title: str,
    introduction: str,
    descriptor: str,
    body: str,
    headings: list[dict[str, object]],
    page_map: dict[str, int],
    index_title: str,
) -> str:
    quote = (
        "<blockquote>"
        + "<br>".join(html.escape(line) for line in introduction.splitlines())
        + "</blockquote>"
        if introduction
        else ""
    )
    return (
        '<!doctype html><html lang="hi"><head><meta charset="utf-8">'
        f"<style>{CSS}</style></head><body>"
        '<section class="cover">'
        f"<h1>{html.escape(title)}</h1>"
        f'<p class="descriptor">{html.escape(descriptor)}</p>'
        f"{quote}</section>"
        f"{_contents_html(headings, page_map, index_title)}"
        f"<main>{body}</main></body></html>"
    )


def _print_html(html_path: Path, output_path: Path) -> None:
    subprocess.run(
        [
            str(CHROME),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={output_path}",
            html_path.as_uri(),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError(f"Chromium did not create {output_path}")


def _heading_pages(
    pdf_path: Path,
    headings: list[dict[str, object]],
) -> dict[str, int]:
    result: dict[str, int] = {}
    with fitz.open(pdf_path) as document:
        for page_number, page in enumerate(document, 1):
            text = page.get_text("text")
            for heading in headings:
                token = str(heading["token"])
                if token in text:
                    result[token] = page_number
    missing = [
        str(heading["title"])
        for heading in headings
        if str(heading["token"]) not in result
    ]
    if missing:
        raise RuntimeError(f"Could not locate rendered headings: {missing}")
    return result


def _finalize_pdf(
    pdf_path: Path,
    headings: list[dict[str, object]],
    page_map: dict[str, int],
    index_title: str,
    footer_label: str,
) -> None:
    finalized = pdf_path.with_suffix(".finalized.pdf")
    with fitz.open(pdf_path) as document:
        toc = [[1, index_title, 2]]
        for heading in headings:
            toc.append(
                [
                    int(heading["level"]) - 1,
                    str(heading["title"]),
                    page_map[str(heading["token"])],
                ]
            )
        document.set_toc(toc)
        for page_number, page in enumerate(document, 1):
            for heading in headings:
                for rectangle in page.search_for(str(heading["token"])):
                    page.add_redact_annot(rectangle, fill=False)
            page.apply_redactions()
            footer = f"{footer_label} | {page_number}/{document.page_count}"
            page.insert_text(
                (page.rect.width / 2 - 70, page.rect.height - 18),
                footer,
                fontsize=7,
                fontname="helv",
                color=(0.25, 0.32, 0.4),
            )
        document.save(finalized, garbage=4, deflate=True)
    os.replace(finalized, pdf_path)


def build_pdf(
    source: str | Path,
    output: str | Path,
    *,
    internal_index: bool = False,
    index_title: str = "CONTENTS",
    cover_descriptor: str = "",
    footer_label: str = "UPSC Qualifying Language",
) -> Path:
    source_path = Path(source).resolve()
    output_path = Path(output).resolve()
    if not source_path.is_file():
        raise FileNotFoundError(source_path)
    if not CHROME.is_file():
        raise FileNotFoundError(CHROME)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_path = output_path.with_suffix(".render.html")
    source_text = source_path.read_text(encoding="utf-8")
    if not internal_index:
        body = markdown.markdown(
            source_text,
            extensions=["extra", "tables", "fenced_code", "sane_lists"],
        )
        html_path.write_text(
            '<!doctype html><html lang="hi"><head><meta charset="utf-8">'
            f"<style>{CSS}</style></head><body>{body}</body></html>",
            encoding="utf-8",
        )
        try:
            _print_html(html_path, output_path)
        finally:
            if html_path.is_file():
                html_path.unlink()
        return output_path

    title, introduction, main_markdown = _split_front_matter(source_text)
    body, headings = _body_with_heading_anchors(main_markdown)
    page_map: dict[str, int] = {}
    pass_pdf = output_path.with_suffix(".layout-pass.pdf")
    try:
        for _ in range(4):
            html_path.write_text(
                _document_html(
                    title,
                    introduction,
                    cover_descriptor,
                    body,
                    headings,
                    page_map,
                    index_title,
                ),
                encoding="utf-8",
            )
            _print_html(html_path, pass_pdf)
            updated = _heading_pages(pass_pdf, headings)
            if updated == page_map:
                break
            page_map = updated
        else:
            raise RuntimeError("Unicode contents pagination did not stabilize.")
        os.replace(pass_pdf, output_path)
        _finalize_pdf(
            output_path,
            headings,
            page_map,
            index_title,
            footer_label,
        )
    finally:
        if html_path.is_file():
            html_path.unlink()
        if pass_pdf.is_file():
            pass_pdf.unlink()
    return output_path
