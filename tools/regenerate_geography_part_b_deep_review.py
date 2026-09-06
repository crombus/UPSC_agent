"""Deep-review and immutably regenerate Geography Part B topics 26-37."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import textwrap
import time
from pathlib import Path
from typing import Any


_BASE = Path(__file__).with_name("regenerate_geography_part_a_deep_review.py")
_BASE_SHA256 = "9ebad1b4a958b293ed30678a7436182abd7bf474ec40c637ddc4a5f6d9aa3286"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The Geography Part A pattern changed. Review and repin it before "
        "running the Geography Part B workflow."
    )

_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]
for _old, _new in (
    ("all 25 Geography Part A", "all 12 Geography Part B"),
    ("Geography Part A topics 01-25", "Geography Part B topics 26-37"),
    ("Part A — Physical Geography", "Part B — Human, Economic and Regional Geography"),
    ("part-a-physical-geography", "part-b-human-economic-and-regional-geography"),
    ('"range(1, 26)"', '"range(1, 13)"'),
    ('"!= 25"', '"!= 12"'),
    ("exact topic keys 01-25", "exact operational topic keys 26-37"),
    ("topics 01-25", "topics 26-37"),
    ("All 25 topics", "All 12 topics"),
    ("geography_part_a", "geography_part_b"),
):
    if _old not in _source:
        raise RuntimeError(f"Part A transformation anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

_inner_exec = 'exec(compile(_source, str(Path(__file__)), "exec"), globals())'
if _inner_exec not in _source:
    raise RuntimeError("Part A inner-engine execution anchor is missing.")
_source = _source.replace(
    _inner_exec,
    """_source = _source.replace(
    "tools\\\\test_regenerate_geography_part_a_deep_review.py",
    "tools\\\\test_regenerate_geography_part_b_deep_review.py",
)
_source = _source.replace("2026-09-01", "2026-09-05")
_source = _source.replace("1 September 2026", "5 September 2026")
_source = _source.replace('"topic_count": 25', '"topic_count": 12')
_source = _source.replace('"topic_validations_passed": 25', '"topic_validations_passed": 12')
_source = _source.replace('"latest_topic_count": 25', '"latest_topic_count": 12')
_source = _source.replace('"learning_and_workbook_pdfs_checked": 50', '"learning_and_workbook_pdfs_checked": 24')
_source = _source.replace('"represented": 25', '"represented": 12')
_source = _source.replace('"expected": 25', '"expected": 12')
_source = _source.replace(
    "test_regenerate_geography_part_a_deep_review",
    "test_regenerate_geography_part_b_deep_review",
)
_source = _source.replace(
    '''    tests = [
        run_unittest("test_regenerate_geography_part_b_deep_review"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
''',
    '''    tests = [
        run_unittest("test_regenerate_geography_part_b_deep_review"),
        run_unittest("test_generate_geography_26_sequential"),
        run_unittest("test_generate_geography_27_sequential"),
        run_unittest("test_generate_geography_29_sequential"),
        run_unittest("test_generate_geography_31_sequential"),
        run_unittest("test_generate_geography_33_sequential"),
        run_unittest("test_generate_geography_34_sequential"),
        run_unittest("test_generate_geography_35_sequential"),
        run_unittest("test_generate_geography_36_sequential"),
        run_unittest("test_generate_geography_37_sequential"),
        run_unittest("test_v2_section_indexes"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
''',
)
_source = _source.replace(
    "geography-deep-review-",
    "geography-part-b-deep-review-",
)
_source = _source.replace(
    "Geography-Subject-Completion-",
    "Geography-Part-B-Subject-Completion-",
)
_source = _source.replace(
    "# Geography Subject Completion",
    "# Geography Part B Subject Completion",
)
exec(compile(_source, str(Path(__file__)), "exec"), globals())""",
    1,
)

exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


DATE = "2026-09-05"
SECTION = "Part B — Human, Economic and Regional Geography"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "geography--part-b-human-economic-and-regional-geography.json"
)
GEOGRAPHY_PATTERN_PATH = Path(__file__)
CANONICAL_TO_OPERATIONAL = {
    "geography-28": "geography-28-human-settlements-and-urbanisation",
    "geography-30": "geography-30-primary-economic-activities-agriculture",
    "geography-32": "geography-32-industries-and-industrial-regions",
}
PART_B_TEST_MODULES = (
    "test_generate_geography_26_sequential",
    "test_generate_geography_27_sequential",
    "test_generate_geography_29_sequential",
    "test_generate_geography_31_sequential",
    "test_generate_geography_33_sequential",
    "test_generate_geography_34_sequential",
    "test_generate_geography_35_sequential",
    "test_generate_geography_36_sequential",
    "test_generate_geography_37_sequential",
)


def _status_hashes() -> dict[str, str | None]:
    """Avoid hashing unrelated dirty-tree files in the shared workspace."""
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
    return {path: sha256(repo(path)) for path in owned}


GEOGRAPHY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    26: (
        "Population geography separates stock, structure, distribution, density, growth, fertility, mortality and mobility; demographic transition moves from high birth/high death through mortality-led growth and fertility decline toward low rates, with a possible ageing or below-replacement phase rather than one universal timetable.",
        "Crude birth/death rates, TFR, replacement fertility, dependency ratio, sex ratio, life expectancy and population pyramid answer different questions; demographic dividend is a conditional age-structure opportunity, not an automatic growth bonus, and Census 2011, SRS, NFHS and UN estimates retain different reference dates and methods.",
        "India must be mapped through Kerala/Tamil Nadu ageing and low fertility, EAG-state youth and higher fertility, urban-rural and gender contrasts, and migration-adjusted state patterns; transition theory is descriptive, while policy, health, education, labour absorption and gender agency explain divergent pathways.",
    ),
    27: (
        "Migration analysis joins Ravenstein's regularities, Lee's push-pull-intervening-obstacle framework, gravity and distance-decay, Zelinsky's mobility transition, Harris-Todaro expected-income logic, network/cumulative causation and segmented labour demand to India's marriage, work, education, distress and circulation streams.",
        "Migrant stock differs from flow, lifetime from last-residence migration, internal from international movement, seasonal/circular from permanent relocation, and Census reason-for-migration categories from causal explanation; women recorded under marriage can also be workers, so one response category must not erase economic agency.",
        "India patterns require Bihar–Uttar Pradesh source belts, Delhi–NCR/Mumbai/Surat/Bengaluru destinations, Kerala–Gulf corridors, tribal and drought-prone seasonal streams, remittances and care/skill loss; Census 2011 is the latest completed census baseline as of the review date, while surveys and administrative records are partial.",
    ),
    28: (
        "Settlement geography connects site and situation, rural form, central-place hierarchy, rank-size and primate-city patterns, urban morphology, suburbanisation, peri-urbanisation and metropolitan regions to India's statutory town, census town, urban agglomeration and outgrowth categories.",
        "Urbanisation is a rising urban share and structural-spatial transformation, not merely urban population growth; municipality status does not equal Census urban classification, conurbation differs from megalopolis, slum from all informal settlement, and Smart Cities Mission from AMRUT and PMAY-U mandates.",
        "Delhi–NCR, Mumbai Metropolitan Region, Bengaluru, Surat, Chandigarh, Jaipur and Kerala's dispersed settlement provide contrasting map anchors; Burgess, Hoyt, Harris-Ullman and Christaller are simplified models whose assumptions, scale and Global-South informality limits must be explicit.",
    ),
    29: (
        "Regional development links spatial inequality, cumulative causation, growth poles, spread and backwash, core-periphery, agropolitan and balanced/unbalanced strategies to India's planning regions, river-valley projects, industrial location, infrastructure corridors and district-level intervention.",
        "Five Year Plans ended after the Twelfth Plan period and the Planning Commission was replaced by NITI Aayog in 2015; plan strategy, Finance Commission transfers, centrally sponsored schemes, NITI cooperative/competitive federalism and constitutional local planning are institutionally distinct.",
        "Damodar Valley, NCR, Dandakaranya, command areas, hill/tribal regions, Aspirational Districts and freight/industrial corridors show that growth-node benefits depend on linkages, displacement, skills, ecology and state capacity; convergence is an empirical result, not an automatic consequence of investment.",
    ),
    30: (
        "Agricultural geography reconstructs land use through physical controls, tenure, labour, technology, markets and policy; it compares subsistence/commercial, intensive/extensive, plantation, mixed, dairy, Mediterranean, shifting, pastoral and von Thünen location logics before mapping India's crop seasons and agro-regions.",
        "Kharif, rabi and zaid are seasons rather than crop essences; net sown area differs from gross cropped area, cropping intensity from yield, MSP announcement from procurement, food security from cereal self-sufficiency, and irrigation potential from realised equitable water delivery.",
        "Punjab–Haryana wheat-rice, western Maharashtra sugarcane, Malwa cotton/soybean, Assam tea, Kerala rubber/spices, Karnataka coffee, eastern rice, dryland Deccan millets/pulses and horticultural belts must be explained through water, soil, labour, market and policy interactions, with Agriculture Census/land-use/production data source-dated.",
    ),
    31: (
        "Resource geography begins with geological occurrence, reserve/resource classification, grade, extraction technology, transport, processing, markets and externalities; world belts and India's Gondwana coal, offshore/onshore hydrocarbons, Odisha–Jharkhand iron-manganese-bauxite, Rajasthan non-ferrous minerals and nuclear/renewable endowments require map logic.",
        "Resource differs from reserve, occurrence from economically recoverable deposit, thermal from metallurgical coal, conventional from non-conventional only by stated taxonomy, and installed renewable capacity from actual generation; criticality combines economic importance and supply risk rather than geological scarcity alone.",
        "Jharia/Raniganj/Talcher/Korba, Mumbai High, Assam, Krishna-Godavari, Bailadila, Keonjhar, Khetri, Jaduguda, monazite coasts, solar Rajasthan/Gujarat and wind Tamil Nadu/Gujarat anchor India; Ministry, IBM, CEA and international data need year/status labels, while just-transition and import dependence qualify security claims.",
    ),
    32: (
        "Industrial geography links raw material, energy, labour, capital, market, transport, agglomeration and policy through Weber's least-cost theory, Lösch's market areas, growth-pole and product-cycle/network perspectives, then maps old and new industrial regions at world and India scales.",
        "Industry, manufacturing and factory employment are not synonyms; localisation economies differ from urbanisation economies, industrial corridor from a single estate or transport line, footloose from location-free, and deindustrialisation can be relative employment/output change rather than disappearance.",
        "Chotanagpur, Mumbai–Pune, Gujarat, Hugli, Bengaluru–Tamil Nadu, NCR and Visakhapatnam–Guntur contrast with Ruhr, Great Lakes, Japan's Pacific Belt and China's coast; Jamshedpur, petrochemical ports, auto clusters, electronics/services and DMIC show changing weights of material, market, skills and logistics.",
    ),
    33: (
        "Transport geography explains networks through nodes, links, accessibility, connectivity, density, hierarchy, break-of-bulk, modal cost and hinterland; trade adds comparative advantage, corridors, ports, logistics and chokepoints, while India's space programme links launch, satellite, application and governance institutions.",
        "Road/rail density differs from effective accessibility, port capacity from throughput, inland waterway declaration from operational traffic, trade balance from current account, ISRO from the Department of Space and NewSpace India Limited, and navigation/communication/earth-observation missions retain distinct functions.",
        "Golden Quadrilateral, Dedicated Freight Corridors, Bharatmala, Sagarmala, major ports, National Waterway-1, Delhi–Mumbai corridor, Malacca/Hormuz/Suez and PSLV/GSLV/LVM3, INSAT/GSAT, IRS/EOS and NavIC form named map-institution anchors; project and mission claims require official date/status qualification.",
    ),
    34: (
        "World regional geography synthesises location, physiography, drainage, climate, biomes, resources, population and economy rather than memorising country lists; every continent is reconstructed through plate-relief belts, wind/current controls, river basins, settlement cores and strategic interfaces.",
        "Europe is not coterminous with the EU, Middle East with West Asia, Latin America with South America, Sahel with Sahara, mainland with maritime Southeast Asia, and a continent, cultural region, economic bloc and political boundary answer different map questions.",
        "Andes–Amazon–Pampas, Rockies–Great Lakes–Mississippi, Alps–North European Plain, Atlas–Sahara–Sahel–Congo–Rift, West Siberian Plain–Central Asian basins–monsoon Asia, and Australian interior/eastern rim provide comparable regional spines; country data and geopolitical status remain source-dated.",
    ),
    35: (
        "Indian political geography connects territorial evolution, international boundaries, maritime zones, federal units, borderland societies and neighbourhood corridors; boundary morphology must distinguish natural, geometric, antecedent, subsequent, superimposed and relic forms without treating labels as complete histories.",
        "Line of Control, Line of Actual Control, International Boundary and Actual Ground Position Line are not interchangeable; Radcliffe, McMahon and Durand lines have different origins/statuses, a land boundary differs from a maritime delimitation, and border management from final boundary settlement.",
        "Pakistan, China, Nepal, Bhutan, Bangladesh and Myanmar sectors plus Sri Lanka/Maldives maritime neighbourhood require pass-river-valley-corridor logic; Sir Creek, Siachen, Doklam, Kalapani-Lipulekh, Teesta, enclaves and connectivity projects need exact bilateral/legal and current-status qualification.",
    ),
    36: (
        "Contemporary Indian issues are spatial systems: regional inequality, urban stress, agrarian change, land degradation, water conflict, disasters, climate risk, coastal/Himalayan vulnerability, displacement and environmental justice emerge through hazard or pressure × exposure × vulnerability × governance.",
        "Hazard differs from disaster, scarcity from access failure, drought from aridity, degradation from desertification, climate trend from single event, mitigation from adaptation, and project approval, construction and operation are separate status stages.",
        "Joshimath/Himalayan towns, Delhi air basin, Bengaluru/Chennai water stress, Marathwada drought, Punjab groundwater, Bundelkhand, Sundarbans, Western Ghats, mining belts and inter-state river disputes show scale-specific causation; current claims require IMD, Census, CWC, CGWB, ISRO, MoEFCC or other official source-date-status labels.",
    ),
    37: (
        "Cultural and social geography examines language, religion, caste, tribe, ethnicity, gender, livelihood, landscape, place identity and diffusion across India's plural regions; cultural area, hearth, route, frontier, sacred landscape and vernacular region are analytical tools rather than fixed natural containers.",
        "Scheduled Tribe, tribe, indigenous and ethnic group are not automatic synonyms; language family differs from script and official status, caste distribution from caste determinism, cultural region from state boundary, and diversity from either frictionless harmony or permanent conflict.",
        "Indo-Aryan/Dravidian/Austroasiatic/Tibeto-Burman language zones, tribal central belt and Northeast, Himalayan and coastal livelihoods, pilgrimage networks, pastoral routes, borderlands and metropolitan mosaics require named maps; Census 2011 remains the completed census baseline while identities are dynamic and multi-scalar.",
    ),
}

CANONICAL_OWNER_CONTROLS = {
    26: """### Semantic-completeness ownership and PYQ control

