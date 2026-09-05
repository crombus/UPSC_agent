"""Generate Polity learner-v2 topics 28-32 in strict preservation-safe order."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_23_27_sequential as prior


base = prior.base
case_years = prior.case_years
ROOT = prior.ROOT
DATE = prior.DATE
SECTION = prior.SECTION
EXPORTS = prior.EXPORTS
FINAL_LIBRARY = prior.FINAL_LIBRARY
FLOW_LIBRARY = prior.FLOW_LIBRARY
BATCH_ID = "polity-28-32-sequential-batch-2026-08-24"


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
        "polity-28",
        "UPSC and SPSC",
        "upsc-ai-kit\\knowledge\\Polity\\28_UPSC-and-SPSC_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\UPSC-and-SPSC.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\28_UPSC-and-SPSC.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\09_Civil-Services-and-Mission-Karmayogi.md",
        ],
        [
            "https://upsc.gov.in/",
            "https://upsc.gov.in/examinations/active-examinations",
            "https://www.indiacode.nic.in/",
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://dopt.gov.in/",
        ],
        0,
        0,
        "UPSC, DoPT, India Code and Legislative Department official portals "
        "were rechecked on 24 August 2026. The Public Examinations Act and "
        "Rules, 2024 and the 15 March 2024 consultation-regulation amendment "
        "remain dated controls; no volatile officeholder or calendar data is frozen.",
        "Article 320 advice is constitutionally important but generally directory "
        "and non-binding. A Joint State PSC has constitutional authority but needs "
        "State resolutions and parliamentary law; lateral recruitment must be "
        "tested post by post rather than treated as a general exemption.",
        [
            "Articles 315-323 and Union, State and Joint Public Service Commissions",
            "appointment, experience rule, tenure, acting chair, resignation and removal",
            "Articles 318-319 service safeguards and post-office restrictions",
            "Article 320 examinations, recruitment methods and disciplinary consultation",
            "exemptions, non-consultation, Articles 321-323 and advisory accountability",
            "UPSC-SPSC-Joint PSC comparison, recruitment ecosystem and lateral entry",
            "case law, examination integrity, neutrality, capacity, technology and reform",
        ],
        visual_sessions=[1, 3, 5, 7, 9, 12, 14, 17, 20, 22, 24, 27, 30, 35, 43, 49],
    ),
    topic(
        "polity-29",
        "Finance Commission",
        "upsc-ai-kit\\knowledge\\Polity\\29_Finance-Commission_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\29_Finance-Commission.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\NITI-Aayog.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        ],
        [
            "https://fincomindia.nic.in/",
            "https://www.indiabudget.gov.in/",
            "https://www.pib.gov.in/",
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://cag.gov.in/en",
        ],
        4,
        1,
        "The Sixteenth Finance Commission's official report, submitted on "
        "17 November 2025, the Explanatory Memorandum tabled on 1 February "
        "2026 and Union Budget 2026-27 remain the dated controls for the "
        "2026-31 award. Recommendation, acceptance and implementation are kept distinct.",
        "The Finance Commission is periodic and advisory. Its tax-devolution "
        "recommendations concern net shareable proceeds, not gross tax revenue; "
        "cesses and surcharges require separate treatment, and local-body "
        "augmentation remains textually linked to State Finance Commission recommendations.",
        [
            "Articles 280-281 with Articles 270, 271, 275, 279 and 282",
            "composition, qualifications, tenure, procedure and evidentiary powers",
            "vertical and horizontal devolution, divisible pool and formula criteria",
            "grants-in-aid, local-body augmentation and disaster financing",
            "Fourteenth, Fifteenth and Sixteenth Commission mandates and dated status",
            "cesses, surcharges, borrowing, off-budget risk and performance debates",
            "Finance Commission comparison, fiscal-federalism traps and answer frameworks",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16, 19, 21, 24],
    ),
    topic(
        "polity-30",
        "GST Council",
        "upsc-ai-kit\\knowledge\\Polity\\30_GST-Council_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\30_GST-Council.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism.md",
        ],
        [
            "https://gstcouncil.gov.in/en/gst-council",
            "https://gstcouncil.gov.in/en/gst-council-newsletter",
            "https://gstcouncil.gov.in/sites/default/files/2024-09/procedure_conduct_business.pdf",
            "https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau.pdf",
            "https://api.sci.gov.in/supremecourt/2020/23083/23083_2020_4_1501_35969_Judgement_19-May-2022.pdf",
        ],
        1,
        4,
        "The official 56th GST Council meeting release dated 3 September 2025 "
        "and the April 2026 Secretariat newsletter were rechecked on "
        "24 August 2026. They are dated recommendation and notification-chain "
        "anchors, not a frozen commodity-wise rate code.",
        "Article 279A recommendations are persuasive for legislatures after "
        "Mohit Minerals (2022), though statutes may condition delegated action "
        "on a Council recommendation. The five-year compensation entitlement "
        "ended in June 2022; later cess collection for loan servicing is not an extension.",
        [
            "101st Amendment and Articles 246A, 269A, 279A, 286 and 366(12A)",
            "Council composition, quorum, weighted voting, recommendations and Secretariat",
            "CGST, SGST and IGST competence, settlement and legal-effect chain",
            "alcohol, petroleum and electricity distinctions without transient clutter",
            "compensation framework and dated post-June-2022 status",
            "Mohit Minerals doctrine, dispute-resolution mandate and federal bargaining",
            "Finance Commission comparison, technology, compliance, reforms and traps",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18],
    ),
    topic(
        "polity-31",
        "National Commissions SC ST BC",
        "upsc-ai-kit\\knowledge\\Polity\\31_National-Commissions-SC-ST-BC_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Commissions-SC-ST-BC.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\31_National-Commissions-SC-ST-BC.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions-Relating-to-Certain-Classes.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Social-Justice\\basic\\07_Scheduled-Castes-Rights-Atrocities-and-Welfare.md",
            "upsc-ai-kit\\knowledge\\Social-Justice\\basic\\08_Scheduled-Tribes-PVTGs-and-Tribal-Welfare.md",
            "upsc-ai-kit\\knowledge\\Social-Justice\\basic\\09_OBC-EWS-and-Social-Mobility.md",
        ],
        [
            "https://ncsc.nic.in/about-us/functions-of-ncsc",
            "https://ncsc.nic.in/annual_reports_of_ncsc",
            "https://ncst.nic.in/page/about-the-commission",
            "https://www.ncbc.nic.in/User_Panel/UserView.aspx?TypeID=1171",
            "https://legislative.gov.in/document/amendment-acts-102-onwards",
            "https://api.sci.gov.in/supremecourt/2010/25536/25536_2010_1_1501_54462_Judgement_01-Aug-2024.pdf",
        ],
        5,
        1,
        "NCSC, NCST, NCBC, Legislative Department and Supreme Court official "
        "sources were rechecked on 24 August 2026. No later constitutional "
        "amendment changing Articles 338, 338A, 338B, 341, 342 or 342A is asserted.",
        "Civil-court powers are evidentiary powers during inquiry, not ordinary "
        "court jurisdiction. Davinder Singh (2024) permits evidence-based SC "
        "sub-classification without altering the Presidential List; separate "
        "creamy-layer observations are not presented as one unanimous exclusion rule.",
        [
            "Articles 338, 338A and 338B with 65th, 89th, 102nd and 105th Amendments",
            "composition, appointment, tenure, procedure and common constitutional duties",
            "civil-court powers, consultation, reports and action-taken memoranda",
            "distinct SC, ST and SEBC safeguard domains and institutional boundaries",
            "Articles 341, 342 and 342A list specification and alteration mechanics",
            "Jaishri Patil, Davinder Singh, sub-classification and creamy-layer limits",
            "advisory force, vacancies, data, follow-up, coordination and reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20],
    ),
    topic(
        "polity-32",
        "CAG",
        "upsc-ai-kit\\knowledge\\Polity\\32_CAG_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\32_CAG.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        ],
        [
            "https://cag.gov.in/en/page-duties-power-and-conditions-of-services-act",
            "https://cag.gov.in/en/page-audit-regulations",
            "https://cag.gov.in/en/guidelines",
            "https://cag.gov.in/en/page-performance-audit",
            "https://cag.gov.in/en/page-cdma",
            "https://sansad.in/ls/committee/financial-committees/26-public%20accounts",
        ],
        2,
        3,
        "The CAG's DPC Act, Audit Regulations, Auditing Standards, performance-"
        "audit guidance, CDMA page and parliamentary committee routes were "
        "rechecked on 24 August 2026. Current reports are examples only; no "
        "volatile officeholder, report count or headline loss figure is frozen.",
        "The CAG is an independent ex-post auditor, not a pre-authorising "
        "comptroller, investigating agency, court or policy-maker. Audit findings "
        "acquire democratic consequence through President/Governor laying, "
        "legislative committees, executive response and lawful follow-up.",
        [
            "Articles 148-151 and CAG DPC Act, 1971 source allocation",
            "appointment, oath, tenure, removal, service safeguards and independence",
            "accounts role, audit domain, access and Consolidated/Contingency/Public Accounts",
            "bodies, grants, receipts, companies, corporations and public-private nexus",
            "financial, compliance, propriety, performance, environment and IT audit",
            "President/Governor reporting and PAC/CoPU legislative scrutiny chain",
            "CAG-CGA-Finance Commission-PAC comparison, local audit and reforms",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    ),
]


SUPPLEMENTS: dict[str, str] = {}


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-28": [
        (
            "Constitutional purpose, evolution and Articles 315-323 master map",
            "psc-purpose-article-architecture",
            [1, 2, 3, 4],
            """ROOT QUESTION
