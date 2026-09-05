"""Generate Polity learner-v2 topics 48-51 in strict preservation-safe order."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_43_47_sequential as prior


base = prior.base
preserve = prior.preserve
case_years = prior.case_years
ROOT = prior.ROOT
DATE = "2026-08-25"
SECTION = prior.SECTION
EXPORTS = prior.EXPORTS
FINAL_LIBRARY = prior.FINAL_LIBRARY
FLOW_LIBRARY = prior.FLOW_LIBRARY
BATCH_ID = "polity-48-51-sequential-batch-2026-08-25"

base.DATE = DATE


def topic(
    key: str,
    title: str,
    canonical: str,
    basic: str,
    advanced: str,
    cross: list[str],
    live: list[str],
    exact_pyqs: int,
    supporting_pyqs: int,
    current_note: str,
    caveat: str,
    coverage_contract: list[str],
    *,
    visual_sessions: list[int],
) -> dict[str, Any]:
    value = base.topic(
        key,
        title,
        canonical,
        basic,
        advanced,
        cross,
        live,
        exact_pyqs,
        supporting_pyqs,
        current_note,
        caveat,
        visual_sessions=visual_sessions,
    )
    value["coverage_contract"] = coverage_contract
    return value


TOPICS = [
    topic(
        "polity-48",
        "Ministries Departments and Central Secretariat",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Ministries-and-Departments-of-Government.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Ministries-and-Departments-of-Government.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\48_Ministries-Departments-and-Central-Secretariat.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CIC-and-SIC.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\05_E-Governance-Models-and-User-Centricity.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\09_Civil-Services-and-Mission-Karmayogi.md",
        ],
        [
            "https://cabsec.gov.in/",
            "https://darpg.gov.in/",
            "https://sansad.in/",
        ],
        1,
        2,
        "The Cabinet Secretariat's official description of the Allocation and "
        "Transaction of Business Rules, Cabinet/Cabinet Committee assistance, "
        "inter-ministerial coordination and crisis coordination was rechecked on "
        "25 August 2026. Ministry, department, office and committee names remain "
        "notification-sensitive and no permanent count is frozen.",
        "Articles 73, 74, 77 and 78 establish the executive framework, while the "
        "1961 business rules allocate and route work. The Central Secretariat is "
        "the collective policy machinery, not the Cabinet Secretariat or PMO. "
        "Attached offices, autonomous bodies, CPSEs and statutory regulators retain "
        "distinct legal identities; reorganisation is a dated executive-rule fact.",
        [
            "Articles 73, 74, 77 and 78 with Allocation/Transaction of Business Rules",
            "ministry, department, portfolio, office, secretariat and field distinctions",
            "political executive, permanent executive and Minister-Secretary relationship",
            "Central Secretariat policy, legislation, budget, coordination and memory",
            "Cabinet Secretariat, PMO, Cabinet Secretary, committees and escalation",
            "file hierarchy, delegation, consultation, authentication and accountability",
            "attached/subordinate offices, autonomous bodies, CPSEs and regulators",
            "Parliament, CAG, RTI, digital systems, expertise and reform commissions",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20],
    ),
    topic(
        "polity-49",
        "Regulatory State and Quasi Judicial Institutions",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\49_Regulatory-State-and-Quasi-Judicial-Institutions.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\11_Regulatory-Governance-and-Independent-Regulators.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\04_RBI-Monetary-Policy-and-Liquidity-Management.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md",
        ],
        [
            "https://www.cci.gov.in/antitrust",
            "https://www.sebi.gov.in/",
            "https://www.meity.gov.in/",
            "https://www.sci.gov.in/",
        ],
        4,
        0,
        "CCI's current official competition-law description and the official "
        "regulator, MeitY and Supreme Court portals were rechecked on 25 August "
        "2026. Digital, data and platform proposals or subordinate frameworks are "
        "used only with their dated legal status; no draft is represented as enacted law.",
        "Statutory, regulatory and quasi-judicial describe different axes. A regulator "
        "is quasi-judicial only while performing an adjudicatory function. Independence "
        "does not remove legislative, audit, transparency, appeal or judicial-review "
        "accountability, and a consultation paper or proposed digital regime is not law.",
        [
            "rise of the regulatory state after liberalisation and specialised governance",
            "constitutional, statutory and executive source distinctions with sector examples",
            "rule-making, licensing, tariffs, monitoring, enforcement and adjudication",
            "natural justice, bias, hearing, reasons and functional separation",
            "court, tribunal, regulator, commission and appellate-forum distinctions",
            "appointments, tenure, removal, finance, capture and revolving-door controls",
            "delegated legislation, appeals, judicial review, Parliament, CAG and RTI",
            "digital/platform regulation boundaries and calibrated regulatory reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],
    ),
    topic(
        "polity-50",
        "Concept of the Constitution",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Concept-of-the-Constitution.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Concept-of-the-Constitution.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\50_Concept-of-the-Constitution.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Making-of-the-Constitution.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Salient-Features.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Preamble.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Emergency-Provisions.md",
        ],
        [
            "https://legislative.gov.in/",
            "https://www.sci.gov.in/",
        ],
        0,
        3,
        "The official Constitution and Supreme Court portals were rechecked on "
        "25 August 2026. This is a concept-and-doctrine topic: current litigation, "
        "political claims and interpretive proposals are not converted into settled "
        "constitutional meaning merely because they use constitutional vocabulary.",
        "This topic owns the higher-order idea of a constitution and constitutionalism, "
        "not a duplicate list of salient features or the history of constitution-making. "
        "Living, original-meaning, transformative and morality-based approaches are "
        "bounded interpretive lenses; none authorises free-standing personal preference.",
        [
            "constitution as higher-order framework of power, rights and political community",
            "constitutionalism, rule of law, limited government, consent and legitimacy",
            "written/uncodified, rigid/flexible, federal/unitary and supremacy classifications",
            "constituent versus constituted power and legal versus political constitution",
            "popular, parliamentary and constitutional sovereignty with conventions",
            "constitutional morality, transformative and living constitutionalism bounded",
            "Preamble, amendment, basic structure, identity and social revolution",
            "emergency failure, interpretive debates, cases, traps and answer frameworks",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20],
    ),
    topic(
        "polity-51",
        "Rights and Liabilities of the Government",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Rights-and-Liabilities-of-the-Government.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Rights-and-Liabilities-of-the-Government.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\51_Rights-and-Liabilities-of-the-Government.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\18_Utilization-of-Public-Funds-and-Challenges-of-Corruption.md",
        ],
        [
            "https://gem.gov.in/",
            "https://doe.gov.in/",
            "https://legislative.gov.in/",
            "https://www.sci.gov.in/",
        ],
        0,
        1,
        "The Constitution, Government e-Marketplace and official expenditure, "
        "legislative and Supreme Court portals were rechecked on 25 August 2026. "
        "Procurement manuals and platform instructions are administrative controls; "
        "an arbitration proposal changes the 1996 Act only if duly enacted.",
        "Articles 294-300 create governmental legal capacity and liability; they do "
        "not establish blanket sovereign immunity. Article 299 form, Contract Act "
        "Section 70 restitution, private tort, constitutional tort, Article 361 "
        "official protection and CPC notice are separate legal routes.",
        [
            "Part XII Chapter III Articles 294-300 and juristic-person concepts",
            "succession, reorganisation, property, ownerless assets and maritime resources",
            "Article 298 trade/business/property/contract capacity and legislative limits",
            "Article 299 mandatory form, authority, execution and consequences",
            "Contract Act Section 70 restitution and quantum-meruit boundary",
            "Article 300 suits, CPC Sections 79/80, Union/State party naming",
            "tort immunity trajectory, vicarious liability and constitutional compensation",
            "Article 300A, procurement, arbitration, privileges, traps and reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20],
    ),
]


SUPPLEMENTS: dict[str, list[tuple[str, str]]] = {
    "polity-48": [
        (
            "Secretariat, directorate, field administration and delivery chain",
            """| Level | Governing purpose | Typical output | Accountability |
|---|---|---|---|
| Secretariat | policy, law, budget and coordination | decision, rule, scheme, review | Minister, Parliament, audit and court |
| Directorate/attached office | technical executive direction | standards, technical supervision | department plus governing instrument |
| Subordinate/field office | territorial execution and enforcement | inspection, service or field order | hierarchy, citizen remedy and audit |
| Autonomous body | specialised programme/research/service | grant-based or chartered output | instrument, governing body and ministry |
| CPSE | commercial or strategic operation | goods/services and commercial return | company/statute, ownership and CAG regime |
| Regulator | arm's-length statutory governance | rule, licence, supervision or order | parent Act, appeal, Parliament and court |

[LIMIT] "Directorate" is an administrative label, not a single constitutional category.
The source instrument and allocated function determine control and accountability.""",
        ),
        (
            "Digital government, mission units and lateral expertise",
            """DIGITAL FILE CHAIN
receipt/e-file -> metadata and allocation -> noting/options -> consultation
-> authenticated approval -> digital issue -> record retention -> audit/RTI retrieval.

MISSION-MODE UNIT
cross-department outcome -> named lead -> time-bound multidisciplinary team
-> shared data/milestones -> escalation -> sunset or mainstreaming.

EXPERTISE BOUNDARY
specialist advice and lateral recruitment can improve competency-to-post fit;
selection must remain fair, conflicts disclosed, tenure sufficient and authority recorded.

[LIMIT] A dashboard or project-management unit cannot silently replace the department,
statutory authority, financial sanction, Cabinet route or parliamentary answerability.""",
        ),
    ],
    "polity-49": [
        (
            "Natural justice and regulator-power case matrix",
            """| Decision | Decision year | Safe proposition |
