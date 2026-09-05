"""Authored data for Environment and Ecology learner-v2 Topic 07."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import BIOSPHERE_RAMSAR_LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    ("National Biosphere Reserve designation", "India can designate a Biosphere Reserve nationally as a landscape-planning and conservation unit; that national status is distinct from UNESCO World Network recognition."),
    ("UNESCO World Network status", "Inclusion in UNESCO's World Network follows a separate international process; not every nationally designated Indian Biosphere Reserve automatically has UNESCO status."),
    ("Core zone", "The core zone prioritises long-term conservation and minimal disturbance and commonly overlaps an area already protected under domestic wildlife or forest law."),
    ("Buffer zone", "The buffer zone supports activities compatible with conservation, including research, monitoring, education and carefully managed use."),
    ("Transition zone", "The transition zone is a cooperation landscape for settlements, livelihoods and ecologically sustainable development rather than a strict exclusion zone."),
    ("Three biosphere functions", "The biosphere model combines conservation, sustainable development and logistical support for research, monitoring and education."),
    ("Ramsar Convention", "The Convention on Wetlands was signed at Ramsar in 1971; MoEFCC's retrievable page states that India became a party on 1 February 1982."),
    ("Wise use", "Ramsar wise use means maintaining wetland ecological character through ecosystem approaches within sustainable development, not imposing universal no-use preservation."),
    ("Ramsar designation", "A Ramsar Site is a wetland placed on the List of Wetlands of International Importance; the international designation does not itself create a new Indian statutory land category."),
    ("Ramsar criteria boundary", "The Ramsar framework uses multiple ecological criteria and a site needs to meet at least one applicable criterion; no numerical threshold is used here without readable official text."),
    ("Ecological character", "Ecological character is the combination of ecosystem components, processes and benefits or services that defines a wetland at a stated time."),
    ("Montreux Record", "The Montreux Record flags listed wetlands where ecological character has changed, is changing or is likely to change because of human interference; it is not a delisting or prestige list."),
    ("Montreux status discipline", "A site's current Montreux inclusion or removal must be checked against the live Ramsar record; historical examples must not be converted into an undated current claim."),
    ("Wetlands Rules 2017", "India's Wetlands Conservation and Management Rules 2017 operate under the Environment Protection Act and provide the domestic regulatory layer separate from Ramsar designation."),
    ("State Wetland Authorities", "State or Union Territory Wetland Authorities identify, notify, plan and regulate wetlands under the domestic framework; Ramsar visibility does not replace their work."),
    ("NPCA transition", "The owner records that the National Wetland Conservation Programme and National Lake Conservation Plan merged into NPCA in 2013; programme labels must match the question's time point."),
    ("Overlapping designations", "One landscape can contain a National Park, Tiger Reserve, Biosphere Reserve and Ramsar Site, but every designation retains its own legal or institutional function and boundary."),
    ("Designation and implementation", "National notification, UNESCO recognition, Ramsar listing, domestic wetland notification and an implemented management plan are separate milestones."),
    ("Live count boundary", "The retrievable MoEFCC page displayed 99 Indian Ramsar sites on 2026-09-03, while other official discovery results differed; no latest count or area was asserted."),
    ("Audited PYQ boundary", "Verified demands cover wise use, Agasthyamala components, Wetlands Rules, urban water-body reclamation, wetland locations and the older NWCP label; objective keys are not inferred."),
]

TRAPS = [
    "Do not equate national Biosphere Reserve designation with UNESCO World Network status.",
    "Do not treat the core, buffer and transition zones as equally restrictive.",
    "Do not describe a transition zone as an uninhabited strict-protection zone.",
    "Do not reduce the biosphere model to conservation while omitting development and logistics.",
    "Do not call every wetland a Ramsar Site.",
    "Do not interpret wise use as unrestricted exploitation or universal prohibition.",
    "Do not treat Ramsar listing as a new Indian statutory land category.",
    "Do not quote a Ramsar criterion threshold from an unreadable or stale source.",
    "Do not equate ecological character with a species list alone.",
    "Do not call the Montreux Record a delisting or honour roll.",
    "Do not state a current Montreux entry without checking the live record.",
    "Do not treat the Wetlands Rules and Ramsar Convention as the same instrument.",
    "Do not infer management success from designation count.",
    "Do not merge overlapping designations or their boundaries.",
    "Do not present an undated site count as current.",
]

SESSION_TITLES = [
    "National designation and UNESCO World Network status",
    "Core zone",
    "Buffer zone",
    "Transition zone",
    "Three biosphere functions",
    "Ramsar Convention and wise use",
    "Ramsar designation",
    "Ramsar criteria boundary",
    "Ecological character",
    "Montreux Record",
    "Montreux status and Wetlands Rules",
    "State Wetland Authorities",
    "NPCA historical transition",
    "Overlapping designations and implementation milestones",
    "Live count and audited PYQ boundary",
]

ANSWER_ROUTES = [
    "Open by separating national declaration from UNESCO World Network inclusion.",
    "Define core protection and name the underlying domestic legal layer.",
    "Use conservation-compatible research and managed activity.",
    "Explain livelihoods and cooperation without calling the zone unregulated.",
    "Organise the model around conservation, development and logistical support.",
    "State the treaty vintage, India party date and wise-use principle.",
    "Separate international listing from domestic legal notification.",
    "Describe criterion families without inventing unreadable thresholds.",
    "Define ecological character through components, processes and benefits.",
    "Use the Record as an ecological-change accountability mechanism.",
    "Check current status and then move to the domestic Wetlands Rules.",
    "Assign identification, notification and management to the competent authority.",
    "Keep historical NWCP wording separate from the present NPCA framework.",
    "Map each overlapping designation and implementation milestone separately.",
    "Close with dated counts, verified demands and no inferred objective key.",
]

PANELS = [
    panel("Two-step biosphere status", "process-flow", [
        "INDIAN NATIONAL DESIGNATION -> Biosphere Reserve planning status",
        "SEPARATE NOMINATION -> UNESCO MAB process",
        "WORLD NETWORK INCLUSION -> international recognition",
        "NOT AUTOMATIC -> national status may exist without UNESCO status",
        "RULE -> always name which status and year is meant",
    ], [FACTS[0][0], FACTS[1][0]]),
    panel("Core buffer transition", "nested-zones", [
        "CORE -> long-term conservation and minimal disturbance",
        "BUFFER -> research, monitoring, education and compatible use",
        "TRANSITION -> settlements, livelihoods and sustainable development",
        "INTERACTION -> zones support one landscape strategy",
        "CAUTION -> zonation is not three equal legal protection tiers",
    ], [FACTS[2][0], FACTS[3][0], FACTS[4][0]]),
    panel("Biosphere function triangle", "triangle", [
        "CONSERVATION -> landscapes, ecosystems, species and genetic variation",
        "DEVELOPMENT -> sustainable human and economic activity",
        "LOGISTICAL SUPPORT -> research, monitoring, education and training",
        "ZONATION -> assigns compatible functions across space",
        "VERDICT -> effectiveness depends on domestic implementation",
    ], [FACTS[5][0]]),
    panel("Ramsar three-pillar rail", "process-flow", [
        "WISE USE -> all wetlands",
        "RAMSAR LIST -> designate suitable wetlands and manage them",
        "COOPERATION -> transboundary wetlands, systems and shared species",
        "INDIA PARTY DATE -> 1 February 1982 on MoEFCC page",
        "RULE -> treaty obligation is broader than listed sites alone",
    ], [FACTS[6][0], FACTS[7][0]]),
    panel("Ramsar status firewall", "comparison-table", [
        "RAMSAR SITE -> international Wetland of Importance listing",
        "DOMESTIC NOTIFICATION -> Indian legal instrument",
        "MANAGEMENT PLAN -> operational commitments and actions",
        "IMPLEMENTATION -> monitored ecological outcome",
        "RULE -> one milestone never proves the next",
    ], [FACTS[8][0], FACTS[17][0]]),
    panel("Criteria discipline", "decision-gate", [
        "SITE EVIDENCE -> representative type, species or ecological functions",
        "TEST -> applicable Ramsar criteria",
        "AT LEAST ONE -> can support nomination",
        "THRESHOLD -> use only readable official criterion text",
        "NO SHORTCUT -> designation cannot be inferred from importance alone",
    ], [FACTS[9][0]]),
    panel("Ecological character map", "system-map", [
        "COMPONENTS -> biotic and abiotic features",
        "PROCESSES -> hydrology, nutrient and ecological interactions",
        "BENEFITS OR SERVICES -> functions valued by people and ecosystems",
        "BASELINE -> stated time and site boundary",
        "CHANGE -> requires evidence, not a generic degradation label",
    ], [FACTS[10][0]]),
    panel("Montreux accountability loop", "feedback-loop", [
        "RAMSAR-LISTED SITE -> ecological character concern",
        "MONTREUX RECORD -> change occurred, is occurring or is likely",
        "ATTENTION AND ADVICE -> corrective management route",
        "REVIEW -> current record can change",
        "RULE -> Record status is neither delisting nor permanent stigma",
    ], [FACTS[11][0], FACTS[12][0]]),
    panel("International and domestic layers", "layered-rail", [
        "RAMSAR CONVENTION -> international wise-use framework",
        "RAMSAR DESIGNATION -> site recognition and reporting",
        "WETLANDS RULES 2017 -> domestic regulatory framework",
        "STATE WETLAND AUTHORITY -> identification and implementation",
        "NPCA -> programme support; not the Ramsar designation itself",
    ], [FACTS[13][0], FACTS[14][0], FACTS[15][0]]),
    panel("Programme time-point timeline", "timeline", [
        "OLDER DEMAND -> National Wetland Conservation Programme",
        "PARALLEL PROGRAMME -> National Lake Conservation Plan",
        "2013 OWNER ROUTE -> merger into NPCA",
        "CURRENT ANSWER -> use NPCA with Wetlands Rules framework",
        "CAUTION -> do not rewrite a historical PYQ's original programme label",
    ], [FACTS[15][0], FACTS[19][0]]),
    panel("Overlapping designation stack", "layered-map", [
        "NATIONAL PARK OR SANCTUARY -> domestic wildlife-law status",
        "TIGER RESERVE -> species-management overlay",
        "BIOSPHERE RESERVE -> zoned landscape designation",
        "RAMSAR SITE -> wetland international listing",
        "RULE -> map functions and boundaries separately",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("Evidence and answer spine", "answer-spine", [
        "CLASSIFY -> biosphere status, zone, Ramsar status or domestic wetland law",
        "FIX -> site boundary, designation date and competent authority",
        "ANALYSE -> ecological character, wise use and livelihood mechanism",
        "VERIFY -> current count and Montreux status before citing",
        "CONCLUDE -> designation matters only through implemented management",
    ], [FACTS[12][0], FACTS[18][0], FACTS[19][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2018", "GS-III Q7",
        "Wetlands and the Ramsar wise-use concept with Indian examples.",
        "Routed from an audited official-paper ledger; model answer independently authored.",
        [6, 7, 8, 13, 14],
    ),
    common.make_pyq_solution(
        FACTS, "2021", "GS-I Q6",
        "Environmental implications of reclaiming water bodies for urban land use.",
        "Routed from an audited official-paper ledger; model answer independently authored.",
        [10, 13, 14, 17],
    ),
    common.make_pyq_solution(
        FACTS, "2023", "GS-III Q17",
        "National Wetland Conservation Programme and India's Ramsar sites.",
        "Routed from an audited official-paper ledger; model answer independently authored.",
        [7, 8, 13, 15, 17],
    ),
]

TOPIC_07 = common.topic(
    7,
    "Biosphere Reserves and Ramsar Sites",
    "07_Biosphere-Reserves-and-Ramsar-Sites",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-07_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish national Biosphere Reserve designation from UNESCO recognition.", [0, 1, 2, 3, 4]),
        (10, "Explain the Ramsar wise-use principle.", [6, 7, 8]),
        (15, "Explain ecological character and the Montreux Record.", [10, 11, 12]),
        (15, "Distinguish Ramsar designation from India's Wetlands Rules framework.", [8, 13, 14, 17]),
        (20, "Assess Biosphere Reserves as zoned conservation-development landscapes.", [2, 3, 4, 5, 16]),
        (20, "India's wetland designation growth must be matched by implementation. Examine.", [7, 10, 12, 14, 15, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "national designation", "UNESCO World Network", "core zone", "buffer zone",
        "transition zone", "conservation", "sustainable development",
        "logistical support", "Ramsar Convention", "1 February 1982", "wise use",
        "Ramsar Site", "ecological character", "Montreux Record",
        "Wetlands Rules 2017", "State Wetland Authorities", "NPCA",
        "National Wetland Conservation Programme", "management plan",
        "designation count",
    ],
    (
        "Audited ledgers route the 2018 Ramsar wise-use Mains demand, 2021 urban "
        "water-body reclamation, 2023 NWCP and Ramsar analysis, and objective "
        "demands on Agasthyamala, Wetlands Rules and site locations. Mains models "
        "are independently authored; no objective key, current count, area, "
        "designation date or Montreux status is inferred."
    ),
    PYQ_SOLUTIONS,
    BIOSPHERE_RAMSAR_LIVE_SOURCE_ATTEMPTS,
    (
        "MoEFCC's Ramsar page was substantively retrieved on 2026-09-03 for the "
        "1971 treaty, India's 1 February 1982 party date and three pillars. Its "
        "displayed count was not treated as latest because official discovery "
        "results differed. Ramsar and UNESCO pages returned HTTP 403 or a title-"
        "only stub, while official PDFs were opaque raw bytes. No current count, "
        "area, UNESCO list, Montreux status or criterion threshold was imported."
    ),
    extra=[
        "basic/06_Protected-Area-Network-India.md",
        "basic/14_Water-Pollution-and-River-Cleaning-Missions.md",
        "basic/22_Multilateral-Environmental-Conventions-CBD-Basel-Stockholm-Montreal.md",
        "basic/28_Species-and-Current-Affairs-Tracker.md",
    ],
    register_headings=(
        "BIOSPHERE STATUS, ZONATION AND RAMSAR LAYER MAP",
        "WISE-USE, MONTREUX AND DESIGNATION TRAPS",
        "DESIGNATION-TO-IMPLEMENTATION ANSWER SPINE",
        "LIVE COUNT, UNESCO, RAMSAR AND DOMESTIC-LAW BOUNDARY",
    ),
    register_answer_spine=[
        "IDENTIFY NATIONAL BIOSPHERE, UNESCO, RAMSAR OR DOMESTIC WETLAND STATUS",
        "MAP CORE, BUFFER AND TRANSITION OR THE RAMSAR WISE-USE ROUTE",
        "FIX THE SITE BOUNDARY, DESIGNATION DATE AND COMPETENT AUTHORITY",
        "SEPARATE ECOLOGICAL CHARACTER FROM A SPECIES LIST",
        "USE MONTREUX ONLY WITH A CURRENT OFFICIAL STATUS CHECK",
        "LINK RAMSAR TO WETLANDS RULES, STATE AUTHORITIES AND NPCA",
        "CONCLUDE WITH IMPLEMENTED MANAGEMENT, NOT DESIGNATION COUNT",
    ],
)
