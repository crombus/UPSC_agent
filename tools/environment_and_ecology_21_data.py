"""Authored data for Environment and Ecology learner-v2 Topic 21."""

from __future__ import annotations

import generate_environment_and_ecology_common as common
from environment_and_ecology_data_helpers import panel


FACTS = [
    ("Allowance-credit distinction", "An allowance authorises emissions within a compliance system's rule-defined limit, while a credit represents a verified reduction or removal against an approved baseline; the units may be tradable but their origins are not interchangeable."),
    ("Cap-and-trade boundary", "A cap-and-trade market fixes an absolute covered-emissions ceiling and distributes or auctions allowances; it must not be relabelled as an intensity baseline-and-credit system."),
    ("Baseline-and-credit boundary", "A baseline-and-credit market compares performance with a rule-defined baseline or target and issues credits for qualifying over-performance; it does not necessarily impose an absolute emissions cap."),
    ("Compliance-voluntary boundary", "Compliance markets arise from legal obligations, while voluntary markets arise from non-mandated purchases or claims; registry use or private demand does not convert one into the other."),
    ("Avoidance-reduction-removal", "Avoided emissions prevent a counterfactual source, reductions lower emissions from an existing source or activity, and removals take greenhouse gases from the atmosphere and durably store them; claim type must remain explicit."),
    ("Additionality and baseline", "A credited activity needs a defensible baseline and additionality test so the claimed outcome is not merely business as usual; neither label alone proves integrity."),
    ("MRV and verification", "Monitoring, reporting and verification quantify the claimed outcome and test it against the governing methodology, boundary and period; verification is evidence infrastructure, not a guarantee against every integrity risk."),
    ("Issuance-transfer-retirement", "Credit validation or registration, verification, issuance, transfer and retirement are separate lifecycle stages; issuance creates a unit, while retirement is the act used to support a final claim."),
    ("Double counting boundary", "Double issuance, double use and double claiming are distinct accounting risks; preventing one does not automatically prevent the others."),
    ("Article 6 accounting boundary", "Paris Agreement cooperative approaches require instrument-specific authorisation and accounting discipline; a corresponding adjustment is an accounting treatment and must not be confused with credit issuance, transfer or retirement."),
    ("India CCTS status boundary", "India's Carbon Credit Trading Scheme has a legal and institutional architecture with compliance and offset pathways, but notification, sectoral target setting, credit issuance, exchange trading and a discovered market price are separate implementation stages."),
    ("CCUS chain", "CCUS is a chain of carbon dioxide capture, conditioning, transport, utilisation or storage, monitoring and closure; performance at the capture unit alone does not establish whole-chain climate benefit."),
    ("Point-source capture", "Point-source capture separates carbon dioxide from a relatively concentrated industrial or power-sector stream before release; capture efficiency is not the same as lifecycle emissions avoided."),
    ("Utilisation-storage boundary", "Carbon utilisation places captured carbon into a product or process, whereas geological storage seeks long-duration containment; utilisation is not automatically permanent storage."),
    ("Permanence and leakage", "A storage claim requires site characterisation, injection control, monitoring, leakage-risk management and long-term stewardship; stored quantity must not be inferred from nominal project capacity."),
    ("DAC identity", "Direct Air Capture separates carbon dioxide from ambient air rather than a point-source stream and therefore addresses atmospheric carbon already dispersed at low concentration."),
    ("DAC versus point-source CCUS", "Point-source CCUS principally avoids or reduces new emissions from a facility, while DAC can support atmospheric removal only when captured carbon is durably stored and lifecycle emissions do not negate the removal."),
    ("BECCS boundary", "Bioenergy with carbon capture and storage can support removal only when biomass carbon, land-use effects, supply-chain emissions and durable storage are accounted for; capture equipment alone does not prove net-negative emissions."),
    ("Residual-emissions role", "Carbon dioxide removal may counterbalance residual emissions in a net-zero framework, but a removal pathway does not excuse avoidable emissions or replace rapid source reduction."),
    ("Current evidence boundary", "Carbon prices, traded volumes, methodologies, Article 6 operational status, CCTS obligations, capture rates, costs, storage capacity and DAC deployment require dated primary evidence and are not inferred from announcements or design documents."),
]

