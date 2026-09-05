"""Generate the final Polity learner-v2 topics 52-55 in strict order."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_48_51_sequential as prior


content = prior.prior
base = prior.base
preserve = prior.preserve
case_years = prior.case_years
ROOT = prior.ROOT
DATE = "2026-08-25"
SECTION = prior.SECTION
EXPORTS = prior.EXPORTS
FINAL_LIBRARY = prior.FINAL_LIBRARY
FLOW_LIBRARY = prior.FLOW_LIBRARY
BATCH_ID = "polity-52-55-sequential-batch-2026-08-25"

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
        "polity-52",
        "NCRWC and Working of the Constitution",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\NCRWC-and-Working-of-the-Constitution.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\NCRWC-and-Working-of-the-Constitution.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\52_NCRWC-and-Working-of-the-Constitution.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Concept-of-the-Constitution.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
        ],
        [
            "https://www.legalaffairs.gov.in/national-commission-review-working-constitution-ncrwc-report",
            "https://www.legalaffairs.gov.in/",
            "https://www.sci.gov.in/",
            "https://sansad.in/",
        ],
        0,
        4,
        "The Department of Legal Affairs NCRWC report gateway, the official "
        "Constitution/Supreme Court and Parliament portals, and the later legal "
        "instruments used in the implementation matrix were rechecked on 25 August "
        "2026. The official report is a 2002 recommendation source; later similarity "
        "is not labelled implementation without instrument-specific support.",
        "The NCRWC was an executive, temporary, advisory commission established in "
        "2000 under Justice M.N. Venkatachaliah. Its 2002 recommendations are not law. "
        "Every implementation claim is proposal-specific; working of the Constitution "
        "includes institutions, conventions, political practice, capacity and remedies.",
        [
            "2000 resolution, Justice M.N. Venkatachaliah, composition, consultation and 2002 report",
            "review of constitutional working within parliamentary democracy and basic structure",
            "distinction from Constituent Assembly, Parliament, Law Commission, Sarkaria and Punchhi",
            "rights, DPSP, duties, elections, parties, Parliament, executive and judiciary clusters",
            "federalism, decentralisation, administration, corruption and constitutional bodies",
            "proposal-by-proposal implementation matrix without causal overclaim",
            "text, conventions, institutions, coalition/centralisation and legislative functioning",
            "constitutional morality, accountability, rights enforcement and reform-method ladder",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22],
    ),
    topic(
        "polity-53",
        "Special Provisions Relating to Certain Classes",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions-Relating-to-Certain-Classes.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions-Relating-to-Certain-Classes.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\53_Special-Provisions-Relating-to-Certain-Classes.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Commissions-SC-ST-BC.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
        ],
        [
            "https://legislative.gov.in/",
            "https://socialjustice.gov.in/",
            "https://ncsc.nic.in/",
            "https://ncst.nic.in/",
            "https://www.ncbc.nic.in/",
        ],
        2,
        2,
        "The official Constitution and Social Justice/NCSC/NCST/NCBC portals were "
        "rechecked on 25 August 2026. The 106th Amendment provisions are in the "
        "constitutional text but remain tied to the census-delimitation trigger; "
        "current lists, schemes and implementation notifications remain date-specific.",
        "Part XVI is not a single reservation code. Representation, service claims, "
        "commissions and constitutional lists use different legal mechanisms. Davinder "
        "Singh (2024) permits evidence-based SC sub-classification for distribution; "
        "it does not transfer Article 341 list-alteration power to States.",
        [
            "Part XVI Articles 330-342A architecture and owner-scope firewall",
            "SC/ST Lok Sabha and Assembly reservation without separate electorates",
            "106th Amendment women-within-SC/ST seats and non-operational delimitation caveat",
            "Anglo-Indian nomination expiry, 104th Amendment and Article 334 extensions",
            "Article 335 claims, efficiency and relaxation proviso",
            "Articles 338-340 cross-reference, Article 339 control and Article 275 welfare grants",
            "Articles 341, 342 and 342A list specification and 105th Amendment federal split",
            "Davinder Singh line, local-body cross-links, schemes/lists/area administration traps",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20],
    ),
    topic(
        "polity-54",
        "Lok Adalats and Other Courts",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Lok-Adalats-and-Other-Courts.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Lok-Adalats-and-Other-Courts.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\54_Lok-Adalats-and-Other-Courts.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
        ],
        [
            "https://nalsa.gov.in/",
            "https://nalsa.gov.in/lok-adalat/",
            "https://doj.gov.in/",
            "https://www.indiacode.nic.in/",
        ],
        3,
        0,
        "NALSA, the Department of Justice and India Code sources for the Legal "
        "Services Authorities Act 1987, Gram Nyayalayas Act 2008 and Mediation "
        "Act 2023 were rechecked on 25 August 2026. No notification-sensitive "
        "pecuniary ceiling, operational court count or commencement assumption is frozen.",
        "Ordinary Lok Adalats settle only by compromise and cannot decide merits. "
        "Permanent Lok Adalats are pre-litigation public-utility bodies that conciliate "
        "first and may then decide an eligible dispute. Courts, tribunals, mediation, "
        "schemes and operational Lok Adalat formats remain legally distinct.",
        [
            "Article 39A and Legal Services Authorities Act 1987 institutional ladder",
            "ordinary Lok Adalat jurisdiction, consent, return on failure and award finality",
            "Permanent Lok Adalat public-utility pre-litigation hybrid and statutory limits",
            "National, Mega, Mobile and E-Lok Adalat as operational forms",
            "Gram Nyayalayas Act 2008 design, jurisdiction, procedure, appeals and gaps",
            "Family, Fast Track, Special, Commercial and evening-court comparisons",
            "Mediation Act 2023 interface and courts/tribunals/ADR firewall",
            "cases, voluntariness, power asymmetry, quality, digital divide and reform",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22],
    ),
    topic(
        "polity-55",
        "Constitutional Interpretation Doctrines",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Constitutional-Interpretation-Doctrines.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Constitutional-Interpretation-Doctrines.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\55_Constitutional-Interpretation-Doctrines.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Concept-of-the-Constitution.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Duties.md",
        ],
        [
            "https://www.sci.gov.in/",
            "https://api.sci.gov.in/",
            "https://legislative.gov.in/",
            "https://www.legalaffairs.gov.in/",
        ],
        2,
        4,
        "The official Constitution/Supreme Court portals and the controlling "
        "decision-year ledger were rechecked on 25 August 2026. Decided holdings "
        "are separated from later references, reviews, interim orders and pending "
        "questions; no pending doctrinal issue is presented as settled law.",
        "A doctrine is a structured test anchored in text, structure and precedent, "
        "not a substitute for the governing Article. Interpretation, amendment and "
        "judicial legislation are distinct. Bench strength, decision year, legal "
        "effect and limitation must accompany every case-based doctrine.",
        [
            "textual, structural, historical, purposive and precedent-based methods",
            "severability, eclipse, waiver, reading down/into and invalidity remedies",
            "pith and substance, colourability, ancillary power, nexus and Article 254",
            "harmonious construction, prospective overruling and basic structure",
            "presumption, arbitrariness, manifest arbitrariness and proportionality",
            "constitutional morality, transformative constitutionalism and ERP caution",
            "pleasure, expectation, estoppel, casus omissus, silence and conventions",
            "Articles 141/142, bench strength and competence/rights/remedy decision trees",
        ],
        visual_sessions=[1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24],
    ),
]


SUPPLEMENTS: dict[str, list[tuple[str, str]]] = {
    "polity-52": [
        (
            "Recommendation clusters and correct current-law route",
            """| Cluster | NCRWC use | Current-law route |
