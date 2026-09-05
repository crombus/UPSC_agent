"""Assemble Medieval History learner-v2 Topics 01-02 and authored visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_ancient_history_17_21_sequential as base


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
GRAPHICAL_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-01-02-2026-08-30-sequential.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "medieval-indian-history--subject-wide-syllabus.json"
)
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SATISH_HISTORY = (
    ROOT / "books" / "medival_history" / "Satish Chandra History of Medieval India.pdf"
)
SATISH_SULTANAT = (
    ROOT
    / "books"
    / "medival_history"
    / "dokumen.pub_medieval-india-from-sultanat-to-the-mughals-part-i-8124119899-9788124119891.pdf"
)

COMMON_CROSS = [
    "upsc-ai-kit\\knowledge\\Medieval-Indian-History\\00_Master-Chronology.md",
    "upsc-ai-kit\\knowledge\\Medieval-Indian-History\\README.md",
    "upsc-ai-kit\\knowledge\\Medieval-Indian-History\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    "upsc-ai-kit\\knowledge\\Medieval-Indian-History\\ANSWER-WORTHINESS-AUDIT.md",
    "upsc-ai-kit\\knowledge\\Medieval-Indian-History\\REVISION-CHART_Ages-Eras-and-Distinctive-Features.md",
    "upsc-ai-kit\\knowledge\\Medieval-Indian-History\\LEARNING-SESSION-COMMAND-INDEX.md",
]
PYQ_INDEXES = [
    "upsc-ai-kit\\knowledge\\_PYQ-INDEX.md",
    "upsc-ai-kit\\knowledge\\PYQ-INTEGRATION-AUDIT-2018-2023.md",
    "upsc-ai-kit\\knowledge\\PYQ-INTEGRATION-AUDIT-2024-2025.md",
    "upsc-ai-kit\\knowledge\\PYQ-INTEGRATION-AUDIT-2026.md",
]


def config(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    legacy_main: str,
    legacy_workbook: str,
    practice_profile: str,
    live_sources: list[str],
    current_note: str,
    extra_markdown: list[str] | None = None,
) -> dict[str, object]:
    key = f"medieval-indian-history-{number:02d}"
    return {
        "number": number,
        "key": key,
        "title": title,
        "canonical": KNOWLEDGE / canonical,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "legacy_main": ROOT / "notes" / SUBJECT / legacy_main,
        "legacy_workbook": ROOT / "notes" / SUBJECT / legacy_workbook,
        "practice_profile": practice_profile,
        "live_sources": live_sources,
        "current_note": current_note,
        "extra_markdown": [KNOWLEDGE / item for item in (extra_markdown or [])],
    }


TOPICS = [
    config(
        1,
        "India on the Eve of the Medieval Age & Arab-Turkish Contacts",
        "01_India-on-the-Eve-of-the-Medieval-Age-Arab-Turkish-Contacts_Complete-Topic-Package.md",
        "01_India-on-the-Eve-of-Medieval-Age.md",
        "01_India-on-the-Eve-of-Medieval-Age.md",
        "01_India-on-the-Eve-Arab-Turkish-Contacts_Complete-Topic-Package_2026-08-10.pdf",
        "01_India-on-the-Eve-Arab-Turkish-Contacts_Solved-Workbook_2026-08-10.pdf",
        "7 routed application PYQs; 16 learning, 32 workbook and 8 remedial "
        "MCQs; 16 original solved Mains questions.",
        [
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2191073",
            "https://whc.unesco.org/en/statesparties/in",
        ],
        "The November 2025 Archaeological Survey of India workshop on Project "
        "Mausam was rechecked on 30 August 2026. It provides a bounded modern "
        "link to documentation of Indian Ocean movement, ports and cultural "
        "exchange. It does not prove any specific early Indo-Arab route, date "
        "or settlement without the medieval textual and archaeological record.",
        [
            "learning-sessions\\India-on-Eve-Arab-Turkish-Contacts_Complete-Learning-Session_2026-08-10.md",
            "learning-sessions\\India-on-Eve-Arab-Turkish-Contacts_Premium-Solved-PYQ-Workbook_2026-08-10.md",
        ],
    ),
    config(
        2,
        "The Ghaznavids & the Ghurian Invasions",
        "02_Ghaznavids-Ghurian-Invasions_Complete-Topic-Package.md",
        "02_Ghaznavids-and-Ghurian-Invasions.md",
        "02_Ghaznavids-and-Ghurian-Invasions.md",
        "02_Ghaznavids-Ghurian-Invasions_Complete-Topic-Package_2026-08-13.pdf",
        "02_Ghaznavids-Ghurian-Invasions_Solved-Workbook_2026-08-13.pdf",
        "3 verified/routed PYQs; 48 hard and 12 remedial MCQs; 9 original "
        "solved Mains questions.",
        [
            "https://whc.unesco.org/en/list/211",
            "https://www.unesco.org/en/culture-emergencies/heritage-emergency-fund/urgent-repairs-monuments-and-emergency-protective-measures-archaeological-sites-kabul-zabul-and",
            "https://whc.unesco.org/en/list/233/",
        ],
        "UNESCO's Minaret and Archaeological Remains of Jam record was rechecked "
        "on 30 August 2026. It confirms the 1194 Ghurid monument, its influence "
        "on later architecture including the Qutb Minar, and continuing "
        "conservation requirements. This heritage linkage does not establish "
        "campaign chronology, motives or territorial control.",
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-01": [
        (
            "Transition without a political vacuum",
            "network-map",
            """PALA ---- PRATIHARA ---- RASHTRAKUTA competitive order
                         |
                 regional redistribution
                         |
