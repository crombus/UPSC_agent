"""Shared authoring-only engine for Economy learner-v2 topics.

The engine follows the International Relations, Social Justice and Governance
single-writer workflow while enforcing Economy-specific precision: every
estimate keeps its period and vintage, every price index keeps its base year
and basket, every agricultural instrument keeps its crop, geography,
eligibility and implementation stage, and every regulator or safety net keeps
its legal perimeter and stock-flow boundary.
"""

from __future__ import annotations

import hashlib
import json
import re
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType
from typing import Iterable, Iterator

import carvaka_flowchart
import generate_v2_section_indexes as section_indexes
import generate_world_history_common as _base
import notions_style_ascii_master as ascii_master


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-03"
SUBJECT = "Economy"
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
    ROOT / "upsc-ai-kit" / "manifests" / "v2" / "economy--subject-wide-syllabus.json"
)
LOCAL_BOOKS = [
    ROOT / "books" / "mains" / "03 UPSC 2024 Paper-III.pdf",
    ROOT / "books" / "mains" / "UPSC Mains 2025 GS Paper 3 3.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM19-GeneralStudies-III.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-21-GENSTUDIESPAPER-III-110122.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-22-GENERAL-STUDIES-PAPER-III-190922.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSM-23-GENERAL-STUDIES-PAPER-III-180923.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSP-18-GS-I-C.pdf",
    ROOT / "books" / "more_previous_papers" / "CSP_2020_GS_Paper-1.pdf",
    ROOT
    / "books"
    / "more_previous_papers"
    / "QP-CSP-21-GeneralStudiesPaper-I-121021.pdf",
]
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Framework.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md",
    KNOWLEDGE / "REVISION-CHART_Mechanisms-Sectors-and-Distinctive-Features.md",
    KNOWLEDGE / "ANSWER-WORTHINESS-AUDIT.md",
]
COMMON_CROSS = [path for path in COMMON_CROSS if path.is_file()]
PYQ_INDEXES = [
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2026.md",
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]

_BASE_OWNER_DEPTH = _base._owner_depth
_PLAN_INDEXES = (
    [0, 1],
    [2],
    [3],
    [4],
    [5],
    [6, 7],
    [8],
    [9],
    [10],
    [11],
    [12, 13],
    [14],
    [15],
    [16, 17],
    [18, 19],
)
_KEYWORD_EXCLUSIONS = {
    "about", "after", "against", "analysis", "answer", "because", "before",
    "between", "claim", "concept", "current", "different", "economy",
    "economic", "evidence", "exact", "fact", "india", "indian", "limit",
    "limits", "measure", "measurement", "named", "owner", "policy", "question", "source", "topic",
    "which", "while", "with", "without",
}


def make_plans(
    titles: list[str],
    traps: list[str],
    answer_routes: list[str],
) -> list[tuple[str, list[int], str, str]]:
    if len(titles) != 15:
        raise ValueError("Exactly fifteen Economy session titles are required.")
    return [
        (
            title,
            list(_PLAN_INDEXES[index]),
            traps[index % len(traps)],
            answer_routes[index % len(answer_routes)],
        )
        for index, title in enumerate(titles)
    ]


def make_mains(
    facts: list[tuple[str, str]],
    prompts: list[tuple[int, str, list[int]]],
) -> list[tuple[int, str, str, list[int]]]:
    result = []
    for marks, prompt, indexes in prompts:
        selected = [facts[index] for index in indexes]
        model = " ".join(
            (
                f"**Claim:** {label}. **Named evidence/example:** {statement} "
                "**Analysis:** This identifies the economic mechanism, the "
                "relevant institution or accounting boundary, and the effect on "
                "output, prices, distribution or financial stability. "
                "**Qualification:** The conclusion must retain the stated "
                "period, estimate vintage, base year, basket, instrument "
                "eligibility, crop and geography scope, implementation stage, "
                "stock-flow distinction or legal perimeter rather than "
                "generalise beyond the source."
            )
            for label, statement in selected
        )
        result.append((marks, prompt, model, indexes))
    return result


