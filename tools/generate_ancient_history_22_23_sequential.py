"""Assemble Ancient History learner-v2 Topics 22-23 and authored visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_ancient_history_17_21_sequential as base


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Ancient-Indian-History"
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
GRAPHICAL_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / "Ancient-Indian-History"
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
ASCII_PATH = ASCII_DIR / "ancient-indian-history-22-23-2026-08-30-sequential.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "ancient-indian-history--subject-wide-syllabus.json"
)
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"


def config(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    live_sources: list[str],
    current_note: str,
    include_art_book: bool = False,
) -> dict[str, object]:
    key = f"ancient-indian-history-{number:02d}"
    legacy_stem = canonical.removesuffix("_Complete-Topic-Package.md")
    return {
        "number": number,
        "key": key,
        "title": title,
        "canonical": KNOWLEDGE / canonical,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "legacy_main": (
            ROOT
            / "notes"
            / "Ancient-Indian-History"
            / f"{legacy_stem}_Complete-Topic-Package_2026-08-15.pdf"
        ),
        "legacy_workbook": (
            ROOT
            / "notes"
            / "Ancient-Indian-History"
            / f"{legacy_stem}_Solved-Workbook_2026-08-15.pdf"
        ),
        "live_sources": live_sources,
        "current_note": current_note,
        "include_art_book": include_art_book,
    }


TOPICS = [
    config(
        22,
        "Post-Gupta India: Harsha & Eastern India",
        "22_Post-Gupta-Harsha-and-Eastern-India_Complete-Topic-Package.md",
        "22_Post-Gupta-Harsha-and-Eastern-India.md",
        "22_Post-Gupta-Harsha-and-Eastern-India.md",
        [
            "https://whc.unesco.org/en/list/1502",
            "https://culture.gov.in/events/ministry-culture-showcases-confluence-heritage-and-technology-india-ai-impact-summit-2026",
        ],
        "UNESCO's Nalanda Mahavihara record and the Ministry of Culture's 2026 "
        "heritage-technology update were rechecked on 30 August 2026. They are "
        "used only for present conservation, manuscript access and evidence-method "
        "linkages; they do not alter the post-Gupta chronology.",
    ),
    config(
        23,
        "Peninsular India: Pallavas, Chalukyas & Brahmanization",
        "23_Peninsular-India-Pallavas-Chalukyas_Complete-Topic-Package.md",
        "23_Peninsular-India-Pallavas-Chalukyas.md",
        "23_Peninsular-India-Pallavas-Chalukyas.md",
        [
            "https://whc.unesco.org/en/list/249",
            "https://whc.unesco.org/en/list/239",
            "https://culture.gov.in/events/ministry-culture-showcases-confluence-heritage-and-technology-india-ai-impact-summit-2026",
        ],
        "UNESCO's Mahabalipuram and Pattadakal records and the Ministry of Culture's "
        "2026 heritage-technology update were rechecked on 30 August 2026. They "
        "supply bounded conservation and documentation context, not evidence for "
        "new dynastic or architectural chronology.",
        include_art_book=True,
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "ancient-indian-history-22": [
        (
            "Chronology and evidence discipline",
            "timeline",
            """c. 550 CE -> Gupta concentration weakens; regional houses multiply
606 CE -> Harsha succeeds amid the Rajyavardhana-Rajyashri crisis
c. 630s -> Pulakeshin II checks northern expansion near the Narmada
637 CE -> Shashanka dies; eastern competition continues
647-648 CE -> Harsha dies without a durable successor empire
SOURCES: Bana + Xuanzang + charters + coins + Aihole + archaeology
RULE: triangulate literary praise, pilgrim report and rival inscription.""",
            ["Scope", "Chronology", "Evidence discipline"],
        ),
        (
            "Post-Gupta political landscape",
            "network-map",
            """NORTH-WEST / WEST -> Maitrakas and other regional powers
MIDDLE GANGA -> Later Guptas + Maukharis
THANESAR-KANNAUJ -> Pushyabhutis under Harsha
GAUDA -> Shashanka
KAMARUPA -> Bhaskaravarman
DECCAN LIMIT -> Badami Chalukyas under Pulakeshin II
VERDICT: several strong regional states replaced one uncontested imperial centre.""",
            ["Political landscape", "Regional powers"],
        ),
        (
            "Pushyabhuti rise and Kannauj shift",
            "cause-mechanism-effect",
            """PRABHAKARAVARDHANA -> stronger Thanesar line
