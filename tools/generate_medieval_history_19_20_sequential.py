"""Assemble Medieval History learner-v2 Topics 19-20 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_17_18_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-19-20-2026-08-30-sequential.json"
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
    / "medieval-indian-history--subject-wide-syllabus.json"
)
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SATISH_HISTORY = (
    ROOT / "books" / "medival_history" / "Satish Chandra History of Medieval India.pdf"
)
SATISH_MUGHALS = (
    ROOT
    / "books"
    / "medival_history"
    / "Medieval-History-Satish-Chandra-1526-1748-Part-2.pdf"
)
GS1_2025 = ROOT / "knowledge-export" / "Mains PYQ" / "UPSC Mains 2025 GS Paper 1.md"
BASE_GENERATOR = previous.BASE_GENERATOR
BASE = previous.BASE
HELPERS = previous.HELPERS


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
    official_question_sources: list[Path],
) -> dict[str, object]:
    value = previous.topic_config(
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
        cover_alt,
        cover_path,
        extra_markdown,
        official_question_sources,
    )
    return value


TOPICS = [
    topic_config(
        19,
        "Foreign Policy of the Mughals",
        "19_Foreign-Policy-of-the-Mughals_Complete-Topic-Package.md",
        "19_Mughal-Foreign-Policy.md",
        "19_Mughal-Foreign-Policy.md",
        "19_Foreign-Policy-of-the-Mughals_Complete-Learning-Session_2026-08-18.pdf",
        "19_Foreign-Policy-of-the-Mughals_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 remedial "
        "MCQs; 10 original solved Mains answers with source criticism.",
        [
            "https://www.pmindia.gov.in/en/news_updates/"
            "pm-speaks-with-the-president-of-iran-4/"
        ],
        "PMIndia's 30 June 2026 release was rechecked through live search on "
        "30 August 2026. It records a conversation between the Prime Minister "
        "of India and Iran's President Masoud Pezeshkian on regional "
        "developments, lasting peace and stability, and safeguarding freedom "
        "of navigation and commerce. It is used only as a bounded modern "
        "comparison for access, security and connectivity. Modern sovereign "
        "borders, international law, Chabahar and INSTC are not continuations "
        "of Mughal Qandahar routes; historical claims remain controlled by "
        "repository Markdown, OCR books and source criticism.",
        "Mughal foreign policy Qandahar Balkh and diplomatic balance cover",
        "notes/Medieval-Indian-History/assets/"
        "19_Foreign-Policy-of-the-Mughals/00_cover.png",
        [
            "learning-sessions\\19_Foreign-Policy-of-the-Mughals_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\19_Foreign-Policy-of-the-Mughals_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [],
    ),
    topic_config(
        20,
        "Jahangir & the Early Seventeenth Century (Nur Jahan)",
        "20_Jahangir-Early-Seventeenth-Century-Nur-Jahan_Complete-Topic-Package.md",
        "20_Jahangir-and-Early-17th-Century.md",
        "20_Jahangir-and-Early-17th-Century.md",
        "20_Jahangir-Early-Seventeenth-Century-Nur-Jahan_Complete-Learning-Session_2026-08-18.pdf",
        "20_Jahangir-Early-Seventeenth-Century-Nur-Jahan_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 remedial "
        "MCQs; 10 original solved Mains answers with an evidence-led gender lens.",
        [
            "https://agra.nic.in/tourist-place/"
            "tomb-of-itimad-ud-daulah-baby-taj/",
            "https://whc.unesco.org/en/list/251/",
        ],
        "The District Agra government and UNESCO Agra Fort pages were "
        "rechecked on 30 August 2026. The first identifies the ASI-protected "
        "Itimad-ud-Daulah tomb as built in 1622-28 by Nur Jahan for her father "
        "Mirza Ghiyas Beg, using white marble and extensive pietra dura. The "
        "second supports the material setting of the Mughal imperial city and "
        "its Jahangir Palace. These official heritage pages support bounded "
        "claims about patronage, architecture and court setting; they do not "
        "prove a fixed Nur Jahan junta, sole sovereignty, political motives or "
        "the reach of imperial orders. No material recent topic-specific "
        "official current-affairs announcement was found.",
        "Jahangir Nur Jahan authority succession and source criticism cover",
        "notes/Medieval-Indian-History/assets/"
        "20_Jahangir-Early-Seventeenth-Century-Nur-Jahan/00_00_cover.png",
        [
            "learning-sessions\\20_Jahangir-Early-Seventeenth-Century-Nur-Jahan_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\20_Jahangir-Early-Seventeenth-Century-Nur-Jahan_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-19": [
        (
            "A qualified foreign-policy framework",
            "argument-tree",
            """MODERN LABEL -> useful for diplomacy, frontiers, trade and warfare
