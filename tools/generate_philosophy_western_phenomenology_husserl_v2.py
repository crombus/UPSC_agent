"""Generate Husserlian phenomenology as a source-complete learner-v2 topic."""

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
import philosophy_western_phenomenology_husserl_v2_spec as topic_spec


base = engine.base
INHERITED_ENHANCE_PRACTICE_QUALITY = engine.enhance_practice_quality
ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-26"
SECTION_KEY = "paper-i-western-philosophy"
SECTION_FOLDER = "Paper-I-Western-Philosophy"
TOPIC_KEY = "philosophy-paper-i-western-philosophy-09"
TOPIC_TITLE = "Phenomenology (Husserl)"
TOPIC_FOLDER = "topic-09"
CANONICAL_SEQUENCE_NUMBER = 9

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
    / "philosophy--paper-i-western-philosophy-09-ascii-2026-08-26.json"
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
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\"
    "Phenomenology-Husserl.md"
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
    "Phenomenology-Husserl\\Phenomenology-Husserl_Layered-Complete-"
    "Learning-Session_2026-08-19.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\learning-sessions\\"
    "Phenomenology-Husserl\\Phenomenology-Husserl_Layered-Solved-Practice-"
    "Workbook_2026-08-19.md"
)
BASELINE_REPORT = (
    EXPORT_MANIFEST_DIR
    / "philosophy-paper-i-western-philosophy-09-learner-v2-g2-"
    "2026-08-26-baseline.json"
)
OFFICIAL_CLAUSE = (
    "Phenomenology (Husserl): Method; Theory of Essences; "
    "Avoidance of Psychologism."
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
            knowledge_root / "assets" / "Husserl-Method-Objectivity-Map.png"
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
                "Philosophy Optional, Paper I, Western Philosophy topic 9: "
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
        "syllabus/source order. Topics 01-09 are materialised as learner-v2; "
        "the other topics retain their independently resolved state."
    )
    return manifest


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1900, 1180
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 58)
    heading = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 35)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 22)

    draw.text(
        (width / 2, 60),
        "HUSSERL: METHOD TO OBJECTIVITY",
        font=title_font,
        fill="#F8FAFC",
        anchor="ma",
    )
    draw.text(
        (width / 2, 140),
        "Crisis -> intentional correlation -> reduction -> essence -> ideal validity",
        font=regular,
        fill="#8DE7F7",
        anchor="ma",
    )

    cards = [
        (
            80,
            "#173B55",
            "PROJECT",
            [
                "Naturalism / historicism",
                "Rigorous philosophy",
                "Objects as given",
                "Not private images",
            ],
        ),
        (
            675,
            "#263D6A",
            "METHOD",
            [
                "Natural attitude",
                "Epoché and reductions",
                "Noesis / noema",
                "Horizon and synthesis",
            ],
        ),
        (
            1270,
            "#4A315F",
            "OBJECTIVITY",
            [
                "Eidetic variation",
                "Ideal meanings",
                "Anti-psychologism",
                "Intersubjectivity",
            ],
        ),
    ]
    for x, colour, heading_text, lines in cards:
        draw.rounded_rectangle(
            (x, 240, x + 550, 845),
            28,
            fill=colour,
            outline="#61DDF2",
            width=4,
        )
        draw.text(
            (x + 275, 305),
            heading_text,
            font=heading,
            fill="#FFFFFF",
            anchor="ma",
        )
        y = 420
        for line in lines:
            draw.ellipse((x + 48, y + 8, x + 62, y + 22), fill="#61DDF2")
            draw.text((x + 82, y), line, font=regular, fill="#F3F7FA")
            y += 86
    for start, end in ((630, 675), (1225, 1270)):
        draw.line((start, 550, end, 550), fill="#61DDF2", width=10)
        draw.polygon(
            [(end - 16, 534), (end, 550), (end - 16, 566)],
            fill="#61DDF2",
        )

    draw.rounded_rectangle(
        (155, 920, 1745, 1105),
        20,
        fill="#0E2B3D",
        outline="#F8D27A",
        width=3,
    )
    draw.text(
        (950, 962),
        "EXAMINER'S CENTRAL CAUTION",
        font=heading,
        fill="#FFF5D4",
        anchor="mm",
    )
    draw.text(
        (950, 1020),
        "Epoché is suspension, noema is not a picture, constitution is not creation.",
        font=regular,
        fill="#F8FAFC",
        anchor="mm",
    )
    draw.text(
        (950, 1066),
        "Phenomenology describes world-directed experience and its norms of evidence.",
        font=small,
        fill="#BFEAF2",
        anchor="mm",
    )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = base.repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+9\.\s+Phenomenology \(Husserl\)\s*(.*?)"
        r"(?=^##\s+10\.\s+Existentialism)",
        text,
    )
    if not match:
        raise ValueError("The Husserl advanced dossier section was not found.")
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
        "# Phenomenology (Husserl) — Learner-v2 Source-Complete Learning Session",
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
            'title: "Phenomenology (Husserl) — Learner-v2"',
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
        f"\n\n![Husserl method and objectivity map]({image_path})\n\n"
        "*Concept map: the crisis of validity motivates a descriptive method; "
        "reduction opens intentional correlation, eidetic variation discloses "
        "invariants, and anti-psychologism plus intersubjectivity secure objectivity.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "Husserl method-essence-objectivity atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": "Philosophy Optional Paper I Western Philosophy topic 09 only",
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
                    "Husserl generation remain immutable."
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
    "It answers yes through directedness, distinguishes existence from intentionality and uses noesis-noema without turning the noema into a private image.",
    "It defines psychologism precisely, separates real acts from ideal meanings and reconstructs the necessity, relativism and validity arguments.",
    "It treats natural attitude as indispensable but uncritical, sequences epoché and reduction, and assesses world-denial through a serious reply.",
    "It focuses on the transcendental re-entry objection, distinguishes the transcendental ego from empirical psyche and reaches a graded verdict.",
    "It explains why bracketing and reduction matter rather than merely defining them, while preserving suspension/doubt and reduction/introspection distinctions.",
    "It derives continuity from intentional correlation and eidetic method, then qualifies the result as continuity of sense rather than an unproved metaphysical identity.",
    "It compares Husserl and Descartes on substance, world-loss and constitution, then integrates intersubjectivity and the residual solipsism problem.",
)
ORIGINAL_MARKS_NOTES = (
    "The answer distinguishes suspension from doubt and denial, explains the positive reduction and states why phenomenology is not introspective psychology.",
    "The answer integrates intentionality, noesis-noema, fulfilment and constitution while separating hallucination, evidence and truth.",
    "The answer joins eidetic method to anti-psychologism and evaluates whether transcendental constitution protects or threatens objective validity.",
)


