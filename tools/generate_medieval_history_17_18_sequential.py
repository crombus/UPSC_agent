"""Assemble Medieval History learner-v2 Topics 17-18 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_15_16_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-17-18-2026-08-30-sequential.json"
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
    )
    value["official_question_sources"] = official_question_sources
    return value


TOPICS = [
    topic_config(
        17,
        "Akbar's Religious Views: Ibadat Khana & Din-i-Ilahi",
        "17_Akbar-Religious-Views-Ibadat-Khana-Din-i-Ilahi_Complete-Topic-Package.md",
        "17_Akbar-Religious-Views-Din-i-Ilahi.md",
        "17_Akbar-Religious-Views-Din-i-Ilahi.md",
        "17_Akbar-Religious-Views-Ibadat-Khana-Din-i-Ilahi_Complete-Learning-Session_2026-08-18.pdf",
        "17_Akbar-Religious-Views-Ibadat-Khana-Din-i-Ilahi_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "1 verified direct 2025 GS-I Mains PYQ; 18 learning, 40 broad and "
        "12 remedial MCQs; 10 solved Mains answers with source criticism.",
        ["https://whc.unesco.org/en/list/255/"],
        "UNESCO's Fatehpur Sikri property page was rechecked on 30 August "
        "2026. It supports a bounded material-history bridge: Akbar made the "
        "planned city his capital, its administrative and religious ensemble "
        "expresses a late sixteenth-century imperial centre, and ASI manages "
        "its conservation. It does not identify a surviving structure as the "
        "Ibadat Khana with final archaeological certainty or prove the content, "
        "participants, motives or effects of court debates; those remain "
        "controlled by repository Markdown, OCR books and source criticism.",
        "Akbar religious policy Ibadat Khana and sulh-i-kul cover",
        "notes/Medieval-Indian-History/assets/"
        "17_Akbar-Religious-Views-Ibadat-Khana-Din-i-Ilahi/01_01_cover.png",
        [
            "learning-sessions\\17_Akbar-Religious-Views-Ibadat-Khana-Din-i-Ilahi_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\17_Akbar-Religious-Views-Ibadat-Khana-Din-i-Ilahi_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [GS1_2025],
    ),
    topic_config(
        18,
        "The Deccan & the Mughals (to 1657)",
        "18_Deccan-Mughals-to-1657_Complete-Topic-Package.md",
        "18_Deccan-and-the-Mughals.md",
        "18_Deccan-and-the-Mughals.md",
        "18_Deccan-Mughals-to-1657_Complete-Learning-Session_2026-08-18.pdf",
        "18_Deccan-Mughals-to-1657_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 remedial "
        "MCQs; 10 original solved Mains answers with a strict 1657 boundary.",
        [
            "https://whc.unesco.org/en/list/1739/",
            "https://whc.unesco.org/en/tentativelists/5887/",
        ],
        "UNESCO's Maratha Military Landscapes and Deccan Sultanate tentative-"
        "list pages were rechecked on 30 August 2026. The first supports only "
        "a bounded later bridge: twelve fortifications adapted chiefly from "
        "the late seventeenth century formed a strategic Maratha network. It "
        "must not be projected backward as a mature Maratha state before 1657. "
        "The second supports the material setting of Gulbarga, Bidar, Bijapur "
        "and Golconda, including forts, water systems and walled cities; it "
        "does not independently prove Mughal campaign motives, treaty terms "
        "or state capacity. Those remain controlled by repository Markdown, "
        "OCR books and historical source criticism.",
        "Mughal Deccan policy Malik Ambar and 1636 settlement cover",
        "notes/Medieval-Indian-History/assets/"
        "18_Deccan-Mughals-to-1657/00_00_cover.png",
        [
            "learning-sessions\\18_Deccan-Mughals-to-1657_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\18_Deccan-Mughals-to-1657_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-17": [
        (
            "Evolution, not a sudden creed",
            "timeline",
            """1563 -> pilgrim tax remitted | 1564 -> jizyah abolished
