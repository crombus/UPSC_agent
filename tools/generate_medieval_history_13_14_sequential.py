"""Assemble Medieval History learner-v2 Topics 13-14 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_11_12_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-13-14-2026-08-30-sequential.json"
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
BASE_GENERATOR = previous.BASE_GENERATOR
BASE = previous.BASE


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
    return previous.topic_config(
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
        [SATISH_HISTORY, SATISH_MUGHALS],
    )


TOPICS = [
    topic_config(
        13,
        "Struggle for Empire: Afghans, Rajputs & Humayun",
        "13_Struggle-for-Empire-Afghans-Rajputs-Humayun_Complete-Topic-Package.md",
        "13_Struggle-for-Empire-Humayun-Afghans.md",
        "13_Struggle-for-Empire-Humayun-Afghans.md",
        "13_Struggle-for-Empire-Afghans-Rajputs-Humayun_Complete-Learning-Session_2026-08-18.pdf",
        "13_Struggle-for-Empire-Afghans-Rajputs-Humayun_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 remedial "
        "MCQs; 10 original solved Mains questions with transparent adjacent "
        "routing.",
        ["https://whc.unesco.org/en/list/232/"],
        "UNESCO's Humayun's Tomb property page was rechecked on 30 August "
        "2026. It supports a bounded dynastic-memory and source-method bridge: "
        "the tomb was built in the 1560s under Akbar's patronage, combines "
        "Persian and Indian craftsmanship, and remains the subject of "
        "archaeology-led conservation. It does not prove Humayun's campaign "
        "chronology, motives, battlefield decisions or the Karnavati tradition; "
        "those remain controlled by repository Markdown, OCR books and source "
        "criticism.",
        "Humayun Afghans Rajputs and struggle for empire cover",
        "notes/Medieval-Indian-History/assets/"
        "13_Struggle-for-Empire-Afghans-Rajputs-Humayun/00_cover.png",
        [
            "learning-sessions\\13_Struggle-for-Empire-Afghans-Rajputs-Humayun_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\13_Struggle-for-Empire-Afghans-Rajputs-Humayun_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
    ),
    topic_config(
        14,
        "Sher Shah Sur & the Sur Empire",
        "14_Sher-Shah-Sur-Empire_Complete-Topic-Package.md",
        "14_Sher-Shah-and-the-Sur-Empire.md",
        "14_Sher-Shah-and-the-Sur-Empire.md",
        "14_Sher-Shah-Sur-Empire_Complete-Learning-Session_2026-08-18.pdf",
        "14_Sher-Shah-Sur-Empire_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 remedial "
        "MCQs; 10 original solved Mains questions with source and comparison "
        "drills.",
        ["https://rohtas.nic.in/tourist-place/sher-shah-suri-tomb/"],
        "The Rohtas district administration's Sher Shah Suri Tomb page was "
        "rechecked through the official government listing on 30 August 2026. "
        "It supports a bounded material-history bridge to the protected "
        "octagonal lake tomb at Sasaram and to Sher Shah's continuing public "
        "memory. The modern tourism description cannot authenticate every "
        "administrative claim, quotation or causal judgement; those remain "
        "controlled by repository Markdown, OCR books, coins, monuments and "
        "source criticism.",
        "Sher Shah Sur empire state capacity and administration cover",
        "notes/Medieval-Indian-History/assets/"
        "14_Sher-Shah-Sur-Empire/00_cover.png",
        [
            "learning-sessions\\14_Sher-Shah-Sur-Empire_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\14_Sher-Shah-Sur-Empire_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-13": [
        (
            "The central problem: conquest without consolidation",
            "argument-tree",
            """BABUR'S VICTORIES -> a core, prestige and a dynastic claim
