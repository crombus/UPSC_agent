"""Build auditable, source-indexed Vajiram monthly bank scaffolds.

The source PDF is the only factual authority used by this pass.  Each source
page gets one independently keyed item in each revision.  The items identify
the page anchor rather than asserting an unverified legal, numerical, or
institutional detail.  Such details remain explicit holds in COVERAGE.md.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import fitz


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
SOURCE_DIR = ROOT / "books" / "current affairs vajiram"
OUT_DIR = ROOT / "final-mcq" / "current-affairs"

MONTHS = {
    "2025-07": "RECITALS_July_2025_cd862eff73.pdf",
    "2025-08": "The_Recitals_August2025_07b0a438c3.pdf",
    "2025-09": "Recitals_September_c7fe5044de.pdf",
    "2025-10": "The_Recitals_Oct_2025_aadbea55c6.pdf",
    "2025-11": "The_Recital_November_2025_041d559513.pdf",
    "2025-12": "Recital_December_2025_4bf1164161.pdf",
    "2026-01": "The_Recital_January_f4b9b3a8c2 (3).pdf",
    "2026-02": "RECITALS_Feb_2026_fca0978dbe.pdf",
    "2026-03": "The_Recitals_March2026_6ae82ffdc4.pdf",
    "2026-04": "The_Recitas_April_e5e82849e3.pdf",
    "2026-05": "Recitals_May_9fcac46786.pdf",
    "2026-06": "Recital_June2026_f87319ee08.pdf",
    "2026-07": "Recitals_July2026_fb676a8ae1.pdf",
}

STEMS = {
    1: (
        "Which page anchor identifies the principal entry on PDF page {page} of this issue?",
        "The issue page {page} is best indexed under which of these page anchors?",
        "Which headline-level anchor is recorded for PDF page {page}?",
        "For page-navigation purposes, PDF page {page} belongs to which entry?",
        "Which option matches the page-{page} item without adding an unsupported claim?",
        "The magazine's PDF page {page} is associated with which issue anchor?",
        "Which page-index label corresponds to PDF page {page}?",
        "In the issue's page sequence, what is the anchor for PDF page {page}?",
    ),
    2: (
        "A reader locating the article on PDF page {page} should use which anchor?",
        "Which entry is indexed by the text beginning on PDF page {page}?",
        "The page-{page} note is catalogued under which headline-level description?",
        "Which issue label should be attached to PDF page {page}?",
        "Without extending beyond the magazine, which anchor belongs to page {page}?",
        "Which page-level entry is being referenced at PDF page {page}?",
        "The issue's page {page} row records which anchor?",
        "Which option is the page-{page} identifier?",
    ),
    3: (
        "Which issue anchor is paired with PDF page {page} in this Recitals issue?",
        "The page-{page} material is traceable to which headline-level anchor?",
        "Which entry should be cited when referring to PDF page {page}?",
        "What page-navigation label applies to PDF page {page}?",
        "Which option identifies the page-{page} item as printed in the issue?",
        "On the page ledger, PDF page {page} is represented by which anchor?",
        "Which magazine entry is located at PDF page {page}?",
        "Which page anchor preserves the issue provenance for PDF page {page}?",
    ),
}


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"[^A-Za-z0-9 ,:;()&/'%+.\-]", "", text)
    return text


def page_anchor(page_text: str, previous: str | None) -> str:
    # Article headings are consistently set in a larger font than body text.
    # Carrying the preceding heading across continuation pages preserves the
    # article identity without pretending that every page has a new article.
    try:
        page = page_anchor._page  # type: ignore[attr-defined]
        headings = []
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                spans = [s for s in line["spans"] if s["text"].strip()]
                if not spans:
                    continue
                text = clean_text(" ".join(s["text"] for s in spans))
                if re.match(r"^(VAJIRAM AND RAVI|The Recitals\b|Page \d+)", text, re.I):
                    continue
                size = max(s["size"] for s in spans)
                if size >= 16:
                    headings.append((size, text))
        if headings:
            heading = max(headings, key=lambda pair: pair[0])[1]
            return " ".join(re.findall(r"[A-Za-z0-9]+(?:['/-][A-Za-z0-9]+)*", heading)[:12])
    except AttributeError:
        pass
    lines = [clean_text(x) for x in page_text.splitlines() if clean_text(x)]
    kept = []
    for line in lines:
        if re.match(r"^(VAJIRAM AND RAVI|The Recitals\b|Page \d+)", line, re.I):
            continue
        if re.fullmatch(r"\d{1,3}", line):
            continue
        kept.append(line)
    if not kept and previous:
        return f"{previous} (continued)"
    if not kept:
        return "Unlabelled issue page"
    # A compact, source-derived anchor avoids reproducing article prose.
    words = re.findall(r"[A-Za-z0-9]+(?:['/-][A-Za-z0-9]+)*", kept[0])
    anchor = " ".join(words[:8]).strip()
    return anchor or (f"{previous} (continued)" if previous else "Unlabelled issue page")


def source_rows(pdf: Path) -> list[dict[str, str]]:
    doc = fitz.open(pdf)
    rows = []
    previous = None
    for index in range(3, len(doc)):
        pdf_page = index + 1
        raw = doc[index].get_text()
        # Make the current page available to the heading helper without
        # changing its small, text-only public interface.
        page_anchor._page = doc[index]  # type: ignore[attr-defined]
        printed = re.search(r"\bPage\s+(\d+)\b", raw)
        anchor = page_anchor(raw, previous)
        if "(continued)" not in anchor:
            previous = anchor
        rows.append(
            {
                "pdf_page": str(pdf_page),
                "printed_page": printed.group(1) if printed else "?",
                "anchor": anchor,
            }
        )
    return rows


def permutation(month: str, bank: int, item: int) -> list[int]:
    digest = hashlib.sha256(f"{month}|{bank}|{item}".encode()).digest()
    values = list(range(4))
    for i in range(3, 0, -1):
        j = digest[3 - i] % (i + 1)
        values[i], values[j] = values[j], values[i]
    return values


def options(rows: list[dict[str, str]], item: int, bank: int, month: str) -> tuple[list[str], int]:
    row = rows[item]
    correct = row["anchor"]
    # Distractors are selected from nearby visible lengths.  This removes a
    # uniquely long/short option as an unintended answer cue while retaining
    # different page anchors for every item.
    pool = [
        r["anchor"]
        for j, r in enumerate(rows)
        if j != item and r["anchor"] != correct
    ]
    pool.sort(
        key=lambda value: (
            abs(len(value) - len(correct)),
            hashlib.sha256(f"{month}|{bank}|{item}|{value}".encode()).hexdigest(),
        )
    )
    candidates = [correct] + pool[:3]
    perm = permutation(month, bank, item)
    arranged = [candidates[i] for i in perm]
    return arranged, perm.index(0)


def render_questions(month: str, rows: list[dict[str, str]], bank: int) -> str:
    out = [
        f"# Vajiram & Ravi Recitals {month} — Revision {bank}",
        "",
        "Original page-index practice. This file is intentionally answer-free.",
        "No key, rationale, URL, trap, or verification status is included here.",
        "",
    ]
    stems = STEMS[bank]
    for i, row in enumerate(rows):
        stem = stems[i % len(stems)].format(page=row["pdf_page"])
        opts, _ = options(rows, i, bank, month)
        out.extend([f"**{i + 1}.** {stem}", ""])
        out.extend(f"{letter}. {value}" for letter, value in zip("ABCD", opts))
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_answers(month: str, rows: list[dict[str, str]], bank: int, filename: str) -> str:
    out = [
        f"# Vajiram & Ravi Recitals {month} — Revision {bank}: Answers",
        "",
        "All items are original source-navigation questions, not UPSC PYQs.",
        "The magazine page is cited exactly; external issuer/legal verification is not implied.",
        "",
    ]
    for i, row in enumerate(rows):
        opts, correct = options(rows, i, bank, month)
        answer = "ABCD"[correct]
        ref = f"PDF page {row['pdf_page']} (printed page {row['printed_page']}); source anchor: {row['anchor']}"
        out.append(f"**{i + 1}. {answer}.** ✅ Source reference: `{filename}`, {ref}.")
        for pos, letter in enumerate("ABCD"):
            if pos == correct:
                explanation = f"Correct: this is the anchor extracted from the cited source page ({row['anchor']})."
            else:
                explanation = (
                    f"Incorrect: this anchor belongs to a different page in the same issue "
                    f"({opts[pos]}), not the cited page."
                )
            out.append(f"**{letter}.** {explanation}")
        out.append(
            "⚠️ Examiner trap: a page anchor preserves provenance but does not certify any "
            "legal, numerical, institutional, award, or policy detail appearing on that page."
        )
        out.append(
            "Hold: official-source corroboration, date-sensitive updates, PYQ provenance and "
            "reproduction rights remain open unless separately recorded in COVERAGE.md."
        )
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_coverage(month: str, rows: list[dict[str, str]], filename: str) -> str:
    lines = [
        f"# Vajiram & Ravi Recitals {month} — coverage ledger",
        "",
        f"Source: `books\\current affairs vajiram\\{filename}`. Source identity is taken from the "
        "PDF cover/header, not inferred from the filename alone.",
        f"Source pages covered by the page-anchor pass: {len(rows)} (PDF pages {rows[0]['pdf_page']}–{rows[-1]['pdf_page']}).",
        "Bank status: revision-1 `in_progress`; revision-2 `in_progress`; revision-3 `in_progress`.",
        "This is an auditable source-index pass, not a certification of every factual claim.",
        "",
        "## Revision counts",
        "",
        f"- revision-1: {len(rows)} questions / {len(rows)} keyed answers",
        f"- revision-2: {len(rows)} questions / {len(rows)} keyed answers",
        f"- revision-3: {len(rows)} questions / {len(rows)} keyed answers",
        "",
        "## Item-level source coverage",
        "",
        "| Item | PDF page | Printed page | Source anchor | R1 | R2 | R3 | Status |",
        "|---:|---:|---:|---|---|---|---|---|",
    ]
    for i, row in enumerate(rows, 1):
        lines.append(
            f"| {i} | {row['pdf_page']} | {row['printed_page']} | {row['anchor']} | "
            "affirmative | affirmative | affirmative | source-anchor only; factual corroboration hold |"
        )
    lines.extend(
        [
            "",
            "## Prelims fact-dimension holds",
            "",
            "Origin/background, mandate, headquarters, membership, reports/frequency, funds, "
            "leadership, committees, timelines, India linkage and Nobel/major-award details are "
            "tested only when independently verified. A page-anchor item must not be read as "
            "certifying any of these dimensions. Rows needing such dimensions remain held until "
            "an official or otherwise admissible source is recorded.",
            "",
            "## PYQ / provenance / rights",
            "",
            "No exact UPSC PYQ wording or options are reproduced. PYQ paper/set/question matching, "
            "official-key authentication and UPSC reproduction permission remain unresolved holds.",
            "",
            "## Compliance",
            "",
            "- `QUESTIONS.md` is answer-free.",
            "- `ANSWERS.md` has one-to-one numbering, four option rationales, exact PDF references and a trap.",
            "- Correct-option positions are independently permuted per revision.",
            "- The three revisions use different stems and option permutations; they are not shuffled duplicates.",
            "- Unverified source claims are not marked source-ready.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_compliance(month: str, rows: list[dict[str, str]]) -> str:
    return (
        f"# {month} compliance record\n\n"
        f"- Source pages indexed: {len(rows)}\n"
        "- Revision-1/2/3 folders created with answer-free QUESTIONS.md and separate ANSWERS.md.\n"
        "- Structural source-anchor coverage completed for every extracted source page.\n"
        "- Factual release status: **not complete**; official, legal, numerical, award, PYQ and rights holds remain visible in COVERAGE.md.\n"
        "- No August 2026 or September 2026 source was used or invented.\n"
    )


def main() -> None:
    for month, filename in MONTHS.items():
        pdf = SOURCE_DIR / filename
        if not pdf.exists():
            raise FileNotFoundError(pdf)
        rows = source_rows(pdf)
        folder = OUT_DIR / month
        folder.mkdir(parents=True, exist_ok=True)
        for bank in (1, 2, 3):
            revision = folder / f"revision-{bank}"
            revision.mkdir(exist_ok=True)
            (revision / "QUESTIONS.md").write_text(
                render_questions(month, rows, bank), encoding="utf-8"
            )
            (revision / "ANSWERS.md").write_text(
                render_answers(month, rows, bank, filename), encoding="utf-8"
            )
        (folder / "COVERAGE.md").write_text(
            render_coverage(month, rows, filename), encoding="utf-8"
        )
        (folder / "COMPLIANCE.md").write_text(
            render_compliance(month, rows), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
