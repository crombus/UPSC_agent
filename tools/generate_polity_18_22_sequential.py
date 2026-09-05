"""Generate Polity learner-v2 topics 18-22 in strict preservation-safe order."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import generate_polity_13_17_sequential as base
import polity_flowchart_case_years as case_years


ROOT = base.ROOT
DATE = base.DATE
SECTION = base.SECTION
EXPORTS = base.EXPORT_MANIFEST_DIR
FINAL_LIBRARY = base.FINAL_LIBRARY
FLOW_LIBRARY = ROOT / "notes" / "Flow-Learning"


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
        "polity-18",
        "Supreme Court",
        "upsc-ai-kit\\knowledge\\Polity\\18_Supreme-Court_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\18_Supreme-Court.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Comparative-Constitutional-Schemes.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Constitutional-Interpretation-Doctrines.md",
        ],
        [
            "https://www.sci.gov.in/chief-justice-judges/",
            "https://www.sci.gov.in/collegium-resolutions/",
            "https://www.sci.gov.in/indian-judiciary-annual-report/",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
        ],
        8,
        7,
        "Official Supreme Court pages rechecked on 24 August 2026 continue to "
        "publish the current judges, Collegium Resolutions and annual-report "
        "portals; no undated pendency or vacancy total is frozen.",
        "Justice Surya Kant's office-holder fact is dated. The 20 November 2025 "
        "Article 143 assent opinion is advisory; Article 142 creates neither "
        "rigid assent timelines nor automatic deemed assent.",
        [
            "Articles 124-147, integrated hierarchy, composition, benches and service conditions",
            "collegium evolution, NJAC, independence and accountability",
            "original, writ, appellate, SLP, advisory, review, curative and contempt powers",
            "Articles 141-142 limits, judicial review, basic structure, PIL and access reform",
            "Supreme Court-High Court distinctions, verified cases, traps and answer spines",
        ],
        visual_sessions=[1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 15, 17, 19, 26],
    ),
    topic(
        "polity-19",
        "Governor CM State Council",
        "upsc-ai-kit\\knowledge\\Polity\\19_Governor-CM-State-Council_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\19_Governor-CM-State-Council.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Emergency-Provisions.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
        ],
        [
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
            "https://www.sci.gov.in/",
            "https://www.legislative.gov.in/constitution-of-india/",
        ],
        1,
        8,
        "The official 20 November 2025 Article 143 assent opinion was rechecked "
        "on 24 August 2026; it rejects court-created rigid timelines and "
        "automatic deemed assent while preserving limited review of prolonged inaction.",
        "The 2025 Article 143 opinion is advisory and did not overrule the April "
        "2025 Tamil Nadu judgment. Chancellor powers arise only from the relevant "
        "State law, and the Nabam Rebia Speaker-removal issue remains referred.",
        [
            "Articles 153-167, Governor office, immunity and power classification",
            "aid and advice, bounded discretion, formation, floor tests and Article 356 reporting",
            "Articles 200-201 assent, Article 213 ordinance and Article 161 clemency",
            "Chief Minister, State Council, Advocate General and 91st Amendment controls",
            "Chancellor caveat, Sarkaria-Punchhi reforms and federal-neutrality evaluation",
        ],
        visual_sessions=[1, 2, 3, 5, 6, 8, 10, 11, 13, 14, 16, 18, 20, 24],
    ),
    topic(
        "polity-20",
        "State Legislature",
        "upsc-ai-kit\\knowledge\\Polity\\20_State-Legislature_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\20_State-Legislature.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
        ],
        [
            "https://prsindia.org/billtrack/the-delimitation-bill-2026",
            "https://www.legislative.gov.in/constitution-of-india/",
            "https://censusindia.gov.in/",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
        ],
        2,
        3,
        "Constitution, delimitation and assent controls were rechecked on "
        "24 August 2026. Six States retain Legislative Councils; the 106th "
        "Amendment is commenced but not yet operational.",
        "The failed and withdrawn 2026 delimitation-linked Bills are not law. "
        "No State joint sitting exists, and Article 212 does not immunise "
        "substantive illegality or unconstitutionality from judicial review.",
        [
            "Articles 168-212, unicameral-bicameral design and Article 169",
            "composition, elections, terms, qualification, disqualification and officers",
            "sessions, privileges, devices, committees, budget and financial control",
            "ordinary, Money and financial Bills, Council limits and Governor interface",
            "anti-defection, competence, Article 212 review, comparisons and reform",
        ],
        visual_sessions=[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 20, 23, 27, 30],
    ),
    topic(
        "polity-21",
        "High Court and Subordinate Courts",
        "upsc-ai-kit\\knowledge\\Polity\\21_High-Court-and-Subordinate-Courts_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\21_High-Court-and-Subordinate-Courts.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
        ],
        [
            "https://doj.gov.in/",
            "https://dashboard.doj.gov.in/hc_vacancies/",
            "https://ecourts.gov.in/ecourts_home/",
            "https://www.sci.gov.in/collegium-resolutions/",
        ],
        0,
        4,
        "Department of Justice, eCourts and Supreme Court appointment portals "
        "were rechecked on 24 August 2026. Dynamic vacancy and pendency figures "
        "remain dated; no All India Judicial Service has been created.",
        "India has 25 High Courts as a dated institutional fact. eCourts Phase III "
        "is an implementation programme, not proof that the digital divide or "
        "pendency has been solved.",
        [
            "Articles 214-237, High Court judges, independence, transfer and temporary judges",
            "original, appellate, writ, territorial, supervisory and control jurisdictions",
            "Article 226-32 distinction, judicial review and court-of-record powers",
            "Articles 233-235 subordinate judiciary, Article 50 and bounded Gram Nyayalayas",
            "tribunals, AIJS debate, vacancies, eCourts, comparisons and answer spines",
        ],
        visual_sessions=[1, 2, 3, 5, 7, 9, 11, 13, 16, 20, 24, 28, 32, 36],
    ),
    topic(
        "polity-22",
        "Special Provisions",
        "upsc-ai-kit\\knowledge\\Polity\\22_Special-Provisions_Complete-Topic-Package.md",
        "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions.md",
        "upsc-ai-kit\\knowledge\\Polity\\advanced\\22_Special-Provisions.md",
        base.COMMON_CROSS
        + [
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Union-Territories.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Citizenship.md",
        ],
        [
            "https://api.sci.gov.in/supremecourt/2019/29796/29796_2019_1_1501_49019_Judgement_11-Dec-2023.pdf",
            "https://www.jk.gov.in/",
            "https://ladakh.gov.in/",
            "https://www.legislative.gov.in/constitution-of-india/",
        ],
        1,
        4,
        "The official Article 370 judgment and current Jammu and Kashmir and "
        "Ladakh government portals were rechecked on 24 August 2026. Articles "
        "371-371J remain distinct operative State-specific safeguards.",
        "Article 370 remains printed but is inoperative after the 2019 measures "
        "upheld in 2023. Jammu and Kashmir Statehood has not been restored; "
        "Ladakh protection demands are proposals, not enacted constitutional change.",
        [
            "catalogue-owned Part XXI scope and relevant Articles 369-392 distinctions",
            "Article 370 evolution, 2019 mechanisms and 2023 judgment with open questions",
            "Articles 371-371J State-specific institutions, customs, land and opportunity",
            "Presidential Order and amendment routes; current operative status",
            "Fifth-Sixth Schedule boundary, federalism-equality debate, traps and answers",
        ],
        visual_sessions=[1, 2, 3, 5, 7, 9, 12, 15, 18, 21, 24, 27, 31, 36],
    ),
]


PANELS: dict[str, list[tuple[str, str, list[int], str]]] = {
    "polity-18": [
        (
            "Apex court inside one integrated judicial hierarchy",
            "integrated-judiciary-architecture",
            [1, 2],
            """ARTICLES 124-147, PART V
  +-- Supreme Court: constitutional apex + final appellate court
  +-- High Courts: State-level constitutional courts
  +-- subordinate courts: ordinary trial and first-appeal structure

