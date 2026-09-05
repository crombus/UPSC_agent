"""Build the master study index from knowledge files and generated notes PDFs.

Run:
    python tools/build_study_index.py

The generated index is intentionally reproducible. Re-run it after adding a topic,
learning-session note or PDF; no link list needs to be maintained by hand.
"""
from __future__ import annotations

import json
import os
import re
from collections import defaultdict
from datetime import date
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
WORKSPACE = ROOT.parent
NOTES = WORKSPACE / "notes"
OUTPUT = KNOWLEDGE / "STUDY-INDEX.md"
CANONICAL_SESSION_DIRECTORY = "learning-sessions"
LEGACY_SESSION_DIRECTORY_ALIASES = (
    "Terminal-Learning-Sessions",
    "learning-sessions-v2",
    "_learning-sessions",
)

SUBJECT_ORDER = [
    "Ancient-Indian-History",
    "Medieval-Indian-History",
    "Modern-Indian-History",
    "Indian-Art-and-Culture",
    "World-History",
    "Indian-Society",
    "Geography",
    "Polity",
    "Governance",
    "Social-Justice",
    "International-Relations",
    "Economy",
    "Environment-and-Ecology",
    "Science-and-Technology",
    "Internal-Security",
    "Disaster-Management",
    "Ethics",
    "Essay",
    "CSAT",
    "Qualifying-English",
    "Qualifying-Hindi",
    "Political-Theory",
    "Philosophy",
]

PRELIMS_AND_MAINS = {
    "Ancient-Indian-History",
    "Medieval-Indian-History",
    "Modern-Indian-History",
    "Indian-Art-and-Culture",
    "Geography",
    "Polity",
    "Governance",
    "Social-Justice",
    "International-Relations",
    "Economy",
    "Environment-and-Ecology",
    "Science-and-Technology",
}

MAINS_PRIMARY = {
    "World-History",
    "Indian-Society",
    "Internal-Security",
    "Disaster-Management",
    "Ethics",
    "Essay",
    "Political-Theory",
}

DISPLAY_NAMES = {
    "Ancient-Indian-History": "Ancient Indian History",
    "Medieval-Indian-History": "Medieval Indian History",
    "Modern-Indian-History": "Modern Indian History",
    "Indian-Art-and-Culture": "Indian Art and Culture",
    "World-History": "World History",
    "Indian-Society": "Indian Society",
    "Environment-and-Ecology": "Environment and Ecology",
    "Science-and-Technology": "Science and Technology",
    "Internal-Security": "Internal Security",
    "Disaster-Management": "Disaster Management",
    "Social-Justice": "Social Justice",
    "International-Relations": "International Relations",
    "Political-Theory": "Political Theory",
    "Qualifying-English": "Qualifying English",
    "Qualifying-Hindi": "Qualifying Hindi",
}

STOPWORDS = {
    "and", "the", "of", "in", "to", "a", "an", "for", "with", "india",
    "indian", "basic", "advanced", "must", "do", "complete", "topic",
}


def display_subject(subject: str) -> str:
    return DISPLAY_NAMES.get(subject, subject.replace("-", " "))


def md_link(label: str, target: Path) -> str:
    relative = Path(os.path.relpath(target, OUTPUT.parent)).as_posix()
    return f"[{escape(label)}]({relative})"


def escape(text: str) -> str:
    return text.replace("|", r"\|").replace("\n", " ").strip()


def file_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^#\s+(.+?)\s*$", text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return path.stem.replace("_", " ").replace("-", " ")


def topic_number(path: Path) -> str:
    match = re.match(r"^(\d{1,2})[_-]", path.name)
    if match:
        return match.group(1).zfill(2)
    for part in path.stem.split("-")[:6]:
        if re.fullmatch(r"\d{2}", part):
            return part
    return ""


def topic_label(path: Path) -> str:
    title = file_title(path)
    title = re.sub(
        r"\s+(?:-|—)\s+(?:MUST-DO|ADVANCED|CORE.*|EXAM-COMPLETE).*$",
        "",
        title,
        flags=re.I,
    )
    return title


def same_topic_number(topic: Path, candidate: Path) -> bool:
    topic_num = topic_number(topic)
    candidate_num = topic_number(candidate)
    if topic_num and candidate_num and candidate_num != topic_num:
        return False
    return True


def tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[A-Za-z0-9]+", text.casefold())
        if len(token) > 2 and token not in STOPWORDS
    }


