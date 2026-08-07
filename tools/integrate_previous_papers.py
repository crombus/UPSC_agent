"""Export the locally held 2018-2023 UPSC papers without using Qdrant.

The generated Markdown/JSON exports are provenance copies for search and
routing. They do not contain answer keys or inferred answers.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "books" / "more_previous_papers"
TEXT_DIR = ROOT / "attempts" / "_pyq_text"
EXPORT_ROOT = ROOT / "knowledge-export"
CATALOG_JSON = EXPORT_ROOT / "_catalog.json"
CATALOG_MD = EXPORT_ROOT / "_catalog.md"


@dataclass(frozen=True)
class Paper:
    year: int
    paper_type: str
    subject: str
    filename: str

    @property
    def source_path(self) -> str:
        return f"books/more_previous_papers/{self.filename}"

    @property
    def export_folder(self) -> str:
        return {
            "Prelims GS-I": "Prelims PYQ",
            "CSAT": "CSAT PYQ",
        }.get(self.paper_type, "Mains PYQ")


PAPERS = [
    Paper(2018, "Prelims GS-I", "Prelims", "QP-CSP-18-GS-I-C.pdf"),
    Paper(2018, "CSAT", "CSAT", "QP-CSP-18-GS-II-C.pdf"),
    Paper(2019, "Prelims GS-I", "Prelims", "csp-p1.pdf"),
    Paper(2019, "CSAT", "CSAT", "csp-p2.pdf"),
    Paper(2020, "Prelims GS-I", "Prelims", "CSP_2020_GS_Paper-1.pdf"),
    Paper(2020, "CSAT", "CSAT", "CSP_2020_GS_Paper-2.pdf"),
    Paper(2021, "Prelims GS-I", "Prelims", "QP-CSP-21-GeneralStudiesPaper-I-121021.pdf"),
    Paper(2021, "CSAT", "CSAT", "QP-CSP-21-GeneralStudiesPaper-II-121021.pdf"),
    Paper(2022, "Prelims GS-I", "Prelims", "GENERAL STUDIES PAPER I.pdf"),
    Paper(2022, "CSAT", "CSAT", "GENERAL STUDIES PAPER II.pdf"),
    Paper(2023, "Prelims GS-I", "Prelims", "QP_CS_Pre_Exam_2023_280523.pdf"),
    Paper(2023, "CSAT", "CSAT", "QP_CS_Pre_Exam_2023_GENERAL_STUDIES_PAPER_II_280523.pdf"),
    Paper(2018, "Mains GS-I", "Mains", "GENERAL-STUDIES-PAPER-I.pdf"),
    Paper(2018, "Mains GS-II", "Mains", "GENERAL-STUDIES-PAPER-II.pdf"),
    Paper(2018, "Mains GS-III", "Mains", "GENERAL-STUDIES-PAPER-III.pdf"),
    Paper(2018, "Mains GS-IV", "Mains", "GENERAL-STUDIES-PAPER-IV.pdf"),
    Paper(2018, "Mains Essay", "Mains", "ESSAY_0.pdf"),
    Paper(2019, "Mains GS-I", "Mains", "QP-CSM19-GeneralStudies-I.pdf"),
    Paper(2019, "Mains GS-II", "Mains", "QP-CSM19-GeneralStudies-II.pdf"),
    Paper(2019, "Mains GS-III", "Mains", "QP-CSM19-GeneralStudies-III.pdf"),
    Paper(2019, "Mains GS-IV", "Mains", "QP-CSM19-GeneralStudies-IV.pdf"),
    Paper(2019, "Mains Essay", "Mains", "QP-CSM19-Essay.pdf"),
    Paper(2020, "Mains GS-I", "Mains", "Gen_St_P1.pdf"),
    Paper(2020, "Mains GS-II", "Mains", "Gen_St_P2.pdf"),
    Paper(2020, "Mains GS-III", "Mains", "Gen_St_P3.pdf"),
    Paper(2020, "Mains GS-IV", "Mains", "Gen_St_P4.pdf"),
    Paper(2020, "Mains Essay", "Mains", "ESSAY_1.pdf"),
    Paper(2021, "Mains GS-I", "Mains", "QP-CSM-21-GENSTUDIESPAPER-I-110122.pdf"),
    Paper(2021, "Mains GS-II", "Mains", "QP-CSM-21-GENSTUDIESPAPER-II-110122.pdf"),
    Paper(2021, "Mains GS-III", "Mains", "QP-CSM-21-GENSTUDIESPAPER-III-110122.pdf"),
    Paper(2021, "Mains GS-IV", "Mains", "QP-CSM-21-GENSTUDIESPAPER-IV-110122.pdf"),
    Paper(2021, "Mains Essay", "Mains", "QP-CSM-21-ESSAY-110122.pdf"),
    Paper(2022, "Mains GS-I", "Mains", "QP-CSM-22-GENERAL-STUDIES-PAPER I-190922.pdf"),
    Paper(2022, "Mains GS-II", "Mains", "QP-CSM-22-GENERAL-STUDIES-PAPER-II-190922.pdf"),
    Paper(2022, "Mains GS-III", "Mains", "QP-CSM-22-GENERAL-STUDIES-PAPER-III-190922.pdf"),
    Paper(2022, "Mains GS-IV", "Mains", "QP-CSM-22-GENERAL-STUDIES-PAPER IV-190922.pdf"),
    Paper(2022, "Mains Essay", "Mains", "QP-CSM-22-ESSAY-190922.pdf"),
    Paper(2023, "Mains GS-I", "Mains", "QP-CSM-23-GENERAL-STUDIES-PAPER-I-180923.pdf"),
    Paper(2023, "Mains GS-II", "Mains", "QP-CSM-23-GENERAL-STUDIES-PAPER-II-180923.pdf"),
    Paper(2023, "Mains GS-III", "Mains", "QP-CSM-23-GENERAL-STUDIES-PAPER-III-180923.pdf"),
    Paper(2023, "Mains GS-IV", "Mains", "QP-CSM-23-GENERAL-STUDIES-PAPER-IV-180923.pdf"),
    Paper(2023, "Mains Essay", "Mains", "QP-CSM-23-ESSAY-180923.pdf"),
]


def extract_pages(path: Path) -> list[dict[str, object]]:
    document = fitz.open(path)
    try:
        return [
            {
                "page": index + 1,
                "text": re.sub(r"[ \t]+\n", "\n", page.get_text("text")).strip(),
            }
            for index, page in enumerate(document)
        ]
    finally:
        document.close()


def write_exports(paper: Paper, pages: list[dict[str, object]]) -> dict[str, object]:
    text = "\n\n".join(
        f"===== PAGE {page['page']} =====\n{page['text']}" for page in pages
    ).strip()
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    (TEXT_DIR / f"{paper.filename}.txt").write_text(text + "\n", encoding="utf-8")

    export_dir = EXPORT_ROOT / paper.export_folder
    export_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": paper.filename,
        "source_path": paper.source_path,
        "year": paper.year,
        "paper_type": paper.paper_type,
        "subject": paper.subject,
        "provenance": "Direct local PDF extraction; no Qdrant retrieval",
        "answer_key_status": (
            "Not supplied locally; no answers inferred"
            if paper.paper_type in {"Prelims GS-I", "CSAT"}
            else "Not applicable"
        ),
        "page_count": len(pages),
        "char_count": len(text),
        "pages": pages,
    }
    json_path = export_dir / f"{paper.filename}.json"
    json_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    key_note = (
        "\n> **Answer-key status:** Not supplied locally; no answers are inferred.\n"
        if paper.paper_type in {"Prelims GS-I", "CSAT"}
        else ""
    )
    markdown = (
        f"# {paper.year} {paper.paper_type}\n\n"
        f"> **Official local source:** `{paper.source_path}`\n"
        f"> **Provenance:** Direct extraction from the searchable local PDF; Qdrant was not used.\n"
        f"{key_note}\n"
        f"## Extracted paper text\n\n{text}\n"
    )
    (export_dir / f"{paper.filename}.md").write_text(markdown, encoding="utf-8")

    return {
        "source": paper.filename,
        "source_path": paper.source_path,
        "book_title": f"{paper.year} {paper.paper_type}",
        "subject": paper.subject,
        "chunks_stored": len(pages),
        "total_chunks": len(pages),
        "char_count": len(text),
        "provenance": "direct-local-pdf",
        "answer_key_status": payload["answer_key_status"],
    }


def update_catalog(new_entries: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    catalog_is_list = isinstance(catalog, list)
    books = catalog if catalog_is_list else catalog.get("books", [])
    source_paths = {entry["source_path"] for entry in new_entries}
    books = [book for book in books if book.get("source_path") not in source_paths]
    books.extend(new_entries)
    books.sort(key=lambda item: (str(item.get("subject")), str(item.get("book_title"))))
    total_chunks = sum(int(book.get("chunks_stored", 0)) for book in books)
    if not catalog_is_list:
        catalog["books"] = books
        catalog["total_books"] = len(books)
        catalog["total_chunks"] = total_chunks
    output_catalog = books if catalog_is_list else catalog
    CATALOG_JSON.write_text(
        json.dumps(output_catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    rows = [
        "# Knowledge Export Catalog",
        "",
        f"- **Sources:** {len(books)}",
        f"- **Stored chunks/pages:** {total_chunks}",
        "",
        "| Source title | Subject | Provenance | Local source |",
        "|---|---|---|---|",
    ]
    for book in books:
        rows.append(
            f"| {book.get('book_title', book.get('source', ''))} "
            f"| {book.get('subject', '')} "
            f"| {book.get('provenance', 'legacy export')} "
            f"| `{book.get('source_path', book.get('source', ''))}` |"
        )
    CATALOG_MD.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> None:
    missing = [paper.filename for paper in PAPERS if not (SOURCE_DIR / paper.filename).is_file()]
    if missing:
        raise FileNotFoundError("Missing source papers:\n" + "\n".join(missing))

    entries = []
    for paper in PAPERS:
        pages = extract_pages(SOURCE_DIR / paper.filename)
        if not any(str(page["text"]).strip() for page in pages):
            raise ValueError(f"No searchable text found in {paper.filename}")
        entries.append(write_exports(paper, pages))
        print(f"{paper.year} {paper.paper_type}: {paper.filename} ({len(pages)} pages)")

    update_catalog(entries)
    print(f"Integrated {len(entries)} papers into direct local exports.")


if __name__ == "__main__":
    main()