INTEGRATED DOES NOT MEAN UNITARY ADMINISTRATION
Article 141 promotes legal uniformity; Articles 226, 227 and 235 preserve local access and control.

STRUCTURE CARD
sanctioned strength 34 including CJI | retirement 65 | seat Delhi under Article 130
Article 145(3) -> at least five judges for a substantial constitutional question.""",
        ),
        (
            "Appointment power, collegium evolution and the NJAC test",
            "appointment-doctrine-timeline",
            [3, 4],
            """ARTICLE 124 TEXT -> President appoints after constitutionally required consultation.

DOCTRINE TIMELINE
First Judges Case (1981) -> executive primacy
Second Judges Case (1993) -> judicial primacy; collegium created
Third Judges Case (1998) -> CJI + four senior-most judges for Supreme Court appointments
99th Amendment + NJAC Act, 2014 -> commission model
Fourth Judges Case (2015) -> NJAC invalid; collegium restored

REFORM TEST
transparent criteria + diversity + timely processing, without executive capture of adjudication.""",
        ),
        (
            "Qualifications, tenure, removal and independence firewall",
            "judge-service-independence-map",
            [5, 6, 7],
            """QUALIFICATION
Indian citizen + five years as High Court judge OR ten years as High Court advocate
OR distinguished jurist in the President's opinion.

SERVICE
constitutional oath -> secure tenure to 65 -> charged expenditure -> protected conditions
post-retirement practice prohibited before any court or authority in India.

REMOVAL
proved misbehaviour or incapacity -> special majority in each House -> presidential order.

INDEPENDENCE + ACCOUNTABILITY
security, salary and contempt power -> decisional autonomy
declaration of assets, in-house process and reasoned appointments -> public legitimacy.""",
        ),
        (
            "Jurisdiction gateway: choose the constitutional route first",
            "jurisdiction-selection-matrix",
            [8, 9, 10, 11, 12],
            """FEDERAL DISPUTE -> Article 131 original jurisdiction; legal-right dispute is essential.
FUNDAMENTAL RIGHT -> Article 32; itself a Fundamental Right.
GENERAL PUBLIC-LAW WRONG -> High Court Article 226 is wider in cause and territorial reach.
CONSTITUTIONAL APPEAL -> Article 132 | civil -> 133 | criminal -> 134.
SPECIAL LEAVE -> Article 136 extraordinary discretion, not a regular fourth appeal.
ADVISORY -> Article 143; opinion is advisory and normally non-binding.

CURRENT ASSENT CONTROL
State of Tamil Nadu v. Governor of Tamil Nadu (2025) used timelines and deemed assent on its facts.
In re Assent, Withholding or Reservation of Bills (2025) is a non-binding advisory opinion:
no rigid court-made timelines or automatic deemed assent; prolonged inaction remains reviewable.""",
        ),
        (
            "Review, curative power, court of record and contempt",
            "finality-correction-contempt-system",
            [13, 14],
            """ARTICLE 137 REVIEW
error-control within prescribed grounds -> finality remains the rule.

CURATIVE PETITION
Rupa Ashok Hurra (2002) -> rare post-review cure for grave miscarriage
-> no routine second review.

ARTICLE 129 COURT OF RECORD
authoritative records + power to punish contempt.

CONTEMPT LIMIT
fair criticism is not contempt; power protects administration of justice.
Supreme Court Bar Association (1998) -> Article 142 cannot replace the governing disciplinary law.""",
        ),
        (
            "Precedent, complete justice, assistance and bench discipline",
            "precedent-complete-justice-limits",
            [15, 16],
            """ARTICLE 141
ratio decidendi of Supreme Court law binds all courts; obiter persuades, not identically binds.
larger Bench > smaller Bench; coordinate Bench ordinarily refers disagreement.

ARTICLE 142
complete justice in the cause or matter before the Court
  +-- fills remedial gaps
  +-- cannot ignore substantive statutory or constitutional limits
  +-- does not create a free-standing legislative power.

ARTICLE 144 -> all civil and judicial authorities act in aid.
ARTICLE 145 -> Court rules; five-judge floor for Article 143 and substantial interpretation.
Articles 126-128 -> acting CJI, ad hoc judges and retired-judge sittings are distinct routes.""",
        ),
        (
            "Judicial review, Basic Structure, Ninth Schedule and tribunals",
            "constitutional-review-doctrine-chain",
            [17, 18],
            """CONSTITUTIONAL SUPREMACY -> judicial review of law and executive action.

DOCTRINE CHAIN
Kesavananda Bharati (1973) -> amendment power cannot damage Basic Structure
Minerva Mills (1980) -> limited amendment power + Parts III-IV harmony
I.R. Coelho (2007) -> post-24 April 1973 Ninth Schedule laws face Basic Structure review

TRIBUNALS
specialised adjudication may supplement courts.
L. Chandra Kumar (1997) -> High Court Article 226/227 and Supreme Court Article 32 review
remain part of the Basic Structure; tribunals cannot become total constitutional substitutes.""",
        ),
        (
            "PIL, activism, restraint and social-transformation controls",
            "pil-activism-dialectic",
            [19, 20, 21, 22],
            """ACCESS EXPANSION
Hussainara Khatoon (1979) -> speedy trial and undertrial justice
epistolary jurisdiction + relaxed standing -> collective-rights access
continuing mandamus -> monitored compliance where ordinary relief is inadequate.

JUDICIAL LEGISLATION
Vishaka (1997) -> interim norm in a legal vacuum, anchored in rights and international law.

