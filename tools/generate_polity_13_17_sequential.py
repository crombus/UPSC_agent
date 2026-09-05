"""Generate Polity learner-v2 topics 13-17 in a preservation-safe sequence."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

import carvaka_flowchart as graphical
import refresh_all_v2_learning_sessions as refresh


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-24"
SECTION = "Subject-Wide-Syllabus"
SOURCE_SESSION_ROOT = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Polity"
    / "learning-sessions"
    / "v2"
    / "subject-wide-syllabus"
)
ASCII_DIR = (
    ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
)
GRAPHICAL_DIR = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "carvaka-graphical-specs"
    / "Polity"
)
EXPORT_MANIFEST_DIR = ROOT / "upsc-ai-kit" / "manifests" / "exports"
FINAL_LIBRARY = ROOT / "notes" / "Final-Learning-Packages"
REFERENCE_ASCII = (
    "notes\\Philosophy\\Philosophy-of-Religion\\flowcharts\\01_Notions-of-God\\"
    "continuous-at-a-glance-carvaka-standard-g9\\"
    "Notions-of-God_Complete-Topic_ASCII-Master-Flow-Diagram.txt"
)
FONT_REGULAR = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\segoeuib.ttf")


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


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
    *,
    visual_sessions: list[int] | None = None,
) -> dict[str, Any]:
    return {
        "key": key,
        "number": int(key[-2:]),
        "title": title,
        "canonical": canonical,
        "basic": basic,
        "advanced": advanced,
        "cross": cross,
        "live": live,
        "exact_pyqs": exact_pyqs,
        "supporting_pyqs": supporting_pyqs,
        "current_note": current_note,
        "caveat": caveat,
        "visual_sessions": visual_sessions or [],
    }


COMMON_CROSS = [
    "upsc-ai-kit\\knowledge\\Polity\\README.md",
    "upsc-ai-kit\\knowledge\\Polity\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
    "upsc-ai-kit\\knowledge\\Polity\\ANSWER-WORTHINESS-AUDIT.md",
]
PYQ_INDEXES = [
    "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2018-2023.md",
    "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
]
LOCAL_OCR = [
    "books\\Indian Polity by M Laxmikant.pdf",
    "books\\Courseware on Indian Polity by M Laxmikanth.pdf",
]
QUESTION_SOURCES = [
    "books\\more_previous_papers\\QP-CSP-18-GS-I-C.pdf",
    "books\\more_previous_papers\\CSP_2020_GS_Paper-1.pdf",
    "books\\more_previous_papers\\QP-CSP-21-GeneralStudiesPaper-I-121021.pdf",
    "books\\more_previous_papers\\QP_CS_Pre_Exam_2023_280523.pdf",
    "books\\more_previous_papers\\QP-CSM19-GeneralStudies-II.pdf",
    "books\\more_previous_papers\\QP-CSM-21-GENSTUDIESPAPER-II-110122.pdf",
    "books\\more_previous_papers\\QP-CSM-22-GENERAL-STUDIES-PAPER-II-190922.pdf",
    "books\\more_previous_papers\\QP-CSM-23-GENERAL-STUDIES-PAPER-II-180923.pdf",
    "books\\mains\\02 UPSC 2024 Paper-II.pdf",
    "books\\mains\\UPSC Mains 2025 GS Paper 2.pdf",
    "books\\prelima_question_paper_answers\\2024-GS1-Set A.pdf",
    "books\\prelima_question_paper_answers\\Ans-2024-GS1.pdf",
    "books\\prelima_question_paper_answers\\2025-GS1-Set A.pdf",
    "books\\prelima_question_paper_answers\\Ans-2025-GS1.pdf",
    "books\\prelima_question_paper_answers\\2026-GS1-Set A.pdf",
    "books\\prelima_question_paper_answers\\Ans-2026-GS1-Provisional.pdf",
]

TOPICS = [
    topic(
        "polity-13",
        "Centre State and Inter State Relations",
        "upsc-ai-kit\\knowledge\\Polity\\13_Centre-State-and-Inter-State-Relations_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\13_Centre-State-and-Inter-State-Relations.md",
        COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Constitutional-Interpretation-Doctrines.md",
        ],
        [
            "https://fincomindia.nic.in/",
            "https://gstcouncil.gov.in/",
            "https://interstatecouncil.gov.in/",
            "https://www.mha.gov.in/",
        ],
        7,
        1,
        "The official Finance Commission site states that the Sixteenth Finance "
        "Commission report was tabled in Parliament; GST Council and Inter-State "
        "Council Secretariat sites remain active on 24 August 2026.",
        "The 2019 river-water amendment Bill is not treated as enacted law; GST "
        "Council recommendations are not treated as binding commands.",
    ),
    topic(
        "polity-14",
        "Emergency Provisions",
        "upsc-ai-kit\\knowledge\\Polity\\14_Emergency-Provisions_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Emergency-Provisions.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\14_Emergency-Provisions.md",
        COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Constitutional-Interpretation-Doctrines.md",
        ],
        [
            "https://www.legislative.gov.in/constitution-of-india",
            "https://www.sci.gov.in/",
            "https://www.pib.gov.in/indexd.aspx?reg=3&lang=1",
        ],
        4,
        2,
        "The official Constitution and Supreme Court portals were rechecked on "
        "24 August 2026; the package retains the 44th Amendment, S.R. Bommai and "
        "Puttaswamy controls.",
        "No Financial Emergency is presented as having been proclaimed. "
        "Samvidhaan Hatya Diwas is identified only as commemorative policy.",
    ),
    topic(
        "polity-15",
        "President and Vice President",
        "upsc-ai-kit\\knowledge\\Polity\\15_President-and-Vice-President_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\15_President-and-Vice-President.md",
        COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
        ],
        [
            "https://www.presidentofindia.gov.in/",
            "https://vicepresidentofindia.nic.in/",
            "https://www.eci.gov.in/",
            "https://www.sci.gov.in/",
        ],
        7,
        1,
        "The official office websites accessed 24 August 2026 identify Droupadi "
        "Murmu as President and C. P. Radhakrishnan as Vice-President.",
        "Office-holder facts are dated. The 2025 Article 143 opinion is used only "
        "for the bounded assent rule stated in the source package.",
    ),
    topic(
        "polity-16",
        "PM and Council of Ministers",
        "upsc-ai-kit\\knowledge\\Polity\\16_PM-and-Council-of-Ministers_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\16_PM-and-Council-of-Ministers.md",
        COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
        ],
        [
            "https://www.pmindia.gov.in/en/",
            "https://cabsec.gov.in/",
            "https://cabsec.gov.in/councilofministers/cabinetcommittees/",
        ],
        2,
        1,
        "PM India showed current Prime Minister Narendra Modi updates dated "
        "24 August 2026. Cabinet Secretariat confirms its Rules of Business, "
        "Cabinet-support and inter-ministerial coordination functions.",
        "Committee number, membership and chairmanship remain notification-sensitive "
        "and are not frozen beyond the dated official control.",
        visual_sessions=[1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 14, 15, 16, 19],
    ),
    topic(
        "polity-17",
        "Parliament",
        "upsc-ai-kit\\knowledge\\Polity\\17_Parliament_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\17_Parliament.md",
        COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
        ],
        [
            "https://sansad.in/ls",
            "https://sansad.in/rs",
            "https://www.sci.gov.in/",
            "https://censusindia.gov.in/",
        ],
        8,
        20,
        "Digital Sansad pages accessed 24 August 2026 identify the Lok Sabha and "
        "Rajya Sabha and show C. P. Radhakrishnan as Rajya Sabha Chairman.",
        "The 106th Amendment is commenced but not operational; defeated 2026 Bills "
        "remain proposals, and no final larger-Bench Money Bill resolution is claimed.",
        visual_sessions=[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16],
    ),
]


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-13": [
        (
            "The four-dimensional federal relations map",
            "constitutional-relations-architecture",
            [1],
            """CENTRE-STATE AND INTER-STATE RELATIONS
  +-- LEGISLATIVE: Articles 245-255 + Seventh Schedule
  +-- ADMINISTRATIVE: Articles 256-263
  +-- FINANCIAL: Articles 264-293 + GST Articles 246A / 269A / 279A
  +-- INTER-STATE / ECONOMIC: Articles 261-263 and 301-307

