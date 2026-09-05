"""Authored learner-v2 data for Essay Topic 04."""

from __future__ import annotations

import generate_essay_common as common


LIVE_ATTEMPTS = [
    (
        "https://upsc.gov.in/examinations/previous-question-papers — attempted "
        "2026-09-04; the official index was access-blocked, so only locally "
        "audited V1 prompts are used in the application cards."
    ),
    (
        "https://upsc.gov.in/examinations/active-examinations — attempted "
        "2026-09-04; the official page was access-blocked and supplied no "
        "official dimension count, brainstorming template or paragraph rule."
    ),
    (
        "https://upsc.gov.in/sites/default/files/Notif-CSP-2024-Engl-140224.pdf "
        "— searched 2026-09-04; the official notification route was recorded "
        "only to preserve the scheme boundary, not to validate any framework."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Divergent pass", "Begin by generating a broad pool of possible claims without yet deciding paragraph order, so early preference does not suppress a useful dimension."),
        ("Actor axis", "Search across individual, family, community, institution, state and world actors, but keep only levels that change the claim or mechanism."),
        ("Scale axis", "Test local, regional, national, global and civilisational scales without assuming that the same proposition operates identically at each level."),
        ("Time axis", "Historical origin, present manifestation and plausible future trajectory are prompts for inquiry, not mandatory sections."),
        ("Domain axis", "Material, political, economic, social, ethical, technological, ecological and cultural lenses are a search field, not a checklist."),
        ("Causality axis", "Generate immediate causes, structural causes, consequences, feedback loops and response choices where the decoded proposition supports them."),
        ("Distribution axis", "Ask who gains, loses, decides, bears cost or remains invisible; a distributional claim must still connect to the central proposition."),
        ("Direction axis", "Test intended benefits, unintended consequences and double effects rather than assuming every dimension moves in one direction."),
        ("PESTLE boundary", "PESTLE or a comparable framework may jog recall, but it is not a compulsory Essay template and should disappear once prompt-specific claims emerge."),
        ("Cause-impact-response boundary", "Cause-impact-response can organise an issue prompt, but each part must serve one thesis and must not collapse into a generic GS answer."),
        ("Value-institution-technology-environment pass", "Values, institutions, technology and environment are useful cross-checks when they expose different mechanisms, actors or trade-offs."),
        ("One-line claim test", "State each candidate dimension as one sentence; if two sentences make the same claim, one is redundant despite different labels."),
        ("Mechanism test", "A dimension survives only if it explains how or why the prompt's relationship operates, not merely where the topic can be mentioned."),
        ("Evidence map", "Attach a named, verifiable illustration to every kept dimension and park any angle dependent on unsafe recall."),
        ("Limit map", "Attach a counter-case, exception or condition to each major dimension so breadth does not become a series of absolutes."),
        ("Prioritisation", "Rank candidate dimensions by thesis relevance, mechanism strength, evidence safety and capacity to add a new argumentative job."),
        ("Clustering", "Group related claims into paragraph clusters around one mechanism or scale movement instead of assigning one paragraph to every brainstormed word."),
        ("Redundancy removal", "Delete a dimension when removing it costs only vocabulary rather than a distinct claim, mechanism or evidentiary function."),
        ("Convergent pass", "After divergence, cut to the strongest coherent set and reject angles that form parallel mini-essays under the same title."),
        ("Argument sequence", "Order the final clusters so each raises, complicates or qualifies the stakes of the previous one and collectively earns the synthesis."),
    ]
    traps = [
        "Do not treat PESTLE, actor lists or domain lists as mandatory headings.",
        "Do not confuse a new label with a genuinely new claim.",
        "Do not force a historical, future or global angle where the prompt does not support it.",
        "Do not keep a dimension that lacks a mechanism.",
        "Do not keep a dimension whose only evidence is unsafe recall.",
        "Do not use cause-impact-response as a disguised GS answer.",
        "Do not mistake breadth for coherence.",
        "Do not preserve redundant material because time was spent generating it.",
        "Do not write one thin paragraph for every brainstormed dimension.",
        "Do not sequence clusters as an unconnected catalogue.",
    ]
    titles = [
        "Divergent generation and actor axis",
        "Scale axis",
        "Time axis",
        "Domain axis",
        "Causality axis",
        "Distribution and direction axes",
        "PESTLE as prompt not template",
        "Cause impact response with Essay discipline",
        "Values institutions technology and environment",
        "One-line claim test",
        "Mechanism and evidence map",
        "Limit and counter-case map",
        "Prioritisation",
        "Clustering and redundancy removal",
        "Convergent sequence and synthesis",
    ]
    routes = [
        "Generate broadly before ranking.",
        "Use actors only when the mechanism changes across them.",
        "Move scale only where the proposition remains textually defensible.",
        "Use time to reveal change, not to fill sections.",
        "Select domains that contribute distinct analytical work.",
        "Trace causes, effects and feedback without creating a list.",
        "Add distribution and double-effect analysis where relevant.",
        "Discard framework labels after they have generated prompt-specific claims.",
        "Keep every cause, impact and response tied to one thesis.",
        "Use cross-check lenses to expose omitted mechanisms or trade-offs.",
        "Compare claim sentences to detect false expansion.",
        "Require both explanation and safe illustration.",
        "Qualify each major dimension before synthesis.",
        "Rank, cluster and cut before planning paragraphs.",
        "Sequence a coherent build rather than parallel coverage.",
    ]
    panels = [
        common.panel("Divergent-to-convergent funnel", "process-flow", [
            "DECODED PROMPT",
            "DIVERGE -> generate candidate claims",
            "FILTER -> mechanism + evidence + limit",
            "CONVERGE -> coherent argument clusters",
        ], ["Divergent pass", "Convergent pass"]),
        common.panel("Actor ladder", "hierarchy", [
            "INDIVIDUAL -> FAMILY OR COMMUNITY",
            "INSTITUTION -> STATE",
            "GLOBAL ORDER -> CIVILISATION",
            "KEEP ONLY -> levels that change claim or mechanism",
        ], ["Actor axis", "Mechanism test"]),
        common.panel("Scale-time matrix", "matrix", [
            "LOCAL TO NATIONAL -> proximity and institutions",
            "GLOBAL TO CIVILISATIONAL -> systems and long-run pattern",
            "PAST TO PRESENT -> continuity and change",
            "FUTURE -> plausible trajectory, not prediction",
        ], ["Scale axis", "Time axis"]),
        common.panel("Domain search field", "radial-map", [
            "SOCIAL + ECONOMIC + POLITICAL",
            "ETHICAL + CULTURAL",
            "TECHNOLOGICAL + ECOLOGICAL",
            "RULE -> lens earns entry only through a distinct claim",
        ], ["Domain axis", "Value-institution-technology-environment pass"]),
        common.panel("Causal architecture", "causal-chain", [
            "IMMEDIATE CAUSE -> STRUCTURAL CAUSE",
            "IMPACT -> DISTRIBUTIONAL EFFECT",
            "RESPONSE -> FEEDBACK",
            "LIMIT -> not every prompt requires the whole chain",
        ], ["Causality axis", "Distribution axis", "Cause-impact-response boundary"]),
        common.panel("Direction test", "dialectic", [
            "INTENDED BENEFIT",
            "UNINTENDED CONSEQUENCE",
            "WHO GAINS OR LOSES",
            "SYNTHESIS -> conditions changing the balance",
        ], ["Direction axis", "Distribution axis"]),
        common.panel("Framework firewall", "comparison-table", [
            "PESTLE -> recall prompt",
            "ACTOR OR DOMAIN GRID -> search aid",
            "COMPULSORY HEADINGS -> reject",
            "OUTPUT -> prompt-specific claims without visible template",
        ], ["PESTLE boundary", "Domain axis"]),
        common.panel("Claim distinction test", "decision-tree", [
            "WRITE ONE SENTENCE PER DIMENSION",
            "SAME CLAIM IN NEW WORDS? -> DELETE",
            "NEW MECHANISM OR SCALE? -> CONTINUE",
            "NO THESIS LINK? -> PARK",
        ], ["One-line claim test", "Redundancy removal"]),
        common.panel("Evidence-limit card", "status-ladder", [
            "CLAIM -> MECHANISM",
            "MECHANISM -> NAMED EVIDENCE",
            "EVIDENCE -> LIMIT OR COUNTER-CASE",
            "COMPLETE CARD -> eligible for prioritisation",
        ], ["Mechanism test", "Evidence map", "Limit map"]),
        common.panel("Prioritisation grid", "matrix", [
            "THESIS RELEVANCE -> high or low",
            "MECHANISM STRENGTH -> clear or vague",
            "EVIDENCE SAFETY -> secure or risky",
            "NEW ARGUMENT JOB -> distinct or redundant",
        ], ["Prioritisation", "Redundancy removal"]),
        common.panel("Cluster builder", "systems-map", [
            "RELATED CLAIMS -> one mechanism cluster",
            "CLUSTER ONE -> foundation",
            "CLUSTER TWO -> expansion or complication",
            "CLUSTER THREE -> counter-view and synthesis",
        ], ["Clustering", "Argument sequence"]),
        common.panel("Brainstorming answer spine", "answer-spine", [
            "DIVERGE ACROSS ACTOR SCALE TIME DOMAIN",
            "TEST CAUSALITY DISTRIBUTION AND DIRECTION",
            "WRITE CLAIMS -> MAP EVIDENCE -> MAP LIMITS",
            "PRIORITISE -> CLUSTER -> CUT -> SEQUENCE",
        ], ["Convergent pass", "Argument sequence", "Evidence map"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2024-A2", "Essay",
            "The empires of the futures will be the empires of the mind.",
            "Exact V1 wording; used to generate and filter actor, scale, domain and evidence dimensions.",
            [0, 1, 2, 4, 10, 11, 12, 13, 15, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2025-A3", "Essay",
            "Thought finds a world and creates one also.",
            "Exact V1 wording; used to test double effects, time, scale and convergent clustering.",
            [2, 3, 7, 11, 12, 14, 16, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2023-B5", "Essay",
            "Girls are weighed down by restrictions, boys with demands — two equally harmful disciplines.",
            "Exact V1 wording; used for actor, distribution, direction and redundancy tests.",
            [1, 6, 7, 11, 12, 13, 14, 15, 16, 19],
        ),
    ]
    return common.topic(
        4,
        "Brainstorming and Dimensional Expansion",
        "04_Brainstorming-and-Dimensional-Expansion",
        facts,
        traps,
        [
            (10, "Distinguish divergent generation from convergent selection.", [0, 18]),
            (10, "Explain how actor, scale, time and domain axes generate candidate dimensions.", [1, 2, 3, 4]),
            (15, "Assess PESTLE and cause-impact-response as prompts rather than Essay templates.", [5, 8, 9, 10]),
            (15, "Design a claim-mechanism-evidence-limit filter for candidate dimensions.", [11, 12, 13, 14]),
            (20, "Analyse prioritisation, clustering and redundancy removal in building a coherent brainstorm.", [15, 16, 17, 18, 19]),
            (20, "Apply the divergent-to-convergent method to a verified philosophical or hybrid prompt.", [0, 1, 2, 3, 4, 6, 7, 11, 12, 13, 15, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "Dimension", "Scale axis", "Time axis", "Domain axis",
            "distributional", "duplicate-claim", "mechanism",
            "recallable illustration", "breadth", "coherence",
        ],
        "The three cards preserve exact V1 prompt wording from 2023–2025. Their models demonstrate brainstorming, filtering and sequencing rather than an official or complete model essay.",
        pyqs,
        LIVE_ATTEMPTS,
        "The official-site attempts on 2026-09-04 found no official brainstorming framework or dimension count. All axes, PESTLE use, filters and sequencing rules remain explicitly pedagogical and prompt-dependent.",
        extra=[
            "00_Master-Framework.md",
            "README.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
            "PYQ-Corpus-2013-2025.md",
        ],
        register_headings=(
            "DIVERGENT AXES AND PROMPT-SPECIFIC SEARCH FIELD",
            "MECHANISM, EVIDENCE, LIMIT AND REDUNDANCY FIREWALLS",
            "PRIORITISE, CLUSTER, CUT AND SEQUENCE SPINE",
            "NON-OFFICIAL FRAMEWORK AND LIVE-SOURCE BOUNDARY",
        ),
        register_answer_spine=[
            "START FROM THE DECODED OR SCOPED PROMPT",
            "DIVERGE ACROSS ACTOR SCALE TIME DOMAIN AND DIRECTION",
            "USE PESTLE ONLY AS A RECALL PROMPT",
            "WRITE ONE-LINE CLAIMS",
            "MAP MECHANISM EVIDENCE AND LIMIT",
            "PRIORITISE CLUSTER AND REMOVE REDUNDANCY",
            "SEQUENCE ONE COHERENT ARGUMENT",
        ],
    )


TOPIC_04 = _build()