|---|---|---|
| Rights/DPSP/Duties | reform diagnosis and proposed text | Constitution + controlling cases/statutes |
| Elections/parties | decriminalisation, finance, ECI and party-law proposals | RPA, Symbols Order, Tenth Schedule, case law |
| Parliament/executive | sittings, committees, privileges, ministry size | Constitution, rules, later amendments |
| Judiciary | appointments, complaints, delay and access | current collegium, statutes and judgments |
| Federalism | Governor, Art 356, ISC, water and reserved Bills | constitutional text + later cases |
| Decentralisation | functions, finance, audit, elections | Parts IX/IXA and State law |
| Administration/integrity | civil services, disclosure, Lokpal and audit | later statutes/rules, not report alone |

[LIMIT] The report is reform evidence. It is never the operative source for a later legal rule.""",
        ),
        (
            "Constitutional-working dashboard",
            """WORKING TEST
authority -> restraint -> deliberation -> implementation -> remedy -> public justification.

TEXT FAILURE
unclear allocation or missing safeguard -> amendment may be considered.

PRACTICE FAILURE
adequate text + weak convention/capacity -> procedure, staffing, transparency or accountability.

MIXED FAILURE
text and incentives interact -> calibrated constitutional + legislative + institutional reform.

[LIMIT] Do not constitutionalise every administrative problem or treat every convention as law.""",
        ),
        (
            "Case-bounded follow-through",
            """Kesavananda Bharati (1973) -> basic-structure boundary.
Minerva Mills (1980) -> limited amendment + rights-DPSP harmony.
S.R. Bommai (1994) -> federal/secular structural enforcement.
K.S. Puttaswamy (2017) -> privacy/dignity in modern governance.
Navtej Singh Johar (2018) -> constitutional morality and transformation.

[LIMIT] These are governing judicial developments, not proof that the Court implemented NCRWC.""",
        ),
    ],
    "polity-53": [
        (
            "Part XVI architecture by legal effect",
            """IDENTIFY
Arts 341/342/342A -> who is constitutionally listed.

REPRESENT
Arts 330-334A -> who receives legislative-seat protection and for how long.

SERVICES
Art 335 -> SC/ST claims + administrative efficiency + relaxation proviso.

MONITOR
Arts 338/338A/338B/339/340 -> commissions, reports, directions and investigation.

FUND
Art 275 cross-link -> specified ST welfare/Scheduled Area grants.

[LIMIT] Identification, reservation, welfare funding and area administration are separate.""",
        ),
        (
            "Sub-classification after Davinder Singh",
            """ARTICLE 341 LIST
President specifies -> Parliament includes/excludes.
                    |
                    v
BENEFIT DISTRIBUTION
State designs evidence-based sub-classification within the notified class.
                    |
                    v
JUDICIAL REVIEW
data, rational basis, class integrity, non-exclusion and equality.

E.V. Chinnaiah (2004) -> earlier indivisibility rule.
Davinder Singh (2024) -> overruled that rule; distribution is distinct from list alteration.""",
        ),
        (
            "Representation clocks and cross-links",
            """ARTICLE 334
SC/ST seat reservation -> extended to eighty years from commencement.
Anglo-Indian nomination -> not extended beyond seventy years; ceased in 2020.

ARTICLE 334A
106th Amendment text -> census figures -> delimitation -> operation/rotation.

LOCAL GOVERNMENT
Arts 243D/243T -> separate Panchayat/Municipality reservation architecture.

[LIMIT] Constitutional insertion, commencement and electoral operation are not synonyms.""",
        ),
    ],
    "polity-54": [
        (
            "Referral and outcome decision map",
            """PENDING/PRE-LITIGATION DISPUTE
        |
        +-- ordinary Lok Adalat -> compromise? yes: award; no: return/normal remedy.
        |
        +-- PLA public utility -> conciliate; fail: eligible merits decision.
        |
        +-- mediation -> party-made settlement; no settlement: chosen legal route.
        |
        +-- court/tribunal -> authoritative adjudication under jurisdiction.

[LIMIT] Finality cannot create jurisdiction or genuine consent where none existed.""",
        ),
        (
            "Gram Nyayalaya implementation test",
            """STATUTORY DESIGN
State establishment + High Court consultation + Nyayadhikari + mobile sittings.
        |
        v
JURISDICTION
scheduled civil/criminal matters + local procedure + settlement effort.
        |
        v
APPEAL
Sessions Court criminal | District Court civil, subject to statutory exceptions.
        |
        v
REAL ACCESS
notifications + judges + staff + buildings + awareness + legal aid.

[LIMIT] Enabling legislation does not prove uniform establishment or utilisation.""",
        ),
        (
            "Mediation, commercial justice and operational forms",
            """Mediation Act 2023 -> statutory mediation framework; verify commencement/rules.
Commercial Courts Act -> pre-institution mediation subject to statutory exception.
National/Mega/Mobile/E-Lok Adalat -> operational modes under existing legal character.
Fast Track/Evening Courts -> capacity or scheduling designs, not new constitutional levels.
Special Court -> exact parent statute controls jurisdiction and appeal.

[LIMIT] A label never answers consent, merits power, appeal or review by itself.""",
        ),
    ],
    "polity-55": [
        (
            "Interpretation, amendment and judicial-legislation firewall",
            """INTERPRETATION
text + structure + history + purpose + precedent -> meaning and remedy.

AMENDMENT
Article 368 procedure -> changed constitutional text -> basic-structure review.

JUDICIAL LEGISLATION RISK
no available textual meaning + policy code created + institutional choices displaced.

CONTROL
trigger + provision + test + case-year + effect + limit + narrow remedy.""",
        ),
        (
            "Invalidity and remedy sequence",
            """RIGHTS DEFECT
read down if text bears valid meaning
-> sever invalid part if independent
-> strike if defect is incurable.

PRE-CONSTITUTION LAW
eclipse may suspend enforceability to inconsistency.

NEW RULE
prospective overruling only when the court expressly shapes temporal effect.

[LIMIT] These doctrines alter different objects: meaning, parts, enforceability and time.""",
        ),
        (
            "Doctrinal caution and pending questions",
            """DECIDED CASE
holding + decision year + bench strength + operative remedy.

PENDING REVIEW/REFERENCE
question remains open; earlier binding ratio is not silently erased.

INTERIM ORDER
temporary procedural control, not necessarily final doctrine.

