"""Generate Polity learner-v2 topics 23-27 in strict preservation-safe order."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_18_22_sequential as prior


base = prior.base
case_years = prior.case_years
ROOT = prior.ROOT
DATE = prior.DATE
SECTION = prior.SECTION
EXPORTS = prior.EXPORTS
FINAL_LIBRARY = prior.FINAL_LIBRARY
FLOW_LIBRARY = prior.FLOW_LIBRARY
BATCH_ID = "polity-23-27-sequential-batch-2026-08-24"


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
        "polity-23",
        "Panchayati Raj",
        "upsc-ai-kit\\knowledge\\Polity\\23_Panchayati-Raj_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\23_Panchayati-Raj.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\12_Local-Governance-and-Service-Delivery.md",
        ],
        [
            "https://panchayat.gov.in/",
            "https://egramswaraj.gov.in/",
            "https://auditonline.gov.in/",
            "https://svamitva.nic.in/svamitva/",
            "https://fincomindia.nic.in/",
        ],
        2,
        2,
        "The Ministry of Panchayati Raj, eGramSwaraj, AuditOnline, SVAMITVA and "
        "Finance Commission portals were rechecked on 24 August 2026. The "
        "Devolution Index 2024 and 2026-31 local-body grant period are dated "
        "anchors; no changing dashboard total is frozen.",
        "Part IX constitutionalises institutions, elections and inclusion but "
        "leaves substantive devolution mainly to State law. PESA applies to "
        "Fifth Schedule Scheduled Areas with statutory modifications; digital "
        "uploads do not prove Gram Sabha power or actual three-F devolution.",
        [
            "democratic-decentralisation history, committees and 73rd Amendment",
            "Part IX Articles 243-243O, Eleventh Schedule, Gram Sabha and tiers",
            "elections, reservations, tenure, disqualification, SEC and SFC",
            "Article 243G/H devolution, 29 subjects, finance, functionaries and capacity",
            "PESA, Scheduled-Area boundary, planning, accountability, cases and comparison",
        ],
        visual_sessions=[1, 2, 3, 4, 7, 11, 13, 14, 17, 21, 24, 26, 29, 36, 40, 41],
    ),
    topic(
        "polity-24",
        "Municipalities",
        "upsc-ai-kit\\knowledge\\Polity\\24_Municipalities_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\24_Municipalities.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\12_Local-Governance-and-Service-Delivery.md",
            "upsc-ai-kit\\knowledge\\Geography\\28_Human-Settlements-and-Urbanisation_Complete-Topic-Package.md",
        ],
        [
            "https://mohua.gov.in/",
            "https://amrut.mohua.gov.in/",
            "https://fincomindia.nic.in/",
            "https://www.sebi.gov.in/",
            "https://www.indiacode.nic.in/",
        ],
        2,
        2,
        "Official MoHUA, AMRUT, Finance Commission, SEBI and India Code portals "
        "were rechecked on 24 August 2026. Property tax, user charges, municipal "
        "bonds and grants remain financing tools; programme and city totals are "
        "treated only as dated evidence.",
        "Part IXA secures municipal form more strongly than functional autonomy. "
        "Mayor-commissioner arrangements, parastatals, bond eligibility and "
        "tax design vary by State law and city; mission or digital status is not "
        "proof of constitutional devolution.",
        [
            "urban-governance evolution, 74th Amendment and Articles 243P-243ZG",
            "municipal types, industrial-township proviso, wards and representation",
            "Article 243W, Twelfth Schedule, three Fs and service delivery",
            "property tax, user charges, bonds, grants, audit and fiscal accountability",
            "DPC/MPC, metropolitan governance, parastatals, cases, comparison and reform",
        ],
        visual_sessions=[1, 2, 3, 6, 9, 15, 18, 21, 24, 27, 31, 32, 34, 39, 47, 48],
    ),
    topic(
        "polity-25",
        "Union Territories",
        "upsc-ai-kit\\knowledge\\Polity\\25_Union-Territories_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Union-Territories.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\25_Union-Territories.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Union-and-Territory.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
        ],
        [
            "https://www.mha.gov.in/en/divisionofmha/union-territory-division",
            "https://www.indiacode.nic.in/",
            "https://delhi.gov.in/",
            "https://www.jk.gov.in/",
            "https://ladakh.gov.in/",
        ],
        2,
        0,
        "MHA, India Code, Delhi, Jammu and Kashmir and Ladakh official portals "
        "were rechecked on 24 August 2026. India continues to have eight Union "
        "Territories; Delhi, Puducherry and Jammu and Kashmir have legislatures.",
        "The GNCTD Amendment Act, 2023 is treated as operative unless displaced "
        "by a later binding judgment. Jammu and Kashmir remains a Union Territory "
        "with legislature and Ladakh one without; Statehood and new special-status "
        "demands are not presented as enacted law.",
        [
            "Articles 1 and 239-241, rationale, history and current classification",
            "President, Administrator/LG, legislature and Parliament override models",
            "Delhi Article 239AA/AB, services, reserved fields and controlling cases",
            "Puducherry Article 239A/B, J&K statute and bounded non-legislature profiles",
            "Article 240, judiciary, budget, representation, reorganisation and comparisons",
        ],
        visual_sessions=[1, 2, 3, 5, 6, 10, 13, 14, 22, 24, 27, 29, 31, 34, 38, 45],
    ),
    topic(
        "polity-26",
        "Scheduled and Tribal Areas",
        "upsc-ai-kit\\knowledge\\Polity\\26_Scheduled-and-Tribal-Areas_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\26_Scheduled-and-Tribal-Areas.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
            "upsc-ai-kit\\knowledge\\Environment-and-Ecology\\basic\\12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
        ],
        [
            "https://tribal.nic.in/",
            "https://panchayat.gov.in/",
            "https://www.indiacode.nic.in/",
            "https://www.mha.gov.in/en/commoncontent/north-east-division",
            "https://www.sci.gov.in/",
        ],
        6,
        0,
        "Ministry of Tribal Affairs, Panchayati Raj, India Code, MHA and Supreme "
        "Court portals were rechecked on 24 August 2026. The Fifth and Sixth "
        "Schedules, PESA and FRA remain distinct operative layers.",
        "Ladakh or other extension demands, negotiating positions and accords are "
        "not constitutional amendments or Sixth Schedule inclusion by themselves. "
        "PESA consultation, recommendation and approval verbs must not be converted "
        "into one universal veto.",
        [
            "Articles 244/244A and complete Fifth-Sixth Schedule comparison",
            "Scheduled Area declaration, Governor, TAC, reports and regulations",
            "district/regional councils, four-State scope and law/judicial/fiscal powers",
            "PESA-FRA-land-resource interaction, safeguards and verified case limits",
            "Article 371/Panchayat distinctions, autonomy-development tensions and reform",
        ],
        visual_sessions=[1, 2, 3, 5, 8, 10, 12, 18, 21, 24, 27, 33, 35, 41, 44, 56],
    ),
    topic(
        "polity-27",
        "Election Commission",
        "upsc-ai-kit\\knowledge\\Polity\\27_Election-Commission_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\27_Election-Commission.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
        ],
        [
            "https://www.eci.gov.in/about-eci",
            "https://www.indiacode.nic.in/",
            "https://www.sci.gov.in/",
            "https://www.eci.gov.in/election-management",
            "https://www.eci.gov.in/evm",
        ],
        3,
        6,
        "ECI, India Code and Supreme Court official portals were rechecked on "
        "24 August 2026. The official ECI leadership control remains Gyanesh "
        "Kumar, Dr Sukhbir Singh Sandhu and Dr Vivek Joshi on this dated audit.",
        "The 2023 appointment Act operates; the pending challenge is not described "
        "as finally upheld or struck down. ECI does not conduct local-body elections, "
        "does not replace the Delimitation Commission and cannot regulate every "
        "internal party matter without legal authority.",
        [
            "Article 324 position, composition, appointment, tenure and removal",
            "2023 appointment Act, current challenge, independence and accountability",
            "rolls, schedules, symbols, MCC, repolls and disqualification advice",
            "RPA 1950/1951, delimitation, NOTA, parties and regulatory limits",
            "finance, criminalisation, paid news, social media, EVM-VVPAT, cases and reform",
        ],
        visual_sessions=[1, 2, 3, 4, 6, 9, 14, 17, 22, 25, 28, 33, 35, 39, 44, 61],
    ),
]


SUPPLEMENTS: dict[str, str] = {
    "polity-23": r"""
