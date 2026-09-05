"""Authored Economy learner-v2 data for Topics 11-15."""

from __future__ import annotations

import generate_economy_common as common


STEMS = {
    11: "11_Land-Reforms-Green-Revolution-and-Cropping-Systems",
    12: "12_MSP-Procurement-Buffer-Stocks-PDS-and-Food-Security",
    13: "13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains",
    14: "14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture",
    15: "15_Food-Processing-Cold-Chains-and-Value-Addition",
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


FACTS_11 = [
    ("Land-reform breadth", "Land reform covers abolition of intermediaries, tenancy regulation, ceilings, consolidation and land records; it is not synonymous with redistribution alone."),
    ("State implementation", "Land is principally state-administered, so outcomes vary with state law, political mobilisation, record quality, administrative capacity and local power relations."),
    ("Intermediary abolition", "Abolition of zamindari and other intermediary interests sought to connect the cultivator more directly with the state, but did not by itself settle tenancy, fragmentation or title disputes."),
    ("Tenancy reform", "Tenancy reform concerns rent regulation, security of tenure, recording of the actual cultivator and ownership or purchase rights under the applicable state law."),
    ("Land ceilings", "Ceiling laws limit permissible holdings and identify surplus land for redistribution, but exemptions, benami adjustment, litigation and weak detection can separate statutory intent from field outcome."),
    ("Consolidation", "Consolidation reorganises fragmented parcels into more workable holdings without necessarily changing aggregate ownership, while secure leasing separates ownership from cultivation under safeguards."),
    ("Land records", "Survey, settlement and updated land records are rights, credit, planning and dispute-resolution infrastructure; a legal reform cannot reach the actual cultivator if records remain inaccurate."),
    ("Operation Barga", "Operation Barga in West Bengal recorded sharecroppers and is evidence about tenancy security and implementation, not a Green-Revolution seed programme or a complete solution to fragmentation."),
    ("Kerala reform", "The Kerala Land Reforms Act is a named example of comparatively thorough tenancy abolition and ceiling implementation, while later smallholding and employment constraints remained."),
    ("Early Jammu and Kashmir reform", "The Big Landed Estates Abolition Act, 1950 in Jammu and Kashmir is a distinct early ceiling and estate-restructuring episode whose political-legal setting should not be generalised mechanically."),
    ("Green-Revolution package", "The Green Revolution was a complementary package of high-yielding seed, assured water, fertiliser, credit, extension, procurement and price support rather than a seed-only event."),
    ("Regional and crop concentration", "Early gains were concentrated in irrigated Punjab, Haryana and western Uttar Pradesh and in wheat and later rice, so national output gains coexisted with regional and crop imbalance."),
    ("Technology and institutions", "High-yielding varieties produced durable gains only where research, local adaptation, irrigation, input delivery, extension and market institutions operated together."),
    ("Cropping pattern", "Cropping pattern is the distribution of cultivated area among crops at a stated time and geography; exact shares are year-specific and cannot be treated as timeless."),
    ("Cropping intensity", "Cropping intensity compares gross cropped area with net sown area, so multiple cropping raises the ratio without necessarily expanding net cultivated land."),
    ("Diversification conditions", "Diversification toward pulses, oilseeds, horticulture, millets or allied activities needs water suitability, risk cover, storage, processing and remunerative demand, not a price slogan alone."),
    ("Water-intensive path dependence", "Rice, wheat and sugarcane incentives can reinforce water-intensive regional specialisation; crop choice must be read with irrigation source, energy pricing and procurement access."),
    ("Millet route", "Millets are dryland-oriented, relatively low-water and nutrient-dense crops, but their revival depends on seed, processing, procurement, consumer demand and region-specific agronomy."),
    ("Visvesvaraya contribution", "M. Visvesvaraya's named contribution is irrigation engineering, including automatic sluice gates and the block system; it must remain distinct from later crop-breeding achievements."),
    ("Swaminathan contribution", "M.S. Swaminathan's scientific contribution centred on adapting semi-dwarf wheat and rice technologies to Indian conditions, distinct from his later National Commission on Farmers role."),
]

TRAPS_11 = [
    "Do not reduce land reform to redistribution or judge success from statute text alone.",
    "Do not merge intermediary abolition, tenancy regulation, ceilings, consolidation and records.",
    "Do not generalise one state's reform experience to all legal and agrarian settings.",
    "Do not describe the Green Revolution as seed-only or uniformly national.",
    "Do not equate higher cropping intensity with sustainable resource use.",
    "Do not quote crop-area shares without the year, geography and official estimate.",
    "Do not call diversification viable without demand, logistics and risk support.",
    "Do not treat every organic or low-chemical system as NPOP-certified organic production.",
    "Do not merge Visvesvaraya's engineering with Swaminathan's crop-science contribution.",
    "Do not infer a PYQ answer key from a routed objective demand.",
]

PANELS_11 = [
    panel(11, "Land-reform instrument map", "classification-tree", ["INTERMEDIARY ABOLITION -> cultivator-state link", "TENANCY -> rent + security + recorded cultivator", "CEILINGS -> permissible holding + surplus land", "CONSOLIDATION / RECORDS -> workable parcels + enforceable rights"]),
    panel(11, "Law-to-outcome rail", "implementation-flow", ["STATE LAW", "-> ACCURATE RECORDS", "-> LOCAL ADMINISTRATION + MOBILISATION", "-> ACTUAL TENURE / REDISTRIBUTION OUTCOME"]),
    panel(11, "State reform comparison", "comparison-matrix", ["OPERATION BARGA -> sharecropper recording", "KERALA -> tenancy abolition + ceiling depth", "J&K 1950 -> early estate restructuring", "COMPARE context; do not copy outcomes mechanically"]),
    panel(11, "Green-Revolution package", "input-wheel", ["HYV SEED + ASSURED WATER", "+ FERTILISER + CREDIT + EXTENSION", "+ PROCUREMENT + PRICE SUPPORT", "PACKAGE EFFECT -> yield + marketed surplus"]),
    panel(11, "Concentration legacy", "cause-effect-board", ["IRRIGATED NORTHWEST", "-> WHEAT / RICE SPECIALISATION", "-> FOODGRAIN SURPLUS", "-> GROUNDWATER + SOIL + REGIONAL STRESS"]),
    panel(11, "Cropping metrics fork", "ratio-map", ["PATTERN -> crop-area distribution", "INTENSITY -> gross cropped / net sown area", "DIVERSIFICATION -> crop / allied shift", "EACH needs stated time + geography"]),
    panel(11, "Diversification decision board", "decision-matrix", ["AGRO-CLIMATE + WATER", "EXPECTED RETURN + VOLATILITY", "CREDIT + INSURANCE + EXTENSION", "STORAGE + PROCESSING + BUYER ACCESS"]),
    panel(11, "Millet transition rail", "transition-flow", ["DRYLAND SUITABILITY", "-> LOWER WATER EXPOSURE", "-> NUTRITION / RESILIENCE VALUE", "-> NEED processing + procurement + demand"]),
    panel(11, "Water-crop lock-in", "feedback-loop", ["PROCUREMENT + CHEAP PUMPING", "-> WATER-INTENSIVE CROP CHOICE", "-> AQUFER / SOIL STRESS", "-> DIVERSIFICATION BECOMES HARDER"]),
    panel(11, "Scientist-engineer distinction", "comparison-matrix", ["VISVESVARAYA -> sluice gates + block irrigation", "SWAMINATHAN -> semi-dwarf crop adaptation", "ENGINEERING -> assured water systems", "CROP SCIENCE -> yield response"]),
    panel(11, "Agrarian trade-offs", "trade-off-board", ["SECURE TENURE -> investment / owner concerns", "CONSOLIDATION -> scale / vulnerable-user safeguards", "HIGH YIELD -> food security / ecological cost", "DIVERSIFICATION -> resilience / market risk"]),
    panel(11, "Agrarian answer spine", "answer-spine", ["DEFINE rights, records and holding structure", "TRACE technology + water + market package", "COMPARE regional outcomes and trade-offs", "CONCLUDE with viable diversification"]),
]

PYQ_SOLUTIONS_11 = [
    common.make_pyq_solution(FACTS_11, "2021", "GS-III", "Explain how land reforms affected the conditions of marginal and small farmers.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 1, 3, 6, 7]),
    common.make_pyq_solution(FACTS_11, "2023", "GS-III", "Discuss land-reform objectives, measures and the role of land ceilings.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 2, 3, 4, 5, 6]),
    common.make_pyq_solution(FACTS_11, "2024", "GS-III", "Elaborate the factors behind successful land reforms in parts of India.", "Verified routed Mains demand; original model solution, not an official answer.", [1, 6, 7, 8, 9]),
]

TOPIC_11 = common.topic(
    11,
    "Land Reforms, Green Revolution and Cropping Systems",
    STEMS[11],
    f"{STEMS[11]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_11,
    TRAPS_11,
    [
        (10, "Distinguish the major instruments of land reform.", [0, 2, 3, 4, 5, 6]),
        (10, "Why did land-reform outcomes differ sharply across states?", [1, 6, 7, 8, 9]),
        (15, "Explain why the Green Revolution was an institutional package rather than a seed revolution.", [10, 11, 12]),
        (15, "Differentiate cropping pattern, cropping intensity and diversification.", [13, 14, 15]),
        (20, "Evaluate the production and ecological legacy of India's Green Revolution.", [10, 11, 12, 16, 17]),
        (20, "Design an agrarian transition from secure rights to sustainable crop diversification.", [0, 1, 6, 15, 16, 17]),
    ],
    [
        "Land-reform instruments and state implementation",
        "Intermediary abolition",
        "Tenancy regulation",
        "Land ceilings",
        "Consolidation and leasing",
        "Land records and Operation Barga",
        "Kerala reform experience",
        "Early Jammu and Kashmir reform",
        "Green-Revolution package",
        "Regional and crop concentration",
        "Technology, institutions and cropping pattern",
        "Cropping intensity",
        "Diversification conditions",
        "Water-intensive path dependence and millets",
        "Visvesvaraya and Swaminathan distinctions",
    ],
    [
        "Sequence rights, records, holding structure, inputs, markets, risk and sustainability.",
        "Compare reform outcomes through political backing, record quality and implementation.",
        "Judge crop transitions through water, demand, logistics, farmer risk and ecological cost.",
    ],
    PANELS_11,
    ["Operation Barga", "Big Landed Estates Abolition Act, 1950", "Green Revolution", "cropping pattern", "cropping intensity", "gross cropped area", "net sown area", "diversification", "automatic sluice", "semi-dwarf"],
    "Audited ledgers route Mains demands on land-reform success, marginal farmers, ceilings, cropping-pattern change, rice-wheat consequences, crop diversification and the distinct contributions of Visvesvaraya and Swaminathan. Objective demands on organic certification, crop seasons, household surveys and water-intensive crops remain answer-key neutral.",
    PYQ_SOLUTIONS_11,
    [
        "https://dolr.gov.in/en/programmes-schemes/dilrmp/ — retrieved 2026-09-03 after redirect; the official page returned only the DILRMP+ title in the live fetcher, so no progress count, coverage percentage or title-status claim was imported.",
    ],
    "The live Department of Land Resources page was only a thin shell in the fetcher. The package therefore uses the repository owners for land-record architecture and makes no current digitisation-progress claim.",
    extra=[
        "basic/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "advanced/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "basic/30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries.md",
        "advanced/30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries.md",
    ],
)


FACTS_12 = [
    ("MSP announcement", "Minimum Support Price is an announced price signal and downside-support instrument; announcement alone is not a universal legal purchase or income guarantee."),
    ("CACP and CCEA", "The Commission for Agricultural Costs and Prices recommends MSPs, while the Cabinet Committee on Economic Affairs takes the Union-level announcement decision; recommendation and decision are distinct stages."),
    ("Cost concepts", "A2 records paid-out expenses, A2+FL adds imputed family labour, and C2 further includes imputed rent on owned land and interest on owned fixed capital; the named base matters to any margin claim."),
    ("Procurement", "Procurement is actual agency purchase of eligible produce under specified crop, grade, season, geography and operational conditions; it must not be inferred from MSP notification."),
    ("Uneven procurement access", "Effective support varies by crop, state, market arrivals, agency presence and quality compliance, so announced coverage and realised procurement are different measures."),
    ("FCI economic cost", "FCI's economic cost is broader than MSP because procurement incidentals, movement, storage, carrying and distribution-related costs enter the public food-management chain."),
    ("Buffer-stock boundary", "Buffer stock is publicly held inventory for operational distribution, strategic security and stabilisation; buffer norms are desired benchmarks, not the actual stock on every date."),
    ("Open-market release", "Open Market Sale Scheme releases address broader market supply and price conditions, while PDS releases serve household entitlements; the channels and purposes must remain distinct."),
    ("NFSA and TPDS", "The National Food Security Act provides a statutory entitlement architecture, while the Targeted Public Distribution System is the principal delivery network; law and delivery operation are not identical."),
    ("NFSA entitlement units", "The owner records Priority Household entitlement per person per month and Antyodaya Anna Yojana entitlement per household per month, so beneficiary category and accounting unit must not be mixed."),
    ("NFSA coverage ceilings", "The owner records NFSA coverage ceilings of up to 75 per cent of rural population and 50 per cent of urban population; ceilings are not identical to actual enrolled beneficiaries in each state."),
    ("Entitlement versus offtake", "A legal allocation or entitlement does not prove household offtake, consumption, nutritional utilisation or error-free delivery; each is a separate outcome measure."),
    ("PMGKAY status", "PMGKAY uses the public-distribution architecture for free-foodgrain support, but continuation, merger and beneficiary-period claims are executive-status questions that require a dated notification."),
    ("ONORC portability", "One Nation One Ration Card enables portability within the NFSA delivery architecture, but portability use depends on beneficiary awareness, identity matching, ePoS connectivity and stock availability."),
    ("Digitisation trade-off", "End-to-end computerisation and ePoS authentication can reduce duplicate records and diversion, while device, connectivity, seeding or biometric failure can exclude genuine beneficiaries."),
    ("Decentralised procurement", "Decentralised procurement gives participating states a larger operational role in purchase, storage and distribution, without eliminating Union financing, stock-transfer or quality questions."),
    ("Price stabilisation", "Public purchase can support farm prices and later stock release can moderate consumer prices, but excessive or unpredictable intervention can crowd private storage and distort crop choice."),
    ("Nutrition dimensions", "Food security includes availability, economic access, utilisation or nutrition and stability; cereal distribution alone cannot substitute for diverse diets, sanitation, health and care."),
    ("Oilseed procurement boundary", "Oilseed procurement is not an everywhere-unlimited operation equivalent to classic paddy-wheat procurement; agency operations, arrivals and scheme conditions determine actual purchase."),
    ("Crop-list and millet caution", "The owner distinguishes notified price-support crops, sugarcane's separate FRP mechanism and millet or niger-seed questions; exact current lists, rates and season claims require the relevant notification."),
]

TRAPS_12 = [
    "Do not equate MSP announcement with procurement or a universal income guarantee.",
    "Do not quote a margin over cost without naming A2, A2+FL or C2.",
    "Do not treat notified crop coverage as actual purchase in every state.",
    "Do not reduce FCI economic cost to MSP alone.",
    "Do not equate buffer norms, actual stocks, operational stock and strategic stock.",
    "Do not merge OMSS market release with PDS entitlement delivery.",
    "Do not equate NFSA entitlement, allocation, offtake and nutritional utilisation.",
    "Do not quote PMGKAY continuation or free-food status without a dated official source.",
    "Do not call authentication reform costless when exclusion failures remain possible.",
    "Do not infer objective PYQ answer letters for MSP, economic cost or niger seed.",
]

PANELS_12 = [
    panel(12, "Price-to-food rail", "policy-flow", ["CACP RECOMMENDATION", "-> CCEA MSP ANNOUNCEMENT", "-> AGENCY PROCUREMENT", "-> STOCK / PDS / MARKET RELEASE"]),
    panel(12, "Cost-concept ladder", "cost-ladder", ["A2 -> paid-out cultivation expense", "A2+FL -> A2 + imputed family labour", "C2 -> A2+FL + owned-land rent + fixed-capital interest", "MARGIN CLAIM -> always name the base"]),
    panel(12, "Announcement-procurement fork", "comparison-matrix", ["MSP -> announced signal", "PROCUREMENT -> actual eligible purchase", "SCOPE -> crop + grade + season + place", "REALISATION -> agency access + arrivals"]),
    panel(12, "FCI cost chain", "accounting-flow", ["PURCHASE PRICE", "+ PROCUREMENT INCIDENTALS", "+ MOVEMENT + STORAGE + CARRYING", "-> ECONOMIC COST; not MSP alone"]),
    panel(12, "Public-stock board", "stock-flow-map", ["BUFFER NORM -> desired benchmark", "ACTUAL STOCK -> dated inventory", "OPERATIONAL -> distribution need", "STRATEGIC -> emergency / stabilisation reserve"]),
    panel(12, "Release-channel fork", "comparison-matrix", ["PDS -> entitled household access", "OMSS -> wider market supply", "PROCUREMENT -> stock inflow", "OFFTAKE / RELEASE -> stock outflow"]),
    panel(12, "NFSA architecture", "institution-map", ["NFSA -> legal entitlement", "TPDS -> delivery network", "PHH -> person-based entitlement unit", "AAY -> household-based entitlement unit"]),
    panel(12, "Delivery-outcome ladder", "outcome-ladder", ["ENTITLEMENT", "-> ALLOCATION", "-> OFFTAKE", "-> HOUSEHOLD RECEIPT -> NUTRITIONAL USE"]),
    panel(12, "Portability and authentication", "trade-off-board", ["ONORC -> portable entitlement", "ePoS -> transaction record", "AADHAAR MATCH -> identity check", "FAILURE RISK -> connectivity / device / seeding"]),
    panel(12, "Farmer-consumer balance", "two-lens-board", ["FARMER -> price assurance + purchase access", "CONSUMER -> affordable access + stability", "STATE -> fiscal + storage cost", "ECOLOGY -> crop / water incentive"]),
    panel(12, "Nutrition diversification", "dimension-board", ["AVAILABILITY", "ACCESS", "UTILISATION / NUTRITION", "STABILITY -> cereals alone are insufficient"]),
    panel(12, "Food-policy answer spine", "answer-spine", ["SEPARATE announcement, purchase and stock", "TRACE inflow, carrying and release", "TEST entitlement against actual delivery", "BALANCE farm, consumer, fiscal and ecology"]),
]

PYQ_SOLUTIONS_12 = [
    common.make_pyq_solution(FACTS_12, "2018", "GS-III", "Discuss MSP as an instrument for protecting farmers from low income.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 1, 2, 3, 4]),
    common.make_pyq_solution(FACTS_12, "2019", "GS-III", "Suggest reforms to make foodgrain distribution more effective.", "Verified routed Mains demand; original model solution, not an official answer.", [8, 11, 13, 14]),
    common.make_pyq_solution(FACTS_12, "2021", "GS-III", "Explain the NFSA architecture and assess its effect on hunger.", "Verified routed Mains demand; original model solution, not an official answer.", [8, 9, 10, 11, 17]),
    common.make_pyq_solution(FACTS_12, "2022", "GS-III", "Discuss PDS challenges and measures for effectiveness and transparency.", "Verified routed Mains demand; original model solution, not an official answer.", [8, 11, 13, 14]),
    common.make_pyq_solution(FACTS_12, "2024", "GS-III", "Elucidate the importance of buffer stocks for price stabilisation and the storage challenge.", "Verified routed Mains demand; original model solution, not an official answer.", [5, 6, 7, 16]),
    common.make_pyq_solution(FACTS_12, "2024", "GS-III", "Explain the role of millets in health and nutritional security.", "Verified routed Mains demand; original model solution, not an official answer.", [17, 19]),
]

TOPIC_12 = common.topic(
    12,
    "MSP, Procurement, Buffer Stocks, PDS and Food Security",
    STEMS[12],
    f"{STEMS[12]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_12,
    TRAPS_12,
    [
        (10, "Distinguish MSP recommendation, announcement and procurement.", [0, 1, 3, 4]),
        (10, "Explain why the cost concept changes an MSP-margin claim.", [2]),
        (15, "Trace FCI economic cost and the public-stock cycle.", [5, 6, 7]),
        (15, "Distinguish NFSA entitlement, TPDS delivery and actual offtake.", [8, 9, 10, 11]),
        (20, "Evaluate India's food-management system from procurement to price stabilisation.", [3, 5, 6, 7, 15, 16]),
        (20, "How can food security balance farmer support, consumer access, nutrition and fiscal discipline?", [0, 4, 8, 11, 17, 19]),
    ],
    [
        "MSP recommendation and announcement",
        "CACP cost concepts",
        "Procurement definition",
        "Uneven procurement access",
        "FCI economic cost",
        "Buffer norms and actual stocks",
        "Open-market release",
        "NFSA and TPDS",
        "Entitlement accounting units",
        "Coverage ceilings",
        "Entitlement, allocation and offtake",
        "PMGKAY status discipline",
        "ONORC portability",
        "Digitisation and decentralised procurement",
        "Price stabilisation, nutrition and crop boundaries",
    ],
    [
        "Map food policy as announcement, purchase, storage, release and household outcome.",
        "Keep stock norms, actual inventory, releases and offtake on separate accounting lines.",
        "Balance farmer, consumer, nutrition, fiscal and ecological objectives explicitly.",
    ],
    PANELS_12,
    ["CACP", "CCEA", "A2+FL", "C2", "procurement", "economic cost", "buffer norm", "operational", "strategic", "NFSA", "TPDS", "offtake", "ONORC", "OMSS"],
    "Audited ledgers route Mains demands on MSP and low farm income, food-distribution reform, NFSA, PDS transparency, buffer-stock stabilisation and millets. Objective demands test the CCEA announcement role, FCI economic cost, rice-price drivers, limits of oilseed procurement and niger seed; no answer letter is inferred.",
    PYQ_SOLUTIONS_12,
    [
        "https://dfpd.gov.in/procurement-policy/en — retrieved 2026-09-03; the official page exposed only the toll-free number 1967 to the live fetcher, so no procurement quantity, season, crop or state claim was imported.",
        "https://dfpd.gov.in/allocation-of-food-grains/en — retrieved 2026-09-03; the official page likewise exposed only the toll-free number, so no allocation, beneficiary or offtake figure was imported.",
        "https://cacp.dacnet.nic.in/ — attempted 2026-09-03; DNS resolution failed in the live fetcher, so no current MSP rate, crop list or cost estimate was imported.",
    ],
    "The live DFPD pages were stubs and the CACP host did not resolve. All rates, quantities, stocks, procurement volumes and continuation periods are therefore deliberately omitted from the authored anchors unless the repository owner states a stable legal distinction.",
    extra=[
        "basic/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
        "advanced/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
    ],
)


FACTS_13 = [
    ("APMC legal layer", "An Agricultural Produce Market Committee operates under the applicable state marketing law for notified produce, market yards, licensing, fees and local practices; state designs differ."),
    ("Market committee function", "APMC regulation supplies a legal and institutional market layer, but competition, assaying, storage, payment and dispute resolution determine the quality of actual trade."),
    ("e-NAM boundary", "e-NAM is an electronic trading and price-discovery layer connecting participating mandis; it does not itself abolish APMC laws or create physical logistics."),
    ("e-NAM launch", "The repository owner records e-NAM as launched in 2016; any current count of mandis, states, lots or participants requires a dated official dashboard."),
    ("Assaying", "Assaying and grading convert heterogeneous produce into credible tradable categories, enabling comparison and distant bidding while imposing quality-measurement requirements."),
    ("Settlement and logistics", "A displayed bid becomes a completed trade only when payment, title, loading, transport, delivery, grievance handling and quality settlement work."),
    ("FPO definition", "An FPO is a producer organisation whose members are farmers; a producer organisation may take more than one legal form, so FPO and cooperative are not universally identical."),
    ("FPO legal forms", "The official SFAC FAQ states that a producer organisation can be a producer company, cooperative society or another legal form that shares benefits among members."),
    ("FPO functions", "The SFAC FAQ lists production, procurement, grading, pooling, marketing, processing, member services, resource conservation, insurance and finance among possible producer-company objects."),
    ("FPO viability", "Aggregation can reduce transaction cost and improve bargaining, but working capital, professional management, member trust, business volume and reliable buyers determine viability."),
    ("Warehouse-receipt finance", "A negotiable warehouse receipt can separate harvest-time cash need from sale timing by supporting credit against stored produce, provided storage, grading and documentation are trusted."),
    ("WDRA layer", "The Warehousing Development and Regulatory Authority anchors the regulated warehousing and negotiable-receipt framework; a receipt is not credible merely because a building is called a warehouse."),
    ("Supply and value chains", "A supply chain traces product, information, payment and risk from inputs to retail, while a value-chain lens additionally asks where value is created and margins or power accumulate."),
    ("Karnataka ReMS", "Karnataka's ReMS model illustrates unified rules, assaying and electronic processes within a reformed mandi architecture rather than digitisation detached from physical institutions."),
    ("Bihar repeal lesson", "Bihar's APMC repeal illustrates that removing a statutory mandi does not automatically create assaying, private competition, storage, roads or enforceable settlement."),
    ("Farm-law episode", "The Farmers' Produce Trade and Commerce Act, 2020 created an outside-APMC channel and was repealed through the Farm Laws Repeal Act, 2021; legal status and federal trust must be dated."),
    ("Contract asymmetry", "Contract farming may reduce buyer uncertainty but can shift quality, rejection, price and enforcement risk onto small farmers when bargaining and dispute-resolution capacity are unequal."),
    ("Intermediary function", "Organised retail or direct procurement can replace the traditional commission-agent layer, but aggregation, grading, finance and logistics functions still have to be performed."),
    ("Direct-procurement examples", "The owner uses ITC e-Choupal, Mother Dairy Safal and organised retail sourcing as named examples, while cautioning that reach, commodity scope and bargaining outcomes vary."),
    ("High-value crop chain", "High-value crop choice depends on water, perishability, cold-chain depth, standards, contract terms and buyer access; production promotion without downstream demand can increase loss."),
]

TRAPS_13 = [
    "Do not treat APMC regulation and e-NAM's electronic layer as the same instrument.",
    "Do not quote current e-NAM participation or trade figures without a dated dashboard.",
    "Do not call screen-based bidding a completed national market without assaying and logistics.",
    "Do not assume APMC repeal automatically creates competitive private markets.",
    "Do not equate every FPO with one legal form.",
    "Do not treat registration or member count as proof of FPO commercial viability.",
    "Do not call an unregulated storage receipt reliable collateral.",
    "Do not say organised retail eliminates the economic functions of intermediation.",
    "Do not treat contract farming as risk-free or bargaining-symmetric.",
    "Do not infer Tea Board or Small Farmer Large Field answer keys from routed PYQs.",
]

PANELS_13 = [
    panel(13, "Agricultural-market layers", "layer-map", ["STATE APMC LAW -> legal venue + rules", "e-NAM -> electronic bid / discovery layer", "ASSAY + WAREHOUSE -> quality + storage", "PAYMENT + LOGISTICS -> completed trade"]),
    panel(13, "Farm-to-market rail", "supply-flow", ["FARM LOT", "-> AGGREGATION + GRADING", "-> BID / CONTRACT", "-> STORAGE + TRANSPORT + SETTLEMENT"]),
    panel(13, "APMC-e-NAM distinction", "comparison-matrix", ["APMC -> state-law institution", "e-NAM -> platform across participating mandis", "LAW REFORM != DIGITAL REFORM", "DIGITAL REFORM != PHYSICAL INFRASTRUCTURE"]),
    panel(13, "Assay-to-settlement chain", "transaction-flow", ["SAMPLE + ASSAY", "-> STANDARD GRADE", "-> COMPARABLE BID", "-> PAYMENT + DELIVERY + GRIEVANCE"]),
    panel(13, "FPO legal-role board", "institution-map", ["FPO -> farmer-member producer organisation", "FORM -> producer company / cooperative / other", "ROLE -> pool inputs, produce and services", "RETURN -> member benefit; not guaranteed profit"]),
    panel(13, "FPO viability wheel", "viability-wheel", ["MEMBER TRUST + GOVERNANCE", "WORKING CAPITAL + MANAGEMENT", "BUSINESS VOLUME + QUALITY", "RELIABLE BUYER + PAYMENT"]),
    panel(13, "Warehouse-finance rail", "collateral-flow", ["ACCREDITED STORAGE", "-> ASSAYED INVENTORY", "-> NEGOTIABLE RECEIPT", "-> CREDIT -> DELAYED SALE CHOICE"]),
    panel(13, "Reform model comparison", "comparison-matrix", ["KARNATAKA ReMS -> integrate rules + assay + platform", "BIHAR REPEAL -> legal exit, infrastructure still needed", "2020 OUTSIDE-APMC LAW -> new channel", "2021 REPEAL -> status + trust matter"]),
    panel(13, "Intermediary replacement", "function-map", ["TRADITIONAL AGENT may be bypassed", "AGGREGATION still required", "GRADING + FINANCE still required", "LOGISTICS performer changes; function remains"]),
    panel(13, "Market-power board", "power-matrix", ["MANY SMALL SELLERS", "FEW LOCAL BUYERS", "TIED CREDIT / INFORMATION GAP", "FPO + COMPETITION can rebalance"]),
    panel(13, "High-value crop gate", "decision-gate", ["CAN IT BE GROWN?", "CAN IT BE STORED / MOVED?", "IS QUALITY MEASURABLE?", "IS THERE A RELIABLE BUYER?"]),
    panel(13, "Marketing answer spine", "answer-spine", ["SEPARATE law, platform and infrastructure", "TRACE product, payment, information and risk", "TEST FPO and buyer bargaining power", "CONCLUDE with integrated reform"]),
]

PYQ_SOLUTIONS_13 = [
    common.make_pyq_solution(FACTS_13, "2018", "GS-III", "Examine whether supermarkets can eliminate intermediaries in agricultural supply chains.", "Verified routed Mains demand; original model solution, not an official answer.", [17, 18, 9, 16]),
    common.make_pyq_solution(FACTS_13, "2020", "GS-III", "Identify constraints in transport and marketing of agricultural produce.", "Verified routed Mains demand; original model solution, not an official answer.", [1, 4, 5, 10, 19]),
    common.make_pyq_solution(FACTS_13, "2022", "GS-III", "Discuss bottlenecks in upstream and downstream agricultural marketing.", "Verified routed Mains demand; original model solution, not an official answer.", [4, 5, 9, 12, 16, 19]),
    common.make_pyq_solution(FACTS_13, "2025", "GS-III", "Elaborate the scope and significance of supply-chain management for agricultural commodities.", "Verified routed Mains demand; original model solution, not an official answer.", [12, 4, 5, 10, 19]),
    common.make_pyq_solution(FACTS_13, "2025", "GS-III", "Explain factors influencing farmers' selection of high-value crops.", "Verified routed Mains demand; original model solution, not an official answer.", [9, 16, 19]),
]

TOPIC_13 = common.topic(
    13,
    "APMC, e-NAM, FPOs and Agricultural Supply Chains",
    STEMS[13],
    f"{STEMS[13]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_13,
    TRAPS_13,
    [
        (10, "Distinguish APMC regulation from e-NAM trading.", [0, 1, 2, 3]),
        (10, "Why are assaying and settlement indispensable to digital trade?", [4, 5]),
        (15, "Explain the legal role and commercial constraints of FPOs.", [6, 7, 8, 9]),
        (15, "How does warehouse-receipt finance reduce distress sale?", [10, 11]),
        (20, "Compare Karnataka integration, Bihar repeal and the 2020-2021 farm-law episode.", [13, 14, 15]),
        (20, "Design an agricultural supply chain that improves price realisation without replacing one monopsony with another.", [9, 12, 16, 17, 18, 19]),
    ],
    [
        "APMC legal and institutional layer",
        "e-NAM electronic layer",
        "e-NAM launch and status discipline",
        "Assaying and grading",
        "Settlement and logistics",
        "FPO definition and legal forms",
        "FPO functions",
        "FPO commercial viability",
        "Warehouse-receipt finance",
        "WDRA framework",
        "Supply-chain and value-chain lenses",
        "Karnataka ReMS",
        "Bihar repeal",
        "Farm-law status and contract asymmetry",
        "Intermediaries, direct procurement and high-value crops",
    ],
    [
        "Map legal rules, electronic discovery, physical infrastructure and settlement separately.",
        "Judge FPOs through member governance, capital, management, volume and buyer linkage.",
        "Trace who performs each intermediary function and who captures value or bears risk.",
    ],
    PANELS_13,
    ["APMC", "e-NAM", "2016", "assaying", "FPO", "producer company", "warehouse receipt", "WDRA", "ReMS", "Farm Laws Repeal Act, 2021", "monopsony", "Small Farmer Large Field"],
    "Audited ledgers route Mains demands on supermarkets, transport and marketing constraints, upstream and downstream bottlenecks, high-value crops and supply-chain management. Objective demands on Tea Board and Small Farmer Large Field are retained as concept routes without inferred answer letters.",
    PYQ_SOLUTIONS_13,
    [
        "https://www.enam.gov.in/web/ — attempted 2026-09-03; the official portal failed at the transport layer, so no current mandi, state, trader, lot or trade-value figure was imported.",
        "https://sfacindia.com/fpofaq.aspx — retrieved 2026-09-03; the official FAQ substantively described PO/FPO definitions, legal forms and producer-company objects. It was used only for those legal-role propositions, not for current FPO counts, targets or participation.",
    ],
    "The SFAC FAQ was substantively retrievable and supports the legal-form and member-service anchors. The e-NAM portal failed to load, so all platform participation and transaction figures are deliberately excluded.",
    extra=[
        "basic/27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers.md",
        "advanced/27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers.md",
        "basic/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "advanced/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
    ],
)


FACTS_14 = [
    ("Potential and utilisation", "Created irrigation potential, utilised potential, reliable field delivery and water-use efficiency are different measures; project capacity does not prove equitable or productive use."),
    ("PMKSY convergence", "The official PMKSY page describes convergence of field-level irrigation investment, assured irrigation expansion, on-farm efficiency, aquifer recharge and decentralised state planning."),
    ("Access and efficiency", "Har Khet Ko Pani addresses irrigation access, while Per Drop More Crop addresses precise application and on-farm efficiency; access and efficiency must not be merged."),
    ("Micro-irrigation rebound", "Drip and sprinkler systems can reduce water applied per unit at plot level, but basin extraction may not fall if irrigated area expands or crop choice remains water-intensive."),
    ("Groundwater common pool", "An individual pumper captures private benefit while cumulative extraction lowers a shared aquifer, making groundwater a common-pool governance problem."),
    ("Water-energy-crop nexus", "Cheap or free pumping power lowers private extraction cost and can reinforce water-intensive crops where procurement and other incentives point in the same direction."),
    ("Watershed method", "Watershed development treats a geo-hydrological catchment from ridge to valley through soil, moisture, recharge, vegetation and participatory maintenance rather than isolated structures."),
    ("Jal Shakti campaign", "The owner records Jal Shakti Abhiyan as a 2019 campaign that later evolved into Catch the Rain; dated coverage and asset claims require the relevant campaign record."),
    ("Atal Bhujal Yojana", "Atal Bhujal Yojana is a groundwater-management programme for water-stressed areas that emphasises community participation, water budgeting and behavioural change."),
    ("KCC liquidity role", "Kisan Credit Card is an institutional working-capital channel for crop and eligible allied needs; it addresses seasonal liquidity rather than compensating a realised insured loss."),
    ("NABARD and co-operatives", "NABARD is a rural and agricultural refinance and development institution, while District Central Cooperative Banks occupy a distinct tier in the cooperative credit architecture."),
    ("Insurance boundary", "Crop insurance pools specified production or weather risk under scheme terms; it is not a universal guarantee of price, income, debt repayment or every individual loss."),
    ("PMFBY scope", "PMFBY operates through notified crops, areas, seasons and perils under the applicable scheme rules; current premium, enrolment and state-participation claims require the governing notification."),
    ("Enrolment and claims", "Insurance enrolment or premium collection does not prove claim admissibility, assessment, settlement amount or timeliness; these are separate implementation outcomes."),
    ("Basis risk", "Area-yield assessment reduces individual verification cost but can create basis risk when the reference-area loss differs from a particular farmer's field loss."),
    ("Rainfed Area Development", "Rainfed Area Development under the National Mission for Sustainable Agriculture promotes integrated farming systems and diversification suited to rainfed risk."),
    ("Conservation agriculture", "Conservation agriculture combines minimum soil disturbance, residue cover and crop rotation; zero tillage is one practice rather than the whole system."),
    ("Precision input tools", "Fertigation applies nutrients through irrigation water, while a tensiometer measures soil-water tension for irrigation scheduling; neither is itself a crop-insurance instrument."),
    ("Sikkim organic transition", "Sikkim's organic transition was phased through policy, input withdrawal, mission support and certification; its scale and hill ecology limit mechanical replication."),
    ("Tenant inclusion", "Title-linked credit, insurance and subsidy administration can exclude tenants and sharecroppers even when they are the actual cultivators, so records and eligibility design matter."),
]

TRAPS_14 = [
    "Do not equate irrigation potential with utilisation, reliability or water productivity.",
    "Do not merge irrigation access with application efficiency.",
    "Do not assume micro-irrigation automatically reduces basin-level extraction.",
    "Do not treat free power as only a transfer without crop and groundwater effects.",
    "Do not reduce watershed development to a pond or check dam.",
    "Do not equate KCC liquidity with crop-insurance compensation.",
    "Do not equate insurance enrolment with claim settlement.",
    "Do not quote PMFBY premiums, coverage or state participation without scheme vintage.",
    "Do not treat Sikkim's organic transition as universally replicable.",
    "Do not infer provisional 2026 objective answer letters.",
]

PANELS_14 = [
    panel(14, "Irrigation accounting ladder", "measurement-ladder", ["CREATED POTENTIAL", "-> UTILISED POTENTIAL", "-> RELIABLE FIELD DELIVERY", "-> WATER PRODUCTIVITY / FARM OUTCOME"]),
    panel(14, "PMKSY distinction board", "comparison-matrix", ["HAR KHET KO PANI -> access", "PER DROP MORE CROP -> application efficiency", "STATE PLAN -> decentralised project choice", "CONVERGENCE -> source to field"]),
    panel(14, "Micro-irrigation rebound", "feedback-loop", ["LESS WATER PER UNIT", "-> LOWER PRIVATE COST / MORE AREA", "-> WATER-INTENSIVE CROP MAY PERSIST", "-> BASIN SAVING NOT AUTOMATIC"]),
    panel(14, "Water-energy-crop nexus", "causal-triangle", ["CHEAP POWER", "PROCUREMENT INCENTIVE", "GROUNDWATER ACCESS", "JOINT EFFECT -> extraction + crop lock-in"]),
    panel(14, "Watershed rail", "ridge-valley-flow", ["RIDGE -> vegetation + contour treatment", "MID-SLOPE -> bunds + moisture retention", "DRAINAGE -> check / recharge structures", "VALLEY -> productive use + maintenance"]),
    panel(14, "Groundwater governance", "common-pool-map", ["PRIVATE PUMP", "SHARED AQUIFER", "LOCAL WATER BUDGET", "CROP + EXTRACTION RULES"]),
    panel(14, "Credit-insurance fork", "comparison-matrix", ["KCC -> pre-harvest liquidity", "INSURANCE -> covered-loss transfer", "NABARD / BANK -> finance architecture", "CLAIM -> trigger + assessment + settlement"]),
    panel(14, "Insurance outcome chain", "process-flow", ["ENROLMENT", "-> PREMIUM + NOTIFIED SCOPE", "-> LOSS ASSESSMENT", "-> ADMISSIBLE CLAIM -> SETTLEMENT"]),
    panel(14, "Basis-risk board", "comparison-matrix", ["AREA YIELD -> lower verification cost", "FARM LOSS -> may diverge", "WEATHER INDEX -> proxy trigger", "DATA + TIMELINESS decide trust"]),
    panel(14, "Sustainable-practice map", "practice-tree", ["CONSERVATION -> minimum disturbance + residue + rotation", "PRECISION -> drip + fertigation + tensiometer", "DIVERSIFICATION -> integrated farming", "ORGANIC -> certification and transition context"]),
    panel(14, "Tenant-access gate", "eligibility-flow", ["ACTUAL CULTIVATOR", "-> RECORD / LEASE EVIDENCE", "-> CREDIT / INSURANCE ELIGIBILITY", "-> COVERAGE OR EXCLUSION"]),
    panel(14, "Resilience answer spine", "answer-spine", ["SEPARATE potential, use and efficiency", "LINK water, energy, crop and credit", "TRACE enrolment to claim settlement", "CONCLUDE with aquifer + tenant governance"]),
]

PYQ_SOLUTIONS_14 = [
    common.make_pyq_solution(FACTS_14, "2018", "GS-III", "Discuss the ecological and economic benefits and limits of Sikkim's organic transition.", "Verified routed Mains demand; original model solution, not an official answer.", [18]),
    common.make_pyq_solution(FACTS_14, "2019", "GS-III", "Elaborate the impact of watershed development on water-stressed agriculture.", "Verified routed Mains demand; original model solution, not an official answer.", [6, 4, 15]),
    common.make_pyq_solution(FACTS_14, "2020", "GS-III", "Suggest measures for water storage and irrigation under groundwater depletion.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 2, 3, 4, 6, 8]),
    common.make_pyq_solution(FACTS_14, "2021", "GS-III", "Assess the role and limits of micro-irrigation in addressing India's water crisis.", "Verified routed Mains demand; original model solution, not an official answer.", [2, 3, 4, 5]),
    common.make_pyq_solution(FACTS_14, "2024", "GS-III", "State the challenges of India's irrigation system and government measures.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 1, 2, 3, 6]),
    common.make_pyq_solution(FACTS_14, "2025", "GS-III", "Examine groundwater depletion and evaluate government responses.", "Verified routed Mains demand; original model solution, not an official answer.", [3, 4, 5, 8, 15]),
]

TOPIC_14 = common.topic(
    14,
    "Irrigation, Inputs, Credit, Insurance and Sustainable Agriculture",
    STEMS[14],
    f"{STEMS[14]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_14,
    TRAPS_14,
    [
        (10, "Distinguish irrigation potential, utilisation and water-use efficiency.", [0]),
        (10, "Separate irrigation access from precision application under PMKSY.", [1, 2]),
        (15, "Explain the groundwater-energy-crop nexus and micro-irrigation rebound.", [3, 4, 5]),
        (15, "How does watershed development differ from isolated water structures?", [6, 7, 8]),
        (20, "Evaluate farm credit and crop insurance through liquidity, eligibility, basis risk and claims.", [9, 10, 11, 12, 13, 14, 19]),
        (20, "Design a sustainable agriculture strategy for rainfed and groundwater-stressed India.", [3, 4, 6, 8, 15, 16, 17, 18]),
    ],
    [
        "Irrigation potential and utilisation",
        "PMKSY convergence",
        "Access versus efficiency",
        "Micro-irrigation rebound",
        "Groundwater common-pool problem",
        "Water-energy-crop nexus",
        "Watershed development",
        "Jal Shakti and Atal Bhujal",
        "KCC liquidity",
        "NABARD and cooperative credit",
        "Crop-insurance boundary",
        "PMFBY notified scope",
        "Enrolment, claims and basis risk",
        "Rainfed development and conservation agriculture",
        "Precision tools, organic transition and tenant inclusion",
    ],
    [
        "Separate infrastructure capacity, delivered water, farm use and basin outcomes.",
        "Distinguish liquidity support, risk pooling, enrolment, assessment and settlement.",
        "Integrate aquifer governance, crop incentives, tenant eligibility and resilient agronomy.",
    ],
    PANELS_14,
    ["irrigation potential", "Har Khet Ko Pani", "Per Drop More Crop", "common-pool", "ridge-to-valley", "Kisan Credit Card", "NABARD", "PMFBY", "basis risk", "Rainfed Area Development", "fertigation", "tensiometer"],
    "Audited ledgers route Mains demands on organic transition, integrated farming, watershed development, Jal Shakti Abhiyan, water storage, micro-irrigation, irrigation-system challenges and groundwater depletion. Objective demands cover conservation agriculture, DCCBs, KCC, biochar, zero tillage, fertigation, crop-protection chemicals and the provisionally keyed 2026 Rainfed Area Development question; no answer letter is inferred.",
    PYQ_SOLUTIONS_14,
    [
        "https://www.pmksy.gov.in/AboutPMKSY.aspx — retrieved 2026-09-03; the official page substantively described convergence, assured irrigation, on-farm efficiency, aquifer recharge, precision irrigation and decentralised state planning. No dashboard quantity was imported.",
        "https://pmfby.gov.in/ — retrieved 2026-09-03; the official homepage returned only the PMFBY title in the live fetcher, so no premium rate, enrolment, insured area, claim or state-participation figure was imported.",
    ],
    "The PMKSY objectives were substantively retrievable and support the convergence and efficiency anchors. The PMFBY portal was a title-only shell, so insurance amounts, enrolment and claim-performance figures are excluded.",
    extra=[
        "basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md",
        "advanced/25_Climate-Economics-Green-Finance-and-Circular-Economy.md",
        "basic/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
        "advanced/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
        "basic/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "advanced/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
    ],
)


FACTS_15 = [
    ("Food processing", "Food processing transforms, preserves or packages food to change shelf life, form, safety, convenience or market value; the degree of processing must be stated where relevant."),
    ("Cold chain", "A cold chain is temperature-controlled handling and movement across linked stages from first-mile cooling to consumption; a standalone warehouse is not a complete chain."),
    ("Value addition", "Value addition is an increase in utility or market value through grading, processing, packaging, branding or services; higher final price does not prove the farmer captured the gain."),
    ("Post-harvest management", "Post-harvest management includes cleaning, sorting, grading, drying, storage, transport, processing and loss control after harvest."),
    ("Traceability", "Traceability tracks origin, processing and movement through the chain and supports recall, quality assurance and export compliance; it is not the same as food-safety regulation itself."),
    ("PM Kisan SAMPADA", "Pradhan Mantri Kisan SAMPADA Yojana is an umbrella for food-processing and value-chain infrastructure; component status, eligibility and outlay require the applicable dated guideline."),
    ("Integrated cold-chain nodes", "An effective cold chain can require pack houses, pre-cooling, controlled storage, reefer transport, processing interfaces and reliable power; capacity at one node cannot substitute for continuity."),
    ("Operation Greens boundary", "Operation Greens links price stabilisation and value-chain support for specified perishables, but commodity coverage and assistance windows are status-sensitive and not universal."),
    ("PLISFPI boundary", "The Production Linked Incentive Scheme for Food Processing Industries links support to eligible incremental performance; approval, investment, incremental sales, disbursal and realised exports are different stages."),
    ("Mega Food Park model", "The Mega Food Park model links collection and primary-processing centres with common central infrastructure, but sanction or constructed capacity does not prove occupancy, throughput or commercial viability."),
    ("Capacity utilisation", "Processing viability depends on throughput, seasonality, energy, logistics, working capital and capacity utilisation; installed capacity is a stock while actual processed output is a flow."),
    ("FSSAI and APEDA", "FSSAI regulates domestic food-safety standards within its mandate, while APEDA supports agricultural and processed-food export development and market access; their functions are not interchangeable."),
    ("Standards and SPS", "Testing, sanitary and phytosanitary requirements, quality certification and traceability can unlock premium markets while imposing fixed compliance costs on small processors."),
    ("Backward and forward links", "Backward linkage connects processors with farm aggregation and quality supply, while forward linkage connects processed output with retail, institutional buyers and exports."),
    ("Contract and margin distribution", "Contracts allocate quantity, quality, price, rejection and force-majeure risk; competition and farmer aggregation determine whether additional value reaches primary producers."),
    ("Employment nodes", "Food processing creates work in aggregation, grading, cold logistics, factories, packaging, testing, maintenance and retail, but job quality, formality and seasonality must be assessed separately."),
    ("Small-processor constraints", "Micro and small processors can face working-capital, technology, testing, formalisation, power and market-access barriers even when local demand exists."),
    ("By-product use", "Processing by-products can support feed, compost, energy and other circular-bioeconomy uses, but commercial value depends on segregation, safety, technology and markets."),
    ("Capacity versus value realised", "Cold-chain or plant capacity measures an installed stock, actual throughput measures use, and realised value addition depends on output quality, price, cost and distribution of margins."),
    ("PYQ routing boundary", "Verified PYQs test sector scope, policy, farmer income, employment and the cold-chain distinction; the routed palm-oil objective demand remains answer-key neutral and cross-owned with crop missions."),
]

TRAPS_15 = [
    "Do not call a warehouse or cold store a complete cold chain.",
    "Do not equate installed capacity, operational capacity, throughput and value addition.",
    "Do not treat scheme sanction as construction, operation, sales or disbursal.",
    "Do not quote cold-chain capacity, scheme outlay or project counts without a dated source.",
    "Do not merge FSSAI regulation with APEDA export-development functions.",
    "Do not assume higher retail value reaches farmers automatically.",
    "Do not treat all processing employment as formal, permanent or factory-based.",
    "Do not call standards pure market access without recognising compliance cost.",
    "Do not treat Operation Greens commodity scope as timeless or universal.",
    "Do not infer the palm-oil objective answer key from routing metadata.",
]

PANELS_15 = [
    panel(15, "Farm-to-value rail", "value-flow", ["FARM OUTPUT", "-> AGGREGATION + GRADING", "-> COLD / AMBIENT LOGISTICS + PROCESSING", "-> PACKAGING + MARKET -> DISTRIBUTED VALUE"]),
    panel(15, "Cold-chain continuity", "process-chain", ["PACK HOUSE", "-> PRE-COOLING", "-> COLD STORAGE", "-> REEFER -> PROCESSOR / RETAIL"]),
    panel(15, "Capacity accounting fork", "stock-flow-map", ["INSTALLED CAPACITY -> stock", "OPERATIONAL CAPACITY -> available stock", "THROUGHPUT -> period flow", "VALUE ADDED -> output value minus inputs"]),
    panel(15, "PMKSY umbrella", "scheme-map", ["COMMON / CLUSTER INFRASTRUCTURE", "COLD CHAIN + VALUE ADDITION", "PROCESSING + QUALITY SUPPORT", "STATUS -> guideline and component vintage"]),
    panel(15, "Scheme-stage ladder", "implementation-ladder", ["APPROVAL / SANCTION", "-> INVESTMENT / CONSTRUCTION", "-> OPERATION + CAPACITY USE", "-> SALES / DISBURSAL / OUTCOME"]),
    panel(15, "Operation Greens boundary", "scope-board", ["PERISHABLE PRICE STRESS", "SPECIFIED COMMODITY / WINDOW", "STORAGE + PROCESSING LINK", "NOT universal farm-price insurance"]),
    panel(15, "Food Park cluster", "cluster-map", ["COLLECTION CENTRE", "-> PRIMARY PROCESSING", "-> COMMON CENTRAL FACILITIES", "-> PROCESSOR + MARKET LINK"]),
    panel(15, "Regulatory-export fork", "comparison-matrix", ["FSSAI -> food-safety regulation", "APEDA -> export development / market access", "SPS + TESTING -> compliance gate", "TRACEABILITY -> chain evidence"]),
    panel(15, "Value-capture board", "power-matrix", ["FARMER / FPO -> raw material + aggregation", "PROCESSOR -> transformation + quality risk", "LOGISTICS / RETAIL -> access + shelf", "CONTRACT + COMPETITION -> margin split"]),
    panel(15, "Employment chain", "jobs-map", ["FARM-GATE SORTING", "COLD LOGISTICS + MAINTENANCE", "PROCESSING + PACKAGING + TESTING", "RETAIL / EXPORT; test formality + seasonality"]),
    panel(15, "Small-processor constraint wheel", "constraint-wheel", ["WORKING CAPITAL", "POWER + TECHNOLOGY", "TESTING + FORMALISATION", "MARKET + BRAND + DISTRIBUTION"]),
    panel(15, "Processing answer spine", "answer-spine", ["DEFINE chain and accounting units", "MAP missing node and scheme stage", "TEST standards, jobs and bargaining", "CONCLUDE with throughput + fair value capture"]),
]

PYQ_SOLUTIONS_15 = [
    common.make_pyq_solution(FACTS_15, "2019", "GS-III", "Elaborate government policy for addressing food-processing-sector challenges.", "Verified routed Mains demand; original model solution, not an official answer.", [5, 6, 7, 8, 9, 16]),
    common.make_pyq_solution(FACTS_15, "2020", "GS-III", "Explain food-processing opportunities and challenges and their relation to farmer income.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 2, 6, 10, 13, 14]),
    common.make_pyq_solution(FACTS_15, "2022", "GS-III", "Elaborate the scope and significance of India's food-processing industry.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 1, 2, 3, 11, 15]),
    common.make_pyq_solution(FACTS_15, "2025", "GS-III", "Examine the scope of food-processing industries and measures for employment generation.", "Verified routed Mains demand; original model solution, not an official answer.", [0, 6, 10, 15, 16, 18]),
]

TOPIC_15 = common.topic(
    15,
    "Food Processing, Cold Chains and Value Addition",
    STEMS[15],
    f"{STEMS[15]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_15,
    TRAPS_15,
    [
        (10, "Distinguish food processing, post-harvest management, cold chain and value addition.", [0, 1, 2, 3]),
        (10, "Explain the role of traceability in safe and export-ready food chains.", [4, 11, 12]),
        (15, "Evaluate PM Kisan SAMPADA, Operation Greens and PLISFPI as distinct instruments.", [5, 7, 8]),
        (15, "Why does a Mega Food Park or cold store not prove a functioning value chain?", [6, 9, 10, 18]),
        (20, "Assess whether food processing can raise farmer income and rural employment.", [2, 13, 14, 15, 16]),
        (20, "Design a competitive, safe and resource-efficient food-processing chain for India.", [4, 6, 11, 12, 14, 17, 18]),
    ],
    [
        "Food-processing definition",
        "Cold-chain definition",
        "Value addition",
        "Post-harvest management",
        "Traceability",
        "PM Kisan SAMPADA",
        "Integrated cold-chain nodes",
        "Operation Greens",
        "PLISFPI",
        "Mega Food Park model",
        "Capacity utilisation and stock-flow distinction",
        "FSSAI and APEDA",
        "Standards and SPS",
        "Backward and forward linkages",
        "Contracts, employment, small processors and realised value",
    ],
    [
        "Map every chain node from farm aggregation to final market and identify the missing link.",
        "Separate sanction, installed capacity, operational throughput, sales, disbursal and value added.",
        "Evaluate standards, employment and farmer income through competition and contract design.",
    ],
    PANELS_15,
    ["food processing", "cold chain", "pre-cooling", "reefer", "traceability", "PM Kisan SAMPADA", "Operation Greens", "PLISFPI", "Mega Food Park", "capacity utilisation", "FSSAI", "APEDA", "SPS"],
    "Audited ledgers route Mains demands on government policy, food-processing challenges and opportunities, farmer income, sector scope and employment generation. The objective palm-oil demand is cross-routed and answer-key neutral; no origin, use or biodiesel option is inferred.",
    PYQ_SOLUTIONS_15,
    [
        "https://www.mofpi.gov.in/Schemes/pradhan-mantri-kisan-sampada-yojana — retrieved 2026-09-03; the official page returned only the scheme title, so no component outlay, project count, eligibility or continuation claim was imported.",
        "https://www.mofpi.gov.in/en/Schemes/cold-chain — retrieved 2026-09-03; the official page returned only its title and breadcrumb, so no cold-storage capacity, project status, grant or beneficiary figure was imported.",
    ],
    "The live MoFPI pages were thin shells in the fetcher. Scheme identities are retained, but all capacity, project, outlay, sanction, disbursal and employment quantities remain omitted unless tied to a dated repository-owner source.",
    extra=[
        "basic/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md",
        "advanced/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md",
        "basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
        "advanced/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
        "basic/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "advanced/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "basic/30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries.md",
        "advanced/30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries.md",
    ],
)


TOPICS = {
    "economy-11": TOPIC_11,
    "economy-12": TOPIC_12,
    "economy-13": TOPIC_13,
    "economy-14": TOPIC_14,
    "economy-15": TOPIC_15,
}