ANACHRONISM RISK -> no nation-state ministry or fixed sovereign border
COURT ACTORS -> emperor, princes, nobles, governors, envoys and merchants
CORE AIMS -> security, commerce, honour and dynastic influence
VERDICT -> use the label analytically, then state its limits.""",
            ["Foreign policy", "Court politics", "Anachronism", "State interest"],
        ),
        (
            "Northwest strategic geography",
            "spatial-map",
            """INDIAN CORE -> Delhi / Lahore / Multan supply and revenue base
KABUL - GHAZNI - QANDAHAR -> defensible but porous outer line
QANDAHAR -> junction toward Herat-Iran and the Indus-sea network
BALKH / BADAKHSHAN -> buffer field beyond the Hindukush
SAMARQAND / OXUS -> Timurid memory and contested movement zone
RULE -> schematic routes are not modern international boundaries.""",
            ["Kabul", "Qandahar", "Herat", "Balkh", "Hindukush"],
        ),
        (
            "Four-court balance, not a sectarian bloc",
            "systems-map",
            """MUGHALS -> protect the Indian core and northwest routes
UZBEKS -> pressure Balkh-Badakhshan and can threaten Kabul
SAFAVIDS -> rival over Qandahar but useful counterweight to Uzbeks
OTTOMANS -> prestige, Safavid rivalry and distant maritime context
CALCULATION -> a weaker Iran could strengthen the Uzbek danger
VERDICT -> interest and status qualify Sunni-Shia rhetoric.""",
            ["Mughals", "Uzbeks", "Safavids", "Ottomans", "Balance"],
        ),
        (
            "Diplomacy as message, intelligence and theatre",
            "process",
            """MISSION -> elchi or safir carries letters, gifts and oral claims
JOURNEY -> routes, escorts and delays filter information
AUDIENCE -> robes, seating, titles and precedence stage status
OBSERVATION -> envoy reports roads, officials, armies and court mood
RETURN -> gifts and replies preserve ambiguity as well as goodwill
TRAP -> cordial ritual does not settle a territorial claim.""",
            ["Elchi", "Safir", "Embassy", "Gifts", "Intelligence"],
        ),
        (
            "Akbar and the Uzbek balance",
            "timeline",
            """1572-73 -> Abdullah Khan takes Balkh; Shahrukh later recovers it
1577 -> anti-Safavid partition proposal; Akbar avoids entanglement
1583 -> Abdullah retakes Balkh | 1585 -> Badakhshan and Kabul change the field
PRACTICAL UNDERSTANDING -> Hindukush restraint, not a fixed treaty border
1595 -> Qandahar passes to Akbar through surrender / defection context
RESULT -> a stronger outer line without Central Asian reconquest.""",
            ["Abdullah Khan Uzbek", "Balkh", "Kabul", "Qandahar", "Akbar"],
        ),
        (
            "Why Qandahar mattered",
            "triangle",
            """SECURITY -> fort and water base shielding approaches to Kabul
COMMERCE -> caravan junction toward Iran, Central Asia, Multan and the sea
PRESTIGE -> Timurid-imperial honour and a visible frontier claim
ASYMMETRY -> Mughal outer bastion; Iranian outpost linked to Herat
LIMIT -> no single motive or route monopoly explains every crisis
VERDICT -> strategic value changed with power, supply and alternatives.""",
            ["Qandahar", "Security", "Commerce", "Prestige"],
        ),
        (
            "Jahangir and the loss of 1622",
            "cause-mechanism-effect",
            """CORDIAL EMBASSIES -> Jahangir underestimates a persistent Safavid claim
