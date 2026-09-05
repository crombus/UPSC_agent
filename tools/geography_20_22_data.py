"""Authored Geography learner-v2 data for Topics 20-22."""

from __future__ import annotations

import generate_geography_common as common


def plan(
    title: str, indexes: list[int], caution: str, exam_use: str
) -> tuple[str, list[int], str, str]:
    return title, indexes, caution, exam_use


def panel(
    title: str,
    kind: str,
    lines: list[str],
    references: list[str],
) -> tuple[str, str, str, list[str]]:
    return title, kind, "\n".join(lines), references


# ═══════════════════════════════════════════════════════════════════════════════
# TOPIC 20 — Temperate Continental Steppe Climate
# Basic owner: basic/20_Temperate-Continental-Steppe-Climate.md
# Advanced owner: advanced/20_India-Wheat-Granary.md
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_20 = common.topic(
    20,
    "Temperate Continental Steppe Climate",
    "20_Temperate-Continental-Steppe-Climate.md",
    "20_India-Wheat-Granary.md",
    "20_India-Wheat-Granary_Complete-Topic-Package.md",
    [
        ("Steppe continental-interior location", "The temperate continental or steppe climate occurs in mid-latitude continental interiors, bordering deserts and far from maritime influence, with major expressions in Eurasia, North America, South America, South Africa and Australia."),
        ("Local grassland names", "The biome is named differently by region: steppes in Eurasia, prairies in USA and Canada, pampas in Argentina and Uruguay, veld in South Africa and downs in Australia; all share nutritious grasses that flower in spring and early summer."),
        ("Continentality control", "The controlling factor is continentality: distance from the sea produces hot summers, cold winters and a large annual temperature range, especially in northern hemisphere interiors where continental mass is greatest."),
        ("Rainfall regime", "Rainfall is low to moderate, about 25 to 75 centimetres annually, with most falling in late spring and early summer; the defining character is moisture deficit rather than extreme aridity."),
        ("Hemisphere contrast", "Northern hemisphere steppes and prairies experience more extreme temperatures than southern hemisphere pampas, veld and downs because southern continents are narrower and more maritime."),
        ("Natural grassland cover", "Natural cover is grassland, practically treeless, with tree scarcity controlled by seasonal moisture deficit, continentality, fire and grazing rather than by poor soil alone."),
        ("Grass height gradient", "Grass is shorter toward the desert margin and taller toward the wetter margin, reflecting a moisture gradient that also controls the boundary between steppe and forest."),
        ("Chernozem and prairie soils", "Steppe and prairie soils such as chernozem or black earth are humus-rich because of centuries of grass-root decay under low leaching, and are among the most fertile agricultural soils in the world."),
        ("Granary identity", "The temperate grasslands are the granaries of the world, with major wheat belts in the Ukrainian steppe, North American prairies and Argentine pampas, supported by level relief permitting mechanisation."),
        ("Ranching economy", "These grasslands also support commercial grazing and ranching on a large scale, with temperate grasslands alongside tropical savannas as leading areas of extensive livestock production."),
        ("Transport-conversion argument", "The physical endowment did not create the granaries by itself: rail penetration, ocean freight, mechanisation and external market demand converted pastoral or unexploited interiors into surplus wheat suppliers, which is the strongest available counter to environmental determinism in this climate sequence."),
        ("Ecological cost of ploughing", "Ploughing removes the protective grass sod, exposing fine soil to wind erosion in drought years; consequences include the Dust Bowl analogy, organic-matter decline and aquifer drawdown where irrigation was added."),
        ("India climate boundary", "India has no true temperate-steppe wheat climate like Eurasia's chernozem grasslands, but the Indo-Gangetic alluvial plain, especially Punjab-Haryana-western Uttar Pradesh, plays the equivalent economic role as India's wheat granary."),
        ("India alluvial distinction", "India's wheat belt sits on Indo-Gangetic alluvial soil, not black chernozem like the steppe; the economic analogy holds but the pedological basis is fundamentally different."),
        ("Green Revolution package", "The Green Revolution package of HYV semi-dwarf wheat, fertiliser, assured canal and tube-well irrigation and MSP procurement transformed the north-western plains into a surplus granary, with Punjab described as a major food basket region in the source text."),
        ("Rabi crop identity", "Wheat is a Rabi or winter crop in India, sown October to December and harvested March to April, which is the seasonal reverse of the northern-hemisphere temperate summer growing season."),
        ("Haryana wheat belt", "Khullar lists a broad Haryana wheat belt across the eastern irrigated districts and central-western plains; district names and boundaries from older editions should not be treated as a current exhaustive list."),
        ("Sustainability crisis", "Intensive wheat-rice systems in Punjab-Haryana have sustainability costs including groundwater depletion, soil-nutrient imbalance and stubble-burning; MSP procurement concentrates these pressures in a narrow belt."),
        ("Savanna-steppe comparison", "Both the savanna and the steppe are grasslands, but tropical versus temperate latitude, wet-and-dry versus low-total-with-summer-maximum rainfall, leached laterising versus base-rich chernozem soils, and pastoral-subsistence versus mechanised-commercial grain distinguish them."),
        ("Transparent zero-direct route", "The audited routing ledgers contain no direct question owned by Geography Topic 20; steppe and granary concepts may be tested through adjacent climate-agriculture questions but no solved PYQ is fabricated."),
    ],
    [
        "Do not claim temperate grasslands are treeless because soils are poor.",
        "Do not equate steppes and pampas as having identical climates.",
        "Do not reverse the rainfall regime to winter-maximum.",
        "Do not call temperate grasslands only grazing lands.",
        "Do not label chernozem as a desert or laterite soil.",
        "Do not attribute the granary role to physical endowment alone.",
        "Do not ignore wind erosion risk from ploughing the sod.",
        "Do not place India's wheat belt on chernozem soil.",
        "Do not call wheat a Kharif monsoon crop in India.",
        "Do not quote Khullar's book-era percentages as current statistics.",
        "Do not equate MSP with the open-market price.",
        "Do not invent a direct PYQ for this topic.",
    ],
    [
        (10, "Explain why temperate continental interiors are treeless grasslands despite fertile soils.", "Treelessness is a moisture-deficit and disturbance outcome from continentality, fire and grazing, not a soil-fertility outcome; the chernozem soils are among the most fertile in the world.", [0, 5, 7]),
        (10, "Compare the steppe and pampas in terms of climate severity and maritime influence.", "Northern hemisphere steppes have more extreme temperatures because of larger continental mass, while southern hemisphere pampas are moderated by surrounding ocean and narrower landmass.", [2, 4, 3]),
        (15, "Explain why the temperate grasslands became the world's granaries and what ecological cost this conversion carried.", "Chernozem fertility, level relief and mechanisation provided the physical base, but rail, freight and market demand were the converting agents; ploughing removed the protective sod and created wind-erosion and aquifer risks.", [8, 10, 11]),
        (15, "Assess how India's Indo-Gangetic wheat granary compares with the world's temperate steppe granaries.", "India's wheat belt shares the granary function but sits on alluvial soil, relies on the Rabi season, and was transformed by the Green Revolution package rather than by rail-and-mechanisation alone.", [12, 13, 14, 15]),
        (20, "Analyse the transport-conversion argument as a counter to environmental determinism in the temperate grasslands.", "The grasslands were pastoral or unexploited for centuries despite identical soils and became granaries only when railways, mechanisation and ocean freight connected them to distant markets; this is the strongest evidence that physical endowment requires institutional access to become a resource.", [10, 8, 6, 11]),
        (20, "Design a sustainability strategy for the Punjab-Haryana wheat-rice system using the steppe-conversion lesson.", "The steppe lesson shows that converting a natural grassland into a monoculture granary carries predictable ecological costs; apply conservation tillage, crop diversification, groundwater regulation and MSP reform to the Indo-Gangetic system.", [17, 14, 13, 18]),
    ],
    [
        plan("Steppe location and continental setting", [0], "Continental interior is a guide, not a fixed boundary.", "Locate Eurasia, North America and southern grasslands before explaining process."),
        plan("Local grassland names", [1], "Do not treat all five names as one identical biome.", "Use regional names to distinguish steppe, prairie, pampas, veld and downs."),
        plan("Continentality and temperature range", [2], "Do not reverse hot summers and cold winters.", "Explain how distance from the sea drives the large annual range."),
        plan("Rainfall regime and moisture deficit", [3], "Do not call this a winter-maximum regime.", "Use the 25-75 cm and late-spring maximum as the defining character."),
        plan("Hemisphere contrast", [4], "Southern grasslands are milder, not identical to northern.", "Compare continental mass and maritime influence."),
        plan("Natural grassland and treelessness", [5, 6], "Do not attribute treelessness to poor soil.", "Explain the moisture-fire-grazing complex."),
        plan("Chernozem formation and fertility", [7], "Chernozem is not a desert or laterite soil.", "Follow the grass-root decay to humus-rich soil chain."),
        plan("Granary identity and wheat belts", [8, 9], "Do not reduce the granary to soil alone.", "Map Ukraine, prairies and pampas as wheat-and-ranching belts."),
        plan("Transport-conversion argument", [10], "The physical base was necessary but not sufficient.", "Build the anti-determinism argument explicitly."),
        plan("Ecological cost of ploughing", [11], "Do not ignore the sod-removal risk.", "Follow sod removal to wind erosion, organic decline and aquifer drawdown."),
        plan("India climate boundary", [12], "India has no true steppe climate.", "Preserve global Basic versus India Advanced ownership."),
        plan("Alluvial-chernozem distinction", [13, 15], "India's wheat belt is alluvial, not chernozem.", "Compare Rabi season with temperate summer growing season."),
        plan("Green Revolution and granary conversion", [14, 16], "Do not quote book-era percentages as current.", "Map the HYV-irrigation-MSP transformation."),
        plan("Sustainability and savanna-steppe comparison", [17, 18], "Both are grasslands but differ in mechanism and outcome.", "Use the comparison to distinguish tropical from temperate grassland systems."),
        plan("PYQ boundary and answer spine", [19], "No direct PYQ is owned by this topic.", "Close with the transparent zero-direct-PYQ audit."),
    ],
    [
        panel("Temperate grassland world map", "spatial-map", [
            "EURASIA -> steppes: Ukraine-Kazakhstan belt, continental interior",
            "NORTH AMERICA -> prairies: Great Plains, USA and Canada",
            "SOUTH AMERICA -> pampas: Argentina and Uruguay, maritime fringe",
            "SOUTH AFRICA -> veld: elevated interior plateau",
            "AUSTRALIA -> downs: eastern interior grasslands",
        ], ["Steppe location and continental setting"]),
        panel("Continentality mechanism", "process-flow", [
            "DISTANCE FROM SEA -> weak maritime moderation",
            "SUMMER -> strong heating of continental mass -> hot",
            "WINTER -> strong radiative cooling -> cold",
            "RESULT -> large annual temperature range, especially in Eurasia",
        ], ["Continentality and temperature range"]),
        panel("Rainfall-moisture profile", "comparison-table", [
            "TOTAL ANNUAL -> about 25-75 cm, low to moderate",
            "SEASONAL MAXIMUM -> late spring and early summer",
            "DRY MARGIN -> shorter grass, steppe-desert transition",
            "WET MARGIN -> taller grass, steppe-forest boundary",
        ], ["Rainfall regime and moisture deficit", "Natural grassland and treelessness"]),
        panel("Hemisphere asymmetry", "comparison-table", [
            "NORTHERN -> steppes and prairies: large continental mass, extreme range",
            "SOUTHERN -> pampas, veld, downs: narrower landmass, maritime moderation",
            "CAUSE -> continental mass determines winter severity",
            "EXAM TRAP -> do not treat all five as climatically identical",
        ], ["Hemisphere contrast"]),
        panel("Chernozem-soil chain", "causal-system", [
            "GRASSLAND COVER -> deep root network decays in place",
            "LOW LEACHING -> base-rich conditions preserved",
            "HUMUS ACCUMULATES -> dark, deep, fertile soil profile",
            "RESULT -> chernozem or black earth, among world's most fertile",
        ], ["Chernozem formation and fertility"]),
        panel("Granary conversion timeline", "process-flow", [
            "NATURAL STATE -> pastoral grassland, low-density use",
            "RAIL + OCEAN FREIGHT -> access to distant industrial markets",
            "MECHANISATION + HYV -> high output per worker on level plains",
            "RESULT -> world's wheat granaries: Ukraine, prairies, pampas",
        ], ["Granary identity and wheat belts", "Transport-conversion argument"]),
        panel("Anti-determinism firewall", "decision-tree", [
            "PHYSICAL BASE -> fertile soil + level relief + suitable climate",
            "CONVERSION AGENTS -> rail, freight, mechanisation, market demand",
            "WITHOUT ACCESS -> same soil, no granary for centuries",
            "CONCLUSION -> endowment is necessary, access is sufficient",
        ], ["Transport-conversion argument"]),
        panel("Ecological-cost chain", "hazard-flow", [
            "SOD REMOVAL -> bare fine soil exposed to wind",
            "DROUGHT YEAR -> vegetation fails, deflation peaks",
            "ORGANIC DECLINE -> reduced humus, compaction risk",
            "AQUIFER DRAWDOWN -> irrigation in semi-arid belt depletes groundwater",
        ], ["Ecological cost of ploughing"]),
        panel("India wheat granary map", "spatial-map", [
            "PUNJAB-HARYANA-WESTERN UP -> Indo-Gangetic alluvial plain",
            "SOIL -> alluvial, not chernozem (fundamental difference)",
            "SEASON -> Rabi: sown Oct-Dec, harvested Mar-Apr",
            "ENABLERS -> HYV seeds + irrigation + fertiliser + MSP procurement",
        ], ["India climate boundary", "Alluvial-chernozem distinction"]),
        panel("Green Revolution package", "institutional-ladder", [
            "HYV SEMI-DWARF WHEAT -> raised yield potential",
            "CANAL + TUBE-WELL IRRIGATION -> reduced rainfall dependence",
            "CHEMICAL FERTILISERS -> supported intensive cultivation",
            "MSP/PROCUREMENT -> assured floor price and central pool stocks",
        ], ["Green Revolution and granary conversion"]),
        panel("Savanna-steppe comparison", "comparison-table", [
            "LATITUDE -> tropical savanna versus temperate steppe/prairie",
            "RAINFALL -> wet-and-dry seasonal versus low-total spring maximum",
            "SOIL -> leached laterising versus base-rich chernozem/prairie",
            "ECONOMY -> pastoral-subsistence versus mechanised-commercial grain",
        ], ["Sustainability and savanna-steppe comparison"]),
        panel("Steppe answer spine", "answer-spine", [
            "DEFINE -> continental interior grassland with large annual range",
            "LOCATE -> five regional names on a world map",
            "EXPLAIN -> moisture deficit, chernozem, granary conversion",
            "QUALIFY -> anti-determinism: access converted endowment into resource",
        ], ["PYQ boundary and answer spine"]),
    ],
    [
        "temperate continental", "steppe", "prairie", "pampas", "veld",
        "chernozem", "black earth", "continentality", "annual range",
        "granary", "Rabi", "HYV", "MSP", "alluvial",
    ],
    (
        "The audited routing ledgers contain no direct question owned by "
        "Geography Topic 20. Steppe and granary concepts may be tested "
        "through adjacent climate-agriculture cross-owner questions, but no "
        "solved PYQ or fabricated answer key is included."
    ),
    [],
    [
        "https://www.fao.org/worldfoodsituation/csdb/en/",
        "https://fci.gov.in/",
    ],
    (
        "FAO and FCI sources are used only to establish the Black Sea "
        "breadbasket and Indian wheat procurement as live current anchors. "
        "No volatile production, export or price figure is quoted without "
        "a dated official source."
    ),
)


