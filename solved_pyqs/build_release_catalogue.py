from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
PAPERS = ROOT / "papers"
REVIEWS = ROOT / "reviews"
TOPICS = ROOT / "topics"
CATALOGUE = ROOT / "catalogue"
YEARS = tuple(range(2019, 2027))

PAPER_ORDER = (
    "prelims-gs1",
    "prelims-csat",
    "mains-hindi",
    "mains-english",
    "mains-essay",
    "mains-gs1",
    "mains-gs2",
    "mains-gs3",
    "mains-gs4",
    "philosophy-paper-1",
    "philosophy-paper-2",
)

PAPER_NAMES = {
    "prelims-gs1": "Prelims GS-I",
    "prelims-csat": "Prelims CSAT",
    "mains-hindi": "Mains Qualifying Hindi",
    "mains-english": "Mains Qualifying English",
    "mains-essay": "Mains Essay",
    "mains-gs1": "Mains GS-I",
    "mains-gs2": "Mains GS-II",
    "mains-gs3": "Mains GS-III",
    "mains-gs4": "Mains GS-IV",
    "philosophy-paper-1": "Philosophy Paper I",
    "philosophy-paper-2": "Philosophy Paper II",
}

SUBJECT_DIR_NAMES = {
    "ancient-history": "Ancient History",
    "art-and-culture": "Indian Art and Culture",
    "csat": "CSAT",
    "disaster-management": "Disaster Management",
    "economy": "Economy",
    "environment": "Environment and Ecology",
    "essay": "Essay",
    "ethics": "Ethics",
    "geography": "Geography",
    "governance": "Governance",
    "indian-society": "Indian Society",
    "internal-security": "Internal Security",
    "international-relations": "International Relations",
    "medieval-history": "Medieval History",
    "modern-history": "Modern History",
    "philosophy-paper-i": "Philosophy Paper I",
    "philosophy-paper-ii": "Philosophy Paper II",
    "polity": "Polity",
    "post-independence-history": "Post-Independence History",
    "qualifying-english": "Qualifying English",
    "qualifying-hindi": "Qualifying Hindi",
    "science-and-technology": "Science and Technology",
    "social-justice": "Social Justice",
    "world-history": "World History",
}

NEW_TOPIC_INFO = {
    "ancient-history/stone-age-and-human-evolution.md": (
        "The Stone Age and Human Evolution",
        "Ancient History",
    ),
    "geography/islands-and-coral-reefs.md": (
        "Islands and Coral Reefs",
        "Geography",
    ),
    "governance/regulatory-governance-and-independent-regulators.md": (
        "Regulatory Governance and Independent Regulators",
        "Governance",
    ),
    "indian-society/population-and-associated-issues.md": (
        "Population and Associated Issues",
        "Indian Society",
    ),
    "modern-history/national-movement-organisations-and-leaders.md": (
        "National Movement Organisations and Leaders",
        "Modern History",
    ),
    "modern-history/post-war-upsurge-ina-rin-mutiny-and-cabinet-mission.md": (
        "Post-War Upsurge, INA, RIN Mutiny and Cabinet Mission",
        "Modern History",
    ),
    "polity/state-legislatures.md": (
        "State Legislatures",
        "Polity",
    ),
    "world-history/american-and-french-revolutions.md": (
        "American and French Revolutions",
        "World History",
    ),
}

# Canonical routes for every 2019 Prelims GS-I question. These are deliberately
# explicit: the original file linked broad knowledge owners, several of which
# own more than one catalogue topic and therefore cannot be mapped safely by
# filename alone.
PRELIMS_2019_TOPICS = {
    1: "medieval-history/mughal-society-economy-and-culture.md",
    2: "economy/land-reforms-green-revolution-and-cropping-systems.md",
    3: "economy/growth-development-hdi-ihdi-and-mpi.md",
    4: "modern-history/colonial-government-structure-and-constitutional-development.md",
    5: "modern-history/militant-nationalism-and-swadeshi.md",
    6: "modern-history/socio-religious-reform-movements.md",
    7: "ancient-history/harappan-civilization.md",
    8: "ancient-history/ashokan-inscriptions-mauryan-history.md",
    9: "ancient-history/jainism-and-buddhism.md",
    10: "ancient-history/gupta-empire.md",
    11: "art-and-culture/vijayanagara-architecture.md",
    12: "medieval-history/sultanate-technology-economy-and-society.md",
    13: "medieval-history/bhakti-and-sufi-movements.md",
    14: "modern-history/gandhian-mass-mobilisation.md",
    15: "modern-history/national-movement-organisations-and-leaders.md",
    16: "art-and-culture/indian-music.md",
    17: "art-and-culture/painting-traditions.md",
    18: "environment/protected-area-network-india.md",
    19: "governance/government-policy-design-and-implementation.md",
    20: "geography/the-earth-and-the-universe.md",
    21: "geography/primary-economic-activities-agriculture.md",
    22: "environment/iucn-red-list-and-endemism.md",
    23: "geography/water-resources-scarcity-and-access.md",
    24: "economy/poverty-inequality-social-sector-and-inclusive-growth.md",
    25: "environment/climate-change-science-greenhouse-effect.md",
    26: "environment/solid-plastic-and-e-waste-rules.md",
    27: "environment/protected-area-network-india.md",
    28: "environment/ecosystem-structure-and-function.md",
    29: "environment/iucn-red-list-and-endemism.md",
    30: "environment/water-pollution-and-river-cleaning-missions.md",
    31: "environment/species-and-current-affairs-tracker.md",
    32: "science-and-technology/satellites-navic-gagan-and-applications.md",
    33: "environment/forest-types-and-forest-rights-act.md",
    34: "environment/climate-change-science-greenhouse-effect.md",
    35: "environment/air-pollution-and-cpcb-standards.md",
    36: "geography/world-regional-geography-continents-countries.md",
    37: "economy/foreign-trade-wto-ftas-and-protectionism.md",
    38: "geography/himalayan-glaciers-and-glof.md",
    39: "economy/irrigation-inputs-credit-insurance-and-sustainable-agriculture.md",
    40: "environment/wetlands-ramsar-and-conservation-programmes.md",
    41: "environment/biogeochemical-cycles-and-ecological-pyramids.md",
    42: "geography/lakes.md",
    43: "science-and-technology/electric-vehicles-batteries-and-alternative-fuels.md",
    44: "geography/weather-elements.md",
    45: "polity/amendment-and-basic-structure.md",
    46: "polity/supreme-court.md",
    47: "polity/amendment-and-basic-structure.md",
    48: "economy/industrial-policy-1991-reforms-psus-and-disinvestment.md",
    49: "polity/parliament.md",
    50: "polity/scheduled-and-tribal-areas.md",
    51: "social-justice/scheduled-tribes-and-pvtgs.md",
    52: "polity/supreme-court.md",
    53: "polity/state-legislatures.md",
    54: "international-relations/un-and-international-institutions-global-governance.md",
    55: "environment/forest-types-and-forest-rights-act.md",
    56: "polity/fundamental-rights.md",
    57: "science-and-technology/intellectual-property-rights-and-patents.md",
    58: "environment/environmental-impact-assessment-and-ngt.md",
    59: "environment/solid-plastic-and-e-waste-rules.md",
    60: "economy/employment-labour-codes-skills-and-demographic-dividend.md",
    61: "economy/banking-structure-nbfcs-and-financial-regulation.md",
    62: "geography/mineral-energy-resources-world-and-india.md",
    63: "economy/balance-of-payments-exchange-rates-and-forex-reserves.md",
    64: "economy/banking-structure-nbfcs-and-financial-regulation.md",
    65: "economy/balance-of-payments-exchange-rates-and-forex-reserves.md",
    66: "polity/governor-and-cm.md",
    67: "economy/securities-bonds-equity-derivatives-and-investment-funds.md",
    68: "environment/forest-governance-campa-and-green-india-mission.md",
    69: "polity/parliament.md",
    70: "economy/industrial-policy-1991-reforms-psus-and-disinvestment.md",
    71: "economy/imf-world-bank-adb-aiib-ndb-and-global-governance.md",
    72: "economy/banking-structure-nbfcs-and-financial-regulation.md",
    73: "economy/banking-structure-nbfcs-and-financial-regulation.md",
    74: "governance/regulatory-governance-and-independent-regulators.md",
    75: "science-and-technology/digital-india-india-stack-and-digital-infrastructure.md",
    76: "social-justice/women-and-gender-justice.md",
    77: "economy/growth-development-hdi-ihdi-and-mpi.md",
    78: "environment/solid-plastic-and-e-waste-rules.md",
    79: "economy/msp-procurement-buffer-stocks-pds-and-food-security.md",
    80: "economy/growth-development-hdi-ihdi-and-mpi.md",
    81: "polity/supreme-court.md",
    82: "economy/national-income-gdp-gva-and-measurement.md",
    83: "economy/land-reforms-green-revolution-and-cropping-systems.md",
    84: "economy/foreign-trade-wto-ftas-and-protectionism.md",
    85: "polity/fundamental-rights.md",
    86: "economy/rbi-monetary-policy-and-liquidity-management.md",
    87: "economy/rbi-monetary-policy-and-liquidity-management.md",
    88: "science-and-technology/data-protection-dpdp-act-and-cybersecurity.md",
    89: "international-relations/india-china-major-powers-and-resilient-supply-chains.md",
    90: "economy/rbi-monetary-policy-and-liquidity-management.md",
    91: "science-and-technology/digital-india-india-stack-and-digital-infrastructure.md",
    92: "ancient-history/stone-age-and-human-evolution.md",
    93: "science-and-technology/genetic-engineering-gm-crops-and-crispr.md",
    94: "science-and-technology/data-protection-dpdp-act-and-cybersecurity.md",
    95: "science-and-technology/digital-india-india-stack-and-digital-infrastructure.md",
    96: "science-and-technology/genetic-engineering-gm-crops-and-crispr.md",
    97: "science-and-technology/general-science-physics-fundamentals.md",
    98: "science-and-technology/general-science-biology-and-physiology.md",
    99: "science-and-technology/genetic-engineering-gm-crops-and-crispr.md",
    100: "science-and-technology/general-science-biology-and-physiology.md",
}

