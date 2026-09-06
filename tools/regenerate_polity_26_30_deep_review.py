"""Extend the hostile Polity deep-review workflow to topics 26-30."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_21_25_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    26: (
        "Keep Article 244, Article 244A, the Fifth Schedule and the Sixth "
        "Schedule separate before adding the statutory PESA and FRA layers.",
        "PESA section 4 uses distinct verbs: approval, consultation, mandatory "
        "prior recommendation, ownership and control. None creates one universal veto.",
        "The 4 August 2026 MHA parliamentary answer identifies ten Sixth-Schedule "
        "ADCs in four States; Ladakh remains outside the Sixth Schedule.",
    ),
    27: (
        "Separate Article 324, Articles 325-329, the RPA 1950, the RPA 1951, "
        "the 2023 appointment Act and the non-statutory Model Code.",
        "The ECI conducts Union, State, Presidential and Vice-Presidential "
        "elections; State Election Commissions conduct local-body elections, "
        "and the Delimitation Commission remains a distinct statutory body.",
        "The official ECI roster lists CEC Gyanesh Kumar and ECs Dr Sukhbir "
        "Singh Sandhu and Dr Vivek Joshi. The 2023 Act operates while its "
        "section 7 challenge remains undecided.",
    ),
    28: (
        "Audit Articles 315-323 actor by actor across UPSC, SPSC and a Joint "
        "State PSC; constitutional existence does not mean constitutionally fixed strength.",
        "Only the President removes any PSC member, but pending an Article 317 "
        "reference the President suspends UPSC/Joint PSC members and the Governor "
        "suspends an SPSC member.",
        "The official UPSC page identifies Dr Ajay Kumar as Chairman. Article "
        "320 consultation remains directory under Manbodhan Lal, while valid "
        "exemption regulations and Article 323 reporting preserve accountability.",
    ),
    29: (
        "Keep Article 280 Finance Commission, State Finance Commissions and "
        "the Article 279A GST Council institutionally and functionally distinct.",
        "Vertical devolution applies to Article 270 net proceeds, not gross tax "
        "revenue; Article 271 surcharges and applicable cesses stay outside the divisible pool.",
        "The Sixteenth Finance Commission report and February 2026 Explanatory "
        "Memorandum control the 2026-31 award: 41 per cent vertical share and "
        "the accepted six-criterion horizontal formula.",
    ),
    30: (
        "Separate Articles 246A, 269A and 279A, the Council's recommendation, "
        "legislative enactment and delegated notification at every stage.",
        "Quorum is one-half; the Union has one-third vote weight, States together "
        "two-thirds, and a decision needs at least three-fourths of weighted votes "
        "of members present and voting.",
        "The 56th meeting of 3 September 2025 is the latest official meeting "
        "release located. Mohit Minerals remains the controlling rule that Council "
        "recommendations are persuasive, not binding.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    26: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Article 244(1) applies the Fifth Schedule to Scheduled
  Areas and Scheduled Tribes in States other than Assam, Meghalaya, Tripura and
  Mizoram; Article 244(2) applies the Sixth Schedule to tribal areas in those
  four States. Article 244A is a separate parliamentary route for an autonomous
  State within Assam.
- **Fifth-Schedule territory:** the President declares, enlarges, diminishes,
  alters or rescinds a Scheduled Area by order after the constitutional
  consultation route. Official Ministry of Tribal Affairs material continues
  to list Scheduled Areas in ten States.
- **Fifth-Schedule administration:** State executive power extends to Scheduled
  Areas; the Governor reports annually, or whenever required, to the President;
  and Union executive power extends to directions regarding administration.
- **TAC precision:** a Tribes Advisory Council has not more than twenty members.
  As nearly as may be, three-fourths are representatives of Scheduled Tribes in
  the State Legislative Assembly, with the Schedule's shortfall rule. It advises
  on welfare and advancement matters referred by the Governor; it does not legislate.
- **Governor's paragraph 5 power:** by public notification the Governor may
  direct that an Act does not apply, or applies with exceptions/modifications,
  and may make peace-and-good-government regulations on tribal land transfer,
  land allotment and money-lending. Regulations require presidential assent and,
  where a TAC exists, consultation with it.
- **Sixth-Schedule institutions:** the Governor organises autonomous districts
  and regions. District and Regional Councils exercise textually specified
  legislative, judicial, executive and revenue powers; council laws requiring
  assent, State-law application and parliamentary-law application remain
  paragraph- and State-specific rather than one blanket rule.
- **Current council map:** an official MHA Lok Sabha answer dated 4 August 2026
  lists ten Sixth-Schedule Autonomous District Councils: three in Assam, three
  in Meghalaya, three in Mizoram and one in Tripura. Special council designs,
  including Bodoland, must not be replaced by the ordinary maximum-thirty model.
- **PESA verbs:** section 4 of the PESA Act, 1996 distinguishes Gram Sabha
  approval of plans/programmes/projects, beneficiary identification, utilisation
  certification, consultation before land acquisition and rehabilitation, and
  mandatory prior recommendation for specified minor-mineral licences, leases
  and concessions. Ownership of minor forest produce and specified control
  powers do not create a universal project veto.
- **FRA and judgments:** the Forest Rights Act, 2006 has its own rights-recognition
  process initiated through the Gram Sabha. Samatha (1997) is used within its
  Andhra Pradesh Scheduled-Area land-transfer setting. Orissa Mining Corporation
  (2013) required Gram Sabha determination of specified FRA-linked cultural and
  religious claims at Niyamgiri while leaving the final Stage-II decision with MoEF.
- **Ownership/PYQ firewall:** Topic 23 owns Panchayat structure and the PESA
  local-government bridge; Topic 22 owns Articles 371-371J; Topic 31 owns the
  National Commissions; Topic 53 owns the wider special-provisions-for-classes
  architecture. Direct and routed 2019-2026 Scheduled-Area demands retain their
  official-key or answer-free status without fabricated answer letters.""",
    27: """### Semantic-completeness ownership and PYQ control

- **Constitution/statute map:** Article 324 vests superintendence, direction and
  control of electoral rolls and elections in the ECI; Articles 325-329 add the
  common-roll, adult-suffrage, legislative and election-petition framework. The
  RPA 1950 chiefly governs rolls and allocation architecture; the RPA 1951
  governs conduct, corrupt practices, disqualifications and election petitions.
- **Institution boundary:** the ECI conducts elections to Parliament, State
  legislatures, President and Vice-President. State Election Commissions conduct
  Panchayat and municipal elections. A Delimitation Commission, when constituted
  by statute, is not the ECI acting alone.
- **Current composition:** the official ECI leadership page rechecked on
  5 September 2026 lists Chief Election Commissioner Gyanesh Kumar and Election
  Commissioners Dr Sukhbir Singh Sandhu and Dr Vivek Joshi.
- **Act 49 of 2023:** eligible appointees must hold or have held Secretary-to-
  Government-of-India-equivalent rank and possess integrity plus election-
  management knowledge and experience. The Law Minister heads the three-member
  Search Committee that prepares five names.
- **Selection and service:** the President appoints on the recommendation of
  the Prime Minister, Leader of Opposition (or leader of the largest opposition
  party) and a PM-nominated Union Cabinet Minister. The Selection Committee may
  consider a person outside the Search Committee panel. Term is six years or
  age sixty-five, whichever is earlier; reappointment is barred and aggregate
  EC-plus-CEC tenure cannot exceed six years. Salary equals that of a Supreme
  Court judge.
- **Removal and business:** the CEC is removed like a Supreme Court judge; an
  Election Commissioner or Regional Commissioner is removed only on the CEC's
  recommendation. Commission business should be unanimous where possible and
  otherwise follows the majority under section 18 of the 2023 Act.
- **Appointment litigation:** Anoop Baranwal (2023) supplied the PM-LoP-CJI
  arrangement only until Parliament enacted a law. Dr Jaya Thakur (2024 INSC 246)
  refused interim stay and made its observations tentative. No later official
  stay or merits judgment was located by 5 September 2026; the Act operates
  while the section 7 challenge remains pending.
- **EVM-VVPAT control:** Association for Democratic Reforms v ECI, 2024 INSC
  341, refused a return to paper ballots and 100 per cent VVPAT counting while
  directing forty-five-day sealing of Symbol Loading Units and a candidate-
  requested post-result microcontroller verification route.
- **Electoral-roll control:** Association for Democratic Reforms v ECI, 2026
  INSC 564, upheld the Bihar Special Intensive Revision framework, recognised a
  limited ECI eligibility/citizenship inquiry for electoral purposes, denied it
  final citizenship-determination power and required reference to the competent
  Citizenship Act authority where citizenship remained in issue.
- **PYQ firewall:** direct election-reform, Model Code, corrupt-practice,
  delimitation and candidature demands remain attached to their verified
  ledgers. Electoral bonds, anti-defection, local elections and full
  delimitation doctrine retain their separate owners and are only bridged here.""",
    28: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Articles 315-323 separately govern establishment,
  appointment/tenure, removal/suspension, service conditions, post-office bars,
  functions, extension of functions, charged expenditure and annual reporting
  for the UPSC, SPSCs and Joint State Public Service Commissions.
