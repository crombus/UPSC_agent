"""Assemble Medieval History learner-v2 Topics 21-22 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_19_20_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-21-22-2026-08-30-sequential.json"
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
        21,
        "Shah Jahan & the Evolution of the Mughal Ruling Class",
        "21_Shah-Jahan-Evolution-Mughal-Ruling-Class_Complete-Topic-Package.md",
        "21_Shah-Jahan-and-Mansabdari-Evolution.md",
        "21_Shah-Jahan-and-Mansabdari-Evolution.md",
        "21_Shah-Jahan-Evolution-Mughal-Ruling-Class_Complete-Learning-Session_2026-08-18.pdf",
        "21_Shah-Jahan-Evolution-Mughal-Ruling-Class_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 20 learning, 44 broad and 16 remedial "
        "MCQs; 10 original solved Mains answers with fiscal-source criticism.",
        [
            "https://pib.gov.in/PressReleasePage.aspx?"
            "PRID=2253199&reg=3&lang=1",
            "https://culture.gov.in/our-organisations/"
            "archaeological-survey-india-new-delhi",
            "https://whc.unesco.org/en/list/252/",
            "https://whc.unesco.org/en/list/231/",
        ],
        "A PIB heritage-conservation explainer dated 18 April 2026, the "
        "Ministry of Culture's ASI mandate page, and UNESCO's Taj Mahal and "
        "Red Fort pages were rechecked on 30 August 2026. The PIB item is used "
        "only as a bounded current bridge to monument protection, scientific "
        "documentation and the AMASR framework; UNESCO supports material-"
        "history claims about patronage, skilled production and imperial "
        "urbanism. None is a Mughal fiscal ledger or evidence for universal "
        "prosperity, exact construction cost, jagir health or a monument-"
        "caused decline. No genuinely topic-specific recent event was found.",
        "Shah Jahan ruling class mansabdari jagir and managed strain cover",
        "notes/Medieval-Indian-History/assets/"
        "21_Shah-Jahan-Evolution-Mughal-Ruling-Class/00_00_cover.png",
        [
            "learning-sessions\\21_Shah-Jahan-Evolution-Mughal-Ruling-Class_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\21_Shah-Jahan-Evolution-Mughal-Ruling-Class_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [],
    ),
    topic_config(
        22,
        "Aurangzeb: Religious Policy, North India & the Rajputs",
        "22_Aurangzeb-Religious-Policy-North-India-Rajputs_Complete-Topic-Package.md",
        "22_Aurangzeb-Religious-Policy-Rajputs.md",
        "22_Aurangzeb-Religious-Policy-Rajputs.md",
        "22_Aurangzeb-Religious-Policy-North-India-Rajputs_Complete-Learning-Session_2026-08-18.pdf",
        "22_Aurangzeb-Religious-Policy-North-India-Rajputs_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 20 learning, 44 broad and 16 remedial "
        "MCQs; 10 original solved Mains answers with case-by-case source control.",
        [],
        "Official heritage, archive and court-source searches were rechecked "
        "on 30 August 2026 for the preceding six months. No material recent "
        "official current-affairs anchor suitable for historical use was "
        "found, so static relevance is retained. Modern litigation, political "
        "claims and contemporary site disputes are not used as proof of a "
        "medieval event. Claims about jizyah, temple action, Sikh history, "
        "local rebellions and Rajput relations remain controlled by dated "
        "repository evidence, OCR books and explicit source criticism.",
        "Aurangzeb religious policy Rajput rupture and evidence method cover",
        "notes/Medieval-Indian-History/assets/"
        "22_Aurangzeb-Religious-Policy-North-India-Rajputs/00_00_cover.png",
        [
            "learning-sessions\\22_Aurangzeb-Religious-Policy-North-India-Rajputs_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\22_Aurangzeb-Religious-Policy-North-India-Rajputs_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-21": [
        (
            "Visible apex and managed strain",
            "balance-sheet",
            """VISIBLE CAPACITY -> revenue claim, armies, court, capital and monuments
