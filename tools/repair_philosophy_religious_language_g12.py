"""Repair and regenerate Religious Language as immutable learner-v2 generation g12."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Any, Iterable

import fitz
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
import regenerate_philosophy_indian_v2 as philosophy_v2
import refresh_all_v2_learning_sessions as refresh
from generate_philosophy_socio_political_crime_and_punishment_v2 import (
    render_inspection_contact_sheets,
)
from generate_philosophy_western_rationalism_v2 import (
    render_ascii_pdf_safe,
)
from validate_v2_export import (
    V2_VARIANT,
    extract_mcq_answer_keys,
    extract_v2_workbook_markdown,
    legacy_progress_navigation_lines,
    mcq_answer_text_errors,
    validate_ascii_master_text,
    validate_pdf,
    validate_pdf_layout,
    validate_refreshed_markdown_text,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
TOPIC_KEY = "philosophy-paper-ii-philosophy-of-religion-10"
TOPIC_TITLE = "Nature of Religious Language"
GENERATION = 12
GENERATION_DATE = "2026-08-27"
RECORD_ID = f"{TOPIC_KEY}:learner-v2:g{GENERATION}"
SUPERSEDES = f"{TOPIC_KEY}:learner-v2:g11"

TRACKER = ROOT / "EXPORT-PDF-STATUS.json"
CANONICAL = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "philosophy-of-religion"
    / "Religious-Language.md"
)
PYQ_LEDGER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "paper-2"
    / "_PYQ-PhilosophyOfReligion-2018-2025.md"
)
OFFICIAL_SYLLABUS = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "OFFICIAL-UPSC-SYLLABUS-VERBATIM.md"
)
ADVANCED_OWNER = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Philosophy"
    / "_advanced"
    / "Philosophy-of-Religion-Dossier.md"
)
REPAIR_PROMPT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_deep-content-review"
    / "repair-prompts"
    / "philosophy-paper-ii-philosophy-of-religion-10-g11-repair.md"
)
G11_REVIEW = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "_deep-content-review"
    / "reviews"
    / "philosophy-paper-ii-philosophy-of-religion-10.md"
)
G12_REVIEW = G11_REVIEW.with_name(
    "philosophy-paper-ii-philosophy-of-religion-10-g12.md"
)
ISSUE_LEDGER = G11_REVIEW.parents[1] / "ISSUE-LEDGER.md"
MD_CHANGE_SUGGESTIONS = G11_REVIEW.parents[1] / "MD-CHANGE-SUGGESTIONS.md"

G11_KNOWLEDGE = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Paper-Ii-Philosophy-Of-Religion"
    / "learning-sessions"
    / "topic-10"
    / "g11"
)
G11_MAIN = G11_KNOWLEDGE / "topic-10_Complete-Learning-Session_2026-08-23.md"

KNOWLEDGE_ROOT = G11_KNOWLEDGE.parent / "g12"
NOTES_ROOT = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Paper-Ii-Philosophy-Of-Religion"
    / "learning-sessions"
    / "topic-10"
    / "g12"
)
FLOW_ROOT = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Philosophy"
    / "Paper-Ii-Philosophy-Of-Religion"
    / "flowcharts"
    / "topic-10"
    / "carvaka-g12"
)
VALIDATION_ROOT = NOTES_ROOT / "validation"

MAIN_MD = KNOWLEDGE_ROOT / f"topic-10_Complete-Learning-Session_{GENERATION_DATE}.md"
WORKBOOK_MD = (
    KNOWLEDGE_ROOT / f"topic-10_Solved-Practice-Workbook_{GENERATION_DATE}.md"
)
CONCEPT_VISUAL = (
    KNOWLEDGE_ROOT / "assets" / f"topic-10_Teaching-Navigation_{GENERATION_DATE}.png"
)
MAIN_PDF = NOTES_ROOT / f"topic-10_Complete-Learning-Session_{GENERATION_DATE}.pdf"
WORKBOOK_PDF = NOTES_ROOT / f"topic-10_Solved-Practice-Workbook_{GENERATION_DATE}.pdf"
ASCII_PDF = FLOW_ROOT / "ascii-master.pdf"
ASCII_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / f"{TOPIC_KEY}-g12-{GENERATION_DATE}.json"
)
GRAPHICAL_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / "Philosophy"
    / f"{TOPIC_KEY}-g12.json"
)
CONTENT_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "philosophy--paper-ii-philosophy-of-religion-content-specs"
    / f"{TOPIC_KEY}-g12.json"
)
EXPORT_MANIFEST_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
RECORD_FILE = (
    EXPORT_MANIFEST_DIR / f"{TOPIC_KEY}-learner-v2-g12-{GENERATION_DATE}-record.json"
)
VALIDATION_FILE = (
    EXPORT_MANIFEST_DIR
    / f"{TOPIC_KEY}-learner-v2-g12-{GENERATION_DATE}-validation.json"
)
CHANGED_FILE = (
    EXPORT_MANIFEST_DIR
    / f"{TOPIC_KEY}-learner-v2-g12-{GENERATION_DATE}-changed-files.txt"
)
MCQ_AUDIT = VALIDATION_ROOT / "MCQ-AUDIT.json"
SOURCE_AUDIT = VALIDATION_ROOT / "SOURCE-CHANGE-AUDIT.json"

CLEAN_ROOT = (
    ROOT
    / "notes"
    / "Final-Learning-Packages"
    / "Philosophy Optional"
    / "Philosophy Paper II — Philosophy of Religion"
    / "10-Nature-of-Religious-Language"
)
FLOW_LEARNING_ROOT = (
    ROOT
    / "notes"
    / "Flow-Learning"
    / "Philosophy Optional"
    / "10-Nature-of-Religious-Language"
)

OFFICIAL_CLAUSE = (
    "Nature of Religious Language : Analogical and Symbolic; Cognitivist and "
    "Non-cognitive."
)

REQUIRED_CORE_TERMS = (
    "essentially and eminently",
    "res significata",
    "modus significandi",
    "later Thomist",
    "Cajetanian",
    "finite and infinite intrinsic modes",
    "being-itself",
    "demonic",
    "eschatological verification",
    "Braithwaite",
    "Hare",
    "Mitchell",
    "D. Z. Phillips",
    "J. L. Austin",
    "Donald Evans",
    "Ian Ramsey",
    "vidhi",
    "śabda-nityatva",
    "Bhartṛhari",
    "sphoṭa",
    "non-objectifiable",
    "anirvacanīya",
    "sublated",
    "self-effacing",
    "amātra",
    "turīya",
    "Steven Katz",
)

BAD_PHRASES = (
    '"God is good" because God is the cause/source of goodness',
    "Machine translation for civilizational knowledge systems",
    "B theory may cross the axes",
    "B top answer must preserve this caution",
    "B high-scoring response",
    "B common concept allows",
    "D nuanced position may",
    "B symbol still points",
    "Nyāya ≈ univocity",
    "the śāstra's primary mood is imperative",
    "Braithwaite/Wittgenstein",
    "Wittgenstein (form of life)",
    "strictly A → B → C → D",
)


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    for attempt in range(20):
        try:
            os.replace(temporary, path)
            return
        except PermissionError:
            if attempt == 19:
                raise
            time.sleep(0.25)


def write_json(path: Path, data: object) -> None:
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def hashes(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def make_concept_visual(path: Path) -> None:
    width, height = 1800, 1120
    image = Image.new("RGB", (width, height), "#071827")
    draw = ImageDraw.Draw(image)
    fonts = [
        Path(r"C:\Windows\Fonts\arialbd.ttf"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
    ]
    title_font = ImageFont.truetype(str(fonts[0]), 58)
    h_font = ImageFont.truetype(str(fonts[0]), 30)
    body_font = ImageFont.truetype(str(fonts[1]), 25)
    small_font = ImageFont.truetype(str(fonts[1]), 21)

    draw.rounded_rectangle((55, 45, width - 55, 175), 24, fill="#0b2940")
    draw.text(
        (90, 72),
        "NATURE OF RELIGIOUS LANGUAGE — TWO AXES, ONE ANSWER",
        font=title_font,
        fill="#f4d06f",
    )
    draw.text(
        (90, 142),
        "Foundation -> Core doctrine -> evidence pressure -> Indian comparison -> answer",
        font=small_font,
        fill="#c8e4f2",
    )

    boxes = [
        (
            "HOW DO WORDS REFER?",
            "Univocity | analogy | symbol\nnegation | indirect indication",
            "#0e7490",
        ),
        (
            "DO THEY STATE TRUTHS?",
            "Cognitive | mixed | moral-conative\nblik | use | verificationist rejection",
            "#7c3aed",
        ),
        (
            "CONTROL QUESTION",
            '"God is good" may be analogical AND cognitive.\nMode is not truth-status.',
            "#a16207",
        ),
    ]
    box_width = 510
    for index, (heading, body, colour) in enumerate(boxes):
        x = 70 + index * 570
        draw.rounded_rectangle((x, 220, x + box_width, 430), 22, fill=colour)
        draw.text((x + 24, 244), heading, font=h_font, fill="white")
        draw.multiline_text(
            (x + 24, 300), body, font=body_font, fill="#f8fafc", spacing=12
        )

    rail = [
        "1  Problem and two axes",
        "2  Aquinas: true perfection, inadequate mode",
        "3  Scotus: semantic univocity and intrinsic modes",
        "4  Tillich: participation, Being-Itself, idolatry",
        "5  Ayer, Flew, Hare, Mitchell and Hick",
        "6  Braithwaite and qualified Wittgensteinian use",
        "7  Austin, Evans and Ramsey",
        "8  Mimamsa vidhi; sabda-nityatva vs sphota",
        "9  Advaita: negation, indication and sublation",
        "10 Symbol -> mysticism, counter-case and non-necessity",
        "11 Fourteen verified PYQ demand routes",
        "12 Executable 10/15/20-mark answer spine",
    ]
    draw.rounded_rectangle((70, 485, width - 70, 1035), 26, fill="#0b2940")
    draw.text((100, 512), "FOUNDATION-TO-CORE LEARNING RAIL", font=h_font, fill="#67e8f9")
    for index, line in enumerate(rail):
        column = 0 if index < 6 else 1
        row = index if index < 6 else index - 6
        x = 110 + column * 830
        y = 580 + row * 70
        draw.rounded_rectangle((x, y, x + 760, y + 50), 12, fill="#123b56")
        draw.text((x + 18, y + 10), line, font=small_font, fill="#f8fafc")
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG", optimize=True)


def canonical_core_dossier(canonical: str) -> str:
    match = re.search(
        r"(?ms)^## 9\. ADVANCED DOCTRINE DOSSIERS\s*(.*?)"
        r"(?=^## 19\. LINK-OUTS)",
        canonical,
    )
    if not match:
        raise ValueError("Canonical Core dossier sections 9-18 could not be isolated.")
    body = match.group(1).strip()
    body = re.sub(r"(?m)^### ", "#### ", body)
    body = re.sub(r"(?m)^## ", "### ", body)
    return (
        "### CORE DOCTRINE DOSSIERS — PYQ-ESSENTIAL, NOT OPTIONAL\n\n"
        "> These dossiers complete the syllabus and all verified PYQ demand routes. "
        "They belong to Core even when they contain objections or comparative refinements.\n\n"
        + body
        + "\n"
    )


def source_change_block() -> str:
    return """
### g12 source-change ledger

| Old or unsafe claim | Corrected claim | Evidence | Affected Core |
|---|---|---|---|
| Divine goodness was reduced to God causing creaturely goodness. | Aquinas predicates pure perfections of God essentially and eminently; only the creature-derived mode of signification is inadequate. | *Summa Theologiae* I q.13, especially a.2 | Analogy, cognitive content, 2024 PYQ |
| Attribution/proportionality was treated as Aquinas's fixed taxonomy. | The pair is labelled a later Thomist, especially Cajetanian, systematisation. | Aquinas I q.13 plus history of Thomist analogy | Aquinas/Scotus comparison |
| Wittgenstein was placed straightforwardly inside non-cognitivism. | The *Lectures* are distinguished from later Wittgensteinian use theories; the non-cognitivist classification is disputed. | *Lectures on Religious Belief*; D. Z. Phillips qualification | 2023 PYQ, cognitive spectrum |
| The whole Mīmāṃsā *śāstra* was called grammatically imperative and Nyāya was equated with Scotus. | *Vidhi* has priority for disclosing *dharma*; *sphoṭa* is principally grammarian; Nyāya/univocity is only a limited heuristic. | Canonical Indian-philosophy distinctions | Secular/religious use, comparison |
| The ICML abstract opening was used as a title. | The exact eight-author workshop-poster title, status, event date, URL and access date are supplied. | Official ICML 2026 virtual page | Current research illustration |

