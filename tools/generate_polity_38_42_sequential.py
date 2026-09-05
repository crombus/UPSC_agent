"""Generate Polity learner-v2 topics 38-42 in strict preservation-safe order."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_33_37_sequential as prior


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
BATCH_ID = "polity-38-42-sequential-batch-2026-08-25"

# The generalized helpers are date-driven globals in the original sequential tool.
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
        "polity-38",
        "Lokpal and Lokayuktas",
        "upsc-ai-kit\\knowledge\\Polity\\38_Lokpal-and-Lokayuktas_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Lokpal-and-Lokayuktas.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\38_Lokpal-and-Lokayuktas.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CVC-and-CBI.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\20_Anti-Corruption-Institutions.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\21_Protecting-Honest-Officials-and-Vigilance-Administration.md",
        ],
        [
            "https://lokpal.gov.in/",
            "https://dopt.gov.in/",
            "https://www.indiacode.nic.in/",
            "https://api.sci.gov.in/jonew/judis/44396.pdf",
        ],
        1,
        0,
        "The current Lokpal Act framework, Complaint Rules, official Lokpal "
        "circular/wing material, DoPT asset-declaration position and controlling "
        "Supreme Court decisions were rechecked on 25 August 2026. The 2025 "
        "High Court-judge jurisdiction order remains stayed; officeholders and "
        "case-output totals are not frozen.",
        "Lokpal is a statutory corruption-complaint institution, not a general "
        "grievance body, police force or criminal court. The Prime Minister is "
        "covered through special filters; parliamentary speech/vote protection, "
        "agency dependence, State-law Lokayukta variation and pending litigation "
        "must remain expressly qualified.",
        [
            "ombudsman evolution, 2013 Act, amendments, rules and statutory identity",
            "composition, selection/search, eligibility, tenure, removal and suspension",
            "PM safeguards, Ministers, MPs, officials, entities and privilege exclusions",
            "complaint, inquiry, investigation, sanction, prosecution and Special Courts",
            "Inquiry/Prosecution Wings and bounded Lokpal-CVC-CBI superintendence",
            "assets, powers, timelines, limitation, whistleblower and vigilance interfaces",
            "State-law Lokayukta diversity, cases, capacity limits, reforms and traps",
        ],
        visual_sessions=[1, 2, 3, 4, 6, 9, 10, 13, 14, 16, 17, 18, 21, 23, 25, 27, 30],
    ),
    topic(
        "polity-39",
        "Cooperative Societies",
        "upsc-ai-kit\\knowledge\\Polity\\39_Cooperative-Societies_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Cooperative-Societies.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\39_Cooperative-Societies.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
        ],
        [
            "https://www.cooperation.gov.in/",
            "https://crcs.gov.in/",
            "https://www.rbi.org.in/",
            "https://www.nabard.org/",
        ],
        0,
        3,
        "The official Constitution, Rajendra N. Shah judgment, current Multi-State "
        "Co-operative Societies Act and 2023 amendment framework, Ministry/CRCS, "
        "RBI and NABARD material were rechecked on 25 August 2026. National "
        "Cooperation Policy 2025 is a dated policy anchor, not a transfer of State "
        "legislative competence.",
        "After Rajendra N. Shah, Part IXB cannot be written as a uniform binding "
        "code for ordinary State-field cooperatives. Article 19(1)(c), Article "
        "43B and the valid multi-State field survive; Ministry, Registrar, "
        "financing, representative and operating cooperative bodies remain "
        "legally distinct.",
        [
            "principles, evolution, economic functions and cooperative enterprise identity",
            "97th Amendment triptych and Rajendra N. Shah's exact surviving scope",
            "Articles 243ZH-243ZT with boards, elections, supersession, audit and returns",
            "State cooperative law versus Entry 44 multi-State cooperative law",
            "MSCS Act 2002 and authoritative 2023 amendment mechanisms",
            "Ministry, CRCS, NCDC, representative bodies and operating societies distinguished",
            "banking overlays, examples, governance failure, professionalisation and traps",
        ],
        visual_sessions=[1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18],
    ),
    topic(
        "polity-40",
        "Official Language",
        "upsc-ai-kit\\knowledge\\Polity\\40_Official-Language_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Official-Language.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\40_Official-Language.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
        ],
        [
            "https://samiti.rajbhasha.gov.in/",
            "https://www.pib.gov.in/",
            "https://rajbhasha.gov.in/",
            "https://legislative.gov.in/",
        ],
        1,
        0,
        "The Constitution as on 1 May 2026, Official Languages Act and Rules, "
        "Committee portal, Eighth Schedule and official classical-language "
        "material were rechecked on 25 August 2026. The Constitution still lists "
        "22 scheduled languages; October 2024 classical recognition remains a "
        "separate executive-status anchor.",
        "India has an official-language settlement, not a constitutionally "
        "declared national language. English continuation is statutory; State, "
        "court, grievance, minority-instruction, scheduled, classical and "
        "education-policy categories must not be collapsed.",
        [
            "Part XVII Articles 343-351 and official-versus-national distinction",
            "Article 344 commission/committee and 1963 Act continuation of English",
            "State languages, intergovernmental communication and Article 347 route",
            "Article 348 court proceedings, judgments and authoritative translations",
            "Articles 350, 350A, 350B and 351 safeguards and development directive",
            "Eighth Schedule, 22 languages, classical status and three-language policy",
            "language cases, federalism, access, technology, reforms and exact traps",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 16, 18, 19, 21, 25],
    ),
    topic(
        "polity-41",
        "Public Services",
        "upsc-ai-kit\\knowledge\\Polity\\41_Public-Services_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\41_Public-Services.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\UPSC-and-SPSC.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CVC-and-CBI.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\09_Civil-Services-and-Mission-Karmayogi.md",
            "upsc-ai-kit\\knowledge\\Ethics\\basic\\09_Public-Service-Values-Status-and-Ethical-Dilemmas.md",
        ],
        [
            "https://dopt.gov.in/",
            "https://igotkarmayogi.gov.in/",
            "https://cgat.gov.in/",
            "https://legislative.gov.in/",
        ],
        0,
        1,
        "Part XIV, current DoPT service-rule material, Mission Karmayogi/iGOT, "
        "tribunal and civil-service reform sources were rechecked on 25 August "
        "2026. Mission/training architecture is a dated implementation anchor; "
        "vacancies, lateral-entry advertisements and dashboard counts are not frozen.",
        "Public Services owns the service relationship under Articles 308-314, "
        "not the separate PSC institutional topic. Pleasure is constitutionally "
        "fettered; Article 311 is a procedural shield, not immunity; public-sector, "
        "contractual, constitutional-office and civil-post categories require "
        "separate legal tests.",
        [
            "canonical scope under Articles 308-314 distinct from PSC institutions",
            "Article 309 rule authority and Article 310 doctrine of pleasure",
            "Article 311 inquiry, penalties, natural justice and three exceptions",
            "civil post, office under State, body employment and contractual distinctions",
            "Article 312 All-India Services and federal dual-control design",
            "Article 335, neutrality, anonymity, accountability and ethics",
            "lateral entry, Mission Karmayogi, CAT interface, cases and reform",
        ],
        visual_sessions=[1, 3, 4, 5, 7, 9, 10, 12, 15, 16, 18, 21, 22, 25, 29, 36],
    ),
    topic(
        "polity-42",
        "Anti Defection Law",
        "upsc-ai-kit\\knowledge\\Polity\\42_Anti-Defection-Law_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\42_Anti-Defection-Law.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
        ],
        [
            "https://www.sci.gov.in/",
            "https://sansad.in/",
            "https://legislative.gov.in/",
            "https://eci.gov.in/",
        ],
        2,
        1,
        "The Constitution as on 1 May 2026, 52nd/91st Amendment texts, House "
        "procedure and controlling Supreme Court cases were rechecked on 25 "
        "August 2026. Nabam Rebia remains subject to the larger-bench reference; "
        "current party alignments and reported merger litigation are not frozen.",
        "The Tenth Schedule disqualifies specified conduct; it does not criminalise "
        "defection or make every dissenting speech a whip breach. Speaker delay, "
        "resignation, merger and party-identity disputes require chronology, "
        "natural justice, judicial review and pending-case qualifications.",
        [
            "defection history, 52nd/91st Amendments and complete Tenth Schedule map",
            "voluntary giving up, voting/abstention, independent and nominated members",
            "two-thirds merger exception, deleted split and paragraph 5 exemption",
            "presiding-officer jurisdiction, House rules, hearing and judicial review",
            "Articles 75(1B), 164(1B), 361B, resignation and disqualification effects",
            "Kihoto, Keisham, Nabam Rebia and Subhash Desai with pending qualification",
            "whip scope, comparisons, democratic trade-offs, proposals and traps",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16, 17, 19, 20, 23, 25],
    ),
]


SUPPLEMENTS: dict[str, str] = {
    "polity-38": r"""