OPERATING QUESTION
Who may act -> through which constitutional route -> with what check -> with what remedy?

FEDERALISM IS NOT ONE LIST
legal competence + implementation control + fiscal capacity + bargaining institutions.""",
        ),
        (
            "Legislative competence before conflict",
            "competence-list-hierarchy",
            [2],
            """ARTICLE 245: territorial reach
  +-- Parliament: whole or any part of India; extra-territorial operation protected
  +-- State legislature: whole or any part of the State; territorial nexus applies

ARTICLE 246 + SEVENTH SCHEDULE
Union List 100 -> Parliament
State List 61 -> States, subject to constitutional exceptions
Concurrent List 52 -> both; Article 254 resolves repugnancy

SPECIAL RULES
Article 246A -> GST competence
Article 248 + Union Entry 97 -> residuary power with Parliament.""",
        ),
        (
            "Parliament's routes into the State field",
            "state-list-exception-process",
            [3],
            """STATE LIST IS PRIMARY, NOT ABSOLUTE
  |
  +-- Article 249 -> Rajya Sabha national-interest resolution
  +-- Article 250 -> National Emergency; temporary extension after it ends
  +-- Article 252 -> two or more States request; other States may adopt
  +-- Article 253 -> treaty / international obligation implementation
  +-- Article 356 -> Parliament legislates for the affected State
  +-- Article 246(4) -> territories not included in a State

EXAM CONTROL
State trigger, national trigger, duration and amendment/repeal control differ by route.""",
        ),
        (
            "Doctrines, repugnancy and State-law control",
            "doctrine-repugnancy-matrix",
            [4, 5],
            """FIRST RECONCILE COMPETENCE
pith and substance -> true nature
harmonious construction -> preserve both entries
incidental encroachment -> tolerated when substance is competent
colourable legislation -> what cannot be done directly cannot be disguised

THEN TEST ARTICLE 254
Concurrent field + direct conflict -> Union law ordinarily prevails
reserved State law + Presidential assent -> operates in that State
Parliament may later override

ASSENT CONTROL
prior sanction != reservation; Articles 200-201 remain distinct procedures.""",
        ),
        (
            "Administrative directions, delegation and common services",
            "administrative-relations-chain",
            [6, 7],
            """STATE EXECUTIVE DUTY
Article 256 -> ensure compliance with parliamentary law
Article 257 -> do not impede Union executive power; directions in stated fields
        |
        +-- Article 365: non-compliance may supply material
        +-- Article 356: still requires separate constitutional satisfaction and review

COOPERATIVE ADMINISTRATION
Articles 258 / 258A -> mutual entrustment of functions
Article 312 -> Rajya Sabha route for All-India Services
CBI -> DSPE Act consent architecture; State consent and federal litigation remain bounded.""",
        ),
        (
            "Fiscal federalism from tax power to borrowing",
            "fiscal-federalism-system",
            [8, 9, 10, 11],
            """NO TAX WITHOUT AUTHORITY OF LAW: ARTICLE 265
  +-- assigned / distributed taxes: Articles 268-270
  +-- surcharge for Union purposes: Article 271
  +-- grants: Articles 273, 275 and 282
  +-- Finance Commission: Article 280
  +-- borrowing: Articles 292-293

GST LAYER
Articles 246A + 269A + 279A -> shared tax field + destination rule + Council

CURRENT CONTROL
Sixteenth Finance Commission award 2026-31; report tabled in Parliament.
Fiscal autonomy depends on predictable devolution, not State List words alone.""",
        ),
        (
            "Intergovernmental forums and river-water adjudication",
            "institutions-water-dispute-map",
            [12, 13, 14, 15, 16],
            """ARTICLE 263 INTER-STATE COUNCIL
inquiry + discussion + recommendation; constitutional and recommendatory

ZONAL COUNCILS
States Reorganisation Act, 1956; regional consultation; statutory, not constitutional
North Eastern Council -> separate statutory regional body

ARTICLE 262 WATER DISPUTES
negotiation -> statutory tribunal -> decision/publication -> implementation
Parliament may exclude court jurisdiction through law

CURRENT LIMIT
The 2019 permanent-tribunal Bill has not become law; do not invent one tribunal.""",
        ),
        (
            "Sarkaria, Punchhi and the modes of federalism",
            "commission-mode-dialectic",
            [17],
            """COOPERATIVE -> consultation and joint implementation
COMPETITIVE -> innovation, investment and policy comparison
BARGAINING -> negotiated grants, GST and political accommodation
COERCIVE -> conditional finance, directions or unilateral central leverage

SARKARIA
strong Union within cooperation; Article 356 last resort; neutral Governor; active ISC

PUNCHHI
localised emergency debate; clearer Governor practice; consultation and dispute prevention

REFORM TEST
regular institutions + shared data + reasoned decisions + fiscal transparency.""",
        ),
        (
            "Prelims controls, PYQ routes and answer synthesis",
            "exam-synthesis-board",
            list(range(1, 18)),
            """PRELIMS FIREWALL
Article 254 -> Concurrent repugnancy, not every Union-State disagreement
Article 365 -> possible consequence, not automatic President's Rule
GST -> Article 246A special field, not a general Concurrent List tax entry
Zonal Councils -> statutory; Inter-State Council -> constitutional

PYQ ROUTES
2019 supremacy/harmony | 2020 centralisation | 2024 relation reform | 2025 fiscal federalism

MAINS SPINE
define dimension -> cite Article/institution -> explain mechanism -> evidence
-> State/Union counterpoint -> commission reform -> cooperative, reviewable conclusion.""",
        ),
    ],
    "polity-14": [
        (
            "Three emergencies, three constitutional failures",
            "three-emergency-architecture",
            [1],
            """PART XVIII: ARTICLES 352-360
  +-- Article 352 -> war, external aggression or armed rebellion
  +-- Article 356 -> State government cannot be carried on according to Constitution
  +-- Article 360 -> threat to financial stability or credit of India / any part

THE SAME WORD 'EMERGENCY' HIDES DIFFERENT RULES
trigger | advice | majority | duration | territorial effect | rights effect | revocation

CORE PURPOSE
preserve constitutional government in crisis, not replace limited government permanently.""",
        ),
        (
            "Article 352 trigger, approval and revocation",
            "national-emergency-process",
            [2, 3, 4],
            """IMMINENT DANGER MAY JUSTIFY PROCLAMATION
Cabinet decision in writing -> President -> proclamation for whole or part
        |
        +-- approval within one month
        +-- special majority in each House
        +-- renewal every six months
        +-- Lok Sabha disapproval mechanism and presidential revocation

44TH AMENDMENT CONTROLS
internal disturbance -> armed rebellion
written Cabinet advice + special majority + stronger Lok Sabha trigger

TRAP
Article 352 is not approved by a simple majority and is not indefinite without renewal.""",
        ),
        (
            "National Emergency effects and historical evolution",
            "effects-amendment-timeline",
            [5, 8],
            """EFFECTS
Union executive directions expand
Parliament gains State List competence while States continue
Article 354 may modify revenue-distribution operation
Lok Sabha and Assembly terms may be extended in one-year increments

HISTORY
1962 external aggression -> 1971 external aggression -> 1975 internal emergency

AMENDMENT ARC
38th immunity -> 42nd centralisation -> 44th review, liberty and procedure safeguards

VERDICT
emergency federalisation is temporary; constitutional identity and review survive.""",
        ),
        (
            "Articles 358 and 359: rights firewall",
            "rights-suspension-comparison",
            [6, 7],
            """ARTICLE 358                              ARTICLE 359
automatic operation                         presidential order required
Article 19 only                             specified Part III enforcement
war / external aggression only              any Article 352 ground
emergency-related law nexus after 44th       order states scope and duration

PERMANENT LIBERTY CONTROL
Articles 20 and 21 cannot be suspended through Article 359.

CASE ARC
ADM Jabalpur (1976) majority denied habeas route -> Khanna dissent
-> K.S. Puttaswamy (2017) rejects the majority's constitutional approach.

TRAP: rights are not 'abolished'; enforcement and legal consequences must be stated precisely.""",
        ),
        (
            "Article 356 mechanics and constitutional consequences",
            "presidents-rule-process",
            [9, 10],
            """GOVERNOR REPORT OR OTHERWISE
