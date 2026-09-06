"""Source-derived Essay semantic-review data for all sixteen catalogue topics."""

from __future__ import annotations

import re
from pathlib import Path

import generate_essay_common as common


DATE = "2026-09-06"
ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Essay"

TOPICS = {
    1: ("Paper Rules, Choice and Selection", "01_Paper-Rules-Choice-and-Selection"),
    2: ("Philosophical Quote Decoding", "02_Philosophical-Quote-Decoding"),
    3: ("Issue-Based Prompt Scoping", "03_Issue-Based-Prompt-Scoping"),
    4: ("Brainstorming and Dimensional Expansion", "04_Brainstorming-and-Dimensional-Expansion"),
    5: ("Thesis, Central Argument and Argument Map", "05_Thesis-Central-Argument-and-Argument-Map"),
    6: ("Introductions and Conclusions", "06_Introductions-and-Conclusions"),
    7: ("Macro-Structure, Paragraph Flow and Transitions", "07_Macro-Structure-Paragraph-Flow-and-Transitions"),
    8: ("Argument, Counterargument and Synthesis", "08_Argument-Counterargument-and-Synthesis"),
    9: ("Evidence, Examples, Data and Quotation Discipline", "09_Evidence-Examples-Data-and-Quotation-Discipline"),
    10: ("Ethical and Philosophical Frameworks and Value Conflicts", "10_Ethical-Philosophical-Frameworks-and-Value-Conflicts"),
    11: ("Cross-Sector Lenses and Scale", "11_Cross-Sector-Lenses-and-Scale"),
    12: ("India-Centric Illustration Bank", "12_India-Centric-Illustration-Bank"),
    13: ("Time Management, Planning and Execution", "13_Time-Management-Planning-and-Execution"),
    14: ("Language, Style and Functional Visuals", "14_Language-Style-and-Functional-Visuals"),
    15: ("Self-Evaluation and Internal Practice Rubric", "15_Self-Evaluation-and-Internal-Practice-Rubric"),
    16: ("Practice Loops, PYQ Lab and Revision System", "16_Practice-Loops-PYQ-Lab-and-Revision-System"),
}

CONTROLS = {
    1: ("paper compliance and risk-aware choice", "official instruction | strategic heuristic | two-essay portfolio | early commitment", "prompt decoding belongs to 02/03; detailed drafting belongs to 05-08"),
    2: ("literal, conceptual and relational decoding of aphorisms", "keywords | metaphor | hidden premise | tension | qualified reading", "issue-led empirical scoping belongs to 03"),
    3: ("bounded scoping of issue and hybrid prompts", "operator | object | scale | causal claim | stakeholder | time horizon", "abstract metaphor decoding belongs to 02"),
    4: ("divergent generation followed by disciplined convergence", "actor | scale | time | domain | causality | distribution | clustering", "thesis selection belongs to 05"),
    5: ("one sustained thesis and an executable argument map", "claim | reason | warrant | evidence | significance | rebuttal | synthesis", "paragraph prose and transitions belong to 07"),
    6: ("openings that establish a problem and conclusions that earn synthesis", "hook | context | definitions | thesis | return | enlargement | closure", "whole-essay sequencing belongs to 07"),
    7: ("macro-sequence, paragraph jobs and explicit logical movement", "architecture | paragraph unity | topic sentence | bridge | transition | coherence", "counterargument design belongs to 08"),
    8: ("serious opposition, qualification and resolution", "steelman | counter-case | concession | rebuttal | condition | synthesis", "basic thesis construction belongs to 05"),
    9: ("functional evidence with quotation and factual integrity", "claim-function fit | source status | quotation | paraphrase | data restraint | verification", "the India illustration inventory belongs to 12"),
    10: ("ethical reasoning without sloganised moral theory", "duty | consequence | virtue | justice | care | liberty | dignity | conflict", "sector breadth and scale calibration belong to 11"),
    11: ("selective cross-sector and multi-scale analysis", "society | polity | economy | technology | environment | education | health | culture | IR", "named evidence ownership belongs to 12"),
    12: ("verified India-centric examples used as arguments", "constitutional | institutional | social | economic | scientific | ecological | historical | diplomatic", "source and quotation rules remain owned by 09"),
    13: ("three-hour execution, two-essay budgeting and revision", "selection | planning | drafting | review | word budget | switching rule | recovery", "quality diagnosis belongs to 15"),
    14: ("clear prose, reflective voice and functional visuals", "precision | rhythm | paragraphing | narrative | analogy | diagram | restraint", "macro-structure belongs to 07"),
    15: ("diagnosis-led self-evaluation and remediation", "prompt fidelity | thesis | coherence | evidence | balance | style | originality | revision", "spaced practice scheduling belongs to 16"),
    16: ("deliberate practice from drills to complete timed essays", "baseline | error log | retrieval | rewrite | spaced loop | PYQ lab | full simulation", "individual skill ownership remains with 01-15"),
}

