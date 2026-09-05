"""Authored Economy learner-v2 data for Topics 20-23."""

from __future__ import annotations

import generate_economy_common as common


STEMS = {
    20: "20_Foreign-Trade-WTO-FTAs-and-Protectionism",
    21: "21_IMF-World-Bank-ADB-AIIB-NDB-and-Global-Governance",
    22: "22_Employment-Labour-Codes-Skills-and-Demographic-Dividend",
    23: "23_Poverty-Inequality-Social-Sector-and-Inclusive-Growth",
}


def panel(
    topic_number: int,
    title: str,
    kind: str,
    lines: list[str],
) -> tuple[str, str, str, list[str]]:
    stem = STEMS[topic_number]
    return (
        title,
        kind,
        "\n".join(lines),
        [
            f"upsc-ai-kit/knowledge/Economy/basic/{stem}.md",
            f"upsc-ai-kit/knowledge/Economy/advanced/{stem}.md",
        ],
    )


FACTS_20 = [
    ("Trade-policy transmission", "A tariff, standard or agreement first changes landed prices and market access, then affects sourcing, investment, output, jobs and consumers; a border measure is not itself an outcome."),
    ("Merchandise and services boundary", "Merchandise trade records cross-border goods, while services trade follows service-supply concepts; neither should be silently substituted for total exports, imports or the broader current account."),
    ("Tariff boundary", "A tariff is a customs tax on imported goods; its producer protection can coexist with higher costs for consumers and downstream firms using the import as an input."),
    ("Non-tariff measure boundary", "A non-tariff measure may pursue a legitimate health, safety or quality objective, but its design and application determine whether it becomes discriminatory or unnecessarily trade-restrictive."),
    ("MFN treatment", "WTO most-favoured-nation treatment generally requires a trade advantage granted to one member to be extended to other members, subject to agreement-specific exceptions."),
    ("National treatment", "WTO national treatment concerns internal treatment after an imported product or service has entered the market; charging an ordinary border tariff is not by itself a national-treatment violation."),
    ("Bound and applied tariffs", "A WTO bound tariff is a negotiated ceiling, while the applied tariff is the rate actually charged; policy space exists when the applied rate remains below the binding."),
    ("FTA legal and status boundary", "An FTA creates preferences under agreed coverage, schedules and exceptions; signed, ratified, entered-into-force and under-negotiation are different legal statuses."),
    ("Rules of origin", "Rules of origin determine whether a good qualifies for an FTA preference and are distinct from the preferential tariff rate itself."),
    ("Trade creation and diversion", "Trade creation replaces higher-cost domestic supply with lower-cost partner supply, while trade diversion replaces a lower-cost non-member source with a higher-cost preferred partner."),
    ("Trade-remedy categories", "Anti-dumping, countervailing and safeguard actions have different legal predicates: dumping, subsidisation and serious injury from an import surge must not be treated as one generic protection tool."),
    ("DGTR and notification boundary", "The Directorate General of Trade Remedies investigates specified Indian trade-remedy cases, but an investigation or recommendation is not the same as a final notified duty."),
    ("TRIMS scope", "The WTO Agreement on Trade-Related Investment Measures concerns goods-related measures inconsistent with GATT disciplines, including local-content and trade-balancing requirements; it is not a general investment treaty."),
    ("TRIPS and domestic rights", "TRIPS sets minimum intellectual-property standards, while grant, validity, enforcement and commercialisation of a patent or geographical indication remain governed through domestic institutions and law."),
    ("International Grains Council", "The International Grains Council is an intergovernmental grain-trade and market-transparency body, not a UN relief agency, domestic procurement authority or price-setting organisation."),
    ("Protection and downstream competitiveness", "Protecting an upstream input can weaken downstream export competitiveness when the input cost rises, so nominal protection must be assessed across the value chain."),
    ("GVC capability conditions", "Global value-chain participation depends on reliable logistics, customs, standards, imported inputs, finance, technology and investment predictability rather than low wages alone."),
    ("WTO dispute-settlement status", "The WTO Appellate Body has been unable to hear new appeals since December 2019, while first-level panels and notified appeals continue; weakened appellate review is not the disappearance of all dispute settlement."),
    ("Public stockholding boundary", "WTO agriculture rules and the interim peace-clause route for eligible public-stockholding programmes must be kept distinct from a permanent negotiated solution, which the owner records as unresolved."),
    ("Resilience versus autarky", "Trade resilience diversifies suppliers, markets and capabilities; it does not require indiscriminate self-sufficiency or permanent economy-wide protection."),
]

TRAPS_20 = [
    "Do not equate merchandise trade, services trade, total trade and the current account.",
    "Do not quote a tariff without distinguishing the bound ceiling from the applied rate.",
    "Do not treat MFN and national treatment as the same stage of non-discrimination.",
    "Do not describe every FTA product as duty-free immediately or ignore legal status.",
    "Do not treat rules of origin as a tariff or proof of domestic value addition.",
    "Do not merge dumping, subsidisation and import-surge safeguards.",
    "Do not turn an investigation or recommendation into a notified remedy.",
    "Do not infer a WTO dispute outcome or PYQ answer letter from a routed demand.",
    "Do not call the Appellate Body impasse the end of every WTO panel process.",
    "Do not use protectionism and resilience as synonyms.",
]

