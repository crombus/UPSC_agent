"""Authored learner-v2 data for Essay Topic 01."""

from __future__ import annotations

import generate_essay_common as common


LIVE_ATTEMPTS = [
    (
        "https://upsc.gov.in/examinations/previous-question-papers — attempted "
        "2026-09-04; the official UPSC index returned an access block to the "
        "live fetch, so no new wording or paper rule was imported."
    ),
    (
        "https://upsc.gov.in/examinations/active-examinations — attempted "
        "2026-09-04; the official UPSC page returned an access block, so the "
        "repository's audited rule boundary remains controlling."
    ),
    (
        "https://upsc.gov.in/sites/default/files/Notif-CSP-2024-Engl-140224.pdf "
        "— searched 2026-09-04; the official notification URL was located only "
        "as a scheme cross-check route and supplied no unaudited current rule."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("2024 printed instruction", "The locally audited 2024 paper says: \"Write two essays, choosing one topic from each of the following Sections A and B, in about 1000-1200 words each:\" and prints \"(125 × 2 = 250)\"."),
        ("2025 audited boundary", "The locally audited 2025 English instruction is garbled, but its Hindi line and two section headings still establish two essays, one from each Section, about 1000–1200 words each; that copy prints no marks line."),
        ("One-per-section constraint", "The audited 2024 and 2025 papers require one topic from Section A and one from Section B, so selecting two prompts from one Section violates the printed structure."),
        ("Four-prompt choice set", "Each audited 2024 and 2025 Section displays four prompts, producing a separate four-way choice within each Section."),
        ("Bilingual display", "The audited prompts are printed bilingually, Hindi first and English second; the repository quotes only the audited English line."),
        ("Numbering instability", "Printed numbering is not a stable rule: 2024 restarts Section B at 1–4, whereas 2025 continues it at 5–8."),
        ("Attribution boundary", "Neither audited 2024 nor 2025 paper prints an author beside any prompt, so selection must not depend on an invented attribution."),
        ("Rubric boundary", "The audited papers print no granular marking rubric, examiner weightage or ideal paragraph and example count; internal choice tools are therefore strategy, not official rules."),
        ("Duration boundary", "The repository dates the three-hour Essay duration to the official Civil Services Main examination scheme, not to a time header in the locally held 2024–2025 scans."),
        ("Rule-strategy firewall", "Official constraints state what must be attempted; topic scanning, time splits, matrices and risk scores are pedagogical strategies that must remain explicitly non-official."),
        ("Thesis-fit", "A prompt is high-fit when it quickly yields one contestable, qualified and supportable central claim rather than a restatement or subject label."),
        ("Interpretive clarity", "A safe choice allows the candidate to restate the exact proposition and identify whether it needs philosophical decoding, issue scoping or both."),
        ("Dimension distinctness", "A viable prompt yields several genuinely different claims or mechanisms; repeated vocabulary around one idea is not multidimensional depth."),
        ("Evidence availability", "Selection should favour prompts for which safe, verifiable Indian or global illustrations can be recalled without invented data or forced relevance."),
        ("Familiarity limit", "Subject familiarity is useful only when it supports the printed proposition; familiarity alone can trigger a GS-style fact stack on an adjacent topic."),
        ("Originality limit", "Originality means a defensible interpretation and synthesis, not an eccentric reading that loses contact with the prompt's words."),
        ("Risk screening", "A prompt becomes risky when its thesis is strained, dimensions duplicate, evidence is uncertain, the conclusion is forced or the reading depends on a printing defect."),
        ("Two-essay portfolio", "The final choice is a pair decision: both selected prompts must remain defensible under the same total time and evidence budget."),
        ("Time allocation", "Choice, planning, drafting and revision allocations are internal execution choices; no phase split should be presented as an official UPSC instruction."),
        ("Commitment discipline", "After a bounded scan and viability test, commit before drafting; switch only early when the prompt fails a genuine thesis, dimension or evidence gate."),
    ]
    traps = [
        "Do not convert a locally audited 2024 rule into an unsupported claim about every future paper.",
        "Do not quote the garbled 2025 English instruction as clean official wording.",
        "Do not select two prompts from the same Section.",
        "Do not treat internal B5–B8 labels as stable printed numbering.",
        "Do not present a choice matrix or time split as an official UPSC rule.",
        "Do not choose by familiarity, emotional appeal or quotation recognition alone.",
        "Do not mistake eccentric interpretation for originality.",
        "Do not commit when evidence depends on half-remembered figures or attributions.",
        "Do not optimise one essay by leaving the second with an unworkable time budget.",
        "Do not reverse a viable choice merely because another topic later looks more fashionable.",
    ]
    titles = [
        "Audited 2024 and 2025 paper boundary",
        "One topic from each Section",
        "Four-prompt scan within each Section",
        "Bilingual prompt display",
        "Printed numbering instability",
        "Attribution and rubric boundaries",
        "Three-hour duration boundary",
        "Official rule versus strategy",
        "Thesis-fit viability test",
        "Interpretive clarity and prompt type",
        "Dimension and evidence tests",
        "Familiarity versus tractability",
        "Originality without eccentricity",
        "Risk screen and two-essay portfolio",
        "Time allocation and commitment discipline",
    ]
    routes = [
        "State the dated audited boundary before giving any selection advice.",
        "Check the one-per-Section rule before comparing prompt appeal.",
        "Run the same quick viability test on all four prompts in a Section.",
        "Follow section headings rather than assuming a numbering convention.",
        "Use prompt wording without inventing an author or official rubric.",
        "Label every matrix, score and time split as strategy.",
        "Prefer the prompt that produces a qualified claim early.",
        "Classify the prompt before planning dimensions.",
        "Demand distinct claims, not renamed repetitions.",
        "Choose only evidence-safe routes that can survive verification.",
        "Use familiarity as a resource, never as the selection criterion.",
        "Reward textual fidelity and defensible synthesis.",
        "Reject choices with multiple unresolved risk signals.",
        "Protect both essays inside one execution budget.",
        "Commit after sufficient testing and change only before sunk drafting.",
    ]
    panels = [
        common.panel("Official paper boundary", "comparison-table", [
            "2024 PAPER -> clean two-essay and one-per-section instruction",
            "2025 PAPER -> garbled English line but two sections remain clear",
            "SCHEME -> three-hour duration",
            "FIREWALL -> audited fact is not a prediction of a future paper",
        ], ["2024 printed instruction", "2025 audited boundary", "Duration boundary"]),
        common.panel("Section-choice constraint", "numbered-rail", [
            "SECTION A -> scan four prompts -> choose one",
            "SECTION B -> scan four prompts -> choose one",
            "PAIR -> two essays",
            "INVALID -> both choices from the same Section",
        ], ["One-per-section constraint", "Four-prompt choice set"]),
        common.panel("Paper-layout cautions", "matrix", [
            "BILINGUAL -> Hindi then English",
            "2024 B NUMBERING -> restarts",
            "2025 B NUMBERING -> continues",
            "ACTION -> read headings before relying on numbers",
        ], ["Bilingual display", "Numbering instability"]),
        common.panel("Official versus strategic", "firewall", [
            "OFFICIAL -> attempt structure and audited wording",
            "STRATEGY -> scan, score, allocate and commit",
            "NOT PRINTED -> granular rubric or paragraph count",
            "RULE -> never promote a heuristic into an instruction",
        ], ["Rubric boundary", "Rule-strategy firewall", "Time allocation"]),
        common.panel("Prompt viability gate", "process-flow", [
            "RESTATABLE CLAIM?",
            "QUALIFIED THESIS?",
            "DISTINCT DIMENSIONS?",
            "SAFE EVIDENCE? -> if any answer is no, raise risk",
        ], ["Thesis-fit", "Interpretive clarity", "Dimension distinctness", "Evidence availability"]),
        common.panel("Familiarity test", "comparison-table", [
            "FAMILIAR + THESIS-FIT -> usable",
            "FAMILIAR + FACT STACK -> unsafe",
            "UNFAMILIAR + CLEAR TENSION -> potentially safer",
            "DECISION -> tractability outranks comfort",
        ], ["Familiarity limit", "Thesis-fit"]),
        common.panel("Originality boundary", "dialectic", [
            "PLAIN READING -> faithful but contestable",
            "ORIGINAL MOVE -> qualified connection or synthesis",
            "ECCENTRIC MOVE -> loses the printed relation",
            "KEEP -> originality that remains text-bound",
        ], ["Originality limit", "Interpretive clarity"]),
        common.panel("Evidence-risk screen", "status-ladder", [
            "GREEN -> named and safely recallable illustration",
            "AMBER -> useful but detail uncertain",
            "RED -> invented number, author or forced example",
            "CHOICE -> prefer the prompt with stronger evidence safety",
        ], ["Evidence availability", "Risk screening", "Attribution boundary"]),
        common.panel("Conclusion feasibility", "causal-chain", [
            "THESIS -> DIMENSIONS -> COUNTER-VIEW",
            "COUNTER-VIEW -> QUALIFICATION",
            "QUALIFICATION -> EARNED SYNTHESIS",
            "FORCED ENDING -> warning that choice may be weak",
        ], ["Thesis-fit", "Risk screening"]),
        common.panel("Two-essay portfolio", "systems-map", [
            "ESSAY A -> clarity + depth + evidence",
            "ESSAY B -> clarity + depth + evidence",
            "SHARED BUDGET -> planning + drafting + revision",
            "PAIR TEST -> neither choice should impoverish the other",
        ], ["Two-essay portfolio", "Time allocation"]),
        common.panel("Commitment rule", "decision-tree", [
            "BOUNDED SCAN -> viability passed -> commit",
            "EARLY FAILURE -> switch once before drafting expands",
            "LATE DOUBT -> return to thesis and evidence map",
            "DISCIPLINE -> do not chase a fashionable alternative",
        ], ["Commitment discipline", "Risk screening"]),
        common.panel("Selection answer spine", "answer-spine", [
            "READ RULE -> SCAN EACH SECTION -> CLASSIFY PROMPTS",
            "TEST THESIS -> TEST DIMENSIONS -> TEST EVIDENCE",
            "SCREEN RISK -> TEST THE PAIR -> ALLOCATE TIME",
            "COMMIT -> DECODE OR SCOPE -> PLAN",
        ], ["Rule-strategy firewall", "Two-essay portfolio", "Commitment discipline"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2024", "Essay instructions",
            "Write two essays, choosing one topic from each of the following Sections A and B, in about 1000-1200 words each:",
            "Exact locally audited instruction; the associated marks line is (125 × 2 = 250).",
            [0, 2, 3, 9, 18],
        ),
        common.make_pyq_solution(
            facts, "2024-A2", "Essay",
            "The empires of the futures will be the empires of the mind.",
            "Exact V1 wording from the local official paper; used as a selection application, not an official model answer.",
            [10, 11, 12, 13, 14, 15],
        ),
        common.make_pyq_solution(
            facts, "2024-B5", "Essay",
            "Social media is triggering 'Fear of Missing Out' amongst the youth precipitating depression and loneliness.",
            "Exact V1 wording from the local official paper; used to contrast issue-prompt tractability with familiarity risk.",
            [10, 11, 13, 14, 16, 17],
        ),
    ]
    return common.topic(
        1,
        "Paper Rules, Choice and Selection",
        "01_Paper-Rules-Choice-and-Selection",
        facts,
        traps,
        [
            (10, "Separate the audited Essay paper rules from candidate strategy.", [0, 1, 2, 8, 9]),
            (10, "Build a concise prompt-selection viability test.", [10, 11, 12, 13]),
            (15, "Explain why familiarity and originality are insufficient selection criteria.", [14, 15, 16]),
            (15, "Design a risk-screening matrix for choosing one prompt from each Section.", [2, 10, 12, 13, 16]),
            (20, "Analyse topic choice as a two-essay portfolio decision under time pressure.", [10, 13, 16, 17, 18, 19]),
            (20, "Apply the selection method to one philosophical and one issue-based V1 prompt.", [10, 11, 12, 13, 14, 15, 17]),
        ],
        titles,
        routes,
        panels,
        [
            "one topic from each", "thesis-fit", "dimension count",
            "evidence availability", "portfolio decision", "familiarity",
            "three-hour", "1000–1200",
        ],
        "The cards preserve one exact 2024 instruction and two exact V1 prompts. Their solutions demonstrate selection method only and never claim an official model answer.",
        pyqs,
        LIVE_ATTEMPTS,
        "Rule boundary dated 2026-09-04: use the repository's locally audited 2024–2025 instructions plus the official-scheme duration. Re-check the applicable UPSC notification and paper before asserting a future year's exact rules.",
        extra=[
            "00_Master-Framework.md",
            "README.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
            "PYQ-Corpus-2013-2025.md",
        ],
        register_headings=(
            "AUDITED PAPER RULES AND DATED BOUNDARY",
            "CHOICE SIGNALS, FALSE SIGNALS AND RISK FIREWALLS",
            "TWO-SECTION SELECTION AND COMMITMENT SPINE",
            "LIVE UPSC CHECK AND FUTURE-PAPER CAUTION",
        ),
        register_answer_spine=[
            "CONFIRM THE DATED ONE-PER-SECTION RULE",
            "SCAN ALL FOUR PROMPTS IN EACH SECTION",
            "CLASSIFY PHILOSOPHICAL ISSUE OR HYBRID",
            "TEST THESIS DIMENSIONS EVIDENCE AND CONCLUSION",
            "SCREEN ATTRIBUTION PRINTING AND FACT RISK",
            "TEST BOTH ESSAYS AGAINST ONE TIME BUDGET",
            "COMMIT BEFORE DRAFTING",
        ],
        allow_existing_history=True,
    )


TOPIC_01 = _build()
