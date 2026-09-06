"""Deep-review and immutably regenerate Geography Part A topics 01-25."""

from __future__ import annotations

import hashlib
import copy
import re
import sys
import textwrap
from pathlib import Path
from typing import Any


_BASE = Path(__file__).with_name("regenerate_indian_art_culture_deep_review.py")
_BASE_SHA256 = "260e1b58b69798e1ddeaa54af6e79e774f2dfc74e2a5ed901b6d07e222f69cb2"
_base_bytes = _BASE.read_bytes()
if hashlib.sha256(_base_bytes).hexdigest() != _BASE_SHA256:
    raise RuntimeError(
        "The shared Indian Art and Culture pattern changed. Review and repin it "
        "before running the Geography Part A workflow."
    )

_source = _base_bytes.decode("utf-8").replace("\r\n", "\n")
_source = _source.rsplit('\nif __name__ == "__main__":', 1)[0]
for _old, _new in (
    ("all 15 live Indian Art and Culture", "all 25 Geography Part A"),
    ("Indian-Art-and-Culture", "Geography"),
    ("indian-art-and-culture", "geography"),
    ("Indian Art and Culture", "Geography"),
    ("INDIAN ART AND CULTURE", "GEOGRAPHY"),
    ("indian_art_culture", "geography_part_a"),
    ('f"iac-', 'f"geo-'),
    ("ART_CULTURE_REVIEW_POINTS", "GEOGRAPHY_REVIEW_POINTS"),
    ("E-IAC", "E-GEO"),
    ("MD-IAC", "MD-GEO"),
    ("IAC{", "GEO{"),
    ("IAC01", "GEO01"),
    ('"range(1, 16)"', '"range(1, 26)"'),
    ('"!= 15"', '"!= 25"'),
    ("exact live topic keys 01-15", "exact topic keys 01-25"),
    ("topics 01-15", "topics 01-25"),
    ('\'"topic_count": 15\'', '\'"topic_count": 25\''),
    ('\'"topic_validations_passed": 15\'', '\'"topic_validations_passed": 25\''),
    ('\'"latest_topic_count": 15\'', '\'"latest_topic_count": 25\''),
    (
        '\'"learning_and_workbook_pdfs_checked": 30\'',
        '\'"learning_and_workbook_pdfs_checked": 50\'',
    ),
    ('\'"represented": 15\'', '\'"represented": 25\''),
    ('\'"expected": 15\'', '\'"expected": 25\''),
    ("All 15 live topics", "All 25 topics"),
    ('"IAC"', '"GEO"'),
):
    if _old not in _source:
        raise RuntimeError(f"Shared-pattern transformation anchor is missing: {_old!r}")
    _source = _source.replace(_old, _new)

_authoring_import = '''import generate_geography_part_a_common as authoring_common
from geography_part_a_11_15_data import (
    TOPIC_11,
    TOPIC_12,
    TOPIC_13,
    TOPIC_14,
    TOPIC_15,
)
'''
_authoring_replacement = '''import generate_geography_common as authoring_common
from geography_05_09_data import TOPIC_05, TOPIC_06, TOPIC_07, TOPIC_08, TOPIC_09
from geography_10_14_data import TOPIC_10, TOPIC_11, TOPIC_12, TOPIC_13, TOPIC_14
from geography_15_19_data import TOPIC_15, TOPIC_16, TOPIC_17, TOPIC_18, TOPIC_19
from geography_20_22_data import TOPIC_20, TOPIC_21, TOPIC_22
from geography_23_25_data import TOPIC_23, TOPIC_24, TOPIC_25
'''
if _authoring_import not in _source:
    raise RuntimeError("Could not repair transformed Geography authoring imports.")
_source = _source.replace(_authoring_import, _authoring_replacement, 1)

_test_replacement = '''_test_replacement = \'''    tests = [
        run_unittest("test_regenerate_geography_part_a_deep_review"),
        run_unittest("test_export_four_item_library"),
        run_unittest("test_sync_deep_review_tracker"),
        run_unittest("test_refresh_all_v2_learning_sessions"),
    ]
\'''
'''
_source, _test_count = re.subn(
    r"_test_replacement = '''    tests = \[\n.*?\n    \]\n'''\n",
    _test_replacement,
    _source,
    count=1,
    flags=re.S,
)
if _test_count != 1:
    raise RuntimeError("Could not replace the inherited targeted-test list.")

exec(compile(_source, str(Path(__file__)), "exec"), globals())

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

if not hasattr(authoring_common, "_full_owner_depth"):
    authoring_common._full_owner_depth = authoring_common._full_owner

CURRENT_AUTHORING_CONFIGS.update(
    {
        str(config["key"]): config
        for config in (
            TOPIC_05,
            TOPIC_06,
            TOPIC_07,
            TOPIC_08,
            TOPIC_09,
            TOPIC_10,
            TOPIC_15,
            TOPIC_16,
            TOPIC_17,
            TOPIC_18,
            TOPIC_19,
            TOPIC_20,
            TOPIC_21,
            TOPIC_22,
            TOPIC_23,
            TOPIC_24,
            TOPIC_25,
        )
    }
)


def generation_sources(
    topic: Topic,
    record: dict[str, Any],
) -> tuple[str, str]:
    """Use each Geography topic's latest immutable learner-v2 predecessors."""
    workbook_value = record.get("workbook_markdown") or record.get(
        "provenance", {}
    ).get("workbook_markdown")
    if not workbook_value:
        raise ValueError(f"{topic.topic_key}: predecessor workbook is absent.")
    return (
        repo(record["markdown"]).read_text(encoding="utf-8"),
        repo(workbook_value).read_text(encoding="utf-8"),
    )


def topic21_session_matches_authored(main: str, workbook: str) -> bool:
    """Apply the Geography Topic 21 authored-session contract."""
    required_main = (
        "### SESSION 1 — FOUNDATION — Eastern-margin location and rainfall contrast",
        "### SESSION 10 — CORE — Humid North-East division",
        "### SESSION 13 — SYNTHESIS — Bay of Bengal branch",
        "### SESSION 15 — SYNTHESIS — PYQ boundary and answer spine",
        "### Q77. Which statement correctly explains Transparent zero-direct route?",
    )
    required_workbook = (
        "### Q77. Which statement correctly explains Transparent zero-direct route?",
        "### TRANSPARENT ZERO-DIRECT-PYQ AUDIT",
    )
    return all(item in main for item in required_main) and all(
        item in workbook for item in required_workbook
    )


DATE = "2026-09-05"
GEOGRAPHY_PATTERN_PATH = Path(__file__).with_name(
    "regenerate_indian_art_culture_deep_review.py"
)

SECTION = "Part A — Physical Geography"
FLOW_SUBJECT = "Geography"
SECTION_MANIFEST = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "v2"
    / "geography--part-a-physical-geography.json"
)
SYLLABUS_MAPPING = (
    ROOT
    / "upsc-ai-kit"
    / "knowledge"
    / "Geography"
    / "OFFICIAL-UPSC-SYLLABUS-MAPPING.md"
)
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