1575 -> Ibadat Khana built at Fatehpur Sikri
1578 -> debates widened beyond Muslim participants
1579 -> Mahzar gives Akbar a bounded arbitral role
1580-81 -> rebellion and orthodox opposition sharpen the sovereignty issue
1581-82 -> public debates close; Tauhid-i-Ilahi discipleship phase emerges.""",
            ["Chronology", "Pilgrim tax", "Jizyah", "Ibadat Khana", "Mahzar"],
        ),
        (
            "Five layers of Akbar's religious policy",
            "systems-map",
            """PERSONAL -> Chishti links, inquiry, prayer and spiritual search
FISCAL -> selected religious disabilities removed in 1563-64
INTELLECTUAL -> Ibadat Khana, translations and comparative encounter
SOVEREIGN -> Mahzar and final imperial arbitration
GOVERNING -> sulh-i-kul, justice and non-sectarian accommodation
DISCIPLESHIP -> small Tauhid-i-Ilahi circle around the sovereign.""",
            ["Personal belief", "State policy", "Sulh-i-kul", "Discipleship"],
        ),
        (
            "Ibadat Khana debate cycle",
            "process",
            """BUILD 1575 -> court-linked prayer and disputation forum
FIRST PHASE -> ulama, Sufis, scholars and companions
CONFLICT -> doctrine, precedence and court status become entangled
WIDENING -> Hindu, Jain, Christian and Zoroastrian interlocutors
PARADOX -> more voices, but no shared theological settlement
CLOSURE -> public forum ends; private inquiry and translation continue.""",
            ["Ibadat Khana", "Participants", "Debate", "Closure"],
        ),
        (
            "Interfaith encounter: influence is not conversion",
            "comparison-matrix",
            """HINDU -> interlocutors and translation | not Akbar becoming Hindu
JAIN -> petitions and animal-life concerns | not a universal permanent ban
JESUIT -> books, images and theology | courtesy is not Christian conversion
ZOROASTRIAN -> Meherji Rana and light symbols | symbolism is not adoption
SUFI-ISLAMIC -> tawhid and pir-murid idiom remain central continuities
RULE: state the encounter, evidence, bounded influence and non-equivalence.""",
            ["Hindu", "Jain", "Jesuit", "Zoroastrian", "Sufi"],
        ),
        (
            "The debate paradox",
            "cause-mechanism-effect",
            """ROYAL FORUM -> participants compete before the emperor
DOCTRINAL CERTAINTY -> argument hardens rather than dissolves
COURT STATUS -> theological dispute also becomes political rivalry
AKBAR'S LESSON -> no one clerical network can secure plural order
POLICY SHIFT -> theological concord yields to non-sectarian governance
VERDICT: dialogue failed as consensus but mattered for statecraft.""",
            ["Debate failure", "Court politics", "Statecraft"],
        ),
        (
            "Mahzar: scope before significance",
            "myth-vs-rule",
            """MYTH -> Akbar became pope, prophet or an infallible lawgiver
RULE -> after jurists disagree, he selects an existing opinion for public welfare
SIGNIFICANCE -> clerical monopoly narrows as imperial arbitration grows
LIMIT -> bounded juristic choice is not unlimited sacred legislation.""",
            ["Mahzar", "Imperial sovereignty", "Decree of Infallibility"],
        ),
        (
            "Sulh-i-kul as a governing principle",
            "argument-tree",
            """PROBLEM -> a plural, ranked empire needs order beyond theological agreement
MECHANISM -> justice, tax reform, wider service and calibrated patronage
LIMIT -> the emperor still defines inclusion, protection and coercion
VERDICT: durable imperial idiom, not modern constitutional secularism.""",
            ["Sulh-i-kul", "Justice", "Composite nobility", "Limits"],
        ),
        (
            "Tauhid-i-Ilahi: neither mass religion nor nothing",
            "balance-sheet",
            """ABSENT -> scripture, priesthood, congregation and mass mission