|---|---:|---|
| In re Delhi Laws Act | 1951 | essential legislative function cannot be abdicated |
| A.K. Kraipak v. Union of India | 1969 | administrative/quasi-judicial line is thin; bias rule applies |
| Maneka Gandhi v. Union of India | 1978 | procedure affecting liberty must be just, fair and reasonable |
| S.N. Mukherjee v. Union of India | 1990 | reasons support fairness, discipline and effective review |
| CCI v. SAIL | 2010 | character and appealability depend on the statutory stage/function |
| Cellular Operators Association v. TRAI | 2016 | delegated regulation must remain within statute and non-arbitrary |
| L. Chandra Kumar v. Union of India | 1997 | High Court judicial review is a basic-structure floor |

[LIMIT] The same authority may act quasi-legislatively, administratively and
quasi-judicially at different stages. Do not attach one label to every act.""",
        ),
        (
            "Digital, data and platform regulation boundary",
            """REGULATORY QUESTION
identified harm -> statutory competence -> affected market/right -> proposed tool
-> consultation and impact assessment -> rule/order -> appeal/review -> ex-post evaluation.

PLATFORM RISKS
network effects | self-preferencing | data concentration | dark patterns
| algorithmic opacity | child/consumer harm | systemic cyber risk.

DESIGN OPTIONS
competition enforcement | sector regulation | data-protection duties
| consumer law | interoperability/access duties | code/sandbox.

[CURRENT] As of 25 August 2026, every rule, board, draft Bill or consultation must be
named with its exact instrument and date. A proposal is not settled law.

[LIMIT] Regulating a digital activity does not make every affected authority a
quasi-judicial body; character remains function-specific.""",
        ),
    ],
    "polity-50": [
        (
            "Constituent power and constituted institutions",
            """CONSTITUENT POWER
creates/founds constitutional authority -> chooses institutional architecture.

CONSTITUTED POWER
Parliament | executive | judiciary | federal units | commissions
-> authority exists only within the Constitution.

INDIAN AMENDMENT QUESTION
Article 368 permits constitutional change
-> Kesavananda Bharati (1973) preserves basic structure
-> amendment is broad constituted power, not unlimited original sovereignty.

[LIMIT] Basic-structure review does not make the judiciary an unlimited constituent body.""",
        ),
        (
            "Legal constitution, political constitution and conventions",
            """LEGAL CONTROL
text -> rights -> jurisdiction -> judicial review -> enforceable remedy.

POLITICAL CONTROL
election -> confidence -> debate/committee -> convention -> federal bargaining
-> public accountability.

CONVENTION
non-judicial rule of constitutional behaviour;
politically obligatory but not automatically enforceable as law.

INDIAN SYNTHESIS
supreme written Constitution + parliamentary responsibility + conventions.

[LIMIT] Courts may enforce legal structure, not every preferred political convention.""",
        ),
        (
            "Sovereignty and legitimacy",
            """POPULAR SOVEREIGNTY
"We, the People" -> democratic authorship and consent.

PARLIAMENTARY SOVEREIGNTY
classic UK idea -> legally unlimited legislature.

CONSTITUTIONAL SOVEREIGNTY IN INDIA
people authorise Constitution -> Parliament legislates/amends within it
-> executive is responsible -> courts review -> federal units retain protected fields.

LEGITIMACY
source of authority + fair procedure + rights + accountable performance.

[LIMIT] Electoral victory supplies governing authority, not a power to erase constitutional limits.""",
        ),
        (
            "Constitutional morality and transformative constitutionalism",
            """CONSTITUTIONAL MORALITY
fidelity to text + forms + procedures + institutional role + equal citizenship.

TRANSFORMATIVE CONSTITUTIONALISM
rights + dignity + social justice + anti-hierarchy commitments
-> lawful institutional transformation.

CASE ARC
S.R. Bommai (1994) -> secular/federal limits;
Navtej Singh Johar (2018) -> dignity, equality and constitutional morality.

CONTROL
anchor every morality claim in identifiable text, structure or precedent.

[LIMIT] Neither doctrine is a licence for personal judicial or political morality.""",
        ),
        (
            "Living constitution and interpretive discipline",
            """TEXT AND ORIGINAL MEANING
language/history constrain interpretation.

STRUCTURE AND PRECEDENT
institutional relationships + accumulated doctrine support coherence.

LIVING APPLICATION
enduring principle -> new circumstance -> reasoned extension.

CASE ARC
Maneka Gandhi (1978) -> fair procedure;
K.S. Puttaswamy (2017) -> privacy/dignity in a technological society.

[LIMIT] Dynamism must explain the textual principle, institutional competence and remedy.""",
        ),
        (
            "Constitutional identity, amendment and failure",
            """IDENTITY
Preamble values + democracy + rights + federalism + responsibility
+ judicial review + social transformation.

AMENDMENT
adaptation -> continuity;
Minerva Mills (1980) -> limited power and rights-DPSP harmony.

FAILURE MODES
emergency abuse | rights hollowing | captured institutions | broken conventions
| majority treated as unlimited authority.

RESPONSE
review + Parliament + federal checks + elections + public reason + lawful amendment.

[LIMIT] Identity is structured continuity, not a judicially frozen policy code.""",
        ),
    ],
    "polity-51": [
        (
            "Succession after commencement and reorganisation",
            """ARTICLES 294-295
constitutional commencement -> property/assets/rights/liabilities continue
-> Union/State successor identified by constitutional field and purpose.

LATER REORGANISATION
reorganisation statute/agreement -> apportion land, undertakings, debt, guarantees
-> allocate employees/pensions -> substitute parties in pending proceedings
-> continue or adapt contracts, licences and records.

[LIMIT] Articles 294-295 do not supply one permanent formula for every later territorial change.""",
        ),
        (
            "Section 70 restitution and quantum meruit",
            """ARTICLE 299 DEFECT
no enforceable government contract merely by consent/performance.

CONTRACT ACT SECTION 70
lawful act/delivery + non-gratuitous intention + government enjoys benefit
-> restitutionary compensation for proved benefit.

B.K. Mondal & Sons (1961)
supports independent non-gratuitous-benefit liability.

Mulamchand v. State of Madhya Pradesh (1968)
keeps mandatory Article 299 form distinct from restitution.

[LIMIT] Section 70 does not validate the void contract or automatically award its price.""",
        ),
        (
            "Article 300 suits and CPC Sections 79-80",
            """PROPER PARTY
Union transaction -> Union of India;
State transaction -> State by its legal name.

CPC SECTION 79
procedural naming of the governmental defendant/plaintiff.

CPC SECTION 80
ordinary suit concerning official act -> statutory two-month prior notice;
urgent/immediate relief -> court-controlled exception under Section 80(2).

[LIMIT] Notice is a procedural precondition with statutory exceptions, not sovereign immunity.""",
        ),
        (
            "Sovereign-immunity trajectory in private tort",
            """            P & O Steam Navigation (1861)
-> sovereign/non-sovereign colonial distinction.

State of Rajasthan v. Vidyawati (1962)
-> liability for ordinary operational negligence.

Kasturi Lal v. State of Uttar Pradesh (1964)
-> older immunity for police sovereign function.

N. Nagendra Rao & Co. (1994)
-> welfare State makes broad immunity untenable; any residue is narrow.

VERDICT
no blanket immunity; identify function, duty, remedy and controlling authority.""",
        ),
        (
            "Constitutional tort and public-law compensation",
            """Rudul Sah v. State of Bihar (1983)
-> compensation for unlawful detention under writ jurisdiction.

Nilabati Behera v. State of Orissa (1993)
-> public-law compensation for Fundamental-Right violation
is distinct from private tort damages.

State of Andhra Pradesh v. Challa Ramkrishna Reddy (2000)
-> rule-of-law accountability rejects broad immunity for prison-rights harm.

[LIMIT] Constitutional compensation does not decide every private damages issue or replace trial.""",
        ),
        (
            "Vicarious liability, act of State and official protection",
            """VICARIOUS LIABILITY
employee tort in course of employment -> possible governmental liability
subject to function, duty, causation and defence.

ACT OF STATE
external sovereign dealing historically distinguished from ordinary domestic administration.

ARTICLE 361
personal protection for President/Governor during office;
governmental action remains reviewable through proper proceedings.

[LIMIT] Article 299 signatory protection, Article 361 immunity, sanction and CPC notice differ.""",
        ),
        (
            "Government property, Article 300A and eminent domain",
            """GOVERNMENT PROPERTY
acquire/hold/dispose under Article 298 -> statute, budget, public trust and audit controls.

PRIVATE PROPERTY
Article 300A -> deprivation only by authority of law.

EMINENT DOMAIN
public acquisition -> legislative authority + public purpose framework
-> compensation according to governing constitutional/statutory doctrine.

[LIMIT] Article 300A is not the source of Article 299 contracts or Article 300 suits.""",
        ),
        (
            "Procurement, arbitration and accountable contracting",
            """PROCUREMENT
need -> sanction -> fair specification -> competition -> reasoned award
-> Article 299 execution -> performance/payment -> CAG/audit.

ARBITRATION
valid authorised clause -> tribunal -> award -> statutory challenge/enforcement.

CURRENT ANCHOR
GeM is a dated digital procurement mechanism; manuals/platform rules do not amend
the Constitution, CPC, Contract Act or Arbitration and Conciliation Act 1996.

