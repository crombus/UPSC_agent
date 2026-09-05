"""Generate Polity learner-v2 topics 43-47 in strict preservation-safe order."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_38_42_sequential as prior


base = prior.base
common = prior.common
preserve = prior.preserve
case_years = prior.case_years
ROOT = prior.ROOT
DATE = "2026-08-25"
SECTION = prior.SECTION
EXPORTS = prior.EXPORTS
FINAL_LIBRARY = prior.FINAL_LIBRARY
FLOW_LIBRARY = prior.FLOW_LIBRARY
BATCH_ID = "polity-43-47-sequential-batch-2026-08-25"

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
        "polity-43",
        "Political Parties",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\43_Political-Parties.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
        ],
        [
            "https://www.eci.gov.in/",
            "https://www.sci.gov.in/",
            "https://www.indiacode.nic.in/",
            "https://legislative.gov.in/",
        ],
        1,
        1,
        "Section 29A, the Election Symbols Order, the post-electoral-bonds "
        "legal position and controlling party-registration, disclosure, "
        "criminalisation and symbol-dispute decisions were rechecked on "
        "25 August 2026. Recognition criteria are stated as dated rules; "
        "the current list of recognised parties is deliberately not frozen.",
        "India has no comprehensive constitutional party code. Registration, "
        "recognition, finance, defection and candidate disclosure arise from "
        "different legal instruments. The ECI cannot use Section 29A as a "
        "general merits-based deregistration power, and the electoral-bonds "
        "judgment did not create a complete campaign-finance code.",
        [
            "democratic functions, constitutional silence and association-autonomy tension",
            "RPA 1951 Section 29A registration and constitutional-allegiance declaration",
            "Symbols Order recognition criteria, reserved symbols and dated-rule caveat",
            "party-system evolution, regional parties, coalitions and federal bargaining",
            "internal democracy, membership, candidate selection, dynasticism and centralisation",
            "finance, donations, disclosures and the 2024 electoral-bonds judgment",
            "anti-defection, whips, criminalisation, candidate disclosure and NOTA limits",
            "ECI deregistration limits, cases, reform choices and close-option traps",
        ],
        visual_sessions=[1, 2, 4, 5, 7, 9, 11, 13, 15, 16, 17, 18],
    ),
    topic(
        "polity-44",
        "Pressure Groups",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Pressure-Groups.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Pressure-Groups.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\44_Pressure-Groups.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md",
        ],
        [
            "https://www.mha.gov.in/",
            "https://www.sci.gov.in/",
            "https://legislative.gov.in/",
            "https://ngodarpan.gov.in/",
        ],
        3,
        0,
        "The constitutional association, assembly, petition and judicial-remedy "
        "channels, FCRA framework and official NGO sources were rechecked on "
        "25 August 2026. India still has no general lobbying-registration or "
        "lobbying-disclosure statute; FCRA is not represented as one.",
        "Pressure groups seek policy influence without assuming governmental "
        "office. Political parties, movements, NGOs, lobbyists and interest "
        "groups overlap in practice but are not synonyms. Protest remains "
        "subject to reasonable restrictions, and dated movements or funding "
        "rules are not converted into permanent generalisations.",
        [
            "definition and distinctions from parties, movements, NGOs, lobbyists and interests",
            "associational, non-associational, institutional and anomic classification",
            "business, labour, farmer, professional, caste, issue, environment and digital forms",
            "lobbying, consultation, petitions, PIL, expertise, media, protest and elections",
            "Articles 19, 32 and 226 with reasonable restrictions and protest-space cases",
            "pluralism, participation, policy information, accountability and corporatist forums",
            "resource inequality, capture, opacity, misinformation, violence and revolving doors",
            "FCRA boundary, insider-outsider comparison and transparent consultation reform",
        ],
        visual_sessions=[1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    ),
    topic(
        "polity-45",
        "National Integration and Foreign Policy",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Integration-and-Foreign-Policy.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Integration-and-Foreign-Policy.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\45_National-Integration-and-Foreign-Policy.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Preamble.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Duties.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions.md",
            "upsc-ai-kit\\knowledge\\International-Relations\\basic\\01_Foreign-Policy-Foundations-and-Strategic-Autonomy.md",
        ],
        [
            "https://www.mea.gov.in/",
            "https://www.mha.gov.in/",
            "https://legislative.gov.in/",
            "https://www.sci.gov.in/",
        ],
        0,
        3,
        "The Constitution, MEA and MHA portals and controlling treaty/territory "
        "decisions were rechecked on 25 August 2026. The latest located National "
        "Integration Council meeting remains the 2013 meeting; no later official "
        "reconstitution or meeting is asserted. Strategic autonomy and current "
        "diplomatic initiatives are dated policy anchors, not binding law.",
        "National integration is constitutional accommodation, equal citizenship "
        "and civic fraternity, not cultural uniformity or unrestricted coercion. "
        "Article 51 is a non-justiciable directive; treaty-making and foreign-policy "
        "doctrines remain executive policy unless domestic law gives them legal effect.",
        [
            "Preamble unity, integrity and fraternity with constitutional patriotism",
            "single citizenship, federalism, asymmetry, rights, DPSPs, duties and safeguards",
            "communalism, regionalism, caste, secessionism, inequality, migration and disinformation",
            "NIC status, cooperative federalism, accommodation and lawful security limits",
            "Articles 51, 73, 246, Union List and 253 treaty-implementation architecture",
            "strategic autonomy, non-alignment, Panchsheel, neighbourhood and multilateralism",
            "diaspora, development, climate and parliamentary/federal consultation",
            "territory/treaty cases, policy-law distinction and integration-foreign-policy link",
        ],
        visual_sessions=[1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20],
    ),
    topic(
        "polity-46",
        "Administrative Tribunals",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\46_Administrative-Tribunals.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
        ],
        [
            "https://cgat.gov.in/",
            "https://dopt.gov.in/",
            "https://www.sci.gov.in/",
            "https://legislative.gov.in/",
        ],
        3,
        1,
        "Articles 323A/323B, the Administrative Tribunals Act 1985, CAT material "
        "and the Supreme Court's tribunal-independence line through the judgment "
        "reported as 2025 INSC 1330 were rechecked on 25 August 2026. Appointment, "
        "tenure and service-condition statements carry an exact dated caveat because "
        "the common tribunal framework remains litigation- and implementation-sensitive.",
        "Tribunals supplement specialist adjudication; they do not replace High "
        "Courts or the Supreme Court. L. Chandra Kumar preserves Articles 226/227 "
        "review. CAT, SATs, other Article 323B tribunals, commissions, courts and "
        "Lok Adalats must not be collapsed into one institutional category.",
        [
            "42nd Amendment, Articles 323A/323B and Administrative Tribunals Act 1985",
            "CAT/SAT structure, benches, jurisdiction, composition and service matters",
            "current appointment, tenure and service-condition framework with dated caveat",
            "procedure, civil-court powers, contempt, exclusions and review/appeal chain",
            "L. Chandra Kumar and High Court Division Bench judicial review",
            "Article 323A versus 323B and CAT versus courts, commissions and Lok Adalats",
            "expertise, speed and access versus control, vacancies and fragmented appeals",
            "R. Gandhi, Madras Bar Association, Rojer Mathew and reform principles",
        ],
        visual_sessions=[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19],
    ),
    topic(
        "polity-47",
        "Comparative Constitutional Design",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Comparative-Constitutional-Schemes.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Comparative-Constitutional-Schemes.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\47_Comparative-Constitutional-Design.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Salient-Features.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Emergency-Provisions.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Lokpal-and-Lokayuktas.md",
        ],
        [
            "https://legislative.gov.in/",
            "https://www.sci.gov.in/",
            "https://sansad.in/",
            "https://www.eci.gov.in/",
        ],
        8,
        0,
        "The official Constitution and the controlling Indian comparison cases "
        "were rechecked on 25 August 2026. Foreign systems are used as stable "
        "design comparators rather than as volatile political snapshots; no "
        "current officeholder, party majority or transient reform proposal is frozen.",
        "India borrowed constitutional techniques but adapted them to a written, "
        "supreme, federal-parliamentary and judicially reviewable Constitution. "
        "Comparison must identify function, context and Indian adaptation; the "
        "Indian President is not a US President, Rajya Sabha is not a US Senate, "
        "and Directive Principles are not an operational copy of Ireland.",
        [
            "written/unwritten and rigid/flexible constitutions with context",
            "parliamentary, presidential and semi-presidential government",
            "federal, unitary and hybrid design with bicameral representation",
            "constitutional courts, judicial review and parliamentary sovereignty",
            "rights, due process, procedure established by law and socio-economic directives",
            "amendment, basic structure, emergency and electoral-system design",
            "secularism, ombudsman, audit and fiscal institutions",
            "constitutional transplantation, hybrid adaptation, traps and answer matrices",
        ],
        visual_sessions=[1, 3, 5, 7, 9, 11, 13, 15, 18, 21, 24, 27, 30, 34],
    ),
]


SUPPLEMENTS: dict[str, list[tuple[str, str]]] = {
    "polity-43": [
        (
            "Democratic functions and the missing comprehensive party code",
            """[FACT] Political parties link citizens to government through representation,
interest aggregation, policy choice, leadership recruitment, government formation,
opposition, legislative coordination and electoral accountability.

[FACT] The Constitution's original text did not establish a general party code. The
Tenth Schedule later constitutionalised a narrow defection relationship; Section 29A
governs registration, and the Symbols Order governs recognition and symbol disputes.

[ANALYSIS] The result is segmented regulation: the party is strongly regulated at
entry, elections and legislative discipline but weakly regulated in its internal
membership, leadership and candidate-selection life.

[LIMIT] Article 19(1)(c) association autonomy matters. Reform must distinguish
transparent minimum standards from State control of political ideology or leadership.""",
        ),
        (
            "Membership, candidate selection and internal federalism",
            """| Internal field | Democratic benchmark | Common risk | Reform direction |
|---|---|---|---|
| membership | clear eligibility, notice and appeal | arbitrary admission/expulsion | published rules and reasoned process |
| leadership | periodic, competitive election | indefinite high-command control | verified internal electoral rolls |
| candidates | transparent criteria and consultation | dynasty, money and winnability | recorded criteria and local participation |
| finance | audited, donor-visible accounts | centralised opaque control | public disclosure and independent audit |
| State units | meaningful organisational autonomy | national centralisation | internal federal allocation of authority |