PRESENT -> initiation, conduct, greetings and graded devotion language
SCALE / IDIOM -> small elite circle; Birbal; Sufi-like guide-disciple bond
VERDICT: loyalist spiritual fellowship, not a new universal religion.""",
            ["Tauhid-i-Ilahi", "Din-i-Ilahi", "Birbal", "Discipleship"],
        ),
        (
            "Inclusion and coercion in one empire",
            "tension-map",
            """INCLUSION -> tax relief, service, dialogue and non-sectarian justice
HIERARCHY / COERCION -> rank, conquest and punishment remain sovereign tools
SOCIAL LIMIT -> orders are uneven; policy depends on the ruler
RULE: praise innovation without inventing equality or neutrality.""",
            ["Inclusion", "Coercion", "Hierarchy", "Implementation"],
        ),
        (
            "Source triangle and evidentiary limits",
            "evidence-matrix",
            """ABUL FAZL -> policy and kingship | courtly legitimation
BADAUNI / JESUITS -> dissent and encounter | polemic and conversion hopes
ORDERS / ARCHITECTURE -> policy acts and setting | uneven reach, no transcript
METHOD: state what each source proves, cannot prove and needs checked.""",
            ["Abul Fazl", "Badauni", "Jesuits", "Material evidence"],
        ),
        (
            "2025 GS-I syncretism answer map",
            "answer-synthesis",
            """OPEN -> layered state-building programme, not a sudden mass faith
EARLY -> 1563-64 fiscal change; Ibadat Khana inquiry and widening
STATE -> Mahzar arbitration; sulh-i-kul and composite legitimacy
CLOSE -> Tauhid fellowship was small and policy remained ruler-centred.""",
            ["2025 GS-I", "Religious syncretism", "Answer architecture"],
        ),
        (
            "Topic 17 final answer spine",
            "answer-synthesis",
            """DEFINE -> separate belief, debate, sovereignty, governance and fellowship
TRACE -> 1563-64 -> 1575 -> 1578 -> 1579 -> 1581-82
PROVE -> taxes, Ibadat Khana, Mahzar, sulh-i-kul and Tauhid evidence
ANALYSE -> plural empire, elite integration and public order
QUALIFY -> source bias, coercion, hierarchy and limited implementation
VERDICT -> innovative state formation, not modern secularism or mass religion.""",
            ["Answer architecture", "Chronology", "Qualified verdict"],
        ),
    ],
    "medieval-indian-history-18": [
        (
            "The Deccan as a connected but frictional field",
            "spatial-map",
            """AGRA / MALWA -> mobilisation and northern imperial core
KHANDESH / BURHANPUR -> corridor, market and staging point
ASIRGARH -> fortified gateway, not automatic plateau control
BERAR / BALAGHAT -> operational foothold and contested revenue
AHMADNAGAR -> claimant, fort and hinterland can come apart
BIJAPUR / GOLCONDA -> autonomous courts, resources and southern ambitions.""",
            ["Khandesh", "Burhanpur", "Asirgarh", "Berar", "Ahmadnagar"],
        ),
        (
            "Deccan chronology 1562-1657",
            "timeline",
            """1562-76 -> Khandesh contacts and submission | 1591 -> embassies
1595-96 -> Ahmadnagar crisis; Chand Bibi; Berar settlement
1600-01 -> Ahmadnagar fort, Balaghat, Asirgarh and Khandesh
1610 -> Malik Ambar reverses much of Akbar's gain
1616-21 -> Mughal recovery followed by Jahangir's limited policy
1633 -> Daulatabad | 1636 -> treaties | 1656-57 -> compact breached.""",
            ["Chronology", "Chand Bibi", "Malik Ambar", "1636 treaties"],
        ),
        (
            "A spectrum of political relations",
            "continuum",
            """DIPLOMACY -> recognition sought without immediate annexation
