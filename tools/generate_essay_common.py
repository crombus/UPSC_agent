"""Essay-specific authoring engine.

Essay intentionally does not use the GS learner-session or MCQ contract. Each
topic produces one complete knowledge guide, one question-only essay practice
workbook, and one separate solutions document while preserving the Basic and
Advanced owner text in full.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType
from typing import Iterable, Iterator

import carvaka_flowchart
import generate_world_history_common as _base
import notions_style_ascii_master as ascii_master
import refresh_all_v2_learning_sessions as refresh


ROOT = Path(__file__).resolve().parents[1]
DATE = os.environ.get("ESSAY_TOPIC_DATE", "2026-09-04")
SUBJECT = "Essay"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "subject-wide-syllabus"
GRAPHICAL_DIR = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits"
    / "carvaka-graphical-specs" / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = (
    ROOT / "upsc-ai-kit" / "manifests" / "v2"
    / "essay--subject-wide-syllabus.json"
)
LOCAL_BOOKS = [
    ROOT / "books" / "mains" / "UPSC Mains 2024 Essay Paper.pdf",
    ROOT / "books" / "mains" / "UPSC Mains 2025 Essay Paper.pdf",
    ROOT / "books" / "more_previous_papers" / "ESSAY_0.pdf",
    ROOT / "books" / "more_previous_papers" / "ESSAY_1.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM19-Essay.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM-21-ESSAY-110122.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM-22-ESSAY-190922.pdf",
    ROOT / "books" / "more_previous_papers" / "QP-CSM-23-ESSAY-180923.pdf",
]
LOCAL_BOOKS = [path for path in LOCAL_BOOKS if path.is_file()]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Framework.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    KNOWLEDGE / "LEARNING-SESSION-COMMAND-INDEX.md",
    KNOWLEDGE / "REVISION-CHART_Decoding-Arguments-and-Distinctive-Features.md",
    KNOWLEDGE / "ANSWER-WORTHINESS-AUDIT.md",
    KNOWLEDGE / "PYQ-Corpus-2013-2025.md",
]
COMMON_CROSS = [path for path in COMMON_CROSS if path.is_file()]
PYQ_INDEXES = [
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
]
PYQ_INDEXES = [path for path in PYQ_INDEXES if path.is_file()]
_BASE_OWNER_DEPTH = _base._owner_depth

_PLAN_INDEXES = (
    [0, 1], [2], [3], [4], [5], [6, 7], [8], [9], [10], [11],
    [12, 13], [14], [15], [16, 17], [18, 19],
)
_KEYWORD_EXCLUSIONS = {
    "about", "after", "against", "analysis", "answer", "because", "before",
    "between", "claim", "concept", "current", "different", "evidence",
    "exact", "fact", "india", "indian", "limit", "mission", "named",
    "owner", "programme", "question", "essay", "source", "status",
    "topic", "which", "while", "with", "without",
}
REGISTER_HEADINGS = (
    "PROMPT READING AND ARGUMENT MAP",
    "METHOD, EVIDENCE AND OFFICIAL-RULE FIREWALLS",
    "ESSAY-PLANNING AND ANSWER-WRITING SPINE",
    "PYQ WORDING AND OFFICIAL-SOURCE BOUNDARY",
)

SOLUTION_PROFILES = {
    "The empires of the futures will be the empires of the mind.": {
        "thesis": (
            "Future power will depend increasingly on the capacity to create, "
            "organise and democratise knowledge, but an empire of the mind is "
            "legitimate only when intellectual power enlarges freedom rather "
            "than reproducing domination through technology or exclusion."
        ),
        "dimensions": [
            ("Knowledge as power", "Scientific discovery, education and innovation increasingly determine economic and strategic capability."),
            ("Human capital", "A society's schools, universities, skills and public reasoning shape whether demographic scale becomes creative capacity."),
            ("Digital power", "Data, algorithms, platforms and artificial intelligence can influence choices without territorial conquest."),
            ("Culture and ideas", "Languages, narratives, universities and media create durable influence by shaping what societies consider possible or desirable."),
            ("Democratic access", "Knowledge concentration produces a new hierarchy unless digital access, literacy and research opportunities are broadly shared."),
            ("Ethical boundary", "Intellectual leadership becomes imperial domination when surveillance, manipulation or monopoly displaces autonomy."),
        ],
        "counter": "Material resources, geography and military capacity will not disappear; knowledge magnifies these assets rather than making them irrelevant.",
        "conclusion": "The humane empire of the future should therefore be a republic of minds: innovative yet open, powerful yet accountable, and competitive without closing the gates of knowledge.",
    },
    "Social media is triggering 'Fear of Missing Out' amongst the youth precipitating depression and loneliness.": {
        "thesis": (
            "Social media can intensify FOMO by turning social comparison into a "
            "continuous, quantified and commercially amplified experience, yet "
            "youth distress arises from the interaction of platform design, social "
            "conditions and individual vulnerability rather than technology alone."
        ),
        "dimensions": [
            ("Comparison architecture", "Curated highlights make ordinary life appear deficient and convert belonging into a visible competition for attention."),
            ("Attention economy", "Notifications, streaks and algorithmic recommendation reward repeated checking and make absence feel like social loss."),
            ("Loneliness paradox", "High connectivity can coexist with weak intimacy when interaction is performative, fragmented or measured through public approval."),
            ("Unequal vulnerability", "Adolescents facing exclusion, academic pressure or weak support systems may experience the same platforms more harmfully."),
            ("Positive capability", "Online communities can also provide expression, learning and support, especially where offline opportunities are limited."),
            ("Shared responsibility", "Digital literacy, humane platform design, family communication, counselling and accessible mental-health services must work together."),
        ],
        "counter": "Blaming social media alone ignores family stress, unemployment, educational pressure and pre-existing mental-health conditions.",
        "conclusion": "The answer is neither digital abstinence nor technological fatalism, but an online environment in which connection serves human relationships instead of converting them into an endless status contest.",
    },
    "There is no path to happiness, Happiness is the path.": {
        "thesis": (
            "Happiness is not merely a reward postponed until success is achieved; "
            "it is a quality of meaningful, ethical and attentive participation in "
            "life, though this insight must not romanticise deprivation or deny the "
            "material conditions required for dignity."
        ),
        "dimensions": [
            ("Process over destination", "Goals organise effort, but a life spent treating every present moment as a sacrifice can make achievement emotionally empty."),
            ("Meaningful action", "Work, learning and service generate deeper well-being when their daily practice itself expresses purpose."),
            ("Relationships", "Trust, friendship and care are lived processes; they cannot be accumulated later like material assets."),
            ("Ethical conduct", "Means shape character, so happiness pursued through exploitation or dishonesty undermines itself."),
            ("Public policy", "Development must value health, security, community and ecological quality alongside income and output."),
            ("Material floor", "Freedom from hunger, violence and preventable illness is essential; inner attitude cannot substitute for justice."),
        ],
        "counter": "Some hardship is unavoidable and long-term projects require delayed gratification, so happiness cannot mean constant comfort or pleasure.",
        "conclusion": "Happiness becomes the path when purpose, just means and humane relationships inhabit the journey, while society secures the minimum dignity that makes such a journey genuinely possible.",
    },
    "Muddy water is best cleared by leaving it alone.": {
        "thesis": (
            "Restraint can allow disturbed systems to recover when intervention "
            "would amplify confusion, but wise non-action is an active judgment "
            "about timing and self-restraint, not indifference to injustice or danger."
        ),
        "dimensions": [
            ("Psychological clarity", "Pausing before reacting allows anger and anxiety to settle, improving judgment and communication."),
            ("Conflict resolution", "Cooling-off periods can reduce escalation when each intervention is interpreted as provocation."),
            ("Institutions", "Stable rules sometimes work better than constant discretionary interference, which creates uncertainty and rent-seeking."),
            ("Ecological recovery", "Natural regeneration can outperform intrusive engineering where ecosystems retain resilience."),
            ("Limits of non-action", "Violence, discrimination, epidemics and irreversible ecological damage demand timely intervention."),
            ("Criterion for choice", "The decision must compare the harm of intervention with the harm, reversibility and urgency of waiting."),
        ],
        "counter": "Silence can protect the powerful and convert patience into complicity when harm is ongoing or those affected cannot defend themselves.",
        "conclusion": "The wisdom of leaving muddy water alone lies not in worshipping passivity but in learning when restraint restores order and when justice requires decisive action.",
    },
    "Nearly all men can stand adversity, but to test the character, give him power.": {
        "thesis": (
            "Adversity reveals endurance, but power more searchingly reveals "
            "character because it reduces external restraint and exposes whether "
            "authority is treated as public trust, personal entitlement or licence."
        ),
        "dimensions": [
            ("Freedom of choice", "Power expands the consequences of preference and therefore reveals values that hardship may keep hidden."),
            ("Institutional temptation", "Control over appointments, information or resources creates opportunities for favouritism and self-dealing."),
            ("Public trust", "Constitutional office is legitimate when authority remains bounded by law, transparency and accountability."),
            ("Everyday power", "Character is also tested in families, workplaces and social hierarchies where unequal dependence can be exploited."),
            ("Transformative use", "Power can enlarge justice when leaders share credit, protect dissent and strengthen institutions beyond themselves."),
            ("Checks and balances", "Good systems do not rely on virtue alone; they limit discretion and make abuse visible and correctable."),
        ],
        "counter": "Adversity can also reveal cruelty, solidarity or courage, while even decent individuals may be distorted by institutions that reward abuse.",
        "conclusion": "Character under power is proved not by possessing authority modestly in appearance, but by converting authority into accountable service and leaving others more capable of freedom.",
    },
    "Alternative technologies for a climate change resilient India.": {
        "thesis": (
            "Alternative technologies can strengthen India's climate resilience "
            "when they are locally appropriate, affordable and integrated with "
            "institutions and community knowledge; technology is an enabler of "
            "adaptation, not a substitute for ecological planning or social justice."
        ),
        "dimensions": [
            ("Resilient agriculture", "Drought-tolerant crops, micro-irrigation, soil monitoring and weather advisories can reduce climate-sensitive farm losses."),
            ("Distributed energy", "Decentralised renewable systems and storage can support essential services when central networks fail."),
            ("Water security", "Wastewater reuse, aquifer monitoring, rainwater harvesting and efficient treatment expand local buffers."),
            ("Risk information", "Remote sensing, forecasting and last-mile warning systems improve preparedness only when alerts are trusted and actionable."),
            ("Climate-resilient settlements", "Cool roofs, passive design, permeable surfaces and nature-based drainage can reduce heat and flood exposure."),
            ("Justice and capability", "Open standards, local repair skills, finance and public procurement determine whether vulnerable communities can use the technology."),
        ],
        "counter": "Expensive imported systems, energy-intensive solutions and poorly governed infrastructure can create new dependencies or shift risk elsewhere.",
        "conclusion": "India needs not a catalogue of futuristic devices but a resilient technology ecosystem joining science, local institutions, ecological wisdom and equitable access.",
    },
    "Biased media is a real threat to Indian democracy.": {
        "thesis": (
            "Biased media threatens Indian democracy when systematic distortion "
            "deprives citizens of reliable information, weakens scrutiny and "
            "polarises public reason, although viewpoint diversity must be protected "
            "and bias distinguished from mere disagreement."
        ),
        "dimensions": [
            ("Informed citizenship", "Elections are meaningful only when citizens can evaluate competing claims through sufficiently reliable information."),
            ("Accountability", "Selective silence or partisan framing can shield power and make public institutions less answerable."),
            ("Polarisation", "Sensational and identity-driven coverage can replace deliberation with permanent mobilisation against imagined enemies."),
            ("Ownership and incentives", "Concentrated ownership, advertising dependence and attention metrics can shape editorial priorities without explicit censorship."),
            ("Digital amplification", "Algorithmic distribution and misinformation accelerate biased narratives and blur the boundary between journalism and propaganda."),
            ("Democratic safeguards", "Independent regulation, transparency, media literacy, plural ownership and strong public-interest journalism must coexist with free expression."),
        ],
        "counter": "Government control in the name of neutrality can itself become a greater democratic threat, and complete value-neutrality is neither possible nor desirable.",
        "conclusion": "The democratic objective is not a voicelessly neutral press but a plural, transparent and accountable media order in which facts remain contestable without becoming disposable.",
    },
    "Thought finds a world and creates one also.": {
        "thesis": (
            "Thought interprets an inherited reality and simultaneously reshapes it "
            "through imagination, institutions and action; its creative power can "
            "liberate or dominate depending on evidence, ethics and inclusion."
        ),
        "dimensions": [
            ("Perception", "Concepts and language organise experience, helping people notice patterns that would otherwise remain invisible."),
            ("Scientific discovery", "Inquiry finds structures already present in nature while theories and technologies create new fields of human possibility."),
            ("Political imagination", "Ideas such as liberty, equality and constitutionalism first reinterpret injustice and then build institutions to contest it."),
            ("Economic creation", "Entrepreneurship and design transform knowledge into products, work and new forms of exchange."),
            ("Social construction", "Prejudices and stereotypes also create harmful realities by shaping institutions, expectations and self-belief."),
            ("Ethical responsibility", "Because thought has consequences, creativity must remain open to criticism, evidence and those who bear its costs."),
        ],
        "counter": "Thought is constrained by material conditions and cannot create reality by wish alone; imagination becomes effective through collective action and institutions.",
        "conclusion": "Human progress depends on thought that sees the world honestly, imagines it differently and accepts responsibility for the world its imagination helps produce.",
    },
    "Girls are weighed down by restrictions, boys with demands — two equally harmful disciplines.": {
        "thesis": (
            "Patriarchal gender norms harm girls through restricted autonomy and "
            "boys through coercive expectations of strength, success and emotional "
            "silence; the burdens differ in form and power, so equality requires "
            "removing both without falsely equating their consequences."
        ),
        "dimensions": [
            ("Restrictions on girls", "Control over mobility, education, work, clothing and marriage narrows agency and exposes women to structural dependence."),
            ("Demands on boys", "Pressure to earn, dominate, suppress vulnerability and take risks damages mental health and relationships."),
            ("Unequal power", "The two disciplines are mutually reinforcing, but restrictions on girls often carry deeper legal, economic and bodily consequences."),
            ("Family and education", "Homes and schools reproduce norms through different freedoms, chores, subjects, punishments and career expectations."),
            ("Work and care", "Men are pushed toward breadwinning while women carry unpaid care, limiting both shared parenthood and economic equality."),
            ("Transformative equality", "Safety, autonomy, emotional literacy, shared care and freedom from rigid roles should be expanded for every gender."),
        ],
        "counter": "Calling the disciplines equally harmful must not obscure violence, exclusion and material disadvantage disproportionately borne by girls and women.",
        "conclusion": "A just society will neither protect girls by confining them nor prepare boys by hardening them; it will equip all children with autonomy, care and equal responsibility.",
    },
}


def panel(
    title: str,
    structural_type: str,
    lines: list[str],
    source_references: list[str],
) -> tuple[str, str, str, list[str]]:
    """Return one manually authored ASCII/graphical panel definition."""

    return title, structural_type, "\n".join(lines), source_references


def expected_generation(topic_key: str) -> int:
    """Return the append-only generation across legacy and learner variants."""

    return refresh.next_new_topic_generation(refresh.load_tracker(), topic_key)


def make_plans(
    titles: list[str],
    traps: list[str],
    answer_routes: list[str],
) -> list[tuple[str, list[int], str, str]]:
    if len(titles) != 15:
        raise ValueError("Exactly fifteen Essay sessions are required.")
    return [
        (title, list(_PLAN_INDEXES[index]), traps[index % len(traps)],
         answer_routes[index % len(answer_routes)])
        for index, title in enumerate(titles)
    ]


def make_mains(
    facts: list[tuple[str, str]],
    prompts: list[tuple[int, str, list[int]]],
) -> list[tuple[int, str, str, list[int]]]:
    result = []
    for marks, prompt, indexes in prompts:
        selected = [facts[index] for index in indexes]
        model = " ".join(
            (
                f"**Claim:** {label}. **Named evidence/example:** {statement} "
                "**Analysis:** This identifies the exact Essay-method move and "
                "shows how it keeps the response tied to the printed proposition "
                "rather than an adjacent GS topic. **Qualification:** It remains "
                "a repository-audited writing scaffold, not an official UPSC "
                "rubric, compulsory formula or model answer."
            )
            for label, statement in selected
        )
        result.append((marks, prompt, model, indexes))
    return result


def make_pyq_solution(
    facts: list[tuple[str, str]],
    year: str,
    paper: str,
    demand: str,
    status: str,
    indexes: list[int],
) -> tuple[str, str, str, str, str]:
    model = " ".join(
        f"**{facts[index][0]}:** {facts[index][1]}" for index in indexes
    )
    model += (
        " This is a method-focused decoding or application card, not an official "
        "UPSC model answer and not a claim that only one interpretation is valid."
    )
    return year, paper, demand, status, model


def topic(
    number: int,
    title: str,
    source_stem: str,
    facts: list[tuple[str, str]],
    traps: list[str],
    mains_prompts: list[tuple[int, str, list[int]]],
    session_titles: list[str],
    answer_routes: list[str],
    panels: list[tuple[str, str, str, list[str]]],
    required_terms: list[str],
    pyq_note: str,
    pyq_solutions: list[tuple[str, str, str, str, str]],
    live_sources: Iterable[str],
    current_note: str,
    extra: Iterable[str] = (),
    register_headings: tuple[str, str, str, str] | None = None,
    register_answer_spine: Iterable[str] = (),
    allow_existing_history: bool = False,
) -> dict[str, object]:
    key = f"essay-{number:02d}"
    extra = list(extra)
    if len(facts) != 20:
        raise ValueError(f"{key}: exactly twenty source-bounded facts are required.")
    if len(panels) != 12:
        raise ValueError(f"{key}: exactly twelve manual ASCII panels are required.")
    if len(pyq_solutions) != 3:
        raise ValueError(f"{key}: exactly three verified PYQ/application cards are required.")
    live_sources = list(live_sources)
    if len(live_sources) < 3:
        raise ValueError(f"{key}: at least three official live-source attempts are required.")
    if any(
        DATE not in attempt
        or "http" not in attempt
        or not re.search(r"\b(?:attempted|fetched|searched)\b", attempt, re.I)
        for attempt in live_sources
    ):
        raise ValueError(
            f"{key}: every live-source attempt must contain its URL, action and {DATE}."
        )
    official_domains = ("upsc.gov.in",)
    if any(not any(domain in attempt for domain in official_domains) for attempt in live_sources):
        raise ValueError(f"{key}: every live-source attempt must use an official domain.")
    owner_paths = [
        KNOWLEDGE / "basic" / f"{source_stem}.md",
        KNOWLEDGE / "advanced" / f"{source_stem}.md",
        *[KNOWLEDGE / value for value in extra],
    ]
    owner_text = "\n".join(
        path.read_text(encoding="utf-8") for path in owner_paths if path.is_file()
    ).casefold()
    missing_source_terms = [
        term for term in required_terms if term.casefold() not in owner_text
    ]
    if missing_source_terms:
        raise ValueError(
            f"{key}: required terms are not literal owner-source substrings: "
            f"{missing_source_terms}"
        )
    return {
        "number": number,
        "key": key,
        "title": title,
        "basic": KNOWLEDGE / "basic" / f"{source_stem}.md",
        "advanced": KNOWLEDGE / "advanced" / f"{source_stem}.md",
        "canonical": SESSION_DIR / key / f"{key}_Knowledge-Guide.md",
        "extra": [KNOWLEDGE / value for value in extra],
        "facts": facts,
        "traps": traps,
        "mains": make_mains(facts, mains_prompts),
        "session_plans": make_plans(session_titles, traps, answer_routes),
        "panels": panels,
        "required_terms": required_terms,
        "live_sources": live_sources,
        "current_note": current_note,
        "ocr_note": (
            "Repository Markdown was primary. OCR-searchable official UPSC "
            "Essay papers were supplementary only for printed instructions and "
            "V1 prompt wording. No author, official model answer, current marks "
            "split, phase allocation, paragraph count or scoring rubric was inferred."
        ),
        "pyq_note": pyq_note,
        "pyq_solutions": pyq_solutions,
        "register_headings": register_headings or REGISTER_HEADINGS,
        "register_answer_spine": list(register_answer_spine),
        "allow_existing_history": allow_existing_history,
    }


def _session_keywords(title: str, selected: list[tuple[str, str]]) -> list[str]:
    source = " ".join(
        [title, *[label for label, _ in selected], *[text for _, text in selected]]
    )
    result: list[str] = []
    seen: set[str] = set()
    for word in re.findall(r"[A-Za-z][A-Za-z0-9'-]{3,}", source):
        folded = word.casefold().strip("-'")
        if folded in _KEYWORD_EXCLUSIONS or folded in seen:
            continue
        seen.add(folded)
        result.append(word)
        if len(result) == 6:
            break
    if len(result) < 4:
        raise ValueError(f"{title}: fewer than four essay-specific keywords.")
    return result


def _session_fragment(
    config: dict[str, object],
    number: int,
    plan: tuple[str, list[int], str, str],
) -> str:
    title, indexes, caution, exam_use = plan
    facts: list[tuple[str, str]] = config["facts"]
    selected = [facts[index] for index in indexes]
    labels = [label for label, _ in selected]
    joined = ", ".join(labels[:-1]) + (
        f" and {labels[-1]}" if len(labels) > 1 else labels[0]
    )
    keywords = _session_keywords(title, selected)
    visual = [title.upper()]
    for index, label in enumerate(labels, 1):
        visual.append(f"{index:02d}. {label}")
        if index < len(labels):
            visual.extend(("    |", "    v"))
    visual.append(f"STATUS / CATEGORY FIREWALL -> {caution}")
    return (
        f"### SESSION {number} — {_base.phase_for(number)} — {title}\n\n"
        "#### METHOD MOVE / WHAT THIS DOES\n\n"
        f"**Plain-language definition:** {title} explains how {joined} combine "
        "into one usable Essay-planning move.\n\n"
        f"**Technical definition:** The learner fixes the printed prompt, its "
        "relationship or demand, the defensible scope, the argument function "
        "and the evidence boundary before drafting prose.\n\n"
        "#### ANSWER-GRABBING OPENING — WRITE/ADAPT IN THE EXAM\n\n"
        f"> {title} should be applied through {joined}, while preserving the "
        "difference between official paper instruction and strategy, prompt "
        "wording and interpretation, example and evidence, breadth and coherence.\n\n"
        "#### MUST-WRITE KEYWORDS\n\n"
        + "\n".join(f"- **{item}**" for item in keywords)
        + "\n\n**How to use them:** Define the first three terms, trace the "
        "relationship with the next two, and attach the final term to the exact "
        f"claim, example and qualification. Qualification: {caution}\n\n"
        "#### VISUAL FIRST\n\n```text\n"
        + "\n".join(visual)
        + "\n```\n\n*The rail fixes the prompt-to-argument sequence and claim boundary "
        "before explanation.*\n\n#### CORE EXPLANATION\n\n"
        + " ".join(statement for _, statement in selected)
        + "\n\n#### SIMPLE SYSTEM EXAMPLE\n\n"
        + f"Read {title} as a sequence: identify {labels[0]}, follow the "
        "method through the printed proposition, and stop before adding a rule, "
        "attribution, fact or inference the audited sources do not support.\n\n"
        + "#### TECHNICAL DISTINCTION\n\n"
        + f"The decisive boundary is {caution} This keeps {joined} in the "
        "correct prompt, method, argument and evidence category."
        + "\n\n#### NAMED EVIDENCE AND MECHANISM\n\n"
        + "\n".join(f"- {statement}" for _, statement in selected)
        + f"\n\n#### EXAMINER CAUTION\n\n- {caution}\n\n#### EXAM LINK\n\n"
        f"- **Objective practice:** Apply {title} by distinguishing the correct "
        "Essay-method move from nearby but invalid shortcuts; no factual-trivia "
        "recall is being tested.\n"
        f"- **Essay application:** {exam_use}\n\n#### MINI RECAP\n\n"
        f"- **Mechanism chain:** {' -> '.join(labels)}\n"
        f"- **Qualified use:** {exam_use}\n\n#### CLOSING RECALL FLOW\n\n"
        "```closure-flow\n"
        f"START / CONCEPT: {title}\n"
        f"EXACT TERMS: {' | '.join(keywords)}\n"
        f"MECHANISM / ARGUMENT: connect {joined} without changing the prompt or evidence status\n"
        f"CONSEQUENCE / CONTRAST: {exam_use}\n"
        f"UPSC TRAP / ANSWER-USE: {caution}\n"
        "ANSWER-GRABBING FORMULATION: a scaffold is useful only while it serves "
        "the exact proposition and remains qualified\n```"
    )


def _build_mcqs(config: dict[str, object]) -> str:
    facts: list[tuple[str, str]] = config["facts"]
    variants = [
        "Which option applies {label} as an Essay-method distinction?",
        "Which use of {label} stays closest to the printed prompt?",
        "Which statement preserves the strategy-versus-official-rule boundary for {label}?",
        "Which option avoids the standard Essay-method trap about {label}?",
    ]
    distractor_profiles = [
        (
            "Treat {label} as a compulsory UPSC formula even when it distorts the prompt.",
            "Replace {label} with a familiar adjacent GS topic and maximise factual coverage.",
            "Use {label} to add more headings or dimensions without testing coherence.",
        ),
        (
            "Apply {label} only after drafting, when topic drift can no longer be prevented.",
            "Use {label} while dropping the prompt's operator, qualifier or scale.",
            "Let a striking anecdote or quotation determine {label} regardless of thesis fit.",
        ),
        (
            "Present {label} as an official marking rule rather than a pedagogical scaffold.",
            "Use {label} to avoid stating a serious counter-case or qualification.",
            "Support {label} with an unverified statistic, attribution or current claim.",
        ),
        (
            "Maximise the number of outputs produced by {label}, even if they repeat one claim.",
            "Allow an exception discovered through {label} to replace the central proposition.",
            "Silently tidy the printed prompt before applying {label} to make it easier to answer.",
        ),
    ]
    blocks = []
    for fact_index, (label, statement) in enumerate(facts):
        for variant_index, template in enumerate(variants):
            number = fact_index * 4 + variant_index + 1
            answer = "ABCD"[(number - 1) % 4]
            distractors = [
                value.format(label=label)
                for value in distractor_profiles[variant_index]
            ]
            choices = {answer: statement}
            for letter, distractor in zip(
                [letter for letter in "ABCD" if letter != answer], distractors
            ):
                choices[letter] = distractor
            blocks.append(
                f"### Q{number}. {template.format(label=label)}\n\n"
                + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
                + f"\n\n**Answer: {answer}.**\n"
                f"**Explanation:** {statement} The other options convert a "
                "qualified writing method into an official formula, permit topic "
                "drift, or reward quantity without coherence and evidence safety."
            )
    return "\n\n".join(blocks)


def _owner_depth(path: Path, *, exclude_pyq: bool) -> str:
    return _BASE_OWNER_DEPTH(path, exclude_pyq=exclude_pyq)


def _audited_pyq_section(config: dict[str, object], _blocks: list[str]) -> str:
    text = "### AUDITED TOPIC-SPECIFIC PYQ OWNERSHIP\n\n" + str(config["pyq_note"])
    for number, (year, paper, demand, status, model) in enumerate(
        config["pyq_solutions"], 1
    ):
        text += (
            f"\n\n### PYQ DEMAND CARD {number} — {year} {paper}\n\n"
            f"**Demand:** {demand}\n\n**Status:** {status}\n\n"
            f"**Model solution:** {model}"
        )
    full_models = list(config.get("full_model_essays", []))
    if full_models:
        text += "\n\n### COMPLETE MODEL ESSAYS\n"
        for number, model in enumerate(full_models, 1):
            text += (
                f"\n\n#### COMPLETE MODEL ESSAY {number} — {model['label']}\n\n"
                f"**Prompt:** {model['prompt']}\n\n"
                f"**Verification:** {model['verification']}\n\n"
                f"**Model essay ({model['word_count']} words):**\n\n"
                f"{model['essay']}"
            )
    return text


def _register_notes(config: dict[str, object]) -> str:
    headings = tuple(config["register_headings"])
    facts = "\n".join(
        f"{number}. **{label}:** {statement}"
        for number, (label, statement) in enumerate(config["facts"], 1)
    )
    traps = "\n".join(f"- {trap}" for trap in config["traps"])
    spine = list(config["register_answer_spine"])
    return (
        f"### {config['title']}: {headings[0]}\n\n{facts}\n\n"
        f"### {config['title']}: {headings[1]}\n\n{traps}\n\n"
        f"### {config['title']}: {headings[2]}\n\n```text\n"
        + "\n-> ".join(spine)
        + "\n```\n\n"
        f"### {config['title']}: {headings[3]}\n\n{config['current_note']}"
    )


def _live_source_audit(config: dict[str, object]) -> str:
    return (
        "### LIVE OFFICIAL-SOURCE ATTEMPT LOG\n\n"
        f"The checks below were made on {DATE}. Substantive official text "
        "is used only for the proposition it supports; title-only, blocked or "
        "thin pages are recorded and supply no factual claim.\n\n"
        + "\n".join(f"- {item}" for item in config["live_sources"])
    )


def _source_audit(config: dict[str, object]) -> str:
    return (
        "### SOURCE, PROGRESSION AND OFFICIAL-RULE AUDIT\n\n"
        f"- **Generation date:** {DATE}.\n"
        "- **Source order:** canonical Basic owner first; Advanced owner second; "
        "Essay master framework, README, official-syllabus map, answer-worthiness "
        "audit and revision chart next; PYQ corpus and official OCR papers after "
        "that; live official UPSC pages only as a final check.\n"
        "- **Basic/Advanced boundary:** complete Basic teaching remains first and "
        "Advanced material remains optional and last.\n"
        f"- **OCR boundary:** {config['ocr_note']}\n"
        "- **Qdrant:** not used; repository Markdown and local official papers "
        "were sufficient.\n"
        f"- **PYQ integrity:** {config['pyq_note']}\n"
        f"- **Live-source boundary:** {config['current_note']}\n"
        "- **No-formula rule:** strategy, heuristics and practice weights are "
        "never presented as official UPSC instructions or marking criteria."
    )


def _assemble(
    config: dict[str, object],
    ascii_path: Path,
) -> tuple[str, str, int]:
    sessions = [
        _session_fragment(config, number, plan)
        for number, plan in enumerate(config["session_plans"], 1)
    ]
    mcqs = _build_mcqs(config)
    practice = (
        _audited_pyq_section(config, [])
        + "\n\n" + _base.original_mains_section(config)
    )
    manual = ascii_master.normalize_manual_spec_file(ascii_path)
    ascii_fragment = ascii_master.build_manual_fragment(manual[str(config["key"])])
    markdown = (
        f"# {config['title']} — Learner-v2 Complete Learning Session\n\n"
        f"> **Authoring-only generation:** {DATE}. No PDF was rendered and no "
        "tracker or index was mutated.\n\n"
        + _source_audit(config)
        + "\n\n" + _live_source_audit(config)
        + "\n\n## BASIC LEARNING SESSION\n\n"
        + "\n\n".join(sessions)
        + "\n\n### COMPLETE BASIC OWNER EVIDENCE BANK\n\n"
        + _owner_depth(Path(config["basic"]), exclude_pyq=True)
        + "\n\n## BASIC MCQS / REMEDIATION\n\n" + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n" + practice
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + _owner_depth(Path(config["advanced"]), exclude_pyq=True)
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + _register_notes(config)
        + "\n\n### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + ascii_fragment + "\n"
    )
    workbook = (
        f"# {config['title']} — Solved Practice Workbook\n\n"
        f"> **Authoring-only generation:** {DATE}. Uses the same source-bounded "
        "essay distinctions and strict A-B-C-D rotation.\n\n"
        "## BASIC MCQS / REMEDIATION\n\n" + mcqs
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n" + practice + "\n"
    )
    return markdown, workbook, len(sessions)


def ensure_section_manifest() -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    manifest = json.loads(SECTION_MANIFEST.read_text(encoding="utf-8"))
    catalog_keys = [
        item["topic_key"]
        for item in catalog["topics"]
        if str(item.get("topic_key", "")).startswith("essay-")
    ]
    manifest_keys = [item["topic_key"] for item in manifest["topics"]]
    if manifest_keys != catalog_keys or len(manifest_keys) != 16:
        raise ValueError("Essay section manifest must contain all 16 catalogue topics in order.")
    return SECTION_MANIFEST


def validate_catalog(topics: list[dict[str, object]]) -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    keys = {item.get("topic_key") for item in catalog["topics"]}
    missing = [config["key"] for config in topics if config["key"] not in keys]
    if missing:
        raise ValueError(f"Essay topics missing from catalogue: {missing}")


def _write_graphical_spec(
    config: dict[str, object],
    markdown: str,
    ascii_path: Path,
) -> Path:
    panels = [
        {
            "title": title,
            "body": body,
            "structural_type": kind,
            "source_references": references,
        }
        for title, kind, body, references in config["panels"]
    ]
    source_path = SESSION_DIR / f"{config['key']}_Learning-Session.md"
    spec = carvaka_flowchart.author_topic_spec(
        topic_key=str(config["key"]),
        subject=SUBJECT,
        title=str(config["title"]),
        source_markdown=markdown.replace("…", ""),
        source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ascii_path.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ascii_path.read_bytes()).hexdigest(),
        panels=panels,
        source_generation=expected_generation(str(config["key"])),
    )
    errors = carvaka_flowchart.validate_spec(spec)
    if errors:
        raise carvaka_flowchart.CarvakaError(" | ".join(errors))
    if len(spec["stages"]) != 13:
        raise ValueError(f"{config['key']}: expected thirteen graphical stages.")
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{config['key']}.json"
    output.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def _write_generation_spec(
    config: dict[str, object],
    source_path: Path,
    workbook_path: Path,
    graphical_path: Path,
    ascii_path: Path,
) -> Path:
    sources = [
        Path(config["basic"]), Path(config["advanced"]), Path(config["canonical"]),
        *[Path(path) for path in config["extra"]], source_path, workbook_path,
        SECTION_MANIFEST, CATALOG, ascii_path, graphical_path,
        *COMMON_CROSS, *PYQ_INDEXES, *LOCAL_BOOKS,
    ]
    sources = list(dict.fromkeys(sources))
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing Essay sources: " + ", ".join(missing))
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        item for item in catalog["topics"] if item.get("topic_key") == config["key"]
    )
    generation = expected_generation(str(config["key"]))
    payload = {
        "schema_version": 1,
        "topic_key": config["key"],
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "topic_folder": config["key"],
        "title": config["title"],
        "variant": "learner-v2",
        "generation": generation,
        "expected_generation": generation,
        "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "source_markdown": str(source_path.relative_to(ROOT)),
        "workbook_markdown": str(workbook_path.relative_to(ROOT)),
        "source_basic": str(Path(config["basic"]).relative_to(ROOT)),
        "source_canonical": str(Path(config["canonical"]).relative_to(ROOT)),
        "source_advanced": str(Path(config["advanced"]).relative_to(ROOT)),
        "manifest": str(SECTION_MANIFEST.relative_to(ROOT)),
        "cross_topic_sources": [
            str(path.relative_to(ROOT))
            for path in [*COMMON_CROSS, *map(Path, config["extra"])]
        ],
        "local_ocr_sources": [str(path.relative_to(ROOT)) for path in LOCAL_BOOKS],
        "pyq_indexes": [str(path.relative_to(ROOT)) for path in PYQ_INDEXES],
        "official_question_sources": [
            str(path.relative_to(ROOT)) for path in LOCAL_BOOKS
        ],
        "live_sources": config["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": (
            "80 unique Essay-method MCQs with A/B/C/D at 20 each; three "
            "verified PYQ/application cards; six solved original answer-writing "
            "prompts weighted 10,10,15,15,20,20; complete model essays; final "
            "topic-specific register notes."
        ),
        "pyq_status_note": config["pyq_note"],
        "current_linkage_note": config["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "supersedes": (
            "essay-01:legacy-v1:g1"
            if config["key"] == "essay-01" else None
        ),
        "tracker_untouched": True,
        "allow_existing_history": bool(config["allow_existing_history"]),
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{config['key']}-new-topic-{DATE}.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


@contextmanager
def _configured() -> Iterator[None]:
    names = {
        "ROOT": ROOT, "DATE": DATE, "SUBJECT": SUBJECT, "KNOWLEDGE": KNOWLEDGE,
        "SESSION_DIR": SESSION_DIR, "GRAPHICAL_DIR": GRAPHICAL_DIR,
        "EXPORT_DIR": EXPORT_DIR, "CATALOG": CATALOG,
        "SECTION_MANIFEST": SECTION_MANIFEST, "LOCAL_BOOKS": LOCAL_BOOKS,
        "COMMON_CROSS": COMMON_CROSS, "PYQ_INDEXES": PYQ_INDEXES,
        "ensure_section_manifest": ensure_section_manifest,
        "validate_catalog": validate_catalog,
        "write_graphical_spec": _write_graphical_spec,
        "write_generation_spec": _write_generation_spec,
        "assemble": _assemble, "build_mcqs": _build_mcqs,
        "_owner_depth": _owner_depth, "_session_fragment": _session_fragment,
        "solved_pyq_section": _audited_pyq_section,
        "source_audit": _source_audit,
    }
    previous = {name: getattr(_base, name) for name in names}
    try:
        for name, value in names.items():
            setattr(_base, name, value)
        yield
    finally:
        for name, value in previous.items():
            setattr(_base, name, value)


def _owner_text(path: Path) -> str:
    """Return the complete owner text without duplicating its top-level title."""

    text = path.read_text(encoding="utf-8").strip()
    return re.sub(r"\A# .+?\n+", "", text, count=1)


def _pyq_is_essay_topic(paper: str) -> bool:
    return paper.strip().casefold() == "essay"


def _solution_components(model: str) -> list[tuple[str, str]]:
    body = model.split(
        " This is a method-focused decoding or application card", 1
    )[0]
    return [
        (label.strip(), statement.strip())
        for label, statement in re.findall(
            r"\*\*(.+?):\*\*\s*(.+?)(?=\s+\*\*.+?:\*\*|\Z)",
            body,
        )
    ]


def _complete_solution(
    number: int,
    year: str,
    paper: str,
    demand: str,
    status: str,
    model: str,
) -> str:
    components = _solution_components(model)
    profile = SOLUTION_PROFILES.get(demand)
    claims = "\n".join(
        f"{index}. **{label}:** {statement}"
        for index, (label, statement) in enumerate(components, 1)
    )
    if profile:
        thesis = str(profile["thesis"])
        dimensions = list(profile["dimensions"])
        body = "\n\n".join(
            f"**{label}.** {paragraph}" for label, paragraph in dimensions
        )
        counter = str(profile["counter"])
        conclusion = str(profile["conclusion"])
    else:
        thesis = (
            "The answer should apply the audited paper boundary and distinguish "
            "official instruction from candidate strategy."
        )
        body = "\n\n".join(
            f"**{label}.** {statement}" for label, statement in components
        )
        counter = (
            "A dated paper instruction must not be projected unchanged onto a "
            "future paper without checking that year's official document."
        )
        conclusion = (
            "Paper compliance begins with the current printed instruction; all "
            "selection grids and time divisions remain non-official strategy."
        )
    thesis_terms = ", ".join(label for label, _ in components[:4])
    return (
        f"## SOLUTION {number} — {year} {paper}\n\n"
        f"### Question\n\n{demand}\n\n"
        f"### Verification status\n\n{status}\n\n"
        "### Prompt reading and central thesis\n\n"
        f"**Working thesis:** {thesis}\n\n"
        f"**Method controls:** Integrate {thesis_terms} while remaining open to "
        "qualification, counter-reading and limits. This is a repository-authored "
        "model, not an official UPSC answer or compulsory formula.\n\n"
        "### Complete brainstorming and argument map\n\n"
        f"{claims}\n\n"
        "### Suggested essay architecture\n\n"
        "1. Open by restating the proposition in plain language without invented attribution.\n"
        "2. Define the operative terms and state a qualified thesis.\n"
        "3. Develop each distinct claim through mechanism, evidence and analysis.\n"
        "4. Introduce the strongest counter-view or limiting condition.\n"
        "5. Synthesize the competing insights instead of ending with a catalogue.\n"
        "6. Conclude by returning to the proposition at a deeper level.\n\n"
        "### Model solution\n\n"
        f"**Introduction.** “{demand}” is best approached as a proposition to "
        "be interpreted and defended, not as a cue for unrelated factual display. "
        f"{thesis}\n\n"
        f"{body}\n\n"
        f"**Counter-view and qualification.** {counter}\n\n"
        f"**Conclusion.** {conclusion}"
    )


def _method_appendix(config: dict[str, object]) -> str:
    blocks = []
    for number, (marks, prompt, thesis, indexes) in enumerate(config["mains"], 1):
        evidence = "\n".join(
            f"- {config['facts'][index][1]}" for index in indexes
        )
        blocks.append(
            f"### METHOD DRILL {number} — {marks} MARKS\n\n"
            f"**Question:** {prompt}\n\n"
            f"**Model response:** {thesis}\n\n"
            f"**Complete evidence and reasoning bank:**\n\n{evidence}"
        )
    return "\n\n".join(blocks)


def _assemble_essay_package(
    config: dict[str, object],
) -> tuple[str, str, str]:
    solved = [
        _complete_solution(number, *item)
        for number, item in enumerate(config["pyq_solutions"], 1)
    ]
    practice_items = [
        item for item in config["pyq_solutions"] if _pyq_is_essay_topic(item[1])
    ]
    workbook_questions = "\n\n".join(
        (
            f"## TOPIC {number} — {year}\n\n"
            f"{demand}\n\n"
            "**Attempt independently:** Plan first, then write a complete Essay. "
            "Do not consult the separate solutions document before finishing."
        )
        for number, (year, _paper, demand, _status, _model) in enumerate(
            practice_items, 1
        )
    )
    practice_solutions = [
        _complete_solution(number, *item)
        for number, item in enumerate(practice_items, 1)
    ]
    guide = (
        f"# {config['title']} — Complete Essay Knowledge Guide\n\n"
        "> Essay-specific format: one continuous guide, no artificial learning "
        "sessions and no MCQs. The complete Basic and Advanced owner material is "
        "preserved below, followed by solved UPSC questions and retained method drills.\n\n"
        "## HOW TO USE THIS GUIDE\n\n"
        "Read the concise orientation first, study the complete Basic and Advanced "
        "material, then work through the solved UPSC questions. Use the separate "
        "workbook only after understanding the method.\n\n"
        + _source_audit(config)
        + "\n\n" + _live_source_audit(config)
        + "\n\n## COMPLETE BASIC KNOWLEDGE\n\n"
        + _owner_text(Path(config["basic"]))
        + "\n\n## COMPLETE ADVANCED KNOWLEDGE\n\n"
        + _owner_text(Path(config["advanced"]))
        + "\n\n## SOLVED UPSC QUESTIONS\n\n"
        + "\n\n".join(solved)
        + "\n\n## RETAINED METHOD DRILLS AND SOLUTIONS\n\n"
        + _method_appendix(config)
        + "\n\n## CONSOLIDATED REVISION GUIDE\n\n"
        + _register_notes(config)
        + "\n"
    )
    workbook = (
        f"# {config['title']} — Essay Practice Workbook\n\n"
        "> Question-only workbook. Solutions are intentionally placed in a "
        "separate document.\n\n"
        "## ATTEMPT INSTRUCTIONS\n\n"
        "1. Decode or scope the topic before brainstorming.\n"
        "2. Write a qualified thesis and argument map.\n"
        "3. Draft a complete essay with counter-view and synthesis.\n"
        "4. Compare with the separate solution only after completion.\n\n"
        "## UPSC ESSAY TOPICS\n\n"
        + workbook_questions + "\n"
    )
    solutions = (
        f"# {config['title']} — Essay Practice Solutions\n\n"
        "> Separate solutions for the question-only practice workbook. These are "
        "repository-authored models, not official UPSC model answers.\n\n"
        + "\n\n".join(practice_solutions) + "\n"
    )
    return guide, workbook, solutions


def _write_essay_generation_spec(
    config: dict[str, object],
    guide_path: Path,
    workbook_path: Path,
    solutions_path: Path,
) -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        item for item in catalog["topics"] if item.get("topic_key") == config["key"]
    )
    sources = list(
        dict.fromkeys(
            [
                Path(config["basic"]),
                Path(config["advanced"]),
                *[Path(path) for path in config["extra"]],
                *COMMON_CROSS,
                *PYQ_INDEXES,
                *LOCAL_BOOKS,
            ]
        )
    )
    generation = expected_generation(str(config["key"]))
    payload = {
        "schema_version": 2,
        "topic_key": config["key"],
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "title": config["title"],
        "variant": "learner-v2",
        "format": "essay-specific-guide-v1",
        "generation": generation,
        "expected_generation": generation,
        "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "knowledge_guide_markdown": str(guide_path.relative_to(ROOT)),
        "workbook_markdown": str(workbook_path.relative_to(ROOT)),
        "solutions_markdown": str(solutions_path.relative_to(ROOT)),
        "source_basic": str(Path(config["basic"]).relative_to(ROOT)),
        "source_advanced": str(Path(config["advanced"]).relative_to(ROOT)),
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "live_sources": config["live_sources"],
        "practice_profile": (
            "No MCQs and no learning sessions; one complete knowledge guide with "
            "solved UPSC questions, one question-only Essay workbook, and one "
            "separate solutions document."
        ),
        "tracker_untouched": True,
        "approved": False,
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{config['key']}-essay-guide-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def self_check(
    config: dict[str, object],
    guide: str,
    workbook: str,
    solutions: str,
) -> None:
    key = str(config["key"])
    if re.search(r"(?im)^### SESSION \d+", guide):
        raise ValueError(f"{key}: learning-session headings remain.")
    if re.search(r"(?im)^### Q\d+\.", guide + workbook + solutions):
        raise ValueError(f"{key}: MCQs remain in the Essay package.")
    for owner in (Path(config["basic"]), Path(config["advanced"])):
        owner_body = _owner_text(owner)
        if owner_body not in guide:
            raise ValueError(f"{key}: complete owner text was not preserved: {owner}")
    essay_questions = sum(
        _pyq_is_essay_topic(item[1]) for item in config["pyq_solutions"]
    )
    if workbook.count("## TOPIC ") != essay_questions:
        raise ValueError(f"{key}: workbook question count mismatch.")
    if solutions.count("## SOLUTION ") != essay_questions:
        raise ValueError(f"{key}: solutions count mismatch.")
    if guide.count("## SOLUTION ") != len(config["pyq_solutions"]):
        raise ValueError(f"{key}: solved UPSC question count mismatch.")
    if len(config["mains"]) != guide.count("### METHOD DRILL "):
        raise ValueError(f"{key}: retained method-drill coverage mismatch.")
    missing = [
        term for term in config["required_terms"]
        if term.casefold() not in guide.casefold()
    ]
    if missing:
        raise ValueError(f"{key}: required terms missing: {missing}")


def run_batch(
    *,
    topics: list[dict[str, object]],
    ascii_path: Path,
    scope: str,
    previous: ModuleType | None = None,
    previous_keys: list[str] | None = None,
) -> int:
    del ascii_path, scope
    validate_catalog(topics)
    ensure_section_manifest()
    if previous is not None:
        actual = [str(config["key"]) for config in previous.TOPICS]
        if actual != (previous_keys or []):
            raise ValueError(
                f"Previous Essay batch changed: {actual} != {previous_keys or []}"
            )
    for config in topics:
        key = str(config["key"])
        folder = SESSION_DIR / key
        folder.mkdir(parents=True, exist_ok=True)
        guide, workbook, solutions = _assemble_essay_package(config)
        guide_path = folder / f"{key}_Knowledge-Guide.md"
        workbook_path = folder / f"{key}_Practice-Workbook.md"
        solutions_path = folder / f"{key}_Practice-Solutions.md"
        guide_path.write_text(guide, encoding="utf-8")
        workbook_path.write_text(workbook, encoding="utf-8")
        solutions_path.write_text(solutions, encoding="utf-8")
        Path(config["canonical"]).write_text(guide, encoding="utf-8")
        _write_essay_generation_spec(
            config, guide_path, workbook_path, solutions_path
        )
        self_check(config, guide, workbook, solutions)
        print(
            f"{key}: one complete guide; "
            f"{workbook.count('## TOPIC ')} practice topics; separate solutions; "
            "sessions=0; mcqs=0; tracker=untouched"
        )
    return 0
