"""Extend the hostile Polity deep-review workflow to topics 11-15."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_06_10_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    11: (
        "Build responsible government from Articles 74, 75, 78 and 88 at the "
        "Union and Articles 163-164 in the States: aid and advice, appointment, "
        "collective responsibility, confidence, six-month membership, ministry "
        "size, secrecy and dissolution must remain distinct.",
        "India has parliamentary government but not British parliamentary "
        "sovereignty. Compare parliamentary and presidential systems only on "
        "executive identity, tenure, responsibility, membership, dissolution and "
        "fusion/separation; do not turn an analytical comparison into Indian law.",
        "The 129th Amendment Bill, 2024 remains a proposal under Joint Committee "
        "examination on the located official record. Article 82A is not operative "
        "constitutional text and no implementation date may be invented.",
    ),
    12: (
        "Test federalism through dual government, constitutional distribution, "
        "supremacy, rigidity, independent courts and bicameral representation, "
        "then map the Union tilt through Articles 3, 248-253, 256-257, 312, "
        "352-356 and integrated constitutional institutions.",
        "Article 1's 'Union of States' rejects a secession compact but does not "
        "make India unitary. Federalism is basic structure; the Union may be "
        "stronger and States territorially alterable while each level retains "
        "constitutionally assigned fields.",
        "Current federal claims must distinguish enacted law, advisory judgments "
        "and failed proposals: the 2025 Article 143 opinion controls assent, the "
        "16th Finance Commission retains 41 percent vertical devolution, and the "
        "defeated 131st Amendment Bill, 2026 never amended the Constitution.",
    ),
    13: (
        "Keep four owned dimensions separate: legislative relations under "
        "Articles 245-255, administrative relations under Articles 256-263 and "
        "355/365, financial relations under Articles 268-293, and inter-State "
        "coordination under Articles 261-263 and 301-307.",
        "Article 254 repugnancy is principally a Concurrent-List conflict rule; "
        "pith and substance tests competence, Article 262 permits statutory "
        "exclusion for defined river disputes, and Article 263 creates an enabling "
        "power rather than a self-executing adjudicatory council.",
        "Special Reference No. 1 of 2025 rejects rigid judicial timelines and "
        "deemed assent, recognises Article 200 discretion, and permits only a "
        "limited mandamus against prolonged, unexplained and indefinite inaction. "
        "Do not continue the displaced April 2025 timeline rule.",
    ),
    14: (
        "Teach Articles 352-360 as three different regimes with exact triggers, "
        "approval periods, renewal, revocation, maximum duration, federal effects "
        "and rights consequences; Articles 358 and 359 must never be merged.",
        "The 44th Amendment replaced internal disturbance with armed rebellion, "
        "requires written Cabinet advice, protects Articles 20 and 21, narrows "
        "Article 358 to war/external aggression and creates the Lok Sabha "
        "revocation route; Article 356 still has its own six-month approval cycle.",
        "As of 5 September 2026 no National or Financial Emergency was located in "
        "force. The Gazette proclamation of 4 February 2026 revoked the Manipur "
        "Article 356 proclamation; retain Bommai review and floor-test discipline "
        "without converting every political crisis into constitutional breakdown.",
    ),
    15: (
        "Map Articles 52-73 office by office: electoral colleges, vote values, "
        "qualifications, oath, term, vacancy, impeachment/removal, Article 71 "
        "disputes, aid and advice, veto, ordinance and clemency require separate "
        "procedural chains.",
        "The President is indirectly elected by elected MPs and elected MLAs of "
        "States plus Delhi and Puducherry; the Vice-President is elected by all "
        "members of both Houses. Presidential impeachment under Article 61 and "
        "Vice-Presidential removal under Article 67(b) are not interchangeable.",
        "Current office control is Droupadi Murmu as President and C. P. "
        "Radhakrishnan as Vice-President, elected 9 September and assuming office "
        "12 September 2025. Articles 72 and 123 remain advice-bound and judicially "
        "reviewable within settled constitutional limits.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    11: """### Semantic-completeness ownership and PYQ control

