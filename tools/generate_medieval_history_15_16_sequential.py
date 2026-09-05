"""Assemble Medieval History learner-v2 Topics 15-16 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_13_14_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-15-16-2026-08-30-sequential.json"
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
HELPERS = previous.previous


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
    )


TOPICS = [
    topic_config(
        15,
        "Akbar: Consolidation & Expansion of the Empire",
        "15_Akbar-Consolidation-Expansion_Complete-Topic-Package.md",
        "15_Akbar-Consolidation-and-Expansion.md",
        "15_Akbar-Consolidation-and-Expansion.md",
        "15_Akbar-Consolidation-Expansion_Complete-Learning-Session_2026-08-18.pdf",
        "15_Akbar-Consolidation-Expansion_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 remedial "
        "MCQs; 10 original solved Mains questions plus evidence workshops.",
        ["https://whc.unesco.org/en/list/255/"],
        "UNESCO's Fatehpur Sikri property page was rechecked on 30 August "
        "2026. It supports a bounded material-history bridge: Akbar made the "
        "planned city his capital, its administrative, residential and "
        "religious buildings express an imperial centre, and the Buland "
        "Darwaza commemorates the Gujarat victory. The modern property record "
        "does not independently prove campaign motives, court consensus or "
        "the effectiveness of Akbar's political integration; those remain "
        "controlled by repository Markdown, OCR books and source criticism.",
        "Akbar consolidation expansion and political integration cover",
        "notes/Medieval-Indian-History/assets/"
        "15_Akbar-Consolidation-Expansion/01_cover.png",
        [
            "learning-sessions\\15_Akbar-Consolidation-Expansion_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\15_Akbar-Consolidation-Expansion_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
    ),
    topic_config(
        16,
        "State & Government under Akbar (Mansabdari, Dahsala)",
        "16_State-Government-under-Akbar_Complete-Topic-Package.md",
        "16_State-and-Government-under-Akbar.md",
        "16_State-and-Government-under-Akbar.md",
        "16_State-Government-under-Akbar_Complete-Learning-Session_2026-08-18.pdf",
        "16_State-Government-under-Akbar_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "1 routed Prelims hierarchy demand; 20 learning, 44 broad and 16 "
        "remedial MCQs; 10 original solved Mains questions.",
        ["https://dolr.gov.in/en/programmes-schemes/dilrmp-2/"],
        "The Department of Land Resources' DILRMP page was rechecked on "
        "30 August 2026. It supports only a bounded administrative analogy: "
        "modern land-record management emphasises accurate updated records, "
        "public access, integration and adaptation to diverse state contexts. "
        "It must not be equated with Mughal assessment, proprietary title or "
        "peasant-state relations; Akbar's zabt, dahsala and local mediation "
        "remain controlled by repository Markdown, OCR books and historical "
        "source criticism.",
        "Akbar government mansabdari revenue and dahsala cover",
        "notes/Medieval-Indian-History/assets/"
        "16_State-Government-under-Akbar/01_01_cover.png",
        [
            "learning-sessions\\16_State-Government-under-Akbar_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\16_State-Government-under-Akbar_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-15": [
        (
            "Consolidation before durable expansion",
            "argument-tree",
            """1555 RESTORATION -> Mughal foothold, not a settled empire
1556 CRISIS -> Hemu, Sikandar Sur, Afghan strength and Kabul uncertainty
REGENCY -> Bairam Khan stabilises command during Akbar's minority
PERSONAL RULE -> household and noble alternatives are disciplined
EXPANSION -> campaigns are joined to alliances, ranks, jagirs and retention
VERDICT: durability came from reconquest + elite integration + institutions.""",
            ["Consolidation", "State building", "Elite integration"],
        ),
        (
            "Akbar chronology 1542-1605",
            "timeline",
            """1542 Amarkot -> 1556 Kalanaur and Second Panipat
1556-60 -> Bairam Khan regency | 1562 -> Adham Khan crisis
1567 -> Uzbek challenge broken | 1568 -> Chittor
1572-73 -> Gujarat conquest and rapid return
1576 -> Daud Khan defeated; Haldighati
1580-81 -> eastern rebellion and Mirza Hakim | 1605 -> Akbar dies.""",
            ["Chronology", "Panipat II", "Chittor", "Gujarat", "Haldighati"],
        ),
        (
            "The fractured field of 1556",
            "network-map",
            """AKBAR / BAIRAM -> fragile restored centre and young sovereign
HEMU -> Adil Shah's commander with Afghan army, elephants and artillery
SIKANDAR SUR -> continuing Afghan territorial alternative
KABUL / MIRZA FIELD -> north-western dynastic and communications risk
PANIPAT II -> Hemu's wound disrupts command; Mughal victory remains contingent
TRAP: the battle reopens consolidation; it does not end every rival at once.""",
            ["Hemu", "Sikandar Sur", "Second Panipat", "Contingency"],
        ),
        (
            "Bairam Khan to personal rule",
            "process",
            """1556-60 REGENCY -> wakil mutlaq rallies nobles and secures the regime
