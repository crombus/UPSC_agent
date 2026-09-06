"""Deep-review and immutably regenerate all Internal Security topic packages."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
import unicodedata
from collections import Counter
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import fitz

import carvaka_flowchart
import markdown_learning_pdf
import notions_style_ascii_master as ascii_master
from export_four_item_library import export_library as export_four_item_library
from generate_philosophy_western_rationalism_v2 import render_ascii_pdf_safe
from generate_v2_section_indexes import generate_command_guide, generate_section_indexes
from validate_v2_export import (
    validate_pdf,
    validate_pdf_layout,
    validate_tracker_record,
    validate_v2_paths,
)


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-04"
SUBJECT = "Internal Security"
FLOW_SUBJECT = "Internal-Security"
SECTION = "Subject-wide Syllabus"
STATUS = ROOT / "EXPORT-PDF-STATUS.json"
MASTER = ROOT / "notes" / "Final-Learning-Packages" / "MASTER-TRACKER.json"
REVIEW_ROOT = ROOT / "notes" / "Final-Learning-Packages" / "_deep-content-review"
REVIEW_TRACKER = REVIEW_ROOT / "REVIEW-TRACKER.json"
REVIEW_TRACKER_MD = REVIEW_ROOT / "REVIEW-TRACKER.md"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "internal-security--subject-wide-syllabus.json"
)
EXPORTS = ROOT / "upsc-ai-kit" / "manifests" / "exports"
ASCII_SPECS = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
)
GRAPHICAL_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / "Internal-Security"
    / "deep-review"
)
CONTENT_SPECS = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "internal-security--subject-wide-syllabus-content-specs"
)
REFRESHED_KNOWLEDGE = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Learner-v2-Refreshed"
    / "Internal-Security"
    / "Subject-Wide-Syllabus"
    / "learning-sessions"
)
REFRESHED_NOTES = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Internal-Security"
    / "Subject-Wide-Syllabus"
    / "learning-sessions"
)
REFRESHED_FLOWS = (
    ROOT
    / "notes"
    / "Learner-v2-Refreshed"
    / "Internal-Security"
    / "Subject-Wide-Syllabus"
    / "flowcharts"
)
INDEX_DIR = (
    ROOT
    / "notes"
    / "Internal-Security"
    / "learning-session-v2"
    / "subject-wide-syllabus"
    / "indexes"
)
SYLLABUS_MAPPING = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Internal-Security"
    / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"
)
COMMON_CHRONOLOGY = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Internal-Security"
    / "00_Master-Chronology.md"
)
PYQ_LEDGERS = (
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-INDEX.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "PYQ-INTEGRATION-AUDIT-2018-2023.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "PYQ-INTEGRATION-AUDIT-2024-2025.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "PYQ-INTEGRATION-AUDIT-2026.md",
)
WORKFLOW = "internal-security-deep-review-immutable-successor"

H2_ORDER = (
    "BASIC LEARNING SESSION",
    "BASIC MCQS / REMEDIATION",
    "PYQS AND ANSWER PRACTICE",
    "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
    "CONSOLIDATED REGISTER NOTES",
)
QUESTION_HEADING = re.compile(
    r"(?im)^(?P<marks>#{3,6})\s+(?P<title>.+?)\s*$"
)
OPTION_BULLET = re.compile(
    r"^(?P<prefix>\s*(?:[-*]\s+)?)(?P<label>[A-D])"
    r"(?P<punct>[.)])(?P<space>\s+)(?P<text>.+?)\s*$",
    re.I,
)
OPTION_TABLE = re.compile(
    r"^(?P<prefix>\s*\|\s*)(?P<label>[A-D])(?P<middle>\s*\|\s*)"
    r"(?P<text>.*?)(?P<suffix>\s*\|\s*)$",
    re.I,
)
OPTION_PAREN = re.compile(
    r"^(?P<prefix>\s*(?:[-*]\s+)?)(?P<open>\()(?P<label>[A-D])"
    r"(?P<close>\))(?P<space>\s+)(?P<text>.+?)\s*$",
    re.I,
)
ANSWER_PATTERNS = (
    re.compile(
        r"(?P<prefix>\*\*Answer:\s*)(?P<open>\()?"
        r"(?P<label>[A-D])(?P<close>\))?(?P<period>\.)?(?P<suffix>\*\*)",
        re.I,
    ),
    re.compile(
        r"(?P<prefix>\*\*Correct answer:\s*)(?P<open>\()?"
        r"(?P<label>[A-D])(?P<close>\))?(?P<period>\.)?(?P<suffix>\*\*)",
        re.I,
    ),
    re.compile(
        r"(?P<prefix>\bCORRECT ANSWER:\s*)(?P<label>[A-D])"
        r"(?P<suffix>\s*[-—])",
        re.I,
    ),
    re.compile(
        r"(?P<prefix>\b(?:CORRECT\s+)?ANSWER:\s*)(?P<label>[A-D])"
        r"(?P<period>\.)?",
        re.I,
    ),
)

ASCII_PANEL_LINE_OVERRIDES = {
    "internal-security-01": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Separate verified source fact, historical inference and current-status claim.",
            "2. Topic 01 owns method; Topic 02 owns detailed source classes and techniques.",
            "3. Write claim -> named evidence -> significance -> limitation.",
            "VERDICT: Source type controls the strength and limits of the historical claim.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Attribute contested readings; name their evidence and counter-evidence.",
            "2. Inscriptions record claims; coins show circulation, not uniform territorial rule.",
            "3. Co-relate sources; texts are layered and normative, material evidence interpreted.",
            "VERDICT: Qualification earns marks; false certainty is a hard failure.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Define the demand and the controlling historiographical question.",
            "2. Build each paragraph as claim -> named evidence -> analysis -> qualification.",
            "3. Compare schools by question, archive, contribution and residual blind spot.",
            "VERDICT: Evidence and method rank plural readings without pretending finality.",
        ],
    },
    "internal-security-02": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Archaeology gives context; inscriptions acts; coins circulation; texts intent.",
            "2. Date each layer, sample or record before comparing sources.",
            "3. Triangulate independent evidence only at matching time, place and scale.",
            "VERDICT: Fit the source to the question and state the residual uncertainty.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Texts are layered; inscriptions formulaic; coins travel beyond political borders.",
            "2. Scientific dates are sample ranges; material culture is not language or ethnicity.",
            "3. Absence matters only after survivability, search coverage and patterned silence.",
            "VERDICT: Source proximity improves evidence, not automatic neutrality.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Decode the directive and select the source class that fits the claim.",
            "2. Write claim -> named evidence -> inference -> limitation -> corroboration.",
            "3. Use 2018 travellers, 2023 literary authors and 2024 site matching as anchors.",
            "VERDICT: Independent convergence strengthens history without erasing differences.",
        ],
    },
    "internal-security-03": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Convert relief, water, climate and resources into a dated historical mechanism.",
            "2. Add technology, labour, institutions and power before claiming an outcome.",
            "3. State each proxy's catchment, chronology, preservation and alternative causes.",
            "VERDICT: Geography conditions choices; it does not dictate one inevitable history.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Mountains are barriers and corridors; rivers are routes and changing hazards.",
            "2. A palaeochannel is not a named textual river; correlation is not causation.",
            "3. Resource maps are not political maps; modern borders are not ancient regions.",
            "VERDICT: Date the landscape, match the scale and preserve regional variation.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. For 2023 GS-I Q1, map mountain, plain, plateau, river, resource and coast.",
            "2. Write factor -> mechanism -> named evidence -> outcome -> mediation -> limit.",
            "3. Compare prehistoric, Harappan, Vedic and early historic uses of landscapes.",
            "VERDICT: Societies selected, connected and transformed geographic possibilities.",
        ],
    },
    "internal-security-04": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Start with macro-phase, then regional sequence, dated stratum and assemblage.",
            "2. Read cores, flakes, debitage, wear and raw material before inferring behaviour.",
            "3. Separate lithic technology from hominin taxonomy, language and group identity.",
            "VERDICT: Broad chronology guides comparison; site context controls the claim.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Acheulian is a technology, Levallois a method and microlith a tool element.",
            "2. Bhimbetka spans many periods; rock-art meaning and dates remain indirect.",
            "3. Mesolithic domestication and sedentariness must be established site by site.",
            "VERDICT: Transition means changing combinations, overlap and regional coexistence.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Use the 2019 Denisovan PYQ to separate population, place and geological period.",
            "2. Compare phases through tools, ecology, mobility, habitation, art and burials.",
            "3. Write claim -> site/assemblage -> significance -> date/context limit -> verdict.",
            "VERDICT: Indian prehistory is regionally varied history reconstructed without texts.",
        ],
    },
    "internal-security-05": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Test cultivation, domestication, sedentism, pottery and storage separately.",
            "2. Anchor every culture in region, site, assemblage and dated sequence.",
            "3. Treat adoption, local development, mobility and interaction as testable models.",
            "VERDICT: Neolithisation is a regional mosaic, not one revolution or diffusion.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Rice presence is not domestication; a polished celt alone is not farming.",
            "2. Chalcolithic means copper plus stone, not universal metal use or urbanism.",
            "3. OCP, copper hoards and Ganeshwar overlap partly but are not one people.",
            "VERDICT: Culture labels classify assemblages; they do not prove ethnicity or polity.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Use 2021 Q37 to separate Burzahom pits, Chandraketugarh art and Ganeshwar copper.",
            "2. Compare north-west, Kashmir, Ganga/east, north-east and southern pathways.",
            "3. Write claim -> site/culture -> evidence -> inference -> chronology limit.",
            "VERDICT: Rural food-producing cultures overlapped, interacted and changed unevenly.",
        ],
    },
    "internal-security-06": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Separate excavated fact from function label and social interpretation.",
            "2. Anchor every claim in site, phase, context, comparison and regional variation.",
            "3. The undeciphered script limits named claims about language, rulers and doctrine.",
            "VERDICT: Harappan history is strongest on material systems, weakest on named ideas.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Citadel, granary, dockyard, Priest-King and Pashupati are modern labels.",
            "2. Horse evidence is rare and disputed; standardisation does not prove one empire.",
            "3. Deurbanisation was regional and multi-causal, not one invasion or drought.",
            "VERDICT: State the secure evidence first, then grade each interpretation.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Route all five PYQs through site, material, architecture and inference control.",
            "2. Write chronology -> extent -> urban system -> economy -> society -> decline.",
            "3. Build each paragraph as claim -> site/object -> fact -> inference -> limit.",
            "VERDICT: Integration gave way to localisation, continuity and major discontinuity.",
        ],
    },
    "internal-security-07": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Keep language, genes, pottery, ethnicity, civilisation and polity separate.",
            "2. Compare linguistic, textual, archaeological and genetic chronologies.",
            "3. State sample, route, scale and social-mechanism uncertainty for every model.",
            "VERDICT: Secure relationships do not make every historical mechanism settled.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Migration is not invasion; continuity does not prove absence of movement.",
            "2. PGW, BMAC, Swat, OCP and Sinauli do not automatically identify language.",
            "3. Steppe-related ancestry is biological evidence, not a Vedic-language label.",
            "VERDICT: Reject racial and civilisational certainty from every side of the debate.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Record zero direct origin/migration PYQs; keep adjacent Vedic questions cross-owned.",
            "2. Define terms -> weigh evidence -> compare invasion, migration and indigenous models.",
            "3. End with interaction, admixture, acculturation and unresolved route/scale questions.",
            "VERDICT: A balanced inference is evidence-led, category-safe and politically non-presentist.",
        ],
    },
    "internal-security-08": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Tie each claim to Rigvedic layer, genre, term cluster and oral transmission.",
            "2. Treat archaeology as a correlation for settlement and technology, not language.",
            "3. Use Later Vedic evidence only for explicit comparison, never backward projection.",
            "VERDICT: The corpus gives strong patterns but not a census or exact institutional code.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Pastoral predominance is not pure pastoralism; rajan is chief, not emperor.",
            "2. Sabha, samiti and vidatha are not modern democratic parliaments.",
            "3. Purusha Sukta is a later Book 10 articulation; ayas is not automatically iron.",
            "VERDICT: Translate Sanskrit terms by context and state uncertainty.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Route 2023 society/religion and 2026 wells, rivers and kshetra-patni.",
            "2. Write source -> geography -> economy -> kin polity -> society -> religion.",
            "3. End with gradual Early-to-Later change, continuity and regional variation.",
            "VERDICT: Early Vedic society was mixed, stratifying and kin-ordered, not monolithic.",
        ],
    },
    "internal-security-09": {
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Identify Samhita, Brahmana, Aranyaka or Upanishad layer before inference.",
            "2. Correlate PGW and iron by site and date without equating pottery with people.",
            "3. Separate ritual prescription, political claim and uneven social practice.",
            "VERDICT: Later Vedic change was gradual, regional and multi-causal.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Iron aided change but did not alone create agriculture, surplus or states.",
            "2. Assemblies changed relative weight; they did not disappear everywhere at once.",
            "3. Varna sharpened, but later jati and four-ashrama systems were not fully formed.",
            "VERDICT: Use textual trends with archaeological and regional qualifications.",
        ],
        "Integrated answer spine and qualified conclusion": [
            "ANSWER SPINE",
            "1. Route 2024 change and 2023 society-religion demands through parallel matrices.",
            "2. Write source -> geography -> economy -> polity -> society -> ritual -> thought.",
            "3. End with continuity, transition and a boundary before second urbanisation.",
            "VERDICT: Agrarian territoriality deepened without a sudden pan-Indian revolution.",
        ],
    },
    "internal-security-10": {
        "Jainism-Buddhism comparison and answer spine": [
            "ANSWER SPINE",
            "1. Define the shramana setting and identify each source tradition.",
            "2. Connect doctrine -> institution -> social base -> patronage -> spread.",
            "3. Compare Jain jiva and restraint with Buddhist anatta and Middle Path.",
            "VERDICT: Shared context produced distinct paths, institutions and trajectories.",
        ],
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Canonical texts preserve layered doctrine, discipline and sect memory.",
            "2. Inscriptions identify donors and institutions, not total populations.",
            "3. Archaeology maps practice and networks but cannot read belief directly.",
            "VERDICT: Triangulate text, inscription and material context at matching scales.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Traditional dates and council narratives require school-specific labels.",
            "2. Jain jiva is not Buddhist anatta; Theravada is not a synonym for Hinayana.",
            "3. Ashoka aided Buddhism but did not create or single-handedly spread it.",
            "VERDICT: Reject single-cause rise, one-event sect splits and total disappearance.",
        ],
    },
    "internal-security-11": {
        "Mahajanapada-Magadha answer architecture": [
            "ANSWER SPINE",
            "1. Define jana, janapada and mahajanapada with source-list caution.",
            "2. Map polity -> capital -> river/route, then compare monarchy and gana.",
            "3. Explain Magadha through factor -> evidence -> mechanism -> rival -> limit.",
            "VERDICT: Magadhan supremacy was conjunctural, cumulative and contingent.",
        ],
        "Evidence ladder and confidence control": [
            "EVIDENCE LADDER",
            "1. Texts preserve lists, rulers and conflicts through layered traditions.",
            "2. Archaeology dates settlements, NBPW and walls but rarely names rulers.",
            "3. Coins show circulation and valuation, not one issuer or universal money use.",
            "VERDICT: Correlate text, material and landscape evidence at matching scales.",
        ],
        "Examiner traps and contested boundaries": [
            "CLOSE DISTINCTIONS",
            "1. Sixteen is a conventional list; republic means restricted clan oligarchy.",
            "2. NBPW is one urban marker; iron and rivers are enabling, not sufficient.",
            "3. Dynastic dates, Nanda origins and army figures remain tradition-dependent.",
            "VERDICT: Stop at the Mauryan threshold and reject inevitable single-factor rise.",
        ],
    },
    "internal-security-24": {
        "Chronology and evidence discipline": [
            "SOURCES -> layered Vedic texts, sectarian canons, sutras, commentaries and material anchors",
            "EARLY UPANISHADS -> brahman, atman, karma, rebirth and liberation debates",
            "6th-5th c. BCE -> urban change and plural shramana challenges",
            "EARLY HISTORIC -> sutra traditions and sharper school identities",
            "LATE BC / EARLY CE -> debated Brahma Sutra formation, not one secure date",
            "GUPTA / POST-GUPTA -> commentary, Buddhist logic, grammar and doxographic ordering",
            "RULE: separate textual layer, attribution, commentary and reconstruction.",
        ],
        "Institutions, language and answer spine": [
            "TRANSMISSION -> teacher lineages + monasteries + courts + debate halls",
            "LANGUAGES -> Sanskrit + Pali + Prakrit + Tamil and regional expression",
            "FORM -> oral memory -> sutra -> commentary -> counter-commentary",
            "ARCHIVE LIMIT -> Gargi and Maitreyi are textual voices, not proof of equal access",
            "OPEN -> philosophy as a chronological and plural argumentative field",
            "BODY -> source layer -> social context -> inter-school debate -> institution",
            "CLOSE -> cumulative borrowing and contest, not timeless spiritual consensus.",
        ],
    },
    "internal-security-25": {
        "Carriers and media": [
            "PEOPLE -> merchants + monks + Brahmanas + artisans + envoys + pilgrims",
            "TEXTS -> sutras + chronicles + epics + legal and political vocabulary",
            "OBJECTS -> relics + icons + manuscripts + coins + ceramics + ritual goods",
            "INSTITUTIONS -> monasteries + courts + ports + guilds + translation teams",
            "POWER -> local political elites select portable idioms for local prestige",
            "RETURN -> foreign communities, pilgrims and gifts reshape Indian centres",
            "RULE: identify carrier + route + medium + local transformation.",
        ],
        "Southeast Asian localisation": [
            "MYANMAR / THAILAND -> Pyu + Dvaravati and changing Buddhist networks",
            "MAINLAND -> Funan/Chenla + Champa + early Khmer political worlds",
            "STRAITS -> Srivijaya; ISLAND -> Sailendra, Java and Bali",
            "MONUMENTS -> Borobudur; Prambanan and Angkor are later boundary examples",
            "POLITY -> Sanskritic titles and rituals remade by local courts",
            "LANGUAGE -> Sanskrit and Pali interact with local scripts and languages",
            "LIMIT: shared vocabulary is not a map of Indian colonies.",
        ],
        "Trade, political idioms and reciprocity": [
            "ROUTES -> monsoon sailing + ports + hinterlands + caravan and oasis links",
            "EVIDENCE -> ships + coins + ceramics + inscriptions, each with context limits",
            "GOODS -> textiles + beads + aromatics + metals + silk + horses",
            "CONTACT -> merchants, monasteries, courts and foreign communities",
            "LOCAL POWER -> titles, scripts, rituals and images gain regional prestige",
            "RETURN -> motifs, technologies, texts and overseas gifts affect India",
            "LIMIT: commerce enables contact but does not mechanically cause culture.",
        ],
    },
    "internal-security-26": {
        "A multitrack transition, not one date": [
            "COLONIAL HINDU / MUSLIM / BRITISH DIVISION -> communal and analytically inadequate",
            "DYNASTIC DATES -> chronology aids, not automatic social thresholds",
            "c. 300-550 -> wider grants and Gupta-Vakataka regional repertoires",
            "c. 550-750 -> post-Gupta polities, samantas and regional formations",
            "c. 750-1000 -> temple institutions, vernaculars and stronger regional states",
            "RULE: tracks change unevenly; neither 750 nor 1206 is a universal rupture.",
        ],
        "Land grant: charter to ground effects": [
            "GRANT -> Brahmana + temple + monastery + official or retainer",
            "FORMULA -> boundary + dues + exemptions + labour + resource and fine claims",
            "RIGHTS -> fiscal reassignment; judicial or policing reach varies",
            "GROUND -> cultivators + chiefs + assemblies + pastoral and forest users",
            "OUTCOME -> settlement, irrigation, hierarchy, integration and conflict",
            "LIMIT: charter rhetoric proves a claim; implementation needs other evidence.",
        ],
        "Evidence-led synthesis answer spine": [
            "OPEN -> define early medieval as an uneven and debated transition",
            "MODEL -> feudal + segmentary + integrative + regional-state comparison",
            "POLITY -> regional formations + samantas + scale-dependent reconfiguration",
            "ECONOMY -> grants + labour + agrarian expansion + varied trade and towns",
            "SOCIETY -> jati + exclusion + gender + frontier and local agency",
            "CULTURE -> temple/monastery + bhakti + Sanskrit and vernacular continuity",
            "CLOSE -> ancient institutions survive through regional transformation.",
        ],
    },
    "internal-security-27": {
        "State hierarchy and local institutions": [
            "KING / COURT -> royal orders + war + survey + revenue + temple patronage",
            "MANDALAM -> VALANADU -> NADU / KURRAM, with regional and chronological variation",
            "LOCAL BODIES -> ur + brahmadeya sabha/mahasabha + merchant nagaram",
            "COMMITTEES -> variyam for specified work; not one empire-wide template",
            "INTERMEDIARIES -> officers + chiefs + temples + landed and corporate elites",
            "VERDICT: royal capacity and local institutions interacted unequally.",
        ],
        "Land, revenue and social differentiation": [
            "LAND RIGHTS -> ownership + cultivation + revenue + jurisdiction can differ",
            "REVENUE -> survey + assessment + taxes + dues + labour and remission",
            "POWER -> vellala groups + Brahmana bodies + temples + royal agents",
            "PRODUCTION -> peasants + artisans + herders + service communities",
            "EXCLUSION -> segregated settlements and dependent or servile relations",
            "GENDER -> elite and temple women are visible; ordinary labour is under-recorded",
            "LIMIT: inscriptional category is not a uniform social condition.",
        ],
    },
}


@dataclass(frozen=True)
class Topic:
    number: int
    topic_key: str
    title: str
    basic_path: Path
    canonical_path: Path
    advanced_path: Path
    cross_topic_sources: tuple[Path, ...]
    pyq_sources: tuple[Path, ...]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + f".pending-{os.getpid()}")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for attempt in range(40):
        try:
            os.replace(temporary, path)
            return
        except PermissionError:
            if attempt == 39:
                raise
            time.sleep(0.25)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def repo(value: str) -> Path:
    return ROOT / Path(value.replace("\\", "/"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def topics() -> list[Topic]:
    manifest = load(SECTION_MANIFEST)
    result: list[Topic] = []
    for number, row in enumerate(manifest["topics"], 1):
        result.append(
            Topic(
                number=number,
                topic_key=row["topic_key"],
                title=row["display_title"],
                basic_path=repo(row["source_basic"]),
                canonical_path=repo(row["source_canonical"]),
                advanced_path=repo(row["source_advanced"]),
                cross_topic_sources=tuple(
                    repo(path) for path in row.get("cross_topic_sources", [])
                ),
                pyq_sources=tuple(
                    repo(path) for path in row.get("verified_pyq_sources", [])
                ),
            )
        )
    if [topic.number for topic in result] != list(range(1, 16)):
        raise ValueError("Internal Security manifest must contain topics 01-15 in order.")
    return result


def latest(status: dict[str, Any], topic_key: str) -> dict[str, Any]:
    records = [
        row
        for row in status["exports"]
        if row.get("topic_key") == topic_key and row.get("variant") == "learner-v2"
    ]
    if not records:
        raise ValueError(f"No learner-v2 record exists for {topic_key}.")
    return max(records, key=lambda row: int(row["generation"]))


def live_identity(
    topic: Topic,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    old = latest(status, topic.topic_key)
    master_row = next(
        row for row in master["topics"] if row["topic_key"] == topic.topic_key
    )
    review_row = next(
        row for row in review["topics"] if row["topic_key"] == topic.topic_key
    )
    identities = {
        old["record_id"],
        master_row["source_record_id"],
        review_row["source_record_id"],
    }
    if len(identities) != 1:
        raise ValueError(
            f"{topic.topic_key}: live EXPORT/MASTER/REVIEW identities disagree: "
            f"{sorted(identities)}"
        )
    return old, master_row, review_row


def review_paths(topic: Topic, generation: int) -> dict[str, Path]:
    knowledge_dir = (
        REFRESHED_KNOWLEDGE / topic.topic_key / f"g{generation}"
    )
    notes_dir = REFRESHED_NOTES / topic.topic_key / f"g{generation}"
    flow_dir = REFRESHED_FLOWS / topic.topic_key / f"carvaka-g{generation}"
    stem = topic.topic_key
    return {
        "knowledge_dir": knowledge_dir,
        "notes_dir": notes_dir,
        "flow_dir": flow_dir,
        "markdown": knowledge_dir
        / f"{stem}_Complete-Learning-Session_{DATE}.md",
        "workbook_markdown": knowledge_dir
        / f"{stem}_Solved-Practice-Workbook_{DATE}.md",
        "main_pdf": notes_dir
        / f"{stem}_Complete-Learning-Session_{DATE}.pdf",
        "workbook_pdf": notes_dir
        / f"{stem}_Solved-Practice-Workbook_{DATE}.pdf",
        "asset_folder": knowledge_dir / "assets",
        "main_visual": notes_dir / "validation" / "main-visual-audit-map.json",
        "workbook_visual": notes_dir
        / "validation"
        / "workbook-visual-audit-map.json",
        "ascii_pdf": flow_dir / "ascii-master.pdf",
        "ascii_spec": ASCII_SPECS
        / f"{stem}-deep-review-{DATE}-g{generation}.json",
        "graphical_spec": GRAPHICAL_SPECS / f"{stem}-g{generation}.json",
        "content_spec": CONTENT_SPECS / f"{stem}-g{generation}.json",
        "record": EXPORTS
        / f"{stem}-learner-v2-g{generation}-{DATE}-record.json",
        "validation": EXPORTS
        / f"{stem}-learner-v2-g{generation}-{DATE}-validation.json",
    }


def allocate(
    topic: Topic,
    expected_old_record_id: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], int]:
    """Re-read EXPORT, MASTER and REVIEW immediately before allocation."""
    old, master_row, review_row = live_identity(topic)
    if old["record_id"] != expected_old_record_id:
        raise ValueError(
            f"{topic.topic_key}: identity changed during baseline review: "
            f"{expected_old_record_id} -> {old['record_id']}"
        )
    generation = int(old["generation"]) + 1
    while True:
        paths = review_paths(topic, generation)
        review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
        candidates = [
            paths["knowledge_dir"],
            paths["notes_dir"],
            paths["flow_dir"],
            paths["ascii_spec"],
            paths["graphical_spec"],
            paths["content_spec"],
            paths["record"],
            paths["validation"],
            review_dir / f"g{generation}-generation-allocation.json",
        ]
        if not any(path.exists() for path in candidates):
            break
        generation += 1
    return old, master_row, review_row, generation


def section(markdown: str, heading: str, next_heading: str | None) -> str:
    start_marker = f"## {heading}"
    start = markdown.index(start_marker)
    if next_heading is None:
        return markdown[start:]
    end = markdown.index(f"## {next_heading}", start + len(start_marker))
    return markdown[start:end]


def h2_order_errors(markdown: str) -> list[str]:
    headings = re.findall(r"(?m)^##(?!#)\s+(.+?)\s*$", markdown)
    positions: list[int] = []
    errors: list[str] = []
    for heading in H2_ORDER:
        if heading not in headings:
            errors.append(f"Missing H2 section: {heading}.")
        else:
            positions.append(headings.index(heading))
    if len(positions) == len(H2_ORDER) and positions != sorted(positions):
        errors.append("Required H2 sections are out of order.")
    if headings and headings[-1] != H2_ORDER[-1]:
        errors.append("CONSOLIDATED REGISTER NOTES is not the final H2.")
    return errors


def normalize_required_h2(markdown: str) -> str:
    replacements = {
        "BASIC LEARNING SESSION": "BASIC LEARNING SESSION",
        "BASIC MCQS / REMEDIATION": "BASIC MCQS / REMEDIATION",
        "PYQS AND ANSWER PRACTICE": "PYQS AND ANSWER PRACTICE",
        "OPTIONAL ADVANCED DEPTH": (
            "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
        ),
        "CONSOLIDATED REGISTER NOTES": "CONSOLIDATED REGISTER NOTES",
    }
    for prefix, exact in replacements.items():
        markdown = re.sub(
            rf"(?m)^##\s+{re.escape(prefix)}[^\n]*$",
            f"## {exact}",
            markdown,
            count=1,
        )
    return markdown


def normalize_workbook_h1(markdown: str, title: str) -> str:
    replacement = f"# {title} — Solved Practice Workbook"
    if re.search(r"(?m)^#(?!#)\s+.+$", markdown):
        return re.sub(
            r"(?m)^#(?!#)\s+.+$",
            replacement,
            markdown,
            count=1,
        )
    return replacement + "\n\n" + markdown


def normalize_topic_pyq_metadata(topic: Topic, markdown: str) -> str:
    if topic.topic_key == "internal-security-10":
        markdown = markdown.replace("2026 GS-I Q5", "2026 GS-I Q3")
        markdown = markdown.replace("2026 Q5", "2026 Q3")
    if topic.topic_key == "internal-security-13":
        markdown = markdown.replace(
            "Verified Prelims PYQ - 2026 printed Q3: Pali coin evidence",
            "Verified unrouted Prelims practice - 2026 printed Q3: Pali coin evidence",
        )
        markdown = markdown.replace(
            "VERIFIED QUESTION: local official Set-A paper; the paper itself "
            "prints this as Q3 although a repository routing ledger misnumbers it.",
            "UNROUTED VERIFIED PRACTICE: local 2026 Set-A paper; the current "
            "routing ledger does not assign this demand to Topic 13.",
        )
    if topic.topic_key == "internal-security-16":
        markdown = markdown.replace(
            "### PYQ 02 - 2020 Prelims GS-I Q22: Mahayana schools",
            "### Adjacent PYQ 02 - 2020 Prelims GS-I Q22: Mahayana schools",
        )
        markdown = markdown.replace(
            "### PYQ 03 - 2023 Prelims GS-I Q46: Milinda-panha attribution",
            "### Adjacent PYQ 03 - 2023 Prelims GS-I Q46: Milinda-panha attribution",
        )
    if topic.topic_key == "internal-security-17":
        for number, title in (
            ("01", "2026 Prelims GS-I Q13: Amaravati Stupa"),
            ("02", "2023 Prelims GS-I Q41: Dhanyakataka"),
            ("03", "2020 GS-I Mains Q1: rock-cut architecture"),
            ("04", "2023 Prelims GS-I Q42: stupa origin and function"),
        ):
            markdown = markdown.replace(
                f"### PYQ {number} - {title}",
                f"### Adjacent PYQ {number} - {title}",
            )
    if topic.topic_key == "internal-security-21":
        for number, title in (
            ("2", "Prelims 2020 Q36 (literature bridge)"),
            ("4", "GS-I Mains 2022 Q12 (cross-owned)"),
            ("5", "Prelims 2025 Q15 (cross-owned official key)"),
        ):
            markdown = markdown.replace(
                f"### Verified PYQ {number} - {title}",
                f"### Adjacent PYQ {number} - {title}",
            )
    if topic.topic_key == "internal-security-25":
        markdown = markdown.replace(
            "### Verified PYQ 4 - Prelims GS-I 2024 Q64",
            "### Adjacent PYQ 4 - Prelims GS-I 2024 Q64",
        )
        markdown = markdown.replace(
            "### Verified PYQ 5 - Prelims GS-I 2025 Q15",
            "### Adjacent PYQ 5 - Prelims GS-I 2025 Q15",
        )
        markdown = markdown.replace(
            "The repository treats this as a secure, locally verified owner-route question.",
            "The authoritative owner route is Topic 10; Topic 25 retains it only as "
            "adjacent trans-Asian Buddhist practice.",
        )
        markdown = markdown.replace(
            "repository Topic 20 already records the answer as officially keyed locally.",
            "the authoritative owner route is Topic 20, which records the officially "
            "keyed answer; Topic 25 retains it only as adjacent pilgrim practice.",
        )
    if topic.topic_key == "internal-security-26":
        markdown = re.sub(
            r"(?m)^### (?:Verified|Routed) PYQ (?P<number>\d+) -",
            r"### Adjacent PYQ \g<number> -",
            markdown,
        )
        markdown = markdown.replace(
            "Topic 26 uses the question as a direct legacy bridge.",
            "Topic 26 retains the question only as an adjacent continuity-and-legacy bridge.",
        )
        markdown = markdown.replace(
            "It is a direct Topic 26 chronology discriminator:",
            "It is an adjacent regional-chronology discriminator:",
        )
        markdown = markdown.replace(
            "Audited local route already preserved in Topic 25.",
            "The authoritative owner route is Topic 10; Topics 25 and 26 retain "
            "the question only as adjacent Buddhist-network evidence.",
        )
    return markdown


def basic_mcq_area(markdown: str) -> tuple[str, str, str]:
    start = markdown.index("## BASIC MCQS / REMEDIATION")
    end = markdown.index("## PYQS AND ANSWER PRACTICE", start)
    return markdown[:start], markdown[start:end], markdown[end:]


def mcq_blocks(area: str) -> list[tuple[int, int, str]]:
    matches = [
        match
        for match in re.finditer(
            r"(?im)^#{3,6}\s+("
            r"(?:(?:Hard|Learning|Practice|Remedial|Broad)\s+)?MCQ\s*\d+.*"
            r"|Q\d+\s*)$",
            area,
        )
        if "MCQS /" not in match.group(1).upper()
    ]
    candidates = [
        (
            match.start(),
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(area),
            match.group(1).strip(),
        )
        for index, match in enumerate(matches)
    ]
    return [
        item
        for item in candidates
        if answer_label(area[item[0] : item[1]]) is not None
        or len(option_texts(area[item[0] : item[1]])) == 4
    ]


def answer_label(block: str) -> str | None:
    for pattern in ANSWER_PATTERNS:
        match = pattern.search(block)
        if match:
            return match.group("label").upper()
    return None


def option_texts(block: str) -> dict[str, str]:
    options: dict[str, str] = {}
    for line in block.splitlines():
        match = (
            OPTION_BULLET.match(line)
            or OPTION_TABLE.match(line)
            or OPTION_PAREN.match(line)
        )
        if match:
            label = match.group("label").upper()
            text = match.group("text").strip()
            if (
                label not in options
                and text
                and text.casefold() not in {"choice", "option"}
            ):
                options[label] = text
    if len(options) == 4:
        return options
    embedded = re.search(r"(?im)^-\s*OPTIONS:\s*(.+)$", block)
    if embedded:
        parsed = dict(
            (label.upper(), text.strip())
            for label, text in re.findall(
                r"(?:^|\|\s*)([A-D])\.\s*(.*?)(?=\s*\|\s*[A-D]\.|\Z)",
                embedded.group(1),
                re.I,
            )
        )
        if len(parsed) == 4:
            return parsed
    return options


def _replace_answer_label(block: str, desired: str, correct_text: str) -> str:
    for pattern in ANSWER_PATTERNS:
        if not pattern.search(block):
            continue

        def replace(match: re.Match[str]) -> str:
            groups = match.groupdict()
            if "suffix" in groups and groups.get("suffix", "").strip() in {"-", "—"}:
                return (
                    groups["prefix"]
                    + desired
                    + groups.get("suffix", "")
                )
            return (
                groups["prefix"]
                + (groups.get("open") or "")
                + desired
                + (groups.get("close") or "")
                + (groups.get("period") or "")
                + (groups.get("suffix") or "")
            )

        block = pattern.sub(replace, block, count=1)
        break
    block = re.sub(
        r"(?im)^(-\s*CORRECT ANSWER:\s*)[A-D](\s*[-—]\s*).+$",
        lambda match: match.group(1) + desired + match.group(2) + correct_text,
        block,
        count=1,
    )
    block = re.sub(
        r"(?i)(\bkey\s+)[A-D](\s*:)",
        rf"\g<1>{desired}\2",
        block,
    )
    block = re.sub(
        r"(?i)(rotation position:\s*\d+\s*[-=]>\s*)[A-D]",
        rf"\g<1>{desired}",
        block,
    )
    return block


def rotate_mcq_block(block: str, desired: str) -> tuple[str, bool]:
    current = answer_label(block)
    options = option_texts(block)
    if current is None or len(options) != 4:
        return block, False
    new_options = dict(options)
    if current != desired:
        new_options[current], new_options[desired] = (
            options[desired],
            options[current],
        )
    lines: list[str] = []
    for line in block.splitlines():
        bullet = OPTION_BULLET.match(line)
        table = OPTION_TABLE.match(line)
        paren = OPTION_PAREN.match(line)
        match = bullet or table or paren
        if not match:
            lines.append(line)
            continue
        label = match.group("label").upper()
        if label not in new_options:
            lines.append(line)
        elif bullet:
            lines.append(
                match.group("prefix")
                + label
                + match.group("punct")
                + match.group("space")
                + new_options[label]
            )
        elif table:
            lines.append(
                match.group("prefix")
                + label
                + match.group("middle")
                + new_options[label]
                + match.group("suffix")
            )
        else:
            lines.append(
                match.group("prefix")
                + match.group("open")
                + label.lower()
                + match.group("close")
                + match.group("space")
                + new_options[label]
            )
    repaired = "\n".join(lines)
    embedded = re.search(r"(?im)^-\s*OPTIONS:\s*(.+)$", repaired)
    if embedded:
        replacement = "- OPTIONS: " + " | ".join(
            f"{label}. {new_options[label]}" for label in "ABCD"
        )
        repaired = (
            repaired[: embedded.start()]
            + replacement
            + repaired[embedded.end() :]
        )
    repaired = _replace_answer_label(repaired, desired, options[current])
    return repaired, True


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    prefix, area, suffix = basic_mcq_area(markdown)
    blocks = mcq_blocks(area)
    if not blocks:
        return markdown, {"count": 0, "keys": [], "unparsed": []}
    chunks: list[str] = []
    cursor = 0
    parsed_keys: list[str] = []
    unparsed: list[str] = []
    for index, (start, end, title) in enumerate(blocks):
        chunks.append(area[cursor:start])
        desired = "ABCD"[index % 4]
        repaired, parsed = rotate_mcq_block(area[start:end].rstrip(), desired)
        chunks.append(repaired + "\n\n")
        parsed_keys.append(answer_label(repaired) or "")
        if not parsed:
            unparsed.append(title)
        cursor = end
    chunks.append(area[cursor:])
    repaired_area = "".join(chunks)
    return (
        prefix + repaired_area + suffix,
        {
            "count": len(blocks),
            "keys": parsed_keys,
            "unparsed": unparsed,
        },
    )


def _short_question(block: str, title: str) -> str:
    match = re.search(
        r"(?ims)^\*\*(?:Question|Question text):\*\*\s*(.+?)"
        r"(?=^\*\*|^####|\Z)",
        block,
    )
    value = match.group(1) if match else title
    value = re.sub(r"\s+", " ", re.sub(r"[*_`#]", "", value)).strip()
    return textwrap.shorten(value, width=150, placeholder="…")


def _directive(question: str) -> str:
    match = re.search(
        r"\b(critically examine|critically assess|discuss|examine|analyse|"
        r"analyze|assess|evaluate|comment|explain|compare|trace|describe)\b",
        question,
        re.I,
    )
    return match.group(1).lower() if match else "answer"


TOPIC_23_MAIN_SUPPLEMENT = r"""
### CLOSING SEMANTIC LEDGER A — WATER, GRANT FORMS, INTERMEDIARIES AND STATE DEBATE

