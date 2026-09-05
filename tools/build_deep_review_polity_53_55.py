"""Build deep-reviewed immutable source Markdown and flow specs for Polity 53-55."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path

import generate_polity_52_55_sequential as batch


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "notes" / "Final-Learning-Packages" / "_deep-content-review"
CONTROL_DATE = "29 August 2026"
GENERATION_DATE = "2026-08-29"


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve())).replace("/", "\\")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_owner(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"^# .*\n+", "", text, count=1, flags=re.M)
    return re.sub(
        r"^(#{2,5}) ",
        lambda match: "#" + match.group(1) + " ",
        text,
        flags=re.M,
    ).strip()


def options(correct: str, distractors: list[str], key_index: int) -> list[str]:
    result = list(distractors)
    result.insert(key_index, correct)
    return result


def mcq_block(facts: list[dict[str, object]]) -> str:
    rows: list[str] = []
    number = 1
    for round_no in range(4):
        for fact in facts:
            key_index = (number - 1) % 4
            correct = str(fact["correct"])
            wrong = [str(item) for item in fact["wrong"]]
            if round_no == 0:
                stem = str(fact["stem"])
            elif round_no == 1:
                stem = "Which close-option distinction is constitutionally accurate concerning " + str(
                    fact["label"]
                ) + "?"
            elif round_no == 2:
                stem = "A State authority adopts the following proposition. Which correction is legally safest?"
                wrong = [
                    wrong[1],
                    wrong[2],
                    "The proposition is valid because all affirmative-action powers are interchangeable.",
                ]
            else:
                stem = "For a UPSC answer on " + str(fact["label"]) + ", which proposition should anchor the analysis?"
                wrong = [
                    wrong[2],
                    "The issue is controlled only by executive policy and not constitutional text.",
                    wrong[0],
                ]
            answer_options = options(correct, wrong[:3], key_index)
            rows.extend(
                [
                    f"#### MCQ {number}. {stem}",
                    "",
                    *[
                        f"- {letter}. {answer_options[index]}"
                        for index, letter in enumerate("ABCD")
                    ],
                    "",
                    f"**Answer: {'ABCD'[key_index]}**",
                    "",
                    f"**Explanation:** {fact['explanation']} The other options confuse the legal source, "
                    "institution, beneficiary-identification rule, benefit-conferral rule or current-status gate.",
                    "",
                ]
            )
            number += 1
    return "\n".join(rows)


P53_FACTS = [
    {
        "label": "Part XVI",
        "stem": "Which statement best describes the constitutional architecture of Part XVI?",
        "correct": "It separates legislative representation, service claims, constitutional safeguards and beneficiary-list identification.",
        "wrong": [
            "It is a self-contained code for every educational and employment quota.",
            "It transfers administration of all Scheduled Areas to the commissions under Articles 338-338B.",
            "It makes inclusion in a constitutional list an automatic entitlement to every welfare benefit.",
        ],
        "explanation": "Articles 330-334A, 335, 338-340 and 341-342A create legally different techniques.",
    },
    {
        "label": "SC/ST legislative reservation",
        "stem": "Which statement about Articles 330 and 332 is correct?",
        "correct": "They reserve seats for SCs/STs while the constituency continues to vote through the ordinary territorial electorate.",
        "wrong": [
            "They revive separate electorates for SCs/STs.",
            "They permit State executives to determine the SC/ST lists.",
            "They reserve seats in the Rajya Sabha and Legislative Councils.",
        ],
        "explanation": "Seat/candidacy reservation is not a communal or separate electorate.",
    },
    {
        "label": "Article 334",
        "stem": "Which statement correctly distinguishes the two clocks in Article 334?",
        "correct": "The 104th Amendment extended SC/ST legislative-seat reservation to eighty years but did not extend Anglo-Indian nomination beyond seventy years.",
        "wrong": [
            "Both SC/ST reservation and Anglo-Indian nomination were extended to 2030.",
            "The 104th Amendment deleted Articles 331 and 333 from the printed Constitution.",
            "Article 334 permanently entrenches every political reservation.",
        ],
        "explanation": "Textual presence and continued operation under a time clause are separate questions.",
    },
    {
        "label": "the 106th Amendment",
        "stem": "Which is the safest current-status statement on the 106th Amendment?",
        "correct": "Enactment and incorporation are distinct from a Gazette-appointed commencement date; after commencement, Article 334A still requires published census figures and delimitation before electoral operation.",
        "wrong": [
            "The reservation automatically applied to the eighteenth Lok Sabha.",
            "Publication of census figures alone activates the reservation without delimitation.",
            "It reserves one-third of Rajya Sabha and Legislative Council seats.",
        ],
        "explanation": "Section 1(2), Article 334A and electoral implementation must be analysed as separate gates.",
    },
    {
        "label": "Article 335",
        "stem": "Which proposition about Article 335 is correct?",
        "correct": "It requires SC/ST claims in services to be considered consistently with administrative efficiency and permits specified promotion-related relaxation by proviso.",
        "wrong": [
            "It defines administrative efficiency exhaustively.",
            "It creates the OBC and EWS reservation quotas.",
            "It fixes a uniform percentage for SC/ST appointments.",
        ],
        "explanation": "Article 335 is neither a universal quota clause nor a statutory definition of efficiency.",
    },
    {
        "label": "constitutional commissions",
        "stem": "Which institutional mapping is correct?",
        "correct": "Articles 338, 338A and 338B establish the NCSC, NCST and NCBC respectively.",
        "wrong": [
            "Article 340 permanently establishes all three commissions.",
            "Civil-court inquiry powers make commission reports binding decrees.",
            "The commissions can amend the constitutional lists by notification.",
        ],
        "explanation": "Constitutional status, inquiry powers, reporting and final policy authority must remain distinct.",
    },
    {
        "label": "Articles 339 and 340",
        "stem": "Which statement correctly distinguishes Articles 339 and 340?",
        "correct": "Article 339 concerns Scheduled Areas/ST welfare supervision, while Article 340 authorises a temporary commission to investigate backward-class conditions.",
        "wrong": [
            "Both provisions create permanent constitutional commissions.",
            "Article 339 authorises States to alter the ST list.",
            "Article 340 itself grants reservation without further law or policy.",
        ],
        "explanation": "Union supervision and an investigative commission perform different constitutional functions.",
    },
    {
        "label": "SC/ST list authority",
        "stem": "Which statement reflects Articles 341 and 342?",
        "correct": "The President initially specifies the State/UT-specific list, while Parliament alone may include or exclude communities by law.",
        "wrong": [
            "A State cabinet may alter the list by executive order.",
            "The lists are identical throughout India.",
            "The NCSC or NCST may finally add a community after inquiry.",
        ],
        "explanation": "The constitutional list is territorial and its alteration is reserved to Parliament.",
    },
    {
        "label": "the 102nd-105th Amendment sequence",
        "stem": "Which account of the SEBC-list architecture is correct?",
        "correct": "The 102nd Amendment constitutionalised the NCBC and Article 342A; the 105th expressly preserved a Central List and restored State/UT own-purpose list competence by law.",
        "wrong": [
            "The 105th abolished the Central List.",
            "The 102nd created the EWS quota.",
            "The 105th authorised States to alter SC/ST lists.",
        ],
        "explanation": "Central-purpose and State-purpose SEBC lists coexist after the 105th Amendment.",
    },
    {
        "label": "EWS reservation",
        "stem": "Which statement about EWS is constitutionally accurate?",
        "correct": "Its enabling provisions are Articles 15(6) and 16(6), inserted by the 103rd Amendment and upheld by a 3:2 majority in Janhit Abhiyan.",
        "wrong": [
            "EWS is a category within the Article 342A Central SEBC List.",
            "Article 335 is the source of EWS reservation.",
            "Janhit Abhiyan invalidated the exclusion of classes covered by existing reservation clauses.",
        ],
        "explanation": "EWS has a separate equality-clause source and is not a Part XVI identification list.",
    },
    {
        "label": "Davinder Singh",
        "stem": "What is the narrow constitutional holding relevant from State of Punjab v. Davinder Singh (2024)?",
        "correct": "A State may design evidence-based sub-classification within notified Scheduled Castes for fair distribution, without altering the Article 341 list or wholly excluding a listed caste.",
        "wrong": [
            "States may add and delete Scheduled Castes.",
            "Every State is constitutionally compelled to introduce sub-classification.",
            "The judgment converted separate-opinion creamy-layer observations into automatic nationwide list deletion.",
        ],
        "explanation": "Benefit distribution, list alteration and mandatory nationwide policy are separate propositions.",
    },
    {
        "label": "local bodies and Article 275",
        "stem": "Which cross-owner distinction is correct?",
        "correct": "Articles 243D/243T govern local-body reservation, while Article 275 supplies a fiscal grant route; neither alters a constitutional list.",
        "wrong": [
            "Article 334 governs Panchayat and municipal reservation.",
            "Article 275 authorises the President to amend the ST list.",
            "Part XVI exhaustively administers Fifth and Sixth Schedule areas.",
        ],
        "explanation": "Representation, fiscal support, list identification and area administration have separate sources.",
    },
]


P53_PYQS = r"""
### Verified PYQ 1 — UPSC Prelims 2023, GS Paper I, Question 40

**Exact question:** Consider the following statements:

**Statement-I:** The Supreme Court of India has held in some judgements that the reservation
policies made under Article 16(4) of the Constitution of India would be limited by Article 335 for
maintenance of efficiency of administration.

**Statement-II:** Article 335 of the Constitution of India defines the term 'efficiency of
administration'.

Which one of the following is correct in respect of the above statements?