TENSION -> delegated power, court factions and Akbar's growing autonomy
DISMISSAL -> Bairam resists, submits, is pardoned and leaves for pilgrimage
HOUSEHOLD FIELD -> Maham Anaga, Adham Khan and access to the young ruler
ATKA KHAN MURDER -> Adham's execution re-centres sovereign authority
LESSON: regency enabled survival but could not become permanent kingship.""",
            ["Bairam Khan", "Wakil mutlaq", "Adham Khan", "Personal rule"],
        ),
        (
            "Noble and Uzbek challenge",
            "cause-mechanism-effect",
            """OLD NOBLES -> commands and jagirs create bases for bargaining
UZBEK REBELLION -> Khan-i-Zaman and allies resist centralising control
AKBAR -> manoeuvre, pardon, transfer and force divide the opposition
JUNE 1567 -> Khan-i-Zaman defeated; major internal alternative broken
EFFECT -> mobilisation and reward become more credible for distant campaigns
QUALIFY: central security enabled expansion but did not abolish faction.""",
            ["Uzbek rebellion", "Khan-i-Zaman", "Noble control"],
        ),
        (
            "Malwa and Garh-Katanga: coercive limits",
            "comparison-matrix",
            """MALWA -> Baz Bahadur defeated; Adham corrected; Baz later enters Mughal service
GARH-KATANGA -> Rani Durgavati resists; conquest brings death and plunder
IMPERIAL VIEW -> expansion and agent discipline | REGIONAL VIEW -> agency and resources
TRAP: integration joined selective accommodation to severe coercion.""",
            ["Malwa", "Baz Bahadur", "Rani Durgavati", "Garh-Katanga"],
        ),
        (
            "Rajput policy in phases",
            "process",
            """EARLY ALLIES -> Amber before Chittor; service through mansabs, office and watan
GUJARAT PHASE -> Rajputs become an imperial arm; after 1578 partnership deepens
SURJAN HADA -> service without marriage disproves a marriage-only explanation
LIMIT -> honour and patronage sustained an unequal political alliance.""",
            ["Rajput policy", "Amber", "Watan jagir", "Surjan Hada"],
        ),
        (
            "Chittor, Ranthambhor and the Mewar exception",
            "spatial-map",
            """RAJASTHAN -> flank security and routes toward Malwa and Gujarat
CHITTOR -> strategic fort, symbolic resistance and massacre | RANTHAMBHOR -> settlement
MOST RAJAS -> honour, office and local status | MEWAR -> submission remains unresolved
RULE: force backed settlement; settlement did not erase refusal or violence.""",
            ["Chittor", "Ranthambhor", "Mewar", "Rajput settlement"],
        ),
        (
            "Gujarat and Bengal: conquest plus retention",
            "comparison-matrix",
            """GUJARAT -> ports and maritime access; 1572-73 conquest followed by rapid return
HUMAYUN CONTRAST -> local command and retention are treated more deliberately
BIHAR-BENGAL -> Afghan resistance and river logistics; Daud Khan defeated in 1576
LIMIT -> Bengal needs continuing attention; conquest is not instant pacification.""",
            ["Gujarat", "Rapid march", "Bengal", "Daud Khan"],
        ),
        (
            "Haldighati: coalition and outcome",
            "evidence-matrix",
            """MUGHAL -> Man Singh's mixed force | MEWAR -> Rajputs, Bhils and Hakim Khan's Afghans
BATTLE 1576 -> political struggle over submission and regional autonomy
OUTCOME -> tactical Mughal advantage; Rana Pratap continues resistance and recovery
TRAP: mixed coalitions defeat a Hindu-versus-Muslim framing.""",
            ["Haldighati", "Man Singh", "Rana Pratap", "Hakim Khan Sur"],
        ),
        (
            "Rebellion, frontier and source method",
            "systems-map",
            """1580-81 REBELLION + MIRZA HAKIM -> fiscal, noble, Kabul and Punjab pressures
AKBAR -> mobility, loyal commanders and a broader elite contain the crisis
ABUL FAZL -> imperial narrative | BADAUNI / BARDIC MEMORY -> dissent and honour limits
FATEHPUR SIKRI -> material imperial centre, not proof of every policy outcome.""",
            ["1580-81 rebellion", "Mirza Hakim", "Abul Fazl", "Fatehpur Sikri"],
        ),
        (
            "Topic 15 answer spine",
            "answer-synthesis",
            """OPEN -> Akbar inherited a restored but fractured political field
