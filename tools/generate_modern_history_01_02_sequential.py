"""Assemble Modern Indian History learner-v2 Topics 01-02 and visual specs.

This authoring-only generator deliberately does not finalise tracker records or render PDFs.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_v2_section_indexes as section_indexes
import notions_style_ascii_master as ascii_master


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Modern-Indian-History"
DISPLAY_SUBJECT = "Modern History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "modern-indian-history-01-02-2026-08-30-sequential.json"
GRAPHICAL_DIR = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "carvaka-graphical-specs" / SUBJECT
)
EXPORT_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "modern-indian-history--subject-wide-syllabus.json"
)
PYQ_INDEXES = [
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-INDEX.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "PYQ-INTEGRATION-AUDIT-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "PYQ-INTEGRATION-AUDIT-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "PYQ-INTEGRATION-AUDIT-2026.md",
]
COMMON_CROSS = [
    KNOWLEDGE / "00_Master-Chronology.md",
    KNOWLEDGE / "README.md",
    KNOWLEDGE / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
]
LOCAL_BOOKS = [
    ROOT / "books" / "modern india" / "MODERN INDIA -- BIPIN CHANDRA -- ENGLISH ##.pdf",
    ROOT / "books" / "medival_history" / "Medieval-History-Satish-Chandra-1526-1748-Part-2.pdf",
    ROOT / "books" / "medival_history" / "FROM PLASY TO PARTITION -- SEKAR B -- ENGLISH.pdf",
]
OFFICIAL_QUESTION_SOURCES = [
    ROOT / "knowledge-export" / "Prelims PYQ" / "QP-CSP-21-GeneralStudiesPaper-I-121021.pdf.md",
    ROOT / "knowledge-export" / "Mains PYQ" / "QP-CSM-22-GENERAL-STUDIES-PAPER I-190922.pdf.md",
]


def config(number: int, title: str, canonical: str, basic: str, advanced: str,
           legacy_main: str, legacy_workbook: str, extra: list[str],
           live_sources: list[str], current_note: str) -> dict[str, object]:
    return {
        "key": f"modern-indian-history-{number:02d}",
        "title": title,
        "canonical": KNOWLEDGE / canonical,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "legacy_main": ROOT / "notes" / SUBJECT / legacy_main,
        "legacy_workbook": ROOT / "notes" / SUBJECT / legacy_workbook,
        "extra": [KNOWLEDGE / item for item in extra],
        "live_sources": live_sources,
        "current_note": current_note,
    }


TOPICS = [
    config(
        1, "The Decline of the Mughal Empire (1707–1740s)",
        "01_The-Decline-of-the-Mughal-Empire-1707-1740s_Complete-Topic-Package.md",
        "01_Decline-of-the-Mughal-Empire.md", "01_Decline-of-the-Mughal-Empire.md",
        "01_The-Decline-of-the-Mughal-Empire-1707-1740s_Complete-Topic-Package_2026-08-09.pdf",
        "01_The-Decline-of-the-Mughal-Empire-1707-1740s_Solved-Workbook_2026-08-09.pdf",
        [],
        [
            "https://asi.nic.in/pages/WorldHeritageRedFort",
            "https://whc.unesco.org/en/list/231/",
        ],
        "The ASI and UNESCO Red Fort records are used only as a bounded material-heritage "
        "bridge for institutional and symbolic continuity. They do not establish the causes "
        "of Mughal political contraction or disputed numerical claims about the 1739 sack.",
    ),
    config(
        2, "Indian States & Society in the Eighteenth Century",
        "02_Indian-States-Society-18th-Century_Complete-Topic-Package.md",
        "02_Indian-States-and-Society-18th-Century.md",
        "02_Indian-States-and-Society-18th-Century.md",
        "02_Indian-States-Society-18th-Century_Complete-Topic-Package_2026-08-14.pdf",
        "02_Indian-States-Society-18th-Century_Solved-Workbook_2026-08-14.pdf",
        [],
        [
            "https://whc.unesco.org/en/list/1739/",
            "https://whc.unesco.org/en/list/1338/",
            "https://amritsar.nic.in/tourist-place/gobindgarh-fort/",
        ],
        "The 2025 UNESCO inscription of the Maratha Military Landscapes, UNESCO's Jantar "
        "Mantar record and the District Amritsar Gobindgarh Fort page are bounded heritage "
        "links for fort networks, scientific patronage and layered reuse. They do not prove "
        "uniform prosperity, political causation or the meaning of every eighteenth-century site.",
    ),
]


# These panels are independent authored maps of the complete core spine, not session dumps.
PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "modern-indian-history-01": [
        ("Scope: decline of command, not disappearance", "scope-map",
         """1707 -> imperial command weakens; dynasty, titles and Persianate grammar endure
CORE WINDOW -> succession, factions, jagirs, regions and Nadir Shah to the 1740s
NOT THE CLAIM -> instant 1707 collapse, universal Indian decline or Company inevitability
ANSWER RULE -> distinguish enforceable authority from symbolic legitimacy.""",
         ["01. Meaning, scope and governing thesis"]),
        ("Chronology from Aurangzeb to the 1740s", "timeline",
         """1707 Aurangzeb dies -> Bahadur Shah I 1707-12 -> Jahandar Shah 1712-13
