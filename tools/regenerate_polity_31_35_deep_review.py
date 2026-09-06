"""Extend the hostile Polity deep-review workflow to topics 31-35."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_26_30_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST
PYQ_LEDGERS = deep.deep.deep.deep.deep.deep.PYQ_LEDGERS

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    31: (
        "Keep Articles 338, 338A and 338B distinct from Articles 341, 342 "
        "and 342A and from the temporary Article 340 commission route.",
        "Civil-court powers are evidentiary inquiry powers; recommendations, "
        "consultation and reports do not become binding judgments or list amendments.",
        "The 5 September 2026 roster check records the occupied and unfilled "
        "posts shown by the official NCSC, NCST and NCBC pages without inventing incumbents.",
    ),
    32: (
        "Separate constitutional status under Articles 148-151 from the detailed "
        "audit mandate supplied by the CAG's DPC Act, 1971 and its amendments.",
        "The CAG is an ex-post auditor and reports through legislatures; it does "
        "not pre-authorise expenditure, prosecute wrongdoing or enforce PAC action.",
        "The official CAG page identifies K. Sanjay Murthy as CAG from "
        "21 November 2024; the statutory term remains six years or age sixty-five.",
    ),
    33: (
        "Keep the constitutional Attorney General and Advocate General separate "
        "from the executive offices of Solicitor General and Additional Solicitors General.",
        "Pleasure tenure, legislative participation without vote, audience rights "
        "and professional-practice restrictions must be stated office by office.",
        "The 2025 Gazette reappointed R. Venkataramani as Attorney General for "
        "two years from 1 October 2025; the 2026 rules amendment concerns fees.",
    ),
    34: (
        "NITI Aayog is an executive, non-constitutional and non-statutory policy "
        "platform created by the Cabinet resolution of 1 January 2015.",
        "Advice, convening, monitoring and rankings do not confer legislative, "
        "taxing, devolution, fund-allocation or implementation powers.",
        "The 24 April 2026 Gazette replaced the Vice Chairperson and full-time "
        "member roster while retaining the July 2024 ex-officio members and invitees.",
    ),
    35: (
        "Use the Protection of Human Rights Act, 1993 as amended in 2019; keep "
        "NHRC and SHRC statutory rather than constitutional.",
        "Sections 12-14 inquiry powers and section 18 recommendations do not "
        "create criminal jurisdiction or self-executing compensation awards.",
        "The official roster identifies Justice V. Ramasubramanian and three "
        "full-time members; GANHRI alteration proceedings remain unresolved.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    31: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Articles 338, 338A and 338B establish the NCSC,
  NCST and NCBC. Articles 341, 342 and 342A separately govern the legal lists;
  Article 340 authorises temporary backward-class investigation commissions.
- **Composition and appointment:** each commission consists of a Chairperson,
  Vice-Chairperson and three other Members appointed by the President by
  warrant under hand and seal. The constitutional clauses leave service
  conditions and tenure to presidential rules.
- **Applicable tenure rules:** the NCSC and NCST 2004 rules and the NCBC 2018
  rules prescribe a three-year term from assumption of office. The rule source,
  not Article 338/338A/338B itself, supplies that duration.
- **Current occupied roster, checked 5 September 2026:** the official NCSC
  directory, updated 1 September 2026, displays Chairperson Kishor Makwana and
  Members Love Kush Kumar, Vaddepalli Ramchander and Dr Partha Biswas; the
  Vice-Chairperson line has no displayed incumbent. The official NCST material
  displays Chairperson Antar Singh Arya and Members Dr Asha Lakra, Nirupam
  Chakma and Jatothu Hussain, with no displayed Vice-Chairperson. The NCBC
  present-commission page displays Chairperson Sadhvi Niranjan Jyoti and Member
  Kiran Umesh Mahalle; no occupant is inferred for posts not displayed.
- **Common functions:** investigate and monitor safeguards; inquire into
  specific complaints; participate and advise in socio-economic planning;
  evaluate development; report to the President; recommend measures; and
  perform other functions specified by the President subject to law.
- **Inquiry and accountability:** civil-court powers apply while investigating
  or inquiring. Reports go through the President to Parliament with action-taken
  memoranda; State-related portions follow the Governor/State-legislature route.
  Recommendations and consultation are not binding decrees or vetoes.
- **Distinct mandates:** NCST carries additional tribal land, forest,
  displacement and resource concerns. NCBC's Article 338B role must be read with
  the 102nd Amendment, the Maratha-reservation judgment and the 105th Amendment,
  which expressly restored State/UT own-list competence under Article 342A(3).
- **List firewall:** commissions investigate and advise; the President and
  Parliament perform the constitutionally assigned SC/ST/Central-SEBC list
  functions, while States/UTs legislate their own SEBC lists under Article
  342A(3). Commission advice alone neither adds nor removes a community.
- **PYQ/ownership firewall:** minority-institution reservations remain bounded
  by Articles 15(5) and 30; Topic 26 owns Scheduled-Area administration and
  Topic 53 owns the wider special-provisions architecture. Direct 2018, 2020
  and 2022 commission demands retain their verified wording and ownership.""",
    32: """### Semantic-completeness ownership and PYQ control

- **Constitutional/statutory map:** Articles 148-151 create and protect the
  single Comptroller and Auditor General; Article 149 leaves detailed duties to
  Parliament, chiefly the Comptroller and Auditor-General's (Duties, Powers and
  Conditions of Service) Act, 1971, as amended in 1976, 1984, 1987 and 1994.
- **Current officeholder:** the official CAG page rechecked on 5 September 2026
  identifies Shri K. Sanjay Murthy, sworn in and assuming office on
  21 November 2024.
- **Appointment and tenure:** the President appoints by warrant under hand and
  seal. Section 4 of the 1971 Act fixes six years or age sixty-five, whichever
  is earlier. Removal follows the Supreme-Court-judge process; service
  conditions cannot be varied to disadvantage after appointment.
- **Independence:** salary and administrative expenses are charged on the
  Consolidated Fund of India, and the CAG is ineligible for further office
  under the Union or a State after demitting office. The Constitution prescribes
  no collegium for appointment.
- **Functions:** audit receipts and expenditure and the three public-account
  funds within the statutory mandate; audit grants, substantially financed
  bodies, government companies and corporations through their governing legal
  routes; advise the President on the form of accounts under Article 150; and
  finally certify net proceeds under Article 279.
- **Report route:** Union reports go to the President for laying before
  Parliament; State reports go to the Governor for laying before the State
  legislature. PAC/COPU scrutiny and executive follow-up give reports
  consequence; the CAG does not itself recover, prosecute or invalidate.
- **Audit limits:** India's CAG does not control the issue of money and is
  therefore a comptroller in name but an ex-post auditor in operation.
  Legality/compliance audit is mandatory; propriety and performance review must
  not become substitution of audit judgment for lawful policy choice.
- **Classification control:** there is no immutable constitutional list of
  exactly three reports, and entity labels alone do not decide audit coverage.
  Apply the DPC Act, Companies Act and entity statute rather than memorised lists.
- **PYQ/ownership firewall:** direct 2018 appointment-powers and 2024
  legality-propriety demands are owned here; Budget procedure, parliamentary
  committees and Finance Commission devolution remain cross-owned.""",
    33: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Article 76 creates the Attorney General for India;
  Article 165 creates an Advocate General for each State. The Solicitor General
  and Additional Solicitors General are executive law offices under Union rules,
  not constitutional offices.