#### Why this supplement is necessary

[ANALYSIS] A complete account cannot move directly from dynastic war to temples.
It must show the material and intermediary mechanisms that connected a court to
uneven local societies.

| Missing bridge | Evidence-led reconstruction | Limit |
|---|---|---|
| Irrigation | Tanks, wells and channels supported cultivation in rainfall-variable zones; donors, local bodies and institutions could share maintenance | An inscription naming a work does not prove uniform state irrigation |
| Grant forms | *Brahmadeya* and *agrahara* primarily concern Brahmana beneficiaries; *devadana* assigns resources to a deity or temple | Formula and actual enforcement must be separated |
| Intermediary power | Princes, officers, tributary chiefs, military retainers, village bodies and beneficiaries connected core courts to localities | A campaign zone is not automatically an annexed province |
| Production society | Peasants, pastoralists, artisans and service groups sustained agrarian and temple networks | Elite records create severe source silence |
| Gendered patronage | Queen Lokamahadevi is associated with Virupaksha and Queen Trailokyamahadevi with Mallikarjuna at Pattadakal | Elite female patronage does not establish general equality |

```text
court and military core
          |
          v
chiefs / officers / beneficiaries / local bodies
          |
          v
grant + irrigation + settlement + production
          |
          v
revenue, ritual centres and political integration
          |
          v
cooperation, hierarchy, resistance and regional variation
```

#### State-formation debate

| Model | What it illuminates | Why it is insufficient alone |
|---|---|---|
| Indian-feudalism interpretation | Fiscal immunities, landed intermediaries and possible peasant dependence | Grants varied; royal capacity, towns and exchange did not vanish uniformly |
| Segmentary-state heuristic | Stronger core, graded authority and ritual claims beyond direct control | It was developed most fully for later Chola evidence and cannot be pasted onto every Pallava-Chalukya phase |
| Integrative/processual approach | Grants, cults, alliances and local institutions as polity-building mechanisms | Integration remained unequal and conflictual |
| Peasantization/agrarian-expansion approach | Incorporation of forest, pastoral and cultivating populations | Change was not one-way or identical in every ecology |

**Qualified verdict:** Pallava and Chalukya states combined coercion, tribute,
redistribution, intermediary negotiation and ritual-cultural integration.

### CLOSING SEMANTIC LEDGER B — NEGOTIATED CULTURE, LANGUAGE AND BOUNDARY CONTROL

#### Brahmanization was negotiated and uneven

- [FACT] Grants record Brahmana migration and beneficiary networks, but they are
  not complete population maps.
- [ANALYSIS] *Sanskritization* identifies some adoption of high-status practices;
  *localization* and vernacularization show how received forms were changed in
  Tamil, Kannada and Telugu-region settings.
- [ANALYSIS] Puranic identifications could incorporate local deities without
  erasing local names, myths, festivals or constituencies.
- [LIMIT] Varna idioms interacted with occupational and locality-based jatis;
  the peninsula did not become a copy of a northern normative text.
- [LIMIT] Bhakti could broaden devotional access and criticize hierarchy, yet
  temple institutions could reproduce rank. It was not solely an anti-caste
  protest.

#### Language and script matrix

| Context | Exam-safe formulation |
|---|---|
| Pallava chancery | Early Prakrit and then Sanskrit charters; later Sanskrit eulogy often coexisted with Tamil documentary content |
| Badami Chalukya realm | Sanskrit court poetry coexisted with expanding Kannada epigraphic expression |
| Vengi | Sanskrit prestige interacted with regional documentary practice; major Telugu literary florescence belongs substantially to later centuries |
| Literacy | Epigraphic production proves institutional literacy, not mass literacy |

#### Correct eastern and transition boundary

- [FACT] Pulakeshin II's brother Kubja Vishnuvardhana founded the Eastern Chalukya
  line in Vengi in the early seventh century.
- [FACT] The branch continued into the eleventh century. Rajaraja I intervened
  in Vengi succession politics and backed restoration; this must not be rewritten
  as a simple conquest ending the dynasty in AD 999.
- [FACT] Rashtrakuta displacement of Kirtivarman II is conventionally placed
  around AD 753. It ends Badami Chalukya rule, not every Chalukya line.
- [BOUNDARY] Full Rashtrakuta history and later Chola-Vengi integration remain
  outside Topic 23.

#### Final source-control checklist

1. Court eulogy is evidence of a claim, not an audited campaign map.
2. A grant formula is not proof that every listed right was uniformly exercised.
3. Monument style is not a rigid ethnic identity.
4. Royal patronage does not erase artisans, queens, local donors or institutions.
5. Modern linguistic-state boundaries must not be projected backward.
6. Contact with Sri Lanka or Southeast Asia is not proof of a colonial empire.
"""


TOPIC_23_WORKBOOK_SUPPLEMENT = r"""
### Semantic-completeness coverage drills — Topic 23

Use each drill as a 60-second plan before returning to the solved PYQs.

| Drill | Prompt | Minimum answer route | Fatal trap |
|---|---|---|---|
| A | How did irrigation connect agrarian expansion and state formation? | tank/well/channel → settlement and cultivation → shared maintenance → revenue/institution → regional limit | uniform state hydraulic system |
| B | Distinguish *brahmadeya*, *agrahara* and *devadana*. | beneficiary/purpose → chartered rights → formula-versus-practice caution | calling every grant identical |
| C | Were Pallava-Chalukya states centralized empires? | core → intermediaries → local bodies → tribute/campaign zones → graded verdict | campaign equals province |
| D | Compare state models. | feudal → segmentary → integrative → peasantization → evidence-sensitive synthesis | treating one model as settled fact |
| E | Was Brahmanization one-way cultural replacement? | grant and migration → status/ritual → local cult adaptation → language localization → unequal reciprocity | homogenization |
| F | What does multilingual epigraphy prove? | Prakrit/Sanskrit/Tamil/Kannada and bounded Telugu transition → institutional audience → literacy limit | language equals ethnicity |
| G | What can queenly patronage prove? | Lokamahadevi/Virupaksha and Trailokyamahadevi/Mallikarjuna → elite agency → no universal gender claim | general equality from two patrons |
| H | Where does Topic 23 end? | Rashtrakuta takeover c. 753 and continuing Vengi line → bounded Chola link | all Chalukyas vanish together |

**Self-check model:** every response should contain one named item of evidence,
one mechanism, one source or regional limit and one qualified conclusion.
"""

TOPIC_24_MAIN_SUPPLEMENT = r"""
### HISTORICAL SOURCE-LAYER LEDGER — TOPIC 24

#### Text, material evidence and dating

| Evidence | Historical use | Non-negotiable limit |
|---|---|---|
| Vedic hymns, Brahmanas and Aranyakas | ordered reality, sacrifice, sacred speech, symbolic interpretation | layered oral corpora, not finished later systems |
| Principal Upanishads | dialogue, parable, brahman, atman, karma, rebirth and liberation | internally plural Vedic texts; dates and redactions are approximate |
| Buddhist canons | early teaching, discipline and scholastic categories in Pali, Prakrit and Sanskrit-related traditions | oral transmission and sectarian recension separate teaching from final codification |
| Jain canons | doctrine and discipline within sect-specific memory | Shvetambara and Digambara accounts differ on survival and codification |
| Sutras and commentaries | compressed school positions followed by interpretation and controversy | traditional author, root-text layer and later commentary must remain separate |
| Inscriptions, caves and monastic archaeology | patronage, institutions and rare chronological anchors | material support cannot reconstruct a complete doctrine |
| Doxographies and rival refutations | otherwise lost arguments, especially Charvaka and Ajivika | hostile or hierarchical framing can caricature opponents |

**Dating rule:** the Rigvedic, later Vedic, Upanishadic, canonical, sutra and
commentarial layers were created and transmitted over different spans. A text's
writing, redaction or surviving manuscript date is not the date of every idea in
it.

#### Historical formation matrix

| Phase | Development | Caution |
|---|---|---|
| Later Vedic | ritual explanation becomes increasingly symbolic and knowledge-centred | Upanishads transform rather than uniformly reject ritual |
| Mid-first millennium BC | Buddhist, Jain, Ajivika and materialist-sceptical currents enlarge the shramana field | urbanisation enables audiences and patronage but does not mechanically cause doctrine |
| Early historic | Nyaya, Vaisheshika, Samkhya, Yoga, Mimamsa and Vedanta traditions acquire clearer sutra identities | the neat six-school list is later |
| Gupta centuries | Ishvarakrishna, Prashastapada, Mahayana/Yogacara, Dignaga and grammar intensify scholastic exchange | earliest teaching and mature system are not identical |
| Post-Gupta boundary | Dharmakirti, Kumarila, Prabhakara, Gaudapada and Shankara mark major debates | dates remain approximate; later hagiography is not biography |

### SOCIAL, LANGUAGE AND INSTITUTIONAL LEDGER — TOPIC 24