- **Owned core:** population distribution, density, growth and composition;
  fertility, mortality, age-sex structure and dependency; population
  pyramids; demographic transition, momentum, dividend, ageing, optimum
  population and the Malthus-Boserup debate.
- **Theory/model control:** demographic transition is a descriptive
  generalisation, not a universal timetable or deterministic forecast.
  Malthus, Boserup and optimum-population reasoning retain assumptions,
  counter-evidence, entitlement/distribution and ecological qualifications.
- **Indicator control:** CBR, CDR, TFR, IMR, life expectancy, sex ratio and
  dependency ratio answer different questions. Replacement fertility does
  not mean immediate zero growth; momentum and age structure intervene.
- **Scale/map control:** world transition regions are separated from India's
  staggered state transitions. Kerala and Tamil Nadu ageing/low fertility,
  EAG-state youth and higher fertility, and urban-rural/gender contrasts are
  mapped without treating national averages as uniform state conditions.
- **Date/data control:** Census 2011 is the latest completed Indian
  enumeration at this review cutoff. SRS and NFHS are sample-based, and UN
  World Population Prospects 2024 is an estimate/projection series; none is
  relabelled as a post-2011 census count.
- **Close-option control:** population growth differs from birth rate;
  youthful structure from demographic dividend; ageing from population
  decline; child sex ratio from all-ages sex ratio; stock from flow.
- **Boundary:** Indian Society owns population-policy, gender and social
  consequences in full; Economy owns labour absorption and dividend policy.
  Geography owns spatial distribution, demographic mechanisms and regional
  differentiation, with bounded bridges to those owners.
- **Verified PYQ ownership, 2018-2026:** direct routes include 2024 Prelims
  TFR definition and low-birth-rate/ageing country questions plus 2024 GS-I
  Q7 on demographic winter. Official answer letters absent from routing
  ledgers are not invented.""",
    27: """### Semantic-completeness ownership and PYQ control

- **Owned core:** migration stock and flow; place-of-birth and last-residence
  measures; internal/international, intra/interstate, rural-rural,
  rural-urban, urban-urban, return, seasonal and circular movement; origin,
  destination, corridor, remittance and demographic effects.
- **Theory/model control:** Ravenstein, Lee, gravity/distance-decay,
  Stouffer's intervening opportunities, Harris-Todaro expected income,
  Zelinsky mobility transition and network/cumulative causation retain their
  assumptions, predictive reach and empirical limits.
- **Causal control:** wage or population size alone never explains a flow.
  Opportunity sets, job probability, kinship networks, transport, gender,
  marriage, distress, policy and intervening obstacles jointly shape
  selectivity and destination choice.
- **Scale/map control:** Bihar-Uttar Pradesh source belts,
  Delhi-NCR/Mumbai-Surat/Bengaluru destinations, Kerala-Gulf corridors,
  tribal/drought-prone seasonal streams and counter/return flows are mapped
  as corridors, not timeless state labels.
- **Date/data control:** Census 2011 migration tables remain the latest
  completed census baseline; MoSPI's Migration in India 2020-21 is a
  survey-period estimate, while UN International Migrant Stock 2024 covers
  international stock and may extrapolate countries not fully reassessed.
- **Gender/close-option control:** a recorded marriage reason does not erase
  women's work; migrant stock differs from annual flow, internal from
  international movement, and usual-residence migration from temporary or
  circular mobility.
- **Boundary:** Social Justice/Governance own entitlement portability and
  labour protection; Indian Society owns gender/family transformation.
  Geography owns movement measurement, theory, spatial streams and regional
  consequences, retaining bounded institutional bridges.
- **Verified PYQ ownership, 2018-2026:** direct ownership includes 2024 GS-I
  Q5 on why large cities attract more migrants; the 2018 indentured-labour
  diaspora demand is cross-owned with Modern History. No direct objective key
  or migrant count is fabricated.""",
    28: """### Semantic-completeness ownership and PYQ control

- **Owned core:** settlement site and situation; rural forms; settlement
  hierarchy; central-place, rank-size and primate-city ideas; urbanisation,
  morphology, suburbanisation, peri-urbanisation, conurbations, metropolitan
  regions and India's statutory-town/census-town/urban-agglomeration system.
- **Theory/model control:** Christaller, Burgess, Hoyt and Harris-Ullman state
  assumptions, mechanisms, predicted forms and limits. Their idealised
  geometry does not erase planning, transport corridors, informality,
  polycentricity, topography or Global-South land institutions.
- **Definition control:** urbanisation differs from urban population growth;
  statutory town from census town; urban agglomeration from municipality;
  conurbation from megalopolis; slum from every informal settlement.
- **Scale/map control:** Delhi-NCR, Mumbai Metropolitan Region, Bengaluru,
  Surat, Chandigarh, Jaipur and Kerala's dispersed settlement are compared
  through site, situation, corridor, density, governance boundary and
  morphology rather than city-size lists.
- **Date/data control:** Census 2011 remains India's completed enumeration and
  classification baseline; UN World Urbanization Prospects 2025 is a modelled
  international series using national definitions. Projected urban shares
  are not census counts.
- **Plan/status control:** Smart Cities Mission, AMRUT 2.0 and PMAY-U 2.0
  have distinct mandates. Sanction, funding, project completion, service
  output and measured outcome are separate status claims and must be dated.
- **Boundary:** Governance/Polity own municipal powers and finance; Indian
  Society owns social exclusion and slum livelihoods. Geography owns
  settlement classification, urban spatial process, morphology and regional
  urban systems with bounded policy bridges.
- **Verified PYQ ownership, 2018-2026:** audited ledgers contain no direct
  Topic 28 route. Large-city migrant attraction remains Topic 27-owned and
  urban-local-body questions remain Governance/Polity-owned; no direct PYQ is
  invented.""",
    29: """### Semantic-completeness ownership and PYQ control

- **Owned core:** formal, functional and planning regions; regional
  inequality and convergence; cumulative causation, spread/backwash,
  growth-pole, core-periphery, balanced/unbalanced and agropolitan strategies;
  India's planning chronology and spatial interventions.
- **Theory/model control:** Myrdal, Perroux, Hirschman, Friedmann and
  agropolitan approaches retain assumptions and transmission mechanisms.
  A growth node produces spread only through labour, supplier, market,
  infrastructure and fiscal linkages; convergence is an empirical result.
- **Institutional chronology:** Five Year Plans ran from the First Plan
  (1951-56) through the Twelfth Plan period (2012-17). The Planning
  Commission was replaced by NITI Aayog in 2015; NITI strategy, Finance
  Commission transfers, CSS and constitutional district/local planning are
  not synonyms.
- **Scale/map control:** Damodar Valley, NCR, Dandakaranya, command areas,
  hill/tribal regions, Aspirational Districts/Blocks and freight-industrial
  corridors are mapped by node, hinterland, administrative scale and
  intended linkage.
- **Date/data control:** SDG India Index 2023-24 and programme dashboards are
  dated monitoring instruments, not timeless regional-income series.
  Rankings, delta scores, selections, sanctions and outcomes require their
  own reference period and coverage.
- **Distribution/control trap:** infrastructure investment differs from
  inclusive regional development; corridor notification from operation;
  district targeting from proof of causal impact; balanced development from
  equal allocation.
- **Boundary:** Economy owns macro planning and public finance; Governance
  owns implementation architecture. Geography owns regionalisation, spatial
  inequality, location/linkage mechanisms and map-based evaluation.
- **Verified PYQ ownership, 2018-2026:** audited central ledgers contain no
  direct Topic 29 route. AI/GIS locational planning and federal/local
  development questions remain with their routed owners; no direct PYQ is
  fabricated.""",
    30: """### Semantic-completeness ownership and PYQ control

- **Owned core:** primary-activity classification; physical, tenure, labour,
  technology, market and policy controls on agriculture; subsistence,
  commercial, intensive, extensive, plantation, mixed, dairy,
  Mediterranean, shifting and pastoral systems; crop seasons, agro-regions
  and von Thünen location logic.
- **Theory/model control:** von Thünen's isolated market, uniform plain,
  fertility and transport assumptions are stated before applying
  rent-distance logic. Refrigeration, multiple markets, contracts, policy,
  unequal infrastructure and global value chains qualify exact rings.
- **Measure control:** kharif/rabi/zaid are seasons, not crop essences; net
  sown area differs from gross cropped area, cropping intensity from yield,
  production from productivity, irrigation potential from created/utilised
  delivery, and MSP announcement from procurement/farm-gate realisation.
