"""Extend the hostile Polity deep-review workflow to topics 21-25."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import regenerate_polity_16_20_deep_review as deep


ROOT = deep.ROOT
DATE = "2026-09-05"
SECTION_MANIFEST = deep.SECTION_MANIFEST

POLITY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    21: (
        "Audit Articles 214-237 as separate constitutional controls: High Court "
        "existence/common courts, judge appointment and service, jurisdiction, "
        "writs, superintendence, court administration and subordinate-judiciary "
        "recruitment/control must not be collapsed into one judicial-independence claim.",
        "Keep Articles 226, 227 and 235 distinct. Article 226 reaches Fundamental "
        "Rights and other legal rights; Article 227 is supervisory rather than an "
        "ordinary appeal; Article 235 gives the High Court administrative control "
        "over the district and subordinate judiciary.",
        "India has 25 High Courts. The 1 July 2026 DoJ snapshot is 1,122 sanctioned, "
        "781 working and 341 vacant. Rejanish K.V. (2025 INSC 1208) prospectively "
        "replaced the categorical Dheeraj Mor exclusion; AIJS remains uncreated.",
    ),
    22: (
        "Own Articles 371-371J and only the minimum Article 370/35A status needed "
        "to explain present asymmetric federalism. State, Article, amendment, "
        "protected interest and constitutionally responsible actor must match exactly.",
        "Do not merge Part XXI State-specific clauses with Article 244 and the "
        "Fifth/Sixth Schedules, PESA, Union-Territory administration, or special "
        "provisions for certain classes. Those are Topics 26, 23, 25 and 53.",
        "Article 370 remains printed but inoperative. In re Article 370 upheld the "
        "2019 constitutional result, did not finally adjudicate J&K's conversion "
        "to a Union Territory after the Union assurance, and left Ladakh's UT "
        "formation undisturbed. J&K statehood remains unrestored.",
    ),
    23: (
        "Map the Seventy-third Amendment, Part IX Articles 243-243O and the "
        "Eleventh Schedule's 29 matters before testing actual devolution of "
        "functions, functionaries and finances under State law.",
        "Article 243M exclusions and PESA's Section 4 bridge require exact verbs: "
        "consultation before land acquisition/resettlement; mandatory prior "
        "recommendation for minor-mineral licences/leases/concessions; ownership "
        "of minor forest produce and specified control powers.",
        "The Devolution Index Report 2024 and Sixteenth Finance Commission "
        "2026-27 to 2030-31 framework are dated official controls. PESA covers "
        "Fifth Schedule Scheduled Areas; full Fifth/Sixth Schedule machinery is Topic 26.",
    ),
    24: (
        "Audit the Seventy-fourth Amendment, Part IXA Articles 243P-243ZG and "
        "Twelfth Schedule's 18 matters through municipal types, composition, "
        "reservation, duration, elections, powers, finance and planning committees.",
        "Articles 243W and 243X are enabling: constitutional status does not itself "
        "transfer functions, staff or buoyant revenue. DPC four-fifths, MPC "
        "two-thirds, Ward Committee three-lakh threshold and SEC ownership must stay exact.",
        "Use XVI Finance Commission 2026-31, AMRUT 2.0 and the SEBI municipal-debt "
        "framework only as dated evidence. SEBI's 2015 regulations were amended "
        "on 8 July 2026; bonds are regulated borrowing, not tax devolution.",
    ),
    25: (
        "Separate Articles 239, 239A, 239AA, 239AB, 239B, 240, 241 and 246(4), "
        "then distinguish direct administration, statutory legislatures and "
        "Delhi's constitutionally entrenched NCT model.",
        "Delhi excludes State List Entries 1, 2 and 18 plus related 64-66; J&K "
        "excludes public order and police; Puducherry's statutory competence is "
        "over List II/III matters insofar as applicable to Union Territories. "
        "Parliament retains overriding UT competence.",
        "India has eight Union Territories and three legislatures: Delhi, "
        "Puducherry and J&K. J&K has an elected government but remains a UT; "
        "Ladakh has no legislature. Act 19 of 2023 remains operative while the "
        "Delhi services constitutional challenge is unresolved.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    21: """### Semantic-completeness ownership and PYQ control