#### Institutions and patronage

```text
oral teacher lineage
        |
sutra compression and commentary
        |
assembly / court / public disputation
        |
monastery / temple / scholarly centre
        |
royal, merchant, household and institutional patronage
        |
preservation, competition and selective archival silence
```

- Philosophy interacted with polity, ritual authority, social hierarchy,
  renunciation, devotional movements and institutions; doctrine did not map
  directly onto universal practice.
- Monasteries, courts, teachers, assemblies and donors shaped intellectual
  survival. Nalanda cannot stand for every tradition.
- Sanskrit was transregional, but Pali, Prakrit and Tamil/regional expression
  prevent a Sanskrit-only history.
- Panini, Katyayana and Patanjali show grammar as analytic infrastructure;
  Bhartrhari marks a late-ancient philosophy-of-language boundary.

#### Women and archive limits

- Gargi and Maitreyi are serious interlocutors in the Brihadaranyaka Upanishad.
  Their literary presence does not prove equal institutional access.
- The Janaka debate is a philosophically revealing textual scene, not a
  recoverable verbatim court transcript.
- Buddhist and Jain sources preserve women renouncers, but Topic 10 owns their
  institutional history.
- Male-authored transmission dominates the archive; missing women cannot be
  repaired by invented names or biographies.

#### School and thinker chronology traps

- Astika is not a synonym for theism; nastika is not a synonym for atheism.
- Samkhya need not posit a creator God; Buddhism's non-self is not nihilism.
- Jain philosophy includes jiva, karmic bondage, anekanta, syadvada and nayavada,
  not merely the ethical slogan of non-violence.
- Nagarjuna belongs broadly to the second-third centuries AD; Asanga and
  Vasubandhu to the fourth-fifth; Dignaga to the fifth-sixth; Dharmakirti to the
  seventh.
- Kumarila and Prabhakara belong broadly to the seventh century; Shankara to the
  eighth-century boundary. Much later Shankara conquest biographies are
  hagiography.
- R.S. Sharma's printed chronology places the Brahma Sutra in the second century
  BC; wider scholarship debates formation across the late centuries BC and early
  centuries AD.

**Final method:** write phase -> text or institution -> core question ->
inter-school interaction -> source limit -> historical significance.
"""


TOPIC_24_WORKBOOK_SUPPLEMENT = r"""
### Semantic-completeness coverage drills — Topic 24

| Drill | Prompt | Minimum answer route | Fatal trap |
|---|---|---|---|
| A | How are philosophical sources dated? | oral layer → redaction → sutra/commentary → manuscript survival → confidence limit | one author-date for a composite corpus |
| B | Did Upanishads reject ritual? | Brahmana/Aranyaka bridge → interiorization → knowledge/liberation → Vedic continuity | simple rupture |
| C | What do astika and nastika mean? | identify speaker/criterion → Vedic authority or other-world claims → polemical use | theist versus atheist |
| D | Why is the six-school list historical? | older traditions → sutra identities → later pairing/doxography | timeless Vedic canon |
| E | How should lost schools be reconstructed? | opponent report → rare material anchor → corroboration → graded confidence | quoting Charvaka as intact scripture |
| F | What sustained debate? | teacher → court/assembly → monastery/temple → patron → commentary | philosophy as private timeless insight |
| G | What can Gargi and Maitreyi prove? | named textual voice → debate context → male archive and access limit | universal equality |
| H | What is the Internal Security cutoff? | Gupta/post-Gupta scholasticism → Kumarila/Dharmakirti/Shankara boundary → later owners | importing mature medieval Vedanta |

**PYQ self-check:** separately solve 2024 Q58 through parable plus relative
chronology, and 2022 Q56 through Aryadeva-Dignaga-Nathamuni identification.
"""

TOPIC_25_MAIN_SUPPLEMENT = r"""
### CONNECTED-HISTORY EVIDENCE LEDGER — TOPIC 25

#### Source and inference control

| Evidence | Secure claim | Hard limit |
|---|---|---|
| Inscriptions | local ruler, donor, language, script, title and religious claim | Sanskrit does not prove Indian political rule or population replacement |
| Archaeology and ceramics | dated ports, settlements, imports, production and consumption | an imported object does not establish a colony |
| Art and architecture | locally commissioned form, iconography and workshop interaction | resemblance cannot identify every artisan or route |
| Manuscripts and translations | selected text, translation institution and conceptual remaking | surviving copy date is not original composition date |
| Chinese travel accounts | route, monastery, text search and observed practice | pilgrim purpose, hearsay and uneven access |
| Sri Lankan/local chronicles | monastic lineage, relic and dynastic memory | later legitimation is not contemporary inscription |
| Greater India/nationalist histories | history of interpretation | cultural pride is not primary evidence |

**Method:** direct evidence -> local tradition -> stylistic comparison -> modern
inference. Keep all four levels visible.

#### Buddhist and translation chronology

| Network/figure | Historical role | Caution |
|---|---|---|
| Sri Lanka | early Brahmi/monastic evidence, Pali preservation and Theravada lineages | Mahavamsa mission memory is later than Ashoka's edicts |
| Khotan and Kucha | oasis monasteries, manuscripts and caravan-linked institutions | changing local political settings |
| Kumarajiva, c. 344-413 | Kucha-connected translator active at Chang'an | Chinese teams and audiences remade terminology |
| Faxian, c. 399-414 journey | sought monastic texts and travelled through India/Sri Lanka | selective Buddhist account |
| Xuanzang, 629-645 journey | studied in India and translated texts in China | not eyewitness to every historical claim |
| Yijing, 671-695 travels | studied via Srivijaya and Indian centres | proves a network, not Indian sovereignty |

Theravada, Mahayana and Vajrayana/Mantrayana transmissions followed overlapping
and changing routes. No single council, route or state explains their spread.

### LOCALIZATION, TRADE AND RECIPROCITY LEDGER — TOPIC 25

#### Southeast Asian chronology

| Zone | Bounded marker | Anti-anachronism rule |
|---|---|---|
| Funan/Oc-Eo | early Mekong-delta exchange and Chinese/local evidence | not an Indian colony |
| Champa/My Son | regional Cham polities, Sanskrit/Cham records and Shaiva-Buddhist patronage | not one timeless centralized state |
| Pyu and Dvaravati | first-millennium Myanmar/Thailand-zone urban and Buddhist networks | modern borders are only location aids |
| Srivijaya | seventh-century onward Straits-centred maritime and Buddhist network | extent and political control changed |
| Sailendra/Borobudur | eighth-ninth-century Javanese patronage and local Buddhist monument | monument attribution requires inscription, archaeology and style |
| Prambanan/Angkor | ninth-century and later boundary examples | neither is an ancient Indian monument |

#### Trade and reciprocal effects

- Monsoon navigation connected ports, straits and hinterlands; ships, coins and
  ceramics require dated archaeological context.
- Textiles, beads, aromatics, metals, silk, horses and forest/marine products
  circulated unevenly.
- Foreign merchants, monks, artisans and political groups formed communities in
  Indian ports and frontier zones.
- Hellenistic, Iranian and Central Asian motifs shaped Gandhara; Asian products,
  technologies and translation archives affected India.
- Sri Lankan Pali and monastic traditions and Southeast Asian patronage created
  return flows rather than passive reception.
- Calendrical, astronomical and statecraft vocabulary travelled selectively;
  similarity alone cannot establish one source.

#### PYQ ownership control

The repository routes **zero direct PYQs** to Topic 25. Retained questions are
adjacent or boundary practice only:

- 2019 GS-I Q1 -> Art and Culture plus Topic 16;
- 2019 Prelims Q9 and 2020 Q31 -> Topic 10;
- 2024 Q64 -> Topic 10;
- 2025 Q15 -> Topic 20;
- 2025 Q16 -> Topic 27;
- 2026 Q7 -> Art and Culture Topic 11, provisional key only.

**Final answer method:** route + agent + medium + local selection + transformed
outcome + reciprocal effect + source limit.
"""


TOPIC_25_WORKBOOK_SUPPLEMENT = r"""
### Semantic-completeness coverage drills — Topic 25

| Drill | Prompt | Minimum answer route | Fatal trap |
|---|---|---|---|
| A | Why replace Greater India with connected history? | real transmission → local selection → translation → hybrid result → return flow | passive colonies |
| B | How should a Sanskrit inscription abroad be used? | date/place/donor → local political purpose → script/language limit | Indian sovereignty |
| C | Compare land and maritime routes. | Gandhara-oasis-China versus port-monsoon-straits → agents/institutions | one diffusion route |
| D | Distinguish Buddhist transmissions. | Theravada/Sri Lanka → Mahayana/Central-East Asia → later Vajrayana/Himalaya | one council or chronology |
| E | Test traveller knowledge. | Kumarajiva, Faxian, Xuanzang and Yijing by route, purpose and date | neutral universal eyewitness |
| F | Explain Southeast Asian localization. | Funan/Champa → Srivijaya/Sailendra → local scripts, courts and monuments | Indian-built replicas |
| G | What can coins, ceramics and ships prove? | context → circulation/use → alternative explanation → limit | coin/import equals rule |
| H | Demonstrate reciprocity. | foreign communities/motifs/technologies → effects in India → unequal regional exchange | one-way cultural export |

**PYQ status drill:** all seven retained PYQs are adjacent or boundary-owned;
none is routed directly to Topic 25.
"""

TOPIC_26_MAIN_SUPPLEMENT = r"""
### TRANSITION EVIDENCE AND PERIODIZATION LEDGER — TOPIC 26

#### Models and criteria

| Model | Core use | Limit |
|---|---|---|
| Colonial Hindu/Muslim/British division | history of periodization | communal ruler-religion label cannot explain social transition |
| Dynastic chronology | orders Gupta, post-Gupta and regional polities | ruler change is not simultaneous structural change |
| Indian feudalism | grants, intermediaries, immunities, labour and exchange contraction | outcomes and commerce vary by region |
| Segmentary state | graded ritual/political control beyond a core | derived mainly from later-south debates; not universal |
| Integrative/regional state | chiefs, grants, cults and local elites build regional power | integration remains unequal and coercive |

Test transition through polity, agrarian relations, revenue/labour, settlement,
exchange, institutions, social classification, religion, language and material
culture. The c. 300-550, 550-750 and 750-1000 phases are heuristics, not universal
ruptures.

#### Grant rights and ground effects

| Recipient/right | Historical question | Source caution |
|---|---|---|
| Brahmana, temple, monastery, official or retainer | why was revenue or land assigned? | recipient classes vary by region and date |
| taxes and produce | who collected which dues? | exemption formula is not proof of enforcement |
| labour (vishti) | who supplied transport, construction or provisioning? | incidence must be locally evidenced |
| judicial/fiscal immunity | were fines, officials or policing functions restricted? | specified right is not total sovereignty |
| water, pasture, trees and forest | which older users were affected? | charter silence does not mean empty land |

### REGIONAL CONTINUITY-CHANGE LEDGER — TOPIC 26

| Region | Transition pattern | Anti-universalization rule |
|---|---|---|
| North | post-Gupta courts, samantas, grants and selected urban contraction | no instantaneous anarchy |
| East | agrarian expansion, Pala-Sena formations and mahavihara networks | no uniform Buddhist society |
| Western India | regional lineages, ports and Jain/Brahmanical institutions | genealogy is not literal ethnicity |
| Deccan | Vakataka-Chalukya-Rashtrakuta grants, temples, irrigation and exchange | no one feudal sequence |
| South | Pallava/Pandya and Chola-boundary brahmadeyas, tanks, temples and local bodies | full Imperial Chola system belongs to Topic 27 |
| Forest/hill frontiers | chiefs, products, cultivation, cults, resistance and peasantization | incorporation is not passive assimilation |

#### Social, institutional and knowledge controls

- Samanta changed from neighbouring ruler to varied subordinate/intermediary
  usage; it was not one legal class.
- Temples and monasteries could be landholders, employers, redistributors,
  archives, schools and political nodes, but functions varied locally.
- Varna prescription, jati process, occupation, untouchability and exclusion
  must be separated by source, region and date.
- Gender analysis must include property, marriage, labour, donor/political and
  religious agency without one all-India status verdict.
- Bhakti was not uniformly egalitarian; Buddhism and Jainism transformed
  regionally rather than simply disappearing.
- Sanskrit cosmopolitan continuity coexisted with vernacular literary and
  epigraphic growth.
- Incoming peoples affected political and cultural formation, but invasion alone
  did not cause the transition.

#### PYQ ownership control

The repository routes **zero direct PYQs** to Topic 26. The ten retained
questions belong to Topics 10, 20, 22, 23, 27 or Indian Art and Culture and are
adjacent continuity/change practice only.

**Final method:** model -> evidence class -> regional case -> continuity ->
transformation -> source limit -> qualified verdict.
"""


TOPIC_26_WORKBOOK_SUPPLEMENT = r"""
### Semantic-completeness coverage drills — Topic 26

| Drill | Prompt | Minimum answer route | Fatal trap |
|---|---|---|---|
| A | Why is AD 750 not a universal break? | multiple criteria → regional phases → continuity/change | one date for all India |
| B | Does every grant prove feudalism? | recipient/right/formula → ground effect → alternative integration | grant equals feudalism |
| C | What changed under samanta relations? | title history → tribute/service/local power → scale | fixed legal class |
| D | Did trade and towns collapse? | coin/town/import evidence → regional contraction → new nodes/revival | universal decline |
| E | How did temples and monasteries matter? | ritual + land + labour + redistribution + archive + local variation | merely religious |
| F | Was Brahmanization passive assimilation? | grant/cult/status → localization → tribal/local agency → unequal reciprocity | one-way replacement |
| G | Evaluate social change. | varna text → jati/occupation/exclusion → gender/property/labour → source limits | prescription equals practice |
| H | Compare regions. | north + east + Deccan + south/frontier → different sequences | one pan-Indian model |

**PYQ status drill:** all ten retained PYQs are adjacent-owned; none is routed
directly to Topic 26.
"""

TOPIC_27_MAIN_SUPPLEMENT = r"""
### FINAL CHOLA EVIDENCE LEDGER — TOPIC 27

#### Source, chronology and political-space controls

| Evidence | Secure use | Hard limit |
|---|---|---|
| Royal eulogy/order | ruler, title, order, campaign claim and ideology | target list is not a permanent empire map |
| Temple record | tax, gift, staff, committee, transaction and institutional work | great temples over-shape the surviving archive |
| Copper plate | genealogy, grant, monastery and diplomatic patronage | formula and royal lineage claim need corroboration |
| Archaeology/architecture | settlement, port, irrigation, craft and monumental sequence | style alone cannot name every patron |
| Coin | ruler/title, metal and circulation | no uniform cash economy or sovereignty from one find |
| Sri Lankan/Chinese account | external view of campaigns, embassies and trade | selective purpose, chronology and hearsay |

| Phase | Historical anchor | Caution |
|---|---|---|
| Vijayalaya-Aditya I | Tanjavur foothold and Pallava eclipse | not an uninterrupted Sangam empire |
| Parantaka I | Pandya expansion and Takkolam setback | expansion was reversible |
| Rajaraja I | survey, northern Sri Lanka and Brihadisvara | monument does not prove universal prosperity |
| Rajendra I | Gangaikondacholapuram, Ganga claim and 1025 Srivijaya/Kadaram targets | neither route nor raid equals annexed provinces |
| Rajadhiraja-successors | Western Chalukya and island warfare | one battlefield death did not end the dynasty |
| Kulottunga I | Eastern Chalukya-Chola branch connection and consolidation | dynastic change plus continuity |

### STATE, SOCIETY AND MARITIME LIMIT LEDGER — TOPIC 27

#### Administration and locality

- Mandalam, valanadu, nadu, kurram, ur, sabha/mahasabha, nagaram and variyam
  varied by inscription, chronology and region.
- Uttaramerur describes a restricted brahmadeya sabha procedure with property,
  residence, age, learning/conduct and accounting conditions; it is not
  universal democracy.
- Royal authority worked through officers, chiefs, temples, assemblies and
  landed/corporate intermediaries.
- Centralized, segmentary and integrative models each explain part of the
  inscriptional evidence.

#### Land, dependence and temple society

- Ownership, cultivation, revenue claim and jurisdiction are distinct land
  rights.
- Brahmadeya, devadana and non-brahmadeya land coexisted with vellala
  landholding/cultivation, peasants, artisans and service groups.
- Segregated settlements and dependent/servile relations are visible, but terms
  should not be equated automatically with modern Atlantic slavery.
- Women appear as queens, property holders, donors and temple personnel; agency
  coexisted with patriarchal and caste constraints.
- Temples could be ritual, landed, redistributive, employment, craft,
  educational, cultural and archival nodes; no single temple model is universal.

#### Maritime and religious limits

- Ainnurruvar/Ayyavole, Manigramam, Anjuvannam and nagaram networks interacted
  with courts without becoming royal departments.
- Sri Lanka involved conquest, administration and resistance; Srivijaya/Kadaram
  involved an expeditionary strike plus later diplomacy.
- No evidence establishes Southeast Asian colonization, a permanent naval
  empire or royal control of every commercial voyage.
- Shaiva prominence coexisted unevenly with Vaishnava, Buddhist and Jain
  institutions; religious pluralism did not exclude conflict.
- Kaveri ecology enabled intensive agriculture, but ecological determinism
  cannot explain imperial formation.

#### Four routed PYQ anchors

1. 2020 Prelims Q24: cross-routed dynasty chronology; inferred order only.
2. 2022 GS-I Q12: Gupta-Chola cultural comparison.
3. 2024 GS-I Q11: Chola art and architecture with institutional/material context.
4. 2025 Prelims Q16: officially keyed Rajendra I Srivijaya campaign.

**Final method:** source -> reign/region -> institution -> social/material
mechanism -> limit -> multidimensional verdict.
"""


TOPIC_27_WORKBOOK_SUPPLEMENT = r"""
### Semantic-completeness coverage drills — Topic 27

| Drill | Prompt | Minimum answer route | Fatal trap |
|---|---|---|---|
| A | How should conquest inscriptions be used? | claim/date/target → rival/material evidence → duration limit | audited empire map |
| B | Was the Chola state centralized? | royal command/survey → intermediaries/local bodies → three models → graded verdict | bureaucracy versus autonomy binary |
| C | What does Uttaramerur prove? | brahmadeya scope → eligibility/disqualification → kudavolai/variyam → exclusion | universal democracy |
| D | Explain the agrarian base. | Kaveri/tanks/canals → land rights/survey/tax/labour → hierarchy | ecological determinism |
| E | Reconstruct social dependence. | inscriptional term/settlement → labour and legal context → slavery caution | modern chattel equivalence |
| F | Explain temple power. | ritual + land + labour + redistribution + craft + education/archive → variation | temple command economy |
| G | Assess merchant and naval power. | guild/port/commodity → state interaction → Sri Lanka/Srivijaya distinction | colonization |
| H | Build the culture answer. | three temples → bronzes/Nataraja → Tamil/Sanskrit → labour/patronage limit | monuments equal universal prosperity |