CONTROL BOARD
rights failure + legal vacuum may justify calibrated relief
BUT policy merits, polycentric choices and institutional capacity require restraint.

ENVIRONMENT
Article 21 + principles + statutory review -> constitutionalisation without replacing regulators.""",
        ),
        (
            "Comparisons, delivery deficits, traps and the Mains spine",
            "supreme-court-exam-synthesis",
            [23, 24, 25, 26],
            """INDIA-UK
written supreme Constitution + strong review versus parliamentary sovereignty under UK doctrine.

INDIA-USA
collegium-led recommendation versus presidential nomination and Senate confirmation.

DELIVERY CHAIN
legal authority -> affordable filing -> timely hearing -> reasoned order -> implementation.
technology helps listing, e-filing and access; it does not itself cure vacancies or exclusion.

PRELIMS FIREWALL
Article 32 narrower in cause than 226 | Article 136 discretionary | Article 143 advisory
Article 142 is bounded | Constitution Bench minimum five, not every constitutional plea.

MAINS SPINE
define role -> cite Article -> explain mechanism -> case with year -> limit -> access reform
-> independent, accountable and institutionally restrained constitutional-court conclusion.""",
        ),
    ],
    "polity-19": [
        (
            "Responsible State government under Articles 153-167",
            "state-executive-architecture",
            [1],
            """PEOPLE -> LEGISLATIVE ASSEMBLY -> CONFIDENCE -> CM + COUNCIL
                                      |
                                      v
                           GOVERNOR GIVES LEGAL FORM

ARTICLE MAP
153 Governor | 154 executive power | 155 appointment | 156 term/pleasure
157 qualification | 158 conditions | 159 oath | 161 clemency | 163 advice/discretion
164 ministers/responsibility | 165 Advocate General | 166 business | 167 CM duties.

CORE RULE
Governor is constitutional head; the confidence-holding ministry is the real political executive.""",
        ),
        (
            "Appointment, tenure, oath, conditions and immunity",
            "governor-office-conditions",
            [2, 3, 4],
            """ENTRY
President appoints by warrant -> Indian citizen + 35 years -> Article 159 oath before HC CJI
or the senior-most available judge.

CONDITIONS
no Parliament/State-legislature seat | no other office of profit | protected emoluments.

TENURE
nominal five years + President's pleasure + resignation to President + hold office until successor.
Pleasure does not convert the office into an ordinary Union employee.

ARTICLE 361
personal immunity for official acts while remedies against government action remain available;
criminal proceedings cannot continue during the term; civil notice rules are distinct.""",
        ),
        (
            "Executive, legislative, financial, judicial and statutory powers",
            "governor-power-classification",
            [5, 6, 7],
            """EXECUTIVE
appoint CM; appoint ministers on CM advice; appoint Advocate General and specified authorities.

LEGISLATIVE
summon, prorogue, dissolve Assembly; address; nominate where text permits; assent/reserve/return.

FINANCIAL
recommend Money Bill and demands; cause budget to be laid; use Contingency Fund under law.

JUDICIAL
Article 161 clemency for offences within State executive field; judicial review survives.

STATUTORY ROLE
Governor as university Chancellor exists only where the relevant State statute so provides.
It is not an inherent power flowing from Articles 153-167.""",
        ),
        (
            "Aid and advice with a narrow, reviewable discretion field",
            "advice-discretion-case-matrix",
            [8, 9],
            """DEFAULT
Shamsher Singh (1974) -> Governor ordinarily acts on ministerial aid and advice.

BOUNDED EXCEPTIONS
hung House formation | floor-test trigger on objective material | Bill reservation
| Article 356 report | express constitutional or necessary situational discretion.

SESSION CONTROL
Nabam Rebia (2016) -> Articles 174-175 ordinarily advice-bound.
Subhash Desai (2023) -> no floor test merely to arbitrate an internal party dispute.
The Speaker-removal issue from Nabam Rebia (2016)
was referred in Subhash Desai (2023) and remains pending.

REVIEW
discretion is not personal political preference; relevance, purpose and objective material matter.""",
        ),
        (
            "Government formation, floor test, dismissal and dissolution",
            "confidence-crisis-process",
            [10, 11, 12],
            """HUNG ASSEMBLY
invite person most likely to command confidence -> early floor test -> no secret Raj Bhavan count.

LOSS OF MAJORITY
objective material -> floor test as ordinary constitutional forum.
S.R. Bommai (1994) -> majority normally proved in House; Article 356 is reviewable.
Subhash Desai (2023) -> factional dissent alone cannot justify a floor test.

DISMISSAL / DISSOLUTION
ministry losing a floor test may resign or face dismissal;
dissolution advice is not mechanically binding
when an alternative government is feasible.
Rameshwar Prasad (2006) -> speculative horse-trading material
cannot justify pre-emptive dissolution.""",
        ),
        (
            "Articles 200-201: assent, return, reservation and current control",
            "assent-reservation-gateway",
            [13, 14, 15],
            """ARTICLE 200 OPTIONS
assent | withhold | return a non-Money Bill once | reserve for President.
Mandatory reservation applies where the Bill endangers the High Court's constitutional position.

AFTER RECONSIDERATION
the Governor cannot return the same Bill again; reservation questions remain text-specific.

ARTICLE 201
President may assent, withhold, or direct return of a non-Money Bill through the Governor.

CURRENT CASE CONTROL
State of Tamil Nadu v. Governor of Tamil Nadu (2025)
-> timelines and deemed assent used on the facts.
In re Assent, Withholding or Reservation of Bills (2025): advisory and non-binding;
no rigid timelines or automatic deemed assent, but prolonged unexplained inaction is reviewable.""",
        ),
        (
            "Ordinance necessity and clemency limits",
            "ordinance-clemency-comparison",
            [16, 17],
            """ARTICLE 213 ORDINANCE
legislature not in session as constitutionally required + immediate action necessary
-> Act-like force -> laying -> ceases six weeks after reassembly unless approved earlier.

RE-PROMULGATION CONTROL
D.C. Wadhwa (1986) -> routine serial re-promulgation is a fraud on the Constitution.
Krishna Kumar Singh (2017) -> laying is mandatory; satisfaction is reviewable;
legislative supremacy bars automatic enduring effects of every lapsed ordinance.

ARTICLE 161
State-field offences; advice-bound clemency; relevant-material and non-arbitrariness review.
Unlike Article 72, it has no court-martial limb and no independent Union-law offence limb.""",
        ),
        (
            "Chief Minister, State Council, Advocate General and Chancellor",
            "state-real-executive-system",
            [18, 19, 20, 21, 22, 23],
            """CHIEF MINISTER
Governor appoints -> prove Assembly confidence -> choose portfolios/ministers
-> coordinate policy -> advise sessions/dissolution -> communicate under Article 167.