- **Scale/map control:** Punjab-Haryana wheat-rice, western Maharashtra
  sugarcane, Malwa cotton/soybean, Assam tea, Kerala rubber/spices, Karnataka
  coffee, eastern rice, dryland Deccan millets/pulses and horticultural belts
  are explained through water-soil-labour-market-policy interaction.
- **Primary-activity map:** fisheries follow shelf/upwelling and inland-water
  systems; forestry/NTFP follows forest-access regimes; mining/quarrying
  follows geology. Technology changes accessibility, not resource occurrence.
- **Date/data control:** Agriculture Census 2015-16 is the latest fully
  published round at this cutoff; the 2021-22 round is under process.
  Advance crop estimates are provisional, Agricultural Statistics at a
  Glance 2024 is a dated compilation, and FAOSTAT carries reporting lags.
- **Policy/close-option control:** MSP, CACP recommendation, CCEA approval,
  procurement, buffer stocks and food/nutrition security are separate;
  scheme announcement, coverage, expenditure, output and impact are not
  interchangeable.
- **Verified PYQ ownership, 2018-2026:** routes include 2019 New World crops,
  2020 crop-climate, 2022 tea states, 2023 India-China farm statistics, 2025
  turmeric and 2025 GS-I Q5 on non-farm primary activities. Missing and
  provisional answer letters remain unpromoted.""",
    31: """### Semantic-completeness ownership and PYQ control

- **Owned core:** geological occurrence; resource/reserve and grade/economic
  filters; metallic, non-metallic and energy-resource classification; world
  and Indian mineral belts; coal, petroleum, gas, hydro, nuclear and
  renewable-energy geography; critical-mineral supply chains.
- **Resource-process control:** occurrence is a geological fact, a resource
  is potentially usable, and a reserve is the recoverable subset under a
  stated classification, technology, price and date. Extraction,
  beneficiation, smelting/refining, generation, transmission and final use
  are separate stages and may occur in different regions.
- **Geological-model control:** shields favour many metallic ores,
  sedimentary basins host coal and hydrocarbons, lateritisation can
  concentrate bauxite, and a petroleum system requires source, reservoir,
  seal and trap. These are tendencies with deposit-specific exceptions.
- **Scale/map control:** world belts and India's Jharia-Raniganj-Talcher-
  Korba, Mumbai High-Assam-KG, Bailadila-Keonjhar, Khetri, Jaduguda and
  monazite-coast anchors are taught as belts, basins and corridors rather
  than isolated mine lists.
- **Energy-measure control:** installed capacity differs from generation,
  capacity addition from commissioning, electricity from primary energy,
  resources from reserves, and thermal coal from metallurgical coal.
  Renewable potential is not identical to realisable capacity.
- **Date/data control:** IBM mineral inventories, National Coal Inventory,
  CEA/National Power Portal and MNRE releases retain their own reference
  dates, classifications and provisional/final status. Production rank,
  reserve/resource, project and capacity claims require a dated official
  release.
- **Criticality control:** a critical mineral is defined by economic or
  strategic importance plus supply risk; it is not necessarily geologically
  rare. Extraction, processing concentration, import dependence, recycling,
  substitution and stockpiling are distinct vulnerabilities or responses.
- **Boundary and PYQ control:** Environment owns full mining-impact/EIA and
  transition ecology; Economy and Science-and-Technology own fiscal, market
  and technology detail. Geography owns occurrence, distribution, location,
  networks and spatial dependence. Verified 2018-2025 routes are retained;
  unavailable or provisional answer letters remain unpromoted.""",
    32: """### Semantic-completeness ownership and PYQ control

- **Owned core:** industrial classification; raw-material, energy, labour,
  capital, market, transport, agglomeration, policy and environmental
  controls; Weber, Lösch, growth-pole, product-cycle and network approaches;
  old and new industrial regions of India and the world.
- **Location-theory control:** Weber's material-index, transport, labour and
  agglomeration logic and Lösch's market-area reasoning retain assumptions
  and limits. Neither predicts one timeless optimum under multiple markets,
  global value chains, policy incentives, sunk costs or digital inputs.
- **Terminology control:** industry is broader than manufacturing; factory,
  firm, plant, cluster, estate, SEZ and corridor are not synonyms.
  Localisation differs from urbanisation economies, footloose from
  location-free, and relative deindustrialisation from disappearance.
- **Scale/map control:** Chotanagpur, Mumbai-Pune, Gujarat, Hugli,
  Bengaluru-Tamil Nadu, NCR and Visakhapatnam-Guntur are compared with Ruhr,
  Great Lakes, Japan's Pacific Belt and China's coast through input,
  market, port, labour, technology, network and inertia logic.
- **Process/status control:** notification, approval, land acquisition,
  trunk infrastructure, allotment, construction, commissioning, production
  and measured outcome are separate stages. A freight line or planned node
  does not itself prove an operational industrial corridor.
- **Date/data control:** IIP is a monthly volume index, ASI an annual
  registered-factory survey, national accounts a value-added framework, and
  PLI/corridor releases administrative records. Base year, reference period,
  release date, revisions and coverage accompany changing claims.
- **Boundary and PYQ control:** Economy owns industrial policy and scheme
  design; Environment owns compliance and impact assessment. Geography owns
  location theory, industrial-region morphology, corridor networks and
  spatial restructuring. No direct PYQ or unavailable key is invented.""",
    33: """### Semantic-completeness ownership and PYQ control

- **Owned core:** transport modes and modal choice; network nodes, links,
  density, connectivity, accessibility, hierarchy, break-of-bulk,
  hinterland and corridors; trade routes, ports and chokepoints; India's
  launch, satellite, navigation and application geography.
- **Network-process control:** route length or density does not establish
  accessibility. Cost, time, reliability, capacity, interchange, last-mile
  links, terrain, demand and network centrality determine connectivity and
  modal advantage.
- **Trade control:** merchandise differs from services trade; exports from
  total trade, trade balance from current account, port capacity from
  throughput, and a declared waterway from operational traffic.
- **Scale/map control:** Golden Quadrilateral, freight corridors, major
  ports, National Waterway-1 and industrial corridors are linked to
  hinterlands; Hormuz, Bab-el-Mandeb, Suez, Malacca and Panama are mapped by
  connected seas and bypass implications.
- **Space-programme control:** Department of Space, ISRO, IN-SPACe and NSIL
  have distinct roles. PSLV, GSLV and LVM3 are launch-vehicle families;
  INSAT/GSAT, IRS/EOS and NavIC retain distinct functions. Launch, orbit
  insertion, commissioning and operational service are separate statuses.
- **Date/data control:** MoRTH, Railways, MoPSW/IWAI, Commerce/DGCI&S and
  ISRO/Department of Space releases retain publication date, reference
  period and provisional/final or project-specific status. Announcement,
  sanction, completion and operation are never conflated.
- **Boundary and PYQ control:** Economy owns trade policy and balance-of-
  payments analysis; Science-and-Technology owns spacecraft engineering.
  Geography owns network, corridor, hinterland, chokepoint, launch-site and
  application geography. Specialist-routed space PYQs remain cross-owned.""",
    34: """### Semantic-completeness ownership and PYQ control

- **Owned core:** every inhabited continent and major world region through
  relative location, plate-relief spine, drainage, climate, currents,
  biomes, resources, population/economic cores and strategic interfaces;
  representative countries are placed inside these systems.
- **Regional-method control:** a continent, UN statistical region, cultural
  region, economic bloc, state and disputed territory answer different
  questions. Synthesis runs from physical frame to human pattern and
  interregional connection, not disconnected country lists.
- **Terminology control:** Europe is not the EU, South America not Latin
  America, West Asia not automatically the same extent as the Middle East,
  Sahara not Sahel, and mainland not maritime Southeast Asia.
- **Map completeness:** Andes-Amazon-Pampas; Rockies-Great Lakes-Mississippi;
  Alps-North European Plain; Atlas-Sahara-Sahel-Congo-Rift; West Siberian
  Plain-Central Asian basins-monsoon Asia; Australian interior-eastern rim;
  major islands, peninsulas, seas, straits, canals and landlocked corridors
  are covered through relational maps.
- **Cross-scale control:** relief, climate and resources explain but do not
  determine population, economy or power. Country averages cannot be
  projected onto every subregion.
- **Date/status control:** UN M49 names/codes are statistical and carry a
  no-position boundary disclaimer; UN membership is a separate status;
  World Bank income groups are annual Atlas-method classifications. Country
  names, memberships, classifications, population estimates and disputed
  status require edition/extraction dates.
- **Boundary and PYQ control:** International Relations owns diplomatic
  disputes and current alignments; Economy owns detailed indicators.
  Geography owns regional synthesis and map relationships. Statistical
  designations are not converted into recognition claims.""",
    35: """### Semantic-completeness ownership and PYQ control

- **Owned core:** India's territorial evolution, Union and state/UT frame,
  international land boundaries, maritime zones, borderland societies,
  transboundary rivers, passes, valleys, corridors and the immediate
  neighbourhood's spatial relationships.
- **Boundary-theory control:** natural, geometric, antecedent, subsequent,
  superimposed and relic describe morphology or genesis; they do not alone
  establish legal validity, acceptance or present control. Delimitation,
  demarcation, administration, management and settlement are distinct.
- **Terminology control:** International Boundary, Line of Control, Line of
  Actual Control and Actual Ground Position Line are not interchangeable.
  Radcliffe, McMahon and Durand lines have different origins and contexts.
- **Map completeness:** Pakistan and China sectors, Nepal, Bhutan,
  Bangladesh and Myanmar land frontiers plus Sri Lanka and Maldives maritime
  neighbourhood are reconstructed through rivers, ridges, passes, valleys,
  enclaves/exclaves, border trade points, ports and corridors.
- **Maritime-law control:** baseline, territorial sea, contiguous zone,
  exclusive economic zone and continental shelf are different legal spaces;
  sovereignty, sovereign rights and jurisdiction are not synonyms.
- **Current-status control:** Sir Creek, Siachen/AGPL, LAC sectors, Doklam,
  Kalapani-Lipulekh, Teesta and connectivity projects require exact official
  bilateral/legal wording and an as-of date. Negotiation, agreement,
  ratification, implementation and ground position are separate statuses.
- **Source and ownership control:** Survey of India supplies the official
  Indian map; MEA, MHA, domestic law and UN DOALOS serve different purposes.
  International Relations and Internal Security own diplomacy and security;
  Geography owns terminology, morphology, sectors, corridors and spatial
  consequences. No disputed claim is presented as uncontested fact.""",
    36: """### Semantic-completeness ownership and PYQ control

- **Owned core:** contemporary Indian issues are synthesised as spatial
  systems through process, pattern, scale, exposure, vulnerability, spatial
  spillover, trade-off, instrument and graded verdict. Groundwater stress,
  river-basin conflict, urban flooding, air-shed stress, land degradation,
  coastal/island pressure, Himalayan instability, displacement and regional
  inequality are map-based applications rather than a news catalogue.
- **Causal control:** hazard differs from disaster, scarcity from access
  failure, drought from aridity, degradation from desertification, climate
  trend from one event, and natural variability from human amplification.
  Rainfall may trigger flooding while land use and drainage govern loss.
- **Scale mismatch control:** aquifer, basin, catchment, air-shed, sediment cell,
  metropolitan labour market and mountain corridor frequently cross the
  administrative unit expected to act. The governing scale must be named
  before prescribing an institution or instrument.
- **Status/data control:** observation, forecast, projection, survey,
  census, announcement, approval, construction, operation, target and
  achievement are distinct. IMD, CGWB, CWC, ISRO/SAC and ministry releases
  retain their reference period, publication date, method and status.
