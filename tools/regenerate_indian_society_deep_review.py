"""Deep-review and immutably regenerate all 15 Indian Society topics."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import textwrap
import time
from collections import Counter
from pathlib import Path
from typing import Any


_BASE = Path(__file__).with_name("regenerate_indian_art_culture_deep_review.py")
_BASE_SHA256 = "06ad0dfdb82fb84b12dc0e1634fe4c2c2b6dac50c20a3d15f5e0f520de3a7d21"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The Indian Art and Culture pattern changed. Review and repin it before "
        "running the Indian Society workflow."
    )

_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]
for _old, _new in (
    ("Indian-Art-and-Culture", "Indian-Society"),
    ("indian-art-and-culture", "indian-society"),
    ("Indian Art and Culture", "Indian Society"),
    ("INDIAN ART AND CULTURE", "INDIAN SOCIETY"),
    ("indian_art_culture", "indian_society"),
    ("ART_CULTURE_REVIEW_POINTS", "SOCIETY_REVIEW_POINTS"),
    ("E-IAC", "E-SOC"),
    ("MD-IAC", "MD-SOC"),
    ("IAC{", "SOC{"),
    ("IAC01", "SOC01"),
    ('"IAC"', '"SOC"'),
    ("2026-09-01", "2026-09-02"),
    ("1 September 2026", "2 September 2026"),
    ("session_count < 14", "session_count < 15"),
    ("fewer than fourteen sessions", "fewer than fifteen sessions"),
    ("main.count(\"#### VISUAL FIRST\") < 14", "main.count(\"#### VISUAL FIRST\") < 15"),
):
    if _old not in _source:
        raise RuntimeError(f"Indian Society transformation anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

_old_tests = """    tests = [
        run_unittest("test_regenerate_indian_society_deep_review"),
        run_unittest("test_generate_indian_society_01_02_sequential"),
        run_unittest("test_generate_indian_society_03_04_sequential"),
        run_unittest("test_generate_indian_society_05_sequential"),
        run_unittest("test_generate_indian_society_06_07_sequential"),
        run_unittest("test_generate_indian_society_08_09_sequential"),
        run_unittest("test_generate_indian_society_10_sequential"),
        run_unittest("test_generate_indian_society_11_12_sequential"),
        run_unittest("test_generate_indian_society_13_14_sequential"),
        run_unittest("test_generate_indian_society_15_sequential"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
"""
_new_tests = """    tests = [
        run_unittest("test_regenerate_indian_society_deep_review"),
        run_unittest("test_generate_indian_society_01_sequential"),
        run_unittest("test_generate_indian_society_02_sequential"),
        run_unittest("test_generate_indian_society_03_sequential"),
        run_unittest("test_generate_indian_society_04_sequential"),
        run_unittest("test_generate_indian_society_05_sequential"),
        run_unittest("test_generate_indian_society_06_sequential"),
        run_unittest("test_generate_indian_society_07_sequential"),
        run_unittest("test_generate_indian_society_08_sequential"),
        run_unittest("test_generate_indian_society_09_sequential"),
        run_unittest("test_generate_indian_society_10_sequential"),
        run_unittest("test_generate_indian_society_11_sequential"),
        run_unittest("test_generate_indian_society_12_sequential"),
        run_unittest("test_generate_indian_society_13_sequential"),
        run_unittest("test_generate_indian_society_14_sequential"),
        run_unittest("test_generate_indian_society_15_sequential"),
        run_unittest("test_v2_section_indexes"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
"""
if _old_tests not in _source:
    raise RuntimeError("Transformed Indian Society test anchor is missing.")
_source = _source.replace(_old_tests, _new_tests, 1)
exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


DATE = "2026-09-02"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "indian-society--subject-wide-syllabus.json"
)
COMMON_CHRONOLOGY = (
    ROOT / "upsc-ai-kit" / "knowledge" / "Indian-Society" / "00_Master-Framework.md"
)
SOCIETY_TEST_MODULES = tuple(
    f"test_generate_indian_society_{number:02d}_sequential"
    for number in range(1, 16)
)


SOCIETY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Indian society is plural, stratified and relational: language, religion, caste, tribe, class, gender, region, rural-urban location and migration overlap, while constitutional citizenship and institutions create unity without erasing difference.",
        "Diversity is not inequality, pluralism is not assimilation, integration is not homogenisation, and coexistence is not proof of equal power; intersectionality explains combined disadvantages without treating every identity combination as identical.",
        "Use Census 2011 language/religion baselines, the notified PVTG position and named regional examples with source-date-status labels; neither harmony nor conflict is timeless, and correlation between diversity and marginality is not sufficient causation.",
    ),
    2: (
        "Caste joins varna ideology, locally ranked jatis, endogamy, hereditary occupation, purity-pollution, social closure and power; Sanskritisation, dominant caste, secularisation, politicisation and caste-class mobility explain change without implying disappearance.",
        "Varna is not jati, caste is not class, ritual rank is not identical to economic or political power, untouchability is not every caste inequality, and constitutional Scheduled Caste status is a legal-administrative category rather than a complete sociological map.",
        "Articles 15-17, 46, 330-342A and reservation institutions set legal boundaries, but legal prohibition does not equal social eradication; compare Jat, Maratha, Patidar, Dalit and regional caste dynamics without homogenising communities or inferring causes from aggregate correlations.",
    ),
    3: (
        "Tribal societies must be analysed through kinship, territory, livelihood, political organisation, exchange, religion and state-market interfaces, with isolation, assimilation, integration, dispossession, migration and self-governance treated as historically variable processes.",
        "Scheduled Tribe, tribe, indigenous people, Particularly Vulnerable Tribal Group and forest dweller are not synonyms; Fifth Schedule, Sixth Schedule, PESA 1996 and Forest Rights Act 2006 have distinct territorial, institutional and rights boundaries.",
        "Use central Indian, Northeast, Himalayan, island and pastoral examples, including Bhil, Gond, Santhal, Naga and PVTG variation; avoid primitive-versus-modern binaries, and distinguish notified status, statutory entitlement, implementation and lived outcome.",
    ),
    4: (
        "Family, household, marriage and kinship are separate but connected institutions organising reproduction, care, property, residence, descent, alliance and identity; nuclearisation, migration, education, work and law alter functions more than they simply dissolve families.",
        "Family is not household, joint is not necessarily co-resident, monogamy is not gender equality, patriarchy is not identical across communities, and patriliny, matriliny, patrilocality, matrilocality, inheritance and authority must be compared on separate axes.",
        "Use Hindu Succession reform, personal-law and Special Marriage Act boundaries with Khasi/Garo, Nair, north Indian and south Indian kinship variation; legal capacity and formal equality must not be reported as automatic bargaining power or social acceptance.",
    ),
    5: (
        "Rural society combines caste, class, land, labour, credit, kinship, panchayat, market and state relations; agrarian change follows tenure reform, Green Revolution, mechanisation, commercialisation, feminisation, migration, non-farm diversification and ecological stress.",
        "Rural is not agricultural, landowner is not cultivator, farmer is not only title-holder, productivity is not income, agricultural labour is not bonded labour, and Panchayati Raj representation is not the same as effective decision-making power.",
        "Contrast Punjab-Haryana, eastern India, dryland Deccan, plantation, tribal and peri-urban regions; use Agriculture Census, Situation Assessment and labour data with period/coverage labels, and treat technology-policy correlations as mechanisms requiring land, water, market and power analysis.",
    ),
    6: (
        "Population analysis separates size, growth, fertility, mortality, age structure, sex composition, density, distribution, migration and human capability; demographic transition and dividend are conditional processes shaped by health, education, gender agency and employment.",
        "Population growth is not fertility, replacement fertility is not zero growth, density is not pressure, sex ratio at birth is not overall sex ratio, Census stock is not survey flow, and demographic dividend is an opportunity rather than an automatic bonus.",
        "Census 2011 is the latest completed census baseline as of review, while SRS, NFHS-5 and projections have different dates and methods; compare Kerala/Tamil Nadu ageing, EAG-state youth and migration destinations without causal claims from state averages alone.",
    ),
    7: (
        "Women's status is produced through patriarchy, caste, class, tribe, religion, region, disability and life course across care, work, property, education, health, bodily autonomy, representation and collective action; women's organisations range from reform associations to unions, SHGs and movements.",
        "Women are not a homogeneous category, labour-force participation is not total work, unpaid care is not inactivity, descriptive representation is not substantive empowerment, and protective law is not implementation or transformed social norms.",
        "Use SEWA, Kudumbashree, Self-Employed Women's Association, anti-arrack, Chipko participation and constitutional/statutory institutions with named regional variation; distinguish NFHS/PLFS source periods and avoid attributing outcomes to one scheme without a mechanism.",
    ),
    8: (
        "Social empowerment means expanding capabilities, voice, resources, recognition, representation, legal agency and institutional access for groups facing structural exclusion; redistribution, recognition, participation and autonomy are complementary but not interchangeable routes.",
        "Welfare is not empowerment, formal inclusion is not substantive access, equality is not uniform treatment, reservation is not the whole of social justice, and constitutional rights, statutory commissions, executive schemes and community institutions have different mandates.",
        "Analyse SC, ST, OBC, minority, disability, transgender, elderly and other experiences without merging them; use Articles 14-17, 21, 38, 46 and relevant commissions/laws precisely, separating entitlement, implementation, uptake and outcome.",
    ),
    9: (
        "Poverty is multidimensional deprivation in income or consumption, nutrition, health, education, housing, services, security and agency; development changes capabilities and structural opportunities, while vulnerability describes exposure to falling into or remaining in deprivation.",
        "Absolute is not relative poverty, poverty is not inequality, incidence is not depth or severity, multidimensional indices are not interchangeable with consumption lines, and programme coverage is not proof of adequacy, access or durable exit.",
        "Use Tendulkar/Rangarajan history, NITI Aayog's National MPI and official survey dates/status carefully; map rural, urban, regional, caste, tribe and gender variation, and distinguish correlation from mechanisms such as assets, labour markets, discrimination, health shocks and state capacity.",
    ),
    10: (
        "Urbanisation is a rising urban share plus economic, occupational, spatial and institutional transformation; migration, natural increase, reclassification and boundary expansion produce different growth paths, while informality mediates housing, work, services and citizenship.",
        "Urbanisation is not urban population growth, statutory town is not census town, slum is not every informal settlement, metropolitan region is not one municipality, and Smart Cities, AMRUT, PMAY-U and municipal constitutional functions have distinct mandates.",
        "Compare Delhi-NCR, Mumbai, Bengaluru, Surat, Chennai and Kerala's dispersed settlement; source Census 2011 classifications and current mission status separately, and explain congestion, segregation or flooding through land, infrastructure, ecology and governance rather than city size alone.",
    ),
    11: (
        "Globalisation intensifies cross-border flows of capital, goods, services, people, information and culture, producing glocalisation, consumption change, labour-market restructuring, care chains, diaspora networks and uneven bargaining power.",
        "Globalisation is not westernisation, liberalisation is not privatisation, cultural diffusion is not homogenisation, hybridity is not equal exchange, and aggregate growth or connectivity does not establish inclusion, causation or uniform local response.",
        "Use IT-Bengaluru, garment clusters, Kerala-Gulf migration, platform work, food/media hybridity and farmer/artisan value chains with sector and region qualifications; distinguish policy chronology, firm strategy, technology and household agency.",
    ),
    12: (
        "Social change alters institutions, relations, norms and identities through Sanskritisation, westernisation, secularisation, modernisation, democratisation, education, technology, migration, social movements and state action; continuity and change coexist at different speeds.",
        "Modernisation is not westernisation, secularisation is not necessarily declining belief, Sanskritisation is not structural equality, mobility is not transformation of the hierarchy, and legal reform is not identical to normative or behavioural change.",
        "Use M.N. Srinivas and Yogendra Singh as bounded analytical frameworks, alongside education, media, urban and movement examples; avoid linear tradition-to-modernity teleology and identify feedback, resistance, regional paths and unintended effects.",
    ),
    13: (
        "Communalism politicises religious identity by representing internally diverse communities as bounded, homogeneous and opposed interest blocs; its mechanisms include elite competition, historical narratives, segregation, rumours, organisational mobilisation and institutional failures.",
        "Religion is not communalism, religiosity is not violence, communal identity is not internally homogeneous, prejudice is not automatically collective violence, and secular constitutional regulation is not hostility to religion.",
        "Use colonial representation and post-Independence examples with constitutional Articles 14-16, 25-30 and public-order boundaries; analyse triggering events separately from enabling structures, avoid collective blame, and distinguish legal norms, enforcement and social reconciliation.",
    ),
    14: (
        "Regionalism is political, economic or cultural mobilisation around territory and perceived interests; it can deepen federal representation and cultural recognition or become exclusionary when joined to unequal development, resource competition and insider-outsider politics.",
        "Region is not state, regionalism is not automatically separatism, federal autonomy is not sovereignty, sub-state demand is not secession, and linguistic reorganisation, inter-state disputes, special provisions and local nativism have distinct constitutional routes.",
        "Use Andhra, Maharashtra-Gujarat, Telangana, Gorkhaland, Bodoland, Northeast autonomy and river/resource disputes with historical specificity; distinguish grievance, leadership, mobilisation and outcome, and do not infer separatism from every regional party.",
    ),
    15: (
        "Indian secularism combines equal citizenship, freedom of conscience, principled state engagement and reform of exclusionary practices within a religiously plural society; it is structured by Fundamental Rights, minority protections, public order and constitutional morality.",
        "Secularism is not atheism, equal respect is not unconditional non-intervention, religious freedom is not immunity from health, morality, public order or other rights, and minority educational rights are not a general exemption from regulation.",
        "Use Articles 14-16, 25-30, 44 and relevant constitutional doctrine with precise institutional boundaries; distinguish legal secularism from social outcomes, avoid homogenising religions, and qualify comparisons with strict separation or establishment models.",
    ),
}


def _status_hashes() -> dict[str, str | None]:
    """Hash only Indian Society source owners in the shared dirty workspace."""
    owned = {
        rel(path)
        for topic in topics()
        for path in (
            topic.basic_path,
            topic.canonical_path,
            topic.advanced_path,
            *topic.cross_topic_sources,
            *topic.pyq_sources,
        )
        if path.is_file()
    }
    owned.update(
        rel(path)
        for path in (COMMON_CHRONOLOGY, SYLLABUS_MAPPING, SECTION_MANIFEST)
        if path.is_file()
    )
    return {path: sha256(repo(path)) for path in owned}


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    current_note = provenance.get("current_linkage_note") or (
        "Static sociological mechanisms are separated from volatile counts, rates, "
        "scheme coverage, judgments and implementation claims. Current evidence "
        "requires institution, reference period, release date and status."
    )
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No volatile live claim is necessary for the static sociological core."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Indian Society Basic/Core is answer-complete before optional Advanced depth. |
| Concept method | Define and distinguish the institution, identity, process, legal category and measured indicator before analysis. |
| Sociological method | Structure/institution → mechanism and agency → differentiated group/region outcome → feedback, resistance and qualification. |
| Evidence method | Claim → named Indian community/region/institution/dataset → analysis → source-date-status or causal qualification. |
| Non-homogenisation | Caste, tribe, women, religion, region and rural/urban groups retain internal class, gender, locality and historical variation. |
| Boundary method | Constitutional right, statutory mandate, executive scheme, implementation and lived social outcome remain distinct. |
| Practice contract | Every solved item has demand decoding, a detailed examiner-grade model, executable timed/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Definition discipline:** close concepts and legal-administrative categories share a comparison axis and are never treated as synonyms.
- **Mechanism discipline:** correlation, temporal sequence and aggregate association do not establish causation; identify institutions, incentives, norms, power and agency.
- **Historical discipline:** colonial, constitutional, developmental, liberalisation and contemporary phases are separated without a linear tradition-to-modernity story.
- **Intersectional discipline:** overlapping caste, tribe, class, gender, religion, disability, region and life-course positions are analysed without creating a single homogeneous category.
- **India discipline:** use named communities, movements, institutions, cities, states and regional contrasts without stereotyping or treating one case as nationally representative.
- **Data discipline:** Census 2011, NFHS, PLFS, SRS, Agriculture Census, MPI and scheme claims retain source, reference period, release date, coverage and provisional/final status.
- **PYQ discipline:** repository routing ledgers and locally held papers control wording and metadata; reconstructed wording and unavailable official keys remain labelled.
- **Current-status note, rechecked {DATE}:** {current_note}

**Live/official context sources recorded by the predecessor generation:**

{source_lines}
"""


def _answer_controls(question: str, title: str) -> dict[str, str]:
    marks_match = re.search(r"\b(10|15|20)\s*marks?\b", title + " " + question, re.I)
    marks = int(marks_match.group(1)) if marks_match else 15
    evidence_count = {10: "three", 15: "five", 20: "six to eight"}[marks]
    directive = _directive(question)
    focus = textwrap.shorten(question, width=94, placeholder="…")
    if "prelims" in title.casefold() or re.search(
        r"\boption\b|\bwhich of the following\b", question, re.I
    ):
        return {
            "demand": (
                f"Treat “{focus}” as a definition, category, constitutional boundary, "
                "institution, mechanism and source-date-status problem. Test each statement."
            ),
            "plan": (
                "Fix the comparison axis; separate social category from legal status, "
                "right from institution and scheme from outcome; test the closest "
                "homogenisation, causation or stale-data distractor."
            ),
            "why": (
                "It prevents a familiar label or aggregate statistic from replacing "
                "the exact concept, institutional mandate, mechanism or evidence status."
            ),
            "improve": (
                f"For “{focus}”, state why the nearest distractor fails on definition, "
                "group variation, causation, constitutional boundary, date or status."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "all clauses, a sociological mechanism, historical trajectory, "
            "intersectional and regional variation, named Indian evidence, "
            "constitutional/institutional boundaries and a qualified conclusion."
        ),
        "plan": (
            f"For a {marks}-mark answer, spend about one-sixth of the time decoding "
            f"the directive and drawing the mechanism; define and state a thesis; "
            f"organise {evidence_count} points as claim → named evidence → analysis "
            "→ qualification; compress examples before mechanisms and reserve the "
            "final minute for causation, group variation and legal-outcome limits."
        ),
        "why": (
            "The answer obeys the directive, explains rather than lists, integrates "
            "India-centric evidence and avoids homogenisation, legalism and causal overclaim."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one named "
            "community, region, institution, movement or source-dated dataset and "
            "state what that evidence cannot establish."
        ),
    }


def _detailed_model_answer(block: str, question: str) -> str:
    thesis_match = re.search(
        r"(?is)\*\*Model thesis:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)", block
    )
    conclusion_match = re.search(
        r"(?is)\*\*Qualified conclusion:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)", block
    )
    evidence_match = re.search(
        r"(?is)\*\*Claim\s*→\s*named evidence\s*→\s*analysis\s*→\s*"
        r"qualification:\*\*\s*(.+?)(?=\n\n\*\*Qualified conclusion:|\Z)",
        block,
    )
    solution_match = re.search(
        r"(?is)\*\*Model (?:solution|answer):\*\*\s*(.+?)(?=\n\n\*\*|\Z)", block
    )
    thesis = (
        thesis_match.group(1).strip()
        if thesis_match
        else (
            solution_match.group(1).strip()
            if solution_match
            else f"The answer must resolve the sociological demand in “{question}”."
        )
    )
    conclusion = conclusion_match.group(1).strip() if conclusion_match else thesis
    evidence = (
        re.findall(r"(?m)^\s*[-*]\s+(.+?)\s*$", evidence_match.group(1))
        if evidence_match
        else []
    )
    if not evidence:
        evidence = [
            clean_source_line(line)
            for line in block.splitlines()
            if 45 <= len(clean_source_line(line)) <= 220
            and not line.lstrip().startswith(("**Question:", "**Demand decoding:"))
        ][:5]
    if not evidence:
        evidence = [
            "Define the central concept and separate it from the nearest social or legal category.",
            "Trace the historical and institutional setting instead of assuming a timeless practice.",
            "Explain the norm, incentive, network, power or agency mechanism producing the outcome.",
            "Use one named Indian community, movement, region, institution or source-dated dataset.",
            "Qualify the pattern through intersectionality, regional variation, causation and implementation limits.",
        ]
    body = "\n".join(
        f"{number}. **Claim and named evidence:** {item} "
        "**Analysis:** Connect structure or institution → norm/incentive/power/agency "
        "mechanism → differentiated social outcome → feedback or policy implication. "
        "**Qualification:** State internal group variation, regional/historical scope, "
        "correlation-versus-causation or legal-norm-versus-lived-outcome boundary."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** Neither a constitutional provision, one scheme, "
        "aggregate correlation nor a single community example establishes uniform "
        "implementation, causation or national experience; test institutions, power, "
        "agency, intersectionality, region, period and evidence status.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    topic_map = {topic.topic_key: topic for topic in topics()}
    issues: list[str] = []
    evidence: list[str] = []
    suggestions: list[str] = []
    for row in rows:
        topic = topic_map[row["topic_key"]]
        number = topic.number
        key = topic.topic_key
        generation = row["new_generation"]
        metrics = row["baseline_metrics"]
        issues.extend(
            (
                f"| SOC{number:02d}-001 | high | `{key}` | all four artifacts | "
                "Concept, mechanism, trajectory, intersectionality and regional "
                f"controls | Fresh deep-review control required | E-SOC{number:02d}-001 | "
                f"MD-SOC{number:02d}-001 | closed in g{generation} |",
                f"| SOC{number:02d}-002 | high | `{key}` | solved practice | "
                "Every answer requires demand, detailed model, timed compression, "
                f"marks rationale and improvement | Baseline solved={metrics['question_count']} | "
                f"E-SOC{number:02d}-002 | MD-SOC{number:02d}-002 | closed in g{generation} |",
                f"| SOC{number:02d}-003 | high | `{key}` | MCQs and flows | "
                "Strict A→B→C→D plus independent complete graphical/ASCII reconstruction | "
                f"Baseline MCQs={metrics['mcq_count']}, panels={metrics['flow_panel_count']} | "
                f"E-SOC{number:02d}-003 | MD-SOC{number:02d}-003 | closed in g{generation} |",
            )
        )
        evidence.extend(
            (
                f"| E-SOC{number:02d}-001 | `{key}` | Basic/Core, canonical package, "
                "optional Advanced, master framework and syllabus mapping were hash-locked | "
                f"repository source | `{rel(topic.basic_path)}`; `{rel(topic.canonical_path)}`; "
                f"`{rel(topic.advanced_path)}`; `{rel(COMMON_CHRONOLOGY)}`; "
                f"`{rel(SYLLABUS_MAPPING)}` | repository owners | {DATE} | verified; unchanged |",
                f"| E-SOC{number:02d}-002 | `{key}` | Models distinguish correlation "
                "from causation and legal norms from outcomes, with named Indian evidence "
                f"and source-date-status controls | generated provenance | `{row['validation']}` | "
                f"g{generation} | {DATE} | verified; approval false |",
                f"| E-SOC{number:02d}-003 | `{key}` | Session, workbook, graphical/ASCII "
                "masters, PDFs, hashes, rotation and latest identity agree | generated "
                f"provenance | `{row['validation']}` | g{generation} | {DATE} | verified |",
            )
        )
        suggestions.extend(
            (
                f"| MD-SOC{number:02d}-001 | high | `{key}` | generated session/flows | "
                "Topic-specific sociological review control absent | "
                f"E-SOC{number:02d}-001 | Add definitions, mechanisms, trajectory, "
                "intersectionality, regional variation and evidence limits | Generated only | "
                f"applied g{generation}; canonical owners unchanged |",
                f"| MD-SOC{number:02d}-002 | high | `{key}` | generated practice | "
                f"Per-answer execution controls incomplete | E-SOC{number:02d}-002 | "
                "Repair each model and timed plan without changing verified PYQ wording | "
                f"applied g{generation}; canonical owners unchanged |",
                f"| MD-SOC{number:02d}-003 | high | `{key}` | generated MCQs/flows | "
                f"Rotation and independent flow completeness required | E-SOC{number:02d}-003 | "
                "Regenerate all four agreeing artifacts | Generated only | "
                f"applied and verified g{generation} |",
            )
        )
    append_once(REVIEW_ROOT / "ISSUE-LEDGER.md", "| SOC01-001 |", issues, changed)
    append_once(
        REVIEW_ROOT / "EVIDENCE-LEDGER.md", "| E-SOC01-001 |", evidence, changed
    )
    append_once(
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
        "| MD-SOC01-001 |",
        suggestions,
        changed,
    )


def update_review_tracker(rows: list[dict[str, Any]], changed: set[str]) -> None:
    _base_update_review_tracker(rows, changed)
    tracker = load(REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    topic_map = {topic.topic_key: topic for topic in topics()}
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if result is None:
            continue
        topic = topic_map[item["topic_key"]]
        item["issue_counts"] = {"critical": 0, "high": 3, "medium": 2, "low": 0}
        item["md_change_required"] = False
        item["md_change_ids"] = [
            f"MD-SOC{topic.number:02d}-{index:03d}" for index in range(1, 4)
        ]
        item["evidence_ids"] = [
            f"E-SOC{topic.number:02d}-{index:03d}" for index in range(1, 4)
        ]
        start = _command_start(topic)
        item["reviewer_notes"] = (
            f"Command-start baseline {start['score']}/100; immutable successor "
            f"{result['new_score']}/100. Canonical owners remained hash-locked; "
            "generation-local sociological, answer and dual-flow controls were repaired. "
            "Approval remains false."
        )
    tracker["summary"] = dict(Counter(row["status"] for row in tracker["topics"]))
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def _society_latest_ids(status: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for topic in topics():
        records = [
            row
            for row in status["exports"]
            if row.get("variant") == "learner-v2"
            and row.get("topic_key") == topic.topic_key
        ]
        if not records:
            raise RuntimeError(f"Live status has no record for {topic.topic_key}.")
        result[topic.topic_key] = max(
            records, key=lambda row: int(row.get("generation", 0))
        )["record_id"]
    return result


def _republish_master_library() -> dict[str, Any]:
    """Republish dynamically from a stable snapshot despite unrelated writers."""
    master = load(MASTER)
    selected_keys = [row["topic_key"] for row in master["topics"]]
    if len(selected_keys) != len(set(selected_keys)):
        raise RuntimeError("Full-library republish found duplicate MASTER keys.")
    live_status = load(STATUS)
    subject_ids = _society_latest_ids(live_status)
    snapshot = EXPORTS / f"indian-society-live-status-snapshot-{DATE}.json"
    dump(snapshot, live_status)
    result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=snapshot,
        catalogue_path=(
            ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
        ),
        selected_keys=selected_keys,
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
    if _society_latest_ids(load(STATUS)) != subject_ids:
        raise RuntimeError(
            "An Indian Society identity changed during full-library publication; "
            "re-read live state before publishing."
        )
    manifest = load(repo(result["manifest"]))
    validation = load(repo(result["validation_manifest"]))
    count = len(selected_keys)
    if (
        manifest.get("topic_count") != count
        or validation.get("topic_count") != count
        or validation.get("status") != "passed"
    ):
        raise RuntimeError("The dynamic full-library validation did not pass.")
    review = load(REVIEW_TRACKER)
    review["source_master_created_at"] = load(MASTER)["created_at"]
    dump(REVIEW_TRACKER, review)
    render_review_tracker_markdown(review)
    return result


_inherited_rewrite_command_history = _rewrite_command_history


def _rewrite_command_history() -> None:
    _inherited_rewrite_command_history()
    replacements = {
        "form, chronology, region, terminology,\npatronage and evidentiary controls": (
            "definitions, mechanisms, historical trajectories, intersectionality,\n"
            "regional variation and evidentiary controls"
        ),
        "form, chronology, region, patronage and function": (
            "concept, institution, mechanism, trajectory and differentiated outcome"
        ),
        "monuments, objects, forms, texts, practitioners, communities or institutions": (
            "communities, regions, movements, institutions, constitutional provisions or datasets"
        ),
        "form and patronage to social meaning": "social structure and agency to differentiated outcomes",
        "list-making, essentialism, false continuity and unsupported attribution": (
            "listing, homogenisation, causal overclaim and legal-outcome conflation"
        ),
    }
    paths = [
        REVIEW_ROOT / "reviews" / topic.topic_key / "REVIEW-REPORT.md"
        for topic in topics()
    ]
    paths.extend(
        (REVIEW_ROOT / "batch-reports").glob(f"Indian-Society-Topics-*-{DATE}.md")
    )
    paths.append(
        REVIEW_ROOT / "subject-reports" / f"Indian-Society-Subject-Completion-{DATE}.md"
    )
    for path in paths:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        write_text(path, text)


_inherited_augment_inventory = _augment_inventory_with_git_status


def _augment_inventory_with_git_status() -> None:
    """Retain the validated UTF-8 inventory and verify its NUL twin exactly."""
    _inherited_augment_inventory()
    text_inventory = EXPORTS / f"indian-society-deep-review-{DATE}-changed-files.txt"
    nul_inventory = EXPORTS / f"indian-society-deep-review-{DATE}-changed-files.nul"
    ordered = [
        line
        for line in text_inventory.read_text(encoding="utf-8").splitlines()
        if line
    ]
    if rel(nul_inventory) not in ordered:
        ordered.append(rel(nul_inventory))
    if rel(text_inventory) not in ordered:
        ordered.append(rel(text_inventory))
    ordered = sorted(set(ordered), key=str.casefold)
    missing = [
        path
        for path in ordered
        if path not in {rel(text_inventory), rel(nul_inventory)}
        and not repo(path).is_file()
    ]
    if missing:
        raise RuntimeError(
            "Changed-file inventory contains missing paths: " + ", ".join(missing[:20])
        )
    write_text(text_inventory, "\n".join(ordered))
    nul_inventory.write_bytes(
        b"".join(path.encode("utf-8") + b"\0" for path in ordered)
    )
    payload = nul_inventory.read_bytes()
    if not payload.endswith(b"\0") or payload.count(b"\0") != len(ordered):
        raise RuntimeError("NUL-delimited changed inventory is invalid.")


_society_inherited_main = main


def main() -> int:
    global _INDIAN_SOCIETY_RUN_STARTED_NS
    _INDIAN_SOCIETY_RUN_STARTED_NS = time.time_ns()
    return _society_inherited_main()


if __name__ == "__main__":
    raise SystemExit(main())
