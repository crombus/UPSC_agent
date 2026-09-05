"""Shared authoring-only engine for Social Justice learner-v2 batches.

The engine reuses the proven Indian Society / Governance learner-v2 architecture:
one assembled learner-facing Markdown per topic, twenty source-bounded fact
anchors, fifteen visual-first sessions, eighty unique MCQs on a strict A-B-C-D
cycle, six solved original Mains answers weighted 10/10/15/15/20/20, twelve
manually authored ASCII panels and a thirteen-stage graphical master spec. It
never renders a PDF, never mutates `EXPORT-PDF-STATUS.json` and never touches an
index.

Social Justice adds one subject-specific discipline that the engine enforces in
wording: every session, register heading and boundary note keeps rights, schemes,
administrative delivery, measured outcomes and analytical recommendations apart,
and every volatile poverty, nutrition, health or education indicator is carried
with its issuing body, edition or round and status date.
"""

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
import notions_style_ascii_master as ascii_master
import carvaka_flowchart


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-02"
SUBJECT = "Social-Justice"
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
    / "social-justice--subject-wide-syllabus.json"
)
# OCR-searchable official General Studies question papers held locally. They are
# read only to confirm the printed wording of a routed PYQ demand. No official
# answer key, marking scheme or page precision is imported from them, and no
# question is invented from them.
LOCAL_BOOKS = [
    ROOT / "books" / "mains" / "02 UPSC 2024 Paper-II.pdf",
    ROOT / "books" / "mains" / "UPSC Mains 2025 GS Paper 2.pdf",
    ROOT / "books" / "mains" / "UPSC Mains 2025 GS Paper 1.pdf",
    ROOT / "books" / "mains" / "UPSC Mains 2024 GS Paper I.pdf",
    ROOT / "books" / "more_previous_papers" / "GENERAL-STUDIES-PAPER-I.pdf",
    ROOT / "books" / "more_previous_papers" / "GENERAL-STUDIES-PAPER-II.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM19-GeneralStudies-II.pdf",
    ROOT / "books" / "more_previous_papers" / "Gen_St_P2.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-21-GENSTUDIESPAPER-II-110122.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-22-GENERAL-STUDIES-PAPER-II-190922.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-23-GENERAL-STUDIES-PAPER-II-180923.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSP-18-GS-I-C.pdf",
]
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Framework.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md",
    KNOWLEDGE / "REVISION-CHART_Rights-Capabilities-and-Distinctive-Features.md",
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
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]

_BASE_OWNER_DEPTH = _base._owner_depth

_KEYWORD_EXCLUSIONS = {
    "about",
    "across",
    "after",
    "against",
    "already",
    "always",
    "analysis",
    "answer",
    "because",
    "before",
    "between",
    "boundary",
    "build",
    "cannot",
    "claim",
    "classification",
    "concept",
    "context",
    "current",
    "definition",
    "different",
    "effect",
    "evidence",
    "exact",
    "fact",
    "factor",
    "feature",
    "final",
    "framework",
    "further",
    "impact",
    "india",
    "indian",
    "inference",
    "instead",
    "justice",
    "limit",
    "limits",
    "link",
    "merely",
    "method",
    "never",
    "note",
    "notes",
    "often",
    "owner",
    "prepare",
    "process",
    "question",
    "rather",
    "roadmap",
    "route",
    "routing",
    "should",
    "social",
    "source",
    "stage",
    "status",
    "supporting",
    "their",
    "there",
    "through",
    "topic",
    "toward",
    "trap",
    "traps",
    "under",
    "verified",
    "where",
    "which",
    "while",
    "within",
    "without",
}


