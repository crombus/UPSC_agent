"""Extend the hostile Polity deep-review workflow to topics 36-40."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_31_35_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST
PYQ_LEDGERS = deep.PYQ_LEDGERS

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    36: (
        "Keep the constitutional Article 19(1)(a) right-to-know root distinct "
        "from the statutory CIC/SIC machinery created by the RTI Act, 2005.",
        "Separate requests, first appeals, second appeals and section 18 "
        "complaints; a Commission cannot be treated as a record-creation agency.",
        "The 13 November 2025 DPDP substitution is operative but section 8(2), "
        "section 10 and judicial review remain; Raj Kumar Goyal heads the CIC.",
    ),
    37: (
        "Keep the statutory CVC, executive-created CBI and statutory DSPE police "
        "establishment legally distinct despite their connected vigilance work.",
        "CVC superintendence is offence-field specific and does not permit "
        "dictating a particular investigation, conviction or disciplinary result.",
        "A S Rajeev is acting Central Vigilance Commissioner; Praveen Vashista is "
        "Vigilance Commissioner; Praveen Sood's CBI term runs to 24 May 2027.",
    ),
    38: (
        "Treat Lokpal as a statutory corruption-complaint institution under the "
        "2013 Act, not as a constitutional court, police force or ombudsman for every grievance.",
        "Prime-Minister safeguards, parliamentary privilege, the seven-year bar, "
        "agency dependence and State-law Lokayukta variation must remain explicit.",
        "Justice A. M. Khanwilkar and the six officially listed Members form the "
        "dated central roster; the 2025 High Court-judge jurisdiction order remains stayed.",
    ),
    39: (
        "Preserve the post-Rajendra N. Shah split: State-field cooperatives remain "
        "under Entry 32 and State law; Part IXB survives for the multi-State field.",
        "Do not merge the Ministry, CRCS, Election Authority, Ombudsman, RBI, "
        "NABARD, representative federations or operating cooperative societies.",
        "The MSCS Amendment Act and Rules, 2023 remain operative; National "
        "Cooperation Policy 2025 is policy, not a transfer of legislative competence.",
    ),
    40: (
        "State precisely that Hindi in Devanagari is the Union's official language "
        "and that the Constitution declares no national language.",
        "Keep Union, State, court, grievance, minority-instruction, scheduled, "
        "classical and education-policy language categories separate.",
        "The 1963 Act, 1967 settlement and 1976 Rules as amended through 2011 "
        "remain operative; the Eighth Schedule contains twenty-two languages.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    36: """### Semantic-completeness ownership and PYQ control

- **Status and constitutional root:** CIC and SIC are statutory bodies under
  the Right to Information Act, 2005. The right to know is derived from
  Article 19(1)(a), but the Commission's office, jurisdiction and remedies come
  from the Act rather than directly from the Constitution.
- **Current central roster, checked 5 September 2026:** the official CIC
  present-commission pages identify Chief Information Commissioner Raj Kumar
  Goyal and Information Commissioners Anandi Ramalingam, Vinod Kumar Tiwari,
  Surendra Singh Meena, Ashutosh Chaturvedi, Swagat Das, Sudha Rani Relangi,
  P. R. Ramesh, Khushwant Singh Sethi, Jaya Varma Sinha and Sanjeev Kumar
  Jindal. State rosters remain State-specific and must be checked separately.
- **Composition and appointment:** the CIC consists of the Chief and up to ten
  Information Commissioners, appointed by the President after the statutory
  PM-LoP-nominated Cabinet Minister committee. The SIC analogue is appointed
  by the Governor after the CM-LoP-nominated State Cabinet Minister committee.
- **Tenure and independence:** after the 2019 amendment, tenure and service
  conditions are prescribed by Central rules. The 2019 Rules prescribe three
  years, subject to the statutory age ceiling of sixty-five; an IC elevated as
  Chief cannot exceed the aggregate statutory service limit. Removal for proved
  misbehaviour or incapacity follows the Supreme Court inquiry route.
