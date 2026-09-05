"""Assemble Medieval History learner-v2 Topics 23-25 and visual specs."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import carvaka_flowchart
import generate_medieval_history_21_22_sequential as previous


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-30"
SUBJECT = "Medieval-Indian-History"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / SUBJECT
SESSION_DIR = KNOWLEDGE / "learning-sessions" / "v2" / "subject-wide-syllabus"
ASCII_DIR = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
ASCII_PATH = ASCII_DIR / "medieval-indian-history-23-25-2026-08-30-sequential.json"
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
PRELIMS_PYQ_DIR = ROOT / "knowledge-export" / "Prelims PYQ"
MAINS_PYQ_DIR = ROOT / "knowledge-export" / "Mains PYQ"
TOPIC_24_OFFICIAL_QUESTIONS = [
    PRELIMS_PYQ_DIR / "QP-CSP-18-GS-I-C.pdf.md",
    PRELIMS_PYQ_DIR / "csp-p1.pdf.md",
    PRELIMS_PYQ_DIR / "CSP_2020_GS_Paper-1.pdf.md",
    PRELIMS_PYQ_DIR / "GENERAL STUDIES PAPER I.pdf.md",
    MAINS_PYQ_DIR / "Gen_St_P1.pdf.md",
]
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
        23,
        "The Marathas, Shivaji & Aurangzeb's Deccan; Jagirdari Crisis",
        "23_Marathas-Shivaji-Aurangzeb-Deccan-Jagirdari-Crisis_Complete-Topic-Package.md",
        "23_Marathas-Shivaji-and-Deccan.md",
        "23_Marathas-Shivaji-and-Deccan.md",
        "23_Marathas-Shivaji-Aurangzeb-Deccan-Jagirdari-Crisis_Complete-Learning-Session_2026-08-19.pdf",
        "23_Marathas-Shivaji-Aurangzeb-Deccan-Jagirdari-Crisis_Premium-Solved-PYQ-Workbook_2026-08-19.pdf",
        "No fabricated direct CSE PYQ; exactly 80 independent MCQs in a "
        "strict A-B-C-D cycle and 12 examiner-grade solved Mains answers.",
        [
            "https://pib.gov.in/PressReleasePage.aspx?"
            "PRID=2240848&reg=1&lang=1",
            "https://whc.unesco.org/en/list/1739/",
        ],
        "PIB's 16 March 2026 release reports site-management and conservation "
        "arrangements for the twelve Maratha Military Landscapes forts, "
        "including ASI or state responsibility and site management. UNESCO "
        "identifies twelve forts, including Raigad, Shivneri and Sindhudurg, "
        "as a strategically located network supporting defence, trade "
        "protection and territorial control. These sources are used only as "
        "bounded heritage and spatial evidence. They do not prove every "
        "seventeenth-century tactical episode, modern nationalism, exact "
        "force sizes, or the institutional meaning of chauth or the "
        "jagirdari crisis.",
        "Maratha forts state-building Deccan war and jagirdari crisis cover",
        "notes/Medieval-Indian-History/assets/"
        "23_Marathas-Shivaji-Aurangzeb-Deccan-Jagirdari-Crisis/"
        "00_00_cover.png",
        [
            "learning-sessions\\23_Marathas-Shivaji-Aurangzeb-Deccan-Jagirdari-Crisis_Complete-Learning-Session_2026-08-19.md",
            "learning-sessions\\23_Marathas-Shivaji-Aurangzeb-Deccan-Jagirdari-Crisis_Premium-Solved-PYQ-Workbook_2026-08-19.md",
        ],
        [],
    ),
    topic_config(
        24,
        "Mughal Society, Economy & Culture",
        "24_Mughal-Society-Economy-Culture_Complete-Topic-Package.md",
        "24_Mughal-Society-Economy-Culture.md",
        "24_Mughal-Society-Economy-Culture.md",
        "24_Mughal-Society-Economy-Culture_Complete-Learning-Session_2026-08-19.pdf",
        "24_Mughal-Society-Economy-Culture_Premium-Solved-PYQ-Workbook_2026-08-19.pdf",
        "Five exact routed UPSC PYQs are preserved from locally held official "
        "paper extracts; answer keys without local official keys are labelled "
        "inferred. Exactly 80 independent MCQs follow a strict A-B-C-D cycle, "
        "with 12 examiner-grade solved Mains answers.",
        [
            "https://culture.gov.in/our-organisations/"
            "archaeological-survey-india-new-delhi",
            "https://whc.unesco.org/en/list/252/",
            "https://whc.unesco.org/en/list/231/",
        ],
        "Rechecked on 30 August 2026. The ASI mandate and UNESCO Taj Mahal "
        "and Red Fort pages support monument conservation, skilled and "
        "artisanal production, composite architectural traditions, material "
        "setting and patronage. They are not evidence of universal "
        "prosperity, social equality, exact GDP, private landownership, or "
        "the reach of imperial policy. No genuinely topic-specific new "
        "official event was found in the preceding six months, so static "
        "relevance is retained.",
        "Mughal society economy commerce crafts and composite culture cover",
        "notes/Medieval-Indian-History/assets/"
        "24_Mughal-Society-Economy-Culture/00_00_cover.png",
        [
            "learning-sessions\\24_Mughal-Society-Economy-Culture_Complete-Learning-Session_2026-08-19.md",
            "learning-sessions\\24_Mughal-Society-Economy-Culture_Premium-Solved-PYQ-Workbook_2026-08-19.md",
        ],
        TOPIC_24_OFFICIAL_QUESTIONS,
    ),
    topic_config(
        25,
        "Decline of the Mughal Empire & the Eighteenth Century",
        "25_Decline-of-the-Mughal-Empire-and-the-Eighteenth-Century_Complete-Topic-Package.md",
        "25_Decline-of-the-Mughal-Empire.md",
        "25_Decline-of-the-Mughal-Empire.md",
        "25_Decline-of-the-Mughal-Empire-and-the-Eighteenth-Century_Complete-Learning-Session_2026-08-19.pdf",
        "25_Decline-of-the-Mughal-Empire-and-the-Eighteenth-Century_Premium-Solved-PYQ-Workbook_2026-08-19.pdf",
        "No fabricated direct CSE PYQ; exactly 80 independent MCQs in a "
        "strict A-B-C-D cycle and 12 examiner-grade solved Mains answers "
        "with adjacent questions labelled by their true ownership.",
        [
            "https://culture.gov.in/our-organisations/"
            "archaeological-survey-india-new-delhi",
            "https://static.pib.gov.in/WriteReadData/specificdocs/"
            "documents/2026/apr/doc2026418850901.pdf",
        ],
        "Official conservation materials were rechecked on 30 August 2026 "
        "and provide only a bounded modern bridge to preserving monuments "
        "and archives. No genuinely topic-specific recent official event "
        "was found for Mughal successor states or the 1707-1761 transition. "
        "Heritage policy is not evidence for eighteenth-century causal "
        "claims; those remain controlled by canonical Markdown, OCR books "
        "and source criticism.",
        "Mughal decline successor states invasions and continuity cover",
        "notes/Medieval-Indian-History/assets/"
        "25_Decline-of-the-Mughal-Empire-and-the-Eighteenth-Century/"
        "00_00_cover.png",
        [
            "learning-sessions\\25_Decline-of-the-Mughal-Empire-and-the-Eighteenth-Century_Complete-Learning-Session_2026-08-19.md",
            "learning-sessions\\25_Decline-of-the-Mughal-Empire-and-the-Eighteenth-Century_Premium-Solved-PYQ-Workbook_2026-08-19.md",
        ],
        [],
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "medieval-indian-history-23": [
        (
            "Western Deccan: terrain becomes a fort network",
            "spatial-system",
            """SAHYADRI RIDGE -> height, narrow passes and monsoon friction