- **Constitutional spine:** Articles 74-75 create the Union aid-and-advice and
  responsible-ministry structure; Article 78 is the Prime Minister-President
  information bridge; Article 88 supplies participation rights. Articles 163-164
  are the State counterparts, subject to constitutionally conferred gubernatorial
  discretion.
- **Advice and office:** the 42nd Amendment made Article 74 advice binding and
  the 44th permits one reconsideration, after which reconsidered advice binds.
  Article 75 separately controls appointment, presidential pleasure, collective
  responsibility, oath and the six-month non-member rule.
- **Responsibility:** the Council is collectively responsible only to the Lok
  Sabha under Article 75(3). Individual responsibility, collective responsibility
  and legal responsibility are distinct; no-confidence is a House mechanism and
  ministerial resignation conventions cannot be presented as express text.
- **Ninety-first Amendment:** Article 75(1A) caps Union ministers at fifteen per
  cent of Lok Sabha strength; Article 75(1B) bars a disqualified defector from
  ministership. Article 164(1A) applies the State cap with a minimum of twelve.
- **Confidence and dissolution:** government survives while it commands Lok Sabha
  confidence. Dissolution, caretaker practice, floor tests and alternative-
  government exploration operate through constitutional text plus conventions
  and judicial controls; the President does not acquire a personal political veto.
- **Owned comparison:** this topic alone owns the full parliamentary-presidential
  comparison: dual/single executive, flexible/fixed tenure, responsibility,
  legislative membership, dissolution and fusion/separation. India-UK distinctions
  are republican head, limited Parliament and the Indian PM's eligibility from
  either House.
- **Practice critique:** majority control, whip and the Tenth Schedule, government
  control of business, delegated legislation, ordinances and money-bill routing
  explain cabinet dominance; committees, questions, finance control, confidence
  and judicial review qualify the claim.
- **Current control:** the Constitution (129th Amendment) Bill, 2024 was introduced
  on 17 December 2024 and remains with the Joint Committee on the located official
  record. Proposed Article 82A is not constitutional law.
- **Four-ledger hostile audit:** exact Articles, amendments, conventions, cases,
  comparative axes, institutional practice and every routed 2018-2026 demand were
  checked without moving detailed PM/CoM or parliamentary procedure out of their
  adjacent owners.
- **Verified PYQ ownership:** direct 2024 GS-II Q3 and routed 2020/2021 objective
  demands are preserved; 2018 and 2023 comparative Mains demands remain disclosed
  cross-owner routes, and unavailable historical keys are not promoted.""",
    12: """### Semantic-completeness ownership and PYQ control

- **Federal test:** India combines dual polity, a written and supreme Constitution,
  distributed competence, partial rigidity, independent judicial review and
  bicameral representation. Article 1's 'Union of States' denies a compact-based
  right to secede; it does not erase the federal distribution.
- **Distribution:** Articles 245-246 and the Seventh Schedule allocate fields;
  Article 248 with Union List Entry 97 gives Parliament the residue. Article 246A
  is a special concurrent GST power, not a new Concurrent-List entry.
- **Union tilt:** Articles 3, 249, 250, 252, 253, 256-257, 312 and 352-356, the
  Governor's Union appointment, single citizenship, integrated services and
  emergency conversion explain why India is a holding-together federation with a
  strong Centre.
- **Basic structure:** Kesavananda Bharati supplies the limitation method and S.R.
  Bommai expressly treats federalism as a basic feature. Union strength cannot be
  converted into unlimited central supremacy over constitutionally assigned State
  fields.
- **Working modes:** cooperative, competitive and coercive federalism are analytical
  descriptions. GST Council, Finance Commission, Inter-State Council and Zonal
  Councils are different in source, membership and legal effect.
- **Asymmetry:** Articles 371-371J, Fifth/Sixth Schedule arrangements and Union
  territories show differentiated integration. Article 370 is inoperative and
  Jammu and Kashmir is not presently a special-status State.
- **Owned comparison:** the complete federal-unitary comparison belongs here:
  levels, source of powers, constitutional supremacy, amendment, judiciary,
  representation and territorial security. Topic 13 owns the detailed operating
  relations between the two levels.