## 30. Whistleblower, Vigilance and Grievance Interfaces

| Route | Entry condition | Principal output | Boundary |
|---|---|---|---|
| Lokpal | prescribed corruption complaint against a covered public servant | inquiry/investigation/prosecution route | not a general service grievance |
| CVC/CVO | vigilance information or departmental integrity issue | vigilance advice or disciplinary route | no criminal conviction |
| CBI/DSPE | notified offence and lawful territorial/jurisdictional route | criminal investigation report | guilt remains for court |
| whistleblower channel | protected disclosure under the applicable legal framework | identity protection and examination route | do not assume full commencement of every enactment |
| grievance portal | service-delivery complaint | administrative redress | not a substitute for corruption evidence |

[LIMIT] These routes may interact, but one filing does not automatically satisfy another
statute's form, jurisdiction, limitation, evidence or sanction requirements.
""",
    "polity-39": r"""
## 18. Ministry, Registrars and National Cooperative Bodies

| Institution type | Legal identity | Core role | What it is not |
|---|---|---|---|
| Ministry of Cooperation | Union executive department | policy and Union business allocation | Registrar for every society |
| Central Registrar | MSCS Act statutory authority | registration and statutory administration of MSCS | State cooperative regulator |
| State Registrar | authority under the applicable State Act | State-field society administration | MSCS-wide national authority |
| NCDC | statutory development-finance corporation | finance and development support under its Act | election or prudential regulator |
| NCUI/representative bodies | cooperative-sector representative/education bodies | advocacy, training and coordination | constitutional or statutory regulator merely by prominence |
| national multi-State cooperatives | registered operating societies | member-owned economic activity | Ministry, Registrar or sovereign authority |

[LIMIT] A national label, Union support or multi-State operation does not merge policy,
registration, finance, representation, ownership and prudential supervision into one office.
""",
    "polity-40": r"""
## 25. Judicial Doctrine: Language Choice, Minorities and Medium

| Decision | Exam-safe proposition | Qualification |
|---|---|---|
| Gujarat University v. Shri Krishna (1963) | education-language power operates within the Union-State legislative distribution | not an Article 343 national-language ruling |
| D.A.V. College v. State of Punjab (1971) | linguistic-minority and language safeguards require contextual constitutional analysis | scheduled status is not the sole test |
| State of Karnataka v. Associated Management (2014) | the State cannot impose a mother-tongue medium in a manner that violates protected choice | Article 350A still directs facilities at the primary stage |

[ANALYSIS] The cases show that language policy is controlled by competence, rights,
minority context and proportionality, not by a single hierarchy of "national" languages.
""",
    "polity-41": r"""
## 36. Article 335: Representation and Administrative Efficiency

[FACT] Article 335 requires the claims of Scheduled Castes and Scheduled Tribes to be
considered consistently with maintenance of efficiency of administration, subject to its
constitutional proviso concerning qualifying marks and standards for promotion.

[ANALYSIS] The provision is a reconciliation clause. It neither erases equality-based
reservation authority nor licenses an undefined efficiency veto. Recruitment rules,
constitutional amendments and controlling reservation doctrine must be read together.

## 37. Employment-Status Boundary

| Category | Governing question | Article 311 baseline |
|---|---|---|
| Union/State civil post | is there a civil post under the government? | may apply |
| All-India Service | is the person a member of an AIS? | applies |
| constitutional office | does the Constitution create a special tenure/removal code? | use that code first |
| statutory body employee | who is the legal employer and what does the statute provide? | not automatic |
| public-sector enterprise employee | corporation/service rules and public-law duties | not automatic |
| contractor/outsourced worker | contract, labour law and real-control facts | not automatic |
| lateral/short-term appointee | appointment mode, post and applicable rules | post-specific |

[LIMIT] "Public employment", "office under the State", "civil post" and employment by a
government-controlled company are related but non-identical constitutional categories.
""",
}


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-38": [
        (
            "Ombudsman evolution and the statutory anti-corruption design",
            "evolution-status-timeline",
            [1, 2],
            """ROOT QUESTION
How can high public office be investigated without merging complaint, police and court?

1809 Sweden -> ombudsman model.
1966 First ARC -> Union Lokpal + State Lokayuktas.
1968 onward -> repeated Bills.
2013 Act -> assent 1 January 2014 -> commencement 16 January 2014.

LEGAL IDENTITY
statutory | corruption-specific | Union institution | no general suo-motu route.

CORE DISTINCTION
Lokpal directs a legal process; the Special Court decides criminal guilt.""",
        ),
        (
            "Composition, selection, search, tenure and removal lifecycle",
            "appointment-lifecycle-matrix",
            [3, 4, 5, 6, 7],
            """COMPOSITION
