"""Propagate the audited 2024-2025 UPSC PYQ routes into topic owners.

This is the recent-cycle sibling of `propagate_historical_pyqs.py`. It reads the four
2024-2025 routing ledgers and inserts a *separate* generated block, delimited by its own
2024-2025 markers, into every routed owner - without touching the existing 2018-2023 block.

Idempotence and stale-route safety: on every run it first strips the 2024-2025 block from
*all* Basic/Advanced owner files, then re-appends a fresh block only to currently-routed
owners. An owner that loses all its 2024-2025 routes therefore loses its recent block too.
Prelims/CSAT answers are never inferred; the accurate key status is carried from the ledger.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
AUDIT_PATH = KNOWLEDGE / "PYQ-INTEGRATION-AUDIT-2024-2025.md"

BEGIN = "<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->"
END = "<!-- END GENERATED PYQ INTEGRATION: 2024-2025 -->"

# The historical propagator re-appends its 2018-2023 block at end-of-file. To make the two
# propagators mutually stable regardless of run order, the 2024-2025 block is inserted
# immediately BEFORE the 2018-2023 block when one exists, otherwise appended at end.
HIST_BEGIN = "<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->"

LEDGERS = (
    ("Prelims GS-I", KNOWLEDGE / "_PYQ-ROUTING-PRELIMS-2024-2025.md"),
    ("CSAT", KNOWLEDGE / "_PYQ-ROUTING-CSAT-2024-2025.md"),
    (
        "Mains GS-I/GS-II/Essay",
        KNOWLEDGE / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
    ),
    (
        "Mains GS-III/GS-IV",
        KNOWLEDGE / "_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md",
    ),
)

EXPECTED = {
    "Prelims GS-I": 200,
    "CSAT": 160,
    "GS-I": 40,
    "GS-II": 40,
    "GS-III": 40,
    "GS-IV": 24,
    "Essay": 16,
}

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
YEAR_RE = re.compile(r"^20(?:24|25)$")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]{3,}")

STOP_WORDS = {
    "about", "after", "against", "among", "between", "could", "from", "have",
    "india", "indian", "into", "their", "there", "these", "through", "under",
    "versus", "what", "when", "where", "which", "while", "with", "would",
}


@dataclass(frozen=True)
class Entry:
    ledger_label: str
    ledger_name: str
    year: int
    paper: str
    question: str
    theme: str
    family: str
    directive: str
    note: str
    target: Path

    @property
    def question_key(self) -> tuple[str, int, str]:
        return (self.paper, self.year, self.question)


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def question_number(value: str) -> int:
    """Extract a sortable integer from a question label (handles Essay 'Section A - 1')."""
    match = re.search(r"(\d+)", value)
    return int(match.group(1)) if match else 0


def parse_ledger(label: str, path: Path) -> list[Entry]:
    entries: list[Entry] = []
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not line.startswith("|"):
            continue
        cells = split_row(line)
        if not cells or not YEAR_RE.fullmatch(cells[0]):
            continue
        if not LINK_RE.search(line):
            continue

        if label in ("Prelims GS-I", "CSAT"):
            if len(cells) != 6:
                raise ValueError(f"{path.name}:{line_number}: expected 6 cells, got {len(cells)}")
            year, question, theme, family, routes, note = cells
            paper = label if label == "CSAT" else "Prelims GS-I"
            directive = "Objective question; official Set-A key available locally, answer not inferred"
        else:
            if len(cells) != 8:
                raise ValueError(f"{path.name}:{line_number}: expected 8 cells, got {len(cells)}")
            year, paper, question, theme, family, directive, routes, note = cells

        targets = LINK_RE.findall(routes)
        if not targets:
            raise ValueError(f"{path.name}:{line_number}: no route target")
        for target_text in targets:
            target = (KNOWLEDGE / target_text).resolve()
            try:
                target.relative_to(KNOWLEDGE.resolve())
            except ValueError as exc:
                raise ValueError(
                    f"{path.name}:{line_number}: route escapes knowledge root: {target_text}"
                ) from exc
            entries.append(
                Entry(
                    ledger_label=label,
                    ledger_name=path.name,
                    year=int(year),
                    paper=paper,
                    question=question,
                    theme=theme,
                    family=family,
                    directive=directive,
                    note=note,
                    target=target,
                )
            )
    return entries


def strip_generated(text: str) -> str:
    begin_count = text.count(BEGIN)
    end_count = text.count(END)
    if begin_count != end_count or begin_count > 1:
        raise ValueError(
            f"Malformed generated markers: begin={begin_count}, end={end_count}"
        )
    if begin_count == 0:
        return text
    pattern = re.compile(
        rf"\n*{re.escape(BEGIN)}.*?{re.escape(END)}\n*",
        flags=re.DOTALL,
    )
    return pattern.sub("\n", text).rstrip() + "\n"


def normalize_generated_spacing(text: str) -> str:
    """Keep exactly one blank line between adjacent generated cycle blocks."""
    return re.sub(
        r"(<!-- END GENERATED PYQ INTEGRATION: [^>]+ -->)\n+"
        r"(<!-- BEGIN GENERATED PYQ INTEGRATION: [^>]+ -->)",
        r"\1\n\n\2",
        text,
    )


def markdown_safe(text: str) -> str:
    return text.replace("|", r"\|").replace("\n", " ").strip()


def owner_requirement(entry: Entry) -> str:
    if entry.paper == "Prelims GS-I":
        return "Cover the named fact/concept and its likely statement-level distinctions."
    if entry.paper == "CSAT":
        return "Practise this exact skill form under timed elimination; no answer is inferred here."
    if entry.paper == "Essay":
        return "Use as a brainstorming/theme test; this owner supplies essay method, not a model essay."
    if entry.paper == "GS-IV" and "case" in entry.theme.lower():
        return "Apply stakeholders, dilemmas, options, justification, implementation and safeguards."
    return "Prepare context, core dimensions, evidence/examples, counterpoint and a concise conclusion."


def render_block(entries: list[Entry]) -> str:
    entries = sorted(
        entries,
        key=lambda item: (item.year, item.paper, question_number(item.question), item.theme),
    )
    sources = sorted({entry.ledger_name for entry in entries})
    objective = any(entry.paper in {"Prelims GS-I", "CSAT"} for entry in entries)
    years = sorted({entry.year for entry in entries})
    papers = sorted({entry.paper for entry in entries})

    rows = [
        "",
        BEGIN,
        "## Recent PYQ Integration (2024-2025)",
        "",
        "> **Status:** 2024-2025 question-level PYQ demand is integrated into this owner.",
        "> **Provenance:** Audited local official-paper routing ledgers: "
        + ", ".join(f"`{source}`" for source in sources)
        + ".",
    ]
    if objective:
        rows.append(
            "> **Answer-key rule:** The official 2024-2025 Prelims Set-A keys are present in the "
            "repository and CSAT Set-A keys are supplied; even so, no option or answer is recorded "
            "or inferred in this integration."
        )
    rows.extend(
        [
            "",
            f"- **Years represented:** {', '.join(map(str, years))}",
            f"- **Paper(s):** {', '.join(papers)}",
            f"- **Routed question demands:** {len(entries)}",
            "",
            "| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format "
            "| Source status | Owner requirement |",
            "|---:|---|---|---|---|---|---|",
        ]
    )
    for entry in entries:
        rows.append(
            f"| {entry.year} | {markdown_safe(entry.paper)} | {markdown_safe(entry.question)} "
            f"| {markdown_safe(entry.theme)} | {markdown_safe(entry.directive)} "
            f"| {markdown_safe(entry.note)} "
            f"| {markdown_safe(owner_requirement(entry))} |"
        )

    unique_themes = []
    seen = set()
    for entry in entries:
        key = entry.theme.casefold()
        if key not in seen:
            seen.add(key)
            unique_themes.append(entry.theme)
    rows.extend(["", "### What this owner must now support", ""])
    rows.extend(f"- {theme}" for theme in unique_themes)
    rows.extend(
        [
            "",
            "> This block integrates the 2024-2025 examinable demand and paper metadata. It is kept "
            "separate from the 2018-2023 block and does not convert an unkeyed/answer-free objective "
            "question into a solved answer.",
            END,
            "",
        ]
    )
    return "\n".join(rows)


def theme_tokens(theme: str) -> set[str]:
    return {
        token.casefold()
        for token in WORD_RE.findall(theme)
        if token.casefold() not in STOP_WORDS
    }


def lexical_signal(theme: str, source_text: str) -> tuple[bool, str]:
    tokens = theme_tokens(theme)
    if not tokens:
        return True, "no discriminating tokens"
    source_words = {token.casefold() for token in WORD_RE.findall(source_text)}
    matched = sorted(tokens & source_words)
    ratio = len(matched) / len(tokens)
    adequate = len(matched) >= min(2, len(tokens)) or ratio >= 0.4
    detail = f"{len(matched)}/{len(tokens)} tokens"
    return adequate, detail


def topic_files(subject_dir: Path) -> list[Path]:
    files: list[Path] = []
    for tier in ("basic", "advanced"):
        tier_dir = subject_dir / tier
        if tier_dir.is_dir():
            files.extend(
                path for path in tier_dir.glob("*.md") if not path.name.startswith("_")
            )
    return sorted(files)


def all_owner_files() -> list[Path]:
    files: list[Path] = []
    for subject in KNOWLEDGE.iterdir():
        if subject.is_dir() and ((subject / "basic").is_dir() or (subject / "advanced").is_dir()):
            files.extend(topic_files(subject))
    return sorted(files)


def display_path(path: Path) -> str:
    return path.relative_to(KNOWLEDGE).as_posix()


def write_audit(
    entries: list[Entry],
    original_text: dict[Path, str],
    missing_targets: list[Path],
) -> None:
    by_target: dict[Path, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_target[entry.target].append(entry)

    subjects = sorted(
        {path.relative_to(KNOWLEDGE).parts[0] for path in by_target}
        | {
            path.name
            for path in KNOWLEDGE.iterdir()
            if path.is_dir() and ((path / "basic").is_dir() or (path / "advanced").is_dir())
        }
    )

    low_signal: dict[str, list[tuple[Entry, str]]] = defaultdict(list)
    manual: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        subject = entry.target.relative_to(KNOWLEDGE).parts[0]
        if entry.paper == "Essay":
            continue
        adequate, detail = lexical_signal(entry.theme, original_text.get(entry.target, ""))
        if not adequate:
            low_signal[subject].append((entry, detail))
        if "ocr-uncertain" in entry.note.casefold() or "manual verification needed" in entry.note.casefold():
            manual[subject].append(entry)

    unique_questions = {entry.question_key for entry in entries}
    owners = all_owner_files()
    unrouted_owner_files = [path for path in owners if path not in by_target]
    manual_questions = {entry.question_key for items in manual.values() for entry in items}

    lines = [
        "# RECENT PYQ INTEGRATION AUDIT, 2024-2025",
        "",
        "> Generated by `tools/propagate_recent_pyqs.py` from the four audited 2024-2025 routing "
        "ledgers. Counts distinguish unique printed questions from route assignments, because "
        "cross-cutting questions and all CSAT questions may have more than one owner. This audit "
        "is separate from the 2018-2023 audit and does not alter it.",
        "",
        "## 1. Reconciliation",
        "",
        f"- **Unique printed questions integrated:** {len(unique_questions)}",
        f"- **Question-to-owner assignments written:** {len(entries)}",
        f"- **Owner files updated (2024-2025 block):** {len(by_target)}",
        f"- **Basic/advanced owner files audited:** {len(owners)}",
        f"- **Owners without a 2024-2025 route:** {len(unrouted_owner_files)}",
        f"- **Missing route targets:** {len(missing_targets)}",
        f"- **Questions carrying OCR/manual-verification warnings:** {len(manual_questions)}",
        f"- **Warning-bearing route assignments:** {sum(len(items) for items in manual.values())}",
        f"- **Priority lexical-review assignments:** {sum(len(items) for items in low_signal.values())}",
        "",
        "### Unique questions by paper",
        "",
        "| Paper | Questions |",
        "|---|---:|",
    ]
    unique_by_paper = Counter(key[0] for key in unique_questions)
    for paper, count in sorted(unique_by_paper.items()):
        lines.append(f"| {paper} | {count} |")

    lines.extend(
        [
            "",
            "## 2. Subject-wise status",
            "",
            "| Subject | Unique questions | Route assignments | Files updated | "
            "Basic/advanced topic files | No 2024-2025 route | Low lexical signal | "
            "OCR/manual flags |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    subject_data: dict[str, tuple[list[Entry], list[Path], list[Path]]] = {}
    for subject in subjects:
        subject_entries = [
            entry for entry in entries
            if entry.target.relative_to(KNOWLEDGE).parts[0] == subject
        ]
        owners_here = topic_files(KNOWLEDGE / subject)
        routed = {entry.target for entry in subject_entries}
        unrouted = [path for path in owners_here if path not in routed]
        subject_data[subject] = (subject_entries, owners_here, unrouted)
        unique = {entry.question_key for entry in subject_entries}
        lines.append(
            f"| {subject} | {len(unique)} | {len(subject_entries)} | {len(routed)} "
            f"| {len(owners_here)} | {len(unrouted)} | {len(low_signal[subject])} "
            f"| {len(manual[subject])} |"
        )

    lines.extend(
        [
            "",
            "## 3. How to read what remains",
            "",
            "- **No 2024-2025 route** means this two-year corpus did not route a question to that "
            "owner. It is not automatically a syllabus gap.",
            "- **Low lexical signal** flags owners whose pre-integration text did not visibly contain "
            "enough discriminating words from the routed theme - a priority for conceptual review.",
            "- **OCR/manual flags** preserve export OCR uncertainty (wording or exact question number "
            "not legibly recoverable). Verify against the official scan before using the wording.",
            "- Essay is excluded from lexical-gap scoring because its routes point to writing-method owners.",
            "",
            "## 4. Topic-wise residuals",
        ]
    )
    for subject in subjects:
        subject_entries, owners_here, unrouted = subject_data[subject]
        if not subject_entries and not owners_here:
            continue
        lines.extend(["", f"### {subject}", ""])
        if unrouted:
            lines.append("**No routed 2024-2025 question in this owner:**")
            lines.append("")
            lines.extend(f"- `{display_path(path)}`" for path in unrouted)
            lines.append("")
        else:
            lines.extend(["**No-route owners:** None.", ""])

        if manual[subject]:
            lines.append("**OCR / official-scan verification still required:**")
            lines.append("")
            for entry in sorted(
                manual[subject],
                key=lambda item: (item.year, item.paper, question_number(item.question)),
            ):
                lines.append(
                    f"- {entry.year} {entry.paper} Q{entry.question}: {entry.theme}"
                )
            lines.append("")

    if missing_targets:
        lines.extend(["", "## 5. Missing targets", ""])
        lines.extend(f"- `{path}`" for path in missing_targets)
    else:
        lines.extend(
            [
                "",
                "## 5. Missing targets",
                "",
                "None. Every routed path resolves to an existing knowledge file.",
            ]
        )

    AUDIT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def place_block(clean: str, block: str) -> str:
    """Insert the 2024-2025 block before the 2018-2023 block if present, else append."""
    idx = clean.find(HIST_BEGIN)
    if idx != -1:
        head = clean[:idx].rstrip()
        tail = clean[idx:]
        return head + block + "\n" + tail
    return clean.rstrip() + "\n" + block


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Parse and reconcile without writing owner files or the audit.",
    )
    args = parser.parse_args()

    entries: list[Entry] = []
    for label, ledger in LEDGERS:
        parsed = parse_ledger(label, ledger)
        entries.extend(parsed)
        print(f"{ledger.name}: {len(parsed)} route assignments")

    missing_targets = sorted({entry.target for entry in entries if not entry.target.is_file()})
    if missing_targets:
        raise FileNotFoundError(
            "Missing route targets:\n" + "\n".join(str(path) for path in missing_targets)
        )

    by_target: dict[Path, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_target[entry.target].append(entry)

    duplicates = [
        key for key, count in Counter(
            (entry.question_key, entry.target) for entry in entries
        ).items() if count > 1
    ]
    if duplicates:
        raise ValueError(f"Duplicate question-to-owner assignments: {duplicates[:10]}")

    unique_questions = {entry.question_key for entry in entries}
    actual = Counter(key[0] for key in unique_questions)
    if actual != Counter(EXPECTED):
        raise ValueError(f"Question reconciliation failed: expected={EXPECTED}, actual={dict(actual)}")

    # Snapshot the 2024-2025-stripped text of every routed owner (for the lexical audit).
    original_text = {
        target: strip_generated(target.read_text(encoding="utf-8"))
        for target in by_target
    }
    print(f"Unique printed questions: {len(unique_questions)}")
    print(f"Owner files to update: {len(by_target)}")

    if args.check:
        return

    # Stale-route safety: strip the 2024-2025 block from EVERY owner, rewriting only on change.
    routed_targets = set(by_target)
    stripped = 0
    for path in all_owner_files():
        if path in routed_targets:
            continue
        current = path.read_text(encoding="utf-8")
        cleaned = strip_generated(current)
        if cleaned != current:
            path.write_text(normalize_generated_spacing(cleaned), encoding="utf-8")
            stripped += 1

    for target, target_entries in sorted(by_target.items()):
        clean = strip_generated(target.read_text(encoding="utf-8"))
        target.write_text(
            normalize_generated_spacing(place_block(clean, render_block(target_entries))),
            encoding="utf-8",
        )

    write_audit(entries, original_text, missing_targets)
    print(f"Wrote {len(by_target)} owner files; stripped stale recent block from {stripped} others")
    print(f"Audit: {AUDIT_PATH}")


if __name__ == "__main__":
    main()