[LIMIT] A reform proposal or model clause is not enacted law.""",
        ),
    ],
}


PYQS: dict[str, list[dict[str, Any]]] = {
    "polity-48": [
        {
            "label": "Verified direct PYQ",
            "year": 2025,
            "paper": "Prelims GS-I Q57",
            "question": (
                "With reference to India, consider the pairs: National Automotive "
                "Board-Ministry of Commerce and Industry; Coir Board-Ministry of "
                "Heavy Industries; National Centre for Trade Information-Ministry "
                "of Micro, Small and Medium Enterprises. How many are correctly matched?"
            ),
            "directive": "Objective close-option classification",
            "marks": 2,
            "words": "objective",
            "points": [
                "The official Set-A key is D: none of the three displayed pairings is correct.",
                "National Automotive Board belongs to the Heavy Industries subject field.",
                "Coir Board belongs to the MSME subject field under its statutory/allocated business.",
                "NCTI belongs to the Commerce and Industry subject field.",
                "The method is to identify the parent statute/allocated subject, not infer from the name.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2020,
            "paper": "GS-II Q7",
            "question": (
                "Suggest civil-service reforms required to strengthen democracy by "
                "improving institutional quality."
            ),
            "directive": "Suggest reforms",
            "marks": 10,
            "words": 150,
            "points": [
                "Institutional quality depends on competent departments, recorded advice and lawful responsibility.",
                "Minister-Secretary complementarity joins democratic direction to professional continuity.",
                "Stable tenure, domain capability, delegation and field feedback reduce policy failure.",
                "Digital files improve traceability only when authority and reasons remain clear.",
                "Civil-service reform must be linked to departmental process, outcomes and parliamentary scrutiny.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2024,
            "paper": "GS-II Q3",
            "question": (
                "The growth of cabinet system has practically resulted in the "
                "marginalisation of parliamentary supremacy. Elucidate."
            ),
            "directive": "Elucidate",
            "marks": 10,
            "words": 150,
            "points": [
                "Ministries control policy information, drafting, delegated legislation and budget preparation.",
                "Cabinet solidarity and party discipline can reduce independent legislative influence.",
                "Questions, committees, demands for grants and audit remain constitutional correctives.",
                "The claim concerns executive dominance, not British-style legal parliamentary sovereignty in India.",
                "A balanced answer seeks stronger scrutiny without disabling responsible government.",
            ],
        },
    ],
    "polity-49": [
        {
            "label": "Verified direct PYQ",
            "year": 2018,
            "paper": "Prelims GS-I Q4",
            "question": (
                "How is the National Green Tribunal different from the Central "
                "Pollution Control Board, with reference to their legal source and functions?"
            ),
            "directive": "Objective statement evaluation",
            "marks": 2,
            "words": "objective",
            "points": [
                "NGT is a statutory adjudicatory tribunal under the NGT Act 2010.",
                "CPCB is also statutory, principally under the Water Act 1974, not an executive-order body.",
                "NGT provides environmental adjudication and relief within statutory jurisdiction.",
                "CPCB performs pollution-control regulation, standards, monitoring and enforcement functions.",
                "The tested distinction is tribunal versus regulator, not statutory versus executive.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2018,
            "paper": "Prelims GS-I Q23",
            "question": (
                "Consider statements on the Food Safety and Standards Act 2006 "
                "replacing the Prevention of Food Adulteration Act 1954 and on "
                "whether FSSAI is under the Director General of Health Services."
            ),
            "directive": "Objective statement evaluation",
            "marks": 2,
            "words": "objective",
            "points": [
                "The 2006 Act consolidated and replaced the earlier food-adulteration framework.",
                "FSSAI is a statutory authority under the Union health ministry's administrative field.",
                "It is not a subordinate office under the Director General of Health Services.",
                "Administrative ministry, statutory identity and internal departmental control are separate axes.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2023,
            "paper": "GS-II Q7",
            "question": (
                "Discuss the role of the Competition Commission of India in containing "
                "the abuse of dominant position by multinational corporations in India. "
                "Refer to recent decisions."
            ),
            "directive": "Discuss",
            "marks": 10,
            "words": 150,
            "points": [
                "Dominance is not prohibited; abuse in a properly defined relevant market is.",
                "CCI investigates, hears and orders under the Competition Act with statutory appeal to NCLAT.",
                "Market access, unfair conditions, leveraging and exclusionary conduct require evidence.",
                "Digital markets intensify network-effect, data and self-preferencing concerns.",
                "Enforcement must remain reasoned, proportionate and judicially reviewable.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2025,
            "paper": "Prelims GS-I Q60",
            "question": (
                "How many among crude-oil production; petroleum refining, storage "
                "and distribution; petroleum-product marketing and sale; and natural-gas "
                "production are regulated by the Petroleum and Natural Gas Regulatory Board?"
            ),
            "directive": "Objective jurisdiction test",
            "marks": 2,
            "words": "objective",
            "points": [
                "The official Set-A key is B: only two listed activities fall within the tested PNGRB field.",
                "Downstream refining/storage/distribution and marketing/sale are within the regulatory map.",
                "Upstream crude-oil and natural-gas production are not converted into PNGRB functions.",
                "Regulatory jurisdiction must be read from the parent Act, not the sector's broad name.",
            ],
        },
    ],
    "polity-50": [
        {
            "label": "Supporting routed PYQ",
            "year": 2021,
            "paper": "GS-II Q1",
            "question": (
                "Constitutional Morality is rooted in the Constitution itself and "
                "is founded on its essential facets. Explain with relevant judicial decisions."
            ),
            "directive": "Explain",
            "marks": 10,
            "words": 150,
            "points": [
                "Define constitutional morality as fidelity to forms, procedures, values and institutional roles.",
                "Anchor it in the Preamble, rights, responsibility, federalism and judicial review.",
                "Use S.R. Bommai (1994) and Navtej Singh Johar (2018) as bounded illustrations.",
                "It protects minorities and institutional good faith against raw majoritarianism.",
                "It must remain tied to text and structure rather than personal morality.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2023,
            "paper": "GS-II Q11",
            "question": (
                "The Constitution of India is a living instrument with capabilities "
                "of enormous dynamism and is made for a progressive society. Illustrate "
                "with the expanding horizons of life and personal liberty."
            ),
            "directive": "Illustrate",
            "marks": 15,
            "words": 250,
            "points": [
                "A living constitution applies enduring textual principles to new conditions.",
                "Maneka Gandhi (1978) transformed procedure into a fair, just and reasonable guarantee.",
                "K.S. Puttaswamy (2017) applied dignity and liberty to informational privacy.",
                "Dynamic interpretation remains bounded by text, structure, precedent and institutional competence.",
                "Amendment and democratic lawmaking complement rather than disappear before interpretation.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2025,
            "paper": "GS-II Q11",
            "question": (
                "Explain constitutional morality and its application in balancing "
                "judicial independence with judicial accountability in India."
            ),
            "directive": "Explain",
            "marks": 15,
            "words": 250,
            "points": [
                "Constitutional morality protects decisional independence and rejects executive intimidation.",
                "It also requires transparent institutional procedure, reasons and ethical responsibility.",
                "Appointments, recusal, disclosure and removal rules operationalise the balance.",
                "Accountability must not become control of judgments; independence must not become insulation from standards.",
                "The doctrine is a role-based constitutional discipline for judges and other high functionaries.",
            ],
        },
    ],
    "polity-51": [
        {
            "label": "Supporting routed PYQ",
            "year": 2025,
            "paper": "Prelims GS-I Q59",
            "question": (
                "Evaluate statements on a Governor's answerability to courts, the "
                "bar on criminal proceedings during the term, and legislative immunity "
                "for words spoken inside a State Legislature."
            ),
            "directive": "Objective immunity-source distinction",
            "marks": 2,
            "words": "objective",
            "points": [
                "The official Set-A key is D: all three constitutional statements are correct.",
                "Article 361 protects the Governor personally for official powers and during the term.",
                "Article 194 protects legislative speech/vote within the constitutional privilege field.",
                "These personal/legislative protections do not create blanket governmental immunity.",
                "Article 299, Article 300, CPC notice and criminal sanction arise from different sources.",
            ],
        },
    ],
}


FACTS: dict[str, list[tuple[str, str, list[str], str]]] = {
    "polity-48": [
        ("Article 73", "Union executive power broadly follows Parliament's legislative field, subject to constitutional federal limits.", ["It personally vests every decision in the President.", "It creates the Cabinet Secretariat.", "It is the rule-making source for civil-service recruitment."], "Article 73 defines executive reach, not the complete internal machinery."),
        ("Articles 74 and 78", "Article 74 establishes aid and advice; Article 78 imposes Prime Ministerial communication and information duties to the President.", ["Article 78 allocates departments among Secretaries.", "Article 74 makes the PMO a constitutional body.", "Article 78 creates Cabinet Committees."], "The provisions govern the parliamentary executive relationship."),
        ("Allocation versus Transaction Rules", "AoB identifies who handles a subject; ToB prescribes how consultation, disposal and escalation occur.", ["AoB and ToB are rules under Article 309.", "AoB prescribes only Cabinet meeting procedure.", "ToB permanently fixes ministry names."], "Both arise under Article 77(3) but answer different questions."),
        ("ministry and department", "A ministry is the broader political-administrative unit; a department is an allocated subject unit generally headed administratively by a Secretary.", ["Every ministry has exactly one department.", "A department is always a statutory corporation.", "A portfolio and department are synonyms."], "Political charge, allocated business and administrative structure must be separated."),
        ("Minister and Secretary", "The Minister supplies democratic direction and parliamentary answerability; the Secretary supplies administration, advice, legality and continuity.", ["The Secretary is a parallel political executive.", "The Minister cannot seek professional advice.", "Ministerial responsibility erases official accountability."], "Responsive neutrality requires candid advice and lawful implementation."),
        ("Central Secretariat", "The Central Secretariat collectively supports policy, legislation, budgeting, coordination, monitoring and institutional memory.", ["It is another name for the Cabinet Secretariat.", "It performs only field delivery.", "It is a single constitutional office."], "It is collective policy machinery across departments."),
        ("Cabinet Secretariat and PMO", "The Cabinet Secretariat services collective Cabinet government; the PMO supports the Prime Minister directly.", ["Both are constitutional commissions.", "The PMO is custodian of Cabinet records by definition.", "The Cabinet Secretary is a political minister."], "Different centre-of-government roles must not be collapsed."),
        ("delegation and files", "Routine work should be disposed at the lowest competent delegated level with recorded authority, consultation and reasons.", ["Every file must reach the Secretary.", "Oral approval permanently replaces record.", "Delegation removes ministerial accountability."], "Delegation prevents apex overload while retaining traceability."),
        ("attached and subordinate offices", "Attached offices provide detailed executive/technical direction; subordinate offices commonly execute in the field.", ["Both are independent constitutional bodies.", "Attached offices necessarily adjudicate.", "Subordinate offices cannot exercise delegated statutory power."], "Labels indicate administrative relation, not identical legal power."),
        ("autonomous bodies CPSEs regulators", "Autonomous bodies, CPSEs and regulators have distinct instruments, purposes and accountability regimes.", ["All are departments under Article 77.", "A ministry may override any statutory regulator order.", "A CPSE is automatically a constitutional body."], "Stewardship and ownership do not erase legal autonomy."),
        ("oversight", "Parliamentary committees, demands for grants, CAG, RTI, courts and vigilance provide different accountability routes.", ["CAG directly dismisses officials.", "RTI removes every lawful exemption.", "Committee recommendations are judicial decrees."], "Political, financial, transparency and legal controls are complementary."),
        ("reorganisation", "Ministries and departments may be renamed, merged or split through the business-rule framework, subject to statutes and transition requirements.", ["Every reorganisation needs Article 368.", "A renamed ministry automatically amends all statutes.", "The number of ministries is constitutionally fixed."], "Current organisation is notification-sensitive and must be dated."),
    ],
    "polity-49": [
        ("three classification axes", "Statutory identifies source, regulatory identifies function and quasi-judicial identifies the character of a particular decision.", ["Every statutory body is regulatory.", "Every regulator is always quasi-judicial.", "Every commission is constitutional."], "The axes overlap but are not synonyms."),
        ("regulatory state", "Liberalisation can reduce direct production while increasing specialised rule-setting, supervision and market correction.", ["Regulation means absence of the State.", "Only public monopolies need regulation.", "A regulator must be constitutional."], "The State shifts from owner-command toward rule-governance."),
        ("delegated legislation", "A regulator may make rules or regulations only within the parent statute and cannot receive abdicated essential legislative power.", ["Delegation permits amendment of the Constitution.", "Consultation cures lack of statutory power.", "Every regulation is a judicial order."], "Authority, purpose, procedure and review control delegation."),
        ("functional cycle", "Regulators may combine rule-making, licensing, monitoring, investigation, enforcement and adjudication under statute.", ["All functions use identical procedure.", "Licensing is necessarily a court function.", "Monitoring removes the need for hearing before penalty."], "Safeguards intensify as individual rights and sanctions are affected."),
        ("natural justice", "Notice, opportunity to be heard, absence of bias and reasons ordinarily control adverse quasi-judicial action.", ["Natural justice always requires full CPC trial.", "Urgency permanently removes fairness.", "Reasons are irrelevant when appeal exists."], "Fairness is flexible but arbitrariness is not."),
        ("tribunal regulator court", "A tribunal mainly adjudicates specialised disputes; a regulator governs a sector and may sometimes adjudicate; constitutional courts retain review.", ["A regulator and its appellate tribunal are the same.", "A tribunal is always an executive department.", "High Court review can be eliminated by naming a tribunal."], "Institutional role and appeal chain must be stated separately."),
        ("independence design", "Appointment, tenure, for-cause removal, finance, staff and decisional non-interference together determine independence.", ["One fixed term guarantees independence.", "Fee funding eliminates capture.", "Ministerial policy guidance may dictate case outcomes."], "De jure and de facto independence may diverge."),
        ("capture", "Industry, political, bureaucratic, informational and cognitive capture arise through different incentive channels.", ["Capture requires criminal bribery.", "More insulation always prevents capture.", "Consumer interests are always concentrated."], "Use a portfolio of transparency, conflict and appeal safeguards."),
        ("appeals and review", "A statutory merits appeal differs from constitutional judicial review of legality, jurisdiction, fairness and rights.", ["Judicial review always retries facts de novo.", "An appeal automatically excludes Article 226.", "A regulator's order is final if statute says so."], "L. Chandra Kumar preserves the constitutional review floor."),
        ("accountability", "Parent statutes, Parliament, CAG where applicable, RTI, consultation, annual reports, appeals and courts constrain regulators.", ["Independent means beyond Parliament.", "RTI converts recommendations into orders.", "CAG decides sector tariffs."], "Autonomy from case-specific control coexists with public answerability."),
        ("digital regulation", "Digital harms may engage competition, data, consumer, sector and cyber laws through distinct legal instruments.", ["A consultation paper is enacted law.", "Every digital platform is a public utility.", "Data concentration proves abuse without market analysis."], "Instrument and status must be dated and legally identified."),
        ("reform", "Clear mandates, impact assessment, consultation, conflict controls, functional separation and coherent appeals improve legitimacy.", ["A super-regulator always removes overlap.", "Consultation makes all comments binding.", "Regulatory independence requires no reporting."], "Reform must diagnose the specific failure mechanism."),
    ],
    "polity-50": [
        ("constitution definition", "A constitution creates institutions, allocates and limits power, protects rights and identifies the political community.", ["It is only a list of government offices.", "It is identical to every ordinary statute.", "It concerns rights but not public power."], "Constitutive and restraining functions operate together."),
        ("constitutionalism", "Constitutionalism requires limited, accountable and legally reviewable government, not merely possession of a constitutional document.", ["Every written constitution guarantees constitutionalism.", "Constitutionalism means judicial supremacy.", "It excludes democratic government."], "Effective restraint depends on institutions, rights and remedies."),
        ("constitutional law", "Constitutional law includes the text plus binding interpretation, statutes, rules and doctrines governing public power.", ["It is narrower than the document alone.", "Every convention is enforceable law.", "Ordinary law is constitutionally supreme."], "The Constitution is foundational; constitutional law is the wider field."),
        ("classification", "Written/uncodified, rigid/flexible, federal/unitary and supreme/parliamentary classify different dimensions.", ["Written always means rigid.", "Federal always means presidential.", "Uncodified means no written sources."], "Do not infer one axis from another."),
        ("constituent power", "Constituent power founds the order; constituted institutions exercise powers conferred by that order.", ["Parliament's ordinary majority is original constituent power.", "Courts possess unlimited constituent authority.", "Executive convention overrides the Constitution."], "Article 368 is broad but constitutionally bounded."),
        ("rule of law", "Rule of law requires authorised, non-arbitrary, equally applied and reviewable public power.", ["It prohibits all discretion.", "It applies only to courts.", "A majority vote cures unconstitutional action."], "Discretion must be structured rather than eliminated."),
        ("sovereignty", "India combines popular authorship with constitutional supremacy; Parliament is not sovereign in the classic British legal sense.", ["Courts are politically sovereign.", "States possess external sovereignty.", "Popular sovereignty makes amendment procedure unnecessary."], "Every institution is constituted and limited."),
        ("conventions", "Conventions guide constitutional behaviour without automatically becoming judicially enforceable law.", ["Conventions amend text silently.", "Every repeated practice is a convention.", "Courts must enforce all conventions."], "Political obligation and legal enforceability differ."),
        ("constitutional morality", "Constitutional morality is fidelity to constitutional forms, procedures, values and institutional roles.", ["It means a judge's personal morality.", "It permits ignoring text for desirable outcomes.", "It binds only citizens and not offices."], "Claims must be anchored in text and structure."),
        ("transformative constitutionalism", "Transformative constitutionalism uses rights, dignity and social-justice commitments to change entrenched hierarchy through lawful institutions.", ["It abolishes separation of powers.", "It makes every DPSP directly enforceable.", "It rejects institutional restraint."], "Transformation remains competence- and remedy-bounded."),
        ("living constitution", "Living interpretation applies enduring principles to new circumstances through text, structure, precedent and reasons.", ["It authorises amendment by judgment.", "Original meaning is legally irrelevant in every case.", "Every new social claim becomes a right."], "Dynamism requires a disciplined interpretive bridge."),
        ("basic structure identity", "Basic structure permits amendment while preventing destruction of constitutional identity.", ["It is an express constitutional schedule.", "It freezes every policy.", "It makes Article 368 unusable."], "Identity protects foundational design, not a closed policy code."),
    ],
    "polity-51": [
        ("Articles 294 and 295", "These provisions continue and allocate commencement-era property, rights, liabilities and obligations between Union and States.", ["They create the current procurement code.", "They govern only private inheritance.", "They abolish later reorganisation statutes."], "They are succession and continuity provisions."),
        ("Article 296", "Escheat, lapse and bona vacantia generally vest ownerless property by location, subject to the constitutional proviso.", ["It is the eminent-domain article.", "It governs government contracts.", "All ownerless property vests in the Union."], "Location and prior governmental purpose matter."),
        ("Article 298", "Union and State executive power extends to trade, business, property and contracts, subject to legislative-field provisos.", ["It exempts government companies from ordinary law.", "It personally contracts through the President.", "It creates sovereign immunity."], "Capacity does not remove statutory or rights controls."),
        ("Article 299 form", "Government contracts must be expressed in the President/Governor's name, executed on their behalf and by authorised persons/manner.", ["Substantial compliance always cures missing authority.", "The President becomes personally liable.", "An oral promise binds the exchequer automatically."], "The formalities are mandatory public-fund safeguards."),
        ("Section 70 restitution", "A lawful non-gratuitous act whose benefit government enjoys may found restitution independently of an invalid contract.", ["Section 70 validates the Article 299-defective contract.", "It requires no proof of benefit.", "It always awards the quoted contract price."], "Contract enforcement and restitution are distinct."),
        ("Article 300 party", "The Union sues or is sued as Union of India; a State uses the name of the State.", ["Every ministry is a separate constitutional defendant.", "The President must be personally impleaded.", "Article 300 bars tort suits."], "Correct party naming reflects governmental legal personality."),
        ("CPC Sections 79 and 80", "Section 79 governs party description; Section 80 ordinarily requires two-month notice before specified government/official suits, with an urgent-relief exception.", ["Section 80 is blanket sovereign immunity.", "Notice is never required.", "Section 79 creates Article 299 authority."], "These are procedural rules distinct from substantive liability."),
        ("private tort trajectory", "The colonial sovereign-function distinction has been narrowed as welfare-State operations expanded.", ["Kasturi Lal abolished immunity.", "Nagendra Rao restored blanket immunity.", "Every policy decision creates damages."], "Identify function, duty, causation and modern authority."),
        ("constitutional tort", "Writ courts may award public-law compensation for Fundamental-Right violations, distinct from private damages.", ["It validates an invalid contract.", "It requires no State action.", "It replaces every civil trial."], "The remedy vindicates constitutional rights."),
        ("vicarious liability", "Government may answer for employee torts in the course of employment while personal and disciplinary responsibility remain separately possible.", ["State liability always excludes officer liability.", "Every private act binds the State.", "Good faith automatically defeats all claims."], "Employment nexus, function and statutory protection matter."),
        ("Article 300A", "No person may be deprived of property except by authority of law; it is distinct from Articles 294-300 liability mechanics.", ["It is a Fundamental Right in Part III.", "It authorises all government contracts.", "Executive instruction alone is always authority of law."], "Property deprivation requires legal authority."),
        ("procurement and arbitration", "Fair procurement, authorised Article 299 execution, audit and a valid arbitration clause create accountable dispute resolution.", ["GeM replaces Article 299.", "Arbitration removes judicial supervision entirely.", "A draft amendment changes current law."], "Platform, manual, contract and statute must be distinguished."),
    ],
}


MAINS_PROMPTS: dict[str, list[tuple[int, str, str]]] = {
    "polity-48": [
        (10, "Distinguish a ministry, department, secretariat and attached office in the Union Government.", "Distinguish"),
        (10, "Explain the constitutional and rules-of-business basis of Union ministries and departments.", "Explain"),
        (15, "Examine the Minister-Secretary relationship as the hinge between democratic control and administrative continuity.", "Examine"),
        (15, "Analyse how the Cabinet Secretariat secures inter-ministerial coordination without becoming a super-ministry.", "Analyse"),
        (20, "Discuss the functions, internal process and accountability architecture of the Central Secretariat.", "Discuss"),
        (20, "Critically evaluate centralisation, silos and delegation in the Union machinery of government.", "Critically evaluate"),
        (15, "Assess the role and limits of mission-mode units, digital files and lateral expertise in departmental government.", "Assess"),
        (20, "Propose a reform framework for reorganising ministries while preserving statutory continuity and accountability.", "Propose"),
    ],
    "polity-49": [
        (10, "Distinguish statutory, regulatory and quasi-judicial bodies.", "Distinguish"),
        (10, "Explain why a regulator is not quasi-judicial in all its functions.", "Explain"),
        (15, "Examine natural justice as the constitutional discipline of regulatory adjudication.", "Examine"),
        (15, "Analyse the independence-accountability balance in sector regulators.", "Analyse"),
        (20, "Discuss the regulatory cycle from delegated rule-making to appeal and judicial review.", "Discuss"),
        (20, "Critically evaluate the combination of investigation, enforcement and adjudication in one regulator.", "Critically evaluate"),
        (15, "Assess regulatory capture and the safeguards required against its different forms.", "Assess"),
        (20, "Design a coherent reform architecture for data, digital and platform regulation without treating proposals as law.", "Design"),
    ],
    "polity-50": [
        (10, "Distinguish a constitution from constitutionalism.", "Distinguish"),
        (10, "Explain the constitutive and restraining functions of a constitution.", "Explain"),
        (15, "Examine constituent power and the limits of constituted institutions in India.", "Examine"),
        (15, "Analyse popular, parliamentary and constitutional sovereignty in the Indian order.", "Analyse"),
        (20, "Discuss constitutional morality and transformative constitutionalism with appropriate limits.", "Discuss"),
        (20, "Critically evaluate living-constitution and original-meaning approaches in Indian interpretation.", "Critically evaluate"),
        (15, "Assess how conventions connect India's legal and political constitution.", "Assess"),
        (20, "Explain Indian constitutional identity through the Preamble, basic structure, social revolution and institutional restraint.", "Explain"),
    ],
    "polity-51": [
        (10, "Map the rights, property and liability provisions in Articles 294 to 300.", "Map"),
        (10, "Explain the mandatory requirements and consequences of Article 299 government contracts.", "Explain"),
        (15, "Distinguish an enforceable government contract from restitution under Contract Act Section 70.", "Distinguish"),
        (15, "Examine Article 300 with CPC Sections 79 and 80 in suits against government.", "Examine"),
        (20, "Trace the evolution of sovereign immunity in Indian tort law and state the present qualified position.", "Trace"),
        (20, "Analyse the distinction between private tort liability and constitutional-tort compensation.", "Analyse"),
        (15, "Assess vicarious liability, official protection and the act-of-State distinction.", "Assess"),
        (20, "Discuss public procurement and arbitration as instruments of accountable governmental contracting.", "Discuss"),
    ],
}


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-48": [
        (
            "Constitutional root and the operating chain",
            "constitutional-chain",
            [],
            """ROOT QUESTION