Chairperson + not more than eight Members.
50% of Members judicial | at least 50% of Members from named social categories.

SELECTION COMMITTEE
PM | Lok Sabha Speaker | Lok Sabha LoP | CJI or nominee | eminent jurist.

SEARCH COMMITTEE
assists with a panel; it does not appoint and its panel is not the final decision.

TENURE
five years or age seventy, whichever earlier | no reappointment.

REMOVAL
President + Supreme Court inquiry for misbehaviour; statutory direct grounds are separate.

Common Cause v. Union of India
vacancy did not make the Act unworkable or create a substitute committee seat.""",
        ),
        (
            "Jurisdiction map: Prime Minister, MPs, officials and covered entities",
            "jurisdiction-ring-screen",
            [8, 9, 10, 11],
            """PERSONAL REACH
PM | Union Ministers | MPs | Groups A-D | specified financed/foreign-funded entities.

PM FILTER
excluded subjects: international relations | external/internal security | public order
| atomic energy | space.
Full bench + at least two-thirds approval | in-camera inquiry | record controls.

MP FIREWALL
speech or vote protected by Article 105(2) is outside the statutory route.

Sita Soren v. Union of India
legislative bribery is not constitutionally immunised merely because it relates to a vote.

TRAP
wide personal jurisdiction != unrestricted subject-matter jurisdiction.""",
        ),
        (
            "Complaint-to-trial chain with natural justice and statutory timelines",
            "complaint-process-rail",
            [12, 13, 14, 15, 16],
            """PRESCRIBED COMPLAINT
identity + form + allegation + supporting material -> Registry scrutiny.

LOKPAL CHOICE
preliminary inquiry | direct investigation | in-limine closure within legal bounds.

PRELIMINARY INQUIRY
prima facie screen -> public-servant hearing -> report ordinarily within ninety days
with recorded extension.

INVESTIGATION
evidence collection -> report ordinarily within six months with recorded extensions.

THREE-MEMBER BENCH
closure | departmental action | sanction/prosecution route.

END POINT
Prosecution Wing or agency -> Special Court -> conviction or acquittal.""",
        ),
        (
            "Wings, CVC, CBI and superintendence without institutional merger",
            "agency-relationship-grid",
            [17, 18, 22, 26],
            """INQUIRY WING
preliminary inquiry and prima facie assessment.

PROSECUTION WING
files and conducts prosecution when Lokpal directs.

CVC ROUTE
specified Groups A-D preliminary-inquiry categories under the statutory distribution.

CBI / DSPE ROUTE
criminal investigation; Lokpal superintendence is confined to Lokpal-referred matters.
Investigating-officer transfer in a referred matter needs Lokpal approval.

VIGILANCE / WHISTLEBLOWER / GRIEVANCE
distinct entry tests and outputs; no automatic jurisdictional substitution.

LIMIT
superintendence != power to dictate a predetermined investigative result.""",
        ),
        (
            "Powers, assets, limitation, attachment and Special Court control",
            "power-safeguard-board",
            [19, 20, 21],
            """PROCESS POWERS
search/seizure | civil-court powers | provisional attachment | prosecution sanction.

ATTACHMENT
recorded reasons + suspected corruption proceeds + maximum ninety-day provisional order
-> material sent to Special Court -> confirmation, refusal or later restoration.

SECTION 44
2016 substitution -> assets/liabilities in prescribed form and manner.
Checked official material did not yield a later fresh replacement form-and-manner rule.

LIMITATION
complaint barred after seven years from the alleged offence.

FALSE COMPLAINT
statutory safeguard requires legal proof; it must not deter bona fide disclosures.

Lok Prahari v. Union of India
electoral disclosure case; it did not restore the pre-2016 Lokpal return format.""",
        ),
        (
            "Lokayuktas: State-law variation inside a common federal objective",
            "federal-variation-comparison",
            [23],
            """SECTION 63
each State shall establish a Lokayukta by State law.

VARIATION AXES
single/member body | selection panel | tenure | jurisdiction | suo-motu power
| minister coverage | investigation support | recommendation/enforcement route.

DO NOT UNIVERSALISE
one State's Governor panel, age, term, Upalokayukta or report consequence.

FEDERAL GAIN
State adaptation and experimentation.

FEDERAL RISK
uneven minimum protection, vacancies and dependence on State agencies.

REFORM
model baseline + State autonomy + transparent appointments + public follow-up.""",
        ),
        (
            "Cases, independence deficits, accountability controls and reform priorities",
            "case-reform-balance-sheet",
            [24, 25],
            """CASE SPINE
Common Cause v. Union of India -> appointment cannot be blocked by committee vacancy.
Lok Prahari v. Union of India -> electoral disclosure, not section 44 rulemaking.
Sita Soren v. Union of India -> bribery outside legislative privilege immunity.

2025 HIGH COURT-JUDGE ISSUE
Supreme Court stay is interlocutory control; jurisdiction is not finally expanded.

INDEPENDENCE RISKS
executive weight in selection | vacancy | agency reliance | opaque closure | capacity gaps.

ACCOUNTABILITY CONTROLS
reasons | hearing | judicial review | Special Court | reports | removal safeguards.

REFORM
timely vacancies + clear section 44 rules + interoperable tracking + reasoned publication.""",
        ),
        (
            "UPSC traps, PYQ route and qualified answer synthesis",
            "exam-synthesis-ladder",
            [24, 25, 26],
            """PRELIMS FIREWALL
statutory, not constitutional | maximum eight Members | PM included with filters
| speech/vote exclusion | no general suo-motu power | seven-year limitation
| referred-case CBI superintendence only | Lokayukta design varies.

2025 PRELIMS ROUTE
jurisdiction + composition -> test percentage denominator, PM safeguards and privilege.

MAINS SPINE
ombudsman evolution -> legal identity -> composition/independence
-> jurisdiction -> complaint-to-court process -> agency interfaces
-> powers and safeguards -> State variation -> capacity reform.

VERDICT
Lokpal has real process powers, but credibility depends on appointments, agency autonomy,
reasoned transparency and court-controlled legality rather than institutional mythology.""",
        ),
    ],
    "polity-39": [
        (
            "Cooperative identity, principles, evolution and constitutional location",
            "principle-evolution-map",
            [1, 2, 3],
            """ROOT QUESTION
How can member-owned enterprise combine democratic control with commercial discipline?

CORE IDENTITY
voluntary association + member ownership + one-member democratic voice + shared benefit.

SEVEN PRINCIPLES
voluntary/open membership | democratic control | member economic participation
| autonomy | education | cooperation among cooperatives | community concern.

EVOLUTION
1904 credit law -> 1912 general law -> provincial/State field -> 97th Amendment.

FEDERAL LOCATION
Entry 32: State cooperatives | Entry 44: multi-State corporations | Entry 45: banking.