ALLIANCE -> service and negotiated cooperation
SUZERAINTY -> tribute, khutba or arbitration under retained local rule
OCCUPATION -> army controls a fort or zone without durable integration
ANNEXATION -> territorial incorporation plus administrative claim
TRAP: do not translate every hierarchy into a modern sovereignty binary.""",
            ["Diplomacy", "Suzerainty", "Occupation", "Annexation"],
        ),
        (
            "Chand Bibi and the Ahmadnagar crisis",
            "process",
            """SUCCESSION DISPUTE -> external intervention becomes possible
CHAND BIBI -> defends, seeks allies and negotiates under factional pressure
1596 TERMS -> Bahadur recognised; Berar ceded; suzerainty accepted
RENEWED WAR -> factions and the Berar dispute erode the bargain
1600 SIEGE -> proposed negotiation is branded betrayal; Chand Bibi is killed
LESSON: constrained agency, not a romantic warrior-queen-only story.""",
            ["Chand Bibi", "Ahmadnagar", "Berar", "Factionalism"],
        ),
        (
            "Akbar's foothold and its limits",
            "balance-sheet",
            """GAIN -> Berar, Balaghat, Ahmadnagar fort and Khandesh-Asirgarh
STRATEGY -> diplomacy first, then force through succession opportunity
VALUE -> routes, prestige, revenue claims and a Deccan entry platform
LIMIT -> Bijapur and Golconda remain outside direct Mughal rule
LIMIT -> a captured fort does not secure countryside or local loyalty
VERDICT: meaningful foothold, not conquest of the whole Deccan.""",
            ["Akbar", "1591 missions", "Ahmadnagar", "Asirgarh"],
        ),
        (
            "Malik Ambar's resistance engine",
            "systems-map",
            """LEGITIMACY -> Nizam Shahi claimant and Ahmadnagar state frame
LEADERSHIP -> Habshi political and military organisation
COALITION -> Maratha bargis, local chiefs and shifting Bijapur support
METHOD -> mobility, supply disruption, terrain knowledge and negotiation
FISCAL BASE -> attributed measurement and zabti-type reconstruction
LIMIT -> alliances shift; success delays but does not permanently save the state.""",
            ["Malik Ambar", "Habshi", "Bargi", "Revenue policy"],
        ),
        (
            "Why conquest did not equal consolidation",
            "causal-loop",
            """DISTANCE + SEASON -> supplies and communications become costly
FORT CAPTURE -> garrisons consume men and revenue
LOCAL INTERMEDIARIES -> information and collection require bargaining
MOBILE COALITIONS -> attack routes and avoid set-piece weakness
NOMINAL REVENUE -> differs from realised, usable surplus
LOOP: incomplete control creates resistance, cost and renewed intervention.""",
            ["State capacity", "Logistics", "Intermediaries", "Revenue"],
        ),
        (
            "Jahangir: recovery with restraint",
            "argument-tree",
            """INHERITANCE -> Ambar has reversed much of Akbar's position
COMMAND PROBLEM -> rival Mughal forces struggle to coordinate
1616-17 -> Khan-i-Khanan and Prince Khurram recover ground
DIPLOMACY -> attempts to detach allies and recognise negotiated hierarchy
CHOICE -> Jahangir does not convert victory into unlimited expansion
VERDICT: limited commitment can be policy, not simple military weakness.""",
            ["Jahangir", "Prince Khurram", "Khan-i-Khanan", "Restraint"],
        ),
        (
            "The pre-Shivaji Maratha bridge",
            "network-map",
            """DESHMUKHS -> local revenue, armed following and territorial knowledge