How does parliamentary executive authority become organised governmental action?

+-- ARTICLES 73 + 74 --+-- Union executive field and ministerial advice
|                     +-- political authority remains Constitution-bounded
+-- ARTICLE 77 --------+-- action in President's name and authentication
|                     +-- Article 77(3) business-allocation and transaction rules
+-- ARTICLE 78 ----------- PM communication and information duties to President
                              |
                              v
Ministerial direction -> Secretariat advice/process -> agency delivery -> accountability.""",
        ),
        (
            "AoB and ToB: jurisdiction before procedure",
            "rules-of-business-matrix",
            [],
            """                    ARTICLE 77(3)
                         +----------+----------+
                         v                     v
ALLOCATION OF BUSINESS RULES             TRANSACTION OF BUSINESS RULES
who handles what                         how a proposal is decided
ministry/department + subjects           disposal + consultation + escalation
                         +----------+----------+
                                    v
                 lawful owner + lawful decision route

TRAP RAIL
AoB != ToB | both != Article 309 | schedule can change | statute still controls.

ANSWER STRIP
Allocation supplies jurisdiction; transaction supplies procedure and collective discipline.""",
        ),
        (
            "Institution map: political head to field delivery",
            "institution-hierarchy",
            [],
            """PORTFOLIO -> MINISTRY -> DEPARTMENT -> SECRETARIAT
     |           |             |              |
 political      broad          allocated       policy/law/budget/
 charge         unit           subject unit    coordination/memory
                                    |
                    +---------------+----------------+
                    v               v                v
              ATTACHED OFFICE  SUBORDINATE OFFICE  FIELD/DIRECTORATE
              technical lead   execution/service   territorial chain