PHILOSOPHY_V2_PREFIXES = {
    ("paper-1", "western"): "philosophy-paper-i-western-philosophy",
    ("paper-1", "indian"): "philosophy-paper-i-indian-philosophy",
    ("paper-2", "socio-political"): "philosophy-paper-ii-socio-political-philosophy",
    ("paper-2", "philosophy-of-religion"): "philosophy-paper-ii-philosophy-of-religion",
}


@lru_cache(maxsize=1)
def tracked_v2_owner_keys() -> dict[str, str]:
    tracker = WORKSPACE / "EXPORT-PDF-STATUS.json"
    if not tracker.is_file():
        return {}
    data = json.loads(tracker.read_text(encoding="utf-8"))
    owners: dict[str, str] = {}
    for entry in data.get("exports", []):
        if not isinstance(entry, dict) or entry.get("variant") != "learner-v2":
            continue
        provenance = entry.get("provenance")
        source = (
            provenance.get("source_basic")
            if isinstance(provenance, dict)
            else None
        )
        topic_key = entry.get("topic_key")
        if source and topic_key:
            owners[str(source).replace("\\", "/").casefold()] = str(topic_key)
    return owners


@lru_cache(maxsize=1)
def tracked_export_paths() -> dict[str, tuple[str, str]]:
    tracker = WORKSPACE / "EXPORT-PDF-STATUS.json"
    if not tracker.is_file():
        return {}
    data = json.loads(tracker.read_text(encoding="utf-8"))
    paths: dict[str, tuple[str, str]] = {}
    for entry in data.get("exports", []):
        if not isinstance(entry, dict):
            continue
        topic_key = entry.get("topic_key")
        variant = entry.get("variant")
        if not topic_key or not variant:
            continue
        for field in ("main_pdf", "workbook", "markdown"):
            value = entry.get(field)
            if value:
                paths[str(value).replace("\\", "/").casefold()] = (
                    str(topic_key),
                    str(variant),
                )
    return paths


def philosophy_v2_topic_prefix(topic: Path) -> str:
    try:
        relative = topic.relative_to(WORKSPACE).as_posix().casefold()
    except ValueError:
        relative = ""
    tracked = tracked_v2_owner_keys().get(relative)
    if tracked:
        return tracked.casefold()

    parts = [part.casefold() for part in topic.parts]
    for index, part in enumerate(parts[:-1]):
        if part not in {"paper-1", "paper-2"} or index + 1 >= len(parts):
            continue
        prefix = PHILOSOPHY_V2_PREFIXES.get((part, parts[index + 1]))
        number = topic_number(topic)
        if prefix and number:
            return f"{prefix}-{number}".casefold()
    return ""


def session_label(path: Path) -> str:
    stem = path.stem.casefold()
    if "workbook" in stem:
        return "Workbook"
    if "v2" in {part.casefold() for part in path.parts}:
        return "V2 session"
    if any(alias.casefold() in {part.casefold() for part in path.parts}
           for alias in LEGACY_SESSION_DIRECTORY_ALIASES):
        return "Legacy session"
    if CANONICAL_SESSION_DIRECTORY.casefold() in {
        part.casefold() for part in path.parts
    }:
        return "Legacy/reference v1 session"
    if "learning-session" in stem:
        return "Session"
    return "Session"


def notes_for_subject(subject: str) -> list[Path]:
    if not NOTES.is_dir():
        return []
    aliases = {subject, display_subject(subject), subject.replace("-and-", "-")}
    if subject in {"Ancient-Indian-History", "Medieval-Indian-History", "Modern-Indian-History", "World-History"}:
        aliases.add("History")
    folders = [
        child for child in NOTES.iterdir()
        if child.is_dir() and child.name.casefold() in {alias.casefold() for alias in aliases}
    ]
    pdfs: list[Path] = []
    for folder in folders:
        pdfs.extend(folder.rglob("*.pdf"))
    return sorted(set(pdfs))


def matched_notes(topic: Path, subject_pdfs: list[Path]) -> list[Path]:
    topic_words = tokens(topic_label(topic))
    if not topic_words:
        return []
    stable_prefix = philosophy_v2_topic_prefix(topic)
    tracked_paths = tracked_export_paths()
    scored: list[tuple[float, Path]] = []
    for pdf in subject_pdfs:
        if not same_topic_number(topic, pdf):
            continue
        try:
            relative = pdf.relative_to(WORKSPACE).as_posix().casefold()
        except ValueError:
            relative = ""
        tracked = tracked_paths.get(relative)
        if stable_prefix and tracked and tracked[0].casefold() == stable_prefix:
            scored.append((2.0 if tracked[1] == "learner-v2" else 1.9, pdf))
            continue
        pdf_stem = pdf.stem.casefold()
        if "learning-session-v2" in {
            part.casefold() for part in pdf.parts
        } and pdf_stem.startswith("philosophy-"):
            if stable_prefix and pdf_stem.startswith(stable_prefix):
                scored.append((2.0, pdf))
            continue
        pdf_words = tokens(pdf.stem)
        overlap = len(topic_words & pdf_words)
        if not overlap:
            continue
        score = overlap / max(1, len(topic_words))
        if score >= 0.35 or overlap >= 3:
            scored.append((score, pdf))
    scored.sort(key=lambda item: (-item[0], item[1].as_posix().casefold()))
    limit = 4 if stable_prefix else 3
    return [path for _, path in scored[:limit]]


