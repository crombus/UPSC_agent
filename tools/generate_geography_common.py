"""Shared authoring-only engine for Geography learner-v2 Topics 05-19."""

from __future__ import annotations

import hashlib
import json
import re
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType
from typing import Iterable, Iterator

import carvaka_flowchart
import generate_world_history_common as _base


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-01"
SUBJECT = "Geography"
SECTION = "Part-A-Physical-Geography"
SECTION_KEY = "part-a-physical-geography"
REQUIRED_TOPIC_NUMBERS = tuple(range(5, 20))
GENERATION = 2
SUPERSEDES_TEMPLATE = "{key}:legacy-v1:g1"
ALLOW_EXISTING_HISTORY = False
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / SECTION_KEY
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
    / "geography--part-a-physical-geography.json"
)
LOCAL_BOOKS = [
    ROOT / "books" / "GC Leong - Certificate Physical and human Geography.pdf",
    ROOT / "books" / "Indian & World Geography - Husain, Majid_Compressed.pdf",
    ROOT / "books" / "Indian-geography-majid-hussain.pdf",
]
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Framework.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md",
    KNOWLEDGE / "REVISION-CHART_Core-Processes-Regions-and-Distinctive-Features.md",
    KNOWLEDGE / "ANSWER-WORTHINESS-AUDIT.md",
]
COMMON_CROSS = [path for path in COMMON_CROSS if path.is_file()]
PYQ_INDEXES = [
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2026.md",
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]

_BASE_OWNER_DEPTH = _base._owner_depth


def topic(
    number: int,
    title: str,
    basic_name: str,
    advanced_name: str,
    canonical_name: str,
    facts: list[tuple[str, str]],
    traps: list[str],
    mains: list[tuple[int, str, str, list[int]]],
    session_plans: list[tuple[str, list[int], str, str]],
    panels: list[tuple[str, str, str, list[str]]],
    required_terms: list[str],
    pyq_note: str,
    pyq_solutions: list[tuple[str, str, str, str, str]],
    live_sources: Iterable[str],
    current_note: str,
    extra: Iterable[str] = (),
) -> dict[str, object]:
    """Create one source-owned Geography topic configuration."""

    return {
        "number": number,
        "key": f"geography-{number:02d}",
        "title": title,
        "basic": KNOWLEDGE / "basic" / basic_name,
        "advanced": KNOWLEDGE / "advanced" / advanced_name,
        "canonical": KNOWLEDGE / canonical_name,
        "legacy_main": KNOWLEDGE / canonical_name,
        "extra": [KNOWLEDGE / value for value in extra],
        "facts": facts,
        "traps": traps,
        "mains": mains,
        "session_plans": session_plans,
        "panels": panels,
        "required_terms": required_terms,
        "live_sources": list(live_sources),
        "current_note": current_note,
        "ocr_note": (
            "Repository Markdown was primary. The three required local Geography "
            "books were inspected as supplementary OCR/searchable evidence. "
            "No unsupported page precision, volatile figure or quotation was imported."
        ),
        "pyq_note": pyq_note,
        "pyq_solutions": pyq_solutions,
    }


def _keywords(title: str, selected: list[tuple[str, str]]) -> list[str]:
    ignored = {
        "about", "after", "answer", "boundary", "current", "evidence",
        "geography", "india", "mechanism", "process", "source", "topic",
        "within", "which", "their", "through", "because", "system",
    }
    text = " ".join([title, *[label for label, _ in selected]])
    result: list[str] = []
    seen: set[str] = set()
    for word in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", text):
        folded = word.casefold()
        if folded in ignored or folded in seen:
            continue
        seen.add(folded)
        result.append(word)
        if len(result) == 6:
            break
    if len(result) < 4:
        result.extend(["classification", "causation", "comparison", "qualification"])
    return result[:6]