PANELS_20 = [
    panel(20, "Trade transmission rail", "cause-effect-rail", ["BORDER RULE", "-> LANDED PRICE + MARKET ACCESS", "-> SOURCING + INVESTMENT", "-> OUTPUT + JOBS + CONSUMERS"]),
    panel(20, "Trade-account boundary", "comparison-matrix", ["MERCHANDISE -> goods crossing borders", "SERVICES -> mode-specific supply", "TOTAL TRADE -> state included components", "CURRENT ACCOUNT -> broader than trade balance"]),
    panel(20, "WTO non-discrimination map", "two-stage-map", ["MFN -> treatment across trading partners", "NATIONAL TREATMENT -> internal treatment after entry", "EXCEPTIONS -> agreement-specific conditions", "CUSTOMS DUTY -> border stage"]),
    panel(20, "Tariff space ladder", "status-ladder", ["BOUND RATE -> negotiated ceiling", "APPLIED RATE -> rate actually charged", "WATER -> gap between the two", "CHANGE -> preserve schedule + date"]),
    panel(20, "FTA status and origin chain", "process-flow", ["NEGOTIATING -> SIGNED -> RATIFIED", "-> ENTERED INTO FORCE", "PRODUCT COVERAGE + PHASE-DOWN", "RULES OF ORIGIN -> preference eligibility"]),
    panel(20, "Creation versus diversion", "comparison-matrix", ["TRADE CREATION -> lower-cost partner replaces domestic supply", "TRADE DIVERSION -> preferred partner displaces cheaper outsider", "TEST -> welfare + productivity", "DO NOT infer from gross trade alone"]),
    panel(20, "Trade-remedy decision tree", "decision-tree", ["DUMPING + INJURY -> anti-dumping route", "SUBSIDY + INJURY -> countervailing route", "IMPORT SURGE + SERIOUS INJURY -> safeguard", "DGTR FINDING -> not final duty"]),
    panel(20, "TRIMS and TRIPS boundary", "agreement-map", ["TRIMS -> goods-linked investment measures", "TRIPS -> minimum IP standards", "GATS -> services rules", "DOMESTIC LAW -> grant + enforcement"]),
    panel(20, "IGC objective trap", "institution-card", ["INTERGOVERNMENTAL GRAIN-TRADE BODY", "MARKET INFORMATION + COOPERATION", "NOT UN RELIEF AGENCY", "NOT FCI PROCUREMENT OR PRICE SETTING"]),
    panel(20, "Protection cost cascade", "cause-effect-board", ["UPSTREAM TARIFF", "-> INPUT COST", "-> DOWNSTREAM EXPORT PRICE", "-> COMPETITIVENESS + CONSUMER EFFECT"]),
    panel(20, "WTO dispute-settlement status", "status-board", ["PANELS CONTINUE", "APPELLATE BODY -> no new appeals since Dec 2019", "NOTIFIED APPEALS ACCUMULATE", "WEAKENED SYSTEM != NO SYSTEM"]),
    panel(20, "Trade-policy answer spine", "answer-spine", ["DEFINE legal category + status", "TRACE value-chain incidence", "TEST consumers + firms + workers", "CONCLUDE capability + diversification"]),
]

PYQS_20 = [
    common.make_pyq_solution(
        FACTS_20,
        "2018",
        "GS-III",
        "Protectionism and currency manipulation impact on macroeconomic stability.",
        "Official-paper demand routed in the audited 2018-2023 GS-III ledger; no official model answer is claimed.",
        [0, 1, 2, 15, 19],
    ),
    common.make_pyq_solution(
        FACTS_20,
        "2025",
        "GS-III",
        "Challenges to the Indian economy amid protectionism and bilateralism.",
        "Official-paper demand routed in the audited 2024-2025 GS-III ledger; answer uses only source-bounded categories.",
        [7, 8, 9, 16, 17, 19],
    ),
]

TOPIC_20 = common.topic(
    20,
    "Foreign Trade, WTO, FTAs and Protectionism",
    STEMS[20],
    f"{STEMS[20]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_20,
    TRAPS_20,
    [
        (10, "Distinguish MFN treatment, national treatment and an FTA preference.", [4, 5, 7]),
        (10, "Why can protection of an upstream industry reduce downstream export competitiveness?", [2, 15, 16]),
        (15, "Compare anti-dumping, countervailing and safeguard action.", [10, 11]),
        (15, "Evaluate FTAs through legal status, origin rules, trade creation and trade diversion.", [7, 8, 9]),
        (20, "How should India respond to protectionism without moving towards indiscriminate autarky?", [0, 3, 15, 16, 17, 19]),
        (20, "Assess the WTO's continuing relevance amid weakened appellate dispute settlement.", [4, 5, 6, 10, 17, 18]),
    ],
    [
        "Trade-policy transmission and accounting boundaries",
        "Merchandise and services trade",
        "Tariffs and value-chain incidence",
        "Non-tariff measures",
        "Most-favoured-nation treatment",
        "National treatment and border treatment",
        "Bound and applied tariffs",
        "FTA coverage and legal status",
        "Rules of origin",
        "Trade creation and trade diversion",
        "Trade remedies and DGTR",
        "TRIMS",
        "TRIPS, geographical indications and domestic law",
        "IGC, GVCs and downstream competitiveness",
        "WTO dispute settlement, stockholding and resilience",
    ],
    [
        "Move from the border instrument to prices, firms, workers, consumers and macroeconomic stability.",
        "State the WTO legal category and agreement status before making a policy claim.",
        "Prefer diversified capability, predictable rules and adjustment support over permanent protection.",
    ],
    PANELS_20,
    ["most-favoured-nation", "national treatment", "bound tariff", "rules of origin", "trade creation", "trade diversion", "Directorate General of Trade Remedies", "TRIMS", "TRIPS", "International Grains Council", "December 2019", "peace clause"],
    "Audited ledgers route the 2018 and 2025 GS-III protectionism demands and objective demands on edible oils, geographical indications, merchandise/services trade, TRIMS, the International Grains Council and apple/GM-food distinctions. Objective answer letters are not reproduced or inferred.",
    PYQS_20,
    [
        "https://www.wto.org/english/thewto_e/whatis_e/tif_e/fact2_e.htm — retrieved 2026-09-03; substantive WTO text supports MFN, national treatment, bindings, transparency and qualified protection.",
        "https://www.wto.org/english/tratop_e/dispu_e/appellate_body_e.htm — retrieved 2026-09-03; substantive current page lists notified appeals and supports the continuing appellate impasse without inferring dispute outcomes.",
    ],
    "The live WTO pages were substantively retrievable. They support stable legal categories and the continuing appellate-review impairment; no tariff rate, trade share, deficit, agreement status or dispute result was imported.",
    extra=[
        "basic/19_Balance-of-Payments-Exchange-Rates-and-Forex-Reserves.md",
        "advanced/19_Balance-of-Payments-Exchange-Rates-and-Forex-Reserves.md",
        "basic/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
        "advanced/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
    ],
)


