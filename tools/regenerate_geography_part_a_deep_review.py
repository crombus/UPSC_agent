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
_BASE_SHA256 = "06ad0dfdb82fb84b12dc0e1634fe4c2c2b6dac50c20a3d15f5e0f520de3a7d21"
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


def source_contract(topic: Topic, record: dict[str, Any]) -> str:
    provenance = record.get("provenance", {})
    live_sources = provenance.get("live_sources") or []
    current_note = provenance.get("current_linkage_note") or (
        "The static physical-geography core needs no volatile claim. Any hazard "
        "event, project, designation, regulatory status, climate anomaly or count "
        "must retain an official source, observation date and status boundary."
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