SAFAVID INITIATIVE -> Shah Abbas chooses the opportunity to recover Qandahar
FORT CONDITION -> limited readiness and delayed relief weaken defence
COURT POLITICS -> Khurram's response is tied to succession and resource fears
EFFECT -> claim and friendship fail without operational preparation
TRAP -> do not blame Nur Jahan alone or erase Safavid agency.""",
            ["Jahangir", "Shah Abbas I", "Qandahar 1622", "Prince Khurram"],
        ),
        (
            "Shah Jahan recovers Qandahar in 1638",
            "process",
            """ALI MARDAN KHAN -> Safavid governor faces court and frontier pressure
TRANSFER -> Qandahar passes to Mughal control through defection
MUGHAL RESPONSE -> honour, office and resources consolidate the gain
STRATEGIC RESULT -> outer defence and prestige improve temporarily
LIMIT -> diplomatic tension survives and durable possession is not guaranteed.""",
            ["Shah Jahan", "Ali Mardan Khan", "Qandahar 1638"],
        ),
        (
            "Balkh 1646-47: forward defence meets limits",
            "balance-sheet",
            """AIM -> influence through a friendly client and pressure beyond Kabul
CAPABILITY -> Mughal armies take Balkh and fight effectively in the field
FRICTION -> winter, distance, supply and noble reluctance raise the cost
POLITICAL LIMIT -> no durable local settlement or compliant client emerges
WITHDRAWAL -> tactical success cannot sustain the occupation
VERDICT -> costly forward defence, not simple cowardice or total collapse.""",
            ["Balkh campaign", "1646-47", "Forward defence", "Logistics"],
        ),
        (
            "Why Qandahar resisted recovery, 1649-53",
            "systems-map",
            """FORTIFICATION -> Safavid defence and terrain favour the holder
ARTILLERY -> siege calibre and effectiveness, not a claim of general weakness
SUPPLY -> long haul from Lahore constrains repeated operations
COMMAND -> coordination, season and pressure narrow the campaign window
THREE ATTEMPTS -> field capacity does not become a successful siege
RESULT -> recovery is abandoned while diplomacy and trade continue.""",
            ["Qandahar sieges", "1649-53", "Artillery", "Logistics"],
        ),
        (
            "Evidence and the bounded modern bridge",
            "evidence-matrix",
            """CHRONICLES -> sequence and court claim | patronage and victory language
LETTERS / GIFTS -> status and communication | not private intention
MERCHANTS / TRAVELLERS -> routes and exchange | selective outsider lens
FORTS / MAPS -> material capacity and geography | not policy motive
2026 INDIA-IRAN -> navigation and commerce | analogy, not continuity
METHOD -> match each claim to a source and state its limit.""",
            ["Sources", "PMIndia 2026", "India-Iran", "Source criticism"],
        ),
        (
            "Topic 19 final answer spine",
            "answer-synthesis",
            """DEFINE -> qualified court diplomacy across a porous northwest world
MAP -> Indian core, Kabul-Qandahar line, Iran and Balkh field
TRACE -> Akbar balance -> Jahangir 1622 -> Shah Jahan 1638 / 1646-53
EXPLAIN -> security + commerce + honour + dynastic ambition
TEST -> diplomacy, garrison, supply, local allies and source limits
VERDICT -> India-centred defence was central but never the whole story.""",
            ["Answer architecture", "Policy evolution", "Qualified verdict"],
        ),
    ],
    "medieval-indian-history-20": [
        (
            "Jahangir's reign: the chronology spine",
            "timeline",
            """1605 -> accession | 1606 -> Khusrau revolt and Guru Arjan episode
1611 -> marriage to Nur Jahan | 1613-15 -> Mewar settlement
1615-19 -> Roe mission | 1620 -> Kangra captured
1622 -> Qandahar lost; Khurram crisis intensifies
1622-25 -> Khurram rebellion | 1626 -> Mahabat Khan coup
1627 -> Jahangir dies; succession field is settled for Shah Jahan.""",
            ["Jahangir", "Chronology", "Khusrau", "Nur Jahan", "Mahabat Khan"],
        ),
        (
            "Continuity, consolidation and contest",
            "balance-sheet",
            """CONTINUITY -> Akbar's fiscal-military state and composite elite survive