MANAGED STRAIN -> growing rank claims meet uneven realised revenue
COURT SPLENDOUR -> evidence of coordination, not universal prosperity
MONTH-RATING -> adaptation inside a functioning order, not final collapse
VERDICT -> an imperial apex carrying an expanding claim-resource mismatch.""",
            ["Golden age", "Managed strain", "Month-scale", "State capacity"],
        ),
        (
            "Shah Jahan chronology, 1628-58",
            "timeline",
            """1628 -> accession after a courtly succession settlement
1633 / 1636 -> Ahmadnagar ends; Bijapur-Golconda framework follows
1638 -> Shahjahanabad foundation and capital-making process
1646-47 -> Balkh venture | 1649-53 -> Qandahar loss and failed recovery
1656-57 -> renewed Deccan pressure | 1657 -> imperial illness
1658 -> Dharmat and Samugarh; sovereignty is violently reconfigured.""",
            ["Shah Jahan", "Deccan", "Shahjahanabad", "Balkh", "Succession"],
        ),
        (
            "The ruling class as a composite service elite",
            "systems-map",
            """CENTRE -> emperor distributes rank, honour, command and revenue claims
SERVICE ELITE -> mansabdars link court access to military-administrative duty
GROUP LABELS -> Turani, Irani, Hindustani, Rajput, Afghan and Deccani overlap
LOCAL LINKS -> houses, clients and regional networks add capacity and leverage
SAFE CLAIM -> diversity widened; no percentage without date and denominator.""",
            ["Mansabdar", "Composite nobility", "Rajputs", "Deccanis"],
        ),
        (
            "Recruitment, reproduction and faction",
            "cause-mechanism-effect",
            """ENTRY -> competence, recommendation, household service and imperial favour
FORMAL RULE -> mansab is appointed, transferable and not automatically hereditary
SOCIAL FACT -> kin, clients, training and reputation reproduce advantage
FACTION -> shifting patronage coalition, not a permanent ethnic voting bloc
PRESSURE -> promotion and good jagirs intensify competition around princes.""",
            ["Recruitment", "Patronage", "Non-heredity", "Faction"],
        ),
        (
            "Mansabdari evolution and verification",
            "timeline",
            """ALAUDDIN / SHER SHAH -> earlier branding and descriptive controls
AKBAR -> mature mansab; zat status-pay and sawar cavalry obligation
JAHANGIR -> du-aspa sih-aspa raises specified cavalry duty, not zat
SHAH JAHAN -> context-bound contingent ratios and closer claim management
CONTROL LIMIT -> nominal rank, inspected muster and field strength can diverge.""",
            ["Zat", "Sawar", "Dagh", "Chehra", "Du-aspa sih-aspa"],
        ),
        (
            "Jagir vocabulary: claim is not ownership",
            "comparison-matrix",
            """JAGIR -> transferable assignment of a state revenue claim for service
JAGIRDAR -> imperial assignee | ZAMINDAR -> locally rooted, variable intermediary
KHALISA -> revenue retained for the crown
JAMA -> assessed or estimated claim | HASIL -> realised collection
WATAN -> hereditary-local association in context, not an ordinary transferable jagir
TRAP -> none of these terms is simply modern private landownership.""",
            ["Jagir", "Jagirdar", "Zamindar", "Jama", "Hasil", "Khalisa"],
        ),
        (
            "How the month-scale worked",
            "process",
            """NOMINAL JAMA -> jagir appears to support twelve months of entitlement
REALISATION TEST -> war, control, survey and collection reduce usable return
MONTH RATING -> twelve becomes eight, six, five, four or less in context
ADJUSTMENT -> salary and sawar obligation scale to effective yield
POLITICAL EFFECT -> pressure for better assignments, patrons and collection
TRAP -> month-rating is a reduction device, not a bonus.""",
            ["Month-scale", "Jama", "Hasil", "Salary", "Sawar"],
        ),
        (
            "From paper rank to effective force",
            "causal-chain",
            """HIGHER MANSAB CLAIMS -> larger salary and cavalry obligations