def _session_keywords(
    title: str,
    selected: list[tuple[str, str]],
) -> list[str]:
    """Select six compact, topic-specific terms for semantic navigation."""

    source = " ".join(
        [title, *[label for label, _ in selected], *[text for _, text in selected]]
    )
    result: list[str] = []
    seen: set[str] = set()
    for word in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", source):
        folded = word.casefold().strip("-'")
        if folded in _KEYWORD_EXCLUSIONS or folded in seen:
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
        f"{joined} fit into one examinable social-justice relationship."
    )
    technical = (
        f"In social-justice analysis, {title} denotes the source-bounded relation "
        f"among {joined}, described by the entitlement or claim that is asserted, "
        "the legal, statutory or purely administrative form that carries it, the "
        "delivery mechanism that is supposed to convert it into access, the "
        "measured outcome by which the conversion is tested, and the remedy or "
        "recommendation that follows when the conversion fails."
    )
    keywords = _session_keywords(title, selected)
    mapped_terms = ", ".join(keywords[:3])
    evidence_term = keywords[3]
    guidance = (
        f"Define {mapped_terms}; cite {evidence_term} as named evidence with its "
        f"issuing body and dated edition or round; then apply this qualification: "
        f"{caution} Conclude by showing how the distinction supports this answer "
        f"route: {exam_use}"
    )
    fragment = (
        f"### SESSION {number} — {_base.phase_for(number)} — {title}\n\n"
        "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        f"**Plain-language definition:** {plain}\n\n"
        f"**Technical definition:** {technical}\n\n"
        "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        f"> {title} should be analysed as a relation among {joined}, separating "
        "the right claimed, the scheme that carries it, the delivery that reaches "
        "a person and the outcome that is actually measured.\n\n"
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
        + f"- **Prelims:** Retain the exact statute, section, article, ministry, "
        f"official category, survey round or dated edition attached to {title}, "
        "and never upgrade a policy document into a statute or a targeted scheme "
        "into a universal entitlement.\n"
        + f"- **Mains:** {exam_use}\n\n"
        + "#### MINI RECAP\n\n"
        + f"- **Evidence chain:** {' -> '.join(labels)}\n"
        + f"- **Qualified use:** {exam_use}\n\n"
        + "#### CLOSING RECALL FLOW\n\n"
        + "```closure-flow\n"
        + f"START / CONCEPT: {title}\n"
        + f"EXACT TERMS: {' | '.join(keywords)}\n"
        + f"MECHANISM / ARGUMENT: relate {joined} through claim, carrying instrument, delivery and measured outcome\n"
        + f"CONSEQUENCE / CONTRAST: This relation supports the answer route that {exam_use[0].lower() + exam_use[1:]}\n"
        + f"UPSC TRAP / ANSWER-USE: LIMIT: {caution}\n"
        + f"ANSWER-GRABBING FORMULATION: {title} converts a dated official entitlement or indicator into a qualified capability argument\n"
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
    pyq_audit_heading: str | None = None,
) -> dict[str, object]:
    """Create one Social Justice topic configuration.

    `pyq_audit_heading` exists because an owner can carry a verified routed
    objective demand while carrying no solved Mains demand card. Calling that
    state a zero-PYQ audit would misdescribe the ledger, so such an owner names
    its own audit heading instead of inheriting the zero/solved default.
    """

    return {
        "number": number,
        "key": f"social-justice-{number:02d}",
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
            "No additional live official item was verified for this topic on "
            "2026-09-02. Only the dated official anchors already carried by the "
            "repository owners are used, each with its issuing body, edition or "
            "survey round and status date. The package invents no poverty, "
            "nutrition, health or education indicator, no National Family Health "
            "Survey, Periodic Labour Force Survey, National Sample Survey, NITI "
            "Aayog or Sustainable Development Goal figure, no scheme eligibility "
            "rule or coverage count, no budget or expenditure number, no legal or "
            "constitutional entitlement, no institutional mandate, no policy "
            "status, no previous-year question, answer key or date, and no "
            "current finding."
        ),
        "ocr_note": (
            "Repository Markdown was primary. The OCR-searchable official General "
            "Studies question papers held under books\\mains and "
            "books\\more_previous_papers were read only to confirm the printed "
            "wording of routed Mains demands. No official answer key, marking "
            "scheme, page precision or unsupported quotation was imported from "
            "them."
        ),
        "pyq_note": pyq_note,
        "pyq_solutions": pyq_solutions,
        "pyq_audit_heading": pyq_audit_heading,
    }


def _full_owner_depth(path: Path, *, exclude_pyq: bool) -> str:
    """Preserve the complete owner while lowering its headings for assembly."""

    return _BASE_OWNER_DEPTH(path, exclude_pyq=False)


def _audited_pyq_section(
    config: dict[str, object],
    pyq_blocks: list[str],
) -> str:
    override = config.get("pyq_audit_heading")
    heading = (
        f"### {override}"
        if override
        else (
            "### TRANSPARENT ZERO-DIRECT-PYQ AUDIT"
            if not config["pyq_solutions"]
            else "### VERIFIED PYQ OWNERSHIP AUDIT"
        )
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
        if item.get("topic_key") == "social-justice-01"
    )
    path = section_indexes.materialize_catalog_section_manifest(
        ROOT,
        catalog,
        target,
    )
    if path != SECTION_MANIFEST:
        raise ValueError(f"Unexpected Social Justice manifest path: {path}")
    return path