FACTS_21 = [
    ("Institution-comparison frame", "International institutions must be compared by mandate, client, instrument, governance, conditionality and lending window rather than grouped as one pool of external finance."),
    ("IMF mandate", "The IMF supports monetary cooperation, surveillance and balance-of-payments financing; its core function is not long-lived project construction."),
    ("IMF quota functions", "An IMF member's quota relates to financial contribution, voting power, access to resources and its share in general SDR allocations; the current numerical share requires a dated IMF source."),
    ("SDR boundary", "A Special Drawing Right is an IMF-created international reserve asset valued from a currency basket; it is neither retail currency, budget revenue nor automatically an IMF loan."),
    ("Reserve tranche position", "A reserve tranche position is a member's liquid claim on the IMF arising from quota resources and is treated as a reserve asset; it is distinct from conditional programme borrowing."),
    ("Gold tranche terminology", "Gold tranche is the historical name associated with what modern IMF usage calls the reserve tranche position, not an additional separate lending facility."),
    ("RFI and programme lending", "The Rapid Financing Instrument provides urgent balance-of-payments support with limited ex-post programme structure, while arrangements such as the SBA or EFF involve phased access and programme reviews."),
    ("World Bank boundary", "The term World Bank commonly refers to IBRD and IDA, while the World Bank Group also includes institutions with private-investment and guarantee mandates."),
    ("IBRD and IDA", "IBRD and IDA both support sovereign development but on different eligibility and financing terms; they must not be presented as identical lending windows."),
    ("IFC and MIGA", "IFC supports private-sector development through finance and mobilisation, while MIGA provides political-risk insurance or credit enhancement; neither is an IMF stabilisation window."),
    ("ADB mandate", "The Asian Development Bank is a regional development bank serving Asia and the Pacific through sovereign, private-sector, knowledge and technical-assistance operations."),
    ("AIIB mandate", "The Asian Infrastructure Investment Bank is a multilateral development bank focused on sustainable infrastructure and connectivity; current membership or voting figures require a dated institutional source."),
    ("NDB mandate", "The New Development Bank was founded by BRICS countries to mobilise resources for infrastructure and sustainable development in member emerging and developing economies."),
    ("Nature Solutions Finance Hub", "The Nature Solutions Finance Hub for Asia and the Pacific is an ADB initiative, an audited 2025 Prelims concept; any current financing total or project count requires a dated ADB source."),
    ("Conditionality and safeguards", "Macroeconomic programme conditionality, project procurement rules and environmental-social safeguards serve different purposes and should not be collapsed into one generic lender condition."),
    ("Project and policy-based lending", "Project lending finances a bounded investment, while policy-based lending supports an agreed reform programme; disbursement conditions and evaluation units therefore differ."),
    ("Guarantees and co-financing", "A guarantee absorbs specified risks and co-financing combines institutions or financiers; neither means that one lender funds or bears every project risk."),
    ("Currency-risk boundary", "Foreign-currency development finance can be concessional or long-term yet still create exchange-rate exposure for a borrower whose revenues are in domestic currency."),
    ("DSSI and Common Framework", "The Debt Service Suspension Initiative temporarily deferred eligible official bilateral payments, while the G20 Common Framework aims at case-specific debt treatment beyond mere suspension."),
    ("Global-governance reform", "Governance reform concerns voice, quota or shareholding representation, leadership, crisis resources, debt coordination and development additionality; creating a new bank does not by itself solve each deficit."),
]

TRAPS_21 = [
    "Do not describe IMF balance-of-payments support as ordinary infrastructure project lending.",
    "Do not quote quota, voting, membership or finance figures without a dated institutional source.",
    "Do not call SDRs currency, budget revenue or an IMF loan.",
    "Do not treat gold tranche and reserve tranche position as separate facilities.",
    "Do not merge RFI emergency support with phased SBA or EFF programme lending.",
    "Do not use World Bank and World Bank Group as exact synonyms.",
    "Do not merge IBRD, IDA, IFC and MIGA clients or instruments.",
    "Do not treat ADB, AIIB and NDB as interchangeable or as replacements for the IMF.",
    "Do not equate DSSI payment suspension with Common Framework debt treatment.",
    "Do not infer an objective PYQ answer letter from a routed concept.",
]

