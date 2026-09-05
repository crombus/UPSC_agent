"""Authored data for Environment and Ecology learner-v2 Topic 04."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import LIVE_SOURCE_ATTEMPTS, panel


FACTS = [
    (
        "Genetic diversity",
        "Genetic diversity is variation within a species or population and "
        "supports adaptive capacity; crop landraces are the owner's Indian "
        "example, but no unsupported count of varieties is used.",
    ),
    (
        "Species diversity",
        "Species diversity concerns the variety and relative abundance of "
        "species in a community or region; it combines more than a bare species "
        "list and must be measured at a stated spatial scale.",
    ),
    (
        "Ecosystem diversity",
        "Ecosystem diversity is variation among habitats, communities and "
        "ecological processes across a landscape; it is an ecological level and "
        "not another taxonomic rank.",
    ),
    (
        "Richness and evenness",
        "Species richness is the number of species and evenness describes how "
        "abundance is distributed among them; equal richness does not guarantee "
        "equal species diversity.",
    ),
    (
        "Alpha diversity",
        "Alpha diversity describes diversity within one local community or "
        "habitat at a stated sampling scale; it must not be silently equated "
        "with regional richness.",
    ),
    (
        "Beta diversity",
        "Beta diversity describes turnover in species composition between "
        "communities or along a gradient; high turnover does not by itself mean "
        "that either individual community is species-rich.",
    ),
    (
        "Gamma diversity",
        "Gamma diversity describes diversity across a larger landscape or "
        "region and reflects the combined local diversity and compositional "
        "turnover within that stated region.",
    ),
    (
        "Ecological and taxonomic levels",
        "Genetic, species and ecosystem diversity are ecological assessment "
        "levels, whereas genus, family or order are taxonomic ranks; a question "
        "about biodiversity level cannot be answered with a taxonomic hierarchy.",
    ),
    (
        "Endemic versus native",
        "A native species occurs naturally in a region, while an endemic species "
        "has a naturally restricted distribution to a defined region; native "
        "does not automatically mean endemic.",
    ),
    (
        "Endemic versus rare or threatened",
        "Endemism describes geographic restriction, rarity describes abundance "
        "or occurrence, and threatened status belongs to an assessment framework; "
        "these properties can overlap but are not synonyms.",
    ),
    (
        "Hotspot dual criteria",
        "The owner records the Conservation International hotspot test as at "
        "least 1,500 endemic vascular plant species and 30 per cent or less of "
        "original natural vegetation remaining; both criteria are required.",
    ),
    (
        "Norman Myers and operational status",
        "The hotspot idea is credited in the owner to Norman Myers in 1988 and "
        "was later operationalised through the dual criteria; it is a scientific "
        "prioritisation framework, not an Indian statutory designation.",
    ),
    (
        "India-linked hotspots",
        "The owners identify Himalaya, Indo-Burma, Western Ghats-Sri Lanka and "
        "Sundaland represented in India by the Nicobar Islands; each name denotes "
        "a wider biogeographic unit, not necessarily India's political boundary.",
    ),
    (
        "Hotspot versus general richness",
        "A species-rich area is not automatically a hotspot because hotspot "
        "status requires both vascular-plant endemism and severe historical "
        "habitat loss; richness alone is insufficient.",
    ),
    (
        "Hotspot triage and non-hotspot value",
        "Hotspots prioritise scarce conservation resources where endemism and "
        "habitat loss coincide, but non-hotspot grasslands, wetlands, cold deserts "
        "or other ecosystems can remain nationally important.",
    ),
    (
        "Megadiverse and LMMC distinction",
        "India is carried by the owner as a megadiverse country and participates "
        "in the Like-Minded Megadiverse Countries grouping; that political label "
        "and a hotspot designation answer different questions.",
    ),
    (
        "NBA, SBB and BMC levels",
        "The Biological Diversity Act architecture uses the National Biodiversity "
        "Authority, State Biodiversity Boards and local Biodiversity Management "
        "Committees; institutional level must not be confused with biodiversity level.",
    ),
    (
        "Access, benefit sharing and PBRs",
        "Access and benefit sharing links use of biological resources or "
        "associated knowledge to benefit sharing, while Biodiversity Management "
        "Committees prepare People's Biodiversity Registers; legal design does "
        "not prove uniform local implementation.",
    ),
    (
        "KMGBF, OECMs and status boundary",
        "The owner carries the Kunming-Montreal Global Biodiversity Framework "
        "Target 3 area-based conservation commitment and OECMs; the live CBD "
        "Secretariat guidance says its guidance does not replace COP decisions.",
    ),
    (
        "Verified PYQ and current-claim boundary",
        "Routed concepts include human drivers of mass extinction, the IUCN "
        "Invasive Species Specialist Group and the EU Nature Restoration Law; "
        "they are external or institutional comparators, not Indian legal designations or inferred answer keys.",
    ),
]

TRAPS = [
    "Do not use biodiversity as a synonym for species count alone.",
    "Do not describe species diversity without fixing spatial scale.",
    "Do not turn ecosystem diversity into a taxonomic rank.",
    "Do not equate richness with evenness or a complete diversity measure.",
    "Do not use alpha diversity for an unspecified whole region.",
    "Do not infer high local richness from high beta diversity.",
    "Do not discuss gamma diversity without defining the landscape boundary.",
    "Do not mix ecological diversity levels with taxonomic hierarchy.",
    "Do not use native and endemic interchangeably.",
    "Do not use endemic, rare and threatened as synonyms.",
    "Do not quote hotspot criteria without both source-bounded thresholds.",
    "Do not present hotspot as an Indian statutory protected-area category.",
    "Do not shrink a transboundary hotspot name to India's political boundary.",
    "Do not label every species-rich forest a hotspot.",
    "Do not imply non-hotspot ecosystems lack conservation value.",
    "Do not treat megadiverse-country status as hotspot status.",
    "Do not confuse NBA-SBB-BMC levels with genetic-species-ecosystem levels.",
    "Do not treat a People's Biodiversity Register as proof of benefit delivery.",
    "Do not turn Secretariat guidance into a replacement for adopted COP decisions.",
    "Do not import an external PYQ comparator as Indian law or infer its answer key.",
]

SESSION_TITLES = [
    "Genetic, species and ecosystem diversity",
    "Richness and evenness",
    "Alpha diversity",
    "Beta diversity and turnover",
    "Gamma diversity and ecological versus taxonomic levels",
    "Native and endemic species",
    "Endemic, rare and threatened status",
    "Hotspot dual criteria",
    "Norman Myers and scientific designation",
    "India-linked transboundary hotspots",
    "Hotspot versus general richness",
    "Hotspot triage and non-hotspot value",
    "Megadiverse status and NBA-SBB-BMC institutions",
    "ABS and People's Biodiversity Registers",
    "KMGBF, OECMs, verified PYQs and current boundaries",
]

ANSWER_ROUTES = [
    "Open with the three nested biodiversity levels and one bounded Indian example each.",
    "Use richness and evenness as distinct components.",
    "Define the local sampling unit before using alpha diversity.",
    "Describe compositional turnover rather than local abundance.",
    "Fix the landscape boundary and separate ecological levels from taxonomic ranks.",
    "Define native and endemic through natural distribution.",
    "Define geographic restriction, abundance and threat status separately.",
    "Write both hotspot criteria and their logical AND relation.",
    "Identify hotspot as scientific triage, not a statutory category.",
    "Name the four India-linked hotspots with their wider biogeographic extent.",
    "Show why species richness alone cannot establish hotspot status.",
    "Balance hotspot priority against conservation value outside hotspots.",
    "Separate country grouping, scientific label and statutory institutional levels.",
    "Explain ABS and PBR roles without claiming uniform benefit delivery.",
    "Close with Target 3 status, OECMs and verified external PYQ limits.",
]

PANELS = [
    panel("Three-level biodiversity ladder", "hierarchy", [
        "GENETIC -> variation within a species or population",
        "SPECIES -> variety and relative abundance within a stated area",
        "ECOSYSTEM -> variety of habitats, communities and processes",
        "DEPENDENCE -> loss at one level can weaken the others",
        "RULE -> level is ecological scale, not taxonomic rank",
    ], [FACTS[0][0], FACTS[1][0], FACTS[2][0], FACTS[7][0]]),
    panel("Species-diversity components", "comparison-table", [
        "RICHNESS -> number of species",
        "EVENNESS -> distribution of abundance among species",
        "SAME RICHNESS -> can coexist with different evenness",
        "DIVERSITY INDEX -> depends on its stated formula and sample",
        "CAUTION -> never infer community quality from count alone",
    ], [FACTS[3][0]]),
    panel("Alpha beta gamma map", "spatial", [
        "HABITAT A -> alpha diversity inside one local community",
        "HABITAT B -> its own local alpha diversity",
        "A TO B TURNOVER -> beta diversity",
        "WHOLE LANDSCAPE -> gamma diversity",
        "RULE -> every term requires a stated sampling or regional boundary",
    ], [FACTS[4][0], FACTS[5][0], FACTS[6][0]]),
    panel("Ecological and taxonomic axes", "matrix", [
        "ECOLOGICAL LEVEL -> genetic, species, ecosystem",
        "SPATIAL DIVERSITY -> alpha, beta, gamma",
        "TAXONOMIC RANK -> species, genus, family and higher ranks",
        "THREAT STATUS -> separate assessment of extinction risk",
        "RULE -> answer on the axis actually asked",
    ], [FACTS[7][0], FACTS[9][0]]),
    panel("Distribution vocabulary", "comparison", [
        "NATIVE -> occurs naturally in the defined region",
        "ENDEMIC -> naturally restricted to the defined region",
        "RARE -> low abundance or occurrence under a stated measure",
        "THREATENED -> status under an assessment framework",
        "CAUTION -> one species may satisfy several, but terms are not synonyms",
    ], [FACTS[8][0], FACTS[9][0]]),
    panel("Hotspot criteria gate", "process-flow", [
        "GATE 1 -> at least 1,500 endemic vascular plant species",
        "AND",
        "GATE 2 -> 30 per cent or less of original natural vegetation remains",
        "BOTH GATES MET -> hotspot prioritisation framework applies",
        "FAILED GATE -> species richness alone cannot create hotspot status",
    ], [FACTS[10][0], FACTS[13][0]]),
    panel("Designation firewall", "evidence-table", [
        "HOTSPOT -> Conservation International scientific prioritisation framework",
        "PROTECTED AREA -> legal designation under applicable domestic law",
        "BIODIVERSITY HERITAGE SITE -> separate statutory category",
        "ECO-SENSITIVE ZONE -> notification-based regulatory status",
        "RULE -> one label never automatically confers another status",
    ], [FACTS[11][0], FACTS[13][0]]),
    panel("India-linked hotspot map in words", "spatial", [
        "HIMALAYA -> transboundary mountain biodiversity region",
        "INDO-BURMA -> wider mainland Southeast Asian biogeographic region",
        "WESTERN GHATS-SRI LANKA -> linked biogeographic hotspot name",
        "SUNDALAND -> India's represented portion is the Nicobar Islands",
        "CAUTION -> hotspot extent is not coterminous with India's border",
    ], [FACTS[12][0]]),
    panel("Triage and completeness", "dialectic", [
        "HOTSPOT LOGIC -> focus scarce resources where endemism and habitat loss coincide",
        "PRESSURE -> plant criteria can understate other nationally important values",
        "NON-HOTSPOT EXAMPLES -> grasslands, wetlands and cold deserts",
        "REPLY -> use hotspots for priority, not for exclusion",
        "VERDICT -> national strategy must retain a wider ecological baseline",
    ], [FACTS[14][0]]),
    panel("Country, label and institution", "comparison-table", [
        "MEGADIVERSE COUNTRY -> national biodiversity descriptor",
        "LMMC -> international political grouping",
        "HOTSPOT -> transboundary scientific priority region",
        "NBA, SBB, BMC -> domestic statutory governance levels",
        "RULE -> four categories answer different questions",
    ], [FACTS[15][0], FACTS[16][0]]),
    panel("ABS governance rail", "process-flow", [
        "BIOLOGICAL RESOURCE OR ASSOCIATED KNOWLEDGE -> access request",
        "RELEVANT AUTHORITY -> scrutiny under the legal architecture",
        "COMMERCIAL OR RESEARCH USE -> applicable conditions",
        "BENEFIT SHARING -> intended return to eligible claimants or communities",
        "PBR -> local documentation; not proof that benefits were delivered",
    ], [FACTS[16][0], FACTS[17][0]]),
    panel("Global and PYQ boundary", "answer-spine", [
        "KMGBF TARGET 3 -> area-based conservation and OECMs in the owner",
        "CBD GUIDANCE -> does not replace or qualify adopted COP decisions",
        "MASS EXTINCTION ROUTE -> human drivers, no inferred objective answer",
        "ISSG AND EU NRL -> external institutional or legal comparators",
        "CLOSE -> scientific label, domestic law and external comparator stay distinct",
    ], [FACTS[18][0], FACTS[19][0]]),
]


TOPIC_04 = common.topic(
    4,
    "Biodiversity Levels and Hotspots",
    "04_Biodiversity-Levels-and-Hotspots",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-04_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish genetic, species and ecosystem diversity with bounded examples.", [0, 1, 2]),
        (10, "Explain alpha, beta and gamma diversity without confusing scale and richness.", [3, 4, 5, 6]),
        (15, "Distinguish native, endemic, rare and threatened species terminology.", [7, 8, 9]),
        (15, "Explain the dual biodiversity-hotspot criteria and why richness alone is insufficient.", [10, 11, 13]),
        (20, "Hotspot-based conservation is necessary but not sufficient for India. Critically examine.", [12, 14, 15, 18]),
        (20, "Assess how biodiversity levels connect with India's NBA-SBB-BMC, ABS and PBR architecture.", [0, 2, 16, 17, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "genetic diversity",
        "species diversity",
        "ecosystem diversity",
        "richness",
        "evenness",
        "alpha diversity",
        "beta diversity",
        "gamma diversity",
        "endemic",
        "native",
        "1,500 endemic vascular plant species",
        "30 per cent or less",
        "Norman Myers",
        "Himalaya",
        "Indo-Burma",
        "Western Ghats-Sri Lanka",
        "Sundaland",
        "National Biodiversity Authority",
        "People's Biodiversity Registers",
        "OECMs",
    ],
    (
        "The audited ledgers route 2018 human drivers of the sixth mass "
        "extinction, 2023 identification of the IUCN Invasive Species Specialist "
        "Group and 2025 the EU Nature Restoration Law. These concepts are carried "
        "into Basic sessions and practice as answer-free objective routes. They "
        "are not converted into Indian legal designations or official answer keys."
    ),
    [],
    LIVE_SOURCE_ATTEMPTS,
    (
        "The CBD Secretariat Target 3 page was substantively retrievable on "
        "2026-09-03 and was used only for its express statement that the guidance "
        "does not replace or qualify COP decisions 15/4 or 15/5. It did not supply "
        "the hotspot thresholds, an Indian hotspot extent, a species total or "
        "implementation result. Those claims remain bounded to repository owners. "
        "FSI was a contact-only stub, MoEFCC was unrelated, IPCC was title-only "
        "and PIB returned HTTP 403."
    ),
    pyq_audit_heading="VERIFIED OBJECTIVE-ONLY PYQ OWNERSHIP AUDIT",
)