STATE COUNCIL
collectively responsible to Assembly
| minister individually holds office during Governor's pleasure,
constitutionally mediated by CM advice and collective responsibility.

91ST AMENDMENT
ministry cap = 15% of Assembly strength; minimum 12; defector-minister bar.
Tribal Welfare Minister requirement applies to the constitutionally specified States.

ADVOCATE GENERAL
Article 165 law officer; qualifications of a High Court judge; advises State government.

CHANCELLOR
State-statute office only; powers and advice rules vary with the governing State law.""",
        ),
        (
            "Federal neutrality, commission reforms, traps and answer spine",
            "governor-federal-synthesis",
            [24, 25, 26],
            """FAULT LINES
Union appointment + pleasure tenure + State-facing powers -> risk of partisan perception.

SARKARIA / PUNCHHI ROUTE
eminent detached appointee | CM consultation | secure convention | floor-test priority
| reasoned Article 356 material | restrained assent/reservation | post-tenure neutrality.

PRELIMS FIREWALL
Governor elected? NO | five-year term guaranteed? NO | discretion general? NO
Chancellor constitutional? NO | Money Bill returnable? NO | Article 361 = State immunity? NO.

MAINS SPINE
state textual power -> advice default -> exceptional trigger -> case with year
-> federal-risk counterpoint -> commission reform -> neutral constitutional-umpire conclusion.""",
        ),
    ],
    "polity-20": [
        (
            "Articles 168-212 and the choice between one House and two",
            "state-legislature-architecture",
            [1, 2, 3],
            """ARTICLE 168
Governor + Legislative Assembly in every State
  +-- Legislative Council only in a bicameral State.

ARTICLE 169 CREATION / ABOLITION
Assembly special resolution -> Parliament ordinary law -> no Article 368 amendment procedure.
Parliament is enabled, not legally compelled, by the State resolution.

CURRENT MAP
six Council States: Andhra Pradesh, Telangana, Uttar Pradesh, Bihar, Maharashtra, Karnataka.

DESIGN VERDICT
Assembly carries direct democratic confidence; Council supplies revision and continuity,
but cannot become a co-equal veto chamber.""",
        ),
        (
            "Composition, election, duration and membership controls",
            "membership-election-matrix",
            [4, 5, 6, 7],
            """ASSEMBLY
direct election | normal five-year term | minimum age 25 | dissolution possible.

COUNCIL
indirect mixed composition under Article 171 | permanent House | one-third retire every two years
| minimum age 30 | total strength normally not more than one-third of Assembly, minimum 40.

COUNCIL ELECTORAL STREAMS
local authorities 1/3 | graduates 1/12 | teachers 1/12 | Assembly members 1/3
| Governor nominates remainder for specified knowledge/experience.

MEMBERSHIP
Article 191 disqualification -> Article 192 Governor decision after ECI opinion;
Tenth Schedule questions follow the presiding-officer route.""",
        ),
        (
            "Presiding officers, sessions, quorum and voting",
            "house-procedure-system",
            [8, 9, 10, 11],
            """OFFICERS
Assembly Speaker/Deputy Speaker | Council Chairman/Deputy Chairman.
removal requires notice and the constitutional majority stated for the House.

SESSION CHAIN
Governor summons -> sitting -> adjournment / adjournment sine die -> prorogation
-> Assembly alone may be dissolved.
No more than six months may intervene between sessions.

QUORUM
ten members or one-tenth of total membership, whichever is greater.

VOTING
members present and voting -> presiding officer ordinarily no first vote
-> casting vote on equality; vacancies do not invalidate otherwise lawful proceedings.""",
        ),
        (
            "Privileges, questions, motions and procedural accountability",
            "privilege-device-accountability-map",
            [12, 13, 14],
            """ARTICLE 194 PRIVILEGE
functional protection for speech, vote and legislative work; not a personal criminal licence.
Sita Soren (2024) -> bribery is not protected merely because it relates to a vote or speech.

JUDICIAL CONTROL
Raja Ram Pal (2007) -> privilege and expulsion powers remain reviewable for illegality,
unconstitutionality, mala fides or substantive procedural violation.

ACCOUNTABILITY DEVICES
questions | short-duration discussion | calling attention | adjournment motion
| no-confidence/censure | privilege motion | cut motions.

CORE DISTINCTION
no-confidence tests ministry survival in the Assembly; Council cannot make or unmake the ministry.""",
        ),
        (
            "Ordinary, Money and financial Bills across unequal Houses",
            "bill-procedure-comparison",
            [15, 16, 17, 18, 19],
            """ORDINARY BILL IN BICAMERAL STATE
either House may originate -> Council may delay first passage up to three months
-> Assembly repasses -> Council may delay up to one month
-> Assembly ultimately prevails; no State joint sitting.

MONEY BILL
Assembly only + Governor's recommendation -> Speaker certificate
-> Council has 14 days and recommendations only -> Assembly may accept or reject.

FINANCIAL BILLS
identify the constitutional category; not every Bill involving money is a Money Bill.

ASSENT GATE
Article 200 assent/withhold/return non-Money Bill/reserve
-> Article 201 presidential route for reserved Bills.""",
        ),
        (
            "Budget, funds, committees and executive scrutiny",
            "financial-control-committee-system",
            [20, 21, 22, 23],
            """ANNUAL FINANCIAL STATEMENT
charged expenditure discussed but not voted
-> demands for grants voted only by Assembly
-> appropriation authorises withdrawal from Consolidated Fund
-> Finance Bill completes taxation changes.

FUNDS
Consolidated Fund | Contingency Fund | Public Account: distinct custody and vote rules.

COMMITTEE CHAIN
Public Accounts Committee -> appropriation and audit
Estimates Committee -> economy and policy efficiency
Public Undertakings Committee -> State enterprise scrutiny
Departmental/subject committees -> detailed examination.

CONTROL TEST
budget power matters only when members receive time, data, research and follow-up compliance.""",
        ),
        (
            "Anti-defection and the ordinance-legislature interface",
            "defection-ordinance-interface",
            [24, 25, 26],
            """TENTH SCHEDULE
voluntary giving up | whip breach without permission/condonation | independent joins party
| nominated member joins after six months -> disqualification routes.

ADJUDICATION
Speaker/Chairman decides, subject to judicial review.
Kihoto Hollohan (1992) -> review survives after the decision on recognised grounds.
Nabam Rebia (2016) decided several Governor/Speaker questions;
its Speaker-removal issue was referred in Subhash Desai (2023) and remains unresolved.

ARTICLE 213 INTERFACE
ordinance is a temporary necessity bridge when the session condition is met;
it must return to legislative scrutiny and cannot become a parallel ordinary lawmaking cycle.""",
        ),
        (
            "Legislative competence and Article 212's limited shield",
            "competence-review-boundary",
            [27],
            """COMPETENCE FIRST
