"""Extend the hostile Polity deep-review workflow to topics 06-10."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import regenerate_polity_01_05_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    6: (
        "Separate the commencement settlement in Articles 5-11 from the continuing "
        "statutory regime under the Citizenship Act, 1955, and state each migration, "
        "birth, descent, registration, naturalisation, loss, Section 6A, OCI and "
        "Section 6B rule with its exact trigger and date.",
        "Article 9 is confined to citizenship by virtue of Articles 5, 6 or 8; the "
        "present no-dual-citizenship position also depends on Section 9. OCI is a "
        "statutory card, while the CAA and the 2025 immigration exemption use "
        "different cut-offs and produce different legal consequences.",
        "Current procedure must follow the 2024 Rules and the 19 August 2026 "
        "Collector-route notifications. Section 6A remains valid under the 17 "
        "October 2024 majority; no unlocated final CAA judgment may be invented.",
    ),
    7: (
        "Treat Part III as a system of beneficiaries, respondents, exact restriction "
        "grounds, positive duties, remedies and exceptional controls: Articles 12-35 "
        "must be mapped before doctrine or current cases are applied.",
        "Citizen-only and person-rights, Article 32 and wider Article 226, ordinary "
        "law under Article 13 and amendments under Article 368, Articles 358 and 359, "
        "and private reach versus State action are separate constitutional questions.",
        "Use current official judgments and notifications only: Electoral Bonds, "
        "Davinder Singh, Property Owners, phased DPDP commencement, Harish Rana and "
        "the pending Section 152 challenge each have a bounded proposition.",
    ),
    8: (
        "Article 37 makes Articles 36-51 non-justiciable but fundamental in governance; "
        "teach every directive, its amendment history and implementation mechanism "
        "before applying the non-textual socialistic/Gandhian/liberal taxonomy.",
        "The present FR-DPSP position is harmony, not blanket primacy. Original "
        "Article 31C survives only for genuine Article 39(b)/(c) laws against Articles "
        "14 and 19, with nexus and basic-structure review preserved.",
        "Current examples must be legally current: Property Owners controls Article "
        "31C, Rajendra N Shah limits Part IX-B but not Article 43B, and Uttarakhand's "
        "April 2026 Amendment Act supersedes the January Ordinance.",
    ),
    9: (
        "Part IVA contains the exact eleven duties in Article 51A: ten inserted by the "
        "42nd Amendment in 1976 and clause (k) by the 86th Amendment in 2002; the "
        "Swaran Singh Committee recommended eight, not the enacted ten.",
        "Fundamental Duties bind citizens, are non-justiciable and create no automatic "
        "offence. Legal consequences arise only through valid statutes, while courts "
        "may use duties as interpretive context subject to Fundamental Rights.",
        "Durga Dutt remains a pending proceeding on the located official record; its "
        "11 September 2024 order sought a legislative synopsis and did not make duties "
        "justiciable or convert reported oral observations into ratio.",
    ),
    10: (
        "Article 368 constituent power, the dual special majority, the exact federal "
        "proviso list, mandatory assent, no joint sitting and simple-majority changes "
        "outside Article 368 must precede the basic-structure doctrine.",
        "Case propositions must remain chronological and distinct: Shankari Prasad, "
        "Sajjan Singh, Golak Nath, the 24th Amendment, Kesavananda, Indira Gandhi, "
        "Minerva Mills, Waman Rao, Bommai, Coelho, NJAC and Anjum Kadari.",
        "Basic structure limits constitutional amendments, not ordinary statutes as a "
        "free-standing test. The 131st Bill was defeated; the 106th Amendment has "
        "commenced, while Article 334A still separates commencement from operation.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    6: """### Semantic-completeness ownership and PYQ control

- **Constitutional settlement:** Part II is Articles 5-11 and identifies citizens
  at commencement. Article 5 requires domicile plus birth, parental birth or five
  years' ordinary residence; Articles 6-7 use the exact 19 July 1948 and 1 March
  1947 migration divisions; Article 8 covers qualifying Indian-origin persons
  abroad registered by a diplomatic or consular representative.
- **Articles 9-11 precision:** Article 9 denies citizenship by virtue of Articles
  5, 6 or 8 after voluntary acquisition of foreign citizenship; Article 10
  continues citizenship subject to parliamentary law; Article 11 preserves
  Parliament's plenary citizenship power. Do not convert Article 9 alone into a
  complete permanent-code proposition.