CONSTITUTIONAL MORALITY / ERP / TRANSFORMATION
identify text, right, conflict, precedent and remedy; never invoke as slogans.""",
        ),
    ],
}


PYQS: dict[str, list[dict[str, Any]]] = {
    "polity-52": [
        {
            "label": "Supporting routed PYQ",
            "year": 2021,
            "paper": "GS-II Q1",
            "question": "Explain the doctrine of constitutional morality with illustrations.",
            "directive": "Explain with illustrations",
            "marks": 10,
            "words": 150,
            "points": [
                "Define constitutional morality as fidelity to constitutional forms, equal citizenship and role limits.",
                "Connect text with institutions, conventions and public justification.",
                "Use Navtej Singh Johar (2018) only as a bounded rights illustration.",
                "Distinguish constitutional morality from social or personal morality.",
                "Conclude that constitutional working depends on conduct as well as text.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2024,
            "paper": "GS-II Q1",
            "question": "Examine electoral reforms with reference to the debate on simultaneous elections.",
            "directive": "Examine",
            "marks": 10,
            "words": 150,
            "points": [
                "Locate electoral reform within stability, accountability and federal choice.",
                "Use NCRWC party, ECI and constructive-confidence proposals as recommendations.",
                "Separate later proposals from enacted constitutional law.",
                "Assess representation, campaign finance, legislatures and federal schedules.",
                "Prefer proposal-specific constitutional and implementation scrutiny.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2025,
            "paper": "GS-II Q11",
            "question": "Explain constitutional morality in relation to judicial independence and accountability.",
            "directive": "Explain",
            "marks": 15,
            "words": 250,
            "points": [
                "Independence protects adjudication from improper influence.",
                "Accountability requires reasons, ethics, complaints and constitutional process.",
                "NCRWC judicial proposals are historical recommendations, not current design.",
                "Basic structure protects judicial review without eliminating accountability.",
                "Institutional legitimacy requires both autonomy and transparent restraint.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2019,
            "paper": "GS-II Q12",
            "question": "Explain whether Parliament's Article 368 power can destroy the basic structure.",
            "directive": "Explain",
            "marks": 15,
            "words": 250,
            "points": [
                "Article 368 provides broad but limited constituent power.",
                "Kesavananda Bharati (1973) is the controlling boundary.",
                "NCRWC expressly worked without disturbing basic structure.",
                "A commission report cannot amend or authorise unconstitutional amendment.",
                "Reform must choose the proper legal route and survive structural review.",
            ],
        },
    ],
    "polity-53": [
        {
            "label": "Verified direct PYQ",
            "year": 2023,
            "paper": "Prelims GS-I Q40",
            "question": "Evaluate statements linking reservation under Article 16 with administrative efficiency under Article 335.",
            "directive": "Objective statement evaluation",
            "marks": 2,
            "words": "objective",
            "points": [
                "Article 335 concerns SC/ST claims consistently with administrative efficiency.",
                "Its proviso permits qualifying-mark or standard relaxation in promotion.",
                "Article 335 is not the source of every reservation category.",
                "Read it with Article 16 and controlling case law.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2024,
            "paper": "Prelims GS-I Q81",
            "question": "Evaluate statements concerning the Nari Shakti Vandan Adhiniyam and women's legislative reservation.",
            "directive": "Objective statement evaluation",
            "marks": 2,
            "words": "objective",
            "points": [
                "Arts 330A, 332A and 334A are now constitutional text.",
                "Women-within-SC/ST reserved seats is part of the architecture.",
                "Operation is linked to census figures and delimitation under Article 334A.",
                "Constitutional insertion must not be confused with current electoral operation.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2018,
            "paper": "GS-II Q2",
            "question": "Examine the role of the NCSC and reservation for Scheduled Castes in minority institutions.",
            "directive": "Examine",
            "marks": 10,
            "words": 150,
            "points": [
                "Article 338 creates NCSC monitoring and reporting functions.",
                "Civil-court inquiry powers do not make recommendations binding.",
                "Educational reservation arises from equality provisions and law, not Article 338 alone.",
                "Minority-right limitations require the specialist rights framework.",
                "Keep commission, list and benefit sources separate.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2022,
            "paper": "GS-II Q5",
            "question": "Discuss the constitutionalisation of the National Commission for Backward Classes.",
            "directive": "Discuss",
            "marks": 10,
            "words": 150,
            "points": [
                "The 102nd Amendment inserted Article 338B and Article 342A.",
                "NCBC status is distinct from an Article 340 temporary commission.",
                "Jaishri Laxmanrao Patil (2021) preceded the 105th Amendment response.",
                "The 105th Amendment restored express State/UT list competence for own purposes.",
                "Commission advice, list identification and reservation policy remain distinct.",
            ],
        },
    ],
    "polity-54": [
        {
            "label": "Verified direct PYQ",
            "year": 2020,
            "paper": "Prelims GS-I Q9",
            "question": "Evaluate eligibility categories for free legal services under the Legal Services Authorities framework.",
            "directive": "Objective statement evaluation",
            "marks": 2,
            "words": "objective",
            "points": [
                "Section 12 contains status-based and income-based categories.",
                "SC/ST members, women/children, custody and specified vulnerability may qualify.",
                "Free legal services are broader than criminal-trial representation.",
                "The authority also considers whether a prima facie case exists.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2023,
            "paper": "GS-II Q2",
            "question": "Assess entitlement to free legal aid and the role of NALSA.",
            "directive": "Assess",
            "marks": 10,
            "words": 150,
            "points": [
                "Article 39A supplies the constitutional access-to-justice anchor.",
                "NALSA sets policy and schemes under the 1987 Act.",
                "State, District and Taluk institutions deliver legal services.",
                "Hussainara Khatoon (1979) links legal aid and speed to fair procedure.",
                "Quality, awareness and continuity qualify formal entitlement.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2024,
            "paper": "GS-II Q2",
            "question": "Explain and distinguish Lok Adalats and Arbitration Tribunals.",
            "directive": "Explain and distinguish",
            "marks": 10,
            "words": 150,
            "points": [
                "Ordinary Lok Adalat is statutory compromise-based settlement.",
                "An arbitral tribunal derives adjudicatory authority from agreement and statute.",
                "Lok Adalat award is a deemed decree; arbitral award follows the arbitration enforcement route.",
                "Ordinary Lok Adalat cannot impose a merits result after settlement fails.",
                "PLA is a separate public-utility hybrid and must not be used to define every Lok Adalat.",
            ],
        },
    ],
    "polity-55": [
        {
            "label": "Verified direct PYQ",
            "year": 2019,
            "paper": "GS-II Q4",
            "question": "Explain the principles of federal supremacy and harmonious construction.",
            "directive": "Explain",
            "marks": 10,
            "words": 150,
            "points": [
                "Begin with Articles 245-246 and the Seventh Schedule.",
                "Harmonious construction first gives each field meaningful operation.",
                "Pith and substance tolerates incidental overlap.",
                "Federal supremacy resolves only an irreconcilable conflict authorised by the Constitution.",
                "Article 254 has its own Concurrent-field test.",
            ],
        },
        {
            "label": "Verified direct PYQ",
            "year": 2021,
            "paper": "GS-II Q1",
            "question": "Explain the doctrine of constitutional morality with illustrations.",
            "directive": "Explain with illustrations",
            "marks": 10,
            "words": 150,
            "points": [
                "Define it through constitutional forms, equality, dignity and institutional roles.",
                "Use Navtej Singh Johar (2018) as a bounded illustration.",
                "Connect the doctrine to text, structure and remedy.",
                "Distinguish it from social or personal morality.",
                "State that it cannot become free-standing judicial preference.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2019,
            "paper": "GS-II Q12",
            "question": "Explain Article 368 amending power and the basic structure doctrine.",
            "directive": "Explain",
            "marks": 15,
            "words": 250,
            "points": [
                "Article 368 provides the amendment procedure and power.",
                "Kesavananda Bharati (1973) supplies the damage-to-basic-structure limit.",
                "Minerva Mills (1980) confirms limited amendment power.",
                "Interpretation applies the limit; it does not itself amend text.",
                "A strong conclusion reconciles adaptation with constitutional identity.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2020,
            "paper": "Prelims GS-I Q13",
            "question": "Identify the correct meaning of the basic structure doctrine and judicial review.",
            "directive": "Objective doctrine identification",
            "marks": 2,
            "words": "objective",
            "points": [
                "The doctrine limits Parliament's constitutional-amendment power.",
                "It does not place every ordinary law beyond its own rights/competence tests.",
                "The Constitution does not contain a closed textual list of features.",
                "Bench holdings and context determine the doctrinal proposition.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2023,
            "paper": "Prelims GS-I Q34",
            "question": "Evaluate constitutional amendments enacted in response to judicial interpretation.",
            "directive": "Objective chronology and effect",
            "marks": 2,
            "words": "objective",
            "points": [
                "A constitutional amendment changes text through Article 368.",
                "A judgment interprets the existing text and may invalidate law.",
                "Later amendment does not erase the historical holding.",
                "The amendment itself remains open to basic-structure review.",
            ],
        },
        {
            "label": "Supporting routed PYQ",
            "year": 2025,
            "paper": "GS-II Q11",
            "question": "Explain constitutional morality in relation to judicial independence and accountability.",
            "directive": "Explain",
            "marks": 15,
            "words": 250,
            "points": [
                "Judicial independence is a structural guarantee, not personal immunity.",
                "Accountability uses reasons, ethics, procedure and review-compatible mechanisms.",
                "Constitutional morality disciplines every institution's role.",
                "Article 141 bench hierarchy and Article 142 limits support institutional restraint.",
                "The conclusion should join independence with transparent constitutional responsibility.",
            ],
        },
    ],
}


FACTS: dict[str, list[tuple[str, str, list[str], str]]] = {
    "polity-52": [
        ("NCRWC status", "It was a temporary executive advisory commission created by a 2000 resolution.", ["It was a constitutional body under Article 368.", "It was a statutory Law Commission.", "It exercised constituent power."], "Legal status controls the force of every recommendation."),
        ("review boundary", "Its mandate reviewed working within parliamentary democracy and without disturbing basic structure.", ["It could replace the Constitution.", "It excluded institutional practice.", "It bound Parliament."], "Review was maintenance-oriented, not a constituent rewrite."),
        ("report timing", "Justice M.N. Venkatachaliah chaired the Commission and the report was submitted in 2002.", ["The report was submitted in 1950.", "Sarkaria chaired it.", "It remains a pending court case."], "Identity and year are foundational facts."),
        ("recommendation status", "Each proposal remains non-binding unless separately enacted or judicially recognised.", ["All 249 proposals became law.", "None can ever influence reform.", "A later similar law proves adoption."], "Implementation requires instrument-specific comparison."),
        ("working concept", "Constitutional working includes text, institutions, conventions, parties, administration and remedies.", ["It means amendments alone.", "It excludes political practice.", "It is identical to judicial review."], "Performance may fail without textual collapse."),
        ("implementation audit", "Exact adoption, modified adoption and functional similarity are different findings.", ["Chronology proves causation.", "A common subject proves adoption.", "Global implementation claims are sufficient."], "Recommendation-by-recommendation audit prevents overclaim."),
        ("ministry ceiling", "The NCRWC proposed 10%; the 91st Amendment adopted a different 15% ceiling.", ["Both used 10%.", "The NCRWC enacted the ceiling.", "There is no ministry ceiling."], "Related reform is not exact implementation."),
        ("judicial commission", "The NCRWC proposal, later NJAC scheme and current collegium are distinct.", ["They are the same institution.", "NCRWC created NJAC.", "The 2015 decision approved NJAC."], "Source, design and legal status differ."),
        ("federal reform", "Governor, Article 356 and Inter-State Council proposals were recommendations, not current text.", ["They amended Articles 155-156.", "They repealed Article 356.", "They bind every Governor."], "Use current Articles and cases for operative law."),
        ("constitutional morality", "It means fidelity to constitutional forms, equality and institutional role limits.", ["It means majority morality.", "It is personal judicial ethics only.", "It replaces constitutional text."], "The doctrine must be textually and structurally anchored."),
        ("reform ladder", "Practice, executive action, legislation and amendment are distinct reform routes.", ["Every problem needs amendment.", "Executive action can amend Part III.", "Commission advice itself changes law."], "Choose the least legally sufficient route."),
        ("answer method", "Cluster recommendations, state status, compare later law and give a qualified verdict.", ["List proposals without status.", "Call every later reform implementation.", "Ignore basic structure."], "This converts a report into an analytical answer."),
    ],
    "polity-53": [
        ("Part XVI", "Part XVI combines representation, services, commissions and list identification.", ["It is only an employment quota code.", "It administers Scheduled Areas completely.", "It contains every welfare scheme."], "Different Articles produce different legal effects."),
        ("reserved seats", "Articles 330 and 332 reserve SC/ST seats without creating separate electorates.", ["Only SC/ST voters vote there.", "Seats are executive grants.", "Article 335 creates them."], "Territorial electorate and candidate reservation differ."),
        ("women reservation", "Arts 330A, 332A and 334A are inserted but operation is tied to census-delimitation.", ["They were removed.", "They operate without delimitation.", "They alter SC/ST lists."], "Insertion is not current electoral operation."),
        ("Anglo-Indian nomination", "The Article 334 period was not extended beyond seventy years and nomination ceased in 2020.", ["Articles 331/333 were necessarily omitted.", "It continues to eighty years.", "The 104th Amendment ended SC/ST seats."], "Text presence and time-clause operation differ."),
        ("Article 335", "It joins SC/ST service claims with efficiency and contains a promotion-relaxation proviso.", ["It fixes all quota percentages.", "It governs OBC lists.", "Efficiency automatically defeats reservation."], "Read it with Article 16 and cases."),
        ("commission cross-reference", "Arts 338, 338A and 338B create NCSC, NCST and NCBC.", ["Article 340 creates all three.", "Civil-court powers make reports binding.", "They are statutory tribunals."], "Commission detail remains cross-owned."),
        ("Article 339", "It supports Union directions and commissions concerning Scheduled Areas and ST welfare.", ["It alters Article 342 lists.", "It is the Sixth Schedule.", "It creates local reservations."], "Supervision is distinct from list and area institutions."),
        ("Article 275", "It includes a fiscal route for specified ST welfare and Scheduled Area administration grants.", ["It permits caste-list amendment.", "It is a reservation Article.", "It abolishes State discretion."], "Fiscal support does not redefine status."),
        ("SC/ST lists", "President specifies; Parliament alone includes or excludes under Arts 341-342.", ["States may alter by executive order.", "Courts maintain lists.", "Lists are nationally identical."], "Lists are territorial and constitutionally controlled."),
        ("SEBC lists", "After the 105th Amendment Central and State/UT lists serve different governmental purposes.", ["Only one list exists.", "States may alter SC lists.", "NCBC alone legislates entries."], "The federal list split is explicit."),
        ("Davinder Singh", "The 2024 decision permits evidence-based SC sub-classification for benefit distribution.", ["It lets States alter Article 341.", "It mandates exclusion of every advanced group.", "It restored E.V. Chinnaiah."], "Distribution and identification remain separate."),
        ("local-body cross-link", "Arts 243D and 243T separately govern Panchayat and Municipal reservation.", ["They are Part XVI provisions.", "Article 334 governs all local seats.", "Lists automatically create local quotas."], "Local representation has its own source."),
    ],
    "polity-54": [
        ("Article 39A", "It directs equal-opportunity justice and free legal aid.", ["It creates every Lok Adalat directly.", "It is a Fundamental Right text.", "It abolishes court fees."], "Statutes and Article 21 doctrine operationalise the directive."),
        ("authority ladder", "The 1987 Act links NALSA, State, High Court, District and Taluk bodies.", ["NALSA is a trial court.", "Only income-based persons qualify.", "DLSA is constitutional."], "The ladder combines policy and delivery."),
        ("ordinary Lok Adalat", "It settles pending or pre-litigation disputes only through compromise.", ["It always decides merits.", "It hears non-compoundable offences.", "It is an arbitral tribunal."], "Consent is the source of the award."),
        ("failed settlement", "A pending case returns to court when ordinary Lok Adalat settlement fails.", ["The Lok Adalat imposes judgment.", "The claim is extinguished.", "PLA rules automatically apply."], "No compromise means no ordinary award."),
        ("award effect", "A compromise award is final, binding and deemed a civil-court decree with no statutory appeal.", ["No review is conceivable.", "It is merely advice.", "It requires arbitral enforcement."], "Limited constitutional challenge survives fraud/consent/jurisdiction defects."),
        ("Permanent Lok Adalat", "PLA is pre-litigation, public-utility specific and conciliates before eligible merits adjudication.", ["It is an ordinary permanent sitting.", "It hears every civil dispute.", "Consent is always required for the final merits award."], "Its hybrid power is statutory and limited."),
        ("operational forms", "National, Mega, Mobile and E-Lok Adalats do not change the underlying legal character.", ["Each is a new constitutional court.", "E-Lok Adalat can compel settlement.", "Mobile format creates appeal."], "Format is not jurisdiction."),
        ("Gram Nyayalaya", "It is a statutory local/mobile first-instance court with scheduled jurisdiction and appeals.", ["It is a Panchayat.", "It is a Lok Adalat.", "It has no adjudicatory power."], "Establishment and utilisation remain State-dependent."),
        ("Family Court", "It is a statutory court combining family adjudication with settlement orientation.", ["It is compromise-only.", "Lawyers always have an absolute right of appearance.", "It is a tribunal under Article 323B."], "Specialisation does not remove fairness or appeal rules."),
        ("other courts", "Fast Track/evening courts are designs; special/commercial courts depend on governing law.", ["Every label creates a constitutional level.", "All are ADR.", "All have identical appeals."], "Source determines power."),
        ("mediation", "Mediation produces a party-made settlement and differs from PLA merits adjudication.", ["Mediator imposes a decree.", "Every mediation is Lok Adalat.", "The 2023 Act erases sectoral laws."], "Check commencement, rules and exclusions."),
        ("fairness", "Access gains must be tested against consent quality, power asymmetry and digital exclusion.", ["Disposal volume alone proves justice.", "Finality cures coercion.", "Online access has no exclusion risk."], "Access requires affordability and procedural fairness."),
    ],
    "polity-55": [
        ("method order", "Begin with text, then structure, history, purpose and binding precedent.", ["Choose any preferred value first.", "History always controls.", "Purpose can contradict text."], "Interpretive legitimacy requires an explained method."),
        ("severability", "A separable invalid part may fall while a workable intended remainder survives.", ["The whole law always falls.", "Court rewrites the scheme.", "It applies only to amendments."], "Intent and functional completeness matter."),
        ("eclipse", "A pre-Constitution law may become unenforceable to the extent of FR inconsistency.", ["It is repealed.", "Every post-Constitution law revives.", "It waives the right."], "Classical eclipse is not repeal."),
        ("waiver", "Consent cannot ordinarily validate State action contrary to a Fundamental Right.", ["Every private right is non-waivable.", "Waiver amends Part III.", "Only Parliament can invoke it."], "The rule protects public constitutional policy."),
        ("pith and substance", "Dominant nature controls competence and tolerates genuine incidental overlap.", ["Every overlap is repugnancy.", "Political motive controls.", "Ancillary power creates any field."], "Identify true subject and effect."),
        ("colourability", "The doctrine tests disguised lack of legislative competence, not bad motive alone.", ["It is a corruption test.", "It applies only to executive action.", "Form always controls."], "Substance defeats disguise."),
        ("repugnancy", "Article 254 addresses actual conflict in the same Concurrent field.", ["It governs every Union-State overlap.", "Assent cures lack of competence.", "State law permanently overrides Parliament."], "Field, conflict and assent must be separate."),
        ("reading down", "A court may preserve a textually available narrower meaning.", ["It may create a new code.", "It is identical to severability.", "It ignores clear words."], "Textual availability is the limit."),
        ("basic structure", "Article 368 amendment cannot damage basic constitutional structure.", ["Every ordinary policy is reviewed under it.", "It is an enumerated Article list.", "Court may amend text directly."], "It limits amendment, not democratic choice generally."),
        ("manifest arbitrariness", "Legislation may fail Article 14 when capricious or without an adequate principle.", ["Any disagreement suffices.", "It replaces proportionality.", "It tests only motive."], "The threshold is demanding."),
        ("proportionality", "Review tests authority, aim, connection, necessity and balance.", ["Court selects its preferred policy.", "It applies without a right.", "It is only classification."], "Identify the right and restriction first."),
        ("precedent", "Article 141 binds through ratio and bench strength; Article 142 remains substantively limited.", ["Every observation is ratio.", "Smaller benches overrule larger benches.", "Article 142 replaces legislation."], "Reference and remedy discipline preserve legitimacy."),
    ],
}


MAINS_PROMPTS: dict[str, list[tuple[int, str, str]]] = {
    "polity-52": [
        (10, "Explain the constitutional status and mandate of the NCRWC.", "Explain"),
        (10, "Distinguish review of constitutional working from constitutional rewriting.", "Distinguish"),
        (15, "Examine the NCRWC recommendations on elections, parties and legislative functioning.", "Examine"),
        (15, "Assess the NCRWC's federalism and decentralisation reform agenda.", "Assess"),
        (15, "Analyse why implementation must be audited recommendation by recommendation.", "Analyse"),
        (20, "The Constitution may fail in practice without failing in text. Discuss.", "Discuss"),
        (20, "Evaluate the NCRWC as a model of constitutional maintenance rather than replacement.", "Evaluate"),
        (20, "Design a calibrated reform method for improving the working of the Constitution.", "Design"),
    ],
    "polity-53": [
        (10, "Explain the four-part architecture of Part XVI.", "Explain"),
        (10, "Distinguish constitutional-list identification from reservation policy.", "Distinguish"),
        (15, "Examine Article 335 as a balance between representation and administrative efficiency.", "Examine"),
        (15, "Analyse the 102nd-105th Amendment sequence governing SEBC lists.", "Analyse"),
        (15, "Assess the constitutional position of Anglo-Indian nomination after the 104th Amendment.", "Assess"),
        (20, "Discuss legislative representation safeguards under Articles 330-334A.", "Discuss"),
        (20, "Evaluate Davinder Singh (2024) and the boundary between sub-classification and list alteration.", "Evaluate"),
        (20, "Part XVI is a layered equality architecture, not a single reservation code. Comment.", "Comment"),
    ],
    "polity-54": [
        (10, "Distinguish an ordinary Lok Adalat from a Permanent Lok Adalat.", "Distinguish"),
        (10, "Explain the constitutional and statutory basis of free legal aid.", "Explain"),
        (15, "Assess Gram Nyayalayas as instruments of doorstep justice.", "Assess"),
        (15, "Compare Family Courts, Commercial Courts and Fast Track Courts.", "Compare"),
        (15, "Analyse the Mediation Act 2023 interface with Lok Adalats and commercial justice.", "Analyse"),
        (20, "Evaluate India's plural access-to-justice architecture.", "Evaluate"),
        (20, "Consent is the legitimacy boundary of settlement justice. Discuss.", "Discuss"),
        (20, "Suggest reforms for accessible, fair and digitally inclusive dispute resolution.", "Suggest"),
    ],
    "polity-55": [
        (10, "Explain severability, eclipse and waiver as distinct Article 13 doctrines.", "Explain"),
        (10, "Distinguish pith and substance from colourable legislation.", "Distinguish"),
        (15, "Analyse occupied field and repugnancy under Article 254.", "Analyse"),
        (15, "Examine reading down and its boundary with judicial legislation.", "Examine"),
        (15, "Discuss constitutional morality and transformative constitutionalism.", "Discuss"),
        (20, "Construct a doctrine-based decision tree for reviewing a rights-restricting law.", "Construct"),
        (20, "Evaluate proportionality and manifest arbitrariness as standards of rights review.", "Evaluate"),
        (20, "Constitutional interpretation is disciplined creativity, not judicial sovereignty. Comment.", "Comment"),
    ],
}


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-52": [
        (
            "NCRWC identity, mandate and constitutional boundary",
            "commission-identity-root",
            [1, 2],
            """ROOT QUESTION