- **Current assent law:** the 20 November 2025 Article 143 opinion rejects fixed
  judicial timelines and deemed assent, recognises Article 200 discretion, and
  permits limited mandamus only for prolonged, unexplained, indefinite inaction.
- **Fiscal and representational control:** the Sixteenth Finance Commission report
  for 2026-31 retains forty-one per cent vertical devolution. The 131st Amendment
  Bill, 2026 was defeated and its proposed 850-seat ceiling never became law.
- **Four-ledger/PYQ control:** the federal/unitary taxonomy, exact centralising
  devices, cases, commissions, current fiscal/assent/representation status and all
  routed demands were checked; direct and cross-topic ownership remain labelled.""",
    13: """### Semantic-completeness ownership and PYQ control

- **Legislative relations:** Articles 245-255, the Seventh Schedule and Articles
  246A/248 establish territorial reach, distribution, GST competence, residue and
  repugnancy. Parliament enters the State field only through the distinct routes
  in Articles 249, 250, 252, 253 and 356.
- **Conflict doctrines:** pith and substance tests true character; territorial
  nexus tests State-law reach; colourable legislation tests disguised incompetence;
  harmonious construction seeks coexistence; Article 254 resolves repugnancy,
  including the limited President-assented State-law exception in clause (2).
- **Administrative relations:** Articles 256-257 directions, Article 258/258A
  entrustment, Article 261 full faith and credit, Article 263 coordination,
  Article 312 All-India Services, and Articles 355/365 must retain separate
  triggers and consequences.
- **CBI boundary:** Section 6 of the Delhi Special Police Establishment Act requires
  State consent for ordinary CBI exercise of powers in a State. Withdrawal of
  general consent does not displace constitutional-court power under Articles
  32/226 or automatically nullify every lawfully commenced investigation.
- **Financial relations:** Articles 268-281, 292-293, Article 246A/269A/279A,
  the divisible pool, grants, cesses/surcharges, borrowing and Finance Commission
  recommendations must be analysed as distinct vertical and horizontal mechanisms.
- **Inter-State relations:** Article 262 plus the 1956 water-disputes statute,
  Article 263, statutory Zonal Councils, the North-Eastern Council, Article 261 and
  Articles 301-307 create different adjudicatory, consultative and market routes.
- **Commissions:** Rajamannar, Sarkaria and Punchhi recommendations are named
  reform evidence, not binding constitutional amendments. Article 356 remains a
  last-resort control under S.R. Bommai.
- **Current assent law:** Special Reference No. 1 of 2025 holds that the Governor
  has three Article 200 options, acts with discretion rather than State-Cabinet
  advice for that choice, and is not subject to merits review; only prolonged,
  unexplained and indefinite inaction permits limited mandamus to act.
- **Current fiscal control:** the Sixteenth Finance Commission submitted its report
  on 17 November 2025 for 2026-31 and retained forty-one per cent vertical
  devolution. Mohit Minerals continues to treat GST Council recommendations as
  persuasive rather than binding.
- **Four-ledger/PYQ control:** all four relation dimensions, doctrines, commissions,
  institutions, live legal status and the eleven direct/supporting 2018-2025
  demands were reconciled; federal/unitary taxonomy stays in Topic 12.""",
    14: """### Semantic-completeness ownership and PYQ control

- **Part XVIII map:** Article 352 is National Emergency; Articles 353-354 state
  its executive, legislative and revenue effects; Article 355 is the Union duty;
  Articles 356-357 govern State constitutional failure; Articles 358-359 govern
  specified rights effects; Article 360 is Financial Emergency.
- **Article 352:** only war, external aggression or armed rebellion qualify.
  Written Union-Cabinet advice, one-month parliamentary approval by special
  majority, six-month renewals, revocation and the one-tenth Lok Sabha notice
  route inserted by the 44th Amendment must remain exact.
- **Rights firewall:** Article 358 concerns Article 19 only, operates automatically
  only during war/external-aggression emergency, and protects only emergency-
  related law/action carrying the required recital. Article 359 requires a
  Presidential order and cannot suspend enforcement of Articles 20 and 21.
- **Article 356:** the proclamation needs parliamentary approval within two months,
  continues in six-month blocks and ordinarily cannot exceed three years; beyond
  one year the Article 356(5) conditions apply. Parliament assumes legislative
  power but High Court jurisdiction cannot be taken over.
