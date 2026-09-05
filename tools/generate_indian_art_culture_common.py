"""Shared authoring-only engine for Indian Art and Culture learner-v2 batches."""

from __future__ import annotations

import hashlib
import json
import re
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType
from typing import Iterable, Iterator

import generate_v2_section_indexes as section_indexes
import generate_world_history_common as _base
import carvaka_flowchart


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-01"
SUBJECT = "Indian-Art-and-Culture"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
GRAPHICAL_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "indian-art-and-culture--subject-wide-syllabus.json"
)
LOCAL_BOOKS = [
    ROOT / "books" / "Nitin Singhania's Indian Art and Culture.pdf",
]
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Framework.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md",
    KNOWLEDGE / "REVISION-CHART_Forms-Styles-and-Distinctive-Features.md",
    KNOWLEDGE / "ANSWER-WORTHINESS-AUDIT.md",
]
COMMON_CROSS = [path for path in COMMON_CROSS if path.is_file()]
PYQ_INDEXES = [
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2026.md",
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]

_BASE_OWNER_DEPTH = _base._owner_depth
_BASE_SOLVED_PYQ_SECTION = _base.solved_pyq_section


def _session_keywords(
    title: str,
    selected: list[tuple[str, str]],
) -> list[str]:
    """Select six compact, topic-specific terms for semantic navigation."""

    excluded = {
        "about",
        "across",
        "after",
        "against",
        "answer",
        "audit",
        "boundary",
        "build",
        "current",
        "definition",
        "evidence",
        "exact",
        "final",
        "framework",
        "historical",
        "history",
        "indian",
        "link",
        "living",
        "mechanism",
        "method",
        "prepare",
        "question",
        "rather",
        "source",
        "stage",
        "through",
        "topic",
        "tradition",
        "verified",
        "while",
        "within",
    }
    source = " ".join(
        [title, *[label for label, _ in selected], *[text for _, text in selected]]
    )
    result: list[str] = []
    seen: set[str] = set()
    for word in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", source):
        folded = word.casefold().strip("-'")
        if folded in excluded or folded in seen:
            continue
        seen.add(folded)
        result.append(word)
        if len(result) == 6:
            break
    if len(result) < 4:
        raise ValueError(f"{title}: unable to derive four topic-specific keywords.")
    return result


def _session_fragment(
    config: dict[str, object],
    number: int,
    session_plan: tuple[str, list[int], str, str],
) -> str:
    """Build one semantically complete learner-v2 teaching session."""

    title, indexes, caution, exam_use = session_plan
    facts: list[tuple[str, str]] = config["facts"]
    selected = [facts[index] for index in indexes]
    labels = [label for label, _ in selected]
    evidence = "\n".join(f"- {statement}" for _, statement in selected)
    core = " ".join(statement for _, statement in selected)
    joined = ", ".join(labels[:-1]) + (
        f" and {labels[-1]}" if len(labels) > 1 else labels[0]
    )
    plain = (
        f"{title} is the part of {config['title']} that explains how "
        f"{joined} fit into one examinable idea."
    )
    technical = (
        f"In art-historical analysis, {title} denotes the source-bounded "
        f"relationship among {joined}, classified by form, medium, "
        "patronage, performance context and evidentiary limit."
    )
    keywords = _session_keywords(title, selected)
    mapped_terms = ", ".join(keywords[:3])
    evidence_term = keywords[3]
    guidance = (
        f"Define {mapped_terms}; cite {evidence_term} as named evidence; "
        f"then apply this qualification: {caution} Conclude by showing how "
        f"the distinction supports this answer route: {exam_use}"
    )
    fragment = (
        f"### SESSION {number} — {_base.phase_for(number)} — {title}\n\n"
        "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        f"**Plain-language definition:** {plain}\n\n"
        f"**Technical definition:** {technical}\n\n"
        "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        f"> {title} should be analysed as a relation among {joined}, not "
        "as an isolated list of names.\n\n"
        "#### MUST-WRITE KEYWORDS\n\n"
        + "\n".join(f"- **{label}**" for label in keywords)
        + "\n\n"
        f"**How to use them:** {guidance}.\n\n"
        + _base._session_visual(title, labels, caution)
        + "\n\n#### CORE EXPLANATION\n\n"
        + core
        + "\n\n#### NAMED EVIDENCE AND MECHANISM\n\n"
        + evidence
        + "\n\n#### EXAMINER CAUTION\n\n"
        + f"- {caution}\n\n"
        + "#### EXAM LINK\n\n"
        + f"- **Prelims:** Retain the exact form, region, text, technique "
        f"or institution attached to {title}.\n"
        + f"- **Mains:** {exam_use}\n\n"
        + "#### MINI RECAP\n\n"
        + f"- **Evidence chain:** {' -> '.join(labels)}\n"
        + f"- **Qualified use:** {exam_use}\n\n"
        + "#### CLOSING RECALL FLOW\n\n"
        + "```closure-flow\n"
        + f"START / CONCEPT: {title}\n"
        + f"EXACT TERMS: {' | '.join(keywords)}\n"
        + f"MECHANISM / ARGUMENT: relate {joined} through form, context and patronage\n"
        + f"CONSEQUENCE / CONTRAST: This relation supports the answer route that {exam_use[0].lower() + exam_use[1:]}\n"
        + f"UPSC TRAP / ANSWER-USE: LIMIT: {caution}\n"
        + f"ANSWER-GRABBING FORMULATION: {title} converts named evidence into a qualified argument\n"
        + "```"
    )
    return re.sub(r"[ \t]+\n", "\n", fragment).strip()