- **Composition:** the Constitution fixes no numerical strength. The President
  appoints UPSC and Joint Commission members and determines their number/service
  conditions under Article 318; the Governor performs the corresponding SPSC
  functions. As nearly as may be, one-half of members must have held government
  office for at least ten years.
- **Current UPSC control:** the official UPSC Commission page, last updated
  3 September 2026 and rechecked 5 September 2026, identifies Dr Ajay Kumar as
  Chairman. The package does not freeze an unsupported full roster or a
  constitutionally fixed member count.
- **Tenure and acting chair:** Article 316 gives six years subject to age
  sixty-five for UPSC and sixty-two for SPSC/Joint Commission members. The
  President or Governor, as applicable, may appoint a member as acting chair.
- **Removal/suspension precision:** only the President removes any PSC member.
  Misbehaviour requires a presidential reference, Supreme Court inquiry and
  recommendation under Article 317(1). Pending inquiry, the President may
  suspend a UPSC or Joint Commission member, while the Governor may suspend an
  SPSC member. Article 317(3)-(4) contains the separate objective/deemed grounds.
- **Post-office and finance:** Article 319's eligibility bars are office-specific
  and do not mean one blanket ban. Article 322 charges UPSC/Joint Commission
  expenses on the Consolidated Fund of India and SPSC expenses on the
  Consolidated Fund of the State.