UNEQUAL JAGIR YIELD -> nominal jama exceeds realised hasil
SHORT RATING -> pay, remounts and contingent support are compressed
ELITE RESPONSE -> bargaining, patronage competition or harder local extraction
STATE RESPONSE -> transfer, muster, ratio rules and fresh assignments
VERDICT -> recurring management reveals strain without proving collapse.""",
            ["Mansab inflation", "Jagir", "Hasil", "Remounts", "Managed strain"],
        ),
        (
            "Expansion creates resources and claimants",
            "balance-sheet",
            """DECCAN GAINS -> forts, tribute claims, routes and assessed revenue
NEW COSTS -> garrisons, commanders, transport, remounts and collection friction
BALKH -> tactical capacity without durable retention
QANDAHAR -> mobilisation cannot overcome every siege and supply constraint
VERDICT -> map expansion and fiscal realisation must be tested separately.""",
            ["Deccan", "Balkh", "Qandahar", "Expansion paradox", "Logistics"],
        ),
        (
            "Grandeur as political economy",
            "two-sided-system",
            """MONUMENTS / CAPITAL -> coordinate labour, workshops, materials and transport
SOVEREIGNTY -> court, fort, mosque, tomb and city make hierarchy visible
URBAN DEMAND -> artisans and suppliers can benefit from concentrated consumption
AGRARIAN BASE -> revenue extraction and distribution remain unequal
TRAP -> splendour is neither a treasury balance nor proof of universal welfare
TRAP -> monuments alone did not cause Mughal decline.""",
            ["Taj Mahal", "Red Fort", "Jama Masjid", "Shahjahanabad"],
        ),
        (
            "Succession as a ruling-class stress test",
            "actor-network",
            """TRIGGER 1657 -> illness creates uncertainty without primogeniture
PRINCES -> Dara, Shuja, Aurangzeb and Murad command regional-household bases
NOBLES -> choose through access, survival, command and expected reward
1658 -> Dharmat and Samugarh shift control of the imperial centre
RESULT -> institutions persist while their sovereign command is violently reassigned
TRAP -> faction is not ethnicity and war is not instant state collapse.""",
            ["Dara Shukoh", "Shah Shuja", "Aurangzeb", "Murad Bakhsh"],
        ),
        (
            "Topic 21 final answer spine",
            "answer-synthesis",
            """OPEN -> visible imperial apex plus managed claim-resource strain
DEFINE -> ruling class, mansab, jagir, jama, hasil and month-rating
TRACE -> composite recruitment -> expanding claims -> uneven realisation
PROVE -> Deccan/frontier costs, capital-making and the 1657-58 stress test
QUALIFY -> no false percentages, monument ledger or inevitable-collapse story
VERDICT -> high capacity adapted to pressure but did not eliminate it.""",
            ["Answer architecture", "Ruling class", "Fiscal mechanism", "Verdict"],
        ),
    ],
    "medieval-indian-history-22": [
        (
            "Differentiated rule under pressure",
            "argument-tree",
            """PERSONAL ORTHODOXY -> preference and public legitimacy matter
SOVEREIGNTY -> emperor still selects officials, policy, war and regulation
LOCAL ADMINISTRATION -> orders acquire uneven reach through officials and powerholders
POLITICAL FIELD -> Rajputs, Sikhs, zamindars and sect communities act independently
VERDICT -> religion is consequential but cannot explain every conflict alone.""",
            ["Aurangzeb", "Orthodoxy", "Statecraft", "Differentiated rule"],
        ),
        (
            "Aurangzeb chronology, 1658-1707",
            "timeline",
            """1658 -> accession | 1665 -> Shivaji treaty boundary
1667 -> Jai Singh dies | c.1669 -> Jat rising and temple-order context
1672 -> Satnami revolt | 1675 -> Guru Tegh Bahadur executed
1678 -> Jaswant Singh dies | 1679 -> jizyah and Rajput war
1681 -> Prince Akbar rebels | 1698 -> Ajit receives recognition
1699 -> Khalsa established | 1707 -> unresolved reign ends.""",
            ["Chronology", "Jizyah", "Guru Tegh Bahadur", "Marwar", "Khalsa"],
        ),
        (
            "Sharia, zawabit and imperial choice",
            "triangle",
            """SHARIA -> legal-moral idiom and learned authority
