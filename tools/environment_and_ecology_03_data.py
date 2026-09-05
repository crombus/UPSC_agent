"""Authored data for Environment and Ecology learner-v2 Topic 03."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    (
        "Ecological succession",
        "Ecological succession is directional change in community composition "
        "and ecosystem structure through time after formation or disturbance; "
        "directional does not mean deterministic, irreversible or forest-bound.",
    ),
    (
        "Primary succession",
        "Primary succession begins on a substrate without a developed soil, such "
        "as newly exposed rock; soil formation and biological colonisation are "
        "part of the process, but no universal completion timeline is asserted.",
    ),
    (
        "Secondary succession",
        "Secondary succession follows disturbance where soil and often propagules "
        "or a seed bank remain; it commonly proceeds faster than primary "
        "succession because the substrate and biological legacies differ.",
    ),
    (
        "Pioneer organisms",
        "Pioneer organisms tolerate the starting substrate and begin modifying "
        "it; lichens are the classic routed example for exposed surfaces without "
        "soil, but pioneer identity depends on the actual substrate.",
    ),
    (
        "Sere and seral stage",
        "A sere is the complete succession sequence at a site, while a seral "
        "stage is one intermediate community within that sequence; the whole "
        "sequence and one phase are not synonyms.",
    ),
    (
        "Named seres",
        "Lithosere begins on rock, psammosere on sand, halosere in saline "
        "conditions, hydrosere in fresh water and xerosere on dry substrate; "
        "these names identify starting conditions, not guaranteed endpoints.",
    ),
    (
        "Hydrarch and xerarch direction",
        "Hydrarch succession begins in water and xerarch succession begins in "
        "dry conditions; both may move toward more mesic conditions under a "
        "given regional setting without following one universal sequence.",
    ),
    (
        "Autogenic mechanism",
        "Autogenic succession is driven by changes organisms themselves produce, "
        "such as litter accumulation, soil development, shading or altered "
        "microclimate that changes later establishment conditions.",
    ),
    (
        "Allogenic mechanism",
        "Allogenic succession is driven by external forces such as flooding, "
        "sediment deposition, fire regime, erosion, climate variation or land "
        "use; it must not be attributed to community modification alone.",
    ),
    (
        "Facilitation, inhibition and tolerance",
        "Facilitation makes later establishment easier, inhibition delays other "
        "colonists, and tolerance allows later species to establish without "
        "requiring early species to improve conditions; no one model governs every sere.",
    ),
    (
        "Classical climax and modern qualification",
        "The classical climax model emphasises a relatively stable community "
        "under regional climate, while modern ecology recognises disturbance "
        "history, species availability and chance can produce multiple plausible states.",
    ),
    (
        "Disturbance and reset",
        "Fire, storm, cultivation, grazing or land conversion can redirect or "
        "reset succession; a relatively stable community remains dynamic and is "
        "not a permanently fixed endpoint.",
    ),
    (
        "Restoration staging",
        "Restoration should match substrate and stage: stabilisation and soil "
        "building may precede later structural complexity, so planting late-stage "
        "trees directly on hostile mine spoil is not automatically restoration.",
    ),
    (
        "Biome versus ecosystem and habitat",
        "A biome is a broad regional ecological category associated with climate "
        "and characteristic vegetation, an ecosystem is a bounded functional "
        "unit, and habitat is the physical place used by a species.",
    ),
    (
        "Climate and local biome modifiers",
        "Temperature and precipitation organise broad biome patterns, while "
        "soil, fire, herbivory, topography and land-use history modify local "
        "vegetation; climate is a broad control, not a complete deterministic map.",
    ),
    (
        "Biome boundaries and ecotones",
        "Biome boundaries are gradients and transition zones rather than exact "
        "lines; maps generalise spatial patterns and cannot establish a sharp "
        "ecological border at every local site.",
    ),
    (
        "Indian biome diversity",
        "The owners use tropical wet evergreen, dry deciduous, thorn or desert "
        "and montane temperate or alpine settings as Indian examples; these are "
        "broad ecological categories, not a substitute for legal forest classification.",
    ),
    (
        "Open Natural Ecosystems",
        "Grasslands, savannas, scrublands, ravines and rocky outcrops can be "
        "natural open ecosystems rather than degraded forests awaiting trees; "
        "their ecological status must be assessed before afforestation.",
    ),
    (
        "Administrative, legal and ecological labels",
        "Wasteland is an administrative or revenue label, forest may be a legal "
        "category, and grassland or biome is an ecological category; converting "
        "one label into another without evidence creates a category error.",
    ),
    (
        "PYQ, monitoring and current boundary",
        "The 2021 routed objective demand on pioneers belongs in Basic practice, "
        "and the 2024 essay phrase on forests and deserts is used only as a "
        "qualified restoration argument; forest-cover change cannot prove successional stage.",
    ),
]

TRAPS = [
    "Do not define succession as any random change in species composition.",
    "Do not assign a universal duration to primary succession.",
    "Do not say every disturbed site undergoes primary succession.",
    "Do not assume lichens pioneer every substrate.",
    "Do not use sere and seral stage as synonyms.",
    "Do not let a named sere imply a guaranteed climax.",
    "Do not treat hydrarch as movement toward a wetter endpoint.",
    "Do not call an externally imposed change autogenic.",
    "Do not call community-driven soil or shade change allogenic.",
    "Do not force every succession pathway into facilitation alone.",
    "Do not present climatic climax as one inevitable permanent endpoint.",
    "Do not treat disturbance only as failure; it can structure ecosystems.",
    "Do not equate tree planting with completed ecological restoration.",
    "Do not use biome, ecosystem and habitat interchangeably.",
    "Do not explain every local vegetation pattern by climate alone.",
    "Do not draw biome borders as precise ecological lines.",
    "Do not equate broad biome labels with statutory forest categories.",
    "Do not describe every natural grassland or savanna as degraded forest.",
    "Do not turn an administrative wasteland label into an ecological diagnosis.",
    "Do not infer successional stage or essay determinism from canopy-cover data.",
]

SESSION_TITLES = [
    "Succession as directional but contingent change",
    "Secondary succession and biological legacies",
    "Pioneer organisms and substrate",
    "Sere, seral stages and named seres",
    "Hydrarch direction and autogenic mechanism",
    "Allogenic external forcing",
    "Facilitation, inhibition and tolerance",
    "Climax theory and multiple stable states",
    "Disturbance, reset and dynamic stability",
    "Restoration staging and biome scale",
    "Climate controls and local modifiers",
    "Biome boundaries and ecotones",
    "Indian biome diversity and open ecosystems",
    "Administrative, legal and ecological labels",
    "PYQ, monitoring and current boundary",
]

ANSWER_ROUTES = [
    "Define succession as a temporal community trajectory and qualify its contingency.",
    "Use retained soil and propagules to explain faster secondary recovery.",
    "Match the pioneer to the starting substrate rather than memorising one organism.",
    "Name the entire sere, the individual seral stage and the starting substrate separately.",
    "State the initial moisture condition and show how organisms alter later establishment.",
    "Identify the external disturbance or material input driving the trajectory.",
    "Use the three models as alternatives that can operate in different contexts.",
    "Present climax as relatively stable but disturbance- and history-dependent.",
    "Name the disturbance regime and the state variable it changes.",
    "Sequence restoration and fix spatial scale before using biome, ecosystem or habitat.",
    "Use climate for the broad pattern and local modifiers for deviations.",
    "Treat biome boundaries as gradients rather than exact site-level lines.",
    "Use Indian biome examples while protecting natural open ecosystems from default afforestation.",
    "Separate administrative, legal and ecological labels.",
    "Close with monitoring limits, current evidence and verified PYQ routes.",
]

PANELS = [
    panel("Succession decision tree", "hierarchy", [
        "START -> newly exposed substrate or disturbed former community",
        "NO DEVELOPED SOIL -> primary succession pathway",
        "SOIL AND BIOLOGICAL LEGACIES REMAIN -> secondary succession pathway",
        "DRIVERS -> autogenic community change plus allogenic external forcing",
        "OUTCOME -> contingent trajectory, not one guaranteed endpoint",
    ], [FACTS[0][0], FACTS[1][0], FACTS[2][0]]),
    panel("Primary succession rail", "process-flow", [
        "BARE OR NEW SUBSTRATE -> pioneer establishment",
        "WEATHERING AND ORGANIC INPUT -> initial soil development",
        "HERBS OR OTHER COLONISTS -> more cover and resource capture",
        "LATER COMMUNITIES -> increasing structural complexity where conditions permit",
        "LIMIT -> no universal species list or completion time",
    ], [FACTS[1][0], FACTS[3][0]]),
    panel("Secondary succession rail", "process-flow", [
        "DISTURBANCE -> prior vegetation reduced or removed",
        "SOIL, ROOTS, SEEDS OR MICROBES REMAIN -> biological legacy",
        "RAPID COLONISERS -> early recovery",
        "COMPETITION AND RECRUITMENT -> later community change",
        "LIMIT -> faster than primary does not mean instant or identical recovery",
    ], [FACTS[2][0], FACTS[11][0]]),
    panel("Sere vocabulary map", "matrix", [
        "SERE -> complete sequence at one site",
        "SERAL STAGE -> one community within the sequence",
        "LITHOSERE -> rock   PSAMMOSERE -> sand",
        "HALOSERE -> saline   HYDROSERE -> fresh water",
        "XEROSERE -> dry substrate; names identify starts, not fixed ends",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("Hydrarch and xerarch comparison", "comparison-table", [
        "HYDRARCH -> begins in water or very wet substrate",
        "XERARCH -> begins under dry conditions",
        "BOTH -> may trend toward more mesic regional conditions",
        "PATH -> depends on sediment, soil, colonists and disturbance",
        "CAUTION -> convergence is not one universal sequence",
    ], [FACTS[6][0]]),
    panel("Mechanism fork", "comparison", [
        "AUTOGENIC -> organisms alter litter, soil, shade or microclimate",
        "ALLOGENIC -> flood, fire, erosion, deposition, climate or land use acts externally",
        "FACILITATION -> early species improve later establishment",
        "INHIBITION OR TOLERANCE -> alternative replacement mechanisms",
        "RULE -> identify the driver before naming the mechanism",
    ], [FACTS[7][0], FACTS[8][0], FACTS[9][0]]),
    panel("Climax theory pressure test", "dialectic", [
        "CLASSICAL CLAIM -> regional climate favours a relatively stable climax",
        "PRESSURE -> disturbance history and species arrival differ among sites",
        "MODERN READING -> multiple plausible stable states can occur",
        "DISTURBANCE -> redirects or resets trajectories",
        "VERDICT -> climate constrains but does not uniquely script every endpoint",
    ], [FACTS[10][0], FACTS[11][0]]),
    panel("Restoration staging ladder", "hierarchy", [
        "1 STABILISE -> erosion, substrate and hydrology",
        "2 REBUILD FUNCTION -> organic matter, soil biota and nutrient processes",
        "3 ENABLE NATIVE RECRUITMENT -> propagules and suitable microclimate",
        "4 RECOVER STRUCTURE -> composition, layering and connectivity",
        "5 MONITOR -> function and trajectory, not planting count alone",
    ], [FACTS[12][0]]),
    panel("Scale vocabulary", "comparison-table", [
        "HABITAT -> place used by a species",
        "ECOSYSTEM -> bounded interacting biotic and abiotic functional unit",
        "BIOME -> broad regional ecological category",
        "FOREST LEGAL CATEGORY -> status under applicable law or interpretation",
        "RULE -> one term cannot silently substitute for another",
    ], [FACTS[13][0], FACTS[18][0]]),
    panel("Biome control matrix", "matrix", [
        "BROAD CLIMATE -> temperature and precipitation pattern",
        "SOIL AND TOPOGRAPHY -> local water and nutrient conditions",
        "FIRE AND HERBIVORY -> maintain or redirect open vegetation",
        "LAND-USE HISTORY -> modifies present composition",
        "BOUNDARY -> biome maps are gradients, not exact site-level lines",
    ], [FACTS[14][0], FACTS[15][0]]),
    panel("Open ecosystem firewall", "evidence-table", [
        "GRASSLAND, SAVANNA, SCRUB -> may be natural ecological states",
        "WASTELAND -> administrative or revenue label",
        "FOREST -> legal category in the relevant context",
        "PLANTATION -> land-cover intervention, not proof of restored biome",
        "DECISION -> assess native biome before afforestation",
    ], [FACTS[17][0], FACTS[18][0]]),
    panel("PYQ and monitoring boundary", "answer-spine", [
        "2021 ROUTE -> pioneers surviving on surfaces without soil",
        "2024 ESSAY -> forests and deserts used as a qualified ecological warning",
        "FOREST COVER -> canopy trend, not successional-stage proof",
        "RESTORATION CLAIM -> needs repeated composition, soil and function evidence",
        "LIVE STUB -> adds no succession timeline, biome range or status",
    ], [FACTS[19][0]]),
]


TOPIC_03 = common.topic(
    3,
    "Ecological Succession and Biomes",
    "03_Ecological-Succession-and-Biomes",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-03_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Differentiate primary and secondary succession using the soil and biological-legacy test.", [1, 2, 3]),
        (10, "Distinguish autogenic and allogenic succession with mechanisms.", [7, 8, 9]),
        (15, "Explain why the classical climax concept requires qualification in modern ecology.", [0, 10, 11]),
        (15, "How should succession theory guide mine-spoil or degraded-land restoration?", [1, 3, 12, 19]),
        (20, "Afforestation is not always ecological restoration. Analyse with reference to biomes and Open Natural Ecosystems.", [13, 14, 16, 17, 18]),
        (20, "Use succession and biome concepts to critically examine the proposition that forests precede civilizations and deserts follow them.", [10, 11, 12, 17, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "primary succession",
        "secondary succession",
        "pioneer",
        "sere",
        "seral stage",
        "lithosere",
        "hydrosere",
        "autogenic",
        "allogenic",
        "facilitation",
        "inhibition",
        "tolerance",
        "climax",
        "multiple stable states",
        "biome",
        "ecosystem",
        "habitat",
        "Open Natural Ecosystems",
        "wasteland",
    ],
    (
        "The audited 2021 Prelims route on pioneer organisms surviving on "
        "surfaces without soil is retained in Basic sessions and objective "
        "practice without an inferred option. The 2024 Essay phrase 'Forests "
        "precede civilizations and deserts follow them' is carried as a verified "
        "demand and solved only through a qualified original framework that "
        "rejects ecological determinism."
    ),
    [
        common.make_pyq_solution(
            FACTS,
            "2024",
            "Essay, Section A",
            "Forests precede civilizations and deserts follow them.",
            "Verified essay demand; model framework is original and does not claim an official solution.",
            [10, 11, 12, 17, 18, 19],
        )
    ],
    LIVE_SOURCE_ATTEMPTS,
    (
        "No succession duration, climax timeline, biome range or restoration "
        "outcome was imported from live checks on 2026-09-03. The FSI page was a "
        "contact-only stub, the MoEFCC page was unrelated, the IPCC page supplied "
        "only a title and PIB returned HTTP 403. CBD Target 3 guidance was "
        "substantive but addresses area-based conservation and does not determine "
        "a site's successional stage or native biome."
    ),
)