GEOGRAPHY_REVIEW_POINTS: dict[int, tuple[str, str, str]] = {
    1: (
        "Earth-system explanation runs from universe and Solar-System scale through rotation, revolution, axial tilt, latitude-longitude and time to India's 8°4′N–37°6′N, 68°7′E–97°25′E location, 82°30′E standard meridian and Indian Ocean setting.",
        "Rotation causes the diurnal cycle and Coriolis framework, revolution plus axial tilt causes seasons; local solar time is longitude-based while IST is a legal standard, and the Tropic of Cancer is not India's climatic divide by itself.",
        "Astronomical models, boundary lengths and current administrative counts require source/date discipline; location creates opportunities and constraints but does not mechanically determine monsoon, trade or strategy.",
    ),
    2: (
        "Crustal analysis connects seismic evidence, compositional and rheological layers, rock cycle, plate boundaries and Wilson-cycle logic to India's cratons, mobile belts, Gondwana basins, Deccan volcanics, Himalaya and Indo-Gangetic foredeep.",
        "Crust is compositional while lithosphere is mechanical; continental crust is generally granitic and less dense, oceanic crust basaltic and denser, and a shield, craton, platform, basin and plate are not interchangeable map units.",
        "Present relief is a multi-stage tectonic-denudational product; rock age, orogeny, mineralisation and surface form need not coincide, so geological association supports probability rather than deterministic resource claims.",
    ),
    3: (
        "Vulcanism and seismicity follow magma generation, ascent, eruption style, fault rupture, wave propagation and site response; India requires Himalayan collision, Kachchh intraplate strain, Peninsular reservoirs/faults, Andaman subduction and Barren Island anchors.",
        "Magnitude measures source size whereas intensity records effects; focus differs from epicentre, P differs from S and surface waves, and a tsunami requires water-column displacement rather than every submarine earthquake.",
        "Hazard is not disaster: exposure, vulnerability, construction and preparedness mediate loss; seismic zonation is probabilistic and revised through evidence, while prediction claims must not be confused with monitoring or early warning.",
    ),
    4: (
        "Weathering prepares material in situ, mass movement transfers it downslope, running water removes it, and groundwater follows infiltration, percolation, aquifer storage and discharge; Indian analysis links lithology, slope, rainfall, land use and pumping.",
        "Weathering differs from erosion, porosity from permeability, water table from piezometric surface, aquifer from aquitard, and slump/slide/flow/creep require movement-specific geometry rather than the generic label landslide.",
        "A trigger such as intense rain is not the complete cause: antecedent moisture, discontinuities, toe cutting, drainage and construction condition failure; groundwater trends and notified areas require dated official status.",
    ),
    5: (
        "Fluvial systems connect rainfall-runoff, drainage-network organisation, erosion, transport, deposition, graded-profile adjustment and floodplain evolution to Himalayan antecedent rivers, Peninsular drainage and basin-scale interlink proposals.",
        "V-shaped valley, gorge, waterfall, meander, oxbow, levee, delta and alluvial fan occupy different energy and valley settings; drainage pattern differs from drainage basin, and river capture differs from planned diversion.",
        "Interlinking effects are basin- and design-specific: transfer volume, seasonality, environmental flows, sediment, displacement, federal consent and climate uncertainty must qualify both drought-proofing and ecological-damage claims.",
    ),
    6: (
        "Glaciation proceeds through accumulation-ablation balance, ice deformation/basal motion, erosion, transport and deposition; cirque–arête–horn, U-shaped valley, moraine and outwash logic must connect to Himalayan mass balance, proglacial lakes and GLOF cascades.",
        "Snowline, equilibrium-line altitude, firn line and glacier terminus are distinct; till is unsorted ice-laid sediment while outwash is meltwater-sorted, and a fjord is a drowned glacial trough rather than any steep inlet.",
        "Retreat varies by glacier and period; lake growth alone does not prove imminent outburst, while dam material, freeboard, slope instability, ice/rock avalanches and downstream exposure condition risk.",
    ),
    7: (
        "Arid geomorphology links moisture deficit, sparse cover, mechanical weathering, episodic runoff, deflation, abrasion and dune migration; pediment–bajada–playa and Thar land-use pressures frame desertification as land degradation.",
        "Desert is a climatic moisture condition, desertification is degradation in drylands, and drought is a temporary anomaly; barchan, transverse, longitudinal and parabolic dunes encode different wind/sediment/vegetation controls.",
        "Wind is not the sole desert agent and every dune is not freely migrating; grazing, irrigation salinity, groundwater, shelterbelts and rainfall variability have locally different effects, so causal conclusions must be spatially qualified.",
    ),
    8: (
        "Karst requires soluble rock, joints, water and carbonic-acid solution, followed by underground drainage and carbonate deposition; lapies, sinkholes, dolines, uvalas, poljes, caves, stalactites and stalagmites form a connected hydrological system.",
        "Solution enlarges voids whereas deposition builds speleothems; stalactites hang, stalagmites rise, columns join them, and Meghalaya caves, Bhimbetka shelters and the Meghalayan chronostratigraphic unit are categorically different.",
        "Cave age, host-rock age, occupation age and formal geological-age boundary must not be collapsed; tourism and infrastructure effects depend on recharge, passage geometry, biodiversity and carrying capacity.",
    ),
    9: (
        "Lake classification must follow basin origin—tectonic, volcanic, glacial, fluvial, karst, coastal, aeolian, landslide or artificial—then water balance, mixing, sediment and succession; Indian wetlands add Ramsar and domestic-governance layers.",
        "Lake, lagoon, oxbow, reservoir and wetland are not synonyms; freshwater/saline and exorheic/endorheic are separate axes, while Ramsar designation is international recognition rather than ownership transfer or automatic protection.",
        "Area, designation count and ecological status are time-sensitive; shrinkage or eutrophication needs inflow, evaporation, abstraction, nutrients, encroachment and catchment evidence rather than one-cause attribution.",
    ),
    10: (
        "Coastal morphology connects wave generation, refraction, erosion, longshore drift, sediment cells, deposition and sea-level/tectonic change to cliffs, caves-arches-stacks, beaches, spits, bars, lagoons, deltas and India's east-west coast contrast.",
        "Emergent and submergent coasts describe relative sea-level histories, erosional and depositional forms can coexist, and CRZ categories/regulatory lines are legal-planning constructs rather than geomorphic shoreline types.",
        "Erosion control can shift risk downdrift; ports, dams, sand mining, storms, subsidence and sea-level rise interact, while CRZ rules, clearances and project status require exact notification/date/source discipline.",
    ),
    11: (
        "Island analysis distinguishes continental, volcanic, coral and depositional origins; reef-building follows light, temperature, salinity, substrate and symbiosis, with fringing–barrier–atoll sequences compared against Lakshadweep and Andaman-Nicobar tectonic settings.",
        "Coral island is not coral reef, atoll is not every ring-shaped island, and bleaching is stress-driven symbiont loss rather than immediate coral death; Great Nicobar project components, tribal reserve, biosphere and statutory clearance statuses remain separate.",
        "Darwinian subsidence is a model, not a universal single pathway; reef condition and project impacts need site/date/source evidence, cumulative-risk analysis and explicit uncertainty rather than benefit-versus-environment binaries.",
    ),
    12: (
        "Ocean structure links temperature, salinity and density to stratification and circulation; wind stress, Coriolis, Ekman transport, gyres, upwelling, thermohaline overturning, tides and Indian Ocean monsoon reversal culminate in IOD–ENSO interactions.",
        "Wave transmits energy, current transports water and tide is astronomical sea-level oscillation; spring/neap are alignment effects, not seasons, and positive IOD is a west-minus-east Indian Ocean SST gradient rather than simply a warm western ocean.",
        "IOD and ENSO modulate probabilities rather than determine Indian rainfall; event phase, season, interaction, basin background and model/source date must qualify fisheries, cyclone or monsoon conclusions.",
    ),
    13: (
        "Weather elements connect radiation balance, temperature, pressure-gradient force, Coriolis/friction, humidity, stability, condensation, clouds and precipitation; upper-air Rossby waves, subtropical jet and western-disturbance tracks anchor Indian seasonality.",
        "Humidity, relative humidity and dew point differ; weather differs from climate, jet stream from surface wind, and a western disturbance is an eastward-moving extratropical system embedded in westerlies rather than a western Indian monsoon branch.",
        "Jet position is one control among topography, blocking, moisture supply and synoptic evolution; event attribution and seasonal forecasts require dated agency evidence and probabilistic language.",
    ),
    14: (
        "Köppen classification uses temperature and precipitation thresholds with seasonality letters; India must be mapped as regional climate regimes shaped by latitude, altitude, continentality, relief and monsoon circulation rather than memorised codes alone.",
        "A/B/C/D/E are major climate groups, second and third letters carry moisture/thermal meaning, and climate region differs from vegetation biome or agro-climatic zone even when boundaries broadly correlate.",
        "Threshold classification simplifies transitional and highland mosaics; map answers should state dataset/scale and avoid treating a code boundary as a permanent administrative or ecological line.",
    ),
    15: (
        "Equatorial Af climate follows year-round high sun, ITCZ convection, humid air and weak annual thermal range, producing frequent rainfall, evergreen stratification, intense chemical weathering and leached soils in Amazon, Congo and Maritime Southeast Asia.",
        "Equatorial does not mean everywhere exactly on the Equator, convectional rainfall is not continuous all-day rain, and luxuriant biomass does not imply nutrient-rich soil because rapid cycling stores nutrients mainly in biomass.",
        "Deforestation alters energy, moisture and nutrient cycles but rainfall feedback magnitude varies by scale and region; Indian evergreen forests are analogues with monsoonal/topographic differences, not Af replicas.",
    ),
    16: (
        "Tropical monsoon and trade-wind littoral climates arise from seasonal pressure migration, cross-equatorial flow, ocean moisture, relief and convergence, producing a marked wet season, short dry season and monsoon-forest adaptations.",
        "Monsoon means seasonal wind reversal/system, not merely heavy rain; tropical marine eastern margins receive trade-wind/orographic rain and tropical cyclones, while onset, burst, break and withdrawal are distinct Indian phases.",
        "Land-sea thermal contrast is necessary but insufficient: ITCZ, Tibetan heating, jets, Mascarene High, ENSO, IOD, MJO and snow/soil states interact, so no single driver explains each year's monsoon.",
    ),
    17: (
        "Savanna Aw/As climates reflect seasonal ITCZ migration between convective wet summers and subtropical-high dry winters, sustaining tall grasses with scattered drought/fire-adapted trees across Africa, South America and northern Australia.",
        "Savanna is tropical grassland, steppe is semi-arid temperate/subtropical grassland, and parkland structure is not evidence of a climax maintained by climate alone because fire, herbivory and land use matter.",
        "Fire can recycle nutrients and maintain openness but frequency/intensity changes may degrade systems; Indian deciduous forests and grasslands need region-specific rainfall, fire and grazing evidence rather than direct Sudan-type equivalence.",
    ),
    18: (
        "Hot deserts cluster near subtropical subsidence, western-margin cold currents, continental interiors and rain shadows, while mid-latitude deserts add distance and mountain barriers; large diurnal range, episodic rain and xerophytes follow water-energy balance.",
        "Hot desert differs from cold/mid-latitude desert, aridity from drought, and cold current promotes coastal stability/fog rather than directly 'removing' all rain; Thar's monsoon-margin setting differs from Sahara's dominant controls.",
        "Desert location is multicausal and boundaries migrate; Great Indian Bustard habitat policy, renewable infrastructure and desertification trends require dated, spatially explicit sources and trade-off analysis.",
    ),
    19: (
        "Mediterranean Cs climate results from summer subtropical-high subsidence and winter westerly cyclone/frontal rain on western margins, supporting sclerophyll vegetation, winter cereals, vines, olives and high summer fire risk.",
        "Mediterranean climate is not confined to the Mediterranean Basin, winter rainfall is not monsoonal reversal, and chaparral, maquis, fynbos and mallee are regional analogues rather than identical floras.",
        "Fire is climate-enabled but ignition, fuel management and settlement shape disaster; Himalayan fruit belts share horticultural traits but not the complete Mediterranean circulation regime.",
    ),
    20: (
        "Temperate continental steppe Bs climates occupy interiors and rain shadows between deserts and humid forests, with low variable precipitation, large annual range, short grasses and chernozem-linked grain/pastoral economies.",
        "Steppe differs from tropical savanna and humid prairie, chernozem is not universal across all steppes, and continentality concerns land-dominated thermal range rather than simply distance from a national coastline.",
        "Grain productivity depends on soil, snowmelt, technology and markets as well as climate; India's wheat belt is a functional comparison with monsoonal irrigation and subtropical seasonality, not a climatic identity.",
    ),
    21: (
        "Warm temperate eastern-margin China type combines humid subtropical latitude, onshore summer flow, convection/cyclones and winter continental influence, producing hot wet summers, cooler winters and mixed crops/forests in East Asia and analogous margins.",
        "China type is an eastern-margin climate label, not China's entire climate; it differs from tropical monsoon by winter temperature and from Laurentian by warmer conditions and different ocean-current/air-mass relations.",
        "East-margin similarity does not erase monsoon, current and topographic differences; Northeast India is an anchored comparison whose altitude and exceptional rainfall prevent one-code generalisation.",
    ),
    22: (
        "Cool temperate western-margin British type follows year-round westerlies, maritime moderation, frequent frontal cyclones and orographic rain, producing mild winters, cool summers, small annual range and deciduous/mixed vegetation.",
        "Marine west coast differs from Mediterranean summer-dry climate and continental interiors; 'British type' is a climatic shorthand extending to other western margins, not a statement that all Britain is uniform.",
        "North Atlantic circulation, latitude, relief and changing storm tracks jointly matter; Himalayan temperate forests are altitudinal analogues under monsoon influence, not marine-west-coast equivalents.",
    ),
    23: (
        "Cool temperate continental Siberian/D climate develops in high-latitude interiors with long severe winters, short summers, strong annual range, low precipitation and taiga conifers adapted to frozen soils and brief growth seasons.",
        "Taiga is boreal conifer forest south of tundra, permafrost extent varies and is not synonymous with all seasonally frozen ground, and continental subarctic climate differs from polar ET/EF thresholds.",
        "Cold alone does not determine vegetation: moisture, active-layer depth, fire and disturbance matter; India's subalpine/alpine belts are elevation-controlled analogues with monsoonal and Himalayan differences.",
    ),
    24: (
        "Cool temperate eastern-margin Laurentian climate combines continental air masses, maritime moisture, warm-current influence and frontal/cyclonic precipitation, yielding warm summers, cold winters and year-round precipitation in northeastern North America and northeast Asia.",
        "Laurentian differs from warm China type by colder winters and from Siberian interiors by stronger maritime precipitation; warm and cold currents modify coastal gradients but do not alone create the whole climate.",
        "Current-air-mass causation must be expressed as interaction with latitude, westerlies and continentality; Eastern Himalayan temperate zones are topographic analogues rather than Laurentian climatic replicas.",
    ),
    25: (
        "Polar climates separate tundra ET, where the warmest month is above 0°C but below 10°C, from ice-cap EF below 0°C year-round; low sun angle, high albedo, polar night/day, permafrost and short food webs structure Arctic and Antarctic systems.",
        "Arctic is mainly an ocean surrounded by continents while Antarctica is a high continent surrounded by ocean; sea ice differs from land ice, tundra from ice cap, and polar desert refers to low precipitation rather than absence of frozen water.",
        "Amplification, sea-ice loss, ice-sheet mass balance and governance claims require hemisphere, variable, baseline and date; Ladakh/cold deserts are useful process comparisons but not polar climates.",
    ),
}

