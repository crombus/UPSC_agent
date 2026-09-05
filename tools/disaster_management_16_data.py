"""Authored learner-v2 data for Disaster Management Topic 16."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/en/divisionofmha/disaster-management-division/"
        "response-fund — attempted 2026-09-04; MHA returned HTTP 403. "
        "https://www.indiacode.nic.in/handle/123456789/2045 — attempted "
        "2026-09-04; India Code returned HTTP 403. Statutory fund categories "
        "therefore remain bounded to the audited owners and Act references."
    ),
    (
        "https://fincomindia.nic.in/ — attempted 2026-09-04; the Finance "
        "Commission site returned HTTP 403. https://pib.gov.in/ — searched "
        "2026-09-04 for official Finance Commission and disaster-fund releases; "
        "no corpus, sharing ratio, sanction, expenditure or utilisation figure "
        "was newly imported."
    ),
    (
        "https://irdai.gov.in/ — fetched 2026-09-04 but returned a thin "
        "administrative feature rather than disaster-insurance guidance. "
        "https://ndma.gov.in/ — attempted 2026-09-04; the route was not usable. "
        "Insurance forms and trigger concepts are therefore stated conceptually, "
        "not as claims about Indian market coverage."
    ),
    (
        "https://www.undrr.org/implementing-sendai-framework/what-sendai-"
        "framework — fetched 2026-09-04; UNDRR identified investment in "
        "structural/non-structural risk reduction and Build Back Better in "
        "recovery. https://cdri.world/ — fetched 2026-09-04 for the official "
        "resilient-infrastructure finance and governance route."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Ex-ante finance", "Ex-ante disaster finance is arranged before an event for prevention, mitigation, preparedness, contingent response or pre-agreed recovery; timing alone does not make an instrument risk reducing."),
        ("Ex-post finance", "Ex-post finance is mobilised after impact through budget reallocation, supplementary grants, borrowing, relief funds, appeals or other measures; it can be necessary but may be slow and fiscally disruptive."),
        ("Four-fund statutory grid", "The Disaster Management Act separates the National Disaster Response Fund under section 46, National Disaster Mitigation Fund under section 47, and State response and mitigation funds under section 48; fund and force must never be confused."),
        ("Response versus mitigation funds", "Response funds meet eligible post-event response and relief needs, whereas mitigation funds finance ex-ante risk reduction; a response payment is not proof that future risk was reduced."),
        ("Budgetary and contingency reserves", "Annual budget provisions and contingency reserves retain risk on the public balance sheet but improve liquidity; adequacy depends on rules, replenishment, accessibility and the scale and timing of loss."),
        ("Pre-arranged finance", "Pre-arranged finance fixes eligibility, trigger, amount or drawdown procedure before a disaster so funds can arrive faster; speed does not ensure good targeting, sufficient volume or risk reduction."),
        ("Risk layering", "Risk layering matches frequent lower-severity losses, less frequent medium losses and rare severe losses with different combinations of retention, reserves, contingent credit, insurance and external support."),
        ("Sovereign subnational household layers", "The Union, States, local bodies, utilities, firms and households face different fiscal capacities and loss types; transferring sovereign risk does not automatically protect uninsured households or municipal services."),
        ("Indemnity insurance", "Indemnity insurance pays for verified covered loss subject to policy terms, exclusions, deductibles and limits; loss assessment supports alignment but may delay settlement."),
        ("Parametric insurance", "Parametric insurance pays when a pre-agreed measurable index crosses a threshold, regardless of exact realised loss; it can be rapid but creates basis risk."),
        ("Basis risk", "Basis risk is the mismatch between a parametric payout and actual loss, including no or low payout despite severe local harm or a payout where losses are limited."),
        ("Risk pools", "A risk pool combines diversified participants or exposures and common financing arrangements to spread volatility; correlation, governance, pricing and entry rules determine whether diversification is real."),
        ("Catastrophe bonds", "A catastrophe bond transfers a defined layer of catastrophe risk to capital-market investors through specified triggers and loss of principal or interest; it should be used conceptually unless a dated official deployment is verified."),
        ("Moral hazard and adverse selection", "Moral hazard is changed behaviour after protection reduces the perceived cost of loss, while adverse selection arises when higher-risk participants are more likely to seek cover; design, pricing and safeguards address different problems."),
        ("Fiscal protection", "Fiscal protection aims to preserve timely government financing and essential public services after shocks through risk assessment, layered instruments, transparent rules and debt or budget safeguards."),
        ("Damage loss and needs assessment", "Transparent damage, economic-loss and recovery-needs assessments serve different purposes and baselines; none should be substituted for another merely because each produces a monetary estimate."),
        ("Build Back Better", "Build Back Better uses recovery, rehabilitation and reconstruction to reduce future risk through safer location, standards, services, institutions and livelihoods rather than recreating pre-disaster vulnerability."),
        ("BBB safeguards", "Build Back Better requires participation, tenure and livelihood safeguards, environmental assessment, accessibility, maintenance finance and avoidance of rushed rebuilding in hazardous locations."),
        ("Incentive and affordability balance", "Deductibles, co-financing, risk-based signals and mitigation conditions can reduce moral hazard, but unaffordable pricing can exclude high-risk low-income households and local bodies."),
        ("Finance-outcome firewall", "A fund corpus, allocation rule, policy, premium, bond, pool, payout, sanction or reconstruction budget proves finance or transfer only; coverage, timeliness, equity, safer rebuilding and reduced fiscal loss require separate evidence."),
    ]
    traps = [
        "Do not use ex-ante and risk reduction as synonyms.",
        "Do not confuse NDRF-the-fund with NDRF-the-force.",
        "Do not treat response, mitigation, rehabilitation and reconstruction funds as one category.",
        "Do not infer household protection from sovereign liquidity.",
        "Do not call parametric insurance indemnity insurance.",
        "Do not ignore basis risk when praising rapid trigger-based payout.",
        "Do not use moral hazard and adverse selection interchangeably.",
        "Do not claim catastrophe-bond or risk-pool deployment without a dated official source.",
        "Do not equate money sanctioned or paid with Build Back Better.",
        "Do not rebuild unsafe location, exclusion or ecological harm under the BBB label.",
    ]
    titles = [
        "Ex-ante ex-post and retained fiscal risk",
        "DM Act response mitigation and statutory fund categories",
        "Budget provisions contingency reserves and liquidity",
        "Pre-arranged finance trigger rules and rapid access",
        "Risk layering frequent medium and catastrophic losses",
        "Sovereign subnational utility and household protection layers",
        "Indemnity insurance covered loss assessment and settlement",
        "Parametric triggers basis risk and payout mismatch",
        "Risk pools diversification correlation and governance",
        "Catastrophe bonds as a conceptual capital-market layer",
        "Moral hazard adverse selection pricing and safeguards",
        "Fiscal protection essential services debt and transparency",
        "Damage loss and needs assessment for financing decisions",
        "Build Back Better safeguards and rebuilding-risk prevention",
        "PYQ synthesis finance instruments and outcome firewall",
    ]
    routes = [
        "Classify finance by timing purpose trigger and risk bearer.",
        "Name sections and keep fund force response and mitigation separate.",
        "Explain retained risk liquidity replenishment and access rules.",
        "Separate pre-agreement from automatic adequacy or equitable use.",
        "Match loss frequency and severity to a layered instrument.",
        "Trace who receives liquidity and who still bears final loss.",
        "Explain covered verified loss exclusions deductible and limit.",
        "State index trigger speed and basis-risk consequence.",
        "Test diversification correlation pricing and governance.",
        "Describe transfer mechanics without claiming Indian deployment.",
        "Distinguish post-cover behaviour from hidden high-risk selection.",
        "Protect budget solvency and continuity of essential services.",
        "Fix baseline method purpose and audit trail for each assessment.",
        "Rebuild safer with social environmental tenure and maintenance safeguards.",
        "Conclude with timely equitable finance converted into lower future risk.",
    ]
    panels = [
        common.panel("Finance timing map", "comparison-table", [
            "EX-ANTE -> MITIGATION PREPAREDNESS RESERVE PRE-ARRANGED COVER",
            "EX-POST -> RELIEF REALLOCATION BORROWING APPEAL",
            "RETAIN / TRANSFER / SHARE",
            "TIMING DOES NOT PROVE RISK REDUCTION",
        ], ["Ex-ante finance", "Ex-post finance"]),
        common.panel("Statutory fund grid", "matrix", [
            "s.46 NATIONAL RESPONSE FUND",
            "s.47 NATIONAL MITIGATION FUND",
            "s.48 STATE RESPONSE + MITIGATION FUNDS",
            "FUND != FORCE; RESPONSE != MITIGATION",
        ], ["Four-fund statutory grid", "Response versus mitigation funds"]),
        common.panel("Liquidity ladder", "layered-map", [
            "ANNUAL BUDGET / CONTINGENCY RESERVE",
            "PRE-ARRANGED DRAWDOWN / CONTINGENT FINANCE",
            "INSURANCE / POOL",
            "EXCEPTIONAL BORROWING / EXTERNAL SUPPORT",
        ], ["Budgetary and contingency reserves", "Pre-arranged finance", "Risk layering"]),
        common.panel("Risk-bearer map", "systems-map", [
            "UNION <-> STATE <-> LOCAL BODY / UTILITY",
            "FIRM / HOUSEHOLD / COMMUNITY",
            "LIQUIDITY AT ONE LAYER MAY NOT REACH ANOTHER",
            "MATCH INSTRUMENT TO OWNER AND LOSS TYPE",
        ], ["Sovereign subnational household layers"]),
        common.panel("Insurance split", "comparison-table", [
            "INDEMNITY -> VERIFIED COVERED LOSS",
            "PARAMETRIC -> INDEX CROSSES THRESHOLD",
            "INDEMNITY: ASSESSMENT DELAY",
            "PARAMETRIC: BASIS RISK",
        ], ["Indemnity insurance", "Parametric insurance", "Basis risk"]),
        common.panel("Risk-pool test", "decision-tree", [
            "POOL PARTICIPANTS / EXPOSURES",
            "ARE RISKS SUFFICIENTLY DIVERSE?",
            "PRICE ENTRY RESERVE AND PAYOUT GOVERNANCE",
            "CORRELATED LOSS CAN OVERWHELM NOMINAL DIVERSIFICATION",
        ], ["Risk pools"]),
        common.panel("Cat-bond boundary", "mechanism-chain", [
            "DEFINED RISK LAYER + TRIGGER",
            "INVESTOR CAPITAL AT RISK",
            "TRIGGER EVENT -> PRINCIPAL / INTEREST LOSS -> ISSUER FINANCE",
            "CONCEPT ONLY UNLESS DATED DEPLOYMENT IS VERIFIED",
        ], ["Catastrophe bonds"]),
        common.panel("Insurance incentives", "comparison-table", [
            "MORAL HAZARD -> BEHAVIOUR AFTER PROTECTION",
            "ADVERSE SELECTION -> HIGHER-RISK DEMAND / INFORMATION",
            "TOOLS -> DEDUCTIBLE PRICING CONDITIONS DISCLOSURE",
            "SAFEGUARD -> AFFORDABILITY AND INCLUSION",
        ], ["Moral hazard and adverse selection", "Incentive and affordability balance"]),
        common.panel("Fiscal protection spine", "process-flow", [
            "ASSESS FISCAL EXPOSURE",
            "LAYER RETENTION PRE-ARRANGED AND TRANSFER",
            "PROTECT ESSENTIAL-SERVICE LIQUIDITY",
            "REPORT ALLOCATION EXPENDITURE COVERAGE AND OUTCOME",
        ], ["Fiscal protection"]),
        common.panel("Assessment firewall", "comparison-table", [
            "DAMAGE -> PHYSICAL ASSET EFFECT",
            "LOSS -> FLOW / ECONOMIC EFFECT",
            "NEEDS -> COSTED RECOVERY REQUIREMENT",
            "METHOD BASELINE DATE AND UNCERTAINTY MUST BE EXPLICIT",
        ], ["Damage loss and needs assessment"]),
        common.panel("Build Back Better gate", "audit-ladder", [
            "SAFER SITE / STANDARD / SERVICE DESIGN",
            "TENURE LIVELIHOOD ACCESSIBILITY PARTICIPATION",
            "ENVIRONMENT MAINTENANCE AND FUTURE CLIMATE RISK",
            "REJECT REBUILDING THAT RECREATES OR TRANSFERS RISK",
        ], ["Build Back Better", "BBB safeguards"]),
        common.panel("Disaster-finance answer spine", "answer-spine", [
            "CLASSIFY TIMING PURPOSE TRIGGER AND RISK BEARER",
            "MAP STATUTORY FUNDS RESERVES INSURANCE POOLS AND CONCEPTUAL BONDS",
            "ADD BASIS RISK INCENTIVES AFFORDABILITY AND FISCAL PROTECTION",
            "TEST WHETHER FINANCE PRODUCED EQUITABLE BUILD BACK BETTER",
        ], ["Finance-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Describe disaster resilience, how it is determined and the elements of the Sendai Framework.",
            "Verified support route: disaster finance contributes investment, fiscal protection, continuity and Build Back Better but is not itself the complete resilience definition.",
            [0, 3, 4, 6, 14, 16, 17, 19]),
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss the shift from reactive to proactive disaster management in India.",
            "Verified adjacent governance route; ex-ante mitigation, reserves, pre-arranged finance and risk transfer illustrate proactivity without claiming adequacy or outcome.",
            [0, 1, 2, 3, 4, 5, 14, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss urban flooding as a climate-induced disaster and the policies and frameworks in India that aim at tackling it.",
            "Verified cross-owned route led by Topic 08; this card contributes only mitigation finance, fiscal layering and BBB safeguards for urban assets.",
            [0, 2, 3, 4, 14, 16, 17, 19]),
    ]
    return common.topic(
        16, "Disaster Finance, Risk Transfer and Build Back Better",
        "16_Disaster-Finance-Risk-Transfer-and-Build-Back-Better", facts, traps,
        [
            (10, "Distinguish ex-ante finance, ex-post finance, response funds and mitigation funds.", [0, 1, 2, 3]),
            (10, "Differentiate indemnity and parametric insurance and explain basis risk.", [8, 9, 10]),
            (15, "Explain disaster-risk layering across sovereign, subnational, utility and household levels.", [4, 5, 6, 7, 11]),
            (15, "Analyse moral hazard, adverse selection, affordability and fiscal-protection safeguards.", [13, 14, 18, 19]),
            (20, "Design a pre-arranged disaster-finance strategy combining reserves, contingent finance, insurance and transparent assessment.", [0, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 19]),
            (20, "Critically evaluate Build Back Better as a financial and governance principle rather than a reconstruction slogan.", [2, 3, 14, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "ex-ante", "ex-post", "SDRF", "NDRF", "SDMF", "NDMF",
            "insurance", "risk transfer", "catastrophe bonds",
            "budget reserve funds", "Build Back Better", "recovery",
            "reconstruction", "mitigation", "immediate relief",
        ],
        "No audited 2024-2025 GS-III question directly owns disaster finance. The 2024 resilience question is the closest conceptual route; the 2020 proactive-management and 2024 urban-flood cards are bounded adjacent applications.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts covered MHA response-fund and India Code routes, Finance Commission and PIB, IRDAI/NDMA, UNDRR and CDRI. Several Indian pages were blocked or thin; no funding amount, corpus, payout, coverage, market deployment, utilisation, debt effect or BBB outcome was newly invented.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md", "REVISION-CHART_Hazards-Risk-and-Distinctive-Features.md"],
        register_headings=(
            "FINANCE TIMING STATUTORY FUNDS RISK LAYERS AND TRIGGERS MAP",
            "FUND FORCE PARAMETRIC BASIS-RISK PAYOUT AND OUTCOME FIREWALLS",
            "RETAIN PRE-ARRANGE TRANSFER PROTECT AND BUILD-BACK-BETTER SPINE",
            "CURRENT MHA INDIA-CODE FINANCE-COMMISSION IRDAI UNDRR CDRI BOUNDARY",
        ),
        register_answer_spine=[
            "CLASSIFY EX-ANTE / EX-POST FINANCE BY PURPOSE TRIGGER AND RISK BEARER",
            "SEPARATE s.46 RESPONSE s.47 MITIGATION AND s.48 STATE FUNDS",
            "LAYER BUDGET RESERVE CONTINGENT FINANCE INSURANCE POOL AND EXTREME RISK",
            "DISTINGUISH INDEMNITY / PARAMETRIC PAYOUT AND STATE BASIS RISK",
            "TEST MORAL HAZARD ADVERSE SELECTION CORRELATION AND AFFORDABILITY",
            "USE DAMAGE LOSS AND NEEDS ASSESSMENTS WITH AUDITABLE BASELINES",
            "FINANCE SAFER INCLUSIVE MAINTAINABLE BBB AND VERIFY OUTCOMES",
        ],
    )


TOPIC_16 = _build()