How can constitutional performance be reviewed without claiming constituent power?

2000 Government resolution -> temporary executive advisory commission.
Justice M.N. Venkatachaliah -> chair | 11 members | report submitted in 2002.

MANDATE
review fifty years of working -> effective governance + socio-economic development.

BOUNDARY
parliamentary democracy + basic structure preserved.

VERDICT
review of working != rewriting the Constitution.""",
        ),
        (
            "Consultation and institutional identity firewall",
            "institution-comparison-matrix",
            [3, 4],
            """CONSULTATION
papers + expert studies + public responses + thematic deliberation -> advisory report.

CONSTITUENT ASSEMBLY -> framed Constitution.
PARLIAMENT/ART 368 -> amends through constitutional procedure.
LAW COMMISSION -> law-reform reports.
SARKARIA/PUNCHHI -> Centre-State review.
NCRWC -> comprehensive working review, no constituent authority.

TRAP
expertise and consultation create persuasion, not legal force.""",
        ),
        (
            "Working of the Constitution: text to lived performance",
            "constitutional-working-chain",
            [5, 6],
            """TEXT
Articles + Parts + Schedules
   |
   v
INSTITUTIONS
Parliament + executive + courts + federal units + bodies
   |
   v
PRACTICE
conventions + parties + administration + political incentives
   |
   v
