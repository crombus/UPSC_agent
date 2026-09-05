"""Authored learner-v2 data for Internal Security Topic 10."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.fatf-gafi.org/en/publications/Mutualevaluations/India-"
        "MER-2024.html and https://www.pib.gov.in/ — fetched and attempted "
        "2026-09-04. FATF's official page confirms publication on 19 September "
        "2024, regular follow-up, a three-year report-back cycle, recognised "
        "strengths and prosecution/non-profit-sector recommendations; PIB "
        "retrieval returned 403."
    ),
    (
        "https://fiuindia.gov.in/files/AML_Legislation/notification.html and "
        "https://www.indiacode.nic.in/ — fetched and attempted 2026-09-04. "
        "The FIU-IND page reproduced the PMLA Maintenance of Records framework "
        "and client-due-diligence terminology; India Code returned 403. No "
        "reporting volume, enforcement count or effectiveness outcome is used."
    ),
    (
        "https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566 "
        "and https://www.pib.gov.in/ — fetched and attempted 2026-09-04. The "
        "RBI KYC Master Direction showed an update date of 14 August 2025 and "
        "states the AML/CFT purpose of customer identification and transaction "
        "monitoring; PIB retrieval returned 403. Compliance is not equated with "
        "absence of laundering."
    ),
    (
        "https://enforcementdirectorate.gov.in/what-we-do, "
        "https://www.mha.gov.in/ and https://www.indiacode.nic.in/ — attempted "
        "2026-09-04 for current ED, PMLA, UAPA Section 51A and WMD-financing "
        "material; the ED path returned 404 and the MHA/India Code pages were "
        "not substantively retrievable. Only owner-audited mandates and status "
        "rungs are retained."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Terror-finance laundering distinction", "Terror financing provides or moves value for a terrorist purpose and may use lawful or unlawful origins, whereas money laundering disguises proceeds of crime; the two can intersect but are not the same offence or evidentiary chain."),
        ("Predicate-offence gateway", "PMLA is derivative: proceeds of crime must be linked to a registered scheduled predicate offence, so the quality and status of the underlying investigation shape the laundering case."),
        ("Placement typology", "Placement is the conceptual stage at which illicit proceeds first enter a financial or commercial channel; it is a typology for diagnosis, not a guide to evasion."),
        ("Layering typology", "Layering conceptually describes transactions or structures that distance value from its criminal origin; answers should identify the control failure without reproducing operational concealment techniques."),
        ("Integration typology", "Integration is the stage at which value returns in an apparently legitimate form; legitimate appearance does not by itself establish lawful origin."),
        ("TBML boundary", "Trade-Based Money Laundering moves or disguises value through manipulated trade transactions or documentation; it is distinct from ordinary trade error, customs evasion and virtual-asset laundering and should be discussed only at a non-operational level."),
        ("Clean-clean dirty-clean distinction", "Funds legally generated and transferred but diverted to terror may present fewer criminal-origin indicators than dirty proceeds later laundered, which is why terror-finance risk cannot be reduced to proceeds-of-crime detection."),
        ("Reporting-entity controls", "Customer due diligence, beneficial-owner identification, record maintenance and suspicious-transaction reporting are preventive inputs by regulated or notified reporting entities, not findings of criminal guilt."),
        ("FIU-IND mandate", "FIU-IND under the Department of Revenue receives, analyses and disseminates specified financial intelligence; an STR is an intelligence lead, not an FIR, charge or conviction."),
        ("ED mandate", "The Enforcement Directorate investigates money laundering within PMLA's statutory gateway and may seek provisional attachment; it does not adjudicate guilt or convert every unexplained asset into proceeds of crime."),
        ("PMLA property ladder", "The property chain runs ED provisional attachment, Adjudicating Authority confirmation or release, Special Court adjudication and confiscation on the legally required outcome; attachment and confiscation are different rungs."),
        ("Investigation-prosecution boundary", "Financial intelligence, predicate-offence investigation, PMLA investigation, prosecution, conviction and sanction require coordinated but distinct institutional work; detection strength cannot substitute for timely fair trial."),
        ("UAPA terror-finance route", "UAPA contains terror-fund offences and Section 51A provides a listing-linked route to freeze, seize or attach covered funds and assets and prevent funds being made available; this route is distinct from PMLA's predicate-proceeds model."),
        ("Sanctions-listing boundary", "UN Security Council 1267-linked or domestic designation and targeted financial sanctions are preventive legal statuses, not criminal conviction; review, delisting and identity accuracy remain essential safeguards."),
        ("Proliferation-finance limb", "The WMD Act, 2005 as amended in 2022 prohibits financing connected with prohibited weapons-of-mass-destruction activity, forming a proliferation-financing limb distinct from money laundering and terrorist financing."),
        ("FATF standards role", "FATF sets international AML, CFT and proliferation-financing standards through its Recommendations and assesses legal, institutional and effectiveness performance; it is not a supranational criminal court."),
        ("Mutual Evaluation", "A FATF Mutual Evaluation examines technical compliance and effectiveness outcomes through a peer-review process; formal laws and institutions do not by themselves establish effective implementation."),
        ("Listing-follow-up firewall", "Jurisdictions under increased monitoring and high-risk jurisdictions subject to a call for action are listing processes, while regular or enhanced follow-up describes post-Mutual-Evaluation reporting frequency; grey list, black list and regular follow-up are not synonyms."),
        ("India MER 2024", "FATF's official India page dated 19 September 2024 placed India in regular follow-up and recognised risk understanding, financial-intelligence use, beneficial-ownership access and asset recovery while calling for completed ML/TF trials, appropriate sanctions and risk-based non-profit outreach."),
        ("Compliance-outcome end-state", "An effective AML/CFT system must connect risk assessment, preventive controls, financial intelligence, lawful disruption, predicate investigation, prosecution, conviction or acquittal, confiscation where ordered, international cooperation and rights safeguards."),
    ]
    traps = [
        "Do not use terror financing and money laundering as synonyms.",
        "Do not omit the scheduled predicate offence and proceeds-of-crime gateway.",
        "Do not present placement, layering or integration as evasion instructions.",
        "Do not equate TBML with every customs discrepancy or virtual-asset transfer.",
        "Do not treat an STR as proof of an offence.",
        "Do not describe FIU-IND, ED and the Special Court as interchangeable bodies.",
        "Do not equate provisional attachment with confiscation or recovered property.",
        "Do not treat UAPA Section 51A listing action as a conviction.",
        "Do not merge AML, CFT and proliferation financing into one legal route.",
        "Do not describe FATF as an investigative or adjudicatory agency.",
        "Do not confuse grey/black listing with Mutual Evaluation follow-up.",
        "Do not turn regular follow-up or technical compliance into an unqualified effectiveness outcome.",
    ]
    titles = [
        "Terror financing and money laundering distinction",
        "Predicate offence and proceeds of crime",
        "Placement layering and integration typology",
        "Trade-Based Money Laundering boundary",
        "Clean-clean and dirty-clean detection problem",
        "Customer due diligence beneficial ownership and STRs",
        "FIU-IND financial-intelligence function",
        "ED investigation and provisional attachment",
        "Adjudicating Authority Special Court and confiscation",
        "UAPA Section 51A and terror-finance sanctions",
        "UN listing delisting and due-process safeguards",
        "WMD proliferation-financing limb",
        "FATF standards Mutual Evaluation and effectiveness",
        "Grey list black list and follow-up categories",
        "India MER 2024 and implementation-outcome verdict",
    ]
    routes = [
        "Define purpose and source of funds before selecting the legal route.",
        "Name the underlying scheduled offence, proceeds and registration status.",
        "Use the three stages only as a conceptual diagnostic sequence.",
        "Explain trade-value disguise without operational concealment detail.",
        "Show why lawful origin does not remove terror-purpose risk.",
        "Separate preventive control, intelligence flag and criminal finding.",
        "Keep receipt, analysis and dissemination distinct from investigation.",
        "State PMLA gateway, investigative power and provisional status.",
        "Trace property and case status through every adjudicatory rung.",
        "Distinguish terror offences and listing-linked freezing from PMLA.",
        "Pair preventive sanctions with review, delisting and identity safeguards.",
        "Keep proliferation financing analytically separate from AML and CFT.",
        "Evaluate technical compliance and effectiveness as separate dimensions.",
        "Identify whether the question concerns listing or reporting follow-up.",
        "Balance recognised strengths with named prosecution and outreach gaps.",
    ]
    panels = [
        common.panel("Finance-purpose matrix", "comparison-table", [
            "MONEY LAUNDERING -> DISGUISE PROCEEDS OF CRIME",
            "TERROR FINANCING -> PROVIDE / MOVE VALUE FOR TERROR PURPOSE",
            "FUNDS -> MAY BE LAWFUL OR UNLAWFUL IN ORIGIN",
            "RULE -> purpose, source and legal route must all be named",
        ], ["Terror-finance laundering distinction", "Clean-clean dirty-clean distinction"]),
        common.panel("Predicate-proceeds gateway", "process-flow", [
            "SCHEDULED PREDICATE OFFENCE REGISTERED",
            "-> PROCEEDS OF CRIME IDENTIFIED",
            "-> PMLA INVESTIGATION",
            "-> PROSECUTION / ADJUDICATION",
            "TRAP -> unexplained wealth alone is not the complete gateway",
        ], ["Predicate-offence gateway"]),
        common.panel("Laundering-stage typology", "timeline", [
            "PLACEMENT -> VALUE ENTERS A CHANNEL",
            "LAYERING -> DISTANCE FROM CRIMINAL ORIGIN",
            "INTEGRATION -> APPARENTLY LEGITIMATE RETURN",
            "SAFE RULE -> conceptual diagnosis, never evasion instruction",
        ], ["Placement typology", "Layering typology", "Integration typology"]),
        common.panel("Channel distinction map", "comparison-table", [
            "TBML -> TRADE VALUE / DOCUMENT MANIPULATION",
            "BANKING CHANNEL -> REPORTING / TRANSACTION CONTROLS",
            "VIRTUAL ASSET -> SEPARATE TECHNOLOGY / REPORTING RISK",
            "TERROR DIVERSION -> MAY START WITH LAWFUL FUNDS",
        ], ["TBML boundary", "Clean-clean dirty-clean distinction"]),
        common.panel("Preventive-control chain", "process-flow", [
            "CDD / KYC -> BENEFICIAL OWNER",
            "-> RECORDS / TRANSACTION MONITORING",
            "-> SUSPICIOUS TRANSACTION REPORT",
            "-> FIU-IND ANALYSIS / DISSEMINATION",
            "NOT PROVED -> crime or guilt",
        ], ["Reporting-entity controls", "FIU-IND mandate"]),
        common.panel("PMLA institution ladder", "institution-map", [
            "PREDICATE AGENCY -> UNDERLYING OFFENCE",
            "FIU-IND -> FINANCIAL INTELLIGENCE",
            "ED -> PMLA INVESTIGATION / PROVISIONAL ATTACHMENT",
            "ADJUDICATING AUTHORITY -> CONFIRM / RELEASE",
            "SPECIAL COURT -> TRIAL / LEGAL OUTCOME",
        ], ["FIU-IND mandate", "ED mandate", "PMLA property ladder"]),
        common.panel("Property-status firewall", "status-ladder", [
            "TRACE / IDENTIFY",
            "-> PROVISIONAL ATTACHMENT",
            "-> CONFIRMATION OR RELEASE",
            "-> CONVICTION OR ACQUITTAL",
            "-> CONFISCATION ONLY ON THE LEGALLY REQUIRED OUTCOME",
        ], ["PMLA property ladder", "Investigation-prosecution boundary"]),
        common.panel("Terror-sanctions route", "decision-tree", [
            "TERROR-FUND OFFENCE? -> UAPA INVESTIGATION / TRIAL",
            "LISTED PERSON / ENTITY? -> SECTION 51A TARGETED ACTION",
            "UN 1267 LINK -> DOMESTIC IMPLEMENTATION",
            "SAFEGUARD -> REVIEW / DELISTING / IDENTITY ACCURACY",
        ], ["UAPA terror-finance route", "Sanctions-listing boundary"]),
        common.panel("Three-finance-limbs", "comparison-table", [
            "AML -> PROCEEDS OF CRIME",
            "CFT -> FUNDS FOR TERROR PURPOSE",
            "PF -> PROHIBITED WMD-RELATED FINANCING",
            "COMMON NEED -> risk controls + intelligence + lawful adjudication",
        ], ["Terror-finance laundering distinction", "Proliferation-finance limb"]),
        common.panel("FATF assessment architecture", "systems-map", [
            "FATF RECOMMENDATIONS -> INTERNATIONAL STANDARDS",
            "MUTUAL EVALUATION -> TECHNICAL COMPLIANCE + EFFECTIVENESS",
            "FOLLOW-UP -> POST-EVALUATION REPORTING",
            "LISTING -> INCREASED MONITORING / CALL FOR ACTION",
        ], ["FATF standards role", "Mutual Evaluation", "Listing-follow-up firewall"]),
        common.panel("India 2024 balanced scorecard", "matrix", [
            "STRENGTH -> RISK UNDERSTANDING / FINANCIAL INTELLIGENCE",
            "STRENGTH -> BENEFICIAL OWNERSHIP / ASSET RECOVERY",
            "GAP -> COMPLETE ML / TF TRIALS + APPROPRIATE SANCTIONS",
            "GAP -> RISK-BASED NON-PROFIT OUTREACH",
            "STATUS -> REGULAR FOLLOW-UP; REPORT BACK IN THREE YEARS",
        ], ["India MER 2024"]),
        common.panel("PYQ and effectiveness rail", "answer-spine", [
            "2021 -> TECHNOLOGY / GLOBALISATION + MATCHED CONTROLS",
            "2023 -> FUNDING SOURCES + FATF COMPLIANCE EFFORTS",
            "2018 -> CROSS-OWNED DRUG / LAUNDERING LINK",
            "END -> PREVENT / DETECT / DISRUPT / PROSECUTE / ADJUDICATE",
            "QUALIFY -> attachment, listing and compliance are not conviction",
        ], ["Compliance-outcome end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2021", "GS-III",
            "How emerging technologies and globalisation contribute to money laundering and the national and international measures to tackle it.",
            "Routed to this owner; Discuss · 10 marks · 150 words.",
            [0, 1, 5, 7, 8, 9, 11, 15, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2023", "GS-III",
            "Major sources of terror funding in India and efforts to curb them in light of FATF compliance.",
            "Printed stem verified in the routing ledger; Discuss · 15 marks · 250 words.",
            [0, 1, 6, 7, 8, 9, 12, 13, 15, 16, 17, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2018", "GS-III",
            "Drug-trafficking linkages with money laundering and human trafficking.",
            "Conservative cross-owned component card routed principally to Topic 11; Explain · 15 marks · 250 words. This solution covers only the laundering and proceeds-status leg.",
            [0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 19],
        ),
    ]
    return common.topic(
        10, "Terror Financing, Money Laundering and FATF",
        "10_Terror-Financing-Money-Laundering-and-FATF", facts, traps,
        [
            (10, "Distinguish terror financing from money laundering and explain why lawful-origin funds may still create CFT risk.", [0, 1, 6, 12, 19]),
            (10, "Explain placement, layering and integration as a conceptual typology without turning the answer into evasion guidance.", [2, 3, 4, 5, 7]),
            (15, "Discuss how technology and globalisation alter money-laundering risk and evaluate matched national and international controls.", [1, 5, 7, 8, 9, 11, 15, 16, 19]),
            (15, "Assess India's terror-finance architecture across UAPA Section 51A, PMLA, FIU-IND, ED and targeted financial sanctions.", [0, 1, 8, 9, 10, 11, 12, 13, 19]),
            (20, "Critically evaluate India's 2024 FATF Mutual Evaluation outcome by separating technical compliance, disruption and adjudicated effectiveness.", [7, 10, 11, 15, 16, 17, 18, 19]),
            (20, "Examine the proposition that India's AML/CFT bottleneck lies in converting financial intelligence and provisional action into timely fair prosecution and confiscation.", [1, 7, 8, 9, 10, 11, 16, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Placement", "Layering", "Integration",
            "Trade-Based Money Laundering", "PMLA",
            "predicate", "proceeds of crime", "FIU-IND",
            "Enforcement Directorate", "Adjudicating Authority",
            "Special Court", "Section 51A", "FATF",
            "Mutual Evaluation", "regular follow-up", "grey list",
            "black list", "beneficial ownership", "19 September 2024",
            "2027",
        ],
        "The routed ledger provides direct 2021 and 2023 GS-III demands. The third conservative card is the 2018 drug-trafficking linkage question, explicitly marked as cross-owned with Topic 11 and limited here to its money-laundering and proceeds-status component.",
        pyqs, LIVE_ATTEMPTS,
        "On 2026-09-04 FATF's official India page confirmed the 19 September 2024 regular-follow-up outcome and balanced recommendations, FIU-IND reproduced the PMLA records framework, and RBI's KYC Master Direction showed an update through 14 August 2025. No STR, attachment, prosecution, conviction, confiscation or compliance-rate statistic is used.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "TERROR-FINANCE, PROCEEDS AND LAUNDERING-STAGE THREAT GRAMMAR",
            "PMLA, UAPA, FIU-IND, ED AND PROPERTY-STATUS FIREWALLS",
            "FATF MUTUAL EVALUATION AND THREE CONSERVATIVE PYQ SPINES",
            "TECHNICAL COMPLIANCE, PROSECUTION AND ADJUDICATED EFFECTIVENESS",
        ),
        register_answer_spine=[
            "DISTINGUISH FUNDING PURPOSE FROM CRIMINAL ORIGIN",
            "NAME THE PREDICATE OFFENCE AND PROCEEDS OF CRIME",
            "USE PLACEMENT LAYERING INTEGRATION ONLY AS TYPOLOGY",
            "MATCH CDD BENEFICIAL OWNERSHIP STR AND FIU ANALYSIS",
            "TRACE ED ATTACHMENT AUTHORITY CONFIRMATION COURT AND CONFISCATION",
            "KEEP UAPA SECTION 51A LISTING DISTINCT FROM PMLA",
            "SEPARATE FATF LISTING MUTUAL EVALUATION AND FOLLOW-UP",
            "CONCLUDE WITH FAIR TRIAL SANCTION CONFISCATION REVIEW AND RIGHTS",
        ],
    )


TOPIC_10 = _build()