1713 Farrukhsiyar rises with Sayyid support -> 1719 deposition and enthronements
1720 Sayyids fall -> 1724 Nizam's Hyderabad autonomy -> 1739 Karnal and Delhi
1740s -> regional bargaining and frontier pressure; later Durrani/Panipat stay bounded.""",
         ["01. Meaning, scope and governing thesis", "08. Court politics"]),
        ("Succession instability: throne becomes a prize", "causal-chain",
         """NO FIXED PRIMOGENITURE -> princes mobilise households and noble clients
SUCCESSION WAR -> victory reallocates mansab, jagir and office
REPEATED CONTEST -> emperor cannot credibly arbitrate elite competition
RESULT -> political transmission fails; it is a mechanism, not a lone cause.""",
         ["08. Court politics", "19. Why central authority declined"]),
        ("Factions and the Sayyid moment", "actor-network",
         """TURANI / IRANI / AFGHAN / HINDUSTANI -> shifting patronage formations
FARRUKHSIYAR 1713 -> Sayyid Brothers supply military-political support
1719 -> kingmaking exposes the throne's dependence on coalition control
1720 -> Sayyids removed; factional politics survives the two individuals.""",
         ["08. Court politics", "09. The Sayyid Brothers"]),
        ("Jagirdari vocabulary prevents category errors", "comparison-matrix",
         """JAGIR -> transferable revenue assignment, not private landownership
JAMA -> assessed claim | HASIL -> realised collection
PAIBAQI -> reserve assignable pool | BE-JAGIRI -> usable jagir shortage
TRAP -> nominal assessment never automatically measures treasury cash or welfare.""",
         ["03. Imperial structure inherited in 1707", "11. Jagirdari crisis"]),
        ("Fiscal-military feedback loop", "feedback-loop",
         """MORE CLAIMANTS + WEAK PAIBAQI -> scramble for productive jagirs
SHORT TENURE / EXTRACTION -> resistance, evasion, flight or negotiation
LOWER HASIL -> unpaid contingents and weaker imperial service
WEAKER CONTROL -> regional retention of revenue -> still lower central capacity.""",
         ["11. Jagirdari crisis", "19. Why central authority declined"]),
        ("Aurangzeb's legacy: a weighted background", "balance-sheet",
         """DECCAN WAR -> garrisons, transport, remounts and unresolved Maratha challenge
ANNEXATIONS -> territory and claims grow faster than reliable realisation
NORTH ABSENCE -> strains of supervision and arbitration
QUALIFY -> legacy mattered, but Aurangzeb alone cannot explain post-1707 factions or regions.""",
         ["04. Late-Aurangzeb strains", "19. Why central authority declined"]),
        ("Agrarian and regional assertion", "systems-map",
         """REVENUE PRESSURE -> zamindars, peasants and intermediaries bargain or resist