- A. Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
- B. Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
- C. Statement-I is correct but Statement-II is incorrect
- D. Statement-I is incorrect but Statement-II is correct

**Official answer:** C.

**Demand decode and solution:** Statement-I reflects the judicial relationship between reservation
under Article 16(4) and the efficiency consideration in Article 335. Statement-II is false because
Article 335 does not define efficiency. The question tests the difference between a constitutional
standard and an exhaustive statutory definition.

### Verified PYQ 2 — UPSC Prelims 2024, GS Paper I, Question 81

**Exact question:** Consider the following statements regarding 'Nari Shakti Vandan Adhiniyam':

1. Provisions will come into effect from the 18th Lok Sabha.
2. This will be in force for 15 years after becoming an Act.
3. There are provisions for the reservation of seats for Scheduled Castes Women within the quota
   reserved for the Scheduled Castes.

Which of the statements given above are correct?

- A. 1, 2 and 3
- B. 1 and 2 only
- C. 2 and 3 only
- D. 1 and 3 only

**Official Set-A answer:** C.

**Demand decode and solution:** Statement 1 is incorrect because Article 334A ties electoral effect
to the post-commencement census-publication-delimitation chain, not merely to the number of a Lok
Sabha. Statements 2 and 3 state the enacted duration design and women-within-SC-seat design. The
current-status answer must additionally distinguish enactment, commencement and operation.

### Supporting cross-owned PYQ 3 — UPSC Mains 2018, GS Paper II, Question 2

**Exact question:** "Whether National Commission for Scheduled Castes (NCSC) can enforce the
implementation of constitutional reservation for the Scheduled Castes in the religious minority
institutions? Examine." **10 marks, 150 words.**

**Demand decode:** Separate the NCSC's Article 338 monitoring/inquiry/reporting role from the legal
source and limits of admission reservation, especially Article 15(5)'s Article 30(1) exclusion.

**Model answer:** Article 338 authorises the NCSC to investigate safeguards, inquire into complaints,
advise on planning and report to the President. Its civil-court powers assist investigation; they
do not convert recommendations into binding judicial decrees. Educational reservation must rest on
the equality provisions and valid law. Article 15(5) expressly excludes minority educational
institutions protected by Article 30(1). Therefore, the NCSC can investigate discrimination,
recommend corrective action and place non-acceptance before democratic institutions, but it cannot
by itself compel a religious minority institution to implement a reservation that the governing
constitutional provision excludes. Judicial remedies remain available for violations falling
within enforceable law. The correct conclusion is institutional: a commission strengthens
accountability, but cannot enlarge its jurisdiction beyond the Constitution.

**Why this earns marks:** It answers "can enforce", identifies Articles 338, 15(5) and 30(1), and
distinguishes inquiry from adjudication. **How to improve:** Add one line on action-taken memoranda
and avoid a generic discussion of all NCSC functions. **Compression:** 20-word introduction,
90-word legal analysis and 25-word qualified conclusion.

### Supporting cross-owned PYQ 4 — UPSC Mains 2022, GS Paper II, Question 5

**Exact question:** "Discuss the role of the National Commission for Backward Classes in the wake
of its transformation from a statutory body to a constitutional body." **10 marks, 150 words.**

**Model answer:** The 102nd Amendment inserted Article 338B and transformed the NCBC from a statutory
body under the 1993 Act into a constitutional commission. This strengthened permanence,
independence of mandate, complaint inquiry, safeguard monitoring, planning advice and reporting to
the President and Parliament. Civil-court powers improve fact-finding, while consultation duties
can expose the distributional impact of policy. Yet constitutional status does not make its advice
binding, confer list-amending power, or merge it with an Article 340 commission. The 2021 Maratha
reservation decision interpreted the pre-105th text; the 105th Amendment then expressly restored
State/UT competence to maintain own-purpose SEBC lists while retaining the Central List. Thus, the
NCBC's transformation deepened constitutional accountability, but effective inclusion still
depends on reliable data, reasoned government response and judicially reviewable law.