HUMAYUN'S INHERITANCE -> weak finance + thin administration + rival elites
COMPETING FIELDS -> Afghans in the east + Gujarat-Malwa + Rajput powers
IMPERIAL AMBITION -> Delhi, Gujarat and Bengal pursued before deep rooting
RESULT -> military reach repeatedly outruns revenue, routes and noble commitment
VERDICT: Humayun's fall joins structural weakness to avoidable choices.""",
            ["Unfinished conquest", "State capacity", "Competing fields"],
        ),
        (
            "Humayun chronology 1530-1556",
            "timeline",
            """30 Dec 1530 -> accession | 1533-34 -> Din Panah
1535 -> Mandu, Champaner and Gujarat campaign successes
1537-38 -> six-month Chunar siege and eastern advance
1538-39 -> Gaur occupation and communications crisis
26 Jun 1539 -> Chausa | 17 May 1540 -> Kannauj/Bilgram
1545 -> Qandahar and Kabul recovered | 1555 Delhi | 1556 death.""",
            ["Chronology", "Din Panah", "Chausa", "Kannauj", "Restoration"],
        ),
        (
            "Inherited balance sheet",
            "comparison-matrix",
            """ASSET -> Delhi-Agra core, Timurid prestige and campaign capability
FINANCE -> stretched treasury and large assignments to begs
ADMINISTRATION -> conquest not converted into routine territorial control
EAST -> Afghan chiefs and Sher Khan retain regional depth
WEST -> Bahadur Shah links Gujarat, Malwa and Rajasthan
DYNASTY -> princely-share expectations complicate unified sovereignty.""",
            ["Finance", "Begs", "Afghan challenge", "Bahadur Shah"],
        ),
        (
            "Brothers: chronology before blame",
            "timeline",
            """KAMRAN -> Kabul/Qandahar, then Lahore-Multan and the Punjab hinge
EARLY PHASE -> khutba and sikka remain in Humayun's name
ASKARI -> Gujarat command becomes an administrative cohesion test
HINDAL -> Agra move matters during the stretched Bengal campaign
AFTER CHAUSA -> Kamran withholds hardened troops from Humayun
RULE: fraternal politics changes by time and theatre; avoid timeless guilt.""",
            ["Kamran", "Askari", "Hindal", "Timurid succession"],
        ),
        (
            "Rajput-Gujarat-Mughal western triangle",
            "spatial-map",
            """GUJARAT-MALWA -> Bahadur Shah's wealth, artillery and regional expansion
MEWAR / CHITTOR -> Rajput power inside the western strategic field
DELHI-AGRA -> Mughal core threatened through eastern Rajasthan and Malwa
HUMAYUN -> supply pressure at Mandsor, then Mandu and Champaner
KARNAVATI STORY -> later memory; contemporary corroboration is absent
TRAP: Rajputs were not one permanent bloc and legend is not event proof.""",
            ["Bahadur Shah", "Mewar", "Chittor", "Karnavati"],
        ),
        (
            "Gujarat: victory without settlement",
            "cause-mechanism-effect",
            """CAMPAIGN -> Mandsor pressure -> Mandu -> Champaner -> Ahmedabad
MILITARY RESULT -> real operational success and territorial seizure
ADMINISTRATIVE GAP -> thin revenue, weak local coalition and divided command
NOBLE PROBLEM -> many begs resist durable residence far from Delhi-Agra
REGIONAL RESPONSE -> Bahadur Shah returns; Askari withdraws; Malwa is lost
LESSON: winning forts is not the same as building a provincial regime.""",
            ["Gujarat campaign", "Mandu", "Champaner", "Askari"],
        ),
        (
            "Sher Khan's Bihar-Bengal scale-up",
            "cause-mechanism-effect",
            """BIHAR BASE -> forts, revenue, Afghan networks and local knowledge
SURAJGARH 1534 -> Bengal checked and Sher Khan's standing enlarged
GAUR 1537-38 -> Bengal resources and strategic depth enter the contest
HUMAYUN AT CHUNAR -> six months spent before the Bengal advance
SHER KHAN MOVES WEST -> route nodes and communications threatened
OUTCOME: a regional Afghan project becomes an imperial alternative.""",
            ["Sher Khan", "Bihar", "Surajgarh", "Gaur"],
        ),
        (
            "Chunar-Gaur communications trap",
            "process",
            """AGRA-DELHI CORE -> eastern movement depends on a long communication line
CHUNAR -> gateway fort affects land-river movement, supply and rear security
GAUR -> symbolic Bengal occupation but no durable administrative bridge
MONSOON + DISTANCE + NOBLE STRAIN -> Mughal position becomes brittle
SHER KHAN -> controls crossings and pressures the route back west
FORMULA: ambition + delayed logistics + severed communications = isolation.""",
            ["Chunar", "Gaur", "Logistics", "Communications"],
        ),
        (
            "Chausa and Kannauj: do not collapse the battles",
            "comparison-matrix",
            """CHAUSA, 26 JUN 1539 -> river at Humayun's rear + surprise + near escape
EFFECT -> army shattered, confidence falls, but the contest is not yet closed
KANNAUJ, 17 MAY 1540 -> set battle against a stronger Afghan position
MUGHAL LIMIT -> hastily assembled force lacks Kamran's hardened troops
EFFECT -> Humayun loses north India and Sher Shah's sovereignty opens
TRAP: Chausa weakens; Kannauj decides the first-reign struggle.""",
            ["Chausa", "Kannauj", "Battle distinction"],
        ),
        (
            "Exile, Safavid bargain and restoration",
            "process",
            """1540 DEFEAT -> Sindh and a prolonged search for a viable base
SHAH TAHMASP -> assistance is strategic and politically conditioned
1545 -> Qandahar and Kabul recovery rebuilds a north-western platform
SUR FIELD -> succession conflict and fragmentation after Islam Shah
1555 -> Delhi-Agra recovered through restored capacity and opponent weakness
LIMIT: restoration proves resilience, not that the earlier collapse was trivial.""",
            ["Exile", "Shah Tahmasp", "Qandahar", "1555 restoration"],
        ),
        (
            "Evidence, rehabilitation and heritage",
            "evidence-matrix",
            """NIZAMUDDIN AHMAD -> alternate chronology; compression and omissions
ABUL FAZL -> fuller reconstruction; later dynastic framing
MIRZA HAIDER -> critical testimony; one voice cannot explain a reign
KARNAVATI TRADITION -> later memory requiring corroboration
HUMAYUN'S TOMB -> later Akbar-era dynastic memory and conservation evidence
METHOD -> replace caricature with ranked evidence, agency and qualification.""",
            ["Source criticism", "Historiography", "Humayun's Tomb", "UNESCO"],
        ),
        (
            "Topic 13 answer spine",
            "answer-synthesis",
            """OPEN -> Babur left a prestigious but unfinished conquest
STRUCTURE -> finance + brothers + unrooted nobles + competing regional powers
AGENCY -> Gujarat overreach, Bengal logistics and Sher Khan's superior timing
BATTLES -> Chausa operational shock; Kannauj decisive political displacement
RECOVERY -> Safavid-backed base + Sur fragmentation + 1555 return
CLOSE -> Humayun failed seriously, but not through a one-word moral defect.""",
            ["Answer architecture", "Structure and agency", "Qualified verdict"],
        ),
    ],
    "medieval-indian-history-14": [
        (
            "From Farid to Sher Shah",
            "process",
            """FARID -> practical exposure in family parganas around Sasaram
BIHAR POLITICS -> service, alliances, revenue knowledge and fort strategy
SHER KHAN -> enlarges an Afghan regional base after Panipat
SURAJGARH / GAUR -> Bengal resources and corridor depth
CHAUSA 1539 + KANNAUJ 1540 -> Mughal displacement and Sur sovereignty
VERDICT: administrative experience and opportunity precede imperial scale.""",
            ["Farid", "Sher Khan", "Sasaram", "Bihar"],
        ),
        (
            "Sur chronology c.1510-1555",
            "timeline",
            """c.1510 -> Farid gains pargana-level experience
1534 -> Surajgarh | 1537 -> Gaur captured by Sher Khan's side
1539 -> Chausa | 1540 -> Kannauj and formal sovereignty
1542 -> Malwa | 1543-44 -> Multan, upper Sindh and Rajasthan fields
1544 -> Samel | May 1545 -> death during Kalinjar siege
1545-53 -> Islam Shah | 1555 -> Humayun returns after fragmentation.""",
            ["Chronology", "Surajgarh", "Samel", "Kalinjar", "Islam Shah"],
        ),
        (
            "Bihar-Bengal scale-up to sovereignty",
            "cause-mechanism-effect",
            """LOCAL BASE -> land knowledge + Afghan followers + forts + revenue
BENGAL CONTEST -> Surajgarh and Gaur enlarge resources and reputation
ROUTE CONTROL -> Gangetic communications expose Humayun's eastern campaign
MILITARY VICTORY -> Chausa and Kannauj redistribute forts and elite loyalty
POLITICAL TASK -> battlefield success must become collection and enforcement
OUTCOME: Sher Khan becomes Sher Shah by converting scale into sovereignty.""",
            ["Bihar", "Bengal", "Route control", "Sovereignty"],
        ),
        (
            "Empire and campaign fields",
            "spatial-map",
            """BENGAL TO INDUS -> useful claim for the broad reach of the Sur realm
KASHMIR -> explicitly excluded from the standard extent formula
MALWA 1542 -> western-central expansion
MULTAN / UPPER SINDH -> north-western campaign and corridor field
RAJASTHAN / SAMEL -> coercion, negotiation and uneven control
RULE: map corridors, forts and campaigns; do not draw a modern solid border.""",
            ["Empire extent", "Malwa", "Multan", "Samel"],
        ),
        (
            "Afghan monarchy and personal supervision",
            "argument-tree",
            """AFGHAN NOBLES -> expectations of dignity, counsel and assignments
SHER SHAH -> forceful monarchy, direct scrutiny and rapid decision
STRENGTH -> coordination can be concentrated under a masterful sovereign
LIMIT -> jagir/iqta expectations and coalition politics do not disappear
SUCCESSION -> Islam Shah asserts monarchy but deepens noble resentment
FRAGILITY -> high personal capacity is difficult to reproduce after the ruler.""",
            ["Afghan nobility", "Personal despotism", "Islam Shah"],
        ),
        (
            "Territory and mediated countryside",
            "hierarchy",
            """SOVEREIGN CENTRE
 -> SARKAR / SHIQ: territorial command and overlapping officials
 -> PARGANA: assessment, records, policing and local information
 -> VILLAGE: cultivators, muqaddams and other intermediaries
ZAMINDARS -> controlled, punished or negotiated with; not abolished
TRAP: this was neither Akbar's mature suba system nor modern ryotwari.""",
            ["Sarkar", "Shiq", "Pargana", "Zamindar", "Muqaddam"],
        ),
        (
            "Revenue measurement and record chain",
            "process",
            """SOWN LAND -> measurement
 -> good / middling / bad classification
 -> average yield and crop-rate schedule (rai)
 -> general one-third state demand
 -> patta records area, crop and amount due
QUALIFY -> cash/kind, local mediation, annual practice and Multan exception.""",
            ["Measurement", "Rai", "Patta", "One-third", "Multan"],
        ),
        (
            "Road-sarai-customs-dak circulation system",
            "systems-map",
            """ROADS -> old imperial corridors restored and improved
FOUR-ROAD FRAME -> Indus-Sonargaon; Agra-Rajasthan; Lahore-Multan; Burhanpur
SARAIS -> lodging + markets + relay + surveillance at two-karoh intervals
DAK / NEWS -> information and orders move through nodal stations
CUSTOMS -> duties simplified around entry and sale
RESULT -> commerce, army movement and coercive reach reinforce one another.""",
            ["Roads", "Sarais", "Dak", "Customs", "Two karohs"],
        ),
        (
            "Money, order and military controls",
            "comparison-matrix",
            """RUPEE -> fine silver standard with durable later influence, not first coin
TRIMETALLIC FIELD -> gold, silver and copper support exchange and payments
LAW AND ORDER -> merchant safety backed by harsh collective responsibility
CHEHRA -> descriptive roll of soldiers | DAGH -> branding of horses
CONTINUITY -> Alauddin precedent; Sher Shah revival; Akbar systematisation
RULE: administrative effectiveness is not the same as modern legality.""",
            ["Silver rupee", "Law and order", "Chehra", "Dagh"],
        ),
        (
            "Forts, religion and succession limits",
            "evidence-matrix",
            """ROHTAS, NORTHWEST -> frontier control and Mughal-return check
ROHTASGARH, BIHAR -> distinct site; never conflate the two forts
RAISEN / PURAN MAL -> violence with political and religious readings
KALINJAR 1545 -> siege death ends Sher Shah's personal direction
ISLAM SHAH -> continuity plus sharper conflict with Afghan nobles
SUR COLLAPSE -> succession and faction reopen the field to Humayun.""",
            ["Rohtas", "Rohtasgarh", "Puran Mal", "Kalinjar", "Succession"],
        ),
        (
            "Continuity, source method and Akbar",
            "comparison-matrix",
            """SULTANATE -> measurement, assignments, dagh-chehra and road precedents
SUR -> practical revival, standardisation and fast integrated implementation
AKBAR -> wider scale, longer duration, mansabdari and refined revenue systems
SARWANI -> valuable retrospective Afghan memory; praise needs corroboration
SASARAM TOMB -> material evidence for patronage and legitimacy, not every reform
VERDICT: Sher Shah was a bridge and systematiser, not Akbar's full blueprint.""",
            ["Continuity", "Akbar", "Sarwani", "Sasaram tomb"],
        ),
        (
            "Topic 14 answer spine",
            "answer-synthesis",
            """OPEN -> short reign, dense state-building and a longer Sur phase
RISE -> pargana experience + Bihar-Bengal base + Mughal displacement
CAPACITY -> revenue + money + roads + information + order + military controls
MEDIATION -> zamindars and local officials remain inside the system
LIMITS -> uneven reach, harsh coercion, personal supervision and succession
CLOSE -> achievement lay in integration and execution within a longer process.""",
            ["Answer architecture", "State capacity", "Qualified synthesis"],
        ),
    ],
}


