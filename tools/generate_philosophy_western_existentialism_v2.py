"""Generate Existentialism as a source-complete learner-v2 topic."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable

import fitz
from PIL import Image, ImageDraw, ImageFont

import generate_philosophy_western_moore_russell_early_wittgenstein_v2 as engine
import philosophy_western_existentialism_v2_spec as topic_spec


base = engine.base
INHERITED_ENRICH_BASIC_SESSIONS = base.enrich_basic_sessions
INHERITED_RENDER_ASCII_PDF_SAFE = base.render_ascii_pdf_safe
INHERITED_ASSEMBLE_LEGACY = base.philosophy_v2.assemble_legacy
INHERITED_PARSE_TABLE = base.markdown_learning_pdf.parse_table
ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-27"
GENERATION_DATE_DISPLAY = "27 August 2026"
EXPECTED_GENERATION = 3
SECTION_KEY = "paper-i-western-philosophy"
SECTION_FOLDER = "Paper-I-Western-Philosophy"
TOPIC_KEY = "philosophy-paper-i-western-philosophy-10"
TOPIC_TITLE = "Existentialism"
TOPIC_FOLDER = "topic-10"
CANONICAL_SEQUENCE_NUMBER = 10

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
    / "philosophy--paper-i-western-philosophy-10-ascii-2026-08-27-g3.json"
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
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\Existentialism.md"
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
    "Existentialism\\Existentialism_Layered-Complete-Learning-Session_2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Existentialism\\Existentialism_Layered-Solved-Practice-Workbook_2026-08-19.md"
)
BASELINE_REPORT = (
    EXPORT_MANIFEST_DIR
    / "philosophy-paper-i-western-philosophy-10-learner-v2-g3-"
    "2026-08-27-baseline.json"
)
OFFICIAL_CLAUSE = (
    "Existentialism (Kierkegaard, Sarte, Heidegger): Existence and Essence; "
    "Choice, Responsibility and Authentic Existence; Being-in-the-world and Temporality."
)
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
            knowledge_root / "assets" / "Existentialism-Family-Project-Map.png"
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
                "Philosophy Optional, Paper I, Western Philosophy topic 10: "
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
        "order. Topics 01-10 are materialised as learner-v2; topic 11 retains its "
        "independently resolved state."
    )
    return manifest


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1900, 1210
    image = Image.new("RGB", (width, height), "#071521")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 58)
    heading_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 31)
    body_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 24)
    small_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 20)

    draw.text(
        (width / 2, 54),
        "EXISTENTIALISM: ONE PROBLEM-FIELD, THREE PROJECTS",
        font=title_font,
        fill="#F8FAFC",
        anchor="ma",
    )
    draw.text(
        (width / 2, 138),
        "Concrete, finite existence resists reduction to a fixed essence or detached system",
        font=body_font,
        fill="#8DE7F7",
        anchor="ma",
    )
    draw.rounded_rectangle(
        (235, 195, 1665, 315),
        24,
        fill="#0E3042",
        outline="#65D9EC",
        width=4,
    )
    draw.text(
        (950, 234),
        "COMMON ORIENTATION",
        font=heading_font,
        fill="#FFFFFF",
        anchor="ma",
    )
    draw.text(
        (950, 279),
        "lived situation • individuality • choice • anxiety • responsibility • finitude",
        font=body_font,
        fill="#D7F5FA",
        anchor="ma",
    )

    cards = [
        (
            70,
            "#183B55",
            "KIERKEGAARD",
            "RELIGIOUS INWARDNESS",
            [
                "existing individual vs System",
                "subjectivity as appropriation",
                "aesthetic / ethical / religious",
                "anxiety, despair, leap and faith",
                "self responsibly before God",
            ],
        ),
        (
            670,
            "#293F68",
            "HEIDEGGER",
            "FUNDAMENTAL ONTOLOGY",
            [
                "Dasein: Being is an issue",
                "unitary being-in-the-world",
                "care and thrown projection",
                "the They, anxiety and death",
                "finite ecstatic temporality",
            ],
        ),
        (
            1270,
            "#4A315E",
            "SARTRE",
            "ATHEISTIC FREEDOM",
            [
                "existence precedes essence",
                "in-itself / for-itself",
                "facticity and transcendence",
                "choice, anguish, responsibility",
                "bad faith and the Look",
            ],
        ),
    ]
    for x, colour, name, subtitle, rows in cards:
        draw.rounded_rectangle(
            (x, 380, x + 560, 930),
            28,
            fill=colour,
            outline="#62DCEC",
            width=4,
        )
        draw.text(
            (x + 280, 425),
            name,
            font=heading_font,
            fill="#FFFFFF",
            anchor="ma",
        )
        draw.text(
            (x + 280, 473),
            subtitle,
            font=small_font,
            fill="#F8D27A",
            anchor="ma",
        )
        y = 545
        for row in rows:
            draw.ellipse((x + 48, y + 7, x + 62, y + 21), fill="#62DCEC")
            draw.text((x + 82, y), row, font=body_font, fill="#F2F6FA")
            y += 73

    draw.rounded_rectangle(
        (120, 985, 1780, 1145),
        22,
        fill="#0D2939",
        outline="#F8D27A",
        width=3,
    )
    draw.text(
        (950, 1020),
        "EXAMINER'S CENTRAL CAUTION",
        font=heading_font,
        fill="#FFF3C8",
        anchor="ma",
    )
    draw.text(
        (950, 1067),
        "Do not flatten faith, ontology and freedom into one slogan.",
        font=body_font,
        fill="#FFFFFF",
        anchor="ma",
    )
    draw.text(
        (950, 1110),
        "Anxiety is not fear; authenticity is not nonconformity; freedom is not omnipotence.",
        font=small_font,
        fill="#C6EEF4",
        anchor="ma",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = base.repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+10\.\s+Existentialism\s*(.*?)"
        r"(?=^##\s+11\.\s+Quine)",
        text,
    )
    if not match:
        raise ValueError("The Existentialism advanced dossier section was not found.")
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
        "# Existentialism — Learner-v2 Source-Complete Learning Session",
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
            'title: "Existentialism — Learner-v2"',
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
        f"\n\n![Existentialism family and distinct-project map]({image_path})\n\n"
        "*Concept map: the family shares the priority of concrete, finite existence, "
        "then divides into Kierkegaard's religious inwardness, Heidegger's fundamental "
        "ontology and Sartre's atheistic freedom.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def enrich_basic_sessions(text: str) -> str:
    return INHERITED_ENRICH_BASIC_SESSIONS(text)


def _reorder_session_section(
    text: str,
    start_pattern: str,
    end_pattern: str,
    session_pattern: str,
) -> str:
    section = re.search(
        rf"(?is)({start_pattern})(.*?)({end_pattern})",
        text,
        re.MULTILINE,
    )
    if not section:
        raise ValueError("The retained session section could not be isolated.")
    body = section.group(2)
    matches = list(re.finditer(session_pattern, body, re.MULTILINE))
    if len(matches) != 10:
        raise ValueError(
            f"Expected 10 retained session blocks before reordering, found {len(matches)}."
        )
    prefix = body[: matches[0].start()]
    chunks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        chunks.append(body[match.start() : end])
    order = (0, 1, 6, 7, 8, 2, 3, 4, 5, 9)
    reordered = prefix + "".join(chunks[index] for index in order)
    return text[: section.start(2)] + reordered + text[section.end(2) :]


def assemble_legacy(*args: Any, **kwargs: Any) -> str:
    text = INHERITED_ASSEMBLE_LEGACY(*args, **kwargs)
    text = _reorder_session_section(
        text,
        r"^##\s+BASIC LEARNING SESSION\s*$",
        r"^##\s+BASIC MCQS / REMEDIATION\s*$",
        r"^###\s+SESSION\s+\d+\s*[—-].+?$",
    )
    text = _reorder_session_section(
        text,
        r"^##\s+OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\s*$",
        r"^##\s+CONSOLIDATED REGISTER NOTES\s*$",
        r"^###\s+OPTIONAL DEPTH\s+\d+\s*[—-].+?$",
    )
    advanced = re.search(
        r"(?is)(^##\s+OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\s*$)"
        r"(.*?)"
        r"(?=^##\s+CONSOLIDATED REGISTER NOTES\s*$)",
        text,
        re.MULTILINE,
    )
    if not advanced:
        raise ValueError("The reordered Advanced section could not be isolated.")
    counter = iter(range(1, 11))
    body = re.sub(
        r"(?m)^###\s+OPTIONAL DEPTH\s+\d+\s*[—-]\s*",
        lambda _: f"### OPTIONAL DEPTH {next(counter)} — ",
        advanced.group(2),
    )
    text = text[: advanced.start(2)] + body + text[advanced.end(2) :]
    return text


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "Existentialism faith-ontology-freedom atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": "Philosophy Optional Paper I Western Philosophy topic 10 only",
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
                    "The approved Cārvāka design reference and every prior "
                    "Existentialism generation remain immutable."
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


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if "[Existentialism]" not in line:
            continue
        match = re.search(r"\):\*\*\s*(.+?)\s*$", line)
        if match:
            questions.append(match.group(1).strip().split(" 📝 ", 1)[0].strip())
    return questions


def enhance_practice_quality(text: str) -> str:
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
        "- **Qdrant:** optional fallback only; not required for this canonical topic.",
        "- **OCR-searchable local PDFs:** `Robert.Audi_The.Cambridge.Dictionary.of.Philosophy.pdf`, "
        "`a_new_history_of_western_philosophy_volume_4.pdf` and Nigel Warburton's "
        "`Philosophy: The Classics` were searched for Kierkegaard, Sartre, Heidegger, "
        "Dasein, anxiety, despair, bad faith, authenticity and being-in-the-world. "
        "They corroborate the Markdown owners but do not replace them.\n"
        "- **Qdrant:** optional fallback only; not required for this canonical topic.",
    )
    text = text.replace(
        "#### 4.2 Criticisms of Heidegger",
        "#### VISUAL — 4.2 Criticisms of Heidegger",
    )
    text = text.replace(
        "#### Common UPSC Traps",
        "#### VISUAL — Common UPSC Traps",
    )
    synthesis = """