## 40. Panchayats and Municipalities compared

| Dimension | Panchayats | Municipalities |
|---|---|---|
| constitutional home | Part IX | Part IXA |
| amendment | 73rd | 74th |
| schedule | Eleventh: 29 matters | Twelfth: 18 matters |
| participatory base | Gram Sabha | Ward Committee where Article 243S applies |
| types | village, intermediate, district | Nagar Panchayat, Council, Corporation |
| planning bridge | District Planning Committee | DPC plus Metropolitan Planning Committee |
| elections | State Election Commission | State Election Commission |
| fiscal review | State Finance Commission | same State Finance Commission |

[LIMIT] Neither Schedule transfers functions automatically; State legislation and activity
mapping determine operational control.

## 41. Local-body case law and Gram Nyayalaya boundary

| Decision | Exam-safe holding |
|---|---|
| Kishansing Tomar (2006) | timely local elections are a constitutional command |
| K. Krishna Murthy (2010) | local political reservation needs distinct constitutional care |
| Vikas Kishanrao Gawali (2021) | OBC reservation requires the judicially stated triple test |
| State of Goa v. Fouziya Imtiaz Shaikh (2021) | SEC independence cannot be executive-subordinate |

[FACT] Gram Nyayalayas arise under the Gram Nyayalayas Act, 2008. They are statutory
judicial institutions, not Gram Sabhas, Gram Panchayats or a fourth Panchayat tier.
""",
    "polity-24": r"""
## 47. Panchayats and Municipalities compared

| Dimension | Rural local government | Urban local government |
|---|---|---|
| constitutional home | Part IX | Part IXA |
| amendment | 73rd | 74th |
| schedule | Eleventh: 29 | Twelfth: 18 |
| direct forum | Gram Sabha | ward-level institutions under State law |
| forms | village, intermediate, district | Nagar Panchayat, Council, Corporation |
| integrated planning | DPC | DPC and MPC |
| election manager | State Election Commission | State Election Commission |
| fiscal review | State Finance Commission | State Finance Commission |

[LIMIT] A census town is not automatically a municipality, and an industrial area is not
automatically an industrial township under the Article 243Q proviso.

## 48. Local-body elections and reservation case law

| Decision | Exam-safe holding |
|---|---|
| Kishansing Tomar (2006) | election delay cannot defeat the five-year constitutional cycle |
| K. Krishna Murthy (2010) | backward-class political reservation needs local-body analysis |
| Vikas Kishanrao Gawali (2021) | triple test controls OBC reservation in local bodies |
| State of Goa v. Fouziya Imtiaz Shaikh (2021) | the SEC must remain institutionally independent |

[LIMIT] These decisions do not create one national municipal design; State law continues to
govern offices, mayoral form, disqualification detail and administrative organisation.
""",
    "polity-26": r"""
## 56. Scheduled Tribe safeguards beyond the territorial Schedules

| Provision | Function |
|---|---|
| Article 46 | DPSP for educational/economic interests and protection from exploitation |
| Articles 330 and 332 | political reservation in Lok Sabha and State Assemblies |
| Article 335 | ST claims in services, consistently with administrative efficiency |
| Article 275(1) | constitutional grants for specified welfare and administration needs |
| Article 338A | National Commission for Scheduled Tribes |
| Article 339 | presidential commission and Union welfare-scheme directions |

[FACT] The NCST investigates and monitors safeguards, inquires into complaints, advises on
planning and reports to the President. It does not replace the Governor, TAC, Gram Sabha or ADC.
""",
    "polity-27": r"""
## 61. Paid news, social media and campaign-finance boundary

| Problem | ECI-linked tool | Constitutional or statutory limit |
|---|---|---|
| candidate expenditure | accounts, observers, monitoring teams | ceiling and liability follow law |
| paid news | media monitoring and expense attribution where supported | facts and due process matter |
| political advertising | certification and expenditure disclosure rules | not general content censorship |
| misinformation/deepfakes | MCC directions, advisories and applicable law | ECI cannot invent offences |
| criminalisation | candidate disclosure and lawful disqualification routes | ECI cannot add RPA grounds |
| party finance | disclosure platform and election administration | Parliament defines core regime |

[LIMIT] Candidate expenditure ceilings and party campaign expenditure are not identical.
Platform regulation, criminal liability and takedown powers require the applicable statute,
rules, court orders and reasoned procedural safeguards.
""",
}


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-23": [
        (
            "From democratic decentralisation to constitutional local government",
            "decentralisation-timeline",
            [1, 2, 3],
            """ROOT QUESTION
How did village administration become constitutionally protected self-government?

ARTICLE 40 -> organise village Panchayats and endow self-government powers.
1957 Balwant Rai Mehta -> three tiers and democratic decentralisation.
1977-78 Ashok Mehta -> district-centred two-tier alternative.
1985 G.V.K. Rao -> district development administration.
1986 L.M. Singhvi -> constitutional status + Gram Sabha.

73RD AMENDMENT ACT, 1992
Part IX + Eleventh Schedule -> effective 24 April 1993.

CORE LIMIT
constitutional status guarantees democratic form; State law controls devolution substance.""",
        ),
        (
            "Part IX architecture: Gram Sabha, tiers and constitutional exceptions",
            "part-ix-architecture",
            [3, 4, 5, 23],
            """PART IX: ARTICLES 243-243O
243A Gram Sabha | 243B tiers | 243C composition | 243D reservation
243E duration | 243F disqualification | 243G powers | 243H finance
243I SFC | 243J audit | 243K SEC | 243O election bar.

THREE-TIER DEFAULT
district -> intermediate -> village.
State population <= 20 lakh may omit only the intermediate tier.

GRAM SABHA
all registered voters in a village area; exact powers come from State law.

ARTICLE 243M
specified Scheduled/tribal and other excluded areas require distinct legal routes.
PESA, 1996 extends Part IX principles to Fifth Schedule areas with modifications.""",
        ),
        (
            "Representation, election, continuity and reservation controls",
            "local-democracy-cycle",
            [6, 7, 8, 9, 10, 21, 22],
            """DEMOCRATIC CYCLE