- **Statutory architecture:** Citizenship Act, 1955 acquisition is by birth,
  descent, registration, naturalisation and incorporation of territory. Loss is
  by renunciation, termination and deprivation; deprivation is category-limited
  and cannot be described as a general executive cancellation power.
- **Section 6A:** retain the 1 January 1966 and 25 March 1971 bands, the ten-year
  electoral consequence for the middle cohort, the Assam-specific boundary and
  the 17 October 2024 four-to-one judgment upholding the provision, followed by
  implementation monitoring.
- **OCI and CAA:** OCI under Sections 7A-7D is not citizenship or a constitutional
  right. Section 6B/CAA covers six named communities from Afghanistan, Bangladesh
  and Pakistan entering on or before 31 December 2014, subject to statutory
  application and scrutiny; protected tribal/Inner Line areas remain excluded.
- **Current procedural control:** the 2024 Rules operationalised Section 6B.
  G.S.R. 742(E) and S.O. 4583(E), both 19 August 2026, move specified applications
  to the jurisdictional Collector and transfer pending files; they do not alter
  the statutory class or cut-off.
- **Immigration boundary:** the Immigration and Foreigners Act/Exemption Order,
  2025 concerns entry-document liability and uses a 31 December 2024 date for the
  notified exemption. It neither grants citizenship nor changes the CAA's 2014
  cut-off.
- **Four-ledger hostile audit:** constitutional text, indispensable statutory
  rules, textbook taxonomy and all routed 2018-2026 PYQs were checked for dates,
  categories, exceptions, proof documents, legal consequence and current status.
- **Verified PYQ ownership, 2018-2026:** direct 2021 Prelims Q89; 2018 Aadhaar
  citizenship-proof is retained only as a disclosed cross-topic route. No direct
  Mains question or unavailable official key is fabricated.""",
    7: """### Semantic-completeness ownership and PYQ control

- **Part III architecture:** Articles 12-13 define the State/law gateway;
  Articles 14-18 equality; 19-22 freedom and criminal-process safeguards; 23-24
  exploitation; 25-28 religion; 29-30 culture and education; Article 32 remedies;
  Articles 31A-31C and 33-35 are exact saving/competence controls.
- **Beneficiary and respondent:** Articles 15, 16, 19 and 29 are citizen-specific;
  Articles 14, 20, 21 and 25 protect persons; Article 30 speaks of minorities.
  Articles 15(2), 17, 23 and 24 have specified horizontal reach. Article 226 may
  reach public duty beyond Article 12 without rewriting the Article 12 test.
- **Equality and reservation:** reasonable classification, anti-arbitrariness,
  Articles 15(3)-(6), 16(4), 16(4A), 16(4B), 16(6), Indra Sawhney, M. Nagaraj,
  Jarnail Singh, Janhit Abhiyan and Davinder Singh must retain distinct holdings,
  evidence requirements and limits.
- **Freedoms and liberty:** quote the closed Article 19(2)-(6) grounds; distinguish
  Articles 20(1)-(3), Maneka's fair-just-reasonable procedure, Article 21A, and
  ordinary arrest from preventive detention. The uncommenced 44th-Amendment
  two-month text must not replace the operative three-month Article 22 ceiling.
- **Religion, minority rights and remedies:** preserve Article 25(2), Articles
  26-28, the distinct limbs of Articles 29-30, the five writs and the wider
  Article 226 jurisdiction. Articles 358 and 359 are not interchangeable, and
  Articles 20-21 cannot be included in an Article 359 order.
- **Current legal controls:** Electoral Bonds (2024 INSC 113), Davinder Singh
  (2024 INSC 562), Property Owners (2024 INSC 835), phased DPDP notifications
  G.S.R. 843(E)/846(E), Harish Rana (2026 INSC 222), and the 28 August 2025
  notice on BNS Section 152 are used only for their exact official propositions.
- **Four-ledger hostile audit:** every Article, beneficiary, restriction ground,
  doctrine, case, amendment, exception, remedy, emergency effect and routed
  2018-2026 demand was checked independently.
- **Verified PYQ ownership:** preserve all routed Mains and Prelims metadata;
  historical unavailable keys remain inferred, 2024 official keys stay official,
  and 2026 provisional keys are never promoted.""",
    8: """### Semantic-completeness ownership and PYQ control

- **Exact text first:** Part IV contains Articles 36-51. Article 36 imports the
  Part III definition of State; Article 37 denies court enforcement while making
  the principles fundamental in governance and imposing a State duty to apply
  them in making laws.
