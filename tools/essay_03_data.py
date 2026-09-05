"""Authored learner-v2 data for Essay Topic 03."""

from __future__ import annotations

import generate_essay_common as common


LIVE_ATTEMPTS = [
    (
        "https://upsc.gov.in/examinations/previous-question-papers — attempted "
        "2026-09-04; the official index was access-blocked, so the module uses "
        "only locally audited V1 wording for issue-prompt cards."
    ),
    (
        "https://upsc.gov.in/examinations/active-examinations — attempted "
        "2026-09-04; the official page was access-blocked and supplied no "
        "current issue-prompt taxonomy or model-answer claim."
    ),
    (
        "https://upsc.gov.in/sites/default/files/Notif-CSP-2024-Engl-140224.pdf "
        "— searched 2026-09-04; the official notification route was logged only "
        "for scheme provenance, not for coaching-style scoping rules."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Issue-statement prompt", "An issue prompt names a real phenomenon and makes a causal, comparative, interrogative or evaluative claim that can be contested without first decoding a dominant metaphor."),
        ("Classification gate", "A prompt is scoped as an issue when it names a concrete phenomenon, asserts something about it and already yields a literal contestable proposition."),
        ("Directive or demand", "Identify whether the wording asks a question, presents alternatives, asserts causation or makes a value judgment; that demand governs the essay's argumentative burden."),
        ("Object", "The object is the precise phenomenon or relationship being examined, not the entire GS subject area surrounding it."),
        ("Qualifier", "Words such as Indian, majority, youth, real, complex, alternative or better narrow the claim and must survive in the thesis."),
        ("Geography", "State whether the prompt is bounded to India, South Asia, another named region or a wider frame; do not globalise or nationalise it automatically."),
        ("Time", "Distinguish a present condition, historical change, future possibility or long-run consequence when the wording supports that temporal boundary."),
        ("Actor", "Identify who acts, experiences, decides, benefits or bears cost, and do not treat a broad group such as youth or farmers as homogeneous."),
        ("Scale", "Locate the demand at individual, community, institutional, state, regional or global scale before importing examples from another level."),
        ("Causal demand", "Where the prompt asserts causation, test each link through mechanism, evidence, mediator and limit instead of merely repeating the causal words."),
        ("Evaluative demand", "Where the prompt uses judgment terms such as threat, anomaly, myth, reality or complex, define the standard by which the judgment will be assessed."),
        ("Hidden tension", "Issue prompts normally contain a trade-off or double effect that must be made explicit, such as connection versus isolation or automation versus reskilling."),
        ("Excluded material", "Write a negative boundary naming adjacent content that will not enter unless it directly advances the exact prompt."),
        ("Definition boundary", "Define only the terms needed to fix the proposition; a long textbook background section expands the topic before the thesis is secure."),
        ("Thesis boundary", "The thesis must answer the prompt's exact causal or evaluative claim with stated conditions, not announce that the issue has both advantages and disadvantages."),
        ("Scope creep", "Scope creep occurs when the response becomes a general survey of the domain instead of testing the prompt's specified relationship."),
        ("GS-answer collapse", "A causes-effects-measures or scheme catalogue does not by itself create a sustained Essay argument, even when every listed fact is accurate."),
        ("Policy-catalogue avoidance", "Policies and institutions should appear as evidence for a claim, mechanism or synthesis, never as an isolated inventory of government action."),
        ("Counter-case", "The strongest rival or beneficial effect should be stated fairly and used to qualify the thesis rather than appended as token balance."),
        ("Synthesis", "A good issue essay resolves the tension by distributing responsibility, specifying conditions and connecting feasible institutional action with agency and values."),
    ]
    traps = [
        "Do not scope a metaphor-heavy hybrid as a literal issue statement before decoding it.",
        "Do not ignore interrogative, causal, comparative or evaluative wording.",
        "Do not drop qualifiers such as India, youth, majority or long run.",
        "Do not shift geography, actor, time or scale without explaining the move.",
        "Do not present association as causation without a mechanism and mediator.",
        "Do not define the whole subject when only one relationship is contested.",
        "Do not convert the essay into a scheme or policy catalogue.",
        "Do not treat a broad social group as internally uniform.",
        "Do not add a token counterpoint after a one-sided essay.",
        "Do not end with generic balance; state the conditions of synthesis.",
    ]
    titles = [
        "Issue-prompt classification",
        "Directive and demand",
        "Object boundary",
        "Qualifier boundary",
        "Geography boundary",
        "Time and actor boundary",
        "Scale boundary",
        "Causal demand",
        "Evaluative demand",
        "Hidden tension",
        "Excluded material and definition boundary",
        "Thesis boundary",
        "Scope-creep diagnosis",
        "GS-answer and policy-catalogue avoidance",
        "Counter-case and condition-based synthesis",
    ]
    routes = [
        "Classify before deciding whether to decode or scope first.",
        "Turn the wording into the exact burden the essay must discharge.",
        "Carry the object and every important qualifier into the thesis.",
        "Fix where and when the claim applies.",
        "Disaggregate actors and match evidence to scale.",
        "Test every causal link through mechanism and limit.",
        "State the criterion behind evaluative words.",
        "Name the trade-off the proposition compresses.",
        "Exclude adjacent GS content before it creates drift.",
        "Define only what the argument needs.",
        "Answer the exact claim with conditions.",
        "Run a relevance sweep against the printed proposition.",
        "Use policies as functional evidence, never as a list.",
        "Give the strongest rival case full argumentative force.",
        "Resolve through responsibilities, conditions and feasible action.",
    ]
    panels = [
        common.panel("Issue classification gate", "decision-tree", [
            "CONCRETE PHENOMENON NAMED?",
            "CAUSAL OR EVALUATIVE CLAIM PRESENT?",
            "LITERAL READING ALREADY CONTESTABLE?",
            "YES -> SCOPE | NO -> DECODE FIRST",
        ], ["Issue-statement prompt", "Classification gate"]),
        common.panel("Demand types", "matrix", [
            "QUESTION -> judgment required",
            "ALTERNATIVES -> compare and qualify",
            "CAUSAL ASSERTION -> test links",
            "VALUE CLAIM -> define evaluative standard",
        ], ["Directive or demand", "Causal demand", "Evaluative demand"]),
        common.panel("Object-qualifier lock", "firewall", [
            "OBJECT -> exact phenomenon or relationship",
            "QUALIFIER -> named population, place or judgment",
            "THESIS -> must preserve both",
            "DRIFT -> adjacent subject matter without argumentative function",
        ], ["Object", "Qualifier", "Thesis boundary"]),
        common.panel("Scope coordinates", "spatial-map", [
            "WHERE -> geography",
            "WHEN -> time horizon",
            "WHO -> actor",
            "AT WHAT LEVEL -> scale",
        ], ["Geography", "Time", "Actor", "Scale"]),
        common.panel("Causal chain test", "causal-chain", [
            "ASSERTED CAUSE",
            "MECHANISM -> EVIDENCE",
            "MEDIATOR OR FEEDBACK",
            "LIMIT -> QUALIFIED EFFECT",
        ], ["Causal demand", "Hidden tension"]),
        common.panel("Evaluative standard", "comparison-table", [
            "PROMPT WORD -> threat, anomaly, myth or complex",
            "STANDARD -> what would make the judgment true",
            "EVIDENCE -> cases supporting or weakening it",
            "VERDICT -> graded rather than absolute",
        ], ["Evaluative demand", "Thesis boundary"]),
        common.panel("Hidden-tension map", "dialectic", [
            "PROMISED BENEFIT",
            "OBSERVED OR ASSERTED COST",
            "CONDITIONS ALTERING THE BALANCE",
            "SYNTHESIS -> responsibility across actors",
        ], ["Hidden tension", "Counter-case", "Synthesis"]),
        common.panel("Exclusion box", "boundary-map", [
            "IN -> material proving the exact relationship",
            "OUT -> generic history of the whole domain",
            "OUT -> unrelated schemes and statistics",
            "RE-ENTRY -> only with a clear argumentative function",
        ], ["Excluded material", "Policy-catalogue avoidance"]),
        common.panel("Definition-to-thesis bridge", "process-flow", [
            "DEFINE NECESSARY TERMS",
            "STATE OBJECT AND QUALIFIERS",
            "NAME CAUSAL OR EVALUATIVE BURDEN",
            "WRITE CONDITIONAL THESIS",
        ], ["Definition boundary", "Thesis boundary", "Directive or demand"]),
        common.panel("GS-collapse warning", "comparison-table", [
            "GS LIST -> causes, effects, schemes",
            "ESSAY MOVE -> claim, mechanism, counter-case",
            "GS LIST -> parallel headings",
            "ESSAY MOVE -> connected paragraph argument",
        ], ["GS-answer collapse", "Policy-catalogue avoidance"]),
        common.panel("Counter-case to synthesis", "feedback-loop", [
            "THESIS -> strongest supporting mechanism",
            "COUNTER-CASE -> rival effect or limit",
            "CONDITION -> when each side dominates",
            "SYNTHESIS -> distributed responsibility and feasible action",
        ], ["Counter-case", "Synthesis"]),
        common.panel("Scoping answer spine", "answer-spine", [
            "CLASSIFY -> DEMAND -> OBJECT -> QUALIFIER",
            "GEOGRAPHY -> TIME -> ACTOR -> SCALE",
            "MECHANISM -> TENSION -> EXCLUSIONS",
            "THESIS -> COUNTER-CASE -> SYNTHESIS",
        ], ["Classification gate", "Scope creep", "Synthesis"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018-A1", "Essay",
            "Alternative technologies for a climate change resilient India.",
            "Exact V1 wording from the local official paper; used to scope object, qualifier and India boundary.",
            [2, 3, 4, 5, 8, 10, 12, 14],
        ),
        common.make_pyq_solution(
            facts, "2019-B7", "Essay",
            "Biased media is a real threat to Indian democracy.",
            "Exact V1 wording; used to expose the evaluative standards behind real threat and Indian democracy.",
            [2, 3, 4, 5, 10, 11, 14, 18],
        ),
        common.make_pyq_solution(
            facts, "2024-B5", "Essay",
            "Social media is triggering 'Fear of Missing Out' amongst the youth precipitating depression and loneliness.",
            "Exact V1 wording, including the missing comma before precipitating; used for a causal-chain scoping application.",
            [3, 4, 7, 9, 11, 14, 18, 19],
        ),
    ]
    return common.topic(
        3,
        "Issue-Based Prompt Scoping",
        "03_Issue-Based-Prompt-Scoping",
        facts,
        traps,
        [
            (10, "Distinguish issue-prompt scoping from philosophical decoding.", [0, 1, 2]),
            (10, "Build an object-qualifier-geography-time-actor-scale scope map.", [3, 4, 5, 6, 7, 8]),
            (15, "Explain how causal and evaluative demands require different argument tests.", [9, 10, 11]),
            (15, "Show how excluded material and thesis boundaries prevent scope creep.", [12, 13, 14, 15]),
            (20, "Analyse why a policy catalogue or GS-answer structure cannot substitute for an issue essay.", [14, 15, 16, 17, 18, 19]),
            (20, "Apply the complete scoping method to one verified issue prompt.", [2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "issue-statement prompt", "scope creep", "GS-answer collapse",
            "causal", "evaluative", "mechanism", "youth",
            "continuous argued essay",
        ],
        "The cards preserve exact V1 issue or issue-adjacent prompts from 2018, 2019 and 2024. The solutions demonstrate scope control and do not claim official model essays.",
        pyqs,
        LIVE_ATTEMPTS,
        "The 2026-09-04 official-site attempts supplied no new content. Prompt wording and metadata remain bounded by local V1 papers and the audited Essay corpus; issue analysis is explicitly repository-authored method.",
        extra=[
            "00_Master-Framework.md",
            "README.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
            "PYQ-Corpus-2013-2025.md",
        ],
        register_headings=(
            "DEMAND, OBJECT AND QUALIFIER SCOPE MAP",
            "GEOGRAPHY, TIME, ACTOR, SCALE AND EXCLUSION FIREWALLS",
            "CAUSAL OR EVALUATIVE THESIS-TO-SYNTHESIS SPINE",
            "V1 ISSUE-PROMPT WORDING AND LIVE-SOURCE BOUNDARY",
        ),
        register_answer_spine=[
            "CLASSIFY THE PROMPT",
            "IDENTIFY DIRECTIVE OR ASSERTED DEMAND",
            "LOCK OBJECT QUALIFIER GEOGRAPHY TIME ACTOR AND SCALE",
            "TEST CAUSAL LINKS OR EVALUATIVE STANDARD",
            "NAME HIDDEN TENSION AND EXCLUDED MATERIAL",
            "WRITE A CONDITIONAL THESIS",
            "COUNTER-CASE THEN SYNTHESIS WITHOUT POLICY CATALOGUE",
        ],
    )


TOPIC_03 = _build()