RECONQUEST -> Panipat II + continuing Afghan and frontier containment
CENTRE -> regency transition + household discipline + Uzbek defeat
EXPANSION -> Malwa, Rajasthan, Gujarat and Bengal with varied mechanisms
INTEGRATION -> Rajput alliance and composite service widen the loyalty base
CLOSE -> durable empire joined coercion, accommodation, mobility and retention.""",
            ["Answer architecture", "Coercion and accommodation", "Durability"],
        ),
    ],
    "medieval-indian-history-16": [
        (
            "State capacity as an integrated architecture",
            "systems-map",
            """RULER-CENTRED AUTHORITY -> appointment, transfer, promotion and judgement
OFFICES -> differentiated finance, military, household and grant functions
MANSABDARI -> ranks elite status, remuneration and service obligation
REVENUE -> measurement, averages, records and local mediation fund the state
VERIFICATION -> dagh, chehra, accounts and news test paper claims
VERDICT: substantial capacity remained personal, hierarchical and uneven.""",
            ["State capacity", "Ruler-centred checks", "Information"],
        ),
        (
            "Administrative evolution 1556-1605",
            "timeline",
            """1556 -> Bairam Khan as powerful wakil during minority
1565 -> Muzaffar Khan Turbati strengthens the diwan's fiscal role
1567 -> numerical mansab hierarchy associated with the 11th regnal year
1573-74 -> dagh introduced | 1575 -> Todar Mal as mushrif-i-diwan
1580 -> dahsala and twelve subas
1595-96 -> zat-sawar distinction in the 40th regnal year.""",
            ["Chronology", "Muzaffar Khan", "Todar Mal", "Mansab evolution"],
        ),
        (
            "Central offices and ruler-centred checks",
            "hierarchy",
            """EMPEROR -> final authority and coordinator
WAKIL -> prestige retained; over-mighty regency power reduced
DIWAN -> income, expenditure, khalisa, jagir, inam and fiscal audit
MIR BAKHSHI -> mansab presentation, musters, personnel and intelligence
MIR SAMAN -> household, stores and karkhanas | SADR-QAZI -> grants and justice
RULE: differentiated functions checked concentration, not the monarch.""",
            ["Wakil", "Diwan", "Mir bakhshi", "Mir saman", "Sadr-qazi"],
        ),
        (
            "Province to village: hierarchy and counterweights",
            "hierarchy",
            """CENTRE -> appoints provincial officers and receives reports
SUBA -> subadar + separate diwan, bakhshi, sadr-qazi and news channels
SARKAR -> faujdar and fiscal/coercive work; jurisdictions may vary
PARGANA -> amil/amalguzar, qanungo and clerical record structure
VILLAGE -> cultivators, muqaddam/patel, patwari and local custom
TRAP: pargana -> sarkar -> suba, but not a modern federal hierarchy.""",
            ["Suba", "Sarkar", "Pargana", "Village", "Provincial checks"],
        ),
        (
            "Mansabdari: rank, remuneration and obligation",
            "systems-map",
            """MANSAB -> graded imperial rank, not one military headcount
STATUS -> court position and place in the service elite
SALARY -> cash calculation, often met through a transferable jagir
SERVICE -> civil command and cavalry obligation inside one hierarchy
RECRUITMENT -> Turani, Irani, Rajput, Indian Muslim and other elites integrated
LIMIT -> hierarchy creates competition and remains dependent on imperial favour.""",
            ["Mansab", "Composite elite", "Salary", "Service"],
        ),
        (
            "Zat, sawar and jagir logic",
            "comparison-matrix",
            """ZAT -> personal status and salary dimension
SAWAR -> cavalry obligation; introduced as a separate late distinction
JAGIR -> assignment of state revenue, not private ownership of land
KHALISA -> revenue reserved for the crown
TRANSFER -> restrains territorial rooting but can encourage short-term extraction
JAMA / HASIL -> paper assessment may exceed actual receipt.""",
            ["Zat", "Sawar", "Jagir", "Khalisa", "Jama-hasil"],
        ),
        (
            "Dagh, chehra and the verification problem",
            "process",
            """SANCTIONED CONTINGENT -> a mansabdar claims horses and personnel
CHEHRA -> descriptive roll records the soldier
DAGH -> branding identifies the inspected horse
MUSTER -> officials compare paper obligation with actual resources
INFORMATION -> mir bakhshi and news channels support oversight
QUALIFY -> Alauddin precedent, Sher Shah revival, Akbar systematisation.""",
            ["Dagh", "Chehra", "Muster", "Mir bakhshi"],
        ),
        (
            "Revenue reform as experiment",
            "timeline",
            """SHER SHAH PRECEDENT -> measurement and crop-rate practices