def make_pyq_solution(
    facts: list[tuple[str, str]],
    year: str,
    paper: str,
    demand: str,
    status: str,
    indexes: list[int],
) -> tuple[str, str, str, str, str]:
    model = " ".join(
        f"**{facts[index][0]}:** {facts[index][1]}" for index in indexes
    )
    model += (
        " The answer therefore separates definition, mechanism, evidence and "
        "limitation, and does not infer an official model answer or objective key."
    )
    return year, paper, demand, status, model


def _session_keywords(
    title: str,
    selected: list[tuple[str, str]],
) -> list[str]:
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
        raise ValueError(f"{title}: fewer than four Economy-specific keywords.")
    return result


def _session_fragment(
    config: dict[str, object],
    number: int,
    session_plan: tuple[str, list[int], str, str],
) -> str:
    title, indexes, caution, exam_use = session_plan
    facts: list[tuple[str, str]] = config["facts"]
    selected = [facts[index] for index in indexes]
    labels = [label for label, _ in selected]
    joined = ", ".join(labels[:-1]) + (
        f" and {labels[-1]}" if len(labels) > 1 else labels[0]
    )
    evidence = "\n".join(f"- {statement}" for _, statement in selected)
    core = " ".join(statement for _, statement in selected)
    keywords = _session_keywords(title, selected)
    return (
        f"### SESSION {number} — {_base.phase_for(number)} — {title}\n\n"
        "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        f"**Plain-language definition:** {title} explains how {joined} fit into "
        "one examinable economic mechanism.\n\n"
        f"**Technical definition:** In Economy analysis, {title} separates the "
        "concept and accounting boundary from its unit, coverage, price basis, "
        "base year or basket, estimate vintage, institutional or legal source, "
        "crop and geography scope, eligibility, implementation stage, "
        "stock-flow boundary, transmission channel and distributional or "
        "stability consequence.\n\n"
        "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        f"> {title} must be read through {joined}, with the formula or legal "
        "perimeter stated before the policy inference.\n\n"
        "#### MUST-WRITE KEYWORDS\n\n"
        + "\n".join(f"- **{item}**" for item in keywords)
        + "\n\n"
        f"**How to use them:** Define {', '.join(keywords[:3])}; attach "
        f"{keywords[3]} to its named source, period and status; then qualify the "
        f"answer with this limit: {caution}\n\n"
        + _base._session_visual(title, labels, caution)
        + "\n\n#### CORE EXPLANATION\n\n"
        + core
        + "\n\n#### NAMED EVIDENCE AND MECHANISM\n\n"
        + evidence
        + "\n\n#### EXAMINER CAUTION\n\n"
        + f"- {caution}\n\n"
        + "#### EXAM LINK\n\n"
        + "- **Prelims:** Preserve the exact formula, territorial or resident "
        "boundary, price basis, base year, index basket, eligible counterparty, "
        "institution and legal status; never upgrade a projection into an actual "
        "or a regulatory direction into a universal rule.\n"
        + f"- **Mains:** {exam_use}\n\n"
        + "#### MINI RECAP\n\n"
        + f"- **Mechanism chain:** {' -> '.join(labels)}\n"
        + f"- **Qualified use:** {exam_use}\n\n"
        + "#### CLOSING RECALL FLOW\n\n"
        + "```closure-flow\n"
        + f"START / CONCEPT: {title}\n"
        + f"EXACT TERMS: {' | '.join(keywords)}\n"
        + f"MECHANISM / ARGUMENT: connect {joined} through accounting, incentives and transmission\n"
        + f"CONSEQUENCE / CONTRAST: {exam_use}\n"
        + f"UPSC TRAP / ANSWER-USE: {caution}\n"
        + f"ANSWER-GRABBING FORMULATION: {title} converts a precise economic distinction into a qualified conclusion\n"
        + "```"
    )