direct election to territorial seats -> chairperson route under State law
-> five-year term -> election before expiry or within six months of dissolution.

ARTICLE 243D
SC/ST reservation linked to population; not less than one-third seats for women.
Chairperson reservations include women and SC/ST; many States exceed the floor.

ARTICLE 243K
State Election Commission controls Panchayat rolls and elections.

ARTICLE 243O
delimitation/allotment barred from ordinary challenge; election petition is the route.

TRAPS
candidate age floor is 21 | ECI does not conduct Panchayat elections
| reservation creates access but proxy control can block substantive authority.""",
        ),
        (
            "Article 243G, Eleventh Schedule and the three-F functionality test",
            "devolution-functionality-system",
            [11, 12, 13, 33, 34],
            """ARTICLE 243G IS ENABLING
State legislature may endow Panchayats with self-government powers.

ELEVENTH SCHEDULE: 29 MATTERS
agriculture/land/water -> rural infrastructure -> health/education
-> poverty alleviation -> welfare -> community assets.

FUNCTIONS
clear activity map and tier responsibility.
FUNCTIONARIES
staff placement, direction and accountability to the elected body.
FINANCES
own revenue + assigned revenue + predictable grants + spending discretion.

FUNCTIONALITY TEST
Can the Panchayat decide, direct staff, spend and answer publicly for outcomes?""",
        ),
        (
            "Fiscal constitution: own revenue, SFC, Union grants and audit",
            "panchayat-finance-ladder",
            [14, 15, 16, 17, 18, 19],
            """ARTICLE 243H
State law may authorise taxes/duties/tolls/fees, assignments, grants and Panchayat Funds.

OWN-SOURCE BASKET
property/market levies | licence/service fees | user charges | rents
| ponds/fisheries/community assets | State-law borrowing.

ARTICLE 243I
Governor constitutes SFC every five years -> tax sharing, assignments, grants and measures.

ARTICLE 280
Union Finance Commission recommends augmentation of State funds for Panchayats
on the basis of SFC recommendations.

ACCOUNTABILITY
Article 243J accounts/audit -> public records -> social audit -> corrective action.
LIMIT grants equalise capacity but cannot substitute for State tax devolution.""",
        ),
        (
            "PESA, Scheduled Areas and community-centred decision verbs",
            "pesa-scheduled-area-map",
            [23, 24, 25],
            """FIFTH SCHEDULE AREA
ordinary Part IX exclusion under Article 243M -> PESA, 1996 extension with modifications.

PESA GRAM SABHA
community resources + customs + cultural identity + customary dispute practices.

DECISION VERBS MUST STAY DISTINCT
consultation != recommendation != prior recommendation != approval.

LAND AND RESOURCES
prevent alienation + restore unlawfully alienated land
| minor minerals and markets within the exact statutory allocation.

FRA LINK
forest-right recognition and community forest-resource powers overlap but do not merge.

LIMIT PESA is not an unlimited veto over every project or every Scheduled Tribe area.""",
        ),
        (
            "Planning, accountability, digital tools and judicial boundary",
            "panchayat-accountability-network",
            [20, 26, 27, 28, 29, 30, 31, 32],
            """PLANNING CHAIN
Gram Sabha priorities -> GPDP -> intermediate/district convergence
-> DPC consolidates Panchayat and municipal plans under Article 243ZD.

ACCOUNTABILITY CHAIN
notice + records + quorum/inclusion -> social audit -> audit trail -> follow-up.

DIGITAL TOOLS
eGramSwaraj planning/accounts | AuditOnline audit workflow
| SVAMITVA survey/property cards | RGSA capacity building.

CAUTION
portal entry != lawful devolution, informed consent or service quality.

JUDICIAL BOUNDARY
Gram Nyayalayas Act, 2008 courts != Gram Sabha or Panchayat institutions.""",
        ),
        (
            "Panchayat-municipality comparison and controlling local-body cases",
            "local-body-comparison-case-matrix",
            [37, 40, 41],
            """PANCHAYATS                           MUNICIPALITIES
Part IX | 73rd | Eleventh 29        Part IXA | 74th | Twelfth 18
Gram Sabha                            Ward Committee where Article 243S applies
village/intermediate/district         Nagar Panchayat/Council/Corporation

COMMON CONTROLS
SEC elections | SFC fiscal review | DPC planning bridge | State-law devolution.

CASE CODE
Kishansing Tomar (2006) -> timely local elections.
K. Krishna Murthy (2010) -> reservation requires local-body constitutional analysis.
Vikas Kishanrao Gawali (2021) -> OBC-reservation triple test.
State of Goa v. Fouziya Imtiaz Shaikh (2021) -> independent SEC.

LIMIT cases regulate constitutional boundaries; they do not create one national local law.""",
        ),
        (
            "Implementation gaps, reform sequence, PYQ routes and final synthesis",
            "panchayat-reform-answer-spine",
            [33, 34, 35, 36, 38, 39],
            """DIAGNOSIS
regular elections + representation gains
but vague activity maps + departmental staff + weak own revenue + delayed SFCs.

REFORM SEQUENCE
binding activity map -> accountable local cadre -> predictable untied finance
-> fair own-revenue reform -> strong Gram Sabha -> audit/social audit
-> assisted digital access -> outcome-based GPDP.

PYQ ROUTES
finance beyond grants | women and patriarchy | three Fs to functionality
| intermediate-tier exception | PESA limits.

MAINS SPINE
define decentralisation -> cite Part IX -> explain mechanism -> show gap
-> named case/current anchor -> State-variation qualification -> functionality verdict.

SYNTHESIS
representation becomes self-government only when authority, staff and money converge.""",
        ),
    ],
    "polity-24": [
        (
            "Urban constitutionalisation and the Article 243Q institutional map",
            "urbanisation-constitutional-timeline",
            [1, 2, 3, 4, 5, 6, 7],
            """URBAN GOVERNANCE PROBLEM
growth across wards and agencies -> services, planning, finance and democratic voice.

74TH AMENDMENT ACT, 1992
Part IXA + Twelfth Schedule -> constitutional municipal framework from 1 June 1993.

ARTICLE 243P DEFINITIONS
municipality | municipal area | ward | metropolitan area | population.

ARTICLE 243Q TYPES
transitional area -> Nagar Panchayat
smaller urban area -> Municipal Council
larger urban area -> Municipal Corporation.

INDUSTRIAL-TOWNSHIP PROVISO
Governor may specify after considering municipal services supplied/proposed;
it is an exception, not the status of every industrial or census town.""",
        ),
        (
            "Council, wards, reservation, tenure and State Election Commission",
            "municipal-democracy-cycle",
            [8, 9, 10, 11, 12, 13, 14],
            """ARTICLE 243R
directly elected ward representatives; State law may add specified representation.

ARTICLE 243S
Ward Committees mandatory in municipalities with population >= three lakh.
State law fixes composition, area and additional committees.

ARTICLE 243T
SC/ST population-linked reservation + not less than one-third seats for women.

ARTICLE 243U
five-year duration; hearing before dissolution; timely re-election.

ARTICLE 243ZA
State Election Commission controls municipal rolls and elections.

