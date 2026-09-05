"""Assemble Modern Indian History learner-v2 Topics 07-08 and visual specs.

This authoring-only generator writes Markdown and JSON specifications. It does
not render PDFs, stage files, finalise tracker records, or modify approval state.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import generate_modern_history_03_04_sequential as base
import notions_style_ascii_master as ascii_master


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Modern-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_PATH = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "modern-indian-history-07-08-2026-08-30-sequential.json"
)
GRAPHICAL_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "modern-indian-history--subject-wide-syllabus.json"
)
LOCAL_BOOKS = [
    ROOT
    / "books"
    / "modern india"
    / "MODERN INDIA -- BIPIN CHANDRA -- ENGLISH ##.pdf",
    ROOT
    / "books"
    / "modern india"
    / "INDIA STRUGGLE FOR INDEPENDENCE-- BIPIN C ENG.pdf",
    ROOT
    / "books"
    / "medival_history"
    / "FROM PLASY TO PARTITION -- SEKAR B -- ENGLISH.pdf",
]


def topic_config(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    legacy_main: str | None,
    legacy_workbook: str | None,
    extra: list[Path],
    live_sources: list[str],
    current_note: str,
    session_count: int,
    pyq_note: str,
    generation: int,
) -> dict[str, object]:
    return {
        "key": f"modern-indian-history-{number:02d}",
        "title": title,
        "canonical": KNOWLEDGE / canonical,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "legacy_main": ROOT / "notes" / SUBJECT / legacy_main
        if legacy_main
        else None,
        "legacy_workbook": ROOT / "notes" / SUBJECT / legacy_workbook
        if legacy_workbook
        else None,
        "extra": extra,
        "live_sources": live_sources,
        "current_note": current_note,
        "basic_session_count": session_count,
        "pyq_note": pyq_note,
        "generation": generation,
    }


TOPICS = [
    topic_config(
        7,
        "Economic Impact of British Rule (Drain, Deindustrialisation, Land Revenue, Famines)",
        "07_Economic-Impact-of-British-Rule-Drain-Deindustrialisation-Land-Revenue-Famines_Complete-Topic-Package.md",
        "07_Economic-Impact-of-British-Rule.md",
        "07_Economic-Impact-of-British-Rule.md",
        "07_Economic-Impact-of-British-Rule-Drain-Deindustrialisation-Land-Revenue-Famines_Complete-Learning-Session_2026-08-20.pdf",
        "07_Economic-Impact-of-British-Rule-Drain-Deindustrialisation-Land-Revenue-Famines_Premium-Solved-PYQ-Workbook_2026-08-20.pdf",
        [
            KNOWLEDGE / "basic" / "04_British-Conquest-of-Bengal.md",
            KNOWLEDGE / "basic" / "08_Administrative-Organisation.md",
            KNOWLEDGE / "basic" / "14_Foundation-of-INC-and-Moderate-Phase.md",
            KNOWLEDGE / "basic" / "23_Left-Peasant-Workers-and-States-Peoples-Movements.md",
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "World-History"
            / "advanced"
            / "04_Industrial-Revolution.md",
            ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Economy"
            / "basic"
            / "04_RBI-Monetary-Policy-and-Liquidity-Management.md",
        ],
        [],
        "A live 2025-26 search found no topic-tight official event that improves the "
        "historical explanation without importing disputed figures. The package therefore "
        "keeps reparations, restitution and food-security comparisons as optional bridges "
        "and grounds all colonial claims in repository owners and OCR-searchable books.",
        22,
        "The verified 2022 GS-I famine question and 2024 GS-I handicrafts question are "
        "direct Mains owners. The 2018 indentured-labour question is retained only as a "
        "bounded bridge. The 2024 Prelims land-settlement item was officially dropped, "
        "and the 2026 Hilton-Young key remains provisional.",
        2,
    ),
    topic_config(
        8,
        "Administrative Organisation (Civil Services, Army, Police, Judiciary, Rule of Law)",
        "08_Administrative-Organisation-Civil-Services-Army-Police-Judiciary-Rule-of-Law_Complete-Topic-Package.md",
        "08_Administrative-Organisation.md",
        "08_Administrative-Organisation.md",
        None,
        None,
        [
            KNOWLEDGE / "basic" / "07_Economic-Impact-of-British-Rule.md",
            KNOWLEDGE / "basic" / "09_Social-and-Cultural-Policy-Education-Press.md",
            KNOWLEDGE / "basic" / "11_The-Revolt-of-1857.md",
            KNOWLEDGE / "basic" / "12_Administrative-Changes-After-1858.md",
        ],
        [
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2150998",
            "https://bprd.nic.in/page/new_criminal_laws",
        ],
        "PIB's 31 July 2025 Mission Karmayogi update and BPR&D's new-criminal-laws "
        "hub provide bounded contrasts with colonial recruitment, training, policing and "
        "codification. They are not evidence for nineteenth-century institutional facts.",
        16,
        "The repository's 2018-2026 PYQ integration audits route zero direct questions to "
        "Topic 08. The package therefore uses a transparent zero-PYQ audit and labels any "
        "Topic 05, 06 or 09 question only as an adjacent bridge, never as Topic-08-owned.",
        1,
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-07": [
        (
            "Extraction became structural underdevelopment",
            "causal-ladder",
            """COMPANY PLUNDER -> early direct extraction after conquest and Diwani