**Why this earns marks:** It links institutional transformation to powers, federal list authority
and limits. **How to improve:** Name Articles 338B and 342A in the first two sentences and do not
claim the Commission itself legislates list entries. **Compression:** 25-word introduction,
95-word role-and-limit body and 25-word conclusion.
"""


P53_MAINS = [
    (
        "Explain why Part XVI cannot be described as a single reservation code.",
        "Explain",
        10,
        "Part XVI uses four techniques: Articles 330-334A provide political representation; Article 335 integrates SC/ST service claims with administrative efficiency; Articles 338-340 create monitoring, supervision and investigation; and Articles 341-342A identify protected classes. These provisions do not themselves supply every benefit. Educational and service reservations primarily use Articles 15 and 16; local-body seats use Articles 243D and 243T; Scheduled Area administration uses the Fifth and Sixth Schedules; and welfare grants may use Article 275. Therefore a list answers who is constitutionally recognised, while another provision or law answers what benefit follows. This distinction prevents the common error of treating commission advice, list status, quota authority and area governance as interchangeable. Part XVI is best understood as an architecture of substantive equality whose components have different decision-makers, procedures and legal effects.",
    ),
    (
        "Analyse the constitutional safeguards governing SC/ST legislative representation.",
        "Analyse",
        15,
        "Articles 330 and 332 reserve Lok Sabha and Assembly seats broadly by population while retaining ordinary territorial voting, so reservation does not recreate separate electorates. Article 334 time-frames the arrangement: the 104th Amendment extended SC/ST seats to eighty years from commencement, presently reaching 25 January 2030, while Anglo-Indian nomination was not similarly extended. Delimitation law translates population and constitutional rules into constituency boundaries. The 106th Amendment adds women-within-SC/ST seat design, but enactment, commencement, census publication, delimitation and electoral operation remain separate gates under section 1(2) and Article 334A. Political reservation improves descriptive representation but cannot alone guarantee substantive voice, party autonomy or constituency accountability. A sound reform assessment therefore combines constitutional continuity, evidence of exclusion, fair delimitation and periodic democratic review.",
    ),
    (
        "Distinguish identification of Scheduled Castes from sub-classification for distribution of benefits.",
        "Distinguish",
        15,
        "Article 341 establishes a State/UT-specific identification process: the President initially specifies Scheduled Castes and Parliament alone may include or exclude communities by law. Sub-classification asks a different question—how an otherwise valid benefit should be distributed within the notified class. In State of Punjab v. Davinder Singh (2024), the Supreme Court overruled E.V. Chinnaiah on this point and permitted evidence-based sub-classification to advance substantive equality. The State still cannot alter the Article 341 list, use political labels without data, or wholly exclude a listed caste from the benefit. Nor did the judgment constitutionally compel every State to adopt one uniform model. Identification protects list integrity; sub-classification addresses unequal benefit capture. The constitutional balance is therefore parliamentary control over membership plus judicially reviewable State design over distribution.",
    ),
    (
        "Critically examine Article 335 as a bridge between representation and administrative efficiency.",
        "Critically examine",
        15,
        "Article 335 requires SC/ST claims in Union and State services to be considered consistently with administrative efficiency. It neither fixes a quota nor defines efficiency. The 82nd Amendment proviso permits relaxation of qualifying marks or evaluation standards for promotion reservation. Read with Articles 16(4A) and 16(4B), M. Nagaraj and Jarnail Singh, the provision requires a constitutionally disciplined balance rather than a presumption that equality and efficiency are opposites. Inclusive administration can improve legitimacy and institutional knowledge, but reservation design must remain evidence-based and attentive to cadre, representation and service requirements. Conversely, an undefined appeal to efficiency cannot become a device for preserving historical exclusion. The strongest interpretation treats Article 335 as an integration clause: substantive representation is pursued within a reasoned, reviewable account of administrative performance.",
    ),
    (
        "Discuss the federal consequences of the 102nd and 105th Amendments.",
        "Discuss",
        15,
        "The 102nd Amendment constitutionalised the NCBC through Article 338B, inserted Article 342A and defined socially and educationally backward classes in Article 366(26C). In Jaishri Laxmanrao Patil, the Supreme Court interpreted the pre-105th text as centralising identification for the constitutional list. The 105th Amendment responded by expressly distinguishing the Central List for Central purposes from State/UT lists prepared by law for their own purposes. The result is cooperative but differentiated federalism: national institutions retain a Central-purpose architecture while States can respond to local disadvantage. Limits remain. State SEBC-list competence does not extend to Articles 341 and 342 SC/ST lists, and list inclusion does not itself validate any quota percentage. Transparent criteria, current data and judicial review remain necessary to prevent political over-inclusion and arbitrary exclusion.",
    ),
    (
        "Evaluate the constitutional commissions for SCs, STs and backward classes as accountability institutions.",
        "Evaluate",
        20,
        "Articles 338, 338A and 338B give the NCSC, NCST and NCBC constitutional permanence, complaint inquiry, safeguard monitoring, planning advice, reporting duties and specified civil-court powers. Reports routed through the President, Parliament, Governors and State legislatures make governmental response visible. Their specialised mandates can identify systemic exclusion that ordinary administration overlooks. Yet they are not courts: recommendations generally remain advisory, civil-court powers relate to inquiry, and list alteration follows separate constitutional procedures. Effectiveness also depends on appointments, research capacity, data access, follow-up and reasoned action-taken memoranda. Article 339 Union supervision and Article 340 temporary commissions perform neighbouring but distinct functions. Reform should strengthen timely appointments, public dashboards, compliance tracking and institutional consultation without falsely converting expert advice into binding adjudication. These bodies are best judged as constitutional accountability multipliers rather than substitute governments.",
    ),
    (
        "Assess EWS reservation within the wider constitutional design of substantive equality.",
        "Assess",
        20,
        "The 103rd Amendment inserted Articles 15(6) and 16(6), enabling additional reservation up to ten per cent for economically weaker sections outside the classes covered by specified existing reservation clauses. Janhit Abhiyan upheld the amendment by 3:2, including economic criteria, exclusion of already covered classes and the additional design. The measure broadens affirmative action beyond traditional social-backwardness categories, but it does not convert EWS into an Article 342A list or derive from Article 335. Its legitimacy rests on constitutional text, valid identification criteria and non-arbitrary implementation. Critics stress the relationship between economic disadvantage, structural discrimination and the ordinary Indra Sawhney ceiling; the majority nevertheless found no basic-structure violation. A balanced assessment recognises EWS as a distinct equality route while insisting that income/asset criteria, access outcomes and institutional exclusions be periodically evaluated.",
    ),
    (
        "Design a constitutional decision tree for any reservation-related problem.",
        "Design",
        10,
        "First identify the field: Parliament/Assembly seats use Articles 330-334A; local bodies use Articles 243D/243T; education and services use Articles 15-16 plus law; service efficiency adds Article 335. Second identify the class: SC/ST lists use Articles 341-342; Central and State SEBC lists use Article 342A after the 105th Amendment; EWS uses Articles 15(6)/16(6). Third identify the competent actor—President, Parliament, State legislature, commission, delimitation authority or appointing authority. Fourth distinguish identification, benefit design, monitoring and adjudication. Fifth add the controlling amendment/case and current-status date. This sequence prevents category errors and produces an answer that moves from source to power, procedure, limit and remedy.",
    ),
]


P53_PANELS = [
    ("Part XVI: four distinct constitutional techniques", "ROOT: inclusion is pursued through different legal effects.\n\nREPRESENTATION -> Arts 330-334A.\nSERVICES -> Art 335 with Arts 15-16 cross-route.\nSAFEGUARDS -> Arts 338-340.\nIDENTIFICATION -> Arts 341-342A.\n\nFIREWALL: list != quota != commission report != welfare scheme."),
    ("SC/ST legislative seats and territorial electorate", "ART 330 -> Lok Sabha SC/ST seats.\nART 332 -> Assembly SC/ST seats plus specified North-East rules.\nSEAT/CANDIDACY RESERVED -> all constituency electors vote ordinarily.\n\nLIMIT: no Rajya Sabha or Legislative Council reservation under these Articles.\nTRAP: political reservation != separate electorate."),
    ("Article 334 clocks and Anglo-Indian transition", "104TH AMENDMENT\nSC/ST seat reservation -> eighty years from commencement -> 25 January 2030.\nAnglo-Indian nomination -> seventy-year clock not extended -> ceased in 2020.\n\nARTS 336-337 -> ten-year transitional protections exhausted.\nTRAP: cessation through time clause != automatic textual deletion."),
    ("106th Amendment: five-gate status chain", "ENACTMENT / INCORPORATION\n        -> Gazette-appointed COMMENCEMENT under section 1(2)\n        -> first post-commencement census\n        -> relevant figures published\n        -> delimitation for this purpose\n        -> electoral operation under Art 334A.\n\nSCOPE: Lok Sabha, State Assemblies and Delhi Assembly; not Rajya Sabha/Councils."),
    ("Delimitation and women-within-SC/ST seats", "ARTS 330A / 332A -> one-third design, including one-third within SC/ST reserved seats.\nART 334A -> fifteen-year duration from operational commencement; later continuation by law.\nROTATION -> after subsequent delimitation as Parliament provides.\n\nTRAP: census publication alone does not draw constituencies."),
    ("Article 335 and the equality-service bridge", "SC/ST CLAIMS IN SERVICES\n        + maintenance of administrative efficiency.\n82ND AMENDMENT PROVISO -> qualifying-mark/evaluation relaxation for promotion reservation.\nM. Nagaraj (2006) + Jarnail Singh (2018) -> controlling promotion doctrine.\n\nTRAP: no fixed quota and no definition of efficiency."),
    ("NCSC, NCST, NCBC and neighbouring powers", "ART 338 -> NCSC | 338A -> NCST | 338B -> NCBC.\nINQUIRY + REPORT + ADVICE + CIVIL-COURT POWERS -> accountability, not binding decree.\nART 339 -> Scheduled Areas/ST welfare supervision.\nART 340 -> temporary backward-class investigation commission.\nART 275 -> separate welfare-grant route."),
    ("SC/ST list authority under Articles 341-342", "PRESIDENT -> initial State/UT-specific specification after required consultation.\nPARLIAMENT BY LAW -> inclusion/exclusion.\nSTATE -> cannot alter list by executive or legislation.\n\nTERRITORIALITY: status is not automatically pan-India.\nTRAP: commission recommendation does not amend the list."),
    ("SEBC federalism: 102nd to 105th Amendments", "102ND -> Arts 338B + 342A + Art 366(26C).\nJaishri Laxmanrao Patil (2021) -> pre-105th interpretation.\n105TH -> Central List for Central purposes + State/UT own-purpose list by law.\n\nLIMIT: State SEBC power does not alter SC/ST lists."),
    ("EWS as a separate equality route", "103RD AMENDMENT -> Arts 15(6) and 16(6).\nADDITIONAL RESERVATION -> up to 10% in each clause's field.\nJANHIT ABHIYAN (2022) -> upheld 3:2.\n\nFIREWALL: EWS != Article 342A SEBC list != Article 335 SC/ST service claim."),
    ("Davinder Singh (2024): distribution, not list alteration", "E.V. Chinnaiah v. State of Andhra Pradesh (2004) -> earlier indivisibility rule.\nDavinder Singh (2024) -> overruled it on sub-classification.\nSTATE MAY -> use evidence for fair distribution within notified SC class.\nSTATE MAY NOT -> alter Art 341 list or wholly exclude a listed caste.\n\nNo automatic nationwide mandate."),
    ("UPSC decision tree and qualified verdict", "1 FIELD -> legislature/local body/education/service.\n2 CLASS -> SC/ST/SEBC/EWS.\n3 AUTHORITY -> President/Parliament/State/commission/delimitation body.\n4 EFFECT -> identify/benefit/monitor/adjudicate.\n5 STATUS -> amendment, case, notification and date.\n\nVERDICT: substantive equality requires exact-source discipline."),
]


P54_FACTS = [
    {"label": "Article 39A", "stem": "What is the constitutional anchor for equal access and free legal aid?", "correct": "Article 39A directs the State to promote justice on equal opportunity and prevent economic or other disability from denying access.", "wrong": ["Article 32 creates every legal-services authority.", "Article 136 guarantees free counsel in every dispute.", "Article 50 establishes Lok Adalats."], "explanation": "Article 39A is a Directive Principle operationalised through statutes and Article 21 jurisprudence."},
    {"label": "the legal-services ladder", "stem": "Which institutional description is accurate?", "correct": "NALSA, the Supreme Court Committee, SLSAs, High Court Committees, DLSAs and TLSCs perform level-specific legal-services functions.", "wrong": ["SALSA is the statutory name of every State authority.", "DLSAs are constitutional courts.", "TLSCs may overrule High Court decisions."], "explanation": "The 1987 Act creates a coordinated statutory ladder; SLSA is the ordinary abbreviation."},
    {"label": "Section 12 eligibility", "stem": "Which statement about free legal-services eligibility is correct?", "correct": "Eligibility includes several status-based vulnerable categories as well as prescribed income criteria, subject also to a prima facie case assessment.", "wrong": ["Only persons below an income ceiling qualify.", "Every senior citizen qualifies solely by age under Section 12.", "OBC status by itself is expressly listed in Section 12."], "explanation": "SC/ST members, women/children, persons in custody and other listed groups do not depend solely on income."},
    {"label": "ordinary Lok Adalat jurisdiction", "stem": "Which matter may an ordinary Lok Adalat handle?", "correct": "A pending case or pre-litigation dispute within a court's jurisdiction, excluding a non-compoundable offence.", "wrong": ["Only disputes already decided by a High Court.", "Every criminal offence regardless of compoundability.", "A matter outside all ordinary court jurisdiction."], "explanation": "Sections 19-20 combine pending and pre-litigation settlement jurisdiction with a criminal-law exclusion."},
    {"label": "ordinary Lok Adalat power", "stem": "What may an ordinary Lok Adalat do when settlement fails?", "correct": "It must not decide the merits; a referred pending case returns to court and parties retain the ordinary remedy.", "wrong": ["It must impose an equitable merits award.", "It converts automatically into a Permanent Lok Adalat.", "It may compel one party to accept the proposed terms."], "explanation": "State of Punjab v. Jalour Singh (2008) confirms the compromise-only character."},
    {"label": "ordinary Lok Adalat awards", "stem": "Which statement about an agreed Lok Adalat award is correct?", "correct": "It is deemed a civil-court decree, final and binding, and no statutory appeal lies; limited constitutional challenge remains for jurisdictional or consent defects.", "wrong": ["Any dissatisfied party may appeal on facts.", "The award is only a non-binding recommendation.", "Finality validates an award imposed without settlement."], "explanation": "Consent supports statutory finality but does not eliminate constitutional review for illegality."},
    {"label": "Permanent Lok Adalat jurisdiction", "stem": "Which feature defines a Permanent Lok Adalat?", "correct": "It is a standing pre-litigation forum for notified public utility services under Chapter VI-A.", "wrong": ["It hears every pending civil suit transferred by a court.", "It is merely a continuously sitting ordinary Lok Adalat.", "It may try non-compoundable offences."], "explanation": "Sector, stage and statutory exclusions define PLA competence."},
    {"label": "Permanent Lok Adalat merits power", "stem": "When may a PLA decide an eligible dispute on merits?", "correct": "After conducting the statutory conciliation process and failing to secure settlement, subject to jurisdictional limits.", "wrong": ["Before attempting conciliation.", "Only with a fresh arbitral agreement.", "Never; all Lok Adalats are compromise-only."], "explanation": "Bar Council of India (2012) and Canara Bank v. G.S. Jayarama (2022) support the conciliation-cum-adjudication design."},
    {"label": "Gram Nyayalayas", "stem": "Which statement about a Gram Nyayalaya is correct?", "correct": "It is a statutory mobile-capable court of first instance with scheduled civil/criminal jurisdiction and appellate routes.", "wrong": ["It is a village panchayat exercising customary power.", "Its awards are unappealable compromises.", "It is constitutionally mandatory in every Panchayat."], "explanation": "The 2008 Act creates a judicial forum; establishment and operation remain State-dependent."},
    {"label": "Family Courts", "stem": "Which feature distinguishes a Family Court?", "correct": "It combines specialised statutory adjudication with a duty to explore settlement, privacy tools and a defined High Court appeal.", "wrong": ["It can only record compromises.", "It is an arbitral tribunal chosen by contract.", "Lawyers have an unconditional right of appearance as of course."], "explanation": "Conciliation orientation does not remove adjudicatory power or fairness duties."},
    {"label": "fast-track and special courts", "stem": "Which classification is accurate?", "correct": "Fast-track courts are capacity/administrative schemes, while special courts obtain jurisdiction from a parent statute or valid notification.", "wrong": ["Both are new constitutional tiers.", "Every special court is a tribunal outside the judiciary.", "An evening court has nationwide statutory jurisdiction."], "explanation": "Labels do not answer source, appointment, procedure or appeal."},
    {"label": "mediation, arbitration and Lok Adalat", "stem": "Which comparison is legally correct?", "correct": "Mediation produces a party-made settlement, arbitration produces an adjudicatory award, ordinary Lok Adalat records compromise, and a PLA has limited post-conciliation merits power.", "wrong": ["All four can decide non-compoundable criminal offences.", "All four require an identical prior contract.", "Every outcome has the same appeal and enforcement route."], "explanation": "Consent, jurisdiction, decision-maker and legal effect differ across dispute-resolution designs."},
]


P54_PYQS = r"""
### Verified PYQ 1 — UPSC Prelims 2020, GS Paper I, Question 9

