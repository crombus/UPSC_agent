"""Extend the hostile Polity deep-review workflow to topics 16-20."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_11_15_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    16: (
        "Reconstruct the responsible Union executive through Articles 74, 75, "
        "77, 78 and 88: appointment, advice, confidence, responsibility, "
        "membership, business allocation and parliamentary participation are "
        "separate constitutional questions.",
        "Keep Council of Ministers, Cabinet, Cabinet Committees, Cabinet "
        "Secretariat, PMO and kitchen cabinet distinct by source, membership, "
        "legal status and function; do not constitutionalise administrative or "
        "informal bodies.",
        "Use the current Prime Minister and the Cabinet Secretariat's Allocation "
        "of Business and Transaction of Business Rules only as dated official "
        "controls. Committee number, membership and chairmanship remain "
        "notification-sensitive.",
    ),
    17: (
        "Audit Parliament through Articles 79-122 and the financial provisions: "
        "composition, officers, sessions, membership, privileges, legislation, "
        "lapse, joint sitting, finance, committees and accountability require "
        "their own procedural chains.",
        "Keep constitutional text, House rules and conventions separate. Speaker "
        "certification is textually final but not wholly immune from constitutional "
        "review; Rajya Sabha is subordinate on money and confidence but co-equal "
        "on ordinary legislation and amendment, with exclusive Articles 249/312 powers.",
        "The 106th Amendment commenced on 16 April 2026 but reservation remains "
        "non-operational pending the Article 334A census-publication-delimitation "
        "sequence. Census 2027 dates are notified; publication and delimitation "
        "dates are not.",
    ),
    18: (
        "Map Articles 124-147 with exact appointment, qualification, tenure, "
        "removal, independence, jurisdiction, precedent, review, contempt and "
        "complete-justice rules; do not merge Article 32, 136, 137, 141, 142 or 143.",
        "Keep collegium doctrine, NJAC invalidation, judicial review, Basic "
        "Structure, PIL and judicial legislation proposition-specific. Article "
        "142 supplies complete justice in a cause or matter, not free-standing "
        "power to ignore substantive law.",
        "Act 14 of 2026 raises the statutory maximum to thirty-seven judges "
        "excluding the CJI, total sanctioned strength thirty-eight, deemed in "
        "force from 16 May 2026. Working strength and pendency remain dynamic.",
    ),
    19: (
        "Teach Articles 153-167 office by office, then separate aid and advice, "
        "express or necessarily implied discretion, government formation, floor "
        "tests, Article 356 reporting, assent, ordinance and clemency.",
        "Apply Shamsher Singh, Bommai, Rameshwar Prasad, B.P. Singhal, Nabam "
        "Rebia and Subhash Desai only for their stated propositions. Article 200 "
        "discretion does not create general gubernatorial discretion.",
        "The 20 November 2025 Article 143 opinion gives three Article 200 options, "
        "rejects rigid timelines and deemed assent, and permits only limited "
        "mandamus against prolonged unexplained indefinite inaction. Article 161 "
        "can include pardon of a death sentence where the offence-law nexus lies "
        "within State executive power; court-martial remains outside it.",
    ),
    20: (
        "Audit Articles 168-212 through legislature shape, Article 169, "
        "composition, duration, membership, officers, sessions, privileges, "
        "ordinary and financial Bills, budget, procedure and judicial-review limits.",
        "Keep the Council's four-month ordinary-Bill delay, fourteen-day "
        "Money-Bill role and absence of a State joint sitting distinct. Article "
        "207(1) and 207(3) financial Bills are not automatically Money Bills.",
        "Six States retain Councils. The 106th Amendment is commenced but its "
        "reservation is not operational; Census 2027 reference dates do not equal "
        "publication of figures or commencement of delimitation.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    16: """### Semantic-completeness ownership and PYQ control

- **Responsible-executive spine:** Article 74 creates the Prime-Minister-headed
  Council that aids and advises the President; Article 75 separately controls
  appointment, pleasure, collective responsibility, oaths and the six-month rule.
  Article 77 controls formal executive action and business rules; Article 78 makes
  the Prime Minister the constitutional information channel to the President.
- **Appointment and confidence:** the President appoints the person most likely to
  command Lok Sabha confidence. A decisive majority leaves no personal choice; a
  hung House permits bounded judgment tested promptly on the floor. The Prime
  Minister may belong to either House or remain a non-member only for six
  consecutive months under Article 75(5).
