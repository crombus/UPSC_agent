"""Propagate the audited 2026 UPSC PYQ routes into topic owners.

This is the 2026-cycle sibling of `propagate_historical_pyqs.py` (2018-2023) and
`propagate_recent_pyqs.py` (2024-2025). It reads the two 2026 routing ledgers
(Prelims GS-I and CSAT) and inserts a *separate* generated block, delimited by its own
2026 markers, into every routed owner - without touching the 2018-2023 or 2024-2025 blocks.

Idempotence and stale-route safety: on every run it first strips the 2026 block from
*all* Basic/Advanced owner files, then re-appends a fresh block only to currently-routed
owners. An owner that loses all its 2026 routes therefore loses its 2026 block too.

Cross-order stability: the 2026 block is anchored immediately BEFORE the 2024-2025 block
(RECENT_BEGIN) when present, else immediately before the 2018-2023 block (HIST_BEGIN),
else appended at end. Because the recent propagator always inserts its block immediately
before the 2018-2023 block, and the historical propagator always appends its block at end,
the three propagators converge on a stable newest->oldest order regardless of run order:

    [owner content] [2026 block] [2024-2025 block] [2018-2023 block]

The 2026 Prelims and CSAT keys held locally are PROVISIONAL; no answer letter is ever
recorded or inferred. The accurate provisional-key status is carried from the ledgers.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
AUDIT_PATH = KNOWLEDGE / "PYQ-INTEGRATION-AUDIT-2026.md"

BEGIN = "<!-- BEGIN GENERATED PYQ INTEGRATION: 2026 -->"
END = "<!-- END GENERATED PYQ INTEGRATION: 2026 -->"

# Anchors for cross-order-stable placement (see module docstring).
RECENT_BEGIN = "<!-- BEGIN GENERATED PYQ INTEGRATION: 2024-2025 -->"
HIST_BEGIN = "<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->"

LEDGERS = (
    ("Prelims GS-I", KNOWLEDGE / "_PYQ-ROUTING-PRELIMS-2026.md"),
    ("CSAT", KNOWLEDGE / "_PYQ-ROUTING-CSAT-2026.md"),
)

EXPECTED = {
    "Prelims GS-I": 100,
    "CSAT": 80,
}

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
YEAR_RE = re.compile(r"^2026$")
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

    @property
    def is_core_gap(self) -> bool:
        return "core-gap" in self.note.casefold()


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def question_number(value: str) -> int:
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

        if len(cells) != 6:
            raise ValueError(f"{path.name}:{line_number}: expected 6 cells, got {len(cells)}")
        year, question, theme, family, routes, note = cells
        paper = label  # "Prelims GS-I" or "CSAT"
        directive = ("Objective question; provisional 2026 Set-A key present locally, "
                     "answer not inferred")

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
    if entry.paper == "CSAT":
        return "Practise this exact skill form under timed elimination; no answer is inferred here."
    return "Cover the named fact/concept and its likely statement-level distinctions."


def render_block(entries: list[Entry]) -> str:
    entries = sorted(
        entries,
        key=lambda item: (item.year, item.paper, question_number(item.question), item.theme),
    )
    sources = sorted({entry.ledger_name for entry in entries})
    papers = sorted({entry.paper for entry in entries})

    rows = [
        "",
        BEGIN,
        "## 2026 PYQ Integration",
        "",
        "> **Status:** 2026 question-level PYQ demand is integrated into this owner.",
        "> **Provenance:** Audited local official-paper routing ledgers: "
        + ", ".join(f"`{source}`" for source in sources)
        + ".",
        "> **Answer-key rule:** The 2026 Prelims and CSAT Set-A keys held locally are "
        "**provisional**; no option or answer is recorded or inferred in this integration.",
        "",
        f"- **Year represented:** 2026",
        f"- **Paper(s):** {', '.join(papers)}",
        f"- **Routed question demands:** {len(entries)}",
        "",
        "| Year | Paper | Q | PYQ demand (neutral rendering) | Directive / format "
        "| Source status | Owner requirement |",
        "|---:|---|---|---|---|---|---|",
    ]
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
            "> This block integrates the 2026 examinable demand and paper metadata. It is kept "
            "separate from the 2018-2023 and 2024-2025 blocks and does not convert a "
            "provisionally-keyed, answer-free objective question into a solved answer.",
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
        adequate, detail = lexical_signal(entry.theme, original_text.get(entry.target, ""))
        if not adequate:
            low_signal[subject].append((entry, detail))
        if "ocr-uncertain" in entry.note.casefold() or "manual verification needed" in entry.note.casefold():
            manual[subject].append(entry)

    core_gaps = sorted(
        {entry for entry in entries if entry.is_core_gap},
        key=lambda item: (item.paper, question_number(item.question)),
    )

    unique_questions = {entry.question_key for entry in entries}
    owners = all_owner_files()
    unrouted_owner_files = [path for path in owners if path not in by_target]
    manual_questions = {entry.question_key for items in manual.values() for entry in items}

    lines = [
        "# 2026 PYQ INTEGRATION AUDIT",
        "",
        "> Generated by `tools/propagate_2026_pyqs.py` from the two audited 2026 routing "
        "ledgers (Prelims GS-I and CSAT). Counts distinguish unique printed questions from "
        "route assignments, because a question may have more than one owner. This audit is "
        "separate from the 2018-2023 and 2024-2025 audits and does not alter them.",
        "",
        "## 1. Reconciliation",
        "",
        f"- **Unique printed questions integrated:** {len(unique_questions)}",
        f"- **Question-to-owner assignments written:** {len(entries)}",
        f"- **Owner files updated (2026 block):** {len(by_target)}",
        f"- **Basic/advanced owner files audited:** {len(owners)}",
        f"- **Owners without a 2026 route:** {len(unrouted_owner_files)}",
        f"- **Missing route targets:** {len(missing_targets)}",
        f"- **Questions carrying OCR/manual-verification warnings:** {len(manual_questions)}",
        f"- **Priority lexical-review assignments:** {sum(len(items) for items in low_signal.values())}",
        f"- **Core-owner gaps (routed to closest owner, gap recorded):** {len(core_gaps)}",
        "",
        "> **Key status:** The 2026 Prelims and CSAT Set-A keys held locally are provisional; "
        "no answer letter is recorded or inferred anywhere in this integration.",
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
            "Basic/advanced topic files | No 2026 route | Low lexical signal | "
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
            "- **No 2026 route** means this one-year corpus did not route a question to that "
            "owner. It is not automatically a syllabus gap.",
            "- **Low lexical signal** flags owners whose pre-integration text did not visibly "
            "contain enough discriminating words from the routed theme - a priority for "
            "conceptual review.",
            "- **OCR/manual flags** preserve any export OCR uncertainty. Every 2026 row was "
            "verified against the official Set-A scan, so this count is expected to be zero.",
            "- **Core-owner gaps** are questions for which no dedicated Core (basic) owner exists; "
            "each is routed to the closest existing Core owner and listed in section 5, never "
            "hidden behind the loosely related route.",
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
            lines.append("**No routed 2026 question in this owner:**")
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

    lines.extend(["", "## 5. Core-owner gaps revealed by 2026 PYQs", ""])
    if core_gaps:
        lines.append(
            "These 2026 questions have no dedicated Core (basic) owner. Each is routed to the "
            "closest existing Core owner (shown), and the gap is recorded here rather than hidden:"
        )
        lines.append("")
        for entry in core_gaps:
            lines.append(
                f"- **{entry.paper} Q{entry.question}** - {entry.theme} "
                f"-> closest owner `{display_path(entry.target)}`; {entry.note.split('CORE-GAP:', 1)[-1].strip()}"
            )
        lines.append("")
    else:
        lines.append("None. Every 2026 question has an adequate Core owner.")
        lines.append("")

    if missing_targets:
        lines.extend(["## 6. Missing targets", ""])
        lines.extend(f"- `{path}`" for path in missing_targets)
    else:
        lines.extend(
            [
                "## 6. Missing targets",
                "",
                "None. Every routed path resolves to an existing knowledge file.",
            ]
        )

    AUDIT_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def place_block(clean: str, block: str) -> str:
    """Insert the 2026 block at a cross-order-stable anchor.

    Priority: immediately before the 2024-2025 block, else before the 2018-2023 block,
    else appended at end. This yields a stable newest->oldest order regardless of the
    order in which the three propagators are run.
    """
    for anchor in (RECENT_BEGIN, HIST_BEGIN):
        idx = clean.find(anchor)
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

    original_text = {
        target: strip_generated(target.read_text(encoding="utf-8"))
        for target in by_target
    }
    print(f"Unique printed questions: {len(unique_questions)}")
    print(f"Owner files to update: {len(by_target)}")

    if args.check:
        return

    # Stale-route safety: strip the 2026 block from EVERY owner, rewriting only on change.
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
    print(f"Wrote {len(by_target)} owner files; stripped stale 2026 block from {stripped} others")
    print(f"Audit: {AUDIT_PATH}")


if __name__ == "__main__":
    main()