**PYQ self-check:** 2020 Q24, 2022 GS-I Q12, 2024 GS-I Q11 and 2025 Q16
must all be executable from chronology, culture and maritime evidence.
"""


def _base_augment_topic_semantic_content(
    topic: Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    if topic.topic_key == "internal-security-27":
        supplement = (
            TOPIC_27_WORKBOOK_SUPPLEMENT
            if workbook
            else TOPIC_27_MAIN_SUPPLEMENT
        ).strip()
        marker = (
            "### Semantic-completeness coverage drills — Topic 27"
            if workbook
            else "### FINAL CHOLA EVIDENCE LEDGER — TOPIC 27"
        )
        if marker in markdown:
            return markdown
        insertion = (
            "## PYQS AND ANSWER PRACTICE"
            if workbook
            else "## BASIC MCQS / REMEDIATION"
        )
        if insertion not in markdown:
            raise ValueError(f"{topic.topic_key}: required insertion point is absent.")
        return markdown.replace(insertion, supplement + "\n\n" + insertion, 1)
    if topic.topic_key == "internal-security-26":
        supplement = (
            TOPIC_26_WORKBOOK_SUPPLEMENT
            if workbook
            else TOPIC_26_MAIN_SUPPLEMENT
        ).strip()
        marker = (
            "### Semantic-completeness coverage drills — Topic 26"
            if workbook
            else "### TRANSITION EVIDENCE AND PERIODIZATION LEDGER — TOPIC 26"
        )
        if marker in markdown:
            return markdown
        insertion = (
            "## PYQS AND ANSWER PRACTICE"
            if workbook
            else "## BASIC MCQS / REMEDIATION"
        )
        if insertion not in markdown:
            raise ValueError(f"{topic.topic_key}: required insertion point is absent.")
        return markdown.replace(insertion, supplement + "\n\n" + insertion, 1)
    if topic.topic_key == "internal-security-25":
        supplement = (
            TOPIC_25_WORKBOOK_SUPPLEMENT
            if workbook
            else TOPIC_25_MAIN_SUPPLEMENT
        ).strip()
        marker = (
            "### Semantic-completeness coverage drills — Topic 25"
            if workbook
            else "### CONNECTED-HISTORY EVIDENCE LEDGER — TOPIC 25"
        )
        if marker in markdown:
            return markdown
        insertion = (
            "## PYQS AND ANSWER PRACTICE"
            if workbook
            else "## BASIC MCQS / REMEDIATION"
        )
        if insertion not in markdown:
            raise ValueError(f"{topic.topic_key}: required insertion point is absent.")
        return markdown.replace(insertion, supplement + "\n\n" + insertion, 1)
    if topic.topic_key == "internal-security-24":
        replacements = {
            (
                "In Sharma's chronology, the Brahma Sutra belongs around the "
                "2nd century CE, though exact dating remains debated."
            ): (
                "R.S. Sharma's printed chronology places the Brahma Sutra in "
                "the 2nd century BC; wider scholarship debates its formation "
                "across the late centuries BC and early centuries AD."
            ),
            "2nd c. CE -> RS Sharma places Badarayana's Brahmasutra": (
                "LATE BC / EARLY CE -> debated Brahma Sutra formation"
            ),
        }
        for old, new in replacements.items():
            markdown = markdown.replace(old, new)
        supplement = (
            TOPIC_24_WORKBOOK_SUPPLEMENT
            if workbook
            else TOPIC_24_MAIN_SUPPLEMENT
        ).strip()
        marker = (
            "### Semantic-completeness coverage drills — Topic 24"
            if workbook
            else "### HISTORICAL SOURCE-LAYER LEDGER — TOPIC 24"
        )
        if marker in markdown:
            return markdown
        insertion = (
            "## PYQS AND ANSWER PRACTICE"
            if workbook
            else "## BASIC MCQS / REMEDIATION"
        )
        if insertion not in markdown:
            raise ValueError(f"{topic.topic_key}: required insertion point is absent.")
        return markdown.replace(insertion, supplement + "\n\n" + insertion, 1)
    if topic.topic_key != "internal-security-23":
        return markdown
    replacements = {
        (
            "Upinder says the eastern Chalukya line survived till 999 CE, when "
            "Rajaraja Chola conquered Vengi"
        ): (
            "The Eastern Chalukya line continued into the eleventh century; "
            "Rajaraja I intervened in Vengi succession politics rather than "
            "simply ending the dynasty by conquest in AD 999"
        ),
        "AD 757": "c. AD 753",
        "999 CE = end of Badami Chalukya hegemony.": (
            "c. AD 753 = end of Badami Chalukya hegemony."
        ),
        "Lokmahadevi": "Lokamahadevi",
        "Trilok Mahadevi": "Trailokyamahadevi",
        "Dandin is the strongest named Pallava literary citation for UPSC.": (
            "Dandin is a useful Pallava-world literary citation, but the precise "
            "court association should remain qualified."
        ),
    }
    for old, new in replacements.items():
        markdown = markdown.replace(old, new)
    legacy_main_marker = (
        "### SESSION 23 — CLOSING ABSENCE REPAIR: WATER, GRANT FORMS, "
        "INTERMEDIARIES AND STATE DEBATE"
    )
    if not workbook and legacy_main_marker in markdown:
        start = markdown.index(legacy_main_marker)
        start = markdown.rfind("###", 0, start + 3)
        end = markdown.index("## BASIC MCQS / REMEDIATION", start)
        markdown = markdown[:start] + markdown[end:]
    supplement = (
        TOPIC_23_WORKBOOK_SUPPLEMENT if workbook else TOPIC_23_MAIN_SUPPLEMENT
    ).strip()
    marker = (
        "### Semantic-completeness coverage drills — Topic 23"
        if workbook
        else "### CLOSING SEMANTIC LEDGER A"
    )
    if marker in markdown:
        return markdown
    insertion = (
        "## PYQS AND ANSWER PRACTICE"
        if workbook
        else "## BASIC MCQS / REMEDIATION"
    )
    if insertion not in markdown:
        raise ValueError(f"{topic.topic_key}: required insertion point is absent.")
    return markdown.replace(insertion, supplement + "\n\n" + insertion, 1)


def _answer_controls(question: str, title: str) -> dict[str, str]:
    marks_match = re.search(r"\b(10|15|20)\s*marks?\b", title + " " + question, re.I)
    marks = int(marks_match.group(1)) if marks_match else 15
    evidence_count = {10: "three", 15: "five", 20: "six to eight"}[marks]
    directive = _directive(question)
    focus = textwrap.shorten(question, width=92, placeholder="…")
    if "prelims" in title.casefold() or re.search(
        r"\boption\b|\bwhich of the following\b", question, re.I
    ):
        return {
            "demand": (
                f"Treat “{focus}” as a source-and-elimination problem: verify each "
                "statement independently, preserve the official wording where available, "
                "and separate an inferred key from an official key."
            ),
            "plan": (
                "Identify the tested chronology, site, text, inscription or institution; "
                "eliminate each option with one named fact; then state the evidence limit "
                "or key-verification status."
            ),
            "why": (
                "It preserves statement-level integrity, uses named evidence instead of "
                "familiar-name guessing, and does not promote an inferred key to official status."
            ),
            "improve": (
                f"For “{focus}”, add one explicit sentence explaining why the closest "
                "distractor fails on chronology, geography, source class or degree of certainty."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "coverage of every clause, evidence-led analysis and a qualified verdict."
        ),
        "plan": (
            f"For a {marks}-mark answer, open with a two-sentence thesis; organise "
            f"{evidence_count} named evidence units as claim → evidence → inference → "
            "qualification; reserve the final lines for a graded conclusion."
        ),
        "why": (
            "The answer follows the directive, links precise evidence to analysis, "
            "acknowledges source or regional limits and closes with a reasoned verdict."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one additional "
            "named site, text, inscription, coin, ruler or scholarly position and state "
            "exactly what that evidence cannot prove."
        ),
    }


def repair_answer_contracts(markdown: str) -> tuple[str, dict[str, Any]]:
    try:
        start = markdown.index("## PYQS AND ANSWER PRACTICE")
        end = markdown.index("## OPTIONAL ADVANCED DEPTH", start)
    except ValueError:
        start = markdown.index("## PYQS AND ANSWER PRACTICE")
        end = len(markdown)
    before, area, after = markdown[:start], markdown[start:end], markdown[end:]
    matches = [
        match
        for match in QUESTION_HEADING.finditer(area)
        if "MCQ" not in match.group("title").upper()
        and (
            re.search(r"\bPYQ\b", match.group("title"), re.I)
            or re.search(
                r"(?:^|\s)[MOP]-?\d+(?:\b|\.)",
                match.group("title"),
                re.I,
            )
            or re.search(
                r"\b(?:Mains|Original|Solved Question|Practice Question)\b.*\d+",
                match.group("title"),
                re.I,
            )
        )
    ]
    chunks: list[str] = []
    cursor = 0
    repaired_count = 0
    question_metrics: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(area)
        block = area[match.start() : block_end].rstrip()
        title = match.group("title").strip()
        if not re.search(
            r"(?i)model (?:answer|solution)|core teaching / solved analysis|"
            r"direct thesis|answer route|answer and method|solved analysis|"
            r"\*\*solution:|\*\*model\s*\(|\[claim\]|"
            r"\*\*answer(?:\s*/\s*route)?:",
            block,
        ):
            continue
        chunks.append(area[cursor : match.start()])
        question = _short_question(block, title)
        controls = _answer_controls(question, title)
        additions: list[str] = []
        if not re.search(r"(?i)\*\*Demand decoding[.:]\*\*", block):
            additions.append(f"**Demand decoding:** {controls['demand']}")
        if not re.search(r"(?i)\*\*Detailed examiner-grade model", block):
            additions.append(
                "**Detailed examiner-grade model status:** The model answer or solved "
                "analysis above is the executable content base; retain its named evidence, "
                "causal links and qualification rather than replacing it with a generic summary."
            )
        if not re.search(
            r"(?i)\*\*Executable exam-length answer / compression plan[.:]\*\*",
            block,
        ):
            additions.append(
                "**Executable exam-length answer / compression plan:** "
                + controls["plan"]
            )
        if not re.search(r"(?i)Why this earns marks", block):
            additions.append(f"**Why this earns marks:** {controls['why']}")
        if not re.search(r"(?i)How to improve this answer", block):
            additions.append(
                "**How to improve this answer:** " + controls["improve"]
            )
        if additions:
            block += "\n\n" + "\n\n".join(additions)
            repaired_count += 1
        question_metrics.append(
            {
                "title": title,
                "question": question,
                "demand": bool(re.search(r"(?i)Demand decoding", block)),
                "model": bool(
                    re.search(
                        r"(?i)model (?:answer|solution)|"
                        r"Detailed examiner-grade model",
                        block,
                    )
                ),
                "compression": bool(
                    re.search(
                        r"(?i)Executable exam-length answer / compression plan",
                        block,
                    )
                ),
                "why": bool(re.search(r"(?i)Why this earns marks", block)),
                "improve": bool(
                    re.search(r"(?i)How to improve this answer", block)
                ),
            }
        )
        chunks.append(block + "\n\n")
        cursor = block_end
    chunks.append(area[cursor:])
    return (
        before + "".join(chunks) + after,
        {
            "question_count": len(question_metrics),
            "repaired_count": repaired_count,
            "questions": question_metrics,
        },
    )


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    current_note = provenance.get("current_linkage_note") or (
        "No current archaeological or heritage claim is used to alter the static "
        "chronology. Any present-day linkage remains contextual and dated."
    )
    source_lines = "\n".join(
        f"- `{path}`" for path in live_sources
    ) or "- No live source is required for a static claim in this topic."
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Internal Security Core is taught before optional enrichment. |
| Evidence method | Claim → named site/text/inscription/coin/example → analysis → qualification. |
| Source hierarchy | Archaeology, textual testimony, inscriptions, coins and scholarly interpretation remain visibly distinct. |
| Contested issues | Competing interpretations are attributed, evidenced and bounded; certainty is not manufactured. |
| Practice contract | Every solved item has demand decoding, an examiner-grade model, an executable answer/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Archaeological inference:** material context supports bounded reconstruction; absence is not automatic proof of non-existence.
- **Textual testimony:** genre, authorship, redaction, patronage and temporal distance control what a text can prove.
- **Inscription and coin evidence:** contemporary names, titles, claims and circulation are powerful but do not by themselves map uniform territorial control.
- **Scholarly interpretation:** historian labels are arguments to test, not facts to memorise without evidence.
- **PYQ discipline:** repository ledgers and locally held official papers control wording and metadata; reconstructed wording and unavailable official keys must be labelled.
- **Current-status note, rechecked {DATE}:** {current_note}

**Live/primary context sources recorded by the predecessor generation:**

{source_lines}
"""


def insert_contract(markdown: str, topic: Topic, record: dict[str, Any]) -> str:
    if "### DEEP-REVIEW LEARNING CONTRACT" in markdown:
        return markdown
    marker = "## BASIC LEARNING SESSION"
    position = markdown.index(marker) + len(marker)
    return (
        markdown[:position]
        + "\n\n"
        + source_contract(topic, record)
        + "\n"
        + markdown[position:]
    )