- **Complete article map:** retain every clause of Articles 38-39, then Articles
  39A, 40, 41, 42, 43, 43A, 43B, 44, 45, 46, 47, 48, 48A, 49, 50 and 51.
  Textbook socialistic, Gandhian and liberal-intellectual groupings are aids,
  not constitutional labels, and overlapping placement must be acknowledged.
- **Amendment control:** the 42nd Amendment substituted Article 39(f) and inserted
  Articles 39A, 43A and 48A; the 44th added Article 38(2); the 86th recast Article
  45 while inserting Article 21A and Article 51A(k); the 97th inserted Article 43B.
- **FR-DPSP spine:** Champakam, the First Amendment, Golak Nath, the 24th and 25th
  Amendments, Kesavananda Bharati, the 42nd Amendment and Minerva Mills establish
  harmony and balance rather than unlimited priority for either Part.
- **Article 31C present law:** Property Owners Association (5 November 2024)
  confirms survival of the original shield for genuine Article 39(b)/(c) laws
  against Articles 14 and 19; nexus review and basic-structure review remain, and
  not every private resource is automatically a material resource of the community.
- **Implementation:** distinguish constitutional direction from delivery through
  legislation and institutions. Article 39A connects to the Legal Services
  Authorities Act, NALSA and Lok Adalats; Article 40 to Panchayats; Articles
  41/45 to education; Articles 42-43A to labour; Article 48A to environmental law.
- **Current UCC control:** Article 44 is non-justiciable; courts have urged reform
  but have not ordered Parliament to enact a UCC. Uttarakhand's 2024 Act commenced
  on 27 January 2025; the Amendment Act published 7 April 2026 supersedes the
  January 2026 Ordinance.
- **Four-ledger hostile audit:** exact Part IV text, indispensable welfare-state
  prerequisites, textbook classifications and every routed 2018-2026 PYQ were
  checked for amendment history, case holdings, implementation and current status.
- **Boundary and PYQs:** Topic 07 owns detailed rights doctrine and Topic 10 basic
  structure; this owner supplies the reconciliation needed for DPSP answers.
  Direct NALSA and routed objective demands retain exact metadata and key status.""",
    9: """### Semantic-completeness ownership and PYQ control

- **Origin and placement:** the original Constitution had no separate citizen-duty
  list. The Swaran Singh Committee recommended eight duties; the 42nd Amendment,
  1976 inserted Part IVA and ten clauses in Article 51A; the 86th Amendment, 2002
  inserted clause (k), bringing the total to eleven.
- **Exact clauses:** preserve the constitutional wording and scope of clauses
  (a)-(k): Constitution/institutions/Flag/Anthem; freedom-struggle ideals;
  sovereignty-unity-integrity; defence/service; harmony and women's dignity;
  composite culture; environment/compassion; scientific temper/humanism/inquiry/
  reform; public property/non-violence; excellence; and education opportunity by
  a parent or guardian for a child or ward aged six to fourteen.
- **Legal character:** duties apply to citizens only, are non-justiciable and are
  not self-executing offences. Parliament or a competent legislature may enact a
  precise law; its validity remains subject to Fundamental Rights, competence and
  proportionality.
- **Case-law discipline:** Bijoe Emmanuel protects conscientious non-singing where
  no disrespect occurs; M.C. Mehta supports environmental education; AIIMS
  Students' Union recognises interpretive value; Naveen Jindal protects respectful
  flag display; A. Nagaraja and the 2023 Jallikattu judgment must retain their
  different statutory/constitutional outcomes.
- **Operationalisation:** the J.S. Verma Committee (1999) mapped existing laws and
  education/awareness measures. The National Honour Act, UAPA, BNS, environmental,
  public-property and education statutes create their own offences or duties;
  Article 51A alone does not.
- **Current status:** Durga Dutt, W.P.(C) 67/2022, remains pending on the located
  official record. The 11 September 2024 order sought a synopsis of Central and
  State laws effectuating Article 51A and did not make duties enforceable.
- **Four-ledger hostile audit:** exact text, committee/amendment history, legal
  mechanisms, cases, criticisms, omitted-duty traps, implementation and every
  routed or supporting 2018-2026 PYQ were checked.
- **PYQ boundary:** no direct routed objective or Mains question is invented.
  Relevant 2020 and 2025 questions remain explicitly supporting cross-topic routes.""",
    10: """### Semantic-completeness ownership and PYQ control

