"""Generate Hegel as a source-complete learner-v2 Philosophy topic."""

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

import generate_philosophy_western_empiricism_v2 as pipeline
import philosophy_western_hegel_v2_spec as hegel_spec


base = pipeline.base
ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-26"
SECTION_KEY = "paper-i-western-philosophy"
SECTION_FOLDER = "Paper-I-Western-Philosophy"
TOPIC_KEY = "philosophy-paper-i-western-philosophy-05"
TOPIC_TITLE = "Hegel"
TOPIC_FOLDER = "topic-05"
CANONICAL_SEQUENCE_NUMBER = 5

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
    / "philosophy--paper-i-western-philosophy-05-ascii-2026-08-26.json"
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
CANONICAL_OWNER = "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\Hegel.md"
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Western-Philosophy-Dossier.md"
)
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\"
    "_PYQ-Western-Philosophy-2018-2025.md"
)
RETAINED_SESSION = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\"
    "learning-sessions\\Hegel\\Hegel_Layered-Complete-Learning-Session_2026-08-18.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\"
    "learning-sessions\\Hegel\\Hegel_Layered-Solved-Practice-Workbook_2026-08-18.md"
)
BASELINE_REPORT = (
    EXPORT_MANIFEST_DIR
    / "philosophy-paper-i-western-philosophy-05-learner-v2-g2-"
    "2026-08-26-baseline.json"
)
OFFICIAL_CLAUSE = (
    "Hegel : Dialectical Method; Absolute Idealism."
)
SESSION_SPECS = hegel_spec.SESSION_SPECS
ASCII_PANELS = hegel_spec.ASCII_PANELS
REQUIRED_CORE_TERMS = hegel_spec.REQUIRED_CORE_TERMS