- **Four-route firewall:** section 6 request -> section 7 decision/deemed
  refusal -> section 19(1) first appeal -> section 19(3) second appeal.
  Section 18 complaint is a distinct supervisory route and does not itself
  become the substitute disclosure appeal identified in State of Manipur.
- **Powers and remedies:** sections 18-20 confer inquiry/civil-court powers,
  binding disclosure/compliance directions, compensation, recommendation of
  disciplinary action and personal PIO penalty of Rs 250 per day up to
  Rs 25,000. They do not authorize creation of non-existent records.
- **Exemption architecture:** sections 8 and 9 are exemptions, section 8(2) is
  the public-interest override, section 10 requires severability, section 11 is
  third-party procedure rather than an exemption, and section 24 preserves the
  corruption and human-rights provisos for listed organisations.
- **Current privacy law:** DPDP Act section 44(3) substituted section 8(1)(j)
  with effect from 13 November 2025. The shorter personal-information exemption
  is in force; section 8(2), severability, reasons, appeal and judicial review
  remain. The constitutional challenge has not produced a final merits holding.
- **Case controls:** Raj Narain and S.P. Gupta ground open government; CBSE v.
  Aditya Bandopadhyay limits RTI to held/controlled records; Chief Information
  Commissioner v. State of Manipur separates complaint and appeal; Thalappalam
  controls the public-authority test; Jayantilal Mistry rejects blanket
  fiduciary secrecy; Subhash Chandra Agarwal applies privacy balancing to the
  CJI's office; Anjali Bhardwaj and Kishan Chand Jain address functioning,
  appointments and access.
- **PYQ firewall:** the verified 2020 GS-II RTI-amendment/autonomy demand is
  owned here. Privacy, data protection, judicial administration and cooperative
  public-authority questions remain cross-owned where their principal demand lies.""",
    37: """### Semantic-completeness ownership and PYQ control

- **Legal identity:** CVC is statutory under the Central Vigilance Commission
  Act, 2003. CBI is an organisation constituted by executive resolution on
  1 April 1963; the Delhi Special Police Establishment Act, 1946 supplies its
  core police powers. Neither is a constitutional body.
- **Current leadership, checked 5 September 2026:** A S Rajeev, a serving
  Vigilance Commissioner, is authorised to act as Central Vigilance
  Commissioner from 3 August 2026; Praveen Vashista is the other officially
  identified Vigilance Commissioner. Praveen Sood continues as CBI Director
  under the dated extension through 24 May 2027.
- **CVC appointment and tenure:** the President appoints the Central Vigilance
  Commissioner and up to two Vigilance Commissioners after recommendation by
  the PM-Home Minister-LoP committee. The term is four years or age sixty-five,
  whichever is earlier. Removal for proved misbehaviour/incapacity uses a
  Supreme Court inquiry; direct statutory grounds remain separate.
- **CVC jurisdiction:** section 8 functions include specified superintendence
  over DSPE corruption investigations, vigilance administration, inquiry or
  investigation on references/complaints, review of investigation progress and
  prosecution-sanction applications, and advice. Directions cannot require
  disposal of a particular case in a particular manner.
- **CVO and disciplinary boundary:** Central Vigilance Officers connect
  prevention, complaint scrutiny and departmental action. CVC advice informs
  the competent disciplinary authority but is not a criminal judgment or
  universally binding adjudication.
- **CBI Director:** appointment follows DSPE section 4A through the
  PM-LoP-CJI/nominee committee after the statutory eligibility panel. The
  minimum tenure is two years. The 2021 amendment permits recorded
  public-interest extensions one year at a time up to five years in aggregate;
  five years is not automatic. Transfer requires committee consent.
- **Territorial jurisdiction:** sections 3 and 5 identify notified offences and
  extension of DSPE powers; section 6 ordinarily requires State consent.
  General consent can be withdrawn prospectively, specific consent remains
  possible, and constitutional courts retain exceptional Articles 32/226 power
  to direct a CBI investigation without consent.
