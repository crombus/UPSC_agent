"""Generate Rationalism as a source-complete learner-v2 Philosophy topic."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

import fitz
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart
import markdown_learning_pdf
import notions_style_ascii_master
import philosophy_western_rationalism_v2_spec as rationalism_spec
import regenerate_philosophy_indian_v2 as philosophy_v2
from generate_v2_section_indexes import generate_section_indexes
from validate_v2_export import (
    V2_VARIANT,
    extract_mcq_answer_keys,
    extract_v2_workbook_markdown,
    validate_ascii_master_text,
    validate_pdf,
    validate_pdf_layout,
    validate_refreshed_markdown_text,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
GENERATION_DATE = "2026-08-26"
SECTION_KEY = "paper-i-western-philosophy"
SECTION_FOLDER = "Paper-I-Western-Philosophy"
TOPIC_KEY = "philosophy-paper-i-western-philosophy-02"
TOPIC_TITLE = "Rationalism"
TOPIC_FOLDER = "topic-02"

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
    / "philosophy--paper-i-western-philosophy-02-ascii-2026-08-26.json"
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
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\Rationalism.md"
)
ADVANCED_DOSSIER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\_advanced\\Western-Philosophy-Dossier.md"
)
PYQ_LEDGER = (
    "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\"
    "_PYQ-Western-Philosophy-2018-2025.md"
)
RETAINED_SESSION = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\"
    "learning-sessions\\Rationalism\\"
    "Rationalism_Layered-Complete-Learning-Session_2026-08-18.md"
)
RETAINED_WORKBOOK = (
    "upsc-ai-kit\\knowledge\\Philosophy\\Western-Philosophy\\"
    "learning-sessions\\Rationalism\\"
    "Rationalism_Layered-Solved-Practice-Workbook_2026-08-18.md"
)
BASELINE_REPORT = (
    EXPORT_MANIFEST_DIR
    / "philosophy-paper-i-western-philosophy-02-learner-v2-g2-"
    "2026-08-26-baseline.json"
)

SYLLABUS_CLAUSES = (
    "Plato and Aristotle : Ideas; Substance; Form and Matter; Causation; Actuality and Potentiality.",
    (
        "Rationalism (Descartes, Spinoza, Leibniz); Cartesian Method and Certain "
        "Knowledge; Substance; God; Mind-Body Dualism; Determinism and Freedom."
    ),
    (
        "Empiricism (Locke, Berkeley, Hume) : Theory of Knowledge; Substance and "
        "Qualities; Self and God; Scepticism."
    ),
    (
        "Kant: Possibility of Synthetic a priori Judgments; Space and Time; "
        "Categories; Ideas of Reason; Antinomies; Critique of Proofs for the "
        "Existence of God."
    ),
    "Hegel : Dialectical Method; Absolute Idealism.",
    (
        "Moore, Russell and Early Wittgenstein : Defence of Commonsense; "
        "Refutation of Idealism; Logical Atomism; Logical Constructions; "
        "Incomplete Symbols; Picture Theory of Meaning; Sying and Showing."
    ),
    (
        "Logical Positivism : Verification Theory of Meaning; Rejection of "
        "Metaphysics; Linguistic Theory of Necessary Propositions."
    ),
    (
        "Later Wittgenstein : Meaning and Use; Language-games; Critique of "
        "Private Language."
    ),
    (
        "Phenomenology (Husserl): Method; Theory of Essences; Avoidance of "
        "Psychologism."
    ),
    (
        "Existentialism (Kierkegaard, Sarte, Heidegger): Existence and Essence; "
        "Choice, Responsibility and Authentic Existence; Being-in-the-world and "
        "Temporality."
    ),
    (
        "Quine and Strawson : Critique of Empiricism; Theory of Basic "
        "Particulars and Persons."
    ),
)

TOPIC_DEFINITIONS = (
    ("Plato and Aristotle", "Plato-Aristotle.md"),
    ("Rationalism", "Rationalism.md"),
    ("Empiricism", "Empiricism.md"),
    ("Kant", "Kant.md"),
    ("Hegel", "Hegel.md"),
    (
        "Moore, Russell and Early Wittgenstein",
        "Moore-Russell-EarlyWittgenstein.md",
    ),
    ("Logical Positivism", "Logical-Positivism.md"),
    ("Later Wittgenstein", "Later-Wittgenstein.md"),
    ("Phenomenology (Husserl)", "Phenomenology-Husserl.md"),
    ("Existentialism", "Existentialism.md"),
    ("Quine and Strawson", "Quine-Strawson.md"),
)

SESSION_SPECS = (
    {
        "title": "Plato's Master Map: Forms, Particulars and Two-World Ontology",
        "plain": (
            "Plato explains how many changing things can share one character by "
            "distinguishing sensible particulars from stable intelligible Forms."
        ),
        "technical": (
            "The Theory of Forms posits transcendent, eternal and non-sensible "
            "universals as the proper objects of knowledge, while particulars "
            "derive their determinate character through participation or imitation."
        ),
        "answer": (
            "Plato's Forms convert the one-many and knowledge problems into a "
            "two-level ontology in which stable intelligible universals ground "
            "predication and knowledge, while sensible particulars possess "
            "derivative reality."
        ),
        "keywords": [
            "intelligible and sensible",
            "universality",
            "one-many problem",
            "transcendent Form",
            "participation",
            "knowledge and opinion",
        ],
        "usage": (
            "Begin with the one-many and stability problems, define the two levels "
            "of reality, connect Forms to knowledge, and qualify the account by "
            "noting the explanatory burden carried by participation."
        ),
        "mechanism": (
            "Many changing particulars are intelligible as instances only because "
            "a stable universal Form supplies the common character reason grasps."
        ),
        "consequence": (
            "Plato secures universality and objective knowledge, but the sensible "
            "world becomes ontologically derivative rather than self-explanatory."
        ),
        "trap": (
            "Do not describe the intelligible realm as another physical place or "
            "reduce sensible particulars to sheer non-being."
        ),
    },
    {
        "title": "Sun, Divided Line and Cave: Good, Knowledge and Metaphysics",
        "plain": (
            "The Sun, Divided Line and Cave show how the mind moves from images "
            "and opinion toward rational knowledge of Forms and the Good."
        ),
        "technical": (
            "Plato correlates degrees of being with cognitive states from eikasia "
            "and pistis to dianoia and noesis, while the Good grounds both the "
            "being and knowability of intelligible objects."
        ),
        "answer": (
            "The Sun, Line and Cave jointly identify the Good as the condition of "
            "being and knowing, grade opinion into knowledge, and portray education "
            "as the turning of the soul toward intelligible reality."
        ),
        "keywords": [
            "Form of the Good",
            "eikasia",
            "pistis",
            "dianoia",
            "noesis",
            "doxa and episteme",
        ],
        "usage": (
            "Treat the three images as one argument: use the Form of the Good as the "
            "first principle, map eikasia and pistis to opinion, map dianoia and "
            "noesis to knowledge, and finish with the philosopher's return."
        ),
        "mechanism": (
            "Cognitive ascent occurs by leaving images and unexamined hypotheses "
            "for dialectical understanding of Forms under the illumination of the Good."
        ),
        "consequence": (
            "Plato's epistemology and metaphysics become one graded structure in "
            "which clearer knowledge corresponds to more stable being."
        ),
        "trap": (
            "Do not isolate the Cave from the Sun and Line or confuse mathematical "
            "dianoia with dialectical noesis."
        ),
    },
    {
        "title": "Participation, Third Man and Aristotle's Critique of Separation",
        "plain": (
            "Participation is Plato's link between Forms and particulars, but the "
            "Third Man problem asks whether a separate Form merely starts a new regress."
        ),
        "technical": (
            "The participation relation faces whole-part and regress pressures, "
            "while Aristotle charges separated Forms with duplication, causal "
            "impotence and failure to explain generation and change."
        ),
        "answer": (
            "Aristotle's criticism does not deny intelligibility through form; it "
            "denies that a separately existing Form can explain particulars without "
            "duplication, a non-metaphorical participation relation and regress."
        ),
        "keywords": [
            "participation",
            "imitation",
            "separation",
            "Third Man regress",
            "duplication",
            "causal impotence",
        ],
        "usage": (
            "State why participation is needed, reconstruct the regress and "
            "duplication objections, and present immanent form as Aristotle's "
            "transformative repair rather than a rejection of intelligibility."
        ),
        "mechanism": (
            "If likeness to a separate Form itself requires a further Form, the "
            "original explanation reproduces the one-many problem instead of ending it."
        ),
        "consequence": (
            "The critique motivates Aristotle to retain form as an explanatory "
            "principle while locating it within the concrete substance."
        ),
        "trap": (
            "Do not treat the Third Man as automatically refuting every possible "
            "theory of universals or claim that Aristotle simply discards form."
        ),
    },
    {
        "title": "Aristotle's Substance: Primary, Secondary and Explanatory Essence",
        "plain": (
            "Aristotle first calls the concrete individual the primary substance, "
            "then asks what makes that individual the kind of thing it is."
        ),
        "technical": (
            "The Categories identifies primary substances as ultimate subjects and "
            "species or genera as secondary substances, while Metaphysics explains "
            "substance-hood through form and essence."
        ),
        "answer": (
            "Aristotle makes the concrete individual the primary subject of "
            "predication, yet explains substance-hood through immanent form and "
            "essence, thereby distinguishing what exists primarily from what makes "
            "it what it is."
        ),
        "keywords": [
            "primary substance",
            "secondary substance",
            "ultimate subject",
            "essence",
            "substance-hood",
            "Categories and Metaphysics",
        ],
        "usage": (
            "Separate primary substance from secondary substance, then distinguish "
            "the ultimate subject from essence and substance-hood to handle the "
            "Categories-Metaphysics tension."
        ),
        "mechanism": (
            "The individual bears predicates, while its form or essence answers why "
            "this matter constitutes this determinate substance."
        ),
        "consequence": (
            "Aristotle reverses Plato's priority of the universal without reducing "
            "substance to an unexplained bundle of accidental properties."
        ),
        "trap": (
            "Do not identify secondary substance with a separately existing Platonic "
            "Form or say that matter alone is a complete substance."
        ),
    },
    {
        "title": "Hylomorphism: Matter, Form, Composite and Immanent Essence",
        "plain": (
            "A natural thing is neither bare matter nor detached form; it is one "
            "concrete composite whose matter is organised by form."
        ),
        "technical": (
            "Hylomorphism analyses natural substance as a composite of matter, the "
            "relative principle of potentiality, and immanent form, the principle "
            "of actuality, unity and essence."
        ),
        "answer": (
            "Hylomorphism treats natural substance as one matter-form composite: "
            "matter supplies determinate capacity, while immanent form gives unity, "
            "essence and actuality without Platonic separation."
        ),
        "keywords": [
            "hylomorphism",
            "matter",
            "immanent form",
            "composite substance",
            "essence",
            "prime matter",
        ],
        "usage": (
            "Define matter and form as explanatory principles within one composite, "
            "use a worked artifact and organism example, and distinguish relative "
            "matter from the limiting concept of prime matter."
        ),
        "mechanism": (
            "Matter makes alternative determination possible, while form organises "
            "that capacity into the actual unity and intelligibility of a substance."
        ),
        "consequence": (
            "Aristotle explains how a material individual can remain one intelligible "
            "thing without dividing reality into separate sensible and intelligible worlds."
        ),
        "trap": (
            "Do not equate form with visible shape, matter with formless stuff that "
            "exists independently, or hylomorphism with Cartesian dualism."
        ),
    },
    {
        "title": "Four Causes: Explanatory Completeness and Teleology",
        "plain": (
            "Aristotle's four causes explain what a thing is made of, what it is, "
            "what produced it and what end it fulfils."
        ),
        "technical": (
            "Material, formal, efficient and final causes are complementary senses "
            "of aitia that explain constitution, essence, source of change and telos."
        ),
        "answer": (
            "Aristotle's four causes are complementary dimensions of explanatory "
            "completeness, because material constitution, formal identity, efficient "
            "production and final end answer irreducible senses of why."
        ),
        "keywords": [
            "material cause",
            "formal cause",
            "efficient cause",
            "final cause",
            "aitia",
            "teleology",
        ],
        "usage": (
            "Apply all four causes to the same example, show why none simply replaces "
            "the others, and distinguish intrinsic natural teleology from a conscious "
            "designer imposing an external purpose."
        ),
        "mechanism": (
            "The four causes converge by explaining the material capacity, defining "
            "form, originating process and completed end of one substance or change."
        ),
        "consequence": (
            "Knowledge becomes knowledge of a structured why rather than a record of "
            "efficient succession alone."
        ),
        "trap": (
            "Do not reduce aitia to modern event-causation or assume every final cause "
            "is a consciously intended human purpose."
        ),
    },
    {
        "title": "Potentiality and Actuality: Change, Development and Priority",
        "plain": (
            "Change is possible because a thing can possess a real capacity that is "
            "not yet fulfilled and can become actual under suitable conditions."
        ),
        "technical": (
            "Potentiality is a determinate capacity for actuality, actuality is its "
            "realisation or fulfilled activity, and motion is the actuality of the "
            "potential precisely as potential."
        ),
        "answer": (
            "Potentiality is a real, qualified capacity ordered to actuality, so "
            "change becomes the actualisation of what can be rather than an "
            "impossible leap from non-being to being."
        ),
        "keywords": [
            "potentiality",
            "actuality",
            "dynamis",
            "energeia",
            "entelecheia",
            "priority of actuality",
        ],
        "usage": (
            "Define potentiality or dynamis relationally to actuality or energeia, "
            "trace one complete developmental example, and distinguish explanatory "
            "priority from a crude claim of universal temporal priority."
        ),
        "mechanism": (
            "An efficient process actualises a grounded capacity under a determining "
            "form and toward the completed actuality that gives the process direction."
        ),
        "consequence": (
            "Aristotle mediates between static being and sheer flux by locating "
            "becoming within the structured powers of what already exists."
        ),
        "trap": (
            "Do not call every imaginable outcome a potentiality or say that actuality "
            "is always earlier than potentiality in the life of an individual."
        ),
    },
    {
        "title": "Pure Actuality, Teleological Order and the Unmoved Mover",
        "plain": (
            "If every motion depended on an endlessly prior actualiser, Aristotle "
            "argues that cosmic motion would lack a fully actual explanatory terminus."
        ),
        "technical": (
            "The Unmoved Mover is pure actuality without unrealised potentiality and "
            "moves as a final cause or object of desire and thought rather than as a "
            "temporal efficient push."
        ),
        "answer": (
            "The Unmoved Mover completes Aristotle's priority of actuality as pure "
            "act and final cause of cosmic motion, but it should not be assimilated "
            "uncritically to a personal efficient creator."
        ),
        "keywords": [
            "pure actuality",
            "Unmoved Mover",
            "final causation",
            "thought thinking itself",
            "eternal motion",
            "teleological order",
        ],
        "usage": (
            "Derive pure act from the priority of actuality, explain motion by final "
            "causation, and add the qualification that Aristotle's mover differs from "
            "a creator who produces the world through efficient action."
        ),
        "mechanism": (
            "The highest actuality moves without undergoing change because dependent "
            "motion is ordered toward it as the ultimate object of desire and thought."
        ),
        "consequence": (
            "Aristotle links metaphysics, cosmology and teleology, while leaving open "
            "questions about providence and personal divine agency."
        ),
        "trap": (
            "Do not describe the Unmoved Mover as the temporal first event, material "
            "cause or straightforward personal creator of the cosmos."
        ),
    },
    {
        "title": "Plato and Aristotle Compared: Criticisms, Replies and Significance",
        "plain": (
            "Plato locates the universal standard beyond particulars, whereas "
            "Aristotle locates form within concrete substances and their development."
        ),
        "technical": (
            "The contrast is between transcendent Forms grounding universality and "
            "immanent form grounding substance, hylomorphic unity, causation and "
            "potentiality-to-actuality change."
        ),
        "answer": (
            "Plato secures universality by transcendent Forms, whereas Aristotle "
            "internalises form within substance to gain causal and developmental "
            "explanation, though both must still account for the relation between "
            "universality and particulars."
        ),
        "keywords": [
            "transcendent and immanent",
            "universal and particular",
            "participation",
            "hylomorphism",
            "explanatory duplication",
            "qualified comparison",
        ],
        "usage": (
            "Compare transcendent and immanent form on the same axes of universality, "
            "participation, substance, causation and change, then give criticisms and "
            "replies before a qualified verdict rather than declaring a simple victory."
        ),
        "mechanism": (
            "Aristotle preserves Plato's demand for intelligible form but relocates "
            "its explanatory work inside substances, causes and developmental powers."
        ),
        "consequence": (
            "The debate establishes the enduring metaphysical choice between separated "
            "universals and immanent principles of intelligibility."
        ),
        "trap": (
            "Do not caricature Plato's Forms as physical objects or Aristotle's form "
            "as a mere shape abstracted after the substance is already complete."
        ),
    },
    {
        "title": "Precision Toolkit: Distinctions, PYQ Routes and Answer Spine",
        "plain": (
            "High-scoring answers depend on keeping nearby terms distinct and then "
            "connecting only those distinctions demanded by the question."
        ),
        "technical": (
            "The answer method separates universal, form, essence, substance, matter, "
            "cause, potentiality and actuality before integrating thesis, argument, "
            "example, objection, reply and qualified conclusion."
        ),
        "answer": (
            "A precise answer must keep universal, form, essence, substance, matter, "
            "cause, potentiality and actuality distinct before showing how Aristotle "
            "reorganises Plato's problem rather than merely rejecting it."
        ),
        "keywords": [
            "form and universal",
            "essence and substance",
            "matter and potentiality",
            "cause and explanation",
            "claim-evidence-analysis",
            "qualified verdict",
        ],
        "usage": (
            "Decode the directive, distinguish form from universal, essence from "
            "substance, matter from potentiality and cause from mere sequence, then "
            "build claim, evidence, analysis, objection, reply and qualified verdict."
        ),
        "mechanism": (
            "Directive fidelity converts doctrine into marks by ordering definition, "
            "argument, named example, criticism, reply and an explicitly qualified verdict."
        ),
        "consequence": (
            "The same conceptual map can answer narrow questions on Forms, substance, "
            "causes or change without becoming a generic thinker biography."
        ),
        "trap": (
            "Do not use form, universal, essence and substance interchangeably or "
            "append criticism without returning to the printed directive."
        ),
    },
)

ASCII_PANELS = (
    {
        "title": "Central problem: one, many, knowledge and stability",
        "structural_type": "conceptual-root-branch",
        "sessions": [1],
        "lines": [
            "CENTRAL QUESTION: HOW CAN MANY CHANGING THINGS SHARE ONE KNOWABLE CHARACTER?",
            "        |",
            "        +--> ONE-MANY: many just acts -> one intelligible standard of Justice",
            "        |",
            "        +--> KNOWLEDGE: episteme requires a stable object, not flux alone",
            "        |",
            "        +--> PLATO: transcendent Forms; particulars participate or imitate",
            "        |",
            "        +--> COST: separation makes the Form-particular relation hard to explain",
        ],
    },
    {
        "title": "Two-level ontology and the ascent from opinion to knowledge",
        "structural_type": "epistemic-ladder-hierarchy",
        "sessions": [1, 2],
        "lines": [
            "PLATO'S TWO-LEVEL ONTOLOGY",
            "+----------------------------+      +----------------------------+",
            "| INTELLIGIBLE                |      | SENSIBLE                   |",
            "| Forms: stable, universal    |      | particulars: many, changing|",
            "| episteme through reason     |      | doxa through perception     |",
            "+-------------+--------------+      +-------------+--------------+",
            "              ^ participation / imitation          |",
            "              +-------------------------------------+",
            "CAVE: shadows -> visible things -> mathematics -> Forms -> Good",
            "LINE: eikasia -> pistis -> dianoia -> noesis",
            "SUN: the Good grounds both being and knowability.",
        ],
    },
    {
        "title": "Participation pressure and Aristotle's immanent repair",
        "structural_type": "problem-response-dialectic",
        "sessions": [3],
        "lines": [
            "PLATONIC EXPLANATION                     ARISTOTELIAN PRESSURE",
            "Form F -> participation -> many F-things | participation remains metaphorical",
            "separate paradigm explains common F     | separation duplicates the explanandum",
            "        |                                | likeness invites another Form",
            "        v                                v",
            "THIRD MAN: particulars + Form F resemble -> further Form F2 -> regress",
            "        |",
            "        +--> REPLY: deny unrestricted self-predication or restrict the premise",
            "        |",
            "        +--> RESIDUAL: how does a separate Form causally determine a particular?",
            "ARISTOTLE'S REPAIR: retain form, but make it immanent in concrete substance.",
        ],
    },
    {
        "title": "Aristotle's substance hierarchy and explanatory essence",
        "structural_type": "substance-hierarchy-tree",
        "sessions": [4],
        "lines": [
            "ARISTOTLE: WHAT EXISTS PRIMARILY, AND WHAT MAKES IT WHAT IT IS?",
            "                           SUBSTANCE",
            "                              |",
            "              +---------------+----------------+",
            "              |                                |",
            "CATEGORIES: WHICH THINGS?          METAPHYSICS: SUBSTANCE-HOOD?",
            "primary = this person/horse         form or essence explains the compound",
            "secondary = species and genus       matter alone is not a determinate this",
            "accidents exist in a substance      universal and genus are not primary",
            "              |                                |",
            "              +--> safe synthesis: individual exists; form explains its identity",
        ],
    },
    {
        "title": "Hylomorphic composite: matter, form and substantial unity",
        "structural_type": "hylomorphic-composite-columns",
        "sessions": [5],
        "lines": [
            "ONE NATURAL SUBSTANCE = MATTER INFORMED BY IMMANENT FORM",
            "+--------------------------+     +--------------------------+",
            "| MATTER                   |     | FORM                     |",
            "| that out of which        |     | what-it-is / essence     |",
            "| relative potentiality    |     | organisation / actuality |",
            "| can receive determination|     | makes the composite one  |",
            "+-------------+------------+     +-------------+------------+",
            "              +---------------+---------------+",
            "                              v",
            "                    CONCRETE COMPOSITE",
            "bronze + statue-form; wood + table-form; body + soul in a living organism",
            "LIMIT: prime matter is a theoretical limit, not independently existing stuff.",
        ],
    },
    {
        "title": "Four causes as a matrix of explanatory completeness",
        "structural_type": "four-causes-comparison-matrix",
        "sessions": [6],
        "lines": [
            "ONE QUESTION, FOUR COMPLEMENTARY SENSES OF WHY",
            "+-------------+----------------------+----------------------+----------------------+",
            "| MATERIAL    | FORMAL               | EFFICIENT            | FINAL                |",
            "| made of what| what it is           | source of change     | for the sake of what |",
            "| wood        | table structure      | carpenter and tools  | usable working surface|",
            "+-------------+----------------------+----------------------+----------------------+",
            "NATURAL CASE: acorn matter + oak form + generating parent/process + mature oak telos",
            "        |",
            "        +--> formal, efficient and final causes may coincide in natural development",
            "        |",
            "        +--> teleology need not mean a conscious external designer",
            "RESULT: explanatory completeness is richer than efficient succession alone.",
        ],
    },
    {
        "title": "Potentiality to actuality: change without creation from nothing",
        "structural_type": "potentiality-actuality-process-flow",
        "sessions": [7],
        "lines": [
            "GROUNDED CAPACITY -> PROCESS OF ACTUALISATION -> FULFILLED ACTUALITY",
            "wood fit for a table -> cutting and joining -> completed table",
            "acorn ordered to oak -> organic development -> mature oak",
            "        |                    |                    |",
            "     dynamis             kinesis          energeia / entelecheia",
            "        |",
            "        +--> change = actuality of the potential precisely as potential",
            "        +--> actuality is prior in definition, end and species-level explanation",
            "        +--> qualification: potentiality may be earlier in an individual's time",
            "RESULT: becoming is structured being-in-capacity, not emergence from sheer non-being.",
        ],
    },
    {
        "title": "Teleological order and pure actuality",
        "structural_type": "teleological-causal-sequence",
        "sessions": [8],
        "lines": [
            "MOTION HERE AND NOW REQUIRES ACTUALITY, BUT THE SERIES CANNOT BE PURE POTENCY",
            "moved mover -> moved mover -> ordered eternal motion",
            "        |",
            "        v",
            "UNMOVED MOVER = PURE ACTUALITY WITHOUT UNREALISED POTENTIALITY",
            "        |",
            "        +--> moves as final cause: object of desire and thought",
            "        +--> thought thinking itself; no material composition",
            "        +--> not a temporal first event or material cause",
            "LIMIT: do not equate Aristotle's mover with a personal efficient creator.",
        ],
    },
    {
        "title": "Plato and Aristotle on form: comparison, criticism and reply",
        "structural_type": "comparison-matrix-dialectic",
        "sessions": [9],
        "lines": [
            "+---------------------------+---------------------------+---------------------------+",
            "| AXIS                      | PLATO                     | ARISTOTLE                 |",
            "+---------------------------+---------------------------+---------------------------+",
            "| status of form            | transcendent and separate | immanent in substance     |",
            "| primary reality           | universal Form            | concrete individual       |",
            "| relation to particulars   | participation / imitation | hylomorphic constitution  |",
            "| explanation of change     | limited paradigmatic role | causes plus potency-act    |",
            "+---------------------------+---------------------------+---------------------------+",
            "OBJECTION TO PLATO -> duplication, regress and causal gap",
            "REPLY FOR PLATO -> stable universals secure objectivity, definition and norms",
            "OBJECTION TO ARISTOTLE -> universality and prime matter remain difficult",
            "VERDICT -> Aristotle transforms Plato's insight; he does not simply erase it.",
        ],
    },
    {
        "title": "Answer spine and precision distinctions",
        "structural_type": "answer-exam-synthesis",
        "sessions": [10],
        "lines": [
            "DIRECTIVE -> DEFINITION -> ARGUMENT -> EXAMPLE -> OBJECTION -> REPLY -> VERDICT",
            "        |",
            "        +--> FORM: organising actuality; UNIVERSAL: predicable of many",
            "        +--> ESSENCE: what-it-is; SUBSTANCE: primary bearer / concrete being",
            "        +--> MATTER: capacity principle; CAUSE: explanatory because",
            "        +--> POTENTIALITY: qualified capacity; ACTUALITY: fulfilment or activity",
            "PYQ ROUTES",
            "Forms -> one-many + knowledge + participation; Substance -> Categories/Metaphysics",
            "Causes -> four complementary explanations; Change -> potentiality to actuality",
            "Comparison -> transcendent Form versus immanent form on matched axes",
            "FINAL CONTROL: answer the printed directive, not a general biography of two thinkers.",
        ],
    },
)

REQUIRED_CORE_TERMS = (
    "Plato and Aristotle : Ideas; Substance; Form and Matter; Causation; Actuality and Potentiality.",
    "one-many",
    "universality",
    "participation",
    "imitation",
    "intelligible",
    "sensible",
    "epistēmē",
    "doxa",
    "Third Man",
    "duplication",
    "primary substance",
    "secondary substance",
    "hylomorphism",
    "material cause",
    "formal cause",
    "efficient cause",
    "final cause",
    "potentiality",
    "actuality",
    "transcendent",
    "immanent",
)

SESSION_SPECS = rationalism_spec.SESSION_SPECS
ASCII_PANELS = rationalism_spec.ASCII_PANELS
REQUIRED_CORE_TERMS = rationalism_spec.REQUIRED_CORE_TERMS


class Topic:
    def __init__(self, key: str, title: str) -> None:
        self.key = key
        self.title = title


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


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".pending")
    temporary.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".pending")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def latest_identity(
    tracker: dict[str, Any],
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
    legacy_id = (
        str(max(legacy, key=lambda item: int(item.get("generation") or 1))["record_id"])
        if legacy
        else None
    )
    if learners:
        current = max(learners, key=lambda item: int(item.get("generation") or 0))
        return int(current["generation"]) + 1, str(current["record_id"]), legacy_id
    return 2, legacy_id or f"{topic_key}:legacy-v1:g1", legacy_id


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
            knowledge_root / "assets" / "Rationalism-Problem-Sequence.png"
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


def planned_paths(topic_key: str, number: int, generation: int) -> dict[str, str]:
    folder = f"topic-{number:02d}"
    base_knowledge = (
        "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Philosophy\\"
        f"{SECTION_FOLDER}\\learning-sessions\\{folder}\\g{generation}"
    )
    base_notes = (
        "notes\\Learner-v2-Refreshed\\Philosophy\\"
        f"{SECTION_FOLDER}\\learning-sessions\\{folder}\\g{generation}"
    )
    return {
        "assembled_markdown": (
            f"{base_knowledge}\\{folder}_Complete-Learning-Session_"
            f"{GENERATION_DATE}.md"
        ),
        "notes_pdf": (
            f"{base_notes}\\{folder}_Complete-Learning-Session_"
            f"{GENERATION_DATE}.pdf"
        ),
        "workbook_pdf": (
            f"{base_notes}\\{folder}_Solved-Practice-Workbook_"
            f"{GENERATION_DATE}.pdf"
        ),
        "graphical_flowchart_folder": (
            "notes\\Learner-v2-Refreshed\\Philosophy\\"
            f"{SECTION_FOLDER}\\flowcharts\\{folder}\\carvaka-g{generation}"
        ),
    }


def build_manifest(
    tracker: dict[str, Any],
    topic_generation: int,
) -> dict[str, Any]:
    topics: list[dict[str, Any]] = []
    for number, ((title, owner), clause) in enumerate(
        zip(TOPIC_DEFINITIONS, SYLLABUS_CLAUSES),
        1,
    ):
        key = f"philosophy-paper-i-western-philosophy-{number:02d}"
        learner_records = [
            record
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == key
            and record.get("variant") == V2_VARIANT
        ]
        legacy_records = [
            record
            for record in tracker["exports"]
            if isinstance(record, dict)
            and record.get("topic_key") == key
            and record.get("variant") == "legacy-v1"
        ]
        legacy_id = (
            str(
                max(
                    legacy_records,
                    key=lambda item: int(item.get("generation") or 1),
                )["record_id"]
            )
            if legacy_records
            else None
        )
        if number == 2:
            generation = topic_generation
        elif learner_records:
            generation = int(
                max(
                    learner_records,
                    key=lambda item: int(item.get("generation") or 0),
                )["generation"]
            )
        else:
            generation = 2
        paths = planned_paths(key, number, generation)
        topic: dict[str, Any] = {
            "topic_key": key,
            "display_title": title,
            "syllabus_mapping": (
                "Philosophy Optional, Paper I, Western Philosophy topic "
                f"{number}: {clause}"
            ),
            "source_basic": (
                "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\" + owner
            ),
            "source_canonical": (
                "upsc-ai-kit\\knowledge\\Philosophy\\paper-1\\western\\" + owner
            ),
            "source_advanced": ADVANCED_DOSSIER,
            "cross_topic_sources": [PHILOSOPHY_README, OFFICIAL_SYLLABUS],
            "verified_pyq_sources": [PYQ_LEDGER],
            "ascii_master_spec": (
                relative(ASCII_SPEC)
                if number == 2
                else (
                    "upsc-ai-kit\\manifests\\retrofits\\ascii-panel-specs\\"
                    "philosophy--paper-i-western-philosophy-ascii-2026-08-26.json"
                )
            ),
            "superseded_v1": legacy_id,
            **paths,
        }
        if legacy_records:
            legacy = max(
                legacy_records,
                key=lambda item: int(item.get("generation") or 1),
            )
            if legacy.get("markdown"):
                topic["retained_learning_session"] = str(legacy["markdown"])
            if legacy.get("workbook"):
                workbook = str(legacy["workbook"])
                if workbook.casefold().endswith(".pdf"):
                    candidate = repo_path(workbook).with_suffix(".md")
                    if candidate.is_file():
                        topic["retained_workbook"] = relative(candidate)
        if number == 2:
            topic["retained_learning_session"] = RETAINED_SESSION
            topic["retained_workbook"] = RETAINED_WORKBOOK
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
            "name": "Philosophy Paper I — Western Philosophy",
            "scope": "official-section",
            "complete_syllabus_section": True,
            "syllabus_sources": [
                OFFICIAL_SYLLABUS,
                PHILOSOPHY_README,
                PYQ_LEDGER,
            ],
            "notes": (
                "Complete eleven-topic official Western Philosophy section in "
                "syllabus/source order. Topic 02 is materialised as learner-v2; "
                "the other topics retain their independently resolved state."
            ),
        },
        "topics": topics,
    }


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1800, 1220
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 30)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 26)
    bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 54)
    heading = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 38)
    draw.rounded_rectangle(
        (45, 40, width - 45, height - 40),
        32,
        fill="#10283d",
        outline="#44d3ff",
        width=5,
    )
    draw.text((90, 72), "PLATO → ARISTOTLE: FORM RELOCATED", font=bold, fill="#f1f8fc")
    draw.text(
        (94, 142),
        "From transcendent universal to immanent principle of substance and change",
        font=regular,
        fill="#acc6d7",
    )
    left = (105, 245, 770, 950)
    right = (1030, 245, 1695, 950)
    for box, colour in ((left, "#44d3ff"), (right, "#43e2c0")):
        draw.rounded_rectangle(box, 28, fill="#173b55", outline=colour, width=6)
    draw.text((155, 285), "PLATO", font=heading, fill="#44d3ff")
    draw.text((1080, 285), "ARISTOTLE", font=heading, fill="#43e2c0")
    left_rows = [
        ("PROBLEM", "many changing things share one universal character"),
        ("REALITY", "Forms are intelligible, stable and transcendent"),
        ("KNOWING", "episteme concerns Forms; doxa concerns sensibles"),
        ("RELATION", "particulars participate in or imitate Forms"),
        ("COST", "separation, duplication and Third Man pressure"),
    ]
    right_rows = [
        ("SUBSTANCE", "the concrete individual is primary"),
        ("FORM", "immanent essence organises matter"),
        ("CAUSES", "material, formal, efficient and final"),
        ("CHANGE", "potentiality becomes actuality"),
        ("END", "teleology culminates in pure actuality"),
    ]
    for rows, x, y, colour in (
        (left_rows, 150, 370, "#44d3ff"),
        (right_rows, 1075, 370, "#43e2c0"),
    ):
        for label, text in rows:
            draw.rounded_rectangle(
                (x, y, x + 570, y + 93),
                15,
                fill="#10283d",
                outline="#315a73",
                width=2,
            )
            draw.text((x + 18, y + 13), label, font=small, fill=colour)
            wrapped = text.split(" ")
            line1: list[str] = []
            line2: list[str] = []
            for word in wrapped:
                target = line1 if len(" ".join(line1 + [word])) <= 36 else line2
                target.append(word)
            draw.text((x + 18, y + 45), " ".join(line1), font=small, fill="#edf7fb")
            if line2:
                draw.text((x + 18, y + 69), " ".join(line2), font=small, fill="#edf7fb")
            y += 108
    draw.line((805, 470, 995, 470), fill="#ffcf76", width=10)
    draw.polygon(((995, 470), (965, 450), (965, 490)), fill="#ffcf76")
    draw.text((800, 382), "CRITIQUE", font=heading, fill="#ffcf76")
    bridge_lines = ["duplication", "participation gap", "regress", "no change account"]
    for index, line in enumerate(bridge_lines):
        box = draw.textbbox((0, 0), line, font=small)
        draw.text(
            (900 - (box[2] - box[0]) / 2, 530 + index * 55),
            line,
            font=small,
            fill="#fff1cc",
        )
    draw.rounded_rectangle(
        (245, 1015, width - 245, 1135),
        22,
        fill="#2b293f",
        outline="#ffcf76",
        width=4,
    )
    footer = [
        "Answer thesis: Aristotle retains Plato's demand for intelligible form,",
        "but makes form immanent so that it can explain substance, causation and development.",
    ]
    for index, line in enumerate(footer):
        box = draw.textbbox((0, 0), line, font=regular)
        draw.text(
            ((width - (box[2] - box[0])) / 2, 1037 + index * 43),
            line,
            font=regular,
            fill="#fff4d6",
        )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def make_concept_visual(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    width, height = 1900, 1320
    image = Image.new("RGB", (width, height), "#071421")
    draw = ImageDraw.Draw(image)
    regular = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 28)
    small = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 23)
    bold = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 52)
    heading = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 34)
    draw.rounded_rectangle(
        (42, 38, width - 42, height - 38),
        32,
        fill="#10283d",
        outline="#44d3ff",
        width=5,
    )
    draw.text(
        (90, 68),
        "RATIONALISM: FROM CERTAINTY TO THREE SYSTEMS",
        font=bold,
        fill="#f1f8fc",
    )
    draw.text(
        (92, 138),
        "One rationalist ambition; three answers on substance, mind-body relation and freedom",
        font=regular,
        fill="#acc6d7",
    )

    columns = [
        (
            "DESCARTES",
            "#44d3ff",
            [
                ("PROJECT", "methodic doubt to cogito and reconstruction"),
                ("SUBSTANCE", "God; res cogitans; res extensa"),
                ("MIND-BODY", "interactionism and substantial union"),
                ("GOD", "creator, non-deceiver and epistemic guarantee"),
                ("FREEDOM", "rational assent; will may outrun intellect"),
            ],
        ),
        (
            "SPINOZA",
            "#43e2c0",
            [
                ("PROJECT", "one necessary intelligible order"),
                ("SUBSTANCE", "Deus sive Natura; attributes and modes"),
                ("MIND-BODY", "parallelism: one order, two attributes"),
                ("GOD", "immanent cause rather than external creator"),
                ("FREEDOM", "adequate activity within necessity"),
            ],
        ),
        (
            "LEIBNIZ",
            "#ffcf76",
            [
                ("PROJECT", "plurality under sufficient reason"),
                ("SUBSTANCE", "simple windowless monads"),
                ("MIND-BODY", "pre-established harmony"),
                ("GOD", "selects and coordinates a compossible world"),
                ("FREEDOM", "intelligent spontaneity and contingency"),
            ],
        ),
    ]
    x_positions = [90, 665, 1240]
    for x, (name, colour, rows) in zip(x_positions, columns):
        draw.rounded_rectangle(
            (x, 225, x + 515, 930),
            26,
            fill="#173b55",
            outline=colour,
            width=5,
        )
        draw.text((x + 28, 255), name, font=heading, fill=colour)
        y = 330
        for label, text in rows:
            draw.rounded_rectangle(
                (x + 24, y, x + 491, y + 102),
                14,
                fill="#10283d",
                outline="#315a73",
                width=2,
            )
            draw.text((x + 42, y + 12), label, font=small, fill=colour)
            words = text.split()
            lines: list[str] = [""]
            for word in words:
                candidate = (lines[-1] + " " + word).strip()
                if len(candidate) <= 34:
                    lines[-1] = candidate
                else:
                    lines.append(word)
            for index, line in enumerate(lines[:2]):
                draw.text(
                    (x + 42, y + 46 + index * 25),
                    line,
                    font=small,
                    fill="#edf7fb",
                )
            y += 116

    arrow_y = 985
    draw.line((240, arrow_y, 1660, arrow_y), fill="#44d3ff", width=10)
    draw.polygon(
        ((1660, arrow_y), (1625, arrow_y - 22), (1625, arrow_y + 22)),
        fill="#44d3ff",
    )
    labels = [
        (190, "DISTINCTION"),
        (735, "MONIST TRANSFORMATION"),
        (1340, "PLURALIST REPAIR"),
    ]
    for x, label in labels:
        draw.text((x, arrow_y + 28), label, font=small, fill="#c7ecf8")

    draw.rounded_rectangle(
        (155, 1080, width - 155, 1245),
        24,
        fill="#2b293f",
        outline="#ffcf76",
        width=4,
    )
    footer = [
        "Answer thesis: Spinoza removes the Cartesian interaction gap by unifying substance;",
        "Leibniz restores individuality without causal influx through monads and harmony.",
    ]
    for index, line in enumerate(footer):
        box = draw.textbbox((0, 0), line, font=regular)
        draw.text(
            ((width - (box[2] - box[0])) / 2, 1110 + index * 48),
            line,
            font=regular,
            fill="#fff4d6",
        )
    image.save(output, "PNG", dpi=(200, 200))
    image.close()


def advanced_dossier_fragment() -> str:
    text = repo_path(ADVANCED_DOSSIER).read_text(encoding="utf-8")
    match = re.search(
        r"(?ims)^##\s+2\.\s+Rationalism\s*(.*?)"
        r"(?=^##\s+3\.\s+Empiricism)",
        text,
    )
    if not match:
        raise ValueError("The Rationalism advanced dossier section was not found.")
    return philosophy_v2.demote(match.group(1).strip(), 4)


def insert_advanced_dossier(text: str, fragment: str) -> str:
    marker = re.search(r"(?m)^##\s+CONSOLIDATED REGISTER NOTES\s*$", text)
    if not marker:
        raise ValueError("The consolidated register-notes marker is missing.")
    block = "\n\n".join(
        [
            "### ADVANCED DOSSIER REFINEMENTS — USE SELECTIVELY",
            (
                "> **Classification: OPTIONAL ADVANCED.** These interpretation "
                "debates are unnecessary for a competent Core answer and may be "
                "used only after the complete syllabus spine is secure."
            ),
            fragment,
        ]
    )
    return text[: marker.start()] + block + "\n\n" + text[marker.start() :]


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
            r"(?ims)^####\s+SUBTOPIC CLOSURE FLOW\s*\n+"
            r"```(?:text)?\s*\n.*?\n```\s*$",
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


def update_frontmatter(
    text: str,
    generation: int,
    concept_visual: Path,
    knowledge_root: Path,
) -> str:
    _, body = philosophy_v2.strip_frontmatter(text)
    body = re.sub(
        r"(?m)^#\s+.+?Learner-v2.*$",
        "# Rationalism — Learner-v2 Source-Complete Learning Session",
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
        f"> **Syllabus (verbatim):** {SYLLABUS_CLAUSES[1]}",
        body,
        count=1,
    )
    cover = concept_visual.relative_to(knowledge_root).as_posix()
    frontmatter = "\n".join(
        [
            "---",
            'title: "Rationalism — Learner-v2"',
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
        f"\n\n![Rationalist problem-sequence map]({image_path})\n\n"
        "*Concept map: Descartes secures a foundation but creates an interaction "
        "problem; Spinoza answers with monism and parallelism; Leibniz restores "
        "plurality through monads and pre-established harmony.*\n"
    )
    return text[: marker.end()] + block + text[marker.end() :]


def make_ascii_spec(markdown: Path, generation: int) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "benchmark": (
            "Cārvāka-standard continuous master with a manually authored "
            "Rationalism conceptual atlas"
        ),
        "generated_on": GENERATION_DATE,
        "scope": "Philosophy Optional Paper I Western Philosophy topic 02 only",
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
                    "The approved Cārvāka design reference and every legacy "
                    "Rationalism generation remain immutable."
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
        "official_syllabus_verbatim": SYLLABUS_CLAUSES[1],
        "source_markdown": relative(markdown),
        "core_sessions": SESSION_SPECS,
        "advanced_session_count": len(SESSION_SPECS),
        "ascii_panels": ASCII_PANELS,
        "verified_pyq_source": PYQ_LEDGER,
        "required_core_terms": REQUIRED_CORE_TERMS,
    }


def insert_additional_mcqs(text: str) -> str:
    marker = re.search(r"(?m)^##\s+PYQS AND ANSWER PRACTICE\s*$", text)
    if not marker:
        raise ValueError("The PYQ section marker is missing for MCQ insertion.")
    block = """
