"""Render Unicode-heavy Markdown to PDF through Chromium."""

from __future__ import annotations

import subprocess
from pathlib import Path

import markdown


CHROME = Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

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
  overflow-wrap: anywhere;
  vertical-align: top;
}
pre {
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  background: #f3f6f9;
  border: 1px solid #d6dde5;
  padding: 9px;
}
code { font-family: Consolas, "Nirmala UI", monospace; }
"""


def build_pdf(source: str | Path, output: str | Path) -> Path:
    source_path = Path(source).resolve()
    output_path = Path(output).resolve()
    if not source_path.is_file():
        raise FileNotFoundError(source_path)
    if not CHROME.is_file():
        raise FileNotFoundError(CHROME)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_path = output_path.with_suffix(".render.html")
    body = markdown.markdown(
        source_path.read_text(encoding="utf-8"),
        extensions=["extra", "tables", "fenced_code", "sane_lists"],
    )
    html_path.write_text(
        "<!doctype html><html lang=\"hi\"><head><meta charset=\"utf-8\">"
        f"<style>{CSS}</style></head><body>{body}</body></html>",
        encoding="utf-8",
    )
    try:
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
    finally:
        if html_path.is_file():
            html_path.unlink()
    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise RuntimeError(f"Chromium did not create {output_path}")
    return output_path