TRAPS = [
    "Do not merge allowances with project credits.",
    "Do not call every compliance market cap-and-trade.",
    "Do not infer an absolute cap from an intensity baseline.",
    "Do not call voluntary demand a legal compliance obligation.",
    "Do not merge avoidance, reduction and removal claims.",
    "Do not treat a baseline or methodology label as proof of additionality.",
    "Do not treat verification as immunity from over-crediting.",
    "Do not merge issuance, transfer and retirement.",
    "Do not merge double issuance, double use and double claiming.",
    "Do not call a corresponding adjustment a credit or retirement event.",
    "Do not infer an operating liquid CCTS market from a notified framework.",
    "Do not reduce CCUS to capture equipment alone.",
    "Do not equate capture rate with lifecycle emissions avoided.",
    "Do not assume utilisation provides durable storage.",
    "Do not infer injected or stored quantity from announced capacity.",
    "Do not call standard point-source CCUS atmospheric removal.",
    "Do not call DAC removal unless durable storage and lifecycle accounting are specified.",
    "Do not treat BECCS as automatically net negative.",
    "Do not use removals to excuse avoidable source emissions.",
    "Do not invent prices, volumes, costs, capacity, methodologies or deployment status.",
]

SESSION_TITLES = [
    "Allowance credit and cap-and-trade unit architecture",
    "Baseline-and-credit architecture",
    "Compliance and voluntary market boundary",
    "Avoidance reduction and removal claim types",
    "Baseline and additionality integrity",
    "MRV and credit lifecycle through retirement",
    "Double issuance use and claiming",
    "Article 6 accounting and corresponding adjustment",
    "India CCTS implementation stages",
    "Complete CCUS chain",
    "Point-source capture and utilisation-storage boundary",
    "Storage permanence and leakage",
    "Direct Air Capture identity",
    "DAC point-source CCUS and BECCS comparison",
    "Residual emissions and current evidence audit",
]

ANSWER_ROUTES = [
    "Identify whether the unit is an allowance or a credited outcome before discussing trade.",
    "State whether the constraint is an absolute cap or an intensity baseline.",
    "Separate legal compliance demand from voluntary purchasing and claims.",
    "Classify the claimed outcome as avoidance, reduction or atmospheric removal.",
    "Audit baseline, additionality, boundary, monitoring and independent verification.",
    "Trace registration, verification, issuance, transfer and retirement separately.",
    "Name the double-counting risk and the accounting response without merging stages.",
    "Separate the notified Indian framework from targets, issuance, trading and price discovery.",
    "Follow carbon dioxide from source separation through transport to its destination.",
    "Test utilisation duration, storage permanence, monitoring and leakage responsibility.",
    "Compare capture-unit performance with full lifecycle emissions.",
    "Define ambient-air capture before discussing removal value or energy demand.",
    "Compare source, carbon origin, destination and net atmospheric effect.",
    "Place removals after avoidance and reduction for genuinely residual emissions.",
    "Conclude only with dated primary evidence for market and deployment status.",
]

