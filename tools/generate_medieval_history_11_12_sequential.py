"""Assemble Medieval History learner-v2 Topics 11-12 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_09_10_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-11-12-2026-08-30-sequential.json"
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
NITIN_ART = ROOT / "books" / "Nitin Singhania's Indian Art and Culture.pdf"
BASE_GENERATOR = previous.previous.previous
BASE = BASE_GENERATOR.base


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
    local_books: list[Path],
) -> dict[str, object]:
    value = BASE_GENERATOR.config(
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
    value["local_books"] = local_books
    return value


TOPICS = [
    topic_config(
        11,
        "Art, Architecture & Culture of the Sultanate",
        "11_Sultanate-Art-Architecture-Culture_Complete-Topic-Package.md",
        "11_Sultanate-Art-and-Architecture.md",
        "11_Sultanate-Art-and-Architecture.md",
        "11_Sultanate-Art-Architecture-Culture_Complete-Learning-Session_2026-08-18.pdf",
        "11_Sultanate-Art-Architecture-Culture_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "1 verified adjacent UPSC Mains route and 1 CAPF technical route; "
        "18 learning, 40 broad and 12 remedial MCQs; 8 original solved "
        "Mains questions.",
        ["https://whc.unesco.org/en/list/233/"],
        "UNESCO's Qutb Minar and its Monuments page was rechecked on "
        "30 August 2026. It supports a bounded heritage bridge: the ensemble "
        "contains mosques, minars, tombs, a madrasa, the Iron Pillar and "
        "successive Qutb-Alai additions; UNESCO also records ASI management, "
        "substantial authenticity and reversible conservation work. The "
        "modern property description does not independently settle every "
        "medieval attribution, motive or contested claim, which remain "
        "controlled by architectural fabric, inscriptions, repository "
        "Markdown and OCR-book source criticism.",
        "Sultanate art architecture and culture cover",
        "notes/Medieval-Indian-History/assets/"
        "11_Sultanate-Art-Architecture-Culture/00_cover.png",
        [
            "learning-sessions\\11_Sultanate-Art-Architecture-Culture_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\11_Sultanate-Art-Architecture-Culture_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [SATISH_HISTORY, SATISH_SULTANAT, NITIN_ART],
    ),
    topic_config(
        12,
        "Babur & the Central Asian Backdrop",
        "12_Babur-Central-Asian-Backdrop_Complete-Topic-Package.md",
        "12_Babur-and-Central-Asian-Backdrop.md",
        "12_Babur-and-Central-Asian-Backdrop.md",
        "12_Babur-Central-Asian-Backdrop_Complete-Learning-Session_2026-08-18.pdf",
        "12_Babur-Central-Asian-Backdrop_Premium-Solved-PYQ-Workbook_2026-08-18.pdf",
        "No fabricated direct CSE PYQ; 18 learning, 40 broad and 12 "
        "remedial MCQs; 10 original solved Mains questions with honest "
        "adjacent-topic routing.",
        ["https://whc.unesco.org/en/tentativelists/5469/"],
        "UNESCO's Bagh-e Babur Tentative List page was rechecked on "
        "30 August 2026. It supports a bounded material and source-method "
        "bridge: the garden preserves Timurid, Mughal and later phases, "
        "Babur's tomb, a central terraced axis, water works, and a restoration "
        "history grounded in archaeology, documents, photographs and "
        "miniatures. It cannot authenticate Babur's campaign narrative, "
        "army figures or political motives; those remain controlled by the "
        "Baburnama, repository Markdown, OCR books and corroboration.",
        "Babur and the Central Asian backdrop cover",
        "notes/Medieval-Indian-History/assets/"
        "12_Babur-Central-Asian-Backdrop/"
        "00_babur_central_asian_backdrop_cover.png",
        [
            "learning-sessions\\12_Babur-Central-Asian-Backdrop_Complete-Learning-Session_2026-08-18.md",
            "learning-sessions\\12_Babur-Central-Asian-Backdrop_Premium-Solved-PYQ-Workbook_2026-08-18.md",
        ],
        [SATISH_HISTORY, SATISH_MUGHALS],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-11": [
        (
            "Culture as power, technique and labour",
            "argument-tree",
            """SULTANATE CULTURE
 -> POWER: conquest, patronage, legitimacy and memory
 -> TECHNIQUE: trabeate + arcuate + mortar + dome transition
 -> LABOUR: masons, stonecutters, designers and material supply
 -> EXPRESSION: monuments, language, literature, music and institutions