- **Superintendence split:** CVC superintends DSPE investigation of specified
  Prevention of Corruption Act offences; the Central Government superintends
  other DSPE matters. Lokpal has bounded superintendence for Lokpal-referred cases.
- **Case controls:** Vineet Narain created the independence architecture;
  Committee for Protection of Democratic Rights (2010) preserves constitutional
  court power; Kazi Lhendup Dorji addresses validly begun investigations after
  consent withdrawal; Fertico is fact-specific; Alok Kumar Verma protects the
  statutory Director process; Jaya Thakur upheld the conditional extension framework.
- **PYQ firewall:** the verified 2021 GS-II federal-consent demand and the
  controlled 2026 objective institutional-matching demand are owned here.
  No current State-consent count or caseload statistic is frozen.""",
    38: """### Semantic-completeness ownership and PYQ control

- **Status and source:** Lokpal is a statutory body under the Lokpal and
  Lokayuktas Act, 2013 (Act 1 of 2014), read with the 2016 amendment, Complaint
  Rules, 2020 and applicable administrative/recruitment rules. It is neither a
  constitutional court nor a general grievance commission.
- **Current roster, checked 5 September 2026:** Justice Ajay Manikrao
  Khanwilkar is Chairperson. The official present-member pages list judicial
  members Justice L. Narayana Swamy, Justice Sanjay Yadav and Justice Ritu Raj
  Awasthi, and members Sushil Chandra, Pankaj Kumar and Ajay Tirkey. No occupant
  is invented for an unfilled statutory seat.
- **Composition and representation:** Chairperson plus not more than eight
  Members; at least fifty per cent of Members are judicial, and at least fifty
  per cent of Members must collectively come from the named SC/ST/OBC/minority/
  women categories. The representation rule does not add seats.
- **Selection and tenure:** the statutory selection committee is PM, Lok Sabha
  Speaker, LoP, CJI/nominee and eminent jurist. A Search Committee assists.
  The President appoints. Term is five years or age seventy, whichever is
  earlier, without reappointment; statutory removal safeguards apply.
- **Jurisdiction:** covered persons include the PM subject to special filters,
  Union Ministers, MPs, Groups A-D officials, former covered public servants
  and qualifying government-linked/donation/foreign-contribution entities.
  Parliamentary speech and vote remain constitutionally protected.
- **Prime-Minister safeguards:** excluded subject matters, full-bench
  screening, two-thirds approval, in-camera proceedings and confidentiality
  qualify the ordinary complaint route. Coverage is not equivalent to an
  unrestricted investigation power.
- **Process and powers:** complaint scrutiny may lead to preliminary inquiry or
  investigation, followed by disciplinary, sanction or prosecution directions
  within the Act. The Inquiry and Prosecution Wings, CVC and CBI remain distinct;
  guilt and punishment belong to the Special Court.
- **Limits:** the Act does not create a general suo-motu grievance power; the
  seven-year limitation, statutory procedure, natural justice and judicial
  review remain. The 2016 asset-return amendment must not be confused with
  restoration of the original public-disclosure form.
- **Judges and State variation:** the Supreme Court stayed the Lokpal's
  27 January 2025 High Court-judge jurisdiction order on 20 February 2025; no
  final merits proposition is asserted. Section 63 requires State establishment,
  but each Lokayukta's composition, appointment, jurisdiction and powers depend
  on its own State law.
- **PYQ/case firewall:** Common Cause (2017) prevented implementation delay;
  Lok Prahari concerns electoral disclosure; Sita Soren (2024) rejects
  bribery immunity under legislative privilege. The direct 2025 Prelims Lokpal
  composition/jurisdiction demand is owned here; no direct Mains PYQ is invented.""",
    39: """### Semantic-completeness ownership and PYQ control

- **Federal map:** State-field cooperative societies belong principally to
  Entry 32, State List and the respective State cooperative law. Corporations
  whose objects are not confined to one State fall under Entry 44, Union List
  and the Multi-State Co-operative Societies Act, 2002.