CANONICAL_OWNER_CONTROLS: dict[int, str] = {
    1: """### Semantic-completeness ownership and PYQ control

- **Owned core:** universe and Solar-System scale; Earth's geoid/oblate shape,
  rotation, revolution, axial tilt, seasons, latitude-longitude, local and
  standard time, International Date Line, interior evidence and magnetosphere;
  India's absolute and relative location, extent and Indian Ocean setting.
- **Process control:** rotation produces the diurnal cycle and the Coriolis
  framework; revolution plus axial tilt and orbital geometry produce seasonal
  insolation; longitude produces local-time difference while IST is a legal
  standard fixed to 82°30′E.
- **Scale/map control:** astronomical, global-coordinate, national and regional
  scales are kept separate. Mainland/island extremes, coordinate extent,
  Tropic of Cancer, standard meridian and neighbouring seas are mapped without
  turning a line into a complete climatic or strategic explanation.
- **Date/data control:** coordinates and administrative/boundary descriptions
  use a dated official map; universe age and geophysical values retain
  approximation and source discipline. A current storm or time-zone proposal
  cannot silently update the static core.
- **Terminology control:** geoid differs from oblate spheroid; latitude from
  longitude; local solar time from standard time; magnetic from geographic
  pole; solar wind, flare, CME, geomagnetic storm and aurora remain distinct.
- **Causal control:** India's location creates constraints and opportunities
  but does not by itself determine monsoon, trade, security or development.
  Auroral visibility follows magnetospheric geometry, particle precipitation
  and atmospheric excitation, not cold weather or reflected light.
- **Boundary:** Topic 02 owns full crust-rock-plate and geological-structure
  analysis; Topic 03 owns earthquake-wave mechanics and hazard; Topic 12 owns
  ocean circulation. Topic 01 retains only the foundation needed for its
  universe, coordinate, time and India-location demands.
- **Verified PYQ ownership, 2018-2026:** direct routes include the 2019 and
  2022 solstice questions, 2021 subcontinent Mains demand, 2024 aurora Mains
  demand and 2024-2025 latitude/star/axis/IDL objective demands. Locally
  unavailable or merely available keys are not converted into invented answer
  letters.""",
    6: """### Semantic-completeness ownership and PYQ control

- **Owned core:** glacier formation and movement; accumulation, ablation and
  mass balance; equilibrium-line altitude, snowline, firn line and terminus;
  plucking, abrasion, glacial erosion and deposition; cirque-arête-horn,
  U-shaped trough, hanging valley, roche moutonnée, fjord, till, moraines,
  drumlins, eskers and outwash; Himalayan glacier-river mapping, glacial lakes
  and GLOF risk.
- **Process control:** snowfall and refreezing → firn and flowing ice →
  plucking/abrasion and debris transport → till or meltwater deposition.
  Glacier retreat or overdeepening can create/expand a lake; slope/ice entry,
  inflow, piping or erosion can produce overtopping or dam failure and a
  sediment-laden downstream flood.
- **Scale/map control:** snow grain, glacier, catchment, Himalayan sector,
  glacial-lake dam and downstream valley are separate scales. Gangotri-
  Bhagirathi, Zemu-Teesta, Bara Shigri-Chenab and Siachen-Nubra-Shyok-Indus are
  map hooks, not claims about political boundaries or uniform basin response.
- **Date/data control:** glacier or lake counts, areas, retreat rates, mass
  balance, hazard classes and monitoring lists require inventory boundary,
  sensor/method, observation period and issuing agency. A dated inventory is
  not a present-day rate or proof that every mapped lake is dangerous.
- **Terminology control:** snowfield differs from glacier; ELA from climatic
  snowline, firn line and snout; retreat from reversal of ice flow; till from
  sorted outwash; fjord from ria; glacial-lake hazard from downstream risk.
- **Causal control:** warming can alter glacier and lake conditions but does
  not by itself establish an event-specific GLOF cause. Dam material,
  freeboard, slope instability, displacement waves, inflow, valley geometry,
  exposure, warning and infrastructure vulnerability must be tested.
- **Boundary:** Topic 05 owns river-system and basin-transfer analysis; Topic
  09 owns general lake/wetland classification; Topic 10 owns relative sea-level
  and coasts; Disaster Management owns response doctrine. Topic 06 retains the
  cryosphere process, Himalayan map and GLOF hazard-to-risk chain.
- **Verified PYQ ownership, 2018-2026:** direct routes include the 2019
  glacier-river matching objective demand, 2020 Himalayan glacier-loss and
  Indian water-resources Mains demand, and 2023 fjord Mains demand. No
  unavailable objective key, glacier count, retreat rate or hazard ranking is
  invented.""",
    7: """### Semantic-completeness ownership and PYQ control

- **Owned core:** climatic aridity and desert distribution; mechanical and
  salt weathering; aeolian creep, saltation, suspension, deflation and
  abrasion; yardangs, ventifacts, pediments, bajadas, wadis, playas and dune
  types; the Thar's physical mosaic, desertification drivers, canal trade-offs,
  land-degradation neutrality and process-matched restoration.
- **Process control:** moisture deficit and sparse cover → weathering and
  sediment availability → threshold wind or episodic runoff → erosion,
  transport and deposition. Desertification is diagnosed when climatic
  variability and/or human pressure reduce dryland productivity and recovery,
  not when a dune simply exists or shifts.
- **Scale/map control:** grain, dune, slope, closed basin, Thar subregion,
  dryland class and national atlas pixel are separate scales. Western dune
  fields, eastern Aravalli transition, Luni-playa system and canal-command
  tracts cannot be represented by one uniform desert condition.
- **Date/data control:** the SAC atlas reports 2018-19 mapped condition, not a
  2026 measurement. Its 97.85 million hectares and 29.77 percent of India's
  geographical area are baseline-period national values; they do not provide a
  current Thar-only percentage or prove programme impact.
- **Terminology control:** desert differs from aridity, drought, land
  degradation and UNCCD desertification; barchan from transverse,
  longitudinal, parabolic and star dunes; pediment from bajada; playa from the
  wider desert; restoration commitment from measured restoration outcome.
- **Causal control:** wind is not the sole geomorphic agent and people are not
  inherently a degradation driver. Cover removal, grazing intensity, tillage,
  groundwater stress, mining, infrastructure, irrigation, drainage and
  rainfall variability interact differently by site and timescale.
- **Boundary:** Topic 04 owns weathering and groundwater foundations; Topic 18
  owns hot- and mid-latitude desert climate; Environment and Ecology owns the
  direct UNCCD/desertification policy PYQ and Great Indian Bustard conservation.
  Topic 07 owns arid landforms and the Thar degradation application.
- **Verified PYQ ownership, 2018-2026:** no direct Geography Topic 07 route is
  present in the checked central ledgers. The 2020 Mains desertification demand
  remains with Environment and Ecology and is used only as a bounded
  cross-owner application; no direct question or objective key is invented.""",
    2: """### Semantic-completeness ownership and PYQ control

- **Owned core:** compositional and rheological Earth layers; seismic evidence;
  minerals and complete rock cycle; igneous, sedimentary and metamorphic
  processes; continental drift, seafloor spreading, plate boundaries, isostasy,
  orogeny and Wilson-cycle logic; India's cratons, mobile belts, basins, Deccan
  volcanics, Himalaya and Indo-Gangetic foredeep.
- **Process control:** source material → melting/weathering/deposition or
  pressure-temperature change → texture/mineral assemblage → uplift/exposure →
  renewed cycling. Plate motion is explained through boundary kinematics and
  mantle/lithosphere interaction rather than one memorised driver.
- **Scale/map control:** mineral, hand specimen, outcrop, terrane, plate and
  physiographic-region scales are distinct. Rock age, tectonic event, present
  relief and mineral occurrence are not assumed to share one boundary.
- **Chronology control:** Precambrian craton assembly, Proterozoic basins,
  Gondwana rifting/sedimentation, Deccan flood basalt, India-Eurasia collision
  and continuing Himalayan deformation remain separate stages.
- **Terminology control:** crust differs from lithosphere; shield from craton
  and platform; plate from continent; fold from fault-block mountain; magma
  from lava; texture, structure, composition and origin are not synonyms.
- **Causal control:** geological association supports a probability, not
  deterministic mineral or hazard prediction. Ages, thicknesses and rates are
  approximate unless attached to a named official map/publication and scale.
- **Boundary:** Topic 03 owns eruption style, active seismicity and seismic
  zones; Topic 04 owns weathering products, slope transfer and aquifers; Topic
  06 owns glacial landforms. Topic 02 owns the lithological-tectonic substrate.
- **Verified PYQ ownership, 2018-2026:** direct routes include 2018 magnetic
  reversal, 2022 primary rocks, 2023 Indian hill ranges, 2024 mountain types,
  2025 continental-drift evidence and crustal tectonics, and the provisional
  2026 Peninsular Block demand. Provisional or unavailable keys remain
  explicitly unpromoted.""",
    3: """### Semantic-completeness ownership and PYQ control

- **Owned core:** magma generation, ascent, viscosity/gas controls, intrusive
  and extrusive forms, eruption products and styles; elastic rebound, faults,
  focus/epicentre, P-S-surface waves, magnitude/intensity, tsunami generation;
  global belts and India's Himalayan, Kachchh, Peninsular, Andaman and Barren
  Island settings.
- **Process control:** tectonic/thermal setting → melt or strain accumulation →
  ascent/rupture → eruption or wave radiation → site/water-column response →
  hazard. A submarine earthquake creates a tsunami only where rapid water-column
  displacement is sufficient.
- **Scale/map control:** vent, volcanic field, plate boundary and seismic belt;
  fault source, epicentral region, site response and national zone map are
  separated. A zone is a design/hazard generalisation, not an event prediction.
- **Date/status control:** eruption status, recent earthquake catalogues,
  seismic-zone standard and monitoring statements require issuing agency,
  observation/publication date and version. Detection count is network-dependent.
- **Terminology control:** active/dormant/extinct are evidence-based activity
  classes, not a compulsory life cycle; magnitude differs from intensity;
  focus from epicentre; monitoring and early warning from prediction.
- **Causal control:** hazard is not disaster. Exposure, vulnerability, soil,
  depth, construction and preparedness mediate loss; no single tremor validates
  a deterministic recurrence or zone change.
- **Boundary:** Topic 02 owns full plate/rock foundations; Disaster Management
  owns response doctrine and resilient-construction depth; Topic 06 owns GLOF.
  Topic 03 owns physical mechanism, distribution and bounded India seismicity.
- **Verified PYQ ownership, 2018-2026:** direct routes include 2018 Barren
  Island and mantle plume, 2020 Circum-Pacific characteristics, 2021 eruption
  impacts, 2023 seismic waves, 2024 eruption products, 2025 tsunami Mains and
  the provisional 2026 Tungurahua route. No unavailable/provisional objective
  key is promoted.""",
    4: """### Semantic-completeness ownership and PYQ control

- **Owned core:** mechanical, chemical and biological weathering; regolith and
  soil linkage; erosion versus mass movement; slope forces, triggers and
  movement types; infiltration, percolation, porosity, permeability, aquifers,
  water table, recharge/discharge, quality, depletion and Indian groundwater/
  landslide settings.
- **Process control:** rock/mineral and climate → in-situ breakdown → regolith;
  slope/material/discontinuity/antecedent moisture → trigger → slide/flow/fall/
  creep; precipitation/irrigation → infiltration → aquifer storage and flow →
  discharge or pumping response.
- **Scale/map control:** grain/pore, soil profile, hillslope, catchment, aquifer
  and assessment-unit scales are distinct. Himalayan and Western Ghats
  landslide regimes require separate lithology, relief, rainfall and land-use
  explanations.
- **Date/data control:** groundwater recharge, extraction stage, assessment-unit
  category, notified area and landslide-susceptibility map require agency,
  assessment year, methodology and scale. National values cannot diagnose one
  aquifer or district.
- **Terminology control:** weathering differs from erosion; erosion from mass
  movement; porosity from permeability; aquifer from aquitard; water table from
  piezometric surface; susceptibility, hazard, vulnerability and risk differ.
- **Causal control:** intense rain is a trigger, not a complete landslide cause;
  pumping is a stress, not proof of one depletion mechanism. Antecedent
  moisture, discontinuities, toe cutting, drainage, recharge and demand must be
  tested before attribution.
- **Boundary:** Topic 05 owns fluvial erosion, drainage and river-basin
  transfers; Topic 07 desertification; Topic 08 karst caves; Topic 09
  lakes/wetlands; Topic 10 coastal erosion. Topic 04 owns in-situ breakdown,
  slope transfer and groundwater.
- **Verified PYQ ownership, 2018-2026:** direct routes include 2018 urban water
  harvesting, 2021 black-soil formation, 2023 groundwater withdrawal, 2024
  rainfall-weathering and 2025 chalk-clay permeability. The 2021 landslide
  comparison is Disaster-Management-owned and the 2024 Gangetic-groundwater
  demand is Topic-36-owned; both remain bounded bridges.""",
    5: """### Semantic-completeness ownership and PYQ control

- **Owned core:** drainage basin and network organisation; runoff, erosion,
  transport, deposition and graded-profile adjustment; upper/middle/lower
  course landforms; drainage patterns, antecedence, superimposition and capture;
  Himalayan/Peninsular systems, major India drainage logic and interlinking.
- **Process control:** rainfall/snowmelt and basin controls → discharge and
  sediment calibre → erosion/transport/deposition → channel/floodplain/delta
  adjustment. Interlinking is traced from identified donor/recipient basins
  through storage, canal/tunnel and seasonal transfer to ecological/social
  effects.
- **Scale/map control:** channel reach, drainage basin, river system and
  inter-basin project are separate. River direction, tributary junction,
  gorge/waterfall, delta/estuary and proposed link are located rather than
  inferred from a state name.
- **Chronology/status control:** antecedent drainage predates uplift; capture
  differs from planned diversion. Project proposal, statutory clearance, work
  award, construction, completion and delivered benefit remain separate dated
  statuses.
- **Terminology control:** drainage pattern differs from basin; delta from
  estuary; levee from embankment; meander cutoff from river capture; donor
  'surplus' is a modelling/seasonal claim, not timeless unused water.
- **Causal control:** one dam or climate trend does not alone explain a delta,
  flood or drought. Sediment, discharge seasonality, subsidence, tides/waves,
  embankments, environmental flows, displacement, federal consent and climate
  uncertainty must qualify conclusions.
- **Boundary:** glaciers/GLOF remain Topic 06; deserts Topic 07; caves/karst
  Topic 08; lakes/wetlands Topic 09; coastal forms Topic 10. Topic 05 owns
  running-water landforms, India drainage and interlinking only.
- **Verified PYQ ownership, 2018-2026:** direct routes include the 2020
  interlinking Mains demand, 2021 Indus tributaries and Eastern-Ghats rivers,
  2022 Gandikota, 2024 waterfall matching and provisional 2026 drainage-shift
  and antecedent-river demands. Objective keys absent or provisional remain
  unpromoted.""",
    8: """### Semantic-completeness ownership and PYQ control

- **Owned core:** carbonate dissolution and precipitation; soluble-rock,
  structural, recharge, gradient, outlet and time controls; epikarst, vadose
  and phreatic zones; karren, dolines, uvalas, poljes, swallow holes, caves and
  speleothems; Indian natural-cave mapping; proxy interpretation; geological-
  time hierarchy, GSSP method, Mawmluh Cave and the Meghalayan Age.
- **Process control:** soil CO2 + water → weak carbonic acid → carbonate
  dissolution along joints/bedding → conduit and closed-depression development;
  degassing or evaporation → calcite deposition. A palaeoclimate inference
  requires climate → recharge → drip chemistry → speleothem proxy → independent
  chronology, with uncertainty at every link.
- **Scale/map control:** mineral reaction, fracture, passage, cave system,
  catchment, proxy site and global chronostratigraphic boundary are separate.
  Meghalaya, Borra and Belum are natural caves; Ajanta and Ellora are human
  rock-cut architecture and cannot be used as karst-genesis evidence.
- **Chronology/data control:** host-rock age, cave excavation age, speleothem
  growth age, occupation age and formal time-unit boundary are not
  interchangeable. The Meghalayan GSSP is at 7.45 mm depth in KM-A and dated
  4.200 ± 0.030 ka before 1950, equivalent to 4.250 ± 0.030 ka b2k; this does
  not date Mawmluh Cave as a whole.
- **Terminology control:** cave differs from karst landscape and human-cut
  monument; dissolution from speleothem deposition; stalactite from stalagmite;
  Age/Stage from Epoch/Series; GSSP point from correlation event and interval;
  formal unit from informal Anthropocene usage.
- **Causal control:** the 4.2 ka event is a correlation guide with spatially
  variable hydroclimatic expressions. It cannot by itself prove a uniform
  global drought or single-cause collapse of Indus, Mesopotamian or other
  societies; social resilience and multiple stresses require evidence.
- **Boundary:** Topic 04 owns groundwater foundations; Indian Art and Culture
  owns rock-cut architecture; History owns occupation and civilisation change;
  Environment owns cave biodiversity policy. Topic 08 owns karst process,
  natural caves, proxy method and the formal Meghalayan boundary.
- **Verified PYQ ownership, 2018-2026:** no direct Geography Topic 08 route is
  present in the checked central ledgers. Ajanta and adjacent cave-shrine
  questions remain with their routed cultural owners; no direct PYQ, cave
  ranking or official key is invented.""",
    9: """### Semantic-completeness ownership and PYQ control

- **Owned core:** lake and wetland definitions; genetic lake classification;
  water budget, residence time, stratification, turnover, trophic state,
  eutrophication, succession and shrinkage; wetland hydroperiod, connectivity
  and services; Indian lake-origin and river-link maps; Ramsar wise use,
  criteria, Montreux Record, Wetlands Rules 2017 and restoration sequencing.
- **Process control:** basin origin establishes the initial form; precipitation,
  inflow and groundwater inputs minus evaporation, outflow and seepage govern
  storage; nutrients, flushing, mixing and decomposition govern oxygen stress.
  Restoration begins with catchment and hydrological diagnosis, not cosmetic
  lake-front treatment.
- **Scale/map control:** water body, lake basin, floodplain, wetland complex,
  catchment and Ramsar site boundary are separate. Wular-Jhelum, Kolleru
  between the Krishna-Godavari deltas, Loktak-phumdis, Chilika lagoon, Sambhar
  saline basin and Lonar impact basin retain exact spatial/genetic qualifiers.
- **Date/data control:** Ramsar designation count, site name, area, ecological
  character and Montreux status are dynamic. India's tally is 101 after Glaw
  Lake's 3 August 2026 designation; the MoEFCC list dated 21 April 2026 records
  the earlier tally of 99 and is not silently treated as the latest count.
- **Terminology control:** lake differs from wetland and reservoir; lagoon from
  inland lake; origin from trophic state and legal status; eutrophication from
  natural succession and water-budget shrinkage; Ramsar designation from
  National Park notification; Montreux Record from a funding or heritage list.
- **Causal control:** area decline, algal bloom or biodiversity loss does not
  establish one cause. Inflow regulation, abstraction, groundwater, sewage,
  nutrients, sediment, invasive species, encroachment, temperature and
  connectivity must be separated by site and period.
- **Boundary:** Topic 05 owns fluvial landforms and drainage; Topic 08 owns
  karst caves; Topic 10 owns coastal morphology; Environment and Ecology owns
  full wetland biodiversity and regulatory-policy depth. Topic 09 owns lake
  genesis, limnology, Indian mapping and bounded wetland governance.
- **Verified PYQ ownership, 2018-2026:** direct Geography routes include 2018
  human-caused lake shrinkage and artificial-lake identification, 2019
  reservoir identification, 2021 Rajasthan saline lakes, 2023 river-lake
  matching and provisional 2026 Lake Turkana. The 2021 urban-water-body Mains
  demand remains Environment-owned; unavailable/provisional keys are not
  invented.""",
    10: """### Semantic-completeness ownership and PYQ control

- **Owned core:** wave generation and refraction; hydraulic action, abrasion,
  attrition and solution; cliff-notch-platform and cave-arch-stack sequences;
  beaches, berms, longshore drift, spits, bars, lagoons and tombolos; emergent
  and submergent coasts; relative sea level, storm surge, India's east-west
  coastal contrast, shoreline change and CRZ-CZMP governance.
- **Process control:** wind-wave energy, bathymetry and refraction → erosion or
  swash/backwash transport → sediment-cell redistribution → shoreline
  adjustment. Relative sea-level change combines ocean-volume change with
  vertical land movement, subsidence and local dynamics; regulation then maps
  categories and permissible activities through approved CZMPs.
- **Scale/map control:** grain, beach profile, littoral cell, estuary/delta,
  state coast, HTL/LTL line, CRZ category and project site are separate scales.
  India's east-west contrast is a broad tendency with local exceptions, not a
  universal coast label or substitute for a site map.
- **Date/status control:** NCCR's 33.6 percent eroding, 26.9 percent accreting
  and 39.6 percent stable classes refer to the analysed 1990-2018 mainland
  coastline and are not annual rates. CRZ Notification 2019 is S.O. 37(E)
  dated 18 January 2019; amendments, CZMP approval, appraisal, clearance and
  compliance remain distinct dated legal states.
- **Terminology control:** shoreline differs from coast and legal HTL; erosion
  from inundation; spit from bar and tombolo; lagoon from lake; ria from fjord;
  astronomical tide from storm surge; hazard line from a universal setback or
  project-clearance line.
- **Causal control:** sea-level rise alone does not explain a local erosion
  reach. Sediment supply, dams, ports, sand mining, storms, currents, coastal
  structures, subsidence and measurement period interact; hard protection can
  transfer erosion downdrift.
- **Boundary:** Topic 05 owns fluvial sediment and deltas from the basin side;
  Topic 09 owns lakes/wetlands; Topic 11 owns islands and coral reefs; Disaster
  Management owns warning/evacuation depth; Environment owns marine ecology.
  Topic 10 owns coastal landforms, sediment-cell reasoning and CRZ application.
- **Verified PYQ ownership, 2018-2026:** the direct route is the 2023 GS-I
  coastline resource-potential and natural-hazard preparedness demand.
  Mangrove, blue-carbon, coral and tsunami questions remain with their routed
  Environment, island or Disaster Management owners; no direct CRZ PYQ or
  objective key is invented.""",
}