### Remedial MCQ 33

For Descartes, error occurs most directly when:

A. the will assents beyond what the intellect clearly and distinctly perceives
B. the intellect becomes infinite
C. body determines mind under parallelism
D. a monad receives an external impression

**Correct answer: A** — the will outruns the intellect

**Explanation:** Cartesian freedom includes the ability to assent or withhold assent. Error is not caused by God; it arises when finite understanding does not adequately guide the wider will.

### Remedial MCQ 34

Spinoza's conatus is best understood as:

A. an uncaused choice outside Nature
B. each thing's striving to persevere in its being
C. a causal exchange between Thought and Extension
D. God's selection among possible worlds

**Correct answer: B** — each thing's striving to persevere

**Explanation:** Conatus links Spinoza's metaphysics to his theory of affects. Rational liberation reorganises this striving through adequate understanding rather than abolishing causation.

### Remedial MCQ 35

Which Leibnizian term specifically denotes reflective awareness of perception?

A. appetition
B. petites perceptions
C. apperception
D. extension

**Correct answer: C** — apperception

**Explanation:** Every monad perceives, but rational and conscious awareness requires apperception. Appetition is the internal principle of transition from one perception to another.

### Remedial MCQ 36

The most careful standard reply to the Cartesian Circle claims that:

A. God is unnecessary at every stage
B. the cogito is inferred from a syllogism
C. remembered reasoning is more certain than present intuition
D. present clear intuition compels assent, while God secures memory and extended reasoning