PANELS_21 = [
    panel(21, "Institution comparison grid", "comparison-matrix", ["MANDATE -> stabilisation or development purpose", "CLIENT -> sovereign or private counterparty", "INSTRUMENT -> loan, guarantee, surveillance or advice", "GOVERNANCE + CONDITIONALITY -> voice and implementation rules"]),
    panel(21, "IMF function rail", "process-flow", ["SURVEILLANCE", "-> EXTERNAL FINANCING NEED", "-> FACILITY + CONDITIONALITY", "-> REVIEWS + REPAYMENT"]),
    panel(21, "Quota and SDR map", "relationship-map", ["QUOTA -> contribution", "QUOTA -> voting + access", "QUOTA -> general SDR allocation share", "SDR -> reserve asset; not loan"]),
    panel(21, "Reserve tranche trap", "terminology-board", ["RESERVE TRANCHE POSITION -> liquid IMF claim", "GOLD TRANCHE -> historical name", "PROGRAMME CREDIT -> separate borrowing", "RESERVE ASSET != fiscal receipt"]),
    panel(21, "IMF facility ladder", "comparison-ladder", ["RFI -> urgent one-off support", "SBA -> shorter stabilisation arrangement", "EFF -> medium-term structural need", "VERIFY current access limits separately"]),
    panel(21, "World Bank Group map", "institution-map", ["IBRD -> eligible sovereign borrowers", "IDA -> concessional sovereign window", "IFC -> private sector", "MIGA -> political-risk guarantees"]),
    panel(21, "Development-bank family", "comparison-matrix", ["ADB -> Asia-Pacific regional bank", "AIIB -> sustainable infrastructure + connectivity", "NDB -> BRICS-founded development bank", "MANDATES overlap but governance differs"]),
    panel(21, "ADB PYQ anchor", "objective-card", ["NATURE SOLUTIONS FINANCE HUB", "LAUNCHED BY ADB", "ASIA AND THE PACIFIC", "DO NOT invent current finance totals"]),
    panel(21, "Lending-window distinction", "two-track-flow", ["PROJECT LOAN -> asset + appraisal", "POLICY LOAN -> reform programme", "GUARANTEE -> defined risk", "CO-FINANCE -> shared funding structure"]),
    panel(21, "Foreign-currency risk chain", "cause-effect-board", ["FOREIGN-CURRENCY LIABILITY", "DOMESTIC-CURRENCY REVENUE", "DEPRECIATION -> repayment burden", "CONCESSIONAL TERMS do not erase mismatch"]),
    panel(21, "Debt-treatment timeline", "timeline-strip", ["DSSI -> temporary suspension", "COMMON FRAMEWORK -> treatment beyond DSSI", "OFFICIAL + PRIVATE creditor coordination", "CASE STATUS -> verify by date"]),
    panel(21, "Global-governance answer spine", "answer-spine", ["COMPARE mandate + window", "TEST voice + ownership", "ASSESS additionality + debt", "CONCLUDE reformed plural multilateralism"]),
]

TOPIC_21 = common.topic(
    21,
    "IMF, World Bank, ADB, AIIB, NDB and Global Governance",
    STEMS[21],
    f"{STEMS[21]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_21,
    TRAPS_21,
    [
        (10, "Distinguish SDRs, the reserve tranche position and IMF programme borrowing.", [3, 4, 5, 6]),
        (10, "Differentiate IBRD, IDA, IFC and MIGA by client and instrument.", [7, 8, 9]),
        (15, "Compare the IMF with multilateral development banks.", [0, 1, 10, 11, 12, 14]),
        (15, "Why do project loans, policy-based loans and guarantees require different evaluation criteria?", [14, 15, 16]),
        (20, "Evaluate the role of ADB, AIIB and NDB in a plural development-finance architecture.", [10, 11, 12, 13, 16, 17]),
        (20, "What reforms can improve representation and effectiveness in global economic governance?", [2, 14, 18, 19]),
    ],
    [
        "How to compare international economic institutions",
        "IMF mandate and surveillance",
        "IMF quotas",
        "Special Drawing Rights",
        "Reserve tranche position and gold tranche",
        "Rapid Financing Instrument and programme arrangements",
        "World Bank and World Bank Group",
        "IBRD and IDA",
        "IFC and MIGA",
        "Asian Development Bank",
        "AIIB",
        "New Development Bank",
        "Nature Solutions Finance Hub",
        "Development lending, guarantees and currency risk",
        "DSSI, Common Framework and global-governance reform",
    ],
    [
        "Compare mandate, borrower, lending window, governance and conditionality before evaluating performance.",
        "Separate reserve assets, stabilisation finance, development loans and guarantees.",
        "Judge reform through representation, policy ownership, additionality, safeguards and debt sustainability.",
    ],
    PANELS_21,
    ["Special Drawing Right", "reserve tranche position", "gold tranche", "Rapid Financing Instrument", "IBRD", "IDA", "IFC", "MIGA", "Asian Development Bank", "Asian Infrastructure Investment Bank", "New Development Bank", "Common Framework"],
    "Audited Prelims ledgers route objective concepts on AIIB, the reserve or gold tranche, the Rapid Financing Instrument, the G20 Common Framework, ADB's Nature Solutions Finance Hub and IBRD. No direct Economy Mains demand is claimed and no objective answer letter is inferred.",
    [],
    [
        "https://www.imf.org/en/about/faq/quotas — direct factsheet access returned HTTP 403 on 2026-09-03; official-domain search exposed only qualitative quota functions, so no current figure was imported.",
        "https://www.worldbank.org/en/about/articles-of-agreement — official-domain results substantively distinguished IBRD, IDA, IFC and MIGA mandates; the redesigned landing page itself exposed only partial raw content.",
        "https://www.adb.org/what-we-do — official-domain search substantively exposed ADB's Asia-Pacific development mandate; no target or portfolio total was imported.",
        "https://www.aiib.org/en/about-aiib/index.html — official-domain search substantively exposed the sustainable-infrastructure mandate; membership and finance counts were excluded.",
        "https://www.ndb.int/about-ndb/ — official-domain search substantively exposed the infrastructure and sustainable-development mandate; strategy targets were excluded.",
    ],
    "Official institutional pages or official-domain search results supported qualitative mandates and lending-window distinctions. Direct IMF access was blocked and the World Bank landing page was only partially retrievable, so current quota, voting, membership, capital and finance figures were not used.",
    extra=[
        "basic/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md",
        "advanced/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md",
        "basic/19_Balance-of-Payments-Exchange-Rates-and-Forex-Reserves.md",
        "advanced/19_Balance-of-Payments-Exchange-Rates-and-Forex-Reserves.md",
        "basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md",
        "advanced/25_Climate-Economics-Green-Finance-and-Circular-Economy.md",
    ],
)