- **Power and routes:** Article 368 in Part XX confers constituent power to amend
  by addition, variation or repeal. Constitution-affecting changes authorised by
  provisions such as Articles 2-4, 11 and 169 may use simple-majority ordinary
  legislation outside Article 368; most amendments require the Article 368 special
  majority; federal subjects additionally require State ratification.
- **Exact procedure:** an amendment Bill may originate in either House and may be
  introduced by a minister or private member without prior Presidential
  recommendation. Each House separately must pass it by a majority of its total
  membership and two-thirds of members present and voting; there is no joint
  sitting. Where the proviso applies, not less than half the State legislatures
  ratify by simple majority. The President shall assent.
- **Exact federal proviso:** Articles 54-55, Articles 73 and 162, Article 241,
  Article 279A, Chapter IV of Part V, Chapter V of Part VI, Chapter I of Part XI,
  any Seventh Schedule List, representation of States in Parliament and Article
  368 itself require the additional ratification route.
- **Doctrine chronology:** Shankari Prasad (1951), Sajjan Singh (decision 1964,
  reporting 1965), Golak Nath (1967), 24th Amendment (1971), Kesavananda Bharati
  (24 April 1973), Indira Nehru Gandhi (1975), Minerva Mills (1980), Waman Rao
  (decision 1980, reporting 1981), S.R. Bommai (1994), L. Chandra Kumar (1997),
  I.R. Coelho (2007) and NJAC (2015) must retain their distinct holdings.
- **Basic structure:** the list is illustrative and case-attributed, not a closed
  list announced wholesale in Kesavananda. Limited amending power and judicial
  review prevent constitutional destruction while allowing broad amendment.
- **Ninth Schedule:** Waman Rao fixes 24 April 1973 as the cut-off; I.R. Coelho
  subjects later insertions to basic-structure review through the impact on
  Fundamental Rights. Article 31B is not absolute immunity.
- **Ordinary-law boundary:** Anjum Kadari, 2024 INSC 831, rejects basic structure
  as a free-standing ground to invalidate ordinary legislation; the challenger
  must identify legislative incompetence, Part III or another constitutional defect.
- **Current controls:** the 131st Amendment Bill, 2026 was defeated and is not law
  or precedent. S.O. 1922(E), 16 April 2026 commenced the 106th Amendment, while
  Article 334A still requires the post-commencement census figures and delimitation
  before reservation becomes operational.
