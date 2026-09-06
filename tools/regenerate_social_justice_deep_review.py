"""Deep-review and immutably regenerate all 17 Social Justice topics."""

from __future__ import annotations

import hashlib
import re
import sys
import textwrap
import time
import types
from pathlib import Path
from typing import Any


def _register_legacy_data_shim(name: str, topics: dict[int, object]) -> None:
    module = types.ModuleType(name)
    for number, value in topics.items():
        setattr(module, f"TOPIC_{number:02d}", value)
    sys.modules[name] = module


import social_justice_01_02_data as _sj_01_02
import social_justice_03_04_data as _sj_03_04
import social_justice_05_06_data as _sj_05_06
import social_justice_07_08_data as _sj_07_08
import social_justice_09_10_data as _sj_09_10
import social_justice_11_12_data as _sj_11_12
import social_justice_13_14_data as _sj_13_14
import social_justice_15_16_data as _sj_15_16

_register_legacy_data_shim(
    "social_justice_01_05_data",
    {
        1: _sj_01_02.TOPIC_01,
        2: _sj_01_02.TOPIC_02,
        3: _sj_03_04.TOPIC_03,
        4: _sj_03_04.TOPIC_04,
        5: _sj_05_06.TOPIC_05,
    },
)
_register_legacy_data_shim(
    "social_justice_06_10_data",
    {
        6: _sj_05_06.TOPIC_06,
        7: _sj_07_08.TOPIC_07,
        8: _sj_07_08.TOPIC_08,
        9: _sj_09_10.TOPIC_09,
        10: _sj_09_10.TOPIC_10,
    },
)
_register_legacy_data_shim(
    "social_justice_11_15_data",
    {
        11: _sj_11_12.TOPIC_11,
        12: _sj_11_12.TOPIC_12,
        13: _sj_13_14.TOPIC_13,
        14: _sj_13_14.TOPIC_14,
        15: _sj_15_16.TOPIC_15,
    },
)


_BASE = Path(__file__).with_name("regenerate_governance_deep_review.py")
_BASE_SHA256 = "6efb5306c2ca7f9679eaf33bf57bf7b7a302f0c5678f59dbae0a426a6ef3753c"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The Governance deep-review pattern changed. Review and repin it before "
        "running the Social Justice workflow."
    )

_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]

