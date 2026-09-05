"""Authored Economy learner-v2 data for Topics 28-31."""

from __future__ import annotations

import generate_economy_common as common


STEMS = {
    28: "28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules",
    29: "29_Agricultural-Technology-Missions-and-Mission-Mode-Policy",
    30: "30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries",
    31: "31_Energy-Infrastructure-Economics-Power-Fuels-and-Energy-Security",
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


FACTS_28 = [
    ("Delivery and legal classification", "Direct and indirect describe delivery channels in Indian policy, while WTO treatment depends on the measure's legal criteria, production linkage and applicable exemption; a cash transfer is not automatically Green Box."),
    ("Explicit and implicit support", "Explicit support appears as a budget payment or revenue concession, whereas implicit support depends on a below-cost or opportunity-cost benchmark; neither label identifies the final economic beneficiary."),
    ("Income support boundary", "Income support supplements an eligible farm household's liquidity without requiring purchase of one input, but land-record eligibility can exclude tenants, sharecroppers and undocumented cultivators."),
    ("Fertiliser DBT boundary", "Under fertiliser DBT, subsidy is released to fertiliser companies on recorded retail sales through Point-of-Sale systems; it is not a PM-KISAN-style cash deposit to each fertiliser buyer."),
    ("NBS and urea distinction", "Nutrient Based Subsidy covers notified phosphatic and potassic fertiliser grades through per-nutrient support, while urea remains outside that regime under a separate pricing and subsidy framework."),
    ("Power-water-crop nexus", "Concessional or unmetered farm power lowers private pumping cost but can reinforce groundwater extraction, water-intensive cropping and DISCOM or state fiscal stress when resource governance is weak."),
    ("Irrigation incidence", "Public irrigation and low water charges can raise productivity, yet benefit depends on command location, head-tail distribution, maintenance and water access; plot efficiency does not prove basin-level water saving."),
    ("Credit and insurance support", "Interest and premium support can ease liquidity and transfer specified risk, but cheap credit does not make an unviable crop viable and insurance value collapses when basis risk, yield data, settlement or appeal is weak."),
    ("MSP, procurement and expenditure", "MSP announcement, effective procurement, budget expenditure and WTO market-price-support measurement are different objects with crop, grade, geography, quantity and methodology boundaries."),
    ("Economic incidence", "The budget recipient, statutory beneficiary and final economic beneficiary can differ after prices, rents, input demand, supplier margins and output supply adjust."),
    ("Producer and consumer support", "Farm input or price support primarily targets producers, while PDS food subsidy targets eligible consumers; procurement links the systems but does not make consumer food subsidy a farm-input subsidy."),
    ("Public goods and capital grants", "Research, extension, pest control, roads, markets and eligible infrastructure can correct public-good or coordination failures, while capital grants require demand, maintenance and additionality checks."),
    ("WTO domestic-support pillars", "The Agreement on Agriculture separates market access, domestic support and export competition; farm-subsidy box analysis belongs primarily to domestic support even when border and export effects interact."),
    ("Amber and de minimis", "Amber Box covers non-exempt support considered production- or trade-distorting, while product-specific and non-product-specific de minimis tests are separate and the general developing-country ceiling is 10 percent."),
    ("Green and Blue Boxes", "Green Box measures must be publicly funded, avoid producer price support and meet general plus measure-specific minimal-distortion criteria; Blue Box covers qualifying direct payments under production-limiting conditions."),
    ("Article 6.2 flexibility", "Article 6.2 permits specified developing-country development measures, including generally available agricultural investment subsidies and input subsidies generally available to low-income or resource-poor producers."),
    ("AMS measurement boundary", "Aggregate Measurement of Support measures non-exempt domestic support; administered market-price support uses a price gap against a fixed external reference price multiplied by eligible production, not actual procurement expenditure."),
    ("Public stockholding status", "The 2013 Bali public-stockholding decision provides interim, conditional due-restraint protection for qualifying existing food-security programmes involving traditional staple crops; it is not a permanent settlement or blanket exemption."),
    ("Reform sequencing", "Subsidy reform should identify the objective and incidence, build alternatives first, protect small and actual cultivators, coordinate input and output incentives, phase change predictably and reinvest in public goods."),
    ("WTO transparency boundary", "Notification, methodology, eligible production and stock-disposal questions are legal and transparency issues; a member notification is not an adjudicated ruling and a peace-clause invocation does not settle the underlying dispute."),
]

TRAPS_28 = [
    "Do not equate direct delivery, DBT and WTO Green Box treatment.",
    "Do not infer the final beneficiary from the entity receiving the budget payment.",
    "Do not merge PM-KISAN-style income support with fertiliser DBT.",
    "Do not place urea inside the Nutrient Based Subsidy regime.",
    "Do not treat MSP announcement, procurement, fiscal cost and WTO support as one number.",
    "Do not merge product-specific and non-product-specific de minimis tests.",
    "Do not call all public investment Green Box without applying the policy criteria.",
    "Do not describe the Bali peace clause as a permanent or unconditional exemption.",
    "Do not convert a notification or counter-notification into a WTO adjudication.",
    "Do not present abrupt withdrawal as the only meaning of subsidy reform.",
]

PANELS_28 = [
    panel(28, "Farm-support transmission rail", "cause-effect-rail", ["OBJECTIVE", "-> DELIVERY CHANNEL", "-> ECONOMIC INCIDENCE", "-> BEHAVIOUR + OUTCOME + WTO TEST"]),
    panel(28, "Delivery-classification matrix", "comparison-matrix", ["DIRECT / INDIRECT -> delivery", "EXPLICIT / IMPLICIT -> fiscal visibility", "GREEN / AMBER / BLUE -> WTO criteria", "LABEL != legal result"]),
    panel(28, "Income-support boundary", "eligibility-map", ["ELIGIBLE RECORD", "-> CASH TRANSFER", "-> HOUSEHOLD LIQUIDITY", "TENANT + SHARECROPPER exclusion risk"]),
    panel(28, "Fertiliser support chain", "principal-agent-map", ["GOVERNMENT", "-> COMPANY CLAIM AFTER PoS SALE", "-> LOWER FARMER PRICE", "DBT != buyer cash transfer"]),
    panel(28, "Nutrient-pricing split", "classification-tree", ["NBS -> notified P + K grades", "UREA -> separate regime", "RELATIVE PRICE -> nutrient choice", "AFFORDABILITY != balanced use"]),
    panel(28, "Water-energy-crop loop", "feedback-loop", ["CHEAP POWER -> PUMPING", "PUMPING -> WATER-INTENSIVE CROP", "GROUNDWATER FALL -> MORE ENERGY", "REFORM needs crop + aquifer safeguards"]),
    panel(28, "Risk-support audit", "risk-board", ["CREDIT -> liquidity", "INSURANCE -> specified risk transfer", "BASIS RISK + DELAY", "SUBSIDY != viable farm system"]),
    panel(28, "Price-support distinctions", "four-way-map", ["MSP -> announcement", "PROCUREMENT -> actual operation", "BUDGET -> fiscal expenditure", "AMS -> WTO methodology"]),
    panel(28, "WTO box map", "classification-tree", ["AMBER -> non-exempt distortion", "GREEN -> criteria-based minimal distortion", "BLUE -> production-limiting payment", "ARTICLE 6.2 -> development flexibility"]),
    panel(28, "De minimis and AMS", "formula-board", ["PRODUCT-SPECIFIC -> separate test", "NON-PRODUCT-SPECIFIC -> separate test", "DEVELOPING COUNTRY -> general 10%", "PRICE GAP x ELIGIBLE PRODUCTION"]),
    panel(28, "Public-stockholding status", "status-ladder", ["FOOD-SECURITY PROGRAMME", "-> BALI 2013 INTERIM SHIELD", "-> TRANSPARENCY + CONDITIONS", "PEACE CLAUSE != permanent solution"]),
    panel(28, "Farm-subsidy answer spine", "answer-spine", ["CLASSIFY delivery + objective", "TRACE incidence + distortion", "APPLY WTO category + status", "REFORM with transition protection"]),
]

PYQS_28 = [
    common.make_pyq_solution(FACTS_28, "2023", "GS-III", "Direct and indirect farm subsidies in India and issues raised at the WTO.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger; no official model answer is claimed.", [0, 3, 5, 8, 13, 14, 15, 17, 19]),
]

TOPIC_28 = common.topic(
    28,
    "Direct and Indirect Farm Subsidies and WTO Rules",
    STEMS[28],
    f"{STEMS[28]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_28,
    TRAPS_28,
    [
        (10, "Distinguish direct, indirect, explicit and implicit farm support.", [0, 1, 2]),
        (10, "Explain why fertiliser DBT is not a cash transfer to the farmer.", [3, 4]),
        (15, "Analyse the economic incidence and ecological effects of farm input subsidies.", [5, 6, 7, 9]),
        (15, "Distinguish WTO Amber, Green, Blue and Article 6.2 treatment.", [12, 13, 14, 15]),
        (20, "Discuss India's public-stockholding dispute and the legal status of the peace clause.", [8, 16, 17, 19]),
        (20, "Design a sequenced reform of Indian farm support that protects livelihoods and food security.", [2, 5, 7, 9, 10, 11, 18]),
    ],
    [
        "Farm-support taxonomy and legal boundary",
        "Explicit, implicit and benchmark choice",
        "Income support and actual-cultivator inclusion",
        "Fertiliser DBT and payment channel",
        "NBS, urea and nutrient incentives",
        "Power and groundwater nexus",
        "Irrigation distribution and basin effects",
        "Credit, insurance and risk transfer",
        "MSP, procurement and measurement",
        "Economic incidence across markets",
        "Producer versus consumer support",
        "Public goods and investment support",
        "Agreement on Agriculture architecture",
        "Amber, de minimis, Green and Blue",
        "AMS, public stockholding and reform",
    ],
    [
        "Classify the objective, delivery channel and WTO category before judging a subsidy.",
        "Trace who finally benefits and who bears fiscal, distributional and ecological costs.",
        "Reform quantity-linked support only after building protected income and public-good alternatives.",
    ],
    PANELS_28,
    ["fertiliser DBT", "Nutrient Based Subsidy", "economic incidence", "Amber Box", "de minimis", "Green Box", "Blue Box", "Article 6.2", "Aggregate Measurement of Support", "fixed external reference price", "public stockholding", "Bali"],
    "Audited ledgers route the 2023 GS-III farm-subsidy/WTO demand and the 2020 objective fertiliser concept. The Basic/practice firewall preserves fertiliser pricing, ammonia and sulphur distinctions without inferring an unavailable objective answer key.",
    PYQS_28,
    [
        "https://www.wto.org/english/tratop_e/agric_e/agboxes_e.htm — substantive WTO page fetched 2026-09-03; confirms Amber, Blue, Green, de minimis and Article 6.2 criteria without establishing any India-specific notification result.",
        "https://www.wto.org/english/tratop_e/agric_e/ag_intro03_domestic_e.htm — substantive WTO domestic-support page fetched 2026-09-03; confirms the conceptual framework, government-service criteria and separate de minimis tests.",
        "https://www.fert.gov.in/en/department/our-wings/direct-benefit-transfer-dbt — substantive Department of Fertilizers page fetched 2026-09-03; confirms company reimbursement after PoS-recorded sales. Dashboard counts were not imported.",
    ],
    "The WTO and fertiliser pages substantively confirmed legal categories and the fertiliser payment channel. No subsidy outlay, beneficiary count, notification percentage, peace-clause invocation, product support value or current dispute outcome was imported.",
    extra=[
        "basic/12_MSP-Procurement-Buffer-Stocks-PDS-and-Food-Security.md",
        "advanced/12_MSP-Procurement-Buffer-Stocks-PDS-and-Food-Security.md",
        "basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "advanced/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
        "advanced/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
    ],
)


FACTS_29 = [
    ("Mission-mode definition", "An agricultural technology mission is a coordinated intervention organised around a defined production, quality, sustainability or value-chain problem, with outcome objectives, institutions, monitoring and feedback."),
    ("Mission versus scheme label", "A programme is mission-mode only when its design links the problem, technology, complementary delivery and measurable outcome; the word Mission in its title does not establish those properties."),
    ("Research-to-market chain", "Durable mission performance requires research, adaptive trials, quality material, multiplication or manufacturing, demonstration, extension, finance, complementary inputs, repeated adoption and market feedback."),
    ("Technology breadth", "Agricultural technology includes biological, agronomic, mechanical, water-resource, digital, post-harvest and institutional innovations; it is not confined to machinery or frontier gadgets."),
    ("Adoption threshold", "A farmer adopts when expected additional return exceeds purchase, finance, learning, transition, failure and market risk relative to the existing practice; availability or demonstration alone is not adoption."),
    ("Technology Mission on Oilseeds", "The Technology Mission on Oilseeds began in 1986 and its successor architecture changed through later umbrellas; historical names, current schemes and measured results must retain their date."),
    ("Oilseed and oil-palm missions", "NMEO-OS and NMEO-OP address distinct oilseed and perennial oil-palm systems through value-chain measures; approval, outlay, operational reach, area, production and import outcome are separate facts."),
    ("Horticulture mission evolution", "The National Horticulture Mission began in 2005-06 and later became a component of the wider MIDH architecture; NHM and MIDH are not interchangeable names for every year."),
    ("Food-security mission evolution", "The National Food Security Mission began in 2007-08 and later acquired a nutrition emphasis and renamed architecture; vintage must be stated before listing components."),
    ("Cotton mission boundary", "The historical Technology Mission on Cotton used four linked mini-missions across research, transfer, market infrastructure and ginning or pressing; later cotton-mission architecture must not be merged with it."),
    ("Extension-system functions", "The classic NMAET architecture separated agricultural extension, seeds and planting material, mechanisation, and plant protection or quarantine; these diffusion functions remain distinct even when umbrellas change."),
    ("Sustainability missions", "NMSA links agricultural resilience and resource conservation with the climate-policy framework, while natural-farming or rainfed programmes require location-specific systems rather than a universal input package."),
    ("Institutional federalism", "Union departments and ICAR can set guidelines, research and standards, but states, districts, universities, KVKs, extension systems, FPOs and local service networks determine adaptation and implementation."),
    ("Complementarity and weakest link", "Mission outcome depends jointly on research, quality supply, extension, water and input complements, finance, market readiness and repair or service; one near-zero link can defeat a strong technology."),
    ("Output and outcome ladder", "Funds, training, demonstrations, kits, assets or area are inputs, activities and outputs; continued adoption, yield, quality, net income, resilience, ecology and equity are outcomes or impacts."),
    ("National Horticulture Mission PYQ", "The 2018 GS-III demand requires assessment of production, productivity and farmer income; higher horticulture output does not prove higher net income when perishability, price, cost and market power intervene."),
    ("Palm-oil distinctions", "African oil palm originated in tropical Africa; palm oil comes mainly from the fruit mesocarp and palm-kernel oil from the kernel, while mission evaluation separately tests ecology, gestation and processing proximity."),
    ("Cluster and smallholder inclusion", "Clusters can lower extension, machinery, aggregation and certification costs, but can exclude isolated, tribal, tenant, women or rainfed farmers and strengthen a single buyer without safeguards."),
    ("Evaluation and attribution", "National before-after production growth cannot establish mission causation because rainfall, prices, area, trade and unrelated technology also change; credible evaluation needs a theory of change and comparison."),
    ("Mission redesign rule", "Mission 2.0 should diagnose the binding constraint, fund a portfolio, align markets, publish distributional and ecological results, preserve open standards and define scaling, sunset or redesign conditions."),
]

TRAPS_29 = [
    "Do not treat every programme bearing Mission in its name as mission-mode policy.",
    "Do not reduce agricultural technology to machines, drones or laboratory research.",
    "Do not equate distribution, demonstration, registration or availability with adoption.",
    "Do not merge historical and current mission names or mini-mission structures.",
    "Do not treat NMEO-OS and NMEO-OP as one crop system.",
    "Do not convert an approved outlay or target into expenditure, reach or achievement.",
    "Do not use area or production growth as proof of farmer net-income gain.",
    "Do not ignore state, district, extension, repair and market complements.",
    "Do not attribute national change solely to a mission without a counterfactual.",
    "Do not scale a locally successful technology without ecological and inclusion tests.",
]

PANELS_29 = [
    panel(29, "Mission-mode policy rail", "cause-effect-rail", ["DEFINED BOTTLENECK", "-> TECHNOLOGY PORTFOLIO", "-> DELIVERY + ADOPTION", "-> OUTCOME + FEEDBACK"]),
    panel(29, "Mission-versus-scheme test", "comparison-matrix", ["MISSION -> outcome + convergence", "ROUTINE SCHEME -> activity risk", "TITLE != design", "TEST theory of change"]),
    panel(29, "Research-to-market chain", "value-chain", ["RESEARCH -> TRIAL", "-> MULTIPLICATION + EXTENSION", "-> FINANCE + COMPLEMENTS", "-> MARKET + REPEATED USE"]),
    panel(29, "Technology family map", "classification-tree", ["BIOLOGICAL + AGRONOMIC", "MECHANICAL + WATER", "DIGITAL + POST-HARVEST", "INSTITUTIONAL innovation"]),
    panel(29, "Adoption threshold", "decision-board", ["EXPECTED RETURN", "- PURCHASE + LEARNING", "- FAILURE + MARKET RISK", "> EXISTING PRACTICE"]),
    panel(29, "Mission chronology spine", "timeline", ["1986 -> OILSEEDS", "2000 -> COTTON", "2005-06 -> NHM", "2007-08 -> NFSM"]),
    panel(29, "Oilseed system split", "comparison-matrix", ["NMEO-OS -> annual oilseeds", "NMEO-OP -> perennial oil palm", "APPROVAL != reach", "TARGET != outcome"]),
    panel(29, "Horticulture income chain", "value-chain", ["PLANTING MATERIAL", "-> PRODUCTION + QUALITY", "-> COLD CHAIN + MARKET", "-> NET INCOME only after cost + price"]),
    panel(29, "Diffusion institution map", "institution-map", ["UNION + ICAR", "STATE + DISTRICT", "KVK + EXTENSION + FPO", "FARMER FEEDBACK closes loop"]),
    panel(29, "Mission complementarity and weakest-link diagnostic", "bottleneck-map", ["QUALITY SEED", "TRUSTED EXTENSION", "FINANCE + WATER ACCESS", "MARKET + REPAIR SERVICE"]),
    panel(29, "Mission evaluation and attribution ladder", "status-ladder", ["BUDGET INPUT", "-> DELIVERY ACTIVITY", "-> MEASURABLE OUTPUT", "-> OUTCOME -> LONG-TERM IMPACT"]),
    panel(29, "Technology-mission answer spine", "answer-spine", ["DEFINE problem + mission", "TRACE research to market", "TEST inclusion + ecology", "EVALUATE outcome + redesign"]),
]

PYQS_29 = [
    common.make_pyq_solution(FACTS_29, "2018", "GS-III", "Role of the National Horticulture Mission in production, productivity and farmer income.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [0, 2, 7, 14, 15, 18]),
]

TOPIC_29 = common.topic(
    29,
    "Agricultural Technology Missions and Mission-Mode Policy",
    STEMS[29],
    f"{STEMS[29]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_29,
    TRAPS_29,
    [
        (10, "Distinguish a technology mission from a routine agricultural scheme.", [0, 1, 2]),
        (10, "Explain why demonstration and platform availability do not prove technology adoption.", [4, 13]),
        (15, "Trace the historical evolution of India's major agricultural technology missions.", [5, 6, 7, 8, 9]),
        (15, "Assess the National Horticulture Mission's effect on farmer income.", [7, 14, 15, 18]),
        (20, "Evaluate agricultural mission-mode policy through federalism, diffusion, inclusion and ecology.", [10, 11, 12, 13, 17, 18]),
        (20, "Design an outcome-oriented next generation agricultural technology mission.", [0, 2, 3, 4, 14, 18, 19]),
    ],
    [
        "Mission-mode definition and design test",
        "Mission name versus mission mechanism",
        "Research-to-market innovation chain",
        "Technology families beyond machinery",
        "Farmer adoption threshold",
        "Oilseed-mission chronology",
        "Oilseed and oil-palm system boundary",
        "NHM to MIDH evolution",
        "NFSM and nutrition architecture",
        "Cotton mission and value-chain design",
        "Extension-system functions",
        "Sustainability and location specificity",
        "Federal delivery architecture",
        "Weakest-link and cluster economics",
        "Evaluation, attribution and redesign",
    ],
    [
        "Start with the bottleneck and the complete research-to-market chain, not a scheme list.",
        "Separate approval, outlay, activity, reach, adoption, output and farmer-income outcome.",
        "Judge a mission by additionality, inclusion, ecology and the credibility of its evaluation.",
    ],
    PANELS_29,
    ["Technology Mission on Oilseeds", "National Horticulture Mission", "MIDH", "National Food Security Mission", "NMEO-OS", "NMEO-OP", "Technology Mission on Cotton", "NMAET", "NMSA", "adoption", "diffusion", "palm-kernel oil"],
    "Audited ledgers route the 2018 GS-III National Horticulture Mission demand and the 2021 objective palm-oil concept. The Basic/practice firewall preserves origin, mesocarp, kernel, mission-system and income distinctions without inferring an unavailable objective key.",
    PYQS_29,
    [
        "https://agriwelfare.gov.in/en/Oilseeds — substantive Agriculture Ministry page fetched 2026-09-03; confirms separate NMEO-OS and NMEO-OP value-chain architectures. Displayed outlays, areas and targets were not imported.",
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2258111&reg=3&lang=1 — direct fetch returned HTTP 403 on 2026-09-03; no cotton-mission status, mini-mission, outlay, period or target claim was imported from the failed request.",
    ],
    "The oilseeds page substantively confirmed distinct mission architectures. The cotton release was inaccessible, so the package relies on the audited owners and imports no live outlay, target, launch, approval, expenditure, adoption or production claim.",
    extra=[
        "basic/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md",
        "advanced/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md",
        "basic/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        "advanced/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        "basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "advanced/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "basic/15_Food-Processing-Cold-Chains-and-Value-Addition.md",
        "advanced/15_Food-Processing-Cold-Chains-and-Value-Addition.md",
        "basic/27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers.md",
        "advanced/27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers.md",
    ],
)


FACTS_30 = [
    ("Scope and sector boundary", "Animal rearing covers terrestrial livestock and poultry, while aquaculture is managed aquatic farming and capture fishing harvests a natural stock; processing and retail are downstream activities rather than rearing."),
    ("Biological stock and annual flow", "Livestock Census measures a point-in-time biological stock, the Integrated Sample Survey estimates annual product flows, and Basic Animal Husbandry Statistics consolidates official sector data; their vintages are not interchangeable."),
    ("Asset and production-unit character", "An animal is both a productive asset and a source of recurring output, offspring, manure and terminal value, so disease or distress sale can destroy current income and future earning capacity."),
    ("Net enterprise income", "Animal-enterprise profitability equals product and by-product revenue plus asset-value change minus feed, labour, health, breeding, housing, finance, mortality, spoilage, transport and market costs; gross production is not net income."),
    ("Productivity complementarity", "Realised output reflects genetics, nutrition, health, reproduction, management, climate adaptation and market access; breed improvement alone cannot overcome feed or veterinary constraints."),
    ("Feed and fodder economics", "Feed and fodder are major recurring costs in many systems, and scarcity, quality, competing land use and concentrate-price volatility affect lifetime productivity, fertility and margin."),
    ("Disease and One Health", "Vaccination, surveillance, diagnostics and biosecurity generate network benefits because one producer's prevention reduces disease risk for others, while zoonoses and antimicrobial resistance connect animal, human and environmental health."),
    ("Dairy value chain", "Milk's daily production and perishability make collection, transparent fat or SNF testing, chilling, transport, processing and producer payment central to value realisation."),
    ("Operation Flood boundary", "Operation Flood was launched in 1970 and implemented in three phases through producer cooperatives, market links and input services; cooperative form improves aggregation but does not eliminate governance or local monopsony risk."),
    ("Poultry integration", "In an integrator model the firm may supply chicks, feed, medicine, technical protocol and market access while the farmer supplies shed, utilities, labour and management; risk is reallocated, not removed."),
    ("Small ruminants and pastoral systems", "Sheep, goats and related systems can suit drylands and land-poor households, but depend on grazing access, mobility, health, breeding, fibre or meat markets and common-property governance."),
    ("Fisheries production systems", "Capture fisheries face common-pool stock and excessive-effort risks, whereas aquaculture depends on managed seed, feed, water quality, stocking, biosecurity and effluent control."),
    ("MSY and economic yield", "Maximum Sustainable Yield is a biological stock-yield concept, while Maximum Economic Yield concerns economic rent; neither alone settles equity, ecosystem or small-fisher rights."),
    ("Aquaculture biofilter boundary", "A recirculating-aquaculture biofilter supports microbial treatment of ammonia within a larger water-treatment system; it is not complete removal of every solid, pathogen, nutrient or chemical contaminant."),
    ("Integrated Farming System", "IFS intentionally links crops and allied enterprises through residue, feed, manure, pond, nutrient and income flows, but integration becomes pollution transfer when disease or nutrient loads exceed absorptive capacity."),
    ("Employment classification", "Animal rearing is an allied primary-sector activity that creates non-crop rural work, while feed services, veterinary care, transport, testing, processing, retail and equipment generate upstream and downstream non-farm employment."),
    ("Gender and control", "Women's labour participation in feeding, cleaning, milking or backyard poultry does not prove ownership, cooperative voice, decision-making or control over sale proceeds."),
    ("Institutions and scheme mechanisms", "DAHD, the Department of Fisheries, ICAR systems, NDDB, states, producer organisations, FSSAI and export bodies have distinct roles; scheme names must be tied to health, genetics, infrastructure, finance or value-chain mechanisms."),
    ("Rashtriya Gokul Mission boundary", "Rashtriya Gokul Mission concerns bovine genetic improvement and breeding infrastructure, including indigenous cattle; it does not by itself supply feed, health, chilling, income or market outcomes."),
    ("Environment and biosecurity", "Emissions intensity per unit of output can fall while absolute emissions rise with herd or output expansion, so policy must track methane, manure, nutrient load, AMR, welfare, aquatic carrying capacity and disease boundaries."),
]

TRAPS_30 = [
    "Do not merge livestock rearing, aquaculture, capture fishing and downstream processing.",
    "Do not use a livestock stock count as an annual milk, egg, meat or fish flow.",
    "Do not equate total production with net producer income.",
    "Do not treat genetics or artificial insemination as sufficient without feed and health.",
    "Do not infer fair producer price merely from organised milk procurement.",
    "Do not claim that poultry integration removes farmer risk.",
    "Do not equate Maximum Sustainable Yield with maximum profit or equitable allocation.",
    "Do not describe a biofilter as complete aquaculture water purification.",
    "Do not infer women's income control from their labour participation.",
    "Do not convert a scheme's coverage or infrastructure into disease, income or export outcomes.",
]

PANELS_30 = [
    panel(30, "Animal-economy value rail", "value-chain", ["BIOLOGICAL ASSET", "-> INPUT + HEALTH SYSTEM", "-> PRODUCT FLOW", "-> MARKET + HOUSEHOLD WELFARE"]),
    panel(30, "Stock-flow-statistics split", "comparison-matrix", ["LIVESTOCK CENSUS -> stock", "ISS -> annual production flow", "BAHS -> compiled publication", "YEAR + instrument must match"]),
    panel(30, "Lifetime-return board", "formula-board", ["OUTPUT + OFFSPRING + ASSET VALUE", "- FEED + HEALTH + LABOUR", "- MORTALITY + FINANCE + LOSS", "= NET ENTERPRISE RETURN"]),
    panel(30, "Productivity complement chain", "bottleneck-map", ["GENETICS", "x FEED", "x HEALTH + MANAGEMENT", "x CLIMATE + MARKET"]),
    panel(30, "Dairy collection chain", "value-chain", ["MILKING HOUSEHOLD", "-> TESTING + PAYMENT", "-> CHILLING + PROCESSING", "-> CONSUMER + PRODUCER SHARE"]),
    panel(30, "Operation Flood institution map", "institution-map", ["VILLAGE SOCIETY", "-> DISTRICT UNION", "-> STATE FEDERATION", "COOPERATIVE != automatic good governance"]),
    panel(30, "Poultry risk allocation", "principal-agent-map", ["INTEGRATOR -> chick + feed + market", "FARMER -> shed + labour + utilities", "CONTRACT -> mortality + quality rules", "RISK REALLOCATED, not erased"]),
    panel(30, "Disease externality loop", "risk-map", ["UNDER-VACCINATION", "-> NETWORK TRANSMISSION", "-> ASSET + PUBLIC-HEALTH LOSS", "SURVEILLANCE + COMPENSATION + BIOSECURITY"]),
    panel(30, "Aquatic-system split", "comparison-matrix", ["CAPTURE -> common-pool stock", "AQUACULTURE -> managed farming", "MSY != MEY", "EFFLUENT + DISEASE boundaries"]),
    panel(30, "IFS circular flow", "circular-flow", ["CROP RESIDUE -> FEED", "MANURE -> SOIL / BIOGAS", "POND -> NUTRIENT + INCOME", "ABSORPTIVE LIMIT prevents waste transfer"]),
    panel(30, "Inclusion and value board", "distribution-board", ["LANDLESS + SMALLHOLDER", "WOMEN + PASTORALIST", "OWNERSHIP + INCOME CONTROL", "MARKET POWER + TIME BURDEN"]),
    panel(30, "Animal-economy answer spine", "answer-spine", ["DEFINE asset + production system", "TRACE feed + health + market", "TEST inclusion + biosecurity", "CONCLUDE lifetime net social value"]),
]

PYQS_30 = [
    common.make_pyq_solution(FACTS_30, "2019", "GS-III", "Role of Integrated Farming Systems in sustaining agricultural production.", "Official-paper demand cross-routed in the audited 2018-2023 GS-III ledger.", [2, 4, 14, 15, 19]),
    common.make_pyq_solution(FACTS_30, "2022", "GS-III", "Benefits of Integrated Farming Systems for small and marginal farmers.", "Official-paper demand cross-routed in the audited 2018-2023 GS-III ledger.", [3, 5, 14, 15, 16]),
]

TOPIC_30 = common.topic(
    30,
    "Economics of Animal Rearing, Livestock, Dairy, Poultry and Fisheries",
    STEMS[30],
    f"{STEMS[30]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_30,
    TRAPS_30,
    [
        (10, "Why must animal-rearing performance be measured through lifetime net return rather than headcount?", [2, 3, 4]),
        (10, "Distinguish livestock stock statistics from annual production-flow statistics.", [0, 1]),
        (15, "Analyse the economics of dairy collection and cooperative organisation.", [5, 7, 8, 16]),
        (15, "Examine risk allocation in poultry integration and animal-disease control.", [6, 9, 19]),
        (20, "Evaluate fisheries and aquaculture through biological, economic and ecological boundaries.", [11, 12, 13, 19]),
        (20, "Design an inclusive One-Health-compatible strategy for India's animal economy.", [3, 4, 5, 6, 14, 15, 16, 17, 18, 19]),
    ],
    [
        "Animal-rearing and aquatic-sector boundary",
        "Biological stock and annual production flow",
        "Animal as asset and production unit",
        "Net enterprise-income accounting",
        "Genetics, feed, health and market complements",
        "Feed and fodder cost system",
        "Disease externality and One Health",
        "Dairy value-chain economics",
        "Operation Flood and cooperative governance",
        "Poultry integration and contracts",
        "Small ruminants and common resources",
        "Capture fisheries and aquaculture",
        "MSY, MEY and fishery governance",
        "Biofilters and Integrated Farming Systems",
        "Employment, inclusion, institutions and ecology",
    ],
    [
        "Begin with the biological asset, production flow and full cost boundary.",
        "Trace producer margin through feed, health, mortality, collection, processing and market power.",
        "Qualify growth with One Health, welfare, gender, commons and carrying-capacity limits.",
    ],
    PANELS_30,
    ["Livestock Census", "Integrated Sample Survey", "Operation Flood", "feed conversion", "One Health", "biosecurity", "Maximum Sustainable Yield", "Maximum Economic Yield", "biofilter", "Integrated Farming System", "Rashtriya Gokul Mission", "primary-sector activity"],
    "Audited ledgers route the 2019 and 2022 Integrated Farming System demands and objective concepts on livestock emissions, aquaculture biofilters, sector classification, Rashtriya Gokul Mission and FAO Blue Transformation. The Basic/practice firewall carries them without inferring objective answer letters.",
    PYQS_30,
    [
        "https://www.nddb.coop/about/genesis/flood — substantive NDDB page fetched 2026-09-03; confirms the 1970 launch, three phases and producer-cooperative institution-building. Historical scale figures were not imported.",
        "https://dahd.gov.in/en/schemes-programmes — fetch on 2026-09-03 returned only a title-level shell; no scheme coverage, outlay, beneficiary, production or health outcome was imported.",
        "https://dahd.gov.in/en/schemes/programmes/national_livestock_mission — fetch on 2026-09-03 returned only a title-level shell; no component, target, expenditure or reach claim was imported.",
        "https://www.dof.gov.in/offerings — direct fetch returned HTTP 403 on 2026-09-03; no fisheries production, export, infrastructure, welfare or scheme figure was imported.",
    ],
    "NDDB substantively confirmed Operation Flood's institutional history. DAHD pages were shells and the fisheries page was blocked, so the package imports no current livestock, milk, egg, meat, fish, export, income, census-release, scheme-coverage or disease-outcome figure.",
    extra=[
        "basic/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md",
        "advanced/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md",
        "basic/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        "advanced/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        "basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "advanced/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "basic/15_Food-Processing-Cold-Chains-and-Value-Addition.md",
        "advanced/15_Food-Processing-Cold-Chains-and-Value-Addition.md",
        "basic/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "advanced/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
    ],
)


FACTS_31 = [
    ("Primary and final energy", "Primary energy exists in natural resources before conversion, while electricity and refined fuels are secondary carriers and final energy is what reaches end users; electricity is a power-system carrier, not the whole energy system."),
    ("Power and energy units", "Installed capacity is rated power in MW or GW, while generation is energy produced over time in MWh, GWh or billion units; capacity share and generation share are not interchangeable."),
    ("Energy-service boundary", "A connection, sanctioned project or installed plant does not prove reliable, affordable, accessible or acceptable energy service at the point of use."),
    ("Electricity value chain", "Generation, transmission ownership, system operation, distribution, retail supply and market trading are distinct layers with different competition, coordination and regulatory properties."),
    ("Real-time balancing", "Electricity systems must continuously balance generation, imports and discharge against demand, exports, charging and losses, giving economic value to forecasting, reserves, flexibility, storage and demand response."),
    ("Natural monopoly and competition", "Transmission and distribution wires have strong natural-monopoly features, while generation, trading or retail arrangements may support competition under regulated access, settlement and reliability rules."),
    ("Institutional perimeter", "CEA provides statutory technical advice and planning, CERC regulates inter-state and central-sector matters within mandate, SERCs regulate intra-state and retail matters, Grid-India operates national and regional systems, and DISCOMs deliver and bill retail supply."),
    ("Tariff and subsidy boundary", "An observed below-cost tariff may be financed by explicit state subsidy, cross-subsidy, deferred regulatory recovery or DISCOM debt; these have different fiscal, distributional and investment consequences."),
    ("AT&C and ACS-ARR", "AT&C loss combines technical and commercial energy-recovery failures, while the ACS-ARR gap measures average cost versus realised revenue; reducing one does not guarantee financial viability."),
    ("PPA and procurement risk", "Long-term PPAs enable project finance but allocate fuel, demand, payment, curtailment, change-in-law and technology risks and can create stranded or inflexible cost when assumptions change."),
    ("Access and energy poverty", "Energy access is a ladder from network reach and connection to active metering, availability, reliability, affordability, productive use and clean cooking; connection counts alone are incomplete."),
    ("Coal system boundary", "Thermal and coking coal have different uses and quality constraints, while mining, evacuation, plant stock, combustion, ash and closure form one infrastructure chain; geological resource is not the same as an economically recoverable reserve."),
    ("Petroleum chain and regulator", "Upstream exploration and production differ from midstream transport and storage and downstream refining and marketing; PNGRB's statutory perimeter excludes production of crude oil and natural gas."),
    ("Crude imports and product trade", "High crude-oil import dependence can coexist with large refinery capacity and petroleum-product exports; import dependence must state its commodity and denominator."),
    ("Energy-security dimensions", "Energy security requires availability, accessibility, affordability, acceptability and resilience, including diversification of sources, routes and contracts, stocks, infrastructure, financial viability and shock recovery."),
    ("Renewable integration", "Variable renewable capacity requires transmission, forecasting, flexible generation, storage, demand response, geographical diversity and market design; no fuel cost does not mean zero system cost."),
    ("RPO, REC and finance", "RPO creates a renewable-procurement obligation, REC represents an eligible renewable attribute, and a finance company named REC Limited is a different institution; procurement rules do not by themselves create physical generation."),
    ("Energy efficiency and rebound", "Efficiency supplies the same or better service with less energy input, but total energy use can still rise when output or use expands; energy conservation and efficiency are related but not identical."),
    ("Fuel pricing and transition", "Retail fuel prices can reflect international prices, exchange rate, refining, marketing, freight, taxes and applicable support, while transition policy must separate consumer support, producer support and unpriced external costs."),
    ("Targets and legal status", "A capacity target, planning estimate, scheme outlay, Bill, sanctioned project and achieved generation are separate status categories; current claims must retain the exact date, unit, legal stage and reporting body."),
]

TRAPS_31 = [
    "Do not use power, electricity and total energy as synonyms.",
    "Do not merge MW with MWh or installed capacity with actual generation.",
    "Do not treat a connection or sanctioned project as reliable energy service.",
    "Do not merge transmission ownership, system operation and regulation.",
    "Do not treat tariff subsidy, cross-subsidy and deferred under-recovery as one mechanism.",
    "Do not equate AT&C loss with the ACS-ARR gap.",
    "Do not place crude-oil or natural-gas production inside PNGRB's perimeter.",
    "Do not equate crude import dependence with petroleum-product trade dependence.",
    "Do not call every non-fossil source renewable or every resource a reserve.",
    "Do not convert a target, Bill, outlay or planning estimate into achieved generation.",
]

PANELS_31 = [
    panel(31, "Energy-service value rail", "value-chain", ["PRIMARY RESOURCE / IMPORT", "-> CONVERSION + NETWORK", "-> DISTRIBUTION + END USE", "-> RELIABLE AFFORDABLE SERVICE"]),
    panel(31, "Power-energy distinction", "comparison-matrix", ["MW / GW -> power capacity", "MWh / GWh -> energy flow", "CAPACITY SHARE != generation share", "ELECTRICITY != total energy"]),
    panel(31, "Electricity-layer map", "layer-map", ["GENERATION", "TRANSMISSION + SYSTEM OPERATION", "DISTRIBUTION + RETAIL", "MARKET + REGULATION"]),
    panel(31, "Real-time balance board", "formula-board", ["GENERATION + IMPORT + DISCHARGE", "=", "DEMAND + EXPORT + CHARGE + LOSS", "RESERVE + FLEXIBILITY protect balance"]),
    panel(31, "Institutional perimeter", "institution-map", ["CEA -> technical planning", "CERC / SERC -> regulation", "GRID-INDIA / SLDC -> operation", "DISCOM -> retail service"]),
    panel(31, "Tariff-finance split", "four-way-map", ["EXPLICIT STATE SUBSIDY", "CROSS-SUBSIDY", "REGULATORY ASSET", "DISCOM DEBT / UNDER-RECOVERY"]),
    panel(31, "DISCOM diagnostic", "risk-board", ["AT&C -> energy recovery", "ACS-ARR -> revenue-cost gap", "PPA + SUBSIDY + COLLECTION", "ONE RATIO cannot diagnose all stress"]),
    panel(31, "Petroleum perimeter", "value-chain", ["UPSTREAM -> production", "MIDSTREAM -> pipeline + storage", "DOWNSTREAM -> refining + marketing", "PNGRB excludes crude + gas production"]),
    panel(31, "Energy-security dimensions and resilience pentagon", "five-part-map", ["PHYSICAL AVAILABILITY", "INFRASTRUCTURE ACCESSIBILITY", "USER AFFORDABILITY", "SOCIAL ACCEPTABILITY + SYSTEM RESILIENCE"]),
    panel(31, "Renewable-integration chain", "system-map", ["VARIABLE CAPACITY", "-> GRID + FORECAST", "-> FLEXIBILITY + STORAGE", "-> RELIABLE GENERATION VALUE"]),
    panel(31, "Status and unit ladder", "status-ladder", ["ANNOUNCED / BILL", "APPROVED / SANCTIONED / OUTLAY", "INSTALLED CAPACITY", "GENERATION + SERVICE OUTCOME"]),
    panel(31, "Energy-economics answer spine", "answer-spine", ["DEFINE carrier + unit + layer", "TRACE network + tariff + regulator", "TEST security + transition", "CONCLUDE service, not headline capacity"]),
]

PYQS_31 = [
    common.make_pyq_solution(FACTS_31, "2018", "GS-III", "Affordable, reliable, sustainable and modern energy as a development driver.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [2, 10, 14, 17]),
    common.make_pyq_solution(FACTS_31, "2022", "GS-III", "Renewable-energy target and the shift from fossil-fuel subsidies.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [7, 14, 15, 18, 19]),
]

TOPIC_31 = common.topic(
    31,
    "Energy Infrastructure Economics, Power, Fuels and Energy Security",
    STEMS[31],
    f"{STEMS[31]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_31,
    TRAPS_31,
    [
        (10, "Distinguish installed power capacity, electricity generation and final energy service.", [0, 1, 2]),
        (10, "Explain why transmission ownership, system operation and regulation are distinct.", [3, 4, 6]),
        (15, "Analyse DISCOM stress through tariff, subsidy, loss and procurement channels.", [7, 8, 9]),
        (15, "Examine India's petroleum value chain and PNGRB's regulatory perimeter.", [12, 13, 18]),
        (20, "Evaluate renewable integration through system value rather than capacity addition alone.", [1, 4, 15, 16, 17, 19]),
        (20, "Design an energy-security strategy balancing affordability, access, resilience and transition.", [2, 10, 11, 12, 13, 14, 15, 18, 19]),
    ],
    [
        "Primary, secondary and final energy",
        "Capacity, generation and unit discipline",
        "Energy access and service outcomes",
        "Electricity-sector functional layers",
        "Real-time balancing and flexibility",
        "Natural monopoly and contestable layers",
        "CEA, CERC, SERC, Grid-India and DISCOM",
        "Tariff, subsidy and cross-subsidy",
        "AT&C loss and ACS-ARR gap",
        "PPAs, markets and risk allocation",
        "Access ladder and energy poverty",
        "Coal, resource and reserve boundary",
        "Petroleum value chain and PNGRB",
        "Energy security and import denominators",
        "Renewable integration, efficiency and status",
    ],
    [
        "Fix the energy carrier, unit, time period and institutional layer before making a claim.",
        "Evaluate infrastructure through delivered reliability and affordability, not announced capacity.",
        "Balance diversification, financial viability, transition and distributional protection.",
    ],
    PANELS_31,
    ["primary energy", "installed capacity", "generation", "Grid-India", "CERC", "SERC", "AT&C loss", "ACS-ARR gap", "PNGRB", "crude oil", "Renewable Purchase Obligation", "Renewable Energy Certificate", "energy security"],
    "Audited ledgers route the 2018 energy-access, 2020 solar, 2021 Green Grid, 2022 renewable-target and 2025 clean-technology demands, plus objective concepts on PNGRB, coal institutions, solar regulation and ethanol feedstocks. The Basic/practice firewall carries them without inferring objective answers.",
    PYQS_31,
    [
        "https://www.pngrb.gov.in/eng-web/ — substantive PNGRB page fetched 2026-09-03; confirms the Act-based mandate and exclusion of crude-oil and natural-gas production from the Board's regulatory perimeter.",
        "https://powermin.gov.in/en/content/electricity-act-2003 — direct fetch returned HTTP 403 on 2026-09-03; no legal-status, amendment, tariff, market or institutional claim was imported from the failed request.",
        "https://cea.nic.in/dashboard/?lang=en — fetch on 2026-09-03 returned a generic dashboard HTML shell without reliable current data; no capacity, generation, demand, storage, reserve or import figure was imported.",
        "https://beeindia.gov.in/en/programmes/perform-achieve-and-trade-pat — redirected to a generic BEE home page on 2026-09-03; no PAT cycle, target, savings or certificate claim was imported.",
        "https://cercind.gov.in/2023/regulation/IEGC-Regulations-2023.pdf — transport-level fetch failure on 2026-09-03; no grid-code provision was imported.",
    ],
    "PNGRB substantively confirmed its statutory perimeter. Other live sources were blocked, generic or failed, so the package imports no current capacity, generation, reserve, resource, import-dependence, tariff, subsidy, fuel-price, transition-target or achieved-outcome figure.",
    extra=[
        "basic/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md",
        "advanced/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md",
        "basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md",
        "advanced/25_Climate-Economics-Green-Finance-and-Circular-Economy.md",
        "basic/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
        "advanced/28_Direct-and-Indirect-Farm-Subsidies-and-WTO-Rules.md",
    ],
)