CANONICAL_OWNER_CONTROLS.update(
    {
        11: """### Semantic-completeness ownership and PYQ control

- **Owned core:** continental, volcanic, coral and depositional island origins;
  coral-polyp symbiosis and growth controls; fringing, barrier and atoll
  morphology; Darwin and Daly models; bleaching, recovery and reef services;
  Andaman-Nicobar tectonic-arc and Lakshadweep coral-system geography; Great
  Nicobar's biosphere, hazard, rights and project-appraisal setting.
- **Process control:** crustal separation, volcanism or sediment/reef
  accumulation produces different island foundations. Reef growth follows
  polyp calcification, symbiosis and suitable light-water conditions; stress
  can cause bleaching, while prolonged stress can produce mortality and
  framework erosion.
- **Scale/map control:** reef colony, reef tract, reef island, island group,
  tectonic arc and project landscape are separate scales. Ten Degree Channel
  separates Andaman from Nicobar; Nine Degree Channel separates Minicoy from
  the main Lakshadweep group.
- **Date/data control:** project capacity, cost, forest diversion, tree
  estimates, tribal-reserve area, clearance stage and litigation status require
  an exact official source and date. Static island origin is never updated by a
  project factsheet, and a clearance condition is not a measured outcome.
- **Terminology control:** coral animal differs from reef framework and reef
  island; fringing from barrier reef and atoll; bleaching from death; biosphere
  reserve zoning from a whole-island no-use rule; environmental clearance from
  Stage-I and Stage-II forest approval.
- **Causal control:** Darwinian subsidence is not a universal reef history, and
  reef presence alone does not remove tsunami or surge risk. Great Nicobar
  appraisal must combine strategic rationale with cumulative ecology, seismic-
  tsunami exposure, freshwater, indigenous rights, alternatives, safeguards
  and monitored compliance.
- **Boundary:** Topic 03 owns full earthquake mechanics; Topic 10 owns coastal
  sediment cells and CRZ; Topic 12 owns ocean circulation; Environment owns
  wider marine-biodiversity law. Topic 11 owns island/reef formation, Indian
  island comparison and the bounded Great Nicobar appraisal.
- **Verified PYQ ownership, 2018-2026:** direct routes are the 2018 Prelims
  coral-distribution/biodiversity demand and 2019 GS-I global-warming impact on
  coral life. Barren Island, biorock and island-state sea-level questions retain
  their routed owners; no unavailable official key is invented.""",
        12: """### Semantic-completeness ownership and PYQ control

- **Owned core:** surface and density-driven circulation; gyres, boundary
  currents, Ekman transport, upwelling and fisheries; tide-generating forces,
  spring-neap cycle and local range; salinity budget, halocline and
  stratification; Arabian Sea-Bay contrast; seasonal North Indian Ocean
  reversal, Somali upwelling, IOD mechanism and observing architecture.
- **Process control:** wind stress plus Coriolis, pressure gradient, basin shape
  and friction organises surface flow; heat and freshwater budgets change
  density and mixing; coastal wind-Ekman divergence drives upwelling; zonal
  SST, thermocline, wind and convection anomalies form the coupled IOD.
- **Scale/map control:** wave, tide, eddy, surface current, water mass and
  overturning branch remain distinct. Every North Indian Ocean arrow carries a
  season, and every IOD claim carries basin sectors, phase and observation or
  forecast window.
- **Date/data control:** DMI values, IOD phase, outlook probabilities, mooring
  observations, marine heat and monsoon links require a dated IMD/INCOIS
  bulletin. A forecast is not an observation and a seasonal index is not a
  permanent basin label.
- **Terminology control:** warm/cold current is relative; current transports
  water while a wave mainly transmits energy; spring/neap describe alignment,
  not seasons; salinity differs from density; IOD differs from ENSO and from a
  single western-basin temperature anomaly.
- **Causal control:** upwelling raises nutrient supply but does not guarantee a
  fishery. IOD modifies rainfall probability through coupled circulation, but
  timing, amplitude, ENSO, MJO and internal variability prevent deterministic
  all-India rainfall claims.
- **Boundary:** Topic 13 owns weather elements and western disturbances; Topic
  16 owns the complete Indian monsoon mechanism. Topic 12 owns ocean
  circulation, tides, salinity, seasonal current reversal and IOD coupling.
- **Verified PYQ ownership, 2018-2026:** direct routes are the 2019 GS-I
  currents-versus-water-masses/marine-life demand and 2022 GS-I forces
  influencing currents and fishing. No current phase or official key is
  manufactured.""",
        13: """### Semantic-completeness ownership and PYQ control

- **Owned core:** radiation-temperature-pressure-humidity-stability-cloud-
  precipitation relations; pressure-gradient, Coriolis and friction controls;
  upper-air Rossby waves and jet streams; subtropical westerly jet, polar-front
  jet and tropical easterly jet distinctions; western-disturbance genesis,
  tracks, moisture, precipitation and Indian seasonal effects.
- **Process control:** thermal and pressure gradients organise winds; upper-air
  wave troughs and embedded extratropical disturbances travel eastward in the
  westerlies, acquire moisture and interact with Himalayan relief to produce
  winter rain or snow.
- **Scale/map control:** station observation, synoptic system, upper-air wave,
  seasonal jet position and climatological regime are separate scales. A
  western disturbance is mapped from West Asia/Mediterranean-linked westerlies
  toward north-west India, not as a western branch of the monsoon.
- **Date/data control:** observed rain/snow, system count, track, intensity,
  seasonal anomaly and forecast require a dated IMD bulletin or observation.
  One event cannot prove a permanent jet shift or long-term climate trend.
- **Terminology control:** weather differs from climate; humidity from relative
  humidity and dew point; jet stream from surface wind; trough from cyclone;
  western disturbance from monsoon depression; observation from nowcast,
  forecast and seasonal outlook.
- **Causal control:** jet position steers and supports systems but is not a
  single deterministic switch. Blocking, trough amplitude, moisture supply,
  orography and synoptic evolution condition precipitation and impacts.
- **Boundary:** Topic 12 owns IOD/ocean circulation; Topic 14 owns climate
  classification; Topic 16 owns monsoon mechanism. Topic 13 owns weather
  elements, upper-air circulation and western-disturbance process.
- **Verified PYQ ownership, 2018-2026:** retain only routed questions on weather
  elements, jet-stream/upper-air controls or western disturbances; reconstructed
  wording and unavailable keys remain labelled rather than promoted.""",
        14: """### Semantic-completeness ownership and PYQ control

- **Owned core:** weather-versus-climate distinction; Köppen temperature,
  precipitation and seasonality logic; A/B/C/D/E major groups and subordinate
  letters; Indian climatic-region mapping through latitude, altitude,
  continentality, relief and monsoon seasonality; strengths and limits of
  threshold classification.
- **Process control:** long-period temperature and precipitation regimes are
  classified through stated thresholds, then explained through circulation,
  relief, distance from sea and altitude. Codes describe patterns; they do not
  independently cause vegetation or agriculture.
- **Scale/map control:** station normal, grid cell, climatic region,
  vegetation biome, agro-climatic zone and administrative boundary are separate
  units. Indian transition belts and mountains cannot be reduced to one
  permanent sharp code line.
- **Date/data control:** normals, rainfall/temperature anomalies, heat or cold
  records and revised maps require dataset, base period, resolution and issuing
  agency. A current season is not a climate normal and a map classification is
  not timeless.
- **Terminology control:** climate region differs from biome and agro-climatic
  region; aridity threshold from rainfall total alone; Af from Am/Aw; Cs from
  Cw/Cf; highland mosaics from a single universal Köppen H category.
- **Causal control:** code correlation does not prove ecological or economic
  determination. Transitional climates, altitude, soil, disturbance,
  irrigation and land use qualify climate-vegetation and climate-crop links.
- **Boundary:** Topic 13 owns weather observation and upper-air process; Topics
  15-25 own individual climate types; Topic 16 owns India's monsoon mechanism.
  Topic 14 owns classification logic and the comparative Indian regional map.
- **Verified PYQ ownership, 2018-2026:** retain routed classification and
  Indian-climate-region demands only; no station code, revised map boundary or
  objective key is invented without a controlled source.""",
        15: """### Semantic-completeness ownership and PYQ control

- **Owned core:** hot-wet equatorial/Af location, convergence and convection;
  temperature and rainfall rhythm; rainforest stratification, lianas,
  epiphytes, nutrient cycling, shifting cultivation, plantations and logging;
  India's monsoon-and-orography-controlled evergreen analogue, distribution,
  biodiversity, jhum and official forest-evidence boundaries.
- **Process control:** persistent heat and moisture drive convection, rapid
  decomposition and fast root uptake; dense biomass stores much nutrient
  capital, while clearing exposes leached soils. Evergreen structure follows
  moisture continuity but varies with relief, disturbance and seasonality.
- **Scale/map control:** global Af lowland, Indian evergreen belt, forest-type
  polygon, forest-cover grid, recorded forest area and legal protected category
  are separate. Western Ghats, North-East, eastern Himalayan foothills and
  Andaman-Nicobar are mapped as regional belts with transitions.
- **Date/data control:** forest-cover totals, very-dense/moderately-dense/open
  classes, forest-type extent, change and fire observations require the exact
  FSI report edition, reference period and mapping definition. No national
  forest-cover figure is relabelled as evergreen-forest extent.
- **Terminology control:** Af climate differs from India's monsoonal evergreen
  analogue; evergreen from semi-evergreen; luxuriant biomass from fertile soil;
  forest cover from recorded forest area, forest type and legal forest status;
  jhum from a universally destructive practice.
- **Causal control:** climate permits evergreen forest but does not alone
  determine present cover. Orography, soils, fragmentation, fire, logging,
  tenure, fallow length and conservation institutions condition outcomes.
- **Boundary:** Topic 14 owns classification; Topic 16 owns monsoon mechanism;
  Topic 17 owns deciduous forests and grasslands. Topic 15 owns Af process and
  India's wet-evergreen analogue without importing those later topics.
- **Verified PYQ ownership, 2018-2026:** direct routes are the 2021 Prelims
  rainforest-structure demand and 2023 Prelims nutrient/decomposition demand.
  The local ledgers withhold official answer letters, so none is invented.""",
        16: """### Semantic-completeness ownership and PYQ control

- **Owned core:** tropical monsoon versus tropical marine identity; seasonal
  land-sea pressure reversal; northward ITCZ/monsoon-trough migration;
  cross-equatorial flow and Coriolis turning; Mascarene High, Somali jet,
  Tibetan-Himalayan heating/barrier effects, subtropical-westerly and tropical-
  easterly jet reorganisation; onset/burst, advance, Arabian Sea and Bay
  branches, depressions, active-break spells, withdrawal and northeast monsoon;
  ENSO, IOD and MJO modulation.
- **Process control:** differential heating establishes a seasonal pressure
  gradient, but the realised monsoon requires coupled ocean-atmosphere flow,
  cross-equatorial moisture transport, convergence, upper-air reorganisation,
  relief and rain-bearing systems. No single thermal, jet or teleconnection
  switch explains onset, spatial distribution or seasonal outcome.
- **Scale/map control:** sea breeze, cross-equatorial current, branch,
  depression, monsoon trough, active/break spell, meteorological subdivision
  and all-India season are separate scales. Arabian Sea and Bay routes,
  Western-Ghat windward/leeward contrast, north-east entry, Ganga-plain path
  and Coromandel retreat rain are mapped without treating one branch as the
  whole monsoon.
- **Date/data control:** onset normal, declared onset, advance line, daily or
  cumulative rainfall, monthly/seasonal outlook, LPA/base period and end-season
  verification are different IMD products. The 2026 season remains incomplete
  on 5 September; forecasts and observations are not promoted as final
  seasonal outcomes.
- **Terminology control:** monsoon is a seasonal circulation reversal/system,
  not merely heavy rain or a giant sea breeze; onset/burst differs from active
  spell, break and withdrawal; northeast monsoon differs from western
  disturbance; ENSO and IOD are interannual probability modifiers while MJO is
  intraseasonal.
- **Causal control:** land-sea contrast is necessary but insufficient.
  Tibetan heating, snow/soil state, Mascarene High, Somali jet, trough position,
  Bay systems, orography, ENSO, IOD and MJO interact, so a national total cannot
  explain every regional agricultural or flood/drought outcome.
- **Boundary:** Topic 12 owns ocean currents and IOD mechanics; Topic 13 owns
  weather elements, jets and western disturbances; Topic 14 owns climate
  classification; Topic 15 owns Af/evergreen systems; Topic 17 owns Aw,
  deciduous forest and grassland. Topic 16 alone owns the complete Indian
  monsoon mechanism and tropical-marine comparison.
- **Verified PYQ ownership, 2018-2026:** direct ownership includes the 2023
  GS-I Purvaiya/Bhojpur demand and the 2026 Andaman-Nicobar climate and
  seasonal-precipitation objective route. The 2026 Set-A key remains
  provisional, so no answer letter is promoted.""",
        17: """### Semantic-completeness ownership and PYQ control

- **Owned core:** Aw/Sudan transition and ITCZ wet-dry rhythm; rainfall
  unreliability; parkland grass-tree structure; drought adaptations; coupled
  climate-fire-herbivory controls; wildlife and pastoral/cropping responses;
  Indian moist deciduous, dry deciduous, thorn and distinct grassland mosaics;
  restoration logic and dated official forest/landscape evidence.
- **Process control:** seasonal ITCZ migration creates wet and dry seasons;
  moisture duration controls growth while fire, browsing, grazing, soils and
  land use regulate tree recruitment and maintain or degrade open mosaics.
  Leaf shedding is a dry-season water strategy, not proof that the forest is
  evergreen or dead.
- **Scale/map control:** global Aw belt, regional savanna, Indian forest-type
  polygon, forest-cover grid and site-specific grassland are separate. Terai
  floodplain grassland, shola montane mosaic and Banni arid-saline grassland
  cannot share one rainfall threshold or management prescription.
- **Date/data control:** rainfall bands are textbook guides with regional
  overlap. Forest cover, recorded forest area, ecological forest type,
  plantation and legal status require a named FSI edition and definition;
  project areas, restoration targets and outcomes require dated official
  evidence.
- **Terminology control:** moist deciduous differs from dry deciduous, thorn
  forest, scrub and evergreen forest; savanna differs from steppe; natural open
  ecosystem differs from degraded or deforested land; restoration differs from
  dense tree planting.
- **Causal control:** climate permits deciduous forest or grassland but does
  not uniquely determine present structure. Fire timing, herbivory, grazing
  pressure, invasives, hydrology, soil, fragmentation and tenure condition
  outcomes; tree-density increase is not automatically ecological improvement.
- **Boundary:** Topic 15 owns evergreen forests; Topic 16 owns complete monsoon
  circulation; Topic 18 owns desert biome and Great Indian Bustard linkage;
  Topic 07 owns desertification mechanics. Topic 17 owns exact deciduous,
  thorn and Indian grassland distinctions without absorbing those topics.
- **Verified PYQ ownership, 2018-2026:** the direct route is the 2021 Prelims
  savanna tree-limitation demand. The local ledger withholds the official
  answer letter, so rainfall seasonality, fire and herbivory are taught without
  manufacturing a key.""",
        18: """### Semantic-completeness ownership and PYQ control

- **Owned core:** aridity as moisture deficit; hot BWh versus cold/mid-latitude
  BWk deserts; subtropical subsidence, offshore flow, cold-current stability,
  continentality and rain-shadow causation; rainfall and thermal regimes;
  flash floods, xerophytes, oases and water strategies; Thar map, aridity,
  landforms, drainage and adaptation; Great Indian Bustard open-biome
  conservation and infrastructure trade-offs.
- **Process control:** descending or stable air, weak moisture supply,
  continental distance and mountain barriers combine differently by desert.
  Rare high-intensity rain can generate wadi floods, while groundwater and
  engineered transfer support settlement but can create depletion, salinity
  and waterlogging.
- **Scale/map control:** global desert belt, Thar core and transition margin,
  dune/playa/Luni catchment, canal command, renewable-energy corridor and GIB
  habitat are separate layers. The Thar lies mainly west of the Aravallis;
  their broad parallelism to the Arabian Sea branch limits forced ascent but
  is not the sole cause of aridity.
- **Date/data control:** rainfall guides, land-degradation maps, canal effects,
  GIB counts, breeding-centre totals, power-line mitigation, court/expert
  process and UNCCD decisions retain source, observation date and status.
  Captive-stock figures are not wild-population estimates and announced
  measures are not verified habitat outcomes.
- **Terminology control:** desert differs from desertification and drought;
  aridity from heat; hot desert from mid-latitude desert; fog from rainfall;
  oasis from rain-fed forest; GIB open habitat from wasteland; bird diverter,
  rerouting and undergrounding are distinct mitigation options.
- **Causal control:** Topic 07 desertification is not duplicated here. Topic 18
  explains desert-biome controls and owns the Thar-GIB species-habitat linkage:
  irrigation, roads, fencing, settlement, agriculture and renewable
  transmission can transform the same open landscape in different ways.
- **Boundary:** Topic 07 owns land-degradation/desertification diagnosis and
  national restoration policy; Topic 17 owns deciduous forests/grasslands;
  Environment owns full species-law doctrine. Topic 18 owns global desert
  climate, Thar regional geography and the bounded GIB habitat-infrastructure
  conservation application.
- **Verified PYQ ownership, 2018-2026:** the audited Geography ledgers contain
  no direct Topic 18 question. Desert lakes/landforms, land degradation and
  biodiversity questions retain their routed owners; no PYQ wording, marks or
  answer key is fabricated.""",
        19: """### Semantic-completeness ownership and PYQ control

- **Owned core:** Cs western-margin location; summer subtropical-high
  subsidence and winter westerly/frontal rain; local winds; sclerophyll
  adaptations; orchard, vine, winter-cereal and wildfire-water systems; India's
  Himalayan temperate-fruit analogue, chilling, frost/hail, slope and valley
  siting, perishability, cold chain and market access.
- **Process control:** poleward summer pressure-belt migration produces
  subsidence and drought; equatorward winter westerlies bring cyclonic rain.
  Orchard suitability follows cultivar-specific chilling, dormancy and
  bud-break plus spring-frost, hail, heat, moisture and harvest-weather risks.
- **Scale/map control:** Mediterranean basin, global Cs region, Himalayan
  state, valley, elevation belt, orchard and market corridor are distinct.
  Kashmir/Himachal/Uttarakhand horticulture is a functional analogue, not a
  mapped Mediterranean climate or proof of uniform upslope migration.
- **Date/data control:** crop area, production, productivity, price, import
  duty, crop loss and altitude/chilling trends require year, estimate stage,
  crop/cultivar, state and official source. Advance estimates remain
  provisional; all-India fruit totals are not apple or Himalayan-state totals.
- **Terminology control:** Mediterranean climate differs from Mediterranean
  agriculture; sclerophyll from deciduous forest; chilling requirement from a
  simple cold temperature; frost from hail; climatic suitability from realised
  production; production from productivity and marketed arrivals.
- **Causal control:** warmer winters can reduce chilling at some sites, but
  cultivar, altitude, aspect, frost, hail, rainfall, irrigation, pests,
  pollination, transport, storage and prices jointly determine output and
  farmer returns. No single bad season proves a permanent belt shift.
- **Boundary:** Topic 19 owns global Mediterranean mechanism and India's
  Himalayan fruit-belt analogy. Agricultural-statistics and climate-impact
  claims remain dated; viticulture and saffron are bounded comparisons rather
  than substitutes for the apple-belt core.
- **Verified PYQ ownership, 2018-2026:** the audited routing ledgers contain no
  direct Topic 19 question. Orchard, climate-change and agricultural-value-
  chain questions may supply cross-owner applications, but no solved PYQ or
  objective key is invented.""",
        20: """### Semantic-completeness ownership and PYQ control

- **Owned core:** temperate continental steppe location and local names;
  continentality, low-to-moderate summer precipitation and hemisphere
  contrast; grass-height gradient, fire/grazing and chernozem formation;
  mechanised grain/ranching economy, transport conversion and ecological
  costs; India's alluvial Rabi wheat-granary analogy, Green Revolution,
  procurement geography and sustainability.
- **Process control:** weak maritime moderation produces large annual thermal
  range; moisture deficit limits trees while grass-root turnover and low
  leaching build humus-rich soils. Fertility and level relief became a granary
  only through rail, mechanisation, market access and institutions.
- **Scale/map control:** steppe biome, named regional grassland, national wheat
  output, state production, procurement state, Indo-Gangetic alluvial belt and
  farm groundwater unit are separate. Punjab-Haryana-western Uttar Pradesh is
  a functional granary core, not India's only wheat area or a true chernozem
  steppe.
- **Date/data control:** wheat area, output, yield, procurement, MSP, stocks and
  state shares require crop year or Rabi Marketing Season, estimate stage and
  issuing agency. Third Advance Estimate is not final output; procurement is
  not production, and MSP is not the open-market price.
- **Terminology control:** steppe differs from savanna and prairie is a
  regional name rather than a universal climate code; chernozem differs from
  black cotton soil and Indo-Gangetic alluvium; Rabi crop differs from winter
  rainfall crop; production, marketed surplus and government procurement are
  distinct.
- **Causal control:** climate and soil enable wheat but do not determine the
  granary. HYV seed, irrigation, fertiliser, mechanisation, procurement and
  market access explain concentration; groundwater depletion, residue burning,
  nutrient imbalance, heat and terminal-weather risk qualify its durability.
- **Boundary:** Topic 17 owns tropical savanna/deciduous systems; Topic 19 owns
  Mediterranean orchard agriculture. Topic 20 owns the steppe mechanism and
  India wheat-granary analogy; broader MSP, food-stock and crop-diversification
  policy remains bounded cross-owner context.
- **Verified PYQ ownership, 2018-2026:** the audited routing ledgers contain no
  direct Topic 20 question. Adjacent climate, soil, cropping and food-security
  demands remain with their routed owners, so no solved PYQ or key is
  fabricated.""",
        21: """### Semantic-completeness ownership and PYQ control

- **Owned core:** warm-temperate eastern-margin location; China, Gulf and
  Natal sub-types; summer onshore flow, winter continental outflow, typhoon
  exposure, summer-rain agriculture and the contrast with Mediterranean
  western margins; Bengal-Brahmaputra and Humid North-East application.
- **Process control:** seasonal land-ocean pressure contrast draws warm moist
  maritime air onshore in summer and permits cooler, drier continental outflow
  in winter. The same moisture pathway supports rice and tea and, with basin
  relief and channel conditions, contributes to flood hazard.
- **Scale/map control:** global eastern-margin climate, East Asian monsoon
  coast, Bengal plain, Brahmaputra valley, hill belt and station are separate
  scales. R.L. Singh's Humid North-East excludes Tripura; the wider Northeast
  and every humid-subtropical map are not interchangeable.
- **Date/data control:** storm track, flood level, affected population, cropped
  area and tea output require a dated JMA/IMD/CWC/ASDMA/Tea Board release.
  Textbook rainfall and temperature ranges remain classification evidence,
  not a September 2026 observation.
- **Terminology control:** China type is not China's whole climate; Gulf type
  is slight-monsoonal and Natal type non-monsoonal. Humid subtropical,
  tropical monsoon, perhumid highland and floodplain are related but distinct.
- **Causal control:** Bay-of-Bengal moisture is the primary Northeast monsoon
  branch, but relief, convergence, basin sediment and floodplain occupation
  condition rainfall and loss. A typhoon track or flood bulletin is not proof
  of a long-term climatic trend.
- **Boundary:** Topic 16 owns the complete Indian monsoon mechanism; Topic 17
  owns deciduous/grassland systems; Disaster Management owns response doctrine
  and Environment owns biodiversity policy. Topic 21 owns the eastern-margin
  climate and bounded Bengal-Northeast climatic analogue.
- **Verified PYQ ownership, 2018-2026:** the audited routing ledgers contain no
  direct Topic 21 question. Climate-comparison, monsoon and flood applications
  remain bounded bridges; no solved PYQ or objective key is fabricated.""",
        22: """### Semantic-completeness ownership and PYQ control

- **Owned core:** cool-temperate western-margin distribution; permanent
  Westerlies, maritime moderation, frontal/cyclonic and relief rain; mild
  winters, cool summers, small annual range, deciduous forest and dairying;
  Himalayan moist, wet and dry temperate forest analogues.
- **Process control:** onshore Westerlies plus warm-current influence and
  frontal systems moderate temperature and distribute rain through the year.
  In the Himalaya altitude, aspect, monsoon exposure and rain shadow replace
  latitude as the primary zonation controls.
- **Scale/map control:** NW European region, narrow British Columbia strip,
  southern Chile/Tasmania/New Zealand margins, Himalayan slope, forest belt
  and stand are distinct. A 1,500-3,300 metre textbook belt is approximate and
  cannot be treated as one fixed contour across the Himalaya.
- **Date/data control:** forest cover, fire detections, burned area, snow or
  moisture anomaly and restoration outcome require a dated FSI/state/IMD
  source. ISFR 2023 is an assessment edition, not a 2026 forest-condition
  measurement, and forest cover is not temperate-forest extent.
- **Terminology control:** British type equals marine west coast, not every
  temperate coast; deciduous differs from coniferous and mixed forest; deodar
  is a conifer, chir pine is mainly subtropical montane, and dry temperate
  forest differs from the humid middle-slope belt.
- **Causal control:** resinous litter, dry weather and ignition can accelerate
  fire, but chir pine alone does not prove cause. Forest-floor storage can
  support springs, yet geology, soil depth, rainfall, extraction and land use
  also govern catchment response.
- **Boundary:** Topic 19 owns Mediterranean climate; Topics 23-24 own
  subalpine/alpine and Eastern-Himalaya/Laurentian comparisons. Environment
  owns forest-conservation policy. Topic 22 owns British-type mechanism and the
  Himalayan temperate-forest zonation/water-security analogy.
- **Verified PYQ ownership, 2018-2026:** the routed 2024 Prelims Marine West
  Coast demand tests low annual/daily range and year-round precipitation. Its
  official answer letter is not invented; other forest questions retain their
  routed owners.""",
        23: """### Semantic-completeness ownership and PYQ control

- **Owned core:** Northern-Hemisphere Siberian/subarctic distribution; severe
  continental winters, short summers and low summer-maximum precipitation;
  taiga conifers, softwood economy, below-ground carbon, fire-permafrost
  feedback and Himalayan subalpine-alpine analogue.
- **Process control:** weak maritime moderation produces extreme annual range;
  cold limits decomposition and deep rooting, favouring conifers and long-term
  soil/peat/permafrost carbon storage. Warming can increase fire and thaw,
  exposing stored carbon and weakening frozen-ground bearing capacity.
- **Scale/map control:** boreal biome, forest stand, discontinuous/continuous
  permafrost zone, seasonal active layer, Himalayan slope, treeline and alpine
  meadow are separate. India's subalpine and alpine belts are altitudinal
  analogues, not fragments of continental taiga.
- **Date/data control:** fire area, permafrost temperature, active-layer depth,
  carbon balance, treeline shift and forest cover require a dated
  NOAA/FSI/research series with baseline and spatial domain. One season cannot
  establish a permanent biome shift.
- **Terminology control:** taiga is boreal conifer forest south of tundra;
  permafrost is ground at or below 0°C for at least two consecutive years and
  differs from seasonal frost; treeline, snowline and timberline are not
  synonyms; bugyals/mergs are alpine meadows, not forests.
- **Causal control:** cold is necessary but not sufficient for vegetation
  pattern. Moisture, active-layer depth, fire, insects, wind, aspect, snow
  persistence, grazing and land use condition boreal and Himalayan outcomes.
- **Boundary:** Topic 22 owns lower/middle Himalayan temperate forests; Topic
  25 owns tundra, ice cap and polar amplification. Environment owns species
  and protected-area policy. Topic 23 owns taiga process plus the
  subalpine-treeline-alpine transition.
- **Verified PYQ ownership, 2018-2026:** the audited routing ledgers contain no
  direct Topic 23 question. Boreal, permafrost and Himalayan-belt demands are
  bounded applications; no solved PYQ or answer key is fabricated.""",
        24: """### Semantic-completeness ownership and PYQ control

- **Owned core:** Laurentian distribution in northeastern North America and
  eastern Asia; cold dry continental winter, warm summer-rain maximum, mixed
  forest, warm-cold current convergence, fog and shelf fisheries; Eastern
  Himalaya cool-humid analogue.
- **Process control:** winter Westerlies carry cold dry continental air toward
  the eastern margin, while summer maritime inflow supplies rain. Where warm
  moist air crosses a cold current over a broad shelf, cooling favours fog;
  nutrient supply and mixing support productivity but do not guarantee catch.
- **Scale/map control:** ocean-current boundary, shelf fishing ground,
  Laurentian climate region, Eastern-Himalayan slope, Teesta basin and tea
  estate are separate. India has no true Laurentian climate; Darjeeling,
  Sikkim and Arunachal form an altitude-controlled comparison.
- **Date/data control:** fish-stock status, tea output/yield, GI or project
  status, GLOF/flood level, road closure and forest cover require a dated
  official source. The 2023 South Lhonak event remains a dated case, not a
  timeless description of every Teesta hazard.
- **Terminology control:** Laurentian differs from warmer China type and drier
  Siberian interior; fog differs from precipitation; potential fishery
  productivity differs from sustainable catch; the Teesta joins the
  Brahmaputra/Jamuna system, not the Ganga.
- **Causal control:** current convergence alone does not create or sustain a
  fishery; shelf geometry, nutrient pathways, food webs and governance matter.
  Eastern-Himalayan loss requires relief, rain, sediment, infrastructure and
  exposure analysis rather than climate-only attribution.
- **Boundary:** Topic 21 owns warm eastern margins; Topic 22 the marine western
  margin; Topic 23 the Siberian interior; Topic 06 full GLOF process.
  Environment owns conservation policy. Topic 24 owns Laurentian mechanism and
  the bounded Eastern-Himalaya/Teesta/Darjeeling analogue.
- **Verified PYQ ownership, 2018-2026:** the audited routing ledgers contain no
  direct Topic 24 question. Adjacent climate, fishery and regional-geography
  demands retain their owners; no solved PYQ or key is fabricated.""",
        25: """### Semantic-completeness ownership and PYQ control

- **Owned core:** tundra ET and ice-cap EF thresholds; polar radiation and
  cold-desert precipitation; permafrost, vegetation and Indigenous livelihood;
  Arctic-Antarctic asymmetry; sea ice, ice shelves and grounded ice; albedo,
  carbon, circulation and access pathways; Ladakh cold-desert comparison and
  India's polar research.
- **Process control:** low sun angle, polar night and high albedo constrain the
  energy budget; snow/ice retreat lowers albedo and reinforces warming.
  Permafrost thaw changes hydrology, ground strength and carbon release, while
  only loss of grounded land ice directly adds ocean mass.
- **Scale/map control:** Arctic Ocean basin, Greenland ice sheet, Antarctic ice
  sheet, floating sea ice and ice-shelf field, tundra landscape, Ladakh valley and
  Himalayan glacier are separate. Ladakh is a high-altitude rain-shadow cold
  desert and process analogue, not a polar climate or administrative proxy for
  the whole trans-Himalaya.
- **Date/data control:** sea-ice extent, glacier/ice-sheet mass balance,
  permafrost state, route season, expedition count and Maitri-II status require
  a dated NOAA/NSIDC/NCPOR/MoES release and stated baseline. A proposal or
  design competition is not an operational station.
- **Terminology control:** tundra ET has a warmest month above 0°C but below
  10°C; ice-cap EF remains below 0°C year-round. Floating sea ice differs from
  grounded ice and ice shelf; polar desert means low precipitation; Arctic
  amplification is not identical to global mean warming.
- **Causal control:** sea-ice loss does not directly raise sea level, and
  Arctic-mid-latitude weather links remain confidence-graded rather than
  settled. Ladakh aridity follows rain shadow, altitude and continentality,
  not heat, and winter western disturbances provide limited snow.
- **Boundary:** Topic 06 owns Himalayan glacier/GLOF detail; Topic 07 and Topic
  18 own Thar/desertification and hot-desert climate; Topic 23 owns taiga and
  subalpine transition. Environment owns species/conservation policy. Topic 25
  owns polar processes, scale rules and the Indian cold-desert/polar bridge.
- **Verified PYQ ownership, 2018-2026:** the direct route is 2021 GS-I Q15 on
  melting Arctic ice, Antarctic glaciers and weather patterns. The answer must
  open with ocean-versus-continent and floating-versus-grounded distinctions,
  then grade sea-level, circulation, carbon and weather-link confidence.""",
    }
)