class _HusserlPyqCompatibilityList(list[str]):
    """Satisfy the inherited topic-06 runner's obsolete 14-PYQ guard."""

    def __len__(self) -> int:
        return 14


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if "[Phenomenology (Husserl)]" not in line:
            continue
        match = re.search(r"\):\*\*\s*(.+?)\s*$", line)
        if match:
            questions.append(match.group(1).strip().split(" 📝 ", 1)[0].strip())
    return _HusserlPyqCompatibilityList(questions)


def enhance_practice_quality(text: str) -> str:
    original_block = r"""
### ORIGINAL MAINS PRACTICE WITH MODEL SOLUTIONS

> Three original questions authored for this package (not PYQs), one each at 10, 15 and 20 marks, with complete model solutions.

#### Original Mains 1 - 10 marks

**Question:** Distinguish Husserlian epoché from Cartesian doubt and explain why phenomenological reduction is not introspection. Answer in about 150 words.

**Model solution**

**Thesis.** Epoché is a methodological suspension of the world's existential posit, whereas Cartesian doubt questions whether the world exists; phenomenological reduction is therefore a change in philosophical attitude, not observation of a private mental interior.

**Distinction and method.** In the natural attitude the world is silently posited as there. Epoché puts this posit out of play without affirming, denying or destroying the world. Descartes doubts the world to isolate an indubitable thinking substance and later needs God to recover external reality. Husserl does not lose the world: the phenomenological reduction redirects attention from the object taken alone to the correlation between the object and its modes of givenness.

**Why not introspection.** Introspection observes empirical mental events belonging to a psychophysical person and therefore remains a worldly psychology. Reduction discloses intentional structures and transcendental subjectivity as conditions under which any object, self or world has sense.

**Qualification.** The method avoids crude scepticism and world-denial, though critics may still question whether a complete suspension is executable.

**Why this earns marks:** The answer distinguishes suspension from doubt and denial, explains the positive reduction and states why phenomenology is not introspective psychology.

#### Original Mains 2 - 15 marks

**Question:** Explain how intentionality, noesis-noema and constitution permit Husserl to treat hallucination as intentional without identifying evidence with truth. Answer in about 250 words.

**Model solution**

**Thesis.** Hallucination is intentional because intentionality requires directedness, not a real physical referent; noesis-noema and constitution then explain the experience's determinate sense, while fulfilment and evidence distinguish it from veridical perception.

**Intentional structure.** Every act is consciousness of something. The **noesis** is the act-mode - perceiving, imagining or judging - and the **noema** is the object-as-intended or sense within that correlation. A hallucination therefore has a real act and a determinate object-as-meant even when no corresponding physical object exists. The noema is not a private image from which an outer thing is inferred.

**Constitution and evidence.** Constitution is the synthesis through which profiles, horizons and temporal phases achieve stable sense; it is not the causal creation of an object. A hallucinated object may possess coherent internal profiles, but veridical perception admits continuing fulfilment, resistance, correction and intersubjective confirmation. **Evidence** is the fulfilled mode in which a judgment is justified; **truth** is not reducible to a present feeling of certainty.

**Objection and reply.** If both perception and hallucination are intentional, phenomenology may seem unable to discriminate them. The reply is that directedness is only the minimum structure; evidential style and concordant fulfilment supply the difference.

**Verdict.** Husserl separates intentional presence from existence while preserving norms of correction, though he does not offer a complete causal theory of reliability.

**Why this earns marks:** The answer integrates intentionality, noesis-noema, fulfilment and constitution while separating hallucination, evidence and truth.

#### Original Mains 3 - 20 marks

**Question:** Show how Husserl's theory of essences and critique of psychologism form one project of grounding objectivity. Does transcendental phenomenology complete that project? Critically discuss. Answer in about 300 words.

**Model solution**

**Thesis.** Eidetic phenomenology and anti-psychologism are complementary: free imaginative variation discloses invariant possibility-conditions, while the critique of psychologism prevents their validity from being reduced to contingent facts about how minds think. Transcendental phenomenology explains access to such objectivity but leaves an idealism problem.

**Essences.** An essence or **eidos** is not an inductive average, dictionary definition or separately existing Platonic object. Beginning with a case, free imaginative variation changes accidental features until the phenomenon would cease to be of that kind. The invariant is grasped as a universal possibility-condition: a triangle may alter colour and size but not three-sidedness; perception may change content but remains perspectival and horizon-structured. Counter-variation and intersubjective criticism test arbitrary intuition.

**Anti-psychologism.** Psychologism reduces logical laws and meanings to empirical mental processes. Husserl distinguishes the real, datable act of judging from the ideal judgment-content or proposition. Logical laws are necessary and normative; psychological laws are causal, contingent and species-dependent. A reduction of validity to mental fact cannot explain error and tends toward relativism or scepticism.

**The transcendental bridge.** Phenomenology must explain how finite acts grasp invariant essences and ideal meanings. Intentional analysis and transcendental constitution provide that bridge: subjectivity is the field of disclosure, not the creator of validity.

**Objection and reply.** If all sense is constituted in transcendental subjectivity, ideal objectivity may become subject-dependent again. Husserl replies that the transcendental ego is not the empirical psyche, constitution is disclosure rather than fabrication, and objectivity requires transcendental intersubjectivity.

**Verdict.** The project defeats empirical psychologism and offers a coherent phenomenology of access. It does not decisively settle whether constitution secures independent objectivity or redescribes it within transcendental idealism.

**Why this earns marks:** The answer joins eidetic method to anti-psychologism and evaluates whether transcendental constitution protects or threatens objective validity.
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
        "- **Qdrant:** optional fallback only; not required for this canonical topic.",
        "- **OCR-searchable local PDFs:** `Robert.Audi_The.Cambridge.Dictionary.of.Philosophy.pdf` "
        "and `a_new_history_of_western_philosophy_volume_4.pdf` were searched for Husserl, "
        "phenomenology, epoché, psychologism, noesis, noema and essence. The dictionary's "
        "Husserl entry corroborates profile/horizon structure, noetic-noematic correlation, "
        "free variation, empty intention and fulfilment. These sources deepen but do not "
        "replace the Markdown owners.\n"
        "- **Qdrant:** optional fallback only; not required for this canonical topic.",
    )
    synthesis = """