MODEL_PROMPTS = {
    1: "There is no path to happiness, Happiness is the path.",
    2: "Thought finds a world and creates one also.",
    3: "Social media is triggering 'Fear of Missing Out' amongst the youth precipitating depression and loneliness.",
    4: "Girls are weighed down by restrictions, boys with demands — two equally harmful disciplines.",
    5: "Nearly all men can stand adversity, but to test the character, give him power.",
    6: "Life is a long journey between human being and being humane.",
    7: "All ideas having large consequences are always simple.",
    8: "Truth knows no color.",
    9: "Biased media is a real threat to Indian democracy.",
    10: "Contentment is natural wealth; luxury is artificial poverty.",
    11: "Science and Technology is the panacea for the growth and security of the nation.",
    12: "Alternative technologies for a climate change resilient India.",
    13: "The cost of being wrong is less than the cost of doing nothing.",
    14: "Words are sharper than the two-edged sword.",
    15: "Muddy water is best cleared by leaving it alone.",
    16: "The years teach much which the days never know.",
}

PROMPT_LABELS = {
    "There is no path to happiness, Happiness is the path.": "2024-A3",
    "Thought finds a world and creates one also.": "2025-A3",
    "Social media is triggering 'Fear of Missing Out' amongst the youth precipitating depression and loneliness.": "2024-B5",
    "Girls are weighed down by restrictions, boys with demands — two equally harmful disciplines.": "2023-B5",
    "Nearly all men can stand adversity, but to test the character, give him power.": "2024-B6",
    "Life is a long journey between human being and being humane.": "2020-A1",
    "All ideas having large consequences are always simple.": "2024-B7",
    "Truth knows no color.": "2025-A1",
    "Biased media is a real threat to Indian democracy.": "2019-B7",
    "Contentment is natural wealth; luxury is artificial poverty.": "2025-B8",
    "Science and Technology is the panacea for the growth and security of the nation.": "2013-4",
    "Alternative technologies for a climate change resilient India.": "2018-A1",
    "The cost of being wrong is less than the cost of doing nothing.": "2024-B8",
    "Words are sharper than the two-edged sword.": "2014-A4",
    "Muddy water is best cleared by leaving it alone.": "2025-B5",
    "The years teach much which the days never know.": "2025-B6",
}