- **Responsibility firewall:** Article 75(3) collective responsibility is owed only
  to the Lok Sabha and makes the ministry stand or fall together. Article 75(2)
  individual pleasure is normally enforced on the Prime Minister's advice.
  Political, individual and legal responsibility are not synonyms; Article 74(2)
  protects advice from inquiry but not every resulting executive act from review.
- **Ministry size and defection:** Article 75(1A), inserted by the Ninety-first
  Amendment, caps all Union ministers including the Prime Minister at fifteen per
  cent of Lok Sabha strength. Article 75(1B) separately bars a disqualified
  defector from ministership for the stated period.
- **Institution map:** the Council is the wider constitutional ministry; Cabinet is
  its smaller decision core and is expressly defined for Article 352(3). Cabinet
  Committees arise under business-rule practice; the Cabinet Secretariat and PMO
  are administrative staff institutions; a kitchen cabinet is informal. None of
  the last four may be treated as a constitutional substitute for the Council.
- **Business machinery:** the Government of India (Allocation of Business) Rules,
  1961 distribute subjects among ministries; the Transaction of Business Rules,
  1961 prescribe decision, consultation and Cabinet routes. Authentication under
  Article 77 does not erase ministerial responsibility or judicial review of the
  underlying legality.
- **Prime-ministerial government:** portfolio control, party leadership, Cabinet
  agenda, dissolution advice and the Article 78 channel concentrate power.
  Cabinet deliberation, coalition arithmetic, federal politics, Parliament,
  elections and judicial review qualify rather than abolish that concentration.
- **Continuity and caretaker control:** resignation or death of the Prime Minister
  ends the ministry politically, while Article 74 requires constitutional
  continuity until a successor assumes office. Caretaker restraint is convention,
  not a separate codified constitutional government.
- **Current control:** official PM India identifies Narendra Modi as Prime
  Minister. Cabinet Secretariat continues to publish the two 1961 business-rule
  sets and dated Cabinet-Committee compositions; committee membership and chairs
  must never be frozen beyond the cited notification.
- **Four-ledger/PYQ control:** every routed 2018-2026 demand was checked against
  constitutional text, the complete Basic owner, cross-owner boundaries and
  verified papers. Topic 11 retains the full parliamentary-system comparison;
  Topic 17 owns detailed parliamentary procedure.""",
    17: """### Semantic-completeness ownership and PYQ control

- **Institutional map:** Article 79 makes the President, Rajya Sabha and Lok Sabha
  the Parliament. Articles 80-84 govern composition and membership; Articles
  89-98 presiding officers; Articles 85-88 sessions and participation; Articles
  100-122 voting, privileges, legislation, finance, language and procedural autonomy.
- **Composition and duration:** Rajya Sabha is permanent, with one-third retiring
  every second year; Lok Sabha normally lasts five years unless sooner dissolved.
  The constitutional maxima, actual sanctioned/elected strengths and current
  vacancies are different registers and must not be merged.
- **Session distinctions:** summoning, prorogation, adjournment, adjournment sine
  die and dissolution have different actors and legal consequences. Article 85
  fixes the six-month maximum interval; Budget, Monsoon and Winter are conventions,
  not constitutional session names.
- **Bill-class firewall:** ordinary Bills follow bicameral passage and possible
  Article 108 joint sitting; Money Bills satisfy Article 110 exclusively, originate
  only in Lok Sabha and give Rajya Sabha fourteen days to recommend. Article 117
  financial Bills, demands for grants and appropriation require separate routes.
- **Money-Bill review:** the Speaker's Article 110 certificate is textually final,
  but K.S. Puttaswamy (Aadhaar) and Rojer Mathew preserve constitutional review for
  illegality; no unresolved larger-Bench issue may be presented as finally settled.
- **Lapse and ordinance:** prorogation does not lapse Bills. Rajya-Sabha-pending
  Bills not passed by Lok Sabha survive dissolution; Lok-Sabha-pending Bills and
  Bills passed by Lok Sabha but pending in Rajya Sabha lapse. Article 123 remains
  an executive emergency route subject to reassembly and legislative control.
- **Accountability:** questions, motions, confidence, budget votes, cut motions,
  CAG-PAC scrutiny and committees are distinct tools. The anti-defection whip,
  executive control of time, disruptions, guillotine and bypass routes explain
  why strong formal instruments may yield weak practical scrutiny.
