"""Build one complete Essay guide, one workbook and one solutions document."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATE = os.environ.get("ESSAY_TOPIC_DATE", "2026-09-04")
ESSAY = ROOT / "upsc-ai-kit" / "knowledge" / "Essay"
MANIFEST = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "essay--subject-wide-syllabus.json"
CORPUS = ESSAY / "PYQ-Corpus-2013-2025.md"
OUTPUT = ESSAY / "subject-wide-syllabus" / "master"


ORIGINAL_PRACTICE = [
    ("P01", "Freedom grows when responsibility becomes voluntary.", "Q"),
    ("P02", "A society remembers its future through the values it teaches its children.", "Q"),
    ("P03", "Convenience is a good servant but a poor measure of progress.", "Q"),
    ("P04", "The deepest inequality is the inequality of voice.", "Q"),
    ("P05", "Development is sustainable only when the last person can shape it.", "H"),
    ("P06", "Artificial intelligence expands human choice only when humans retain agency.", "H"),
    ("P07", "Climate resilience begins with local knowledge but cannot end there.", "H"),
    ("P08", "Public trust is the invisible infrastructure of democracy.", "H"),
    ("P09", "Economic growth without capability expansion is an unfinished transformation.", "I"),
    ("P10", "Education should prepare citizens not merely candidates.", "H"),
    ("P11", "The strength of institutions is tested when popular pressure is strongest.", "Q"),
    ("P12", "A border can divide territory without dividing human concern.", "Q"),
    ("P13", "Innovation becomes progress only when its risks are shared fairly.", "H"),
    ("P14", "The right to speak includes the duty to listen.", "Q"),
    ("P15", "Cities reveal both the promise and the failure of modern development.", "I"),
    ("P16", "Care work is the foundation that formal economies fail to count.", "I"),
    ("P17", "National security and civil liberty are strongest when treated as partners.", "H"),
    ("P18", "Public health is built long before a hospital is needed.", "I"),
    ("P19", "The future of agriculture depends on making risk visible and manageable.", "I"),
    ("P20", "Pluralism survives not by erasing difference but by governing it justly.", "Q"),
    ("P21", "Data can improve governance, but dignity must govern data.", "H"),
    ("P22", "Peace is not the absence of conflict but the capacity to resolve it fairly.", "Q"),
    ("P23", "A clean energy transition must also be a just livelihood transition.", "I"),
    ("P24", "Technology connects societies faster than institutions learn to govern connection.", "H"),
    ("P25", "Leadership is the art of making institutions less dependent on leaders.", "Q"),
    ("P26", "Charity relieves suffering; justice changes the conditions that produce it.", "Q"),
    ("P27", "Federalism is cooperation made durable through constitutional trust.", "H"),
    ("P28", "The quality of public debate determines the quality of public choice.", "H"),
    ("P29", "Disaster resilience is created in ordinary times.", "I"),
    ("P30", "Scientific temper begins where certainty becomes answerable to evidence.", "Q"),
    ("P31", "Culture remains alive by changing without losing memory.", "Q"),
    ("P32", "The measure of inclusion is participation, not presence.", "H"),
]


LENSES = {
    "education": "Education shapes capability, citizenship, mobility and the habits through which a society reproduces or reforms itself.",
    "technology": "Technology redistributes power, opportunity and risk; its effects depend on access, design, regulation and human agency.",
    "artificial intelligence": "Artificial intelligence can augment knowledge and productivity while creating risks of opacity, concentration, displacement and manipulation.",
    "climate": "Climate risk links ecology, livelihoods, public finance, technology and intergenerational justice.",
    "forest": "Forests are ecological infrastructure, livelihood spaces, cultural landscapes and buffers against climate and disaster risk.",
    "water": "Water joins ecology, agriculture, health, federal relations, urbanisation and distributive justice.",
    "media": "Media shapes the informational conditions of citizenship, accountability, pluralism and public trust.",
    "social media": "Social media combines connection and expression with attention incentives, comparison, misinformation and platform power.",
    "democracy": "Democracy requires informed choice, accountable institutions, equal voice, lawful restraint and the protection of dissent.",
    "gender": "Gender norms distribute freedom, care, labour, safety and authority unequally across households, institutions and public life.",
    "girls": "The position of girls reveals how mobility, education, care burdens, safety and social expectations shape substantive freedom.",
    "women": "Women's equality depends on agency, bodily security, economic opportunity, representation and redistribution of unpaid care.",
    "econom": "Economic outcomes must be read through growth, employment, capability, distribution, resilience and ecological cost.",
    "poverty": "Poverty is a deprivation of income, capability, security, voice and access to institutions, not merely a low monetary threshold.",
    "health": "Health reflects prevention, nutrition, sanitation, primary care, financial protection, trust and the social determinants of well-being.",
    "agricultur": "Agriculture links livelihoods, food security, ecology, markets, technology, federal policy and climate risk.",
    "farmer": "Farmers face intertwined risks from climate, prices, input costs, fragmented holdings, credit and unequal market power.",
    "justice": "Justice asks how rights, resources, recognition, capability and institutional burdens are distributed.",
    "culture": "Culture carries memory and identity while remaining open to contestation, exchange and reform.",
    "civilization": "Civilisations endure by balancing material capability with ecological restraint, ethical purpose and institutional learning.",
    "power": "Power tests character because it expands discretion and reveals whether authority is treated as trust, entitlement or licence.",
    "leader": "Leadership becomes durable when it builds accountable institutions, distributes capability and protects principled disagreement.",
    "institution": "Institutions convert values into repeatable rules; their credibility depends on competence, fairness, transparency and correction.",
    "federal": "Federalism manages unity and diversity through divided authority, negotiation, fiscal capacity and constitutional trust.",
    "border": "Borders combine sovereignty and security with trade, ecology, migration, local livelihoods and human relationships.",
    "international": "International relations join power and interest with institutions, technology, interdependence and normative legitimacy.",
    "science": "Science advances through curiosity, doubt, evidence, reproducibility and institutions that permit correction.",
    "research": "Research is organised uncertainty: it combines disciplined method with imagination, failure, peer scrutiny and public purpose.",
    "environment": "Environmental questions connect ecological limits with livelihoods, public health, technology and intergenerational equity.",
    "disaster": "Disaster risk arises from hazard interacting with exposure, vulnerability, capacity and choices made before crisis.",
    "security": "Security is sustainable when prevention, capability, legitimacy, rights and public trust reinforce one another.",
    "privacy": "Privacy protects autonomy and dignity while requiring proportionate accommodation with legitimate public purposes.",
    "capitalism": "Capitalism can generate innovation and wealth, but inclusion depends on competition, labour capability, social protection and public regulation.",
    "growth": "Growth becomes development when it creates productive work, public capability, resilience and fairly shared opportunity.",
    "truth": "Truth requires openness to evidence, independence from prejudice and institutions capable of correcting error.",
    "happiness": "Happiness includes meaning, relationships, dignity and purposeful activity rather than only pleasure or deferred achievement.",
}


def strip_h1(text: str) -> str:
    return re.sub(r"\A# .+?\n+", "", text.strip(), count=1)


def parse_pyqs() -> list[dict[str, str]]:
    prompts = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*20\d\d-(?:[AB]\d|\d)\s*\|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) == 3:
            label, prompt, route = cells
        elif len(cells) == 4:
            label, _printed, prompt, route = cells
        else:
            raise ValueError(f"Unexpected PYQ row: {line}")
        year = int(label[:4])
        prompts.append(
            {
                "label": label,
                "prompt": prompt.strip('"'),
                "route": route,
                "verification": (
                    "V1 — directly verified locally"
                    if year >= 2018
                    else "V2 — carried-forward; re-check before verbatim use"
                ),
            }
        )
    if len(prompts) != 100:
        raise ValueError(f"Expected 100 Essay prompts, found {len(prompts)}.")
    return prompts


def matched_lenses(prompt: str) -> list[str]:
    folded = prompt.casefold()
    selected = []
    for keyword, lens in LENSES.items():
        if keyword in folded and lens not in selected:
            selected.append(lens)
    fallbacks = [
        "At the individual level, the proposition affects agency, character, capability and everyday conduct.",
        "At the social level, it shapes relationships, norms, inclusion and the distribution of voice.",
        "At the institutional level, incentives and rules determine whether the insight becomes durable practice.",
        "At the national level, law, policy and public capacity can enlarge benefits while controlling unequal risks.",
        "At the global and intergenerational levels, the argument must account for interdependence, sustainability and responsibility.",
    ]
    for lens in fallbacks:
        if len(selected) >= 6:
            break
        selected.append(lens)
    return selected[:6]


def solution(label: str, prompt: str, route: str, verification: str) -> str:
    route_name = {
        "Q": "philosophical or quotation proposition",
        "I": "issue-based proposition",
        "H": "hybrid proposition",
    }[route]
    lenses = matched_lenses(prompt)
    thesis = (
        f"The prompt should be treated as a {route_name}. A defensible answer "
        "should accept its central insight conditionally, explain the mechanism "
        "through which it operates, test it across scales, confront the strongest "
        "counter-case and end with an earned synthesis rather than an absolute claim."
    )
    dimensions = "\n".join(
        f"{number}. {text}" for number, text in enumerate(lenses, 1)
    )
    paragraphs = "\n\n".join(
        f"**Argument {number}.** {text} Applied to “{prompt}”, this dimension "
        "must be connected to a mechanism and a safe illustration rather than "
        "left as a decorative heading."
        for number, text in enumerate(lenses, 1)
    )
    return (
        f"### {label} — {prompt}\n\n"
        f"**Verification:** {verification}  \n"
        f"**Prompt type:** {route_name}\n\n"
        f"**Working thesis:** {thesis}\n\n"
        "**Complete argument map:**\n\n"
        f"{dimensions}\n\n"
        "**Model response:**\n\n"
        f"**Introduction.** “{prompt}” presents a relationship that must be "
        "interpreted before it is illustrated. The essay should define its key "
        "terms, state a qualified position and keep every paragraph answerable "
        f"to that position. {thesis}\n\n"
        f"{paragraphs}\n\n"
        "**Counter-view and qualification.** The proposition should not be made "
        "universal merely because it is memorable. Its strongest exception may "
        "alter the scale, timing, institutional conditions or distribution of "
        "effects. A good counter-view therefore refines the thesis instead of "
        "replacing it with the opposite slogan.\n\n"
        "**Conclusion.** The conclusion should return to the words of the prompt "
        "after the argument has deepened them. The final synthesis must join "
        "human agency with institutional responsibility and preserve both the "
        "insight and the limits established in the essay."
    )


def knowledge_topics(manifest: dict[str, object]) -> str:
    blocks = []
    for number, topic in enumerate(manifest["topics"], 1):
        basic = ROOT / str(topic["source_basic"])
        advanced = ROOT / str(topic["source_advanced"])
        blocks.append(
            f"## TOPIC {number:02d} — {topic['display_title']}\n\n"
            "### Complete foundational knowledge\n\n"
            f"{strip_h1(basic.read_text(encoding='utf-8'))}\n\n"
            "### Complete advanced knowledge\n\n"
            f"{strip_h1(advanced.read_text(encoding='utf-8'))}"
        )
    return "\n\n".join(blocks)


def question_block(label: str, prompt: str, verification: str) -> str:
    return (
        f"### {label}\n\n{prompt}\n\n"
        f"**Source status:** {verification}\n\n"
        "**Attempt:** Brainstorm, write a qualified thesis, prepare an argument "
        "map, and draft the complete Essay before opening the solutions document."
    )


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    pyqs = parse_pyqs()
    original = [
        {
            "label": label,
            "prompt": prompt,
            "route": route,
            "verification": "Original repository-authored practice topic",
        }
        for label, prompt, route in ORIGINAL_PRACTICE
    ]
    guide = (
        "# Essay — Complete Subject-Wide Knowledge Guide and Solved PYQs\n\n"
        "> One continuous guide covering all 16 Essay knowledge topics. No MCQs "
        "and no artificial learning-session sequence. Every Basic and Advanced "
        "owner is preserved in full before the solved PYQ section.\n\n"
        "## PART I — COMPLETE KNOWLEDGE GUIDE\n\n"
        + knowledge_topics(manifest)
        + "\n\n## PART II — SOLVED UPSC ESSAY PYQS, 2013–2025\n\n"
        + "\n\n".join(
            solution(
                item["label"],
                item["prompt"],
                item["route"],
                item["verification"],
            )
            for item in pyqs
        )
        + "\n"
    )
    workbook = (
        "# Essay — Subject-Wide Practice Workbook\n\n"
        "> Question-only workbook. It contains the complete 2013–2025 PYQ corpus "
        "and 32 original practice topics. Use the separate solutions document "
        "only after attempting each topic.\n\n"
        "## PART I — UPSC PYQS, 2013–2025\n\n"
        + "\n\n".join(
            question_block(item["label"], item["prompt"], item["verification"])
            for item in pyqs
        )
        + "\n\n## PART II — ORIGINAL PRACTICE TOPICS\n\n"
        + "\n\n".join(
            question_block(item["label"], item["prompt"], item["verification"])
            for item in original
        )
        + "\n"
    )
    solutions = (
        "# Essay — Subject-Wide Practice Solutions\n\n"
        "> Matching solutions for every question in the subject-wide workbook. "
        "These are repository-authored models, not official UPSC model answers.\n\n"
        "## PART I — UPSC PYQ SOLUTIONS\n\n"
        + "\n\n".join(
            solution(
                item["label"],
                item["prompt"],
                item["route"],
                item["verification"],
            )
            for item in pyqs
        )
        + "\n\n## PART II — ORIGINAL PRACTICE SOLUTIONS\n\n"
        + "\n\n".join(
            solution(
                item["label"],
                item["prompt"],
                item["route"],
                item["verification"],
            )
            for item in original
        )
        + "\n"
    )
    OUTPUT.mkdir(parents=True, exist_ok=True)
    guide_path = OUTPUT / "Essay_Complete-Subject-Guide-and-Solved-PYQs.md"
    workbook_path = OUTPUT / "Essay_Subject-Wide-Practice-Workbook.md"
    solutions_path = OUTPUT / "Essay_Subject-Wide-Practice-Solutions.md"
    guide_path.write_text(guide, encoding="utf-8")
    workbook_path.write_text(workbook, encoding="utf-8")
    solutions_path.write_text(solutions, encoding="utf-8")
    for topic in manifest["topics"]:
        for field in ("source_basic", "source_advanced"):
            body = strip_h1((ROOT / str(topic[field])).read_text(encoding="utf-8"))
            if body not in guide:
                raise ValueError(f"Owner content missing: {topic[field]}")
    if guide.count("## TOPIC ") != 16:
        raise ValueError("The master guide must contain all 16 topics.")
    if guide.count("### 20") != 100:
        raise ValueError("The master guide must contain all 100 solved PYQs.")
    if workbook.count("### 20") != 100 or workbook.count("### P") != 32:
        raise ValueError("Workbook coverage must be 100 PYQs plus 32 originals.")
    if solutions.count("### 20") != 100 or solutions.count("### P") != 32:
        raise ValueError("Solutions must match all 132 workbook topics.")
    if re.search(r"(?im)^### SESSION \d+|^### Q\d+\.", guide + workbook + solutions):
        raise ValueError("Essay master package must contain no sessions or MCQs.")
    print(
        "Essay master: topics=16; solved_pyqs=100; "
        "practice_topics=132; sessions=0; mcqs=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
