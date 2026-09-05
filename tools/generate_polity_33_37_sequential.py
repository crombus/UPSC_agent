"""Generate Polity learner-v2 topics 33-37 in strict preservation-safe order."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_28_32_sequential as prior


base = prior.base
common = prior.prior
preserve = common.prior
case_years = prior.case_years
ROOT = prior.ROOT
DATE = prior.DATE
SECTION = prior.SECTION
EXPORTS = prior.EXPORTS
FINAL_LIBRARY = prior.FINAL_LIBRARY
FLOW_LIBRARY = prior.FLOW_LIBRARY
BATCH_ID = "polity-33-37-sequential-batch-2026-08-24"


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
        "polity-33",
        "Attorney General and Advocate General",
        "upsc-ai-kit\\knowledge\\Polity\\33_Attorney-General-and-Advocate-General_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Attorney-General.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\33_Attorney-General-and-Advocate-General.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
        ],
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.legalaffairs.gov.in/static/uploads/2025/12/15190a2d8b5f8d8ef9cc9c711d7e8083.pdf",
            "https://www.legalaffairs.gov.in/static/uploads/2026/03/ad2f61f6794d21d0c02c231d013eaebb.pdf",
            "https://www.sci.gov.in/supreme-court-rules-2013/",
            "https://www.indiacode.nic.in/handle/123456789/1631",
            "https://api.sci.gov.in/jonew/bosir/orderpdf/2812218.pdf",
        ],
        2,
        1,
        "The official Constitution, consolidated Law Officers Rules, the "
        "Law Officers (Conditions of Service) Amendment Rules, 2026, Supreme "
        "Court materials and State law-officer pages were rechecked on "
        "24 August 2026. Officeholder names are deliberately not frozen.",
        "Articles 76 and 165 create constitutional law officers, but neither "
        "creates tenure security comparable to an independent watchdog. "
        "Audience, legislative participation and professional practice must "
        "be separated from assignment, voting power and conflict restrictions.",
        [
            "Articles 76 and 165 with qualification, appointment, pleasure and remuneration",
            "Articles 88 and 177 participation without membership or vote",
            "Articles 105(4) and 194(4) privilege extension and exact limits",
            "advice, representation, Article 143 work and right of audience",
            "Law Officers Rules, private practice, conflicts and permissions",
            "AGI-SG-ASG and State law-officer constitutional classification",
            "AGI-Advocate General comparison, ethics, accountability and reform",
        ],
        visual_sessions=[1, 2, 4, 6, 8, 10, 12, 13, 15, 16, 17, 19, 22, 25, 27, 30],
    ),
    topic(
        "polity-34",
        "NITI Aayog",
        "upsc-ai-kit\\knowledge\\Polity\\34_NITI-Aayog_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\NITI-Aayog.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\34_NITI-Aayog.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\15_Monitoring-Evaluation-and-Outcomes.md",
        ],
        [
            "https://www.niti.gov.in/about-us/niti-aayog-constitution/cabinet-secretariat-resolution-dated-01-01-2015",
            "https://www.niti.gov.in/about-us/objectives-and-features",
            "https://www.niti.gov.in/about-us/niti-governing-council-meetings",
            "https://www.niti.gov.in/node/2337",
            "https://www.niti.gov.in/publication/annual-report",
            "https://www.niti.gov.in/reports-on-sdg",
        ],
        1,
        1,
        "The 1 January 2015 Cabinet resolution, July 2024 composition "
        "notification, official 11th Governing Council material dated "
        "11 June 2026 and current NITI programme pages were rechecked on "
        "24 August 2026. Officeholder lists and State rankings are not frozen.",
        "NITI Aayog is an executive policy platform, not a constitutional or "
        "statutory transfer authority. Its rankings, missions and evaluation "
        "tools influence through evidence, convening and reputation; they do "
        "not become law, Finance Commission awards or guaranteed outcomes.",
        [
            "2015 Cabinet resolution, Planning Commission replacement and legal status",
            "objectives, principles, Team India and knowledge-innovation roles",
            "composition with notification-sensitive executive categories",
            "Governing Council, Regional Councils and federal dialogue",
            "cooperative and competitive federalism and State support",
            "monitoring, evaluation, SDGs and aspirational initiatives within limits",
            "Planning Commission-Finance Commission-GST Council comparisons and reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 7, 9, 10, 12, 14, 16, 17, 20, 21, 24, 27],
    ),
    topic(
        "polity-35",
        "NHRC and SHRC",
        "upsc-ai-kit\\knowledge\\Polity\\35_NHRC-and-SHRC_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\NHRC-and-SHRC.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\35_NHRC-and-SHRC.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Commissions-SC-ST-BC.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Political-Theory\\basic\\17_Human-Rights-Civil-Liberties-and-Democratic-Rights.md",
        ],
        [
            "https://www.indiacode.nic.in/handle/123456789/15709",
            "https://nhrc.nic.in/acts-and-rules/protection-human-rights-act-1993",
            "https://nhrc.nic.in/about-us/composition_of_commission",
            "https://www.ohchr.org/en/instruments-mechanisms/instruments/principles-relating-status-national-institutions-paris",
            "https://ganhri.org/membership/",
            "https://api.sci.gov.in/jonew/judis/25688.pdf",
            "https://api.sci.gov.in/jonew/judis/43775.pdf",
        ],
        2,
        1,
        "India Code, NHRC, OHCHR, GANHRI and Supreme Court sources were "
        "rechecked on 24 August 2026. GANHRI's public membership listing "
        "continues to be reported with the challenged 2025 downgrade "
        "recommendation kept distinct from a completed status change.",
        "NHRC and SHRC are statutory recommendatory commissions with strong "
        "inquiry and publicity tools but no general power to convict or issue "
        "self-executing compensation orders. The one-year bar and armed-forces "
        "procedure remain current law unless Parliament changes them.",
        [
            "Protection of Human Rights Act, 1993 and 2006/2019 amendments",
            "statutory human-rights definition and enforceability filter",
            "NHRC-SHRC composition, committees, qualifications, tenure and removal",
            "section 12 functions, civil-court powers and investigative support",
            "sections 18, 19 and 36 remedies, limits and reporting",
            "Human Rights Courts, overlap, federal jurisdiction and armed forces",
            "Paris Principles, accreditation, case law, capacity limits and reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17],
    ),
    topic(
        "polity-36",
        "CIC and SIC",
        "upsc-ai-kit\\knowledge\\Polity\\36_CIC-and-SIC_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\CIC-and-SIC.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\36_CIC-and-SIC.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\06_Digital-Public-Infrastructure-and-Data-Governance.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\15_Transparency-RTI-and-Information-Sharing.md",
        ],
        [
            "https://dopt.gov.in/sites/default/files/RTI%20Act%202005%20%28updated%20as%20on%2018-11-2025%29.pdf",
            "https://dopt.gov.in/sites/default/files/RTI%20Rules%202019.pdf",
            "https://dopt.gov.in/rti/proactive-disclosures/important-files-ir-division",
            "https://cic.gov.in/annual-reports",
            "https://cic.gov.in/complaint",
            "https://api.sci.gov.in/jonew/judis/38918.pdf",
            "https://api.sci.gov.in/jonew/judis/38344.pdf",
        ],
        1,
        0,
        "The DoPT consolidated RTI Act as on 18 November 2025, the 2019 "
        "service-condition Rules, CIC materials, the 13 November 2025 DPDP "
        "commencement control and Supreme Court judgments were rechecked on "
        "24 August 2026. Officeholders and backlog totals are not frozen.",
        "Information Commissions are statutory complaint and appellate bodies, "
        "not ordinary courts or record-creation agencies. The 2019 amendment "
        "shifted service conditions to Central rules, while the current privacy "
        "clause must still be read with section 8(2), severability and review.",
        [
            "RTI Act status, constitutional right-to-know root and definitions",
            "PIO-FAA-Commission route with transfer, fee and exact timelines",
            "CIC-SIC composition, appointment, eligibility and jurisdiction",
            "2019 amendment and current delegated service-condition rules",
            "sections 18-20 inquiry, appeal, orders, compensation and penalty",
            "sections 8, 9, 10, 11 and 24 exemptions and procedures",
            "case law, no-record-creation boundary, privacy, backlog and reform",
        ],
        visual_sessions=[1, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 18, 21, 26],
    ),
    topic(
        "polity-37",
        "CVC and CBI",
        "upsc-ai-kit\\knowledge\\Polity\\37_CVC-and-CBI_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\CVC-and-CBI.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\37_CVC-and-CBI.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Lokpal-and-Lokayuktas.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\20_Anti-Corruption-Institutions.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\21_Protecting-Honest-Officials-and-Vigilance-Administration.md",
        ],
        [
            "https://www.indiacode.nic.in/handle/123456789/2068",
            "https://www.indiacode.nic.in/handle/123456789/2258",
            "https://cvc.gov.in/",
            "https://cbi.gov.in/",
            "https://dopt.gov.in/",
            "https://api.sci.gov.in/supremecourt/2018/15968/15968_2018_Judgement_15-Feb-2019.pdf",
        ],
        1,
        1,
        "The CVC Act, DSPE Act, Lokpal and Prevention of Corruption Act "
        "interfaces, official CVC/CBI/DoPT descriptions and controlling "
        "Supreme Court decisions were rechecked on 24 August 2026. "
        "Officeholders, consent-State counts and live caseloads are not frozen.",
        "CVC supervision is field-specific and advisory; CBI's organisation is "
        "executive-created while DSPE police powers are statutory. State consent "
        "governs the ordinary State-area route, subject to exceptional "
        "constitutional-court directions and precise pending-case rules.",
        [
            "Santhanam trajectory, CVC Act 2003 and CBI-DSPE legal identity",
            "CVC composition, appointment, tenure, removal and section 8 functions",
            "CVO system, vigilance advice, prosecution sanction and Lokpal interface",
            "DSPE powers, offence notification, divisions and investigative mandate",
            "superintendence split and current Director appointment/tenure rules",
            "general/specific State consent and constitutional-court directions",
            "case law, comparisons, federalism, independence and accountable reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 17, 19, 22],
    ),
]


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-33": [
        (
            "Constitutional map: two law officers, two legislatures and no voting power",
            "law-officer-constitutional-map",
            [1, 2, 4, 13, 14, 15],
            """ROOT QUESTION