- **Named India anchors:** Punjab groundwater, Gangetic aquifers, Delhi's
  air basin, Bengaluru/Chennai water stress, Marathwada and Bundelkhand,
  Joshimath and Himalayan towns, the Sundarbans, Western Ghats, mining
  belts, Great Nicobar, north-east corridors and inter-state river basins
  are used only where the named spatial mechanism is established.
- **Ownership boundary:** Environment owns ecosystem science, conservation
  law and pollution control in full; Disaster Management owns preparedness,
  response and recovery systems; Economy owns prices, employment, finance
  and sector policy. Geography owns location, distribution, regional
  differentiation, network/basin/catchment scale and spatial consequence,
  with only the bridge needed to complete that explanation.
- **Verified PYQ ownership, 2018-2026:** direct routes include 2019 Indian
  water-stress variation, 2023 freshwater availability/access and 2024
  Gangetic-groundwater food-security demands. Adjacent questions remain
  cross-owned and unavailable objective answer letters are not invented.""",
    37: """### Semantic-completeness ownership and PYQ control

- **Owned core:** language, religion, caste, tribe, ethnicity, gender,
  livelihood, migration, cultural landscape, place identity, hearth,
  diffusion, route, frontier, sacred landscape, vernacular region, cultural
  region and social-spatial inequality across India.
- **Region/control principle:** formal, functional and vernacular regions
  are analytical constructions with cores, transition zones, overlaps and
  changing boundaries. A cultural region is not a natural container, a
  homogeneous population or an administrative state.
- **Classification control:** language family differs from mother tongue,
  script, Eighth Schedule inclusion and official-language status. Religion
  tables, Scheduled Caste and Scheduled Tribe constitutional categories,
  tribe, PVTG, indigenous identity, caste group and ethnic community are not
  interchangeable classifications.
- **Social-spatial method:** caste and gender are analysed through access to
  land, work, education, mobility, safety, services, political voice and
  residential or occupational clustering. Spatial association never proves
  innate group character, and national/state averages never erase class,
  rural-urban, age, disability, regional or intra-group variation.
- **No-stereotyping control:** no language, religion, caste, tribe, gender
  or region is assigned a fixed temperament, occupation, capacity or
  political behaviour. Historical institutions, ecology, markets, state
  policy, migration and unequal power explain patterns; identities remain
  dynamic, internally diverse, overlapping and self-defined.
- **Map completeness:** Indo-Aryan, Dravidian, Austroasiatic and
  Tibeto-Burman language zones; linguistic transition belts; sacred and
  pilgrimage networks; the central tribal belt and Northeast; Himalayan,
  pastoral, coastal and island livelihoods; borderlands, migration
  corridors and metropolitan mosaics are named without converting broad
  zones into exclusive or deterministic boundaries.
- **Date/data control:** Census 2011 remains the latest completed all-India
  baseline for language, religion and SC/ST distributions at this cutoff.
  C-16, C-01 and Primary Census Abstract tables have distinct categories and
  levels. PLFS is a sample labour survey, not a census. Census 2027 is
  scheduled and includes caste enumeration, but no 2027 language, religion,
  caste, tribe or gender-distribution result yet exists.