OUTCOMES
rights + accountability + deliberation + federal trust + remedies.

Kesavananda Bharati (1973) -> structural boundary.
Minerva Mills (1980) -> limited amendment + rights-DPSP harmony.""",
        ),
        (
            "Recommendation clusters without law-status contamination",
            "recommendation-cluster-grid",
            [7, 8],
            """RIGHTS / DPSP / DUTIES
new rights, stronger implementation and proposed duties.

ELECTIONS / PARTIES
criminalisation, finance, ECI selection, party law and anti-defection.

PARLIAMENT / EXECUTIVE / ADMINISTRATION
sittings, committees, privileges, ministry size, civil services and integrity.

JUDICIARY / FEDERALISM / LOCAL GOVERNMENT
appointments, access, Governor, Art 356, councils and devolution.

STATUS
every node = NCRWC recommendation until separately enacted.""",
        ),
        (
            "Implementation audit: exact, modified, similar or pending",
            "implementation-status-ladder",
            [9, 10],
            """PROPOSAL -> LATER INSTRUMENT -> WORDING -> LEGAL EFFECT -> VERDICT

10% ministry ceiling
-> 91st Amendment (2003) uses 15% -> modified related reform, not exact adoption.

judicial commission
-> NJAC enacted 2014, invalidated 2015 -> not current NCRWC design.