def topic(
    number: int,
    title: str,
    source_stem: str,
    canonical_name: str,
    facts: list[tuple[str, str]],
    traps: list[str],
    mains_prompts: list[tuple[int, str, list[int]]],
    session_titles: list[str],
    answer_routes: list[str],
    panels: list[tuple[str, str, str, list[str]]],
    required_terms: list[str],
    pyq_note: str,
    pyq_solutions: list[tuple[str, str, str, str, str]],
    live_sources: Iterable[str],
    current_note: str,
    extra: Iterable[str] = (),
    pyq_audit_heading: str | None = None,
    allow_existing_history: bool = False,
) -> dict[str, object]:
    return {
        "number": number,
        "key": f"economy-{number:02d}",
        "title": title,
        "basic": KNOWLEDGE / "basic" / f"{source_stem}.md",
        "advanced": KNOWLEDGE / "advanced" / f"{source_stem}.md",
        "canonical": KNOWLEDGE / canonical_name,
        "extra": [KNOWLEDGE / value for value in extra],
        "facts": facts,
        "traps": traps,
        "mains": make_mains(facts, mains_prompts),
        "session_plans": make_plans(session_titles, traps, answer_routes),
        "panels": panels,
        "required_terms": required_terms,
        "live_sources": list(live_sources),
        "current_note": current_note,
        "ocr_note": (
            "Repository Markdown was primary. OCR-searchable local official "
            "General Studies papers were used only to confirm printed routed "
            "demands. No answer key, marking scheme, unsupported page precision "
            "or current macroeconomic statistic was inferred from them."
        ),
        "pyq_note": pyq_note,
        "pyq_solutions": pyq_solutions,
        "pyq_audit_heading": pyq_audit_heading,
        "allow_existing_history": allow_existing_history,
    }


def _build_mcqs(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    variants = [
        "Which statement correctly identifies {label}?",
        "Which option preserves the accounting or regulatory boundary of {label}?",
        "Which statement uses {label} without losing its vintage, basket or legal status?",
        "Which option avoids the standard UPSC close-option trap about {label}?",
    ]
    blocks = []
    for fact_index, (label, statement) in enumerate(facts):
        for variant_index, template in enumerate(variants):
            number = fact_index * 4 + variant_index + 1
            answer = "ABCD"[(number - 1) % 4]
            distractors = [
                facts[(fact_index + variant_index + offset) % len(facts)][1]
                for offset in (1, 2, 3)
            ]
            choices = {answer: statement}
            for letter, distractor in zip(
                [letter for letter in "ABCD" if letter != answer],
                distractors,
            ):
                choices[letter] = distractor
            blocks.append(
                f"### Q{number}. {template.format(label=label)}\n\n"
                + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
                + f"\n\n**Answer: {answer}.**\n"
                + f"**Explanation:** {statement} The other options belong to "
                "different measures, vintages, baskets, instruments, institutions "
                "or legal perimeters."
            )
    return "\n\n".join(blocks)


def _full_owner_depth(path: Path, *, exclude_pyq: bool) -> str:
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
            "### TRANSPARENT OBJECTIVE-ONLY PYQ AUDIT"
            if not config["pyq_solutions"]
            else "### VERIFIED PYQ OWNERSHIP AUDIT"
        )
    )
    text = f"{heading}\n\n{config['pyq_note']}"
    if pyq_blocks:
        text += "\n\n### OWNER PYQ LEDGER EXTRACTS\n\n" + "\n\n".join(pyq_blocks)
    for number, (year, paper, demand, status, model) in enumerate(
        config["pyq_solutions"], 1
    ):
        text += (
            f"\n\n### PYQ DEMAND CARD {number} — {year} {paper}\n\n"
            f"**Demand:** {demand}\n\n**Status:** {status}\n\n"
            f"**Model solution:** {model}"
        )
    return text