GAHADAVALA | CHAUHAN | PARAMARA | CHALUKYA | CHANDELLA | TOMARA
SOUTHERN AXIS -> Chola state, ports and Indian Ocean networks
VERDICT: substantial state capacity survived; pooled command remained difficult.""",
            ["Political setting", "Regional successor states"],
        ),
        (
            "Four contact layers",
            "comparison-matrix",
            """COMMERCIAL -> Arab and Indian merchants, ports and monsoon routes
CULTURAL -> numerals, astronomy, medicine, language and translation
FRONTIER -> Sind, Kabul, Zabul, Jalalabad and Punjab
MILITARY-INSTITUTIONAL -> cavalry, roads, iqta logic and concentrated command
RULE: contact preceded conquest, and the four layers changed at different speeds.""",
            ["Scope", "Arab-Turkish distinction"],
        ),
        (
            "Chronology of contact and frontier change",
            "timeline",
            """711-12 -> Arab conquest of Sind
8th-10th c. -> Arab settlements and trade strengthen on the Malabar coast
963 -> Alp-tigin establishes himself at Ghazni
990-91 -> Hindu Shahi frontier setback around Kabul-Jalalabad
1173 -> Muizz al-Din takes Ghazni
1191 / 1192 -> First and Second Battles of Tarain
1206 -> independent Delhi Sultanate consolidation begins after Ghurid rupture.""",
            ["Chronology", "Transition"],
        ),
        (
            "Monsoon maritime circuit",
            "network-map",
            """PERSIAN GULF / RED SEA
          |
Arab and Indian merchants + monsoon navigation
          |
GUJARAT COAST ---- MALABAR COAST ---- SRI LANKA / SOUTHEAST ASIA
          |
goods + resident communities + worship spaces + knowledge
LIMIT: a mosque or merchant settlement does not prove foreign sovereignty.""",
            ["Arab maritime trade", "Malabar"],
        ),
        (
            "Sind as conquest and conduit",
            "cause-mechanism-effect",
            """ARAB POLITICAL FOOTHOLD IN SIND
             |
frontier towns + administrators + scholars + merchant routes
             |
translation and circulation of numerals, astronomy and medicine
             |