VERDICT: architecture is the main archive, not the whole cultural field.""",
            ["Scope", "Patronage", "Craft labour"],
        ),
        (
            "Trabeate and arcuate load paths",
            "comparison-matrix",
            """TRABEATE -> posts support a horizontal lintel or beam
CORBELLED -> courses project inward until the gap is capped
TRUE ARCH -> radiating voussoirs carry compression around an opening
VAULT -> extended arch | DOME -> curved roof over a space
SQUINCH -> corner transition from square chamber toward dome zone
RULE: Sultanate expansion of arcuate practice was not first invention.""",
            ["Trabeate", "Arcuate", "Voussoir", "Squinch"],
        ),
        (
            "Rupture, reuse and adaptation",
            "evidence-matrix",
            """QUWWAT-UL-ISLAM -> reused pillars + new ritual and political programme
ARHAI DIN KA JHONPRA -> early conversion/adaptation and new facade
SPOLIA -> evidence of appropriation and material reuse
WORKSHOP -> local carving and construction choices remain visible
LIMIT -> one documented complex cannot prove a universal policy
SAFE FORMULA -> rupture + adaptation + technical synthesis.""",
            ["Quwwat-ul-Islam", "Arhai Din ka Jhonpra", "Spolia"],
        ),
        (
            "Qutb complex as layered patronage",
            "timeline",
            """AIBAK -> begins mosque/minar programme
ILTUTMISH -> major minar completion + tomb + complex expansion
ALAUDDIN KHALJI -> Alai Darwaza + madrasa + unfinished Alai Minar
FIROZ SHAH TUGHLAQ -> repairs damaged upper minar work
UNESCO / ASI -> present conservation, authenticity and reversible repair
LESSON: read the ensemble across patrons, functions and interventions.""",
            ["Qutb complex", "Layered patronage", "UNESCO"],
        ),
        (
            "Balban to Alai technical sequence",
            "timeline",
            """ILTUTMISH TOMB -> square-to-dome transition experiment
        |
BALBAN TOMB -> first surviving true arch in the assigned source
        |
ALAI DARWAZA -> mature radiating voussoirs, dome and proportion
        |
KHALJI URBAN AMBITION -> Siri and the incomplete Alai programme
TRAP: mature mastery is not the same claim as first surviving example.""",
            ["Iltutmish", "Balban", "Alai Darwaza", "Siri"],
        ),
        (
            "Tughlaq form and inference discipline",
            "cause-mechanism-effect",
            """TUGHLAQABAD / GHIYASUDDIN TOMB
 -> battered walls + rubble/lime surfaces + massive enclosure
 -> fortress effect, strong skyline and restrained ornament
 -> arches continue beside lintel-and-beam combinations
OBSERVE form first; qualify claims about economy or insecurity
RULE: austerity is a visual tendency, not proof of one motive.""",
            ["Tughlaqabad", "Batter", "Ghiyasuddin Tughlaq tomb"],
        ),
        (
            "Regional adaptation matrix",
            "comparison-matrix",
            """BENGAL -> brick + curved roof / drop-arch associations
GUJARAT -> fine stone carving + local Jain-associated craft vocabulary
MALWA / MANDU -> mass + ventilation + water and climate response
JAUNPUR -> lofty portal or screen + no-minar tendency
COMMON -> shared repertoire adapted to material, labour and court setting
TRAP: regional schools are not imperfect copies of Delhi.""",
            ["Bengal", "Gujarat", "Malwa", "Jaunpur"],
        ),
        (
            "Ornament and visual grammar",
            "classification",
            """CALLIGRAPHY -> script becomes visual through scale and placement
ARABESQUE -> geometric-vegetal pattern joined to inscription
LOCAL MOTIFS -> lotus, bell and swastika in adapted workshop vocabularies
COLOUR / MATERIAL -> sandstone, marble and surface contrast
RELIGIOUS SPACE -> often non-figural, but avoid an absolute for all contexts
USE: surface grammar supports synthesis only when tied to a monument.""",
            ["Arabesque", "Calligraphy", "Local motifs"],
        ),
        (
            "Building types and social functions",
            "institution-map",
            """MOSQUE -> congregation, ritual orientation and community visibility
