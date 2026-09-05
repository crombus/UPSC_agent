"""Authored data for Environment and Ecology learner-v2 Topic 06."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import PROTECTED_AREA_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("Four protected-area categories", "The owner separates National Park, Wildlife Sanctuary, Conservation Reserve and Community Reserve under the Wildlife Protection Act; they are not one uniform land category."),
    ("National Park", "A National Park uses the strictest of the four owner-described regimes; rights, grazing, entry and activities remain governed by the Act and the area's notification."),
    ("Wildlife Sanctuary", "A Wildlife Sanctuary protects wildlife and habitat while permitting a different, generally less restrictive rights and regulated-activity settlement than a National Park."),
    ("Conservation Reserve", "A Conservation Reserve is a statutory connector or buffer category generally associated with government land and consultation with local communities."),
    ("Community Reserve", "A Community Reserve is a consent-based category on community or private land with a continuing local management role."),
    ("Rights and activity gradient", "Permitted rights and activities vary by legal category and site-specific notification; strictness cannot be inferred from the generic phrase protected area."),
    ("2002 category expansion", "The owner attributes Conservation Reserves and Community Reserves to the 2002 amendment, extending conservation beyond exclusion-oriented core categories."),
    ("Tiger Reserve overlay", "A Tiger Reserve is a species-management overlay under the NTCA framework and does not erase the underlying National Park, Sanctuary or other land status."),
    ("Critical tiger habitat and buffer", "The tiger-reserve model separates core or critical tiger habitat from a buffer or peripheral area; each boundary and management claim must remain site-specific."),
    ("Relocation and rights", "The owner requires voluntary informed consent and rehabilitation for relocation from critical tiger habitat and flags coordination with Forest Rights Act processes."),
    ("Elephant landscape distinction", "Elephant reserves and corridors rely more on landscape coordination than an NTCA-equivalent statutory core-buffer mechanism; the two species models are not interchangeable."),
    ("Eco-Sensitive Zone statute", "An Eco-Sensitive Zone is separately notified under the Environment Protection Act, not declared as a fifth protected-area category under the Wildlife Protection Act."),
    ("ESZ extent and activities", "ESZ extent and prohibited, regulated or promoted activities come from the individual notification; there is no automatic uniform statutory width."),
    ("Boundary and surrounding landscape", "The notified protected-area boundary, a separately notified ESZ and the wider ecological corridor are distinct spatial objects even when they interact."),
    ("Connectivity", "Corridors, stepping-stone habitats and compatible land use outside protected areas determine whether populations can disperse across a fragmented landscape."),
    ("Boundary alteration safeguards", "The owner records State Legislature, NBWL and, for Tiger Reserves, NTCA roles in specified boundary alteration or de-notification safeguards; the applicable route must be checked."),
    ("Authorities and jurisdiction", "State wildlife authorities manage the four categories, while NBWL, NTCA, WII and MoEFCC perform different approval, species-overlay, scientific and policy functions."),
    ("OECM distinction", "An OECM records sustained area-based conservation outside the formal protected-area system; it is not automatically a Wildlife Protection Act category."),
    ("Live official network boundary", "MoEFCC's retrievable wildlife page confirmed the four categories and protection outside protected areas, but its undated displayed count was not adopted as the latest network total."),
    ("Audited PYQ and designation route", "Routed demands cover named parks, habitats, community-reserve governance and Madhav National Park, Tiger Reserve and Sakhya Sagar as separate designation functions; no objective key is inferred."),
]

TRAPS = [
    "Do not treat every protected area as a National Park.",
    "Do not assign National Park restrictions automatically to every Sanctuary.",
    "Do not describe a Conservation Reserve as community-owned land by definition.",
    "Do not describe a Community Reserve without the consent and management role.",
    "Do not infer permitted activity without the Act and site notification.",
    "Do not date all four categories to the original 1972 enactment.",
    "Do not call a Tiger Reserve a fifth generic protected-area land category.",
    "Do not treat core, buffer and ESZ as interchangeable boundaries.",
    "Do not present relocation as automatic or rights-free.",
    "Do not give Elephant Reserves the NTCA's statutory core-buffer structure.",
    "Do not place ESZ notification under the Wildlife Protection Act.",
    "Do not apply a uniform ESZ width to every protected area.",
    "Do not equate a legal boundary with the whole ecological landscape.",
    "Do not turn notification count into proof of connectivity or management quality.",
    "Do not infer a current protected-area count from an undated official page.",
]

SESSION_TITLES = [
    "Four legal categories and National Park",
    "Wildlife Sanctuary",
    "Conservation Reserve",
    "Community Reserve",
    "Rights and activity gradient",
    "2002 expansion and Tiger Reserve overlay",
    "Critical tiger habitat and buffer",
    "Relocation and Forest Rights Act coordination",
    "Elephant landscape model",
    "Eco-Sensitive Zone statute",
    "ESZ extent and distinct spatial boundaries",
    "Landscape connectivity",
    "Boundary safeguards",
    "Authorities, jurisdiction and OECMs",
    "Live network and audited PYQ boundary",
]

ANSWER_ROUTES = [
    "Open with all four categories and the National Park regime.",
    "Contrast Sanctuary rights and regulated activity with a National Park.",
    "Use the connector or buffer function and government-land basis carefully.",
    "Use consent, tenure and local management as the distinguishing axis.",
    "Fix the category and notification before asserting an activity or right.",
    "Explain the 2002 expansion and present Tiger Reserve as an overlay.",
    "Keep core and buffer boundaries tied to the particular reserve.",
    "Pair habitat protection with consent, rehabilitation and tenure recognition.",
    "Match reserve design to elephant ranging ecology and corridors.",
    "Name the Environment Protection Act and separate ESZ from a PA category.",
    "Draw PA, ESZ and corridor as distinct, site-specific spatial layers.",
    "Explain dispersal, stepping-stone habitat and outside-PA land use.",
    "Identify the applicable State Legislature, NBWL or NTCA safeguard.",
    "Assign each institution and OECM to its correct jurisdiction.",
    "Close with dated evidence and no inferred network outcome or objective key.",
]

PANELS = [
    panel("Four-category legal ladder", "hierarchy", [
        "NATIONAL PARK -> strict statutory habitat regime",
        "WILDLIFE SANCTUARY -> protected habitat with a different rights settlement",
        "CONSERVATION RESERVE -> connector or buffer, generally government land",
        "COMMUNITY RESERVE -> consent-based community or private land",
        "RULE -> each category has its own notification and activity regime",
    ], [FACTS[0][0], FACTS[1][0], FACTS[2][0], FACTS[3][0], FACTS[4][0]]),
    panel("Rights and tenure matrix", "comparison-table", [
        "NATIONAL PARK -> strictest owner-described activity regime",
        "SANCTUARY -> regulated rights may continue after settlement",
        "CONSERVATION RESERVE -> consultation-centered government-land route",
        "COMMUNITY RESERVE -> consent plus local management role",
        "CAUTION -> read the Act and site notification before asserting a right",
    ], [FACTS[5][0]]),
    panel("2002 expansion logic", "timeline", [
        "1972 FRAMEWORK -> National Parks and Sanctuaries",
        "LANDSCAPE GAP -> corridors, buffers and non-state tenure",
        "2002 AMENDMENT -> Conservation and Community Reserves",
        "RESULT -> wider legal menu without one exclusion model",
        "LIMIT -> category creation does not prove on-ground conservation",
    ], [FACTS[6][0]]),
    panel("Tiger overlay stack", "layered-rail", [
        "UNDERLYING LAND STATUS -> NP, Sanctuary or other notified landscape",
        "TIGER RESERVE -> NTCA-linked species-management overlay",
        "CORE -> critical tiger habitat",
        "BUFFER -> coexistence and connectivity functions",
        "RULE -> overlay and underlying category remain distinct",
    ], [FACTS[7][0], FACTS[8][0]]),
    panel("Relocation safeguard gate", "process-flow", [
        "CORE-HABITAT PROPOSAL -> identify affected rights holders",
        "CONSENT -> voluntary and informed",
        "REHABILITATION -> applicable package and implementation",
        "FRA COORDINATION -> tenure-recognition process cannot be ignored",
        "VERDICT -> habitat protection and rights compliance must travel together",
    ], [FACTS[9][0]]),
    panel("Tiger and elephant models", "comparison-table", [
        "TIGER -> statutory NTCA core-buffer architecture",
        "ELEPHANT -> wide-ranging corridor and landscape coordination",
        "BOUNDARY FIT -> stronger for bounded tiger habitat than elephant movement",
        "JURISDICTION -> multi-state coordination matters for elephants",
        "RULE -> reserve design must follow species ecology",
    ], [FACTS[10][0]]),
    panel("ESZ legal firewall", "comparison", [
        "PROTECTED AREA -> Wildlife Protection Act notification",
        "ESZ -> Environment Protection Act notification",
        "PA BOUNDARY -> primary protected-area legal line",
        "ESZ BOUNDARY -> separate site-specific regulatory line",
        "NO UNIFORM WIDTH -> read the individual notification",
    ], [FACTS[11][0], FACTS[12][0], FACTS[13][0]]),
    panel("Three spatial objects", "spatial", [
        "INNER -> notified protected-area boundary",
        "AROUND -> separately notified Eco-Sensitive Zone",
        "BEYOND -> corridor, catchment or seasonal-use landscape",
        "OVERLAP IN ECOLOGY -> distinct in legal identity",
        "ANSWER RULE -> never call the whole landscape the notified PA",
    ], [FACTS[13][0], FACTS[14][0]]),
    panel("Connectivity mechanism", "causal-chain", [
        "ISOLATED HABITAT -> reduced movement and dispersal",
        "CORRIDOR OR STEPPING STONE -> functional linkage",
        "GENE FLOW AND SEASONAL ACCESS -> improved persistence pathway",
        "OUTSIDE-PA LAND USE -> determines corridor quality",
        "LIMIT -> mapped corridor is not proof of functional connectivity",
    ], [FACTS[14][0]]),
    panel("Boundary safeguard map", "authority-map", [
        "STATE PROCESS -> protected-area notification and management",
        "STATE LEGISLATURE -> owner-recorded role for specified boundary changes",
        "NBWL -> owner-recorded recommendation or approval safeguard",
        "NTCA -> additional Tiger Reserve boundary role",
        "RULE -> identify the exact category before naming the authority",
    ], [FACTS[15][0], FACTS[16][0]]),
    panel("Formal PA and OECM", "comparison-table", [
        "FORMAL PA -> statutory category under wildlife law",
        "OECM -> sustained conservation outcome outside formal PA status",
        "SACRED OR WORKING LANDSCAPE -> possible OECM route, not automatic status",
        "COUNTING CLAIM -> needs a verified recognition process",
        "RULE -> outcome label does not silently create a legal category",
    ], [FACTS[17][0]]),
    panel("Evidence and PYQ spine", "answer-spine", [
        "CLASSIFY -> PA category, Tiger overlay, ESZ, corridor or OECM",
        "FIX -> notified boundary and competent authority",
        "ADD -> rights, connectivity and management mechanism",
        "DATE -> any count, notification or overlay milestone",
        "QUALIFY -> designation is not verified protection outcome",
    ], [FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS,
        "2023",
        "GS-I Q15",
        "Diversity of natural vegetation and the role of rain-forest wildlife sanctuaries.",
        "Routed from an audited official-paper ledger; model answer independently authored.",
        [2, 13, 14, 16],
    )
]

TOPIC_06 = common.topic(
    6,
    "Protected Area Network India",
    "06_Protected-Area-Network-India",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-06_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish India's four protected-area categories.", [0, 1, 2, 3, 4]),
        (10, "Why were Conservation and Community Reserves added?", [3, 4, 6]),
        (15, "Explain Tiger Reserve overlay, core-buffer design and rights safeguards.", [7, 8, 9]),
        (15, "Distinguish a protected-area boundary, ESZ and ecological corridor.", [11, 12, 13, 14]),
        (20, "Critically assess India's protected-area network through rights and connectivity.", [5, 9, 14, 15, 16]),
        (20, "Compare tiger and elephant conservation architecture in India.", [7, 8, 10, 14, 17]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "National Park", "Wildlife Sanctuary", "Conservation Reserve",
        "Community Reserve", "2002 amendment", "Tiger Reserve",
        "critical tiger habitat", "buffer", "voluntary informed consent",
        "Forest Rights Act", "Elephant Reserve", "Eco-Sensitive Zone",
        "Environment Protection Act", "site-specific notification", "corridor",
        "State Legislature", "National Board for Wildlife", "NTCA", "OECM",
        "Sakhya Sagar",
    ],
    (
        "Audited ledgers route named parks and habitats, Community Reserve "
        "governance, a 2023 GS-I sanctuary demand and a provisional 2026 Madhav "
        "National Park, Tiger Reserve and Sakhya Sagar distinction. The Mains "
        "demand receives an independently authored model; objective keys, "
        "current counts and unstated legal boundaries are not inferred."
    ),
    PYQ_SOLUTIONS,
    PROTECTED_AREA_LIVE_SOURCE_ATTEMPTS,
    (
        "MoEFCC's wildlife page was substantively retrieved on 2026-09-03 and "
        "used only to confirm the four categories and conservation outside PAs. "
        "Its undated count was not promoted as latest. WII ENVIS did not resolve, "
        "India Code returned HTTP 403, and ESZ material was used only to confirm "
        "notification-specific mapping, not a uniform width or individual boundary."
    ),
    extra=[
        "basic/08_Wildlife-Protection-Act-and-Schedules.md",
        "basic/11_Forest-Types-and-Forest-Rights-Act.md",
        "advanced/11_Forest-Types-and-Forest-Rights-Act.md",
        "basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
    ],
    register_headings=(
        "LEGAL CATEGORY, OVERLAY AND SPATIAL LAYER MAP",
        "RIGHTS, BOUNDARY, ESZ AND CONNECTIVITY TRAPS",
        "LANDSCAPE-CONSERVATION ANSWER SPINE",
        "LIVE COUNT, NOTIFICATION AND JURISDICTION BOUNDARY",
    ),
    register_answer_spine=[
        "CLASSIFY THE OBJECT: NP, SANCTUARY, CONSERVATION OR COMMUNITY RESERVE",
        "SEPARATE THE UNDERLYING CATEGORY FROM TIGER OR ELEPHANT MANAGEMENT",
        "FIX THE NOTIFIED PA BOUNDARY, ESZ AND WIDER CORRIDOR",
        "STATE RIGHTS, CONSENT AND REHABILITATION REQUIREMENTS",
        "NAME THE COMPETENT STATE, NBWL OR NTCA ROLE",
        "ADD CONNECTIVITY AND OUTSIDE-PA LAND-USE ANALYSIS",
        "CONCLUDE THAT NOTIFICATION IS NOT MANAGEMENT EFFECTIVENESS",
    ],
)