# ═══════════════════════════════════════════════════════════════════════════════
# TOPIC 21 — Warm Temperate Eastern Margin China Type
# Basic owner: basic/21_Warm-Temperate-Eastern-Margin-China-Type.md
# Advanced owner: advanced/21_India-Humid-Subtropical-NE.md
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_21 = common.topic(
    21,
    "Warm Temperate Eastern Margin China Type",
    "21_Warm-Temperate-Eastern-Margin-China-Type.md",
    "21_India-Humid-Subtropical-NE.md",
    "21_India-Humid-Subtropical-NE_Complete-Topic-Package.md",
    [
        ("Eastern-margin location", "The warm temperate eastern margin or China type climate is found on eastern margins of continents in warm temperate latitudes, just outside the tropics, with more rainfall than the Mediterranean climate of the same latitudes, coming mainly in summer."),
        ("Temperate monsoon identity", "It is essentially a modified or temperate form of monsoon climate, hence also called the Temperate Monsoon or China Type, driven by seasonal pressure reversal over the Asian landmass."),
        ("Three sub-types", "The three sub-types are the China type, which is the most typical temperate monsoonal form in central and north China and southern Japan; the Gulf type, a slight-monsoonal version in the south-eastern United States; and the Natal type, a non-monsoonal southern-hemisphere expression in Natal, eastern Australia and south-eastern South America."),
        ("Asiatic pressure reversal", "The huge Asiatic landmass with a mountainous interior induces great pressure changes between seasons: intense summer heating creates low pressure drawing in the tropical Pacific air stream for summer rain, while winters are cooler and drier with offshore flow."),
        ("Temperature-range variation", "The annual temperature range decreases toward the south and coast, with the source text noting about 28 degrees Fahrenheit at Canton, 27 at Swatow and only 22 at Hong Kong, illustrating the maritime-moderation gradient."),
        ("Typhoon mechanism", "Typhoons are intense tropical cyclones that originate in the Pacific Ocean and move westwards to the coasts bordering the South China Sea, most frequent in late summer July to September, and can be very disastrous."),
        ("Sub-type contrast: winter severity", "The three sub-types differ chiefly in the severity of the winter because that depends on the size of the adjoining landmass; the Asian type has the harshest winters, and the southern-hemisphere Natal types are moderated by surrounding ocean."),
        ("Summer-rain versus Mediterranean", "The eastern-margin warm temperate type has no summer drought, which is precisely what distinguishes it from the Mediterranean type at the same latitude on the western margin; the contrast is the highest-value single comparison in this part of the syllabus."),
        ("Natural vegetation and crops", "Warm wet summers support luxuriant forests, with regional examples including eucalyptus forests in NSW, sugar-cane thriving in Natal, the maize belt of the Gulf-type region, and rice and tea as characteristic crops of the monsoonal China-type lands."),
        ("Agricultural intensity", "The mechanism that makes a region agriculturally rich is the same one that makes it hazardous: the summer inflow of warm moist maritime air gives a long wet growing season supporting dense rural populations while also bringing tropical cyclones onto the same low-lying coastal plains."),
        ("India China-type analogue", "India's humid eastern margin, the Bengal-Brahmaputra plains and the North-East, is the subcontinental counterpart of the warm temperate eastern margin China type climate, with hot wet summers with heavy monsoon rain and mild winters supporting rice and tea."),
        ("Humid North-East division", "R.L. Singh's Humid North-East division includes the whole of NE India except Tripura, plus Sikkim and NW West Bengal, with average annual rainfall above 200 centimetres, mean July temperature 25 to 33 degrees Celsius and mean January temperature 10 to 25 degrees Celsius."),
        ("Bengal and Assam Plain", "Khullar's Bengal and Assam Plain region covers the entire plain of West Bengal and the Brahmaputra valley of Assam, receiving about 150 centimetres annual rainfall from the Bay of Bengal branch of the south-west monsoon, with climate classed hot sub-humid to humid to perhumid."),
        ("Rice-economy base", "Rich alluvial soils combined with heavy monsoon rainfall form a solid base for rice cultivation in the Bengal-Assam plain; the same moisture regime that sustains rice and tea also makes Assam India's most flood-prone region."),
        ("Trewartha classification", "Khullar notes that Trewartha's climatic regions of India recognise humid mesothermal and tropical-humid types plus an H or undifferentiated highland class; the NE-Bengal belt spans several classification codes depending on elevation and scheme."),
        ("Bay of Bengal branch", "The North-East's rainfall comes primarily from the Bay of Bengal branch of the south-west monsoon, not the Arabian Sea branch; this is a standard close-option discriminator."),
        ("Flood-fertility paradox", "The Brahmaputra valley's flood-fertility paradox means the same monsoon regime that sustains rice and tea also makes Assam India's most flood-prone region through intense rain, sediment-rich braided channels, bank erosion and floodplain occupation."),
        ("Tea industry link", "Assam is central to India's tea output as the world's second-largest producer; tea depends on the humid eastern-margin monsoon regime and is vulnerable to erratic rainfall, droughts and floods that threaten a key export crop and NE livelihoods."),
        ("Tripura exclusion", "R.L. Singh's Humid North-East division excludes Tripura from its coverage, which is a precise close-option distinction that has appeared in objective formats."),
        ("Transparent zero-direct route", "The audited routing ledgers contain no direct question owned by Geography Topic 21; eastern-margin climate concepts may be tested through climate-comparison or monsoon-mechanism questions but no solved PYQ is fabricated."),
    ],
    [
        "Do not reverse the rainfall regime to winter-maximum for the China type.",
        "Do not equate the China type with the Mediterranean climate.",
        "Do not call the Natal sub-type monsoonal.",
        "Do not say typhoons form near the coast.",
        "Do not treat all three sub-types as having identical winter severity.",
        "Do not claim there is a summer drought in the China type.",
        "Do not attribute NE India rainfall to the Arabian Sea branch.",
        "Do not include Tripura in R.L. Singh's Humid North-East division.",
        "Do not force the entire NE-Bengal belt into one single Koppen code.",
        "Do not separate the agricultural-richness mechanism from the hazard mechanism.",
        "Do not quote volatile cyclone statistics without a dated official source.",
        "Do not invent a direct PYQ for this topic.",
    ],
    [
        (10, "Explain why the warm temperate eastern margin receives more rainfall than the western margin at the same latitude.", "Seasonal onshore flow from a warm ocean delivers summer rain to the eastern margin, while the western margin at the same latitude is under a summer subtropical high producing drought; this is the single highest-value comparison.", [0, 7, 3]),
        (10, "Distinguish the three sub-types of the warm temperate eastern margin climate.", "The China type is the most typical temperate monsoonal form, the Gulf type is slight-monsoonal, and the Natal type is non-monsoonal; they differ chiefly in winter severity, which depends on the size of the adjoining landmass.", [2, 6, 4]),
        (15, "Analyse the dual role of the summer maritime mechanism in making eastern-margin regions both agriculturally rich and hazard-prone.", "The same summer inflow of warm moist maritime air that gives a long wet growing season supporting rice, tea and dense populations also brings typhoons, floods and surges onto the same low-lying coastal plains.", [9, 5, 8]),
        (15, "Assess India's Bengal-Brahmaputra region as a China-type climatic analogue.", "The humid eastern margin of India shares the China type's hot wet summers and mild winters supporting rice and tea, but is governed by monsoon seasonality and displays the flood-fertility paradox of the Brahmaputra valley.", [10, 12, 13, 16]),
        (20, "Compare the warm temperate eastern-margin climate with the Mediterranean climate as a test of the east-west asymmetry in the same latitude belt.", "The eastern margin receives summer rain from onshore monsoonal flow while the western margin has summer drought under a subtropical high; this contrast in rainfall regime, vegetation, agriculture and hazard exposure is the highest-value single comparison in the temperate climate sequence.", [7, 0, 3, 8]),
        (20, "Design an evidence-led strategy for managing the Brahmaputra flood-fertility paradox without destroying the rice-tea economy.", "Combine the flood-fertility paradox with monsoon science, tea-industry vulnerability and NE livelihood dependence to propose flood management that preserves alluvial fertility, using ASDMA monitoring and diversified cropping rather than complete flood exclusion.", [16, 13, 17, 14]),
    ],
    [
        plan("Eastern-margin location and rainfall contrast", [0], "This is wetter than the Mediterranean at the same latitude.", "Locate China, Gulf and Natal regions on a world map."),
        plan("Temperate monsoon identity", [1], "Do not confuse this with a true tropical monsoon.", "Explain the pressure-reversal mechanism driving the China type."),
        plan("Three sub-types", [2], "The Natal type is non-monsoonal, not monsoonal.", "Distinguish China, Gulf and Natal sub-types by mechanism and severity."),
        plan("Asiatic pressure reversal", [3], "The Asiatic landmass size drives the seasonal switch.", "Build the summer-low to winter-high pressure chain."),
        plan("Temperature range and maritime moderation", [4], "Ranges are illustrative, not universal.", "Show how proximity to the coast reduces the annual range."),
        plan("Typhoon mechanism and seasonality", [5], "Typhoons originate in the Pacific, not near the coast.", "Map origin, westward track and July-September peak."),
        plan("Sub-type winter-severity contrast", [6, 7], "Eastern-margin type has no summer drought.", "Compare winter severity across the three sub-types."),
        plan("Vegetation, crops and agricultural intensity", [8, 9], "The agricultural mechanism is also the hazard mechanism.", "Connect summer rain to rice-tea economy and typhoon exposure."),
        plan("India China-type analogue", [10], "India's humid eastern margin is not a true China-type zone.", "Preserve global Basic versus India Advanced ownership."),
        plan("Humid North-East division", [11, 18], "Tripura is excluded from R.L. Singh's division.", "Map the division boundaries precisely."),
        plan("Bengal and Assam Plain", [12, 13], "About 150 cm rain from the Bay of Bengal branch.", "Follow rainfall to alluvial soils to rice economy."),
        plan("Trewartha and classification", [14], "Do not force the NE belt into one single code.", "Note the H highland class and classification complexity."),
        plan("Bay of Bengal branch", [15], "NE rainfall is from the Bay of Bengal, not Arabian Sea.", "State the close-option discriminator explicitly."),
        plan("Flood-fertility paradox and tea", [16, 17], "Same monsoon sustains the economy and creates the hazard.", "Build the Brahmaputra flood-fertility-tea argument."),
        plan("PYQ boundary and answer spine", [19], "No direct PYQ is owned by this topic.", "Close with the transparent zero-direct-PYQ audit."),
    ],
    [
        panel("Eastern-margin world map", "spatial-map", [
            "CHINA -> central and north China + southern Japan: temperate monsoonal",
            "SE UNITED STATES -> Gulf type: slight-monsoonal, Gulf of Mexico coast",
            "NATAL + E AUSTRALIA + SE S. AMERICA -> non-monsoonal southern hemisphere",
            "WESTERN MARGIN (same latitude) -> Mediterranean: summer drought contrast",
        ], ["Eastern-margin location and rainfall contrast"]),
        panel("Pressure-reversal mechanism", "process-flow", [
            "SUMMER -> intense heating over Asian interior -> low pressure",
            "INFLOW -> tropical Pacific air stream drawn onshore -> summer rain",
            "WINTER -> cooling over continental mass -> high pressure",
            "OUTFLOW -> cold dry air moves offshore -> drier, cooler winter",
        ], ["Temperate monsoon identity", "Asiatic pressure reversal"]),
        panel("Three sub-types comparison", "comparison-table", [
            "CHINA TYPE -> temperate monsoonal, harshest winter (large Asian landmass)",
            "GULF TYPE -> slight-monsoonal, SE USA, moderate winter",
            "NATAL TYPE -> non-monsoonal, southern hemisphere, mildest winter",
            "CAUSE -> winter severity depends on size of adjoining continental mass",
        ], ["Three sub-types", "Sub-type winter-severity contrast"]),
        panel("East-west rainfall asymmetry", "comparison-table", [
            "EASTERN MARGIN -> summer rain from onshore flow, no summer drought",
            "WESTERN MARGIN -> summer drought under subtropical high, winter rain",
            "MECHANISM -> same latitude, opposite pressure-wind regime",
            "HIGHEST-VALUE COMPARISON -> in the warm temperate latitude belt",
        ], ["Eastern-margin location and rainfall contrast", "Sub-type winter-severity contrast"]),
        panel("Typhoon track map", "hazard-flow", [
            "ORIGIN -> warm western Pacific Ocean, low-latitude genesis",
            "TRACK -> westward toward South China Sea coasts",
            "SEASON -> late summer, July to September peak",
            "IMPACT -> wind, surge and flood on densely settled coastal plains",
        ], ["Typhoon mechanism and seasonality"]),
        panel("Agriculture-hazard duality", "causal-system", [
            "SUMMER INFLOW -> warm moist air gives long wet growing season",
            "RESULT -> rice, tea, sugar-cane, maize: dense rural population",
            "SAME MECHANISM -> brings typhoons, floods and surges",
            "PARADOX -> richness and hazard arise from the same maritime source",
        ], ["Vegetation, crops and agricultural intensity"]),
        panel("India humid eastern-margin map", "spatial-map", [
            "BENGAL PLAIN -> West Bengal plain, about 150 cm Bay-of-Bengal monsoon",
            "BRAHMAPUTRA VALLEY -> Assam, hot sub-humid to perhumid",
            "NE INDIA (R.L. Singh) -> NE except Tripura, Sikkim, NW W. Bengal",
            "RAINFALL -> above 200 cm in Humid NE; July 25-33 C, Jan 10-25 C",
        ], ["India China-type analogue", "Humid North-East division"]),
        panel("Monsoon-branch discriminator", "decision-tree", [
            "QUESTION: which monsoon branch serves NE India?",
            "BAY OF BENGAL BRANCH -> correct for Bengal-Brahmaputra region",
            "ARABIAN SEA BRANCH -> serves western coast, NOT NE India",
            "EXAM TRAP -> this is a standard close-option Prelims discriminator",
        ], ["Bay of Bengal branch"]),
        panel("Flood-fertility paradox", "causal-system", [
            "HEAVY MONSOON RAIN -> annual flooding of Brahmaputra floodplain",
            "POSITIVE -> alluvial fertility renews rice-tea economy each year",
            "NEGATIVE -> bank erosion, displacement, crop loss, infrastructure damage",
            "CONCLUSION -> flood management must preserve fertility, not exclude water",
        ], ["Flood-fertility paradox and tea"]),
        panel("Tea-industry vulnerability", "evidence-table", [
            "ASSAM -> central to India's tea output, world's 2nd-largest producer",
            "RISK -> erratic rainfall, drought, flood: second-flush crop losses",
            "CAUSE -> humid eastern-margin monsoon regime variability",
            "SIGNIFICANCE -> climate change links to NE livelihoods and export crop",
        ], ["Flood-fertility paradox and tea"]),
        panel("Trewartha classification note", "evidence-table", [
            "TREWARTHA -> humid mesothermal and tropical-humid types in India",
            "H CLASS -> undifferentiated highland for elevated regions",
            "NE BELT -> spans several codes depending on elevation and scheme",
            "CAUTION -> do not force entire region into one Cwg or Amw code",
        ], ["Trewartha and classification"]),
        panel("China-type answer spine", "answer-spine", [
            "DEFINE -> warm temperate eastern margin with summer-rain regime",
            "COMPARE -> east vs west margin at same latitude (highest-value contrast)",
            "EXPLAIN -> pressure reversal, sub-types, agriculture-hazard duality",
            "APPLY -> India's Bengal-NE as the China-type analogue with flood-fertility paradox",
        ], ["PYQ boundary and answer spine"]),
    ],
    [
        "temperate monsoon", "China type", "Gulf type", "Natal type",
        "typhoon", "subtropical high", "onshore flow", "summer rain",
        "Bay of Bengal branch", "Humid North-East", "Brahmaputra",
        "Trewartha", "alluvial", "rice-tea economy",
    ],
    (
        "The audited routing ledgers contain no direct question owned by "
        "Geography Topic 21. Eastern-margin and monsoon concepts may be "
        "tested through climate-comparison or tropical-cyclone questions, but "
        "no solved PYQ or fabricated answer key is included."
    ),
    [],
    [
        "https://www.jma.go.jp/jma/en/Activities/rsmc.html",
        "https://asdma.assam.gov.in/",
    ],
    (
        "JMA/RSMC and ASDMA sources are used only to establish western "
        "Pacific typhoon seasonality and Assam flood monitoring as live "
        "current anchors. No volatile cyclone track, flood extent or crop-loss "
        "figure is quoted without a dated official source."
    ),
)


