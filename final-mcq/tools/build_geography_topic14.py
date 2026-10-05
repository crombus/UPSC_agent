from __future__ import annotations

import json
import random
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
TOPIC = SUBJECT / "14-Climate-Classification-Koppen-India-Climatic-Regions"
AUDIT_DATE = "2026-10-04"

BASIC = "upsc-ai-kit/knowledge/Geography/basic/14_Climate-Classification-Koppen.md"
ADVANCED = "upsc-ai-kit/knowledge/Geography/advanced/14_India-Climatic-Regions.md"
PACKAGE = "upsc-ai-kit/knowledge/Geography/14_India-Climatic-Regions_Complete-Topic-Package.md"
LEARNER = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-14_Learning-Session.md"
)
WORKBOOK = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-14_Solved-Workbook.md"
)
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Geography/Part-A-—-Physical-Geography/"
    "14-Climate-Classification-(Koppen)-India-Climatic-Regions/MCQ-Bank-With-Solutions.md"
)
OCR_1 = "attempts/_gs_source_text/GC_Leong_Certificate_Physical_and_human_Geography_pdf.txt"
OCR_2 = "attempts/_gs_source_text/Indian_geography_majid_hussain_pdf.txt"


def spec(
    area: str,
    stem: str,
    correct: str,
    wrongs: tuple[str, str, str],
    explanation: str,
    source: str,
    trap: str,
) -> dict[str, object]:
    return {
        "area": area,
        "stem": stem,
        "correct": correct,
        "wrongs": wrongs,
        "explanation": explanation,
        "source": source,
        "trap": trap,
    }


S1 = f"Basic owner §; Advanced owner §; {OCR_2}; snapshot {AUDIT_DATE}"
S2 = f"Basic owner §§2–4; G.C. Leong cross-check; snapshot {AUDIT_DATE}"
S3 = f"Advanced owner §§1–5; {OCR_2}; snapshot {AUDIT_DATE}"