def ensure_section_manifest() -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    target = next(
        item for item in catalog["topics"] if item.get("topic_key") == "economy-01"
    )
    path = section_indexes.materialize_catalog_section_manifest(ROOT, catalog, target)
    if path != SECTION_MANIFEST:
        raise ValueError(f"Unexpected Economy manifest path: {path}")
    return path


def validate_catalog(topics: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [config["key"] for config in topics if config["key"] not in keys]
    if missing:
        raise ValueError(f"Economy topics missing from catalogue: {missing}")


def _write_graphical_spec(
    config: dict[str, object],
    markdown: str,
    ascii_path: Path,
) -> Path:
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
        subject=SUBJECT,
        title=str(config["title"]),
        source_markdown=markdown.replace("…", ""),
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ascii_path.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ascii_path.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=1,
    )
    errors = carvaka_flowchart.validate_spec(spec)
    if errors:
        raise carvaka_flowchart.CarvakaError(" | ".join(errors))
    if len(spec["stages"]) != 13:
        raise ValueError(f"{config['key']}: expected thirteen graphical stages.")
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{config['key']}.json"
    output.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


REGISTER_HEADINGS = (
    "RAPID CONCEPT, INSTITUTION AND STATUS MAP",
    "SCOPE, ELIGIBILITY, STOCK-FLOW AND IMPLEMENTATION TRAPS",
    "ANSWER-WRITING SPINE",
    "LIVE-SOURCE, VINTAGE AND EVIDENCE BOUNDARY",
)


def _register_notes(config: dict[str, object]) -> str:
    facts = "\n".join(
        f"{number}. **{label}:** {statement}"
        for number, (label, statement) in enumerate(config["facts"], 1)
    )
    traps = "\n".join(f"- {trap}" for trap in config["traps"])
    return (
        f"### {config['title']}: {REGISTER_HEADINGS[0]}\n\n{facts}\n\n"
        f"### {config['title']}: {REGISTER_HEADINGS[1]}\n\n{traps}\n\n"
        f"### {config['title']}: {REGISTER_HEADINGS[2]}\n\n"
        "```text\n"
        "DEFINE THE MEASURE OR INSTITUTION AND FIX ITS COVERAGE\n"
        "-> STATE FORMULA, CROP, GEOGRAPHY, ELIGIBILITY OR LEGAL POWER\n"
        "-> NAME THE PERIOD, ESTIMATE VINTAGE AND ISSUING BODY\n"
        "-> SEPARATE ANNOUNCEMENT, IMPLEMENTATION, STOCK AND FLOW OUTCOMES\n"
        "-> ADD ONE INDIA-SPECIFIC EVIDENCE UNIT AND ITS LIMIT\n"
        "-> TEST DISTRIBUTION, OUTPUT, PRICE OR FINANCIAL-STABILITY EFFECTS\n"
        "-> CONCLUDE WITH A GRADED VERDICT, NOT A TIMELESS NUMBER\n"
        "```\n\n"
        f"### {config['title']}: {REGISTER_HEADINGS[3]}\n\n"
        f"{config['current_note']}"
    )


def _live_source_audit(config: dict[str, object]) -> str:
    lines = "\n".join(f"- {item}" for item in config["live_sources"])
    return (
        "### LIVE OFFICIAL-SOURCE ATTEMPT LOG\n\n"
        "The checks below were made on 2026-09-03. Substantive official text is "
        "used only for the proposition it actually supports; binary files, "
        "dynamic shells, stubs and undated dashboard snippets are recorded but "
        "not converted into current claims.\n\n"
        f"{lines}"
    )