GOVERNORS + BANKERS + ARMED FOLLOWINGS -> provincial resource control
MARATHA / SIKH / JAT mobilisation -> distinct political routes, not one rebellion
RESULT -> Delhi's weakening and regional state-making reinforce each other.""",
         ["12. Agrarian pressure", "13. Regional assertion"]),
        ("Successor-state spectrum", "authority-spectrum",
         """BENGAL -> Murshid Quli Khan | AWADH -> Saadat Khan | HYDERABAD -> Nizam-ul-Mulk
IMPERIAL OFFICE -> local revenue, army and patronage become durable
COIN / KHUTBA / TITLE -> formal Mughal legitimacy may remain useful
TRAP -> autonomy in substance does not require a modern declaration of independence.""",
         ["14. Provincial autonomy", "20. Continuities after political contraction"]),
        ("Nadir Shah: shock exposes a prior crisis", "shock-sequence",
         """FRONTIER WEAKNESS + Persian military capacity -> invasion opportunity
KARNAL, 24 FEBRUARY 1739 -> fragmented command loses to unified command
DELHI -> sack, treasury loss and prestige shock; Muhammad Shah remains emperor
VERDICT -> accelerant and revealer, not the original cause of decline.""",
         ["18. Nadir Shah's invasion", "19. Why central authority declined"]),
        ("Institutional continuity after contraction", "continuity-map",
         """EMPEROR / FARMAN / SANAD -> symbolic arbitration and legal vocabulary
COIN + KHUTBA -> layered legitimacy | PERSIAN CHANCERY -> portable administration
MANSAB / DIWAN / ZAMINDAR -> institutions repurposed in regional arenas
RULE -> continuity of form coexists with change in who commands resources.""",
         ["20. Continuities after political contraction"]),
        ("Topic 01 answer spine", "answer-synthesis",
         """OPEN -> central fiscal-military command declined inside a continuing political culture
EXPLAIN -> succession + faction + jagir-agrarian strain + regional assertion
WEIGH -> Deccan legacy matters; reject Aurangzeb-only monocausality
TEST -> Nadir 1739 exposes weakness; continuity and regional variation qualify conclusion
CLOSE -> stop core chronology in the 1740s.""",
         ["19. Why central authority declined", "20. Continuities after political contraction"]),
    ],
    "modern-indian-history-02": [
        ("Eighteenth-century frame: crisis and reordering", "scope-map",
         """MUGHAL CENTRE CONTRACTS -> provincial, confederate and local arenas gain leverage
CORE QUESTION -> how revenue, armed labour, credit and legitimacy form regional states
TWO ERRORS -> pure chaos / universal prosperity
VERDICT -> uneven state formation, commercial continuity and social cost coexist.""",
         ["01. Scope, periodisation and governing debate"]),
        ("Three state types, not one hierarchy", "classification-table",
         """SUCCESSOR -> Bengal, Awadh, Hyderabad: Mughal office becomes practical autonomy
AUTONOMOUS / REGIONAL -> Mysore, Travancore, Rajput houses: older fields centralise selectively
NEW / MOBILISED -> Marathas, Sikhs, Jats, Rohillas: armed networks and local solidarities
RULE -> origin category does not predetermine capacity or welfare.""",
         ["03. Political map after Mughal weakening"]),
        ("Regional chronology and bounded sequence", "timeline",
         """1707-20 -> succession, Shahu-Tarabai conflict and Banda Bahadur
1720s-40s -> Hyderabad, Awadh, Bengal consolidate; Baji Rao expands
1740s-61 -> Alivardi, Maratha northern bid, Sikh recovery and Afghan pressure
POST-1761 -> later Mysore, Ranjit Singh and Company only as bounded trajectory.""",
         ["01. Scope, periodisation and governing debate"]),
        ("Hyderabad, Awadh and Bengal compared", "comparison-matrix",
         """HYDERABAD -> Nizam-ul-Mulk turns subedari and military authority into autonomy
AWADH -> Saadat Khan / Safdar Jang work through chiefs, taluqdars and imperial office
BENGAL -> Murshid Quli Khan and successors concentrate revenue and banking links
SHARED -> Mughal forms survive | DIFFERENCE -> alliance, finance and local control vary.""",
         ["05. Successor states"]),
        ("Maratha confederacy: reach and coordination", "network-map",
         """SATARA / POONA -> chhatrapati, Peshwa and negotiated leadership
CHAUTH + SARDESHMUKHI -> fiscal claims interact with local collection
SCINDIA / HOLKAR / GAEKWAD / BHONSLE -> expanding houses and regional bases
TRAP -> neither a unitary nation-state nor only raiding; coordination had limits.""",
         ["06. Marathas"]),
        ("Sikhs: community, mobilisation and misls", "process",
         """KHALSA LEGACY -> persecution, mobilisation and armed community formation
BANDA BAHADUR -> early challenge; later repression changes the field
DAL KHALSA / MISLS -> fluid armed-territorial networks in Punjab
BOUNDARY -> Ranjit Singh belongs only as a later consolidating bridge.""",
         ["07. Sikhs"]),
        ("Mysore, Rajputs and Jats: bounded comparisons", "comparison",
         """MYSORE -> Haidar Ali / Tipu: military and administrative centralisation, later bounded
RAJPUT STATES -> court, tribute, diplomacy and selective autonomy
JATS -> agrarian-zamindari mobilisation around Bharatpur and Suraj Mal
RULE -> compare resource route and legitimacy; avoid a single 'rebel state' label.""",
         ["08. Other regional states"]),
        ("State-formation engine", "feedback-loop",
         """REVENUE ASSESSMENT + INTERMEDIARIES -> treasury and credit
CREDIT / BANKERS -> advances, remittance and military payment
ARMY -> enforces revenue and rewards clients -> court and patronage become durable
LIMIT -> warfare and extraction can strengthen rulers while burdening cultivators.""",
         ["04. State formation engine"]),
        ("Society: hierarchy with differentiated agency", "social-map",
         """CASTE / CLASS / REGION -> condition access to land, work, honour and mobility
WOMEN -> elite sources show particular agency; ordinary labour needs cautious reconstruction
PEASANTS -> production base facing varied rents, dues, credit and war disruption
SOLDIERS / OFFICIALS -> selective mobility without dissolving hierarchy.""",
         ["12. Society: caste, gender and social groups"]),
        ("Commercialisation links town and countryside", "circulation-system",
         """PEASANT SURPLUS -> markets, revenue and military supply
ARTISANS -> textiles, arms and specialised work | MERCHANTS -> brokerage and trade
BANKERS / HUNDIS -> credit and long-distance remittance
QUALIFY -> commercial dynamism does not prove equal prosperity or secure cultivation.""",
         ["13. Economy, commerce and production"]),
        ("Culture and institutional continuity", "culture-map",
         """PERSIANATE COURTS + regional languages -> administrative and literary continuity
COURTS / TOWNS -> art, architecture, music and patronage shift regionally
MUGHAL SYMBOLS -> titles, coin, khutba and records remain politically usable
VERDICT -> cultural production persists amid war, hierarchy and changing patrons.""",
         ["14. Culture, continuity and change"]),
        ("Topic 02 answer spine", "answer-synthesis",
         """CLASSIFY -> successor / autonomous-regional / newly mobilised states
COMPARE -> Hyderabad, Awadh, Bengal, Marathas, Sikhs, Mysore, Rajputs and Jats
EXPLAIN -> administration, revenue, army, credit and local alliances
INTEGRATE -> caste, gender, peasants, artisans and commercial networks
CLOSE -> neither chaos nor prosperity was universal; give a region-and-group verdict.""",
         ["23. Crisis, transition or regional resurgence"]),
    ],
}


