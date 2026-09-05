"""Assemble Ancient History learner-v2 Topics 26-27 and authored visual specs."""

from __future__ import annotations

import json
import re
from pathlib import Path

import generate_ancient_history_22_23_sequential as prior


ROOT = prior.ROOT
DATE = "2026-08-30"
KNOWLEDGE = prior.KNOWLEDGE
SESSION_DIR = prior.SESSION_DIR
ASCII_DIR = prior.ASCII_DIR
ASCII_PATH = ASCII_DIR / "ancient-indian-history-26-27-2026-08-30-sequential.json"


def topic(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    legacy_date: str,
    live_sources: list[str],
    current_note: str,
    practice_profile: str,
    *,
    include_art_book: bool,
) -> dict[str, object]:
    value = prior.config(
        number,
        title,
        canonical,
        basic,
        advanced,
        live_sources,
        current_note,
        include_art_book=include_art_book,
    )
    legacy_stem = canonical.removesuffix("_Complete-Topic-Package.md")
    value["legacy_main"] = (
        ROOT
        / "notes"
        / "Ancient-Indian-History"
        / f"{legacy_stem}_Complete-Topic-Package_{legacy_date}.pdf"
    )
    value["legacy_workbook"] = (
        ROOT
        / "notes"
        / "Ancient-Indian-History"
        / f"{legacy_stem}_Solved-Workbook_{legacy_date}.pdf"
    )
    value["practice_profile"] = practice_profile
    return value