CONSOLIDATION -> Mewar, Kangra and negotiated commercial access
CONTEST -> princes, household networks, nobles and unfinished frontiers
CAPACITY -> campaigns and administration continue despite court conflict
LIMIT -> Qandahar, Deccan and succession expose coordination problems
VERDICT -> neither automatic decline nor an untroubled golden age.""",
            ["Continuity", "Consolidation", "Court politics", "Decline debate"],
        ),
        (
            "Accession, orders and the chain of justice",
            "claim-reach-map",
            """ACCESSION -> titles, rewards and audience reproduce elite confidence
TWELVE ORDERS -> memoir publicises a programme of rectitude and control
ZANJIR-I-ADL -> gold chain makes royal accessibility visible and audible
IMPLEMENTATION -> proclamation must be separated from local compliance
LIMIT -> ruler-centred discretion is not modern equal rule of law
METHOD -> object / claim / transmission / social reach.""",
            ["Accession", "Twelve orders", "Zanjir-i-adl", "Justice"],
        ),
        (
            "Khusrau and Guru Arjan: event plus source matrix",
            "evidence-matrix",
            """KHUSRAU 1606 -> princely succession revolt moving through Punjab
JAHANGIRNAMA -> imperial suspicion and self-justification
SIKH TRADITION -> community memory of Guru Arjan's martyrdom
OTHER ACCOUNTS -> fiscal, political and religious dimensions need comparison
TURNING POINT -> rupture deepens; later militarisation has its own chronology
TRAP -> avoid both communal monocause and sanitised denial of coercion.""",
            ["Khusrau", "Guru Arjan", "Punjab", "Source criticism"],
        ),
        (
            "Mewar 1615: pressure joined to accommodation",
            "comparison-matrix",
            """MUGHAL PRESSURE -> Khurram's campaign and sustained imperial weight
MEWAR COST -> exhaustion and disruption make settlement attractive
HIERARCHY -> Mughal suzerainty is recognised
HONOUR -> Amar Singh avoids personal attendance; Karan Singh is received
RESTRAINT -> no personal humiliation or compulsory marriage bargain
VERDICT -> incorporation without dynastic absorption or equality.""",
            ["Mewar settlement", "Amar Singh", "Karan Singh", "Prince Khurram"],
        ),
        (
            "English commercial diplomacy without colonial teleology",
            "process",
            """HAWKINS / SWALLY -> petitioning trade; maritime leverage, not sovereignty
ROE 1615-19 -> gifts, audiences, delays and rank disputes
1618 FACILITIES -> trading permission on Mughal terms, not territory
METHOD -> reject colonial teleology; read Company records as interested sources.""",
            ["William Hawkins", "Thomas Roe", "Swally", "Surat", "1618 farman"],
        ),
        (
            "Nur Jahan's authority: evidence before label",
            "evidence-matrix",
            """ACCESS / KINSHIP -> proximity links household and service networks
FARMANS -> directed intervention; COINS -> exceptional public visibility
ITIMAD-UD-DAULAH -> commemoration and architectural patronage
LIMIT -> strong evidence of unusual authority, not proof that she ruled alone.""",
            ["Nur Jahan", "Farmans", "Coins", "Ghiyas Beg", "Itimad-ud-Daulah"],
        ),
        (
            "The fixed-junta thesis under review",
            "myth-vs-rule",
            """FIXED-JUNTA CLAIM -> Nur Jahan, kin and Khurram form one lasting bloc
TEST -> alliances shift after 1622; emperor, princes and offices remain operative
GENDER RULE -> correct exaggeration without erasing exceptional female agency
BETTER MODEL -> changing household-service networks around access and succession.""",
            ["Nur Jahan junta", "Beni Prasad", "Nurul Hasan", "Faction"],
        ),
        (
            "Why Khurram rebelled, 1622-25",
            "cause-mechanism-effect",
            """SUCCESSION FEAR -> rival claims and changing household alignments