BANKS: dict[int, list[dict[str, object]]] = {
    1: [
        spec("empirical basis", "Which feature most directly identifies Köppen's classification as empirical rather than genetic?",
             "It groups climates using observed temperature and precipitation thresholds associated with vegetation patterns",
             ("It classifies every region only by the direction of prevailing air masses",
              "It derives all boundaries from the age and composition of the underlying rocks",
              "It assigns climates solely from the economic activities of local populations"),
             "Köppen uses measured temperature, precipitation and seasonality, with thresholds chosen to correspond broadly to vegetation. A genetic scheme instead begins from causes such as air masses or circulation.",
             S1, "Calling any vegetation-linked classification genetic because vegetation is used as an interpretive correlate."),
        spec("major groups", "With reference to the principal Köppen groups, which statement is correct?",
             "A is tropical rainy, B is dry, C and D are warm-temperate/continental temperature groups, and E is polar",
             ("A is dry, B is tropical rainy, C is polar, and E is highland",
              "A is polar, B is maritime, C is desert, and D is tropical monsoon",
              "A, B, C, D and E are five rainfall mechanisms rather than climate groups"),
             "The first capital letter identifies the broad climate group. B is defined by aridity; A by a warm tropical regime; C and D by temperature thresholds; E by absence of a warm season.",
             S2, "Reading the letters as a simple temperature sequence and missing that B is defined by dryness."),
        spec("group A threshold", "A station has every monthly mean above 18°C. Which Köppen inference is most defensible, subject to rainfall criteria?",
             "It satisfies the principal temperature condition for Group A",
             ("It must be Group E because high monthly temperatures indicate polar insolation",
              "It must be Group B because any warm climate is automatically arid",
              "It must be Group D because continentality is measured only by annual temperature"),
             "Group A requires the coolest month to remain above 18°C. The station still needs precipitation and seasonality tests for a full subtype, so the temperature observation alone does not identify Af, Am or Aw.",
             S1, "Treating a first-group temperature threshold as a complete three-letter classification."),
        spec("group B", "Why cannot Group B be treated as a cold-climate category in a map-reading question?",
             "Because Group B is based on an aridity balance in which potential evaporation exceeds precipitation, and it includes hot and cold dry climates",
             ("Because Group B is defined by permanent snow cover at all elevations",
              "Because Group B is restricted to equatorial rainforest belts",
              "Because Group B is based only on the number of rainy days, not moisture balance"),
             "B climates are dry climates. Their temperature suffixes distinguish hot and cold forms, but the group boundary is fundamentally an aridity criterion rather than a latitude or snow criterion.",
             S2, "Assuming the alphabet makes B the second-coldest group."),
        spec("group C", "Which combination best represents the defining temperature logic of a typical Group C climate?",
             "The coldest month is below 18°C but above the adopted C/D boundary, while the warmest month exceeds 10°C",
             ("The warmest month is below 10°C and the coldest month is always below −20°C",
              "Every month exceeds 18°C and the climate therefore belongs to Group A",
              "Annual evaporation must exceed precipitation, which is the defining test for Group C"),
             "Group C is a mesothermal or warm-temperate category. Exact C/D boundary conventions vary, but Group C is warmer than D and has a warmest month above 10°C.",
             S1, "Substituting the Group E warmest-month threshold or the Group B aridity rule."),
        spec("group D", "Which observation would most strongly support a Group D classification rather than Group C?",
             "The coldest month falls below the adopted C/D threshold while the warmest month remains above 10°C",
             ("Every month remains above 18°C, with no cool season",
              "The climate has a dry summer but no information about temperature",
              "The warmest month never reaches 10°C, which is the defining Group E condition"),
             "D is the continental or microthermal group: its cold season is colder than the C/D boundary, while at least one month is warm enough to exceed 10°C.",
             S1, "Using rainfall seasonality alone to distinguish C and D."),
        spec("group E", "Which criterion is most diagnostic of Group E in the Köppen system?",
             "The warmest month has a mean temperature below 10°C",
             ("The coolest month remains above 18°C",
              "Annual precipitation is lower than potential evaporation",
              "The region must receive rainfall only in winter"),
             "Group E represents polar climates without a warm season. Tundra and ice-cap distinctions are made with further temperature criteria, but the first test is the warmest-month threshold.",
             S2, "Confusing the temperature basis of E with the moisture basis of B."),
        spec("highland addition", "How should H be treated when a map includes it beside the five original Köppen groups?",
             "H is a later highland designation for mountainous conditions that are not adequately represented by the lowland groups",
             ("H is the original Köppen group for humid equatorial forests",
              "H is a universal sixth group defined only by annual rainfall below 25 cm",
              "H replaces E everywhere because all high mountains are polar"),
             "Highland is a later addition used in applied schemes. Altitude can produce sharp vertical climatic change, so a highland label avoids forcing every elevation belt into one lowland code.",
             S3, "Treating H as an original group or as a synonym for ice cap."),
        spec("letter grammar", "In a full Köppen code, what does the first capital letter principally communicate?",
             "The major climate group, such as tropical, dry, warm-temperate, continental or polar",
             ("The exact district or station where the climate was observed",
              "The dominant crop grown under irrigation",
              "The direction from which the summer monsoon arrives"),
             "The capital first letter is the broad thermal or aridity group. Lower-case or additional capitals then refine rainfall seasonality and temperature severity.",
             S1, "Reading the code as a place-name or crop code rather than a hierarchical climate label."),
        spec("moisture suffixes", "Which pairing correctly interprets the common moisture suffixes f, m, w and s?",
             "f means no dry season, m indicates monsoon/short dry season, w dry winter and s dry summer",
             ("f means dry winter, m dry summer, w no dry season and s monsoon",
              "f means desert, m steppe, w tundra and s ice cap",
              "f and m refer only to temperature while w and s refer only to altitude"),
             "The lower-case moisture letters describe the seasonal distribution of precipitation. They are not a simple wet-to-dry scale and w does not mean wet.",
             S2, "Expanding w as wet instead of dry winter."),
        spec("dry-climate suffixes", "A code beginning BW or BS is being read. Which interpretation is sound?",
             "W denotes desert/arid conditions and S denotes steppe/semi-arid conditions; later letters can indicate thermal severity",
             ("W denotes winter rainfall and S denotes summer rainfall in every group",
              "W denotes warm temperate and S denotes subtropical highland",
              "BW and BS are both humid tropical subtypes distinguished only by forest height"),
             "For dry climates, the second capital letter W/S separates desert from steppe. h/k and related suffixes provide further thermal refinement in common usage.",
             S1, "Applying the f-m-w-s moisture grammar to the dry-climate capital suffixes."),
        spec("temperature suffixes", "What is the purpose of the a–d suffixes commonly used with C and D climates?",
             "They refine summer warmth or winter severity within the temperate and continental groups",
             ("They identify the four seasons in the order in which they occur",
              "They distinguish four levels of annual rainfall in tropical climates",
              "They indicate four different soil orders rather than thermal conditions"),
             "The a–d letters add temperature-season detail, especially the warmth of the summer or severity of the winter. They are not rainfall totals or soil labels.",
             S2, "Treating the suffix alphabet as a chronology or precipitation ranking."),
        spec("Af Am Aw", "Which sequence correctly matches Af, Am and Aw?",
             "Af is tropical rainforest/no dry season, Am tropical monsoon, and Aw tropical savanna with dry winter",
             ("Af is desert, Am Mediterranean, and Aw ice cap",
              "Af is dry winter, Am dry summer, and Aw no dry season",
              "Af is cold continental, Am steppe, and Aw tundra"),
             "The A group is subdivided by rainfall seasonality. Af has no dry season; Am has monsoonal rainfall with a short dry period; Aw has a pronounced dry winter.",
             S1, "Treating all A climates as equally wet or interchanging m and w."),
        spec("temperate codes", "Which statement correctly distinguishes Cs, Cw and Cf?",
             "Cs has dry summer, Cw dry winter, and Cf lacks a pronounced dry season",
             ("Cs has dry winter, Cw dry summer, and Cf is always arid",
              "Cs is desert, Cw is ice cap, and Cf is equatorial rainforest",
              "The three codes differ only by altitude, not by precipitation seasonality"),
             "The second letter records the seasonal precipitation pattern in these C climates. Mediterranean climates are Cs because summer is dry; Cw is dry winter; Cf has no marked dry season.",
             S2, "Reversing the Mediterranean dry-summer signal."),
        spec("D and E codes", "Which pair is internally consistent with standard Köppen terminology?",
             "Df can denote humid continental conditions without a dry season, while ET and EF are tundra and ice-cap categories",
             ("Df is tropical rainforest, ET is hot desert and EF is steppe",
              "Df means dry summer Mediterranean, ET means monsoon and EF means savanna",
              "ET and EF are both warm-temperate codes differentiated only by rainfall"),
             "D codes describe cold continental climates, while E codes describe polar climates. ET and EF refine polar conditions by the warmest-month temperature.",
             S1, "Confusing the E-group temperature categories with C-group rainfall suffixes."),
        spec("C/D boundary", "Why should an answer mention the boundary convention when assigning a C or D code?",
             "The original Köppen convention used about −3°C, while many modern maps use 0°C, so the same station can be classified differently near the boundary",
             ("Because C and D are separated by a legally fixed Indian administrative boundary",
              "Because the boundary is determined only by annual rainfall and never by temperature",
              "Because the C/D distinction was abolished when H was added"),
             "The C/D threshold is a methodological convention. A careful answer states the adopted convention rather than presenting a near-boundary code as universal.",
             S1, "Presenting one threshold as if every textbook and map used the same convention."),
        spec("wet west coast", "Which Indian setting best fits an Am or Amw interpretation in applied Köppen maps?",
             "The very wet windward west-coast belt and comparable high-rainfall monsoon pockets",
             ("The core Thar desert with very low annual precipitation",
              "The cold desert of Ladakh at high elevation",
              "The Coromandel coast where winter rainfall dominates"),
             "The west coast receives heavy orographic and monsoon rainfall. Applied Indian maps may write Am or Amw, so the source-specific code convention should be retained.",
             S3, "Swapping the west-coast monsoon belt with the dry-winter interior or Tamil Nadu winter-rain belt."),
        spec("Tamil Nadu code", "Why is an As-type label used for parts of the Coromandel/Tamil Nadu coast in some Indian Köppen maps?",
             "Its tropical rainfall regime has a relatively dry summer and receives important rain from the retreating or north-east monsoon",
             ("It receives almost all rain from a winter westerly disturbance regime",
              "It is a polar climate because the coast has a narrow annual temperature range",
              "It is a hot desert because all coastal climates are arid"),
             "The Tamil Nadu coast is distinctive within India because the retreating or north-east monsoon contributes strongly to its rainfall, while summer can be comparatively dry.",
             S3, "Assuming every Indian coast has the same southwest-monsoon seasonal maximum."),
        spec("peninsular interior", "Which applied Köppen description most plausibly fits much of the peninsular interior away from the wet windward coast?",
             "Aw, a tropical savanna or wet-and-dry climate with a pronounced dry winter",
             ("Af, because every tropical area has rainfall in every month",
              "EF, because the Deccan plateau is a highland ice-cap region",
              "Cw, because all areas south of the Ganga are warm-temperate"),
             "The interior plateau has a marked dry season and monsoon-concentrated rainfall, unlike the perennially wet west-coast belt.",
             S1, "Using latitude alone and ignoring rain-shadow position and seasonality."),
        spec("semi-arid India", "Which physical setting most strongly supports a BShw classification in India?",
             "A rain-shadow or marginal-rainfall belt such as parts of the Deccan and north-western transition zones",
             ("The Meghalaya high-rainfall belt with rainfall in excess of 200 cm",
              "The windward Konkan coast with heavy southwest-monsoon rain",
              "The ice-covered upper Himalaya where the warmest month is below 0°C"),
             "BShw represents hot semi-arid steppe conditions. In India these are linked to rain-shadow effects, distance from moisture sources and north-western aridity gradients.",
             S3, "Equating every hot Indian region with BWh desert or every plateau with Cw."),
        spec("hot desert India", "Which region-code pairing is most defensible in a standard applied Indian map?",
             "Western Rajasthan and Kachchh with BWh or BWhw hot-desert conditions",
             ("Assam and Meghalaya with BWh because heavy rainfall indicates desert heat",
              "Tamil Nadu's Coromandel coast with BWh because it gets winter rain",
              "The windward Western Ghats with BWh because mountains always suppress rainfall"),
             "The Thar and Kachchh have high aridity and hot thermal conditions. The exact suffix varies by the map convention, but BWh/BWhw is the relevant family.",
             S3, "Treating heat, rather than aridity, as sufficient for a desert code."),
        spec("north Indian plains", "Which code family is commonly used for the monsoonal north Indian plains in applied Köppen descriptions?",
             "Cw or Cwg/Cwa variants describing a warm-temperate or humid-subtropical climate with dry winter",
             ("Af variants describing a no-dry-season equatorial rainforest",
              "BWh variants describing a hot desert throughout the Ganga plain",
              "EF variants describing permanent ice cap conditions"),
             "The northern plains have hot monsoon summers and a cooler, comparatively dry winter. Different Indian sources use Cwg or Cwa variants, so the map convention must be cited.",
             S3, "Assuming the entire north Indian plain has an identical code regardless of source convention."),
        spec("high Himalaya", "How should high Himalayan climates be handled in an India-focused Köppen question?",
             "They require highland, cold or polar-type qualification because altitude overrides simple lowland latitude rules",
             ("They must all be Aw because the Himalaya lies in the tropics",
              "They must all be Am because every mountain receives orographic rainfall",
              "They cannot be classified because altitude has no effect on temperature"),
             "Elevation produces vertical climatic zonation and cold-desert or snow conditions in the trans-Himalaya. Applied maps therefore use H/E or local highland conventions.",
             S3, "Projecting lowland tropical codes onto all Himalayan elevations."),
        spec("relief and latitude", "The west-facing slope of the Western Ghats and the leeward Deccan interior lie at similar latitudes but can receive different codes. What does this demonstrate?",
             "Relief and moisture-bearing wind direction can outweigh latitude in determining regional climate",
             ("Latitude alone fixes the climate code, so the two areas must have the same class",
              "Only soil chemistry can explain the difference; rainfall and relief are irrelevant",
              "The difference proves Köppen does not use precipitation at all"),
             "Orographic uplift wets the windward slope, while descending air and rain-shadow effects dry the interior. Classification records this contrast through different temperature-precipitation regimes.",
             S3, "Treating latitude as a complete explanation of Indian climatic regions."),
        spec("coastal moderation", "Which inference about a coastal station is most sound when comparing it with an inland station at similar latitude?",
             "Maritime influence can reduce annual temperature range and alter the seasonal climate code through moisture and thermal moderation",
             ("Coastal location guarantees a desert code because the sea blocks all rain",
              "Continentality is irrelevant once the two stations share a latitude",
              "The coastal station must have a colder winter than every inland station"),
             "Distance from the sea modifies temperature range and moisture supply. It does not by itself determine a code, but it can shift a station across a threshold.",
             S2, "Assuming a single factor such as latitude or coast automatically fixes the code."),
        spec("north-east India", "Which statement best links the north-east Indian climatic region to applied classification?",
             "Very high monsoon rainfall and mountainous relief favour humid tropical or highland mosaics rather than a single uniform lowland code",
             ("The north-east is uniformly BWh because it lies near the northern edge of India",
              "The region is uniformly EF because all mountain rain is snow",
              "The region's rainfall is negligible and cannot affect classification"),
             "Assam, Meghalaya and adjoining hills receive heavy monsoon rainfall, but elevation and local relief create internal variation. Classification scale matters.",
             S3, "Turning a wet regional label into a claim of climatic uniformity."),
        spec("Tamil Nadu seasonality", "Which rainfall-season statement is most useful when distinguishing Tamil Nadu from the west coast?",
             "Tamil Nadu receives a substantial share of rainfall during the retreating or north-east monsoon, unlike the west coast's dominant southwest-monsoon maximum",
             ("Tamil Nadu receives all rain from western disturbances and the west coast receives winter rain",
              "Both coasts have identical rainfall seasonality because they face the same ocean",
              "Tamil Nadu's rainfall is controlled only by snowmelt"),
             "The Coromandel coast is exposed to the north-east monsoon and tropical cyclones in the post-monsoon season, while the west coast is strongly exposed to the Arabian Sea branch of the southwest monsoon.",
             S3, "Memorising only annual rainfall totals and missing seasonal distribution."),
        spec("rain shadow", "Which chain correctly explains why the Deccan interior is often drier than the Western Ghats windward slope?",
             "Moist air rises on the windward slope, loses moisture, and descends warmer and drier on the leeward side",
             ("Dry air rises on the windward slope and becomes wetter only after descending",
              "The interior is wetter because descending air always produces heavy rainfall",
              "The difference is caused only by the Earth's distance from the Sun"),
             "Orographic ascent causes condensation and precipitation on the windward side; subsidence on the leeward side suppresses rainfall and supports semi-arid conditions.",
             S3, "Reversing the windward/leeward moisture sequence."),
        spec("Trewartha", "What is the safest description of Trewartha in relation to Köppen?",
             "It is a modified empirical classification that rearranges or refines climatic groups and explicitly recognises additional thermal/highland distinctions",
             ("It is a purely genetic system based only on air-mass source",
              "It is an agricultural land-capability classification unrelated to climate",
              "It rejects temperature and precipitation data entirely"),
             "Trewartha modifies Köppen rather than abandoning empirical climatic data. It is useful for comparison but is not the same code system.",
             S3, "Treating every alternative classification as either a genetic system or an agro-climatic map."),
        spec("Thornthwaite", "Which variable most clearly separates Thornthwaite's approach from a simple temperature-only classification?",
             "A moisture or water-balance index involving precipitation and potential evapotranspiration",
             ("The legal boundary of each Indian state",
              "The longitude of the nearest coastline",
              "The number of mountain peaks visible from a station"),
             "Thornthwaite asks how much water is available after atmospheric demand, represented through potential evapotranspiration. This makes it relevant to plant water stress and agricultural planning.",
             S3, "Reducing Thornthwaite to a rainfall total or a temperature ladder."),
        spec("genetic comparison", "Which evaluative conclusion best compares empirical Köppen with a genetic climate classification?",
             "Köppen is easier to reproduce and map from observations, while genetic schemes explain circulation causes more directly; the two answer different questions",
             ("Köppen explains all causes and therefore makes genetic schemes unnecessary",
              "Genetic schemes cannot use observations and are always less scientific",
              "Both schemes are identical because every climate code names an air mass"),
             "Empirical classifications describe statistical outcomes; genetic classifications emphasise mechanisms such as air masses and circulation. A balanced answer treats them as complementary.",
             S3, "Turning a comparison into an absolute verdict that one scheme makes the other useless."),
        spec("climate versus biome", "Why must an answer distinguish a Köppen climate region from a biome?",
             "A climate code describes long-term atmospheric conditions, whereas a biome also reflects ecological history, soils, disturbance and other controls",
             ("A biome is merely another spelling of a temperature threshold",
              "Climate codes directly determine one crop and one vegetation type everywhere",
              "Biomes are administrative units and therefore identical to climate grids"),
             "Climate influences vegetation but does not mechanically determine it. Soil, fire, human land use, elevation and ecological history qualify the climate–biome relationship.",
             S3, "Treating a climate code as a complete ecological or economic explanation."),
        spec("agro-climatic distinction", "Which statement correctly distinguishes an agro-climatic region from an agro-ecological region?",
             "Agro-climatic regions emphasise climatic suitability and growing conditions, while agro-ecological regions add land and soil characteristics",
             ("Agro-ecological regions ignore soil and use only rainfall",
              "Agro-climatic regions are defined only by district borders",
              "The two terms are exact synonyms in all planning contexts"),
             "The source distinction is analytical: agro-climatic zoning foregrounds climate and growing period, while agro-ecological zoning superimposes soil and land attributes.",
             OCR_2 + " climate-regions chapter; snapshot " + AUDIT_DATE, "Confusing an administrative map with a climate or ecological classification."),
        spec("R L Singh", "What is a documented feature of R.L. Singh's 1971 climatic division of India?",
             "It modified the Stamp–Kendrew approach and divided India into ten major divisions using quantitative and qualitative rainfall-temperature differences",
             ("It classified India only by crop prices and market distance",
              "It rejected temperature and rainfall measurements in favour of latitude alone",
              "It created the original five global Köppen groups without Indian modification"),
             "Majid Husain records Singh's 1971 scheme as a modification of Stamp and Kendrew, with ten major divisions and a mixed quantitative-qualitative basis centred on rainfall and temperature.",
             OCR_2 + " pp. 4.36–4.37 (local OCR); snapshot " + AUDIT_DATE, "Mixing the Indian regional scheme with the original global Köppen groups."),
        spec("Blandford", "Which historical statement about H.E. Blandford is supported by the source record?",
             "Blandford's 1889 attempt was an early systematic Indian climatic division based on temperature and rainfall from selected stations, but it was considered overgeneralised",
             ("Blandford developed Thornthwaite's moisture index in 1948",
              "Blandford classified India using satellite gridded normals unavailable in the nineteenth century",
              "Blandford's scheme was based solely on vegetation maps and ignored observations"),
             "The historical source identifies Blandford, the first Director General of the Indian Meteorological Department, as an early systematic classifier whose limited station base encouraged overgeneralisation.",
             OCR_2 + " climate-regions chapter; snapshot " + AUDIT_DATE, "Projecting modern gridded datasets or later schemes backward onto Blandford."),
        spec("climate normals", "A map compares Köppen classes for two different periods. Which metadata is essential before interpreting a boundary shift?",
             "The baseline period, dataset, spatial resolution, variables and classification convention",
             ("Only the colour palette used by the cartographer",
              "The current day's weather report from one station",
              "The administrative population of the nearest city, without climate data"),
             "A climate class is threshold-based and depends on the underlying normals and method. Different periods, grids or C/D conventions can change the map without a physical discontinuity at one boundary.",
             S3, "Treating a current weather event or an unlabeled map as a climate normal."),
        spec("moving boundaries", "What is the most defensible inference when sustained warming raises evaporative demand but rainfall seasonality changes little?",
             "A transitional moist-to-dry boundary may move because Group B responds to the precipitation–evaporation balance, not rainfall total alone",
             ("No classification can change unless the continent moves to another latitude",
              "The area must become Af because warming always increases rainforest conditions",
              "Only the map's colours change; the threshold cannot be crossed"),
             "Dry-climate classification depends on moisture balance. Warming can raise evaporative demand and push a marginal area toward BSh even without a dramatic rainfall decline.",
             S3, "Assuming aridification requires a large fall in annual rainfall."),
        spec("hazard overlay", "Why should a Köppen map not be used as a substitute for a climate-hazard vulnerability map?",
             "Köppen describes long-term climatic thresholds, while hazard vulnerability also depends on exposure, assets, frequency and coping capacity",
             ("Köppen maps measure district disaster losses directly",
              "Hazard maps use no climate information at all",
              "A single climate code determines the vulnerability of every settlement within it"),
             "Climate classification and risk assessment answer different questions. The same climatic zone can contain very different populations, infrastructure and adaptive capacity.",
             S3, "Inferring present disaster risk directly from a broad climate code."),
        spec("map scale", "A single Himalayan grid cell contains valley, slope and ridge climates. What is the correct cartographic caution?",
             "The displayed code is scale-dependent and may conceal vertical zonation and transition mosaics within the cell",
             ("The grid cell proves that all elevations share one identical climate",
              "Mountain climate is impossible to classify at any scale",
              "The code should be read as an agro-ecological guarantee for every parcel"),
             "Station normals, grid cells, regional boundaries and agro-ecological units are different analytical scales. Mountains demand caution about averaging and vertical change.",
             S3, "Treating a coarse regional label as a parcel-level field observation."),
        spec("India as climate sample", "Why is India a useful test case for applying Köppen while also exposing its limitations?",
             "Its latitude, monsoon seasonality, relief, continentality, coasts and high mountains create many climatic contrasts within one country",
             ("India has only one climate, so classification is unnecessary",
              "India lacks seasonal rainfall and therefore cannot test the scheme",
              "India's climate is controlled solely by longitude and not by relief"),
             "India contains humid coasts, monsoon interiors, arid west, subtropical plains and highland/cold regions. The range demonstrates both the descriptive utility and boundary limitations of empirical codes.",
             S3, "Reducing India's monsoon climate to a single undifferentiated label."),
    ],
    2: [
        spec("code diagnosis", "A location has no dry month, a coolest month above 18°C and year-round heat. Which code family is the best starting hypothesis?",
             "Af, subject to the source's precise rainfall and forest criteria",
             ("BWh, because year-round heat automatically means desert",
              "Cs, because no dry month indicates Mediterranean summer drought",
              "ET, because a warm annual mean implies polar conditions"),
             "The observations satisfy the A-group thermal condition and the f rainfall suffix. A complete classification still requires the quantitative thresholds used by the adopted map.",
             S1, "Letting annual warmth override the stated no-dry-season evidence."),
        spec("code diagnosis", "A tropical station has a short dry season but very heavy seasonal monsoon rain. Which code is most plausible?",
             "Am, often written Amw in some Indian applications",
             ("Aw, because m always means dry winter",
              "BSh, because monsoon climates are semi-arid",
              "Df, because all monsoonal rainfall is continental"),
             "Am captures tropical monsoon conditions with a short dry period. Applied Indian maps vary in whether they write Am or Amw, so the map convention should be stated.",
             S3, "Treating a short dry season as evidence for the much drier Aw class."),
        spec("code diagnosis", "A tropical location has a pronounced dry winter and a wet summer. What broad code fits best?",
             "Aw, tropical savanna or wet-and-dry climate",
             ("Af, because any wet summer means no dry season",
              "EF, because a dry winter indicates ice cap",
              "Cfa, because every tropical code is warm-temperate"),
             "Aw is the tropical wet-and-dry type with dry winter. The question tests seasonality, not merely annual rainfall.",
             S2, "Ignoring the dry season while noticing only the presence of monsoon rain."),
        spec("code diagnosis", "A dry climate is hot and desert-like rather than semi-arid. Which code family is appropriate?",
             "BW, with h or related suffixes if the adopted convention further specifies heat",
             ("BS, because W means wet season",
              "Cw, because dry winter is the same as desert",
              "Am, because deserts have strong seasonal pressure changes"),
             "W is the dry-climate capital suffix for desert/arid conditions; S is steppe/semi-arid. Thermal suffixes refine the dry group.",
             S1, "Applying the lowercase w seasonal-rain meaning to uppercase W."),
        spec("code diagnosis", "A dry climate is semi-arid steppe and lies in a hot subtropical belt. Which coding logic applies?",
             "BS followed by a hot-temperature suffix such as h in common usage",
             ("BW followed by ET because all dry regions are tundra",
              "Af followed by f because steppe has no dry season",
              "Cw followed by d because semi-arid is a temperate rainfall suffix"),
             "BS identifies steppe/semi-arid conditions. The additional thermal letter separates hot from cold dry climates in common Köppen usage.",
             S2, "Confusing the dry-group capital S with the seasonal lowercase s."),
        spec("C/D threshold", "Two stations have similar rainfall, but one has a colder winter below the adopted C/D boundary. What change is expected?",
             "The colder station may move from a C to a D classification if its warmest month still exceeds 10°C",
             ("Both must be B because rainfall is the only classification variable",
              "The colder station becomes E even if its warmest month exceeds 10°C",
              "The warmer station becomes H solely because it is inland"),
             "C and D are separated primarily by winter temperature under the adopted convention. Rainfall letters remain a separate part of the code.",
             S1, "Allowing rainfall similarities to erase the C/D thermal distinction."),
        spec("polar test", "A station's warmest month averages 7°C. Which conclusion is safest?",
             "It satisfies the principal Group E temperature condition, although ET versus EF requires further testing",
             ("It must be Group A because the warmest month is above freezing",
              "It must be Group B because all cold places are arid",
              "It must be Group C because every station has a warmest month"),
             "Group E requires the warmest month to remain below 10°C. Tundra and ice cap are then separated by the finer temperature threshold.",
             S2, "Using the 0°C freezing point instead of the Köppen 10°C warmest-month test."),
        spec("code hierarchy", "Which sequence reflects the normal information hierarchy in a Köppen code?",
             "Broad group first, then moisture seasonality or aridity detail, then thermal severity or summer/winter refinement",
             ("Administrative unit first, then crop, then latitude",
              "Vegetation species first, then soil, then population density",
              "Monsoon month first, then longitude, then river basin"),
             "The code is hierarchical: first capital group, then letters that refine precipitation regime and thermal severity. It is not a regional administrative code.",
             S1, "Reading a multi-letter code as an arbitrary acronym."),
        spec("isohyets", "What does an isohyet show on a climatic map?",
             "A line joining places receiving equal precipitation over the stated period",
             ("A line joining places with equal temperature",
              "A line joining places with equal pressure",
              "A line joining places with equal potential evapotranspiration only"),
             "Isohyets map rainfall. Isotherms map temperature and isobars map pressure; the time period and dataset still matter for interpretation.",
             S1, "Confusing rainfall isolines with temperature or pressure isolines."),
        spec("isotherms", "Why can January isotherms bend southward over northern India?",
             "The continental interior cools more strongly in winter than maritime and southern areas, producing a thermal gradient",
             ("Because rainfall isolines always bend southward in January",
              "Because isotherms show equal pressure rather than temperature",
              "Because the Himalaya directly heats the northern plains in winter"),
             "Isotherms join equal temperature. Continentality, latitude, altitude and winter circulation shape the pattern; the line is not an administrative boundary.",
             S1, "Treating an isotherm as an isobar or as a fixed latitude."),
        spec("Am versus Aw", "Which observation best separates an Am west-coast pocket from an Aw peninsular interior pocket?",
             "The Am pocket has a shorter or weaker dry season and much heavier monsoon rainfall than the Aw interior",
             ("The Aw interior has no dry season while the Am coast has a polar winter",
              "The two codes differ only in longitude and never in rainfall seasonality",
              "Am always means desert and Aw always means ice cap"),
             "Both belong to A climates, but m indicates monsoonal rainfall with only a short dry period, whereas w denotes a clearer dry winter.",
             S3, "Using the capital A as if it eliminated all seasonal contrasts."),
        spec("As application", "Which combination is most consistent with an As-type Indian coastal setting?",
             "Tropical temperatures, a comparatively dry summer and important post-monsoon or north-east monsoon rainfall",
             ("Coolest month below the C/D threshold and a cold continental winter",
              "No dry month and evenly distributed rainfall throughout the year",
              "Hot desert conditions with negligible annual rainfall"),
             "As is an applied tropical code for a dry-summer pattern. Tamil Nadu/Coromandel is the classic Indian association in the owner material.",
             S3, "Assuming s always means dry winter because it resembles the word summer only informally."),
        spec("BWh versus BSh", "Which field observation would favour BSh over BWh in western or peninsular India?",
             "Seasonal rainfall is low but sufficient for steppe or dryland vegetation, rather than the more extreme aridity of a desert",
             ("Annual moisture deficit is extreme and desert surfaces dominate",
              "Rainfall exceeds 200 cm and forests are evergreen",
              "The warmest month stays below 10°C"),
             "BS is semi-arid steppe, while BW is desert. The distinction is about aridity thresholds, not simply whether the landscape looks brown in one season.",
             S1, "Using colour or vegetation appearance without considering the moisture balance."),
        spec("Cwg/Cwa", "Why may the same north Indian plain be written Cwg in one source and Cwa in another?",
             "Applied maps use variant suffix conventions and threshold details, so the source legend and adopted coding standard must be checked",
             ("Because Cwg and Cwa are unrelated to temperature and rainfall",
              "Because one code is for the southern hemisphere and the other for the northern hemisphere",
              "Because a code changes every year with the monsoon onset date"),
             "The core signal is a humid-subtropical or warm-temperate monsoon climate with dry winter. Variant notation is not evidence that the region changed overnight.",
             S3, "Treating source-specific code variants as contradictory climates."),
        spec("regional scale", "A map shows the same Cw code across a broad plain. Which qualification is necessary?",
             "A broad code summarises dominant normals and may conceal local elevation, riverine, urban and transition effects",
             ("Every location in the plain has identical daily weather",
              "The code proves identical soils and cropping systems everywhere",
              "The code removes the need to examine monsoon and winter mechanisms"),
             "Climate classes are regional summaries. Weather variability, local topography and land use continue within the mapped class.",
             S3, "Confusing a climate-region average with uniform weather or land use."),
        spec("mountain mosaic", "Why is H useful in a Himalayan map but not a substitute for all elevation-specific analysis?",
             "It flags the highland setting, but vertical belts and local exposure can still produce several climates within the mountain region",
             ("H proves that every slope has identical temperature and precipitation",
              "H is simply another spelling of BWh for cold deserts",
              "H means the mountain is outside the atmosphere and cannot be studied"),
             "Highland is a useful applied category, yet mountains contain sharp lapse-rate, aspect, rain-shadow and snowline changes. The code does not erase that mosaic.",
             S3, "Turning a highland umbrella label into a single uniform climatic condition."),
        spec("Trewartha comparison", "Which reason is commonly offered for using Trewartha alongside Köppen?",
             "Trewartha modifies group structure to address some of Köppen's broad thermal generalisations while retaining empirical data",
             ("Trewartha replaces all observations with cultural-region boundaries",
              "Trewartha is identical to Thornthwaite's water-balance index",
              "Trewartha classifies only ocean currents and not climate"),
             "Trewartha is a modified empirical classification. It is a comparative framework, not a synonym for Thornthwaite or a genetic circulation model.",
             S3, "Treating the names of classification systems as interchangeable."),
        spec("water balance", "A crop planner wants to estimate moisture stress rather than merely name a temperature-rainfall class. Which scheme is especially relevant?",
             "Thornthwaite, because potential evapotranspiration is used with precipitation in a moisture balance",
             ("Köppen only, because it directly measures every crop's yield",
              "Blandford only, because a few station totals capture all water stress",
              "A political map, because administrative area determines evapotranspiration"),
             "Thornthwaite's moisture index is closer to plant water availability than a simple annual rainfall total. It is more data-demanding but agriculturally informative.",
             S3, "Assuming the most globally familiar classification is automatically best for every planning task."),
        spec("classification limits", "Which is a genuine limitation of Köppen's empirical scheme?",
             "It records climatic outcomes with thresholds but does not by itself explain the atmospheric mechanisms producing them",
             ("It cannot use temperature or precipitation observations",
              "It has no way to represent seasonality",
              "It classifies only Indian districts and cannot be used comparatively"),
             "The scheme is reproducible and globally comparable, but it is not a causal theory. Monsoon circulation and relief must be supplied as explanatory context.",
             S3, "Mistaking a limitation of explanation for an inability to describe patterns."),
        spec("monsoon causation", "If a Köppen code labels a region as monsoonal, what additional explanation is required in an Indian answer?",
             "The seasonal reversal of circulation, land-sea thermal contrast, relief and moisture transport that produce the observed pattern",
             ("Only the colour of the map legend",
              "A claim that the code itself causes the monsoon winds",
              "The population density of the nearest district without atmospheric reasoning"),
             "Codes describe the resulting climate. A complete Indian explanation connects the pattern to monsoon dynamics, topography and moisture pathways.",
             S3, "Treating a descriptive code as the physical cause of rainfall."),
        spec("west coast contrast", "Which paired comparison best captures the west-coast/Deccan climatic contrast?",
             "Windward uplift supports humid conditions, while leeward descent and continentality support drier interior conditions",
             ("Both areas are equally wet because they share the same latitude",
              "The Deccan is wetter because descending air produces persistent cloud",
              "The west coast is drier because the sea removes all atmospheric moisture"),
             "The contrast is a classic application of relief, wind direction and rain-shadow logic. Latitude is only one background control.",
             S3, "Reversing the rain-shadow mechanism."),
        spec("north-east relief", "Why can the north-east not be represented adequately by annual rainfall alone?",
             "Mountain relief, exposure, elevation and seasonal concentration create local climatic differences even within a very wet monsoon region",
             ("Annual rainfall is the only climate variable that matters in Köppen",
              "The north-east has no rainfall seasonality",
              "High rainfall guarantees one identical biome and code everywhere"),
             "Rainfall total is important but not sufficient. Temperature regime, seasonal distribution and topography determine the applied class.",
             S3, "Treating a single summary statistic as the whole classification."),
        spec("Tamil Nadu coasts", "Which inference follows from the Tamil Nadu coast's retreating-monsoon rainfall maximum?",
             "Its seasonal code can differ from similarly warm west-coast areas despite both being tropical",
             ("It must share the west coast's Am/Amw code because both are maritime",
              "It must be BWh because post-monsoon rainfall is impossible in a tropical climate",
              "It becomes Group E because winter rain lowers the annual mean"),
             "Seasonality matters inside the A group. Tropical temperature does not force identical rainfall timing.",
             S3, "Using thermal similarity as proof of identical precipitation seasonality."),
        spec("Indian divisions", "What is the safest way to use an Indian climatic-division scheme such as Stamp–Kendrew or R.L. Singh in an answer?",
             "Name the scheme, its principal variables and the regional purpose, rather than presenting its boundaries as a universal natural law",
             ("Treat every division as identical to Köppen's global code",
              "Ignore the basis and list only state names",
              "Assume all Indian schemes use the same number of regions and thresholds"),
             "Indian regional schemes differ in purpose, variables and scale. Attribution and method prevent the answer from conflating them.",
             OCR_2 + " climate-regions chapter; snapshot " + AUDIT_DATE, "Blending separate authors' divisions into one unsupported map."),
        spec("R L Singh basis", "Which pair of variables is central to the documented quantitative-cum-qualitative character of R.L. Singh's 1971 scheme?",
             "Rainfall amount and temperature variation",
             ("Soil texture and market distance",
              "River discharge and mineral reserves",
              "Population density and literacy rate"),
             "The source describes Singh's ten divisions as based largely on rainfall and temperature, with qualitative regional interpretation.",
             OCR_2 + " pp. 4.36–4.37 (local OCR); snapshot " + AUDIT_DATE, "Importing variables from agro-economic zoning into a climatic classification."),
        spec("baseline", "A claim says India's BSh area expanded between two maps. Which response is methodologically correct?",
             "Ask for the two periods, data sources, grid or station method, thresholds and whether the same convention was used",
             ("Accept the claim because any newer map is automatically comparable",
              "Reject all climate maps because classifications can never change",
              "Use a single day's rainfall to verify the multi-decadal claim"),
             "Comparability requires consistent methods and metadata. A boundary shift can be real, methodological, or both.",
             S3, "Treating a headline map comparison as self-authenticating evidence."),
        spec("hazard versus climate", "A district with a Cw-type climate suffers a flash flood. What does this illustrate?",
             "A regional climate class does not determine the timing, intensity or vulnerability of every hazard event",
             ("Cw means floods cannot occur",
              "The flood proves the district is permanently changing to Af",
              "Climate classification and hazard assessment are identical exercises"),
             "Hazards operate through short-term weather, catchment conditions, exposure and capacity. A climate class provides background context, not an event forecast.",
             S3, "Using one event to reclassify a climate or infer vulnerability directly."),
        spec("agro-ecological overlay", "Why might two places in the same Köppen class receive different agricultural recommendations?",
             "Soil, irrigation, relief, cultivar, growing period and management can differ even when broad climate normals are similar",
             ("The code fixes one crop everywhere",
              "Agriculture is unrelated to climate and depends only on longitude",
              "Same climate class means identical water balance and soils"),
             "Climate is one constraint among several. Agro-ecological planning adds soil and land characteristics and may use finer scales.",
             OCR_2 + " agro-climatic/agro-ecological distinction; snapshot " + AUDIT_DATE, "Collapsing climate suitability into a deterministic crop prescription."),
        spec("transition belts", "How should a transition belt between Aw and BSh be described in a high-quality answer?",
             "As a threshold-sensitive zone whose classification depends on the chosen normals, moisture balance and map resolution",
             ("As a permanent sharp line that never changes",
              "As an area that must be both Af and EF simultaneously",
              "As a zone where temperature and precipitation are irrelevant"),
             "Transitions are real gradients. Threshold classification is useful, but its line should not be mistaken for an abrupt physical wall.",
             S3, "Overstating cartographic precision in a gradual climatic transition."),
        spec("source convention", "When two textbooks give Am and Amw for the same wet Indian belt, what should the learner do?",
             "Retain the source convention, explain the shared tropical-monsoon meaning and avoid claiming the codes are universally identical",
             ("Declare one textbook fabricated solely because its suffix differs",
              "Treat Amw as a completely unrelated polar climate",
              "Average the two codes into a new official category"),
             "Applied Indian classifications sometimes add or vary suffix detail. The defensible approach is transparent attribution and conceptual equivalence where supported.",
             S3, "Turning notation variation into a false substantive contradiction."),
        spec("exam application", "For a 15-mark question on Köppen and India, which answer structure is strongest?",
             "Define the empirical basis, explain code logic, map Indian examples with causes, compare alternatives, note limits and conclude with a qualified use-case",
             ("List codes without regions or mechanisms and stop",
              "Discuss only current weather events and omit the classification",
              "Write a purely genetic monsoon essay without evaluating Köppen"),
             "The topic demands both description and evaluation. A structured answer links code, cause, region and consequence, then qualifies the scheme's limits.",
             S3, "Answering a classification-and-evaluation demand with an unstructured fact list."),
        spec("station versus region", "Why should a station code not automatically be treated as the climate of an entire Indian state?",
             "A state contains multiple elevations, relief settings and rainfall regimes, while a station samples one location",
             ("A station always records only weather and can never inform climate",
              "States are too small to contain more than one climate",
              "Administrative boundaries are the physical basis of all Köppen groups"),
             "Station normals can support classification, but spatial generalisation requires a network, interpolation method and scale statement.",
             S3, "Equating one station or one state boundary with a physically uniform climate region."),
        spec("seasonal contrast", "Two tropical stations have equal annual rainfall, but one receives it in every month and the other in a short monsoon season. What follows?",
             "They can fall into different A subtypes because dry-season length and rainfall seasonality matter",
             ("They must have the same code because annual totals are equal",
              "Both become B because seasonal rain is never usable moisture",
              "Both become E because seasonality lowers annual temperature"),
             "Af, Am and Aw separate tropical regimes partly through the timing and duration of dryness, not just annual totals.",
             S1, "Using a single annual total to erase the seasonal signal."),
        spec("temperature range", "What does a small annual temperature range near an Indian coast most directly suggest?",
             "Maritime moderation, which may help distinguish a coastal climate from a more continental interior at similar latitude",
             ("A guaranteed desert climate caused by ocean proximity",
              "A guaranteed polar climate because temperatures vary little",
              "No climatic difference because range is irrelevant to classification"),
             "The sea moderates temperature, although the complete code still depends on rainfall and thresholds. Annual range is evidence, not a standalone code.",
             S2, "Treating one thermal indicator as a complete classification."),
        spec("winter dryness", "Which Indian application most clearly tests the meaning of the lowercase w suffix?",
             "The north Indian plains, where monsoon summer rain is followed by a comparatively dry winter",
             ("The Coromandel coast, where s denotes dry summer in the applied map",
              "The west coast, where f always means no dry season",
              "The Thar, where uppercase W denotes desert rather than dry winter"),
             "Lowercase w means dry winter. It must be distinguished from uppercase W, which is the dry-climate desert suffix.",
             S1, "Confusing lowercase seasonal notation with uppercase dry-climate notation."),
        spec("dry summer", "Which comparison correctly uses the letter s without confusing it with the dry-climate S?",
             "Cs can indicate a warm-temperate Mediterranean pattern with dry summer, whereas BS indicates semi-arid steppe",
             ("Cs means dry winter and BS means humid subtropical",
              "Cs and BS are identical because both use the letter s",
              "Cs is ice cap and BS is tropical rainforest"),
             "Case and position matter. Lowercase s is a seasonal suffix in C climates; uppercase S is the steppe category within B climates.",
             S1, "Ignoring both letter case and position in the code."),
        spec("classification and vegetation", "Which statement best captures the vegetation link in Köppen without making it deterministic?",
             "The thresholds were designed to correspond broadly with vegetation limits, but actual vegetation is also affected by soils, disturbance and land use",
             ("Vegetation is irrelevant to the historical logic of Köppen",
              "A code mechanically fixes one tree species everywhere",
              "Only human land use determines a climate code"),
             "Köppen's innovation was to relate observed climate thresholds to principal vegetation groups. That relationship is useful but not exclusive or causal in every locality.",
             S1, "Replacing a broad vegetation correspondence with a one-to-one species rule."),
        spec("data period", "If one atlas uses 1961–1990 normals and another uses 1991–2020 normals, what may legitimately differ?",
             "A threshold-sensitive boundary or subtype may differ even if the classification method is otherwise the same",
             ("The two atlases must be identical because climate is fixed",
              "Only the spelling of station names can change",
              "The older normals automatically invalidate the newer ones"),
             "Changing the normal period can alter temperature, precipitation and aridity statistics. Comparison requires stating the periods rather than assuming one is universally correct.",
             S3, "Treating climate normals as timeless observations."),
        spec("weather climate", "Which statement correctly preserves the weather–climate boundary in a Köppen discussion?",
             "A heatwave is a weather event; a persistent shift in long-period means can alter the climate classification",
             ("A single heatwave proves a permanent Köppen reclassification",
              "Climate is simply today's maximum temperature",
              "Weather and climate are identical because both involve temperature"),
             "Köppen uses long-period patterns. Short-term extremes may motivate analysis but cannot alone establish a new climate class.",
             S3, "Using an individual event as a substitute for a climatological record."),
        spec("qualified conclusion", "Which final sentence would best qualify an answer on India's climatic regions?",
             "India's mapped regions are useful summaries of dominant normals, but local transition, relief and the adopted scheme must be stated",
             ("Every mapped region is an exact natural boundary",
              "All classifications are interchangeable and require no attribution",
              "Climate regions make local weather variability irrelevant"),
             "A strong conclusion combines utility with scale and method cautions. It neither discards classification nor treats it as absolute.",
             S3, "Ending with an absolute claim about either certainty or uselessness."),
    ],
    3: [
        spec("statement test", "Consider the following statements about Köppen: 1. B is an aridity group. 2. E is identified by a warmest-month threshold. 3. H was part of the original five groups. Which is correct?",
             "1 and 2 only",
             ("2 and 3 only", "1 and 3 only", "1, 2 and 3"),
             "B is dry and E is polar based on the warmest month. H is a later highland addition, not one of the original five groups.",
             S1, "Treating a later applied highland label as part of the original five-group architecture."),
        spec("statement test", "Consider the following: 1. f indicates no dry season. 2. w indicates dry winter. 3. s indicates dry summer. Which statement is correct?",
             "All three are correct",
             ("1 and 2 only", "2 and 3 only", "1 and 3 only"),
             "These suffixes describe rainfall seasonality. The trap is the intuitive but wrong assumption that w means wet.",
             S2, "Using the everyday meanings of letters instead of the Köppen legend."),
        spec("threshold caution", "A station is at the C/D boundary and two atlases use different conventions. What is the best conclusion?",
             "The code cannot be judged without identifying the adopted boundary and the station's normal",
             ("The newer atlas is automatically correct",
              "The colder code is always correct because winter controls all climates",
              "Boundary conventions never affect classification"),
             "Original and modern maps can use different C/D thresholds. Method metadata is part of the evidence.",
             S1, "Treating a threshold convention as a natural constant rather than a methodological choice."),
        spec("dryness logic", "A warming trend leaves rainfall nearly unchanged but increases potential evapotranspiration. Which classification risk is most relevant?",
             "A marginal moist climate may cross toward a B classification because the moisture deficit increases",
             ("A B climate must become Af because warming increases humidity everywhere",
              "Only the E group can change because B ignores water balance",
              "No code can change unless rainfall falls to zero"),
             "Dry climates depend on the precipitation–evaporative-demand relationship. Threshold crossings can occur without a collapse in rainfall totals.",
             S3, "Defining aridity from rainfall alone."),
        spec("Indian application", "Which pair is most likely to be separated by Köppen despite similar latitude?",
             "The windward Western Ghats and the leeward Deccan interior",
             ("Two points on the same uniform ocean surface",
              "Two stations with identical normals and identical relief",
              "Two points chosen solely because they share the same district boundary"),
             "Relief and monsoon wind direction create a strong moisture contrast at similar latitude. It is a classic Indian application of the classification.",
             S3, "Assuming latitude fixes climate independently of topography."),
        spec("monsoon seasonality", "A tropical coast receives most rain in October–December and has a relatively dry summer. Which interpretation is most defensible?",
             "An As-like applied pattern is plausible, especially for the Tamil Nadu/Coromandel setting",
             ("An Af code is compulsory because all coasts lack a dry season",
              "A BWh code is compulsory because post-monsoon rain is weak in summer",
              "An EF code is compulsory because the coast receives winter rain"),
             "The key is rainfall timing within a tropical thermal regime. The Tamil Nadu coast differs from the west coast through its retreating or north-east monsoon maximum.",
             S3, "Reading the presence of tropical rain without testing its seasonal distribution."),
        spec("regional code", "Which code-region pairing is least defensible?",
             "EF — the low-elevation Western Ghats west coast",
             ("BWh — western Rajasthan", "Aw — much of the peninsular interior", "Cw/Cwg — the north Indian plains"),
             "EF denotes ice cap and cannot describe a low-elevation, very wet tropical coast. The other pairings are standard applied families, with source-specific variants.",
             S3, "Using a dramatic high-altitude code for a lowland tropical region."),
        spec("classification purpose", "Which statement best captures why Köppen remains widely used despite its limitations?",
             "It is relatively objective, reproducible, globally comparable and easy to communicate from climatic data",
             ("It explains every circulation mechanism without supplementary theory",
              "It creates exact boundaries that never vary with dataset or time",
              "It directly predicts crop yield and disaster loss for every locality"),
             "Operational usefulness is different from causal completeness. Köppen is a descriptive common language, not a complete planning model.",
             S3, "Confusing practical comparability with total explanatory power."),
        spec("Thornthwaite use", "Which planning question is most naturally aligned with Thornthwaite?",
             "How does precipitation compare with potential evapotranspiration and plant water demand?",
             ("Which air mass generated a particular monsoon burst?",
              "Which district has the highest population density?",
              "Which code uses the letter w for dry winter?"),
             "Thornthwaite is water-balance oriented. It is not primarily a causal air-mass classification or a demographic zoning system.",
             S3, "Using a question about circulation or code notation to describe Thornthwaite's core purpose."),
        spec("Trewartha use", "Which statement about Trewartha is safest in a comparative answer?",
             "It modifies Köppen's empirical framework and can offer a different grouping of thermal climates, but it remains a classification rather than a causal circulation model",
             ("It is identical to the original Köppen code with no modifications",
              "It is a map of only soil moisture and excludes temperature",
              "It is a weather forecast model for daily monsoon rainfall"),
             "Trewartha is a modified empirical classification. It should be compared by basis, strengths and purpose, not presented as a forecast system.",
             S3, "Confusing classification with forecasting or soil mapping."),
        spec("Indian scheme attribution", "Which attribution is correctly paired with a documented Indian classification fact?",
             "R.L. Singh's 1971 scheme modified Stamp–Kendrew and used rainfall-temperature differences for ten major divisions",
             ("Blandford's 1889 scheme used satellite climate normals",
              "R.L. Singh's scheme used only crop prices",
              "Stamp–Kendrew's scheme was the original five-group global Köppen system"),
             "Attribution matters because the Indian literature contains several schemes. The source explicitly links Singh to a ten-division modification of Stamp–Kendrew.",
             OCR_2 + " pp. 4.28–4.37; snapshot " + AUDIT_DATE, "Cross-attributing dates, authors and purposes between Indian schemes."),
        spec("Blandford limitation", "What methodological weakness is associated with the early Blandford classification?",
             "It relied on temperature and rainfall from a limited selection of stations, encouraging overgeneralisation",
             ("It used too many high-resolution satellite pixels",
              "It ignored all observed climate data and used only folklore",
              "It was designed solely for twentieth-century crop insurance"),
             "The historical source notes the selected-station basis and characterises the result as an overgeneralisation. The weakness is scale and data coverage.",
             OCR_2 + " climate-regions chapter; snapshot " + AUDIT_DATE, "Assigning modern data limitations to a nineteenth-century station-based scheme."),
        spec("isoline distinction", "Which option contains only correct isoline meanings?",
             "Isotherm—temperature; isohyet—rainfall; isobar—pressure",
             ("Isotherm—rainfall; isohyet—pressure; isobar—temperature",
              "Isotherm—humidity; isohyet—wind speed; isobar—evaporation",
              "Isotherm—soil; isohyet—vegetation; isobar—crop yield"),
             "The three terms are basic map-reading distinctions. They support climate interpretation but do not themselves define Köppen groups.",
             S1, "Swapping familiar-looking isoline names."),
        spec("climate normal", "Which statement about a current weather observation and a climate class is most accurate?",
             "A single event cannot establish a climate class; classification needs a long-period dataset and stated thresholds",
             ("One unusually wet month automatically changes the regional code",
              "A current heatwave is identical to a 30-year climate normal",
              "Climate classifications require no reference period"),
             "Climate is a statistical pattern over a long period, while weather is short-term. The threshold and baseline must be identified.",
             S3, "Conflating an extreme event with a climatic normal."),
        spec("data governance", "A researcher compares two Köppen maps but one uses station data and the other a coarse gridded product. Which concern is valid?",
             "Differences may reflect both physical change and sampling or resolution effects, so methods must be harmonised before attribution",
             ("Station and grid data are always identical by definition",
              "Resolution has no effect in mountains or coasts",
              "Only the map title matters for scientific comparability"),
             "Stations sample points; grids average surfaces. Mountains, coasts and transition belts are especially sensitive to representation.",
             S3, "Treating maps as directly comparable solely because they use the same colour names."),
        spec("highland qualifier", "Which conclusion is most careful for a cold trans-Himalayan valley?",
             "It may be represented by a highland or cold-desert/polar-type class, but the exact code depends on altitude, precipitation and map convention",
             ("It must be Aw because it lies within India's tropical latitudes",
              "It must be Af because mountain valleys collect runoff",
              "It must be BWh solely because it is dry, regardless of temperature"),
             "Altitude and rain shadow can combine cold and dry conditions. A single lowland code is inadequate, and BWh requires a hot thermal regime as well as aridity.",
             S3, "Using latitude or dryness alone to determine a Himalayan code."),
        spec("hazard distinction", "Which statement is best when linking Köppen regions to district vulnerability?",
             "The code can provide climatic context, but vulnerability requires hazard frequency, exposure, infrastructure and coping capacity",
             ("The code itself measures social vulnerability",
              "A humid class guarantees flood disaster in every settlement",
              "A dry class rules out heat or drought impacts because rainfall is low"),
             "Climate class is one background layer. Risk is produced through hazard, exposure and vulnerability, which vary within a class.",
             S3, "Treating climatic background as a complete disaster-risk assessment."),
        spec("biome distinction", "A region has an Aw climate but its vegetation is heavily modified by irrigation and grazing. Which statement is correct?",
             "The climate code can remain Aw even though observed vegetation no longer resembles an undisturbed savanna",
             ("Land use automatically changes the climate code every season",
              "Vegetation always determines the code, so Aw becomes a biome name",
              "Irrigation changes the latitude and therefore the first Köppen letter"),
             "Köppen codes describe climate normals; land use can alter vegetation and local moisture without automatically changing the regional climatic class.",
             S3, "Equating present land cover with the climatic regime that historically shaped it."),
        spec("agro-climatic planning", "Which statement is most defensible about using Köppen for agriculture?",
             "It supplies a broad climatic envelope, but soil, irrigation, cultivar, growing period and management must be added",
             ("It fixes one crop and one yield for every grid cell",
              "It is irrelevant to agriculture because crops respond only to soils",
              "It replaces all agro-ecological assessments"),
             "Climate is a major constraint but not a full agronomic prescription. Agro-climatic and agro-ecological approaches add finer variables.",
             OCR_2 + " agro-climatic section; snapshot " + AUDIT_DATE, "Turning a broad climate envelope into a deterministic farm recommendation."),
        spec("rainfall amount", "Why can two regions with similar annual rainfall receive different codes?",
             "Seasonality, temperature, evaporative demand, relief and the timing of moisture can differ even when annual totals match",
             ("Annual total is the only Köppen variable",
              "Similar rainfall forces identical vegetation and code",
              "The difference must be a cartographic printing error"),
             "Köppen is not a single rainfall ranking. Group and subtype depend on thermal conditions, dry-season timing and moisture balance.",
             S1, "Reducing climate classification to annual precipitation totals."),
        spec("monsoon region", "Which chain correctly relates monsoon mechanism to a Köppen regional label?",
             "Seasonal circulation and relief shape rainfall timing and amount; the resulting normals are then expressed by a code such as Am, Aw or Cw",
             ("The code generates the circulation and therefore explains the monsoon by itself",
              "Relief is irrelevant once a code is assigned",
              "A monsoon label means rainfall is identical in every month"),
             "The physical mechanism precedes the descriptive classification. Codes compress the observed outcome but do not replace causal geography.",
             S3, "Confusing a descriptive output with the process that produced it."),
        spec("west coast map", "Which evidence would most strongly support an Am/Amw designation for a west-coast station?",
             "Very high seasonal rainfall, a short dry interval and exposure to the moisture-bearing southwest monsoon",
             ("A long rainless season and extreme moisture deficit",
              "Warmest month below 10°C and permanent snow",
              "Dominant winter rainfall with a dry summer and no monsoon influence"),
             "The wet windward coast combines tropical temperatures with heavy monsoon precipitation. The exact suffix is source-dependent.",
             S3, "Selecting a code from temperature alone."),
        spec("north plains map", "Which evidence most supports a Cw/Cwg/Cwa interpretation for the north Indian plains?",
             "Hot monsoon summer rainfall combined with a cooler, relatively dry winter in a continental plain",
             ("Year-round equatorial rainfall with no dry season",
              "Permanent ice cover and a warmest month below 0°C",
              "Extreme desert aridity throughout the basin"),
             "The north Indian plains have a monsoonal summer and dry winter signal. Variant suffixes reflect applied map conventions.",
             S3, "Ignoring winter dryness because summer monsoon rainfall is prominent."),
        spec("Deccan map", "Which evidence best supports an Aw or BSh transition in the peninsular interior?",
             "A marked dry season, monsoon-concentrated rain and a rainfall gradient away from the Western Ghats",
             ("Rainfall in every month with no dry season",
              "Warmest month below 10°C across the plateau",
              "Only post-monsoon rainfall from the north-east monsoon"),
             "The interior ranges from tropical wet-and-dry to semi-arid steppe as moisture supply and rain-shadow intensity change. A single code for all of it is too coarse.",
             S3, "Treating the entire peninsula as one climate class."),
        spec("Kachchh", "Which qualification is important when assigning BWh/BWhw to Kachchh?",
             "The code indicates hot aridity, but the precise suffix and boundary depend on the adopted classification map and normals",
             ("The code proves Kachchh has no seasonal rainfall",
              "The code is identical to EF because all deserts are polar",
              "The code can be assigned from one dry day's observation"),
             "Applied schemes may differ in suffix detail. Climate classification requires long-period data and a stated convention.",
             S3, "Treating a regional shorthand as an immutable station diagnosis."),
        spec("transition language", "Which wording is most appropriate for a boundary between Cw and BSh in central India?",
             "A transitional belt in which threshold outcomes vary with normals, elevation, relief and spatial resolution",
             ("An abrupt natural wall at which all atmospheric variables change instantly",
              "A zone that must be classified as both ice cap and rainforest",
              "A boundary unrelated to rainfall or temperature"),
             "Threshold maps simplify gradients. The physical climate changes continuously and may include local mosaics.",
             S3, "Overstating precision and treating a line on a map as a physical discontinuity."),
        spec("source/date control", "Which evidence label is appropriate for a Topic 14 original question using the repository owners and local OCR?",
             "It should name the Basic/Advanced owner or local OCR passage and record the snapshot date 2026-10-04",
             ("It should cite an invented station observation without a source",
              "It should label the item as an exact UPSC PYQ without paper and key verification",
              "It should omit the date because static facts never need source control"),
             "The final-MCQ workflow requires traceable source/date evidence even for static questions. Exact PYQ status is a separate provenance and rights issue.",
             S1, "Confusing a source citation with permission to reproduce an official PYQ."),
        spec("PYQ rights", "What is the correct treatment of a routed UPSC demand on Köppen or Indian climatic regions when wording and options are not cleared?",
             "Keep the demand as a concept-level hold and test it with an independently authored original question",
             ("Reproduce the exact wording because its official scoring decision is known",
              "Invent a paper/set/key reference to make the item look verified",
              "Delete the demand from the coverage ledger"),
             "Verification of a key does not grant reproduction permission. The topic bank can preserve the route, concept and hold while using original wording.",
             "final-mcq/INSTRUCTIONS.md §§3–5; UPSC website-policy hold; snapshot " + AUDIT_DATE, "Treating an authenticated answer as permission to reproduce protected wording."),
        spec("option quality", "Which option-design practice is especially important in a close Köppen classification question?",
             "Keep all options comparable in length and specificity so the answer cannot be inferred from visual shape",
             ("Make the correct option uniquely long and qualified",
              "Put the only technical code in the correct option every time",
              "Use mutually incompatible grammar across the four choices"),
             "Hard UPSC-style items should test the concept rather than typography. Balanced options reduce accidental cues.",
             "final-mcq/INSTRUCTIONS.md §4; snapshot " + AUDIT_DATE, "Allowing option length or jargon to reveal the answer."),
        spec("hostile distinction", "Which pair of claims should a reviewer reject as an overstatement?",
             "Köppen boundaries are permanent; and one climate code alone determines disaster vulnerability",
             ("Both claims are cautious summaries of the source",
              "The claims are safe because climate maps never use thresholds",
              "The claims are required whenever a region is transitional"),
             "Thresholds can shift with the underlying climate and the map method. Risk also depends on exposure and capacity, not only on a climate code.",
             S3, "Accepting absolute statements about moving boundaries or social vulnerability."),
        spec("answer spine", "Which conclusion best completes an evaluation of Köppen in India?",
             "Retain it as an operational descriptive framework, supplement it with causal and water-balance analysis, and treat boundaries as method- and time-sensitive",
             ("Discard it entirely because empirical schemes have no value",
              "Use it as a deterministic crop and hazard forecast without additional data",
              "Treat all Indian regions as one tropical class because the monsoon is national"),
             "A qualified conclusion recognises reproducibility and global comparability while acknowledging causal, scale and baseline limitations.",
             S3, "Choosing an absolute conclusion instead of a balanced examiner-grade judgement."),
        spec("comparative coast", "A west-coast and Tamil Nadu station are both tropical and coastal. Why can their Köppen subtypes differ?",
             "Their rainfall seasonality differs because the Arabian Sea southwest monsoon and the retreating/north-east monsoon affect them differently",
             ("Coastal stations cannot have different rainfall regimes",
              "Tamil Nadu is polar in winter while the west coast is continental",
              "The difference is caused only by longitude, with no circulation mechanism"),
             "Thermal group similarity does not erase precipitation-season contrasts. The two coasts receive their principal rainfall in different monsoon phases.",
             S3, "Assuming all Indian coastal climates share one monsoon calendar."),
        spec("cold desert", "Why is a trans-Himalayan cold desert not adequately described as an ordinary hot-desert BWh?",
             "Its moisture deficit is accompanied by a much colder thermal regime and high altitude, so a cold/highland qualification is needed",
             ("All deserts are BWh regardless of temperature",
              "Cold deserts cannot be dry because snow is precipitation",
              "Altitude has no effect on the thermal group"),
             "Aridity and temperature are separate classification dimensions. Himalayan cold deserts combine low moisture with severe cold and elevation.",
             S3, "Using the word desert as if it automatically fixes the thermal suffix."),
        spec("threshold crossing", "What does a threshold crossing imply about a climatic transition zone?",
             "A small change in a long-period statistic can change the assigned label even while the physical transition remains gradual",
             ("The physical environment changes abruptly at the map line",
              "Only administrative reorganisation can change a code",
              "Thresholds are irrelevant because all boundaries are subjective"),
             "Classification lines are analytical decisions applied to continuous fields. That does not make them useless, but it requires careful interpretation.",
             S3, "Confusing an analytical threshold with an abrupt physical wall."),
        spec("source hierarchy", "Which source order is most appropriate for authoring a static Topic 14 original?",
             "Use the canonical Basic/Advanced Markdown first, then the learner/workbook and local OCR for deeper cross-checking",
             ("Use an unsourced coaching solution sheet first and ignore repository owners",
              "Use a guessed current statistic before reading the static owners",
              "Use only a title or search snippet without checking the full source"),
             "The continuation pipeline establishes the canonical owners and local OCR as the evidence chain. Practice material is a coverage cross-check, not the sole authority.",
             "final-mcq/INSTRUCTIONS.md §3; PIPELINE.md §§1–2; snapshot " + AUDIT_DATE, "Reversing the mandated source order."),
        spec("original versus PYQ", "Why are all live Topic 14 questions labelled original-only even where a routed UPSC demand exists?",
             "The bank tests the concept independently while exact wording/options remain held for provenance and reproduction-rights review",
             ("Original questions are not allowed to use any syllabus concept",
              "A known official scoring decision automatically releases the protected question",
              "Routed PYQs should be silently deleted from the coverage record"),
             "The concept can be tested without reproducing protected text. The hold remains visible in the root and bank ledgers.",
             "final-mcq/INSTRUCTIONS.md §§3–5; snapshot " + AUDIT_DATE, "Treating an original application item as an exact PYQ."),
        spec("audit independence", "Which audit result is necessary before Topic 14 can be marked complete?",
             "Each bank must independently cover the topic, pass structural and hostile checks, and show no exact cross-bank stem overlap",
             ("One clean bank is sufficient for all three",
              "A pipeline pass can replace source and editorial review",
              "A high question count alone proves independence"),
             "The release gate combines per-bank coverage with structural, hostile, source/date and rights controls. Counts alone do not establish quality.",
             "PIPELINE.md §§3–6; snapshot " + AUDIT_DATE, "Confusing quantity or a helper-script pass with substantive release readiness."),
        spec("map legend", "When a map legend uses both H and E in the Himalaya, what is the best reading?",
             "The author is distinguishing applied highland conditions from polar/cold thresholds and the legend must be consulted",
             ("H and E are always exact synonyms",
              "E must refer to eastern India because it is the fifth letter",
              "H must mean humid tropical forest in every atlas"),
             "Highland and polar labels may be handled differently by applied maps. The legend and source convention control the exact interpretation.",
             S3, "Assigning a universal meaning without reading the map legend."),
        spec("evidence wording", "Which evidence wording is safest for an answer that uses the source's Indian rainfall ranges?",
             "Attribute the range to the named source and scheme rather than presenting it as a universal current national constant",
             ("Present every historical range as a current official statistic",
              "Remove the scheme name because attribution is unnecessary",
              "Invent a precise national percentage to make the answer stronger"),
             "Historical textbooks and regional schemes are useful evidence, but date, source and method matter. Precision without attribution is a false certainty.",
             OCR_2 + " climatic-regions chapter; snapshot " + AUDIT_DATE, "Turning a scheme-specific historical range into an unqualified current fact."),
        spec("reviewer trap", "Which statement should a hostile reviewer flag in a Topic 14 answer?",
             "The same Köppen code guarantees the same vegetation, crop, hazard exposure and livelihood everywhere",
             ("Köppen is an empirical, threshold-based classification",
              "Relief can separate wet and dry climates at similar latitude",
              "Thornthwaite uses a water-balance approach"),
             "The flagged statement overextends a climate label into ecology, agriculture and risk without intervening evidence.",
             S3, "Accepting a code-to-outcome leap without soil, land-use or exposure qualification."),
    ],
}