- **97th Amendment:** the Constitution (Ninety-seventh Amendment) Act, 2011
  inserted cooperative societies into Article 19(1)(c), inserted Article 43B,
  and added Part IXB, Articles 243ZH-243ZT. It came into force on 15 February 2012.
- **Rajendra N. Shah control:** the Supreme Court's 2021 majority invalidated
  Part IXB insofar as it governed ordinary State-field cooperatives because the
  amendment lacked State ratification under Article 368(2). Article 19(1)(c),
  Article 43B and Part IXB's multi-State operation survive; the whole 97th
  Amendment was not struck down.
- **Part IXB content:** within its surviving field it regulates incorporation,
  board composition and five-year tenure, elections before expiry,
  supersession limits, audit, returns, offences and member information, subject
  to the Constitution's own banking and no-government-finance qualifications.
- **Current central statute:** the MSCS Act, 2002 as amended in 2023 and the
  amended rules govern multi-State societies. The 2023 architecture includes a
  Co-operative Election Authority, Co-operative Ombudsman, Co-operative
  Information Officer, concurrent-audit controls and the Cooperative
  Rehabilitation, Reconstruction and Development Fund.
- **Appointments and institutions:** the Central Government appoints the
  Central Registrar under section 4 and constitutes/appoints the statutory
  central election, ombudsman and other mechanisms under the amended Act.
  State Registrars derive authority from State Acts. These offices are not the
  Election Commission of India, RBI or an operating cooperative.
- **Banking overlay:** registration under cooperative law and banking
  regulation are separate. RBI/Banking Regulation Act supervision applies to
  banking functions; NABARD and financing institutions have distinct roles.
  A PACS is not automatically a banking company for every legal purpose.
- **Status tests:** Daman Singh addresses the statutory character of cooperative
  membership; Thalappalam holds that registration and ordinary regulatory
  control alone do not automatically make a society an RTI public authority.
  Article 12 and Article 226 tests remain fact-sensitive.
- **Current policy control:** National Cooperation Policy 2025, launched
  24 July 2025, is a policy framework for governance, professionalisation,
  digitalisation, market linkages, finance, inclusion and sustainability. It
  does not transfer Entry 32 competence or erase State-law variation.
- **PYQ firewall:** adjacent 2020 DCCB, 2021 UCB and 2023 cooperative-production
  objective demands are retained as cross-owned banking/agriculture routes.
  No direct Polity Mains PYQ is fabricated.""",
    40: """### Semantic-completeness ownership and PYQ control

- **Constitutional status:** Part XVII contains Articles 343-351. Article 343
  makes Hindi in Devanagari script the official language of the Union and uses
  the international form of Indian numerals. The Constitution does not declare
  any national language.
- **Union settlement:** Article 343(2)'s initial fifteen-year continuation of
  English was followed by Parliament's Official Languages Act, 1963. Section 3,
  substituted in 1967, permits English to continue in addition to Hindi and
  protects Union communication with non-Hindi States through its provisos and
  section 3(5) consent lock.
- **Commission/committee distinction:** Article 344 provides the constitutional
  Commission and parliamentary committee sequence. The continuing Committee of
  Parliament on Official Language is the thirty-member statutory committee
  under section 4 of the 1963 Act, not a permanent Article 344 Commission.
- **Current institutional snapshot, checked 5 September 2026:** the official
  Committee portal identifies Union Home Minister Amit Shah as Chairperson and
  displays the thirteenth part of its report. Recommendations or Presidential
  directions cannot override section 3.
- **State variation:** Article 345 permits a State legislature to adopt one or
  more languages in use in the State or Hindi. Articles 346-347 govern
  intergovernmental communication and recognition of a language spoken by a
  substantial section. No single State-language template can be universalised.
- **Courts and authoritative texts:** Article 348 retains English for Supreme
  Court and High Court proceedings and authoritative legal texts until valid
  legal change. Article 348(2) and section 7 allow bounded High Court use of
  Hindi/a State official language with prior Presidential consent and an
  authoritative English translation of judgments, decrees and orders.