Article 246 + Seventh Schedule + special fields -> pith and substance
-> incidental encroachment -> repugnancy where the Concurrent field applies.

ARTICLE 212
court does not invalidate proceedings merely for procedural irregularity
BUT substantive illegality, constitutional violation and jurisdictional error remain reviewable.

ASSENT CURRENT CONTROL
State of Tamil Nadu v. Governor of Tamil Nadu (2025) used timelines/deemed assent on its facts.
In re Assent, Withholding or Reservation of Bills (2025) is advisory and non-binding:
no rigid timelines or automatic deemed assent; prolonged unexplained inaction may be reviewed.

PRIVILEGE, SPEAKER CERTIFICATION AND DEFECTION ARE NOT REVIEW-FREE ZONES.""",
        ),
        (
            "Assembly-Council comparison, current reforms and answer synthesis",
            "state-legislature-exam-synthesis",
            [24, 25, 26, 27],
            """ASSEMBLY                         COUNCIL
direct mandate                    indirect mixed representation
confidence and grants             revision and continuity
may be dissolved                  permanent
final ordinary-Bill control       maximum delaying power
Money Bill dominance              recommendations within 14 days

CURRENT CONTROLS
106th Amendment commenced but awaits census-linked delimitation for operation.
The failed/withdrawn 2026 Bills are proposals, not law; Census 2027 dates do not fix delimitation.

MAINS SPINE
define chamber design -> cite Article -> compare power -> evidence/problem
-> representation/productivity reform -> stronger committees and sitting calendars
-> effective State legislatures as institutions of representative federalism.""",
        ),
    ],
    "polity-21": [
        (
            "One hierarchy, constitutionally significant High Courts",
            "judicial-hierarchy-map",
            [1, 2, 3, 4],
            """SUPREME COURT
     |
HIGH COURT: constitutional court + appellate court + judicial administrator
     |
DISTRICT AND SUBORDINATE COURTS: ordinary civil/criminal justice.

ARTICLES 214-231 -> High Courts | ARTICLES 233-237 -> subordinate courts.

CURRENT STRUCTURE
25 High Courts; Parliament may establish a common High Court for two or more States/UTs.

INTEGRATED DOES NOT ERASE DECENTRALISED CONTROL
High Court Article 226 access + Article 227 superintendence + Article 235 control
make it the everyday constitutional and administrative court within its territory.""",
        ),
        (
            "High Court appointments, qualification and independence",
            "high-court-judge-service-map",
            [5, 6, 7, 8],
            """ARTICLE 217 APPOINTMENT
President appoints after the constitutionally required consultation architecture
operating through the higher-judiciary collegium system.

QUALIFICATION
Indian citizen + ten years in judicial office OR ten years as High Court advocate.

SERVICE
oath before Governor or appointee | retirement 62 | removal through Article 124(4)-type route
| protected salary and conditions | charged expenditure | post-retirement practice limits.

APPOINTMENT CASE ARC
First Judges Case (1981) -> executive primacy
Second Judges Case (1993) -> judicial primacy
Third Judges Case (1998) -> plural collegium
Fourth Judges Case (2015) -> NJAC invalid; collegium remains operative.""",
        ),
        (
            "Transfer, acting/additional judges and common High Courts",
            "temporary-judge-transfer-system",
            [9, 10, 11, 12],
            """ARTICLE 222 TRANSFER
President transfers after CJI consultation; public interest and judicial independence govern.
Sankalchand Himmatlal Sheth (1977) -> transfer power exists;
consultation must be full and effective.

TEMPORARY CAPACITY
Article 223 acting Chief Justice
Article 224 additional and acting judges for arrears or temporary need
Article 224A retired-judge sitting with consent
Article 231 common High Court by parliamentary law.

TRAPS
additional judge is not a lower rank | common High Court does not merge States
| transfer is not ordinary executive service management | vacancy data are dynamic.""",
        ),
        (
            "Original, appellate, writ and territorial jurisdiction",
            "high-court-jurisdiction-gateway",
            [13, 14, 15, 16, 17, 18],
            """ORIGINAL
constitutional/statutory matters and specified civil jurisdictions depend on law and court history.

APPELLATE
civil + criminal appeals from subordinate hierarchy;
death sentence requires High Court confirmation.

ARTICLE 226 WRIT
Fundamental Rights + any other legal right; habeas corpus may reach private detention;
public-duty mandamus may reach a non-State body.

TERRITORIAL RULE
seat/respondent connection plus Article 226(2) cause of action wholly or partly within territory.

FIVE WRITS
habeas corpus | mandamus | prohibition | certiorari | quo warranto:
choose by wrong, target, timing and remedy, not by memorised definition alone.""",
        ),
        (
            "Article 226 versus 32, superintendence and control",
            "constitutional-remedy-control-matrix",
            [19, 20, 21, 22, 23, 24],
            """ARTICLE 32                         ARTICLE 226
Supreme Court                       High Court
itself a Fundamental Right          constitutional power, not a Part III right
Fundamental Rights                  Fundamental Rights + other legal rights
national apex route                 territorial cause-of-action route

ARTICLE 227
superintendence over courts and tribunals within territory, subject to constitutional exclusions.

ARTICLE 228
withdraw case involving a substantial constitutional question and decide or return it.

ARTICLE 235
High Court control over district and subordinate judiciary protects decisional independence.

L. Chandra Kumar (1997) -> Articles 226/227 and 32 review are Basic Structure;
tribunals supplement but cannot wholly replace constitutional courts.""",
        ),
        (
            "District judges and subordinate judicial independence",
            "subordinate-judiciary-appointment-chain",
            [25, 26, 27, 28, 29],
            """ARTICLE 233 DISTRICT JUDGES
Governor appoints in consultation with High Court;
direct Bar recruit requires at least seven years as advocate/pleader and High Court recommendation.

ARTICLE 234 OTHER JUDICIAL SERVICE
Governor makes appointments under rules after consultation with State PSC and High Court.

ARTICLE 235 CONTROL
posting, promotion, leave and discipline under High Court control, subject to legal safeguards.

ARTICLE 50
State shall separate judiciary from executive in public services.

Chandra Mohan (1966) -> executive dominance over district-judge selection violates
the constitutional scheme of an independent judicial service.""",
        ),
        (
            "Gram Nyayalayas, tribunals and the AIJS debate",
            "access-institution-comparison",
            [30, 31, 32, 33],
            """GRAM NYAYALAYAS ACT, 2008
bounded statutory local-court model for notified areas; establishment and functioning are uneven.

TRIBUNALS
specialisation + speed potential
VERSUS appointments, tenure, executive control and fragmented appeals.
L. Chandra Kumar (1997) keeps High Court judicial review as the constitutional floor.

ALL INDIA JUDICIAL SERVICE
Article 312 route -> Rajya Sabha two-thirds of members present and voting
-> parliamentary law; Article 312(3) excludes posts below district judge.