MINAR -> elevated landmark and call-to-prayer association
TOMB -> burial memory, patronage and skyline
MADRASA -> learning and learned patronage
KHANQAH -> Sufi discipline, teaching, hospitality and community
FORT / CITY -> defence, residence, supply, water and political theatre.""",
            ["Mosque", "Minar", "Tomb", "Madrasa", "Khanqah"],
        ),
        (
            "Language, literature and music",
            "network-map",
            """PERSIAN -> court, administration, diplomacy and chronicles
SANSKRIT -> continuing scholarship and textual production
REGIONAL LANGUAGES -> expanding literary and social expression
AMIR KHUSRAU -> Persianate-Hindavi literary evidence and linguistic plurality
MUSIC -> court, devotional and regional contact
CAUTION: do not credit Khusrau with every later instrument or form.""",
            ["Persian", "Regional languages", "Amir Khusrau", "Music"],
        ),
        (
            "Evidence and conservation ladder",
            "evidence-matrix",
            """MONUMENT FORM -> structure and spatial organisation | motive may be uncertain
INSCRIPTION -> patron, act, date or formula | selective public claim
CHRONICLE -> patronage and elite vocabulary | genre and court bias
LEGEND -> later memory | needs independent dating and corroboration
UNESCO / ASI -> current integrity and repair | not medieval provenance
METHOD -> claim -> named evidence -> analysis -> explicit qualification.""",
            ["Source criticism", "Conservation", "UNESCO"],
        ),
        (
            "Topic 11 answer spine",
            "answer-synthesis",
            """OPEN -> cultural field shaped by power, technique, labour and adaptation
TECHNIQUE -> trabeate/arcuate, true arch, dome transition and mortar
SEQUENCE -> reuse -> Qutb/Iltutmish -> Balban -> Khalji -> Tughlaq
REGION -> Bengal, Gujarat, Malwa and Jaunpur transform the repertoire
CULTURE -> institutions + ornament + multilingual literary worlds
CLOSE -> new plural idioms emerged without erasing rupture or hierarchy.""",
            ["Answer architecture", "Chronology", "Qualified synthesis"],
        ),
    ],
    "medieval-indian-history-12": [
        (
            "Central Asian political field",
            "network-map",
            """TIMURID FRAGMENTS -> competing princes and unstable coalitions
UZBEKS / SHAIBANI -> pressure and consolidation in Transoxiana
SAFAVIDS / SHAH ISMAIL -> temporary opening after Merv, 1510
OTTOMANS / CHALDIRAN, 1514 -> regional balance shifts indirectly
BABUR -> Farghana and Samarqand claimant searching for a durable base
RULE: regional geopolitics constrained agency; it did not cause Panipat alone.""",
            ["Timurids", "Uzbeks", "Safavids", "Ottomans"],
        ),
        (
            "Babur chronology 1494-1530",
            "timeline",
            """1494 Farghana -> 1497 / 1501 Samarqand captures and losses
1504 Kabul -> 1510 Merv opening -> 1514 Chaldiran context
1519-20 Bhira and Sialkot -> November 1525 final march
1526 Panipat -> 1527 Khanwa -> 1528 Chanderi -> 1529 Ghagra
30 December 1530 -> Babur dies at Agra
MEMORY: Central Asian constraint -> Indian opening -> staged consolidation.""",
            ["Chronology", "Farghana", "Kabul", "Battle sequence"],
        ),
        (
            "Layered identity and legitimacy",
            "classification",
            """PATERNAL -> Timurid descent and sovereign prestige
MATERNAL -> Chagatai / Chingizid association
MILITARY-POLITICAL -> Turco-Mongol practices and mobile cavalry world
CULTURAL -> Persianate court culture + Chagatai Turkish literary expression
INDIAN DYNASTIC LABEL -> Mughal
TRAP: identity explains legitimacy and networks, not biological destiny.""",
            ["Timurid", "Chagatai", "Persianate", "Mughal"],
        ),
        (
            "Samarqand cycle: prestige versus resources",
            "cause-mechanism-effect",
            """SAMARQAND -> Timurid legitimacy + affluent strategic centre
