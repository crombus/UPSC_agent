"""Authored data for Environment and Ecology learner-v2 Topic 15."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import (
    WASTE_RULES_LIVE_SOURCE_ATTEMPTS,
    panel,
)


FACTS = [
    ("Separate waste streams", "Municipal solid waste, plastic waste and e-waste have separate rule frameworks, materials, actors and processing chains; a common parent statute does not make them one waste stream."),
    ("Rule-vintage discipline", "A rule, amendment, guideline, portal procedure and later waste-stream notification have different legal status and dates; the applicable vintage must be identified before stating an obligation."),
    ("Waste-generator duty", "A waste generator must segregate and hand over waste through the applicable authorised system; generator duty does not transfer producer, importer, local-body or recycler obligations."),
    ("ULB solid-waste role", "Urban local bodies organise major municipal collection and processing functions, while households, bulk generators, operators and state regulators retain their own duties."),
    ("Segregation boundary", "Wet, dry and domestic-hazardous segregation supports different collection and processing routes; mixing at source can defeat later recovery and safe handling."),
    ("Processing hierarchy", "Prevention, reuse, material recovery, treatment and safe disposal are different stages; collection or transport alone is not recycling or scientific disposal."),
    ("Plastic actor map", "Plastic producers, importers and brand owners have distinct registration and EPR responsibilities under the applicable framework; a retailer or ULB cannot automatically be substituted for them."),
    ("Item ban and packaging EPR", "Restrictions on identified single-use items and EPR for plastic packaging are separate control approaches; an item-specific restriction is not a blanket ban on all plastic."),
    ("Plastic material boundary", "A product may contain plastic without falling within the same banned-item list, packaging category or EPR obligation; material identification and legal classification are separate questions."),
    ("EPR obligation boundary", "Extended Producer Responsibility creates an end-of-life compliance obligation; an assigned target or certificate liability is not proof that physical recycling occurred."),
    ("Certificate and throughput", "Registration, EPR certificate generation or transfer, reported recycling throughput and independently verified material recovery are different records."),
    ("Plastic processor role", "A registered plastic waste processor performs an authorised end-of-life activity within the applicable category; authorisation does not prove every claimed quantity or environmental outcome."),
    ("E-waste actor map", "Manufacturer, producer, importer, consumer, bulk consumer, refurbisher and recycler have different roles; the product-market actor and end-of-life processor must not be merged."),
    ("Authorised channelisation", "E-waste should move to the applicable registered or authorised refurbishment and recycling chain; informal collection reach is distinct from unsafe dismantling or recovery."),
    ("E-waste EPR verification", "A producer's EPR compliance depends on the applicable certificate and recycling framework, but certificate accounting must remain distinct from the actual material processed."),
    ("Importer responsibility", "Importing covered products can create producer-side responsibility under the applicable rule; importing, manufacturing, branding and recycling are not interchangeable roles."),
    ("Informal-sector integration", "Waste pickers and informal collectors can provide collection reach and livelihoods, while hazardous processing requires safer integration with authorised facilities rather than exclusion or romanticisation."),
    ("Legacy stock versus new flow", "Contaminated sites and accumulated dumps are legacy stocks, while EPR principally governs current product and waste flows; remediation and flow control need different instruments."),
    ("Technology boundary", "Pyrolysis, plasma gasification, recycling, co-processing and disposal have feedstock, emission, energy and residue conditions; no technology is universally superior merely by name."),
    ("Audited evidence boundary", "Audited ledgers carry solid-waste governance, EPR, plastic-containing products, PET, pyrolysis, plasma gasification and electronics-recycling concepts into practice without inventing keys, targets, quantities or outcomes."),
]

TRAPS = [
    "Do not merge solid, plastic and e-waste into one rule document.",
    "Do not state an obligation without checking the rule and amendment vintage.",
    "Do not shift producer duties to the waste generator or ULB.",
    "Do not treat source segregation as completed recycling.",
    "Do not treat collection or transport as material recovery.",
    "Do not merge producer, importer and brand-owner roles.",
    "Do not convert an item-specific restriction into a blanket plastic ban.",
    "Do not infer a legal category only because an item contains plastic.",
    "Do not report an EPR target or liability as verified recycling.",
    "Do not equate registration, certificates and physical throughput.",
    "Do not treat recycler authorisation as proof of every claimed quantity.",
    "Do not merge e-waste producer, refurbisher and recycler roles.",
    "Do not treat informal collection as permission for unsafe processing.",
    "Do not use current-flow EPR as proof of legacy-site remediation.",
    "Do not declare a treatment technology universally clean or superior.",
]

SESSION_TITLES = [
    "Three waste streams and parent-statute boundary",
    "Rule amendment guideline and portal vintage",
    "Generator ULB operator and regulator duties",
    "Source segregation and processing hierarchy",
    "Plastic producer importer and brand-owner map",
    "Single-use item restrictions and packaging EPR",
    "Plastic content legal category and product scope",
    "EPR obligation target and verified recycling",
    "Registration certificates and material throughput",
    "Plastic processor authorisation and audit",
    "E-waste actor and responsibility map",
    "Authorised channelisation refurbishment and recycling",
    "Importer role and informal-sector integration",
    "Legacy contamination and treatment technologies",
    "Evidence-safe exam synthesis",
]

ANSWER_ROUTES = [
    "Classify the material stream before naming a rule or actor.",
    "Date the rule, amendment and portal procedure separately.",
    "Assign generator, local-body, operator and regulator duties one by one.",
    "Trace waste from segregation to recovery, treatment and residue disposal.",
    "Map producer, importer and brand owner before discussing compliance.",
    "Separate item restrictions from packaging lifecycle responsibility.",
    "Identify material composition first, then apply the exact legal category.",
    "Distinguish obligation, target and evidence of physical recovery.",
    "Trace registration, certificate accounting, throughput and independent audit.",
    "Treat authorisation as entry to regulation, not proof of outcome.",
    "Separate market actors from refurbishers and end-of-life processors.",
    "Route e-waste through safer authorised processing while preserving collection reach.",
    "State importer responsibility and a just-transition route for informal workers.",
    "Separate legacy stock remediation from new-flow control and compare technologies conditionally.",
    "Close with verified demand ownership and explicit numeric limits.",
]

PANELS = [
    panel("Three-stream firewall", "comparison-table", [
        "SOLID WASTE -> municipal generation, segregation and local services",
        "PLASTIC WASTE -> product and packaging controls plus EPR",
        "E-WASTE -> electrical and electronic end-of-life chain",
        "COMMON PARENT -> Environment Protection Act framework",
        "RULE -> separate streams remain legally distinct",
    ], [FACTS[0][0], FACTS[1][0]]),
    panel("Rule-vintage ladder", "timeline", [
        "BASE RULE -> identify notification",
        "AMENDMENT -> identify changed provision and date",
        "GUIDELINE OR SOP -> implementation instruction",
        "PORTAL PROCEDURE -> digital compliance workflow",
        "CURRENT CLAIM -> verify all later changes",
    ], [FACTS[1][0]]),
    panel("Municipal responsibility map", "hierarchy", [
        "GENERATOR -> segregate and hand over",
        "BULK GENERATOR -> additional applicable duties",
        "ULB -> collection and processing system",
        "OPERATOR -> run authorised facility",
        "SPCB OR PCC -> authorisation and monitoring",
    ], [FACTS[2][0], FACTS[3][0]]),
    panel("Segregation-to-disposal chain", "process-flow", [
        "PREVENT OR REDUCE -> avoid waste",
        "SEGREGATE -> preserve recoverable streams",
        "COLLECT AND TRANSPORT -> move without remixing",
        "RECOVER OR TREAT -> process by stream",
        "RESIDUE -> safe final disposal",
    ], [FACTS[4][0], FACTS[5][0]]),
    panel("Plastic actor matrix", "comparison-table", [
        "PRODUCER -> covered product or packaging responsibility",
        "IMPORTER -> covered imported product responsibility",
        "BRAND OWNER -> branded packaging responsibility",
        "PROCESSOR -> authorised end-of-life activity",
        "ULB -> municipal service role, not automatic EPR substitute",
    ], [FACTS[6][0], FACTS[11][0], FACTS[15][0]]),
    panel("Ban-versus-EPR gate", "decision-gate", [
        "IDENTIFIED ITEM -> test the exact restriction and vintage",
        "PLASTIC PACKAGING -> test EPR category and obligation",
        "OTHER PRODUCT -> do not infer ban from plastic content",
        "MATERIAL FACT -> composition question",
        "LEGAL FACT -> rule-specific classification",
    ], [FACTS[7][0], FACTS[8][0]]),
    panel("EPR evidence ladder", "layered-rail", [
        "OBLIGATION OR TARGET -> legal requirement",
        "REGISTRATION -> actor enters portal",
        "CERTIFICATE -> compliance instrument",
        "REPORTED THROUGHPUT -> claimed processing",
        "VERIFIED RECOVERY -> physical outcome evidence",
    ], [FACTS[9][0], FACTS[10][0]]),
    panel("Processor audit gate", "decision-tree", [
        "REGISTRATION -> formal eligibility",
        "INPUT RECORD -> material received",
        "PROCESS RECORD -> actual authorised operation",
        "OUTPUT AND RESIDUE -> destination and safe handling",
        "AUDIT -> quantity and outcome require verification",
    ], [FACTS[11][0]]),
    panel("E-waste actor chain", "process-flow", [
        "MANUFACTURER OR IMPORTER -> product enters market",
        "PRODUCER -> EPR-side responsibility",
        "CONSUMER OR BULK CONSUMER -> channelisation duty",
        "REFURBISHER -> life extension where applicable",
        "RECYCLER -> authorised material recovery",
    ], [FACTS[12][0], FACTS[15][0]]),
    panel("Formal-informal integration map", "comparison-table", [
        "INFORMAL COLLECTOR -> reach and livelihood",
        "UNSAFE DISMANTLING -> exposure and pollution risk",
        "AUTHORISED FACILITY -> controlled processing route",
        "INTEGRATION -> recognition, safety and traceability",
        "VERDICT -> formalise processing without erasing livelihoods",
    ], [FACTS[13][0], FACTS[16][0]]),
    panel("Stock-flow and technology matrix", "comparison-table", [
        "CURRENT WASTE FLOW -> EPR and collection controls",
        "LEGACY DUMP OR SITE -> remediation problem",
        "RECYCLING -> material recovery route",
        "THERMAL OR CHEMICAL ROUTE -> feedstock and emission conditions",
        "NO UNIVERSAL WINNER -> compare complete mass and residue balance",
    ], [FACTS[17][0], FACTS[18][0]]),
    panel("Waste-governance answer spine", "answer-spine", [
        "CLASSIFY -> stream, material and rule vintage",
        "ASSIGN -> generator, ULB, producer, importer and processor",
        "TRACE -> segregation, collection, processing and residue",
        "VERIFY -> obligation, certificate, throughput and recovery",
        "QUALIFY -> informal sector, legacy stock, technology and PYQ limits",
    ], [FACTS[19][0]]),
]

TOPIC_15 = common.topic(
    15,
    "Solid Plastic and E-Waste Rules",
    "15_Solid-Plastic-and-E-Waste-Rules",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-15_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish solid-waste, plastic-waste and e-waste rule frameworks.", [0, 1, 2, 3]),
        (10, "Explain Extended Producer Responsibility without equating it with recycling.", [6, 9, 10]),
        (15, "Map duties from waste generation to authorised processing.", [2, 3, 4, 5, 11]),
        (15, "Distinguish item-specific plastic restrictions from packaging EPR.", [6, 7, 8, 15]),
        (20, "Evaluate EPR certificate systems through verification and actor responsibility.", [9, 10, 11, 12, 14, 15]),
        (20, "Build an inclusive waste-governance strategy for current flows and legacy stocks.", [0, 5, 13, 16, 17, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "solid waste", "plastic waste", "e-waste", "rule vintage",
        "waste generator", "urban local bodies", "source segregation",
        "processing hierarchy", "producer", "importer", "brand owner",
        "single-use item", "plastic packaging", "Extended Producer Responsibility",
        "EPR certificate", "reported throughput", "verified recycling",
        "plastic waste processor", "refurbisher", "authorised recycler",
        "informal sector", "legacy stock", "pyrolysis", "plasma gasification",
    ],
    (
        "Audited ledgers route direct Mains demand on solid-waste and toxic-"
        "waste management, plus objective concepts on SWM Rules, EPR, PET, "
        "pyrolysis, plasma gasification, electronics recycling, chewing-gum "
        "base and plastic-containing everyday products. Keys are not inferred."
    ),
    [],
    WASTE_RULES_LIVE_SOURCE_ATTEMPTS,
    (
        "The MoEFCC rules page substantively confirmed that solid, plastic, "
        "e-waste, battery, contaminated-site and end-of-life-vehicle rules are "
        "separate families. CPCB pages and the plastic EPR portal were title-"
        "only, and the vehicle PDF failed at transport level. No target, ban "
        "list, quantity, registration, certificate or recycling outcome was used."
    ),
    extra=[
        "basic/14_Water-Pollution-and-River-Cleaning-Missions.md",
        "basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
        "advanced/14_Water-Pollution-and-River-Cleaning-Missions.md",
        "advanced/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md",
    ],
    pyq_audit_heading="AUDITED SOLID-WASTE, PLASTIC, EPR AND E-WASTE PYQ OWNERSHIP",
    allow_existing_history=True,
    register_headings=(
        "WASTE STREAM, ACTOR, RULE VINTAGE AND PROCESSING MAP",
        "BAN, EPR, CERTIFICATE, THROUGHPUT AND RECYCLING TRAPS",
        "WASTE-GOVERNANCE ANSWER SPINE",
        "LIVE TARGET, QUANTITY, AMENDMENT AND PYQ EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "CLASSIFY THE SOLID, PLASTIC OR E-WASTE STREAM",
        "IDENTIFY THE APPLICABLE RULE AND AMENDMENT VINTAGE",
        "ASSIGN GENERATOR, ULB, PRODUCER, IMPORTER AND PROCESSOR DUTIES",
        "TRACE SEGREGATION, COLLECTION, RECOVERY, TREATMENT AND RESIDUE",
        "SEPARATE EPR OBLIGATION, CERTIFICATE AND VERIFIED RECYCLING",
        "INTEGRATE INFORMAL COLLECTORS WITH SAFE AUTHORISED PROCESSING",
        "CONCLUDE WITH TRACEABILITY, AUDIT AND LEGACY-SITE REMEDIATION",
    ],
)