SYSTEMIC DRAIN -> home charges, remittances, profits, pensions and imperial costs
STRUCTURAL CHANGE -> revenue pressure, deindustrialisation and dependent trade
OUTCOME -> poverty and modernisation without autonomous development.""",
            [
                "1. Periodisation and the extraction-to-underdevelopment frame",
                "21. Comparative synthesis: extraction, transformation and colonial modernisation",
            ],
        ),
        (
            "Three land-revenue systems compared",
            "comparison",
            """PERMANENT -> zamindari estate | fixed in perpetuity | Bengal-Bihar-Orissa
RYOTWARI -> individual ryot | periodic revision | Madras-Bombay
MAHALWARI -> village or mahal | periodic revision | north-west and Punjab
COMMON CORE -> cash demand and secure colonial revenue, with different risk carriers.""",
            [
                "3. The Permanent Settlement, 1793: Cornwallis, zamindar property and fixed demand",
                "4. The Ryotwari settlement: Read, Munro, and direct settlement with uncertainty",
                "5. The Mahalwari settlement: Holt Mackenzie's framework and Bird's implementation",
                "6. Comparative synthesis of the three land-revenue systems",
            ],
        ),
        (
            "Commercialisation shifted risk downward",
            "causal-chain",
            """EXPORT DEMAND / PLANTER ADVANCE -> cash-crop commitment
REVENUE CALENDAR + CREDIT -> dependence on moneylender or planter
PRICE / HARVEST SHOCK -> cultivator bears the loss while claims remain due
RESULT -> indebtedness, land alienation and differentiated agrarian protest.""",
            [
                "7. Commercialisation: crops, coercion, credit and risk",
                "19. Poverty, demography, indebtedness and ecological/social variation",
            ],
        ),
        (
            "Indigo, Pabna and Deccan were not one movement",
            "comparison",
            """INDIGO 1859-60 -> European planters -> collective refusal to sow
PABNA FROM 1873 -> zamindars -> leagues, rent resistance and litigation
DECCAN 1875 -> moneylenders -> seizure and destruction of debt bonds
EXAM RULE -> match target, grievance and repertoire before comparing outcomes.""",
            [
                "8. Case studies in economic protest: Indigo, Pabna, Deccan",
            ],
        ),
        (
            "Deindustrialisation was a causal web",
            "causal-web",
            """ENGLISH MECHANISATION -> cheaper factory cloth
TARIFF ASYMMETRY -> unequal access to British and Indian markets
COURT DECLINE -> lost elite demand for fine crafts
RAIL PENETRATION -> imports reach interior markets
RESULT -> uneven output and employment decline, not total craft extinction.""",
            [
                "9. The deindustrialisation causal web",
                "11. Artisan displacement, de-urbanisation and the limits of \"deindustrialisation\"",
            ],
        ),
        (
            "The 2024 how-far answer",
            "argument-map",
            """NECESSARY CONDITION -> Industrial Revolution lowered British production costs
TRANSMISSION MECHANISMS -> tariffs, political power, court decline and rail access
VARIATION -> region, craft and timing prevent a total-extinction claim
VERDICT -> substantially responsible, but not sufficient without colonial policy.""",
            [
                "10. The 2024 \"how far\" demand: Industrial Revolution and Indian handicrafts",
            ],
        ),
        (
            "Drain theory names channels, not an invented total",
            "channel-map",
            """INDIAN REVENUE -> home charges and India Office costs