BARGIS -> mobile cavalry serving changing Deccan coalitions
MALIK AMBAR -> creates opportunities, training and bargaining space
SHAHJI -> moves across Nizam Shahi, Bijapuri and Mughal service fields
RESULT -> capability and confidence grow before a mature Maratha state
BOUNDARY: do not project later nationalism or Shivaji's polity backward.""",
            ["Maratha bridge", "Deshmukhs", "Bargis", "Shahji"],
        ),
        (
            "Daulatabad and the 1636 settlement",
            "comparison-matrix",
            """1633 -> Daulatabad falls; Nizam Shahi dynasty is extinguished
BIJAPUR -> suzerainty, indemnity, arbitration and a Shahji condition
GOLCONDA -> khutba and tribute under Mughal protection
BUFFER LOGIC -> local states retain initiative while direct costs stay lower
COERCION -> force makes the hierarchy possible; parties are not equals
VERDICT: pragmatic institutional design, not full Deccan annexation.""",
            ["Daulatabad", "Bijapur", "Golconda", "1636 treaties"],
        ),
        (
            "Why the 1656-57 compact broke",
            "cause-mechanism-effect",
            """STABLE EXPECTATION -> tribute, protection, arbitration and buffer autonomy
SOUTHERN GROWTH -> Bijapur and Golconda gain resources and confidence
MUGHAL PRESSURE -> fiscal claims, compensation and territorial demands
CRISIS -> Mir Jumla and succession disputes create intervention openings
EFFECT -> trust in the 1636 bargain weakens before the later wars
BOUNDARY: stop at 1657; do not import Aurangzeb's mature annexations.""",
            ["1656 Golconda", "1657 Bijapur", "Treaty credibility"],
        ),
        (
            "Topic 18 final answer spine",
            "answer-synthesis",
            """OPEN -> Mughal policy evolved within a connected but costly frontier
AKBAR -> suzerainty diplomacy, selective force and an incomplete foothold
AMBAR -> coalition, mobility and local capacity expose imperial limits
JAHANGIR -> recovery joined to deliberate restraint
SHAH JAHAN -> 1633 extinction, 1636 buffers and 1656-57 breach
CLOSE -> expansion gained leverage but repeatedly outran durable control.""",
            ["Answer architecture", "Policy evolution", "Qualified verdict"],
        ),
    ],
}


def remove_embedded_cover(fragment: str) -> str:
    return re.sub(
        r"(?ms)\n*!\[[^\n]*\]\([^)\n]*(?:00_00_cover|01_01_cover)\.png\)"
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


def assemble_topic_17(config_value: dict[str, object]) -> str:
    source = HELPERS.strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    source = remove_embedded_cover(root_asset_paths(source))
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
    for title, fragment in sections:
        if title.startswith("Source base"):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if title.startswith("PART I"):
            bucket = "basic"
        elif title.startswith(
            (
                "PART II",
                "PART III",
                "PART IV",
                "PART V",
                "PART VI",
                "PART VII",
                "PART VIII",
                "PART IX",
            )
        ):
            bucket = "basic"
        elif title.startswith(("Learning MCQ", "Broad MCQ", "Remedial MCQ")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith(("PART X", "Examiner-grade solved Mains")):
            bucket = "practice"
        elif title.startswith("Final consolidated"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 17 section: {title}")
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def assemble_topic_18(config_value: dict[str, object]) -> str:
    source = HELPERS.strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    source = root_asset_paths(source)
    source = re.sub(r"(?m)^# (PART .+)$", r"## \1", source)
    source = re.sub(
        r"(?m)^# (FINAL CONSOLIDATED REGISTER NOTES.+)$",
        r"## \1",
        source,
    )
    preamble, sections = BASE.split_h2(source)
    preamble = remove_embedded_cover(BASE.strip_title(preamble))
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    preamble_parts = [cover, preamble]
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    bucket = "basic"
    for title, fragment in sections:
        if title.startswith("How to use this complete learning session"):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if title.startswith("PART V - ADVANCED EVIDENCE LABS"):
            bucket = "advanced"
        elif title.startswith("PART V - PYQ AUDIT"):
            bucket = "practice"
        elif title.startswith(("Learning MCQ", "Broad Topic MCQ", "Remedial MCQ")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Examiner-grade Original Mains"):
            bucket = "practice"
        elif title.startswith("FINAL CONSOLIDATED"):
            bucket = "register"
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-17":
        return assemble_topic_17(config_value)
    return assemble_topic_18(config_value)


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
        "scope": "Medieval Indian History learner-v2 Topics 17-18",
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