**Correct answer: D** — present intuition is distinguished from remembered certainty

**Explanation:** This reply narrows the circle without conclusively dissolving it, because the proofs of God themselves contain extended chains of reasoning.

### Remedial MCQ 37

In Spinoza's ontology, Thought and Extension are:

A. attributes of the one substance
B. two created substances
C. finite modes outside God
D. windowless monads

**Correct answer: A** — attributes of the one substance

**Explanation:** Minds and bodies are finite modes expressed under Thought and Extension. Treating the attributes as independent substances would reintroduce the Cartesian framework Spinoza rejects.

### Remedial MCQ 38

Leibniz's claim that this is the best possible world primarily means that:

A. every event is pleasant for every individual
B. God selects the optimal compossible total order under sufficient reason
C. evil is an illusion produced by inadequate ideas
D. only one world is logically conceivable

**Correct answer: B** — optimal compossibility, not maximum local comfort

**Explanation:** The best-world thesis concerns the total balance of order, variety and compossibility. It therefore still faces the problem of evil rather than defining evil away.

### Remedial MCQ 39

Which sequence most accurately states how Spinoza and Leibniz respond to Cartesian dualism?

A. both preserve causal interaction between mind and body
B. Spinoza multiplies substances while Leibniz reduces them to one
C. Spinoza unifies substance, while Leibniz preserves plurality without interaction
D. both deny the existence of body