# Protect path/key/identifier replacements used by the nested Indian Society
# transformation before changing ordinary prose.
for _old, _new in {
    '("Indian-Society", "Governance")': '("Indian-Society", "__SJ_PATH__")',
    '("indian-society", "governance")': '("indian-society", "__sj-key__")',
    '("indian_society", "governance")': '("indian_society", "__sj_ident__")',
}.items():
    if _old not in _source:
        raise RuntimeError(f"Social Justice protected anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

for _old, _new in (
    ("GOVERNANCE_REVIEW_POINTS", "SOCIAL_JUSTICE_REVIEW_POINTS"),
    ("GOVERNANCE_TEST_MODULES", "SOCIAL_JUSTICE_TEST_MODULES"),
    ("GOVERNANCE_LIVE_OFFICIAL_SOURCES", "SOCIAL_JUSTICE_LIVE_OFFICIAL_SOURCES"),
    ("GOVERNANCE_PYQ_STATUS", "SOCIAL_JUSTICE_PYQ_STATUS"),
    ("_GOVERNANCE_RUN_STARTED_NS", "_SOCIAL_JUSTICE_RUN_STARTED_NS"),
    ("_governance", "_social_justice"),
    ("E-GOV", "E-SJ"),
    ("MD-GOV", "MD-SJ"),
    ("GOV{", "SJ{"),
    ("GOV01", "SJ01"),
    ('"GOV"', '"SJ"'),
    ("governance-", "social-justice-"),
    ("governance_", "social_justice_"),
    ("all 16 Governance", "all 17 Social Justice"),
    ("Governance", "Social Justice"),
    ("GOVERNANCE", "SOCIAL JUSTICE"),
    ("governance", "social justice"),
    ("range(1, 17)", "range(1, 18)"),
    ("All 16 Social Justice", "All 17 Social Justice"),
    ("all 16 Social Justice", "all 17 Social Justice"),
    ("sixteen topics", "seventeen topics"),
    ("sixteen", "seventeen"),
    ("16 Social Justice", "17 Social Justice"),
):
    _source = _source.replace(_old, _new)

_source = (
    _source.replace("__SJ_PATH__", "Social-Justice")
    .replace("__sj-key__", "social-justice")
    .replace("__sj_ident__", "social_justice")
)
_stale_start = _source.index('_stale_config_block = """')
_stale_end = _source.index('"""\n_social_justice_config_block', _stale_start)
_stale_source = _source[_stale_start:_stale_end].replace(
    '/ "knowledge" / "Social Justice" /', '/ "knowledge" / "Social-Justice" /', 1
)
_source = _source[:_stale_start] + _stale_source + _source[_stale_end:]
_source = _source.replace(
    "import social_justice_15_16_data as social_justice_15_16_data",
    "import social_justice_15_16_data as social_justice_15_16_data\n"
    "import social_justice_17_data as social_justice_17_data",
    1,
).replace(
    "            social_justice_15_16_data.TOPIC_16,\n",
    "            social_justice_15_16_data.TOPIC_16,\n"
    "            social_justice_17_data.TOPIC_17,\n",
    1,
)
_test_insertion = (
    "_test_anchor + '\\n        "
    'run_unittest("test_generate_social_justice_16_sequential"),\','
)
if _test_insertion not in _source:
    raise RuntimeError("Social Justice topic-17 test insertion anchor is missing.")
_source = _source.replace(
    _test_insertion,
    _test_insertion[:-1]
    + " + '\\n        "
    + 'run_unittest("test_generate_social_justice_17_sequential"),\',',
    1,
)
_dict_start = _source.index(
    "SOCIAL_JUSTICE_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {"
)
_dict_end_marker = "LIVE_OFFICIAL_SOURCES = SOCIAL_JUSTICE_LIVE_OFFICIAL_SOURCES"
_dict_end = _source.index(_dict_end_marker, _dict_start) + len(_dict_end_marker)
_social_justice_live_block = r'''SOCIAL_JUSTICE_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    1: (["https://legislative.gov.in/constitution-of-india/", "https://socialjustice.gov.in/"],
        "Rechecked 2026-09-06: the Constitution and Department of Social Justice and Empowerment remain authoritative starting points; a constitutional value, enforceable right, Directive Principle, statute and executive welfare measure retain distinct legal force."),
    2: (["https://nfsa.gov.in/", "https://www.niti.gov.in/whats-new/national-multidimentional-poverty-index-2023", "https://poshantracker.in/"],
        "Rechecked 2026-09-06: NFSA, NITI Aayog and the official nutrition platform remain the relevant official owners; entitlement, administrative coverage, survey estimate and nutrition outcome require separate dates, denominators and methods."),
    3: (["https://www.mohfw.gov.in/", "https://nha.gov.in/PM-JAY", "https://main.mohfw.gov.in/sites/default/files/9147562941489753121.pdf"],
        "Rechecked 2026-09-06: MoHFW and the National Health Authority remain authoritative programme and policy sources; insurance eligibility, enrolment, service availability, utilisation, quality and financial protection are not interchangeable."),
    4: (["https://www.education.gov.in/nep/about-nep", "https://dsel.education.gov.in/rte", "https://udiseplus.gov.in/"],
        "Rechecked 2026-09-06: the Ministry of Education, RTE materials and UDISE+ remain official sources; policy announcement, statutory duty, enrolment, attendance, retention and learning outcome must be reported separately."),
    5: (["https://wcd.gov.in/", "https://www.indiacode.nic.in/handle/123456789/2104", "https://www.mospi.gov.in/"],
        "Rechecked 2026-09-06: MWCD, India Code and MoSPI remain authoritative for programme, legal and statistical claims; legal protection, reported incidence, labour-force participation and substantive agency are distinct."),
    6: (["https://wcd.gov.in/acts/juvenile-justice-care-and-protection-children-act-2015", "https://www.indiacode.nic.in/handle/123456789/2079", "https://ncpcr.gov.in/"],
        "Rechecked 2026-09-06: MWCD, India Code and NCPCR remain authoritative; age, forum and procedure are statute-specific, and rescue, adjudication, restoration and rehabilitation are separate stages."),
    7: (["https://socialjustice.gov.in/", "https://ncsc.nic.in/", "https://www.indiacode.nic.in/handle/123456789/1920"],
        "Rechecked 2026-09-06: the Department, NCSC and India Code remain official sources; constitutional status, reservation, offence registration, prosecution, relief, rehabilitation and outcome remain distinct."),
    8: (["https://tribal.nic.in/", "https://ncst.nic.in/", "https://tribal.nic.in/FRA.aspx"],
        "Rechecked 2026-09-06: the Ministry of Tribal Affairs, NCST and official FRA materials remain authoritative; ST, PVTG and forest-rights categories, territorial regimes, claim recognition and implementation outcomes must not be conflated."),
    9: (["https://socialjustice.gov.in/", "https://www.ncbc.nic.in/", "https://legislative.gov.in/constitution-of-india/"],
        "Rechecked 2026-09-06: the Department, NCBC and Constitution remain authoritative; OBC identification, EWS eligibility, list competence, creamy-layer doctrine and mobility evidence follow distinct legal and analytical routes."),
    10: (["https://minorityaffairs.gov.in/", "https://ncm.nic.in/", "https://legislative.gov.in/constitution-of-india/"],
         "Rechecked 2026-09-06: the Ministry, NCM and Constitution remain official sources; constitutional minority rights, regulatory power, notified scheme eligibility, institutional jurisdiction and measured outcomes are distinct."),
    11: (["https://depwd.gov.in/acts/", "https://depwd.gov.in/important-documents/", "https://www.swavlambancard.gov.in/"],
         "Rechecked 2026-09-06: DEPwD and UDID remain official sources; disability, benchmark disability, certification, registration, accessibility, reasonable accommodation and realised inclusion are separate claims."),
    12: (["https://socialjustice.gov.in/schemes/37", "https://nsap.nic.in/", "https://mospi.gov.in/"],
         "Rechecked 2026-09-06: the Department, NSAP and MoSPI remain official sources; statutory maintenance, programme eligibility, pension coverage, adequacy, care access and demographic estimates require exact scope and date."),
    13: (["https://transgender.dosje.gov.in/", "https://socialjustice.gov.in/schemes/40", "https://dwbdnc.dosje.gov.in/"],
         "Rechecked 2026-09-06: the national transgender portal, Department and DNT development board remain official sources; identity recognition, certificate access, scheme eligibility and community-specific outcomes are distinct."),
    14: (["https://socialjustice.gov.in/schemes/37", "https://nskfdc.nic.in/en/content/home/namaste", "https://ncsk.nic.in/"],
         "Rechecked 2026-09-06: the Department, NSKFDC/NAMASTE and NCSK remain official sources; statutory prohibition, identification, mechanisation, compensation, rehabilitation, prosecution and eradication are separate stages."),
    15: (["https://labour.gov.in/labour-codes", "https://eshram.gov.in/", "https://www.epfindia.gov.in/", "https://www.esic.gov.in/"],
         "Rechecked 2026-09-06: the Labour Ministry, e-Shram, EPFO and ESIC remain authoritative; enactment, commencement, registration, contribution, eligibility, claim access, portability and adequacy must be qualified separately."),
    16: (["https://mohua.gov.in/", "https://pmay-urban.gov.in/", "https://nfsa.gov.in/portal/One_Nation_One_Ration_Card"],
         "Rechecked 2026-09-06: MoHUA, PMAY-U and NFSA/ONORC remain official sources; urban poverty, slum residence, homelessness and migration are distinct categories, while sanction, completion, occupancy, portability and security are distinct outcomes."),
    17: (["https://dmeo.gov.in/", "https://dbtbharat.gov.in/", "https://pfms.nic.in/SitePages/aboutus.aspx"],
         "Rechecked 2026-09-06: DMEO, DBT Bharat and PFMS remain official sources; allocation, release, expenditure, output, outcome, impact, inclusion error, exclusion error and attribution require separate evidence."),
}
LIVE_OFFICIAL_SOURCES = SOCIAL_JUSTICE_LIVE_OFFICIAL_SOURCES'''
_source = _source[:_dict_start] + _social_justice_live_block + _source[_dict_end:]
_source = _source.replace("5 September 2026", "6 September 2026")
_source = _source.replace(
    "{number: _canonical_social_justice_control(number) for number in range(1, 18)}",
    "{number: _canonical_social_justice_control(number) for number in range(1, 17)}",
    1,
)
exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


DATE = "2026-09-06"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "social-justice--subject-wide-syllabus.json"
)
COMMON_CHRONOLOGY = (
    ROOT / "upsc-ai-kit" / "knowledge" / "Social-Justice" / "00_Master-Framework.md"
)
SOCIAL_JUSTICE_TEST_MODULES = tuple(
    f"test_generate_social_justice_{number:02d}_sequential"
    for number in range(1, 18)
)