- **Current Attorney General:** the official 2025 Gazette reappointed Senior
  Advocate R. Venkataramani for two years with effect from 1 October 2025.
  This dated appointment does not create a constitutional fixed-term rule.
  Advocate-General incumbents remain State-specific and must be sourced State by State.
- **Appointment and qualification:** the President appoints a person qualified
  to be a Supreme Court judge as Attorney General; the Governor appoints a
  person qualified to be a High Court judge as Advocate General.
- **Tenure and remuneration:** both offices are held during the pleasure of the
  relevant constitutional head; neither Article fixes a term or removal
  procedure. Remuneration is determined by the President or Governor.
- **Functions and rights:** the Attorney General advises the Government of
  India on referred legal matters, performs assigned constitutional/statutory
  functions and has a constitutional right of audience in all courts. Articles
  88 and 105(4) permit parliamentary participation and privileges without a vote.
  Articles 177 and 194(4) provide the State-legislature analogue.
- **Advocate-General limit:** Article 165 contains no counterpart to Article
  76(3)'s express all-India right of audience; court appearance therefore
  depends on applicable procedural and professional law.
- **Current rules:** the Law Officers (Conditions of Service) Rules, 1987
  govern the Union law officers. The Gazette-notified 2026 amendment changes
  Rule 7 fee/retainer provisions; it does not constitutionalise the SG/ASGs or
  give the Attorney General tenure security.