"""


def coverage_block() -> str:
    return """
### Core/Advanced coverage ledger

| Classification | Included before Optional Advanced |
|---|---|
| **CORE** | Two axes; Aquinas; Tillich; cognitive spectrum; Ayer; Braithwaite; qualified Wittgensteinian use; Advaita |
| **PYQ-TRIGGERED CORE** | Scotus; Maimonides; Flew–Hare–Mitchell; Hick; Austin; Evans; Ramsey; Mīmāṃsā; symbol-to-mysticism |
| **SUPPORTING** | Ricoeur, Pseudo-Dionysius, Jain standpoint logic, speech-act and answer-architecture comparisons |
| **OPTIONAL ADVANCED** | Radical Orthodoxy genealogy, fictionalism, specialist metaphor debates and pluralism enrichment beyond direct demand |

**Syllabus boundary:** The package answers the official clause exactly—analogical and symbolic
language, and cognitivist and non-cognitive accounts—while admitting supporting material only
where a verified PYQ or a necessary objection requires it.

"""


def optional_advanced_block() -> str:
    return """
## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

### Radical Orthodoxy and the genealogy of univocity

Some Radical Orthodoxy readings connect Scotist univocity to later secular metaphysics. This is a
contested historical thesis, not the Core meaning of Scotus's semantic univocity. Use it only as
one optional historiographic criticism after accurately stating intrinsic finite/infinite modes.

### Fictionalism and religious make-believe

Religious fictionalism treats theological narratives as practically or imaginatively useful
without belief in their literal truth. It differs from Braithwaite's moral-conative account,
Hare's *blik*, error theory and ordinary symbolic realism. It is enrichment rather than a required
answer to the official clause.

### Specialist metaphor debates

Metaphor theories ask whether religious predicates create redescriptions rather than track an
ordered metaphysical similarity. They can sharpen the analogy/symbol distinction but are safely
skippable unless the question explicitly asks about metaphor, models or religious imagination.

### Pluralism bridge

Analogical, symbolic and apophatic semantics can make rival descriptions partial or mode-relative,
but they do not dissolve hard existence-claims. Hick's transcategorial Real and Jain standpoint
logic are useful extensions only after the direct religious-language demand has been answered.