- **Judicial control:** S.R. Bommai makes the proclamation reviewable and prefers a
  floor test for disputed majority; Rameshwar Prasad condemns premature dissolution.
  Article 355, Article 365 and a Governor's report do not create automatic failure.
- **ADM Jabalpur:** the majority's habeas-corpus approach is repudiated; Justice
  H.R. Khanna's dissent is vindicated and K.S. Puttaswamy records the overruling.
  Do not use the case to negate the express post-44th Article 20/21 protection.
- **Article 360:** two-month parliamentary approval and indefinite continuation
  until revocation are textually distinct from Article 352/356. It has never been
  proclaimed and does not automatically suspend Fundamental Rights.
- **Current status:** the Gazette proclamation dated 4 February 2026 revoked the
  Manipur Article 356 proclamation of 13 February 2025. No National Emergency or
  Financial Emergency was located in force on 5 September 2026.
- **Four-ledger hostile audit:** triggers, dates, amendment history, cases, rights
  effects, federal consequences, commissions, current proclamations and every
  routed 2018-2026 demand were independently checked.
- **PYQ boundary:** the 2018 Article 356 objective demand is direct; the 2023
  detention/POTA demand is retained only as an expressly supporting route and no
  direct Mains question is fabricated.""",
    15: """### Semantic-completeness ownership and PYQ control

- **Office map:** Articles 52-62 govern the President's office/election/term and
  Article 61 impeachment; Articles 63-71 govern the Vice-President, with Article
  71 giving the Supreme Court final jurisdiction over both elections. Articles
  72-73 then address clemency and Union executive extent.
- **Electoral colleges:** Article 54 includes elected MPs and elected MLAs of the
  States plus Delhi and Puducherry; nominated members and Legislative-Council
  members do not vote. Article 66 includes elected and nominated members of both
  Houses but no State legislators.
- **Vote and vacancy:** Article 55 vote values and PR-STV/secret ballot apply to
  the President; the Vice-President uses PR-STV/secret ballot without MLA vote
  values. Articles 62 and 68 impose different vacancy schedules.
- **Removal:** Article 61 impeachment for constitutional violation may begin in
  either House after fourteen days' notice signed by at least one-fourth and needs
  two-thirds of total membership in each House. Article 67(b) Vice-Presidential
  removal begins only in Rajya Sabha, uses an effective-majority resolution agreed
  to by Lok Sabha, and also requires fourteen days' notice.
- **Aid and advice:** Article 74 advice binds after one reconsideration. Situational
  discretion in appointing a Prime Minister, seeking proof of confidence or
  exploring alternatives is bounded by responsible-government conventions and
  cannot become personal presidential rule.
- **Veto and reserved Bills:** Article 111 assent/withholding/return applies to
  Parliamentary Bills, with no return of a Money Bill. Article 201 is a separate
  reserved-State-Bill route governed by the 20 November 2025 Article 143 opinion;
  it has no judicially fixed deadline or deemed assent.
- **Ordinance:** Article 123 requires both Houses not to be in session, has the
  force of an Act, must stay within legislative/rights limits, and ceases six
  weeks after reassembly unless earlier withdrawn/disapproved. D.C. Wadhwa and
  Krishna Kumar Singh reject routine re-promulgation.
- **Clemency:** Article 72 covers Union-law offences, court-martial and death
  sentences; Article 161 tracks State executive competence and cannot pardon a
  court-martial or death sentence. Maru Ram, Kehar Singh and Epuru Sudhakar
  preserve ministerial advice and limited review for mala fides, arbitrariness or
  irrelevant considerations.
- **Current offices:** Droupadi Murmu remains President. C. P. Radhakrishnan was
  elected Vice-President on 9 September 2025 and assumed office on 12 September
  2025 after the casual vacancy; Article 68 requires filling it as soon as possible,
  not within an invented six-month deadline.
