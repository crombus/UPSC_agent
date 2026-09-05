"""Authored learner-v2 data for Internal Security Topic 11."""

from __future__ import annotations

import generate_internal_security_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.mha.gov.in/en/commoncontent/narco-coordination-centre-"
        "ncord — attempted 2026-09-04 for the current NCORD architecture; "
        "direct retrieval returned 403. The four-tier mechanism and State/UT "
        "roles are retained only from the audited owner, with no meeting, "
        "seizure, hotspot or outcome count."
    ),
    (
        "https://narcoticsindia.nic.in/ and https://www.mha.gov.in/ — fetched "
        "and attempted 2026-09-04. The official NCB portal was reachable but "
        "its returned page mainly described controlled substances and health "
        "effects, while MHA retrieval was blocked; no current mandate expansion "
        "or performance statistic is inferred from the page."
    ),
    (
        "https://www.indiacode.nic.in/ — attempted 2026-09-04 for the NDPS "
        "Act, 1985, BNS Sections 111-112 and 143-144, Arms Act and other "
        "relevant provisions; direct retrieval returned 403. Only owner-audited "
        "statutory categories are used, and a statutory offence is not treated "
        "as evidence of prevalence or enforcement outcome."
    ),
    (
        "https://www.unodc.org/unodc/en/organized-crime/intro/UNTOC.html, "
        "https://www.unodc.org/unodc/en/human-trafficking/protocol.html and "
        "https://www.pib.gov.in/ — fetched and attempted 2026-09-04. UNODC "
        "confirmed UNTOC's cooperation framework and the Trafficking Protocol's "
        "victim-identification purpose; PIB retrieval returned 403. International "
        "definitions are used only within those bounded propositions."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("Organised-crime definition", "Organised crime is continuing coordinated serious criminal activity by a group or syndicate for financial or material benefit; legal definitions differ in detail, so the relevant BNS, special-law or UNTOC test must be named."),
        ("Syndicate-network distinction", "A syndicate implies continuing organised association, while a network may be looser and task-based; hierarchy is not required for every criminal network, but continuity, coordination and benefit distinguish organised enterprise from an isolated offence."),
        ("Crime-terror ends boundary", "Organised crime primarily seeks profit and a parallel illicit economy, whereas terrorism seeks political or ideological coercion; they can share routes, protection, weapons, finance and facilitators without becoming identical."),
        ("Narco-terrorism definition", "Narco-terrorism is the financing or enabling intersection between narcotics trafficking and terrorist or insurgent activity; it is not a synonym for drug consumption, addiction or every NDPS case."),
        ("Regional-model variation", "The owner distinguishes extortion and parallel-economy patterns, externally supported or diaspora-linked patterns, and route-based trafficking networks; countermeasures must follow the specific money and protection model rather than assume national uniformity."),
        ("Route-geography boundary", "Golden Crescent and Golden Triangle references identify broad source and transit exposure relevant to India; they do not establish a particular consignment's origin, route, group or sponsor."),
        ("Non-operational supply chain", "At a safe conceptual level, illicit narcotics markets connect source, transit, wholesale or retail distribution, proceeds and laundering; analysis should target governance, finance and logistics without publishing routes, concealment or evasion methods."),
        ("NDPS framework", "The NDPS Act, 1985 regulates narcotic drugs and psychotropic substances, grades offences by statutory quantity categories and provides a separate property-forfeiture framework in Chapter VA; seizure is not conviction or forfeiture."),
        ("NCB mandate", "The Narcotics Control Bureau is the central nodal drug-law-enforcement and coordination agency under MHA, constituted under Section 4(3) of the NDPS Act; State police and other empowered agencies retain their own jurisdiction."),
        ("NCORD architecture", "National Narcotics Coordination uses Apex, Executive, State and District tiers to connect policy and enforcement actors; a coordination meeting or mechanism is an input, not proof of reduced trafficking."),
        ("ANTF role", "State and Union Territory Anti-Narcotics Task Forces support local coordination, hotspot and network analysis and financial investigation; they do not displace State police, NCB, customs, border or maritime mandates."),
        ("Follow-the-property route", "NDPS Chapter VA forfeiture and PMLA attachment where an NDPS offence is a scheduled predicate require parallel financial investigation; intercepted drugs and traced proceeds occupy different evidentiary chains."),
        ("BNS organised-crime offences", "BNS Sections 111 and 112 create general-law offences of organised crime and petty organised crime from 1 July 2024; State special laws may still raise separate forum, procedure and evidence questions."),
        ("Trafficking definition", "Human trafficking concerns acts such as recruitment, transport, harbouring or receipt through coercive, deceptive or abusive means for exploitation, with child cases receiving special treatment under the applicable legal definition."),
        ("Trafficking-smuggling boundary", "Trafficking centres on exploitation and need not cross a border, whereas migrant smuggling centres on facilitating irregular entry for financial or material benefit; a smuggled migrant may later become a trafficking victim, but the offences remain distinct."),
        ("Victim-centred response", "Article 23, BNS Sections 143-144, Anti-Human Trafficking Units and welfare systems require identification, safety, legal aid, non-punishment where applicable, rehabilitation and reintegration alongside network investigation."),
        ("Illicit-market convergence", "Arms, wildlife, counterfeit currency, narcotics and human exploitation can share corrupt protection, transport, document, financial and laundering services; convergence must be proved case by case and not assumed from one seized commodity."),
        ("UNTOC-INTERPOL cooperation", "UNTOC supports criminalisation and cooperation through extradition, mutual legal assistance and law-enforcement channels, while INTERPOL notices facilitate specified information or asset-tracing purposes; neither instrument supplies a conviction or universal arrest warrant."),
        ("Evidence-status firewall", "Intelligence, complaint, interception, seizure, arrest, charge-sheet, attachment, trial, conviction, forfeiture and victim recovery are distinct rungs; no single enforcement output proves dismantling of the wider network."),
        ("Integrated-network end-state", "Effective response follows network, money, logistics and corrupt protection while combining lawful enforcement, border and port coordination, digital and financial forensics, international cooperation, witness protection and survivor-centred rehabilitation."),
    ]
    traps = [
        "Do not define every repeated offence as organised crime without the legal continuity and group test.",
        "Do not assume every criminal network is a rigid hierarchy.",
        "Do not use organised crime and terrorism as synonyms.",
        "Do not label every narcotics case narco-terrorism.",
        "Do not infer a consignment's route or sponsor from Golden Crescent or Golden Triangle geography.",
        "Do not publish supply routes, concealment methods or enforcement vulnerabilities.",
        "Do not confuse NCB, NCORD, ANTF and State police roles.",
        "Do not equate seizure or destruction with conviction, forfeiture or prevalence reduction.",
        "Do not treat trafficking and migrant smuggling as the same offence.",
        "Do not criminalise or stigmatise trafficked persons as network members without evidence.",
        "Do not assume arms, wildlife, FICN and narcotics convergence in every case.",
        "Do not treat an INTERPOL notice as a conviction or automatic international arrest warrant.",
    ]
    titles = [
        "Organised crime syndicate and network",
        "Profit objective versus terrorist coercion",
        "Narco-terrorism definition and nexus",
        "Regional financing and protection models",
        "Golden Crescent Golden Triangle and route caution",
        "Safe narcotics supply-chain analysis",
        "NDPS offences quantity and property framework",
        "NCB State police customs and empowered agencies",
        "NCORD four-tier coordination",
        "ANTF and parallel financial investigation",
        "BNS Sections 111-112 and State special laws",
        "Human trafficking acts means and exploitation",
        "Trafficking versus migrant smuggling",
        "Arms wildlife FICN and illicit-market convergence",
        "UNTOC INTERPOL evidence and victim-centred end-state",
    ]
    routes = [
        "Apply the relevant continuity, group and benefit elements before the label.",
        "Separate primary end-state from shared criminal means.",
        "Prove the drug-finance-terror connection rather than assume it.",
        "Match the intervention to the regional source, protection and money model.",
        "Use route geography as exposure, not case-specific attribution.",
        "Trace categories only and omit operational routes or evasion detail.",
        "Separate offence, quantity, seizure, property action and adjudication.",
        "Assign the case to the empowered institution without creating sole ownership.",
        "Evaluate information flow and handoff rather than meeting existence.",
        "Run financial investigation parallel to the commodity case.",
        "Name the applicable general or special law and procedural boundary.",
        "Identify act, means, exploitative purpose and victim status.",
        "Ask whether exploitation or paid irregular entry is the legal centre.",
        "Prove shared service, facilitator or proceeds before claiming convergence.",
        "Conclude with cooperation, evidence, witness safety and survivor recovery.",
    ]
    panels = [
        common.panel("Enterprise structure map", "comparison-table", [
            "ISOLATED OFFENCE -> one event",
            "NETWORK -> flexible task-based links",
            "SYNDICATE -> continuing organised association",
            "ORGANISED CRIME -> coordinated serious crime for material benefit",
        ], ["Organised-crime definition", "Syndicate-network distinction"]),
        common.panel("Crime-terror nexus matrix", "comparison-table", [
            "ORGANISED CRIME -> PROFIT / PARALLEL ILLICIT ECONOMY",
            "TERRORISM -> POLITICAL / IDEOLOGICAL COERCION",
            "SHARED MEANS -> ROUTES / FINANCE / ARMS / PROTECTION",
            "NARCO-TERRORISM -> proved drug-economy intersection",
        ], ["Crime-terror ends boundary", "Narco-terrorism definition"]),
        common.panel("Regional-model diagnostic", "matrix", [
            "EXTORTION MODEL -> DOMESTIC PARALLEL TAX / PROTECTION",
            "EXTERNAL MODEL -> CROSS-BORDER / DIASPORA SUPPORT",
            "ROUTE MODEL -> TRANSIT / MARKET / LOGISTICS NETWORK",
            "RULE -> intervention follows model, not a uniform slogan",
        ], ["Regional-model variation"]),
        common.panel("Route-geography firewall", "systems-map", [
            "GOLDEN CRESCENT -> BROAD WESTERN SOURCE / TRANSIT EXPOSURE",
            "GOLDEN TRIANGLE -> BROAD EASTERN SOURCE / TRANSIT EXPOSURE",
            "INDIA -> BORDER / MARITIME / MARKET VULNERABILITY",
            "NOT PROVED -> case route, actor or sponsor",
        ], ["Route-geography boundary"]),
        common.panel("Safe supply-chain map", "process-flow", [
            "SOURCE -> TRANSIT -> DISTRIBUTION",
            "-> PROCEEDS -> LAUNDERING / ASSET CONTROL",
            "RESPONSE -> intelligence + finance + lawful interdiction",
            "SAFETY -> no routes, concealment or evasion methods",
        ], ["Non-operational supply chain"]),
        common.panel("NDPS property ladder", "status-ladder", [
            "OFFENCE / QUANTITY CATEGORY",
            "-> SEIZURE + EVIDENCE",
            "-> PARALLEL FINANCIAL INVESTIGATION",
            "-> CHAPTER VA / PMLA PROPERTY PROCESS",
            "-> COURT OUTCOME / FORFEITURE WHERE ORDERED",
        ], ["NDPS framework", "Follow-the-property route"]),
        common.panel("Narcotics institution map", "institution-map", [
            "NCB -> CENTRAL NODAL COORDINATION / ENFORCEMENT",
            "NCORD -> APEX / EXECUTIVE / STATE / DISTRICT",
            "ANTF -> STATE / UT COORDINATION + FINANCIAL FOCUS",
            "POLICE / CUSTOMS / BORDER / MARITIME -> OWN MANDATES",
        ], ["NCB mandate", "NCORD architecture", "ANTF role"]),
        common.panel("Organised-crime law map", "comparison-table", [
            "BNS 111 -> ORGANISED CRIME",
            "BNS 112 -> PETTY ORGANISED CRIME",
            "STATE SPECIAL LAW -> separate forum / procedure questions",
            "RULE -> offence coverage does not prove enforcement outcome",
        ], ["BNS organised-crime offences"]),
        common.panel("Trafficking-smuggling test", "decision-tree", [
            "EXPLOITATION PURPOSE? -> TRAFFICKING ANALYSIS",
            "PAID IRREGULAR ENTRY? -> MIGRANT-SMUGGLING ANALYSIS",
            "BORDER CROSSING -> not required for trafficking",
            "VICTIM STATUS -> protect; do not presume complicity",
        ], ["Trafficking definition", "Trafficking-smuggling boundary"]),
        common.panel("Victim-centred response rail", "process-flow", [
            "IDENTIFY -> IMMEDIATE SAFETY",
            "-> LEGAL AID / EVIDENCE / WITNESS PROTECTION",
            "-> INVESTIGATE RECRUITER / FACILITATOR / PROCEEDS",
            "-> REHABILITATE / REINTEGRATE / PREVENT RE-TRAFFICKING",
        ], ["Victim-centred response"]),
        common.panel("Illicit-market convergence map", "hub-and-spoke", [
            "SHARED CRIMINAL-SERVICE HUB",
            "-> ARMS | WILDLIFE | FICN | NARCOTICS | EXPLOITATION",
            "SHARED SERVICES -> documents / corruption / finance / transport",
            "RULE -> prove the shared link case by case",
        ], ["Illicit-market convergence"]),
        common.panel("PYQ and network-outcome rail", "answer-spine", [
            "2018 -> DRUG / LAUNDERING / HUMAN-TRAFFICKING LINK",
            "2022 -> NATIONAL + TRANSNATIONAL CRIME-TERROR NEXUS",
            "2024 -> NARCO-TERROR THREAT + COUNTERMEASURES",
            "END -> NETWORK / MONEY / LOGISTICS / PROTECTION / VICTIM",
            "QUALIFY -> seizure, notice and arrest are not dismantling",
        ], ["UNTOC-INTERPOL cooperation", "Evidence-status firewall", "Integrated-network end-state"]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018", "GS-III",
            "Drug-trafficking linkages with money laundering and human trafficking and measures to address them.",
            "Routed to this owner; Explain · 15 marks · 250 words.",
            [2, 3, 6, 7, 8, 11, 13, 14, 15, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2022", "GS-III",
            "Types of organised crime and linkages between terrorists and organised crime at national and transnational levels.",
            "Routed to this owner; Discuss · 10 marks · 150 words.",
            [0, 1, 2, 3, 4, 11, 12, 16, 17, 18, 19],
        ),
        common.make_pyq_solution(
            facts, "2024", "GS-III",
            "How narco-terrorism has emerged as a serious threat across the country and suitable countermeasures.",
            "Printed stem is routed to this owner; Explain and suggest · 10 marks · 150 words.",
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19],
        ),
    ]
    return common.topic(
        11, "Organised Crime, Narco-Terrorism and Trafficking",
        "11_Organised-Crime-Narco-Terrorism-and-Trafficking", facts, traps,
        [
            (10, "Distinguish organised crime, criminal networks and terrorism while explaining their possible nexus.", [0, 1, 2, 3, 18]),
            (10, "Explain why narco-terrorism must be proved as a financing or enabling nexus rather than inferred from every drug case.", [2, 3, 4, 5, 18]),
            (15, "Analyse drug-trafficking linkages with money laundering and human trafficking through a route-money-victim framework.", [3, 6, 7, 11, 13, 14, 15, 18, 19]),
            (15, "Assess India's narcotics-control architecture across NDPS, NCB, NCORD, ANTF, State police and financial investigation.", [7, 8, 9, 10, 11, 18, 19]),
            (20, "Critically examine organised-crime and terrorism linkages at national and transnational levels, including arms, wildlife and other illicit-market convergence.", [0, 1, 2, 3, 12, 16, 17, 18, 19]),
            (20, "Design a victim-centred and rights-compatible strategy against human trafficking that preserves the trafficking-smuggling distinction and follows the wider criminal network.", [13, 14, 15, 16, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "organised crime", "syndicate", "narco-terrorism",
            "Golden Crescent", "Golden Triangle", "NDPS Act",
            "Chapter VA", "Section 4(3)", "NCB", "NCORD",
            "Anti-Narcotics Task Force", "Section 111",
            "Section 112", "Article 23", "Sections 143-144",
            "Anti-Human Trafficking Units", "UNTOC",
            "smuggling of migrants", "INTERPOL", "Silver",
        ],
        "The three direct Mains routes are used: the 2018 drug-laundering-human-trafficking linkage, 2022 national/transnational organised-crime-terrorism linkage and 2024 narco-terrorism demand. The provisional 2026 INTERPOL-notices question remains covered in the facts and required terms but is not converted into a fourth card or an inferred answer letter.",
        pyqs, LIVE_ATTEMPTS,
        "Official attempts on 2026-09-04 verified only bounded UNTOC and Trafficking Protocol propositions and the reachability of the NCB portal. MHA and India Code pages were blocked, so no current NCORD meeting, ANTF performance, seizure, conviction, forfeiture, trafficking prevalence or victim-recovery statistic is used.",
        extra=["00_Master-Framework.md", "REVISION-CHART_Threats-Responses-and-Distinctive-Features.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "ORGANISED-CRIME, SYNDICATE, NETWORK AND NARCO-TERROR GRAMMAR",
            "NDPS, NCB, NCORD, ANTF, BNS AND PROPERTY-STATUS FIREWALLS",
            "TRAFFICKING, ILLICIT-MARKET CONVERGENCE AND THREE PYQ SPINES",
            "NETWORK DISRUPTION, EVIDENCE, VICTIM PROTECTION AND RECOVERY",
        ),
        register_answer_spine=[
            "APPLY CONTINUITY GROUP COORDINATION AND BENEFIT ELEMENTS",
            "SEPARATE PROFIT END FROM POLITICAL OR IDEOLOGICAL COERCION",
            "PROVE THE DRUG-FINANCE-TERROR NEXUS",
            "USE ROUTE GEOGRAPHY WITHOUT CASE-SPECIFIC ATTRIBUTION",
            "MAP NDPS NCB NCORD ANTF STATE POLICE AND FINANCIAL ROUTES",
            "DISTINGUISH TRAFFICKING EXPLOITATION FROM MIGRANT SMUGGLING",
            "FOLLOW SHARED SERVICES PROCEEDS AND CORRUPT PROTECTION",
            "CONCLUDE WITH EVIDENCE WITNESS SAFETY VICTIM RECOVERY AND RIGHTS",
        ],
    )


TOPIC_11 = _build()