DEBATE
national standards and vacancies versus language, local law, federal control and career integration.
CURRENT STATUS: no AIJS has been created.""",
        ),
        (
            "Vacancies, pendency, legal aid and eCourts",
            "justice-delivery-reform-chain",
            [34, 35, 36],
            """DELIVERY BOTTLENECK
vacancies + infrastructure + process delay + adjournments + government litigation
-> pendency -> cost -> unequal bargaining -> reduced trust.

ACCESS LAYER
Article 39A legal aid | NALSA/SLSA/DLSA | Lok Adalats | e-Sewa Kendras.
Speedy-trial access principles belong to the wider rights chain;
do not equate disposal with justice.

eCOURTS PHASE III, 2023-2027
digitisation + e-filing + e-payments + paperless courts + data-based management.

LIMIT
technology can reduce transaction costs but cannot replace judges, translators, connectivity,
accessible design, reasoned hearings or enforcement capacity.
Quote dynamic numbers only with a date.""",
        ),
        (
            "SC-HC-subordinate comparison, traps and answer spine",
            "judiciary-level-exam-synthesis",
            [33, 34, 35, 36],
            """SUPREME COURT             HIGH COURT                  SUBORDINATE COURTS
national apex              territorial constitutional court ordinary trial hierarchy
Article 32                 Article 226 wider in cause        statutory jurisdiction
Article 141 precedent      Article 227 superintendence       bound by higher courts
final appeals/SLP          appeals + administration          facts, trial and first appeal

PRELIMS FIREWALL
HC retirement 62, SC 65 | Article 226 wider than 32 | common HC by Parliament
| district judges: Governor + HC consultation | Article 235 control with HC | AIJS absent.

MAINS SPINE
locate Article -> state institutional function -> appointment/control safeguard
-> access or capacity problem -> case with year -> cooperative reform
-> independent, decentralised and digitally inclusive justice conclusion.""",
        ),
    ],
    "polity-22": [
        (
            "Canonical Part XXI scope and the boundary with other topics",
            "part-xxi-scope-map",
            [1, 2, 3, 4],
            """PART XXI: TEMPORARY, TRANSITIONAL AND SPECIAL PROVISIONS
Articles 369-392 include time-bound transitional rules, continuance/adaptation devices
and State-specific constitutional asymmetry.

THIS TOPIC OWNS
Article 370 evolution/current status + Articles 371-371J + asymmetry mechanisms.

DISTINCT OWNERS
Part XVIII emergencies | reservation/class provisions | Part X and Fifth/Sixth Schedules
| ordinary Union-State flexibility | Union Territory administration.

CORE IDEA
constitutional equality permits reasoned differentiation; special treatment remains
inside one Constitution and does not create separate sovereignty.""",
        ),
        (
            "Article 370 before 2019: accession, Orders and constitutional application",
            "article-370-pre2019-system",
            [5, 6, 7, 8],
            """PRE-2019 OPERATING CHAIN
Instrument of Accession fields -> Article 370(1) consultation/concurrence
-> Presidential Orders -> wider Constitution and Union-law application to J&K.

ARTICLE 35A
1954 Constitution Application Order -> permanent-resident definition and specified protections.

CONSTITUENT ASSEMBLY ISSUE
Article 370(3) proviso referred to J&K Constituent Assembly; it dissolved in 1957.

Sampat Prakash (1968) -> Article 370 and Presidential-Order practice continued after 1957.

LIMIT
autonomy was constitutionally mediated; it did not amount to external sovereignty.""",
        ),
        (
            "The 2019 constitutional-order and reorganisation sequence",
            "article-370-2019-process",
            [9, 10, 11, 12],
            """5 AUGUST 2019
C.O. 272 under Article 370(1) -> Constitution applied comprehensively
-> interpretive change used the State-legislature route while President's Rule operated.

PARLIAMENTARY RESOLUTION
recommended Article 370(3) declaration.

6 AUGUST 2019
C.O. 273 -> Article 370 provisions ceased to operate except the modified declaration.

J&K REORGANISATION ACT, 2019
former State -> UT of Jammu and Kashmir with legislature
+ UT of Ladakh without legislature, effective 31 October 2019.

TRAP
Presidential Orders, parliamentary resolution and reorganisation statute are distinct legal acts.""",
        ),
        (
            "In Re Article 370 (2023): holdings and issues left open",
            "article-370-judgment-control",
            [13, 14, 15, 16],
            """In Re: Article 370 of the Constitution (2023)
  +-- Article 370 was temporary; J&K had no internal sovereignty after accession
  +-- Article 370(3) power survived dissolution of the J&K Constituent Assembly
  +-- C.O. 273 declaration was upheld
  +-- C.O. 272's Article 367 route was invalid, but the final outcome survived independently
  +-- J&K Constitution became inoperative after full application of India's Constitution.

OPEN / QUALIFIED
Court recorded restoration-of-Statehood assurance and set no judicial deadline.
It did not finally decide the State-to-UT conversion issue after the Union concession.

VERDICT
the Article 370 abrogation question is judicially settled; Statehood timing remains political/legal.""",
        ),
        (
            "Current Jammu and Kashmir and Ladakh position",
            "current-jk-ladakh-map",
            [17, 18, 19],
            """JAMMU AND KASHMIR
Union Territory with legislature | Assembly elections held Sep-Oct 2024
| Statehood not restored as of 24 August 2026.

LADAKH
Union Territory without legislature.
Demands include Statehood, Sixth Schedule protection and Article 371-type safeguards.

LEGAL STATUS CONTROL
demands, committee talks and political assurances are not enacted constitutional change.

DISTINCTION
J&K Statehood restoration -> reorganisation/federal-status question
Ladakh Sixth Schedule -> Article 244 + Sixth Schedule autonomy question
Article 371-type protection -> Part XXI amendment question.""",
        ),
        (
            "Articles 371 to 371D: development and regional-equity mechanisms",
            "article-371-development-family",
            [20, 21, 22, 23],
            """ARTICLE 371
Maharashtra/Gujarat -> Governor's special responsibility for regional development boards,
equitable funds and opportunities.

ARTICLE 371A: NAGALAND
specified religious/social practices, customary law, customary justice and land/resources
shielded from parliamentary law unless State Assembly resolves otherwise.

ARTICLE 371B: ASSAM
Assembly committee for tribal areas.

ARTICLE 371C: MANIPUR
Hill Areas Committee + Governor reporting/special responsibility framework.

ARTICLE 371D: ANDHRA PRADESH/TELANGANA
equitable local opportunities in public employment/education; presidential-order mechanism.
ARTICLE 371E merely enables a Central University in Andhra Pradesh.""",
        ),
        (
            "Articles 371F to 371J: identity, law-and-order and local opportunity",
            "article-371-identity-family",
            [24, 25, 26, 27, 28, 29],
            """ARTICLE 371F: SIKKIM