- **Committee architecture:** PAC, Estimates and CoPU differ in composition and
  mandate; the twenty-four DRSCs have thirty-one members each and advisory reports.
  Standing, select, joint and ad hoc committees are not interchangeable.
- **Current representation control:** S.O. 1922(E) commenced the 106th Amendment
  on 16 April 2026. Reservation under Articles 330A, 332A and Article 334A is still dormant
  until publication of relevant figures of the first post-commencement census and
  a delimitation exercise for that purpose. Census 2027 reference dates are
  notified; no publication, delimitation or first-reserved-election date is.
- **Current institutional control:** Om Birla is Lok Sabha Speaker and C. P.
  Radhakrishnan is ex officio Rajya Sabha Chairman on the dated official pages.
  The 2026 delimitation-linked Bills did not become law; their proposed seat
  ceilings and census basis remain proposal facts only.
- **Four-ledger/PYQ control:** all direct and routed 2018-2025 Parliament demands
  were retained with official-key discipline. Topic 16 owns executive composition;
  Topic 20 owns State-legislature procedure.""",
    18: """### Semantic-completeness ownership and PYQ control

- **Constitutional identity:** Articles 124-147 create the Supreme Court within an
  integrated judicial hierarchy. It is simultaneously constitutional court,
  federal umpire, Fundamental-Rights guarantor and final appellate court; High
  Courts retain independent Articles 226/227/235 functions.
- **Current statutory strength:** the Supreme Court (Number of Judges) Amendment
  Act, 2026, Act 14 of 2026, substitutes thirty-seven for thirty-three judges
  excluding the Chief Justice and is deemed in force from 16 May 2026. Sanctioned
  strength is therefore thirty-eight including the CJI. Working strength remains
  a live roster fact and must be verified separately.
- **Appointment and independence:** Article 124 text, the First, Second and Third
  Judges Cases, the 99th Amendment/NJAC invalidation and the current collegium
  route must remain chronological. Security of tenure, charged expenditure,
  Article 121, removal and post-retirement restrictions are different safeguards.
- **Jurisdiction gateway:** Article 131 original jurisdiction requires a legal-
  right federal dispute; Article 32 concerns Fundamental Rights; Articles 132-134A
  govern appeals; Article 136 is discretionary special leave; Article 143 advice
  is not an ordinary binding decree. Review under Article 137 and curative relief
  are separate correction routes.
- **Precedent and complete justice:** Article 141 binds through the declared ratio,
  subject to bench strength; Article 142 operates in the cause or matter before
  the Court and cannot supplant substantive constitutional or statutory limits.
  Articles 129, 144 and 145 govern record/contempt, aid and procedure.
- **Constitutional review:** Kesavananda Bharati, Minerva Mills and I.R. Coelho
  control amendment and Ninth-Schedule review; L. Chandra Kumar preserves High
  Court/Supreme Court review over tribunals. Judicial review and independence are
  Basic Structure, not claims of judicial supremacy.
- **PIL and legislation:** Hussainara Khatoon, S.P. Gupta, Vishaka and continuing
  mandamus explain access and gap-filling. Rights enforcement and interim norms
  must be distinguished from permanent policy substitution and merits governance.
- **Accountability and diversity:** impeachment/removal, in-house procedure,
  reasoned collegium disclosure, recusal, assets, representation and access reform
  address different deficits. No lapsed accountability Bill may be taught as law.
- **Current control:** Justice Surya Kant is Chief Justice of India on the official
  roster. Special Reference No. 1 of 2025 is an Article 143 advisory opinion:
  no rigid assent timelines or deemed assent, while prolonged unexplained
  indefinite inaction remains open to limited mandamus.
- **Four-ledger/PYQ control:** all direct and routed 2018-2025 jurisdiction,
  independence, collegium, PIL, environment and accountability demands were
  preserved; current judge, vacancy and pendency figures remain date-labelled.""",
    19: """### Semantic-completeness ownership and PYQ control

- **Office map:** Articles 153-162 govern the Governor and State executive power;
  Articles 163-164 govern advice, discretion, ministers and responsibility;
  Articles 165-167 govern the Advocate General, business and the Chief Minister's
  information duties. Article 361 immunity protects the person, not unlawful State action.