- **Citizen/minority/development provisions:** Article 350 protects grievance
  representation in any language used in the Union or State; Articles 350A and
  350B concern primary-stage mother-tongue facilities and the Special Officer
  for linguistic minorities; Article 351 directs development of Hindi while
  drawing on India's composite culture.
- **Rules:** the Official Languages (Use for Official Purposes of the Union)
  Rules, 1976 are displayed by the Department as amended in 1987, 2007 and
  2011. They divide administration into Regions A/B/C and expressly exclude
  Tamil Nadu from their territorial extent. Rules do not amend Part XVII.
- **Separate categories:** the Eighth Schedule contains twenty-two languages.
  Scheduled status does not itself make a language official everywhere.
  Classical-language status and the three-language formula are separate
  executive/education-policy categories; October 2024 recognition brought the
  then official classical-language count to eleven.
- **Case/PYQ firewall:** Gujarat University, D.A.V. College and Associated
  Management control competence, minority safeguards and educational choice;
  none declares a national language. The routed 2024 Prelims constitutional-
  amendment demand is retained; current proposals are not treated as enacted.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    36: (
        [
            "https://dopt.gov.in/sites/default/files/RTI%20Act%202005%20%28updated%20as%20on%2018-11-2025%29.pdf",
            "https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf",
            "https://dopt.gov.in/sites/default/files/RTI%20Rules%202019.pdf",
            "https://cic.gov.in/cic-profile",
            "https://cic.gov.in/cicrg",
            "https://api.sci.gov.in/jonew/judis/38918.pdf",
            "https://api.sci.gov.in/jonew/judis/38344.pdf",
            "https://api.sci.gov.in/jonew/judis/43192.pdf",
            "https://api.sci.gov.in/supremecourt/2009/36624/36624_2009_1_1502_18247_Judgement_13-Nov-2019.pdf",
        ],
        "Rechecked 2026-09-05: the DoPT Act updated 18 November 2025, "
        "MeitY commencement notification, 2019 service-condition Rules, CIC "
        "present roster and controlling judgments remain current. Raj Kumar "
        "Goyal is Chief Information Commissioner; SIC rosters remain State-specific.",
    ),
    37: (
        [
            "https://www.indiacode.nic.in/handle/123456789/2068",
            "https://www.indiacode.nic.in/handle/123456789/2258",
            "https://cvc.gov.in/",
            "https://cbi.gov.in/",
            "https://dopt.gov.in/",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2215352&reg=3&lang=1",
            "https://api.sci.gov.in/supremecourt/2018/15968/15968_2018_Judgement_15-Feb-2019.pdf",
            "https://api.sci.gov.in/supremecourt/2025/6153/6153_2025_2_2_64992_Order_09-Oct-2025.pdf",
        ],
        "Rechecked 2026-09-05: the CVC Act, DSPE Act, 2021 Director-tenure "
        "amendment, CVC/CBI/DoPT material and Supreme Court consent cases remain "
        "operative. A S Rajeev is acting CVC, Praveen Vashista is Vigilance "
        "Commissioner and Praveen Sood's dated CBI term runs to 24 May 2027.",
    ),
    38: (
        [
            "https://www.indiacode.nic.in/",
            "https://lokpal.gov.in/",
            "https://lokpal.gov.in/about/chairperson",
            "https://lokpal.gov.in/about/present-members",
            "https://dopt.gov.in/lokpal-list?page=1",
            "https://api.sci.gov.in/jonew/judis/44396.pdf",
            "https://api.sci.gov.in/supremecourt/2025/9527/9527_2025_2_301_59727_Order_20-Feb-2025.pdf",
        ],
        "Rechecked 2026-09-05: the 2013 Act, 2016 amendment, Complaint Rules, "
        "official Lokpal roster and the Supreme Court's 20 February 2025 stay "
        "remain current. Justice A. M. Khanwilkar and six listed Members are "
        "recorded as a dated snapshot; State Lokayukta design remains variable.",
    ),
    39: (
        [
            "https://legislative.gov.in/en/constitution-of-india",
            "https://crcs.gov.in/constitutional_provisions",
            "https://crcs.gov.in/",
            "https://www.cooperation.gov.in/en/node/2333",
            "https://www.cooperation.gov.in/",
            "https://www.rbi.org.in/",
            "https://www.nabard.org/",
        ],
        "Rechecked 2026-09-05: the constitutional text, Rajendra N. Shah "
        "federal limit, MSCS Act/2023 amendment and rules, CRCS institutions "
        "and National Cooperation Policy 2025 remain current. Policy and Union "
        "administration do not displace Entry 32 or State Registrars.",
    ),
    40: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://rajbhasha.gov.in/en/official-languages-act-1963",
            "https://rajbhasha.gov.in/en/official-language-rules-1976",
            "https://samiti.rajbhasha.gov.in/",
            "https://rajbhasha.gov.in/en/ol_clause",
        ],
        "Rechecked 2026-09-05: Part XVII, the 1963 Act as amended, the 1976 "
        "Rules displayed with amendments through 2011, twenty-two scheduled "
        "languages and the Committee portal's thirteenth report remain current. "
        "Amit Shah is the dated Committee Chairperson; India has no national language.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[Path, ...]]] = {
    36: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\06_Digital-Public-Infrastructure-and-Data-Governance.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\15_Transparency-RTI-and-Information-Sharing.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    37: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Lokpal-and-Lokayuktas.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\20_Anti-Corruption-Institutions.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\21_Protecting-Honest-Officials-and-Vigilance-Administration.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    38: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CVC-and-CBI.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\20_Anti-Corruption-Institutions.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\21_Protecting-Honest-Officials-and-Vigilance-Administration.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    39: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Panchayati-Raj.md",
                "upsc-ai-kit\\knowledge\\Economy\\basic\\13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    40: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\High-Court.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
}