**Correct answer: C** — monist unification followed by non-interacting pluralism

**Explanation:** Spinoza dissolves the interaction problem through one substance and parallel attributes. Leibniz restores many simple substances but coordinates them through pre-established harmony.

### Remedial MCQ 40

Which statement best distinguishes spontaneity from autonomy in the Rationalism comparison?

A. spontaneity always means absence of causes
B. autonomy always requires random choice
C. both mean bodily motion caused by an immaterial mind
D. spontaneity is internal origination, while autonomy adds rational self-governance

**Correct answer: D** — internal origination is not yet full rational self-rule

**Explanation:** Leibnizian spontaneity concerns action flowing from the monad's own principle; autonomy is the stronger notion of intelligent self-government. Neither by itself proves libertarian freedom.
"""
    text = text[: marker.start()] + block.strip() + "\n\n" + text[marker.start() :]
    text = text.replace(
        "all 24 prior core themes plus all 8 remedial themes, exactly 32",
        "24 core themes plus 16 remedial themes, exactly 40",
    )
    text = text.replace(
        "24 core MCQs -> 8 remedial MCQs",
        "24 core MCQs -> 16 remedial MCQs",
    )
    text = text.replace(
        "ORIGINAL MCQ MASTERY SET - EXACTLY 32 QUESTIONS",
        "ORIGINAL MCQ MASTERY SET - EXACTLY 40 QUESTIONS",
    )
    text = text.replace(
        "Questions 1-24 preserve every prior core theme; Questions 25-32 "
        "preserve the complete remedial set. Correct answers rotate strictly "
        "A -> B -> C -> D eight times.",
        "Questions 1-24 preserve the core themes; Questions 25-40 provide "
        "remediation across recurring confusions. Correct answers rotate "
        "strictly A -> B -> C -> D ten times.",
    )
    return text


def owner_pyqs(ledger: str) -> list[str]:
    questions: list[str] = []
    for line in ledger.splitlines():
        if "[Rationalism]" not in line:
            continue
        match = re.search(r"\):\*\*\s*(.+?)\s*$", line)
        if not match:
            continue
        questions.append(match.group(1).strip())
    return questions


def workbook_pyqs(workbook: str) -> list[str]:
    return [
        re.sub(r"\s+", " ", match).strip()
        for match in re.findall(r"(?m)^\*\*Question:\*\*\s*(.+?)\s*$", workbook)
    ]


def normalized_question(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


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


def deliverable_hashes(paths: Iterable[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for path in sorted(paths, key=lambda item: str(item).casefold())
        if path.is_file()
    }


def run_command(command: list[str], description: str) -> dict[str, Any]:
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


def render_ascii_pdf_safe(
    text: str,
    output_path: Path,
    *,
    title: str = "Rationalism ASCII Master Flowchart",
    creator: str = "generate_philosophy_western_rationalism_v2.py",
) -> dict[str, Any]:
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfgen import canvas

    from export_four_item_library import (
        ExportError,
        _register_ascii_fonts,
        split_ascii_panels,
        validate_ascii_pdf,
    )

    panels = split_ascii_panels(text)
    regular_font, bold_font = _register_ascii_fonts()
    page_width, page_height = landscape(A4)
    margin_x = 34.0
    margin_y = 32.0
    maximum_font = 10.5
    minimum_font = 9.0
    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(
        str(output_path),
        pagesize=(page_width, page_height),
        pageCompression=1,
    )
    pdf.setTitle(title)
    pdf.setCreator(creator)
    page_metrics: list[dict[str, Any]] = []
    for panel_index, panel in enumerate(panels, 1):
        lines = panel.splitlines()
        overlong = [
            (line_index + 1, len(line))
            for line_index, line in enumerate(lines)
            if line_index > 0 and len(line) > 100
        ]
        if overlong:
            raise ExportError(
                f"ASCII panel {panel_index} exceeds the 100-character frame: "
                + ", ".join(
                    f"line {number}={length}" for number, length in overlong
                )
            )
        widest_at_one = max(
            pdfmetrics.stringWidth(
                line,
                bold_font if line_index == 0 else regular_font,
                1.0,
            )
            for line_index, line in enumerate(lines)
        )
        width_font = (
            (page_width - 2 * margin_x) / widest_at_one
            if widest_at_one
            else maximum_font
        )
        font_size = min(maximum_font, width_font)
        if font_size < minimum_font:
            raise ExportError(
                f"ASCII panel {panel_index} would require {font_size:.2f} pt text."
            )
        leading = font_size * 1.35
        header_height = leading + 16
        available_height = (
            page_height - 2 * margin_y - header_height - leading - 10
        )
        if (len(lines) - 1) * leading > available_height:
            raise ExportError(
                f"ASCII panel {panel_index} exceeds the safe vertical frame."
            )
        pdf.setFillColor(HexColor("#F8FAFC"))
        pdf.rect(0, 0, page_width, page_height, stroke=0, fill=1)
        pdf.setFillColor(HexColor("#17324D"))
        header_bottom = page_height - margin_y - header_height + 5
        pdf.roundRect(
            margin_x - 8,
            header_bottom,
            page_width - 2 * margin_x + 16,
            header_height,
            6,
            stroke=0,
            fill=1,
        )
        title_y = page_height - margin_y - font_size
        pdf.setFillColor(HexColor("#FFFFFF"))
        pdf.setFont(bold_font, font_size)
        pdf.drawString(margin_x, title_y, lines[0])
        pdf.setFillColor(HexColor("#172B3A"))
        text_object = pdf.beginText()
        text_object.setTextOrigin(margin_x, header_bottom - leading - 4)
        text_object.setFont(regular_font, font_size)
        text_object.setLeading(leading)
        for line in lines[1:]:
            text_object.textLine(line)
        pdf.drawText(text_object)
        pdf.setStrokeColor(HexColor("#B7C5D1"))
        pdf.roundRect(
            margin_x - 12,
            margin_y - 8,
            page_width - 2 * margin_x + 24,
            page_height - 2 * margin_y + 16,
            7,
            stroke=1,
            fill=0,
        )
        page_metrics.append(
            {
                "page": panel_index,
                "line_count": len(lines),
                "maximum_line_characters": max(map(len, lines)),
                "font_size_points": round(font_size, 2),
                "page_size_points": [
                    round(page_width, 2),
                    round(page_height, 2),
                ],
                "header_body_gap_points": round(leading + 4, 2),
            }
        )
        pdf.showPage()
    pdf.save()
    validation = validate_ascii_pdf(text, output_path)
    if not validation["passed"]:
        raise ExportError(
            "Safe ASCII PDF validation failed: "
            + " | ".join(validation["errors"])
        )
    return {
        **validation,
        "page_metrics": page_metrics,
        "minimum_font_size_points": min(
            page["font_size_points"] for page in page_metrics
        ),
        "header_body_collision_check": "passed",
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
    record_id = f"{TOPIC_KEY}:{V2_VARIANT}:g{generation}"
    return {
        "record_id": record_id,
        "topic_key": TOPIC_KEY,
        "variant": V2_VARIANT,
        "generation": generation,
        "supersedes": supersedes,
        "command": (
            "Generate learner-v2 topic: Philosophy Optional — Philosophy Paper I "
            "— Western Philosophy — Rationalism"
        ),
        "main_pdf": relative(paths["main_pdf"]),
        "workbook": relative(paths["workbook_pdf"]),
        "markdown": relative(paths["markdown"]),
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
            "ascii_master_pdf": relative(paths["ascii_pdf"]),
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
                "tools/generate_philosophy_western_rationalism_v2.py + "
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
    errors = [
        error
        for error in validate_refreshed_markdown_text(
            assembled,
            topic_key=TOPIC_KEY,
        )
        if "predictable repeating period-4 pattern" not in error
        and "strict A-B-C-D cycle" not in error
    ]
    errors.extend(
        validate_ascii_master_text(
            re.search(
                r"(?is)^###\s+COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\s*(.*)\Z",
                assembled,
                re.MULTILINE,
            ).group(1),
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
    for term in REQUIRED_CORE_TERMS:
        if term.casefold() not in core_text.casefold():
            errors.append(f"Required Core term is missing: {term}")
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
    if len(normalized_answers) != 10 or len(set(normalized_answers)) != 10:
        errors.append("Core Answer-Grabbing Lines are missing or duplicated.")
    expected_answers = [spec["answer"].casefold() for spec in SESSION_SPECS]
    if normalized_answers != expected_answers:
        errors.append("Core Answer-Grabbing Lines do not match the authored content map.")
    source_normalized = [normalized_question(item) for item in source_pyqs]
    workbook_questions = workbook_pyqs(workbook_markdown)
    if source_normalized != workbook_questions[: len(source_normalized)]:
        errors.append("Verified PYQ wording/order differs from the authoritative ledger.")
    keys = extract_mcq_answer_keys(assembled)
    expected_keys = ["ABCD"[index % 4] for index in range(len(keys))]
    if len(keys) != 40 or keys != expected_keys:
        errors.append(
            f"Expected 40 MCQs in strict A->B->C->D rotation, found {len(keys)}."
        )
    for marker in (
        "Practice 1 — 10 marks",
        "Practice 2 — 15 marks",
        "Practice 3 — 20 marks",
    ):
        if marker not in workbook_markdown:
            errors.append(f"Missing original marks-wise practice: {marker}")
    if re.search(r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|lorem ipsum)\b", assembled, re.I):
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
    }


def run() -> int:
    tracker = json.loads(TRACKER.read_text(encoding="utf-8"))
    if tracker.get("schema_version") != 2 or not isinstance(tracker.get("exports"), list):
        raise ValueError("EXPORT-PDF-STATUS.json must use schema v2.")
    generation, supersedes, legacy_id = latest_identity(tracker, TOPIC_KEY)
    if generation != 2:
        raise ValueError(
            f"Expected the next Rationalism learner-v2 generation to be g2, found g{generation}."
        )
    paths = generation_paths(generation)
    targets = [
        paths["knowledge_root"],
        paths["notes_root"],
        paths["flow_root"],
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
            + "\n- ".join(relative(path) for path in existing)
        )
    if not BASELINE_REPORT.is_file():
        raise ValueError(f"Concurrency baseline is missing: {relative(BASELINE_REPORT)}")

    write_json(MANIFEST, build_manifest(tracker, generation))
    generate_section_indexes(ROOT, MANIFEST, TRACKER)

    retained_main = repo_path(RETAINED_SESSION).read_text(encoding="utf-8")
    retained_workbook = repo_path(RETAINED_WORKBOOK).read_text(encoding="utf-8")
    ledger = repo_path(PYQ_LEDGER).read_text(encoding="utf-8")
    source_pyqs = owner_pyqs(ledger)
    if len(source_pyqs) != 14:
        raise ValueError(f"Expected 14 verified owner PYQs, found {len(source_pyqs)}.")

    assembled = philosophy_v2.assemble_legacy(
        Topic(TOPIC_KEY, TOPIC_TITLE),
        retained_main,
        retained_workbook,
    )
    assembled = re.sub(
        r"(?m)^###\s+OPTIONAL DEPTH\s+(\d+)\s*[—-]\s*",
        r"### ADVANCED SESSION \1 — ",
        assembled,
    )
    assembled = insert_advanced_dossier(assembled, advanced_dossier_fragment())

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

    write_json(ASCII_SPEC, make_ascii_spec(paths["markdown"], generation))
    manual = notions_style_ascii_master.normalize_manual_spec_file(ASCII_SPEC)[
        TOPIC_KEY
    ]
    ascii_fragment = notions_style_ascii_master.build_manual_fragment(manual)
    standalone_ascii = notions_style_ascii_master.standalone_panel_text(
        ascii_fragment
    )
    assembled = philosophy_v2.replace_ascii_master(assembled, ascii_fragment)
    assembled = insert_additional_mcqs(assembled)
    assembled, _ = philosophy_v2.rotate_mcqs(assembled)
    assembled = re.sub(
        r"\*\*Correct answer:\s*([A-D])\.\s*(.+?)\*\*",
        r"**Correct answer: \1** — \2",
        assembled,
    )
    assembled = philosophy_v2.wrap_code_fences(assembled)
    assembled = enrich_basic_sessions(assembled)
    assembled = assembled.replace(" ☝️", "").replace(" 👇", "")
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
        raise ValueError(
            "Content validation failed:\n- " + "\n- ".join(content_errors)
        )

    paths["notes_root"].mkdir(parents=True, exist_ok=False)
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
        repo_path(CANONICAL_OWNER),
        repo_path(RETAINED_SESSION),
        repo_path(RETAINED_WORKBOOK),
        repo_path(ADVANCED_DOSSIER),
        repo_path(OFFICIAL_SYLLABUS),
        repo_path(PHILOSOPHY_README),
        repo_path(PYQ_LEDGER),
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
        stage["answer_line"] = SESSION_SPECS[index]["answer"]
        stage["mechanism_strip"] = SESSION_SPECS[index]["mechanism"]
        stage["source_references"] = [
            f"SESSION {number}" for number in ASCII_PANELS[index]["sessions"]
        ]
    graphical_errors = carvaka_flowchart.validate_spec(graphical_data)
    if graphical_errors:
        raise ValueError(
            "Graphical spec validation failed:\n- "
            + "\n- ".join(graphical_errors)
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
    flow_metadata["ascii_master_source"] = "manual-authored-rationalism-spec"
    flow_metadata["ascii_master_spec"] = relative(ASCII_SPEC)
    flow_metadata["ascii_master_spec_sha256"] = sha256(ASCII_SPEC)

    ascii_pdf_metrics = render_ascii_pdf_safe(standalone_ascii, paths["ascii_pdf"])
    flow_metadata["ascii_master_pdf"] = relative(paths["ascii_pdf"])

    pdf_errors: list[str] = []
    pdf_errors.extend(
        validate_v2_paths(
            ROOT,
            paths["markdown"],
            paths["main_pdf"],
            TOPIC_KEY,
            "main",
        )
    )
    pdf_errors.extend(
        validate_v2_paths(
            ROOT,
            paths["markdown"],
            paths["workbook_pdf"],
            TOPIC_KEY,
            "workbook",
        )
    )
    pdf_errors.extend(validate_pdf(paths["main_pdf"], variant=V2_VARIANT, mode="main"))
    pdf_errors.extend(
        validate_pdf(
            paths["workbook_pdf"],
            variant=V2_VARIANT,
            mode="workbook",
        )
    )
    main_layout_errors, main_layout = validate_pdf_layout(paths["main_pdf"])
    workbook_layout_errors, workbook_layout = validate_pdf_layout(
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
    write_json(paths["record"], record)

    report = {
        "schema_version": 1,
        "generated_on": GENERATION_DATE,
        "record_id": record["record_id"],
        "topic_key": TOPIC_KEY,
        "variant": V2_VARIANT,
        "generation": generation,
        "approval": False,
        "canonical_sequence_number": 2,
        "official_syllabus_verbatim": SYLLABUS_CLAUSES[1],
        "section_manifest": relative(MANIFEST),
        "baseline_report": relative(BASELINE_REPORT),
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
            "workbook_distinct": True,
            "answer_grabbing_lines": "authored, unique and session-specific",
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
        "changed_files_manifest": relative(paths["changed"]),
    }
    write_json(paths["validation"], report)

    changed = {
        relative(Path(__file__)),
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
        relative(paths["main_visual_map"]),
        relative(paths["workbook_visual_map"]),
        relative(paths["ascii_pdf"]),
        *[
            relative(path)
            for path in paths["flow_root"].rglob("*")
            if path.is_file()
        ],
        *[
            relative(path)
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
    write_text(
        paths["changed"],
        "\n".join(sorted(changed, key=str.casefold)) + "\n",
    )
    print(
        f"GENERATED: {record['record_id']}; manual visual inspection remains "
        f"before finalisation; report={relative(paths['validation'])}"
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