- **Constitutional map:** Articles 214-237 divide into Articles 214-231 governing
  High Courts and Articles 233-237 governing
  govern the subordinate judiciary. Article 214 does not produce one court for
  every State because Article 231 permits Parliament to establish a common High
  Court for two or more States or for States and Union Territories.
- **Judges and independence:** Article 217 separates appointment, qualification,
  tenure and consultation; Article 218 applies specified Supreme Court safeguards;
  Articles 219-224A cover oath, practice, salaries, transfer, acting/additional
  judges and retired judges. High Court judges retire at sixty-two.
- **Jurisdiction firewall:** Article 225 preserves inherited jurisdiction subject
  to the Constitution and law. Article 226 authorises writs for Fundamental Rights
  and any other purpose, subject to territorial cause-of-action rules; Article 227
  is superintendence, not a substitute statutory appeal. Article 215 makes each
  High Court a court of record with contempt power.
- **Review doctrine:** L. Chandra Kumar (1997) preserves Articles 226/227 review
  over tribunal decisions as part of the Basic Structure. Whirlpool (1998)
  states the recognised alternative-remedy exceptions. Radhey Shyam (2015)
  keeps judicial orders of civil courts outside Article 226 while Article 227
  supervision remains available within its limits.
- **Subordinate recruitment:** Article 233 places appointment, posting and
  promotion of district judges with the Governor in consultation with the High
  Court; Article 234 governs recruitment below district judge through Governor-
  made rules after State PSC and High Court consultation. Articles 236-237 define
  the chapter's reach.
- **Current Article 233 rule:** Rejanish K.V. v. K. Deepa, 2025 INSC 1208,
  prospectively overruled Dheeraj Mor's categorical exclusion. Qualifying serving
  judicial officers may compete in direct District-Judge recruitment under the
  combined-experience, minimum-age and application-date conditions stated by the Court.
- **Control and separation:** Article 235 vests control over district and
  subordinate courts in the High Court; Article 50 directs separation of the
  judiciary from the executive. State executive participation in appointment
  does not permit control over judicial careers or adjudication.
- **AIJS boundary:** Article 312 permits an All India Judicial Service only after
  the Rajya Sabha's two-thirds present-and-voting resolution and parliamentary
  law; Article 312(3) excludes posts below district judge. No AIJS exists as of
  5 September 2026.
- **Current capacity control:** India has twenty-five High Courts. The Department
  of Justice snapshot dated 1 July 2026 records 1,122 sanctioned posts, 781
  working judges and 341 vacancies; working strength, vacancy and pendency are
  dynamic and must retain their date.
- **Four-ledger/PYQ control:** direct and routed 2018-2025 High Court, tribunal,
  Lok Adalat, collegium and subordinate-judiciary demands were retained without
  fabricating a direct route. Topic 18 owns Supreme Court detail; Topic 54 owns
  full Lok Adalat and other-court architecture.""",
    22: """### Semantic-completeness ownership and PYQ control

- **Exact ownership:** this topic owns the State-specific asymmetry of Articles
  371-371J and the minimum Article 370/35A history required to state current law.
  Article 369 and Articles 372-392 are classified as other temporary/transitional
  Part XXI provisions, not silently absorbed into the Article 371 catalogue.
- **Boundary firewall:** Article 244 and the Fifth/Sixth Schedules belong to Topic
  26; PESA's Panchayat extension belongs to Topic 23; Articles 239-241 and the
  J&K/Ladakh UT machinery belong to Topic 25; Articles 330 onward concerning
  certain classes belong to Topic 53.
- **Article 371:** the current Maharashtra-Gujarat clause permits a Presidential
  order assigning the Governor special responsibility for separate development
  boards, annual Assembly reporting, equitable development expenditure and
  opportunity in technical education, vocational training and State services.