PANEL_ADDITIONS: dict[int, dict[str, str]] = {
    36: {
        "CIC and SIC composition and appointment": (
            "\n\nCURRENT CENTRAL ROSTER: 5 SEPTEMBER 2026\n"
            "Chief: Raj Kumar Goyal.\n"
            "ICs: Anandi Ramalingam | Vinod Kumar Tiwari | Surendra Singh Meena\n"
            "| Ashutosh Chaturvedi | Swagat Das | Sudha Rani Relangi | P. R. Ramesh\n"
            "| Khushwant Singh Sethi | Jaya Varma Sinha | Sanjeev Kumar Jindal.\n"
            "SIC incumbency is State-specific; never infer one national State roster."
        ),
        "Personal information after the DPDP substitution": (
            "\n\nCURRENT-LAW CONTROL: 5 SEPTEMBER 2026\n"
            "Section 44(3) substitution has operated since 13 November 2025.\n"
            "The shorter clause is in force; section 8(2), severability, appeal\n"
            "and judicial review survive. No final constitutional merits ruling is asserted."
        ),
    },
    37: {
        "CVC composition, appointment and tenure": (
            "\n\nCURRENT LEADERSHIP: 5 SEPTEMBER 2026\n"
            "A S Rajeev: acting Central Vigilance Commissioner from 3 August 2026.\n"
            "Praveen Vashista: Vigilance Commissioner.\n"
            "Acting charge does not alter the statutory appointment architecture."
        ),
        "CBI Director appointment, tenure and transfer safeguards": (
            "\n\nCURRENT DIRECTOR: 5 SEPTEMBER 2026\n"
            "Praveen Sood's dated extension runs through 24 May 2027.\n"
            "A one-year extension under the amended law is not an automatic five-year term."
        ),
    },
    38: {
        "Composition and eligibility": (
            "\n\nCURRENT ROSTER: 5 SEPTEMBER 2026\n"
            "Chairperson: Justice Ajay Manikrao Khanwilkar.\n"
            "Judicial Members: Justice L. Narayana Swamy | Justice Sanjay Yadav\n"
            "| Justice Ritu Raj Awasthi.\n"
            "Members: Sushil Chandra | Pankaj Kumar | Ajay Tirkey.\n"
            "No occupant is inferred for an unfilled statutory seat."
        ),
        "Cases and current legal controls": (
            "\n\nPENDING-JURISDICTION CONTROL\n"
            "The Supreme Court's 20 February 2025 interim order stayed the Lokpal's\n"
            "High Court-judge jurisdiction order. Do not convert the stay into a final merits rule."
        ),
    },
    39: {
        "Ministry, Central Registrar and policy boundary": (
            "\n\nCURRENT POLICY CONTROL: 5 SEPTEMBER 2026\n"
            "National Cooperation Policy 2025 was launched on 24 July 2025.\n"
            "Its governance, professionalisation, digital, market, finance and\n"
            "inclusion programme is policy; Entry 32 and State-law variation remain."
        ),
    },
    40: {
        "Part XVII settlement: official language without a national language": (
            "\n\nCURRENT LAW: 5 SEPTEMBER 2026\n"
            "No constitutional national language exists. Hindi is the Union official\n"
            "language; English continues by statute in addition to Hindi."
        ),
        "Eighth Schedule and separate policy categories": (
            "\n\nCURRENT INSTITUTIONAL SNAPSHOT\n"
            "Eighth Schedule: 22 languages. Rules portal: amendments through 2011.\n"
            "Committee portal: Amit Shah as Chairperson and thirteenth report displayed.\n"
            "Committee recommendations cannot override section 3's statutory safeguards."
        ),
    },
}