**Exact question:** In India, Legal Services Authorities provide free legal services to which of
the following type of citizens?

1. Person with an annual income of less than Rs. 1,00,000
2. Transgender with an annual income of less than Rs. 2,00,000
3. Member of Other Backward Classes (OBC) with an annual income of less than Rs. 3,00,000
4. All Senior Citizens

- A. 1 and 2 only
- B. 3 and 4 only
- C. 2 and 3 only
- D. 1 and 4 only

**Verified answer:** A, reconciled with the applicable legal-services eligibility framework; no
official UPSC key is claimed from the repository.

### Verified PYQ 2 — UPSC Mains 2023, GS Paper II, Question 2

**Exact question:** "Who are entitled to receive free legal aid? Assess the role of the National
Legal Services Authority (NALSA) in rendering free legal aid in India." **10 marks, 150 words.**

**Model answer:** Article 39A directs equal access to justice and the Legal Services Authorities Act
1987 converts that objective into institutions and entitlements. Section 12 covers SC/ST members,
women and children, trafficking/begar victims, persons with disability, disaster or violence
victims, industrial workmen, persons in custody and persons below the prescribed income limit,
subject to a prima facie case. NALSA lays down policy, frames economical schemes, coordinates State
Authorities, supports Lok Adalats and legal-awareness programmes, and monitors delivery through the
statutory ladder. Its strength is national coordination; its limits are uneven awareness, counsel
quality, vacancies, distance and digital exclusion. NALSA should therefore be assessed not only by
beneficiary counts but by timely advice, representation quality and durable case outcomes.

**Why this earns marks:** It answers both entitlement and institutional role. **How to improve:**
Name Section 12 and distinguish NALSA from SLSA/DLSA implementation. **Compression:** 30 words on
law, 85 on role and 30 on limits/verdict.

### Verified PYQ 3 — UPSC Mains 2024, GS Paper II, Question 2

**Exact printed wording:** "Explain and distinguish between Lok Adalats and Arbitration Tribunals,
Whether they intertain civil as well as criminal cases?" **10 marks, 150 words.**

**Model answer:** Lok Adalats are statutory settlement forums under the Legal Services Authorities
Act. An ordinary Lok Adalat may consider pending or pre-litigation civil disputes and compoundable
criminal matters, but cannot adjudicate merits when compromise fails. Its agreed award is deemed a
civil-court decree, final and non-appealable. An arbitral tribunal derives jurisdiction from an
arbitration agreement and the Arbitration and Conciliation Act; it adjudicates arbitrable civil or
commercial disputes and issues a reasoned award subject to the statutory setting-aside and appeal
framework. Criminal liability is generally non-arbitrable, whereas a Lok Adalat can settle a
compoundable criminal case. A Permanent Lok Adalat is a separate public-utility pre-litigation
hybrid and should not be used to describe every Lok Adalat.