- **Four-ledger/PYQ control:** procedure, case holdings, dates, amendments,
  elements, criticisms, current instruments and every routed 2018-2026 demand
  were checked; unavailable historical keys remain labelled and no status is inferred.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    6: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://www.indiacode.nic.in/handle/123456789/19760",
            "https://www.mha.gov.in/en/divisionofmha/foreigners-division",
            "https://www.mha.gov.in/sites/default/files/2026-08/OrderCitizenship_21082026.pdf",
            "https://www.api.sci.gov.in/supremecourt/2009/16113/16113_2009_1_1501_56604_Judgement_17-Oct-2024.pdf",
            "https://api.sci.gov.in/supremecourt/2025/5887/5887_2025_5_104_59110_Order_06-Feb-2025.pdf",
        ],
        "Rechecked 2026-09-05: official MHA/India Code materials retain the "
        "Citizenship Act, 1955, the 2019 amendment and 2024 Rules. The 19 August "
        "2026 Rule/Order changes specified Section 6B administration to Collectors "
        "without changing the class or 31 December 2014 cut-off. Section 6A remains "
        "valid under the 17 October 2024 four-to-one judgment; no later final CAA "
        "constitutional judgment was located on the official record.",
    ),
    7: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/1992/78629/78629_1992_1_1501_57003_Judgement_05-Nov-2024.pdf",
            "https://api.sci.gov.in/supremecourt/2025/60980/60980_2025_7_1501_69246_Judgement_11-Mar-2026.pdf",
            "https://api.sci.gov.in/supremecourt/2025/47573/47573_2025_4_26_63701_Order_28-Aug-2025.pdf",
            "https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf",
            "https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf",
        ],
        "Rechecked 2026-09-05: Part III text remains controlling. Property Owners "
        "preserves original Article 31C; Harish Rana applies passive-euthanasia "
        "safeguards without legalising active euthanasia; the Section 152 challenge "
        "has no located final merits disposition. DPDP Act/Rules commencement remains "
        "phased under the 13 November 2025 Gazette notifications.",
    ),
    8: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/1992/78629/78629_1992_1_1501_57003_Judgement_05-Nov-2024.pdf",
            "https://nalsa.gov.in/the-legal-services-authorities-act-1987/",
            "https://nalsa.gov.in/legal-aid/",
            "https://nalsa.gov.in/lok-adalats/",
            "https://api.sci.gov.in/supremecourt/2020/19935/19935_2020_3_1501_56637_Judgement_23-Oct-2024.pdf",
            "https://ucc.uk.gov.in/api/media/file/UCC%20Amendment%202026-1.pdf",
        ],
        "Rechecked 2026-09-05: Property Owners remains the controlling Article 31C "
        "authority; NALSA continues under the Legal Services Authorities Act, 1987. "
        "Uttarakhand's April 2026 Amendment Act is the current amending instrument, "
        "not the January Ordinance, and no unverified UCC litigation outcome is stated.",
    ),
    9: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2021/10329/10329_2021_2_112_55556_Order_11-Sep-2024.pdf",
            "https://www.indiacode.nic.in/indiacode/bitstream/123456789/15401/1/insults_to_national_honour_act%2C_1971.pdf",
            "https://www.indiacode.nic.in/indiacode/handle/123456789/20062",
        ],
        "Rechecked 2026-09-05: Article 51A remains non-justiciable and non-self-"
        "executing. Current statutory consequences come from their own enacted terms. "
        "No final merits decision was located in Durga Dutt; the 11 September 2024 "
        "order requested a synopsis and did not make Fundamental Duties enforceable.",
    ),
    10: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2024/14432/14432_2024_1_1502_56834_Judgement_05-Nov-2024.pdf",
            "https://legislative.gov.in/sites/default/files/The%20Constitution%20%28106th%20Amendment%29%20Act%2C%202023.pdf",
            "https://egazette.gov.in/WriteReadData/2026/271834.pdf",
            "https://prsindia.org/billtrack/the-constitution-131st-amendment-bill-2026",
        ],
        "Rechecked 2026-09-05: Article 368 and its proviso remain controlling. "
        "Anjum Kadari confines free-standing basic-structure invalidation to "
        "constitutional amendments. The 131st Bill was negatived and never became "
        "law. S.O. 1922(E) commenced the 106th Amendment on 16 April 2026, but "
        "Article 334A's census-publication and delimitation gates remain operative.",
    ),
}

EXTRA_PANELS: dict[str, list[tuple[str, str, str]]] = {
    "polity-06": [],
    "polity-07": [
        (
            "Current Part III control: privacy, dignity and contested speech",
            "current-rights-status-ledger",
            "DPDP G.S.R. 843(E)/846(E), 13 NOV 2025 -> phased commencement\n"
            "HARISH RANA, 11 MAR 2026 -> CANH withdrawal within passive-euthanasia safeguards\n"
            "BNS SECTION 152 -> notice on vires, 28 AUG 2025; no located final merits decision\n"
            "PROPERTY OWNERS ASSOCIATION (2024), 5 NOV 2024 -> original Article 31C survives narrowly\n"
            "RULE: current cases supply bounded propositions, not slogans or predicted outcomes.",
        )
    ],
    "polity-08": [
        (
            "Current implementation control: legal aid, labour and UCC",
            "current-dpsp-implementation-ledger",
            "ARTICLE 39A -> Legal Services Authorities Act 1987 -> NALSA / SLSA / DLSA / TALUK\n"
            "SUHAS CHAKMA, 23 OCT 2024 -> structured prison legal-aid monitoring\n"
            "FOUR LABOUR CODES -> operative from 21 NOV 2025; implementation capacity still varies\n"
            "UTTARAKHAND UCC -> 2024 Act commenced 27 JAN 2025 -> Amendment Act 7 APR 2026\n"
            "RULE: implementation evidence does not turn Article 37 into direct enforceability.",
        )
    ],
    "polity-09": [
        (
            "Current legal-status firewall: duty is not automatic liability",
            "duty-statute-status-ledger",
            "ARTICLE 51A -> constitutional duty, citizens only, non-justiciable\n"
            "NATIONAL HONOUR ACT / BNS / RTE / ENVIRONMENT LAWS -> separate statutory elements\n"
            "DURGA DUTT ORDER, 11 SEP 2024 -> synopsis requested; no final enforceability holding\n"
            "ORAL OBSERVATION != RATIO | MORAL DUTY != OFFENCE | DUTY != UNLIMITED RESTRICTION\n"
            "VERDICT: operationalise through precise law, civic education and rights-compatible review.",
        )
    ],
    "polity-10": [
        (
            "Current amendment-status control: proposal, commencement and operation",
            "constitutional-change-status-ledger",
            "ANJUM KADARI (2024) INSC 831 -> no free-standing basic-structure attack on ordinary law\n"
            "131ST AMENDMENT BILL 2026 -> defeated proposal; not law or precedent\n"
            "S.O. 1922(E), 16 APR 2026 -> 106TH AMENDMENT commenced\n"
            "ARTICLE 334A -> operation awaits specified census publication plus delimitation\n"
            "RULE: enactment, commencement and operational effect are distinct legal events.",
        )
    ],
}


