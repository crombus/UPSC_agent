"""Assemble Ancient History learner-v2 Topics 24-25 and authored visual specs."""

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
ASCII_PATH = ASCII_DIR / "ancient-indian-history-24-25-2026-08-30-sequential.json"


def topic(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    live_sources: list[str],
    current_note: str,
    practice_profile: str,
) -> dict[str, object]:
    value = prior.config(
        number,
        title,
        canonical,
        basic,
        advanced,
        live_sources,
        current_note,
        include_art_book=True,
    )
    value["practice_profile"] = practice_profile
    return value


TOPICS = [
    topic(
        24,
        "Developments in Philosophy",
        "24_Developments-in-Philosophy_Complete-Topic-Package.md",
        "24_Developments-in-Philosophy.md",
        "24_Developments-in-Philosophy.md",
        [
            "https://india.un.org/en/293100-unesco-adds-bhagavadg%C4%ABt%C4%81-and-n%C4%81%E1%B9%ADya%C5%9B%C4%81stra-memory-world-register",
            "https://culture.gov.in/events/ministry-culture-showcases-confluence-heritage-and-technology-india-ai-impact-summit-2026",
        ],
        "The UN India report on the April 2025 Memory of the World inscription "
        "of Bhagavadgita and Natyashastra manuscripts and the Ministry of "
        "Culture's February 2026 Gyan Bharatam update were rechecked on "
        "30 August 2026. They provide bounded manuscript-preservation, "
        "digitisation and access context; they do not establish ancient dates "
        "or settle philosophical interpretation.",
        "3 verified/routed/adjacent PYQs; 16 learning, 32 workbook and 12 "
        "remedial MCQs; 6 original solved Mains questions.",
    ),
    topic(
        25,
        "Cultural Interaction with Asian Countries",
        "25_Cultural-Interaction-with-Asian-Countries_Complete-Topic-Package.md",
        "25_Cultural-Interaction-with-Asia.md",
        "25_Cultural-Interaction-with-Asia.md",
        [
            "https://www.mea.gov.in/Portal/ForeignRelation/India-ASEAN-july-2025.pdf",
            "https://www.mea.gov.in/cultural-and-heritage-cooperation-in-development-projects",
        ],
        "The Ministry of External Affairs' July 2025 India-ASEAN brief and "
        "its cultural and heritage cooperation inventory were rechecked on "
        "30 August 2026. The 2025 ASEAN-India Year of Tourism and conservation "
        "work at Borobudur, Prambanan, My Son, Vat Phou and Cambodian temples "
        "supply modern diplomacy and conservation context only; they do not "
        "prove one-way ancient cultural ownership.",
        "7 verified/routed/adjacent/boundary PYQs; 16 learning, 24 practice "
        "and 8 remedial MCQs; 6 original solved Mains questions.",
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "ancient-indian-history-24": [
        (
            "Chronology and evidence discipline",
            "timeline",
            """VEDIC HORIZON -> rta, sacrifice, sacred speech and speculative hymns
EARLY UPANISHADS -> brahman, atman, karma, rebirth and moksha debates
6th-5th c. BCE -> second urbanisation and shramana challenges
EARLY HISTORIC -> sutra traditions and sharper school identities
2nd c. CE -> RS Sharma places Badarayana's Brahmasutra
EARLY MEDIEVAL -> commentary, logic and later doxographic ordering
RULE: date texts and school formation cautiously; use rival-source triangulation.""",
            ["Scope", "Chronology", "Evidence discipline"],
        ),
        (
            "An argumentative field, not one doctrine",
            "concept-map",
            """DARSHANA -> a viewpoint or way of seeing
ANVIKSIKI -> inquiry as a named knowledge branch
QUESTIONS -> What is real? How is knowledge valid? What binds? What liberates?
METHODS -> dialogue + aphorism + commentary + debate + disciplined practice
WORLDLY AIMS -> dharma + artha + kama
LIBERATION AIM -> moksha develops alongside worldly concerns
VERDICT: plurality and contest are structural, not later exceptions.""",
            ["Darshana", "Anviksiki", "Purusharthas"],
        ),
        (
            "Vedic to Upanishadic transition",
            "cause-mechanism-effect",
            """RTA / YAJNA / SACRED SPEECH
          |
speculative hymns question origin, order and knowledge
          |
Aranyakas and Upanishads interiorise ritual and stage dialogues
          |
BRAHMAN + ATMAN + KARMA + REBIRTH + RELEASE
CONTINUITY: inherited vocabulary and ritual setting
CHANGE: knowledge and self-inquiry gain sharper liberating force.""",
            ["Vedic background", "Upanishadic developments"],
        ),
        (
            "Shramana reconfiguration",
            "comparison",
            """CONTEXT -> towns + states + merchants + renouncers + debate
BUDDHISM -> conditioned arising, non-self, suffering and disciplined path
JAINISM -> jiva, karmic matter, many-sidedness and rigorous restraint
AJIVIKA -> niyati and ascetic discipline; mostly hostile external evidence
LOKAYATA -> materialist and sceptical critique; texts largely lost
COMMON MOVE -> challenge ritual monopoly and rethink action, bondage and release
LIMIT -> shramana schools disagreed profoundly with one another.""",
            ["Shramana milieu", "Buddhism", "Jainism", "Ajivikas", "Lokayata"],
        ),
        (
            "Buddhist philosophical development",
            "timeline",
            """EARLY CORE -> four truths + dependent arising + non-self
ABHIDHARMA -> analytical classification of experienced processes
MAHAYANA -> bodhisattva horizon and expanded textual worlds
MADHYAMAKA -> emptiness as dependent existence, not nihilism
YOGACARA -> analysis of cognition and representation
DIGNAGA TRADITION -> sharper Buddhist epistemology and logic
CAUTION: later developments must not be projected into the earliest canon.""",
            ["Early Buddhism", "Abhidharma", "Mahayana", "Madhyamaka", "Yogacara"],
        ),
        (
            "Jain, Ajivika and Charvaka evidence matrix",
            "evidence-matrix",
            """JAINA -> own canons + later texts | jiva, karma, anekanta, syadvada
AJIVIKA -> Buddhist/Jaina reports + archaeology | niyati; hostile-source problem
CHARVAKA -> opponents' summaries | perception and materialist criticism
ANEKANTAVADA -> reality has multiple aspects
SYADVADA -> conditional predication; not random indecision
HARD RULE -> secure core claim before later anecdote
VERDICT: source survival shapes how confidently each school can be reconstructed.""",
            ["Jain philosophy", "Ajivikas", "Charvaka", "Source criticism"],
        ),
        (
            "Astika, nastika and the six-school caveat",
            "classification",
            """ASTIKA / NASTIKA != simple believer / atheist
CLASSIFICATION AXES -> Vedic authority, other world and polemical usage
SIX LATER ORTHODOX PAIRINGS:
  Samkhya <-> Yoga
  Nyaya <-> Vaisheshika
  Mimamsa <-> Vedanta
OLDER TRADITIONS -> real; neat six-school canon -> later crystallisation
TRAP: do not make one timeless list govern every ancient century.""",
            ["Astika and nastika", "Six darshanas", "Doxography"],
        ),
        (
            "Samkhya and Yoga",
            "comparison",
            """SAMKHYA                         YOGA
purusha / prakriti             related metaphysical framework
three gunas                    disciplined transformation of mind
real evolution of prakriti     citta-vritti-nirodha
analytic tattva sequence       eight-limbed practice
discrimination liberates       disciplined insight liberates
LINK: conceptual analysis <-> practical discipline
CAUTION: historical layers complicate one fixed founder-date story.""",
            ["Samkhya", "Yoga", "Eight limbs"],
        ),
        (
            "Nyaya and Vaisheshika",
            "comparison",
            """NYAYA                           VAISHESHIKA
valid knowledge                categories and substances
perception + inference         atomistic analysis
comparison + testimony         qualities, motion and inherence
five-member inference          padartha classification
public reasoning               realist ontology
LINK: epistemic method <-> analysis of what exists
TRAP: Indian atomism is not identical to modern particle physics.""",
            ["Nyaya", "Vaisheshika", "Pramanas", "Atomism"],
        ),
        (
            "Mimamsa and early Vedanta",
            "comparison",
            """PURVA MIMAMSA                   UTTARA MIMAMSA / VEDANTA
Vedic injunction and dharma    Upanishads + Gita + Brahmasutra
ritual hermeneutics            brahman, self and liberation
language and duty              competing later interpretations
textual authority central      textual authority central
BOUNDARY: early core != Shankara/Ramanuja projected backward
VERDICT: shared canon can sustain sharply different philosophical projects.""",
            ["Mimamsa", "Early Vedanta", "Chronological boundaries"],
        ),
        (
            "Pramana and metaphysics comparison",
            "comparison-matrix",
            """KNOWLEDGE -> perception | inference | comparison | testimony | other debates
SELF -> enduring self | plural selves | no-self | material person
CAUSATION -> transformation | new production | dependent arising
REALITY -> substance/categories | process | non-dual readings | plural aspects
LIBERATION -> knowledge | discipline | duty | ethical restraint | path
METHOD -> compare schools on one axis at a time
TRAP: do not assign every pramana to every school.""",
            ["Epistemology", "Metaphysics", "Causation", "Liberation"],
        ),
        (
            "Institutions, language and answer spine",
            "answer-synthesis",
            """TRANSMISSION -> teacher lineages + monasteries + courts + debate halls
LANGUAGE -> Sanskrit + Pali + Prakrit + grammatical analysis
FORM -> sutra -> commentary -> counter-commentary
OPEN -> philosophy as a chronological, plural argumentative field
BODY -> Vedic/Upanishadic -> shramana -> darshana comparison
EVIDENCE -> named text or thinker + source limitation
CLOSE -> cumulative borrowing and contest, not spiritual homogeneity.""",
            ["Grammar and philosophy", "Institutions", "Answer architecture"],
        ),
    ],
    "ancient-indian-history-25": [
        (
            "Chronology, geography and evidence",
            "spatial-timeline",
            """3rd millennium BCE -> Harappan-West Asian commercial contact
3rd c. BCE setting -> Sri Lankan mission memory develops in later chronicles
EARLY CE -> Central Asian, Chinese and Southeast Asian links widen
3rd-6th c. CE -> Buddhist and Shaiva networks visible across several regions
7th c. onward -> Srivijaya and major trans-Asian monastic circuits
SOURCES -> inscriptions + texts + pilgrims + ports + monuments + objects
RULE: region-specific dates outrank one diffusion timeline.""",
            ["Scope", "Chronology", "Evidence discipline"],
        ),
        (
            "From Greater India to connected histories",
            "argument-tree",
            """OLDER MODEL -> Indianization / Greater India
USEFUL OBSERVATION -> real movement of scripts, religions and political idioms
CORE PROBLEM -> passive recipients + cultural ownership + empire-like language
CONNECTED MODEL:
  |-- transmission through routes and carriers
  |-- local selection and translation
  |-- hybrid form and new political meaning
  `-- return flows to Indian institutions
VERDICT: influence and Asian agency belong in the same sentence.""",
            ["Historiography", "Connected histories", "Localisation"],
        ),
        (
            "Route ecology",
            "network-map",
            """NORTH-WEST -> Gandhara -> Bactria -> oasis Silk Roads -> China
HIMALAYAN -> Kashmir / Nepal -> Tibet
BAY OF BENGAL -> east-coast ports -> Sri Lanka / Myanmar / Malay world
STRAITS -> Kedah / Srivijaya -> Java / South China Sea
ARABIAN SEA -> west-coast links and wider exchange
MECHANISM -> monsoon timing + ports + hinterlands + intermediaries
LIMIT: a route or port does not prove political control.""",
            ["Land routes", "Maritime routes", "Monsoon timing"],
        ),
        (
            "Carriers and media",
            "cultural-ecosystem",
            """PEOPLE -> merchants + monks + translators + diplomats + artisans
TEXTS -> sutras + chronicles + epics + legal and political vocabulary
OBJECTS -> relics + icons + manuscripts + coins + ritual goods
INSTITUTIONS -> monasteries + courts + ports + guilds + translation bureaux
POWER -> local rulers select portable idioms for local legitimacy
RETURN -> pilgrims, gifts and overseas endowments reshape Indian centres
RULE: identify carrier + route + institution + adapted outcome.""",
            ["Carriers", "Texts and objects", "Institutions"],
        ),
        (
            "Gandhara, Central Asia and China",
            "network-map",
            """INDIA <-> GANDHARA HYBRID ZONE <-> CENTRAL ASIAN OASES <-> CHINA
KUSHANA NETWORKS -> political and commercial connectivity
MONKS / MANUSCRIPTS -> Buddhist transmission across changing routes
TRANSLATION INSTITUTIONS -> Chinese conceptual remaking, not word substitution
FAXIAN / XUANZANG / YIJING -> journeys into India and evidence carried back
ART -> shared vocabulary changes by material, patron and region
VERDICT: transmission repeatedly created new local Buddhist worlds.""",
            ["Gandhara", "Central Asia", "China", "Pilgrims"],
        ),
        (
            "Tibet and Sri Lanka",
            "comparison",
            """TIBET                           SRI LANKA
Himalayan routes               maritime and short-sea routes
translation projects           Pali textual preservation
Indian teachers and texts      Mahavamsa mission tradition
monastic institutionalisation  relic, monastery and kingship links
local doctrinal development    Theravada consolidation and return influence
COMMON RULE: reception transformed what was received
SOURCE CAUTION: chronicle memory is not the same as contemporary inscription.""",
            ["Tibet", "Sri Lanka", "Chronicle memory"],
        ),
        (
            "Southeast Asian localisation",
            "comparison-matrix",
            """MYANMAR -> Pyu and later Buddhist networks
MAINLAND -> Dvaravati + Funan/Chenla + Champa + Khmer worlds
ISLAND -> Java + Sumatra + straits-centred Srivijaya
RELIGION -> Buddhist + Shaiva + Vaishnava idioms in different combinations
MONUMENTS -> Borobudur + Angkor + My Son; local plans and political meanings
POLITY -> Sanskritic titles and ritual adapted by Asian courts
LIMIT: shared vocabulary is not a map of Indian colonies.""",
            ["Mainland Southeast Asia", "Island Southeast Asia", "Localisation"],
        ),
        (
            "Scripts, Sanskrit and local languages",
            "process",
            """INDIC SCRIPT / LANGUAGE MODEL
              |
local scribes select signs, terms and formulae
              |
phonology + grammar + political needs reshape the model
              |
new regional inscriptions and literary cultures
SANSKRIT -> portable prestige idiom, not proof of ethnic replacement
VERNACULARS -> active partners in localisation and court communication.""",
            ["Scripts", "Sanskrit", "Epigraphy", "Local languages"],
        ),
        (
            "Religion, epics and performance",
            "cultural-ecosystem",
            """BUDDHISM -> relics + sangha + pilgrimage + translation
SHAIVA / VAISHNAVA -> temples + ritual specialists + royal legitimation
RAMAYANA / MAHABHARATA -> retelling in local languages and performance forms
LOCAL CULTS -> absorb, redirect and coexist with imported idioms
EPIC VARIANTS -> evidence of creative adaptation, not textual corruption
PLURALITY -> different traditions travel through overlapping networks
VERDICT: transmission succeeded through translation into local worlds.""",
            ["Religion across Asia", "Epics", "Performance"],
        ),
        (
            "Art and architecture: shared form, local work",
            "comparison",
            """GANDHARA -> hybrid frontier art, not merely Greek art abroad
BAMIYAN -> Central Asian Buddhist landscape and monumental scale
BOROBUDUR -> Javanese Buddhist monument with local spatial logic
ANGKOR -> Khmer political-sacred landscape
MY SON -> Cham Shaiva architecture and regional technique
METHOD -> form + material + patron + ritual + local environment
TRAP: resemblance alone cannot establish date, route or political domination.""",
            ["Art", "Architecture", "Local form"],
        ),
        (
            "Trade, political idioms and reciprocity",
            "cause-mechanism-effect",
            """GOODS + SHIPPING + PORT-HINTERLAND NETWORKS
                 |
merchants, guilds, monasteries and courts meet
                 |
titles + scripts + rituals + images gain political value
                 |
local rulers recast them for regional sovereignty
RETURN FLOW -> pilgrims + Pali preservation + overseas gifts to Nalanda
LIMIT: commerce enables contact but does not mechanically cause cultural change.""",
            ["Trade goods", "Kingship", "Return flows", "Nalanda-Srivijaya"],
        ),
        (
            "Connected-history answer spine",
            "answer-synthesis",
            """OPEN -> multi-directional interaction across land and sea
FRAME -> influence + localisation + reciprocity
MECHANISM -> route + carrier + institution
CASES -> Gandhara/China + Sri Lanka/Tibet + Southeast Asia
MATERIAL -> text + script + relic + monument + trade good
LIMIT -> uneven archives; no automatic conquest or ownership claim
CLOSE -> a connected Asian world that retained regional diversity.""",
            ["Historical significance", "Source method", "Answer architecture"],
        ),
    ],
}


def classify(key: str, title: str) -> str:
    basic_pattern = (
        r"^(?:0[1-9]|1\d|2[0-2])\."
        if key.endswith("-24")
        else r"^(?:0[1-9]|1[0-8])\."
    )
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if re.match(basic_pattern, title):
        return "basic"
    if title.startswith(
        (
            "Learning MCQ",
            "Workbook MCQ",
            "Practice MCQ",
            "Remedial MCQ",
            "Broad topic coverage MCQs",
            "Remedial MCQs for common confusions",
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
            "Original Mains Question",
            "Original solved Mains",
            "Workbook closing recap",
        )
    ):
        return "practice"
    if title.startswith(("Final consolidated register notes", "Final Register")):
        return "register"
    raise ValueError(f"Unclassified {key} section: {title}")


def assemble(config_value: dict[str, object]) -> str:
    canonical = Path(config_value["canonical"])
    source = canonical.read_text(encoding="utf-8")
    preamble, sections = prior.base.split_h2(source)
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    for title, fragment in sections:
        if (
            str(config_value["key"]) == "ancient-indian-history-24"
            and title.startswith("Adjacent PYQ 3")
            and "\n### Workbook MCQ 01" in fragment
        ):
            practice_fragment, workbook_fragment = fragment.split(
                "\n### Workbook MCQ 01",
                1,
            )
            grouped["practice"].append(
                prior.base.normalize_fragment(practice_fragment)
            )
            grouped["mcq"].append(
                prior.base.normalize_fragment(
                    "### Workbook MCQ 01" + workbook_fragment
                )
            )
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
        f"{prior.base.strip_title(preamble)}\n\n"
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
                "source_markdown": prior.base.relative(Path(config_value["canonical"])),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Ancient Indian History learner-v2 Topics 24-25",
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