ZAWABIT -> ruler-made administrative regulations for order and necessity
SOVEREIGNTY -> emperor chooses, patronises, appoints and enforces
FATAWA-I-ALAMGIRI -> Hanafi compendium, not a modern constitution
ULAMA / QAZIS / SADRS -> influential specialists, not a replacement cabinet
RULE -> law informs policy; administration determines reach.""",
            ["Sharia", "Zawabit", "Fatawa-i-Alamgiri", "Ulama"],
        ),
        (
            "Jizyah, 1679: fiscal form and political signal",
            "three-column",
            """FISCAL FORM -> poll tax; neither land revenue nor customs duty
RELIGIOUS STATUS -> classical idiom of differentiated subjecthood
POLITICAL SIGNAL -> visible reversal of an Akbar-era position
IMPLEMENTATION -> collectors, exemptions, corruption and uneven local contact
EFFECT -> alienation and mistrust; no proof of a single revolt or total decline
SAFE VERDICT -> fiscal in form, religious in idiom, political in consequence.""",
            ["Jizyah 1679", "Poll tax", "Differentiation", "Political signal"],
        ),
        (
            "Temple policy: test one action at a time",
            "evidence-ladder",
            """1 SECURE -> dated and corroborated site-specific action
2 PROBABLE -> source-supported local action with limited corroboration
3 CONTESTED -> later tradition or disputed attribution
4 UNSUPPORTED -> list without date, action or provenance
CLASSIFY -> demolition, conversion, confiscation, closure, restriction or grant
RULE -> protection evidence and destruction evidence must both retain scope.""",
            ["Temple policy", "1669 order", "Kashi", "Mathura", "Source criticism"],
        ),
        (
            "Composite nobility: inclusion is not equality",
            "comparison-matrix",
            """INCLUSION -> Hindu, Rajput and later Maratha elites can hold rank and command
EQUALITY -> asks whether fiscal, legal and symbolic distinctions still operate
EARLY RAJPUT SERVICE -> Jai Singh and Jaswant Singh show inherited partnership
LATER RUPTURE -> particular houses resist while others remain in imperial service
VERDICT -> composite recruitment coexists with discriminatory public policy.""",
            ["Composite nobility", "Inclusion", "Equality", "Rajputs", "Marathas"],
        ),
        (
            "Guru Tegh Bahadur: source and consequence",
            "evidence-matrix",
            """MUGHAL FRAME -> law, order and imperial authority
SIKH TRADITION -> martyrdom and defence of religious freedom
HISTORIAN'S TASK -> compare genre, silence, memory and later amplification
1675 CONSEQUENCE -> martyr memory sharpens community-state relations
1699 KHALSA -> leadership, organisation and politics mediate the later outcome
TRAP -> one execution did not mechanically create every later development.""",
            ["Guru Tegh Bahadur", "1675", "Sikh tradition", "Khalsa 1699"],
        ),
        (
            "Jats and Satnamis: compare mechanisms",
            "comparison-matrix",
            """JATS c.1669 -> Mathura corridor; zamindari, agrarian and local coercive setting
RECURRENCE -> Rajaram and later Churaman mark a longer regional process
SATNAMIS 1672 -> Narnaul clash escalates through community mobilisation
IMPERIAL RESPONSE -> rapid suppression shows coercive capacity still exists
RULE -> neither episode is purely class, purely religious or national revolt
VERDICT -> local state-society contact can turn grievance into armed challenge.""",
            ["Gokula", "Jats", "Satnamis", "Narnaul", "Local resistance"],
        ),
        (
            "Marwar: succession becomes legitimacy crisis",
            "cause-mechanism-effect",
            """1678 -> Jaswant Singh dies without a surviving male heir at that moment
POSTHUMOUS CLAIM -> Ajit Singh becomes the Rathor legitimacy focus
KHALISA -> crown administration during dispute, not automatic permanent annexation
OCCUPATION -> searches, force and temple actions destroy confidence
DURGADAS / RATHORS -> claimant protection turns dispute into organised resistance
VERDICT -> precedent without credible honour becomes statecraft failure.""",
            ["Jaswant Singh", "Ajit Singh", "Khalisa", "Durgadas", "Marwar"],
        ),
        (
            "Mewar and Prince Akbar, 1681",
            "actor-network",
            """MEWAR MOTIVES -> kinship, security, autonomy and fear of Marwar occupation