**Why this earns marks:** It distinguishes source, consent, jurisdiction, merits power and review.
**How to improve:** Preserve the paper's printed spellings only in the quotation, then use correct
legal terminology. **Compression:** two 50-word forum capsules and a 30-word criminal-case verdict.
"""


P54_MAINS = [
    ("Explain the constitutional and statutory architecture of free legal services in India.", "Explain", 10, "Article 39A supplies the equal-access objective, while Article 21 jurisprudence treats effective legal assistance and speedy justice as elements of fair procedure. The Legal Services Authorities Act 1987 creates NALSA, the Supreme Court Legal Services Committee, SLSAs, High Court Committees, DLSAs and TLSCs. Section 12 combines status-based vulnerability with income eligibility and a prima facie case screen. NALSA frames policy and schemes; State and district institutions translate them into representation, advice, awareness and Lok Adalat access. The architecture is therefore vertically coordinated but delivery-dependent. Its constitutional success must be measured by early advice, competent counsel, language/disability access and actual outcomes rather than formal eligibility alone."),
    ("Distinguish ordinary Lok Adalats from Permanent Lok Adalats.", "Distinguish", 15, "An ordinary Lok Adalat under Chapter VI handles pending or pre-litigation disputes within court jurisdiction, excluding non-compoundable offences. It conciliates only; State of Punjab v. Jalour Singh (2008) confirms that it cannot decide merits after failure. A PLA under Chapter VI-A is a standing pre-litigation forum limited to public utility services. It must first conciliate, but may adjudicate an eligible dispute after conciliation fails, as sustained in Bar Council of India v. Union of India (2012). Both awards are final, binding and deemed civil-court decrees, yet their jurisdictional basis differs. The core distinction is not permanence alone but sector, stage and post-failure decisional power."),
    ("Critically assess finality and consent in Lok Adalat awards.", "Critically assess", 15, "Statutory finality makes an agreed Lok Adalat award enforceable as a civil-court decree and prevents routine appeals, reducing delay and preserving settlements. Its legitimacy, however, derives from genuine compromise. An ordinary Lok Adalat cannot use docket pressure, unequal bargaining or an adjudicatory opinion to manufacture consent. Where compromise fails, a pending case returns to court. A writ challenge may remain on narrow grounds such as fraud, absence of consent, jurisdictional error or denial of natural justice. PLA awards involve a different statutory design because eligible disputes may be decided after failed conciliation. Finality should therefore be defended as settlement enforcement, not as insulation of coercion or illegality."),
    ("Evaluate Permanent Lok Adalats as public-utility justice institutions.", "Evaluate", 20, "Permanent Lok Adalats address recurring pre-litigation disputes in notified public utility services such as transport, power, water, sanitation, hospitals and insurance. Their sequence—application, conciliation, proposed settlement and, on failure, limited merits adjudication—offers an enforceable remedy without requiring ordinary litigation. Canara Bank v. G.S. Jayarama (2022) stresses fidelity to the conciliation procedure. Benefits include low cost, sector focus and early resolution; risks include jurisdictional overreach, weak legal assistance and confusing PLA adjudication with ordinary Lok Adalat compromise. Pecuniary limits and notified services are date-sensitive and must be verified. PLAs are valuable when competence, procedural fairness, reasoned decision and constitutional review operate together."),
    ("Discuss the design and implementation challenges of Gram Nyayalayas.", "Discuss", 15, "The Gram Nyayalayas Act 2008 envisages rural first-instance courts at intermediate-Panchayat or grouped-Panchayat level, a Nyayadhikari qualified as a Judicial Magistrate First Class, mobile sittings, scheduled civil/criminal jurisdiction, conciliation and appeals to District or Sessions Courts. This design reduces distance and procedural cost while preserving judicial character. Yet establishment is State-dependent and proximity without judges, staff, awareness, transport, language support and coordination with police/legal aid cannot deliver access. Gram Nyayalayas must not be confused with Panchayats or Lok Adalats. Reform requires rational jurisdiction mapping, regular mobile calendars, DLSA integration and transparent dated performance data."),
    ("Compare Family Courts, fast-track courts, special courts and commercial courts.", "Compare", 15, "Family Courts derive from the 1984 Act and combine specialised adjudication with settlement, privacy and flexible evidentiary reception. Fast-track courts are additional-capacity schemes implemented through States and High Courts rather than a distinct constitutional tier. Special courts obtain subject or offence jurisdiction from a parent statute/notification. Commercial Courts are statutory civil courts using specified-value jurisdiction, case management and pre-institution mediation rules. Therefore the labels cannot be interchanged: source determines judges, jurisdiction, procedure, appeal and permanence. Specialisation can improve expertise and speed, but only adequate staffing and fair process prevent a faster forum from becoming a weaker one."),
    ("Analyse power asymmetry and digital exclusion in settlement-oriented justice.", "Analyse", 20, "Settlement systems lower cost and preserve relationships, but apparent consent may conceal unequal bargaining between insurer and victim, employer and worker, institution and consumer, or digitally connected and excluded parties. Fair design requires independent legal advice, understandable terms, interpreter and disability support, private communication, time to reflect and a clear record of consent. E-Lok Adalats and online mediation reduce travel but need identity assurance, secure documents, language access and an offline alternative. Disposal volume cannot be the sole metric. Durable compliance, informed consent and equitable outcomes better express Article 39A."),
    ("Design a forum-selection test for an access-to-justice problem.", "Design", 10, "Ask five questions. First, is coercive interim relief or authoritative precedent required? If yes, use a competent court. Second, is settlement voluntary and relationship-preserving? Consider mediation or ordinary Lok Adalat. Third, is it a pre-litigation public-utility dispute within PLA limits? Use the PLA sequence. Fourth, is local first-instance civil/criminal jurisdiction under the Gram Nyayalayas Act available? Fifth, is specialist statutory jurisdiction—family, commercial or offence-specific—triggered? Then verify appeal, legal aid, limitation, current notification and digital/offline access. Forum follows legal competence and fairness, not disposal targets."),
]


P54_PANELS = [
    ("Article 39A and the access-to-justice chain", "ART 39A -> equal-opportunity justice + free legal aid.\nHussainara Khatoon (1979) -> Art 21 fair procedure, legal assistance and speedy justice.\n1987 ACT -> institutions + eligibility + Lok Adalats.\n\nVERDICT: Directive Principle becomes operational through law and remedies."),
    ("Legal-services authority ladder", "NALSA -> national policy and schemes.\nSUPREME COURT COMMITTEE -> Supreme Court matters.\nSLSA + HIGH COURT COMMITTEE -> State/High Court delivery.\nDLSA + TLSC -> district/taluk implementation.\n\nTRAP: statutory SLSA, not SALSA; bodies are not constitutional courts."),
    ("Section 12 eligibility and quality gate", "STATUS ROUTES -> SC/ST, women/children, disability, custody, workmen and listed vulnerability.\nINCOME ROUTE -> prescribed ceiling.\nSECTION 13 -> prima facie case.\n\nQUALITY TEST: early advice + competent representation + accessible delivery."),
    ("Ordinary Lok Adalat jurisdiction", "PENDING CASE or PRE-LITIGATION DISPUTE within court jurisdiction.\nEXCLUDED -> non-compoundable offence.\nPROCESS -> referral/application -> conciliation -> compromise.\n\nState of Punjab v. Jalour Singh (2008): no merits adjudication."),
    ("Ordinary award, failure and review", "SETTLEMENT -> award deemed civil-court decree -> final/binding -> no statutory appeal.\nNO SETTLEMENT -> pending case returns / ordinary remedy continues.\nWRIT CONTROL -> fraud, no genuine consent, jurisdiction or natural-justice defect.\n\nFINALITY != power to compel compromise."),
    ("Permanent Lok Adalat jurisdiction", "CHAPTER VI-A -> standing body for PUBLIC UTILITY SERVICES.\nSTAGE -> pre-litigation only.\nBAR -> non-compoundable offence + notified pecuniary boundary.\n\nInterGlobe Aviation v. N. Satchidanand (2011): ordinary and Permanent Lok Adalats differ."),
    ("PLA conciliation-to-adjudication sequence", "APPLICATION -> conciliation papers -> settlement terms -> agreement award.\nIF FAILURE -> eligible merits decision.\nBar Council of India v. Union of India (2012) -> design upheld.\nCanara Bank v. G.S. Jayarama (2022) -> follow statutory conciliation sequence."),
    ("Gram Nyayalaya as a statutory court", "2008 ACT -> State establishment after High Court consultation.\nNYAYADHIKARI -> JMFC qualification.\nMOBILE FIRST INSTANCE -> scheduled civil/criminal cases + conciliation.\nAPPEAL -> District Court / Sessions Court.\n\nTRAP: not Panchayat, khap or Lok Adalat."),
    ("Family and specialist-court distinctions", "FAMILY COURT -> adjudication + conciliation + privacy + High Court appeal.\nFAST TRACK -> capacity scheme.\nSPECIAL COURT -> parent-statute jurisdiction.\nCOMMERCIAL COURT -> statutory civil court and case management.\nEVENING COURT -> administrative sitting format."),
    ("Mediation, arbitration and court firewall", "Afcons Infrastructure v. Cherian Varkey Construction (2010) -> structured ADR referral.\nMEDIATION -> party-made settlement.\nARBITRATION -> private adjudication and statutory award challenge.\nORDINARY LOK ADALAT -> compromise award.\nPLA -> limited post-conciliation adjudication."),
    ("Fairness, data and digital access", "Patil Automation v. Rakheja Engineers (2022)\n-> mandatory commercial pre-institution mediation absent an urgent-relief exception.\nCONSENT QUALITY -> advice + no coercion + understood terms.\nDIGITAL -> identity, privacy, language, disability and offline option.\nCURRENT DATA -> date every count, ceiling and notified service."),
    ("UPSC forum-selection answer spine", "1 LEGAL SOURCE.\n2 SUBJECT / STAGE / COMPOUNDABILITY.\n3 CONSENT OR MERITS POWER.\n4 AWARD / APPEAL / REVIEW.\n5 ACCESS AND POWER-ASYMMETRY SAFEGUARDS.\n\nVERDICT: affordable justice must remain competent and voluntary where required.\nIllegality remains reviewable."),
]


P55_FACTS = [
    {"label": "doctrine selection", "stem": "What is the correct first step before invoking a constitutional doctrine?", "correct": "Identify the governing Article, legal trigger, competent institution and requested legal effect.", "wrong": ["Choose the most famous case regardless of the issue.", "Treat every doctrine as an independent constitutional provision.", "Begin with the desired policy result."], "explanation": "Doctrine follows text, trigger and remedy; it does not replace them."},
    {"label": "severability", "stem": "When may a court sever an unconstitutional part?", "correct": "When the valid remainder is textually separable, workable and consistent with legislative intent.", "wrong": ["Whenever deletion produces a preferred policy.", "Only for pre-Constitution laws.", "Even when the remainder becomes a new scheme."], "explanation": "R.M.D. Chamarbaugwala v. Union of India (1957) requires separability and viability."},
    {"label": "eclipse and waiver", "stem": "Which statement correctly distinguishes eclipse and waiver?", "correct": "Eclipse classically suspends inconsistent pre-Constitution law to the extent of conflict; non-waiver prevents consent from validating unconstitutional State action.", "wrong": ["Both doctrines repeal the law.", "Waiver applies identically to every private procedural right.", "Eclipse automatically validates every post-Constitution void law."], "explanation": "Bhikaji Narain Dhakras (1955) and Basheshar Nath (1958) address different objects and effects."},
    {"label": "pith and substance", "stem": "What does pith and substance test?", "correct": "The law's true nature and character, allowing genuine incidental overlap when the dominant field is competent.", "wrong": ["The political motive of individual legislators.", "Only literal wording of the title.", "Repugnancy in every Union-State overlap."], "explanation": "Purpose, scope and effects locate the dominant legislative field."},
    {"label": "colourable legislation", "stem": "Which statement on colourable legislation is correct?", "correct": "It exposes a disguised lack of legislative competence; bad motive alone is insufficient.", "wrong": ["It invalidates any unpopular law.", "It is identical to manifest arbitrariness.", "It applies only after Presidential assent under Article 254(2)."], "explanation": "K.C. Gajapati Narayan Deo (1953) is a competence doctrine, not a motive inquiry."},
    {"label": "territorial nexus", "stem": "When can a State law have effects beyond the State?", "correct": "When a real and sufficient territorial connection links the State, subject and imposed liability or operation.", "wrong": ["Whenever the State declares a national interest.", "Only after Parliament delegates Article 245(2).", "A remote or illusory connection is enough."], "explanation": "State of Bombay v. R.M.D. Chamarbaugwala (1957) requires a relevant nexus."},
    {"label": "repugnancy and occupied field", "stem": "Which sequence correctly applies Article 254?", "correct": "Find the same Concurrent field, compare schemes and actual conflict, then apply Union priority subject to the Article 254(2) assent route and later parliamentary override.", "wrong": ["Apply Article 254 to every List I-List II overlap.", "Treat any Union law as automatically occupying every related field.", "Use Presidential assent to cure lack of State competence."], "explanation": "Deep Chand (1959) and M. Karunanidhi (1979) demand field and conflict analysis."},
    {"label": "harmonious construction", "stem": "What is the operative aim of harmonious construction?", "correct": "Give meaningful operation to apparently conflicting provisions before invoking an express constitutional priority.", "wrong": ["Erase the less preferred provision.", "Override clear text with abstract purpose.", "Automatically make Union law supreme."], "explanation": "In re Kerala Education Bill (1958) illustrates reconciliation within constitutional structure."},
    {"label": "prospective overruling", "stem": "Which proposition on prospective overruling is correct?", "correct": "A court must expressly shape the temporal effect of a new rule to preserve identified past transactions or effects.", "wrong": ["Every overruled case automatically survives prospectively.", "It changes constitutional text.", "It applies only to legislation and never precedent."], "explanation": "I.C. Golaknath (1967) introduced the technique in Indian constitutional adjudication."},
    {"label": "basic structure", "stem": "What does the basic-structure doctrine review?", "correct": "Whether an Article 368 amendment damages constitutional identity or an essential feature, despite formal procedural validity.", "wrong": ["Whether every ordinary statute is desirable.", "A closed textual list printed in the Constitution.", "Whether courts may amend the Constitution by judgment."], "explanation": "Kesavananda Bharati (1973) and Minerva Mills (1980) limit the amending power."},
    {"label": "constitutional morality and transformation", "stem": "Which use of constitutional morality is legitimate?", "correct": "Reasoning anchored in constitutional text, procedures, equal citizenship and institutional role morality.", "wrong": ["A judge's personal morality as a free-standing veto.", "Social popularity without constitutional source.", "Automatic displacement of legislative competence."], "explanation": "Navtej Singh Johar v. Union of India (2018) links transformative reasoning to rights and structure."},
    {"label": "precedent and remedy", "stem": "Which proposition correctly connects Articles 141 and 142?", "correct": "Binding ratio and bench strength control precedent; Article 142 supplies case-bound complete justice but cannot disregard substantive law.", "wrong": ["Every judicial sentence is binding ratio.", "A smaller bench may silently overrule a larger bench.", "Article 142 is an unlimited source of legislative power."], "explanation": "Supreme Court Bar Association (1998) marks the substantive-law limit."},
]


P55_PYQS = r"""
### Verified direct PYQ 1 — UPSC Mains 2019, GS Paper II, Question 4