party law + narrow whip
-> no comprehensive enactment -> substantially pending.

disaster to Concurrent List
-> Disaster Management Act 2005, no List transfer -> statutory response, not adoption.

RULE
chronology + similarity != proven implementation.""",
        ),
        (
            "Accountability, federalism and legislative practice",
            "accountability-federal-map",
            [11, 12],
            """ACCOUNTABILITY
elections | confidence | committees | CAG | transparency | reasons | judicial review.

LEGISLATURE
sitting time -> scrutiny -> delegated law -> opposition -> financial control.

FEDERAL PRACTICE
consultation -> councils -> Governor restraint -> floor test -> negotiated implementation.

S.R. Bommai (1994) -> federal and secular structural enforcement.

TRAP
majority strength or coalition form does not itself prove good constitutional working.""",
        ),
        (
            "Constitutional morality and rights enforcement",
            "morality-rights-balance",
            [13, 14],
            """CONSTITUTIONAL MORALITY
text + procedure + equal citizenship + institutional role restraint.

K.S. Puttaswamy (2017)
privacy + dignity in modern governance.

Navtej Singh Johar (2018)
constitutional morality + transformative rights.

RIGHTS WORKING
guarantee -> institution -> affordable remedy -> compliance -> public justification.

LIMIT
morality is not personal preference; later cases are not NCRWC implementation evidence.""",
        ),
        (
            "Reform-method ladder and feasibility test",
            "reform-method-decision-tree",
            [15],
            """DIAGNOSE
text gap? convention failure? capacity deficit? incentive failure? remedy gap?
   |
   +-- practice/convention repair
   +-- executive rule or capacity
   +-- ordinary legislation
   +-- Article 368 amendment
   |
   v
TEST
basic structure + rights + federalism + democratic legitimacy
+ finance + implementation + review.

VERDICT
use the least legally sufficient and institutionally workable route.""",
        ),
        (
            "UPSC synthesis: commission report to constitutional answer",
            "answer-synthesis",
            [1, 4, 8, 12, 15],
            """PRELIMS FIREWALL
2000 resolution | Venkatachaliah | 11 members | 2002 report
| advisory | review, not rewrite | recommendations, not law.

MAINS SPINE
identity -> mandate -> working beyond text -> recommendation clusters
-> implementation audit -> morality/accountability/federal practice -> reform ladder.

PYQ ROUTE
constitutional morality | electoral reform | judicial accountability | basic structure.

CONCLUSION
NCRWC is a diagnostic reform menu subject to constitutional route and present-law verification.""",
        ),
    ],
    "polity-53": [
        (
            "Part XVI as a four-part constitutional architecture",
            "part-xvi-root",
            [1, 2],
            """ROOT QUESTION
How does Part XVI combine inclusion without using one legal mechanism?

REPRESENTATION -> Arts 330-334A.
SERVICES -> Art 335.
COMMISSIONS / CONTROL -> Arts 338-340.
IDENTIFICATION -> Arts 341-342A.

CROSS-LINKS
Art 275 grants | Arts 243D/243T local seats | Fifth/Sixth Schedule administration.

VERDICT
list != quota != commission report != welfare scheme.""",
        ),
        (
            "SC/ST legislative seats and ordinary territorial voting",
            "representation-process",
            [3, 4],
            """LOK SABHA
Art 330 -> SC/ST reserved seats linked broadly to population.

STATE ASSEMBLIES
Art 332 -> SC/ST reserved seats + specified North-East provisions.

ELECTION
reserved candidacy/seat -> ordinary territorial electorate votes.

TRAP
political reservation != separate electorate
| representation != Article 341/342 list alteration.""",
        ),
        (
            "Women reservation and Article 334A activation chain",
            "women-reservation-timeline",
            [5, 6],
            """106TH AMENDMENT TEXT
Arts 330A + 332A + 334A.
        |
        v
first census after commencement -> relevant figures published
        |
        v
delimitation exercise -> electoral operation
        |
        v
rotation after subsequent delimitation as Parliament provides.

WITHIN SC/ST SEATS
women share included in constitutional design.

TRAP
inserted/commenced != presently operational.""",
        ),
        (
            "Anglo-Indian history and political-reservation clock",
            "time-clause-comparison",
            [7, 8],
            """ARTS 331 / 333
historical Anglo-Indian nomination provisions remain printed.

ARTICLE 334
SC/ST seat reservation -> extended to eighty years from commencement.
Anglo-Indian nomination -> not extended beyond seventy years -> ceased in 2020.

ARTS 336 / 337
services and educational-grant transitions -> exhausted after ten years.

TRAP
time-clause cessation != necessary textual omission.""",
        ),
        (
            "Article 335: representation with administrative efficiency",
            "services-balance",
            [9, 10],
            """ARTICLE 335
SC/ST claims in Union/State services
        +
maintenance of administrative efficiency.

82ND AMENDMENT PROVISO
qualifying-mark/evaluation relaxation for promotion reservation may be provided.

M. Nagaraj (2006) -> promotion-enabling provisions with constitutional conditions.
Jarnail Singh (2018) -> modifies data rule and applies creamy-layer logic.

TRAP
Art 335 is not a fixed quota or the source of OBC/EWS reservation.""",
        ),
        (
            "Commissions, Union control and welfare grants",
            "safeguard-institution-map",
            [11, 12],
            """ART 338 -> NCSC | ART 338A -> NCST | ART 338B -> NCBC.
reports + complaints + safeguards + civil-court inquiry powers -> advice, not binding judgment.

ART 339
Presidential commission + Union directions on Scheduled Areas/ST welfare.

ART 340
temporary backward-class investigation commission.

ART 275
specified ST welfare/Scheduled Area grant route.

