"""Authored data for Environment and Ecology learner-v2 Topic 01."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    (
        "Ecosystem as a bounded functional unit",
        "The owner defines an ecosystem as interacting biotic communities and "
        "their abiotic physical and chemical environment exchanging energy and "
        "matter; A. G. Tansley coined the term in 1935, and every claim must "
        "state the practical system boundary rather than treat all nature as one unit.",
    ),
    (
        "Biotic and abiotic structure",
        "Biotic structure comprises producers, consumers, decomposers and "
        "detritivores, while abiotic structure comprises climatic, edaphic, "
        "water and nutrient conditions; structure identifies what is present "
        "before function explains what those components do.",
    ),
    (
        "Producer entry point",
        "Producers introduce usable chemical energy through photosynthesis or "
        "chemosynthesis; green plants are not the only producers, and the "
        "source does not support treating consumers or decomposers as an energy entry point.",
    ),
    (
        "Consumers and trophic position",
        "Consumers obtain energy from other organisms and may occupy more than "
        "one trophic position when omnivory occurs, so trophic level is a "
        "feeding relation within the stated web rather than a permanent taxonomic rank.",
    ),
    (
        "Detritivore and decomposer distinction",
        "Detritivores physically fragment dead organic material, whereas "
        "microbial decomposers such as bacteria and fungi chemically break it "
        "down and release nutrients; the two roles cooperate but are not synonyms.",
    ),
    (
        "Energy movement versus matter cycling",
        "Energy passes one way through trophic transfers and dissipates as heat, "
        "whereas chemical matter returns through decomposition and uptake; "
        "energy is not recycled merely because nutrients are.",
    ),
    (
        "Food chain versus food web",
        "A food chain is one linear feeding route, while a food web is the "
        "network of interconnected chains; alternative links can support "
        "resilience, but a web does not make every disturbance harmless.",
    ),
    (
        "Habitat, niche and niche dimensions",
        "Habitat is the physical place a species occupies, while niche is its "
        "functional resource use and interactions; the owner separates habitat, "
        "trophic or food, and reproductive dimensions of niche.",
    ),
    (
        "Ecotone and edge effect",
        "An ecotone is a transition zone of variable width between adjoining "
        "ecosystems and may show an edge effect, but the higher density or "
        "variety often associated with an edge is a pattern, not the definition of the zone.",
    ),
    (
        "Stratification and resource partitioning",
        "Vertical layering such as canopy, understorey, shrub and forest floor "
        "creates different microhabitats and niches; greater layering may "
        "support coexistence without proving universal stability or biodiversity.",
    ),
    (
        "Gross and net primary productivity",
        "Gross primary productivity is total producer fixation over time, while "
        "net primary productivity is gross primary productivity minus producer "
        "respiration and is the production available for growth and consumers.",
    ),
    (
        "Standing crop and standing state",
        "Standing crop is living material present at a stated time and is often "
        "expressed as biomass or number, whereas standing state is the quantity "
        "of an abiotic nutrient in the ecosystem; neither is a productivity rate.",
    ),
    (
        "Stability and resilience",
        "Stability or resistance describes limited change under disturbance, "
        "whereas resilience describes recovery after disturbance; a uniform "
        "plantation can appear stable yet remain poorly resilient to a specific shock.",
    ),
    (
        "Ecosystem services and NCP",
        "The owner uses provisioning, regulating, supporting and cultural "
        "services as the Millennium Ecosystem Assessment vocabulary, while "
        "IPBES Nature's Contributions to People broadens valuation to relational "
        "and indigenous or local-knowledge values.",
    ),
    (
        "Carrying capacity",
        "Carrying capacity is the population or project load an ecosystem can "
        "sustain over time without eroding regenerative functions; it is a "
        "conditional threshold shaped by consumption, technology and governance, not a fixed headcount.",
    ),
    (
        "Interaction and coevolution PYQ routes",
        "The Basic owner carries routed objective concepts on parasitoids, fig "
        "pollination, symbiosis and fungus cultivation; these are interaction "
        "types within ecological networks, and no official answer option is inferred.",
    ),
    (
        "Ocean producers, filter feeders and detritivores",
        "The audited routes require primary producers in ocean food chains, "
        "filter-feeding organisms and detritivore function to remain in Basic "
        "practice; each is a functional role and not a claim about one universal species list.",
    ),
    (
        "Wetland filtering as structure-function evidence",
        "Wetland vegetation, sediments and microbial processes can retain or "
        "transform pollutants and support flood regulation, but a routed wetland "
        "function does not justify an unsupported universal removal percentage.",
    ),
    (
        "Extent versus ecosystem quality",
        "Forest or tree-cover extent is a canopy measure and cannot by itself "
        "establish native composition, age structure, biodiversity, resilience "
        "or ecosystem functioning; extent and ecological quality are different claims.",
    ),
    (
        "Institution and evidence boundary",
        "MoEFCC, WII, BSI, ZSI and FSI occupy different policy, research, "
        "taxonomic and monitoring roles; the owner and audited routing ledgers "
        "remain primary, while thin live pages and unavailable answer keys add no claim.",
    ),
]

TRAPS = [
    "Do not discuss an ecosystem without fixing a defensible spatial and functional boundary.",
    "Do not treat biotic structure and ecosystem function as interchangeable descriptions.",
    "Do not describe green plants as the only possible producers.",
    "Do not turn trophic position into a permanent taxonomic rank.",
    "Do not use detritivore and decomposer as synonyms.",
    "Do not say energy cycles because nutrients cycle.",
    "Do not use food chain and food web interchangeably.",
    "Do not collapse habitat into niche or omit niche dimensions.",
    "Do not define an ecotone merely by a claimed increase in richness.",
    "Do not infer stability or biodiversity from stratification alone.",
    "Do not confuse gross productivity, net productivity and standing biomass.",
    "Do not confuse standing crop with standing state or either with a rate.",
    "Do not equate resistance with recovery.",
    "Do not reduce ecosystem services to marketable provisioning benefits.",
    "Do not quote carrying capacity as a timeless fixed number.",
    "Do not infer official PYQ answers from a routed concept.",
    "Do not treat every named organism as occupying one universal ecological role.",
    "Do not attach an invented filtration percentage to a wetland function.",
    "Do not treat canopy extent as proof of ecological quality.",
    "Do not upgrade a thin live landing page into current ecological evidence.",
]

SESSION_TITLES = [
    "System boundary and the structure-function question",
    "Biotic and abiotic components",
    "Producer entry and autotrophy",
    "Consumers, omnivory and trophic position",
    "Detritivores, decomposers and nutrient return",
    "Energy flow and matter cycling",
    "Food chains, food webs and resilience",
    "Habitat, niche and competitive separation",
    "Ecotones, edge effects and transition zones",
    "Stratification and niche differentiation",
    "Gross productivity, net productivity and rates",
    "Standing crop versus standing state",
    "Resistance, resilience and ecosystem services",
    "Carrying capacity and routed interaction concepts",
    "Wetland function, extent-quality limits and institutions",
]

ANSWER_ROUTES = [
    "Open by fixing the ecosystem boundary and then pair each structural component with its function.",
    "Use a two-column biotic-abiotic frame before tracing any process.",
    "Identify the actual energy entry route before discussing trophic transfer.",
    "State the feeding relation and allow for omnivory rather than assigning a permanent rank.",
    "Trace fragmentation, chemical breakdown and nutrient release as distinct steps.",
    "Write the decisive contrast: energy is dissipative, matter is recyclable.",
    "Use a web to explain alternative pathways, then qualify the resilience claim.",
    "Define habitat as place and niche as role before applying competition or partitioning.",
    "Separate the transition zone from the possible edge pattern.",
    "Link layering to microclimate and resource partitioning without claiming an automatic outcome.",
    "Write GPP, producer respiration and NPP in the correct gross-to-net relation.",
    "Name whether the question measures living stock, abiotic nutrient stock or production rate.",
    "Distinguish resistance, recovery and the service category actually affected.",
    "Treat carrying capacity as conditional and route verified PYQ concepts without inventing keys.",
    "Close by separating monitored extent, ecological quality and institutional evidence.",
]

PANELS = [
    panel("Ecosystem boundary card", "root-axes", [
        "BOUNDARY -> state the pond, forest patch, wetland or landscape being analysed",
        "ABIOTIC -> climate, water, soil, minerals and topography inside that boundary",
        "BIOTIC -> producers, consumers, detritivores and microbial decomposers",
        "FUNCTION -> energy transfer, matter cycling, productivity and recovery",
        "RULE -> a boundary is analytical; it must match the question and evidence",
    ], [FACTS[0][0], FACTS[1][0]]),
    panel("Energy and matter split", "process-flow", [
        "SOLAR OR CHEMICAL INPUT -> producer fixation -> consumer transfer",
        "AT EACH TRANSFER -> respiration and heat dissipation reduce usable energy",
        "DEAD ORGANIC MATTER -> fragmentation -> microbial decomposition",
        "RELEASED NUTRIENTS -> abiotic pool -> producer uptake",
        "VERDICT -> energy moves one way; matter can cycle",
    ], [FACTS[2][0], FACTS[4][0], FACTS[5][0]]),
    panel("Functional guild ladder", "hierarchy", [
        "PRODUCERS -> create organic matter from inorganic inputs",
        "PRIMARY CONSUMERS -> feed directly on producers",
        "HIGHER CONSUMERS -> feed through one or more trophic routes",
        "DETRITIVORES -> fragment dead material",
        "DECOMPOSERS -> chemically release nutrients",
    ], [FACTS[2][0], FACTS[3][0], FACTS[4][0]]),
    panel("Chain and web comparison", "comparison-table", [
        "FOOD CHAIN -> one selected linear route",
        "FOOD WEB -> connected set of chains within the same boundary",
        "ALTERNATIVE LINKS -> may reduce dependence on one route",
        "OMNIVORY -> one organism may feed across trophic positions",
        "LIMIT -> connectivity does not immunise a system against every disturbance",
    ], [FACTS[3][0], FACTS[6][0]]),
    panel("Habitat and niche matrix", "matrix", [
        "HABITAT -> physical address",
        "HABITAT NICHE -> where within that address the organism operates",
        "TROPHIC NICHE -> resources and feeding relations",
        "REPRODUCTIVE NICHE -> breeding requirements and timing",
        "RULE -> overlap in place does not prove identical functional niches",
    ], [FACTS[7][0]]),
    panel("Ecotone logic", "path-consequence", [
        "ECOSYSTEM A -> transition zone of variable width -> ECOSYSTEM B",
        "OVERLAPPING CONDITIONS -> species from both sides may occur",
        "NEW EDGE CONDITIONS -> some additional specialists may occur",
        "COMPETITION AND TENSION -> the zone is not automatically benign",
        "EDGE EFFECT -> possible density or variety pattern, not the definition",
    ], [FACTS[8][0]]),
    panel("Forest stratification section", "hierarchy", [
        "CANOPY -> high light, wind exposure and arboreal niches",
        "UNDERSTOREY -> filtered light and humid microclimate",
        "SHRUB AND HERB LAYERS -> near-ground resource partitioning",
        "FOREST FLOOR -> litter, detritivores and decomposer activity",
        "CAUTION -> more layers do not prove universal stability",
    ], [FACTS[9][0]]),
    panel("Productivity accounting", "process-flow", [
        "GROSS PRIMARY PRODUCTIVITY -> total producer fixation per unit time",
        "MINUS PRODUCER RESPIRATION -> metabolic energy used by producers",
        "NET PRIMARY PRODUCTIVITY -> growth and production available onward",
        "STANDING CROP -> living stock at a stated instant",
        "RULE -> a stock cannot substitute for a production rate",
    ], [FACTS[10][0], FACTS[11][0]]),
    panel("Resistance and resilience", "comparison", [
        "RESISTANCE -> limited departure from prior condition during a disturbance",
        "RESILIENCE -> recovery after the disturbance",
        "MONOCULTURE -> may look uniform while remaining shock-specific and fragile",
        "DIVERSE WEB -> may provide response options but no universal guarantee",
        "ANSWER -> name the shock, response variable and time frame",
    ], [FACTS[12][0]]),
    panel("Services and contributions", "matrix", [
        "PROVISIONING -> material outputs such as food, fibre and water",
        "REGULATING -> flood buffering, pollination and climate moderation",
        "SUPPORTING -> soil formation, primary production and nutrient cycling",
        "CULTURAL -> spiritual, aesthetic, recreational and knowledge values",
        "NCP -> includes relational and indigenous or local-knowledge values",
    ], [FACTS[13][0]]),
    panel("Carrying-capacity answer spine", "answer-spine", [
        "DEFINE -> sustained load without erosion of regenerative functions",
        "MEASURE -> regenerative supply, assimilative capacity and connectivity",
        "CONTEXT -> consumption, technology and governance alter the threshold",
        "LIMIT -> no timeless fixed headcount follows from the concept",
        "CONCLUDE -> plan within ecological limits and monitor the response",
    ], [FACTS[14][0]]),
    panel("Evidence and institution firewall", "evidence-table", [
        "BASIC OWNER -> definitions, mechanisms and verified PYQ concepts",
        "ROUTING LEDGER -> paper, year and neutral demand ownership",
        "OFFICIAL PAPER OCR -> printed wording only, never an inferred answer key",
        "FSI OR SURVEY BODY -> extent or inventory within its stated method",
        "LIVE STUB -> recorded as a failure, never converted into a current claim",
    ], [FACTS[15][0], FACTS[16][0], FACTS[17][0], FACTS[18][0], FACTS[19][0]]),
]


TOPIC_01 = common.topic(
    1,
    "Ecosystem Structure and Function",
    "01_Ecosystem-Structure-and-Function",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-01_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Explain why energy flow is unidirectional while matter cycles in an ecosystem.", [2, 4, 5]),
        (10, "Distinguish habitat, niche, ecotone and edge effect.", [7, 8]),
        (15, "Define ecosystem carrying capacity and explain its relevance to sustainable planning.", [0, 12, 14, 18]),
        (15, "Analyse how ecosystem structure enables ecosystem services.", [1, 9, 13, 17]),
        (20, "Assess whether food-web complexity necessarily guarantees ecosystem resilience.", [3, 6, 12, 15]),
        (20, "Evaluate the limits of using forest or tree cover as a proxy for ecosystem health.", [10, 11, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "A. G. Tansley",
        "system boundary",
        "producer",
        "detritivore",
        "decomposer",
        "energy",
        "matter",
        "food chain",
        "food web",
        "habitat",
        "niche",
        "ecotone",
        "edge effect",
        "gross primary productivity",
        "net primary productivity",
        "standing crop",
        "standing state",
        "stability",
        "resilience",
        "carrying capacity",
    ],
    (
        "The audited owners route the 2019 GS-III carrying-capacity demand "
        "directly to this topic and route objective concepts on primary "
        "producers, filter feeders, detritivores, symbiosis, parasitoids, fig "
        "pollination and wetland function. The direct Mains demand is solved as "
        "a demand card; objective routes remain answer-free because this package "
        "does not infer an official option or key."
    ),
    [
        common.make_pyq_solution(
            FACTS,
            "2019",
            "GS-III, Question 17",
            "Define ecosystem carrying capacity and explain its relevance to sustainable development planning.",
            "Verified routed Mains demand; model answer is original and not an official UPSC solution.",
            [0, 12, 14, 17, 18],
        )
    ],
    LIVE_SOURCE_ATTEMPTS,
    (
        "No new topic-specific live ecological fact was imported on 2026-09-03. "
        "The Forest Survey of India page returned only contact text, the IPCC "
        "page returned only a report title, the MoEFCC page carried an unrelated "
        "recruitment notice and PIB returned HTTP 403. The CBD Target 3 guidance "
        "was substantive but is not evidence for ecosystem productivity, cover "
        "quality or carrying capacity. All numbers and PYQ claims therefore "
        "remain bounded to repository owners and audited ledgers."
    ),
    allow_existing_history=False,
)