- **Professional limits:** the Attorney General is not a whole-time government
  servant and may practise privately subject to the rules, including conflict,
  adverse-brief, criminal-defence and directorship restrictions and permissions.
- **Enforcement boundary:** the section 15 Contempt of Courts Act consent role
  concerns specified private criminal-contempt motions; courts retain suo motu
  power. The law officer advises and represents, but does not adjudicate.
- **PYQ firewall:** the verified 2019 and 2025 Attorney-General demands are
  owned here; wider executive accountability and court procedure remain with
  their respective owners.""",
    34: """### Semantic-completeness ownership and PYQ control

- **Legal status:** NITI Aayog was created by the Union Cabinet resolution of
  1 January 2015. It is executive, non-constitutional and non-statutory; its
  advice becomes operative only through a competent legal or executive authority.
- **Institutional composition:** the Prime Minister is Chairperson. The design
  includes a Vice Chairperson, full-time members, up to two part-time members,
  up to four ex-officio Union Ministers, special invitees, a CEO and a Governing
  Council of State Chief Ministers, Chief Ministers of UTs with legislatures
  and Lieutenant Governors/Administrators of other UTs.
- **Latest formal composition control:** Cabinet Secretariat Notification
  No. 511/1/1/2024-Cab. dated 24 April 2026 appoints Ashok Kumar Lahiri as Vice
  Chairperson and Rajiv Gauba, Prof. K. V. Raju, Prof. Gobardhan Das,
  Prof. Abhay Karandikar and Dr M. Srinivas as full-time members, from
  assumption of charge until further orders. It retains the ex-officio members
  and special invitees in the 16 July 2024 notification.
- **Retained ex-officio members:** Raj Nath Singh, Amit Shah, Shivraj Singh
  Chouhan and Nirmala Sitharaman. The retained special invitees are Nitin
  Gadkari, J. P. Nadda, H. D. Kumaraswamy, Jitan Ram Manjhi, Rajiv Ranjan
  Singh, Virendra Kumar, K. Rammohan Naidu, Jual Oram, Annpurna Devi,
  Chirag Paswan and Rao Inderjit Singh, by the dated notifications.
- **Administrative roster:** the official 18 June 2026 directory identifies
  Nidhi Chhibber as CEO with additional charge. A directory entry is an
  operational snapshot, not a fixed constitutional or statutory tenure.
- **Functions:** foster cooperative federalism, formulate strategic policy,
  provide knowledge and technical support, monitor/evaluate programmes and use
  evidence, indices and initiatives to encourage learning and competition.
- **Limits:** NITI cannot legislate, tax, allocate the divisible pool, issue a
  Finance Commission award, bind States, or directly implement every programme.
  Rankings show measured performance; they do not by themselves prove causation.
- **Institution firewall:** Article 280 Finance Commission transfers, Article
  279A GST Council recommendations, Article 263 coordination and statutory
  Zonal Councils retain distinct sources and powers.
- **PYQ firewall:** the direct 2018 Planning-Commission comparison and routed
  2019 Atal Innovation Mission demand remain attached to this owner with
  notification-sensitive current composition.""",
    35: """### Semantic-completeness ownership and PYQ control

