"""Extend the hostile Polity deep-review workflow to topics 41-45."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_36_40_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST
PYQ_LEDGERS = deep.PYQ_LEDGERS

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    41: (
        "Keep Articles 308-314 service law distinct from the Articles 315-323 "
        "Public Service Commission institution.",
        "Treat pleasure, Article 311 procedure, civil-post status, All-India "
        "Services, tribunals, vigilance and reform as connected but separate tests.",
        "AIJS remains uncreated; Mission Karmayogi is operative policy, while "
        "vacancies, lateral-entry advertisements and platform totals remain date-sensitive.",
    ),
    42: (
        "Apply the Tenth Schedule's exact member-specific grounds, merger defence "
        "and paragraph 5 presiding-officer exemption without reviving the deleted split.",
        "Separate the political party, legislature party, whip, Speaker, Election "
        "Commission, resignation and judicial-review tracks.",
        "Subhash Desai remains controlling; the Nabam Rebia reconsideration remains "
        "unresolved in the official Supreme Court material located through 5 September 2026.",
    ),
    43: (
        "Separate Section 29A registration, Symbols Order recognition, Tenth "
        "Schedule discipline, finance disclosure and candidate regulation.",
        "Do not convert the ECI's bounded registration/symbol powers into a general "
        "power to control internal democracy or deregister parties on the merits.",
        "The 2024 electoral-bonds judgment remains controlling; recognition lists, "
        "party counts, officeholders and election-specific symbol concessions are not frozen.",
    ),
    44: (
        "Treat pressure group as an analytical role, not a single legal form, and "
        "keep parties, movements, NGOs, unions and lobbyists distinct.",
        "Apply Articles 19, protest regulation, PIL, consultation, FCRA and entity "
        "law through separate legal routes rather than inventing a right to lobby.",
        "The 2025 FCRA Rules changes are procedural; India still has no comprehensive "
        "general lobbying-registration or lobbying-disclosure statute.",
    ),
    45: (
        "Keep national integration as constitutional inclusion and accommodation, "
        "not cultural uniformity or an unrestricted security claim.",
        "Separate Article 51 values, Article 73 executive competence, Union List "
        "subjects, Article 253 implementation and domestic-law enforceability.",
        "The 4 August 2026 parliamentary reply still identifies 23 September 2013 "
        "as the latest NIC meeting; current foreign-policy practice remains policy, not law.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    41: """### Semantic-completeness ownership and PYQ control

- **Constitutional boundary:** Part XIV Articles 308-314 govern services under
  the Union and States; Articles 315-323 separately govern UPSC, SPSCs and the
  Joint PSC. Public Services owns the service relationship, while Polity 28
  owns the constitutional commission.
- **Article 309 hierarchy:** the appropriate legislature may regulate
  recruitment and service conditions. Until legislation operates, the
  President or Governor may make rules. Executive instructions cannot override
  the Constitution, a statute or valid statutory rules.
- **Pleasure and protection:** Article 310's pleasure is constitutionally
  fettered by Article 311, equality, natural justice and judicial review.
  Article 311 protects members of civil services and holders of civil posts,
  not defence personnel or every employee of every public body.
- **Article 311 mechanics:** dismissal/removal cannot be by an authority
  subordinate to the appointing authority; dismissal, removal or reduction in
  rank ordinarily requires inquiry and reasonable opportunity. The three
  inquiry exceptions are conviction, recorded impracticability and
  President/Governor satisfaction concerning security of the State.
- **Case controls:** Parshotam Lal Dhingra distinguishes punitive foundation
  from non-punitive termination; Tulsiram Patel controls the three exceptions;
  ECIL v B. Karunakar requires supply of an adverse inquiry report subject to
  prejudice; T.S.R. Subramanian requires written directions and institutional
  tenure safeguards.
- **AIS federal design:** Article 312 requires a Rajya Sabha resolution
  supported by not less than two-thirds of members present and voting before
  Parliament creates a new All-India Service. IAS, IPS and Indian Forest
  Service remain the existing AIS; Centre-State control is dual rather than
  exclusively Union or State.