LIMIT
international principles guide interpretation; applicable Indian law controls outcomes.""",
        ),
        (
            "97th Amendment triptych and the Rajendra N. Shah federalism holding",
            "amendment-severance-triptych",
            [4, 5, 6],
            """97TH AMENDMENT
Article 19(1)(c) -> right to form cooperative societies.
Article 43B -> voluntary formation, autonomous functioning, democratic control.
Part IXB -> Articles 243ZH-243ZT governance code.

Union of India v. Rajendra N. Shah
Part IXB altered the State legislative field without Article 368 ratification.
Majority severed its State-field application.

SURVIVES
Article 19(1)(c) | Article 43B | Part IXB for the valid multi-State field.

EXACT CAUTION
do not claim Part IXB uniformly binds ordinary State cooperatives after the judgment.
The Union-Territory discussion must follow the judgment's precise field analysis.""",
        ),
        (
            "Part IXB architecture from incorporation to transition",
            "article-map-243zh-243zt",
            [7],
            """ARTICLE MAP
243ZH definitions | 243ZI incorporation/regulation/winding up.
243ZJ board size, reservation, co-option and five-year term.
243ZK election before term expiry; State authority conducts.
243ZL supersession/suspension with banking and government-share qualifications.
243ZM audit | 243ZN general body meeting | 243ZO member information.
243ZP returns | 243ZQ offence families | 243ZR multi-State application.
243ZS Union Territories | 243ZT transition.

POST-2021 CONTROL
text remains printed; enforceability depends on the constitutionally valid field.""",
        ),
        (
            "Board, election and supersession safeguards",
            "governance-clock-matrix",
            [7],
            """BOARD
maximum twenty-one directors | reserved seats as text provides
| expert co-option without elected-office voting rights.

TERM
five years from election | office-bearer term tied to board.

ELECTION
must be conducted before expiry; vacancy does not justify indefinite extension.

SUPERSESSION
reasons are textually limited | ordinary maximum six months
| banking society may reach one year | government-share/assistance qualification matters.

DEMOCRATIC LOGIC
member choice -> fixed cycle -> exceptional intervention -> fresh elected control.

TRAP
regulatory supervision does not create permanent administrator ownership.""",
        ),
        (
            "Audit, returns, member rights and offence families",
            "accountability-compliance-ladder",
            [7],
            """AUDIT
qualified panel/accountability route -> annual accounts -> general-body scrutiny.

GENERAL BODY
meeting within the constitutional/statutory clock applicable to the valid field.

MEMBER INFORMATION
access to books and information as law provides; education and participation reinforce control.

RETURNS
annual filing covers activities, audited statements, surplus disposal and governance data.

OFFENCE FAMILIES
false return | disobedience | withholding information | election interference
| failure to hand over records, where textually provided.

LIMIT
penalty, procedure and enforcement source must be identified before asserting liability.""",
        ),
        (
            "State cooperatives, MSCS Act and the 2023 reform framework",
            "dual-regime-2023-system",
            [8, 9],
            """STATE-FIELD SOCIETY
objects confined to one State -> State Act + rules + bye-laws + State Registrar.

MULTI-STATE SOCIETY
objects not confined to one State -> MSCS Act 2002 + Central Registrar.

2023 AMENDMENT
Co-operative Election Authority | election notice and secret ballot
| board/conflict controls | ombudsman grievance route | information officer
| concurrent/risk audit | rehabilitation, reconstruction and development fund
| lawful merger/amalgamation mechanisms.

CURRENT CONTROL
commenced 3 August 2023; Rules notified 4 August 2023.

LIMIT
Union reform in the Entry 44 field does not rewrite every State cooperative Act.""",
        ),
        (
            "Institutional and banking map with sector examples",
            "institution-regulator-value-chain",
            [10, 11, 15],
            """INSTITUTIONS
Ministry -> Union policy/allocated business.
CRCS -> MSCS statutory administration.
State Registrar -> State-law administration.
NCDC -> statutory development finance.
NCUI/representative body -> advocacy, education and coordination.
Operating cooperative -> member-owned enterprise, not regulator.

BANKING OVERLAY
incorporation/governance law + Banking Regulation Act/RBI
| NABARD supervision for specified rural cooperative banks
| PACS boundary must not be erased.

EXAMPLES
dairy pooling | credit access | agricultural marketing | collective input/procurement.

TRAP
credit, dairy and agricultural cooperatives do not share one prudential regulator.""",
        ),
        (
            "Status tests, governance failures and professionalisation",
            "case-status-reform-matrix",
            [12, 13, 14],
            """Thalappalam Service Cooperative Bank
registration and ordinary Registrar control did not automatically create RTI public authority.

THREE DIFFERENT TESTS
Article 12 State | Article 226 public duty | RTI section 2(h) public authority.

FAILURE CHAIN
political capture -> delayed elections -> weak audit -> connected lending
-> member apathy -> losses -> State rescue -> reduced autonomy.

REFORM CHAIN
timely elections + fit expertise + independent audit + member information
-> digital but inclusive records + regulator coordination + proportionate intervention.

VERDICT
autonomy without accountability permits capture; control without autonomy kills cooperation.""",
        ),
        (
            "UPSC traps, adjacent PYQs and federal answer synthesis",
            "exam-federal-synthesis",
            [13, 14, 15],
            """PRELIMS FIREWALL
Part IXB not uniform for all State cooperatives | Article 43B is DPSP
| right to form != right to State aid | Entry 32 != Entry 44
| Ministry != Registrar | RBI != every governance function
| scheduled constitutional text != enforceable State-field command after 2021.

ADJACENT VERIFIED ROUTES
2020 DCCB | 2021 UCB | 2023 Small Farmer Large Field.
They remain Economy/agriculture routes, not invented direct Polity PYQs.

MAINS SPINE
identity/principles -> federal competence -> 97th Amendment
-> Rajendra N. Shah -> State/MSCS regimes -> 2023 accountability
-> banking coordination -> member-centric professionalisation.

CONCLUSION
valid reform is cooperative in both enterprise form and federal method.""",
        ),
    ],
    "polity-40": [
        (
            "Part XVII settlement: official language without a national language",
            "constitutional-language-map",
            [1, 2],
            """ROOT QUESTION
How does one Union preserve common administration without linguistic uniformity?

PART XVII
Chapter I: Articles 343-344 | Union language.
Chapter II: Articles 345-347 | regional languages.
Chapter III: Articles 348-349 | courts and authoritative legal texts.
Chapter IV: Articles 350-351 | grievances, minorities and Hindi development.

CORE DISTINCTIONS
Union official language != national language.
scheduled != official everywhere | classical != scheduled | policy != Constitution.

SETTLEMENT
Hindi in Devanagari + international form of Indian numerals
paired with statutory continuation of English and federal safeguards.""",
        ),
        (
            "Articles 343-344 and the statutory continuation of English",
            "union-language-transition-clock",
            [3, 4, 5, 11, 12],
            """ARTICLE 343
Hindi in Devanagari = official language of Union.
International form of Indian numerals = official numeral form.
English transition period did not create an automatic 1965 switch-off.

OFFICIAL LANGUAGES ACT 1963, AS AMENDED
section 3 continues English for Union official purposes and parliamentary business.
section 3(5) uses a high-consent legislative lock for specified discontinuance.

ARTICLE 344
President's Commission at five years and ten years from commencement.
30-member constitutional parliamentary committee: 20 Lok Sabha + 10 Rajya Sabha.

DO NOT COLLAPSE
Article 344 committee != section 4 statutory Committee on Official Language.""",
        ),
        (
            "Articles 345-347: State choice and intergovernmental communication",
            "state-language-federal-tree",
            [6],
            """ARTICLE 345
State Legislature may adopt one or more languages in use in the State, or Hindi.
English continues until State law otherwise provides within the constitutional frame.

ARTICLE 346
Union-State and inter-State communication follows the authorised Union language,
subject to agreement permitting Hindi between States.

ARTICLE 347
President may recognise a language for specified State purposes on substantial-demand grounds.

TRAPS
Eighth-Schedule inclusion is not a prerequisite for State official-language choice.
Article 347 is not automatic recognition or a general national-language declaration.""",
        ),
        (
            "Articles 348-349: courts, judgments and authoritative texts",
            "court-language-translation-gates",
            [7, 8],
            """ARTICLE 348 BASELINE
English for Supreme Court and High Court proceedings until Parliament provides otherwise.
English authoritative texts for Bills, Acts, ordinances, orders, rules and bye-laws.

HIGH COURT PROCEEDINGS
Governor + previous presidential consent -> Hindi or State official language.
Article 348(2) expressly excludes judgments, decrees and orders.

SECTION 7 ROUTE
authorised non-English High Court judgment/decree/order in addition to English
-> High Court-authorised English translation.

ARTICLE 349
historically time-bounded special procedure; not a routine present-day gate.

LIMIT
machine or general-information translation is not automatically authoritative law.""",
        ),
        (
            "Articles 350, 350A, 350B and 351: access and development",
            "access-minority-development-stack",
            [9, 10],
            """ARTICLE 350
representation for grievance redress may use a language used in the Union or State.

ARTICLE 350A
endeavour to provide mother-tongue instruction facilities at primary stage
for children belonging to linguistic-minority groups.

ARTICLE 350B
Special Officer investigates safeguards -> reports to President
-> laid before Parliament and sent to concerned State governments.

ARTICLE 351
Union duty to promote Hindi and develop it as a medium for India's composite culture,
drawing vocabulary principally from Sanskrit and secondarily from other languages.

BALANCE
promotion of Hindi operates with, not above, plural safeguards and federal consent.""",
        ),
        (
            "Eighth Schedule, classical status and the three-language policy boundary",
            "language-category-matrix",
            [13, 14, 15, 16],
            """EIGHTH SCHEDULE
22 languages in the current official Constitution.
14 original -> Sindhi -> Konkani/Manipuri/Nepali -> Bodo/Dogri/Maithili/Santhali
-> Oriya renamed Odia.

EFFECT
constitutional recognition and Article 344/351 relevance.
No automatic Union, State, court or school-medium status follows.

CLASSICAL STATUS
separate Union executive recognition.
October 2024 additions brought the official count then reported to eleven.

THREE-LANGUAGE FORMULA
education-policy framework with State implementation variation.
It is not a constitutional national-language command.""",
        ),
        (
            "Language cases: competence, minority context and protected choice",
            "case-doctrine-triangle",
            [23],
            """Gujarat University v. Shri Krishna
medium/language power must respect the Union-State education competence boundary.

D.A.V. College v. State of Punjab
linguistic-minority safeguards require contextual constitutional analysis.

State of Karnataka v. Associated Management
compulsory mother-tongue medium cannot override protected educational choice.

DOCTRINAL TRIANGLE
legislative competence | speech/choice rights | linguistic-minority safeguards.

LIMIT
none of these decisions declares a national language or erases Article 350A.""",
        ),
        (
            "Federal accommodation, court access and translation technology",
            "access-technology-balance",
            [17, 18, 19, 20],
            """LEGITIMATE GOALS
administrative interoperability | citizen access | cultural recognition
| judicial usability | educational inclusion.

RISKS
imposition | exclusion from employment/services | translation error
| authoritative-text confusion | weak minority facilities | digital language divide.

TECHNOLOGY CHAIN
multilingual intake -> translation/interpretation -> human legal review
-> authority label -> version control -> accessible publication.

FEDERAL METHOD
consent + capacity + phased implementation + reciprocal communication.

LIMIT
policy targets, committee recommendations and software outputs do not amend Part XVII.""",
        ),
        (
            "UPSC traps, verified PYQ and qualified answer synthesis",
            "exam-language-synthesis",
            [21, 22, 23],
            """PRELIMS FIREWALL
official != national | 22 scheduled languages | Hindi script = Devanagari
| numerals = international form | English continuation = statute
| Article 348(2) excludes judgments | section 7 supplies separate route
| Article 350 grievance right | 350A instruction facility | 350B Special Officer
| classical and three-language categories are separate.

2024 PRELIMS ROUTE
21st, 71st and 92nd Amendment language additions.

MAINS SPINE
constitutional compromise -> Part XVII -> 1963 Act
-> State autonomy -> court/text hierarchy -> minority safeguards
-> category distinctions -> access technology -> federal verdict.

CONCLUSION
multilingual unity requires exact law, consent and authoritative parity.""",
        ),
    ],
    "polity-41": [
        (
            "Canonical scope: Part XIV services, not the PSC institution",
            "scope-article-classification-map",
            [1, 2, 3, 4],
            """ROOT QUESTION
How can an elected executive control administration without creating partisan tenure?

OWNER SCOPE
Articles 308-314 -> recruitment, tenure, discipline and All-India Services.
Articles 315-323 -> Public Service Commissions; treated as a distinct institution topic.

ARTICLE 308
definition provision with present territorial reading after constitutional change.

ARTICLE 309
legislature regulates recruitment and service conditions.
President/Governor makes rules until competent legislation operates.

CLASSIFICATION
Union/State civil service | All-India Service | civil post | defence-connected civil post.

TRAP
departmental label does not by itself decide constitutional status.""",
        ),
        (
            "Doctrine of pleasure and the Article 311 protection trigger",
            "pleasure-protection-fences",
            [5, 6, 7, 8],
            """ARTICLE 310
Union/AIS/civil-post tenure at President's pleasure.
State civil tenure at Governor's pleasure.
The Constitution's express safeguards and special tenure codes limit the doctrine.

Shamsher Singh
formal executive heads ordinarily act through constitutional government.

ARTICLE 311 PERSONS
Union civil service | AIS | State civil service | holder of Union/State civil post.

ARTICLE 311 PENALTIES
dismissal | removal | reduction in rank.

ARTICLE 311(1)
no dismissal/removal by an authority subordinate to the appointing authority.

CORE RULE
pleasure is constitutional power under law, not personal whim.""",
        ),
        (
            "Regular inquiry, natural justice and the three constitutional exceptions",
            "discipline-exception-decision-tree",
            [9, 10, 14, 15],
            """REGULAR ARTICLE 311(2) ROUTE
charges -> evidence -> reasonable opportunity -> inquiry finding -> competent penalty.

Parshotam Lal Dhingra + Khem Chand
punitive-foundation and reasonable-opportunity principles.

42ND AMENDMENT EFFECT
removed the separate constitutional opportunity on proposed penalty,
not the charge-and-inquiry safeguard.

THREE EXCEPTIONS
(a) conviction on criminal charge.
(b) inquiry not reasonably practicable; written reasons required.
(c) President/Governor satisfied inquiry not expedient in State security.

Union of India v. Tulsiram Patel
exceptions are constitutional but their jurisdictional facts and legality remain reviewable.

ECIL v. B. Karunakar
inquiry-report supply and prejudice analysis strengthen fair disciplinary process.""",
        ),
        (
            "Penalty, termination and employment-status distinctions",
            "status-penalty-comparison",
            [11, 12, 13, 36],
            """PENALTIES
dismissal may carry future-employment consequences under rules.
removal is distinct | reduction in rank is punitive demotion.

TERMINATION SIMPLICITER
form is not decisive; motive and foundation determine punitive character.

OTHER ACTIONS
suspension ordinarily interim | compulsory retirement may be punitive or non-punitive
| probation/temporary exit requires the foundation test.

STATUS SCREEN
civil post -> Article 311 may apply.
constitutional office -> special constitutional code first.
statutory-body/PSU employee -> employer, statute and rules control.
contractor/outsourced worker -> contract, labour law and real-control facts.

TRAP
public employment, office under State and civil post are not interchangeable labels.""",
        ),
        (
            "Article 312 and the All-India Services federal bridge",
            "ais-creation-dual-control",
            [16, 17, 18, 19, 20],
            """CREATION ROUTE
Rajya Sabha resolution by at least two-thirds of members present and voting
that national interest requires one or more new All-India Services
-> Parliament may create by law.

EXISTING AIS
IAS | IPS | Indian Forest Service.
Indian Foreign Service is a Central Civil Service, not AIS.

DUAL CONTROL
Union recruitment/cadre framework + State posting and field administration
-> shared career and deputation system.

AIJS
constitutionally enabled under Article 312; no post below district judge; not established.

FEDERAL GAIN
national standards and integration.
FEDERAL RISK
deputation conflict, centralisation and weak State voice.""",
        ),
        (
            "Article 335, neutrality, anonymity and public-service ethics",
            "representation-neutrality-ethics",
            [20, 21, 22, 23, 35],
            """ARTICLE 335
SC/ST claims considered consistently with administrative efficiency,
subject to the constitutional proviso on qualifying marks/standards for promotion.

NEUTRALITY
non-partisanship + constitutional commitment + candid advice + lawful implementation.

ANONYMITY
ministerial responsibility protects ordinary internal advice,
but recordkeeping, courts, RTI law and accountability rules create lawful disclosure routes.

ETHICS STACK
integrity | objectivity | impartiality | political neutrality | empathy | accountability.

ACCOUNTABILITY TRACKS
departmental discipline | vigilance | criminal law | audit | legislative/judicial review.

LIMIT
neutrality is not resistance to lawful elected policy or silence about illegality.""",
        ),
        (
            "Specialists, lateral entry, training and performance management",
            "capacity-reform-portfolio",
            [27, 28, 29, 30, 31],
            """GENERALIST VALUE
coordination, field experience and whole-of-government perspective.

SPECIALIST VALUE
technical depth, regulatory knowledge and domain continuity.

LATERAL ENTRY
post-specific recruitment mode -> equality, recruitment rules, UPSC-consultation question,
reservation, tenure, conflict and cooling-off controls must be checked.

MISSION KARMAYOGI
competency-based capacity building + iGOT learning infrastructure
-> role mapping -> continuous learning -> workplace application.

PERFORMANCE
outcome + legality + process quality + citizen impact + team development.

LIMIT
course completion or short contracts do not themselves prove better administration.""",
        ),
        (
            "Tribunals, transfer reform and the case-law accountability spine",
            "remedy-reform-case-matrix",
            [25, 26, 27],
            """CAT INTERFACE
Article 323A/Administrative Tribunals Act route for covered service disputes.

L. Chandra Kumar
tribunal decisions remain subject to High Court judicial review.

T.S.R. Subramanian
Civil Services Boards, tenure stability and written recording of oral directions.

TRANSFER PROBLEM
formal Article 311 security may coexist with informal pressure through posting control.

REFORM PACKAGE
stable but reviewable tenure | written orders | merit and domain pathways
| fair discipline | protected disclosure | transparent appraisal | reasoned transfers.

VERDICT
security without accountability breeds insulation; control without security breeds compliance.""",
        ),
        (
            "UPSC traps, supporting PYQ and qualified answer synthesis",
            "exam-service-synthesis",
            [32, 33, 34, 35],
            """PRELIMS FIREWALL
Article 309 legislature first | rules are subordinate legislation
| pleasure not personal | Article 311 covers civil posts
| three exceptions exactly | written reasons for clause (b)
| State security for clause (c) | Rajya Sabha gateway for AIS
| IFS not AIS | AIJS enabled, not established | CAT review survives.

SUPPORTING 2020 GS-II ROUTE
institutional quality and civil-service reform for democracy.

MAINS SPINE
permanent executive purpose -> 309 rules -> 310 pleasure
-> 311 fairness/exceptions -> AIS federal bridge -> Article 335
-> neutrality/accountability -> capacity and tenure reform.

CONCLUSION
professional autonomy is legitimate only inside constitutional responsibility.""",
        ),
    ],
    "polity-42": [
        (
            "From 1967 instability to the 52nd and 91st Amendment design",
            "defection-amendment-timeline",
            [1, 2, 3, 4],
            """ROOT QUESTION
How can party-government stability be protected without extinguishing legislative judgment?

1967 defections -> Committee on Defections -> 52nd Amendment Act 1985.
Tenth Schedule effective 1 March 1985.

52ND AMENDMENT
Articles 101, 102, 190, 191 + Tenth Schedule.

91ST AMENDMENT
split defence deleted | ministry-size caps
| Articles 75(1B), 164(1B), 361B office disabilities.

CURRENT PARAGRAPH MAP
1 definitions | 2 grounds | 3 omitted | 4 merger
| 5 presiding exemption | 6 decision | 7 invalid court bar | 8 rules.""",
        ),
        (
            "Grounds and member-type rules",
            "member-ground-matrix",
            [5, 6, 7, 8],
            """PARTY MEMBER
voluntarily gives up membership
OR votes/abstains contrary to direction without prior permission,
unless condoned within fifteen days.

INDEPENDENT MEMBER
joining a political party after election -> disqualification.
No six-month window.

NOMINATED MEMBER
may join within six months from taking the seat;
joining after that period -> disqualification.

Ravi S. Naik
voluntarily giving up is wider than formal resignation and may be inferred from conduct.

TRAP
dissenting speech alone is not automatically paragraph 2(1)(b) voting conduct.""",
        ),
        (
            "Political party, legislature party and the exact whip test",
            "party-whip-authority-chain",
            [5, 6, 7, 19],
            """ORIGINAL POLITICAL PARTY
party to which the member belongs for Schedule purposes.

LEGISLATURE PARTY
House members belonging to the same political party.

WHIP TEST
authorised party direction -> vote or abstention
-> no prior permission -> no condonation within fifteen days.

Subhash Desai
the political party, not a legislature-party faction acting alone,
authorises the whip/leader for Tenth Schedule purposes.

CURRENT LAW
direction may reach ordinary votes under the text.

PROPOSAL
restrict whips to confidence, no-confidence, Money Bills or core manifesto matters.""",
        ),
        (
            "Merger, deleted split and the narrow presiding-officer exemption",
            "merger-replacement-diagram",
            [9, 10],
            """PARAGRAPH 3
one-third split defence omitted by the 91st Amendment.

PARAGRAPH 4
original political party merger + not less than two-thirds of legislature party agree
-> protected choice to join merger or operate as separate group under the text.

INTERPRETIVE CAUTION
two-thirds legislators cannot be written as a free-standing permission to switch parties;
original-party and deeming provisions remain central and live disputes must be qualified.

PARAGRAPH 5
narrow exemption for specified presiding officers on giving up/rejoining party
subject to exact office and timing conditions.

TRAP
Speaker neutrality aspiration does not create a general exemption for every office-holder.""",
        ),
        (
            "Presiding-officer process, natural justice and judicial review",
            "adjudication-review-rail",
            [11, 12, 13, 14, 15],
            """FIRST INSTANCE
Speaker/Chairman decides; if that officer is concerned, House elects another member.

PROCESS
petition -> maintainability/facts -> notice -> reply/evidence -> hearing
-> reasoned decision -> seat consequence.

Kihoto Hollohan
presiding officer acts as tribunal; paragraph 7 invalid for lack of ratification;
limited judicial review survives for jurisdictional error, mala fides and natural justice.

Keisham Meghachandra Singh
absent exceptional circumstances, petitions should ordinarily be decided within three months.

LIMIT
courts ordinarily do not replace the Speaker as first-instance fact finder.""",
        ),
        (
            "Resignation, disqualification and the 91st-Amendment office bars",
            "exit-consequence-chronology",
            [16, 17],
            """CHRONOLOGY
alleged defection -> petition -> resignation -> Speaker decisions -> judicial review.

Shrimanth Balasaheb Patil
resignation does not erase antecedent disqualification;
Speaker cannot add an extra re-election ban beyond constitutional text.

DIRECT EFFECT
loss of House membership under Articles 102(2)/191(2).

OFFICE DISABILITIES
Articles 75(1B), 164(1B), 361B
-> minister/remunerative-political-post bar for the constitutionally defined period.

LIMIT
Tenth Schedule disqualification is not a criminal conviction or universal public-office ban.""",
        ),
        (
            "Nabam Rebia, Subhash Desai and distributed institutional authority",
            "institutional-conflict-map",
            [18, 19],
            """Nabam Rebia
Speaker facing a pending removal notice was held disabled from deciding defection petitions.

PENDING QUALIFICATION
Subhash Desai referred correctness of that rule to a seven-judge bench.
Do not write Nabam Rebia as finally overruled.

Subhash Desai
political party authorises whip | Speaker determines party identity for Schedule purpose
| ECI symbol proceeding is separate | Governor cannot decide intra-party leadership.

DISTRIBUTED ROLES
Speaker -> defection | ECI -> symbol/order field
| Governor -> constitutional functions | court -> review.

TRAP
floor test, symbol dispute and defection petition answer different legal questions.""",
        ),
        (
            "Democratic balance, comparison and reform choices",
            "stability-freedom-reform-matrix",
            [20, 21, 22, 23, 24],
            """GAINS
reduces open floor-crossing | protects mandate | supports government stability.

COSTS
broad whip suppresses deliberation | Speaker incentives | strategic delay
| merger engineering | resignation tactics | weakened committee scrutiny.

COMPARE
Tenth Schedule -> Speaker/Chairman.
Articles 102(1)/191(1) post-election question -> President/Governor on ECI opinion.
RPA -> statutory grounds/procedure | privilege -> House discipline
| symbol dispute -> ECI field.

REFORM OPTIONS
narrow whip | independent tribunal/ECI-advice model | statutory time limit
| reasoned public procedure | neutral presiding-office safeguards.

STATUS
these are proposals unless enacted or judicially ordered in a particular case.""",
        ),
        (
            "UPSC traps, verified PYQs and qualified answer synthesis",
            "exam-defection-synthesis",
            [25, 26, 27],
            """PRELIMS FIREWALL
52nd created | 91st tightened | split deleted | merger two-thirds
| giving up wider than resignation | independent no window
| nominated six months | condonation fifteen days
| Speaker first | judicial review survives | defection not crime.

VERIFIED ROUTES
2022 Prelims -> nominated members.
2025 Prelims -> political-party and Tenth Schedule distinction.
2023 GS-II supporting route -> presiding-officer impartiality.

MAINS SPINE
history -> grounds/member types -> party/whip
-> merger -> process/review/delay -> resignation/office bars
-> institutional conflicts -> stability-freedom balance -> bounded reform.

VERDICT
stability needs discipline, but democratic legitimacy needs a narrower whip,
neutral adjudication and enforceable decision time.""",
        ),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def heading_offsets_any(block: str) -> list[tuple[int, str]]:
    return [
        (match.start(), match.group(1).strip())
        for match in re.finditer(r"(?m)^#{2,5}\s+(.+?)\s*$", block)
    ]


def normalize_question_headings(block: str) -> str:
    headings = heading_offsets_any(block)
    remedial = next(
        (
            offset
            for offset, title in headings
            if re.search(r"^Remedial MCQs?\b|^D\.\s+Remedial MCQs?\b", title, re.I)
        ),
        len(block),
    )

    def normalize_segment(segment: str, prefix: str) -> str:
        pattern = re.compile(
            r"(?m)^(#{2,6})\s+(?:Remedial\s+)?(?:MCQ\s+|Q)(\d+)\.?\s*(.*)$"
        )

        def replace(match: re.Match[str]) -> str:
            tail = match.group(3).strip()
            suffix = f" {tail}" if tail else ""
            return f"{match.group(1)} {prefix}{match.group(2)}.{suffix}"

        return pattern.sub(replace, segment)

    return (
        normalize_segment(block[:remedial], "OM")
        + normalize_segment(block[remedial:], "RM")
    )


def normalize_mains_headings(block: str) -> str:
    pattern = re.compile(
        r"(?m)^(#{2,6})\s+(?:Original\s+)?(?:Solved\s+)?Mains\s+(\d+)"
        r"\s*(?:[—-]\s*)?(.*)$"
    )

    def replace(match: re.Match[str]) -> str:
        tail = match.group(3).strip()
        suffix = f" {tail}" if tail else ""
        return f"{match.group(1)} M{match.group(2)}.{suffix}"

    return pattern.sub(replace, block)


def normalize_control_date(text: str) -> str:
    text = re.sub(
        r"(?mi)(\*\*(?:Legal/current control date|Control date|Export date):\*\*\s*)"
        r"(?:\d{4}-\d{2}-\d{2}|\d{1,2}\s+August\s+2026(?:\s*\(Asia/Kolkata\))?)",
        rf"\g<1>25 August 2026 (Asia/Kolkata)",
        text,
    )
    text = text.replace("19 August 2026", "25 August 2026")
    text = text.replace("20 August 2026", "25 August 2026")
    text = text.replace("19 Aug 2026", "25 Aug 2026")
    text = text.replace("20 Aug 2026", "25 Aug 2026")
    return text


def transform_source(config: dict[str, Any]) -> Path:
    canonical = ROOT / Path(config["canonical"].replace("\\", "/"))
    text = normalize_control_date(
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
    text = re.sub(
        r"(?m)^##\s+(\d)\.\s+",
        lambda match: f"## 0{match.group(1)}. ",
        text,
    )
    status_line = (
        "- [CURRENT] Status is controlled to "
        "**25 August 2026, Asia/Kolkata**."
    )
    first_h2 = re.search(r"(?m)^##\s+", text)
    if not first_h2:
        raise RuntimeError(f"{config['key']}: no package heading found.")
    if status_line not in text:
        text = text[: first_h2.start()] + status_line + "\n\n" + text[first_h2.start() :]
    status = re.search(
        r"(?m)^- \[CURRENT\] Status is controlled to "
        r"\*\*25 August 2026, Asia/Kolkata\*\*\.\s*$",
        text,
    )
    if not status:
        raise RuntimeError(f"{config['key']}: current-control line missing.")
    anchor = (
        f"- [CURRENT] **Live official refresh, 25 August 2026:** "
        f"{config['current_note']}"
    )
    text = text[: status.end()] + "\n" + anchor + text[status.end() :]

    headings = base.heading_offsets(text)
    part_i = base.start_for(headings, [r"^0?1\."])
    practice = base.start_for(
        [(offset, title) for offset, title in headings if offset > part_i],
        [
            r"\bPYQ\b.*\b(?:practice|workbook)\b",
            r"\b(?:practice|workbook)\b.*\bPYQ\b",
        ],
    )
    final = base.start_for(
        headings,
        [r"^Final consolidated register notes(?:\b|$)"],
    )

    supplement = SUPPLEMENTS.get(config["key"], "").strip()
    if supplement:
        text = text[:practice].rstrip() + "\n\n" + supplement + "\n\n" + text[practice:]

    text = base.add_topic_visuals(config, text)
    text = base.add_session_orientations(text)
    headings = base.heading_offsets(text)
    part_i = base.start_for(headings, [r"^0?1\."])
    practice = base.start_for(
        [(offset, title) for offset, title in headings if offset > part_i],
        [
            r"\bPYQ\b.*\b(?:practice|workbook)\b",
            r"\b(?:practice|workbook)\b.*\bPYQ\b",
        ],
    )
    final = base.start_for(
        headings,
        [r"^Final consolidated register notes(?:\b|$)"],
    )

    preamble = text[:part_i]
    core_start = text.find("\n", part_i) + 1
    core = text[core_start:practice]
    practice_start = text.find("\n", practice) + 1
    practice_block = text[practice_start:final]
    final_start = text.find("\n", final) + 1
    register = text[final_start:].strip()

    practice_headings = heading_offsets_any(practice_block)
    mcq_start = base.start_for(
        practice_headings,
        [
            r"^(?:[A-Z]\.\s+)?Original(?: hard)? MCQ",
            r"^Original MCQs?",
        ],
    )
    mains_start = base.start_for(
        practice_headings,
        [
            r"^(?:[A-Z]\.\s+)?Original(?: solved)? Mains",
            r"^Original Solved Mains",
        ],
    )
    pyqs = practice_block[:mcq_start].strip()
    mcqs = normalize_question_headings(practice_block[mcq_start:mains_start].strip())
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
    output = base.SOURCE_SESSION_ROOT / f"{config['key']}_Learning-Session.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8")
    return output


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
            "The complete canonical package is the assembly owner; Basic remains "
            "the independent core and Advanced remains subordinate enrichment."
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
            r"(?m)^#{3,5}\s+(?:[A-Z]\.\s+)?(?:"
            r"PYQ|Verified|Supporting|Cross-linked|Routed|UPSC Prelims"
            r")\b",
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
    expected_order = [f"polity-{number:02d}" for number in range(38, 43)]
    if [config["key"] for config in TOPICS] != expected_order:
        raise RuntimeError("Sequential topic order was altered.")
    base.PANELS.update(PANELS)

    clean_baseline = preserve.topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={38, 39, 40, 41, 42},
    )
    flow_baseline = preserve.flow_topic_hashes(
        exclude_polity={38, 39, 40, 41, 42}
    )
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        resumed = resume_after_tracker(config, 70 + index)
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
            raise RuntimeError(f"{config['key']}: render validation failed.")
        gate_times["F_completed"] = now()

        record = preserve.latest_record(config)
        gate_times["G_completed"] = now()

        base.export_clean_topic(config)
        clean_folder = base.verify_four_folders(config)
        gate_times["H_completed"] = now()

        flow_validation, flow_row = export_flow(config, 70 + index)
        flow_folder = ROOT / Path(flow_row["destination_folder"].replace("\\", "/"))
        gate_times["I_completed"] = now()

        clean_mismatches = preserve.compare_hashes(
            clean_baseline,
            preserve.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={38, 39, 40, 41, 42},
            ),
        )
        flow_mismatches = preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(
                exclude_polity={38, 39, 40, 41, 42}
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
                exclude_polity={38, 39, 40, 41, 42},
            ),
        ),
        "existing_flow_hash_mismatches": preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(
                exclude_polity={38, 39, 40, 41, 42}
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