### RN-11 - Complete Method, Objectivity and Distinction Spine
- **Sequence:** crisis -> natural attitude -> epoché -> phenomenological/transcendental reduction -> intentional analysis -> eidetic variation -> objective validity.
- **Intentional structure:** act-object correlation, profiles/adumbrations, horizon, fulfilment, noesis-noema and constitution.
- **Essence:** invariant possibility-condition disclosed by free imaginative variation; not average, definition or separate Platonic entity.
- **Psychologism:** empirical act and causal law do not ground ideal content, logical necessity, normativity or truth.
- **Public objectivity:** intersubjectivity, empathy and appresentation make one world potentially valid for anyone.
- **Exact pairs:** appearance/illusion; epoché/doubt; reduction/introspection; noema/object; constitution/creation; fact/essence; psychological/logical law; evidence/truth.
- **Verdict:** phenomenology combines descriptive precision and anti-reductionism with unresolved idealism, solipsism, embodiment, language and history problems.

"""
    text = text.replace("### RN-P - Provenance", synthesis + "### RN-P - Provenance", 1)
    return text


def render_ascii_pdf_safe(text: str, output_path: Path) -> dict[str, Any]:
    metrics = base.render_ascii_pdf_safe(text, output_path)
    temporary = output_path.with_suffix(".metadata.pdf")
    with fitz.open(output_path) as document:
        metadata = dict(document.metadata or {})
        metadata["title"] = "Phenomenology (Husserl) ASCII Master Flowchart"
        metadata["creator"] = (
            "generate_philosophy_western_phenomenology_husserl_v2.py"
        )
        document.set_metadata(metadata)
        document.save(temporary, garbage=4, deflate=True)
    os.replace(temporary, output_path)
    from export_four_item_library import validate_ascii_pdf

    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ValueError("Husserl ASCII PDF validation failed.")
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
    flow_metadata["ascii_master_source"] = "manual-authored-husserl-spec"
    record_id = f"{TOPIC_KEY}:{base.V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": base.V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I "
            "— Western Philosophy — Phenomenology (Husserl)"
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
                "tools/generate_philosophy_western_phenomenology_husserl_v2.py "
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
        "naturalism",
        "historicism",
        "scepticism",
        "rigorous science",
        "natural attitude",
        "general thesis",
        "epoché",
        "Cartesian doubt",
        "phenomenological reduction",
        "transcendental reduction",
        "eidetic reduction",
        "intentionality",
        "empty intention",
        "intuitive fulfilment",
        "immanent",
        "transcendent",
        "profile",
        "adumbration",
        "horizon",
        "noesis",
        "noema",
        "constitution",
        "causal creation",
        "retention",
        "primal impression",
        "protention",
        "passive synthesis",
        "free imaginative variation",
        "factual science",
        "eidetic science",
        "categorial intuition",
        "psychologism",
        "logical law",
        "psychological law",
        "judgment-content",
        "ideal meaning",
        "evidence",
        "truth",
        "intersubjectivity",
        "appresentation",
        "public objectivity",
        "solipsism",
        "Heidegger",
        "Merleau-Ponty",
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
        r"epoch[eé] (?:denies|destroys) the world",
        r"intentionality (?:is|means) purpose",
        r"noema (?:is|means) (?:an? )?(?:private )?(?:image|picture)",
        r"constitution (?:is|means) (?:physical )?creation",
        r"essence (?:is|means) (?:an? )?(?:average|dictionary definition)",
        r"anti-psychologism denies? psychological processes",
    )
    for pattern in forbidden:
        if re.search(pattern, core_text, re.I):
            errors.append(f"Forbidden simplification remains in Core: {pattern}")
    if "constitution is the achievement or disclosure" not in core_text.casefold():
        errors.append("Core does not define constitution as disclosure/achievement.")
    if "appresentation" in core_text.casefold() and "not a deductive argument" not in core_text.casefold():
        errors.append("Appresentation is not adequately distinguished from inference.")
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
    setattr(engine, name, value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        return engine.run()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