PANELS = [
    panel("Carbon-unit identity fork", "decision-tree", [
        "ALLOWANCE -> permission unit inside a compliance constraint",
        "CREDIT -> verified outcome against an approved baseline",
        "ORIGIN -> allocation or auction versus methodology and issuance",
        "USE -> surrender or retirement under the applicable rule",
        "TRAP -> tradability does not erase different unit origins",
    ], [FACTS[0][0], FACTS[7][0]]),
    panel("Market architecture matrix", "comparison-table", [
        "CAP AND TRADE -> absolute covered-emissions ceiling",
        "BASELINE AND CREDIT -> performance against target or baseline",
        "COMPLIANCE -> legal obligation and surrender requirement",
        "VOLUNTARY -> non-mandated purchase or claim",
        "QUESTION -> what constrains emissions and who must act",
    ], [FACTS[1][0], FACTS[2][0], FACTS[3][0]]),
    panel("Claim-type ladder", "hierarchy", [
        "AVOIDANCE -> counterfactual source does not arise",
        "REDUCTION -> existing source emits less",
        "REMOVAL -> carbon leaves ambient atmosphere",
        "STORAGE -> duration and reversal risk determine durability",
        "NO MERGER -> each supports a different climate claim",
    ], [FACTS[4][0], FACTS[17][0]]),
    panel("Integrity gate", "process-flow", [
        "BASELINE -> define the counterfactual",
        "ADDITIONALITY -> test business-as-usual risk",
        "MRV -> quantify boundary period and outcome",
        "VERIFICATION -> independent evidence check",
        "ISSUANCE -> unit created only after rule-defined gates",
    ], [FACTS[5][0], FACTS[6][0], FACTS[7][0]]),
    panel("Credit lifecycle rail", "timeline", [
        "DESIGN OR VALIDATION -> method and project accepted",
        "MONITORING -> activity and outcome recorded",
        "VERIFICATION -> evidence examined",
        "ISSUANCE AND TRANSFER -> tradable unit enters registry",
        "RETIREMENT -> unit removed from circulation for a claim",
    ], [FACTS[6][0], FACTS[7][0]]),
    panel("Accounting-risk firewall", "comparison-table", [
        "DOUBLE ISSUANCE -> more than one unit for one outcome",
        "DOUBLE USE -> one unit used more than once",
        "DOUBLE CLAIMING -> same outcome claimed by multiple actors",
        "CORRESPONDING ADJUSTMENT -> international accounting treatment",
        "RULE -> adjustment is not issuance transfer or retirement",
    ], [FACTS[8][0], FACTS[9][0]]),
    panel("India CCTS stage ladder", "hierarchy", [
        "LEGAL BASIS -> enabling framework",
        "SCHEME DESIGN -> compliance and offset pathways",
        "TARGET OR METHODOLOGY -> obligation and credit rules",
        "ISSUANCE AND TRADING -> operational transactions",
        "PRICE AND VOLUME -> dated market evidence only",
    ], [FACTS[10][0], FACTS[20 - 1][0]]),
    panel("CCUS chain", "process-flow", [
        "SOURCE -> concentrated carbon dioxide stream",
        "CAPTURE AND CONDITIONING -> separation and preparation",
        "TRANSPORT -> pipeline ship road or other route",
        "UTILISATION OR STORAGE -> destination determines durability",
        "MONITORING AND CLOSURE -> permanence and responsibility",
    ], [FACTS[11][0], FACTS[12][0], FACTS[13][0]]),
    panel("Utilisation-storage test", "decision-tree", [
        "PRODUCT USE -> how long is carbon retained",
        "PROCESS USE -> does later release occur",
        "GEOLOGICAL STORAGE -> containment and monitoring",
        "LEAKAGE -> reversal risk and remediation",
        "NET BENEFIT -> full lifecycle accounting required",
    ], [FACTS[13][0], FACTS[14][0]]),
    panel("Capture technology comparison", "comparison-table", [
        "POINT SOURCE CCUS -> carbon intercepted before release",
        "DAC -> carbon separated from ambient air",
        "BECCS -> biogenic carbon plus capture and storage",
        "REMOVAL TEST -> atmospheric origin plus durable storage",
        "LIFECYCLE TEST -> energy land transport and reversal",
    ], [FACTS[15][0], FACTS[16][0], FACTS[17][0]]),
    panel("Net-zero mitigation hierarchy", "layered-rail", [
        "AVOID -> prevent unnecessary emissions",
        "REDUCE -> decarbonise existing activities",
        "CAPTURE -> address hard-to-abate point sources",
        "REMOVE -> counterbalance genuinely residual emissions",
        "VERIFY -> net balance needs one boundary and period",
    ], [FACTS[18][0], FACTS[4][0]]),
    panel("Carbon instruments answer spine", "answer-spine", [
        "CLASSIFY -> unit market and claim type",
        "TRACE -> baseline MRV issuance transfer retirement",
        "FOLLOW -> capture transport utilisation or storage",
        "TEST -> permanence leakage lifecycle and double counting",
        "AUDIT -> current rule price volume cost and capacity source",
    ], [FACTS[19][0], FACTS[10][0], FACTS[14][0]]),
]

PYQ_SOLUTIONS = [
    common.make_pyq_solution(
        FACTS, "2025", "GS-III",
        "Define CCUS and assess its potential role in tackling climate change.",
        "Verified routed Mains demand; no official model answer is claimed.",
        [11, 12, 13, 14, 16, 18, 19],
    ),
]

LIVE_SOURCES = [
    "https://unfccc.int/process-and-meetings/the-paris-agreement/article-64-mechanism — attempted 2026-09-03; Incapsula returned an empty noindex shell, so no Article 6 rule, status or transaction claim was imported.",
    "https://beeindia.gov.in/en/programmes/carbon-market — attempted 2026-09-03; the route redirected to a generic BEE landing page, so no current CCTS obligation, methodology, issuance, price or volume was imported.",
    "https://www.ipcc.ch/report/ar6/wg3/ — attempted 2026-09-03; substantive official text identified AR6 Working Group III as the mitigation assessment, but supplied no project capture rate, cost, storage capacity or DAC deployment figure.",
    "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1 — attempted 2026-09-03; the official landing page was not used for any topic-specific current claim.",
    "https://moef.gov.in/ — attempted 2026-09-03; no substantive topic-specific carbon-market, CCUS or DAC status text was retrieved.",
]