- **AIJS status, checked 5 September 2026:** Article 312 permits an
  All-India Judicial Service not including a post inferior to district judge,
  but no creating law or recruitment notification was located. Consultation
  and advocacy are not an existing service.
- **Reform boundary:** Mission Karmayogi/iGOT and the Capacity Building
  Commission remain operative capacity-building architecture. Lateral entry,
  fixed tenure, cadre deputation and performance systems must be stated with
  the applicable rule and date; advertisement, vacancy and dashboard totals
  are deliberately unfrozen.
- **Remedy tracks:** departmental discipline, CVC/CVO vigilance, criminal
  investigation, CAT adjudication and High Court judicial review are distinct.
  L. Chandra Kumar preserves Articles 226/227 review over tribunal decisions.
- **PYQ firewall:** the verified adjacent 2020 civil-services-reform demand is
  retained as supporting application. PSC recruitment, governance reform,
  ethics and tribunal procedure remain cross-owned where their principal
  demand lies.""",
    42: """### Semantic-completeness ownership and PYQ control

- **Text and amendments:** the 52nd Amendment Act, 1985 inserted the Tenth
  Schedule and amended Articles 101, 102, 190 and 191. The 91st Amendment Act,
  2003 deleted the one-third split defence, retained the paragraph 4 merger
  route and added ministry-size and office bars.
- **Grounds:** a party member may be disqualified for voluntarily giving up
  membership or voting/abstaining contrary to a direction without prior
  permission and without condonation within fifteen days. Conduct may prove
  voluntary giving up; formal resignation is not indispensable.
- **Member types:** an independent member is disqualified on joining any
  political party. A nominated member may join within six months of taking the
  seat but is disqualified for joining after that period.
- **Merger and exemption:** paragraph 4 requires merger of the original
  political party and agreement by not less than two-thirds of the legislature
  party. Paragraph 5 narrowly protects a presiding officer who gives up party
  membership on election to the chair. The deleted split cannot be revived.
- **Decision and review:** paragraph 6 assigns the question to the Speaker or
  Chairman. Kihoto Hollohan treats that officer as a tribunal subject to
  judicial review; Rajendra Singh Rana permits review of disabling inaction;
  Keisham Meghachandra states an ordinary three-month norm and recommends an
  independent tribunal without enacting one.
- **Party/whip control:** Subhash Desai (2023) requires recognition of the whip
  and leader appointed by the political party, not merely a legislature-party
  faction, and requires party identity to be assessed through the party
  constitution and organisation rather than legislator headcount alone.
- **Parallel tracks:** a symbol dispute before the ECI and disqualification
  proceedings before the Speaker perform different functions and may proceed
  independently. Resignation does not erase antecedent disqualifying conduct.
- **Pending doctrine, checked 5 September 2026:** the Nabam Rebia question
  concerning a Speaker facing removal notice remains referred for larger-bench
  reconsideration in the latest official Supreme Court material located. No
  later merits disposition is asserted.
- **Reform status:** limiting whips, imposing a statutory deadline or shifting
  adjudication to an independent tribunal remain proposals, not Tenth Schedule
  text. The law disqualifies membership; it does not criminalise defection.
- **PYQ firewall:** the verified 2022 nominated-member and 2025 political-party
  objective demands are owned here. No direct Mains PYQ is fabricated.""",
    43: """### Semantic-completeness ownership and PYQ control

- **Layered legal identity:** Section 29A of the Representation of the People
  Act, 1951 governs registration; the Election Symbols (Reservation and
  Allotment) Order, 1968 governs recognition and symbols; the Tenth Schedule
  governs legislative defection. These are not interchangeable.
- **Registration:** an association of Indian citizens applies to the ECI and
  must carry the statutory constitutional-allegiance declaration. Registration
  does not itself confer National or State party recognition.
