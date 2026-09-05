"""Authored data for Environment and Ecology learner-v2 Topic 02."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    (
        "Biogeochemical cycle",
        "A biogeochemical cycle is movement of an element or compound between "
        "organisms and physical reservoirs; the analysis must identify the "
        "reservoir, the transfer process and the boundary within which a balance is claimed.",
    ),
    (
        "Pool, flux and residence-time boundary",
        "A pool is the quantity held in a reservoir and a flux is transfer per "
        "unit time; residence time requires a stated pool and outgoing flux, so "
        "none of the three may be replaced by an unsupported nutrient figure.",
    ),
    (
        "Gaseous and sedimentary cycle distinction",
        "Gaseous cycles have a major atmosphere or ocean reservoir and "
        "sedimentary cycles are centred in crust, soil or sediment; this is a "
        "reservoir classification, not a claim that every transfer is fast or reversible.",
    ),
    (
        "Carbon-cycle mechanism",
        "Photosynthesis transfers carbon into biomass, while respiration, "
        "decomposition and combustion return carbon to environmental reservoirs; "
        "a carbon stock and an annual carbon flux are different quantities.",
    ),
    (
        "Nitrogen fixation",
        "Nitrogen fixation converts atmospheric nitrogen into biologically "
        "usable forms through biological, atmospheric or industrial pathways; "
        "plants do not perform symbiotic bacterial fixation by themselves.",
    ),
    (
        "Ammonification, nitrification and denitrification",
        "Ammonification releases ammonia from organic nitrogen, nitrification "
        "oxidises ammonia through nitrite to nitrate, and denitrification reduces "
        "nitrate toward atmospheric nitrogen; these are distinct microbial processes.",
    ),
    (
        "Nitrogen-cycle organism routes",
        "The owner names Rhizobium and Azotobacter for fixation, Nitrosomonas "
        "and Nitrobacter for nitrification and Pseudomonas-type organisms for "
        "denitrification, while routed PYQs also require nitrogen-fixing plant associations.",
    ),
    (
        "Phosphorus-cycle boundary",
        "Rock weathering releases phosphate for biological uptake and later "
        "sedimentation; the owner treats phosphorus as having no significant "
        "atmospheric phase, so runoff and dispersed losses cannot be analysed as an atmospheric cycle.",
    ),
    (
        "Human acceleration is cycle-specific",
        "Fossil-fuel combustion alters carbon transfers, synthetic fertiliser "
        "alters reactive nitrogen inputs, and phosphate mining and runoff alter "
        "phosphorus movement; different causes and reservoirs require different policy levers.",
    ),
    (
        "Natural and cultural eutrophication",
        "Eutrophication can describe gradual natural enrichment and ageing of "
        "a water body, whereas cultural eutrophication is human-accelerated "
        "nutrient enrichment from sources such as sewage or fertiliser runoff.",
    ),
    (
        "Oxygen-depletion chain",
        "Nutrient enrichment can stimulate algal production; decomposition of "
        "the resulting organic material raises oxygen demand and can lower "
        "dissolved oxygen, but no universal bloom or fish-kill threshold is asserted.",
    ),
    (
        "Ecological pyramid parameter",
        "An ecological pyramid represents number, biomass or energy across "
        "successive trophic levels; its shape is meaningless unless the parameter, "
        "ecosystem and time basis are named.",
    ),
    (
        "Pyramid of numbers",
        "A numbers pyramid counts organisms and may be upright in a grassland "
        "or inverted where one large producer supports many consumers; organism "
        "size and count are not interchangeable.",
    ),
    (
        "Pyramid of biomass",
        "A biomass pyramid compares standing living material and is commonly "
        "upright on land but may invert in aquatic systems where a small producer "
        "standing crop is replenished rapidly.",
    ),
    (
        "Standing crop versus productivity",
        "A small standing crop can support consumers when producer turnover and "
        "productivity are high; an inverted biomass pyramid therefore does not "
        "prove low production or ecosystem dysfunction.",
    ),
    (
        "Pyramid of energy",
        "An energy pyramid is always upright because usable energy diminishes "
        "across trophic transfers; this thermodynamic direction does not imply "
        "that matter follows the same one-way path.",
    ),
    (
        "Ecological-efficiency caution",
        "The owner carries the roughly ten-per-cent rule only as an average "
        "heuristic and expressly rejects it as a fixed law; this package uses "
        "the qualitative dissipation rule unless a source-specific value is required.",
    ),
    (
        "Pyramid simplification limit",
        "Pyramids compress omnivory, seasonal change, decomposer routes and "
        "interlocking food webs into trophic levels; they are diagnostic models, "
        "not complete maps of ecosystem interaction.",
    ),
    (
        "Verified objective PYQ routes",
        "The audited ledger routes nitrogen compounds from agriculture and "
        "livestock, phosphorus from rock weathering and nitrogen-fixing plant "
        "associations to this topic; no official answer option is recorded or inferred.",
    ),
    (
        "Governance and evidence boundary",
        "CPCB water-quality monitoring and fertiliser policy are distinct levers "
        "on nutrient-cycle outcomes; thin live pages supplied no new cycle rate, "
        "pool size, trophic efficiency or current ecological status.",
    ),
]

TRAPS = [
    "Do not draw a cycle without naming its principal reservoir and transfer processes.",
    "Do not confuse a reservoir pool with a flux or infer residence time without both.",
    "Do not treat gaseous versus sedimentary as a universal fast-versus-slow law.",
    "Do not confuse a carbon stock with an annual carbon flow.",
    "Do not say plants independently fix atmospheric nitrogen.",
    "Do not merge ammonification, nitrification and denitrification.",
    "Do not assign one microorganism to every nitrogen transformation.",
    "Do not give phosphorus a major atmospheric phase.",
    "Do not prescribe one generic pollution lever for all cycles.",
    "Do not use eutrophication and cultural eutrophication as exact synonyms.",
    "Do not invent a universal nutrient or oxygen threshold.",
    "Do not describe a pyramid without naming number, biomass or energy.",
    "Do not infer biomass or energy from organism count.",
    "Do not call an inverted aquatic biomass pyramid an inverted energy pyramid.",
    "Do not confuse standing crop with productivity or turnover.",
    "Do not claim matter must also move one way because energy does.",
    "Do not present the ten-per-cent heuristic as an invariant law.",
    "Do not treat an ecological pyramid as a complete food-web model.",
    "Do not infer official PYQ answer keys from routed concepts.",
    "Do not convert a thin live page into a quantitative cycle claim.",
]

SESSION_TITLES = [
    "Cycle boundary, reservoirs and transfers",
    "Gaseous and sedimentary classification",
    "Carbon stocks and fluxes",
    "Nitrogen fixation pathways",
    "Ammonification, nitrification and denitrification",
    "Nitrogen organisms and phosphorus-cycle boundary",
    "Human acceleration by cycle",
    "Natural and cultural eutrophication",
    "Algal production and oxygen depletion",
    "Ecological pyramid parameters",
    "Number and biomass pyramids",
    "Standing crop and producer turnover",
    "Energy pyramids",
    "Efficiency and pyramid-model limits",
    "Verified PYQ routes and governance boundary",
]

ANSWER_ROUTES = [
    "Begin with reservoir and transfer arrows before discussing imbalance.",
    "Classify by reservoir and then qualify the speed or reversibility claim.",
    "Separate stored carbon from carbon transferred during a stated interval.",
    "Identify the fixation pathway and the organism-process relationship.",
    "Write the microbial sequence in the correct direction.",
    "Use named nitrogen organisms only for their assigned step and keep phosphorus in its reservoir frame.",
    "Match combustion, fertiliser and mining to different cycle disruptions.",
    "Distinguish natural ageing from human acceleration before stating impacts.",
    "Trace nutrient input to production, decomposition, oxygen demand and ecological effect.",
    "Name number, biomass or energy before interpreting a pyramid.",
    "Separate organism count from standing biomass and explain context-dependent inversion.",
    "Use rapid producer turnover to separate standing crop from productivity.",
    "Explain why the energy pyramid remains upright.",
    "Treat the transfer heuristic as non-universal and pyramids as simplified models.",
    "Close with verified route, answer-key and quantitative evidence limits.",
]

PANELS = [
    panel("Cycle accounting frame", "root-axes", [
        "SYSTEM BOUNDARY -> atmosphere, water, soil, sediment and living biomass included",
        "POOL -> amount held in one reservoir at a stated time",
        "FLUX -> transfer between reservoirs per stated time",
        "PROCESS -> biological, chemical or geological transformation",
        "BALANCE -> inputs minus outputs; never assumed from one isolated stock",
    ], [FACTS[0][0], FACTS[1][0]]),
    panel("Reservoir classification", "comparison-table", [
        "GASEOUS -> major atmosphere or ocean reservoir",
        "SEDIMENTARY -> major crust, soil or sediment reservoir",
        "CARBON AND NITROGEN -> prominent atmospheric exchange",
        "PHOSPHORUS -> rock-weathering and sediment pathway",
        "CAUTION -> class does not set one universal cycling speed",
    ], [FACTS[2][0], FACTS[7][0]]),
    panel("Carbon movement", "process-flow", [
        "ATMOSPHERIC OR DISSOLVED CARBON -> photosynthetic fixation",
        "PRODUCER BIOMASS -> consumers and detrital pathways",
        "RESPIRATION -> carbon returned during metabolism",
        "DECOMPOSITION AND COMBUSTION -> additional return pathways",
        "RULE -> stored carbon and annual transfer are different measures",
    ], [FACTS[3][0]]),
    panel("Nitrogen transformation rail", "process-flow", [
        "ATMOSPHERIC NITROGEN -> fixation -> ammonia or usable nitrogen forms",
        "ORGANIC NITROGEN -> ammonification -> ammonia",
        "AMMONIA -> nitrification -> nitrite -> nitrate",
        "NITRATE -> plant uptake or denitrification",
        "DENITRIFICATION -> return toward atmospheric nitrogen",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("Nitrogen organism map", "hierarchy", [
        "RHIZOBIUM -> symbiotic fixation associated with legume roots",
        "AZOTOBACTER -> free-living fixation example in the owner",
        "NITROSOMONAS -> ammonia to nitrite step",
        "NITROBACTER -> nitrite to nitrate step",
        "PSEUDOMONAS-TYPE -> denitrification route",
    ], [FACTS[6][0]]),
    panel("Phosphorus path", "path-consequence", [
        "PHOSPHATE ROCK -> weathering -> soil or water phosphate",
        "PLANT UPTAKE -> consumer transfer -> detrital return",
        "RUNOFF -> aquatic loading -> sedimentation",
        "MINING AND FERTILISER -> accelerate extraction and dispersal",
        "BOUNDARY -> no significant atmospheric phase in the owner",
    ], [FACTS[7][0], FACTS[8][0]]),
    panel("Cycle-specific human pressure", "matrix", [
        "CARBON -> fossil-fuel combustion and land-cover change",
        "NITROGEN -> synthetic fertiliser and combustion-related reactive nitrogen",
        "PHOSPHORUS -> mining, fertiliser application and runoff",
        "OUTCOMES -> climate forcing, nutrient pollution and resource loss differ",
        "POLICY -> source control must match the cycle and reservoir",
    ], [FACTS[8][0], FACTS[19][0]]),
    panel("Eutrophication mechanism", "process-flow", [
        "NUTRIENT ENRICHMENT -> increased algal or plant production",
        "ORGANIC MATERIAL ACCUMULATES -> decomposer activity rises",
        "OXYGEN DEMAND RISES -> dissolved oxygen may decline",
        "ECOLOGICAL STRESS -> composition changes and mortality may occur",
        "CLASSIFY -> natural ageing versus human-accelerated cultural eutrophication",
    ], [FACTS[9][0], FACTS[10][0]]),
    panel("Three pyramid parameters", "comparison-table", [
        "NUMBERS -> count of organisms at each trophic level",
        "BIOMASS -> standing living material at a stated time",
        "ENERGY -> transfer through trophic levels over time",
        "SHAPE -> depends on parameter and ecosystem",
        "RULE -> only the energy pyramid is always upright",
    ], [FACTS[11][0], FACTS[12][0], FACTS[13][0], FACTS[15][0]]),
    panel("Aquatic biomass inversion", "process-flow", [
        "SMALL PHYTOPLANKTON STANDING CROP -> rapid replacement",
        "HIGH TURNOVER -> continued production over the measurement period",
        "CONSUMER STANDING BIOMASS -> may exceed producer biomass at one instant",
        "ENERGY TRANSFER -> still declines upward",
        "VERDICT -> biomass inversion is not energy inversion",
    ], [FACTS[13][0], FACTS[14][0], FACTS[15][0]]),
    panel("Heuristic and model firewall", "evidence-table", [
        "ENERGY LOSS -> qualitative thermodynamic direction is robust",
        "TEN-PER-CENT RULE -> owner labels it an average heuristic",
        "OMNIVORY -> weakens a rigid one-level assignment",
        "SEASONALITY -> changes standing stocks and feeding relations",
        "PYRAMID -> useful summary, not a complete food web",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("PYQ and evidence boundary", "answer-spine", [
        "ROUTED CONCEPTS -> agricultural nitrogen, rock-weathered phosphorus, fixation links",
        "BASIC PRACTICE -> reservoir, process and organism distinctions",
        "OFFICIAL PAPER -> demand wording only",
        "NO KEY -> no option or answer inferred",
        "LIVE CHECK -> no rate, pool, efficiency or status imported from a stub",
    ], [FACTS[18][0], FACTS[19][0]]),
]


TOPIC_02 = common.topic(
    2,
    "Biogeochemical Cycles and Ecological Pyramids",
    "02_Biogeochemical-Cycles-and-Ecological-Pyramids",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-02_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish pool, flux and residence time in biogeochemical analysis.", [0, 1, 3]),
        (10, "Why is the phosphorus cycle analytically different from carbon and nitrogen cycles?", [2, 7, 8]),
        (15, "Explain the microbial sequence of the nitrogen cycle and its major close-option traps.", [4, 5, 6]),
        (15, "Explain natural and cultural eutrophication through a complete oxygen-depletion chain.", [8, 9, 10, 19]),
        (20, "Ecological pyramids can invert, but an energy pyramid cannot. Analyse.", [11, 12, 13, 14, 15]),
        (20, "Assess the usefulness and limitations of ecological pyramids for understanding real food webs.", [14, 15, 16, 17, 18]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "pool",
        "flux",
        "residence time",
        "gaseous cycle",
        "sedimentary cycle",
        "nitrogen fixation",
        "ammonification",
        "nitrification",
        "denitrification",
        "phosphorus",
        "cultural eutrophication",
        "pyramid of numbers",
        "pyramid of biomass",
        "pyramid of energy",
        "standing crop",
        "productivity",
        "turnover",
        "ten-per-cent",
    ],
    (
        "The audited Prelims ledger routes 2019 agricultural and livestock "
        "nitrogen compounds, 2021 phosphorus from rock weathering and 2022 "
        "nitrogen-fixing plant associations to this topic. They are retained in "
        "Basic sessions, MCQs and the owner extracts. No direct Mains demand or "
        "official objective answer is manufactured."
    ),
    [],
    LIVE_SOURCE_ATTEMPTS,
    (
        "No new quantitative cycle or pyramid claim was imported from live "
        "sources on 2026-09-03. FSI returned a contact-only stub, IPCC returned "
        "only the AR6 Synthesis Report title, MoEFCC returned an unrelated notice "
        "and PIB returned HTTP 403. The substantive CBD Target 3 guidance concerns "
        "area-based conservation and does not establish nutrient pools, fluxes, "
        "residence times, trophic efficiencies or pyramid shapes."
    ),
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)