How can recruitment remain merit-based, representative and insulated from patronage?

EVOLUTION
Charter Act 1853 -> Macaulay Committee 1854 -> first PSC, 1 October 1926
-> Government of India Act 1935 -> Constitution, 26 January 1950.

PART XIV, CHAPTER II
315 institution | 316 appointment/term | 317 removal/suspension
318 service/staff rules | 319 post-office limits | 320 functions/consultation
321 additional functions | 322 charged expenses | 323 reports.

DESIGN
independent constitutional advice -> lawful executive appointment -> public accountability.

LIMIT
merit is not one test score; Articles 14, 16, reservation and suitability remain operative.""",
        ),
        (
            "UPSC, SPSC and Joint State PSC: creation, assistance and federal distinctions",
            "psc-federal-institution-matrix",
            [5, 6, 7],
            """UNION PUBLIC SERVICE COMMISSION
Article 315(1) -> Union institution -> members appointed by President.

STATE PUBLIC SERVICE COMMISSION
Article 315(1) -> one for each State, subject to Article 315
-> members appointed by Governor.

JOINT STATE PSC
Article 315(2) -> resolutions by participating State legislatures
-> Parliament provides by law -> members appointed by President.

UPSC ASSISTANCE TO ONE STATE: ARTICLE 315(4)
Governor request + President approval + UPSC agreement.

JOINT RECRUITMENT: ARTICLE 320(2)
UPSC assists two or more States where special qualifications are required.

TRAP
constitutional source, creating instrument, appointing authority and service area differ.""",
        ),
        (
            "Article 316 membership, experience rule, tenure, resignation and acting chair",
            "psc-membership-tenure-lifecycle",
            [8, 9, 10, 11, 12],
            """APPOINTMENT
UPSC / Joint PSC -> President | SPSC -> Governor.

COMPOSITION
number and service conditions are regulated under Article 318.
As nearly as may be, one-half of members must have held government office for ten years.

TERM
six years from entering office.
UPSC member: age ceiling 65 | SPSC or Joint PSC member: age ceiling 62.

RESIGNATION
UPSC / Joint PSC member -> President | SPSC member -> Governor.

ACTING CHAIR: ARTICLE 316(1A)
President for UPSC/Joint PSC | Governor for SPSC.

TRAP
appointment, resignation, acting appointment and removal do not use one authority.""",
        ),
        (
            "Articles 317-319 and 322: removal, suspension and independence safeguards",
            "psc-independence-removal-map",
            [13, 14, 15, 16, 17, 18, 19, 20, 21],
            """MISBEHAVIOUR ROUTE: ARTICLE 317(1)
President refers to Supreme Court -> Court inquiry and report
-> President may remove after constitutional finding.

DIRECT PRESIDENTIAL GROUNDS: ARTICLE 317(3)
insolvency | paid employment outside office | infirmity of mind or body.

DEEMED MISBEHAVIOUR: ARTICLE 317(4)
interest in specified government contracts or benefits.

SUSPENSION PENDING INQUIRY: ARTICLE 317(2)
President for UPSC/Joint PSC | Governor for SPSC.

ARTICLE 318
President/Governor regulates member conditions and staff; disadvantage bar after appointment.

ARTICLE 319 + ARTICLE 322
post-office restrictions + expenses charged on Consolidated Fund.

LIMIT
strong tenure and finance protection coexist with executive appointment and staff dependence.""",
        ),
        (
            "Article 320 functions: examinations, recruitment methods and personnel advice",
            "psc-function-consultation-catalogue",
            [22, 23, 24, 25, 26],
            """ARTICLE 320(1)
conduct examinations for appointments to Union and State services.

ARTICLE 320(2)
UPSC assists two or more States in joint recruitment for specially qualified services.

ARTICLE 320(3) CONSULTATION
methods of recruitment -> principles for appointments
-> promotions and transfers -> candidate suitability
-> disciplinary matters -> legal-cost claims -> injury-pension claims.

DECISION CHAIN
service rules + vacancy + notice -> examination/selection -> recommendation
-> appointing government makes lawful decision.

LIMITS
PSC advice is generally advisory | government owns posts and cadres
| consultation is not adjudication | recommendation is not appointment.""",
        ),
        (
            "Exemptions, non-consultation, additional functions and Article 323 accountability",
            "psc-advice-accountability-loop",
            [27, 28, 29, 30, 31, 32],
            """ARTICLE 320(3) PROVISO
President/Governor may make consultation-exemption regulations
-> regulations must be laid before Parliament/State legislature.

ARTICLE 320(4)
consultation is not required on the manner of Article 16(4) reservation
or giving effect to Article 335.

State of U.P. v. Manbodhan Lal Srivastava (1957)
consultation is directory; non-consultation alone does not invalidate action.

ARTICLE 321
Parliament/State legislature may extend functions to local or other public institutions.

ARTICLE 323
annual report -> President/Governor -> legislature
+ memorandum explaining non-acceptance of advice.

SYNTHESIS
non-binding advice becomes constitutionally visible through reasoned legislative reporting.""",
        ),
        (
            "Recruitment ecosystem, lateral entry and institutional ownership boundaries",
            "psc-recruitment-ecosystem",
            [33, 34, 35, 36, 37],
            """WHO OWNS WHAT?
Government / DoPT -> posts, recruitment rules, cadre, reservation and appointment.
UPSC / SPSC -> examination, selection and consultation assigned by Constitution/rules.
SSC / departmental body -> statutory or executive recruitment within assigned jurisdiction.
CAT / courts -> service-dispute adjudication and legality review.

LATERAL ENTRY TEST
identify post -> recruitment rule -> mode and level -> consultation regulation
-> reservation/equality control -> transparent selection -> appointing authority.

CURRENT CONTROL
15 March 2024 consultation-regulation amendment covers specified posts and methods.
It is not a universal constitutional category called lateral entry.