LIMIT compulsory democratic form does not itself transfer functions, staff or finance.""",
        ),
        (
            "Article 243W, Twelfth Schedule and measurable service devolution",
            "twelfth-schedule-functionality-map",
            [15, 16, 17, 18, 38],
            """ARTICLE 243W IS ENABLING
State law may endow municipalities with self-government and scheme functions.

TWELFTH SCHEDULE: 18 MATTERS
urban planning + land use + roads + water + public health/sanitation
-> fire services + urban forestry/environment
-> weaker sections/slums/poverty
-> amenities/culture + burials + cattle pounds
-> vital statistics + street lighting/parking/bus stops/public conveniences.

THREE-F TEST
function assigned? | staff controlled? | money predictable and discretionary?

SERVICE TEST
clear responsibility -> standard -> budget -> delivery -> grievance -> public audit.""",
        ),
        (
            "Municipal finance: property tax, user charges, bonds and grants",
            "municipal-finance-portfolio",
            [19, 20, 21, 22, 23, 24, 25, 26],
            """ARTICLE 243X
State law may authorise taxes, duties, tolls, fees, assignments, grants and funds.

ARTICLE 243Y
the State Finance Commission reviews municipal and Panchayat finances.

OWN REVENUE
property tax -> complete register + fair valuation + billing + collection + appeal.
user charge -> service cost + affordability protection + transparent subsidy.

CAPITAL FINANCE
municipal bond -> accounts + revenue stream + disclosure + credit discipline.
pooled finance -> smaller bodies aggregate borrowing capacity.

GRANTS
equalisation and national priorities; tied money cannot replace local fiscal authority.""",
        ),
        (
            "Mayor-commissioner relations, parastatals and mission SPVs",
            "urban-executive-accountability-map",
            [27, 28, 29, 30],
            """ELECTED COUNCIL / MAYOR
mandate -> priorities -> budget -> public answerability.

MUNICIPAL COMMISSIONER
State-law executive authority -> administration -> engineering/procurement continuity.

MODEL CAVEAT
mayor selection, tenure, executive power and commissioner control vary by State law.

PARASTATALS
water/transport/development authorities may add expertise and regional scale
but can fragment money, staff and accountability.

MISSION SPVs
project focus + professional delivery
must remain aligned with elected plans, transparent accounts and municipal ownership.

ANSWER TEST
who decides? who spends? who employs? who answers to voters?""",
        ),
        (
            "DPC, MPC and government at the scale of the city-region",
            "metropolitan-planning-system",
            [31, 32, 33, 34, 35, 36, 37],
            """ARTICLE 243ZD: DISTRICT PLANNING COMMITTEE
Panchayat plans + municipal plans -> draft district development plan.
At least four-fifths elected by/from district Panchayat and municipal elected members.

ARTICLE 243ZE: METROPOLITAN PLANNING COMMITTEE
municipal + Panchayat plans -> metropolitan development plan.
At least two-thirds elected by/from municipal members and Panchayat chairpersons.

METROPOLITAN AREA
population ten lakh or more across one or more districts and local bodies.

PERI-URBAN CHOICE
Nagar Panchayat | merger | joint authority | phased transition.

LIMIT constitutional plan preparation needs alignment with agencies, budgets and land powers.""",
        ),
        (
            "Citizen participation, accountability and bounded digital reform",
            "urban-accountability-loop",
            [39, 40, 41, 42],
            """DOWNWARD ACCOUNTABILITY
ward voice -> open budget -> service standard -> grievance redress
-> audit/report -> council correction -> electoral sanction.

FISCAL ACCOUNTABILITY
asset register + double-entry accounts + audit + public disclosure + procurement control.

DIGITAL / SMART TOOLS
GIS property base | online permissions/payments | dashboards | sensor data.

CAUTION
technology can expose performance and expand access
but cannot cure missing staff, fragmented authority or digital exclusion by itself.

REFORM
activity mapping + stronger wards + professional cadre + accountable executive
-> integrated planning + viable revenue + transparent service contracts.""",
        ),
        (
            "Rural-urban comparison and local-government case-law controls",
            "municipal-comparison-case-matrix",
            [43, 45, 47, 48],
            """PANCHAYAT                             MUNICIPALITY
Part IX / Eleventh 29                Part IXA / Twelfth 18
Gram Sabha                            Ward Committee where Article 243S applies
rural three-tier map                  transitional/smaller/larger urban forms.

COMMON
State-law devolution | SEC elections | SFC review | DPC linkage.

CASE CODE
Kishansing Tomar (2006) -> constitutional election timetable.
K. Krishna Murthy (2010) -> local reservation analysis.
Vikas Kishanrao Gawali (2021) -> OBC triple test.
State of Goa v. Fouziya Imtiaz Shaikh (2021) -> SEC independence.

TRAP census town != municipality | every industrial area != industrial township.""",
        ),
        (
            "Urban reform, Prelims traps, PYQ spine and qualified synthesis",
            "municipal-answer-synthesis",
            [40, 42, 43, 44, 45, 46],
            """CORE DIAGNOSIS
constitutional existence and elections
without assured functions, metropolitan coordination, staff control or buoyant revenue.

REFORM LADDER
State activity map -> empowered wards -> stable elected leadership
-> professional administration -> property/user-charge reform
-> accountable bonds/grants -> agency-plan convergence -> public audit.

PRELIMS FIREWALL
243Q types | 243S three-lakh Ward Committee threshold
| DPC four-fifths | MPC two-thirds | metropolitan population ten lakh
| SEC, not ECI | Twelfth Schedule does not transfer automatically.

MAINS SPINE
constitutional design -> operational gap -> finance/governance mechanism
-> city-region evidence -> State-law caveat -> democratic functionality verdict.""",
        ),
    ],
    "polity-25": [
        (
            "Why Union Territories exist and how Part VIII classifies them",
            "ut-rationale-classification",
            [1, 2, 3, 4, 5],
            """CONSTITUTIONAL LOCATION
Article 1 -> States and Union Territories form the territory of India.
Part VIII -> Articles 239-241; related Articles 239A, 239AA, 239AB and 240.

RATIONALES
small size | strategic frontier/islands | national capital
| cultural/administrative history | transitional reorganisation.

CURRENT EIGHT
Andaman and Nicobar Islands | Chandigarh
| Dadra and Nagar Haveli and Daman and Diu | Delhi
| Jammu and Kashmir | Ladakh | Lakshadweep | Puducherry.

CLASSIFICATION
with legislature: Delhi, Puducherry, J&K
without legislature: the other five.

CORE IDEA one constitutional label contains deliberately unequal governance models.""",
        ),
        (
            "President, Administrator and Parliament in the UT administration chain",
            "ut-administration-chain",
            [6, 7, 8, 9, 10, 11, 12],
            """ARTICLE 239
President administers UT through an appointed Administrator
unless the Constitution or parliamentary law creates another arrangement.

ADMINISTRATOR / LIEUTENANT GOVERNOR
designation does not convert the office into a Part VI State Governor.
power depends on the exact Constitution, statute and rules.

PARLIAMENT
may legislate for any UT, including matters otherwise in the State List.

UT WITH LEGISLATURE
local Assembly + Council of Ministers operate only inside the allotted field.
Parliament retains overriding legislative competence.