SOCIAL_JUSTICE_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Social justice joins equal citizenship, redistribution, recognition, capabilities, participation and dignity; a welfare state must secure enforceable floors and accountable access rather than merely announce benevolent schemes.",
        "Formal equality is not substantive equality, welfare is not charity, inclusion is not assimilation, reservation is not the whole of social justice, and a Directive Principle is not automatically an individually enforceable entitlement.",
        "Map rights-holder, duty-bearer, institution, finance, frontline delivery, grievance, social audit and outcome; distinguish constitutional value, statute, judgment, executive policy, scheme design, coverage and lived implementation.",
    ),
    2: (
        "Poverty, hunger, food insecurity, undernutrition and malnutrition overlap but use different concepts, indicators and denominators; deprivation is produced through income, assets, prices, care, disease, sanitation, discrimination and public-service access.",
        "Poverty incidence is not depth, food availability is not household access, calorie adequacy is not diet quality, stunting is not wasting, NFSA entitlement is not universal nutrition security, and scheme coverage is not nutritional outcome.",
        "Use NFSA, PDS/ONORC, ICDS/Saksham Anganwadi, PM POSHAN, POSHAN evidence and MPI/NFHS data with source, reference period and denominator; trace eligibility, documentation, portability, exclusion, grievance and convergence without inferring causality from headline statistics.",
    ),
    3: (
        "Universal health coverage requires promotive, preventive, curative, rehabilitative and palliative services with financial protection, quality and equity; public health acts on population risks while clinical care treats individual illness.",
        "UHC is not free hospitalisation alone, insurance coverage is not service availability, enrolment is not utilisation, expenditure allocation is not effective spending, and legal recognition of health does not prove equal access or quality.",
        "Map Union-state-local responsibilities, primary care, public hospitals, regulation, workforce, medicines, surveillance, referral, Ayushman Bharat components, grievance and health outcomes; qualify NFHS, NHA and scheme figures by year, unit and denominator.",
    ),
    4: (
        "Education justice spans access, attendance, retention, learning, inclusion, language, safety, digital accessibility, teacher capacity and transition to skills or work across early childhood, school, higher and vocational education.",
        "Article 21A is not a general right to every level of education, enrolment is not attendance or learning, literacy is not education quality, digital provision is not digital access, and human-resource development is not reducible to employability.",
        "Use RTE Act duties, NEP status, Samagra Shiksha, PM POSHAN, scholarships, UDISE+/NAS/ASER with source ownership and limits; trace school mapping, admission, disability accommodation, discrimination, grievance, dropout and learning outcomes.",
    ),
    5: (
        "Gender justice addresses bodily autonomy, violence, health, education, unpaid care, property, work, wages, representation and voice through an intersectional life-course lens; women are rights-holders, not a homogeneous beneficiary category.",
        "Sex is not gender, equality is not identical treatment, protective law is not implementation, labour-force participation is not total work, representation is not substantive power, and a scheme for women is not automatically gender-transformative.",
        "Use constitutional equality, statutory protections, Vishaka and later workplace law, SHGs, care infrastructure and sex-disaggregated NFHS/PLFS evidence with regional variation; map survivor-centred reporting, support, investigation, trial, compensation and institutional accountability.",
    ),
    6: (
        "Child rights integrate survival, development, protection and participation, with the best-interests principle, evolving capacities and age-specific safeguards across nutrition, education, labour, marriage, trafficking, care and juvenile justice.",
        "A child is not defined by one uniform age across every statute, child protection is not institutionalisation, rescue is not rehabilitation, legal prohibition is not eradication, and household poverty cannot justify coercive removal without due process.",
        "Distinguish JJ Act, POCSO, child-labour and marriage laws, RTE and schemes by purpose and age; map child, family, CWC/JJB, police, school, health system, DCPU, court, grievance and rehabilitation with privacy and participation safeguards.",
    ),
    7: (
        "Scheduled Caste justice combines abolition of untouchability, equality, representation, protection from atrocities, socio-economic capability and institutional remedy while recognising internal gender, class, occupation and regional variation.",
        "Article 17 is not the whole field of caste discrimination, constitutional Scheduled Caste status is not a sociological synonym for every Dalit identity, reservation is not welfare, and registration of an offence is not conviction or social eradication.",
        "Use Articles 15-17, 46, reservation provisions, PCR Act, SC/ST PoA Act, NCSC and named dignity safeguards precisely; trace prevention, FIR, investigation, special court, relief, rehabilitation, witness protection, grievance and outcome without converting crime data into unsupported causal claims.",
    ),
    8: (
        "Scheduled Tribe and PVTG policy must connect land, forest, habitat, livelihood, culture, health, education, displacement, self-governance and consent while respecting major regional differences among central Indian, Northeast, Himalayan, island and pastoral communities.",
        "Scheduled Tribe, PVTG, forest dweller and indigenous people are not interchangeable legal categories; Fifth Schedule, Sixth Schedule, PESA and Forest Rights Act have distinct territories, institutions and rights, and welfare delivery is not self-governance.",
        "Use Gram Sabha, habitat/community forest rights, NCST, EMRS and PM-JANMAN only with exact status and scope; map recognition, evidence, claim, verification, appeal, consent/consultation, displacement safeguards and outcomes without homogenising tribes.",
    ),
    9: (
        "OBC, EWS and social mobility analysis separates social and educational backwardness, economic disadvantage, representation, capability, discrimination and intergenerational mobility across different constitutional and policy routes.",
        "OBC is not a synonym for poverty, EWS is not an OBC sub-category, creamy-layer doctrine does not travel identically across every reservation category, a commission recommendation is not automatic inclusion, and mobility is not proof that structural barriers disappeared.",
        "Use Articles 15, 16 and 342A, NCBC, list competence and judicial ceilings/qualifications precisely; map identification, data, notification, eligibility, certificate, grievance, representation and outcomes while avoiding unqualified quota or fiscal claims.",
    ),
    10: (
        "Minority justice combines equal citizenship, freedom of conscience, cultural and educational rights, security, non-discrimination and capability, while religious and linguistic minorities remain internally diverse by gender, class, caste-like stratification, sect and region.",
        "Minority is context- and provision-specific, Article 30 is not immunity from reasonable regulation, religious freedom is not exemption from public order, health, morality or other rights, and welfare schemes do not define constitutional minority status.",
        "Use Articles 14-16 and 25-30, NCM/minority institutions, educational safeguards and named regional evidence with exact jurisdiction; distinguish right, regulation, adjudication, scheme eligibility, discrimination, grievance and outcome without collective stereotyping.",
    ),
    11: (
        "Disability justice follows equality, dignity, autonomy, accessibility, reasonable accommodation, supported decision-making and community participation through a social and rights-based model rather than a charity-only approach.",
        "Impairment is not disability, accessibility is not reasonable accommodation, benchmark disability is not every disability, reservation eligibility is not the entire RPwD Act, and a certificate or portal registration is not substantive inclusion.",
        "Use the RPwD Act, UNCRPD status, commissioners, accessibility standards and UDID with precise scope; trace assessment, certification, accommodation, education/work access, transport/digital design, grievance and remedy while preserving agency and avoiding ableist assumptions.",
    ),
    12: (
        "Ageing policy must integrate income security, health and long-term care, housing, accessibility, protection from abuse, legal capacity, social participation and caregiver support while recognising gender, widowhood, disability, rurality and class differences.",
        "Senior citizen is a statutory or programme category, not a homogeneous condition; pension coverage is not adequacy, family maintenance duty is not a substitute for public responsibility, and institutional care is not the default solution.",
        "Use the Maintenance and Welfare of Parents and Senior Citizens Act, NSAP pensions, health programmes and demographic data with exact age, date and denominator; map access, portability, abuse reporting, tribunals, community care, grievance and outcomes.",
    ),
    13: (
        "Transgender persons, Denotified Tribes, Nomadic Tribes and Semi-Nomadic Tribes require distinct histories, legal categories and policy responses joined by dignity, identity, documentation, livelihood, housing, education, health, mobility and protection from discrimination.",
        "Transgender identity is not limited to medical transition, legal recognition is not social acceptance, DNT is not a constitutional reservation category by itself, nomadic is not homeless, and these communities must not be merged into one generic vulnerable group.",
        "Use NALSA, the Transgender Persons Act/rules, commissions or boards and DNT development measures with exact authority and status; trace self-identification/documentation, eligibility, discrimination, grievance, participation and outcomes with community-specific evidence.",
    ),
    14: (
        "Sanitation justice joins safe infrastructure, water, behaviour, municipal capacity, occupational safety, caste and gender dignity, mechanisation, rehabilitation and accountability across the full containment-to-treatment chain.",
        "Open-defecation-free status is not safely managed sanitation, toilet construction is not sustained use, manual scavenging is legally defined and not identical to every sanitation job, prohibition is not eradication, and a reported count depends on identification method and date.",
        "Use the 2013 prohibition/rehabilitation law, Supreme Court directions, NCSK, NAMASTE/SRMS status and municipal duties precisely; trace identification, liberation, mechanisation, PPE, compensation, rehabilitation, grievance, prosecution and outcome without hiding Safai Karamchari agency.",
    ),
    15: (
        "Labour social security must cover lifecycle and work-related risks across organised, unorganised, migrant, self-employed and platform/gig work, with registration, contribution, benefit portability, financing and enforceable responsibility.",
        "Gig worker is not necessarily an employee, platform registration is not social-security coverage, a code's enactment is not the same as commencement of every provision, occupational welfare is not identical to contributory insurance, and formalisation is not just digitisation.",
        "Use labour codes only with notified/operative status, e-Shram, EPFO/ESIC and state welfare boards with exact coverage; map worker, aggregator/employer, board, government and grievance roles plus eligibility, contribution, portability, claim, appeal and adequacy.",
    ),
    16: (
        "Urban poverty is shaped by insecure work, rent and land markets, service deficits, documentation, mobility and disaster or health shocks; homeless persons and migrant workers have distinct housing, shelter, portability and labour-protection needs.",
        "Urban poor is not synonymous with slum resident, migrant is not necessarily homeless, domicile is not citizenship, shelter occupancy is not housing security, portability is not universal eligibility, and city averages conceal intra-urban deprivation.",
        "Use urban livelihoods, shelters, PMAY-U and ONORC/e-Shram portability with programme-specific status; map origin-destination governments, ULBs, employers, landlords, frontline workers and migrants through documents, access, grievance, social audit and outcomes.",
    ),
    17: (
        "Scheme performance requires a theory of change from need and entitlement through finance, institution, frontline process and output to outcome and impact, with convergence, participation, grievance, social audit and course correction.",
        "Allocation is not release, expenditure is not output, output is not outcome, coverage is not adequacy, dashboard is not evaluation, inclusion error adds ineligible persons while exclusion error leaves eligible persons out, and correlation is not attributable impact.",
        "Use SECC/Census/survey data, DBT, portability, DMEO and named scheme evaluations with source, reference period, denominator and status; test universalism-targeting trade-offs, data minimisation, privacy, authentication failure, federal fragmentation and beneficiary voice.",
    ),
}