integration-specific Assembly, representation and continuity protections.

ARTICLE 371G: MIZORAM
specified religious/social practices, customary law/justice and land protection
unless State Assembly resolves otherwise; distinct from Nagaland's resource wording.

ARTICLE 371H: ARUNACHAL PRADESH
Governor's special responsibility for law and order, exercised after ministerial consultation.

ARTICLE 371I: GOA
minimum Assembly size safeguard.

ARTICLE 371J: KALYANA KARNATAKA
development board, equitable funds and local reservation/opportunity mechanisms.

EXAM RULE
match State -> Article -> protected subject -> decision-maker -> consent/resolution requirement.""",
        ),
        (
            "Mechanism comparison: Orders, amendments and tribal Schedules",
            "asymmetry-mechanism-matrix",
            [30, 31, 32, 33, 34],
            """ARTICLE 370 HISTORIC ROUTE
Presidential Orders under its own text -> now inoperative after 2019/2023 control.

ARTICLES 371-371J
constitutional text created or changed through constitutional-amendment history;
some clauses authorise Presidential Orders or Governor responsibilities for implementation.

FIFTH SCHEDULE
Scheduled Areas + Governor/Tribes Advisory Council + presidential declaration architecture.

SIXTH SCHEDULE
autonomous district/regional councils in Assam, Meghalaya, Tripura and Mizoram.

DO NOT MERGE
Article 371A/371G consent shields != Sixth Schedule councils
!= Fifth Schedule administration != Article 370's former application mechanism.""",
        ),
        (
            "Federalism, equality, current traps and qualified synthesis",
            "special-provisions-exam-synthesis",
            [33, 34, 35],
            """WHY ASYMMETRY
historical compact + cultural identity + tribal land/custom + regional imbalance
-> tailored guarantee -> integration with protection.

RISKS
insider-outsider exclusion | weak implementation | Governor controversy
| unequal opportunity | permanent grievance politics.

PRELIMS FIREWALL
Article 370 printed but inoperative | Articles 371-371J still operative
| 371E enables a university | 371I concerns Goa | 371H law and order
| Fifth/Sixth Schedules are not Part XXI | Ladakh demands are not law.

MAINS SPINE
define asymmetric federalism -> classify mechanism -> exact Article/State
-> benefit -> equality/federal counterpoint -> implementation reform
-> unity through constitutionally bounded and reviewable difference.""",
        ),
    ],
}


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def topic_directory_hashes(root: Path, *, exclude_polity: set[int]) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for subject in root.iterdir():
        if not subject.is_dir():
            continue
        for section in subject.iterdir():
            if not section.is_dir():
                continue
            candidates = list(section.iterdir())
            if any(
                path.is_dir() and path.name == "01-Complete-Learning-Session"
                for path in candidates
            ):
                topic_dirs = [section]
            else:
                topic_dirs = [path for path in candidates if path.is_dir()]
            for topic_dir in topic_dirs:
                match = re.match(r"^(\d+)-", topic_dir.name)
                if (
                    subject.name == "Polity"
                    and match
                    and int(match.group(1)) in exclude_polity
                ):
                    continue
                if not any(path.is_file() for path in topic_dir.rglob("*")):
                    continue
                for path in topic_dir.rglob("*"):
                    if path.is_file():
                        hashes[relative(path)] = sha256(path)
    return hashes


def flow_topic_hashes(*, exclude_polity: set[int]) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for subject in FLOW_LIBRARY.iterdir():
        if not subject.is_dir():
            continue
        for topic_dir in subject.iterdir():
            if not topic_dir.is_dir():
                continue
            match = re.match(r"^(\d+)-", topic_dir.name)
            if (
                subject.name == "Polity"
                and match
                and int(match.group(1)) in exclude_polity
            ):
                continue
            for path in topic_dir.rglob("*"):
                if path.is_file():
                    hashes[relative(path)] = sha256(path)
    return hashes


def compare_hashes(before: dict[str, str], after: dict[str, str]) -> list[str]:
    return sorted(
        key
        for key in set(before) | set(after)
        if before.get(key) != after.get(key)
    )


def augment_audit(config: dict[str, Any], audit_path: Path) -> None:
    payload = json.loads(audit_path.read_text(encoding="utf-8"))
    payload["topic_completeness_contract"] = config["coverage_contract"]
    payload["topic_completeness_status"] = "passed"
    if config["key"] == "polity-22":
        payload["canonical_scope_resolution"] = {
            "catalogue_topic": "polity-22 — Special Provisions",
            "owner_manifest": "upsc-ai-kit\\manifests\\v2\\polity--subject-wide-syllabus.json",
            "basic_owner": config["basic"],
            "advanced_owner": config["advanced"],
            "included": [
                "relevant Articles 369-392",
                "Article 370",
                "Articles 371-371J",
                "temporary, transitional and State-specific asymmetry",
            ],
            "distinguished_not_duplicated": [
                "emergency provisions",
                "special provisions relating to certain classes",
                "Fifth and Sixth Schedule specialist doctrine",
                "ordinary federal flexibility",
            ],
            "status": "resolved",
        }
    audit_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def workbook_gate(source_markdown: Path) -> dict[str, int]:
    text = source_markdown.read_text(encoding="utf-8")
    workbook = base.refresh.extract_v2_workbook_markdown(text)
    mcqs = len(re.findall(r"(?m)^####\s+(?:OM|RM)\d+\.", workbook))
    pyqs = len(
        re.findall(
            r"(?m)^#{3,5}\s+(?:PYQ|Prelims route)\b",
            workbook,
        )
    )
    original_mains = len(re.findall(r"(?m)^#{3,5}\s+M\d+\.", workbook))
    if mcqs < 36 or pyqs < 1 or original_mains < 7:
        raise RuntimeError(
            f"Workbook gate failed: mcqs={mcqs}, pyqs={pyqs}, mains={original_mains}"
        )
    return {
        "mcqs_authored": mcqs,
        "pyq_routes_authored": pyqs,
        "original_mains_authored": original_mains,
    }


def case_year_gate(config: dict[str, Any], ascii_path: Path, graph_path: Path) -> None:
    manual = base.refresh.ascii_master.normalize_manual_spec_file(ascii_path)[
        config["key"]
    ]
    ascii_text = "\n".join(
        f"{panel.title}\n{panel.body}" for panel in manual.panels
    )
    errors = case_years.ascii_topic_errors(config["key"], ascii_text)
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    errors.extend(case_years.graphical_spec_errors(graph))
    if errors:
        raise RuntimeError(f"{config['key']}: case-year gate failed: {' | '.join(errors)}")


