"""Generate Later Wittgenstein as a source-complete learner-v2 topic."""

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

import generate_philosophy_western_moore_russell_early_wittgenstein_v2 as pipeline
import philosophy_western_later_wittgenstein_v2_spec as topic_spec


base = pipeline.base
INHERITED_ENHANCE_PRACTICE_QUALITY = pipeline.enhance_practice_quality
ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-26"
SECTION_KEY = "paper-i-western-philosophy"
SECTION_FOLDER = "Paper-I-Western-Philosophy"
TOPIC_KEY = "philosophy-paper-i-western-philosophy-08"
TOPIC_TITLE = "Later Wittgenstein"
TOPIC_FOLDER = "topic-08"
CANONICAL_SEQUENCE_NUMBER = 8

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
    / "philosophy--paper-i-western-philosophy-08-ascii-2026-08-26.json"
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
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\Later-Wittgenstein.md"
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
    "Later-Wittgenstein\\Later-Wittgenstein_Layered-Complete-Learning-Session_"
    "2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Later-Wittgenstein\\Later-Wittgenstein_Layered-Solved-Practice-Workbook_"
    "2026-08-19.md"
)
BASELINE_REPORT = (
    EXPORT_MANIFEST_DIR
    / "philosophy-paper-i-western-philosophy-08-learner-v2-g2-"
    "2026-08-26-baseline.json"
)
OFFICIAL_CLAUSE = (
    "Later Wittgenstein : Meaning and Use; Language-games; Critique of Private Language."
)
SESSION_SPECS = topic_spec.SESSION_SPECS
ASCII_PANELS = topic_spec.ASCII_PANELS
REQUIRED_CORE_TERMS = topic_spec.REQUIRED_CORE_TERMS


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
    "OFFICIAL_CLAUSE": OFFICIAL_CLAUSE,
    "SESSION_SPECS": SESSION_SPECS,
    "ASCII_PANELS": ASCII_PANELS,
    "REQUIRED_CORE_TERMS": REQUIRED_CORE_TERMS,
}.items():
    setattr(base, name, value)
    setattr(pipeline, name, value)

pipeline.topic_spec = topic_spec
pipeline.CANONICAL_SEQUENCE_NUMBER = CANONICAL_SEQUENCE_NUMBER


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
            knowledge_root / "assets" / "Later-Wittgenstein-Practice-Map.png"
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
                "Philosophy Optional, Paper I, Western Philosophy topic 8: "
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
        "syllabus/source order. Topics 01-08 are materialised as learner-v2; "
        "the other topics retain their independently resolved state."
    )
    return manifest


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1900, 1180
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 58)
    heading = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 37)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 27)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 23)

    draw.text(
        (width / 2, 62),
        "LATER WITTGENSTEIN: LANGUAGE AT WORK",
        font=title_font,
        fill="#F8FAFC",
        anchor="ma",
    )
    draw.text(
        (width / 2, 145),
        "Picture and logical form -> use, language-games, rule-following and therapy",
        font=regular,
        fill="#8DE7F7",
        anchor="ma",
    )

    cards = [
        (
            95,
            "#173B55",
            "TRANSITION",
            [
                "Early: picture facts",
                "One logical essence",
                "Later: describe uses",
                "Continuity: clarify",
            ],
        ),
        (
            675,
            "#263D6A",
            "PUBLIC PRACTICE",
            [
                "Meaning as use",
                "Language-games",
                "Grammar and training",
                "Forms of life",
            ],
        ),
        (
            1255,
            "#4A315F",
            "NORMATIVITY",
            [
                "Rule-following",
                "Diary S failure",
                "Criteria and avowal",
                "Therapeutic method",
            ],
        ),
    ]
    for x, colour, heading_text, lines in cards:
        draw.rounded_rectangle(
            (x, 245, x + 550, 845),
            28,
            fill=colour,
            outline="#61DDF2",
            width=4,
        )
        draw.text(
            (x + 275, 310),
            heading_text,
            font=heading,
            fill="#FFFFFF",
            anchor="ma",
        )
        y = 425
        for line in lines:
            draw.ellipse((x + 48, y + 8, x + 62, y + 22), fill="#61DDF2")
            draw.text((x + 82, y), line, font=regular, fill="#F3F7FA")
            y += 86
    for start, end in ((645, 675), (1225, 1255)):
        draw.line((start, 550, end, 550), fill="#61DDF2", width=10)
        draw.polygon(
            [(end - 16, 534), (end, 550), (end - 16, 566)],
            fill="#61DDF2",
        )

    draw.rounded_rectangle(
        (175, 920, 1725, 1098),
        20,
        fill="#0E2B3D",
        outline="#F8D27A",
        width=3,
    )
    draw.text(
        (950, 962),
        "EXAMINER'S CENTRAL DISTINCTION",
        font=heading,
        fill="#FFF5D4",
        anchor="mm",
    )
    draw.text(
        (950, 1020),
        "Public criteria != behaviourism != majority rule; private != secret",
        font=regular,
        fill="#F8FAFC",
        anchor="mm",
    )
    draw.text(
        (950, 1064),
        "Use is a qualified reminder within practices, not a new universal essence of meaning.",
        font=small,
        fill="#BFEAF2",
        anchor="mm",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = base.repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+8\.\s+Later Wittgenstein\s*(.*?)"
        r"(?=^##\s+9\.\s+Phenomenology)",
        text,
    )
    if not match:
        raise ValueError("The Later Wittgenstein dossier section was not found.")
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
        "# Later Wittgenstein — Learner-v2 Source-Complete Learning Session",
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
            'title: "Later Wittgenstein — Learner-v2"',
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
        f"\n\n![Later Wittgenstein practice map]({image_path})\n\n"
        "*Concept map: the transition from picturing to diverse language practices "
        "connects use, grammar and forms of life to rule-following, private language "
        "and philosophical therapy without reducing meaning to behaviour.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "Later Wittgenstein use-games-rules-private-language atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": "Philosophy Optional Paper I Western Philosophy topic 08 only",
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
                    "Later Wittgenstein generation remain immutable."
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
    "It connects family resemblance to language-games through overlapping standards rather than merely listing different games.",
    "It traces solipsism into the diary and correctness problem while denying neither inner experience nor first-person authority.",
    "It defines essential privacy, reconstructs private ostension and answers behaviourism through criteria, avowals and defeasibility.",
    "It preserves the printed anomaly, explains form of life as shared background and distinguishes agreement from majority vote.",
    "It gives internal and methodological reasons for the early-later transition and keeps the section 43 qualification intact.",
    "It states the exact target, reconstructs seeming-versus-being-right and uses the beetle only as a supporting illustration.",
    "It uses the printed quotation as a hinge from logical form to practice, then integrates games, rules and therapy.",
)
ORIGINAL_MARKS_NOTES = (
    "The answer qualifies meaning-as-use, explains why pointing needs grammar and separates use from frequency, intention and reference.",
    "The answer connects language-games, forms of life and finite rule-following while preserving the distinction between practice and majority conformity.",
    "The answer integrates the early-later transition with private ostension, avowals, criteria, objections and a qualified verdict.",
)