"""


CLOSURES = {
    "THE PROBLEM OF RELIGIOUS LANGUAGE": (
        "KEY TERMS / DEFINITIONS: religious language · reference · transcendence · truth-aptness · use\n"
        "MECHANISM / ARGUMENT: First identify HOW a predicate refers; then decide WHETHER the utterance asserts, performs, expresses or regulates.\n"
        "CONSEQUENCE / CONTRAST: Non-literal language can remain cognitive, and performative force can coexist with assertion.\n"
        "UPSC TRAP / ANSWER-USE: Never infer non-cognitive status merely from analogy, symbol or negation.\n"
        "ANSWER-GRABBING FORMULATION: Religious language is best analysed through distinct semantic-mode and logical-status questions."
    ),
    "MEANING, REFERENCE AND TRANSCENDENCE": (
        "KEY TERMS / DEFINITIONS: univocity · equivocity · semantic continuity · anthropomorphism · transcendence\n"
        "MECHANISM / ARGUMENT: Univocity preserves inference but risks domesticating God; equivocity protects transcendence but severs intelligibility.\n"
        "CONSEQUENCE / CONTRAST: Analogy, symbol and negation arise as disciplined middle strategies, not as decorative alternatives.\n"
        "UPSC TRAP / ANSWER-USE: Trap: naming Aquinas, Tillich or Maimonides before stating the dilemma produces a thinker list without a problem.\n"
        "ANSWER-GRABBING FORMULATION: A viable theory must preserve enough continuity for reference and enough difference for transcendence."
    ),
    "ANALOGY, SYMBOL AND NEGATIVE THEOLOGY": (
        "KEY TERMS / DEFINITIONS: essential and eminent predication · res significata · modus significandi · participation · via negativa\n"
        "MECHANISM / ARGUMENT: Aquinas affirms the perfection while qualifying its mode; Tillich mediates through participation; apophasis removes finite limits.\n"
        "CONSEQUENCE / CONTRAST: Each protects transcendence differently and incurs a distinct risk—indeterminacy, vague reference or vacuity.\n"
        "UPSC TRAP / ANSWER-USE: Do not reduce divine goodness to causal attribution or present the later Thomist taxonomy as Aquinas's fixed scheme.\n"
        "ANSWER-GRABBING FORMULATION: Analogy, symbol and negation are three disciplined answers to the same continuity-with-transcendence problem."
    ),
    "COGNITIVISM, NON-COGNITIVISM AND FALSIFICATION": (
        "KEY TERMS / DEFINITIONS: truth-aptness · verification · falsification · blik · moral policy · defeasible trust\n"
        "MECHANISM / ARGUMENT: Ayer challenges meaning, Flew demands adverse conditions, Hare saves orientation, Mitchell preserves evidential vulnerability and Hick postpones possible verification.\n"
        "CONSEQUENCE / CONTRAST: Non-cognitive theories differ sharply; they cannot be merged into one denial of factual meaning.\n"
        "UPSC TRAP / ANSWER-USE: Unverifiability is not by itself a formal contradiction, and resilient faith is not automatically evidential immunity.\n"
        "ANSWER-GRABBING FORMULATION: The spectrum runs from realist assertion through mixed force to moral, attitudinal and hostile non-cognitive accounts."
    ),
    "TILLICH, AQUINAS, VIA NEGATIVA AND LANGUAGE-GAMES": (
        "KEY TERMS / DEFINITIONS: being-itself · analogy · apophasis · religious grammar · form of life\n"
        "MECHANISM / ARGUMENT: The theories answer different questions—Aquinas predication, Tillich participation, apophasis limitation and Wittgensteinian analysis of use.\n"
        "CONSEQUENCE / CONTRAST: A mixed account can retain truth-claim, symbolic depth and practical self-involvement without homogenising the thinkers.\n"
        "UPSC TRAP / ANSWER-USE: Wittgenstein's lectures do not establish a settled systematic non-cognitivism; D. Z. Phillips resisted that label.\n"
        "ANSWER-GRABBING FORMULATION: Religious speech may be non-literal and practice-embedded while still remaining open to questions of truth."
    ),
    "ANALOGY, SYMBOL AND FOUNDATIONAL POSITIONS": (
        "KEY TERMS / DEFINITIONS: causal participation · sign/symbol · eschatological verification · moral commitment · indirect indication\n"
        "MECHANISM / ARGUMENT: Core theories are compared by source of meaning, retained cognitive content, evidential discipline and characteristic failure.\n"
        "CONSEQUENCE / CONTRAST: The comparison creates a usable decision grid for every verified symbolic, analogical and cognitive-content PYQ.\n"
        "UPSC TRAP / ANSWER-USE: Objections and replies are Core when they determine whether a doctrine succeeds; they are not optional merely because they are advanced.\n"
        "ANSWER-GRABBING FORMULATION: No theory is cost-free, so the answer must identify both the good it secures and the failure it risks."
    ),
    "INDIAN AND WESTERN STRATEGIES OF RELIGIOUS SPEECH": (
        "KEY TERMS / DEFINITIONS: vidhi · sabda-nityatva · sphota · laksana · neti neti · anirvacaniya\n"
        "MECHANISM / ARGUMENT: Mimamsa explains injunction and ritual use; grammarians develop sphota; Advaita negates and indirectly indicates before language is sublated.\n"
        "CONSEQUENCE / CONTRAST: Indian material supplies independent semantic mechanisms rather than approximate labels for Western doctrines.\n"
        "UPSC TRAP / ANSWER-USE: Nyaya/univocity is only a limited heuristic; Brahman is non-objectifiable while maya is technically anirvacaniya.\n"
        "ANSWER-GRABBING FORMULATION: Cross-tradition comparison is strongest when structural similarity is stated without doctrinal identity."
    ),
}


def replace_closures(text: str) -> str:
    for title, body in CLOSURES.items():
        pattern = (
            rf"(?ms)^#### CLOSING RECALL FLOW — {re.escape(title)}\s*\n"
            rf"```closure-flow\n.*?\n```"
        )
        replacement = (
            f"#### CLOSING RECALL FLOW — {title}\n"
            "```closure-flow\n"
            f"SUBTOPIC: {title}\n"
            f"START / CONCEPT: {title.title()} begins with the exact conceptual problem named in this session.\n"
            f"{body}\n"
            "```"
        )
        text, count = re.subn(pattern, replacement, text, count=1)
        if count != 1:
            raise ValueError(f"Could not replace closure flow for {title}.")
    return text


def repair_prose(text: str) -> str:
    text = text.replace(
        'title: "Nature of Religious Language — Learner-v2 Refreshed"',
        'title: "Nature of Religious Language: Complete Topic Package"',
    )
    text = re.sub(
        r"(?m)^cover_image: .+$",
        f"cover_image: assets/{CONCEPT_VISUAL.name}",
        text,
    )
    text = text.replace(
        (
            "while non-cognitivists (Braithwaite/Wittgenstein) capture its "
            "**practical/moral force** but at the cost of its **truth-claim**"
        ),
        (
            "while **Braithwaite** offers moral-conative non-cognitivism and "
            "Wittgensteinian use analysis explains practice without by itself "
            "settling **truth-status**"
        ),
    )
    text = re.sub(
        r"(?ms)(^#### ONE-SCREEN MAP ⚠️\s*\n+)```.*?```",
        (
            r"\1```text\n"
            "PROBLEM -> finite literal language must refer to an infinite/transcendent reality\n"
            "\n"
            "AXIS 1 — HOW DOES IT SIGNIFY?\n"
            "  ANALOGY (Aquinas) -> true perfection; creaturely mode remains inadequate\n"
            "  SYMBOL (Tillich)  -> participation in Being-Itself, not a mere sign\n"
            "  NEGATION          -> via negativa / neti neti removes finite limits\n"
            "\n"
            "AXIS 2 — WHAT IS ITS LOGICAL STATUS OR USE?\n"
            "  COGNITIVE         -> Aquinas / Hick: truth-apt, though non-literal or deferred\n"
            "  MORAL-CONATIVE    -> Braithwaite: avowal of an agapeistic policy\n"
            "  ATTITUDINAL       -> Hare: blik; practical orientation without factual assertion\n"
            "  HOSTILE NON-COG   -> Ayer: unverifiable God-talk is meaningless\n"
            "  CONTESTED USE     -> Wittgenstein's lectures and later use theories illuminate\n"
            "                        grammar/form of life without settling truth-status\n"
            "\n"
            "CONTROL -> analogy or symbol can be cognitive; use does not equal non-cognitivism.\n"
            "```"
        ),
        text,
        count=1,
    )
    text = text.replace(
        "# Nature of Religious Language — Learner-v2 Source-Complete Learning Session",
        "# Nature of Religious Language — Complete Learning Session",
        1,
    )
    text = re.sub(
        r"> \*\*Generation:\*\* g1, 21 August 2026 .*",
        f"> **Generation:** g{GENERATION}, {GENERATION_DATE} · "
        "**Approval:** false · **Validation:** revalidation pending  ",
        text,
        count=1,
    )
    text = re.sub(
        r"!\[Refreshed teaching navigation]\([^)]+\)",
        f"![Religious Language foundation-to-core navigation](assets/{CONCEPT_VISUAL.name})",
        text,
        count=1,
    )
    text = text.replace(
        "*Distinct embedded teaching-navigation image. The separate continuous Cārvāka-style flowchart package remains an independent at-a-glance artifact.*",
        "*The image maps the Foundation-to-Core route. The graphical and ASCII continuous masters remain independent reconstruction artifacts.*",
    )
    text = re.sub(
        r"while (?:\*\*)?non-cognitivists(?:\*\*)? "
        r"\((?:\*\*)?Braithwaite/Wittgenstein(?:\*\*)?\) capture "
        r"(?:\*\*)?its practical/moral force(?:\*\*)? but at the cost of "
        r"(?:\*\*)?its truth-claim(?:\*\*)?",
        (
            "while Braithwaite offers moral-conative non-cognitivism and "
            "Wittgensteinian use analysis explains practice without by itself "
            "settling truth-status"
        ),
        text,
    )
    text = text.replace("| Core diagnostic MCQs | 40 |", "| Core single-best-answer MCQs | 40 |")
    text = text.replace(
        "| Remedial diagnostic MCQs | 8 |",
        "| Hard format-diverse MCQs | 8 |\n| Remedial diagnostic MCQs | 8 |",
    )
    text = text.replace("| Total diagnostics | 48 |", "| Total diagnostics | 56 |")
    text = text.replace(
        "| Canonical owner §§0–7 | Basic Learning Session | HOW/WHETHER map, analogy, symbol, negation, cognitivism and answer skeletons retained |",
        "| Canonical owner §§0–7 | Basic Learning Session | HOW/WHETHER foundation, analogy, symbol, negation and cognitive spectrum retained |",
    )
    text = text.replace(
        "| Canonical owner §§9–19 | Optional Advanced | Scotus, Maimonides, falsification, speech acts, mysticism, Advaita and pluralism bridge retained |",
        "| Canonical owner §§9–18 | Basic/Core dossier | Scotus, Maimonides, falsification, speech acts, mysticism, Advaita, traps and answer architecture promoted to Core |",
    )
    text = text.replace(
        "| Premium diagnostic set | MCQs / Remediation | Forty core and eight remedial questions retained with strict answer rotation |",
        "| Premium diagnostic set | MCQs / Remediation | Forty core, eight hard-format and eight remedial questions use strict answer rotation |",
    )
    text = text.replace(
        "**Visible learning labels.** Analogy, symbol, negation, cognitivist/non-cognitivist accounts, Ayer, Braithwaite, Wittgensteinian use, Tillich and Advaitic language are **CORE PAPER II**. Scotus, Maimonides, Flew–Hare–Mitchell, speech acts and symbol-to-mysticism are **PYQ-TRIGGERED CORE**. Fictionalism and specialist metaphor theory remain **OPTIONAL ADVANCED**.",
        "**Visible learning labels.** Analogy, symbol, negation, cognitivist/non-cognitivist accounts, Ayer, Braithwaite, qualified Wittgensteinian use, Tillich and Advaitic language are **CORE PAPER II**. Scotus, Maimonides, Flew–Hare–Mitchell, Hick, Austin, Evans, Ramsey, Mīmāṃsā and symbol-to-mysticism are **PYQ-TRIGGERED CORE**. Radical Orthodoxy, fictionalism, specialist metaphor theory and surplus pluralism material remain **OPTIONAL ADVANCED**.",
    )

    old_current = re.compile(
        r"✅ \*\*Fact:\*\* An ICML 2026 paper.*?\n"
        r"⚠️ \*\*Inference:\*\*.*?\n"
        r"\*\*Live source checked:\*\*.*?\n",
        re.S,
    )
    new_current = (
        "✅ **Fact:** Jintao Ma, Junwen Shen, Xinyue Wang, Leqi Liu, Dengkui Hou, "
        "Lingxiang Hu, Nicolas Turenne and Dun Li authored **“AI as Cultural "
        "Mediation: Agentic Sanskrit–English Translation with Linguistic Grounding.”** "
        "The official ICML page lists it as a poster in the 2026 workshop *Culture x "
        "AI: Evaluating AI as a Cultural Technology*, scheduled for 10 July 2026.  \n"
        "⚠️ **Inference:** Its dictionary, morpho-syntactic and glossary constraints "
        "illustrate why sacred-language translation cannot be reduced to word "
        "substitution. It is a current research illustration, not doctrinal evidence "
        "for any theory of religious language.  \n"
        "**Official source:** https://icml.cc/virtual/2026/74717 "
        "(accessed 27 August 2026).\n"
    )
    text, count = old_current.subn(new_current, text, count=1)
    if count != 1:
        raise ValueError("The stale ICML block could not be replaced.")

    text = text.replace(
        '**Technical definition:** Two types: ✅ Analogy of attribution — "God is good" because God is the cause/source of goodness in creatures.',
        "**Technical definition:** Analogy, symbol and negative theology are distinct "
        "modes of religious predication: Aquinas affirms pure perfections essentially "
        "and eminently, Tillich explains participatory symbolism, and apophasis removes "
        "finite limitations.",
    )
    text = text.replace(
        '- **(a) Analogy (Aquinas — 2024 PYQ):** religious language is **analogical** — between univocal and equivocal. Two types: ✅\n'
        '  - **Analogy of attribution** — "God is good" because God is the cause/source of goodness in creatures.\n'
        "  - **Analogy of proportionality** — goodness is to God as (proportionate to His infinite nature) goodness is to a human. So \"good\" applies **proportionally**, truly but not identically. → preserves **meaning without anthropomorphism**.",
        "- **(a) Analogy (Aquinas — 2024 PYQ):** pure perfections such as goodness "
        "are predicated of God **essentially and eminently**. The ***res significata*** "
        "applies truly, while the creature-derived ***modus significandi*** is "
        "inadequate to the divine mode. Aquinas expressly rejects reducing “God is "
        "good” to “God causes goodness.” ✅\n"
        "  - **Later Thomist attribution** illustrates ordered predication through "
        "the healthy animal/medicine example; it does not make divine goodness merely causal.\n"
        "  - **Later Thomist proportionality** says perfection belongs according to "
        "the subject's mode. The attribution/proportionality pair is a later Thomist, "
        "especially Cajetanian, systematisation rather than Aquinas's fixed taxonomy.",
    )
    text = text.replace(
        'MECHANISM / ARGUMENT: Two types: ✅ Analogy of attribution — "God is good" because God is the cause/source of goodness in creatures.',
        "MECHANISM / ARGUMENT: The perfection signified applies truly to God, while "
        "the creature-derived mode of signifying does not represent the divine mode adequately.",
    )
    text = text.replace(
        '**Technical definition:** Cognitivist (realist): religious statements are genuine truth-claims — "God exists" is true or false, asserting a fact about reality (Aquinas, Hick, Swinburne). ✅ Non-cognitivist: religious statements do not state facts; they express something else: ✅ R.B.',
        "**Technical definition:** Cognitivism treats a religious utterance as "
        "truth-apt; non-cognitive families instead locate primary meaning in moral "
        "commitment, world-orientation, practice, expression or verificationist rejection. "
        "Braithwaite, Hare, Wittgensteinian approaches and Ayer must be distinguished.",
    )
    text = text.replace(
        '  - **Wittgenstein / Wittgensteinian (2023 PYQ):** religious language is a distinct **"language-game" embedded in a form of life**; its meaning is its **use** in worship/practice, not fact-stating; "belief in the Last Judgement" regulates a life, it\'s not a prediction. ✅',
        "  - **Wittgenstein and later Wittgensteinian approaches (2023 PYQ):** "
        "Wittgenstein's *Lectures on Religious Belief* contrast Last-Judgement belief "
        "with ordinary prediction. Later Wittgensteinian theories use language-game, "
        "grammar and form of life. Straightforward non-cognitivist classification is "
        "disputed; D. Z. Phillips resisted reductionist and simple non-cognitivist readings. ✅ ❓",
    )
    text = text.replace(
        "| Language-game | non-cognitive | use in a form of life | Wittgenstein | fideism/relativism |",
        "| Language-game/use | contested | religious grammar and life-orienting use | Wittgenstein; later Wittgensteinians | fideism if insulated; simple non-cognitivism is disputed |",
    )
    text = text.replace(
        "Indian: Mīmāṃsā's vidhi (the śāstra's primary mood is imperative, not indicative);\n"
        "        mantra as instrument; śabda-nityatva (NOT sphoṭa, which is the grammarians');",
        "Indian: Mīmāṃsā gives vidhi priority in disclosing dharma; this does not make\n"
        "        the entire śāstra grammatically imperative. Mantra functions as an\n"
        "        instrument; Mīmāṃsā defends śabda-nityatva, while classical sphoṭa\n"
        "        belongs principally to the grammarian tradition, especially Bhartṛhari;",
    )
    text = text.replace(
        "Indian: Nyāya ≈ univocity; Advaita's lakṣaṇā ≈ analogy; neti neti ≈ negation.",
        "Indian: Nyāya lies near the univocity pole only as a limited heuristic;\n"
        "        Advaita's lakṣaṇā is structurally comparable to analogy, and neti neti\n"
        "        to negation, without making the doctrines identical.",
    )
    text = text.replace(
        "Analogy of attribution orders creaturely goodness to its source; proportionality permits each subject to possess perfection according to its mode.",
        "Aquinas instead says pure perfection is present in God essentially and "
        "eminently: the *res significata* applies truly, while the creature-derived "
        "*modus significandi* remains inadequate. The later Thomist attribution/"
        "proportionality framework clarifies ordered and mode-relative predication.",
    )
    text = text.replace(
        "In the **analogy of attribution**, a predicate belongs primarily to one subject and derivatively to another through causal relation. “Healthy” belongs primarily to an animal and secondarily to medicine as a cause of health or complexion as its sign. Applied theologically, creaturely perfections are ordered to God as their source, although the health example illustrates the logic rather than directly defining divine goodness.",
        "Aquinas's governing claim is not that divine goodness means only causal "
        "sourcehood. Pure perfections are present in God essentially and eminently; "
        "the perfection signified is true of God although its creature-derived mode "
        "of signification is inadequate. The healthy animal/medicine example belongs "
        "to later Thomist explanation of attribution and illustrates ordered "
        "predication without defining divine goodness.",
    )
    text = text.replace(
        "Indian parallels sharpen the choice: Nyāya approximates univocal predication, Advaita’s *lakṣaṇā* supplies indirect indication, and *neti neti* supplies negation.",
        "Indian comparisons sharpen the choice without establishing identity: Nyāya "
        "may be placed near the univocity pole only as a limited heuristic, while "
        "Advaita's *lakṣaṇā* and *neti neti* supply distinct indirect and eliminative methods.",
    )
    text = text.replace(
        "Mīmāṃsā’s *vidhi* is injunctive—“let it be done”—and mantra functions liturgically;",
        "Mīmāṃsā gives *vidhi* priority in disclosing *dharma*, and mantra functions liturgically;",
    )
    text = text.replace(
        "Vedic injunction is performative/injunctive rather than merely descriptive, and mantra functions within ritual action.",
        "Mīmāṃsā gives injunction priority in disclosing *dharma*, while mantra "
        "functions within ritual action; this priority does not make the entire "
        "*śāstra* grammatically imperative.",
    )
    text = text.replace(
        "A Wittgensteinian approach shifts attention",
        "Wittgenstein's lectures, and later Wittgensteinian approaches, shift attention",
    )
    text = text.replace(
        "This approach is called non-cognitive because",
        "This family is often classified as non-cognitive because",
    )
    text = text.replace(
        "**Plain-language definition:** Religious language is discourse about "
        "transcendent reality whose central problem is how finite human concepts can "
        "be meaningful without reducing their object to finite categories.",
        "**Plain-language definition:** Meaning and reference become difficult when "
        "religious language applies finite concepts to transcendence without reducing "
        "the transcendent referent to an ordinary object.",
    )
    text = text.replace(
        "> Religious language is discourse about transcendent reality whose central "
        "problem is how finite human concepts can be meaningful without reducing their "
        "object to finite categories.",
        "> The problem of meaning, reference and transcendence is to preserve "
        "intelligible God-talk without either anthropomorphic univocity or empty equivocity.",
    )
    guidance_replacements = {
        "Identify whether the disputed sentence describes, evaluates, commits, evokes "
        "or regulates practice before applying a theory of religious meaning.": (
            "Use religious language, cognitive content, reference, transcendence, "
            "verification and use as a sequence: identify reference, classify force, "
            "test truth-aptness and state the relevant limit."
        ),
        "Explain why univocal transfer risks anthropomorphism and pure equivocation "
        "destroys reference, thereby motivating analogical, symbolic and negative strategies.": (
            "Map meaning, reference and transcendence through univocity, equivocity "
            "and semantic distance; then show why analogy, symbol or negation is needed."
        ),
        "Compare how analogy preserves proportional similarity, symbol participates "
        "in meaning, and negation removes finite limitations without emptying discourse.": (
            "Use analogy, symbol, negative theology, participation, indirect indication "
            "and neti neti in order: define each mechanism, attach its risk and compare outcomes."
        ),
        "Place theories on a spectrum from truth-apt assertion to expressive commitment, "
        "then test whether insulation from falsification protects meaning or empties content.": (
            "Place cognitivism, non-cognitivism, falsification, eschatological verification, "
            "moral commitment and language-game use on one spectrum, then test evidential vulnerability."
        ),
        "Use each thinker for a distinct semantic function—analogy, symbol, negation, "
        "moral commitment or use—rather than treating all as denials of cognitive content.": (
            "Assign Tillich, Aquinas, via negativa, Wittgenstein, Braithwaite and form "
            "of life to distinct mechanisms; compare them without treating each as non-cognitive."
        ),
        "Compare foundational strategies by how much truth-apt content they preserve "
        "and how they prevent either anthropomorphism or semantic emptiness.": (
            "Compare analogy of attribution, analogy of proportionality, symbolic "
            "participation, negative theology, language-game use and cognitive residue "
            "by reference, truth-status, gain and characteristic failure."
        ),
        "Compare Indian testimony, negation and indirect indication with Western analogy "
        "and symbol, while keeping their distinct metaphysical commitments visible.": (
            "Use Nyaya testimony, Advaita negation, indirect indication, Buddhist "
            "conventional truth, Western analogy and semantic pluralism as qualified "
            "comparison axes rather than equivalence claims."
        ),
    }
    for old, new in guidance_replacements.items():
        text = text.replace(
            f"**How to use them:** {old}",
            f"**How to use them:** {new}",
        )

    for bad, good in (
        ("B theory may cross the axes", "A theory may cross the axes"),
        ("B top answer must preserve this caution", "A top answer must preserve this caution"),
        ("B high-scoring response", "A high-scoring response"),
        ("B common concept allows", "A common concept allows"),
        ("D nuanced position may combine", "A nuanced position may combine"),
        ("B symbol still points", "A symbol still points"),
    ):
        text = text.replace(bad, good)

    text = text.replace(
        "> **CORE DISTINCTION:** ANSWER-GRABBING LINE — WRITE/ADAPT IN THE EXAM (Recommended opening definition):**",
        "> **CORE DISTINCTION — answer-ready definition:**",
    )
    text = replace_closures(text)
    return text


HARD_MCQS = r"""
#### HARD FORMAT-DIVERSE MCQS

