"""Assemble Medieval History learner-v2 Topics 09-10 and visual specs."""

from __future__ import annotations

import json
import re
from pathlib import Path

import generate_medieval_history_07_08_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-09-10-2026-08-30-sequential.json"
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
    value["local_books"] = [SATISH_HISTORY, SATISH_SULTANAT]
    return value


TOPICS = [
    topic_config(
        9,
        "Vijayanagara & the Bahmani Kingdom (Deccan)",
        "09_Vijayanagara-Bahmani-Kingdom_Complete-Topic-Package.md",
        "09_Vijayanagara-and-Bahmani.md",
        "09_Vijayanagara-and-Bahmani.md",
        "09_Vijayanagara-Bahmani-Kingdom_Complete-Learning-Session_2026-08-16.pdf",
        "09_Vijayanagara-Bahmani-Kingdom_Premium-Solved-PYQ-Workbook_2026-08-16.pdf",
        "3 locally routed Prelims PYQs; 16 learning, 40 broad and 12 remedial "
        "MCQs; 8 original solved Mains questions.",
        ["https://whc.unesco.org/en/list/241/"],
        "UNESCO's Group of Monuments at Hampi property page was rechecked on "
        "30 August 2026. It supports a bounded material-history bridge: the "
        "Tungabhadra setting, more than 1,600 surviving remains, integrated "
        "royal, sacred, market, defensive and hydraulic systems, and the "
        "destruction of the capital's physical fabric after Talikota. It does "
        "not independently prove every traveller claim, dynastic narrative "
        "or estimate of prosperity, and its conservation language must not "
        "be projected backwards as a medieval administrative record.",
        "Vijayanagara and Bahmani Deccan political field cover",
        "notes/Medieval-Indian-History/assets/"
        "09_Vijayanagara-Bahmani-Kingdom/00_cover.png",
        [
            "learning-sessions\\09_Vijayanagara-Bahmani-Kingdom_Complete-Learning-Session_2026-08-16.md",
            "learning-sessions\\09_Vijayanagara-Bahmani-Kingdom_Premium-Solved-PYQ-Workbook_2026-08-16.md",
        ],
    ),
    topic_config(
        10,
        "The Bhakti & Sufi Movements",
        "10_Bhakti-Sufi-Movements_Complete-Topic-Package.md",
        "10_Bhakti-and-Sufi-Movements.md",
        "10_Bhakti-and-Sufi-Movements.md",
        "10_Bhakti-Sufi-Movements_Complete-Learning-Session_2026-08-17.pdf",
        "10_Bhakti-Sufi-Movements_Premium-Solved-PYQ-Workbook_2026-08-17.pdf",
        "4 routed Prelims and Mains PYQs; 16 learning, 40 broad and 12 "
        "remedial MCQs; 8 original solved Mains questions.",
        ["https://pib.gov.in/PressReleasePage.aspx?PRID=2135542"],
        "The Press Information Bureau's 11 June 2025 Kabir Jayanti tribute "
        "was rechecked through the official indexed release on 30 August "
        "2026. It is used only as a bounded public-memory bridge to Kabir's "
        "continuing association with social harmony, reform and accessible "
        "verse. A modern commemorative statement cannot prove the wording, "
        "chronology, authorship or medieval reception of the Kabir corpus; "
        "those claims remain controlled by repository sources, OCR books and "
        "source criticism.",
        "Bhakti and Sufi plural devotional field cover",
        "notes/Medieval-Indian-History/assets/"
        "10_Bhakti-Sufi-Movements/00_cover.png",
        [
            "learning-sessions\\10_Bhakti-Sufi-Movements_Complete-Learning-Session_2026-08-17.md",
            "learning-sessions\\10_Bhakti-Sufi-Movements_Premium-Solved-PYQ-Workbook_2026-08-17.md",
        ],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-09": [
        (
            "Deccan political chronology",
            "timeline",
            """c. 1336 -> conventional Vijayanagara foundation anchor
1347 -> Bahmani kingdom established under Alauddin Hasan Bahman Shah
1420s-40s -> Deva Raya II strengthens Vijayanagara military adaptation
1425 -> Bahmani capital shifts from Gulbarga to Bidar
1509-29 -> Krishnadeva Raya and Tuluva apogee
1565 -> Talikota destroys the capital fabric; Aravidu power continues.""",
            ["Chronology", "Dynastic transitions"],
        ),
        (
            "Three contested zones",
            "spatial-map",
            """TUNGABHADRA DOAB -> fertile frontier, forts and recurring campaigns
KRISHNA-GODAVARI -> agrarian basin, routes and eastern-coast connections
KONKAN-GOA -> ports, customs, horse imports and western maritime access
                    |
          REVENUE + CAVALRY + LOGISTICS + PRESTIGE
RULE: political geography explains more than a Hindu-Muslim binary.""",
            ["Tungabhadra doab", "Krishna-Godavari", "Konkan-Goa"],
        ),
        (
            "Foundation and evidence ladder",
            "evidence-matrix",
            """INSCRIPTIONS -> rulers, grants and dated claims | selective formulae
ARCHAEOLOGY -> settlement, water and buildings | cannot recover every motive
TRAVELLERS -> observed city and court | perspective, genre and exaggeration
LATER TRADITIONS -> remembered origins | chronology and political use require care
SAFE OPENING -> c. 1336 is conventional; founder biographies remain debated.""",
            ["Harihara", "Bukka", "Source criticism"],
        ),
        (
            "Vijayanagara dynastic sequence",
            "timeline",
            """SANGAMA -> early consolidation and Deccan rivalry
       |
SALUVA -> military intervention amid succession pressure
       |
TULUVA -> Krishnadeva Raya, campaigns and cultural patronage
       |
ARAVIDU -> continuation after the 1565 capital catastrophe
LESSON: dynastic replacement did not automatically erase the state.""",
            ["Sangama", "Saluva", "Tuluva", "Aravidu"],
        ),
        (
            "Water, capital and agrarian capacity",
            "cause-mechanism-effect",
            """TUNGABHADRA LANDSCAPE + TANKS + CANALS
                    |
cultivation + urban supply + ritual water + military provisioning
                    |
taxable surplus + metropolitan density + resilience
                    |
STATE CAPACITY, but benefits and control remained socially unequal
UNESCO bridge: hydraulic remains support integration, not a welfare census.""",
            ["Irrigation", "Hampi", "UNESCO"],
        ),
        (
            "Amaram and nayaka bargain",
            "process",
            """RULER ASSIGNS REVENUE CLAIM / TERRITORIAL COMMAND
                    |
NAYAKA maintains troops, remits obligations and governs locally
                    |
service produces military reach but also entrenches regional power
                    |
weak centre -> hereditary drift, bargaining and later nayaka polities
CAUTION: comparison with iqta is functional, not an equation.""",
            ["Amaram", "Nayaka", "Military-fiscal system"],
        ),
        (
            "Horse-port-military chain",
            "network-map",
            """WEST ASIAN HORSE SUPPLY -> PORTS / MERCHANTS / CUSTOMS
                              |
GOA / BHATKAL / KONKAN ROUTES -> inland movement and payment
                              |
cavalry recruitment + archery + commanders + fodder and remounts
                              |
competitive adaptation by Vijayanagara and Deccan states
RULE: imported horses mattered, but did not alone decide wars.""",
            ["Horse trade", "Bhatkal", "Portuguese relations"],
        ),
        (
            "Hampi urban system",
            "layered-governance",
            """LANDSCAPE -> river, boulders, plains and defended approaches
SACRED -> temples, processions, tanks and continuing ritual
ROYAL -> enclosures, audience spaces, stables and elite display
COMMERCIAL -> bazaars, craft production and suburban settlements
HYDRAULIC -> channels, wells, tanks and agricultural support
VERDICT: capital, market, ritual and ecology formed one system.""",
            ["Hampi", "Urbanism", "UNESCO"],
        ),
        (
            "Bahmani state and capital shift",
            "timeline",
            """1347 GULBARGA -> foundation, frontier command and early consolidation
       |
1425 BIDAR -> revised strategic centre and courtly-cultural investment
       |
TARAFS -> provincial command, revenue and military resources
       |
late 15th c. -> stronger factions and successor-state formation
TRAP: capital shift is not the same event as dynastic foundation.""",
            ["Bahmani", "Gulbarga", "Bidar", "Taraf"],
        ),
        (
            "Mahmud Gawan reform logic",
            "cause-mechanism-effect",
            """LARGE TARAFLANDS + POWERFUL GOVERNORS + ELITE RIVALRY
                    |
more provinces + forts under tighter control + khalisa enlargement
                    |
measurement, cash expectations and central checks
                    |
greater intended control -> factional resistance -> Gawan's execution
LESSON: sound design can fail without a durable governing coalition.""",
            ["Mahmud Gawan", "Khalisa", "Centralisation"],
        ),
        (
            "Deccani-Afaqi coalition problem",
            "comparison-matrix",
            """DECCANIS -> longer-settled regional Muslim elites and allies
AFAQIS -> newer western and Central Asian migrants and networks
COMPETITION -> office, patronage, military command and court access
CROSS-CUTTING TIES -> marriage, language, service and local alliance
OUTCOME -> factional labels structure politics but are not racial absolutes
TRAP: do not turn elite rivalry into a timeless communal conflict.""",
            ["Deccanis", "Afaqis", "Elite factions"],
        ),
        (
            "Topic 09 answer spine",
            "answer-synthesis",
            """OPEN -> connected Deccan field organised by resources and routes
VIJAYANAGARA -> water + capital + amaram + cavalry + maritime diplomacy
BAHMANI -> capitals + tarafs + Gawan reform + factional coalition
EVIDENCE -> inscriptions + archaeology + travellers + monuments
TURNING POINT -> 1565 destroys Hampi fabric, not every political network
CLOSE -> rivalry and exchange jointly shaped later Deccan formations.""",
            ["Comparison", "Talikota", "Answer architecture"],
        ),
    ],
    "medieval-indian-history-10": [
        (
            "Plural devotional chronology",
            "timeline",
            """6th-9th c. -> Alvar and Nayanar devotional corpora in the south
11th-13th c. -> Vedanta schools and early north Indian Sufi networks
13th-14th c. -> Chishti and Suhrawardi institutions expand
15th c. -> Kabir, Nanak and regional vernacular devotional currents
late 15th-16th c. -> Chaitanya, Surdas, Meera and wider literary publics
RULE: multiple currents overlap; no single movement starts everywhere.""",
            ["Chronology", "Plurality"],
        ),
        (
            "Bhakti field without flattening",
            "classification",
            """SAGUNA -> devotion through embodied divine forms and narratives
NIRGUNA -> devotion to a formless absolute and critique of fixed representation
TEMPLE / SECT -> ritual, institution, pilgrimage and inherited authority
POET-SAINT / SONG -> oral performance, vernacular memory and community
VEDANTA -> Ramanuja, Madhva, Nimbarka and distinct philosophical grammars
CAUTION: these categories overlap and vary by region and period.""",
            ["Saguna", "Nirguna", "Bhakti diversity"],
        ),
        (
            "Sufi vocabulary and transmission",
            "institution-map",
            """SILSILAH -> authorised chain of spiritual transmission
PIR -> guide | MURID -> disciple | KHALIFA -> authorised successor
KHANQAH -> discipline, teaching, hospitality and social contact
SAMA -> devotional audition, accepted and debated in different settings
ZIYARAT -> shrine visitation and remembered saintly presence
FANA -> effacement of ego before God, not a political programme.""",
            ["Silsilah", "Khanqah", "Sama", "Fana"],
        ),
        (
            "Chishti network and social credibility",
            "network-map",
            """AJMER: Muinuddin Chishti
          |
DELHI: Bakhtiyar Kaki -> Nizamuddin Auliya -> Nasiruddin Chiragh
          |
AJODHAN: Baba Farid and Punjabi memory
MECHANISM -> service + hospitality + counsel + sama + relative court distance
TRAP: popularity does not prove a centrally planned conversion campaign.""",
            ["Chishti", "Ajmer", "Delhi", "Ajodhan"],
        ),
        (
            "Chishti-Suhrawardi comparison",
            "comparison-matrix",
            """CHISHTI                         SUHRAWARDI
Ajmer, Delhi, Ajodhan           Multan and Punjab
poverty/service ideal           readier acceptance of grants
relative distance from office   greater possibility of official connection
khanqah credibility             learned and institutional resources
RULE: neither order was uniform, morally pure or socially identical.""",
            ["Chishti", "Suhrawardi", "Bahauddin Zakariya"],
        ),
        (
            "Southern roots and Vedanta paths",
            "comparison-matrix",
            """ALVARS -> Tamil Vaishnava devotion and hymn traditions
NAYANARS -> Tamil Shaiva devotion and temple-linked memory
RAMANUJA -> qualified non-dualism and prapatti
MADHVA -> dualism and enduring difference between God and soul
NIMBARKA -> difference-and-non-difference formulation
LESSON: Bhakti is emotional devotion plus philosophical articulation.""",
            ["Alvars", "Nayanars", "Ramanuja", "Madhva"],
        ),
        (
            "Northward transmission with source caution",
            "process",
            """SOUTHERN DEVOTIONAL CORPORA + PILGRIMAGE + TEACHER NETWORKS
 -> regional languages, temples, sects and remembered guru lineages
 -> RAMANANDA tradition and diverse disciple lists
 -> northern Rama devotion, nirguna critique and vernacular publics
CAUTION: hagiographic genealogy is not a dated attendance register.""",
            ["Ramananda", "Transmission", "Hagiography"],
        ),
        (
            "Kabir critique and corpus method",
            "evidence-matrix",
            """CRITIQUE -> empty ritual, inherited rank and sectarian certainty
LANGUAGE -> accessible vernacular and memorable couplet
THEOLOGY -> nirguna devotion with vocabulary crossing social worlds
CORPUS -> oral circulation and variant later compilations
EFFECT -> ethical challenge and community formation, not abolished caste
LIVE BRIDGE -> modern Kabir memory cannot authenticate medieval wording.""",
            ["Kabir", "Nirguna", "Corpus criticism", "PIB"],
        ),
        (
            "Nanak householder ethic",
            "cause-mechanism-effect",
            """ONE DIVINE REALITY + REMEMBRANCE
 -> HONEST WORK + SHARING + HOUSEHOLDER DISCIPLINE
 -> critique of empty ritual, hierarchy and renunciatory monopoly
 -> ethical community rooted in ordinary social life
CAUTION: separate Nanak's moment from later Sikh institutions.""",
            ["Guru Nanak", "Householder path", "Ethical monotheism"],
        ),
        (
            "Chaitanya public devotion",
            "process",
            """KRISHNA DEVOTION + EMOTIONAL SURRENDER
 -> KIRTAN: collective singing, movement and embodied participation
 -> BENGAL-PURI network: pilgrimage, disciples and remembered charisma
 -> broader affective public and literary-cultural transmission
TRAP: public participation did not automatically erase hierarchy.""",
            ["Chaitanya", "Kirtan", "Bengal", "Puri"],
        ),
        (
            "Bhakti-Sufi interaction without merger",
            "comparison-matrix",
            """SHARED FIELD -> towns, crafts, vernaculars, music, pilgrimage and service
SIMILARITIES -> love, guru/pir relation, ethical critique and accessible idiom
DIFFERENCES -> theology, scripture, law, ritual and institutional lineage
CONTACT -> translation, vocabulary, technique and shared audiences
SAFE FRAME -> parallel exchange or symbiosis with boundaries
TRAP: similarity is not proof of direct borrowing or doctrinal identity.""",
            ["Bhakti-Sufi comparison", "Symbiosis", "Boundaries"],
        ),
        (
            "Topic 10 answer spine",
            "answer-synthesis",
            """OPEN -> plural devotional and mystical currents, not two monoliths
SUFI -> vocabulary + order + khanqah + political posture
BHAKTI -> southern roots + doctrines + poet-saints + vernacularisation
COMPARE -> shared social field while preserving theological differences
QUALIFY -> inclusion, caste, gender, corpus and hagiographic limits
CLOSE -> enlarged ethical and cultural vocabularies without ending hierarchy.""",
            ["Answer architecture", "Source method", "Social impact"],
        ),
    ],
}


