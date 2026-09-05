"""Authored learner-v2 data for Science and Technology Topic 12."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


DPDP_LIVE_ATTEMPTS = [
    (
        "https://www.meity.gov.in/static/uploads/2025/11/"
        "c56ceae6c383460ca69577428d36828b.pdf — attempted 2026-09-04; "
        "the official commencement-notification PDF returned HTTP 403 to direct "
        "retrieval. The repository owner retains its previously verified "
        "G.S.R. 843(E) tranche map; no later commencement or enforcement claim "
        "was imported."
    ),
    (
        "https://www.meity.gov.in/static/uploads/2025/11/"
        "53450e6e5dc0bfa85ebd78686cadad39.pdf — attempted 2026-09-04; "
        "the official DPDP Rules, 2025 PDF returned HTTP 403. Notification of "
        "rules was not treated as commencement of deferred Act provisions."
    ),
    (
        "https://www.meity.gov.in/static/uploads/2026/05/"
        "53b1bcf01cab9a0adde463e73fbc3417.pdf — attempted 2026-09-04; "
        "the official Board recruitment advertisement returned HTTP 403. "
        "Official-domain search surfaced the advertisement and appointment "
        "process, but did not verify completed appointments, operational "
        "staffing or functioning adjudication; none is claimed."
    ),
    (
        "https://www.cert-in.org.in/Directions70B.jsp — fetched 2026-09-04; "
        "the official page substantively listed CERT-In's 28 April 2022 "
        "directions under section 70B and related FAQs and extensions. No "
        "incident total or compliance outcome was imported."
    ),
    (
        "https://nciipc.gov.in/about_us.html — attempted 2026-09-04; direct "
        "retrieval failed at the transport layer. The repository owner's "
        "previously verified section 70A and CII mandate is retained without "
        "inventing current activity, staffing or protected-system counts."
    ),
]


def _topic_12() -> dict[str, object]:
    facts = [
        (
            "Privacy-cybersecurity boundary",
            "Data protection governs whether digital personal data is lawfully "
            "collected, processed, retained, shared and redressed, whereas "
            "cybersecurity protects systems, networks and critical infrastructure "
            "against compromise or disruption; one breach may engage both domains "
            "without merging their legal tests, institutions or remedies.",
        ),
        (
            "DPDP actor boundary",
            "A Data Principal is the individual to whom personal data relates, a "
            "Data Fiduciary determines the purpose and means of processing, a Data "
            "Processor acts for the Fiduciary, and a Consent Manager is a "
            "Board-registered intermediary through which consent can be managed.",
        ),
        (
            "Scope boundary",
            "The DPDP Act covers digital personal data, including personal data "
            "collected offline and digitised later, and can apply outside India "
            "when processing relates to offering goods or services to Data "
            "Principals in India; anonymised, non-personal and wholly offline "
            "records are not automatically covered.",
        ),
        (
            "Legal-status ladder",
            "Enactment creates the statute, Gazette notification publishes a legal "
            "instrument, commencement brings specified provisions into force, and "
            "enforcement requires applicable duties plus functioning institutions "
            "and proceedings; these rungs must never be collapsed.",
        ),
        (
            "Immediate-tranche boundary",
            "G.S.R. 843(E) dated 13 November 2025 immediately commenced provisions "
            "including definitions, sections 18-26 on the Board, rule-making and "
            "section 44(3), while G.S.R. 844(E) legally established the Board and "
            "G.S.R. 845(E) fixed a Chairperson plus four Members.",
        ),
        (
            "One-year-tranche boundary",
            "Section 6(9), section 27(1)(d) and rule 4 concerning Consent Manager "
            "registration and obligations were scheduled for commencement one "
            "year after Gazette publication, not on the Rules' notification date.",
        ),
        (
            "Eighteen-month-tranche boundary",
            "Notice, consent, certain legitimate uses, Data Principal rights and "
            "duties, Fiduciary and Significant Data Fiduciary obligations, section "
            "16, section 17, most Board proceedings, appeals, penalties and the "
            "omission of IT Act section 43A were scheduled for the eighteen-month "
            "tranche; notification alone did not make them binding.",
        ),
        (
            "Consent-legitimate-use boundary",
            "The enacted Act uses consent and the closed list of certain legitimate "
            "uses in section 7; it does not retain the 2022 draft label of deemed "
            "consent, and withdrawal stops consent-based processing unless another "
            "lawful ground applies.",
        ),
        (
            "Rights-duties boundary",
            "The statutory design gives Data Principals access, correction and "
            "erasure, grievance and nomination routes while section 15 also imposes "
            "duties such as not impersonating another person or filing false or "
            "frivolous grievances; design provisions must be written conditionally "
            "until their tranche commences.",
        ),
        (
            "SDF boundary",
            "Significant Data Fiduciary status is conferred by Central Government "
            "notification using risk factors rather than arising automatically; "
            "the design adds an India-based Data Protection Officer, independent "
            "auditor, impact assessment and audit duties.",
        ),
        (
            "Board-role boundary",
            "The Data Protection Board of India is the Act's statutory digital "
            "adjudicatory body for specified compliance matters and monetary "
            "penalties, with appeals to TDSAT; legal establishment and advertised "
            "recruitment do not prove appointed membership, operational staffing "
            "or functioning adjudication.",
        ),
        (
            "Section-16 boundary",
            "Section 16 uses a notification-based negative-list model: transfers "
            "outside India are permitted except to countries or territories the "
            "Central Government restricts, while stricter sectoral localisation "
            "requirements can continue to apply.",
        ),
        (
            "Section-17 boundary",
            "Section 17 contains processing-specific exemptions and allows the "
            "Central Government under section 17(2)(a) to exempt a State "
            "instrumentality by notification on listed grounds; exemption power "
            "is not the same as a universal automatic exemption.",
        ),
        (
            "RTI-amendment boundary",
            "Section 44(3), commenced in the immediate tranche, substituted RTI "
            "Act section 8(1)(j) with an exemption for information relating to "
            "personal information; it creates a privacy-transparency issue and "
            "must not be confused with the deferred omission of IT Act section 43A.",
        ),
        (
            "Penalty boundary",
            "DPDP penalties are civil and financial under the Schedule, not prison "
            "sentences or individual compensation: the listed maximum is 250 crore "
            "rupees for failure to take reasonable security safeguards, with other "
            "maximums including 200 crore rupees for breach notification or "
            "children's-data obligations and 150 crore rupees for SDF obligations.",
        ),
        (
            "CERT-In role boundary",
            "CERT-In is MeitY's national incident-response agency under IT Act "
            "section 70B; its 28 April 2022 directions address specified incident "
            "reporting, clock synchronisation, log retention and provider records, "
            "not DPDP consent, Data Principal rights or Board adjudication.",
        ),
        (
            "NCIIPC role boundary",
            "NCIIPC, a unit of NTRO under IT Act section 70A, is the national nodal "
            "agency for protection of Critical Information Infrastructure; sector "
            "importance alone does not establish that every asset is notified or "
            "declared as a protected system.",
        ),
        (
            "I4C role boundary",
            "The Indian Cyber Crime Coordination Centre under the Ministry of Home "
            "Affairs coordinates cybercrime response and supports the National "
            "Cybercrime Reporting Portal and helpline 1930; it is distinct from "
            "CERT-In incident response, NCIIPC CII protection and Board adjudication.",
        ),
        (
            "GDPR-signature-PKI boundary",
            "GDPR is a European Union comparator rather than Indian law, while a "
            "digital signature uses a private key for signing and a corresponding "
            "public key and certificate trust chain for verification of origin and "
            "integrity; it is not a scanned signature or whole-message encryption.",
        ),
        (
            "Breach-and-status discipline",
            "A personal-data breach can require privacy compliance and cyber "
            "incident response in parallel, but every answer must separately label "
            "the applicable law, institution, remedy and current rung—enacted, "
            "notified, commenced, staffed, adjudicated or enforced—using dated "
            "official evidence.",
        ),
    ]
    traps = [
        "Do not merge privacy compliance with cybersecurity operations.",
        "Do not assign Board functions to CERT-In, NCIIPC or I4C.",
        "Do not say Rules notification made every DPDP duty operative.",
        "Do not collapse enactment, notification, commencement and enforcement.",
        "Do not claim that legal Board establishment proves operational staffing.",
        "Do not call section 16 blanket localisation or an adequacy whitelist.",
        "Do not convert section 17's notification power into an automatic exemption.",
        "Do not omit the immediately effective RTI section 8(1)(j) amendment.",
        "Do not confuse the deferred IT Act section 43A omission with the RTI change.",
        "Do not describe Schedule penalties as imprisonment or victim compensation.",
        "Do not place CERT-In under MHA or I4C under MeitY.",
        "Do not infer an objective answer key from a routed PYQ concept.",
    ]
    titles = [
        "Privacy data protection and cybersecurity split",
        "Data Principal Fiduciary Processor and Consent Manager",
        "Digital personal data scope and extraterritorial reach",
        "Enactment notification commencement and enforcement ladder",
        "Immediate DPDP tranche and legal Board establishment",
        "One-year Consent Manager tranche",
        "Eighteen-month substantive compliance tranche",
        "Consent certain legitimate uses rights and duties",
        "Significant Data Fiduciary risk and governance duties",
        "Board proceedings appeals and operational-status caution",
        "Section 16 cross-border transfer model",
        "Section 17 exemptions and State instrumentalities",
        "RTI amendment IT Act section 43A and penalty schedule",
        "CERT-In NCIIPC and I4C institutional routing",
        "GDPR digital signatures PKI PYQs and breach synthesis",
    ]
    routes = [
        "Open by separating lawful data processing from system defence.",
        "Map each privacy actor before assigning a duty or remedy.",
        "Fix digital-personal-data scope before discussing rights.",
        "Date-stamp each legal rung and avoid present-tense inflation.",
        "State what commenced immediately and what establishment did not prove.",
        "Keep Consent Manager commencement in its own tranche.",
        "Write deferred duties as enacted and scheduled, not enforced.",
        "Link lawful grounds to rights and section 15 duties.",
        "Treat SDF as a notified risk category, not a size synonym.",
        "Separate statutory design, appointment, operation and adjudication.",
        "Explain negative-list transfer while preserving sectoral rules.",
        "Distinguish specific exemptions from notified State exemption power.",
        "Contrast the live RTI change, deferred section 43A omission and penalties.",
        "Route incidents, CII and cybercrime to their correct institutions.",
        "Use routed PYQ concepts without answer keys and conclude with dual response.",
    ]
    panels = [
        panel("Privacy and cyber twin rail", "dual-rail", [
            "PRIVACY -> lawful collection, use, retention and redress",
            "CYBERSECURITY -> prevention, detection, response and recovery",
            "SAME BREACH -> two questions and potentially two response chains",
            "DPDP BOARD != CERT-In != NCIIPC != I4C",
            "RULE -> complementary domains are not interchangeable",
        ], [facts[0][0], facts[19][0]]),
        panel("DPDP actor chain", "institution-map", [
            "DATA PRINCIPAL -> rights-bearing individual",
            "DATA FIDUCIARY -> decides purpose and means",
            "DATA PROCESSOR -> acts for Fiduciary",
            "CONSENT MANAGER -> Board-registered consent interface",
            "BOARD -> specified adjudication; TDSAT hears appeals",
        ], [facts[1][0], facts[10][0]]),
        panel("Scope gateway", "decision-tree", [
            "PERSONAL DATA? -> if no, DPDP personal-data route stops",
            "DIGITAL OR DIGITISED LATER? -> if yes, scope can attach",
            "OUTSIDE INDIA? -> goods or services offered in India test",
            "ANONYMISED / NON-PERSONAL -> not automatically covered",
            "RULE -> identify data class before compliance claim",
        ], [facts[2][0]]),
        panel("Legal status staircase", "status-ladder", [
            "ENACTED -> parent statute exists",
            "NOTIFIED -> instrument published in Gazette",
            "COMMENCED -> specified provision is in force",
            "STAFFED / ADJUDICATING -> institutional evidence required",
            "ENFORCED -> applicable proceeding or outcome required",
        ], [facts[3][0], facts[10][0], facts[19][0]]),
        panel("Three-tranche chronology", "timeline", [
            "13 NOV 2025 -> definitions, Board provisions, RTI amendment",
            "ONE YEAR -> s.6(9), s.27(1)(d), rule 4",
            "EIGHTEEN MONTHS -> substantive compliance core and penalties",
            "RULES NOTIFIED -> does not erase deferred dates",
            "DATE CHECK -> re-verify before present-tense writing",
        ], [facts[4][0], facts[5][0], facts[6][0]]),
        panel("Lawful processing and rights loop", "process-loop", [
            "NOTICE -> specified information",
            "CONSENT OR s.7 CERTAIN LEGITIMATE USE -> lawful ground",
            "PROCESSING -> Fiduciary and Processor responsibilities",
            "ACCESS / CORRECTION / ERASURE / GRIEVANCE / NOMINATION",
            "s.15 DUTIES -> rights holder also has statutory duties",
        ], [facts[7][0], facts[8][0]]),
        panel("SDF governance stack", "risk-pyramid", [
            "GOVERNMENT NOTIFICATION -> creates SDF status",
            "RISK FACTORS -> scale, sensitivity and public consequences",
            "INDIA-BASED DPO -> governance contact",
            "INDEPENDENT AUDITOR + DPIA + AUDITS -> added assurance",
            "TRAP -> large entity is not automatically an SDF",
        ], [facts[9][0]]),
        panel("Sections 16 and 17 matrix", "comparison-matrix", [
            "s.16 -> notified restricted destinations; permissive default",
            "SECTORAL RULE -> may impose stricter localisation",
            "s.17(1) -> processing-specific exemptions",
            "s.17(2)(a) -> notified State-instrumentality exemption",
            "RULE -> transfer rule and exemption rule answer different questions",
        ], [facts[11][0], facts[12][0]]),
        panel("Consequential amendment fork", "replacement-diagram", [
            "s.44(3) -> RTI s.8(1)(j) substituted in immediate tranche",
            "PRIVACY <-> TRANSPARENCY -> contested rights balance",
            "s.44(2) -> IT Act s.43A omission in deferred tranche",
            "LIVE CHANGE != SCHEDULED CHANGE",
            "RULE -> identify parent Act, section and commencement",
        ], [facts[13][0], facts[6][0]]),
        panel("Penalty rail", "penalty-scale", [
            "SECURITY-SAFEGUARD FAILURE -> maximum Rs 250 crore",
            "BREACH NOTICE / CHILDREN'S DUTIES -> maximum Rs 200 crore",
            "SDF DUTIES -> maximum Rs 150 crore",
            "CHARACTER -> civil and financial",
            "NOT INCLUDED -> imprisonment or automatic victim compensation",
        ], [facts[14][0]]),
        panel("Cyber institution router", "routing-map", [
            "CERT-In / MeitY / s.70B -> incident response and directions",
            "NCIIPC / NTRO / s.70A -> notified CII protection",
            "I4C / MHA -> cybercrime coordination, portal and 1930",
            "DATA PROTECTION BOARD -> DPDP compliance adjudication",
            "RULE -> route by function, statute and administrative home",
        ], [facts[15][0], facts[16][0], facts[17][0]]),
        panel("Routed PYQ answer spine", "answer-spine", [
            "2018 -> data-protection report: strengths plus weaknesses",
            "2019 -> GDPR comparator; digital-signature authentication",
            "2024 -> DPDP context, salient features and dated status",
            "BREACH -> privacy compliance plus cyber response",
            "CONCLUDE -> rights, resilience, capacity and status discipline",
        ], [facts[18][0], facts[19][0], facts[3][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018", "GS-III",
            "Discuss the strengths and weaknesses of the personal data-protection "
            "report in safeguarding personal data in cyberspace.",
            "Verified routed Mains demand from the audited 2018-2023 GS-III "
            "ledger; the response uses the report-to-enacted-law context without "
            "pretending the 2023 Act answered every 2018 design criticism.",
            [0, 1, 12, 13, 19],
        ),
        common.make_pyq_solution(
            facts, "2019", "Prelims GS-I",
            "Assess statements on adoption and implementation of the General "
            "Data Protection Regulation.",
            "Verified routed objective concept; GDPR is retained as an EU "
            "comparator and no unavailable answer letter is inferred.",
            [18, 0, 3],
        ),
        common.make_pyq_solution(
            facts, "2019", "Prelims GS-I",
            "Assess digital-signature characteristics and electronic authentication.",
            "Verified routed objective concept shared with computing foundations; "
            "no unavailable answer letter is asserted.",
            [18, 15, 19],
        ),
        common.make_pyq_solution(
            facts, "2020", "Prelims GS-I",
            "Identify the Public Key Infrastructure context in Indian digital security.",
            "Verified routed objective concept; the certificate and trust-chain "
            "boundary is explained without inferring an answer key.",
            [18, 15],
        ),
        common.make_pyq_solution(
            facts, "2022", "Prelims GS-I",
            "Assess Web 3.0, blockchain and user-control claims relating to data.",
            "Verified routed objective concept shared with computing foundations; "
            "technology-design claims are not converted into automatic privacy or "
            "security outcomes, and no answer letter is inferred.",
            [0, 2, 19],
        ),
        common.make_pyq_solution(
            facts, "2024", "GS-III",
            "Describe the context and salient features of the Digital Personal "
            "Data Protection Act, 2023.",
            "Verified direct routed Mains demand from the audited 2024-2025 "
            "GS-III ledger; the model preserves privacy-cyber and phased-status "
            "discipline as of the dated source audit.",
            [0, 1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        ),
    ]
    return common.topic(
        12,
        "Data Protection: DPDP Act and Cybersecurity",
        "12_Data-Protection-DPDP-Act-and-Cybersecurity",
        facts,
        traps,
        [
            (
                10,
                "Distinguish data protection from cybersecurity in India's "
                "digital-governance architecture.",
                [0, 15, 16, 17, 19],
            ),
            (
                10,
                "Explain the DPDP actor chain and the rights-duties design.",
                [1, 7, 8, 10],
            ),
            (
                15,
                "Analyse the phased commencement of the DPDP Act and explain why "
                "notification cannot be equated with enforcement.",
                [3, 4, 5, 6, 10, 19],
            ),
            (
                15,
                "Examine sections 16 and 17 together with the RTI amendment and "
                "their implications for privacy, transparency and State power.",
                [11, 12, 13, 19],
            ),
            (
                20,
                "Evaluate whether the DPDP framework adequately balances rights, "
                "innovation, institutional accountability and effective remedies.",
                [1, 2, 7, 8, 9, 10, 12, 13, 14],
            ),
            (
                20,
                "Discuss how India should coordinate privacy compliance, cyber "
                "incident response, CII protection and cybercrime control without "
                "blurring institutional mandates.",
                [0, 10, 14, 15, 16, 17, 19],
            ),
        ],
        titles,
        routes,
        panels,
        [
            "digital personal data",
            "Data Principal",
            "Data Fiduciary",
            "Data Processor",
            "Consent Manager",
            "certain legitimate uses",
            "section 15",
            "Significant Data Fiduciary",
            "Data Protection Board of India",
            "TDSAT",
            "G.S.R. 843(E)",
            "phased commencement",
            "section 16",
            "negative list",
            "section 17",
            "section 17(2)(a)",
            "section 44(3)",
            "RTI section 8(1)(j)",
            "IT Act section 43A",
            "Schedule penalties",
            "CERT-In",
            "section 70B",
            "NCIIPC",
            "section 70A",
            "Critical Information Infrastructure",
            "I4C",
            "digital signature",
            "Public Key Infrastructure",
            "GDPR",
            "enactment",
            "notification",
            "commencement",
            "enforcement",
        ],
        (
            "Audited routing supplies six demand cards: the 2018 GS-III "
            "data-protection-report critique; the 2019 GDPR and digital-signature "
            "objective concepts; the 2020 PKI concept; the 2022 Web3 data-control "
            "concept; and the 2024 GS-III DPDP Act demand. Objective cards carry "
            "no answer letters or inferred official keys."
        ),
        pyqs,
        DPDP_LIVE_ATTEMPTS,
        (
            "Official live-source attempts were made on 2026-09-04. The Act was "
            "enacted in 2023; notifications dated 13 November 2025 established "
            "the Board in law, notified the Rules and commenced only specified "
            "tranches. Direct retrieval did not verify completed Board "
            "appointments, operational staffing, functioning adjudication or a "
            "later enforcement outcome, so none is claimed. Re-check the one-year "
            "and eighteen-month tranches against official Gazette material before "
            "using present-tense obligations."
        ),
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "PRIVACY, PERSONAL-DATA ACTORS AND CYBERSECURITY SPLIT",
            "PHASED COMMENCEMENT, SECTIONS 16-17, RTI AND PENALTY TRAPS",
            "DPDP-CYBER INSTITUTIONAL ANSWER SPINE",
            "OFFICIAL-SOURCE, BOARD-STATUS AND ENFORCEMENT FIREWALL",
        ),
        register_answer_spine=[
            "DEFINE DIGITAL PERSONAL DATA AND SEPARATE PRIVACY FROM CYBERSECURITY",
            "MAP DATA PRINCIPAL FIDUCIARY PROCESSOR CONSENT MANAGER AND BOARD",
            "LABEL ENACTMENT NOTIFICATION COMMENCEMENT STAFFING ADJUDICATION ENFORCEMENT",
            "TRACE IMMEDIATE ONE-YEAR AND EIGHTEEN-MONTH TRANCHES",
            "EXPLAIN CONSENT s.7 RIGHTS s.15 DUTIES SDF AND TDSAT",
            "COMPARE s.16 NEGATIVE LIST WITH s.17 NOTIFIED EXEMPTIONS",
            "DISTINGUISH RTI s.8(1)(j) CHANGE FROM IT ACT s.43A OMISSION",
            "ROUTE CERT-In NCIIPC I4C AND BOARD BY STATUTE AND FUNCTION",
            "USE CIVIL SCHEDULE PENALTIES AND AUDITED PYQS WITHOUT ANSWER KEYS",
            "CONCLUDE ON RIGHTS RESILIENCE CAPACITY AND DATED STATUS DISCIPLINE",
        ],
    )


TOPIC_12 = _topic_12()