OFFICIAL INCOME -> salaries, pensions and private remittances
BRITISH CAPITAL -> profits, interest and guaranteed returns
IMPERIAL PROCUREMENT / WAR -> stores and external costs charged to India
RULE -> explain mechanism and significance; do not invent a percentage.""",
            [
                "12. Drain theory: plunder, systemic drain and its channels",
                "13. Naoroji, R.C. Dutt and M.G. Ranade: the nationalist economic critique",
            ],
        ),
        (
            "Export surplus could finance transfer",
            "process-map",
            """INDIAN EXPORTS EXCEED VISIBLE IMPORTS -> apparent trade surplus
COUNCIL-BILL MECHANISM -> sterling claims and rupee payments connect the accounts
HOME CHARGES / REMITTANCES -> surplus services external obligations
ANALYTICAL POINT -> a surplus need not mean resources remained available in India.""",
            [
                "14. Export surplus, Council Bills and the colonial fiscal-financial system",
            ],
        ),
        (
            "Infrastructure had a dual effect",
            "dialectic",
            """IMPERIAL DESIGN -> troops, administration, raw-material export and import reach
FINANCING -> private British capital protected through the Guarantee System
UNINTENDED EFFECT -> market integration and later nationalist mobility
SAFE VERDICT -> modern infrastructure without autonomous developmental priority.""",
            [
                "15. Infrastructure: railways, ports, roads, telegraph, canals and forests",
            ],
        ),
        (
            "Colonial industrialisation was real but constrained",
            "balance-map",
            """GROWTH -> plantations, jute, cotton, coal, mines and later steel
OWNERSHIP -> foreign capital remained powerful in key sectors
CONSTRAINTS -> finance, policy bias, technology and narrow domestic demand
VERDICT -> industry developed unevenly; deindustrialisation did not mean zero industry.""",
            [
                "16. Colonial industrialisation: plantations, mines and modern industry",
            ],
        ),
        (
            "Famine was shock plus structural amplification",
            "causal-chain",
            """CLIMATE / HARVEST SHOCK -> immediate scarcity risk
REVENUE RIGIDITY + COMMERCIALISATION -> weak household buffers
PRICE-LED TRANSPORT + LAISSEZ-FAIRE RELIEF -> entitlement failure
ADMINISTRATIVE DELAY -> mortality and distress deepen
RULE -> avoid both climate-only and export-only explanations.""",
            [
                "17. Famine causation: climate shock versus entitlement and governance",
                "18. The famine case sequence and colonial famine policy",
            ],
        ),
        (
            "Historiography and final synthesis",
            "synthesis",
            """NATIONALIST -> drain and deindustrialisation explain poverty
STRUCTURAL -> dependent integration into world capitalism
REVISIONIST -> disputes scale and measurement, not all structural change
REGIONAL -> outcomes varied by place, sector and social group
SYNTHESIS -> extraction and transformation must be assessed together.""",
            [
                "20. Historiography of the colonial economy",
                "21. Comparative synthesis: extraction, transformation and colonial modernisation",
                "22. Topic boundaries and a bounded current link",
            ],
        ),
    ],
    "modern-indian-history-08": [
        (
            "The colonial state's four-pillar machine",
            "institution-map",
            """CIVIL SERVICE -> command, revenue and district administration
ARMY -> conquest, frontier defence and final coercive guarantee
POLICE -> surveillance, collection support and public order
JUDICIARY / CODES -> predictable legality and imperial legitimacy
COMMON PURPOSE -> efficient rule without representative accountability.""",
            [
                "1. What Topic 08 owns: the colonial state's four-pillar machine",
                "2. Why administration mattered: revenue, order, imperial control, not representation",
            ],
        ),
        (
            "Professionalisation and exclusion grew together",
            "dialectic",
            """HIGH SALARIES + RULES -> less private trade and a more disciplined service
COVENANTED POSTS -> superior command reserved mainly for Europeans
DISTRICT AUTHORITY -> collector and magistrate become the local state
VERDICT -> administrative capacity strengthened through racial closure.""",
            [
                "3. Cornwallis and the covenanted service: professionalisation plus exclusion",
            ],
        ),
        (
            "Training to competition did not equal Indianisation",
            "timeline",
            """FORT WILLIAM -> language and administrative training in India