def normalized_fragment(fragment: str, metadata: bool = False) -> str:
    return previous.normalized_fragment(fragment, metadata=metadata)


def normalize_mcq_fragment(fragment: str) -> str:
    return previous.normalize_mcq_fragment(fragment)


def compose(
    config_value: dict[str, object],
    preamble: str,
    grouped: dict[str, list[str]],
) -> str:
    return previous.compose(config_value, preamble, grouped)


def extract_terminal_mcq(
    fragment: str,
    pattern: str,
) -> tuple[str, str | None]:
    match = re.search(pattern, fragment)
    if not match:
        return fragment, None
    teaching = fragment[: match.start()].rstrip() + "\n"
    mcq = normalize_mcq_fragment(match.group(0))
    return teaching, mcq


def assemble_topic_09(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    source = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)
    preamble, sections = previous.previous.base.split_h2(source)
    preamble = previous.previous.base.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        metadata = title.startswith(
            ("Package scope", "Guided Tutor roadmap", "How to use")
        )
        numbered_session = bool(re.match(r"^\d{2}\.", title))
        if numbered_session:
            fragment, extracted = extract_terminal_mcq(
                fragment,
                r"(?ms)^### Learning MCQ \d+.*\Z",
            )
            if extracted:
                grouped["mcq"].append(normalized_fragment(extracted))
        if metadata or numbered_session:
            bucket = "basic"
        elif title.startswith("Distributed learning-MCQ answer rotation audit"):
            continue
        elif title.startswith(
            ("Part V", "Part VI")
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith(
            ("Part III", "Part IV")
        ):
            bucket = "practice"
        elif title.startswith("Final consolidated register notes"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 09 section: {title}")
        grouped[bucket].append(normalized_fragment(fragment, metadata=metadata))
    return compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble_topic_10(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    source = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)
    preamble, sections = previous.previous.base.split_h2(source)
    preamble = previous.previous.base.strip_title(preamble)
    preamble = re.sub(
        r"(?ms)\n*!\[Topic cover[^\n]*\]\([^)]+\)\s*\n+"
        r"\*Topic cover[^\n]*\*\s*",
        "\n",
        preamble,
    ).strip()
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        metadata = title.startswith(
            ("Package scope", "Guided Tutor roadmap", "How to use")
        )
        numbered_session = bool(re.match(r"^\d{2}\.", title))
        if numbered_session:
            fragment, extracted = extract_terminal_mcq(
                fragment,
                r"(?ms)^### Q\d+\..*\Z",
            )
            if extracted:
                grouped["mcq"].append(normalized_fragment(extracted))
        if metadata or numbered_session:
            bucket = "basic"
        elif title.startswith(
            ("Part V", "Part VI")
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith(
            ("Part III", "Part IV", "Part VII")
        ):
            bucket = "practice"
        elif title.startswith("FINAL CONSOLIDATED REGISTER NOTES"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 10 section: {title}")
        grouped[bucket].append(normalized_fragment(fragment, metadata=metadata))
    return compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-09":
        return assemble_topic_09(config_value)
    return assemble_topic_10(config_value)


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
                "source_markdown": previous.previous.base.relative(
                    Path(config_value["canonical"])
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Medieval Indian History learner-v2 Topics 09-10",
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
        *[ROOT / item for item in previous.previous.COMMON_CROSS],
        *[ROOT / item for item in previous.previous.PYQ_INDEXES],
        *local_books,
        Path(config_value["legacy_main"]),
        Path(config_value["legacy_workbook"]),
        ROOT / str(config_value["cover_path"]).replace("/", "\\"),
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *previous.previous.base.image_sources(Path(config_value["canonical"])),
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
        "source_markdown": previous.previous.base.relative(source_path),
        "source_basic": previous.previous.base.relative(Path(config_value["basic"])),
        "source_canonical": previous.previous.base.relative(
            Path(config_value["canonical"])
        ),
        "source_advanced": previous.previous.base.relative(
            Path(config_value["advanced"])
        ),
        "manifest": previous.previous.base.relative(SECTION_MANIFEST),
        "cross_topic_sources": previous.previous.COMMON_CROSS,
        "pyq_indexes": previous.previous.PYQ_INDEXES,
        "official_question_sources": [],
        "local_ocr_sources": [
            previous.previous.base.relative(path) for path in local_books
        ],
        "live_sources": config_value["live_sources"],
        "source_files": [
            previous.previous.base.relative(path) for path in deduplicated
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
    previous.previous.DATE = DATE
    previous.previous.TOPICS = TOPICS
    previous.previous.PANEL_DATA = PANEL_DATA
    previous.previous.ASCII_PATH = ASCII_PATH
    write_ascii_spec()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH]
    for config_value in TOPICS:
        key = str(config_value["key"])
        markdown = assemble(config_value)
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        source_path.write_text(markdown, encoding="utf-8")
        graphical_path = previous.previous.write_graphical_spec(
            config_value,
            markdown,
        )
        generation_spec = write_generation_spec(
            config_value,
            source_path,
            graphical_path,
        )
        written.extend([source_path, graphical_path, generation_spec])
    for path in written:
        print(previous.previous.base.relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