def matched_sessions(subject_dir: Path, topic: Path) -> list[Path]:
    session_dirs = [
        subject_dir / CANONICAL_SESSION_DIRECTORY,
        *(
            subject_dir / alias
            for alias in LEGACY_SESSION_DIRECTORY_ALIASES
        ),
    ]
    if subject_dir.name == "Philosophy":
        session_dirs.extend(
            path
            for path in subject_dir.rglob(CANONICAL_SESSION_DIRECTORY)
            if path not in session_dirs
        )
    topic_words = tokens(topic_label(topic))
    stable_prefix = philosophy_v2_topic_prefix(topic)
    tracked_paths = tracked_export_paths()
    candidates: list[tuple[float, Path]] = []
    for session_dir in session_dirs:
        if not session_dir.is_dir():
            continue
        for path in session_dir.rglob("*.md"):
            if not same_topic_number(topic, path):
                continue
            try:
                relative = path.relative_to(WORKSPACE).as_posix().casefold()
            except ValueError:
                relative = ""
            tracked = tracked_paths.get(relative)
            if stable_prefix and tracked and tracked[0].casefold() == stable_prefix:
                candidates.append(
                    (2.0 if tracked[1] == "learner-v2" else 1.9, path)
                )
                continue
            path_stem = path.stem.casefold()
            if "v2" in {
                part.casefold() for part in path.parts
            } and path_stem.startswith("philosophy-"):
                if stable_prefix and path_stem.startswith(stable_prefix):
                    candidates.append((2.0, path))
                continue
            session_words = tokens(path.stem)
            overlap = len(topic_words & session_words)
            if overlap:
                candidates.append((overlap / max(1, len(topic_words)), path))
    candidates.sort(key=lambda item: (-item[0], item[1].as_posix().casefold()))
    eligible = [path for score, path in candidates if score >= 0.25]
    if stable_prefix:
        selected: list[Path] = []
        selected_families: set[str] = set()
        for path in eligible:
            family = "v2" if session_label(path) == "V2 session" else "legacy"
            if family in selected_families:
                continue
            selected.append(path)
            selected_families.add(family)
            if len(selected) == 2:
                break
        return selected
    return eligible[:2]


def prelims_direction(subject: str) -> str:
    if subject in PRELIMS_AND_MAINS:
        return "Core definitions, classifications, maps/institutions, factual distinctions, traps and routed Prelims PYQs."
    if subject == "CSAT":
        return "Timed concepts, elimination and mixed Paper-II practice; maintain qualifying safety margin."
    if subject in {"Qualifying-English", "Qualifying-Hindi"}:
        return "Not a Prelims subject; use this Core for the compulsory qualifying paper."
    if subject == "Philosophy":
        return "Not a GS Prelims subject; revise only overlaps that independently belong to GS."
    return "No separate static Prelims burden; retain only relevant current-affairs or cross-subject awareness."


def mains_direction(subject: str, has_advanced: bool) -> str:
    if subject == "CSAT":
        return "Not a Mains merit paper; keep two weekly qualifying-practice sessions."
    if subject in {"Qualifying-English", "Qualifying-Hindi"}:
        return "Grammar/usage plus comprehension, précis, essay and translation practice as applicable."
    if subject == "Essay":
        return "Framework, multidimensional brainstorming, introductions/conclusions and timed full essays."
    if subject == "Ethics":
        return "Definitions, thinkers/examples, stakeholder analysis, case decisions and justification."
    if subject == "Philosophy":
        return "Optional doctrine, arguments, objections, comparison and direct 2018-2025 PYQ answer writing."
    if subject == "Political-Theory":
        return "Use selectively as conceptual enrichment; do not replace the direct GS or Optional owner."
    if has_advanced:
        return "Core mechanism plus Advanced analysis, evidence, criticism, reforms and routed Mains PYQs."
    return "Core concepts, examples, structured answer dimensions and timed descriptive practice."