SEPARATE LEGAL FORMS
statutory body | autonomous body | CPSE | regulator.

TRAP
administrative association does not erase the source instrument or statutory independence.""",
        ),
        (
            "Minister, Minister of State and Secretary",
            "role-responsibility-matrix",
            [],
            """POLITICAL EXECUTIVE
Cabinet Minister -> portfolio leadership, Cabinet participation, Parliament.
Minister of State -> independent charge or assigned assistance, as formally allocated.

PERMANENT EXECUTIVE
Secretary -> administrative head + principal official adviser + transaction compliance.

                     PRODUCTIVE RELATION
elected priority -> candid options/legality -> recorded decision -> loyal implementation.

FAILURE BRANCHES
politicised advice | bureaucratic veto | oral direction | short tenure | hidden responsibility.

ANSWER STRIP
Responsive neutrality joins lawful democratic control to professional institutional memory.""",
        ),
        (
            "Central Secretariat functions and file process",
            "file-process-system",
            [],
            """CENTRAL SECRETARIAT
policy | legislation/rules | budget | Parliament | coordination | monitoring | records.

FILE RAIL
receipt -> section examination -> facts/law/finance -> noting/options
-> inter-department consultation -> delegated or higher approval
-> authentication/issue -> implementation -> monitoring/audit/RTI.

HIERARCHY
Section Officer -> Under Secretary -> Deputy Secretary/Director
-> Joint Secretary -> Additional/Special Secretary -> Secretary.

TRAP
not every file reaches Minister/Secretary; delegation is an accountability design, not evasion.""",
        ),
        (
            "Cabinet Secretariat, PMO and coordination",
            "centre-of-government-comparison",
            [],
            """CABINET SECRETARIAT
Cabinet papers/decisions | AoB-ToB administration | CoS | crisis and consensus.

PMO
direct assistance to Prime Minister | priority review | matters requiring PM attention.

                     UNRESOLVED DIFFERENCE
department consultation -> Committee of Secretaries -> concerned ministers
-> Cabinet Committee/Cabinet under the prescribed route.

BOUNDARY
Cabinet Secretariat != Cabinet | PMO != super-ministry | Cabinet Secretary != minister.

ANSWER STRIP
Central coordination should enable departments without erasing ministerial answerability.""",
        ),
        (
            "Agencies, autonomy and whole-of-government outcomes",
            "agency-outcome-map",
            [],
            """DEPARTMENTAL POLICY OWNER
      +-- attached/subordinate office -> technical/field execution
      +-- autonomous body -> chartered special function
      +-- CPSE -> commercial/strategic operation
      +-- regulator -> statute-based arm's-length governance

WHOLE-OF-GOVERNMENT PROBLEM
climate/data/skills/water -> many departments -> silo optimisation -> outcome failure.

CORRECTIVE
named lead + shared milestones/data + funds/functionaries + State/field feedback.

LIMIT
mission unit or dashboard cannot displace statute, sanction, Cabinet route or audit.""",
        ),
        (
            "Oversight, reform and notification-sensitive change",
            "accountability-reform-grid",
            [],
            """ACCOUNTABILITY GRID
Parliament/questions/DRSCs -> political and policy scrutiny.
budget/demands/CAG/PAC -> financial legality, propriety and performance.
RTI/courts/vigilance -> transparency, legality and personal responsibility.

REFORM
2nd ARC principles | delegation | competency-to-post fit | Mission Karmayogi
| digital record | impact evaluation | stable tenure | specialist/lateral support.

REORGANISATION
Article 77(3) rule change -> cadres/budgets/records/contracts/statutory references transition.