**Exact question:** "From the resolution of contentious issues regarding distribution of
legislative powers by the courts, 'Principle of Federal Supremacy' and 'Harmonious Construction'
have emerged. Explain." **10 marks, 150 words.**

**Model answer:** Courts first identify the true field through pith and substance and interpret
entries broadly so incidental overlap does not disable government. Harmonious construction then
assigns meaningful operation to both fields or provisions. Only an irreconcilable conflict triggers
the Constitution's priority rules: Article 246 gives Union-list priority, while Article 254 governs
repugnancy in the same Concurrent field. M. Karunanidhi v. Union of India (1979) requires actual
inconsistency; mere overlap is insufficient. Federal supremacy is therefore a final constitutional
rule, not a shortcut that erases State competence.

### Verified direct PYQ 2 — UPSC Mains 2021, GS Paper II, Question 1

**Exact question:** "'Constitutional Morality' is rooted in the Constitution itself and is founded
on its essential facets. Explain the doctrine of 'Constitutional Morality' with the help of relevant
judicial decisions." **10 marks, 150 words.**

**Model answer:** Constitutional morality means fidelity to constitutional text, procedure, equal
citizenship and the role morality of institutions rather than social or personal morality.
Kesavananda Bharati (1973) protects structural limits; Government of NCT of Delhi and Navtej Singh
Johar v. Union of India (2018) connect constitutional conduct with accountable government, dignity
and equality. The doctrine can test exclusion and abuse of office, but must identify the governing
Article, precedent and remedy. It is thus disciplined constitutional reasoning, not a free-standing
judicial power to impose moral preference.

### Supporting PYQ 3 — UPSC Mains 2019, GS Paper II, Question 12

**Exact question:** "'Parliament's power to amend the Constitution is a limited power and it cannot
be enlarged into absolute power.' In the light of this statement, explain whether Parliament under
Article 368 of the Constitution can destroy the Basic Structure of the Constitution by expanding
its amending power." **15 marks, 250 words.**

**Solution spine:** Article 368 power and procedure -> Kesavananda Bharati (1973) -> limited amending
power -> Minerva Mills (1980) -> judicial review/basic features -> no self-enlargement into
unlimited constituent power -> qualified conclusion distinguishing amendment from interpretation.

### Supporting PYQ 4 — UPSC Prelims 2020, GS Paper I, Question 13

**Exact question:** Consider the following statements:

1. The Constitution of India defines its 'basic structure' in terms of federalism, secularism,
   fundamental rights and democracy.
2. The Constitution of India provides for 'judicial review' to safeguard the citizens' liberties
   and to preserve the ideals on which the Constitution is based.

- A. 1 only
- B. 2 only
- C. Both 1 and 2
- D. Neither 1 nor 2

**Official-key answer:** D. Statement 1 falsely attributes a judicially evolved, non-exhaustive
doctrine to an express constitutional definition. The official key also rejects Statement 2's
specific attribution; the Constitution creates judicial-review powers through provisions such as
Articles 13, 32 and 226, while the quoted purpose is doctrinal description rather than enacted text.

### Supporting PYQ 5 — UPSC Prelims 2023, GS Paper I, Question 34

**Exact question:** In India, which one of the following Constitutional Amendments was widely
believed to be enacted to overcome the judicial interpretations of the Fundamental Rights?

- A. 1st Amendment
- B. 42nd Amendment
- C. 44th Amendment
- D. 86th Amendment

**Official status:** The question was dropped. No scored official answer is attributed. The First
Amendment is the historical route commonly discussed, but a dropped question must remain labelled
as such.

### Supporting PYQ 6 — UPSC Mains 2025, GS Paper II, Question 11

**Exact question:** "'Constitutional morality is the fulcrum which acts as an essential check upon
the high functionaries and citizens alike....' In view of the above observation of the Supreme
Court, explain the concept of constitutional morality and its application to ensure balance between
judicial independence and judicial accountability in India." **15 marks, 250 words.**

**Solution spine:** Define text/role morality -> independence as structural guarantee -> reasons,
recusal, ethics, open justice and review as accountability -> no political control over decisions
and no personal immunity -> institutional balance and public confidence.