HAILEYBURY -> Company training in Britain before open competition
1853 COMPETITION -> formal merit principle; London access barriers remain
1878-79 STATUTORY SERVICE -> limited nominated route
1886 AITCHISON -> classification and Indianisation remain contested.""",
            [
                "4. Fort William, Haileybury, and the training/exclusion pipeline",
                "5. Charter Act 1853 and the London exam: open competition without Indianisation",
                "6. Statutory Civil Service, Aitchison, and the politics of Indianisation",
            ],
        ),
        (
            "The district state concentrated authority",
            "hierarchy",
            """GOVERNMENT OF INDIA / PROVINCE -> policy and supervision
DISTRICT COLLECTOR-MAGISTRATE -> revenue plus executive-magisterial command
SUPERINTENDENT OF POLICE -> coercive hierarchy under executive influence
THANA / DAROGA -> local surveillance and enforcement
COURTS -> legality around the same district-centred state.""",
            [
                "2. Why administration mattered: revenue, order, imperial control, not representation",
                "13. Collector-magistrate-SP interlock: how revenue, police, and law fused on the ground",
            ],
        ),
        (
            "The army before and after 1857",
            "before-after",
            """BEFORE 1857 -> Indian sepoy mass under European officers enables conquest
1857 LESSON -> common military solidarity is treated as a regime threat
AFTER 1857 -> stronger European command, artillery control and fragmented recruitment
PURPOSE -> preserve fighting capacity while preventing unified political action.""",
            [
                "7. Sepoy army before 1857: conquest and internal control",
                "8. Post-1857 reorganisation: ratio, artillery, command, fragmentation",
            ],
        ),
        (
            "Martial races was a doctrine of rule",
            "ideology-map",
            """COLONIAL CLASSIFICATION -> selected groups labelled naturally martial
RECRUITMENT CONCENTRATION -> Punjab, frontier regions and Nepal gain weight
SEPARATE UNITS + HONOUR CODES -> loyalty engineered through difference
RACIAL CLAIM -> fit to fight but allegedly unfit to command
RULE -> teach the category as ideology, never biological truth.""",
            [
                "9. Martial races as colonial governance theory, not ethnographic truth",
                "10. Army policy to politics: recruitment regions, loyalty engineering, later blowback",
            ],
        ),
        (
            "Police design moved from thana to statute",
            "timeline",
            """CORNWALLIS -> thana and daroga structure under district authority
PRE-1861 PRACTICE -> policing serves order, revenue and local surveillance
POLICE ACT 1861 -> provincial Inspector-General and district Superintendent
LEGACY QUESTION -> executive control versus public accountability.""",
            [
                "11. Thana, daroga, magistrate: Cornwallis's police foundation",
                "12. Police Act 1861 and the district coercive hierarchy",
            ],
        ),
        (
            "Police was designed for order, not citizen service",
            "purpose-map",
            """REVENUE DISPUTE / PROTEST -> district executive identifies a threat
POLICE SURVEILLANCE -> intelligence, arrest and crowd control
MAGISTERIAL POWER -> executive direction gains legal force
ARMY BACKSTOP -> escalated resistance meets military coercion
RESULT -> regime security outranks accountable public service.""",
            [
                "12. Police Act 1861 and the district coercive hierarchy",
                "13. Collector-magistrate-SP interlock: how revenue, police, and law fused on the ground",
            ],
        ),
        (
            "Codification modernised and controlled",
            "dialectic",
            """CORNWALLIS CODE -> institutional ordering and judicial separation in principle
SADAR / DISTRICT COURTS -> graded civil and criminal adjudication
LAW COMMISSION TRADITION -> uniform written codes
IPC 1860 + PROCEDURE -> predictability across a centralised state
LIMIT -> the same legal form could authorise repression.""",
            [
                "14. Cornwallis Code, Sadar courts, and codified legality",
                "15. IPC/procedure codes and rule of law versus racial privilege",
            ],
        ),
        (
            "Rule of law had a racial ceiling",
            "contradiction-map",
            """FORMAL CLAIM -> uniform law, evidence and procedure