ARTICLE 239A
Parliament may create Puducherry legislature/CoM by law.
ARTICLE 239B -> Administrator ordinance within the statutory legislature model.""",
        ),
        (
            "Article 240 regulations, High Courts, budgets and representation",
            "ut-law-finance-justice-map",
            [13, 14, 15, 16, 17, 18, 19, 20, 21],
            """ARTICLE 240
President may make regulations for listed UTs; a regulation can amend/repeal Acts.
Its availability changes when a qualifying legislature is functioning.

ARTICLE 241
Parliament may constitute a High Court for a UT or extend another High Court's jurisdiction.

JUDICIAL MAP
Delhi has its High Court | J&K and Ladakh share one High Court
| other UTs use constitutionally/statutorily assigned High Courts.

BUDGET AND REPRESENTATION
legislature UTs have statutory/constitutional budget procedures.
Parliamentary representation follows the Constitution and representation statutes.

LIMIT direct Union administration does not mean absence of courts, elected MPs or local bodies.""",
        ),
        (
            "Delhi Article 239AA: elected government inside reserved-field asymmetry",
            "delhi-239aa-competence-map",
            [22, 23, 24, 25, 26],
            """ARTICLE 239AA
NCT Assembly may legislate on State/Concurrent matters
EXCEPT public order, police and land, plus related entries.

EXECUTIVE POWER
normally co-extensive with the allotted legislative field.
Council of Ministers aids and advises LG within that field.

REFERENCE MECHANISM
LG difference route is exceptional and must not convert "any matter" into "every matter".

PARLIAMENTARY OVERRIDE
Parliament may legislate for Delhi on any subject; inconsistent local law yields as provided.

NCT IS NOT A STATE
representative government is constitutionally real but operates inside Union-capital safeguards.""",
        ),
        (
            "Delhi cases, services and the operative 2023 statutory layer",
            "delhi-case-law-current-control",
            [27, 28, 29, 30],
            """            GNCTD aid-and-advice judgment (2018)
aid/advice is the rule within Delhi's field; LG has no general independent power.

Delhi services judgment (2023)
Entry 41 services followed the representative-accountability chain
outside public order, police and land.

GNCTD AMENDMENT ACT, 2023
National Capital Civil Service Authority -> recommendation
-> LG may differ and has the statutory final decision on disagreement.

CURRENT CONTROL: 24 AUGUST 2026
the Act is treated as operative; a pending challenge is not a final invalidation.

ANSWER RULE
state the 2018 principle -> 2023 services holding -> later statute -> pending-review caveat.""",
        ),
        (
            "Puducherry under Article 239A and its nominated-member design",
            "puducherry-statutory-model",
            [31, 32, 33],
            """ARTICLE 239A + GOVERNMENT OF UNION TERRITORIES ACT, 1963
statutory Assembly + Council of Ministers + Administrator.

LEGISLATIVE FIELD
defined by parliamentary law; Parliament retains UT-wide competence.

K. Lakshminarayanan (2018)
upheld Central nomination of Assembly members under the governing statute.
Nominees may vote unless the law provides otherwise.

ARTICLE 240
presidential-regulation power is unavailable while the legislature operates
and may revive during dissolution/suspension under the constitutional text.

LIMIT Puducherry is not Delhi: Article 239A statutory design != Article 239AA NCT design.""",
        ),
        (
            "Jammu and Kashmir, Ladakh and the present statutory position",
            "jk-ladakh-current-ut-map",
            [34, 35, 36, 37],
            """J&K REORGANISATION ACT, 2019
former State -> J&K UT with legislature + Ladakh UT without legislature
from 31 October 2019.

J&K ASSEMBLY
statutory legislative field and LG relationship follow the 2019 Act and rules.
Police and public order remain outside the Assembly's ordinary field.

In Re: Article 370 of the Constitution (2023)
upheld the operative abrogation result; recorded Statehood assurance
and did not set a judicial restoration date.

CURRENT: 24 AUGUST 2026
J&K Statehood not restored | Ladakh has no legislature.
Demands for Sixth Schedule/Statehood/special provisions are proposals, not law.""",
        ),
        (
            "Bounded UT profiles and State-UT-NCT comparison",
            "ut-profile-comparison-matrix",
            [16, 17, 18, 19, 20, 21, 22, 38, 39, 40],
            """WITHOUT LEGISLATURE
Andaman and Nicobar -> strategic archipelago
Lakshadweep -> small island UT
Chandigarh -> capital of Punjab and Haryana
DNHDD -> merged western UT
Ladakh -> frontier UT after 2019 reorganisation.

STATE                     ORDINARY UT               DELHI NCT
Part VI government        Article 239 chain         Article 239AA elected design
State-list autonomy       Parliament plenary        three reserved fields
Governor/CoM model        Administrator              LG + CoM + reference route

ACCOUNTABILITY TEST
exact field -> decision-maker -> override -> finance/staff -> court remedy.

LIMIT Administrator powers are UT-specific; title alone supplies no common rule.""",
        ),
        (
            "Creation, reorganisation, current traps and qualified answer synthesis",
            "ut-reorganisation-answer-spine",
            [41, 42, 43, 44],
            """CREATION / MERGER
Articles 2-4 and parliamentary reorganisation law can alter territory and status.
UT status is constitutional-administrative design, not a permanently fixed category.

PRELIMS FIREWALL
Article 239 = presidential administration
| 239A Puducherry enabling route | 239AA Delhi
| 239AB Delhi constitutional breakdown | 240 listed-UT regulations
| 241 High Courts | Parliament can legislate on State List for UTs.

CURRENT FIREWALL
operative statute != pending challenge outcome
| political proposal != law | office/status facts require a date.

MAINS SPINE
rationale -> classify UT -> exact Article/statute -> democratic mechanism
-> Union safeguard -> friction -> case-year control -> calibrated reform/verdict.""",
        ),
    ],
    "polity-26": [
        (
            "Article 244 starting point and the autonomy-development rationale",
            "tribal-area-root-map",
            [1, 2, 3, 4],
            """ROOT PROBLEM
ordinary territorial administration may reproduce dispossession and weak bargaining power.

ARTICLE 244(1)
Fifth Schedule -> Scheduled Areas and Scheduled Tribes outside the Sixth Schedule map.

ARTICLE 244(2)
Sixth Schedule -> tribal areas in Assam, Meghalaya, Tripura and Mizoram.

ARTICLE 244A
Parliament may create an autonomous State within Assam with legislature/CoM.

TERMS
Scheduled Tribe = Article 342 community status
| Scheduled Area = presidential territorial declaration
| tribal area = Sixth Schedule territorial unit.

CORE IDEA differentiated institutions pursue substantive equality within one Constitution.""",
        ),
        (
            "Fifth Schedule: declaration, Governor, TAC and regulation chain",
            "fifth-schedule-governance-chain",
            [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17],
            """SCHEDULED AREA
President declares, enlarges, diminishes or alters after the constitutional consultation route.

EXECUTIVE CHAIN
State executive applies -> Governor reports annually/when required to President
-> Union may issue directions on administration.

TRIBES ADVISORY COUNCIL
up to 20 members; as nearly as may be three-fourths ST legislators in the State.
advises on ST welfare/advancement matters referred by Governor.