CANONICAL_OWNER_CONTROLS.clear()
CANONICAL_OWNER_CONTROLS.update(
    {
        number: _canonical_social_justice_control(number)
        for number in range(1, 18)
    }
)


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No volatile live claim is necessary for the static Social Justice core."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Social Justice Basic/Core is answer-complete before optional Advanced depth. |
| Legal-status boundary | Constitutional value/right, statute, rule, judgment, executive policy, scheme, eligibility rule, implementation and outcome remain distinct. |
| Rights-holder map | Rights-holder → entitlement/need → competent institution/duty-bearer → accountability forum → grievance/appeal/remedy. |
| Delivery chain | Identification → eligibility → documentation → enrolment → finance → frontline access → service/benefit → portability → outcome → audit and correction. |
| Inclusion method | Intersectional caste, tribe, gender, age, disability, religion, occupation, migration and regional variation is retained without homogenising groups. |
| Evidence method | Claim → named India-centric law/institution/scheme/case/dataset → analysis → source, reference period, release date, denominator, status and causal qualification. |
| Dignity and safeguards | Accessibility, privacy, participation, social audit, portability, offline access, due process and protection from stigma or coercion are tested. |
| Practice contract | Every model has demand decoding, detailed examiner-grade answer, executable timed/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Substantive canonical provenance owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Prohibition/outcome discipline:** a legal prohibition, reported case, registration, conviction, rehabilitation measure and lived eradication are different claims.
- **Eligibility discipline:** universal, categorical, means-tested, self-declared, notified-list and residence-linked routes require exact scope; coverage never proves adequacy or access.
- **Reservation discipline:** constitutional basis, beneficiary category, competent list, ceiling, creamy-layer rule, EWS route, horizontal/vertical operation and judicial status are qualified separately.
- **Fiscal discipline:** allocation, release, expenditure, unit cost, beneficiary transfer and outcome are not interchangeable.
- **Data discipline:** retain numerator, denominator, unit, geography, reference period, release date, provisional/final status and survey-versus-administrative character.
- **Causal discipline:** headline change, before-after sequence or cross-state correlation does not establish scheme impact without mechanism and counterfactual limits.
- **PYQ discipline:** exact wording is preserved only when verified; routed or reconstructed demands remain labelled and no model is presented as an official UPSC answer.
- **Current-status note, rechecked {DATE}:** volatile law, scheme, judgment, list, budget and dataset claims retain issuing authority, date and operative/interim/final status.

