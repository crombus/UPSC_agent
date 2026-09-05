"""Assemble Ancient History learner-v2 Topics 17-21 and authored visual specs."""

from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path
from typing import Callable

import carvaka_flowchart


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-29"
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
ASCII_PATH = ASCII_DIR / "ancient-indian-history-17-21-2026-08-29-sequential.json"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "ancient-indian-history--subject-wide-syllabus.json"
)
CATALOG = ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
RS_SHARMA = ROOT / "books" / "India Ancient Past By RS Sharma.pdf"
UPINDER = (
    ROOT
    / "books"
    / "1118Singh, Upinder. _A History of Ancient and Early Medieval India, "
    "2nd Ed. [Easy Reading]_-1.pdf"
)
SINGHANIA = ROOT / "books" / "Nitin Singhania's Indian Art and Culture.pdf"

COMMON_CROSS = [
    "upsc-ai-kit\\knowledge\\Ancient-Indian-History\\00_Master-Chronology.md",
    "upsc-ai-kit\\knowledge\\Ancient-Indian-History\\README.md",
    "upsc-ai-kit\\knowledge\\Ancient-Indian-History\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    "upsc-ai-kit\\knowledge\\Ancient-Indian-History\\ANSWER-WORTHINESS-AUDIT.md",
    "upsc-ai-kit\\knowledge\\Ancient-Indian-History\\REVISION-CHART_Ages-Eras-and-Distinctive-Features.md",
]
PYQ_INDEXES = [
    "upsc-ai-kit\\knowledge\\_PYQ-INDEX.md",
    "upsc-ai-kit\\knowledge\\PYQ-INTEGRATION-AUDIT-2018-2023.md",
    "upsc-ai-kit\\knowledge\\PYQ-INTEGRATION-AUDIT-2024-2025.md",
    "upsc-ai-kit\\knowledge\\PYQ-INTEGRATION-AUDIT-2026.md",
]


def config(
    number: int,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    legacy_date: str,
    practice_profile: str,
    live_sources: list[str],
    current_note: str,
) -> dict[str, object]:
    key = f"ancient-indian-history-{number:02d}"
    return {
        "number": number,
        "key": key,
        "title": title,
        "canonical": KNOWLEDGE / canonical,
        "basic": KNOWLEDGE / "basic" / basic,
        "advanced": KNOWLEDGE / "advanced" / advanced,
        "legacy_main": ROOT
        / "notes"
        / "Ancient-Indian-History"
        / f"{canonical.removesuffix('.md')}_{legacy_date}.pdf",
        "legacy_workbook": ROOT
        / "notes"
        / "Ancient-Indian-History"
        / f"{canonical.removesuffix('_Complete-Topic-Package.md')}_Solved-Workbook_{legacy_date}.pdf",
        "practice_profile": practice_profile,
        "live_sources": live_sources,
        "current_note": current_note,
    }


TOPICS = [
    config(
        17,
        "The Satavahanas & the Deccan",
        "17_Satavahanas-Deccan_Complete-Topic-Package.md",
        "17_Satavahanas-and-the-Deccan.md",
        "17_Satavahanas-and-the-Deccan.md",
        "2026-08-13",
        "4 verified/routed PYQs; 48 hard and 12 remedial MCQs; 9 original solved Mains questions.",
        [
            "https://asi.nic.in/pages/Amaravati-Circle",
            "https://asi.nic.in/pdf/CPM_List.pdf",
            "https://culture.gov.in/ministry/our-groups/archaeology",
        ],
        "ASI and Ministry of Culture heritage gateways were rechecked on 29 August 2026. "
        "They are used only for present conservation context, not Satavahana chronology.",
    ),
    config(
        18,
        "The Sangam Age & the Deep South",
        "18_Sangam-Age-Deep-South_Complete-Topic-Package.md",
        "18_Sangam-Age-Deep-South.md",
        "18_Sangam-Age-Deep-South.md",
        "2026-08-14",
        "4 verified Prelims PYQs; 52 learning/workbook MCQs; 9 original solved Mains questions.",
        [
            "https://asi.nic.in/",
            "https://culture.gov.in/ministry/our-groups/archaeology",
        ],
        "A live search on 29 August 2026 found no sufficiently specific official Sangam-age "
        "update to force into the teaching. Heritage links remain bounded method anchors.",
    ),
    config(
        19,
        "Crafts, Commerce & Urban Growth (200 BC–AD 250)",
        "19_Crafts-Commerce-Urban-Growth_Complete-Topic-Package.md",
        "19_Crafts-Commerce-Urban-Growth.md",
        "19_Crafts-Commerce-Urban-Growth.md",
        "2026-08-14",
        "4 routed Prelims PYQs; 56 learning/workbook MCQs; 9 original solved Mains questions.",
        [
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2288292&reg=48&lang=1",
            "https://culture.gov.in/ministry/our-groups/archaeology",
        ],
        "The 2026 heritage-policy search was used only to connect archaeological-site "
        "preservation with evidence recovery; no ancient trade statistic is inferred.",
    ),
    config(
        20,
        "The Gupta Empire",
        "20_Gupta-Empire_Complete-Topic-Package.md",
        "20_Gupta-Empire.md",
        "20_Gupta-Empire.md",
        "2026-08-14",
        "6 verified/routed PYQs; 32 broad and 8 remedial MCQs; 6 original solved Mains questions.",
        [
            "https://whc.unesco.org/en/tentativelists/6805/",
            "https://culture.gov.in/ministry/our-groups/archaeology",
        ],
        "UNESCO's serial tentative listing of Gupta temples was rechecked on 29 August "
        "2026 and is used only for heritage attribution and conservation linkage.",
    ),
    config(
        21,
        "Life & Culture in the Gupta Age",
        "21_Life-Culture-Gupta-Age_Complete-Topic-Package.md",
        "21_Life-and-Culture-in-Gupta-Age.md",
        "21_Life-and-Culture-in-Gupta-Age.md",
        "2026-08-14",
        "5 verified/routed PYQs; 64 objective MCQs plus 8 remedial corrections; 6 original solved Mains questions.",
        [
            "https://whc.unesco.org/en/tentativelists/6805/",
            "https://culture.gov.in/events/ministry-culture-showcases-confluence-heritage-and-technology-india-ai-impact-summit-2026",
        ],
        "The UNESCO Gupta-temple listing and Ministry of Culture Gyan Bharatam update "
        "were rechecked on 29 August 2026 for bounded heritage and manuscript linkages.",
    ),
]