GOVERNOR'S REGULATION
peace and good government -> restrict/prohibit tribal land transfer
-> regulate allotment -> regulate money-lending
-> may amend State/Parliament law for the area.

CHECK
regulation requires Presidential assent; personal-discretion claims need exact authority.""",
        ),
        (
            "Sixth Schedule territory, council composition and four-State scope",
            "sixth-schedule-institution-map",
            [18, 19, 20, 21, 22, 23],
            """SCOPE
Assam | Meghalaya | Tripura | Mizoram only.

AUTONOMOUS DISTRICT
Governor organises territory; multiple tribes may form autonomous regions.

ORDINARY DISTRICT COUNCIL MODEL
not more than 30 members -> up to four nominated by Governor
-> remainder elected by adult suffrage -> normally five-year elected term.

REGIONAL COUNCIL
created for an autonomous region; powers follow the Schedule and applicable rules.

ASSAM VARIATION
special paragraphs/statutes/accord implementation may modify composition and powers.

LIMIT ADC != State, municipality, ordinary Panchayat or Article 244A autonomous State.""",
        ),
        (
            "Sixth Schedule legislative, executive, judicial and fiscal powers",
            "adc-powers-and-checks",
            [24, 25, 26, 27, 28, 29, 30, 31, 32],
            """LEGISLATIVE
land other than reserved forest | non-reserved forest | shifting cultivation
| village administration | inheritance | marriage/divorce | social customs.
Governor assent is required for council laws.

EXECUTIVE
primary schools, dispensaries, markets, roads and specified local services.

JUDICIAL
village courts/council courts for specified tribal-party disputes
subject to constitutional/statutory supervision and jurisdiction rules.

FISCAL
District/Regional Funds | land revenue | listed taxes/fees | mineral-royalty share.

CHECKS
Governor territorial and suspension/dissolution powers
| Parliament/State-law application controls | audit and judicial review.

LIMIT autonomy is substantial but enumerated and supervised, not sovereignty.""",
        ),
        (
            "Fifth and Sixth Schedules: complete close-option comparison",
            "fifth-sixth-comparison-matrix",
            [33, 34],
            """DIMENSION          FIFTH SCHEDULE             SIXTH SCHEDULE
States             multiple notified States      Assam/Meghalaya/Tripura/Mizoram
territory          Scheduled Area                 autonomous district/region
core body          Governor + TAC                 elected District/Regional Council
law mechanism      Governor regulation            council law + Governor assent
judicial power     no Schedule-created ADC courts council/village courts in listed field
finance            State/Union channels           own funds + listed taxes/royalty share
local democracy    PESA in covered areas           council system; Part IX ordinarily excluded

COMMON PURPOSE
land/custom protection + self-government + development administration.

TRAP
TAC is advisory, not an ADC | Sixth Schedule does not cover every North-Eastern State.""",
        ),
        (
            "PESA, FRA, land and resource rights with judicial boundaries",
            "pesa-fra-resource-rights-map",
            [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
            """PESA, 1996
Part IX extension to Fifth Schedule areas -> customary village/Gram Sabha
-> plans/resources/markets/land safeguards through exact statutory verbs.

FRA, 2006
individual/community forest rights + community forest-resource governance
through its own claim and recognition procedure.

LAND / MINING CHAIN
territorial law -> land-transfer rule -> PESA role -> FRA rights
-> forest/environment clearance -> rehabilitation -> judicial review.

Samatha (1997)
protected Scheduled-Area land under the applicable Andhra Pradesh regime;
not a detached nationwide mining ban.

Orissa Mining Corporation (2013)
Gram Sabhas determined specified FRA religious/community-right claims at Niyamgiri;
not an unlimited veto over every project.""",
        ),
        (
            "Scheduled Tribe safeguards beyond territorial autonomy",
            "st-safeguards-constitutional-network",
            [15, 16, 56],
            """RIGHTS AND REPRESENTATION
Article 46 -> education/economic interests and protection from exploitation.
Articles 330/332 -> ST political reservation in Lok Sabha/State Assemblies.
Article 335 -> service claims consistent with administrative efficiency.

FINANCE AND OVERSIGHT
Article 275(1) -> specified grants
| Article 338A -> National Commission for Scheduled Tribes
| Article 339 -> commission and Union welfare-scheme directions.

NCST ROLE
monitor safeguards -> inquire into complaints -> advise planning
-> report to President -> recommendations and follow-up.

BOUNDARY
NCST does not replace Governor/TAC, Gram Sabha, ADC, courts or elected governments.""",
        ),
        (
            "Article 371, ordinary Panchayats, autonomous councils and proposal control",
            "tribal-institution-boundary-map",
            [34, 47, 48, 49, 50, 51, 52],
            """DO NOT COLLAPSE FOUR SYSTEMS
Article 371A/371G -> State-specific Part XXI consent shields.
Fifth Schedule -> Governor/TAC administration for Scheduled Areas.
Sixth Schedule -> autonomous district/regional councils in four States.
ordinary Part IX -> Panchayats outside exclusions; PESA modifies Fifth Schedule route.

ACCOUNTABILITY TENSIONS
autonomy vs elite capture | custom vs individual rights
| development vs land/resource security | Governor oversight vs elected legitimacy.

CURRENT CONTROL
Ladakh or other demands for Sixth Schedule/Statehood/Article 371 safeguards
remain proposals until the Constitution or law is validly changed.

REFORM
clear jurisdiction + audited funds + accessible laws + women/community voice
-> transparent Governor action + timely rights recognition.""",
        ),
        (
            "Prelims firewalls, Mains architecture and qualified tribal-governance synthesis",
            "tribal-areas-answer-synthesis",
            [53, 54, 55],
            """PRELIMS FIREWALL
President declares Scheduled Areas | Governor makes Fifth Schedule regulations
| President assents | TAC advisory | ADC laws need Governor assent
| reserved forest excluded from listed ADC forest power
| Article 244A applies only within Assam.

PYQ ROUTES
Fifth/Sixth identification | council composition/powers
| PESA verbs | FRA relationship | Article 275/339 | land/mining case limits.

MAINS SPINE
define differentiated autonomy -> identify territory -> map institution/power
-> rights/development purpose -> accountability risk -> named case with limit
-> reform through voice, legality, capacity and audit.

SYNTHESIS
autonomy earns legitimacy when it protects land and custom while remaining inclusive,
reviewable, fiscally accountable and capable of delivering development.""",
        ),
    ],
    "polity-27": [
        (
            "Article 324 constitutional position and collegial Election Commission",
            "eci-constitutional-architecture",
            [1, 2, 3, 4, 5, 6, 7, 8],
            """ARTICLE 324
superintendence, direction and control of rolls and elections to
Parliament | State legislatures | President | Vice-President.

COMPOSITION
CEC + such number of Election Commissioners as President fixes.
President may appoint Regional Commissioners after consulting the ECI.

COLLEGIALITY
multi-member Commission decides by majority under the governing statute.

EXCLUSION
local-body elections -> State Election Commissions under Articles 243K and 243ZA.

CONSTITUTIONAL POSITION
independent election manager + distributed field machinery
bounded by Constitution, enacted law, natural justice and judicial review.""",
        ),
        (
            "Appointment Act, tenure, removal and independence safeguards",
            "eci-appointment-independence-map",
            [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            """Anoop Baranwal (2023)