QANDAHAR ORDER -> absence and command risks; resources sustain bargaining
NUR JAHAN / SHAHRYAR -> perceived preference sharpens Khurram's insecurity
VERDICT -> converging pressures cause rebellion; administration survives the test.""",
            ["Prince Khurram", "Qandahar 1622", "Shahryar", "Succession"],
        ),
        (
            "Mahabat Khan's coup, 1626",
            "process",
            """GRIEVANCE / JHELUM -> court tensions meet a tactical river-crossing opening
SEIZURE -> Mahabat controls the emperor's person with Rajput support
LIMIT -> sovereign body is not treasury, scribal state or broad consent
NUR JAHAN -> coalition and manoeuvre show why spectacular capture cannot govern.""",
            ["Mahabat Khan", "Jhelum", "Coup", "Nur Jahan"],
        ),
        (
            "Jahangir as ruler and historical source",
            "balance-sheet",
            """CAPACITY / LIMITS -> Mewar and Kangra; Deccan, Qandahar and princely conflict
RELIGION -> inherited accommodation coexists with selective coercion
JAHANGIRNAMA -> nature, art and self-fashioning; memoir needs corroboration
VERDICT -> capable but uneven; health and habit cannot replace institutions.""",
            ["Jahangirnama", "Mewar", "Kangra", "Religious policy", "Sources"],
        ),
        (
            "Topic 20 final answer spine",
            "answer-synthesis",
            """OPEN -> continuity plus active political reproduction after 1605
