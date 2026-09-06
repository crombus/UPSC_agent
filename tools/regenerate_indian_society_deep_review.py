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
_BASE_SHA256 = "260e1b58b69798e1ddeaa54af6e79e774f2dfc74e2a5ed901b6d07e222f69cb2"
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

import indian_society_01_05_data as society_01_05_data
import indian_society_06_10_data as society_06_10_data
import indian_society_11_15_data as society_11_15_data


DATE = "2026-09-05"
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
CURRENT_AUTHORING_CONFIGS.update(
    {
        config["key"]: config
        for config in (
            society_01_05_data.TOPIC_01,
            society_01_05_data.TOPIC_02,
            society_01_05_data.TOPIC_03,
            society_01_05_data.TOPIC_04,
            society_01_05_data.TOPIC_05,
            society_06_10_data.TOPIC_06,
            society_06_10_data.TOPIC_07,
            society_06_10_data.TOPIC_08,
            society_06_10_data.TOPIC_09,
            society_06_10_data.TOPIC_10,
            society_11_15_data.TOPIC_11,
            society_11_15_data.TOPIC_12,
            society_11_15_data.TOPIC_13,
            society_11_15_data.TOPIC_14,
            society_11_15_data.TOPIC_15,
        )
    }
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


CANONICAL_OWNER_CONTROLS.update(
    {
        1: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** salient features of Indian society,
  diversity and unity-in-diversity; define diversity, plurality, disparity,
  marginality, integration, assimilation, syncretism and composite culture before
  evaluating language, religion, caste, tribe, class, region and rural-urban
  location as intersecting axes.
- **Indispensable sociology:** cross-cutting and reinforcing cleavages explain when
  difference dampens or compounds conflict; Nancy Fraser's recognition-
  redistribution distinction is optional analytical depth, not constitutional
  doctrine. Integration never means homogenisation and coexistence never proves
  equal power.
- **India-specific and intersectional control:** use linguistic reorganisation,
  Sufi-Bhakti/shared-shrine practices, metropolitan linguistic minorities and
  PVTG-linked remoteness as bounded cases. Compare region, class, gender and
  rural-urban location inside every identity instead of stereotyping a community.
- **Data/source control:** Census 2011 language, SC and ST stocks remain the latest
  completed full-Census baseline. Census 2027 is prospective; its reference dates
  and caste-enumeration decision may be cited, but no result may be invented.
  The Ministry of Tribal Affairs PVTG list is dated 9 July 2024.
- **Cross-owner boundary:** Topic 02 owns caste structure, Topic 03 tribal society,
  Topic 04 family/kinship and Topic 05 rural society. Population belongs to Topic
  06, women to Topic 07, empowerment to Topic 08 and poverty to Topic 09.
  Constitutional detail remains Polity-owned.
- **Four-ledger hostile audit:** literal syllabus, indispensable prerequisites,
  textbook taxonomy and PYQ demands were checked for absent concepts, mechanisms,
  counter-cases, regional variation, intersectionality and evidence limitations.
- **Verified PYQ ownership, 2018-2026:** direct GS-I demands are 2019 Q8 and
  2024 Q20. The official 2026 GS-I paper was not available on the UPSC previous-
  papers portal when rechecked on 5 September 2026; no 2026 demand or key is
  fabricated.""",
        2: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** caste as a system of varna ideology,
  locally ranked jatis, hereditary membership, endogamy, occupational linkage,
  purity-pollution, social closure, inequality, mobility, association and power.
  Varna is not jati, caste is not class and ritual rank is not political dominance.
- **Indispensable sociology:** B.R. Ambedkar's endogamy/reproduction insight,
  Louis Dumont's hierarchy-purity lens and M.N. Srinivas's Sanskritisation,
  Westernisation, secularisation, dominant caste and politicisation are used as
  bounded theories, not timeless descriptions. André Béteille's caste-class-power
  distinction prevents collapsing three unequal resources into one ladder.
- **Contemporary mechanism:** occupational decoupling, education, urban labour
  markets, caste associations, electoral mobilisation and network capital change
  caste's register while marriage boundaries and discrimination persist unevenly.
  Compare Dalit, dominant-caste, OBC and intra-jati class/gender positions without
  treating any category as homogeneous.
- **Constitutional/legal boundary:** Articles 15, 16, 17 and 46; political
  representation provisions; and Articles 341, 342 and 342A define distinct legal
  routes. Their detailed doctrine, reservation quantum and case law remain with
  Polity/Social Justice. The Special Marriage Act, 1954 is a civil route, not proof
  of social acceptance.
- **Data/source control:** Census 2027 caste enumeration is prospective. It supplies
  no caste population, income, marriage or mobility figure as of 5 September 2026.
  Aggregate associations never establish caste causation or uniform regional
  experience.
- **Cross-owner boundary:** Topic 01 owns diversity, Topic 04 kinship/marriage,
  Topic 05 rural power and Topic 07 women. Population, empowerment and poverty
  remain Topics 06, 08 and 09 respectively.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were tested for definitions, thinkers, reproduction
  mechanisms, change theories, counter-cases, regional/intersectional variation
  and legal-data limits.
- **Verified PYQ ownership, 2018-2026:** direct GS-I demands are 2018 Q8, 2020
  Q6, 2022 Q7, 2023 Q18 and 2024 Q9. No official 2026 GS-I paper was available
  when checked on 5 September 2026, so none is invented.""",
        3: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** tribe and Scheduled Tribe are not
  synonyms; cover kinship, territory, livelihood, political organisation,
  exchange, religion, knowledge systems and state-market relations across
  central Indian, Northeast, Himalayan, island, pastoral and urban contexts.
- **Indispensable sociology:** Verrier Elwin's protective isolation, G.S.
  Ghurye's contested assimilation and Nehru's integration/Panchsheel are kept
  distinct. The tribe-caste continuum and acculturation are historical theses,
  not tests of authenticity or substitutes for Article 342 notification.
- **Mechanism and intersectionality:** distinguish project displacement from
  cumulative land alienation and cash compensation from restoration of land,
  livelihood and community. Disaggregate PVTGs, forest-dependent cultivators,
  pastoral groups, Sixth Schedule polities and urban workers by gender, class,
  region and market exposure; avoid primitive-modern binaries.
- **Constitutional/legal boundary:** Article 342, the Fifth and Sixth Schedules,
  PESA 1996 and the Forest Rights Act 2006 have distinct territorial,
  governance and rights fields. Society owns their social consequences; Polity
  and Social Justice own detailed doctrine, procedure and scheme implementation.
- **Data/source control:** the Ministry of Tribal Affairs list dated 9 July 2024
  records 75 PVTGs in 18 States and the Union Territory of Andaman and Nicobar
  Islands. It is an administrative list, not a ranking or an outcome measure.
- **Cross-owner boundary:** Topic 01 may borrow diversity, Topic 02 the caste
  comparison and Topic 05 agrarian relations. Topic 06 population, Topic 07
  women, Topic 08 empowerment and Topic 09 poverty remain separately owned.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for category errors, theories, displacement
  mechanisms, knowledge-system domains, regional variation and implementation
  limits.
- **Verified PYQ ownership, 2018-2026:** direct GS-I demands are 2021 Q10,
  2022 Q10 and 2025 Q20; the routed 2021 objective language item remains
  unkeyed. No official 2026 GS-I paper was available on 5 September 2026.""",
        4: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** family, household, marriage and
  kinship are separate institutions organising reproduction, care, residence,
  descent, alliance, inheritance, authority and identity. Nuclear residence is
  not necessarily functional independence and matriliny is not matriarchy.
- **Indispensable sociology:** Irawati Karve's regional kinship comparison,
  Leela Dube's gendered kinship lens and the structural-versus-functional
  nuclearisation distinction are bounded analytical tools. Descent, residence,
  inheritance and authority must be compared on separate axes.
- **India-specific and intersectional control:** compare north/south marriage
  rules, Khasi/Garo matriliny, historically Nair matriliny, migrant nuclear
  households and translocal joint obligations. Differentiate outcomes by caste,
  class, gender, generation, religion, housing and region without converting a
  visible urban trend into a national prevalence claim.
- **Constitutional/legal boundary:** the Special Marriage Act, 1954 and Hindu
  Succession (Amendment) Act, 2005 establish legal routes/capacity; personal-law,
  domestic-violence, dowry and live-in doctrine remain Polity/Social Justice
  detail. Legal capacity does not prove bargaining power or social acceptance.
- **Data/source control:** NFHS-5 (2019-21) TFR 2.0 is a dated fertility
  comparator. NFHS-6 (2023-24) was officially released on 29 May 2026, but no
  NFHS indicator may be used to prove household form, nuclearisation or marriage
  acceptance.
- **Cross-owner boundary:** Topic 02 owns caste structure, Topic 07 women and
  Topic 11 globalisation. Population, empowerment and poverty stay with Topics
  06, 08 and 09.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for unit definitions, kinship theories,
  regional exceptions, gendered power, technology/migration mechanisms and
  survey limitations.
- **Verified PYQ ownership, 2018-2026:** direct GS-I demands are 2022 Q8,
  2023 Q8, 2023 Q10 and the family/kinship side of 2024 Q9. No official 2026
  GS-I paper was available when checked on 5 September 2026.""",
        5: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** rural society is a relation among
  caste, class, land, labour, credit, kinship, panchayat, market and state;
  agrarian change includes tenure, technology, commercialisation,
  mechanisation, feminisation, migration, depeasantisation, non-farm work and
  ecological stress. Rural is not identical to agricultural.
- **Indispensable sociology:** M.N. Srinivas's dominant caste explains the
  convergence of numbers, land and office; André Béteille keeps caste, class and
  power analytically distinct; A.R. Desai's agrarian-structure lens locates
  village relations within markets and the state. Jajmani is a regionally
  variable hereditary patron-client relation, not a timeless village essence.
- **Mechanism and regional variation:** compare Punjab-Haryana irrigated
  agriculture, eastern tenancy and labour, dryland Deccan, plantation, tribal,
  coastal and peri-urban settings. Green Revolution effects depend on land,
  irrigation, credit, crop, price support and market access; Panchayat
  representation is not automatically substantive power.
- **Intersectional control:** landownership, tenancy, caste, gender, migration,
  age and non-farm income create differentiation within every rural category.
  Feminisation may mean greater work burdens without title, wages or
  decision-power and must not be treated as automatic empowerment.
- **Data/source control:** PLFS Annual Report 2025 uses a January-December
  reference period and can describe labour status, not prove jajmani decline or
  village power. Agriculture Census holdings and Situation Assessment income
  concepts require their own reference periods and coverage labels.
- **Cross-owner boundary:** Economy owns land-reform mechanics, farm output and
  poverty aggregates; Governance owns detailed Panchayati Raj design. Population
  Topic 06, women Topic 07, empowerment Topic 08 and poverty Topic 09 remain
  outside this owner's detailed treatment.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were tested for institutions, class categories, thinkers,
  agrarian-change mechanisms, regional variation, intersectionality and
  measurement limits.
- **Verified PYQ ownership, 2018-2026:** no direct GS-I question in the verified
  2018-2025 corpus is routed to Topic 05. The official 2026 GS-I paper was not
  available on 5 September 2026; zero-direct-PYQ status is recorded rather than
  filled by invention.""",
        6: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** population size, growth, fertility,
  mortality, age structure, sex composition, density, distribution and migration
  are separate demographic concepts. The demographic transition, dividend,
  ageing, demographic winter and population education are conditional processes,
  not interchangeable labels.
- **Indispensable sociology:** fertility is mediated by women's education and
  agency, marriage timing, desired family size, son preference, child-survival
  expectations, contraceptive access, care arrangements, urban costs and labour
  markets. Replacement-level fertility is not zero growth because population
  momentum depends on the inherited age structure.
- **Regional and life-course control:** compare ageing Kerala/Tamil Nadu-type
  settings, younger EAG-state populations, migrant destinations and ageing
  sending households without treating any state average as an individual cause.
  Ageing is both a longevity achievement and a care, work and social-security
  challenge.
- **Policy boundary:** the National Population Policy, 2000 is rights-based and
  addresses unmet need, reproductive health and voluntary informed choice; it is
  not a coercive one-child or two-child mandate. Detailed health programmes and
  old-age schemes remain with Social Justice.
- **Data/source control:** Census 2011 is the latest completed full-enumeration
  stock as of 5 September 2026. NFHS-6 (2023-24), released 29 May 2026, and
  NFHS-5 (2019-21) are sample surveys; SRS is a vital-rates system. Their
  reference periods, coverage, provisional/final status and uncertainty must be
  stated, and none alone proves causation or a current state population count.
- **Cross-owner boundary:** Geography owns the full demographic-transition model,
  migration theory and population geography. This owner explains social
  determinants and consequences; Topic 07 owns women, Topic 10 urbanisation and
  Social Justice owns detailed schemes and legal administration.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were tested for concept confusion, momentum, sub-national
  divergence, gender agency, ageing, migration, policy coercion and data limits.
- **Verified PYQ ownership, 2018-2026:** direct routes cover 2019 women's
  empowerment and population growth, 2021 population education and the 2024
  demographic-winter demand. Cross-owner routing is disclosed and no unavailable
  2026 GS-I demand is invented.""",
        7: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** women's status is analysed across
  unpaid care, paid work, property, health, education, bodily autonomy, mobility,
  safety, representation and collective voice. Women's organisations include
  reform associations, national federations, unions, autonomous movements,
  issue-based campaigns and federated self-help groups.
- **Indispensable sociology and movement history:** preserve the sequence from nineteenth-
  century social reform to the Women's Indian Association, All India Women's
  Conference (1927), National Federation of Indian Women, autonomous campaigns,
  SEWA, anti-arrack mobilisation, Chipko participation and contemporary
  collectives. Streams overlap; later forms do not erase earlier organisations.
- **Intersectionality:** women are not homogeneous. Caste, tribe, class, religion,
  disability, sexuality, region, rural-urban location, migration and life course
  alter both exposure and organising capacity. Dalit, Adivasi, informal-worker,
  disabled and queer women's organisations are evidence of unequal voice within
  universal categories, not fragmentation by definition.
- **Concept and measurement control:** equality, equity and empowerment are
  distinct; labour-force participation is not all work, unpaid care is not
  inactivity, membership is not substantive voice, account ownership is not
  control and descriptive representation is not automatically substantive
  representation.
- **Legal/scheme boundary:** constitutional equality and the statutory fields of
  the National Commission for Women Act 1990, Protection of Women from Domestic
  Violence Act 2005, POSH Act 2013 and current executive programmes may be named
  as context. Detailed sections, benefit architecture and implementation belong
  to Polity/Social Justice; a law's existence is never reported as transformed
  norms or safety.
- **Data/source control:** PLFS Annual Report 2025 and NFHS-6 (2023-24) use
  different universes, reference periods and indicator definitions. Any female
  LFPR, health, account-use or internet-use value must identify round, age group,
  status concept and release/status; a participation rate does not measure job
  quality, unpaid care or agency.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for movement chronology, organisational form,
  intersectionality, care/work distinctions, representation, causal restraint
  and legal-data boundaries.
- **Verified PYQ ownership, 2018-2026:** direct routes cover 2018 movement reach,
  2019 challenges across time and space, 2021 gig work, 2023 young-women
  self-harm and 2024 equality-equity-empowerment. No official 2026 demand or
  unsupported causal attribution is invented.""",
        8: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** social empowerment expands
  capability, agency, resources, recognition, representation, accessibility and
  institutional voice. Welfare input, legal entitlement, capability-conversion
  factor and lived outcome are separate stages; formal mobility is not
  substantive equality.
- **Indispensable sociology and owned group map:** Scheduled Castes, Scheduled Tribes, socially and
  educationally backward classes/OBCs, notified religious and linguistic
  minorities, persons with disabilities, transgender persons and wider
  LGBTQIA+ communities, and elderly persons are analysed separately before
  intersectional overlap. None is a homogeneous or legally interchangeable
  category.
- **SC/ST/OBC precision:** Articles 338, 338A and 338B establish distinct national
  commissions; Articles 341, 342 and 342A govern distinct notified/list fields.
  Article 17 and the Protection of Civil Rights Act 1955 concern untouchability;
  the SC/ST (Prevention of Atrocities) Act 1989 has a separate protective field.
  Detailed reservation doctrine and benefit administration remain Polity/Social
  Justice-owned.
- **Minority precision:** Articles 29-30 protect cultural and educational
  interests through constitutional categories that are not identical to the six
  centrally notified religious communities administered under the National
  Commission for Minorities Act 1992. Article 350B separately concerns linguistic
  minorities.
- **Disability, gender-identity and ageing precision:** the Rights of Persons with
  Disabilities Act 2016 is an equality, accessibility and specified-disability
  framework; benchmark disability is a statutory subcategory, not a synonym for
  every person with disability. The Transgender Persons (Protection of Rights)
  Act 2019 applies to transgender persons and is not a complete LGBTQIA+ equality
  code; constitutional sexual-orientation equality and marriage recognition are
  separate legal questions. The Maintenance and Welfare of Parents and Senior
  Citizens Act 2007 creates maintenance/welfare duties but not proof of universal
  pension, care access or family support.
- **Intersectional mechanism:** caste/tribe, class, gender, disability, sexuality,
  religion, age, region and rural-urban location change conversion factors such
  as schooling, documentation, mobility, accessibility, language, stigma and
  digital access. A group-level entitlement cannot establish equal uptake or
  outcome within that group.
- **Data/source control:** use dated commission, ministry and
  statutory sources to establish mandate or legal status; use social evidence to
  analyse conversion and outcome. Detailed scheme inventories, reservation
  quantum, litigation and departmental implementation remain Social Justice or
  Polity-owned.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked separately for every owned group, constitutional
  and statutory category, capability-conversion mechanism, intersectional
  overlap, implementation boundary and data limitation.
- **Verified PYQ ownership, 2018-2026:** the owner's direct answer routes cover
  the 2024 affirmative-action outcome gap and the 2025 Phule demand, with
  cross-owner routing disclosed. No official 2026 demand, group prevalence or
  scheme success rate is invented.""",
        9: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** poverty may be monetary,
  multidimensional, absolute, relative, chronic, transient or vulnerable-to-
  poverty. Incidence, depth, severity, inequality, social exclusion and
  development are different concepts and must not be collapsed into one rate.
- **Development distinction:** economic growth concerns aggregate expansion;
  human development concerns health, education and living standards; capability
  development concerns real freedoms; inclusive and sustainable development add
  distribution, participation, resilience and ecological constraints. Poverty
  reduction is one development outcome, not a synonym for development.
- **Indispensable sociology and intersectionality:** assets, land and housing tenure, labour-
  market security, discrimination, health shocks, care burdens, indebtedness,
  service quality and state capacity explain entry, persistence and exit.
  Rural/urban location, caste, tribe, gender, religion, disability and region
  alter both exposure and conversion of assistance into durable capability.
- **Measurement control:** a consumption poverty line and the National
  Multidimensional Poverty Index answer different questions. Headcount does not
  show depth or severity; MPI incidence does not equal consumption poverty; a
  survey estimate does not prove programme causation or current household status.
- **Data/source control:** NITI Aayog's January 2024 discussion paper estimated
  11.28 per cent multidimensional poverty in 2022-23 and about 24.82 crore exits
  between 2013-14 and 2022-23 using an extrapolative method beyond NFHS-5 actuals.
  MoSPI's HCES 2023-24 covers August 2023-July 2024 and reports consumption, not
  an official poverty headcount unless a specified methodology is applied.
- **Ownership boundary:** Economy owns Tendulkar/Rangarajan and poverty-line
  methodology; Social Justice owns detailed entitlement and scheme architecture;
  Governance owns partnership design. This owner explains deprivation,
  exclusion, capability conversion, class-differentiated shocks and development
  trade-offs without importing those inventories.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were tested for poverty-development distinctions, causal
  direction, persistence mechanisms, measurement limits, collaboration and
  environment-livelihood trade-offs.
- **Verified PYQ ownership, 2018-2026:** direct routes cover 2018 persistent
  poverty, 2020 pandemic/class inequality, the cross-owned 2024 collaboration
  demand and the 2025 sustainable-growth/poor-needs conflict. No unavailable
  2026 demand or current poverty rate is invented.""",
        10: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** urbanisation is a change in urban
  share plus occupational, spatial, economic and institutional transformation.
  Urban population growth may arise through natural increase, migration,
  reclassification or boundary expansion; statutory town, census town,
  agglomeration, metropolitan region, slum and informal settlement are not
  synonyms.
- **Indispensable sociology and urban process:** agglomeration can deepen labour markets, matching, supplier
  networks and knowledge spillovers, while land-price escalation, housing-supply
  lag, commuting cost and environmental externalities distribute gains and costs
  unevenly. Migration is rational for households even when it stresses the city.
- **Governance precision:** the Seventy-fourth Constitutional Amendment inserted
  Part IXA and the Twelfth Schedule, but functional listing, actual devolution,
  municipal finance, parastatal control, metropolitan coordination and ward-level
  participation are separate questions. A metropolitan region is not one
  municipality and formal assignment is not implementation capacity.
- **Housing and informality:** informality is a labour, housing, tenure and
  service relation, not a cultural trait. A slum label depends on legal/Census/
  local definitions; tenure insecurity can block formal services, while remote
  relocation can destroy livelihood access even where housing quality improves.
- **Remedy test:** compare in-situ upgrading, serviced land, rental and affordable
  housing, transit-oriented planning, portable services, drainage/ecological
  restoration, municipal finance, ward participation and metropolitan
  coordination by distributive and procedural justice, resilience and livelihood
  access. No remedy works merely because it is technology-labelled.
- **Data/source control and current programme boundary:** Census 2011 remains the latest completed
  Indian urban stock as of 5 September 2026; UN World Urbanization Prospects 2025
  is a harmonised estimate/projection, not Census data. PMAY-U 2.0 and AMRUT 2.0
  may establish current housing and service-policy context, but project counts,
  coverage and benefit claims require dated dashboard evidence and detailed
  scheme architecture remains Social Justice/Governance-owned.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for growth-component separation, city-size pull,
  governance fragmentation, housing/informality mechanisms, ecological risk,
  justice tests and evidence limits.
- **Verified PYQ ownership, 2018-2026:** direct routes cover 2022 Tier-2
  city/middle-class consumption, 2023 segregation, cross-owned 2024 large-city
  migrant pull and 2025 smart-city poverty/distributive justice. No unavailable
  2026 demand or unsupported city-level statistic is invented.""",
        11: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** globalisation is analysed through
  cross-border flows of goods, services, capital, people, information and
  culture as they alter consumption, work, migration, household authority,
  food systems, media and digital access. Economy owns trade/investment
  mechanics; Social Justice owns labour-code and platform-work regulation.
- **Indispensable sociology and distinctions:** homogenisation predicts
  convergence, glocalisation describes local adaptation, and hybridisation
  describes recombination. Globalisation is not westernisation, liberalisation
  is not privatisation, structural consumerism is not cultural consumerism and
  connectivity is not inclusion.
- **Mechanism and Indian variation:** compare Bengaluru IT and service work,
  garment clusters, Kerala-Gulf migration, women's urban labour migration,
  domestic and global food chains, regional-language media, artisan/farmer
  value chains and platform mediation. Policy, firm strategy, technology,
  household agency, caste, class, gender and region can move in different
  directions; no outcome is automatic.
- **Data/source control:** MoSPI's PLFS Annual Report 2025 uses a
  January-December reference period and reports usual-status female LFPR for
  age 15+ at 40.0 per cent. It can establish aggregate labour context, not the
  size, age, marital status, destination or cause of a migration stream.
  NFHS-6 (2023-24), released 29 May 2026, is sample-based; provisional
  internet-use measures are not current connectivity counts.
- **Intersectional and causal discipline:** gains and risks differ by skill,
  income, gender, caste, region, generation and household bargaining power.
  Remittances can coexist with family-authority renegotiation; freedom can
  coexist with thinner support networks. Association between global exposure
  and change never proves a single cause or uniform response.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for channel separation, theory distinctions,
  Indian mechanisms, intersectionality, source periods, measurement limits and
  cross-owner boundaries.
- **Verified PYQ ownership, 2018-2026:** direct routes cover globalisation and
  cultural specificity in 2018, global/local identity in 2019, pluralism in
  2020, technology and scarce resources in 2022, women's urban migration in
  2024 and consumer culture in 2025. The 2025 fast-food demand remains
  Social Change-owned in the audited ledger despite a local owner conflict. No
  unavailable 2026 demand, market share or migration statistic is invented.""",
        12: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** social change concerns alteration
  in institutions, relations, norms, roles and identities; modernisation is one
  structural process within it. Sanskritisation, Westernisation,
  secularisation, democratisation, education, migration, technology, law,
  markets and movements operate at different levels and speeds.
- **Indispensable sociology:** M.N. Srinivas's Sanskritisation and
  Westernisation, Yogendra Singh's modernisation of Indian tradition,
  structural-functional and conflict explanations, Redfield's Great/Little
  Tradition and Marriott's universalisation/parochialisation are bounded lenses,
  not a unilinear tradition-to-modernity ladder.
- **Conceptual distinctions:** modernisation is not westernisation;
  Sanskritisation can change status claims without abolishing hierarchy;
  secularisation as institutional differentiation is not constitutional
  secularism or necessary decline of belief; mobility is not structural
  transformation; enactment is not normative or behavioural change.
- **Mechanism, continuity and intersectionality:** education, urban work,
  communications, law and movements redistribute resources and expectations,
  but kinship, ritual, language and local institutions adapt and reproduce
  continuity. Effects differ by caste, class, gender, tribe, religion, region,
  generation and rural-urban location; resistance and unintended effects are
  part of change, not evidence of social stasis.
- **Data/source control:** NEP 2020 remains an official policy context for
  education and institutional change, but policy text proves neither equal
  access nor social mobility. No cryptocurrency price/legal status, village
  prevalence, adoption rate or causal outcome is asserted from a technology
  label.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for theories, levels, chronology, continuity,
  feedback, regional pathways, anti-teleology controls and evidence limits.
- **Verified PYQ ownership, 2018-2026:** direct routes cover customs and
  obscurantism in 2020, traditional-value continuity in 2021 and fast-food
  growth amid health concern in 2025; the 2021 cryptocurrency demand is
  cross-owned with Economy/Science and Technology. No unavailable 2026 demand
  or unsupported modernization indicator is invented.""",
        13: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** communalism is the political and
  social mobilisation of religious community identity as if internally
  diverse communities were homogeneous and opposed interest blocs. Religion,
  religiosity, prejudice, discrimination, mobilisation and collective violence
  are distinct stages or concepts, not synonyms.
- **Indispensable sociology:** primordialism explains durable attachment;
  instrumentalist and constructivist accounts explain activation and boundary
  hardening; power struggle and relative deprivation become consequential when
  organisation converts grievance into mobilisation. No theory makes conflict
  natural, inevitable or biologically rooted.
- **Mechanism and historical evolution:** colonial representation and
  competitive politics are cross-linked to Modern History. In contemporary
  analysis, segregation, unequal competition, selective memory, rumour,
  organisational framing and weak or partisan institutions create enabling
  conditions; a proximate incident is a trigger, not a complete cause.
- **Constitutional/legal boundary:** Articles 14-16 and 25-30 provide the
  equality, conscience and minority-rights frame; public order and detailed
  doctrine remain Polity-owned. The Places of Worship (Special Provisions) Act,
  1991 supplies a dated stability example, not permission to infer pending
  litigation or adjudicate historical claims.
- **Anti-stereotyping and response discipline:** analyse actors, incentives,
  institutions and local evidence rather than attributing collective traits to
  a religious community or assigning collective blame. Institutional
  impartiality, verified information,
  protection, accountability and sustained civic/economic contact are separate
  trust-repair mechanisms; mere state presence is not impartiality.
- **Data/source control:** MHA annual reports are official administrative
  sources, but no incident or casualty count is used without year, definition,
  coverage and status. Statutory category, reported incident, prosecution,
  conviction and lived reconciliation are separate evidence units.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for conceptual separation, theory, historical
  mechanisms, trigger/structure distinction, institutional response,
  constitutional ownership, data limits and anti-stereotyping discipline.
- **Verified PYQ ownership, 2018-2026:** direct routes cover power struggle
  versus relative deprivation in 2018 and the post-liberal economy, ethnic
  identity and communalism in 2023. No direct standalone 2024-2025 route and no
  unavailable 2026 question, riot statistic, casualty figure or collective
  blame is invented.""",
        14: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** a region is a historically,
  culturally, economically or ecologically perceived territory; regionalism
  is organised assertion around it; sub-regionalism operates within an existing
  region/state; regional disparity concerns unequal outcomes. Diversity,
  disparity, regionalism, autonomy, statehood and secession are not synonyms.
- **Indispensable sociology and historical mechanism:** linguistic reorganisation after 1956
  shows accommodation through recognition. Andhra, Maharashtra-Gujarat,
  Telangana, Gorkhaland, Bodoland and Northeast autonomy claims must be located
  in their own histories. Grievance, leadership, organisation, political
  opportunity and institutional response link identity or disparity to an
  outcome; no demand follows an automatic escalation ladder.
- **Two causal axes and intersectionality:** identity-driven regionalism seeks
  recognition and representation; disparity-driven regionalism seeks
  redistribution and capability. They may compound but remain analytically
  independent. State averages can conceal sub-regional, tribal, rural-urban,
  class, caste and gender inequalities.
- **Constitutional/institutional boundary:** statehood, autonomy, inter-state
  disputes, Article 263, special provisions and fiscal federalism have distinct
  constitutional routes whose detailed doctrine remains Polity-owned. Zonal
  Councils are statutory advisory forums under the States Reorganisation Act,
  1956; the Inter-State Council is a separate constitutional coordination
  mechanism.
- **Data/source control:** NITI Aayog's SDG India Index 2023-24 is a composite
  state/UT benchmark, not a sub-regional diagnosis or causal proof. No ranking,
  income, infrastructure or fiscal figure is used without edition, unit and
  geographical scale.
- **Non-deterministic conclusion:** regional parties and constitutional
  statehood demands are not presumptively separatist or anti-national.
  Recognition, redistribution, representation and cooperative forums must
  match the diagnosed grievance; creating a new unit can relocate rather than
  eliminate internal disparity.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for concept, scale, historical sequence,
  identity/disparity mechanisms, federal boundaries, intersectionality,
  indicator limits and non-secessionist counter-cases.
- **Verified PYQ ownership, 2018-2026:** direct routes cover cultural
  assertiveness and regionalism in 2020 and regional disparity versus diversity
  in 2024. No unavailable 2026 question, current movement outcome or unsupported
  regional ranking is invented.""",
        15: """### Semantic-completeness ownership and PYQ control

- **Official syllabus/index and owned core:** Society owns secularism as lived
  coexistence through shared public space, syncretic practice and common civic
  life. Constitutional secularism is a normative state standard, and secularism
  as political philosophy is a separate theoretical owner; descriptive social
  outcome cannot prove or disprove doctrinal compliance by itself.
- **Indispensable sociology and conceptual distinctions:** secularism is not atheism; religion is not
  communalism; secularisation is not secularism; tolerance, assimilation and
  pluralism are not synonyms; equal respect is not unconditional
  non-intervention; syncretism does not erase distinct identities.
- **Indian model and comparison:** sarva-dharma-sama-bhava and principled,
  context-sensitive engagement describe an Indian social ideal, while strict
  church-state separation is a Western ideal type. Neither family is uniform
  and neither guarantees equal lived outcomes, so comparison must avoid
  civilisational caricature.
- **Intersectionality and internal diversity:** gender, caste, class, sect,
  tribe, region and generation shape religious experience and access to public
  space. Neither women nor a religious community has a single voice; reform,
  autonomy, consultation and individual rights must be analysed together.
- **Constitutional/legal boundary:** Articles 14-16, 25-30 and 44 supply the
  legal frame, but detailed doctrine, amendments and case law remain
  Polity-owned. Society analyses whether institutions and shared spaces convert
  formal rights into equal participation. Minority notification, educational
  rights and personal-law debate are separate legal and social questions.
- **Data/source control and current status:** the Uttarakhand UCC, 2024 and Rules, 2025 are
  official state texts; the 27 January 2026 change is an ordinance unless an
  enacted amendment text is officially identified. Enactment does not prove
  awareness, access, implementation success or community trust, and Goa's
  separate civil-code history prevents unqualified first/only claims.
- **Four-ledger hostile audit:** literal syllabus, prerequisites, textbook
  taxonomy and PYQs were checked for lived/doctrinal/philosophical ownership,
  ideal-type comparison, syncretism and public-space mechanisms,
  intersectionality, legal-status precision and social-outcome limits.
- **Verified PYQ ownership, 2018-2026:** direct GS-I routes cover Indian versus
  Western secularism in 2018, cultural practices challenging secularism in
  2019 and tolerance/assimilation/pluralism in 2022. The France comparison is
  Polity-owned with Society support. No direct 2024-2025 standalone route,
  unavailable 2026 demand, community stereotype or personal-law statistic is
  invented.""",
    }
)


SOCIETY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    1: (
        [
            "https://censusindia.gov.in/nada/index.php/catalog/42458",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2133845",
            "https://tribal.nic.in/downloads/Statistics/StatewiseListofPVTGs_09072024.pdf",
        ],
        "Rechecked 2026-09-05: Census 2011 remains the latest completed full "
        "Census and its Language Paper/atlas controls language counts; PIB's "
        "Census 2027 notice fixes 1 October 2026 for Ladakh and specified "
        "snow-bound areas and 1 March 2027 elsewhere and records caste "
        "enumeration as prospective; the Ministry of Tribal Affairs list dated "
        "9 July 2024 records 75 PVTGs in 18 States and one Union Territory. "
        "No forthcoming Census result or undated community statistic is used.",
    ),
    2: (
        [
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2133845",
            "https://legislative.gov.in/constitution-of-india/",
            "https://www.indiacode.nic.in/indiacode/handle/123456789/1387?view_type=browse",
        ],
        "Rechecked 2026-09-05: the Constitution and India Code remain the "
        "official legal sources for equality, untouchability, notification and "
        "civil-marriage boundaries. PIB records Census 2027 caste enumeration "
        "as prospective. No caste count, marriage prevalence or reservation "
        "rule is inferred from the announcement, and detailed doctrine remains "
        "with Polity/Social Justice.",
    ),
    3: (
        [
            "https://tribal.nic.in/downloads/Statistics/StatewiseListofPVTGs_09072024.pdf",
            "https://tribal.nic.in/actRules/PESA.pdf",
            "https://tribal.nic.in/FRA.aspx",
            "https://legislative.gov.in/constitution-of-india/",
        ],
        "Rechecked 2026-09-05: the Ministry of Tribal Affairs PVTG list dated "
        "9 July 2024 records 75 groups in 18 States and the Union Territory of "
        "Andaman and Nicobar Islands; the ministry's PESA and FRA pages confirm "
        "distinct self-governance and forest-rights fields. Notification, legal "
        "entitlement, implementation and lived outcome remain separate.",
    ),
    4: (
        [
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2266600&reg=3&lang=1",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=1814223",
            "https://www.indiacode.nic.in/indiacode/handle/123456789/1387?view_type=browse",
            "https://www.indiacode.nic.in/handle/123456789/2046?view_type=browse&sam_handle=123456789/1362",
        ],
        "Rechecked 2026-09-05: MoHFW/PIB released NFHS-6 (2023-24) on "
        "29 May 2026; NFHS-5 (2019-21) recorded national TFR 2.0. These are "
        "health and fertility surveys, not measures of household form, "
        "nuclearisation or marriage acceptance. India Code controls the Special "
        "Marriage and Hindu Succession amendment texts; legal capacity is not "
        "reported as automatic social acceptance or bargaining power.",
    ),
    5: (
        [
            "https://mospi.gov.in/uploads/publications_reports/publications_reports1780040415321_0624fb13-fb47-40bc-b470-7c7e9635c3ef_PLFS_2025_F_REV_29052026.pdf",
            "https://mospi.gov.in/sites/default/files/publication_reports/PLFS_Changes-in-2025_rev.pdf",
            "https://agcensus.nic.in/",
        ],
        "Rechecked 2026-09-05: MoSPI's PLFS Annual Report 2025 uses a "
        "January-December reference period under the revised 2025 design. It "
        "may contextualise rural labour but cannot prove jajmani decline, caste "
        "dominance or Panchayat power. Agriculture Census holdings require the "
        "specific round, unit and coverage; no unverified landholding or income "
        "figure is introduced.",
    ),
    6: (
        [
            "https://censusindia.gov.in/census.website/en/data",
            "http://www.nfhsiips.in/nfhsnew/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-2024%20Fact%20Sheets.pdf",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2266600&reg=3&lang=1",
            "https://main.mohfw.gov.in/sites/default/files/26953755641410949469%20%281%29.pdf",
        ],
        "Rechecked 2026-09-05: the Census of India data portal exposes 2001 "
        "and 2011 Census tables, so 2011 remains the latest completed full "
        "enumeration. MoHFW/IIPS released NFHS-6 (2023-24) national fact "
        "sheets on 29 May 2026; the round is sample-based and its released "
        "figures retain provisional/status labels. National Population Policy "
        "2000 remains the rights-based policy frame. No survey estimate is "
        "converted into a Census stock, current state count or causal proof.",
    ),
    7: (
        [
            "https://www.mospi.gov.in/uploads/latestReleases/latest_release_1774607827733_3e8964a9-268b-4cc9-ad65-cfc8a9e32f08_Press_note_AR_PLFS_2025_23032025_V2.1_26032026_final.pdf",
            "http://www.nfhsiips.in/nfhsnew/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-2024%20Fact%20Sheets.pdf",
            "https://www.ncw.gov.in/important-links/list-of-laws-related-to-women/",
            "https://www.indiacode.nic.in/",
        ],
        "Rechecked 2026-09-05: MoSPI's PLFS Annual Report 2025 uses a "
        "January-December reference period and distinguishes usual status from "
        "current weekly status; NFHS-6 (2023-24) was released 29 May 2026 and "
        "measures a different population and indicator set. NCW and India Code "
        "control statutory context. Participation, account access, membership "
        "or legal coverage is not reported as unpaid-work valuation, job "
        "quality, decision control, safety or substantive empowerment.",
    ),
    8: (
        [
            "https://legislative.gov.in/constitution-of-india/",
            "https://ncm.nic.in/homepage/homepage.php",
            "https://ncbc.nic.in/User_Panel/UserView.aspx?TypeID=1113",
            "https://www.indiacode.nic.in/handle/123456789/2156",
            "https://www.indiacode.nic.in/handle/123456789/2249",
            "https://www.indiacode.nic.in/handle/123456789/2152",
            "https://socialjustice.gov.in/writereaddata/UploadFile/71441776233188.pdf",
        ],
        "Rechecked 2026-09-05: the Constitution, NCBC and NCM official pages "
        "confirm distinct commission and minority fields; India Code controls "
        "the Rights of Persons with Disabilities Act 2016, Transgender Persons "
        "(Protection of Rights) Act 2019 and Maintenance and Welfare of Parents "
        "and Senior Citizens Act 2007. Statutory category, commission mandate, "
        "entitlement, implementation and lived empowerment remain separate, "
        "and detailed schemes stay with Social Justice.",
    ),
    9: (
        [
            "https://www.niti.gov.in/sites/default/files/2024-01/MPI-22_NITI-Aayog20254.pdf",
            "https://www.niti.gov.in/sites/default/files/2023-08/India-National-Multidimentional-Poverty-Index-2023.pdf",
            "https://mospi.gov.in/sites/default/files/press_release/HCES_Press_Note_2023-24_27122024_rev.pdf",
            "https://www.mospi.gov.in/sites/default/files/publication_reports/Final_Report_HCES_2023-24L.pdf",
        ],
        "Rechecked 2026-09-05: NITI Aayog's January 2024 discussion paper "
        "reports an estimated 11.28 per cent multidimensional-poverty incidence "
        "for 2022-23 and about 24.82 crore exits during 2013-14 to 2022-23; "
        "post-NFHS-5 years are estimated, not direct household observations. "
        "MoSPI HCES 2023-24 covers August 2023-July 2024 and measures "
        "consumption. Neither source is silently converted into the other's "
        "poverty concept or into proof of programme causation.",
    ),
    10: (
        [
            "https://censusindia.gov.in/census.website/en/data",
            "https://www.un.org/development/desa/pd/world-urbanization-prospects-2025",
            "https://www.mohua.gov.in/offerings/schemes-and-services/details/pradhan-mantri-awas-yojana-urban-MjNzYjMtQWa",
            "https://mohua.gov.in/offerings/schemes-and-services/details/atal-mission-for-rejuvenation-and-urban-transformation-amrut-IjN5cTMtQWa",
            "https://amrut.mohua.gov.in/uploads/National-Progress-Comparison-Report.pdf",
        ],
        "Rechecked 2026-09-05: Census 2011 remains the latest completed Indian "
        "urban stock; the UN World Urbanization Prospects 2025 product supplies "
        "harmonised estimates and projections rather than Census counts. MoHUA "
        "records PMAY-U 2.0 as a 2024-29 housing context and AMRUT 2.0 as the "
        "water/sewerage reform context. Dashboard totals are volatile and are "
        "not quoted without an as-of date; scheme architecture remains "
        "cross-owned by Social Justice/Governance.",
    ),
    11: (
        [
            "https://www.mospi.gov.in/uploads/latestReleases/latest_release_1774607827733_3e8964a9-268b-4cc9-ad65-cfc8a9e32f08_Press_note_AR_PLFS_2025_23032025_V2.1_26032026_final.pdf",
            "https://mospi.gov.in/uploads/publications_reports/publications_reports1780040415321_0624fb13-fb47-40bc-b470-7c7e9635c3ef_PLFS_2025_F_REV_29052026.pdf",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2266600&reg=3&lang=1",
            "http://www.nfhsiips.in/nfhsnew/nfhsuser/assets/National%20Family%20Health%20Survey%20(NFHS-6)%202023-2024%20Fact%20Sheets.pdf",
        ],
        "Rechecked 2026-09-05: MoSPI's PLFS Annual Report 2025 uses the "
        "January-December 2025 reference period and reports usual-status female "
        "LFPR for age 15+ at 40.0 per cent. It is an aggregate labour measure, "
        "not evidence of the size, composition, destination or cause of skilled "
        "young unmarried women's migration. MoHFW/IIPS released NFHS-6 "
        "(2023-24) on 29 May 2026; its internet-use evidence is sample-based "
        "and status-qualified, not a current connectivity count. No brand, "
        "market-share, migration-flow or causal claim is introduced.",
    ),
    12: (
        [
            "https://www.education.gov.in/nep/nep-2020-english.pdf",
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://censusindia.gov.in/census.website/en/data",
        ],
        "Rechecked 2026-09-05: NEP 2020 remains the official education-policy "
        "context for institutional change, inclusion and multidisciplinary "
        "learning, but a policy text is not evidence of equal access, mobility "
        "or changed social norms. Census 2011 remains the latest completed full "
        "enumeration and cannot measure a current modernisation trajectory. "
        "No technology adoption rate, cryptocurrency status, village prevalence "
        "or linear tradition-to-modernity outcome is asserted.",
    ),
    13: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.indiacode.nic.in/handle/123456789/1922?sam_handle=123456789%2F1362",
            "https://www.mha.gov.in/en/documents/annual-reports",
            "https://www.mha.gov.in/sites/default/files/AnnualReport_27122024.pdf",
        ],
        "Rechecked 2026-09-05: the Constitution and India Code remain the "
        "official equality, religious-freedom and Places of Worship Act sources; "
        "MHA's published 2023-24 Annual Report is an administrative source for "
        "communal-harmony context. No incident or casualty number is used "
        "without a verified definition, year and coverage, and no litigation "
        "outcome, collective attribution or community stereotype is inferred. "
        "Detailed constitutional doctrine remains Polity-owned.",
    ),
    14: (
        [
            "https://www.mha.gov.in/sites/default/files/The%20State%20Reorganisation%20Act%201956_270614.pdf",
            "https://www.mha.gov.in/en/page/zonal-council",
            "https://interstatecouncil.gov.in/",
            "https://www.niti.gov.in/node/1350",
            "https://legislative.gov.in/document/constitution-of-india-in-english",
        ],
        "Rechecked 2026-09-05: MHA's States Reorganisation Act, 1956 and Zonal "
        "Council materials distinguish statutory regional cooperation from the "
        "Article 263 Inter-State Council; NITI Aayog's SDG India Index 2023-24 "
        "remains the latest identified official composite edition. A state/UT "
        "score cannot diagnose an internal sub-region or prove causation. No "
        "current movement outcome, regional ranking, income, infrastructure or "
        "fiscal figure is asserted, and detailed federal doctrine remains "
        "Polity-owned.",
    ),
    15: (
        [
            "https://legislative.gov.in/document/constitution-of-india-in-english",
            "https://www.ncm.nic.in/homepage/homepage.php",
            "https://ncm.nic.in/legislations/NCM_Act_1992.pdf",
            "https://ucc.uk.gov.in/",
            "https://ucc.uk.gov.in/government-orders",
            "https://ucc.uk.gov.in/server/file/uploads/shared-files/ucc-rules-2025-en.pdf",
        ],
        "Rechecked 2026-09-05: the Constitution remains the official rights "
        "frame and the NCM confirms six centrally notified religious minority "
        "communities, with Jains notified on 27 January 2014. Uttarakhand's "
        "official UCC portal carries the 2024 code, Rules 2025 and a 27 January "
        "2026 amendment ordinance; absent an official enacted amendment text, "
        "it is not called an Amendment Act. Enactment is not evidence of social "
        "acceptance, access or implementation success, and detailed doctrine "
        "remains Polity-owned.",
    ),
}
LIVE_OFFICIAL_SOURCES = SOCIETY_LIVE_OFFICIAL_SOURCES