- **Bounded deregistration:** Indian National Congress (I) v Institute of
  Social Welfare (2002) treats the ECI's Section 29A function as quasi-judicial
  and rejects a general merits-based deregistration power, while preserving
  narrow fraud, non-compliance and unlawful-object situations recognised in
  the judgment.
- **Recognition and symbols:** the Symbols Order supplies performance criteria,
  reserved/free symbols and paragraph 15 faction adjudication. Sadiq Ali
  sustains the ECI's party-identity jurisdiction. Recognition lists and
  election-specific concessions are date-sensitive and deliberately unfrozen.
- **Finance:** Sections 29B-29C, the Companies Act, Income-tax law, FCRA and ECI
  disclosure directions operate through different tests. A contribution
  threshold, foreign-source rule or candidate-expenditure ceiling must not be
  transferred to another legal route.
- **Electoral bonds, checked 5 September 2026:** Association for Democratic
  Reforms v Union of India, 2024 INSC 113, remains the controlling official
  judgment invalidating the scheme and enabling amendments on Article
  19(1)(a), proportionality and corporate-funding grounds. It did not enact a
  complete new campaign-finance code.
- **Criminalisation:** ADR (2002) and PUCL (2003) ground candidate disclosure;
  Lily Thomas removes the former sitting-member protection after conviction;
  Rambabu Singh Thakur requires party publication of criminal antecedents and
  reasons for selection. Disclosure is not pre-conviction disqualification.
- **Internal democracy:** no comprehensive enacted party-democracy code
  controls leadership succession, membership and candidate selection. ECI,
  committee and Law Commission proposals remain proposals.
- **System analysis:** national/regional behaviour varies with organisation,
  territorial base and position in Union or State power. Coalition,
  centralisation and autonomy claims require evidence and qualification.
- **PYQ firewall:** the 2022 GS-II centralisation/autonomy demand is shared
  with Federal System, while the party-system incentive analysis is owned
  here. Recognition and finance questions retain exact legal-source labels.""",
    44: """### Semantic-completeness ownership and PYQ control

- **Analytical category:** a pressure group seeks to influence public policy
  without ordinarily seeking governmental office. Party, movement, NGO,
  trade union, professional body and lobbyist are overlapping but non-synonymous
  categories governed by their own legal forms.
- **Constitutional channels:** Articles 19(1)(a), 19(1)(b) and 19(1)(c)
  support speech, peaceful assembly and association subject to Articles
  19(2)-19(4). Articles 32 and 226 supply remedies for enforceable rights, not
  a general licence to convert advocacy into judicial policy-making.
- **Association and protest cases:** Damyanti Naranga protects associational
  composition; Ramlila Maidan and Mazdoor Kisan Shakti Sangathan require
  rights-compatible protest regulation; Amit Sahni rejects indefinite
  occupation of public ways. Peaceful protest, strike, violence and obstruction
  remain legally distinct.
- **Typology:** associational, non-associational, institutional and anomic
  categories describe modes of interest articulation. Anomic does not mean a
  stable armed organisation, and a statutory regulator is not automatically a
  voluntary professional pressure group.
- **Methods and effects:** consultation, expertise, lobbying, petition,
  campaign, collective bargaining, protest, litigation and electoral signalling
  influence different policy stages. Access or visibility does not prove
  adoption, implementation or representative legitimacy.
- **FCRA boundary, checked 5 September 2026:** the FCRA, 2010 and Rules govern
  foreign contribution through registration/prior permission, designated
  banking, use and reporting controls. The 2025 Rules changes are procedural;
  FCRA is not a lobbying-registration statute and must not be presented as one.
- **NGO Darpan:** the portal supplies identification and information functions
  for voluntary organisations in specified government interfaces. It does not
  create one legal form for all NGOs or a general licence to lobby.
- **Lobbying status:** no comprehensive Indian statute requiring general
  registration and disclosure of lobbyists was located. Bribery, election,
  procurement, company, confidentiality and sectoral laws still apply.
- **Democratic balance:** pressure groups can add expertise, participation and
  minority voice, but unequal resources, capture, opaque funding, revolving
  doors, misinformation and weak internal representation require transparent,
  plural and reasoned consultation.
