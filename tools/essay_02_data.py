"""Authored learner-v2 data for Essay Topic 02."""

from __future__ import annotations

import generate_essay_common as common


LIVE_ATTEMPTS = [
    (
        "https://upsc.gov.in/examinations/previous-question-papers — attempted "
        "2026-09-04; the official page was access-blocked, so exact prompt "
        "wording continues to come only from the repository's V1 paper audit."
    ),
    (
        "https://upsc.gov.in/examinations/active-examinations — attempted "
        "2026-09-04; the official page was access-blocked and supplied no "
        "attribution, interpretation or current paper instruction."
    ),
    (
        "https://upsc.gov.in/sites/default/files/Notif-CSP-2024-Engl-140224.pdf "
        "— searched 2026-09-04; the official notification route was logged but "
        "was not used to attach authors or canonical meanings to prompts."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Free-standing proposition", "An unattributed philosophical prompt is treated as a proposition to interpret on its own words, not as a quotation-recall test."),
        ("Content-word inventory", "Decoding begins by identifying every content word and stating its plain meaning before extending the sentence."),
        ("Relation or operator", "The prompt's operative relation may be causal, comparative, conditional, definitional, paradoxical or process-versus-outcome."),
        ("Literal layer", "The literal layer records what the sentence says before metaphorical extension and prevents the essay from losing textual contact."),
        ("Metaphorical layer", "A metaphor-carrying aphorism requires separating the image or vehicle from the idea or tenor it is used to illuminate."),
        ("Normative layer", "The normative layer asks what value, standard, duty or conception of a good life the proposition appears to affirm or question."),
        ("Operative tension", "A usable decoding names the opposition or double pull inside the whole sentence, rather than writing generally on one keyword."),
        ("Paradox", "An apparent contradiction may disclose a deeper relationship, but it must be explained rather than admired as clever wording."),
        ("Scope", "The interpretation should state whether the claim operates at individual, institutional, state, global or civilisational scale and where it does not."),
        ("Hidden assumption", "A compressed proposition normally relies on an unstated premise that must be surfaced and tested before becoming a thesis."),
        ("Exception", "Universal wording is usually handled as a strong tendency with a defensible exception, not as an absolute law or an empty truism."),
        ("Counter-reading", "A serious alternative reading tests whether the preferred interpretation is textually faithful and more generative than its rival."),
        ("Thesis alternatives", "Drafting two or three possible theses exposes interpretive choice and prevents premature commitment to the first metaphorical association."),
        ("Mechanism", "The decoded relation needs a conceptual or causal mechanism explaining how one term bears on the other."),
        ("Scale test", "A reading should be tested across scales and retained only where the prompt's own language can sustain the extension."),
        ("Examples", "Examples should instantiate the decoded claim at a chosen scale; they do not substitute for explaining the relation."),
        ("Counterexamples", "A counterexample identifies a limit or condition and should qualify the claim without replacing it with the opposite thesis."),
        ("Feedback", "Where relevant, trace whether the consequence loops back to reinforce, correct or transform the starting condition."),
        ("Attribution firewall", "Do not invent author attribution, a source text or intellectual biography when the paper prints none; prompt wording is sufficient warrant."),
        ("Printing-defect firewall", "Reproduce a V1 prompt as printed but interpret its evident sense; a typographical defect is not a secret philosophical signal."),
    ]
    traps = [
        "Do not write an essay on one attractive keyword while ignoring the relation asserted by the sentence.",
        "Do not jump from a literal phrase to an unrelated grand theme.",
        "Do not treat metaphorical, normative and empirical layers as interchangeable.",
        "Do not mistake paradox-recognition for completed analysis.",
        "Do not universalise a reading that survives only at one scale.",
        "Do not let an exception swallow the central proposition.",
        "Do not accept the first interpretation without a counter-reading.",
        "Do not use examples as decoration or proof by anecdote.",
        "Do not invent attribution, biography or contextual intent.",
        "Do not build meaning from an audited printing defect.",
    ]
    titles = [
        "Free-standing proposition and content words",
        "Relation and operator types",
        "Literal layer before extension",
        "Metaphor vehicle and tenor",
        "Normative layer and value claim",
        "Operative tension and paradox",
        "Scope across levels",
        "Hidden assumption",
        "Exception and qualification",
        "Counter-reading test",
        "Thesis alternatives and mechanism",
        "Scale test",
        "Examples as claim tests",
        "Counterexamples and feedback",
        "Attribution and printing-defect firewalls",
    ]
    routes = [
        "Begin with the printed proposition, not a remembered author.",
        "Define the sentence's own terms before importing themes.",
        "State exactly what relation the sentence asserts.",
        "Use the literal meaning as a continuing anchor.",
        "Separate the metaphor's image from its argued subject.",
        "Name the value judgment without turning it into moralising.",
        "Turn the sentence into a contestable tension.",
        "Explain why the apparent contradiction is analytically useful.",
        "Extend only to scales the wording can support.",
        "Make the premise visible and test it.",
        "Qualify universal language without dissolving it.",
        "Prefer the reading that is faithful, defensible and generative.",
        "Compare thesis options before choosing one.",
        "Use cases and counter-cases to test mechanism and limits.",
        "Quote exactly while refusing invented context.",
    ]
    panels = [
        common.panel("Decoding start", "process-flow", [
            "PRINTED PROMPT",
            "CONTENT WORDS -> PLAIN MEANINGS",
            "RELATION OR OPERATOR",
            "WORKING PROPOSITION",
        ], ["Free-standing proposition", "Content-word inventory", "Relation or operator"]),
        common.panel("Three-layer reading", "hierarchy", [
            "LITERAL -> what the sentence directly says",
            "METAPHORICAL -> what the image carries",
            "NORMATIVE -> what value or standard is implied",
            "RULE -> layers must remain connected",
        ], ["Literal layer", "Metaphorical layer", "Normative layer"]),
        common.panel("Operator matrix", "matrix", [
            "CAUSAL -> X produces Y",
            "COMPARATIVE -> X matters more or less than Y",
            "DEFINITIONAL -> X is the meaning of Y",
            "PARADOXICAL -> surface conflict reveals a deeper relation",
        ], ["Relation or operator", "Paradox"]),
        common.panel("Metaphor bridge", "comparison-table", [
            "VEHICLE -> image named in the sentence",
            "TENOR -> subject illuminated by the image",
            "BRIDGE -> shared structure or mechanism",
            "LIMIT -> no extension without textual support",
        ], ["Metaphorical layer", "Mechanism"]),
        common.panel("Tension engine", "dialectic", [
            "TERM A -> pressure or value",
            "TERM B -> rival pressure or value",
            "TENSION -> neither side is merely decorative",
            "SYNTHESIS -> condition under which each insight holds",
        ], ["Operative tension", "Normative layer"]),
        common.panel("Scope ladder", "status-ladder", [
            "INDIVIDUAL -> conduct and experience",
            "INSTITUTION -> incentives and rules",
            "STATE OR WORLD -> policy and order",
            "CIVILISATION -> long-run pattern",
        ], ["Scope", "Scale test"]),
        common.panel("Assumption test", "decision-tree", [
            "CLAIM -> what is asserted",
            "ASSUMPTION -> what must be true",
            "SCOPE -> where it plausibly holds",
            "EXCEPTION -> what limits it",
        ], ["Hidden assumption", "Scope", "Exception"]),
        common.panel("Counter-reading test", "comparison-table", [
            "READING ONE -> faithful and generative?",
            "READING TWO -> faithful and generative?",
            "COMPARE -> mechanism, scope and exception",
            "CHOOSE -> stronger text-bound interpretation",
        ], ["Counter-reading", "Mechanism", "Scale test"]),
        common.panel("Thesis alternatives", "branch-map", [
            "DECODED TENSION",
            "BRANCH A -> thesis with one mechanism",
            "BRANCH B -> thesis with another mechanism",
            "SELECT -> defensible claim with explicit qualification",
        ], ["Thesis alternatives", "Mechanism", "Exception"]),
        common.panel("Case testing", "feedback-loop", [
            "EXAMPLE -> instantiates the claim",
            "COUNTEREXAMPLE -> exposes a limit",
            "FEEDBACK -> consequence changes the starting condition",
            "REVISION -> refine scope or mechanism",
        ], ["Examples", "Counterexamples", "Feedback"]),
        common.panel("Attribution firewall", "firewall", [
            "PAPER PRINTS NO AUTHOR -> do not supply one",
            "NO BIOGRAPHY -> no intent can be inferred",
            "PROMPT WORDING -> sufficient interpretive anchor",
            "PRIMARY CHECK -> required before any attribution",
        ], ["Attribution firewall", "Free-standing proposition"]),
        common.panel("Decoding answer spine", "answer-spine", [
            "WORDS -> OPERATOR -> LITERAL LAYER",
            "METAPHOR OR NORMATIVE LAYER -> TENSION",
            "SCOPE -> ASSUMPTION -> EXCEPTION",
            "COUNTER-READING -> THESIS OPTIONS -> CASE TEST",
        ], ["Content-word inventory", "Relation or operator", "Printing-defect firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2024-A3", "Essay",
            "There is no path to happiness, Happiness is the path.",
            "Exact V1 wording, including the printed comma and capitalised second Happiness.",
            [1, 2, 3, 6, 9, 10, 12, 19],
        ),
        common.make_pyq_solution(
            facts, "2025-B5", "Essay",
            "Muddy water is best cleared by leaving it alone.",
            "Exact V1 wording; the card decodes restraint versus intervention without claiming one official reading.",
            [3, 4, 6, 8, 11, 13, 16],
        ),
        common.make_pyq_solution(
            facts, "2024-B6", "Essay",
            "Nearly all men can stand adversity, but to test the character, give him power.",
            "Exact V1 wording; no author is attached because the paper prints none.",
            [0, 2, 5, 6, 9, 10, 14, 18],
        ),
    ]
    return common.topic(
        2,
        "Philosophical Quote Decoding",
        "02_Philosophical-Quote-Decoding",
        facts,
        traps,
        [
            (10, "Distinguish literal, metaphorical and normative layers in philosophical prompts.", [3, 4, 5]),
            (10, "Explain the role of relation or operator in decoding an aphorism.", [1, 2, 6]),
            (15, "Show how scope, assumption and exception convert a universal prompt into a defensible reading.", [8, 9, 10, 14]),
            (15, "Design a counter-reading test for selecting among thesis alternatives.", [11, 12, 13, 16]),
            (20, "Decode one paradoxical prompt from literal wording to a qualified working thesis.", [1, 2, 3, 6, 7, 9, 10, 12]),
            (20, "Examine how examples, counterexamples and feedback loops test a philosophical interpretation.", [13, 14, 15, 16, 17]),
        ],
        titles,
        routes,
        panels,
        [
            "Literal meaning", "Operative tension", "Scope of the claim",
            "Metaphor-carrying aphorism", "Comparative aphorism",
            "Definitional aphorism", "hidden assumption",
            "counterfactual test", "author attribution",
        ],
        "The three cards use exact V1 prompt wording from 2024–2025 and provide method-focused decoding only. No official model answer, author or unique canonical interpretation is claimed.",
        pyqs,
        LIVE_ATTEMPTS,
        "Official UPSC pages were attempted on 2026-09-04 only to locate paper and notification routes. Exact wording remains controlled by the repository's local V1 audit, and no web attribution or biography was imported.",
        extra=[
            "00_Master-Framework.md",
            "README.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
            "PYQ-Corpus-2013-2025.md",
        ],
        register_headings=(
            "WORD, OPERATOR AND THREE-LAYER DECODING MAP",
            "SCOPE, ASSUMPTION, EXCEPTION AND ATTRIBUTION FIREWALLS",
            "COUNTER-READING TO WORKING-THESIS SPINE",
            "V1 WORDING AND OFFICIAL-SOURCE LIMIT",
        ),
        register_answer_spine=[
            "COPY THE PROMPT WORDING ACCURATELY",
            "DEFINE CONTENT WORDS AND RELATION",
            "STATE LITERAL METAPHORICAL AND NORMATIVE LAYERS",
            "NAME THE OPERATIVE TENSION",
            "TEST SCALE ASSUMPTION AND EXCEPTION",
            "COMPARE THESIS ALTERNATIVES",
            "USE EXAMPLE COUNTEREXAMPLE AND QUALIFIED SYNTHESIS",
        ],
    )


TOPIC_02 = _build()