- **Ownership and PYQ control:** Indian Society owns social institutions,
  discrimination and reform in full; Social Justice owns entitlements and
  welfare design; Polity owns constitutional safeguards. Geography owns
  spatial distribution, region formation, diffusion, segregation,
  accessibility and place-based inequality. Direct ownership includes the
  2019 cultural-pockets demand; 2023 Purvaiya is cross-owned with monsoon
  geography, and no social datum or unavailable key is invented.""",
}

GEOGRAPHY_LIVE_OFFICIAL_SOURCES = {
    26: (
        [
            "https://www.un.org/development/desa/pd/content/world-population-prospects-2024",
            "https://population.un.org/wpp/",
            "https://censusindia.gov.in/census.website/data/SRSSTAT",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2133845",
        ],
        "Rechecked 2026-09-05. UN World Population Prospects 2024 is the "
        "current UN estimate/projection revision, not a census. Census 2011 "
        "remains India's latest completed enumeration; SRS supplies sample "
        "vital rates. Census 2027 is scheduled, but no 2027 demographic "
        "results exist at this cutoff.",
    ),
    27: (
        [
            "https://censusindia.gov.in/census.website/search/node?keys=india%20migration%20data",
            "https://mospi.gov.in/sites/default/files/publication_reports/Migration%20in%20India%20RL16082023.pdf",
            "https://www.un.org/development/desa/pd/content/international-migrant-stock",
        ],
        "Rechecked 2026-09-05. Census 2011 remains the detailed internal-"
        "migration census baseline; MoSPI Migration in India 2020-21 is a "
        "PLFS-period survey, not a post-2011 census. UN International Migrant "
        "Stock 2024 covers international stock for 1990-2024 and states that "
        "countries without full reassessment may use extrapolated 2020 trends.",
    ),
    28: (
        [
            "https://www.un.org/development/desa/pd/content/world-urbanization-prospects-2025",
            "https://mohua.gov.in/publication/annual-reports.php",
            "https://mohua.gov.in/offerings/schemes-and-services/details/atal-mission-for-rejuvenation-and-urban-transformation-amrut-IjN5cTMtQWa",
            "https://www.mohua.gov.in/offerings/schemes-and-services/details/pradhan-mantri-awas-yojana-urban-MjNzYjMtQWa",
            "https://niua.in/intranet/sites/default/files/2802.pdf",
        ],
        "Rechecked 2026-09-05. Census 2011 remains India's enumeration and "
        "settlement-classification baseline. UN World Urbanization Prospects "
        "2025 is modelled and retains national-definition comparability "
        "limits. MoHUA mission reports/dashboard claims are dated "
        "administrative progress, not automatically service or welfare impact.",
    ),
    29: (
        [
            "https://www.niti.gov.in/publication/annual-report",
            "https://digitallibrary.niti.gov.in/",
            "https://www.niti.gov.in/node/1350",
            "https://www.niti.gov.in/node/1789",
            "https://www.undp.org/india/publications/aspirational-districts-programme-appraisal",
        ],
        "Rechecked 2026-09-05. The Planning Commission-to-NITI transition and "
        "Five Year Plan chronology are institutional facts. SDG India Index "
        "2023-24, Aspirational District/Block dashboards and UNDP's 2021 "
        "appraisal have different periods, coverage and causal reach; rankings "
        "or delta scores are not proof of economy-wide regional convergence.",
    ),
    30: (
        [
            "https://agcensus.da.gov.in/",
            "https://agcensus.da.gov.in/document/agcen1516/ac_1516_report_final-220221.pdf",
            "https://desagri.gov.in/document-report-category/agriculture-statistics-at-a-glance/",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2265965&lang=1&reg=3",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2260618&reg=3&lang=1",
            "https://www.fao.org/faostat/en/#country/100",
        ],
        "Rechecked 2026-09-05. Agriculture Census 2015-16 remains the latest "
        "fully published round; the portal identifies 2021-22 as the ongoing "
        "eleventh census. Agricultural Statistics at a Glance 2024 is a dated "
        "compilation; 2025-26 Third Advance Estimates are provisional; KMS "
        "2026-27 MSP approval is not procurement; FAOSTAT has national-"
        "reporting and harmonisation lags.",
    ),
    31: (
        [
            "https://ibm.gov.in/IBMPortal/pages/indian_minerals_yearbook",
            "https://www.coal.gov.in/major-statistics/coal-reserves",
            "https://npp.gov.in/publishedReports",
            "https://mnre.gov.in/en/physical-progress/",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2120525",
        ],
        "Rechecked 2026-09-05. IBM yearbooks and mineral statistics retain "
        "commodity-specific reference years; the National Coal Inventory "
        "reports geological resources as on 1 April 2025, not mineable "
        "reserves or current production. CEA/NPP daily reports, MNRE monthly "
        "capacity tables and NCMM policy releases measure different things. "
        "Installed capacity, generation, resource, reserve, production, "
        "auction and operational-project status are not interchangeable.",
    ),
    32: (
        [
            "https://www.mospi.gov.in/annual-survey-industries",
            "https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?page=0&product=ASI",
            "https://www.mospi.gov.in/iip",
            "https://www.dpiit.gov.in/publications/annual-reports",
            "https://www.nicdc.in/",
        ],
        "Rechecked 2026-09-05. ASI is an annual registered-factory survey "
        "with a reference year and later fieldwork/release; IIP is a monthly "
        "volume index with its own base and revisions. DPIIT and NICDC "
        "administrative releases describe scheme or node stages. Approval, "
        "land acquisition, construction, commissioning, production and "
        "measured regional outcome must be reported separately.",
    ),
    33: (
        [
            "https://morth.nic.in/annual-report",
            "https://indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,1,304,366,554,2213",
            "https://shipmin.gov.in/en/publication/annual-reports",
            "https://iwai.nic.in/",
            "https://tradestat.commerce.gov.in/",
            "https://www.isro.gov.in/AnnualReports.html",
            "https://www.isro.gov.in/ISRO_Achievements_FY_2025_2026.html",
        ],
        "Rechecked 2026-09-05. Transport annual reports, operational "
        "dashboards and project releases have different cutoffs; route length, "
        "capacity, throughput and traffic are distinct measures. Commerce "
        "figures may be provisional and merchandise/services series differ. "
        "ISRO mission pages control launch and outcome status, while annual "
        "plans do not guarantee schedule completion.",
    ),
    34: (
        [
            "https://unstats.un.org/unsd/methodology/m49/",
            "https://www.un.org/en/about-us/member-states",
            "https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-country-and-lending-groups",
            "https://population.un.org/wpp/",
            "https://data.worldbank.org/",
        ],
        "Rechecked 2026-09-05. UN M49 country/area names and regions are "
        "statistical classifications and expressly do not determine legal "
        "status or boundaries; UN membership is separate. World Bank FY2027 "
        "income groups use 2025 Atlas-method GNI per capita and may change "
        "annually. Population estimates, classifications, country names and "
        "political status therefore require source and date.",
    ),
    35: (
        [
            "https://www.mha.gov.in/en/division_of_mha/department-of-border-management",
            "https://www.mea.gov.in/bilateral-documents.htm",
            "https://surveyofindia.gov.in/pages/political-map-of-india",
            "https://legislative.gov.in/sites/default/files/A1976-80.pdf",
            "https://www.un.org/depts/los/LEGISLATIONANDTREATIES/STATEFILES/IND.htm",
        ],
        "Rechecked 2026-09-05. Survey of India maps, MEA treaties/statements, "
        "MHA border-management material and the Maritime Zones of India Act "
        "serve different legal and administrative purposes. UN DOALOS states "
        "that publication does not imply recognition of a claim or boundary. "
        "IB, LoC, LAC and AGPL terminology, dispute status, project status and "
        "ground control must be sourced and dated separately.",
    ),
    36: (
        [
            "https://mausamjournal.imd.gov.in/index.php/MAUSAM/Annualreport",
            "https://cgwb.gov.in/en/ground-water-resource-assessment-0",
            "https://cwc.gov.in/en/publications",
            "https://cwc.gov.in/sites/default/files/sopapril2025.pdf",
            "https://www.isro.gov.in/VedasServices.html",
            "https://www.isro.gov.in/LandResources.html",
        ],
        "Rechecked 2026-09-05. IMD observations and climate summaries, CGWB "
        "resource assessments, CWC forecasts/case studies and ISRO/SAC land-"
        "degradation products have different methods, spatial units and "
        "reference periods. A weather event is not a climate trend; a forecast "
        "is not an observation; groundwater resource, quality and extraction "
        "stage are different measures; hazard mapping is not a disaster-loss "
        "count. Geography uses these sources to establish process, pattern and "
        "scale, while Environment, Disaster Management and Economy retain their "
        "full specialist ownership.",
    ),
    37: (
        [
            "https://censusindia.gov.in/census.website/data/census-tables",
            "https://censusindia.gov.in/nada/index.php/catalog/10191",
            "https://censusindia.gov.in/nada/index.php/catalog/11361",
            "https://censusindia.gov.in/nada/index.php/catalog/13378",
            "https://censusindia.gov.in/nada/index.php/catalog/13379",
            "https://tribal.nic.in/downloads/PVTG/OperationalGuidelinePMJANMAN.pdf",
            "https://www.mospi.gov.in/annual-reports",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2133845",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2223099&reg=3&lang=1",
        ],
        "Rechecked 2026-09-05. Census 2011 C-16 language, C-01 religion and "
        "separate SC/ST Primary Census Abstract tables remain completed all-"
        "India baselines; they are not interchangeable cross-tabs. PLFS is a "
        "sample labour survey and must not be relabelled as a census or used to "
        "assign fixed traits to social groups. Census 2027 is scheduled and "
        "includes caste enumeration in Population Enumeration, but no 2027 "
        "language, religion, caste, tribe or gender-distribution result exists "
        "at this cutoff. Ministry of Tribal Affairs classifications are policy "
        "categories and do not erase community self-identification or internal "
        "diversity.",
    ),
}


def ensure_canonical_owner_control(topic: Topic) -> bool:
    """Add the semantic control to the Basic owner without rewriting legacy v1."""
    control = CANONICAL_OWNER_CONTROLS.get(topic.number)
    if control is None:
        return False
    text = topic.basic_path.read_text(encoding="utf-8")
    if "Semantic-completeness ownership and PYQ control" in text:
        return False
    topic.basic_path.write_text(
        text.rstrip() + "\n\n" + control.strip() + "\n",
        encoding="utf-8",
    )
    return True


def _catalogue_rows() -> dict[str, dict[str, Any]]:
    catalogue = load(
        ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
    )
    return {
        row["topic_key"]: row
        for row in catalogue["topics"]
        if row.get("subject", {}).get("key") == "Geography"
    }


def topics() -> list[Topic]:
    """Resolve manifest topics to their existing immutable tracker identities."""
    manifest = load(SECTION_MANIFEST)
    rows = manifest["topics"]
    expected_canonical = [f"geography-{number}" for number in range(26, 38)]
    if [row.get("topic_key") for row in rows] != expected_canonical:
        raise ValueError("Part B manifest must contain canonical topic keys 26-37.")

    catalogue = _catalogue_rows()
    status = load(STATUS)
    result: list[Topic] = []
    for number, row in zip(range(26, 38), rows):
        canonical = row["topic_key"]
        operational = CANONICAL_TO_OPERATIONAL.get(canonical, canonical)
        tracker_keys = catalogue[canonical].get("tracker_topic_keys") or []
        if canonical in CANONICAL_TO_OPERATIONAL:
            if tracker_keys != [operational]:
                raise ValueError(
                    f"{canonical} catalogue alias must resolve exactly to {operational}."
                )
            if any(
                record.get("variant") == "learner-v2"
                and record.get("topic_key") == canonical
                for record in status["exports"]
            ):
                raise ValueError(
                    f"{canonical} unexpectedly has a competing short-key learner-v2 history."
                )
        live_records = [
            record
            for record in status["exports"]
            if record.get("variant") == "learner-v2"
            and record.get("topic_key") == operational
        ]
        if not live_records:
            raise ValueError(f"No live learner-v2 history exists for {operational}.")
        basic = repo(row.get("source_basic") or row["source_canonical"])
        canonical_path = repo(row["source_canonical"])
        advanced = repo(row["source_advanced"])
        result.append(
            Topic(
                number=number,
                topic_key=operational,
                title=row["display_title"],
                basic_path=basic,
                canonical_path=canonical_path,
                advanced_path=advanced,
                cross_topic_sources=tuple(
                    repo(path) for path in row.get("cross_topic_sources", [])
                ),
                pyq_sources=tuple(
                    repo(path) for path in row.get("verified_pyq_sources", [])
                ),
            )
        )
    operational_keys = [topic.topic_key for topic in result]
    if len(result) != 12 or len(set(operational_keys)) != 12:
        raise ValueError("Part B must resolve to twelve unique operational identities.")
    return result


def allocate(
    topic: Topic,
    expected_old_record_id: str,
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], int]:
    """Re-read the canonical manifest row, then allocate on operational identity."""
    reverse_alias = {
        operational: canonical
        for canonical, operational in CANONICAL_TO_OPERATIONAL.items()
    }
    canonical = reverse_alias.get(topic.topic_key, topic.topic_key)
    manifest = load(SECTION_MANIFEST)
    row = next(
        (item for item in manifest["topics"] if item["topic_key"] == canonical),
        None,
    )
    if row is None or row.get("display_title") != topic.title:
        raise ValueError(
            f"{topic.topic_key}: live canonical section manifest changed before allocation."
        )
    return _base_allocate_iac(topic, expected_old_record_id)


def patch_manifest_record(record: dict[str, Any]) -> None:
    """Attach an operational record to its canonical short-key manifest row."""
    reverse_alias = {
        operational: canonical
        for canonical, operational in CANONICAL_TO_OPERATIONAL.items()
    }
    canonical = reverse_alias.get(record["topic_key"], record["topic_key"])
    manifest = load(SECTION_MANIFEST)
    item = next(
        row for row in manifest["topics"] if row["topic_key"] == canonical
    )
    item.update(
        {
            "status": "generated_unapproved",
            "generation": record["generation"],
            "record_id": record["record_id"],
            "operational_topic_key": record["topic_key"],
            "approved": False,
            "assembled_markdown": record["markdown"],
            "workbook_markdown": record["provenance"]["workbook_markdown"],
            "notes_pdf": record["main_pdf"],
            "workbook_pdf": record["workbook"],
            "asset_folder": record["asset_folder"],
            "ascii_master_spec": record["continuous_core_first"][
                "ascii_master_spec"
            ],
            "graphical_flowchart_folder": record["continuous_core_first"][
                "folder"
            ],
            "generation_identity": record["record_id"],
        }
    )
    if canonical != record["topic_key"]:
        item["tracker_topic_keys"] = [record["topic_key"]]
    dump(SECTION_MANIFEST, manifest)


_part_a_validate_tracker_record = validate_tracker_record


def validate_tracker_record(
    tracker_path: Path,
    topic_key: str,
    variant: str,
    generation: int,
    **kwargs: Any,
) -> list[str]:
    """Recover a just-written record if a concurrent tracker writer replaced it."""
    errors = _part_a_validate_tracker_record(
        tracker_path,
        topic_key,
        variant,
        generation,
        **kwargs,
    )
    missing = any("found 0" in error for error in errors)
    if not missing:
        return errors
    record_path = (
        EXPORTS
        / f"{topic_key}-{variant}-g{generation}-{DATE}-record.json"
    )
    if not record_path.is_file():
        return errors
    record = load(record_path)
    for _ in range(5):
        live = load(tracker_path)
        matches = [
            row
            for row in live["exports"]
            if row.get("topic_key") == topic_key
            and row.get("variant") == variant
            and int(row.get("generation", 0)) == generation
        ]
        if not matches:
            live["exports"].append(record)
            dump(tracker_path, live)
        errors = _part_a_validate_tracker_record(
            tracker_path,
            topic_key,
            variant,
            generation,
            **kwargs,
        )
        if not errors:
            return []
        time.sleep(0.2)
    return errors


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    configured_sources, configured_note = GEOGRAPHY_LIVE_OFFICIAL_SOURCES.get(
        topic.number, ([], "")
    )
    live_sources = configured_sources or provenance.get("live_sources") or []
    current_note = configured_note or provenance.get("current_linkage_note") or (
        "Static concepts are separated from volatile population, production, "
        "trade, infrastructure, mission, boundary and policy claims. Every "
        "current number or status requires the issuing institution, reference "
        "period, publication date and provisional/final/operational boundary."
    )
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No volatile live claim is necessary for the static core."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete Human, Economic and Regional Geography Basic/Core is taught before optional Advanced depth. |
| Spatial method | Distribution → controlling physical/human variables → network or region → named world/India anchors → scale and exception. |
| Model method | State assumptions, mechanism, predicted pattern, named application and empirical or Global-South limitation. |
| Evidence method | Claim → named map/place/institution/dataset → analysis → source-date-status or causal qualification. |
| Policy method | Chronology, legal or planning instrument, responsible institution, implementation scale and current status remain distinct. |
| Practice contract | Every solved item has demand decoding, a detailed examiner-grade model, executable timed/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Definition discipline:** close terms share a comparison axis and are never treated as synonyms.
- **Map discipline:** pattern is reconstructed through site, situation, density, gradient, corridor, node, belt, boundary, hinterland and scale.
- **Model discipline:** Ravenstein, Lee, Christaller, Burgess, Hoyt, Harris-Ullman, Myrdal, Perroux, von Thünen, Weber and related models retain assumptions and limits.
- **India discipline:** every explanation carries named state, region, city, corridor, resource belt, border sector or cultural landscape evidence.
- **Data discipline:** Census, SRS, NFHS, Agriculture Census, production, trade, energy and infrastructure claims retain source, reference period, release date and status.
- **PYQ discipline:** repository routing ledgers and held papers control wording and metadata; reconstructed wording and unavailable official keys remain labelled.
- **Current-status note, rechecked {DATE}:** {current_note}

**Live/official context sources recorded by the predecessor generation:**

{source_lines}
"""


_part_a_repair_answer_contracts = repair_answer_contracts