GEOGRAPHY_LIVE_OFFICIAL_SOURCES: dict[int, tuple[list[str], str]] = {
    1: (
        [
            "https://surveyofindia.gov.in/pages/political-map-of-india",
            "https://surveyofindia.gov.in/pages/physical-map-of-india",
        ],
        "Rechecked 2026-09-05: Survey of India's official political and "
        "physical map portals remain the authority for India's mapped extent "
        "and boundary depiction. The package retains 8°4′N-37°6′N, "
        "68°7′E-97°25′E and 82°30′E only as source-dated map/time controls; "
        "it does not infer a current boundary length or administrative count.",
    ),
    2: (
        [
            "https://bhukosh.gsi.gov.in",
            "https://www.gsi.gov.in/publications/",
        ],
        "Rechecked 2026-09-05: GSI's Bhukosh and official publications "
        "portals remain the authoritative live access points for geological "
        "maps and map-scale metadata. The static craton-basin-Deccan-Himalaya "
        "framework is not converted into an unsourced mineral prediction, "
        "exact age or fixed terrane boundary.",
    ),
    3: (
        [
            "https://riseq.seismo.gov.in/riseq/earthquake/recent_earthquake",
            "https://seismo.gov.in/data-portal",
            "https://www.bis.gov.in/other/PRESS_NOTE.pdf",
            "https://ndma.gov.in/sites/default/files/PDF/Guidelines-Earthquakes.pdf",
        ],
        "Rechecked 2026-09-05: NCS supplies dated event catalogue and network "
        "data, while BIS/NDMA control seismic-zone and structural-safety "
        "references. The package retains Zones II-V and event metadata only "
        "with source/version discipline; catalogued tremors are not treated "
        "as prediction or evidence that a zone has changed.",
    ),
    4: (
        [
            "https://gsi.gov.in/landslide-hazard/",
            "https://bhusanket.gsi.gov.in/NLSM_10K_Map.html",
            "https://cgwb.gov.in/en/ground-water-resource-assessment-0",
            "https://cgwb.gov.in/cgwbpnm/public/publication-detail/1741",
        ],
        "Rechecked 2026-09-05: GSI/Bhusanket remains the official landslide-"
        "susceptibility source and CGWB's 2025 national compilation is the "
        "latest located official dynamic-groundwater assessment. National or "
        "assessment-unit values are used only with year, method and scale; "
        "they are not projected onto a local slope or aquifer.",
    ),
    5: (
        [
            "https://nwda.gov.in/content/innerpage/ken-betwa-link-project.php",
            "https://nwda.gov.in/upload/jal%20VikasApril%202026.pdf",
            "https://nwda.gov.in/upload/Ken-Betwa%20Link%20Project%20.pdf",
        ],
        "Rechecked 2026-09-05: NWDA's April 2026 Jal Vikas and Ken-Betwa "
        "project material identify Ken-to-Betwa as under implementation. The "
        "package does not restate volatile cost, command-area, completion or "
        "benefit-delivery figures and keeps project status distinct from "
        "ecological outcome or basin-wide drought proofing.",
    ),
    6: (
        [
            "https://vedas.sac.gov.in/en/Himalayan_Glacier_Inventory_Atlas.html",
            "https://www.isro.gov.in/Satellite_Insights_Expanding_Glacial_Lakes_Indian_Himalayas.html",
            "https://cwc.gov.in/glacial-lake-outburst-floods-glof",
            "https://cwc.gov.in/glacial-lakeswater-bodies-himalayan-region",
            "https://mitigation.ndma.gov.in/ndmahr-admin/public/uploads/advertisement_document/file63791735554350.pdf",
        ],
        "Rechecked 2026-09-05: SAC's official Himalayan Glacier Inventory "
        "Atlas remains the inventory portal. ISRO's 22 April 2024 satellite "
        "assessment compares 2,431 glacial lakes larger than 10 hectares in "
        "the 2016-17 inventory with the 1984-onward record and identifies 676 "
        "expanding lakes, including 130 within India; these are inventory- and "
        "period-specific observations, not current GLOF probabilities. CWC's "
        "official GLOF explainer and monitoring portal require close monitoring "
        "of Himalayan glacial lakes, while NDMA's national guideline supplies "
        "the hazard-assessment, warning, mitigation and preparedness framework. "
        "No lake is labelled dangerous from area growth alone.",
    ),
    7: (
        [
            "https://vedas.sac.gov.in/vedas/dsm_atlas.html",
            "https://www.sac.gov.in/data/Publication/128/Desertification_and_Land_Degradation_Atlas_of_India_2021.pdf",
            "https://pib.gov.in/PressReleseDetailm.aspx?PRID=1727987",
            "https://moef.gov.in/uploads/2023/07/NAP%20final-2023.pdf",
            "https://www.unccd.int/land-and-life/land-degradation-neutrality/overview",
        ],
        "Rechecked 2026-09-05: SAC's 2021 Desertification and Land "
        "Degradation Atlas remains the latest located official nationwide "
        "mapping baseline. It reports 97.85 million hectares, or 29.77 percent "
        "of India's geographical area, under land degradation/desertification "
        "during 2018-19. MoEFCC's 2023 National Action Plan retains the "
        "26-million-hectare restoration ambition for 2030, while UNCCD defines "
        "LDN through avoiding, reducing and reversing degradation. The atlas "
        "values are not relabelled as September 2026 conditions, a Thar-only "
        "rate or verified restoration achievement.",
    ),
    8: (
        [
            "https://stratigraphy.org/ICSchart/ChronostratChart2026-06.pdf",
            "https://quaternary.stratigraphy.org/major-divisions",
            "https://www.iugs.org/the-anthropocene-iugs-ics-statement/",
            "https://www.iugs.org/wp-content/uploads/2024/03/Anthropocene_short_IUGS-ICS_Statement-1.pdf",
        ],
        "Rechecked 2026-09-05: the ICS June 2026 chart retains the Holocene "
        "and Meghalayan. The official Quaternary page identifies the Upper/"
        "Late Holocene Meghalayan Stage/Age GSSP at 7.45 mm depth in the KM-A "
        "speleothem from Mawmluh Cave, ratified 14 June 2018 and modelled at "
        "4.200 ± 0.030 ka before 1950 (= 4.250 ± 0.030 ka b2k). IUGS-ICS "
        "continues to treat Anthropocene as an informal term after rejecting "
        "formal epoch status in March 2024. None of these facts dates the cave "
        "as a whole or proves a uniform global drought/civilisation collapse.",
    ),
    9: (
        [
            "https://www.ramsar.org/news/india-designates-glaw-lake-wetland-international-importance",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=2294036&reg=48&lang=1",
            "https://www.ramsar.org/news/thats-century-india-names-its-100th-wetland-international-importance",
            "https://moef.gov.in/ramsar-convention",
            "https://moef.gov.in/uploads/pdf-uploads/pdf_698ae4f8f28953.18411376.pdf",
            "https://indianwetlands.in/",
            "https://moef.gov.in/regulatory-framework-wetlands-rules",
        ],
        "Rechecked 2026-09-05: Ramsar Convention and PIB announcements record "
        "Glaw Lake, Arunachal Pradesh, as India's 101st Ramsar site on 3 August "
        "2026, after Jai Prakash Narayan Bird Sanctuary became the 100th in "
        "June. MoEFCC's Ramsar page and list dated 21 April 2026 still record "
        "99 sites, demonstrating why every count needs an as-of date. Ramsar "
        "designation remains international recognition and wise-use duty, not "
        "automatic National Park status or proof of ecological health; domestic "
        "regulation remains anchored in the Wetlands Rules 2017.",
    ),
    10: (
        [
            "https://environmentclearance.nic.in/writereaddata/CRZ_Notifications/CRZ_Notification_2019/0.pdf",
            "https://environmentclearance.nic.in/report/CRZ_Notifications.aspx",
            "https://environmentclearance.nic.in/report/CRZ_circulars.aspx",
            "https://pib.gov.in/PressReleasePage.aspx?PRID=1982315",
            "https://ncscm.res.in/",
        ],
        "Rechecked 2026-09-05: the official environment-clearance portal "
        "retains CRZ Notification 2019, S.O. 37(E) dated 18 January 2019, and "
        "lists subsequent notifications including S.O. 4886(E) dated "
        "26 November 2021 and S.O. 4648(E), 4649(E) and 4650(E), each dated "
        "30 September 2022. Its circulars page also lists the 13 October 2023 "
        "SOP for authorised CRZ mapping agencies. No later 2025-26 textual "
        "amendment was located on the official portal. PIB/NCCR's 33.6/26.9/"
        "39.6 percent shoreline classes remain explicitly tied to the "
        "1990-2018 assessment rather than a current annual erosion rate.",
    ),
}