**Why these answers earn marks:** Each begins with the controlling text, states the operative test,
uses a leading case and specifies legal effect and limitation. **How to improve:** Never cite a
doctrine as a slogan; apply its elements to the facts and distinguish holding, obiter and pending
questions.
"""


P55_MAINS = [
    ("Compare severability, eclipse and prospective overruling as techniques that moderate invalidity.", "Compare", 15, "Severability concerns parts of a law: under Article 13 the court removes only the unconstitutional portion when the remainder is separable, workable and intended, as in R.M.D. Chamarbaugwala v. Union of India (1957). Eclipse concerns enforceability: Bhikaji Narain Dhakras (1955) classically treats inconsistent pre-Constitution law as dormant to the extent of conflict, capable of revival if the impediment disappears. Prospective overruling concerns time: I.C. Golaknath (1967) allows a new judicial rule to operate prospectively while preserving specified past effects. None is automatic. Severability cannot rewrite a scheme, eclipse is not repeal, and prospective effect must be expressly reasoned. Together they protect constitutional supremacy while avoiding unnecessarily destructive remedies."),
    ("Analyse pith and substance, ancillary power and colourable legislation as a competence sequence.", "Analyse", 15, "The court first asks the true nature and character of the law—its purpose, scope and effects. If its dominant field lies within competence, pith and substance tolerates incidental overlap. Ancillary power then supports provisions reasonably necessary to make the granted entry effective. Colourable legislation supplies the negative check: K.C. Gajapati Narayan Deo (1953) prevents form from disguising a law whose substance lies outside power, though bad motive alone is insufficient. The sequence preserves workable federal regulation without permitting indirect usurpation. A strong answer therefore moves from dominant field, to genuine auxiliary measure, to disguised incompetence."),
    ("Explain the complete Article 254 repugnancy test and the limits of Presidential assent.", "Explain", 15, "Repugnancy begins only when Parliamentary and State laws occupy the same Concurrent field. The court compares their commands and schemes: can both be obeyed, did Parliament intend exhaustive coverage, or does one law frustrate the other? Deep Chand (1959) and M. Karunanidhi v. Union of India (1979) require actual inconsistency; mere existence of a Union law is not enough. Under Article 254(1), Union law prevails and State law is void only to the extent of repugnancy. A State law reserved for and assented to by the President may prevail in that State under Article 254(2), but assent cannot cure lack of State competence and Parliament may later override it."),
    ("Critically evaluate harmonious construction as a doctrine of constitutional restraint.", "Critically evaluate", 10, "Harmonious construction seeks a reading that gives meaningful operation to apparently conflicting provisions, entries or values. In re Kerala Education Bill (1958) illustrates reconciliation rather than mechanical destruction of one norm. The doctrine supports federal balance and Part III-Part IV coherence by requiring courts to test text, context and structural purpose before invoking supremacy. Its restraint lies in preserving enacted choices. Its limit is equally important: harmony cannot contradict express words, erase a proviso or neutralise a constitutionally declared priority. It is therefore a disciplined first response to apparent conflict, not a device for rewriting the Constitution."),
    ("Assess the legitimacy and limits of prospective overruling in constitutional adjudication.", "Assess", 15, "Prospective overruling separates the declaration of a new legal rule from its temporal consequences. Introduced in I.C. Golaknath (1967), it can protect settled transactions, administrative reliance and legal certainty when immediate retrospectivity would cause disruptive injustice. Yet it creates unequal temporal treatment and may resemble judicial legislation if used without clear reasons. The court should identify the old rule, new rule, protected class of past effects and constitutional justification for the cut-off. It is not automatic whenever precedent changes. Properly reasoned, the doctrine balances constitutional correction with rule-of-law stability; casually invoked, it weakens equality and predictability."),
    ("Distinguish constitutional morality from transformative constitutionalism and personal morality.", "Distinguish", 15, "Constitutional morality concerns fidelity to constitutional text, procedures, equal citizenship and institutional roles. Transformative constitutionalism describes the Constitution's lawful project of dismantling status hierarchy and realising liberty, equality, dignity and fraternity. Navtej Singh Johar v. Union of India (2018) illustrates their interaction in rights adjudication. Personal or social morality, by contrast, has no independent power to override constitutional guarantees. Both constitutional concepts must identify an Article, structure, precedent and remedy; neither authorises judges to ignore competence or invent a complete policy code. Constitutional morality disciplines institutions, while transformation supplies direction within those disciplines."),
    ("Construct a doctrine-selection method for a complex constitutional challenge.", "Construct", 20, "Begin with jurisdiction and text. Identify the enacting institution, Article and legislative entry. For field overlap, apply pith and substance, ancillary power, colourability and territorial nexus; use Article 254 only for the same Concurrent field and actual conflict. Next identify the affected right and apply classification, arbitrariness or proportionality as appropriate. Then choose the invalidity tool: read down if text bears a valid meaning, sever if the remainder is workable, otherwise strike down. Decide temporal effect through reasoned prospective overruling. Finally apply Article 141 bench hierarchy and choose a remedy no broader than necessary, remembering Article 142 cannot disregard substantive law. This sequence converts slogans into a reviewable legal method."),
    ("Examine how precedent and bench strength constrain constitutional creativity.", "Examine", 10, "Article 141 binds courts to the law declared by the Supreme Court, principally the ratio necessary to the decision. Obiter may persuade but does not carry the same force. A smaller bench cannot overrule a larger one; a coordinate bench should distinguish on material grounds or refer the conflict. This hierarchy promotes equal treatment and legal certainty while allowing principled change through a proper larger bench. Article 142 permits complete justice in the cause before the Court, but Supreme Court Bar Association (1998) confirms that it cannot displace substantive law. Constitutional creativity is therefore legitimate when transparent about text, ratio, bench strength and remedy."),
]


P55_PANELS = [
    ("Method before doctrine", "TEXT -> STRUCTURE -> HISTORY -> PURPOSE -> BINDING PRECEDENT.\nTRIGGER -> TEST -> CASE/YEAR -> EFFECT -> LIMIT -> REMEDY.\nAPPLICATION -> facts must satisfy every operative element.\nDOCTRINE != free-standing Article or slogan."),
    ("Severability, eclipse and waiver", "R.M.D. Chamarbaugwala v. Union of India (1957) -> separable workable remainder.\nBhikaji Narain Dhakras (1955) -> pre-Constitution law dormant to conflict extent.\nBasheshar Nath (1958) -> consent cannot validate unconstitutional State action.\nOBJECT CHECK -> part of law / enforceability / individual consent."),
    ("Pith, ancillary power and colourability", "Prafulla Kumar Mukherjee (1947) -> true nature and character.\nState of Bombay v. F.N. Balsara (1951) -> incidental overlap / effective entry.\nK.C. Gajapati Narayan Deo (1953) -> disguised lack of competence.\n\nMOTIVE alone is insufficient."),
    ("Territorial nexus", "ART 245 -> territorial competence.\nState of Bombay v. R.M.D. Chamarbaugwala (1957) -> real and sufficient nexus.\nTEST: connection between State, subject and imposed liability/operation.\n\nREMOTE OR ILLUSORY nexus fails."),
    ("Article 254 repugnancy and occupied field", "Deep Chand v. State of Uttar Pradesh (1959) + M. Karunanidhi v. Union of India (1979).\nSAME CONCURRENT FIELD -> actual inconsistency / exhaustive scheme -> Union priority.\nART 254(1) EFFECT -> State law void only to the extent of repugnancy.\nART 254(2) ASSENT -> State prevalence; no cure for incompetence; Parliament may override."),
    ("Harmony, reading and invalidity", "In re Kerala Education Bill (1958) -> meaningful reconciliation.\nKedar Nath Singh (1962) -> reading down within text.\nREADING INTO -> strong constitutional basis; cannot create a complete code.\nSEVER / STRIKE -> only after saving construction fails."),
    ("Time, amendment and basic structure", "I.C. Golaknath (1967) -> reasoned prospective overruling.\nKesavananda Bharati (1973) -> Article 368 cannot damage basic structure.\nMinerva Mills (1980) -> limited amending power + Part III/IV harmony.\n\nINTERPRETATION != AMENDMENT."),
    ("Equality standards and proportionality", "Ram Krishna Dalmia (1958) -> rebuttable validity presumption.\nE.P. Royappa (1973) -> arbitrariness/equality.\nModern Dental College (2016) -> structured proportionality.\nShayara Bano v. Union of India (2017) -> manifest arbitrariness.\nK.S. Puttaswamy (2017) + Anuradha Bhasin (2020) -> rights justification."),
    ("Morality, transformation and religion", "Navtej Singh Johar v. Union of India (2018) -> constitutional morality + transformation.\nShirur Mutt (1954) -> religious/secular distinction.\nIndian Young Lawyers Association (2018) -> equality, dignity and religion conflict.\n\nPENDING review/reference != changed holding."),
    ("Administration and textual restraint", "Shamsher Singh (1974) -> pleasure/responsible government.\nMotilal Padampat Sugar Mills (1978) -> promissory estoppel limits.\nNavjyoti Cooperative Group Housing (1992) -> legitimate expectation.\nPadma Sundara Rao (2002) -> casus omissus restraint."),
    ("Precedent, bench strength and Article 142", "ARTICLE 141 -> binding ratio; distinguish or refer.\nSupreme Court Bar Association (1998) -> Article 142 cannot disregard substantive law.\nSMALLER BENCH -> no silent overruling.\nOBITER -> persuasive, not automatically binding."),
    ("UPSC integrated decision tree", "1 COMPETENCE -> pith / colour / nexus / Art 254.\n2 MEANING -> harmony / purpose / precedent.\n3 RIGHTS -> equality / proportionality.\n4 INVALIDITY -> read down / sever / strike.\n5 TIME + AUTHORITY -> prospective effect / Article 141.\n\nVERDICT: exact tests constrain judicial choice."),
]


def mains_block(items: list[tuple[str, str, int, str]]) -> str:
    rows: list[str] = ["### Original solved Mains practice"]
    for number, (question, directive, marks, answer) in enumerate(items, 1):
        words = 150 if marks == 10 else 250
        rows.extend(
            [
                "",
                f"#### M{number}. {question}",
                "",
                f"**Directive:** {directive} | **Marks:** {marks} | **Answer in:** {words} words.",
                "",
                "**Demand decode:** Define the exact constitutional issue, organise by legal source "
                "and effect, use named evidence, confront the strongest limit and reach a qualified verdict.",
                "",
                f"**Model answer:** {answer}",
                "",
                "**Why this earns marks:** The answer follows claim -> named Article/amendment/case -> "
                "analysis -> qualification and directly obeys the directive.",
                "",
                "**How to improve:** Convert the first sentence into a precise thesis, underline the "
                "controlling Articles/cases and reserve the final two sentences for a graded conclusion.",
                "",
                f"**Compression plan:** 20-25 words of introduction, {85 if marks == 10 else 175} words "
                "of organised analysis and 25-35 words of qualified conclusion.",
            ]
        )
    return "\n".join(rows)


def write_ascii_spec(topic_key: str, title: str, panels: list[tuple[str, str]], source: Path) -> Path:
    path = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / f"{topic_key}-2026-08-25-sequential.json"
    )
    payload = {
        "schema_version": 1,
        "id": f"{topic_key}-ascii-panels-deep-review-2026-08-29",
        "created_on": GENERATION_DATE,
        "design_benchmark": (
            "notes\\Philosophy\\Philosophy-of-Religion\\flowcharts\\01_Notions-of-God\\"
            "continuous-at-a-glance-carvaka-standard-g9\\"
            "Notions-of-God_Complete-Topic_ASCII-Master-Flow-Diagram.txt"
        ),
        "scope": "Deep-review successor; twelve complete Core panels plus generated subordinate enrichment.",
        "constraints": {
            "panels_per_topic": "12",
            "max_characters_per_line": 100,
            "captions_or_source_notes_as_nodes": False,
            "forbidden_patterns": ["ellipsis", "placeholder", "session-card dump", "generic answer spine"],
        },
        "topic_count": 1,
        "topics": {
            topic_key: {
                "title": title,
                "source_record": f"{topic_key}:learner-v2:successor-pending",
                "source_markdown": rel(source),
                "quality_review": "Manual doctrinal review against constitutional text, cases, PYQs and owner boundaries.",
                "approved_master_reference": (
                    "notes\\Philosophy\\Philosophy-of-Religion\\flowcharts\\01_Notions-of-God\\"
                    "continuous-at-a-glance-carvaka-standard-g9\\"
                    "Notions-of-God_Complete-Topic_ASCII-Master-Flow-Diagram.txt"
                ),
                "benchmark_preservation": "Reference is read-only and hash-preserved.",
                "panel_count": len(panels),
                "panels": [
                    {
                        "title": panel_title,
                        "structural_type": f"deep-review-{index:02d}",
                        "source_references": [f"{rel(source)}#BASIC LEARNING SESSION"],
                        "full_text": body,
                    }
                    for index, (panel_title, body) in enumerate(panels, 1)
                ],
            }
        },
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def normalize_graphical_strings(topic_key: str, value: object, key: str = "") -> object:
    if isinstance(value, str):
        if key == "source_references":
            return value
        return batch.case_years.normalize_text(topic_key, value)
    if isinstance(value, list):
        return [normalize_graphical_strings(topic_key, item, key) for item in value]
    if isinstance(value, dict):
        return {
            item_key: normalize_graphical_strings(topic_key, item, item_key)
            for item_key, item in value.items()
        }
    return value


def write_graphical_spec(config: dict[str, object], source: Path, ascii_path: Path) -> Path:
    manual = batch.base.refresh.ascii_master.normalize_manual_spec_file(ascii_path)[str(config["key"])]
    panels = [
        {
            "title": panel.title,
            "structural_type": panel.structural_type,
            "body": panel.body,
            "source_references": list(panel.source_references),
        }
        for panel in manual.panels
    ]
    checker = batch.base.graphical.polity_flowchart_case_years.graphical_spec_errors
    batch.base.graphical.polity_flowchart_case_years.graphical_spec_errors = lambda spec: []
    try:
        spec = batch.base.graphical.author_topic_spec(
            topic_key=str(config["key"]),
            subject="Polity",
            title=str(config["title"]),
            source_markdown=source.read_text(encoding="utf-8"),
            source_markdown_path=rel(source),
            ascii_spec_path=rel(ascii_path),
            ascii_spec_sha256=sha256(ascii_path),
            panels=panels,
            source_generation=2,
        )
    finally:
        batch.base.graphical.polity_flowchart_case_years.graphical_spec_errors = checker
    spec = normalize_graphical_strings(str(config["key"]), spec)
    errors = batch.case_years.graphical_spec_errors(spec)
    if errors:
        raise RuntimeError("Graphical case-year normalization failed: " + " | ".join(errors))
    path = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "carvaka-graphical-specs"
        / "Polity"
        / f"{config['key']}.json"
    )
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def build_p53() -> tuple[Path, Path, Path]:
    basic = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "basic" / "Special-Provisions-Relating-to-Certain-Classes.md"
    advanced = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "advanced" / "53_Special-Provisions-Relating-to-Certain-Classes.md"
    source_dir = REVIEW / "reviews" / "polity-53" / "g3-source"
    source_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / "polity-53_g3-reviewed-source.md"
    register = "\n".join(
        [
            "### Rapid constitutional map",
            "",
            *[f"- **{fact['label']}:** {fact['correct']}" for fact in P53_FACTS],
            "",
            "### Answer spine",
            "",
            "Field -> beneficiary class -> constitutional source -> competent authority -> procedure -> "
            "legal effect -> limitation -> current-status date -> qualified substantive-equality verdict.",
        ]
    )
    text = f"""---