def remove_embedded_cover(fragment: str) -> str:
    return re.sub(
        r"(?ms)\n*!\[[^\n]*\]\([^)\n]*00_cover\.png\)\s*",
        "\n",
        fragment,
        count=1,
    ).strip()


def compact_topic_13_practice(fragment: str) -> str:
    fragment = fragment.replace(
        "The correct forward link is that Akbar would consolidate on a restored "
        "foundation; it is not that all later Mughal capacities existed in 1555.",
        "Akbar consolidated a restored foundation; later Mughal capacities did "
        "not already exist in 1555.",
    )
    return re.sub(
        r"\*\*Why this earns marks:\*\* It makes restoration causal.*?Akbar\.",
        "**Why this earns marks:** It treats restoration causally, bounds "
        "heritage evidence and transitions to Akbar.",
        fragment,
        count=1,
        flags=re.DOTALL,
    )


def deduplicate_topic_14_drills(fragment: str) -> str:
    parts = re.split(r"(?m)^###\s+", fragment)
    if len(parts) == 1:
        return fragment
    kept = [parts[0]]
    drill_bodies: dict[str, str] = {}
    for part in parts[1:]:
        title = part.splitlines()[0].strip()
        category = next(
            (
                prefix
                for prefix in ("Evidence clinic", "Comparison drill", "Source drill")
                if title.startswith(prefix)
            ),
            None,
        )
        if category is not None:
            if category not in drill_bodies:
                body = "\n".join(part.splitlines()[1:]).strip()
                drill_bodies[category] = body
            continue
        kept.append("### " + part)
    labels = ("Evidence clinic", "Comparison drill", "Source drill")
    compact_drills = [
        "### Evidence, comparison and source drills",
        "",
    ]
    for number, label in enumerate(labels, 1):
        compact_drills.append(f"{number}. **{label}.** {drill_bodies[label]}")
    return ("".join(kept).rstrip() + "\n\n" + "\n".join(compact_drills)).strip()