MAVAL VALLEYS -> recruits, grain, local intelligence and short movement
KONKAN COAST -> creeks, customs, ports and access to maritime rivals
FORT NODE -> garrison + store + signal + refuge + route surveillance
NETWORK EFFECT -> inland plateau, passes and coast support one another
LIMIT -> geography enables choices; organisation converts it into power.""",
            ["Western Deccan", "Maval", "Konkan", "Fort network"],
        ),
        (
            "Chronology from the 1640s to 1707",
            "timeline",
            """1640s -> Torna, Murumbdev-Rajgad and Kondana build a Poona-Maval base
1656 -> Javli | 1659 -> Pratapgad | 1663 -> Poona raid | 1664 -> Surat
1665 -> Purandar | 1666 -> Agra rupture | 1670 -> territorial recovery
1674 -> Raigad coronation | 1680 -> Shivaji dies
1689 -> Sambhaji executed | Rajaram shifts resistance toward Jinji
1700 -> Tarabai's regency | 1707 -> Aurangzeb dies with war unresolved.""",
            ["1640s-1707", "Javli", "Purandar", "Raigad", "Tarabai"],
        ),
        (
            "Purandar, Agra and recovery",
            "cause-mechanism-effect",
            """MUGHAL PRESSURE -> Jai Singh combines siege, diplomacy and Bijapur strategy
PURANDAR 1665 -> 23 forts ceded, 12 retained; Sambhaji receives mansab 5000
INCORPORATION TEST -> service and a retained base coexist uneasily
AGRA 1666 -> rank dispute, confinement and escape destroy political trust
RECOVERY FROM 1670 -> forts and initiative return; surrender was not final
SOURCE RULE -> escape is secure; basket details remain a source version.""",
            ["Treaty of Purandar", "Agra 1666", "Recovery after 1670"],
        ),
        (
            "Coronation and the language of sovereignty",
            "legitimacy-ladder",
            """POWER ALREADY BUILT -> forts, revenue, command and negotiated authority
RAIGAD 1674 -> public claim to chhatrapati sovereignty
GAGA BHATTA -> Kshatriya genealogy addresses contested status
RITUAL EFFECT -> ruler stands above chiefs in a legible royal idiom
POLITICAL EFFECT -> household, territory and administration gain one centre
LIMIT -> coronation crowned state-building; it did not create capacity alone.""",
            ["Raigad 1674", "Chhatrapati", "Gaga Bhatta", "Kshatriya debate"],
        ),
        (
            "Ashtapradhan: eight offices, not a cabinet",
            "institution-map",
            """PESHWA -> general coordination | AMATYA / MAZUMDAR -> finance
SACHIV -> correspondence | MANTRI / WAQIA-NAVIS -> records and intelligence
SENAPATI / SAR-I-NAUBAT -> military | SUMANT / DABIR -> external affairs
NYAYADHISH -> justice | PANDITRAO -> religious grants and duties
CONTROL PRINCIPLE -> each office answers to the ruler
TRAP -> no collective responsibility, parliamentary cabinet or later Peshwa rule.""",
            ["Ashtapradhan", "Ruler-centred offices", "Cabinet trap"],
        ),
        (
            "Chauth and sardeshmukhi are distinct claims",
            "comparison-matrix",
            """CHAUTH -> one-quarter fiscal claim, often tied to protection and restraint
SARDESHMUKHI -> additional ten-percent claim in a superior-right idiom
COLLECTION -> agents bargain, coerce and overlap with existing revenue systems
POLITICAL EFFECT -> payment may acknowledge power without settled sovereignty
LOCAL EFFECT -> payer can seek relief while parallel authority becomes normal
TRAP -> neither pure plunder nor automatic lawful title explains every case.""",
            ["Chauth", "Sardeshmukhi", "Parallel fiscal authority"],
        ),
        (
            "Cavalry and ganimi kava",
            "military-system",
            """BARGIR -> horse and equipment associated with state provision
SILHEDAR -> maintains his own horse and equipment
GANIMI KAVA -> surprise + intelligence + supply attack + selective engagement
FORT ANCHOR -> stores, refuge, signals and route control sustain mobility
LOCAL KNOWLEDGE -> converts short movement into operational advantage
LIMIT -> not invincibility, a social census or modern ideological insurgency.""",
            ["Bargir", "Silhedar", "Ganimi kava", "Fort logistics"],
        ),
        (
            "Coast and navy: capability with scale limits",
            "coastal-network",
            """KONKAN -> creeks, ports, customs and sea forts connect war to commerce
RIVALS -> Sidis of Janjira, Portuguese and English shape naval choices
PEOPLE -> Koli, Bhandari, Muslim and other sailors prevent a closed identity
VESSELS -> gurab and galivat labels require source and context
CAPABILITY -> regional escort, defence, raiding and coastal communication
LIMIT -> not an oceanic blue-water navy or a licence to invent fleet numbers.""",
            ["Konkan", "Sidis", "Sea forts", "Regional navy"],
        ),
        (
            "Resistance after Shivaji",
            "succession-network",
            """SAMBHAJI 1680-89 -> leadership under pressure; execution removes a head
RAJARAM -> movement to Jinji creates strategic depth beyond Maharashtra
SANTAJI / DHANAJI -> strike communications and dispersed imperial forces
RAMCHANDRA PANT / SHANKARAJI -> administration and patronage sustain networks
TARABAI FROM 1700 -> regency supplies legitimacy and political coordination
RESULT -> decapitation changes the war into a more decentralised resistance.""",
            ["Sambhaji", "Rajaram", "Jinji", "Santaji", "Dhanaji", "Tarabai"],
        ),
        (
            "Annexation removes buffers",
            "gain-cost-balance",
            """BIJAPUR 1686 + GOLCONDA 1687 -> territory, forts and nominal revenue gained
BUFFER LOSS -> Mughals now confront mobile Maratha networks more directly
NEW CLAIMANTS -> absorbed elites add service and jagir expectations
NEW COSTS -> garrisons, siege trains, supply, policing and collection friction
REALISATION PROBLEM -> conquered jama does not guarantee usable hasil
VERDICT -> annexation enlarged the map while narrowing strategic flexibility.""",
            ["Bijapur 1686", "Golconda 1687", "Buffer removal", "Deccan costs"],
        ),
        (
            "Jagirdari terms and the feedback loop",
            "feedback-loop",
            """MANSAB -> rank and service claim | JAGIR -> transferable revenue assignment
JAMA -> assessed claim | HASIL -> realised collection
PAIBAQI -> reserve assignable pool | BE-JAGIRI -> shortage of usable assignments
WAR / INFLATED JAMA -> weak hasil -> troop and remount shortfall
HARDER EXTRACTION -> local resistance / private pacts -> further disturbance
RESULT -> fiscal, agrarian, administrative and military strain reinforce one another.""",
            ["Mansab", "Jagir", "Jama", "Hasil", "Paibaqi", "Be-jagiri"],
        ),
        (
            "Topic 23 final answer spine",
            "answer-synthesis",
            """OPEN -> ecology became power through institutions, networks and sovereignty
TRACE -> early forts -> Purandar / Agra -> recovery -> coronation
EXPLAIN -> offices + revenue + chauth claims + mobile war + bounded navy
EXTEND -> Sambhaji -> Rajaram / Jinji -> Tarabai's decentralised resistance
CONNECT -> annexation and long war intensify the jagirdari feedback loop
QUALIFY -> reject hero myth, nationalism, cabinet analogy and instant collapse.""",
            ["Answer architecture", "State-building", "Deccan war", "Jagirdari crisis"],
        ),
    ],
    "medieval-indian-history-24": [
        (
            "Layered society, not a court-peasant binary",
            "social-pyramid",
            """EMPEROR / HOUSEHOLD -> sovereignty, patronage and concentrated consumption
MANSABDARS / CHIEFS -> service rank, local power and armed followings
MERCHANTS / PROFESSIONALS -> credit, brokerage, law, medicine and records
ARTISANS / SERVICE GROUPS -> skilled and ordinary production
CULTIVATORS / LABOURERS -> unequal land, cattle, credit and customary claims
RULE -> hierarchy was real, but region, occupation and mobility varied.""",
            ["Social structure", "Hierarchy", "Mobility", "Regional variation"],
        ),
        (
            "Nobility: mansab, household and reproduction",
            "institution-household",
            """MANSAB -> appointed zat status-pay plus sawar cavalry obligation
HOUSEHOLD -> kin, clients, retainers, scribes, soldiers and dependants
COMPOSITE ELITE -> Turani, Irani, Hindustani, Rajput, Afghan and Deccani labels
FORMAL RULE -> rank is not automatically hereditary
SOCIAL FACT -> khanazad advantage, patronage and training reproduce position
TRAP -> ancestry labels do not prove every noble was foreign-born.""",
            ["Mansab", "Nobility", "Household", "Khanazad"],
        ),
        (
            "Zamindars across a spectrum",
            "scale-spectrum",
            """VILLAGE END -> locally rooted claimant with information and customary dues
MIDDLE -> armed lineage, garhi, caste-clan following and several villages
RAJA END -> substantial territorial chief incorporated or negotiated with
STATE NEED -> collection, order, settlement and local mediation
CONFLICT -> regulation, resistance and mansab incorporation can coexist
TRAP -> neither mere tax clerk nor uniform British-style landlord.""",
            ["Zamindar", "Garhi", "Local power", "Scale variation"],
        ),
        (
            "Cultivators and layered rights",
            "comparison-matrix",
            """KHUD-KASHT -> resident cultivator, often with stronger local resources
PAHI-KASHT -> incoming or non-resident cultivator, often drawn by concession
RAIYATI / MUZARIAN -> varied ordinary cultivator or tenant contexts
RIGHTS -> labour, occupancy, inheritance, revenue and customary access overlap
MEDIATORS -> patil, muqaddam, qanungo, patwari and deshmukh vary by region
TRAP -> layered claims are not simple modern private landownership.""",
            ["Khud-kasht", "Pahi-kasht", "Raiyati", "Land rights"],
        ),
        (
            "Women, work and source silence",
            "evidence-ladder",
            """WORK -> agriculture, spinning, embroidery and domestic production
ELITE EVIDENCE -> Gulbadan, Nur Jahan and Jahanara show particular agency
ARCHIVE BIAS -> court texts record elite women more readily than ordinary labour
MATERIAL / IMAGE -> can suggest practice but cannot serve as an occupation census
CONSTRAINTS -> caste, class, marriage, purdah, property and credit vary
VERDICT -> differentiated agency within a strongly unequal gender order.""",
            ["Women's work", "Gulbadan", "Nur Jahan", "Source silence"],
        ),
        (
            "Towns and the middle strata",
            "urban-network",
            """IMPERIAL CITY -> court, garrison, workshops and consumption
PORT CITY -> customs, shipping, brokers and overseas exchange
QASBA -> administration, learning, market and countryside link
PRODUCTION / PILGRIMAGE CENTRE -> specialised craft or religious demand
MIDDLE STRATA -> clerks, qazis, physicians, shopkeepers and master-craftsmen
RESULT -> urban diversity corrects Bernier's noble-versus-poor binary.""",
            ["Urban typology", "Qasba", "Middle strata", "Bernier"],
        ),
        (
            "Karkhana and craft production",
            "production-chain",
            """INPUTS -> cotton, silk, dyes, metals, stone, timber and skilled labour
KARKHANA -> imperial household store and workshop, not every private workshop
ORGANISATION -> masters, artisans, wage/service ties and quality control
PRIVATE FIELD -> household craft, merchant advance and putting-out coexist
OUTPUT -> textiles, arms, jewellery, ships, books, paintings and monuments
LIMIT -> court production cannot measure all craft labour or welfare.""",
            ["Karkhana", "Craft production", "Merchant advance", "Artisans"],
        ),
        (
            "Inland trade, hundi and banjara",
            "circulation-system",
            """ROAD / RIVER / SARAI -> movement, rest, information and state oversight
BANJARA -> bulk overland carriage, especially grain and army supply
HUNDI -> credit instrument moving value across distance and time
SARRAF -> money changing, testing and finance | BROKER -> market access
AURANG -> warehouse or depot | BANIAN -> company-linked Indian agent-broker
RESULT -> goods, credit and information connect town, port and countryside.""",
            ["Hundi", "Banjara", "Sarraf", "Aurang", "Banian"],
        ),
        (
            "Overseas trade, companies and bullion",
            "maritime-balance",
            """PORTS -> Surat / Cambay, Hugli / Balasore, Masulipatnam / Pulicat
EXPORTS -> textiles, silk, indigo, sugar, grain and saltpetre vary by region
IMPORTS -> horses, metals and luxuries; bullion helps settle trade balances
INDIAN AGENCY -> Virji Vohra, Abdul Ghaffur and merchant communities
COMPANIES -> enter existing networks while naval-coercive capacity grows
TRAP -> bullion is not welfare; company presence is not instant dominance.""",
            ["Indian Ocean", "Bullion", "Virji Vohra", "European companies"],
        ),
        (
            "Technology without stagnation or industrial teleology",
            "debate-matrix",
            """STRENGTH -> textiles, dyes, jewellery, shipbuilding and craft precision
SELECTIVE LIMIT -> pumps, furnaces, screws, optics and some machine linkages
PRINT DISTINCTION -> textile blocks, known presses and uneven institutional uptake
POSSIBLE CAUSES -> labour cost, investment choice and weak science-craft linkage
METHOD -> compare sector, institution, date and diffusion
VERDICT -> high skill with uneven adoption; neither no technology nor industry.""",
            ["Technology debate", "Printing", "Artisanal skill", "Diffusion"],
        ),
        (
            "Culture as institutional and composite production",
            "culture-map",
            """ARCHITECTURE -> Humayun's Tomb -> Fatehpur -> Taj -> Red Fort
PAINTING -> Akbar's workshop / Hamzanama -> Jahangir / Mansur -> dispersion
LITERATURE -> Persian chronicles, memoirs, malfuzat and vernacular fields
TRANSLATION -> Razmnama; Nizamuddin Panipati's Yogavasistha under Akbar
DARA -> Majma-ul-Bahrain and Sirr-i-Akbar are distinct works
QUALIFY -> cultural interaction did not erase caste, gender or coercion.""",
            ["Architecture", "Painting", "Translation", "Composite culture"],
        ),
        (
            "Topic 24 final answer spine",
            "answer-synthesis",
            """OPEN -> productive and connected, yet hierarchical and regionally uneven
SOCIETY -> mansab household + zamindar spectrum + layered cultivator rights
ECONOMY -> agrarian surplus -> towns / craft -> credit -> inland / ocean trade
CULTURE -> patronage and workshops convert resources into material forms
METHOD -> named source or monument -> claim -> reach -> silence / limitation
CLOSE -> dynamism was real; prosperity, equality and industrialisation were not universal.""",
            ["Answer architecture", "Society", "Economy", "Culture", "Source method"],
        ),
    ],
    "medieval-indian-history-25": [
        (
            "Chronology, 1707-1761",
            "timeline",
            """1707 -> Aurangzeb dies; contested succession opens the core period
1712-13 -> Jahandar falls; Farrukhsiyar rises with Sayyid support
1719 -> Farrukhsiyar deposed; repeated enthronements expose kingmaking
1720 -> Sayyids fall | 1724 -> Nizam establishes Deccan autonomy
1739 -> Nadir Shah defeats the Mughals and sacks Delhi
1748-61 -> Abdali invasions | 14 Jan 1761 -> Third Battle of Panipat.""",
            ["1707-1761", "Sayyid Brothers", "Nadir Shah", "Panipat"],
        ),
        (
            "Decline as a converging system",
            "systems-map",
            """POLITICAL -> succession conflict + wizarat competition + noble factions
FISCAL -> jagir scarcity + jama-hasil gap + short-term extraction
AGRARIAN -> zamindar resistance, peasant flight and uneven collection
MILITARY -> Deccan exhaustion, weak contingents and frontier shocks
REGIONAL -> provincial governors convert office into durable autonomy
RULE -> no strand alone explains timing, reach or continuity.""",
            ["Causation map", "Political", "Fiscal", "Agrarian", "Military"],
        ),
        (
            "Succession and the Sayyid wizarat",
            "actor-timeline",
            """BAHADUR SHAH I -> wins the 1707 succession but settles no firm rule
JAHANDAR SHAH -> Zulfiqar Khan's patronage shows wazir-centred leverage
FARRUKHSIYAR 1713 -> throne secured through the Sayyid Brothers
1719 -> the same coalition deposes and kills him
ABDULLAH / HUSSAIN ALI -> office, army and patronage sustain kingmaking
1720 -> rival nobles remove them; factional rule outlives the episode.""",
            ["Bahadur Shah I", "Farrukhsiyar", "Sayyid Brothers", "Wizarat"],
        ),
        (
            "Four jagirdari terms",
            "comparison-matrix",
            """JAMA -> assessed or estimated revenue claim on paper
HASIL -> revenue actually realised after control, harvest and collection
PAIBAQI -> reserve pool available for assignment
BE-JAGIRI -> shortage of sufficiently productive and usable jagirs
MEASUREMENT -> a high jama can conceal a weak hasil
TRAP -> jagir is a transferable revenue assignment, not private ownership.""",
            ["Jama", "Hasil", "Paibaqi", "Be-jagiri", "Jagir"],
        ),
        (
            "The jagirdari feedback loop",
            "feedback-loop",
            """MORE CLAIMANTS / WEAK PAIBAQI -> pressure for productive assignments
SHORT TENURE / POOR JAGIR -> assignee seeks rapid extraction
LOCAL PRESSURE -> zamindar resistance, evasion, debt, flight or negotiation
LOWER HASIL -> contingent maintenance and imperial service weaken
MILITARY FAILURE / DISTURBANCE -> collection becomes still harder
RESULT -> fiscal, agrarian and political strain reproduces itself.""",
            ["Jagirdari crisis", "Extraction", "Zamindar resistance", "Contingents"],
        ),
        (
            "The inherited Deccan burden",
            "legacy-chain",
            """1686-87 ANNEXATIONS -> more territory, forts, elites and paper revenue
1687-1707 WAR -> siege, transport, garrison and remount costs accumulate
BUFFER REMOVAL -> direct conflict with dispersed Maratha networks expands
DISTURBED DISTRICTS -> assessed jama outruns reliable hasil
POST-1707 INHERITANCE -> claimant pressure and military obligations remain
VERDICT -> Deccan war is a legacy mechanism, not the whole decline story.""",
            ["Deccan legacy", "Annexation", "Maratha war", "Jama-hasil gap"],
        ),
        (
            "From centre to region: a spectrum",
            "authority-spectrum",
            """DIRECT CENTRE -> appointment, revenue order and military command from Delhi
NEGOTIATED PROVINCE -> governor and local elites bargain within imperial forms
DE FACTO AUTONOMY -> provincial ruler controls revenue, army and succession
FORMAL DEFERENCE -> title, coin, khutba or confirmation may still invoke emperor
LOCAL POWER -> zamindars and chiefs can cooperate, resist or become state-builders
TRAP -> autonomy is a process; it is not one simultaneous declaration.""",
            ["Centre-region spectrum", "Autonomy", "Imperial legitimacy"],
        ),
        (
            "Bengal, Awadh and Hyderabad compared",
            "comparison-matrix",
            """BENGAL -> Murshid Quli Khan stabilises revenue and limits jagir disruption
AWADH -> Saadat Khan builds through accommodation with zamindars and taluqdars
HYDERABAD -> Nizam-ul-Mulk converts subedari and military power after 1724
SHARED -> revenue, army and patronage become regionally controlled
SHARED -> Mughal titles and symbolic legitimacy often remain useful
DIFFERENCE -> fiscal settlement, local alliance and military conversion vary.""",
            ["Bengal", "Awadh", "Hyderabad", "Successor states"],
        ),
        (
            "Jats, Sikhs and Marathas: bounded snapshot",
            "regional-snapshot",
            """JATS -> agrarian-zamindari power consolidates around Bharatpur
SIKHS -> Khalsa, misls and armed community formation reshape Punjab politics
MARATHAS -> chauth claims and confederate expansion reach Malwa and the north
COMMON -> imperial weakening opens space, but each route has distinct institutions
BOUNDARY -> Shivaji's state detail belongs to Topic 23
BOUNDARY -> later confederacy and Company wars require their proper owners.""",
            ["Jats", "Sikhs", "Marathas", "Regional powers", "Topic boundary"],
        ),
        (
            "Nadir Shah, Abdali and Panipat",
            "shock-sequence",
            """NADIR SHAH 1739 -> Karnal defeat exposes weakness; Delhi loses treasure
EFFECT -> severe fiscal and prestige shock accelerates an older crisis
ABDALI 1748-61 -> repeated invasions keep the northwest under pressure
PANIPAT 1761 -> Abdali coalition defeats Sadashivrao Bhau's Maratha force
LIMIT -> Panipat checks northern expansion but does not end Maratha power
TRAP -> neither 1739 nor 1761 alone makes later British rule inevitable.""",
            ["Nadir Shah", "Abdali", "Karnal", "Third Battle of Panipat"],
        ),
        (
            "Regional economic and cultural continuity",
            "continuity-map",
            """POLITICAL CENTRE CONTRACTS -> patronage and resources shift regionally
BANKERS / CREDIT -> houses such as Jagat Seth remain influential
TRADE / CRAFT -> routes and production persist unevenly across regions
AWADH / HYDERABAD / BENGAL -> courts support art, literature and architecture
QUALIFY -> warfare, extraction and local losses remain real
VERDICT -> regional reorganisation, not uniform economic-cultural collapse.""",
            ["Economic continuity", "Jagat Seth", "Regional patronage"],
        ),
        (
            "Non-inevitability and final answer spine",
            "answer-synthesis",
            """OPEN -> decline is devolution and converging strain, not instant disappearance
TRACE -> succession -> jagirdari loop -> regional autonomy -> external shocks
COMPARE -> Bengal / Awadh / Hyderabad by distinct mechanism
BALANCE -> political fragmentation with economic-cultural continuity
REJECT -> ruler-only blame, one-cause crisis and automatic colonial succession
CLOSE -> 1707-61 created opportunities; later outcomes remained contingent.""",
            ["Non-inevitability", "Answer architecture", "Qualified verdict"],
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


def normalize_register_fragment(fragment: str) -> str:
    lines = [
        line[4:] if line.startswith("    ") else line
        for line in fragment.splitlines()
    ]
    seen_h2 = False
    for index, line in enumerate(lines):
        if not re.match(r"^##(?!#)\s+", line):
            continue
        if seen_h2:
            lines[index] = "#" + line
        else:
            seen_h2 = True
    return "\n".join(lines)


def omit_mcq_blocks(fragment: str, omitted: set[int]) -> str:
    matches = list(re.finditer(r"(?m)^### Q(\d+)\.", fragment))
    if not matches:
        raise ValueError("MCQ fragment has no question headings.")
    output = [fragment[: matches[0].start()]]
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(fragment)
        if int(match.group(1)) not in omitted:
            output.append(fragment[match.start() : end])
    return "".join(output).rstrip()


def renumber_mcq_headings(fragment: str, offset: int) -> str:
    return re.sub(
        r"(?m)^### Q(\d+)\.",
        lambda match: f"### Q{int(match.group(1)) + offset}.",
        fragment,
    )


def enforce_mcq_cycle(fragment: str) -> str:
    matches = list(re.finditer(r"(?m)^### Q(\d+)\.", fragment))
    if not matches:
        raise ValueError("MCQ fragment has no question headings.")
    output = [fragment[: matches[0].start()]]
    letters = "ABCD"
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(fragment)
        block = fragment[match.start() : end]
        question_number = int(match.group(1))
        target = letters[(question_number - 1) % 4]
        answer = re.search(
            r"(?mi)^\*\*Answer:\s*([A-D])(?:[.\s]+.*?)?\*\*\s*$",
            block,
        )
        options = list(re.finditer(r"(?m)^([A-D])\.\s+(.+?)\s*$", block))
        if answer is None or len(options) != 4:
            raise ValueError(f"Cannot rotate MCQ Q{question_number}.")
        current = answer.group(1).upper()
        option_text = {item.group(1): item.group(2) for item in options}
        if current != target:
            option_text[current], option_text[target] = (
                option_text[target],
                option_text[current],
            )
            block = re.sub(
                r"(?m)^([A-D])\.\s+(.+?)\s*$",
                lambda item: f"{item.group(1)}. {option_text[item.group(1)]}",
                block,
            )
        block = re.sub(
            r"(?mi)^\*\*Answer:\s*([A-D])(?:[.\s]+.*?)?\*\*\s*$",
            f"**Answer: {target}.**",
            block,
            count=1,
        )
        output.append(block)
    return "".join(output).rstrip()


def topic_24_remedial_fragment() -> str:
    return """## Remedial MCQ bank (8; application-based, keys A-B-C-D x2)

These questions repair common reasoning errors without repeating the learning loop.

### Q73. A pargana has a high assessed jama, but warfare and resistance sharply reduce actual collection. What is the safest inference?

A. The jama-hasil gap is wide, so the paper assessment cannot be treated as realised resources.

B. The high jama proves universal rural prosperity.

C. The jagirdar privately owns the pargana.

D. Monetisation has eliminated payment in kind.

**Answer: A.**
**Explanation:** Jama is the assessed claim, while hasil is realised collection. A large gap warns against converting an administrative estimate into evidence of output, welfare or usable state income.

### Q74. A court painting depicts women spinning and preparing textiles. How should it be used?

A. As a complete occupational census for all Mughal women.

B. As evidence of possible gendered work, checked against textual and material sources and differentiated by class and region.

C. As proof that elite and non-elite women enjoyed equal autonomy.

D. As proof that domestic production had disappeared.

**Answer: B.**
**Explanation:** The image can support a bounded claim about work, but genre, patronage and social visibility limit representativeness. Corroboration prevents an illustrative scene from becoming a universal statistic.

### Q75. A present-day conservation page describes the Taj Mahal's craftsmanship and material setting. Which historical use is methodologically valid?

A. It proves that every Mughal artisan was prosperous.

B. It establishes the empire's exact share of world GDP.

C. It supports bounded discussion of surviving techniques, materials and patronage, not universal social or economic conclusions.

D. It demonstrates private ownership of all cultivated land.

**Answer: C.**
**Explanation:** Heritage records are useful for the surviving monument and its material features. They do not measure empire-wide wages, equality, output or property relations.

### Q76. Large textile exports and bullion inflows are best combined with which conclusion?

A. Every region experienced identical commercial growth.

B. Bullion inflow automatically raised real wages for all groups.

C. European companies already controlled the entire Indian economy.

D. Commercial dynamism could coexist with hierarchy, uneven bargaining power and regional variation.

**Answer: D.**
**Explanation:** Trade indicators establish circulation and demand, not equal distribution. A strong answer keeps commercial expansion separate from universal welfare.

### Q77. Which pairing correctly distinguishes Dara Shukoh's two works?

A. Majma-ul-Bahrain compared mystical traditions; Sirr-i-Akbar was associated with Persian translations of the Upanishads.

B. Majma-ul-Bahrain was the Persian Yogavasistha; Sirr-i-Akbar was Akbar's revenue manual.

C. Both titles refer to the same illustrated manuscript.

D. Both were composed by Nizamuddin Panipati.

**Answer: A.**
**Explanation:** The titles belong to distinct intellectual projects. Conflating them also obscures Nizamuddin Panipati's separate Yogavasistha translation under Akbar.

### Q78. Which statement best separates imperial karkhanas from the wider craft economy?

A. Karkhanas were the only sites of production in the empire.

B. They were court-linked stores and workshops within a larger field of household, market and merchant-organised production.

C. They consisted entirely of unpaid agricultural labour.

D. Their records provide a complete measure of all artisan welfare.

**Answer: B.**
**Explanation:** Imperial workshops mattered for court consumption and specialised production, but private workshops, household manufacture and merchant advances also organised craft labour.

### Q79. What analytical link between banjaras and hundis is strongest?

A. Both were hereditary Mughal ranks.

B. Both were forms of monumental patronage.

C. Banjaras moved bulk goods while hundis helped move credit and value, jointly linking distant markets.

D. Both made roads, rivers and brokers unnecessary.

**Answer: C.**
**Explanation:** Physical carriage and financial instruments solved different circulation problems. Their interaction is more informative than treating either as the whole trade system.

### Q80. Why should a Persian chronicle be said to reflect and refract the spirit of its age?

A. It records every social group in equal detail.

B. Court patronage makes all its claims false.

C. Its literary form has no bearing on historical use.

D. It reveals institutions and values through a genre, patron and audience that also shape silences and emphasis.

**Answer: D.**
**Explanation:** A source can preserve real evidence while selecting and framing it. Genre and patronage require corroboration, not wholesale acceptance or rejection.
"""


def canonical_sections(
    config_value: dict[str, object],
) -> tuple[str, list[tuple[str, str]]]:
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
    if str(config_value["key"]) == "medieval-indian-history-24":
        source = re.sub(
            r"(?m)^# Mughal Society, Economy & Culture - MUST-DO$",
            "## SOURCE DOSSIER - BASIC OWNER",
            source,
        )
        source = re.sub(
            r"(?m)^# Mughal Society, Economy & Culture - ADVANCED$",
            "## SOURCE DOSSIER - ADVANCED OWNER",
            source,
        )
    preamble, sections = BASE.split_h2(source)
    preamble = BASE.strip_title(preamble)
    cover = f"![{config_value['cover_alt']}]({config_value['cover_path']})"
    return "\n\n".join([cover, preamble]), sections


def assemble_topic_23(config_value: dict[str, object]) -> str:
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
        elif title.startswith("PART IX "):
            mode = "practice"
            bucket = "practice"
        elif title.startswith("PART "):
            mode = "basic"
            bucket = "basic"
        elif re.match(r"^\d+\.", title):
            bucket = "basic"
        elif title.startswith("Transparent PYQ audit"):
            bucket = "practice"
        elif title.startswith(
            (
                "Advanced evidence notebook",
                "Evidence and answer-writing drills",
            )
        ):
            bucket = "advanced"
        elif title.startswith(("Learning MCQ", "Broad MCQ", "Remedial MCQ")):
            bucket = "mcq"
            if title.startswith("Broad MCQ"):
                fragment = omit_mcq_blocks(fragment, {65})
            elif title.startswith("Remedial MCQ"):
                fragment = renumber_mcq_headings(fragment, -1)
            fragment = enforce_mcq_cycle(fragment)
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Examiner-grade solved Mains"):
            bucket = "practice"
        else:
            bucket = mode
        if bucket == "register":
            fragment = normalize_register_fragment(fragment)
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def consolidate_topic_24_foundation(markdown: str) -> str:
    start_marker = "### Authored foundation dossier (source-order first)"
    end_marker = "### PART I - Guided teaching: core to advanced"
    start = markdown.index(start_marker)
    end = markdown.index(end_marker, start)
    foundation = markdown[start:end]
    lines = foundation.splitlines()
    for index, line in enumerate(lines):
        if index == 0:
            lines[index] = (
                "### Foundation dossier: society, economy, culture "
                "and answer architecture"
            )
        elif re.match(r"^###(?!#)\s+", line):
            lines[index] = "#" + line
    return markdown[:start] + "\n".join(lines).rstrip() + "\n\n" + markdown[end:]


def assemble_topic_24(config_value: dict[str, object]) -> str:
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
        if title.startswith("Roadmap and evidence contract"):
            preamble_parts.append(HELPERS.normalized_fragment(fragment))
            continue
        if register_mode:
            bucket = "register"
        elif title.startswith("Final consolidated register notes"):
            register_mode = True
            bucket = "register"
        elif title == "SOURCE DOSSIER - BASIC OWNER":
            mode = "basic"
            bucket = "basic"
            fragment = re.sub(
                r"(?m)^## SOURCE DOSSIER - BASIC OWNER\s*$",
                "## Foundation dossier: society, economy, culture and answer architecture",
                fragment,
                count=1,
            )
            fragment = re.sub(r"(?m)^###(?!#)\s+", "#### ", fragment)
        elif title == "SOURCE DOSSIER - ADVANCED OWNER":
            mode = "advanced"
            bucket = "advanced"
        elif title.startswith("PART I "):
            mode = "basic"
            bucket = "basic"
        elif title.startswith("PART II "):
            mode = "practice"
            bucket = "practice"
        elif title.startswith("PART III "):
            mode = "mcq"
            bucket = "mcq"
        elif title.startswith(
            (
                "Deep evidence-to-answer labs",
                "Comparative evidence cards",
                "Sources and historiography synthesis",
                "Visual synthesis atlas",
                "Terminology and claim-verification clinic",
            )
        ):
            bucket = "advanced"
        elif title.startswith("Exact routed UPSC PYQs"):
            bucket = "practice"
        elif title.startswith(
            (
                "Learning MCQ loop",
                "Broad MCQ bank",
                "Remedial MCQ bank",
            )
        ):
            bucket = "mcq"
            if title.startswith("Remedial MCQ bank"):
                fragment = topic_24_remedial_fragment()
            fragment = enforce_mcq_cycle(fragment)
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Twelve examiner-grade solved Mains"):
            bucket = "practice"
        else:
            bucket = mode
        if bucket == "register":
            fragment = normalize_register_fragment(fragment)
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    markdown = HELPERS.compose(
        config_value,
        "\n\n".join(preamble_parts),
        grouped,
    )
    return consolidate_topic_24_foundation(markdown)


def assemble_topic_25(config_value: dict[str, object]) -> str:
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
        elif title.startswith("PART X "):
            mode = "practice"
            bucket = "practice"
        elif title.startswith("PART "):
            mode = "basic"
            bucket = "basic"
        elif re.match(r"^\d+\.", title):
            bucket = "basic"
        elif title.startswith("Transparent PYQ audit"):
            bucket = "practice"
        elif title.startswith(
            (
                "Advanced evidence notebook",
                "Evidence and answer-writing drills",
            )
        ):
            bucket = "advanced"
        elif title.startswith(("Learning MCQ", "Broad MCQ", "Remedial MCQ")):
            bucket = "mcq"
            fragment = enforce_mcq_cycle(fragment)
            fragment = normalize_mcq_fragment(fragment)
        elif title.startswith("Examiner-grade solved Mains"):
            bucket = "practice"
        else:
            bucket = mode
        if bucket == "register":
            fragment = normalize_register_fragment(fragment)
        grouped[bucket].append(HELPERS.normalized_fragment(fragment))
    return HELPERS.compose(config_value, "\n\n".join(preamble_parts), grouped)


def validate_mcq_profile(markdown: str, key: str) -> None:
    match = re.search(
        r"(?ms)^## BASIC MCQS / REMEDIATION\s*$"
        r"(.*?)"
        r"^## PYQS AND ANSWER PRACTICE\s*$",
        markdown,
    )
    if match is None:
        raise ValueError(f"{key}: assembled MCQ section not found.")
    answers = re.findall(
        r"(?mi)^\*\*Answer:\s*([A-D])\.\*\*\s*$",
        match.group(1),
    )
    expected = list("ABCD" * 20)
    if answers != expected:
        counts = {letter: answers.count(letter) for letter in "ABCD"}
        raise ValueError(
            f"{key}: expected 80 strict-cycle MCQs, found "
            f"{len(answers)} with {counts}."
        )
    questions = re.findall(
        r"(?m)^#{3,4} Q\d+\.\s+(.+?)\s*$",
        match.group(1),
    )
    normalized = [" ".join(question.casefold().split()) for question in questions]
    if len(questions) != 80 or len(set(normalized)) != 80:
        raise ValueError(
            f"{key}: expected 80 independently worded MCQs, found "
            f"{len(questions)} headings and {len(set(normalized))} unique stems."
        )


def assemble(config_value: dict[str, object]) -> str:
    key = str(config_value["key"])
    if key == "medieval-indian-history-23":
        markdown = assemble_topic_23(config_value)
    elif key == "medieval-indian-history-24":
        markdown = assemble_topic_24(config_value)
    else:
        markdown = assemble_topic_25(config_value)
    validate_mcq_profile(markdown, key)
    return markdown


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
        "scope": "Medieval Indian History learner-v2 Topics 23-25",
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
