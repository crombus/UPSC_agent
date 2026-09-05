"""Authored Economy learner-v2 data for Topics 24-27."""

from __future__ import annotations

import generate_economy_common as common


STEMS = {
    24: "24_Services-Digital-Economy-Fintech-and-Platform-Markets",
    25: "25_Climate-Economics-Green-Finance-and-Circular-Economy",
    26: "26_Economic-Survey-Synthesis-and-Current-Macro-Dashboard",
    27: "27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers",
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


FACTS_24 = [
    ("Services heterogeneity", "Services are not one homogeneous sector: tradability, productivity, skill intensity, formality and simultaneity of production and consumption differ across IT, finance, transport, tourism, health, education and personal services."),
    ("Digital public infrastructure boundary", "Digital public infrastructure supplies interoperable identity, payment, data or service rails; it does not imply government ownership of every application operating on those rails."),
    ("RBI and NPCI roles", "RBI regulates payment systems and authorised operators within its legal perimeter, while NPCI operates designated retail payment systems and interfaces; operator and regulator are not interchangeable roles."),
    ("UPI and digital-rupee liability", "UPI sends instructions that transfer commercial-bank deposits, whereas the digital rupee is a direct RBI liability; a payment interface and sovereign digital currency must not be treated as the same instrument."),
    ("ONDC network boundary", "ONDC uses open protocols so buyer-side and seller-side applications can interoperate; it is a network architecture rather than one government marketplace that owns every transaction or participant."),
    ("Multi-sided platform effects", "A platform matches distinct user groups and may subsidise one side to attract another; cross-side network effects, data and switching costs can improve matching while also entrenching market power."),
    ("Fintech unbundling", "Fintech can separate origination, underwriting, funding, payment and servicing across specialised entities, but technological intermediation does not erase the regulated principal's legal obligations or the underlying credit and fraud risks."),
    ("Digital-lending perimeter", "RBI's 2 September 2022 Digital Lending Guidelines apply to specified regulated entities and require their lending-service-provider arrangements not to diminish the regulated entity's obligations."),
    ("Consent-based financial data sharing", "The Account Aggregator framework enables consent-based sharing of financial information through regulated NBFC-AA intermediaries; consent, purpose limitation and data quality remain distinct from credit approval."),
    ("Platform competition tools", "Interoperability, portability, transparent ranking, limits on self-preferencing and competition enforcement can reduce platform gatekeeping, but none by itself guarantees a competitive outcome."),
    ("Access versus capability", "Internet or account access is not digital capability: language, disability, device control, literacy, fraud awareness, assisted access and grievance resolution determine effective inclusion."),
    ("Gig-platform architecture", "Location-based and cloud-based gig work use digital matching, ratings and algorithmic allocation; workforce estimates or transaction growth do not establish stable earnings, employee status or social-security coverage."),
    ("DPDP implementation boundary", "The Digital Personal Data Protection Act, 2023 establishes a consent-or-legitimate-use framework and a Data Protection Board, while the owner's dated account records phased implementation after the November 2025 Rules rather than one fully commenced compliance date."),
    ("Blockchain and cryptocurrency", "Blockchain is a distributed, append-only ledger architecture, while cryptocurrency is one application; neither term is synonymous with every digital database, token or central-bank digital currency."),
    ("Virtual digital asset perimeter", "India's owner records VDA transfer taxation under sections 115BBH and 194S and PMLA reporting-entity duties for service providers, while distinguishing these from legal-tender status or a dedicated securities-style market regulator."),
    ("NFT and metaverse boundary", "An NFT is a unique non-fungible blockchain-recorded token and does not automatically convey copyright; the metaverse is a persistent interoperable virtual-environment concept, not one headset, game or token."),
    ("Merchant Discount Rate", "Merchant Discount Rate is a merchant-side transaction-processing fee shared within the payment chain; it is not the payer's authentication credential or a universal customer charge."),
    ("National Financial Switch", "The National Financial Switch is NPCI's interbank ATM network and is functionally distinct from UPI, RuPay, IMPS and Bharat BillPay even though NPCI operates those systems."),
    ("Crowdfunding perimeter", "Donation, reward, debt or peer-to-peer, and equity crowdfunding offer different returns and fall within different regulatory perimeters; crowdfunding is not one uniformly regulated financial product."),
    ("Dropshipping and principal role", "In dropshipping the seller markets an item without holding the inventory and a third party fulfils the order; outsourcing fulfilment does not automatically remove the seller's consumer-facing responsibility."),
]

TRAPS_24 = [
    "Do not treat aggregate services shares as proof that every service job is high-productivity or formal.",
    "Do not equate a public digital rail with government ownership of every application.",
    "Do not merge RBI's regulatory role with NPCI's operating role.",
    "Do not call UPI a currency or the digital rupee a commercial-bank liability.",
    "Do not turn ONDC into one government marketplace or infer platform share from interoperability.",
    "Do not infer competition merely from low entry costs when network effects and switching costs persist.",
    "Do not let a fintech or lending-service provider obscure the regulated principal's obligations.",
    "Do not upgrade enacted or phased data-protection rules into a single fully commenced deadline.",
    "Do not treat taxation and AML registration as legal-tender recognition or complete market regulation.",
    "Do not infer PYQ answer letters or current platform, payment or adoption figures.",
]

PANELS_24 = [
    panel(24, "Digital-economy transmission rail", "cause-effect-rail", ["IDENTITY + CONNECTIVITY + DATA", "-> INTEROPERABLE RAIL", "-> LOWER SEARCH + TRANSACTION COST", "-> SCALE + INCLUSION + RISK"]),
    panel(24, "Services heterogeneity map", "comparison-matrix", ["TRADABLE -> IT + professional services", "DOMESTIC -> trade + transport + tourism", "ESSENTIAL -> health + education", "AGGREGATE SHARE != uniform productivity"]),
    panel(24, "Rail and application split", "layer-map", ["DPI RAIL -> common protocol", "APPLICATION -> competing interface", "REGULATOR -> legal perimeter", "OPERATOR -> runs designated system"]),
    panel(24, "UPI versus digital rupee", "comparison-matrix", ["UPI -> instruction moving bank deposit", "DIGITAL RUPEE -> direct RBI liability", "INTERFACE != CURRENCY", "KEEP settlement + liability distinct"]),
    panel(24, "ONDC interoperability chain", "network-flow", ["BUYER APP", "-> OPEN PROTOCOL", "-> SELLER APP + LOGISTICS", "NETWORK != one government marketplace"]),
    panel(24, "Platform power loop", "feedback-loop", ["MORE USERS -> MORE MATCHES", "MORE DATA -> BETTER RANKING", "SWITCHING COST -> ENTRY BARRIER", "INTEROPERABILITY -> contestability lever"]),
    panel(24, "Digital-lending responsibility", "principal-agent-map", ["REGULATED ENTITY -> principal duty", "LSP / APP -> technology + servicing role", "DIRECT FLOW + DISCLOSURE -> safeguards", "OUTSOURCING != erased liability"]),
    panel(24, "Data-governance chain", "rights-flow", ["LAWFUL PURPOSE", "-> CONSENT / LEGITIMATE USE", "-> MINIMISATION + SECURITY", "-> CORRECTION + GRIEVANCE"]),
    panel(24, "Digital-asset taxonomy", "classification-tree", ["BLOCKCHAIN -> ledger architecture", "CRYPTO -> private token application", "CBDC -> sovereign RBI liability", "NFT -> unique token; copyright separate"]),
    panel(24, "Payment-system distinctions", "institution-map", ["MDR -> merchant processing fee", "NFS -> interbank ATM network", "UPI PIN -> payer authentication", "NPCI systems remain function-specific"]),
    panel(24, "Platform-work risk board", "distribution-board", ["MATCHING + FLEXIBILITY", "ALGORITHMIC ALLOCATION", "EARNINGS + DEMAND RISK", "LEGAL COVERAGE -> separate Topic 22 route"]),
    panel(24, "Digital-economy answer spine", "answer-spine", ["DEFINE rail + actor + liability", "TRACE cost + scale + network effects", "TEST competition + data + worker risk", "CONCLUDE open rails + accountable applications"]),
]

PYQS_24 = [
    common.make_pyq_solution(FACTS_24, "2021", "GS-I", "Cryptocurrency and its effects on global and Indian society.", "Official-paper demand routed in the audited 2018-2023 ledger; no official model answer is claimed.", [3, 13, 14, 15]),
    common.make_pyq_solution(FACTS_24, "2023", "GS-III", "Status of digitalisation in the Indian economy, associated problems and improvements.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [1, 2, 5, 6, 9, 10, 12]),
]

TOPIC_24 = common.topic(
    24,
    "Services, Digital Economy, Fintech and Platform Markets",
    STEMS[24],
    f"{STEMS[24]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_24,
    TRAPS_24,
    [
        (10, "Distinguish digital public infrastructure from the applications built on it.", [1, 2, 4]),
        (10, "Why are UPI and the digital rupee not interchangeable?", [2, 3]),
        (15, "Examine how network effects create both efficiency and market power in platform markets.", [5, 9, 10]),
        (15, "Assess India's digital-lending and consent-based data-sharing architecture.", [6, 7, 8, 12]),
        (20, "Design a regulatory architecture for fintech and platform markets.", [2, 5, 6, 7, 9, 10, 12]),
        (20, "Evaluate digitalisation through productivity, inclusion, competition, labour and data rights.", [0, 1, 5, 10, 11, 12, 19]),
    ],
    [
        "Services heterogeneity and measurement",
        "Digital public infrastructure",
        "RBI and NPCI roles",
        "UPI and the digital rupee",
        "ONDC and open commerce",
        "Platform markets and network effects",
        "Fintech unbundling",
        "Digital-lending responsibility",
        "Account Aggregators and consent",
        "Competition tools for platforms",
        "Digital access and capability",
        "Gig-platform economics",
        "DPDP implementation boundary",
        "Blockchain, crypto, VDA and NFT",
        "Payments, crowdfunding and dropshipping",
    ],
    [
        "Separate the shared rail, application, operator, regulator and legal principal before evaluating scale.",
        "Trace network effects through matching, data, switching costs, distribution and contestability.",
        "Judge digital inclusion by effective capability, safety and remedy rather than connection counts.",
    ],
    PANELS_24,
    ["digital public infrastructure", "RBI", "NPCI", "UPI", "digital rupee", "ONDC", "network effects", "Digital Lending Guidelines", "Account Aggregator", "DPDP Act", "blockchain", "Merchant Discount Rate"],
    "Audited ledgers route the 2021 cryptocurrency and 2023 digitalisation Mains demands, plus objective concepts on MDR, NFS, UPI authentication, e-commerce, NFTs, CBDC, metaverse, ONDC, dropshipping and crowdfunding. Provisional or unavailable objective keys are not inferred.",
    PYQS_24,
    [
        "https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12382&Mode=0 — substantive RBI circular fetched 2026-09-03; confirms the 2 September 2022 Digital Lending Guidelines, covered regulated entities and continuing principal obligations.",
        "https://www.ondc.org/ — fetch on 2026-09-03 returned only a title-level shell; no coverage, transaction, seller, market-share or operational-scale claim was imported.",
    ],
    "The RBI circular substantively confirmed the digital-lending legal perimeter. The ONDC page was a stub, so the package uses the source owner for architecture only and imports no platform share, transaction count, country coverage or adoption figure.",
    extra=[
        "basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md",
        "advanced/05_Banking-Structure-NBFCs-and-Financial-Regulation.md",
        "basic/08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md",
        "advanced/08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md",
        "basic/22_Employment-Labour-Codes-Skills-and-Demographic-Dividend.md",
        "advanced/22_Employment-Labour-Codes-Skills-and-Demographic-Dividend.md",
    ],
)


FACTS_25 = [
    ("Environmental externality", "An environmental externality is a cost or benefit imposed on others without full market compensation, so private production or consumption decisions may diverge from social welfare."),
    ("Mitigation and adaptation", "Mitigation reduces greenhouse-gas emissions or increases sinks, while adaptation reduces exposure or vulnerability to climate impacts; the two address different parts of climate risk and are complements."),
    ("Carbon-pricing instruments", "A carbon tax sets a statutory price per unit of emissions, while emissions trading determines a market price under a quantity or baseline-and-credit architecture; instrument creation is not proof of emission reduction."),
    ("Social Cost of Carbon", "The Social Cost of Carbon is a model-based monetary estimate of damage from an additional tonne of emissions and is distinct from both a statutory carbon tax and a traded permit or credit price."),
    ("PAT intensity boundary", "Perform, Achieve and Trade sets energy-intensity targets and trades Energy Saving Certificates; intensity improvement can coexist with rising absolute emissions when output expands faster."),
    ("CCTS status boundary", "India's Carbon Credit Trading Scheme is a phased compliance-market architecture whose sector coverage, target years, notification status and market operation must be stated from a dated official source rather than assumed economy-wide."),
    ("Physical and transition risk", "Physical risk arises from acute or chronic climate impacts, while transition risk arises from changes in policy, technology, markets or preferences; both can affect firms, banks, households and public finance."),
    ("Green-finance scope", "Green finance directs capital to eligible environmental or transition-aligned uses, but a green label alone does not establish verified environmental performance or additionality."),
    ("Mitigation and adaptation finance", "Mitigation projects may generate clearer revenue streams, while adaptation often has public-good and avoided-loss benefits; financing one category does not substitute for the other."),
    ("Green and sustainability bonds", "Green bonds finance eligible environmental uses, while sustainability bonds may combine environmental and social uses; both require credible frameworks, allocation reporting and verification."),
    ("Sovereign green-bond boundary", "India's sovereign green bonds earmark government borrowing for eligible public green projects under a framework; earmarking is not certified expenditure, completed assets or measured climate outcome."),
    ("Taxonomy and verification", "A taxonomy classifies eligible activities and can reduce information asymmetry, but credible claims still require use-of-proceeds tracking, metrics, assurance and safeguards against greenwashing."),
    ("BRSR disclosure boundary", "SEBI's Business Responsibility and Sustainability Reporting framework standardises sustainability disclosure for its covered listed-company perimeter; disclosure improves information but does not itself prove impact."),
    ("Circular-economy hierarchy", "Circularity prioritises reduction, redesign, durability, reuse, repair, refurbishment and remanufacture before residual material recovery; recycling alone is not a circular economy."),
    ("Extended Producer Responsibility", "Extended Producer Responsibility shifts specified end-of-life obligations towards producers for notified product or waste categories, but compliance certificates require monitoring of actual collection and processing."),
    ("Additionality", "Environmental additionality asks whether finance or policy caused benefits beyond a credible baseline; relabelling an already-financed activity is not the same as additional climate action."),
    ("Just transition", "A just transition addresses workers, regions, consumers, affordability and energy access during structural decarbonisation; a carbon market or green bond does not automatically fund these distributional costs."),
    ("CBAM and domestic policy", "The EU Carbon Border Adjustment Mechanism is an external import instrument, while India's CCTS and monitoring systems are domestic policies; any recognition or offset link must be verified rather than presumed."),
    ("Intensity and absolute emissions", "Emission intensity measures emissions per unit of output, whereas absolute emissions measure total emissions; a target or achievement in one metric cannot be silently converted into the other."),
    ("Installation flow and capacity stock", "Renewable installations over a stated period are a flow addition, while total installed capacity is a point-in-time stock; period additions, targets and operating generation are different quantities."),
]

TRAPS_25 = [
    "Do not use mitigation and adaptation as synonyms or treat finance for one as finance for both.",
    "Do not equate the Social Cost of Carbon, a carbon tax and a traded carbon price.",
    "Do not convert intensity improvement into a claim of falling absolute emissions.",
    "Do not describe a phased or draft carbon-market status as economy-wide mature operation.",
    "Do not treat a green label, taxonomy classification or disclosure as verified additionality.",
    "Do not merge green bonds and sustainability bonds or borrowing and expenditure outcomes.",
    "Do not reduce circular economy to recycling or ignore repair and reuse.",
    "Do not treat CBAM as part of India's domestic carbon market.",
    "Do not convert an approved target or finance envelope into achievement.",
    "Do not infer objective answer letters, current carbon prices, recycling rates or finance totals.",
]

PANELS_25 = [
    panel(25, "Externality-to-transition rail", "cause-effect-rail", ["RESOURCE USE + EMISSIONS", "-> UNPRICED SOCIAL COST", "-> PRICE + RULE + FINANCE", "-> LOW-CARBON RESILIENT OUTCOME"]),
    panel(25, "Mitigation-adaptation split", "comparison-matrix", ["MITIGATION -> emissions + sinks", "ADAPTATION -> exposure + vulnerability", "FINANCE MODELS differ", "BOTH required; neither substitutes"]),
    panel(25, "Carbon-value triangle", "three-way-map", ["SCC -> damage valuation", "CARBON TAX -> statutory price", "TRADING PRICE -> market outcome", "THREE VALUES may diverge"]),
    panel(25, "PAT-to-CCTS boundary", "status-ladder", ["PAT -> energy intensity", "CCTS -> GHG compliance architecture", "SECTOR + YEAR -> dated notification", "PHASED STATUS != economy-wide market"]),
    panel(25, "Climate-risk channels", "risk-map", ["PHYSICAL -> hazard exposure", "TRANSITION -> policy + technology", "CREDIT + MARKET + OPERATIONAL", "HOUSEHOLD + FISCAL transmission"]),
    panel(25, "Green-finance credibility chain", "verification-flow", ["ELIGIBILITY / TAXONOMY", "-> ALLOCATION", "-> OUTPUT + OUTCOME METRIC", "-> ASSURANCE + ADDITIONALITY"]),
    panel(25, "Bond-use boundary", "comparison-matrix", ["GREEN BOND -> environmental uses", "SUSTAINABILITY BOND -> green + social", "SOVEREIGN ISSUE -> earmarked borrowing", "LABEL != completed verified outcome"]),
    panel(25, "Circular-value ladder", "value-retention-ladder", ["REDUCE + REDESIGN", "REUSE + REPAIR", "REFURBISH + REMANUFACTURE", "RECYCLE residual materials"]),
    panel(25, "EPR results chain", "results-chain", ["PRODUCER OBLIGATION", "-> COLLECTION / PROCESSING", "-> CERTIFICATE + VERIFICATION", "-> ACTUAL MATERIAL OUTCOME"]),
    panel(25, "Just-transition map", "distribution-board", ["WORKERS + SKILLS", "REGIONS + REVENUE", "CONSUMERS + AFFORDABILITY", "ENERGY ACCESS + SOCIAL PROTECTION"]),
    panel(25, "Trade-climate boundary", "two-system-map", ["EU CBAM -> external import rule", "INDIA CCTS / MRV -> domestic system", "RECOGNITION -> unsettled unless verified", "TRADE PRESSURE != policy identity"]),
    panel(25, "Climate-economics answer spine", "answer-spine", ["DEFINE metric + status", "TRACE price + finance + innovation", "TEST distribution + additionality", "CONCLUDE credible just transition"]),
]

TOPIC_25 = common.topic(
    25,
    "Climate Economics, Green Finance and Circular Economy",
    STEMS[25],
    f"{STEMS[25]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_25,
    TRAPS_25,
    [
        (10, "Distinguish the Social Cost of Carbon, a carbon tax and a traded carbon price.", [2, 3]),
        (10, "Why is recycling only one part of a circular economy?", [13, 14]),
        (15, "Assess the credibility conditions for green finance.", [7, 9, 10, 11, 12, 15]),
        (15, "Compare mitigation finance with adaptation finance.", [1, 6, 8, 16]),
        (20, "Evaluate India's movement from energy-intensity trading towards a phased carbon market.", [2, 4, 5, 17, 18]),
        (20, "Design a just green-transition strategy combining pricing, finance, circularity and distribution.", [0, 1, 6, 7, 13, 15, 16]),
    ],
    [
        "Externalities and social welfare",
        "Mitigation and adaptation",
        "Carbon tax and emissions trading",
        "Social Cost of Carbon",
        "PAT energy-intensity trading",
        "CCTS phased status",
        "Physical and transition risk",
        "Green-finance scope",
        "Mitigation and adaptation finance",
        "Green and sustainability bonds",
        "Sovereign green bonds",
        "Taxonomy and verification",
        "BRSR and sustainability disclosure",
        "Circularity, EPR and additionality",
        "Just transition, CBAM and metric boundaries",
    ],
    [
        "Fix the climate instrument, metric, sector, notification status and reference period before evaluating it.",
        "Separate label, allocation, output, verified outcome and additionality in every green-finance claim.",
        "Pair efficiency and decarbonisation with worker, regional, affordability and energy-access consequences.",
    ],
    PANELS_25,
    ["externality", "mitigation", "adaptation", "Social Cost of Carbon", "Perform, Achieve and Trade", "Carbon Credit Trading Scheme", "physical risk", "transition risk", "sovereign green bonds", "BRSR", "circular economy", "Extended Producer Responsibility"],
    "Audited ledgers route objective concepts on the Social Cost of Carbon, greenwashing, BRSR, circular-economy emission channels and sustainability bonds. Their concepts are taught in Basic and practice, while unavailable or provisional answer letters are not inferred.",
    [],
    [
        "https://beeindia.gov.in/en/programmes/carbon-market — fetch on 2026-09-03 redirected to a generic BEE landing page with no substantive scheme text; no sector, cycle, target, credit-price or operational-status claim was imported.",
    ],
    "The BEE carbon-market URL returned a generic shell. The package therefore preserves the owner-recorded phased-status boundary and imports no current carbon price, sector target, taxonomy status, recycling rate, climate-finance amount or market-operational claim.",
    extra=[
        "basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "advanced/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "basic/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md",
        "advanced/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md",
        "basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
        "advanced/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
    ],
    pyq_audit_heading="VERIFIED OBJECTIVE PYQ OWNERSHIP AUDIT",
)


FACTS_26 = [
    ("First Advance Estimate", "A First Advance Estimate is released before complete annual data and is revised as fuller information arrives; it is neither a final audited outcome nor a timeless current fact."),
    ("GDP and GVA boundary", "GDP at market prices and GVA at basic prices answer related but distinct questions, so tax and subsidy effects can make their growth rates differ without contradiction."),
    ("Real and nominal boundary", "Real aggregates remove price change using a stated base and method, while nominal aggregates value output at current prices; a real growth rate cannot be compared directly with a nominal level."),
    ("Demand composition", "PFCE, government consumption, gross capital formation and net exports describe expenditure composition; a component's share of GDP and its growth rate are different measures."),
    ("Estimate-vintage sequence", "National accounts move through advance, provisional and revised estimates as data improve; every quoted figure must retain the release date and estimate vintage used by the source."),
    ("BE, RE and actual", "Budget Estimate is a forward plan, Revised Estimate is an in-year reassessment and CGA provisional or final accounts report realised fiscal flows; proposal, revision and outturn are not interchangeable."),
    ("Headline and core inflation", "Headline CPI includes food and fuel while core measures exclude selected volatile components; low headline inflation does not mean every component or household basket became cheaper."),
    ("High-frequency indicators", "High-frequency indicators provide timely signals before complete national accounts, but they are partial proxies whose seasonal, base and coverage effects must be checked."),
    ("Reserve stock and CAD flow", "Foreign-exchange reserves are a point-in-time stock, while the current-account balance is a period flow; a large stock buffer does not by itself correct a persistent flow imbalance."),
    ("External debt stock", "External debt is a liability stock measured at a stated date and must be assessed with maturity, currency, borrower and servicing capacity rather than confused with annual capital inflows."),
    ("PLFS method boundary", "PLFS labour indicators depend on period, geography and status concept such as usual status or current weekly status; one rate without its denominator and method is incomplete."),
    ("Dashboard denominator", "A dashboard indicator must preserve whether it is a level, growth rate, ratio, share, index, stock, flow or per-capita measure and identify the denominator before comparison."),
    ("Survey, Budget and outturn", "An Economic Survey observation or projection, a Budget proposal and a subsequently reported official outturn are different evidence classes and must not be blended into one government commitment or achievement."),
    ("Forecast and potential growth", "A near-term forecast is conditional on assumptions and a data vintage, while potential growth is an assessment of sustainable capacity; neither is an achieved growth rate."),
    ("Macro-stability frame", "Macro stability combines manageable inflation, fiscal credibility, external resilience and financial soundness; one strong growth headline cannot establish stability across all boxes."),
    ("V-shaped recovery boundary", "India's FY21 quarterly real-GDP path recorded a sharp contraction followed by sequential return to positive year-on-year growth, but a V-shaped aggregate path does not prove uniform sectoral or employment recovery."),
    ("FY21 revision example", "The owner distinguishes the NSO May 2021 provisional full-year FY21 contraction estimate of 7.3 percent from the January 2022 revised estimate of 6.6 percent, illustrating why estimate vintage must be retained."),
    ("Global Competitiveness Report", "The World Economic Forum published the Global Competitiveness Report or Index and discontinued that specific annual series after 2019-20; IMD's separate ranking must not be substituted for it."),
    ("Comparable-period synthesis", "Cross-box synthesis is valid only when growth, prices, fiscal, external and labour indicators use comparable and clearly labelled periods; mixing unmatched vintages can create false divergence."),
    ("Strategic resilience and indispensability", "Strategic resilience is the capacity to absorb shocks, while strategic indispensability is the capacity to become a reliable valuable node in global systems; buffers alone do not create productive capability."),
]

TRAPS_26 = [
    "Do not present an FAE, projection, RE or provisional account as a final realised outcome.",
    "Do not merge GDP with GVA or nominal values with real growth.",
    "Do not confuse a demand component's GDP share with its growth contribution.",
    "Do not treat headline CPI as every household's inflation experience.",
    "Do not use a high-frequency proxy as a complete causal explanation.",
    "Do not substitute reserve stock for current-account flow or external debt stock.",
    "Do not quote a PLFS rate without period, status concept and denominator.",
    "Do not merge Survey observation, Budget proposal and official outturn.",
    "Do not infer current September 2026 conditions from a January 2026 Survey vintage.",
    "Do not infer objective answer letters or invent a dashboard value absent a dated official release.",
]

PANELS_26 = [
    panel(26, "Six-box macro dashboard", "dashboard-grid", ["GROWTH + DEMAND", "INFLATION + MONETARY", "FISCAL + INVESTMENT", "FINANCIAL + EXTERNAL + INCLUSION"]),
    panel(26, "Estimate-vintage ladder", "status-ladder", ["FAE / SAE -> early estimate", "PROVISIONAL -> fuller data", "REVISED -> later benchmark", "DATE + VINTAGE travel with value"]),
    panel(26, "GDP-GVA-price boundary", "comparison-matrix", ["GDP -> market prices", "GVA -> basic prices", "REAL -> volume after price adjustment", "NOMINAL -> current-price value"]),
    panel(26, "Demand-composition map", "component-map", ["PFCE + GFCE", "GROSS CAPITAL FORMATION", "NET EXPORTS", "SHARE != growth contribution"]),
    panel(26, "Fiscal evidence ladder", "evidence-ladder", ["BE -> forward plan", "RE -> in-year reassessment", "CGA PROVISIONAL -> realised to date/year", "FINAL ACTUAL -> later outturn"]),
    panel(26, "Inflation reading board", "decomposition-board", ["HEADLINE CPI", "FOOD + FUEL components", "CORE proxy", "EXPECTATIONS + POLICY stance"]),
    panel(26, "Stock-flow external map", "comparison-matrix", ["RESERVES -> stock at date", "EXTERNAL DEBT -> liability stock", "CAD -> period flow", "EXPORTS / IMPORTS -> period flows"]),
    panel(26, "Labour-data boundary", "method-board", ["PLFS PERIOD", "USUAL / WEEKLY STATUS", "LFPR / WPR / UR denominator", "PUBLICATION LAG"]),
    panel(26, "Survey-budget-outturn split", "three-stage-map", ["SURVEY -> diagnosis / projection", "BUDGET -> proposal / estimate", "OFFICIAL RELEASE -> outturn", "DO NOT blend evidence classes"]),
    panel(26, "V-to-K recovery test", "causal-comparison", ["GDP PATH -> contraction then rebound", "BASE EFFECT -> growth comparison", "SECTORAL PATH -> uneven", "JOBS + INFORMALITY -> K-shaped test"]),
    panel(26, "Cross-box synthesis loop", "diagnostic-loop", ["HEADLINE", "-> COMPONENT + DENOMINATOR", "-> COMPARABLE PERIOD + VINTAGE", "-> DRIVER + LIMIT + VERDICT"]),
    panel(26, "Macro-dashboard answer spine", "answer-spine", ["LABEL value + unit + vintage", "CLASSIFY stock / flow / ratio", "CROSS-CHECK six boxes", "CONCLUDE stability + productive capacity"]),
]

PYQS_26 = [
    common.make_pyq_solution(FACTS_26, "2021", "GS-III", "Whether India's economic recovery after COVID-19 was V-shaped.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [7, 15, 16, 18]),
]

TOPIC_26 = common.topic(
    26,
    "Economic Survey Synthesis and Current Macro Dashboard",
    STEMS[26],
    f"{STEMS[26]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_26,
    TRAPS_26,
    [
        (10, "Distinguish GDP, GVA, real values and nominal values.", [1, 2]),
        (10, "Why must Survey figures retain their estimate vintage and denominator?", [0, 4, 11, 12]),
        (15, "Build a six-box framework for assessing macro stability.", [5, 6, 8, 10, 14]),
        (15, "Assess the claim that India's post-COVID recovery was V-shaped.", [7, 15, 16, 18]),
        (20, "Explain how to synthesise growth, inflation, fiscal, external and employment indicators without mixing vintages.", [3, 5, 6, 8, 10, 11, 18]),
        (20, "Evaluate the Economic Survey as a diagnostic guide rather than a record of final outcomes.", [0, 4, 7, 12, 13, 14, 19]),
    ],
    [
        "First Advance Estimates",
        "GDP and GVA",
        "Real and nominal measurement",
        "Demand composition",
        "Estimate-vintage sequence",
        "Budget Estimate, Revised Estimate and actual",
        "Headline and core inflation",
        "High-frequency indicators",
        "Reserve stock and current-account flow",
        "External debt stock",
        "PLFS method and denominator",
        "Dashboard unit and denominator",
        "Survey, Budget and outturn",
        "Forecast, potential and stability",
        "Recovery, comparability and strategic capacity",
    ],
    [
        "Attach unit, denominator, reference period, release date and estimate vintage to every dashboard claim.",
        "Classify every value as stock, flow, level, growth rate, share, ratio, estimate, projection or outturn.",
        "Cross-check the headline against composition, distribution and comparable-period evidence before judging stability.",
    ],
    PANELS_26,
    ["First Advance Estimate", "GDP", "GVA", "PFCE", "Budget Estimate", "Revised Estimate", "CGA", "headline CPI", "foreign-exchange reserves", "current account", "PLFS", "Global Competitiveness Report"],
    "Audited ledgers route the 2021 V-shaped-recovery Mains demand and the 2019 objective demand on the Global Competitiveness Report publisher. The package retains the provisional-versus-revised FY21 figures and does not infer an unavailable objective key.",
    PYQS_26,
    [
        "https://www.indiabudget.gov.in/economicsurvey/ — direct fetch returned HTTP 403 on 2026-09-03; no current macro value or forecast was imported from the blocked page.",
    ],
    "The official Economic Survey landing page was blocked. The package preserves the January 2026 Survey vintage exactly as recorded in the owner, treats its FY26 values as FAE or stated-period observations, and imports no later forecast, outturn or September 2026 dashboard value.",
    extra=[
        "basic/01_National-Income-GDP-GVA-and-Measurement.md",
        "advanced/01_National-Income-GDP-GVA-and-Measurement.md",
        "basic/03_Inflation-Price-Indices-and-Business-Cycles.md",
        "advanced/03_Inflation-Price-Indices-and-Business-Cycles.md",
        "basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        "advanced/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        "basic/19_Balance-of-Payments-Exchange-Rates-and-Forex-Reserves.md",
        "advanced/19_Balance-of-Payments-Exchange-Rates-and-Forex-Reserves.md",
    ],
)


FACTS_27 = [
    ("e-Technology boundary", "e-Technology in agriculture uses electronic, digital, communication and information systems to support farm decisions, services and markets; the Core firewall keeps this Basic route exam-complete without relying on optional Advanced material."),
    ("Digital agriculture and agritech", "Digital agriculture is data-enabled management across the farm cycle, while agritech also includes firms, devices, mechanisation, biotechnology, nanotechnology and business models; neither is one portal."),
    ("Data-to-outcome chain", "Farm and farmer data must be sensed, analysed, converted into advice, implemented through complementary inputs or services and evaluated through outcomes; data availability alone is not farmer welfare."),
    ("Precision-agriculture boundary", "Precision agriculture varies treatment by measured spatial or temporal need; it does not mean zero-input farming or guarantee lower total resource extraction."),
    ("Remote sensing and ground truth", "Remote sensing observes land or crops without direct contact and can signal condition, but cloud, resolution, revisit and crop-similarity limits require ground truth and appeal when used for consequential decisions."),
    ("GIS and GNSS", "GIS stores, combines and analyses geographically referenced data, while GNSS or NavIC supplies positioning and navigation signals; mapping analysis and location signals are related but distinct."),
    ("IoT, AI and automated control", "IoT sensors collect or exchange data, AI or machine learning infers or predicts, and automated control acts; a system may combine them but capability in one layer does not prove the others."),
    ("DPI, platform and physical market", "Agricultural DPI supplies interoperable shared rails and a platform coordinates participants, but neither replaces physical assaying, storage, logistics, finance, settlement, extension or enforcement."),
    ("Digital Agriculture Mission status", "The Union Cabinet approved the Digital Agriculture Mission in September 2024 as an umbrella architecture; approval and sanctioned outlay are not expenditure, farmer adoption or measured outcome."),
    ("AgriStack federal architecture", "AgriStack is designed as federated Centre-state digital infrastructure rather than one undifferentiated central database, so standards, state operation, data quality and correction must be analysed together."),
    ("AgriStack building blocks", "Farmer Registry, geo-referenced village maps and crop-sown information or Digital Crop Survey are distinct building blocks; an identity record, parcel map and seasonal crop observation are not substitutes."),
    ("Krishi-DSS boundary", "Krishi Decision Support System combines geospatial and administrative information for mapping, monitoring and planning. Decision support remains an input to field agronomy and accountable official judgment rather than an autonomous farm-management authority."),
    ("e-NAM market completion", "e-NAM is operated by SFAC under the agriculture ministry and digitises discovery and transaction functions, but completed trade still needs assaying, aggregation, logistics, settlement and dispute resolution."),
    ("Drone platform and payload", "A drone is an unmanned aircraft platform whose mapping, monitoring or spraying capability depends on its payload, configuration, calibration, trained operation and applicable rules."),
    ("Shared-service economics", "High fixed-cost equipment can be more viable through FPO, SHG, cooperative or custom-hiring services than universal individual ownership, but recurring demand, scheduling, maintenance and working capital remain necessary."),
    ("Digital risk assessment", "Remote sensing and digital records can support credit, insurance and loss assessment, but model error, basis risk, stale records and parcel mismatch require disclosure, field checks and an appeal route."),
    ("Adoption and outcome", "Registrations, app downloads, IDs, connected mandis or distributed devices measure activity or availability; adoption, correct use, net income, resilience and resource outcomes require separate evidence."),
    ("Cultivator-inclusion boundary", "Land ownership is not a perfect proxy for cultivation, so tenants, sharecroppers and women cultivators may be excluded unless alternative evidence, assisted access and correction are built into the system."),
    ("Agricultural platform power", "Digital platforms can reduce search costs and old intermediation while data, ranking, tying and switching costs create new gatekeeping; interoperability and portability are economic safeguards."),
    ("100 Million Farmers status", "The World Economic Forum's 100 Million Farmers initiative is a multistakeholder platform with a stated 2030 support ambition, not a Government of India scheme or evidence that the target has been achieved."),
]

TRAPS_27 = [
    "Do not turn digital agriculture into a gadget list or one government portal.",
    "Do not treat remote sensing as ground truth or GIS as GNSS.",
    "Do not merge sensing, AI inference and automated action.",
    "Do not claim that precision efficiency necessarily lowers basin-level resource use.",
    "Do not convert Mission approval, sanctioned outlay or platform availability into adoption or outcome.",
    "Do not treat Farmer Registry, parcel maps and crop-sown data as one interchangeable record.",
    "Do not say e-NAM stores, transports or assays produce by itself.",
    "Do not attribute every drone capability to every aircraft or ignore payload and training.",
    "Do not use land title as a universal proxy for the actual cultivator.",
    "Current farmer counts, coverage, scheme participation, sensor performance and PYQ answer letters require separate dated verification.",
]

PANELS_27 = [
    panel(27, "Farm data-to-outcome rail", "cause-effect-rail", ["DATA", "-> SENSE + CONNECT", "-> ANALYSE + ADVISE + ACT", "-> INCOME + RISK + RESOURCE OUTCOME"]),
    panel(27, "Technology-family map", "classification-tree", ["REMOTE SENSING -> observation", "GIS -> spatial analysis", "GNSS / NAVIC -> positioning", "IOT + AI + CONTROL -> separate layers"]),
    panel(27, "Farm-cycle application chain", "process-flow", ["PLAN + SOW", "MONITOR + APPLY INPUT", "INSURE + HARVEST", "STORE + ASSAY + SELL"]),
    panel(27, "Digital Agriculture Mission map", "institution-map", ["UMBRELLA MISSION", "AGRISTACK", "KRISHI-DSS", "APPROVAL != adoption or outcome"]),
    panel(27, "AgriStack layers", "layer-map", ["FARMER REGISTRY", "GEO-REFERENCED VILLAGE MAP", "CROP-SOWN INFORMATION", "FEDERATED SERVICE INTERFACE"]),
    panel(27, "Krishi-DSS decision boundary", "decision-flow", ["GEOSPATIAL + ADMIN DATA", "-> MAP + MONITOR + MODEL", "-> HUMAN / OFFICIAL DECISION", "SUPPORT != autonomous authority"]),
    panel(27, "e-NAM completion chain", "market-flow", ["ONLINE DISCOVERY + BID", "+ ASSAYING + AGGREGATION", "+ LOGISTICS + SETTLEMENT", "+ ENFORCEMENT = COMPLETED TRADE"]),
    panel(27, "Drone capability matrix", "capability-matrix", ["AIRCRAFT PLATFORM", "PAYLOAD -> camera / sensor / sprayer", "OPERATOR + CALIBRATION", "RULE + WEATHER + MAINTENANCE"]),
    panel(27, "Shared-service economics", "cost-sharing-flow", ["HIGH FIXED COST", "-> FPO / SHG / CUSTOM HIRING", "-> COST SHARED ACROSS USERS", "DEMAND + REPAIR determine viability"]),
    panel(27, "Inclusion and correction board", "rights-board", ["OWNER != CULTIVATOR", "ASSISTED + OFFLINE ACCESS", "DATA CORRECTION", "HUMAN APPEAL"]),
    panel(27, "Activity-to-outcome ladder", "results-chain", ["REGISTRATION / DEVICE / MESSAGE", "-> ACTIVE ADOPTION", "-> CORRECT DECISION", "-> NET INCOME + RESILIENCE"]),
    panel(27, "Digital-agriculture answer spine", "answer-spine", ["NAME farm-stage problem", "TRACE data -> decision -> action", "ADD physical + institutional complement", "TEST inclusion + outcome + remedy"]),
]

PYQS_27 = [
    common.make_pyq_solution(FACTS_27, "2023", "GS-III", "How e-Technology helps farmers in agricultural production and marketing.", "Official-paper demand routed in the audited 2018-2023 GS-III ledger.", [2, 4, 7, 12, 14, 16, 17]),
]

TOPIC_27 = common.topic(
    27,
    "Digital Agriculture, Agritech and e-Technology for Farmers",
    STEMS[27],
    f"{STEMS[27]}_Learner-V2-Complete-Topic-Package.md",
    FACTS_27,
    TRAPS_27,
    [
        (10, "Explain the data-to-decision-to-action chain in digital agriculture.", [0, 1, 2]),
        (10, "Distinguish remote sensing, GIS, GNSS, IoT and AI.", [4, 5, 6]),
        (15, "Assess AgriStack and Krishi-DSS as agricultural digital public infrastructure.", [8, 9, 10, 11, 17]),
        (15, "Why does e-NAM require physical market complements?", [7, 12, 18]),
        (20, "Evaluate agritech through adoption, shared-service economics and farmer welfare.", [2, 3, 13, 14, 16, 17]),
        (20, "Design inclusive and accountable digital agriculture for India.", [7, 9, 10, 15, 16, 17, 18]),
    ],
    [
        "e-Technology, digital agriculture and agritech",
        "Data-to-outcome chain",
        "Precision agriculture",
        "Remote sensing and ground truth",
        "GIS and GNSS",
        "IoT, AI, automated control and physical complements",
        "Digital Agriculture Mission",
        "AgriStack federal architecture",
        "AgriStack building blocks",
        "Krishi-DSS",
        "e-NAM and drone capabilities",
        "Shared-service economics",
        "Digital risk assessment",
        "Adoption and cultivator inclusion",
        "Platform power and 100 Million Farmers status",
    ],
    [
        "Begin with the farm-stage problem and trace data through a decision to an implementable action.",
        "Add the weakest physical, financial, extension, legal or governance complement before claiming benefit.",
        "Judge success by net income, resilience, resource use, inclusion and correctable outcomes rather than activity counts.",
    ],
    PANELS_27,
    ["e-technology", "precision agriculture", "remote sensing", "GIS", "GNSS", "AgriStack", "Farmer Registry", "Krishi-DSS", "e-NAM", "SFAC", "agricultural drones", "100 Million Farmers"],
    "Audited ledgers route the 2023 GS-III e-Technology demand and objective concepts on drone applications and the WEF 100 Million Farmers platform. The Basic session and practice preserve these concepts without inferring unavailable objective keys or platform achievement.",
    PYQS_27,
    [
        "https://agriwelfare.gov.in/Documents/pib_%20DigitalAgricultureMission.pdf — fetched as a substantive official binary PDF on 2026-09-03; no text was inferred from raw binary beyond the already audited owner.",
        "https://agriwelfare.gov.in/en/DigiAgriDiv — substantive official page fetched 2026-09-03; confirms federated AgriStack building blocks and Krishi-DSS architecture, but newly displayed coverage counts were not imported.",
        "https://agri.enam.gov.in/ — direct fetch returned HTTP 404 on 2026-09-03; no current mandi, trade, farmer or platform-coverage figure was imported.",
    ],
    "The Digital Agriculture Division page substantively confirmed architecture. The mission PDF was binary and e-NAM returned 404, so the package imports no new outlay, Farmer-ID, plot, district, mandi, transaction, drone, sensor or scheme-participation figure and keeps approval, rollout, availability, adoption and outcome separate.",
    extra=[
        "basic/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        "advanced/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        "basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "advanced/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md",
        "basic/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
        "advanced/29_Agricultural-Technology-Missions-and-Mission-Mode-Policy.md",
    ],
)