TOPICS = [
    topic(
        26,
        "From Ancient to Medieval: Social Change & Legacy",
        "26_From-Ancient-to-Medieval-Social-Change-and-Legacy_Complete-Topic-Package.md",
        "26_From-Ancient-to-Medieval-Legacy.md",
        "26_From-Ancient-to-Medieval-Legacy.md",
        "2026-08-15",
        [
            "https://unesdoc.unesco.org/ark:/48223/pf0000399139_eng",
            "https://culture.gov.in/events/ministry-culture-showcases-confluence-heritage-and-technology-india-ai-impact-summit-2026",
        ],
        "UNESCO's August 2026 consultation on preserving and providing access "
        "to documentary heritage, including digital heritage, and the Ministry "
        "of Culture's February 2026 Gyan Bharatam update were rechecked on "
        "30 August 2026. They provide bounded evidence-preservation and access "
        "context only; they do not establish early-medieval chronology or settle "
        "the feudalism and regionalisation debates.",
        "10 verified/routed/adjacent PYQs; 16 learning, 32 workbook and 8 "
        "remedial MCQs; 6 original solved Mains questions.",
        include_art_book=False,
    ),
    topic(
        27,
        "Imperial Cholas: State, Society, Economy & Maritime Power",
        "27_Imperial-Cholas-State-Society-Economy-Maritime-Power_Complete-Topic-Package.md",
        "27_Imperial-Cholas-State-Society-Economy-and-Maritime-Power.md",
        "27_Chola-State-Formation-Locality-Debates-and-Indian-Ocean-Networks.md",
        "2026-08-16",
        [
            "https://whc.unesco.org/en/list/250/",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2260755",
            "https://www.mea.gov.in/Portal/ForeignRelation/India-ASEAN-july-2025.pdf",
        ],
        "UNESCO's Great Living Chola Temples record and the May 2026 PIB "
        "repatriation report on Chola-period Nataraja and Somaskanda bronzes "
        "were rechecked on 30 August 2026. The July 2025 India-ASEAN brief "
        "supplies bounded modern maritime-diplomacy context. These sources "
        "support conservation, provenance and present connectivity only; they "
        "do not prove a permanent Chola overseas empire.",
        "4 verified/routed PYQs; 16 learning, 32 broad and 10 remedial MCQs; "
        "6 original solved Mains questions.",
        include_art_book=True,
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "ancient-indian-history-26": [
        (
            "A multitrack transition, not one date",
            "timeline",
            """c. 300-550 -> Gupta-Vakataka repertoires and widening land-grant practice
c. 550-750 -> post-Gupta polities, samantas and stronger regional houses
c. 750-1200 -> temple institutions, regional states and vernacular cultures
POLITICS -> AGRARIAN ORDER -> SOCIETY -> RELIGION -> LANGUAGE
Each track changes at a different speed and in a different region.
RULE: 1206 is not the single birth date of medieval India.""",
            ["Scope", "Periodisation", "Regional chronologies"],
        ),
        (
            "Continuity, change and regional variation",
            "comparison-matrix",
            """CONTINUITY -> Sanskrit prestige, inherited law, pilgrimage and sacred centres
CHANGE -> distributed sovereignty, denser grants and temple-centred institutions
REGIONAL VARIATION -> Bengal != Rajasthan != Deccan != Tamil country
DECLINE -> selected older towns, coin streams and political centres contract
CREATION -> new capitals, markets, settlements and literary cultures emerge
VERDICT: transition means reorganisation, not uniform rupture or stasis.""",
            ["Periodisation", "Regionalisation", "Historical significance"],
        ),
        (
            "Imperial concentration to regional sovereignty",
            "layered-sovereignty",
            """LARGE IMPERIAL CORE WEAKENS
          |
regional dynasties + feudatories + marriage + warfare
          |
KING -> SAMANTA -> DISTRICT / LOCALITY -> VILLAGE
          |
tribute, military service, grants and negotiated obedience
TENSION: integration can enlarge both royal reach and local landed power.""",
            ["Political change", "Samantas", "Distributed sovereignty"],
        ),
        (
            "Land grant: charter to ground effects",
            "cause-mechanism-effect",
            """ROYAL OR LOCAL CLAIM OVER LAND
          |
brahmadeya / agrahara / devadana grant with boundaries and exemptions
          |
beneficiary rights + fiscal reassignment + local intermediaries
          |
settlement, cultivation, hierarchy and institutional endowment
LIMIT: charter rhetoric proves a claim; implementation needs other evidence.""",
            ["Land grants", "Brahmadeya", "Devadana", "Charter evidence"],
        ),
        (
            "Agrarian frontier and social incorporation",
            "process",
            """FOREST / PASTORAL / CULTIVATED ZONES
          |
irrigation + plough expansion + grants + temples + new settlements
          |
chiefs, peasants, Brahmanas, artisans and labour groups negotiate place
          |
surplus extraction + ranked rights + new regional political society
CAUTION: incorporation could create mobility and deepen exclusion together.""",
            ["Agrarian expansion", "Frontiers", "Social incorporation"],
        ),
        (
            "Indian feudalism debate",
            "argument-tree",
            """R. S. SHARMA -> grants, intermediaries, landlordism and reduced mobility
D. D. KOSAMBI -> change from above and below; social-formation approach
HAR BANS MUKHIA -> warns against mechanical European manor-serf transfer
REGIONAL STUDIES -> chronology, ecology and exchange vary substantially
USEFUL CORE -> ask who controlled land, surplus, labour and armed force
VERDICT: use feudalism as a tested model, not a universal label.""",
            ["Feudalism debate", "R. S. Sharma", "Kosambi", "Mukhia"],
        ),
        (
            "Trade, money and town transformation",
            "comparison",
            """CONTRACTION CLAIM              TRANSFORMATION CLAIM
selected coin decline           monetisation varies by region
older urban centres weaken      new capitals and temple towns emerge
some long routes contract       coastal and regional exchange continues
merchant visibility changes     guilds and markets persist unevenly
SYNTHESIS -> old urban forms decline while new nodes and circuits grow.""",
            ["Economy", "Monetisation", "Urban-decline debate"],
        ),
        (
            "Varna text and jati process",
            "comparison-matrix",
            """VARNA -> normative fourfold vocabulary in prescriptive texts
JATI -> numerous lived, occupational and regional social groups
MOBILITY -> rulers and communities seek ranked identities and genealogies
EXCLUSION -> untouchability and unequal labour become more visible
EVIDENCE -> law text + inscription + donation + settlement + material record
TRAP: a normative text is not a demographic census.""",
            ["Varna", "Jati", "Mobility", "Exclusion"],
        ),
        (
            "Brahmanisation, localisation, gender and frontier",
            "cultural-ecosystem",
            """BRAHMANICAL IDIOMS <-> local cults, chiefs and community practice
GENEALOGY + RITUAL + GRANT -> political legitimation
LOCAL DEITIES + CUSTOM -> reshape received Sanskritic forms
WOMEN -> queens and donors visible; ordinary labour remains under-recorded
FRONTIER GROUPS -> incorporation, resistance and layered identity
VERDICT: cultural change is multidirectional, unequal and locally remade.""",
            ["Brahmanisation", "Localisation", "Gender", "Frontier societies"],
        ),
        (
            "Religion and temple as institution",
            "institution-map",
            """TEMPLE
  |-- sacred centre: ritual, bhakti and pilgrimage
  |-- landholder: grants, fields and irrigation rights
  |-- employer: priests, artisans, dancers and service groups
  |-- redistributor: food, gifts, credit and festival expenditure
  `-- archive: inscriptions preserve donors, taxes and local decisions
PLURAL FIELD -> Puranic, Buddhist, Jaina, tantric and local traditions.""",
            ["Religion", "Bhakti", "Temple institutions"],
        ),
        (
            "Language, knowledge and regional cultures",
            "process",
            """SANSKRIT COSMOPOLIS -> portable prestige, genealogy and political idiom
          |
Tamil, Kannada, Telugu, Bengali and other literary worlds deepen
          |
translation + commentary + inscription + devotional performance
          |
regional cultures become locally rooted yet interregionally connected
CONTINUITY: Sanskrit does not vanish. CHANGE: vernacular agency expands.""",
            ["Language", "Vernacularisation", "Knowledge traditions"],
        ),
        (
            "Evidence-led synthesis answer spine",
            "answer-synthesis",
            """OPEN -> define early medieval as an uneven transition
POLITY -> regional states + samantas + negotiated sovereignty
ECONOMY -> grants + agrarian expansion + transformed exchange and towns
SOCIETY -> jati, mobility, exclusion, gender and frontier incorporation
CULTURE -> temple institutions + bhakti + vernacularisation
DEBATE -> test feudalism against regional evidence
CLOSE -> ancient legacies survive through transformation and reinvention.""",
            ["Source criticism", "Legacy", "Answer architecture"],
        ),
    ],
    "ancient-indian-history-27": [
        (
            "Ruler chronology and turning points",
            "timeline",
            """c. 850 -> Vijayalaya secures Tanjavur and a lower-Kaveri foothold
949 -> Takkolam marks a major setback under Parantaka I
985-1014 -> Rajaraja I expands, surveys and builds Brihadisvara
1012-1044 -> Rajendra I; Gangaikondacholapuram and 1025 expedition
1070 onward -> Kulottunga I links Chola and Eastern Chalukya lines
13th c. -> Pandya resurgence and other pressures end imperial primacy.""",
            ["Chronology", "Ruler sequence", "Decline"],
        ),
        (
            "Political geography as zones",
            "network-map",
            """DIRECT CORE -> lower Kaveri delta, Tanjavur and royal-temple centres
ANNEXED ZONES -> Tondaimandalam and changing southern territories
CONTESTED BELTS -> Pandya, Chera and western Deccan frontiers
DYNASTIC HINGE -> Vengi and Eastern Chalukya marriage politics
ISLAND CONTROL -> stronger and longer in northern Sri Lanka
MARITIME ARC -> Maldives and Srivijaya targets; not mainland-style provinces.""",
            ["Political geography", "Expansion", "Owner boundaries"],
        ),
        (
            "Kaveri ecology to imperial capacity",
            "cause-mechanism-effect",
            """KAVERI WATER + DELTA SOILS
          |
tanks, channels, bunds and coordinated irrigation
          |
wet-rice surplus + dense settlement + taxable agrarian base
          |
temples, armies, officials and monumental building
          |
imperial projection inland and across the Bay of Bengal
LIMIT: ecology enabled power; institutions and coercion organised it.""",
            ["Kaveri delta", "Irrigation", "Agrarian core"],
        ),
        (
            "State hierarchy and local institutions",
            "layered-governance",
            """KING / ROYAL HOUSE
   -> mandalam
      -> valanadu
         -> nadu
            -> ur / sabha / nagaram
UR -> general village assembly
SABHA -> Brahmadeya corporate body
NAGARAM -> merchant or market-centred body
VERDICT: royal command and locality institutions operated together unequally.""",
            ["Administration", "Ur", "Sabha", "Nagaram"],
        ),
        (
            "Uttaramerur without the democracy myth",
            "process",
            """ELIGIBLE LOCAL NOTABLES -> qualifications and disqualifications
          |
WARD NOMINATIONS -> names placed on tickets
          |
KUDAVOLAI -> pot-ticket selection for committees
          |
COMMITTEE SERVICE -> rotation, accounts and removal rules
SECURE CLAIM: sophisticated sabha procedure
LIMIT: restricted Brahmadeya participation, not universal adult franchise.""",
            ["Uttaramerur", "Kudavolai", "Local power"],
        ),
        (
            "Land, revenue and social differentiation",
            "comparison-matrix",
            """LAND -> surveyed, classified, endowed and taxed through varied rights
REVENUE -> land dues plus labour, produce and transaction-linked demands
POWER -> vellala landholders, Brahmana bodies, temples and royal agents
PRODUCTION -> cultivators, artisans, herders and service communities
EXCLUSION -> unequal status and segregated labour remain visible
GENDER -> queens and temple donors appear more clearly than ordinary women.""",
            ["Agrarian economy", "Revenue", "Society", "Gender"],
        ),
        (
            "Temple, monument and institutional power",
            "institution-map",
            """BRIHADISVARA / OTHER GREAT TEMPLES
  |-- royal ideology and public monumentality
  |-- endowed land, lamps, food and ritual services
  |-- employment for specialists, artisans and performers
  |-- inscriptions recording donors, taxes and institutional decisions
  `-- living worship across later political periods
RULE: read architecture together with surplus, labour and authority.""",
            ["Temples", "Brihadisvara", "Great Living Chola Temples"],
        ),
        (
            "Bronzes, religion and language",
            "cultural-ecosystem",
            """LOST-WAX CASTING -> individually modelled processional icons
NATARAJA -> theology, movement, ritual use and technical mastery
SHAIVA BHAKTI -> temple liturgy and Nayanmar memory
VAISHNAVA / BUDDHIST / JAINA -> plural but uneven institutional presence
TAMIL + SANSKRIT -> bilingual political, devotional and learned culture
PROVENANCE RULE -> an art object also has a temple and ownership history.""",
            ["Bronzes", "Nataraja", "Religion", "Language"],
        ),
        (
            "Guilds, ports and Bay of Bengal exchange",
            "network-map",
            """KAVERI HINTERLAND -> produce, textiles, metalwork and temple demand
          |
NAGAPATTINAM + OTHER PORTS
          |
merchant bodies: Ayyavole / Manigramam / Anjuvannam
          |
SRI LANKA -> MALDIVES -> STRAITS -> SOUTHEAST ASIA -> CHINA
MONSOON + SHIPPING + CREDIT + DIPLOMACY sustain movement
LIMIT: trade networks were not simply state-owned fleets.""",
            ["Merchant guilds", "Ports", "Indian Ocean trade"],
        ),
        (
            "Sri Lanka and Srivijaya: coercion with limits",
            "comparison",
            """SRI LANKA                       SRIVIJAYA, 1025
territorial conquest            rapid strike on linked centres
provincial administration       no durable mainland-style province
long resistance and reconquest  commercial-strategic signalling
stronger northern control       target list from Chola inscription
COMMON POINT -> maritime logistics and royal coercive capacity
CAUTION -> expeditionary success != permanent oceanic empire.""",
            ["Sri Lanka", "Srivijaya campaign", "Maritime power"],
        ),
        (
            "How historians model the Chola state",
            "argument-tree",
            """CENTRALISED VIEW -> strong monarchy, hierarchy, survey and taxation
BURTON STEIN -> segmentary state and ritually radiating sovereignty
KARASHIMA / SUBBARAYALU -> inscription-led locality, land and social analysis
NEGOTIATED MODEL -> royal force + temple + nadu + sabha + local elites
BEST USE -> compare evidence by region and reign
VERDICT: neither perfect bureaucracy nor autonomous village republic.""",
            ["Historiography", "Stein", "Karashima", "Subbarayalu"],
        ),
        (
            "Decline, legacy and answer spine",
            "answer-synthesis",
            """CAUSES -> succession strains + frontier wars + Pandya resurgence
        + Hoysala pressure + locality and resource shifts
END OF EMPIRE != end of temples, irrigation, Tamil culture or trade
OPEN -> Kaveri-centred agrarian-imperial-commercial formation
BODY -> state/locality + economy/society + temple/culture + maritime reach
QUALIFY -> inscriptions are elite; sea power was selective
CLOSE -> durable regional institutions outlasted imperial primacy.""",
            ["Decline", "Legacy", "Answer architecture"],
        ),
    ],
}


def classify(key: str, title: str) -> str:
    basic_pattern = (
        r"^(?:0[1-9]|1\d|2[0-2])\."
        if key.endswith("-26")
        else r"^(?:0[1-9]|1\d|2[0-4])\."
    )
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if re.match(basic_pattern, title):
        return "basic"
    if title.startswith(
        (
            "Learning MCQ",
            "Workbook MCQ",
            "Remedial MCQ",
            "Broad topic coverage MCQs",
        )
    ):
        return "mcq"
    if title.startswith(
        (
            "Solved topic-specific MCQs",
            "Verified PYQ",
            "Routed PYQ",
            "Adjacent PYQ",
            "Boundary PYQ",
            "Original Mains Practice",
            "Original solved Mains",
            "Final examiner checklist",
        )
    ):
        return "practice"
    if title.startswith(("Final consolidated register notes", "Final Register")):
        return "register"
    raise ValueError(f"Unclassified {key} section: {title}")


def append_topic_27_workbook(
    grouped: dict[str, list[str]],
    fragment: str,
) -> None:
    broad_marker = "\n### Original broad-coverage MCQs"
    mains_marker = "\n### Original solved Mains questions"
    if broad_marker not in fragment or mains_marker not in fragment:
        raise ValueError("Topic 27 nested workbook markers are incomplete.")
    pyq_fragment, remaining = fragment.split(broad_marker, 1)
    mcq_fragment, mains_fragment = remaining.split(mains_marker, 1)
    mcq_fragment = re.sub(
        r"(?m)^#### Remedial (\d+)\s*$",
        r"#### Remedial MCQ \1",
        mcq_fragment,
    )
    grouped["practice"].append(prior.base.normalize_fragment(pyq_fragment))
    grouped["mcq"].append(
        prior.base.normalize_fragment(
            "### Original broad-coverage MCQs" + mcq_fragment
        )
    )
    grouped["practice"].append(
        prior.base.normalize_fragment(
            "### Original solved Mains questions" + mains_fragment
        )
    )


def assemble(config_value: dict[str, object]) -> str:
    canonical = Path(config_value["canonical"])
    source = canonical.read_text(encoding="utf-8")
    source = source.replace(
        "[ANALYSIS] Therefore the best UPSC line is: varna remained the ideal "
        "hierarchy; jati marked the proliferating social process.",
        "[ANALYSIS] The evidence supports a clear distinction: varna remained "
        "the ideal hierarchy; jati marked the proliferating social process.",
    )
    source = re.sub(
        r"(?m)^\*\*Answer:\*\*\s*([A-D])\s*$",
        r"**Answer: \1.**",
        source,
    )
    preamble, sections = prior.base.split_h2(source)
    cleaned_preamble = prior.base.strip_title(preamble)
    if str(config_value["key"]) == "ancient-indian-history-26":
        cleaned_preamble = cleaned_preamble.replace(
            "bounded cross-owner Ancient History Topics 20-25 and 27 for routed "
            "continuity -> no forced current-affairs hook because no genuinely "
            "necessary live heritage update was required -> Qdrant not used.",
            "bounded cross-owner Ancient History Topics 20-25 and 27 for routed "
            "continuity -> bounded official heritage-preservation linkage -> "
            "Qdrant not used.",
        )
        cleaned_preamble = cleaned_preamble.replace(
            "- No live current-affairs source was forced into the package. This is "
            "deliberate. The brief asked for live material only if genuinely relevant "
            "to heritage or historiography; the static historical evidence base was "
            "already strong enough.",
            "- Live material remains bounded to documentary-heritage preservation "
            "and access. It does not alter the static historical evidence or settle "
            "the package's historiographical debates.",
        )
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        if (
            str(config_value["key"]) == "ancient-indian-history-27"
            and title == "Solved topic-specific MCQs"
        ):
            append_topic_27_workbook(grouped, fragment)
            continue
        bucket = classify(str(config_value["key"]), title)
        normalized = prior.base.normalize_fragment(fragment)
        if title.startswith(("Package counts", "Original visual")):
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        if title.startswith("Final consolidated register notes"):
            normalized = "\n".join(normalized.splitlines()[1:]).strip()
        if normalized:
            grouped[bucket].append(normalized)
    advanced = prior.base.normalize_fragment(
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
        f"{cleaned_preamble}\n\n"
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
                "source_markdown": prior.base.relative(
                    Path(config_value["canonical"])
                ),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Ancient Indian History learner-v2 Topics 26-27",
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
    prior.DATE = DATE
    prior.ASCII_PATH = ASCII_PATH
    prior.TOPICS = TOPICS
    prior.PANEL_DATA = PANEL_DATA
    write_ascii_spec()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH]
    for config_value in TOPICS:
        key = str(config_value["key"])
        markdown = assemble(config_value)
        source_path = SESSION_DIR / f"{key}_Learning-Session.md"
        source_path.write_text(markdown, encoding="utf-8")
        graphical_path = prior.write_graphical_spec(config_value, markdown)
        generation_spec = prior.write_generation_spec(
            config_value,
            source_path,
            graphical_path,
        )
        written.extend([source_path, graphical_path, generation_spec])
    for path in written:
        print(prior.base.relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