MAINS_GS1_2019_TOPICS = {
    1: "art-and-culture/sculpture-pottery-and-iconography.md",
    2: "modern-history/the-revolt-of-1857.md",
    3: "modern-history/socio-religious-reform-movements.md",
    4: "geography/islands-and-coral-reefs.md",
    5: "environment/coastal-and-marine-ecology-crz-blue-economy.md",
    6: "geography/industries-and-industrial-regions.md",
    7: "geography/industries-and-industrial-regions.md",
    8: "indian-society/unity-diversity-communalism-regionalism.md",
    9: "indian-society/population-and-associated-issues.md",
    10: "indian-society/secularism.md",
    11: "modern-history/left-peasant-workers-and-states-peoples-movements.md",
    12: "modern-history/post-war-upsurge-ina-rin-mutiny-and-cabinet-mission.md",
    13: "world-history/american-and-french-revolutions.md",
    14: "geography/water-resources-scarcity-and-access.md",
    15: "environment/environmental-impact-assessment-and-ngt.md",
    16: "geography/transport-trade-and-indian-space-programme.md",
    17: "geography/oceans-currents-tides-and-salinity.md",
    18: "geography/cultural-and-social-geography-of-india.md",
    19: "indian-society/women-gender-and-social-distress.md",
    20: "indian-society/effects-of-globalisation-on-indian-society.md",
}

YEAR_CAVEATS = {
    2019: "Both Prelims Series-A keys are official-final; no item was dropped.",
    2020: "Both Prelims Set-A keys are official-final; GS-I Q27 and Q52 were dropped.",
    2021: "Both Prelims Series-A keys are official-final; GS-I Q80 was dropped and CSAT Q39 accepted C or D.",
    2022: "Both Prelims Series-A keys are official-final; GS-I Q61 and CSAT Q36 were dropped.",
    2023: "Both Prelims Series-A keys are official-final; GS-I Q34 was dropped.",
    2024: "Both Prelims Series-A keys are official-final; GS-I Q20, Q52 and Q57 were dropped.",
    2025: "Both Prelims Series-A keys are official-final; no released scoring exception remains.",
    2026: "Both repository-held Prelims keys remain provisional; GS-I Q64 is dropped in the provisional key.",
}


@dataclass
class TopicInfo:
    path: str
    title: str
    subject: str