def topic(
    number: int,
    title: str,
    source_stem: str,
    canonical_name: str,
    facts: list[tuple[str, str]],
    traps: list[str],
    mains: list[tuple[int, str, str, list[int]]],
    session_plans: list[tuple[str, list[int], str, str]],
    panels: list[tuple[str, str, str, list[str]]],
    required_terms: list[str],
    pyq_note: str,
    pyq_solutions: list[tuple[str, str, str, str, str]],
    live_sources: Iterable[str] = (),
    current_note: str | None = None,
    extra: Iterable[str] = (),
) -> dict[str, object]:
    """Create one Indian Art and Culture topic configuration."""

    return {
        "number": number,
        "key": f"indian-art-and-culture-{number:02d}",
        "title": title,
        "basic": KNOWLEDGE / "basic" / f"{source_stem}.md",
        "advanced": KNOWLEDGE / "advanced" / f"{source_stem}.md",
        "canonical": KNOWLEDGE / canonical_name,
        "extra": [KNOWLEDGE / value for value in extra],
        "facts": facts,
        "traps": traps,
        "mains": mains,
        "session_plans": session_plans,
        "panels": panels,
        "required_terms": required_terms,
        "live_sources": list(live_sources),
        "current_note": current_note
        or (
            "No directly relevant live official item was verified for this "
            "topic on 2026-09-01. The package therefore says 'no verified "
            "live item' and does not invent a date, status, project or figure."
        ),
        "ocr_note": (
            "Repository Markdown was primary. The available OCR-searchable "
            "Nitin Singhania Indian Art and Culture PDF was retained as a "
            "supplementary source; no unsupported page precision, quotation "
            "or dynamic status was imported from it."
        ),
        "pyq_note": pyq_note,
        "pyq_solutions": pyq_solutions,
    }


def _full_owner_depth(path: Path, *, exclude_pyq: bool) -> str:
    """Preserve the complete owner while lowering its headings for assembly."""

    return _BASE_OWNER_DEPTH(path, exclude_pyq=False)


def _audited_pyq_section(
    config: dict[str, object],
    pyq_blocks: list[str],
) -> str:
    heading = (
        "### TRANSPARENT ZERO-DIRECT-PYQ AUDIT"
        if not config["pyq_solutions"]
        else "### VERIFIED PYQ OWNERSHIP AUDIT"
    )
    audit = f"{heading}\n\n{config['pyq_note']}"
    if pyq_blocks:
        audit += "\n\n### OWNER PYQ LEDGER EXTRACTS\n\n" + "\n\n".join(pyq_blocks)
    cards = []
    for number, (year, paper, demand, status, model) in enumerate(
        config["pyq_solutions"], 1
    ):
        cards.append(
            f"### PYQ DEMAND CARD {number} — {year} {paper}\n\n"
            f"**Demand:** {demand}\n\n"
            f"**Status:** {status}\n\n"
            f"**Model solution:** {model}"
        )
    if cards:
        audit += "\n\n" + "\n\n".join(cards)
    return audit