def validate_catalog(topics: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [config["key"] for config in topics if config["key"] not in keys]
    if missing:
        raise ValueError(f"Social Justice topics missing from catalog: {missing}")


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
        subject="Indian-Society",
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
        ("OPTIONAL RIGHTS AND CAPABILITY DEPTH", "evidence"),
        ("INDICATOR, ROUND AND STATUS LIMIT", "caution"),
        ("COMPARATIVE WELFARE-DESIGN NUANCE", "comparison"),
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


REGISTER_HEADINGS = (
    "RAPID RIGHT, SCHEME AND MEASURED-OUTCOME MAP",
    "CLOSE-OPTION AND ENTITLEMENT TRAPS",
    "ANSWER-WRITING SPINE",
    "DATED-INDICATOR AND STATUS BOUNDARY",
)


def _register_notes(config: dict[str, object]) -> str:
    """Compressed, topic-specific consolidated register notes."""

    facts = "\n".join(
        f"{number}. **{label}:** {statement}"
        for number, (label, statement) in enumerate(config["facts"], 1)
    )
    traps = "\n".join(f"- {trap}" for trap in config["traps"])
    return (
        f"### {config['title']}: {REGISTER_HEADINGS[0]}\n\n"
        f"{facts}\n\n"
        f"### {config['title']}: {REGISTER_HEADINGS[1]}\n\n"
        f"{traps}\n\n"
        f"### {config['title']}: {REGISTER_HEADINGS[2]}\n\n"
        "```text\n"
        "NAME THE DEPRIVATION OR CLAIM -> IDENTIFY THE RIGHT-HOLDER AND THE DUTY-BEARER\n"
        "-> SEPARATE THE CONSTITUTIONAL OR STATUTORY ENTITLEMENT FROM THE SCHEME THAT CARRIES IT\n"
        "-> TRACE ADMINISTRATIVE DELIVERY: IDENTIFICATION, ENROLMENT, ACCESS, QUALITY\n"
        "-> TEST THE MEASURED OUTCOME AGAINST THE INPUT, NAMING SURVEY, ROUND AND YEAR\n"
        "-> SEPARATE INCLUSION ERROR FROM EXCLUSION ERROR AND COVERAGE FROM CAPABILITY\n"
        "-> CLOSE WITH A GRADED VERDICT AND AN EXPLICIT INDICATOR OR STATUS CAVEAT\n"
        "```\n\n"
        f"### {config['title']}: {REGISTER_HEADINGS[3]}\n\n"
        f"{config['current_note']}"
    )


def _assemble(
    config: dict[str, object],
    ascii_path: Path,
) -> tuple[str, str, int]:
    """Assemble the learner-v2 Markdown with register notes preserved.

    The shared refresh pipeline rebuilds the terminal ASCII atlas by truncating
    everything from `### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM` to the end of
    the document. Authoring the consolidated register notes *before* that
    heading keeps the complete register content inside the final H2 after
    publication, instead of letting it be silently dropped.
    """

    sessions = [
        _session_fragment(config, number, plan)
        for number, plan in enumerate(config["session_plans"], 1)
    ]
    mcqs = _base.build_mcqs(config)
    pyq_blocks = _base.extract_pyq_blocks(config)
    practice = (
        _audited_pyq_section(config, pyq_blocks)
        + "\n\n"
        + _base.original_mains_section(config)
    )
    manual = ascii_master.normalize_manual_spec_file(ascii_path)
    ascii_fragment = ascii_master.build_manual_fragment(
        manual[str(config["key"])]
    )
    markdown = (
        f"# {config['title']} — Learner-v2 Complete Learning Session\n\n"
        f"> **Authoring-only generation:** {DATE}. No PDF was rendered and no "
        "tracker or index was mutated.\n\n"
        + _base.source_audit(config)
        + "\n\n## BASIC LEARNING SESSION\n\n"
        + "\n\n".join(sessions)
        + "\n\n### COMPLETE BASIC OWNER EVIDENCE BANK\n\n"
        + _full_owner_depth(Path(config["basic"]), exclude_pyq=True)
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + _full_owner_depth(Path(config["advanced"]), exclude_pyq=True)
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + _register_notes(config)
        + "\n\n### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + ascii_fragment
        + "\n"
    )
    workbook = (
        f"# {config['title']} — Solved Practice Workbook\n\n"
        f"> **Authoring-only generation:** {DATE}. Uses the same verified "
        "ownership and strict A-B-C-D rotation as the learning source.\n\n"
        "## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n"
    )
    return markdown, workbook, len(sessions)


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
        "assemble": _assemble,
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