- **Functions and exclusions:** Article 320 covers examinations, recruitment
  methods, appointments/promotions/transfers and disciplinary/claim advice.
  Article 320(4) excludes consultation on Article 16(4) and Article 335 matters;
  the proviso to Article 320(3) authorises valid exemption regulations.
- **Judicial rule:** State of U.P. v Manbodhan Lal Srivastava (1957) holds
  Article 320(3)(c) consultation directory: non-consultation does not by itself
  invalidate action or confer a cause of action. Advice remains institutionally
  important and Article 323 requires reports plus reasons for non-acceptance.
- **Recruitment rule:** selection/recommendation does not itself create an
  indefeasible right to appointment. Tej Prakash Pathak (2024 INSC 847) supplies
  the current Constitution-Bench control against arbitrary mid-process changes
  to recruitment rules, subject to the governing rules and non-arbitrariness.
- **Institution firewall:** UPSC/SPSC recruitment and advice are distinct from
  DoPT cadre administration, the Public Examinations Act integrity framework,
  tribunals, Election Commissions and Finance Commissions. A Joint State PSC
  follows State resolutions and parliamentary law; it is not a permanent third
  constitutionally mandated tier.""",
    29: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Article 280 requires a Finance Commission every fifth
  year or earlier, consisting of a Chairman and four other members appointed by
  the President. Article 281 requires the report and an explanatory memorandum
  on action taken to be laid before Parliament.
- **Statutory qualifications:** the Finance Commission (Miscellaneous Provisions)
  Act, 1951 requires public-affairs experience for the Chairman and draws the
  four members from High-Court judicial qualification, government finance and
  accounts, financial administration and economics. Disqualification and
  financial-interest safeguards are statutory, not invented constitutional text.
- **Current composition:** the Sixteenth Finance Commission was chaired by
  Dr Arvind Panagariya, with full-time members Annie George Mathew and Dr Manoj
  Panda and part-time members T. Rabi Sankar and Dr Soumya Kanti Ghosh. It was
  constituted on 31 December 2023 and submitted its report on 17 November 2025.
- **Vertical devolution:** the February 2026 Explanatory Memorandum records
  Government acceptance of the Commission's recommendation to retain States'
  share at 41 per cent of Article 270 net proceeds for 2026-27 to 2030-31.
  This is not 41 per cent of gross Union tax revenue.
- **Horizontal formula:** the accepted formula assigns 42.5 per cent to per-
  capita GSDP distance, 17.5 per cent to 2011 population and 10 per cent each
  to demographic performance, area, forest and contribution to GDP. The last
  criterion is new; tax/fiscal effort is not a separate Sixteenth-FC weight.
- **Grant status:** no revenue-deficit, sector-specific or State-specific grants
  were recommended. Government took note of that assessment. The accepted
  local-body design totals Rs 7,91,493 crore over five years; the accepted
  State disaster-fund corpus totals Rs 2,04,401 crore. These are award envelopes,
  not annual releases.
- **Local bodies:** Article 280(3)(bb) and (c) concern augmentation of State
  Consolidated Funds on the basis of State Finance Commission recommendations.
  The national Finance Commission does not replace Articles 243-I and 243-Y SFCs.
- **Divisible-pool firewall:** Article 279 defines net proceeds and makes the
  CAG certificate final; Article 270 governs sharing; Article 271 surcharges
  and applicable specific-purpose cesses remain outside the divisible pool.
  Article 275 grants and Article 282 discretionary public-purpose grants are distinct.
- **Advisory status:** Finance Commission recommendations are not judicial
  decrees. Recommendation, Government acceptance, presidential order, budgetary
  provision, release and expenditure are separate stages.
- **Institution/PYQ firewall:** the Article 280 Finance Commission is distinct
  from the GST Council, NITI Aayog and State Finance Commissions. Direct 2018
  constitution/terms-of-reference and 2020 fiscal-position Mains demands and
  routed 2023/2025 objective demands retain their verified ownership and key status.""",
    30: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** the 101st Amendment inserted Articles 246A, 269A and
  279A and amended related provisions. Article 246A creates simultaneous Union-
  State GST competence subject to Parliament's exclusive inter-State field;
  Article 269A governs inter-State levy/collection and apportionment; Article
  279A creates the recommendatory Council.