def export_flow(config: dict[str, Any], expected_count: int) -> tuple[Path, dict[str, Any]]:
    validation_path = (
        EXPORTS / f"{config['key']}-flow-learning-{DATE}-validation.json"
    )
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "export_flow_learning_library.py"),
            "--all-completed",
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


def latest_record(config: dict[str, Any]) -> dict[str, Any]:
    tracker = base.refresh.load_tracker()
    records = [
        record
        for record in tracker["exports"]
        if isinstance(record, dict)
        and record.get("topic_key") == config["key"]
        and record.get("variant") == base.refresh.V2_VARIANT
    ]
    if not records:
        raise RuntimeError(f"{config['key']}: learner-v2 tracker record missing.")
    record = max(records, key=lambda item: int(item.get("generation") or 0))
    if record.get("approved") is not False:
        raise RuntimeError(f"{config['key']}: approval isolation failed.")
    return record


def lock_hashes(paths: list[Path]) -> dict[str, str]:
    return {
        relative(path): sha256(path)
        for root in paths
        for path in root.rglob("*")
        if path.is_file()
    }


def iso_mtime(path: Path) -> str:
    return datetime.fromtimestamp(path.stat().st_mtime).astimezone().isoformat(
        timespec="seconds"
    )


def completed_result(config: dict[str, Any]) -> tuple[dict[str, Any], Path, Path] | None:
    completed = base.existing_result(config)
    if completed is None:
        return None
    record = latest_record(config)
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
        iso_mtime(path) for path in clean_folder.rglob("*") if path.is_file()
    )
    flow_completed = str(flow_payload.get("validated_at") or iso_mtime(flow_validation))
    completed["completed_at"] = flow_completed
    completed["gate_times"] = {
        "A_started": audit["started_at"],
        "A_completed": audit["completed_at"],
        "B_completed": iso_mtime(source_path),
        "C_completed": iso_mtime(source_path),
        "D_completed": iso_mtime(ascii_path),
        "E_completed": iso_mtime(graph_path),
        "F_completed": iso_mtime(validation_path),
        "G_completed": iso_mtime(staged_path),
        "H_completed": clean_completed,
        "I_completed": flow_completed,
        "J_completed": flow_completed,
    }
    completed["approved"] = record["approved"]
    completed["counts"]["flow_pages"] = flow_row["pdf_validation"]["page_count"]
    completed["workbook_authoring_gate"] = workbook_gate(source_path)
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
    expected_order = [f"polity-{number:02d}" for number in range(18, 23)]
    if [config["key"] for config in TOPICS] != expected_order:
        raise RuntimeError("Sequential topic order was altered.")
    base.PANELS.update(PANELS)

    clean_baseline = topic_directory_hashes(
        FINAL_LIBRARY,
        exclude_polity={18, 19, 20, 21, 22},
    )
    flow_baseline = flow_topic_hashes(exclude_polity={18, 19, 20, 21, 22})
    locked_new: dict[str, str] = {}
    results: list[dict[str, Any]] = []

    for index, config in enumerate(TOPICS, 1):
        resumed = completed_result(config)
        if resumed is not None:
            result, clean_folder, flow_folder = resumed
            results.append(result)
            locked_new.update(lock_hashes([clean_folder, flow_folder]))
            continue
        if compare_hashes(locked_new, {key: sha256(ROOT / key) for key in locked_new}):
            raise RuntimeError("Previously generated topic artifacts changed before next gate.")

        gate_times: dict[str, str] = {"A_started": now()}
        live = base.live_checks(config)
        audit = base.write_audit(config, gate_times["A_started"], live)
        augment_audit(config, audit)
        gate_times["A_completed"] = now()

        source_markdown = base.transform_source(config)
        gate_times["B_completed"] = now()

        workbook_authored = workbook_gate(source_markdown)
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
        case_year_gate(config, ascii_path, graph_path)
        gate_times["E_completed"] = now()

        spec_path = base.write_new_topic_spec(
            config,
            source_markdown,
            audit,
            ascii_path,
            graph_path,
        )
        row, record = base.finalize_topic(config, spec_path)
        if not row["passed"]:
            raise RuntimeError(f"{config['key']}: render validation failed.")
        gate_times["F_completed"] = now()

        record = latest_record(config)
        gate_times["G_completed"] = now()

        base.export_clean_topic(config)
        clean_folder = base.verify_four_folders(config)
        gate_times["H_completed"] = now()

        expected_count = 50 + index
        flow_validation, flow_row = export_flow(config, expected_count)
        flow_folder = ROOT / Path(flow_row["destination_folder"].replace("\\", "/"))
        gate_times["I_completed"] = now()

        clean_mismatches = compare_hashes(
            clean_baseline,
            topic_directory_hashes(
                FINAL_LIBRARY,
                exclude_polity={18, 19, 20, 21, 22},
            ),
        )
        flow_mismatches = compare_hashes(
            flow_baseline,
            flow_topic_hashes(exclude_polity={18, 19, 20, 21, 22}),
        )
        if clean_mismatches or flow_mismatches:
            raise RuntimeError(
                f"{config['key']}: preservation regression: "
                f"clean={clean_mismatches[:5]} flow={flow_mismatches[:5]}"
            )
        prior_mismatches = compare_hashes(
            locked_new,
            {key: sha256(ROOT / key) for key in locked_new},
        )
        if prior_mismatches:
            raise RuntimeError(
                f"{config['key']}: prior generated artifacts changed: {prior_mismatches[:5]}"
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
        locked_new.update(lock_hashes([clean_folder, flow_folder]))

    final_clean_mismatches = compare_hashes(
        clean_baseline,
        topic_directory_hashes(
            FINAL_LIBRARY,
            exclude_polity={18, 19, 20, 21, 22},
        ),
    )
    final_flow_mismatches = compare_hashes(
        flow_baseline,
        flow_topic_hashes(exclude_polity={18, 19, 20, 21, 22}),
    )
    state = {
        "schema_version": 1,
        "batch_id": "polity-18-22-sequential-batch-2026-08-24",
        "created_at": now(),
        "strict_order": expected_order,
        "topics": results,
        "existing_clean_topic_artifact_count": len(clean_baseline),
        "existing_flow_topic_artifact_count": len(flow_baseline),
        "existing_clean_hash_mismatches": final_clean_mismatches,
        "existing_flow_hash_mismatches": final_flow_mismatches,
        "prior_generated_topic_hash_mismatches": compare_hashes(
            locked_new,
            {key: sha256(ROOT / key) for key in locked_new},
        ),
    }
    state_path = EXPORTS / "polity-18-22-sequential-batch-state.json"
    state_path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return state


def main() -> int:
    state = run()
    print(
        f"topics={len(state['topics'])} order={','.join(state['strict_order'])} "
        f"clean_mismatches={len(state['existing_clean_hash_mismatches'])} "
        f"flow_mismatches={len(state['existing_flow_hash_mismatches'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