TRACE -> accession -> Khusrau -> Mewar -> Nur Jahan -> 1622 -> 1626
PROVE -> orders, settlement terms, farmans, coins, tomb and memoir
ANALYSE -> emperor, household, princes, nobles and frontier pressures
QUALIFY -> source reach, changing factions, gender structure and coercion
VERDICT -> consolidation with contest, not decline or sole female rule.""",
            ["Answer architecture", "Chronology", "Evidence", "Qualified verdict"],
        ),
    ],
}


def remove_embedded_cover(fragment: str) -> str:
    return re.sub(
        r"(?ms)\n*!\[[^\n]*\]\([^)\n]*(?:00_cover|00_00_cover|01_01_cover)\.png\)"
        r"(?:\s*\n+\*[^\n]*\*)?\s*",
        "\n",
        fragment,
        count=1,
    ).strip()


def root_asset_paths(fragment: str) -> str:
    return re.sub(
        r"(\]\()(?:(?:\.\./)+)notes/",
        r"\1notes/",
        fragment,
    )


def normalize_mcq_fragment(fragment: str) -> str:
    text = HELPERS.normalize_mcq_fragment(fragment)
    return re.sub(
        r"(?mi)^\*\*Answer:\s*([A-D])"
        r"(?:[.\s]+.*)?\*\*\s*$",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        text,
    )


def assemble_topic_19(config_value: dict[str, object]) -> str:
    source = HELPERS.strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    source = remove_embedded_cover(root_asset_paths(source))
    source = re.sub(r"(?m)^# (PART .+)$", r"## \1", source)
    source = re.sub(
        r"(?m)^# (FINAL CONSOLIDATED REGISTER NOTES.+)$",
        r"## \1",
        source,
    )
    preamble, sections = BASE.split_h2(source)
    preamble = BASE.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    preamble_parts = [cover, preamble]
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    register_mode = False
    for title, fragment in sections:
        if title.startswith("Learning roadmap"):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if title.startswith("19. Current-affairs anchor"):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if register_mode:
            bucket = "register"
        elif title.startswith("FINAL CONSOLIDATED"):
            register_mode = True
            bucket = "register"
        elif re.match(r"^\d+\.", title):
            bucket = "basic"
        elif title.startswith(
            (
                "PART I ",
                "PART II ",
                "PART III ",
                "PART IV ",
                "PART V ",
                "PART VI ",
                "PART VII ",
                "PART VIII ",
                "PART IX ",
            )
        ):
            bucket = "basic"
        elif title.startswith("PART IX-A"):
            bucket = "advanced"
        elif title.startswith(
            (
                "Original learning MCQ",
                "Original broad MCQ",
                "Original remedial MCQ",
            )
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith(
            (
                "PART X",
                "PART XI",
                "Transparent PYQ audit",
                "Practice visual labs",
                "Mains ",
                "Practice completion check",
            )
        ):
            bucket = "practice"
        else:
            raise ValueError(f"Unclassified Topic 19 section: {title}")
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def assemble_topic_20(config_value: dict[str, object]) -> str:
    source = HELPERS.strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    source = remove_embedded_cover(root_asset_paths(source))
    source = re.sub(r"(?m)^# (PART .+)$", r"## \1", source)
    source = re.sub(
        r"(?m)^# (FINAL CONSOLIDATED REGISTER NOTES.+)$",
        r"## \1",
        source,
    )
    preamble, sections = BASE.split_h2(source)
    preamble = BASE.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    preamble_parts = [cover, preamble]
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    register_mode = False
    for title, fragment in sections:
        if title.startswith("Learning roadmap"):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if register_mode:
            bucket = "register"
        elif title.startswith("FINAL CONSOLIDATED"):
            register_mode = True
            bucket = "register"
        elif re.match(r"^\d+\.", title):
            bucket = "basic"
        elif title.startswith(
            (
                "PART I ",
                "PART II ",
                "PART III ",
                "PART IV ",
                "PART V ",
                "PART VI ",
                "PART VII ",
                "PART VIII ",
            )
        ):
            bucket = "basic"
        elif title.startswith(
            (
                "PART IXA",
                "PART IXB",
                "PART IXC",
                "Evidence bank ",
                "Advanced lab ",
                "Synthesis extension ",
            )
        ):
            bucket = "advanced"
        elif title.startswith(("PART IX ", "Verified PYQ audit", "PART X")):
            bucket = "practice"
        elif title.startswith(("Learning MCQ", "Broad MCQ", "Remedial MCQ")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        else:
            raise ValueError(f"Unclassified Topic 20 section: {title}")
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-19":
        return assemble_topic_19(config_value)
    return assemble_topic_20(config_value)


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
                "source_markdown": BASE.relative(Path(config_value["canonical"])),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Medieval Indian History learner-v2 Topics 19-20",
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


def write_graphical_spec(
    config_value: dict[str, object],
    markdown: str,
) -> Path:
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
        source_markdown_path=BASE.relative(source_path),
        ascii_spec_path=BASE.relative(ASCII_PATH),
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
    local_books = [SATISH_HISTORY, SATISH_MUGHALS]
    official_sources = list(config_value["official_question_sources"])
    source_files = [
        Path(config_value["basic"]),
        Path(config_value["advanced"]),
        Path(config_value["canonical"]),
        *[Path(path) for path in config_value["extra_markdown"]],
        source_path,
        *[ROOT / item for item in BASE_GENERATOR.COMMON_CROSS],
        *[ROOT / item for item in BASE_GENERATOR.PYQ_INDEXES],
        *official_sources,
        *local_books,
        Path(config_value["legacy_main"]),
        Path(config_value["legacy_workbook"]),
        ROOT / str(config_value["cover_path"]).replace("/", "\\"),
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *BASE.image_sources(Path(config_value["canonical"])),
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
            "- Subject-wide Syllabus - "
            + str(config_value["title"])
        ),
        "source_markdown": BASE.relative(source_path),
        "source_basic": BASE.relative(Path(config_value["basic"])),
        "source_canonical": BASE.relative(Path(config_value["canonical"])),
        "source_advanced": BASE.relative(Path(config_value["advanced"])),
        "manifest": BASE.relative(SECTION_MANIFEST),
        "cross_topic_sources": BASE_GENERATOR.COMMON_CROSS,
        "pyq_indexes": BASE_GENERATOR.PYQ_INDEXES,
        "official_question_sources": [
            BASE.relative(path) for path in official_sources
        ],
        "local_ocr_sources": [BASE.relative(path) for path in local_books],
        "live_sources": config_value["live_sources"],
        "source_files": [BASE.relative(path) for path in deduplicated],
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
        print(BASE.relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
