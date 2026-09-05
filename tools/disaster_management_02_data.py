"""Authored learner-v2 data for Disaster Management Topic 02."""

from __future__ import annotations

import generate_disaster_management_common as common


LIVE_ATTEMPTS = [
    (
        "https://www.indiacode.nic.in/indiacode/bitstream/123456789/2045/1/A200553.pdf "
        "— attempted 2026-09-04; the India Code PDF returned HTTP 403 to the "
        "fetcher. The module therefore relies on the consolidated provisions "
        "already audited into the Basic and Advanced owners and does not infer "
        "a notification or implementation outcome."
    ),
    (
        "https://www.mha.gov.in/MHA1/Par2017/pdfs/par2025-pdfs/LS22072025/284.pdf "
        "— attempted 2026-09-04; the official parliamentary PDF returned HTTP "
        "403, while official search metadata confirmed the amendment's "
        "commencement and the reported 16 operational NDRF battalions. No "
        "deployment success claim was imported."
    ),
    (
        "https://nidm.gov.in/about.asp — fetched 2026-09-04; NIDM's official "
        "page confirms its statutory capacity-development, training, research, "
        "documentation and policy-advocacy responsibilities."
    ),
    (
        "https://ndrf.gov.in/en/about-us — fetched 2026-09-04; the official "
        "force page confirms the DM Act basis and expansion to 16 battalions. "
        "Operational narratives were not converted into comparative outcomes."
    ),
]