FACTS_22 = [
    ("Employment-quality frame", "Employment must be assessed through quantity, hours, productivity, real earnings, security, working conditions and mobility; a headcount alone is not a quality-jobs verdict."),
    ("LFPR denominator", "The labour-force participation rate is the labour force, employed plus unemployed seeking or available for work, as a share of the specified population."),
    ("Worker-population ratio", "The worker-population ratio is employed persons as a share of the specified population and therefore has a different numerator from LFPR."),
    ("Unemployment-rate denominator", "The unemployment rate is unemployed persons as a share of the labour force, not as a share of the total population; people outside the labour force are not unemployed."),
    ("PLFS status and reference period", "PLFS estimates must name the status concept and reference period, such as usual status or current weekly status, because the same labour market can produce different measures."),
    ("Unemployment typology", "Frictional, structural, cyclical, seasonal and disguised unemployment identify different mechanisms and cannot be diagnosed from one aggregate rate."),
    ("Human-capital formation", "Human-capital formation builds productive capabilities through health, education, skills and experience; certification is only one possible signal of capability."),
    ("Skill and placement boundary", "A completed training or certification count is not a placement, sustained job, wage gain or productivity outcome."),
    ("PMKVY scope", "Pradhan Mantri Kaushal Vikas Yojana supports skill training, assessment and certification under the Skill India architecture; current targets or placements require a dated official source."),
    ("Apprenticeship mechanism", "Apprenticeships combine workplace learning with employer demand and can reduce skill mismatch, but registration or seat creation does not prove completion or employment."),
    ("Demographic-dividend condition", "A favourable working-age structure creates only demographic potential; health, learning, participation, productive jobs and savings-investment transmission determine the dividend."),
    ("Female participation and care", "Women's labour-force participation is shaped by unpaid care, safety, mobility, job location and norms, so aggregate participation cannot substitute for gender and rural-urban disaggregation."),
    ("Care and monetised economy", "Unpaid care supports household and market production but generally lies outside the monetised national-accounts production boundary; economic value and GDP inclusion are different questions."),
    ("Four Labour Codes", "The Code on Wages, 2019 and the three 2020 Codes on industrial relations, social security and occupational safety, health and working conditions consolidate 29 central labour laws."),
    ("Enactment and commencement", "Enactment, notification of commencement, central rules, state rules and enforcement readiness are separate stages in labour-law implementation."),
    ("Current Labour-Code status", "Official Ministry material retrieved through official-domain search records commencement from 21 November 2025 and final Central Rules in May 2026; state rules and enforcement readiness still require jurisdiction-specific verification."),
    ("Concurrent-List implementation", "Labour's Concurrent-List setting means central codification does not by itself produce uniform state rules, inspection capacity or enforcement outcomes."),
    ("Gig and platform work", "Gig or platform work can offer entry and flexibility while creating risks around algorithmic control, bargaining power, income variability and portable social security."),
    ("Fixed-term and casual work boundary", "Fixed-term employment, casual work, contract labour and platform work are distinct legal and economic relationships; coverage under wage or social-security rules must be tested provision by provision."),
    ("Productivity and job creation", "Labour-productivity growth can raise incomes and competitiveness, but job outcomes depend on demand, sectoral composition, labour intensity, transition support and the distribution of productivity gains."),
]

TRAPS_22 = [
    "Do not use total population as the unemployment-rate denominator.",
    "Do not treat people outside the labour force as unemployed.",
    "Do not quote PLFS data without status, reference period, age group and geography.",
    "Do not infer job quality from an employment headcount.",
    "Do not equate skill certification with placement or wage progression.",
    "Do not describe the demographic dividend as automatic or permanent.",
    "Do not equate unpaid care's GDP exclusion with absence of economic value.",
    "Do not merge Labour-Code enactment, commencement, rules and enforcement.",
    "Do not assume Central Rules establish uniform state implementation.",
    "Do not infer an objective PYQ answer letter from the routed ledger.",
]