TRAP
commission power != court | fiscal grant != list alteration.""",
        ),
        (
            "List specification and the 102nd-105th Amendment sequence",
            "list-federalism-map",
            [13, 14],
            """ARTS 341 / 342
President specifies State/UT SC/ST list -> Parliament includes/excludes.

102ND AMENDMENT
Arts 338B + 342A -> constitutional NCBC/Central List architecture.

Jaishri Laxmanrao Patil (2021)
interprets the pre-105th text.

105TH AMENDMENT
Central List for Central purposes
| State/UT list by law for own purposes.

TRAP
State SEBC list power != State power to alter SC/ST lists.""",
        ),
        (
            "Sub-classification, local bodies and owner boundaries",
            "subclassification-boundary",
            [15],
            """E.V. Chinnaiah (2004)
earlier rule against SC sub-classification.
        |
        v overruled
Davinder Singh (2024)
evidence-based distribution within notified SC class may be designed.

BOUNDARY
sub-classification != inclusion/exclusion under Art 341.

LOCAL BODY
Arts 243D/243T -> separate reservation route.

AREA ADMINISTRATION / SCHEMES
exact Schedule, statute, budget or policy controls.""",
        ),
        (
            "UPSC synthesis: identify the exact constitutional technique",
            "answer-synthesis",
            [1, 4, 8, 12, 15],
            """PRELIMS FIREWALL
330/332 seats | 334 clock | 335 services | 338-series commissions
| 339 control | 340 inquiry | 341/342/342A lists | 275 grant cross-link.

MAINS SPINE
architecture -> representation -> time/activation -> services
-> safeguards -> list federalism -> Davinder boundary -> owner-scope conclusion.

PYQ ROUTE
Article 335 | women's reservation | NCSC | constitutional NCBC.

VERDICT
substantive equality uses distinct constitutional tools with distinct legal effects.""",
        ),
    ],
    "polity-54": [
        (
            "Article 39A and the legal-services ladder",
            "access-justice-root",
            [1, 2],
            """ROOT QUESTION
How can justice become affordable and proximate without sacrificing fairness?

ARTICLE 39A
equal-opportunity legal system + free legal aid.

1987 ACT LADDER
NALSA -> State Authority -> High Court Committee
-> District Authority -> Taluk Committee.

ARTICLE 21 LINK
Hussainara Khatoon (1979) -> legal aid and speedy justice support fair procedure.

TRAP
Directive Principle anchor != direct creation of every forum.""",
        ),
        (
            "Ordinary Lok Adalat: compromise is the jurisdictional core",
            "ordinary-lok-adalat-flow",
            [3, 4],
            """PENDING CASE / PRE-LITIGATION MATTER
        |
        v
conciliation + justice/equity/fair play
   +----+----+
   |         |
settlement  no settlement
   |         |
award       pending case returns / normal remedy continues.

State of Punjab v. Jalour Singh (2008)
ordinary Lok Adalat cannot adjudicate merits.

NON-COMPOUNDABLE OFFENCE -> excluded.""",
        ),
        (
            "Award finality, consent and limited control",
            "award-effect-map",
            [5, 6],
            """GENUINE COMPROMISE
        |
        v
award -> deemed civil-court decree -> final and binding -> no statutory appeal.

COURT FEE
refund route for referred case under governing law.

LIMITED CONSTITUTIONAL CONTROL
fraud | no genuine consent | jurisdictional defect | natural-justice failure.

Afcons Infrastructure (2010) -> structured ADR referral guidance.

TRAP
finality does not create consent or jurisdiction.""",
        ),
        (
            "Permanent Lok Adalat: public-utility hybrid",
            "pla-hybrid-process",
            [7, 8],
            """PRE-LITIGATION PUBLIC-UTILITY DISPUTE
        |
        v
PLA conciliation
   +----+----+
settlement  failure
   |         |
award       eligible merits decision within statute.

InterGlobe Aviation (2011) -> ordinary/PLA distinction.
Bar Council of India v. Union of India (2012) -> PLA design upheld.
Canara Bank v. G.S. Jayarama (2022) -> conciliation then limited adjudication.

LIMIT
sector + offence bar + current notified pecuniary scope.""",
        ),
        (
            "Operational Lok Adalat forms and digital access",
            "operational-form-grid",
            [9, 10],
            """NATIONAL | MEGA | MOBILE | CONTINUOUS/DAILY | E-LOK ADALAT
        |
administrative mode, scale, mobility or technology
        |
underlying ordinary/PLA legal character remains unchanged.

DIGITAL TEST
identity + private communication + language + disability access
+ document access + offline alternative.

TRAP
online format does not authorise compelled settlement.""",
        ),
        (
            "Gram Nyayalaya: doorstep court with appellate safeguards",
            "gram-nyayalaya-rail",
            [11, 12],
            """GRAM NYAYALAYAS ACT 2008
State establishment + High Court consultation.

NYAYADHIKARI
qualified as Judicial Magistrate First Class.

JURISDICTION
scheduled civil/criminal matters -> local/mobile sittings -> flexible procedure.

APPEAL
criminal -> Sessions Court | civil -> District Court, subject to exceptions.

TRAP
Gram Nyayalaya != Panchayat | khap | mediation camp | Lok Adalat.""",
        ),
        (
            "Family, Commercial, Fast Track, Special and evening courts",
            "court-design-comparison",
            [13, 14],
            """FAMILY COURT
1984 Act -> adjudication + settlement + privacy.

COMMERCIAL COURT
2015 Act -> specified-value commercial disputes + case management.

FAST TRACK / EVENING COURT
capacity or scheduling design under ordinary judicial authority.

SPECIAL COURT
exact parent statute -> subject/person/offence jurisdiction.

Patil Automation (2022)
commercial pre-institution mediation mandatory absent statutory urgent-relief exception.

TRAP
label != constitutional status or common appeal route.""",
        ),
        (
            "Mediation, tribunals and fairness reform",
            "forum-selection-matrix",
            [15],
            """MEDIATION ACT 2023
neutral facilitation -> party-made settlement; verify commencement/rules.

TRIBUNAL
specialised statutory adjudication + constitutional review.

COURT
authoritative judicial hierarchy and appeal.

REFORM TEST
cost + time + consent quality + advice + staff + reasons
+ digital inclusion + compliance + review.

VERDICT
forum must match dispute; disposal volume alone is not justice.""",
        ),
        (
            "UPSC synthesis: access with consent, competence and review",
            "answer-synthesis",
            [1, 4, 8, 12, 15],
            """PRELIMS FIREWALL
Art 39A | 1987 Act | ordinary compromise-only | PLA public-utility hybrid
| deemed decree/finality | Gram/Family statutory courts | forms != new courts.

MAINS SPINE
anchor -> ladder -> ordinary process -> PLA distinction -> other courts
-> mediation/tribunal firewall -> fairness/digital implementation -> reform.

PYQ ROUTE
legal-aid eligibility | NALSA | Lok Adalats versus arbitration.

CONCLUSION
access is constitutional only when proximity is joined to voluntariness and legality.""",
        ),
    ],
    "polity-55": [
        (
            "Interpretive method: from text to disciplined constitutional meaning",
            "interpretive-method-root",
            [1, 2],
            """ROOT QUESTION
How does a court derive meaning without becoming a constituent legislature?

TEXTUAL -> enacted words and context.
STRUCTURAL -> institutional/federal relationships.
HISTORICAL -> framing problem and background.
PURPOSIVE -> effective constitutional object.
PRECEDENT -> binding ratio + bench strength.

CONTROL
provision -> trigger -> test -> case-year -> effect -> limit -> remedy.""",
        ),
        (
            "Article 13 remedies: severability, eclipse and waiver",
            "invalidity-remedy-matrix",
            [3, 4],
            """SEVERABILITY
R.M.D. Chamarbaugwala v. Union of India (1957)
-> separable invalid part falls; workable intended remainder survives.