def ensure_section_manifest() -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    target = next(
        item
        for item in catalog["topics"]
        if item.get("topic_key") == "indian-art-and-culture-01"
    )
    path = section_indexes.materialize_catalog_section_manifest(
        ROOT,
        catalog,
        target,
    )
    if path != SECTION_MANIFEST:
        raise ValueError(f"Unexpected Indian Art and Culture manifest path: {path}")
    return path


def validate_catalog(topics: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [config["key"] for config in topics if config["key"] not in keys]
    if missing:
        raise ValueError(
            f"Indian Art and Culture topics missing from catalog: {missing}"
        )


def _write_graphical_spec(
    config: dict[str, object],
    markdown: str,
    ascii_path: Path,
) -> Path:
    """Author a 13-stage subject-specific spec without rendering artifacts."""

    panels = [
        {
            "title": title,
            "body": body,
            "structural_type": kind,
            "source_references": references,
        }
        for title, kind, body, references in config["panels"]
    ]
    source_path = SESSION_DIR / f"{config['key']}_Learning-Session.md"
    spec = carvaka_flowchart.author_topic_spec(
        topic_key=str(config["key"]),
        subject="World-History",
        title=str(config["title"]),
        source_markdown=markdown.replace("…", ""),
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ascii_path.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ascii_path.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=1,
    )
    spec["subject"] = SUBJECT
    enrichment = spec["stages"][-1]["groups"]
    labels = (
        ("OPTIONAL SOURCE DEPTH", "evidence"),
        ("ATTRIBUTION / INTERPRETIVE LIMIT", "caution"),
        ("COMPARATIVE HERITAGE NUANCE", "comparison"),
    )
    for group, (heading, role) in zip(enrichment, labels):
        group["heading"] = heading
        group["role"] = role
    errors = carvaka_flowchart.validate_spec(spec)
    if errors:
        raise carvaka_flowchart.CarvakaError(
            f"{config['key']}: subject-specific graphical spec failed: "
            + " | ".join(errors)
        )
    if len(spec["stages"]) != 13:
        raise ValueError(f"{config['key']}: graphical master must contain 13 stages.")
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{config['key']}.json"
    output.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


@contextmanager
def _configured() -> Iterator[None]:
    names = {
        "ROOT": ROOT,
        "DATE": DATE,
        "SUBJECT": SUBJECT,
        "KNOWLEDGE": KNOWLEDGE,
        "SESSION_DIR": SESSION_DIR,
        "GRAPHICAL_DIR": GRAPHICAL_DIR,
        "EXPORT_DIR": EXPORT_DIR,
        "CATALOG": CATALOG,
        "SECTION_MANIFEST": SECTION_MANIFEST,
        "LOCAL_BOOKS": LOCAL_BOOKS,
        "COMMON_CROSS": COMMON_CROSS,
        "PYQ_INDEXES": PYQ_INDEXES,
        "ensure_section_manifest": ensure_section_manifest,
        "validate_catalog": validate_catalog,
        "write_graphical_spec": _write_graphical_spec,
        "_owner_depth": _full_owner_depth,
        "_session_fragment": _session_fragment,
        "solved_pyq_section": _audited_pyq_section,
    }
    previous = {name: getattr(_base, name) for name in names}
    try:
        for name, value in names.items():
            setattr(_base, name, value)
        yield
    finally:
        for name, value in previous.items():
            setattr(_base, name, value)


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    with _configured():
        _base.self_check(
            config,
            markdown,
            workbook,
            session_count,
            graphical_path,
        )


def run_batch(
    *,
    topics: list[dict[str, object]],
    ascii_path: Path,
    scope: str,
    previous: ModuleType | None = None,
    previous_keys: list[str] | None = None,
) -> int:
    """Run one single-writer authoring batch without rendering or finalising."""

    with _configured():
        return _base.run_batch(
            topics=topics,
            ascii_path=ascii_path,
            scope=scope,
            previous=previous,
            previous_keys=previous_keys,
        )