# ═══════════════════════════════════════════════════════════════════════════════
# TOPIC 22 — Cool Temperate Western Margin British Type
# Basic owner: basic/22_Cool-Temperate-Western-Margin-British-Type.md
# Advanced owner: advanced/22_India-Himalayan-Temperate-Forests.md
# PYQ: 2024 Prelims Q13 routed (Marine West Coast climate)
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_22 = common.topic(
    22,
    "Cool Temperate Western Margin British Type",
    "22_Cool-Temperate-Western-Margin-British-Type.md",
    "22_India-Himalayan-Temperate-Forests.md",
    "22_India-Himalayan-Temperate-Forests_Complete-Topic-Package.md",
    [
        ("British-type location and westerlies", "The cool temperate western margins at about 45 to 65 degrees north and south are under the permanent influence of the Westerlies all year and are regions of much cyclonic activity, typical of Britain, hence the British type or North-West European Maritime Climate."),
        ("NW European distribution", "The type covers Britain inland across the lowlands of western France, Belgium, the Netherlands, Denmark and western Norway, where the absence of a major mountain barrier allows oceanic influence to penetrate far inland."),
        ("North American confinement", "In North America the Rockies block the onshore Westerlies and confine the British-type climate to the narrow coastlands of British Columbia, unlike open NW Europe where it extends far inland."),
        ("Southern hemisphere distribution", "In the Southern Hemisphere the type is found in southern Chile, Tasmania and most of the South Island of New Zealand, where narrow landmasses ensure strong maritime influence."),
        ("Maritime temperature regime", "The maritime regime gives mild winters, cool summers and a small annual temperature range, moderated by the ocean and the North Atlantic Drift, with ports remaining ice-free in winter."),
        ("Rainfall regime", "Rain falls all year with a maximum in autumn and winter, averaging about 30 inches or 750 millimetres, delivered by Westerlies, cyclonic or frontal activity and relief rainfall on windward slopes."),
        ("Deciduous forest vegetation", "Natural vegetation is deciduous forest with oak, ash, beech, elm and birch shedding their leaves in winter; this is diagnostic of the cool temperate western margin."),
        ("Dairying and mixed-farming economy", "The economy features dairying and mixed farming, temperate cereals and major fishing grounds in the cool shelf seas; the mild, reliable climate supported early industrialisation in NW Europe."),
        ("East-west asymmetry statement", "The westerlies deliver maritime air to western margins and continental air to eastern margins, so the same latitude produces a maritime climate on one side of a continent and a continental climate on the other; ocean-current direction reinforces the same contrast."),
        ("Four-type comparison", "The four cool-temperate and adjacent types are the British type with small annual range, mild winters and autumn-winter rain; the Laurentian type with large range, cold winters and summer rain; the Siberian type with very large range, bitterly cold winters and low summer rain; and the China type with large range and strong summer monsoonal rain."),
        ("Fog-and-fisheries mechanism", "Where a warm current meets a cold one off a cool-temperate eastern margin, warm moist air is chilled from below producing dense persistent fog, while mixing and nutrient supply over a broad shallow shelf sustain a major fishing ground."),
        ("Routed 2024 Prelims demand", "The 2024 Prelims GS-I Q13 tests Marine West Coast climate identified from its low annual and daily temperature range and year-round precipitation; the official Set-A key is available locally but no answer is recorded or inferred in this integration."),
        ("India climate boundary", "India has no true British-type maritime climate, but the mid-to-upper Himalayas carry the country's temperate deciduous and coniferous forest belt, the subcontinental parallel controlled by altitude rather than latitude."),
        ("Himalayan moist temperate belt", "Himalayan moist temperate forests span the western and eastern Himalayan middle elevations with oak, chestnut and mixed broadleaf-conifer species; deodar, magnolia, cedar, maple and silver-fir characterise the montane wet temperate belt from J and K to Arunachal at 1500 to 3300 metres."),
        ("Chir pine subtropical belt", "Chir pine dominates the drier subtropical montane slopes in the NW Himalaya, HP, Uttarakhand, Arunachal and NE hill slopes at 100 to 200 cm rain and 15 to 22 degrees Celsius; it is highly fire-prone because of its resinous needles."),
        ("Dry temperate forests", "Himalayan dry temperate forests occur chiefly in the inner western Himalayan ranges including Ladakh margins, Lahaul-Spiti and Kinnaur rain-shadow valleys, with deodar, chilgoza and juniper as characteristic species."),
        ("Deodar identity", "Deodar is Cedrus deodara, a conifer or cedar, not a broadleaf tree; this is a standard species-identity discriminator in Prelims."),
        ("Himalayan water-security role", "Himalayan temperate forests are vital for North India's water security: the forest-floor sponge feeds Himalayan springs and rivers, and forest loss threatens downstream water supply to the Indo-Gangetic plains."),
        ("Forest-fire risk", "Dry pre-monsoon weather, litter and fuel accumulation, ignition and resin-rich chir pine accelerate Himalayan forest-fire spread; high-elevation fires damage soil, regeneration and spring catchments."),
        ("Verified 2024 Marine West Coast route", "The routed 2024 Prelims demand tests identification of Marine West Coast or British-type climate from its low annual and daily temperature range and year-round precipitation; the local ledger supplies the demand but the official answer letter is withheld."),
    ],
    [
        "Do not give the British type a summer rainfall maximum.",
        "Do not claim a large annual temperature range for the British type.",
        "Do not extend the British type deep inland in North America.",
        "Do not call the natural vegetation coniferous.",
        "Do not confuse the British type with the Siberian type.",
        "Do not ignore the east-west asymmetry as the core causal argument.",
        "Do not assume the fog-fisheries mechanism guarantees a sustained catch.",
        "Do not label Ladakh-Kashmir as carrying subtropical montane chir forests.",
        "Do not call deodar a broadleaf tree.",
        "Do not ignore the Himalayan forest-water security nexus.",
        "Do not quote volatile fire statistics without a dated source.",
        "Do not invent an answer letter for the 2024 routed objective question.",
    ],
    [
        (10, "Explain why the cool temperate western margin has a mild maritime climate despite its high latitude.", "Permanent onshore Westerlies over a warm current, the North Atlantic Drift, and the absence of a blocking mountain barrier deliver mild winters, cool summers and year-round rain.", [0, 4, 5]),
        (10, "Explain why the British-type climate extends far inland in NW Europe but is confined to a narrow coastal strip in North America.", "In NW Europe the lowlands allow oceanic influence to penetrate unblocked, while in North America the Rockies block the onshore Westerlies and confine the type to the British Columbia coast.", [1, 2, 3]),
        (15, "Compare the British type and the Laurentian type as the western and eastern expressions of the cool temperate belt.", "The Westerlies deliver maritime air to western margins giving mild winters and year-round rain, and continental air to eastern margins giving cold winters and summer rain; ocean-current direction reinforces this asymmetry.", [8, 9, 10]),
        (15, "Assess India's Himalayan temperate forests as the subcontinental parallel of the cool temperate western-margin biome.", "India has no true British-type maritime climate, but the mid-to-upper Himalayas carry a temperate deciduous-coniferous belt controlled by altitude rather than latitude, with deodar, oak, chir pine and dry-temperate species in distinct belts.", [12, 13, 14, 15]),
        (20, "Analyse the east-west climatic asymmetry in the cool temperate belt and its consequences for economy and settlement.", "The westerly-oceanic mechanism produces a maritime dairying economy with ice-free ports on western margins and a continental forestry-fishery economy on eastern margins; the fog-fisheries mechanism and the comparison of all four types demonstrate the asymmetry.", [8, 9, 10, 7]),
        (20, "Design an evidence-led strategy for protecting Himalayan temperate forests to safeguard North India's water security.", "Combine altitudinal forest zonation, the forest-floor sponge role, chir-pine fire risk, spring-catchment degradation and climate change to propose integrated fire management, oak-broadleaf restoration and regulated land use.", [17, 18, 13, 16]),
    ],
    [
        plan("British-type location and Westerlies", [0], "This is a western-margin type, not an interior type.", "Locate NW Europe, BC and southern hemisphere at 45-65 degrees."),
        plan("NW European distribution", [1], "No mountain barrier allows inland penetration.", "Map Britain, France, Belgium, Netherlands, Denmark, Norway."),
        plan("North American confinement", [2], "Rockies block the onshore Westerlies.", "Contrast the narrow BC strip with open NW Europe."),
        plan("Southern hemisphere distribution", [3], "Narrow landmasses ensure maritime influence.", "Locate S. Chile, Tasmania and NZ South Island."),
        plan("Maritime temperature regime", [4], "Small annual range, not large.", "Explain the ocean-NAD moderation mechanism."),
        plan("Rainfall regime", [5], "Rain all year, max in autumn-winter, not summer.", "Distinguish frontal, cyclonic and relief rainfall."),
        plan("Deciduous forest vegetation", [6], "Deciduous, not coniferous.", "List oak, ash, beech, elm, birch as diagnostic species."),
        plan("Dairying and early industrialisation", [7], "Mildness and reliability, not warmth, are the operative variables.", "Connect climate to dairying, ports and industry."),
        plan("East-west asymmetry", [8, 9], "Do not describe features without causal comparison.", "State the single-sentence asymmetry argument."),
        plan("Fog-and-fisheries mechanism", [10, 11], "Fishery productivity depends on exploitation levels too.", "Connect warm-cold current meeting to fog and fishing grounds."),
        plan("India temperate boundary", [12], "India has no true British-type maritime climate.", "Preserve global Basic versus India Advanced ownership."),
        plan("Himalayan forest belts", [13, 14], "Altitudinal zonation replaces latitudinal zonation.", "Map moist temperate, chir pine and dry temperate belts."),
        plan("Dry temperate and deodar identity", [15, 16], "Deodar is a conifer, not broadleaf.", "Locate rain-shadow dry temperate forests."),
        plan("Water security and fire risk", [17, 18], "Forest loss threatens downstream water supply.", "Build the sponge-spring-river-fire argument chain."),
        plan("Routed 2024 PYQ and answer spine", [19], "The ledger supplies demand but no answer letter.", "Close with the Marine West Coast elimination logic."),
    ],
    [
        panel("British-type world map", "spatial-map", [
            "NW EUROPE -> Britain, France, Belgium, Netherlands, Denmark, Norway",
            "NORTH AMERICA -> British Columbia coast (Rockies block inland)",
            "SOUTHERN HEMISPHERE -> S. Chile, Tasmania, NZ South Island",
            "LATITUDE BELT -> about 45-65 degrees N and S",
        ], ["British-type location and Westerlies"]),
        panel("Westerly-ocean mechanism", "process-flow", [
            "WESTERLIES -> permanent onshore flow from warm ocean",
            "NORTH ATLANTIC DRIFT -> warm current on seaward side",
            "CYCLONIC ACTIVITY -> travelling frontal depressions",
            "RESULT -> mild winters, cool summers, small annual range, rain all year",
        ], ["Maritime temperature regime", "Rainfall regime"]),
        panel("Rockies-barrier contrast", "comparison-table", [
            "NW EUROPE -> no major barrier, oceanic influence far inland",
            "NORTH AMERICA -> Rockies block Westerlies, narrow BC coastal strip",
            "SOUTHERN HEMISPHERE -> narrow landmasses, strong maritime influence",
            "CAUSE -> mountain barriers and land width determine inland reach",
        ], ["NW European distribution", "North American confinement"]),
        panel("East-west asymmetry diagram", "comparison-table", [
            "WESTERN MARGIN -> onshore Westerlies, warm current, mild/small range",
            "EASTERN MARGIN -> offshore Westerlies, cold current, cold/large range",
            "WESTERN RAIN -> all year, autumn-winter max, frontal depressions",
            "EASTERN RAIN -> summer max, winter snow, ports freeze",
        ], ["East-west asymmetry"]),
        panel("Four-type comparison matrix", "comparison-table", [
            "BRITISH -> mild winter, cool summer, small range, all-year rain",
            "LAURENTIAN -> cold winter, warm summer, large range, summer rain",
            "SIBERIAN -> bitterly cold winter, short summer, very large range",
            "CHINA TYPE -> cool-cold winter, hot summer, large range, monsoon rain",
        ], ["East-west asymmetry"]),
        panel("Fog-fisheries mechanism", "causal-system", [
            "WARM CURRENT meets COLD CURRENT -> air chilled from below",
            "RESULT -> dense persistent fog (navigation hazard)",
            "MIXING + NUTRIENT SUPPLY -> over broad shallow continental shelf",
            "RESULT -> major fishing ground (but productivity depends on catch levels)",
        ], ["Fog-and-fisheries mechanism"]),
        panel("Deciduous-vegetation identity", "classification-tree", [
            "BRITISH TYPE -> deciduous: oak, ash, beech, elm, birch",
            "LAURENTIAN -> mixed and coniferous forest",
            "SIBERIAN -> taiga (boreal coniferous)",
            "EXAM TRAP -> British type is deciduous, NOT coniferous",
        ], ["Deciduous forest vegetation"]),
        panel("Maritime economy", "institutional-ladder", [
            "DAIRYING + MIXED FARMING -> long grass-growing season, reliable moisture",
            "ICE-FREE PORTS -> year-round trade and shipping",
            "TEMPERATE CEREALS -> reliable growing conditions",
            "EARLY INDUSTRIALISATION -> ports, water, equable climate in NW Europe",
        ], ["Dairying and early industrialisation"]),
        panel("India Himalayan temperate map", "spatial-map", [
            "MOIST TEMPERATE -> J&K to Arunachal, 1500-3300 m: deodar, oak, fir",
            "CHIR PINE BELT -> NW Himalaya, HP, Uttarakhand, NE: fire-prone",
            "DRY TEMPERATE -> Ladakh margins, Lahaul-Spiti, Kinnaur: chilgoza, juniper",
            "CONTROL -> altitude replaces latitude as the zonation driver",
        ], ["India temperate boundary", "Himalayan forest belts"]),
        panel("Deodar species firewall", "evidence-table", [
            "DEODAR -> Cedrus deodara, a CONIFER (cedar family)",
            "EXAM TRAP -> frequently tested: deodar is NOT a broadleaf tree",
            "CHILGOZA -> dry-temperate conifer (Pinus gerardiana)",
            "CHIR PINE -> subtropical montane, highly resinous and fire-prone",
        ], ["Dry temperate and deodar identity"]),
        panel("Water-security-fire chain", "hazard-flow", [
            "FOREST FLOOR SPONGE -> absorbs rain, feeds springs and rivers",
            "FOREST LOSS -> reduced infiltration, spring decline, downstream shortage",
            "CHIR PINE + DRY WEATHER -> fuel accumulation, rapid fire spread",
            "FIRE DAMAGE -> soil loss, regeneration failure, catchment degradation",
        ], ["Water security and fire risk"]),
        panel("British-type answer spine", "answer-spine", [
            "DEFINE -> cool temperate western margin under permanent Westerlies",
            "COMPARE -> east-west asymmetry: same latitude, opposite climate",
            "EXPLAIN -> maritime moderation, frontal rain, deciduous vegetation",
            "APPLY -> India's Himalayan temperate forests as altitude-based analogue",
        ], ["Routed 2024 PYQ and answer spine"]),
    ],
    [
        "Westerlies", "cyclonic activity", "North Atlantic Drift", "British type",
        "Marine West Coast", "maritime", "deciduous", "oak", "deodar",
        "Cedrus deodara", "chir pine", "chilgoza", "montane wet temperate",
        "altitudinal zonation",
    ],
    (
        "The audited 2024-2025 routing ledger routes Prelims 2024 GS-I Q13 "
        "(Marine West Coast climate) to this owner. The official Set-A key is "
        "available locally but no answer is recorded or inferred. The package "
        "teaches the low annual and daily temperature range and year-round "
        "precipitation features that satisfy this demand."
    ),
    [
        ("2024", "Prelims GS-I", "Marine West Coast climate identified from its low annual and daily temperature range and year-round precipitation", "Routed demand; official Set-A key available locally; answer not recorded or inferred", "The Marine West Coast or British-type climate is characterised by a low annual temperature range, a low daily temperature range and year-round precipitation, driven by permanent onshore Westerlies over a warm current. The package teaches this identity through the maritime-moderation mechanism and the east-west asymmetry comparison."),
    ],
    [
        "https://climate.copernicus.eu/european-state-climate",
        "https://fsi.nic.in/",
    ],
    (
        "Copernicus European State of the Climate reports and FSI fire data "
        "are used only to establish European maritime climate change and "
        "Himalayan forest-fire risk as live current anchors. No volatile "
        "temperature, fire or flood statistic is quoted without a dated "
        "official source."
    ),
)