- **Advice and discretion:** Shamsher Singh makes ministerial advice the default.
  Express or necessarily implied exceptions remain narrow: specified Article 200
  choices, government formation, objective floor-test situations, Article 356
  reporting and specially worded constitutional responsibilities.
- **Formation and confidence:** the Governor invites the person most likely to
  command Assembly confidence and uses an early floor test where objective doubt
  exists. Bommai, Rameshwar Prasad and Subhash Desai reject subjective arithmetic,
  speculative dissolution and use of a floor test to settle an internal party dispute.
- **Tenure and neutrality:** Article 156 pleasure does not make the Governor a
  Union employee. B.P. Singhal bars arbitrary, capricious or mala fide removal;
  Sarkaria, Punchhi and NCRWC proposals remain reform recommendations, not law.
- **Article 200 current rule:** Special Reference No. 1 of 2025 identifies three
  options—assent, reserve, or withhold and return a non-Money Bill with comments.
  The Governor chooses among them in discretion and is not bound by State-Cabinet
  advice for that choice. Merits review, rigid timelines and deemed assent are
  unavailable; prolonged, unexplained and indefinite inaction permits only a
  limited mandamus to discharge the function within a reasonable time.
- **Article 201:** Presidential assent/withholding is not merits-justiciable and
  carries no court-created deadline. The President need not seek Article 143
  advice whenever a Bill is reserved, and courts cannot adjudicate a Bill's
  contents before it becomes law.
- **Ordinance:** Article 213 requires the relevant House or Houses not to be in
  session and immediate action. D.C. Wadhwa and Krishna Kumar Singh condemn
  routine re-promulgation, require laying and preserve judicial review of satisfaction.
- **Clemency correction:** Article 161 is controlled by the offence-law nexus to
  State executive power; it can include pardon of a death sentence within that
  field. Unlike Article 72, it has no court-martial limb and no separate power over
  every death sentence regardless of legislative field. Maru Ram, State of Haryana
  v. Raj Kumar @ Bittu and A.G. Perarivalan make Cabinet advice binding and delay reviewable.
- **Chief Minister and Council:** Article 164 appointment and collective
  responsibility run to the Legislative Assembly. Article 164(1A) caps ministers
  at fifteen per cent of Assembly strength with a minimum of twelve; clause (1B)
  bars defectors. Article 167 parallels the Union Article 78 information bridge.