### RN-11 - Complete Existentialist Distinction and Answer Spine
- **Family:** common priority of finite lived existence; distinct grounds of God, Being and atheistic freedom.
- **Kierkegaard:** existing individual, subjective appropriation, qualitative spheres, anxiety, despair and faith.
- **Heidegger:** Dasein, unitary being-in-the-world, equipment, care, the They, death and temporality.
- **Sartre:** in-itself/for-itself, nothingness, situated freedom, responsibility, bad faith and the Look.
- **Exact pairs:** fear/anxiety; facticity/determinism; freedom/power; authenticity/nonconformity; subjectivity/arbitrariness; being-in-world/containment; bad faith/lying; death/biological event.
- **Evaluation:** preserve each insight, state the strongest objection, answer it, and retain the residual limit.
- **Answer spine:** define -> locate thinker/project -> reconstruct argument -> distinguish -> object -> reply -> qualify.

"""
    if "### RN-P - Provenance" in text:
        text = text.replace("### RN-P - Provenance", synthesis + "### RN-P - Provenance", 1)
    return text


def render_ascii_pdf_safe(text: str, output_path: Path) -> dict[str, Any]:
    panels = base.notions_style_ascii_master.standalone_panel_blocks(text)
    if len(panels) != 10:
        raise ValueError(f"Expected 10 standalone ASCII panels, found {len(panels)}.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_path.with_suffix(".compact.pdf")
    document = fitz.open()
    width = 841.89
    margin_x = 30.0
    title_height = 31.0
    font_size = 10.5
    leading = 14.2
    bold_font = r"C:\Windows\Fonts\consolab.ttf"
    page_metrics: list[dict[str, Any]] = []
    for number, total, title, body in panels:
        heading = f"ASCII MASTER FLOW — PANEL {number}/{total}: {title}"
        lines = [heading, *body.splitlines()]
        height = 30.0 + title_height + (len(lines) - 1) * leading + 28.0
        page = document.new_page(width=width, height=height)
        page.draw_rect(
            fitz.Rect(margin_x, 18.0, width - margin_x, 18.0 + title_height),
            color=(0.08, 0.21, 0.33),
            fill=(0.08, 0.21, 0.33),
        )
        page.insert_font(fontname="existential-bold", fontfile=bold_font)
        heading_prefix = "ASCII MASTER FLOW "
        heading_suffix = (
            f" PANEL {number}/{total}: {title}"
        )
        heading_x = margin_x + 10.0
        page.insert_text(
            (heading_x, 38.5),
            heading_prefix,
            fontname="cobo",
            fontsize=font_size,
            color=(1, 1, 1),
        )
        heading_x += fitz.get_text_length(
            heading_prefix, fontname="cobo", fontsize=font_size
        )
        page.insert_text(
            (heading_x, 38.5),
            "—",
            fontname="existential-bold",
            fontsize=font_size,
            color=(1, 1, 1),
        )
        heading_x += font_size * 0.65
        page.insert_text(
            (heading_x, 38.5),
            heading_suffix,
            fontname="cobo",
            fontsize=font_size,
            color=(1, 1, 1),
        )
        y = 18.0 + title_height + 22.0
        for line in body.splitlines():
            page.insert_text(
                (margin_x + 10.0, y),
                line,
                fontname="cour",
                fontsize=font_size,
                color=(0.04, 0.10, 0.16),
            )
            y += leading
        page.draw_rect(
            fitz.Rect(margin_x, 18.0, width - margin_x, height - 18.0),
            color=(0.55, 0.65, 0.75),
            width=0.7,
        )
        page_metrics.append(
            {
                "page": number,
                "line_count": len(lines),
                "maximum_line_characters": max(map(len, lines)),
                "font_size_points": font_size,
                "page_size_points": [round(width, 2), round(height, 2)],
                "unused_vertical_space_points": round(height - y - 8.0, 2),
            }
        )
    document.set_metadata(
        {
            "title": "Existentialism ASCII Master Flowchart",
            "creator": "generate_philosophy_western_existentialism_v2.py",
        }
    )
    document.save(temporary, garbage=4, deflate=True)
    document.close()
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError("Existentialism ASCII PDF validation failed.")
    return {
        **validation,
        "page_metrics": page_metrics,
        "minimum_font_size_points": font_size,
        "content_sized_pages": True,
    }


def parse_table_compact(
    lines: list[str],
    start: int,
) -> tuple[Any, int]:
    table, next_index = INHERITED_PARSE_TABLE(lines, start)
    if table is None:
        return table, next_index
    preceding_heading = ""
    for line in reversed(lines[max(0, start - 8) : start]):
        if line.lstrip().startswith("#"):
            preceding_heading = line.lstrip("#").strip()
            break
    protected_tables = (
        "Criticisms of Sartre",
        "Criticisms of Heidegger",
        "Criticisms of Kierkegaard",
        "Common UPSC Traps",
    )
    if any(name in preceding_heading for name in protected_tables):
        return base.markdown_learning_pdf.KeepTogether(
            [
                table,
                base.markdown_learning_pdf.Spacer(
                    1,
                    0.9 * base.markdown_learning_pdf.cm,
                ),
            ]
        ), next_index
    return table, next_index


def build_record(
    generation: int,
    supersedes: str,
    legacy_id: str | None,
    paths: dict[str, Path],
    flow_metadata: dict[str, Any],
    source_hashes: dict[str, str],
    output_files: Iterable[Path],
) -> dict[str, Any]:
    flow_metadata["ascii_master_source"] = "manual-authored-existentialism-spec"
    record_id = f"{TOPIC_KEY}:{base.V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I "
            "— Western Philosophy — Existentialism"
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
                "tools/generate_philosophy_western_existentialism_v2.py "
                "+ tools/validate_v2_export.py"
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
        ascii_spec_path=ASCII_SPEC,
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
    completeness_markers = (
        "family of projects",
        "pessimism",
        "nihilism",
        "subjective whim",
        "Hegel",
        "existing individual",
        "mode of appropriation",
        "qualitative existential orientations",
        "dizziness of freedom",
        "not willing to be oneself",
        "defiantly willing to be oneself",
        "teleological suspension",
        "fundamental ontology",
        "Cartesian mind",
        "unitary structure",
        "worldhood",
        "ready-to-hand",
        "present-at-hand",
        "care",
        "thrownness",
        "projection",
        "fallenness",
        "anonymous norms",
        "not simply evil",
        "certain and indefinite",
        "neither recommends suicide",
        "formal existential modification",
        "future is structurally primary",
        "no divine artisan",
        "being-in-itself",
        "being-for-itself",
        "nihilation",
        "freedom is situated",
        "not blame for every event suffered",
        "abandonment or forlornness",
        "not ordinary lying",
        "less systematically developed",
        "social role",
        "the Look",
        "Kierkegaard's existing individual",
        "Heidegger analyses Dasein",
        "Sartre explains the for-itself",
        "facticity is not determinism",
        "freedom is not power",
        "authenticity is not mere nonconformity",
        "subjectivity is not arbitrariness",
        "being-in-the-world is not spatial containment",
        "bad faith is not ordinary lying",
        "biological event",
        "Beauvoir",
        "Merleau-Ponty",
    )
    for marker in completeness_markers:
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
    if len(keys) != 48 or keys != expected_keys:
        errors.append(
            f"Expected 48 MCQs in strict A->B->C->D rotation, found {len(keys)}."
        )
    for marker in (
        "Original Mains 1",
        "Original Mains 2",
        "Original Mains 3",
        "10-mark",
        "15-mark",
        "20-mark",
    ):
        if marker not in workbook_markdown:
            errors.append(f"Missing original marks-wise practice: {marker}")
    why_count = workbook_markdown.count("**Why this earns marks:**")
    if why_count != 17:
        errors.append(f"Expected 17 Why-this-earns-marks notes, found {why_count}.")
    if re.search(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", assembled, re.I):
        errors.append("Placeholder text is present.")
    if workbook_markdown.strip() == assembled.strip():
        errors.append("Workbook Markdown duplicates the complete learning session.")
    forbidden = (
        r"all existentialists (?:believe|teach|say) (?:that )?life is meaningless",
        r"Kierkegaard.{0,60}existence precedes essence",
        r"Heidegger.{0,60}existence precedes essence(?!.*reject)",
        r"authenticity (?:is|means) social isolation",
        r"freedom (?:is|means) (?:the )?power to change every",
        r"anxiety (?:is|means) (?:a )?stronger fear",
        r"bad faith (?:is|means) ordinary lying",
        r"being-in-the-world (?:is|means) spatial containment",
    )
    for pattern in forbidden:
        if re.search(pattern, core_text, re.I | re.S):
            errors.append(f"Forbidden simplification remains in Core: {pattern}")
    visual_count = len(re.findall(r"(?m)^####\s+VISUAL\s+—", core_text))
    if visual_count < 20:
        errors.append(f"Expected at least 20 explicit Core visuals, found {visual_count}.")
    return errors, {
        "core_session_count": len(core_sessions),
        "advanced_session_count": len(advanced_sessions),
        "answer_grabbing_line_count": len(normalized_answers),
        "verified_pyq_count": len(source_pyqs),
        "mcq_count": len(keys),
        "original_mains_practice_count": 3,
        "why_this_earns_marks_count": why_count,
        "explicit_core_visual_count": visual_count,
    }


base.philosophy_v2.assemble_legacy = assemble_legacy


for name, value in {
    "generation_paths": generation_paths,
    "planned_paths": planned_paths,
    "build_manifest": build_manifest,
    "make_concept_visual": make_concept_visual,
    "advanced_dossier_fragment": advanced_dossier_fragment,
    "update_frontmatter": update_frontmatter,
    "insert_concept_visual": insert_concept_visual,
    "enrich_basic_sessions": enrich_basic_sessions,
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
            "Local Markdown resolved doctrine, qualifications and exact PYQ wording. "
            "OCR sources corroborated the Kierkegaard, Heidegger and Sartre vocabulary "
            "without replacing the repository owners."
        ),
    }
    base.write_json(path, data)


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _tree_fingerprint(path: Path) -> dict[str, Any]:
    files = sorted(
        (item for item in path.rglob("*") if item.is_file()),
        key=lambda item: base.relative(item).casefold(),
    )
    aggregate = hashlib.sha256()
    total_bytes = 0
    for item in files:
        relative = base.relative(item)
        size = item.stat().st_size
        total_bytes += size
        aggregate.update(
            (
                relative
                + "\0"
                + str(size)
                + "\0"
                + _sha256(item)
                + "\n"
            ).encode("utf-8")
        )
    return {
        "exists": path.exists(),
        "file_count": len(files),
        "total_bytes": total_bytes,
        "aggregate_sha256": aggregate.hexdigest(),
    }


def _validate_concurrency_baseline() -> None:
    baseline = json.loads(BASELINE_REPORT.read_text(encoding="utf-8"))
    if baseline.get("planned_generation") != EXPECTED_GENERATION:
        raise ValueError("Concurrency baseline does not target the configured generation.")
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    generation, supersedes, _ = base.latest_identity(tracker, TOPIC_KEY)
    if generation != EXPECTED_GENERATION or supersedes != (
        f"{TOPIC_KEY}:{base.V2_VARIANT}:g{EXPECTED_GENERATION - 1}"
    ):
        raise ValueError(
            "Tracker identity changed after the concurrency snapshot: expected "
            f"g{EXPECTED_GENERATION} superseding g{EXPECTED_GENERATION - 1}."
        )
    errors: list[str] = []
    for section in ("shared_file_hashes", "source_hashes"):
        for relative, expected in baseline.get(section, {}).items():
            path = ROOT / relative
            if not path.is_file() or _sha256(path) != expected:
                errors.append(f"{section}: {relative}")
    for section in ("g2_immutable_snapshot",):
        for relative, expected in baseline.get(section, {}).get("trees", {}).items():
            actual = _tree_fingerprint(ROOT / relative)
            for key in ("exists", "file_count", "total_bytes", "aggregate_sha256"):
                if actual[key] != expected[key]:
                    errors.append(f"{section} tree: {relative}")
                    break
        for relative, expected in baseline.get(section, {}).get("files", {}).items():
            path = ROOT / relative
            if not path.is_file() or _sha256(path) != expected["sha256"]:
                errors.append(f"{section} file: {relative}")
    for relative, expected in baseline.get(
        "out_of_scope_tree_fingerprints", {}
    ).items():
        actual = _tree_fingerprint(ROOT / relative)
        for key in ("exists", "file_count", "total_bytes", "aggregate_sha256"):
            if actual[key] != expected[key]:
                errors.append(f"out-of-scope tree: {relative}")
                break
    if errors:
        raise ValueError(
            "Concurrency baseline changed before g3 generation:\n- "
            + "\n- ".join(errors)
        )


def run(expected_generation: int = EXPECTED_GENERATION) -> int:
    if expected_generation != EXPECTED_GENERATION:
        raise ValueError(
            "This topic-local regeneration is pinned to "
            f"g{EXPECTED_GENERATION}, not g{expected_generation}."
        )
    _validate_concurrency_baseline()
    original_run = engine.run

    def wrapped_build_record(*args: Any, **kwargs: Any) -> dict[str, Any]:
        return build_record(*args, **kwargs)

    engine.build_record = wrapped_build_record
    base.markdown_learning_pdf.parse_table = parse_table_compact
    result = original_run()
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
    _write_source_audit(paths["source_audit"], len(source_pyqs))
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
            *[p for p in paths["flow_root"].rglob("*") if p.is_file()],
        )
        if path.is_file()
    ]
    record["provenance"]["source_audit"] = base.relative(paths["source_audit"])
    record["provenance"]["deliverable_hashes"] = base.deliverable_hashes(output_files)
    base.write_json(paths["record"], record)
    report = json.loads(paths["validation"].read_text(encoding="utf-8"))
    report["deliverables"]["source_audit"] = base.relative(paths["source_audit"])
    report["deliverables"]["hashes"] = base.deliverable_hashes(output_files)
    base.write_json(paths["validation"], report)
    changed = set(paths["changed"].read_text(encoding="utf-8").splitlines())
    changed.update(
        {
            base.relative(Path(__file__)),
            base.relative(
                ROOT / "tools" / "philosophy_western_existentialism_v2_spec.py"
            ),
            base.relative(paths["source_audit"]),
        }
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
        help="Safety pin for this explicit topic regeneration.",
    )
    args = parser.parse_args()
    try:
        return run(args.expected_generation)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