- **Composition:** the Union Finance Minister chairs; the Union Minister of State
  in charge of Revenue or Finance and one finance/taxation or nominated Minister
  from each State are members. State members may choose a Vice-Chairperson.
  Nirmala Sitharaman remains the official Union Finance Minister/current Chair
  on the 5 September 2026 control date.
- **Voting:** one-half of total membership is quorum. At a meeting the Union has
  one-third of total votes cast, States together two-thirds, and a proposal
  requires at least three-fourths of weighted votes of members present and voting.
  Quorum, vote weight and decision threshold must never be conflated.
- **Procedure rules:** the official Conduct of Business Rules provide ordinarily
  seven days' meeting notice, agenda notes at least three days before the meeting
  and a two-day emergency-meeting route with Chair approval. The Vice-Chairperson
  has a two-year term or until ceasing to be a member/resigning, whichever is earlier.
- **Secretariat boundary:** the Revenue Secretary is ex-officio Secretary and
  the CBIC Chair is a permanent non-voting invitee by the 2016 Cabinet decision;
  neither becomes a voting constitutional member. GSTN and GSTAT are different institutions.
- **Recommendation-to-law chain:** a Council recommendation is not a tax rate
  by itself. Parliament/State law and valid delegated notifications give legal
  effect subject to the governing statute and constitutional competence.
- **Judicial rule:** Union of India v Mohit Minerals (2022) holds Council
  recommendations persuasive rather than binding because Union and States hold
  simultaneous Article 246A legislative power. The ocean-freight levy failed
  on the statutory/constitutional analysis; the case does not erase the Council.
- **Current meeting:** the official 56th GST Council release dated 3 September
  2025 is the latest meeting release located by 5 September 2026. It recommended
  broad 5 and 18 per cent rates plus a special 40 per cent demerit rate, with
  most changes intended from 22 September 2025. Every supply-specific legal rate
  still requires the applicable CBIC notification.
- **Compensation status:** the statutory five-year State-compensation entitlement
  ended in June 2022. Under the 56th-meeting official material, compensation
  cess continued on specified tobacco-related goods until discharge of the
  related loan and interest liabilities; no universal post-2022 entitlement is implied.