EXTRA_MCQS = {
    "modern-indian-history-01": [
        ("Which distinction best captures Mughal decline after 1707?",
         "Central enforcement weakened while dynastic legitimacy and administrative vocabulary persisted.",
         ["The dynasty vanished immediately.", "All regional states rejected Mughal forms.", "Trade ceased across India."]),
        ("What did the Sayyid Brothers' kingmaking primarily demonstrate?",
         "Court coalitions could control accession without becoming emperors themselves.",
         ["A fixed law of primogeniture worked.", "Jagirs became private estates.", "Nadir Shah ruled Delhi."]),
        ("Why is a high jama not proof of a strong imperial treasury?",
         "Jama was an assessed claim that could exceed realised hasil.",
         ["It measured coinage only.", "It abolished local intermediaries.", "It recorded military victories."]),
        ("How should Aurangzeb's Deccan wars be used in explanation?",
         "As an inherited fiscal-military strain within a wider causal interaction.",
         ["As the sole cause of all later decline.", "As proof that provinces had no agency.", "As an event after Nadir Shah."]),
        ("Which inference from provincial autonomy is safest?",
         "Governors could retain Mughal symbols while controlling practical revenue and patronage.",
         ["Every province became a modern nation-state.", "Coinage proves direct Delhi taxation.", "All governors stopped using imperial titles."]),
        ("What does Nadir Shah's victory at Karnal most directly reveal?",
         "Fragmented Mughal command was vulnerable to a coordinated invading force.",
         ["The invasion caused every earlier fiscal strain.", "Persia annexed the Gangetic plain.", "Mughal legitimacy disappeared that day."]),
        ("Which actor belongs to the agrarian-regional feedback rather than only court politics?",
         "Zamindars negotiating, resisting or withholding cooperation.",
         ["The Peacock Throne as an object.", "A single chronicler's adjective.", "Only foreign merchants."]),
        ("Which claim should be rejected in a core answer?",
         "Aurangzeb alone explains the post-1707 imperial crisis.",
         ["Succession wars weakened arbitration.", "Jagirdari pressure affected service ties.", "Regional assertion had varied routes."]),
        ("What is be-jagiri?",
         "A shortage of sufficiently productive and usable jagirs for claimants.",
         ["A title for the provincial diwan.", "A Persian invasion route.", "A category of private freehold."]),
        ("Why should the core chronology stop in the 1740s?",
         "Later Durrani invasions and Panipat are consequences or bridges, not this topic's core causal field.",
         ["Nothing happened after 1740.", "Mughal institutions ended in 1740.", "Nadir Shah became Mughal emperor."]),
        ("What is the best use of coin and khutba evidence?",
         "It can show a claim to Mughal legitimacy but not daily administrative obedience.",
         ["It proves universal prosperity.", "It makes farmans unnecessary.", "It proves a modern national border."]),
        ("Which answer structure is most defensible?",
         "Weigh succession, faction, fiscal-military strain, regional assertion and Nadir's shock together.",
         ["List only emperor nicknames.", "Treat invasion as the lone origin.", "Equate all regions with Delhi."]),
        ("Why did short jagir tenure create pressure?",
         "It could reward rapid extraction over durable local cooperation.",
         ["It guaranteed higher hasil.", "It abolished mansab service.", "It made all zamindars royal officials."]),
        ("What continuity qualified the image of total collapse?",
         "Regional rulers continued to use Persianate offices, grants and legitimacy idioms.",
         ["No rulers maintained armies.", "Delhi no longer mattered symbolically.", "All cultural production stopped."]),
        ("Which wording is safest about 1739 Delhi?",
         "It was a severe prestige and fiscal shock with contested numerical estimates.",
         ["It permits a fixed casualty total without sources.", "It established permanent Persian rule.", "It erased all regional economies."]),
        ("What separates faction from ethnicity in this context?",
         "Patronage coalitions shifted and cannot be read as permanent ethnic voting blocs.",
         ["Every noble acted only by birthplace.", "Only one group held office.", "Faction ended in 1720."]),
        ("Which factor is an external shock rather than an original internal mechanism?",
         "Nadir Shah's 1739 invasion.",
         ["Jagir-realisation mismatch.", "Succession conflict.", "Provincial retention of resources."]),
        ("What did regional assertion do to imperial capacity?",
         "It reduced reliable remittance and made central enforcement more difficult.",
         ["It instantly ended symbolic sovereignty.", "It removed all local diversity.", "It guaranteed Company conquest."]),
        ("Which conclusion reflects institutional continuity?",
         "Mughal political grammar outlasted Mughal capacity to command it.",
         ["Administrative terms vanished in 1707.", "Autonomy required abandoning titles.", "Decline ended all record-keeping."]),
        ("What is the final qualified verdict?",
         "The 1707-1740s saw declining central capacity and uneven regional reorganisation, not one monocausal collapse.",
         ["The century was uniformly prosperous.", "The century was uniformly empty of order.", "Only personalities explain history."]),
    ],
    "modern-indian-history-02": [
        ("What distinguishes a successor state from a new mobilised state?",
         "A successor state converted Mughal provincial office into autonomy, while a mobilised state grew through other armed-local routes.",
         ["Successor states had no revenue systems.", "New states never used legitimacy.", "Both were modern republics."]),
        ("Which is the safest description of Hyderabad after 1724?",
         "It combined the Nizam's provincial-military power with retained Mughal political forms.",
         ["It rejected every imperial title immediately.", "It was a Sikh misl.", "It had no Deccan context."]),
        ("What did Awadh's state formation especially require?",
         "Accommodation with local chiefs, zamindars and imperial office.",
         ["The abolition of revenue collection.", "Direct control by Persian invaders.", "A unitary Maratha command."]),
        ("Why is Bengal's commercial wealth not a welfare statistic?",
         "Trade and revenue strength can coexist with unequal social and agrarian outcomes.",
         ["Commerce makes war impossible.", "Bankers replace all rulers.", "Artisans own all land."]),
        ("Which label fits the Maratha polity best?",
         "A fiscal-military confederacy with negotiated leadership and regional houses.",
         ["A uniform central bureaucracy.", "A movement without diplomacy.", "A permanent Delhi province."]),
        ("What is a necessary caution about Sikh misls?",
         "They were fluid armed-territorial formations rather than a timeless fixed map.",
         ["They were Mughal revenue districts.", "They existed only after British rule.", "They lacked any political role."]),
        ("How should Mysore be included here?",
         "As a bounded case of regional centralisation, without turning the topic into later Anglo-Mysore wars.",
         ["As proof every state was identical.", "As a successor province of Bengal.", "As a reason to omit the Marathas."]),
        ("What makes Jat state formation analytically distinct?",
         "Agrarian-zamindari mobilisation and regional consolidation shaped its route.",
         ["It was a direct copy of Hyderabad.", "It lacked local social bases.", "It ended all Mughal symbols everywhere."]),
        ("What did merchant-bankers contribute?",
         "Credit, remittance and brokerage linking rulers, markets and military finance.",
         ["Only religious authority.", "An automatic end to peasant production.", "A replacement for all armies."]),
        ("What does a hundi primarily illustrate?",
         "The movement of credit and value across distance.",
         ["A cavalry rank.", "A fortification type.", "A caste census."]),
        ("Which statement on artisans is most defensible?",
         "Skilled production and commercial links persisted, but outcomes differed by region and group.",
         ["All artisans became court officials.", "Production disappeared outside Europe.", "Craft evidence proves universal prosperity."]),
        ("How should gender evidence be handled?",
         "Elite records show particular agency but cannot stand for all women's work or autonomy.",
         ["One memoir is a social census.", "Gender had no relation to class.", "Only royal women worked."]),
        ("What social condition best qualifies regional resurgence?",
         "Caste, class, credit and warfare produced unequal costs and opportunities.",
         ["Every group gained equally.", "Agriculture ceased to matter.", "Political change erased hierarchy."]),
        ("What does cultural continuity mean here?",
         "Patronage, languages and Persianate administrative forms adapted to regional courts.",
         ["Culture was frozen unchanged.", "Political conflict erased all artistic work.", "Only Delhi could sponsor culture."]),
        ("Which approach avoids the 'dark age' trap?",
         "Separate imperial crisis from varied regional political, economic and cultural evidence.",
         ["Generalise Delhi's disorder to all India.", "Generalise Bengal's commerce to all groups.", "Ignore warfare entirely."]),
        ("What did revenue systems and armies have in common?",
         "They formed a reciprocal fiscal-military mechanism mediated by local alliances and credit.",
         ["They operated without cultivators.", "They prevented all interstate conflict.", "They made legitimacy irrelevant."]),
        ("Why retain Rajput states in the comparison?",
         "They show older regional political fields with their own courtly, tributary and diplomatic logics.",
         ["They were all successor states.", "They had no relation to Mughal politics.", "They make chronology unnecessary."]),
        ("What is the correct Company bridge?",
         "Regional rivalry created openings, but conquest required later Company finance, alliances and military organisation.",
         ["Regional states automatically caused conquest.", "Companies were absent from Indian networks.", "Panipat immediately gave Britain India."]),
        ("Which evidence best supports a layered sovereignty claim?",
         "A ruler may retain Mughal titles while independently directing regional revenue and armies.",
         ["A title proves daily obedience.", "A battle removes all institutions.", "A court painting fixes a border."]),
        ("What is the most balanced final verdict?",
         "The century combined state formation and commercial-cultural continuity with war, extraction and uneven social outcomes.",
         ["It was only anarchy.", "It was universal prosperity.", "It had no institutional inheritance."]),
    ],
}