RAJYASHRI + GRAHAVARMAN -> Maukhari marriage bridge
Grahavarman killed -> Rajyavardhana campaigns -> accession crisis
HARSHAVARDHANA -> rescue + consolidation + Maukhari inheritance
THANESAR -> KANNAUJ
MECHANISM: kinship + strategy + Ganga-doab access + sovereignty prestige
LIMIT: Harsha inherited a crisis, not a ready-made pan-Indian empire.""",
            ["Pushyabhutis", "Maukharis", "Kannauj"],
        ),
        (
            "Harsha's graded sovereignty and Narmada limit",
            "layered-sovereignty",
            """DIRECT CORE -> Haryana, much of UP and parts of Bihar
PROBABLE REACH -> selected eastern territories including Odisha
WIDER ALLEGIANCE -> Kamarupa, Valabhi and other rulers in varying degrees
HARD LIMIT -> Pulakeshin II and the Narmada frontier
BANA / XUANZANG -> prestige-heavy northern view
AIHOLE -> rival Chalukya check
VERDICT: major north Indian hegemon; not a stable all-India emperor.""",
            ["Harsha's campaigns", "Narmada confrontation"],
        ),
        (
            "Administration, revenue and samanta order",
            "layered-governance",
            """KING / MOBILE CAMP
   -> bhukti provincial units
   -> vishaya district units
   -> officers, villages and revenue collectors
   -> samantas and feudatory rulers
REVENUE: bhaga + bhoga + kara + hiranya
ARMY: royal forces reinforced by subordinate chiefs
TENSION: delegated reach could integrate territory and enlarge local autonomy.""",
            ["Administration", "Revenue", "Samanta pattern"],
        ),
        (
            "Eastern India regional state formation",
            "comparison",
            """BENGAL / GAUDA -> Shashanka, Pundravardhana, Samatata, gold issues
ODISHA -> regional lines, charters, agraharas and expanding settlement
ASSAM -> Kamarupa, Varman line and Bhaskaravarman
COMMON PROCESS -> Sanskrit charters + fiscal districts + military camps
                + land rights + agrarian expansion
DIFFERENCE -> chronology, ecology and political scale varied sharply
RULE: do not begin eastern state history only with the Palas.""",
            ["Gauda", "Kamarupa", "Eastern India"],
        ),
        (
            "Land grants and agrarian transformation",
            "process",
            """FALLOW / CULTIVATED LAND + ROYAL CLAIM
                  |
purchase, charter, boundary record and tax remission
                  |
Brahmana / monastery / religious beneficiary
                  |
cultivation + literacy + fiscal reallocation + landed hierarchy
EASTERN PLATES -> local scribes, merchants, landholders and cultivators
LIMIT: elite charters reveal process more clearly than peasant experience.""",
            ["Land grants", "Agrarian expansion"],
        ),
        (
            "Economy and urban change debate",
            "argument-tree",
            """DECLINE EVIDENCE -> contraction of selected older towns and coin changes