INDO-ARAB INTELLECTUAL CONTACT
CAUTION: Sind did not create a straight political line to the Sultanate.""",
            ["Sind", "Knowledge transfer"],
        ),
        (
            "Formation of the Persianate-Turkish package",
            "process",
            """ABBASID FRAGMENTATION
        |
regional Iranian and Central Asian military states
        |
Turkic commanders + Islamisation + Persian language and court culture
        |
cavalry command + documentary kingship + revenue-service institutions
TRAP: Persianate describes culture and administration, not ethnicity.""",
            ["Persianisation", "Turkish military elites"],
        ),
        (
            "Frontier depth and the outer bastions",
            "spatial-timeline",
            """CENTRAL ASIA -> GHAZNI -> KABUL -> JALALABAD -> PUNJAB -> GANGA PLAIN
                         roads, bases, supply and intelligence
HINDU SHAHI CONTROL -> strategic depth
SHAHI LOSSES + PUNJAB BASE -> shorter operational corridor
COUNTER-EVIDENCE -> Gujarat 1178-79 and Tarain 1191 defeats
VERDICT: access enabled campaigns; it did not determine victory.""",
            ["Hindu Shahis", "Outer bastions", "Frontier logistics"],
        ),
        (
            "Rajput capacity and coordination",
            "comparison",
            """STRENGTHS                         LIMITS
agrarian revenue                   rival sovereign centres
forts and feudatory armies         uneven intelligence sharing
regional legitimacy               delayed pooled reinforcement
Gujarat and Tarain I victories     Prithviraj's political isolation
VERDICT: courage and capacity existed; durable common command was weaker.""",
            ["Rajput political order", "Coordination"],
        ),
        (
            "Military-fiscal interaction",
            "cause-mechanism-effect",
            """REVENUE ASSIGNMENT / IQTA LOGIC -> maintained mounted force
ROADS + BASES + REMOUNTS -> mobility and operational endurance
RECONNAISSANCE + RESERVES -> tactical flexibility
CONCENTRATED COMMAND -> rapid decision and reinforcement
NO SINGLE CAUSE: horses without finance, roads and command were insufficient.""",
            ["Iqta", "Cavalry", "Military organisation"],
        ),
        (
            "Condition, mechanism and trigger",
            "argument-tree",
            """CONDITION -> frontier-depth loss + regional rivalry
MECHANISM -> mobility + fiscal concentration + logistics + command
TRIGGER -> leadership + diplomacy + tactical adaptation
COUNTERFACT -> Turkish reverses show structures changed odds, not certainty
FINAL FORMULA: probability, not inevitability; organisation, not race.""",
            ["Causation", "Contingency"],
        ),
        (
            "Evidence discipline",
            "evidence-matrix",
            """TRAVELLERS -> routes and perceptions | itinerary and outsider limits
CHRONICLES -> court claims and campaigns | patronage and rhetoric
COINS -> titles and circulation | not automatic border maps
INSCRIPTIONS -> local claims and genealogy | formula and survival bias
ARCHAEOLOGY -> ports and settlements | identification and dating cautions
METHOD: claim -> named evidence -> corroboration -> explicit limit.""",
            ["Sources", "Historical method"],
        ),
        (
            "Topic 01 answer spine",
            "answer-synthesis",
            """OPEN -> India was connected and politically regionalised, not isolated
SEA -> trade, settlements and knowledge without automatic conquest
WEST/CENTRAL ASIA -> Persianised Turkish military states
FRONTIER -> Shahi depth, roads and Punjab base
POLITY -> Rajput capacity plus coordination limits
CAUSATION -> condition + mechanism + contingent trigger
CLOSE -> interaction and institutional recombination shaped the transition.""",
            ["Answer architecture", "Synthesis"],
        ),
    ],
    "medieval-indian-history-02": [
        (
            "Three phases that must remain separate",
            "timeline",
            """GHAZNAVID PHASE             GHURID PHASE              DELHI SULTANATE