- **Legal status and latest law:** NHRC and SHRCs are statutory bodies under the
  Protection of Human Rights Act, 1993. The 2019 amendment remains the latest
  located amendment affecting composition and tenure on 5 September 2026.
- **NHRC statutory composition:** section 3 provides a Chairperson who has been
  CJI or a Supreme Court judge; one serving/former Supreme Court judge; one
  serving/former High Court Chief Justice; and three human-rights experts, at
  least one a woman. Seven named office-holders participate as deemed members
  for section 12(b)-(j), not section 12(a) complaint inquiries.
- **Current public roster:** the official NHRC composition page rechecked on
  5 September 2026 displays Chairperson Justice V. Ramasubramanian and Members
  Justice (Dr) Bidyut Ranjan Sarangi, Vijaya Bharathi Sayani and Priyank
  Kanoongo. No occupant is inferred for a statutory seat not displayed.
- **Appointment and tenure:** the President appoints NHRC members after the
  statutory six-member committee recommendation. The Governor appoints SHRC
  members after the State committee recommendation. The post-2019 term is
  three years or age seventy, whichever is earlier, with reappointment allowed.
- **Removal:** the President removes both NHRC and SHRC members. Proved
  misbehaviour or incapacity follows the statutory Supreme Court inquiry route;
  direct statutory grounds remain separate.
- **Functions and powers:** section 12 covers inquiries, court intervention with
  approval, institution visits, safeguard review, treaty study, research,
  literacy and NGO encouragement. Section 13 civil-court powers and section 14
  investigative assistance support fact-finding, not adjudication.
- **Limits:** section 18 outputs are recommendations, including relief,
  prosecution/action or approaching constitutional courts; they are not
  self-executing decrees. Section 19 substitutes a report-based armed-forces
  route. Section 36 bars duplicate inquiries and retains the one-year limit.
- **SHRC boundary:** a State may constitute an SHRC for State/Concurrent-list
  matters. The chair qualification, smaller ordinary membership and State
  selection committee differ, while President-only removal remains a federal safeguard.
- **International status:** the March 2025 GANHRI SCA recommendation and India's
  challenge remain distinct from a final alteration. GANHRI lists alteration
  of India's accreditation for a November 2026 session; do not report a
  completed downgrade on the 5 September 2026 control date.
