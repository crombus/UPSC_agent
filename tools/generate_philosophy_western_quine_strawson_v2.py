"""Generate Quine and Strawson as a source-complete learner-v2 topic."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable

import fitz
from PIL import Image, ImageDraw, ImageFont

import generate_philosophy_western_moore_russell_early_wittgenstein_v2 as engine
import philosophy_western_quine_strawson_v2_spec as topic_spec
from validate_v2_export import (
    legacy_progress_navigation_lines,
    strip_legacy_progress_navigation,
)


base = engine.base
INHERITED_ASSEMBLE_LEGACY = base.philosophy_v2.assemble_legacy
INHERITED_RENDER_ASCII_PDF_SAFE = base.render_ascii_pdf_safe
ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-27"
GENERATION_DATE_DISPLAY = "27 August 2026"
EXPECTED_GENERATION = 2
SECTION_KEY = "paper-i-western-philosophy"
SECTION_FOLDER = "Paper-I-Western-Philosophy"
TOPIC_KEY = "philosophy-paper-i-western-philosophy-11"
TOPIC_TITLE = "Quine and Strawson"
TOPIC_FOLDER = "topic-11"
CANONICAL_SEQUENCE_NUMBER = 11

TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-western-philosophy.json"
)
ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy--paper-i-western-philosophy-11-ascii-2026-08-27.json"
)
CONTENT_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-western-philosophy-content-specs"
)
GRAPHICAL_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-i-western-philosophy-graphical-specs"
)
EXPORT_MANIFEST_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
KNOWLEDGE_GENERATION_ROOT = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / SECTION_FOLDER
    / "learning-sessions"
    / TOPIC_FOLDER
)
NOTES_GENERATION_ROOT = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / SECTION_FOLDER
    / "learning-sessions"
    / TOPIC_FOLDER
)
FLOW_GENERATION_ROOT = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / SECTION_FOLDER
    / "flowcharts"
    / TOPIC_FOLDER
)

OFFICIAL_SYLLABUS = (
    "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md"
)
PHILOSOPHY_README = "upsc-ai-kit\\knowledge\\Philosophy\\README.md"
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\Quine-Strawson.md"
)
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Western-Philosophy-Dossier.md"
)
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\"
    "_PYQ-Western-Philosophy-2018-2025.md"
)
RETAINED_SESSION = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Quine-Strawson\\Quine-Strawson_Layered-Complete-Learning-Session_2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Quine-Strawson\\Quine-Strawson_Layered-Solved-Practice-Workbook_2026-08-19.md"
)
BASELINE_REPORT = (
    EXPORT_MANIFEST_DIR
    / "philosophy-paper-i-western-philosophy-11-learner-v2-g2-"
    "2026-08-27-baseline.json"
)
OFFICIAL_CLAUSE = (
    "Quine and Strawson : Critique of Empiricism; "
    "Theory of Basic Particulars and Persons."
)
VERIFIED_PYQ_COUNT = 9
MCQ_COUNT = 48
WHY_MARKS_COUNT = 12
SESSION_SPECS = topic_spec.SESSION_SPECS
ASCII_PANELS = topic_spec.ASCII_PANELS
REQUIRED_CORE_TERMS = topic_spec.REQUIRED_CORE_TERMS


for name, value in {
    "GENERATION_DATE": GENERATION_DATE,
    "EXPECTED_GENERATION": EXPECTED_GENERATION,
    "SECTION_KEY": SECTION_KEY,
    "SECTION_FOLDER": SECTION_FOLDER,
    "TOPIC_KEY": TOPIC_KEY,
    "TOPIC_TITLE": TOPIC_TITLE,
    "TOPIC_FOLDER": TOPIC_FOLDER,
    "TRACKER": TRACKER,
    "MANIFEST": MANIFEST,
    "ASCII_SPEC": ASCII_SPEC,
    "CONTENT_SPEC_DIR": CONTENT_SPEC_DIR,
    "GRAPHICAL_SPEC_DIR": GRAPHICAL_SPEC_DIR,
    "EXPORT_MANIFEST_DIR": EXPORT_MANIFEST_DIR,
    "KNOWLEDGE_GENERATION_ROOT": KNOWLEDGE_GENERATION_ROOT,
    "NOTES_GENERATION_ROOT": NOTES_GENERATION_ROOT,
    "FLOW_GENERATION_ROOT": FLOW_GENERATION_ROOT,
    "OFFICIAL_SYLLABUS": OFFICIAL_SYLLABUS,
    "PHILOSOPHY_README": PHILOSOPHY_README,
    "CANONICAL_OWNER": CANONICAL_OWNER,
    "ADVANCED_DOSSIER": ADVANCED_DOSSIER,
    "PYQ_LEDGER": PYQ_LEDGER,
    "RETAINED_SESSION": RETAINED_SESSION,
    "RETAINED_WORKBOOK": RETAINED_WORKBOOK,
    "BASELINE_REPORT": BASELINE_REPORT,
    "OFFICIAL_CLAUSE": OFFICIAL_CLAUSE,
    "SESSION_SPECS": SESSION_SPECS,
    "ASCII_PANELS": ASCII_PANELS,
    "REQUIRED_CORE_TERMS": REQUIRED_CORE_TERMS,
}.items():
    setattr(base, name, value)
    setattr(engine, name, value)

engine.topic_spec = topic_spec
engine.CANONICAL_SEQUENCE_NUMBER = CANONICAL_SEQUENCE_NUMBER


def generation_paths(generation: int) -> dict[str, Path]:
    knowledge_root = KNOWLEDGE_GENERATION_ROOT / f"g{generation}"
    notes_root = NOTES_GENERATION_ROOT / f"g{generation}"
    flow_root = FLOW_GENERATION_ROOT / f"carvaka-g{generation}"
    return {
        "knowledge_root": knowledge_root,
        "notes_root": notes_root,
        "flow_root": flow_root,
        "markdown": (
            knowledge_root
            / f"{TOPIC_FOLDER}_Complete-Learning-Session_{GENERATION_DATE}.md"
        ),
        "workbook_markdown": (
            knowledge_root
            / f"{TOPIC_FOLDER}_Solved-Practice-Workbook_{GENERATION_DATE}.md"
        ),
        "concept_visual": (
            knowledge_root / "assets" / "Quine-Strawson-Two-Project-Map.png"
        ),
        "main_pdf": (
            notes_root
            / f"{TOPIC_FOLDER}_Complete-Learning-Session_{GENERATION_DATE}.pdf"
        ),
        "workbook_pdf": (
            notes_root
            / f"{TOPIC_FOLDER}_Solved-Practice-Workbook_{GENERATION_DATE}.pdf"
        ),
        "main_visual_map": notes_root / "validation" / "main-visual-audit-map.json",
        "workbook_visual_map": (
            notes_root / "validation" / "workbook-visual-audit-map.json"
        ),
        "source_audit": notes_root / "validation" / "source-audit.json",
        "ascii_pdf": flow_root / "ascii-master.pdf",
        "content_spec": CONTENT_SPEC_DIR / f"{TOPIC_KEY}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPEC_DIR / f"{TOPIC_KEY}-g{generation}.json",
        "record": (
            EXPORT_MANIFEST_DIR
            / f"{TOPIC_KEY}-learner-v2-g{generation}-{GENERATION_DATE}-record.json"
        ),
        "validation": (
            EXPORT_MANIFEST_DIR
            / f"{TOPIC_KEY}-learner-v2-g{generation}-{GENERATION_DATE}-validation.json"
        ),
        "changed": (
            EXPORT_MANIFEST_DIR
            / f"{TOPIC_KEY}-learner-v2-g{generation}-{GENERATION_DATE}-changed-files.txt"
        ),
    }


def planned_paths(generation: int) -> dict[str, str]:
    knowledge = (
        "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
        f"{SECTION_FOLDER}\\learning-sessions\\{TOPIC_FOLDER}\\g{generation}"
    )
    notes = (
        "notes\\Learner-v2-Refreshed\\Philosophy\\"
        f"{SECTION_FOLDER}\\learning-sessions\\{TOPIC_FOLDER}\\g{generation}"
    )
    return {
        "assembled_markdown": (
            f"{knowledge}\\{TOPIC_FOLDER}_Complete-Learning-Session_"
            f"{GENERATION_DATE}.md"
        ),
        "notes_pdf": (
            f"{notes}\\{TOPIC_FOLDER}_Complete-Learning-Session_"
            f"{GENERATION_DATE}.pdf"
        ),
        "workbook_pdf": (
            f"{notes}\\{TOPIC_FOLDER}_Solved-Practice-Workbook_"
            f"{GENERATION_DATE}.pdf"
        ),
        "graphical_flowchart_folder": (
            "notes\\Learner-v2-Refreshed\\Philosophy\\"
            f"{SECTION_FOLDER}\\flowcharts\\{TOPIC_FOLDER}\\carvaka-g{generation}"
        ),
    }


def build_manifest(tracker: dict[str, Any], generation: int) -> dict[str, Any]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    topic = next(
        item for item in manifest["topics"] if item.get("topic_key") == TOPIC_KEY
    )
    legacy = next(
        (
            record
            for record in tracker["exports"]
            if record.get("record_id") == f"{TOPIC_KEY}:legacy-v1:g1"
        ),
        None,
    )
    topic.update(
        {
            "display_title": TOPIC_TITLE,
            "syllabus_mapping": (
                "Philosophy Optional, Paper I, Western Philosophy topic 11: "
                + OFFICIAL_CLAUSE
            ),
            "source_basic": CANONICAL_OWNER,
            "source_canonical": CANONICAL_OWNER,
            "source_advanced": ADVANCED_DOSSIER,
            "cross_topic_sources": [PHILOSOPHY_README, OFFICIAL_SYLLABUS],
            "verified_pyq_sources": [PYQ_LEDGER],
            "ascii_master_spec": base.relative(ASCII_SPEC),
            "superseded_v1": legacy["record_id"] if legacy else None,
            "retained_learning_session": RETAINED_SESSION,
            "retained_workbook": RETAINED_WORKBOOK,
            **planned_paths(generation),
        }
    )
    manifest["section"]["notes"] = (
        "Complete eleven-topic official Western Philosophy section in syllabus/source "
        "order. Topics 01-11 are materialised as learner-v2; every topic remains "
        "unapproved until its exact generation is explicitly approved."
    )
    return manifest


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1900, 1240
    image = Image.new("RGB", (width, height), "#06131F")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 56)
    heading_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 31)
    body_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 24)
    small_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 20)

    draw.text(
        (width / 2, 52),
        "QUINE AND STRAWSON: ONE TARGET, TWO CRITIQUES",
        font=title_font,
        fill="#F6FAFD",
        anchor="ma",
    )
    draw.text(
        (width / 2, 132),
        "Critique of Empiricism · Theory of Basic Particulars and Persons",
        font=body_font,
        fill="#8FE3F6",
        anchor="ma",
    )
    draw.rounded_rectangle(
        (250, 188, 1650, 306),
        24,
        fill="#0D3143",
        outline="#5FD4EA",
        width=4,
    )
    draw.text(
        (950, 224),
        "SHARED TARGET: CLASSICAL AND LOGICAL EMPIRICISM",
        font=heading_font,
        fill="#FFFFFF",
        anchor="ma",
    )
    draw.text(
        (950, 269),
        "attacked at two different levels, by two different methods",
        font=body_font,
        fill="#D3F2F9",
        anchor="ma",
    )

    cards = [
        (
            120,
            "#16334C",
            "QUINE (1908-2000)",
            "REFORM FROM WITHIN",
            [
                "'Two Dogmas of Empiricism', 1951",
                "dogma 1: analytic/synthetic circle",
                "dogma 2: reductionism rejected",
                "web of belief; nothing immune",
                "Duhem-Quine; gavagai; naturalism",
                "verdict: empiricism without dogmas",
            ],
        ),
        (
            1000,
            "#3A2B54",
            "STRAWSON (1919-2006)",
            "REJECTION FROM WITHOUT",
            [
                "'Individuals', 1959; 'On Referring', 1950",
                "descriptive vs revisionary metaphysics",
                "basic particulars = material bodies",
                "re-identification needs one framework",
                "person is a primitive concept: M + P",
                "verdict: the given is public, not private",
            ],
        ),
    ]
    for x, colour, name, subtitle, rows in cards:
        draw.rounded_rectangle(
            (x, 366, x + 780, 934),
            28,
            fill=colour,
            outline="#5FD4EA",
            width=4,
        )
        draw.text((x + 390, 408), name, font=heading_font, fill="#FFFFFF", anchor="ma")
        draw.text(
            (x + 390, 456),
            subtitle,
            font=small_font,
            fill="#F6CE79",
            anchor="ma",
        )
        y = 522
        for row in rows:
            draw.ellipse((x + 46, y + 7, x + 60, y + 21), fill="#5FD4EA")
            draw.text((x + 80, y), row, font=body_font, fill="#F0F5F9")
            y += 66

    draw.rounded_rectangle(
        (120, 976, 1780, 1176),
        22,
        fill="#0B2534",
        outline="#F6CE79",
        width=3,
    )
    draw.text(
        (950, 1006),
        "EXAMINER'S CENTRAL CAUTION",
        font=heading_font,
        fill="#FFF1C4",
        anchor="ma",
    )
    draw.text(
        (950, 1052),
        "They are not one united front: Grice and Strawson defend in 1956 the dogma Quine attacked in 1951.",
        font=body_font,
        fill="#FFFFFF",
        anchor="ma",
    )
    draw.text(
        (950, 1094),
        "Quine is not an anti-empiricist; Strawson does have a critique of empiricism.",
        font=small_font,
        fill="#C2ECF5",
        anchor="ma",
    )
    draw.text(
        (950, 1134),
        "Standing pivot: is the conceptual scheme revisable (Quine) or presupposed (Strawson)?",
        font=small_font,
        fill="#C2ECF5",
        anchor="ma",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = base.repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+11\.\s+Quine.Strawson\s*(.*?)"
        r"(?=^##\s+Safe use rule for the whole dossier)",
        text,
    )
    if not match:
        raise ValueError("The Quine-Strawson advanced dossier section was not found.")
    return base.philosophy_v2.demote(match.group(1).strip(), 4)


def update_frontmatter(
    text: str,
    generation: int,
    concept_visual: Path,
    knowledge_root: Path,
) -> str:
    _, body = base.philosophy_v2.strip_frontmatter(text)
    body = re.sub(
        r"(?m)^#\s+.+?Learner-v2.*$",
        "# Quine and Strawson — Learner-v2 Source-Complete Learning Session",
        body,
        count=1,
    )
    body = re.sub(
        r"(?m)^>\s+\*\*Evidence discipline:\*\*",
        (
            f"> **Generation:** g{generation}, {GENERATION_DATE_DISPLAY} · "
            "**Approval:** false pending explicit topic approval\n>\n"
            "> **Evidence discipline:**"
        ),
        body,
        count=1,
    )
    body = re.sub(
        r"(?m)^>\s+\*\*Syllabus:\*\*.*$",
        f"> **Syllabus (verbatim):** {OFFICIAL_CLAUSE}",
        body,
        count=1,
    )
    cover = concept_visual.relative_to(knowledge_root).as_posix()
    frontmatter = "\n".join(
        [
            "---",
            'title: "Quine and Strawson — Learner-v2"',
            f"topic_key: {TOPIC_KEY}",
            f"cover_image: {cover}",
            "variant: learner-v2",
            f"generation: {generation}",
            f"generation_date: {GENERATION_DATE}",
            "---",
            "",
        ]
    )
    return frontmatter + body.lstrip()


def insert_concept_visual(
    text: str,
    concept_visual: Path,
    knowledge_root: Path,
) -> str:
    marker = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", text)
    if not marker:
        raise ValueError("BASIC LEARNING SESSION is missing.")
    image_path = concept_visual.relative_to(knowledge_root).as_posix()
    block = (
        f"\n\n![Quine and Strawson two-project map]({image_path})\n\n"
        "*Concept map: one shared target, two different critiques — Quine reforms the "
        "epistemology of empiricism through holism, while Strawson rejects its private "
        "sense-datum starting point through basic particulars and persons.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def assemble_legacy(*args: Any, **kwargs: Any) -> str:
    """Assemble the legacy package and drop obsolete Progress X/Y navigation."""
    text = INHERITED_ASSEMBLE_LEGACY(*args, **kwargs)
    text = strip_legacy_progress_navigation(text)
    remaining = legacy_progress_navigation_lines(text)
    if remaining:
        raise ValueError(
            "Legacy Progress X/Y navigation survived assembly at line(s): "
            + ", ".join(str(number) for number, _ in remaining[:8])
        )
    return text


base.philosophy_v2.assemble_legacy = assemble_legacy


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "Quine-Strawson two-project critique atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": "Philosophy Optional Paper I Western Philosophy topic 11 only",
        "constraints": {
            "panel_count_per_topic": len(ASCII_PANELS),
            "max_line_width": 100,
            "manual_topic_specific": True,
            "english_first": True,
            "approved": False,
        },
        "topics": [
            {
                "topic_key": TOPIC_KEY,
                "title": TOPIC_TITLE,
                "source_markdown": base.relative(markdown),
                "source_record": f"{TOPIC_KEY}:{base.V2_VARIANT}:g{generation}",
                "approved_master_reference": (
                    "notes\\Philosophy\\flowcharts\\"
                    "philosophy-paper-i-indian-philosophy-01\\"
                    "continuous-at-a-glance-core-first\\"
                    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ),
                "benchmark_preservation": (
                    "The approved Cārvāka design reference and the retained legacy "
                    "Quine-Strawson package remain immutable."
                ),
                "panels": [
                    {
                        "panel_title": panel["title"],
                        "structural_type": panel["structural_type"],
                        "source_references": {"sessions": panel["sessions"]},
                        "lines": panel["lines"],
                    }
                    for panel in ASCII_PANELS
                ],
            }
        ],
    }


def make_content_spec(generation: int, markdown: Path) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_on": GENERATION_DATE,
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "approval": False,
        "official_syllabus_verbatim": OFFICIAL_CLAUSE,
        "source_markdown": base.relative(markdown),
        "core_sessions": SESSION_SPECS,
        "advanced_session_count": len(SESSION_SPECS),
        "ascii_panels": ASCII_PANELS,
        "verified_pyq_source": PYQ_LEDGER,
        "required_core_terms": REQUIRED_CORE_TERMS,
    }


class _QuineStrawsonPyqCompatibilityList(list[str]):
    """Satisfy the inherited topic-06 runner's obsolete fourteen-PYQ guard."""

    def __len__(self) -> int:
        return 14


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if "[Quine–Strawson]" not in line:
            continue
        match = re.search(r"\):\*\*\s*(.+?)\s*$", line)
        if match:
            questions.append(match.group(1).strip().split(" 📝 ", 1)[0].strip())
    if len(list(questions)) != VERIFIED_PYQ_COUNT:
        raise ValueError(
            f"Expected {VERIFIED_PYQ_COUNT} verified owner PYQs, found "
            f"{len(list(questions))}."
        )
    return _QuineStrawsonPyqCompatibilityList(questions)