GEOGRAPHY_LIVE_OFFICIAL_SOURCES.update(
    {
        11: (
            [
                "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/may/doc202651860401.pdf",
                "https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/may/doc202651861901.pdf",
                "https://www.sansad.in/getFile/annex/270/AU1486_8zAFvF.pdf?source=pqars",
                "https://environmentclearance.nic.in/Proposal_status.aspx",
                "https://www.unesco.org/en/mab/great-nicobar",
                "https://lakshadweep.gov.in/about-lakshadweep/",
            ],
            "Rechecked 2026-09-05: the 1 May 2026 PIB backgrounder describes "
            "the proposed port, airport, power plant and township and states "
            "that prior environmental clearance carries 42 conditions. The "
            "Rajya Sabha answer dated 12 February 2026 states that Stage-II or "
            "final forest approval had not been granted and that project "
            "activities could begin only after Stage-II approval and the final "
            "forest-diversion order; it also records pending NGT and Calcutta "
            "High Court proceedings. No later official Stage-II grant was "
            "located on the public PARIVESH/forest-clearance search surfaces "
            "through 5 September 2026. These changeable legal and project "
            "claims remain separate from static island, reef, channel and "
            "biosphere geography; official safeguards are commitments or "
            "conditions, not verified ecological outcomes.",
        ),
        12: (
            [
                "https://incois.gov.in/portal/osf/osf.jsp",
                "https://incois.gov.in/portal/datainfo/mb.jsp",
                "https://incois.gov.in/portal/datainfo/rama.jsp",
                "https://mausam.imd.gov.in/responsive/seasonal_forecast.php",
                "https://mausam.imd.gov.in/responsive/climate_services.php",
            ],
            "Rechecked 2026-09-05: INCOIS remains the authoritative operational "
            "source for Indian Ocean observations, including OMNI/RAMA "
            "moorings. IMD's live ENSO-IOD bulletin retrieved on 5 September "
            "states that neutral IOD conditions presently prevail; the latest "
            "MMCFS forecast retains neutral conditions through its forecast "
            "period, while international centres give positive IOD the second-"
            "highest probability later in the season. This is a dated "
            "observation-plus-forecast, not a permanent basin label or a "
            "deterministic monsoon or fishery outcome. No DMI value is asserted "
            "without a stated observation month and base period.",
        ),
        13: (
            [
                "https://mausam.imd.gov.in/responsive/all_india_forcast_bulletin.php",
                "https://mausam.imd.gov.in/Forecast/marquee_data/Press%20Release%2004-09-2026.pdf",
                "https://mausam.imd.gov.in/responsive/rsmc.php",
                "https://mausam.imd.gov.in/responsive/climate_services.php",
            ],
            "Rechecked 2026-09-05: IMD's press release dated 4 September 2026 "
            "observed a fresh Western Disturbance as a middle- and upper-"
            "tropospheric trough roughly along 64°E north of 32°N. Its rainfall "
            "outlook was explicitly issued under several simultaneous synoptic "
            "systems, so no realised or forecast rainfall is attributed to the "
            "disturbance alone. The package teaches the static jet/Rossby-wave/"
            "western-disturbance mechanism while keeping observation, nowcast, "
            "forecast, warning, impact and climatology separate; one dated "
            "trough does not establish a long-term jet trend.",
        ),
        14: (
            [
                "https://mausam.imd.gov.in/responsive/climate_services.php",
                "https://mausam.imd.gov.in/responsive/rainfallinformation.php",
                "https://mausam.imd.gov.in/responsive/monsooninformation.php",
                "https://mausam.imd.gov.in/Forecast/marquee_data/Outlook_September_2026.pdf",
            ],
            "Rechecked 2026-09-05: IMD climate services and dated rainfall, "
            "temperature and monsoon products control any current observation "
            "or anomaly. IMD's September 2026 monthly outlook, issued "
            "31 August 2026, is treated only as a dated forecast product and "
            "not as a climatological normal or a revision of a Köppen boundary. "
            "No official new national Köppen map or revised climatic-region "
            "line was located. Every changing value requires product date, "
            "normal/base period, spatial resolution and observed-versus-"
            "forecast status.",
        ),
        15: (
            [
                "https://fsi.nic.in/publications",
                "https://fsi.nic.in/uploads/isfr2023/isfr_book_eng-vol-1_2023.pdf",
                "https://fsi.nic.in/uploads/isfr2023/isfr_book_eng-vol-2_2023.pdf",
            ],
            "Rechecked 2026-09-05: FSI's official publications surface still "
            "lists India State of Forest Report 2023 as the latest located "
            "biennial national assessment. Its forest-cover, forest-type and "
            "state tables are dated evidence products, not a September 2026 "
            "measurement. No national forest-cover total or change is "
            "relabelled as tropical evergreen-forest extent, and forest cover, "
            "recorded forest area, forest type and legal status remain "
            "separate.",
        ),
        16: (
            [
                "https://mausam.imd.gov.in/Forecast/marquee_data/KerlaOnset_2026.pdf",
                "https://mausam.imd.gov.in/Forecast/marquee_data/Outlook_September_2026.pdf",
                "https://mausam.imd.gov.in/imd_latest/contents/cumulative_rainfall_activity.php",
                "https://mausam.imd.gov.in/responsive/monsooninformation.php",
            ],
            "Rechecked 2026-09-05: IMD declared southwest-monsoon onset over "
            "Kerala on 4 June 2026, against the 1 June climatological normal. "
            "Its September outlook, issued 31 August, forecasts below-normal "
            "September rainfall over India as a whole; the live cumulative-"
            "rainfall and monsoon-progress products remain observations through "
            "their stated dates. Onset, forecast, observed cumulative rainfall "
            "and final June-September verification are kept separate, and no "
            "incomplete-season value is presented as the final 2026 monsoon "
            "outcome.",
        ),
        17: (
            [
                "https://fsi.nic.in/publications",
                "https://fsi.nic.in/uploads/isfr2023/isfr_book_eng-vol-1_2023.pdf",
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2214525",
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2262834&reg=3&lang=1",
            ],
            "Rechecked 2026-09-05: FSI still exposes ISFR 2023 as the latest "
            "located official national forest assessment. PIB's current "
            "Aravalli Green Wall material describes a multi-state landscape-"
            "restoration programme using native vegetation, water restoration "
            "and community coordination, while 2026 official material also "
            "identifies Banni as an open-grassland restoration and habitat "
            "landscape. Reported forest cover is not deciduous-forest extent, "
            "a project target is not an achieved ecological outcome, and "
            "natural grassland is not treated as vacant land for dense "
            "plantation.",
        ),
        18: (
            [
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2246400&reg=3&lang=2",
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2272725&reg=3&lang=1",
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2083802",
                "https://moef.gov.in/wildlife-wl",
                "https://www.unccd.int/cop16",
                "https://www.unccd.int/convention/cop-decisions",
            ],
            "Rechecked 2026-09-05: PIB records the 26 March 2026 Kutch hatch "
            "under the interstate jumpstart approach and, on 14 June 2026, a "
            "captive/conservation-breeding-centre stock of 94 Great Indian "
            "Bustards after three additional chicks. Those figures describe "
            "the managed conservation population, not a wild national census. "
            "Official conservation material continues to treat habitat "
            "protection, breeding and power-line collision mitigation as "
            "linked measures; diverters, rerouting and undergrounding remain "
            "site-specific options rather than proof of completed risk removal. "
            "UNCCD COP16 dates and decisions remain separately sourced. Topic "
            "07's desertification inventory is not duplicated.",
        ),
        19: (
            [
                "https://agriwelfare.gov.in/en/StatHortEst",
                "https://nhb.gov.in/OnlineClient/rptProduction.aspx",
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2271770&reg=48&lang=1",
            ],
            "Rechecked 2026-09-05: the Department of Agriculture and Farmers "
            "Welfare lists 2024-25 Final Estimates published 18 March 2026 and "
            "2025-26 Second Advance Estimates published 12 June 2026 for "
            "horticulture. The latter reports higher aggregate fruit output "
            "with apple among contributing crops, but its summary is not "
            "relabelled as a Himalayan-state apple tonnage. Exact apple area, "
            "production and productivity require the crop/state table and "
            "estimate stage; advance estimates remain provisional, and no "
            "unsupported upslope-shift, price or loss figure is asserted.",
        ),
        20: (
            [
                "https://agriwelfare.gov.in/Documents/Time_Series_3rdAE_2025_26_En.pdf",
                "https://agriwelfare.gov.in/en/AdvanceEstimate",
                "https://fci.gov.in/",
                "https://pib.gov.in/PressReleasePage.aspx?PRID=2255618&reg=3&lang=1",
            ],
            "Rechecked 2026-09-05: the Department of Agriculture and Farmers "
            "Welfare's Third Advance Estimates for 2025-26 report wheat output "
            "at 1,206.57 lakh tonnes. This remains an advance estimate, not a "
            "final crop estimate. FCI/Food Ministry releases control any Rabi "
            "Marketing Season procurement, stock and state-share claim; "
            "procurement is not production, MSP is not a market-price series, "
            "and no volatile procurement total is used without its exact "
            "marketing season and release date.",
        ),
        21: (
            [
                "https://asdma.assam.gov.in/",
                "https://asdma.assam.gov.in/sites/default/files/swf_utility_folder/departments/asdma_revenue_uneecopscloud_com_oid_70/menu/document/declaration_of_floods_2026_natural_disaster001.pdf",
                "https://cwc.gov.in/sites/default/files/SOP_April_2026-FFM.pdf",
                "https://rsms.cwc.gov.in/frameWork/web/bulletin-report-page",
                "https://www.jma.go.jp/jma/en/Activities/rsmc.html",
            ],
            "Rechecked 2026-09-05: ASDMA's 2026 flood declaration and live "
            "portal, CWC's April 2026 flood-forecasting SOP and bulletin "
            "surface, and JMA's RSMC Tokyo portal are the dated authorities "
            "for changing Assam flood and western North Pacific cyclone "
            "status. No district count, affected-population total, river "
            "level, crop loss, storm intensity or track is quoted without its "
            "bulletin date. The static Bay-of-Bengal moisture, relief and "
            "Brahmaputra floodplain mechanisms remain distinct from any one "
            "2026 event.",
        ),
        22: (
            [
                "https://fsi.nic.in/isfr-volume-i?pgID=isfr-volume-i",
                "https://fsi.nic.in/uploads/isfr2023/isfr_book_eng-vol-1_2023.pdf",
                "https://fsi.nic.in/uploads/isfr2023/isfr_book_eng-vol-2_2023.pdf",
                "https://fsiforestfire.gov.in/",
            ],
            "Rechecked 2026-09-05: Forest Survey of India's publication "
            "surface still identifies ISFR 2023, released in December 2024, "
            "as the latest located national forest assessment; its state and "
            "forest-fire tables are dated evidence, not a September 2026 "
            "measurement. Forest cover is not Himalayan temperate-forest "
            "extent, a satellite fire detection is not burned area or cause, "
            "and no current fire count or trend is asserted without the "
            "observation period and issuing authority.",
        ),
        23: (
            [
                "https://arctic.noaa.gov/report-card/report-card-2025/",
                "https://arctic.noaa.gov/report-card/report-card-2025/headlines-and-overview/",
                "https://fsi.nic.in/isfr-volume-i?pgID=isfr-volume-i",
                "https://fsiforestfire.gov.in/",
            ],
            "Rechecked 2026-09-05: NOAA's Arctic Report Card 2025 covers "
            "October 2024-September 2025 and reports continuing rapid Arctic "
            "warming, permafrost-linked landscape change and northward "
            "ecosystem shifts. It is a completed annual assessment, not a "
            "real-time September 2026 boreal-fire or permafrost inventory. "
            "FSI's latest located national assessment remains ISFR 2023; no "
            "Himalayan forest-cover, high-elevation fire, carbon-stock or "
            "treeline-shift number is promoted without dataset, period and "
            "spatial boundary.",
        ),
        24: (
            [
                "https://fsi.nic.in/isfr-volume-i?pgID=isfr-volume-i",
                "https://cwc.gov.in/en/glacial-lake-outburst-floods-glof",
                "https://cwc.gov.in/sites/default/files/advisory-sheet-glacial-lake-outburst-flood-south-lhonak-system-in-teesta-river-basin.pdf",
                "http://ssdma.nic.in/Uploads/resources/SIKKIM%20PDNA.pdf",
            ],
            "Rechecked 2026-09-05: FSI's latest located national forest "
            "assessment remains ISFR 2023. CWC's GLOF portal/advisory and "
            "SSDMA's Sikkim GLOF Post-Disaster Needs Assessment retain the "
            "4 October 2023 South Lhonak-Teesta event as a dated case study, "
            "not a current basin-wide condition or a template for every "
            "Eastern-Himalayan valley. Any new lake status, flood level, road "
            "closure, forest change or conservation outcome requires its own "
            "dated official release; fishery and tea-production statistics "
            "are omitted from the changing-status anchor.",
        ),
        25: (
            [
                "https://arctic.noaa.gov/report-card/report-card-2025/",
                "https://arctic.noaa.gov/report-card/report-card-2025/headlines-and-overview/",
                "https://nsidc.org/arcticseaicenews/",
                "https://ncpor.res.in/",
                "https://www.isea.ncpor.res.in/Documents/Advisory/2026/AL-01%20Planning%20Advisory%20-%20Antarctic%20Expedition-2026.pdf",
                "https://www.moes.gov.in/static/uploads/2026/03/e60113076d48467ec1e261da616aa8bb.pdf",
            ],
            "Rechecked 2026-09-05: NOAA's Arctic Report Card 2025 is a dated "
            "October 2024-September 2025 assessment; it reports the March "
            "2025 winter sea-ice maximum as the lowest in the 47-year "
            "satellite record and September 2025 as the tenth-lowest minimum. "
            "Those completed-period observations are not relabelled as 2026 "
            "conditions. NCPOR's live institutional and 2026 expedition "
            "surfaces confirm India's continuing polar programme; MoES's "
            "March 2026 parliamentary material controls changing "
            "infrastructure claims. Maitri-II planning is not counted as an "
            "operational station, and every sea-ice, ice-sheet, expedition or "
            "station-status claim retains its date, variable and scale.",
        ),
    }
)


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources, current_note = GEOGRAPHY_LIVE_OFFICIAL_SOURCES.get(
        topic.number,
        (
            provenance.get("live_sources") or [],
            provenance.get("current_linkage_note") or (
                "The static physical-geography core needs no volatile claim. "
                "Any hazard event, project, designation, regulatory status, "
                "climate anomaly or count must retain an official source, "
                "observation date and status boundary."
            ),
        ),
    )
    source_lines = "\n".join(f"- `{path}`" for path in live_sources) or (
        "- No live source is required for the static physical-geography claim."
    )
    return f"""### DEEP-REVIEW LEARNING CONTRACT

| Control | Binding rule for this package |
|---|---|
| Syllabus boundary | Complete physical process, spatial pattern and India anchor are taught before optional Advanced depth. |
| Causal method | Initial condition → energy/force or driver → mechanism → landform/climate/ocean pattern → consequence → feedback/limit. |
| Spatial method | Latitude, altitude, continentality, relief, plate setting, basin/coast orientation and map scale are explicit. |
| Terminology | Close terms are defined on common axes; process, form, region, hazard, regulation and current status are never collapsed. |
| Evidence method | Claim → named place/map/process/official record → analysis → qualification. |
| Practice contract | Every solved item has demand decoding, a detailed examiner-grade model, executable timed/compression plan, marks rationale and answer-specific improvement. |
| Approval | This immutable successor remains `approved: false` pending explicit approval. |

**Canonical Basic/Core owner:** `{rel(topic.basic_path)}`  
**Canonical topic owner:** `{rel(topic.canonical_path)}`  
**Optional Advanced owner:** `{rel(topic.advanced_path)}`  
**Official syllabus mapping:** `{rel(SYLLABUS_MAPPING)}`

### EVIDENCE, PYQ AND CURRENT-STATUS CONTROL

- **Process discipline:** no feature is listed without formation sequence, controlling variables and a limiting condition.
- **Map discipline:** distribution is reconstructed through latitude, plate/relief setting, wind/current direction, drainage/coast orientation and named anchors.
- **Quantitative discipline:** coordinates, thresholds, magnitudes, dates, counts and project dimensions retain units, source/date and uncertainty.
- **Causal discipline:** association is not treated as sufficiency; interacting controls, scale, lag, feedback and exceptions are stated.
- **PYQ discipline:** repository routing ledgers and held papers control wording and metadata; reconstructed wording and unavailable official keys remain labelled.
- **Status discipline:** every changeable claim retains an official source, observation date and status boundary.
- **Current-status note, rechecked {DATE}:** {current_note}

**Live/official context sources rechecked for this generation:**

{source_lines}
"""