def _topic_map(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    topics_value = raw["topics"]
    if isinstance(topics_value, list):
        return {row["topic_key"]: row for row in topics_value}
    return topics_value


def _repair_current_law(topic_number: int, text: str) -> str:
    for old in (
        "21 July 2026",
        "21 Jul 2026",
        "24 August 2026",
        "25 August 2026",
        "28 August 2026",
        "31 August 2026",
    ):
        text = text.replace(old, "5 September 2026")
    if topic_number == 36:
        text = text.replace(
            "Officeholders and backlog totals are not frozen.",
            "The dated central roster is recorded; SIC rosters and backlog totals "
            "remain variable and are not generalised.",
        )
    if topic_number == 37:
        text = text.replace(
            "Officeholders, consent-State counts and live caseloads are not frozen.",
            "The dated CVC and CBI leadership is recorded; consent-State counts "
            "and live caseloads remain variable.",
        )
    if topic_number == 38:
        text = text.replace(
            "officeholders and case-output totals are not frozen.",
            "the dated Lokpal roster is recorded; case-output totals are not frozen.",
        )
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    source_dates = {36: "2026-08-24", 37: "2026-08-24", 38: "2026-08-25",
                    39: "2026-08-25", 40: "2026-08-25"}
    for number in range(36, 41):
        key = f"polity-{number:02d}"
        path = directory / f"{key}-{source_dates[number]}-sequential.json"
        source = _topic_map(json.loads(path.read_text(encoding="utf-8")))[key]
        panels = []
        additions = PANEL_ADDITIONS[number]
        found: set[str] = set()
        for panel in source["panels"]:
            body = _repair_current_law(number, panel["full_text"])
            if panel["title"] in additions:
                body = body.rstrip() + additions[panel["title"]]
                found.add(panel["title"])
            panels.append(
                (
                    panel["title"],
                    panel["structural_type"],
                    body,
                    panel["source_references"],
                )
            )
        if found != set(additions):
            missing = sorted(set(additions) - found)
            raise ValueError(f"{key}: current-control panels not found: {missing}")
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
    if topic_key in {f"polity-{number:02d}" for number in range(1, 41)}:
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
    rows = manifest["topics"][:40]
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
    expected = [f"polity-{number:02d}" for number in range(1, 41)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-40 changed or are out of order.")
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
    engine.base.WORKFLOW = "polity-36-40-hostile-semantic-immutable-successor"
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