- **Consent shields:** Article 371A, inserted by the Thirteenth Amendment, 1962,
  protects specified Naga practices, customary law/justice and land/resources
  unless the Nagaland Assembly resolves otherwise. Article 371G, inserted by the
  Fifty-third Amendment, 1986, supplies the parallel but textually distinct
  Mizoram shield and a forty-member Assembly minimum.
- **Committee models:** Article 371B, Twenty-second Amendment, 1969, authorises a
  Presidential order for an Assam Assembly committee. Article 371C, Twenty-seventh
  Amendment, 1971, adds Manipur's Hill Areas Committee, Governor report/special
  responsibility and possible Union directions. Neither is a Sixth Schedule council.
- **Opportunity and integration:** Articles 371D/E came through the Thirty-second
  Amendment, 1973; Section 97 of the Andhra Pradesh Reorganisation Act, 2014
  adapted Article 371D for Telangana. Article 371F is the Thirty-sixth Amendment,
  1975 Sikkim settlement; Article 371I, Fifty-sixth Amendment, 1987, only fixes
  Goa's Assembly minimum.
- **Law-and-order and development:** Article 371H, Fifty-fifth Amendment, 1986,
  gives Arunachal Pradesh's Governor bounded law-and-order responsibility after
  ministerial consultation and subject to Presidential termination. Article 371J,
  Ninety-eighth Amendment, 2012, effective 2013, concerns the constitutionally
  named Hyderabad-Karnataka region, now officially Kalyana Karnataka.
- **Article 370 current rule:** C.O. 272 of 5 August 2019 and C.O. 273 of 6 August
  2019 produced the present inoperative position; Article 35A ceased with the
  1954 Order's supersession. In re Article 370, 2023 INSC 1058, upheld the
  constitutional result while treating the Article 367 substitution as invalid
  to the stated extent and unnecessary to the outcome.
- **Reorganisation limit:** the Court did not finally adjudicate J&K's conversion
  from State to Union Territory after recording the Union's restoration assurance;
  it upheld Ladakh's creation as a Union Territory. J&K remains a UT with an
  elected legislature and Ladakh a UT without one on 5 September 2026.
- **Four-ledger/PYQ control:** Article 371 actor/state/amendment traps and routed
  Article 370/asymmetric-federalism demands were retained. Full Scheduled/Tribal
  Areas doctrine is deliberately deferred to Topic 26 rather than duplicated.""",
    23: """### Semantic-completeness ownership and PYQ control

- **Constitutional birth:** the Constitution (Seventy-third Amendment) Act, 1992
  inserted Part IX and the Eleventh Schedule and commenced on 24 April 1993.
  Articles 243-243O and the twenty-nine Schedule matters are the exact core.
- **Democratic structure:** Article 243A leaves Gram Sabha powers to State law;
  Article 243B creates village, intermediate and district tiers, with the
  population-not-exceeding-twenty-lakh intermediate-tier exception; Articles
  243C-243F govern composition, reservation, duration and disqualification.
- **Election precision:** Article 243E requires election before expiry or within
  six months of dissolution, unless the remainder is under six months; a
  reconstituted Panchayat serves only the unexpired term. Article 243K vests
  electoral control in the State Election Commission; Article 243O channels
  challenges through election petitions.
- **Devolution limit:** Article 243G and the Eleventh Schedule enable State-law
  endowment of powers; they do not automatically transfer all twenty-nine matters.
  Article 243H supplies taxes, assignments, grants and funds; Articles 243I/J
  provide the State Finance Commission and audit routes.
- **PESA scope:** Article 243M excludes specified areas and States. The Provisions
  of the Panchayats (Extension to the Scheduled Areas) Act, 1996 extends a
  modified framework only to Fifth Schedule Scheduled Areas, not Sixth Schedule areas.