TRAP
UPSC is not the entire civil-service system and CAT is not a recruitment agency.""",
        ),
        (
            "Selection case law and examination-integrity control",
            "psc-case-law-integrity-matrix",
            [38, 39, 40, 41, 42, 43, 44, 45],
            """FAIRNESS AND REVIEW
Ashok Kumar Yadav (1985) -> bias controls and proportionate interview design.
K. Manjusree (2008) -> no undisclosed minimum criterion after process begins.
Tej Prakash Pathak (2024) -> stable, lawful and non-arbitrary recruitment rules.
Shankarsan Dash (1991) -> select-list entry gives no indefeasible appointment right.
M.V. Thimmaiah (2007) -> courts do not become appellate selection boards.

PUBLIC EXAMINATIONS ACT AND RULES, 2024
prevention -> secure centres/CBT -> incident reporting -> investigation -> penalty.

INTEGRITY SYSTEM
conflict disclosure + audit trail + cyber security + calibrated transparency
-> prompt reasoned remedy.

LIMIT
criminal punishment cannot cure opaque rules, weak governance or inaccessible remedies.""",
        ),
        (
            "Neutrality, capacity, reform, traps and qualified answer synthesis",
            "psc-reform-answer-synthesis",
            [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56],
            """INDEPENDENCE TEST
credible appointments + secure tenure + charged expenses + professional staff
-> protected data/exams + reasoned decisions + legislative reporting + judicial review.

REFORM
transparent criteria -> vacancy planning -> conflict/recusal rules
-> common security standards -> faster grievance disposal
-> SPSC capacity support without Union takeover.

PRELIMS FIREWALL
Governor appoints SPSC but President removes | age 65 versus 62
| Joint PSC needs parliamentary law | Article 320 advice is not binding
| Article 319 restrictions differ | ECI, SSC, CAT and PSC are not interchangeable.

PYQ AUDIT
no direct standalone 2018-2026 PSC PYQ verified; do not manufacture one.

MAINS SPINE
constitutional purpose -> exact Article -> function -> safeguard
-> practical deficit -> case-year -> accountable reform -> neutrality-with-representation verdict.""",
        ),
    ],
    "polity-29": [
        (
            "Fiscal-federal problem and the Articles 270-282 constitutional chain",
            "finance-commission-constitutional-map",
            [1, 2],
            """ROOT PROBLEM
Union has broader buoyant taxes; States carry service-heavy expenditure duties.

VERTICAL IMBALANCE
Union versus all States -> size of States' collective share.

HORIZONTAL IMBALANCE
differences among States -> inter se distribution formula.

ARTICLE CHAIN
270 divisible taxes | 271 Union surcharges | 275 grants-in-aid
279 net proceeds and CAG certification | 280 Finance Commission
281 report + explanatory memorandum | 282 public-purpose grants.

CORE DISTINCTION
gross tax revenue != net proceeds != divisible pool != State share != grants.""",
        ),
        (
            "Article 280 institution: constitution, qualifications, procedure and report",
            "finance-commission-institution-lifecycle",
            [3, 4, 5, 6],
            """CONSTITUTION
President constitutes every fifth year or earlier if necessary.
Chairman + four other members.

FINANCE COMMISSION ACT, 1951
Chairman -> public-affairs experience.
Other members -> judicial qualification | government finance/accounts
| financial administration | economics.

OPERATING DESIGN
President appoints and fixes terms through constituting order
-> Commission determines procedure -> civil-court-type evidentiary powers.

ARTICLE 281
recommendations + explanatory memorandum on action taken
-> laid before each House of Parliament.

LIMIT
recommendations are expert and advisory, not self-executing decrees.""",
        ),
        (
            "Divisible pool, vertical share and horizontal devolution formula",
            "tax-devolution-mechanics",
            [7, 8, 9],
            """GROSS UNION TAX COLLECTION
minus collection cost -> net proceeds.

OUTSIDE THE SHAREABLE POOL
Article 271 surcharges + constitutionally earmarked cesses + excluded receipts.

DIVISIBLE POOL
specified net Union-tax proceeds under Article 270.

VERTICAL DEVOLUTION
Commission recommends percentage for all States together.

HORIZONTAL DEVOLUTION
State share distributed by weighted criteria:
income distance / need | population | area | forest/ecology
| demographic performance | tax effort | other award-specific criteria.

ANALYTICAL TEST
equity + efficiency + predictability + data quality + incentives.

TRAP
a high headline percentage does not neutralise a shrinking divisible base.""",
        ),
        (
            "Grants-in-aid, Article 282 and the tax-versus-grant distinction",
            "finance-commission-grants-map",
            [10],
            """ARTICLE 275
Parliament may provide grants-in-aid of revenues of States in need
and constitutionally specified welfare/administration grants.

FINANCE COMMISSION ROLE
recommend principles governing Article 275 grants
and award-specific grant categories within terms of reference.

ARTICLE 282
Union or State may make grants for any public purpose
even beyond the ordinary legislative field.

Bhim Singh (2010)
supports the breadth of Article 282 public-purpose grants.

TAX DEVOLUTION                         GRANT
share in common tax pool               transfer for need/purpose/design
formula entitlement                    may be conditional or category-specific.

LIMIT
Finance Commission grant, Article 282 grant and centrally sponsored scheme are not synonyms.""",
        ),
        (
            "Panchayat, Municipality and State Finance Commission augmentation chain",
            "finance-commission-local-body-chain",
            [11],
            """73RD AND 74TH AMENDMENT LINK
Article 280(3)(bb) -> augment State Consolidated Fund for Panchayats.
Article 280(3)(c)  -> augment State Consolidated Fund for Municipalities.

TEXTUAL BASIS
recommendations of the State Finance Commission under Articles 243I and 243Y.

FLOW
local functions and finances -> SFC assessment
-> Union Finance Commission augmentation recommendation
-> Union budget/guidelines -> State fund -> eligible local bodies.

ACCOUNTABILITY
accounts + audit + timely SFCs + transparent release + service outcomes.

LIMIT
Union local-body grants supplement; they do not replace State devolution,
own revenue or the constitutional role of State Finance Commissions.""",
        ),
        (
            "Fourteenth, Fifteenth and Sixteenth Finance Commission trajectory",
            "finance-commission-award-timeline",
            [13, 14, 15, 16, 17, 18],
            """FOURTEENTH FINANCE COMMISSION: 2015-20
States' vertical share raised from 32% to 42%.

FIFTEENTH FINANCE COMMISSION: 2021-26
41% vertical share; six horizontal criteria
including demographic performance, forest/ecology and tax/fiscal effort.

SIXTEENTH FINANCE COMMISSION
constituted 31 December 2023 -> report submitted 17 November 2025
-> award period 2026-27 to 2030-31
-> Explanatory Memorandum tabled 1 February 2026.

DATED CONTROL
41% vertical share accepted for 2026-31.
Per-capita GSDP distance carries the largest horizontal weight, 42.5%;
GDP contribution appears with 10% weight.

LIMIT
report recommendation, government acceptance and annual implementation must remain separate.""",
        ),
        (
            "Disaster finance, debt, borrowing and whole-government fiscal risk",
            "finance-commission-fiscal-risk-system",
            [12, 17, 18, 19, 20],
            """DISASTER FINANCE
Finance Commission may recommend disaster-management funding arrangements
within its terms of reference and the Disaster Management Act framework.

FISCAL ROADMAP
deficit and debt paths -> Union/State sustainability
-> transparent liabilities -> credible budget institutions.

OFF-BUDGET RISK
public entities borrow or defer payment outside headline budget
-> contingent liability or future servicing pressure
-> incomplete fiscal picture unless consolidated.

ARTICLE 293 LINK
State borrowing and Union consent conditions belong to the wider fiscal-federal system.

REFORM
comparable accounts + debt register + guarantee disclosure
-> independent projections + medium-term correction.