CAPTURE -> symbolic success
SUPPLY + MONEY + HINTERLAND + FOLLOWER LOYALTY -> insufficient
UZBEK PRESSURE + unstable coalitions -> repeated loss
LEARNING -> manoeuvre, resource discipline and limits of city possession
OUTCOME -> Central Asian failure redirects rather than predestines policy.""",
            ["Samarqand", "Resource base", "Shaibani Khan"],
        ),
        (
            "Kabul-Qandahar strategic bridge",
            "network-map",
            """KABUL 1504 -> survival base, recruitment and southward platform
QANDAHAR -> rear security and Iranian-Central Asian interface
KABUL -> routes toward Kashgar, China, Transoxiana and Turkistan
QANDAHAR -> routes toward Khurasan, Iran and West Asia
LIMIT -> route potential did not automatically solve fiscal weakness
BRIDGE -> Indian agrarian resources + north-western security and trade.""",
            ["Kabul", "Qandahar", "Trade", "Strategic geography"],
        ),
        (
            "Punjab and the Lodi opening",
            "cause-mechanism-effect",
            """BABUR'S EARLIER PUNJAB MOVES + TIMURID CLAIMS
                    |
IBRAHIM LODI-NOBLE TENSIONS + DAULAT KHAN + ALAM KHAN
                    |
local opening, information and favourable timing
                    |
BABUR EXPANDS BEYOND THE INVITERS' LIMITED PURPOSE
FORMULA: external push + internal opening + converting agency.""",
            ["Punjab", "Ibrahim Lodi", "Daulat Khan", "Alam Khan"],
        ),
        (
            "Final march and Panipat frontage",
            "process",
            """NOVEMBER 1525 -> Babur leaves Kabul after securing rear and flank
 -> Punjab movement and communication control
 -> narrow prepared frontage at Panipat
 -> carts linked by raw-hide ropes + breastworks + firing positions
 -> gaps retained for cavalry action
TRAP: not a straight unprepared ride from Kabul to one battle.""",
            ["1525 campaign", "Panipat", "Logistics"],
        ),
        (
            "Panipat combined-arms system",
            "systems-map",
            """FIRE -> artillery and matchlockmen under Ustad Ali and Mustafa
FIX -> carts, ropes, breastworks and constrained frontage
MOVE -> mounted archery, cavalry gaps and tulghuma flanking
COMMAND -> sequencing, reserve use and battlefield coordination
CONTEXT -> Ibrahim's organisation and deployment also matter
VERDICT: guns were important inside a system, never a solitary miracle.""",
            ["Combined arms", "Tulghuma", "Ustad Ali", "Mustafa"],
        ),
        (
            "After Panipat: decision to stay",
            "cause-mechanism-effect",
            """PANIPAT -> Delhi-Agra centre opens
BUT -> forts resist + Afghans remain + begs dislike India + supplies strain
BABUR DISTRIBUTES WEALTH + appeals to followers + chooses settlement
INDIAN RESOURCES -> support a new political base
RESULT -> invasion begins to become state formation
LIMIT -> Humayun and the Sur interregnum expose continuing fragility.""",
            ["Post-Panipat", "Decision to stay", "State formation"],
        ),
        (
            "Panipat-Khanwa-Ghagra ladder",
            "comparison-matrix",
            """PANIPAT 1526 -> Ibrahim Lodi -> removes the Delhi sultanate centre
KHANWA 1527 -> Rana Sanga coalition -> checks a rival north Indian alignment
CHANDERI 1528 -> bounded follow-through against a Rajput stronghold
GHAGRA 1529 -> eastern Afghan resistance in a Bengal-linked setting
TACTICS may recur; opponents, theatres and political functions change
TRAP: consolidation was staged, not complete in April 1526.""",
            ["Panipat", "Khanwa", "Chanderi", "Ghagra"],
        ),
        (
            "Baburnama and heritage source method",
            "evidence-matrix",
            """BABURNAMA -> Chagatai Turkish first-person chronology and observation
