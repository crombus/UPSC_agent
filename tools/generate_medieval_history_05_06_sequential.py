"""Assemble Medieval History learner-v2 Topics 05-06 and visual specs."""

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
ASCII_PATH = ASCII_DIR / "medieval-indian-history-05-06-2026-08-30-sequential.json"
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
SATISH_MUGHALS = (
    ROOT
    / "books"
    / "medival_history"
    / "Medieval-History-Satish-Chandra-1526-1748-Part-2.pdf"
)
UPINDER_SINGH = (
    ROOT
    / "books"
    / "1118Singh, Upinder. _A History of Ancient and Early Medieval India, "
    "2nd Ed. [Easy Reading]_-1.pdf"
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
    local_books: list[Path],
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
    )
    value["cover_alt"] = cover_alt
    value["cover_path"] = cover_path
    value["local_books"] = local_books
    return value


TOPICS = [
    topic_config(
        5,
        "The Tughlaqs: Muhammad bin Tughlaq & Firuz Shah",
        "05_The-Tughlaqs-Muhammad-bin-Tughlaq-Firuz-Shah_Complete-Topic-Package.md",
        "05_Tughlaqs.md",
        "05_Tughlaqs.md",
        "05_The-Tughlaqs-Muhammad-bin-Tughlaq-Firuz-Shah_Complete-Learning-Session_2026-08-16.pdf",
        "05_The-Tughlaqs-Muhammad-bin-Tughlaq-Firuz-Shah_Premium-Solved-PYQ-Workbook_2026-08-16.pdf",
        "4 verified or honestly adjacent PYQs; 16 learning, 40 broad and "
        "12 remedial MCQs; 6 original solved Mains questions.",
        ["https://asi.nic.in/pages/WorldHeritageQutbMinar"],
        "The Archaeological Survey of India's Qutb Minar page was rechecked "
        "on 30 August 2026. It states that inscriptions record repairs to the "
        "minar by Firuz Shah Tughlaq after its earlier Aibak-Iltutmish "
        "construction phases. This official material link helps teach repair, "
        "reuse and dynastic appropriation; it does not validate every literary "
        "claim about Firuz's public works or wider political programme.",
        "Tughlaq comparative cover",
        "notes/Medieval-Indian-History/assets/"
        "05_The-Tughlaqs-Muhammad-bin-Tughlaq-Firuz-Shah/"
        "00_tughlaq_comparative_cover.png",
        [SATISH_HISTORY, SATISH_SULTANAT, UPINDER_SINGH],
    ),
    topic_config(
        6,
        "Decline of the Sultanate: Timur, Sayyids & Lodis",
        "06_Decline-of-the-Sultanate-Timur-Sayyids-Lodis_Complete-Topic-Package.md",
        "06_Decline-Sayyids-Lodis-Timur.md",
        "06_Decline-Sayyids-Lodis-Timur.md",
        "06_Decline-of-the-Sultanate-Timur-Sayyids-Lodis_Complete-Learning-Session_2026-08-16.pdf",
        "06_Decline-of-the-Sultanate-Timur-Sayyids-Lodis_Premium-Solved-PYQ-Workbook_2026-08-16.pdf",
        "4 verified or honestly adjacent PYQs; 16 learning, 32 broad and "
        "12 remedial MCQs; 6 original solved Mains questions.",
        ["https://asi.nic.in/pages/WorldHeritageQutbMinar"],
        "The Archaeological Survey of India's Qutb Minar page was rechecked "
        "on 30 August 2026. It records a repair by Sikandar Lodi as part of a "
        "long material sequence extending beyond the early Sultanate builders. "
        "The linkage is useful for teaching Lodi restoration, monument "
        "afterlives and evidence limits; it does not prove the territorial "
        "reach or administrative effectiveness of the Lodi state.",
        "Delhi Sultanate transition cover",
        "notes/Medieval-Indian-History/assets/"
        "06_Decline-of-the-Sultanate-Timur-Sayyids-Lodis/"
        "00_transition_cover_delhi_to_panipat.png",
        [SATISH_HISTORY, SATISH_SULTANAT, SATISH_MUGHALS],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-05": [
        (
            "Tughlaq chronology and evidence spine",
            "timeline",
            """1320 Ghiyasuddin -> 1325 Muhammad bin Tughlaq
1327-35 Daulatabad phases -> c.1329-33 token currency
1330s doab crisis, cultivation scheme and regional rebellions
1351 Firuz succeeds during Sindh campaign -> 1388 Firuz dies
EVIDENCE: Barani + Isami + Ibn Battuta + Afif + coins + canals + monuments
RULE: separate secure event, chronicler judgement and later legend.""",
            ["Chronology", "Sources"],
        ),
        (
            "Three Tughlaq state strategies",
            "comparison-matrix",
            """GHIYASUDDIN -> moderated restoration, cultivation and frontier authority
MUHAMMAD -> scale, uniformity, experimentation and direct supervision
FIRUZ -> conciliation, heredity, public works and reduced military horizon
SHORT RUN -> restoration | high-risk mobilisation | negotiated stability
LONG RUN -> unfinished consolidation | fragmentation | weaker central checks
VERDICT: compare objectives, instruments, costs and durability.""",
            ["Ghiyasuddin", "Muhammad bin Tughlaq", "Firuz Shah"],
        ),
        (
            "Muhammad's problem of imperial scale",
            "network-map",
            """NORTH-WEST -> frontier risk and strategic ambition
DELHI-DOAB -> grain, revenue, money and army provisioning
DECCAN -> distance, direct rule, Daulatabad and local resistance
BENGAL / GUJARAT / SINDH -> governors, routes and delayed communication
ELITES -> old nobles + foreigners + Indian converts + new appointees
DIAGNOSIS: ambition outran information, trust and enforcement capacity.""",
            ["Imperial scale", "State capacity"],
        ),
        (
            "Five experiment clusters",
            "cause-mechanism-effect",
            """DAULATABAD -> southern supervision | migration and dual-capital logistics
TOKEN MONEY -> monetary flexibility | authentication and redemption
DOAB RESET -> higher dependable revenue | assessment and famine resilience
DIWAN-I-AMIR-I-KOHI -> cultivation | credit and honest supervision
KHURASAN / QARACHIL -> frontier initiative | finance, terrain and intelligence
TEST EACH: rational aim -> required instrument -> implementation failure.""",
            ["Experiments", "Administrative instruments"],
        ),
        (
            "Daulatabad without the empty-Delhi myth",
            "process",
            """DEOGIR / DAULATABAD chosen for central and Deccan position
                |
court, officials, leading groups and some religious-commercial networks moved
                |
Delhi continued to live and mint; coercion and hardship were still real
                |
southern breakaways reduced the project's strategic purpose
VERDICT: second-capital experiment, not total permanent evacuation.""",
            ["Daulatabad", "Migration", "Myth correction"],
        ),
        (
            "Token currency credibility chain",
            "process",
            """STATE ASSIGNS COPPER / BRASS A HIGHER FACE VALUE
                |
success requires mint control + recognisable standard + tax acceptance
                |
weak verification -> private imitation and counterfeit expansion
                |
trust collapses -> redemption burden -> withdrawal
LESSON: monetary design failed through enforcement and credibility gaps.""",
            ["Token currency", "Counterfeiting", "Trust"],
        ),
        (
            "Doab crisis and agrarian repair",
            "cause-mechanism-effect",
            """STANDARD YIELD / OFFICIAL PRICE + HIGH DEMAND
                |
harsh collection + famine stress -> flight, resistance and rebellion
                |
SONDHAR loans + DIWAN-I-AMIR-I-KOHI cultivation programme
                |
corruption, weak monitoring and over-ambitious scale limit recovery
RULE: separate fiscal objective, collector behaviour and climate.""",
            ["Doab taxation", "Diwan-i-Amir-i-Kohi", "Sondhar"],
        ),
        (
            "Khurasan and Qarachil separated",
            "comparison",
            """KHURASAN PROJECT                 QARACHIL EXPEDITION
north-west strategic opening       Himalayan frontier campaign
large recruited force              terrain and supply problem
changed external conditions        severe operational losses
not simply world conquest          not an invasion of China
COMMON LIMIT: strategic ambition exceeded sustainable logistics.""",
            ["Khurasan project", "Qarachil expedition"],
        ),
        (
            "Reading the Tughlaq archive",
            "evidence-matrix",
            """BARANI -> policy detail and elite criticism | later, moralising, aristocratic
ISAMI -> displacement and Deccan memory | hostile political location
IBN BATTUTA -> witnessed court and travel | dramatic, selective, personal
AFIF / FUTUHAT -> Firuz institutions | praise and ruler self-fashioning
COINS / CANALS / MONUMENTS -> material claims | survival is uneven
METHOD: corroborate genre, date, patronage, silence and material trace.""",
            ["Barani", "Isami", "Ibn Battuta", "Afif", "Material evidence"],
        ),
        (
            "Firuz's conciliation bargain",
            "layered-governance",
            """SMALLER GOVERNABLE HORIZON
          |
noble salaries and lighter audits + hereditary offices and iqtas
          |
soldier wajh claims + ulema support + reduced punitive intensity
          |
short-term peace and elite compliance
          |
long-term oligarchic closure, localised army and weaker central discipline.""",
            ["Firuz Shah", "Heredity", "Elite conciliation"],
        ),
        (
            "Works, welfare, slavery and orthodoxy",
            "comparison-matrix",
            """CANALS / HAQQ-I-SHARB -> cultivation and revenue in the northern core
TOWNS / KOTLA / REPAIRS -> urban patronage and dynastic display
DIWAN-I-KHAIRAT / DAR-UL-SHIFA -> bounded charity and care
DIWAN-I-BANDAGAN -> trained coerced service and a political faction
JIZYA / ULEMA -> sharper juristic orthodoxy beside translation and repair
VERDICT: developmental energy coexisted with hierarchy and coercion.""",
            ["Public works", "Welfare", "Slaves", "Religious policy"],
        ),
        (
            "Topic 05 answer spine",
            "answer-synthesis",
            """OPEN -> Tughlaq history is a test of state capacity, not eccentricity alone
CONTEXT -> Ghiyasuddin's restoration and an unusually large inherited empire
MUHAMMAD -> aim, instrument, failure mode and uneven afterlife of each project
FIRUZ -> conciliation, works and welfare balanced against heredity and orthodoxy
SOURCES -> compare chroniclers with coins, canals, inscriptions and monuments
CLOSE -> over-centralisation and negotiated devolution produced different fragilities.""",
            ["Answer architecture", "Comparative verdict"],
        ),
    ],
    "medieval-indian-history-06": [
        (
            "From Firuz's death to Panipat",
            "timeline",
            """1388 Firuz dies -> succession and factional crisis
1398 Timur sacks Delhi -> 1414 Khizr Khan enters Delhi
1414-51 Sayyids -> 1451 Bahlul Lodi
1484 Jaunpur annexed -> 1489-1517 Sikandar Lodi
1526 Ibrahim defeated by Babur at First Panipat
RULE: Delhi contraction, regional vitality and dynastic transition overlap.""",
            ["Chronology", "Transition"],
        ),
        (
            "Structural fragmentation web",
            "cause-mechanism-effect",
            """UNCERTAIN SUCCESSION + HEREDITARY OFFICE + NOBLE FACTION
          |
provincial commanders retain revenue and military resources
          |
distance, communication and army costs weaken rapid central response
          |
regional agrarian-commercial bases sustain alternative courts
          |
DELHI CONTRACTS before Timur; the invasion accelerates an existing crisis.""",
            ["Fragmentation", "Post-Firuz crisis"],
        ),
        (
            "Decline versus regionalisation",
            "comparison",
            """DELHI-CENTRED VIEW               SUBCONTINENTAL VIEW
shrinking coercive reach           Bengal, Gujarat, Malwa and Jaunpur states
prestige loss and civil war        active courts, trade and cultural patronage
Timur's destructive raid          regional political recomposition
VALID CLAIM: Sultanate decline     INVALID CLAIM: all-India civilisational void
BEST FORMULA: central contraction plus regional state formation.""",
            ["Regionalisation", "Balance of power"],
        ),
        (
            "Timur's raid as external shock",
            "spatial-timeline",
            """CENTRAL ASIA -> INDUS / PUNJAB -> DELHI, 1398
MOTIVES -> plunder + strategy + conquest ideology and self-justification
DELHI -> battle, sack, killing, captivity and severe disruption
WITHDRAWAL -> no durable all-India Timurid administration
POLITICAL EFFECT -> prestige collapse and openings for local powers
CAUTION: dramatic numbers in victory traditions are reported, not verified totals.""",
            ["Timur", "Delhi sack", "Consequences"],
        ),
        (
            "How to read Timur's evidence",
            "evidence-matrix",
            """TIMURID MEMOIR TRADITION -> ruler voice and justification | textual layering
COURT CHRONICLES -> campaign sequence | patronage and victory rhetoric
LATER PERSIAN HISTORIES -> memory and synthesis | distance from event
URBAN / MATERIAL TRACE -> disruption and recovery | incomplete survival
REGIONAL POLITICS -> tests whether Delhi's fall equalled India's collapse
METHOD: secure minimum + source label + numerical caution.""",
            ["Timurid sources", "Source criticism"],
        ),
        (
            "Sayyid ruler ladder and weak sovereignty",
            "timeline",
            """KHIZR KHAN 1414-21 -> Punjab base, Timurid association, Delhi capture
MUBARAK SHAH 1421-34 -> repeated pressure and limited recovery
MUHAMMAD SHAH 1434-45 -> narrower authority
ALAM SHAH 1445-51 -> withdrawal; Bahlul takes Delhi
STRUCTURE -> tribute missions + mobile campaigns + contested hinterland
VERDICT: Sayyids preserved Delhi's symbol more than broad coercive reach.""",
            ["Sayyid dynasty", "Khizr Khan", "Weak sovereignty"],
        ),
        (
            "Afghan political tradition",
            "comparison-matrix",
            """SOLIDARITY -> lineage and Roh recruitment could aggregate fighting power
CONSULTATION -> chiefs expected voice, honour and negotiated distribution
EQUALITY CLAIM -> armed nobles resisted extreme royal distance
MONARCHY PROBLEM -> central audit and discipline looked like status loss
CAUTION -> equality among chiefs was not social equality for subjects
RESULT -> mobilisation strength and recurrent centre-noble tension.""",
            ["Afghan nobility", "Kingship", "Political culture"],
        ),
        (
            "Bahlul's consolidation strategy",
            "process",
            """PUNJAB / SIRHIND BASE + AFGHAN RECRUITMENT
                |
1451 Delhi takeover through bargaining and opportunity
                |
personal alliance, territorial sharing and repeated campaigning
                |
Sharqi contest -> Jaunpur annexed in 1484
VERDICT: Delhi recovered range, but partition logic remained embedded.""",
            ["Bahlul Lodi", "Jaunpur", "Afghan mobilisation"],
        ),
        (
            "Sikandar's state-building toolkit",
            "institution-map",
            """NOBLES -> court discipline, farman ritual and jagir account checks
REVENUE -> rent-rolls and gazz-i-Sikandari measurement
ECONOMY -> grain octroi abolition, roads and price stability reports
GEOGRAPHY -> Agra founded in 1506 for doab and western-eastern routes
CULTURE -> Persian learning beside sharper religious orthodoxy
VERDICT: strongest Lodi recovery, still bounded by Afghan bargaining.""",
            ["Sikandar Lodi", "Administration", "Agra"],
        ),
        (
            "Ibrahim's fracture and Panipat system",
            "cause-mechanism-effect",
            """IBRAHIM CENTRALISES -> Afghan nobles fear status and autonomy loss
          |
Daulat Khan, Alam Khan and other rivals widen coalition breakdown
          |
BABUR brings mobile cavalry + field carts + matchlocks / artillery + tulughma
          |
Lodi numerical mass lacks equivalent coordination at Panipat, 1526
VERDICT: guns mattered inside superior leadership and battlefield organisation.""",
            ["Ibrahim Lodi", "First Panipat", "Babur"],
        ),
        (
            "1526: decisive but not instantly final",
            "comparison",
            """CHANGE -> Lodi dynasty falls and Mughal imperial project enters Delhi-Agra
CONTINUITY -> revenue localities, service elites, forts and agrarian structures
RESISTANCE -> Afghan and Rajput powers remain politically consequential
MILITARY -> field artillery gains salience, but adaptation is organisational
HERITAGE -> Lodi tomb landscapes and repairs preserve late-Sultanate afterlives
RULE: dynastic replacement is not immediate subcontinental consolidation.""",
            ["Transition to Mughal rule", "Continuity", "Architecture"],
        ),
        (
            "Topic 06 answer spine",
            "answer-synthesis",
            """OPEN -> define decline as Delhi's contraction, not India's collapse
CAUSES -> succession, elite autonomy, fiscal-military strain and regional bases
SHOCK -> Timur accelerates weakness; label evidence and numbers cautiously
TRANSITION -> Sayyid symbolism, Bahlul's recovery and Sikandar's administration
ENDGAME -> Ibrahim-noble fracture plus Babur's integrated battlefield system
CLOSE -> 1526 was decisive dynastically, incomplete politically and continuous institutionally.""",
            ["Answer architecture", "Decline debate", "Panipat"],
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
    return text


def normalized_fragment(fragment: str, metadata: bool = False) -> str:
    value = previous.base.normalize_fragment(fragment)
    if metadata:
        value = re.sub(r"^### ", "#### ", value, count=1)
    return value


def assemble(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    source = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)
    source = re.sub(r"(?m)^# PART ", "## PART ", source)
    preamble, sections = previous.base.split_h2(source)
    preamble = previous.base.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    preamble = f"{cover}\n\n{preamble}"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }

    for title, fragment in sections:
        if title.startswith("PART II"):
            body = re.sub(r"(?m)^## PART II.*$\n*", "", fragment, count=1)
            if body.strip():
                grouped["mcq"].append(
                    normalized_fragment(normalize_mcq_fragment(body))
                )
            continue
        if title.startswith("PART III"):
            continue
        if title.startswith("PART I"):
            continue

        metadata = title.startswith(
            ("Package counts", "Sources actually", "Original visual asset")
        )
        if metadata or re.match(r"^\d{2}\.", title):
            bucket = "basic"
        elif title.startswith(
            (
                "Learning MCQ",
                "Original broad-coverage MCQs",
                "Remedial trap MCQs",
                "Remedial MCQs",
            )
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title in {
            "Solved topic-specific MCQs",
        }:
            continue
        elif title.startswith(
            (
                "PYQ verification",
                "Verified and honestly-adjacent PYQs",
                "Original solved Mains",
            )
        ):
            bucket = "practice"
        elif title == "Final consolidated register notes":
            bucket = "register"
        else:
            raise ValueError(
                f"Unclassified {config_value['key']} section: {title}"
            )
        grouped[bucket].append(normalized_fragment(fragment, metadata=metadata))

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
        "scope": "Medieval Indian History learner-v2 Topics 05-06",
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
