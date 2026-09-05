"""Authored learner-v2 data for Science and Technology Topic 24."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://dst.gov.in/introduction - fetched 2026-09-04; the official "
        "DST endpoint returned only the page title through the live fetch "
        "tool. The owner's established-May-1971 and nodal-policy propositions "
        "were not independently expanded from this thin response."
    ),
    (
        "https://www.dsir.gov.in/ministry/our-organisation - attempted "
        "2026-09-04 and returned HTTP 403 through direct fetch. An official-"
        "domain search result identified CSIR as an autonomous institution "
        "under DSIR and the 37-laboratory network; the blocked page supplied "
        "no additional mandate, count or status claim."
    ),
    (
        "https://www.csir.res.in/en/about-us/about-csir - fetched 2026-09-04; "
        "substantive official text confirmed CSIR's 37 national laboratories, "
        "39 outreach centres, one Innovation Complex and three units, and its "
        "wide research spectrum. Dated personnel, patent and publication "
        "figures on the page were excluded from the learning facts."
    ),
    (
        "https://www.indiacode.nic.in/bitstream/123456789/19767/1/a2023-25.pdf "
        "- attempted 2026-09-04 and returned HTTP 403. The ANRF Act's Act 25 "
        "of 2023, commencement, sections 5, 7 and 27 remain bounded by the "
        "audited Basic and Advanced owners; the blocked response was not "
        "treated as fresh machine-readable legal proof."
    ),
    (
        "https://dst.gov.in/anusandhan-national-research-foundation-anrf and "
        "https://dst.gov.in/news/anrf-gazette-notifications - fetched "
        "2026-09-04; both official DST endpoints returned title-only content. "
        "They confirm the official surfaces exist but supplied no additional "
        "scheme, governance, funding or operational-status proposition."
    ),
    (
        "https://anrf.gov.in/ - fetched 2026-09-04; the endpoint exposed an "
        "obsolete IMPRINT-II/SERB text fragment rather than a reliable current "
        "ANRF landing-page snapshot. It was recorded as a thin response and "
        "was not used to reverse the statutory SERB-to-ANRF transition."
    ),
    (
        "https://anrf.gov.in/assets/pdf/CFP_of_MAHA_Water.pdf - fetched "
        "2026-09-04 as raw official PDF bytes; official-domain search located "
        "the 2026 ANRF-Jal Shakti MAHA Water call. Raw bytes and snippets were "
        "not converted into award, expenditure, completed-project or outcome "
        "claims."
    ),
]


def _topic_24() -> dict[str, object]:
    facts = [
        (
            "Institutional identity before abbreviation",
            "India's science architecture contains Ministries, Departments, statutory bodies, autonomous societies, offices, academies, regulators, grant programmes and research-performing laboratories. Legal form determines accountability and powers, while mandate determines function; an acronym or shared ministry does not make two bodies institutional peers.",
        ),
        (
            "DST horizontal policy role",
            "The Department of Science and Technology is a Department under the Ministry of Science and Technology, established in May 1971 to promote new areas and organise, coordinate and support science and technology activities. DST is a horizontal policy, programme and mission anchor, not India's single all-purpose laboratory network or a Ministry in its own right.",
        ),
        (
            "DSIR industrial-research role",
            "The Department of Scientific and Industrial Research is a separate Department in the Ministry of Science and Technology; it promotes industrial research, technology transfer and recognition or support mechanisms for industrial R&D and administratively holds CSIR. DSIR is not a laboratory, a generic grant council or another name for DST.",
        ),
        (
            "CSIR legal and research-performing identity",
            "The Council of Scientific and Industrial Research is an autonomous society registered under the Societies Registration Act and administratively under DSIR. Its official profile records a network of 37 national laboratories, 39 outreach centres, one Innovation Complex and three units across fields including chemicals, drugs, genomics, biotechnology, mining, aeronautics, instrumentation, environment and information technology.",
        ),
        (
            "CSIR governance and mandate boundary",
            "The Prime Minister is President of CSIR and the Union Science and Technology Minister its Vice-President, while laboratories perform research, technology development, testing, standards-related work and translation according to their mandates. High-level office-bearers do not convert CSIR into a Department, regulator or primarily grant-disbursing council.",
        ),
        (
            "ANRF statutory identity and commencement",
            "The Anusandhan National Research Foundation is a statutory apex research body created by the ANRF Act, 2023, Act 25 of 2023, enacted on 12 August 2023 and brought into force on 5 February 2024. It is designed to seed, grow and promote research and provide high-level strategic direction; DST is the administrative anchor, not a basis for calling ANRF a DST sub-office.",
        ),
        (
            "ANRF two-tier governance",
            "Section 5 places the Prime Minister as ex officio President of ANRF's Governing Board, with the Union Ministers for Science and Technology and Education as Vice-Presidents, while section 7 makes the Principal Scientific Adviser ex officio Chairperson of the Executive Council. Strategic governance, executive implementation and administrative support are therefore distinct layers.",
        ),
        (
            "SERB repeal and succession",
            "The Science and Engineering Research Board was the statutory competitive-grants body under the SERB Act, 2008; section 27 of the ANRF Act repealed that Act and dissolved SERB with transition and savings for assets, liabilities and personnel. SERB remains historically relevant in older schemes and PYQs but is not a separate continuing statutory apex identity.",
        ),
        (
            "ANRF financing-design firewall",
            "The owner records an announced ANRF design of 50,000 crore rupees over 2023-28, with about 36,000 crore expected from non-government sources including industry and philanthropy. This is a financing design and crowd-in ambition, not proof of appropriation, receipt, annual release, grant award, expenditure or research outcome.",
        ),
        (
            "Grant fellowship and mission-mode distinction",
            "A research grant funds a defined project, a fellowship principally supports a researcher, and a mission-mode programme directs multi-institutional work toward priority outcomes and milestones. Investigator-led curiosity research and directed strategic research serve different risk and time horizons; neither can substitute completely for the other.",
        ),
        (
            "Research-to-use pipeline",
            "A disciplined research pipeline separates question formulation, basic research, experimental validation, replication, applied research, prototype, testing, scale-up, standards or regulation, manufacturing, adoption and verified societal outcome. ANRF can fund or shape parts of this pipeline, while CSIR and universities can perform research, but no institutional label proves every later rung.",
        ),
        (
            "Horizontal versus vertical architecture",
            "DST, ANRF and DSIR-CSIR provide horizontal policy, funding or research capability across sectors, while vertical institutions execute domain mandates. Horizontal bodies multiply capacity but do not replace specialist mission agencies; a vertical mission cannot by itself substitute for broad universities, labs, grants, skills and standards.",
        ),
        (
            "Sectoral mission and agency boundaries",
            "ISRO is an organisation under the Department of Space; DAE and DBT are Departments; DRDO operates under the Ministry of Defence; MeitY is a Ministry; ICMR is under the Ministry of Health and Family Welfare; ICAR is under DARE; and PRIP belongs to the Department of Pharmaceuticals. These bodies may collaborate with DST, ANRF or CSIR without moving into one common legal category.",
        ),
        (
            "University laboratory industry ecosystem",
            "A research ecosystem links universities, national laboratories, mission agencies, startups, industry, standards bodies, funders and skilled people. Funding volume alone cannot repair weak proposal support, laboratory access, peer review, procurement, research administration, mentorship, interdisciplinary coordination or absorption by firms and public systems.",
        ),
        (
            "Named CSIR laboratory function map",
            "CSIR-NPL anchors metrology and measurement science, CSIR-NCL chemistry, CSIR-CCMB cellular and molecular biology, CSIR-IGIB genomics and integrative biology, CSIR-CEERI electronics and CSIR-CECRI electrochemistry. A laboratory example should illustrate a mandate, not be converted into ownership of every mission, product, standard or regulatory decision in that field.",
        ),
        (
            "ANRF programme-instrument boundary",
            "The owners identify PM ECRG as early-career project support and MAHA as a mission-mode platform, with EV mobility and later water or drones calls illustrating directed research. A call for proposals, eligibility rule, selected proposal, sanctioned grant, released instalment, completed project, validated technology and public outcome are separate statuses.",
        ),
        (
            "STI policy and Vigyan Dhara boundary",
            "DST's adopted-policy stack retains Science, Technology and Innovation Policy 2013 as the last clearly adopted national STI policy identified by the owners, while STIP 2020 was a draft and consultation exercise without a located adoption notification. Vigyan Dhara is a consolidated DST umbrella scheme; a policy, draft, umbrella scheme and individual grant are different instruments.",
        ),
        (
            "Governance tensions and inclusion",
            "Research governance must balance autonomy with accountability, excellence with wider institutional capacity, mission-mode urgency with curiosity-driven work, national priorities with peer-review independence, and concentration in elite institutions with regional or state-university inclusion. A new apex institution does not remove these implementation trade-offs.",
        ),
        (
            "Conservative PYQ institutional lens",
            "No audited 2018-2026 question is directly routed to Topic 24; relevant biotechnology, blue-LED, Bose-Einstein and semiconductor demands remain owned by their specialist science topics. Topic 24 may supply only the horizontal funding, laboratory, university and translation dimension and must not claim substantive ownership of the underlying discovery or technology.",
        ),
        (
            "Institution and status evidence ladder",
            "Constitution by law, notification, board meeting, programme launch, call for proposals, application, sanction, release, research activity, prototype, validation, licensing, commercialization, deployment and measured outcome are distinct evidence rungs. Counts, financing plans, current calls and policy status are date-sensitive and require an official dated owner.",
        ),
    ]
    traps = [
        "Do not call DST a Ministry or India's universal laboratory network.",
        "Do not place CSIR directly under DST while omitting DSIR.",
        "Do not call CSIR a Department, regulator or primarily grant-only body.",
        "Do not treat ANRF as a DST sub-office merely because DST is its administrative anchor.",
        "Do not merge ANRF's Governing Board with its Executive Council.",
        "Do not present SERB as a separate continuing statutory apex body after section 27.",
        "Do not rewrite ANRF's financing design as money received, appropriated or spent.",
        "Do not merge grants, fellowships and mission-mode programmes.",
        "Do not convert a funded project into a validated technology or societal outcome.",
        "Do not treat horizontal institutions as substitutes for sectoral mission agencies.",
        "Do not place ISRO, DAE, DBT, DRDO, MeitY, ICMR and ICAR in one constitutional class.",
        "Do not assign every sectoral result to a CSIR lab merely because it works in that discipline.",
        "Do not describe draft STIP 2020 as an adopted replacement without notification.",
        "Do not infer operational success from a portal page or call for proposals.",
        "Do not claim direct ownership of specialist science PYQs that only admit a supporting institution lens.",
    ]
    titles = [
        "Institutional forms mandates and acronym discipline",
        "DST policy coordination missions and Department identity",
        "DSIR industrial research technology transfer and CSIR placement",
        "CSIR society governance laboratory network and research performance",
        "ANRF Act statutory identity commencement and remit",
        "ANRF Governing Board Executive Council and administrative anchor",
        "SERB repeal succession savings and historical relevance",
        "ANRF financing design grants fellowships and crowd-in logic",
        "Curiosity-driven mission-mode translational and strategic research",
        "Research pipeline universities laboratories industry and standards",
        "Horizontal architecture versus vertical mission agencies",
        "ISRO DAE DBT DRDO MeitY ICMR ICAR and PRIP boundaries",
        "CSIR laboratory examples mandates and translation limits",
        "PM ECRG MAHA Vigyan Dhara STI policy and status distinctions",
        "Governance tensions PYQ support and evidence-status ladder",
    ]
    routes = [
        "Identify legal form, parent institution, mandate and instrument before expanding an acronym.",
        "Describe DST as a Department and horizontal policy anchor without turning it into every science agency.",
        "Place DSIR between the Ministry and CSIR, then separate industrial-research promotion from laboratory work.",
        "State CSIR's autonomous-society identity, research network and mandate without regulatory drift.",
        "Date the Act and commencement, then state ANRF's strategic funding and ecosystem role.",
        "Separate the Governing Board, Executive Council, PSA role and DST administrative support.",
        "Explain legal succession from SERB while retaining older references only as historical context.",
        "Classify financing design, grant, fellowship and mission programme before discussing effectiveness.",
        "Balance investigator autonomy, long-horizon science, strategic priority and translational need.",
        "Trace research from question to validation and adoption and locate each actor at its actual rung.",
        "Use horizontal bodies as capacity multipliers, not replacements for vertical missions.",
        "Name each sectoral body's constitutional form and parent before describing collaboration.",
        "Use a CSIR lab as a bounded example of research performance, measurement or translation.",
        "Separate adopted policy, draft policy, umbrella scheme, programme call, sanction and outcome.",
        "Add governance trade-offs, conservative PYQ ownership and a last-verified-status conclusion.",
    ]
    panels = [
        panel("Institutional form classifier", "classification-tree", [
            "MINISTRY -> political-administrative portfolio",
            "DEPARTMENT -> DST | DSIR | DBT | DAE",
            "STATUTORY BODY -> ANRF",
            "AUTONOMOUS SOCIETY -> CSIR",
            "OFFICE / ACADEMY / REGULATOR / LAB -> distinct again",
        ], [facts[0][0], facts[12][0]]),
        panel("Ministry to research network map", "organisation-map", [
            "MINISTRY OF SCIENCE AND TECHNOLOGY",
            "  DST -> policy / missions / coordination",
            "  DSIR -> industrial research / technology transfer",
            "    CSIR -> autonomous society + laboratory network",
            "  DBT -> biotechnology Department",
        ], [facts[1][0], facts[2][0], facts[3][0]]),
        panel("ANRF statutory governance map", "two-tier-governance", [
            "ANRF ACT 2023 -> statutory foundation",
            "COMMENCEMENT -> 5 February 2024",
            "GOVERNING BOARD -> PM ex officio President",
            "EXECUTIVE COUNCIL -> PSA ex officio Chairperson",
            "DST -> administrative anchor, not parent office",
        ], [facts[5][0], facts[6][0]]),
        panel("SERB to ANRF transition", "replacement-rail", [
            "SERB ACT 2008 -> former statutory grant body",
            "ANRF ACT section 27 -> repeal + dissolution",
            "ASSETS / LIABILITIES / PERSONNEL -> transition and savings",
            "OLD SERB REFERENCE -> historical context",
            "CURRENT APEX IDENTITY -> ANRF",
        ], [facts[7][0]]),
        panel("Funding instrument matrix", "instrument-matrix", [
            "FELLOWSHIP -> supports person",
            "PROJECT GRANT -> defined investigator project",
            "MISSION-MODE -> directed multi-institution outcome",
            "FINANCING DESIGN -> expected source mix",
            "APPROPRIATION / RELEASE / SPEND -> separate evidence",
        ], [facts[8][0], facts[9][0]]),
        panel("Research-to-use pipeline", "maturity-pipeline", [
            "QUESTION -> BASIC RESEARCH -> EXPERIMENT",
            "REPLICATION -> APPLIED RESEARCH -> PROTOTYPE",
            "TEST / STANDARD / REGULATION -> SCALE-UP",
            "MANUFACTURE / ADOPTION -> MEASURED OUTCOME",
            "STOP -> last verified rung",
        ], [facts[10][0], facts[19][0]]),
        panel("Horizontal and vertical architecture", "cross-axis-map", [
            "HORIZONTAL -> DST policy | ANRF funding | DSIR-CSIR capability",
            "VERTICAL -> space | nuclear | biotech | defence | digital",
            "BRIDGE -> universities + labs + skills + standards",
            "COLLABORATION -> does not change legal identity",
            "CAPACITY MULTIPLIER != mission replacement",
        ], [facts[11][0], facts[12][0], facts[13][0]]),
        panel("CSIR laboratory portfolio", "lab-portfolio", [
            "NPL -> metrology",
            "NCL -> chemistry | CECRI -> electrochemistry",
            "CCMB -> molecular biology | IGIB -> genomics",
            "CEERI -> electronics",
            "LAB MANDATE != sector-wide regulation or mission ownership",
        ], [facts[14][0]]),
        panel("ANRF programme status ladder", "programme-ladder", [
            "PM ECRG -> early-career project support",
            "MAHA -> mission-mode research platform",
            "CALL -> APPLICATION -> SELECTION -> SANCTION",
            "RELEASE -> RESEARCH -> VALIDATION",
            "NO AUTOMATIC COMMERCIAL OR PUBLIC OUTCOME",
        ], [facts[15][0], facts[19][0]]),
        panel("Policy instrument firewall", "policy-firewall", [
            "STI POLICY 2013 -> adopted policy owner",
            "STIP 2020 -> draft / consultation status",
            "VIGYAN DHARA -> DST umbrella scheme",
            "PROGRAMME / GRANT -> subordinate instrument",
            "DOCUMENT STATUS -> date and notification required",
        ], [facts[16][0]]),
        panel("Research governance balance board", "balance-board", [
            "AUTONOMY <-> ACCOUNTABILITY",
            "EXCELLENCE <-> INCLUSION",
            "CURIOSITY <-> MISSION PRIORITY",
            "PUBLIC RISK CAPITAL <-> INDUSTRY PARTICIPATION",
            "CENTRAL COORDINATION <-> INSTITUTIONAL FLEXIBILITY",
        ], [facts[13][0], facts[17][0]]),
        panel("PYQ support and evidence rail", "ownership-status-rail", [
            "SPECIALIST PYQ -> specialist science owner",
            "TOPIC 24 SUPPORT -> funding / lab / university / translation",
            "NO DIRECT ROUTE -> no ownership inflation",
            "LAW / MEETING / CALL / GRANT / PROTOTYPE / DEPLOYMENT",
            "CONCLUSION -> institution + mandate + last verified status",
        ], [facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018 and 2021", "GS-III",
            "Use only the institutional-support dimension of the routed biotechnology and applied-biotechnology R&D demands.",
            "Cross-owner supporting card: substantive biotechnology ownership remains with Topic 13 and related specialist owners; this card contributes funding, laboratory, university and translation architecture without claiming the technology answer.",
            [10, 11, 13, 14],
        ),
        common.make_pyq_solution(
            facts, "2018 and 2021", "GS-III",
            "Use only the research-ecosystem and translation dimension of the Bose-Einstein-statistics and blue-LED impact demands.",
            "Cross-owner supporting card: Topic 21 retains the physics and device answer; Topic 24 supplies the distinction among long-horizon research, laboratory capability, validation, scale and public outcome.",
            [9, 10, 13, 18],
        ),
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "Use only the horizontal research-architecture dimension of the semiconductor-industry and India Semiconductor Mission demand.",
            "Cross-owner supporting card: Topic 11 retains direct ownership; this card adds universities, ANRF, DST, CSIR, skills and translation constraints without rewriting a mission announcement as manufacturing success.",
            [11, 12, 13, 19],
        ),
    ]
    return common.topic(
        24,
        "S&T Institutions: DST, CSIR, ANRF",
        "24_S-and-T-Institutions-DST-CSIR-ANRF",
        facts,
        traps,
        [
            (10, "Distinguish DST, DSIR, CSIR, ANRF and SERB by legal identity, parentage and function.", [0, 1, 2, 3, 5, 7]),
            (10, "Explain ANRF's statutory governance, financing design and research instruments.", [5, 6, 8, 9]),
            (15, "Analyse the research-to-use pipeline and the complementary roles of funders, universities, laboratories and industry.", [10, 13, 14]),
            (15, "Discuss how horizontal S&T architecture supports but does not replace vertical mission agencies.", [11, 12, 18]),
            (20, "Critically examine ANRF as a research-governance reform through autonomy, inclusion, mission balance and private participation.", [8, 9, 15, 17]),
            (20, "Evaluate India's S&T institutional architecture using policy-status, programme-status and outcome-evidence discipline.", [1, 3, 16, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "Ministries, Departments, statutory bodies, autonomous societies",
            "Department of Science and Technology", "May 1971",
            "Department of Scientific and Industrial Research",
            "Council of Scientific and Industrial Research",
            "Societies Registration Act", "37 national laboratories",
            "39 outreach centres", "Innovation Complex", "ANRF Act, 2023",
            "Act 25 of 2023", "5 February 2024", "section 5",
            "Governing Board", "Prime Minister", "section 7",
            "Principal Scientific Adviser", "Executive Council", "section 27",
            "SERB Act, 2008", "financing design", "non-government sources",
            "research grant", "fellowship", "mission-mode programme",
            "curiosity research", "prototype", "replication",
            "horizontal policy", "vertical institutions", "Department of Space",
            "Ministry of Defence", "Ministry of Health and Family Welfare",
            "Department of Pharmaceuticals", "CSIR-NPL", "CSIR-NCL",
            "CSIR-CCMB", "CSIR-IGIB", "CSIR-CEERI", "CSIR-CECRI",
            "PM ECRG", "MAHA", "STI Policy 2013", "STIP 2020",
            "Vigyan Dhara", "autonomy with accountability",
            "excellence with wider institutional capacity", "call for proposals",
            "commercialization", "measured outcome",
        ],
        "No audited 2018-2026 PYQ is directly routed to Topic 24. Three representative cross-owner cards use biotechnology R&D, physics-discovery impact and semiconductor-mission demands only to demonstrate the supporting funding, laboratory, university and translation lens; direct ownership remains with Topics 13, 21 and 11 respectively.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Live checks on 2026-09-04 confirmed substantive CSIR network text and located official DST, DSIR, India Code and ANRF surfaces, while several returned title-only, blocked, obsolete-fragment or raw-PDF responses. Exact statutory distinctions remain owner-bounded; no portal state, call, financing design or laboratory count was turned into spending, project completion, commercialization or policy outcome.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "DST, DSIR, CSIR, ANRF AND SERB INSTITUTIONAL IDENTITY MAP",
            "FUNDING, RESEARCH, LABORATORY AND MISSION-AGENCY PIPELINE",
            "STATUTE, POLICY, PROGRAMME AND OUTCOME STATUS FIREWALLS",
            "GOVERNANCE TRADE-OFF, PYQ-SUPPORT AND ANSWER-WRITING SPINE",
        ),
        register_answer_spine=[
            "NAME LEGAL FORM PARENT BODY MANDATE AND INSTRUMENT BEFORE THE ACRONYM",
            "PLACE DST AND DSIR AS SEPARATE DEPARTMENTS AND CSIR UNDER DSIR",
            "DESCRIBE CSIR AS AN AUTONOMOUS RESEARCH-PERFORMING SOCIETY",
            "DATE ANRF ACT COMMENCEMENT GOVERNING BOARD AND EXECUTIVE COUNCIL",
            "EXPLAIN SECTION 27 SERB REPEAL AND HISTORICAL-SUCCESSOR BOUNDARY",
            "SEPARATE FINANCING DESIGN APPROPRIATION RELEASE SANCTION SPEND AND OUTCOME",
            "DISTINGUISH FELLOWSHIP PROJECT GRANT CURIOSITY WORK AND MISSION-MODE RESEARCH",
            "TRACE QUESTION RESEARCH REPLICATION PROTOTYPE STANDARD SCALE ADOPTION AND IMPACT",
            "USE HORIZONTAL INSTITUTIONS AS CAPACITY MULTIPLIERS FOR VERTICAL MISSIONS",
            "KEEP ISRO DAE DBT DRDO MEITY ICMR ICAR AND PRIP FORMS DISTINCT",
            "ADD AUTONOMY ACCOUNTABILITY EXCELLENCE INCLUSION AND PUBLIC-PRIVATE TRADE-OFFS",
            "KEEP SPECIALIST PYQ OWNERSHIP AND STOP AT THE LAST VERIFIED EVIDENCE RUNG",
        ],
    )


TOPIC_24 = _topic_24()