- **Four-ledger/PYQ control:** exact Articles, electoral law, vote arithmetic,
  conventions, cases, current officeholders and all routed 2018-2025 demands were
  reconciled; detailed PM/CoM, Parliament and Governor doctrine remains cross-owned.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    11: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://cabsec.gov.in/",
            "https://sansad.in/ls/committee/other-committees/80-Joint%20Committee%20on%20the%20Constitution%20(One%20Hundred%20and%20Twenty%E2%80%93Ninth%20Amendment)%20Bill,%202024%20and%20the%20Union%20Territories%20Laws%20(Amendment)%20Bill,%202024-nameH=undefined",
            "https://prsindia.org/files/bills_acts/bills_parliament/2024/Bill_Summary-Constitution_(129th_Amendment)_Bill_2024.pdf",
        ],
        "Rechecked 2026-09-05: Articles 74, 75, 78, 88, 163 and 164 remain "
        "controlling. The official Lok Sabha Joint Committee page continues to "
        "list the 129th Amendment Bill, 2024 inquiry; the Bill is not enacted and "
        "proposed Article 82A is not operative text.",
    ),
    12: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
            "https://gstcouncil.gov.in/",
            "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/16fc-EM.pdf",
            "https://sansad.in/getFile/BillsTexts/LSBillTexts/Asintroduced/AS%20INTRO416202612944PM.pdf?source=legislation",
        ],
        "Rechecked 2026-09-05: federalism remains basic structure within a "
        "constitutionally strong Union. The 2025 Article 143 opinion controls "
        "State-Bill assent; the Sixteenth Finance Commission retains 41 percent "
        "vertical devolution for 2026-31. The 131st Amendment Bill, 2026 was "
        "defeated and did not amend representation or delimitation law.",
    ),
    13: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
            "https://interstatecouncil.gov.in/",
            "https://www.mha.gov.in/en/page/zonal-council",
            "https://www.indiacode.nic.in/handle/123456789/1664",
            "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/16fc-EM.pdf",
            "https://gstcouncil.gov.in/",
        ],
        "Rechecked 2026-09-05: Special Reference No. 1 of 2025 rejects rigid "
        "assent timelines and deemed assent while preserving limited mandamus for "
        "prolonged, unexplained, indefinite inaction. The Sixteenth Finance "
        "Commission retains 41 percent vertical devolution; Article 263, statutory "
        "Zonal Councils, the 1956 river-disputes framework and DSPE consent remain "
        "legally distinct coordination routes.",
    ),
    14: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://egazette.gov.in/WriteReadData/2026/269819.pdf",
            "https://www.mha.gov.in/en",
            "https://api.sci.gov.in/supremecourt/2012/35071/35071_2012_Judgement_24-Aug-2017.pdf",
        ],
        "Rechecked 2026-09-05: no National Emergency or Financial Emergency was "
        "located in force. The Gazette of India proclamation dated 4 February "
        "2026 revoked the Manipur Article 356 proclamation issued on 13 February "
        "2025. The post-44th Amendment text and S.R. Bommai review remain controlling.",
    ),
    15: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://www.presidentofindia.gov.in/",
            "https://vicepresidentofindia.nic.in/about-department/profile-of-president-of-india/",
            "https://www.eci.gov.in/eci-backend/public/api/download?url=LMAhAK6sOPBp%2FNFF0iRfXbEB1EVSLT41NNLRjYNJJP1KivrUxbfqkDatmHy12e%2FzIC5IR1A3V88Anuk8RlyPGe5wAx9KElz%2FMrntZbUSdw5U7CT4RufW5GdjJTZLaanPhyiHHcRTVH1vrlRp0EJdTg%3D%3D",
            "https://api.sci.gov.in/supremecourt/2025/39157/39157_2025_1_1501_66169_Judgement_20-Nov-2025.pdf",
        ],
        "Rechecked 2026-09-05: official profiles list Droupadi Murmu as President "
        "and C. P. Radhakrishnan as Vice-President; the latter was elected on "
        "9 September 2025 and assumed office on 12 September 2025. No amendment "
        "to Articles 52-73 was located; settled advice, veto, ordinance and "
        "clemency controls remain operative.",
    ),
}