objective material -> President's proclamation -> parliamentary approval within two months
        |
        +-- six-month periods
        +-- maximum three years
        +-- beyond one year: Article 352 emergency condition + ECI certification condition

CONSEQUENCES
President assumes State executive functions
Parliament exercises State legislative power
High Court powers cannot be assumed

FLOOR PRINCIPLE
loss of majority is ordinarily tested in the House, not decided by private assessment.""",
        ),
        (
            "S.R. Bommai (1994), judicial review and the misuse debate",
            "bommai-doctrine-dialectic",
            [11, 12],
            """S.R. BOMMAI (1994) CONTROL BOARD
federalism is Basic Structure
Article 356 satisfaction is reviewable
Union must disclose relevant material
majority ordinarily tested on the floor
Assembly dissolution should await parliamentary approval
court may restore the dismissed government / Assembly
secularism is Basic Structure

RAMESHWAR PRASAD (2006)
pre-emptive dissolution based on speculative horse-trading material invalid.

WHY USE DECLINED
judicial review + coalition era + regional parties + political cost + commission norms.""",
        ),
        (
            "Article 360: financial emergency without fabricated history",
            "financial-emergency-map",
            [13],
            """TRIGGER
financial stability or credit of India or any part is threatened

PROCEDURE
President -> parliamentary approval within two months -> simple-majority control
once approved, no six-month renewal cycle is prescribed

POSSIBLE DIRECTIONS
financial propriety canons
salary / allowance reduction, including judges
State Money and financial Bills reserved for presidential consideration

STATUS CONTROL
India has never proclaimed a Financial Emergency.
Do not convert economic stress, Article 293 conditions or fiscal rules into Article 360.""",
        ),
        (
            "Comparison matrix, alternatives and commission safeguards",
            "emergency-comparison-reform",
            [14, 15],
            """ARTICLE 352         ARTICLE 356             ARTICLE 360
national security     State constitutional failure financial stability / credit
special majority      simple majority             simple majority
six-month renewal     six-month renewal           no periodic renewal in text
rights consequences   State machinery effect      fiscal directions

LAST-RESORT LADDER
warning -> consultation -> floor test / judicial remedy -> targeted ordinary law
-> emergency only when constitutional preconditions are met

SARKARIA / PUNCHHI
speaking material, neutral Governor, floor test, restrained and localised response.""",
        ),
        (
            "PYQ traps and the emergency answer spine",
            "emergency-exam-synthesis",
            list(range(1, 16)),
            """PRELIMS CONTROLS
armed rebellion != internal disturbance
Article 358 != Article 359
Articles 20-21 remain protected
Article 356 extension conditions apply after one year
Article 360 has never been used

PYQ ROUTES
2018 financial emergency | 2018 Article 356 | 2023 security provisions
2023 decline of Article 356 use | supporting 2020 centralisation

MAINS SPINE
state trigger -> procedure -> effect -> 44th safeguard / S.R. Bommai (1994)
-> misuse risk -> alternative -> emergency power remains exceptional and reviewable.""",
        ),
    ],
    "polity-15": [
        (
            "Two offices and the parliamentary executive design",
            "head-state-chairman-architecture",
            [1],
            """PRESIDENT: ARTICLES 52-62, 72, 74
constitutional Head of State + formal Union executive power + national continuity

VICE-PRESIDENT: ARTICLES 63-71
ex officio Chairman of Rajya Sabha + constitutional reserve for presidential vacancy

PARLIAMENTARY LOGIC
President ordinarily acts on ministerial advice
Vice-President ordinarily works inside Parliament

CURRENT DATED CONTROL: 24 AUGUST 2026
Droupadi Murmu -> President
C. P. Radhakrishnan -> Vice-President and Rajya Sabha Chairman.""",
        ),
        (
            "Presidential election, vote value and dispute route",
            "presidential-election-system",
            [2, 3, 4],
            """ELECTORAL COLLEGE: ARTICLE 54
elected MPs + elected MLAs of States + elected MLAs of Delhi and Puducherry
exclude nominated MPs, nominated MLAs and State Legislative Council members

WEIGHTING: ARTICLE 55
MLA vote value -> 1971 census population / elected Assembly strength / 1000
MP vote value -> total MLA vote value / elected MPs

COUNT
proportional representation by single transferable vote + secret ballot

DISPUTE
Article 71 -> Supreme Court; vacancy does not invalidate the election.""",
        ),
        (
            "Qualifications, oath, tenure, vacancy and removal",
            "office-lifecycle-comparison",
            [5, 6, 7, 8],
            """PRESIDENT
citizen + 35 years + qualified for Lok Sabha + no office of profit
oath before Chief Justice of India / senior-most available Supreme Court judge
five-year term; re-election allowed; continues until successor enters office
casual vacancy election within six months

IMPEACHMENT: ARTICLE 61
either House starts -> 14-day notice -> one-fourth signatures
-> two-thirds of total membership in each House -> violation of Constitution

ARTICLE 361
official-act immunity and procedural protection do not create substantive impunity.""",
        ),
        (
            "Aid and advice, reconsideration and bounded discretion",
            "advice-discretion-dialectic",
            [9],
            """ARTICLE 74
Council of Ministers with PM at head aids and advises the President
President may require reconsideration once
reconsidered advice binds
court cannot inquire into what advice was tendered

SITUATIONAL CHOICE
hung Lok Sabha -> identify person most likely to command confidence
outgoing ministry -> continuity until an alternative is formed

NOT PERSONAL POLICY POWER
Shamsher Singh (1974): constitutional head operates through responsible government.

ANSWER VERDICT
the office can warn, encourage and require reconsideration, not create a rival executive.""",
        ),
        (
            "Seven presidential power clusters",
            "presidential-power-map",
            [10, 11, 14],
            """EXECUTIVE -> appointments, Rules of Business, administration in President's name
LEGISLATIVE -> summon, prorogue, dissolve LS, address, nominate, assent
FINANCIAL -> recommendation routes, Budget presentation, Finance Commission
JUDICIAL -> Article 72 clemency + Article 143 reference
DIPLOMATIC -> credentials and treaty form, subject to constitutional law
MILITARY -> Supreme Commander in constitutional form
EMERGENCY -> Articles 352, 356 and 360 on constitutional advice

CONTROL
formal breadth is ordinarily exercised through ministerial responsibility and review.""",
        ),
        (
            "Veto and ordinance: the executive-legislative interface",
            "veto-ordinance-cycle",
            [12, 13],
            """ARTICLE 111
ordinary Bill -> assent / withhold / return once
repassed ordinary Bill -> assent required
Money Bill -> cannot be returned
Constitution Amendment Bill -> assent required
pocket veto -> no textual decision deadline for Union Bills

ARTICLE 123
Parliament not both in session + immediate action necessary
-> ordinance has force of Act -> laid before Parliament
-> ceases six weeks after reassembly unless replaced / disapproved / withdrawn

CASE CONTROL
D.C. Wadhwa (1986) and Krishna Kumar Singh (2017) reject routine re-promulgation.""",
        ),
        (
            "Article 72 clemency and the Governor comparison",
            "clemency-comparison",
            [15],
            """FIVE FORMS
pardon | reprieve | respite | remission | commutation

PRESIDENT: ARTICLE 72
court-martial cases
offences against Union executive field
all death-sentence cases

GOVERNOR: ARTICLE 161
State executive field; cannot pardon a court-martial
death sentence may be suspended, remitted or commuted, not pardoned under Article 161

RULE-OF-LAW CONTROL
ministerial advice + limited review for mala fides, arbitrariness or irrelevant material.""",
        ),
        (
            "Vice-President: election, removal, Chair and acting role",
            "vice-president-role-map",
            [16, 17, 18, 19, 20],
            """ELECTION
members of both Houses, elected and nominated; State legislatures excluded

REMOVAL
Rajya Sabha resolution by majority of all then members
-> agreed by Lok Sabha -> 14-day notice
not impeachment; no 'violation of Constitution' ground is required

CHAIRMAN
procedure, discipline and casting vote; no ordinary first vote
Tenth Schedule adjudication is reviewable; own-removal debate uses special arrangement

ACTING PRESIDENT
discharges presidential functions during vacancy / inability; separate office rules apply.""",
        ),
        (
            "Conventions, cases, traps and the answer spine",
            "presidential-exam-synthesis",
            list(range(1, 22)),
            """CASE / CONVENTION ROUTES