for name, value in {
    "GENERATION_DATE": GENERATION_DATE,
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
    "SESSION_SPECS": SESSION_SPECS,
    "ASCII_PANELS": ASCII_PANELS,
    "REQUIRED_CORE_TERMS": REQUIRED_CORE_TERMS,
}.items():
    setattr(base, name, value)


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
            knowledge_root / "assets" / "Hegel-Dialectical-System.png"
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
    base_knowledge = (
        "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
        f"{SECTION_FOLDER}\\learning-sessions\\{TOPIC_FOLDER}\\g{generation}"
    )
    base_notes = (
        "notes\\Learner-v2-Refreshed\\Philosophy\\"
        f"{SECTION_FOLDER}\\learning-sessions\\{TOPIC_FOLDER}\\g{generation}"
    )
    return {
        "assembled_markdown": (
            f"{base_knowledge}\\{TOPIC_FOLDER}_Complete-Learning-Session_"
            f"{GENERATION_DATE}.md"
        ),
        "notes_pdf": (
            f"{base_notes}\\{TOPIC_FOLDER}_Complete-Learning-Session_"
            f"{GENERATION_DATE}.pdf"
        ),
        "workbook_pdf": (
            f"{base_notes}\\{TOPIC_FOLDER}_Solved-Practice-Workbook_"
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
                "Philosophy Optional, Paper I, Western Philosophy topic 5: "
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
        "Complete eleven-topic official Western Philosophy section in "
        "syllabus/source order. Topics 01-05 are materialised as learner-v2; "
        "the other topics retain their independently resolved state."
    )
    return manifest


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1900, 1180
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 58)
    heading = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 39)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 28)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 24)

    draw.text(
        (width / 2, 65),
        "HEGEL: DIALECTIC AND THE SELF-DEVELOPING WHOLE",
        font=title_font,
        fill="#F8FAFC",
        anchor="ma",
    )
    draw.text(
        (width / 2, 148),
        "Kantian oppositions become internally mediated moments of Absolute Idealism",
        font=regular,
        fill="#8DE7F7",
        anchor="ma",
    )
    stages = [
        (
            92,
            "#173B55",
            "IMMANENT START",
            "Kant's residual dualisms",
            ["phenomenon / noumenon", "subject / object", "freedom / nature"],
            "LIMITS TEST THEMSELVES",
        ),
        (
            670,
            "#263D6A",
            "DIALECTICAL MOVE",
            "Determinate negation",
            ["internal contradiction", "Aufhebung: cancel + keep", "richer mediated result"],
            "PROGRESSION MUST BE EARNED",
        ),
        (
            1248,
            "#4A315F",
            "ABSOLUTE RESULT",
            "Substance also as Subject",
            ["Logic -> Nature -> Spirit", "finite moments remain real", "philosophy comprehends whole"],
            "IDENTITY-IN-DIFFERENCE",
        ),
    ]
    for x, colour, title, subtitle, lines, footer in stages:
        draw.rounded_rectangle(
            (x, 255, x + 560, 875),
            28,
            fill=colour,
            outline="#61DDF2",
            width=4,
        )
        draw.text((x + 280, 315), title, font=heading, fill="#FFFFFF", anchor="ma")
        draw.text(
            (x + 280, 382),
            subtitle,
            font=small,
            fill="#F8D27A",
            anchor="ma",
        )
        y = 490
        for line in lines:
            draw.ellipse((x + 48, y + 8, x + 62, y + 22), fill="#61DDF2")
            draw.text((x + 82, y), line, font=regular, fill="#F3F7FA")
            y += 90
        draw.rounded_rectangle((x + 34, 790, x + 526, 848), 14, fill="#0B202E")
        draw.text(
            (x + 280, 819),
            footer,
            font=small,
            fill="#FFF1B8",
            anchor="mm",
        )
    for start, end in ((652, 670), (1230, 1248)):
        draw.line((start, 575, end, 575), fill="#61DDF2", width=10)
        draw.polygon(
            [(end - 16, 559), (end, 575), (end - 16, 591)],
            fill="#61DDF2",
        )
    draw.rounded_rectangle(
        (180, 945, 1720, 1100),
        20,
        fill="#0E2B3D",
        outline="#F8D27A",
        width=3,
    )
    draw.text(
        (950, 988),
        "CORE RESULT: THE TRUE IS THE WHOLE",
        font=heading,
        fill="#FFF5D4",
        anchor="mm",
    )
    draw.text(
        (950, 1048),
        "The whole is the result of development; finite distinctions survive as moments.",
        font=small,
        fill="#F8FAFC",
        anchor="mm",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = base.repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+5\.\s+Hegel\s*(.*?)"
        r"(?=^##\s+6\.\s+Moore)",
        text,
    )
    if not match:
        raise ValueError("The Hegel advanced dossier section was not found.")
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
        "# Hegel — Learner-v2 Source-Complete Learning Session",
        body,
        count=1,
    )
    body = re.sub(
        r"(?m)^>\s+\*\*Evidence discipline:\*\*",
        (
            f"> **Generation:** g{generation}, 26 August 2026 · "
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
            'title: "Hegel — Learner-v2"',
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
        f"\n\n![Hegelian dialectical system architecture]({image_path})\n\n"
        "*Concept map: Hegel transforms Kant's fixed dualisms through immanent "
        "critique, determinate negation and sublation; the resulting Absolute "
        "is a self-developing whole articulated as Logic, Nature and Spirit.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "Hegel dialectic-and-Absolute-Idealism atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": "Philosophy Optional Paper I Western Philosophy topic 04 only",
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
                    "The approved Cārvāka design reference and every legacy "
                    "Hegel generation remain immutable."
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


PYQ_MARKS_NOTES = (
    "It defines dialectic as immanent self-movement, reconstructs determinate negation and sublation, and explains why developed totality rather than an isolated proposition is truth.",
    "It preserves the phenomenal world's reality as a finite mediated moment, distinguishes Hegel from Berkeley and Kant, and gives a graded rather than eliminative verdict.",
    "It integrates the method with Absolute Idealism through Kant, substance-as-subject and Logic-Nature-Spirit, then tests the system at its most difficult transition.",
    "It uses Hegel's own vocabulary instead of a mechanical triad, shows how the Absolute is realised, and gives a qualified answer to the Logic-Nature objection.",
    "It supplies mechanism, historical stages, institutional freedom, named examples and a critique of retrospective teleology rather than merely listing civilisations.",
    "It states Kant's position fairly, gives Hegel's three prongs, includes Kant's limiting-concept reply and reaches a bounded comparative verdict.",
)
ORIGINAL_MARKS_NOTES = (
    "The answer defines all three senses of sublation, connects them to determinate negation and corrects the thesis-antithesis-synthesis shorthand.",
    "The answer reconstructs recognition, dependence, fear and formative labour before distinguishing conceptual instability from historical prediction.",
    "The answer states the category-to-existence problem, names the major objections, gives the non-temporal reply and concedes the residual limit.",
)


def enhance_practice_quality(text: str) -> str:
    def append_notes(
        source: str,
        pattern: str,
        notes: tuple[str, ...],
    ) -> str:
        matches = list(re.finditer(pattern, source, re.MULTILINE | re.DOTALL))
        if len(matches) != len(notes):
            raise ValueError(
                f"Expected {len(notes)} model-answer blocks, found {len(matches)}."
            )
        result = source
        for match, note in reversed(list(zip(matches, notes))):
            block = match.group(1).rstrip()
            replacement = (
                block
                + "\n\n**Why this earns marks:** "
                + note
                + "\n\n"
            )
            result = result[: match.start(1)] + replacement + result[match.end(1) :]
        return result

    text = append_notes(
        text,
        r"(^####\s+Solved PYQ\s+\d+.*?)(?=^####\s+Solved PYQ\s+\d+|"
        r"^###\s+ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS)",
        PYQ_MARKS_NOTES,
    )
    return append_notes(
        text,
        r"(^####\s+Original Mains\s+\d+.*?)(?=^####\s+Original Mains\s+\d+|"
        r"^##\s+OPTIONAL ADVANCED DEPTH)",
        ORIGINAL_MARKS_NOTES,
    )


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if "[Hegel]" not in line:
            continue
        match = re.search(r"\):\*\*\s*(.+?)\s*$", line)
        if match:
            questions.append(match.group(1).strip())
    return questions


def render_ascii_pdf_safe(text: str, output_path: Path) -> dict[str, Any]:
    metrics = base.render_ascii_pdf_safe(text, output_path)
    temporary = output_path.with_suffix(".metadata.pdf")
    with fitz.open(output_path) as document:
        metadata = dict(document.metadata or {})
        metadata["title"] = "Hegel ASCII Master Flowchart"
        metadata["creator"] = "generate_philosophy_western_hegel_v2.py"
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError("Hegel ASCII PDF metadata repair broke validation.")
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
    record_id = f"{TOPIC_KEY}:{base.V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I "
            "— Western Philosophy — Hegel"
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
            "superseded_v1": legacy_id,
            "english_first": True,
            "source_hashes": source_hashes,
            "deliverable_hashes": base.deliverable_hashes(output_files),
            "concept_visual": base.relative(paths["concept_visual"]),
            "main_visual_audit_map": base.relative(paths["main_visual_map"]),
            "workbook_visual_audit_map": base.relative(paths["workbook_visual_map"]),
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
                "tools/generate_philosophy_western_hegel_v2.py + "
                "tools/validate_v2_export.py"
            ),
        },
        "generated_on": GENERATION_DATE,
        "continuous_core_first": flow_metadata,
    }