c. 990s-1186               1175-1206                from 1206
frontier war + raids       territorial bridgehead   Indian-centred consolidation
Punjab / Lahore base       Delhi-doab expansion      Aibak and Iltutmish
Mahmud != Muizz al-Din != Aibak.""",
            ["Scope", "Core distinctions"],
        ),
        (
            "Campaign chronology",
            "timeline",
            """963 -> Alp-tigin at Ghazni | 977 -> Sabuktigin
1001 -> Jayapala defeated | 1009 -> Anandapala defeated
1025-26 -> Somnath campaign | 1186 -> Ghurids take Lahore
1191 -> Tarain I, Ghurid defeat | 1192 -> Tarain II, Ghurid victory
1194 -> Chandawar | 1206 -> Muizz al-Din dies
RULE: battlefield victory and durable consolidation are different stages.""",
            ["Chronology", "Campaign sequence"],
        ),
        (
            "Source criticism matrix",
            "evidence-matrix",
            """AL-UTBI -> Ghaznavid court claims | panegyric; ends before Somnath
AL-BIRUNI -> comparative inquiry | elite textual and regional limits
BAYHAQI -> court and administration | fragmentary survival
HASAN NIZAMI -> early conquest | ornate Aibak-linked legitimation
MINHAJ -> Ghurid-Delhi sequence | written decades later
COINS / INSCRIPTIONS -> titles and local claims | require contextual reading.""",
            ["Sources", "Historiography"],
        ),
        (
            "From Samanid service to Ghaznavid rule",
            "process",
            """SAMANID PERSIANATE COURT
          |
Turkic military commanders and service networks
          |
Alp-tigin at Ghazni -> Sabuktigin -> Mahmud
          |
roads, cavalry, taxation, court culture and frontier warfare
VERDICT: a state-formation process, not an ethnic migration explanation.""",
            ["Samanids", "Ghaznavid rise"],
        ),
        (
            "Hindu Shahi resistance and frontier breach",
            "spatial-timeline",
            """KABUL / JALALABAD -> PESHAWAR -> SALT RANGE -> PUNJAB
        Hindu Shahi strategic depth and fortified corridors
Sabuktigin pressure -> Jayapala 1001 -> Anandapala 1009 -> Nandana
Kashmir 1015 failure -> weather and terrain still constrained Ghaznavids
VERDICT: prolonged resistance preceded a changing Punjab frontier.""",
            ["Hindu Shahis", "Punjab"],
        ),
        (
            "Mahmud's campaigns: reach and limits",
            "network-map",
            """DURABLE BASE -> Ghazni + Punjab / Lahore
REPEATED TARGETS -> frontier forts, Multan, Mathura-Kanauj and Somnath
METHODS -> campaigning, tribute, plunder, garrisons and local arrangements
LIMITS -> no comparable permanent Ghaznavid Gangetic administration
RULE: repeated deep raids do not equal uniform territorial occupation.""",
            ["Mahmud's campaigns", "Territorial limits"],
        ),
        (
            "Mahmud's motives as a matrix",
            "comparison-matrix",
            """FISCAL -> movable wealth and military finance
STRATEGIC -> rivals, frontier security and Punjab control
POLITICAL -> prestige and dynastic legitimation
RELIGIOUS -> ghazi and iconoclast rhetoric
CULTURAL -> court patronage and Persianate kingship
VERDICT: motives reinforced one another and varied by campaign.""",
            ["Motives", "Multi-causal analysis"],
        ),
        (
            "Somnath and al-Biruni: event versus evidence",
            "evidence-chain",
            """SOMNATH EVENT -> later textual layers, memory and political reuse
AL-UTBI -> cannot narrate 1025 because his account ends earlier
AL-BIRUNI -> scholarship on Indian learning, not a neutral social census
MATERIAL / REGIONAL EVIDENCE -> checks court and later literary claims
METHOD: identify date, genre, patron, report, corroboration and limit.""",
            ["Somnath", "Al-Biruni", "Source criticism"],
        ),
        (
            "Ghaznavid and Ghurid projects compared",
            "comparison",
            """GHAZNAVIDS                        GHURIDS