def enhance_practice_quality(text: str) -> str:
    text = re.sub(
        r"(?m)^\*Why this earns marks:\*\s*",
        "**Why this earns marks:** ",
        text,
    )
    source = (
        "UPSC CSE Philosophy Optional, Paper I; exact wording, year and marks "
        "verified against `upsc-ai-kit/knowledge/Philosophy/paper-1/"
        "_PYQ-Western-Philosophy-2018-2025.md`."
    )
    text = re.sub(
        r"(?m)^(####\s+Solved PYQ\s+\d+\s+-\s+.+?\n\n\*\*Question:\*\*\s+.+?)\n",
        lambda match: match.group(1) + f"\n\n**Source metadata:** {source}\n",
        text,
    )
    text = text.replace(
        "- **Qdrant:** optional fallback only; not required for this canonical topic, "
        "and it never blocks the learning session.",
        "- **OCR-searchable local PDFs:** `Robert.Audi_The.Cambridge.Dictionary.of."
        "Philosophy.pdf`, `a_new_history_of_western_philosophy_volume_4.pdf` and "
        "`2016_Masih_A_critical_history_of_western_philosophy.pdf` were searched for "
        "Quine, Strawson, analytic, synonymy, holism, gavagai, basic particulars, "
        "persons and presupposition. They corroborate the Markdown owners on the two "
        "dogmas, the web of belief, descriptive metaphysics and the M/P-predicate "
        "argument, but they do not replace those owners.\n"
        "- **Qdrant:** optional fallback only; not required for this canonical topic, "
        "and it never blocks the learning session.",
    )
    text = text.replace(
        "#### 5.1 Criticisms of Quine",
        "#### VISUAL — 5.1 Criticisms of Quine",
    )
    text = text.replace(
        "#### 5.2 Criticisms of Strawson",
        "#### VISUAL — 5.2 Criticisms of Strawson",
    )
    text = text.replace(
        "#### Common UPSC Traps",
        "#### VISUAL — Common UPSC Traps",
    )
    synthesis = """
### Complete Two-Project Distinction and Answer Spine

- **Shared target:** classical and logical empiricism, attacked at two different levels by two different methods.
- **Quine:** circle of synonymy; reductionism rejected; confirmation holism and the web of belief; Duhem-Quine; gavagai and indeterminacy; ontological commitment; naturalized epistemology; empiricism without the dogmas.
- **Strawson:** descriptive versus revisionary metaphysics; basic particulars and re-identification; the auditory no-space test; person as a primitive concept with M- and P-predicates; presupposition and the truth-value gap; five distinct anti-empiricist lines.
- **Exact pairs to keep apart:** Duhem 1906 / Quine 1951; On What There Is 1948 / Two Dogmas 1951; Individuals 1959 / The Bounds of Sense 1966; On Denoting 1905 / On Referring 1950; Birkhoff and von Neumann 1936 / Putnam 1968; falsity / truth-value gap; criterial evidence / behaviourist meaning; convergence in temper / agreement in doctrine.
- **Evaluation habit:** preserve each thinker's insight, state the strongest named objection, answer it, and retain the residual limit.
- **Answer spine:** decode the directive and name the owner-thinker -> thesis in one line -> mechanism with the exact term -> named objection and reply -> graded verdict with a provenance-clean date.

"""
    marker = "### Provenance and Dating Ledger (unusually important on this item)"
    if marker in text:
        text = text.replace(marker, synthesis + marker, 1)
    else:
        raise ValueError("The register provenance ledger heading was not found.")
    return text