- **Institution/PYQ firewall:** the GST Council does not distribute the divisible
  pool (Finance Commission), administer GST (tax administrations), operate the
  network (GSTN) or adjudicate appeals (GSTAT). The direct 2023 accommodative-
  federalism Mains demand and routed GST/fiscal-federalism demands retain their
  verified ownership.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    26: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://tribal.nic.in/DivisionsFiles/clm/ScheduledAreas.pdf",
            "https://www.indiacode.nic.in/show-data?actid=AC_CEN_18_21_00007_199640_1517807323053&sectionId=42808&sectionno=4&orderno=4",
            "https://tribal.nic.in/FRA/data/FRARulesBook.pdf",
            "https://www.mha.gov.in/MHA1/Par2017/pdfs/par2026-pdfs/LS04082026/2745.pdf",
            "https://api.sci.gov.in/judis/4271.pdf",
            "https://api.sci.gov.in/judis/19058.pdf",
        ],
        "Rechecked 2026-09-05: official constitutional, MoTA, MoPR/India Code, "
        "MHA and Supreme Court sources preserve distinct Fifth Schedule, Sixth "
        "Schedule, PESA and FRA layers. MHA's 4 August 2026 answer lists ten "
        "Sixth-Schedule ADCs; Ladakh has not been added to the Schedule.",
    ),
    27: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://www.eci.gov.in/honble-commission/",
            "https://www.indiacode.nic.in/indiacode/bitstream/123456789/19721/1/a2023-49.pdf",
            "https://api.sci.gov.in/pdfdate/index1.php?dt=2023-03-02&dno=14582015&filename=supremecourt/2015/1458/1458_2015_3_1501_42634_Judgement_02-Mar-2023.pdf",
            "https://api.sci.gov.in/supremecourt/2024/146/146_2024_2_1501_51762_Judgement_22-Mar-2024.pdf",
            "https://api.sci.gov.in/supremecourt/2023/10857/10857_2023_2_1501_52646_Judgement_26-Apr-2024.pdf",
            "https://api.sci.gov.in/supremecourt/2025/35785/35785_2025_1_1501_71617_Judgement_27-May-2026.pdf",
        ],
        "Rechecked 2026-09-05: the official ECI roster lists Gyanesh Kumar, "
        "Dr Sukhbir Singh Sandhu and Dr Vivek Joshi. Act 49 of 2023 operates; "
        "no later official stay or merits decision on section 7 was located. "
        "The 2024 EVM-VVPAT and 2026 electoral-roll judgments are binding controls.",
    ),
    28: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://upsc.gov.in/about-us/commission-",
            "https://upload.indiacode.nic.in/showfile?actid=AC_CEN_28_38_00013_200755_1517807323574&type=rule&filename=exemption-upsc-1.pdf",
            "https://www.indiacode.nic.in/handle/123456789/20100?view_type=search&col=123456789/1362",
            "https://api.sci.gov.in/jonew/judis/611.pdf",
            "https://api.sci.gov.in/supremecourt/2011/13164/13164_2011_1_1501_57036_Order_07-Nov-2024.pdf",
        ],
        "Rechecked 2026-09-05: the official UPSC Commission page, last updated "
        "3 September 2026, identifies Dr Ajay Kumar as Chairman. The Constitution, "
        "consultation regulations, Public Examinations Act and binding recruitment "
        "judgments remain separate controls; no unsupported full roster is frozen.",
    ),
    29: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://www.indiacode.nic.in/ViewFileUploaded?path=AC_CEN_2_11_00033_195133_1517807323203/actfile/&file=A1951-33.pdf",
            "https://fincomindia.nic.in/compositions",
            "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/reports/Vol1-Main-Report.pdf",
            "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/16fc-EM.pdf",
            "https://www.indiabudget.gov.in/doc/16fc.pdf",
        ],
        "Rechecked 2026-09-05: the official Sixteenth Finance Commission "
        "composition, report and February 2026 Explanatory Memorandum confirm "
        "the 2026-31 award, 41 per cent vertical share, accepted horizontal "
        "formula and the exact recommendation/acceptance distinctions.",
    ),
    30: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://gstcouncil.gov.in/en/gst-council",
            "https://gstcouncil.gov.in/sites/default/files/2024-02/procedure_conduct_business.pdf",
            "https://gstcouncil.gov.in/sites/default/files/2025-09/press_release_press_information_bureau.pdf",
            "https://gstcouncil.gov.in/sites/default/files/2025-09/faq_0.pdf",
            "https://api.sci.gov.in/pdfdate/index1.php?dno=230832020&dt=2022-05-19&filename=supremecourt/2020/23083/23083_2020_4_1501_35969_Judgement_19-May-2022.pdf",
        ],
        "Rechecked 2026-09-05: Article 279A and the official Conduct of Business "
        "Rules control composition, quorum and voting. The 56th meeting release "
        "of 3 September 2025 is the latest official meeting outcome located; "
        "Mohit Minerals remains controlling and recommendations are not self-executing.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[str, ...]]] = {
    26: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\National-Commissions-SC-ST-BC.md",
            "upsc-ai-kit\\knowledge\\Environment-and-Ecology\\basic\\12_Forest-Governance-CAMPA-and-Green-India-Mission.md",
        ),
        "pyq": deep.deep.deep.deep.deep.PYQ_LEDGERS,
    },
    27: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
        ),
        "pyq": deep.deep.deep.deep.deep.PYQ_LEDGERS,
    },
    28: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Public-Services.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Governance\\basic\\09_Civil-Services-and-Mission-Karmayogi.md",
        ),
        "pyq": deep.deep.deep.deep.deep.PYQ_LEDGERS,
    },
    29: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Municipalities.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CAG.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\NITI-Aayog.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md",
        ),
        "pyq": deep.deep.deep.deep.deep.PYQ_LEDGERS,
    },
    30: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Economy\\basic\\10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism.md",
        ),
        "pyq": deep.deep.deep.deep.deep.PYQ_LEDGERS,
    },
}