TERRAIN -> Aravalli passes raise pursuit, supply and occupation costs
PRINCE AKBAR -> dynastic alternative attracts a contingent Rajput coalition
FAILURE -> fragile trust and imperial counter-moves defeat the immediate challenge
AFTERMATH -> military failure does not restore alliance credibility
CAUTION -> famous forged-letter story requires provenance labelling.""",
            ["Mewar", "Rana Raj Singh", "Prince Akbar", "Aravalli", "Durgadas"],
        ),
        (
            "Religious policy and Mughal weakening",
            "causal-balance",
            """CONTRIBUTION -> legitimacy loss, alliance mistrust and higher enforcement cost
NAMED EVIDENCE -> jizyah, temple cases, 1675 execution and Rajput breach
COUNTER-EVIDENCE -> composite recruitment and functioning coercive institutions
OTHER PRESSURES -> Deccan war, jagir-rank competition and regional assertion
METHOD -> weigh mechanism, timing, reach and source type
VERDICT -> consequential and contributory, never a complete monocausal theory.""",
            ["Religious policy", "Legitimacy", "Mughal weakening", "Causation"],
        ),
        (
            "Topic 22 final answer spine",
            "answer-synthesis",
            """OPEN -> orthodoxy and statecraft operate together under pressure
TRACE -> policy phases -> jizyah / temple cases -> local and Rajput conflicts
PROVE -> dated case, action type, source reach and political mechanism
COMPARE -> inclusion versus equality; succession versus annexation
QUALIFY -> no communal monocause, blanket denial or universal-destruction list
VERDICT -> policy choices worsened a multi-causal imperial problem.""",
            ["Answer architecture", "Evidence scale", "Rajputs", "Qualified verdict"],
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


def canonical_sections(config_value: dict[str, object]) -> tuple[str, list[tuple[str, str]]]:
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
    return "\n\n".join([cover, preamble]), sections


def assemble_topic_21(config_value: dict[str, object]) -> str:
    preamble, sections = canonical_sections(config_value)
    preamble_parts = [preamble]
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    register_mode = False
    mode = "basic"
    for title, fragment in sections:
        if title.startswith(("Learning roadmap", "PRE-TEACH CHECKLIST")):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if register_mode:
            bucket = "register"
        elif title.startswith("FINAL CONSOLIDATED"):
            register_mode = True
            bucket = "register"
        elif title.startswith("PART XII "):
            mode = "advanced"
            bucket = "advanced"
        elif title.startswith(("PART XIII ", "PART XIV ")):
            mode = "practice"
            bucket = "practice"
        elif title.startswith(
            (
                "Learning MCQ",
                "Broad technical MCQ",
                "Remedial MCQ",
            )
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith(("Transparent PYQ audit", "Mains ")):
            bucket = "practice"
        else:
            bucket = mode
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def assemble_topic_22(config_value: dict[str, object]) -> str:
    preamble, sections = canonical_sections(config_value)
    preamble_parts = [preamble]
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    register_mode = False
    mode = "basic"
    for title, fragment in sections:
        if title.startswith(("Learning roadmap", "PRE-TEACH CHECKLIST")):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if register_mode:
            bucket = "register"
        elif title.startswith("FINAL CONSOLIDATED"):
            register_mode = True
            bucket = "register"
        elif title.startswith(
            (
                "PART XIV - DEEPENING",
                "PART XIV-B",
            )
        ):
            mode = "advanced"
            bucket = "advanced"
        elif title.startswith(
            (
                "PART XIV - PYQ",
                "PART XV ",
                "PART XVI ",
            )
        ):
            mode = "practice"
            bucket = "practice"
        elif title.startswith(("Learning MCQ", "Broad MCQ", "Remedial MCQ")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        else:
            bucket = mode
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-21":
        return assemble_topic_21(config_value)
    return assemble_topic_22(config_value)


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
        "scope": "Medieval Indian History learner-v2 Topics 21-22",
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