def assemble_topic_13(config_value: dict[str, object]) -> str:
    source = previous.strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    preamble, sections = BASE.split_h2(source)
    preamble = BASE.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    for title, fragment in sections:
        metadata = title.startswith("Package provenance")
        numbered = bool(re.match(r"^\d{2}\.", title))
        if metadata or numbered or title.startswith("Visual atlas"):
            bucket = "basic"
            if metadata:
                fragment = remove_embedded_cover(fragment)
        elif title.startswith(("PART II.", "PART IV.", "PART V.")):
            bucket = "mcq"
            fragment = previous.normalize_mcq_fragment(fragment)
        elif title.startswith(("PART III.", "PART VI.")):
            bucket = "practice"
            if title.startswith("PART VI."):
                fragment = compact_topic_13_practice(fragment)
        elif title.startswith("PART VII."):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 13 section: {title}")
        grouped[bucket].append(previous.normalized_fragment(fragment, metadata=metadata))
    return previous.compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble_topic_14(config_value: dict[str, object]) -> str:
    source = previous.strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    preamble, sections = BASE.split_h2(source)
    preamble = BASE.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    for title, fragment in sections:
        metadata = title.startswith("Package provenance")
        numbered = bool(re.match(r"^\d{2}\.", title))
        if metadata or title.startswith("PYQ route audit") or numbered:
            bucket = "basic"
            if metadata:
                fragment = remove_embedded_cover(fragment)
        elif title.startswith(("PART I.", "PART II.", "PART III.")):
            bucket = "mcq"
            fragment = previous.normalize_mcq_fragment(fragment)
        elif title.startswith("PART IV."):
            bucket = "practice"
            fragment = deduplicate_topic_14_drills(fragment)
        elif title.startswith("FINAL CONSOLIDATED"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 14 section: {title}")
        grouped[bucket].append(previous.normalized_fragment(fragment, metadata=metadata))
    return previous.compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-13":
        return assemble_topic_13(config_value)
    return assemble_topic_14(config_value)


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
        "scope": "Medieval Indian History learner-v2 Topics 13-14",
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
    local_books = [Path(path) for path in config_value["local_books"]]
    source_files = [
        Path(config_value["basic"]),
        Path(config_value["advanced"]),
        Path(config_value["canonical"]),
        *[Path(path) for path in config_value["extra_markdown"]],
        source_path,
        *[ROOT / item for item in BASE_GENERATOR.COMMON_CROSS],
        *[ROOT / item for item in BASE_GENERATOR.PYQ_INDEXES],
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
        "official_question_sources": [],
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