interim PM + Opposition leader + CJI committee only until Parliament made a law.

2023 APPOINTMENT ACT
Search Committee led by Law Minister -> panel of five
-> Selection Committee: PM + Union Cabinet Minister + Opposition leader
-> President appoints.

TERM
six years or age 65, whichever earlier; no reappointment under the Act.

REMOVAL
CEC -> like Supreme Court judge.
EC/Regional Commissioner -> President only on CEC recommendation.

CURRENT LEGAL CONTROL: 24 AUGUST 2026
Act operates; challenge pending; no claim of final validation or invalidation.

INDEPENDENCE TEST
appointment + removal + finance + secretariat + staff + transparent reasons.""",
        ),
        (
            "Election administration from schedule and rolls to repoll",
            "election-administration-chain",
            [20, 21, 22, 23, 24, 27, 28, 29, 30, 31, 32],
            """ADMINISTRATIVE CHAIN
roll revision -> schedule announcement -> statutory notification
-> nomination -> scrutiny -> withdrawal -> campaign
-> poll -> count -> result -> election-petition route.

ROLLS
citizenship + qualifying age + ordinary residence + inclusion/deletion due process.

FIELD CONTROL
Returning Officers | observers | security coordination | expenditure teams.

URGENT INTEGRITY POWER
adjournment, repoll or countermand only through the applicable legal basis and facts.

DISQUALIFICATION ADVICE
President under Article 103 and Governor under Article 192 obtain ECI opinion.
Tenth Schedule disqualification belongs to Speaker/Chairman, not ECI.""",
        ),
        (
            "RPA interface, delimitation boundary, voter registration and NOTA",
            "rpa-delimitation-nota-map",
            [22, 23, 25, 26, 27, 45, 47, 48],
            """RPA 1950
seat allocation/delimitation framework + electoral rolls + eligibility architecture.

RPA 1951
conduct, candidates, expenses, corrupt practices, disqualifications and petitions.

DELIMITATION
Delimitation Commission is the statutory authority when constituted;
CEC/ECI participates as law provides but is not the ordinary sole delimiting body.

People's Union for Civil Liberties (2013)
secret NOTA protects voter expression and secrecy.

NOTA LIMIT
NOTA plurality does not automatically cancel the election or force a repoll.

ARTICLE 329
electoral process receives anti-interruption protection; post-result petition remains available.""",
        ),
        (
            "Political parties, symbols and Model Code enforcement",
            "party-symbol-mcc-system",
            [33, 34, 35, 36, 37, 38],
            """PARTY REGISTRATION
RPA 1951 section 29A -> registration.

RECOGNITION / SYMBOL
Symbols Order, 1968 -> national/State recognition, reserved/free symbols
and quasi-judicial symbol disputes.

MODEL CODE OF CONDUCT
consensus-based non-statutory code -> operates from election-schedule announcement
until completion -> rapid preventive correction and level-playing-field control.

LEGAL OVERLAP
bribery, communal appeals, expenditure and other conduct may independently violate law.

LIMITS
registration != recognition | symbol jurisdiction != every internal party dispute
| MCC is not by itself a complete penal code.""",
        ),
        (
            "Campaign finance, criminalisation, paid news and social-media limits",
            "campaign-integrity-risk-map",
            [30, 46, 49, 50, 51, 61],
            """CAMPAIGN FINANCE
candidate account + statutory ceiling + observers/teams
!= one identical ceiling for total political-party campaign spending.

CRIMINALISATION
candidate affidavit disclosure + RPA disqualification + court process.
ECI cannot invent new conviction or disqualification grounds.

PAID NEWS
media monitoring -> evidence -> expense attribution or legal route where supported.

SOCIAL MEDIA / DEEPFAKES
ad certification + MCC/advisories + applicable election/criminal/technology law.
ECI is not a general platform regulator or universal censor.

TRANSPARENCY
Union of India v. Association for Democratic Reforms (2002)
-> voter right to candidate information.

REFORM TEST
clear law + reasons + equal enforcement + rapid remedy + audit trail.""",
        ),
        (
            "EVM-VVPAT architecture and current judicial controls",
            "evm-vvpat-trust-chain",
            [39, 40, 41, 56],
            """POLLING CHAIN
Ballot Unit -> Control Unit -> VVPAT slip display/drop -> sealed records -> counting protocol.

VVPAT PURPOSE
voter-verifiable paper audit trail, not a take-home ballot.

Association for Democratic Reforms v. Election Commission of India (2024)
rejected paper-ballot return and universal 100% VVPAT counting;
added limited post-result technical safeguards.

2025 FOLLOW-UP
candidate-requested diagnostic/check process operates within the Court's stated protocol.

ANSWER DISCIPLINE
device security + roll accuracy + staff neutrality + campaign fairness
-> transparent audit + reasoned judicial/administrative safeguards.

LIMIT unsupported fraud claims and unsupported infallibility claims are both exam-unsafe.""",
        ),
        (
            "Article 324 case-law code: power, law, collegiality and rights",
            "eci-case-law-doctrine-matrix",
            [42, 43, 44, 45, 46, 47],
            """Mohinder Singh Gill (1977)
Article 324 is a reservoir where law is silent; it cannot override enacted law.

A.C. Jose (1984)
ECI fills gaps but cannot act contrary to a field occupied by legislation/rules.

T.N. Seshan (1995)
multi-member Commission and equal decision-making status are constitutionally valid.

Union of India v. Association for Democratic Reforms (2002)
candidate disclosure serves the voter's Article 19(1)(a) right.

People's Union for Civil Liberties (2013)
secret NOTA protects expression; it is not a binding reject option.

Anoop Baranwal (2023) -> temporary appointment rule until legislation.
The VVPAT ruling is separately controlled by its full 2024 case label in Stage 06.""",
        ),
        (
            "ECI-SEC boundary, reform priorities, traps and final answer spine",
            "eci-reform-answer-synthesis",
            [4, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60],
            """ECI                                  STATE ELECTION COMMISSION
Parliament/State legislature/P/VP     Panchayat and municipal elections
Article 324                           Articles 243K and 243ZA
national election statutes            State local-government election law.

PRELIMS FIREWALL
CEC removal != EC removal | ECI advice != Tenth Schedule decision
| ECI assists delimitation != sole delimiting authority
| party registration != recognition | NOTA != automatic repoll.

REFORM
credible plural appointment + stable secretariat/finance
-> equal collegial security with accountability -> transparent complaint orders
-> cleaner rolls -> faster disputes -> audited technology and campaign enforcement.