LIMIT
Finance Commission advice does not itself amend borrowing law or erase political choices.""",
        ),
        (
            "Finance Commission compared with GST Council, NITI Aayog, CAG and SFC",
            "finance-institution-comparison",
            [21, 22],
            """FINANCE COMMISSION
Article 280 | periodic expert body | tax devolution + grants + fiscal advice.

GST COUNCIL
Article 279A | continuing Union-State forum | GST recommendations and bargaining.
Mohit Minerals (2022) -> recommendations persuasive, not legislative commands.

NITI AAYOG
executive-resolution policy platform | strategy and cooperative dialogue
| no Article 280 transfer award.

CAG
Articles 148-151 | audits and certifies net proceeds under Article 279
| does not allocate the divisible pool.

STATE FINANCE COMMISSION
Articles 243I/243Y | State-local fiscal relations every five years.

TRAP
coordination, distribution, strategy, audit and State-local review are different functions.""",
        ),
        (
            "Fiscal-federal debates, PYQ routes, traps and final answer spine",
            "finance-commission-answer-synthesis",
            [22, 23, 24],
            """CORE DEBATES
cesses/surcharges and divisible-pool erosion | equity versus incentive
| data lag and climate/ecology costs | tied schemes versus State autonomy
| local-body absorption and accountability | debt and off-budget opacity.

PRELIMS FIREWALL
Chair + four | five years or earlier | President constitutes
| Article 281 requires report and memorandum
| vertical != horizontal | Article 275 != Article 282
| SFC != Union Finance Commission | CAG certifies net proceeds.

PYQ ROUTES
2018 constitution/ToR | 2021 Fourteenth FC | 2023 horizontal criteria
| 2025 Fifteenth FC facts | 2025 Centre-State finance.

MAINS SPINE
define imbalance -> article chain -> transfer mechanism -> award evidence
-> contested incentive/autonomy effect -> implementation qualification
-> predictable, transparent and accountable fiscal-federal verdict.""",
        ),
    ],
    "polity-30": [
        (
            "From fragmented indirect taxes to the 101st Amendment compact",
            "gst-constitutional-transition",
            [1, 2],
            """PRE-GST PROBLEM
manufacture tax + service tax + State VAT/CST + entry levies
-> broken cross-credit + cascading + border friction.

101ST AMENDMENT ACT, 2016
Article 246A -> special shared GST competence.
Article 269A -> inter-State levy, collection and apportionment.
Article 279A -> Union-State GST Council.
Article 366(12A) -> GST definition.

CONSTITUTIONAL SURGERY
omitted Article 268A + changed distribution provisions and Seventh Schedule entries.

CORE IDEA
pooled fiscal sovereignty for a destination-based common market.

LIMIT
"One Nation, One Tax" is shorthand; India operates dual GST with exclusions and variations.""",
        ),
        (
            "Articles 246A, 269A and 286: CGST, SGST and IGST legal architecture",
            "gst-competence-settlement-map",
            [3, 4],
            """INTRA-STATE SUPPLY
Central law -> CGST | State/UT law -> SGST/UTGST.

INTER-STATE SUPPLY: ARTICLE 246A(2)
Parliament has exclusive GST legislative power.

ARTICLE 269A
Government of India levies and collects IGST
-> parliamentary law on place of supply and apportionment
-> settlement between Union and destination State.

IMPORT
deemed inter-State supply for GST architecture.

ARTICLE 286
limits State taxation of supplies outside the State or in import/export course.

TRAP
IGST is not a third destination government's tax; it is the settlement bridge
for an integrated dual-GST system.""",
        ),
        (
            "Article 279A composition, quorum, weighted vote and recommendation fields",
            "gst-council-decision-architecture",
            [5, 6, 8],
            """COMPOSITION
Union Finance Minister -> Chairperson.
Union Minister of State for Revenue/Finance.
State finance/taxation ministers or nominated ministers.
State members choose a Vice-Chairperson.

QUORUM
one-half of total members.

WEIGHTED VOTE
Union = one-third | States together = two-thirds.
Decision = at least three-fourths of weighted votes of members present and voting.

COALITION MATHEMATICS
Union alone cannot pass | States alone cannot pass.

RECOMMENDATION FIELDS
taxes to subsume | goods/services | model laws | place of supply
| thresholds | rates/bands | special rates | petroleum start date | special provisions.

LIMIT
Council recommends; competent legislatures and delegated instruments create law.""",
        ),
        (
            "Secretariat, procedure, recommendation-to-law chain and disputes",
            "gst-council-procedure-accountability",
            [7, 9, 15],
            """INSTITUTIONAL SUPPORT
GST Council Secretariat -> agenda, records, coordination and implementation follow-up.

PROCEDURE
proposal -> committee/officer analysis -> agenda note -> meeting
-> consensus or weighted vote -> minutes/recommendation -> legal instrument.

LEGAL-EFFECT CHAIN
constitutional recommendation
-> Parliament/State legislature enacts or amends statute
or authorised executive issues rule/notification
-> taxpayer obligation.

ARTICLE 279A(11)
Council shall establish a mechanism to adjudicate specified Union-State disputes.

CURRENT LIMIT
no complete publicly verified constitutional mechanism is asserted as operational.
GSTAT and taxpayer appeals are not silently relabelled Article 279A(11) adjudication.""",
        ),
        (
            "Tax-base boundaries: alcohol, petroleum, electricity, rates and input credit",
            "gst-boundary-mechanics-matrix",
            [10, 11],
            """ALCOHOLIC LIQUOR FOR HUMAN CONSUMPTION
excluded from Article 366(12A) GST definition.

FIVE PETROLEUM PRODUCTS
GST levy begins from a date recommended under Article 279A(5);
until then, retained excise/VAT fields continue.

TOBACCO
within GST while retained Union excise competence also exists.

ELECTRICITY
not excluded by the GST definition like alcohol;
electricity duty remains under Entry 53 and supply treatment needs exact law.

RATE / EXEMPTION / THRESHOLD
Council recommendation -> competent notification or legislation.

INPUT-TAX CREDIT
reduces cascading where statutory eligibility and compliance conditions are met.

TRAP
do not convert a press release into a self-executing tax rate.""",
        ),
        (
            "GST compensation bargain and dated post-transition boundary",
            "gst-compensation-timeline",
            [12],
            """COMPENSATION ACT, 2017
base year 2015-16 -> projected annual revenue growth 14%
-> protected revenue minus actual revenue -> compensation gap.

FUNDING
compensation cess on specified supplies -> Compensation Fund.

TRANSITION
five years from GST introduction -> entitlement ended in June 2022.

PANDEMIC SHOCK
revenue/cess shortfall -> back-to-back borrowing arrangement
-> cess continued for servicing principal and interest.

CURRENT CONTROL: 24 AUGUST 2026
later cess collection for loan servicing != renewed five-year compensation entitlement.

REFORM LESSON
future shocks need transparent accounts, predictable settlement and negotiated burden sharing.""",
        ),
        (
            "Mohit Minerals (2022): persuasion, legislation and delegated action",
            "gst-mohit-minerals-doctrine",
            [13],
            """Mohit Minerals (2022)

CONSTITUTIONAL HOLDING
Article 279A recommendations are persuasive and carry cooperative value;
they are not binding commands on Parliament or State legislatures.

WHY
Article 246A gives simultaneous legislative power
and Indian federalism works through dialogue, not Council hierarchy.

STATUTORY QUALIFICATION
where GST legislation conditions delegated rules or notifications
on Council recommendation, the executive must obey that statute.

CASE RESULT
ocean-freight levy failed within the statutory composite-supply framework.

TRAP
non-binding recommendation != irrelevant Council
and it does not authorise executive action contrary to enacted GST law.""",
        ),
        (
            "Federal bargaining, Finance Commission comparison and technology-compliance loop",
            "gst-federal-governance-system",
            [14, 16, 17],
            """GST COUNCIL