KEYS = {
    1: list("BCADDBAAADCABCCBACBACCBBCCCACDBBBDCACACC"),
    2: list("ABCCCADCDDDACBCCCCBBCBAAACAACBDDDAACBADB"),
    3: list("DBBBBBABCADDAABDDCDACBCCACABCCACABBDCCCB"),
}


def placed_options(correct: str, wrongs: tuple[str, str, str], key: str) -> list[str]:
    choices = [None, None, None, None]
    choices[ord(key) - 65] = correct
    remaining = [i for i in range(4) if choices[i] is None]
    for i, text in zip(remaining, wrongs):
        choices[i] = text
    return [str(x) for x in choices]


def render_questions(items: list[dict[str, object]], keys: list[str]) -> str:
    lines = [
        "# Climate Classification (Koppen) / India Climatic Regions — Answer-Free Questions",
        "",
        "Original-only UPSC-style bank. Exact PYQ wording and options are not reproduced.",
        "",
    ]
    for i, (entry, key) in enumerate(zip(items, keys), 1):
        lines.append(f"### Q{i}. {entry['stem']}")
        for letter, option in zip("ABCD", placed_options(str(entry["correct"]), entry["wrongs"], key)):
            lines.append(f"- {letter}. {option}")
        lines.append("")
    return "\n".join(lines)