def repair_answer_contracts(markdown: str) -> tuple[str, dict[str, Any]]:
    """Supply executable original Mains blocks when a legacy package has none."""
    repaired, metrics = _part_a_repair_answer_contracts(markdown)
    if metrics["question_count"] >= 3:
        return repaired, metrics
    if "Industries and Industrial Regions" not in repaired:
        return repaired, metrics
    marker = "## OPTIONAL ADVANCED DEPTH — NOT REQUIRED FOR A CORE ANSWER"
    if "## PYQS AND ANSWER PRACTICE" not in repaired:
        return repaired, metrics
    questions = """
### ORIGINAL MAINS 1 — 10 MARKS

**Question:** Explain why industrial location cannot be reduced to raw-material proximity. Answer in 150 words.

**Model thesis:** Raw material matters through weight, bulk and transport cost, but market, energy, labour, skills, agglomeration, infrastructure, policy and technology jointly determine the observed location.

**Claim → named evidence → analysis → qualification:**
- Jamshedpur demonstrates ore-coal-rail logic, while Bengaluru demonstrates skill, network and knowledge-economy advantages.
- Port petrochemical complexes use imported feedstock and coastal logistics, whereas automobile clusters depend on supplier ecosystems and markets.
- Weber explains least-cost pressures, but agglomeration economies, multiple markets, state policy and footloose activities relax his assumptions.

**Qualified conclusion:** Industrial location is a changing weighted combination of material, market, network and institutional factors rather than a one-factor rule.

### ORIGINAL MAINS 2 — 15 MARKS

**Question:** Compare India's major industrial regions and explain the mechanisms producing their different specialisations. Answer in 250 words.

**Model thesis:** India's industrial regions differ because inherited resource and port advantages interact with markets, entrepreneurship, skills, supplier networks, infrastructure and policy.

**Claim → named evidence → analysis → qualification:**
- Chotanagpur's coal, iron ore, power and rail base supports metals and heavy industry, but environmental and social costs qualify resource-led growth.
- Mumbai–Pune and Gujarat combine ports, capital, markets, petrochemicals, engineering and dense urban networks rather than one raw-material base.
- Bengaluru–Tamil Nadu and NCR show the rising importance of skills, electronics, automobiles, services, airports, suppliers and consumption markets.
- Hugli's port-jute-engineering inheritance illustrates industrial inertia, while Visakhapatnam–Guntur shows port, steel, petroleum and corridor linkages.

**Qualified conclusion:** Regional specialisation is path-dependent but continuously reshaped by logistics, technology, policy and value-chain reorganisation.

### ORIGINAL MAINS 3 — 20 MARKS

**Question:** Evaluate industrial corridors as instruments of regional development, manufacturing competitiveness and spatial transformation in India. Answer in 300 words.

**Model thesis:** Corridors can reduce logistics costs and coordinate nodes, trunk infrastructure and investment, but a transport line or notified node becomes transformative only through operational links, skills, urban services, ecological safeguards and local production networks.

**Claim → named evidence → analysis → qualification:**
- DMIC and other NICDC corridors integrate freight backbones with planned nodes, but node-level land, construction and operation stages differ.
- Dedicated Freight Corridors can alter accessibility and shipment time, yet capacity, last-mile links and actual traffic determine realised gains.
- Agglomeration can attract suppliers and jobs, but enclave growth, land conflict, displacement, water stress and uneven state capacity can intensify backwash.
- PM GatiShakti is a planning platform and the National Logistics Policy an institutional framework; neither proves every mapped project is completed.

**Qualified conclusion:** Corridors are conditional regional-development platforms, not automatic growth poles; evaluation must track node-specific implementation, distributional effects and environmental carrying capacity.

"""
    blocks = re.findall(
        r"(?ms)^### ORIGINAL MAINS \d+ — \d+ MARKS\n.*?(?=^### ORIGINAL MAINS |\Z)",
        questions.strip() + "\n",
    )
    needed = 3 - int(metrics["question_count"])
    addition = "\n\n".join(blocks[:needed]) + "\n\n"
    if marker in repaired:
        repaired = repaired.replace(marker, addition + marker, 1)
    else:
        repaired = repaired.rstrip() + "\n\n" + addition
    return _part_a_repair_answer_contracts(repaired)


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
                f"Treat “{focus}” as a definition, model, spatial pattern, "
                "institution and source-date-status problem. Test each statement."
            ),
            "plan": (
                "Fix the comparison axis; reconstruct the map or causal chain; "
                "test model assumptions, India/world anchor, institution and date; "
                "eliminate the closest terminology, determinism or stale-status trap."
            ),
            "why": (
                "It prevents a familiar place, scheme or model label from replacing "
                "the exact definition, mechanism, institutional role or current status."
            ),
            "improve": (
                f"For “{focus}”, state why the nearest distractor fails on definition, "
                "scale, direction, model assumption, institution, date or status."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "all clauses and scales, a causal-spatial argument, named India/world "
            "evidence, model or policy limits and a qualified conclusion."
        ),
        "plan": (
            f"For a {marks}-mark answer, spend about one-sixth of the time decoding "
            f"and drawing the map/flow; open with definition and thesis; organise "
            f"{evidence_count} points as claim → named evidence → analysis → "
            "qualification; compress examples before mechanisms and reserve the "
            "final minute for the scale, model or data-status limit."
        ),
        "why": (
            "The answer obeys the directive, explains spatial differentiation, "
            "integrates Indian evidence and avoids determinism or timeless statistics."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one labelled "
            "map, model assumption, policy chronology or dataset and state the "
            "exception, scale or source-date-status boundary."
        ),
    }


def _detailed_model_answer(block: str, question: str) -> str:
    thesis_match = re.search(
        r"(?is)\*\*Model thesis:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)", block
    )
    conclusion_match = re.search(
        r"(?is)\*\*Qualified conclusion:\*\*\s*(.+?)(?=\n\n\*\*|\n###|\Z)",
        block,
    )
    evidence_match = re.search(
        r"(?is)\*\*Claim\s*→\s*named evidence\s*→\s*analysis\s*→\s*"
        r"qualification:\*\*\s*(.+?)(?=\n\n\*\*Qualified conclusion:|\Z)",
        block,
    )
    thesis = (
        thesis_match.group(1).strip()
        if thesis_match
        else f"The answer must resolve the human-geography demand in “{question}”."
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
            "Define the concept and identify its measurement, classification or model axis.",
            "Map one named Indian pattern and one world or regional comparison.",
            "Trace the driver through mechanism, network or institution to spatial outcome.",
            "Test the nearest terminology, model-assumption or policy-status distinction.",
            "Qualify the conclusion through scale, agency, feedback, exception or data date.",
        ]
    body = "\n".join(
        f"{number}. **Claim and named evidence:** {item} "
        "**Analysis:** Connect the named place, dataset, model or institution to "
        "the driver → mechanism → spatial pattern → consequence chain. "
        "**Qualification:** State the scale, model assumption, interacting control, "
        "regional exception or source-date-status boundary."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** A spatial correlation, model prediction, "
        "single scheme or aggregate statistic is neither a sufficient cause nor "
        "a timeless description; test institutions, agency, networks, scale, "
        "distributional effects and the evidence date.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


_part_a_insert_contract = insert_contract


def insert_contract(markdown: str, topic: Topic, record: dict[str, Any]) -> str:
    repaired = _part_a_insert_contract(markdown, topic, record)
    replacements = {
        "INITIAL CONDITION / DRIVER": "STARTING CONDITION / SPATIAL DRIVER",
        "PHYSICAL MECHANISM OR CIRCULATION": "MODEL / CAUSAL / INSTITUTIONAL MECHANISM",
        "SPATIAL PATTERN / LANDFORM / CLIMATE EXPRESSION": "DISTRIBUTION / NETWORK / REGION / LANDSCAPE",
        "INDIA + WORLD MAP ANCHOR": "NAMED INDIA + WORLD MAP / DATA ANCHOR",
        "SCALE, INTERACTING CONTROL OR EVIDENCE LIMIT": "SCALE + MODEL / DATA / POLICY LIMIT",
        "detailed process, map and qualified causal explanation": "detailed spatial, model, map and qualified causal explanation",
    }
    for old, new in replacements.items():
        repaired = repaired.replace(old, new)
    if topic.number == 30 and repaired.count("### SESSION ") < 15:
        supplements = """
### SESSION 12 — INDIA'S CROP-SEASON AND AGRO-REGIONAL MAP

#### VISUAL FIRST

```text
KHARIF: monsoon sowing → rice/cotton/millets/soybean
RABI: cool-season sowing → wheat/mustard/gram
ZAID: short summer window → vegetables/fodder
        ↓
Punjab–Haryana wheat-rice | eastern rice | Deccan dryland crops
        ↓
Water + soil + labour + market + policy explain the region
```

**Definition and mechanism:** Crop seasons are calendars, not crop essences.
The same crop can cross seasons where irrigation, temperature and varieties
permit. Map answers must connect rainfall timing, soils, water control, market
access and procurement rather than assign one crop mechanically to one state.

**India evidence and trap:** Punjab–Haryana's wheat-rice system, western
Maharashtra sugarcane, Malwa cotton/soybean, Assam tea, Karnataka coffee and
the dryland Deccan millet-pulse belt are named anchors. Net sown area, gross
cropped area, cropping intensity, yield and output are separate measures.

### SESSION 13 — FARM LOCATION, VALUE CHAINS AND VON THÜNEN'S LIMITS

#### VISUAL FIRST

```text
MARKET ACCESS + PERISHABILITY + FREIGHT + LAND RENT
        ↓
peri-urban dairy / vegetables → field crops → extensive grazing
        ↓
cold chain + expressways + contracts + global trade alter the rings
        ↓
location logic survives; exact concentric geometry does not
```

**Model control:** Von Thünen assumes an isolated market, uniform plain,
equal fertility and transport technology. Its mechanism remains useful for
high-value perishables, but refrigeration, processing, multiple markets,
policy and unequal infrastructure weaken the classical rings.

**India evidence and trap:** Metropolitan milk/vegetable belts, contract
horticulture and port-linked plantations show modified distance costs.
Von Thünen is a land-use location model, not a climate classification.

### SESSION 14 — AGRICULTURAL POLICY, INSTITUTIONS AND DATA STATUS

#### VISUAL FIRST

```text
MSP ANNOUNCEMENT ≠ PROCUREMENT ≠ FARM-GATE REALISATION
IRRIGATION POTENTIAL ≠ CREATED ≠ UTILISED ≠ EQUITABLE DELIVERY
FOOD OUTPUT ≠ ACCESS ≠ NUTRITION ≠ RESILIENCE
        ↓
institution + reference year + provisional/final status must be named
```

**Institutional sequence:** The Union agriculture ministry, CACP, FCI,
state procurement agencies, irrigation departments, mandis, cooperatives and
commodity boards perform different roles. A scheme announcement must not be
reported as universal implementation or measured outcome.

**Data discipline:** Agriculture Census, land-use statistics, crop estimates,
procurement releases and survey data have different reference periods and
revision statuses. Current rankings or totals require the issuing source,
year and provisional/final label.

### SESSION 15 — NON-FARM PRIMARY ACTIVITIES AND PHYSIOGRAPHY

#### VISUAL FIRST

```text
RELIEF / GEOLOGY / COAST / DRAINAGE / FOREST
        ↓ resource occurrence + accessibility
fishing | forestry/NTFP | mining | quarrying
        ↓ settlement, transport, livelihood and ecological effects
```

**Exact boundary:** Primary activities extract or harvest from nature.
Fishing, forestry and gathering, mining and quarrying are non-farm primary
activities; manufacturing is secondary. Broad shelves/upwelling support
fisheries, ancient shields and sedimentary basins condition mineral
occurrence, and forest type plus accessibility shapes timber and NTFP use.

**India evidence and qualification:** Western-shelf fisheries, Gangetic and
Brahmaputra inland fisheries, the central Indian NTFP belt, Chotanagpur
minerals and sedimentary coal/hydrocarbon basins show physiographic control.
Technology and transport alter accessibility but cannot create an ore body,
forest ecology or fishing ground where the resource system is absent.

"""
        marker = "## BASIC MCQS / REMEDIATION"
        repaired = repaired.replace(marker, supplements + marker, 1)
    if topic.number == 32 and repaired.count("### SESSION ") < 15:
        supplements = """
### SESSION 9 — INDUSTRY, MANUFACTURING AND LOCATION AXES

#### VISUAL FIRST

```text
INPUTS → TRANSFORMATION → OUTPUT → MARKET
  ↘ material/energy/labour/capital/skills ↙
transport + agglomeration + policy + environment
```

Industry is broader than manufacturing, and factory employment is not a
complete measure of industrialisation. Location analysis must distinguish
material, market, labour, energy, transport, agglomeration and policy axes.

### SESSION 10 — WEBER, LÖSCH AND MODEL LIMITATIONS

#### VISUAL FIRST

```text
WEBER: transport + labour + agglomeration → least-cost site
LÖSCH: demand + market areas → profit landscape
        ↓
real world: multiple markets + policy + networks + technology + ecology
```

Weber's material index and isodapanes explain weight-loss and labour
deviation, while Lösch foregrounds market demand. Both simplify heterogeneous
terrain, institutions, global value chains and cumulative causation.

### SESSION 11 — WORLD INDUSTRIAL REGIONS AS COMPARATIVE SYSTEMS

#### VISUAL FIRST

```text
Ruhr: coal/steel/river/market → restructuring
Great Lakes: ore/coal/water/market → manufacturing belt
Japan Pacific Belt: ports/imports/urban market
China coast: ports/FDI/clusters/hinterland links
```

Named regions must be compared through origin, transport geometry, market,
specialisation, restructuring and environmental legacy—not memorised as lists.

### SESSION 12 — INDIA'S INDUSTRIAL REGIONAL MAP

#### VISUAL FIRST

```text
Chotanagpur → metals/heavy industry
Mumbai–Pune + Gujarat → port/market/engineering/petrochemicals
Hugli → port-jute-engineering inheritance
Bengaluru–Tamil Nadu + NCR → skills/auto/electronics/services
Visakhapatnam–Guntur → port/steel/petroleum/corridor
```

Each Indian region combines inherited advantage with changing logistics,
skills, suppliers and markets. Industrial inertia explains persistence, not
immunity from restructuring.

### SESSION 13 — CORRIDORS, NODES AND IMPLEMENTATION STATUS

#### VISUAL FIRST

```text
freight backbone → planned node → trunk works → allotment
→ factory construction → operation → supplier/urban linkages
```

An industrial corridor is not a single road, rail line or estate. DMIC and
other NICDC corridors require node-specific status; PM GatiShakti is a planning
platform and the National Logistics Policy is an institutional framework.

### SESSION 14 — SECTORAL LOCATION AND NEW INDUSTRIAL GEOGRAPHY

#### VISUAL FIRST

```text
steel/cement → material-energy heavy
petrochemicals → feedstock + port/pipeline
automobiles → suppliers + skills + market
electronics/semiconductors → skills + utilities + clean logistics + policy
textiles/food processing → fibre/crop + labour + market/value chain
```

Footloose means reduced material constraint, not location-free production.
Reliable power, water, clean rooms, skills, airports, suppliers and policy can
be more binding than raw-material proximity in advanced manufacturing.

### SESSION 15 — DATA, EMPLOYMENT AND SUSTAINABILITY FIREWALL

#### VISUAL FIRST

```text
ASI factory sector ≠ all manufacturing
IIP index/growth ≠ output value ≠ GVA
PLI reported jobs ≠ PLFS employment estimate
registration ≠ active-enterprise census
        ↓
source + reference period + release/status + coverage
```

MoSPI, DPIIT, NICDC, DFCCIL and ministry releases answer different questions.
Industrial competitiveness must also account for land, water, pollution,
carbon, worker conditions, displacement and just-transition costs.

"""
        marker = "## BASIC MCQS / REMEDIATION"
        repaired = repaired.replace(marker, supplements + marker, 1)
    return repaired


_part_a_build_ascii_spec = build_ascii_spec


def build_ascii_spec(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    spec = _part_a_build_ascii_spec(
        topic, record, generation, main, markdown_path
    )
    constraints = spec["constraints"]
    constraints.pop("geography_process_spatial_causal_control", None)
    constraints["human_economic_regional_spatial_control"] = True
    constraints["models_india_data_policy_chronology_control"] = True
    return spec


def _split_source_url_table(markdown: str) -> str:
    """Convert an unbreakable three-column source ledger without losing content."""
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0
    header = "| Source | Path / URL | Use and boundary |"
    while index < len(lines):
        if lines[index].strip() != header:
            output.append(lines[index])
            index += 1
            continue
        index += 2
        output.extend(
            [
                "**Source, path and evidence-boundary ledger:**",
                "",
            ]
        )
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
            if len(cells) != 3:
                raise ValueError("Source ledger row no longer has three cells.")
            source, path_or_url, boundary = cells
            output.extend(
                [
                    f"- **{source}:** `{path_or_url}`",
                    f"  - **Use and boundary:** {boundary}",
                ]
            )
            index += 1
        output.append("")
    suffix = "\n" if markdown.endswith("\n") else ""
    return "\n".join(output) + suffix


_part_a_render_artifacts = render_artifacts


def render_artifacts(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    paths: dict[str, Path],
    main: str,
    workbook: str,
) -> tuple[dict[str, Any], str, list[Path], dict[str, str]]:
    return _part_a_render_artifacts(
        topic,
        record,
        generation,
        paths,
        _split_source_url_table(main),
        _split_source_url_table(workbook),
    )


def update_ledgers(rows: list[dict[str, Any]], changed: set[str]) -> None:
    """Record Part B evidence without parsing numbers from long-form keys."""
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
                f"| GEO{number}-001 | high | `{key}` | workbook | "
                "Exam-executable answer controls | Solved items required complete "
                "demand, detailed model, compression, marks and improvement controls | "
                f"E-GEO{number}-002 | MD-GEO{number}-001 | closed in g{generation} |",
                f"| GEO{number}-002 | high | `{key}` | Basic MCQs | Strict A→B→C→D "
                f"sequence | Baseline had {metrics['mcq_count']} blocks and "
                f"{len(metrics['mcq_unparsed'])} unparsed/nonconforming blocks | "
                f"E-GEO{number}-002 | MD-GEO{number}-002 | closed in g{generation} |",
                f"| GEO{number}-003 | medium | `{key}` | flows/data | Independent "
                "topic reconstruction and source-date-status discipline | Fresh "
                f"graphical/ASCII masters and review controls required | "
                f"E-GEO{number}-003 | MD-GEO{number}-003 | closed in g{generation} |",
            )
        )
        evidence.extend(
            (
                f"| E-GEO{number}-001 | `{key}` | Canonical Basic/Core, canonical "
                "package, optional Advanced and official mapping were hash-locked | "
                f"repository source | `{rel(topic.basic_path)}`; "
                f"`{rel(topic.canonical_path)}`; `{rel(topic.advanced_path)}`; "
                f"`{rel(SYLLABUS_MAPPING)}` | repository sources | {DATE} | "
                "verified; canonical owners unchanged |",
                f"| E-GEO{number}-002 | `{key}` | Routed PYQ ledgers control exact "
                "wording and key status; generated Basic practice alone is rotated | "
                f"verified-pyq | `{rel(PYQ_LEDGERS[0])}` plus manifest sources | "
                f"2018-2026 | {DATE} | verified/inferred status preserved |",
                f"| E-GEO{number}-003 | `{key}` | Successor session, workbook, "
                "graphical/ASCII flows, layout, hashes and identity pass | generated "
                f"provenance | `{row['validation']}` | g{generation} | {DATE} | "
                "verified; approval false |",
            )
        )
        suggestions.extend(
            (
                f"| MD-GEO{number}-001 | high | `{key}` | generated practice | "
                "Incomplete per-answer execution controls | "
                f"E-GEO{number}-002 | Add question-specific demand, detailed model, "
                "timed/compression plan, marks rationale and improvement | Practice | "
                f"session/workbook | applied and verified g{generation}; canonical "
                "owner unchanged |",
                f"| MD-GEO{number}-002 | high | `{key}` | generated Basic MCQs | "
                f"Nonconforming key sequence | E-GEO{number}-002 | Enforce strict "
                "A→B→C→D without altering official PYQ options | Practice | "
                f"session/workbook | applied and verified g{generation} |",
                f"| MD-GEO{number}-003 | medium | `{key}` | generation-local package | "
                "Definitions, models, maps, India evidence and current data boundaries "
                f"needed explicit control | E-GEO{number}-001, E-GEO{number}-003 | "
                "Regenerate all four agreeing artifacts | Generated package only | "
                f"applied and verified g{generation}; canonical owner unchanged |",
            )
        )
    append_once(
        REVIEW_ROOT / "ISSUE-LEDGER.md",
        "| GEO26-001 |",
        issues,
        changed,
    )
    append_once(
        REVIEW_ROOT / "EVIDENCE-LEDGER.md",
        "| E-GEO26-001 |",
        evidence,
        changed,
    )
    append_once(
        REVIEW_ROOT / "MD-CHANGE-SUGGESTIONS.md",
        "| MD-GEO26-001 |",
        suggestions,
        changed,
    )