Punjab bridgehead + raids          staged territorial advance
Ghazni-Lahore axis                 Multan-Punjab-Delhi-doab axis
deep campaigns, limited plains     commanders, garrisons and vassalage
state focus remained westward      wider north Indian succession problem
LINK: Ghurids displaced the last Ghaznavid at Lahore in 1186.""",
            ["Ghaznavids", "Ghurids", "Comparison"],
        ),
        (
            "Tarain I and II",
            "comparison-matrix",
            """1191 TARAIN I                    1192 TARAIN II
Ghurid defeat                      Ghurid return and victory
Rajput capacity demonstrated       mounted harassment and reserves matter
no inevitable Turkish success      learning and command alter outcome
AFTERMATH -> occupation remained uneven; forts, rebellions and local deals continued.""",
            ["Tarain", "Contingency"],
        ),
        (
            "Battlefield victory to consolidation",
            "process",
            """VICTORY
  -> commander delegation and garrisons
  -> vassalage, tribute and negotiated local rule
  -> revenue access and route security
  -> suppression of rebellions and rival Turkish claims
  -> post-1206 Aibak-Iltutmish consolidation
TRAP: Ghurid opening != instantly complete Delhi Sultanate.""",
            ["Aibak", "Conquest and consolidation"],
        ),
        (
            "Topic 02 answer spine",
            "answer-synthesis",
            """OPEN -> distinguish Ghaznavid raid-base pattern from Ghurid advance
CONTEXT -> Samanids, military service, roads and frontier geography
MAHMUD -> campaigns + motives + Punjab base + limits
GHURIDS -> Lahore, Tarain, Chandawar and delegated occupation
CAUSES -> organisation and contingency, not racial or weapon determinism
SOURCES -> court rhetoric checked by texts, coins and monuments
CLOSE -> conquest opened a process; consolidation remained contested.""",
            ["Answer architecture", "Synthesis"],
        ),
    ],
}


REMEDIAL_MCQS = """### Remedial correction MCQs

#### Remedial MCQ 01
Which correction best addresses the claim that Sind immediately created the Delhi Sultanate?
- A. Sind was a regional foothold and conduit; different actors and institutions produced the later Sultanate.
- B. Sind and Delhi were ruled continuously by one dynasty after 712.
- C. Arab maritime trade began only after 1206.
- D. The Ghaznavids conquered Sind in the eighth century.
**Answer: A.** The Arab conquest of Sind and the Ghurid-Sultanate transition were separated by centuries.

#### Remedial MCQ 02
What does Persianate most accurately describe in this context?
- A. Persian biological ancestry.
- B. A sphere of Persian language, court culture, literature and administration.
- C. Rejection of Islam by Turkish commanders.
- D. Replacement of every Indian language.
**Answer: B.** Persianisation was cultural and institutional, not an ethnic category.

#### Remedial MCQ 03
Which statement correctly defines iqta in the pre-Sultanate transition?
- A. Unrestricted hereditary ownership of cultivators.
- B. A temple tax collected only at ports.
- C. A ruler-controlled revenue assignment associated with service and troop maintenance.
- D. A Rajput clan council.
**Answer: C.** The assignment supported service obligations and did not automatically transfer full property rights.

#### Remedial MCQ 04
Which is the best correction to the claim that Rajput states had no resources?
- A. They had no forts but controlled all cavalry imports.
- B. They formed a permanent all-India confederacy.
- C. Their only weakness was inferior personal courage.
- D. Several had substantial revenue and armies, but durable inter-state coordination was difficult.
**Answer: D.** The central distinction is individual state capacity versus pooled command.

#### Remedial MCQ 05
Why is cavalry alone an insufficient explanation of Turkish success?
- A. Mobility worked through finance, logistics, intelligence, command and tactics.
- B. Horses were absent from West and Central Asia.
- C. Every mounted army won every battle.
- D. Infantry played no role in medieval warfare.
**Answer: A.** Military advantage was an organisational system rather than a single weapon.