- **PYQ firewall:** the verified 2019 farmer-group, 2021 business-association
  and 2025 environmental-pressure-group Mains demands are owned here with
  named evidence and explicit representativeness limits.""",
    45: """### Semantic-completeness ownership and PYQ control

- **Integration concept:** national integration means equal citizenship,
  constitutional loyalty, accommodation and peaceful membership across
  diversity. It is not cultural uniformity, majoritarian assimilation or a
  free-standing authority to suppress dissent.
- **Constitutional spine:** the Preamble's fraternity, dignity, unity and
  integrity operate with equality, freedoms, minority rights, DPSPs,
  Fundamental Duties, federalism, asymmetry and local participation.
  S. R. Bommai preserves federalism and secularism as basic features.
- **Security boundary:** Articles 355 and 356, public-order law and security
  statutes remain subject to legality, necessity, proportionality, federal
  limits and judicial review. Identity, grievance, regionalism, communalism,
  separatism and violence require distinct diagnosis.
- **NIC status, checked 5 September 2026:** the National Integration Council is
  extra-constitutional, non-statutory and advisory. The official Lok Sabha
  reply dated 4 August 2026 identifies 23 September 2013 as its latest meeting;
  no later meeting or formal abolition is asserted.
- **Foreign-affairs competence:** Article 51 supplies non-justiciable DPSP
  values. Article 73 extends Union executive power within constitutional
  limits; Article 246 and Union List Entries 10-21 allocate core foreign
  affairs subjects; Article 253 permits Parliament to implement international
  obligations notwithstanding ordinary federal distribution.
- **Treaty/domestic-law chain:** executive conclusion of an international
  commitment does not automatically amend domestic law or override rights.
  Existing law may permit implementation; legislation is needed where law or
  rights must change, and constitutional amendment is required where the
  Constitution itself must change.
- **Case controls:** Berubari requires constitutional amendment for cession of
  Indian territory; Maganbhai distinguishes executable boundary settlement
  from legal change; Jolly George rejects automatic treaty override;
  Gramophone favours harmony absent conflict; Vishaka permits consistent
  international norms to fill a domestic-law vacuum.
- **Policy boundary:** non-alignment, strategic autonomy, neighbourhood policy,
  multilateral reform and Global South advocacy are executive-policy
  orientations rather than self-executing constitutional rules. The MEA
  Annual Report 2024-25 is a dated policy source, not a legal code.
- **Integration/foreign-policy link:** inclusive institutions strengthen
  diplomatic legitimacy and resilience; foreign policy can affect domestic
  cohesion through borders, diaspora, migration, security and development.
  The connection does not merge the two legal fields.