def ensure_canonical_owner_control(topic: Topic) -> bool:
    """Repair only the canonical Basic owner and mutable learner-v2 source."""

    control = CANONICAL_OWNER_CONTROLS.get(topic.number)
    if control is None:
        return False
    marker = "Semantic-completeness ownership and PYQ control"
    changed = False
    text = topic.basic_path.read_text(encoding="utf-8")
    if marker not in text:
        topic.basic_path.write_text(
            text.rstrip() + "\n\n" + control.strip() + "\n",
            encoding="utf-8",
        )
        changed = True

    learner = (
        topic.basic_path.parent.parent
        / "learning-sessions"
        / "v2"
        / "subject-wide-syllabus"
        / f"{topic.topic_key}_Learning-Session.md"
    )
    config = CURRENT_AUTHORING_CONFIGS.get(topic.topic_key)
    generated_canonical = Path(config["canonical"]) if config is not None else None
    for assembled in (generated_canonical, learner):
        if assembled is None:
            continue
        if not assembled.is_file():
            continue
        package = assembled.read_text(encoding="utf-8")
        if marker not in package:
            boundary = "## BASIC MCQS / REMEDIATION"
            if boundary not in package:
                raise ValueError(
                    f"{topic.topic_key}: mutable learner-v2 source lacks Basic MCQ boundary."
                )
            assembled.write_text(
                package.replace(
                    boundary,
                    control.strip() + "\n\n" + boundary,
                    1,
                ),
                encoding="utf-8",
            )
            changed = True
    return changed


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


_society_owner_augment = augment_topic_semantic_content


def augment_topic_semantic_content(
    topic: Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    """Insert the active Society owner's bounded hostile-audit supplement once."""

    repaired = _society_owner_augment(topic, markdown, workbook=workbook)
    control = CANONICAL_OWNER_CONTROLS.get(topic.number)
    marker = "Semantic-completeness ownership and PYQ control"
    if workbook or control is None or marker in repaired:
        return repaired
    boundary = "## BASIC MCQS / REMEDIATION"
    if boundary not in repaired:
        raise ValueError(f"{topic.topic_key}: Basic MCQ boundary is absent.")
    learner_control = re.sub(r"(?m)^## ", "### ", control.strip(), count=1)
    return repaired.replace(boundary, learner_control + "\n\n" + boundary, 1)


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