MAINS SPINE
Article 324 purpose -> power/function -> legal boundary -> case-year
-> independence deficit -> accountable reform -> trust-ecosystem verdict.""",
        ),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def _optional_owner(config: dict[str, Any]) -> str:
    path = ROOT / Path(config["advanced"].replace("\\", "/"))
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            text = text[end + 5 :]
    text = re.sub(r"(?m)^#(?!#)\s+.+$\n?", "", text, count=1)

    def demote(match: re.Match[str]) -> str:
        level = len(match.group(1))
        return "#" * min(6, level + 2) + " "

    text = re.sub(r"(?m)^(#{1,4})\s+", demote, text).strip()
    return case_years.normalize_text(config["key"], text)


def _normalize_control_date(text: str) -> str:
    text = re.sub(
        r"(?m)^export_date:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"export_date: {DATE}",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^control_date:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"control_date: {DATE}",
        text,
        count=1,
    )
    text = re.sub(
        r"(?mi)(\*\*(?:Export date|Control date):\*\*\s*)"
        r"(?:\d{4}-\d{2}-\d{2}|\d{1,2}\s+August\s+2026(?:,\s*Asia/Kolkata)?)",
        rf"\g<1>{DATE}",
        text,
    )
    text = re.sub(
        r"(?mi)^- \[CURRENT\] .{0,80}?status is controlled to "
        r"\*\*\d{1,2} August 2026, Asia/Kolkata\*\*\.\s*$",
        "- [CURRENT] Status is controlled to **24 August 2026, Asia/Kolkata**.",
        text,
        count=1,
    )
    text = text.replace(
        "as of 18 August 2026",
        "as of 24 August 2026",
    ).replace(
        "as of 19 August 2026",
        "as of 24 August 2026",
    )
    return text


def transform_source(config: dict[str, Any]) -> Path:
    canonical = ROOT / Path(config["canonical"].replace("\\", "/"))
    text = _normalize_control_date(
        canonical.read_text(encoding="utf-8").replace("\r\n", "\n")
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
    anchor = (
        f"- [CURRENT] **Live official refresh, 24 August 2026:** "
        f"{config['current_note']}"
    )
    if "Status is controlled to **24 August 2026, Asia/Kolkata**." not in text:
        heading = re.search(r"(?m)^## Package method[^\n]*$", text)
        if not heading:
            raise RuntimeError(f"{config['key']}: package-method heading missing.")
        insertion = text.find("\n", heading.end()) + 1
        text = text[:insertion] + "\n- [CURRENT] Status is controlled to **24 August 2026, Asia/Kolkata**.\n" + text[insertion:]
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
            r"^Solved UPSC PYQs",
        ],
    )
    final = base.start_for(headings, [r"^Final consolidated register notes$"])

    supplement = SUPPLEMENTS.get(config["key"], "").strip()
    if supplement:
        text = text[:practice].rstrip() + "\n\n" + supplement + "\n\n" + text[practice:]
        headings = base.heading_offsets(text)
        part_i = base.start_for(headings, [r"^PART I\b"])
        practice = base.start_for(
            [(offset, title) for offset, title in headings if offset > part_i],
            [
                r"PYQ, practice and solved workbook",
                r"^Solved topic-specific MCQs$",
                r"^Verified routed",
                r"^Routed PYQs",
                r"^Solved UPSC PYQs",
            ],
        )
        final = base.start_for(headings, [r"^Final consolidated register notes$"])

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
            r"^Solved UPSC PYQs",
        ],
    )
    final = base.start_for(headings, [r"^Final consolidated register notes$"])

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
    pyq_start = base.start_for(
        practice_headings,
        [
            r"^Routed PYQs",
            r"^Solved UPSC PYQs",
            r"^Verified routed",
            r"^Solved directly routed Mains PYQs",
            r"^(?:Solved|Verified).*\bPYQ",
        ],
    )
    mcq_start = base.start_for(
        practice_headings,
        [r"^Original hard MCQ", r"^Original MCQ loop"],
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
            _optional_owner(config),
            "## CONSOLIDATED REGISTER NOTES",
            register,
        ]
    ) + "\n"
    output = base.SOURCE_SESSION_ROOT / f"{config['key']}_Learning-Session.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8")
    return output


def augment_audit(config: dict[str, Any], audit_path: Path) -> None:
    payload = json.loads(audit_path.read_text(encoding="utf-8"))
    payload["topic_completeness_contract"] = config["coverage_contract"]
    payload["topic_completeness_status"] = "passed"
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
    audit_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run() -> dict[str, Any]:
    expected_order = [f"polity-{number:02d}" for number in range(23, 28)]
    if [config["key"] for config in TOPICS] != expected_order:
        raise RuntimeError("Sequential topic order was altered.")
    base.PANELS.update(PANELS)

    clean_baseline = prior.topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={23, 24, 25, 26, 27},
    )
    flow_baseline = prior.flow_topic_hashes(exclude_polity={23, 24, 25, 26, 27})
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        resumed = prior.completed_result(config)
        if resumed is not None:
            result, clean_folder, flow_folder = resumed
            results.append(result)
            locked_new.update(prior.lock_hashes([clean_folder, flow_folder]))
            continue
        if prior.compare_hashes(
            locked_new,
            {key: prior.sha256(ROOT / key) for key in locked_new},
        ):
            raise RuntimeError("Previously generated topic artifacts changed before next gate.")

        gate_times: dict[str, str] = {"A_started": now()}
        live = base.live_checks(config)
        audit = base.write_audit(config, gate_times["A_started"], live)
        augment_audit(config, audit)
        gate_times["A_completed"] = now()

        source_markdown = transform_source(config)
        gate_times["B_completed"] = now()

        workbook_authored = prior.workbook_gate(source_markdown)
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
        prior.case_year_gate(config, ascii_path, graph_path)
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

        record = prior.latest_record(config)
        gate_times["G_completed"] = now()

        base.export_clean_topic(config)
        clean_folder = base.verify_four_folders(config)
        gate_times["H_completed"] = now()

        flow_validation, flow_row = prior.export_flow(config, 55 + index)
        flow_folder = ROOT / Path(flow_row["destination_folder"].replace("\\", "/"))
        gate_times["I_completed"] = now()

        clean_mismatches = prior.compare_hashes(
            clean_baseline,
            prior.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={23, 24, 25, 26, 27},
            ),
        )
        flow_mismatches = prior.compare_hashes(
            flow_baseline,
            prior.flow_topic_hashes(exclude_polity={23, 24, 25, 26, 27}),
        )
        if clean_mismatches or flow_mismatches:
            raise RuntimeError(
                f"{config['key']}: preservation regression: "
                f"clean={clean_mismatches[:5]} flow={flow_mismatches[:5]}"
            )
        prior_mismatches = prior.compare_hashes(
            locked_new,
            {key: prior.sha256(ROOT / key) for key in locked_new},
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
                "original_mains": base.count_original_mains(final_markdown_path),
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
        locked_new.update(prior.lock_hashes([clean_folder, flow_folder]))

    state = {
        "schema_version": 1,
        "batch_id": BATCH_ID,
        "created_at": now(),
        "strict_order": expected_order,
        "topics": results,
        "existing_clean_topic_artifact_count": len(clean_baseline),
        "existing_flow_topic_artifact_count": len(flow_baseline),
        "existing_clean_hash_mismatches": prior.compare_hashes(
            clean_baseline,
            prior.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={23, 24, 25, 26, 27},
            ),
        ),
        "existing_flow_hash_mismatches": prior.compare_hashes(
            flow_baseline,
            prior.flow_topic_hashes(exclude_polity={23, 24, 25, 26, 27}),
        ),
        "prior_generated_topic_hash_mismatches": prior.compare_hashes(
            locked_new,
            {key: prior.sha256(ROOT / key) for key in locked_new},
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