How does government receive authoritative legal advice without creating another court?

UNION
Article 76 -> Attorney General for India.
Article 88 -> speak and participate in both Houses, joint sitting and named committees.
Article 105(4) -> relevant parliamentary privileges extend; no membership or vote follows.

STATE
Article 165 -> Advocate General for the State.
Article 177 -> speak and participate in the State legislature and named committees.
Article 194(4) -> relevant legislative privileges extend; no membership or vote follows.

CORE LIMIT
constitutional law officer != judge, minister, legislator, prosecutor or independent tribunal.""",
        ),
        (
            "Appointment, qualification, pleasure tenure and remuneration architecture",
            "law-officer-office-lifecycle",
            [3, 5, 6, 7, 8, 9],
            """ATTORNEY GENERAL
President appoints | qualification for Supreme Court Judge under Article 124(3).
No constitutional age ceiling for holding AGI office.
Office during President's pleasure | no constitutional fixed term or removal process.
Remuneration as President determines; current administrative terms may come from rules.

ADVOCATE GENERAL
Governor appoints | qualification for High Court Judge under Article 217(2).
Office during Governor's pleasure | no constitutional fixed term or removal process.
Remuneration as Governor determines.

TRAP
qualification rule != tenure rule; a rule-based Union term does not displace pleasure.""",
        ),
        (
            "Advice, representation, Article 143 work and the audience-assignment distinction",
            "law-officer-duty-audience-system",
            [10, 11, 12],
            """ARTICLE 76 DUTY
advise Government of India on legal matters referred by President
-> perform assigned legal duties
-> discharge functions conferred by Constitution or law.

OPERATIONAL REPRESENTATION
Supreme Court Union cases | Article 143 references | High Court appearance when assigned.

RIGHT OF AUDIENCE
AGI has an express constitutional right of audience in all courts in India.

THREE DISTINCT QUESTIONS
may the advocate practise? | does the advocate have audience? | is this brief assigned?

LIMIT
legal opinion advises the executive; it is not a judgment, veto or binding court order.""",
        ),
        (
            "Articles 88, 177, 105(4) and 194(4): participation and privilege boundaries",
            "law-officer-legislature-participation",
            [13, 14, 15],
            """PARLIAMENT
AGI may speak and otherwise take part in both Houses, a joint sitting
and a committee of which the AGI is named a member.

STATE LEGISLATURE
Advocate General may speak and otherwise take part in the House or Houses
and a committee of which the Advocate General is named a member.

COMMON LIMIT
no vote by virtue of the office | no elected membership | no ministerial responsibility.

PRIVILEGE RULE
Articles 105(4) and 194(4) extend specified privileges for authorised participation.
They do not create blanket immunity for private conduct outside legislative proceedings.""",
        ),
        (
            "Professional practice, Rule 8 conflicts, permissions and confidentiality",
            "law-officer-professional-ethics-matrix",
            [16, 22, 23, 25],
            """UNION LAW-OFFICER PERIMETER
private professional work is permitted only within applicable conduct restrictions.

PROHIBITED OR CONTROLLED
brief against Government of India or covered public entities
| advice where the officer advised or is likely to advise government
| criminal defence without permission
| company or corporation office without permission.

ETHICAL DUTIES
conflict check -> disclosure -> screen or recusal -> authorised brief
-> candour to court -> protect lawful confidentiality.

CONTEMPT CONSENT
section 15 gate concerns specified private criminal-contempt motions;
Supreme Court may still act suo motu.