def _topic_map(raw: dict[str, Any]) -> dict[str, Any]:
    topics = raw["topics"]
    if isinstance(topics, list):
        return {row["topic_key"]: row for row in topics}
    return topics


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    source_files = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / "polity-2026-08-23.json",
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "ascii-panel-specs"
        / "polity-2026-08-24-sequential-batch.json",
    )
    merged: dict[str, Any] = {}
    for path in source_files:
        merged.update(_topic_map(json.loads(path.read_text(encoding="utf-8"))))
    configs: dict[str, dict[str, Any]] = {}
    for number in range(6, 11):
        key = f"polity-{number:02d}"
        source = merged[key]
        panels = [
            (
                panel["title"],
                panel["structural_type"],
                panel["full_text"],
                panel["source_references"],
            )
            for panel in source["panels"]
        ]
        for title, structural_type, body in EXTRA_PANELS[key]:
            panels.append((title, structural_type, body, []))
        if len(panels) != 12:
            raise ValueError(f"{key}: expected twelve manually authored panels.")
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


def topics() -> list[deep.Topic]:
    manifest = deep.load(SECTION_MANIFEST)
    rows = manifest["topics"][:10]
    result = [
        deep.Topic(
            number=number,
            topic_key=row["topic_key"],
            title=row["display_title"],
            basic_path=deep.repo(row["source_basic"]),
            canonical_path=deep.repo(row["source_canonical"]),
            advanced_path=deep.repo(row["source_advanced"]),
            cross_topic_sources=tuple(
                deep.repo(path) for path in row.get("cross_topic_sources", [])
            ),
            pyq_sources=tuple(
                deep.repo(path) for path in row.get("verified_pyq_sources", [])
            ),
        )
        for number, row in enumerate(rows, 1)
    ]
    expected = [f"polity-{number:02d}" for number in range(1, 11)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-10 changed or are out of order.")
    return result


_original_validate_spec = deep._real_graphical_validate_spec


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 11)}:
        deep._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def apply_configuration() -> None:
    combined_points = {**deep.POLITY_REVIEW_POINTS, **POLITY_REVIEW_POINTS}
    combined_controls = {**deep.CANONICAL_OWNER_CONTROLS, **CANONICAL_OWNER_CONTROLS}
    combined_sources = {
        **deep.POLITY_LIVE_OFFICIAL_SOURCES,
        **POLITY_LIVE_OFFICIAL_SOURCES,
    }
    combined_configs = {**deep.CURRENT_AUTHORING_CONFIGS, **CURRENT_AUTHORING_CONFIGS}
    deep.POLITY_REVIEW_POINTS = combined_points
    deep.CANONICAL_OWNER_CONTROLS = combined_controls
    deep.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
    deep.CURRENT_AUTHORING_CONFIGS = combined_configs
    deep.topics = topics
    deep.carvaka_flowchart.validate_spec = _validate_polity_graphical_spec
    deep.base.WORKFLOW = "polity-06-10-hostile-semantic-immutable-successor"
    deep.base.SOCIETY_REVIEW_POINTS = combined_points
    deep.base.SOCIETY_LIVE_OFFICIAL_SOURCES = combined_sources
    deep.base.LIVE_OFFICIAL_SOURCES = combined_sources
    deep.base.CANONICAL_OWNER_CONTROLS = combined_controls
    deep.base.CURRENT_AUTHORING_CONFIGS = combined_configs
    deep.base.topics = topics


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
ensure_canonical_owner_control = deep.ensure_canonical_owner_control
completed_result = deep.completed_result