continuous bargaining over a pooled indirect-tax base.

FINANCE COMMISSION
periodic Article 280 recommendation on divisible taxes and grants.

FEDERAL GAINS
common market + destination settlement + shared rule forum + coordinated compliance.

FEDERAL COSTS
reduced unilateral State rate space + Union veto capacity
| compensation trust deficit | unequal administrative capacity.

TECHNOLOGY CHAIN
registration -> invoice/reporting -> credit matching -> return/payment
-> analytics -> audit/appeal.

CAUTION
digital trace improves verification but can create exclusion, mismatch and refund burdens.

REFORM
publish revenue models + reasoned minutes + stable rate design
-> operational dispute mechanism + stronger State capacity.""",
        ),
        (
            "Current anchors, PYQ routes, traps and qualified synthesis",
            "gst-answer-synthesis",
            [15, 16, 17],
            """DATED ANCHORS
56th Council meeting release: 3 September 2025.
April 2026 Secretariat newsletter: notification-on-recommendation example.
No commodity-wise current rate list is frozen.

PRELIMS FIREWALL
quorum one-half | Union one-third | States two-thirds
| decision threshold three-fourths weighted
| alcohol excluded | petroleum deferred | electricity separately treated
| recommendation != legislation | compensation entitlement ended June 2022.

PYQ ROUTES
2018 exemption mechanics | 2019 subsumed taxes | 2020 compensation
| 2023 101st Amendment/federalism | 2025 fiscal-federalism adjacency.

MAINS SPINE
pre-GST defect -> three-Article architecture -> Council bargain
-> legal-effect limit -> federal gain/cost -> dated anchor
-> transparent, predictable and cooperative reform verdict.""",
        ),
    ],
    "polity-31": [
        (
            "Evolution from Special Officer to three constitutional commissions",
            "commission-evolution-timeline",
            [1, 2],
            """ORIGINAL ARTICLE 338
Special Officer for Scheduled Castes and Scheduled Tribes.

65TH AMENDMENT ACT, 1990
combined National Commission for SCs and STs
-> first constitutional commission constituted 12 March 1992.

89TH AMENDMENT ACT, 2003
Article 338 retained for NCSC + Article 338A inserted for NCST
-> separate commissions operational 19 February 2004.

Indra Sawhney (1992) -> permanent backward-class body.
NCBC Act, 1993 -> statutory NCBC.

102ND AMENDMENT ACT, 2018
Article 338B + Article 342A + Article 366(26C)
-> constitutional NCBC operational 15 August 2018.

105TH AMENDMENT ACT, 2021
State/UT own-list competence made explicit from 15 September 2021.""",
        ),
        (
            "Composition, appointment, tenure and self-regulated procedure",
            "commission-membership-architecture",
            [3],
            """COMMON COMPOSITION
Chairperson + Vice-Chairperson + three other Members.

APPOINTMENT
President by warrant under hand and seal.

SERVICE CONDITIONS / TENURE
subject to parliamentary law, determined by presidential rules.
Three-year term comes from governing rules, not the constitutional clause itself.

PROCEDURE
each Commission may regulate its own procedure.

CONSTITUTIONAL STATUS
entrenches existence, mandate and report route.

LIMIT
constitutional status does not automatically guarantee timely appointments,
regional reach, staff capacity, data quality or acceptance of recommendations.""",
        ),
        (
            "Six common duties and the complaint-to-policy accountability cycle",
            "commission-duty-cycle",
            [4],
            """COMMON DUTIES UNDER CLAUSE (5)
investigate and monitor safeguards.
inquire into specific complaints of deprivation.
participate and advise in socio-economic development planning.
evaluate development progress.
present annual and other reports to President.
recommend measures for effective implementation and protection.
perform other specified functions.

EVIDENCE CYCLE
safeguard -> implementation record -> complaint/monitoring
-> inquiry -> finding -> recommendation -> government response
-> legislative scrutiny -> corrective law, policy or administration.

LIMIT
Commission scrutiny supports remedies; it does not replace police, tribunal or court.""",
        ),
        (
            "Civil-court powers, reports, memoranda and consultation obligation",
            "commission-power-report-consultation",
            [5, 6, 7],
            """CIVIL-COURT POWERS DURING INVESTIGATION OR INQUIRY
summon and enforce attendance | examine on oath
| require discovery/production | receive affidavit evidence
| requisition public records | issue commissions
| prescribed additional matters.

LEGAL EFFECT
evidence-gathering power != ordinary civil-court jurisdiction
!= conviction, sentence, executable damages or constitutional invalidation.

REPORT ROUTE
President -> Parliament + memorandum on action taken and rejected advice.
State-related part -> Governor/State Government route -> State legislature + memorandum.

CONSULTATION
Union and States shall consult the relevant Commission on major policy matters.

LIMIT
consultation is a constitutional hearing duty, not a general veto.""",
        ),
        (
            "NCSC, NCST and NCBC: shared engine, distinct safeguard domains",
            "commission-domain-comparison",
            [8, 9, 10, 14, 15, 16],
            """NCSC: ARTICLE 338
SC safeguards, untouchability, representation, service discrimination
and atrocity-prevention implementation.

NCST: ARTICLE 338A
ST safeguards plus tribal land, forest, minor produce, displacement,
resources, PESA and shifting-cultivation concerns under specified functions.

NCBC: ARTICLE 338B
SEBC safeguards, complaints, development, policy advice
and Central/State list context.

COMMON ENGINE
monitor -> inquire -> advise -> report -> recommend.

BOUNDARIES
NCSC/NCST do not prosecute offences.
NCST does not decide FRA claims or govern Autonomous Councils.
NCBC does not itself amend a Central or State SEBC list.

TRAP
specialised overlap calls for referral and coordination, not automatic merger.""",
        ),
        (
            "Articles 341, 342 and 342A: specification and alteration of lists",
            "protected-class-list-mechanics",
            [11, 12],
            """SCHEDULED CASTES: ARTICLE 341
President specifies by public notification for a State/UT;
Parliament later includes or excludes by law.

SCHEDULED TRIBES: ARTICLE 342
same constitutional pattern; State consultation occurs at initial specification.

SEBC CENTRAL LIST: ARTICLE 342A(1)-(2)
President specifies for Central Government purposes;
Parliament includes or excludes by law.

STATE / UT LIST: ARTICLE 342A(3)
State or UT may by law prepare and maintain its own list for own purposes.

ARTICLE 366(26C)
defines socially and educationally backward classes through Article 342A.

CORE DISTINCTION
Commission advice informs process; the constitutionally named authority changes legal status.""",
        ),
        (
            "102nd-105th federal trajectory and Jaishri Laxmanrao Patil (2021)",
            "ncbc-federal-amendment-case-chain",
            [10, 12, 13],
            """102ND AMENDMENT, 2018
constitutional NCBC + original Article 342A list wording.

Jaishri Laxmanrao Patil (2021)
majority read the 102nd Amendment as displacing independent State SEBC identification;
the Maratha quota also failed the separate 50% ceiling analysis.

105TH AMENDMENT, 2021
Central List confined to Central purposes
-> State/UT own lists expressly restored/clarified in Article 342A(3)
-> Article 338B(9) consultation exception for that list-making purpose.

TRAP
reservation ceiling, identification authority and Commission consultation
are separate constitutional questions.

LIMIT
the 105th Amendment did not itself decide every quota, inclusion or creamy-layer dispute.""",
        ),
        (
            "Davinder Singh (2024), sub-classification and the creamy-layer boundary",
            "sc-subclassification-doctrine",
            [13],
            """            Davinder Singh (2024)

HOLDING
States may create evidence-based sub-classification within Scheduled Castes
to distribute reservation benefits more equitably.