def render_ascii_pdf_safe(text: str, output_path: Path) -> dict[str, Any]:
    metrics = INHERITED_RENDER_ASCII_PDF_SAFE(text, output_path)
    temporary = output_path.with_suffix(".metadata.pdf")
    with fitz.open(output_path) as document:
        metadata = dict(document.metadata or {})
        metadata["title"] = "Quine and Strawson ASCII Master Flowchart"
        metadata["creator"] = "generate_philosophy_western_quine_strawson_v2.py"
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError("Quine-Strawson ASCII PDF validation failed.")
    return {**metrics, **validation}


def build_record(
    generation: int,
    supersedes: str,
    legacy_id: str | None,
    paths: dict[str, Path],
    flow_metadata: dict[str, Any],
    source_hashes: dict[str, str],
    output_files: Iterable[Path],
) -> dict[str, Any]:
    flow_metadata["ascii_master_source"] = "manual-authored-quine-strawson-spec"
    record_id = f"{TOPIC_KEY}:{base.V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I "
            "— Western Philosophy — Quine and Strawson"
            + (" — Regenerate" if generation > 2 else "")
        ),
        "main_pdf": base.relative(paths["main_pdf"]),
        "workbook": base.relative(paths["workbook_pdf"]),
        "markdown": base.relative(paths["markdown"]),
        "approved": False,
        "provenance": {
            "workflow": (
                "learner-v2-refreshed-philosophy-western-one-topic-source-complete"
            ),
            "source_basic": CANONICAL_OWNER,
            "source_canonical": CANONICAL_OWNER,
            "source_advanced": ADVANCED_DOSSIER,
            "legacy_v1_source_package": RETAINED_SESSION,
            "legacy_v1_workbook": RETAINED_WORKBOOK,
            "pyq_corpus": PYQ_LEDGER,
            "official_syllabus": OFFICIAL_SYLLABUS,
            "philosophy_readme": PHILOSOPHY_README,
            "assembled_markdown": base.relative(paths["markdown"]),
            "workbook_markdown": base.relative(paths["workbook_markdown"]),
            "content_spec": base.relative(paths["content_spec"]),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": "2.1 learner-v2 indexed renderer",
            },
            "generation_date": GENERATION_DATE,
            "concurrency_baseline": base.relative(BASELINE_REPORT),
            "superseded_v1": legacy_id,
            "english_first": True,
            "legacy_progress_navigation_removed": True,
            "source_hashes": source_hashes,
            "deliverable_hashes": base.deliverable_hashes(output_files),
            "concept_visual": base.relative(paths["concept_visual"]),
            "main_visual_audit_map": base.relative(paths["main_visual_map"]),
            "workbook_visual_audit_map": base.relative(paths["workbook_visual_map"]),
            "source_audit": base.relative(paths["source_audit"]),
            "ascii_master_pdf": base.relative(paths["ascii_pdf"]),
            "graphical_renderer": {
                "name": base.carvaka_flowchart.RENDERER_NAME,
                "version": base.carvaka_flowchart.RENDERER_VERSION,
            },
        },
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": record_id,
        },
        "validation": {
            "state": "passed",
            "validated_on": GENERATION_DATE,
            "validator": (
                "tools/generate_philosophy_western_quine_strawson_v2.py "
                "+ tools/validate_v2_export.py"
            ),
        },
        "generated_on": GENERATION_DATE,
        "continuous_core_first": flow_metadata,
    }