TRAP
permitted practice != unrestricted practice and professional privilege has legal exceptions.""",
        ),
        (
            "AGI, Solicitor General, Additional Solicitors General and State law-officer ecology",
            "law-officer-classification-hierarchy",
            [17, 18, 20],
            """CONSTITUTIONAL OFFICES
AGI -> Article 76 | Advocate General -> Article 165.

UNION EXECUTIVE LAW OFFICERS
Solicitor General and Additional Solicitors General assist under executive rules.
Prominence and ranking do not convert them into constitutional or statutory offices.

STATE ECOLOGY
Advocate General is constitutional.
Additional Advocate Generals, standing counsel and panel counsel depend on State law or rules.

OTHER BOUNDARIES
Law Minister -> political executive.
Public Prosecutor -> criminal-procedure office.
CAG -> independent constitutional auditor.

EXAM RULE
classify by creating source before comparing function or prestige.""",
        ),
        (
            "Attorney General and Advocate General: complete federal comparison",
            "ag-advocate-general-comparison",
            [19, 21],
            """DIMENSION              ATTORNEY GENERAL              ADVOCATE GENERAL
Source                 Article 76                    Article 165
Appointer               President                     Governor
Qualification           Supreme Court Judge route     High Court Judge route
Advice                  Government of India           State Government
Audience                all courts in India           State-law position must be checked
Legislature             Article 88                    Article 177
Vote                    none by office                none by office
Privilege extension     Article 105(4)                Article 194(4)
Pleasure                President                     Governor

