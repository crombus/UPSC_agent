"""Propagate the audited 2018-2023 UPSC PYQ routes into topic owners.

The routing ledgers are the controlling question-to-owner maps. This script adds an
idempotent, generated PYQ-demand section to every routed Markdown owner and writes a
residual audit. It never infers Prelims or CSAT answers.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
AUDIT_PATH = KNOWLEDGE / "PYQ-INTEGRATION-AUDIT-2018-2023.md"

BEGIN = "<!-- BEGIN GENERATED PYQ INTEGRATION: 2018-2023 -->"
END = "<!-- END GENERATED PYQ INTEGRATION: 2018-2023 -->"

LEDGERS = (
    ("Prelims GS-I", KNOWLEDGE / "_PYQ-ROUTING-PRELIMS-2018-2023.md"),
    ("CSAT", KNOWLEDGE / "_PYQ-ROUTING-CSAT-2018-2023.md"),
    (
        "Mains GS-I/GS-II/Essay",
        KNOWLEDGE / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ),
    (
        "Mains GS-III/GS-IV",
        KNOWLEDGE / "_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md",
    ),
)

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
YEAR_RE = re.compile(r"^20(?:18|19|20|21|22|23)$")
WORD_RE = re.compile(r"[A-Za-z][A-Za-z'-]{3,}")

STOP_WORDS = {
    "about",
    "after",
    "against",
    "among",
    "between",
    "could",
    "from",
    "have",
    "india",
    "indian",
    "into",
    "their",
    "there",
    "these",
    "through",
    "under",
    "versus",
    "what",
    "when",
    "where",
    "which",
    "while",
    "with",
    "would",
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

        if label == "Prelims GS-I":
            if len(cells) != 6:
                raise ValueError(f"{path.name}:{line_number}: expected 6 cells, got {len(cells)}")
            year, question, theme, family, routes, note = cells
            paper = "Prelims GS-I"
            directive = "Objective question; official key unavailable locally"
        elif label == "CSAT":
            if len(cells) != 6:
                raise ValueError(f"{path.name}:{line_number}: expected 6 cells, got {len(cells)}")
            year, question, theme, family, routes, note = cells
            paper = "CSAT"
            directive = "Objective question; official key unavailable locally"
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
    pattern = re.compile(
        rf"\n*{re.escape(BEGIN)}.*?{re.escape(END)}\n*",
        flags=re.DOTALL,
    )
    return pattern.sub("\n", text).rstrip() + "\n"


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
        key=lambda item: (item.year, item.paper, int(item.question), item.theme),
    )
    sources = sorted({entry.ledger_name for entry in entries})
    objective = any(entry.paper in {"Prelims GS-I", "CSAT"} for entry in entries)
    years = sorted({entry.year for entry in entries})
    papers = sorted({entry.paper for entry in entries})

    rows = [
        "",
        BEGIN,
        "## Historical PYQ Integration (2018-2023)",
        "",
        "> **Status:** Question-level PYQ demand is integrated into this owner.",
        "> **Provenance:** Audited local official-paper routing ledgers: "
        + ", ".join(f"`{source}`" for source in sources)
        + ".",
    ]
    if objective:
        rows.append(
            "> **Answer-key rule:** The official 2018-2023 Prelims/CSAT keys are not held "
            "locally; no option or answer has been inferred."
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
            "|---:|---|---:|---|---|---|---|",
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
    rows.extend(
        [
            "",
            "### What this owner must now support",
            "",
        ]
    )
    rows.extend(f"- {theme}" for theme in unique_themes)
    rows.extend(
        [
            "",
            "> The table integrates the examinable demand and paper metadata. It does not "
            "turn an unkeyed objective question into a solved answer, and it does not claim "
            "that lexical presence alone proves full conceptual sufficiency.",
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
                path
                for path in tier_dir.glob("*.md")
                if not path.name.startswith("_")
            )
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
        {
            path.relative_to(KNOWLEDGE).parts[0]
            for path in by_target
            if path != KNOWLEDGE
        }
        | {
            path.name
            for path in KNOWLEDGE.iterdir()
            if path.is_dir()
            and ((path / "basic").is_dir() or (path / "advanced").is_dir())
        }
    )

    low_signal: dict[str, list[tuple[Entry, str]]] = defaultdict(list)
    manual: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        subject = entry.target.relative_to(KNOWLEDGE).parts[0]
        if entry.paper == "Essay":
            # Essay routes intentionally target method owners, not theme-content encyclopedias.
            continue
        adequate, detail = lexical_signal(entry.theme, original_text.get(entry.target, ""))
        if not adequate:
            low_signal[subject].append((entry, detail))
        if "manual verification needed" in entry.note.casefold():
            manual[subject].append(entry)

    unique_questions = {entry.question_key for entry in entries}
    all_owner_files = [
        path
        for subject in subjects
        for path in topic_files(KNOWLEDGE / subject)
    ]
    unrouted_owner_files = [
        path for path in all_owner_files if path not in by_target
    ]
    manual_questions = {
        entry.question_key
        for items in manual.values()
        for entry in items
    }
    lines = [
        "# HISTORICAL PYQ INTEGRATION AUDIT, 2018-2023",
        "",
        "> Generated by `tools/propagate_historical_pyqs.py` from the four audited routing "
        "ledgers. Counts distinguish unique printed questions from route assignments, because "
        "cross-cutting questions and all CSAT questions may have more than one owner.",
        "",
        "## 1. Reconciliation",
        "",
        f"- **Unique printed questions integrated:** {len(unique_questions)}",
        f"- **Question-to-owner assignments written:** {len(entries)}",
        f"- **Owner files updated:** {len(by_target)}",
        f"- **Basic/advanced owner files audited:** {len(all_owner_files)}",
        f"- **Owners without a 2018-2023 route:** {len(unrouted_owner_files)}",
        f"- **Missing route targets:** {len(missing_targets)}",
        f"- **Questions carrying manual-verification warnings:** {len(manual_questions)}",
        f"- **Warning-bearing route assignments:** {sum(len(items) for items in manual.values())}",
        f"- **Priority lexical-review assignments:** "
        f"{sum(len(items) for items in low_signal.values())}",
        "",
        "### Unique questions by paper",
        "",
        "| Paper | Questions |",
        "|---|---:|",
    ]
    paper_counts = Counter(entry.paper for entry in {e for e in entries})
    unique_by_paper = Counter(key[0] for key in unique_questions)
    for paper, count in sorted(unique_by_paper.items()):
        lines.append(f"| {paper} | {count} |")

    lines.extend(
        [
            "",
            "## 2. Subject-wise status",
            "",
            "| Subject | Unique questions | Route assignments | Files updated | "
            "Basic/advanced topic files | No 2018-2023 route | Low lexical signal | "
            "Source verification |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    subject_data: dict[str, tuple[list[Entry], list[Path], list[Path]]] = {}
    for subject in subjects:
        subject_entries = [
            entry
            for entry in entries
            if entry.target.relative_to(KNOWLEDGE).parts[0] == subject
        ]
        subject_dir = KNOWLEDGE / subject
        owners = topic_files(subject_dir)
        routed = {entry.target for entry in subject_entries}
        unrouted = [path for path in owners if path not in routed]
        subject_data[subject] = (subject_entries, owners, unrouted)
        unique = {entry.question_key for entry in subject_entries}
        lines.append(
            f"| {subject} | {len(unique)} | {len(subject_entries)} | {len(routed)} "
            f"| {len(owners)} | {len(unrouted)} | {len(low_signal[subject])} "
            f"| {len(manual[subject])} |"
        )

    lines.extend(
        [
            "",
            "## 3. How to read what remains",
            "",
            "- **No 2018-2023 route** means that this six-year corpus did not route a question "
            "to that owner. It is not automatically a syllabus gap.",
            "- **Low lexical signal** means the pre-integration file did not visibly contain "
            "enough discriminating words from the routed theme. It is a priority for conceptual "
            "review, not proof that the answer is absent.",
            "- Essay is excluded from lexical-gap scoring because its routes intentionally point "
            "to writing-method owners rather than topic-content encyclopedias.",
            "- **Source verification** preserves OCR uncertainty from the ledger. The wording "
            "must be checked against the official scan before using it verbatim.",
            "- Official-syllabus architecture gaps remain controlled separately by "
            "`SYLLABUS-COVERAGE-AUDIT.md`.",
            "",
            "## 4. Topic-wise residuals",
        ]
    )
    for subject in subjects:
        subject_entries, owners, unrouted = subject_data[subject]
        if not subject_entries and not owners:
            continue
        lines.extend(["", f"### {subject}", ""])
        if unrouted:
            lines.append("**No routed 2018-2023 question in this owner:**")
            lines.append("")
            lines.extend(f"- `{display_path(path)}`" for path in unrouted)
            lines.append("")
        else:
            lines.extend(
                ["**No-route owners:** None.", ""]
            )

        if low_signal[subject]:
            lines.append("**Priority content-review signals:**")
            lines.append("")
            for entry, detail in sorted(
                low_signal[subject],
                key=lambda item: (
                    display_path(item[0].target),
                    item[0].year,
                    item[0].paper,
                    int(item[0].question),
                ),
            ):
                lines.append(
                    f"- `{display_path(entry.target)}` - {entry.year} {entry.paper} "
                    f"Q{entry.question}: {entry.theme} ({detail})"
                )
            lines.append("")
        else:
            lines.extend(["**Priority content-review signals:** None from this lexical check.", ""])

        if manual[subject]:
            lines.append("**Official-scan verification still required:**")
            lines.append("")
            for entry in sorted(
                manual[subject],
                key=lambda item: (item.year, item.paper, int(item.question)),
            ):
                lines.append(
                    f"- {entry.year} {entry.paper} Q{entry.question}: {entry.theme} - "
                    f"{entry.note}"
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
        key
        for key, count in Counter(
            (entry.question_key, entry.target) for entry in entries
        ).items()
        if count > 1
    ]
    if duplicates:
        raise ValueError(f"Duplicate question-to-owner assignments: {duplicates[:10]}")

    expected = {
        "Prelims GS-I": 600,
        "CSAT": 480,
        "GS-I": 120,
        "GS-II": 120,
        "GS-III": 120,
        "GS-IV": 72,
        "Essay": 48,
    }
    unique_questions = {entry.question_key for entry in entries}
    actual = Counter(key[0] for key in unique_questions)
    if actual != Counter(expected):
        raise ValueError(f"Question reconciliation failed: expected={expected}, actual={dict(actual)}")

    original_text = {
        target: strip_generated(target.read_text(encoding="utf-8"))
        for target in by_target
    }
    print(f"Unique printed questions: {len(unique_questions)}")
    print(f"Owner files: {len(by_target)}")

    if args.check:
        return

    for target, target_entries in sorted(by_target.items()):
        clean = original_text[target].rstrip()
        target.write_text(clean + "\n" + render_block(target_entries), encoding="utf-8")

    write_audit(entries, original_text, missing_targets)
    print(f"Wrote {len(by_target)} owner files")
    print(f"Audit: {AUDIT_PATH}")


if __name__ == "__main__":
    main()