TRAP
renamed organogram != improved outcome; ministry/committee counts must be dated.""",
        ),
        (
            "UPSC synthesis: organised authority with traceable responsibility",
            "answer-synthesis",
            [],
            """PRELIMS FIREWALL
AoB=owner | ToB=route | President's name != personal decision
| Secretariat != Cabinet Secretariat | Cabinet Committee != Committee of Secretaries
| attached office != autonomous body | regulator autonomy survives ordinary instruction.

MAINS SPINE
Articles 73/74/77/78 -> AoB-ToB -> ministry/department
-> Minister-Secretary -> Secretariat/file -> coordination
-> agencies/outcomes -> oversight -> reform.

PYQ SPINE
2025 organisation-ministry pairs -> verify allocated subject and parent law.

VERDICT
effective machinery aligns functions, funds, functionaries, expertise and answerability.""",
        ),
    ],
    "polity-49": [
        (
            "Why the regulatory state emerged",
            "regulatory-rationale-map",
            [],
            """ROOT QUESTION
How can the State govern complex markets and rights without daily ministerial case control?

LIBERALISATION/SPECIALISATION
less direct production -> more rule-setting, network access, prudential oversight
-> consumer/competition protection -> specialised enforcement and adjudication.

+-- MARKET FAILURES ----- monopoly | information asymmetry | externality | systemic risk
+-- GOVERNANCE NEEDS ---- expertise | continuity | credible commitment | rapid updating
+-- CONSTITUTIONAL NEED - mandate | fairness | reasons | appeal | review | accountability

VERDICT
Regulation is a change in State technique, not disappearance of the State.""",
        ),
        (
            "Source, function and decisional character",
            "three-axis-taxonomy",
            [],
            """                         BODY / AUTHORITY
              +--------------+---------------+----------------+
              v              v               v
LEGAL SOURCE             PRIMARY FUNCTION   CHARACTER OF ACT
constitutional           regulatory         quasi-legislative rule
statutory                advisory           administrative inquiry
executive                investigative      quasi-judicial order

EXAMPLES
RBI/SEBI/TRAI/CERC/IRDAI/CCI -> statutory regulators with different mandates.

MASTER TRAP
one body may occupy several boxes; it is not quasi-judicial in every function.""",
        ),
        (
            "Regulatory cycle and separation problem",
            "regulatory-cycle",
            [],
            """PARENT ACT
   v
regulation/standard -> licence/tariff -> data/monitoring -> investigation
   v
show-cause notice -> hearing -> reasoned order/penalty -> statutory appeal
   v
High Court/Supreme Court constitutional review.

CONCENTRATION RISK
make rule + investigate + prosecute + decide -> confirmation bias/self-vindication.

SAFEGUARDS
separate wings | disclosure | unbiased member | recusal | reasons | external appeal.

ANSWER STRIP
Efficiency can justify combined functions; fairness requires functional separation.""",
        ),
        (
            "Natural justice and delegated-power cases",
            "case-doctrine-timeline",
            [],
            """In re Delhi Laws Act (1951)
-> essential legislative function cannot be abdicated.
             v
A.K. Kraipak v. Union of India (1969)
-> bias rule; administrative/quasi-judicial line is thin.
             v
Maneka Gandhi (1978) -> fair, just and reasonable procedure.
             v
S.N. Mukherjee v. Union of India (1990) -> reasoned decision supports review.

NATURAL-JUSTICE CORE
notice + hearing + no bias + relevant evidence + speaking order.

LIMIT
procedure is context-sensitive; statutory silence is not permission for arbitrariness.""",
        ),
        (
            "Regulator, tribunal, commission and court",
            "institution-comparison",
            [],
            """COURT
general constitutional/statutory adjudication + formal judicial authority.

TRIBUNAL
specialised statutory adjudication -> merits appeal/review chain.

REGULATOR
sector rule/licence/supervision/enforcement + case-specific adjudication when empowered.

COMMISSION
name alone proves nothing: may advise, investigate, regulate or adjudicate.

L. Chandra Kumar (1997)
tribunalisation cannot remove High Court judicial review.

TRAP
specialised != tribunal | civil-court powers != court | recommendation != binding order.""",
        ),
        (
            "Regulator power, appealability and judicial control",
            "regulator-case-control",
            [],
            """            Competition Commission of India v. SAIL (2010)
-> statutory stage and character determine hearing/appealability;
not every CCI step is a final quasi-judicial order.

Cellular Operators Association of India v. TRAI (2016)
-> regulation must remain within statute and satisfy non-arbitrariness.

APPEAL CHAIN EXAMPLES
SEBI -> SAT -> Supreme Court question of law.
CCI -> NCLAT -> Supreme Court.
TRAI dispute/appeal field -> TDSAT -> Supreme Court.
CERC/SERC -> APTEL -> Supreme Court.

LIMIT
statutory merits appeal differs from Article 226/227 legality review.""",
        ),
        (
            "Independence, accountability and capture",
            "independence-capture-matrix",
            [],
            """INDEPENDENCE AXES
appointment | tenure | removal | finance | staff/data | decisional non-interference.

CAPTURE BRANCHES
industry -> information/revolving door/cognitive dependence.
political -> short-term direction or insecure tenure.
bureaucratic -> parent ministry treats regulator as subordinate office.

ACCOUNTABILITY
parent Act | Parliament/report | CAG where applicable | RTI
| consultation | published reasons | appeal | judicial review.

ANSWER STRIP
Independence means insulation from case-specific control, not freedom from public reasons.""",
        ),
        (
            "Digital and platform regulation with legal-status firewall",
            "digital-regulation-map",
            [],
            """DIGITAL HARMS
network effects | data concentration | self-preferencing | dark patterns
| algorithmic opacity | consumer/child/cyber risk.

                    TOOL CHOICE
competition law --+-- data-protection duty
consumer law -----+-- sector regulation
cyber law --------+-- interoperability/access obligation.

REFORM TEST
clear harm -> statutory power -> impact assessment -> consultation
-> conflict control -> proportionate rule -> appeal -> ex-post review.

CURRENT FIREWALL
dated Act/rule/order != draft Bill/committee paper/proposal.""",
        ),
        (
            "UPSC synthesis: calibrated independence under law",
            "answer-synthesis",
            [],
            """PRELIMS FIREWALL
statutory != regulatory != quasi-judicial | dominance != abuse
| NGT != CPCB | TRAI != TDSAT | CCI appeal=NCLAT
| regulator independent != beyond Parliament | proposal != law.

MAINS SPINE
rationale -> three axes -> regulatory cycle -> natural justice
-> institutional comparison -> appeal/review -> independence/capture
-> digital boundary -> reform.

PYQ SPINE
NGT/CPCB | FSSAI source | CCI dominance | PNGRB jurisdiction.

VERDICT
expert regulation is legitimate only when mandate, fairness, reasons and review converge.""",
        ),
    ],
    "polity-50": [
        (
            "The central idea: constitute and restrain public power",
            "constitution-root-map",
            [],
            """ROOT QUESTION
What makes a political community governed by a Constitution rather than by rulers alone?

CONSTITUTION
+-- creates institutions and offices
+-- allocates horizontal and federal authority
+-- identifies people, territory and political membership
+-- protects rights and states public goals
+-- provides amendment, conflict-resolution and continuity rules.

CONSTITUTIONALISM
limited power + rule of law + checks + rights + accountability + remedies.

MASTER DISTINCTION
constitutional document can exist without effective constitutionalism.""",
        ),
        (
            "Classification without false binaries",
            "classification-matrix",
            [],
            """FORM AXES
enacted/evolved | codified/uncodified | rigid/flexible | federal/unitary
| supreme/parliamentary | procedural/prescriptive.

INDIA
enacted + codified + supreme
mixed rigidity + federal division with centralising features
parliamentary responsibility + judicial review
procedure + transformative commitments.

TRAPS
written != rigid | uncodified != unwritten | federal != presidential
| parliamentary government != parliamentary sovereignty.

ANSWER STRIP
Classifications isolate dimensions; India is a designed synthesis across them.""",
        ),
        (
            "Constituent power and constitutional change",
            "constituent-power-tree",
            [],
            """CONSTITUENT POWER
people/founding authority -> creates constitutional order.
                     |
                     v
CONSTITUTED POWERS
Parliament | executive | judiciary | Union/States | constitutional bodies.

ARTICLE 368
change within Constitution -> procedure + federal ratification where required.

Kesavananda Bharati (1973)
amending power is wide but cannot destroy basic structure.

Minerva Mills (1980)
limited amendment and rights-DPSP harmony are part of constitutional identity.

LIMIT
no constituted organ becomes legally unlimited by invoking democracy or necessity.""",
        ),
        (
            "Rule of law, limited government and legitimacy",
            "constitutionalism-mechanism",
            [],
            """POPULAR CONSENT
election and representation -> authority to govern.
             v
RULE OF LAW
legal competence + non-arbitrariness + equality + reasoned procedure.
             v
LIMITED GOVERNMENT
rights + separation/checks + federalism + responsible executive.
             v
ACCOUNTABILITY
Parliament + audit + courts + elections + free public reason.

Maneka Gandhi (1978)
fair, just and reasonable procedure joins legality to substantive non-arbitrariness.

VERDICT
legitimacy requires source, process, rights and accountable performance.""",
        ),
        (
            "Sovereignty, legal-political constitution and conventions",
            "sovereignty-convention-map",
            [],
            """POPULAR SOVEREIGNTY
We, the People -> democratic authorship.

CONSTITUTIONAL SOVEREIGNTY
supreme Constitution -> every institution legally limited.

PARLIAMENT
democratically central, but not British-style legally sovereign.

LEGAL CONSTITUTION
text/rights/review/remedy.

POLITICAL CONSTITUTION
confidence/election/committee/federal bargaining/convention.

CONVENTION
politically obligatory practice; not automatically judicially enforceable law.""",
        ),
        (
            "Morality, transformation and constitutional identity",
            "normative-doctrine-map",
            [],
            """CONSTITUTIONAL MORALITY