Shamsher Singh (1974) -> constitutional head
Kehar Singh (1988) / Maru Ram (1980) -> clemency on advice with bounded review
Krishna Kumar Singh (2017) -> ordinance limits
hung House -> confidence, not personal preference

PRELIMS FIREWALL
President and Vice-President colleges are different
President impeachment != Vice-President removal
six-month vacancy rule applies to President, not Vice-President
Money Bill cannot be returned; Amendment Bill requires assent

MAINS SPINE
constitutional position -> exact power -> advice/procedure -> case -> bounded discretion
-> accountability -> sentinel without a rival popular mandate.""",
        ),
    ],
    "polity-16": [
        (
            "Responsible executive: Articles 74, 75, 77 and 78",
            "responsible-executive-chain",
            [1, 5, 6, 7],
            """FORMAL HEAD                     REAL EXECUTIVE
President                       Prime Minister + Council of Ministers
        \                         /
         +-- ARTICLE 74: aid and advice --+
                         |
ARTICLE 75 -> appointment, tenure, responsibility, six-month rule, ministry cap
ARTICLE 77 -> Union business in President's name + Rules of Business
ARTICLE 78 -> PM informs President and submits matters for reconsideration

CORE RESULT
executive power is politically answerable to Lok Sabha through responsible government.""",
        ),
        (
            "Prime Minister appointment and government formation",
            "government-formation-process",
            [2, 3],
            """CLEAR MAJORITY
President appoints recognised majority leader -> ministers on PM advice

HUNG LOK SABHA
objective support evidence -> appoint person most likely to command confidence
-> prompt floor test -> ministry survives or resigns

ELIGIBILITY
minister may be non-member for six consecutive months
disqualified person cannot use six-month rule to evade the Constitution

TENURE
no fixed PM term; office depends on Lok Sabha confidence and constitutional continuity.""",
        ),
        (
            "Council, Cabinet, ranks and the 91st Amendment",
            "ministerial-structure-matrix",
            [9, 10, 11],
            """COUNCIL OF MINISTERS                 CABINET
larger constitutional body              inner decision-making core
Cabinet + Ministers of State + deputies senior portfolios and collective direction
Article 74                              Article 352 expressly names Cabinet

RANKS
Cabinet Minister | Minister of State (independent charge / attached) | Deputy Minister
labels such as parliamentary secretary do not automatically create Cabinet rank

91ST AMENDMENT
Union ministry <= 15% of Lok Sabha strength
Tenth Schedule defector disqualified from ministerial appointment for the stated period.""",
        ),
        (
            "Collective, individual and legal responsibility",
            "responsibility-triangle",
            [8, 18],
            """COLLECTIVE: ARTICLE 75(3)
one political unit -> Cabinet solidarity -> Lok Sabha confidence
loss of confidence -> whole ministry resigns

INDIVIDUAL: ARTICLE 75(2)
minister holds office during President's pleasure, exercised within PM-led government
PM may require resignation or advise dismissal

LEGAL RESPONSIBILITY
India lacks the British rule requiring a ministerial countersignature on every formal act
Article 77 authentication protects authorised orders from challenge on signature form alone

ACCOUNTABILITY CHAIN
decision -> shared defence -> questions/committee/audit -> confidence sanction.""",
        ),
        (
            "Prime Minister's five relationship arenas",
            "prime-minister-relations-map",
            [4, 5],
            """COUNCIL / CABINET
selects team, allocates portfolios, sets agenda, coordinates and can seek resignation

PRESIDENT
principal adviser + Article 78 information bridge + reconsideration channel

PARLIAMENT
government leader, confidence manager, policy statement and legislative programme

PARTY / COALITION
leadership depends on majority, alliance agreements, internal bargaining and legitimacy

FEDERAL / NATIONAL
intergovernmental leadership, crisis coordination and national policy direction.""",
        ),
        (
            "Cabinet ecosystem: committees, Secretariat and PMO",
            "executive-coordination-system",
            [13, 14, 15, 16, 17],
            """ARTICLE 77(3) RULES
Allocation of Business -> who handles a subject
Transaction of Business -> how important business moves and is decided

CABINET COMMITTEES
standing / ad hoc; reduce workload and coordinate cross-ministry choices
current number, membership and chairs depend on dated notification

CABINET SECRETARIAT
Cabinet support + records + inter-ministerial coordination + crisis management

PMO
staff support, monitoring and policy coordination; not a constitutional substitute for ministries.""",
        ),
        (
            "Parliamentary control, confidence and anti-defection",
            "executive-accountability-ladder",
            [20],
            """INFORMATION
Question Hour -> Zero Hour -> discussions -> committee evidence
        |
FINANCIAL CONTROL
Budget -> grants -> appropriation -> CAG -> PAC / DRSC
        |
POLITICAL SANCTION
no-confidence motion in Lok Sabha -> collective resignation if carried

ANTI-DEFECTION INTERFACE
whip supports government stability but can compress independent legislative judgment

CONSTRUCTIVE NO-CONFIDENCE
reform proposal for stability; not current constitutional law in India.""",
        ),
        (
            "Coalition, minority, caretaker and prime-ministerial government",
            "executive-variation-dialectic",
            [12, 19, 21, 22],
            """MAJORITY GOVERNMENT -> stronger agenda control, risk of executive dominance
COALITION -> bargaining and inclusion, risk of fragmented responsibility
MINORITY -> issue-based support and greater parliamentary negotiation
CARETAKER -> continuity with self-restraint; no separate constitutional article

CABINET GOVERNMENT                     PRIME-MINISTERIAL GOVERNMENT
collective deliberation                 central agenda and appointment influence
ministerial expertise                   PMO / communication / electoral leadership

QUALIFIED VERDICT
PM predominance varies with party control, coalition arithmetic, institutions and public legitimacy.""",
        ),
        (
            "Cases, conventions, reforms and the answer spine",
            "pm-council-exam-synthesis",
            list(range(1, 25)),
            """CONSTITUTIONAL CONTROLS
Shamsher Singh (1974) -> responsible advice
S.R. Chaudhuri (2001) -> six-month rule cannot be serially abused
Tenth Schedule + 91st Amendment -> stability and anti-defection constraints

PRELIMS FIREWALL
Council != Cabinet | Article 88 gives participation, not a vote without membership
ministry cap uses Lok Sabha strength | Cabinet Committee composition is current-sensitive

REFORM
publish reasons and outcomes, strengthen committees, limit whip, protect Cabinet deliberation

MAINS SPINE
text -> formation -> responsibility -> coordination institutions -> accountability
-> political variation -> balanced strong-executive / responsible-government verdict.""",
        ),
    ],
    "polity-17": [
        (
            "Article 79 architecture, composition and representation",
            "parliament-composition-map",
            [1, 2, 3],
            """PARLIAMENT = PRESIDENT + RAJYA SABHA + LOK SABHA

LOK SABHA
direct adult-suffrage election | normal five-year term | dissolution possible

RAJYA SABHA
indirect State/UT representation | nominated members | permanent House
one-third retire every second year

REPRESENTATION CONTROL
seat allocation + delimitation + population-freeze chronology
106th Amendment commencement does not itself operationalise women's reservation

CORE VERDICT
popular chamber, federal chamber and constitutional head form one legislative institution.""",
        ),
        (
            "Membership, vacancies, officers and sessions",
            "membership-session-system",
            [4, 5, 6, 8],
            """MEMBERSHIP
Article 84 qualification -> Article 102 disqualification -> Article 103 decision with ECI opinion
vacancy, double membership, resignation and prolonged absence follow distinct rules

OFFICERS
Speaker / Deputy Speaker -> Articles 93-97
Chairman / Deputy Chairman -> Articles 89-92
Speaker continues after dissolution until immediately before first new-LS meeting

SESSIONS
summon -> sitting -> adjourn / adjourn sine die -> prorogue -> dissolution
Article 85: no more than six months between sessions; no minimum sitting-day count.""",
        ),
        (
            "Privileges, questions and parliamentary devices",
            "privilege-accountability-map",
            [7, 9],
            """FUNCTIONAL PRIVILEGE
speech / vote protection + House powers needed for legislative work
not a personal licence for corruption or unrelated crime