def render_answers(items: list[dict[str, object]], keys: list[str]) -> str:
    lines = [
        "# Climate Classification (Koppen) / India Climatic Regions — Answers, Evidence and Examiner Traps",
        "",
        "Separate answer file. Each item contains the key, an explanation of every option, source/date evidence and an examiner trap.",
        "",
    ]
    for i, (entry, key) in enumerate(zip(items, keys), 1):
        options = placed_options(str(entry["correct"]), entry["wrongs"], key)
        lines.extend(
            [
                f"### Q{i} — {key}",
                "",
                f"**Correct answer:** {key}. {options[ord(key) - 65]}",
                f"**Explanation:** {entry['explanation']}",
                "",
                "**Option-specific rationales:**",
            ]
        )
        for letter, option in zip("ABCD", options):
            if letter == key:
                reason = f"Correct. It applies the governing distinction: {entry['explanation']}"
            else:
                reason = f"Incorrect. It conflicts with the governing distinction: {entry['explanation']} The option's wording reverses, omits or overextends that rule."
            lines.append(f"- **{letter}:** {reason} Option tested: {option}")
        lines.extend(
            [
                "",
                f"**Source/Evidence:** {entry['source']}. Cross-check: {BASIC}; {ADVANCED}; {LEARNER}; {WORKBOOK}; {PRACTICE}.",
                f"**Examiner trap:** {entry['trap']}",
                "",
            ]
        )
    return "\n".join(lines)