title: "Special Provisions Relating to Certain Classes — Learner-v2 Deep Reviewed"
topic_key: polity-53
---
# Special Provisions Relating to Certain Classes — Complete Deep-Reviewed Learning Session

**Legal/current control date:** {CONTROL_DATE} (Asia/Kolkata)

> **Source discipline:** Constitutional text, amendment commencement, electoral operation,
> judgments, policy and analytical inference are separately identified. The reviewed g2 generation
> remains immutable and its score is not carried forward.

## BASIC LEARNING SESSION

{clean_owner(basic)}

## BASIC MCQS / REMEDIATION

{mcq_block(P53_FACTS)}

## PYQS AND ANSWER PRACTICE

{P53_PYQS.strip()}

{mains_block(P53_MAINS)}

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

{clean_owner(advanced)}

## CONSOLIDATED REGISTER NOTES

{register}
"""
    text = batch.case_years.normalize_text("polity-53", text)
    source.write_text(text, encoding="utf-8")
    ascii_path = write_ascii_spec("polity-53", "Special Provisions Relating to Certain Classes", P53_PANELS, source)
    config = next(item for item in batch.TOPICS if item["key"] == "polity-53")
    graph_path = write_graphical_spec(config, source, ascii_path)
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    graph["status"] = {
        "approved": False,
        "review": "REVALIDATION PENDING",
        "line": "Approval: FALSE | immutable successor generated after deep review | baseline g2 preserved",
    }
    graph["source_markdown"] = rel(source)
    graph["ascii_spec_sha256"] = sha256(ascii_path)
    graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return source, ascii_path, graph_path


def build_p54() -> tuple[Path, Path, Path]:
    basic = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "basic" / "Lok-Adalats-and-Other-Courts.md"
    advanced = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "advanced" / "54_Lok-Adalats-and-Other-Courts.md"
    source_dir = REVIEW / "reviews" / "polity-54" / "g3-source"
    source_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / "polity-54_g3-reviewed-source.md"
    register = "\n".join(
        [
            "### Forum and effect map",
            "",
            *[f"- **{fact['label']}:** {fact['correct']}" for fact in P54_FACTS],
            "",
            "### Answer spine",
            "",
            "Constitutional anchor -> statutory source -> institution -> stage and subject matter -> "
            "consent/merits power -> award -> appeal/review -> access safeguards -> dated status.",
        ]
    )
    text = f"""---
title: "Lok Adalats and Other Courts — Learner-v2 Deep Reviewed"
topic_key: polity-54
---
# Lok Adalats and Other Courts — Complete Deep-Reviewed Learning Session

**Legal/current control date:** {CONTROL_DATE} (Asia/Kolkata)

> **Source discipline:** The current pecuniary ceiling, notified public utility services,
> institution counts and commencement status are never frozen without a dated official source.
> The reviewed g2 generation remains immutable.

## BASIC LEARNING SESSION

{clean_owner(basic)}

## BASIC MCQS / REMEDIATION

{mcq_block(P54_FACTS)}

## PYQS AND ANSWER PRACTICE

{P54_PYQS.strip()}

{mains_block(P54_MAINS)}

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

{clean_owner(advanced)}

## CONSOLIDATED REGISTER NOTES

{register}
"""
    text = batch.case_years.normalize_text("polity-54", text)
    source.write_text(text, encoding="utf-8")
    ascii_path = write_ascii_spec("polity-54", "Lok Adalats and Other Courts", P54_PANELS, source)
    config = next(item for item in batch.TOPICS if item["key"] == "polity-54")
    graph_path = write_graphical_spec(config, source, ascii_path)
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    graph["status"] = {
        "approved": False,
        "review": "REVALIDATION PENDING",
        "line": "Approval: FALSE | immutable successor generated after deep review | baseline g2 preserved",
    }
    graph["source_markdown"] = rel(source)
    graph["ascii_spec_sha256"] = sha256(ascii_path)
    graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return source, ascii_path, graph_path


def build_p55() -> tuple[Path, Path, Path]:
    basic = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "basic" / "Constitutional-Interpretation-Doctrines.md"
    advanced = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "advanced" / "55_Constitutional-Interpretation-Doctrines.md"
    source_dir = REVIEW / "reviews" / "polity-55" / "g3-source"
    source_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / "polity-55_g3-reviewed-source.md"
    register = "\n".join(
        [
            "### Doctrine trigger map",
            "",
            *[f"- **{fact['label']}:** {fact['correct']}" for fact in P55_FACTS],
            "",
            "### Answer spine",
            "",
            "Text and competence -> doctrinal trigger -> operative elements -> leading holding/year -> "
            "application -> legal effect -> institutional limit -> proportionate remedy.",
        ]
    )
    basic_text = clean_owner(basic)
    basic_text = re.sub(
        r"### Comprehensive doctrine atlas\n.*?(?=> \*\*Interpretation–amendment firewall:)",
        "### Comprehensive doctrine atlas — compact use\n\n"
        "Use the doctrine-selection matrix and the full operative sections above. For each answer, "
        "write: **trigger -> governing Article -> elements -> leading case/year -> legal effect -> "
        "limit**. This compact route preserves the atlas without an unreadable six-column table.\n\n",
        basic_text,
        flags=re.S,
    )
    text = f"""---
title: "Constitutional Interpretation Doctrines — Learner-v2 Deep Reviewed"
topic_key: polity-55
---
# Constitutional Interpretation Doctrines — Complete Deep-Reviewed Learning Session

**Legal/current control date:** {CONTROL_DATE} (Asia/Kolkata)

> **Source discipline:** A case name without its governing Article, operative test, legal effect,
> limitation and decision year is not treated as doctrine. Pending review or reference proceedings
> do not alter a larger-bench holding.

## BASIC LEARNING SESSION

{basic_text}

## BASIC MCQS / REMEDIATION

{mcq_block(P55_FACTS)}

## PYQS AND ANSWER PRACTICE

{P55_PYQS.strip()}

{mains_block(P55_MAINS)}

## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER

{clean_owner(advanced)}

## CONSOLIDATED REGISTER NOTES

{register}
"""
    text = batch.case_years.normalize_text("polity-55", text)
    source.write_text(text, encoding="utf-8")
    ascii_path = write_ascii_spec("polity-55", "Constitutional Interpretation Doctrines", P55_PANELS, source)
    config = next(item for item in batch.TOPICS if item["key"] == "polity-55")
    graph_path = write_graphical_spec(config, source, ascii_path)
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    graph["status"] = {
        "approved": False,
        "review": "REVALIDATION PENDING",
        "line": "Approval: FALSE | immutable successor generated after deep review | baseline g2 preserved",
    }
    graph["source_markdown"] = rel(source)
    graph["ascii_spec_sha256"] = sha256(ascii_path)
    graph_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return source, ascii_path, graph_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True, choices=["polity-53", "polity-54", "polity-55"])
    args = parser.parse_args()
    if args.topic == "polity-53":
        paths = build_p53()
    elif args.topic == "polity-54":
        paths = build_p54()
    else:
        paths = build_p55()
    print("\n".join(rel(path) for path in paths))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
