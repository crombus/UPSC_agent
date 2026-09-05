"""Generate one finalized learner-v2 Socio-Political Philosophy topic.

The section manifest always covers all ten official topics.  Content generation
is intentionally restricted to explicitly authored topic adapters so a one-topic
command cannot accidentally start later topics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import fitz
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart
import notions_style_ascii_master
import regenerate_philosophy_indian_v2 as philosophy_v2
from generate_v2_section_indexes import (
    generate_section_indexes,
    load_manifest,
    load_tracker,
    resolve_topic_states,
)
from validate_v2_export import (
    V2_VARIANT,
    validate_ascii_master_text,
    validate_pdf,
    validate_pdf_layout,
    validate_tracker_record,
    validate_v2_markdown_text,
)


ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-25"
SECTION_KEY = "paper-ii-socio-political-philosophy"
TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-01"
TOPIC_TITLE = "Social and Political Ideals"

MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-socio-political-philosophy.json"
)
ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "philosophy--paper-ii-socio-political-philosophy-ascii-2026-08-25.json"
)
GRAPHICAL_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-socio-political-philosophy-graphical-specs"
)
EXPORT_MANIFEST_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
GLOBAL_EXPORT_INDEX = ROOT / "EXPORT-PDF-COMMAND-INDEX.md"
V2_COMMAND_INDEX = ROOT / "V2-SUBJECT-SECTION-COMMAND-INDEX.md"
PHILOSOPHY_COMMAND_INDEX = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "LEARNING-SESSION-COMMAND-INDEX.md"
)
MASTER_LEARNING_INDEX = (
    ROOT / "upsc-ai-kit" / "knowledge" / "LEARNING-SESSION-COMMAND-INDEX.md"
)
TOPIC_CATALOG = (
    ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
)

KNOWLEDGE_OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
)
NOTES_OUTPUT = (
    ROOT
    / "notes"
    / "Philosophy"
    / "learning-session-v2"
    / SECTION_KEY
)
FLOW_ROOT = ROOT / "notes" / "Philosophy" / "flowcharts"

OFFICIAL_SYLLABUS = (
    "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md"
)
PHILOSOPHY_README = "upsc-ai-kit\\knowledge\\Philosophy\\README.md"
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\"
    "_PYQ-SocioPolitical-2018-2025.md"
)
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\"
    "Socio-Political-Dossier.md"
)
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Social-Political-Ideals.md"
)
RETAINED_SESSION = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
    "learning-sessions\\Social-Political-Ideals\\"
    "Social-Political-Ideals_Layered-Complete-Learning-Session_2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
    "learning-sessions\\Social-Political-Ideals\\"
    "Social-Political-Ideals_Layered-Solved-Practice-Workbook_2026-08-19.md"
)

TOPIC_DEFINITIONS = (
    (
        "Social and Political Ideals",
        "Social-Political-Ideals.md",
        "Social and Political Ideals: Equality, Justice and Liberty.",
        "Social-Political-Ideals",
        "Social-Political-Ideals",
        "2026-08-19",
    ),
    (
        "Sovereignty",
        "Sovereignty.md",
        "Sovereignty: Austin, Bodin, Laski and Kautilya.",
        "Sovereignty",
        "Sovereignty",
        "2026-08-19",
    ),
    (
        "Individual and State",
        "Individual-and-State.md",
        "Individual and State: Rights, Duties and Accountability.",
        "Individual-and-State",
        "Individual-and-State",
        "2026-08-19",
    ),
    (
        "Forms of Government",
        "Forms-of-Government.md",
        "Forms of Government: Monarchy, Theocracy and Democracy.",
        "Forms-of-Government",
        "Forms-of-Government",
        "2026-08-19",
    ),
    (
        "Political Ideologies",
        "Political-Ideologies.md",
        "Political Ideologies: Anarchism, Marxism and Socialism.",
        "Political-Ideologies",
        "Political-Ideologies",
        "2026-08-19",
    ),
    (
        "Humanism, Secularism and Multiculturalism",
        "Humanism-Secularism-Multiculturalism.md",
        "Humanism; Secularism; Multiculturalism.",
        "Humanism-Secularism-Multiculturalism",
        "Humanism-Secularism-Multiculturalism",
        "2026-08-19",
    ),
    (
        "Crime and Punishment",
        "Crime-and-Punishment.md",
        "Crime and Punishment: Corruption, Mass Violence, Genocide and Capital Punishment.",
        "Crime-and-Punishment",
        "Crime-and-Punishment",
        "2026-08-20",
    ),
    (
        "Development and Social Progress",
        "Development-Social-Progress.md",
        "Development and Social Progress.",
        "Development-and-Social-Progress",
        "Development-and-Social-Progress",
        "2026-08-20",
    ),
    (
        "Gender Discrimination",
        "Gender-Discrimination.md",
        "Gender Discrimination: Female Foeticide, Land and Property Rights, Empowerment.",
        "Gender-Discrimination",
        "Gender-Discrimination",
        "",
    ),
    (
        "Caste Discrimination: Gandhi and Ambedkar",
        "Caste-Gandhi-Ambedkar.md",
        "Caste Discrimination: Gandhi and Ambedkar.",
        "Caste-Gandhi-Ambedkar",
        "Caste-Gandhi-Ambedkar",
        "",
    ),
)

REQUIRED_TERMS = (
    "equal moral worth",
    "formal / legal equality",
    "political equality",
    "social equality",
    "economic equality",
    "equality of opportunity",
    "equality of outcome",
    "natural or physical inequality",
    "moral/political",
    "The Subjection of Women",
    "From each according to his ability, to each according to his need",
    "capabilities",
    "institutional justice (nīti)",
    "realised justice (nyāya)",
    "equality of resources",
    "negative liberty",
    "positive liberty",
    "harm to others",
    "self-regarding acts",
    "other-regarding acts",
    "T. H. Green",
    "non-domination",
    "distributive and corrective justice",
    "compensatory principle",
    "aggregation objection",
    "original position",
    "veil of ignorance",
    "difference principle",
    "reflective equilibrium",
    "entitlement theory",
    "public reasoning",
    "liberty, equality, fraternity",
    "justice mediates",
    "luck egalitarianism",
    "relational equality",
)

PANELS = (
    (
        "The triad and the ordering problem",
        "triadic mediation map",
        (
            "START -> political institutions distribute status, choice, burdens and benefits",
            "EQUALITY asks: in what respect must persons be treated as equals?",
            "LIBERTY asks: what protected sphere and effective agency must each person have?",
            "JUSTICE asks: what is due, by which rule, and with which rectification?",
            "liberty without fair conditions can protect accumulated power",
            "equality without relevant differentiation can become mechanical levelling",
            "justice mediates basic liberties, justified inequalities and equal civic dignity",
            "answer thesis -> the three ideals are distinct but institutionally interdependent",
        ),
    ),
    (
        "Equality from equal worth to real opportunity",
        "four-level equality ladder",
        (
            "equal moral worth -> arbitrary birth hierarchy bears the burden of justification",
            "formal or legal equality -> equality before law and equal protection",
            "political equality -> equal citizenship, vote and eligibility for public office",
            "social equality -> freedom from stigma, caste rank and inherited civic humiliation",
            "economic equality -> limits on disparities that destroy fair background conditions",
            "formal opportunity -> offices are legally open",
            "fair opportunity -> education, health and social power make access realistically open",
            "outcome concern -> use thresholds, needs or protection of the least advantaged",
            "trap -> equality is not sameness of talent, choice or final result",
        ),
    ),
    (
        "Rousseau Mill and Marx on unequal social power",
        "thinker contrast matrix",
        (
            "ROUSSEAU -> natural differences become domination through convention and property",
            "natural inequality -> age, strength, health and intelligence",
            "moral or political inequality -> wealth, honour, power and dependence",
            "MILL -> equal legal and civic status plus individuality and women's equality",
            "The Subjection of Women -> alleged natural subordination is socially manufactured",
            "MARX -> formally equal exchange can conceal class exploitation",
            "equal right can reproduce inequality when persons and needs differ",
            "higher communist rule -> contribution by ability and distribution by need",
            "comparison -> status equality, anti-subordination and material structure must connect",
        ),
    ),
    (
        "Equality of what and the metric decision",
        "metric decision tree",
        (
            "RESOURCE METRIC -> Dworkin equalises resources while distinguishing brute and option luck",
            "CAPABILITY METRIC -> Sen asks what persons are actually able to do and be",
            "same resources can yield unequal freedom because conversion conditions differ",
            "COHEN -> institutions alone are insufficient when incentives express an unequal ethos",
            "LUCK EGALITARIANISM -> correct disadvantage traceable to brute luck",
            "RELATIONAL EQUALITY -> end hierarchy, humiliation and second-class civic standing",
            "Indian use -> distinguish equal rule, access, capability and equal social status",
            "trap -> no single metric settles every question of need, choice, disability and dignity",
        ),
    ),
    (
        "Berlin and Mill on the protected sphere",
        "two-concept liberty comparison",
        (
            "NEGATIVE LIBERTY -> area in which one is left free from interference",
            "POSITIVE LIBERTY -> self-direction, autonomy and being one's own master",
            "Berlin warns -> rulers may coerce the empirical self for an alleged true self",
            "value pluralism -> political goods can conflict without one final harmony",
            "MILL'S HARM PRINCIPLE -> coercion is justified to prevent harm to others",
            "self-regarding conduct receives a strong presumption of liberty",
            "other-regarding harm permits regulation, but offence alone is not harm",
            "reply to spillovers -> liberty shifts the burden of proof onto coercion",
        ),
    ),
    (
        "From contract liberty to effective freedom",
        "contract-to-positive-freedom chain",
        (
            "HOBBES -> absence of external impediment; secure order makes residual liberty possible",
            "LOCKE -> liberty under known law protects life, liberty, property and consent",
            "ROUSSEAU -> autonomy is obedience to a law citizens prescribe through the general will",
            "GREEN -> real freedom is the capacity to develop and pursue worthwhile purposes",
            "poverty, ignorance and dependency can hollow out merely formal non-interference",
            "conflict -> unrestricted economic liberty can generate unequal social power",
            "complementarity -> a minimum equal status protects everyone's usable liberty",
            "qualified verdict -> enabling freedom must not become perfectionist compulsion",
        ),
    ),
    (
        "Technology domination and republican liberty",
        "domination mechanism map",
        (
            "modern technology expands communication, association and access to knowledge",
            "surveillance, behavioural profiling and platform dependence alter the freedom relation",
            "INTERFERENCE is an act; DOMINATION is exposure to uncontrolled arbitrary power",
            "Pettit's test -> can the affected person contest power on equal public terms?",
            "an indulgent master may not interfere yet still dominates through standing capacity",
            "rule-bound contestable law can constitute freedom rather than merely restrict it",
            "trap -> privacy, access and security must be analysed as liberty conditions, not slogans",
            "PYQ route -> assess whether technological society makes liberty unreal or differently fragile",
        ),
    ),
    (
        "Justice from harmony to proportion and repair",
        "classical justice matrix",
        (
            "PLATO -> justice is harmony when each part performs its proper function",
            "city and soul analogy -> reason governs with spirit while appetite remains ordered",
            "objection -> functional harmony can freeze hierarchy and suppress individual claims",
            "ARISTOTLE DISTRIBUTIVE JUSTICE -> proportionate shares by a relevant criterion",
            "criteria dispute -> merit, need, equality and desert produce rival distributions",
            "CORRECTIVE JUSTICE -> restore balance after voluntary or involuntary wrong",
            "compensation asks what loss occurred, who caused it and what repair is proportionate",
            "UTILITARIAN TEST -> aggregate welfare can sacrifice separate persons or minorities",
            "justice therefore needs both allocation and rectification",
        ),
    ),
    (
        "Rawls Nozick Sen and Ambedkar",
        "modern justice debate grid",
        (
            "RAWLS -> original position plus veil of ignorance models fair choice",
            "first principle -> equal basic liberties with lexical priority",
            "second principle -> fair equality of opportunity plus the difference principle",
            "NOZICK -> justice depends on acquisition, transfer and rectification, not a pattern",
            "minimal state protects entitlement but may preserve unequal starting structures",
            "SEN -> compare remediable injustice through capability and public reasoning",
            "institutional justice (nīti) differs from realised justice (nyāya) in actual lives",
            "AMBEDKAR -> political democracy fails without social equality and fraternity",
            "comparison -> fairness, entitlement, capability and anti-caste dignity order differently",
        ),
    ),
    (
        "Integrated verdict PYQ traps and answer spine",
        "integrative answer-writing rail",
        (
            "DEFINE -> state the strongest sense of the ideal named in the question",
            "DISTINGUISH -> status, opportunity, outcome; interference, mastery, domination",
            "ARGUE -> use one named thinker and explain the mechanism, not a decorative quotation",
            "COUNTER -> present the strongest objection or rival ordering principle",
            "INDIA -> use caste, gender, reservation or digital power only when concept-led",
            "PYQ anchors -> Mill, Rousseau, Marx, Berlin, Plato, Rawls, Nozick and Sen",
            "close-option trap -> liberty is not licence; equality is not sameness; justice is not law",
            "10 marks -> definition, distinction, thinker, objection, verdict",
            "15 or 20 marks -> compare positions, add Indian application and qualify the synthesis",
            "END -> justice orders liberty and equality without replacing either ideal",
        ),
    ),
)


@dataclass(frozen=True)
class LegacyTopic:
    key: str
    title: str


def repo_path(value: str | Path) -> Path:
    return ROOT / Path(str(value).replace("\\", os.sep).replace("/", os.sep))


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def hash_if_file(path: Path) -> str | None:
    return sha256(path) if path.is_file() else None


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".pending")
    pending.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(pending, path)


def latest_identity(
    tracker: dict[str, object],
    topic_key: str,
) -> tuple[int, str, str | None]:
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict) and record.get("topic_key") == topic_key
    ]
    learners = [
        record for record in records if record.get("variant") == V2_VARIANT
    ]
    legacy = [
        record for record in records if record.get("variant") == "legacy-v1"
    ]
    if learners:
        current = max(learners, key=lambda item: int(item.get("generation") or 1))
        generation = int(current["generation"]) + 1
        return generation, str(current["record_id"]), (
            str(max(legacy, key=lambda item: int(item.get("generation") or 1))["record_id"])
            if legacy
            else None
        )
    legacy_id = (
        str(max(legacy, key=lambda item: int(item.get("generation") or 1))["record_id"])
        if legacy
        else None
    )
    return 2, legacy_id or f"{topic_key}:legacy-v1:g1", legacy_id


def retained_paths(directory: str, stem: str, generated: str) -> dict[str, str]:
    if not generated:
        return {}
    root = (
        "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
        f"learning-sessions\\{directory}\\"
    )
    candidates = {
        "retained_learning_session": (
            root + f"{stem}_Layered-Complete-Learning-Session_{generated}.md"
        ),
        "retained_workbook": (
            root + f"{stem}_Layered-Solved-Practice-Workbook_{generated}.md"
        ),
    }
    return {
        key: value for key, value in candidates.items() if repo_path(value).is_file()
    }


def build_manifest(
    tracker: dict[str, object],
    generation: int,
) -> dict[str, object]:
    topics: list[dict[str, object]] = []
    for number, definition in enumerate(TOPIC_DEFINITIONS, 1):
        title, owner, syllabus, retained_dir, retained_stem, retained_date = definition
        key = f"philosophy-paper-ii-socio-political-philosophy-{number:02d}"
        _planned_generation, _supersedes, legacy_id = latest_identity(tracker, key)
        actual_generation = generation if number == 1 else 2
        markdown = (
            f"upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"
            f"{SECTION_KEY}\\{key}_Learning-Session.md"
        )
        notes = (
            f"notes\\Philosophy\\learning-session-v2\\{SECTION_KEY}\\notes\\"
            f"{key}_Learning-Session_{GENERATION_DATE}.pdf"
        )
        workbook = (
            f"notes\\Philosophy\\learning-session-v2\\{SECTION_KEY}\\workbooks\\"
            f"{key}_Solved-Workbook_{GENERATION_DATE}.pdf"
        )
        graphical = (
            f"notes\\Philosophy\\flowcharts\\{key}\\"
            f"continuous-at-a-glance-english-first-g{actual_generation}"
        )
        topic = {
            "topic_key": key,
            "display_title": title,
            "syllabus_mapping": (
                f"Philosophy Optional, Paper II, Socio-Political Philosophy "
                f"topic {number}: {syllabus}"
            ),
            "source_basic": (
                "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
                + owner
            ),
            "source_canonical": (
                "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
                + owner
            ),
            "source_advanced": ADVANCED_DOSSIER,
            "cross_topic_sources": [
                PHILOSOPHY_README,
                OFFICIAL_SYLLABUS,
            ],
            "verified_pyq_sources": [PYQ_LEDGER],
            "assembled_markdown": markdown,
            "notes_pdf": notes,
            "workbook_pdf": workbook,
            "ascii_master_spec": relative(ASCII_SPEC),
            "graphical_flowchart_folder": graphical,
            "superseded_v1": legacy_id,
        }
        topic.update(retained_paths(retained_dir, retained_stem, retained_date))
        topics.append(topic)
    return {
        "schema_version": 1,
        "variant": V2_VARIANT,
        "subject": {
            "key": "Philosophy",
            "display_name": "Philosophy Optional",
        },
        "section": {
            "key": SECTION_KEY,
            "name": "Philosophy Paper II — Socio-Political Philosophy",
            "scope": "official-section",
            "complete_syllabus_section": True,
            "syllabus_sources": [
                OFFICIAL_SYLLABUS,
                PHILOSOPHY_README,
                PYQ_LEDGER,
            ],
            "notes": (
                "Complete ten-topic official Socio-Political Philosophy section in "
                "syllabus/source order. Topic 01 is learner-v2 materialised; topics "
                "02-10 remain planned until separately generated and validated."
            ),
        },
        "topics": topics,
    }


def build_ascii_spec(markdown_path: Path, generation: int) -> dict[str, object]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Carvaka-standard continuous master with a manually authored, "
            "topic-specific Social and Political Ideals atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": (
            "Philosophy Optional Paper II Socio-Political Philosophy topic 01 only"
        ),
        "constraints": {
            "panel_count_per_topic": 10,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "english_first": True,
            "approved": False,
        },
        "topics": [
            {
                "topic_key": TOPIC_KEY,
                "title": TOPIC_TITLE,
                "source_markdown": relative(markdown_path),
                "source_record": f"{TOPIC_KEY}:{V2_VARIANT}:g{generation}",
                "approved_master_reference": (
                    "notes\\Philosophy\\flowcharts\\"
                    "philosophy-paper-i-indian-philosophy-01\\"
                    "continuous-at-a-glance-core-first\\"
                    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ),
                "benchmark_preservation": (
                    "The approved reference and all legacy-v1 Socio-Political "
                    "Philosophy artifacts remain immutable."
                ),
                "panels": [
                    {
                        "panel_title": title,
                        "structural_type": structural_type,
                        "source_session_heading_references": [title],
                        "lines": wrap_ascii_lines(lines),
                    }
                    for title, structural_type, lines in PANELS
                ],
            }
        ],
    }


def wrap_ascii_lines(lines: Iterable[str], width: int = 98) -> list[str]:
    result: list[str] = []
    for line in lines:
        if len(line) <= width:
            result.append(line)
            continue
        result.extend(
            textwrap.wrap(
                line,
                width=width,
                subsequent_indent="  ",
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    return result


def extract_advanced_topic(text: str) -> str:
    match = re.search(
        r"(?ims)^##\s+1\.\s+Social and Political Ideals\s*(.*?)"
        r"(?=^##\s+2\.\s+Sovereignty)",
        text,
    )
    if not match:
        raise ValueError("Advanced dossier topic 1 section could not be isolated.")
    return philosophy_v2.demote(match.group(1).strip(), 4)


def insert_advanced_dossier(text: str, advanced: str) -> str:
    marker = re.search(r"(?m)^##\s+CONSOLIDATED REGISTER NOTES\s*$", text)
    if not marker:
        raise ValueError("Cannot place the optional Advanced dossier before register notes.")
    block = "\n\n".join(
        [
            "### ADVANCED DOSSIER COMPLETENESS ADDENDUM",
            (
                "> **Classification: OPTIONAL ADVANCED.** This addendum is "
                "unnecessary for a competent core answer and must be used only "
                "after equality, liberty, justice and their core relations are secure."
            ),
            advanced,
        ]
    )
    return text[: marker.start()] + block + "\n\n" + text[marker.start() :]


def english_first_socio(text: str) -> str:
    replacements = (
        (
            "#### 3.7.1 Nīti and Nyāya",
            "#### 3.7.1 Institutional justice (nīti) and realised justice (nyāya)",
        ),
        (
            "**Nīti ✅:**",
            "**Institutional justice (nīti) ✅:**",
        ),
        (
            "**Nyāya ✅:**",
            "**Realised justice (nyāya) ✅:**",
        ),
        (
            "stress nīti/nyāya",
            "stress institutional justice (nīti) and realised justice (nyāya)",
        ),
        (
            "- nīti / nyāya ✅",
            "- institutional justice (nīti) / realised justice (nyāya) ✅",
        ),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1800, 1120
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 32)
    bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 58)
    label = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 42)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
    draw.rounded_rectangle(
        (48, 42, width - 48, height - 42),
        34,
        fill="#10283d",
        outline="#44d3ff",
        width=5,
    )
    draw.text(
        (95, 82),
        "SOCIAL AND POLITICAL IDEALS",
        font=bold,
        fill="#f1f8fc",
    )
    draw.text(
        (98, 160),
        "A triad of equal standing, protected agency and fair ordering",
        font=regular,
        fill="#a9c4d5",
    )
    centres = {
        "EQUALITY": (480, 465, "#44d3ff"),
        "LIBERTY": (1320, 465, "#43e2c0"),
        "JUSTICE": (900, 835, "#ffcf76"),
    }
    for left, right in (("EQUALITY", "LIBERTY"), ("EQUALITY", "JUSTICE"), ("LIBERTY", "JUSTICE")):
        draw.line(
            (centres[left][0], centres[left][1], centres[right][0], centres[right][1]),
            fill="#49677c",
            width=12,
        )
    descriptions = {
        "EQUALITY": "equal moral worth\nstatus • opportunity • capability",
        "LIBERTY": "non-interference\nself-direction • non-domination",
        "JUSTICE": "fairness • entitlement\ncapability • rectification",
    }
    for title, (x, y, colour) in centres.items():
        draw.ellipse((x - 230, y - 150, x + 230, y + 150), fill="#173b55", outline=colour, width=7)
        title_box = draw.textbbox((0, 0), title, font=label)
        draw.text(
            (x - (title_box[2] - title_box[0]) / 2, y - 84),
            title,
            font=label,
            fill=colour,
        )
        for index, line in enumerate(descriptions[title].splitlines()):
            box = draw.textbbox((0, 0), line, font=small)
            draw.text(
                (x - (box[2] - box[0]) / 2, y - 10 + index * 39),
                line,
                font=small,
                fill="#edf7fb",
            )
    draw.rounded_rectangle(
        (230, 1000, width - 230, 1070),
        18,
        fill="#27445b",
        outline="#ffcf76",
        width=3,
    )
    footer = "Justice orders liberty and equality without replacing either ideal."
    box = draw.textbbox((0, 0), footer, font=regular)
    draw.text(
        ((width - (box[2] - box[0])) / 2, 1015),
        footer,
        font=regular,
        fill="#fff4d6",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def update_frontmatter(
    text: str,
    generation: int,
    concept_visual: Path,
) -> str:
    _, body = philosophy_v2.strip_frontmatter(text)
    body = re.sub(
        r"(?m)^#\s+.+?Learner-v2.*$",
        f"# {TOPIC_TITLE} — Learner-v2 Source-Complete Learning Session",
        body,
        count=1,
    )
    body = re.sub(
        r"(?m)^>\s+\*\*Evidence discipline:\*\*",
        (
            f"> **Generation:** g{generation}, 25 August 2026 · "
            "**Approval:** false pending explicit topic approval\n>\n"
            "> **Evidence discipline:**"
        ),
        body,
        count=1,
    )
    front = "\n".join(
        [
            "---",
            f'title: "{TOPIC_TITLE} — Learner-v2"',
            f"topic_key: {TOPIC_KEY}",
            (
                "cover_image: "
                + concept_visual.relative_to(KNOWLEDGE_OUTPUT).as_posix()
            ),
            "variant: learner-v2",
            f"generation: {generation}",
            f"generation_date: {GENERATION_DATE}",
            "---",
            "",
        ]
    )
    return front + body.lstrip()


def insert_concept_visual(text: str, concept_visual: Path) -> str:
    marker = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", text)
    if not marker:
        raise ValueError("BASIC LEARNING SESSION is missing.")
    relative_image = concept_visual.relative_to(KNOWLEDGE_OUTPUT).as_posix()
    block = (
        f"\n\n![{TOPIC_TITLE} equality-liberty-justice concept map]"
        f"({relative_image})\n\n"
        "*Concept map: equality supplies equal standing, liberty protects agency, "
        "and justice orders their institutional relationship.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def normalized_preservation_lines(text: str) -> set[str]:
    text = philosophy_v2.remove_image_references(text)
    _, body = philosophy_v2.strip_frontmatter(text)
    result: set[str] = set()
    for line in body.splitlines():
        if re.match(r"^#(?!#)\s+", line.strip()):
            continue
        stripped = re.sub(r"^#{1,6}\s+", "", line.strip())
        if not stripped or stripped.startswith("Progress:"):
            continue
        if re.fullmatch(r"LAYER\s+[1-5]\s*[-—].*", stripped, re.I):
            continue
        if stripped.startswith("PART II"):
            continue
        normalized = re.sub(r"\s+", " ", stripped)
        if len(normalized) >= 18:
            result.add(normalized)
    return result


def preservation_audit(
    retained_main: str,
    retained_workbook: str,
    assembled_before_rotation: str,
) -> dict[str, object]:
    main_body = philosophy_v2.strip_frontmatter(retained_main)[1]
    teaching = re.split(
        r"(?im)^#\s+PART II\s*[-—].*$",
        main_body,
        maxsplit=1,
    )[0]
    register_match = re.search(
        r"(?im)^#{1,6}\s+(?:FINAL\s+)?CONSOLIDATED REGISTER NOTES(?:\s*[-—].*)?\s*$",
        main_body,
    )
    register = (
        main_body[register_match.end() :]
        if register_match
        else ""
    )
    source_lines = (
        normalized_preservation_lines(teaching)
        | normalized_preservation_lines(register)
        | normalized_preservation_lines(retained_workbook)
    )
    output_lines = normalized_preservation_lines(assembled_before_rotation)
    missing = sorted(source_lines - output_lines, key=str.casefold)
    return {
        "source_unique_substantive_lines": len(source_lines),
        "preserved_unique_substantive_lines": len(source_lines) - len(missing),
        "missing_count": len(missing),
        "missing_sample": missing[:20],
        "passed": not missing,
    }


def count_owner_pyqs(ledger: str) -> int:
    return len(
        re.findall(
            r"Primary owner:\*\* \[Social and Political Ideals\]",
            ledger,
        )
    )


def count_solved_pyqs(markdown: str) -> int:
    return len(re.findall(r"(?m)^#{3,6}\s+Solved PYQ\s+\d+\b", markdown))


def pdf_metrics(path: Path) -> dict[str, object]:
    with fitz.open(path) as document:
        text = "\n".join(page.get_text("text") for page in document)
        return {
            "pages": document.page_count,
            "bookmarks": len(document.get_toc(simple=True)),
            "replacement_glyphs": text.count("\ufffd"),
            "empty_text_pages": [
                number
                for number, page in enumerate(document, 1)
                if len(page.get_text("text").strip()) < 20
            ],
        }


def validate_markdown_content(
    markdown: str,
    standalone: str,
    keys: list[str],
    source_pyqs: int,
    preservation: dict[str, object],
) -> list[str]:
    errors = validate_v2_markdown_text(markdown)
    ascii_match = re.search(
        r"(?is)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
        markdown,
        re.MULTILINE,
    )
    if not ascii_match:
        errors.append("Embedded ASCII master is missing from final register notes.")
    else:
        errors.extend(
            validate_ascii_master_text(
                ascii_match.group(1),
                topic_key=TOPIC_KEY,
                standalone_text=standalone,
            )
        )
    folded = markdown.casefold()
    for term in REQUIRED_TERMS:
        if term.casefold() not in folded:
            errors.append(f"Required source-grounded term is missing: {term}")
    if count_solved_pyqs(markdown) != source_pyqs:
        errors.append(
            f"Verified PYQ mismatch: expected {source_pyqs}, "
            f"found {count_solved_pyqs(markdown)}."
        )
    expected_keys = ["ABCD"[index % 4] for index in range(len(keys))]
    if len(keys) < 48 or keys != expected_keys:
        errors.append(
            "MCQs/remediation do not follow the complete strict A->B->C->D rotation."
        )
    for marker in ("Original 10-marker", "Original 15-marker", "Original 20-marker"):
        if marker not in markdown:
            errors.append(f"Missing model-answer mark level: {marker}")
    if not preservation.get("passed"):
        errors.append(
            "Retained layered source preservation failed: "
            f"{preservation.get('missing_count')} substantive lines are missing."
        )
    if re.search(r"(?<!\()nīti(?!\))|(?<!\()nyāya(?!\))", markdown, re.I):
        errors.append(
            "Indic terminology is not consistently English-first with immediate IAST."
        )
    advanced = re.search(
        r"(?is)^##\s+OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
        r"\s*(.*?)^##\s+CONSOLIDATED REGISTER NOTES",
        markdown,
        re.MULTILINE,
    )
    if not advanced or "ADVANCED DOSSIER COMPLETENESS ADDENDUM" not in advanced.group(1):
        errors.append("Advanced dossier content is not isolated in the optional block.")
    return errors


def deliverable_hashes(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def create_record(
    generation: int,
    supersedes: str,
    legacy_id: str | None,
    markdown: Path,
    main_pdf: Path,
    workbook_pdf: Path,
    concept_visual: Path,
    flow_metadata: dict[str, object],
    source_hashes: dict[str, str],
    outputs: Iterable[Path],
) -> dict[str, object]:
    record_id = f"{TOPIC_KEY}:{V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper II "
            "— Socio-Political Philosophy — Social and Political Ideals"
        ),
        "main_pdf": relative(main_pdf),
        "workbook": relative(workbook_pdf),
        "markdown": relative(markdown),
        "approved": False,
        "provenance": {
            "workflow": (
                "learner-first-v2-philosophy-socio-political-section-one-topic"
            ),
            "source_basic": CANONICAL_OWNER,
            "source_canonical": CANONICAL_OWNER,
            "source_advanced": ADVANCED_DOSSIER,
            "legacy_v1_source_package": RETAINED_SESSION,
            "legacy_v1_workbook": RETAINED_WORKBOOK,
            "pyq_corpus": PYQ_LEDGER,
            "official_syllabus": OFFICIAL_SYLLABUS,
            "philosophy_readme": PHILOSOPHY_README,
            "assembled_markdown": relative(markdown),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": "2.1 learner-v2 indexed renderer",
            },
            "generation_date": GENERATION_DATE,
            "superseded_v1": legacy_id,
            "english_first": True,
            "source_hashes": source_hashes,
            "deliverable_hashes": deliverable_hashes(outputs),
            "concept_visual": relative(concept_visual),
            "graphical_renderer": {
                "name": carvaka_flowchart.RENDERER_NAME,
                "version": carvaka_flowchart.RENDERER_VERSION,
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
                "tools/generate_philosophy_socio_political_v2.py + "
                "tools/validate_v2_export.py"
            ),
        },
        "generated_on": GENERATION_DATE,
        "continuous_core_first": flow_metadata,
    }


def run_command(command: list[str], description: str) -> dict[str, object]:
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    output = (completed.stdout + "\n" + completed.stderr).strip()
    result = {
        "description": description,
        "command": subprocess.list2cmdline(command),
        "returncode": completed.returncode,
        "output_tail": output.splitlines()[-30:],
    }
    if completed.returncode:
        raise RuntimeError(
            f"{description} failed with exit code {completed.returncode}:\n{output}"
        )
    return result


def shared_snapshot(paths: Iterable[Path]) -> dict[str, str | None]:
    return {relative(path): hash_if_file(path) for path in paths}


def verify_final_state(
    generation: int,
    markdown: Path,
    main_pdf: Path,
    workbook_pdf: Path,
) -> dict[str, object]:
    tracker_errors = validate_tracker_record(
        TRACKER,
        TOPIC_KEY,
        V2_VARIANT,
        generation,
        repository_root=ROOT,
        check_paths=True,
    )
    if tracker_errors:
        raise ValueError("Tracker validation failed:\n- " + "\n- ".join(tracker_errors))
    manifest = load_manifest(MANIFEST)
    records = load_tracker(TRACKER)
    states = resolve_topic_states(ROOT, manifest, records)
    if len(states) != 10:
        raise ValueError(f"Section manifest resolved {len(states)} topics instead of 10.")
    if states[0].package_state != "generated":
        raise ValueError(
            f"Topic 01 state is {states[0].package_state!r}, expected generated."
        )
    later_states = [state.package_state for state in states[1:]]
    if any(state != "planned" for state in later_states):
        raise ValueError(
            "Topics 02-10 were unexpectedly marked beyond planned: "
            + ", ".join(later_states)
        )
    index_dir = NOTES_OUTPUT / "indexes"
    required_indexes = [
        index_dir / "TOPIC-COVERAGE-INDEX.md",
        index_dir / "NOTES-PDF-INDEX.md",
        index_dir / "WORKBOOK-PDF-INDEX.md",
    ]
    for path in required_indexes:
        if not path.is_file():
            raise ValueError(f"Required section index is missing: {relative(path)}")
    export_text = GLOBAL_EXPORT_INDEX.read_text(encoding="utf-8")
    if f"**learner-first v2:** g{generation}" not in export_text[
        max(0, export_text.find(TOPIC_KEY) - 500) : export_text.find(TOPIC_KEY) + 1000
    ]:
        raise ValueError("Global export index does not show the new learner-v2 generation.")
    guide_text = V2_COMMAND_INDEX.read_text(encoding="utf-8")
    command = (
        "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper II — "
        "Socio-Political Philosophy — Social and Political Ideals — Regenerate"
    )
    if command not in guide_text:
        raise ValueError("V2 section command guide did not become generation-aware.")
    philosophy_text = PHILOSOPHY_COMMAND_INDEX.read_text(encoding="utf-8")
    if (
        "Social and Political Ideals" not in philosophy_text
        or "learner-v2 available" not in philosophy_text[
            max(0, philosophy_text.find("Social and Political Ideals") - 200) :
            philosophy_text.find("Social and Political Ideals") + 500
        ]
    ):
        raise ValueError("Philosophy command index does not show learner-v2 availability.")
    forbidden = "notes\\Final-Learning-Packages"
    for path in (relative(markdown), relative(main_pdf), relative(workbook_pdf)):
        if forbidden.casefold() in path.casefold():
            raise ValueError("This learner-v2 generation exported to the forbidden Final path.")
    return {
        "manifest_topic_count": len(states),
        "topic_01_state": states[0].package_state,
        "topics_02_10_states": later_states,
        "approval": states[0].approval_state,
        "validation": states[0].validation_state,
        "section_indexes": [relative(path) for path in required_indexes],
        "global_export_index_consistent": True,
        "v2_command_index_consistent": True,
        "philosophy_command_index_consistent": True,
        "final_learning_packages_exported": False,
    }


def run(topic_number: int) -> int:
    if topic_number != 1:
        raise ValueError(
            "Only topic 01 has an authored learner-v2 adapter in this run; "
            "topics 02-10 must remain planned."
        )
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    if tracker.get("schema_version") != 2 or not isinstance(tracker.get("exports"), list):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
    generation, supersedes, legacy_id = latest_identity(tracker, TOPIC_KEY)
    record_id = f"{TOPIC_KEY}:{V2_VARIANT}:g{generation}"
    markdown = KNOWLEDGE_OUTPUT / f"{TOPIC_KEY}_Learning-Session.md"
    main_pdf = (
        NOTES_OUTPUT
        / "notes"
        / f"{TOPIC_KEY}_Learning-Session_{GENERATION_DATE}.pdf"
    )
    workbook_pdf = (
        NOTES_OUTPUT
        / "workbooks"
        / f"{TOPIC_KEY}_Solved-Workbook_{GENERATION_DATE}.pdf"
    )
    concept_visual = (
        KNOWLEDGE_OUTPUT
        / "assets"
        / TOPIC_KEY
        / "social-political-ideals-triad.png"
    )
    graphical_spec = GRAPHICAL_SPEC_DIR / f"{TOPIC_KEY}-g{generation}.json"
    flow_dir = (
        FLOW_ROOT
        / TOPIC_KEY
        / f"continuous-at-a-glance-english-first-g{generation}"
    )
    stem = (
        f"{TOPIC_KEY}-learner-v2-g{generation}-{GENERATION_DATE}"
    )
    record_file = EXPORT_MANIFEST_DIR / f"{stem}-record.json"
    validation_report = EXPORT_MANIFEST_DIR / f"{stem}-validation.json"
    changed_files_report = EXPORT_MANIFEST_DIR / f"{stem}-changed-files.txt"

    targets = (
        markdown,
        main_pdf,
        workbook_pdf,
        concept_visual,
        graphical_spec,
        flow_dir,
        record_file,
        validation_report,
        changed_files_report,
    )
    existing_targets = [path for path in targets if path.exists()]
    if existing_targets:
        raise ValueError(
            "Refusing to overwrite learner-v2 generation targets:\n- "
            + "\n- ".join(relative(path) for path in existing_targets)
        )

    shared_candidates = (
        TRACKER,
        GLOBAL_EXPORT_INDEX,
        V2_COMMAND_INDEX,
        PHILOSOPHY_COMMAND_INDEX,
        MASTER_LEARNING_INDEX,
        TOPIC_CATALOG,
        MANIFEST,
        ASCII_SPEC,
    )
    before = shared_snapshot(shared_candidates)

    manifest = build_manifest(tracker, generation)
    write_json(MANIFEST, manifest)
    generate_section_indexes(ROOT, MANIFEST, TRACKER)

    write_json(ASCII_SPEC, build_ascii_spec(markdown, generation))
    manual = notions_style_ascii_master.normalize_manual_spec_file(ASCII_SPEC)[
        TOPIC_KEY
    ]
    fragment = notions_style_ascii_master.build_manual_fragment(manual)
    standalone = notions_style_ascii_master.standalone_panel_text(fragment)

    retained_main_text = repo_path(RETAINED_SESSION).read_text(encoding="utf-8")
    retained_workbook_text = repo_path(RETAINED_WORKBOOK).read_text(encoding="utf-8")
    advanced_text = repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    ledger_text = repo_path(PYQ_LEDGER).read_text(encoding="utf-8")
    source_pyqs = count_owner_pyqs(ledger_text)
    if source_pyqs != 14:
        raise ValueError(
            f"Expected 14 verified owner PYQs in the ledger, found {source_pyqs}."
        )

    assembled = philosophy_v2.assemble_legacy(
        LegacyTopic(TOPIC_KEY, TOPIC_TITLE),
        retained_main_text,
        retained_workbook_text,
    )
    assembled = insert_advanced_dossier(
        assembled,
        extract_advanced_topic(advanced_text),
    )
    preservation = preservation_audit(
        retained_main_text,
        retained_workbook_text,
        assembled,
    )
    assembled = english_first_socio(assembled)
    make_concept_visual(concept_visual)
    assembled = update_frontmatter(assembled, generation, concept_visual)
    assembled = insert_concept_visual(assembled, concept_visual)
    assembled = philosophy_v2.replace_ascii_master(assembled, fragment)
    assembled, keys = philosophy_v2.rotate_mcqs(assembled)
    assembled = philosophy_v2.wrap_code_fences(assembled)
    markdown.parent.mkdir(parents=True, exist_ok=True)
    markdown.write_text(assembled, encoding="utf-8")
    markdown_errors = validate_markdown_content(
        assembled,
        standalone,
        keys,
        source_pyqs,
        preservation,
    )
    if markdown_errors:
        markdown.unlink(missing_ok=True)
        concept_visual.unlink(missing_ok=True)
        raise ValueError(
            "Markdown/content validation failed:\n- "
            + "\n- ".join(markdown_errors)
        )

    philosophy_v2.render_pdfs(
        markdown,
        main_pdf,
        workbook_pdf,
        TOPIC_KEY,
    )

    source_paths = [
        repo_path(path)
        for path in (
            CANONICAL_OWNER,
            RETAINED_SESSION,
            RETAINED_WORKBOOK,
            ADVANCED_DOSSIER,
            OFFICIAL_SYLLABUS,
            PHILOSOPHY_README,
            PYQ_LEDGER,
        )
    ]
    source_hashes = deliverable_hashes(source_paths)
    preservation_before = deliverable_hashes(
        [
            *source_paths,
            *[
                ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
                for name in carvaka_flowchart.REFERENCE_HASHES
            ],
        ]
    )
    graphical_panels = [
        {
            "title": panel.title,
            "structural_type": panel.structural_type,
            "body": panel.body,
            "source_references": list(panel.source_references),
        }
        for panel in manual.panels
    ]
    graphical_data = carvaka_flowchart.author_topic_spec(
        topic_key=TOPIC_KEY,
        subject="Philosophy",
        title=TOPIC_TITLE,
        source_markdown=assembled.replace("...", " — ").replace("…", " — "),
        source_markdown_path=relative(markdown),
        ascii_spec_path=relative(ASCII_SPEC),
        ascii_spec_sha256=sha256(ASCII_SPEC),
        panels=graphical_panels,
        source_generation=generation,
    )
    write_json(graphical_spec, graphical_data)
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        graphical_spec,
        flow_dir,
        ascii_master_bytes=standalone.encode("utf-8"),
        preservation_before=preservation_before,
    )
    flow_metadata["approval"] = False
    flow_metadata["ascii_master_source"] = "manually-authored-topic-specific-spec"
    flow_metadata["ascii_master_spec"] = relative(ASCII_SPEC)
    flow_metadata["ascii_master_spec_sha256"] = sha256(ASCII_SPEC)

    pdf_errors = []
    pdf_errors.extend(validate_pdf(main_pdf, variant=V2_VARIANT, mode="main"))
    pdf_errors.extend(
        validate_pdf(workbook_pdf, variant=V2_VARIANT, mode="workbook")
    )
    main_layout_errors, main_layout = validate_pdf_layout(main_pdf)
    workbook_layout_errors, workbook_layout = validate_pdf_layout(workbook_pdf)
    pdf_errors.extend(f"main layout: {error}" for error in main_layout_errors)
    pdf_errors.extend(
        f"workbook layout: {error}" for error in workbook_layout_errors
    )
    if render_result.validation_errors:
        pdf_errors.extend(
            f"graphical package: {error}"
            for error in render_result.validation_errors
        )
    if pdf_errors:
        raise ValueError(
            "PDF/graphical validation failed:\n- " + "\n- ".join(pdf_errors)
        )

    output_files = [
        markdown,
        concept_visual,
        main_pdf,
        workbook_pdf,
        ASCII_SPEC,
        graphical_spec,
        *[path for path in flow_dir.rglob("*") if path.is_file()],
    ]
    record = create_record(
        generation,
        supersedes,
        legacy_id,
        markdown,
        main_pdf,
        workbook_pdf,
        concept_visual,
        flow_metadata,
        source_hashes,
        output_files,
    )
    write_json(record_file, record)

    finalization_result = run_command(
        [
            sys.executable,
            str(ROOT / "tools" / "finalize_v2_topic.py"),
            "--repository-root",
            str(ROOT),
            "--manifest",
            str(MANIFEST),
            "--record-file",
            str(record_file),
        ],
        "Finalize learner-v2 topic",
    )
    guide_result = run_command(
        [
            sys.executable,
            str(ROOT / "tools" / "generate_v2_section_indexes.py"),
            "--repository-root",
            str(ROOT),
            "--guide-only",
        ],
        "Refresh V2 subject/section command guide",
    )
    philosophy_index_result = run_command(
        [
            sys.executable,
            str(ROOT / "tools" / "generate_learning_session_command_indexes.py"),
        ],
        "Refresh Philosophy learning-session command index",
    )
    tests = [
        run_command(
            [
                sys.executable,
                "-m",
                "unittest",
                "tools.test_v2_section_indexes",
                "tools.test_v2_topic_command_catalog",
                "tools.test_v2_export_foundation",
            ],
            "Run section, catalog and export-foundation tests",
        )
    ]
    final_state = verify_final_state(
        generation,
        markdown,
        main_pdf,
        workbook_pdf,
    )

    main_metrics = pdf_metrics(main_pdf)
    workbook_metrics = pdf_metrics(workbook_pdf)
    if not main_metrics["bookmarks"] or not workbook_metrics["bookmarks"]:
        raise ValueError("Expected PDF bookmarks were not generated.")
    if (
        main_metrics["replacement_glyphs"]
        or workbook_metrics["replacement_glyphs"]
        or main_metrics["empty_text_pages"]
        or workbook_metrics["empty_text_pages"]
    ):
        raise ValueError("Final PDF metrics contain empty pages or replacement glyphs.")

    report = {
        "schema_version": 1,
        "generated_on": GENERATION_DATE,
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": V2_VARIANT,
        "generation": generation,
        "approval": False,
        "section": {
            "key": SECTION_KEY,
            "manifest": relative(MANIFEST),
            "official_topic_count": 10,
            "generated_topics": [TOPIC_KEY],
            "planned_topics": [
                f"philosophy-paper-ii-socio-political-philosophy-{number:02d}"
                for number in range(2, 11)
            ],
        },
        "sources": {
            "order": [
                "Canonical and retained Markdown knowledge files",
                "OCR/PDF evidence already reconciled in the retained layered source",
                "No forced live-current-affairs insertion",
                "Qdrant not required",
            ],
            "hashes": source_hashes,
            "verified_pyq_owner_count": source_pyqs,
        },
        "content_validation": {
            "required_h2_order": [
                "BASIC LEARNING SESSION",
                "BASIC MCQS / REMEDIATION",
                "PYQS AND ANSWER PRACTICE",
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                "CONSOLIDATED REGISTER NOTES",
            ],
            "h2_order_passed": True,
            "register_notes_last": True,
            "advanced_optional_and_separated": True,
            "english_first": True,
            "forced_sanskrit_or_pali": False,
            "preservation": preservation,
            "verified_pyqs_preserved": count_solved_pyqs(assembled),
            "mcq_count": len(keys),
            "mcq_rotation": "A->B->C->D",
            "original_model_answers": ["10 marks", "15 marks", "20 marks"],
        },
        "deliverables": {
            "markdown": relative(markdown),
            "main_pdf": relative(main_pdf),
            "workbook_pdf": relative(workbook_pdf),
            "concept_visual": relative(concept_visual),
            "ascii_spec": relative(ASCII_SPEC),
            "graphical_spec": relative(graphical_spec),
            "flowchart_folder": relative(flow_dir),
            "hashes": deliverable_hashes(output_files),
        },
        "pdf_validation": {
            "main": main_metrics,
            "workbook": workbook_metrics,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
            "internal_indexes": "passed",
            "bookmarks": "passed",
            "empty_clipped_overlapping_replacement_glyph_pages": "none",
        },
        "master_flow_validation": {
            "ascii_panel_count": len(manual.panels),
            "embedded_spec_equality": "passed",
            "standalone_spec_equality": "passed",
            "ascii_graphical_factual_agreement": "passed",
            "graphical_metadata": flow_metadata,
            "graphical_validation_errors": render_result.validation_errors,
        },
        "finalization": finalization_result,
        "guide_refresh": guide_result,
        "philosophy_index_refresh": philosophy_index_result,
        "tests": tests,
        "tracker_and_index_consistency": final_state,
        "changed_files_manifest": relative(changed_files_report),
    }
    write_json(validation_report, report)

    changed: set[str] = {
        relative(Path(__file__)),
        relative(MANIFEST),
        relative(ASCII_SPEC),
        relative(graphical_spec),
        relative(record_file),
        relative(validation_report),
        relative(changed_files_report),
        relative(markdown),
        relative(concept_visual),
        relative(main_pdf),
        relative(workbook_pdf),
        *[
            relative(path)
            for path in flow_dir.rglob("*")
            if path.is_file()
        ],
        *[
            relative(path)
            for path in (NOTES_OUTPUT / "indexes").glob("*.md")
            if path.is_file()
        ],
    }
    after = shared_snapshot(shared_candidates)
    for path, old_hash in before.items():
        if after.get(path) != old_hash:
            changed.add(path)
    changed_files_report.parent.mkdir(parents=True, exist_ok=True)
    changed_files_report.write_text(
        "\n".join(sorted(changed, key=str.casefold)) + "\n",
        encoding="utf-8",
    )
    print(
        f"COMPLETE: {record_id}; changed-file inventory: "
        f"{relative(changed_files_report)}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=ROOT,
        help="Must resolve to this script's repository root.",
    )
    parser.add_argument(
        "--topic",
        type=int,
        choices=range(1, 11),
        default=1,
        help="Official Socio-Political Philosophy topic number.",
    )
    args = parser.parse_args()
    if args.repository_root.resolve() != ROOT.resolve():
        parser.error(f"This generator is bound to {ROOT}.")
    try:
        return run(args.topic)
    except (
        OSError,
        ValueError,
        RuntimeError,
        subprocess.CalledProcessError,
        json.JSONDecodeError,
        carvaka_flowchart.CarvakaError,
    ) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