STRENGTH -> routes, places, campaigns, gardens and ruler perception
LIMIT -> selective memory, self-fashioning, rhetoric and number inflation
BAGH-E BABUR -> tomb, terraces, water works and layered later interventions
UNESCO -> archaeology, documents, images and conservation reconstruction
RULE: material heritage can corroborate context, not every memoir claim.""",
            ["Baburnama", "Bagh-e Babur", "UNESCO", "Source criticism"],
        ),
        (
            "Topic 12 answer spine",
            "answer-synthesis",
            """OPEN -> Central Asian failure made India attractive, not inevitable
PUSH -> Timurid fragmentation + Uzbek pressure + Kabul resource limits
OPENING -> Punjab claims + Lodi fissures + invitations
MECHANISM -> prepared combined arms and Babur's command
CONSOLIDATION -> decision to stay + Panipat-Khanwa-Ghagra ladder
CLOSE -> a real but fragile Mughal foundation joined two strategic worlds.""",
            ["Answer architecture", "Causation", "Qualified foundation"],
        ),
    ],
}


def normalized_fragment(fragment: str, metadata: bool = False) -> str:
    return previous.normalized_fragment(fragment, metadata=metadata)


def normalize_mcq_fragment(fragment: str) -> str:
    text = previous.normalize_mcq_fragment(fragment)
    text = re.sub(
        r"(?m)^-\s+\*\*([A-D])\.\*\*\s+",
        lambda match: f"- {match.group(1)}. ",
        text,
    )
    text = re.sub(
        r"(?mi)^\*\*Answer:\s*([A-D])\*\*\s*$",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        text,
    )
    return text


def compose(
    config_value: dict[str, object],
    preamble: str,
    grouped: dict[str, list[str]],
) -> str:
    advanced_owner = normalized_fragment(
        Path(config_value["advanced"]).read_text(encoding="utf-8")
    )
    advanced_parts = [*grouped["advanced"], advanced_owner]
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "The live page is a heritage and source-method bridge only. Historical "
        "chronology, causation, attribution and institutional claims remain "
        "controlled by repository Markdown, OCR-searchable books and explicit "
        "source criticism."
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
        + "\n\n".join(advanced_parts)
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "\n\n".join(grouped["register"])
        + "\n"
    )


def strip_frontmatter(source: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", source, flags=re.DOTALL)


def assemble_topic_11(config_value: dict[str, object]) -> str:
    source = strip_frontmatter(
        Path(config_value["canonical"]).read_text(encoding="utf-8")
    )
    preamble, sections = BASE.split_h2(source)
    preamble = BASE.strip_title(preamble)
    preamble = re.sub(
        r"(?ms)\n*!\[Sultanate art,[^\n]*\]\([^)]+\)\s*\n+"
        r"\*Sultanate art,[^\n]*\*\s*",
        "\n",
        preamble,
    ).strip()
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "advanced": [],
        "register": [],
    }
    for title, fragment in sections:
        if title.startswith("Roadmap and evidence protocol"):
            bucket = "basic"
            fragment = re.sub(r"(?m)^ {4}", "", fragment)
        elif title.startswith("Distributed learning MCQ"):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Part II"):
            bucket = "practice"
        elif title.startswith("Part III"):
            bucket = "advanced"
        elif title.startswith("Part IV"):
            bucket = "practice"
        elif title.startswith(("Part V", "Part VI")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Final consolidated"):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 11 section: {title}")
        grouped[bucket].append(normalized_fragment(fragment))
    return compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble_topic_12(config_value: dict[str, object]) -> str:
    source = strip_frontmatter(
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
        if metadata or numbered:
            bucket = "basic"
        elif title.startswith(("PART II.", "PART IV.", "PART V.")):
            bucket = "mcq"
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("PART III."):
            bucket = "practice"
        elif title.startswith("PART VI-A."):
            bucket = "advanced"
        elif title.startswith("PART VI."):
            bucket = "practice"
        elif title.startswith("PART VII."):
            bucket = "register"
        else:
            raise ValueError(f"Unclassified Topic 12 section: {title}")
        grouped[bucket].append(normalized_fragment(fragment, metadata=metadata))
    return compose(config_value, f"{cover}\n\n{preamble}", grouped)


def assemble(config_value: dict[str, object]) -> str:
    if str(config_value["key"]) == "medieval-indian-history-11":
        return assemble_topic_11(config_value)
    return assemble_topic_12(config_value)


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
        "scope": "Medieval Indian History learner-v2 Topics 11-12",
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