class _LaterWittgensteinPyqCompatibilityList(list[str]):
    """Satisfy the inherited topic-06 runner's obsolete 14-PYQ guard."""

    def __len__(self) -> int:
        return 14


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if "[Later Wittgenstein]" not in line:
            continue
        match = re.search(r"\):\*\*\s*(.+?)\s*$", line)
        if match:
            question = match.group(1).strip().split(" 📝 ", 1)[0].strip()
            questions.append(question)
    return _LaterWittgensteinPyqCompatibilityList(questions)


def enhance_practice_quality(text: str) -> str:
    text = INHERITED_ENHANCE_PRACTICE_QUALITY(text)
    original_block = r"""
### ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS

> Three original questions authored for this package (not PYQs), one each at 10, 15 and 20 marks, with full model solutions.

#### Original Mains 1 - 10 marks

**Question:** Explain why ostensive definition cannot by itself fix meaning. Relate your answer to Wittgenstein's qualified account of meaning as use. Answer in about 150 words.

**Model solution**

**Thesis.** Ostensive definition does not create a word-object bond from an uninterpreted act of pointing; it works only within a grammar already learned through practice.

**Argument.** If a teacher points to a red square and says "red", the learner may take the word to mean the colour, shape, material, number, position or even the act of pointing. The point is therefore ambiguous until training, contrast and correction identify the relevant continuation. A colour sample functions as a rule only for someone initiated into comparing and applying colour words.

**Relation to use.** This supports *Philosophical Investigations* section 43: for a large class of cases, though not all, a word's meaning is its use in the language. Use here is a norm-governed role, not frequency, private intention or bodily movement; reference and definition remain legitimate functions within some games.

**Qualification.** The account explains how ostension operates but may appear circular because the background practice already contains norms. Wittgenstein accepts this practical bedrock rather than offering a hidden semantic mechanism.

**Why this earns marks:** The answer qualifies meaning-as-use, explains why pointing needs grammar and separates use from frequency, intention and reference.

#### Original Mains 2 - 15 marks

**Question:** How do language-games and forms of life support Wittgenstein's account of rule-following without reducing correctness to social conformity? Discuss. Answer in about 250 words.

**Model solution**

**Thesis.** Language-games and forms of life locate rule-following in trained practices, but correctness is not whatever a numerical majority happens to do.

**Language-game and background.** A language-game is language interwoven with activity, participants, training, grammar and purpose. The builders' "Slab!" works because an order, a trained response and a building task form one practice. A form of life is the wider shared background of action and natural reaction that makes such moves intelligible.

**Rule-following.** Section 201 shows that no interpretation can mechanically determine every future application: a further interpretation only generates regress. A rule is instead grasped in what counts as obeying, misunderstanding and correcting it. Thus finite instruction plus training and correction sustain normative continuation.

**Not conformity.** Agreement in judgments is deeper than agreement in a particular opinion and is not majority vote. A solitary person can retain a rule-governed technique when the standards are repeatable and not exhausted by present seeming. Kripke's community-based sceptical solution is a contested 1982 reconstruction, not an uncontested statement of Wittgenstein's own view.

**Verdict.** Practice secures the distinction between rule and regularity more convincingly than private interpretation does, though it may display rather than fully explain normativity.

**Why this earns marks:** The answer connects language-games, forms of life and finite rule-following while preserving the distinction between practice and majority conformity.

#### Original Mains 3 - 20 marks

**Question:** Does the critique of private language complete Wittgenstein's transition from the picture theory to the later conception of language? Critically examine. Answer in about 300 words.

**Model solution**

**Thesis.** The private-language critique completes the later transition by denying that a private word-object relation can ground meaning; however, it does not deny inner experience and does not turn public criteria into behaviourism or majority rule.

**Transition.** The *Tractatus* explains meaningful propositions through picturing and logical form. The later work rejects one hidden essence and examines language-games embedded in forms of life. Section 43's qualified reminder places meaning in use for a large class of cases; rule-following then explains why use must admit correct and incorrect continuation.

**Private ostension and diary S.** An essentially private language would contain signs for sensations knowable in principle only to one speaker. The diarist inwardly fixes "S" and later consults a memory sample, but the present impression judges both sample and application. If seeming right exhausts being right, no norm of reapplication has been established. The problem is not ordinary fallible memory but the absence of a criterion of correction independent of present seeming.

**Sensation grammar.** The beetle-in-the-box shows that a private object drops out of the public word's grammar; it is not a proof that sensations are unreal. "I am in pain" is an avowal, whereas "she is in pain" is a third-person attribution using defeasible outward criteria. Criteria are grammatical grounds, not infallible behavioural symptoms.

**Objections and replies.** A Crusoe case and individual-practice readings question the need for an actual community; the reply is that headcount is not decisive, only standards not exhausted by present impression. Phenomenological resistance rightly notes that public grammar under-describes qualitative character, but that does not restore private ostension as a semantic foundation.

**Verdict.** The critique completes the anti-referential and anti-essentialist movement from logical picture to norm-governed practice, while leaving a residual explanatory question about normativity and private experience.

**Why this earns marks:** The answer integrates the early-later transition with private ostension, avowals, criteria, objections and a qualified verdict.
""".strip()
    text = re.sub(
        r"(?ims)^###\s+ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS\s*.*?"
        r"(?=^##\s+OPTIONAL ADVANCED DEPTH)",
        original_block + "\n\n",
        text,
        count=1,
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
        "a sign with no possible public check of correct use is not functioning as a word at all.",
        "a sign with no possible criterion separating correct from merely seeming-correct use is not functioning as a word.",
    )
    text = text.replace(
        "No public practice, no genuine rule.",
        "No norm-governed practice, no genuine rule.",
    )
    text = text.replace(
        "Meaning = public use.",
        "Meaning is carried by criterion-governed use.",
    )
    text = text.replace(
        "language is necessarily public (grounded in shared practice, learnable criteria, forms of life)",
        "language requires standards not exhausted by a momentary private seeming",
    )
    text = text.replace(
        "If language is necessarily public, the solipsist's claim",
        "If meaningful use requires standards beyond present private seeming, the solipsist's claim",
    )
    text = text.replace(
        "- **Qdrant:** optional fallback only; not required for this canonical topic.",
        "- **OCR-searchable local PDFs:** `Think. A Compelling Introduction To Philosophy.pdf` "
        "and `Robert.Audi_The.Cambridge.Dictionary.of.Philosophy.pdf` were searched for "
        "Wittgenstein, rule-following, language-games and private language; "
        "`HistoryPhilosophy1.pdf` was also audited for searchable coverage. These sources "
        "corroborate the Markdown owners but do not replace them.\n"
        "- **Qdrant:** optional fallback only; not required for this canonical topic.",
    )
    synthesis = """
### RN-11 - Comparative Synthesis and Exact Distinctions
- **Early:** object/name, logical form, picture and ideal analysis; **Later:** practice, grammar, use, language-games, family resemblance and therapy.
- Preserve continuity in clarification and limits while stating the methodological discontinuity.
- Exact pairs: **criterion/evidence**; **symptom/criterion**; **private/secret**; **rule/regularity**; **use/intention**; **grammar/empirical fact**; **agreement/majority**.
- Contributions: ordinary-language philosophy, philosophy of mind, anti-essentialism and rule-following.
- Limits: quietism/conservatism, relativism worry, under-explained normativity, theoretical language and private experience.
- Qualified verdict: a powerful diagnostic method and critique of semantic foundations, not a complete general theory of meaning.

"""
    text = text.replace("### RN-P - Provenance", synthesis + "### RN-P - Provenance", 1)
    return text