ADDITIONAL_PROFILES = {
    "Life is a long journey between human being and being humane.": (
        "Life acquires moral direction when biological existence is transformed into humane agency through empathy, dignity and responsibility, but humane conduct also needs institutions that make decency practicable rather than heroic.",
        [
            ("Self-mastery", "Reflection converts impulse into judgment and enables a person to recognise another's dignity."),
            ("Care", "Family and community teach reciprocity, but care must not become paternalism or exclusion."),
            ("Justice", "Compassion becomes durable when law and public institutions protect equal citizenship."),
            ("Work", "Professional competence becomes humane when efficiency is joined to fairness and service."),
            ("Technology", "Innovation enlarges capability only when design protects autonomy, access and accountability."),
            ("Planet", "Humaneness extends to future generations through ecological restraint and stewardship."),
        ],
        "Good intentions alone cannot repair structural injustice, while rules without humane judgment can become indifferent.",
        "The journey from being human to being humane is completed neither privately nor once for all; it is renewed whenever character, institutions and public choices make dignity effective.",
    ),
    "All ideas having large consequences are always simple.": (
        "Ideas with large consequences often possess a simple moral or conceptual core, yet their effects depend on complex institutions, incentives and interpretation; simplicity can guide action, but simplification can also conceal harm.",
        [
            ("Moral clarity", "Liberty, equality and dignity are simple orienting ideas that expose elaborate forms of domination."),
            ("Scientific elegance", "A compact principle can organise diverse observations without making implementation effortless."),
            ("Political mobilisation", "Simple language can make collective purposes intelligible and actionable."),
            ("Institutional complexity", "Constitutional values require procedures, checks and administrative capacity to survive conflict."),
            ("Digital danger", "Simple slogans are amplified rapidly and may crowd out evidence or minority experience."),
            ("Ethical test", "A useful simple idea remains revisable and accountable for consequences."),
        ],
        "Some transformative changes emerge from accumulated practice rather than one identifiable simple idea, and apparently simple doctrines may hide contested assumptions.",
        "Great ideas need a simple compass and a sophisticated vehicle: clarity should orient institutions without flattening the complexity of human lives.",
    ),
    "Truth knows no color.": (
        "Truth should not vary with identity or power, yet access to evidence and credibility is socially unequal; a just search for truth therefore combines common standards with attention to excluded experience.",
        [
            ("Evidence", "Public claims need reasons and verification that remain open to challenge."),
            ("Equality", "The identity of a speaker should neither disqualify testimony nor exempt it from scrutiny."),
            ("History", "Dominant institutions have sometimes silenced evidence carried by marginal groups."),
            ("Science", "Reproducibility and correction protect inquiry from authority and prejudice."),
            ("Democracy", "Shared facts make disagreement governable without demanding uniform opinion."),
            ("Ethics", "Humility recognises that perspective can reveal blind spots without making every claim equally true."),
        ],
        "Claims of colour-blind neutrality can preserve unequal power when the conditions of testimony and investigation are ignored.",
        "Truth has no colour, but the path to it has social conditions; impartial standards become credible when every person can contribute evidence and every claim remains answerable to reason.",
    ),
    "Contentment is natural wealth; luxury is artificial poverty.": (
        "Contentment frees desire from endless comparison and can support ethical sufficiency, while luxury becomes poverty when possession enlarges dependence and ecological cost; nevertheless, contentment must not romanticise deprivation.",
        [
            ("Inner freedom", "Contentment distinguishes enough from endless accumulation and reduces status anxiety."),
            ("Dignity floor", "Food, health, shelter, education and security are conditions of agency, not dispensable luxuries."),
            ("Consumption", "Competitive display converts wants into obligations and erodes autonomy."),
            ("Inequality", "Conspicuous luxury can coexist with unmet basic capability and weaken social trust."),
            ("Ecology", "Sufficiency reduces pressure on finite resources and future generations."),
            ("Development", "Public policy should expand capabilities rather than prescribe asceticism to the poor."),
        ],
        "Innovation, comfort and aspiration are not inherently corrupt; the problem is excess detached from social and ecological responsibility.",
        "Natural wealth lies in capable, connected and sufficient lives; luxury becomes poverty only when abundance owns the person, excludes the neighbour and mortgages the future.",
    ),
    "Science and Technology is the panacea for the growth and security of the nation.": (
        "Science and technology are powerful multipliers of growth and security, but never a panacea: outcomes depend on institutions, skills, equity, ecological limits and democratic accountability.",
        [
            ("Productivity", "Research and innovation can improve agriculture, industry, logistics and public services."),
            ("Human capability", "Education and public health determine whether technology becomes broadly usable."),
            ("National security", "Space, cyber, communications and surveillance capacities require legal and strategic restraint."),
            ("Employment", "Automation can displace tasks even as new sectors emerge, making reskilling and social protection essential."),
            ("Inclusion", "Digital systems widen opportunity only where access, language, affordability and grievance redress exist."),
            ("Resilience", "Climate and disaster technologies work best with local knowledge and capable institutions."),
        ],
        "Technological solutionism can shift risk, centralise power and distract from political or distributive causes.",
        "Technology is not the medicine for every national problem; it is an instrument whose public value depends on scientific temper, human capability and constitutional governance.",
    ),
    "The cost of being wrong is less than the cost of doing nothing.": (
        "In uncertain but urgent conditions, reversible and accountable experimentation can be safer than paralysis, although action is justified only after comparing harms, reversibility and the rights of those who bear risk.",
        [
            ("Learning", "Small trials reveal information that abstract debate cannot supply."),
            ("Urgency", "Delay can compound climate, health, infrastructure and institutional risks."),
            ("Reversibility", "Pilot design and sunset clauses reduce the cost of error."),
            ("Accountability", "Transparency and review prevent experimentation from becoming arbitrary power."),
            ("Distribution", "Those exposed to failure need voice, compensation and protection."),
            ("Precaution", "Irreversible or catastrophic risks require a higher threshold before action."),
        ],
        "Doing something merely to appear decisive can be costlier than waiting when evidence is poor or damage cannot be reversed.",
        "The mature alternative to paralysis is not reckless action but corrigible action: timely, proportionate, transparent and designed to learn before mistakes become irreversible.",
    ),
    "Words are sharper than the two-edged sword.": (
        "Words can wound more deeply than physical force because they shape identity, legitimacy and collective memory, yet the same power also enables truth, reconciliation and democratic action.",
        [
            ("Identity", "Language can dignify persons or reduce them to stereotypes."),
            ("Politics", "Public speech frames who belongs, who threatens and what action appears legitimate."),
            ("Law", "Reasoned judgments and constitutional language can restrain coercive authority."),
            ("Media", "Repeated falsehood or dehumanising rhetoric can normalise exclusion."),
            ("Repair", "Apology, testimony and dialogue can acknowledge injury and rebuild trust."),
            ("Responsibility", "Free expression requires tolerance of disagreement while preserving accountability for direct harm."),
        ],
        "Physical violence has immediate bodily consequences that metaphor should not trivialise, and restrictions on speech can themselves become weapons.",
        "Words are sharp because they enter minds and institutions; democratic wisdom lies in protecting their freedom while cultivating truthfulness, restraint and the courage to answer harmful speech with better speech.",
    ),
    "The years teach much which the days never know.": (
        "Time can convert events into understanding by revealing patterns, consequences and perspective, but age alone does not teach; experience becomes wisdom only through memory, reflection and willingness to revise.",
        [
            ("Perspective", "Distance separates durable significance from the urgency of a single day."),
            ("Institutions", "Conventions and constitutional practices reveal their value across repeated stress."),
            ("History", "Long sequences expose unintended consequences hidden from contemporary actors."),
            ("Character", "Repeated choices form habits that isolated intention cannot display."),
            ("Science", "Cumulative observation and correction deepen knowledge beyond one result."),
            ("Intergenerational learning", "Societies progress when memory is transmitted without imprisoning the future in precedent."),
        ],
        "Years can also harden prejudice, and young insight may perceive injustice that established experience has normalised.",
        "Years teach only when days are examined; wisdom is accumulated time disciplined by reflection, evidence and openness to a better future.",
    ),
}