PANELS_22 = [
    panel(22, "Jobs quality dashboard", "evaluation-board", ["QUANTITY + HOURS", "PRODUCTIVITY + REAL EARNINGS", "SECURITY + CONDITIONS", "MOBILITY + PROTECTION"]),
    panel(22, "Labour indicators matrix", "formula-board", ["LFPR = labour force / specified population", "WPR = employed / specified population", "UR = unemployed / labour force", "DENOMINATOR must be named"]),
    panel(22, "PLFS reference-period clock", "comparison-strip", ["USUAL STATUS -> longer reference", "CURRENT WEEKLY STATUS -> seven-day reference", "AGE + RURAL/URBAN -> always state", "ONE headline cannot replace disaggregation"]),
    panel(22, "Unemployment mechanism tree", "classification-tree", ["FRICTIONAL -> transition", "STRUCTURAL -> mismatch", "SEASONAL / CYCLICAL -> timing + demand", "DISGUISED -> surplus labour"]),
    panel(22, "Human-capital chain", "cause-effect-rail", ["HEALTH + FOUNDATION LEARNING", "-> SKILL + EXPERIENCE", "-> PRODUCTIVE MATCH", "-> EARNINGS + ADAPTABILITY"]),
    panel(22, "Certification-to-outcome ladder", "status-ladder", ["ENROLLED", "-> TRAINED", "-> CERTIFIED", "-> PLACED -> RETAINED -> WAGE GAIN"]),
    panel(22, "Demographic dividend converter", "conversion-flow", ["WORKING-AGE SHARE", "x HEALTH + EDUCATION", "x PARTICIPATION + JOBS", "x PRODUCTIVITY -> DIVIDEND"]),
    panel(22, "Care-economy constraint map", "two-track-map", ["UNPAID CARE -> time constraint", "CARE SERVICES -> participation support", "GDP BOUNDARY -> not value judgement", "3R -> recognise + reduce + redistribute"]),
    panel(22, "Labour Codes map", "institution-map", ["WAGES 2019", "INDUSTRIAL RELATIONS 2020", "SOCIAL SECURITY 2020", "OSHWC 2020"]),
    panel(22, "Implementation status rail", "status-flow", ["ENACTED 2019-20", "-> COMMENCEMENT 21 NOV 2025", "-> FINAL CENTRAL RULES MAY 2026", "-> STATE RULES + ENFORCEMENT vary"]),
    panel(22, "New-work boundary", "comparison-matrix", ["FIXED-TERM", "CASUAL / CONTRACT", "GIG / PLATFORM", "TEST wages + security + bargaining separately"]),
    panel(22, "Employment answer spine", "answer-spine", ["DEFINE indicator + denominator", "DIAGNOSE unemployment type", "LINK skills to demand", "CONCLUDE jobs + earnings + portable protection"]),
]