#### Remedial MCQ 06
What can a permitted mosque in a merchant settlement establish most securely?
- A. Immediate foreign annexation.
- B. A resident community and local accommodation.
- C. Abolition of Indian Ocean trade.
- D. Uniform conversion of the surrounding population.
**Answer: B.** Religious infrastructure does not by itself prove transferred sovereignty.

#### Remedial MCQ 07
Why should the north-west not be described as an eternally open gate?
- A. No army crossed it before 1206.
- B. Geography had no strategic importance.
- C. Routes became operational through political control, roads, bases, supply and intelligence.
- D. Punjab was separated from Central Asia by the sea.
**Answer: C.** Terrain created opportunities and constraints that states had to organise.

#### Remedial MCQ 08
What is the correct use of digitised manuscripts in historical reconstruction?
- A. Digitisation proves every manuscript is contemporary with the event.
- B. Digital access removes genre and patronage bias.
- C. A repository replaces archaeological corroboration.
- D. Digitisation improves access, while dating, editing, translation and criticism remain necessary.
**Answer: D.** Access and evidentiary reliability are separate questions.
"""


def normalize_objective_syntax(fragment: str, prefix: str | None = None) -> str:
    text = fragment.replace("\r\n", "\n")
    if prefix:
        text = re.sub(
            r"(?m)^### Q(\d+)[ \t]*$",
            lambda match: f"### {prefix} MCQ {int(match.group(1)):02d}",
            text,
        )
        text = re.sub(
            r"(?m)^## Q(\d+)[ \t]*$",
            lambda match: f"## {prefix} MCQ {int(match.group(1)):02d}",
            text,
        )
    text = re.sub(
        r"(?m)^\(([a-d])\)\s+",
        lambda match: f"- {match.group(1).upper()}. ",
        text,
    )
    text = re.sub(
        r"(?m)^>[ \t]*✅[ \t]*\*\*Answer:[ \t]*\(([a-d])\)\.\*\*[ \t]*",
        lambda match: f"**Answer: {match.group(1).upper()}.** - ",
        text,
    )
    text = re.sub(
        r"(?m)^>\s*⚠️\s*\*\*INFERRED ANSWER[^:]*:\s*\(([a-d])\)",
        lambda match: f"> **Inferred answer: {match.group(1).upper()}.**",
        text,
    )
    return text


def assemble_topic_01(config_value: dict[str, object]) -> str:
    learning_path, workbook_path = [
        Path(path) for path in config_value["extra_markdown"]
    ]
    learning = learning_path.read_text(encoding="utf-8")
    learning = re.sub(
        r"(?m)^\*\*Date:\*\*.*\*\*Progress:\*\*.*$\n*",
        "",
        learning,
    )
    learning = re.sub(r"(?m)^Progress:\s+.*$\n*", "", learning)
    workbook = workbook_path.read_text(encoding="utf-8")
    learning_preamble, learning_sections = base.split_h2(learning)
    _, workbook_sections = base.split_h2(workbook)
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in learning_sections:
        if title.startswith("MCQ loop"):
            bucket = "mcq"
            fragment = normalize_objective_syntax(fragment, "Learning")
            fragment = re.sub(
                r"(?m)^## MCQ loop \d+[ \t]*$\n*",
                "",
                fragment,
            )
            fragment = fragment.replace("### Learning MCQ", "## Learning MCQ")
        elif title.startswith(("PYQ integration", "Original Mains practice")):
            continue
        elif title.startswith("R."):
            bucket = "register"
        else:
            bucket = "basic"
        if title == "Revision notes":
            fragment = fragment.replace(
                "## Revision notes",
                "### Revision notes",
                1,
            )
        normalized = base.normalize_fragment(fragment)
        if title in {"Sources actually used", "SOURCE-COVERAGE LEDGER — proof that BOTH mandatory files are integrated"}:
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        grouped[bucket].append(normalized)

    for title, fragment in workbook_sections:
        if title.startswith("Q"):
            bucket = "mcq"
            fragment = fragment.split("# PART IV", 1)[0]
            fragment = normalize_objective_syntax(fragment, "Workbook")
        elif title == "Workbook contents":
            bucket = "basic"
        elif title.startswith(("I.", "M-", "O-")):
            bucket = "practice"
        elif title.startswith(("Forbidden sentences", "Final self-test")):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 01 workbook section: {title}")
        grouped[bucket].append(base.normalize_fragment(fragment))

    grouped["mcq"].append(REMEDIAL_MCQS)
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "This linkage supplies present heritage-method context only. Repository "
        "chronology, OCR-searchable book evidence and source criticism control "
        "the historical claims."
    )
    advanced = base.normalize_fragment(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    return (
        f"# {config_value['title']} - Complete Topic Package\n\n"
        f"{base.strip_title(learning_preamble)}\n\n"
        "## BASIC LEARNING SESSION\n\n"
        + "\n\n".join(grouped["basic"])
        + "\n\n"
        + current
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + "\n\n".join(grouped["mcq"])
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + "\n\n".join(grouped["practice"])
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + advanced
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "\n\n".join(grouped["register"])
        + "\n"
    )


def classify_topic_02(title: str) -> str:
    if title.startswith(("Package practice", "Sources actually", "PART I")):
        return "basic"
    if re.match(r"^\d{2}\.", title):
        return "basic"
    if title.startswith("PART II") or title.startswith("PYQ "):
        return "practice"
    if title.startswith("PART III") or title.startswith(("Hard MCQ", "Remedial MCQ")):
        return "mcq"
    if title.startswith("PART IV") or title.startswith("Mains "):
        return "practice"
    if title.startswith("PART V") or title.startswith("FINAL REGISTER"):
        return "register"
    raise ValueError(f"Unclassified Topic 02 section: {title}")


def assemble_topic_02(config_value: dict[str, object]) -> str:
    canonical = Path(config_value["canonical"])
    source = canonical.read_text(encoding="utf-8")
    preamble, sections = base.split_h2(source)
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        bucket = classify_topic_02(title)
        normalized = base.normalize_fragment(fragment)
        if title.startswith(("Package practice", "Sources actually", "PART ")):
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        grouped[bucket].append(normalized)
    advanced = base.normalize_fragment(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "The UNESCO material supports heritage attribution and conservation "
        "context only. It does not override medieval textual, numismatic, "
        "epigraphic or archaeological evidence."
    )
    return (
        f"# {config_value['title']} - Complete Topic Package\n\n"
        f"{base.strip_title(preamble)}\n\n"
        "## BASIC LEARNING SESSION\n\n"
        + "\n\n".join(grouped["basic"])
        + "\n\n"
        + current
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + "\n\n".join(grouped["mcq"])
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + "\n\n".join(grouped["practice"])
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + advanced
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "\n\n".join(grouped["register"])
        + "\n"
    )


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-01":
        return assemble_topic_01(config_value)
    return assemble_topic_02(config_value)


def write_ascii_spec() -> None:
    topics: list[dict[str, object]] = []
    for config_value in TOPICS:
        key = str(config_value["key"])
        panels = []
        for title, structural_type, body, references in PANEL_DATA[key]:
            lines = body.splitlines()
            if max(map(len, lines)) > 100:
                raise ValueError(
                    f"{key}: ASCII line exceeds 100 characters in {title!r}"
                )
            panels.append(
                {
                    "title": title,
                    "structural_type": structural_type,
                    "ascii_lines": lines,
                    "source_references": references,
                }
            )
        if len(panels) != 12:
            raise ValueError(f"{key}: expected 12 panels, found {len(panels)}")
        topics.append(
            {
                "topic_key": key,
                "display_title": config_value["title"],
                "source_markdown": base.relative(Path(config_value["canonical"])),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Medieval Indian History learner-v2 Topics 01-02",
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "complete_embed_ready_lines": True,
            "tracker_untouched": True,
        },
        "topics": topics,
    }
    ASCII_DIR.mkdir(parents=True, exist_ok=True)
    ASCII_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_graphical_spec(config_value: dict[str, object], markdown: str) -> Path:
    key = str(config_value["key"])
    panel_records = [
        {
            "title": title,
            "body": body,
            "structural_type": structural_type,
            "source_references": references,
        }
        for title, structural_type, body, references in PANEL_DATA[key]
    ]
    source_path = SESSION_DIR / f"{key}_Learning-Session.md"
    spec = carvaka_flowchart.author_topic_spec(
        topic_key=key,
        subject=SUBJECT,
        title=str(config_value["title"]),
        source_markdown=markdown,
        source_markdown_path=base.relative(source_path),
        ascii_spec_path=base.relative(ASCII_PATH),
        ascii_spec_sha256=hashlib.sha256(ASCII_PATH.read_bytes()).hexdigest(),
        panels=panel_records,
        source_generation=1,
    )
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{key}.json"
    output.write_text(
        json.dumps(spec, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def write_generation_spec(
    config_value: dict[str, object],
    source_path: Path,
    graphical_path: Path,
) -> Path:
    key = str(config_value["key"])
    local_books = [SATISH_HISTORY, SATISH_SULTANAT]
    source_files = [
        Path(config_value["basic"]),
        Path(config_value["advanced"]),
        Path(config_value["canonical"]),
        *[Path(path) for path in config_value["extra_markdown"]],
        source_path,
        *[ROOT / item for item in COMMON_CROSS],
        *[ROOT / item for item in PYQ_INDEXES],
        *local_books,
        Path(config_value["legacy_main"]),
        Path(config_value["legacy_workbook"]),
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *base.image_sources(Path(config_value["canonical"])),
    ]
    deduplicated: list[Path] = []
    for path in source_files:
        resolved = path.resolve()
        if resolved not in deduplicated:
            deduplicated.append(resolved)
    missing = [str(path) for path in deduplicated if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    payload = {
        "schema_version": 1,
        "topic_key": key,
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "topic_folder": key,
        "title": config_value["title"],
        "generation_date": DATE,
        "command": (
            "Generate learner-v2 topic: Medieval History — Subject-wide Syllabus — "
            + str(config_value["title"])
        ),
        "source_markdown": base.relative(source_path),
        "source_basic": base.relative(Path(config_value["basic"])),
        "source_canonical": base.relative(Path(config_value["canonical"])),
        "source_advanced": base.relative(Path(config_value["advanced"])),
        "manifest": base.relative(SECTION_MANIFEST),
        "cross_topic_sources": COMMON_CROSS,
        "pyq_indexes": PYQ_INDEXES,
        "official_question_sources": [],
        "local_ocr_sources": [base.relative(path) for path in local_books],
        "live_sources": config_value["live_sources"],
        "source_files": [base.relative(path) for path in deduplicated],
        "practice_profile": config_value["practice_profile"],
        "current_linkage_note": config_value["current_note"],
        "pyq_status_note": (
            "Locally held papers and routing ledgers control wording and ownership; "
            "unavailable official keys remain explicitly inferred or provisional."
        ),
        "mcq_answer_policy": "strict-abcd-cycle",
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{key}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def main() -> int:
    write_ascii_spec()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH]
    for config_value in TOPICS:
        key = str(config_value["key"])
        markdown = assemble(config_value)
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        source_path.write_text(markdown, encoding="utf-8")
        graphical_path = write_graphical_spec(config_value, markdown)
        generation_spec = write_generation_spec(
            config_value,
            source_path,
            graphical_path,
        )
        written.extend([source_path, graphical_path, generation_spec])
    for path in written:
        print(base.relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