text + form + procedure + institutional role + equal citizenship.

TRANSFORMATIVE CONSTITUTIONALISM
dignity + equality + social justice -> lawful anti-hierarchy change.

S.R. Bommai (1994)
federalism and secularism constrain partisan central power.

Navtej Singh Johar v. Union of India (2018)
dignity, equality and constitutional morality protect minority citizenship.

LIMIT
morality/transformative language cannot float free of text, structure and competence.""",
        ),
        (
            "Living constitution with interpretive discipline",
            "interpretive-approach-grid",
            [],
            """TEXT/ORIGINAL MEANING
adopted language and history constrain.

STRUCTURE/PRECEDENT
relationships and doctrine maintain coherence.

LIVING APPLICATION
enduring principle -> new circumstance -> reasoned doctrinal bridge.

K.S. Puttaswamy (2017)
privacy and dignity apply constitutional liberty to technological conditions.

CONTROL QUESTIONS
textual hook? institutional competence? evidence? remedy? democratic space?

TRAP
living Constitution != amendment by judicial preference.""",
        ),
        (
            "Identity, emergency and constitutional failure",
            "failure-response-system",
            [],
            """INDIAN IDENTITY
Preamble + democracy + rights + federalism + responsibility
+ judicial review + social transformation.

FAILURE BRANCHES
emergency abuse | rights hollowing | captured institution
| convention breakdown | majority treated as unlimited.

RESPONSE LADDER
reasons/review -> Parliament/accountability -> federal checks
-> election/public reason -> lawful amendment and institutional repair.

SOCIAL REVOLUTION + RESTRAINT
transform hierarchy, but preserve competence, rights, procedure and plural consent.

LIMIT
constitutional survival is institutional practice, not text alone.""",
        ),
        (
            "UPSC synthesis: higher law, democratic change and restraint",
            "answer-synthesis",
            [],
            """PRELIMS FIREWALL
constitution != constitutional law | constitution != constitutionalism
| convention != enforceable rule | written != rigid | federal != presidential
| Parliament != sovereign in British sense | basic structure != express list.

MAINS SPINE
definition/functions -> classifications -> constituent power
-> rule of law/legitimacy -> sovereignty/conventions
-> morality/transformation -> interpretation -> identity/failure.

PYQ SPINE
2021 morality | 2023 living instrument | 2025 independence-accountability.