TOPIC_21 = common.topic(
    21,
    "Carbon Markets CCUS and Direct Air Capture",
    "21_Carbon-Markets-CCUS-and-Direct-Air-Capture",
    "learning-sessions/v2/subject-wide-syllabus/environment-and-ecology-21_Learning-Session.md",
    FACTS,
    TRAPS,
    [
        (10, "Distinguish allowances, credits and their lifecycle uses.", [0, 7, 8]),
        (10, "Compare cap-and-trade with baseline-and-credit markets.", [1, 2, 3]),
        (15, "Explain integrity requirements for a credible carbon credit.", [4, 5, 6, 7, 8, 9]),
        (15, "Explain the complete CCUS chain and its permanence requirements.", [11, 12, 13, 14]),
        (20, "Compare point-source CCUS, DAC and BECCS in a net-zero pathway.", [12, 15, 16, 17, 18]),
        (20, "Evaluate India's carbon-market and removal toolkit with strict status discipline.", [0, 2, 4, 6, 9, 10, 14, 18, 19]),
    ],
    SESSION_TITLES,
    ANSWER_ROUTES,
    PANELS,
    [
        "allowance", "credit", "cap-and-trade", "baseline-and-credit",
        "compliance", "voluntary", "avoidance", "reduction", "removal",
        "additionality", "monitoring", "reporting", "verification",
        "issuance", "retirement", "corresponding adjustment",
        "Carbon Credit Trading Scheme", "capture", "transport", "utilisation",
        "storage", "permanence", "leakage", "Direct Air Capture", "point-source",
        "BECCS", "residual emissions", "lifecycle",
    ],
    (
        "Audited ledgers route the verified 2025 GS-III CCUS demand and objective "
        "demands on Paris Article 6 and Direct Air Capture. Objective keys are "
        "not inferred, and no carbon-market transaction is presented as a PYQ."
    ),
    PYQ_SOLUTIONS,
    LIVE_SOURCES,
    (
        "Official retrieval confirmed only the broad IPCC mitigation context. "
        "UNFCCC was blocked and the BEE route was generic; therefore no current "
        "carbon price, volume, methodology, Article 6 delivery status, CCTS "
        "obligation, capture rate, cost, storage capacity or DAC deployment is asserted."
    ),
    extra=[
        "basic/17_Climate-Change-Science-Greenhouse-Effect.md",
        "basic/19_UNFCCC-COP-Kyoto-Paris-Agreement.md",
        "basic/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md",
        "basic/25_Renewable-Energy-and-Green-Hydrogen.md",
        "advanced/19_UNFCCC-COP-Kyoto-Paris-Agreement.md",
        "advanced/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md",
        "advanced/25_Renewable-Energy-and-Green-Hydrogen.md",
    ],
    pyq_audit_heading="AUDITED CARBON-MARKET, ARTICLE 6, CCUS AND DAC PYQ OWNERSHIP",
    register_headings=(
        "MARKET UNIT, CLAIM TYPE AND ACCOUNTING MAP",
        "CCUS, DAC, BECCS, PERMANENCE AND LIFECYCLE TRAPS",
        "CARBON-INSTRUMENT ANSWER SPINE",
        "LIVE PRICE, VOLUME, METHODOLOGY, RULE AND DEPLOYMENT EVIDENCE BOUNDARY",
    ),
    register_answer_spine=[
        "CLASSIFY ALLOWANCE VERSUS CREDIT AND COMPLIANCE VERSUS VOLUNTARY",
        "DISTINGUISH CAP-AND-TRADE FROM BASELINE-AND-CREDIT",
        "CLASSIFY AVOIDANCE REDUCTION AND ATMOSPHERIC REMOVAL",
        "TRACE BASELINE MRV ISSUANCE TRANSFER RETIREMENT AND ACCOUNTING",
        "TRACE CAPTURE TRANSPORT UTILISATION STORAGE MONITORING AND CLOSURE",
        "TEST PERMANENCE LEAKAGE LIFECYCLE AND RESIDUAL-EMISSIONS ROLE",
        "CONCLUDE WITH DATED RULE MARKET COST CAPACITY AND DEPLOYMENT EVIDENCE",
    ],
    allow_existing_history=True,
)