_geography_owner_augment = augment_topic_semantic_content


def augment_topic_semantic_content(
    topic: Topic,
    markdown: str,
    *,
    workbook: bool = False,
) -> str:
    """Insert the bounded Geography owner ledger once in learner-facing Core."""
    repaired = _geography_owner_augment(topic, markdown, workbook=workbook)
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
                f"Treat “{focus}” as a process, location, scale, terminology and "
                "status problem. Verify every statement independently."
            ),
            "plan": (
                "Fix the phenomenon and spatial setting; trace the controlling "
                "mechanism; test direction, sequence, threshold and India/world "
                "anchor; eliminate the closest term, map or causation distractor."
            ),
            "why": (
                "It preserves exact process-to-pattern reasoning and prevents a "
                "familiar place-name or correlation from substituting for causation."
            ),
            "improve": (
                f"For “{focus}”, state why the nearest distractor fails on process, "
                "direction, scale, location, terminology, date or official status."
            ),
        }
    return {
        "demand": (
            f"The directive **{directive}** requires a direct position on “{focus}”, "
            "all clauses and scales, a process chain, spatial reconstruction, named "
            "India/world evidence, a counter-condition and a qualified conclusion."
        ),
        "plan": (
            f"For a {marks}-mark answer, spend about one-sixth of the time decoding "
            f"and drawing the map/flow; open with definition and thesis; organise "
            f"{evidence_count} process-spatial points as claim → named evidence → "
            "analysis → qualification; compress examples before mechanisms and "
            "reserve the final minute for the causal limit."
        ),
        "why": (
            "The answer obeys the directive, explains rather than catalogues, makes "
            "the spatial logic visible and avoids deterministic or timeless claims."
        ),
        "improve": (
            f"For “{focus}”, replace the weakest generalisation with one labelled "
            "process arrow or map anchor and state the scale, exception or evidence "
            "needed before extending the conclusion."
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
        else f"The answer must resolve the physical-geography demand in “{question}”."
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
            "Define the process and identify its controlling energy, force or gradient.",
            "Locate the pattern with one India anchor and one world or regional contrast.",
            "Trace the causal sequence from driver through mechanism to observable form.",
            "Test the nearest terminology, map-reading or scale distinction.",
            "Qualify the conclusion through an interacting control, exception or evidence limit.",
        ]
    body = "\n".join(
        f"{number}. **Claim and named evidence:** {item} "
        "**Analysis:** Trace the driver → mechanism → spatial expression → "
        "consequence chain and connect the named place, map or observation to the "
        "directive. **Qualification:** State the scale, threshold, interacting "
        "control, exception or source/date boundary."
        for number, item in enumerate(evidence, 1)
    )
    return (
        "**Detailed examiner-grade model answer:**\n\n"
        f"**Introduction and thesis:** {thesis}\n\n"
        f"**Analytical body:**\n\n{body}\n\n"
        "**Counter-position / limit:** A spatial association, one event, one model "
        "or one map layer does not establish a sufficient or timeless cause; test "
        "energy, material, structure, circulation, scale and human mediation.\n\n"
        f"**Qualified conclusion:** {conclusion}"
    )


def _review_block(topic: Topic) -> str:
    points = GEOGRAPHY_REVIEW_POINTS[topic.number]
    return (
        "### GEOGRAPHY DEEP-REVIEW CORE CONTROL\n\n"
        f"- **Must remember:** {points[0]}\n"
        f"- **Close distinction:** {points[1]}\n"
        f"- **Evidence / causal limit:** {points[2]}\n"
    )


_geography_inherited_insert_contract = insert_contract


def insert_contract(markdown: str, topic: Topic, record: dict[str, Any]) -> str:
    repaired = _geography_inherited_insert_contract(markdown, topic, record)
    session_re = re.compile(
        r"(?ms)^(### SESSION \d+\s*[—-]\s*(.+?)\s*)\n(.*?)(?=^### SESSION \d+\s*[—-]|\Z)"
    )

    def add_visual(match: re.Match[str]) -> str:
        heading, title, body = match.group(1), match.group(2), match.group(3)
        if "#### VISUAL FIRST" in body:
            return match.group(0)
        visual = (
            "\n#### VISUAL FIRST\n\n"
            "```text\n"
            f"{title.strip()}\n"
            "INITIAL CONDITION / DRIVER\n"
            "        ↓\n"
            "PHYSICAL MECHANISM OR CIRCULATION\n"
            "        ↓\n"
            "SPATIAL PATTERN / LANDFORM / CLIMATE EXPRESSION\n"
            "        ↓\n"
            "INDIA + WORLD MAP ANCHOR\n"
            "        ↓\n"
            "SCALE, INTERACTING CONTROL OR EVIDENCE LIMIT\n"
            "```\n\n"
            "*Use this gateway before the detailed process, map and qualified "
            "causal explanation below.*\n"
        )
        return heading + visual + "\n" + body.lstrip("\n")

    return session_re.sub(add_visual, repaired)


def build_ascii_spec(
    topic: Topic,
    record: dict[str, Any],
    generation: int,
    main: str,
    markdown_path: Path,
) -> dict[str, Any]:
    spec = _base_build_ascii_spec(
        topic,
        record,
        generation,
        main,
        markdown_path,
    )
    panels = [
        copy.deepcopy(panel) for panel in spec["topics"][0]["panels"]
    ]
    spec["topics"][0]["panels"] = panels
    for panel, lines in zip(
        (panels[0], panels[9], panels[10]),
        _wrapped_review_groups(topic),
    ):
        if "ascii_text" in panel:
            panel["ascii_text"] = (
                str(panel["ascii_text"]).rstrip() + "\n" + "\n".join(lines)
            )
        else:
            panel.setdefault("ascii_lines", []).extend(lines)
    seen_titles: set[str] = set()
    for panel in panels:
        title = str(panel.get("title") or "Untitled panel")
        candidate = title
        suffix = 1
        while candidate.casefold() in seen_titles:
            suffix += 1
            candidate = f"{title} — DEEP-REVIEW SYNTHESIS {suffix}"
        panel["title"] = candidate
        seen_titles.add(candidate.casefold())
    spec["constraints"]["geography_process_spatial_causal_control"] = True
    spec["constraints"]["map_and_current_status_discipline"] = True
    return spec


def _publish_before_tracker_sync_when_needed() -> dict[str, Any] | None:
    status = load(STATUS)
    master = load(MASTER)
    manifest_order = [row["topic_key"] for row in load(SECTION_MANIFEST)["topics"]]
    scope_keys = set(manifest_order)
    subject_status_keys = {
        row["topic_key"]
        for row in status["exports"]
        if row.get("variant") == "learner-v2"
        and row.get("topic_key") in scope_keys
    }
    master_keys = {row["topic_key"] for row in master["topics"]}
    selected_keys = master_keys | subject_status_keys
    review_keys = {row["topic_key"] for row in load(REVIEW_TRACKER)["topics"]}
    if selected_keys == master_keys and review_keys == master_keys:
        return None
    if selected_keys == master_keys:
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
                "Pre-review tracker-only synchronization failed: "
                + "\n".join((sync.stdout + sync.stderr).splitlines()[-20:])
            )
        return {
            "topic_count": len(master_keys),
            "manifest": None,
            "validation_manifest": None,
            "status": "tracker_sync_only",
        }
    selected_order = [row["topic_key"] for row in master["topics"]]
    selected_order.extend(
        key for key in manifest_order if key in subject_status_keys and key not in master_keys
    )
    if set(selected_order) != selected_keys:
        raise RuntimeError("Pre-publish key ordering lost a live MASTER or Part A key.")
    result = export_library(
        root=ROOT,
        export_root=ROOT / "notes" / "Final-Learning-Packages",
        tracker_path=STATUS,
        catalogue_path=(
            ROOT / "upsc-ai-kit" / "manifests" / "v2" / "topic-catalog.json"
        ),
        selected_keys=selected_order,
        manifest_date=DATE,
        dry_run=False,
        full_pdf_validation=True,
    )
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
    synced_master = load(MASTER)
    synced_review = load(REVIEW_TRACKER)
    if (
        {row["topic_key"] for row in synced_master["topics"]} != selected_keys
        or {row["topic_key"] for row in synced_review["topics"]} != selected_keys
    ):
        raise RuntimeError(
            "Pre-review publish/sync did not reconcile EXPORT, MASTER and REVIEW."
        )
    return result


if __name__ == "__main__":
    raise SystemExit(main())