def split_h2(text: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"(?m)^## (.+?)\s*$", text))
    if not matches:
        raise ValueError("Canonical source has no H2 headings.")
    parts: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        parts.append((match.group(1), text[match.start():end].strip()))
    return text[:matches[0].start()].strip(), parts


def demote_h2(fragment: str) -> str:
    """Keep source substructure while guaranteeing the learner-v2 H2 contract."""
    return re.sub(r"(?m)^#{1,2} ", "### ", fragment).strip()


def metadata_fragment(fragment: str) -> str:
    """Retain package metadata without letting it become a teaching session."""
    lines = fragment.splitlines()
    if lines and lines[0].startswith("## "):
        lines[0] = "#### " + lines[0][3:]
    return "\n".join(lines).strip()


def teaching_session_fragment(fragment: str, number: int) -> str:
    """Promote each numbered canonical topic to one explicit learner session."""
    lines = fragment.splitlines()
    if not lines or not lines[0].startswith("## "):
        raise ValueError("Teaching fragment lacks its canonical H2 heading.")
    title = lines[0][3:].strip()
    transformed = [f"### SESSION {number} — {title}"]
    for line in lines[1:]:
        if line.startswith("##### "):
            transformed.append("#" + line)
        elif line.startswith("#### "):
            transformed.append("#" + line)
        elif line.startswith("### "):
            transformed.append("#" + line)
        else:
            transformed.append(line)
    return "\n".join(transformed).strip()