- **Four-ledger/PYQ control:** all direct and supporting 2018-2025 Governor,
  ordinance, defection, assent and federal-neutrality demands were reconciled;
  State-legislature procedure remains owned by Topic 20.""",
    20: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Article 168 permits one or two Houses with the Governor
  as a component of the legislature. Articles 169-177 govern creation,
  composition, duration, qualification and participation; Articles 178-187
  officers; Articles 188-212 oath, voting, disqualification, privileges,
  legislation, finance, procedure and judicial non-interference.
- **Article 169 route:** the Assembly first resolves by a majority of total
  membership plus two-thirds present and voting; Parliament then creates or
  abolishes the Council by ordinary law and simple majority. The resulting law is
  expressly not an Article 368 constitutional amendment.
- **Composition:** the Assembly is directly elected and normally has 60-500
  members subject to special provisions. A Council may not exceed one-third of
  Assembly strength and ordinarily has at least forty members; Article 171's
  local-body, graduate, teacher, MLA and nominated fractions must remain exact.
- **Duration and officers:** the Assembly normally lasts five years and may be
  dissolved; the Council is permanent with one-third retiring every second year.
  Speaker/Deputy Speaker and Chairman/Deputy Chairman have distinct removal,
  vacancy, casting-vote and continuity rules.
- **Bicameral inequality:** Article 197 allows a Council to delay an ordinary Bill
  for three months and then one month after Assembly repassage. There is no State
  joint sitting. A Council-originated Bill rejected by the Assembly ends.
- **Finance firewall:** Money Bills originate only in the Assembly, receive a
  fourteen-day recommendatory Council review and Speaker certification. Article
  207(1) mixed financial Bills and Article 207(3) expenditure Bills are distinct;
  neither category becomes a Money Bill merely because expenditure is involved.
- **Lapse and procedure:** prorogation does not lapse Bills; Council-only pending
  Bills survive Assembly dissolution; Assembly-pending and Assembly-passed/
  Council-pending Bills lapse. Article 212 protects procedural irregularity, not
  substantive illegality or unconstitutionality.
- **Presiding-officer review:** Kihoto Hollohan makes the Speaker a Tenth-Schedule
  tribunal subject to review. Keisham Meghachandra supplies the ordinarily
  three-month norm; Padi Kaushik Reddy (2025) directed the Telangana
  Speaker to conclude ten pending petitions within three months and confirms that
  Articles 122/212 immunity does not attach to Paragraph 6 adjudication.
- **Current representation control:** Andhra Pradesh, Bihar, Karnataka,
  Maharashtra, Telangana and Uttar Pradesh retain Councils. The 106th Amendment
  commenced on 16 April 2026 but reservation remains dormant until the Article
  334A census-publication-delimitation sequence. Census 2027 reference dates are
  notified; publication and delimitation dates are not.
- **Four-ledger/PYQ control:** all direct and routed 2018-2025 Council,
  presiding-officer, Bill, finance and assent demands were retained. Parliament's
  Union procedure and the Governor's executive doctrine remain cross-owned.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    16: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://www.pmindia.gov.in/en/",
            "https://cabsec.gov.in/allocationofbusinessrules/completeaobrules/",
            "https://cabsec.gov.in/transactionofbusiness/transactionofbusinessrules/",
            "https://cabsec.gov.in/councilofministers/cabinetcommittees/",
        ],
        "Rechecked 2026-09-05: official PM India identifies Narendra Modi as "
        "Prime Minister. Articles 74-75 and 77-78 remain controlling; Cabinet "
        "Secretariat continues to publish the 1961 Allocation and Transaction of "
        "Business Rules. Cabinet-Committee composition remains notification-sensitive.",
    ),
    17: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://sansad.in/ls",
            "https://sansad.in/rs",
            "https://elibrary.sansad.in/items/a35ab2f4-b2b5-45a5-ae1d-0b79cf914adb/full",
            "https://egazette.gov.in/WriteReadData/2026/271834.pdf",
            "https://censusindia.gov.in/nada/index.php/metadata/export/45572/json",
            "https://elibrary.sansad.in/items/42c0a6ae-908c-4221-aaeb-554223bafd67",
        ],
        "Rechecked 2026-09-05: Om Birla is Lok Sabha Speaker and C. P. "
        "Radhakrishnan is Rajya Sabha Chairman. S.O. 1922(E) commenced the 106th "
        "Amendment on 16 April 2026, but Article 334A reservation remains "
        "non-operational. Census 2027 is notified; publication and delimitation "
        "dates are not. The 2026 delimitation-linked Bills did not become law.",
    ),
    18: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://www.sci.gov.in/chief-justice-judges/",
            "https://egazette.gov.in/WriteReadData/2026/275379.pdf",
            "https://www.sci.gov.in/collegium-resolutions/",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
        ],
        "Rechecked 2026-09-05: Justice Surya Kant is Chief Justice of India. "
        "Act 14 of 2026 raises the sanctioned strength to 38 including the CJI "
        "and is deemed in force from 16 May 2026. Working strength and pendency "
        "remain dynamic. The 20 November 2025 Article 143 opinion remains advisory.",
    ),
    19: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
            "https://api.sci.gov.in/supremecourt/2023/45314/45314_2023_11_1501_60770_Judgement_08-Apr-2025.pdf",
            "https://www.api.sci.gov.in/supremecourt/2020/18226/18226_2020_43_1501_28987_Judgement_03-Aug-2021.pdf",
            "https://api.sci.gov.in/supremecourt/2016/17865/17865_2016_5_1503_35995_Judgement_18-May-2022.pdf",
        ],
        "Rechecked 2026-09-05: 2025 INSC 1333 supplies the current Articles "
        "200-201 control: three options, Article 200 discretion, no merits review, "
        "rigid timeline or deemed assent, and limited mandamus for prolonged "
        "unexplained indefinite inaction. Article 161 can pardon a death sentence "
        "within the State offence-law field but has no court-martial limb.",
    ),
    20: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://dspstg.sansad.in/poi/state-legislatures",
            "https://api.sci.gov.in/supremecourt/2025/2745/2745_2025_1_1501_62743_Judgement_31-Jul-2025.pdf",
            "https://egazette.gov.in/WriteReadData/2026/271834.pdf",
            "https://censusindia.gov.in/nada/index.php/metadata/export/45572/json",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
        ],
        "Rechecked 2026-09-05: six States retain Legislative Councils. Padi "
        "Kaushik Reddy (2025), decided 31 July, confirms review and a case-specific "
        "three-month direction for Tenth-Schedule petitions. The 106th Amendment "
        "is commenced but reservation remains non-operational; Census 2027 "
        "reference dates do not supply publication or delimitation dates.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[str, ...]]] = {
    16: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\README.md",
            "upsc-ai-kit\\knowledge\\Polity\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "upsc-ai-kit\\knowledge\\Polity\\ANSWER-WORTHINESS-AUDIT.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\President-and-Vice-President.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Ministries-and-Departments-of-Government.md",
        ),
        "pyq": (
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2024-2025.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
        ),
    },
    17: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\README.md",
            "upsc-ai-kit\\knowledge\\Polity\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "upsc-ai-kit\\knowledge\\Polity\\ANSWER-WORTHINESS-AUDIT.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
        ),
        "pyq": (
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2024-2025.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
        ),
    },
}


def _topic_map(raw: dict[str, Any]) -> dict[str, Any]:
    topics = raw["topics"]
    if isinstance(topics, list):
        return {row["topic_key"]: row for row in topics}
    return topics


def _repair_current_law(topic_number: int, text: str) -> str:
    if topic_number == 16:
        text = text.replace(
            "| **Non-MP limit** | **6 months** (SC 1997) |",
            "| **Non-MP limit** | **6 consecutive months** (Article 75(5)) |",
        )
    if topic_number == 18:
        replacements = {
            "✅ **34** (1 CJI + 33; raised from 31 in 2019)": (
                "✅ **38** (1 CJI + 37; Act 14 of 2026, deemed in force 16 May 2026)"
            ),
            "📰 **34 on 28 Aug 2026**, counted from the official sitting-judges roster; re-verify before use": (
                "📰 **Dynamic official roster**; re-verify working strength before use"
            ),
            "Strength is **34** (1 CJI + 33), raised from 31 in **2019**": (
                "Sanctioned strength is **38** (1 CJI + 37) under Act 14 of 2026, "
                "deemed in force from **16 May 2026**"
            ),
            "[FACT] 34 including the CJI": "[FACT] 38 including the CJI",
            "Sanctioned strength is 34 including the CJI.": (
                "Sanctioned strength is 38 including the CJI."
            ),
            "Sanctioned strength | 34 including CJI": (
                "Sanctioned strength | 38 including CJI"
            ),
            "Sanctioned strength **34 including CJI**": (
                "Sanctioned strength **38 including CJI**"
            ),
            "sanctioned 34 including CJI | official sitting roster 34 | retirement 65": (
                "sanctioned 38 including CJI | working strength: live roster | retirement 65"
            ),
            "[CURRENT] 34 on 28 August 2026; re-verify before use": (
                "[CURRENT] Dynamic official roster; re-verify before use"
            ),
            "both were 34 on the dated": (
                "the two figures need not match on any dated"
            ),
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
    if topic_number == 19:
        replacements = {
            "Governor **cannot pardon a death sentence** and **cannot touch court-martial sentences**, but **may suspend, remit or commute** any sentence including a death sentence": (
                "Governor may **pardon, reprieve, respite, remit, suspend or commute** "
                "a sentence, including a death sentence, when the offence is against "
                "a law within State executive power; **court-martial remains outside "
                "Article 161**"
            ),
            "Governor (Art 161) **cannot pardon death/court-martial**; the President (Art 72) can": (
                "Governor (Art 161) may pardon within the State offence-law field "
                "but has no court-martial limb; President (Art 72) also covers "
                "court-martial and every death sentence"
            ),
            "the Governor cannot pardon a death sentence or deal with court-martial sentences; he may only suspend/remit/commute": (
                "the Governor may pardon within the State offence-law field, "
                "including a death sentence, but cannot exercise court-martial clemency"
            ),
            "The Governor acts for offences within State executive power, cannot exercise court-martial clemency and cannot pardon a death sentence, though suspension, remission or commutation remain possible.": (
                "The Governor acts for offences within State executive power and may "
                "pardon a death sentence within that field, but cannot exercise "
                "court-martial clemency."
            ),
            "Do not say the Governor has no power over a death sentence; the missing power is pardon, not suspension, remission or commutation.": (
                "Do not say the Governor cannot pardon a death sentence. Article "
                "161 permits pardon within the State offence-law field; the "
                "missing limb is court-martial and the President's separate power "
                "over every death sentence."
            ),
            "The Governor has no court-martial jurisdiction and cannot pardon a death sentence, though suspension, remission or commutation of that sentence is possible.": (
                "The Governor has no court-martial jurisdiction but may pardon a "
                "death sentence where the offence-law nexus lies within State "
                "executive power."
            ),
            "Governor cannot pardon death sentence but may suspend/remit/commute.": (
                "Governor may pardon a death sentence within the State offence-law "
                "field; court-martial remains outside Article 161."
            ),
            "The President can pardon a death sentence and court-martial punishment; the Governor cannot exercise those same limbs.": (
                "The President covers court-martial and every death sentence; the "
                "Governor may pardon a death sentence only within the State "
                "offence-law field and has no court-martial limb."
            ),
            "Governor: State-field offences; no court-martial limb; cannot pardon death sentence\nbut may suspend, remit or commute it. President has wider text.": (
                "Governor: State-field offences; may pardon death within that "
                "field; no court-martial limb.\nPresident: court-martial, "
                "Union-field offences and every death sentence."
            ),
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        text = re.sub(
            r"""#### OM28\. Death sentence and Article 161