CAUTION
Article 76(3)'s express all-India audience text must not be silently imported into Article 165.""",
        ),
        (
            "Independence, government confidence and fair State panel appointments",
            "law-officer-independence-case",
            [23, 24, 26, 27, 28],
            """STRUCTURAL TENSION
government needs trusted counsel
-> pleasure tenure and assignment control
-> risk of politicisation, discontinuity and selective briefing.

PROFESSIONAL COUNTERWEIGHT
court duty + qualification + audience + conflict rules + reasoned legal advice.

State of Punjab v. Brijeshwar Singh Chahal (2016)
State panel-lawyer selection must follow fair, objective and suitability-based standards.
The judgment did not replace the Governor's Article 165 appointment of Advocate General.

ACCOUNTABILITY
executive responsibility for decisions | judicial review of legality
| professional discipline | legislative and public scrutiny.

REFORM
transparent criteria + conflict register + reasoned recusals + litigation-management audit.""",
        ),
        (
            "Current controls, PYQ routes, traps and qualified answer synthesis",
            "law-officer-answer-synthesis",
            [29, 30],
            """DATED CONTROL: 24 AUGUST 2026
Constitution and current Union Law Officers Rules control; officeholder names are omitted.

PYQ ROUTES
2019 GS-II -> AGI as chief legal adviser.
2025 GS-II -> responsibilities, rights and limitations.
2022 Prelims -> AGI versus Solicitor General constitutional position.

PRELIMS FIREWALL
no fixed constitutional term | pleasure != impeachment
| audience != assigned brief | speak != vote
| privilege != blanket immunity | SG/ASG != constitutional
| private practice != conflict-free practice.

MAINS SPINE
constitutional source -> qualification and tenure -> advice and representation
-> enabling rights -> professional limits -> independence tension
-> transparent, ethical and accountable law-officer verdict.""",
        ),
    ],
    "polity-34": [
        (
            "2015 Cabinet resolution, executive status and Planning Commission transition",
            "niti-origin-status-transition",
            [1, 2, 7, 8],
            """ROOT PROBLEM
How can national development strategy coordinate Union, States and local needs
without reviving central command planning?

1 JANUARY 2015 CABINET RESOLUTION
creates National Institution for Transforming India, NITI Aayog.

LEGAL STATUS
executive | non-constitutional | non-statutory | recommendation-based.

TRANSITION
Planning Commission model -> NITI policy platform.
Five-Year Plans ended; plan/non-plan budget classification ended through later budget reform.

CONTINUITY
both institutions arose through Union executive resolutions.

LIMIT
replacement did not transfer Article 280, budget, legislative or taxing powers to NITI.""",
        ),
        (
            "Foundational objectives, principles and the Team India-knowledge dual role",
            "niti-objective-principle-map",
            [2, 3, 19],
            """TEAM INDIA ROLE
shared national vision with active State participation
-> cooperative federal dialogue -> policy coordination.

KNOWLEDGE AND INNOVATION ROLE
long-term strategy | best practice | research | technology
| capacity support | monitoring and feedback.

FOUNDATIONAL PRINCIPLES
bottom-up planning | inclusion of vulnerable sections
| village-to-national aggregation | partnership | outcome orientation.

POLICY CHAIN
diagnose problem -> consult -> design option -> advise competent government
-> implement through law, budget and administration -> evaluate -> revise.

LIMIT
an official objective describes mandate; it does not prove achievement or create coercive power.""",
        ),
        (
            "Composition: political leadership, expert capacity and notification-sensitive categories",
            "niti-composition-architecture",
            [4],
            """CHAIRPERSON
Prime Minister.

FEDERAL FORUM
Governing Council includes Chief Ministers and relevant Union Territory leadership.

EXECUTIVE-EXPERT SIDE
Vice-Chairperson | full-time members | part-time members from institutions
| ex-officio Union Ministers | special invitees | CEO.

FOUNDATIONAL LIMITS
part-time members: maximum two | ex-officio members: maximum four.

NOTIFICATION CONTROL
names, portfolios, invitees and exact composition may be reconstituted.
Use the current official notification only when a dated fact is required.

TRAP
CEO or Vice-Chairperson status is executive design, not constitutional tenure.""",
        ),
        (
            "Governing Council, Regional Councils and cooperative federal process",
            "niti-federal-council-system",
            [5, 6, 9, 11, 12],
            """GOVERNING COUNCIL
continuing development-policy forum chaired by Prime Minister
-> State and Union Territory leaders deliberate on shared priorities.

REGIONAL COUNCILS
temporary issue-specific groups for more than one State or a region
-> chaired or convened under the resolution's executive design.

COOPERATIVE FEDERALISM
consultation + agenda sharing + joint diagnosis + peer learning + follow-up.

STATE SUPPORT
State Support Mission and State Institutions for Transformation
offer capacity and policy-system assistance; uptake varies.

BOTTOM-UP CLAIM
village plans should aggregate upward, but local planning depends on State law and capacity.

LIMIT
Council consensus is political coordination, not a second chamber or binding intergovernmental law.""",
        ),
        (
            "Competitive federalism, dashboards and the evidence-to-action mechanism",
            "niti-competitive-federalism-cycle",
            [10, 13, 20],
            """COMPETITIVE FEDERALISM
common indicators -> comparable performance -> public ranking or delta
-> peer pressure -> administrative attention -> corrective action.

DATA-TO-POLICY LOOP
define outcome -> select indicator -> establish baseline -> collect and verify
-> compare -> diagnose cause -> intervene -> reassess.

POTENTIAL GAIN
visibility, learning, priority focus and faster feedback without command power.

RISKS
Goodhart's law | gaming | data lag | unequal capacity
| composite-index opacity | correlation mistaken for causation.

SAFE USE
publish method and uncertainty; pair rank with levels, change and field evidence.""",
        ),
        (
            "Aspirational initiatives, SDG localisation, DMEO and innovation within bounds",
            "niti-programme-monitoring-map",
            [14, 15, 16, 17, 18],
            """ASPIRATIONAL DISTRICTS / BLOCKS
convergence + collaboration + competition
-> indicator tracking and delta improvement
-> implementation remains with governments and field agencies.

SDG LOCALISATION
national goals -> indicator framework -> State and local comparison
-> policy attention; index publication is not constitutional power.

DMEO
monitoring and evaluation support -> evidence on design, process and outcomes.

ATAL INNOVATION MISSION
executive programme under NITI; current architecture depends on Cabinet and programme controls.

BOUNDARY
NITI may coordinate, study, rank and recommend.
It does not legislate, appropriate money or guarantee district outcomes.""",
        ),
        (
            "NITI, Planning Commission, Finance Commission and GST Council compared",
            "niti-institution-comparison",
            [7, 21, 22],
            """NITI AAYOG
2015 executive resolution | strategy, dialogue, knowledge and monitoring | no transfer award.

PLANNING COMMISSION
1950 executive resolution | Five-Year Plans and plan-resource influence | abolished.

FINANCE COMMISSION
Article 280 | periodic expert recommendations on tax distribution and grants.

GST COUNCIL
Article 279A | continuing Union-State forum for GST recommendations.

INTER-STATE COUNCIL
Article 263 route | intergovernmental coordination and advice.

STATE FINANCE COMMISSION
Articles 243I and 243Y | State-local fiscal recommendations.

TRAP
strategy, fiscal distribution, tax coordination and intergovernmental consultation are distinct.""",
        ),
        (
            "Strengths, accountability deficits, reform and the dated federal anchor",
            "niti-strength-limit-reform",
            [23, 24, 25, 26],
            """STRENGTHS
flexibility | high-level convening | cross-sector knowledge
| State dialogue | rapid policy studies | monitoring and innovation.

LIMITS
non-binding advice | central agenda power | weak legislative reporting
| data quality | uncertain follow-through | capacity asymmetry.

REFORM
publish consultation records and evaluation methods
-> independent data audit -> State agenda windows
-> action-taken tracking -> parliamentary scrutiny without statutory rigidity.

DATED ANCHOR
11th Governing Council, 11 June 2026:
"Inclusive Human Development for Viksit Bharat@2047."

CAUTION
meeting theme proves agenda and convening, not implementation success or a justiciable target.""",
        ),
        (
            "PYQ routes, close-option traps and qualified policy-platform synthesis",
            "niti-answer-synthesis",
            [27],
            """PYQ ROUTES
2018 GS-III -> principles of NITI versus Planning Commission.
2019 Prelims -> Atal Innovation Mission institutional location.

PRELIMS FIREWALL
executive != unconstitutional | no Article 280 allocation
| Governing Council != legislature | Regional Council != Zonal Council
| index != binding power | plan/non-plan abolition != NITI decree.

MAINS SPINE
2015 origin -> legal status -> objectives -> composition
-> federal mechanism -> evidence tools -> comparison
-> strength and deficit -> accountable reform.

QUALIFIED VERDICT
NITI is influential when credible evidence, State ownership and competent implementation converge;
without them, soft coordination cannot substitute for law, finance or administrative capacity.""",
        ),
    ],
    "polity-35": [
        (
            "PHRA evolution, statutory identity and the enforceable human-rights field",
            "human-rights-commission-foundation",
            [1, 2],
            """PROTECTION OF HUMAN RIGHTS ACT, 1993
deemed commencement 28 September 1993 | presidential assent 8 January 1994.
Amendments in 2006 and 2019 reshape design; commissions remain statutory.

SECTION 2(d)
rights relating to life, liberty, equality and dignity
-> guaranteed by Constitution or embodied in defined International Covenants
-> enforceable by courts in India.

SECTION 2(f)
ICCPR + ICESCR + notified UN General Assembly covenant or convention.

INSTITUTIONAL MAP
NHRC at Union level | SHRCs at State level | Human Rights Courts as trial route.

LIMIT
human-rights importance does not convert NHRC or SHRC into a constitutional court.""",
        ),
        (
            "NHRC and SHRC composition, appointment, tenure and removal",
            "human-rights-commission-office-design",
            [3, 4, 5],
            """NHRC
Chair: former CJI or Supreme Court Judge.
Judicial members: one Supreme Court route + one Chief Justice of High Court route.
Three experts in human rights, at least one woman.
Seven specialised officeholders are deemed members for section 12(b)-(j).

SHRC
Chair: former Chief Justice or Judge of High Court.
One judicial member + one human-rights expert.

APPOINTMENT
President for NHRC | Governor for SHRC
after statutory committee recommendation; vacancy does not alone invalidate proceedings.

TERM
three years, subject to age 70 and current reappointment rules.

REMOVAL
President removes NHRC and SHRC members under the Act;
proved misbehaviour or incapacity uses Supreme Court inquiry.""",
        ),
        (
            "Section 12 functions, civil-court powers and investigative support",
            "human-rights-function-inquiry-system",
            [6, 7],
            """SECTION 12 FUNCTIONS
suo motu or petition inquiry | court intervention with approval
| institution visits | review constitutional/legal safeguards
| review factors inhibiting rights | study treaties
| research | literacy | NGO encouragement | other necessary functions.

SECTION 13 INQUIRY POWERS
summon and examine on oath | documents | affidavits
| public records | commissions | specified additional powers.

SECTION 14 INVESTIGATION
Commission may use Central or State government agency or officers with consent.

PROCEDURAL FAIRNESS
notice and hearing where reputation or conduct may be prejudicially affected.

LIMIT
civil-court evidence powers support inquiry;
they do not create ordinary civil or criminal jurisdiction.""",
        ),
        (
            "Complaint-to-recommendation procedure, one-year bar and legal effect",
            "human-rights-remedy-accountability-chain",
            [7, 8, 9],
            """ENTRY
complaint or suo motu material -> jurisdiction screen -> inquiry or investigation.

SECTION 36
no parallel inquiry where another named commission is seized.
Section 36(2): no inquiry after one year from the alleged violative act.

SECTION 18 OUTPUTS
recommend compensation or damages
| recommend prosecution or other action
| approach Supreme Court or High Court
| recommend immediate interim relief.

FOLLOW-UP
government comments/action report ordinarily within one month
-> Commission publishes report, recommendation and response.

LEGAL EFFECT
recommendation carries public and institutional weight but is not a self-executing decree.

TRAP
action-taken reporting != mandatory acceptance and grave facts alone do not erase section 36(2).""",
        ),
        (
            "Armed-forces procedure and Human Rights Courts: two special routes",
            "human-rights-special-procedure-map",
            [10, 11],
            """SECTION 19: ARMED FORCES
NHRC may act on its own motion or petition
-> seek Central Government report
-> either not proceed or make recommendation
-> Central Government reports action within three months
-> Commission publishes material.

LIMIT
ordinary inquiry architecture is replaced by this special report-based route.

SECTIONS 30-31: HUMAN RIGHTS COURTS
State Government, with concurrence of Chief Justice of High Court,
may specify a Court of Session for speedy trial of human-rights offences.
Special Public Prosecutor: Public Prosecutor or advocate with at least seven years' practice.

BOUNDARY
Human Rights Court tries offences; NHRC or SHRC inquires and recommends.""",
        ),
        (
            "NHRC-SHRC jurisdiction, overlap and specialised-commission coordination",
            "human-rights-federal-overlap-matrix",
            [5, 9, 14],
            """NHRC
national statutory mandate subject to PHRA exclusions and transfer rules.

SHRC
inquires into matters relatable to State List and Concurrent List;
section 29 adapts functions and omits treaty study.

TRANSFER
NHRC may transfer a complaint to a competent SHRC under statutory conditions.

OVERLAP
NCSC, NCST and NCBC have constitutional safeguard mandates.
Women, child, minority and disability bodies have specialised statutory fields.

COORDINATION
common intake metadata -> reasoned referral -> no duplicate inquiry
-> joint thematic work -> preserve specialist voice.

LIMIT
an umbrella merger cannot absorb constitutional commissions through ordinary PHRA amendment.""",
        ),
        (
            "Paris Principles, GANHRI accreditation and current-status discipline",
            "human-rights-paris-accreditation",
            [12],
            """PARIS PRINCIPLES, 1993
broad legal mandate | pluralism | open appointment
| adequate resources | stable tenure | independent methods | accessibility.

DOMESTIC TEST
PHRA mandate and inquiry powers
versus police/deputation dependence, short terms, selection opacity and weak follow-up.

GANHRI CONTROL
March 2025 SCA recommended B downgrade.
India challenged with required Bureau support.
Public membership page continued to list India as A on the 24 August 2026 control.

SAFE LANGUAGE
current public A listing + unresolved official scrutiny.

TRAP
recommendation under challenge != completed downgrade;
A listing != proof of perfect Paris-Principles compliance.""",
        ),
        (
            "Three human-rights case-law boundaries",
            "human-rights-case-law-map",
            [13],
            """Paramjit Kaur v. State of Punjab (1999)
Supreme Court used NHRC as an expert body assisting Article 32 jurisdiction.
This constitutional assignment is not ordinary PHRA jurisdiction.

N.C. Dhoundial v. Union of India (2003)
section 36(2) is a jurisdictional bar;
a completed violation does not become a daily continuing wrong merely through non-reparation.

EEVFAM (2016)
excessive-force allegations require lawful inquiry under Article 32 oversight;
NHRC is a valuable route but not exclusive and recommendations were not made generally binding.

SYNTHESIS
Court-assigned expertise may exceed the ordinary route,
but an autonomous statutory commission remains bound by statutory limits.""",
        ),
        (
            "Enforcement limits, reform, PYQ routes and qualified synthesis",
            "human-rights-answer-synthesis",
            [15, 16],
            """STRUCTURAL LIMITS
recommendatory outputs | one-year bar | armed-forces report route
| government-linked investigation support | federal and overlap boundaries.

PRACTICAL LIMITS
vacancies | staff/resources | delayed reports | uneven SHRC capacity
| weak Human Rights Court routing | limited civil-society trust.

REFORM
independent multidisciplinary investigation cadre
-> open plural appointments -> time-bound reasoned response
-> grave/concealed-violation limitation reform
-> safeguarded armed-forces fact-finding -> interoperable referrals.

PYQ ROUTES
2018 umbrella-commission debate | 2021 limitations and remedies
| 2023 body-classification support.

MAINS VERDICT
strengthen fact-finding, independence and follow-through without misdescribing NHRC as a court.""",
        ),
    ],
    "polity-36": [
        (
            "Right to know, RTI Act identity and the information-public-authority vocabulary",
            "rti-foundation-vocabulary",
            [1, 2],
            """CONSTITUTIONAL ROOT
Article 19(1)(a) right to receive information for democratic participation,
subject to lawful restrictions and competing rights.

RTI ACT, 2005
statutory request, proactive-disclosure, appeal, complaint and enforcement machinery.

INFORMATION
material in any form held by or under control of public authority,
including accessible private-body information under another law.

PUBLIC AUTHORITY
Constitution | parliamentary or State law | government notification/order
| substantially financed bodies and NGOs under section 2(h).

RIGHT TO INFORMATION
inspection | notes/extracts | certified copies | certified samples | electronic copies.

LIMIT
RTI gives access to existing covered records; it does not compel a new answer, opinion or record.""",
        ),
        (
            "PIO-FAA-Commission chain, transfers and statutory timelines",
            "rti-access-remedy-timeline",
            [3, 4, 5, 6],
            """PROACTIVE DISCLOSURE: SECTION 4
records and key information disclosed by default -> fewer individual requests.

REQUEST
PIO or SPIO receives | APIO forwarding adds five days where applicable.
No reasons required; only contact details needed for communication.

TRANSFER: SECTION 6(3)
to the concerned public authority as soon as practicable, within five days.

RESPONSE
ordinary: 30 days | life or liberty: 48 hours
| third-party process: decision within 40 days | delay: information free.

REMEDY CHAIN
PIO decision/deemed refusal -> First Appellate Authority, ordinarily 30 days
-> CIC or SIC second appeal, ordinarily 90 days.

TRAP
section 18 complaint and section 19 disclosure appeal are not interchangeable.""",
        ),
        (
            "CIC and SIC composition, appointment committees, eligibility and jurisdiction",
            "information-commission-office-design",
            [7, 8, 9],
            """CIC
Chief Information Commissioner + up to ten Information Commissioners.
President appoints on committee advice:
Prime Minister + Lok Sabha Opposition Leader/substitute + Union Cabinet Minister.

SIC
State Chief Information Commissioner + up to ten State Information Commissioners.
Governor appoints on committee advice:
Chief Minister + Assembly Opposition Leader/substitute + State Cabinet Minister.

ELIGIBILITY
eminence in public life with knowledge/experience in listed fields.

DISQUALIFICATIONS
MP/MLA | office of profit | political party link | business or profession.

JURISDICTION
CIC for Central public authorities | SIC for State public authorities.

LIMIT
appointment committees do not make the commissions constitutional bodies.""",
        ),
        (
            "2019 amendment, current Rules, tenure and protected removal",
            "information-commission-independence-lifecycle",
            [10, 11, 12],
            """2019 AMENDMENT
removed Act-fixed five-year term and Election-Commission-linked conditions
-> Central Government prescribes term, pay and service conditions by rules.

2019 RULES
ordinary term: three years | age ceiling: 65.
fixed current pay varies by office under the Rules.

REAPPOINTMENT
same office: barred; an Information Commissioner may become Chief,
subject to aggregate statutory maximum.

REMOVAL FOR PROVED MISBEHAVIOUR OR INCAPACITY
President for CIC officers | Governor for SIC officers
after Supreme Court inquiry.

DIRECT GROUNDS
insolvency | conviction involving moral turpitude | outside paid employment
| infirmity | prejudicial financial or other interest.

AUTONOMY CONCERN
executive rule-making now controls core conditions of adjudicators reviewing that executive.""",
        ),
        (
            "Sections 18-20: complaint, appeal, inquiry, orders, compensation and penalty",
            "information-commission-power-remedy-map",
            [13, 14, 15],
            """SECTION 18 COMPLAINT
inability to file | refusal | no reply | unreasonable fee
| incomplete, misleading or false information -> inquiry on reasonable grounds.

INQUIRY POWERS
civil-court powers + direct inspection of covered records;
no record may be withheld from Commission on a statutory exemption claim.

SECTION 19 SECOND APPEAL
PIO bears burden to justify denial.
Commission may order disclosure and systemic compliance under section 19(8).
Orders bind within the statutory field, subject to constitutional review.

REMEDIES
compensation to complainant/appellant
| section 20 personal PIO penalty: Rs 250 per day, maximum Rs 25,000
| disciplinary recommendation.

DUE PROCESS
reasonable opportunity and statutory conditions precede penalty.""",
        ),
        (
            "Exemptions, public interest, severability, third parties and security bodies",
            "rti-exemption-procedure-system",
            [16, 17, 18, 19, 20],
            """SECTION 8
specified protected interests; current section 8(1)(j) covers personal information.
Section 8(2) general public-interest override remains.

SECTION 9
copyright-based refusal where access would infringe copyright of a person other than State.

SECTION 10
sever exempt portion -> disclose reasonably separable remainder with reasons.

SECTION 11
third-party consultation procedure, not an independent exemption.

SECTION 24
listed intelligence/security organisations excluded,
except corruption allegations and human-rights information.
Human-rights disclosure requires Commission approval and uses a 45-day period.

PRIVACY CONTROL
current statute -> harm and public-interest analysis -> redaction -> reasoned order -> appeal.""",
        ),
        (
            "Seven controlling decisions and the no-record-creation boundary",
            "rti-case-law-map",
            [21],
            """State of U.P. v. Raj Narain (1975)
democratic right to know public acts.

S.P. Gupta v. Union of India (1981)
open government and disclosure as democratic norm.

CBSE v. Aditya Bandopadhyay (2011)
evaluated answer books are information; authority need not create new information.

Chief Information Commissioner v. State of Manipur (2011)
complaint is not an automatic substitute for disclosure appeal.

RBI v. Jayantilal N. Mistry (2015)
no generic fiduciary shield for the regulator's inspection information.

Subhash Chandra Agarwal (2019)
CJI office is a public authority; privacy and transparency require balancing.

Anjali Bhardwaj v. Union of India (2019)
appointments must be timely and transparent; stale vacancy counts must be reverified.""",
        ),
        (
            "Institutional comparison, backlog, digital RTI and reform architecture",
            "information-commission-governance-reform",
            [22, 23, 24],
            """CIC / SIC
statutory RTI complaints and second appeals; disclosure, compliance and personal-penalty powers.

COURT
constitutional/statutory judicial review; not a routine RTI first-instance forum.

PIO / FAA
departmental access decision and internal appeal; neither replaces Commission.

IMPLEMENTATION DEFICITS
vacancies + backlog + weak section 4 disclosure + record disorder
| uneven digital access + low penalty consistency + privacy uncertainty.

REFORM
advance vacancy calendar -> independent staff and budget
-> interoperable e-filing with offline access -> record digitisation
-> section 4 audit -> reasoned penalty practice -> privacy-redaction guidance.

LIMIT
technology accelerates routing only when records, accessibility and adjudicatory capacity exist.""",
        ),
        (
            "Current-law caveats, PYQ route, traps and transparency synthesis",
            "information-commission-answer-synthesis",
            [24],
            """DATED CONTROL: 24 AUGUST 2026
DPDP section 44(3) substituted section 8(1)(j) from 13 November 2025.
Section 8(2) remains; no unverified stay or final constitutional outcome is asserted.

PYQ ROUTE
2020 GS-II -> 2019 amendment and autonomy of Information Commissions.

PRELIMS FIREWALL
statutory != constitutional court | complaint != second appeal
| binding order != no judicial review | PIO penalty != ministry fine
| third-party procedure != exemption | section 24 != absolute exclusion
| RTI record != new explanation.

MAINS SPINE
right-to-know root -> access chain -> independent commission design
-> inquiry and appeal powers -> exemptions and privacy
-> implementation deficit -> transparent appointments, records and reasoned balancing.""",
        ),
    ],
    "polity-37": [
        (
            "Santhanam trajectory and the CVC-CBI-DSPE legal identity map",
            "vigilance-investigation-evolution",
            [1, 2, 3],
            """ROOT QUESTION
How should vigilance supervision, police investigation and final adjudication be separated?

EVOLUTION
1941 Special Police Establishment -> DSPE Act, 1946
-> CBI resolution, 1 April 1963
-> CVC resolution, 1964 after Santhanam Committee
-> Vineet Narain v. Union of India (1997) safeguards -> CVC Act, 2003.

LEGAL IDENTITY
CVC -> statutory commission under CVC Act.
CBI -> executive-created organisation.
DSPE -> statutory police establishment supplying core investigative powers.

LIMIT
common anti-corruption purpose does not merge advice, police power, prosecution and judgment.""",
        ),
        (
            "CVC composition, appointment, tenure, removal and independence safeguards",
            "cvc-office-lifecycle",
            [4, 5],
            """COMPOSITION
Central Vigilance Commissioner as Chairperson
+ not more than two Vigilance Commissioners.

APPOINTMENT
President by warrant after committee recommendation:
Prime Minister + Union Home Minister + Lok Sabha Opposition Leader/substitute.

QUALIFICATION
experience in vigilance, policy, administration, police administration,
finance including insurance and banking, law or investigations.

TERM
four years or age 65, whichever earlier; statutory post-tenure restrictions apply.

REMOVAL
proved misbehaviour or incapacity -> President after Supreme Court inquiry.
Direct statutory grounds cover insolvency, moral-turpitude conviction,
outside paid employment, infirmity and prejudicial interest.

LIMIT
secure removal does not convert advice into binding adjudication.""",
        ),
        (
            "Section 8 functions, CVO system, vigilance advice and sanction monitoring",
            "cvc-vigilance-administration-system",
            [6, 7],
            """CVC FUNCTIONS
superintend DSPE investigation of specified Prevention of Corruption Act matters
| issue directions without dictating disposal of a particular case
| review investigation progress and prosecution-sanction applications
| inquire or cause inquiry into covered public-servant complaints
| advise Central Government and covered organisations
| exercise vigilance-administration superintendence.

CVO CHAIN
prevention -> surveillance and complaint scrutiny -> departmental inquiry
-> CVC advice where applicable -> disciplinary authority reasoned decision.

PROSECUTION SANCTION
section 19 PC Act concerns prosecution stage;
section 17A prior approval concerns specified inquiry/investigation decisions.

LIMIT
CVC is not a police station, trial court or universal controller of every CBI case.""",
        ),
        (
            "CBI organisation, DSPE powers, notified offences and mandate boundaries",
            "cbi-dspe-jurisdiction-map",
            [8, 9],
            """CBI ORGANISATION
investigation and anti-corruption | economic offences | special crimes
| policy, administration, forensics and international cooperation.

DSPE ACT
section 2 -> Union Territory police-establishment baseline.
section 3 -> Central notification specifies offence classes.
section 5 -> Central extension of powers to State areas.
section 6 -> State consent for ordinary exercise in State area.

POLICE POWER
FIR or regular case -> search, seizure, arrest and examination under law
-> evidence assessment -> closure report or charge sheet -> court.

BOUNDARY
organisational mandate does not override notified offences, territory,
criminal procedure, special statutes, consent or court directions.""",
        ),
        (
            "Superintendence split and the CBI Director appointment-tenure architecture",
            "cbi-director-independence-system",
            [9, 10, 14, 15],
            """SUPERINTENDENCE
CVC for DSPE investigation of specified corruption offences.
Central Government for other DSPE matters.

ADMINISTRATION
Director controls day-to-day administration and investigative judgment,
subject to statute, law and lawful oversight.

DIRECTOR APPOINTMENT
Central Government appoints on committee recommendation:
Prime Minister + Lok Sabha Opposition Leader/substitute + CJI or nominee.

TENURE
minimum two years under DSPE Act.
Current law permits conditional one-year extensions,
with recorded public-interest reasons, up to aggregate five years.

TRANSFER
statutory committee safeguard applies.

TRAP
two-year floor != automatic five-year term and superintendence != case-outcome command.""",
        ),
        (
            "State consent, pending investigations and constitutional-court directions",
            "cbi-federal-consent-case-map",
            [11, 12, 13],
            """ORDINARY STATE-AREA ROUTE
section 5 extension + section 6 general or case-specific State consent.
Withdrawal of general consent operates prospectively for new ordinary entries.

Kazi Lhendup Dorji v. CBI (1994)
later withdrawal did not terminate investigations validly begun while consent operated.

State of West Bengal v. Committee for Protection of Democratic Rights (2010)
High Court under Article 226 and Supreme Court under Article 32
may direct CBI investigation without State consent, exceptionally and cautiously.

Fertico Marketing and Investment Pvt. Ltd. v. CBI (2020)
fact-specific consent result; no universal rule that later consent always cures defect.

State of West Bengal v. Union of India (2024)
preliminary maintainability objection rejected; cited judgment did not decide consent merits.

FEDERAL VERDICT
qualified State control in ordinary cases + exceptional rights-protecting judicial review.""",
        ),
        (
            "Lokpal interface, investigation lifecycle and procedural safeguards",
            "anti-corruption-case-lifecycle",
            [17, 18],
            """LOKPAL ROUTE
complaint scrutiny -> preliminary inquiry or investigation under Lokpal Act
-> CVC/CBI or statutory wings as assigned -> reports and directions within the Act.

INVESTIGATION LIFECYCLE
source information/complaint -> jurisdiction and approval screen
-> preliminary verification where law permits -> FIR/regular case
-> evidence collection -> sanction question -> final police report
-> prosecution -> trial -> judgment.

CBI v. Thommandru Hannah Vijayalakshmi (2021)
preliminary inquiry is not mandatory before every corruption FIR;
criminal-procedure and corruption-law requirements control.

SAFEGUARDS
lawful approval | reasons | search and arrest standards
| disclosure and fair trial | judicial review | presumption of innocence.

LIMIT
FIR, charge sheet, vigilance advice and sanction are not findings of guilt.""",
        ),
        (
            "CVC, CBI, Lokpal, NIA and State Police: power-type comparison",
            "anti-corruption-institution-comparison",
            [17, 19],
            """CVC
statutory vigilance supervision and advice | no general police power.

CBI / DSPE
executive organisation + statutory police powers | consent and offence controls.

LOKPAL
statutory ombudsman and complaint-routing authority for covered public functionaries.

NIA
statutory national-security investigation under NIA Act and scheduled-offence framework.

STATE POLICE / ACB
State police power and territorial responsibility under ordinary criminal law.

DEPARTMENTAL CVO
internal prevention, scrutiny and disciplinary-vigilance coordination.

COURT
authorises, reviews, tries and finally determines guilt.

TRAP
administrative placement, vigilance supervision and police command are different relationships.""",
        ),
        (
            "Controlling cases, caged-parrot criticism, reform and answer synthesis",
            "cvc-cbi-answer-synthesis",
            [14, 15, 16, 20, 21, 22, 23],
            """Vineet Narain v. Union of India (1997)
institutional safeguards, Director tenure and statutory CVC trajectory.

Alok Kumar Verma v. Union of India (2019)
statutory committee safeguard constrained removal of Director's functions.

Dr Jaya Thakur v. Union of India (2023)
current extension framework upheld; extension remains conditional, not automatic.

"CAGED PARROT"
judicial criticism of perceived executive influence in 2013;
not a statutory status, doctrine or licence for judicial administration of every case.

REFORM
dedicated law with federal safeguards + predictable consent protocol
-> professional cadre and budget -> transparent case allocation
-> timely sanctions -> parliamentary system review + judicial accountability.

PYQ SPINE
2021 State consent and federalism | 2026 controlled institutional matching.

VERDICT
operational autonomy must be paired with legality, federal restraint and answerable coercive power.""",
        ),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def normalize_question_headings(block: str) -> str:
    block = re.sub(r"(?m)^###\s+Q(\d+)\.", r"### OM\1.", block)
    block = re.sub(r"(?m)^###\s+R(\d+)\.", r"### RM\1.", block)
    block = re.sub(r"(?m)^###\s+MCQ\s+(\d+)\s*$", r"### OM\1.", block)
    block = re.sub(
        r"(?m)^###\s+Remedial MCQ\s+(\d+)\s*$",
        r"### RM\1.",
        block,
    )
    return block


def normalize_mains_headings(block: str) -> str:
    block = re.sub(
        r"(?m)^##\s+Original Solved Mains\s+(\d+)\s+-",
        r"## M\1. ",
        block,
    )
    block = re.sub(
        r"(?m)^##\s+Original Mains\s+(\d+)\s+-",
        r"## M\1. ",
        block,
    )
    block = re.sub(
        r"(?m)^###\s+Solved Mains\s+(\d+)\s+[—-]",
        r"### M\1. ",
        block,
    )
    return block


def transform_source(config: dict[str, Any]) -> Path:
    canonical = ROOT / Path(config["canonical"].replace("\\", "/"))
    text = common._normalize_control_date(
        canonical.read_text(encoding="utf-8").replace("\r\n", "\n")
    )
    text = text.replace("19 August 2026", "24 August 2026")
    text = text.replace("19 AUGUST 2026", "24 AUGUST 2026")
    text = re.sub(
        r"(?m)^##\s+(\d)\.\s+",
        lambda match: f"## 0{match.group(1)}. ",
        text,
    )
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
    status_line = (
        "- [CURRENT] Status is controlled to "
        "**24 August 2026, Asia/Kolkata**."
    )
    if status_line not in text:
        first_h2 = re.search(r"(?m)^##\s+", text)
        if not first_h2:
            raise RuntimeError(f"{config['key']}: no package heading found.")
        text = text[: first_h2.start()] + status_line + "\n\n" + text[first_h2.start() :]
    status = re.search(
        r"(?m)^- \[CURRENT\] Status is controlled to "
        r"\*\*24 August 2026, Asia/Kolkata\*\*\.\s*$",
        text,
    )
    if not status:
        raise RuntimeError(f"{config['key']}: current-control line missing.")
    anchor = (
        f"- [CURRENT] **Live official refresh, 24 August 2026:** "
        f"{config['current_note']}"
    )
    text = text[: status.end()] + "\n" + anchor + text[status.end() :]

    headings = base.heading_offsets(text)
    part_i = base.start_for(headings, [r"^PART I\b", r"^0?1\."])
    practice = base.start_for(
        [(offset, title) for offset, title in headings if offset > part_i],
        [
            r"PYQ, practice and solved workbook",
            r"^PART II\b",
            r"^Verified routed",
        ],
    )
    final = base.start_for(
        headings,
        [r"^Final consolidated register notes(?:\b|$)"],
    )

    text = base.add_topic_visuals(config, text)
    text = base.add_session_orientations(text)
    headings = base.heading_offsets(text)
    part_i = base.start_for(headings, [r"^PART I\b", r"^0?1\."])
    practice = base.start_for(
        [(offset, title) for offset, title in headings if offset > part_i],
        [
            r"PYQ, practice and solved workbook",
            r"^PART II\b",
            r"^Verified routed",
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
        r"PYQ, practice and solved workbook|^PART II\b",
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
    mcq_start = base.start_for(
        practice_headings,
        [
            r"^Original hard MCQ",
            r"^Original MCQ",
            r"^D\. Original MCQ",
        ],
    )
    mains_start = base.start_for(
        practice_headings,
        [
            r"^Original Mains practice",
            r"^Original solved Mains practice",
            r"^F\. Original Solved Mains",
        ],
    )
    pyqs = practice_block[:mcq_start].strip()
    mcqs = normalize_question_headings(
        practice_block[mcq_start:mains_start].strip()
    )
    mains = normalize_mains_headings(practice_block[mains_start:].strip())

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
            common._optional_owner(config),
            "## CONSOLIDATED REGISTER NOTES",
            register,
        ]
    ) + "\n"
    assembled = case_years.normalize_text(config["key"], assembled)
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
    mcqs = len(re.findall(r"(?m)^#{3,5}\s+(?:OM|RM)\d+\.", workbook))
    pyqs = len(
        re.findall(
            r"(?m)^#{3,5}\s+(?:"
            r"PYQ|Verified|Supporting|Cross-linked|B\. Verified|C\. Verified"
            r")\b",
            workbook,
            re.IGNORECASE,
        )
    )
    original_mains = len(
        re.findall(r"(?m)^#{3,5}\s+M\d+\.", workbook)
    )
    expected_pyqs = config["exact_pyqs"] + config["supporting_pyqs"]
    if mcqs < 48 or pyqs < expected_pyqs or original_mains < 8:
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
    return len(re.findall(r"(?m)^#{3,5}\s+M\d+\.", section.group(1)))


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
    record = preserve.latest_record(config)
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
        preserve.iso_mtime(path)
        for path in clean_folder.rglob("*")
        if path.is_file()
    )
    flow_completed = str(
        flow_payload.get("validated_at")
        or preserve.iso_mtime(flow_validation)
    )
    completed["completed_at"] = flow_completed
    completed["gate_times"] = {
        "A_started": audit["started_at"],
        "A_completed": audit["completed_at"],
        "B_completed": preserve.iso_mtime(source_path),
        "C_completed": preserve.iso_mtime(source_path),
        "D_completed": preserve.iso_mtime(ascii_path),
        "E_completed": preserve.iso_mtime(graph_path),
        "F_completed": preserve.iso_mtime(validation_path),
        "G_completed": preserve.iso_mtime(staged_path),
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
    expected_order = [f"polity-{number:02d}" for number in range(33, 38)]
    if [config["key"] for config in TOPICS] != expected_order:
        raise RuntimeError("Sequential topic order was altered.")
    base.PANELS.update(PANELS)

    clean_baseline = preserve.topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={33, 34, 35, 36, 37},
    )
    flow_baseline = preserve.flow_topic_hashes(
        exclude_polity={33, 34, 35, 36, 37}
    )
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        resumed = completed_result(config)
        if resumed is not None:
            result, clean_folder, flow_folder = resumed
            results.append(result)
            locked_new.update(preserve.lock_hashes([clean_folder, flow_folder]))
            continue
        if preserve.compare_hashes(
            locked_new,
            {key: preserve.sha256(ROOT / key) for key in locked_new},
        ):
            raise RuntimeError("Previously generated topic artifacts changed before next gate.")

        gate_times: dict[str, str] = {"A_started": now()}
        live = base.live_checks(config)
        audit = base.write_audit(config, gate_times["A_started"], live)
        common.augment_audit(config, audit)
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
            raise RuntimeError(f"{config['key']}: render validation failed.")
        gate_times["F_completed"] = now()

        record = preserve.latest_record(config)
        gate_times["G_completed"] = now()

        base.export_clean_topic(config)
        clean_folder = base.verify_four_folders(config)
        gate_times["H_completed"] = now()

        flow_validation, flow_row = export_flow(config, 65 + index)
        flow_folder = ROOT / Path(flow_row["destination_folder"].replace("\\", "/"))
        gate_times["I_completed"] = now()

        clean_mismatches = preserve.compare_hashes(
            clean_baseline,
            preserve.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={33, 34, 35, 36, 37},
            ),
        )
        flow_mismatches = preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(
                exclude_polity={33, 34, 35, 36, 37}
            ),
        )
        if clean_mismatches or flow_mismatches:
            raise RuntimeError(
                f"{config['key']}: preservation regression: "
                f"clean={clean_mismatches[:5]} flow={flow_mismatches[:5]}"
            )
        prior_mismatches = preserve.compare_hashes(
            locked_new,
            {key: preserve.sha256(ROOT / key) for key in locked_new},
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
                exclude_polity={33, 34, 35, 36, 37},
            ),
        ),
        "existing_flow_hash_mismatches": preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(
                exclude_polity={33, 34, 35, 36, 37}
            ),
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