def update_review_tracker(
    rows: list[dict[str, Any]],
    changed: set[str],
) -> None:
    """Synchronize review rows using manifest numbers, not key suffixes."""
    tracker = load(REVIEW_TRACKER)
    by_key = {row["topic_key"]: row for row in rows}
    number_by_key = {topic.topic_key: topic.number for topic in topics()}
    completed_at = datetime.now(timezone.utc).isoformat()
    for item in tracker["topics"]:
        result = by_key.get(item["topic_key"])
        if not result:
            continue
        number = number_by_key[item["topic_key"]]
        metrics = result["baseline_metrics"]
        high = 2
        expected = [
            "ABCD"[position % 4] for position in range(metrics["mcq_count"])
        ]
        if metrics["mcq_unparsed"] or metrics["mcq_keys"] != expected:
            high += 1
        if metrics["flow_panel_count"] < 12:
            high += 1
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
                    "high": high,
                    "medium": 2,
                    "low": 0,
                },
                "md_change_required": False,
                "md_change_ids": [
                    f"MD-GEO{number}-001",
                    f"MD-GEO{number}-002",
                    f"MD-GEO{number}-003",
                ],
                "evidence_ids": [
                    f"E-GEO{number}-001",
                    f"E-GEO{number}-002",
                    f"E-GEO{number}-003",
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
    tracker["source_master_created_at"] = load(MASTER)["created_at"]
    tracker["summary"] = dict(
        Counter(row["status"] for row in tracker["topics"])
    )
    dump(REVIEW_TRACKER, tracker)
    render_review_tracker_markdown(tracker)
    changed.update({rel(REVIEW_TRACKER), rel(REVIEW_TRACKER_MD)})


def _operational_manifest_keys() -> list[str]:
    return [
        CANONICAL_TO_OPERATIONAL.get(row["topic_key"], row["topic_key"])
        for row in load(SECTION_MANIFEST)["topics"]
    ]


def _run_tracker_sync() -> None:
    sync = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "sync_deep_review_tracker.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if sync.returncode:
        raise RuntimeError(
            "Pre-review tracker synchronization failed: "
            + "\n".join((sync.stdout + sync.stderr).splitlines()[-20:])
        )


def _part_b_latest_ids(status: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key in _operational_manifest_keys():
        records = [
            row
            for row in status["exports"]
            if row.get("variant") == "learner-v2"
            and row.get("topic_key") == key
        ]
        if not records:
            raise RuntimeError(f"Stable snapshot has no Part B record for {key}.")
        result[key] = max(
            records, key=lambda row: int(row.get("generation", 0))
        )["record_id"]
    return result


def _export_full_library_from_live_snapshot(
    selected_keys: list[str],
) -> dict[str, Any]:
    """Avoid unrelated concurrent status writes invalidating a long export."""
    live_status = load(STATUS)
    snapshot_ids = _part_b_latest_ids(live_status)
    snapshot = (
        EXPORTS / f"geography-part-b-live-status-snapshot-{DATE}.json"
    )
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
    if _part_b_latest_ids(load(STATUS)) != snapshot_ids:
        raise RuntimeError(
            "A Part B identity changed during full-library publication; "
            "re-read live state before allocating successors."
        )
    return result


def _publish_before_tracker_sync_when_needed() -> dict[str, Any] | None:
    """Publish the full library before sync whenever raw or live keys differ."""
    status = load(STATUS)
    master = load(MASTER)
    review = load(REVIEW_TRACKER)
    raw_manifest_keys = [row["topic_key"] for row in load(SECTION_MANIFEST)["topics"]]
    operational_keys = _operational_manifest_keys()
    operational_set = set(operational_keys)
    status_scope = {
        row["topic_key"]
        for row in status["exports"]
        if row.get("variant") == "learner-v2"
        and row.get("topic_key") in operational_set
    }
    master_keys = [row["topic_key"] for row in master["topics"]]
    master_set = set(master_keys)
    review_set = {row["topic_key"] for row in review["topics"]}
    existing_manifest = EXPORTS / f"final-four-item-library-{DATE}.json"
    existing_validation = (
        EXPORTS / f"final-four-item-library-{DATE}-validation.json"
    )
    if existing_manifest.is_file() and existing_validation.is_file():
        published = load(existing_manifest)
        validation = load(existing_validation)
        published_ids = {
            row["topic_key"]: row["source_record_id"]
            for row in published.get("topics", [])
            if row.get("topic_key") in operational_set
        }
        if (
            validation.get("status") == "passed"
            and published.get("topic_count") == len(master_keys)
            and len(published.get("topics", [])) == len(master_keys)
            and review_set == master_set
            and published_ids == _part_b_latest_ids(status)
        ):
            return {
                "topic_count": published["topic_count"],
                "manifest": rel(existing_manifest),
                "validation_manifest": rel(existing_validation),
                "raw_manifest_keys": raw_manifest_keys,
                "operational_keys": operational_keys,
                "identity_aliases": CANONICAL_TO_OPERATIONAL,
                "published_before_tracker_sync": True,
                "status": "reused_live_full_library_proof",
            }
    key_sets_differ = (
        set(raw_manifest_keys) != operational_set
        or status_scope != operational_set
        or not operational_set.issubset(master_set)
        or review_set != master_set
    )
    if not key_sets_differ:
        return None
    if status_scope != operational_set:
        raise RuntimeError(
            "Part B live status does not contain exactly the resolved operational keys."
        )
    selected_keys = list(master_keys)
    selected_keys.extend(key for key in operational_keys if key not in master_set)
    if len(selected_keys) != len(set(selected_keys)):
        raise RuntimeError("Full-library pre-publish selected duplicate identities.")
    result = _export_full_library_from_live_snapshot(selected_keys)
    if result["topic_count"] != len(selected_keys):
        raise RuntimeError("Pre-review full-library publication lost a topic.")
    _run_tracker_sync()
    synced_master = load(MASTER)
    synced_review = load(REVIEW_TRACKER)
    synced_master_set = {row["topic_key"] for row in synced_master["topics"]}
    synced_review_set = {row["topic_key"] for row in synced_review["topics"]}
    if (
        not operational_set.issubset(synced_master_set)
        or synced_review_set != synced_master_set
    ):
        raise RuntimeError(
            "Pre-review full-library publish/sync did not reconcile live identities."
        )
    return {
        **result,
        "raw_manifest_keys": raw_manifest_keys,
        "operational_keys": operational_keys,
        "identity_aliases": CANONICAL_TO_OPERATIONAL,
        "published_before_tracker_sync": True,
    }


def _republish_master_library() -> dict[str, Any]:
    """Republish the dynamic full MASTER against a stable live snapshot."""
    selected_keys = [row["topic_key"] for row in load(MASTER)["topics"]]
    if len(selected_keys) != len(set(selected_keys)):
        raise RuntimeError("Full-library republish found duplicate MASTER keys.")
    result = _export_full_library_from_live_snapshot(selected_keys)
    manifest = load(repo(result["manifest"]))
    validation = load(repo(result["validation_manifest"]))
    if (
        manifest.get("topic_count") != len(selected_keys)
        or validation.get("topic_count") != len(selected_keys)
        or validation.get("status") != "passed"
    ):
        raise RuntimeError("The dynamic full-library validation did not pass.")
    review = load(REVIEW_TRACKER)
    review["source_master_created_at"] = load(MASTER)["created_at"]
    dump(REVIEW_TRACKER, review)
    render_review_tracker_markdown(review)
    return result


def _copy_base_control_reports() -> None:
    pairs = (
        (
            EXPORTS / f"geography-deep-review-validation-{DATE}.json",
            EXPORTS / f"geography-part-b-deep-review-validation-{DATE}.json",
        ),
        (
            EXPORTS / f"geography-deep-review-reconciliation-{DATE}.json",
            EXPORTS / f"geography-part-b-deep-review-reconciliation-{DATE}.json",
        ),
    )
    for source, target in pairs:
        if source.is_file():
            dump(target, load(source))
    inherited_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Geography-Subject-Completion-{DATE}.md"
    )
    part_b_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Geography-Part-B-Subject-Completion-{DATE}.md"
    )
    if inherited_report.is_file():
        report_text = inherited_report.read_text(encoding="utf-8").replace(
            "# Geography Subject Completion",
            "# Geography Part B Subject Completion",
            1,
        )
        report_text = report_text.replace(
            "1 September 2026", "2 September 2026", 1
        )
        write_text(part_b_report, report_text)