def _session_fragment(
    config: dict[str, object],
    number: int,
    plan: tuple[str, list[int], str, str],
) -> str:
    title, indexes, caution, exam_use = plan
    facts: list[tuple[str, str]] = config["facts"]
    selected = [facts[index] for index in indexes]
    labels = [label for label, _ in selected]
    joined = ", ".join(labels[:-1]) + (
        f" and {labels[-1]}" if len(labels) > 1 else labels[0]
    )
    keywords = _keywords(title, selected)
    phase = "FOUNDATION" if number <= 4 else ("SYNTHESIS" if number >= 13 else "CORE")
    evidence = "\n".join(f"- **{label}:** {statement}" for label, statement in selected)
    core = " ".join(statement for _, statement in selected)
    return (
        f"### SESSION {number} — {phase} — {title}\n\n"
        "#### DEFINITION / WHAT THIS IS CALLED\n\n"
        f"**Plain-language definition:** {title} explains how {joined} shape "
        f"the examinable geography of {config['title']}.\n\n"
        f"**Technical definition:** In geographical analysis, {title} is the "
        f"source-bounded relation among {joined}, classified by process, form, "
        "spatial setting, temporal change and human consequence.\n\n"
        "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        f"> {title} must be explained as a process-to-pattern chain, not as an "
        "unconnected catalogue of landforms, places or schemes.\n\n"
        "#### MUST-WRITE KEYWORDS\n\n"
        + "\n".join(f"- **{word}**" for word in keywords)
        + "\n\n"
        f"**How to use them:** Define the process, locate its spatial expression, "
        f"cite named evidence, apply this limit — {caution} — and conclude: {exam_use}\n\n"
        + _base._session_visual(title, labels, caution)
        + "\n\n#### CORE EXPLANATION\n\n"
        + core
        + "\n\n#### NAMED EVIDENCE AND MECHANISM\n\n"
        + evidence
        + "\n\n#### EXAMINER CAUTION\n\n"
        + f"- {caution}\n\n"
        + "#### EXAM LINK\n\n"
        + f"- **Prelims:** Separate the agent, landform, location, status and scale attached to {title}.\n"
        + f"- **Mains:** {exam_use}\n\n"
        + "#### MINI RECAP\n\n"
        + f"- **Evidence chain:** {' -> '.join(labels)}\n"
        + f"- **Qualified use:** {exam_use}\n\n"
        + "#### CLOSING RECALL FLOW\n\n"
        + "```closure-flow\n"
        + f"START / CONCEPT: {title}\n"
        + f"EXACT TERMS: {' | '.join(keywords)}\n"
        + f"MECHANISM / ARGUMENT: connect {joined} through process, place and time\n"
        + f"CONSEQUENCE / CONTRAST: {exam_use}\n"
        + f"UPSC TRAP / ANSWER-USE: {caution}\n"
        + f"ANSWER-GRABBING FORMULATION: {title} converts physical process into a qualified spatial argument\n"
        + "```"
    )


def _full_owner(path: Path, *, exclude_pyq: bool) -> str:
    return _BASE_OWNER_DEPTH(path, exclude_pyq=False)


def _pyq_section(config: dict[str, object], pyq_blocks: list[str]) -> str:
    heading = (
        "### TRANSPARENT ZERO-DIRECT-PYQ AUDIT"
        if not config["pyq_solutions"]
        else "### VERIFIED PYQ OWNERSHIP AUDIT"
    )
    parts = [f"{heading}\n\n{config['pyq_note']}"]
    if pyq_blocks and config["pyq_solutions"]:
        parts.append("### OWNER PYQ LEDGER EXTRACTS\n\n" + "\n\n".join(pyq_blocks))
    elif pyq_blocks:
        parts.append(
            "### CROSS-OWNER MATERIAL BOUNDARY\n\n"
            "Legacy owner PYQ integration remains preserved inside the complete "
            "Basic or Advanced evidence banks, but it is not repeated here or "
            "presented as direct solved PYQ practice."
        )
    for number, (year, paper, demand, status, model) in enumerate(
        config["pyq_solutions"], 1
    ):
        parts.append(
            f"### PYQ DEMAND CARD {number} — {year} {paper}\n\n"
            f"**Demand:** {demand}\n\n"
            f"**Status:** {status}\n\n"
            f"**Model solution:** {model}"
        )
    return "\n\n".join(parts)