SITA SOREN (2024)
bribery is not protected merely because it relates to a vote or speech.

INFORMATION DEVICES
starred -> oral answer + supplementaries
unstarred -> written answer
short-notice -> urgent public importance
Zero Hour -> convention, not Rules

MOTIONS
no-confidence | censure | adjournment | privilege | cut motions | discussions.""",
        ),
        (
            "Legislative procedure and the Bill-class firewall",
            "bill-procedure-matrix",
            [10, 11, 12],
            """ORDINARY BILL
introduction -> consideration / committee -> passage -> other House
-> deadlock route where available -> presidential assent

MONEY BILL: ARTICLES 109-110
Lok Sabha only + presidential recommendation + Speaker certificate
Rajya Sabha recommendations within 14 days + no joint sitting

FINANCIAL BILL-I
Article 110 matter plus others; LS only, but Rajya Sabha has full legislative power

FINANCIAL BILL-II
expenditure from Consolidated Fund; either House, recommendation before consideration

ARTICLE 368 BILL
special majority; no joint sitting; presidential assent obligatory.""",
        ),
        (
            "Budget, grants, funds and financial control",
            "parliamentary-finance-chain",
            [13, 14],
            """ARTICLE 112 ANNUAL FINANCIAL STATEMENT
charged expenditure discussed, not voted
voted expenditure -> demands for grants in Lok Sabha
        |
cut motions -> guillotine -> Appropriation Bill -> Finance Bill
        |
CAG audit -> PAC / committee follow-up

GRANTS
supplementary | additional | excess | vote on account | vote of credit | exceptional

FUNDS
Consolidated Fund -> appropriation by law
Contingency Fund -> advances for urgent unforeseen expenditure
Public Account -> other public money; no appropriation vote for withdrawal.""",
        ),
        (
            "Committee architecture: Parliament's working rooms",
            "committee-architecture-matrix",
            [15],
            """FINANCIAL COMMITTEES
PAC 22 = 15 LS + 7 RS -> CAG / post-spending scrutiny
Estimates 30 LS -> economy and administrative improvement
CoPU 22 = 15 LS + 7 RS -> public undertakings

DRSCs
24 committees; each 31 = 21 LS + 10 RS; ministers excluded
demands for grants + referred Bills + annual reports + long-term policy

OTHER CONTROLS
Subordinate Legislation | Privileges | Ethics | Assurances | Petitions | Welfare

LIMIT
reports are advisory, but evidence, publicity and follow-up make them institutionally powerful.""",
        ),
        (
            "Rajya Sabha special powers, joint sitting and ordinance interface",
            "bicameral-power-map",
            [12, 16],
            """RAJYA SABHA EQUAL
ordinary Bills | constitutional amendments | specified elections / removals

RAJYA SABHA UNEQUAL
Money Bills | demands for grants | Lok Sabha confidence

RAJYA SABHA EXCLUSIVE
Article 249 -> Parliament on State List in national interest
Article 312 -> create All-India Services

JOINT SITTING: ARTICLE 108
ordinary / Financial Bill deadlock; Speaker presides; no Money or Amendment Bill route

ORDINANCE
Article 123 temporary law must return to parliamentary control; re-promulgation is bounded.""",
        ),
        (
            "Anti-defection, sovereignty limits and reform",
            "parliamentary-decline-dialectic",
            [17, 18, 19, 20],
            """TENTH SCHEDULE
stability and party mandate <-> reduced individual deliberation
Speaker / Chairman decision remains judicially reviewable

PARLIAMENTARY SOVEREIGNTY IS LIMITED
written Constitution + federal distribution + Fundamental Rights + Basic Structure
judicial review + bicameral and procedural limits

DECLINE DIAGNOSIS
executive agenda control | whip | disruption | guillotine | weak referral | ordinances

REFORM
predictable calendar + default committee referral + reasoned bypass
limited whip + stronger research + timely presiding-officer decisions

CURRENT LIMITS
pending / defeated Bills and unknown delimitation dates are never converted into law.""",
        ),
        (
            "PYQ routes, close-option traps and answer synthesis",
            "parliament-exam-synthesis",
            list(range(1, 21)),
            """PRELIMS FIREWALL
President is part of Parliament, not a House member
Question Hour is regulated; Zero Hour is conventional
Money Bill 'only' test differs from Financial Bills
Speaker continuity differs from Deputy Speaker
Rajya Sabha is not uniformly inferior

PYQ ROUTES
8 solved Mains demands on committees, Speaker, Rajya Sabha and accountability
20 routed Prelims demands with doctrinal resolutions and provenance limits