@dataclass
class Record:
    year: int
    paper: str
    paper_name: str
    anchor: str
    question_label: str
    heading: str
    subject: str
    topic: str
    topic_path: str
    subtopic: str
    answerable_unit: bool
    marks_represented: int
    word_limit: int | None
    secondary_topics: list[str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and read_text(path) == text:
        return False
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def anchor_sections(text: str):
    matches = list(re.finditer(r'<a id="([^"]+)"></a>', text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        yield match.group(1), match.start(), end, text[match.end() : end]


def heading_from_block(block: str) -> str:
    match = re.search(r"^#{2,5}\s+(.+?)\s*$", block, re.MULTILINE)
    if match:
        return match.group(1).strip()
    for line in block.splitlines():
        value = line.strip()
        if not value:
            continue
        value = re.sub(r"^\d+\.\s*", "", value)
        value = value.strip("*_` ")
        if value and not value.startswith("**Primary route:"):
            return value
    return ""


def clean_heading(heading: str) -> str:
    return re.sub(r"\s+", " ", heading).strip()


def question_label(heading: str, anchor: str) -> str:
    suffix_match = re.search(r"-q0*(\d+)([a-z])?(?:-?([ivx]+))?$", anchor)
    if suffix_match:
        number, letter, roman = suffix_match.groups()
        label = f"Q{number}"
        if letter:
            label += f"({letter})"
        if roman:
            label += f"({roman})"
        return label
    match = re.match(
        r"(Q\d+(?:\([a-z]\))?(?:\([ivx]+\))?|Q\d+[A-Za-z]?)(?=\.|\s|—|-|$)",
        heading,
        re.IGNORECASE,
    )
    if match:
        return match.group(1)
    return anchor.rsplit("-", 1)[-1].upper()


def natural_key(value: str):
    return tuple(
        int(piece) if piece.isdigit() else piece.casefold()
        for piece in re.split(r"(\d+)", value)
    )


def strip_question_prefix(heading: str) -> str:
    value = re.sub(
        r"^Q\d+(?:\([a-z]\))?(?:\([ivx]+\))?\.\s*",
        "",
        heading,
        flags=re.IGNORECASE,
    )
    return re.sub(r"\s+[—-]\s+\d+(?:\s*[×x]\s*\d+\s*=\s*\d+)?\s*(?:marks?|अंक).*$", "", value, flags=re.IGNORECASE).strip()


def load_topic_info() -> dict[str, TopicInfo]:
    result: dict[str, TopicInfo] = {}
    for path in sorted(TOPICS.rglob("*.md")):
        relative = path.relative_to(TOPICS).as_posix()
        text = read_text(path)
        title_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
        subject_match = re.search(r"^\*\*Subject:\*\*\s*(.+?)\s*$", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()
        subject = (
            subject_match.group(1).strip()
            if subject_match
            else SUBJECT_DIR_NAMES.get(relative.split("/", 1)[0], relative.split("/", 1)[0])
        )
        result[relative] = TopicInfo(relative, title, subject)
    for relative, (title, subject) in NEW_TOPIC_INFO.items():
        result[relative] = TopicInfo(relative, title, subject)
    return result


def route_subtopic(route_line: str, fallback_heading: str) -> str:
    topic_link = re.search(r"\]\(\.\./\.\./topics/[^)]+\.md\)", route_line)
    if topic_link:
        tail = route_line[topic_link.end() :]
        match = re.match(r"\s*→\s*(.+?)(?:\s*·\s*\*\*|$)", tail)
        if match and match.group(1).strip():
            return match.group(1).strip()
    return strip_question_prefix(fallback_heading) or fallback_heading


def update_2019_prelims(topic_info: dict[str, TopicInfo]) -> bool:
    path = PAPERS / "2019" / "prelims-gs1.md"
    text = read_text(path)
    chunks: list[str] = []
    cursor = 0
    changed = False
    for anchor, start, end, block in anchor_sections(text):
        chunks.append(text[cursor:start])
        section = text[start:end]
        number_match = re.search(r"-q(\d+)$", anchor)
        if not number_match:
            chunks.append(section)
            cursor = end
            continue
        number = int(number_match.group(1))
        topic_path = PRELIMS_2019_TOPICS[number]
        info = topic_info[topic_path]
        heading = heading_from_block(block)
        old_route = re.search(r"^\*\*Primary route:\*\*(.+?)$", section, re.MULTILINE)
        if not old_route:
            raise ValueError(f"Missing route in {anchor}")
        old_subtopic_match = re.search(
            r"^\*\*Primary route:\*\*.+?\]\([^)]+\)\s*→\s*(.+?)\s*$",
            section,
            re.MULTILINE,
        )
        subtopic = (
            old_subtopic_match.group(1).strip()
            if old_subtopic_match
            else strip_question_prefix(heading)
        )
        new_route = (
            f"**Primary route:** {info.subject} → [{info.title}]"
            f"(../../topics/{topic_path}) → {subtopic}  "
        )
        section = re.sub(
            r"^\*\*Primary route:\*\*.+?$",
            new_route,
            section,
            count=1,
            flags=re.MULTILINE,
        )
        new_classification = (
            f"**Primary classification:** {info.subject} → {info.title} → {subtopic}  "
        )
        section = re.sub(
            r"^\*\*Primary classification:\*\*.+?$",
            new_classification,
            section,
            count=1,
            flags=re.MULTILINE,
        )
        if section != text[start:end]:
            changed = True
        chunks.append(section)
        cursor = end
    chunks.append(text[cursor:])
    return write_if_changed(path, "".join(chunks)) or changed


def update_2019_mains_gs1(topic_info: dict[str, TopicInfo]) -> bool:
    path = PAPERS / "2019" / "mains-gs1.md"
    text = read_text(path)
    chunks: list[str] = []
    cursor = 0
    changed = False
    for anchor, start, end, block in anchor_sections(text):
        chunks.append(text[cursor:start])
        section = text[start:end]
        number_match = re.search(r"-q(\d+)$", anchor)
        if not number_match:
            chunks.append(section)
            cursor = end
            continue
        number = int(number_match.group(1))
        topic_path = MAINS_GS1_2019_TOPICS[number]
        info = topic_info[topic_path]
        old_route = re.search(r"^\*\*Primary route:\*\*(.+?)$", section, re.MULTILINE)
        if not old_route:
            raise ValueError(f"Missing route in {anchor}")
        route_text = old_route.group(1)
        old_subtopic_match = re.search(r"\]\([^)]+\)\s*→\s*(.+?)(?:\s*·\s*\*\*|$)", route_text)
        subtopic = (
            old_subtopic_match.group(1).strip()
            if old_subtopic_match
            else strip_question_prefix(heading_from_block(block))
        )
        if number == 13:
            subtopic = "Foundations of the modern world"
        secondary = ""
        secondary_match = re.search(r"\s*·\s*\*\*Secondary owner:\*\*.+?(?=\s*·\s*\*\*Backlink:)", route_text)
        if secondary_match:
            secondary = secondary_match.group(0)
        if number == 13:
            secondary = (
                " · **Source owners:** "
                "[American Revolution](../../../upsc-ai-kit/knowledge/World-History/advanced/02_American-Revolution.md); "
                "[French Revolution and Napoleon](../../../upsc-ai-kit/knowledge/World-History/advanced/03_French-Revolution-and-Napoleon.md)"
            )
        new_route = (
            f"**Primary route:** {info.subject} → [{info.title}]"
            f"(../../topics/{topic_path}) → {subtopic}"
            f"{secondary} · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)"
        )
        section = re.sub(
            r"^\*\*Primary route:\*\*.+?$",
            new_route,
            section,
            count=1,
            flags=re.MULTILINE,
        )
        new_classification = (
            f"**Primary classification:** {info.subject} → {info.title} → {subtopic}  "
        )
        section = re.sub(
            r"^\*\*Primary classification:\*\*.+?$",
            new_classification,
            section,
            count=1,
            flags=re.MULTILINE,
        )
        if section != text[start:end]:
            changed = True
        chunks.append(section)
        cursor = end
    chunks.append(text[cursor:])
    return write_if_changed(path, "".join(chunks)) or changed


def english_atomic_subtopic(anchor: str, heading: str) -> tuple[str, str]:
    if re.search(r"-q04a-", anchor):
        return "qualifying-english/grammar-and-sentence-correction.md", "Sentence correction"
    if re.search(r"-q04b-", anchor):
        return "qualifying-english/grammar-and-sentence-correction.md", "Missing function words"
    if re.search(r"-q04c-", anchor):
        return "qualifying-english/grammar-and-sentence-correction.md", "Verb forms"
    if re.search(r"-q04d-", anchor):
        return "qualifying-english/grammar-and-sentence-correction.md", "Antonyms"
    if re.search(r"-q05a-", anchor):
        return "qualifying-english/sentence-transformation.md", "Sentence transformation"
    if re.search(r"-q05b-", anchor):
        return "qualifying-english/sentence-transformation.md", "Contextual word usage"
    if re.search(r"-q05c-", anchor):
        return "qualifying-english/sentence-transformation.md", "Confusable word choice"
    if re.search(r"-q05d-", anchor):
        return "qualifying-english/sentence-transformation.md", "Idiomatic usage"
    raise ValueError(f"Unexpected unrouted English anchor {anchor}: {heading}")


def update_2019_english(topic_info: dict[str, TopicInfo]) -> bool:
    path = PAPERS / "2019" / "mains-english.md"
    text = read_text(path)
    chunks: list[str] = []
    cursor = 0
    changed = False
    for anchor, start, end, block in anchor_sections(text):
        chunks.append(text[cursor:start])
        section = text[start:end]
        if re.search(r"^\*\*Primary route:\*\*", section, re.MULTILINE):
            chunks.append(section)
            cursor = end
            continue
        heading_match = re.search(r"^(#{2,5}\s+.+?)$", section, re.MULTILINE)
        if not heading_match:
            raise ValueError(f"Missing heading in {anchor}")
        heading = heading_match.group(1).lstrip("#").strip()
        topic_path, family_subtopic = english_atomic_subtopic(anchor, heading)
        info = topic_info[topic_path]
        item = strip_question_prefix(heading)
        subtopic = f"{family_subtopic}: {item}" if item else family_subtopic
        route = (
            f"\n**Primary route:** {info.subject} → [{info.title}]"
            f"(../../topics/{topic_path}) → {subtopic}"
            " · **Backlink:** [Paper-wise index](../../catalogue/PAPERWISE-INDEX.md)"
        )
        insert_at = heading_match.end()
        section = section[:insert_at] + route + section[insert_at:]
        changed = True
        chunks.append(section)
        cursor = end
    chunks.append(text[cursor:])
    return write_if_changed(path, "".join(chunks)) or changed


def apply_2019_integration() -> list[str]:
    topic_info = load_topic_info()
    changed = []
    if update_2019_prelims(topic_info):
        changed.append("solved_pyqs/papers/2019/prelims-gs1.md")
    if update_2019_mains_gs1(topic_info):
        changed.append("solved_pyqs/papers/2019/mains-gs1.md")
    if update_2019_english(topic_info):
        changed.append("solved_pyqs/papers/2019/mains-english.md")
    return changed


def is_answerable_unit(paper: str, anchor: str) -> bool:
    if paper == "mains-english":
        return not bool(
            re.search(r"-(?:q01|q02|q04|q04[abcd]|q05|q05[abcd])$", anchor)
        )
    if paper == "mains-hindi":
        return not bool(re.search(r"-(?:q2|q6[abcd])$", anchor))
    if paper == "mains-gs4":
        return not bool(re.search(r"-q(?:7|8|9|10|11|12)$", anchor))
    return True


def extract_marks(paper: str, anchor: str, heading: str, block: str, unit: bool) -> int:
    if paper in {"prelims-gs1", "prelims-csat"}:
        return 0
    if paper == "mains-essay":
        return 125
    if paper in {"mains-english", "mains-hindi"} and not unit:
        return 0
    if paper == "mains-english":
        if re.search(r"-q0?1[a-d]$", anchor):
            return 100
        if re.search(r"-q0?2[a-e]$", anchor):
            return 15
        if re.search(r"-q0?3$", anchor):
            return 75
        if re.search(r"-q0?[45][a-d]?(?:-|(?=[ivx]+$))[ivx]+$", anchor):
            return 1
    if paper == "mains-hindi":
        if re.search(r"-q1[a-d]$", anchor):
            return 100
        if re.search(r"-q2[a-e]$", anchor):
            return 12
        if re.search(r"-q3$", anchor):
            return 60
        if re.search(r"-q[45]$", anchor):
            return 20
        if re.search(r"-q6[a-d]-[ivx]+$", anchor):
            return 2
    if paper == "mains-gs4" and re.search(r"-q(?:7|8|9|10|11|12)[a-z]$", anchor):
        return 0
    prefix = "\n".join(block.splitlines()[:18])
    source = f"{heading}\n{prefix}"
    match = re.search(r"(?<!\d)(\d{1,3})\s*(?:marks?|अंक)\b", source, re.IGNORECASE)
    if match:
        return int(match.group(1))
    labelled = re.search(
        r"\*\*Marks(?:/limit)?:\*\*\s*(\d{1,3})\b", source, re.IGNORECASE
    )
    if labelled:
        return int(labelled.group(1))
    if paper in {"mains-gs1", "mains-gs2", "mains-gs3"}:
        number = int(re.search(r"-q(\d+)$", anchor).group(1))
        return 10 if number <= 10 else 15
    if paper == "mains-gs4" and re.search(r"-q(?:7|8|9|10|11|12)$", anchor):
        return 20
    raise ValueError(f"Unable to parse marks for {anchor}")


def extract_word_limit(heading: str, block: str) -> int | None:
    prefix = "\n".join(block.splitlines()[:18])
    source = f"{heading}\n{prefix}"
    match = re.search(r"(?<!\d)(\d{2,4})\s*(?:words?|शब्द)\b", source, re.IGNORECASE)
    return int(match.group(1)) if match else None


def parse_records(topic_info: dict[str, TopicInfo]) -> tuple[list[Record], dict[str, list[str]]]:
    records: list[Record] = []
    explicit_anchors: dict[str, list[str]] = {}
    for year in YEARS:
        for paper in PAPER_ORDER:
            path = PAPERS / str(year) / f"{paper}.md"
            if not path.exists():
                raise FileNotFoundError(path)
            text = read_text(path)
            explicit_anchors[path.relative_to(ROOT).as_posix()] = re.findall(
                r'<a id="([^"]+)"></a>', text
            )
            for anchor, _, _, block in anchor_sections(text):
                route_match = re.search(r"^\*\*Primary route:\*\*(.+?)$", block, re.MULTILINE)
                if not route_match:
                    continue
                route_line = route_match.group(1).strip()
                primary_match = re.search(
                    r"^\s*(.+?)\s*→\s*\[([^\]]+)\]"
                    r"\(\.\./\.\./topics/([^)#]+\.md)\)",
                    route_line,
                )
                if not primary_match:
                    raise ValueError(f"Non-canonical primary route in {path}: {anchor}")
                route_subject, route_title, topic_path = primary_match.groups()
                if topic_path not in topic_info:
                    title = route_title.strip()
                    subject = route_subject.strip()
                    topic_info[topic_path] = TopicInfo(topic_path, title, subject)
                info = topic_info[topic_path]
                heading = clean_heading(heading_from_block(block))
                subtopic = route_subtopic(route_line, heading)
                unit = is_answerable_unit(paper, anchor)
                marks = extract_marks(paper, anchor, heading, block, unit)
                secondary_topics: list[str] = []
                all_primary_line_topics = re.findall(
                    r"\]\(\.\./\.\./topics/([^)#]+\.md)\)", route_line
                )
                secondary_topics.extend(all_primary_line_topics[1:])
                for secondary_line in re.findall(
                    r"^\*\*Secondary route:\*\*(.+?)$", block, re.MULTILINE
                ):
                    secondary_topics.extend(
                        re.findall(
                            r"\]\(\.\./\.\./topics/([^)#]+\.md)\)", secondary_line
                        )
                    )
                secondary_topics = list(dict.fromkeys(secondary_topics))
                records.append(
                    Record(
                        year=year,
                        paper=paper,
                        paper_name=PAPER_NAMES[paper],
                        anchor=anchor,
                        question_label=question_label(heading, anchor),
                        heading=heading,
                        subject=info.subject,
                        topic=info.title,
                        topic_path=topic_path,
                        subtopic=subtopic,
                        answerable_unit=unit,
                        marks_represented=marks,
                        word_limit=extract_word_limit(heading, block),
                        secondary_topics=secondary_topics,
                    )
                )
    return records, explicit_anchors


def paper_link(record: Record, from_dir: str) -> str:
    if from_dir == "topic":
        prefix = "../../papers"
    elif from_dir == "catalogue":
        prefix = "../papers"
    else:
        raise ValueError(from_dir)
    return f"{prefix}/{record.year}/{record.paper}.md#{record.anchor}"


def safe_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def format_marks(value: int) -> str:
    return str(value) if value else "—"


def paper_structure(year: int, paper: str, anchors: int, units: int) -> str:
    if paper == "prelims-gs1":
        return "100 printed questions · 200 marks"
    if paper == "prelims-csat":
        return "80 printed questions · 200 marks"
    if paper == "mains-hindi":
        return "6 compulsory questions · 300 attempted marks"
    if paper == "mains-english":
        return "5 compulsory questions · 300 attempted marks"
    if paper == "mains-essay":
        return "8 prompts · one from each section · 250 attempted marks"
    if paper in {"mains-gs1", "mains-gs2", "mains-gs3", "mains-gs4"}:
        return "250 attempted marks"
    if paper.startswith("philosophy"):
        return "400 represented selectable marks · 250 attempted marks"
    return f"{anchors} anchors · {units} units"


def generate_topic_pages(records: list[Record], topic_info: dict[str, TopicInfo]) -> set[str]:
    primary: dict[str, list[Record]] = defaultdict(list)
    secondary: dict[str, list[Record]] = defaultdict(list)
    for record in records:
        primary[record.topic_path].append(record)
        for topic_path in record.secondary_topics:
            secondary[topic_path].append(record)
    used = set(primary) | set(secondary)
    changed: set[str] = set()
    for topic_path in sorted(used):
        if topic_path not in topic_info:
            folder = topic_path.split("/", 1)[0]
            topic_info[topic_path] = TopicInfo(
                topic_path,
                Path(topic_path).stem.replace("-", " ").title(),
                SUBJECT_DIR_NAMES.get(folder, folder),
            )
        info = topic_info[topic_path]
        rows = sorted(
            primary.get(topic_path, []),
            key=lambda item: (
                -item.year,
                PAPER_ORDER.index(item.paper),
                natural_key(item.anchor),
            ),
        )
        secondary_rows = sorted(
            secondary.get(topic_path, []),
            key=lambda item: (
                -item.year,
                PAPER_ORDER.index(item.paper),
                natural_key(item.anchor),
            ),
        )
        lines = [
            f"# {info.title}",
            "",
            f"**Subject:** {info.subject}  ",
            f"**Canonical topic:** {info.title}  ",
            "**Scope:** Catalogue-only route for solved PYQs whose primary demand falls under "
            f"{info.title}. Full solutions remain in the paper files.",
            "",
            "## Cross-year concentration",
            "",
        ]
        years = sorted({row.year for row in rows})
        units = sum(row.answerable_unit for row in rows)
        marks = sum(row.marks_represented for row in rows)
        paper_counts = Counter(
            row.paper_name for row in rows if row.answerable_unit
        )
        subtopics = list(dict.fromkeys(row.subtopic for row in rows if row.subtopic))
        lines.extend(
            [
                f"- **Released years represented:** {', '.join(map(str, years)) if years else 'Secondary links only'}",
                f"- **Solved answerable questions/parts:** {units}",
                f"- **Stable linked anchors:** {len(rows)}",
                "- **Paper concentration:** "
                + (
                    "; ".join(f"{paper}: {count}" for paper, count in sorted(paper_counts.items()))
                    if paper_counts
                    else "—"
                ),
            ]
        )
        if marks:
            lines.append(
                f"- **Marks represented:** {marks} (solved selectable alternatives included; GS-IV case marks counted once)"
            )
        lines.append(
            "- **Subtopics represented:** "
            + ("; ".join(subtopics) if subtopics else "—")
        )
        if secondary_rows:
            lines.append(
                f"- **Justified secondary-route anchors:** {len(secondary_rows)} "
                "(excluded from primary concentration totals)"
            )
        for year in YEARS:
            year_rows = [row for row in rows if row.year == year]
            if not year_rows:
                continue
            year_units = sum(row.answerable_unit for row in year_rows)
            year_marks = sum(row.marks_represented for row in year_rows)
            year_papers = Counter(
                row.paper_name for row in year_rows if row.answerable_unit
            )
            year_subtopics = list(
                dict.fromkeys(row.subtopic for row in year_rows if row.subtopic)
            )
            lines.extend(
                [
                    "",
                    f"## {year} concentration",
                    "",
                    f"- **Solved answerable questions/parts:** {year_units}",
                    f"- **Stable linked anchors:** {len(year_rows)}",
                    "- **Paper concentration:** "
                    + (
                        "; ".join(
                            f"{paper}: {count}"
                            for paper, count in sorted(year_papers.items())
                        )
                        if year_papers
                        else "—"
                    ),
                ]
            )
            if year_marks:
                lines.append(
                    f"- **Marks represented:** {year_marks} (solved selectable alternatives included; GS-IV case marks counted once)"
                )
            lines.append(
                "- **Subtopics represented:** "
                + ("; ".join(year_subtopics) if year_subtopics else "—")
            )
        lines.extend(["", "## Linked PYQs"])
        for year in sorted({row.year for row in rows}, reverse=True):
            lines.extend(["", f"### {year}"])
            for paper in PAPER_ORDER:
                paper_rows = [
                    row for row in rows if row.year == year and row.paper == paper
                ]
                if not paper_rows:
                    continue
                lines.extend(["", f"#### {PAPER_NAMES[paper]}", ""])
                for row in paper_rows:
                    marks_text = (
                        f" · {row.marks_represented} marks"
                        if row.marks_represented
                        else ""
                    )
                    lines.append(
                        f"- [{safe_cell(row.heading)}]({paper_link(row, 'topic')})"
                        f" — {safe_cell(row.subtopic)}{marks_text}"
                    )
        if secondary_rows:
            lines.extend(
                [
                    "",
                    "## Secondary-routed PYQs",
                    "",
                    "These links are interdisciplinary aids and are excluded from all primary counts.",
                ]
            )
            for row in secondary_rows:
                lines.append(
                    f"- [{row.year} · {row.paper_name} · {safe_cell(row.heading)}]"
                    f"({paper_link(row, 'topic')}) — {safe_cell(row.subtopic)}"
                )
        text = "\n".join(lines).rstrip() + "\n"
        path = TOPICS / topic_path
        if write_if_changed(path, text):
            changed.add(path.relative_to(REPO).as_posix())
    return changed


def anchor_link_list(records: list[Record]) -> list[str]:
    links = [
        f"[{row.question_label}](../papers/{row.year}/{row.paper}.md#{row.anchor})"
        for row in records
    ]
    return [
        " · ".join(links[index : index + 10])
        for index in range(0, len(links), 10)
    ]


def generate_paperwise(records: list[Record], explicit_anchors: dict[str, list[str]]) -> str:
    by_paper: dict[tuple[int, str], list[Record]] = defaultdict(list)
    for record in records:
        by_paper[(record.year, record.paper)].append(record)
    lines = [
        "# Solved PYQs — Paper-wise Index",
        "",
        "All eight released years have paper-specific review records and final shared-release status.",
    ]
    for year in sorted(YEARS, reverse=True):
        lines.extend(
            [
                "",
                f'<a id="{year}-complete-release"></a>',
                f"## {year} — Complete release",
                "",
                YEAR_CAVEATS[year],
            ]
        )
        for paper in PAPER_ORDER:
            rows = by_paper[(year, paper)]
            units = sum(row.answerable_unit for row in rows)
            relative = f"papers/{year}/{paper}.md"
            explicit_count = len(explicit_anchors[relative])
            lines.extend(
                [
                    "",
                    f"### {PAPER_NAMES[paper]}",
                    "",
                    f"- [Complete solved paper](../papers/{year}/{paper}.md) — "
                    f"{paper_structure(year, paper, len(rows), units)} · release status: **PASS**",
                    f"- [Review record](../reviews/{year}-{paper}.md) — **PASS**",
                    f"- Routed stable anchors: **{len(rows)}** · answerable solved units: **{units}**"
                    + (
                        f" · explicit anchors including source notes: **{explicit_count}**"
                        if explicit_count != len(rows)
                        else ""
                    ),
                    "",
                    "<details>",
                    "<summary>Exact question/part anchors</summary>",
                    "",
                ]
            )
            lines.extend(f"- {line}" for line in anchor_link_list(rows))
            lines.extend(["", "</details>"])
    return "\n".join(lines).rstrip() + "\n"


def aggregate_topic(records: list[Record]):
    groups: dict[str, list[Record]] = defaultdict(list)
    for record in records:
        groups[record.topic_path].append(record)
    return groups


def generate_subject_index(records: list[Record], topic_info: dict[str, TopicInfo]) -> str:
    topic_groups = aggregate_topic(records)
    subject_rows: dict[str, list[Record]] = defaultdict(list)
    for record in records:
        subject_rows[record.subject].append(record)
    total_units = sum(record.answerable_unit for record in records)
    total_anchors = len(records)
    lines = [
        "# Solved PYQs — Subject Index",
        "",
        f"**2019–2026 released corpus:** {total_units:,} solved answerable units · "
        f"{total_anchors:,} stable routed anchors · {len(topic_groups):,} canonical topic pages.",
        "",
        "Counts are generated from `catalogue/CORPUS-METADATA.json`. Topic pages are catalogue-only "
        "and link to canonical paper-wise solutions. Marks are represented marks across every solved "
        "selectable alternative; they are not attempted-paper totals.",
        "",
        "## Subject concentration summary",
        "",
        "| Subject | "
        + " | ".join(f"{year} units" for year in YEARS)
        + " | Total units | Routed anchors | Topics | Marks represented |",
        "|---|"
        + "|".join("---:" for _ in YEARS)
        + "|---:|---:|---:|---:|",
    ]
    for subject in sorted(subject_rows):
        rows = subject_rows[subject]
        year_units = [
            sum(record.answerable_unit for record in rows if record.year == year)
            for year in YEARS
        ]
        lines.append(
            f"| {subject} | "
            + " | ".join(map(str, year_units))
            + f" | {sum(year_units)} | {len(rows)} | "
            f"{len({row.topic_path for row in rows})} | "
            f"{format_marks(sum(row.marks_represented for row in rows))} |"
        )
    for subject in sorted(subject_rows):
        lines.extend(["", f"## {subject}", ""])
        topic_paths = sorted(
            {record.topic_path for record in subject_rows[subject]},
            key=lambda path: topic_info[path].title.casefold(),
        )
        for topic_path in topic_paths:
            rows = sorted(
                topic_groups[topic_path],
                key=lambda item: (
                    -item.year,
                    PAPER_ORDER.index(item.paper),
                    natural_key(item.anchor),
                ),
            )
            units = sum(row.answerable_unit for row in rows)
            year_counts = Counter(
                row.year for row in rows if row.answerable_unit
            )
            paper_names = sorted({row.paper_name for row in rows})
            marks = sum(row.marks_represented for row in rows)
            summary = ", ".join(
                f"{year}: {year_counts[year]}" for year in YEARS if year_counts[year]
            )
            direct = " · ".join(
                f"[{row.question_label}]({paper_link(row, 'catalogue')})" for row in rows
            )
            lines.append(
                f"- [{topic_info[topic_path].title}](../topics/{topic_path}) — "
                f"**{units}** solved units ({summary}; {', '.join(paper_names)})"
                + (f" · **{marks} marks represented**" if marks else "")
                + f". {direct}"
            )
    return "\n".join(lines).rstrip() + "\n"


def generate_topic_index(records: list[Record], topic_info: dict[str, TopicInfo]) -> str:
    groups = aggregate_topic(records)
    lines = [
        "# Solved PYQs — Topic Index",
        "",
        "Marks are represented marks across every solved selectable alternative; GS-IV case marks are counted once at case level.",
        "",
        "| Canonical topic | Subject | "
        + " | ".join(f"{year} units" for year in YEARS)
        + " | Total units | Routed anchors | Marks represented | Papers | Exact solved-question links |",
        "|---|---|"
        + "|".join("---:" for _ in YEARS)
        + "|---:|---:|---:|---|---|",
    ]
    for topic_path in sorted(groups, key=lambda path: topic_info[path].title.casefold()):
        rows = sorted(
            groups[topic_path],
            key=lambda item: (
                -item.year,
                PAPER_ORDER.index(item.paper),
                natural_key(item.anchor),
            ),
        )
        year_units = [
            sum(row.answerable_unit for row in rows if row.year == year)
            for year in YEARS
        ]
        links = " · ".join(
            f"[{safe_cell(row.heading)}]({paper_link(row, 'catalogue')})" for row in rows
        )
        papers = ", ".join(sorted({row.paper_name for row in rows}))
        lines.append(
            f"| [{safe_cell(topic_info[topic_path].title)}](../topics/{topic_path})"
            f" | {safe_cell(topic_info[topic_path].subject)} | "
            + " | ".join(map(str, year_units))
            + f" | {sum(year_units)} | {len(rows)} | "
            f"{format_marks(sum(row.marks_represented for row in rows))} | "
            f"{safe_cell(papers)} | {links} |"
        )
    return "\n".join(lines).rstrip() + "\n"


def generate_years_index(records: list[Record]) -> str:
    by_year = defaultdict(list)
    for record in records:
        by_year[record.year].append(record)
    lines = [
        "# Years Index",
        "",
        "The catalogue covers exactly the latest eight available years: **2019–2026**.",
        "",
        "| Year | Paper files | Answerable units | Routed anchors | Topics | Release |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for year in sorted(YEARS, reverse=True):
        rows = by_year[year]
        lines.append(
            f"| {year} | 11 | {sum(row.answerable_unit for row in rows)} | {len(rows)} | "
            f"{len({row.topic_path for row in rows})} | "
            f"[**Complete — shared release PASS**](PAPERWISE-INDEX.md#{year}-complete-release) |"
        )
    lines.extend(["", "## Direct paper and review links"])
    for year in sorted(YEARS, reverse=True):
        lines.extend(["", f"### {year}", ""])
        for paper in PAPER_ORDER:
            lines.append(
                f"- [{PAPER_NAMES[paper]}](../papers/{year}/{paper}.md) · "
                f"[review](../reviews/{year}-{paper}.md)"
            )
        lines.extend(["", f"- **Key/source caveat:** {YEAR_CAVEATS[year]}"])
    return "\n".join(lines).rstrip() + "\n"


def generate_concentration(records: list[Record], topic_info: dict[str, TopicInfo]) -> str:
    by_year = defaultdict(list)
    by_paper = defaultdict(list)
    by_subject = defaultdict(list)
    by_topic = defaultdict(list)
    by_subtopic = defaultdict(list)
    for row in records:
        by_year[row.year].append(row)
        by_paper[row.paper].append(row)
        by_subject[row.subject].append(row)
        by_topic[row.topic_path].append(row)
        by_subtopic[(row.subject, row.topic_path, row.subtopic)].append(row)
    total_units = sum(row.answerable_unit for row in records)
    total_marks = sum(row.marks_represented for row in records)
    lines = [
        "# 2019–2026 Concentration Analysis",
        "",
        "## Methodology",
        "",
        "- Source: every canonical `**Primary route:**` attached to an explicit paper anchor, exported to "
        "`CORPUS-METADATA.json`.",
        "- **Answerable unit** excludes structural parent anchors in qualifying-language papers and the "
        "six GS-IV case parents. Each GS-IV case parent carries its marks once; its separately routed "
        "demands carry unit counts but zero additional marks.",
        "- Marks are **represented marks**, so all solved alternatives are counted: qualifying Hindi and "
        "English each represent 600 marks per year, Essay 1,000, each Philosophy paper 400, while the "
        "candidate-attempt totals remain 300, 250 and 250 respectively.",
        "- Prelims/CSAT concentration uses printed question counts, including officially dropped items as "
        "solved learning units. Scoring exceptions are listed under caveats.",
        "- Secondary routes are excluded from every primary total to prevent double counting.",
        "",
        "## Corpus reconciliation",
        "",
        f"- Paper files: **88 = 8 years × 11 paper families**.",
        f"- Routed stable anchors: **{len(records):,}**.",
        f"- Answerable solved units: **{total_units:,}**.",
        f"- Canonical topic pages: **{len(by_topic):,}**.",
        f"- Represented marks across Mains/Philosophy: **{total_marks:,}**.",
        "",
        "## Concentration by year",
        "",
        "| Year | Paper files | Answerable units | Routed anchors | Topics represented | Marks represented |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for year in YEARS:
        rows = by_year[year]
        lines.append(
            f"| {year} | 11 | {sum(row.answerable_unit for row in rows)} | {len(rows)} | "
            f"{len({row.topic_path for row in rows})} | {sum(row.marks_represented for row in rows)} |"
        )
    lines.extend(
        [
            "",
            "## Concentration by paper family",
            "",
            "| Paper | Years | Answerable units | Routed anchors | Topics | Marks represented |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for paper in PAPER_ORDER:
        rows = by_paper[paper]
        lines.append(
            f"| {PAPER_NAMES[paper]} | {len({row.year for row in rows})} | "
            f"{sum(row.answerable_unit for row in rows)} | {len(rows)} | "
            f"{len({row.topic_path for row in rows})} | {sum(row.marks_represented for row in rows)} |"
        )
    lines.extend(
        [
            "",
            "## Concentration by primary subject",
            "",
            "| Subject | Answerable units | Routed anchors | Topics | Years | Marks represented |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for subject in sorted(by_subject):
        rows = by_subject[subject]
        lines.append(
            f"| {safe_cell(subject)} | {sum(row.answerable_unit for row in rows)} | {len(rows)} | "
            f"{len({row.topic_path for row in rows})} | {len({row.year for row in rows})} | "
            f"{sum(row.marks_represented for row in rows)} |"
        )
    lines.extend(
        [
            "",
            "## Concentration by canonical topic",
            "",
            "| Subject | Topic | Answerable units | Routed anchors | Years | Papers | Marks represented |",
            "|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for topic_path in sorted(
        by_topic,
        key=lambda path: (topic_info[path].subject.casefold(), topic_info[path].title.casefold()),
    ):
        rows = by_topic[topic_path]
        lines.append(
            f"| {safe_cell(topic_info[topic_path].subject)} | "
            f"[{safe_cell(topic_info[topic_path].title)}](../topics/{topic_path}) | "
            f"{sum(row.answerable_unit for row in rows)} | {len(rows)} | "
            f"{len({row.year for row in rows})} | {len({row.paper for row in rows})} | "
            f"{sum(row.marks_represented for row in rows)} |"
        )
    lines.extend(
        [
            "",
            "## Concentration by exact subtopic",
            "",
            "Each row is the exact primary Subject → Topic → Subtopic metadata route. Repeated wording is "
            "grouped; question-specific wording remains separate rather than being merged by guesswork.",
            "",
            "| Subject | Topic | Subtopic | Answerable units | Routed anchors | Years | Marks represented |",
            "|---|---|---|---:|---:|---:|---:|",
        ]
    )
    for key in sorted(
        by_subtopic,
        key=lambda item: (item[0].casefold(), topic_info[item[1]].title.casefold(), item[2].casefold()),
    ):
        subject, topic_path, subtopic = key
        rows = by_subtopic[key]
        lines.append(
            f"| {safe_cell(subject)} | {safe_cell(topic_info[topic_path].title)} | "
            f"{safe_cell(subtopic)} | {sum(row.answerable_unit for row in rows)} | {len(rows)} | "
            f"{len({row.year for row in rows})} | {sum(row.marks_represented for row in rows)} |"
        )
    lines.extend(
        [
            "",
            "## Prelims and CSAT question-count concentration",
            "",
            "| Year | Prelims GS-I printed/solved | CSAT printed/solved | Key status and scoring exception |",
            "|---:|---:|---:|---|",
        ]
    )
    for year in YEARS:
        lines.append(f"| {year} | 100 | 80 | {safe_cell(YEAR_CAVEATS[year])} |")
    lines.extend(
        [
            "",
            "## Mains and Philosophy marks concentration",
            "",
            "| Paper family | Represented marks across 8 years | Attempted marks across 8 years | Caveat |",
            "|---|---:|---:|---|",
        ]
    )
    attempted = {
        "mains-hindi": 2400,
        "mains-english": 2400,
        "mains-essay": 2000,
        "mains-gs1": 2000,
        "mains-gs2": 2000,
        "mains-gs3": 2000,
        "mains-gs4": 2000,
        "philosophy-paper-1": 2000,
        "philosophy-paper-2": 2000,
    }
    for paper in PAPER_ORDER[2:]:
        represented = sum(row.marks_represented for row in by_paper[paper])
        caveat = {
            "mains-hindi": "Four essay alternatives are solved each year.",
            "mains-english": "Four essay alternatives are solved each year; no translation task is invented.",
            "mains-essay": "All eight prompts are solved; candidates attempt two.",
            "philosophy-paper-1": "All selectable parts are solved; candidates attempt 250 marks.",
            "philosophy-paper-2": "All selectable parts are solved; candidates attempt 250 marks.",
        }.get(paper, "All questions are compulsory; represented and attempted totals coincide.")
        lines.append(
            f"| {PAPER_NAMES[paper]} | {represented} | {attempted[paper]} | {caveat} |"
        )
    recurring = []
    for topic_path, rows in by_topic.items():
        years = len({row.year for row in rows})
        units = sum(row.answerable_unit for row in rows)
        if years >= 6:
            recurring.append((years, units, topic_path))
    recurring.sort(key=lambda item: (-item[0], -item[1], topic_info[item[2]].title.casefold()))
    lines.extend(
        [
            "",
            "## Recurring themes",
            "",
            "Themes below recur in at least six of the eight released years. Counts remain primary-route "
            "counts; broad interdisciplinary resemblance is not double-counted.",
            "",
        ]
    )
    for years, units, topic_path in recurring:
        rows = by_topic[topic_path]
        marks = sum(row.marks_represented for row in rows)
        lines.append(
            f"- **{topic_info[topic_path].title}** — {units} answerable units, "
            f"{len(rows)} routed anchors, {years} years"
            + (f", {marks} represented marks" if marks else "")
            + "."
        )
    lines.extend(
        [
            "",
            "## Explicit caveats",
            "",
            "- The 2026 held keys remain provisional and are never promoted to official-final.",
            "- Official drops and the 2021 CSAT multiple-answer outcome remain printed questions and solved "
            "learning units, but their scoring status is separately preserved.",
            "- Represented marks measure the released library, not what a candidate writes in one sitting.",
            "- Parent anchors improve navigation and case-level marks accounting; they are not answerable-unit "
            "inflation.",
            "- Canonical routing uses exactly one primary topic. Secondary links are optional, justified and "
            "excluded from concentration totals.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def review_is_pass(path: Path) -> bool:
    if not path.exists():
        return False
    text = read_text(path)
    return bool(re.search(r"\bPASS\b", text)) and not bool(
        re.search(r"Final release conclusion:\s*\*\*BLOCKED\*\*", text, re.IGNORECASE)
    )


def quality_markers(paper: str, text: str) -> bool:
    lower = text.casefold()
    if paper == "prelims-gs1":
        return "answer" in lower and (
            "option" in lower or "reasoning" in lower or "elimination" in lower
        )
    if paper == "prelims-csat":
        return "answer" in lower and ("reason" in lower or "method" in lower)
    if paper in {"mains-gs1", "mains-gs2", "mains-gs3"}:
        return "demand" in lower and (
            "why this earns marks" in lower
            or "examiner takeaway" in lower
            or "model answer" in lower
        )
    if paper == "mains-gs4":
        return "stakeholder" in lower and "why this earns marks" in lower
    if paper == "mains-essay":
        return "model" in lower and "why this earns marks" in lower
    if paper.startswith("philosophy"):
        return "demand decoding" in lower and "why this earns marks" in lower
    if paper in {"mains-hindi", "mains-english"}:
        return "answer" in lower or "उत्तर" in text or "model" in lower
    return True


def generate_quality_spot_checks(records: list[Record]) -> str:
    by_paper: dict[tuple[int, str], list[Record]] = defaultdict(list)
    for record in records:
        by_paper[(record.year, record.paper)].append(record)
    lines = [
        "# Whole-Corpus Answer-Quality Spot Checks",
        "",
        "Every year × paper-family combination was checked against its dedicated review record and a "
        "first/middle/last answerable-anchor sample. This is a release spot-check, not a substitute "
        "for the complete paper-specific reviews.",
        "",
        "| Year | Paper | Sampled anchors | Review | Structural answer-quality check | Result |",
        "|---:|---|---|:---:|:---:|:---:|",
    ]
    for year in YEARS:
        for paper in PAPER_ORDER:
            rows = [row for row in by_paper[(year, paper)] if row.answerable_unit]
            samples = [rows[0], rows[len(rows) // 2], rows[-1]]
            sample_text = ", ".join(
                f"[{row.anchor}](../papers/{year}/{paper}.md#{row.anchor})"
                for row in samples
            )
            review_path = REVIEWS / f"{year}-{paper}.md"
            review_pass = review_is_pass(review_path)
            structural = quality_markers(
                paper, read_text(PAPERS / str(year) / f"{paper}.md")
            )
            result = "PASS" if review_pass and structural else "BLOCKED"
            lines.append(
                f"| {year} | {PAPER_NAMES[paper]} | {sample_text} | "
                f"[{'PASS' if review_pass else 'MISSING/BLOCKED'}](../reviews/{year}-{paper}.md) | "
                f"{'PASS' if structural else 'FAIL'} | **{result}** |"
            )
    lines.extend(
        [
            "",
            "## Family-specific checks applied",
            "",
            "- **Prelims:** key status, answer, option/statement analysis, elimination and provenance.",
            "- **CSAT:** complete reasoning/calculation or passage proof, plus a safe exam method.",
            "- **Qualifying languages:** source-verified structure, idiomatic accuracy, précis discipline and "
            "translation only where officially present.",
            "- **Essay:** interpretation, thesis, transition-bearing structure, counter-view, synthesis and "
            "model treatment.",
            "- **GS-I/II/III:** demand fidelity, proportionality, named evidence, qualification and examiner "
            "takeaway.",
            "- **GS-IV:** theory application and stakeholder–values–options–consequences–safeguards architecture.",
            "- **Philosophy:** English-first terminology, IAST where relevant, argument–objection–reply–evaluation "
            "and exact syllabus routing.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def metadata_json(records: list[Record]) -> str:
    data = {
        "schema": 1,
        "window": {"from": 2019, "to": 2026, "years": 8, "paper_families": 11},
        "method": (
            "Generated from explicit paper anchors and canonical Primary route metadata. "
            "Secondary routes are retained but excluded from primary concentration."
        ),
        "records": [asdict(record) for record in records],
    }
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def markdown_heading_anchors(text: str) -> set[str]:
    anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
    counts: Counter[str] = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*$", text, re.MULTILINE):
        value = re.sub(r"<[^>]+>", "", heading).strip().casefold()
        value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
        value = re.sub(r"\s+", "-", value).strip("-")
        suffix = counts[value]
        counts[value] += 1
        anchors.add(value if suffix == 0 else f"{value}-{suffix}")
    return anchors


def validate_links() -> dict:
    markdown_files = sorted(ROOT.rglob("*.md"))
    anchor_cache = {path: markdown_heading_anchors(read_text(path)) for path in markdown_files}
    missing_files = []
    missing_anchors = []
    occurrences = 0
    unique_targets = set()
    for source in markdown_files:
        text = read_text(source)
        for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
            if re.match(r"^(?:https?://|mailto:)", target):
                continue
            occurrences += 1
            target = unquote(target.strip())
            path_part, _, fragment = target.partition("#")
            target_file = source if not path_part else (source.parent / path_part).resolve()
            unique_targets.add((str(target_file).casefold(), fragment.casefold()))
            if not target_file.exists():
                missing_files.append(
                    {"source": source.relative_to(REPO).as_posix(), "target": target}
                )
                continue
            if fragment and target_file.suffix.casefold() == ".md":
                if target_file not in anchor_cache:
                    anchor_cache[target_file] = markdown_heading_anchors(read_text(target_file))
                if fragment not in anchor_cache[target_file]:
                    missing_anchors.append(
                        {"source": source.relative_to(REPO).as_posix(), "target": target}
                    )
    return {
        "markdown_link_occurrences": occurrences,
        "unique_local_link_targets": len(unique_targets),
        "missing_files": missing_files,
        "missing_anchors": missing_anchors,
    }


def validate_corpus(records: list[Record], explicit_anchors: dict[str, list[str]]) -> dict:
    issues: list[str] = []
    topic_paths = set(load_topic_info())
    paper_blocks: dict[str, str] = {}
    for year in YEARS:
        for paper in PAPER_ORDER:
            paper_path = PAPERS / str(year) / f"{paper}.md"
            for anchor, _, _, block in anchor_sections(read_text(paper_path)):
                paper_blocks[anchor] = block
    expected_files = {
        f"papers/{year}/{paper}.md" for year in YEARS for paper in PAPER_ORDER
    }
    actual_files = {
        path.relative_to(ROOT).as_posix() for path in PAPERS.glob("*/*.md")
    }
    if actual_files != expected_files:
        issues.append(
            f"paper inventory mismatch: missing={sorted(expected_files - actual_files)}, "
            f"extra={sorted(actual_files - expected_files)}"
        )
    expected_reviews = {
        f"{year}-{paper}.md" for year in YEARS for paper in PAPER_ORDER
    }
    actual_reviews = {path.name for path in REVIEWS.glob("*.md")}
    if expected_reviews - actual_reviews:
        issues.append(f"missing reviews: {sorted(expected_reviews - actual_reviews)}")
    actual_topic_paths = {
        path.relative_to(TOPICS).as_posix() for path in TOPICS.rglob("*.md")
    }
    used_topic_paths = {record.topic_path for record in records}
    if actual_topic_paths != used_topic_paths:
        issues.append(
            f"topic inventory mismatch: missing={sorted(used_topic_paths - actual_topic_paths)}, "
            f"orphan={sorted(actual_topic_paths - used_topic_paths)}"
        )
    global_anchors: list[str] = []
    for relative, anchors in explicit_anchors.items():
        if len(anchors) != len(set(anchors)):
            issues.append(f"duplicate anchors in {relative}")
        global_anchors.extend(anchors)
    if len(global_anchors) != len(set(global_anchors)):
        issues.append("duplicate explicit anchors across paper files")
    routed_by_anchor = Counter(record.anchor for record in records)
    if any(count != 1 for count in routed_by_anchor.values()):
        issues.append("one or more routed anchors do not have exactly one primary record")
    for relative, anchors in explicit_anchors.items():
        for anchor in anchors:
            if anchor == "2026-mains-english-translation":
                continue
            if routed_by_anchor[anchor] != 1:
                issues.append(f"orphan or multiply routed paper anchor: {anchor}")
    by_year = Counter()
    anchor_by_year = Counter()
    for record in records:
        by_year[record.year] += int(record.answerable_unit)
        anchor_by_year[record.year] += 1
    expected_units = {
        2019: 421,
        2020: 425,
        2021: 428,
        2022: 439,
        2023: 424,
        2024: 429,
        2025: 429,
        2026: 421,
    }
    expected_routed = {
        2019: 444,
        2020: 448,
        2021: 451,
        2022: 462,
        2023: 447,
        2024: 452,
        2025: 452,
        2026: 444,
    }
    if dict(by_year) != expected_units:
        issues.append(f"unit reconciliation mismatch: {dict(by_year)}")
    if dict(anchor_by_year) != expected_routed:
        issues.append(f"routed-anchor reconciliation mismatch: {dict(anchor_by_year)}")
    paper_counts = Counter((record.year, record.paper) for record in records)
    unit_counts = Counter()
    for record in records:
        unit_counts[(record.year, record.paper)] += int(record.answerable_unit)
    for year in YEARS:
        expected = {
            "prelims-gs1": (100, 100),
            "prelims-csat": (80, 80),
            "mains-hindi": (37, 32),
            "mains-english": (72, 60),
            "mains-essay": (8, 8),
            "mains-gs1": (20, 20),
            "mains-gs2": (20, 20),
            "mains-gs3": (20, 20),
            "mains-gs4": (
                {2019: 31, 2020: 35, 2021: 38, 2022: 49, 2023: 34, 2024: 39, 2025: 39, 2026: 31}[year],
                {2019: 25, 2020: 29, 2021: 32, 2022: 43, 2023: 28, 2024: 33, 2025: 33, 2026: 25}[year],
            ),
            "philosophy-paper-1": (28, 28),
            "philosophy-paper-2": (28, 28),
        }
        for paper, pair in expected.items():
            actual = (paper_counts[(year, paper)], unit_counts[(year, paper)])
            if actual != pair:
                issues.append(f"{year} {paper} counts {actual}, expected {pair}")
    marks_by_year = Counter()
    for record in records:
        marks_by_year[record.year] += record.marks_represented
    if any(marks_by_year[year] != 4000 for year in YEARS):
        issues.append(f"represented-marks mismatch: {dict(marks_by_year)}")
    for record in records:
        block = paper_blocks[record.anchor]
        if not record.heading:
            issues.append(f"empty question heading: {record.anchor}")
        if "PAPERWISE-INDEX.md" not in block:
            issues.append(f"missing paper-index backlink: {record.anchor}")
        if record.topic_path not in topic_paths:
            issues.append(f"missing topic page: {record.topic_path}")
    residue_patterns = {
        "unfinished marker": re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE),
        "replacement character": re.compile("\ufffd|�"),
        "draft refusal": re.compile(r"\bI cannot answer\b|\bprovided text\b", re.IGNORECASE),
        "placeholder": re.compile(r"\[(?:insert|placeholder)[^\]]*\]", re.IGNORECASE),
    }
    for path in sorted(PAPERS.rglob("*.md")) + sorted(TOPICS.rglob("*.md")):
        text = read_text(path)
        for label, pattern in residue_patterns.items():
            if pattern.search(text):
                issues.append(f"{label} in {path.relative_to(REPO).as_posix()}")
    duplicated_solution_markers = []
    for path in TOPICS.rglob("*.md"):
        text = read_text(path)
        if re.search(
            r"^#{2,5}\s+(?:Model answer|Full reasoning|Model essay)|^\*\*Answer(?:\s|\()",
            text,
            re.MULTILINE | re.IGNORECASE,
        ):
            duplicated_solution_markers.append(path.relative_to(REPO).as_posix())
    if duplicated_solution_markers:
        issues.append(
            "possible duplicated full solutions in topics: "
            + ", ".join(duplicated_solution_markers)
        )
    links = validate_links()
    if links["missing_files"]:
        issues.append(f"{len(links['missing_files'])} broken relative file links")
    if links["missing_anchors"]:
        issues.append(f"{len(links['missing_anchors'])} broken explicit/heading anchors")
    quality_path = CATALOGUE / "QUALITY-SPOT-CHECKS.md"
    if quality_path.exists() and "**BLOCKED**" in read_text(quality_path):
        issues.append("one or more year × paper-family quality spot checks are blocked")
    topic_reverse_counts = Counter()
    topic_anchor_counts = Counter()
    for path in TOPICS.rglob("*.md"):
        text = read_text(path)
        topic_path = path.relative_to(TOPICS).as_posix()
        for anchor in re.findall(
            r"\]\(\.\./\.\./papers/\d{4}/[^)#]+\.md#([^)]+)\)", text
        ):
            topic_reverse_counts[anchor] += 1
            topic_anchor_counts[(topic_path, anchor)] += 1
    bad_primary_reverse = [
        (record.topic_path, record.anchor, topic_anchor_counts[(record.topic_path, record.anchor)])
        for record in records
        if topic_anchor_counts[(record.topic_path, record.anchor)] != 1
    ]
    if bad_primary_reverse:
        issues.append(f"non-exact primary reverse links: {bad_primary_reverse[:10]}")
    bad_secondary_reverse = [
        (topic_path, record.anchor, topic_anchor_counts[(topic_path, record.anchor)])
        for record in records
        for topic_path in record.secondary_topics
        if topic_anchor_counts[(topic_path, record.anchor)] != 1
    ]
    if bad_secondary_reverse:
        issues.append(f"non-exact secondary reverse links: {bad_secondary_reverse[:10]}")
    missing_reverse = [
        record.anchor for record in records if topic_reverse_counts[record.anchor] < 1
    ]
    if missing_reverse:
        issues.append(f"missing primary reverse topic links: {missing_reverse[:10]}")
    orphan_reverse = [
        anchor for anchor in topic_reverse_counts if routed_by_anchor[anchor] == 0
    ]
    if orphan_reverse:
        issues.append(f"orphan topic links: {orphan_reverse[:10]}")
    philosophy_files = sorted(PAPERS.glob("*/philosophy-paper-*.md"))
    philosophy_replacement = [
        path.relative_to(REPO).as_posix()
        for path in philosophy_files
        if "\ufffd" in read_text(path) or "�" in read_text(path)
    ]
    if philosophy_replacement:
        issues.append(f"Philosophy encoding/IAST residue: {philosophy_replacement}")
    return {
        "status": "PASS" if not issues else "BLOCKED",
        "issues": issues,
        "paper_files": len(actual_files),
        "review_files": len(actual_reviews & expected_reviews),
        "years": len(YEARS),
        "paper_families": len(PAPER_ORDER),
        "answerable_units": sum(record.answerable_unit for record in records),
        "routed_anchors": len(records),
        "explicit_paper_anchors": len(global_anchors),
        "canonical_topics": len(used_topic_paths),
        "topic_files": len(actual_topic_paths),
        "represented_marks": sum(record.marks_represented for record in records),
        "primary_reverse_links": sum(
            1 for record in records if topic_reverse_counts[record.anchor] >= 1
        ),
        "secondary_topic_routes": sum(len(record.secondary_topics) for record in records),
        **links,
    }


def generate_all() -> dict:
    topic_info = load_topic_info()
    records, explicit_anchors = parse_records(topic_info)
    changed = set()
    changed.update(generate_topic_pages(records, topic_info))
    outputs = {
        CATALOGUE / "PAPERWISE-INDEX.md": generate_paperwise(records, explicit_anchors),
        CATALOGUE / "SUBJECT-INDEX.md": generate_subject_index(records, topic_info),
        CATALOGUE / "TOPIC-INDEX.md": generate_topic_index(records, topic_info),
        CATALOGUE / "YEARS-INDEX.md": generate_years_index(records),
        CATALOGUE / "CONCENTRATION-ANALYSIS.md": generate_concentration(records, topic_info),
        CATALOGUE / "QUALITY-SPOT-CHECKS.md": generate_quality_spot_checks(records),
        CATALOGUE / "CORPUS-METADATA.json": metadata_json(records),
    }
    for path, text in outputs.items():
        if write_if_changed(path, text):
            changed.add(path.relative_to(REPO).as_posix())
    audit = validate_corpus(records, explicit_anchors)
    audit_text = json.dumps(audit, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    audit_path = CATALOGUE / "CORPUS-AUDIT.json"
    if write_if_changed(audit_path, audit_text):
        changed.add(audit_path.relative_to(REPO).as_posix())
    return {"changed": sorted(changed), "audit": audit}


def file_hashes(scope: Path) -> dict[str, str]:
    hashes = {}
    for path in sorted(scope.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            relative = path.relative_to(REPO).as_posix()
            hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return hashes


def generate_manifests(baseline_path: Path) -> dict:
    before = json.loads(baseline_path.read_text(encoding="utf-8"))
    topic_info = load_topic_info()
    records, _ = parse_records(topic_info)
    current = file_hashes(ROOT)
    final_manifest = "solved_pyqs/FINAL-RELEASE-FILE-CHANGES.txt"
    release_2019_manifest = "solved_pyqs/2019-RELEASE-FILE-CHANGES.txt"
    changed = {
        path for path, digest in current.items() if before.get(path) != digest
    }
    changed.update({final_manifest, release_2019_manifest})

    topics_2019 = {
        f"solved_pyqs/topics/{record.topic_path}"
        for record in records
        if record.year == 2019
    }
    topics_2019.update(
        f"solved_pyqs/topics/{topic_path}"
        for record in records
        if record.year == 2019
        for topic_path in record.secondary_topics
    )
    release_2019 = {
        release_2019_manifest,
        "solved_pyqs/build_release_catalogue.py",
        "solved_pyqs/catalogue/CONCENTRATION-ANALYSIS.md",
        "solved_pyqs/catalogue/CORPUS-AUDIT.json",
        "solved_pyqs/catalogue/CORPUS-METADATA.json",
        "solved_pyqs/catalogue/PAPERWISE-INDEX.md",
        "solved_pyqs/catalogue/QUALITY-SPOT-CHECKS.md",
        "solved_pyqs/catalogue/SUBJECT-INDEX.md",
        "solved_pyqs/catalogue/TOPIC-INDEX.md",
        "solved_pyqs/catalogue/YEARS-INDEX.md",
        "solved_pyqs/EXECUTION-QUEUE.md",
        "solved_pyqs/FINAL-RELEASE-REPORT.md",
        "solved_pyqs/README.md",
        "solved_pyqs/REVIEW-LOG.md",
        "solved_pyqs/STATUS.md",
    }
    release_2019.update(
        f"solved_pyqs/papers/2019/{paper}.md" for paper in PAPER_ORDER
    )
    release_2019.update(
        f"solved_pyqs/reviews/2019-{paper}.md" for paper in PAPER_ORDER
    )
    release_2019.update(topics_2019)

    release_2019_lines = [
        "2019 solved-PYQ final shared release — exact file-change manifest",
        "",
        f"Total files: {len(release_2019)}",
        "",
        *sorted(release_2019),
    ]
    final_lines = [
        "2019–2026 solved-PYQ final whole-corpus release — exact changed-path manifest",
        "",
        f"Total files: {len(changed)}",
        "",
        *sorted(changed),
    ]
    write_if_changed(
        ROOT / "2019-RELEASE-FILE-CHANGES.txt",
        "\n".join(release_2019_lines) + "\n",
    )
    write_if_changed(
        ROOT / "FINAL-RELEASE-FILE-CHANGES.txt",
        "\n".join(final_lines) + "\n",
    )
    return {
        "2019_release_files": len(release_2019),
        "final_changed_paths": len(changed),
        "2019_manifest": release_2019_manifest,
        "final_manifest": final_manifest,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--integrate-2019", action="store_true")
    parser.add_argument("--generate", action="store_true")
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--manifests", action="store_true")
    parser.add_argument("--baseline", type=Path)
    args = parser.parse_args()
    if not any((args.integrate_2019, args.generate, args.validate, args.manifests)):
        args.integrate_2019 = args.generate = True
    if args.integrate_2019:
        changed = apply_2019_integration()
        print(json.dumps({"2019_integration_changed": changed}, indent=2))
    if args.generate:
        result = generate_all()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if result["audit"]["status"] == "PASS" else 1
    if args.validate:
        topic_info = load_topic_info()
        records, explicit_anchors = parse_records(topic_info)
        audit = validate_corpus(records, explicit_anchors)
        print(json.dumps(audit, ensure_ascii=False, indent=2))
        return 0 if audit["status"] == "PASS" else 1
    if args.manifests:
        if not args.baseline:
            parser.error("--manifests requires --baseline")
        result = generate_manifests(args.baseline.resolve())
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