EARLY AKBAR -> central price schedule creates delay and local-price distortion
1573 ONWARD -> closer imperial attention after Gujarat
TEAM -> Muzaffar Khan, Todar Mal, Shah Mansur and record officials
1580 DAHSALA -> ten-year produce and price averages structure demand
RULE: reform evolved through correction; it was not a first-day blueprint.""",
            ["Revenue experiments", "Price problem", "Dahsala team"],
        ),
        (
            "Zabt-dahsala calculation chain",
            "process",
            """JARIB -> bamboo linked by iron rings standardises measurement
LAND -> polaj, parati, chachar and banjar track cultivation history
PRODUCE -> ten-year average | PRICES -> ten-year local average
DEMAND -> generally one-third of average produce, converted into cash
PATTA / RECORD -> assessed liability becomes legible
TRAP: ten-year data window is not a permanent ten-year settlement.""",
            ["Jarib", "Land categories", "Dahsala", "One-third"],
        ),
        (
            "Methods, geography and mediation",
            "comparison-matrix",
            """ZABT -> measurement-based assessment in suitable record-rich zones
BATAI -> crop divided in an agreed proportion
KANKUT -> measurement combined with standing-crop appraisal
NASAQ -> estimate relying substantially on previous demand or payment
ZAMINDAR / LOCAL STAFF -> information, bargaining and collection remain necessary
LIMIT -> no method covered every field, crop, terrain or province uniformly.""",
            ["Zabt", "Batai", "Kankut", "Nasaq", "Zamindar"],
        ),
        (
            "Continuity, evidence and structural limits",
            "evidence-matrix",
            """SULTANATE / SUR -> assignments, measurement and verification precedents
AKBAR -> coordination at larger scale and over longer duration
AIN-I-AKBARI -> normative detail and imperial knowledge; not every local outcome
DILRMP ANALOGY -> records matter, but modern title systems are not Mughal zabt
LIMITS -> jagir incentives, uneven hasil, evasion, coercion and local bargaining
VERDICT: refinement and integration mattered more than invention from zero.""",
            ["Continuity", "Ain-i-Akbari", "DILRMP", "Structural limits"],
        ),
        (
            "Topic 16 answer spine",
            "answer-synthesis",
            """OPEN -> Akbar coordinated inherited devices into a larger imperial system
CENTRE -> differentiated offices under final ruler-centred authority
ELITE -> mansab + zat/sawar + jagir + verification
FISCAL -> measurement + averages + alternative methods + local mediation
CHECKS -> reports and parallel officers constrain but do not constitutionalise power
CLOSE -> rational capacity increased without becoming uniform or modern.""",
            ["Answer architecture", "Administrative synthesis", "Qualified verdict"],
        ),
    ],
}


def remove_embedded_cover(fragment: str) -> str:
    return re.sub(
        r"(?ms)\n*!\[[^\n]*\]\([^)\n]*(?:01_cover|01_01_cover)\.png\)\s*",
        "\n",
        fragment,
        count=1,
    ).strip()


def normalize_mcq_fragment(fragment: str) -> str:
    text = HELPERS.normalize_mcq_fragment(fragment)
    return re.sub(
        r"(?mi)^\*\*Answer:\s*([A-D])"
        r"(?:\s*[—–-]\s*.*?)?\*\*\s*$",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        text,
    )


def assemble_topic_15(config_value: dict[str, object]) -> str:
    source = HELPERS.strip_frontmatter(
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
        basic_numbered = bool(re.match(r"^Part (?:[1-9]|1[0-4]):", title))
        if title.startswith("Orientation") or title.startswith("Learning map") or basic_numbered:
            bucket = "basic"
            if title.startswith("Learning map"):
                fragment = remove_embedded_cover(fragment)
        elif title.startswith(("Part 15:", "Part 16:", "Part 17:")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Part 18:"):
            bucket = "practice"
        elif title.startswith("Part 19:"):
            bucket = "advanced"
        elif title.startswith("Final consolidated"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 15 section: {title}")
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble_topic_16(config_value: dict[str, object]) -> str:
    source = HELPERS.strip_frontmatter(
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
        if title.startswith("Roadmap"):
            bucket = "basic"
        elif title.startswith("PART") and "Practice and examiner feedback" not in title:
            bucket = "basic"
        elif title.startswith("PART") and "Practice and examiner feedback" in title:
            continue
        elif title.startswith(("Learning MCQ", "Broad practice", "Remedial MCQs")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Examiner-grade solved Mains practice"):
            bucket = "practice"
        elif title.startswith("FINAL CONSOLIDATED"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 16 section: {title}")
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-15":
        return assemble_topic_15(config_value)
    return assemble_topic_16(config_value)


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
        "scope": "Medieval Indian History learner-v2 Topics 15-16",
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