def _build_mcqs(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    prompts = (
        "Which statement correctly explains {label}?",
        "Which option is the safest spatial interpretation of {label}?",
        "Which statement preserves the process boundary for {label}?",
        "Which option avoids the main UPSC trap concerning {label}?",
    )
    blocks: list[str] = []
    for fact_index, (label, statement) in enumerate(facts):
        for prompt_index, prompt in enumerate(prompts):
            number = fact_index * 4 + prompt_index + 1
            answer = "ABCD"[(number - 1) % 4]
            distractors = [
                facts[(fact_index + prompt_index + offset) % len(facts)][1]
                for offset in (1, 2, 3)
            ]
            choices = {answer: statement}
            for letter, wrong in zip(
                [letter for letter in "ABCD" if letter != answer],
                distractors,
            ):
                choices[letter] = wrong
            blocks.append(
                f"### Q{number}. {prompt.format(label=label)}\n\n"
                + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
                + f"\n\n**Answer: {answer}.**\n"
                + f"**Explanation:** {statement} The other options describe "
                "different processes, locations, scales or governance categories."
            )
    return "\n\n".join(blocks)


def _register_notes(config: dict[str, object]) -> str:
    facts = "\n".join(
        f"{number}. **{label}:** {statement}"
        for number, (label, statement) in enumerate(config["facts"], 1)
    )
    traps = "\n".join(f"- {trap}" for trap in config["traps"])
    return (
        f"### {config['title']}: PROCESS, FORM AND LOCATION LEDGER\n\n"
        f"{facts}\n\n"
        f"### {config['title']}: CLOSE-OPTION FIREWALLS\n\n"
        f"{traps}\n\n"
        f"### {config['title']}: MAP-AND-ANSWER SPINE\n\n"
        "```text\n"
        "DEFINE -> DRAW OR LOCATE -> EXPLAIN THE PROCESS -> NAME EVIDENCE\n"
        "-> COMPARE THE CLOSE ALTERNATIVE -> ADD HUMAN/CURRENT LINK\n"
        "-> QUALIFY SCALE, STATUS AND UNCERTAINTY -> GIVE A GRADED VERDICT\n"
        "```\n\n"
        f"### {config['title']}: VERIFIED CURRENT-LINK BOUNDARY\n\n"
        f"{config['current_note']}"
    )


def ensure_section_manifest() -> Path:
    if not SECTION_MANIFEST.is_file():
        raise FileNotFoundError(f"Missing Geography section manifest: {SECTION_MANIFEST}")
    data = json.loads(SECTION_MANIFEST.read_text(encoding="utf-8"))
    if data["subject"]["key"] != SUBJECT or data["section"]["key"] != SECTION_KEY:
        raise ValueError("Geography section manifest identity is incorrect.")
    keys = {item["topic_key"] for item in data["topics"]}
    missing = {f"geography-{number:02d}" for number in REQUIRED_TOPIC_NUMBERS} - keys
    if missing:
        raise ValueError(f"Geography section manifest is missing: {sorted(missing)}")
    return SECTION_MANIFEST


def validate_catalog(topics: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    by_key = {item.get("topic_key"): item for item in catalog["topics"]}
    for config in topics:
        entry = by_key.get(config["key"])
        if not entry:
            raise ValueError(f"Missing Geography catalog entry: {config['key']}")
        if entry["source_basic"].replace("\\", "/") != str(
            Path(config["basic"]).relative_to(ROOT)
        ).replace("\\", "/"):
            raise ValueError(f"{config['key']}: Basic catalog ownership changed.")
        if entry["source_advanced"].replace("\\", "/") != str(
            Path(config["advanced"]).relative_to(ROOT)
        ).replace("\\", "/"):
            raise ValueError(f"{config['key']}: Advanced catalog ownership changed.")


def _write_ascii_spec(
    topics: list[dict[str, object]], ascii_path: Path, scope: str
) -> None:
    payload_topics = []
    for config in topics:
        panels = []
        for title, structural_type, body, references in config["panels"]:
            lines = body.splitlines()
            if len(lines) < 4 or any(len(line) > 100 for line in lines):
                raise ValueError(f"{config['key']}: invalid manual ASCII dimensions.")
            if re.search(r"(?i)\bkey terms\b|\.{3}|…", body):
                raise ValueError(f"{config['key']}: generic ASCII scaffolding found.")
            panels.append(
                {
                    "title": title,
                    "structural_type": structural_type,
                    "ascii_lines": lines,
                    "source_references": references,
                }
            )
        if len(panels) != 12:
            raise ValueError(f"{config['key']}: exactly 12 panels are required.")
        payload_topics.append(
            {
                "topic_key": config["key"],
                "display_title": config["title"],
                "source_markdown": str(Path(config["canonical"]).relative_to(ROOT)),
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
        json.dumps(payload, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )


def _write_graphical_spec(
    config: dict[str, object], markdown: str, ascii_path: Path
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
        source_markdown=markdown.replace("\ufffd", ""),
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ascii_path.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ascii_path.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=GENERATION,
    )
    if len(spec["stages"]) != 13:
        raise ValueError(f"{config['key']}: graphical master must contain 13 stages.")
    errors = carvaka_flowchart.validate_spec(spec)
    if errors:
        raise ValueError(f"{config['key']}: graphical spec errors: {' | '.join(errors)}")
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{config['key']}.json"
    output.write_text(
        json.dumps(spec, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


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
        source_path,
        workbook_path,
        SECTION_MANIFEST,
        CATALOG,
        ascii_path,
        graphical_path,
        *[Path(path) for path in config["extra"]],
        *COMMON_CROSS,
        *PYQ_INDEXES,
        *LOCAL_BOOKS,
    ]
    sources = list(dict.fromkeys(sources))
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing generation sources: " + ", ".join(missing))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entry = next(item for item in catalog["topics"] if item["topic_key"] == config["key"])
    payload = {
        "schema_version": 1,
        "topic_key": config["key"],
        "subject": SUBJECT,
        "section": SECTION,
        "topic_folder": config["key"],
        "title": config["title"],
        "variant": "learner-v2",
        "generation": GENERATION,
        "generation_date": DATE,
        "command": entry["learner_v2_command"],
        "catalog_export_command": entry["export_mapping"]["command"],
        "catalog_export_source": entry["export_mapping"]["source"],
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
            "80 unique MCQs with strict A-B-C-D rotation; verified routed PYQs "
            "only; six original solved Mains questions weighted 10,10,15,15,20,20."
        ),
        "pyq_status_note": config["pyq_note"],
        "current_linkage_note": config["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "supersedes": (
            SUPERSEDES_TEMPLATE.format(key=config["key"])
            if SUPERSEDES_TEMPLATE
            else None
        ),
        "tracker_untouched": True,
    }
    if ALLOW_EXISTING_HISTORY:
        payload["allow_existing_history"] = True
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{config['key']}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=True, indent=2) + "\n",
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
        "write_ascii_spec": _write_ascii_spec,
        "write_graphical_spec": _write_graphical_spec,
        "write_generation_spec": _write_generation_spec,
        "_owner_depth": _full_owner,
        "_session_fragment": _session_fragment,
        "solved_pyq_section": _pyq_section,
        "build_mcqs": _build_mcqs,
        "register_notes": _register_notes,
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
    check_config = config
    canonical = Path(config["canonical"])
    canonical_text = canonical.read_text(encoding="utf-8")
    if (
        canonical_text != markdown
        and "### Semantic-completeness ownership and PYQ control" in canonical_text
    ):
        generated = SESSION_DIR / f"{config['key']}_Learning-Session.md"
        if generated.is_file() and generated.read_text(encoding="utf-8") == markdown:
            check_config = dict(config)
            check_config["canonical"] = generated
    with _configured():
        _base.self_check(
            check_config,
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
    """Run a strict sequential authoring batch without rendering or finalising."""

    with _configured():
        _base.validate_previous_batch(previous, previous_keys or [])
        validate_catalog(topics)
        ensure_section_manifest()
        _write_ascii_spec(topics, ascii_path, scope)
        SESSION_DIR.mkdir(parents=True, exist_ok=True)
        for config in topics:
            markdown, workbook, session_count = _base.assemble(config, ascii_path)
            key = str(config["key"])
            source_path = SESSION_DIR / f"{key}_Learning-Session.md"
            workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
            source_path.write_text(markdown, encoding="utf-8")
            workbook_path.write_text(workbook, encoding="utf-8")
            Path(config["canonical"]).write_text(markdown, encoding="utf-8")
            graphical_path = _write_graphical_spec(config, markdown, ascii_path)
            _write_generation_spec(
                config,
                source_path,
                workbook_path,
                graphical_path,
                ascii_path,
            )
            _base.self_check(
                config,
                markdown,
                workbook,
                session_count,
                graphical_path,
            )
            print(
                f"{key}: sessions=15; mcqs=80 (A20/B20/C20/D20); "
                f"ascii=12; graphical=13; generation={GENERATION}; tracker=untouched"
            )
    return 0