- **PESA verb control:** Section 4 requires consultation before land acquisition
  and resettlement/rehabilitation; mandatory prior recommendation before minor-
  mineral prospecting licences, mining leases and concessions; ownership of minor
  forest produce; and specified powers over alienation, markets, money-lending,
  social sectors and local plans. These verbs are not one universal Gram Sabha veto.
- **Inclusion:** Article 243D makes SC/ST seat reservation population-linked,
  reserves not less than one-third of all seats and chairperson offices for women,
  and permits backward-class reservation. State laws providing fifty per cent
  women's reservation are State-specific, not the constitutional national floor.
- **Current evidence:** the Ministry of Panchayati Raj's Devolution Index Report
  2024 remains the latest named national index located on the dated review. The
  Sixteenth Finance Commission award period is 2026-27 to 2030-31; report ratios
  and portal totals remain dated evidence.
- **Ownership boundary:** Topic 23 owns Panchayat institutions and the PESA
  Panchayat interface. Topic 26 owns the Fifth Schedule Governor/TAC/President
  machinery and Sixth Schedule autonomous councils; PESA must not be used to
  erase that distinction.
- **Four-ledger/PYQ control:** direct 2018 finance and 2025 intermediate-tier
  demands plus routed 2019-2024 women, three-F and rural-urban merger demands were
  retained with official-key discipline and cross-owner labels.""",
    24: """### Semantic-completeness ownership and PYQ control

- **Constitutional birth:** the Constitution (Seventy-fourth Amendment) Act, 1992
  inserted Part IXA and the Twelfth Schedule and commenced on 1 June 1993.
  Articles 243P-243ZG and the eighteen Schedule matters are the exact core.
- **Municipal types:** Article 243Q distinguishes Nagar Panchayat, Municipal
  Council and Municipal Corporation and contains the industrial-township proviso.
  State notification and State law determine the actual institutional form.
- **Democratic design:** Articles 243R-243V govern composition, Ward Committees,
  reservation, five-year duration and disqualification. Article 243S requires
  Ward Committees at population three lakh or more; Article 243T fixes the
  constitutional one-third women's floor and population-linked SC/ST reservation.
- **Election and continuity:** Article 243U uses the same before-expiry/within-six-
  months rule and unexpired-term principle; Article 243ZA assigns elections to the
  State Election Commission and Article 243ZG bars ordinary electoral interference.
- **Functional and fiscal limit:** Article 243W and the Twelfth Schedule are
  enabling rather than self-executing. Article 243X permits State-law taxes,
  assignments, grants and funds; Article 243Y uses the Article 243I State Finance
  Commission. Constitutional existence is not automatic three-F devolution.
- **Planning precision:** Article 243ZD requires at least four-fifths elected
  representation on a District Planning Committee; Article 243ZE requires at
  least two-thirds on a Metropolitan Planning Committee. A metropolitan area is
  ten lakh or more under Article 243P(c); planning committees do not themselves
  control every parastatal, budget or land power.
- **Scope controls:** Articles 243ZB/ZC apply/adapt Part IXA to Union Territories
  and exclude Scheduled/tribal areas subject to the constitutional extension
  route; Article 243ZF governed transition and Article 243ZG the election bar.
- **Current finance:** the Sixteenth Finance Commission covers 2026-27 to
  2030-31 and recommends a 60:40 rural-urban aggregate split, with basic and
  performance components; these are dated grant recommendations, not permanent
  constitutional ratios.
- **Current regulation:** AMRUT 2.0 remains a scheme/reform framework rather than
  constitutional devolution. The SEBI (Issue and Listing of Municipal Debt
  Securities) Regulations, 2015 were amended on 8 July 2026, followed by the
  11 August 2026 implementation circular; municipal bonds remain debt, not own tax.
- **Four-ledger/PYQ control:** direct 2023 functional-financial empowerment and
  routed 2024 rural-urban merger demands were retained. Topic 23 owns rural
  institutions; Topic 26 owns excluded Scheduled/tribal-area architecture.""",
    25: """### Semantic-completeness ownership and PYQ control

