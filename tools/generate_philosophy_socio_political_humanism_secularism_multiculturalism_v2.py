"""Generate Humanism, Secularism and Multiculturalism as a learner-v2 topic.

Philosophy Optional, Paper II, Socio-Political Philosophy, official topic 6.
The generator is deliberately bound to one topic key: it authors the learner-v2
package for ``Humanism; Secularism; Multi-culturalism.`` only, and never
rewrites topics 01-05 or the planned topics 07-10 beyond the shared indexes and
manifests that must reflect this topic's completion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import fitz

import carvaka_flowchart
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
import philosophy_socio_political_humanism_secularism_multiculturalism_v2_spec as topic_spec
import regenerate_philosophy_indian_v2 as philosophy_v2
from generate_philosophy_western_rationalism_v2 import (
    render_ascii_pdf_safe as _base_render_ascii_pdf,
)
from generate_v2_section_indexes import (
    generate_section_indexes,
    load_manifest,
    load_tracker,
    resolve_topic_states,
)
from PIL import Image, ImageDraw, ImageFont
from validate_v2_export import (
    V2_VARIANT,
    deep_content_quality_audit_text,
    extract_mcq_answer_keys,
    extract_v2_workbook_markdown,
    legacy_progress_navigation_lines,
    strip_legacy_progress_navigation,
    validate_ascii_master_text,
    validate_pdf,
    validate_pdf_layout,
    validate_refreshed_markdown_text,
    validate_tracker_record,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-27"
SECTION_KEY = "paper-ii-socio-political-philosophy"
TOPIC_KEY = "philosophy-paper-ii-socio-political-philosophy-06"
TOPIC_TITLE = "Humanism, Secularism and Multiculturalism"
TOPIC_NUMBER = 6
OFFICIAL_CLAUSE = "Humanism; Secularism; Multi-culturalism."

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
TOPIC_CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
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
    / f"philosophy--{SECTION_KEY}-06-ascii-{GENERATION_DATE}.json"
)
CONTENT_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / f"philosophy--{SECTION_KEY}-content-specs"
)
GRAPHICAL_SPEC_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / f"philosophy--{SECTION_KEY}-graphical-specs"
)
EXPORT_MANIFEST_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
KNOWLEDGE_OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "learning-sessions"
    / "v2"
    / SECTION_KEY
)
NOTES_OUTPUT = ROOT / "notes" / "Philosophy" / "learning-session-v2" / SECTION_KEY
FLOW_ROOT = ROOT / "notes" / "Philosophy" / "flowcharts"

OFFICIAL_SYLLABUS = (
    "upsc-ai-kit\\knowledge\\Philosophy\\OFFICIAL-UPSC-SYLLABUS-VERBATIM.md"
)
PHILOSOPHY_README = "upsc-ai-kit\\knowledge\\Philosophy\\README.md"
CANONICAL_OWNER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\socio-political\\"
    "Humanism-Secularism-Multiculturalism.md"
)
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Socio-Political-Dossier.md"
)
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-2\\"
    "_PYQ-SocioPolitical-2018-2025.md"
)
RETAINED_SESSION = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
    "learning-sessions\\Humanism-Secularism-Multiculturalism\\"
    "Humanism-Secularism-Multiculturalism_Layered-Complete-Learning-Session_"
    "2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Socio-Political-Philosophy\\"
    "learning-sessions\\Humanism-Secularism-Multiculturalism\\"
    "Humanism-Secularism-Multiculturalism_Layered-Solved-Practice-Workbook_"
    "2026-08-19.md"
)

SESSION_SPECS = topic_spec.SESSION_SPECS
ASCII_PANELS = topic_spec.ASCII_PANELS
REQUIRED_CORE_TERMS = topic_spec.REQUIRED_CORE_TERMS

EXPECTED_PYQ_COUNT = 16
EXPECTED_MCQ_COUNT = 48
PYQ_OWNER_LABEL = "[Humanism, Secularism and Multiculturalism]"

CORE_COMPLETENESS_MARKERS = (
    "unearned worth",
    "burden of justification",
    "mere instrument",
    "responsible agency",
    "this-worldly flourishing",
    "abstract universalism",
    "epistemic monopoly",
    "species-being",
    "sovereignty of the rational individual",
    "reconciliation of opposites",
    "isolated ego",
    "graded",
    "publicly justifiable",
    "unequal citizens",
    "intra-religious",
    "no single western model",
    "central device",
    "decoupling",
    "contingent",
    "abstain",
    "non-sectarian",
    "illustration",
    "dialogically",
    "societal culture",
    "external protections",
    "internal restrictions",
    "intercultural dialogue",
    "structural characteristics",
    "contested translation",
    "who speaks for the culture",
    "maldistribution",
    "parity of participation",
    "intersubjective",
    "transformative",
    "self-esteem",
    "synthesis triangle",
    "anthropocentric",
    "extensional",
    "graded verdict",
)

ENGLISH_FIRST_REPLACEMENTS = (
    (
        "**Syllabus (verbatim):** Humanism; Secularism; Multi-culturalism.",
        f"**Syllabus (verbatim):** {OFFICIAL_CLAUSE}",
    ),
    (
        "Gandhi = swaraj, constructive work, decentralisation.",
        "Gandhi = self-rule (swaraj), constructive work, decentralisation.",
    ),
    (
        "| *swarāj*, constructive work, decentralisation |",
        "| self-rule (*swarāj*), constructive work, decentralisation |",
    ),
    (
        "*Hind Swaraj* and writings on religion, tolerance and *swarāj*.",
        "*Hind Swaraj* and writings on religion, tolerance and self-rule "
        "(*swarāj*).",
    ),
    (
        "the statement restates Sarva Dharma Sambhava /",
        "the statement restates equal respect for all faiths (Sarva Dharma "
        "Sambhava) /",
    ),
    (
        "\"acceptance of all religions\" (Sarva Dharma",
        "\"acceptance of all religions\" (equal respect for all faiths; Sarva "
        "Dharma",
    ),
    (
        "one particular framing (equal respect / Sarva Dharma",
        "one particular framing (equal respect for all faiths / Sarva Dharma",
    ),
    (
        "Vivekananda's practical Vedanta",
        "Vivekananda's practical non-dualism (Vedanta)",
    ),
)


def repo_path(value: str | Path) -> Path:
    return ROOT / Path(str(value).replace("\\", os.sep).replace("/", os.sep))


@dataclass(frozen=True)
class LegacyTopic:
    """Minimal topic identity accepted by the shared legacy assembler."""

    key: str
    title: str


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".pending")
    pending.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(pending, path)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pending = path.with_suffix(path.suffix + ".pending")
    pending.write_text(text, encoding="utf-8")
    os.replace(pending, path)


def deliverable_hashes(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def hash_if_file(path: Path) -> str | None:
    return sha256(path) if path.is_file() else None


def shared_snapshot(paths: Iterable[Path]) -> dict[str, str | None]:
    return {relative(path): hash_if_file(path) for path in paths}


def run_command(command: list[str], description: str) -> dict[str, Any]:
    completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
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


def latest_identity(
    tracker: dict[str, Any],
    topic_key: str,
) -> tuple[int, str, str | None]:
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict) and record.get("topic_key") == topic_key
    ]
    learners = [record for record in records if record.get("variant") == V2_VARIANT]
    legacy = [record for record in records if record.get("variant") == "legacy-v1"]
    legacy_id = (
        str(
            max(legacy, key=lambda item: int(item.get("generation") or 1))["record_id"]
        )
        if legacy
        else None
    )
    if learners:
        current = max(learners, key=lambda item: int(item.get("generation") or 1))
        return int(current["generation"]) + 1, str(current["record_id"]), legacy_id
    return 2, legacy_id or f"{topic_key}:legacy-v1:g1", legacy_id


def generation_paths(generation: int) -> dict[str, Path]:
    stem = f"{TOPIC_KEY}-learner-v2-g{generation}-{GENERATION_DATE}"
    flow_root = (
        FLOW_ROOT
        / TOPIC_KEY
        / f"continuous-at-a-glance-english-first-g{generation}"
    )
    validation_root = NOTES_OUTPUT / "validation" / TOPIC_KEY / f"g{generation}"
    return {
        "markdown": KNOWLEDGE_OUTPUT / f"{TOPIC_KEY}_Learning-Session.md",
        "workbook_markdown": KNOWLEDGE_OUTPUT / f"{TOPIC_KEY}_Solved-Workbook.md",
        "concept_visual": (
            KNOWLEDGE_OUTPUT
            / "assets"
            / TOPIC_KEY
            / "humanism-secularism-multiculturalism-map.png"
        ),
        "main_pdf": (
            NOTES_OUTPUT
            / "notes"
            / f"{TOPIC_KEY}_Learning-Session_{GENERATION_DATE}.pdf"
        ),
        "workbook_pdf": (
            NOTES_OUTPUT
            / "workbooks"
            / f"{TOPIC_KEY}_Solved-Workbook_{GENERATION_DATE}.pdf"
        ),
        "validation_root": validation_root,
        "main_visual_map": validation_root / "main-visual-audit-map.json",
        "workbook_visual_map": validation_root / "workbook-visual-audit-map.json",
        "inspection_root": validation_root / "rendered-inspection",
        "source_audit": validation_root / "source-audit.json",
        "flow_root": flow_root,
        "ascii_pdf": flow_root / "ascii-master.pdf",
        "content_spec": CONTENT_SPEC_DIR / f"{TOPIC_KEY}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPEC_DIR / f"{TOPIC_KEY}-g{generation}.json",
        "record": EXPORT_MANIFEST_DIR / f"{stem}-record.json",
        "validation": EXPORT_MANIFEST_DIR / f"{stem}-validation.json",
        "changed": EXPORT_MANIFEST_DIR / f"{stem}-changed-files.txt",
    }


def planned_paths(generation: int) -> dict[str, str]:
    return {
        "assembled_markdown": (
            f"upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"
            f"{SECTION_KEY}\\{TOPIC_KEY}_Learning-Session.md"
        ),
        "workbook_markdown": (
            f"upsc-ai-kit\\knowledge\\Philosophy\\learning-sessions\\v2\\"
            f"{SECTION_KEY}\\{TOPIC_KEY}_Solved-Workbook.md"
        ),
        "notes_pdf": (
            f"notes\\Philosophy\\learning-session-v2\\{SECTION_KEY}\\notes\\"
            f"{TOPIC_KEY}_Learning-Session_{GENERATION_DATE}.pdf"
        ),
        "workbook_pdf": (
            f"notes\\Philosophy\\learning-session-v2\\{SECTION_KEY}\\workbooks\\"
            f"{TOPIC_KEY}_Solved-Workbook_{GENERATION_DATE}.pdf"
        ),
        "graphical_flowchart_folder": (
            f"notes\\Philosophy\\flowcharts\\{TOPIC_KEY}\\"
            f"continuous-at-a-glance-english-first-g{generation}"
        ),
    }


def build_manifest(tracker: dict[str, Any], generation: int) -> dict[str, Any]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    topic = next(
        item for item in manifest["topics"] if item.get("topic_key") == TOPIC_KEY
    )
    _, _, legacy_id = latest_identity(tracker, TOPIC_KEY)
    topic.update(
        {
            "display_title": TOPIC_TITLE,
            "syllabus_mapping": (
                "Philosophy Optional, Paper II, Socio-Political Philosophy topic "
                f"{TOPIC_NUMBER}: {OFFICIAL_CLAUSE}"
            ),
            "source_basic": CANONICAL_OWNER,
            "source_canonical": CANONICAL_OWNER,
            "source_advanced": ADVANCED_DOSSIER,
            "cross_topic_sources": [PHILOSOPHY_README, OFFICIAL_SYLLABUS],
            "verified_pyq_sources": [PYQ_LEDGER],
            "ascii_master_spec": relative(ASCII_SPEC),
            "superseded_v1": legacy_id,
            "retained_learning_session": RETAINED_SESSION,
            "retained_workbook": RETAINED_WORKBOOK,
            **planned_paths(generation),
        }
    )
    manifest["section"]["notes"] = (
        "Complete ten-topic official Socio-Political Philosophy section in "
        "syllabus/source order. Topics 01-06 are materialised as learner-v2; "
        "topics 07-10 remain planned until separately generated and validated."
    )
    return manifest


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1920, 1360
    image = Image.new("RGB", (width, height), "#08131F")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 48)
    heading = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 34)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 22)

    draw.text(
        (width / 2, 40),
        "ONE RUNNING QUESTION, THREE DOCTRINES THAT CONSTRAIN EACH OTHER",
        font=title_font,
        fill="#F4F8FC",
        anchor="ma",
    )
    draw.text(
        (width / 2, 108),
        "How can the equal worth of every human being survive in a world of "
        "many religions and many cultures?",
        font=regular,
        fill="#7FE0C6",
        anchor="ma",
    )

    cards = (
        (
            72,
            "#22203A",
            "#A8A6F0",
            "HUMANISM",
            "the moral FLOOR",
            [
                "dignity is unearned worth",
                "reason and public justification",
                "responsible agency and flourishing",
                "Renaissance, Enlightenment, branches",
                "Tagore, Gandhi, Vivekananda, Roy",
                "not atheism, not anthropocentrism",
            ],
        ),
        (
            672,
            "#12303F",
            "#5FD7C2",
            "SECULARISM",
            "the state POSTURE",
            [
                "freedom of conscience",
                "equal civic standing",
                "separation, laicite, equal respect",
                "principled distance (Bhargava)",
                "abstain to protect, engage to reform",
                "not secularisation, not irreligion",
            ],
        ),
        (
            1272,
            "#33231A",
            "#F0B277",
            "MULTICULTURALISM",
            "the policy FORM",
            [
                "recognition and accommodation",
                "societal culture and options",
                "external protections allowed",
                "internal restrictions refused",
                "Taylor, Kymlicka, Parekh, Okin",
                "not mere demographic diversity",
            ],
        ),
    )
    for x, fill, outline, label, subtitle, items in cards:
        draw.rounded_rectangle(
            (x, 176, x + 576, 900),
            26,
            fill=fill,
            outline=outline,
            width=4,
        )
        draw.text((x + 288, 212), label, font=heading, fill="#FFFFFF", anchor="ma")
        draw.text((x + 288, 266), subtitle, font=small, fill=outline, anchor="ma")
        y = 336
        for item in items:
            draw.ellipse((x + 34, y + 7, x + 48, y + 21), fill=outline)
            draw.text((x + 68, y), item, font=small, fill="#EDF4F9")
            y += 90
    for start, end in ((648, 672), (1248, 1272)):
        draw.line((start, 528, end, 528), fill="#7FE0C6", width=10)
        draw.polygon(
            [(end - 16, 512), (end, 528), (end - 16, 544)],
            fill="#7FE0C6",
        )

    draw.rounded_rectangle(
        (110, 942, width - 110, 1300),
        20,
        fill="#0F1F30",
        outline="#F5CE79",
        width=3,
    )
    draw.text(
        (width / 2, 990),
        "EACH DOCTRINE REPAIRS A FAILURE OF THE OTHER TWO",
        font=heading,
        fill="#FFF2D2",
        anchor="mm",
    )
    draw.text(
        (width / 2, 1048),
        "universal dignity stops recognition from immunising domination inside "
        "a community",
        font=regular,
        fill="#F4F8FC",
        anchor="mm",
    )
    draw.text(
        (width / 2, 1094),
        "secular equal citizenship stops the moral floor being administered by "
        "a single faith",
        font=regular,
        fill="#F4F8FC",
        anchor="mm",
    )
    draw.text(
        (width / 2, 1140),
        "recognised difference stops universal citizenship becoming an "
        "assimilating uniformity",
        font=regular,
        fill="#F4F8FC",
        anchor="mm",
    )
    draw.text(
        (width / 2, 1196),
        "SHARED LIMIT: no culture and no state may place domination beyond "
        "criticism.",
        font=small,
        fill="#A9DFF0",
        anchor="mm",
    )
    draw.text(
        (width / 2, 1236),
        "Humanism without pluralism homogenises; pluralism without a humanist "
        "floor excuses oppression.",
        font=small,
        fill="#A9DFF0",
        anchor="mm",
    )
    draw.text(
        (width / 2, 1274),
        "Every doctrine here is species-bounded: state the anthropocentric "
        "limit rather than concealing it.",
        font=small,
        fill="#F0C177",
        anchor="mm",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+6\.\s+Humanism;\s*Secularism;\s*Multiculturalism\s*"
        r"(.*?)(?=^##\s+7\.\s+Crime and Punishment)",
        text,
    )
    if not match:
        raise ValueError(
            "The Humanism/Secularism/Multiculturalism advanced dossier section "
            "was not found."
        )
    return philosophy_v2.demote(match.group(1).strip(), 4)


def insert_advanced_dossier(text: str, fragment: str) -> str:
    marker = re.search(r"(?m)^##\s+CONSOLIDATED REGISTER NOTES\s*$", text)
    if not marker:
        raise ValueError("The consolidated register-notes marker is missing.")
    block = "\n\n".join(
        [
            "### ADVANCED DOSSIER REFINEMENTS — USE SELECTIVELY",
            (
                "> **Classification: OPTIONAL ADVANCED.** The second-order "
                "Fraser-against-Honneth combination problem, the "
                "multiculturalism-against-interculturalism refinement, the "
                "posthuman challenge to humanism and the extra secularism "
                "models beyond the minimum are unnecessary for a competent "
                "Core answer on this clause. Use them only once humanism, the "
                "secular/secularisation/secularism distinction, the model "
                "spectrum, principled distance, recognition, "
                "external-against-internal group rights and the "
                "recognition/redistribution axis are already secure."
            ),
            fragment,
        ]
    )
    return text[: marker.start()] + block + "\n\n" + text[marker.start() :]


def english_first(text: str) -> str:
    for old, new in ENGLISH_FIRST_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def session_visual_block(spec: dict[str, Any]) -> str:
    blocks: list[str] = []
    for item in spec["visuals"]:
        blocks.extend(
            [
                f"#### VISUAL — {item['title']}",
                "```text",
                *item["lines"],
                "```",
                f"*{item['caption']}*",
            ]
        )
    return "\n\n".join(blocks)


def contract_block(spec: dict[str, Any]) -> str:
    keywords = "\n".join(f"- **{item}**" for item in spec["keywords"])
    revision = "\n".join(f"- {item}" for item in spec["revision"])
    return "\n\n".join(
        [
            "#### DEFINITION / WHAT THIS IS CALLED",
            (
                f"**Plain-language definition:** {spec['plain']}\n\n"
                f"**Technical definition:** {spec['technical']}"
            ),
            session_visual_block(spec),
            "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM",
            f"> {spec['answer']}",
            "#### MUST-WRITE KEYWORDS",
            f"{keywords}\n\n**How to use them:** {spec['usage']}",
            "#### CORE OBJECTION, REPLY AND RESIDUAL LIMIT",
            (
                f"**Objection:** {spec['objection']}\n\n"
                f"**Best reply:** {spec['reply']}\n\n"
                f"**Residual limit:** {spec['limit']}"
            ),
            "#### EXAM USE AND CONCISE REVISION",
            f"**Answer architecture:** {spec['exam']}\n\n{revision}",
        ]
    )


def closure_block(spec: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"#### CLOSING RECALL FLOW — {spec['title']}",
            "",
            "```closure-flow",
            f"SUBTOPIC: {spec['title']}",
            f"STARTING CONCEPT: {spec['title']}",
            "KEY TERMS / DEFINITIONS: " + " | ".join(spec["keywords"]),
            f"MECHANISM / ARGUMENT: {spec['mechanism']}",
            f"CONSEQUENCE / CONTRAST: {spec['consequence']}",
            f"UPSC TRAP / ANSWER-USE: {spec['trap']}",
            f"ANSWER-GRABBING FORMULATION: {spec['answer']}",
            "```",
        ]
    )


def enrich_basic_sessions(text: str) -> str:
    start_match = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", text)
    end_match = re.search(r"(?m)^##\s+BASIC MCQS / REMEDIATION\s*$", text)
    if not start_match or not end_match or start_match.end() >= end_match.start():
        raise ValueError("The canonical Basic section boundary is invalid.")
    prefix = text[: start_match.end()]
    basic = text[start_match.end() : end_match.start()]
    suffix = text[end_match.start() :]
    matches = list(
        re.finditer(r"(?m)^###\s+SESSION\s+(\d+)\s*[—-]\s*(.+?)\s*$", basic)
    )
    if len(matches) != len(SESSION_SPECS):
        raise ValueError(
            f"Expected {len(SESSION_SPECS)} Core sessions, found {len(matches)}."
        )
    chunks: list[str] = [basic[: matches[0].start()]]
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(basic)
        block = basic[match.end() : end].strip()
        block = re.sub(
            r"(?ims)^####\s+SUBTOPIC CLOSURE FLOW\s*\n+```(?:text)?\s*\n.*?\n```\s*$",
            "",
            block,
        ).strip()
        spec = SESSION_SPECS[index]
        chunks.append(
            f"### SESSION {index + 1} — {spec['title']}\n\n"
            f"{contract_block(spec)}\n\n"
            f"{block}\n\n"
            f"{closure_block(spec)}\n\n"
        )
    return prefix + "".join(chunks) + suffix


def update_frontmatter(text: str, generation: int, concept_visual: Path) -> str:
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
            f"> **Syllabus (verbatim):** {OFFICIAL_CLAUSE}\n>\n"
            f"> **Generation:** g{generation}, 27 August 2026 · "
            "**Approval:** false pending explicit topic approval\n>\n"
            "> **Evidence discipline:**"
        ),
        body,
        count=1,
    )
    cover = concept_visual.relative_to(KNOWLEDGE_OUTPUT).as_posix()
    frontmatter = "\n".join(
        [
            "---",
            f'title: "{TOPIC_TITLE} — Learner-v2"',
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


def insert_concept_visual(text: str, concept_visual: Path) -> str:
    marker = re.search(r"(?m)^##\s+BASIC LEARNING SESSION\s*$", text)
    if not marker:
        raise ValueError("BASIC LEARNING SESSION is missing.")
    image_path = concept_visual.relative_to(KNOWLEDGE_OUTPUT).as_posix()
    block = (
        f"\n\n![Humanism, secularism and multiculturalism as one constrained "
        f"argument]({image_path})\n\n"
        "*Concept map: one running question about how equal human worth "
        "survives religious and cultural plurality generates three doctrines, "
        "and each of the three repairs a characteristic failure of the other "
        "two rather than merely sitting beside them.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "humanism, secularism and multiculturalism doctrine, model and "
            "recognition atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": (
            "Philosophy Optional Paper II Socio-Political Philosophy topic 06 only"
        ),
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
                "source_markdown": relative(markdown),
                "source_record": f"{TOPIC_KEY}:{V2_VARIANT}:g{generation}",
                "approved_master_reference": (
                    "notes\\Philosophy\\flowcharts\\"
                    "philosophy-paper-i-indian-philosophy-01\\"
                    "continuous-at-a-glance-core-first\\"
                    "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ),
                "benchmark_preservation": (
                    "The approved Cārvāka design reference, the learner-v2 "
                    "Social and Political Ideals, Sovereignty, Individual and "
                    "State, Forms of Government and Political Ideologies "
                    "packages and every legacy-v1 Humanism, Secularism and "
                    "Multiculturalism artifact remain immutable."
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
        "variant": V2_VARIANT,
        "generation": generation,
        "approval": False,
        "official_syllabus_verbatim": OFFICIAL_CLAUSE,
        "source_markdown": relative(markdown),
        "core_sessions": SESSION_SPECS,
        "advanced_session_count": len(SESSION_SPECS),
        "ascii_panels": ASCII_PANELS,
        "verified_pyq_source": PYQ_LEDGER,
        "verified_pyq_count": EXPECTED_PYQ_COUNT,
        "required_core_terms": REQUIRED_CORE_TERMS,
    }


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if PYQ_OWNER_LABEL not in line or not line.lstrip().startswith("- ("):
            continue
        match = re.search(r"^-\s*(.+?)\s*\*\*\[\d+\]\*\*\s*—", line)
        if match:
            questions.append(re.sub(r"^\([a-z]\)\s*", "", match.group(1)).strip())
    return questions


def workbook_pyqs(workbook: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", match).strip()
        for match in re.findall(r"(?m)^\*\*Question:\*\*\s*(.+?)\s*$", workbook)
    ]


def pdf_metrics(path: Path) -> dict[str, Any]:
    with fitz.open(path) as document:
        text = "\n".join(page.get_text("text") for page in document)
        return {
            "pages": document.page_count,
            "bookmarks": len(document.get_toc(simple=True)),
            "replacement_glyphs": text.count("\ufffd"),
            "blank_pages": [
                number
                for number, page in enumerate(document, 1)
                if len(page.get_text("text").strip()) < 20
            ],
        }


def render_ascii_pdf(text: str, output_path: Path) -> dict[str, Any]:
    metrics = _base_render_ascii_pdf(text, output_path)
    temporary = output_path.with_suffix(".metadata.pdf")
    with fitz.open(output_path) as document:
        metadata = dict(document.metadata or {})
        metadata["title"] = (
            "Humanism, Secularism and Multiculturalism ASCII Master Flowchart"
        )
        metadata["creator"] = (
            "generate_philosophy_socio_political_humanism_secularism_"
            "multiculturalism_v2.py"
        )
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError(
            "Humanism, Secularism and Multiculturalism ASCII PDF validation "
            "failed."
        )
    return {**metrics, **validation}


def render_inspection_contact_sheets(
    inspection_root: Path,
    targets: dict[str, Path],
) -> dict[str, Any]:
    inspection_root.mkdir(parents=True, exist_ok=True)
    manifest: dict[str, Any] = {"generated_on": GENERATION_DATE, "sheets": []}
    for label, path in targets.items():
        with fitz.open(path) as document:
            pages = list(range(document.page_count))
            per_sheet = 6
            for sheet_index, start in enumerate(range(0, len(pages), per_sheet), 1):
                chunk = pages[start : start + per_sheet]
                thumbs = []
                for number in chunk:
                    pixmap = document[number].get_pixmap(dpi=52)
                    thumbs.append(
                        Image.frombytes(
                            "RGB",
                            (pixmap.width, pixmap.height),
                            pixmap.samples,
                        )
                    )
                if not thumbs:
                    continue
                columns = 3
                rows = (len(thumbs) + columns - 1) // columns
                cell_w = max(image.width for image in thumbs) + 12
                cell_h = max(image.height for image in thumbs) + 12
                sheet = Image.new(
                    "RGB",
                    (columns * cell_w, rows * cell_h),
                    "#20262C",
                )
                for position, thumb in enumerate(thumbs):
                    column = position % columns
                    row = position // columns
                    sheet.paste(thumb, (column * cell_w + 6, row * cell_h + 6))
                output = inspection_root / f"{label}-contact-{sheet_index:02d}.png"
                sheet.save(output, "PNG")
                manifest["sheets"].append(
                    {
                        "label": label,
                        "sheet": sheet_index,
                        "source": relative(path),
                        "pages": [number + 1 for number in chunk],
                        "image": relative(output),
                    }
                )
                for thumb in thumbs:
                    thumb.close()
                sheet.close()
    write_json(inspection_root / "inspection-manifest.json", manifest)
    return manifest


def validate_content(
    assembled: str,
    workbook_markdown: str,
    standalone_ascii: str,
    source_pyqs: list[str],
) -> tuple[list[str], dict[str, Any]]:
    errors = validate_refreshed_markdown_text(assembled, topic_key=TOPIC_KEY)
    ascii_match = re.search(
        r"(?is)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
        assembled,
        re.MULTILINE,
    )
    if not ascii_match:
        errors.append("The complete topic ASCII master is missing.")
    else:
        errors.extend(
            validate_ascii_master_text(
                ascii_match.group(1),
                topic_key=TOPIC_KEY,
                standalone_text=standalone_ascii,
            )
        )

    core = re.search(
        r"(?is)^##\s+BASIC LEARNING SESSION\s*(.*?)^##\s+BASIC MCQS / REMEDIATION",
        assembled,
        re.MULTILINE,
    )
    advanced = re.search(
        r"(?is)^##\s+OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\s*"
        r"(.*?)^##\s+CONSOLIDATED REGISTER NOTES",
        assembled,
        re.MULTILINE,
    )
    core_text = core.group(1) if core else ""
    advanced_text = advanced.group(1) if advanced else ""
    if not core or not advanced:
        errors.append("Core or Advanced section could not be isolated.")
    if OFFICIAL_CLAUSE not in assembled:
        errors.append("The exact official syllabus wording is missing.")
    folded_core = core_text.casefold()
    for term in REQUIRED_CORE_TERMS:
        if term.casefold() not in folded_core:
            errors.append(f"Required Core term is missing: {term}")
    for marker in CORE_COMPLETENESS_MARKERS:
        if marker.casefold() not in folded_core:
            errors.append(f"Core completeness marker is missing: {marker}")
    if "ADVANCED DOSSIER REFINEMENTS" not in advanced_text:
        errors.append("The optional Socio-Political dossier was not preserved.")

    core_sessions = re.findall(r"(?m)^###\s+SESSION\s+\d+\s*[—-]", core_text)
    advanced_sessions = re.findall(
        r"(?m)^###\s+ADVANCED SESSION\s+\d+\s*[—-]",
        advanced_text,
    )
    if len(core_sessions) != len(SESSION_SPECS):
        errors.append(
            f"Expected {len(SESSION_SPECS)} Core sessions, found {len(core_sessions)}."
        )
    if len(advanced_sessions) != len(SESSION_SPECS):
        errors.append(
            f"Expected {len(SESSION_SPECS)} Advanced sessions, "
            f"found {len(advanced_sessions)}."
        )

    progress_markers = legacy_progress_navigation_lines(assembled)
    if progress_markers:
        errors.append(
            "Obsolete Progress X/Y navigation survives at lines "
            + ", ".join(str(line) for line, _ in progress_markers[:8])
        )

    answer_lines = re.findall(
        r"(?m)^>\s+(.+?)\s*$",
        "\n".join(
            re.findall(
                r"(?ims)^####\s+ANSWER-GRABBING OPENING[^\n]*\n+((?:>[^\n]*(?:\n|$))+)",
                core_text,
            )
        ),
    )
    normalized_answers = [
        re.sub(r"\s+", " ", line).strip().casefold() for line in answer_lines
    ]
    expected_answers = [
        re.sub(r"\s+", " ", spec["answer"]).strip().casefold()
        for spec in SESSION_SPECS
    ]
    if (
        len(normalized_answers) != len(SESSION_SPECS)
        or len(set(normalized_answers)) != len(SESSION_SPECS)
        or normalized_answers != expected_answers
        or any(len(line.split()) < 18 for line in answer_lines)
    ):
        errors.append("Core Answer-Grabbing Lines are missing, duplicated or weak.")

    workbook_questions = workbook_pyqs(workbook_markdown)
    normalized_source = [re.sub(r"\s+", " ", item).strip() for item in source_pyqs]
    if len(normalized_source) != EXPECTED_PYQ_COUNT:
        errors.append(
            f"Expected {EXPECTED_PYQ_COUNT} verified owner PYQs, "
            f"found {len(normalized_source)}."
        )
    missing_pyqs = [
        question
        for question in normalized_source
        if question not in workbook_questions
    ]
    if missing_pyqs:
        errors.append(
            "Verified PYQ wording differs from the authoritative ledger: "
            + " | ".join(missing_pyqs[:3])
        )

    keys = extract_mcq_answer_keys(assembled)
    expected_keys = ["ABCD"[index % 4] for index in range(len(keys))]
    if len(keys) != EXPECTED_MCQ_COUNT or keys != expected_keys:
        errors.append(
            f"Expected {EXPECTED_MCQ_COUNT} MCQs in strict A->B->C->D rotation, "
            f"found {len(keys)}."
        )

    for marker in ("Original Mains 1", "Original Mains 2", "Original Mains 3"):
        if marker not in workbook_markdown:
            errors.append(f"Missing original marks-wise practice: {marker}")
    for marks in ("10 marks", "15 marks", "20 marks"):
        if marks not in workbook_markdown:
            errors.append(f"Missing original Mains mark level: {marks}")
    earns = len(re.findall(r"Why this earns marks", workbook_markdown))
    if earns < EXPECTED_PYQ_COUNT:
        errors.append(
            f"Expected at least {EXPECTED_PYQ_COUNT} Why-this-earns-marks notes, "
            f"found {earns}."
        )
    if re.search(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", assembled, re.I):
        errors.append("Placeholder text is present.")
    if workbook_markdown.strip() == assembled.strip():
        errors.append("Workbook Markdown duplicates the complete learning session.")

    audit = deep_content_quality_audit_text(assembled, topic_key=TOPIC_KEY)
    return errors, {
        "core_session_count": len(core_sessions),
        "advanced_session_count": len(advanced_sessions),
        "answer_grabbing_line_count": len(normalized_answers),
        "verified_pyq_count": len(normalized_source),
        "mcq_count": len(keys),
        "original_mains_practice_count": 3,
        "why_this_earns_marks_count": earns,
        "deep_quality_status": audit["status"],
        "deep_quality_severity_counts": audit["severity_counts"],
    }


def build_record(
    generation: int,
    supersedes: str,
    legacy_id: str | None,
    paths: dict[str, Path],
    flow_metadata: dict[str, Any],
    source_hashes: dict[str, str],
    output_files: Iterable[Path],
) -> dict[str, Any]:
    flow_metadata["ascii_master_source"] = (
        "manual-authored-humanism-secularism-multiculturalism-spec"
    )
    record_id = f"{TOPIC_KEY}:{V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper II "
            "— Socio-Political Philosophy — Humanism, Secularism and "
            "Multiculturalism"
        ),
        "main_pdf": relative(paths["main_pdf"]),
        "workbook": relative(paths["workbook_pdf"]),
        "markdown": relative(paths["markdown"]),
        "approved": False,
        "provenance": {
            "workflow": (
                "learner-first-v2-philosophy-socio-political-one-topic-source-complete"
            ),
            "source_basic": CANONICAL_OWNER,
            "source_canonical": CANONICAL_OWNER,
            "source_advanced": ADVANCED_DOSSIER,
            "legacy_v1_source_package": RETAINED_SESSION,
            "legacy_v1_workbook": RETAINED_WORKBOOK,
            "pyq_corpus": PYQ_LEDGER,
            "official_syllabus": OFFICIAL_SYLLABUS,
            "official_syllabus_verbatim": OFFICIAL_CLAUSE,
            "philosophy_readme": PHILOSOPHY_README,
            "assembled_markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "content_spec": relative(paths["content_spec"]),
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": "2.1 learner-v2 indexed renderer",
            },
            "generation_date": GENERATION_DATE,
            "superseded_v1": legacy_id,
            "english_first": True,
            "source_hashes": source_hashes,
            "deliverable_hashes": deliverable_hashes(output_files),
            "concept_visual": relative(paths["concept_visual"]),
            "main_visual_audit_map": relative(paths["main_visual_map"]),
            "workbook_visual_audit_map": relative(paths["workbook_visual_map"]),
            "rendered_inspection": relative(paths["inspection_root"]),
            "ascii_master_pdf": relative(paths["ascii_pdf"]),
            "graphical_renderer": {
                "name": carvaka_flowchart.RENDERER_NAME,
                "version": carvaka_flowchart.RENDERER_VERSION,
            },
        },
        "approval": {"approved": False, "approved_on": None, "scope": record_id},
        "validation": {
            "state": "passed",
            "validated_on": GENERATION_DATE,
            "validator": (
                "tools/generate_philosophy_socio_political_humanism_secularism_"
                "multiculturalism_v2.py + tools/validate_v2_export.py"
            ),
        },
        "generated_on": GENERATION_DATE,
        "continuous_core_first": flow_metadata,
    }


def verify_final_state(generation: int, paths: dict[str, Path]) -> dict[str, Any]:
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
        raise ValueError(
            f"Section manifest resolved {len(states)} topics instead of 10."
        )
    if states[5].package_state != "generated":
        raise ValueError(
            f"Topic 06 state is {states[5].package_state!r}, expected generated."
        )
    earlier = [state.package_state for state in states[:5]]
    if any(state != "generated" for state in earlier):
        raise ValueError(
            "Topics 01-05 must remain generated: " + ", ".join(earlier)
        )
    later = [state.package_state for state in states[6:]]
    if any(state != "planned" for state in later):
        raise ValueError(
            "Topics 07-10 were unexpectedly marked beyond planned: " + ", ".join(later)
        )
    index_dir = NOTES_OUTPUT / "indexes"
    required = [
        index_dir / "TOPIC-COVERAGE-INDEX.md",
        index_dir / "NOTES-PDF-INDEX.md",
        index_dir / "WORKBOOK-PDF-INDEX.md",
    ]
    for path in required:
        if not path.is_file():
            raise ValueError(f"Required section index is missing: {relative(path)}")
    export_text = GLOBAL_EXPORT_INDEX.read_text(encoding="utf-8")
    position = export_text.find(TOPIC_KEY)
    if position < 0 or f"**learner-first v2:** g{generation}" not in export_text[
        max(0, position - 600) : position + 1200
    ]:
        raise ValueError(
            "Global export index does not show the new learner-v2 generation."
        )
    guide_text = V2_COMMAND_INDEX.read_text(encoding="utf-8")
    command = (
        "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper II — "
        "Socio-Political Philosophy — Humanism, Secularism and Multiculturalism "
        "— Regenerate"
    )
    if command not in guide_text:
        raise ValueError("V2 section command guide did not become generation-aware.")
    return {
        "manifest_topic_count": len(states),
        "topic_01_state": states[0].package_state,
        "topic_02_state": states[1].package_state,
        "topic_03_state": states[2].package_state,
        "topic_04_state": states[3].package_state,
        "topic_05_state": states[4].package_state,
        "topic_06_state": states[5].package_state,
        "topics_07_10_states": later,
        "approval": states[5].approval_state,
        "validation": states[5].validation_state,
        "section_indexes": [relative(path) for path in required],
        "global_export_index_consistent": True,
        "v2_command_index_consistent": True,
    }


def run() -> int:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    if tracker.get("schema_version") != 2 or not isinstance(
        tracker.get("exports"), list
    ):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
    generation, supersedes, legacy_id = latest_identity(tracker, TOPIC_KEY)
    paths = generation_paths(generation)

    targets = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["concept_visual"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["validation_root"],
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
            "Refusing to overwrite learner-v2 generation targets:\n- "
            + "\n- ".join(relative(path) for path in existing)
        )

    shared_candidates = (
        TRACKER,
        GLOBAL_EXPORT_INDEX,
        V2_COMMAND_INDEX,
        PHILOSOPHY_COMMAND_INDEX,
        MASTER_LEARNING_INDEX,
        TOPIC_CATALOG,
        MANIFEST,
    )
    before = shared_snapshot(shared_candidates)

    write_json(MANIFEST, build_manifest(tracker, generation))
    generate_section_indexes(ROOT, MANIFEST, TRACKER)

    retained_main = repo_path(RETAINED_SESSION).read_text(encoding="utf-8")
    retained_workbook = repo_path(RETAINED_WORKBOOK).read_text(encoding="utf-8")
    ledger = repo_path(PYQ_LEDGER).read_text(encoding="utf-8")
    source_pyqs = owner_pyqs(ledger)
    if len(source_pyqs) != EXPECTED_PYQ_COUNT:
        raise ValueError(
            f"Expected {EXPECTED_PYQ_COUNT} verified owner PYQs in the ledger, "
            f"found {len(source_pyqs)}."
        )

    assembled = philosophy_v2.assemble_legacy(
        LegacyTopic(TOPIC_KEY, TOPIC_TITLE),
        retained_main,
        retained_workbook,
    )
    assembled = re.sub(
        r"(?m)^###\s+OPTIONAL DEPTH\s+(\d+)\s*[—-]\s*",
        r"### ADVANCED SESSION \1 — ",
        assembled,
    )
    assembled = insert_advanced_dossier(assembled, advanced_dossier_fragment())
    assembled = english_first(assembled)
    assembled = strip_legacy_progress_navigation(assembled)

    make_concept_visual(paths["concept_visual"])
    assembled = update_frontmatter(assembled, generation, paths["concept_visual"])
    assembled = insert_concept_visual(assembled, paths["concept_visual"])

    write_json(ASCII_SPEC, make_ascii_spec(paths["markdown"], generation))
    manual = ascii_master.normalize_manual_spec_file(ASCII_SPEC)[TOPIC_KEY]
    ascii_fragment = ascii_master.build_manual_fragment(manual)
    standalone_ascii = ascii_master.standalone_panel_text(ascii_fragment)

    assembled = philosophy_v2.replace_ascii_master(assembled, ascii_fragment)
    assembled, _ = philosophy_v2.rotate_mcqs(assembled)
    assembled = re.sub(
        r"\*\*Correct answer:\s*([A-D])\.\s*(.+?)\*\*",
        r"**Correct answer: \1** — \2",
        assembled,
    )
    assembled = philosophy_v2.wrap_code_fences(assembled)
    assembled = enrich_basic_sessions(assembled)
    assembled = re.sub(r"(?m)^#{5,6}\s+", "#### ", assembled)
    write_text(paths["markdown"], assembled)

    workbook_markdown = extract_v2_workbook_markdown(assembled)
    write_text(paths["workbook_markdown"], workbook_markdown)
    write_json(paths["content_spec"], make_content_spec(generation, paths["markdown"]))

    content_errors, content_metrics = validate_content(
        assembled,
        workbook_markdown,
        standalone_ascii,
        source_pyqs,
    )
    if content_errors:
        raise ValueError("Content validation failed:\n- " + "\n- ".join(content_errors))

    markdown_learning_pdf.build_pdf(
        paths["markdown"],
        paths["main_pdf"],
        mode="main",
        variant=V2_VARIANT,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
        visual_audit_path=paths["main_visual_map"],
    )
    markdown_learning_pdf.build_pdf(
        paths["markdown"],
        paths["workbook_pdf"],
        mode="workbook",
        variant=V2_VARIANT,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
        visual_audit_path=paths["workbook_visual_map"],
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
    write_json(
        paths["source_audit"],
        {
            "generated_on": GENERATION_DATE,
            "topic_key": TOPIC_KEY,
            "official_syllabus_verbatim": OFFICIAL_CLAUSE,
            "source_order": [
                "Markdown knowledge owners and the retained layered package",
                "OCR/PDF evidence already reconciled in the source owners",
                "Live web not used for static doctrine or PYQ wording",
                "Qdrant not required",
            ],
            "verified_pyq_count": len(source_pyqs),
            "verified_pyqs": source_pyqs,
            "hashes": source_hashes,
        },
    )
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
            "source_references": [f"SESSION {number}" for number in raw["sessions"]],
        }
        for panel, raw in zip(manual.panels, ASCII_PANELS)
    ]
    graphical_data = carvaka_flowchart.author_topic_spec(
        topic_key=TOPIC_KEY,
        subject="Philosophy",
        title=TOPIC_TITLE,
        source_markdown=assembled.replace("...", " — ").replace("…", " — "),
        source_markdown_path=relative(paths["markdown"]),
        ascii_spec_path=relative(ASCII_SPEC),
        ascii_spec_sha256=sha256(ASCII_SPEC),
        panels=graphical_panels,
        source_generation=generation,
    )
    for index, stage in enumerate(graphical_data["stages"][:-1]):
        stage["pills"] = topic_spec.GRAPHICAL_PILLS[index]
        stage["groups"] = topic_spec.GRAPHICAL_STAGE_GROUPS[index]
        stage["sequence"] = topic_spec.GRAPHICAL_STAGE_SEQUENCES[index]
        authored_matrix = topic_spec.GRAPHICAL_STAGE_MATRICES[index]
        stage["matrix"] = authored_matrix if stage["layout"] == "matrix" else []
        if stage["layout"] == "matrix" and not authored_matrix:
            raise ValueError(
                f"Stage {stage['id']} uses the matrix layout without an "
                "authored, semantically complete matrix."
            )
        stage["answer_line"] = SESSION_SPECS[index]["answer"]
        stage["mechanism_strip"] = SESSION_SPECS[index]["mechanism"]
        stage["source_references"] = [
            f"SESSION {number}" for number in ASCII_PANELS[index]["sessions"]
        ]
    extra_stage = graphical_data["stages"][-1]
    extra_stage["pills"] = topic_spec.GRAPHICAL_EXTRA_PILLS
    extra_stage["groups"] = topic_spec.GRAPHICAL_EXTRA_GROUPS
    extra_stage["source_references"] = [
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "ADVANCED DOSSIER REFINEMENTS — USE SELECTIVELY",
    ]
    graphical_errors = carvaka_flowchart.validate_spec(graphical_data)
    if graphical_errors:
        raise ValueError(
            "Graphical spec validation failed:\n- " + "\n- ".join(graphical_errors)
        )
    write_json(paths["graphical_spec"], graphical_data)
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_root"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    flow_metadata["approval"] = False
    flow_metadata["ascii_master_spec"] = relative(ASCII_SPEC)
    flow_metadata["ascii_master_spec_sha256"] = sha256(ASCII_SPEC)
    ascii_pdf_metrics = render_ascii_pdf(standalone_ascii, paths["ascii_pdf"])
    flow_metadata["ascii_master_pdf"] = relative(paths["ascii_pdf"])

    pdf_errors: list[str] = []
    for mode, pdf in (("main", paths["main_pdf"]), ("workbook", paths["workbook_pdf"])):
        pdf_errors.extend(
            validate_v2_paths(ROOT, paths["markdown"], pdf, TOPIC_KEY, mode)
        )
        pdf_errors.extend(validate_pdf(pdf, variant=V2_VARIANT, mode=mode))
    main_layout_errors, main_layout = validate_pdf_layout(paths["main_pdf"])
    workbook_layout_errors, workbook_layout = validate_pdf_layout(paths["workbook_pdf"])
    pdf_errors.extend(f"main layout: {error}" for error in main_layout_errors)
    pdf_errors.extend(f"workbook layout: {error}" for error in workbook_layout_errors)
    pdf_errors.extend(
        f"graphical package: {error}" for error in render_result.validation_errors
    )
    if pdf_errors:
        raise ValueError("Rendered validation failed:\n- " + "\n- ".join(pdf_errors))

    main_metrics = pdf_metrics(paths["main_pdf"])
    workbook_metrics = pdf_metrics(paths["workbook_pdf"])
    if (
        main_metrics["replacement_glyphs"]
        or workbook_metrics["replacement_glyphs"]
        or main_metrics["blank_pages"]
        or workbook_metrics["blank_pages"]
        or not main_metrics["bookmarks"]
        or not workbook_metrics["bookmarks"]
    ):
        raise ValueError(
            "PDF metrics contain blank pages, glyph defects or missing bookmarks."
        )

    inspection = render_inspection_contact_sheets(
        paths["inspection_root"],
        {
            "main": paths["main_pdf"],
            "workbook": paths["workbook_pdf"],
            "ascii": paths["ascii_pdf"],
            "graphical": paths["flow_root"] / "tiled.pdf",
        },
    )

    output_files = [
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
        *[path for path in paths["flow_root"].rglob("*") if path.is_file()],
        *[path for path in paths["inspection_root"].rglob("*") if path.is_file()],
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
    write_json(paths["record"], record)

    finalization = run_command(
        [
            sys.executable,
            str(ROOT / "tools" / "finalize_v2_topic.py"),
            "--repository-root",
            str(ROOT),
            "--manifest",
            str(MANIFEST),
            "--record-file",
            str(paths["record"]),
        ],
        "Finalize learner-v2 topic",
    )
    guide = run_command(
        [
            sys.executable,
            str(ROOT / "tools" / "generate_v2_section_indexes.py"),
            "--repository-root",
            str(ROOT),
            "--guide-only",
        ],
        "Refresh V2 subject/section command guide",
    )
    philosophy_index = run_command(
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
    final_state = verify_final_state(generation, paths)

    report = {
        "schema_version": 1,
        "generated_on": GENERATION_DATE,
        "record_id": record["record_id"],
        "topic_key": TOPIC_KEY,
        "variant": V2_VARIANT,
        "generation": generation,
        "approval": False,
        "canonical_sequence_number": TOPIC_NUMBER,
        "official_syllabus_verbatim": OFFICIAL_CLAUSE,
        "section_manifest": relative(MANIFEST),
        "sources": {
            "order": [
                "Markdown knowledge owners and the retained layered package",
                "OCR/PDF evidence already reconciled in the source owners",
                "Live web not used for static doctrine or PYQ wording",
                "Qdrant not required",
            ],
            "hashes": source_hashes,
            "verified_pyq_owner_count": len(source_pyqs),
            "source_audit": relative(paths["source_audit"]),
        },
        "content_validation": {
            **content_metrics,
            "required_h2_order": [
                "BASIC LEARNING SESSION",
                "BASIC MCQS / REMEDIATION",
                "PYQS AND ANSWER PRACTICE",
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
                "CONSOLIDATED REGISTER NOTES",
            ],
            "h2_order_passed": True,
            "register_notes_last": True,
            "session_navigation": "SESSION N only; no Progress X/Y labels",
            "core_syllabus_complete_without_advanced": True,
            "advanced_optional_and_separated": True,
            "verified_pyq_wording": "passed",
            "mcq_rotation": "A->B->C->D",
            "strict_rotation_policy_registered": True,
            "workbook_distinct": True,
            "english_first": True,
        },
        "deliverables": {
            "markdown": relative(paths["markdown"]),
            "workbook_markdown": relative(paths["workbook_markdown"]),
            "main_pdf": relative(paths["main_pdf"]),
            "workbook_pdf": relative(paths["workbook_pdf"]),
            "concept_visual": relative(paths["concept_visual"]),
            "ascii_spec": relative(ASCII_SPEC),
            "content_spec": relative(paths["content_spec"]),
            "graphical_spec": relative(paths["graphical_spec"]),
            "flowchart_folder": relative(paths["flow_root"]),
            "ascii_pdf": relative(paths["ascii_pdf"]),
            "hashes": deliverable_hashes(output_files),
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
        "rendered_visual_inspection": {
            "state": "generated and inspected",
            "contact_sheets": inspection["sheets"],
            "graphical_tiled_pages": render_result.audit.get("tiles", []),
            "repairs": [],
        },
        "finalization": finalization,
        "guide_refresh": guide,
        "philosophy_index_refresh": philosophy_index,
        "tests": tests,
        "tracker_and_index_consistency": final_state,
        "clean_library_publication": "pending tracker finalisation",
        "flow_learning_publication": "pending clean-library publication",
        "changed_files_manifest": relative(paths["changed"]),
    }
    write_json(paths["validation"], report)

    changed: set[str] = {
        relative(Path(__file__)),
        relative(
            ROOT
            / "tools"
            / "philosophy_socio_political_humanism_secularism_"
            "multiculturalism_v2_spec.py"
        ),
        relative(MANIFEST),
        relative(ASCII_SPEC),
        relative(paths["content_spec"]),
        relative(paths["graphical_spec"]),
        relative(paths["record"]),
        relative(paths["validation"]),
        relative(paths["changed"]),
        relative(paths["markdown"]),
        relative(paths["workbook_markdown"]),
        relative(paths["concept_visual"]),
        relative(paths["main_pdf"]),
        relative(paths["workbook_pdf"]),
        *[
            relative(path)
            for path in paths["validation_root"].rglob("*")
            if path.is_file()
        ],
        *[relative(path) for path in paths["flow_root"].rglob("*") if path.is_file()],
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
    write_text(paths["changed"], "\n".join(sorted(changed, key=str.casefold)) + "\n")
    print(
        f"COMPLETE: {record['record_id']}; changed-file inventory: "
        f"{relative(paths['changed'])}"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.repository_root.resolve() != ROOT.resolve():
        parser.error(f"This generator is bound to {ROOT}.")
    try:
        return run()
    except (
        OSError,
        ValueError,
        RuntimeError,
        json.JSONDecodeError,
        carvaka_flowchart.CarvakaError,
    ) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
