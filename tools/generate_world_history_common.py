"""Shared authoring-only engine for sequential World History learner-v2 batches."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from types import ModuleType
from typing import Iterable

import carvaka_flowchart
import generate_modern_history_03_04_sequential as session_common
import generate_v2_section_indexes as section_indexes
import notions_style_ascii_master as ascii_master


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-01"
SUBJECT = "World-History"
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
    / "world-history--subject-wide-syllabus.json"
)
LOCAL_BOOKS = [
    ROOT / "books" / "WORLD HISTORY -- NORMAN LOWE -- ENGLISH  ##.pdf",
]
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Chronology.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md",
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
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]


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
    """Create one World History topic configuration."""

    return {
        "number": number,
        "key": f"world-history-{number:02d}",
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
            "No verified live current-affairs item is pegged to this historical "
            "topic in the repository owners. The package therefore uses the "
            "bounded phrase 'no verified live item' rather than inventing a "
            "headline, date, institution or contemporary linkage."
        ),
        "ocr_note": (
            "Repository Markdown was used first. The available OCR-searchable "
            "Norman Lowe World History PDF was retained as supplementary local "
            "context, but no unsupported page number, quotation or precision "
            "was imported from it."
        ),
        "pyq_note": pyq_note,
        "pyq_solutions": pyq_solutions,
    }


def split_h2(markdown: str) -> tuple[str, list[tuple[str, str]]]:
    return session_common.split_h2(markdown)


def lower_headings(markdown: str) -> str:
    return session_common.lower_headings(markdown)


def phase_for(number: int) -> str:
    if number <= 3:
        return "FOUNDATION"
    if number >= 13:
        return "CORE SYNTHESIS"
    return "CORE"


def _session_visual(
    title: str,
    labels: list[str],
    caution: str,
) -> str:
    visual_lines = [title.upper()]
    for index, label in enumerate(labels, 1):
        visual_lines.append(f"{index:02d}. {label}")
        if index < len(labels):
            visual_lines.append("    |")
            visual_lines.append("    v")
    visual_lines.append(f"BOUNDARY -> {caution}")
    return (
        "#### VISUAL FIRST\n\n"
        "```text\n"
        + "\n".join(visual_lines)
        + "\n```\n\n"
        "*This topic-specific rail fixes the evidence sequence and its "
        "exam boundary before analysis.*"
    )


def _session_fragment(
    config: dict[str, object],
    number: int,
    plan: tuple[str, list[int], str, str],
) -> str:
    title, indexes, caution, exam_use = plan
    facts: list[tuple[str, str]] = config["facts"]
    selected = [facts[index] for index in indexes]
    labels = [label for label, _ in selected]
    evidence = "\n".join(f"- {statement}" for _, statement in selected)
    core = " ".join(statement for _, statement in selected)
    definition = (
        f"{title} is the source-bounded relationship among "
        + ", ".join(labels[:-1])
        + (f" and {labels[-1]}" if labels else "")
        + f" within {config['title']}."
    )
    fragment = (
        f"## {title}\n\n"
        + _session_visual(title, labels, caution)
        + "\n\n#### CONCEPT DEFINITIONS\n\n"
        + f"- **Precise definition:** {definition}\n"
        + "- **Classification:** Historical facts below are source-backed; "
        "causal weight and evaluative verdicts are analytical synthesis.\n\n"
        + "#### CORE EXPLANATION\n\n"
        + core
        + "\n\n#### NAMED EVIDENCE AND MECHANISM\n\n"
        + evidence
        + "\n\n#### EXAMINER CAUTION\n\n"
        + f"- {caution}\n\n"
        + "#### EXAM LINK\n\n"
        + f"- **Prelims:** Retain the exact actor, date, document and category in {title}.\n"
        + f"- **Mains:** {exam_use}\n\n"
        + "#### MINI RECAP\n\n"
        + f"- **Evidence chain:** {' -> '.join(labels)}\n"
        + f"- **Qualified use:** {exam_use}"
    )
    return session_common.session_fragment(fragment, number, phase_for(number))


def _owner_depth(path: Path, *, exclude_pyq: bool) -> str:
    text = path.read_text(encoding="utf-8")
    preface, sections = split_h2(text)
    retained = []
    for title, fragment in sections:
        if exclude_pyq and "PYQ" in title.upper():
            continue
        retained.append(lower_headings(fragment))
    preface_lines = [
        line
        for line in preface.splitlines()
        if not line.startswith("# ") and line.strip() != "---"
    ]
    pieces = ["\n".join(preface_lines).strip(), *retained]
    return "\n\n".join(piece for piece in pieces if piece)


def extract_pyq_blocks(config: dict[str, object]) -> list[str]:
    blocks: list[str] = []
    for owner in (Path(config["basic"]), Path(config["advanced"])):
        _, sections = split_h2(owner.read_text(encoding="utf-8"))
        for title, fragment in sections:
            if "PYQ" in title.upper():
                blocks.append(lower_headings(fragment))
    return blocks


def build_mcqs(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    variants = [
        "Which statement correctly identifies {label}?",
        "Which chronology card should be filed under {label}?",
        "Which option preserves the source-bounded meaning of {label}?",
        "Which statement avoids a close-option trap about {label}?",
    ]
    blocks: list[str] = []
    for fact_index, (label, statement) in enumerate(facts):
        for variant_index, template in enumerate(variants):
            number = fact_index * 4 + variant_index + 1
            expected = "ABCD"[(number - 1) % 4]
            wrongs = [
                facts[(fact_index + variant_index + offset) % len(facts)][1]
                for offset in (1, 2, 3)
            ]
            choices = {expected: statement}
            for letter, wrong in zip(
                [letter for letter in "ABCD" if letter != expected],
                wrongs,
            ):
                choices[letter] = wrong
            blocks.append(
                f"### Q{number}. {template.format(label=label)}\n\n"
                + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
                + f"\n\n**Answer: {expected}.**\n"
                + f"**Explanation:** {statement} The remaining options belong "
                "to different chronology, actor or analytical categories."
            )
    return "\n\n".join(blocks)


def solved_pyq_section(
    config: dict[str, object],
    pyq_blocks: list[str],
) -> str:
    if pyq_blocks:
        audit = "\n\n".join(pyq_blocks)
    else:
        audit = (
            "### TRANSPARENT ZERO-DIRECT-PYQ AUDIT\n\n"
            f"{config['pyq_note']}"
        )
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
    return audit + ("\n\n" + "\n\n".join(cards) if cards else "")


def original_mains_section(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    blocks = []
    for number, (marks, prompt, thesis, indexes) in enumerate(
        config["mains"], 1
    ):
        word_limit = {10: 150, 15: 250, 20: 300}[marks]
        evidence = "\n".join(f"- {facts[index][1]}" for index in indexes)
        blocks.append(
            f"### ORIGINAL MAINS {number} — {marks} MARKS\n\n"
            f"**Question:** {prompt} Answer in about {word_limit} words.\n\n"
            f"**Model thesis:** {thesis}\n\n"
            "**Claim → named evidence → analysis → qualification:**\n\n"
            f"{evidence}\n\n"
            f"**Qualified conclusion:** {thesis}"
        )
    return "\n\n".join(blocks)


def source_audit(config: dict[str, object]) -> str:
    return (
        "### SOURCE, PROGRESSION AND CURRENT-LINKAGE AUDIT\n\n"
        f"- **Generation date:** {DATE}.\n"
        "- **Repository-first evidence:** the Basic owner is taught first and "
        "preserved in full; the Advanced owner is retained only in the "
        "optional final teaching block.\n"
        f"- **OCR evidence:** {config['ocr_note']}\n"
        "- **Qdrant:** not used; repository Markdown and available OCR context "
        "were sufficient.\n"
        f"- **PYQ integrity:** {config['pyq_note']}\n"
        f"- **Live-link boundary:** {config['current_note']}\n"
        "- **Fact/inference discipline:** no current-affairs item, PYQ wording, "
        "figure or quotation is invented."
    )


def register_notes(config: dict[str, object]) -> str:
    facts = "\n".join(
        f"{number}. **{label}:** {statement}"
        for number, (label, statement) in enumerate(config["facts"], 1)
    )
    traps = "\n".join(f"- {trap}" for trap in config["traps"])
    return (
        f"### {config['title']}: RAPID CHRONOLOGY AND ARGUMENT MAP\n\n"
        f"{facts}\n\n"
        f"### {config['title']}: CLOSE-OPTION AND CAUSAL TRAPS\n\n"
        f"{traps}\n\n"
        f"### {config['title']}: ANSWER-WRITING SPINE\n\n"
        "```text\n"
        "DEFINE THE HISTORICAL PROBLEM -> ORDER THE CHRONOLOGY\n"
        "-> GROUP NAMED EVIDENCE BY MECHANISM -> TEST EXCLUSIONS AND LIMITS\n"
        "-> LINK CONSEQUENCES TO THE NEXT PHASE -> GIVE A GRADED VERDICT\n"
        "```\n\n"
        f"### {config['title']}: CURRENT-LINK BOUNDARY\n\n"
        f"{config['current_note']}"
    )


def assemble(
    config: dict[str, object],
    ascii_path: Path,
) -> tuple[str, str, int]:
    sessions = [
        _session_fragment(config, number, plan)
        for number, plan in enumerate(config["session_plans"], 1)
    ]
    mcqs = build_mcqs(config)
    pyq_blocks = extract_pyq_blocks(config)
    practice = (
        solved_pyq_section(config, pyq_blocks)
        + "\n\n"
        + original_mains_section(config)
    )
    manual = ascii_master.normalize_manual_spec_file(ascii_path)
    ascii_fragment = ascii_master.build_manual_fragment(
        manual[str(config["key"])]
    )
    markdown = (
        f"# {config['title']} — Learner-v2 Complete Learning Session\n\n"
        f"> **Authoring-only generation:** {DATE}. No PDF was rendered and no "
        "tracker or index was mutated.\n\n"
        + source_audit(config)
        + "\n\n## BASIC LEARNING SESSION\n\n"
        + "\n\n".join(sessions)
        + "\n\n### COMPLETE BASIC OWNER EVIDENCE BANK\n\n"
        + _owner_depth(Path(config["basic"]), exclude_pyq=True)
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + practice
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + _owner_depth(Path(config["advanced"]), exclude_pyq=True)
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + ascii_fragment
        + "\n\n"
        + register_notes(config)
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


def write_ascii_spec(
    topics: list[dict[str, object]],
    ascii_path: Path,
    scope: str,
) -> None:
    payload_topics = []
    for config in topics:
        key = str(config["key"])
        panels = []
        for title, structural_type, body, references in config["panels"]:
            lines = body.splitlines()
            if not lines or max(map(len, lines)) > 100:
                raise ValueError(f"{key}: ASCII line exceeds 100 characters.")
            if len([line for line in lines if line.strip()]) < 4:
                raise ValueError(f"{key}: ASCII panel has fewer than four lines.")
            if re.search(r"(?i)\bkey terms\b|\.{3}|…", body):
                raise ValueError(f"{key}: generic scaffolding or ellipsis found.")
            panels.append(
                {
                    "title": title,
                    "structural_type": structural_type,
                    "ascii_lines": lines,
                    "source_references": references,
                }
            )
        if len(panels) != 12:
            raise ValueError(f"{key}: expected 12 manual panels.")
        payload_topics.append(
            {
                "topic_key": key,
                "display_title": config["title"],
                "source_markdown": str(
                    Path(config["canonical"]).relative_to(ROOT)
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": scope,
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "complete_embed_ready_lines": True,
            "generic_scaffolding_forbidden": True,
            "tracker_untouched": True,
        },
        "topics": payload_topics,
    }
    ascii_path.parent.mkdir(parents=True, exist_ok=True)
    ascii_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_graphical_spec(
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
        source_markdown=markdown,
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ascii_path.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ascii_path.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=1,
    )
    if len(spec["stages"]) != 13:
        raise ValueError(
            f"{config['key']}: graphical master must contain 13 stages."
        )
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{config['key']}.json"
    output.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def ensure_section_manifest() -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    target = next(
        item
        for item in catalog["topics"]
        if item.get("topic_key") == "world-history-01"
    )
    path = section_indexes.materialize_catalog_section_manifest(
        ROOT,
        catalog,
        target,
    )
    if path != SECTION_MANIFEST:
        raise ValueError(f"Unexpected World History manifest path: {path}")
    return path


def validate_catalog(topics: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [config["key"] for config in topics if config["key"] not in keys]
    if missing:
        raise ValueError(f"World History topics missing from catalog: {missing}")


def write_generation_spec(
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
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        item
        for item in catalog["topics"]
        if item.get("topic_key") == config["key"]
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
        "local_ocr_sources": [
            str(path.relative_to(ROOT)) for path in LOCAL_BOOKS
        ],
        "pyq_indexes": [str(path.relative_to(ROOT)) for path in PYQ_INDEXES],
        "official_question_sources": [],
        "live_sources": config["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": (
            "80 unique MCQs with strict A-B-C-D rotation; only verified routed "
            "PYQ demands; six solved original Mains questions weighted "
            "10,10,15,15,20,20; final topic-specific register notes."
        ),
        "pyq_status_note": config["pyq_note"],
        "current_linkage_note": config["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "supersedes": None,
        "tracker_untouched": True,
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{config['key']}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def self_check(
    config: dict[str, object],
    markdown: str,
    workbook: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    key = str(config["key"])
    required_h2 = [
        "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION",
        "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "CONSOLIDATED REGISTER NOTES",
    ]
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    if [item for item in headings if item in required_h2] != required_h2:
        raise ValueError(f"{key}: learner-v2 H2 order failed.")
    if headings[-1] != "CONSOLIDATED REGISTER NOTES":
        raise ValueError(f"{key}: register notes must be the final H2.")
    sessions = re.findall(
        r"(?m)^### SESSION (\d+) — (.+?) — (.+?)\s*$",
        markdown,
    )
    if len(sessions) != 15 or session_count != 15:
        raise ValueError(f"{key}: exactly 15 sessions are required.")
    if markdown.count("#### VISUAL FIRST") != 15:
        raise ValueError(f"{key}: every session needs a visual.")
    if len(config["facts"]) != 20:
        raise ValueError(f"{key}: exactly 20 fact anchors are required.")
    if len(config["mains"]) != 6:
        raise ValueError(f"{key}: exactly six original Mains are required.")
    if [item[0] for item in config["mains"]] != [10, 10, 15, 15, 20, 20]:
        raise ValueError(f"{key}: Mains weighting is not 10,10,15,15,20,20.")
    if markdown.count("### ORIGINAL MAINS") != 6:
        raise ValueError(f"{key}: generated Mains count failed.")
    session_common.mcq_audit(markdown, key)
    session_common.mcq_audit(workbook, key)
    stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", markdown)
    if len(stems) != 80 or len(set(stems)) != 80:
        raise ValueError(f"{key}: MCQ stems are not 80 unique questions.")
    if markdown.count("```ascii-master") != 12:
        raise ValueError(f"{key}: embedded ASCII panel count failed.")
    graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
    if len(graphical["stages"]) != 13:
        raise ValueError(f"{key}: graphical stage count failed.")
    forbidden = re.compile(r"(?i)\b(?:todo|placeholder|lorem ipsum)\b")
    if forbidden.search(markdown):
        raise ValueError(f"{key}: generic scaffolding or ellipsis detected.")
    missing = [
        term
        for term in config["required_terms"]
        if term.casefold() not in markdown.casefold()
    ]
    if missing:
        raise ValueError(f"{key}: required terms missing: {missing}")
    if Path(config["canonical"]).read_text(encoding="utf-8") != markdown:
        raise ValueError(f"{key}: canonical Markdown diverged.")


def validate_previous_batch(
    previous: ModuleType | None,
    expected_keys: list[str],
) -> None:
    if previous is None:
        return
    actual = [str(config["key"]) for config in previous.TOPICS]
    if actual != expected_keys:
        raise ValueError(
            f"Previous World History batch changed: {actual} != {expected_keys}"
        )
    for key in expected_keys:
        source = SESSION_DIR / f"{key}_Learning-Session.md"
        workbook = SESSION_DIR / f"{key}_Solved-Workbook.md"
        if not source.is_file() or not workbook.is_file():
            raise FileNotFoundError(
                f"Previous sequential batch output is missing for {key}."
            )


def run_batch(
    *,
    topics: list[dict[str, object]],
    ascii_path: Path,
    scope: str,
    previous: ModuleType | None = None,
    previous_keys: list[str] | None = None,
) -> int:
    validate_previous_batch(previous, previous_keys or [])
    validate_catalog(topics)
    ensure_section_manifest()
    write_ascii_spec(topics, ascii_path, scope)
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    for config in topics:
        markdown, workbook, session_count = assemble(config, ascii_path)
        key = str(config["key"])
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
        source_path.write_text(markdown, encoding="utf-8")
        workbook_path.write_text(workbook, encoding="utf-8")
        Path(config["canonical"]).write_text(markdown, encoding="utf-8")
        graphical_path = write_graphical_spec(config, markdown, ascii_path)
        write_generation_spec(
            config,
            source_path,
            workbook_path,
            graphical_path,
            ascii_path,
        )
        self_check(
            config,
            markdown,
            workbook,
            session_count,
            graphical_path,
        )
        print(
            f"{key}: sessions=15; mcqs=80 (A20/B20/C20/D20); "
            "ascii=12; graphical=13; generation=1; tracker=untouched"
        )
    return 0
