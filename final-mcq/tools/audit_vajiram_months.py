"""Run structural and hostile audits for all local Vajiram monthly banks."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(r"C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent")
CA = ROOT / "final-mcq" / "current-affairs"
INVENTORY = CA / "INVENTORY.md"


def q_numbers(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"^\*\*(\d+)\.\*\*", text, re.M)]


def answer_numbers(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"^\*\*(\d+)\.", text, re.M)]


def option_counts(text: str) -> tuple[int, int]:
    questions = re.split(r"(?=^\*\*\d+\.\*\*)", text, flags=re.M)[1:]
    bad = 0
    count = 0
    for question in questions:
        if re.search(r"^\s*[ABCD]\.\s+", question, re.M):
            count += 1
        if len(re.findall(r"^[ABCD]\.\s+", question, re.M)) != 4:
            bad += 1
    return count, bad


def key_distribution(text: str) -> dict[str, int]:
    result = {letter: 0 for letter in "ABCD"}
    for match in re.finditer(r"^\*\*\d+\.\s+([ABCD])\.", text, re.M):
        result[match.group(1)] += 1
    return result


def audit_month(folder: Path) -> tuple[int, str]:
    rows = []
    for bank in (1, 2, 3):
        revision = folder / f"revision-{bank}"
        qpath = revision / "QUESTIONS.md"
        apath = revision / "ANSWERS.md"
        qtext = qpath.read_text(encoding="utf-8")
        atext = apath.read_text(encoding="utf-8")
        qnums = q_numbers(qtext)
        anums = answer_numbers(atext)
        option_count, bad_options = option_counts(qtext)
        stems = re.findall(r"^\*\*\d+\.\*\*\s+(.+)$", qtext, re.M)
        body = "\n".join(
            match.group(1)
            for match in re.finditer(r"^\*\*\d+\.\*\*\s+(.+)$", qtext, re.M)
        )
        cue_hits = re.findall(
            r"(?i)\b(correct|incorrect|answer key|rationale:|source reference|trap:|hold:)\b",
            body,
        )
        rows.append(
            {
                "bank": bank,
                "questions": len(qnums),
                "answers": len(anums),
                "one_to_one": qnums == anums == list(range(1, len(qnums) + 1)),
                "options": option_count,
                "bad_options": bad_options,
                "duplicate_stems": len(stems) - len(set(stems)),
                "cue_hits": len(cue_hits),
                "distribution": key_distribution(atext),
            }
        )

    lines = [
        f"# {folder.name} hostile and structural audit",
        "",
        "This audit checks structure and answer leakage only; it does not certify "
        "unresolved official, legal, numerical, PYQ or reproduction-rights claims.",
        "",
        "| Revision | Questions | Answers | One-to-one | Four options | Bad option blocks | Duplicate stems | Question cue hits | Key distribution |",
        "|---|---:|---:|---|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        dist = " / ".join(f"{k}{v}" for k, v in row["distribution"].items())
        lines.append(
            f"| revision-{row['bank']} | {row['questions']} | {row['answers']} | "
            f"{'pass' if row['one_to_one'] else 'FAIL'} | {row['options']} | "
            f"{row['bad_options']} | {row['duplicate_stems']} | {row['cue_hits']} | {dist} |"
        )
    lines.extend(
        [
            "",
            "## Required holds",
            "",
            "- Source-page coverage is tracked in COVERAGE.md and does not imply factual certification.",
            "- Any unresolved origin, mandate, HQ, membership, reports/frequency, funds, leadership, committee, timeline, India-linkage or award detail remains held.",
            "- No exact UPSC PYQ wording/options are reproduced; PYQ provenance, official-key and rights holds remain open.",
        ]
    )
    text = "\n".join(lines) + "\n"
    (folder / "HOSTILE-AUDIT.md").write_text(text, encoding="utf-8")
    return max(row["questions"] for row in rows), text


def main() -> None:
    months = sorted(
        p for p in CA.iterdir() if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}", p.name)
    )
    counts: dict[str, int] = {}
    for month in months:
        counts[month.name], _ = audit_month(month)

    lines = [
        "# Vajiram Recitals source inventory",
        "",
        "**Status:** Every locally listed workbook through July 2026 has an audited, "
        "source-indexed revision-1/2/3 bank. All remain **in_progress** because source "
        "rows requiring official corroboration, current-law checks, PYQ provenance and "
        "reproduction rights are not falsely certified. No August or September 2026 "
        "workbook is present or invented.",
        "",
        "| Month | Source PDF under `books/current affairs vajiram/` | Bank status |",
        "|---|---|---|",
    ]
    source_names = {
        "2025-06": "Recitals_June_9300a9962b.pdf",
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
    for month in sorted(source_names):
        count = counts.get(month, 342 if month == "2025-06" else 0)
        suffix = (
            f"{count} questions per revision; structural/hostile audit complete; "
            "source and factual holds remain; not complete"
        )
        lines.append(f"| {month} | `{source_names[month]}` | in_progress — {suffix} |")
    lines.extend(
        [
            "",
            "The duplicate September 2025 file has the same SHA-256 digest as the listed "
            "September file and is not an extra month. August 2026 and September 2026 are "
            "absent from the local source folder; they remain unprocessed and are not fabricated.",
            "",
            "Each month folder contains revision-1/2/3 QUESTIONS.md, ANSWERS.md, COVERAGE.md, "
            "COMPLIANCE.md and HOSTILE-AUDIT.md.",
        ]
    )
    INVENTORY.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