- **PYQ firewall:** direct 2018 umbrella-commission and 2021 limitations/remedies
  demands are owned here; constitutional SC/ST/BC commissions remain Topic 31.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    31: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://ncsc.nic.in/who-is-who",
            "https://ncsc.nic.in/about-us/about-the-commission",
            "https://ncst.nic.in/page/about-the-commission",
            "https://ncst.nic.in/whos-who",
            "https://www.ncbc.nic.in/User_Panel/PresentCommissionView.aspx",
            "https://www.ncbc.nic.in/Writereaddata/23_08_2018.pdf",
            "https://api.sci.gov.in/supremecourt/2010/25536/25536_2010_1_1501_54462_Judgement_01-Aug-2024.pdf",
        ],
        "Rechecked 2026-09-05: Articles 338, 338A and 338B and the applicable "
        "2004/2018 tenure rules control institutional composition. Official "
        "rosters show the named occupied posts; unlisted posts are not assigned "
        "invented incumbents. Recommendations remain advisory.",
    ),
    32: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://cag.gov.in/en/page-duties-power-and-conditions-of-services-act",
            "https://cag.gov.in/uploads/media/DPC_Act_1971.pdf",
            "https://cag.gov.in/uploads/media/Amendments-to-the-CAG-s-DPC-Act-1971-20200729002457.pdf",
            "https://cag.gov.in/en/page-audit-regulations",
            "https://cag.gov.in/en/pages/single/17",
            "https://sansad.in/ls/committee/financial-committees/26-public%20accounts",
        ],
        "Rechecked 2026-09-05: Articles 148-151 and the DPC Act, 1971 as "
        "amended through 1994 remain the applicable framework. The official "
        "CAG page identifies K. Sanjay Murthy in office from 21 November 2024.",
    ),
    33: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://www.legalaffairs.gov.in/static/uploads/2025/11/2bac9e8f01fe8b23f940f8a25f4d8d13.pdf",
            "https://www.legalaffairs.gov.in/static/uploads/2026/03/ad2f61f6794d21d0c02c231d013eaebb.pdf",
            "https://www.indiacode.nic.in/handle/123456789/1631",
            "https://www.sci.gov.in/supreme-court-rules-2013/",
        ],
        "Rechecked 2026-09-05: R. Venkataramani's official reappointment runs "
        "for two years from 1 October 2025. Articles 76 and 165 still prescribe "
        "pleasure tenure; the 2026 Law Officers Rules amendment concerns fees.",
    ),
    34: (
        [
            "https://www.niti.gov.in/about-us/niti-aayog-constitution/cabinet-secretariat-resolution-dated-01-01-2015",
            "https://www.niti.gov.in/sites/default/files/2024-08/cabinet%20secretariat%20notification%20dated%2016.07.2024.pdf",
            "https://www.niti.gov.in/sites/default/files/2026-05/Revised-Composition-of-the-National-Institution-for-Transforming-India-NITI-Aayog-24-04-26_0.pdf",
            "https://www.niti.gov.in/sites/default/files/2026-06/Telephone-Directory-of-Officers-and-employees-of-NITI-Aayog-as-on-18-06-2026.pdf",
            "https://www.niti.gov.in/about-us/objectives-and-features",
            "https://www.niti.gov.in/about-us/niti-governing-council-meetings",
        ],
        "Rechecked 2026-09-05: the 24 April 2026 Cabinet Secretariat "
        "notification controls the Vice Chairperson and five full-time members, "
        "retains the July 2024 ex-officio/invitee roster, and the 18 June 2026 "
        "directory identifies the CEO on additional charge.",
    ),
    35: (
        [
            "https://www.indiacode.nic.in/handle/123456789/15709",
            "https://nhrc.nic.in/acts-and-rules/protection-human-rights-act-1993",
            "https://nhrc.nic.in/about-us/composition_of_commission",
            "https://www.ohchr.org/en/instruments-mechanisms/instruments/principles-relating-status-national-institutions-paris",
            "https://ganhri.org/accreditation/sca-reports/",
            "https://ganhri.org/upcoming-sessions/",
            "https://api.sci.gov.in/jonew/judis/25688.pdf",
            "https://api.sci.gov.in/jonew/judis/43775.pdf",
        ],
        "Rechecked 2026-09-05: the PHRA 1993 as amended in 2019 controls "
        "composition, three-year tenure and jurisdiction. The official NHRC "
        "page displays four ordinary incumbents; GANHRI alteration review "
        "remains pending rather than a completed downgrade.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[Path, ...]]] = {
    31: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Scheduled-and-Tribal-Areas.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions-Relating-to-Certain-Classes.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
                "upsc-ai-kit\\knowledge\\Social-Justice\\basic\\07_Scheduled-Castes-Rights-Atrocities-and-Welfare.md",
                "upsc-ai-kit\\knowledge\\Social-Justice\\basic\\08_Scheduled-Tribes-PVTGs-and-Tribal-Welfare.md",
                "upsc-ai-kit\\knowledge\\Social-Justice\\basic\\09_OBC-EWS-and-Social-Mobility.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    32: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
                "upsc-ai-kit\\knowledge\\Economy\\basic\\09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    33: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    34: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\15_Monitoring-Evaluation-and-Outcomes.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    35: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Commissions-SC-ST-BC.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Political-Theory\\basic\\17_Human-Rights-Civil-Liberties-and-Democratic-Rights.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
}