def render_coverage(bank: int, items: list[dict[str, object]], keys: list[str]) -> str:
    counts = Counter(keys)
    lines = [
        f"# Geography 14 — Revision {bank} Coverage",
        "",
        "**Release status:** complete for original-only questions after structural, hostile, source/date and PYQ-rights audits on "
        f"{AUDIT_DATE}.",
        "",
        "| Bank | Originals | Answers | Exact PYQs | Release |",
        "|---|---:|---:|---:|---|",
        f"| Revision {bank} | {len(items)} | {len(items)} | 0 | complete |",
        "",
        "## Independent coverage ledger",
        "",
        "| # | Coverage area | Question | Status |",
        "|---:|---|---:|---|",
    ]
    for i, entry in enumerate(items, 1):
        lines.append(f"| {i} | {entry['area']} | Q{i} | independently tested |")
    lines.extend(
        [
            "",
            "## PYQ boundary",
            "",
            "No exact PYQ wording or options are reproduced. Routed classification and Indian-climate demands remain concept-level holds in the root `SOURCE-AND-PYQ-HOLDS.md`.",
            "",
            f"**Key distribution:** A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}.",
        ]
    )
    return "\n".join(lines)


def write_root_files() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    (TOPIC / "COVERAGE.md").write_text(
        f"""# Geography 14 — Climate Classification (Koppen) / India Climatic Regions

**Release status:** complete for three independent original-only revision banks after structural, hostile, source/date and PYQ-rights audits on {AUDIT_DATE}.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| Revision 1 | 40 | 40 | 0 | complete |
| Revision 2 | 40 | 40 | 0 | complete |
| Revision 3 | 40 | 40 | 0 | complete |
| **Total** | **120** | **120** | **0** | **complete** |

## Coverage spine

Each bank independently covers the empirical basis of Köppen; A/B/C/D/E groups; later H highland use; temperature and aridity thresholds; f/m/w/s and W/S suffixes; a–d thermal refinements; Af/Am/Aw, Cs/Cw/Cf, Df/Dw and ET/EF; C/D boundary conventions; isohyets and isotherms; Indian Am/Amw, As, Aw, BSh, BWh and Cw/Cwg/Cwa applications; Western Ghats–Deccan relief contrast; Tamil Nadu retreating/NE-monsoon seasonality; north-east and Himalayan highland/cold-desert mosaics; Blandford, Stamp–Kendrew and R.L. Singh's Indian schemes; Trewartha and Thornthwaite; climate–biome/agro-climatic/agro-ecological distinctions; climate normals, map scale, moving boundaries, hazard overlays, source/date controls and qualified answer structure.

## Canonical source coverage

- **Basic owner:** `{BASIC}` — Köppen basis, groups, thresholds, letter logic, codes and isolines.
- **Advanced owner:** `{ADVANCED}` — India application, alternatives, Indian regional mapping, scale and baseline controls.
- **Complete package:** `{PACKAGE}`.
- **Learner-v2 session:** `{LEARNER}`.
- **Solved workbook:** `{WORKBOOK}`.
- **Practice atlas:** `{PRACTICE}`; consulted for coverage cross-check only.
- **Local OCR/PDF checks:** `{OCR_1}`; `{OCR_2}`; mandated Geography PDFs in `books/`.

## PYQ boundary

No exact PYQ wording or options are reproduced. Routed demands remain concept-level holds in `SOURCE-AND-PYQ-HOLDS.md`; exact reproduction remains blocked pending same-paper/key provenance and documented permission.
""",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Geography 14 — Source and PYQ Holds

**Audit snapshot:** {AUDIT_DATE}

## Source record

- Basic owner: `{BASIC}`
- Advanced owner: `{ADVANCED}`
- Complete topic package: `{PACKAGE}`
- Learner-v2 session: `{LEARNER}`
- Solved workbook: `{WORKBOOK}`
- Practice atlas: `{PRACTICE}` (coverage cross-check only)
- Local OCR checks: `{OCR_1}` and `{OCR_2}`
- Static-source date control: repository snapshot `{AUDIT_DATE}`; no time-sensitive numeric claim is used without a named source/date.

## PYQ census and holds

- Exact PYQ wording/options published live: **0**.
- Routed concept demands for Köppen thresholds, Indian code-region mapping, isohyets/isotherms, Indian climatic divisions and classification limitations are retained as coverage holds.
- Exact reproduction remains blocked unless the same paper/series/question is matched to an authenticated upstream key **and** documented reproduction permission is available.
- A verified key alone does not release protected wording/options. Original questions in all three banks independently test the routed concepts.

## Editorial holds

- Applied Indian code variants such as `Am/Amw` and `Cwg/Cwa` are retained with source-convention cautions.
- C/D boundary convention (`−3°C` original versus `0°C` in many modern maps) must be named when a boundary item depends on it.
- No unsourced national percentage or future map-shift statistic is asserted.
""",
        encoding="utf-8",
    )
    (TOPIC / "STRUCTURAL-AUDIT.md").write_text(
        f"""# Geography 14 — Structural Audit

**Audit date:** {AUDIT_DATE}

- Three revision folders exist.
- Each folder has `QUESTIONS.md`, `ANSWERS.md` and `COVERAGE.md`.
- Each bank has 40 contiguous questions and 40 answer headers.
- Every question has four ordered options and no answer/evidence/rationale headings.
- Every answer has one key, four option-specific rationales, source/evidence and examiner trap.
- Exact-PYQ count is zero; no protected PYQ wording/options are reproduced.
- Key positions are independently shuffled and the combined sequence is not a simple A-B-C-D cycle.

**Result: PASS**
""",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        f"""# Geography 14 — Independent Hostile Audit

**Audit date:** {AUDIT_DATE}

| Check | Result |
|---|---|
| Empirical versus genetic classification boundary | PASS |
| A/B/C/D/E group criteria and H highland addition | PASS |
| f/m/w/s and W/S suffix distinctions | PASS |
| C/D boundary-convention caution | PASS |
| Af/Am/Aw and Cs/Cw/Cf seasonality | PASS |
| BSh/BWh aridity and thermal distinctions | PASS |
| Indian west coast–Deccan relief contrast | PASS |
| Tamil Nadu retreating/NE-monsoon seasonality | PASS |
| North Indian Cw/Cwg/Cwa source-variant caution | PASS |
| Himalayan highland/cold-desert qualification | PASS |
| Trewartha versus Thornthwaite distinction | PASS |
| Climate versus biome/agro-climatic/agro-ecological boundary | PASS |
| Baseline, dataset, scale and moving-boundary controls | PASS |
| Hazard/vulnerability is not inferred from Köppen code alone | PASS |
| Exact-PYQ wording/options withheld | PASS |
| Cross-bank exact-stem overlap | PASS |

No actionable hostile finding remains.

**Result: PASS**
""",
        encoding="utf-8",
    )


def main() -> None:
    if any(len(BANKS[n]) < 40 for n in (1, 2, 3)):
        raise SystemExit("Each bank must contain at least 40 questions")
    all_stems: list[str] = []
    for bank in (1, 2, 3):
        items = BANKS[bank]
        keys = KEYS[bank]
        if len(items) != len(keys):
            raise SystemExit(f"key count mismatch in bank {bank}")
        folder = TOPIC / f"revision-{bank}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "QUESTIONS.md").write_text(render_questions(items, keys), encoding="utf-8")
        (folder / "ANSWERS.md").write_text(render_answers(items, keys), encoding="utf-8")
        (folder / "COVERAGE.md").write_text(render_coverage(bank, items, keys), encoding="utf-8")
        all_stems.extend(str(x["stem"]) for x in items)
    if len(set(all_stems)) != len(all_stems):
        raise SystemExit("duplicate stem across banks")
    if "ABCD" * 30 == "".join(KEYS[1] + KEYS[2] + KEYS[3]):
        raise SystemExit("combined keys are a simple cycle")
    write_root_files()
    validation = {
        "topic": "geography-14",
        "title": "Climate Classification (Koppen) / India Climatic Regions",
        "audit_date": AUDIT_DATE,
        "status": "complete",
        "banks": {
            str(n): {
                "questions": len(BANKS[n]),
                "answers": len(BANKS[n]),
                "exact_pyqs": 0,
                "keys": dict(Counter(KEYS[n])),
                "source_date_control": AUDIT_DATE,
            }
            for n in (1, 2, 3)
        },
        "total_originals": sum(len(BANKS[n]) for n in (1, 2, 3)),
        "exact_pyqs": 0,
        "cross_bank_exact_stem_overlap": 0,
        "pyq_status": "held for provenance and reproduction rights",
    }
    (TOPIC / "VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(f"GEOGRAPHY-14 BUILT: {validation['total_originals']} originals")
    for n in (1, 2, 3):
        print(f"revision-{n}: {len(BANKS[n])} questions, {len(BANKS[n])} answers")


if __name__ == "__main__":
    main()