EXTRA_PANELS: dict[str, list[tuple[str, str, str]]] = {
    "polity-11": [
        (
            "Current parliamentary-design control: simultaneous elections remain a Bill",
            "current-parliamentary-design-ledger",
            "129TH AMENDMENT BILL, 17 DEC 2024 -> proposed Article 82A\n"
            "JOINT COMMITTEE -> official inquiry continues on 5 SEP 2026\n"
            "BILL != ACT | PROPOSED ARTICLE != CONSTITUTIONAL TEXT\n"
            "FIXED CYCLES MAY AFFECT DISSOLUTION/CONFIDENCE -> requires enacted amendment\n"
            "RULE: analyse the proposal; never teach implementation as current law.",
        )
    ],
    "polity-12": [],
    "polity-13": [],
    "polity-14": [],
    "polity-15": [],
}

SOURCE_OVERRIDES: dict[int, dict[str, tuple[str, ...]]] = {
    13: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\README.md",
            "upsc-ai-kit\\knowledge\\Polity\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "upsc-ai-kit\\knowledge\\Polity\\ANSWER-WORTHINESS-AUDIT.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Finance-Commission.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\GST-Council.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\CVC-and-CBI.md",
        ),
        "pyq": (
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2024-2025.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
        ),
    },
    14: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\README.md",
            "upsc-ai-kit\\knowledge\\Polity\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Fundamental-Rights.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Federal-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
        ),
        "pyq": (
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
        ),
    },
    15: {
        "cross": (
            "upsc-ai-kit\\knowledge\\Polity\\README.md",
            "upsc-ai-kit\\knowledge\\Polity\\OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliamentary-System.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\PM-and-Council-of-Ministers.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Parliament.md",
            "upsc-ai-kit\\knowledge\\Polity\\basic\\Governor-and-CM.md",
        ),
        "pyq": (
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2018-2023.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-PRELIMS-2024-2025.md",
            "upsc-ai-kit\\knowledge\\_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
        ),
    },
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
        / "polity-2026-08-24-sequential-batch.json",
        *(
            ROOT
            / "upsc-ai-kit"
            / "manifests"
            / "retrofits"
            / "ascii-panel-specs"
            / f"polity-{number:02d}-2026-08-24-sequential.json"
            for number in range(13, 16)
        ),
    )
    merged: dict[str, Any] = {}
    for path in source_files:
        merged.update(_topic_map(json.loads(path.read_text(encoding="utf-8"))))
    configs: dict[str, dict[str, Any]] = {}
    for number in range(11, 16):
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
        if key == "polity-12":
            title, structural_type, body, references = panels[7]
            panels[7] = (
                title,
                structural_type,
                body
                + "\n2024 West Bengal ruling (2024 INSC 502): Article 131 suit survived\n"
                "preliminary objections; CBI-consent merits were not decided.",
                references,
            )
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

_inherited_enforce_strict_rotation = deep.deep.enforce_strict_rotation


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = deep.deep.basic_mcq_area(repaired)
    keys = re.findall(r"(?im)^\*\*Answer:\s*([A-D])\.\*\*\s*$", area)
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
    rows = manifest["topics"][:15]
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
    expected = [f"polity-{number:02d}" for number in range(1, 16)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-15 changed or are out of order.")
    return result


_original_validate_spec = deep._original_validate_spec


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 16)}:
        deep.deep._normalize_graphical_tree(spec, topic_key)
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
    deep.deep.POLITY_REVIEW_POINTS = combined_points
    deep.deep.CANONICAL_OWNER_CONTROLS = combined_controls
    deep.deep.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.CURRENT_AUTHORING_CONFIGS = combined_configs
    deep.deep.topics = topics
    deep.deep.enforce_strict_rotation = enforce_strict_rotation
    deep.deep.carvaka_flowchart.validate_spec = _validate_polity_graphical_spec
    deep.deep.base.WORKFLOW = "polity-11-15-hostile-semantic-immutable-successor"
    deep.deep.base.SOCIETY_REVIEW_POINTS = combined_points
    deep.deep.base.SOCIETY_LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.base.LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.base.CANONICAL_OWNER_CONTROLS = combined_controls
    deep.deep.base.CURRENT_AUTHORING_CONFIGS = combined_configs
    deep.deep.base.topics = topics
    deep.deep.base.enforce_strict_rotation = enforce_strict_rotation


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