CONDITIONS
quantifiable and demonstrable material -> rational classification
-> no deletion from or alteration of the Article 341 Presidential List
-> judicial review remains.

OVERRULED BOUNDARY
E.V. Chinnaiah was overruled on the bar against SC sub-classification.

CREAMY-LAYER CAUTION
separate judicial opinions discussed exclusion ideas;
do not present them as one unanimous, enacted SC/ST creamy-layer rule.

COMMISSION ROLE
evidence, consultation and monitoring may inform policy but do not replace valid law.""",
        ),
        (
            "Institutional gaps, Prelims traps, PYQ routes and answer synthesis",
            "commission-reform-answer-synthesis",
            [17, 18, 19],
            """IMPLEMENTATION GAPS
vacancies + delayed reports + weak regional access + fragmented complaint data
+ poor recommendation tracking + overlapping forums.

REFORM
transparent appointments -> time-bound staffing -> common intake/referral
-> joint inquiry protocol -> public action-taken dashboard
-> research capacity -> reasoned government response.

PRELIMS FIREWALL
338 NCSC | 338A NCST | 338B NCBC
| Chair + Vice-Chair + three Members
| civil-court powers only for inquiry | recommendations generally advisory
| 341 SC | 342 ST | 342A Central/State SEBC architecture.

PYQ ROUTES
2018 NCSC/minority reservation + umbrella commission
| 2020 constitutionalisation | 2022 NCBC | 2023 body status | 2024 ST list.

MAINS SPINE
constitutional purpose -> common powers -> distinct domain -> legal limit
-> case/amendment -> implementation gap -> coordinated-specialisation verdict.""",
        ),
    ],
    "polity-32": [
        (
            "Democratic audit purpose and the Constitution-to-report accountability chain",
            "cag-democratic-accountability-map",
            [1],
            """ROOT QUESTION
How does the legislature verify executive use of public money?

AUTHORITY CHAIN
legislature authorises tax and appropriation
-> executive collects, spends and keeps records
-> independent CAG audits evidence
-> President/Governor causes report to be laid
-> PAC/CoPU or legislature scrutinises
-> executive replies and corrects.

SOURCE LADDER
Articles 148-151 -> CAG DPC Act, 1971
-> entity-specific law -> Audit Regulations/Standards -> judicial interpretation.

LIMIT
audit informs democratic control; it does not govern, prosecute or recover by itself.""",
        ),
        (
            "Article 148 office: appointment, oath, tenure, removal and independence",
            "cag-office-independence-architecture",
            [2, 3, 4],
            """APPOINTMENT
President by warrant under hand and seal.

OATH
before President or nominee in Third Schedule form.

TENURE: DPC ACT, SECTION 4
six years or age 65, whichever earlier; resignation addressed to President.

REMOVAL
same manner and grounds as a Supreme Court Judge
-> proved misbehaviour or incapacity + special-majority address.

INDEPENDENCE SAFEGUARDS
service conditions not varied to disadvantage
| no further Union/State government office
| IAAD administration after consultation
| office expenses charged on Consolidated Fund of India.

LIMIT
appointment has no constitutional collegium and post-audit impact depends on follow-up.""",
        ),
        (
            "Articles 149-151, the DPC Act and the audit-versus-accounts boundary",
            "cag-constitutional-statutory-map",
            [2, 5, 6],
            """ARTICLE 149
constitutional gateway -> Parliament prescribes duties and powers.

ARTICLE 150
President prescribes form of Union/State accounts on CAG advice.

ARTICLE 151
Union report -> President -> both Houses.
State report -> Governor -> State legislature.

DPC ACT, 1971
Sections 10-12 accounts role where retained
| 13-18 audit and access
| 19-20 companies/corporations/entrusted audits
| 23-24 regulations and scope.

AUDITOR, NOT UNIVERSAL COMPTROLLER
predominantly ex-post review; no routine pre-authorisation of each withdrawal.

ACCOUNTS LIMIT
departmentalisation and State arrangements mean CAG does not compile every account.""",
        ),
        (
            "Audit domain: public funds, expenditure, receipts, grants and access",
            "cag-audit-jurisdiction-system",
            [6],
            """PUBLIC ACCOUNT DOMAINS
Consolidated Fund -> authorised revenue/expenditure.
Contingency Fund -> urgent advances under law.
Public Account -> provident funds, small savings and other trust-like receipts.

DPC ACT ROUTES
Section 13 expenditure | Section 14 substantially financed bodies
| Section 15 grants/loans | Section 16 receipts
| Section 17 stores/stock | Section 18 records, inspection and information.

JURISDICTION TEST
identify entity -> identify public-money/revenue nexus
-> identify statutory route -> define scope -> obtain records -> audit evidence.

LIMIT
public importance alone does not create jurisdiction; legal nexus and proportionate scope matter.""",
        ),
        (
            "Financial, compliance, propriety, performance, environment and IT audit",
            "cag-audit-type-matrix",
            [7],
            """FINANCIAL AUDIT
fair presentation and sufficient appropriate evidence.

COMPLIANCE AUDIT
law, rule, sanction, contract and authority.

PROPRIETY AUDIT
wisdom, faithfulness, economy and avoidance of waste or improper discretion.

PERFORMANCE AUDIT
economy -> efficiency -> effectiveness.

RECEIPTS AUDIT
assessment, collection and proper allocation of public revenue.

IT / ENVIRONMENT / THEMATIC AUDIT
specialised subject or method within the wider mandate.

POLICY BOUNDARY
CAG may test authority, design implementation, prudence and results;
it should not substitute its preferred lawful policy merely because another choice was possible.""",
        ),
        (
            "Companies, corporations, PPPs, regulators and local-body audit routes",
            "cag-entity-route-map",
            [8, 9, 11],
            """GOVERNMENT COMPANY
CAG appoints statutory auditor under Companies Act Section 139
-> directions under Section 143(5)
-> supplementary audit/comments/test audit under Sections 143(6)-(7).

STATUTORY CORPORATION
governing law + DPC Act Section 19 route.

OTHER BODY / PPP / REGULATED ENTITY
Sections 14, 15, 16 or 20 only where legal public-finance nexus exists.

LOCAL BODIES
State law and entrustment vary; CAG may provide Technical Guidance and Support.
This is not one uniform constitutional municipal/Panchayat audit model.

Association of Unified Telecom Service Providers of India v. Union of India (2014)
audit may follow Union revenue share from a public-resource licence;
it is not universal private-company audit power.""",
        ),
        (
            "Report laying, PAC and CoPU: converting audit information into accountability",
            "cag-legislative-scrutiny-chain",
            [10],
            """UNION CHAIN
CAG report -> President -> laid before Parliament
-> PAC / CoPU / relevant committee -> ministry evidence
-> committee finding -> action-taken response -> correction.

STATE CHAIN
CAG report -> Governor -> State legislature -> State PAC/committee scrutiny.

PAC
appropriation accounts + finance accounts + relevant CAG reports.

COPU
public-undertaking reports/accounts + related CAG reports.

CAG ROLE
technical evidence and assistance; not committee member or final political decision-maker.

LIMIT
CAG paragraph != PAC conclusion != court judgment != automatic recovery order.""",
        ),
        (
            "Judicial controls: performance, timing, report status and revenue-share access",
            "cag-case-law-boundary",
            [7, 9, 10],
            """Arvind Gupta (2012)
performance audit and the three Es are in-built in the DPC Act.

S. Subramaniam Balaji (2013)
CAG examines legality, validity and propriety after expenditure.

Arun Kumar Agrawal (2013)
CAG report deserves respect but remains subject to legislative/PAC scrutiny;
it does not automatically prove the final basis for judicial relief.

Association of Unified Telecom Service Providers of India v. Union of India (2014)
revenue-share audit access follows the public-resource and Consolidated-Fund nexus.