- **PYQ firewall:** adjacent constitutional, federal, security and
  international-relations PYQs are routed to their principal owners. This
  topic retains only the integration/constitutional-competence bridge and does
  not fabricate a direct question.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    41: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://dopt.gov.in/sites/default/files/Revised_AIS_Rule_Vol_I_Rule_01.pdf",
            "https://cbc.gov.in/index.php/about-cbc",
            "https://igotkarmayogi.gov.in/",
            "https://api.sci.gov.in/jonew/judis/40943.pdf",
            "https://doj.gov.in/static/uploads/2025/11/0420d9aef08a41515f6f92ac586189fe.pdf",
        ],
        "Rechecked 2026-09-05: Part XIV, AIS rules, T.S.R. Subramanian, "
        "Mission Karmayogi/CBC and the official AIJS consultation record remain "
        "consistent with the owner. AIJS is not created; volatile staffing and "
        "advertisement metrics are not frozen.",
    ),
    42: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.api.sci.gov.in/supremecourt/2022/20234/20234_2022_1_1502_44512_Judgement_11-May-2023.pdf",
            "https://api.sci.gov.in/supremecourt/2022/20234/20234_2022_1_1502_44512_Order_11-May-2023.pdf",
            "https://sansad.in/",
        ],
        "Rechecked 2026-09-05: the Tenth Schedule and 52nd/91st Amendment "
        "architecture remain unchanged. Subhash Desai remains controlling and "
        "the Nabam Rebia reconsideration is not presented as decided.",
    ),
    43: (
        [
            "https://www.eci.gov.in/political-party-registration",
            "https://old.eci.gov.in/files/file/4303-the-election-symbols-reservation-and-allotmentorder-1968/",
            "https://www.indiacode.nic.in/",
            "https://api.sci.gov.in/supremecourt/2017/27935/27935_2017_1_1501_50573_Judgement_15-Feb-2024.pdf",
        ],
        "Rechecked 2026-09-05: Section 29A registration, the Symbols Order and "
        "the 2024 electoral-bonds judgment remain authoritative. Current party "
        "recognition lists and election-specific symbol concessions are not frozen.",
    ),
    44: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://fcraonline.nic.in/Home/Notices.aspx?divName=A",
            "https://www.mha.gov.in/en/divisionofmha/foreigners-division/online-fcra-services",
            "https://ngodarpan.gov.in/",
            "https://api.sci.gov.in/judis/17189.pdf",
            "https://api.sci.gov.in/supremecourt/2025/41929/41929_2025_1_1501%20_66095_Judgement_18-Nov-2025.pdf",
        ],
        "Rechecked 2026-09-05: Articles 19, the protest-rights line, FCRA 2010 "
        "and the procedural 2025 Rules changes remain current. No comprehensive "
        "general lobbying-registration/disclosure statute was located.",
    ),
    45: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.mha.gov.in/MHA1/Par2017/pdfs/par2026-pdfs/LS04082026/2720.pdf",
            "https://www.mea.gov.in/images/CPV/140725MEAAnnualReport2024English.pdf",
            "https://www.mea.gov.in/annualreports",
            "https://www.sci.gov.in/",
        ],
        "Rechecked 2026-09-05: Articles 51, 73, 246 and 253 and the treaty-case "
        "line remain controlling. The 4 August 2026 Lok Sabha reply retains "
        "23 September 2013 as the latest NIC meeting; MEA policy remains dated policy.",
    ),
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[Path, ...]]] = {
    41: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\UPSC-and-SPSC.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Administrative-Tribunals.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\CVC-and-CBI.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\09_Civil-Services-and-Mission-Karmayogi.md",
                "upsc-ai-kit\\knowledge\\Ethics\\basic\\09_Public-Service-Values-Status-and-Ethical-Dilemmas.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    42: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\State-Legislature.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Amendment-and-Basic-Structure.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    43: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Election-Commission.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Anti-Defection-Law.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    44: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Supreme-Court.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Political-Parties.md",
                "upsc-ai-kit\\knowledge\\Governance\\basic\\08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
    45: {
        "cross": tuple(
            deep.repo(path)
            for path in (
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Preamble.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Directive-Principles.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Duties.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Centre-State-Relations.md",
                "upsc-ai-kit\\knowledge\\Polity\\basic\\Special-Provisions.md",
                "upsc-ai-kit\\knowledge\\International-Relations\\basic\\01_Foreign-Policy-Foundations-and-Strategic-Autonomy.md",
            )
        ),
        "pyq": PYQ_LEDGERS,
    },
}