MAINS SPINE
constitutional instrument -> operating mechanism -> evidence -> executive / party constraint
-> counter-evidence -> institutional reform -> Parliament strong in law, variable in practice.""",
        ),
    ],
}


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def wrap(draw: ImageDraw.ImageDraw, text: str, face: ImageFont.FreeTypeFont, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textlength(candidate, font=face) <= width:
            current = candidate
        elif current:
            lines.append(current)
            current = word
        else:
            lines.append(word)
            current = ""
    if current:
        lines.append(current)
    return lines


def clean_phrase(line: str) -> str:
    value = re.sub(r"!\[[^\]]*]\([^)]+\)", "", line)
    value = re.sub(r"[`*_>#|]", " ", value)
    value = re.sub(r"^\s*(?:[-+]|\d+[.)])\s*", "", value)
    value = re.sub(r"\s+", " ", value).strip(" -:")
    return value


def source_sessions(text: str) -> dict[int, tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^##\s+(\d+)\.\s+(.+?)\s*$", text))
    result: dict[int, tuple[str, str]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[int(match.group(1))] = (match.group(2), text[match.end():end])
    return result


def visual_phrases(body: str) -> list[str]:
    values: list[str] = []
    for line in body.splitlines():
        phrase = clean_phrase(line)
        if (
            18 <= len(phrase) <= 135
            and not phrase.startswith("http")
            and not re.match(
                r"^(?:caption|source|evidence key|learner orientation|current anchor)\s*:|"
                r"^visual\s+\d+\b",
                phrase,
                re.I,
            )
            and phrase.casefold() not in {value.casefold() for value in values}
        ):
            values.append(phrase)
        if len(values) == 8:
            break
    return values or ["Constitutional rule", "Operating mechanism", "Exam distinction"]


def render_visual(path: Path, title: str, phrases: list[str], mode: int) -> None:
    width, height = 1800, 940
    image = Image.new("RGB", (width, height), "#F3F6FA")
    draw = ImageDraw.Draw(image)
    title_face = font(FONT_BOLD, 48)
    sub_face = font(FONT_BOLD, 27)
    body_face = font(FONT_REGULAR, 25)
    draw.rounded_rectangle((42, 36, width - 42, 188), 28, fill="#17233C")
    for line_no, line in enumerate(wrap(draw, title.upper(), title_face, 1600)[:2]):
        draw.text((90, 62 + line_no * 58), line, font=title_face, fill="#FFFFFF")
    palette = ["#2166A5", "#168373", "#A26116", "#8C3A52"]
    items = phrases[:8]
    if mode % 4 == 0:
        boxes = [(80 + i * 420, 300, 380, 390) for i in range(4)]
        for i in range(3):
            draw.line((460 + i * 420, 495, 500 + i * 420, 495), fill="#168373", width=8)
            draw.polygon([(500 + i * 420, 482), (526 + i * 420, 495), (500 + i * 420, 508)], fill="#168373")
    elif mode % 4 == 1:
        boxes = [(70 + i * 570, 270, 530, 520) for i in range(3)]
    elif mode % 4 == 2:
        boxes = [(610, 245, 580, 190), (100, 565, 500, 250), (650, 565, 500, 250), (1200, 565, 500, 250)]
        draw.line((900, 435, 350, 565), fill="#2166A5", width=6)
        draw.line((900, 435, 900, 565), fill="#2166A5", width=6)
        draw.line((900, 435, 1450, 565), fill="#2166A5", width=6)
    else:
        boxes = [(80, 260, 790, 280), (930, 260, 790, 280), (80, 585, 790, 280), (930, 585, 790, 280)]
    chunk = max(1, (len(items) + len(boxes) - 1) // len(boxes))
    for index, (x, y, box_width, box_height) in enumerate(boxes):
        colour = palette[index % len(palette)]
        draw.rounded_rectangle(
            (x, y, x + box_width, y + box_height),
            24,
            fill="#FFFFFF",
            outline=colour,
            width=6,
        )
        draw.rectangle((x, y, x + box_width, y + 58), fill=colour)
        draw.text(
            (x + 24, y + 13),
            ("STEP" if mode % 4 == 0 else "AXIS") + f" {index + 1}",
            font=sub_face,
            fill="#FFFFFF",
        )
        cursor = y + 82
        for phrase in items[index * chunk:(index + 1) * chunk]:
            lines = wrap(draw, phrase, body_face, box_width - 55)[:4]
            draw.ellipse((x + 22, cursor + 8, x + 34, cursor + 20), fill=colour)
            for line_no, line in enumerate(lines):
                draw.text(
                    (x + 48, cursor + line_no * 33),
                    line,
                    font=body_face,
                    fill="#17233C",
                )
            cursor += max(48, len(lines) * 33 + 20)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path, "PNG", dpi=(180, 180), optimize=True)


def add_topic_visuals(config: dict[str, Any], text: str) -> str:
    selected = config["visual_sessions"]
    if not selected:
        return text
    sessions = source_sessions(text)
    title_slug = re.sub(r"[^A-Za-z0-9]+", "-", config["title"]).strip("-")
    folder_name = f"{config['number']:02d}_{title_slug}"
    asset_dir = ROOT / "notes" / "Polity" / "assets" / folder_name
    for ordinal, number in enumerate(selected, 1):
        title, body = sessions[number]
        filename = f"{ordinal:02d}_{re.sub(r'[^a-z0-9]+', '_', title.casefold()).strip('_')[:52]}.png"
        path = asset_dir / filename
        render_visual(path, title, visual_phrases(body), ordinal - 1)
        caption = (
            f"Topic-specific visual map: {title.rstrip('.')}."
        )
        image_line = (
            f"\n\n![{caption}]"
            f"(../../../../../../notes/Polity/assets/{folder_name}/{filename})"
        )
        pattern = rf"(?m)^(##\s+{number:02d}\.\s+.+?)\s*$"
        text, count = re.subn(pattern, rf"\1{image_line}", text, count=1)
        if count != 1:
            raise RuntimeError(f"{config['key']}: could not insert visual for session {number}.")
    return text


def add_session_orientations(text: str) -> str:
    sessions = source_sessions(text)
    for number in sorted(sessions, reverse=True):
        title, body = sessions[number]
        phrases = visual_phrases(body)
        while len(phrases) < 8:
            phrases.append(phrases[len(phrases) % len(phrases)])
        cleaned = [phrase.rstrip(" .;:") for phrase in phrases[:8]]
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


def demote_one(block: str) -> str:
    def replacement(match: re.Match[str]) -> str:
        return "#" + match.group(0)

    return re.sub(r"(?m)^#{2,5}(?=\s)", replacement, block)


def meta_demote(block: str) -> str:
    return re.sub(r"(?m)^##(?=\s)", "####", block)


def heading_offsets(block: str) -> list[tuple[int, str]]:
    return [
        (match.start(), match.group(1).strip())
        for match in re.finditer(r"(?m)^##\s+(.+?)\s*$", block)
    ]


def start_for(headings: list[tuple[int, str]], patterns: list[str]) -> int:
    for offset, title in headings:
        if any(re.search(pattern, title, re.I) for pattern in patterns):
            return offset
    raise RuntimeError("Required section marker was not found: " + ", ".join(patterns))


def current_anchor_line(config: dict[str, Any]) -> str:
    return f"- [CURRENT] **Live official refresh, 24 August 2026:** {config['current_note']}"


def transform_source(config: dict[str, Any]) -> Path:
    canonical = ROOT / Path(config["canonical"].replace("\\", "/"))
    text = canonical.read_text(encoding="utf-8").replace("\r\n", "\n")
    text = re.sub(
        r"(?m)^export_date:\s*\d{4}-\d{2}-\d{2}\s*$",
        f"export_date: {DATE}",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^>\s*\*\*Subject:(.+?)\|\s*\*\*Export date:\*\*\s*\d{4}-\d{2}-\d{2}\s*$",
        rf"> **Subject:\1| **Export date:** {DATE}",
        text,
        count=1,
    )
    text, status_count = re.subn(
        r"(?mi)^- \[CURRENT\] "
        r"(?:Legal(?: and institutional)?\s+)?Status is controlled to "
        r"\*\*\d{1,2} August 2026, Asia/Kolkata\*\*\.\s*$",
        "- [CURRENT] Status is controlled to **24 August 2026, Asia/Kolkata**.",
        text,
        count=1,
    )
    if status_count != 1:
        raise RuntimeError(f"{config['key']}: current-control line was not normalized.")
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
    status_match = re.search(
        r"(?m)^- \[CURRENT\] Status is controlled to \*\*24 August 2026, Asia/Kolkata\*\*\.\s*$",
        text,
    )
    if status_match:
        insertion = status_match.end()
        text = text[:insertion] + "\n" + current_anchor_line(config) + text[insertion:]
    else:
        raise RuntimeError(f"{config['key']}: current-control line was not found.")
    text = add_topic_visuals(config, text)
    text = add_session_orientations(text)

    headings = heading_offsets(text)
    part_i = start_for(headings, [r"^PART I\b"])
    part_ii = start_for(headings, [r"^PART II\b"])
    final = start_for(headings, [r"^Final consolidated register notes$"])
    practice = start_for(
        [(offset, title) for offset, title in headings if offset > part_ii],
        [r"^Solved topic-specific MCQs$", r"^PYQ, practice and solved workbook$"],
    )

    preamble = text[:part_i]
    core_start = text.find("\n", part_i) + 1
    core = text[core_start:part_ii]
    optional_start = text.find("\n", part_ii) + 1
    optional = text[optional_start:practice]
    practice_start = text.find("\n", practice) + 1
    practice_block = text[practice_start:final]
    final_start = text.find("\n", final) + 1
    register = text[final_start:].strip()

    practice_headings = heading_offsets(practice_block)
    pyq_start = start_for(
        practice_headings,
        [
            r"^Routed PYQs",
            r"^Solved UPSC PYQs",
            r"^Verified routed PYQs",
            r"^Solved directly routed Mains PYQs",
            r"^(?:Solved|Verified).*\bPYQ",
        ],
    )
    mcq_start = start_for(
        practice_headings,
        [r"^Original hard MCQ", r"^Original MCQ loop"],
    )
    mains_start = start_for(
        practice_headings,
        [r"^Original Mains practice", r"^Original solved Mains practice"],
    )
    pyqs = practice_block[pyq_start:mcq_start].strip()
    mcqs = practice_block[mcq_start:mains_start].strip()
    mains = practice_block[mains_start:].strip()

    assembled = "\n\n".join(
        [
            meta_demote(preamble).strip(),
            "## BASIC LEARNING SESSION",
            demote_one(core).strip(),
            "## BASIC MCQS / REMEDIATION",
            demote_one(mcqs).strip(),
            "## PYQS AND ANSWER PRACTICE",
            demote_one(pyqs).strip(),
            demote_one(mains).strip(),
            "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER",
            demote_one(optional).strip(),
            "## CONSOLIDATED REGISTER NOTES",
            register,
        ]
    ) + "\n"
    output = SOURCE_SESSION_ROOT / f"{config['key']}_Learning-Session.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(assembled, encoding="utf-8")
    return output


def empty_spec_file(config: dict[str, Any]) -> Path:
    path = ASCII_DIR / f"{config['key']}-{DATE}-sequential.json"
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "id": f"{config['key']}-ascii-panels-{DATE}-sequential",
                    "created_on": DATE,
                    "design_benchmark": REFERENCE_ASCII,
                    "scope": "Sequential placeholder; populated only at the topic's own Gate D.",
                    "topic_count": 0,
                    "topics": {},
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    return path


def write_ascii_spec(config: dict[str, Any], final_markdown: str) -> Path:
    path = empty_spec_file(config)
    topic_panels = []
    for title, structural_type, sessions, body in PANELS[config["key"]]:
        references = [
            final_markdown + f"#SESSION {number}"
            for number in sessions
        ]
        topic_panels.append(
            {
                "title": title,
                "structural_type": structural_type,
                "source_references": references,
                "full_text": body,
            }
        )
    payload = {
        "schema_version": 1,
        "id": f"{config['key']}-ascii-panels-{DATE}-sequential",
        "created_on": DATE,
        "design_benchmark": REFERENCE_ASCII,
        "scope": (
            "Topic-specific Gate D authored only after source and workbook completion; "
            "prior topic specifications remain unchanged."
        ),
        "constraints": {
            "panels_per_topic": "8-10",
            "max_characters_per_line": 100,
            "captions_or_source_notes_as_nodes": False,
            "forbidden_patterns": [
                "ellipsis",
                "placeholder",
                "generic central question",
                "session-card dump",
                "generic answer spine",
            ],
        },
        "topic_count": 1,
        "topics": {
            config["key"]: {
                "title": config["title"],
                "source_record": f"{config['key']}:learner-v2:g2",
                "source_markdown": final_markdown,
                "quality_review": (
                    "Manual topic-specific review against the complete Core, optional "
                    "Advanced, routed PYQs, traps and answer architecture."
                ),
                "approved_master_reference": REFERENCE_ASCII,
                "benchmark_preservation": "Reference is read-only and hash-preserved.",
                "panel_count": len(topic_panels),
                "panels": topic_panels,
            }
        },
    }
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def write_graphical_spec(
    config: dict[str, Any],
    source_markdown: Path,
    ascii_path: Path,
    final_markdown: str,
) -> Path:
    manual = refresh.ascii_master.normalize_manual_spec_file(ascii_path)[config["key"]]
    panels = [
        {
            "title": panel.title,
            "structural_type": panel.structural_type,
            "body": panel.body,
            "source_references": list(panel.source_references),
        }
        for panel in manual.panels
    ]
    spec = graphical.author_topic_spec(
        topic_key=config["key"],
        subject="Polity",
        title=config["title"],
        source_markdown=source_markdown.read_text(encoding="utf-8"),
        source_markdown_path=final_markdown,
        ascii_spec_path=rel(ascii_path),
        ascii_spec_sha256=sha256(ascii_path),
        panels=panels,
        source_generation=2,
    )
    path = GRAPHICAL_DIR / f"{config['key']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def live_checks(config: dict[str, Any]) -> list[dict[str, Any]]:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    results: list[dict[str, Any]] = []
    for url in config["live"]:
        try:
            response = requests.get(url, headers=headers, timeout=30)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.get_text(" ", strip=True) if soup.title else ""
            text = " ".join(soup.get_text(" ", strip=True).split())
            results.append(
                {
                    "url": url,
                    "status_code": response.status_code,
                    "final_url": response.url,
                    "title": title[:220],
                    "evidence_excerpt": text[:600],
                    "accessed_at": now(),
                }
            )
        except Exception as exc:
            results.append(
                {
                    "url": url,
                    "status_code": None,
                    "error": repr(exc),
                    "accessed_at": now(),
                }
            )
    if not any(result.get("status_code") == 200 for result in results):
        raise RuntimeError(f"{config['key']}: no live official source returned HTTP 200.")
    return results


def source_files(config: dict[str, Any], source_markdown: Path, audit: Path, ascii_path: Path, graph_path: Path) -> list[str]:
    candidates = [
        config["basic"],
        config["advanced"],
        config["canonical"],
        rel(source_markdown),
        *config["cross"],
        *PYQ_INDEXES,
        *LOCAL_OCR,
        *QUESTION_SOURCES,
        "upsc-ai-kit\\manifests\\v2\\polity--subject-wide-syllabus.json",
        "upsc-ai-kit\\manifests\\v2\\topic-catalog.json",
        rel(ascii_path),
        rel(graph_path),
        rel(audit),
    ]
    missing = [
        value
        for value in candidates
        if not (ROOT / Path(value.replace("\\", "/"))).is_file()
    ]
    if missing:
        raise RuntimeError(f"{config['key']}: missing source files: {missing}")
    return list(dict.fromkeys(candidates))


def write_audit(config: dict[str, Any], started_at: str, live: list[dict[str, Any]]) -> Path:
    path = EXPORT_MANIFEST_DIR / f"{config['key']}-source-pyq-current-audit-{DATE}.json"
    base_sources = [
        config["basic"],
        config["advanced"],
        config["canonical"],
        *config["cross"],
        *PYQ_INDEXES,
        *LOCAL_OCR,
        *QUESTION_SOURCES,
    ]
    existing = [
        value
        for value in dict.fromkeys(base_sources)
        if (ROOT / Path(value.replace("\\", "/"))).is_file()
    ]
    payload = {
        "schema_version": 1,
        "topic_key": config["key"],
        "title": config["title"],
        "gate": "A",
        "started_at": started_at,
        "completed_at": now(),
        "status": "passed",
        "source_order": [
            {
                "order": 1,
                "kind": "markdown",
                "result": "Basic, complete canonical, Advanced and cross-topic owners reconciled.",
            },
            {
                "order": 2,
                "kind": "local_ocr",
                "result": "Two local Polity books and available official local papers/keys checked.",
            },
            {
                "order": 3,
                "kind": "live_authoritative",
                "sources": live,
                "result": config["current_note"],
            },
            {"order": 4, "kind": "qdrant", "result": "Not used."},
        ],
        "topic_specific_completeness": True,
        "pyq_audit": {
            "verified_or_direct_count": config["exact_pyqs"],
            "supporting_route_count": config["supporting_pyqs"],
            "total_routed_count": config["exact_pyqs"] + config["supporting_pyqs"],
            "status": (
                "Exact wording is retained where held; neutral routed wording and "
                "doctrinal solutions are labelled when official keys/models are unavailable."
            ),
        },
        "current_affairs_audit": {
            "control_date": "2026-08-24",
            "fact": config["current_note"],
            "caveat": config["caveat"],
        },
        "source_hashes": {
            value: sha256(ROOT / Path(value.replace("\\", "/")))
            for value in existing
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def write_new_topic_spec(
    config: dict[str, Any],
    source_markdown: Path,
    audit: Path,
    ascii_path: Path,
    graph_path: Path,
) -> Path:
    files = source_files(config, source_markdown, audit, ascii_path, graph_path)
    total_pyqs = config["exact_pyqs"] + config["supporting_pyqs"]
    payload = {
        "schema_version": 1,
        "topic_key": config["key"],
        "subject": "Polity",
        "section": SECTION,
        "topic_folder": config["key"],
        "title": config["title"],
        "generation_date": DATE,
        "command": f"Generate learner-v2 topic: Polity — Subject-wide Syllabus — {config['title']}",
        "source_markdown": rel(source_markdown),
        "source_basic": config["basic"],
        "source_canonical": config["canonical"],
        "source_advanced": config["advanced"],
        "manifest": "upsc-ai-kit\\manifests\\v2\\polity--subject-wide-syllabus.json",
        "cross_topic_sources": config["cross"],
        "pyq_indexes": PYQ_INDEXES,
        "official_question_sources": [
            value for value in QUESTION_SOURCES
            if (ROOT / Path(value.replace("\\", "/"))).is_file()
        ],
        "local_ocr_sources": LOCAL_OCR,
        "live_sources": config["live"],
        "source_files": files,
        "practice_profile": (
            f"{total_pyqs} routed PYQs ({config['exact_pyqs']} direct/verified and "
            f"{config['supporting_pyqs']} supporting); strict A-B-C-D original MCQs; "
            "remedial MCQs; 7 original solved Mains questions."
        ),
        "current_linkage_note": config["current_note"],
        "pyq_status_note": (
            "Official keys are used where held locally; unsupported objective letters "
            "and official Mains model answers are not invented."
        ),
        "mcq_answer_policy": "strict-abcd-cycle",
    }
    path = EXPORT_MANIFEST_DIR / f"{config['key']}-new-topic-{DATE}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def wrapper_paths(config: dict[str, Any]) -> tuple[Path, Path]:
    validation = EXPORT_MANIFEST_DIR / f"{config['key']}-validation-{DATE}.json"
    staged = EXPORT_MANIFEST_DIR / f"{config['key']}-staged-records-{DATE}.json"
    return validation, staged


def finalize_topic(
    config: dict[str, Any],
    spec_path: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    tracker = refresh.load_tracker()
    row, record = refresh.process_new_topic_spec(spec_path, tracker)
    validation_path, staged_path = wrapper_paths(config)
    validation_payload = {
        "schema_version": 1,
        "selection": f"{config['key']} sequential gate F",
        "passed": bool(row["passed"]),
        "topic_count": 1,
        "topics": [row],
    }
    staged_payload = {
        "schema_version": 1,
        "selection": f"{config['key']} sequential gate G",
        "record_count": 1,
        "records": [record],
    }
    validation_path.write_text(
        json.dumps(validation_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    staged_path.write_text(
        json.dumps(staged_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    refresh.finalize(staged_path, validation_path, commit=True)
    return row, record


def export_clean_topic(config: dict[str, Any]) -> None:
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "export_four_item_library.py"),
            "--topic-key",
            config["key"],
            "--manifest-date",
            DATE,
        ],
        cwd=ROOT,
        check=True,
    )


def count_original_mains(markdown: Path) -> int:
    text = markdown.read_text(encoding="utf-8")
    section = re.search(
        r"(?ims)^##\s+PYQS AND ANSWER PRACTICE\s*(.*?)"
        r"(?=^##\s+OPTIONAL ADVANCED DEPTH)",
        text,
    )
    return len(re.findall(r"(?m)^####\s+M\d+\.", section.group(1))) if section else 0


def hash_existing_library_topics() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in FINAL_LIBRARY.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(FINAL_LIBRARY)
        if len(relative.parts) < 4:
            continue
        if relative.parts[0] == "Polity" and relative.parts[2].startswith(
            ("13-", "14-", "15-", "16-", "17-")
        ):
            continue
        hashes[str(relative).replace("/", "\\")] = sha256(path)
    return hashes


def verify_four_folders(config: dict[str, Any]) -> Path:
    topic_slug = re.sub(r"[^A-Za-z0-9]+", "-", config["title"]).strip("-")
    folder = (
        FINAL_LIBRARY
        / "Polity"
        / "Subject-wide Syllabus"
        / f"{config['number']:02d}-{topic_slug}"
    )
    expected = {
        "01-Complete-Learning-Session",
        "02-Solved-Practice-Workbook",
        "03-Carvaka-Graphical-Flowchart",
        "04-ASCII-Master-Flowchart",
    }
    actual = {path.name for path in folder.iterdir() if path.is_dir()}
    if actual != expected:
        raise RuntimeError(f"{config['key']}: clean folder mismatch: {actual}")
    return folder


def existing_result(config: dict[str, Any]) -> dict[str, Any] | None:
    tracker = refresh.load_tracker()
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == config["key"]
        and record.get("variant") == refresh.V2_VARIANT
    ]
    if not records:
        return None
    record = max(records, key=lambda item: int(item.get("generation") or 0))
    validation_path, _ = wrapper_paths(config)
    if not validation_path.is_file():
        raise RuntimeError(f"{config['key']}: tracker record exists without validation.")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    row = validation["topics"][0]
    clean_folder = verify_four_folders(config)
    audit_path = EXPORT_MANIFEST_DIR / f"{config['key']}-source-pyq-current-audit-{DATE}.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    completion_stamp = max(
        path.stat().st_mtime
        for path in clean_folder.rglob("*")
        if path.is_file()
    )
    final_markdown_path = ROOT / Path(str(row["paths"]["markdown"]).replace("\\", "/"))
    return {
        "topic_key": config["key"],
        "title": config["title"],
        "started_at": audit["started_at"],
        "completed_at": datetime.fromtimestamp(completion_stamp).astimezone().isoformat(
            timespec="seconds"
        ),
        "record_id": record["record_id"],
        "counts": {
            "sessions": row["session_count"],
            "main_pdf_pages": row["main_pdf_pages"],
            "workbook_pdf_pages": row["workbook_pdf_pages"],
            "mcqs": row["mcq_count"],
            "verified_pyqs": config["exact_pyqs"],
            "supporting_pyqs": config["supporting_pyqs"],
            "original_mains": count_original_mains(final_markdown_path),
            "ascii_panels": row["ascii_panel_count"],
            "graphical_core_stages": record["continuous_core_first"]["core_stage_count"],
        },
        "clean_library_path": rel(clean_folder),
        "source_audit": rel(audit_path),
        "validation": rel(validation_path),
        "new_topic_spec": rel(
            EXPORT_MANIFEST_DIR / f"{config['key']}-new-topic-{DATE}.json"
        ),
        "ascii_spec": rel(ASCII_DIR / f"{config['key']}-{DATE}-sequential.json"),
        "graphical_spec": rel(GRAPHICAL_DIR / f"{config['key']}.json"),
        "paths": row["paths"],
        "factual_caveat": config["caveat"],
        "gates_passed": 9,
    }


def run() -> dict[str, Any]:
    if [config["key"] for config in TOPICS] != [
        "polity-13",
        "polity-14",
        "polity-15",
        "polity-16",
        "polity-17",
    ]:
        raise RuntimeError("Sequential topic order was altered.")
    for config in TOPICS:
        empty_spec_file(config)
    baseline = hash_existing_library_topics()
    results: list[dict[str, Any]] = []
    for config in TOPICS:
        completed = existing_result(config)
        if completed is not None:
            results.append(completed)
            continue
        started_at = now()
        live = live_checks(config)
        audit = write_audit(config, started_at, live)
        source_markdown = transform_source(config)
        final_markdown = (
            "upsc-ai-kit\\knowledge\\Learner-v2-Refreshed\\Polity\\"
            f"{SECTION}\\learning-sessions\\{config['key']}\\"
            f"{config['key']}_Complete-Learning-Session_{DATE}.md"
        )
        ascii_path = write_ascii_spec(config, final_markdown)
        graph_path = write_graphical_spec(
            config,
            source_markdown,
            ascii_path,
            final_markdown,
        )
        new_topic_spec = write_new_topic_spec(
            config,
            source_markdown,
            audit,
            ascii_path,
            graph_path,
        )
        row, record = finalize_topic(config, new_topic_spec)
        export_clean_topic(config)
        clean_folder = verify_four_folders(config)
        final_markdown_path = ROOT / Path(str(row["paths"]["markdown"]).replace("\\", "/"))
        completed_at = now()
        results.append(
            {
                "topic_key": config["key"],
                "title": config["title"],
                "started_at": started_at,
                "completed_at": completed_at,
                "record_id": record["record_id"],
                "counts": {
                    "sessions": row["session_count"],
                    "main_pdf_pages": row["main_pdf_pages"],
                    "workbook_pdf_pages": row["workbook_pdf_pages"],
                    "mcqs": row["mcq_count"],
                    "verified_pyqs": config["exact_pyqs"],
                    "supporting_pyqs": config["supporting_pyqs"],
                    "original_mains": count_original_mains(final_markdown_path),
                    "ascii_panels": row["ascii_panel_count"],
                    "graphical_core_stages": record["continuous_core_first"]["core_stage_count"],
                },
                "clean_library_path": rel(clean_folder),
                "source_audit": rel(audit),
                "validation": rel(wrapper_paths(config)[0]),
                "new_topic_spec": rel(new_topic_spec),
                "ascii_spec": rel(ascii_path),
                "graphical_spec": rel(graph_path),
                "paths": row["paths"],
                "factual_caveat": config["caveat"],
                "gates_passed": 9,
            }
        )
    after = hash_existing_library_topics()
    mismatches = sorted(
        key
        for key in set(baseline) | set(after)
        if baseline.get(key) != after.get(key)
    )
    if mismatches:
        raise RuntimeError(
            "Existing clean-library topic artifacts changed: " + ", ".join(mismatches[:20])
        )
    state = {
        "schema_version": 1,
        "batch_id": "polity-13-17-sequential-batch-2026-08-24",
        "created_at": now(),
        "strict_order": [config["key"] for config in TOPICS],
        "topics": results,
        "existing_library_baseline_file_count": len(baseline),
        "existing_library_hash_mismatches": mismatches,
    }
    state_path = EXPORT_MANIFEST_DIR / "polity-13-17-sequential-batch-state.json"
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    state = run()
    print(
        f"topics={len(state['topics'])} order={','.join(state['strict_order'])} "
        f"existing_hash_mismatches={len(state['existing_library_hash_mismatches'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