ECLIPSE
Bhikaji Narain Dhakras (1955)
-> pre-Constitution law dormant to inconsistency, not repealed.

WAIVER
Basheshar Nath (1958)
-> consent cannot validate unconstitutional State action.

TRAP
parts | enforceability | consent are three different questions.""",
        ),
        (
            "Legislative competence: true field before conflict",
            "competence-decision-tree",
            [5, 6],
            """Prafulla Kumar Mukherjee (1947) -> pith and substance.
State of Bombay v. F.N. Balsara (1951) -> incidental/ancillary reach.
K.C. Gajapati Narayan Deo (1953) -> colourable competence, not motive.

STATE EXTRA-TERRITORIAL EFFECT
State of Bombay v. R.M.D. Chamarbaugwala (1957) -> real territorial nexus.

SEQUENCE
entry -> true nature/effect -> incidental overlap -> disguise -> nexus.

TRAP
do not jump to Article 254 before identifying the field.""",
        ),
        (
            "Article 254: occupied field, repugnancy and assent",
            "repugnancy-rail",
            [7, 8],
            """SAME CONCURRENT FIELD?
        |
actual conflict / impossible obedience / intended complete coverage?
        |
Deep Chand v. State of Uttar Pradesh (1959)
        +
M. Karunanidhi v. Union of India (1979)
        |
Union law prevails; State law void to extent of conflict.
        |
Presidential assent -> State law may prevail in that State.
        |
Parliament may later override.

TRAP
assent cannot cure lack of State competence.""",
        ),
        (
            "Meaning, amendment and invalidity boundaries",
            "meaning-remedy-comparison",
            [9, 10],
            """HARMONIOUS CONSTRUCTION
Kerala Education Bill (1958) -> reconcile meaningful operation.

READING DOWN
Kedar Nath Singh (1962) -> choose textually available valid meaning.

PROSPECTIVE OVERRULING
I.C. Golaknath (1967) -> expressly shape temporal effect.

BASIC STRUCTURE
Kesavananda Bharati (1973) + Minerva Mills (1980)
-> Article 368 cannot damage constitutional identity.

LIMIT
interpretation != amendment != judicial policy code.""",
        ),
        (
            "Equality review: presumption, arbitrariness and proportionality",
            "rights-review-ladder",
            [11, 12],
            """Ram Krishna Dalmia (1958) -> rebuttable presumption/classification discipline.
E.P. Royappa (1973) -> arbitrariness and equality.
Shayara Bano (2017) -> manifest arbitrariness of legislation.

PROPORTIONALITY
Modern Dental College (2016)
-> authority + aim + connection + necessity + balance.
K.S. Puttaswamy (2017) + Anuradha Bhasin (2020)
-> structured rights justification in modern settings.

TRAP
review justification; do not choose the court's preferred policy.""",
        ),
        (
            "Morality, transformation and religious-practice caution",
            "values-rights-balance",
            [13, 14],
            """CONSTITUTIONAL MORALITY / TRANSFORMATION
Navtej Singh Johar (2018)
-> equal citizenship, dignity and anti-hierarchy through text and rights.

ESSENTIAL RELIGIOUS PRACTICES
Shirur Mutt (1954)
-> religious matter versus regulable secular activity.

Indian Young Lawyers Association (2018)
-> religion, equality, dignity and morality interaction.

LIMIT
pending review/reference != decided doctrinal change
| constitutional morality != personal morality.""",
        ),
        (
            "Neighbouring doctrines, precedent and judicial restraint",
            "precedent-restraint-map",
            [15],
            """PLEASURE
Shamsher Singh (1974) -> Arts 310-311 + responsible government.

EXPECTATION / ESTOPPEL
Navjyoti Cooperative Group Housing (1992)
| Motilal Padampat Sugar Mills (1978) -> fairness/reliance, no compelled illegality.

CASUS OMISSUS
Padma Sundara Rao (2002) -> genuine omission ordinarily left to legislature.

PRECEDENT / ART 142
Supreme Court Bar Association (1998)
-> ratio + bench strength + proper reference; complete justice remains limited.""",
        ),
        (
            "UPSC synthesis: select doctrine by trigger and legal effect",
            "answer-synthesis",
            [1, 4, 8, 12, 15],
            """PRELIMS FIREWALL
Art 13 validity | Arts 245-246 competence | Art 254 conflict
| Art 368 amendment | Art 141 precedent | Art 142 case-bound complete justice.

MAINS SPINE
method -> trigger -> doctrine sequence -> case + decision year
-> legal effect -> limitation -> calibrated remedy.

PYQ ROUTE
federal supremacy/harmony | constitutional morality | basic structure
| amendments responding to judgments | judicial independence/accountability.

CONCLUSION
doctrine is disciplined reasoning, not a case-name dump or judicial sovereignty.""",
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
    prior.configure_shared_helpers()
    content.TOPICS = TOPICS
    content.SUPPLEMENTS = SUPPLEMENTS
    content.PYQS = PYQS
    content.FACTS = FACTS
    content.MAINS_PROMPTS = MAINS_PROMPTS
    content.PANELS = PANELS
    content.DATE = DATE
    base.PANELS.update(PANELS)


def export_flow(
    config: dict[str, Any],
    expected_count: int,
) -> tuple[Path, dict[str, Any]]:
    """Publish the selected Polity topic without touching concurrent non-Polity work."""
    validation_path = (
        EXPORTS / f"{config['key']}-flow-learning-{DATE}-validation.json"
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "export_flow_learning_library.py"),
            "--subject",
            "Polity",
            "--topic-prefix",
            "polity-",
            "--topic-key",
            config["key"],
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
    if payload["summary"]["topic_folder_count"] != expected_count:
        raise RuntimeError(
            f"{config['key']}: expected {expected_count} Polity Flow topics, "
            f"found {payload['summary']['topic_folder_count']}."
        )
    if not row["hashes"]["pdf"]["equal"] or not row["hashes"]["txt"]["equal"]:
        raise RuntimeError(f"{config['key']}: Flow Learning source bytes changed.")
    return validation_path, row


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
    return content.completed_result(config)


def run() -> dict[str, Any]:
    configure_shared_helpers()
    expected_order = [f"polity-{number:02d}" for number in range(52, 56)]
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
        exclude_polity={52, 53, 54, 55},
    )
    flow_baseline = preserve.flow_topic_hashes(exclude_polity={52, 53, 54, 55})
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        prior.ensure_legacy_reference(config)
        resumed = resume_after_tracker(config, 51 + index)
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
        audit = content.write_audit(config, gate_times["A_started"], live)
        gate_times["A_completed"] = now()

        source_markdown = prior.transform_source(config)
        gate_times["B_completed"] = now()

        workbook_authored = content.workbook_gate(source_markdown, config)
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

        flow_validation, flow_row = export_flow(config, 51 + index)
        flow_folder = ROOT / Path(
            flow_row["destination_folder"].replace("\\", "/")
        )
        gate_times["I_completed"] = now()

        clean_mismatches = preserve.compare_hashes(
            clean_baseline,
            preserve.topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={52, 53, 54, 55},
            ),
        )
        flow_mismatches = preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(exclude_polity={52, 53, 54, 55}),
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
                "original_mains": content.count_original_mains(final_markdown_path),
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
                exclude_polity={52, 53, 54, 55},
            ),
        ),
        "existing_flow_hash_mismatches": preserve.compare_hashes(
            flow_baseline,
            preserve.flow_topic_hashes(exclude_polity={52, 53, 54, 55}),
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
    argparse.ArgumentParser().parse_args()
    state = run()
    print(
        f"topics={len(state['topics'])} order={','.join(state['strict_order'])} "
        f"clean_mismatches={len(state['existing_clean_hash_mismatches'])} "
        f"flow_mismatches={len(state['existing_flow_hash_mismatches'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