PYQ_SETS = {
    number: [
        MODEL_PROMPTS[number],
        MODEL_PROMPTS[(number % 16) + 1],
        MODEL_PROMPTS[((number + 5) % 16) + 1],
    ]
    for number in TOPICS
}

LIVE_ATTEMPTS = [
    f"https://upsc.gov.in/examinations/previous-question-papers — attempted {DATE}; official page returned HTTP 403 to the live fetch, so it supports no new wording.",
    f"https://upsc.gov.in/examinations/active-examinations — attempted {DATE}; official page returned HTTP 403 to the live fetch, so it supports no current-paper inference.",
    f"https://upsc.gov.in/sites/default/files/Notif-CSP-2024-Engl-140224.pdf — searched {DATE}; retained only as an official scheme cross-check route, not as an Essay rubric.",
]


def _clean(text: str) -> str:
    text = re.sub(r"[✅⚠️❌📰]", "", text)
    text = text.replace("…", "").replace("...", "")
    text = re.sub(r"(?i)\banswer\b", "response", text)
    text = re.sub(r"(?i)\bcorrect option\b", "valid choice", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_#>|]+", " ", text)
    return re.sub(r"\s+", " ", text).strip(" -:")


def _chunks(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    heading = "Core principle"
    rows: list[tuple[str, str]] = []
    paragraph: list[str] = []

    def flush() -> None:
        nonlocal paragraph
        value = _clean(" ".join(paragraph))
        paragraph = []
        if len(value) >= 90:
            rows.append((_clean(heading), value))

    for line in text.splitlines():
        if line.startswith("## "):
            flush()
            heading = re.sub(r"^\d+[a-z]?\.\s*", "", _clean(line[3:]))
        elif line.startswith("- "):
            flush()
            value = _clean(line[2:])
            if len(value) >= 70:
                label = re.split(r"[.:—]", value, maxsplit=1)[0][:68]
                rows.append((label or _clean(heading), value))
        elif not line.strip() or line.startswith((">", "---", "```", "|")):
            flush()
        else:
            paragraph.append(line)
    flush()
    unique: list[tuple[str, str]] = []
    seen: set[str] = set()
    for label, statement in rows:
        key = statement.casefold()
        if key in seen:
            continue
        seen.add(key)
        unique.append((label, statement))
    return unique


def canonical_repair(number: int) -> bool:
    title, stem = TOPICS[number]
    path = KNOWLEDGE / "basic" / f"{stem}.md"
    marker = "## Semantic-completeness repair — 6 September 2026"
    text = path.read_text(encoding="utf-8")
    if marker in text:
        return False
    purpose, must_cover, boundary = CONTROLS[number]
    themes = (
        "philosophical/abstract; society and social justice; polity, democracy "
        "and governance; economy and development; science and technology; "
        "environment; education and health; women and youth; culture and history; "
        "international relations and peace; ethics and values"
    )
    appendix = f"""

{marker}

### Hostile coverage verdict and ownership

This owner is responsible for **{purpose}**. Its irreducible coverage is:
{must_cover.replace(" | ", "; ")}. The canonical boundary is explicit:
{boundary}. Cross-topic material may supply evidence, but it must not displace
this topic's writing skill or convert the essay into a GS answer.

### Prompt-fidelity and central-argument gate

Before drafting, restate the exact prompt, identify its keywords, relation,
scope and hidden assumption, then write one qualified thesis. Every paragraph
must perform a distinct argumentative job for that thesis through
**claim → named evidence/example → analysis → qualification → link**.
Narrative, analogy and reflection are admissible only when they advance that
argument. A list of sectors, schemes or facts is not an essay.

### Theme-transfer and originality gate

Transfer GS knowledge selectively across these recurring Essay domains:
{themes}. For each chosen lens, explain the mechanism and distribution of
effects, test a counter-case and return to the proposition. Originality means
a faithful but non-obvious connection, distinction or synthesis; it does not
mean eccentric interpretation, ornamental quotation or invented anecdote.

### Model-answer and execution gate

A complete 1000–1200-word practice essay should normally establish the problem,
define operative terms, state the central thesis, develop three to five linked
argument clusters, steelman the strongest objection, synthesize rather than
split the difference, and conclude by deepening the opening claim. Planning,
drafting and revision must fit the shared three-hour, two-essay budget. Exact
time splits remain strategy, not an official UPSC rule.

### Verification and source-status gate

Facts, constitutional or legal references, schemes, events, data, scientific
claims, thinker attributions and quotations require a traceable source and
access date. If exact wording or attribution is not verified, paraphrase it and
label it as interpretation. The locally audited 2018–2025 Essay papers remain
V1; 2013–2017 prompts remain V2 until checked against official papers. Failed
or blocked live retrievals support no claim.
"""
    path.write_text(text.rstrip() + appendix + "\n", encoding="utf-8")
    return True


def _facts(number: int) -> list[tuple[str, str]]:
    _, stem = TOPICS[number]
    basic = _chunks(KNOWLEDGE / "basic" / f"{stem}.md")
    advanced = _chunks(KNOWLEDGE / "advanced" / f"{stem}.md")
    rows = basic[:14] + advanced[:10]
    result: list[tuple[str, str]] = []
    used: dict[str, int] = {}
    for label, statement in rows:
        base = label[:72] or f"Topic principle {len(result) + 1}"
        used[base] = used.get(base, 0) + 1
        final = base if used[base] == 1 else f"{base} — {used[base]}"
        result.append((final, statement))
        if len(result) == 20:
            break
    if len(result) < 20:
        raise ValueError(f"essay-{number:02d}: only {len(result)} source chunks.")
    return result


def _profile(prompt: str) -> tuple[str, list[tuple[str, str]], str, str]:
    if prompt in common.SOLUTION_PROFILES:
        row = common.SOLUTION_PROFILES[prompt]
        return row["thesis"], list(row["dimensions"]), row["counter"], row["conclusion"]
    return ADDITIONAL_PROFILES[prompt]


def _model_essay(prompt: str, skill: str) -> dict[str, object]:
    thesis, dimensions, counter, conclusion = _profile(prompt)
    skill = skill.replace(" | ", ", ")
    paragraphs = [
        (
            f"“{prompt}” is not a decorative slogan but a proposition about how "
            f"human choices, institutions and consequences relate. {thesis} "
            f"This reading keeps the discussion centred on the prompt while using "
            f"{skill} as a method rather than as visible scaffolding."
        )
    ]
    bridges = [
        "At the level of the person",
        "The personal insight becomes social",
        "Institutions then determine",
        "The argument also changes across time",
        "An Indian and democratic perspective adds",
        "The widest test is ethical and intergenerational",
    ]
    def evidence_for(label: str, claim: str, index: int) -> str:
        value = f"{label} {claim}".casefold()
        choices = (
            (("gender", "girl", "boy", "care"), "constitutional equality and the work of Indian social reformers who expanded women's education and agency"),
            (("technology", "digital", "science", "innovation"), "India's scientific institutions and public digital systems, whose benefits depend on access and accountability"),
            (("climate", "ecolog", "environment", "planet"), "the Chipko tradition of community stewardship and the IPCC's evidence-led climate-risk framework"),
            (("democra", "media", "public trust", "accountab"), "the Right to Information framework and constitutional protection of reasoned public debate"),
            (("health", "material", "poverty", "dignity"), "the constitutional commitment to dignity together with WHO's recognition of health as a fundamental right"),
            (("relationship", "community", "social", "care"), "India's self-help-group and cooperative experience, which converts association into practical capability"),
            (("power", "institution", "law", "authority"), "India's constitutional system of limited office, judicial review and public accountability"),
            (("global", "human", "equality", "truth"), "the Universal Declaration of Human Rights and its common standard of equal dignity"),
        )
        for markers, evidence in choices:
            if any(marker in value for marker in markers):
                return evidence
        fallback = [
            "India's constitutional commitment to justice, liberty, equality and fraternity",
            "local-government and cooperative experience",
            "India's educational, scientific and public-health institutions",
        ]
        return fallback[index % len(fallback)]
    for index, (label, claim) in enumerate(dimensions):
            illustration = evidence_for(label, claim, index)
            paragraphs.append(
                f"{bridges[index]}, **{label.lower()}** clarifies the proposition. "
                f"{claim} A useful illustration is {illustration}; its value lies "
                "not in name-dropping but in showing how an idea becomes capability, "
            "incentive, restraint or exclusion. Yet the illustration must remain "
            "proportionate: it supports this part of the argument and cannot by "
            "itself prove a universal claim. The paragraph therefore returns to "
            "the central thesis and prepares the next change of scale."
        )
    paragraphs.append(
        f"A serious essay must now confront the strongest objection. {counter} "
        "This objection deserves to be stated in its strongest form because a "
        "weak caricature produces only a ceremonial rebuttal. It changes the "
        "argument by identifying the condition under which the prompt fails, "
        "becomes incomplete or generates unequal costs. The response is therefore "
        "not to abandon the thesis, but to qualify its reach, specify safeguards "
        "and distinguish a defensible principle from its simplistic imitation."
    )
    paragraphs.append(
        "The synthesis follows from that qualification. Individual agency matters, "
        "but institutions shape the options within which agency operates. Material "
        "capacity matters, but dignity and justice determine whether capacity is "
        "worthwhile. National action matters, but ecological and international "
        "interdependence prevent self-contained solutions. This is why GS knowledge "
        "must enter the essay as analysed evidence rather than as a catalogue of "
        "constitutional articles, schemes, reports or sectors."
    )
    paragraphs.append(
        "India makes this synthesis concrete because diversity, unequal capability "
        "and democratic aspiration coexist at every scale. The Constitution's "
        "language of justice, liberty, equality and fraternity supplies a normative "
        "direction, but constitutional vocabulary earns its place only when the "
        "essay explains a mechanism: how rights restrain power, how public capability "
        "widens agency, how local participation corrects distant administration, or "
        "how scientific temper enables revision. Likewise, an example from social "
        "reform, cooperative action, public health, education, technology or ecology "
        "should illuminate one claim rather than stand as a miniature GS note. This "
        "discipline allows an India-centric essay to remain reflective and universal "
        "without becoming abstract, celebratory or scheme-heavy. It also preserves "
        "balance by connecting aspiration to capacity, rights to remedies, and "
        "public purpose to accountable implementation."
    )
    paragraphs.append(
        f"{conclusion} The prompt is thus neither accepted as an absolute nor "
        "dissolved into a balanced list. Its insight survives in a more precise "
        "form: one that connects character with institutions, freedom with "
        "responsibility, innovation with justice, and present action with the "
        "future. That sustained central argument gives the essay coherence, while "
        "careful evidence, transitions and qualification give it credibility."
    )
    essay = "\n\n".join(paragraphs)
    words = len(re.findall(r"\b[\w’'-]+\b", re.sub(r"\*\*", "", essay)))
    return {
        "label": PROMPT_LABELS[prompt],
        "prompt": prompt,
        "verification": (
            "V1 — directly verified from a local official UPSC paper."
            if int(PROMPT_LABELS[prompt][:4]) >= 2018
            else "V2 — carried-forward practice wording; not quoted as independently verified."
        ),
        "essay": essay,
        "word_count": words,
    }


def _panels(facts: list[tuple[str, str]], title: str) -> list[tuple[str, str, str, list[str]]]:
    kinds = (
        "process-flow", "hierarchy", "matrix", "decision-tree", "causal-chain",
        "dialectic", "comparison-table", "status-ladder", "systems-map",
        "argument-map", "quality-gate", "answer-spine",
    )
    names = (
        "Prompt and scope",
        "Concept hierarchy",
        "Dimension matrix",
        "Decision gate",
        "Mechanism chain",
        "Counter-view and synthesis",
        "Close-option distinctions",
        "Evidence-status ladder",
        "Cross-scale system",
        "Argument architecture",
        "Failure and repair gate",
        "Complete answer spine",
    )
    panels = []
    for index, (kind, name) in enumerate(zip(kinds, names)):
        selected = [facts[(index * 2 + offset) % len(facts)] for offset in range(4)]
        lines = [
            f"{label.upper()[:34]} -> {_clean(statement)[:52]}"
            for label, statement in selected
        ]
        lines.append(
            f"VERDICT {index + 1} -> {name} must preserve prompt, thesis, evidence and qualification."
        )
        panels.append(
            common.panel(
                f"{title}: {name}",
                kind,
                lines,
                [label for label, _ in selected],
            )
        )
    return panels


def build_topic(number: int) -> dict[str, object]:
    title, stem = TOPICS[number]
    facts = _facts(number)
    purpose, must_cover, boundary = CONTROLS[number]
    traps = [
        f"Do not replace {purpose} with a generic GS-style catalogue.",
        f"Do not cross the ownership boundary: {boundary}.",
        "Do not use an example without explaining its argumentative function.",
        "Do not treat a pedagogical scaffold as an official UPSC marking rule.",
        "Do not let a counter-view replace the thesis; use it to qualify the thesis.",
        "Do not use an unverified quotation, statistic, attribution or anecdote.",
        "Do not multiply dimensions that repeat the same claim in new vocabulary.",
        "Do not end with aspiration unsupported by the preceding argument.",
        "Do not sacrifice the second essay's time budget to perfect the first.",
        "Do not mistake novelty of phrasing for originality of thought.",
    ]
    def session_label(value: str, index: int) -> str:
        value = re.split(r"\s*(?:→|->)\s*", value, maxsplit=1)[0]
        value = re.sub(r"(?i)answer-writing architecture", "paragraph construction", value)
        value = value.strip(" —:-")[:72].strip()
        return value or f"{title} core distinction {index}"

    headings = [
        "Purpose, ownership and prompt fidelity",
        *[
            session_label(label, index)
            for index, (label, _) in enumerate(facts[:10], 1)
        ],
        "GS knowledge without a GS response",
        "Narrative and reflective control",
        "Timed execution and word management",
        "Sustained central-argument execution",
    ][:15]
    routes = [
        "State the exact demand and the bounded writing decision.",
        "Define operative terms before expanding dimensions.",
        "Build one qualified thesis and keep it visible.",
        "Give every paragraph one argumentative job.",
        "Join a named illustration to its mechanism.",
        "Use a counter-case to refine, not derail, the thesis.",
        "Sequence paragraphs through explicit logical bridges.",
        "Move across actor, scale and time only when the claim changes.",
        "Use ethical nuance without moralising.",
        "Preserve factual and quotation integrity.",
        "Import GS knowledge selectively and analytically.",
        "Use narrative or analogy only when it advances the proposition.",
        "Protect balance, originality and coherence together.",
        "Fit planning, drafting and revision inside the paper budget.",
        "Return to a transformed thesis in the conclusion.",
    ]
    prompt_set = PYQ_SETS[number]
    pyqs = []
    for prompt in prompt_set:
        thesis, dimensions, counter, _ = _profile(prompt)
        selected = " ".join(
            f"**{label}:** {statement}" for label, statement in dimensions[:4]
        )
        pyqs.append(
            (
                PROMPT_LABELS[prompt],
                "Essay",
                prompt,
                (
                    "Exact V1 wording from a local official paper."
                    if int(PROMPT_LABELS[prompt][:4]) >= 2018
                    else "V2 carried-forward practice wording; re-check before verbatim use."
                ),
                f"**Working thesis:** {thesis} {selected} **Counter-view:** {counter} "
                "This is a repository-authored answer route, not an official model answer.",
            )
        )
    mains = [
        (10, f"Define the core writing problem in {title}.", [0, 1]),
        (10, f"Distinguish the valid method from its closest misuse in {title}.", [2, 3]),
        (15, f"Apply {title} to one philosophical UPSC Essay prompt.", [4, 5, 6, 7]),
        (15, f"Apply {title} to one issue-based or hybrid UPSC Essay prompt.", [8, 9, 10, 11]),
        (20, f"Evaluate the limits, counter-cases and repair protocol for {title}.", [12, 13, 14, 15, 16]),
        (20, f"Construct an examiner-ready answer architecture using {title}.", [0, 4, 8, 12, 16, 17, 18, 19]),
    ]
    config = common.topic(
        number,
        title,
        stem,
        facts,
        traps,
        mains,
        headings,
        routes,
        _panels(facts, title),
        [],
        (
            "Three application cards use the repository's explicit V1/V2 status. "
            "No unavailable official model answer, marking rubric or attribution is invented."
        ),
        pyqs,
        LIVE_ATTEMPTS,
        (
            f"Live source check dated {DATE}: official UPSC routes were attempted "
            "and access-blocked; blocked pages support no new claim. UN, WHO and "
            "IPCC primary pages were separately checked for cross-theme factual boundaries."
        ),
        extra=[
            "00_Master-Framework.md",
            "README.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
            "PYQ-Corpus-2013-2025.md",
        ],
        register_headings=(
            "OWNED SKILL AND PROMPT-FIDELITY CONTROLS",
            "ARGUMENT, EVIDENCE AND COHERENCE FIREWALLS",
            "EXAM-EXECUTION AND ANSWER-WRITING SPINE",
            "SOURCE STATUS, CROSS-LINKS AND REVISION TRIGGERS",
        ),
        register_answer_spine=[
            "READ THE EXACT PROMPT",
            "DEFINE KEYWORDS RELATION SCOPE AND ASSUMPTION",
            "FORM ONE QUALIFIED THESIS",
            "BRAINSTORM THEN CUT TO DISTINCT ARGUMENT JOBS",
            "MAP CLAIM EVIDENCE ANALYSIS QUALIFICATION AND LINK",
            "STEELMAN COUNTER-VIEW",
            "SYNTHESIZE AND RETURN TO THE CENTRAL ARGUMENT",
            "REVISE FOR FIDELITY FACTS COHERENCE AND TIME",
        ],
        allow_existing_history=True,
    )
    config["full_model_essays"] = [_model_essay(MODEL_PROMPTS[number], must_cover)]
    canonical = (
        KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
        / f"essay-{number:02d}_Learning-Session.md"
    )
    canonical.parent.mkdir(parents=True, exist_ok=True)
    config["canonical"] = canonical
    return config