PANEL_CURRENT_CONTROLS = {
    31: (
        "Composition, appointment, tenure and procedure",
        "\n\nCURRENT ROSTER: 5 SEPTEMBER 2026\n"
        "NCSC: Kishor Makwana + Love Kush Kumar + Vaddepalli Ramchander + Dr Partha Biswas;\n"
        "Vice-Chairperson not displayed. NCST: Antar Singh Arya + Dr Asha Lakra\n"
        "+ Nirupam Chakma + Jatothu Hussain; Vice-Chairperson not displayed.\n"
        "NCBC page displays Sadhvi Niranjan Jyoti + Kiran Umesh Mahalle only.",
    ),
    32: (
        "Appointment tenure removal and independence",
        "\n\nCURRENT OFFICEHOLDER: 5 SEPTEMBER 2026\n"
        "K. Sanjay Murthy was sworn in and assumed office on 21 November 2024.\n"
        "The officeholder changes; Article 148 and section 4 tenure rules do not.",
    ),
    33: (
        "Qualifications appointment tenure and remuneration",
        "\n\nCURRENT OFFICEHOLDER: 5 SEPTEMBER 2026\n"
        "R. Venkataramani: reappointed for two years from 1 October 2025.\n"
        "This appointment term does not replace Article 76 pleasure tenure.",
    ),
    34: (
        "Composition and notification-sensitive roles",
        "\n\nLATEST FORMAL ROSTER: 24 APRIL 2026\n"
        "Vice Chairperson: Ashok Kumar Lahiri.\n"
        "Full-time: Rajiv Gauba | K. V. Raju | Gobardhan Das\n"
        "| Abhay Karandikar | M. Srinivas.\n"
        "Ex-officio members and special invitees remain those in the 16 July 2024 notice.",
    ),
    35: (
        "NHRC composition and deemed-member boundary",
        "\n\nCURRENT PUBLIC ROSTER: 5 SEPTEMBER 2026\n"
        "Chair: Justice V. Ramasubramanian.\n"
        "Members: Justice (Dr) Bidyut Ranjan Sarangi | Vijaya Bharathi Sayani\n"
        "| Priyank Kanoongo. Do not infer occupants for undisplayed statutory seats.",
    ),
}

PANEL_BODY_OVERRIDES = {
    (
        35,
        "Paris Principles, accreditation and case-law controls",
    ): """PARIS PRINCIPLES, 1993
broad mandate | pluralism | open appointment | adequate resources
| stable tenure | independent methods | accessibility.

DOMESTIC TEST
PHRA mandate and inquiry powers versus police/deputation dependence,
short terms, selection opacity and weak follow-up.

GANHRI CONTROL
March 2025 SCA recommended B downgrade; India challenged.
Alteration of India's accreditation is listed for a November 2026 session.
SAFE LANGUAGE: unresolved official scrutiny, not a completed downgrade.

CASE CONTROLS
Paramjit Kaur v. State of Punjab (1999): Court-assigned Article 32 expert role
does not erase ordinary PHRA limits.
N.C. Dhoundial v. Union of India (2003): section 36(2) is jurisdictional;
non-reparation does not make a completed act a daily continuing wrong.
EEVFAM (2016): unlawful-force allegations require lawful inquiry;
NHRC is valuable but neither exclusive nor generally binding.

SYNTHESIS
Court-assigned expertise may exceed the ordinary route,
but autonomous statutory action remains bounded by the PHRA.""",
}