The Governor:

A\. may pardon a death sentence and a court-martial sentence\.
B\. has no clemency role in death cases\.
C\. may deal with court-martial but not State offences\.
D\. cannot pardon a death sentence but may suspend, remit or commute it\.

\*\*Answer: D\.\*\*

\*\*Explanation:\*\* \[FACT\] This is the precise Article 161-Article 72 distinction\.""",
            """#### OM28. Death sentence and Article 161

The Governor:

A. may pardon every death sentence and every court-martial sentence.
B. has no clemency role in death-sentence cases.
C. may deal with court-martial but not State-field offences.
D. may pardon a death sentence where the offence-law nexus lies within State executive power, but has no court-martial limb.

**Answer: D.**

**Explanation:** [FACT] Article 161 is delimited by the State offence-law field; Article 72 separately covers court-martial and every death sentence.""",
            text,
        )
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = (
        ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    )
    for number in range(16, 21):
        key = f"polity-{number:02d}"
        path = directory / f"{key}-2026-08-24-sequential.json"
        source = _topic_map(json.loads(path.read_text(encoding="utf-8")))[key]
        panels = [
            (
                panel["title"],
                panel["structural_type"],
                _repair_current_law(number, panel["full_text"]),
                panel["source_references"],
            )
            for panel in source["panels"]
        ]
        if len(panels) != 12 or len({panel[0] for panel in panels}) != 12:
            raise ValueError(f"{key}: expected twelve unique authored panels.")
        configs[key] = {
            "key": key,
            "canonical": ROOT
            / "upsc-ai-kit"
            / "knowledge"
            / "Polity"
            / "learning-sessions"
            / "v2"
            / "subject-wide-syllabus"
            / f"{key}_Learning-Session.md",
            "panels": panels,
        }
    return configs


CURRENT_AUTHORING_CONFIGS = _load_authoring_configs()

_inherited_enforce_strict_rotation = deep.enforce_strict_rotation
_original_validate_spec = deep.deep._original_validate_spec


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 21)}:
        deep.deep.deep._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = deep.deep.deep.base.basic_mcq_area(repaired)
    keys = re.findall(r"(?im)^\*\*Answer:\s*([A-D])\.\*\*", area)
    if not keys:
        return repaired, metrics
    expected = ["ABCD"[index % 4] for index in range(len(keys))]
    if keys != expected:
        raise ValueError(
            "Non-standard MCQ headings prevent safe option rewriting and the "
            f"existing answer sequence is not strict A-B-C-D: {keys}"
        )
    return repaired, {"count": len(keys), "keys": keys, "unparsed": []}


def topics() -> list[deep.Topic]:
    manifest = deep.load(SECTION_MANIFEST)
    rows = manifest["topics"][:20]
    result: list[deep.Topic] = []
    for number, row in enumerate(rows, 1):
        override = SOURCE_OVERRIDES.get(number, {})
        cross = tuple(row.get("cross_topic_sources", [])) or override.get("cross", ())
        pyq = tuple(row.get("verified_pyq_sources", [])) or override.get("pyq", ())
        result.append(
            deep.Topic(
                number=number,
                topic_key=row["topic_key"],
                title=row["display_title"],
                basic_path=deep.repo(row["source_basic"]),
                canonical_path=deep.repo(row["source_canonical"]),
                advanced_path=deep.repo(row["source_advanced"]),
                cross_topic_sources=tuple(deep.repo(path) for path in cross),
                pyq_sources=tuple(deep.repo(path) for path in pyq),
            )
        )
    expected = [f"polity-{number:02d}" for number in range(1, 21)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-20 changed or are out of order.")
    return result


_inherited_augment = deep.deep.deep.augment_topic_semantic_content


def augment_topic_semantic_content(
    topic: deep.Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    repaired = _repair_current_law(topic.number, markdown)
    if workbook:
        return repaired
    return _inherited_augment(topic, repaired, workbook=False)


_inherited_owner_control = deep.ensure_canonical_owner_control


def ensure_canonical_owner_control(topic: deep.Topic) -> bool:
    changed = False
    for path in (
        topic.basic_path,
        Path(CURRENT_AUTHORING_CONFIGS[topic.topic_key]["canonical"]),
    ):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        repaired = _repair_current_law(topic.number, text)
        if repaired != text:
            path.write_text(repaired, encoding="utf-8")
            changed = True
    return _inherited_owner_control(topic) or changed


def apply_configuration() -> None:
    combined_points = {**deep.POLITY_REVIEW_POINTS, **POLITY_REVIEW_POINTS}
    combined_controls = {**deep.CANONICAL_OWNER_CONTROLS, **CANONICAL_OWNER_CONTROLS}
    combined_sources = {
        **deep.POLITY_LIVE_OFFICIAL_SOURCES,
        **POLITY_LIVE_OFFICIAL_SOURCES,
    }
    combined_configs = {**deep.CURRENT_AUTHORING_CONFIGS, **CURRENT_AUTHORING_CONFIGS}

    modules = (deep, deep.deep, deep.deep.deep)
    for module in modules:
        module.POLITY_REVIEW_POINTS = combined_points
        module.CANONICAL_OWNER_CONTROLS = combined_controls
        module.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
        module.CURRENT_AUTHORING_CONFIGS = combined_configs
        module.topics = topics
        module.enforce_strict_rotation = enforce_strict_rotation

    deep.deep.deep.augment_topic_semantic_content = augment_topic_semantic_content
    deep.deep.deep.base.WORKFLOW = "polity-16-20-hostile-semantic-immutable-successor"
    deep.deep.deep.base.SOCIETY_REVIEW_POINTS = combined_points
    deep.deep.deep.base.SOCIETY_LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.deep.base.LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.deep.base.CANONICAL_OWNER_CONTROLS = combined_controls
    deep.deep.deep.base.CURRENT_AUTHORING_CONFIGS = combined_configs
    deep.deep.deep.base.topics = topics
    deep.deep.deep.base.augment_topic_semantic_content = augment_topic_semantic_content
    deep.deep.deep.base.enforce_strict_rotation = enforce_strict_rotation
    deep.deep.deep.carvaka_flowchart.validate_spec = _validate_polity_graphical_spec


apply_configuration()

Topic = deep.Topic
STATUS = deep.STATUS
MASTER = deep.MASTER
REVIEW_ROOT = deep.REVIEW_ROOT
REVIEW_TRACKER = deep.REVIEW_TRACKER
REVIEW_TRACKER_MD = deep.REVIEW_TRACKER_MD
EXPORTS = deep.EXPORTS
INDEX_DIR = deep.INDEX_DIR

load = deep.load
dump = deep.dump
rel = deep.rel
repo = deep.repo
sha256 = deep.sha256
latest = deep.latest
process_topic = deep.process_topic
update_ledgers = deep.update_ledgers
generate_command_guide = deep.generate_command_guide
export_library = deep.export_library
add_final_library_paths = deep.add_final_library_paths
update_review_tracker = deep.update_review_tracker
validate_final_library = deep.validate_final_library
reconcile = deep.reconcile
add_all_operation_generation_paths = deep.add_all_operation_generation_paths
run_unittest = deep.run_unittest
completed_result = deep.completed_result