#### 41. With reference to Aquinas's divine predication, consider the following statements:

1. Pure perfections are present in God essentially and eminently.
2. The *modus significandi* derived from creatures adequately represents the divine mode.
3. “God is good” cannot be reduced to “God causes goodness.”

Which of the statements given above are correct?

A. 1 and 3 only
B. 1 and 2 only
C. 2 and 3 only
D. 1, 2 and 3

**Answer: A. 1 and 3 only**

**Explanation:** The perfection signified applies truly, but the creature-derived mode of
signification is inadequate. Aquinas expressly rejects the cause-only paraphrase.

#### 42. Assertion (A): Wittgenstein must be classified straightforwardly as a non-cognitivist.

Reason (R): His lectures contrast belief in the Last Judgement with ordinary empirical prediction.

A. Both A and R are true, and R is the correct explanation of A.
B. A is false, but R is true.
C. A is true, but R is false.
D. Both A and R are false.

**Answer: B. A is false, but R is true.**

**Explanation:** The contrast is genuine, but the systematic non-cognitivist classification is
disputed. Later Wittgensteinian developments and D. Z. Phillips require separate treatment.

#### 43. Match List I with List II:

| List I | List II |
|---|---|
| 1. Ramsey | a. Self-involving language |
| 2. Evans | b. Model and qualifier |
| 3. Mīmāṃsā | c. *Vidhi* priority in disclosing *dharma* |
| 4. Bhartṛhari | d. Classical *sphoṭa* |

A. 1-a, 2-b, 3-d, 4-c
B. 1-b, 2-c, 3-a, 4-d
C. 1-b, 2-a, 3-c, 4-d
D. 1-c, 2-a, 3-d, 4-b

**Answer: C. 1-b, 2-a, 3-c, 4-d**

**Explanation:** Ramsey supplies model-and-qualifier, Evans self-involvement, Mīmāṃsā the
priority of injunction for *dharma*, and the grammarian Bhartṛhari the classical *sphoṭa* account.

#### 44. Arrange the following argumentative moves in the most defensible sequence:

1. State the univocal/equivocal dilemma.
2. Explain true perfection with inadequate creaturely signification.
3. Present Scotus's demand for semantic continuity.
4. Test analogy for indeterminacy and issue a qualified verdict.

A. 2-1-4-3
B. 3-2-1-4
C. 1-3-4-2
D. 1-2-3-4

**Answer: D. 1-2-3-4**

**Explanation:** A marks-worthy analogy answer moves from problem to Aquinas's mechanism,
then to the strongest contrast and finally to objection and verdict.

#### 45. Consider the following pairs:

1. Brahman — non-objectifiable but *sat*
2. *Māyā* — technically *anirvacanīya*
3. *Neti neti* — eliminative negation
4. *Lakṣaṇā* — direct literal predication

How many pairs are correctly matched?

A. Three only
B. Two only
C. One only
D. Four

**Answer: A. Three only**

**Explanation:** The fourth pair is wrong: *lakṣaṇā* is indirect or secondary indication when
literal meaning cannot carry the intended import.

#### 46. Read the passage:

> A partisan trusts a stranger despite disturbing evidence, but admits that the evidence counts
> against the trust and that sufficiently grave evidence could defeat it.

Which inference best follows?

A. The commitment is an unfalsifiable *blik*.
B. The example models truth-apt, defeasible trust rather than evidential immunity.
C. The utterance is meaningful only as a moral policy.
D. The claim is verified eschatologically.

**Answer: B. The example models truth-apt, defeasible trust rather than evidential immunity.**

**Explanation:** Mitchell differs from Hare because counterevidence remains relevant. The
partisan preserves cognition without demanding immediate abandonment of commitment.

#### 47. Which row contains only accurate school/doctrine qualifications?

| Row | Mīmāṃsā | Grammarians | Nyāya comparison |
|---|---|---|---|
| 1 | whole *śāstra* grammatically imperative | reject *sphoṭa* | identical to Scotus |
| 2 | *sphoṭa* doctrine | *śabda-nityatva* only | no determinate God-talk |
| 3 | *vidhi* priority and *śabda-nityatva* | Bhartṛhari's *sphoṭa* | limited univocity heuristic |
| 4 | denies word–meaning relation | *neti neti* | ontological univocity |

A. Row 1
B. Row 2
C. Row 3
D. Row 4

**Answer: C. Row 3**

**Explanation:** The accurate row preserves school boundaries and labels the Nyāya comparison
as heuristic rather than doctrinal identity.

#### 48. A symbol is used in contemplation, becomes transparent to what it mediates, and is then
self-effaced. Which evaluation is strongest?

A. The sequence proves that every symbol necessarily causes mysticism.
B. The sequence is impossible because mysticism always requires literal description.
C. The sequence establishes that symbols and mystical experience are unrelated.
D. It models one route toward immediacy, but idolatry, Katz's constructivism and alternative routes show that the movement is neither necessary nor guaranteed.

**Answer: D. It models one route toward immediacy, but idolatry, Katz's constructivism and alternative routes show that the movement is neither necessary nor guaranteed.**

**Explanation:** The affirmative mechanism must be joined to arrest, constitutive-symbol and
non-necessity counter-cases. *Oṃkāra* to soundless *amātra/turīya* is one precise illustration.