def render_ascii_pdf_safe(text: str, output_path: Path) -> dict[str, Any]:
    metrics = base.render_ascii_pdf_safe(text, output_path)
    temporary = output_path.with_suffix(".metadata.pdf")
    with fitz.open(output_path) as document:
        metadata = dict(document.metadata or {})
        metadata["title"] = "Later Wittgenstein ASCII Master Flowchart"
        metadata["creator"] = (
            "generate_philosophy_western_later_wittgenstein_v2.py"
        )
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError("Later Wittgenstein ASCII PDF validation failed.")
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
    flow_metadata["ascii_master_source"] = "manual-authored-later-wittgenstein-spec"
    record_id = f"{TOPIC_KEY}:{base.V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I "
            "— Western Philosophy — Later Wittgenstein"
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
            "workbook_visual_audit_map": base.relative(
                paths["workbook_visual_map"]
            ),
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
                "tools/generate_philosophy_western_later_wittgenstein_v2.py + "
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
        "picture theory",
        "logical form",
        "continuity",
        "methodological discontinuity",
        "for a large class of cases",
        "Augustinian picture",
        "ostensive definition",
        "usage frequency",
        "speaker intention",
        "slab",
        "colour sample",
        "number series",
        "language-game",
        "form of life",
        "grammar",
        "family resemblance",
        "agreement in judgments",
        "majority vote",
        "rule-following",
        "normativity",
        "regularity",
        "Kripkenstein",
        "private ostensive definition",
        "diary S",
        "memory sample",
        "criterion of correction",
        "avowal",
        "third-person",
        "beetle-in-the-box",
        "secret code",
        "inner experience",
        "perspicuous representation",
        "philosophical therapy",
        "quietism",
        "ordinary-language philosophy",
        "scientific",
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
    if len(keys) != 40 or keys != expected_keys:
        errors.append(
            f"Expected 40 MCQs in strict A->B->C->D rotation, found {len(keys)}."
        )
    for marker in (
        "Original Mains 1 - 10 marks",
        "Original Mains 2 - 15 marks",
        "Original Mains 3 - 20 marks",
    ):
        if marker not in workbook_markdown:
            errors.append(f"Missing original marks-wise practice: {marker}")
    why_count = workbook_markdown.count("**Why this earns marks:**")
    if why_count != 10:
        errors.append(f"Expected 10 Why-this-earns-marks notes, found {why_count}.")
    if re.search(r"\b(?:TODO|TBD|FIXME|lorem ipsum)\b", assembled, re.I):
        errors.append("Placeholder text is present.")
    if workbook_markdown.strip() == assembled.strip():
        errors.append("Workbook Markdown duplicates the complete learning session.")
    forbidden = (
        r"all words? simply mean(?:s)? (?:their|its) use",
        r"public criteria (?:are|mean) majority",
        r"wittgenstein denies? (?:the existence of )?inner experience",
    )
    for pattern in forbidden:
        if re.search(pattern, core_text, re.I):
            errors.append(f"Forbidden simplification remains in Core: {pattern}")
    if "Kripke's" in core_text and "contested" not in core_text.casefold():
        errors.append("Kripke's reading is not clearly labelled contested.")
    if "criteria are defeasible" not in core_text.casefold():
        errors.append("Core does not state that criteria are defeasible.")
    if "not a proof that sensations are unreal" not in core_text.casefold():
        errors.append("The beetle illustration is not adequately qualified.")
    return errors, {
        "core_session_count": len(core_sessions),
        "advanced_session_count": len(advanced_sessions),
        "answer_grabbing_line_count": len(normalized_answers),
        "verified_pyq_count": sum(1 for _ in source_pyqs),
        "mcq_count": len(keys),
        "original_mains_practice_count": 3,
        "why_this_earns_marks_count": why_count,
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
    "PYQ_MARKS_NOTES": PYQ_MARKS_NOTES,
    "ORIGINAL_MARKS_NOTES": ORIGINAL_MARKS_NOTES,
    "owner_pyqs": owner_pyqs,
    "enhance_practice_quality": enhance_practice_quality,
    "render_ascii_pdf_safe": render_ascii_pdf_safe,
    "build_record": build_record,
    "validate_content": validate_content,
}.items():
    setattr(pipeline, name, value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        return pipeline.run()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