SYNTHESIS
broad audit methods + ex-post timing + evidentiary public report
-> no automatic adjudicatory finality.""",
        ),
        (
            "CAG-CGA-Finance Commission-PAC comparison, reform and answer synthesis",
            "cag-reform-answer-synthesis",
            [11, 12],
            """CAG
constitutional independent audit and legislative reporting.

CGA
executive accounting and financial-information system for Union civil ministries.

FINANCE COMMISSION
Article 280 transfer recommendations; CAG certifies net proceeds under Article 279.

PAC / COPU
legislative scrutiny; committees make parliamentary findings and seek action.

REFORM
secure data access + audit-ready digital systems + risk analytics
-> PPP/regulator clarity + stronger local audit + timely reports
-> action-taken tracking + legislative research capacity.

PRELIMS FIREWALL
Article 148 office | 149 statutory duties | 150 President on CAG advice
| 151 report route | six years/65 from DPC Act | audit != investigation.

MAINS SPINE
independence -> legal mandate -> audit type/entity route -> report chain
-> limitation -> digital/access reform -> evidence-led accountability verdict.""",
        ),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def transform_source(config: dict[str, Any]) -> Path:
    canonical = ROOT / Path(config["canonical"].replace("\\", "/"))
    text = prior._normalize_control_date(
        canonical.read_text(encoding="utf-8").replace("\r\n", "\n")
    )
    text = text.replace("19 August 2026", "24 August 2026")
    text = text.replace(
        "../../../notes/Polity/assets/",
        "../../../../../../notes/Polity/assets/",
    )
    text = re.sub(
        r"(?m)^#\s+.+$",
        f"# {config['title']} — Complete Uncompressed Learning Session",
        text,
        count=1,
    )
    anchor = (
        f"- [CURRENT] **Live official refresh, 24 August 2026:** "
        f"{config['current_note']}"
    )
    if "Status is controlled to **24 August 2026, Asia/Kolkata**." not in text:
        heading = re.search(r"(?m)^## Package method[^\n]*$", text)
        if not heading:
            raise RuntimeError(f"{config['key']}: package-method heading missing.")
        insertion = text.find("\n", heading.end()) + 1
        text = (
            text[:insertion]
            + "\n- [CURRENT] Status is controlled to "
            + "**24 August 2026, Asia/Kolkata**.\n"
            + text[insertion:]
        )
    status = re.search(
        r"(?m)^- \[CURRENT\] Status is controlled to "
        r"\*\*24 August 2026, Asia/Kolkata\*\*\.\s*$",
        text,
    )
    if not status:
        raise RuntimeError(f"{config['key']}: current-control line missing.")
    text = text[: status.end()] + "\n" + anchor + text[status.end() :]

    headings = base.heading_offsets(text)
    part_i = base.start_for(headings, [r"^PART I\b"])
    practice = base.start_for(
        [(offset, title) for offset, title in headings if offset > part_i],
        [
            r"PYQ, practice and solved workbook",
            r"^Solved topic-specific MCQs$",
            r"^Verified routed",
            r"^Routed PYQs",
        ],
    )
    final = base.start_for(
        headings,
        [r"^Final consolidated register notes(?:\b|$)"],
    )

    text = base.add_topic_visuals(config, text)
    text = base.add_session_orientations(text)
    headings = base.heading_offsets(text)
    part_i = base.start_for(headings, [r"^PART I\b"])
    practice = base.start_for(
        [(offset, title) for offset, title in headings if offset > part_i],
        [
            r"PYQ, practice and solved workbook",
            r"^Solved topic-specific MCQs$",
            r"^Verified routed",
            r"^Routed PYQs",
        ],
    )
    final = base.start_for(
        headings,
        [r"^Final consolidated register notes(?:\b|$)"],
    )

    preamble = text[:part_i]
    core_start = text.find("\n", part_i) + 1
    core = text[core_start:practice]
    practice_title = next(title for offset, title in headings if offset == practice)
    if re.search(
        r"PYQ, practice and solved workbook|^Solved topic-specific MCQs$",
        practice_title,
        re.I,
    ):
        practice_start = text.find("\n", practice) + 1
    else:
        practice_start = practice
    practice_block = text[practice_start:final]
    final_start = text.find("\n", final) + 1
    register = text[final_start:].strip()

    practice_headings = base.heading_offsets(practice_block)
    pyq_start = 0
    mcq_start = base.start_for(
        practice_headings,
        [r"^Original hard MCQ", r"^Original MCQ loop", r"^Original MCQs"],
    )
    mains_start = base.start_for(
        practice_headings,
        [r"^Original Mains practice", r"^Original solved Mains practice"],
    )
    pyqs = practice_block[pyq_start:mcq_start].strip()
    mcqs = practice_block[mcq_start:mains_start].strip()
    mains = practice_block[mains_start:].strip()

    assembled = "\n\n".join(
        [
            base.meta_demote(preamble).strip(),
            "## BASIC LEARNING SESSION",
            base.demote_one(core).strip(),
            "## BASIC MCQS / REMEDIATION",
            base.demote_one(mcqs).strip(),
            "## PYQS AND ANSWER PRACTICE",
            base.demote_one(pyqs).strip(),
            base.demote_one(mains).strip(),
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            prior._optional_owner(config),
            "## CONSOLIDATED REGISTER NOTES",
            register,
        ]
    ) + "\n"
    output = base.SOURCE_SESSION_ROOT / f"{config['key']}_Learning-Session.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8")
    return output


def workbook_gate(
    source_markdown: Path,
    config: dict[str, Any],
) -> dict[str, int]:
    text = source_markdown.read_text(encoding="utf-8")
    workbook = base.refresh.extract_v2_workbook_markdown(text)
    mcqs = len(re.findall(r"(?m)^####\s+(?:OM|RM)\d+\.", workbook))
    pyqs = len(
        re.findall(
            r"^#{3,5}\s+(?:PYQ|Verified(?: Adjacent)? PYQ|Prelims route)\b",
            workbook,
            re.MULTILINE | re.IGNORECASE,
        )
    )
    original_mains = len(
        re.findall(
            r"(?m)^#{3,5}\s+(?:M\d+\.|Original Solved Mains \d+\b)",
            workbook,
        )
    )
    expected_pyqs = config["exact_pyqs"] + config["supporting_pyqs"]
    if mcqs < 36 or pyqs < expected_pyqs or original_mains < 7:
        raise RuntimeError(
            f"Workbook gate failed: mcqs={mcqs}, pyqs={pyqs}, "
            f"expected_pyqs={expected_pyqs}, mains={original_mains}"
        )
    return {
        "mcqs_authored": mcqs,
        "pyq_routes_authored": pyqs,
        "original_mains_authored": original_mains,
    }


def count_original_mains(markdown: Path) -> int:
    text = markdown.read_text(encoding="utf-8")
    section = re.search(
        r"(?ims)^##\s+PYQS AND ANSWER PRACTICE\s*(.*?)"
        r"(?=^##\s+OPTIONAL ADVANCED DEPTH)",
        text,
    )
    if not section:
        return 0
    return len(
        re.findall(
            r"(?m)^#{3,5}\s+(?:M\d+\.|Original Solved Mains \d+\b)",
            section.group(1),
        )
    )


def export_flow(
    config: dict[str, Any],
    expected_count: int,
) -> tuple[Path, dict[str, Any]]:
    validation_path = (
        EXPORTS / f"{config['key']}-flow-learning-{DATE}-validation.json"
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "export_flow_learning_library.py"),
            "--all-completed",
            "--topic-key",
            config["key"],
            "--expected-topic-count",
            str(expected_count),
            "--manifest-date",
            DATE,
            "--validation-path",
            relative(validation_path),
        ],
        cwd=ROOT,
        check=True,
    )
    payload = json.loads(validation_path.read_text(encoding="utf-8"))
    row = next(
        item for item in payload["topics"] if item["topic_key"] == config["key"]
    )
    if payload["status"] != "passed" or row["status"] != "passed":
        raise RuntimeError(f"{config['key']}: Flow Learning export did not pass.")
    if not row["hashes"]["pdf"]["equal"] or not row["hashes"]["txt"]["equal"]:
        raise RuntimeError(f"{config['key']}: Flow Learning source bytes changed.")
    return validation_path, row


def completed_result(
    config: dict[str, Any],
) -> tuple[dict[str, Any], Path, Path] | None:
    completed = base.existing_result(config)
    if completed is None:
        return None
    record = prior.prior.latest_record(config)
    flow_validation = (
        EXPORTS / f"{config['key']}-flow-learning-{DATE}-validation.json"
    )
    if not flow_validation.is_file():
        return None
    flow_payload = json.loads(flow_validation.read_text(encoding="utf-8"))
    flow_row = next(
        item
        for item in flow_payload["topics"]
        if item["topic_key"] == config["key"]
    )
    clean_folder = ROOT / Path(completed["clean_library_path"].replace("\\", "/"))
    flow_folder = ROOT / Path(flow_row["destination_folder"].replace("\\", "/"))
    audit_path = ROOT / Path(completed["source_audit"].replace("\\", "/"))
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    source_path = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Polity"
        / "learning-sessions"
        / "v2"
        / "subject-wide-syllabus"
        / f"{config['key']}_Learning-Session.md"
    )
    ascii_path = ROOT / Path(completed["ascii_spec"].replace("\\", "/"))
    graph_path = ROOT / Path(completed["graphical_spec"].replace("\\", "/"))
    validation_path = ROOT / Path(completed["validation"].replace("\\", "/"))
    staged_path = EXPORTS / f"{config['key']}-staged-records-{DATE}.json"
    clean_completed = max(
        prior.prior.iso_mtime(path)
        for path in clean_folder.rglob("*")
        if path.is_file()
    )
    flow_completed = str(
        flow_payload.get("validated_at")
        or prior.prior.iso_mtime(flow_validation)
    )
    completed["completed_at"] = flow_completed
    completed["gate_times"] = {
        "A_started": audit["started_at"],
        "A_completed": audit["completed_at"],
        "B_completed": prior.prior.iso_mtime(source_path),
        "C_completed": prior.prior.iso_mtime(source_path),
        "D_completed": prior.prior.iso_mtime(ascii_path),
        "E_completed": prior.prior.iso_mtime(graph_path),
        "F_completed": prior.prior.iso_mtime(validation_path),
        "G_completed": prior.prior.iso_mtime(staged_path),
        "H_completed": clean_completed,
        "I_completed": flow_completed,
        "J_completed": flow_completed,
    }
    completed["approved"] = record["approved"]
    completed["counts"]["flow_pages"] = flow_row["pdf_validation"]["page_count"]
    completed["counts"]["original_mains"] = count_original_mains(source_path)
    completed["workbook_authoring_gate"] = workbook_gate(source_path, config)
    completed["flow_library_path"] = relative(flow_folder)
    completed["flow_validation"] = relative(flow_validation)
    completed["gates_passed"] = 10
    completed["preservation"] = {
        "existing_clean_mismatches": [],
        "existing_flow_mismatches": [],
        "prior_new_topic_mismatches": [],
    }
    return completed, clean_folder, flow_folder


def run() -> dict[str, Any]:
    expected_order = [f"polity-{number:02d}" for number in range(28, 33)]
    if [config["key"] for config in TOPICS] != expected_order:
        raise RuntimeError("Sequential topic order was altered.")
    prior.SUPPLEMENTS.update(SUPPLEMENTS)
    base.PANELS.update(PANELS)

    clean_baseline = prior.prior.topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={28, 29, 30, 31, 32},
    )
    flow_baseline = prior.prior.flow_topic_hashes(
        exclude_polity={28, 29, 30, 31, 32}
    )
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        resumed = completed_result(config)
        if resumed is not None:
            result, clean_folder, flow_folder = resumed
            results.append(result)
            locked_new.update(prior.prior.lock_hashes([clean_folder, flow_folder]))
            continue
        if prior.prior.compare_hashes(
            locked_new,
            {key: prior.prior.sha256(ROOT / key) for key in locked_new},
        ):
            raise RuntimeError("Previously generated topic artifacts changed before next gate.")

        gate_times: dict[str, str] = {"A_started": now()}
        live = base.live_checks(config)
        audit = base.write_audit(config, gate_times["A_started"], live)
        prior.augment_audit(config, audit)
        gate_times["A_completed"] = now()

        source_markdown = transform_source(config)
        gate_times["B_completed"] = now()

        workbook_authored = workbook_gate(source_markdown, config)
        gate_times["C_completed"] = now()

        final_markdown = (
            "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Polity\\"
            f"{SECTION}\\learning-sessions\\{config['key']}\\"
            f"{config['key']}_Complete-Learning-Session_{DATE}.md"
        )
        ascii_path = base.write_ascii_spec(config, final_markdown)
        gate_times["D_completed"] = now()

        graph_path = base.write_graphical_spec(
            config,
            source_markdown,
            ascii_path,
            final_markdown,
        )
        prior.prior.case_year_gate(config, ascii_path, graph_path)
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
            raise RuntimeError(f"{config['key']}: render validation failed.")
        gate_times["F_completed"] = now()

        record = prior.prior.latest_record(config)
        gate_times["G_completed"] = now()

        base.export_clean_topic(config)
        clean_folder = base.verify_four_folders(config)
        gate_times["H_completed"] = now()

        flow_validation, flow_row = export_flow(config, 60 + index)
        flow_folder = ROOT / Path(flow_row["destination_folder"].replace("\\", "/"))
        gate_times["I_completed"] = now()

        clean_mismatches = prior.prior.compare_hashes(
            clean_baseline,
            prior.prior.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={28, 29, 30, 31, 32},
            ),
        )
        flow_mismatches = prior.prior.compare_hashes(
            flow_baseline,
            prior.prior.flow_topic_hashes(
                exclude_polity={28, 29, 30, 31, 32}
            ),
        )
        if clean_mismatches or flow_mismatches:
            raise RuntimeError(
                f"{config['key']}: preservation regression: "
                f"clean={clean_mismatches[:5]} flow={flow_mismatches[:5]}"
            )
        prior_mismatches = prior.prior.compare_hashes(
            locked_new,
            {key: prior.prior.sha256(ROOT / key) for key in locked_new},
        )
        if prior_mismatches:
            raise RuntimeError(
                f"{config['key']}: prior generated artifacts changed: "
                f"{prior_mismatches[:5]}"
            )
        gate_times["J_completed"] = now()

        final_markdown_path = ROOT / Path(row["paths"]["markdown"].replace("\\", "/"))
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
                "original_mains": count_original_mains(final_markdown_path),
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
        locked_new.update(prior.prior.lock_hashes([clean_folder, flow_folder]))

    state = {
        "schema_version": 1,
        "batch_id": BATCH_ID,
        "created_at": now(),
        "strict_order": expected_order,
        "topics": results,
        "existing_clean_topic_artifact_count": len(clean_baseline),
        "existing_flow_topic_artifact_count": len(flow_baseline),
        "existing_clean_hash_mismatches": prior.prior.compare_hashes(
            clean_baseline,
            prior.prior.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={28, 29, 30, 31, 32},
            ),
        ),
        "existing_flow_hash_mismatches": prior.prior.compare_hashes(
            flow_baseline,
            prior.prior.flow_topic_hashes(
                exclude_polity={28, 29, 30, 31, 32}
            ),
        ),
        "prior_generated_topic_hash_mismatches": prior.prior.compare_hashes(
            locked_new,
            {key: prior.prior.sha256(ROOT / key) for key in locked_new},
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