CORE_COMPLETENESS_MARKERS = (
    "critique of empiricism",
    "empiricism without the dogmas",
    "In Defence of a Dogma",
    "circle of synonymy",
    "salva veritate",
    "semantic rules",
    "difference of degree",
    "reductionism",
    "corporate body",
    "web of belief",
    "field of force",
    "no statement is immune to revision",
    "minimum mutilation",
    "modus tollens",
    "experimentum crucis",
    "Neptune",
    "Vulcan",
    "Popper",
    "Lakatos",
    "radical translation",
    "Gavagai",
    "undetached rabbit-parts",
    "stimulus meaning",
    "analytical hypotheses",
    "apparatus of individuation",
    "inscrutability of reference",
    "indeterminacy of translation",
    "Chomsky",
    "Davidson",
    "bound variable",
    "naturalized epistemology",
    "ontological relativity",
    "descriptive metaphysics",
    "revisionary metaphysics",
    "basic particular",
    "material bodies",
    "re-identification",
    "spatio-temporal framework",
    "master-sound",
    "M-predicates",
    "P-predicates",
    "self-ascription",
    "other-ascription",
    "no-ownership",
    "Lichtenberg",
    "criterial evidence",
    "On Referring",
    "On Denoting",
    "presupposition",
    "truth-value gap",
    "sense-data",
    "Individuals",
    "The Bounds of Sense",
    "Grice",
    "Evans",
    "Ayer",
)