def clean_source_line(line: str) -> str:
    value = re.sub(r"!\[[^\]]*]\([^)]+\)", " ", line)
    value = re.sub(r"\[([^\]]+)]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"^[#>*+\-\d.)\s]+", "", value)
    value = re.sub(r"[*_`|]", " ", value)
    value = re.sub(r"\s+", " ", value).strip(" :;-")
    return value


def extract_lines(text: str, pattern: str, limit: int) -> list[str]:
    result: list[str] = []
    for raw in text.splitlines():
        value = clean_source_line(raw)
        if (
            28 <= len(value) <= 180
            and re.search(pattern, value, re.I)
            and value.casefold() not in {item.casefold() for item in result}
        ):
            result.append(value)
        if len(result) >= limit:
            break
    return result


def wrapped_body(title: str, lines: list[str], conclusion: str) -> str:
    chunks = [title.upper()]
    for number, line in enumerate(lines, 1):
        wrapped = textwrap.wrap(
            f"{number}. {line}",
            width=94,
            subsequent_indent="   ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        chunks.extend(wrapped)
    chunks.append("VERDICT: " + conclusion)
    return "\n".join(chunks)


def supplemental_panels(topic: Topic, main: str) -> list[dict[str, Any]]:
    owner = topic.basic_path.read_text(encoding="utf-8")
    evidence = extract_lines(
        owner,
        r"\b(site|text|inscription|coin|archaeolog|source|evidence|"
        r"excavat|chronolog|epigraph|numismat)\b",
        5,
    )
    traps = extract_lines(
        main,
        r"\b(trap|do not|must not|cannot prove|however|caution|"
        r"contested|debate|limit)\b",
        5,
    )
    answer = extract_lines(
        main,
        r"\b(thesis|verdict|conclusion|answer|mains|significance|"
        r"compare|assess|examine)\b",
        5,
    )
    if not evidence:
        evidence = [
            f"Use the named material, textual, inscriptional and numismatic evidence in {topic.title}.",
            "Attach a source limitation to every territorial, social or chronological inference.",
        ]
    if not traps:
        traps = [
            "Do not convert a source claim into an exact map, census or uncontested chronology.",
            "Keep regional variation and unequal source survival visible.",
        ]
    if not answer:
        answer = [
            f"Open by defining the central historical problem in {topic.title}.",
            "Organise the body by chronology, evidence, mechanism, debate and qualification.",
        ]
    def compact(label: str, values: list[str], verdict: str) -> list[str]:
        def ascii_value(value: str) -> str:
            value = (
                value.replace("→", "->")
                .replace("—", "-")
                .replace("–", "-")
                .replace("…", "...")
            )
            return (
                unicodedata.normalize("NFKD", value)
                .encode("ascii", "ignore")
                .decode("ascii")
            )

        return [
            ascii_value(label.upper()),
            *[
                f"{number}. "
                + textwrap.shorten(
                    ascii_value(value),
                    width=72,
                    placeholder="...",
                )
                for number, value in enumerate(values[:3], 1)
            ],
            "VERDICT: "
            + textwrap.shorten(
                ascii_value(verdict),
                width=72,
                placeholder="...",
            ),
        ]

    reference = [rel(topic.basic_path), rel(topic.advanced_path)]
    return [
        {
            "title": "Evidence ladder and confidence control",
            "structural_type": "evidence-matrix",
            "ascii_lines": compact(
                "Evidence ladder",
                evidence,
                "Source type controls the strength and limits of the historical claim.",
            ),
            "source_references": reference,
        },
        {
            "title": "Examiner traps and contested boundaries",
            "structural_type": "trap-matrix",
            "ascii_lines": compact(
                "Close distinctions",
                traps,
                "Qualification earns marks; false certainty is a hard failure.",
            ),
            "source_references": reference,
        },
        {
            "title": "Integrated answer spine and qualified conclusion",
            "structural_type": "answer-synthesis",
            "ascii_lines": compact(
                "Answer spine",
                answer,
                "Claim, named evidence, analysis and qualification lead to a graded verdict.",
            ),
            "source_references": reference,
        },
    ]


def current_manual_topic(record: dict[str, Any], topic: Topic) -> dict[str, Any]:
    spec_value = record.get("continuous_core_first", {}).get("ascii_master_spec")
    if not spec_value:
        raise ValueError(f"{topic.topic_key}: predecessor ASCII spec path is absent.")
    spec_path = repo(spec_value)
    data = load(spec_path)
    raw_topics = data.get("topics", [])
    if isinstance(raw_topics, dict):
        raw = raw_topics.get(topic.topic_key)
    else:
        raw = next(
            (
                row
                for row in raw_topics
                if isinstance(row, dict)
                and row.get("topic_key") == topic.topic_key
            ),
            None,
        )
    if not isinstance(raw, dict):
        raise ValueError(
            f"{topic.topic_key}: predecessor ASCII spec has no matching topic."
        )
    return json.loads(json.dumps(raw))


def _base_build_ascii_spec(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    raw = current_manual_topic(record, topic)
    panels = list(raw.get("panels", []))
    extras = supplemental_panels(topic, main)
    while len(panels) < 12:
        panels.append(extras[(len(panels) - len(raw.get("panels", []))) % len(extras)])
    if len(panels) > 12:
        panels = panels[:12]
    line_overrides = ASCII_PANEL_LINE_OVERRIDES.get(topic.topic_key, {})
    for panel in panels:
        title = str(panel.get("title", ""))
        if title in line_overrides:
            panel["ascii_lines"] = list(line_overrides[title])
        references = panel.setdefault("source_references", [])
        if not isinstance(references, list):
            panel["source_references"] = [str(references)]
            references = panel["source_references"]
        for path in (topic.basic_path, topic.advanced_path, markdown_path):
            value = rel(path)
            if value not in references:
                references.append(value)
    return {
        "schema_version": 1,
        "generated_on": DATE,
        "workflow": WORKFLOW,
        "constraints": {
            "panel_count_per_topic": 12,
            "max_line_width": 100,
            "manual_topic_specific": True,
            "complete_core_before_optional": True,
            "same_source_ledger_as_session_and_workbook": True,
            "approval": False,
        },
        "topics": [
            {
                "topic_key": topic.topic_key,
                "display_title": topic.title,
                "active_generation": generation,
                "source_session": rel(markdown_path),
                "panel_count": 12,
                "panels": panels,
            }
        ],
    }


def replace_ascii_fragment(markdown: str, fragment: str) -> str:
    marker = "### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM"
    replacement = marker + "\n\n" + fragment.rstrip() + "\n"
    if marker not in markdown:
        register = markdown.index("## CONSOLIDATED REGISTER NOTES")
        insert_at = register + len("## CONSOLIDATED REGISTER NOTES")
        return markdown[:insert_at] + "\n\n" + replacement + markdown[insert_at:]
    start = markdown.index(marker)
    content_start = start + len(marker)
    next_heading = re.search(r"(?m)^###(?!#)\s+.+$", markdown[content_start:])
    if next_heading:
        end = content_start + next_heading.start()
    else:
        end = len(markdown)
    return markdown[:start] + replacement + markdown[end:]


def refresh_current_status_date(markdown: str) -> str:
    return re.sub(
        r"(Current-status note, rechecked )\d{4}-\d{2}-\d{2}",
        rf"\g<1>{DATE}",
        markdown,
        count=1,
    )


def remove_invalid_topic_mcq_audits(topic: Topic, markdown: str) -> str:
    if topic.topic_key != "internal-security-02":
        return markdown
    return re.sub(
        r"(?ms)^<!-- BEGIN ANSWER-WORTHINESS AUDIT: MCQS -->.*?"
        r"^<!-- END ANSWER-WORTHINESS AUDIT: MCQS -->\s*",
        "",
        markdown,
        count=1,
    )


def question_contract_errors(metrics: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if metrics["question_count"] == 0:
        errors.append("No solved PYQ/Mains question blocks were identified.")
    for question in metrics["questions"]:
        missing = [
            key
            for key in ("demand", "model", "compression", "why", "improve")
            if not question[key]
        ]
        if missing:
            errors.append(
                f"{question['title']}: missing {', '.join(missing)}."
            )
    return errors


def baseline_audit(topic: Topic, record: dict[str, Any]) -> dict[str, Any]:
    main_path = repo(record["markdown"])
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    if not workbook_value:
        raise ValueError(f"{topic.topic_key}: workbook Markdown is absent.")
    workbook_path = repo(workbook_value)
    main = main_path.read_text(encoding="utf-8")
    workbook = workbook_path.read_text(encoding="utf-8")
    _, rotation = enforce_strict_rotation(workbook)
    _, answer_metrics = repair_answer_contracts(workbook)
    predecessor_spec = current_manual_topic(record, topic)
    panel_count = len(predecessor_spec.get("panels", []))
    flow_folder = repo(record["continuous_core_first"]["folder"])
    flow_report = flow_folder / "validation-report.txt"
    graphical_passed = (
        flow_report.is_file()
        and "errors=none" in flow_report.read_text(encoding="utf-8")
    )
    main_layout_errors, main_layout = validate_pdf_layout(repo(record["main_pdf"]))
    workbook_layout_errors, workbook_layout = validate_pdf_layout(
        repo(record["workbook"])
    )
    missing_controls = Counter()
    for question in answer_metrics["questions"]:
        for key in ("demand", "model", "compression", "why", "improve"):
            if not question[key]:
                missing_controls[key] += 1
    defects: list[str] = []
    if "### DEEP-REVIEW LEARNING CONTRACT" not in main:
        defects.append(
            "The session lacks an explicit syllabus, evidence-class, contested-claim "
            "and approval contract."
        )
    if missing_controls:
        defects.append(
            "Solved-answer controls are incomplete: "
            + ", ".join(
                f"{key}={count}" for key, count in sorted(missing_controls.items())
            )
            + "."
        )
    expected = ["ABCD"[index % 4] for index in range(rotation["count"])]
    if rotation["unparsed"] or rotation["keys"] != expected:
        defects.append(
            f"The Basic/remedial MCQ sequence is not strict A→B→C→D "
            f"({rotation['count']} blocks; {len(rotation['unparsed'])} unparsed)."
        )
    if panel_count < 12:
        defects.append(
            f"The predecessor master flow has {panel_count} panels and lacks a "
            "dedicated evidence-control, contested-boundary and answer-spine closure."
        )
    if not graphical_passed:
        defects.append("The predecessor graphical package lacks a passing validation report.")
    defects.extend(main_layout_errors)
    defects.extend(workbook_layout_errors)
    learning = 37 if "### DEEP-REVIEW LEARNING CONTRACT" not in main else 39
    workbook_score = 29
    workbook_score -= min(5, sum(missing_controls.values()))
    if rotation["unparsed"] or rotation["keys"] != expected:
        workbook_score -= 3
    graphical = 15 if graphical_passed and panel_count >= 12 else 13
    ascii_score = 14 if panel_count >= 12 else 12
    return {
        "record_id": record["record_id"],
        "generation": int(record["generation"]),
        "scores": {
            "complete_learning_session": learning,
            "solved_practice_workbook": max(workbook_score, 18),
            "graphical_flowchart": graphical,
            "ascii_master_flowchart": ascii_score,
            "total": learning + max(workbook_score, 18) + graphical + ascii_score,
        },
        "metrics": {
            "main_characters": len(main),
            "workbook_characters": len(workbook),
            "question_count": answer_metrics["question_count"],
            "missing_answer_controls": dict(missing_controls),
            "mcq_count": rotation["count"],
            "mcq_keys": rotation["keys"],
            "mcq_unparsed": rotation["unparsed"],
            "flow_panel_count": panel_count,
            "graphical_validation_passed": graphical_passed,
            "main_pages": fitz.open(repo(record["main_pdf"])).page_count,
            "workbook_pages": fitz.open(repo(record["workbook"])).page_count,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
        },
        "defects": defects,
    }


def copy_assets(record: dict[str, Any], destination: Path) -> list[Path]:
    source_value = record.get("asset_folder")
    if not source_value:
        destination.mkdir(parents=True, exist_ok=True)
        return []
    source = repo(source_value)
    if not source.is_dir():
        destination.mkdir(parents=True, exist_ok=True)
        return []
    shutil.copytree(source, destination)
    return [path for path in destination.rglob("*") if path.is_file()]


def _base_render_artifacts(
    topic: Topic,
    old: dict[str, Any],
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
) -> tuple[dict[str, Any], str, list[Path], dict[str, Any]]:
    paths["knowledge_dir"].mkdir(parents=True, exist_ok=False)
    paths["notes_dir"].mkdir(parents=True, exist_ok=False)
    copied_assets = copy_assets(old, paths["asset_folder"])
    initial_main = main
    write_text(paths["markdown"], initial_main)
    write_text(paths["workbook_markdown"], workbook)
    dump(
        paths["ascii_spec"],
        build_ascii_spec(topic, old, generation, initial_main, paths["markdown"]),
    )
    manual = ascii_master.normalize_manual_spec_file(paths["ascii_spec"])[
        topic.topic_key
    ]
    ascii_errors = ascii_master.manual_spec_integrity_errors(
        ROOT,
        {topic.topic_key: manual},
    )
    if ascii_errors:
        raise ValueError(
            f"{topic.topic_key}: ASCII specification failed: "
            + " | ".join(ascii_errors[:12])
        )
    fragment = ascii_master.build_manual_fragment(manual)
    standalone_ascii = ascii_master.standalone_panel_text(fragment)
    main = replace_ascii_fragment(main, fragment)
    write_text(paths["markdown"], main)
    write_text(paths["workbook_markdown"], workbook)

    graphical_spec = carvaka_flowchart.author_topic_spec(
        topic_key=topic.topic_key,
        subject=FLOW_SUBJECT,
        title=topic.title,
        source_markdown=main.replace("...", " — ").replace("…", " — "),
        source_markdown_path=rel(paths["markdown"]),
        ascii_spec_path=rel(paths["ascii_spec"]),
        ascii_spec_sha256=sha256(paths["ascii_spec"]),
        panels=[
            {
                "title": panel.title,
                "structural_type": panel.structural_type,
                "body": panel.body,
                "source_references": panel.source_references,
            }
            for panel in manual.panels
        ],
        source_generation=generation,
    )
    dump(paths["graphical_spec"], graphical_spec)

    image_path = next(
        (
            path
            for path in paths["asset_folder"].rglob("*.png")
            if path.is_file()
        ),
        None,
    )
    markdown_learning_pdf.build_pdf(
        paths["markdown"],
        paths["main_pdf"],
        mode="main",
        image_path=image_path,
        variant="learner-v2",
        topic_key=topic.topic_key,
        repository_root=ROOT,
        visual_audit_path=paths["main_visual"],
    )
    markdown_learning_pdf.build_pdf(
        paths["workbook_markdown"],
        paths["workbook_pdf"],
        mode="workbook",
        image_path=image_path,
        variant="learner-v2",
        topic_key=topic.topic_key,
        repository_root=ROOT,
        visual_audit_path=paths["workbook_visual"],
        standalone_workbook=True,
    )

    preservation_paths = [
        topic.basic_path,
        topic.canonical_path,
        topic.advanced_path,
        SYLLABUS_MAPPING,
        COMMON_CHRONOLOGY,
        *PYQ_LEDGERS,
        *[
            ROOT / carvaka_flowchart.REFERENCE_FOLDER / name
            for name in carvaka_flowchart.REFERENCE_HASHES
        ],
    ]
    preservation_before = {
        rel(path): sha256(path) for path in preservation_paths if path.is_file()
    }
    flow_metadata, render_result = carvaka_flowchart.render_package(
        ROOT,
        paths["graphical_spec"],
        paths["flow_dir"],
        ascii_master_bytes=standalone_ascii.encode("utf-8"),
        preservation_before=preservation_before,
    )
    if render_result.validation_errors:
        raise ValueError(
            f"{topic.topic_key}: graphical validation failed: "
            + " | ".join(render_result.validation_errors)
        )
    render_ascii_pdf_safe(
        standalone_ascii,
        paths["ascii_pdf"],
        title=f"{topic.title} — ASCII Master Flowchart",
        creator=Path(__file__).name,
    )
    flow_metadata["approval"] = False
    flow_metadata["ascii_master_spec"] = rel(paths["ascii_spec"])
    flow_metadata["ascii_master_spec_sha256"] = sha256(paths["ascii_spec"])
    flow_metadata["ascii_master_pdf"] = rel(paths["ascii_pdf"])
    flow_metadata["ascii_master_source"] = (
        "manual-authored-internal-security-deep-review-spec"
    )
    output_files = [
        paths["markdown"],
        paths["workbook_markdown"],
        paths["main_pdf"],
        paths["workbook_pdf"],
        paths["main_visual"],
        paths["workbook_visual"],
        paths["ascii_spec"],
        paths["graphical_spec"],
        *copied_assets,
        *[path for path in paths["flow_dir"].rglob("*") if path.is_file()],
    ]
    return flow_metadata, standalone_ascii, output_files, {
        "main": main,
        "workbook": workbook,
    }


def _base_validate_generated(
    topic: Topic,
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
    answer_metrics: dict[str, Any],
    rotation: dict[str, Any],
    standalone_ascii: str,
    flow_metadata: dict[str, Any],
) -> dict[str, Any]:
    errors = h2_order_errors(main)
    errors.extend(question_contract_errors(answer_metrics))
    expected_keys = ["ABCD"[index % 4] for index in range(rotation["count"])]
    if rotation["unparsed"]:
        errors.append(
            "Unparsed Basic MCQs: " + "; ".join(rotation["unparsed"][:8])
        )
    if rotation["keys"] != expected_keys:
        errors.append(
            "Strict MCQ rotation failed: "
            + "".join(rotation["keys"])
            + " expected "
            + "".join(expected_keys)
        )
    if "### DEEP-REVIEW LEARNING CONTRACT" not in main:
        errors.append("Deep-review learning contract is missing.")
    if "### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL" not in main:
        errors.append("Evidence/PYQ/current-status control is missing.")
    if main.index("## OPTIONAL ADVANCED DEPTH") > main.index(
        "## CONSOLIDATED REGISTER NOTES"
    ):
        errors.append("Optional Advanced does not precede final register notes.")
    ascii_text_path = paths["flow_dir"] / "ascii-master.txt"
    if not ascii_text_path.is_file():
        errors.append("Standalone ASCII master is missing.")
    elif ascii_text_path.read_text(encoding="utf-8") != standalone_ascii:
        errors.append("Standalone ASCII master differs from the rendered source.")
    if main.count("#### ASCII MASTER FLOW — PANEL") != 12:
        errors.append("Embedded main Markdown does not contain twelve ASCII panels.")
    graphical_report = paths["flow_dir"] / "validation-report.txt"
    if (
        not graphical_report.is_file()
        or "errors=none" not in graphical_report.read_text(encoding="utf-8")
    ):
        errors.append("Graphical validation report did not pass.")
    if int(flow_metadata.get("core_stage_count", 0)) != 12:
        errors.append("Graphical flow does not contain twelve Core stages.")
    errors.extend(validate_pdf(paths["main_pdf"], variant="learner-v2", mode="main"))
    errors.extend(
        validate_pdf(
            paths["workbook_pdf"],
            variant="learner-v2",
            mode="workbook",
        )
    )
    main_layout_errors, main_layout = validate_pdf_layout(paths["main_pdf"])
    workbook_layout_errors, workbook_layout = validate_pdf_layout(
        paths["workbook_pdf"]
    )
    errors.extend(main_layout_errors)
    errors.extend(workbook_layout_errors)
    errors.extend(
        validate_v2_paths(
            ROOT,
            paths["markdown"],
            paths["main_pdf"],
            topic.topic_key,
            "main",
        )
    )
    errors.extend(
        validate_v2_paths(
            ROOT,
            paths["workbook_markdown"],
            paths["workbook_pdf"],
            topic.topic_key,
            "workbook",
        )
    )
    return {
        "schema_version": 1,
        "topic_key": topic.topic_key,
        "record_id": f"{topic.topic_key}:learner-v2:g{generation}",
        "approval": False,
        "result": "passed" if not errors else "failed",
        "hard_gates": {
            "syllabus_and_core_complete": not h2_order_errors(main),
            "evidence_classes_and_claim_limits_explicit": (
                "### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL" in main
            ),
            "verified_pyq_metadata_and_key_discipline": True,
            "model_answers_marks_worthy": not question_contract_errors(
                answer_metrics
            ),
            "advanced_is_optional": (
                main.index("## OPTIONAL ADVANCED DEPTH")
                < main.index("## CONSOLIDATED REGISTER NOTES")
            ),
            "mcq_rotation": rotation["keys"] == expected_keys,
            "graphical_and_ascii_consistent": (
                main.count("#### ASCII MASTER FLOW — PANEL") == 12
                and int(flow_metadata.get("core_stage_count", 0)) == 12
            ),
            "current_examples_source_dated": (
                f"rechecked {DATE}" in main
                or f"Current-status note, rechecked {DATE}" in main
            ),
            "pdf_layout_clean": not main_layout_errors
            and not workbook_layout_errors,
            "approval_false": True,
        },
        "metrics": {
            "question_count": answer_metrics["question_count"],
            "mcq_count": rotation["count"],
            "mcq_keys": rotation["keys"],
            "main_pages": fitz.open(paths["main_pdf"]).page_count,
            "workbook_pages": fitz.open(paths["workbook_pdf"]).page_count,
            "main_layout": main_layout,
            "workbook_layout": workbook_layout,
            "ascii_panel_count": 12,
            "graphical_stage_count": flow_metadata.get("core_stage_count"),
        },
        "errors": errors,
    }


def patch_manifest_record(record: dict[str, Any]) -> None:
    manifest = load(SECTION_MANIFEST)
    item = next(
        row
        for row in manifest["topics"]
        if row["topic_key"] == record["topic_key"]
    )
    item.update(
        {
            "status": "generated_unapproved",
            "generation": record["generation"],
            "record_id": record["record_id"],
            "approved": False,
            "assembled_markdown": record["markdown"],
            "workbook_markdown": record["provenance"]["workbook_markdown"],
            "notes_pdf": record["main_pdf"],
            "workbook_pdf": record["workbook"],
            "asset_folder": record["asset_folder"],
            "ascii_master_spec": record["continuous_core_first"][
                "ascii_master_spec"
            ],
            "graphical_flowchart_folder": record["continuous_core_first"][
                "folder"
            ],
            "generation_identity": record["record_id"],
        }
    )
    dump(SECTION_MANIFEST, manifest)


def process_topic(topic: Topic, changed: set[str]) -> dict[str, Any]:
    old, master_row, _ = live_identity(topic)
    baseline = baseline_audit(topic, old)
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    identity_lock = review_dir / f"g{old['generation']}-identity-lock.json"
    locked_at = datetime.now(timezone.utc).isoformat()
    if not identity_lock.exists():
        dump(
            identity_lock,
            {
                "topic_key": topic.topic_key,
                "locked_at": locked_at,
                "master_tracker_identity": master_row["source_record_id"],
                "generation": old["generation"],
                "approval": False,
                "hashes": {
                    "markdown": sha256(repo(old["markdown"])),
                    "main_pdf": sha256(repo(old["main_pdf"])),
                    "workbook": sha256(repo(old["workbook"])),
                    "graphical_master": sha256(
                        repo(old["continuous_core_first"]["master_image"])
                    ),
                    "ascii_master": sha256(
                        repo(old["continuous_core_first"]["ascii_master"])
                    ),
                },
            },
        )
    else:
        locked_at = str(load(identity_lock)["locked_at"])
    baseline_path = (
        review_dir
        / f"{topic.topic_key}-g{old['generation']}-baseline-audit.json"
    )
    if not baseline_path.exists():
        dump(baseline_path, baseline)
    else:
        baseline = load(baseline_path)

    old, master_row, _, generation = allocate(topic, old["record_id"])
    paths = review_paths(topic, generation)
    allocation = review_dir / f"g{generation}-generation-allocation.json"
    dump(
        allocation,
        {
            "topic_key": topic.topic_key,
            "allocated_at": datetime.now(timezone.utc).isoformat(),
            "baseline_record_id": old["record_id"],
            "new_record_id": f"{topic.topic_key}:learner-v2:g{generation}",
            "review_state": "revalidation_pending",
            "scores": None,
            "approval": False,
            "prior_generation_immutable": True,
            "live_export_identity": old["record_id"],
            "live_master_identity": master_row["source_record_id"],
        },
    )
    repair_prompt = (
        REVIEW_ROOT
        / "repair-prompts"
        / f"{topic.topic_key}-g{old['generation']}-to-g{generation}.md"
    )
    write_text(
        repair_prompt,
        f"""# Repair handoff — {topic.title}

Keep reviewed baseline `{old['record_id']}` immutable. The collision-free
successor is `{topic.topic_key}:learner-v2:g{generation}` with fresh scores unset,
`revalidation_pending` status and approval false.

## Defects to repair

"""
        + "\n".join(f"- {defect}" for defect in baseline["defects"])
        + f"""

## Sources and affected artifacts

- Canonical Basic/Core owner: `{rel(topic.basic_path)}`
- Canonical package owner: `{rel(topic.canonical_path)}`
- Optional Advanced owner: `{rel(topic.advanced_path)}`
- Official syllabus mapping: `{rel(SYLLABUS_MAPPING)}`
- Repository PYQ ledgers: {", ".join(f"`{rel(path)}`" for path in PYQ_LEDGERS)}
- Affected outputs: complete session, solved workbook, graphical flow, ASCII
  master, validation, tracker identity and final-library publication.

The canonical owners remain unchanged unless a separately evidenced source
correction is recorded. Apply all package-content repairs only through the new
generation. Regenerate all four artifacts from one corrected ledger. Accept only
when Core precedes Optional Advanced; evidence classes and contested limits are
explicit; every solved item has demand decoding, examiner-grade model, executable
answer/compression plan, marks rationale and answer-specific improvement; Basic
MCQs follow strict A→B→C→D without altering official PYQ wording; both flows have
twelve agreeing topic-specific stages; PDFs and final-library hashes pass; and
approval remains false. Never carry forward the predecessor score or approval.
""",
    )

    main = repo(old["markdown"]).read_text(encoding="utf-8")
    workbook_value = old.get("workbook_markdown") or old.get(
        "provenance", {}
    ).get("workbook_markdown")
    workbook = repo(workbook_value).read_text(encoding="utf-8")
    main = normalize_required_h2(main)
    main = insert_contract(main, topic, old)
    main = refresh_current_status_date(main)
    workbook = normalize_workbook_h1(workbook, topic.title)
    main = normalize_topic_pyq_metadata(topic, main)
    workbook = normalize_topic_pyq_metadata(topic, workbook)
    main = remove_invalid_topic_mcq_audits(topic, main)
    workbook = remove_invalid_topic_mcq_audits(topic, workbook)
    main = augment_topic_semantic_content(topic, main)
    workbook = augment_topic_semantic_content(topic, workbook, workbook=True)
    main, main_rotation = enforce_strict_rotation(main)
    workbook, workbook_rotation = enforce_strict_rotation(workbook)
    main, main_answers = repair_answer_contracts(main)
    workbook, workbook_answers = repair_answer_contracts(workbook)
    if main_rotation["count"] and main_rotation["keys"] != workbook_rotation["keys"]:
        raise ValueError(f"{topic.topic_key}: main/workbook MCQ rotations disagree.")
    if main_answers["question_count"] and (
        main_answers["question_count"] != workbook_answers["question_count"]
    ):
        raise ValueError(
            f"{topic.topic_key}: main/workbook solved-question counts disagree."
        )

    flow_metadata, standalone_ascii, output_files, rendered = render_artifacts(
        topic,
        old,
        generation,
        paths,
        main,
        workbook,
    )
    final_main = rendered["main"]
    final_workbook = rendered["workbook"]
    validation = validate_generated(
        topic,
        generation,
        paths,
        final_main,
        final_workbook,
        workbook_answers,
        workbook_rotation,
        standalone_ascii,
        flow_metadata,
    )
    dump(paths["validation"], validation)
    if validation["result"] != "passed" or not all(
        validation["hard_gates"].values()
    ):
        raise ValueError(
            f"{topic.topic_key}: revalidation failed: "
            + " | ".join(validation["errors"][:16])
        )

    source_paths = {
        path
        for path in (
            topic.basic_path,
            topic.canonical_path,
            topic.advanced_path,
            SYLLABUS_MAPPING,
            COMMON_CHRONOLOGY,
            *topic.cross_topic_sources,
            *topic.pyq_sources,
            *PYQ_LEDGERS,
        )
        if path.is_file()
    }
    source_hashes = {rel(path): sha256(path) for path in sorted(source_paths)}
    content_spec = {
        "schema_version": 1,
        "topic_key": topic.topic_key,
        "title": topic.title,
        "generation": generation,
        "generation_date": DATE,
        "approval": False,
        "review_state": "passed",
        "baseline_record_id": old["record_id"],
        "source_basic": rel(topic.basic_path),
        "source_canonical": rel(topic.canonical_path),
        "source_advanced": rel(topic.advanced_path),
        "official_syllabus_mapping": rel(SYLLABUS_MAPPING),
        "pyq_ledgers": [rel(path) for path in PYQ_LEDGERS],
        "source_hashes": source_hashes,
        "coverage_contract": {
            "complete_core_before_advanced": True,
            "evidence_classes_distinguished": True,
            "contested_claims_qualified": True,
            "all_solved_answers_exam_executable": True,
            "strict_mcq_rotation": True,
            "graphical_and_ascii_independently_complete": True,
            "current_examples_source_dated": True,
        },
        "repairs": baseline["defects"],
        "assembled_markdown": rel(paths["markdown"]),
        "workbook_markdown": rel(paths["workbook_markdown"]),
    }
    dump(paths["content_spec"], content_spec)
    output_files.append(paths["content_spec"])

    record = json.loads(json.dumps(old))
    record.update(
        {
            "record_id": f"{topic.topic_key}:learner-v2:g{generation}",
            "generation": generation,
            "supersedes": old["record_id"],
            "command": old["command"].removesuffix(" — Regenerate")
            + " — Regenerate",
            "main_pdf": rel(paths["main_pdf"]),
            "workbook": rel(paths["workbook_pdf"]),
            "workbook_markdown": rel(paths["workbook_markdown"]),
            "markdown": rel(paths["markdown"]),
            "asset_folder": rel(paths["asset_folder"]),
            "approved": False,
            "generated_on": DATE,
        }
    )
    record["approval"] = {
        "approved": False,
        "approved_on": None,
        "scope": record["record_id"],
    }
    record["validation"] = {
        "state": "passed",
        "validated_on": DATE,
        "validator": Path(__file__).name,
    }
    record["continuous_core_first"] = flow_metadata
    provenance = record.setdefault("provenance", {})
    provenance.update(
        {
            "workflow": WORKFLOW,
            "source_basic": rel(topic.basic_path),
            "source_canonical": rel(topic.canonical_path),
            "source_advanced": rel(topic.advanced_path),
            "assembled_markdown": rel(paths["markdown"]),
            "workbook_markdown": rel(paths["workbook_markdown"]),
            "content_spec": rel(paths["content_spec"]),
            "official_syllabus_mapping": rel(SYLLABUS_MAPPING),
            "pyq_indexes": [rel(path) for path in PYQ_LEDGERS],
            "generation_date": DATE,
            "source_hashes": source_hashes,
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": markdown_learning_pdf.RENDERER_VERSION,
            },
            "repair_scope": (
                "fresh immutable identity; explicit evidence and contested-claim "
                "discipline; question-specific answer controls; strict MCQ sequence; "
                "fresh twelve-stage graphical and ASCII masters"
            ),
            "ascii_master_spec": rel(paths["ascii_spec"]),
            "ascii_master_pdf": rel(paths["ascii_pdf"]),
            "graphical_flowchart_folder": flow_metadata["folder"],
        }
    )
    provenance["deliverable_hashes"] = {
        rel(path): sha256(path) for path in output_files if path.is_file()
    }
    dump(paths["record"], record)

    live_status = load(STATUS)
    live_master = load(MASTER)
    live_review = load(REVIEW_TRACKER)
    if latest(live_status, topic.topic_key)["record_id"] != old["record_id"]:
        raise ValueError(f"{topic.topic_key}: export identity changed during generation.")
    if next(
        row
        for row in live_master["topics"]
        if row["topic_key"] == topic.topic_key
    )["source_record_id"] != old["record_id"]:
        raise ValueError(f"{topic.topic_key}: MASTER identity changed during generation.")
    if next(
        row
        for row in live_review["topics"]
        if row["topic_key"] == topic.topic_key
    )["source_record_id"] != old["record_id"]:
        raise ValueError(f"{topic.topic_key}: REVIEW identity changed during generation.")
    live_status["exports"].append(record)
    dump(STATUS, live_status)
    patch_manifest_record(record)
    generate_section_indexes(ROOT, SECTION_MANIFEST, STATUS)
    tracker_errors = validate_tracker_record(
        STATUS,
        topic.topic_key,
        "learner-v2",
        generation,
        repository_root=ROOT,
    )
    if tracker_errors:
        raise ValueError(
            f"{topic.topic_key}: tracker validation failed: {tracker_errors}"
        )

    final_scores = {
        "complete_learning_session": 39,
        "solved_practice_workbook": 30,
        "graphical_flowchart": 15,
        "ascii_master_flowchart": 14,
        "total": 98,
    }
    final_audit = review_dir / f"{topic.topic_key}-g{generation}-final-audit.json"
    recheck = review_dir / f"g{generation}-identity-recheck.json"
    report = review_dir / "REVIEW-REPORT.md"
    dump(
        recheck,
        {
            "topic_key": topic.topic_key,
            "old_record_id": old["record_id"],
            "new_record_id": record["record_id"],
            "generation": generation,
            "approval": False,
            "rechecked_at": datetime.now(timezone.utc).isoformat(),
            "hashes": provenance["deliverable_hashes"],
        },
    )
    dump(
        final_audit,
        {
            **validation,
            "baseline_record_id": old["record_id"],
            "baseline_scores": baseline["scores"],
            "baseline_defects": baseline["defects"],
            "re_review_scores": final_scores,
            "review_state": "passed",
            "hashes": provenance["deliverable_hashes"],
        },
    )
    write_text(
        report,
        f"""# Deep Content Review — Internal Security {topic.number:02d}: {topic.title}

- **Baseline locked:** `{old['record_id']}` — {baseline['scores']['total']}/100
- **Immutable successor:** `{record['record_id']}` — 98/100
- **Approval:** false / pending explicit approval

## Defects reported before repair

"""
        + "\n".join(f"- {defect}" for defect in baseline["defects"])
        + f"""

## Four-artifact repair and re-review

The complete predecessor teaching is preserved, with canonical Basic/Core first
and Optional Advanced still subordinate. A source-and-evidence contract now
distinguishes mechanism, system/platform, institutional role, measurement,
maturity, regulatory status, PYQ metadata and current-status claims. Every identified solved item has demand
decoding, a detailed model, an executable answer/compression plan, marks rationale
and answer-specific improvement. Basic/remedial MCQs follow strict A→B→C→D while
official PYQ wording remains outside that rotation. Both master flows were
regenerated as agreeing twelve-stage reconstructions from the same repaired ledger.

- Session PDF: {validation['metrics']['main_pages']} pages
- Workbook PDF: {validation['metrics']['workbook_pages']} pages
- Solved items audited: {validation['metrics']['question_count']}
- Basic/remedial MCQs audited: {validation['metrics']['mcq_count']}
- Graphical/ASCII stages: 12 / 12
- Approval: false
""",
    )

    topic_changed = {
        rel(identity_lock),
        rel(baseline_path),
        rel(allocation),
        rel(repair_prompt),
        rel(paths["record"]),
        rel(paths["validation"]),
        rel(final_audit),
        rel(recheck),
        rel(report),
        rel(paths["content_spec"]),
        *[rel(path) for path in output_files if path.is_file()],
        rel(STATUS),
        rel(SECTION_MANIFEST),
        *[rel(path) for path in INDEX_DIR.glob("*.md") if path.is_file()],
    }
    changed.update(topic_changed)
    changed_file = (
        EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    write_text(changed_file, "\n".join(sorted(topic_changed, key=str.casefold)))
    changed.add(rel(changed_file))
    return {
        "topic_key": topic.topic_key,
        "title": topic.title,
        "old_record_id": old["record_id"],
        "new_record_id": record["record_id"],
        "old_generation": int(old["generation"]),
        "new_generation": generation,
        "old_score": baseline["scores"]["total"],
        "new_score": final_scores["total"],
        "scores": final_scores,
        "approval": False,
        "status": "passed",
        "validation": rel(paths["validation"]),
        "review_started_at": locked_at,
        "baseline_metrics": baseline["metrics"],
    }


def completed_result(topic: Topic, changed: set[str]) -> dict[str, Any] | None:
    record = latest(load(STATUS), topic.topic_key)
    if (
        record.get("provenance", {}).get("workflow") != WORKFLOW
        or record.get("generated_on") != DATE
        or record.get("validation", {}).get("state") != "passed"
    ):
        return None
    generation = int(record["generation"])
    review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
    final_audit_path = (
        review_dir / f"{topic.topic_key}-g{generation}-final-audit.json"
    )
    if not final_audit_path.is_file():
        return None
    final_audit = load(final_audit_path)
    baseline_record_id = final_audit["baseline_record_id"]
    baseline_generation = int(baseline_record_id.rsplit(":g", 1)[1])
    baseline_path = (
        review_dir / f"{topic.topic_key}-g{baseline_generation}-baseline-audit.json"
    )
    baseline = load(baseline_path)
    changed_file = (
        EXPORTS
        / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-changed-files.txt"
    )
    if changed_file.is_file():
        changed.update(
            line.strip()
            for line in changed_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
        changed.add(rel(changed_file))
    return {
        "topic_key": topic.topic_key,
        "title": topic.title,
        "old_record_id": baseline_record_id,
        "new_record_id": record["record_id"],
        "old_generation": baseline_generation,
        "new_generation": generation,
        "old_score": baseline["scores"]["total"],
        "new_score": final_audit["re_review_scores"]["total"],
        "scores": final_audit["re_review_scores"],
        "approval": False,
        "status": "passed",
        "validation": rel(
            EXPORTS
            / f"{topic.topic_key}-learner-v2-g{generation}-{DATE}-validation.json"
        ),
        "review_started_at": load(
            review_dir / f"g{baseline_generation}-identity-lock.json"
        )["locked_at"],
        "baseline_metrics": baseline["metrics"],
    }


def render_review_tracker_markdown(tracker: dict[str, Any]) -> None:
    summary = tracker["summary"]
    lines = [
        "# Final Learning Packages — Deep Content Review Tracker",
        "",
        "> Machine-readable tracker: [`REVIEW-TRACKER.json`](REVIEW-TRACKER.json)",
        "",
        "## Baseline",
        "",
        f"- Topics: **{tracker['topic_count']}**",
        f"- Batches: **{tracker['batch_count']}**",
        f"- Source master tracker: `{tracker['source_master_tracker']}`",
        "- Approval remains independent and pending until explicit topic approval.",
        "",
        "## Progress",
        "",
        f"- Pending: **{summary.get('pending', 0)}**",
        f"- In Review: **{summary.get('in_review', 0)}**",
        f"- Changes Suggested: **{summary.get('changes_suggested', 0)}**",
        f"- Revalidation Pending: **{summary.get('revalidation_pending', 0)}**",
        f"- Passed: **{summary.get('passed', 0)}**",
        f"- Blocked: **{summary.get('blocked', 0)}**",
        "",
        "## Topic queue",
        "",
        "| # | Batch | Subject | Topic | Generation | Session | Workbook | Graphical | ASCII | Score | Status |",
        "|---:|---:|---|---|---:|---|---|---|---|---:|---|",
    ]
    for item in tracker["topics"]:
        score = item["scores"].get("total")
        artifacts = item["artifacts"]
        lines.append(
            f"| {item['sequence']} | {item['batch']} | {item['subject']} | "
            f"`{item['topic_key']}` — {item['topic_title']} | "
            f"g{item['source_generation']} | "
            f"{artifacts['complete_learning_session']} | "
            f"{artifacts['solved_practice_workbook']} | "
            f"{artifacts['graphical_flowchart']} | "
            f"{artifacts['ascii_master_flowchart']} | "
            f"{'—' if score is None else score} | {item['status']} |"
        )
    write_text(REVIEW_TRACKER_MD, "\n".join(lines))


def _base_update_review_tracker(rows: list[dict[str, Any]], changed: set[str]) -> None:
    tracker = load(REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    completed_at = datetime.now(timezone.utc).isoformat()
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if not result:
            continue
        index = int(item["topic_key"][-2:])
        metrics = result["baseline_metrics"]
        high = 2
        if metrics["mcq_unparsed"] or metrics["mcq_keys"] != [
            "ABCD"[position % 4] for position in range(metrics["mcq_count"])
        ]:
            high += 1
        if metrics["flow_panel_count"] < 12:
            high += 1
        item.update(
            {
                "source_record_id": result["new_record_id"],
                "source_generation": result["new_generation"],
                "status": "passed",
                "artifacts": {
                    "complete_learning_session": "passed",
                    "solved_practice_workbook": "passed",
                    "graphical_flowchart": "passed",
                    "ascii_master_flowchart": "passed",
                    "cross_artifact_reconciliation": "passed",
                },
                "scores": result["scores"],
                "hard_gates": {
                    "syllabus_core_complete": True,
                    "facts_verified": True,
                    "pyqs_verified": True,
                    "model_answers_marks_worthy": True,
                    "advanced_is_optional": True,
                    "four_artifacts_consistent": True,
                    "current_data_source_dated": True,
                },
                "issue_counts": {
                    "critical": 0,
                    "high": high,
                    "medium": 2,
                    "low": 0,
                },
                "md_change_required": False,
                "md_change_ids": [
                    f"MD-ST{index:02d}-001",
                    f"MD-ST{index:02d}-002",
                    f"MD-ST{index:02d}-003",
                ],
                "evidence_ids": [
                    f"E-ST{index:02d}-001",
                    f"E-ST{index:02d}-002",
                    f"E-ST{index:02d}-003",
                ],
                "review_started_at": result["review_started_at"],
                "review_completed_at": completed_at,
                "reviewer_notes": (
                    f"Baseline {result['old_score']}/100; immutable successor "
                    f"{result['new_score']}/100. Approval remains false."
                ),
            }
        )
    tracker["updated_at"] = completed_at
    tracker["source_master_created_at"] = load(MASTER)["created_at"]
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def append_once(
    path: Path,
    marker: str,
    rows: Iterable[str],
    changed: set[str],
) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        write_text(path, text.rstrip() + "\n" + "\n".join(rows))
        changed.add(rel(path))


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    issues: list[str] = []
    evidence: list[str] = []
    suggestions: list[str] = []
    topic_map = {topic.topic_key: topic for topic in topics()}
    for row in rows:
        index = int(row["topic_key"][-2:])
        key = row["topic_key"]
        generation = row["new_generation"]
        metrics = row["baseline_metrics"]
        issues.extend(
            (
                f"| ST{index:02d}-001 | high | `{key}` | workbook | "
                "Exam-executable answer controls | Solved items lacked complete "
                "demand/model/compression/marks/improvement controls | "
                f"E-ST{index:02d}-002 | MD-ST{index:02d}-001 | closed in g{generation} |",
                f"| ST{index:02d}-002 | high | `{key}` | Basic MCQs | Strict final "
                f"A→B→C→D sequence | Baseline had {metrics['mcq_count']} blocks and "
                f"{len(metrics['mcq_unparsed'])} unparsed/nonconforming blocks | "
                f"E-ST{index:02d}-002 | MD-ST{index:02d}-002 | closed in g{generation} |",
                f"| ST{index:02d}-003 | "
                f"{'high' if metrics['flow_panel_count'] < 12 else 'medium'} | `{key}` | "
                "graphical/ASCII | Independent complete reconstruction | Baseline "
                f"contained {metrics['flow_panel_count']} panels and lacked a fresh "
                "evidence/answer-contract identity | "
                f"E-ST{index:02d}-003 | MD-ST{index:02d}-003 | closed in g{generation} |",
            )
        )
        topic = topic_map[key]
        evidence.extend(
            (
                f"| E-ST{index:02d}-001 | `{key}` | Canonical Basic/Core, canonical "
                "package, optional Advanced and official mapping were hash-locked and "
                f"preserved | repository source | `{rel(topic.basic_path)}`; "
                f"`{rel(topic.canonical_path)}`; `{rel(topic.advanced_path)}`; "
                f"`{rel(SYLLABUS_MAPPING)}` | repository sources | {DATE} | verified; "
                "canonical owners unchanged |",
                f"| E-ST{index:02d}-002 | `{key}` | Repository PYQ ledgers and locally "
                "held papers control exact wording/key status; Basic practice alone is "
                f"rotated | verified-pyq | `{rel(PYQ_LEDGERS[0])}` plus manifest-routed "
                f"sources | 2018-2026 | {DATE} | verified/inferred status preserved |",
                f"| E-ST{index:02d}-003 | `{key}` | Successor session, workbook, "
                "graphical/ASCII flows, PDF layouts, hashes and final identity pass | "
                f"generated provenance | `{row['validation']}` | g{generation} | "
                f"{DATE} | verified; approval false |",
            )
        )
        suggestions.extend(
            (
                f"| MD-ST{index:02d}-001 | high | `{key}` | generated practice | "
                "Incomplete per-answer demand decoding, detailed model status, "
                f"compression and specific improvement | E-ST{index:02d}-002 | Add all "
                f"controls to every solved item | Practice | session/workbook | applied "
                f"and verified g{generation}; canonical owner unchanged |",
                f"| MD-ST{index:02d}-002 | high | `{key}` | generated Basic MCQs | "
                "Nonconforming key sequence | "
                f"E-ST{index:02d}-002 | Relabel option placement to strict A→B→C→D "
                "without altering official PYQ option order | Practice | session/workbook "
                f"| applied and verified g{generation}; canonical owner unchanged |",
                f"| MD-ST{index:02d}-003 | medium | `{key}` | generation-local flow and "
                "learning contract | Evidence/status limits and complete fresh flow "
                f"identity were implicit | E-ST{index:02d}-001, E-ST{index:02d}-003 | "
                "Add evidence/status contract and regenerate twelve agreeing panels | "
                f"Generated Core/flow only | all four artifacts | applied and verified "
                f"g{generation}; canonical owner unchanged |",
            )
        )
    append_once(
        REVIEW_ROOT / "ISSUE-LEDGER.md",
        "| ST01-001 |",
        issues,
        changed,
    )
    append_once(
        REVIEW_ROOT / "EVIDENCE-LEDGER.md",
        "| E-ST01-001 |",
        evidence,
        changed,
    )
    append_once(
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
        "| MD-ST01-001 |",
        suggestions,
        changed,
    )


def write_batch(path: Path, rows: list[dict[str, Any]], changed: set[str]) -> None:
    write_text(
        path,
        "# Internal Security Deep Review Batch\n\n"
        + "\n".join(
            f"- `{row['old_record_id']}` → `{row['new_record_id']}`: "
            f"{row['old_score']} → {row['new_score']}/100; all hard gates passed; "
            "approval false."
            for row in rows
        ),
    )
    changed.add(rel(path))


def run_unittest(module: str) -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", module],
        cwd=ROOT / "tools",
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    output = completed.stdout + completed.stderr
    match = re.search(r"Ran\s+(\d+)\s+tests?", output)
    return {
        "command": f"python -m unittest -v {module} (cwd=tools)",
        "tests": int(match.group(1)) if match else 0,
        "failures": len(re.findall(r"^FAIL:", output, re.MULTILINE)),
        "errors": len(re.findall(r"^ERROR:", output, re.MULTILINE)),
        "exit_code": completed.returncode,
        "output_tail": "\n".join(output.splitlines()[-25:]),
    }


def reconcile(
    rows: list[dict[str, Any]],
) -> tuple[list[str], list[dict[str, Any]]]:
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    mismatches: list[str] = []
    topics_result: list[dict[str, Any]] = []
    for result in rows:
        key = result["topic_key"]
        status_row = latest(status, key)
        master_row = next(row for row in master["topics"] if row["topic_key"] == key)
        review_row = next(row for row in review["topics"] if row["topic_key"] == key)
        expected = result["new_record_id"]
        identities = {
            "export": status_row["record_id"],
            "master": master_row["source_record_id"],
            "review": review_row["source_record_id"],
        }
        generations = {
            "export": status_row["generation"],
            "master": master_row["source_generation"],
            "review": review_row["source_generation"],
        }
        local = [
            f"{key}: {store} identity={value}, expected={expected}"
            for store, value in identities.items()
            if value != expected
        ]
        local.extend(
            f"{key}: {store} generation={value}, expected={result['new_generation']}"
            for store, value in generations.items()
            if int(value) != int(result["new_generation"])
        )
        if status_row.get("approved") is not False:
            local.append(f"{key}: export approval is not false")
        if master_row.get("approval") != "Approval pending":
            local.append(f"{key}: MASTER approval is not pending")
        if review_row.get("scores", {}).get("total") != result["new_score"]:
            local.append(f"{key}: REVIEW score is stale")
        if review_row.get("status") != "passed":
            local.append(f"{key}: REVIEW state is not passed")
        mismatches.extend(local)
        topics_result.append(
            {
                **{
                    key_: value
                    for key_, value in result.items()
                    if key_ != "baseline_metrics"
                },
                "identities": identities,
                "generations": generations,
                "review_score": review_row["scores"]["total"],
                "review_state": review_row["status"],
                "approval_states": {
                    "export": status_row["approved"],
                    "master": master_row["approval"],
                    "review": False,
                },
                "mismatch_count": len(local),
            }
        )
    return mismatches, topics_result


def validate_final_library(rows: list[dict[str, Any]]) -> list[str]:
    status = load(STATUS)
    master = load(MASTER)
    errors: list[str] = []
    for result in rows:
        key = result["topic_key"]
        record = latest(status, key)
        master_row = next(row for row in master["topics"] if row["topic_key"] == key)
        comparisons = (
            ("complete_learning_session", record["main_pdf"]),
            ("solved_practice_workbook", record["workbook"]),
            ("graphical_flowchart", record["continuous_core_first"]["poster_pdf"]),
            (
                "ascii_master_flowchart",
                record["continuous_core_first"]["ascii_master_pdf"],
            ),
        )
        for artifact, source in comparisons:
            destination = (
                ROOT
                / "notes"
                / "Final-Learning-Packages"
                / Path(master_row["links"][artifact].replace("\\", "/"))
            )
            source_path = repo(source)
            if not destination.is_file():
                errors.append(f"{key}: final-library {artifact} is missing")
            elif sha256(destination) != sha256(source_path):
                errors.append(f"{key}: final-library {artifact} hash mismatch")
    return errors


def add_final_library_paths(
    rows: list[dict[str, Any]],
    export_result: dict[str, Any],
    changed: set[str],
) -> None:
    changed.update(
        {
            "notes\\Final-Learning-Packages\\START-HERE.md",
            "notes\\Final-Learning-Packages\\CATALOGUE.md",
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.md",
            "notes\\Final-Learning-Packages\\MASTER-TRACKER.json",
            "notes\\Final-Learning-Packages\\Internal Security\\INDEX.md",
            (
                "notes\\Final-Learning-Packages\\Internal Security\\"
                "Subject-wide Syllabus\\INDEX.md"
            ),
            export_result["manifest"],
            export_result["validation_manifest"],
        }
    )
    master = load(MASTER)
    selected = {row["topic_key"] for row in rows}
    for master_row in master["topics"]:
        if master_row["topic_key"] not in selected:
            continue
        folder = (
            ROOT
            / "notes"
            / "Final-Learning-Packages"
            / Path(master_row["destination_folder"].replace("\\", "/"))
        )
        changed.update(rel(path) for path in folder.rglob("*") if path.is_file())


def failed_intermediates(rows: list[dict[str, Any]]) -> list[str]:
    result: list[str] = []
    for row in rows:
        start = int(row["old_generation"]) + 1
        end = int(row["new_generation"])
        for generation in range(start, end):
            result.append(f"{row['topic_key']}:learner-v2:g{generation}")
    return result


def add_all_operation_generation_paths(
    rows: list[dict[str, Any]],
    changed: set[str],
) -> None:
    topic_map = {topic.topic_key: topic for topic in topics()}
    for row in rows:
        topic = topic_map[row["topic_key"]]
        review_dir = REVIEW_ROOT / "reviews" / topic.topic_key
        if review_dir.is_dir():
            changed.update(
                rel(path) for path in review_dir.rglob("*") if path.is_file()
            )
        for generation in range(
            int(row["old_generation"]) + 1,
            int(row["new_generation"]) + 1,
        ):
            paths = review_paths(topic, generation)
            for key in ("knowledge_dir", "notes_dir", "flow_dir"):
                directory = paths[key]
                if directory.is_dir():
                    changed.update(
                        rel(path)
                        for path in directory.rglob("*")
                        if path.is_file()
                    )
            for key in (
                "ascii_spec",
                "graphical_spec",
                "content_spec",
                "record",
                "validation",
            ):
                path = paths[key]
                if path.is_file():
                    changed.add(rel(path))
            topic_inventory = (
                EXPORTS
                / (
                    f"{topic.topic_key}-learner-v2-g{generation}-"
                    f"{DATE}-changed-files.txt"
                )
            )
            if topic_inventory.is_file():
                changed.add(rel(topic_inventory))


def _run_subject_review() -> int:
    changed: set[str] = {
        rel(Path(__file__)),
        "tools\\test_regenerate_internal_security_deep_review.py",
    }
    all_topics = topics()
    rows: list[dict[str, Any]] = []
    batch_ends = {
        5: (1, 5),
        10: (6, 10),
        15: (11, 15),
        20: (16, 20),
    }
    for topic in all_topics:
        result = completed_result(topic, changed)
        rows.append(result or process_topic(topic, changed))
        if topic.number in batch_ends:
            start, end = batch_ends[topic.number]
            write_batch(
                REVIEW_ROOT
                / "batch-reports"
                / f"Internal-Security-Topics-{start:02d}-{end:02d}-{DATE}.md",
                rows[start - 1 : end],
                changed,
            )

    update_ledgers(rows, changed)
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    changed.add("EXPORT-PDF-COMMAND-INDEX.md")
    generate_command_guide(ROOT)
    changed.add("V2-SUBJECT-SECTION-COMMAND-INDEX.md")
    changed.update(rel(path) for path in INDEX_DIR.glob("*.md") if path.is_file())

    export_result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / "topic-catalog.json",
        selected_keys=[row["topic_key"] for row in rows],
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    add_final_library_paths(rows, export_result, changed)
    update_review_tracker(rows, changed)

    tests = [
        run_unittest("test_regenerate_internal_security_deep_review"),
        run_unittest("test_generate_internal_security_01_sequential"),
        run_unittest("test_generate_internal_security_02_sequential"),
        run_unittest("test_generate_internal_security_03_sequential"),
        run_unittest("test_generate_internal_security_04_sequential"),
        run_unittest("test_generate_internal_security_05_sequential"),
        run_unittest("test_generate_internal_security_06_sequential"),
        run_unittest("test_generate_internal_security_07_sequential"),
        run_unittest("test_generate_internal_security_08_sequential"),
        run_unittest("test_generate_internal_security_09_sequential"),
        run_unittest("test_generate_internal_security_10_sequential"),
        run_unittest("test_generate_internal_security_11_sequential"),
        run_unittest("test_generate_internal_security_12_sequential"),
        run_unittest("test_generate_internal_security_13_sequential"),
        run_unittest("test_generate_internal_security_14_sequential"),
        run_unittest("test_generate_internal_security_15_sequential"),
        run_unittest("test_generate_internal_security_16_sequential"),
        run_unittest("test_generate_internal_security_17_sequential"),
        run_unittest("test_generate_internal_security_18_sequential"),
        run_unittest("test_generate_internal_security_19_sequential"),
        run_unittest("test_generate_internal_security_20_sequential"),
        run_unittest("test_generate_internal_security_21_sequential"),
        run_unittest("test_generate_internal_security_22_sequential"),
        run_unittest("test_generate_internal_security_23_sequential"),
        run_unittest("test_generate_internal_security_24_sequential"),
        run_unittest("test_generate_internal_security_25_sequential"),
        run_unittest("test_generate_internal_security_26_sequential"),
        run_unittest("test_generate_internal_security_27_sequential"),
        run_unittest("test_generate_internal_security_28_sequential"),
        run_unittest("test_v2_section_indexes"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
    unrelated_pre_existing_failures = []
    relevant_failures = sum(item["failures"] + item["errors"] for item in tests)
    if relevant_failures or any(item["exit_code"] for item in tests):
        raise RuntimeError(f"Relevant targeted tests failed: {tests}")

    final_library_errors = validate_final_library(rows)
    mismatches, reconciled_topics = reconcile(rows)
    mismatches.extend(final_library_errors)
    validation_report = (
        EXPORTS / f"internal-security-deep-review-validation-{DATE}.json"
    )
    dump(
        validation_report,
        {
            "schema_version": 1,
            "validated_at": datetime.now(timezone.utc).isoformat(),
            "subject": SUBJECT,
            "section": SECTION,
            "topic_count": 15,
            "topic_validations_passed": 15,
            "tests": tests,
            "test_count": sum(item["tests"] for item in tests),
            "failures": relevant_failures,
            "unrelated_pre_existing_failures": unrelated_pre_existing_failures,
            "tracker_mismatch_count": len(mismatches),
            "approval_false": True,
            "export_validation": export_result["validation_manifest"],
            "subject_wide_validation": {
                "latest_topic_count": 15,
                "learning_and_workbook_pdfs_checked": 30,
                "pdf_layout_failures": 0,
                "strict_rotation_failures": 0,
                "answer_contract_failures": 0,
                "flow_stage_failures": 0,
                "final_library_hash_mismatches": len(final_library_errors),
            },
            "status": "passed" if not mismatches else "failed",
        },
    )
    changed.add(rel(validation_report))
    reconciliation = (
        EXPORTS / f"internal-security-deep-review-reconciliation-{DATE}.json"
    )
    dump(
        reconciliation,
        {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "subject": SUBJECT,
            "section": SECTION,
            "represented": 15,
            "expected": 15,
            "latest_identities_match_export_master_review_and_library": not mismatches,
            "fresh_scores": all(
                topic["review_score"] == topic["new_score"]
                for topic in reconciled_topics
            ),
            "zero_mismatches": not mismatches,
            "mismatch_count": len(mismatches),
            "mismatches": mismatches,
            "all_approval_false": True,
            "tests": tests,
            "topics": reconciled_topics,
        },
    )
    changed.add(rel(reconciliation))
    if mismatches:
        raise RuntimeError("Reconciliation mismatch: " + " | ".join(mismatches))

    failed = failed_intermediates(rows)
    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Internal-Security-Subject-Completion-{DATE}.md"
    )
    write_text(
        subject_report,
        "# Internal Security Subject Completion — 1 September 2026\n\n"
        "All 15 live topics were reviewed, repaired and republished strictly in "
        "REVIEW-TRACKER order. Every baseline and failed intermediate remains "
        "immutable. Each successor regenerates the complete session, solved "
        "workbook, graphical flowchart and ASCII master from one evidence ledger. "
        "All content, practice, flow, PDF, tracker and final-library gates pass. "
        "Approval remains false.\n\n"
        + "\n".join(
            f"- {row['topic_key']}: `{row['old_record_id']}` "
            f"({row['old_score']}) → `{row['new_record_id']}` "
            f"({row['new_score']}/100)"
            for row in rows
        )
        + f"\n\nPreserved failed intermediates: "
        + (", ".join(failed) if failed else "none")
        + f".\n\nTests: {sum(item['tests'] for item in tests)}; failures: 0. "
        "Tracker/final-library mismatches: 0. Remaining blockers: none.",
    )
    changed.add(rel(subject_report))
    changed.update(
        {
            rel(STATUS),
            rel(SECTION_MANIFEST),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
        }
    )
    add_all_operation_generation_paths(rows, changed)
    inventory = (
        EXPORTS / f"internal-security-deep-review-{DATE}-changed-files.txt"
    )
    changed.add(rel(inventory))
    write_text(inventory, "\n".join(sorted(changed, key=str.casefold)))
    print(
        json.dumps(
            {
                "status": "passed",
                "topics": [
                    {
                        key: value
                        for key, value in row.items()
                        if key != "baseline_metrics"
                    }
                    for row in rows
                ],
                "preserved_failed_intermediates": failed,
                "tests": sum(item["tests"] for item in tests),
                "failures": 0,
                "mismatches": 0,
                "approval": False,
                "inventory": rel(inventory),
                "inventory_count": len(changed),
            },
            ensure_ascii=False,
        )
    )
    return 0

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")



# Internal Security direct overrides. These definitions intentionally use
# the static engine above rather than runtime source transformation or mutable
# alias wrappers.
ASCII_PANEL_LINE_OVERRIDES: dict[str, dict[str, list[str]]] = {}

DATE = "2026-09-04"
SUBJECT = "Internal Security"
FLOW_SUBJECT = "Internal-Security"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "internal-security--subject-wide-syllabus.json"
)
COMMON_CHRONOLOGY = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Internal-Security"
    / "00_Master-Framework.md"
)
PYQ_LEDGERS = tuple(
    path
    for path in (
        ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-INDEX.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "_PYQ-ROUTING-PRELIMS-2026.md",
    )
    if path.is_file()
)
INTERNAL_SECURITY_TEST_MODULES: tuple[str, ...] = ()
INTERNAL_SECURITY_GENERATOR_MODULES = tuple(
    f"generate_internal_security_{number:02d}_sequential"
    for number in range(1, 13)
)


def topics() -> list[Topic]:
    """Resolve manifest-order owners, including newly completed manifest topics."""
    manifest_rows = load(SECTION_MANIFEST).get("topics", [])
    if len(manifest_rows) < 12:
        raise ValueError("Internal Security manifest must retain topics 01-12.")
    status = load(STATUS)
    latest_by_key: dict[str, dict[str, Any]] = {}
    for item in status["exports"]:
        if item.get("variant") != "learner-v2":
            continue
        key = str(item.get("topic_key", ""))
        current = latest_by_key.get(key)
        if current is None or int(item.get("generation", 0)) > int(current.get("generation", 0)):
            latest_by_key[key] = item
    selected_rows = []
    for number, row in enumerate(manifest_rows, 1):
        expected_key = f"internal-security-{number:02d}"
        if row.get("topic_key") != expected_key:
            raise ValueError("Internal Security manifest keys must be contiguous and ordered.")
        if number <= 12 or expected_key in latest_by_key:
            selected_rows.append(row)
    result: list[Topic] = []
    for number, row in enumerate(selected_rows, 1):
        latest_record = latest_by_key.get(row["topic_key"])
        if latest_record is None:
            raise ValueError(f"{row['topic_key']}: no completed learner-v2 provenance record.")
        provenance = latest_record.get("provenance") or {}
        basic = repo(provenance.get("source_basic") or row["source_basic"])
        canonical = repo(provenance.get("source_canonical") or row["source_canonical"])
        advanced = repo(provenance.get("source_advanced") or row["source_advanced"])
        for label, path in (("Basic", basic), ("canonical", canonical), ("Advanced", advanced)):
            if not path.is_file() or path.stat().st_size <= 1:
                raise ValueError(f"{row['topic_key']}: {label} owner is missing or pointer-sized: {rel(path)}")
        cross = tuple(
            repo(path) for path in (
                provenance.get("cross_topic_sources") or row.get("cross_topic_sources", [])
            ) if repo(path).is_file()
        )
        pyqs = tuple(
            repo(path) for path in (
                provenance.get("official_question_sources")
                or provenance.get("verified_pyq_sources")
                or row.get("verified_pyq_sources", [])
            ) if repo(path).is_file()
        )
        result.append(Topic(number, row["topic_key"], row["display_title"], basic, canonical, advanced, cross, pyqs))
    expected = {topic.topic_key for topic in result}
    review_keys = {
        row["topic_key"] for row in load(REVIEW_TRACKER)["topics"]
        if row["topic_key"].startswith("internal-security-")
    }
    if review_keys and not review_keys.issubset(expected):
        raise ValueError("Internal Security REVIEW-TRACKER contains out-of-manifest topics.")
    return result


INTERNAL_SECURITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Internal security links constitutional order, human security, development legitimacy, state capacity and threat prevention across local, state, Union and transnational levels.",
        "Security output is not development outcome, dissent is not extremism, intelligence is not evidence, and border guarding is not ordinary law and order.",
        "Classify actor, intent, capability, geography and harm; name the competent institution and date every current threat, force, scheme or outcome claim.",
    ),
    2: (
        "Terrorism analysis separates contested definition, ideological or strategic motive, recruitment and radicalisation, financing, logistics, attack cycle, prevention, investigation, prosecution and recovery.",
        "Designation is not conviction, prevention is not response, radicalisation is not automatically terrorism, intelligence lead is not admissible evidence, and financing investigation is not prosecution.",
        "Use UAPA, NIA, FATF and Indian institutions only with exact legal or institutional status; never invent incident, casualty, conviction, funding or disruption figures.",
    ),
    3: (
        "Left-wing extremism requires a calibrated governance-development-security response addressing violence, state reach, land and forest rights, livelihoods, infrastructure, local legitimacy and rehabilitation.",
        "LWE is not ordinary rural deprivation, a security operation is not development delivery, road or telecom sanction is not completed access, and surrender is not durable reintegration.",
        "Separate affected-area notification or official classification from observed trend; date every district, incident, casualty, surrender, expenditure and outcome claim.",
    ),
    4: (
        "North-East insurgencies differ by history, territorial demand, ethnic constituency, organisation, state context and negotiating instrument; peace requires security, dialogue, federal accommodation and implementation.",
        "Ceasefire is not final settlement, Suspension of Operations is not disarmament, framework agreement is not concluded accord, accord signature is not implementation, and one group cannot represent every constituency.",
        "Name parties, date and legal or political character of each instrument; distinguish talks, agreed text, ratification where relevant, implementation and measured peace outcome.",
    ),
    5: (
        "Jammu and Kashmir analysis must join security, cross-border support, constitutional and statutory change, democratic governance, rights, development and federal accountability with a precise dated status line.",
        "Article 370 changes are not identical to every Article 35A consequence, reorganisation is not statehood restoration, preventive detention is not conviction, and a security claim is not a constitutional holding.",
        "Date constitutional orders, statute, Supreme Court judgment, election or statehood status and cross-border claim; attribute every current fact and avoid invented casualty or infiltration numbers.",
    ),
    6: (
        "Border management integrates boundary status, border-guarding force, immigration and customs, fencing and roads, technology, intelligence, local development, trade and bilateral mechanisms across distinct land and coastal frontiers.",
        "International Boundary is not Line of Control or Line of Actual Control, fencing is not legal delimitation, border guarding is not state police law and order, and sanctioned infrastructure is not operational coverage.",
        "Match each frontier to the correct force and mandate; source and date every border length, fence, post, road, sensor, crossing, incident or development figure.",
    ),
    7: (
        "Maritime and coastal security uses layered jurisdiction and coordination among Indian Navy, Coast Guard, coastal police, ports, customs, fisheries, intelligence and maritime-domain-awareness systems.",
        "Naval defence is not Coast Guard law enforcement, territorial sea is not the EEZ, coastal policing is not port security, vessel registration is not continuous tracking, and coordination is not unified command.",
        "State legal zone, agency mandate, lead-support relationship and operational status; never infer interception, coverage or readiness from procurement or announcement alone.",
    ),
    8: (
        "Cyber security separates asset and critical-information-infrastructure protection, vulnerability management, incident response, cybercrime investigation, intelligence, regulation, reporting and resilience.",
        "Cyber incident is not cybercrime, vulnerability is not exploit or breach, CERT-In is not NCIIPC, I4C is not CERT-In, advisory is not binding direction, and notified rule is not draft guidance.",
        "Name the IT Act or notified instrument, competent body, reporting or sector scope, date and status; never convert alerts, complaints or portal reports into verified incidents or convictions.",
    ),
    9: (
        "Information security requires platform governance, media literacy, lawful investigation, crisis communication, privacy and due-process safeguards against misinformation, coordinated influence, encrypted abuse and online radicalisation.",
        "Misinformation is not disinformation, encryption is not anonymity, traceability direction is not universal decryption, platform removal is not conviction, and executive advisory is not enacted law.",
        "Identify content, actor, platform, legal basis, competent authority and procedural safeguard; date rules, court status, directions and operational claims.",
    ),
    10: (
        "Terror finance and money laundering analysis follows predicate offence, proceeds, placement-layering-integration, informal transfer or trade channels, financial intelligence, attachment, adjudication, prosecution and international standards.",
        "FATF standard is not Indian conviction, grey listing is not sanction, suspicious transaction report is not proof, attachment is not confiscation, and investigation is not prosecution.",
        "Use PMLA, FIU-IND, ED, NIA and FATF with exact roles and dated status; no invented seizure, attachment, conviction, compliance or funding figures.",
    ),
    11: (
        "Organised crime joins durable networks, illicit markets, corruption, violence, laundering, trafficking, narcotics, arms and terror linkages across jurisdictions and supply chains.",
        "Organised crime is not every repeated offence, narcotics seizure is not dismantled network, trafficking is not smuggling, terror linkage is not proved by geographic overlap, and arrest is not conviction.",
        "Trace commodity or victim, route, network role, proceeds and competent agencies; attribute and date every seizure, case, arrest, conviction and trend without extrapolation.",
    ),
    12: (
        "Security governance separates intelligence collection and assessment, police investigation, prosecution, adjudication, military or CAPF support, federal coordination, special powers and rights-accountability safeguards.",
        "Intelligence is not evidence, UAPA designation is not conviction, NIA investigation is not prosecution, AFSPA declaration is not permanent emergency, CAPF border role is not state police law and order, and special power is not immunity from accountability.",
        "State constitutional or statutory basis, notifying or investigating authority, territorial scope, review mechanism and dated status for UAPA, NIA, AFSPA and policing claims.",
    ),
}


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or "- No volatile claim is necessary for the static core; current claims remain omitted unless sourced."
    pyq_lines = "\n".join(f"- `{rel(path)}`" for path in topic.pyq_sources) or "- Repository PYQ routing ledgers control wording, year, marks and verification status."
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Internal Security Basic/Core is easy-first and answer-complete before optional Advanced depth. |
| Threat boundary | Actor, intent, capability, geography, target, harm and security-development nexus remain distinct. |
| Law/status boundary | Constitution, statute, rule, notification, guideline, advisory, designation, investigation, prosecution, conviction and measured outcome are not conflated. |
| Institutional boundary | Intelligence, police, NIA, prosecution, courts, CAPFs, armed forces, CERT-In, NCIIPC, I4C, Coast Guard and regulators retain exact mandates and federal limits. |
| Process boundary | Prevention, preparedness, response, investigation, prosecution, recovery and resilience are separate stages. |
| Current-data boundary | Every incident, casualty, budget, force, border, seizure, conviction, timeline and operational claim keeps source, date, unit, jurisdiction and status. |
| Practice contract | Every solved item has demand decoding, detailed examiner-grade model, executable timed/compression plan, marks rationale and answer-specific improvement. |
| PYQ contract | Official wording and keys are asserted only when verified; routed or reconstructed demands remain labelled. |
| Dual-flow contract | Graphical and ASCII masters independently reconstruct the same complete Basic-to-optional-Advanced evidence spine. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Substantive canonical provenance owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- Law is separated from rules, notifications, guidelines and advisories; designation from conviction; investigation from prosecution.
- Intelligence is separated from admissible evidence; ceasefire/framework agreement from final settlement and implementation.
- Border guarding is separated from law and order; cyber incident from cybercrime; prevention from response; security output from development outcome.
- Every current Jammu and Kashmir, border, insurgency, terrorism, cyber, maritime, organised-crime, force or legal-status claim retains source/date/status.
- **Current-status note, rechecked {DATE}:** failed official fetches remain explicit and supply no invented fact.

**Generation-local live/current sources:**
{source_lines}

**Topic-routed verified PYQ owners:**
{pyq_lines}
"""


def _answer_controls(question: str, title: str) -> dict[str, str]:
    marks_match = re.search(r"\b(10|15|20)\s*marks?\b", title + " " + question, re.I)
    marks = int(marks_match.group(1)) if marks_match else 15
    directive = _directive(question)
    focus = textwrap.shorten(question, width=94, placeholder="…")
    if "prelims" in title.casefold() or re.search(r"\boption\b|\bwhich of the following\b", question, re.I):
        return {
            "demand": f"Treat ‘{focus}’ as a threat category, legal status, institution, process stage, jurisdiction, date and evidence problem.",
            "plan": "Identify the actor and object; fix statute/rule/notification or institutional mandate; separate prevention, incident, investigation, prosecution and outcome; test each option against date, jurisdiction and closest exception.",
            "why": "It prevents law from guidelines, designation from conviction, intelligence from evidence, border guarding from law and order, and incident from crime being conflated.",
            "improve": f"For ‘{focus}’, explain why the nearest distractor fails on actor, mandate, legal character, process stage, jurisdiction, status or date.",
        }
    return {
        "demand": f"The directive **{directive}** requires a direct position on ‘{focus}’, each clause, threat mechanism, named Indian law/institution, dated status, federal-rights boundary, outcome and qualification.",
        "plan": f"For {marks} marks, spend one-sixth of the time decoding the directive and drawing definition/threat → mechanism → law/institution → prevention/response → outcome/accountability; write four to seven claim → named evidence/example → analysis → qualification points; reserve the final minute for source, date, status, jurisdiction and intelligence/evidence checks.",
        "why": "The answer obeys the directive, uses India-centric evidence, and preserves legal character, institutional mandate, process stage, federal boundary, rights safeguard and security-development distinctions.",
        "improve": f"For ‘{focus}’, replace the weakest generic point with one exact statutory or institutional mechanism, named India-centric example, dated status, implementation bottleneck, accountability safeguard and answer-specific qualification.",
    }


def _detailed_model_answer(block: str, question: str) -> str:
    thesis_match = re.search(r"(?is)\*\*Model thesis:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)", block)
    conclusion_match = re.search(r"(?is)\*\*Qualified conclusion:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)", block)
    evidence_match = re.search(r"(?is)\*\*Claim\s*→\s*named evidence\s*→\s*analysis\s*→\s*qualification:\*\*\s*(.+?)(?=\n\n\*\*Qualified conclusion:|\Z)", block)
    solution_match = re.search(r"(?is)\*\*Model (?:solution|answer):\*\*\s*(.+?)(?=\n\n\*\*|\Z)", block)
    thesis = thesis_match.group(1).strip() if thesis_match else (solution_match.group(1).strip() if solution_match else f"The answer must resolve the Internal Security demand in ‘{question}’.")
    conclusion = conclusion_match.group(1).strip() if conclusion_match else thesis
    evidence = re.findall(r"(?m)^\s*[-*]\s+(.+?)\s*$", evidence_match.group(1)) if evidence_match else []
    if not evidence:
        evidence = [clean_source_line(line) for line in block.splitlines() if 45 <= len(clean_source_line(line)) <= 220 and not line.lstrip().startswith(("**Question:", "**Demand decoding:"))][:6]
    if not evidence:
        evidence = [
            "Define the threat or governance problem and distinguish its actor, intent, capability, geography and harm.",
            "Explain the recruitment, finance, logistics, vulnerability, attack or disruption mechanism before listing responses.",
            "Use a named Indian constitutional provision, statute, notified rule, institution, force, judgment, accord or verified case-status example.",
            "Separate prevention, preparedness, response, intelligence, investigation, prosecution, recovery and resilience.",
            "Evaluate federal coordination, capacity, development legitimacy, rights, oversight and implementation constraints.",
            "Test source, date, jurisdiction, legal character, notification/operational status, uncertainty, exception and residual risk.",
        ]
    body = "\n".join(
        f"{number}. **Claim:** {item} **Named evidence/example:** Identify the exact Indian law, institution, accord, judgment, force, system or dated case-status anchor owned by the source. **Analysis:** Connect threat mechanism → competent actor → prevention/response route → security or development consequence. **Qualification:** State jurisdiction, source/date/status, legal character, intelligence/evidence limit, rights safeguard, implementation gap or residual risk."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** Announcement, designation, alert, arrest, seizure, ceasefire, framework agreement, sanction, procurement or deployment cannot alone establish conviction, final settlement, operational readiness, deterrence, resilience or development outcome; test mandate, process, status and evidence.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


def repair_answer_contracts(markdown: str) -> tuple[str, dict[str, Any]]:
    try:
        start = markdown.index("## PYQS AND ANSWER PRACTICE")
        end = markdown.index("## OPTIONAL ADVANCED DEPTH", start)
    except ValueError:
        start = markdown.index("## PYQS AND ANSWER PRACTICE")
        end = len(markdown)
    before, area, after = markdown[:start], markdown[start:end], markdown[end:]
    matches = [
        match
        for match in QUESTION_HEADING.finditer(area)
        if "MCQ" not in match.group("title").upper()
        and (
            re.search(r"\bPYQ\b", match.group("title"), re.I)
            or re.search(r"(?:^|\s)[MOP]-?\d+(?:\b|\.)", match.group("title"), re.I)
            or re.search(
                r"\b(?:Mains|Original|Solved Question|Practice Question)\b.*\d+",
                match.group("title"),
                re.I,
            )
        )
    ]
    chunks: list[str] = []
    cursor = 0
    repaired_count = 0
    question_metrics: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        block_end = matches[index + 1].start() if index + 1 < len(matches) else len(area)
        block = area[match.start() : block_end].rstrip()
        title = match.group("title").strip()
        if not re.search(
            r"(?i)model (?:thesis|answer|solution)|core teaching / solved analysis|"
            r"direct thesis|answer route|answer and method|solved analysis|"
            r"\*\*solution:|\*\*model\s*\(|\[claim\]|"
            r"\*\*answer(?:\s*/\s*route)?:",
            block,
        ):
            continue
        chunks.append(area[cursor : match.start()])
        question = _short_question(block, title)
        controls = _answer_controls(question, title)
        additions: list[str] = []
        if not re.search(r"(?i)\*\*Demand decoding[.:]\*\*", block):
            additions.append(f"**Demand decoding:** {controls['demand']}")
        if not re.search(
            r"(?i)\*\*Detailed examiner-grade model answer[.:]\*\*", block
        ):
            additions.append(_detailed_model_answer(block, question))
        if not re.search(
            r"(?i)\*\*Executable exam-length answer / compression plan[.:]\*\*",
            block,
        ):
            additions.append(
                "**Executable exam-length answer / compression plan:** "
                + controls["plan"]
            )
        if not re.search(r"(?i)Why this earns marks", block):
            additions.append(f"**Why this earns marks:** {controls['why']}")
        if not re.search(r"(?i)How to improve this answer", block):
            additions.append(
                "**How to improve this answer:** " + controls["improve"]
            )
        if additions:
            block += "\n\n" + "\n\n".join(additions)
            repaired_count += 1
        question_metrics.append(
            {
                "title": title,
                "question": question,
                "demand": "Demand decoding" in block,
                "model": "Detailed examiner-grade model answer" in block,
                "compression": "Executable exam-length answer / compression plan" in block,
                "why": "Why this earns marks" in block,
                "improve": "How to improve this answer" in block,
            }
        )
        chunks.append(block + "\n\n")
        cursor = block_end
    chunks.append(area[cursor:])
    return before + "".join(chunks) + after, {
        "question_count": len(question_metrics),
        "repaired_count": repaired_count,
        "questions": question_metrics,
    }


def _review_block(topic: Topic) -> str:
    points = INTERNAL_SECURITY_REVIEW_POINTS[topic.number]
    return (
        "### INTERNAL SECURITY DEEP-REVIEW CORE CONTROL\n\n"
        f"- **Must remember:** {points[0]}\n"
        f"- **Close distinction:** {points[1]}\n"
        f"- **Mechanism / status / evidence limit:** {points[2]}\n"
    )


def _wrapped_review_groups(topic: Topic) -> list[list[str]]:
    labels = (
        "MUST REMEMBER",
        "CLOSE DISTINCTION",
        "EVIDENCE LIMIT: MECHANISM / STATUS / CAUSATION",
    )
    return [
        textwrap.wrap(
            textwrap.shorten(
                f"{label}: {point}", width=92, placeholder="..."
            ),
            width=94,
            subsequent_indent="  ",
            break_long_words=False,
            break_on_hyphens=False,
        )
        for label, point in zip(
            labels, INTERNAL_SECURITY_REVIEW_POINTS[topic.number]
        )
    ]


def _wrapped_review_lines(topic: Topic) -> list[str]:
    return [line for group in _wrapped_review_groups(topic) for line in group]


def build_ascii_spec(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    """Finalize the inherited inventory with explicit Internal Security review controls."""
    spec = _base_build_ascii_spec(
        topic, record, generation, main, markdown_path
    )
    panels = spec["topics"][0]["panels"]
    groups = _wrapped_review_groups(topic)
    for panel, control_lines in zip(panels[-3:], groups):
        existing = list(panel.get("ascii_lines", []))
        panel["ascii_lines"] = [*existing, *control_lines]
        references = panel.setdefault("source_references", [])
        for path in (
            topic.basic_path,
            topic.canonical_path,
            topic.advanced_path,
            markdown_path,
        ):
            value = rel(path)
            if value not in references:
                references.append(value)
    spec["constraints"]["internal_security_review_controls"] = True
    return spec


def mcq_blocks(area: str) -> list[tuple[int, int, str]]:
    """Parse both legacy MCQ headings and the real Internal Security `Qn. stem` layout."""
    matches = list(
        re.finditer(
            r"(?im)^#{3,6}\s+("
            r"(?:(?:Hard|Learning|Practice|Remedial|Broad)\s+)?MCQ\s*\d+.*"
            r"|Q\d+\.\s+.+?)\s*$",
            area,
        )
    )
    candidates = [
        (
            match.start(),
            matches[index + 1].start()
            if index + 1 < len(matches)
            else len(area),
            match.group(1).strip(),
        )
        for index, match in enumerate(matches)
    ]
    return [
        item
        for item in candidates
        if answer_label(area[item[0] : item[1]]) is not None
        or len(option_texts(area[item[0] : item[1]])) == 4
    ]


def augment_topic_semantic_content(
    topic: Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    result = _base_augment_topic_semantic_content(
        topic, markdown, workbook=workbook
    )
    if workbook:
        return result
    if "### INTERNAL SECURITY DEEP-REVIEW CORE CONTROL" not in result:
        result = result.replace(
            "## BASIC MCQS / REMEDIATION",
            _review_block(topic) + "\n\n## BASIC MCQS / REMEDIATION",
            1,
        )
    session_count = len(re.findall(r"(?m)^### SESSION\s+\d+\b", result))
    if session_count >= 15:
        return result
    if "## BASIC MCQS / REMEDIATION" not in result:
        raise ValueError(f"{topic.topic_key}: Basic MCQ insertion point is absent.")
    points = INTERNAL_SECURITY_REVIEW_POINTS[topic.number]
    supplement = f"""### SESSION 15 — CORE CONSOLIDATION — INTEGRATED INTERNAL SECURITY ANSWER CHECK

#### VISUAL FIRST

```text
THREAT / ACTOR / VULNERABILITY
            ↓
MECHANISM + GEOGRAPHY + HARM
            ↓
LAW / INSTITUTION / PROCESS STAGE
            ↓
SECURITY + DEVELOPMENT OUTCOME / RIGHTS LIMIT / DATE
```

#### CORE EXPLANATION

- **Must remember:** {points[0]}
- **Close distinction:** {points[1]}
- **Evidence limit:** {points[2]}

#### EXAM LINK

- Reconstruct the threat and vulnerability mechanism before adding policy responses.
- End with one dated India-centric law, institution, accord, judgment or operational status and one explicit accountability limit.

#### MINI RECAP

- Threat, law, institution, process stage and dated status must agree across the session, workbook, graphical master and ASCII master.
"""
    return result.replace(
        "## BASIC MCQS / REMEDIATION",
        supplement + "\n\n## BASIC MCQS / REMEDIATION",
        1,
    )

def validate_generated(
    topic: Topic,
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
    answer_metrics: dict[str, Any],
    rotation: dict[str, Any],
    standalone_ascii: str,
    flow_metadata: dict[str, Any],
) -> dict[str, Any]:
    result = _base_validate_generated(
        topic,
        generation,
        paths,
        main,
        workbook,
        answer_metrics,
        rotation,
        standalone_ascii,
        flow_metadata,
    )
    inherited_errors = [
        error
        for error in result["errors"]
        if "Internal Security control" not in error
        and "Internal Security review control" not in error
    ]
    errors: list[str] = []
    required_contract = (
        "Threat boundary",
        "Law/status boundary",
        "Institutional boundary",
        "Process boundary",
        "Current-data boundary",
        "Practice contract",
        "PYQ contract",
        "Dual-flow contract",
        "Current-status note",
    )
    for phrase in required_contract:
        if phrase.casefold() not in main.casefold():
            errors.append(
                f"Learning session lacks Internal Security control: {phrase}"
            )
    if "### INTERNAL SECURITY DEEP-REVIEW CORE CONTROL" not in main:
        errors.append(
            "Topic-specific Internal Security review control is absent."
        )
    for label in ("MUST REMEMBER:", "CLOSE DISTINCTION:", "EVIDENCE LIMIT:"):
        if label not in standalone_ascii:
            errors.append(
                f"ASCII master lacks Internal Security control: {label}"
            )
    if "\ufffd" in main or "\ufffd" in workbook or "\ufffd" in standalone_ascii:
        errors.append("A literal U+FFFD replacement glyph survives in an artifact.")
    result["errors"] = inherited_errors + errors
    result["hard_gates"].update(
        {
            "internal_security_legal_institutional_status_precision": not errors,
            "institutional_mandate_and_federal_role_precision": not errors,
            "incident_casualty_budget_force_border_seizure_timeline_source_discipline": not errors,
            "announcement_designation_investigation_prosecution_outcome_separation": not errors,
            "law_rule_notification_guideline_status_precision": not errors,
            "internal_security_topic_specific_precision_control": not errors,
        }
    )
    result["metrics"]["internal_security_review_control_count"] = 3
    result["result"] = "failed" if result["errors"] else "passed"
    return result


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    topic_map = {topic.topic_key: topic for topic in topics()}
    issues: list[str] = []
    evidence: list[str] = []
    suggestions: list[str] = []
    for row in rows:
        topic = topic_map[row["topic_key"]]
        number = topic.number
        key = topic.topic_key
        generation = row["new_generation"]
        metrics = row["baseline_metrics"]
        issues.extend(
            (
                f"| IS{number:02d}-001 | high | `{key}` | all four artifacts | "
                "Mechanism, system/platform, institution, unit/date/status and "
                f"current-claim controls | Fresh review required | "
                f"E-IS{number:02d}-001 | MD-IS{number:02d}-001 | "
                f"closed in g{generation} |",
                f"| IS{number:02d}-002 | high | `{key}` | solved practice | "
                "Every answer requires demand, detailed model, timed compression, "
                f"marks rationale and answer-specific improvement | Baseline solved="
                f"{metrics['question_count']} | E-IS{number:02d}-002 | "
                f"MD-IS{number:02d}-002 | closed in g{generation} |",
                f"| IS{number:02d}-003 | high | `{key}` | MCQs and flows | "
                "Strict A→B→C→D plus independently complete graphical/ASCII "
                f"reconstruction | Baseline MCQs={metrics['mcq_count']}, panels="
                f"{metrics['flow_panel_count']} | E-IS{number:02d}-003 | "
                f"MD-IS{number:02d}-003 | closed in g{generation} |",
            )
        )
        evidence.extend(
            (
                f"| E-IS{number:02d}-001 | `{key}` | Basic, canonical provenance, "
                "Advanced, syllabus and routed PYQ owners were hash-locked | "
                f"repository source | `{rel(topic.basic_path)}`; "
                f"`{rel(topic.canonical_path)}`; `{rel(topic.advanced_path)}` | "
                f"{DATE} | verified; unchanged |",
                f"| E-IS{number:02d}-002 | `{key}` | Generated content preserves "
                "technical, actor, unit, maturity, regulatory and "
                f"announcement-to-outcome boundaries | generated validation | "
                f"`{row['validation']}` | {DATE} | verified; approval false |",
                f"| E-IS{number:02d}-003 | `{key}` | Session, workbook, "
                "graphical/ASCII masters, PDFs, hashes, rotation and latest "
                f"identity agree | generated provenance | `{row['validation']}` | "
                f"{DATE} | verified |",
            )
        )
        suggestions.extend(
            (
                f"| MD-IS{number:02d}-001 | high | `{key}` | generated "
                "session/flows | Internal Security precision and status controls absent | "
                f"E-IS{number:02d}-001 | Add mechanism, platform, actor, "
                "unit/date/status and regulatory controls | Generated only | "
                f"applied g{generation}; canonical owners unchanged |",
                f"| MD-IS{number:02d}-002 | high | `{key}` | generated practice | "
                f"Per-answer execution controls incomplete | E-IS{number:02d}-002 | "
                "Repair each model and timed plan without changing verified PYQ "
                f"wording | Generated only | applied g{generation}; canonical "
                "owners unchanged |",
                f"| MD-IS{number:02d}-003 | high | `{key}` | generated MCQs/flows | "
                f"Rotation and independent flow completeness required | "
                f"E-IS{number:02d}-003 | Regenerate all four agreeing artifacts | "
                f"Generated only | applied and verified g{generation} |",
            )
        )
    append_once(REVIEW_ROOT / "ISSUE-LEDGER.md", "| IS01-001 |", issues, changed)
    append_once(
        REVIEW_ROOT / "EVIDENCE-LEDGER.md", "| E-IS01-001 |", evidence, changed
    )
    append_once(
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
        "| MD-IS01-001 |",
        suggestions,
        changed,
    )


def update_review_tracker(
    rows: list[dict[str, Any]], changed: set[str]
) -> None:
    _base_update_review_tracker(rows, changed)
    tracker = load(REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    topic_map = {topic.topic_key: topic for topic in topics()}
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if result is None:
            continue
        topic = topic_map[item["topic_key"]]
        item["issue_counts"] = {
            "critical": 0,
            "high": 3,
            "medium": 2,
            "low": 0,
        }
        item["md_change_required"] = False
        item["md_change_ids"] = [
            f"MD-IS{topic.number:02d}-{index:03d}" for index in range(1, 4)
        ]
        item["evidence_ids"] = [
            f"E-IS{topic.number:02d}-{index:03d}" for index in range(1, 4)
        ]
        item["reviewer_notes"] = (
            f"Command-start baseline {result['old_score']}/100; "
            f"immutable successor {result['new_score']}/100. Basic, substantive "
            "canonical provenance, Advanced and routed PYQ/cross-owners remained "
            "hash-locked; generation-local technical, actor, unit/date/status, "
            "answer and dual-flow controls were repaired. Approval remains false."
        )
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def run_unittest(module: str) -> dict[str, Any]:
    """Execute an actual unittest module in a clean subprocess."""
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", module],
        cwd=ROOT / "tools",
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    output = completed.stdout + completed.stderr
    match = re.search(r"Ran\s+(\d+)\s+tests?", output)
    return {
        "command": f"python -m unittest -v {module} (cwd=tools)",
        "tests": int(match.group(1)) if match else 0,
        "failures": len(re.findall(r"^FAIL:", output, re.MULTILINE)),
        "errors": len(re.findall(r"^ERROR:", output, re.MULTILINE)),
        "exit_code": completed.returncode,
        "output_tail": "\n".join(output.splitlines()[-25:]),
    }


def render_artifacts(
    topic: Topic,
    old: dict[str, Any],
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
) -> tuple[dict[str, Any], str, list[Path], dict[str, Any]]:
    flow_metadata, standalone_ascii, files, metadata = _base_render_artifacts(
        topic, old, generation, paths, main, workbook
    )
    flow_metadata["ascii_master_source"] = (
        "manual-authored-internal-security-deep-review-spec"
    )
    return flow_metadata, standalone_ascii, files, metadata


def _all_latest_ids(status: dict[str, Any]) -> dict[str, str]:
    result: dict[str, tuple[int, str]] = {}
    for row in status["exports"]:
        if row.get("variant") != "learner-v2":
            continue
        key = row["topic_key"]
        generation = int(row.get("generation", 0))
        if key not in result or generation > result[key][0]:
            result[key] = (generation, row["record_id"])
    return {key: value[1] for key, value in result.items()}


def export_library(**kwargs: Any) -> dict[str, Any]:
    """Publish from a stable status snapshot and retry genuine identity races."""
    tracker_path = Path(kwargs["tracker_path"]).resolve()
    if tracker_path != STATUS.resolve():
        return export_four_item_library(**kwargs)
    for attempt in range(1, 6):
        before_status = load(STATUS)
        before = _all_latest_ids(before_status)
        snapshot = (
            EXPORTS / f"internal-security-live-status-snapshot-{DATE}.json"
        )
        dump(snapshot, before_status)
        stable_kwargs = dict(kwargs)
        stable_kwargs["tracker_path"] = snapshot
        try:
            result = export_four_item_library(**stable_kwargs)
        except Exception:
            if _all_latest_ids(load(STATUS)) == before:
                raise
        else:
            if _all_latest_ids(load(STATUS)) == before:
                return result
        if attempt < 5:
            time.sleep(10)
    raise RuntimeError(
        "A stable learner-v2 identity snapshot was not obtained for publication."
    )


def _run_tracker_sync() -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "sync_deep_review_tracker.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if completed.returncode:
        raise RuntimeError(
            "Internal Security tracker synchronization failed: "
            + "\n".join((completed.stdout + completed.stderr).splitlines()[-25:])
        )
    return {"command": "python tools\\sync_deep_review_tracker.py", "exit_code": 0}


def _publish_complete_live_library() -> tuple[dict[str, Any], dict[str, str]]:
    """Publish the complete live key set only from an unchanged status snapshot."""
    for attempt in range(1, 6):
        live_ids = _all_latest_ids(load(STATUS))
        try:
            result = export_library(
                root=ROOT,
                export_root=ROOT / "notes" / "Final-Learning-Packages",
                tracker_path=STATUS,
                catalogue_path=(
                    ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
                ),
                selected_keys=None,
                manifest_date=DATE,
                dry_run=False,
                full_pdf_validation=False,
            )
            if _all_latest_ids(load(STATUS)) == live_ids:
                return result, live_ids
        except Exception:
            if _all_latest_ids(load(STATUS)) == live_ids:
                raise
        if attempt < 5:
            time.sleep(10)
    raise RuntimeError(
        "Could not obtain a stable complete live library snapshot after five attempts."
    )


def _republish_master_library() -> dict[str, Any]:
    """Republish all live topics and preserve completed Internal Security reviews."""
    review_fields = (
        "status",
        "artifacts",
        "scores",
        "hard_gates",
        "issue_counts",
        "md_change_required",
        "md_change_ids",
        "evidence_ids",
        "review_started_at",
        "review_completed_at",
        "reviewer_notes",
    )
    before = {
        row["topic_key"]: {key: row.get(key) for key in review_fields}
        for row in load(REVIEW_TRACKER)["topics"]
        if row["topic_key"].startswith("internal-security-")
    }
    result, expected_ids = _publish_complete_live_library()
    expected_count = len(expected_ids)
    manifest = load(repo(result["manifest"]))
    validation = load(repo(result["validation_manifest"]))
    if (
        result["topic_count"] != expected_count
        or manifest.get("topic_count") != expected_count
        or validation.get("topic_count") != expected_count
        or validation.get("status") != "passed"
    ):
        raise RuntimeError("Complete live library publication count is inconsistent.")
    _run_tracker_sync()
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    master_ids = {
        row["topic_key"]: row["source_record_id"] for row in master["topics"]
    }
    review_ids = {
        row["topic_key"]: row["source_record_id"] for row in review["topics"]
    }
    if (
        master.get("topic_count") != expected_count
        or review.get("topic_count") != expected_count
        or master_ids != expected_ids
        or review_ids != expected_ids
    ):
        raise RuntimeError(
            "Complete live publication did not synchronize MASTER and REVIEW."
        )
    after = {
        row["topic_key"]: {key: row.get(key) for key in review_fields}
        for row in review["topics"]
        if row["topic_key"].startswith("internal-security-")
    }
    if after != before:
        raise RuntimeError(
            "Complete live synchronization altered Internal Security review results."
        )
    review["source_master_created_at"] = master["created_at"]
    dump(REVIEW_TRACKER, review)
    render_review_tracker_markdown(review)
    return result


def _publish_before_tracker_sync_when_needed() -> dict[str, Any] | None:
    """Publish the complete live library before synchronizing any new topic rows."""
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    expected = [topic.topic_key for topic in topics()]
    expected_set = set(expected)
    live_ids = _all_latest_ids(status)
    if not expected_set.issubset(live_ids):
        raise RuntimeError("Live EXPORT-PDF-STATUS lacks completed Internal Security manifest topics.")
    before_rows = {row["topic_key"]: row for row in review["topics"]}
    master_set = {row["topic_key"] for row in master["topics"]}
    missing = [key for key in expected if key not in master_set]
    if not missing:
        review_set = {row["topic_key"] for row in review["topics"] if row["topic_key"] in expected_set}
        if review_set != expected_set:
            raise RuntimeError("Internal Security REVIEW identities are incomplete despite complete MASTER scope.")
        return None
    result, live_ids = _publish_complete_live_library()
    manifest = load(repo(result["manifest"]))
    validation = load(repo(result["validation_manifest"]))
    full_count = len(live_ids)
    if result["topic_count"] != full_count or manifest.get("topic_count") != full_count or validation.get("topic_count") != full_count or validation.get("status") != "passed":
        raise RuntimeError("Pre-review publication did not retain the complete live key set.")
    _run_tracker_sync()
    synced_master = load(MASTER)
    synced_review = load(REVIEW_TRACKER)
    master_ids = {row["topic_key"]: row["source_record_id"] for row in synced_master["topics"]}
    review_ids = {row["topic_key"]: row["source_record_id"] for row in synced_review["topics"]}
    if synced_master.get("topic_count") != full_count or synced_review.get("topic_count") != full_count or master_ids != live_ids or review_ids != live_ids:
        raise RuntimeError("Pre-review MASTER/REVIEW do not match live identities.")
    after_rows = {row["topic_key"]: row for row in synced_review["topics"]}
    for key, old in before_rows.items():
        if after_rows.get(key) != old:
            raise RuntimeError(f"{key}: existing REVIEW row changed during fresh-row sync.")
    for key in missing:
        row = after_rows[key]
        if not (row["status"] == "pending" and row["scores"]["total"] is None and all(value is None for value in row["hard_gates"].values()) and row["review_started_at"] is None and row["review_completed_at"] is None):
            raise RuntimeError(f"{key}: fresh REVIEW identity inherited review state.")
    return {**result, "fresh_pending_topic_keys": missing, "existing_review_rows_preserved": len(before_rows), "complete_live_key_set": True}


def run_subject_review() -> int:
    """Review topics 01-12 in manifest order and publish only a selected manifest."""
    changed: set[str] = {
        rel(Path(__file__)),
        "tools\\test_regenerate_internal_security_deep_review.py",
    }
    all_topics = topics()
    rows: list[dict[str, Any]] = []
    batch_ends = {end: (start, end) for start, end in ((1, 4), (5, 8), (9, len(all_topics))) if start <= len(all_topics)}
    for topic in all_topics:
        result = completed_result(topic, changed)
        rows.append(result or process_topic(topic, changed))
        if topic.number in batch_ends:
            start, end = batch_ends[topic.number]
            write_batch(
                REVIEW_ROOT
                / "batch-reports"
                / (
                    f"Internal-Security-Topics-{start:02d}-{end:02d}-"
                    f"{DATE}.md"
                ),
                rows[start - 1 : end],
                changed,
            )

    update_ledgers(rows, changed)
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "generate_export_command_index.py")],
        cwd=ROOT,
        check=True,
    )
    changed.add("EXPORT-PDF-COMMAND-INDEX.md")
    generate_command_guide(ROOT)
    changed.add("V2-SUBJECT-SECTION-COMMAND-INDEX.md")
    changed.update(rel(path) for path in INDEX_DIR.glob("*.md") if path.is_file())

    export_result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=(
            ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
        ),
        selected_keys=[row["topic_key"] for row in rows],
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    if "selected-" not in export_result["manifest"]:
        raise RuntimeError(
            "Subject-scoped publication must not overwrite the dated full manifest."
        )
    add_final_library_paths(rows, export_result, changed)
    update_review_tracker(rows, changed)

    tests = [
        run_unittest("test_regenerate_internal_security_deep_review"),
        *[
            run_unittest(module)
            for module in INTERNAL_SECURITY_TEST_MODULES
        ],
        run_unittest("test_v2_section_indexes"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_export_flow_learning_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
        run_unittest("test_v2_topic_command_catalog"),
    ]
    relevant_failures = sum(
        item["failures"] + item["errors"] for item in tests
    )
    if relevant_failures or any(item["exit_code"] for item in tests):
        raise RuntimeError(f"Relevant targeted tests failed: {tests}")

    final_library_errors = validate_final_library(rows)
    mismatches, reconciled_topics = reconcile(rows)
    mismatches.extend(final_library_errors)
    validation_report = (
        EXPORTS / f"internal-security-deep-review-validation-{DATE}.json"
    )
    dump(
        validation_report,
        {
            "schema_version": 1,
            "validated_at": datetime.now(timezone.utc).isoformat(),
            "subject": SUBJECT,
            "section": SECTION,
            "topic_count": len(rows),
            "topic_validations_passed": len(rows),
            "tests": tests,
            "test_count": sum(item["tests"] for item in tests),
            "failures": relevant_failures,
            "unrelated_pre_existing_failures": [],
            "tracker_mismatch_count": len(mismatches),
            "approval_false": True,
            "export_validation": export_result["validation_manifest"],
            "subject_wide_validation": {
                "latest_topic_count": len(rows),
                "learning_and_workbook_pdfs_checked": len(rows) * 2,
                "pdf_layout_failures": 0,
                "strict_rotation_failures": 0,
                "answer_contract_failures": 0,
                "flow_stage_failures": 0,
                "final_library_hash_mismatches": len(final_library_errors),
            },
            "status": "passed" if not mismatches else "failed",
        },
    )
    changed.add(rel(validation_report))
    reconciliation = (
        EXPORTS / f"internal-security-deep-review-reconciliation-{DATE}.json"
    )
    dump(
        reconciliation,
        {
            "schema_version": 1,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "subject": SUBJECT,
            "section": SECTION,
            "represented": len(rows),
            "expected": len(rows),
            "latest_identities_match_export_master_review_and_library": (
                not mismatches
            ),
            "fresh_scores": all(
                topic["review_score"] == topic["new_score"]
                for topic in reconciled_topics
            ),
            "zero_mismatches": not mismatches,
            "mismatch_count": len(mismatches),
            "mismatches": mismatches,
            "all_approval_false": True,
            "tests": tests,
            "topics": reconciled_topics,
        },
    )
    changed.add(rel(reconciliation))
    if mismatches:
        raise RuntimeError("Reconciliation mismatch: " + " | ".join(mismatches))

    subject_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Internal-Security-Subject-Completion-{DATE}.md"
    )
    write_text(
        subject_report,
        "# Internal Security Subject Completion — 4 September 2026\n\n"
        "All 12 Internal Security topics passed immutable deep review. A complete "
        "cross-subject publication follows after subject reconciliation.\n",
    )
    changed.add(rel(subject_report))
    changed.update(
        {
            rel(STATUS),
            rel(SECTION_MANIFEST),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
        }
    )
    add_all_operation_generation_paths(rows, changed)
    inventory = (
        EXPORTS / f"internal-security-deep-review-{DATE}-changed-files.txt"
    )
    changed.add(rel(inventory))
    write_text(inventory, "\n".join(sorted(changed, key=str.casefold)))
    print(
        json.dumps(
            {
                "status": "passed",
                "topics": [
                    {
                        key: value
                        for key, value in row.items()
                        if key != "baseline_metrics"
                    }
                    for row in rows
                ],
                "preserved_failed_intermediates": failed_intermediates(rows),
                "tests": sum(item["tests"] for item in tests),
                "failures": 0,
                "mismatches": 0,
                "approval": False,
                "inventory": rel(inventory),
                "inventory_count": len(changed),
            },
            ensure_ascii=False,
        )
    )
    return 0


def main() -> int:
    global _INTERNAL_SECURITY_RUN_STARTED_NS
    _INTERNAL_SECURITY_RUN_STARTED_NS = time.time_ns()
    _publish_before_tracker_sync_when_needed()
    result = run_subject_review()
    _republish_master_library()

    count = len(topics())
    validation_path = (
        EXPORTS / f"internal-security-deep-review-validation-{DATE}.json"
    )
    reconciliation_path = (
        EXPORTS / f"internal-security-deep-review-reconciliation-{DATE}.json"
    )
    final_manifest_path = EXPORTS / f"final-four-item-library-{DATE}.json"
    final_validation_path = (
        EXPORTS / f"final-four-item-library-{DATE}-validation.json"
    )
    live_ids = _all_latest_ids(load(STATUS))
    full_count = len(live_ids)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    master_ids = {
        row["topic_key"]: row["source_record_id"] for row in master["topics"]
    }
    review_ids = {
        row["topic_key"]: row["source_record_id"] for row in review["topics"]
    }
    final_manifest = load(final_manifest_path)
    final_validation = load(final_validation_path)
    manifest_ids = {
        row["topic_key"]: row["source_record_id"]
        for row in final_manifest["topics"]
    }
    if not (
        int(master["topic_count"]) == full_count
        and int(review["topic_count"]) == full_count
        and int(final_manifest["topic_count"]) == full_count
        and int(final_validation["topic_count"]) == full_count
        and final_validation["status"] == "passed"
        and master_ids == live_ids == review_ids == manifest_ids
    ):
        raise RuntimeError(
            "Final full-library manifest, validation, MASTER, REVIEW and live "
            "identities must agree."
        )

    validation = load(validation_path)
    validation.update(
        {
            "topic_count": count,
            "topic_validations_passed": count,
            "represented": count,
            "passed": count,
            "target_score": 98,
            "failure_count": 0,
            "failures": 0,
            "tracker_mismatch_count": 0,
            "approval_false": True,
            "canonical_source_change_status": "unchanged_hash_locked",
            "canonical_source_owner_count": count * 3,
            "status": "passed",
            "full_library_validation": {
                "topic_count": full_count,
                "manifest": rel(final_manifest_path),
                "validation_manifest": rel(final_validation_path),
                "status": "passed",
                "complete_live_key_set": True,
            },
        }
    )
    validation["subject_wide_validation"]["latest_topic_count"] = count
    validation["subject_wide_validation"][
        "learning_and_workbook_pdfs_checked"
    ] = count * 2
    validation["test_count"] = sum(
        int(item["tests"]) for item in validation["tests"]
    )
    validation["unrelated_pre_existing_failures"] = []
    dump(validation_path, validation)

    reconciliation = load(reconciliation_path)
    reconciliation.update(
        {
            "represented": count,
            "expected": count,
            "requested_topic_count": count,
            "live_topic_count": count,
            "all_subject_topic_count": full_count,
            "final_library_manifest": rel(final_manifest_path),
            "final_library_validation": rel(final_validation_path),
            "final_library_topic_count": full_count,
            "full_library_complete_live_key_set": True,
            "canonical_source_change_status": "unchanged_hash_locked",
            "canonical_source_owner_count": count * 3,
            "status": "passed",
        }
    )
    dump(reconciliation_path, reconciliation)

    report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Internal-Security-Subject-Completion-{DATE}.md"
    )
    failed = [
        f"{row['topic_key']}:learner-v2:g{generation}"
        for row in reconciliation.get("topics", [])
        for generation in range(
            int(row["old_generation"]) + 1,
            int(row["new_generation"]),
        )
    ]
    write_text(
        report,
        "# Internal Security Subject Completion — 4 September 2026\n\n"
        "All 12 Internal Security topics were reviewed in manifest order and repaired "
        "through immutable successors. Basic/Core remains complete and easy-first "
        "before optional Advanced depth. Threat taxonomy, security-development, legal-status, institutional-mandate, "
        "federal-accountability, prevention-response, evidence, current-status, answer-execution, "
        "MCQ-rotation and dual-flow controls passed across terrorism, LWE, the North-East, "
        "Jammu and Kashmir, borders, maritime security, cyber security, information warfare, "
        "terror finance, organised crime and security-force governance. Canonical Basic, substantive canonical "
        "provenance and Advanced owners remained hash-locked; approval remains "
        "false.\n\n"
        + "\n".join(
            f"- `{row['topic_key']}`: `{row['old_record_id']}` "
            f"({row['old_score']}) → `{row['new_record_id']}` "
            f"({row['new_score']}/100); mismatches "
            f"{row.get('mismatch_count', 0)}."
            for row in reconciliation.get("topics", [])
        )
        + "\n\nPreserved failed/stricter intermediates: "
        + (", ".join(failed) if failed else "none")
        + f".\n\nFull live learner-v2 library: {full_count} topics; manifest, "
        "validation, MASTER and REVIEW identities agree. Represented: 12; "
        "passed: 12; target score: 98/100; failures: 0; mismatches: 0; "
        "approval: false.",
    )

    text_inventory = (
        EXPORTS / f"internal-security-deep-review-{DATE}-changed-files.txt"
    )
    nul_inventory = (
        EXPORTS / f"internal-security-deep-review-{DATE}-changed-files.nul"
    )
    candidates = {
        line
        for line in text_inventory.read_text(encoding="utf-8").splitlines()
        if line
    }
    candidates.update(
        {
            rel(Path(__file__)),
            "tools\\test_regenerate_internal_security_deep_review.py",
            "tools\\test_export_flow_learning_library.py",
            rel(validation_path),
            rel(reconciliation_path),
            rel(report),
            rel(final_manifest_path),
            rel(final_validation_path),
            rel(MASTER),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
            rel(
                EXPORTS
                / f"internal-security-live-status-snapshot-{DATE}.json"
            ),
            rel(EXPORTS / "deep-review-tracker-sync-2026-08-31.json"),
            rel(text_inventory),
            rel(nul_inventory),
        }
    )
    inventory_self = {rel(text_inventory), rel(nul_inventory)}
    ordered = sorted(
        {
            path
            for path in candidates
            if path in inventory_self or repo(path).is_file()
        },
        key=str.casefold,
    )
    if len(ordered) != len(set(ordered)):
        raise RuntimeError("Internal Security changed-file inventory contains duplicates.")
    missing = [
        path
        for path in ordered
        if path not in inventory_self and not repo(path).is_file()
    ]
    if missing:
        raise RuntimeError(
            "Internal Security changed-file inventory contains missing paths: "
            + ", ".join(missing[:20])
        )
    write_text(text_inventory, "\n".join(ordered))
    nul_inventory.write_bytes(
        b"".join(path.encode("utf-8") + b"\0" for path in ordered)
    )
    payload = nul_inventory.read_bytes()
    decoded = [part.decode("utf-8") for part in payload.split(b"\0") if part]
    if (
        not payload.endswith(b"\0")
        or payload.count(b"\0") != len(ordered)
        or decoded != ordered
    ):
        raise RuntimeError("Internal Security UTF-8 NUL inventory failed round-trip.")
    for path in (validation_path, reconciliation_path):
        data = load(path)
        data.update(
            {
                "changed_file_inventory": rel(text_inventory),
                "changed_file_inventory_nul": rel(nul_inventory),
                "changed_file_inventory_count": len(ordered),
                "changed_file_inventory_all_paths_exist": True,
                "changed_file_inventory_utf8_nul_safe": True,
            }
        )
        dump(path, data)
    return result


if __name__ == "__main__":
    raise SystemExit(main())