**Generation-local live/current sources:**
{source_lines}
"""


def _answer_controls(question: str, title: str) -> dict[str, str]:
    marks_match = re.search(r"\b(10|15|20)\s*marks?\b", title + " " + question, re.I)
    marks = int(marks_match.group(1)) if marks_match else 15
    directive = _directive(question)
    focus = textwrap.shorten(question, width=94, placeholder="…")
    if "prelims" in title.casefold() or re.search(
        r"\boption\b|\bwhich of the following\b", question, re.I
    ):
        return {
            "demand": (
                f"Treat “{focus}” as a category, right, authority, eligibility, "
                "implementation, indicator and source-date-status problem; test each statement."
            ),
            "plan": (
                "Fix the legal and measured category; separate entitlement from scheme, "
                "coverage from outcome and prohibition from implementation; eliminate the "
                "nearest group-homogenising, stale-data, denominator or jurisdiction distractor."
            ),
            "why": (
                "It prevents a familiar scheme, group label or headline statistic from "
                "being mistaken for an exact right, operative rule or proven outcome."
            ),
            "improve": (
                f"For “{focus}”, state why the closest distractor fails on category, "
                "authority, eligibility, denominator, causation, date or implementation status."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "every clause, constitutional/statutory/policy distinction, rights-holder and "
            "institution map, eligibility/exclusion and delivery chain, intersectional and "
            "regional variation, named Indian evidence, accountability and qualified conclusion."
        ),
        "plan": (
            f"For {marks} marks, spend one-sixth of the time decoding the directive and "
            "drawing right/need → institution → eligibility → delivery → outcome → remedy; "
            "state a thesis; write four to seven claim → named evidence → analysis → "
            "qualification points; reserve the final minute for dignity, accessibility, "
            "portability, grievance, denominator, fiscal and causal limits."
        ),
        "why": (
            "The answer obeys the directive, explains mechanisms rather than listing schemes, "
            "uses named India-centric evidence and preserves legal, institutional, group, "
            "eligibility, implementation, fiscal, data and outcome distinctions."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest scheme-catalogue point with one named "
            "rights-holder, duty-bearer, eligibility bottleneck, safeguard, grievance route, "
            "process/outcome indicator and source-status qualification."
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
            else f"The answer must resolve the Social Justice demand in “{question}”."
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
        ][:6]
    if not evidence:
        evidence = [
            "Define the vulnerable group, deprivation, right or policy concept and distinguish the nearest legal and measured category.",
            "Identify the constitutional, statutory, judicial or executive basis and the competent Union, state or local institution.",
            "Map rights-holder, household/community context, duty-bearer, frontline worker, provider and accountability forum.",
            "Trace identification, eligibility, documentation, finance, access, portability, grievance, appeal and correction.",
            "Use a named Indian law, judgment, scheme, institution or official dataset with source, date, denominator and status.",
            "Test intersectionality, regional variation, stigma, accessibility, privacy, fiscal adequacy, exclusion and causal limits.",
        ]
    body = "\n".join(
        f"{number}. **Claim and named evidence:** {item} "
        "**Analysis:** Connect right or deprivation → institutional duty and eligibility "
        "rule → frontline implementation → differentiated access and outcome → grievance, "
        "audit or course correction. **Qualification:** State internal group and regional "
        "variation, legal/operative status, denominator, fiscal or causal limit, accessibility, "
        "dignity, privacy, portability or residual exclusion."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** A constitutional promise, prohibition, reservation "
        "provision, scheme catalogue, allocation, registration count or headline statistic "
        "cannot alone establish accessible implementation, adequate benefit, dignity, remedy "
        "or attributable outcome; test eligibility, institutions, frontline capacity, "
        "intersectionality, regional variation, grievance and evidence status.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


_social_justice_driver_main = main


def main() -> int:
    global _SOCIAL_JUSTICE_RUN_STARTED_NS
    _SOCIAL_JUSTICE_RUN_STARTED_NS = time.time_ns()
    return _social_justice_driver_main()


if __name__ == "__main__":
    raise SystemExit(main())