PYQS_22 = [
    common.make_pyq_solution(FACTS_22, "2022", "GS-III", "Labour-productivity-led growth and the job-creation pattern India should follow.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [0, 6, 9, 19]),
    common.make_pyq_solution(FACTS_22, "2023", "GS-III", "Structural unemployment in India and improvements in computation methodology.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [1, 2, 3, 4, 5]),
    common.make_pyq_solution(FACTS_22, "2023", "GS-III", "Distinguish the care economy from the monetised economy and explain their integration.", "Official scan wording is recorded as verified in the audited routing ledger.", [11, 12, 17]),
    common.make_pyq_solution(FACTS_22, "2024", "GS-III", "Merits and demerits of the four Labour Codes.", "Official-paper demand routed in the audited 2024-2025 GS-III ledger; current status is separately dated.", [13, 14, 15, 16, 18]),
]

TOPIC_22 = common.topic(
    22,
    "Employment, Labour Codes, Skills and Demographic Dividend",
    STEMS[22],
    f"{STEMS[22]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_22,
    TRAPS_22,
    [
        (10, "Distinguish LFPR, worker-population ratio and unemployment rate.", [1, 2, 3, 4]),
        (10, "Why is skill certification not an adequate employment outcome?", [6, 7, 8, 9]),
        (15, "Explain how India can convert demographic potential into a demographic dividend.", [6, 10, 11, 19]),
        (15, "Discuss the relationship between the care economy and women's labour-force participation.", [11, 12, 17]),
        (20, "Evaluate the four Labour Codes through legal status, worker protection, firm incentives and state capacity.", [13, 14, 15, 16, 18]),
        (20, "Design an employment strategy that combines productivity, labour demand, skills and portable protection.", [0, 5, 6, 9, 17, 19]),
    ],
    [
        "Employment quantity and job quality",
        "Labour-force participation rate",
        "Worker-population ratio",
        "Unemployment rate and denominator",
        "PLFS status and reference periods",
        "Types of unemployment",
        "Human-capital formation",
        "Skill certification and placement",
        "PMKVY and apprenticeships",
        "Demographic dividend",
        "Female participation",
        "Care economy and monetised economy",
        "The four Labour Codes",
        "Commencement, rules and Concurrent-List implementation",
        "Gig work, employment forms and productivity-led job creation",
    ],
    [
        "Begin with the indicator, denominator and reference period before interpreting a labour-market trend.",
        "Trace training through employer demand, placement, retention, earnings and productivity.",
        "Balance flexibility and job creation with bargaining, safety and portable social protection.",
    ],
    PANELS_22,
    ["labour-force participation rate", "worker-population ratio", "unemployment rate", "Periodic Labour Force Survey", "human-capital formation", "Pradhan Mantri Kaushal Vikas Yojana", "demographic dividend", "care economy", "Code on Wages, 2019", "21 November 2025", "May 2026", "Concurrent List"],
    "Audited ledgers route Mains demands on productivity-led job creation, structural-unemployment measurement, the care economy, Labour Codes, inflation and unemployment, and skill-to-employment linkages, plus objective concepts on human capital, PMKVY, fixed-term work, casual workers and industrial-dispute statistics. No objective key is inferred.",
    PYQS_22,
    [
        "https://labour.gov.in/offerings/schemes-and-services/details/labour-codes-gzNzQzMtQWa — direct fetch returned HTTP 403 on 2026-09-03; official-domain search substantively exposed commencement and Central-Rules milestones.",
        "https://www.labour.gov.in/documents/acts-and-policies — official-domain search identified the Ministry's current Labour Codes and rules pages; jurisdiction-specific state readiness was not fully retrievable.",
    ],
    "Official Ministry search results support commencement on 21 November 2025 and final Central Rules in May 2026. Direct pages and the annual-report PDF returned HTTP 403, so no state-by-state rule count, employment value, scheme target or outlay was added.",
    extra=[
        "basic/02_Growth-Development-HDI-IHDI-and-MPI.md",
        "advanced/02_Growth-Development-HDI-IHDI-and-MPI.md",
        "basic/03_Inflation-Price-Indices-and-Business-Cycles.md",
        "advanced/03_Inflation-Price-Indices-and-Business-Cycles.md",
        "basic/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md",
        "advanced/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md",
        "basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md",
        "advanced/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md",
    ],
)


FACTS_23 = [
    ("Poverty and inequality boundary", "Poverty measures shortfall below a stated threshold, while inequality measures dispersion across a distribution; poverty can fall even when inequality rises."),
    ("Absolute and relative poverty", "Absolute poverty uses a defined minimum standard, while relative poverty evaluates position against the prevailing distribution or social standard."),
    ("Headcount and poverty gap", "The poverty headcount ratio measures incidence, while the poverty gap captures average depth below the line; neither alone describes every deprivation."),
    ("Poverty-line vintage", "A poverty estimate is inseparable from its line, price basis, survey, reference period and methodology; estimates from different vintages should not be presented as one continuous series."),
    ("Tendulkar and Rangarajan", "The Tendulkar and Rangarajan expert-group methods use different consumption baskets and thresholds; neither should be mislabeled as a timeless current official poverty line."),
    ("Lorenz curve and Gini", "The Lorenz curve represents cumulative distribution, while the Gini coefficient summarises inequality; income, consumption and wealth data can produce different results."),
    ("MPI architecture", "India's national Multidimensional Poverty Index follows an Alkire-Foster structure across health, education and standard-of-living dimensions using twelve indicators."),
    ("MPI formula", "The multidimensional poverty index combines the headcount ratio of multidimensionally poor people with their average intensity of deprivation, conventionally expressed as MPI equals H multiplied by A."),
    ("Observed and projected MPI", "The 2019-21 national MPI estimate is tied to NFHS-5 observations, while NITI Aayog's 2022-23 figure is an estimate projected from earlier reduction trends rather than a fresh household survey."),
    ("Inclusive-growth frame", "Inclusive growth combines productive participation, quality public services, redistribution and protection against shocks; growth and distribution are related but distinct tests."),
    ("Growth elasticity of poverty", "The poverty reduction generated by growth depends on initial inequality, sectoral composition, labour intensity and access to assets and services."),
    ("Social-sector spending chain", "Budget allocation, release, actual spending, service availability, service quality and household outcome are separate stages; expenditure is not itself an outcome."),
    ("Universal and targeted provision", "Universal public services and targeted benefits can complement each other, while targeting saves resources but creates exclusion, inclusion and transaction-cost risks."),
    ("Social assistance and insurance", "Social assistance is generally tax-financed support based on need or category, while social insurance pools contributions or specified risks; both differ from universal public services."),
    ("MGNREGA boundary", "MGNREGA is a demand-driven legal employment guarantee for rural households, not an unconditional cash transfer or proof that every demand for work was met."),
    ("NFSA boundary", "The National Food Security Act creates legal food and nutrition entitlements through an in-kind architecture; statutory coverage rules and actual beneficiary inclusion are different questions."),
    ("Health-protection boundary", "Hospitalisation insurance can reduce catastrophic inpatient costs but cannot by itself replace primary care, public-health capacity, outpatient access or service quality."),
    ("Financial inclusion", "Financial inclusion requires access, usage and quality of suitable services; account ownership alone does not prove credit access, income growth or poverty exit."),
    ("Intergenerational and spatial inequality", "Inclusive-growth analysis must examine mobility across generations and disparities across states, districts, social groups, gender and rural-urban locations rather than rely on a national average."),
    ("Shock-responsive inclusion", "Social protection should prevent temporary health, climate or employment shocks from becoming persistent poverty traps while retaining a pathway to productive capability and fiscal sustainability."),
]

TRAPS_23 = [
    "Do not use poverty and inequality as synonyms.",
    "Do not quote a poverty estimate without its line, methodology, period and price basis.",
    "Do not merge headcount incidence with poverty-gap depth.",
    "Do not treat Tendulkar and Rangarajan estimates as one current official series.",
    "Do not compare income, consumption and wealth Gini values as if they used one base.",
    "Do not present the projected 2022-23 MPI estimate as a fresh household survey result.",
    "Do not equate social-sector allocation, expenditure, service quality and outcome.",
    "Do not treat a bank account as proof of inclusive growth.",
    "Do not assume a national average describes every state, district or group.",
    "Do not infer an objective PYQ answer letter from a routed demand.",
]

PANELS_23 = [
    panel(23, "Poverty and inequality map", "comparison-matrix", ["POVERTY -> threshold shortfall", "INEQUALITY -> distributional dispersion", "BOTH can move differently", "STATE metric + data base"]),
    panel(23, "Poverty-measure ladder", "measurement-ladder", ["HEADCOUNT -> incidence", "POVERTY GAP -> depth", "SEVERITY -> distribution among poor", "MPI -> multiple deprivations"]),
    panel(23, "Methodology clock", "vintage-strip", ["LINE + BASKET", "PRICE BASIS + SURVEY", "REFERENCE PERIOD", "COMPARABILITY before trend"]),
    panel(23, "Committee distinction", "comparison-board", ["TENDULKAR -> one methodology vintage", "RANGARAJAN -> revised basket + threshold", "NO TIMELESS current line", "ATTRIBUTE every estimate"]),
    panel(23, "Lorenz and Gini map", "concept-map", ["PERFECT-EQUALITY LINE", "LORENZ CURVE", "AREA -> GINI summary", "INCOME / CONSUMPTION / WEALTH differ"]),
    panel(23, "MPI construction rail", "formula-flow", ["12 INDICATORS", "-> deprivation score", "-> H headcount + A intensity", "-> MPI = H x A"]),
    panel(23, "MPI vintage boundary", "status-board", ["NFHS-5 2019-21 -> observed base", "2022-23 -> projected estimate", "NOT fresh survey", "COMPARE editions cautiously"]),
    panel(23, "Inclusive-growth engine", "cause-effect-rail", ["PRODUCTIVE JOBS + ASSETS", "QUALITY HEALTH + EDUCATION", "REDISTRIBUTION + PROTECTION", "CAPABILITY + MOBILITY"]),
    panel(23, "Social-spending results chain", "results-chain", ["ALLOCATION", "-> RELEASE -> SPENDING", "-> SERVICE ACCESS + QUALITY", "-> HOUSEHOLD OUTCOME"]),
    panel(23, "Protection architecture", "institution-map", ["ASSISTANCE -> need/category", "INSURANCE -> pooled risk", "UNIVERSAL SERVICES -> broad access", "TARGETING -> exclusion risk"]),
    panel(23, "Named instrument boundary", "comparison-matrix", ["MGNREGA -> work guarantee", "NFSA -> food entitlement", "HEALTH INSURANCE -> hospitalisation protection", "FINANCE -> access + usage + quality"]),
    panel(23, "Inclusive-growth answer spine", "answer-spine", ["FIX metric + vintage", "TRACE jobs + services + transfers", "DISAGGREGATE groups + places", "CONCLUDE capability + resilience"]),
]

PYQS_23 = [
    common.make_pyq_solution(FACTS_23, "2019", "GS-III", "Inclusive-growth strategy for inclusiveness and sustainability objectives.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [9, 10, 12, 18, 19]),
    common.make_pyq_solution(FACTS_23, "2020", "GS-III", "Intra- and inter-generational equity in inclusive growth.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [5, 9, 10, 18, 19]),
    common.make_pyq_solution(FACTS_23, "2022", "GS-III", "Financial inclusion and inclusive growth under a market economy.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [9, 12, 17, 18]),
    common.make_pyq_solution(FACTS_23, "2022", "GS-III", "Community-health challenges arising from rising life expectancy in India.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [11, 13, 16, 18, 19]),
    common.make_pyq_solution(FACTS_23, "2024", "GS-III", "Public expenditure on social services after reforms and its relationship with inclusive growth.", "Official-paper demand routed in the audited 2024-2025 GS-III ledger.", [9, 11, 12, 16, 18]),
]

TOPIC_23 = common.topic(
    23,
    "Poverty, Inequality, Social Sector and Inclusive Growth",
    STEMS[23],
    f"{STEMS[23]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_23,
    TRAPS_23,
    [
        (10, "Distinguish poverty incidence, poverty depth and inequality.", [0, 1, 2, 5]),
        (10, "Why must the 2022-23 national MPI estimate be separated from NFHS-5 observations?", [6, 7, 8]),
        (15, "Explain why growth can reduce poverty while increasing inequality.", [0, 9, 10, 18]),
        (15, "Evaluate targeting against universal public services in India's social sector.", [11, 12, 13, 18]),
        (20, "Design an inclusive-growth strategy combining jobs, services, redistribution and shock protection.", [9, 10, 11, 12, 17, 19]),
        (20, "How should India measure and address poverty without collapsing methodology, distribution and capability into one indicator?", [2, 3, 4, 5, 6, 7, 8, 18]),
    ],
    [
        "Poverty and inequality",
        "Absolute and relative poverty",
        "Headcount ratio and poverty gap",
        "Poverty-line method and vintage",
        "Tendulkar and Rangarajan methods",
        "Lorenz curve and Gini coefficient",
        "National Multidimensional Poverty Index",
        "MPI headcount, intensity and formula",
        "Observed and projected MPI estimates",
        "Inclusive growth",
        "Growth elasticity of poverty",
        "Social-sector spending results chain",
        "Universal provision and targeting",
        "Social assistance, insurance and public services",
        "MGNREGA, NFSA, health protection, finance and shock response",
    ],
    [
        "Fix the poverty or inequality metric, data source, price basis and reference period before comparing estimates.",
        "Trace social expenditure from allocation to service quality and household outcome.",
        "Combine productive participation, universal basics, targeted protection and disaggregated accountability.",
    ],
    PANELS_23,
    ["absolute poverty", "relative poverty", "poverty gap", "Tendulkar Committee", "Rangarajan Committee", "Lorenz curve", "Gini coefficient", "Alkire-Foster", "MPI = H", "NFHS-5", "MGNREGA", "National Food Security Act"],
    "Audited ledgers route Mains demands on inclusive growth, inter-generational equity, financial inclusion, community health and social-service expenditure, plus the objective poverty-line variation concept. These demands are solved or retained in practice without inventing an official model answer or objective key.",
    PYQS_23,
    [
        "https://www.niti.gov.in/sites/default/files/2024-01/MPI-22_NITI-Aayog20254.pdf — direct fetch returned HTTP 403 on 2026-09-03; official-domain search substantively exposed the Alkire-Foster method, twelve indicators and projection basis.",
        "https://www.niti.gov.in/whats-new/multidimensional-poverty-india-2005-06 — direct fetch returned HTTP 403; official-domain search confirmed that the 2022-23 value is an estimate rather than a fresh survey observation.",
    ],
    "The official NITI pages were blocked to direct fetch, but official-domain search substantively exposed the national MPI method and the projected status of the 2022-23 estimate. No poverty rate, inequality value, scheme outlay or current beneficiary count was imported.",
    extra=[
        "basic/02_Growth-Development-HDI-IHDI-and-MPI.md",
        "advanced/02_Growth-Development-HDI-IHDI-and-MPI.md",
        "basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        "advanced/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        "basic/22_Employment-Labour-Codes-Skills-and-Demographic-Dividend.md",
        "advanced/22_Employment-Labour-Codes-Skills-and-Demographic-Dividend.md",
    ],
)