def first_question_stem(block: str, fallback: str) -> str:
    for line in block.splitlines():
        candidate = re.sub(r"[*`]", "", line).strip()
        if candidate.endswith("?") and not candidate.startswith(("A.", "B.", "C.", "D.")):
            return candidate
    return fallback


def rebalance_block(block: str, expected: str) -> str:
    answer = re.search(
        r"(?mi)^(?:\*\*Answer:\s*([A-D])\.?\*{0,2}|\*\*Answer:\*\*\s*([A-D])\.)",
        block,
    )
    options = re.findall(r"(?m)^-?\s*([A-D])\.\s+(.+?)\s*$", block)
    if answer is None or len(options) < 4:
        raise ValueError("Unable to parse a canonical MCQ for safe option rotation.")
    option_map = dict(options[:4])
    actual = next(group for group in answer.groups() if group).upper()
    correct = option_map[actual]
    wrongs = [option_map[letter] for letter in "ABCD" if letter != actual]
    ordered = {expected: correct}
    for letter, value in zip([letter for letter in "ABCD" if letter != expected], wrongs):
        ordered[letter] = value
    first_option = re.search(r"(?m)^-?\s*A\.\s+.+?$", block)
    last_option = list(re.finditer(r"(?m)^-?\s*D\.\s+.+?$", block))
    if first_option is None or not last_option:
        raise ValueError("Canonical MCQ option bounds are missing.")
    replacement = "\n".join(f"{letter}. {ordered[letter]}" for letter in "ABCD")
    block = block[:first_option.start()] + replacement + block[last_option[-1].end():]
    return re.sub(
        r"(?mi)^(?:\*\*Answer:\s*[A-D]\.?\*{0,2}|\*\*Answer:\*\*\s*[A-D]\..*)$",
        f"**Answer: {expected}.**",
        block,
        count=1,
    )


def authored_mcq(number: int, stem: str, correct: str, wrongs: list[str], expected: str) -> str:
    choices = {expected: correct}
    for letter, text in zip([letter for letter in "ABCD" if letter != expected], wrongs):
        choices[letter] = text
    return (
        f"### Q{number}. {stem}\n\n"
        + "\n".join(f"{letter}. {choices[letter]}" for letter in "ABCD")
        + f"\n\n**Answer: {expected}.**\n"
        + f"**Explanation:** {correct}\n"
    )


def build_mcqs(source: str, key: str) -> str:
    pattern = re.compile(r"(?m)^## (?:Hard|Remedial) MCQ (\d+)\s*$")
    matches = list(pattern.finditer(source))
    if len(matches) != 60:
        raise ValueError(f"{key}: expected 60 canonical MCQs, found {len(matches)}.")
    blocks: list[str] = []
    for index, match in enumerate(matches, 1):
        if index < len(matches):
            end = matches[index].start()
        else:
            next_section = re.search(r"(?m)^## PART IV\b", source[match.end():])
            end = match.end() + next_section.start() if next_section else len(source)
        raw = source[match.start():end].strip()
        stem = first_question_stem(raw, f"Canonical concept check {index}")
        raw = pattern.sub("", raw, count=1).strip()
        raw = rebalance_block(raw, "ABCD"[(index - 1) % 4])
        blocks.append(f"### Q{index}. {stem}\n\n{raw}")
    for offset, (stem, correct, wrongs) in enumerate(EXTRA_MCQS[key], 61):
        blocks.append(authored_mcq(offset, stem, correct, wrongs, "ABCD"[(offset - 1) % 4]))
    return "\n\n".join(blocks)