- **Part VIII map:** Article 239 provides administration through a President-
  appointed Administrator; Article 239A enables local legislatures/Councils of
  Ministers for specified UTs; Article 239AA constitutionalises Delhi; Articles
  239AB, 239B, 240 and 241 govern breakdown, ordinances, regulations and High Courts.
- **Parliamentary competence:** Article 246(4) lets Parliament legislate on any
  matter for territory not included in a State. A UT legislature therefore
  creates real local accountability without State-equivalent exclusivity.
- **Current classification:** India has eight Union Territories. Delhi, Puducherry
  and Jammu and Kashmir have legislatures; Andaman and Nicobar Islands,
  Chandigarh, Dadra and Nagar Haveli and Daman and Diu, Ladakh and Lakshadweep do not.
- **Administrator rule:** an Administrator/Lieutenant Governor is the President's
  agent rather than a Part VI Governor. Under Article 239(2), a State Governor
  appointed administrator of an adjoining UT acts independently of the State Council.
- **Delhi field:** Article 239AA excludes State List Entries 1, 2 and 18 and
  Entries 64, 65 and 66 insofar as related. The 2018 Constitution Bench makes aid
  and advice the rule and presidential reference exceptional within the allotted field.
- **Delhi services current rule:** the 11 May 2023 Constitution Bench recognised
  elected-government control over services outside reserved fields. Act 19 of
  2023 subsequently created the NCCSA route and statutory LG primacy on
  disagreement; the Act remains operative and its constitutional challenge
  remains unresolved on 5 September 2026.
- **Puducherry model:** Article 239A and the Government of Union Territories Act,
  1963 create a statutory legislature. Section 18 competence covers List II and
  III matters insofar as applicable to Union Territories, subject to Parliament's
  continuing power; Article 239B supplies the ordinance route.
- **J&K model:** the Jammu and Kashmir Reorganisation Act, 2019, effective
  31 October 2019, created J&K as a UT with legislature and Ladakh without one.
  J&K's Assembly field excludes public order and police; unlike Delhi, land is not
  a generally excluded entry. Parliament retains overriding competence.
- **Article 370 judgment limit:** In re Article 370 upheld the 2019 constitutional
  result and Ladakh's UT formation but did not finally adjudicate J&K's conversion
  after the Union's statehood assurance. J&K has an elected Assembly and Council
  of Ministers after the 2024 election but remains a UT on 5 September 2026.