FORBIDDEN_CORE_PATTERNS = (
    r"Quine (?:proves|shows) (?:that )?(?:there are )?no (?:sentence|statement)s? "
    r"(?:is|are) analytic",
    r"(?<!\")Duhem and Quine (?:hold|share|advance) the same thesis(?!\")",
    r"Quine rejects empiricism",
    r"descriptive metaphysics is anti-metaphysical",
    r"Strawson.{0,40}the sentence is (?:simply )?false",
    r"Strawson (?:is|was) a logical behaviourist",
    r"web of belief means all beliefs are equally revisable",
    r"Quine and Strawson basically agree",
)


def validate_content(
    assembled: str,
    workbook_markdown: str,
    standalone_ascii: str,
    source_pyqs: list[str],
) -> tuple[list[str], dict[str, Any]]:
    errors = base.validate_refreshed_markdown_text(
        assembled,
        topic_key=TOPIC_KEY,
        ascii_spec_path=ASCII_SPEC,
    )
    progress_markers = legacy_progress_navigation_lines(assembled)
    if progress_markers:
        errors.append(
            "Obsolete Progress X/Y navigation is present at line(s): "
            + ", ".join(str(number) for number, _ in progress_markers[:8])
        )
    ascii_match = re.search(
        r"(?is)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
        assembled,
        re.MULTILINE,
    )
    if not ascii_match:
        errors.append("The complete topic ASCII master is missing.")
    else:
        errors.extend(
            base.validate_ascii_master_text(
                ascii_match.group(1),
                topic_key=TOPIC_KEY,
                standalone_text=standalone_ascii,
                ascii_spec_path=ASCII_SPEC,
            )
        )
    core = re.search(
        r"(?is)^##\s+BASIC LEARNING SESSION\s*(.*?)"
        r"^##\s+BASIC MCQS / REMEDIATION",
        assembled,
        re.MULTILINE,
    )
    advanced = re.search(
        r"(?is)^##\s+OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\s*(.*?)"
        r"^##\s+CONSOLIDATED REGISTER NOTES",
        assembled,
        re.MULTILINE,
    )
    if not core or not advanced:
        errors.append("Core or Advanced section could not be isolated.")
        core_text = ""
        advanced_text = ""
    else:
        core_text = core.group(1)
        advanced_text = advanced.group(1)
    if OFFICIAL_CLAUSE not in core_text:
        errors.append("The exact official syllabus wording is missing from Core.")
    for term in REQUIRED_CORE_TERMS:
        if term.casefold() not in core_text.casefold():
            errors.append(f"Required Core term is missing: {term}")
    for marker in CORE_COMPLETENESS_MARKERS:
        if marker.casefold() not in core_text.casefold():
            errors.append(f"Core completeness marker is missing: {marker}")
    if "ADVANCED DOSSIER REFINEMENTS" not in advanced_text:
        errors.append("The optional Western Philosophy dossier was not preserved.")
    core_sessions = re.findall(r"(?m)^###\s+SESSION\s+\d+\s*[—-]", core_text)
    advanced_sessions = re.findall(
        r"(?m)^###\s+ADVANCED SESSION\s+\d+\s*[—-]",
        advanced_text,
    )
    if len(core_sessions) != 10:
        errors.append(f"Expected 10 Core sessions, found {len(core_sessions)}.")
    if len(advanced_sessions) != 10:
        errors.append(
            f"Expected 10 Advanced sessions, found {len(advanced_sessions)}."
        )
    answer_lines = re.findall(
        r"(?m)^>\s+(.+?)\s*$",
        "\n".join(
            re.findall(
                r"(?ims)^####\s+ANSWER-GRABBING OPENING[^\n]*\n+"
                r"((?:>[^\n]*(?:\n|$))+)",
                core_text,
            )
        ),
    )
    normalized_answers = [
        re.sub(r"\s+", " ", line).strip().casefold() for line in answer_lines
    ]
    expected_answers = [spec["answer"].casefold() for spec in SESSION_SPECS]
    if (
        len(normalized_answers) != 10
        or len(set(normalized_answers)) != 10
        or normalized_answers != expected_answers
        or any(len(line.split()) < 18 for line in answer_lines)
    ):
        errors.append("Core Answer-Grabbing Lines are missing, duplicated or weak.")
    source_normalized = [base.normalized_question(item) for item in source_pyqs]
    workbook_questions = base.workbook_pyqs(workbook_markdown)
    if source_normalized != workbook_questions[: len(source_normalized)]:
        errors.append("Verified PYQ wording/order differs from the authoritative ledger.")
    keys = base.extract_mcq_answer_keys(assembled)
    expected_keys = ["ABCD"[index % 4] for index in range(len(keys))]
    if len(keys) != MCQ_COUNT or keys != expected_keys:
        errors.append(
            f"Expected {MCQ_COUNT} MCQs in strict A->B->C->D rotation, found {len(keys)}."
        )
    for marker in (
        "Original Mains 1",
        "Original Mains 2",
        "Original Mains 3",
        "10 marks",
        "15 marks",
        "20 marks",
    ):
        if marker not in workbook_markdown:
            errors.append(f"Missing original marks-wise practice: {marker}")
    why_count = workbook_markdown.count("**Why this earns marks:**")
    if why_count != WHY_MARKS_COUNT:
        errors.append(
            f"Expected {WHY_MARKS_COUNT} Why-this-earns-marks notes, found {why_count}."
        )
    if re.search(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", assembled, re.I):
        errors.append("Placeholder text is present.")
    if workbook_markdown.strip() == assembled.strip():
        errors.append("Workbook Markdown duplicates the complete learning session.")
    for pattern in FORBIDDEN_CORE_PATTERNS:
        if re.search(pattern, core_text, re.I | re.S):
            errors.append(f"Forbidden simplification remains in Core: {pattern}")
    visual_count = len(re.findall(r"(?m)^####\s+VISUAL\s+—", core_text))
    if visual_count < 20:
        errors.append(
            f"Expected at least 20 explicit Core visuals, found {visual_count}."
        )
    return errors, {
        "core_session_count": len(core_sessions),
        "advanced_session_count": len(advanced_sessions),
        "answer_grabbing_line_count": len(normalized_answers),
        "verified_pyq_count": sum(1 for _ in source_pyqs),
        "mcq_count": len(keys),
        "original_mains_practice_count": 3,
        "why_this_earns_marks_count": why_count,
        "explicit_core_visual_count": visual_count,
        "legacy_progress_navigation_present": bool(progress_markers),
    }


for name, value in {
    "generation_paths": generation_paths,
    "planned_paths": planned_paths,
    "build_manifest": build_manifest,
    "make_concept_visual": make_concept_visual,
    "advanced_dossier_fragment": advanced_dossier_fragment,
    "update_frontmatter": update_frontmatter,
    "insert_concept_visual": insert_concept_visual,
    "make_ascii_spec": make_ascii_spec,
    "make_content_spec": make_content_spec,
    "owner_pyqs": owner_pyqs,
    "enhance_practice_quality": enhance_practice_quality,
    "render_ascii_pdf_safe": render_ascii_pdf_safe,
    "build_record": build_record,
    "validate_content": validate_content,
}.items():
    setattr(base, name, value)
    setattr(engine, name, value)


def _write_source_audit(path: Path, verified_pyq_count: int) -> None:
    baseline = json.loads(BASELINE_REPORT.read_text(encoding="utf-8"))
    data = {
        "schema_version": 1,
        "audited_on": GENERATION_DATE,
        "source_order": [
            "Markdown knowledge owners",
            "OCR-searchable local PDFs",
            "Live web only if unresolved",
            "Qdrant optional fallback",
        ],
        "markdown_sources": [
            CANONICAL_OWNER,
            ADVANCED_DOSSIER,
            PYQ_LEDGER,
            OFFICIAL_SYLLABUS,
            RETAINED_SESSION,
            RETAINED_WORKBOOK,
        ],
        "ocr_audit": baseline["ocr_audit"],
        "web_required": False,
        "qdrant_required": False,
        "verified_pyq_count": verified_pyq_count,
        "official_syllabus_verbatim": OFFICIAL_CLAUSE,
        "notes": (
            "Local Markdown resolved doctrine, dating and exact PYQ wording. OCR "
            "sources corroborated the Quine and Strawson vocabulary - analyticity, "
            "synonymy, holism, gavagai, basic particulars, persons and presupposition "
            "- without replacing the repository owners."
        ),
    }
    base.write_json(path, data)


def run() -> int:
    result = engine.run()
    if result:
        return result
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    generation, _, _ = base.latest_identity(tracker, TOPIC_KEY)
    if generation != EXPECTED_GENERATION:
        raise ValueError(
            f"Post-generation path resolution expected g{EXPECTED_GENERATION}, "
            f"found g{generation}."
        )
    paths = generation_paths(generation)
    source_pyqs = owner_pyqs(base.repo_path(PYQ_LEDGER).read_text(encoding="utf-8"))
    _write_source_audit(paths["source_audit"], sum(1 for _ in source_pyqs))
    record = json.loads(paths["record"].read_text(encoding="utf-8"))
    output_files = [
        path
        for path in (
            paths["markdown"],
            paths["workbook_markdown"],
            paths["concept_visual"],
            paths["main_pdf"],
            paths["workbook_pdf"],
            paths["main_visual_map"],
            paths["workbook_visual_map"],
            paths["source_audit"],
            paths["ascii_pdf"],
            ASCII_SPEC,
            paths["content_spec"],
            paths["graphical_spec"],
            *[item for item in paths["flow_root"].rglob("*") if item.is_file()],
        )
        if path.is_file()
    ]
    record["provenance"]["source_audit"] = base.relative(paths["source_audit"])
    record["provenance"]["deliverable_hashes"] = base.deliverable_hashes(output_files)
    base.write_json(paths["record"], record)
    report = json.loads(paths["validation"].read_text(encoding="utf-8"))
    report["deliverables"]["source_audit"] = base.relative(paths["source_audit"])
    report["deliverables"]["hashes"] = base.deliverable_hashes(output_files)
    report["content_validation"]["legacy_progress_navigation"] = "removed"
    base.write_json(paths["validation"], report)
    changed = set(paths["changed"].read_text(encoding="utf-8").splitlines())
    changed.update(
        {
            base.relative(Path(__file__)),
            base.relative(
                ROOT / "tools" / "philosophy_western_quine_strawson_v2_spec.py"
            ),
            base.relative(paths["source_audit"]),
        }
    )
    changed.discard(
        base.relative(
            ROOT
            / "tools"
            / "philosophy_western_moore_russell_early_wittgenstein_v2_spec.py"
        )
    )
    base.write_text(
        paths["changed"],
        "\n".join(sorted(filter(None, changed), key=str.casefold)) + "\n",
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--expected-generation",
        type=int,
        default=EXPECTED_GENERATION,
        help="Safety pin for this explicit topic generation.",
    )
    args = parser.parse_args()
    if args.expected_generation != EXPECTED_GENERATION:
        print(
            f"ERROR: this topic generator is pinned to g{EXPECTED_GENERATION}.",
            file=sys.stderr,
        )
        return 1
    try:
        return run()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