def paired_topics(subject_dir: Path) -> list[tuple[Path, Path | None]]:
    basic_dir = subject_dir / "basic"
    advanced_dir = subject_dir / "advanced"
    if not basic_dir.is_dir():
        return []
    advanced_by_number: dict[str, Path] = {}
    if advanced_dir.is_dir():
        for path in advanced_dir.glob("*.md"):
            number = topic_number(path)
            if number:
                advanced_by_number[number] = path
    return [
        (basic, advanced_by_number.get(topic_number(basic)))
        for basic in sorted(basic_dir.glob("*.md"))
    ]


def philosophy_topics(subject_dir: Path) -> list[Path]:
    paths: list[Path] = []
    for paper in ("paper-1", "paper-2"):
        paper_dir = subject_dir / paper
        if paper_dir.is_dir():
            paths.extend(
                path for path in paper_dir.rglob("*.md")
                if not path.name.startswith("_PYQ-")
            )
    return sorted(paths)


def render_topic_section(subject: str, subject_dir: Path) -> list[str]:
    lines = [f"## {display_subject(subject)}", ""]
    overview = []
    for name in (
        "README.md",
        "00_Master-Framework.md",
        "00_Master-Chronology.md",
        "REVISION-CHART_Ages-Eras-and-Distinctive-Features.md",
        "REVISION-CHART_Core-Processes-Regions-and-Distinctive-Features.md",
        "REVISION-CHART_Forms-Styles-and-Distinctive-Features.md",
        "REVISION-CHART_Structures-Change-and-Distinctive-Features.md",
        "REVISION-CHART_Constitutional-Architecture-and-Distinctive-Features.md",
        "REVISION-CHART_Systems-Delivery-and-Distinctive-Features.md",
        "REVISION-CHART_Rights-Capabilities-and-Distinctive-Features.md",
        "REVISION-CHART_Actors-Interests-and-Distinctive-Features.md",
        "REVISION-CHART_Mechanisms-Sectors-and-Distinctive-Features.md",
        "REVISION-CHART_Ecological-Processes-Laws-and-Distinctive-Features.md",
        "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md",
        "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md",
        "REVISION-CHART_Values-Dilemmas-and-Distinctive-Features.md",
        "REVISION-CHART_Concepts-Ideologies-and-Distinctive-Features.md",
        "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
        "REVISION-CHART_Skills-Shortcuts-and-Distinctive-Features.md",
        "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    ):
        path = subject_dir / name
        if path.is_file():
            overview.append(md_link(name.replace(".md", ""), path))
    if overview:
        lines.extend(["**Start/ownership:** " + " · ".join(overview), ""])

    subject_pdfs = notes_for_subject(subject)
    rows: list[str] = []
    topics = paired_topics(subject_dir)
    if topics:
        for basic, advanced in topics:
            resources = [md_link("Core", basic)]
            if advanced:
                resources.append(md_link("Advanced", advanced))
            sessions = matched_sessions(subject_dir, basic)
            session_links = " · ".join(
                md_link(session_label(path), path) for path in sessions
            ) or "—"
            note_links = " · ".join(
                md_link(pdf.stem, pdf) for pdf in matched_notes(basic, subject_pdfs)
            ) or "—"
            rows.append(
                f"| {escape(topic_number(basic) or '—')} | {escape(topic_label(basic))} "
                f"| {escape(prelims_direction(subject))} | {escape(mains_direction(subject, advanced is not None))} "
                f"| {' · '.join(resources)} | {session_links} | {note_links} |"
            )
    elif subject == "Philosophy":
        for path in philosophy_topics(subject_dir):
            relative_area = path.parent.relative_to(subject_dir).as_posix()
            note_links = " · ".join(
                md_link(pdf.stem, pdf) for pdf in matched_notes(path, subject_pdfs)
            ) or "—"
            sessions = matched_sessions(subject_dir, path)
            session_links = " · ".join(
                md_link(session_label(item), item) for item in sessions
            ) or "—"
            rows.append(
                f"| {escape(relative_area)} | {escape(topic_label(path))} "
                f"| {escape(prelims_direction(subject))} | {escape(mains_direction(subject, False))} "
                f"| {md_link('Topic', path)} | {session_links} | {note_links} |"
            )
    else:
        lines.extend(["No numbered Core topic files found; use the complete registry below.", ""])
        return lines

    lines.extend(
        [
            "| # / Area | Topic | Prelims / objective study | Mains / descriptive study | Knowledge | Learning-session notes | Notes PDFs |",
            "|---|---|---|---|---|---|---|",
            *rows,
            "",
        ]
    )
    return lines


def render_file_registry() -> list[str]:
    lines = ["# Complete Knowledge-File Registry", ""]
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in KNOWLEDGE.rglob("*.md"):
        if path == OUTPUT:
            continue
        relative = path.relative_to(KNOWLEDGE)
        grouped[relative.parts[0]].append(path)
    for subject in SUBJECT_ORDER:
        paths = sorted(grouped.pop(subject, []))
        if not paths:
            continue
        lines.extend([f"## {display_subject(subject)}", ""])
        for path in paths:
            label = path.relative_to(KNOWLEDGE / subject).as_posix()
            lines.append(f"- {md_link(label, path)}")
        lines.append("")
    for subject in sorted(grouped):
        lines.extend([f"## {display_subject(subject)}", ""])
        for path in sorted(grouped[subject]):
            lines.append(f"- {md_link(path.relative_to(KNOWLEDGE).as_posix(), path)}")
        lines.append("")
    return lines


def render_notes_registry() -> list[str]:
    lines = ["# Notes PDF Registry", ""]
    if not NOTES.is_dir():
        return lines + ["Notes directory is not available.", ""]
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in NOTES.rglob("*.pdf"):
        relative = path.relative_to(NOTES)
        grouped[relative.parts[0]].append(path)
    total = sum(len(paths) for paths in grouped.values())
    lines.extend(
        [
            f"**Current PDFs indexed:** {total}. Re-run `python tools/build_study_index.py` after generating notes.",
            "",
        ]
    )
    for folder in sorted(grouped):
        lines.extend([f"## {folder}", ""])
        for path in sorted(grouped[folder]):
            label = path.relative_to(NOTES).as_posix()
            lines.append(f"- {md_link(label, path)}")
        lines.append("")
    return lines


def main() -> None:
    subject_dirs = {
        path.name: path
        for path in KNOWLEDGE.iterdir()
        if path.is_dir() and not path.name.startswith("_")
    }
    knowledge_files = [path for path in KNOWLEDGE.rglob("*.md") if path != OUTPUT]
    note_files = list(NOTES.rglob("*.pdf")) if NOTES.is_dir() else []

    lines = [
        "# UPSC Master Study Index",
        "",
        f"> **Generated:** {date.today().isoformat()} by `tools/build_study_index.py`.",
        "> **Update rule:** Re-run the builder whenever a knowledge file, learning-session note or notes PDF is added.",
        f"> **Session path:** `{CANONICAL_SESSION_DIRECTORY}/` is canonical. "
        f"`{'`, `'.join(LEGACY_SESSION_DIRECTORY_ALIASES)}` are read-only compatibility aliases.",
        "",
        "## Coverage status",
        "",
        "- **Official syllabus:** 147 COVERED, 27 deliberate PARTIAL ownership boundaries, 0 GAP.",
        "- **GS/CSAT/Essay PYQs:** 2,260 printed questions from 2018-2026 routed through 2,974 owner assignments; zero missing targets and zero unresolved OCR warnings.",
        "- **Philosophy Optional:** official clause ownership and 2018-2025 PYQ banks are present.",
        "- **Qualifying languages:** the complete official skill pattern is owned; locally available 2019 and 2021 Hindi/English papers ground the practice architecture, but this is not a claim that every historical language paper has been ingested.",
        "- **Remaining production work:** learning-session delivery, personal revision notes and answer-writing performance—not syllabus architecture.",
        "",
        "## How to use each topic row",
        "",
        "1. Read **Core** first; skipping it can affect exam outcome.",
        "2. Solve routed PYQs and make/revise the topic PDF note.",
        "3. Use **Advanced** for Mains/Optional depth after Core; it must not be the sole source of an indispensable fact.",
        "4. Mark the topic complete only after active recall, objective practice where applicable and one written answer.",
        "",
        f"**Inventory:** {len(knowledge_files)} knowledge Markdown files and {len(note_files)} notes PDFs.",
        "",
        "# Topic-by-Topic Study Map",
        "",
    ]
    for subject in SUBJECT_ORDER:
        subject_dir = subject_dirs.get(subject)
        if subject_dir:
            lines.extend(render_topic_section(subject, subject_dir))

    lines.extend(render_file_registry())
    lines.extend(render_notes_registry())
    OUTPUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(
        f"Wrote {OUTPUT} with {len(knowledge_files)} knowledge files "
        f"and {len(note_files)} notes PDFs indexed."
    )


if __name__ == "__main__":
    main()