REORGANISATION EVIDENCE:
  |-- Kannauj rises as a strategic centre
  |-- eastern land was purchased with gold in selected records
  |-- new camps, grants, monasteries and regional capitals appear
  `-- routes and markets persist unevenly
NALANDA -> institutional concentration, not proof of universal prosperity
VERDICT: decline in older forms coexisted with regional creation.""",
            ["Economy", "Urban-decline debate"],
        ),
        (
            "Religion, assemblies and political theatre",
            "cultural-ecosystem",
            """EARLY LINE -> solar associations
HARSHACHARITA / CHARTERS -> Shaiva idioms
XUANZANG -> strong Buddhist patronage
KANNAUJ ASSEMBLY -> debate, hierarchy and royal display
PRAYAGA ASSEMBLY -> Buddha + Shiva + Sun across successive days
CHARITY -> piety + redistribution + sovereignty performance
VERDICT: overlapping royal affiliations, not one exclusive religious label.""",
            ["Religion under Harsha", "Kannauj and Prayaga assemblies"],
        ),
        (
            "Nalanda and trans-Asian learning networks",
            "network-map",
            """ROYAL / LANDED SUPPORT -> monastic infrastructure
INDIAN TEACHERS <-> Nalanda study and debate <-> ASIAN PILGRIMS
XUANZANG -> study, travel and carriage of Buddhist texts to China
YIJING -> comparative evidence and numerical caution
UNESCO SITE -> surviving viharas, temples, art and planned layout
SECURE CLAIM: major scholastic network
CAUTION: famous enrolment figures are estimates, not census data.""",
            ["Nalanda", "Learning networks"],
        ),
        (
            "Source criticism and historiography",
            "evidence-matrix",
            """BANA -> accession and court world | literary praise / elite focus
XUANZANG -> routes, Nalanda, assemblies | pilgrim purpose / later writing
CHARTERS -> offices, grants, taxes | selective documentary survival
COINS -> rulers, economy, symbols | circulation is not a border map
AIHOLE -> Narmada limit | rival prashasti and exaggeration
SHARMA -> structural transition | avoid universal decline
METHOD: claim -> source -> corroboration -> limitation.""",
            ["Source criticism", "Historiography"],
        ),
        (
            "Post-Gupta answer spine",
            "answer-synthesis",
            """OPEN -> c. 550-750 as contraction plus regional reorganisation
POLITY -> Pushyabhuti rise + Kannauj + graded sovereignty
LIMIT -> Pulakeshin II and the Narmada
EAST -> Gauda + Kamarupa + Odisha/Bengal grants
STRUCTURE -> samantas + land rights + agrarian change
CULTURE -> assemblies + Nalanda + source triangulation
CLOSE -> Harsha briefly reunited the north while regional states deepened.""",
            ["UPSC answer architecture", "PYQ routes"],
        ),
    ],
    "ancient-indian-history-23": [
        (
            "Peninsular chronology and political geography",
            "spatial-timeline",
            """c. 535 CE -> independent Badami Chalukya power consolidates
late 6th c. -> Simhavishnu renews Pallava expansion
early 7th c. -> Mahendravarman I and Pulakeshin II
c. 630s -> Narmada check on Harsha
c. 642 -> Narasimhavarman I captures Vatapi
8th c. -> Vikramaditya II, Rajasimha legacy and mature temple patronage
757 -> Rashtrakutas end Badami line; Pallavas survive to c. 893.""",
            ["Scope", "Chronology", "Political geography"],
        ),
        (
            "Evidence and source criticism matrix",
            "evidence-matrix",
            """AIHOLE PRASHASTI -> genealogy and campaigns | royal exaggeration
PALLAVA CHARTERS -> grants and legitimation | formulaic claims
SANSKRIT + TAMIL EPIGRAPHY -> praise and documentary practice
MONUMENTS -> patronage, technique and cult | attribution limits
LITERATURE -> court, satire and devotion | genre and redaction
PORT / SETTLEMENT ARCHAEOLOGY -> exchange | uneven survival
RULE: monument first, style label later; inscription data plus ideology.""",
            ["Evidence base", "Source criticism"],
        ),
        (
            "Pallava and Chalukya ruler ladders",
            "comparison",
            """PALLAVA                         CHALUKYA OF BADAMI
Simhavishnu                     Pulakeshin I
Mahendravarman I                Kirtivarman I
Narasimhavarman I Mamalla       Mangalesha
Paramesvaravarman I             Pulakeshin II
Narasimhavarman II Rajasimha    Vikramaditya I / II
Nandivarman line                fall to Rashtrakutas
ANCHORS: Kanchi-Mamallapuram | Vatapi-Aihole-Pattadakal.""",
            ["Pallava rulers", "Chalukya rulers"],
        ),
        (
            "Kanchi-Vatapi rivalry and regional effects",
            "cause-mechanism-effect",
            """KANCHI <-> VENGI / DECCAN ROUTES <-> VATAPI
             |
Pulakeshin II expands east and checks Harsha
             |
Mahendravarman-Pulakeshin conflict
             |
Narasimhavarman I captures Vatapi -> Vatapikonda memory
             |
later Chalukya victories at Kanchi -> Virupaksha commemoration
RESULT: rivalry reshaped frontiers, branches, prestige and sacred landscapes.""",
            ["Pallava-Chalukya rivalry", "Vatapi and Kanchi"],
        ),
        (
            "Administration and local institutions",
            "layered-governance",
            """KING / COURT / MILITARY ELITE
     -> territorial officers and revenue rights
     -> grants to Brahmanas and religious institutions
     -> ur: peasant village
     -> sabha: Brahmana assembly in grant village
     -> nagaram: merchant-linked settlement
     -> mahajana: prominent village elders in Chalukya records
CAUTION: do not project mature later Chola committee detail backward.""",
            ["Administration", "Local institutions"],
        ),
        (
            "Land grants and Brahmanization",
            "process",
            """ROYAL CHARTER -> brahmadeya / agrahara
        -> revenue rights + exemptions + jurisdiction
        -> donee insertion into settled or expanding agrarian zones
        -> cultivation + Sanskritic legitimacy + caste ordering
        -> reciprocal reshaping of local cults and Brahmanical practice
USEFUL MODEL: integration and hierarchy together
LIMIT: not every grant created a new village or proved royal weakness.""",
            ["Land grants", "Brahmanization"],
        ),
        (
            "Bhakti and religious plurality",
            "cultural-ecosystem",
            """ALVARS -> Vaishnava hymns, shrine routes and emotional devotion
NAYANARS -> Shaiva hymns, sacred places and community memory
TEMPLES -> ritual + landed patronage + political visibility
JAIN / BUDDHIST GROUPS -> continued debate, institutions and court presence
INCLUSION STORIES -> Nandanar, Tiruppan Alvar and Andal
LIMIT: devotional access did not abolish caste, patriarchy or elite power
VERDICT: vernacular opening within a hierarchical religious field.""",
            ["Bhakti", "Religious interaction"],
        ),
        (
            "Pallava architecture trajectory",
            "timeline",
            """MAHENDRAVARMAN I -> rock-cut caves: Mandagapattu, Mamandur
NARASIMHAVARMAN I -> Mamallapuram rathas and great reliefs
RAJASIMHA -> Shore Temple + Kailasanatha structural phase
LATER PALLAVAS -> Vaikuntha Perumal and continuing Kanchi patronage
TECHNIQUE: cave -> monolith -> structural temple, with overlap
MEANING: ritual experiment + royal image + coastal sacred landscape
RULE: sequence is analytical, not a crude progress ladder.""",
            ["Pallava architecture", "Mamallapuram"],
        ),
        (
            "Chalukya architecture and Vesara caution",
            "comparison",
            """AIHOLE -> varied structural experiments and plans
BADAMI -> caves, capital landscape and early structural work
PATTADAKAL -> northern and southern superstructure forms side by side
VIRUPAKSHA -> Dravida form, Lokmahadevi and victory memory
PAPANATHA -> comparison point for mixed formal vocabulary
DURGA TEMPLE -> apsidal plan; name does not prove Durga dedication
VESARA: modern shorthand only after site-specific description.""",
            ["Chalukya architecture", "Pattadakal"],
        ),
        (
            "Art, literature and bilingual court culture",
            "cultural-ecosystem",
            """SCULPTURE / RELIEF -> Somaskanda, Shaiva-Vaishnava programmes
PAINTING -> Badami evidence with survival and attribution limits
SANSKRIT -> prashasti, court literature and Mattavilasa-prahasana
TAMIL -> documentary epigraphy and devotional hymn worlds
DANDIN / NANDIKKALAMBAKAM -> literary memory with context cautions
MONUMENT + TEXT -> kingship communicated through several media
2024 GS-I ROUTE: art and literature must appear together.""",
            ["Painting and sculpture", "Languages and literature"],
        ),
        (
            "Economy, ports and Bay of Bengal links",
            "network-map",
            """AGRARIAN SETTLEMENTS -> surplus + taxes + temple support
CRAFT CENTRES -> weaving, metal, sculpture and building labour
KANCHI -> political, religious, literary and commercial centre
MAMALLAPURAM -> coastal outlet and port-hinterland connection
MERCHANT GROUPS / NAGARAMS -> inland and maritime circulation
BAY OF BENGAL -> exchange and cultural contact
LIMIT: maritime connectivity is not proof of a Pallava overseas empire.""",
            ["Economy", "Maritime links"],
        ),
        (
            "Peninsular regionalisation answer spine",
            "answer-synthesis",
            """OPEN -> c. 550-900 as a formative early-medieval transition
POLITY -> Pallava-Chalukya rivalry + Vengi consequence
LOCALITY -> grants + ur/sabha/nagaram + hierarchy
RELIGION -> bhakti + Jain/Buddhist plurality + social limits
ART -> named Pallava and Chalukya sites before style labels
ECONOMY -> Kanchi-Mamallapuram and selective maritime vitality
CLOSE -> rivalry, land, shrines and language rooted regional states.""",
            ["UPSC answer architecture", "Regionalisation"],
        ),
    ],
}


def classify(key: str, title: str) -> str:
    basic_limit = 23 if key.endswith("-22") else 22
    basic_pattern = rf"^(?:0[1-9]|1\d|2[0-{basic_limit - 20}])\."
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if re.match(basic_pattern, title):
        return "basic"
    if title.startswith(("Learning MCQ", "Workbook MCQ", "Remedial")):
        return "mcq"
    if title.startswith(
        (
            "Solved topic-specific MCQs",
            "Verified PYQ",
            "Routed PYQ",
            "Adjacent PYQ",
            "Original solved Mains",
            "Original Mains Practice",
            "Final examiner checklist",
        )
    ):
        return "practice"
    if title.startswith(("Final consolidated register notes", "Final Register")):
        return "register"
    raise ValueError(f"Unclassified {key} section: {title}")


def assemble(config_value: dict[str, object]) -> str:
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
        bucket = classify(str(config_value["key"]), title)
        normalized = base.normalize_fragment(fragment)
        if title.startswith(("Package counts", "Original visual")):
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        if str(config_value["key"]) == "ancient-indian-history-22" and title.startswith(
            "15."
        ):
            normalized = normalized.replace(
                '[ANALYSIS] Therefore the most defensible answer is "uneven '
                'transformation": some old towns lost earlier centrality, but new '
                "regional nodes, monasteries and political centres grew.",
                "[ANALYSIS] Uneven transformation denotes the coexistence of declining "
                "older urban centrality with growing regional nodes, monasteries and "
                "political centres.",
            )
        if str(config_value["key"]) == "ancient-indian-history-22" and title.startswith(
            "Remedial "
        ):
            normalized = normalized.replace(
                "### Remedial ",
                "### Remedial MCQ ",
                1,
            )
        if title.startswith("Final consolidated register notes"):
            normalized = "\n".join(normalized.splitlines()[1:]).strip()
        grouped[bucket].append(normalized)
    advanced = base.normalize_fragment(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "This linkage does not override repository chronology, OCR-searchable book "
        "evidence, verified PYQ routing or the source limitations printed throughout."
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


def write_ascii_spec() -> None:
    topics: list[dict[str, object]] = []
    for config_value in TOPICS:
        key = str(config_value["key"])
        panels = []
        for title, structural_type, body, references in PANEL_DATA[key]:
            lines = body.splitlines()
            if max(map(len, lines)) > 100:
                raise ValueError(f"{key}: ASCII line exceeds 100 characters in {title!r}")
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
        "scope": "Ancient Indian History learner-v2 Topics 22-23",
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
        subject="Ancient-Indian-History",
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
    local_books = [base.RS_SHARMA, base.UPINDER]
    if bool(config_value["include_art_book"]):
        local_books.append(base.SINGHANIA)
    source_files = [
        Path(config_value["basic"]),
        Path(config_value["advanced"]),
        Path(config_value["canonical"]),
        source_path,
        *[ROOT / item for item in base.COMMON_CROSS],
        *[ROOT / item for item in base.PYQ_INDEXES],
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
        "subject": "Ancient-Indian-History",
        "section": "Subject-Wide-Syllabus",
        "topic_folder": key,
        "title": config_value["title"],
        "generation_date": DATE,
        "command": (
            "Generate learner-v2 topic: Ancient History \u2014 Subject-wide Syllabus \u2014 "
            + str(config_value["title"])
        ),
        "source_markdown": base.relative(source_path),
        "source_basic": base.relative(Path(config_value["basic"])),
        "source_canonical": base.relative(Path(config_value["canonical"])),
        "source_advanced": base.relative(Path(config_value["advanced"])),
        "manifest": base.relative(SECTION_MANIFEST),
        "cross_topic_sources": base.COMMON_CROSS,
        "pyq_indexes": base.PYQ_INDEXES,
        "official_question_sources": [],
        "local_ocr_sources": [base.relative(path) for path in local_books],
        "live_sources": config_value["live_sources"],
        "source_files": [base.relative(path) for path in deduplicated],
        "practice_profile": config_value.get(
            "practice_profile",
            (
                "4 verified/routed PYQs; 16 learning, 40 workbook and 8 remedial "
                "MCQs; 6 original solved Mains questions."
            ),
        ),
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
        generation_spec = write_generation_spec(config_value, source_path, graphical_path)
        written.extend([source_path, graphical_path, generation_spec])
    for path in written:
        print(base.relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