- **Four-ledger/PYQ control:** the direct 2018 Delhi and 2025 J&K Assembly demands
  were preserved with Article/statute/judgment/current-status separation. Topic 22
  owns Article 370/371 doctrine; Topic 26 owns Scheduled/Tribal Areas.""",
}

POLITY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    21: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://doj.gov.in/static/uploads/2026/07/b18601168f894d13fdde14296d79e6b3.pdf",
            "https://api.sci.gov.in/supremecourt/2020/26442/26442_2020_1_1501_64994_Judgement_09-Oct-2025.pdf",
            "https://www.api.sci.gov.in/supremecourt/2020/26442/26442_2020_1_1502_63276_Judgement_12-Aug-2025.pdf",
            "https://ecourts.gov.in/ecourts_home/",
        ],
        "Rechecked 2026-09-05: India has 25 High Courts. The dated DoJ "
        "1 July 2026 snapshot records 1,122 sanctioned, 781 working and 341 "
        "vacant posts. Rejanish K.V. (2025 INSC 1208) is the current direct-"
        "District-Judge eligibility control; no All India Judicial Service exists.",
    ),
    22: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://api.sci.gov.in/supremecourt/2019/29796/29796_2019_1_1501_49019_Judgement_11-Dec-2023.pdf",
            "https://www.jk.gov.in/",
            "https://ladakh.gov.in/",
            "https://www.mha.gov.in/en/divisionofmha/jammu-kashmir-and-ladakh-affairs",
        ],
        "Rechecked 2026-09-05: Articles 371-371J remain operative for their "
        "specified States. Article 370 remains printed but inoperative. J&K "
        "remains a UT with an elected legislature and Ladakh a UT without one; "
        "no Statehood, Sixth Schedule or Article 371-type change has been enacted.",
    ),
    23: (
        [
            "https://legislative.gov.in/constitution-seventy-third-amendment-act-1992",
            "https://www.indiacode.nic.in/show-data?actid=AC_CEN_18_21_00007_199640_1517807323053&sectionId=42808&sectionno=4&orderno=4",
            "https://panchayat.gov.in/en/notice/devolution-index-report-2024-summary/",
            "https://panchayat.gov.in/en/document-category/pesa-rules-framed-by-pesa-states/",
            "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/reports/Vol1-Main-Report.pdf",
        ],
        "Rechecked 2026-09-05: Part IX, the Eleventh Schedule and PESA remain "
        "operative. Devolution Index Report 2024 is the current named national "
        "index located; XVI Finance Commission covers 2026-27 to 2030-31. PESA "
        "extends only to Fifth Schedule Scheduled Areas and uses distinct legal verbs.",
    ),
    24: (
        [
            "https://legislative.gov.in/static/uploads/2025/07/8e3828fa91baa94f3aaa74cdc4152cf2.pdf",
            "https://fincomindia.nic.in/asset/doc/commission-reports/16th-FC/reports/Vol1-Main-Report.pdf",
            "https://mohua.gov.in/offerings/schemes-and-services/details/atal-mission-for-rejuvenation-and-transformation-amrut-IjN5cTMtQWa",
            "https://www.sebi.gov.in/legal/regulations/jul-2026/securities-and-exchange-board-of-india-issue-and-listing-of-municipal-debt-securities-regulations-2015-last-amendment-on-july-08-2026-_102918.html",
            "https://www.sebi.gov.in/legal/circulars/aug-2026/amendment-to-sebi-issue-and-listing-of-municipal-debt-securities-regulations-2015-ilmds-regulations-_103488.html",
        ],
        "Rechecked 2026-09-05: Part IXA and the Twelfth Schedule remain the "
        "constitutional framework. XVI FC covers 2026-31; AMRUT 2.0 is a dated "
        "scheme framework. SEBI municipal-debt regulations were amended on "
        "8 July 2026 with an implementation circular dated 11 August 2026.",
    ),
    25: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.indiacode.nic.in/handle/123456789/1362",
            "https://igr.jk.gov.in/files/J&K%20Reorganisation%20Act,%202019.pdf",
            "https://www.mha.gov.in/MHA1/Par2017/pdfs/par2026-pdfs/LS24032026/5250.pdf",
            "https://api.sci.gov.in/supremecourt/2019/29796/29796_2019_1_1501_49019_Judgement_11-Dec-2023.pdf",
            "https://www.sci.gov.in/latest-orders/",
        ],
        "Rechecked 2026-09-05: India has eight UTs; Delhi, Puducherry and J&K "
        "have legislatures. J&K has an elected government but remains a UT; "
        "Ladakh has no legislature. Act 19 of 2023 remains operative and the "
        "Delhi services constitutional challenge remains unresolved.",
    ),
}


def _topic_map(raw: dict[str, Any]) -> dict[str, Any]:
    topics = raw["topics"]
    if isinstance(topics, list):
        return {row["topic_key"]: row for row in topics}
    return topics


def _repair_current_law(topic_number: int, text: str) -> str:
    text = text.replace("28 August 2026", "5 September 2026")
    text = text.replace("28 Aug 2026", "5 Sep 2026")
    text = text.replace("24 August 2026", "5 September 2026")
    if topic_number == 22:
        text = text.replace(
            "IN RE ARTICLE 370 (2023)",
            "IN RE: ARTICLE 370 OF THE CONSTITUTION (2023)",
        )
    if topic_number == 23:
        text = text.replace(
            "control over local resources, minor forest produce, land-alienation prevention and mandatory consultation before land acquisition/mining",
            "ownership of minor forest produce and specified control over local "
            "resources/land alienation; consultation before land acquisition and "
            "mandatory prior recommendation for minor-mineral licences, leases and concessions",
        )
    if topic_number == 25:
        text = text.replace(
            "*In re Article 370* (2023) upheld the reorganisation but directed",
            "*In re Article 370* (2023) upheld the Article 370 result and Ladakh's "
            "UT formation, but did not finally adjudicate J&K's conversion after "
            "the Union assurance; it directed",
        )
        text = text.replace(
            "PUDUCHERRY | Article 239A + 1963 Act | broad statutory State/Concurrent field.",
            "PUDUCHERRY | Article 239A + 1963 Act | List II/III matters insofar as applicable to UTs.",
        )
        text = text.replace(
            "| ✅ **Puducherry assembly** | **Any** State + Concurrent List subject |",
            "| ✅ **Puducherry assembly** | State + Concurrent List matters insofar as applicable to Union Territories |",
        )
    return text


def _load_authoring_configs() -> dict[str, dict[str, Any]]:
    configs: dict[str, dict[str, Any]] = {}
    directory = ROOT / "upsc-ai-kit" / "manifests" / "retrofits" / "ascii-panel-specs"
    for number in range(21, 26):
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
    if topic_key in {f"polity-{number:02d}" for number in range(1, 26)}:
        deep.deep.deep.deep._normalize_graphical_tree(spec, topic_key)
    return _original_validate_spec(spec)


def enforce_strict_rotation(markdown: str) -> tuple[str, dict[str, Any]]:
    repaired, metrics = _inherited_enforce_strict_rotation(markdown)
    if metrics["count"]:
        return repaired, metrics
    _, area, _ = deep.deep.deep.deep.base.basic_mcq_area(repaired)
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
    rows = manifest["topics"][:25]
    result: list[deep.Topic] = []
    for number, row in enumerate(rows, 1):
        result.append(
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
        )
    expected = [f"polity-{number:02d}" for number in range(1, 26)]
    if [topic.topic_key for topic in result] != expected:
        raise ValueError("Polity manifest topics 01-25 changed or are out of order.")
    return result


def generation_sources(
    topic: deep.Topic,
    record: dict[str, Any],
) -> tuple[str, str]:
    """Use the accepted Polity generation, avoiding a subject-engine topic-21 hook."""
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

    modules = (deep, deep.deep, deep.deep.deep, deep.deep.deep.deep)
    for module in modules:
        module.POLITY_REVIEW_POINTS = combined_points
        module.CANONICAL_OWNER_CONTROLS = combined_controls
        module.POLITY_LIVE_OFFICIAL_SOURCES = combined_sources
        module.CURRENT_AUTHORING_CONFIGS = combined_configs
        module.topics = topics
        module.enforce_strict_rotation = enforce_strict_rotation

    deep.deep.deep.deep.augment_topic_semantic_content = augment_topic_semantic_content
    deep.deep.deep.deep.base.WORKFLOW = "polity-21-25-hostile-semantic-immutable-successor"
    deep.deep.deep.deep.base.SOCIETY_REVIEW_POINTS = combined_points
    deep.deep.deep.deep.base.SOCIETY_LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.deep.deep.base.LIVE_OFFICIAL_SOURCES = combined_sources
    deep.deep.deep.deep.base.CANONICAL_OWNER_CONTROLS = combined_controls
    deep.deep.deep.deep.base.CURRENT_AUTHORING_CONFIGS = combined_configs
    deep.deep.deep.deep.base.topics = topics
    deep.deep.deep.deep.base.generation_sources = generation_sources
    deep.deep.deep.deep._base_build_ascii_spec_iac = (
        deep.deep.deep.deep._base_build_ascii_spec
    )
    deep.deep.deep.deep.base.augment_topic_semantic_content = augment_topic_semantic_content
    deep.deep.deep.deep.base.enforce_strict_rotation = enforce_strict_rotation
    deep.deep.deep.deep.carvaka_flowchart.validate_spec = _validate_polity_graphical_spec


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