def _assemble(
    config: dict[str, object],
    ascii_path: Path,
) -> tuple[str, str, int]:
    sessions = [
        _session_fragment(config, number, plan)
        for number, plan in enumerate(config["session_plans"], 1)
    ]
    mcqs = _build_mcqs(config)
    pyq_blocks = _base.extract_pyq_blocks(config)
    practice = (
        _audited_pyq_section(config, pyq_blocks)
        + "\n\n"
        + _base.original_mains_section(config)
    )
    manual = ascii_master.normalize_manual_spec_file(ascii_path)
    ascii_fragment = ascii_master.build_manual_fragment(manual[str(config["key"])])
    markdown = (
        f"# {config['title']} — Learner-v2 Complete Learning Session\n\n"
        f"> **Authoring-only generation:** {DATE}. No PDF was rendered and no "
        "tracker or index was mutated.\n\n"
        + _base.source_audit(config)
        + "\n\n"
        + _live_source_audit(config)
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
        f"> **Authoring-only generation:** {DATE}. Uses the same source-bounded "
        "Economy distinctions and strict A-B-C-D rotation.\n\n"
        "## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n"
    )
    return markdown, workbook, len(sessions)


def _write_generation_spec(
    config: dict[str, object],
    source_path: Path,
    workbook_path: Path,
    graphical_path: Path,
    ascii_path: Path,
) -> Path:
    sources = [
        Path(config["basic"]),
        Path(config["advanced"]),
        Path(config["canonical"]),
        *[Path(path) for path in config["extra"]],
        source_path,
        workbook_path,
        SECTION_MANIFEST,
        CATALOG,
        ascii_path,
        graphical_path,
        *COMMON_CROSS,
        *PYQ_INDEXES,
        *LOCAL_BOOKS,
    ]
    sources = list(dict.fromkeys(sources))
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing Economy sources: " + ", ".join(missing))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        item for item in catalog["topics"] if item.get("topic_key") == config["key"]
    )
    payload = {
        "schema_version": 1,
        "topic_key": config["key"],
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "topic_folder": config["key"],
        "title": config["title"],
        "variant": "learner-v2",
        "generation": 1,
        "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "source_markdown": str(source_path.relative_to(ROOT)),
        "workbook_markdown": str(workbook_path.relative_to(ROOT)),
        "source_basic": str(Path(config["basic"]).relative_to(ROOT)),
        "source_canonical": str(Path(config["canonical"]).relative_to(ROOT)),
        "source_advanced": str(Path(config["advanced"]).relative_to(ROOT)),
        "manifest": str(SECTION_MANIFEST.relative_to(ROOT)),
        "cross_topic_sources": [
            str(path.relative_to(ROOT))
            for path in [*COMMON_CROSS, *map(Path, config["extra"])]
        ],
        "local_ocr_sources": [str(path.relative_to(ROOT)) for path in LOCAL_BOOKS],
        "pyq_indexes": [str(path.relative_to(ROOT)) for path in PYQ_INDEXES],
        "official_question_sources": [],
        "live_sources": config["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": (
            "80 unique MCQs with A/B/C/D at 20 each; verified routed PYQ "
            "demands; six solved original Mains answers weighted "
            "10,10,15,15,20,20; final topic-specific register notes."
        ),
        "pyq_status_note": config["pyq_note"],
        "current_linkage_note": config["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "supersedes": None,
        "tracker_untouched": True,
        # Correct for Topic 01: legacy-v1 history alone does not require the
        # learner-v2 regeneration path. Existing learner-v2 history would.
        "allow_existing_history": bool(config["allow_existing_history"]),
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{config['key']}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
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
        "write_generation_spec": _write_generation_spec,
        "assemble": _assemble,
        "build_mcqs": _build_mcqs,
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
        _base.self_check(config, markdown, workbook, session_count, graphical_path)


def run_batch(
    *,
    topics: list[dict[str, object]],
    ascii_path: Path,
    scope: str,
    previous: ModuleType | None = None,
    previous_keys: list[str] | None = None,
) -> int:
    with _configured():
        return _base.run_batch(
            topics=topics,
            ascii_path=ascii_path,
            scope=scope,
            previous=previous,
            previous_keys=previous_keys,
        )