def _topic_map(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    topics_value = raw["topics"]
    if isinstance(topics_value, list):
        return {row["topic_key"]: row for row in topics_value}
    return topics_value


def _repair_current_law(topic_number: int, text: str) -> str:
    text = text.replace("28 August 2026", "5 September 2026")
    text = text.replace("28 Aug 2026", "5 Sep 2026")
    text = text.replace("24 August 2026", "5 September 2026")
    text = text.replace("21 Jul 2026", "5 Sep 2026")
    text = text.replace("21 July 2026", "5 September 2026")
    if topic_number == 32:
        text = text.replace(
            "no volatile officeholder, report count or headline loss figure is frozen.",
            "the current officeholder is K. Sanjay Murthy from 21 November 2024; "
            "no volatile report count or headline loss figure is frozen.",
        )
    if topic_number == 33:
        text = text.replace(
            "Officeholder names are deliberately not frozen.",
            "R. Venkataramani's two-year reappointment from 1 October 2025 is "
            "the dated current officeholder control.",
        )
    if topic_number == 34:
        text = text.replace(
            "Officeholder lists and State rankings are not frozen.",
            "The 24 April 2026 Gazette roster is frozen only as a dated composition "
            "snapshot; State rankings remain variable.",
        )
    if topic_number == 35:
        text = text.replace(
            "volatile composition/count data omitted.",
            "the official current roster is stated only as a dated snapshot.",
        )
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    for number in range(31, 36):
        key = f"polity-{number:02d}"
        path = directory / f"{key}-2026-08-24-sequential.json"
        source = _topic_map(json.loads(path.read_text(encoding="utf-8")))[key]
        title_match, addition = PANEL_CURRENT_CONTROLS[number]
        panels = []
        found = False
        for panel in source["panels"]:
            body = _repair_current_law(number, panel["full_text"])
            body = PANEL_BODY_OVERRIDES.get((number, panel["title"]), body)
            if panel["title"] == title_match:
                body = body.rstrip() + addition
                found = True
            panels.append(
                (
                    panel["title"],
                    panel["structural_type"],
                    body,
                    panel["source_references"],
                )
            )
        if not found:
            raise ValueError(f"{key}: current-composition panel was not found.")
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
_inherited_augment = deep.augment_topic_semantic_content
_inherited_owner_control = deep.ensure_canonical_owner_control


def _deepest_module() -> Any:
    module = deep
    while hasattr(module, "deep"):
        module = module.deep
    return module


_engine = _deepest_module()
_original_validate_spec = _engine.carvaka_flowchart.validate_spec


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 36)}:
        _engine._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = _engine.base.basic_mcq_area(repaired)
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
    rows = manifest["topics"][:35]
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
                cross_topic_sources=tuple(
                    path if isinstance(path, Path) else deep.repo(path) for path in cross
                ),
                pyq_sources=tuple(
                    path if isinstance(path, Path) else deep.repo(path) for path in pyq
                ),
            )
        )
    expected = [f"polity-{number:02d}" for number in range(1, 36)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-35 changed or are out of order.")
    return result


def generation_sources(
    topic: deep.Topic,
    record: dict[str, Any],
) -> tuple[str, str]:
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    if not workbook_value:
        raise ValueError(f"{topic.topic_key}: accepted workbook Markdown is missing.")
    return (
        deep.repo(record["markdown"]).read_text(encoding="utf-8"),
        deep.repo(workbook_value).read_text(encoding="utf-8"),
    )


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

    modules = []
    module = deep
    while True:
        modules.append(module)
        if not hasattr(module, "deep"):
            break
        module = module.deep
    for module in modules:
        module.POLITY_REVIEW_POINTS = combined_points
        module.CANONICAL_OWNER_CONTROLS = combined_controls
        module.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
        module.CURRENT_AUTHORING_CONFIGS = combined_configs
        module.topics = topics
        module.enforce_strict_rotation = enforce_strict_rotation

    engine = modules[-1]
    engine.augment_topic_semantic_content = augment_topic_semantic_content
    engine.base.WORKFLOW = "polity-31-35-hostile-semantic-immutable-successor"
    engine.base.SOCIETY_REVIEW_POINTS = combined_points
    engine.base.SOCIETY_LIVE_OFFICIAL_SOURCES = combined_sources
    engine.base.LIVE_OFFICIAL_SOURCES = combined_sources
    engine.base.CANONICAL_OWNER_CONTROLS = combined_controls
    engine.base.CURRENT_AUTHORING_CONFIGS = combined_configs
    engine.base.topics = topics
    engine.base.generation_sources = generation_sources
    engine._base_build_ascii_spec_iac = engine._base_build_ascii_spec
    engine.base.augment_topic_semantic_content = augment_topic_semantic_content
    engine.base.enforce_strict_rotation = enforce_strict_rotation
    engine.carvaka_flowchart.validate_spec = _validate_polity_graphical_spec


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
