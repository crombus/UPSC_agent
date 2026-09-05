"""Assemble Medieval History learner-v2 Topics 07-08 and visual specs."""

from __future__ import annotations

import json
import re
from pathlib import Path

import generate_medieval_history_01_02_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-07-08-2026-08-30-sequential.json"
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
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


def topic_config(
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
    cover_alt: str,
    cover_path: str,
    extra_markdown: list[str],
) -> dict[str, object]:
    value = previous.config(
        number,
        title,
        canonical,
        basic,
        advanced,
        legacy_main,
        legacy_workbook,
        practice_profile,
        live_sources,
        current_note,
        extra_markdown,
    )
    value["cover_alt"] = cover_alt
    value["cover_path"] = cover_path
    value["local_books"] = [SATISH_HISTORY, SATISH_SULTANAT]
    return value


TOPICS = [
    topic_config(
        7,
        "Administration, Economy & Society under the Sultanate",
        "07_Administration-Economy-Society-under-the-Sultanate_Complete-Topic-Package.md",
        "07_Sultanate-Administration-Economy-Society.md",
        "07_Sultanate-Administration-Economy-Society.md",
        "07_Administration-Economy-Society-under-the-Sultanate_Complete-Learning-Session_2026-08-16.pdf",
        "07_Administration-Economy-Society-under-the-Sultanate_Premium-Solved-PYQ-Workbook_2026-08-16.pdf",
        "4 verified or honestly adjacent PYQs; 18 learning, 32 broad and "
        "12 remedial MCQs; 6 original solved Mains questions.",
        ["https://www.rbi.org.in/commonman/English/Currency/Scripts/Medieval.aspx"],
        "The Reserve Bank of India's Medieval India coinage page was rechecked "
        "on 30 August 2026. It describes the consolidation of the tanka and "
        "jittal, an attempted standardisation under the Delhi Sultanate, "
        "expansion of the money economy and gold, silver and copper issues. "
        "This official numismatic bridge supports the package's coinage and "
        "monetisation section; its estimates and evaluative language are "
        "identified as RBI museum-page claims rather than universal measures "
        "of social welfare or uniform market penetration.",
        "Sultanate administration economy and society cover",
        "notes/Medieval-Indian-History/assets/"
        "07_Administration-Economy-Society-under-the-Sultanate/"
        "00_sultanate_admin_economy_society_cover.png",
        [
            "learning-sessions\\07_Administration-Economy-Society-under-the-Sultanate_Complete-Learning-Session_2026-08-16.md",
            "learning-sessions\\07_Administration-Economy-Society-under-the-Sultanate_Premium-Solved-PYQ-Workbook_2026-08-16.md",
        ],
    ),
    topic_config(
        8,
        "Provincial & Regional Kingdoms (Bengal, Gujarat, Malwa, Jaunpur, "
        "Kashmir) + bounded Ahom/Assam Prelims extension",
        "08_Provincial-Regional-Kingdoms_Complete-Topic-Package.md",
        "08_Provincial-Regional-Kingdoms.md",
        "08_Provincial-Regional-Kingdoms.md",
        "08_Provincial-Regional-Kingdoms_Complete-Learning-Session_2026-08-16.pdf",
        "08_Provincial-Regional-Kingdoms_Premium-Solved-PYQ-Workbook_2026-08-16.pdf",
        "3 honestly routed PYQ demands; 12 learning, 32 broad and 12 remedial "
        "MCQs; 6 original solved Mains questions.",
        ["https://whc.unesco.org/en/list/1711/"],
        "UNESCO's Moidams - the Mound-Burial System of the Ahom Dynasty page "
        "was rechecked on 30 August 2026. It identifies Charaideo as a "
        "Tai-Ahom royal necropolis, records 90 moidams, and dates the funerary "
        "tradition from the thirteenth to the nineteenth centuries. The live "
        "link remains bounded: political ecology, Paik mobilisation, Buranji "
        "source criticism and royal memory belong here, while detailed "
        "funerary form, cosmology and conservation remain with Art & Culture.",
        "Regional kingdoms and bounded Ahom extension cover",
        "notes/Medieval-Indian-History/assets/"
        "08_Provincial-Regional-Kingdoms/00_cover.png",
        [
            "learning-sessions\\08_Provincial-Regional-Kingdoms_Complete-Learning-Session_2026-08-16.md",
            "learning-sessions\\08_Provincial-Regional-Kingdoms_Premium-Solved-PYQ-Workbook_2026-08-16.md",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-07": [
        (
            "Sultanate thematic chronology",
            "timeline",
            """13th c. -> consolidation through court, iqta and inherited local structures
1296-1316 -> Alauddin tightens revenue, cavalry and market supervision
1320s-1351 -> sharing, assessment, cash demands and high-risk experiments
1351-1388 -> canals, karkhanas, elite conciliation and hereditary drift
15th c. -> weaker Delhi control and stronger regional landed interests
RULE: institutions changed by reign, region, distance and enforcement capacity.""",
            ["Chronology", "Institutional change"],
        ),
        (
            "State formation as a layered network",
            "layered-governance",
            """SULTAN / COURT -> sovereignty, appointments, campaign direction
CENTRAL DEPARTMENTS -> finance, army, correspondence and intelligence
IQTADARS / GOVERNORS -> troops, collection and provincial bargaining
KHUTS / MUQADDAMS / CHIEFS -> village access, information and mediation
CULTIVATORS / ARTISANS -> production, labour and taxable surplus
VERDICT: coercive at nodes, negotiated across the countryside.""",
            ["State formation", "Local intermediaries"],
        ),
        (
            "Central departments with chronology caution",
            "institution-map",
            """DIWAN-I-WIZARAT -> finance, accounts and revenue supervision
DIWAN-I-ARZ -> army review, horses, equipment and recruitment
DIWAN-I-INSHA -> royal correspondence and chancery practice
BARID NETWORK -> intelligence, reports and communication
SADR / QAZI FUNCTIONS -> grants, law and religious authority
CAUTION: portfolios and practical power were not identical in every reign.""",
            ["Central departments", "Administrative caution"],
        ),
        (
            "Iqta fiscal-military flow",
            "process",
            """CROWN ASSIGNS REVENUE CLAIM -> MUQTI / IQTADAR COLLECTS
                    |
authorised salary + troops + local administration
                    |
accounts and audit -> surplus expected for the centre
                    |
transfer restrains local roots; weak control encourages heredity
RULE: assignment of revenue was not unrestricted ownership of land.""",
            ["Iqta", "Muqti", "Audit"],
        ),
        (
            "Revenue and local hierarchy",
            "cause-mechanism-effect",
            """AGRARIAN OUTPUT -> assessment through law, custom and state demand
LOCAL ELITES -> khuts, muqaddams, chaudhris, chiefs and accountants
ALAUDDIN -> measurement, khalisa expansion and pressure on privileges
TUGHLAQ VARIANTS -> sharing, standard yields, canals and changing incidence
OUTCOME -> stronger surplus claims but uneven burden, flight and resistance
METHOD: separate nominal rate, collection practice and cultivator experience.""",
            ["Revenue", "Khalisa", "Rural elites"],
        ),
        (
            "Army, logistics and urban regulation",
            "network-map",
            """HORSES / REMOUNTS -> import routes, branding, inspection and fodder
CASH SALARIES -> coin supply, price conditions and treasury capacity
FORTS / ROADS -> frontier defence, messengers and grain movement
MARKET OVERSIGHT -> weights, supplies, intelligence and punishment
KOTWAL / QAZI -> policing and judicial plurality in towns
LESSON: military power rested on fiscal, commercial and informational systems.""",
            ["Army", "Markets", "Urban administration"],
        ),
        (
            "Agrarian surplus and irrigation",
            "cause-mechanism-effect",
            """RAIN + WELLS + LIFTS + CANALS -> variable cultivation capacity
                    |
grain and cash crops -> village consumption + dues + marketable surplus
                    |
state, iqta holder and intermediaries compete over extraction
                    |
town demand and armies grow, while famine and harsh collection expose risk
CAUTION: public works did not distribute gains equally.""",
            ["Agriculture", "Irrigation", "Surplus transfer"],
        ),
        (
            "Coinage and monetisation evidence",
            "evidence-matrix",
            """TANKA / JITTAL -> units and denominations in an expanding money economy
GOLD / SILVER / COPPER -> metal range, scarcity and regional variation
MINTS / LEGENDS -> authority, titles and public monetary claims
CASH REVENUE / SALARY -> links countryside, treasury, army and merchants
RBI PAGE -> official museum synthesis, not a complete price or welfare series
VERDICT: monetisation expanded unevenly; barter and payment in kind persisted.""",
            ["RBI coinage page", "Tanka", "Jittal", "Monetisation"],
        ),
        (
            "Urban craft and technology circuit",
            "process",
            """COURT + ARMY + MERCHANT DEMAND
            |
DELHI / DAULATABAD / MULTAN / CAMBAY and smaller qasbas
            |
textiles + paper + metal + leather + building crafts + royal karkhanas
            |
spinning wheel, carder's bow, improved looms, mortar and water lifting
RESULT: greater output and specialisation without equal gains for labour.""",
            ["Urbanisation", "Crafts", "Technology"],
        ),
        (
            "Trade, transport and credit",
            "network-map",
            """VILLAGE PRODUCERS -> banjaras and local markets -> inland towns
MULTANIS / SAHS / BROKERS -> advances, exchange and merchant finance
HUNDIS -> transfer and credit across distance
CAMBAY / BENGAL PORTS -> Indian Ocean exchange and textile exports
HORSE IMPORTS -> military demand links coast, merchants and court
LIMIT: route activity does not prove uniform prosperity or state control.""",
            ["Trade", "Hundis", "Merchants", "Transport"],
        ),
        (
            "Social differentiation without static blocs",
            "comparison-matrix",
            """NOBLES / ULEMA -> status, office, grants and internal hierarchy
MERCHANTS / ARTISANS -> wealth at the top, insecurity lower down
RURAL GROUPS -> chiefs, privileged intermediaries, peasants and labourers
HINDU / MUSLIM COMMUNITIES -> conflict, interaction and differentiated mobility
SLAVERY / GENDER -> household, military and productive roles under coercion
RULE: avoid timeless census boxes and single-cause conversion claims.""",
            ["Social groups", "Conversion", "Slavery", "Gender"],
        ),
        (
            "Topic 07 evidence and answer spine",
            "answer-synthesis",
            """OPEN -> changing military-fiscal state, centralising in aspiration
ADMIN -> court + departments + iqta + local intermediaries
ECONOMY -> agrarian surplus + money + towns + crafts + trade
SOCIETY -> layered elites, labour, caste, community, slavery and gender
METHOD -> chroniclers + travellers + coins + inscriptions + monuments
CLOSE -> negotiated in practice, regionally uneven and socially unequal.""",
            ["Historiography", "Sources", "Answer architecture"],
        ),
    ],
    "medieval-indian-history-08": [
        (
            "Regionalisation chronology and map",
            "timeline",
            """1338-42 Bengal break and Ilyas Shahi consolidation
1398 Timur shock -> Delhi contraction accelerates
1407 Gujarat formal independence -> 1411-42 Ahmad Shah consolidation
15th c. Malwa, Jaunpur, Kashmir and western-eastern balances
1459-1511 Mahmud Begarha -> 1484 Bahlul annexes Jaunpur
RULE: regional states were active systems, not debris between empires.""",
            ["Regionalisation", "Chronology"],
        ),
        (
            "Bengal delta autonomy circuit",
            "cause-mechanism-effect",
            """DISTANCE + RIVERS + HUMID CLIMATE -> costly external projection
INTERNAL WATERWAYS -> movement of grain, people and craft goods
ILYAS SHAHI ORGANISATION + EKDALA -> defensive and dynastic capacity
CHITTAGONG + TEXTILES + CHINA CONTACT -> wider commercial connection
GAUR / PANDUA + BENGALI PATRONAGE -> locally intelligible legitimacy
VERDICT: ecology created possibilities; institutions converted them into autonomy.""",
            ["Bengal", "Delta ecology", "Ilyas Shah"],
        ),
        (
            "Gujarat port-hinterland state",
            "process",
            """FERTILE INTERIOR + HANDICRAFT PRODUCTION
                |
AHMEDABAD markets, administration and building patronage
                |
ROADS / CARAVANS / CAMBAY and west-coast ports
                |
REVENUE + MERCHANT NETWORKS + MILITARY RESOURCES
CAUTION: ports were nodes in a territorial system, not automatic wealth machines.""",
            ["Gujarat", "Ahmedabad", "Ports", "Mahmud Begarha"],
        ),
        (
            "Malwa strategic plateau",
            "network-map",
            """                 MEWAR
                   / forts and corridors
GUJARAT <---- MALWA / MANDU ----> GANGA ROUTES
                   \ Deccan links
MANDU -> defensible plateau capital, court and monumental patronage
POLITICS -> rivalry, alliances and border-state intervention
RULE: explain strategic geography without reducing events to religion alone.""",
            ["Malwa", "Mandu", "Mewar", "Gujarat"],
        ),
        (
            "Jaunpur power and cultural capital",
            "layered-governance",
            """GANGA-VALLEY LOCATION
        |
SHARQI COURT + revenue territory + military competition with Delhi
        |
learning, Persian culture and 'Shiraz of the East' reputation
        |
lofty gates, arches and an identifiable architectural idiom
1484 -> Bahlul Lodi annexes Jaunpur, but regional memory survives.""",
            ["Jaunpur", "Sharqis", "Cultural legitimacy"],
        ),
        (
            "Kashmir reign contrast",
            "comparison",
            """SIKANDAR SHAH                 ZAINUL ABIDIN / BUD SHAH
coercive religious measures       reversal and reconciliation
temple and grant disruption       restorations and return of groups
sharper exclusion                 Hindu officers and translation patronage
                                  crafts, agriculture and learning
RULE: do not project either reign across all Kashmir or all medieval India.""",
            ["Kashmir", "Sikandar Shah", "Zainul Abidin"],
        ),
        (
            "Five regional capacity models",
            "comparison-matrix",
            """BENGAL -> delta mobility, agrarian base, ports and language
GUJARAT -> port-hinterland trade, crafts, routes and urban capital
MALWA -> plateau position, Mandu and western-Deccan corridors
JAUNPUR -> Ganga-valley territory, learned court and Lodi rivalry
KASHMIR -> valley ecology, reconciliation and craft-cultural reconstruction
COMMON TEST: resources + coalition + institutions + legitimacy + limits.""",
            ["Comparative political economy", "State capacity"],
        ),
        (
            "Fifteenth-century balance of power",
            "network-map",
            """WEST: GUJARAT <-> MALWA <-> MEWAR
EAST: BENGAL <-> ORISSA / JAUNPUR
UPPER GANGA: JAUNPUR <-> LODI DELHI
NORTH-WEST: KASHMIR follows a distinct valley trajectory
LINKS: wars + exiles + marriages + corridors + commercial competition
CAUTION: balance describes recurring checks, not fixed modern borders or a treaty.""",
            ["Balance of power", "Inter-state relations"],
        ),
        (
            "Architecture and language as evidence",
            "evidence-matrix",
            """BENGAL -> brick, curved roofs, Gaur-Pandua and Bengali patronage
GUJARAT -> fine stone, brackets, turrets, Ahmedabad and Champaner
MALWA -> Mandu scale, high plinths, palaces and glazed decoration
JAUNPUR -> monumental gateways, arches and learned prestige
KASHMIR -> translation, crafts and courtly reconciliation
RULE: material patronage shows claims and labour, not equality for every subject.""",
            ["Regional culture", "Architecture", "Language"],
        ),
        (
            "Bounded Ahom political extension",
            "process",
            """13th c. Tai-Ahom migration -> Charaideo first capital and royal memory
BRAHMAPUTRA ECOLOGY -> wet-rice expansion, mobility and frontier adaptation
PAIK ROTATION -> household-linked labour and military mobilisation
OFFICIALS / KHELS -> organise service and productive capacity over time
BOUNDARY -> comparison beyond Delhi, not a substitute for the five core kingdoms
CAUTION: avoid equating rotational obligation with one timeless labour category.""",
            ["Ahom", "Paik", "Political ecology"],
        ),
        (
            "Buranji and Moidam evidence ladder",
            "evidence-matrix",
            """BURANJIS -> chronology and institutions | royal viewpoint and silences
MOIDAMS -> royal memory and labour | funerary evidence, not a fiscal ledger
UNESCO -> 90 moidams and 13th-19th c. tradition | heritage synthesis
LANDSCAPE -> hills, water and sacred setting | needs archaeological context
BEST USE -> triangulate chronicle, material site and institutional comparison
ROUTE OUT -> detailed cosmology, form and conservation to Art & Culture.""",
            ["Buranjis", "Moidams", "UNESCO", "Source criticism"],
        ),
        (
            "Topic 08 answer spine",
            "answer-synthesis",
            """OPEN -> Delhi contraction redistributed sovereignty; it did not erase states
MAP -> delta, coast, plateau, Ganga plain, valley and Brahmaputra
MECHANISM -> resources + routes + elites + revenue + court legitimacy
COMPARE -> Bengal, Gujarat, Malwa, Jaunpur and Kashmir without flattening
EXTEND -> Paik, Buranjis and Charaideo within a strict Ahom boundary
CLOSE -> plural regional capacity shaped the setting inherited by later empires.""",
            ["Answer architecture", "Regional state system", "Ahom boundary"],
        ),
    ],
}


def normalize_mcq_fragment(fragment: str) -> str:
    text = previous.normalize_objective_syntax(fragment)
    text = re.sub(r"[ \t]*\\n(?=[A-D]\.[ \t])", "\n", text)
    text = re.sub(
        r"(?m)^([A-D])\.[ \t]+",
        lambda match: f"- {match.group(1)}. ",
        text,
    )
    text = re.sub(
        r"(?mi)^\*\*Correct answer:\*\*[ \t]*\*\*([A-D])\*\*[ \t]*$",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        text,
    )
    text = re.sub(
        r"(?mi)^\*\*Correct answer:\*\*[ \t]*([A-D])[ \t]*$",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        text,
    )
    text = re.sub(
        r"(?mi)^\*\*Answer:\*\*[ \t]*\*\*([A-D])\*\*[ \t]*$",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        text,
    )
    return text


def normalized_fragment(fragment: str, metadata: bool = False) -> str:
    value = previous.base.normalize_fragment(fragment)
    if metadata:
        value = re.sub(r"^### ", "#### ", value, count=1)
    return value


def compose(
    config_value: dict[str, object],
    preamble: str,
    grouped: dict[str, list[str]],
) -> str:
    advanced = normalized_fragment(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "The live page is a teaching bridge only. Historical chronology, "
        "causation and institutional claims remain controlled by repository "
        "Markdown, OCR-searchable books and source criticism."
    )
    return (
        f"# {config_value['title']} - Complete Topic Package\n\n"
        f"{preamble}\n\n"
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


def assemble_topic_07(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    source = source.replace(
        "Therefore technology and trade expanded capability, but they did not "
        "democratise society. They enlarged state power, urban consumption and "
        "commercial reach within a deeply stratified order.  \n\n"
        "**Why this earns marks:** It ties technique to trade, then to class "
        "outcome, and refuses to confuse growth with equality.",
        "Therefore technology and trade expanded capability, but they did not "
        "democratise society. They enlarged state power, urban consumption and "
        "commercial reach within a deeply stratified order.",
    )
    source = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)
    preamble, sections = previous.base.split_h2(source)
    preamble = previous.base.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        metadata = title.startswith(
            ("Package counts", "Sources actually", "Original visual asset")
        )
        if metadata or re.match(r"^\d{2}\.", title):
            bucket = "basic"
        elif title.startswith(
            ("Learning MCQ", "Original broad-coverage MCQs", "Remedial trap MCQs")
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title == "Solved topic-specific MCQs":
            continue
        elif title.startswith(
            (
                "Verified and honestly-adjacent PYQs",
                "PYQ verification",
                "Original solved Mains",
            )
        ):
            bucket = "practice"
        elif title == "Final consolidated register notes":
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 07 section: {title}")
        grouped[bucket].append(normalized_fragment(fragment, metadata=metadata))
    return compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble_topic_08(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    source = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)
    preamble, sections = previous.base.split_h2(source)
    preamble = previous.base.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        metadata = title.startswith(
            ("Package scope", "Roadmap and retrieval")
        )
        numbered_session = bool(re.match(r"^\d{2}\.", title))
        if numbered_session:
            mcq_match = re.search(r"(?ms)^### Learning MCQ.*\Z", fragment)
            if mcq_match:
                grouped["mcq"].append(
                    normalized_fragment(
                        normalize_mcq_fragment(mcq_match.group(0))
                    )
                )
                fragment = fragment[: mcq_match.start()].rstrip() + "\n"
        if metadata or numbered_session:
            bucket = "basic"
        elif title.startswith(
            (
                "PART II",
                "Original broad-coverage MCQs",
                "Remedial trap MCQs",
            )
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Original solved Mains"):
            bucket = "practice"
        elif title.startswith("Final consolidated register notes"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 08 section: {title}")
        grouped[bucket].append(normalized_fragment(fragment, metadata=metadata))
    return compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-07":
        return assemble_topic_07(config_value)
    return assemble_topic_08(config_value)


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
                "source_markdown": previous.base.relative(
                    Path(config_value["canonical"])
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Medieval Indian History learner-v2 Topics 07-08",
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


def write_generation_spec(
    config_value: dict[str, object],
    source_path: Path,
    graphical_path: Path,
) -> Path:
    key = str(config_value["key"])
    local_books = [Path(path) for path in config_value["local_books"]]
    source_files = [
        Path(config_value["basic"]),
        Path(config_value["advanced"]),
        Path(config_value["canonical"]),
        *[Path(path) for path in config_value["extra_markdown"]],
        source_path,
        *[ROOT / item for item in previous.COMMON_CROSS],
        *[ROOT / item for item in previous.PYQ_INDEXES],
        *local_books,
        Path(config_value["legacy_main"]),
        Path(config_value["legacy_workbook"]),
        ROOT / str(config_value["cover_path"]).replace("/", "\\"),
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *previous.base.image_sources(Path(config_value["canonical"])),
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
            "Generate learner-v2 topic: Medieval History "
            "— Subject-wide Syllabus — "
            + str(config_value["title"])
        ),
        "source_markdown": previous.base.relative(source_path),
        "source_basic": previous.base.relative(Path(config_value["basic"])),
        "source_canonical": previous.base.relative(Path(config_value["canonical"])),
        "source_advanced": previous.base.relative(Path(config_value["advanced"])),
        "manifest": previous.base.relative(SECTION_MANIFEST),
        "cross_topic_sources": previous.COMMON_CROSS,
        "pyq_indexes": previous.PYQ_INDEXES,
        "official_question_sources": [],
        "local_ocr_sources": [
            previous.base.relative(path) for path in local_books
        ],
        "live_sources": config_value["live_sources"],
        "source_files": [
            previous.base.relative(path) for path in deduplicated
        ],
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
    previous.DATE = DATE
    previous.TOPICS = TOPICS
    previous.PANEL_DATA = PANEL_DATA
    previous.ASCII_PATH = ASCII_PATH
    write_ascii_spec()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH]
    for config_value in TOPICS:
        key = str(config_value["key"])
        markdown = assemble(config_value)
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        source_path.write_text(markdown, encoding="utf-8")
        graphical_path = previous.write_graphical_spec(config_value, markdown)
        generation_spec = write_generation_spec(
            config_value,
            source_path,
            graphical_path,
        )
        written.extend([source_path, graphical_path, generation_spec])
    for path in written:
        print(previous.base.relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