PANEL_DATA: dict[str, list[tuple[str, str, str, list[str]]]] = {
    "ancient-indian-history-17": [
        ("Deccan network polity and route frame", "root-branch", """SATAVAHANA POWER
      |-- plateau agrarian zones + Godavari-Krishna corridors
      |-- Naneghat and western passes -> Konkan ports
      |-- aharas and royal officers -> local administration
      |-- maharathis / mahabhojas -> negotiated regional authority
      `-- merchants + Brahmanas + Buddhist institutions -> legitimacy
VERDICT: a strong but uneven network polity, not uniform peninsular bureaucracy.""", ["Scope", "Deccan geography"]),
        ("Evidence hierarchy and chronology", "evidence-chain", """PURANIC LISTS -> genealogy and broad sequence -> redaction limits
INSCRIPTIONS -> rulers, donors, offices and claims -> prashasti limits
COINS -> names, metals, overstrikes and circulation -> borders remain uncertain
ARCHAEOLOGY -> towns, caves, stupas and crafts -> attribution varies
CLASSICAL TEXTS -> routes and commodities -> external perspective
METHOD: converge sources; use ranges rather than one exact dynastic chronology.""", ["Sources", "Chronology debates"]),
        ("Early rulers, Satakarni and Naneghat", "timeline", """SIMUKA -> conventional founder; date and first core debated
KANHA -> early western Deccan inscriptional presence
SATAKARNI I + NAGANIKA
      |-- Naneghat genealogy and portrait memory
      |-- Vedic sacrifices and royal status claims
      `-- route-pass location converts mobility into political display
CAUTION: ritual language and portraits prove claims, not complete territorial maps.""", ["Simuka and Kanha", "Naneghat"]),
        ("Multi-centred political geography", "spatial-timeline", """PRATISHTHANA / PAITHAN -> western-central dynastic anchor
NASHIK / JUNNAR / NANEghat -> passes, caves, donors and conflict zone
TAGARA / TER -> inland market network
KRISHNA-GODAVARI -> Dharanikota-Amaravati and eastern centres
LOCAL CORES SHIFT ACROSS REIGNS AND RIVALRIES
RULE: capitals and coin finds identify nodes; they do not prove equal direct control.""", ["Political geography", "Capitals"]),
        ("Administration and local elites", "layered-governance", """KING / MOBILE COURT
      |-- ahara territorial units
      |-- amatya, mahamatra and mahasenapati offices
      |-- revenue, grants, warfare and route protection
      |-- maharathi / mahabhoja / local ruling families
      `-- village, guild, monastery and donor networks
RESULT: royal capacity worked through layered authority and local intermediaries.""", ["Administration", "Local elites"]),
        ("Kshatrapa conflict and Gautamiputra", "cause-mechanism-effect", """WESTERN PORTS + PASSES + MALWA-DECCAN ROUTES
                 |
SATAVAHANA <-> WESTERN KSHATRAPA RIVALRY
                 |
Nahapana expansion -> Gautamiputra counter-expansion
                 |
Nashik prashasti: royal victory and social-ideological claims
LIMIT: Gautami Balashri's eulogy must be checked against coins and regional evidence.""", ["Kshatrapa conflict", "Gautamiputra Satakarni"]),
        ("Nahapana overstrikes as evidence", "evidence-chain", """NAHAPANA SILVER COINS
          |
GAUTAMIPUTRA OVERSTRIKES
          |
secure sequence of displacement / metal reuse in a conflict context
          |
supports restoration of authority in selected western zones
DOES NOT PROVE: one-day conquest, total destruction or unchanged borders afterward.""", ["Nahapana overstrikes", "Numismatic method"]),
        ("Agrarian expansion and land grants", "process", """IRON + CLEARANCE + PADDY / COTTON + WATER MANAGEMENT
                         |
              expanding agrarian production
                         |
royal grants -> rights, exemptions and religious beneficiaries
                         |
new settlements + fiscal reallocation + local authority
DEBATE: grants aided expansion and legitimation; effects differed by place and date.""", ["Agrarian base", "Land grants"]),
        ("Crafts, guilds, towns and trade", "network-map", """VILLAGE RAW MATERIALS -> CRAFT CLUSTERS -> INLAND TOWNS
      |                    |                 |
 cotton / metal         guild bodies      Paithan / Tagara
      |                    |                 |
      `------------ passes and markets ----------->
                         western/eastern ports
EVIDENCE: cave donors, deposits, coins, Periplus and excavated settlements.
LIMIT: connectivity was extensive but neither uniform nor wholly state-controlled.""", ["Crafts and guilds", "Trade"]),
        ("Society, matronymics and women", "comparison", """VARNA IDEOLOGY -> royal claims and Brahmanical legitimation
SOCIAL PRACTICE -> merchants, artisans, cultivators and local elites
MATRONYMICS -> Gautamiputra, Vasisthiputra and lineage identification
ROYAL WOMEN -> Naganika and Gautami Balashri as inscriptional actors
DONOR WOMEN -> visible in cave and religious patronage
VERDICT: female agency was real but operated within unequal patriarchal structures.""", ["Society", "Matronymics and women"]),
        ("Religion, language, caves and Amaravati", "cultural-ecosystem", """BRAHMANICAL RITES + Prakrit royal inscriptions
BUDDHIST CAVES -> Nashik, Karla and Junnar donor-route landscapes
AMARAVATI -> long stupa, sculpture and patronage sequence
MERCHANTS + ARTISANS + WOMEN + RULERS -> plural donor field
GATHA SATTASAI tradition -> literary memory with attribution cautions
RULE: plural patronage joined belief, legitimacy, routes and social visibility.""", ["Religion", "Language and art"]),
        ("Decline, legacy and answer spine", "answer-synthesis", """LATER RULERS + REGIONAL SUCCESSORS + SHIFTING ROUTES
                         |
      contraction and fragmentation, not instant disappearance
                         |
LEGACIES: Deccan state forms, grants, Prakrit epigraphy, caves and trade nodes
WRITE: thesis -> chronology/source -> polity -> economy -> society/culture
      -> one debate -> graded verdict
FINAL: integration was durable, but sovereignty and prosperity remained uneven.""", ["Decline", "Historiography and answer architecture"]),
    ],
    "ancient-indian-history-18": [
        ("Tamilakam geography and tinai", "spatial-map", """VENKATAM / TIRUPATI HILLS -> conventional northern marker
WESTERN UPLANDS -> Chera-linked pepper and coast
KAVERI-MARUTAM -> wet agriculture, Uraiyur and Puhar
MADURAI-KORKAI -> Pandya court, pearls and southern coast
TINAI: kurinji | mullai | marutam | neital | palai
RULE: tinai is a poetic-ecological model, not a fixed revenue or cadastral map.""", ["Tamilakam geography", "Tinai"]),
        ("Evidence and chronology architecture", "evidence-chain", """MEGALITHIC / IRON-AGE BACKGROUND
        -> Ashokan southern-polity references
        -> Tamil-Brahmi names, donors and offices
        -> early historic poems, coins, ports and ceramics
        -> later anthology and redaction
METHOD: poem + inscription + archaeology + external text
LIMIT: c. 300 BCE-300 CE is a broad evidentiary horizon, not one synchronized reign.""", ["Chronology", "Sources"]),
        ("Sangam corpus: akam and puram", "comparison", """ETTUTTOKAI + PATTUPPATTU + TOLKAPPIYAM
AKAM                         PURAM
interior / love              public / war / gift / fame
landscape convention         chief, bard and heroic ethic
social and emotional codes   political-redistributive values
USE: recover vocabulary and institutions.
LIMIT: genre and later compilation prevent literal chronicle reading.""", ["Sangam corpus", "Genre"]),
        ("Chera, Chola and Pandya comparison", "comparison", """CHERA -> western routes / pepper / Muchiri / Senguttuvan
CHOLA -> Kaveri basin / Uraiyur / Puhar / Karikala
PANDYA -> Madurai / Korkai / pearls / Nedunjeliyan
MUVENDAR = three crowned lineages in literary memory
BOUNDARY: named rulers and places do not yield fixed continuous borders.
TRAP: Sangam Cholas are not the later imperial Cholas.""", ["Muvendar", "Dynasties"]),
        ("Chiefship, warfare, gift and fame", "cause-mechanism-effect", """AGRARIAN / PASTORAL / COASTAL RESOURCES
                  |
raids + warfare + tribute / booty
                  |
court feast and gifts -> followers + bards + dependants
                  |
praise, honour and heroic memory -> renewed legitimacy
VATTakirutal: defeated ruler's ritual fasting in the heroic code.
LIMIT: celebratory poems mute producer costs and coercion.""", ["Polity", "Warrior redistribution"]),
        ("Production and internal exchange", "process", """ECOLOGICAL ZONES
  |-- paddy and wet cultivation
  |-- cattle and pastoral products
  |-- fish, salt, pearls, pepper and forest goods
  `-- weaving, beads, shell, iron and other crafts
                         |
markets + chattu caravans + river/coastal movement
RESULT: diversified local production underpinned courts and overseas exchange.""", ["Economy", "Crafts"]),
        ("Port and hinterland network", "network-map", """HINTERLAND PRODUCTION -> MARKET / CARAVAN -> PORT
KAVERI BASIN --------------------------------------> PUHAR
PANDYA SOUTH / PEARL ZONE ------------------------> KORKAI
WESTERN PEPPER CIRCUITS --------------------------> MUCHIRI / MUZIRIS TRADITION
PORT FUNCTIONS: aggregation + customs + shipping + redistribution
RULE: no port flourished without inland producers, routes and consumers.""", ["Ports", "Trade"]),
        ("Mediterranean links, Arikamedu and Pattanam", "evidence-chain", """COINS + AMPHORAE + CERAMICS + PAPYRUS / CLASSICAL TEXTS
                         |
Indian Ocean and Mediterranean-linked exchange
ARIKAMEDU: earlier settlement + local craft + imported material
PATTANAM: major connected port evidence; Muziris identification debated
NOT PROVED: Roman colony, Roman sovereignty or foreign creation of Tamil economy.
VERDICT: multi-nodal contact amplified indigenous production and routes.""", ["Arikamedu", "Muziris debate"]),
        ("Society, labour, women and varna", "social-matrix", """COURT ELITES / CHIEFS / BARDS / WARRIORS
MERCHANTS / ARTISANS / CULTIVATORS / PASTORALISTS
FISHERS / SALT WORKERS / OTHER DEPENDANT LABOUR
WOMEN: poetry, spinning, fishing, salt exchange and household work
VARNA vocabulary was known; regional social practice was not a neat four-box census.
RULE: occupational visibility or named women does not prove equality.""", ["Society", "Women and varna"]),
        ("Religion, culture and megalithic context", "cultural-ecosystem", """MURUGAN / MAYON / KORRAVAI + Brahmanical vocabulary
JAIN / BUDDHIST donors and cave contexts
HEROIC AND MORTUARY MEMORY -> poems, stones and burials
MEGALITHS -> varied forms, grave goods, iron and pottery
LIMIT: burial evidence does not automatically disclose settlement map or exact belief.
CULTURE: plurality emerged through local traditions and wider exchanges.""", ["Religion", "Megaliths"]),
        ("Chiefdom-to-state debate", "argument-tree", """CHIEFDOM READING -> personal retinue, raid, gift and bardic prestige
STATE READING -> centres, extraction, titles, offices and durable lineages
EVIDENCE -> ko/kon, Pugalur, Mangulam, ports and agrarian cores
TRADE -> amplifier, not sole creator
IRON -> enabling technology, not sole cause
VERDICT: uneven movement toward early states; regional and reversible.""", ["State formation", "Historiography"]),
        ("PYQ and answer spine", "answer-synthesis", """PRELIMS: varna awareness | ports | Vattakirutal | ruler-lineage pairs
MAINS OPENING: evidentiary horizon, not one synchronized dynasty block
BODY 1: geography and source method
BODY 2: polity + economy + society + culture
BODY 3: port-hinterland mechanism and one historiographical debate
QUALIFY: genre, chronology, identification and representativeness
VERDICT: connected, uneven chiefdom-to-early-state Tamilakam.""", ["PYQs", "Answer architecture"]),
    ],
    "ancient-indian-history-19": [
        ("Periodization and evidence discipline", "timeline", """c. 600 BCE -> second-urbanisation background
c. 200 BCE -> regional polities and wider craft-trade networks
1st-2nd c. CE -> dense urban and maritime evidence in selected regions
3rd c. CE onward -> decline, continuity and route change coexist
SOURCES: texts + inscriptions + coins + craft debris + settlements + imports
RULE: archaeological phase labels do not automatically prove dynastic rule.""", ["Scope", "Chronology"]),
        ("Agrarian base of urban growth", "cause-mechanism-effect", """LAND + WATER + LABOUR + DIVERSE CROPS
                  |
food surplus + cotton / oilseeds / timber / ores / salt
                  |
supports non-food producers and supplies craft chains
                  |
town demand returns tools, markets, credit and institutions
VERDICT: village and town formed an interdependent system, not separate economies.""", ["Agrarian surplus", "Urban-rural interdependence"]),
        ("Craft production chains", "process", """RAW MATERIAL -> SPECIALISED LABOUR -> INSTALLATION / TOOL -> FINISHED GOOD
cotton -> spinning -> weaving -> dyeing -> cloth
agate/carnelian -> cutting -> drilling -> polishing -> beads
ore -> smelting -> forging/casting -> tools and ornaments
clay/glass/ivory/shell -> repeated forms and elite/common consumption
LIMIT: one vat, mould or workshop cannot establish ownership, scale or export destination.""", ["Craft specialisation", "Production"]),
        ("Shreni, nigama and merchant bodies", "institution-map", """ARTISANS / MERCHANTS
        |
shreni / corporate body / nigama identities
        |
deposits + endowments + standards + representation + donor visibility
        |
recurring provision for religious institutions
CAUTION: local records show corporate capacity, not one pan-Indian guild law
or a modern banking system.""", ["Guilds", "Merchant bodies"]),
        ("Inland corridors and market nodes", "network-map", """NORTH-WEST -> Taxila -> Mathura -> Ujjain -> Bharuch
GANGA ROUTES -> Kaushambi and other urban nodes
DECCAN -> Paithan / Tagara -> western and eastern outlets
TAMILAKAM -> production zones -> chattu caravans -> ports
UTTARAPATHA / DAKSHINAPATHA = broad changing route concepts
RULE: route lines show connectivity, not permanent paved highways or one ruler's monopoly.""", ["Internal trade", "Routes"]),
        ("Ports, monsoon and Indian Ocean exchange", "process", """HINTERLAND SURPLUS -> MARKET NODE -> PORT
                                  |
aggregation + customs + storage + shipping + redistribution
                                  |
seasonal winds + accumulated navigation knowledge
                                  |
Arabian Sea / Red Sea / Bay of Bengal networks
TRAP: no single foreign discoverer created monsoon sailing or Indian maritime trade.""", ["Ports", "Maritime trade"]),
        ("Mediterranean exchange without colony claims", "evidence-chain", """PEPPER / TEXTILES / BEADS / PEARLS / IVORY / STONES OUTWARD
COINS / BULLION / AMPHORAE / GLASS / CERAMICS / METALS INWARD
EVIDENCE -> Periplus, Pliny, papyrus, archaeology and coin contexts
PLINY -> Roman anxiety, not an audited Indian trade balance
IMPORTED OBJECT -> contact and consumption possibility
NOT PROVED -> resident Roman colony, sovereignty or universal prosperity.""", ["Roman trade", "Source limits"]),
        ("Coinage and uneven monetisation", "comparison", """KUSHANA -> gold and copper
WESTERN KSHATRAPA -> silver
SATAVAHANA -> lead, copper, potin and selected silver/portrait issues
CIVIC / PUNCH-MARKED / ROMAN-LINKED FINDS -> varied monetary worlds
COINS aided payments, revenue and exchange.
LIMIT: coin abundance does not erase barter, kind payments or regional monetary gaps.""", ["Coinage", "Monetisation"]),
        ("Urban morphology and regional centres", "evidence-matrix", """URBAN INDICATORS
fortification | planned streets | brick | drains | wells | coins | seals | crafts
NORTH-WEST / NORTH: Taxila, Mathura, Kaushambi and other nodes
CENTRAL / WEST: Ujjain, Bharuch and route centres
DECCAN / SOUTH: Paithan, Tagara, Arikamedu, Puhar and others
RULE: infer urban function from a cluster of indicators, never one imported sherd.""", ["Towns", "Regional centres"]),
        ("Religion, state and urban-rural systems", "systems-map", """VILLAGES -> food, fibre, labour and raw materials
TOWNS -> workshops, markets, rulers and consumers
ROUTES / PORTS -> wider demand and movement
RELIGIOUS INSTITUTIONS -> donors, endowments, lodging and legitimacy
STATE -> security + tolls + coinage + infrastructure + extraction
RESULT: mutually reinforcing functions, but burdens and benefits were unequal.""", ["Religion and trade", "State and commerce"]),
        ("Transformation and decline debate", "argument-tree", """OBSERVED: contraction at some sites / coin changes / route shifts
POSSIBLE CAUSES: political fragmentation + demand change + ecology + local restructuring
ROMAN-TRADE DECLINE -> relevant to selected circuits, never a universal single cause
CONTINUITIES: internal, eastern and regional networks; new centres can rise
METHOD: separate one site's decline from subcontinental transformation
VERDICT: early historic urbanism changed unevenly after the second century CE.""", ["Transformation", "Decline debates"]),
        ("UPSC answer spine", "answer-synthesis", """DEFINE PERIOD + SOURCE CAUTION
      -> agrarian and raw-material base
      -> crafts and corporate institutions
      -> inland routes + port-hinterland mechanism
      -> money + urban morphology + religious/state roles
      -> regional comparison + decline debate
WRITE EACH UNIT: claim -> named evidence -> significance -> limit
VERDICT: a networked, mutually reinforcing but regionally uneven florescence.""", ["Answer architecture", "PYQ route"]),
    ],
    "ancient-indian-history-20": [
        ("Source-led chronology", "evidence-chain", """GUPTA ERA 319-20 CE -> conventional imperial phase
PRAYAG PRASHASTI -> campaign categories + royal ideology
COINS -> titles, images, ritual and monetary zones
COPPER PLATES / SEALS -> offices, grants and local actors
FAXIAN -> selected Buddhist and social observations
RULE: triangulate sources; prashasti praise and coin circulation are not border maps.""", ["Sources", "Chronology"]),
        ("Formation and Chandragupta I", "timeline", """SRI GUPTA -> GHATOTKACHA -> CHANDRAGUPTA I
maharaja                  maharajadhiraja
                              |
Kumaradevi-Lichchhavi alliance represented on coin type
                              |
Ganga core + alliance + inherited routes + symbolic legitimacy
LIMIT: the coin proves advertised alliance, not a measurable dowry or exact border.""", ["Imperial formation", "Chandragupta I"]),
        ("Samudragupta's graded sovereignty", "layered-sovereignty", """ARYAVARTA -> rulers uprooted -> stronger core incorporation
ATAVIKA -> subordinated forest rulers
FRONTIER STATES / GANAS -> tribute, orders and obeisance
DAKSHINAPATHA -> captured, released and reinstated
DISTANT RULERS / ISLANDS -> gifts, service and prestige diplomacy
VERDICT: annexation, subordination and hegemony coexisted; not every name was a province.""", ["Samudragupta", "Prayag prashasti"]),
        ("Chandragupta II and western expansion", "cause-mechanism-effect", """SUCCESSION AND ALLIANCE CAPACITY
          |
defeat of western Kshatrapas in Malwa-Gujarat
          |
access to western routes, silver-coin zone and prestige centres
          |
Udayagiri and royal imagery strengthen Vaishnava political communication
CAUTION: Vikramaditya/Navaratna traditions require source and chronology control.""", ["Chandragupta II", "Western expansion"]),
        ("Late Guptas, Hunas and decline", "multi-causal-chain", """KUMARAGUPTA -> SKANDAGUPTA -> LATER GUPTAS
                         |
succession strains + Huna pressure + feudatory autonomy
                         |
fiscal and military burdens + regional powers + changing networks
                         |
contracting imperial authority
VERDICT: decline was cumulative and regional, not one invasion or instant collapse.""", ["Late Guptas", "Decline"]),
        ("Territoriality and administration", "layered-governance", """KING / COURT
   -> bhukti provincial level
   -> vishaya district level
   -> town / village bodies and local notables
   -> feudatories and frontier rulers
OFFICES and practice varied by region; Bengal plates are especially visible.
EMPIRE = directly ruled core + delegated administration + layered hegemony.""", ["Territoriality", "Administration"]),
        ("Land grants and fiscal decentralisation", "process", """ROYAL CHARTER
    -> land / revenue rights + exemptions + boundary record
    -> Brahmana or religious beneficiary
    -> local cultivators, labour and intermediaries
    -> agrarian expansion + legitimation + fiscal reallocation
DEBATE: grants could strengthen frontier integration while also enlarging local autonomy.
RULE: read the exact rights; do not assume every grant transferred total sovereignty.""", ["Land grants", "Decentralisation"]),
        ("Economy, coinage and urban change", "comparison", """GOLD COINS -> royal high-value capacity and imagery
SILVER ISSUES -> western zone after Kshatrapa conquest
COPPER SCARCITY / REGIONAL MEDIA -> uneven everyday monetisation
GUILDS / CRAFTS / PORTS -> continuity in selected nodes
URBAN EVIDENCE -> contraction in some centres, persistence or relocation in others
VERDICT: neither universal prosperity nor total urban collapse fits the evidence.""", ["Economy", "Urban change"]),
        ("Society, Faxian and religion", "social-matrix", """VARNA / JATI / OCCUPATION -> norm and lived diversity
VISHTI -> labour obligation in selected grants
FAXIAN -> Buddhist pilgrim lens; Chandala passage and institutional observations
VAISHNAVA / SHAIVA / SHAKTA patronage + Buddhist and Jain continuities
ROYAL AND NON-ROYAL DONORS -> plural religious landscape
LIMIT: normative texts and traveller accounts are not censuses.""", ["Society", "Religion"]),
        ("Literature, science and arts", "cultural-ecosystem", """SANSKRIT COURT CULTURE -> Kalidasa / Amarasimha traditions
MATHEMATICS-ASTRONOMY -> Aryabhatiya, 499 CE
METALLURGY -> Mehrauli iron pillar with attribution caution
ARCHITECTURE -> Udayagiri, Sanchi 17, Bhitargaon and Deogarh
SCULPTURE / PAINTING -> Mathura, Sarnath and Vakataka-context Ajanta
RULE: name work, date, patronage context and ownership limit.""", ["Culture", "Science and art"]),
        ("Golden Age and historiography", "argument-tree", """FOR: durable literature + science + sculpture + temple forms + political prestige
AGAINST UNIVERSAL LABEL:
  |-- regional production beyond direct Gupta rule
  |-- hierarchy, exclusion, vishti and patriarchal norms
  |-- uneven urban and monetary conditions
  `-- elite-source bias
VERDICT: a bounded classical florescence, not a census judgement on all society.""", ["Golden Age", "Historiography"]),
        ("Gupta answer spine", "answer-synthesis", """OPEN: inscription- and coin-led layered empire, c. 319-550 CE
RULERS: formation -> Samudragupta -> Chandragupta II -> late pressures
POLITY: graded sovereignty + administration + feudatories
ECONOMY: grants + agrarian base + coins + urban variation
CULTURE: use only bounded examples; Topic 21 owns social-cultural depth
QUALIFY: genre, region, attribution and distribution
VERDICT: high-capacity core with negotiated and changing peripheries.""", ["Answer architecture", "Topic boundary"]),
    ],
    "ancient-indian-history-21": [
        ("Topic boundary and source matrix", "evidence-matrix", """OWNER: society, daily life, knowledge, religion and arts in the Gupta age
TOPIC 20 RETAINS: rulers, campaigns, offices, grants machinery and decline
SOURCES: Smriti | literature | inscriptions | coins | Faxian | art | archaeology
TEXT -> norm / imagination; INSCRIPTION -> selected public actor
TRAVELLER -> situated observation; MATERIAL -> practice with dating limits
METHOD: use at least two source classes and state each limitation.""", ["Scope", "Sources"]),
        ("Varna, jati and exclusion", "social-matrix", """VARNA -> normative four-fold macro-model
JATI / OCCUPATION -> numerous local and professional identities
STATUS CLAIM -> genealogy, office, patronage and Sanskritic idiom
EXCLUSION -> Chandala evidence, occupational stigma and spatial distance
MOBILITY and hierarchy coexisted.
RULE: one Smriti norm or Faxian passage cannot become a uniform all-India census.""", ["Social hierarchy", "Marginal groups"]),
        ("Family, women and property", "comparison", """PATRILINEAL / PATRIARCHAL NORM -> dominant prescriptive frame
MARRIAGE / INHERITANCE -> text-specific and socially varied
STRIDHANA -> recognized category with differing control and succession rules
WOMEN'S AGENCY -> queens, donors, workers and literary representations
LIMIT: elite visibility does not prove general equality.
TRAP: Mitakshara and Dayabhaga are later schools, not Gupta legal codes.""", ["Household", "Women"]),
        ("Village, labour, craft and urban life", "systems-map", """VILLAGE -> cultivators + land + taxes + vishti + household production
                           |
                 food / fibre / revenue
                           v
TOWN -> artisans + merchants + guild-linked groups + markets + sacred institutions
MANDASOR SILK WEAVERS -> migration, corporate identity and patronage
VERDICT: agrarian surplus and urban craft networks interacted, but regionally unevenly.""", ["Village life", "Guild-linked urban life"]),
        ("Faxian and daily-life reconstruction", "evidence-chain", """FAXIAN c. 399-414 CE -> Buddhist pilgrimage purpose
        |
monasteries, routes, selected customs and Chandala passage
        |
valuable near-contemporary social and religious observations
        |
LIMITS: itinerary + audience + translation + silence + idealisation
USE: corroborate with inscriptions, texts and archaeology; never quote as a census.""", ["Faxian", "Daily life"]),
        ("Education, Sanskrit and multilingualism", "knowledge-ecosystem", """COURTS + BRAHMANICAL CENTRES + MONASTERIES + TEACHER-PUPIL NETWORKS
                              |
Sanskrit prestige in kavya, prashasti, theology and science
                              |
Prakrits, regional speech and local inscriptions continue
                              |
SANSKRITISATION = adoption + negotiation + local adaptation
NOT: one royal language law, universal literacy or extinction of other languages.""", ["Education", "Sanskritisation"]),
        ("Literature and genre map", "classification", """KAVYA / DRAMA -> Kalidasa and courtly aesthetic worlds
LEXICOGRAPHY -> Amarasimha / Amarakosha tradition
PURANIC TEXTS -> layered redaction and devotional-cosmological synthesis
SMRITI -> prescriptive law and social norm
BUDDHIST / JAIN WRITING -> continuing intellectual plurality
RULE: secure work and genre are stronger than later court-biography legends.""", ["Literature", "Genre"]),
        ("Mathematics, astronomy and metallurgy", "timeline", """499 CE -> ARYABHATIYA: computation, astronomy, pi and earth-rotation argument
6th c. -> VARAHAMIHIRA: post-main-Gupta continuation
628 CE -> BRAHMAGUPTA: explicitly post-Gupta chronology
MEHRAULI IRON PILLAR -> large wrought iron and corrosion resistance
CAUTION: place value != sole invention of zero; King Chandra identification debated.
VERDICT: cumulative specialist traditions, not isolated miracle claims.""", ["Science", "Chronology cautions"]),
        ("Religious plurality and patronage", "cultural-ecosystem", """VAISHNAVA + SHAIVA + SHAKTA Puranic formations
BUDDHIST monasteries, images and pilgrimage networks
JAIN communities, images and sites
ROYAL COURTS + regional rulers + guilds + households + monks -> patrons
Udayagiri joins royal Vaishnava imagery with wider sacred presence.
RULE: plural patronage was unequal and strategic; it is not modern secular neutrality.""", ["Religion", "Patronage"]),
        ("Temples, sculpture, painting and Ajanta", "comparison", """TEMPLES -> Sanchi 17 | Udayagiri | Bhitargaon | Deogarh
SCULPTURE -> Mathura and Sarnath materials, modelling and robe conventions
PAINTING -> Ajanta narrative, courtly, devotional and workshop production
ARCHITECTURAL TREND -> garbhagriha + porch/mandapa + emerging superstructure
OWNERSHIP LIMIT: major fifth-century Ajanta phase is Vakataka-context.
RULE: name object/site, form, date, patronage and attribution caution.""", ["Temple architecture", "Sculpture and painting"]),
        ("Golden Age and social distribution", "argument-tree", """CLASSICAL ACHIEVEMENT
literature + science + iconic art + structural temples + prestige language
                         |
TEST DISTRIBUTION
region | class | caste | gender | labour | literacy | patronage
                         |
COUNTER-EVIDENCE: exclusion, vishti, patriarchal norms and elite archives
VERDICT: culturally consequential and enduring, but neither uniform nor universally golden.""", ["Golden Age debate", "Social distribution"]),
        ("Culture answer spine", "answer-synthesis", """OPEN: social-cultural companion to Gupta polity, reconstructed through mixed sources
BODY 1: hierarchy + household + women + labour
BODY 2: village-town and patronage institutions
BODY 3: language + literature + science + religion + arts
EACH EXAMPLE: claim -> named evidence -> significance -> limit
QUALIFY: chronology, regional ownership, source genre and social distribution
VERDICT: classical production emerged from plural but unequal social worlds.""", ["Answer architecture", "PYQ ownership"]),
    ],
}


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def split_h2(markdown: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(re.finditer(r"(?m)^##(?!#)\s+(.+?)\s*$", markdown))
    if not matches:
        raise ValueError("Source package has no H2 sections.")
    preamble = markdown[: matches[0].start()]
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        sections.append((match.group(1).strip(), markdown[match.start() : end].strip()))
    return preamble, sections


def strip_title(preamble: str) -> str:
    lines = preamble.strip().splitlines()
    if lines and re.match(r"^#(?!#)\s+", lines[0]):
        lines = lines[1:]
    return "\n".join(lines).strip()


def normalize_fragment(fragment: str) -> str:
    output: list[str] = []
    for line in fragment.replace("\r\n", "\n").splitlines():
        if re.match(r"^#\s+PART\b", line, re.I):
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not heading:
            output.append(line)
            continue
        level = len(heading.group(1))
        new_level = 3 if level <= 2 else min(6, level + 1)
        output.append("#" * new_level + " " + heading.group(2))
    text = "\n".join(output)
    text = text.replace("(../../../notes/", "(notes/")
    text = text.replace("(..\\..\\..\\notes\\", "(notes\\")
    text = re.sub(
        r"\*\*(?:Correct answer|Answer):\*\*\s*([A-D])\s*-\s*",
        lambda match: f"**Answer: {match.group(1).upper()}** - ",
        text,
        flags=re.I,
    )
    return text.strip()


def expand_inline_mcqs(fragment: str, start: int) -> tuple[str, int]:
    lines = fragment.splitlines()
    output: list[str] = []
    number = start
    pattern = re.compile(r"^\s*-\s*((?:Q|Loop|R)\s*\d+)\.\s+(.+)$", re.I)
    answer_pattern = re.compile(
        r"\s+(?:Correct answer|Answer):\s*([A-D])\.\s*(?:Explanation:\s*)?",
        re.I,
    )
    answer_line_pattern = re.compile(
        r"^\s*-\s*(?:Correct answer|Answer):\s*([A-D])\.\s*(?:Explanation:\s*)?(.+)$",
        re.I,
    )
    option_pattern = re.compile(r"(?<!\S)([A-D])[\.)]\s+")
    index = 0
    while index < len(lines):
        line = lines[index]
        match = pattern.match(line)
        if not match:
            output.append(line)
            index += 1
            continue
        answer = answer_pattern.search(match.group(2))
        consumed_answer_line = False
        answer_letter = ""
        explanation = ""
        if answer:
            core = match.group(2)[: answer.start()].strip()
            answer_letter = answer.group(1).upper()
            explanation = match.group(2)[answer.end() :].strip()
        elif index + 1 < len(lines):
            answer_line = answer_line_pattern.match(lines[index + 1])
            if answer_line:
                core = match.group(2).strip()
                answer_letter = answer_line.group(1).upper()
                explanation = answer_line.group(2).strip()
                consumed_answer_line = True
            else:
                output.append(line)
                index += 1
                continue
        else:
            output.append(line)
            index += 1
            continue
        option_matches = list(option_pattern.finditer(core))
        if len(option_matches) != 4 or [item.group(1).upper() for item in option_matches] != list("ABCD"):
            output.append(line)
            index += 1
            continue
        question = core[: option_matches[0].start()].strip()
        options: list[str] = []
        for option_index, option in enumerate(option_matches):
            end = (
                option_matches[option_index + 1].start()
                if option_index + 1 < 4
                else len(core)
            )
            options.append(core[option.end() : end].strip())
        number += 1
        output.extend(
            [
                f"#### MCQ {number:02d} - {match.group(1)}",
                "",
                question,
                "",
                *[f"- {letter}. {value}" for letter, value in zip("ABCD", options)],
                "",
                f"**Answer: {answer_letter}** - {explanation}",
                "",
            ]
        )
        index += 2 if consumed_answer_line else 1
    return "\n".join(output).strip(), number


def promote_bold_mcqs(fragment: str, start: int) -> tuple[str, int]:
    output: list[str] = []
    number = start
    pattern = re.compile(r"^\*\*((?:Q|R)\d+)\.\s+(.+?)\*\*\s*$", re.I)
    for line in fragment.splitlines():
        match = pattern.match(line.strip())
        if not match:
            output.append(line)
            continue
        number += 1
        output.extend(
            [
                f"#### MCQ {number:02d} - {match.group(1)}",
                "",
                match.group(2).strip(),
            ]
        )
    return "\n".join(output).strip(), number


def classify_17(title: str) -> str:
    if title.startswith("PART I") or title.startswith(("Package practice", "Sources actually")):
        return "basic"
    if re.match(r"^\d{2}\.", title):
        return "basic"
    if title.startswith("PART II") or title.startswith("PYQ "):
        return "practice"
    if title.startswith("PART III") or "MCQ " in title:
        return "mcq"
    if title.startswith("PART IV") or title.startswith("Mains "):
        return "practice"
    if title.startswith("PART V") or title.startswith("FINAL REGISTER"):
        return "register"
    raise ValueError(f"Unclassified Topic 17 section: {title}")


def classify_18(title: str) -> str:
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if title.startswith("16.") or title.startswith(
        ("01. Workbook method", "03. Broad", "04. Broad", "05. Broad", "06. Broad", "07. Remedial")
    ):
        return "mcq"
    if title.startswith(("17.", "02. Direct", "08. Original", "09. Original", "10. Original")):
        return "practice"
    if title.startswith("FINAL REGISTER"):
        return "register"
    if re.match(r"^(?:0[1-9]|1[0-5])\.", title):
        return "basic"
    raise ValueError(f"Unclassified Topic 18 section: {title}")


def classify_19(title: str) -> str:
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if title.startswith(
        ("24.", "25.", "01. Workbook method", "03. Broad", "04. Broad", "05. Broad", "06. Broad", "07. Remedial")
    ):
        return "mcq"
    if title.startswith(("23.", "26.", "02. Solved", "08. Solved", "09. Solved", "10. Solved")):
        return "practice"
    if title.startswith("FINAL REGISTER"):
        return "register"
    if re.match(r"^(?:0[1-9]|1\d|2[0-2])\.", title):
        return "basic"
    raise ValueError(f"Unclassified Topic 19 section: {title}")


def classify_20(title: str) -> str:
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if re.match(r"^(?:0[1-9]|1\d|2[0-4])\.", title):
        return "basic"
    if title.startswith(("Broad MCQs", "Remedial MCQs")):
        return "mcq"
    if title.startswith(("PYQ ", "Original solved Mains")):
        return "practice"
    if title.startswith("Final Register"):
        return "register"
    raise ValueError(f"Unclassified Topic 20 section: {title}")


def classify_21(title: str) -> str:
    if title.startswith(("Package counts", "Original visual")):
        return "basic"
    if re.match(r"^(?:0[1-9]|1\d|2[0-1])\.", title):
        return "basic"
    if title.startswith(("Learning MCQ", "Workbook MCQ", "Remedial ")):
        return "mcq"
    if title.startswith(
        (
            "Critically examine",
            "Discuss the relationship",
            "Explain the contribution",
            "Verified PYQ",
            "Original solved Mains",
        )
    ):
        return "practice"
    if title.startswith("FINAL REGISTER"):
        return "register"
    raise ValueError(f"Unclassified Topic 21 section: {title}")


CLASSIFIERS: dict[str, Callable[[str], str]] = {
    "ancient-indian-history-17": classify_17,
    "ancient-indian-history-18": classify_18,
    "ancient-indian-history-19": classify_19,
    "ancient-indian-history-20": classify_20,
    "ancient-indian-history-21": classify_21,
}


def assemble(config_value: dict[str, object]) -> str:
    canonical = Path(config_value["canonical"])
    source = canonical.read_text(encoding="utf-8")
    preamble, sections = split_h2(source)
    grouped: dict[str, list[str]] = {
        "basic": [],
        "mcq": [],
        "practice": [],
        "register": [],
    }
    inline_counter = 0
    for title, fragment in sections:
        bucket = CLASSIFIERS[str(config_value["key"])](title)
        normalized = normalize_fragment(fragment)
        if title.startswith(
            (
                "Package practice counts",
                "Package counts",
                "Original visual inventory",
                "Sources actually used",
                "PART ",
            )
        ) or (
            title.startswith("Original visual asset index")
            and str(config_value["key"])
            in {
                "ancient-indian-history-19",
                "ancient-indian-history-20",
                "ancient-indian-history-21",
            }
        ):
            normalized = re.sub(r"^### ", "#### ", normalized, count=1)
        if (
            str(config_value["key"]) == "ancient-indian-history-20"
            and title.startswith("20.")
        ):
            normalized = normalized.replace(
                "[ANALYSIS] Architecture and images created ritual space, "
                "political meaning and durable cultural models.",
                "[ANALYSIS] Gupta art, architecture, sculpture and painting "
                "created ritual space, political meaning and durable cultural models.",
            )
        if bucket == "mcq" and str(config_value["key"]) in {
            "ancient-indian-history-18",
            "ancient-indian-history-19",
        }:
            normalized, inline_counter = expand_inline_mcqs(normalized, inline_counter)
        if bucket == "mcq" and str(config_value["key"]) == "ancient-indian-history-20":
            normalized, inline_counter = promote_bold_mcqs(normalized, inline_counter)
        grouped[bucket].append(normalized)
    advanced = normalize_fragment(Path(config_value["advanced"]).read_text(encoding="utf-8"))
    intro = strip_title(preamble)
    current = (
        "### Bounded live linkage\n\n"
        f"{config_value['current_note']}\n\n"
        "This linkage does not override the repository chronology, local book evidence, "
        "or the source limitations printed throughout the package."
    )
    return (
        f"# {config_value['title']} - Complete Topic Package\n\n"
        f"{intro}\n\n"
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


def image_sources(source: Path) -> list[Path]:
    text = source.read_text(encoding="utf-8")
    results: list[Path] = []
    for raw in re.findall(r"!\[[^\]]*]\(([^)]+)\)", text):
        if "://" in raw:
            continue
        normalized = Path(raw.replace("\\", "/"))
        candidates = [source.parent / normalized, ROOT / normalized]
        resolved = next((item.resolve() for item in candidates if item.resolve().is_file()), None)
        if resolved and resolved not in results:
            results.append(resolved)
    return results


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
                "source_markdown": relative(Path(config_value["canonical"])),
                "panel_count": 12,
                "panels": panels,
            }
        )
    payload = {
        "schema_version": 1,
        "generated_on": DATE,
        "scope": "Ancient Indian History learner-v2 Topics 17-21",
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
        source_markdown_path=relative(source_path),
        ascii_spec_path=relative(ASCII_PATH),
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
    local_books = [RS_SHARMA, UPINDER]
    if key == "ancient-indian-history-21":
        local_books.append(SINGHANIA)
    source_files = [
        Path(config_value["basic"]),
        Path(config_value["advanced"]),
        Path(config_value["canonical"]),
        source_path,
        *[ROOT / item for item in COMMON_CROSS],
        *[ROOT / item for item in PYQ_INDEXES],
        *local_books,
        Path(config_value["legacy_main"]),
        Path(config_value["legacy_workbook"]),
        SECTION_MANIFEST,
        CATALOG,
        ASCII_PATH,
        graphical_path,
        *image_sources(Path(config_value["canonical"])),
    ]
    deduplicated: list[Path] = []
    for path in source_files:
        resolved = path.resolve()
        if resolved not in deduplicated:
            deduplicated.append(resolved)
    missing = [str(path) for path in deduplicated if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing source files: " + ", ".join(missing))
    command_title = str(config_value["title"])
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
            + command_title
        ),
        "source_markdown": relative(source_path),
        "source_basic": relative(Path(config_value["basic"])),
        "source_canonical": relative(Path(config_value["canonical"])),
        "source_advanced": relative(Path(config_value["advanced"])),
        "manifest": relative(SECTION_MANIFEST),
        "cross_topic_sources": COMMON_CROSS,
        "pyq_indexes": PYQ_INDEXES,
        "official_question_sources": [],
        "local_ocr_sources": [relative(path) for path in local_books],
        "live_sources": config_value["live_sources"],
        "source_files": [relative(path) for path in deduplicated],
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
        generation_spec = write_generation_spec(config_value, source_path, graphical_path)
        written.extend([source_path, graphical_path, generation_spec])
    for path in written:
        print(relative(path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