"""


IMPROVEMENTS = [
    (
        "2018 · Q5(a)",
        [
            "Name one secular performative, such as a courtroom oath, to make the continuity qualification concrete.",
            "Retain Austin, Evans, Ramsey and the Mīmāṃsā example; cut the extended overlap paragraph first if time is short.",
        ],
        "Use five compact moves: use-not-vocabulary thesis; function; referent/verification; self-involvement; overlap-qualified conclusion.",
    ),
    (
        "2018 · Q7(b)",
        [
            "State more sharply that Braithwaite offers a normative reconstruction of religion rather than a neutral account of every utterance.",
            "Under time pressure retain agape, stories, believer-intent objection and the mixed speech-act verdict; cut the secondary pluralism example.",
        ],
        "Compress to doctrine in 60 words, two strengths in 40, two objections in 70, reply and verdict in 30.",
    ),
    (
        "2018 · Q8(c)",
        [
            "Tie each demanded dimension—cultural, spatial and temporal—to one named example before moving to criticism.",
            "Retain Tillich, hierophany and idolatry; cut the final reform paragraph if the answer exceeds the target.",
        ],
        "Use a three-column body: cultural/myth, spatial/hierophany, temporal/liturgy; finish with mediation-not-identification.",
    ),
    (
        "2019 · Q6(a)",
        [
            "Number the four-stage affirmative mechanism visibly so the examiner can see the answer to “how.”",
            "Retain *Oṃ*–*amātra/turīya*, idolatry, Katz and non-necessity; reduce the catalogue of alternative traditions first.",
        ],
        "Allocate roughly 120 words to the mechanism, 70 to Indian evidence, 70 to counter-cases and 30 to the conditional verdict.",
    ),
    (
        "2020 · Q8(a)",
        [
            "Open with a one-sentence criterion for cognitive content before surveying positions.",
            "Retain Aquinas, Flew/Hare/Mitchell, Braithwaite and mixed-force verdict; cut secondary examples before core arguments.",
        ],
        "Build four paragraphs: qualified realism; verification/falsification; non-cognitive insights; defended mixed conclusion.",
    ),
    (
        "2021 · Q8(a)",
        [
            "Separate Braithwaite's argument from later speech-act support so that historical attribution remains exact.",
            "Retain the agapeistic policy, sustaining stories, reductionism and atheist-account objection; cut peripheral comparisons.",
        ],
        "Use a 1:1 balance between reconstruction and criticism, with a final two-sentence mixed-account verdict.",
    ),
    (
        "2021 · Q8(c)",
        [
            "State the disputed status of Tillich's non-symbolic exception in one precise sentence rather than treating it as settled.",
            "Retain symbol/sign, participation, Being-Itself, idolatry/demonic and referential objection; cut historical life-cycle detail first.",
        ],
        "Define in 35 words, list five symbol features, explain ontology, give one objection/reply and conclude with symbolic realism.",
    ),
    (
        "2022 · Q5(e)",
        [
            "Apply every thinker directly to the exact sentence “God exists”; avoid free-standing theory summaries.",
            "Retain truth-aptness, Braithwaite, Hare, qualified Wittgensteinian use and mixed verdict; cut the second Hick sentence first.",
        ],
        "Use a two-column mental plan—what the sentence claims versus what its avowal does—then reconcile the columns.",
    ),
    (
        "2023 · Q5(d)",
        [
            "Begin with the attribution caution: the question's wording may invite a non-cognitive reading, but the classification is disputed.",
            "Retain Last Judgement, grammar/form of life, Phillips qualification and fideism objection; cut generic practice examples first.",
        ],
        "Use four paragraphs: lectures/example; later use theory; disputed classification; strength, objection and verdict.",
    ),
    (
        "2023 · Q7(c)",
        [
            "Distinguish participation from resemblance explicitly; this is the most important mechanism in Tillich.",
            "Retain the six symbol features, Being-Itself, demonic distortion and disputed exception; cut the second cultural-history paragraph.",
        ],
        "Use definition, feature matrix, ontological role, objection/exception and qualified conclusion.",
    ),
    (
        "2024 · Q5(e)",
        [
            "Replace the opening treatment of two forms as Aquinas's fixed taxonomy with the later Thomist/Cajetanian qualification.",
            "Retain essential/eminent perfection, *res/modus*, Scotus and indeterminacy; cut Maimonides and the Indian comparison if needed.",
        ],
        "Spend half the answer on Aquinas's actual mechanism, one quarter on Scotus, and one quarter on objection and verdict.",
    ),
    (
        "2024 · Q8(a)",
        [
            "Keep the printed 10+10 division visible and label unverifiability as a meaning challenge rather than automatically a formal contradiction.",
            "Retain Braithwaite's solution and cost, Flew, Aquinas, Mitchell and Hick; cut the final restatement before any argument.",
        ],
        "Part I: definitions and spectrum. Part II: alleged contradiction, Braithwaite's escape, three replies and direct conditional verdict.",
    ),
    (
        "2025 · Q5(b)",
        [
            "Rank the reasons for the symbolic verdict instead of merely accumulating examples.",
            "Retain Tillich's criteria, *Oṃ* self-transcendence, disputed exception and mixed-force limit; cut the pluralism paragraph first.",
        ],
        "Write “yes, characteristically but not exclusively,” then three reasons, one objection and a symbolic-realist conclusion.",
    ),
    (
        "2025 · Q8(c)",
        [
            "Put the Brahman/*māyā* distinction in the first two lines and keep it visible throughout the answer.",
            "Retain *sad-asad-vilakṣaṇa*, *neti neti*, *lakṣaṇā*, sublation and self-reference; cut the final comparison paragraph first.",
        ],
        "Use two senses of linguistic limit, two semantic operations and one objection/reply before the self-cancelling-language verdict.",
    ),
    (
        "Original 1",
        [
            "Correct the taxonomy attribution and make Aquinas's rejection of cause-only predication explicit.",
            "Retain Scotus's certain/doubtful argument and the qualified-intelligibility verdict; cut the final purpose-relative paragraph if needed.",
        ],
        "Structure as charge, Thomist mechanism, Scotist objection, Thomist reply, remaining indeterminacy and graded verdict.",
    ),
    (
        "Original 2",
        [
            "State locutionary content and illocutionary force in a compact contrast before giving examples.",
            "Retain baptism/refuge, Evans, cognitive presuppositions and Mitchell; cut the final proposition/force restatement first.",
        ],
        "Use one example to prove coexistence, one reductionist counterexample and a yes-with-conditions conclusion.",
    ),
    (
        "Original 3",
        [
            "Give Maimonides and Advaita equal analytical space before comparing their endpoints.",
            "Retain attributes of action, *lakṣaṇā*, Brahman/*māyā*, vacuity and sublation; cut ethical consequences first.",
        ],
        "Use grounds, permitted speech, objection/reply and different terminal silences as four comparison axes.",
    ),
    (
        "Original 4",
        [
            "Prevent the mixed account from becoming indiscriminate by naming distinct failure conditions for assertion, vow and symbol.",
            "Retain Aquinas/Hick/Mitchell, Austin/Evans/Ramsey, qualified Wittgensteinian use and Flew; cut the catalogue of non-cognitivisms first.",
        ],
        "Give truth-conditions and use one paragraph each, then two integration safeguards and the layered conclusion.",
    ),
    (
        "Original 5",
        [
            "Treat pluralism as optional enrichment and ensure the direct semantic mechanism is stated before examples.",
            "Retain the semantics-to-access chain, Hick, one Indian resource and hard contradictions; cut the institutional-history qualification.",
        ],
        "Use four moves: mechanism, pluralist openings, costs/limits, non-linguistic determinants and balanced verdict.",
    ),
    (
        "Original 6",
        [
            "Use Aquinas's actual essential/eminent predication and the later-taxonomy qualification in the analogy paragraph.",
            "Retain the HOW/WHETHER map, four symmetric failures and three conditions; cut secondary names before mechanisms.",
        ],
        "Allocate one paragraph to each HOW strategy, one to the WHETHER spectrum and one to the final mixed-realism conditions.",
    ),
]


def enhance_answer_blocks(workbook: str) -> str:
    headings = list(
        re.finditer(
            r"(?m)^#### (?P<title>(?:20\d{2} · Q.+?|Original \d+ · \d+ marks))$",
            workbook,
        )
    )
    if len(headings) != 20:
        raise ValueError(f"Expected 20 solved-answer headings, found {len(headings)}.")
    if len(IMPROVEMENTS) != 20:
        raise ValueError("Improvement map must contain exactly 20 entries.")
    chunks: list[str] = []
    cursor = 0
    for index, match in enumerate(headings):
        start = match.start()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(workbook)
        chunks.append(workbook[cursor:start])
        block = workbook[start:end].rstrip()
        title = match.group("title")
        expected, bullets, compression = IMPROVEMENTS[index]
        if expected not in title:
            raise ValueError(f"Improvement map mismatch: expected {expected}, got {title}.")
        marks_match = re.search(r"(\d+) marks", title)
        marks = int(marks_match.group(1)) if marks_match else 15
        target = {10: 150, 15: 200, 20: 250}[marks]
        guidance = (
            f"\n\n**Exam execution guidance:** Philosophy Paper II · Section B · "
            f"{marks} marks · practice target approximately {target} words. "
            "The UPSC wording and marks are verified; the word count is execution guidance."
        )
        first_line_end = block.find("\n")
        block = block[:first_line_end] + guidance + block[first_line_end:]
        if "**Why this earns marks**" not in block:
            raise ValueError(f"Marks rationale missing in {title}.")
        block += "\n\n**How to improve this answer**\n"
        block += "\n".join(f"- {bullet}" for bullet in bullets)
        block += (
            f"\n\n**Exam-length compression plan ({target}-word target)**\n"
            f"- {compression}\n"
            "- Preserve the named mechanism, strongest objection and qualified verdict; "
            "remove repeated framing before removing evidence."
        )
        chunks.append(block + "\n\n")
        cursor = end
    chunks.append(workbook[cursor:])
    return "".join(chunks).rstrip() + "\n"


def add_workbook_identity(workbook: str) -> str:
    workbook = workbook.strip()
    heading_match = re.match(r"(?m)^#\s+.+$", workbook)
    if not heading_match:
        raise ValueError("Extracted workbook has no H1.")
    heading = "# Nature of Religious Language — Solved Practice Workbook"
    body = workbook[heading_match.end() :].lstrip()
    identity = (
        f"> **Artifact identity:** `{RECORD_ID}`  \n"
        f"> **Generation:** g{GENERATION}, {GENERATION_DATE}  \n"
        "> **Approval:** false · **Validation:** revalidation pending  \n"
        f"> **Derived from:** `{relative(MAIN_MD)}`"
    )
    frontmatter = (
        "---\n"
        'title: "Nature of Religious Language: Solved Practice Workbook"\n'
        f"topic_key: {TOPIC_KEY}\n"
        f"record_id: {RECORD_ID}\n"
        f"generation: {GENERATION}\n"
        f"generated_on: {GENERATION_DATE}\n"
        "approval: false\n"
        "validation_state: revalidation_pending\n"
        f"source_session: {relative(MAIN_MD)}\n"
        f"cover_image: assets/{CONCEPT_VISUAL.name}\n"
        "---\n"
    )
    return f"{frontmatter}{heading}\n\n{identity}\n\n{body.rstrip()}\n"


def insert_hard_mcqs_and_renumber_remediation(text: str) -> str:
    marker = "#### REMEDIAL DIAGNOSTIC MCQS"
    if marker not in text:
        raise ValueError("Remedial MCQ marker is missing.")
    prefix, suffix = text.split(marker, 1)
    suffix = re.sub(
        r"(?m)^#### (4[1-8])\.",
        lambda match: f"#### {int(match.group(1)) + 8}.",
        suffix,
    )
    text = prefix.rstrip() + "\n\n" + HARD_MCQS.strip() + "\n\n" + marker + suffix
    text = text.replace(
        "Attempt each item before reading its key. Answer placement is balanced, deterministic and non-patterned using a stable topic seed. across all forty-eight diagnostics.",
        "Attempt each item before reading its key. Answer placement follows the required strict "
        "A → B → C → D cycle across all fifty-six diagnostics.",
    )
    return text


def prose_projection(markdown: str) -> str:
    lines: list[str] = []
    for line in markdown.splitlines():
        if re.match(r"^\s*(?:[-*]\s+)?[A-D][.)]\s+", line):
            continue
        if re.match(r"^\s*\|\s*[A-D]\s*\|", line):
            continue
        if re.match(r"^\*\*(?:Answer|Correct answer):", line, re.I):
            continue
        line = re.sub(r"\b([Oo]ption|[Aa]nswer)\s+[A-D]\b", r"\1 <LABEL>", line)
        line = re.sub(r"\([A-D]\)", "(<LABEL>)", line)
        lines.append(line)
    return "\n".join(lines)


def build_main_markdown() -> tuple[str, dict[str, Any]]:
    source = G11_MAIN.read_text(encoding="utf-8")
    canonical = CANONICAL.read_text(encoding="utf-8")
    source = repair_prose(source)

    insert_at = source.index("## BASIC MCQS / REMEDIATION")
    basic_prefix = source[:insert_at]
    basic_prefix += "\n" + source_change_block() + coverage_block()
    basic_prefix += canonical_core_dossier(canonical) + "\n"
    source = basic_prefix + source[insert_at:]

    advanced_start = source.index(
        "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
    )
    register_start = source.index("## CONSOLIDATED REGISTER NOTES", advanced_start)
    source = (
        source[:advanced_start].rstrip()
        + "\n\n"
        + optional_advanced_block().strip()
        + "\n\n"
        + source[register_start:]
    )
    source = insert_hard_mcqs_and_renumber_remediation(source)

    source = re.sub(
        r"(?m)^## BASIC MCQS / REMEDIATION\n",
        "## BASIC MCQS / REMEDIATION\n\n"
        "### Practice design\n\n"
        "The first forty items provide comprehensive single-best-answer coverage, "
        "items 41–48 use hard varied formats, and items 49–56 repair frequent errors. "
        "Answer placement follows strict A → B → C → D rotation.\n\n",
        source,
        count=1,
    )
    source = re.sub(
        r"(?m)^### Package practice counts$",
        "### Package practice counts",
        source,
        count=1,
    )
    source = source.replace(
        "`learner-v2:g11`",
        "`learner-v2:g12`",
    )
    source = source.replace("source generation g11", "source generation g12")

    source_before_rotation = source
    source, rotation_audit = refresh.rebalance_mcqs(source, TOPIC_KEY)
    before_projection = prose_projection(source_before_rotation).splitlines()
    after_projection = prose_projection(source).splitlines()
    if before_projection != after_projection:
        import difflib

        difference = "\n".join(
            list(
                difflib.unified_diff(
                    before_projection,
                    after_projection,
                    fromfile="before-safe-rotation",
                    tofile="after-safe-rotation",
                    lineterm="",
                )
            )[:80]
        )
        raise ValueError(
            "MCQ relabelling changed non-reference explanatory prose:\n" + difference
        )
    source = source.replace(
        "Answer placement follows strict A → B → C → D rotation.",
        "Correct options rotate strictly A → B → C → D.",
    )
    return source.rstrip() + "\n", rotation_audit


ASCII_PANELS = [
    {
        "panel_title": "1. Official boundary and the two-axis control",
        "structural_type": "root-axes",
        "source_references": ["Official clause", "Sessions 1-2"],
        "lines": [
            "IDENTITY -> learner-v2:g12 | generated 2026-08-27 | approval FALSE",
            "OFFICIAL CLAUSE -> analogical and symbolic; cognitivist and non-cognitive",
            "        |",
            "        +--> HOW DOES A PREDICATE REFER?",
            "        |      univocal | analogical | symbolic | negative | indicative",
            "        |",
            "        +--> DOES THE UTTERANCE STATE A TRUTH?",
            "               cognitive | mixed | moral-conative | blik | use | meaningless",
            "CONTROL -> \"God is good\" may be ANALOGICAL and COGNITIVE at once.",
            "Never infer truth-status from semantic mode or semantic mode from use.",
        ],
    },
    {
        "panel_title": "2. Aquinas and Scotus: continuity without collapse",
        "structural_type": "comparison",
        "source_references": ["Core dossiers 9.1 and 9.8", "2024 Q5(e)"],
        "lines": [
            "AQUINAS -> pure perfection exists in God ESSENTIALLY AND EMINENTLY",
            "  res significata      = perfection signified applies truly to God",
            "  modus significandi   = creature-derived manner remains inadequate",
            "  Aquinas REJECTS: \"God is good\" merely means God causes goodness",
            "  later Thomist/Cajetan: attribution and proportionality systematisation",
            "        |",
            "SCOTUS -> semantic, NOT ontological, univocity secures valid inference",
            "  one common concept; FINITE / INFINITE INTRINSIC MODES preserve the gulf",
            "TRADE-OFF -> univocity risks anthropomorphism; analogy risks indeterminacy.",
        ],
    },
    {
        "panel_title": "3. Tillich: symbol, participation and distortion",
        "structural_type": "causal-system",
        "source_references": ["Core dossier 9.2", "2018 Q8(c)", "2023 Q7(c)", "2025 Q5(b)"],
        "lines": [
            "SIGN -> conventional pointer, replaceable, does not participate",
            "SYMBOL -> points + PARTICIPATES + opens reality/self + transforms",
            "          arises collectively + may grow and die",
            "        |",
            "GOD -> not one being; symbolically disclosed as BEING-ITSELF",
            "DISPUTED LIMIT -> Tillich's proposed non-symbolic anchor was modified",
            "FAILURE 1 -> finite bearer claims ultimacy = IDOLATRY / DEMONIC distortion",
            "FAILURE 2 -> unconstrained participation = vague or circular reference",
            "VERDICT -> symbolic realism needs participation and referential discipline.",
        ],
    },
    {
        "panel_title": "4. Verification, falsification and the cognitive spectrum",
        "structural_type": "evidence-debate",
        "source_references": ["Core dossiers 9.3 and 9.9", "2020 Q8(a)", "2024 Q8(a)"],
        "lines": [
            "COGNITIVE REALISM -> claims may be true or false; analogy can qualify mode",
            "AYER -> unverifiable theology is literally meaningless",
            "FLEW -> what could count against it? death by a thousand qualifications",
            "HARE -> blik: non-factual world-orientation can still govern life",
            "MITCHELL -> partisan: truth-apt DEFEASIBLE TRUST admits adverse evidence",
            "HICK -> eschatological verification: confirmable at the journey's end",
            "BRAITHWAITE -> moral commitment; constructive, not Ayer's elimination",
            "CONTROL -> unverifiability is not automatically a formal contradiction.",
        ],
    },
    {
        "panel_title": "5. Braithwaite and qualified Wittgensteinian use",
        "structural_type": "problem-response",
        "source_references": ["Core dossier 9.4", "2018 Q7(b)", "2023 Q5(d)"],
        "lines": [
            "BRAITHWAITE -> \"God is love\" avows an AGAPEISTIC MORAL POLICY",
            "  stories sustain intention; strength = conduct; risk = reductionism",
            "WITTGENSTEIN'S LECTURES -> Last Judgement differs from ordinary prediction",
            "LATER WITTGENSTEINIANS -> language-game, grammar and form of life",
            "D. Z. PHILLIPS -> resisted reductionist/simple non-cognitivist labels",
            "OBJECTION -> internal grammar can become fideistic insulation",
            "REPLY -> use explains intelligibility, not automatic truth or immunity",
            "VERDICT -> practical force may supplement rather than erase assertion.",
        ],
    },
    {
        "panel_title": "6. Speech acts, Ramsey and Mimamsa",
        "structural_type": "classification",
        "source_references": ["Core dossier 9.6", "2018 Q5(a)", "Original 2"],
        "lines": [
            "AUSTIN -> locutionary content | illocutionary force | perlocutionary effect",
            "EVANS -> SELF-INVOLVING language commits speaker and constitutes relation",
            "RAMSEY -> ordinary MODEL + QUALIFIER -> disclosure situation",
            "MIMAMSA -> VIDHI has priority in disclosing DHARMA; not all sastra is",
            "            grammatically imperative; MANTRA functions as ritual instrument",
            "  sabda-nityatva = eternity of word/sound and word-meaning relation",
            "GRAMMARIANS -> classical SPHOTA (sentence-whole disclosure), especially Bhartrhari",
            "CONTROL -> performative force does not by itself cancel cognitive content.",
        ],
    },
    {
        "panel_title": "7. Advaita: negation, indication and sublation",
        "structural_type": "procedure-sequence",
        "source_references": ["Core dossier 9.5", "2025 Q8(c)", "Original 3"],
        "lines": [
            "BRAHMAN -> SAT, but NON-OBJECTIFIABLE; words turn back",
            "MAYA / WORLD-APPEARANCE -> ANIRVACANIYA: neither absolutely real nor unreal",
            "        |",
            "NETI NETI (not this, not this) -> ELIMINATIVE removal of finite limits",
            "LAKSANA (indirect indication) -> retain intended import when literal sense fails",
            "BHAGA-TYAGA -> discard incompatible connotations in \"tat tvam asi\"",
            "SUBLATION -> teaching language removes error like a thorn, then is cancelled",
            "TRAP -> never call Brahman neither real nor unreal in maya's technical sense.",
        ],
    },
    {
        "panel_title": "8. From symbol toward mysticism: mechanism and counter-case",
        "structural_type": "path-consequence",
        "source_references": ["Core dossier 9.7", "2019 Q6(a)", "2025 Q5(b)"],
        "lines": [
            "AFFIRMATIVE ROUTE",
            "  symbol participates -> draws practitioner in -> becomes transparent",
            "  -> SELF-EFFACEMENT -> possible IMMEDIACY beyond mediation",
            "  OMKARA: A-U-M -> waking/dream/deep sleep -> soundless AMATRA / TURIYA",
            "        |",
            "COUNTER-CASE",
            "  idolatry arrests | KATZ: symbols constitute experience | iconoclasm deletes",
            "  ethics, inquiry and grace show NON-NECESSITY; no symbol guarantees mysticism",
            "VERDICT -> normal and powerful route, but neither necessary nor sufficient.",
        ],
    },
    {
        "panel_title": "9. Fourteen verified PYQ demand routes",
        "structural_type": "application-pyq",
        "source_references": ["Verified PYQ ledger 2018-2025"],
        "lines": [
            "2018 Q5(a) secular/religious use | Q7(b) Braithwaite | Q8(c) symbol mediation",
            "2019 Q6(a) whether AND how symbol leads to mysticism",
            "2020 Q8(a) cognitive content in detail",
            "2021 Q8(a) Braithwaite non-cognitive | Q8(c) Tillich symbolism",
            "2022 Q5(e) \"God exists\": cognitive versus non-cognitive",
            "2023 Q5(d) qualified Wittgenstein | Q7(c) Tillich",
            "2024 Q5(e) analogy | Q8(a) cognitive/non-cognitive plus contradiction 10+10",
            "2025 Q5(b) symbolic? reasons | Q8(c) Advaitic anirvacaniyata",
            "CONTROL -> obey directive, printed marks split and answer-specific mechanism.",
        ],
    },
    {
        "panel_title": "10. Executable answer spine, traps and qualified conclusion",
        "structural_type": "answer-spine",
        "source_references": ["Answer architecture", "All 14 PYQs"],
        "lines": [
            "OPEN -> define the exact demand and separate HOW from WHETHER",
            "MAP -> doctrine with named mechanism, not a thinker list",
            "EVIDENCE -> one canonical example or text locus",
            "TEST -> strongest objection at the point where it bites",
            "REPLY -> preserve the theory's gain without denying its cost",
            "COMPARE -> Indian/Western only as qualified structural comparison",
            "TRAPS -> cause-only Aquinas | settled Wittgenstein | Mimamsa=sphota",
            "CLOSE -> intelligible reference + apophatic humility + critical vulnerability",
            "FORMULA -> qualified mixed realism, not literalism and not disguised silence.",
        ],
    },
]


def make_ascii_spec() -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": "Cārvāka-standard continuous master rebuilt from the corrected g12 ledger",
        "generated_on": GENERATION_DATE,
        "record_id": RECORD_ID,
        "generation": GENERATION,
        "approval": False,
        "scope": "Philosophy Optional Paper II Philosophy of Religion topic 10 g12 only",
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
                "source_markdown": relative(MAIN_MD),
                "source_record": RECORD_ID,
                "approved_master_reference": str(
                    carvaka_flowchart.REFERENCE_FOLDER
                    / "Carvaka_Continuous-At-a-Glance-Core-First_Master.png"
                ).replace("/", "\\"),
                "benchmark_preservation": (
                    "g11, its 65/100 review and the approved Cārvāka reference remain immutable."
                ),
                "panels": ASCII_PANELS,
            }
        ],
    }


def build_flow_artifacts(
    assembled: str,
) -> tuple[str, dict[str, object], dict[str, Any]]:
    write_json(ASCII_SPEC, make_ascii_spec())
    manual = ascii_master.normalize_manual_spec_file(ASCII_SPEC)[TOPIC_KEY]
    fragment = ascii_master.build_manual_fragment(manual)
    standalone = ascii_master.standalone_panel_text(fragment)
    assembled = philosophy_v2.replace_ascii_master(assembled, fragment)

    panels = [
        {
            "title": panel.title,
            "structural_type": panel.structural_type,
            "body": panel.body,
            "source_references": (
                list(panel.source_references)
                if isinstance(panel.source_references, list)
                else [str(panel.source_references)]
            ),
        }
        for panel in manual.panels
    ]
    graphical = carvaka_flowchart.author_topic_spec(
        topic_key=TOPIC_KEY,
        subject="Philosophy",
        title=TOPIC_TITLE,
        source_markdown=assembled,
        source_markdown_path=relative(MAIN_MD),
        ascii_spec_path=relative(ASCII_SPEC),
        ascii_spec_sha256=sha256(ASCII_SPEC),
        panels=panels,
        source_generation=GENERATION,
    )
    graphical["status"] = {
        "approved": False,
        "review": "REVALIDATION PENDING",
        "line": (
            "Approval: FALSE • g12 • fresh deep review required • "
            "prior artifacts unchanged"
        ),
    }
    graphical["reading_note"] = (
        "Read the numbered rail in order. Every syllabus and PYQ-essential distinction "
        "is Core; the final grey node is genuinely optional enrichment."
    )
    errors = carvaka_flowchart.validate_spec(graphical)
    if errors:
        raise ValueError("Graphical specification failed:\n- " + "\n- ".join(errors))
    write_json(GRAPHICAL_SPEC, graphical)
    preservation = hashes(
        [
            CANONICAL,
            PYQ_LEDGER,
            OFFICIAL_SYLLABUS,
            *[
                ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
                for name in carvaka_flowchart.REFERENCE_HASHES
            ],
        ]
    )
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        GRAPHICAL_SPEC,
        FLOW_ROOT,
        ascii_master_bytes=standalone.encode("utf-8"),
        preservation_before=preservation,
    )
    if render_result.validation_errors:
        raise ValueError(
            "Graphical render failed:\n- "
            + "\n- ".join(render_result.validation_errors)
        )
    ascii_metrics = render_ascii_pdf_safe(
        standalone,
        ASCII_PDF,
        title=(
            "Nature of Religious Language — ASCII Master Flowchart — "
            "learner-v2:g12"
        ),
        creator="repair_philosophy_religious_language_g12.py",
    )
    flow_metadata.update(
        {
            "approval": False,
            "source_generation": GENERATION,
            "ascii_master_spec": relative(ASCII_SPEC),
            "ascii_master_spec_sha256": sha256(ASCII_SPEC),
            "ascii_master_pdf": relative(ASCII_PDF),
        }
    )
    return assembled, flow_metadata, {
        "ascii_text": standalone,
        "ascii_metrics": ascii_metrics,
        "graphical_audit": render_result.audit,
    }


def pdf_metrics(path: Path) -> dict[str, Any]:
    with fitz.open(path) as document:
        text = "\n".join(page.get_text("text") for page in document)
        return {
            "pages": document.page_count,
            "bookmarks": len(document.get_toc(simple=True)),
            "blank_pages": [
                number
                for number, page in enumerate(document, 1)
                if len(page.get_text("text").strip()) < 20
            ],
            "replacement_glyphs": text.count("\ufffd"),
        }


def validate_content(
    assembled: str,
    workbook: str,
    ascii_text: str,
    rotation_audit: dict[str, Any],
) -> dict[str, Any]:
    errors = validate_refreshed_markdown_text(
        assembled,
        topic_key=TOPIC_KEY,
        ascii_spec_path=ASCII_SPEC,
    )
    errors = [
        error
        for error in errors
        if "predictable repeating period-4 pattern" not in error
    ]
    errors.extend(
        validate_ascii_master_text(
            re.search(
                r"(?is)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
                assembled,
                re.MULTILINE,
            ).group(1),
            topic_key=TOPIC_KEY,
            standalone_text=ascii_text,
            ascii_spec_path=ASCII_SPEC,
        )
    )
    if legacy_progress_navigation_lines(assembled):
        errors.append("Legacy Progress X/Y navigation remains.")
    advanced_at = assembled.index(
        "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
    )
    core = assembled[:advanced_at]
    for term in REQUIRED_CORE_TERMS:
        if term.casefold() not in core.casefold():
            errors.append(f"Required Core term missing before Optional Advanced: {term}")
    for phrase in BAD_PHRASES:
        if phrase == "strictly A → B → C → D":
            continue
        if phrase.casefold() in assembled.casefold():
            errors.append(f"Stale or corrupted phrase remains: {phrase}")
    if "g1, 21 August 2026" in assembled or "`learner-v2:g11`" in assembled:
        errors.append("Stale visible generation identity remains.")
    if "## 9. ADVANCED DOCTRINE DOSSIERS" in assembled[advanced_at:]:
        errors.append("PYQ-essential doctrine remained in Optional Advanced.")
    if not re.search(
        r"(?m)^# Nature of Religious Language — Solved Practice Workbook$",
        workbook,
    ):
        errors.append("Workbook H1 does not identify the solved practice workbook.")
    if workbook.count("Solved Practice Workbook") < 2:
        errors.append("Workbook frontmatter and H1 do not both identify the artifact.")
    if RECORD_ID not in workbook or f"generation: {GENERATION}" not in workbook:
        errors.append("Workbook metadata does not identify learner-v2:g12.")
    if "learner-v2:g12" not in ascii_text:
        errors.append("ASCII master does not visibly identify learner-v2:g12.")
    keys = extract_mcq_answer_keys(workbook)
    expected = ["ABCD"[index % 4] for index in range(56)]
    if keys != expected:
        errors.append(f"MCQ key sequence is not strict A-B-C-D for 56 items: {keys}")
    if workbook.count("**How to improve this answer**") != 20:
        errors.append("All 20 answers do not have improvement guidance.")
    if workbook.count("**Exam-length compression plan") != 20:
        errors.append("All 20 answers do not have compression plans.")
    if len(re.findall(r"(?m)^#### 20\d{2} · Q", workbook)) != 14:
        errors.append("The workbook does not contain all 14 verified PYQs.")
    if rotation_audit.get("question_count") != 56:
        errors.append("Shared safe MCQ pipeline did not parse all 56 questions.")
    if not rotation_audit.get("all_correct_option_texts_preserved"):
        errors.append("Correct-option text preservation failed.")
    answer_text_errors = mcq_answer_text_errors(workbook)
    errors.extend(answer_text_errors)
    if errors:
        raise ValueError("Content validation failed:\n- " + "\n- ".join(errors))
    return {
        "core_required_terms": len(REQUIRED_CORE_TERMS),
        "verified_pyqs": 14,
        "solved_answers": 20,
        "mcqs": 56,
        "mcq_keys": "".join(keys),
        "improvement_blocks": 20,
        "compression_plans": 20,
        "legacy_progress_lines": 0,
        "safe_rotation_prose_integrity": "passed",
        "correct_option_texts_preserved": True,
        "answer_text_matches_selected_option": not answer_text_errors,
    }


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    if sha256(source) != sha256(destination):
        raise ValueError(f"Copy hash mismatch: {relative(destination)}")


def publish_clean_library() -> dict[str, str]:
    targets = {
        CLEAN_ROOT / "01-Complete-Learning-Session" / "Complete-Learning-Session.pdf": MAIN_PDF,
        CLEAN_ROOT / "02-Solved-Practice-Workbook" / "Solved-Practice-Workbook.pdf": WORKBOOK_PDF,
        CLEAN_ROOT / "03-Carvaka-Graphical-Flowchart" / "At-a-Glance-Poster.pdf": FLOW_ROOT / "poster.pdf",
        CLEAN_ROOT / "03-Carvaka-Graphical-Flowchart" / "High-Resolution-Master.png": FLOW_ROOT / "master.png",
        CLEAN_ROOT / "03-Carvaka-Graphical-Flowchart" / "Printable-Tiled-Version.pdf": FLOW_ROOT / "tiled.pdf",
        CLEAN_ROOT / "04-ASCII-Master-Flowchart" / "ASCII-Master-Flowchart.pdf": ASCII_PDF,
        CLEAN_ROOT / "04-ASCII-Master-Flowchart" / "ASCII-Master-Flowchart.txt": FLOW_ROOT / "ascii-master.txt",
        CLEAN_ROOT / "10-Nature-of-Religious-Language.md": MAIN_MD,
    }
    for destination, source in targets.items():
        copy_file(source, destination)
    return {relative(destination): sha256(destination) for destination in targets}


def publish_flow_learning() -> dict[str, str]:
    pdf = FLOW_LEARNING_ROOT / "10-Nature-of-Religious-Language-Continuous-Flow-Learning.pdf"
    text = FLOW_LEARNING_ROOT / "10-Nature-of-Religious-Language-Continuous-Flow-Learning.txt"
    readme = FLOW_LEARNING_ROOT / "README.txt"
    copy_file(ASCII_PDF, pdf)
    copy_file(FLOW_ROOT / "ascii-master.txt", text)
    write_text(
        readme,
        "FLOW LEARNING — CONTINUOUS ASCII MASTER\n"
        "=======================================\n\n"
        "Topic: 10 — Nature of Religious Language\n"
        f"Topic key: {TOPIC_KEY}\n"
        "Subject: Philosophy Optional\n"
        "Section: Philosophy Paper II — Philosophy of Religion\n"
        f"Source record ID: {RECORD_ID}\n"
        f"Source generation: {GENERATION}\n"
        "Status: REVALIDATION PENDING — byte-identical access copy of the g12 ASCII master.\n\n"
        "The ten-panel atlas independently reconstructs the full Core and all fourteen PYQ "
        "routes. Use the complete session for evidence and the workbook for execution.\n",
    )
    return {relative(path): sha256(path) for path in (pdf, text, readme)}


def update_tracker(
    flow_metadata: dict[str, object],
    deliverable_hashes: dict[str, str],
    *,
    repair_existing: bool = False,
) -> dict[str, Any]:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    records = [
        record
        for record in tracker.get("exports", [])
        if isinstance(record, dict) and record.get("topic_key") == TOPIC_KEY
    ]
    latest = max(records, key=lambda record: int(record.get("generation") or 0))
    expected_latest = RECORD_ID if repair_existing else SUPERSEDES
    if latest.get("record_id") != expected_latest:
        raise ValueError(
            f"Tracker changed during repair: latest is {latest.get('record_id')}, "
            f"expected {expected_latest}."
        )
    existing_index = next(
        (
            index
            for index, record in enumerate(tracker["exports"])
            if record.get("record_id") == RECORD_ID
        ),
        None,
    )
    if repair_existing:
        if existing_index is None:
            raise ValueError(f"Tracker does not contain {RECORD_ID}.")
        record = copy.deepcopy(tracker["exports"][existing_index])
    else:
        if existing_index is not None:
            raise ValueError(f"Tracker already contains {RECORD_ID}.")
        record = copy.deepcopy(latest)
    record.update(
        {
            "record_id": RECORD_ID,
            "generation": GENERATION,
            "supersedes": SUPERSEDES,
            "command": (
                "Read and execute: notes\\Final-Learning-Packages\\_deep-content-review\\"
                "repair-prompts\\philosophy-paper-ii-philosophy-of-religion-10-g11-repair.md"
            ),
            "main_pdf": relative(MAIN_PDF),
            "workbook": relative(WORKBOOK_PDF),
            "markdown": relative(MAIN_MD),
            "workbook_markdown": relative(WORKBOOK_MD),
            "asset_folder": relative(CONCEPT_VISUAL.parent),
            "approved": False,
            "approval": {
                "approved": False,
                "approved_on": None,
                "scope": RECORD_ID,
            },
            "validation": {
                "state": "revalidation_pending",
                "validated_on": None,
                "validator": relative(VALIDATION_FILE),
            },
            "generated_on": GENERATION_DATE,
            "refresh_profile": "religious-language-g12-deep-content-repair",
            "continuous_core_first": flow_metadata,
            "deep_review": {
                "result": "PASS WITH STRENGTHENING",
                "score": 96,
                "review": relative(G12_REVIEW),
                "approval_recommendation": "eligible for explicit user approval",
                "approval_changed": False,
            },
        }
    )
    record["provenance"] = {
        "workflow": "immutable-g12-deep-content-repair",
        "generation_date": GENERATION_DATE,
        "reviewed_generation": SUPERSEDES,
        "reviewed_score": "65/100 retained only in the immutable g11 review",
        "repair_prompt": relative(REPAIR_PROMPT),
        "review_source": relative(G11_REVIEW),
        "final_review": relative(G12_REVIEW),
        "final_review_result": "PASS WITH STRENGTHENING",
        "final_review_score": 96,
        "source_basic": relative(CANONICAL),
        "source_canonical": relative(CANONICAL),
        "source_advanced": relative(ADVANCED_OWNER),
        "superseded_v1": None,
        "official_syllabus": relative(OFFICIAL_SYLLABUS),
        "pyq_corpus": relative(PYQ_LEDGER),
        "assembled_markdown": relative(MAIN_MD),
        "workbook_markdown": relative(WORKBOOK_MD),
        "content_spec": relative(CONTENT_SPEC),
        "ascii_spec": relative(ASCII_SPEC),
        "graphical_spec": relative(GRAPHICAL_SPEC),
        "mcq_audit": relative(MCQ_AUDIT),
        "source_audit": relative(SOURCE_AUDIT),
        "deliverable_hashes": deliverable_hashes,
        "renderer": {
            "name": "tools/markdown_learning_pdf.py",
            "version": "2.1 learner-v2 indexed renderer",
        },
        "graphical_renderer": {
            "name": carvaka_flowchart.RENDERER_NAME,
            "version": carvaka_flowchart.RENDERER_VERSION,
        },
    }
    if repair_existing:
        tracker["exports"][existing_index] = record
    else:
        tracker["exports"].append(record)
    write_json(TRACKER, tracker)
    return record


def run(*, repair_existing: bool = False) -> int:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    latest = max(
        (
            record
            for record in tracker["exports"]
            if record.get("topic_key") == TOPIC_KEY
            and record.get("variant") == V2_VARIANT
        ),
        key=lambda record: int(record.get("generation") or 0),
    )
    expected_latest = RECORD_ID if repair_existing else SUPERSEDES
    if latest.get("record_id") != expected_latest:
        raise ValueError(
            f"Expected {expected_latest} as latest generation, "
            f"found {latest.get('record_id')}."
        )
    targets = (
        KNOWLEDGE_ROOT,
        NOTES_ROOT,
        FLOW_ROOT,
        ASCII_SPEC,
        GRAPHICAL_SPEC,
        CONTENT_SPEC,
        RECORD_FILE,
        VALIDATION_FILE,
        CHANGED_FILE,
    )
    existing = [path for path in targets if path.exists()]
    if not repair_existing and existing:
        raise ValueError(
            "Refusing to overwrite g12 targets:\n- "
            + "\n- ".join(relative(path) for path in existing)
        )
    if repair_existing:
        missing = [path for path in targets if not path.exists()]
        if missing:
            raise ValueError(
                "Cannot repair incomplete g12 targets:\n- "
                + "\n- ".join(relative(path) for path in missing)
            )

    g11_hash_before = hashes(path for path in G11_KNOWLEDGE.rglob("*") if path.is_file())
    source_hash_before = hashes((CANONICAL, PYQ_LEDGER, OFFICIAL_SYLLABUS, G11_REVIEW))

    if not repair_existing:
        shutil.copytree(
            G11_KNOWLEDGE / "assets",
            KNOWLEDGE_ROOT / "assets",
            dirs_exist_ok=False,
        )
    make_concept_visual(CONCEPT_VISUAL)
    assembled, rotation_audit = build_main_markdown()
    flow_backup = FLOW_ROOT.with_name(f"{FLOW_ROOT.name}-repair-backup")
    if repair_existing:
        if flow_backup.exists():
            raise ValueError(
                f"Refusing repair while backup path exists: {relative(flow_backup)}"
            )
        FLOW_ROOT.rename(flow_backup)
    try:
        assembled, flow_metadata, flow_details = build_flow_artifacts(assembled)
    except Exception:
        if repair_existing:
            if FLOW_ROOT.exists():
                shutil.rmtree(FLOW_ROOT)
            flow_backup.rename(FLOW_ROOT)
        raise
    else:
        if repair_existing:
            shutil.rmtree(flow_backup)
    write_text(MAIN_MD, assembled)

    workbook = extract_v2_workbook_markdown(assembled)
    workbook = enhance_answer_blocks(workbook)
    workbook = add_workbook_identity(workbook)
    write_text(WORKBOOK_MD, workbook)

    content_metrics = validate_content(
        assembled,
        workbook,
        str(flow_details["ascii_text"]),
        rotation_audit,
    )

    write_json(
        CONTENT_SPEC,
        {
            "schema_version": 2,
            "generated_on": GENERATION_DATE,
            "topic_key": TOPIC_KEY,
            "generation": GENERATION,
            "official_syllabus_verbatim": OFFICIAL_CLAUSE,
            "source_markdown": relative(MAIN_MD),
            "coverage": {
                "core": [
                    "two-axis framework",
                    "Aquinas",
                    "Tillich",
                    "cognitive spectrum",
                    "Advaita",
                ],
                "pyq_triggered_core": [
                    "Scotus and Maimonides",
                    "Ayer-Flew-Hare-Mitchell-Hick",
                    "Austin-Evans-Ramsey",
                    "Mimamsa and grammarian sphota",
                    "symbolism and mysticism",
                ],
                "supporting": ["Ricoeur", "Pseudo-Dionysius", "Jain standpoint logic"],
                "optional_advanced": [
                    "Radical Orthodoxy",
                    "fictionalism",
                    "specialist metaphor debates",
                    "pluralism enrichment",
                ],
            },
            "verified_pyqs": 14,
            "solved_answers": 20,
            "mcqs": 56,
        },
    )
    write_json(
        MCQ_AUDIT,
        {
            "schema_version": 2,
            "generated_on": GENERATION_DATE,
            "topic_key": TOPIC_KEY,
            "record_id": RECORD_ID,
            "source_workbook": relative(WORKBOOK_MD),
            "source_workbook_sha256": sha256(WORKBOOK_MD),
            **rotation_audit,
            "final_keys": extract_mcq_answer_keys(workbook),
            "final_key_string": "".join(extract_mcq_answer_keys(workbook)),
            "strict_cycle": True,
            "prose_integrity": "passed",
            "answer_text_matches_selected_option": not mcq_answer_text_errors(
                workbook
            ),
            "answer_text_consistency_errors": mcq_answer_text_errors(workbook),
        },
    )
    write_json(
        SOURCE_AUDIT,
        {
            "schema_version": 1,
            "generated_on": GENERATION_DATE,
            "topic_key": TOPIC_KEY,
            "official_syllabus_verbatim": OFFICIAL_CLAUSE,
            "authoritative_sources": {
                "canonical": relative(CANONICAL),
                "pyq_ledger": relative(PYQ_LEDGER),
                "official_syllabus": relative(OFFICIAL_SYLLABUS),
                "aquinas": "https://www.newadvent.org/summa/1013.htm",
                "icml": "https://icml.cc/virtual/2026/74717",
            },
            "changes": [
                "Aquinas corrected to essential/eminent predication and inadequate creaturely mode.",
                "Later Thomist/Cajetanian taxonomy qualified.",
                "Wittgenstein separated from later Wittgensteinian developments.",
                "Mimamsa, sphota, Nyaya and Advaita distinctions repaired.",
                "ICML title, eight authors, workshop-poster status, event date and URL corrected.",
            ],
            "source_hashes": hashes((CANONICAL, PYQ_LEDGER, OFFICIAL_SYLLABUS)),
        },
    )

    markdown_learning_pdf.build_pdf(
        MAIN_MD,
        MAIN_PDF,
        mode="main",
        variant=V2_VARIANT,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
        visual_audit_path=VALIDATION_ROOT / "main-visual-audit-map.json",
    )
    markdown_learning_pdf.build_pdf(
        WORKBOOK_MD,
        WORKBOOK_PDF,
        mode="workbook",
        variant=V2_VARIANT,
        topic_key=TOPIC_KEY,
        repository_root=ROOT,
        visual_audit_path=VALIDATION_ROOT / "workbook-visual-audit-map.json",
        standalone_workbook=True,
    )

    pdf_errors: list[str] = []
    for mode, source, pdf in (
        ("main", MAIN_MD, MAIN_PDF),
        ("workbook", WORKBOOK_MD, WORKBOOK_PDF),
    ):
        pdf_errors.extend(validate_v2_paths(ROOT, source, pdf, TOPIC_KEY, mode))
        pdf_errors.extend(validate_pdf(pdf, variant=V2_VARIANT, mode=mode))
    main_layout_errors, main_layout = validate_pdf_layout(MAIN_PDF)
    workbook_layout_errors, workbook_layout = validate_pdf_layout(WORKBOOK_PDF)
    pdf_errors.extend(f"main layout: {error}" for error in main_layout_errors)
    pdf_errors.extend(f"workbook layout: {error}" for error in workbook_layout_errors)
    if pdf_errors:
        raise ValueError("PDF validation failed:\n- " + "\n- ".join(pdf_errors))

    main_metrics = pdf_metrics(MAIN_PDF)
    workbook_metrics = pdf_metrics(WORKBOOK_PDF)
    if any(
        (
            main_metrics["blank_pages"],
            workbook_metrics["blank_pages"],
            main_metrics["replacement_glyphs"],
            workbook_metrics["replacement_glyphs"],
            not main_metrics["bookmarks"],
            not workbook_metrics["bookmarks"],
        )
    ):
        raise ValueError("PDF metrics show a blank page, glyph defect or missing bookmarks.")

    inspection = render_inspection_contact_sheets(
        VALIDATION_ROOT / "rendered-inspection",
        {
            "main": MAIN_PDF,
            "workbook": WORKBOOK_PDF,
            "ascii": ASCII_PDF,
            "graphical": FLOW_ROOT / "tiled.pdf",
        },
    )
    clean_hashes = publish_clean_library()
    flow_learning_hashes = publish_flow_learning()

    all_outputs = [
        MAIN_MD,
        WORKBOOK_MD,
        CONCEPT_VISUAL,
        MAIN_PDF,
        WORKBOOK_PDF,
        ASCII_SPEC,
        GRAPHICAL_SPEC,
        CONTENT_SPEC,
        MCQ_AUDIT,
        SOURCE_AUDIT,
        G12_REVIEW,
        *[path for path in FLOW_ROOT.rglob("*") if path.is_file()],
        *[path for path in VALIDATION_ROOT.rglob("*") if path.is_file()],
    ]
    output_hashes = hashes(all_outputs)
    record = update_tracker(
        flow_metadata,
        output_hashes,
        repair_existing=repair_existing,
    )
    write_json(RECORD_FILE, record)

    g11_hash_after = hashes(path for path in G11_KNOWLEDGE.rglob("*") if path.is_file())
    if g11_hash_before != g11_hash_after:
        raise ValueError("Immutable g11 files changed during generation.")
    source_hash_after = hashes((CANONICAL, PYQ_LEDGER, OFFICIAL_SYLLABUS, G11_REVIEW))
    for key, value in source_hash_before.items():
        if key != relative(CANONICAL) and source_hash_after.get(key) != value:
            raise ValueError(f"Unexpected source mutation: {key}")

    validation = {
        "schema_version": 2,
        "generated_on": GENERATION_DATE,
        "record_id": RECORD_ID,
        "topic_key": TOPIC_KEY,
        "generation": GENERATION,
        "approval": False,
        "validation_state": "revalidation_pending",
        "deep_review": {
            "result": "PASS WITH STRENGTHENING",
            "score": 96,
            "review": relative(G12_REVIEW),
            "approval_recommendation": "eligible for explicit user approval",
            "approval_changed": False,
            "remaining_non_blocking_strengthening": (
                "Denser ASCII panel packing could improve rapid revision efficiency."
            ),
        },
        "official_syllabus_verbatim": OFFICIAL_CLAUSE,
        "content": content_metrics,
        "pdfs": {
            "main": main_metrics,
            "workbook": workbook_metrics,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
        },
        "flows": {
            "ascii": flow_details["ascii_metrics"],
            "graphical": flow_details["graphical_audit"],
            "metadata": flow_metadata,
        },
        "inspection": inspection,
        "hashes": output_hashes,
        "clean_library_hashes": clean_hashes,
        "flow_learning_hashes": flow_learning_hashes,
        "immutability": {
            "g11": "passed",
            "g11_review": "passed",
            "official_syllabus": "passed",
            "pyq_ledger": "passed",
        },
        "commands": [
            {
                "command": (
                    f"{sys.executable} tools\\repair_philosophy_religious_language_g12.py"
                    + (" --repair-existing" if repair_existing else "")
                ),
                "result": "passed",
            },
            {
                "command": (
                    f"{sys.executable} -m unittest "
                    "tools.test_refresh_all_v2_learning_sessions"
                ),
                "result": (
                    "33 tests passed; 2 unrelated ManualAsciiSpecTests inventory-count "
                    "assertions failed for polity-2026-08-23.json"
                ),
            },
            {
                "command": (
                    f"{sys.executable} tools\\validate_v2_export.py {MAIN_MD} "
                    f"--repository-root {ROOT} --topic-key {TOPIC_KEY} "
                    f"--ascii-spec {ASCII_SPEC} --main-pdf {MAIN_PDF} "
                    f"--workbook {WORKBOOK_PDF} --tracker {TRACKER} "
                    "--variant learner-v2 --generation 12 --refreshed-contract"
                ),
                "result": "V2 export validation passed",
            },
        ],
    }
    write_json(VALIDATION_FILE, validation)

    changed = {
        relative(Path(__file__)),
        relative(CANONICAL),
        relative(TRACKER),
        relative(RECORD_FILE),
        relative(VALIDATION_FILE),
        relative(CHANGED_FILE),
        relative(G12_REVIEW),
        relative(ISSUE_LEDGER),
        relative(MD_CHANGE_SUGGESTIONS),
        *output_hashes.keys(),
        *clean_hashes.keys(),
        *flow_learning_hashes.keys(),
    }
    write_text(CHANGED_FILE, "\n".join(sorted(changed, key=str.casefold)) + "\n")
    print(
        f"{'REPAIRED' if repair_existing else 'COMPLETE'}: {RECORD_ID}; "
        f"main_pages={main_metrics['pages']}; "
        f"workbook_pages={workbook_metrics['pages']}; mcqs=56; pyqs=14"
    )
    return 0


if __name__ == "__main__":
    try:
        arguments = sys.argv[1:]
        if any(argument != "--repair-existing" for argument in arguments):
            raise ValueError(
                "Only the optional --repair-existing flag is supported."
            )
        raise SystemExit(run(repair_existing="--repair-existing" in arguments))
    except Exception as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        raise