VERDICT
India's Constitution enables democratic transformation by limiting every constituted power.""",
        ),
    ],
    "polity-51": [
        (
            "Government as property-holder, contractor and suable legal person",
            "legal-person-root",
            [],
            """ROOT QUESTION
How can the State exercise public power yet remain answerable as a legal actor?

PART XII, CHAPTER III
+-- Articles 294-297 -> succession, ownerless and maritime property
+-- Article 298 -> trade, business, property and contract capacity
+-- Article 299 -> mandatory government-contract form
+-- Article 300 -> suits, proceedings and liability continuity.

SEPARATE LINK
Article 300A -> private property may be deprived only by authority of law.

MASTER DISTINCTION
official personal protection != governmental immunity from review or liability.""",
        ),
        (
            "Succession, ownerless property and reorganisation",
            "property-succession-map",
            [],
            """ARTICLES 294-295
commencement continuity -> Union/State succeeds to property, rights and liabilities.

ARTICLE 296
escheat/lapse/bona vacantia -> location rule + governmental-purpose proviso.

ARTICLE 297
specified maritime lands, minerals and resources -> Union.

LATER REORGANISATION
statute/agreement -> assets + debt + guarantees + employees
-> contracts/licences + records + pending proceedings.

TRAP
no universal apportionment formula; use the exact reorganisation instrument.""",
        ),
        (
            "Articles 298 and 299: capacity before valid commitment",
            "government-contract-chain",
            [],
            """ARTICLE 298
executive capacity to trade, do business, acquire/hold/dispose property and contract.
                              |
                              v
ARTICLE 299 MANDATORY FORM
expressed in President/Governor's name
+ executed on behalf of that constitutional head
+ authorised person and prescribed manner.
                              |
                              v
valid public commitment -> no personal liability of head/authorised signatory.

TRAP
capacity != authority | signature != authorisation | personal immunity != State immunity.""",
        ),
        (
            "Defective contract and restitution",
            "contract-restitution-comparison",
            [],
            """ARTICLE 299 DEFECT
purported contract unenforceable as government contract.

INDEPENDENT SECTION 70 ROUTE
lawful act/delivery + non-gratuitous intention + government enjoys benefit
-> restitution measured by benefit.

State of West Bengal v. B.K. Mondal & Sons (1961)
non-gratuitous benefit can create restitutionary liability.

Mulamchand v. State of Madhya Pradesh (1968)
mandatory Article 299 form remains separate.

LIMIT
quantum meruit does not validate the contract or automatically award contract price.""",
        ),
        (
            "Article 300 and the civil-suit route",
            "suit-procedure-rail",
            [],
            """PROPER PARTY
Union matter -> Union of India | State matter -> name of State.

CPC SECTION 79
party description in government litigation.

CPC SECTION 80
ordinary official-act suit -> two-month prior notice
-> Section 80(2) court-controlled urgent/immediate-relief route.

PROCEEDING
cause of action -> correct party -> notice/exception -> pleading/evidence
-> decree/appeal/enforcement subject to law.

TRAP
procedural notice != substantive sovereign immunity.""",
        ),
        (
            "Private tort and the narrowing of sovereign immunity",
            "tort-case-timeline",
            [],
            """P & O Steam Navigation Co. v. Secretary of State (1861)
colonial sovereign/non-sovereign distinction.
             v
State of Rajasthan v. Vidyawati (1962)
ordinary operational negligence can attract State liability.
             v
Kasturi Lal v. State of Uttar Pradesh (1964)
older police-sovereign immunity line.
             v
N. Nagendra Rao & Co. v. State of Andhra Pradesh (1994)
broad immunity untenable in welfare State; any residue is narrow.

VERDICT
no blanket formula: identify function, duty, causation and remedy.""",
        ),
        (
            "Constitutional tort and vicarious responsibility",
            "public-private-remedy-map",
            [],
            """PUBLIC-LAW COMPENSATION
Rudul Sah v. State of Bihar (1983) -> unlawful detention compensation.
Nilabati Behera v. State of Orissa (1993) -> Fundamental-Right remedy distinct.
State of Andhra Pradesh v. Challa Ramkrishna Reddy (2000)
-> prison-rights accountability.

PRIVATE TORT
duty + breach + causation + damage + vicarious-employment nexus.

OFFICIAL RESPONSIBILITY
State liability may coexist with disciplinary, criminal or personal liability.

LIMIT
writ compensation vindicates rights; it does not replace every civil trial.""",
        ),
        (
            "Property, procurement, arbitration and protection boundaries",
            "accountable-contracting-map",
            [],
            """ARTICLE 300A
deprivation of private property only by authority of law.

PROCUREMENT RAIL
need/sanction -> fair criteria/competition -> reasoned award
-> Article 299 execution -> performance/payment -> CAG/audit.

ARBITRATION
valid authorised clause -> tribunal -> award -> statutory challenge/enforcement.

PROTECTION FIREWALL
Article 361 | Article 299 signatory rule | CPC notice | sanction | privilege
are separate sources with separate limits.

CURRENT
GeM/manual/draft reform != constitutional or statutory amendment.""",
        ),
        (
            "UPSC synthesis: no blanket immunity in government under law",
            "answer-synthesis",
            [],
            """PRELIMS FIREWALL
294/295 succession | 296 ownerless property | 297 maritime resources
| 298 capacity | 299 form | 300 suits | 300A property right
| Section 70 restitution != valid contract | Section 80 notice != immunity.

MAINS SPINE
legal person -> property/succession -> capacity/form
-> restitution -> suit procedure -> private tort
-> constitutional tort -> procurement/arbitration -> qualified reform.

PYQ SPINE
2025 immunity statements test source separation, not blanket State immunity.

VERDICT
public power carries special form and protection, but remains legally answerable.""",
        ),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def configure_shared_helpers() -> None:
    prior.TOPICS = TOPICS
    prior.SUPPLEMENTS = SUPPLEMENTS
    prior.PYQS = PYQS
    prior.FACTS = FACTS
    prior.MAINS_PROMPTS = MAINS_PROMPTS
    prior.PANELS = PANELS
    prior.DATE = DATE
    base.DATE = DATE
    base.PANELS.update(PANELS)


def add_session_orientations(text: str) -> str:
    sessions = base.source_sessions(text)
    for number in sorted(sessions, reverse=True):
        title, body = sessions[number]
        phrases = base.visual_phrases(body)
        while len(phrases) < 8:
            phrases.append(phrases[len(phrases) % len(phrases)])
        cleaned = [phrase.rstrip(" .;:") for phrase in phrases[:8]]
        if re.search(r"trap|discipline|caution|limit|firewall", title, re.I):
            orientation = "\n".join(
                (
                    "",
                    "",
                    f"Close-option source discipline means the systematic verification of legal source, "
                    "institutional category, status and exception before choosing a close option.",
                    "Technically, close-option source discipline comprises source attribution, doctrinal "
                    "classification, date control and remedy-specific qualification.",
                    f"The operative mechanism matters because {cleaned[3][0].lower() + cleaned[3][1:]}.",
                    f"Its principal consequence is that {cleaned[4][0].lower() + cleaned[4][1:]}.",
                    f"The decisive contrast is between {cleaned[5]} and {cleaned[6]}.",
                    f"The exam-safe limitation is that {cleaned[7][0].lower() + cleaned[7][1:]}.",
                )
            )
        else:
            orientation = "\n".join(
                (
                    "",
                    "",
                    f"{title} denotes the constitutional rules and institutional links "
                    f"organised around {cleaned[0]}.",
                    f"{title} operates through {cleaned[1]}, connected with {cleaned[2]}.",
                    f"The operative mechanism matters because {cleaned[3][0].lower() + cleaned[3][1:]}.",
                    f"Its principal consequence is that {cleaned[4][0].lower() + cleaned[4][1:]}.",
                    f"The decisive contrast is between {cleaned[5]} and {cleaned[6]}.",
                    f"The exam-safe limitation is that {cleaned[7][0].lower() + cleaned[7][1:]}.",
                )
            )
        pattern = rf"(?m)^(##\s+{number:02d}\.\s+.+?)\s*$"
        text, count = re.subn(pattern, rf"\1{orientation}", text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not add orientation to session {number}.")
    return text


def transform_source(config: dict[str, Any]) -> Path:
    original = base.add_session_orientations
    base.add_session_orientations = add_session_orientations
    try:
        return prior.transform_source(config)
    finally:
        base.add_session_orientations = original


def ensure_legacy_reference(config: dict[str, Any]) -> None:
    tracker_path = ROOT / "EXPORT-PDF-STATUS.json"
    tracker = json.loads(tracker_path.read_text(encoding="utf-8"))
    if any(
        isinstance(item, dict)
        and item.get("topic_key") == config["key"]
        and item.get("variant") == "legacy-v1"
        for item in tracker["exports"]
    ):
        return

    slug = re.sub(r"[^A-Za-z0-9]+", "-", config["title"]).strip("-")
    main_pdf = (
        ROOT
        / "notes"
        / "Polity"
        / "Topic-PDFs"
        / f"{config['number']:02d}_{slug}_Deep-Learning.pdf"
    )
    workbook = (
        ROOT
        / "notes"
        / "Polity"
        / "Session-Level-Topic-PDFs"
        / f"{config['number']:02d}_{slug}_Session-Level.pdf"
    )
    main_pdf.parent.mkdir(parents=True, exist_ok=True)
    base.refresh.markdown_learning_pdf.build_pdf(
        ROOT / Path(config["basic"].replace("\\", "/")),
        main_pdf,
        variant="legacy-v1",
        topic_key=config["key"],
        repository_root=ROOT,
    )
    workbook.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(main_pdf, workbook)
    record = {
        "record_id": f"{config['key']}:legacy-v1:g1",
        "topic_key": config["key"],
        "variant": "legacy-v1",
        "generation": 1,
        "supersedes": None,
        "command": f"Export PDF for Polity {config['number']} — {config['title']}",
        "main_pdf": relative(main_pdf),
        "workbook": relative(workbook),
        "markdown": config["basic"],
        "approved": False,
        "provenance": {
            "workflow": "legacy-compatibility-materialisation",
            "source_basic": config["basic"],
            "source_advanced": config["advanced"],
            "assembled_markdown": config["basic"],
            "renderer": {
                "name": "tools/markdown_learning_pdf.py",
                "version": "legacy-v1",
            },
            "generation_date": DATE,
            "superseded_v1": None,
            "migration_note": (
                "Compatibility PDFs were materialised from the canonical Core owner "
                "before learner-v2 generation; approval remains isolated and false."
            ),
        },
        "approval": {
            "approved": False,
            "approved_on": None,
            "scope": f"{config['key']}:legacy-v1:g1",
        },
    }
    tracker["exports"].append(record)
    tracker_path.write_text(
        json.dumps(tracker, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run() -> dict[str, Any]:
    configure_shared_helpers()
    expected_order = [f"polity-{number:02d}" for number in range(48, 52)]
    if [config["key"] for config in TOPICS] != expected_order:
        raise RuntimeError("Sequential topic order was altered.")

    safe_references = (
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
        [9, 10],
        [11, 12],
        [13, 14],
        [15],
        [1, 4, 8, 12, 15],
    )
    for key, panels in list(PANELS.items()):
        PANELS[key] = [
            (title, structural_type, safe_references[index], body)
            for index, (title, structural_type, _sessions, body) in enumerate(panels)
        ]
    base.PANELS.update(PANELS)

    clean_baseline = preserve.topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={48, 49, 50, 51},
    )
    flow_baseline = preserve.flow_topic_hashes(exclude_polity={48, 49, 50, 51})
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        ensure_legacy_reference(config)
        resumed = prior.resume_after_tracker(config, 80 + index)
        if resumed is not None:
            result, clean_folder, flow_folder = resumed
            results.append(result)
            locked_new.update(preserve.lock_hashes([clean_folder, flow_folder]))
            continue
        if preserve.compare_hashes(
            locked_new,
            {key: preserve.sha256(ROOT / key) for key in locked_new},
        ):
            raise RuntimeError(
                "Previously generated topic artifacts changed before next gate."
            )

        gate_times: dict[str, str] = {"A_started": now()}
        live = base.live_checks(config)
        audit = prior.write_audit(config, gate_times["A_started"], live)
        gate_times["A_completed"] = now()

        source_markdown = transform_source(config)
        gate_times["B_completed"] = now()

        workbook_authored = prior.workbook_gate(source_markdown, config)
        gate_times["C_completed"] = now()

        final_markdown = (
            "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Polity\\"
            f"{SECTION}\\learning-sessions\\{config['key']}\\"
            f"{config['key']}_Complete-Learning-Session_{DATE}.md"
        )
        ascii_path = base.write_ascii_spec(config, final_markdown)
        ascii_payload = json.loads(ascii_path.read_text(encoding="utf-8"))
        ascii_payload, _ = case_years.normalize_ascii_document(ascii_payload)
        ascii_path.write_text(
            json.dumps(ascii_payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        gate_times["D_completed"] = now()

        graph_path = base.write_graphical_spec(
            config,
            source_markdown,
            ascii_path,
            final_markdown,
        )
        preserve.case_year_gate(config, ascii_path, graph_path)
        gate_times["E_completed"] = now()

        spec_path = base.write_new_topic_spec(
            config,
            source_markdown,
            audit,
            ascii_path,
            graph_path,
        )
        row, _ = base.finalize_topic(config, spec_path)
        if not row["passed"]:
            raise RuntimeError(
                f"{config['key']}: render validation failed: {row['errors']}"
            )
        gate_times["F_completed"] = now()

        record = preserve.latest_record(config)
        gate_times["G_completed"] = now()

        base.export_clean_topic(config)
        clean_folder = base.verify_four_folders(config)
        gate_times["H_completed"] = now()

        flow_validation, flow_row = prior.export_flow(config, 80 + index)
        flow_folder = ROOT / Path(
            flow_row["destination_folder"].replace("\\", "/")
        )
        gate_times["I_completed"] = now()

        clean_mismatches = preserve.compare_hashes(
            clean_baseline,
            preserve.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={48, 49, 50, 51},
            ),
        )
        flow_mismatches = preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(exclude_polity={48, 49, 50, 51}),
        )
        prior_mismatches = preserve.compare_hashes(
            locked_new,
            {key: preserve.sha256(ROOT / key) for key in locked_new},
        )
        if clean_mismatches or flow_mismatches or prior_mismatches:
            raise RuntimeError(
                f"{config['key']}: preservation regression: "
                f"clean={clean_mismatches[:5]} flow={flow_mismatches[:5]} "
                f"prior={prior_mismatches[:5]}"
            )
        gate_times["J_completed"] = now()

        final_markdown_path = ROOT / Path(
            row["paths"]["markdown"].replace("\\", "/")
        )
        result = {
            "topic_key": config["key"],
            "title": config["title"],
            "started_at": gate_times["A_started"],
            "completed_at": gate_times["J_completed"],
            "gate_times": gate_times,
            "record_id": record["record_id"],
            "approved": record["approved"],
            "counts": {
                "sessions": row["session_count"],
                "main_pdf_pages": row["main_pdf_pages"],
                "workbook_pdf_pages": row["workbook_pdf_pages"],
                "mcqs": row["mcq_count"],
                "verified_pyqs": config["exact_pyqs"],
                "supporting_pyqs": config["supporting_pyqs"],
                "original_mains": prior.count_original_mains(final_markdown_path),
                "ascii_panels": row["ascii_panel_count"],
                "graphical_core_stages": record["continuous_core_first"][
                    "core_stage_count"
                ],
                "flow_pages": flow_row["pdf_validation"]["page_count"],
            },
            "workbook_authoring_gate": workbook_authored,
            "clean_library_path": relative(clean_folder),
            "flow_library_path": relative(flow_folder),
            "source_audit": relative(audit),
            "validation": relative(base.wrapper_paths(config)[0]),
            "new_topic_spec": relative(spec_path),
            "ascii_spec": relative(ascii_path),
            "graphical_spec": relative(graph_path),
            "flow_validation": relative(flow_validation),
            "paths": row["paths"],
            "factual_caveat": config["caveat"],
            "gates_passed": 10,
            "preservation": {
                "existing_clean_mismatches": clean_mismatches,
                "existing_flow_mismatches": flow_mismatches,
                "prior_new_topic_mismatches": prior_mismatches,
            },
        }
        results.append(result)
        locked_new.update(preserve.lock_hashes([clean_folder, flow_folder]))

    state = {
        "schema_version": 1,
        "batch_id": BATCH_ID,
        "created_at": now(),
        "strict_order": expected_order,
        "topics": results,
        "existing_clean_topic_artifact_count": len(clean_baseline),
        "existing_flow_topic_artifact_count": len(flow_baseline),
        "existing_clean_hash_mismatches": preserve.compare_hashes(
            clean_baseline,
            preserve.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={48, 49, 50, 51},
            ),
        ),
        "existing_flow_hash_mismatches": preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(exclude_polity={48, 49, 50, 51}),
        ),
        "prior_generated_topic_hash_mismatches": preserve.compare_hashes(
            locked_new,
            {key: preserve.sha256(ROOT / key) for key in locked_new},
        ),
    }
    state_path = EXPORTS / f"{BATCH_ID}-state.json"
    state_path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return state


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()
    state = run()
    print(
        f"topics={len(state['topics'])} order={','.join(state['strict_order'])} "
        f"clean_mismatches={len(state['existing_clean_hash_mismatches'])} "
        f"flow_mismatches={len(state['existing_flow_hash_mismatches'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