def assemble(config_value: dict[str, object]) -> str:
    source = Path(config_value["canonical"]).read_text(encoding="utf-8")
    preamble, sections = split_h2(source)
    basic_metadata: list[str] = []
    basic_sessions: list[str] = []
    practice: list[str] = []
    register: list[str] = []
    for title, fragment in sections:
        if title.startswith("PART III") or re.match(r"^(?:Hard|Remedial) MCQ", title):
            continue
        if title.startswith("PART II") or title.startswith("PYQ ") or title.startswith("PART IV") or title.startswith("Mains "):
            practice.append(demote_h2(fragment))
        elif title.startswith("FINAL CONSOLIDATED"):
            register.append(demote_h2(fragment))
        elif re.match(r"^\d{2}\.\s+", title):
            basic_sessions.append(
                teaching_session_fragment(fragment, len(basic_sessions) + 1)
            )
        else:
            basic_metadata.append(metadata_fragment(fragment))
    key = str(config_value["key"])
    advanced = Path(config_value["advanced"]).read_text(encoding="utf-8")
    source_audit = (
        "#### Source audit and syllabus boundary\n\n"
        f"Markdown-first assembly uses the canonical package plus the paired Basic and Advanced owners. "
        f"OCR sources are listed in the manifest for deeper checking; no live source is used except bounded "
        f"heritage linkage. Verified local PYQs retain their provenance; unavailable keys remain labelled "
        f"inferred, and no direct UPSC question is invented."
    )
    return (
        f"# {config_value['title']} — Learner-v2 Complete Learning Session\n\n"
        + re.sub(r"(?m)^# .+\n*", "", preamble).strip()
        + "\n\n## BASIC LEARNING SESSION\n\n"
        + source_audit
        + "\n\n"
        + "\n\n".join(basic_metadata)
        + "\n\n"
        + "\n\n".join(basic_sessions)
        + "\n\n## BASIC MCQS / REMEDIATION\n\n"
        + build_mcqs(source, key)
        + "\n\n## PYQS AND ANSWER PRACTICE\n\n"
        + "\n\n".join(practice)
        + "\n\n## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER\n\n"
        + demote_h2(advanced)
        + "\n\n## CONSOLIDATED REGISTER NOTES\n\n"
        + "\n\n".join(register)
        + "\n\n### COMPLETE TOPIC ASCII MASTER FLOW DIAGRAM\n\n"
        + ascii_master.build_manual_fragment(
            ascii_master.normalize_manual_spec_file(ASCII_PATH)[key]
        )
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
                raise ValueError(f"{key}: ASCII line exceeds 100 characters in {title!r}.")
            panels.append({"title": title, "structural_type": structural_type,
                           "ascii_lines": lines, "source_references": references})
        if len(panels) != 12:
            raise ValueError(f"{key}: expected 12 panels, found {len(panels)}.")
        topics.append({"topic_key": key, "display_title": config_value["title"],
                       "source_markdown": str(Path(config_value["canonical"]).relative_to(ROOT)),
                       "panel_count": 12, "panels": panels})
    payload = {
        "schema_version": 1, "generated_on": DATE,
        "scope": "Modern Indian History learner-v2 Topics 01-02",
        "constraints": {"panel_count_per_topic": 12, "max_line_width": 100,
                        "manual_topic_specific": True, "complete_embed_ready_lines": True,
                        "tracker_untouched": True},
        "topics": topics,
    }
    ASCII_DIR.mkdir(parents=True, exist_ok=True)
    ASCII_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_graphical_spec(config_value: dict[str, object], markdown: str) -> Path:
    key = str(config_value["key"])
    panels = [{"title": title, "body": body, "structural_type": kind,
               "source_references": refs} for title, kind, body, refs in PANEL_DATA[key]]
    source_path = SESSION_DIR / f"{key}_Learning-Session.md"
    spec = carvaka_flowchart.author_topic_spec(
        topic_key=key, subject=SUBJECT, title=str(config_value["title"]),
        source_markdown=markdown, source_markdown_path=str(source_path.relative_to(ROOT)),
        ascii_spec_path=str(ASCII_PATH.relative_to(ROOT)),
        ascii_spec_sha256=hashlib.sha256(ASCII_PATH.read_bytes()).hexdigest(),
        panels=panels, source_generation=2,
    )
    if len(spec["stages"]) != 13:
        raise ValueError(f"{key}: expected a 13-stage graphical master.")
    GRAPHICAL_DIR.mkdir(parents=True, exist_ok=True)
    output = GRAPHICAL_DIR / f"{key}.json"
    output.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def write_section_manifest() -> Path:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    target = next(
        topic
        for topic in catalog["topics"]
        if topic.get("topic_key") == "modern-indian-history-01"
    )
    manifest = section_indexes.materialize_catalog_section_manifest(
        ROOT,
        catalog,
        target,
    )
    if manifest != SECTION_MANIFEST:
        raise ValueError(f"Unexpected Modern History section manifest: {manifest}")
    return manifest


def write_generation_spec(config_value: dict[str, object], source_path: Path, graphical_path: Path) -> Path:
    sources = [Path(config_value[name]) for name in ("basic", "advanced", "canonical", "legacy_main", "legacy_workbook")]
    sources += [
        source_path,
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *COMMON_CROSS,
        *PYQ_INDEXES,
        *OFFICIAL_QUESTION_SOURCES,
        *LOCAL_BOOKS,
    ]
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    key = str(config_value["key"])
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog_topic = next(
        topic for topic in catalog["topics"] if topic.get("topic_key") == key
    )
    payload = {
        "schema_version": 1, "topic_key": key, "subject": SUBJECT,
        "section": "Subject-Wide-Syllabus", "topic_folder": key, "title": config_value["title"],
        "variant": "learner-v2", "generation": 2, "generation_date": DATE,
        "command": catalog_topic["learner_v2_command"],
        "source_markdown": str(source_path.relative_to(ROOT)),
        "source_basic": str(Path(config_value["basic"]).relative_to(ROOT)),
        "source_canonical": str(Path(config_value["canonical"]).relative_to(ROOT)),
        "source_advanced": str(Path(config_value["advanced"]).relative_to(ROOT)),
        "manifest": str(SECTION_MANIFEST.relative_to(ROOT)),
        "cross_topic_sources": [str(path.relative_to(ROOT)) for path in COMMON_CROSS],
        "local_ocr_sources": [str(path.relative_to(ROOT)) for path in LOCAL_BOOKS],
        "pyq_indexes": [str(path.relative_to(ROOT)) for path in PYQ_INDEXES],
        "official_question_sources": [
            str(path.relative_to(ROOT)) for path in OFFICIAL_QUESTION_SOURCES
        ],
        "live_sources": config_value["live_sources"],
        "source_files": [str(path.relative_to(ROOT)) for path in sources],
        "practice_profile": "80 independently worded MCQs; strict A-B-C-D repeated 20 times; canonical PYQ provenance retained.",
        "pyq_status_note": "Verified local provenance is preserved; unavailable official keys remain inferred and no direct UPSC wording is fabricated.",
        "current_linkage_note": config_value["current_note"],
        "mcq_answer_policy": "strict-abcd-cycle", "tracker_untouched": True,
    }
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    output = EXPORT_DIR / f"{key}-new-topic-{DATE}.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def self_check(markdown: str, key: str, graphical_path: Path) -> None:
    headings = re.findall(r"(?m)^## (.+?)\s*$", markdown)
    required = ["BASIC LEARNING SESSION", "BASIC MCQS / REMEDIATION", "PYQS AND ANSWER PRACTICE",
                "OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER", "CONSOLIDATED REGISTER NOTES"]
    if [item for item in headings if item in required] != required or headings[-1] != required[-1]:
        raise ValueError(f"{key}: learner-v2 H2 order is invalid.")
    mcq_section = re.search(r"(?ms)^## BASIC MCQS / REMEDIATION\s*$\n(.*?)^## PYQS AND ANSWER PRACTICE", markdown)
    if mcq_section is None:
        raise ValueError(f"{key}: MCQ section missing.")
    answers = re.findall(r"(?mi)^\*\*Answer:\s*([A-D])\.\*\*$", mcq_section.group(1))
    stems = re.findall(r"(?m)^### Q\d+\. (.+?)\s*$", mcq_section.group(1))
    normalized = [re.sub(r"[^a-z0-9]+", " ", stem.casefold()).strip() for stem in stems]
    if answers != list("ABCD" * 20) or len(stems) != 80 or len(set(normalized)) != 80:
        raise ValueError(f"{key}: MCQ rotation, count or normalized-stem uniqueness failed.")
    spec = ascii_master.normalize_manual_spec_file(ASCII_PATH)[key]
    if len(spec.panels) != 12 or markdown.count("```ascii-master") != 12:
        raise ValueError(f"{key}: authored ASCII panel count failed.")
    if len(json.loads(graphical_path.read_text(encoding="utf-8"))["stages"]) != 13:
        raise ValueError(f"{key}: graphical stage count failed.")


def main() -> int:
    write_ascii_spec()
    write_section_manifest()
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = [ASCII_PATH, SECTION_MANIFEST]
    for config_value in TOPICS:
        markdown = assemble(config_value)
        source_path = SESSION_DIR / f"{config_value['key']}_Learning-Session.md"
        source_path.write_text(markdown, encoding="utf-8")
        graphical_path = write_graphical_spec(config_value, markdown)
        manifest = write_generation_spec(config_value, source_path, graphical_path)
        self_check(markdown, str(config_value["key"]), graphical_path)
        written.extend([source_path, graphical_path, manifest])
    for path in written:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