def _topic_map(raw: dict[str, Any]) -> dict[str, Any]:
    topics_value = raw["topics"]
    if isinstance(topics_value, list):
        return {row["topic_key"]: row for row in topics_value}
    return topics_value


def _repair_current_law(topic_number: int, text: str) -> str:
    text = text.replace("28 August 2026", "5 September 2026")
    text = text.replace("28 Aug 2026", "5 Sep 2026")
    text = text.replace("24 August 2026", "5 September 2026")
    if topic_number == 26:
        text = text.replace(
            "PESA's Gram-Sabha consent",
            "PESA's differentiated Gram-Sabha approval, consultation and recommendation powers",
        )
        text = text.replace(
            "PESA consultation, recommendation and approval verbs",
            "PESA approval, consultation, recommendation, ownership and control verbs",
        )
    if topic_number == 27:
        text = text.replace(
            "The official Supreme Court record confirms the 22 March 2024 refusal "
            "of interim interference.",
            "The official Supreme Court record confirms the 22 March 2024 refusal "
            "of interim interference; 2026 INSC 564 separately controls the "
            "electoral-roll/citizenship boundary.",
        )
    if topic_number == 28:
        text = text.replace(
            "The President may suspend the member during the inquiry.",
            "Pending the inquiry, the President may suspend a UPSC or Joint "
            "Commission member, while the Governor may suspend an SPSC member.",
        )
    if topic_number == 30:
        text = text.replace(
            "the cess continues to service pandemic-era loans — re-verify its current end-date.",
            "the official 56th-meeting material retained cess on specified "
            "tobacco-related goods until the related loan and interest liabilities "
            "are discharged; do not state one universal end-date.",
        )
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    for number in range(26, 31):
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
_original_validate_spec = deep._original_validate_spec


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 31)}:
        deep.deep.deep.deep.deep._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = deep.deep.deep.deep.deep.base.basic_mcq_area(repaired)
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
    rows = manifest["topics"][:30]
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
    expected = [f"polity-{number:02d}" for number in range(1, 31)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-30 changed or are out of order.")
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


_inherited_augment = deep.augment_topic_semantic_content


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

    modules = (deep, deep.deep, deep.deep.deep, deep.deep.deep.deep, deep.deep.deep.deep.deep)
    for module in modules:
        module.POLITY_REVIEW_POINTS = combined_points
        module.CANONICAL_OWNER_CONTROLS = combined_controls
        module.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
        module.CURRENT_AUTHORING_CONFIGS = combined_configs
        module.topics = topics
        module.enforce_strict_rotation = enforce_strict_rotation

    engine = deep.deep.deep.deep.deep
    engine.augment_topic_semantic_content = augment_topic_semantic_content
    engine.base.WORKFLOW = "polity-26-30-hostile-semantic-immutable-successor"
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