def validate_content(
    assembled: str,
    workbook_markdown: str,
    standalone_ascii: str,
    source_pyqs: list[str],
) -> tuple[list[str], dict[str, Any]]:
    errors = base.validate_refreshed_markdown_text(
        assembled,
        topic_key=TOPIC_KEY,
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
    for marker in (
        "ABSTRACT / UNDERSTANDING",
        "DIALECTICAL / NEGATIVE",
        "SPECULATIVE / POSITIVE",
        "cancel one-sidedness",
        "preserve partial truth",
        "ELEVATE into a richer determination",
        "negation of negation",
        "mediated immediacy",
        "PURE BEING",
        "PURE NOTHING",
        "BECOMING",
        "Nature and finite minds",
        "Subjective Spirit",
        "Objective Spirit",
        "Absolute Spirit",
        "Wirklichkeit",
        "Dasein",
        "one-sided recognition",
        "thing-in-itself",
        "rational institutions",
        "thesis-antithesis-synthesis",
        "Logic-Nature transition",
        "Kierkegaard",
        "Marx",
        "Schopenhauer",
    ):
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
    if len(keys) != 36 or keys != expected_keys:
        errors.append(
            f"Expected 36 MCQs in strict A->B->C->D rotation, found {len(keys)}."
        )
    for marker in (
        "Original Mains 1 - 10 marks",
        "Original Mains 2 - 15 marks",
        "Original Mains 3 - 20 marks",
    ):
        if marker not in workbook_markdown:
            errors.append(f"Missing original marks-wise practice: {marker}")
    why_count = workbook_markdown.count("**Why this earns marks:**")
    if why_count != 9:
        errors.append(f"Expected 9 Why-this-earns-marks notes, found {why_count}.")
    if re.search(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", assembled, re.I):
        errors.append("Placeholder text is present.")
    if workbook_markdown.strip() == assembled.strip():
        errors.append("Workbook Markdown duplicates the complete learning session.")
    return errors, {
        "core_session_count": len(core_sessions),
        "advanced_session_count": len(advanced_sessions),
        "answer_grabbing_line_count": len(normalized_answers),
        "verified_pyq_count": len(source_pyqs),
        "mcq_count": len(keys),
        "original_mains_practice_count": 3,
        "why_this_earns_marks_count": why_count,
    }


def run() -> int:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    if tracker.get("schema_version") != 2 or not isinstance(tracker.get("exports"), list):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
    generation, supersedes, legacy_id = base.latest_identity(tracker, TOPIC_KEY)
    if generation != 2:
        raise ValueError(
            "Tracker resolution changed during generation: the audited target was g2, "
            f"but the latest tracker now resolves g{generation}."
        )
    paths = generation_paths(generation)
    targets = [
        paths["knowledge_root"],
        paths["notes_root"],
        paths["flow_root"],
        ASCII_SPEC,
        paths["content_spec"],
        paths["graphical_spec"],
        paths["record"],
        paths["validation"],
        paths["changed"],
    ]
    existing = [path for path in targets if path.exists()]
    if existing:
        raise ValueError(
            "Refusing to overwrite generation targets:\n- "
            + "\n- ".join(base.relative(path) for path in existing)
        )
    if not BASELINE_REPORT.is_file():
        raise ValueError(f"Concurrency baseline is missing: {base.relative(BASELINE_REPORT)}")

    base.write_json(MANIFEST, build_manifest(tracker, generation))
    base.generate_section_indexes(ROOT, MANIFEST, TRACKER)

    retained_main = base.repo_path(RETAINED_SESSION).read_text(encoding="utf-8")
    retained_workbook = base.repo_path(RETAINED_WORKBOOK).read_text(encoding="utf-8")
    ledger = base.repo_path(PYQ_LEDGER).read_text(encoding="utf-8")
    source_pyqs = owner_pyqs(ledger)
    if len(source_pyqs) != 6:
        raise ValueError(f"Expected 6 verified owner PYQs, found {len(source_pyqs)}.")

    assembled = base.philosophy_v2.assemble_legacy(
        base.Topic(TOPIC_KEY, TOPIC_TITLE),
        retained_main,
        retained_workbook,
    )
    assembled = re.sub(
        r"(?m)^###\s+OPTIONAL DEPTH\s+(\d+)\s*[—-]\s*",
        r"### ADVANCED SESSION \1 — ",
        assembled,
    )
    assembled = base.insert_advanced_dossier(
        assembled,
        advanced_dossier_fragment(),
    )

    paths["knowledge_root"].mkdir(parents=True, exist_ok=False)
    make_concept_visual(paths["concept_visual"])
    assembled = update_frontmatter(
        assembled,
        generation,
        paths["concept_visual"],
        paths["knowledge_root"],
    )
    assembled = insert_concept_visual(
        assembled,
        paths["concept_visual"],
        paths["knowledge_root"],
    )

    base.write_json(ASCII_SPEC, make_ascii_spec(paths["markdown"], generation))
    manual = base.notions_style_ascii_master.normalize_manual_spec_file(ASCII_SPEC)[
        TOPIC_KEY
    ]
    ascii_fragment = base.notions_style_ascii_master.build_manual_fragment(manual)
    standalone_ascii = base.notions_style_ascii_master.standalone_panel_text(
        ascii_fragment
    )
    assembled = base.philosophy_v2.replace_ascii_master(assembled, ascii_fragment)
    assembled = enhance_practice_quality(assembled)
    assembled, _ = base.philosophy_v2.rotate_mcqs(assembled)
    assembled = re.sub(
        r"\*\*Correct answer:\s*([A-D])\.\s*(.+?)\*\*",
        r"**Correct answer: \1** — \2",
        assembled,
    )
    assembled = base.philosophy_v2.wrap_code_fences(assembled)
    assembled = base.enrich_basic_sessions(assembled)
    assembled = assembled.replace(" ☝️", "").replace(" 👇", "")
    assembled = re.sub(r"(?m)^#{5,6}\s+", "#### ", assembled)
    base.write_text(paths["markdown"], assembled)

    workbook_markdown = base.extract_v2_workbook_markdown(assembled)
    base.write_text(paths["workbook_markdown"], workbook_markdown)
    base.write_json(paths["content_spec"], make_content_spec(generation, paths["markdown"]))

    content_errors, content_metrics = validate_content(
        assembled,
        workbook_markdown,
        standalone_ascii,
        source_pyqs,
    )
    if content_errors:
        raise ValueError(
            "Content validation failed:\n- " + "\n- ".join(content_errors)
        )

    paths["notes_root"].mkdir(parents=True, exist_ok=False)
    base.markdown_learning_pdf.build_pdf(
        paths["markdown"],
        paths["main_pdf"],
        mode="main",
        variant=base.V2_VARIANT,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
        visual_audit_path=paths["main_visual_map"],
    )
    base.markdown_learning_pdf.build_pdf(
        paths["markdown"],
        paths["workbook_pdf"],
        mode="workbook",
        variant=base.V2_VARIANT,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
        visual_audit_path=paths["workbook_visual_map"],
    )

    source_paths = [
        base.repo_path(CANONICAL_OWNER),
        base.repo_path(RETAINED_SESSION),
        base.repo_path(RETAINED_WORKBOOK),
        base.repo_path(ADVANCED_DOSSIER),
        base.repo_path(OFFICIAL_SYLLABUS),
        base.repo_path(PHILOSOPHY_README),
        base.repo_path(PYQ_LEDGER),
    ]
    source_hashes = base.deliverable_hashes(source_paths)
    preservation_before = base.deliverable_hashes(
        [
            *source_paths,
            *[
                ROOT / base.carvaka_flowchart.REFERENCE_FOLDER / name
                for name in base.carvaka_flowchart.REFERENCE_HASHES
            ],
        ]
    )
    graphical_panels = [
        {
            "title": panel.title,
            "structural_type": panel.structural_type,
            "body": panel.body,
            "source_references": [f"SESSION {number}" for number in raw["sessions"]],
        }
        for panel, raw in zip(manual.panels, ASCII_PANELS)
    ]
    graphical_data = base.carvaka_flowchart.author_topic_spec(
        topic_key=TOPIC_KEY,
        subject="Philosophy",
        title=TOPIC_TITLE,
        source_markdown=assembled.replace("...", " — ").replace("…", " — "),
        source_markdown_path=base.relative(paths["markdown"]),
        ascii_spec_path=base.relative(ASCII_SPEC),
        ascii_spec_sha256=base.sha256(ASCII_SPEC),
        panels=graphical_panels,
        source_generation=generation,
    )
    for index, stage in enumerate(graphical_data["stages"][:-1]):
        stage["answer_line"] = SESSION_SPECS[index]["answer"]
        stage["mechanism_strip"] = SESSION_SPECS[index]["mechanism"]
        stage["source_references"] = [
            f"SESSION {number}" for number in ASCII_PANELS[index]["sessions"]
        ]
    graphical_errors = base.carvaka_flowchart.validate_spec(graphical_data)
    if graphical_errors:
        raise ValueError(
            "Graphical spec validation failed:\n- "
            + "\n- ".join(graphical_errors)
        )
    base.write_json(paths["graphical_spec"], graphical_data)
    flow_metadata, render_result = base.carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_root"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    flow_metadata["approval"] = False
    flow_metadata["ascii_master_source"] = "manual-authored-hegel-spec"
    flow_metadata["ascii_master_spec"] = base.relative(ASCII_SPEC)
    flow_metadata["ascii_master_spec_sha256"] = base.sha256(ASCII_SPEC)

    ascii_pdf_metrics = render_ascii_pdf_safe(standalone_ascii, paths["ascii_pdf"])
    flow_metadata["ascii_master_pdf"] = base.relative(paths["ascii_pdf"])

    pdf_errors: list[str] = []
    pdf_errors.extend(
        base.validate_v2_paths(
            ROOT,
            paths["markdown"],
            paths["main_pdf"],
            TOPIC_KEY,
            "main",
        )
    )
    pdf_errors.extend(
        base.validate_v2_paths(
            ROOT,
            paths["markdown"],
            paths["workbook_pdf"],
            TOPIC_KEY,
            "workbook",
        )
    )
    pdf_errors.extend(
        base.validate_pdf(paths["main_pdf"], variant=base.V2_VARIANT, mode="main")
    )
    pdf_errors.extend(
        base.validate_pdf(
            paths["workbook_pdf"],
            variant=base.V2_VARIANT,
            mode="workbook",
        )
    )
    main_layout_errors, main_layout = base.validate_pdf_layout(paths["main_pdf"])
    workbook_layout_errors, workbook_layout = base.validate_pdf_layout(
        paths["workbook_pdf"]
    )
    pdf_errors.extend(f"main layout: {error}" for error in main_layout_errors)
    pdf_errors.extend(
        f"workbook layout: {error}" for error in workbook_layout_errors
    )
    pdf_errors.extend(
        f"graphical package: {error}"
        for error in render_result.validation_errors
    )
    if pdf_errors:
        raise ValueError("Rendered validation failed:\n- " + "\n- ".join(pdf_errors))

    main_metrics = base.pdf_metrics(paths["main_pdf"])
    workbook_metrics = base.pdf_metrics(paths["workbook_pdf"])
    if (
        main_metrics["replacement_glyphs"]
        or workbook_metrics["replacement_glyphs"]
        or main_metrics["blank_pages"]
        or workbook_metrics["blank_pages"]
        or not main_metrics["bookmarks"]
        or not workbook_metrics["bookmarks"]
    ):
        raise ValueError("PDF metrics contain blank pages, glyph defects or missing bookmarks.")

    output_files = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["concept_visual"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["main_visual_map"],
        paths["workbook_visual_map"],
        paths["ascii_pdf"],
        ASCII_SPEC,
        paths["content_spec"],
        paths["graphical_spec"],
        *[path for path in paths["flow_root"].rglob("*") if path.is_file()],
    ]
    record = build_record(
        generation,
        supersedes,
        legacy_id,
        paths,
        flow_metadata,
        source_hashes,
        output_files,
    )
    base.write_json(paths["record"], record)

    report = {
        "schema_version": 1,
        "generated_on": GENERATION_DATE,
        "record_id": record["record_id"],
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "approval": False,
        "canonical_sequence_number": CANONICAL_SEQUENCE_NUMBER,
        "official_syllabus_verbatim": OFFICIAL_CLAUSE,
        "section_manifest": base.relative(MANIFEST),
        "baseline_report": base.relative(BASELINE_REPORT),
        "sources": {
            "order": [
                "Markdown knowledge owners and retained layered package",
                "OCR/PDF evidence already reconciled in the source owners",
                "Live web not required for doctrine or PYQ wording",
                "Qdrant not required",
            ],
            "hashes": source_hashes,
        },
        "content_validation": {
            **content_metrics,
            "core_syllabus_complete_without_advanced": True,
            "advanced_optional_and_separated": True,
            "verified_pyq_wording_and_order": "passed",
            "mcq_rotation": "A->B->C->D",
            "strict_rotation_policy_registered": True,
            "workbook_distinct": True,
            "answer_grabbing_lines": "authored, unique and session-specific",
        },
        "deliverables": {
            "markdown": base.relative(paths["markdown"]),
            "workbook_markdown": base.relative(paths["workbook_markdown"]),
            "main_pdf": base.relative(paths["main_pdf"]),
            "workbook_pdf": base.relative(paths["workbook_pdf"]),
            "concept_visual": base.relative(paths["concept_visual"]),
            "ascii_spec": base.relative(ASCII_SPEC),
            "content_spec": base.relative(paths["content_spec"]),
            "graphical_spec": base.relative(paths["graphical_spec"]),
            "flowchart_folder": base.relative(paths["flow_root"]),
            "ascii_pdf": base.relative(paths["ascii_pdf"]),
            "hashes": base.deliverable_hashes(output_files),
        },
        "pdf_validation": {
            "main": main_metrics,
            "workbook": workbook_metrics,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
            "internal_indexes": "passed",
            "bookmarks": "passed",
            "empty_clipped_overflow_replacement_glyph_pages": "none",
        },
        "master_flow_validation": {
            "ascii_panel_count": len(manual.panels),
            "embedded_spec_equality": "passed",
            "standalone_spec_equality": "passed",
            "ascii_pdf": ascii_pdf_metrics,
            "graphical_metadata": flow_metadata,
            "graphical_validation_errors": render_result.validation_errors,
        },
        "manual_rendered_visual_inspection": {
            "state": "pending before tracker finalisation",
            "main_visual_pages": [],
            "workbook_visual_pages": [],
            "graphical_tiled_pages": render_result.audit.get("tiles", []),
            "repairs": [],
        },
        "tracker_finalisation": "pending manual rendered-visual inspection",
        "clean_library_publication": "pending tracker finalisation",
        "flow_learning_publication": "pending clean-library publication",
        "changed_files_manifest": base.relative(paths["changed"]),
    }
    base.write_json(paths["validation"], report)

    changed = {
        base.relative(Path(__file__)),
        base.relative(ROOT / "tools" / "philosophy_western_hegel_v2_spec.py"),
        base.relative(ROOT / "tools" / "validate_v2_export.py"),
        base.relative(ROOT / "tools" / "test_v2_export_foundation.py"),
        base.relative(MANIFEST),
        base.relative(BASELINE_REPORT),
        base.relative(ASCII_SPEC),
        base.relative(paths["content_spec"]),
        base.relative(paths["graphical_spec"]),
        base.relative(paths["record"]),
        base.relative(paths["validation"]),
        base.relative(paths["changed"]),
        base.relative(paths["markdown"]),
        base.relative(paths["workbook_markdown"]),
        base.relative(paths["concept_visual"]),
        base.relative(paths["main_pdf"]),
        base.relative(paths["workbook_pdf"]),
        base.relative(paths["main_visual_map"]),
        base.relative(paths["workbook_visual_map"]),
        base.relative(paths["ascii_pdf"]),
        *[
            base.relative(path)
            for path in paths["flow_root"].rglob("*")
            if path.is_file()
        ],
        *[
            base.relative(path)
            for path in (
                ROOT
                / "notes"
                / "Philosophy"
                / "learning-session-v2"
                / SECTION_KEY
                / "indexes"
            ).glob("*.md")
            if path.is_file()
        ],
    }
    base.write_text(
        paths["changed"],
        "\n".join(sorted(changed, key=str.casefold)) + "\n",
    )
    print(
        f"GENERATED: {record['record_id']}; manual visual inspection remains "
        f"before finalisation; report={base.relative(paths['validation'])}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        return run()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