PANEL_ADDITIONS: dict[int, dict[str, str]] = {
    41: {
        "UPSC traps, supporting PYQ and qualified answer synthesis": (
            "\n\nCURRENT CONTROL: 5 SEPTEMBER 2026\n"
            "AIJS remains constitutionally enabled but uncreated.\n"
            "Mission Karmayogi/CBC/iGOT is operative reform architecture;\n"
            "vacancies, lateral-entry advertisements and dashboard totals remain unfrozen."
        ),
    },
    42: {
        "Delay, judicial remedies and current doctrinal control": (
            "\n\nCURRENT CASE CONTROL\n"
            "Subhash Desai (2023) remains controlling. Nabam Rebia (2016) remains\n"
            "referred for larger-bench reconsideration; no later merits result is asserted.\n"
            "Status rechecked on 5 September 2026."
        ),
    },
    43: {
        "Finance and the electoral-bonds constitutional reset": (
            "\n\nCURRENT LAW: 5 SEPTEMBER 2026\n"
            "ADR, 2024 INSC 113, remains the controlling electoral-bonds judgment.\n"
            "It invalidated the scheme and enabling amendments; it did not enact\n"
            "a complete replacement campaign-finance code."
        ),
    },
    44: {
        "FCRA and lobbying: separate legal questions": (
            "\n\nCURRENT LAW: 5 SEPTEMBER 2026\n"
            "The 2025 FCRA Rules changes are procedural application controls.\n"
            "FCRA is not a lobbying statute; no comprehensive general Indian\n"
            "lobbying-registration or lobbying-disclosure law was located."
        ),
    },
    45: {
        "Constitutional belonging without uniformity": (
            "\n\nVERDICT: Equal citizenship secures diverse identities within one constitutional order."
        ),
        "Preamble, rights, DPSPs and duties": (
            "\n\nVERDICT: Fraternity needs liberty, equality, minority protection and social justice."
        ),
        "Federal accommodation": (
            "\n\nVERDICT: Federal accommodation converts difference into constitutional bargaining."
        ),
        "Language and minority safeguards": (
            "\n\nVERDICT: Language unity rests on protected plurality, not forced uniformity."
        ),
        "Challenge-response ladder": (
            "\n\nVERDICT: Diagnosis must precede dialogue, development and proportionate security."
        ),
        "Emergency and security limits": (
            "\n\nVERDICT: Exceptional power needs legality, necessity, proportionality and review."
        ),
        "National Integration Council": (
            "\n\nCURRENT STATUS: 5 SEPTEMBER 2026\n"
            "The official Lok Sabha reply dated 4 August 2026 identifies\n"
            "23 September 2013 as the latest NIC meeting. No later meeting or\n"
            "formal abolition is asserted.\n\n"
            "VERDICT: Consultation needs regular meetings and action-taken accountability."
        ),
        "Foreign-affairs competence": (
            "\n\nVERDICT: Article 51 gives values; Articles 73, 246 and 253 allocate authority."
        ),
        "International-to-domestic chain": (
            "\n\nVERDICT: International commitments need the constitutionally required domestic route."
        ),
        "Treaty case doctrine": (
            "\n\nVERDICT: Treaties cannot silently amend rights, statutes or constitutional territory."
        ),
        "Non-alignment to strategic autonomy": (
            "\n\nVERDICT: Strategic autonomy means diversified choice, not neutrality or isolation."
        ),
        "UPSC synthesis and PYQ map": (
            "\n\nVERDICT: Inclusive legitimacy at home strengthens accountable strategic choice abroad."
        ),
    },
}


def _topic_map(raw: dict[str, Any]) -> dict[str, dict[str, Any]]:
    topics_value = raw["topics"]
    if isinstance(topics_value, list):
        return {row["topic_key"]: row for row in topics_value}
    return topics_value


def _repair_current_law(topic_number: int, text: str) -> str:
    del topic_number
    for old in (
        "25 August 2026",
        "25 Aug 2026",
        "28 August 2026",
        "28 Aug 2026",
        "31 August 2026",
    ):
        text = text.replace(old, "5 September 2026")
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    for number in range(41, 46):
        key = f"polity-{number:02d}"
        path = directory / f"{key}-2026-08-25-sequential.json"
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
    if topic_key in {f"polity-{number:02d}" for number in range(1, 46)}:
        _engine._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = _engine.base.basic_mcq_area(repaired)
    keys = re.findall(r"(?im)^\*\*Answer:\s*([A-D])(?:\.)?\*\*", area)
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
    rows = manifest["topics"][:45]
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
    expected = [f"polity-{number:02d}" for number in range(1, 46)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-45 changed or are out of order.")
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
    engine.base.WORKFLOW = "polity-41-45-hostile-semantic-immutable-successor"
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
