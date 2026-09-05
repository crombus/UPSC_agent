"""Assemble Medieval History learner-v2 Topics 03-04 and authored visual specs."""

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
ASCII_PATH = ASCII_DIR / "medieval-indian-history-03-04-2026-08-30-sequential.json"


TOPICS = [
    previous.config(
        3,
        "Foundation of the Delhi Sultanate: The Slave (Mamluk) Dynasty",
        "03_Foundation-Delhi-Sultanate-Mamluk-Dynasty_Complete-Topic-Package.md",
        "03_Slave-Mamluk-Dynasty.md",
        "03_Slave-Mamluk-Dynasty.md",
        "03_Foundation-Delhi-Sultanate-Mamluk-Dynasty_Complete-Topic-Package_2026-08-13.pdf",
        "03_Foundation-Delhi-Sultanate-Mamluk-Dynasty_Solved-Workbook_2026-08-13.pdf",
        "3 verified/routed PYQs; 48 hard and 12 remedial MCQs; "
        "9 original solved Mains questions.",
        [
            "https://whc.unesco.org/en/list/233/",
            "https://culture.gov.in/qutb-minar-and-its-monuments",
        ],
        "UNESCO's Qutb Minar and its Monuments record was rechecked on "
        "30 August 2026. It identifies the Aibak-Iltutmish building sequence, "
        "Iltutmish's tomb, the complex's early Sultanate architectural value "
        "and continuing ASI management. This heritage record supports bounded "
        "attribution and conservation context; it does not prove uniform "
        "territorial control or remove the need for textual, numismatic and "
        "epigraphic source criticism.",
    ),
    previous.config(
        4,
        "The Khaljis: Alauddin Khalji & Market Reforms",
        "04_The-Khaljis-Alauddin-Khalji-Market-Reforms_Complete-Topic-Package.md",
        "04_Khaljis-Alauddin.md",
        "04_Khaljis-Alauddin.md",
        "04_The-Khaljis-Alauddin-Khalji-Market-Reforms_Complete-Topic-Package_2026-08-16.pdf",
        "04_The-Khaljis-Alauddin-Khalji-Market-Reforms_Solved-Workbook_2026-08-16.pdf",
        "3 verified/routed or honestly adjacent PYQs; 16 learning, 32 broad "
        "and 12 remedial MCQs; 6 original solved Mains questions.",
        [
            "https://consumeraffairs.gov.in/pages/price-monitoring-division",
            "https://whc.unesco.org/en/list/233/",
        ],
        "The Department of Consumer Affairs Price Monitoring Division page "
        "was rechecked on 30 August 2026. It reports daily monitoring of 38 "
        "essential commodities through 575 reporting centres. The modern "
        "example is used only to teach the general analytical categories of "
        "information, supply, enforcement and geographic coverage. Alauddin's "
        "Delhi-centred coercive military-fiscal system had different aims, "
        "institutions and economic conditions and is not treated as a direct "
        "precedent for modern price policy.",
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-03": [
        (
            "Mamluk century chronology",
            "timeline",
            """1206 Aibak -> 1210 succession rupture -> 1211 Iltutmish
1221 Mongol-Khwarazm crisis -> 1229 caliphal investiture
1236 Raziya struggle -> 1246 Nasiruddin Mahmud
1266 Balban -> 1287 succession crisis -> 1290 Khalji transition
RULE: foundation was a repeated process of survival, consolidation and repair.""",
            ["Scope", "Chronology"],
        ),
        (
            "Military slavery and household power",
            "process",
            """PURCHASE / CAPTURE -> household training -> patronage and command
                    -> manumission -> office, iqta and marriage ties
                    -> governor, kingmaker or sovereign
MAMLUK = trained military-household status, not plantation labour
LIMIT: the 1206-1290 rulers were not one simple hereditary bloodline.""",
            ["Mamluk institution", "Manumission"],
        ),
        (
            "Evidence and source discipline",
            "evidence-matrix",
            """HASAN NIZAMI -> Aibak conquest world | panegyric and selectivity
MINHAJ -> Iltutmish, Raziya, offices | court-clerical and gendered lens
BARANI -> Balban and nobility | later, aristocratic and normative
COINS / INSCRIPTIONS -> titles, mints, patrons | claims are not border maps
MONUMENTS -> patronage and technique | repair phases and reuse need caution.""",
            ["Sources", "Historical method"],
        ),
        (
            "Conquest to consolidation",
            "cause-mechanism-effect",
            """GHURID VICTORIES -> forts, garrisons and delegated commanders
AIBAK -> continuity after 1206, Lahore-Delhi axis, limited independent reign
ILTUTMISH -> defeats rivals + restores provinces + secures revenue and Delhi
RESULT -> an Indian-centred Sultanate able to survive the Ghurid rupture
VERDICT: Aibak founded continuity; Iltutmish consolidated sovereignty.""",
            ["Aibak", "Iltutmish"],
        ),
        (
            "Iltutmish and the rival-frontier problem",
            "network-map",
            """YILDIZ / GHAZNI <- NORTH-WEST -> QUBACHA / MULTAN-SIND
                           |
                     DELHI CORE
                           |
        BENGAL-BIHAR detachments + RAJPUT frontier resistance
1221: deny Jalaluddin Mangbarani a risky alliance as Chinggis approaches
METHOD: selective war, delay, recognition and provincial reassertion.""",
            ["Iltutmish", "Mongol frontier", "Regional consolidation"],
        ),
        (
            "Iltutmish's institutional bundle",
            "institution-map",
            """IQTA -> assigned revenue for service; not full land ownership
TANKA / JITAL -> monetary claim and wider circulation
1229 INVESTITURE -> symbolic legitimacy, not political dependence
DELHI -> court, mint, patronage and dynastic centre
SULTAN GHARI / QUTB WORKS -> material statement of durable rule
SYNTHESIS: fiscal, monetary, symbolic and urban consolidation reinforced each other.""",
            ["Iqta", "Coinage", "Caliphate", "Delhi"],
        ),
        (
            "Succession and Raziya",
            "argument-tree",
            """ILtutmish's death -> weak succession rules + court faction
RUKNUDDIN / SHAH TURKAN -> rapid crisis
RAZIYA -> recognised ability + sovereign presentation + wider appointments
                 |
gendered expectations + elite resistance + provincial military conflict
VERDICT: gender mattered through institutions; it was not the only cause.""",
            ["Succession crisis", "Raziya"],
        ),
        (
            "Crown and Chihalgani",
            "comparison-matrix",
            """ELITE SLAVE OFFICERS              SULTANATE CROWN
household loyalty networks         appointment and removal claims
iqtas and provincial commands      revenue and central office
collective bargaining power        need for obedience and succession
CHIHILGANI: remembered corporate elite, not exactly forty cabinet ministers
TENSION: the same network that built the state could constrain the monarch.""",
            ["Chihalgani", "Nobility"],
        ),
        (
            "Balban's kingship architecture",
            "layered-governance",
            """DIVINE SHADOW / MAJESTY
          |
sijda and paibos + court distance + high-born nobility
          |
spies, justice, army review and punishment
          |
royal awe intended to discipline faction and rebellion
CAUTION: Barani's later normative account must not be read as a transcript.""",
            ["Balban", "Kingship", "Court ritual"],
        ),
        (
            "Balban's security state",
            "cause-mechanism-effect",
            """MEWAT / DOAB disorder -> roads, policing, forts and coercion
MONGOL pressure -> frontier commands, garrisons and prince Muhammad
BENGAL / TUGHRIL rebellion -> direct punitive expedition
SUCCESS -> stronger centre and defended approaches
LIMIT -> succession remained fragile; territorial depth stayed uneven.""",
            ["Law and order", "Mongol frontier", "Bengal"],
        ),
        (
            "Architecture as political evidence",
            "timeline",
            """AIBAK -> Quwwat-ul-Islam, Ajmer work, Qutb Minar beginning
ILTUTMISH -> Qutb completion phases, Sultan Ghari, royal tomb
BALBAN -> tomb conventionally linked to an early surviving true arch
MATERIAL STORY -> reuse + local carving + imported forms + experimentation
RULE: monument, inscription and repair phase must be read together.""",
            ["Qutb complex", "Sultan Ghari", "Balban's tomb"],
        ),
        (
            "Topic 03 answer spine",
            "answer-synthesis",
            """OPEN -> foundation was post-conquest state formation, not one event
INSTITUTION -> military households, iqta, coinage and Delhi
POLITICS -> Aibak continuity, Iltutmish consolidation, Raziya's test
MONARCHY -> Chihalgani tension and Balban's coercive repair
LIMITS -> Mongols, Bengal, succession and negotiated regional control
CLOSE -> durable core, uneven reach, major institutional legacy.""",
            ["Answer architecture", "Synthesis"],
        ),
    ],
    "medieval-indian-history-04": [
        (
            "Khalji phase chronology",
            "timeline",
            """1290 Jalaluddin -> 1296 Alauddin seizes power
1297-1306 major Mongol crises and northern campaigns
1303 Chittor and Delhi-Siri crisis -> 1308-1311 Deccan expeditions
1311 Alai Darwaza -> 1316 Alauddin dies
1320 Khusrau Khan falls; Tughlaq transition
RULE: campaigns, reforms and succession must stay on one dated spine.""",
            ["Chronology", "Scope"],
        ),
        (
            "The Khalji revolution debate",
            "comparison",
            """CONTINUITY -> Delhi, iqta, court idiom and frontier problem
CHANGE -> old Turkish monopoly of high office weakened
NOT A MASS REVOLUTION -> cultivators and artisans did not gain equality
BEST FORMULA -> broader elite recruitment plus intensified royal coercion
LIMIT -> Khaljis did not exclude all Turks or abolish inherited institutions.""",
            ["Khalji revolution", "Elite composition"],
        ),
        (
            "Accession and anti-rebellion controls",
            "cause-mechanism-effect",
            """DEVAGIRI LOOT -> wealth and political leverage
MURDER OF JALALUDDIN -> legitimacy and conspiracy anxiety
                  |
confiscation + intelligence + limits on noble feasts, wine and marriage ties
                  |
isolate elite networks and finance the crown
VERDICT: coercive monarchy answered the regime's insecure origin.""",
            ["Alauddin's accession", "Anti-rebellion ordinances"],
        ),
        (
            "Mongol pressure and army reform",
            "institution-map",
            """MONGOL ASSAULTS -> fortified Delhi-Siri and frontier vigilance
LARGE STANDING CAVALRY -> cash salary and regular inspection
DAGH -> horse branding | CHEHRA -> descriptive roll
FORTS + COMMANDERS + INTELLIGENCE -> operational defence
DEPENDENCE -> affordable grain prices were tied to sustaining real wages.""",
            ["Mongol threat", "Dagh", "Chehra", "Siri"],
        ),
        (
            "Expansion and control zones",
            "spatial-timeline",
            """DIRECT CORE -> Delhi, upper doab and key khalisa areas
NORTHERN CAMPAIGNS -> Gujarat, Ranthambore, Chittor and Malwa
DECCAN SUBORDINATION -> Devagiri, Warangal, Dwarasamudra and Mabar
METHODS -> annexation, garrison, tribute, treasure and local ruler retention
RULE: military reach, tributary submission and direct administration differ.""",
            ["Northern expansion", "Deccan campaigns"],
        ),
        (
            "Agrarian revenue engine",
            "cause-mechanism-effect",
            """MEASUREMENT + high state demand in core areas
          |
reduced privileges of khuts, muqaddams and chaudhuris
          |
larger direct revenue claim and tighter village-state link
          |
cash-financed army and weaker rural intermediaries
LIMIT: intensity and implementation were not uniform across the empire.""",
            ["Revenue reforms", "Rural intermediaries"],
        ),
        (
            "Market institutional architecture",
            "layered-governance",
            """SULTAN / POLICY
      |
DIWAN-I-RIYASAT -> registration, rules and supervision
SHAHNA-I-MANDI -> market enforcement
BARIDS / MUNHIYAN -> reports and intelligence checks
MERCHANTS / TRANSPORTERS -> compulsory supply and regulated conduct
RESULT: price schedules required information, supply and coercion together.""",
            ["Diwan-i-Riyasat", "Shahna-i-Mandi", "Enforcement"],
        ),
        (
            "Four regulated market clusters",
            "comparison-matrix",
            """GRAIN -> staple provisioning and military real wage
CLOTH / IMPORTS -> Sarai-i-Adl and registered trade
HORSES / CATTLE / SLAVES -> quality, brokers and military procurement
GENERAL GOODS -> daily urban consumption
CAUTION: quoted schedules depend heavily on Barani and require unit discipline
SCOPE: strongest evidence concerns Delhi, not one uniform national market.""",
            ["Market clusters", "Price schedules"],
        ),
        (
            "Grain supply and scarcity response",
            "process",
            """DOAB COLLECTION / MERCHANT SUPPLY
             |
banjaras and regulated transport -> Delhi markets and state granaries
             |
fixed-price sale + surveillance
             |
scarcity -> controlled release and rationing reports
LIMIT: enforcement pressure and evasion remained part of the system.""",
            ["Grain supply", "Banjaras", "Granaries"],
        ),
        (
            "Military-fiscal causal chain",
            "cause-mechanism-effect",
            """MONGOL THREAT + IMPERIAL AMBITION
          -> larger standing cavalry
          -> cash salaries create provisioning problem
          -> revenue extraction expands state resources
          -> regulated grain supply protects soldiers' real wages
          -> surveillance enforces the chain
VERDICT: army affordability, not welfare equality, is the strongest motive.""",
            ["Military-fiscal system", "Market-reform objectives"],
        ),
        (
            "Effectiveness, sources and limits",
            "evidence-matrix",
            """BARANI -> detailed mechanism | later, moralising and aristocratic
KHUSRAU -> campaigns and court culture | contemporary panegyric
MONUMENTS / COINS -> durable claims | not proof of market reach
EFFECT -> provisioning and army support under Alauddin
LIMIT -> Delhi-centred, coercive, evasion-prone and ruler-dependent
AFTER 1316 -> succession conflict exposes institutional fragility.""",
            ["Sources", "Effectiveness", "Limits"],
        ),
        (
            "Topic 04 answer spine",
            "answer-synthesis",
            """OPEN -> Khalji change combined elite widening and coercive monarchy
PRESSURE -> Mongols, conspiracy and expansion
REFORMS -> revenue + army inspection + market institutions
MECHANISM -> information + supply + price schedule + punishment
ASSESS -> effective in core objectives, geographically and politically bounded
CLOSE -> major military-fiscal experiment, not socialism or a modern command economy.""",
            ["Answer architecture", "Synthesis"],
        ),
    ],
}