PRACTICAL ORDER -> executive dominance and political offences
RACIAL PRIVILEGE -> Europeans resist equal jurisdiction
ILBERT BILL 1883 -> collision makes the hierarchy visible
VERDICT -> legalistic administration was not liberal citizenship.""",
            [
                "15. IPC/procedure codes and rule of law versus racial privilege",
                "16. Ilbert Bill, nationalist critique, colonial legacy, and bounded current bridge",
            ],
        ),
        (
            "Ilbert Bill exposed organised racial privilege",
            "event-map",
            """PROPOSAL -> qualified Indian judges may try European British subjects
EUROPEAN AGITATION -> equality framed as a racial threat
COMPROMISE -> original principle diluted
INDIAN RESPONSE -> humiliation strengthens organised political critique
USE -> decisive evidence that formal legality stopped at racial power.""",
            [
                "16. Ilbert Bill, nationalist critique, colonial legacy, and bounded current bridge",
            ],
        ),
        (
            "Interlock, contradiction and legacy",
            "synthesis",
            """REVENUE -> collector commands the district
ORDER -> police and army secure extraction and political control
LEGALITY -> courts and codes regularise authority
EXCLUSION -> superior command remains racially restricted
LEGACY -> durable institutions require democratic repurposing, not simple celebration.""",
            [
                "13. Collector-magistrate-SP interlock: how revenue, police, and law fused on the ground",
                "16. Ilbert Bill, nationalist critique, colonial legacy, and bounded current bridge",
            ],
        ),
    ],
}

ORIGINAL_NORMALIZE_MCQS = base.normalize_mcqs
TOPIC_07_MCQ_REPLACEMENTS = {
    21: (
        "Which option correctly distinguishes Company plunder, systemic drain and "
        "structural underdevelopment?",
        "Plunder was early direct extraction; drain was continuing institutional "
        "transfer; underdevelopment was the long-run structural outcome.",
        [
            "All three terms describe only the initial seizure of Bengal's treasury.",
            "Drain means domestic taxation, while underdevelopment means a single famine.",
            "Plunder and drain are identical, and neither changed India's economic structure.",
        ],
    ),
}


def split_register(source: str, key: str) -> tuple[str, str]:
    number = key.rsplit("-", 1)[-1]
    markers = (
        f"# FINAL CONSOLIDATED REGISTER NOTES - TOPIC {number}",
        f"# FINAL CONSOLIDATED REGISTER NOTES -- TOPIC {number}",
    )
    marker = next((value for value in markers if value in source), None)
    if marker is None:
        raise ValueError(f"{key}: final register marker missing.")
    main, register = source.split(marker, 1)
    return main.rstrip(), marker + register


def phase_for(key: str, number: int) -> str:
    if key.endswith("-07"):
        if number <= 2:
            return "FOUNDATION"
        if number <= 19:
            return "CORE"
        return "CORE SYNTHESIS"
    if number <= 2:
        return "FOUNDATION"
    if number <= 15:
        return "CORE"
    return "CORE SYNTHESIS"


def source_audit(config_value: dict[str, object]) -> str:
    key = str(config_value["key"])
    if key.endswith("-07"):
        live = (
            "✅ **Live-source result:** a 2025-26 search found no topic-tight official "
            "event whose inclusion would improve the historical explanation without "
            "introducing disputed colonial-loss, mortality or reparations figures.\n\n"
            "⚠️ **Inference boundary:** contemporary reparations, restitution, food-security "
            "or industrial-policy debates may activate this static topic, but they do not "
            "supply evidence for the historical drain, famine or deindustrialisation claims."
        )
    else:
        live = (
            "✅ **Bounded official institutional links:** PIB's 31 July 2025 Mission "
            "Karmayogi update records competency-based civil-service capacity building, "
            "while BPR&D's new-criminal-laws hub documents implementation resources for "
            "BNS, BNSS and BSA.\n\n"
            "⚠️ **Inference boundary:** these sources create a present-day comparison with "
            "colonial recruitment, policing and codification. They do not prove any "
            "nineteenth-century fact or erase current implementation debates."
        )
    return (
        "#### Source audit, progression and syllabus boundary\n\n"
        "- **Foundation:** chronology, institutions, actors and exact terminology.\n"
        "- **Core:** mechanisms, comparisons, causal chains, Indian agency and exam traps.\n"
        "- **Core synthesis:** historiography, answer architecture, boundaries and bridges.\n"
        "- **Optional Advanced:** the separate owner is taught only after Basic practice.\n"
        "- **Static source order:** repository Markdown -> OCR-searchable Bipan Chandra "
        "and Sekhar Bandyopadhyay -> bounded live research; Qdrant not needed.\n"
        f"- **PYQ integrity:** {config_value['pyq_note']}\n\n"
        "#### Live-linkage block\n\n"
        + live
    )


def normalize_mcqs(source: str, key: str) -> str:
    replacements = TOPIC_07_MCQ_REPLACEMENTS if key.endswith("-07") else {}
    previous = base.MCQ_REPLACEMENTS_04
    try:
        base.MCQ_REPLACEMENTS_04 = replacements
        return ORIGINAL_NORMALIZE_MCQS(source, key)
    finally:
        base.MCQ_REPLACEMENTS_04 = previous


def write_ascii_spec() -> None:
    topics: list[dict[str, object]] = []
    for config_value in TOPICS:
        key = str(config_value["key"])
        panels = []
        for title, structural_type, body, references in PANEL_DATA[key]:
            lines = body.splitlines()
            if max(map(len, lines)) > 100:
                raise ValueError(
                    f"{key}: ASCII line exceeds 100 characters in {title!r}."
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
            raise ValueError(f"{key}: expected 12 panels, found {len(panels)}.")
        topics.append(
            {
                "topic_key": key,
                "display_title": config_value["title"],
                "source_markdown": str(
                    Path(config_value["canonical"]).relative_to(ROOT)
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Modern Indian History learner-v2 Topics 07-08",
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "complete_embed_ready_lines": True,
            "tracker_untouched": True,
        },
        "topics": topics,
    }
    ASCII_PATH.parent.mkdir(parents=True, exist_ok=True)
    ASCII_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_generation_spec(
    config_value: dict[str, object],
    source_path: Path,
    workbook_path: Path,
    graphical_path: Path,
) -> Path:
    sources = [
        Path(config_value[name])
        for name in ("basic", "advanced", "canonical")
    ]
    for name in ("legacy_main", "legacy_workbook"):
        value = config_value.get(name)
        if value:
            sources.append(Path(value))
    sources += [Path(path) for path in config_value["extra"]]
    sources += [
        source_path,
        workbook_path,
        SECTION_MANIFEST,
        base.CATALOG,
        ASCII_PATH,
        graphical_path,
        *base.COMMON_CROSS,
        *base.PYQ_INDEXES,
        *base.OFFICIAL_QUESTION_SOURCES,
        *LOCAL_BOOKS,
    ]
    sources = list(dict.fromkeys(sources))
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    key = str(config_value["key"])
    catalog = json.loads(base.CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        topic for topic in catalog["topics"] if topic.get("topic_key") == key
    )
    cross_sources = [
        *base.COMMON_CROSS,
        *[Path(value) for value in config_value["extra"]],
    ]
    payload = {
        "schema_version": 1,
        "topic_key": key,
        "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus",
        "topic_folder": key,
        "title": config_value["title"],
        "variant": "learner-v2",
        "generation": config_value["generation"],
        "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "source_markdown": str(source_path.relative_to(ROOT)),
        "workbook_markdown": str(workbook_path.relative_to(ROOT)),
        "source_basic": str(Path(config_value["basic"]).relative_to(ROOT)),
        "source_canonical": str(Path(config_value["canonical"]).relative_to(ROOT)),
        "source_advanced": str(Path(config_value["advanced"]).relative_to(ROOT)),
        "manifest": str(SECTION_MANIFEST.relative_to(ROOT)),
        "cross_topic_sources": [
            str(path.relative_to(ROOT)) for path in cross_sources
        ],
        "local_ocr_sources": [
            str(path.relative_to(ROOT)) for path in LOCAL_BOOKS
        ],
        "pyq_indexes": [
            str(path.relative_to(ROOT)) for path in base.PYQ_INDEXES
        ],
        "official_question_sources": [
            str(path.relative_to(ROOT)) for path in base.OFFICIAL_QUESTION_SOURCES
        ],
        "live_sources": config_value["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": (
            "80 unique MCQ stems with substantive explanations; strict A-B-C-D repeated "
            "20 times; original 10/15/20-mark Mains practice and verified/inferred PYQ "
            "provenance retained in both session and solved workbook Markdown."
        ),
        "pyq_status_note": config_value["pyq_note"],
        "current_linkage_note": config_value["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle",
        "ascii_panel_count": 12,
        "graphical_stage_count": 13,
        "tracker_untouched": True,
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{key}-new-topic-{DATE}.json"
    output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output


def self_check(
    markdown: str,
    workbook: str,
    key: str,
    session_count: int,
    graphical_path: Path,
) -> None:
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    required = [
        "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION",
        "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
        "CONSOLIDATED REGISTER NOTES",
    ]
    if [item for item in headings if item in required] != required:
        raise ValueError(f"{key}: learner-v2 H2 order is invalid.")
    if headings[-1] != "CONSOLIDATED REGISTER NOTES":
        raise ValueError(f"{key}: consolidated register notes are not the last H2.")
    sessions = re.findall(r"(?m)^### SESSION (\d+) — (.+?) — (.+?)\s*$", markdown)
    if len(sessions) != session_count:
        raise ValueError(f"{key}: explicit session count mismatch.")
    if [int(row[0]) for row in sessions] != list(range(1, session_count + 1)):
        raise ValueError(f"{key}: explicit session numbering is invalid.")
    if not any(row[1] == "FOUNDATION" for row in sessions):
        raise ValueError(f"{key}: Foundation progression is missing.")
    if not any(row[1] == "CORE" for row in sessions):
        raise ValueError(f"{key}: Core progression is missing.")
    base.mcq_audit(markdown, key)
    base.mcq_audit(workbook, key)
    spec = ascii_master.normalize_manual_spec_file(ASCII_PATH)[key]
    if len(spec.panels) != 12 or markdown.count("```ascii-master") != 12:
        raise ValueError(f"{key}: authored ASCII panel count failed.")
    graphical = json.loads(graphical_path.read_text(encoding="utf-8"))
    if len(graphical["stages"]) != 13:
        raise ValueError(f"{key}: graphical stage count failed.")
    required_terms = {
        "modern-indian-history-07": [
            "Permanent Settlement",
            "Ryotwari",
            "Mahalwari",
            "deindustrialisation",
            "drain of wealth",
            "Council Bills",
            "Guarantee System",
            "Strachey Commission",
            "entitlement",
            "Dadabhai Naoroji",
        ],
        "modern-indian-history-08": [
            "Cornwallis Code",
            "covenanted civil service",
            "Haileybury",
            "Charter Act, 1853",
            "Statutory Civil Service",
            "Aitchison Commission",
            "martial races",
            "Police Act, 1861",
            "Indian Penal Code",
            "Ilbert Bill",
            "rule of law",
        ],
    }[key]
    missing = [
        term for term in required_terms if term.casefold() not in markdown.casefold()
    ]
    if missing:
        raise ValueError(f"{key}: missing required concepts: {missing}.")


def configure_base() -> None:
    base.DATE = DATE
    base.SUBJECT = SUBJECT
    base.TOPICS = TOPICS
    base.PANEL_DATA = PANEL_DATA
    base.ASCII_PATH = ASCII_PATH
    base.SESSION_DIR = SESSION_DIR
    base.GRAPHICAL_DIR = GRAPHICAL_DIR
    base.EXPORT_DIR = EXPORT_DIR
    base.SECTION_MANIFEST = SECTION_MANIFEST
    base.LOCAL_BOOKS = LOCAL_BOOKS
    base.MCQ_REPLACEMENTS_04 = {}
    base.split_register = split_register
    base.phase_for = phase_for
    base.source_audit = source_audit
    base.normalize_mcqs = normalize_mcqs
    base.write_generation_spec = write_generation_spec


def main() -> int:
    configure_base()
    write_ascii_spec()
    base.write_section_manifest()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH, SECTION_MANIFEST]
    for config_value in TOPICS:
        markdown, workbook, session_count = base.assemble(config_value)
        key = str(config_value["key"])
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        workbook_path = SESSION_DIR / f"{key}_Solved-Workbook.md"
        source_path.write_text(markdown, encoding="utf-8")
        workbook_path.write_text(workbook, encoding="utf-8")
        graphical_path = base.write_graphical_spec(config_value, markdown)
        manifest = write_generation_spec(
            config_value,
            source_path,
            workbook_path,
            graphical_path,
        )
        self_check(markdown, workbook, key, session_count, graphical_path)
        written.extend([source_path, workbook_path, graphical_path, manifest])
        print(
            f"{key}: sessions={session_count}; mcqs=80 (A20/B20/C20/D20); "
            "ascii=12; graphical=13"
        )
    for path in written:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