def _build() -> dict[str, object]:
    facts = [
        ("DM Act foundation", "The Disaster Management Act, 2005 establishes national, state and district authorities and assigns prevention, mitigation, preparedness, response and recovery functions."),
        ("Current amendment status", "The Disaster Management (Amendment) Act, 2025 received assent on 29 March 2025 and came into force on 9 April 2025; the current position is not the unamended 2005 text."),
        ("NDMA", "NDMA is the Prime Minister-chaired apex authority that lays down policies, plans and guidelines and exercises statutory functions under the Act."),
        ("NEC", "The National Executive Committee is chaired by the Union Home Secretary and coordinates, monitors and implements national disaster-management policy and plans."),
        ("SDMA", "The State Disaster Management Authority is chaired by the Chief Minister and lays down state policy and approves the State Plan."),
        ("SEC", "The State Executive Committee is chaired by the Chief Secretary and coordinates and monitors state-level implementation."),
        ("DDMA", "The District Disaster Management Authority is chaired by the District Collector or Magistrate, with the elected local-authority representative as Co-Chairperson, and prepares the District Plan."),
        ("Local authorities", "Panchayats, municipalities and other local authorities perform assigned preparedness, mitigation, response and recovery functions closest to the affected population."),
        ("NDRF force", "The National Disaster Response Force is a specialist response force under the Act; official NDRF material states that it has expanded to 16 battalions."),
        ("NDRF fund", "The National Disaster Response Fund under section 46 finances eligible response and relief needs and is institutionally distinct from the identically abbreviated response force."),
        ("NIDM", "NIDM is the statutory nodal institute for human-resource development, capacity building, training, research, documentation and policy advocacy."),
        ("NCMC and HLC", "Sections 8A and 8B inserted in 2025 give statutory status to the National Crisis Management Committee and High Level Committee."),
        ("Urban authority", "Section 41A enables a State Government to constitute an Urban Disaster Management Authority by notification; the statutory permission does not prove constitution in every eligible city."),
        ("State response force", "Section 44A enables a State Government to constitute a specialist State Disaster Response Force; this force must not be confused with the SDRF fund."),
        ("Plan responsibility", "The amended architecture assigns National and State Plan preparation to NDMA and SDMA, while executive committees retain implementation and monitoring roles."),
        ("Plan hierarchy", "The revised National Disaster Management Plan, 2019 is the latest published national plan and must be distinguished from the first 2016 edition."),
        ("Fund architecture", "Sections 46, 47 and 48 contemplate national, state and district response and mitigation funds; statutory provision does not establish that every district fund is operational."),
        ("Finance coordination", "Finance Commission awards and Central-State assistance shape disaster financing, but allocation, release, expenditure and verified outcome are separate evidence rungs."),
        ("Federal cascade", "The NDMA-SDMA-DDMA-local cascade distributes policy, coordination and implementation across federal levels; an apex guideline does not itself prove local capacity."),
        ("Mandate-outcome firewall", "A statute, authority, plan, force, fund, notification or database mandate proves its legal or institutional rung only; operational readiness and disaster outcomes require separate evidence."),
    ]
    traps = [
        "Do not present the original 2005 Act as the complete current law.",
        "Do not confuse NDMA policy functions with NEC coordination functions.",
        "Do not merge NDRF-the-force with NDRF-the-fund.",
        "Do not merge State Disaster Response Force with State Disaster Response Fund.",
        "Do not treat an enabling provision as proof of universal implementation.",
        "Do not call NIDM an operational response force.",
        "Do not describe DDMA as merely advisory.",
        "Do not infer district-fund constitution from section 48 alone.",
        "Do not treat a national plan as proof of district capability.",
        "Do not equate allocation or deployment with a verified outcome.",
    ]
    titles = [
        "DM Act and amendment chronology",
        "NDMA policy and plan authority",
        "NEC coordination and implementation",
        "SDMA and State policy",
        "SEC implementation layer",
        "DDMA and district operational planning",
        "Local authorities and subsidiarity",
        "NDRF force architecture",
        "NDRF force versus fund",
        "NIDM capacity-building mandate",
        "NCMC and High Level Committee",
        "Urban authority and State response force",
        "National State and District plans",
        "Response and mitigation funds",
        "Federal coordination and mandate-outcome proof",
    ]
    routes = [
        "Open with the current amended statute and date.",
        "Attribute policy and plan functions to the correct apex authority.",
        "Separate coordination and monitoring from policy approval.",
        "Show how the State tier adapts national direction.",
        "Locate implementation monitoring at the executive-committee layer.",
        "Test district staffing, plans, finance and local linkages.",
        "Name PRIs and ULBs rather than writing government generically.",
        "Describe specialist response capacity without operational speculation.",
        "Use force or fund only after expanding the acronym.",
        "Link training and research to capacity rather than field command.",
        "Explain statutory status without displacing the ordinary cascade.",
        "State that may constitute is enabling, not automatic.",
        "Distinguish plan preparation, approval, implementation and review.",
        "Separate response finance from mitigation finance.",
        "Conclude with the weakest-tier and evidence-rung tests.",
    ]
    panels = [
        common.panel("Statutory chronology", "timeline", [
            "2005 -> DISASTER MANAGEMENT ACT",
            "2009 -> NATIONAL POLICY",
            "2016 -> FIRST NDMP | 2019 -> REVISED NDMP",
            "2025 -> AMENDMENT | IN FORCE 9 APRIL 2025",
        ], ["DM Act foundation", "Current amendment status", "Plan hierarchy"]),
        common.panel("National tier", "institution-map", [
            "NDMA -> policy, plans, guidelines",
            "NEC -> coordination, monitoring, implementation",
            "NCMC -> major disasters with national ramifications",
            "HLC -> statutory financial-assistance role",
        ], ["NDMA", "NEC", "NCMC and HLC"]),
        common.panel("State tier", "institution-map", [
            "SDMA -> state policy and State Plan",
            "SEC -> coordination and monitoring",
            "STATE DEPARTMENTS -> hazard and sector functions",
            "STATE FORCE / FUND -> distinct instruments",
        ], ["SDMA", "SEC", "State response force"]),
        common.panel("District-local cascade", "hierarchy", [
            "DDMA -> District Plan and coordination",
            "COLLECTOR / MAGISTRATE -> Chair",
            "ELECTED LOCAL REPRESENTATIVE -> Co-Chair",
            "PRI / ULB -> last-mile implementation",
        ], ["DDMA", "Local authorities"]),
        common.panel("NDRF acronym firewall", "comparison-table", [
            "FORCE -> specialist personnel and response teams",
            "FUND -> eligible response and relief expenditure",
            "STATE FORCE -> section 44A enabling power",
            "STATE FUND -> section 48 finance",
        ], ["NDRF force", "NDRF fund", "State response force"]),
        common.panel("NIDM knowledge chain", "process-flow", [
            "RESEARCH -> DOCUMENTATION -> TRAINING",
            "CAPACITY BUILDING -> POLICY ADVOCACY",
            "STATE / LOCAL SUPPORT -> CULTURE OF PREVENTION",
            "TRAP -> knowledge institute is not response command",
        ], ["NIDM"]),
        common.panel("2025 amendment map", "status-ladder", [
            "8A NCMC | 8B HLC",
            "41A URBAN AUTHORITY | 44A STATE FORCE",
            "PLAN RESPONSIBILITY + DATABASE DUTIES",
            "ENACTMENT -> NOTIFICATION -> IMPLEMENTATION -> OUTCOME",
        ], ["Current amendment status", "NCMC and HLC", "Urban authority", "State response force"]),
        common.panel("Plan responsibility matrix", "matrix", [
            "NATIONAL PLAN -> NDMA preparation / approval architecture",
            "STATE PLAN -> SDMA preparation / approval architecture",
            "DISTRICT PLAN -> DDMA",
            "EXECUTIVE COMMITTEES -> implementation and monitoring",
        ], ["Plan responsibility", "Plan hierarchy"]),
        common.panel("Fund architecture", "hierarchy", [
            "NATIONAL -> response s46 | mitigation s47",
            "STATE -> response | mitigation",
            "DISTRICT -> response | mitigation",
            "RULE -> statutory design is not constitution or expenditure proof",
        ], ["Fund architecture", "Finance coordination"]),
        common.panel("Federal operating chain", "process-flow", [
            "NATIONAL GUIDANCE -> STATE ADAPTATION",
            "DISTRICT PLAN -> LOCAL EXECUTION",
            "FEEDBACK / DATA -> PLAN REVISION",
            "BOTTLENECK -> weakest implementation tier",
        ], ["Federal cascade"]),
        common.panel("Evidence-rung ladder", "status-ladder", [
            "ACT -> RULE / NOTIFICATION -> AUTHORITY / PLAN",
            "ALLOCATION -> RELEASE -> EXPENDITURE",
            "DEPLOYMENT -> SERVICE DELIVERY -> VERIFIED OUTCOME",
            "NO AUTOMATIC JUMP BETWEEN RUNGS",
        ], ["Finance coordination", "Mandate-outcome firewall"]),
        common.panel("Institutional answer spine", "answer-spine", [
            "CITE CURRENT LAW -> NAME TIER -> STATE MANDATE",
            "MAP PLAN + FORCE / FUND + LOCAL IMPLEMENTER",
            "IDENTIFY COORDINATION OR CAPACITY GAP",
            "QUALIFY ENABLING POWER AND OUTCOME CLAIM",
        ], ["Federal cascade", "Mandate-outcome firewall"]),
    ]
    pyqs = [
        common.make_pyq_solution(facts, "2020", "GS-III",
            "Discuss how the Government's proactive disaster-management approach replaced the earlier reactive strategy.",
            "Verified direct routing: Discuss · 15 marks · 250 words.",
            [0, 2, 3, 4, 5, 10, 15, 18]),
        common.make_pyq_solution(facts, "2020", "GS-II",
            "Elucidate centralising tendencies through disaster-management legislation and other contemporary legislation.",
            "Verified cross-cutting routing: Elucidate · 15 marks · 250 words; this card addresses only the disaster-law and federal-balance limb.",
            [0, 2, 3, 4, 6, 18, 19]),
        common.make_pyq_solution(facts, "2024", "GS-III",
            "Discuss policies and frameworks for tackling urban flooding.",
            "Conservative cross-topic application of the verified 2024 Q18 demand; primary ownership remains Topic 08.",
            [6, 7, 12, 15, 16, 18, 19]),
    ]
    return common.topic(
        2, "Indian Legal and Institutional Architecture",
        "02_Indian-Legal-and-Institutional-Architecture", facts, traps,
        [
            (10, "Distinguish NDMA, NEC, SDMA, SEC and DDMA by composition and mandate.", [2, 3, 4, 5, 6]),
            (10, "Differentiate NDRF-the-force from disaster-response and mitigation funds.", [8, 9, 13, 16]),
            (15, "Explain the significance and limits of the Disaster Management (Amendment) Act, 2025.", [1, 11, 12, 13, 14, 19]),
            (15, "Analyse district and local capacity as the weak link in India's disaster-management cascade.", [6, 7, 10, 18, 19]),
            (20, "Evaluate India's legal, planning and financial architecture for proactive disaster risk reduction.", [0, 2, 3, 4, 5, 15, 16, 17, 18]),
            (20, "Examine federal coordination in disaster management while separating statutory mandate from operational outcome.", [1, 2, 3, 4, 5, 6, 7, 17, 18, 19]),
        ],
        titles, routes, panels,
        [
            "Disaster Management Act, 2005", "NDMA", "NEC", "SDMA",
            "SEC", "DDMA", "NIDM", "NDRF", "National Disaster Management Plan",
            "National Crisis Management Committee", "High Level Committee",
            "Urban Disaster Management Authority", "State Disaster Response Force",
            "s. 46", "s. 47", "s. 48",
        ],
        "The 2020 GS-III card is directly routed. The 2020 GS-II card is explicitly cross-cutting. The 2024 urban-flood card is an institutional application and does not displace Topic 08 ownership.",
        pyqs, LIVE_ATTEMPTS,
        "India Code and MHA parliamentary material are the current legal-status anchors; NIDM and NDRF official pages verify their institutional roles. Blocked PDFs are recorded honestly, and no enabling provision is treated as completed rollout.",
        extra=["00_Master-Framework.md", "README.md", "OFFICIAL-UPSC-SYLLABUS-MAPPING.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "CURRENT STATUTE AND THREE-TIER AUTHORITY MAP",
            "FORCE, FUND, PLAN AND ENABLING-POWER FIREWALLS",
            "FEDERAL COORDINATION AND CAPACITY ANSWER SPINE",
            "CURRENT AMENDMENT AND IMPLEMENTATION-EVIDENCE BOUNDARY",
        ),
        register_answer_spine=[
            "CITE THE 2005 ACT AS AMENDED IN 2025",
            "MAP NDMA NEC SDMA SEC DDMA AND LOCAL AUTHORITIES",
            "DISTINGUISH NDRF FORCE FUND AND STATE FORCE FUND",
            "LOCATE NIDM AS CAPACITY BUILDING",
            "STATE PLAN PREPARATION IMPLEMENTATION AND REVIEW ROLES",
            "TEST DISTRICT FINANCE STAFF AND LOCAL CAPACITY",
            "CONCLUDE WITHOUT TURNING MANDATE INTO OUTCOME",
        ],
    )


TOPIC_02 = _build()