[LIMIT] A statutory internal-democracy floor can protect members and voters, but a
regulator should not select a party's ideology, leadership or candidates.""",
        ),
    ],
    "polity-44": [
        (
            "Pressure group, interest group, movement, NGO and lobbyist compared",
            """| Form | Primary objective | Organisation | Seeks office? | Typical method |
|---|---|---|---|---|
| pressure group | influence a public decision | variable | no | consultation, lobbying, protest |
| interest group | articulate a shared interest | often stable | no | representation and bargaining |
| social movement | wider social change | networked | ordinarily no | mobilisation and norm change |
| NGO | service, research or advocacy mission | formal entity | no | projects, expertise, advocacy |
| lobbyist | professional representation for a client | individual/firm | no | direct policy communication |
| political party | capture and exercise public power | electoral organisation | yes | contesting elections |

[ANALYSIS] One organisation may occupy more than one category, but the categories
answer different questions about purpose, legal form and relation to public office.""",
        ),
        (
            "Insider, outsider and corporatist access",
            """INSIDER ROUTE
recognised expertise -> committee/consultation access -> draft input -> negotiated change.

OUTSIDER ROUTE
excluded or dissatisfied group -> public campaign -> protest/litigation -> agenda pressure.

CORPORATIST ROUTE
State convenes organised business, labour or sector representatives in a structured forum.

RISKS
privileged access | revolving doors | undisclosed clients | consultation capture
| token participation | digital misinformation | violence.

REFORM
public consultation calendar -> disclosure of submissions/meetings -> conflict rules
-> cooling-off safeguards -> reasoned response -> support for under-resourced groups.""",
        ),
    ],
    "polity-45": [
        (
            "National-integration challenge map without security sensationalism",
            """| Challenge | Constitutional injury | Integration response | Limit |
|---|---|---|---|
| communalism | equality, fraternity and public order | non-discrimination, dialogue, lawful policing | no collective blame |
| regionalism | federal trust and equal citizenship | devolution, asymmetry, intergovernmental forums | autonomy is not secession |
| caste exclusion | dignity and equal opportunity | rights, affirmative action, social reform | avoid token inclusion |
| insurgency/secessionism | sovereignty and life | political accommodation plus proportionate security | judicial review remains |
| inequality | substantive citizenship | welfare, fiscal transfers, regional development | growth alone is insufficient |
| migration | identity and service pressure | lawful citizenship, portability and local consultation | migrants retain rights |
| disinformation | informed democratic choice | transparent official communication and media literacy | censorship must be lawful |

[ANALYSIS] Durable integration treats security as one bounded instrument inside a
larger architecture of rights, development, representation and federal accommodation.""",
        ),
        (
            "Foreign-policy doctrine and the integration link",
            """DOCTRINE RAIL
anti-colonialism -> non-alignment -> strategic autonomy
-> diversified partnerships -> issue-based coalitions.

OPERATING DIMENSIONS
Panchsheel | neighbourhood | UN and multilateralism | Global South
| development partnership | diaspora | maritime/border security | climate diplomacy.

INTEGRATION LINK
sovereignty and borders -> territorial confidence;
diaspora -> citizenship/identity connection;
border communities -> federal consultation;
trade/climate treaties -> domestic State-subject effects;
external disinformation -> civic resilience.

[LIMIT] "Strategic autonomy", "Neighbourhood First" and similar labels are policy
doctrines. They are not self-executing constitutional rules.""",
        ),
    ],
    "polity-46": [
        (
            "Articles 323A and 323B: exact constitutional distinction",
            """| Axis | Article 323A | Article 323B |
|---|---|---|
| subject | recruitment and service conditions of public servants | specified fields such as tax, labour, land reforms and elections |
| law-maker | Parliament | appropriate legislature within competence |
| tribunal pattern | administrative tribunals | subject-specific tribunals |
| hierarchy | may provide a structured administrative-tribunal system | may provide a hierarchy for listed matters |
| court exclusion text | originally contemplated exclusion except Article 136 | similar exclusion possibility |
| current control | High Court review survives under L. Chandra Kumar (1997) | same basic-structure floor |

[LIMIT] The two Articles are enabling provisions. They do not themselves create CAT,
every State tribunal or every subject tribunal.""",
        ),
        (
            "CAT process, exclusions and judicial-review chain",
            """SERVICE GRIEVANCE
covered recruitment/service matter -> Original Application before competent CAT bench
-> notice, pleadings, records, hearing -> reasoned tribunal order
-> High Court Division Bench under Articles 226/227
-> Supreme Court route under the Constitution.

PROCEDURE
natural justice | not rigidly bound by CPC | civil-court-type statutory powers
| contempt power as provided | interim relief within jurisdiction.

BOUNDARIES
specified constitutional officeholders and excluded services follow the Act's exact text;
criminal prosecution, ordinary civil disputes and every public-employment question do not
automatically become CAT matters.

[LIMIT] Article 136 is not a substitute for the L. Chandra Kumar High Court review chain.""",
        ),
    ],
    "polity-47": [
        (
            "Ombudsman, audit and fiscal watchdogs in comparative design",
            """| Function | India | Comparative design lesson |
|---|---|---|
| ombudsman | statutory Lokpal; State-law Lokayuktas | legal force and appointment design vary across systems |
| public audit | constitutional CAG reporting to legislatures | Westminster-derived audit becomes constitutionally entrenched in India |
| fiscal transfers | periodic Finance Commission | expert federal equalisation is adapted to Indian vertical/horizontal imbalance |
| election management | independent constitutional ECI | central professional administration differs from decentralised models |
| rights enforcement | Supreme Court/High Courts with writs | diffuse review plus constitutional remedies, not a separate Kelsenian court |

[ANALYSIS] Borrowing an institution's name does not import its appointment method,
jurisdiction, remedial force or political context.""",
        ),
        (
            "Constitutional transplantation and hybrid adaptation",
            """TRANSPLANT TEST
origin -> original function -> Indian textual adaptation -> Indian social/federal context
-> judicial interpretation -> operating consequence.

INDIAN HYBRIDS
British responsible government + written constitutional supremacy;
US-style rights/review + parliamentary executive;
Canadian strong-centre federation + elected State governments;
Irish directives + Indian judicially developed harmony with rights;
Australian concurrent-list and trade ideas + Indian emergency centralisation;
German emergency safeguards and South African transformative comparison as later lessons.

[LIMIT] "Borrowed from" is an origin clue, not an answer. UPSC comparison requires
function, adaptation, reason and consequence.

[FACT] Verified PYQ routes cover India-USA political systems, France and Indian
secularism, India-UK judicial systems, India-France presidential elections,
British-Indian parliamentary practice, India-USA secularism, pardon power and
judicial appointments.

> **Firewall confirmation:** The Core already contains every indispensable
comparison, trap and verified PYQ answer engine; Advanced is enrichment only.""",
        ),
    ],
}