def normalize_mcq_fragment(fragment: str) -> str:
    text = previous.normalize_objective_syntax(fragment)
    text = re.sub(
        r"(?m)^([A-D])\.[ \t]+",
        lambda match: f"- {match.group(1)}. ",
        text,
    )
    text = re.sub(
        r"(?m)^\*\*Answer:\*\*[ \t]*([A-D])[ \t]*$",
        lambda match: f"**Answer: {match.group(1)}.**",
        text,
    )
    return text


def assemble_topic_03(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    preamble, sections = previous.base.split_h2(source)
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        if title.startswith("PART "):
            continue
        if title.startswith(("Package practice", "Sources actually")):
            bucket = "basic"
        elif re.match(r"^\d{2}\.", title):
            bucket = "basic"
        elif title.startswith("PYQ "):
            bucket = "practice"
        elif title.startswith(("Hard MCQ", "Remedial MCQ")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Mains "):
            bucket = "practice"
        elif title.startswith("FINAL REGISTER"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 03 section: {title}")
        normalized = previous.base.normalize_fragment(fragment)
        if title.startswith(("Package practice", "Sources actually")):
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        grouped[bucket].append(normalized)
    return compose(config_value, preamble, grouped)


def assemble_topic_04(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    source = re.sub(r"(?m)^# PART ", "## PART ", source)
    source = re.sub(
        r"(?m)^### (Verified and routed PYQs|Original broad-coverage MCQs|"
        r"Remedial MCQs - trap correction set)[ \t]*$",
        r"## \1",
        source,
    )
    source = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)
    preamble, sections = previous.base.split_h2(source)
    cover = (
        "![Khalji topic cover]"
        "(notes/Medieval-Indian-History/assets/"
        "04_The-Khaljis-Alauddin-Khalji-Market-Reforms/"
        "00_khalji_cover_state_capacity.png)"
    )
    preamble = previous.base.strip_title(preamble)
    preamble = f"{cover}\n\n{preamble}"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        if title.startswith("PART ") or title == "Solved topic-specific MCQs":
            continue
        if title.startswith(
            ("Package counts", "Sources actually", "Original visual asset")
        ):
            bucket = "basic"
        elif re.match(r"^\d{2}\.", title):
            bucket = "basic"
        elif title.startswith(
            ("Learning MCQ", "Original broad-coverage MCQs", "Remedial MCQs")
        ):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith(("Verified and routed PYQs", "Original solved Mains")):
            bucket = "practice"
        elif title == "Final consolidated register notes":
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 04 section: {title}")
        normalized = previous.base.normalize_fragment(fragment)
        if title.startswith(
            ("Package counts", "Sources actually", "Original visual asset")
        ):
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        grouped[bucket].append(normalized)
    return compose(config_value, preamble, grouped)


def compose(
    config_value: dict[str, object],
    preamble: str,
    grouped: dict[str, list[str]],
) -> str:
    advanced = previous.base.normalize_fragment(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "The live material is a teaching bridge only. Historical chronology, "
        "causation and institutional claims remain controlled by repository "
        "Markdown, OCR-searchable books and source criticism."
    )
    return (
        f"# {config_value['title']} - Complete Topic Package\n\n"
        f"{previous.base.strip_title(preamble)}\n\n"
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


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-03":
        return assemble_topic_03(config_value)
    return assemble_topic_04(config_value)


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
        "scope": "Medieval Indian History learner-v2 Topics 03-04",
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
        generation_spec = previous.write_generation_spec(
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