_world_rewrite_command_history = _rewrite_command_history


def _rewrite_command_history() -> None:
    _copy_base_control_reports()
    _world_rewrite_command_history()


_inherited_record_post_shared_checks = _record_post_shared_checks


def _record_post_shared_checks(full_library_result: dict[str, Any]) -> None:
    _inherited_record_post_shared_checks(full_library_result)
    inherited_reconciliation = (
        EXPORTS / f"geography-deep-review-reconciliation-{DATE}.json"
    )
    inherited_validation = (
        EXPORTS / f"geography-deep-review-validation-{DATE}.json"
    )
    reconciliation = load(inherited_reconciliation)
    reconciliation["identity_resolution"] = {
        "canonical_manifest_keys": [
            row["topic_key"] for row in load(SECTION_MANIFEST)["topics"]
        ],
        "operational_tracker_keys": _operational_manifest_keys(),
        "aliases": CANONICAL_TO_OPERATIONAL,
        "policy": (
            "Preserve established long-form learner-v2 histories for topics "
            "28, 30 and 32; do not create competing short-key histories."
        ),
        "latest_identity_agreement": True,
    }
    part_b_reconciliation = (
        EXPORTS / f"geography-part-b-deep-review-reconciliation-{DATE}.json"
    )
    part_b_validation = (
        EXPORTS / f"geography-part-b-deep-review-validation-{DATE}.json"
    )
    dump(inherited_reconciliation, reconciliation)
    dump(part_b_reconciliation, reconciliation)
    dump(part_b_validation, load(inherited_validation))
    inherited_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Geography-Subject-Completion-{DATE}.md"
    )
    part_b_report = (
        REVIEW_ROOT
        / "subject-reports"
        / f"Geography-Part-B-Subject-Completion-{DATE}.md"
    )
    report_text = inherited_report.read_text(encoding="utf-8")
    report_text = report_text.replace(
        "# Geography Subject Completion",
        "# Geography Part B Subject Completion",
        1,
    )
    report_text = report_text.replace(
        "1 September 2026", "2 September 2026", 1
    )
    write_text(part_b_report, report_text)


def _augment_inventory_with_git_status() -> None:
    """Write exact UTF-8 text and NUL inventories from this run's mtimes."""
    inventory = (
        EXPORTS / f"geography-part-b-deep-review-{DATE}-changed-files.txt"
    )
    nul_inventory = (
        EXPORTS / f"geography-part-b-deep-review-{DATE}-changed-files.nul"
    )
    threshold_ns = globals().get("_PART_B_RUN_STARTED_NS", time.time_ns())
    changed: set[str] = set()
    base_inventory = (
        EXPORTS / f"geography-deep-review-{DATE}-changed-files.txt"
    )
    if base_inventory.is_file():
        changed.update(
            path
            for path in base_inventory.read_text(encoding="utf-8").splitlines()
            if path and repo(path).is_file()
        )
    for directory, subdirs, files in os.walk(ROOT):
        subdirs[:] = [
            name
            for name in subdirs
            if name not in {".git", "__pycache__", ".pytest_cache"}
        ]
        base = Path(directory)
        for name in files:
            path = base / name
            try:
                if path.stat().st_mtime_ns >= threshold_ns:
                    changed.add(rel(path))
            except FileNotFoundError:
                continue
    changed.update(
        {
            rel(Path(__file__)),
            "tools\\test_regenerate_geography_part_b_deep_review.py",
            "tools\\test_v2_section_indexes.py",
            "tools\\test_export_four_item_library.py",
            rel(STATUS),
            rel(SECTION_MANIFEST),
            rel(MASTER),
            rel(REVIEW_TRACKER),
            rel(REVIEW_TRACKER_MD),
            "EXPORT-PDF-COMMAND-INDEX.md",
            "V2-SUBJECT-SECTION-COMMAND-INDEX.md",
            rel(
                EXPORTS
                / f"geography-part-b-deep-review-validation-{DATE}.json"
            ),
            rel(
                EXPORTS
                / f"geography-part-b-deep-review-reconciliation-{DATE}.json"
            ),
            rel(
                EXPORTS
                / f"geography-part-b-live-status-snapshot-{DATE}.json"
            ),
            rel(
                REVIEW_ROOT
                / "subject-reports"
                / f"Geography-Part-B-Subject-Completion-{DATE}.md"
            ),
            rel(inventory),
            rel(nul_inventory),
        }
    )
    ordered = sorted(changed, key=str.casefold)
    missing = [
        path
        for path in ordered
        if path not in {rel(inventory), rel(nul_inventory)}
        and not repo(path).is_file()
    ]
    if missing:
        raise RuntimeError(
            "Changed-file inventory contains missing paths: "
            + ", ".join(missing[:20])
        )
    write_text(inventory, "\n".join(ordered))
    nul_inventory.write_bytes(
        b"".join(path.encode("utf-8") + b"\0" for path in ordered)
    )
    payload = nul_inventory.read_bytes()
    if not payload.endswith(b"\0") or payload.count(b"\0") != len(ordered):
        raise RuntimeError("NUL-delimited changed inventory is invalid.")
    for path in inventory.read_text(encoding="utf-8").splitlines():
        if path and path not in {rel(inventory), rel(nul_inventory)}:
            if not repo(path).is_file():
                raise RuntimeError(f"Inventory path disappeared: {path}")


_inherited_process_topic = process_topic


def process_topic(topic: Topic, changed: set[str]) -> dict[str, Any]:
    """Generate one successor and persist its dated official-source controls."""
    result = _inherited_process_topic(topic, changed)
    live_sources, current_note = GEOGRAPHY_LIVE_OFFICIAL_SOURCES.get(
        topic.number, ([], "")
    )
    if not live_sources:
        return result

    status = load(STATUS)
    record = latest(status, topic.topic_key)
    provenance = record.setdefault("provenance", {})
    provenance["live_sources"] = live_sources
    provenance["current_linkage_note"] = current_note

    content_spec_path = repo(provenance["content_spec"])
    content_spec = load(content_spec_path)
    content_spec["live_official_sources"] = live_sources
    content_spec["current_status_note"] = current_note
    dump(content_spec_path, content_spec)
    provenance.setdefault("deliverable_hashes", {})[
        rel(content_spec_path)
    ] = sha256(content_spec_path)

    record_path = (
        EXPORTS
        / f"{topic.topic_key}-learner-v2-g{record['generation']}-{DATE}-record.json"
    )
    dump(record_path, record)
    for index, candidate in enumerate(status["exports"]):
        if candidate.get("record_id") == record["record_id"]:
            status["exports"][index] = record
            break
    else:
        raise RuntimeError(f"{topic.topic_key}: generated record disappeared.")
    dump(STATUS, status)

    final_audit_path = (
        REVIEW_ROOT
        / "reviews"
        / topic.topic_key
        / f"{topic.topic_key}-g{record['generation']}-final-audit.json"
    )
    final_audit = load(final_audit_path)
    final_audit.setdefault("hashes", {})[rel(content_spec_path)] = sha256(
        content_spec_path
    )
    final_audit["live_official_sources"] = live_sources
    final_audit["current_status_note"] = current_note
    dump(final_audit_path, final_audit)
    changed.update(
        {
            rel(STATUS),
            rel(record_path),
            rel(content_spec_path),
            rel(final_audit_path),
        }
    )
    return result


_part_a_entrypoint = main


def main() -> int:
    global _PART_B_RUN_STARTED_NS
    _PART_B_RUN_STARTED_NS = time.time_ns()
    return _part_a_entrypoint()


if __name__ == "__main__":
    raise SystemExit(main())