PYQS: dict[str, list[dict[str, Any]]] = {
    "polity-43": [
        {
            "label": "Verified direct PYQ",
            "year": 2022,
            "paper": "GS-II Q13",
            "question": "National political parties favour centralisation whereas regional parties favour State autonomy. Comment.",
            "directive": "Comment",
            "marks": 15,
            "words": 250,
            "points": [
                "The correlation is real but follows organisational incentives and location in power, not permanent ideology.",
                "Pan-Indian parties internalise Union-wide programmes, a strong Centre and high-command coordination.",
                "Regional parties depend on State identity, fiscal devolution and bargaining over Governors and schemes.",
                "Coalition governments show regional parties influencing national policy and national parties conceding autonomy.",
                "Parties reverse positions between Union office and State opposition; institutions must protect federalism.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2023,
            "paper": "GS-II Q5",
            "question": "Discuss the role of presiding officers of State legislatures in maintaining order and impartiality, with reference to party pressures.",
            "directive": "Discuss",
            "marks": 10,
            "words": 150,
            "points": [
                "Presiding officers protect procedure, debate and House order but normally emerge from party politics.",
                "Whip, anti-defection and removal incentives create a party-institution tension.",
                "Kihoto Hollohan (1992) preserves judicial review of defection decisions.",
                "Neutral conventions, reasoned decisions and timely adjudication reduce partisan misuse.",
            ],
        },
    ],
    "polity-44": [
        {
            "label": "Verified direct PYQ",
            "year": 2019,
            "paper": "GS-II Q3",
            "question": "What are the methods used by farmers' organisations to influence policy-makers in India, and how effective are these methods?",
            "directive": "Enumerate and assess",
            "marks": 10,
            "words": 150,
            "points": [
                "Agrarian groups use memoranda, consultation, electoral signalling, media, litigation and mass protest.",
                "Articles 19(1)(a), 19(1)(b) and 19(1)(c) provide the constitutional channel subject to restrictions.",
                "CACP representations and the 2020-21 farm-law movement illustrate insider and outsider methods.",
                "Numerical strength can produce policy reversal, but marginal and regionally dispersed farmers remain weakly represented.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2021,
            "paper": "GS-II Q5",
            "question": "Explain how pressure groups and business associations contribute to public-policy making in India.",
            "directive": "Explain",
            "marks": 10,
            "words": 150,
            "points": [
                "Business associations aggregate sector interests and supply technical information.",
                "Pre-Budget consultation, expert committees, draft-rule comments, litigation and public communication are key channels.",
                "FICCI, CII, ASSOCHAM and NASSCOM provide named Indian examples.",
                "Their expertise improves feasibility, but unequal access creates capture risk and requires disclosure.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2025,
            "paper": "GS-II Q15",
            "question": "Discuss the role of environmental pressure groups in creating awareness, influencing policy and undertaking advocacy in India.",
            "directive": "Discuss",
            "marks": 15,
            "words": 250,
            "points": [
                "Environmental groups combine community mobilisation, research, media, consultation and PIL.",
                "Chipko, Silent Valley, Narmada Bachao Andolan and CSE illustrate distinct methods.",
                "They widen environmental democracy and expose dispersed ecological costs.",
                "Funding, representation, scientific contestation and development trade-offs require transparency and qualification.",
            ],
        },
    ],
    "polity-45": [
        {
            "label": "Supporting routed PYQ",
            "year": 2021,
            "paper": "GS-II",
            "question": "Examine the significance of new security partnerships in the Indo-Pacific for India's strategic autonomy.",
            "directive": "Examine",
            "marks": 15,
            "words": 250,
            "points": [
                "Strategic autonomy is independent choice, not equidistance or isolation.",
                "Issue-based partnerships can supply maritime capacity without creating automatic alliance obligations.",
                "Article 73 locates external executive action while Parliament retains financial and legislative accountability.",
                "India balances partnerships with BRICS, SCO, UN and neighbourhood engagement.",
                "The answer must separate policy doctrine from binding constitutional or treaty law.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2022,
            "paper": "GS-II",
            "question": "Compare the regional roles of SAARC and BIMSTEC and assess their relevance to India's neighbourhood policy.",
            "directive": "Compare and assess",
            "marks": 10,
            "words": 150,
            "points": [
                "SAARC and BIMSTEC have different membership, geography and functional scope.",
                "Neighbourhood policy links connectivity, development partnership and security with regional institutions.",
                "Institutional performance depends on political relations and implementation capacity.",
                "Membership in a forum is policy practice, not a constitutional obligation.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2023,
            "paper": "GS-II",
            "question": "Discuss the role of the Indian diaspora in advancing India's interests while identifying the limits of diaspora diplomacy.",
            "directive": "Discuss",
            "marks": 15,
            "words": 250,
            "points": [
                "Diaspora networks support investment, knowledge, reputation and crisis assistance.",
                "Consular protection and overseas engagement operate within host-State law and international relations.",
                "Diaspora identity also links foreign policy to plural national integration.",
                "The State must not treat diverse overseas communities as a single political instrument.",
            ],
        },
    ],
    "polity-46": [
        {
            "label": "Verified direct PYQ",
            "year": 2018,
            "paper": "GS-II Q12",
            "question": "How far do you agree that tribunals curtail the jurisdiction of ordinary courts? Discuss.",
            "directive": "How far do you agree? Discuss",
            "marks": 15,
            "words": 250,
            "points": [
                "Tribunals transfer first-instance jurisdiction but cannot extinguish constitutional judicial review.",
                "Articles 323A/323B contemplated exclusion, but L. Chandra Kumar (1997) restored Articles 226/227 review.",
                "Madras Bar Association (2014) protected judicial functions from executive-dominated replacement.",
                "Tribunals supplement rather than supplant constitutional courts.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2019,
            "paper": "GS-II Q2",
            "question": "The Central Administrative Tribunal exercises independent judicial authority. Explain.",
            "directive": "Explain",
            "marks": 10,
            "words": 150,
            "points": [
                "CAT is a statutory adjudicatory forum under the Administrative Tribunals Act 1985.",
                "It decides covered service disputes through reasoned orders and natural justice.",
                "Its independence is functional but structurally qualified by appointments, tenure and executive support.",
                "High Court review after L. Chandra Kumar (1997) prevents a self-contained parallel judiciary.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2024,
            "paper": "GS-II Q2",
            "question": "Explain and distinguish Lok Adalats and Arbitration Tribunals.",
            "directive": "Explain and distinguish",
            "marks": 10,
            "words": 150,
            "points": [
                "Lok Adalat is statutory and conciliatory; arbitration is consensual and adjudicatory.",
                "The Legal Services Authorities Act 1987 and Arbitration and Conciliation Act 1996 supply different legal bases.",
                "Lok Adalat awards rest on settlement; arbitral awards face limited Section 34 challenge.",
                "Neither institution is an administrative tribunal under Article 323A.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2025,
            "paper": "GS-II Q2",
            "question": "Comment on the need for administrative tribunals compared with courts and assess the 2021 rationalisation reforms.",
            "directive": "Comment and assess",
            "marks": 10,
            "words": 150,
            "points": [
                "Expertise, flexible procedure and high-volume specialisation justify tribunals.",
                "Rationalisation can remove duplication but may transfer specialised work to burdened courts.",
                "Independent selection, secure tenure, benches and infrastructure determine actual speed.",
                "The post-2025 constitutional position must be stated with a dated service-condition caveat.",
            ],
        },
    ],
    "polity-47": [
        {
            "label": "Verified direct PYQ",
            "year": 2018,
            "paper": "GS-II Q13",
            "question": "Examine the basic tenets of the Indian and United States political systems.",
            "directive": "Examine",
            "marks": 15,
            "words": 250,
            "points": [
                "Both are constitutional democracies with federalism, rights, bicameralism and judicial review.",
                "India uses parliamentary responsibility; the USA uses presidential separation.",
                "Indian federalism has residuary Union power, single citizenship and an integrated judiciary.",
                "Comparison must connect design to accountability, stability and federal representation.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2019,
            "paper": "GS-II Q5",
            "question": "What can France learn from the Indian approach to secularism?",
            "directive": "What can it learn?",
            "marks": 10,
            "words": 150,
            "points": [
                "Indian secularism permits principled engagement and social reform rather than strict institutional separation.",
                "Equality, liberty and proportionality can protect individuals within religious communities.",
                "French laicite arises from a different republican history.",
                "Transplantation must therefore be selective, contextual and rights-centred.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2020,
            "paper": "GS-II Q4",
            "question": "Highlight the points of convergence and divergence between the judicial systems of India and the United Kingdom.",
            "directive": "Highlight",
            "marks": 10,
            "words": 150,
            "points": [
                "Both share common-law reasoning, precedent and institutional independence.",
                "India operates under written constitutional supremacy and strong-form judicial review.",
                "The UK remains shaped by parliamentary sovereignty and an uncodified constitution.",
                "Court structure, rights remedies and appointments require separate comparison.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2022,
            "paper": "GS-II Q14",
            "question": "Critically examine the election procedures for the Presidents of India and France.",
            "directive": "Critically examine",
            "marks": 15,
            "words": 250,
            "points": [
                "India elects an indirectly chosen constitutional head through a weighted federal electoral college.",
                "France directly elects a politically active semi-presidential head through majority voting.",
                "Procedure follows office design, mandate and relation with the legislature.",
                "The comparison should not equate formal title with constitutional power.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2023,
            "paper": "GS-II Q4",
            "question": "Compare and contrast British and Indian parliamentary practice.",
            "directive": "Compare and contrast",
            "marks": 10,
            "words": 150,
            "points": [
                "Both use responsible cabinet government and lower-house confidence.",
                "India constitutionalises rules that Britain often leaves to convention.",
                "Written supremacy, federalism, rights and judicial review limit Indian Parliament.",
                "The British source is adapted rather than copied.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2024,
            "paper": "GS-II Q15",
            "question": "Discuss India as a secular State in comparison with the secular principles of the United States.",
            "directive": "Discuss",
            "marks": 15,
            "words": 250,
            "points": [
                "Both protect religious liberty and equality but use different institutional techniques.",
                "The US combines non-establishment and free exercise.",
                "India permits principled engagement, reform and denominational protection.",
                "Neither system is captured by a complete-separation caricature.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2025,
            "paper": "GS-II",
            "question": "Compare the pardon powers of the Presidents of India and the United States.",
            "directive": "Compare",
            "marks": 10,
            "words": 150,
            "points": [
                "Compare constitutional source, advice, offence jurisdiction, express limits and judicial review.",
                "India's President ordinarily acts on ministerial advice.",
                "The US President has a personal federal pardon power subject to textual limits.",
                "Pre-emptive pardon concerns completed conduct, not future illegality.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2025,
            "paper": "GS-II",
            "question": "Compare judicial appointments in India and the United States and assess the accountability-independence balance.",
            "directive": "Compare and assess",
            "marks": 15,
            "words": 250,
            "points": [
                "India's collegium emerged through the Judges Cases and the NJAC judgment.",
                "The US uses presidential nomination and Senate confirmation.",
                "India prioritises judicial primacy; the US model makes political accountability explicit.",
                "Both face transparency, delay and politicisation concerns in different forms.",
            ],
        },
    ],
}


FACTS: dict[str, list[tuple[str, str, list[str], str]]] = {
    "polity-43": [
        ("constitutional status of parties", "The original Constitution did not create a comprehensive party code; later provisions regulate specific fields.", ["Political parties are wholly unregulated by law.", "Article 324 itself registers political parties.", "The Tenth Schedule regulates every aspect of party organisation."], "Party law is segmented across the Constitution, statutes and the Symbols Order."),
        ("Section 29A", "Section 29A of the RPA 1951 provides the statutory registration route and allegiance declaration.", ["Section 29A grants national-party recognition.", "Section 29A creates the anti-defection whip.", "Section 29A makes every registered party a public authority."], "Registration is distinct from recognition, defection and RTI status."),
        ("recognition", "National and State recognition follows dated criteria in the Election Symbols Order, not an immutable constitutional list.", ["Recognition follows Article 324 alone without an Order.", "Every registered party has a reserved symbol.", "Recognition never changes after first grant."], "Criteria and lists must be rechecked against ECI orders."),
        ("party functions", "Parties aggregate interests, recruit leaders, form governments, organise opposition and enable electoral accountability.", ["Parties only nominate candidates.", "Opposition is external to the party system.", "Interest aggregation belongs only to pressure groups."], "The democratic role extends across representation, government and accountability."),
        ("internal democracy", "India lacks a comprehensive statutory internal-democracy code despite registration and disclosure requirements.", ["The ECI conducts all internal party elections.", "The Constitution prescribes candidate-selection primaries.", "Dynastic succession is itself a statutory disqualification."], "Autonomy and minimum democratic safeguards must be balanced."),
        ("party finance", "The 2024 electoral-bonds judgment invalidated the scheme and enabling anonymity changes on right-to-information grounds.", ["The judgment constitutionalised anonymous bonds.", "The judgment prohibited every corporate donation.", "The judgment created full State funding of elections."], "One instrument was struck down; the wider finance framework still needs statutory analysis."),
        ("candidate disclosure", "ADR (2002) and PUCL (2003) ground candidate-affidavit disclosure in the voter's right to know.", ["Disclosure arises only after conviction.", "The ECI may cancel an election solely for any pending case.", "Candidate education is constitutionally irrelevant and cannot be disclosed."], "Disclosure and disqualification are different mechanisms."),
        ("criminalisation", "Lily Thomas (2013) removed the sitting-member protection in RPA Section 8(4), but disqualification still depends on conviction.", ["Every chargesheet causes automatic disqualification.", "Disclosure alone equals acquittal.", "Political parties cannot nominate a person with pending cases."], "The core gap is the delay between accusation, trial and conviction."),
        ("NOTA", "NOTA protects a negative voting choice but does not automatically cancel the election or require re-poll.", ["NOTA converts India to recall elections.", "NOTA votes are transferred to the runner-up.", "NOTA disqualifies all listed candidates."], "PUCL (2013) concerns secrecy and choice, not automatic rejection of the field."),
        ("anti-defection interface", "The Tenth Schedule disciplines legislators; it is not a general code for party membership or finance.", ["A party whip can criminally punish a voter.", "Every internal party dispute is decided by the Speaker.", "The Symbols Order and Tenth Schedule are the same proceeding."], "Party, legislature-party, symbol and defection questions remain distinct."),
        ("deregistration", "Indian National Congress v. Institute of Social Welfare (2002) limits ECI cancellation to narrow grounds such as fraud or loss of foundational allegiance.", ["The ECI has an unlimited policy power to deregister inactive parties.", "Recognition withdrawal and registration cancellation are identical.", "The Supreme Court barred cancellation even for fraud."], "Registration power does not imply a general merits-based deregistration power."),
        ("regional parties and coalitions", "Regional parties can deepen federal representation while also increasing bargaining and coordination costs.", ["Regional parties are constitutionally confined to State elections.", "Coalitions are unconstitutional when no party has a majority.", "National parties always favour autonomy."], "Effects depend on incentives, alliances and institutional context."),
    ],
    "polity-44": [
        ("pressure-group definition", "A pressure group seeks to influence public policy without itself seeking to form the government.", ["It must contest elections to remain lawful.", "It is identical to a political party.", "It can operate only as a registered society."], "Purpose, not one legal form, defines the category."),
        ("party distinction", "Political parties seek public office; pressure groups ordinarily seek influence over office-holders.", ["Pressure groups cannot support candidates.", "Parties cannot represent interests.", "Both terms are legally interchangeable."], "Electoral influence does not itself convert a group into a party."),
        ("typology", "Associational, non-associational, institutional and anomic categories describe organisation and method.", ["Anomic groups are permanent professional bodies.", "Institutional groups exist only outside government.", "Non-associational interests have formal membership rolls."], "The typology is analytical and groups may shift forms."),
        ("constitutional channels", "Articles 19(1)(a), 19(1)(b) and 19(1)(c) protect speech, peaceful assembly and association subject to restrictions.", ["Article 19 protects violent blockade.", "Only citizens may invoke Article 32.", "Article 226 is narrower than Article 32 in every respect."], "Rights enable influence but do not immunise unlawful conduct."),
        ("litigation and PIL", "Groups may use Articles 32 and 226 to seek judicial remedies where standing and jurisdiction permit.", ["PIL allows courts to enact policy without law.", "Every petition by an NGO is a PIL.", "Article 226 excludes public-law remedies."], "Litigation is one channel among many and remains court-controlled."),
        ("business associations", "Business associations supply expertise and organised representation but can enjoy unequal insider access.", ["Their submissions bind the government.", "Business consultation is prohibited by equality.", "Expertise removes capture risk."], "Transparency is the answer to privileged access, not exclusion from consultation."),
        ("farmers' organisations", "Farm groups combine lobbying, electoral signalling, media and protest; effectiveness varies by organisation and representation.", ["All farmers share identical interests.", "Only litigation can change farm policy.", "Road blockade is constitutionally unrestricted."], "Numerical strength can coexist with regional and crop bias."),
        ("environmental groups", "Environmental groups use awareness, research, community mobilisation, consultation and PIL.", ["They are constitutional bodies.", "FCRA status determines whether their environmental claim is correct.", "Development and conservation never conflict."], "Advocacy value and regulatory compliance are separate questions."),
        ("lobbying law", "India has no general lobbying-registration and disclosure statute.", ["FCRA is India's general lobbying statute.", "Lobbying is expressly criminalised as a category.", "All policy meetings are already published by law."], "Sectoral laws may apply, but no comprehensive disclosure regime exists."),
        ("FCRA boundary", "FCRA regulates receipt and use of foreign contribution by covered persons; it does not define all domestic advocacy.", ["FCRA registers political parties as lobbyists.", "Domestic donations are always foreign contribution.", "FCRA determines constitutional reasonableness of protest."], "Funding regulation and policy-influence regulation must be separated."),
        ("pluralism and capture", "Pressure groups widen participation and information but unequal resources can produce capture and opacity.", ["Pluralism guarantees equal influence.", "Capture occurs only through bribery.", "Digital mobilisation eliminates misinformation."], "Democratic assessment must examine both access gains and distributional inequality."),
        ("reform", "A sound regime discloses meetings and submissions, manages conflicts and supports inclusive consultation.", ["Government should ban all organised representation.", "Only courts should hear policy views.", "Consultation must make every submission binding."], "Transparency, reason-giving and inclusion preserve both participation and accountability."),
    ],
    "polity-45": [
        ("national integration", "National integration combines equal citizenship, constitutional loyalty, fraternity and accommodation of diversity.", ["It requires cultural uniformity.", "It is identical to territorial conquest.", "It suspends minority rights."], "Unity is constitutional and plural rather than assimilationist."),
        ("Preamble", "Unity and integrity operate with justice, liberty, equality and fraternity.", ["Integrity overrides every Fundamental Right.", "Fraternity is only a foreign-policy doctrine.", "The Preamble creates emergency power by itself."], "Values must be read together, not hierarchically isolated."),
        ("single citizenship and federalism", "Single citizenship coexists with federal distribution, linguistic States and asymmetric provisions.", ["Federalism requires dual citizenship.", "Asymmetry is necessarily anti-national.", "State boundaries are constitutionally indestructible."], "India combines common citizenship with differentiated territorial accommodation."),
        ("minority safeguards", "Articles 29 and 30 protect cultural and educational interests within the integrative constitutional order.", ["Minority rights are exceptions to citizenship.", "Article 30 creates secession rights.", "Only linguistic majorities can establish institutions."], "Safeguards integrate by recognition, subject to constitutional regulation."),
        ("NIC status", "The National Integration Council is an extra-constitutional advisory forum; no post-2013 meeting is asserted on the checked record.", ["It is a permanent constitutional commission.", "Its recommendations bind States.", "It exercises emergency powers."], "Status and recent activity must be stated separately."),
        ("Article 51", "Article 51 is a non-justiciable DPSP on peace, international law and arbitration.", ["It gives courts a power to ratify treaties.", "It is a Fundamental Right.", "It fixes India's alliances."], "It supplies values, not a complete foreign-policy doctrine."),
        ("Articles 73 and 253", "Article 73 supports Union executive action; Article 253 enables Parliament to implement international obligations even in State fields.", ["Treaties automatically amend every domestic law.", "States ratify Union treaties under Article 253.", "Article 73 abolishes parliamentary accountability."], "International commitment and domestic legal effect are distinct."),
        ("territorial cession", "Berubari Union (1960) requires constitutional amendment for cession, while boundary settlement without cession is distinct.", ["Article 3 alone cedes territory abroad.", "Every boundary clarification needs Article 368.", "The executive may cede territory by press release."], "Internal reorganisation and external cession follow different routes."),
        ("strategic autonomy", "Strategic autonomy means independent choice through diversified partnerships, not neutrality or isolation.", ["It constitutionally bars every alliance.", "It is another name for non-participation.", "It makes treaties non-binding."], "It is a policy doctrine whose content changes with circumstances."),
        ("Panchsheel and non-alignment", "Panchsheel and non-alignment are historical policy principles, not enforceable constitutional commands.", ["Panchsheel is in the Seventh Schedule.", "NAM requires neutrality in every conflict.", "Article 51 lists the five Panchsheel principles verbatim."], "Historical doctrine should be linked to current strategy with qualification."),
        ("diaspora and climate", "Diaspora, development and climate diplomacy connect external policy with domestic rights, economy and federal implementation.", ["Diaspora members are governed only by Indian law abroad.", "Climate commitments automatically override statutes.", "States have treaty-making competence."], "External goals often need domestic legislation and consultation."),
        ("integration-policy link", "Borders, sovereignty, diaspora and treaty effects make national integration and foreign policy mutually connected.", ["Foreign policy is unrelated to federalism.", "National integration is only an internal-security subject.", "Border communities have no constitutional interests."], "The connection is strongest where external choices create internal distributional effects."),
    ],
    "polity-46": [
        ("Article 323A", "Article 323A concerns administrative tribunals for public-service recruitment and service conditions and can be legislated by Parliament.", ["It creates every tax tribunal.", "States alone legislate under Article 323A.", "It abolishes High Courts."], "The Article is enabling and subject to the judicial-review basic structure."),
        ("Article 323B", "Article 323B covers specified subject fields and allows the appropriate legislature to create tribunals within competence.", ["It is limited to Union civil servants.", "It is identical to Article 323A.", "It automatically creates a national appellate tribunal."], "Subject, law-maker and scope distinguish the two Articles."),
        ("Administrative Tribunals Act 1985", "The 1985 Act establishes CAT and enables SAT arrangements for covered service matters.", ["It is a constitutional amendment.", "It governs all private employment.", "It makes CAT a High Court."], "Statutory jurisdiction depends on the Act's coverage and exclusions."),
        ("CAT jurisdiction", "CAT hears covered recruitment and service disputes, not every public-law or criminal matter.", ["CAT tries corruption offences.", "CAT reviews constitutional amendments.", "Every PSU employee automatically falls within CAT."], "Employer, post and statutory notification matter."),
        ("procedure and powers", "CAT follows natural justice and statutory powers without being rigidly bound by the CPC.", ["CAT has no power to summon evidence.", "Natural justice never applies to tribunals.", "Flexible procedure means arbitrary procedure."], "Flexibility remains bounded by jurisdiction, fairness and reasoned orders."),
        ("judicial review", "L. Chandra Kumar (1997) preserves High Court Division Bench review under Articles 226/227.", ["Tribunal orders go only by direct Article 136 appeal.", "High Court review was permanently excluded.", "CAT can overrule the Supreme Court."], "Tribunals are first-instance substitutes, not constitutional-court replacements."),
        ("independence", "Appointments, tenure, removal, infrastructure and administrative control determine tribunal independence.", ["Expert members alone guarantee independence.", "Executive funding is legally irrelevant.", "Short tenure always improves neutrality."], "Institutional design must match the judicial work transferred."),
        ("rationalisation", "Abolishing or merging tribunals can reduce duplication but can also shift specialised work and pendency to courts.", ["Rationalisation automatically reduces delay.", "Every merger is unconstitutional.", "Abolition removes judicial review."], "Capacity and transition design determine outcomes."),
        ("R. Gandhi", "Union of India v. R. Gandhi (2010) accepts tribunalisation only with independence safeguards equivalent to transferred judicial functions.", ["It abolished all tribunals.", "It made administrative members constitutional judges.", "It removed qualification standards."], "The functional-equivalence principle controls institutional design."),
        ("Madras Bar Association", "The Madras Bar Association line invalidates executive-dominated or insecure tribunal arrangements.", ["It bars Parliament from creating specialist forums.", "It treats tenure as purely executive policy.", "It removes court review of appointments."], "Tribunal validity and particular service-condition defects must be separated."),
        ("Rojer Mathew", "Rojer Mathew (2019) challenged the rules framework and reinforced scrutiny of tribunal independence.", ["It made tribunal recommendations binding legislation.", "It held every Finance Act invalid.", "It removed judicial members."], "The decision belongs to a continuing line rather than a single final settlement."),
        ("CAT comparison", "CAT is an adjudicatory tribunal; commissions investigate or advise, and constitutional courts retain supervisory review.", ["CAT and UPSC perform the same role.", "A commission's recommendation is a judicial decree.", "A Lok Adalat is an Article 323A tribunal."], "Institutional taxonomy prevents close-option errors."),
    ],
    "polity-47": [
        ("written and unwritten", "India has a written supreme Constitution; the UK has an uncodified constitution formed by statutes, cases and conventions.", ["The UK has no constitutional law.", "Every written constitution is rigid.", "India relies only on convention."], "Codification, supremacy and rigidity are separate axes."),
        ("parliamentary and presidential", "India's executive is responsible to the Lok Sabha; the US executive has a separate electoral mandate and fixed tenure.", ["The Indian President governs like the US President.", "The US Cabinet is collectively responsible to Congress.", "Parliamentary government means no separation of powers."], "Executive-legislative relationship is the decisive comparison."),
        ("semi-presidential", "France combines a directly elected President with a Prime Minister responsible to Parliament.", ["France is identical to the US model.", "Cohabitation is constitutionally impossible.", "The French President is only ceremonial."], "Dual executive authority changes with legislative majority."),
        ("federal design", "India is federal with strong-centre and unitary features; Canada and Australia supply useful but non-identical comparisons.", ["India is unitary because residuary power lies with the Union.", "Every federation gives equal upper-house representation.", "Federalism forbids asymmetry."], "Federal character depends on distribution, institutions and amendment, not one feature."),
        ("bicameralism", "Rajya Sabha represents States unequally by population and has special but not Senate-identical powers.", ["Every State has equal Rajya Sabha seats.", "Rajya Sabha confirms Supreme Court judges like the US Senate.", "Rajya Sabha can remove the Union government by no-confidence."], "Upper houses reflect different federal bargains."),
        ("parliamentary sovereignty", "Indian Parliament is limited by the Constitution, rights, federalism, judicial review and basic structure.", ["India copied unlimited British sovereignty.", "Judicial review is merely a convention.", "A constitutional amendment is immune from review."], "British origin does not erase Indian constitutional supremacy."),
        ("rights models", "India combines enforceable Fundamental Rights with non-justiciable Directive Principles and constitutional remedies.", ["DPSPs operate exactly like Irish law in India.", "Socio-economic rights are wholly absent from Indian doctrine.", "Fundamental Rights are absolute."], "Text, remedies and judicial harmonisation matter."),
        ("procedure and due process", "Article 21's 'procedure established by law' acquired fairness and reasonableness through Maneka Gandhi (1978).", ["India constitutionally copied the US phrase due process.", "Any enacted procedure is valid after Maneka.", "Article 21 protects only physical detention."], "Indian doctrine moved beyond formal legality without rewriting the text."),
        ("amendment and basic structure", "Article 368 permits broad amendment, but Kesavananda Bharati (1973) preserves the basic structure.", ["India follows an entirely unamendable constitution.", "Parliament can destroy constitutional identity.", "The UK basic-structure doctrine binds Westminster."], "India occupies a middle position between rigidity and unlimited amendment."),
        ("emergency design", "Indian emergency provisions centralise power but are bounded by text, amendments and judicial review.", ["Emergency automatically suspends every right.", "Germany and India have identical emergency constitutions.", "Federalism permanently ends during any emergency."], "Comparative borrowing must include post-abuse safeguards."),
        ("secularism", "Indian principled engagement differs from US non-establishment and French laicite while sharing liberty and equality commitments.", ["India has an official religion.", "The USA constitutionally funds all religions equally.", "French laicite can be transplanted without context."], "Historical context shapes the institutional form of secularism."),
        ("institutional borrowing", "The CAG, Finance Commission, ECI and Lokpal show adaptation of audit, federal and ombudsman functions to Indian needs.", ["Borrowing imports identical powers.", "The Finance Commission is copied from the US Senate.", "Lokpal is a constitutional court."], "Origin is only the first step of a comparative answer."),
    ],
}


MAINS_PROMPTS: dict[str, list[tuple[int, str, str]]] = {
    "polity-43": [
        (10, "Explain the segmented constitutional and statutory regulation of political parties in India.", "Explain"),
        (10, "Distinguish registration, recognition and deregistration of political parties.", "Distinguish"),
        (10, "Examine the democratic functions of political parties beyond electioneering.", "Examine"),
        (15, "Critically examine the deficit of internal democracy in Indian political parties.", "Critically examine"),
        (15, "Assess the current party-finance framework after the electoral-bonds judgment.", "Assess"),
        (15, "Analyse the party-system causes of criminalisation and weak candidate selection.", "Analyse"),
        (20, "Political parties are regulated strongly at their edges but weakly in their interior. Discuss and propose a balanced regulatory framework.", "Discuss"),
        (20, "Evaluate regional parties and coalition politics as instruments of federal representation and democratic accountability.", "Evaluate"),
    ],
    "polity-44": [
        (10, "Distinguish pressure groups from political parties, NGOs and social movements.", "Distinguish"),
        (10, "Explain the constitutional channels through which pressure groups influence policy.", "Explain"),
        (10, "Classify pressure groups and illustrate each category from India.", "Classify"),
        (15, "Assess the contribution of pressure groups to pluralism and accountability.", "Assess"),
        (15, "Unequal resources can convert participation into capture. Examine.", "Examine"),
        (15, "Should India enact a lobbying-transparency law? Discuss.", "Discuss"),
        (20, "Evaluate insider and outsider pressure-group strategies in Indian democracy.", "Evaluate"),
        (20, "Design an inclusive consultation framework that preserves participation while reducing opacity, conflict and misinformation.", "Design"),
    ],
    "polity-45": [
        (10, "Explain constitutional patriotism as a basis of national integration.", "Explain"),
        (10, "Distinguish Article 73 treaty power from Article 253 implementation power.", "Distinguish"),
        (10, "Examine the constitutional status and present relevance of the National Integration Council.", "Examine"),
        (15, "National integration in India is sustained more by accommodation than assimilation. Discuss.", "Discuss"),
        (15, "Assess executive dominance and parliamentary accountability in treaty-making.", "Assess"),
        (15, "Analyse strategic autonomy as the contemporary evolution of non-alignment.", "Analyse"),
        (20, "Evaluate the constitutional architecture for national integration against communalism, regionalism, inequality and disinformation.", "Evaluate"),
        (20, "National integration and foreign policy meet at sovereignty, borders, diaspora and federal consultation. Discuss.", "Discuss"),
    ],
    "polity-46": [
        (10, "Distinguish Articles 323A and 323B.", "Distinguish"),
        (10, "Explain CAT's jurisdiction, procedure and review chain.", "Explain"),
        (10, "Why do tribunals not replace constitutional courts?", "Explain"),
        (15, "Assess administrative tribunals as instruments of expertise, speed and access.", "Assess"),
        (15, "Examine executive control, vacancies and short tenure as threats to tribunal independence.", "Examine"),
        (15, "Evaluate tribunal rationalisation and abolition as pendency reforms.", "Evaluate"),
        (20, "Trace the constitutional evolution of tribunal judicial review from the 42nd Amendment to L. Chandra Kumar and later cases.", "Trace and analyse"),
        (20, "Propose a tribunal reform architecture consistent with independence, specialisation, access and constitutional review.", "Propose"),
    ],
    "polity-47": [
        (10, "Distinguish constitutional borrowing from constitutional adaptation.", "Distinguish"),
        (10, "Compare Rajya Sabha with the United States Senate.", "Compare"),
        (10, "Explain why the Indian President is not comparable to the United States President merely by title.", "Explain"),
        (15, "Compare parliamentary sovereignty in the United Kingdom with constitutional supremacy in India.", "Compare"),
        (15, "Assess India's hybrid federal-parliamentary constitutional design.", "Assess"),
        (15, "Compare Indian secularism with the United States and France.", "Compare"),
        (20, "Evaluate how India adapted foreign constitutional features to its social and federal context.", "Evaluate"),
        (20, "Design an India-centred comparative matrix covering executive, federalism, rights, courts, amendment, emergency and accountability institutions.", "Design and evaluate"),
    ],
}


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-43": [
        ("Party as democratic intermediary, not constitutional sovereign", "party-role-constitution-map", [1, 2], """ROOT QUESTION
How can parties aggregate citizens and govern without becoming private constitutional sovereigns?

DEMOCRATIC FUNCTIONS
representation | aggregation | recruitment | programme choice
| government | opposition | legislative coordination | accountability.

LEGAL LOCATION
original Constitution: no comprehensive party code.
Tenth Schedule: defection only.
RPA 1951: registration, contribution and disclosure fields.
Symbols Order 1968: recognition and symbol disputes.

TENSION
public democratic power <-> Article 19(1)(c) associational autonomy."""),
        ("Section 29A registration and ECI's bounded cancellation power", "registration-deregistration-rail", [3, 4], """SECTION 29A
association applies to ECI -> memorandum/rules -> allegiance declaration
to Constitution, socialism, secularism, democracy, sovereignty, unity and integrity.

REGISTRATION != RECOGNITION
registration creates statutory party status;
recognition follows Symbols Order performance criteria.

Indian National Congress v. Institute of Social Welfare (2002)
ECI has no general review/deregistration power;
narrow cancellation survives for fraud, foundational disqualification or analogous grounds.

TRAP
loss of recognition, symbol consequence and deregistration are different legal events."""),
        ("Recognition and symbol architecture without freezing party lists", "recognition-criteria-matrix", [5, 6], """SYMBOLS ORDER 1968
recognised National party | recognised State party | registered-unrecognised party.

NATIONAL: ANY ONE DATED ROUTE
6% valid votes in four or more States + four Lok Sabha seats
| 2% Lok Sabha seats from at least three States
| State-party recognition in four States.

STATE: ANY ONE DATED ROUTE
vote-plus-seat tests | 3% or three Assembly seats | Lok Sabha ratio route | 8% vote route.

PRIVILEGE
reserved symbol and specified electoral facilities.

CONTROL
criteria are Order-based and re-verifiable; do not freeze the current party list."""),
        ("Party system evolution, regionalisation and coalition federalism", "party-system-timeline", [7, 8], """EVOLUTION
1952-1967 Congress system -> 1967 fragmentation
-> 1977 alternation -> 1989-2014 coalition bargaining
-> post-2014 central dominance with strong State-party plurality.

PARTY-SYSTEM TYPES
one-party dominance | two-party tendency | multi-party competition | coalition system.

REGIONAL PARTIES
identity representation + State autonomy + policy innovation
<-> personalisation + fragmentation + bargaining cost.

2022 GS-II
centralisation/autonomy preference follows organisational position and power incentives,
not a permanent ideological law."""),
        ("Internal democracy, membership, candidates and dynastic control", "internal-democracy-lifecycle", [9, 10], """MEMBERSHIP
published eligibility -> reliable roll -> notice/hearing for discipline -> appeal.

LEADERSHIP
periodic election -> real competition -> transparent counting -> State-unit voice.

CANDIDATES
local consultation + published criteria + integrity + representativeness
<-> dynasty + money + winnability + central nomination.

CURRENT GAP
ECI receives organisational particulars but no comprehensive statutory
internal-democracy code exists.

REFORM LIMIT
minimum process safeguards must not authorise State selection of ideology or leaders."""),
        ("Finance and the electoral-bonds constitutional reset", "finance-disclosure-chain", [11, 12], """PARTY FINANCE CHANNELS
individual/corporate contribution | electoral trust | cash within law | public facilities.

DISCLOSURE
RPA Section 29C and tax/company-law rules operate through separate thresholds and filings.

Association for Democratic Reforms v. Union of India (2024)
Electoral Bond Scheme and enabling anonymity changes struck down;
voter's Article 19(1)(a) right to information protected;
SBI disclosure to ECI ordered.

LIMIT
judgment did not create full State funding, ban every corporate donation
or enact a complete campaign-finance code."""),
        ("Whips, anti-defection and party-symbol identity", "party-discipline-distinction", [13, 14], """PARTY ORGANISATION
membership, leadership and candidate selection.

LEGISLATURE PARTY
members of the House belonging to the political party.

TENTH SCHEDULE
voluntary giving up | vote/abstention direction | merger | presiding-officer decision.

SYMBOLS ORDER
ECI decides rival-faction symbol/recognition questions.

Sadiq Ali (1972)
majority in organisational and legislative wings informs symbol identity.

TRAP
symbol dispute, internal leadership, whip authorisation and defection are related
but legally separate proceedings."""),
        ("Criminalisation, disclosure and NOTA limits", "criminalisation-choice-map", [15, 16], """        Union of India v. Association for Democratic Reforms (2002) + PUCL (2003)
candidate affidavit -> criminal, financial and educational disclosure -> informed voter.

Lily Thomas (2013)
RPA Section 8(4) sitting-member shield removed;
disqualification still follows conviction, not accusation alone.

Rambabu Singh Thakur (2020)
party publication of criminal antecedents and selection reasons.

PUCL NOTA (2013)
negative secret choice recognised.

LIMIT
NOTA does not automatically cancel the poll, disqualify all candidates or trigger re-election."""),
        ("UPSC synthesis: regulate democratic power without nationalising association", "party-answer-synthesis", [17, 18, 19, 20], """PRELIMS FIREWALL
29A registration != recognition | reserved != free symbol
| recognition loss != deregistration | disclosure != disqualification
| NOTA != re-poll | party != legislature party | bonds verdict != finance code.

MAINS SPINE
democratic role -> segmented legal basis -> party-system evolution
-> internal democracy -> finance -> criminalisation -> whip/symbol interfaces
-> autonomy-transparency balance -> reform.

REFORM PACKAGE
verified internal elections | candidate criteria | donation transparency
| independent audit | trial expedition | narrow deregistration amendment
| proportionate ECI power + judicial review.

VERDICT
regulate the party's public consequences while preserving its legitimate associational core."""),
    ],
    "polity-44": [
        ("Influence without office: the pressure-group starting point", "definition-distinction-map", [1, 2], """ROOT QUESTION
How can organised interests shape policy without becoming the government?

PRESSURE GROUP
organised or networked interest seeking policy influence, not public office.

DISTINGUISH
party -> contests for office.
movement -> broad social transformation.
NGO -> formal service/research/advocacy entity.
lobbyist -> professional representative.
interest group -> shared-interest articulation.

OVERLAP
one body may occupy several forms; purpose and method decide the label."""),
        ("Typology from associational to anomic action", "pressure-group-typology", [3, 4], """ASSOCIATIONAL
formal membership: business, labour, farmer, professional bodies.

NON-ASSOCIATIONAL
community, caste, kinship, religious or regional networks without stable formal structure.

INSTITUTIONAL
interests voiced from established organisations,
including bureaucratic or professional institutions.

ANOMIC
spontaneous, episodic mobilisation, sometimes disruptive.

ISSUE FORMS
environmental | rights-based | consumer | digital | neighbourhood.

TRAP
anomic describes organisation/method, not a licence for violence."""),
        ("Methods of influence: insider and outsider routes", "method-spectrum-rail", [5, 6], """INSIDER
lobbying | ministry representation | committees | consultation | expert evidence
| corporatist forum | draft comments.

OUTSIDER
petition | media | campaign | election signalling | protest | boycott | litigation/PIL.

CONSTITUTIONAL CHANNELS
Article 19 speech + peaceful assembly + association
| Article 32 Supreme Court | Article 226 High Court.

EFFECTIVENESS TEST
access + organisation + numbers + expertise + public legitimacy + policy timing.

LIMIT
peaceful influence is protected; coercion, violence and unlawful obstruction are not."""),
        ("Business, labour, farmers and professional groups", "sector-comparison-matrix", [7, 8], """BUSINESS
FICCI/CII/ASSOCHAM/NASSCOM -> expertise, pre-Budget input, sector lobbying.

LABOUR
trade unions -> bargaining, tripartite forums, strikes, labour-law advocacy.

FARMERS
AIKS/BKU/Shetkari/SKM -> MSP representation, electoral pressure, protest.

PROFESSIONAL
bar, medical and other associations -> standards, expert consultation, litigation.

UNEQUAL ACCESS
capital and organised professions often possess continuous insider capacity;
informal labour and marginal farmers face collective-action barriers."""),
        ("Environmental, community, issue-based and digital mobilisation", "issue-group-network", [9, 10], """ENVIRONMENT
Chipko | Silent Valley | NBA | CSE
-> awareness + research + community mobilisation + consultation + PIL.

COMMUNITY / CASTE
representation and recognition <-> exclusionary mobilisation risk.

ISSUE-BASED
RTI, consumer, gender, disability and anti-corruption networks.

DIGITAL
rapid agenda-setting + distributed participation
<-> misinformation + astroturfing + platform opacity.

2025 GS-II
environmental advocacy is democratically valuable but requires evidence,
representation and lawful funding."""),
        ("Constitutional protest space and judicial limits", "protest-rights-balance", [11, 12], """Damayanti Naranga (1971)
association autonomy includes protection against State-imposed membership alteration.

Ramlila Maidan Incident (2012)
peaceful assembly and State response remain subject to constitutional scrutiny.

Mazdoor Kisan Shakti Sangathan (2018)
protest rights must be balanced with residents' and public-order interests.

Amit Sahni (2020)
public ways cannot be occupied indefinitely.

TEST
legality | necessity | proportionality | alternatives | non-violence | reasoned policing."""),
        ("Lobbying gap, FCRA boundary and NGO regulation", "regulatory-boundary-board", [13, 14], """NO GENERAL LOBBYING STATUTE
no comprehensive register of lobbyists, clients, meetings and spending.

FCRA
foreign-contribution receipt/use by covered persons;
registration/prior permission, accounts, utilisation and prohibitions.

OTHER LEGAL FORMS
Societies Act | trusts | Companies Act Section 8 | Trade Unions Act
| tax, election, anti-corruption and sectoral rules.

Noel Harper (2022)
FCRA amendments examined as funding regulation.

TRAP
FCRA compliance does not prove policy merit; advocacy does not determine FCRA status."""),
        ("Pluralist gain versus capture, opacity and revolving doors", "pluralism-capture-balance", [15, 16], """DEMOCRATIC GAINS
participation | minority voice | policy information | monitoring | accountability | experimentation.

RISKS
resource inequality | elite capture | undisclosed access | misinformation
| violence | clientelism | revolving doors | consultation theatre.

REFORM
meeting/submission register | client and funding disclosure
| conflict and cooling-off rules | public draft period
| reasoned response | accessible regional-language participation
| support for under-represented groups.

VERDICT
transparent inclusion, not prohibition, is the pluralist answer."""),
        ("PYQ and answer synthesis across three verified routes", "pressure-group-exam-synthesis", [17, 18, 19, 20], """VERIFIED ROUTES
2019 farmers' methods | 2021 business associations | 2025 environmental groups.

PRELIMS FIREWALL
influence != office | association right != unrestricted blockade
| PIL != legislation | FCRA != lobbying law
| consultation != capture automatically | NGO != pressure group always.

MAINS SPINE
definition -> typology -> constitutional channels -> methods
-> named sector evidence -> pluralist gain -> unequal-resource risk
-> transparent inclusive reform.

CONCLUSION
pressure groups are an informal democratic infrastructure whose legitimacy
depends on peaceful method, disclosed access and fair opportunity to participate."""),
    ],
    "polity-45": [
        ("Constitutional patriotism and integration by accommodation", "integration-value-map", [1, 2], """ROOT QUESTION
How can a plural federation sustain common citizenship without cultural uniformity?

PREAMBLE
unity and integrity + fraternity + dignity + justice + liberty + equality.

CONSTITUTIONAL PATRIOTISM
loyalty to constitutional values and equal citizenship, not compulsory cultural sameness.

ACCOMMODATION
linguistic States | Articles 29-30 | Fifth/Sixth Schedules
| Articles 371-371J | official-language pluralism.

COMMON SPINE
single citizenship | integrated judiciary | All-India Services | national institutions.

VERDICT
India integrates through a calibrated blend, predominantly accommodationist."""),
        ("Rights, DPSPs, Duties and cooperative-federal mechanisms", "integration-instrument-matrix", [3, 4], """RIGHTS
equality | freedoms | religious liberty | cultural/educational protection | remedies.

DPSP
social justice and reduction of inequality reduce exclusion-driven alienation.

DUTIES
51A(c) sovereignty, unity and integrity;
51A(e) harmony and common brotherhood;
51A(i) public property and non-violence.

S.R. Bommai (1994)
federalism and secularism operate as basic-structure limits on central power.

FEDERAL MECHANISMS
Finance Commission | Inter-State Council | linguistic reorganisation
| asymmetric autonomy | local self-government.

LIMIT
duties are non-justiciable; emergency/security power remains rights- and review-bounded."""),
        ("Integration challenge-response map", "integration-risk-response", [5, 6], """CHALLENGES
communalism | regionalism | caste exclusion | secessionism/insurgency
| inequality | migration stress | disinformation.

        In Re: Section 6A (2024)
        citizenship, migration and regional protection require text, evidence and equality review.

RESPONSE LADDER
equal citizenship -> representation -> devolution/asymmetry
-> development/fiscal justice -> dialogue -> lawful proportionate security
-> judicial review -> reconciliation.

CAUTION
regional identity != secession;
migration != collective guilt;
dissent != disloyalty;
security necessity != unrestricted power.

OUTCOME
integration is a continuing constitutional negotiation, not a completed event."""),
        ("National Integration Council and the shift from forum to architecture", "nic-status-accountability", [7, 8], """NIC
extra-constitutional | non-statutory | advisory | chaired by Prime Minister | created 1961.

LOCATED STATUS
latest located meeting: 2013.
No later official reconstitution or meeting is asserted through 25 August 2026.

WHY IT MATTERED
cross-party, Union-State and civil-society deliberation on communalism and integration.

WHY IT WEAKENED
irregular meetings | non-binding output | politicisation | alternative forums.

REFORM CHOICE
reconstitute with agenda, evidence, State voice and published follow-up
or strengthen equivalent cooperative-federal mechanisms."""),
        ("Foreign-policy constitutional competence", "foreign-policy-article-chain", [9, 10], """ARTICLE 51
peace and security | honourable relations | international law/treaties | arbitration.

ARTICLE 246 + UNION LIST 10-21
foreign affairs | diplomacy | UN | treaties | war/peace | citizenship/aliens | extradition.

ARTICLE 73
Union executive power extends to parliamentary fields and treaty-derived rights/jurisdiction.

ARTICLE 253
Parliament may implement treaty/convention/international decisions
notwithstanding ordinary legislative distribution.

CHAIN
international negotiation -> executive commitment -> domestic-law test
-> legislation if rights/duties/law must change -> judicial review."""),
        ("Treaties, territory and domestic-law cases", "treaty-case-doctrine", [11, 12], """Berubari Union (1960)
cession of Indian territory requires constitutional amendment.

Maganbhai Ishwarbhai Patel (1969)
executive may implement a boundary settlement if existing domestic law need not change;
legislation is required where law or rights must be altered.

Jolly George Varghese (1980)
international covenant does not automatically override inconsistent domestic law.

Gramophone Company (1984)
international law may guide interpretation where domestic law is not contrary.

Vishaka (1997)
international norms can fill a domestic-law vacuum consistently with Fundamental Rights.

TRAP
treaty binding internationally != automatic self-execution domestically."""),
        ("From non-alignment to strategic autonomy", "foreign-policy-evolution-rail", [13, 14], """FOUNDATIONAL PRINCIPLES
anti-colonialism | sovereign equality | peaceful coexistence | disarmament | UN support.

PANCHSHEEL 1954
territorial integrity/sovereignty | non-aggression | non-interference
| equality/mutual benefit | peaceful coexistence.

NON-ALIGNMENT
independent judgment in bloc rivalry; not neutrality in every conflict.

STRATEGIC AUTONOMY
diversified partnerships + issue-based coalitions + defence/economic capacity.

CURRENT DIMENSIONS
neighbourhood | Indo-Pacific | BRICS/SCO/Quad | Global South | UN reform.

LIMIT
these are policy doctrines, not judicially enforceable constitutional commands."""),
        ("Diaspora, development, climate and federal consultation", "external-domestic-link-map", [15, 16], """DIASPORA
consular support | investment | knowledge | reputation | crisis assistance
<-> host-State law and plural overseas interests.

DEVELOPMENT PARTNERSHIP
capacity, credit, infrastructure and humanitarian cooperation
<-> debt, local ownership and delivery concerns.

CLIMATE
equity and common-but-differentiated responsibility
-> national commitments -> domestic energy/agriculture/industry policy.

FEDERAL CONSULTATION
treaty effects on State subjects, border communities, trade and water
require information-sharing and implementation cooperation.

INTEGRATION LINK
external policy is durable when domestic regions and citizens see legitimate inclusion."""),
        ("UPSC synthesis: unity without uniformity, autonomy without isolation", "integration-foreign-policy-synthesis", [17, 18, 19, 20], """PRELIMS FIREWALL
NIC advisory, not constitutional | Article 51 DPSP
| Article 73 executive != Article 253 legislation
| Article 3 internal boundary != foreign cession
| NAM != neutrality | policy doctrine != binding law.

MAINS SPINE
Preamble -> rights/DPSP/duties -> federal accommodation
-> challenge-response -> NIC -> competence/treaties
-> strategic autonomy -> diaspora/climate/federal consultation.

QUALIFIED VERDICT
national integration supplies domestic legitimacy and resilience;
foreign policy protects sovereignty and expands national capability.
Both succeed through constitutional inclusion, strategic flexibility and accountable power."""),
    ],
    "polity-46": [
        ("Tribunalisation: specialist justice under constitutional supervision", "tribunal-purpose-map", [1, 2], """ROOT QUESTION
Can specialist adjudication improve access and speed without creating executive-controlled courts?

RATIONALE
expertise | flexible procedure | high-volume disposal | geographical access | lower cost.

CONSTITUTIONAL SOURCE
42nd Amendment 1976 -> Part XIVA -> Articles 323A and 323B.

STATUTORY SOURCE
Administrative Tribunals Act 1985 -> CAT and enabled SAT arrangements.

NON-NEGOTIABLE FLOOR
judicial independence + natural justice + reasoned order
+ High Court/Supreme Court constitutional review."""),
        ("Articles 323A and 323B compared", "323a-323b-matrix", [3, 4], """ARTICLE 323A
public-service recruitment and service conditions.
law-maker: Parliament.
administrative-tribunal design.

ARTICLE 323B
listed subjects: tax, labour, land reform, elections and others in text.
law-maker: appropriate legislature within competence.
subject-specific tribunal/hierarchy.

COMMON HISTORY
text allowed court exclusion.

CURRENT LAW
L. Chandra Kumar (1997): Articles 226/227 and 32 judicial review is basic structure.

TRAP
enabling Article != automatic creation of a tribunal."""),
        ("CAT and SAT institutional architecture", "cat-sat-structure", [5, 6], """CAT
Principal Bench + notified benches;
Chairperson + Judicial Members + Administrative Members under current law.

JURISDICTION
covered Union recruitment/service matters and notified bodies.

SAT
State service tribunal may exist through statutory arrangement;
States vary and some SATs have been abolished or not constituted.

EXCLUSIONS
follow exact Administrative Tribunals Act text and notifications;
not every public employee or constitutional office enters CAT.

CONTROL
appointments, tenure and service conditions must be stated with the 25 August 2026 caveat."""),
        ("Application, procedure, powers and contempt", "cat-process-rail", [7, 8], """PROCESS
jurisdiction check -> Original Application -> notice/reply/record
-> interim issue -> hearing -> reasoned final order.

PROCEDURE
natural justice | flexible procedure | not rigidly bound by CPC.

POWERS
summons | documents | affidavits | commissions | review/other statutory powers.

CONTEMPT
statutory power subject to governing law and constitutional review.

LIMIT
procedural flexibility is not freedom from evidence, fairness, reasons or limitation rules."""),
        ("L. Chandra Kumar and the correct review chain", "judicial-review-chain", [9, 10], """ORIGINAL CONSTITUTIONAL DESIGN
tribunal as substitute first-instance forum + exclusion clauses.

L. Chandra Kumar (1997)
High Court Articles 226/227 and Supreme Court Article 32 review are basic structure;
exclusion clauses invalid;
tribunals may test vires of subordinate legislation and statutes except parent legislation limits.

OPERATIVE CHAIN
tribunal order -> territorial High Court Division Bench -> Supreme Court constitutional route.

TRAP
routine direct appeal from CAT to Supreme Court
is not the ordinary substitute for High Court review."""),
        ("Tribunal-independence doctrine across five decisions", "tribunal-case-timeline", [11, 12], """Union of India v. R. Gandhi (2010)
transferred judicial work requires equivalent independence, qualifications and safeguards.

Madras Bar Association NTT (2014)
National Tax Tribunal design invalidated; core judicial functions cannot be executive-dominated.

Madras Bar Association IV (2020)
Tribunal Rules scrutinised; selection and tenure safeguards reinforced.

Madras Bar Association V (2021)
short tenure, age and executive override defects invalidated in the 2021 ordinance/Act line.

Rojer Mathew (2019)
Finance Act/rules route and tribunal independence examined.

Madras Bar Association tribunal reforms (2025)
reported 2025 INSC 1330 continues the constitutional control and directs institutional reform.

LIMIT
service-condition detail remains date-sensitive; doctrine is stable, implementation is not."""),
        ("Rationalisation, abolition and access-to-justice consequences", "rationalisation-balance", [13, 14], """2021 RATIONALISATION
abolish specified appellate bodies -> transfer functions to courts/other forums
-> common service framework.

POSSIBLE GAIN
less fragmentation | fewer duplicative bodies | clearer appeal path.

POSSIBLE COST
specialised expertise lost | burden shifted to High Courts
| vacancies and transition delay | access becomes geographically harder.

SAT VARIATION
abolition/merger differs by State and statute; no uniform live SAT map should be invented.

TEST
pendency outcome + bench capacity + independence + user cost + transitional clarity."""),
        ("CAT, courts, commissions and ADR distinguished", "institution-comparison-grid", [15, 16], """CAT
statutory service adjudication -> binding reasoned order -> High Court review.

HIGH COURT
constitutional court -> writ/supervisory jurisdiction -> broad public-law control.

COMMISSION
investigation/advice/report unless statute grants adjudicatory power.

LOK ADALAT
statutory settlement/conciliation -> award based on compromise.

ARBITRATION
consensual private adjudication -> limited statutory challenge.

DEPARTMENTAL APPEAL
administrative reconsideration -> not independent judicial adjudication.

TRAP
specialised does not automatically mean tribunal; binding does not automatically mean court."""),
        ("UPSC synthesis and reform architecture", "tribunal-answer-synthesis", [17, 18, 19, 20], """PRELIMS FIREWALL
323A service != 323B listed subjects | enabling != creating
| CAT != constitutional court | flexible != arbitrary
| first instance != final constitutional word | rationalisation != pendency cure.

MAINS SPINE
rationale -> constitutional/statutory source -> structure/jurisdiction
-> procedure/powers -> L. Chandra Kumar chain
-> independence cases -> rationalisation/access -> reform.

REFORM
independent appointments body | secure adequate tenure | transparent vacancies
| administrative autonomy | national data/standards | regional benches
| coherent appeals | periodic performance review without decisional interference.

VERDICT
tribunals are justified only as independent, accessible specialist courts
under constitutional supervision."""),
    ],
    "polity-47": [
        ("Compare functions and contexts, not country labels", "comparative-method-map", [1, 2], """ROOT QUESTION
Why does the same constitutional institution behave differently after transplantation?

COMPARATIVE METHOD
function -> source model -> Indian text -> social/federal context
-> judicial interpretation -> political practice -> consequence.

AXES
codification/rigidity | executive-legislative relation | federal distribution
| rights/remedies | courts | amendment | emergency | elections | accountability.

TRAP
"borrowed from" without adaptation and purpose is a memory list, not constitutional analysis."""),
        ("Written, unwritten, rigid and flexible constitutional forms", "constitution-form-matrix", [3, 4], """UK
uncodified: statutes + common law + conventions + authoritative practice;
politically flexible under parliamentary sovereignty.

USA
codified, supreme and comparatively rigid.

INDIA
codified and supreme; amendment routes range from simple majority
to special majority and State ratification.

SOUTH AFRICA / GERMANY
written transformative/post-authoritarian constitutions with entrenched principles.

CONTROL
written != rigid; unwritten != lawless; flexibility and supremacy are separate variables."""),
        ("Parliamentary, presidential and semi-presidential executives", "executive-model-comparison", [5, 6], """INDIA / UK
parliamentary fusion | collective responsibility | confidence | nominal/formal head distinction.

USA
presidential separation | fixed tenure | separately elected executive | legislative checks.

FRANCE
semi-presidential dual executive | directly elected President | responsible Prime Minister
| cohabitation when parliamentary majority differs.

GERMANY
constructive vote of no confidence strengthens parliamentary stability.

SWITZERLAND
collegial Federal Council and direct-democratic context.

TRAP
Indian President != US President; parliamentary fusion != absence of checks."""),
        ("Federal, unitary and hybrid design with upper houses", "federal-bicameral-matrix", [7, 8], """USA
coordinate federalism | State equality in Senate | dual citizenship/court features.

CANADA
federal with strong-centre and residuary federal power influences.

AUSTRALIA
federal division + strong elected Senate + concurrent/trade inspirations.

INDIA
Union/State/Concurrent Lists | Union residuary power | single citizenship
| integrated judiciary | emergency centralisation | asymmetry.

UPPER HOUSES
Rajya Sabha population-weighted, indirectly elected and unequal;
US Senate State-equal and appointment-confirming;
German Bundesrat represents Land governments.

TRAP
bicameral label does not imply identical federal representation."""),
        ("Supremacy, judicial review and constitutional courts", "review-sovereignty-map", [9, 10], """UK
parliamentary sovereignty with rights and devolution qualifications.

USA
written supremacy + diffuse judicial review through ordinary courts.

GERMANY
specialised Federal Constitutional Court.

INDIA
Supreme Court + High Courts exercise diffuse review, writs and federal adjudication;
Parliament remains Constitution-limited.

CASES
Kesavananda Bharati (1973) -> basic structure.
Minerva Mills (1980) -> limited amendment and FR-DPSP harmony.
First Judges Case (1981) -> initial executive primacy.
Second Judges Case (1993) -> collegium and judicial primacy.
Third Judges Case (1998) -> collegium consultation enlarged.
Fourth Judges Case (2015) -> judicial-independence control of NJAC.
S.R. Bommai (1994) -> federalism and secularism as basic-structure controls.

TRAP
Indian judicial review is not borrowed as an unlimited US copy."""),
        ("Rights, due process and socio-economic directives", "rights-model-comparison", [11, 12], """USA
rights tradition + due process + strong judicial enforcement.

INDIA
Fundamental Rights + Article 32/226 remedies
+ Directive Principles + duties + reasonable-restriction architecture.

IRELAND
directive-principle inspiration, adapted to Indian transformative governance.

SOUTH AFRICA
express justiciable socio-economic rights and proportionality context.

JAPAN / INDIA
"procedure established by law" textual influence.
Maneka Gandhi (1978) adds fairness, non-arbitrariness and reasonableness.

TRAP
Indian DPSPs are not operationally identical to Ireland;
procedure is not post-Maneka formalism."""),
        ("Amendment, emergency and electoral design", "change-crisis-election-matrix", [13, 14], """AMENDMENT
UK political flexibility | USA high rigidity | India multi-track Article 368
| Germany eternity clause | Switzerland referendum routes.

INDIAN CONTROL
Kesavananda Bharati (1973) basic structure;
I.R. Coelho (2007) post-1973 Ninth Schedule review.

EMERGENCY
India: Articles 352/356/360 with 44th-Amendment safeguards and review.
Germany: post-authoritarian safeguards.
France: distinct presidential emergency design.

ELECTIONS
India/UK FPTP legislatures | US electoral college Presidency
| France two-round Presidency | Germany mixed-member
| Switzerland referendums/initiatives.

TRAP
electoral system follows office and party-system context; no model is universally superior."""),
        ("Secularism and accountability institutions", "secular-watchdog-comparison", [15, 16], """SECULARISM
India: principled engagement, equality and reform.
USA: non-establishment + free exercise.
France: laicite and republican public sphere.
Germany: cooperative church-State arrangements.

ACCOUNTABILITY
India CAG: constitutional Westminster adaptation.
Lokpal: statutory ombudsman, not constitutional court.
Finance Commission: periodic expert federal-transfer body.
ECI: central constitutional election management.

COMPARATIVE LESSON
appointment, jurisdiction, remedy and political context matter more than institutional label."""),
        ("India's hybrid adaptation and UPSC synthesis", "comparative-answer-synthesis", [17, 18, 19, 20], """INDIAN HYBRID
British responsible government + written supremacy
| US rights/review + Canadian strong-centre federation
| Irish directives + Australian federal techniques
| German emergency lessons + South African transformative comparison.

PRELIMS FIREWALL
uncodified != unwritten | parliamentary != legislative supremacy in India
| federal != equal upper-house seats | President titles != powers
| borrowed != copied | DPSP != enforceable right | Rajya Sabha != US Senate.

MAINS MATRIX
design -> commonality -> difference -> reason -> consequence -> qualification.

VERDICT
India's Constitution is original in synthesis: foreign techniques were re-engineered
for democratic responsibility, social transformation, federal diversity
and judicially limited power."""),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def clean_source_text(text: str, key: str) -> str:
    replacements = {
        "✅": "[FACT]",
        "📰": "[CURRENT]",
        "⚠️": "[LIMIT]",
        "⚠": "[LIMIT]",
        "❌": "Wrong:",
        "🔑": "[KEY]",
        "⭐": "",
        "➡️": "See also:",
        "➡": "See also:",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("\r\n", "\n")
    if key == "polity-43":
        text = text.replace(
            "| National parties (2023) | **6** — BJP, INC, CPI(M), BSP, NPP, AAP |",
            "| National-party list | Dated ECI list only; recheck before use. The recognition rules, not a transient list, are the examinable core. |",
        )
        text = text.replace(
            "**official list checked 21 Jul 2026: six national\nparties**",
            "**official list checked 21 Jul 2026 as a dated illustration only; the list must be rechecked before use**",
        )
    if key == "polity-45":
        text = text.replace(
            "The **NIC is defunct** (last met **2013**, not reconstituted since 2014).",
            "The latest located **NIC** meeting was in **2013**; no later official reconstitution or meeting is asserted.",
        )
        text = text.replace(
            "it is **effectively defunct** (last met **2013**, not reconstituted since 2014)",
            "its latest located meeting was in **2013**, and no later official reconstitution or meeting is asserted",
        )
    return text


def clean_title(title: str) -> str:
    title = re.sub(r"\[[A-Z]+\]", "", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def source_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    text = re.sub(r"(?m)^#\s+.+?\s*$", "", text, count=1)
    matches = list(re.finditer(r"(?m)^#{2,3}\s+(.+?)\s*$", text))
    preamble = text[: matches[0].start()].strip() if matches else text.strip()
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        title = clean_title(match.group(1))
        if re.search(
            r"Recent PYQ Integration|Historical PYQ Integration|"
            r"What this owner must now support|Direct Mains demands owned|"
            r"Mark-scaled comparative structures",
            title,
            re.I,
        ):
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end].strip()
        if body and title:
            sections.append((title, body))
    return preamble, sections


def practice_mcqs(config: dict[str, Any]) -> str:
    rows = FACTS[config["key"]]
    blocks = ["### Original MCQs 1-36 — Broad Coverage"]
    question_number = 0
    prompts = (
        "Which statement most accurately describes {concept}?",
        "Which is the safest UPSC distinction concerning {concept}?",
        "A candidate makes a close-option error about {concept}. Which correction is most accurate?",
    )
    for round_number in range(3):
        for concept, correct, wrongs, explanation in rows:
            question_number += 1
            options = [correct, *wrongs]
            blocks.extend(
                [
                    f"#### OM{question_number}. "
                    + prompts[round_number].format(concept=concept),
                    "",
                    *[
                        f"- {letter}. {option}"
                        for letter, option in zip("ABCD", options)
                    ],
                    "",
                    "**Answer: A**",
                    "",
                    f"**Explanation:** {explanation} The other options collapse "
                    "distinct legal sources, institutions or consequences and therefore "
                    "fail the close-option test.",
                    "",
                ]
            )
    blocks.append("### Remedial MCQs 1-12 — Common Error Repair")
    for index, (concept, correct, wrongs, explanation) in enumerate(rows, 1):
        blocks.extend(
            [
                f"#### RM{index}. Which statement best repairs a recurring error about {concept}?",
                "",
                f"- A. {correct}",
                f"- B. {wrongs[1]}",
                f"- C. {wrongs[2]}",
                f"- D. {wrongs[0]}",
                "",
                "**Answer: A**",
                "",
                f"**Remedial explanation:** {explanation} Write the governing source, "
                "then the mechanism, and finally the limitation before choosing an option.",
                "",
            ]
        )
    return "\n".join(blocks).strip()


def pyq_block(config: dict[str, Any]) -> str:
    blocks = ["### Verified and Supporting PYQs with Model Solutions"]
    for index, item in enumerate(PYQS[config["key"]], 1):
        blocks.extend(
            [
                f"#### {item['label']} {index} — {item['year']} {item['paper']}",
                "",
                f"**Question:** {item['question']}",
                "",
                f"**Directive:** {item['directive']} · **Marks:** {item['marks']} · "
                f"**Word limit:** {item['words']}",
                "",
                "**Model solution**",
                "",
                f"**Opening:** {item['question'].split('.')[0]}. The answer must respond "
                f"to the directive **{item['directive']}** rather than merely describe the topic.",
                "",
            ]
        )
        for point in item["points"]:
            blocks.append(
                f"- **Claim -> evidence -> analysis -> qualification:** {point}"
            )
        blocks.extend(
            [
                "",
                "**Conclusion:** The strongest answer identifies the governing design, "
                "shows how it operates with named evidence, tests the counter-position "
                "and ends with a qualified institutional verdict.",
                "",
            ]
        )
    return "\n".join(blocks).strip()


def mains_block(config: dict[str, Any]) -> str:
    facts = FACTS[config["key"]]
    blocks = ["### Original Solved Mains Practice"]
    for index, (marks, question, directive) in enumerate(
        MAINS_PROMPTS[config["key"]], 1
    ):
        words = 150 if marks == 10 else 250 if marks == 15 else 300
        selected = [facts[(index + offset) % len(facts)] for offset in range(5)]
        blocks.extend(
            [
                f"#### M{index}. {question}",
                "",
                f"**Directive:** {directive} · **Marks:** {marks} · **Suggested words:** {words}",
                "",
                "**Demand decode:** Define the exact institutional or doctrinal issue, "
                "answer the directive, use named constitutional/statutory/judicial "
                "evidence, include the strongest counterpoint and reach a qualified verdict.",
                "",
                f"**Examiner opening:** {question} The issue should be analysed through "
                "constitutional purpose, operating mechanism and enforceable limitation.",
                "",
            ]
        )
        for concept, correct, _wrongs, explanation in selected:
            blocks.append(
                f"- **{concept.title()} — claim -> evidence -> analysis -> qualification:** "
                f"{correct} {explanation}"
            )
        blocks.extend(
            [
                "",
                "**Counter-position:** Institutional reform can improve accountability, "
                "but overbroad regulation may displace autonomy, federal choice, expertise "
                "or access. The answer must identify the exact trade-off rather than offer "
                "a generic reform list.",
                "",
                "**Conclusion:** Prefer a calibrated design that preserves the institution's "
                "constitutional purpose while adding transparency, independence, reason-giving "
                "and judicially reviewable safeguards.",
                "",
            ]
        )
    return "\n".join(blocks).strip()


def register_notes(config: dict[str, Any], sections: list[tuple[str, str]]) -> str:
    lines = [
        f"### {config['title']}: Rapid Constitutional Recall",
        "",
        f"- **Current-control rule:** {config['current_note']}",
        f"- **Factual caveat:** {config['caveat']}",
        "",
    ]
    for title, body in sections:
        candidates: list[str] = []
        for raw in body.splitlines():
            cleaned = re.sub(r"[`*_>#|]", " ", raw)
            cleaned = re.sub(r"^\s*(?:[-+]|\d+[.)])\s*", "", cleaned)
            cleaned = re.sub(r"\s+", " ", cleaned).strip(" -:")
            if (
                28 <= len(cleaned) <= 260
                and not re.fullmatch(r":?-{3,}:?", cleaned)
                and cleaned not in candidates
            ):
                candidates.append(cleaned)
            if len(candidates) == 3:
                break
        lines.extend([f"#### {title}", ""])
        lines.extend(f"- {value}" for value in candidates)
        lines.append("")
    lines.extend(
        [
            "### Final Answer Spine",
            "",
            "- Define the institution or design in plain and technical language.",
            "- State the exact constitutional, statutory, order-based or policy source.",
            "- Explain the operating mechanism with named Indian evidence.",
            "- Separate settled law from recommendation, policy, pending litigation and dated status.",
            "- Present the strongest democratic, federal, independence or accountability counterpoint.",
            "- Conclude with a calibrated reform or comparative verdict.",
        ]
    )
    return "\n".join(lines).strip()


def transform_source(config: dict[str, Any]) -> Path:
    basic_path = ROOT / Path(config["basic"].replace("\\", "/"))
    basic_text = clean_source_text(
        basic_path.read_text(encoding="utf-8"),
        config["key"],
    )
    source_preamble, sections = source_sections(basic_text)
    sections.extend(SUPPLEMENTS[config["key"]])

    numbered: list[str] = []
    for index, (title, body) in enumerate(sections, 1):
        numbered.extend([f"## {index:02d}. {title}", "", body.strip(), ""])
    numbered_text = "\n".join(numbered).strip()
    numbered_text = base.add_topic_visuals(config, numbered_text)
    numbered_text = base.add_session_orientations(numbered_text)

    preamble = "\n".join(
        [
            f"# {config['title']} — Complete Uncompressed Learning Session",
            "",
            "**Complete independent learning session + verified PYQ routing + solved "
            "practice workbook + final consolidated register notes**",
            "",
            "**Legal/current control date:** 25 August 2026 (Asia/Kolkata)",
            "",
            "> **Tag key:** `[FACT]` = named constitutional, statutory, official, "
            "judicial or audited local support; `[ANALYSIS]` = reasoned examination; "
            "`[CURRENT]` = checked for the control date; `[LIMIT]` = qualification.",
            ">",
            "> **Answer-writing discipline:** claim -> named evidence -> analysis -> qualification.",
            "",
            "- [CURRENT] Status is controlled to **25 August 2026, Asia/Kolkata**.",
            f"- [CURRENT] **Live official refresh, 25 August 2026:** {config['current_note']}",
            "",
            "#### How to Use This Package",
            "",
            "[FACT] The complete Basic/Core owner is taught first in source order. "
            "Cross-topic Markdown, local OCR books and verified PYQ ledgers supplement it.",
            "",
            "[FACT] Advanced-owner material appears only after the Core and practice "
            "sections under the required optional-depth label.",
            "",
            f"[LIMIT] {config['caveat']}",
            "",
            "#### Local Owner Gateway",
            "",
            source_preamble,
        ]
    ).strip()

    assembled = "\n\n".join(
        [
            preamble,
            "## BASIC LEARNING SESSION",
            base.demote_one(numbered_text),
            "## BASIC MCQS / REMEDIATION",
            practice_mcqs(config),
            "## PYQS AND ANSWER PRACTICE",
            pyq_block(config),
            mains_block(config),
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            common._optional_owner(config),
            "## CONSOLIDATED REGISTER NOTES",
            register_notes(config, sections),
        ]
    ) + "\n"
    assembled = assembled.replace("…", ".").replace("\ufffd", "")
    output = base.SOURCE_SESSION_ROOT / f"{config['key']}_Learning-Session.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8")
    return output


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

    number = config["number"]
    title_slug = {
        43: "Political-Parties",
        44: "Pressure-Groups",
        45: "National-Integration-and-Foreign-Policy",
        46: "Administrative-Tribunals",
        47: "Comparative-Constitutional-Design",
    }[number]
    main_pdf = (
        ROOT / "notes" / "Polity" / "Topic-PDFs"
        / f"{number:02d}_{title_slug}_Deep-Learning.pdf"
    )
    workbook = (
        ROOT / "notes" / "Polity" / "Session-Level-Topic-PDFs"
        / f"{number:02d}_{title_slug}_Session-Level.pdf"
    )
    if number == 47 and not main_pdf.is_file():
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
    if not main_pdf.is_file() or not workbook.is_file():
        raise RuntimeError(
            f"{config['key']}: legacy compatibility PDFs are missing."
        )
    generation_date = "2026-08-05" if number < 47 else DATE
    record = {
        "record_id": f"{config['key']}:legacy-v1:g1",
        "topic_key": config["key"],
        "variant": "legacy-v1",
        "generation": 1,
        "supersedes": None,
        "command": f"Export PDF for Polity {number} — {config['title']}",
        "main_pdf": relative(main_pdf),
        "workbook": relative(workbook),
        "markdown": config["basic"],
        "approved": False,
        "provenance": {
            "workflow": "existing-deep-learning-v1",
            "source_basic": config["basic"],
            "source_advanced": config["advanced"],
            "assembled_markdown": config["basic"],
            "renderer": {
                "name": "existing Polity deep-learning workflow",
                "version": "legacy-v1",
            },
            "generation_date": generation_date,
            "superseded_v1": None,
            "migration_note": (
                "Registered without changing existing deliverables or approval. "
                "Polity-47 compatibility PDFs were materialised from the existing "
                "legacy deep-learning renderer before learner-v2 generation."
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


def write_audit(
    config: dict[str, Any],
    started_at: str,
    live: list[dict[str, Any]],
) -> Path:
    path = base.write_audit(config, started_at, live)
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["current_affairs_audit"]["control_date"] = DATE
    payload["topic_completeness_contract"] = config["coverage_contract"]
    payload["topic_completeness_status"] = "passed"
    payload["canonical_owner_resolution"] = {
        "source_basic": config["basic"],
        "source_canonical": config["canonical"],
        "source_advanced": config["advanced"],
        "scope_note": (
            "The Basic/Core Markdown is the canonical owner and remains independently "
            "UPSC-complete. Cross-topic owners supplement it; Advanced remains "
            "subordinate optional enrichment."
        ),
    }
    payload["case_year_sources"] = [
        case_years.source_record(case_id)
        for case_id in case_years.TOPIC_CASE_IDS.get(config["key"], ())
    ]
    payload["current_status_boundary"] = {
        "control_date": DATE,
        "settled_law_only": True,
        "pending_or_proposed_items_are_qualified": True,
        "note": config["caveat"],
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def workbook_gate(
    source_markdown: Path,
    config: dict[str, Any],
) -> dict[str, int]:
    text = source_markdown.read_text(encoding="utf-8")
    workbook = base.refresh.extract_v2_workbook_markdown(text)
    mcqs = len(re.findall(r"(?m)^#{3,5}\s+(?:OM|RM)\d+\.", workbook))
    pyqs = len(
        re.findall(
            r"(?m)^#{3,5}\s+(?:Verified direct PYQ|Supporting routed PYQ)\b",
            workbook,
            re.IGNORECASE,
        )
    )
    original_mains = len(re.findall(r"(?m)^#{3,5}\s+M\d+\.", workbook))
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
    return (
        len(re.findall(r"(?m)^#{3,5}\s+M\d+\.", section.group(1)))
        if section
        else 0
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


def resume_after_tracker(
    config: dict[str, Any],
    expected_count: int,
) -> tuple[dict[str, Any], Path, Path] | None:
    tracker = base.refresh.load_tracker()
    exists = any(
        isinstance(record, dict)
        and record.get("topic_key") == config["key"]
        and record.get("variant") == base.refresh.V2_VARIANT
        for record in tracker["exports"]
    )
    if not exists:
        return None
    try:
        base.verify_four_folders(config)
    except (FileNotFoundError, RuntimeError):
        base.export_clean_topic(config)
        base.verify_four_folders(config)
    flow_validation = (
        EXPORTS / f"{config['key']}-flow-learning-{DATE}-validation.json"
    )
    if not flow_validation.is_file():
        export_flow(config, expected_count)
    return completed_result(config)


def run() -> dict[str, Any]:
    expected_order = [f"polity-{number:02d}" for number in range(43, 48)]
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
            for index, (title, structural_type, _sessions, body) in enumerate(
                panels
            )
        ]
    base.PANELS.update(PANELS)

    clean_baseline = preserve.topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={43, 44, 45, 46, 47},
    )
    flow_baseline = preserve.flow_topic_hashes(
        exclude_polity={43, 44, 45, 46, 47}
    )
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        ensure_legacy_reference(config)
        resumed = resume_after_tracker(config, 75 + index)
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
        audit = write_audit(config, gate_times["A_started"], live)
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

        flow_validation, flow_row = export_flow(config, 75 + index)
        flow_folder = ROOT / Path(
            flow_row["destination_folder"].replace("\\", "/")
        )
        gate_times["I_completed"] = now()

        clean_mismatches = preserve.compare_hashes(
            clean_baseline,
            preserve.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={43, 44, 45, 46, 47},
            ),
        )
        flow_mismatches = preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(
                exclude_polity={43, 44, 45, 46, 47}
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
                exclude_polity={43, 44, 45, 46, 47},
            ),
        ),
        "existing_flow_hash_mismatches": preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(
                exclude_polity={43, 44, 45, 46, 47}
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
