"""Authored Geography learner-v2 data for Part B Topics 31 and 33-37."""

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


TOPIC_31 = common.topic(
    31,
    "Mineral and Energy Resources: World and India",
    "31_Mineral-Energy-Resources-World-and-India.md",
    "31_Mineral-Energy-Resources-World-and-India.md",
    "31_Mineral-Energy-Resources-World-and-India_Complete-Topic-Package.md",
    [
        (
            "Geological control of distribution",
            "Mineral and energy resources are unevenly distributed because occurrence depends on geological history, rock structure, sedimentary basins, tectonics and climate-driven surface processes.",
        ),
        (
            "Mineral classification ladder",
            "Economic geography classifies minerals as ferrous metallic, non-ferrous metallic, non-metallic industrial and mineral fuels, so coal and petroleum are mineral resources and not merely fuels.",
        ),
        (
            "Energy classification pairs",
            "Energy resources are classified twice over: conventional commercial against non-conventional newer sources, and exhaustible stock against renewable flow.",
        ),
        (
            "Shield and basin rule",
            "Shield and igneous-metamorphic terrain is associated with metallic ores, while sedimentary basins hold coal, petroleum and natural gas.",
        ),
        (
            "Lateritisation and bauxite",
            "Tropical weathering and lateritisation concentrate bauxite on suitable plateaux and hilltops, so the bauxite map does not simply repeat the shield-ore map.",
        ),
        (
            "World mineral-energy belts",
            "The standard world belts are the Persian Gulf hydrocarbon province, the Appalachian and interior United States belts, the Ruhr-Lorraine coal-iron core, the Russian and Siberian basins, the Chinese northern and interior coal belts, the African Copperbelt and South African shield, the Australian shield and basins, and the Andean and Latin American shield zones.",
        ),
        (
            "Extraction to industry chain",
            "Minerals matter along a chain of extraction, transport, processing, power supply and industrial clustering, so a mine site alone does not create an industrial region.",
        ),
        (
            "Occurrence versus usable resource",
            "Geology fixes occurrence only; grade, depth, transport distance, technology and price decide whether an occurrence becomes a usable resource at all.",
        ),
        (
            "Four-element petroleum system",
            "Oil and gas require source rock, reservoir rock, an impermeable seal and a trap geometry together, so a sedimentary basin is necessary but not sufficient for petroleum.",
        ),
        (
            "Why margins concentrate oil",
            "Continental shelves and slopes act as great sediment sinks, oxygen-poor marine bottom water preserves organic matter, and passive margins accumulate thick undisturbed sediment prisms with deltaic and salt-tectonic traps.",
        ),
        (
            "Offshore versus onshore regime",
            "Offshore petroleum needs very high lumpy capital and large fields, works through platforms, subsea pipelines and coastal landfall terminals, and carries marine spill risk and maritime jurisdictional questions that onshore fields do not.",
        ),
        (
            "Indian petroleum provinces",
            "India combines onshore Assam-Arakan and Cambay basins with a major western offshore province and east-coast deltaic offshore gas in the Krishna-Godavari and Cauvery margins.",
        ),
        (
            "Midstream critical-mineral chokepoint",
            "For transition minerals the processing and refining stage is even more geographically concentrated than extraction and often sits in different countries, so the binding chokepoint is midstream rather than at the mine.",
        ),
        (
            "Critical-mineral response levers",
            "Recycling, substitution, supply diversification and strategic stockpiling are the principal long-term levers available to resource-poor consuming economies.",
        ),
        (
            "Chota Nagpur mineral heartland",
            "Khullar treats the Chota Nagpur Plateau complex and the wider peninsular shield as India's classic mineral heartland and heavy-industry base.",
        ),
        (
            "Indian belt map hooks",
            "Iron ore belongs to Odisha-Jharkhand, Bailadila and Ballari-Hospet; Gondwana coal to the Damodar, Mahanadi, Son and Godavari valley basins; copper to Khetri, Singhbhum and Malanjkhand; and lead-zinc to Zawar and Rampura-Agucha.",
        ),
        (
            "Coal and the east-central pull",
            "Coalfields of the Damodar valley and the adjoining eastern belt pulled steel plants, thermal power and rail-linked heavy industry into east-central India.",
        ),
        (
            "Renewable corridor shift",
            "Solar capacity concentrates in the dry high-insolation belts of Rajasthan and Gujarat while wind concentrates along Tamil Nadu, Gujarat, Karnataka and Maharashtra coasts and passes, so the renewable map does not mirror the coal map.",
        ),
        (
            "Institutional conversion ladder",
            "The Ministry of Mines, Geological Survey of India, Indian Bureau of Mines, Ministry of Coal, Ministry of Power with the Central Electricity Authority, and NPCIL convert geological occurrence into extractive, power and siting geography.",
        ),
        (
            "National Critical Mineral Mission anchor",
            "The Union Cabinet approved the National Critical Mineral Mission on 29 January 2025 with a total envisaged outlay of Rs 34,300 crore over seven years including Rs 16,300 crore of government expenditure, covering exploration, mining, beneficiation, processing, recovery and recycling.",
        ),
    ],
    [
        "Do not treat mineral resource as a synonym for metal; coal and petroleum are mineral resources too.",
        "Do not call hydropower a mineral resource; it is an energy resource without a mineral stock.",
        "Do not claim minerals become renewable because they can be recycled.",
        "Do not assume that an oilfield and its refinery must occupy the same location.",
        "Do not answer an oil question with sedimentary basins alone; name the four-element petroleum system.",
        "Do not treat a mineral-producing region as automatically an industrial region.",
        "Do not place India's mineral core in the Indo-Gangetic plain instead of the peninsular shield.",
        "Do not give hydrocarbons the same shield-core geography as iron-ore belts.",
        "Do not swap the commodity identities of Bailadila, Jharia, Khetri, Zawar and the western offshore province.",
        "Do not quote country percentage shares, reserve totals or import-dependence ratios from memory.",
        "Do not treat installed capacity as if it were annual generation.",
        "Do not argue that renewable growth has already made coal irrelevant to dispatchable power.",
        "Do not convert an unkeyed routed Prelims question into a solved answer with an invented key.",
        "Do not describe offshore development as simply onshore petroleum placed under water.",
    ],
    [
        (
            10,
            "Explain why the world distribution of mineral and energy resources is better treated as a deduction from Earth history than as a list of producing countries.",
            "Distribution follows geological history because shields concentrate metallic ores, sedimentary basins hold fuels and lateritic weathering profiles concentrate bauxite, while accessibility and economics decide which occurrences become usable resources.",
            [0, 3, 4, 7],
        ),
        (
            10,
            "Distinguish mineral-resource geography from energy geography with suitable Indian examples.",
            "Mineral geography asks where ores and industrial minerals occur, while energy geography asks where usable power can be produced, so India's shield-based ore belts and its solar and wind corridors do not overlap.",
            [1, 2, 17],
        ),
        (
            15,
            "Explain the distribution of offshore petroleum reserves and how it differs from onshore occurrence.",
            "Offshore petroleum reflects a distinct depositional and tectonic setting on thick passive-margin sediment prisms, and it imposes a different capital, technological, environmental and jurisdictional regime rather than being onshore petroleum placed under water.",
            [8, 9, 10, 11],
        ),
        (
            15,
            "Examine why India's mineral-industrial geography still carries the imprint of the peninsular shield.",
            "The peninsular shield and its Gondwana basins supplied the ore and coal combinations around which steel, thermal power and rail-linked industry clustered, so the historic mineral heartland continues to shape industrial location.",
            [5, 14, 15, 16],
        ),
        (
            20,
            "In the energy transition, is the critical-mineral constraint located at the mine or in the midstream? Analyse.",
            "Extraction is geologically concentrated, but processing and refining are more concentrated still and often located elsewhere, so supply security depends on midstream capacity, recycling and substitution rather than on mine ownership alone.",
            [7, 12, 13, 19],
        ),
        (
            20,
            "Assess how far renewable-energy corridors are overlaying, rather than replacing, India's coal-centred energy geography.",
            "Renewable corridors are creating a new western and southern energy map while coal-linked east-central geography still anchors dispatchable power and freight-dependent heavy industry, so the correct verdict is overlay with partial substitution.",
            [16, 17, 18, 19],
        ),
    ],
    [
        plan(
            "Why resource geography begins with geology",
            [0, 3],
            "Distribution is a geological outcome, not a policy accident.",
            "Open with the geological control before naming any belt or country.",
        ),
        plan(
            "Classifying minerals and energy resources",
            [1, 2],
            "Mineral fuels sit inside the mineral class, not outside it.",
            "Use the four-fold mineral ladder and the two energy pairs as the opening classification.",
        ),
        plan(
            "Weathering, lateritisation and bauxite geography",
            [4],
            "Bauxite follows weathering profiles, not shield cores alone.",
            "Explain bauxite through climate-driven surface processes rather than ore-belt lists.",
        ),
        plan(
            "World mineral-energy belts",
            [5],
            "Name belts as geological provinces, not as national brands.",
            "Group the world belts by shield, basin and coal-iron combination logic.",
        ),
        plan(
            "From mine to industry: the resource chain",
            [6],
            "A mine is one node in a longer chain.",
            "Move from extraction through transport and power to industrial clustering.",
        ),
        plan(
            "Occurrence versus usable resource",
            [7],
            "Geology fixes occurrence; economics fixes usability.",
            "Add the grade, depth, distance, technology and price filter to every distribution claim.",
        ),
        plan(
            "The four-element petroleum system",
            [8],
            "A sedimentary basin alone does not guarantee petroleum.",
            "State source, reservoir, seal and trap together before locating any oil province.",
        ),
        plan(
            "Why passive margins concentrate offshore oil",
            [9],
            "Marine preservation and thick prisms explain margins, not luck.",
            "Explain sediment sinks, organic preservation and salt or deltaic traps in sequence.",
        ),
        plan(
            "Offshore versus onshore as economic geography",
            [10],
            "The contrast is a trade-off in kind, not a simple ranking.",
            "Compare by axis: cost, field-size threshold, infrastructure, risk and jurisdiction.",
        ),
        plan(
            "India's petroleum provinces",
            [11],
            "Keep carbonate western offshore and deltaic east-coast gas distinct.",
            "Name onshore and offshore provinces without attaching remembered output figures.",
        ),
        plan(
            "Critical minerals and the midstream chokepoint",
            [12, 13],
            "The chokepoint is midstream, so mine ownership is not the whole answer.",
            "Separate extraction concentration from processing concentration, then add the response levers.",
        ),
        plan(
            "Chota Nagpur and the peninsular mineral heartland",
            [14],
            "India's mineral core lies in the peninsular shield, not the plains.",
            "Anchor India's mineral answer in the shield and its Gondwana basins.",
        ),
        plan(
            "Indian belt map hooks for Prelims",
            [15],
            "Do not swap commodity identities between named belts.",
            "Fix one commodity to one belt and rehearse the pairing before the exam.",
        ),
        plan(
            "Coal, power and the east-central industrial pull",
            [16],
            "Coal geography explains industrial location, not only fuel supply.",
            "Link coalfields to steel, thermal power and freight corridors in one causal line.",
        ),
        plan(
            "Renewable corridors, institutions and the critical-mineral mission",
            [17, 18, 19],
            "Installed capacity and generation are different measures.",
            "Close with overlay logic: new corridors, converting institutions and a dated mission anchor.",
        ),
    ],
    [
        panel(
            "Geological control of resource distribution",
            "causal-system",
            [
                "GEOLOGICAL HISTORY -> rock structure, basins, tectonics, surface weathering",
                "SHIELD / IGNEOUS-METAMORPHIC TERRAIN -> metallic ores",
                "SEDIMENTARY BASIN -> coal, petroleum, natural gas",
                "TROPICAL LATERITISATION -> bauxite on suitable plateaux and hilltops",
                "TRAP -> distribution is a deduction from Earth history, not a country list",
            ],
            ["Geological control of distribution", "Shield and basin rule", "Lateritisation and bauxite"],
        ),
        panel(
            "Mineral and energy classification ladder",
            "comparison-table",
            [
                "FERROUS METALLIC -> iron ore, manganese, chromite; steel-making base",
                "NON-FERROUS METALLIC -> copper, bauxite, lead, zinc",
                "NON-METALLIC INDUSTRIAL -> mica, limestone, gypsum, phosphates",
                "MINERAL FUELS -> coal, petroleum, natural gas, uranium",
                "ENERGY PAIRS -> conventional vs non-conventional; exhaustible stock vs renewable flow",
            ],
            ["Mineral classification ladder", "Energy classification pairs"],
        ),
        panel(
            "World mineral-energy belt rail",
            "institutional-ladder",
            [
                "PERSIAN GULF -> classic sedimentary hydrocarbon province",
                "APPALACHIAN / INTERIOR USA -> coal, oil, gas with iron associations",
                "RUHR-LORRAINE -> historic coal-iron heavy-industry core",
                "RUSSIAN-SIBERIAN / CHINESE INTERIOR -> continental-scale fuel frontiers",
                "COPPERBELT, AUSTRALIAN SHIELD, ANDES -> shield and tectonic metal provinces",
            ],
            ["World mineral-energy belts", "Shield and basin rule"],
        ),
        panel(
            "Extraction to industry chain",
            "process-flow",
            [
                "EXTRACTION -> ore or fuel raised at the deposit",
                "TRANSPORT -> rail, slurry pipeline, port or inland waterway evacuation",
                "PROCESSING -> beneficiation, smelting, refining, petrochemical conversion",
                "POWER + MARKET -> dispatchable energy, capital and demand complete the cluster",
                "RULE -> a producing region is not automatically an industrial region",
            ],
            ["Extraction to industry chain", "Occurrence versus usable resource"],
        ),
        panel(
            "Occurrence to usable resource filter",
            "decision-tree",
            [
                "OCCURRENCE EXISTS -> geology has done its part",
                "IF grade and depth are workable -> continue to the economic test",
                "IF transport distance and technology permit -> continue to the price test",
                "IF price sustains the cost -> occurrence becomes a usable resource",
                "ELSE -> the deposit stays a geological fact with no economic geography",
            ],
            ["Occurrence versus usable resource", "Extraction to industry chain"],
        ),
        panel(
            "Four-element petroleum system",
            "process-flow",
            [
                "SOURCE ROCK -> organic-rich fine sediment buried deeply and long enough",
                "RESERVOIR ROCK -> porous permeable sandstone or fractured carbonate",
                "SEAL / CAP ROCK -> shale, evaporite or tight limestone preventing escape",
                "TRAP -> anticline, fault block, salt dome, reef or stratigraphic pinch-out",
                "VERDICT -> sedimentary basin is necessary but never sufficient",
            ],
            ["Four-element petroleum system", "Why margins concentrate oil"],
        ),
        panel(
            "Why passive margins hold offshore oil",
            "causal-system",
            [
                "SHELF AND SLOPE -> the world's great sediment sinks receive river-borne organic load",
                "OXYGEN-POOR BOTTOM WATER -> marine settings preserve organic matter from decay",
                "PASSIVE MARGIN SUBSIDENCE -> thick, tectonically quiet sediment prisms accumulate",
                "DELTAS AND SALT TECTONICS -> pair source with reservoir and generate trap families",
                "PRESERVATION EDGE -> uplift and erosion have breached many onshore accumulations",
            ],
            ["Why margins concentrate oil", "Four-element petroleum system"],
        ),
        panel(
            "Offshore versus onshore comparison",
            "comparison-table",
            [
                "GEOLOGY -> onshore intracratonic and rift basins vs shelf, slope and deepwater margin",
                "COST AND TECHNOLOGY -> incremental land drilling vs lumpy high-cost marine systems",
                "THRESHOLD -> small onshore fields can be viable; offshore needs large fields",
                "FOOTPRINT -> land acquisition onshore vs fisheries, shipping and spill risk offshore",
                "JURISDICTION -> ordinary national law vs maritime zones and contested boundaries",
            ],
            ["Offshore versus onshore regime", "Indian petroleum provinces"],
        ),
        panel(
            "India petroleum province map hooks",
            "comparison-table",
            [
                "ONSHORE -> Assam-Arakan basin and the Cambay basin of western India",
                "WESTERN OFFSHORE -> major continental-margin province, carbonate reservoir character",
                "EAST-COAST OFFSHORE -> Krishna-Godavari and Cauvery deltaic margins, gas-prone",
                "COASTAL CONSEQUENCE -> landfall terminals pull refining and petrochemicals to the coast",
                "CAUTION -> name provinces and reservoir character, never remembered output figures",
            ],
            ["Indian petroleum provinces", "Offshore versus onshore regime"],
        ),
        panel(
            "Critical-mineral chokepoint fork",
            "decision-tree",
            [
                "TRANSITION DEMAND RISES -> lithium, cobalt, nickel, graphite, copper, rare earths",
                "IF the question is extraction -> supply is geologically narrow but visible",
                "IF the question is processing -> concentration is tighter and often in other countries",
                "THEREFORE -> the binding chokepoint is midstream, not at the mine",
                "RESPONSE -> recycling, substitution, diversification and strategic stockpiling",
            ],
            ["Midstream critical-mineral chokepoint", "Critical-mineral response levers"],
        ),
        panel(
            "India mineral belt and energy corridor rail",
            "institutional-ladder",
            [
                "CHOTA NAGPUR COMPLEX -> iron ore, coal, mica, bauxite, manganese heartland",
                "BELT HOOKS -> Bailadila iron, Jharia coking coal, Khetri copper, Zawar lead-zinc",
                "GONDWANA COAL -> Damodar, Mahanadi, Son and Godavari valley basins",
                "SOLAR CORRIDOR -> Rajasthan and Gujarat dry high-insolation belts",
                "WIND CORRIDOR -> Tamil Nadu, Gujarat, Karnataka and Maharashtra coasts and passes",
            ],
            ["Chota Nagpur mineral heartland", "Indian belt map hooks", "Coal and the east-central pull", "Renewable corridor shift"],
        ),
        panel(
            "Mineral and energy answer spine",
            "answer-spine",
            [
                "DEFINE -> which class of resource and which measure is being asked about",
                "DEDUCE -> shield, basin or weathering control before naming any place",
                "LOCATE -> world belt, then the Indian belt or petroleum province",
                "QUALIFY -> occurrence versus usable resource; capacity versus generation",
                "CLOSE -> midstream chokepoint, institutional conversion and the dated mission anchor",
            ],
            ["Occurrence versus usable resource", "Institutional conversion ladder", "National Critical Mineral Mission anchor"],
        ),
    ],
    [
        "sedimentary basin",
        "shield",
        "bauxite",
        "Chota Nagpur",
        "Bailadila",
        "Khetri",
        "Zawar",
        "Krishna-Godavari",
        "National Critical Mineral Mission",
        "midstream",
    ],
    (
        "Geography Topic 31 owns direct Mains PYQ demand in the audited routing ledgers. "
        "Five GS-I demands are routed to this owner: 2018 Q5, 2021 Q5, 2021 Q16, 2022 Q6 and 2025 Q14. "
        "Each is answered below as an original model solution built only from the owner evidence. "
        "The routed Prelims demands for this topic are recorded in the owner ledgers as objective "
        "questions whose official keys are either unavailable locally or deliberately not inferred, "
        "so no option letter, answer key or invented question wording is reproduced here."
    ),
    [
        (
            "2018",
            "GS-I Q5 (Why, 10 marks, 150 words)",
            "Explain why India has an interest in the resources of the Arctic region.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. The wording is the ledger's neutral rendering, not a reproduced official paper text.",
            "Frame the Arctic as a high-latitude resource frontier whose hydrocarbon potential rests on sedimentary basins and continental-margin geology, exactly the shield-versus-basin logic that governs resource distribution everywhere. India's interest follows the same chain that this owner sets out: occurrence must be converted into usable resource through transport, processing and power, so the Arctic matters for prospective fuel and mineral access, for shipping routes that shorten the distance filter, and for scientific presence that supports exploration capability. Qualify the answer twice: occurrence is not usability, since grade, depth, distance, technology and price still decide viability; and no reserve, share or output figure should be quoted, because the owner explicitly forbids remembered figures. Conclude that the interest is strategic and anticipatory rather than an established production relationship.",
        ),
        (
            "2021",
            "GS-I Q5 (Discuss, 10 marks, 150 words)",
            "Discuss why India's Gondwanaland mineral base has not translated into a large share of mining in the national economy.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. Only the ledger's neutral rendering is used.",
            "Open with the endowment: Gondwana sequences in the Damodar, Mahanadi, Son and Godavari valley basins, set within the peninsular shield that Khullar treats as India's mineral heartland, give India a genuinely strong bulk-mineral base. Then apply this owner's central distinction between occurrence and usable resource. Endowment alone is inert: grade, depth, transport distance, technology and price stand between a deposit and an economically significant industry, and the chain from extraction through transport, processing and power to industrial clustering has to be completed before value is captured. East-central abundance therefore raises a logistics question of rail evacuation, slurry pipelines, port linkage and power availability rather than an automatic economic dividend, and bulk-mineral strength does not by itself create high-end processing strength. Qualify by refusing any GDP-share, production or reserve figure from memory, and conclude that the low economic share reflects an unconverted chain rather than a poor endowment.",
        ),
        (
            "2021",
            "GS-I Q16 (Discuss, 15 marks, 250 words)",
            "Discuss the uneven distribution of mineral oil in the world.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. No official answer key exists for a Mains question, and none is implied.",
            "Thesis: mineral oil is unevenly distributed because it requires a rare coincidence of geological conditions, not because it is randomly scattered. Establish the four-element petroleum system first, since source rock, reservoir rock, seal and trap must occur together, which makes a sedimentary basin necessary but never sufficient. Explain next why particular settings satisfy all four conditions: continental shelves and slopes act as great sediment sinks, oxygen-poor marine bottom water preserves organic matter, passive margins subside steadily and accumulate thick undisturbed prisms, deltas deliver source and reservoir facies together, and salt tectonics generates both traps and seals. Then locate the pattern: the Persian Gulf as the classic sedimentary hydrocarbon province, the Russian and Siberian basins as a continental-scale frontier, the interior United States belts, and India's own combination of Assam-Arakan and Cambay onshore basins with a western offshore province and Krishna-Godavari and Cauvery deltaic gas. Add the second filter: uplift, erosion and faulting have breached many onshore accumulations, so preservation as well as formation shapes the map. Qualify by separating occurrence from usable resource and by refusing reserve or production percentages from memory. Conclude that the world oil map is a preserved record of basin evolution read through an economic filter.",
        ),
        (
            "2022",
            "GS-I Q6 (Discuss, 10 marks, 150 words)",
            "Discuss the natural resource potentials of the Deccan Trap region.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. The rendering is the ledger's neutral phrasing.",
            "Treat the Deccan Trap as a case of this owner's central rule that resource potential is deduced from geological and weathering history. As a vast basaltic province it does not carry shield-core metallic ore belts or thick hydrocarbon-bearing sedimentary sequences; its potential is instead of the kinds that basalt and its weathering profile generate. Tropical weathering and lateritisation on basaltic terrain concentrate bauxite on suitable plateaux and hilltops, and the same weathering produces deep regur soils that convert the region into an agricultural rather than a metallurgical resource base. Basalt also yields large-volume building and industrial stone, while jointed and fractured flows govern the groundwater question. Qualify sharply: do not attribute coal, petroleum or shield-type metallic ore belts to the traps, and do not attach reserve or production figures from memory. Conclude that the Deccan Trap's potential is weathering-derived and surface-linked, which is precisely why it must not be read through the Chota Nagpur template.",
        ),
        (
            "2025",
            "GS-I Q14 (Explain, 15 marks, 250 words)",
            "Explain the distribution of offshore oil reserves and how it differs from onshore occurrence.",
            "Verified routed demand from the audited Mains routing ledger for 2024-2025, routed to this owner as the owning topic. The owner file itself flags the demand and supplies the geological and economic logic.",
            "Thesis: offshore petroleum is not onshore petroleum placed under water; it reflects a different depositional and tectonic setting and imposes a different economic, environmental and jurisdictional regime. Begin with the common requirement, the four-element petroleum system of source, reservoir, seal and trap, which applies identically in both settings. Then explain why submerged margins are favoured: shelves and slopes are the world's great sediment sinks, marine bottom water preserves organic matter, passive margins subside quietly and build thick prisms, deltas pair source with reservoir under rapid burial and growth faulting, salt tectonics supplies traps and seals, and offshore sections escape the uplift and erosion that have breached many onshore accumulations. Next compare by axis rather than by location: geological setting, exploration method, capital and technology intensity, the field-size threshold that governs viability, infrastructure from platforms and subsea lines to coastal landfall terminals, land acquisition against fisheries and shipping conflict, contamination against marine spill risk, hazard exposure, jurisdictional regime and decommissioning obligation. Illustrate with India's own expression: Assam-Arakan and Cambay onshore against a carbonate-dominated western offshore province and deltaic Krishna-Godavari and Cauvery gas, with landfall pulling refining and petrochemicals to the coast. Qualify with the maritime-zone dimension and refuse remembered figures. Conclude with a graded verdict: offshore raises capital and marine environmental stakes while reducing land and displacement burden, so the two are a trade-off in kind rather than a ranking.",
        ),
    ],
    [
        "https://mines.gov.in/",
        "https://coal.nic.in/",
        "https://cea.nic.in/",
        "https://pib.gov.in/",
    ],
    (
        "The only dated current anchor used is the Union Cabinet approval of the National Critical "
        "Mineral Mission on 29 January 2025, with a total envisaged outlay of Rs 34,300 crore over "
        "seven years including Rs 16,300 crore of government expenditure, as recorded in the owner "
        "file and confirmed against the official Ministry of Mines and Press Information Bureau "
        "release. Central Electricity Authority capacity publications are named only as the correct "
        "source class for power-capacity geography. No reserve total, production ranking, country "
        "share, import-dependence ratio, installed-capacity figure or generation figure is quoted "
        "from memory, and installed capacity is never presented as generation."
    ),
)

TOPIC_33 = common.topic(
    33,
    "Transport, Trade and the Indian Space Programme",
    "33_Transport-Trade-and-Indian-Space-Programme.md",
    "33_Transport-Trade-and-Indian-Space-Programme.md",
    "33_Transport-Trade-and-Indian-Space-Programme_Complete-Topic-Package.md",
    [
        (
            "Transport as economic circulation",
            "Transport is the circulatory system of an economy because it moves raw materials, labour, finished goods, information and strategic power across space, and trade geography grows out of connectivity, cost, time and chokepoints.",
        ),
        (
            "Six modes and their limits",
            "Road, rail, sea, inland waterway, air and pipeline each pair a distinct strength with a distinct limitation, so no mode is best in general and air is not best for bulk merely because it is fastest.",
        ),
        (
            "Modal cost structure",
            "Road has low terminal cost and high cost per kilometre, rail has higher terminal and lower per-kilometre cost, water has the highest terminal and lowest per-kilometre cost, air is expensive throughout, and pipeline has very high fixed with very low operating cost.",
        ),
        (
            "Break-even and value density",
            "The cheapest mode is the one whose terminal cost is recovered over the haul length involved, so the road-rail break-even distance and the value-to-weight ratio together decide modal choice.",
        ),
        (
            "Intermodal chain rule",
            "Modern freight is a chain of road collection, rail or water trunk haul and road distribution, so container handling, multimodal terminals and last-mile connectivity determine actual logistics cost more than headline modal tariffs.",
        ),
        (
            "Network vocabulary",
            "Hinterland, node, corridor, break of bulk and hub-and-spoke are the standard concepts for reading any transport network from mine or farm through roadhead and rail corridor to port and world market.",
        ),
        (
            "Site versus situation",
            "A port's site is its own physical setting of depth, shelter, tidal range, foreshore, expansion land and siltation risk, while its situation is its position relative to a hinterland and to shipping routes, and situation normally decides which ports grow.",
        ),
        (
            "Site is engineerable, situation is not",
            "Depth and shelter can be dredged and engineered while hinterland productivity and connectivity cannot, which makes dedicated freight corridors and inland container depots a port policy instrument rather than a merely transport one.",
        ),
        (
            "Hinterland competition boundary",
            "Two ports serving the same interior compete, and the boundary between their hinterlands shifts with rail freight rates, road quality and inland container facilities.",
        ),
        (
            "Containerisation and hub concentration",
            "Containerisation standardised the cargo unit, collapsed handling time and cost, made intermodal transfer routine, permitted fragmentation of production across countries, and concentrated traffic at fewer deep-draught, high-crane-productivity, well-connected hubs with feeder services.",
        ),
        (
            "Chokepoint vulnerability",
            "Canals and straits matter because they shorten or control routes, so a disruption at one narrow passage lengthens voyages and raises freight and insurance costs far beyond the affected region.",
        ),
        (
            "Two-way transport-development relation",
            "Transport lowers input and output costs and widens markets, while development generates the traffic that justifies investment, so network density mirrors economic geography as much as it creates it.",
        ),
        (
            "Tunnel and backwash caveats",
            "A corridor can pass through a region without benefiting it when there are no junctions, no local loading and no complementary investment, and better connectivity can also expose weak local producers to outside competition and accelerate out-migration of the young and skilled.",
        ),
        (
            "India multimodal corridor programmes",
            "Bharatmala builds economic corridors, inter-corridors, border and port connectivity, Dedicated Freight Corridors separate freight from passenger congestion, Sagarmala pursues port modernisation with port-led industrialisation, and PM Gati Shakti replaces mode-wise planning with network integration.",
        ),
        (
            "India coastal trade contrast",
            "India's trade is coast-oriented but hinterland-dependent, with the western seaboard acting as the gateway for container and petroleum flows and the eastern coast tied to bulk minerals, coal, fertilizers and East Asian links.",
        ),
        (
            "Space as observation instrument",
            "Satellite systems are the primary observation instrument of modern geography, supplying land-use and land-cover mapping, crop acreage and condition assessment, forest and water-body monitoring, glacier and coastline change detection, and cyclone and monsoon tracking for warning systems.",
        ),
        (
            "Application-led space orientation",
            "India's space programme has been organised around application in communication, meteorology, resource survey, navigation, education and disaster support rather than around prestige, and that orientation is what makes it a geography topic rather than a technology one.",
        ),
        (
            "Space institutional ladder",
            "ISRO, the Satish Dhawan Space Centre at Sriharikota with its east-coast over-sea launch safety advantage, URSC, VSSC and LPSC, NSIL for commercialisation, IN-SPACe for non-governmental participation and NavIC for indigenous navigation form India's space-geography institutional ladder.",
        ),
        (
            "GIS convergence rule",
            "Remote-sensing imagery becomes usable planning information only when combined in a geographic information system with terrain, infrastructure, administrative and socio-economic layers, which is what supports site selection, corridor alignment, watershed and command-area planning and disaster damage assessment.",
        ),
        (
            "NVS-02 launch-versus-operations anchor",
            "GSLV-F15 placed NVS-02 in transfer orbit on 29 January 2025, but its orbit-raising propulsion could not be used and the satellite did not enter its intended NavIC slot, which shows that launch success and operational-constellation success are not identical.",
        ),
    ],
    [
        "Do not treat trade geography as only exports and imports; it is routes, nodes, costs, chokepoints and hinterlands.",
        "Do not claim air transport dominates world freight; sea transport carries the heavy international cargo.",
        "Do not call one mode cheapest without stating the cargo type and haul length.",
        "Do not merge site and situation when explaining why a port grew.",
        "Do not treat a port as serving only its coastal state; hinterlands run deep inland.",
        "Do not describe Dedicated Freight Corridors as ordinary railway upgrades.",
        "Do not present a canal or strait as valuable as a water body rather than as a route control.",
        "Do not assume connectivity automatically develops the region a corridor passes through.",
        "Do not omit the backwash counterpoint when praising infrastructure-led development.",
        "Do not treat the space programme as symbolic; navigation, remote sensing and communication have direct economic use.",
        "Do not equate launch success with operational-constellation success.",
        "Do not quote satellite counts, mission specifications, port tonnages, highway or railway lengths or freight shares from memory.",
        "Do not convert an unkeyed routed Prelims question into a solved answer with an invented key.",
        "Do not treat remote-sensing imagery as planning information before it is combined in a geographic information system.",
    ],
    [
        (
            10,
            "Explain why the cheapest transport mode cannot be identified without stating the cargo type and the length of haul.",
            "Modal cost is a structure rather than a single price, so the terminal-cost and per-kilometre-cost combination, the break-even haul length and the value-to-weight ratio jointly decide which mode is actually cheapest for a given consignment.",
            [1, 2, 3, 4],
        ),
        (
            10,
            "Distinguish the site of a port from its situation and explain which of the two usually decides port growth.",
            "Site is the correctable physical setting while situation is the hinterland and route position that cannot be engineered, so situation usually decides which ports grow and inland connectivity becomes a port policy instrument.",
            [5, 6, 7, 8],
        ),
        (
            15,
            "Examine the significance of straits, canals and isthmuses in international trade.",
            "Narrow passages compress world movement into small spaces, so they shorten routes, concentrate traffic and convert commercial geography into strategic geography by making disruption at a single point a global cost event.",
            [0, 9, 10, 14],
        ),
        (
            15,
            "How far is efficient and affordable urban mass transport a key to the economic development of a city region?",
            "Mass transport raises effective accessibility and enlarges the labour and consumption market of a city region, but its developmental payoff depends on network reach, land-use integration and complementary local capacity rather than on the line alone.",
            [0, 4, 11, 12],
        ),
        (
            20,
            "Assess how far Bharatmala, the Dedicated Freight Corridors and Sagarmala together are reshaping India's economic geography.",
            "The three programmes replace isolated links with multimodal corridors that connect hinterland production to ports and export routes, but corridor-led growth redistributes accessibility rather than creating development automatically, so complementary investment decides the outcome.",
            [11, 12, 13, 14],
        ),
        (
            20,
            "Evaluate the Indian space programme as an instrument of applied geography rather than as scientific prestige.",
            "The programme's application orientation makes satellites the primary observation and positioning infrastructure of Indian geography, but capability is realised only through GIS integration and operational constellations, so a launch is not by itself a governance outcome.",
            [15, 16, 17, 19],
        ),
    ],
    [
        plan(
            "Transport as the circulatory system of the economy",
            [0],
            "Trade geography is inseparable from connectivity and cost.",
            "Open with movement of goods, labour, information and power before naming any mode.",
        ),
        plan(
            "The six transport modes and their limits",
            [1],
            "Every mode pairs a strength with a limitation.",
            "Set out modes as a suitability table rather than as an advantages list.",
        ),
        plan(
            "Modal cost structure",
            [2],
            "Terminal cost and per-kilometre cost behave differently.",
            "Explain cost as a structure so the comparison survives any cargo example.",
        ),
        plan(
            "Break-even distance and value density",
            [3],
            "The cheapest mode changes with haul length and value-to-weight ratio.",
            "Use break-even logic as the decisive rule in any modal-comparison answer.",
        ),
        plan(
            "The intermodal chain",
            [4],
            "Freight is a chain, not a single modal choice.",
            "Shift the answer from modal tariffs to terminals and last-mile connectivity.",
        ),
        plan(
            "Reading a network: hinterland, node, corridor and break of bulk",
            [5],
            "Break of bulk marks a cost step, not a mere transfer.",
            "Apply the network vocabulary to one continuous farm-to-market rail.",
        ),
        plan(
            "Port site versus port situation",
            [6],
            "An excellent site with a poor hinterland stays small.",
            "Separate the two terms explicitly before judging any port.",
        ),
        plan(
            "Why situation cannot be engineered",
            [7],
            "Dredging corrects site; it cannot create a hinterland.",
            "Convert the distinction into a port policy conclusion about inland connectivity.",
        ),
        plan(
            "Hinterland competition between ports",
            [8],
            "Hinterland boundaries move with freight rates, not with coastlines.",
            "Explain competing hinterlands before comparing two ports.",
        ),
        plan(
            "Containerisation and hub concentration",
            [9],
            "Fewer ports handling more cargo is a hierarchy effect, not a statistic.",
            "Answer port-hierarchy questions with containerisation logic and no tonnage figures.",
        ),
        plan(
            "Chokepoints and route vulnerability",
            [10],
            "A chokepoint matters as route control, not as a water body.",
            "Show why disruption at a narrow passage becomes a global cost event.",
        ),
        plan(
            "The two-way transport and development relation",
            [11],
            "Density mirrors the economy as much as it creates it.",
            "State both directions before assessing any corridor programme.",
        ),
        plan(
            "Tunnel effect and backwash caveats",
            [12],
            "A corridor can cross a region without benefiting it.",
            "Add the distributional counterpoint that most infrastructure answers omit.",
        ),
        plan(
            "India's corridor and port programmes",
            [13, 14],
            "Corridor programmes redistribute accessibility rather than guarantee growth.",
            "Link Bharatmala, freight corridors and Sagarmala into one multimodal argument.",
        ),
        plan(
            "Space as applied geography and the operational-orbit boundary",
            [15, 16, 17, 18, 19],
            "Launch success is not operational-constellation success.",
            "Close with observation, navigation and GIS integration under a dated operational caution.",
        ),
    ],
    [
        panel(
            "Transport to trade chain",
            "process-flow",
            [
                "MINE OR FARM -> production point with dispersed origins",
                "ROADHEAD -> flexible collection over short hauls",
                "RAIL OR WATERWAY CORRIDOR -> bulk trunk haul over long distance",
                "PORT OR AIRPORT -> break of bulk and interface with global routes",
                "WORLD MARKET -> exchange completed through connectivity, cost and time",
            ],
            ["Transport as economic circulation", "Network vocabulary"],
        ),
        panel(
            "Modal cost structure comparison",
            "comparison-table",
            [
                "ROAD -> low terminal cost, high per-km cost; short hauls and door-to-door delivery",
                "RAIL -> higher terminal cost, lower per-km cost; medium to long bulk hauls",
                "WATER -> highest terminal cost, lowest per-km cost; long bulky low-value cargo",
                "AIR -> costly throughout; justified by high value-to-weight, urgency or inaccessibility",
                "PIPELINE -> very high fixed cost, very low operating cost; continuous liquid or gas flow",
            ],
            ["Six modes and their limits", "Modal cost structure"],
        ),
        panel(
            "Modal choice decision rule",
            "decision-tree",
            [
                "IDENTIFY CARGO -> bulk, value density, urgency and perishability",
                "IF haul is short -> terminal cost dominates, road usually wins",
                "IF haul exceeds the road-rail break-even -> rail or water recovers its terminal cost",
                "IF value-to-weight is very high or access is difficult -> air becomes defensible",
                "ALWAYS -> treat freight as an intermodal chain, not a single modal verdict",
            ],
            ["Break-even and value density", "Intermodal chain rule"],
        ),
        panel(
            "Network vocabulary rail",
            "institutional-ladder",
            [
                "HINTERLAND -> inland area served by a port, city or route",
                "NODE -> junction or terminal where flows converge",
                "CORRIDOR -> linear axis of intense transport and economic activity",
                "BREAK OF BULK -> port, railhead or dry port where cargo changes mode",
                "HUB AND SPOKE -> one major hub redistributes flows to smaller nodes",
            ],
            ["Network vocabulary", "Intermodal chain rule"],
        ),
        panel(
            "Port site versus situation",
            "comparison-table",
            [
                "SITE -> depth, shelter, tidal range, foreshore, expansion land, siltation risk",
                "SITUATION -> hinterland productivity, inland connectivity, position on shipping lanes",
                "CORRECTABILITY -> site can be dredged and engineered; situation cannot",
                "GROWTH RULE -> situation normally decides which ports grow",
                "POLICY -> freight corridors and inland container depots are port instruments",
            ],
            ["Site versus situation", "Site is engineerable, situation is not"],
        ),
        panel(
            "Port type worked comparison",
            "comparison-table",
            [
                "NATURAL HARBOUR -> excellent site; stays small if the hinterland is poor",
                "ESTUARINE PORT -> good route situation, but siltation and draught limit the site",
                "ARTIFICIAL DEEP-WATER PORT -> engineered site chosen for hinterland reach and rail links",
                "SATELLITE CONTAINER TERMINAL -> deep draught and back-up land beside a congested parent",
                "TRANSHIPMENT HUB -> situation is the route itself, so it lives without a local hinterland",
            ],
            ["Site versus situation", "Hinterland competition boundary", "Containerisation and hub concentration"],
        ),
        panel(
            "Containerisation hierarchy effect",
            "causal-system",
            [
                "STANDARD CARGO UNIT -> handling time and cost collapse at every transfer",
                "INTERMODAL TRANSFER BECOMES ROUTINE -> production fragments across countries",
                "ADVANTAGE SHIFTS -> deep draught, crane productivity and inland rail connectivity",
                "TRAFFIC CONCENTRATES -> fewer, larger hubs with feeder services to the rest",
                "ANSWER USE -> a hierarchy argument that needs no throughput statistic",
            ],
            ["Containerisation and hub concentration", "Hinterland competition boundary"],
        ),
        panel(
            "Chokepoint vulnerability rail",
            "causal-system",
            [
                "NARROW PASSAGE -> world shipping is funnelled through a small cross-section",
                "DISRUPTION -> voyages lengthen and rerouting begins immediately",
                "COST TRANSMISSION -> freight and insurance rise far beyond the affected region",
                "POLICY RESPONSE -> chokepoint security, alternative routes and canal capacity",
                "READING -> the passage is valuable as route control, not as a water body",
            ],
            ["Chokepoint vulnerability", "Transport as economic circulation"],
        ),
        panel(
            "Transport and development two-way fork",
            "decision-tree",
            [
                "NEW LINK OPENS -> relative accessibility of every node changes, not only the two joined",
                "IF junctions, local loading and complementary investment exist -> corridor growth follows",
                "IF they are absent -> the tunnel effect carries benefit to the endpoints",
                "IF local producers are weak -> backwash exposes them and speeds out-migration",
                "VERDICT -> connectivity is necessary but not sufficient for regional development",
            ],
            ["Two-way transport-development relation", "Tunnel and backwash caveats"],
        ),
        panel(
            "India multimodal corridor ladder",
            "institutional-ladder",
            [
                "BHARATMALA -> economic corridors, inter-corridors, border and port connectivity",
                "DEDICATED FREIGHT CORRIDORS -> separate freight from passenger congestion on major axes",
                "SAGARMALA -> port modernisation, port-led industrialisation and coastal connectivity",
                "PM GATI SHAKTI -> network integration replacing mode-wise sectoral planning",
                "TRADE MAP -> western container and petroleum gateway; eastern bulk and mineral coast",
            ],
            ["India multimodal corridor programmes", "India coastal trade contrast"],
        ),
        panel(
            "Space as applied geography",
            "process-flow",
            [
                "EARTH OBSERVATION -> land use, crop condition, forests, water bodies, coasts, glaciers",
                "METEOROLOGY -> cyclone tracking and monsoon monitoring feeding warning systems",
                "NAVIGATION AND COMMUNICATION -> positioning, timing and remote-region connectivity",
                "GIS INTEGRATION -> imagery plus terrain, infrastructure and socio-economic layers",
                "OUTPUT -> site selection, corridor alignment, watershed planning, damage assessment",
            ],
            ["Space as observation instrument", "GIS convergence rule"],
        ),
        panel(
            "Space institutions and the operational-orbit caution",
            "institutional-ladder",
            [
                "ISRO -> national space architecture organised around application, not prestige",
                "SRIHARIKOTA -> east-coast launch site with over-sea trajectory safety advantage",
                "NSIL AND IN-SPACe -> commercialisation and non-governmental participation",
                "NavIC -> indigenous navigation supporting transport timing and positioning",
                "NVS-02 ON 29 JAN 2025 -> reached transfer orbit but not its intended NavIC slot",
            ],
            ["Space institutional ladder", "Application-led space orientation", "NVS-02 launch-versus-operations anchor"],
        ),
    ],
    [
        "hinterland",
        "break of bulk",
        "containerisation",
        "chokepoint",
        "Bharatmala",
        "Dedicated Freight Corridor",
        "Sagarmala",
        "Sriharikota",
        "NavIC",
        "geographic information system",
    ],
    (
        "Geography Topic 33 owns direct Mains PYQ demand in the audited routing ledgers. "
        "Two GS-I demands are routed to this owner: 2019 Q16 on efficient and affordable urban mass "
        "transport, and 2022 Q16 on the significance of straits and isthmuses in international trade. "
        "Both are answered below as original model solutions built only from owner evidence. The "
        "routed Prelims demands for this topic are recorded in the owner ledgers as objective "
        "questions whose official keys are either unavailable locally or deliberately not inferred, "
        "so no option letter, answer key or invented question wording appears anywhere in this package."
    ),
    [
        (
            "2019",
            "GS-I Q16 (How is it key, 15 marks, 250 words)",
            "Explain how efficient and affordable urban mass transport is key to the economic development of India.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. The wording is the ledger's neutral rendering, not reproduced official paper text.",
            "Thesis: urban mass transport is developmental because it changes relative accessibility inside a city region, and it is that redistribution rather than the aggregate saving that produces economic effects. Build the argument from this owner's cost logic. Road transport carries a low terminal cost and a high cost per kilometre, so dispersed private movement becomes expensive in time and congestion as a city grows; a high-capacity fixed-route system reverses the structure by absorbing a heavy terminal and capital cost in exchange for a very low cost per passenger-kilometre. The consequence is that the effective labour market of the city widens, employers draw on a larger skill pool, low-income workers reach distant jobs without spending a punitive share of income on travel, and land near stations gains value that can be captured for further investment. Apply the intermodal rule next: a trunk line delivers benefit only when feeder services, walkability and last-mile connectivity complete the chain, exactly as freight logistics depends on terminals rather than headline tariffs. Then supply the honest counterpoint this owner insists on. The relationship is two-way, since traffic densities justify investment as much as investment creates them, so a line built where demand and land use are not aligned underperforms. A corridor can also produce a tunnel effect, carrying passengers across intermediate areas that gain nothing without stations, junctions and complementary land-use planning. Conclude in graded terms: efficient and affordable mass transport is a necessary condition for large-city productivity and inclusion, and it becomes sufficient only when integrated with land use, feeder networks and affordable fare design.",
        ),
        (
            "2022",
            "GS-I Q16 (Mention, 15 marks, 250 words)",
            "Mention the significance of straits and isthmuses in international trade.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. Only the ledger's neutral rendering is used, and no official key exists for a Mains question.",
            "Thesis: straits and isthmuses matter because world trade follows routes that minimise time and fuel while connecting large markets, and narrow passages compress that movement into very small cross-sections. Explain the geographic mechanism first. Sea transport carries the bulk of world merchandise because it has the lowest cost per tonne-kilometre, but that advantage is realised only along viable routes; a strait shortens or controls such a route, and an isthmus either blocks a sea route and forces a long detour or, when cut by a canal, removes the detour entirely. Both therefore convert a physical narrowing into an economic multiplier. Develop the consequences in three layers. First, distance and time savings lower freight and insurance cost and change which producers can compete in which market, which is the comparative-advantage argument expressed spatially. Second, the passages concentrate traffic and so create chokepoint vulnerability: disruption at one narrow point lengthens voyages and raises freight and insurance costs far beyond the affected region, which is why capacity, security and alternative-route projects are treated as strategic rather than commercial questions. Third, the passages restructure port hierarchies, because containerisation rewards deep-draught, well-connected locations positioned on trunk routes, and transhipment hubs can live on route position alone with almost no local hinterland. Qualify the answer by refusing traffic-share or tonnage figures from memory and by noting that route significance shifts with technology, fuel prices and conflict. Conclude that straits and isthmuses are best described not as water bodies or land bridges but as control points where geography sets the terms of global exchange.",
        ),
    ],
    [
        "https://www.isro.gov.in/",
        "https://sagarmala.gov.in/",
        "https://shipmin.gov.in/",
        "https://morth.nic.in/",
        "https://pib.gov.in/",
    ],
    (
        "The only dated current anchor used is the GSLV-F15 flight of 29 January 2025, which placed "
        "NVS-02 in transfer orbit while the orbit-raising propulsion could not be used, so the "
        "satellite did not enter its intended NavIC slot. That status is recorded in the repository "
        "owner and was confirmed against the official ISRO mission page. Ministry, Sagarmala and PIB "
        "portals are named only as the correct source class for corridor, port and space updates. No "
        "port tonnage, container throughput, highway or railway length, freight share, satellite "
        "count or programme outlay is quoted from memory, and no launch is presented as an "
        "operational-constellation outcome."
    ),
)

TOPIC_34 = common.topic(
    34,
    "World Regional Geography: Continents and Countries",
    "34_World-Regional-Geography-Continents-Countries.md",
    "34_World-Regional-Geography-Continents-Countries.md",
    "34_World-Regional-Geography-Continents-Countries_Complete-Topic-Package.md",
    [
        (
            "What regional geography does",
            "Regional geography studies the Earth by dividing it into large areas with internal coherence, which may be physical, climatic, cultural, economic or historical rather than merely political.",
        ),
        (
            "First frame and second frame",
            "Continents are the first-order frame, but examination questions usually work at the second frame of sub-regions, transition zones, chokepoints, river basins, deserts, mountain systems and country-location associations.",
        ),
        (
            "Country-linking rule",
            "A country should never be memorised as an isolated name; it must be linked to a region, a relief unit, a river or sea, and an economic identity so that map elimination becomes possible.",
        ),
        (
            "Continental first-order pattern",
            "In the source framework Asia is the largest continent in both area and population, Antarctica is an ice-dominated polar desert, Europe is highly peninsular and urbanised, and Australia is the smallest continent with a strong interior-aridity pattern.",
        ),
        (
            "Macro-region catalogue",
            "The macro-regions to recognise are South-West Asia, South Asia, mainland and maritime South-East Asia, East Asia, Central Asia, North Asia or Siberia, North Africa against Sub-Saharan Africa, Anglo America against Latin America, the northern, western, eastern and Mediterranean Europes, and Australia against Oceania.",
        ),
        (
            "Category discipline",
            "Continent, region, sub-region and civilisational label are different categories, so Middle East, Latin America and Nordic are regional labels rather than continents, and Australia is a continent while Oceania is the wider island region around it.",
        ),
        (
            "Transition-belt concept",
            "The Sahel is a transition belt defined by a rainfall gradient rather than by relief or political boundary, so it runs across many states and lies wholly within none.",
        ),
        (
            "Physiographic-economic pairing",
            "Every macro-region pairs a dominant physical frame with an economic association: Sahara, Atlas and the Nile corridor with oasis belts and the Suez gateway; the Congo Basin and plateaux with mining and plantation belts; the North European Plain and navigable rivers with dense transport and port economy; the Western Cordillera and Great Plains with wheat and industrial corridors; and the Andes, Amazon and Pampas with copper, rainforest and temperate farming.",
        ),
        (
            "Left-to-right map chain",
            "A workable mental chain runs Atlantic world to Europe to West Asia to South Asia to South-East Asia to Pacific Asia, so any given sea, strait, plateau or river should first be placed inside a region and then inside a continent.",
        ),
        (
            "Eight comparison axes",
            "Any comparative regional question can be answered on eight axes: location and situation, structure and relief, climate and water, resource base, population and settlement, economic structure, connectivity, and constraints and risks.",
        ),
        (
            "Comparison method rule",
            "Each chosen axis must be applied to both regions inside the same paragraph, because a comparison written as two separate descriptions is marked as description rather than comparison.",
        ),
        (
            "Landlocked structural penalty",
            "A landlocked state depends on a neighbour's ports, roads and goodwill, faces higher freight costs and longer transit times and cannot independently guarantee trade access, which is why transit agreements and corridor projects matter disproportionately to interior states.",
        ),
        (
            "Situation outweighs site",
            "Regions positioned on major shipping lanes or at land bridges between economic cores have historically prospered relative to better-endowed peripheral regions, but situation is a relative and changeable property that a new canal, pipeline, corridor or route closure can transform.",
        ),
        (
            "Seven-step regional method",
            "A regional answer is built by locating and delimiting the region, establishing its physical base, testing accessibility, assessing the resource base, describing population and culture, stating the economic outcome, and closing with synthesis and qualification.",
        ),
        (
            "North-east India worked case",
            "India's north-east is internationally adjacent but nationally peripheral, combining young fold ranges and hill terrain around a large alluvial valley, extremely high rainfall on some slopes, high seismicity, a narrow land corridor that raises transport cost, hydropower, hydrocarbon, plantation and forest resources that are hard to move to market, and very high ethno-linguistic diversity, while remaining internally non-uniform.",
        ),
        (
            "Sahel worked case",
            "The Sahel is a semi-arid east-west belt with a single short wet season, exceptionally high inter-annual rainfall variability, level to gently undulating terrain, thin fragile soils vulnerable to wind and water erosion, largely interior location with long distances to any port, and an economy historically built on rain-fed drought-tolerant cereals and extensive pastoralism.",
        ),
        (
            "India's outward arcs",
            "India's regional geography is maritime-heavy in the west and east and barrier-heavy in the north: westward through the Arabian Sea to the Gulf and Red Sea approaches and Suez, eastward through the Bay of Bengal and Andaman Sea toward Malacca-oriented passages, and northward against the Himalaya-Karakoram barrier toward Central Asia.",
        ),
        (
            "Feature-not-capital trap",
            "Questions increasingly combine a country with a strait, sea, river, plateau, delta or island chain, so the high-yield pairings are Suez with Egypt, the Bosporus and Dardanelles with Turkey, Hormuz with Iran, the United Arab Emirates and Oman, and Malacca with Singapore, Indonesia and Malaysia.",
        ),
        (
            "Neighbourhood anchors",
            "Myanmar is India's only land bridge into mainland South-East Asia, Bangladesh is the deltaic neighbour that wraps around much of India's north-east approach, and Central Asia is close in map distance but access-constrained by mountains and intervening transit politics.",
        ),
        (
            "Kaladan corridor anchor",
            "The Kaladan Multi-Modal Transit Transport Project connects Kolkata by sea to Sittwe on Myanmar's Rakhine coast, then along the Kaladan river to Paletwa and by road to Zorinpui on the Mizoram border; the Paletwa-Zorinpui road segment remains under construction and the officially stated operational target is 2027.",
        ),
    ],
    [
        "Do not treat continent, region, sub-region and civilisational label as interchangeable categories.",
        "Do not equate North America with Latin America; Latin America begins at Mexico and runs southward.",
        "Do not reduce Africa to Sahara plus rainforest and omit the Sahel, savanna, Rift Valley and Mediterranean margins.",
        "Do not treat the Sahel as a country or a continent instead of a rainfall-defined transition belt.",
        "Do not merge Australia the continent with Oceania the wider island region.",
        "Do not treat mainland and maritime South-East Asia as one undifferentiated region.",
        "Do not define the Middle East as all Muslim-majority countries rather than as a geographic-regional label.",
        "Do not answer a comparison by describing two regions one after the other.",
        "Do not treat a landlocked region's internal resources as sufficient without addressing transit dependence.",
        "Do not present situation as a permanent attribute; a new corridor or closure can change it.",
        "Do not generalise across a region that is internally non-uniform, such as India's north-east.",
        "Do not quote continental area or population shares as current data; the source table is a book-era snapshot.",
        "Do not quote corridor widths, state areas, rainfall records, hydropower megawatts or population percentages from memory.",
        "Do not convert an unkeyed routed Prelims question into a solved answer with an invented key.",
    ],
    [
        (
            10,
            "Distinguish continent, region, sub-region and transition belt with suitable world examples.",
            "The four terms describe different orders of spatial coherence, so a continent is a landmass frame, a region is an internally coherent area, a sub-region is its differentiated part, and a transition belt is a gradient zone that belongs fully to neither of its neighbours.",
            [0, 4, 5, 6],
        ),
        (
            10,
            "Explain why a country should be learnt through its region, relief and route position rather than as an isolated name.",
            "Locational learning works because map questions test associations between a country and a strait, sea, river, plateau or island chain, and elimination depends on placing a feature first in a region and then in a continent.",
            [1, 2, 8, 17],
        ),
        (
            15,
            "Discuss how physical frames such as the Andes-Amazon system, the North European Plain and West Asian desert-plateau geography create distinct regional identities.",
            "Regional identity emerges where a dominant physical frame sets the terms for soils, water, minerals and transport, and the economic association that follows becomes the region's recognisable personality rather than an accidental attribute.",
            [3, 7, 9, 12],
        ),
        (
            15,
            "Explain the method by which a distinctive region should be analysed, using India's north-east and the Sahel as worked cases.",
            "A regional answer is an argument that a particular combination of physical, historical, economic and political conditions produces a distinctive outcome, so the seven-step method matters more than the accumulation of regional facts.",
            [13, 14, 15, 11],
        ),
        (
            20,
            "Is location or resource endowment the stronger explanation of a world region's economic importance? Analyse.",
            "Situation frequently outweighs endowment because route position and transit access decide whether resources can reach markets, but situation is changeable and endowment still sets the ceiling, so the honest verdict is conditional rather than absolute.",
            [9, 11, 12, 16],
        ),
        (
            20,
            "Assess the proposition that India's regional geography is outward-facing in the seas and constrained in the mountains.",
            "India's westward and eastward maritime arcs give it comparatively open access to West Asia, East Africa and South-East Asia, while the northern mountain barrier and transit politics make Central Asia difficult, so corridor projects through the eastern land bridge carry disproportionate significance.",
            [16, 17, 18, 19],
        ),
    ],
    [
        plan(
            "What regional geography does and at which frame",
            [0, 1],
            "Continents are the opening frame, not the examinable one.",
            "Open by naming the frame you are working at before describing any region.",
        ),
        plan(
            "Learning a country as a locational bundle",
            [2],
            "An isolated country name carries no eliminating power.",
            "Attach region, relief, river or sea and economic identity to every country named.",
        ),
        plan(
            "The continental first-order pattern",
            [3],
            "The source continental table is a book-era snapshot, not current data.",
            "Use continental extremes as pattern anchors without quoting dated shares.",
        ),
        plan(
            "The macro-region catalogue",
            [4],
            "Mainland and maritime South-East Asia are not one region.",
            "Set out macro-regions by organising logic rather than by membership list.",
        ),
        plan(
            "Category discipline: continent, region, label",
            [5],
            "Middle East, Latin America and Nordic are labels, not continents.",
            "Name the category you are using before you compare any two areas.",
        ),
        plan(
            "Transition belts and gradient boundaries",
            [6],
            "A gradient belt lies wholly inside no single state.",
            "Explain the Sahel as a rainfall gradient before mentioning any country.",
        ),
        plan(
            "Physiographic frames and their economic associations",
            [7],
            "The economic association follows the physical frame, not the reverse.",
            "Pair frame with economy for each region instead of listing produce.",
        ),
        plan(
            "The left-to-right map chain",
            [8],
            "Place a feature in a region before placing it in a continent.",
            "Use the chain as a fast locating device in map-based elimination.",
        ),
        plan(
            "The eight comparison axes and how to use them",
            [9, 10],
            "Two separate descriptions never score as a comparison.",
            "Select four or five axes and apply each to both regions in one paragraph.",
        ),
        plan(
            "Landlocked location as a structural variable",
            [11],
            "Transit dependence is structural, not diplomatic accident.",
            "Convert interior location into a freight-cost and transit argument.",
        ),
        plan(
            "Situation against site in regional importance",
            [12],
            "Situation is relative and can be transformed by a new route.",
            "Argue route position first, then qualify its impermanence.",
        ),
        plan(
            "The seven-step regional method",
            [13],
            "A regional answer is an argument, not a fact list.",
            "Move through locate, base, access, resources, people, outcome and qualification.",
        ),
        plan(
            "Worked case one: India's north-east",
            [14],
            "The region is internally non-uniform, so avoid region-wide generalisation.",
            "Show compound causation: terrain, corridor, adjacency and plurality together.",
        ),
        plan(
            "Worked case two: the Sahel",
            [15],
            "Variability, not average rainfall, is the operative constraint.",
            "Use the Sahel as the second worked case any comparison requires.",
        ),
        plan(
            "India's outward arcs and the eastern land bridge",
            [16, 17, 18, 19],
            "Corridor status must be stated as target, not as completion.",
            "Close with maritime openness, northern constraint and a dated corridor anchor.",
        ),
    ],
    [
        panel(
            "Frames of regional analysis",
            "institutional-ladder",
            [
                "CONTINENT -> first-order landmass frame used to open the answer",
                "REGION -> area with internal physical, cultural or economic coherence",
                "SUB-REGION -> differentiated part such as mainland versus maritime South-East Asia",
                "TRANSITION BELT -> gradient zone such as the Sahel, belonging fully to neither side",
                "LABEL -> Middle East, Latin America, Nordic: regional shorthand, never a continent",
            ],
            ["What regional geography does", "First frame and second frame", "Category discipline", "Transition-belt concept"],
        ),
        panel(
            "Continental pattern anchors",
            "comparison-table",
            [
                "ASIA -> largest in area and population in the source framework; greatest sub-regional variety",
                "AFRICA -> plateaux, rift valley and the desert-savanna-rainforest sequence",
                "EUROPE -> peninsular, river-linked, densely urbanised interaction space",
                "AMERICAS -> Cordillera with interior plains north; Andes, Amazon and Pampas south",
                "ANTARCTICA AND AUSTRALIA -> polar desert under ice; smallest continent with arid interior",
            ],
            ["Continental first-order pattern", "Physiographic-economic pairing"],
        ),
        panel(
            "Macro-region organising logic",
            "comparison-table",
            [
                "SOUTH-WEST ASIA -> arid plateau, desert and chokepoint interfaces",
                "SOUTH ASIA -> monsoon domain framed by the Himalaya and the Indian Ocean",
                "SOUTH-EAST ASIA -> mainland river basins plus a maritime archipelagic world",
                "CENTRAL ASIA -> interior steppe, basin and mountain knotlands with transit dependence",
                "AFRICA SPLIT -> Sahara divides, but the Sahel is the transition belt between the halves",
            ],
            ["Macro-region catalogue", "Transition-belt concept", "Landlocked structural penalty"],
        ),
        panel(
            "Physical frame to economic association",
            "causal-system",
            [
                "SAHARA, ATLAS, NILE -> oasis belts, Mediterranean coast and the Suez gateway",
                "CONGO BASIN AND PLATEAUX -> mining, plantation belts and pastoral margins",
                "NORTH EUROPEAN PLAIN AND RIVERS -> dense transport, manufacturing and port economy",
                "CORDILLERA AND GREAT PLAINS -> wheat belt, industrial corridor and energy basins",
                "ANDES, AMAZON, PAMPAS -> copper west, rainforest core, temperate farming south",
            ],
            ["Physiographic-economic pairing", "Continental first-order pattern"],
        ),
        panel(
            "Left-to-right locating chain",
            "process-flow",
            [
                "ATLANTIC WORLD -> Europe with its plains, peninsulas and Alpine spine",
                "WEST ASIA -> Arabian and Iranian core with desert-plateau geography",
                "SOUTH ASIA -> Himalayan-monsoon core opening on the Indian Ocean",
                "SOUTH-EAST ASIA -> Malacca-facing archipelagic and mainland passage world",
                "RULE -> place the feature in a region first, then inside its continent",
            ],
            ["Left-to-right map chain", "Feature-not-capital trap"],
        ),
        panel(
            "Eight comparison axes",
            "institutional-ladder",
            [
                "LOCATION AND SITUATION -> latitude, coastal or landlocked, proximity to routes",
                "STRUCTURE AND CLIMATE -> shield, fold belt, basin; regime and reliability of water",
                "RESOURCES AND PEOPLE -> accessibility and processing; density and urbanisation",
                "ECONOMY AND CONNECTIVITY -> sectoral composition; ports, corridors and chokepoints",
                "CONSTRAINTS -> hazard, water stress, fragmentation and resource dependence",
            ],
            ["Eight comparison axes", "Comparison method rule"],
        ),
        panel(
            "Comparison versus description fork",
            "decision-tree",
            [
                "QUESTION ASKS FOR A COMPARISON -> select four or five relevant axes",
                "IF each axis is applied to both regions in one paragraph -> it reads as comparison",
                "IF the regions are described one after the other -> it is marked as description",
                "THEN -> name the decisive axis on which the two differ most",
                "FINALLY -> give the counter-case axis on which they are alike, then a graded verdict",
            ],
            ["Comparison method rule", "Eight comparison axes"],
        ),
        panel(
            "Landlocked penalty and route position",
            "causal-system",
            [
                "INTERIOR LOCATION -> dependence on a neighbour's ports, roads and goodwill",
                "CONSEQUENCE -> higher freight cost, longer transit, no independent trade guarantee",
                "RESPONSE -> transit agreements and corridor projects gain disproportionate weight",
                "CONTRAST -> route position on a lane or land bridge often outweighs endowment",
                "CAUTION -> situation is relative; a new canal, corridor or closure rewrites it",
            ],
            ["Landlocked structural penalty", "Situation outweighs site"],
        ),
        panel(
            "Seven-step regional method",
            "process-flow",
            [
                "LOCATE AND DELIMIT -> state what bounds the region and what it excludes",
                "PHYSICAL BASE -> structure, relief, climate regime and hazard exposure",
                "ACCESSIBILITY -> corridor, coast or interior position and its cost consequence",
                "RESOURCES, PEOPLE, OUTCOME -> endowment, settlement pattern, economic result",
                "SYNTHESIS AND QUALIFICATION -> compound causation, then internal non-uniformity",
            ],
            ["Seven-step regional method", "North-east India worked case"],
        ),
        panel(
            "Two worked regions compared",
            "comparison-table",
            [
                "DELIMITATION -> hill-and-valley corridor region; east-west rainfall-gradient belt",
                "PHYSICAL BASE -> fold ranges, very high rainfall, seismicity; semi-arid, variable rainfall",
                "ACCESS -> narrow land corridor raising cost; interior location far from any port",
                "ECONOMY -> primary activity and out-migration; rain-fed cereals and pastoralism",
                "SHARED LESSON -> distinctiveness is compound, and neither region is internally uniform",
            ],
            ["North-east India worked case", "Sahel worked case"],
        ),
        panel(
            "India outward arcs",
            "process-flow",
            [
                "WEST -> Arabian Sea to Gulf and Red Sea approaches to the Suez corridor",
                "EAST -> Bay of Bengal to Andaman Sea toward Malacca-oriented passages",
                "NORTH -> Himalaya and Karakoram barrier with transit-constrained Central Asia",
                "LAND BRIDGE -> Myanmar is the only overland entry to mainland South-East Asia",
                "READING -> maritime-heavy west and east, barrier-heavy north",
            ],
            ["India's outward arcs", "Neighbourhood anchors"],
        ),
        panel(
            "Kaladan corridor and mapwork revival",
            "institutional-ladder",
            [
                "KOLKATA -> sea leg across the Bay of Bengal to the Rakhine coast",
                "SITTWE -> port node where the maritime leg meets the Kaladan river route",
                "PALETWA -> river terminus and start of the road segment still under construction",
                "ZORINPUI -> border crossing into Mizoram completing the multimodal chain",
                "STATUS RULE -> state the 2027 official target, never an achieved completion",
            ],
            ["Kaladan corridor anchor", "Neighbourhood anchors"],
        ),
    ],
    [
        "transition belt",
        "Sahel",
        "landlocked",
        "situation",
        "Malacca",
        "Hormuz",
        "Suez",
        "Kaladan",
        "Zorinpui",
        "maritime South-East Asia",
    ],
    (
        "The audited routing ledgers consulted for this build assign no direct Mains PYQ to Geography "
        "Topic 34. The topic does own a large body of routed Prelims demand across 2018 to 2025, "
        "covering seas and bordering countries, world rivers, the Levant, Congo Basin membership, "
        "Andean and equatorial crossings, time zones and region-country pairings, but those entries "
        "are recorded in the ledgers as objective questions whose official keys are either "
        "unavailable locally or deliberately not inferred. This package therefore keeps the regional "
        "method transparent, reproduces no option letter or answer key, and does not fabricate a "
        "direct solved PYQ card for a Mains demand this owner does not hold."
    ),
    [],
    [
        "https://pib.gov.in/",
        "https://www.mea.gov.in/",
        "https://mopsw.nic.in/",
        "https://www.iwai.nic.in/",
    ],
    (
        "The only dated current anchor used is the Kaladan Multi-Modal Transit Transport Project, "
        "recorded in the repository owner through a Press Information Bureau release of 7 July 2025 "
        "and confirmed against official Ministry of Ports, Shipping and Waterways material. Its route "
        "geography of Kolkata, Sittwe, the Kaladan river, Paletwa and Zorinpui is stated as route "
        "geography, the Paletwa-Zorinpui road is described as still under construction, and the 2027 "
        "date is presented strictly as an officially stated operational target rather than an "
        "achieved completion. No continental area or population share, corridor width, state area, "
        "rainfall record, hydropower figure or demographic percentage is quoted from memory."
    ),
)

TOPIC_35 = common.topic(
    35,
    "Indian Political Geography: Boundaries and Neighbours",
    "35_Indian-Political-Geography-Boundaries-and-Neighbours.md",
    "35_Indian-Political-Geography-Boundaries-and-Neighbours.md",
    "35_Indian-Political-Geography-Boundaries-and-Neighbours_Complete-Topic-Package.md",
    [
        (
            "Core political-geography vocabulary",
            "A boundary is a recognised line separating the territory or jurisdiction of two states, a frontier is a wider borderland zone of transition, a borderland is the human-use space on either side of the line, an enclave is territory enclosed by another state, and an exclave is a detached part of a state separated from its main territory.",
        ),
        (
            "Four stages of boundary making",
            "Boundaries are made through allocation as a political decision, delimitation as the map and text drawing, demarcation as physical marking on the ground, and administration through check posts, patrols, crossings and settlements.",
        ),
        (
            "Delimitation-demarcation gap",
            "Many disputes persist because delimitation exists on paper while demarcation on the ground is incomplete, or because a river or channel used as the defining feature later shifts.",
        ),
        (
            "Natural and geometric boundary types",
            "A natural or physical boundary follows a mountain, river, watershed, desert or sea, while an artificial or geometric boundary follows a straight or coordinate-based line, and straight-line boundaries are usually more political than physical.",
        ),
        (
            "Genetic classification of boundaries",
            "Antecedent, subsequent, superimposed and relict is a genetic classification that sorts boundaries by when they were drawn relative to the human landscape, and it is that timing which predicts the kind of dispute that follows.",
        ),
        (
            "Frontier as zone, boundary as line",
            "A boundary separates sovereignty as a precise line, while a frontier explains interaction, friction, migration, exchange and strategic depth as a zone, so converting a historical frontier into a modern boundary is itself a common origin of disputes.",
        ),
        (
            "Typology of dispute causes",
            "Boundary disputes arise from positional disagreement about where an agreed line runs, territorial disagreement about who owns a defined area, resource or functional contest over use across the line, antecedent and superimposed line problems, relict boundary effects and geomorphic instability of the defining feature.",
        ),
        (
            "Neither type is intrinsically stable",
            "A natural boundary is not automatically more peaceful than a geometric one, because a river migrates and is hard to demarcate while a straight line divides communities and resources.",
        ),
        (
            "Classical geopolitical lenses",
            "Mackinder's Heartland argument on Eurasian interior depth, Spykman's Rimland argument on coastal margins and Mahan's Sea Power argument on naval access and sea lanes are historical lenses, each identifying a genuine spatial variable rather than a predictive law.",
        ),
        (
            "What the classical theories omit",
            "The classical lenses omit air and space power, cyber and submarine-cable infrastructure, economic interdependence, non-state actors and nuclear deterrence, which together mean geography conditions strategy without determining it.",
        ),
        (
            "India's dual strategic character",
            "India's position is genuinely dual: a continental frontier requiring mountain and plains defence, and a peninsular maritime position astride major sea lanes with island territories extending its maritime reach, and recognising that duality is stronger than assigning India to any one school.",
        ),
        (
            "Sector-by-terrain management framework",
            "India's boundary management differs by terrain: high-altitude glaciated sectors face inaccessibility and watershed ambiguity, densely populated plains sectors face smuggling and divided fields, riverine and deltaic sectors face migrating channels and shifting char lands, forested hill sectors face cross-border ethnic continuity, desert sectors face surveillance over long distances with shifting markers, and the maritime boundary raises zone delimitation, island baselines and fishing questions.",
        ),
        (
            "Why uniform instruments fail",
            "Because India's border problem is several problems differing by terrain, settlement density, legal status of the line and the nature of cross-border activity, uniform instruments such as blanket fencing or a single force posture cannot fit all sectors.",
        ),
        (
            "Enclave and exchange logic",
            "An enclave leaves residents cut off from their own state's administration, services and law enforcement, which is why enclave exchange is the standard remedy and why this is a geographic problem before it is a diplomatic one.",
        ),
        (
            "India's neighbour set",
            "The source text treats India as sharing boundaries with Afghanistan through its claimed far north-west position, Pakistan, China, Nepal, Bhutan, Myanmar and Bangladesh, while Sri Lanka lies across the Palk Strait and Gulf of Mannar and the Maldives is the atoll neighbour across the Eight Degree Channel from Lakshadweep.",
        ),
        (
            "High-yield boundary lines",
            "The Radcliffe Line of 1947 framed the partition boundary with Pakistan, the McMahon Line of the 1914 framework concerns the eastern India-China sector, the Durand Line of 1893 is the Afghanistan-Pakistan line rather than an India-Pakistan line, and the 1949 Ceasefire Line became the Line of Control in 1972.",
        ),
        (
            "Category firewall for control lines",
            "International Boundary, the Line of Control and the Line of Actual Control are not interchangeable categories, because the first defines sovereignty, the second is a military control line and the third is a control reality over an undemarcated high-mountain frontier.",
        ),
        (
            "India-China three-sector division",
            "The India-China boundary is divided into a western sector in the Ladakh, Karakoram and Aksai Chin space, a middle sector along the Himachal Pradesh and Uttarakhand frontier, and an eastern sector along the Sikkim and Arunachal Pradesh frontier where the McMahon Line chiefly applies.",
        ),
        (
            "Land Boundary Agreement chain",
            "The 1974 Land Boundary Agreement, the 2011 Protocol and the 2015 implementation with its exchange of letters on 6 June and appointed day of 31 July resolved enclaves, adverse possessions and undemarcated stretches on the India-Bangladesh alluvial border.",
        ),
        (
            "Border-force geographic mandates",
            "The geographic mandates are the Border Security Force on the India-Pakistan and India-Bangladesh borders, the Indo-Tibetan Border Police on the India-China frontier, the Sashastra Seema Bal on the India-Nepal and India-Bhutan borders, the Assam Rifles on the India-Myanmar border and the Indian Coast Guard in the maritime surveillance space.",
        ),
    ],
    [
        "Do not treat boundary and frontier as synonyms; one is a legal line and the other is a zone.",
        "Do not call delimitation the act of marking a boundary on the ground; that is demarcation.",
        "Do not assume a natural boundary is automatically peaceful or easy to demarcate.",
        "Do not treat the Durand Line as India's boundary with Afghanistan.",
        "Do not equate the McMahon Line with the Line of Actual Control across all sectors.",
        "Do not use International Boundary, Line of Control and Line of Actual Control interchangeably.",
        "Do not present classical geopolitical theories as timeless predictive laws.",
        "Do not assign India to a single geopolitical school when its character is continental and maritime together.",
        "Do not answer border management with force names and schemes instead of terrain-to-management logic.",
        "Do not propose one uniform instrument for sectors with different terrain and settlement density.",
        "Do not confuse border-guarding mandates with the legal definition of a boundary.",
        "Do not state boundary lengths, numbers of border districts, disputed areas in square kilometres or the precise legal status of a disputed sector from memory.",
        "Do not describe Sri Lanka as a land neighbour; the separation is a shallow maritime gap.",
        "Do not convert an unkeyed routed Prelims question into a solved answer with an invented key.",
    ],
    [
        (
            10,
            "Distinguish boundary, frontier and borderland, and explain why frontier geography often matters more than the legal line.",
            "The three terms describe a line of sovereignty, a zone of transition and a lived human-use space, and questions about interaction, migration, exchange and strategic depth belong to the frontier and borderland rather than to the line itself.",
            [0, 5, 11, 13],
        ),
        (
            10,
            "Explain how boundaries are made and why so many disputes survive the making of a boundary.",
            "The four-stage sequence of allocation, delimitation, demarcation and administration leaves two structural weak points, since a paper line may never be marked on the ground and a defining physical feature may move after the line is drawn.",
            [1, 2, 3, 6],
        ),
        (
            15,
            "Examine the genetic classification of boundaries and show how boundary genesis predicts the type of dispute that follows.",
            "Classifying a boundary as antecedent, subsequent, superimposed or relict states when it was drawn relative to the human landscape, and that timing predicts whether the resulting dispute is positional, territorial, functional or a legacy effect.",
            [4, 6, 7, 12],
        ),
        (
            15,
            "Assess the relevance and the limitations of the Heartland, Rimland and Sea Power arguments for contemporary geography.",
            "Each classical lens isolates a genuine spatial variable in interior depth, coastal transition and maritime access, but each omits domains that now shape strategy, so the arguments frame a question without settling it.",
            [8, 9, 10, 16],
        ),
        (
            20,
            "Discuss the challenges of managing India's land and maritime borders and explain why uniform instruments cannot secure them all.",
            "India's borders present several distinct geographic problems set by terrain, settlement density and the legal clarity of the line, so differentiated management combining infrastructure, surveillance and local economic integration outperforms uniform hardening.",
            [11, 12, 13, 19],
        ),
        (
            20,
            "Analyse how India's boundary lines and neighbour geography require different analytical categories rather than a single border narrative.",
            "India's northern high-mountain frontier, its plains and deltaic land boundaries and its maritime neighbourhood are governed by different legal categories and terrain logics, so accurate answers separate international boundary, control line and undemarcated frontier before arguing.",
            [14, 15, 16, 17],
        ),
    ],
    [
        plan(
            "The core vocabulary of political geography",
            [0],
            "A frontier is a zone while a boundary is a line.",
            "Define all five terms before naming any place or dispute.",
        ),
        plan(
            "How a boundary is made, stage by stage",
            [1, 2],
            "Delimitation is on the map; demarcation is on the ground.",
            "Use the four-stage sequence to locate exactly where a dispute originates.",
        ),
        plan(
            "Natural and geometric boundary types",
            [3],
            "A straight line is a political artefact, not a physical feature.",
            "Classify the line physically before judging its stability.",
        ),
        plan(
            "The genetic classification and what it predicts",
            [4],
            "Genesis timing predicts the dispute type that follows.",
            "Name antecedent, subsequent, superimposed or relict, then predict the friction.",
        ),
        plan(
            "Frontier interaction against boundary sovereignty",
            [5],
            "Converting a frontier into a boundary is itself a dispute origin.",
            "Answer interaction questions from frontier geography, not from the line.",
        ),
        plan(
            "A typology of boundary-dispute causes",
            [6],
            "Positional, territorial and functional disputes need different remedies.",
            "Match the dispute mechanism to its remedy instead of listing disputed places.",
        ),
        plan(
            "Why no boundary type is intrinsically stable",
            [7],
            "Rivers migrate and straight lines divide communities.",
            "Reject the assumption that natural boundaries are inherently peaceful.",
        ),
        plan(
            "Classical geopolitical lenses",
            [8],
            "Treat Heartland, Rimland and Sea Power as lenses, not laws.",
            "Use each lens to isolate the spatial variable it actually identifies.",
        ),
        plan(
            "What the classical lenses omit",
            [9],
            "Geography conditions strategy without determining it.",
            "Add the omissions immediately after deploying any classical theory.",
        ),
        plan(
            "India's dual continental and maritime character",
            [10],
            "Assigning India to one school hides the resource trade-off.",
            "Argue duality and the trade-off it imposes rather than a single orientation.",
        ),
        plan(
            "India's sector-by-terrain border framework",
            [11],
            "The terrain sets the management problem in each sector.",
            "Move sector by sector, stating the management consequence each time.",
        ),
        plan(
            "Why uniform border instruments fail",
            [12, 13],
            "Hardening a line without livelihoods creates the alienation it targets.",
            "Close border-management answers with differentiated management, not uniform fencing.",
        ),
        plan(
            "India's neighbour set and its adjacency types",
            [14],
            "Sri Lanka and the Maldives are maritime, not land, neighbours.",
            "State adjacency type before discussing any neighbour relationship.",
        ),
        plan(
            "High-yield boundary lines and the category firewall",
            [15, 16],
            "International Boundary, Line of Control and Line of Actual Control are distinct.",
            "Name the correct legal category before describing any sector.",
        ),
        plan(
            "India-China sectors, the Bangladesh settlement and force mandates",
            [17, 18, 19],
            "Cartographic settlement is as much political geography as conflict is.",
            "Close with sectors, the enclave settlement chain and terrain-linked mandates.",
        ),
    ],
    [
        panel(
            "Political-geography vocabulary rail",
            "institutional-ladder",
            [
                "BOUNDARY -> recognised line separating territory or jurisdiction of two states",
                "FRONTIER -> wider zone of transition where authority thins out",
                "BORDERLAND -> lived human-use space on either side of the line",
                "ENCLAVE -> territory entirely enclosed by another state's territory",
                "EXCLAVE -> detached part of a state separated by another state's territory",
            ],
            ["Core political-geography vocabulary", "Frontier as zone, boundary as line"],
        ),
        panel(
            "Four stages of boundary making",
            "process-flow",
            [
                "ALLOCATION -> political decision on who receives which territory",
                "DELIMITATION -> the line is drawn in map and text form",
                "DEMARCATION -> pillars, fences, coordinates or a channel reference on the ground",
                "ADMINISTRATION -> check posts, patrols, crossings and settlement management",
                "WEAK POINTS -> a paper line never marked, and a defining feature that later moves",
            ],
            ["Four stages of boundary making", "Delimitation-demarcation gap"],
        ),
        panel(
            "Boundary classification matrix",
            "comparison-table",
            [
                "PHYSICAL FORM -> natural follows mountain, river, watershed, desert or sea",
                "PHYSICAL FORM -> geometric follows a straight or coordinate-based line",
                "GENESIS -> antecedent drawn before dense settlement; subsequent adjusted to it",
                "GENESIS -> superimposed cuts across existing fabric; relict survives in landscape",
                "RULE -> genesis predicts dispute type; neither form is intrinsically stable",
            ],
            ["Natural and geometric boundary types", "Genetic classification of boundaries", "Neither type is intrinsically stable"],
        ),
        panel(
            "Dispute-cause typology",
            "decision-tree",
            [
                "IF the parties agree on ownership but not alignment -> positional dispute",
                "IF the parties contest ownership of a named area -> territorial dispute",
                "IF the line is agreed but use across it is contested -> resource or functional dispute",
                "IF the line predates or cuts across settlement -> antecedent or superimposed problem",
                "IF the defining river or watershed moves -> geomorphic instability recalculates the line",
            ],
            ["Typology of dispute causes", "Delimitation-demarcation gap"],
        ),
        panel(
            "Frontier to boundary conversion",
            "causal-system",
            [
                "HISTORICAL FRONTIER -> broad transition zone administered with tolerated ambiguity",
                "STATE CONSOLIDATION -> a precise line becomes legally and militarily necessary",
                "CONVERSION -> ambiguity must be resolved into one agreed alignment",
                "FRICTION -> competing readings of the same terrain surface as claims",
                "LESSON -> many disputes begin at the moment a zone is asked to become a line",
            ],
            ["Frontier as zone, boundary as line", "Typology of dispute causes"],
        ),
        panel(
            "Classical lenses and their omissions",
            "comparison-table",
            [
                "HEARTLAND -> interior continental depth and overland access as the variable",
                "RIMLAND -> coastal transition belts around the Eurasian margin",
                "SEA POWER -> naval access, ports and sea lines of communication",
                "OMISSIONS -> air and space power, cyber and submarine cables, interdependence",
                "OMISSIONS -> non-state actors and nuclear deterrence; geography conditions, not determines",
            ],
            ["Classical geopolitical lenses", "What the classical theories omit"],
        ),
        panel(
            "India's dual strategic character",
            "comparison-table",
            [
                "CONTINENTAL SIDE -> mountain and plains frontier requiring land force and infrastructure",
                "MARITIME SIDE -> peninsular position astride major sea lanes with island territories",
                "CONSEQUENCE -> a genuine resource trade-off between the two theatres",
                "ANSWER MOVE -> recognise duality instead of assigning India to one school",
                "CAUTION -> avoid quoting boundary lengths or disputed areas from memory",
            ],
            ["India's dual strategic character", "What the classical theories omit"],
        ),
        panel(
            "Sector-by-terrain management framework",
            "comparison-table",
            [
                "HIGH-ALTITUDE GLACIATED -> inaccessibility, watershed ambiguity, costly infrastructure",
                "DENSELY POPULATED PLAINS -> fencing feasible but divides fields; smuggling dominates",
                "RIVERINE AND DELTAIC -> migrating channels, shifting char lands, fencing impossible",
                "FORESTED HILL -> cross-border ethnic continuity and traditional movement regimes",
                "DESERT AND MARITIME -> long-distance surveillance; zone delimitation and fishing friction",
            ],
            ["Sector-by-terrain management framework", "Why uniform instruments fail"],
        ),
        panel(
            "Differentiated border management fork",
            "decision-tree",
            [
                "SECTOR IDENTIFIED -> state terrain, settlement density and legal status of the line",
                "IF terrain and settlement differ across sectors -> uniform instruments will misfit",
                "IF hardening ignores local livelihoods -> alienation grows in the borderland",
                "THEREFORE -> combine infrastructure, surveillance and local economic integration",
                "AND -> keep force doctrine outside a geography answer; retain terrain-to-management logic",
            ],
            ["Why uniform instruments fail", "Border-force geographic mandates"],
        ),
        panel(
            "India neighbour adjacency grid",
            "comparison-table",
            [
                "LAND NEIGHBOURS -> Pakistan, China, Nepal, Bhutan, Bangladesh and Myanmar",
                "CLAIMED ADJACENCY -> Afghanistan through India's far north-west map position",
                "MARITIME NEIGHBOURS -> Sri Lanka across the Palk Strait and Gulf of Mannar",
                "MARITIME NEIGHBOURS -> Maldives across the Eight Degree Channel from Lakshadweep",
                "LAND BRIDGE -> Myanmar alone opens India into mainland South-East Asia",
            ],
            ["India's neighbour set", "Sector-by-terrain management framework"],
        ),
        panel(
            "Boundary-line category firewall",
            "institutional-ladder",
            [
                "RADCLIFFE LINE 1947 -> partition framework for the boundary with Pakistan",
                "McMAHON LINE 1914 FRAMEWORK -> eastern-sector India-China boundary claim",
                "DURAND LINE 1893 -> Afghanistan-Pakistan line, never an India-Pakistan line",
                "CEASEFIRE LINE 1949 TO LINE OF CONTROL 1972 -> military control, not sovereignty",
                "LINE OF ACTUAL CONTROL -> control reality over an undemarcated mountain frontier",
            ],
            ["High-yield boundary lines", "Category firewall for control lines"],
        ),
        panel(
            "Sectors, settlement chain and mandates",
            "process-flow",
            [
                "WESTERN SECTOR -> Ladakh, Karakoram and Aksai Chin space with watershed ambiguity",
                "MIDDLE AND EASTERN SECTORS -> Himachal and Uttarakhand; Sikkim and Arunachal",
                "LAND BOUNDARY AGREEMENT -> 1974 accord, 2011 Protocol, 2015 implementation",
                "SETTLEMENT EFFECT -> enclaves, adverse possessions and undemarcated stretches resolved",
                "MANDATES -> BSF, ITBP, SSB, Assam Rifles and Coast Guard mapped to terrain",
            ],
            ["India-China three-sector division", "Land Boundary Agreement chain", "Border-force geographic mandates"],
        ),
    ],
    [
        "frontier",
        "delimitation",
        "demarcation",
        "superimposed",
        "Radcliffe Line",
        "McMahon Line",
        "Durand Line",
        "Line of Actual Control",
        "Land Boundary Agreement",
        "enclave",
    ],
    (
        "The audited routing ledgers consulted for this build assign no direct Mains PYQ to Geography "
        "Topic 35. The topic does own routed Prelims demand, including the 2018 longitude-proximity "
        "question on Indian cities, the 2020 Siachen Glacier location question, the 2022 Himalayan "
        "peak-location matching question, the 2024 west-to-east sequence of Himalayan tributaries of "
        "the Ganga and the 2026 question on state boundaries, international borders and interstate "
        "adjacency. Those entries are recorded in the ledgers as objective questions whose official "
        "keys are either unavailable locally or deliberately not inferred, so this package reproduces "
        "no option letter or answer key and fabricates no direct solved PYQ card."
    ),
    [],
    [
        "https://www.mea.gov.in/",
        "https://www.mha.gov.in/",
        "https://surveyofindia.gov.in/",
        "https://pib.gov.in/",
    ],
    (
        "The dated official linkages used are deliberately narrow. The India-Bangladesh Land Boundary "
        "Agreement chain of 1974, the 2011 Protocol and the 2015 implementation with its 6 June "
        "exchange of letters and 31 July appointed day is taken from the Ministry of External Affairs "
        "material recorded in the repository owner. The Press Information Bureau release of 7 July "
        "2025 on the Kaladan Multi-Modal Transit Transport Project is retained only to illustrate "
        "that a boundary is accompanied by a wider frontier of hills, rivers, roads, ports and "
        "communities. No boundary length, number of border districts, disputed area in square "
        "kilometres, patrol figure or claimed alignment is stated from memory, and the legal status "
        "of any disputed sector is left to cited official sources."
    ),
)

TOPIC_36 = common.topic(
    36,
    "Contemporary Geographical Issues (India)",
    "36_Contemporary-Geographical-Issues-India.md",
    "36_Contemporary-Geographical-Issues-India.md",
    "36_Contemporary-Geographical-Issues-India_Complete-Topic-Package.md",
    [
        (
            "What makes an issue geographical",
            "An issue becomes geographical when location, terrain, climate, water, settlement pattern, resource distribution or connectivity directly shapes the problem, so the answer must establish where it occurs, why there rather than elsewhere, and with what spatial consequence.",
        ),
        (
            "The six issue-lenses",
            "The reusable lenses are resource conflict over water, minerals, forests and coasts, boundary and borderland clustering, hazard and vulnerability exposure on floodplains, coasts and slopes, mobility and migration under stress or opportunity, urban primacy overwhelming drainage and land markets, and ecological fragility where development enters islands, wetlands, deltas and mountains.",
        ),
        (
            "The simple analytical chain",
            "Resource, climate or terrain stress leads to uneven access or exposure, which produces social conflict or governance pressure, which generates spatial spillover through migration, flooding, erosion or corridor shift, which then invites a policy response.",
        ),
        (
            "Standing issue families",
            "The families that recur regardless of the year's headlines are water stress and allocation, climate-linked hazard change, land degradation and land-use conflict, urbanisation stress, regional imbalance and migration pressure, resource and energy transition, infrastructure and ecology trade-offs, coastal and island pressure, and boundary and transboundary questions.",
        ),
        (
            "Nine-step analytical chain",
            "Any unfamiliar issue can be analysed by naming the process, establishing the pattern, separating drivers, fixing the scale, identifying exposure, distinguishing vulnerability, naming the trade-off, matching the instrument to the mechanism, and closing with a graded verdict.",
        ),
        (
            "Exposure against vulnerability",
            "Exposure asks who and what lies in the way of a hazard, while vulnerability asks why the same hazard hurts some groups far more, and collapsing the two is one of the most common analytical failures.",
        ),
        (
            "Refusal of single-cause attribution",
            "Natural variability and human amplification must be separated rather than merged, because most contemporary geographical problems are the joint product of a physical process and a land-use or governance decision.",
        ),
        (
            "Scale-mismatch insight",
            "The geography of a problem frequently fails to match the administrative unit expected to solve it, and naming that mismatch is the most frequently available and least frequently used insight in these answers.",
        ),
        (
            "Groundwater worked case",
            "Groundwater decline in an intensively irrigated plain is abstraction exceeding recharge in an alluvial aquifer, concentrated where tube-well density, water-intensive cropping and assured procurement coincide rather than simply where rainfall is low, operating at aquifer scale that matches no administrative boundary, and hurting smallholders first because they cannot finance deeper wells.",
        ),
        (
            "Urban flooding worked case",
            "Recurrent urban flooding is runoff generation exceeding drainage conveyance, concentrated in low-lying areas, filled tanks and wetlands and encroached natural drains, driven by surface sealing, undersized silted networks and floodplain construction, and operating at catchment scale that typically extends beyond the municipal boundary, so rainfall is the trigger rather than the cause.",
        ),
        (
            "Five current-material confusions",
            "Most factual errors in current-affairs answers are one of five confusions: a forecast taken for an observation, a projection for a measurement, a survey for a census, an announcement for an implementation, and a target for an achievement.",
        ),
        (
            "Core-independence rule",
            "A current example must illustrate a process already taught in a core file, so that if the example is removed the answer still stands; core content must never become dependent on current material.",
        ),
        (
            "Peninsular against Himalayan river questions",
            "Peninsular river disputes differ from Himalayan river questions because storage capacity, monsoon timing, delta requirements and irrigation command areas matter differently in the two settings.",
        ),
        (
            "Krishna basin geography",
            "The Krishna question is a basin-management problem in which upstream storage and timed release shape downstream availability, the basin spreads across Maharashtra, Karnataka, Telangana and Andhra Pradesh, irrigation command areas depend on predictable release windows, lower riparians fear reduced seasonal flow, and bifurcation changed basin administration itself.",
        ),
        (
            "Great Nicobar development tension",
            "Great Nicobar matters because proximity to major east-west sea routes and the Malacca-facing arc sits inside a fragile island system of coral coast, tribal habitat, seismicity and coastal regulation, so strategic geography and fragile-island geography have to be written together.",
        ),
        (
            "North-east corridor fragility",
            "The north-east combines narrow mainland access, folded hill terrain, heavy monsoon, young unstable slopes and multiple international frontiers, so every road, rail or multimodal corridor is simultaneously a development project and a geomorphic risk problem, and Bay of Bengal access is sought precisely to bypass the narrow mainland hinge.",
        ),
        (
            "Urban flooding factor set",
            "Wetland and lake loss reduces storage and spill space, impervious surface growth raises runoff speed and volume, encroached drainage channels block discharge pathways, floodplain construction places assets directly in hazard space, and short-duration intense rainfall exposes the weakness of built drainage design.",
        ),
        (
            "Connectivity-hazard caveat",
            "Connectivity does not automatically reduce regional vulnerability, because in mountains and borderlands badly sited roads and corridors can deepen slope instability, forest fragmentation and sediment risk.",
        ),
        (
            "Krishna tribunal current anchor",
            "A Press Information Bureau and Lok Sabha written reply dated 21 August 2025 recorded continued relevance and term extension of the Krishna Water Disputes Tribunal after the complex post-bifurcation situation, showing how one peninsular basin produces repeated upper-lower riparian conflict.",
        ),
        (
            "Urban flooding current anchor",
            "The Press Information Bureau release on urban flooding during the monsoon season, dated 29 July 2024, stresses that urban flooding is not only about rainfall but about urban planning, storm-water drains, land use and water-body management, and cites storm-water and water-body interventions under AMRUT.",
        ),
    ],
    [
        "Do not treat every geography current-affairs item as environmental; many concern location, access and regional inequality.",
        "Do not explain a river dispute as purely legal and omit basin geometry and upstream-downstream structure.",
        "Do not attribute urban flooding to heavy rainfall alone.",
        "Do not merge exposure and vulnerability into one idea.",
        "Do not offer a single-cause attribution for a compound physical and human problem.",
        "Do not ignore the mismatch between the problem's scale and the administrative unit expected to act.",
        "Do not assume connectivity automatically reduces vulnerability in mountains and borderlands.",
        "Do not treat a forecast as an observation, a projection as a measurement or a target as an achievement.",
        "Do not use a survey estimate as if it were a census count.",
        "Do not build a core answer that collapses when the current example is removed.",
        "Do not summarise the news instead of naming the process and the pattern.",
        "Do not offer a generic way-forward list instead of instruments matched to the identified mechanism.",
        "Do not quote rainfall totals, groundwater levels, project outlays, tribunal allocations or flooded-area figures from memory.",
        "Do not convert an unkeyed routed Prelims question into a solved answer with an invented key.",
    ],
    [
        (
            10,
            "Explain what makes a development problem a geographical issue rather than a general policy problem.",
            "A problem becomes geographical when its location, terrain, water, settlement pattern or connectivity materially shapes it, so the answer must establish where it occurs, why there and with what spatial consequence before any policy discussion.",
            [0, 1, 2, 3],
        ),
        (
            10,
            "Distinguish exposure from vulnerability and show why the distinction changes the policy instrument chosen.",
            "Exposure identifies who and what lies in a hazard's path while vulnerability explains why the same hazard hurts some groups far more, so a distributional remedy is required alongside a physical one.",
            [4, 5, 6, 9],
        ),
        (
            15,
            "Discuss how upstream storage, command areas and inter-state basin spread shape the geography of a peninsular river-sharing dispute.",
            "A peninsular basin dispute is governed by storage location, timed release and command-area dependence across several states, so basin geometry and administrative reorganisation determine outcomes that legal allocation alone cannot settle.",
            [12, 13, 7, 18],
        ),
        (
            15,
            "Examine why projects on fragile island and hill-frontier sites are simultaneously strategic initiatives and ecological risk questions.",
            "Sites that gain value from route proximity or frontier position are frequently the same sites whose coral, forest, slope and seismic conditions make development risky, so the honest answer names the trade-off rather than assuming it away.",
            [14, 15, 17, 3],
        ),
        (
            20,
            "Is recurrent urban flooding in Indian cities primarily a rainfall problem or a land-use problem? Analyse.",
            "Rainfall is the trigger while surface sealing, wetland loss, drainage encroachment and floodplain construction are the causes, and because the catchment extends beyond municipal limits the problem is also a scale-mismatch failure rather than a purely civic one.",
            [9, 16, 7, 19],
        ),
        (
            20,
            "Construct a reusable framework for analysing any unfamiliar contemporary geographical issue and defend each step.",
            "The nine-step chain works because it forces the process and pattern to be established before policy, separates natural from human drivers, keeps exposure distinct from vulnerability, names the real trade-off, and matches the instrument to the mechanism rather than to a generic list.",
            [4, 5, 6, 10],
        ),
    ],
    [
        plan(
            "What makes an issue geographical",
            [0],
            "Where, why there and with what consequence must be answered first.",
            "Open by proving the issue is spatial before describing any event.",
        ),
        plan(
            "The six issue-lenses",
            [1],
            "Choose the lens the question actually engages.",
            "Name the operative lens instead of applying all six mechanically.",
        ),
        plan(
            "The simple stress-to-response chain",
            [2],
            "An issue is neither only political nor only environmental.",
            "Follow the chain from stress to spillover to policy response.",
        ),
        plan(
            "Standing issue families that outlive headlines",
            [3],
            "The family survives even when the example dates.",
            "Route an unfamiliar issue into a family before analysing it.",
        ),
        plan(
            "The nine-step analytical chain",
            [4],
            "Process and pattern must precede any policy discussion.",
            "Use the nine steps as the spine of every contemporary-issue answer.",
        ),
        plan(
            "Exposure against vulnerability",
            [5],
            "Exposure is physical position; vulnerability is differential capacity.",
            "Separate the two and derive a distributional remedy from vulnerability.",
        ),
        plan(
            "Refusing single-cause attribution",
            [6],
            "Natural variability and human amplification operate together.",
            "State both driver classes before assigning any causal weight.",
        ),
        plan(
            "Scale mismatch as the decisive insight",
            [7],
            "Problem geography rarely matches the administrative unit.",
            "Name the governing scale and the unit expected to act on it.",
        ),
        plan(
            "Worked case one: groundwater decline in an irrigated plain",
            [8],
            "The pattern follows cropping and procurement, not rainfall alone.",
            "Trace abstraction, aquifer scale and distributional loss in one chain.",
        ),
        plan(
            "Worked case two: recurrent flooding in a growing city",
            [9],
            "Rainfall is the trigger; land use is the cause.",
            "Move from conveyance failure to catchment scale and tenure-linked remedies.",
        ),
        plan(
            "Discipline for using current material",
            [10, 11],
            "A target is not an achievement and a survey is not a census.",
            "Date and attribute every current claim, and keep the core answer independent.",
        ),
        plan(
            "Peninsular basin geography and the Krishna question",
            [12, 13],
            "Basin geometry constrains what legal allocation can deliver.",
            "Explain storage, release timing and command dependence before allocation shares.",
        ),
        plan(
            "Great Nicobar and the fragile-edge trade-off",
            [14],
            "Route advantage and ecological fragility occupy the same site.",
            "Write strategic geography and island fragility together, not in sequence.",
        ),
        plan(
            "North-east corridors and geomorphic risk",
            [15, 17],
            "Badly sited connectivity can deepen hazard instead of reducing it.",
            "Pair corridor benefit with slope, forest and sediment risk in one verdict.",
        ),
        plan(
            "Urban drainage factors and the dated official anchors",
            [16, 18, 19],
            "Anchors must be dated, attributed and kept illustrative.",
            "Close with drainage factors bounded by two dated official releases.",
        ),
    ],
    [
        panel(
            "Is it a geographical issue",
            "decision-tree",
            [
                "ASK WHERE -> can the problem be located on a basin, coast, slope or corridor",
                "ASK WHY THERE -> does terrain, climate, water or connectivity explain the location",
                "ASK SO WHAT -> is there a spatial consequence such as migration, flooding or erosion",
                "IF all three answer yes -> it is a geographical issue and the chain applies",
                "IF only the policy dispute is present -> it is a governance question, not a spatial one",
            ],
            ["What makes an issue geographical", "The simple analytical chain"],
        ),
        panel(
            "Six issue-lenses",
            "institutional-ladder",
            [
                "RESOURCE CONFLICT -> control of water, minerals, forests and coasts",
                "BORDERLAND -> clustering near a frontier, gateway or corridor",
                "HAZARD AND VULNERABILITY -> floodplain, coast, hill slope and seismic exposure",
                "MOBILITY AND URBAN PRIMACY -> stress migration; drainage and land-market overload",
                "ECOLOGICAL FRAGILITY -> coral island, wetland, delta and mountain ecosystems",
            ],
            ["The six issue-lenses", "Standing issue families"],
        ),
        panel(
            "Stress to policy chain",
            "process-flow",
            [
                "RESOURCE, CLIMATE OR TERRAIN STRESS -> the initiating physical condition",
                "UNEVEN ACCESS OR EXPOSURE -> the stress falls unequally across space and groups",
                "CONFLICT OR GOVERNANCE PRESSURE -> contestation becomes visible",
                "SPATIAL SPILLOVER -> migration, flooding, erosion or corridor shift follows",
                "POLICY RESPONSE -> instruments arrive, usually after the spillover",
            ],
            ["The simple analytical chain", "What makes an issue geographical"],
        ),
        panel(
            "Nine-step analytical spine",
            "process-flow",
            [
                "PROCESS AND PATTERN -> name the process, then explain why there and not elsewhere",
                "DRIVERS AND SCALE -> separate natural from human; fix local, regional or transboundary",
                "EXPOSURE AND VULNERABILITY -> who is in the way; why the same hazard hurts unequally",
                "TRADE-OFF -> name the genuine competing interest that always exists",
                "INSTRUMENT AND VERDICT -> match the remedy to the mechanism, then grade the conclusion",
            ],
            ["Nine-step analytical chain", "Exposure against vulnerability", "Scale-mismatch insight"],
        ),
        panel(
            "Exposure and vulnerability separated",
            "comparison-table",
            [
                "EXPOSURE -> population, assets and livelihoods physically in the hazard path",
                "VULNERABILITY -> capacity to absorb, cope and recover from the same hazard",
                "GROUNDWATER CASE -> smallholders lose access first because deeper wells need finance",
                "FLOOD CASE -> informal housing without insurance or alternative shelter bears the loss",
                "IMPLICATION -> physical protection alone leaves the distributional problem untouched",
            ],
            ["Exposure against vulnerability", "Groundwater worked case", "Urban flooding worked case"],
        ),
        panel(
            "Scale mismatch rail",
            "causal-system",
            [
                "AQUIFER SCALE -> matches no administrative boundary in an irrigated plain",
                "CATCHMENT SCALE -> extends beyond the municipal limit of a flooding city",
                "BASIN SCALE -> crosses several states in a peninsular river dispute",
                "CONSEQUENCE -> the unit expected to act cannot govern the whole process",
                "ANSWER MOVE -> name the mismatch explicitly; it is the least used available insight",
            ],
            ["Scale-mismatch insight", "Groundwater worked case", "Krishna basin geography"],
        ),
        panel(
            "Groundwater decline worked chain",
            "process-flow",
            [
                "PROCESS -> abstraction exceeds recharge in an alluvial aquifer",
                "PATTERN -> tube-well density, water-intensive cropping and assured procurement coincide",
                "DRIVERS -> cropping pattern, energy pricing, procurement geography, rainfall variability",
                "BURDEN -> smallholders unable to finance deeper wells lose access first",
                "INSTRUMENT -> demand-side crop and energy reform with managed recharge at aquifer scale",
            ],
            ["Groundwater worked case", "Scale-mismatch insight"],
        ),
        panel(
            "Urban flooding worked chain",
            "process-flow",
            [
                "PROCESS -> runoff generation exceeds drainage conveyance capacity",
                "PATTERN -> low-lying land, filled tanks and wetlands, encroached natural drains",
                "DRIVERS -> surface sealing, undersized silted networks, floodplain construction",
                "TRADE-OFF -> protecting drains and floodplains forgoes valuable developable land",
                "INSTRUMENT -> drainage restoration, blue-green infrastructure and tenure-backed relocation",
            ],
            ["Urban flooding worked case", "Urban flooding factor set"],
        ),
        panel(
            "Current-material discipline",
            "comparison-table",
            [
                "FORECAST vs OBSERVATION -> a prediction is not a recorded measurement",
                "PROJECTION vs MEASUREMENT -> a model output is not an instrument reading",
                "SURVEY vs CENSUS -> a sample estimate is not an enumerated count",
                "ANNOUNCEMENT vs IMPLEMENTATION -> approval is not delivery on the ground",
                "TARGET vs ACHIEVEMENT -> a stated goal is never a completed outcome",
            ],
            ["Five current-material confusions", "Core-independence rule"],
        ),
        panel(
            "Peninsular basin dispute geography",
            "causal-system",
            [
                "UPSTREAM STORAGE -> reservoir location and timed release govern downstream availability",
                "INTER-STATE SPREAD -> Maharashtra, Karnataka, Telangana and Andhra Pradesh all matter",
                "COMMAND AREAS -> irrigated agriculture depends on predictable release windows",
                "LOWER BASIN -> delta and lower-riparian needs fear reduced seasonal flow",
                "ADMINISTRATION -> bifurcation reorganised the basin's management, not its geometry",
            ],
            ["Krishna basin geography", "Peninsular against Himalayan river questions"],
        ),
        panel(
            "Fragile-edge development trade-off",
            "comparison-table",
            [
                "GREAT NICOBAR ADVANTAGE -> proximity to east-west routes and the Malacca-facing arc",
                "GREAT NICOBAR CONSTRAINT -> coral coast, tribal habitat, seismicity, coastal regulation",
                "NORTH-EAST ADVANTAGE -> Bay of Bengal access bypassing the narrow mainland hinge",
                "NORTH-EAST CONSTRAINT -> folded slopes, heavy monsoon, landslides, forest fragmentation",
                "RULE -> route value and ecological fragility occupy the same site, so name the trade-off",
            ],
            ["Great Nicobar development tension", "North-east corridor fragility", "Connectivity-hazard caveat"],
        ),
        panel(
            "Dated official anchors and their boundary",
            "institutional-ladder",
            [
                "21 AUG 2025 -> PIB and Lok Sabha reply on continued Krishna tribunal relevance",
                "29 JUL 2024 -> PIB release on urban flooding during the monsoon season",
                "READING -> both anchors illustrate processes already owned by core files",
                "AMRUT -> storm-water and water-body interventions cited in the flooding release",
                "BOUNDARY -> no allocation share, rainfall total or outlay is quoted from memory",
            ],
            ["Krishna tribunal current anchor", "Urban flooding current anchor", "Core-independence rule"],
        ),
    ],
    [
        "exposure",
        "vulnerability",
        "scale",
        "aquifer",
        "managed recharge",
        "Krishna",
        "Great Nicobar",
        "floodplain",
        "AMRUT",
        "catchment",
    ],
    (
        "Geography Topic 36 owns direct Mains PYQ demand in the audited routing ledgers. Three GS-I "
        "demands are routed to this owner: 2019 Q14 on water stress and its regional variation within "
        "India, 2023 Q5 on the crisis of availability of and access to freshwater resources, and "
        "2024 Q14 on the declining groundwater of the Gangetic valley and food security. All three "
        "are answered below as original model solutions built only from owner evidence. Routed "
        "Prelims demands for this topic remain recorded in the ledgers as objective questions whose "
        "official keys are either unavailable locally or deliberately not inferred, so no option "
        "letter or answer key is reproduced anywhere in this package."
    ),
    [
        (
            "2019",
            "GS-I Q14 (What is, how and why, 15 marks, 250 words)",
            "Explain what water stress is, how and why it varies regionally within India.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. The wording is the ledger's neutral rendering, not reproduced official paper text.",
            "Thesis: water stress is a mismatch between demand and dependable supply at a given place and time, and it varies regionally within India because the physical supply regime, the demand structure and the governing scale differ from one region to another. Define the term precisely first: stress is not the same as absolute scarcity, since a well-watered region with concentrated abstraction and poor quality management can be stressed while a drier region with modest demand is not. Then explain the physical variation. Rainfall regime, its reliability rather than its average, monsoon timing, storage possibility, aquifer character and the difference between peninsular and Himalayan basins in storage, timing, delta requirement and command dependence all vary systematically across the country. Next explain the human amplification, refusing single-cause attribution: tube-well density, water-intensive cropping and assured procurement concentrate abstraction in specific plains; urban surface sealing and wetland loss reduce recharge while raising demand; and industrial and thermal demand adds a further competing claim. Apply the scale insight, which lifts the answer: aquifers and catchments match no administrative boundary, so the unit expected to solve stress rarely governs the process producing it. Keep exposure distinct from vulnerability, since smallholders unable to finance deeper wells and informal urban households without dependable supply bear the loss first. Name the trade-off honestly: crop diversification and pricing reform reduce abstraction but conflict with assured procurement and farm incomes. Conclude in graded terms: regional variation in water stress is a compound of hydrological endowment, cropping and energy incentives, urban land use and governance scale, and only demand-side and aquifer-scale instruments can address it. Quote no groundwater level, rainfall total or allocation figure from memory.",
        ),
        (
            "2023",
            "GS-I Q5 (Why is the world confronted, 10 marks, 150 words)",
            "Explain why the world is increasingly confronted with a crisis of availability of and access to freshwater resources.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic. Only the ledger's neutral rendering is used.",
            "Thesis: the freshwater crisis is one of availability and access together, and treating it as availability alone is the standard error. Availability is constrained physically because usable freshwater is a small and unevenly distributed fraction of total water, because its supply depends on rainfall reliability rather than long-run averages, and because storage in surface reservoirs, snow and ice and aquifers is being drawn down faster than it is replenished in many regions. Access is constrained separately, because water reaches people through infrastructure, entitlement, price and institutions, so two households in the same basin can face entirely different effective supplies. Add the amplifiers without collapsing them into one cause: rising and shifting demand from irrigation, cities and industry; land-use change that seals surfaces, removes wetlands and reduces recharge; quality failure that removes water from usable supply even when it is physically present; and hazard change that alters both extremes. Apply the scale point, since aquifers, catchments and transboundary basins seldom coincide with the administrative unit expected to act. Conclude with a graded verdict: the crisis is real but not uniform, and it is more accurately described as a distributional and governance failure layered over a genuine physical limit than as a simple global shortage.",
        ),
        (
            "2024",
            "GS-I Q14 (Explain, 15 marks, 250 words)",
            "Explain the declining groundwater of the Gangetic valley and its implications for food security.",
            "Verified routed demand from the audited Mains routing ledger for 2024-2025, routed to this owner as the owning topic. No official answer key exists for a Mains question, and none is implied.",
            "Thesis: groundwater decline in the Gangetic alluvium is abstraction exceeding recharge in a highly productive aquifer, and because the same aquifer underpins a national foodgrain surplus, the decline converts a hydrological process directly into a food-security question. Establish the process first, then the pattern, and note that the pattern is decisive: depletion concentrates where tube-well density, water-intensive cropping and assured procurement coincide, not simply where rainfall is lowest, which is why the map of decline does not follow the map of aridity. Separate the drivers rather than merging them: cropping pattern and the water intensity it implies, energy pricing that lowers the marginal cost of pumping, procurement geography that stabilises the incentive to grow those crops, and rainfall variability that shifts recharge between years. Fix the scale, since the alluvial aquifer is a continuous body matching no administrative boundary, so district or state action alone cannot govern the process. Distinguish exposure from vulnerability: the exposed asset is a surplus-producing agricultural region, but the first losers are smallholders who cannot finance deeper wells or higher pumping costs, so the burden is distributional before it is national. Draw the food-security implication carefully in three layers: rising extraction cost and falling well yields raise the cost of the same output; quality deterioration in some depleted settings removes water from usable supply; and any abrupt correction transfers risk to the very producers whose surplus the system relies on. Name the trade-off: diversification and pricing reform reduce abstraction but conflict with assured procurement and farm incomes. Conclude in graded terms that the decline is stabilisable through demand-side crop and energy reform, managed recharge and conjunctive use at aquifer scale, while refusing any remembered figure for water table, extraction or production.",
        ),
    ],
    [
        "https://pib.gov.in/",
        "https://jalshakti-dowr.gov.in/",
        "https://cgwb.gov.in/",
        "https://mohua.gov.in/",
    ],
    (
        "Two dated official anchors are used and nothing more. The Press Information Bureau and Lok "
        "Sabha written reply of 21 August 2025 is used only to record continued relevance and term "
        "extension of the Krishna Water Disputes Tribunal after the post-bifurcation situation, with "
        "no allocation share stated. The Press Information Bureau release on urban flooding during "
        "the monsoon season, dated 29 July 2024, is used only for its framing that urban flooding "
        "involves planning, storm-water drains, land use and water-body management, together with its "
        "reference to storm-water and water-body interventions under AMRUT. No rainfall total, "
        "groundwater level, flooded-area figure, project outlay or tribunal allocation is quoted from "
        "memory, and every anchor illustrates a process that the core files already own."
    ),
)

TOPIC_37 = common.topic(
    37,
    "Cultural and Social Geography of India",
    "37_Cultural-and-Social-Geography-of-India.md",
    "37_Cultural-and-Social-Geography-of-India.md",
    "37_Cultural-and-Social-Geography-of-India_Complete-Topic-Package.md",
    [
        (
            "Scope of cultural and social geography",
            "Cultural geography studies how language, religion, ethnicity, livelihood, settlement and identity vary across space, with the source text treating language and religion as major bases for demarcating cultural regions, while social geography asks how those identities interact with class, caste, tribe, migration, urbanisation and state policy in real space.",
        ),
        (
            "Building blocks of a cultural region",
            "A cultural region is built from language as a communication and literary core, religion as sacred sites and group identity, tribe and ethnicity linked to habitat, livelihood as the cultural landscape of work, migration as diffusion and mixing, and state policy through linguistic states, schedules, autonomy and reservation.",
        ),
        (
            "Three types of cultural region",
            "A formal cultural region rests on a dominant shared trait such as language or religion, a functional cultural region is tied together by interaction through pilgrimage, market or media networks, and a vernacular or perceived region is one people imagine and name, such as the Hindi belt, the Deccan or the North-East.",
        ),
        (
            "Diffusion and overlap sequence",
            "The standard sequence runs from a cultural hearth through diffusion to an overlap zone, then a mixed borderland and finally a new regional identity, and examiners test the overlap zone far more often than the core.",
        ),
        (
            "Transition-zone principle",
            "Cultural regions have cores that are clear and margins that are mixed, so linguistic border districts, bilingual belts, syncretic traditions and contested regional identities all live in the margin rather than the core.",
        ),
        (
            "Distribution against density",
            "Distribution describes where people are as a spatial arrangement, while density is a ratio of people to area, so the two are not synonyms and a question naming both expects both to be answered.",
        ),
        (
            "Three densities and their meanings",
            "Arithmetic density divides total population by total area and misleads where much of the area is uninhabitable, physiological density divides population by cultivable area and reveals pressure hidden by arithmetic figures, and agricultural density divides the agricultural population by cultivable area to isolate farming pressure.",
        ),
        (
            "Controls on India's population distribution",
            "Population distribution is controlled by relief permitting cultivation and transport, soil depth and renewability, water availability from rainfall, perennial rivers and shallow groundwater, growing-season climate, historical continuity of settlement and state formation, economic opportunity in industry, ports and irrigated commands, and connectivity through rail, road, port and canal networks.",
        ),
        (
            "Ganga basin convergence of controls",
            "The Ganga basin is the standard worked case because every control reinforces the same outcome: an extensive level alluvial plain, deep renewable alluvium with annually renewed khadar tracts, perennial snow-fed and rain-fed rivers, shallow highly productive alluvial aquifers, adequate monsoon rainfall increasing eastward, long historical continuity of settlement, urbanism and trade, and a dense transport network on level ground.",
        ),
        (
            "Ganga basin internal variation",
            "The basin is not uniform: density rises broadly from the drier west toward the wetter middle and lower basin, the tarai and northern fringe face different constraints from the central plain, the deltaic and flood-prone lower basin combines extremely high rural density with recurrent flood and erosion risk, and urban-industrial nodes produce density peaks that agriculture does not explain at all.",
        ),
        (
            "Density consequence chain",
            "Very high physiological density produces small and fragmenting holdings, small holdings limit the surplus available for investment, land pressure drives groundwater over-abstraction and out-migration, settlement on the active floodplain raises flood exposure, and the same fertility makes the region nationally critical for foodgrain supply, so a regional resource constraint becomes a national food-security question.",
        ),
        (
            "Density-poverty qualification",
            "High density is not the same as poverty, because the basin's difficulties follow from the combination of density with a still largely agrarian employment structure and limited non-farm absorption, and densely populated industrialised regions elsewhere show that the relationship is conditional.",
        ),
        (
            "Micro-relief belt sequence",
            "Away from the mountain front the plain shows a fixed sequence: the porous bhabar of coarse gravel where streams disappear underground, the marshy terai where they re-emerge, the older bhangar upland above the flood limit often carrying kankar nodules, the newer khadar of the active floodplain renewed by deposition, and the active channel belt of levees, bars, ox-bow lakes and char or diara lands.",
        ),
        (
            "Two gradients of the Northern Plain",
            "Two gradients cut across the plain: rainfall rises markedly from the drier north-west toward the humid east and the Brahmaputra valley, producing irrigation-dependent wheat and rabi cultivation in the west against rainfall-sufficient rice and kharif cultivation in the east, and a north-to-south transect from the mountain front reproduces the micro-relief sequence everywhere.",
        ),
        (
            "Northern Plain sub-regions",
            "The plain resolves into a western plain of canal and tube-well irrigated cereal cultivation with water-table drawdown, a central plain of high cropping intensity with severe holding fragmentation, an eastern plain that is water-rich yet productivity-constrained by low gradient and poor drainage, a Brahmaputra valley of braided-channel flood and erosion insecurity, and a deltaic tract facing tidal influence, saline intrusion and cyclone exposure.",
        ),
        (
            "Language as core and transition",
            "Linguistic geography works as broad regional core areas separated by transition zones with pockets sustained by relief and isolation, and although linguistic reorganisation aligned administrative with linguistic space, transition zones and minority pockets mean no boundary is a clean linguistic line.",
        ),
        (
            "Religion as functional geography",
            "Religious geography is functional as well as formal, because regional concentrations coexist with pilgrimage networks and sacred landscapes that create interaction regions cutting across the formal ones, and religion therefore shapes settlement and everyday resource use rather than belief alone.",
        ),
        (
            "Tribe and habitat association",
            "Tribal populations show a strong association with forested hill and plateau tracts and with the north-east, but the association is historical and political rather than natural, since it reflects relative isolation from plains state formation, and saying so avoids an environmentally deterministic answer.",
        ),
        (
            "Migration as continuous redistribution",
            "Migration and diaspora redistribute culture continuously through corridor-based communities in destination cities and overseas communities drawn from specific source regions, which makes metropolitan cities the principal mixing zones of Indian cultural geography.",
        ),
        (
            "Vulnerable-community mapping anchor",
            "The Ministry of Tribal Affairs state-wise list of Particularly Vulnerable Tribal Groups, dated 9 July 2024, shows that cultural and social geography is not merely historical description, because the state continues to map highly vulnerable communities region by region for policy purposes.",
        ),
    ],
    [
        "Do not treat distribution and density as synonyms when a question names both.",
        "Do not rely on arithmetic density where much of the area is uninhabitable; name physiological density.",
        "Do not assume a cultural region must coincide with a state boundary.",
        "Do not reduce religious geography to belief and omit settlement, pilgrimage and resource use.",
        "Do not treat linguistic geography as one majority language and ignore transition zones and minority pockets.",
        "Do not present the tribe-habitat association as natural determinism rather than historical and political isolation.",
        "Do not describe the Northern Plain as a single agricultural or hydrological region.",
        "Do not swap bhabar, terai, bhangar, khadar and the active channel belt.",
        "Do not equate high density with poverty; the relationship is conditional on employment structure.",
        "Do not treat the Ganga basin as internally uniform in density or risk.",
        "Do not quote density figures, state populations, decadal growth rates, urbanisation shares, literacy rates, sex ratios, language speaker counts, or religious or tribal population shares from memory.",
        "Do not use a post-census survey estimate as if it were a census count; attribute any newer figure to a named survey with its date.",
        "Do not answer a cultural-geography question with a list of regions instead of cores and transition zones.",
        "Do not convert an unkeyed routed Prelims question into a solved answer with an invented key.",
    ],
    [
        (
            10,
            "Distinguish arithmetic, physiological and agricultural density and explain which of them best reveals pressure on land.",
            "The three ratios measure different denominators, so physiological density best exposes pressure on cultivable land and explains why a sparsely settled mountain or desert state can conceal intense pressure in its habitable pockets.",
            [5, 6, 7, 10],
        ),
        (
            10,
            "Explain why cultural regions must be read through cores and transition zones rather than as a list of regions.",
            "Cores are clear and margins are mixed, so linguistic border districts, bilingual belts and syncretic traditions all occur in the margin, and an answer organised around cores and transitions explains contestation that a regional list cannot.",
            [2, 3, 4, 15],
        ),
        (
            15,
            "Critically examine the view that the Northern Plain of India is a uniform region.",
            "The plain is a single structural unit of alluvium filling one foredeep, but two gradients and a fixed micro-relief sequence subdivide it agriculturally and hydrologically, so uniformity holds in structure and relief while failing in agrarian and water terms.",
            [8, 12, 13, 14],
        ),
        (
            15,
            "Explain how language, religion and tribal habitat become spatial markers of identity in India.",
            "Each marker generates a distinct spatial form, since language produces cores with transition zones, religion produces both concentrations and pilgrimage-linked functional regions, and tribal distribution reflects historical isolation from plains state formation rather than natural determinism.",
            [0, 15, 16, 17],
        ),
        (
            20,
            "Assess the proposition that very high rural density in the Ganga basin converts a regional resource constraint into a national problem.",
            "Fragmenting holdings, limited investable surplus, groundwater over-abstraction, floodplain exposure and out-migration together tie the basin's local pressures to national foodgrain supply, but the outcome is conditional on employment structure rather than density alone.",
            [7, 8, 9, 10],
        ),
        (
            20,
            "Analyse how migration and metropolitan mixing are reshaping India's cultural map without erasing its regional cores.",
            "Migration continuously redistributes cultural traits into corridor-based urban communities while regional cores persist through language, religion, livelihood and habitat, so the map is being layered rather than homogenised.",
            [0, 3, 18, 19],
        ),
    ],
    [
        plan(
            "What cultural and social geography study",
            [0],
            "Social geography prevents cultural geography from becoming folklore.",
            "State both scopes before naming any marker or region.",
        ),
        plan(
            "Building blocks of a cultural region",
            [1],
            "State policy is a building block, not an external factor.",
            "Assemble a region from markers rather than describing a place.",
        ),
        plan(
            "Formal, functional and perceived regions",
            [2],
            "A pilgrimage circuit is functional, not formal.",
            "Name the region type before analysing its boundary.",
        ),
        plan(
            "Diffusion, overlap zones and mixed borderlands",
            [3, 4],
            "The examinable material sits at the margin, not the core.",
            "Build the answer around cores and transition zones together.",
        ),
        plan(
            "Distribution against density",
            [5],
            "A ratio is not an arrangement.",
            "Answer both halves whenever a question names distribution and density.",
        ),
        plan(
            "The three densities",
            [6],
            "Arithmetic density hides pressure in habitable pockets.",
            "Introduce physiological density as the high-value analytical move.",
        ),
        plan(
            "Controls on India's population distribution",
            [7],
            "Economic and historical controls act alongside physical ones.",
            "Order the controls before locating any dense or sparse region.",
        ),
        plan(
            "The Ganga basin as the worked case",
            [8],
            "Every control reinforces the same outcome in this basin.",
            "Explain convergence of controls rather than listing basin features.",
        ),
        plan(
            "Internal variation within the basin",
            [9],
            "Urban-industrial peaks are not explained by agriculture.",
            "Add west-east, fringe, deltaic and urban variation to any basin answer.",
        ),
        plan(
            "The density consequence chain and its qualification",
            [10, 11],
            "Density alone does not produce poverty.",
            "Run the chain to national food security, then qualify with employment structure.",
        ),
        plan(
            "Micro-relief belts of the plain",
            [12],
            "Bhabar, terai, bhangar and khadar carry different agrarian meanings.",
            "Use the belt sequence to defeat any uniform-plain assertion.",
        ),
        plan(
            "The two gradients of the Northern Plain",
            [13],
            "Rainfall and distance from the mountain front cut across each other.",
            "Combine both gradients before naming any sub-region.",
        ),
        plan(
            "Sub-regions of the plain",
            [14],
            "The eastern plain is water-rich yet productivity-constrained.",
            "Give each sub-region its distinguishing combination and agrarian outcome.",
        ),
        plan(
            "Language cores and religious interaction regions",
            [15, 16],
            "No administrative boundary is a clean linguistic line.",
            "Separate formal concentration from functional pilgrimage geography.",
        ),
        plan(
            "Tribal habitat, migration and the vulnerable-community anchor",
            [17, 18, 19],
            "Habitat association is historical and political, not natural.",
            "Close with redistribution through migration and a dated official mapping anchor.",
        ),
    ],
    [
        panel(
            "Building blocks of a cultural region",
            "institutional-ladder",
            [
                "LANGUAGE -> communication and literary core with a hearth and a spread",
                "RELIGION -> sacred sites, ritual calendars, group identity and landscapes",
                "TRIBE AND ETHNICITY -> historical communities associated with a habitat",
                "LIVELIHOOD AND MIGRATION -> the cultural landscape of work; diffusion and mixing",
                "STATE POLICY -> linguistic states, schedules, autonomy arrangements and reservation",
            ],
            ["Scope of cultural and social geography", "Building blocks of a cultural region"],
        ),
        panel(
            "Region types compared",
            "comparison-table",
            [
                "FORMAL -> a dominant shared trait such as language or religion defines the area",
                "FUNCTIONAL -> interaction through pilgrimage, market or media ties the area together",
                "VERNACULAR -> a named, imagined region such as the Hindi belt, Deccan or North-East",
                "OVERLAP -> functional circuits routinely cut across formal boundaries",
                "EXAM USE -> name the type first, then argue about the boundary",
            ],
            ["Three types of cultural region", "Religion as functional geography"],
        ),
        panel(
            "Hearth to identity sequence",
            "process-flow",
            [
                "CULTURAL HEARTH -> the source area where the trait originates",
                "DIFFUSION -> spread along routes, rivers, markets and migration corridors",
                "OVERLAP ZONE -> two traditions coexist and interact in the same space",
                "MIXED BORDERLAND -> bilingual belts, syncretic practice and shared calendars",
                "NEW REGIONAL IDENTITY -> the margin produces its own recognised character",
            ],
            ["Diffusion and overlap sequence", "Transition-zone principle"],
        ),
        panel(
            "Distribution and density firewall",
            "comparison-table",
            [
                "DISTRIBUTION -> the spatial arrangement of people; answers the where question",
                "DENSITY -> a ratio of people to area; answers the how concentrated question",
                "ARITHMETIC -> total population over total area; misleads where land is uninhabitable",
                "PHYSIOLOGICAL -> population over cultivable area; exposes hidden land pressure",
                "AGRICULTURAL -> farming population over cultivable area; isolates agrarian pressure",
            ],
            ["Distribution against density", "Three densities and their meanings"],
        ),
        panel(
            "Controls on population distribution",
            "institutional-ladder",
            [
                "RELIEF AND SOIL -> level land and deep renewable alluvium permit intensive settlement",
                "WATER -> rainfall, perennial rivers and shallow groundwater set cropping intensity",
                "CLIMATE -> growing-season length and reliability deter or permit occupation",
                "HISTORY -> valleys carrying millennia of settlement, urbanism and state formation",
                "ECONOMY AND CONNECTIVITY -> industry, ports, irrigated commands, rail and canal networks",
            ],
            ["Controls on India's population distribution", "Ganga basin convergence of controls"],
        ),
        panel(
            "Ganga basin convergence",
            "causal-system",
            [
                "LEVEL EXTENSIVE ALLUVIAL PLAIN -> almost the whole surface is cultivable and traversable",
                "DEEP RENEWABLE ALLUVIUM -> khadar tracts are renewed by annual deposition",
                "PERENNIAL SNOW-FED RIVERS -> assured water unlike seasonal peninsular rivers",
                "SHALLOW PRODUCTIVE AQUIFERS -> tube-well irrigation permits multiple cropping",
                "HISTORY AND TRANSPORT -> inherited settlement plus dense networks on level ground",
            ],
            ["Ganga basin convergence of controls", "Controls on India's population distribution"],
        ),
        panel(
            "Basin internal variation",
            "comparison-table",
            [
                "WEST TO EAST -> density rises from the drier west toward the wetter middle and lower basin",
                "NORTHERN FRINGE -> tarai constraints differ sharply from the central plain",
                "LOWER AND DELTAIC BASIN -> very high rural density with flood and erosion exposure",
                "URBAN-INDUSTRIAL NODES -> density peaks that agriculture does not explain",
                "RULE -> never write the basin as an internally uniform region",
            ],
            ["Ganga basin internal variation", "Northern Plain sub-regions"],
        ),
        panel(
            "Density consequence chain",
            "process-flow",
            [
                "HIGH PHYSIOLOGICAL DENSITY -> holdings become small and continue fragmenting",
                "SMALL HOLDINGS -> investable surplus and mechanisation capacity fall",
                "LAND PRESSURE -> groundwater over-abstraction and out-migration follow",
                "FLOODPLAIN SETTLEMENT -> exposure rises because the active surface is occupied",
                "NATIONAL LINK -> the same fertility makes the region critical to foodgrain supply",
            ],
            ["Density consequence chain", "Density-poverty qualification"],
        ),
        panel(
            "Micro-relief belt sequence",
            "process-flow",
            [
                "BHABAR -> coarse gravel and boulder wash where streams disappear underground",
                "TERAI -> marshy belt where those streams re-emerge; productive once drained",
                "BHANGAR -> older alluvial upland above the flood limit, often with kankar nodules",
                "KHADAR -> newer alluvium of the active floodplain, most fertile and most flood-exposed",
                "ACTIVE CHANNEL BELT -> levees, bars, ox-bow lakes and char or diara lands",
            ],
            ["Micro-relief belt sequence", "Two gradients of the Northern Plain"],
        ),
        panel(
            "Two gradients and five sub-regions",
            "comparison-table",
            [
                "GRADIENT ONE -> rainfall rises from the north-west toward the humid east",
                "GRADIENT TWO -> the micro-relief transect repeats away from the mountain front",
                "WESTERN AND CENTRAL PLAIN -> irrigated cereals with drawdown; dense fragmented holdings",
                "EASTERN PLAIN -> water-rich yet productivity-constrained by gradient and drainage",
                "BRAHMAPUTRA AND DELTA -> braided erosion insecurity; tidal salinity and cyclone exposure",
            ],
            ["Two gradients of the Northern Plain", "Northern Plain sub-regions"],
        ),
        panel(
            "Cultural marker geographies",
            "comparison-table",
            [
                "LANGUAGE -> regional cores, transition zones and relief-sustained minority pockets",
                "RELIGION -> concentrations plus pilgrimage circuits forming functional interaction regions",
                "TRIBE -> forested hill, plateau and north-eastern association from historical isolation",
                "LIVELIHOOD -> agrarian structures and urban occupational clustering link to economy",
                "MIGRATION -> corridor communities in destination cities redistribute culture continuously",
            ],
            ["Language as core and transition", "Religion as functional geography", "Tribe and habitat association", "Migration as continuous redistribution"],
        ),
        panel(
            "Data discipline and the policy-mapping anchor",
            "institutional-ladder",
            [
                "CENSUS RULE -> the last completed all-India Census is the baseline for any figure",
                "SURVEY RULE -> a newer figure must carry a named survey and its date",
                "FORBIDDEN -> density, growth, literacy, sex ratio, speaker and share figures from memory",
                "9 JULY 2024 -> Ministry of Tribal Affairs state-wise list of vulnerable tribal groups",
                "READING -> identity and habitat remain geographically organised for present policy",
            ],
            ["Vulnerable-community mapping anchor", "Density-poverty qualification"],
        ),
    ],
    [
        "physiological density",
        "khadar",
        "bhangar",
        "terai",
        "bhabar",
        "transition zone",
        "formal cultural region",
        "functional",
        "pilgrimage",
        "Particularly Vulnerable Tribal Groups",
    ],
    (
        "Geography Topic 37 owns direct Mains PYQ demand in the audited routing ledgers. Two GS-I "
        "demands are routed to this owner: 2019 Q18 on the cultural pockets of small India across "
        "the nation, routed through the Advanced companion, and 2025 Q17 on population distribution "
        "and density in the Ganga basin, routed to the Basic owner. Both are answered below as "
        "original model solutions built only from owner evidence. Routed Prelims demand for this "
        "topic remains recorded in the ledgers as objective questions whose official keys are either "
        "unavailable locally or deliberately not inferred, so no option letter or answer key appears "
        "in this package."
    ),
    [
        (
            "2019",
            "GS-I Q18 (Elaborate with examples, 15 marks, 250 words)",
            "Elaborate, with reference to spatial patterns, why cultural pockets of a small India are found across the nation.",
            "Verified routed demand from the audited Mains routing ledger for 2018-2023; the owner file records it as routed to this topic through its Advanced companion. The wording is the ledger's neutral rendering, not reproduced official paper text.",
            "Thesis: cultural pockets recur across India because culture diffuses along routes and migration corridors while regional cores persist, so the country repeatedly reproduces small mixed spaces that resemble the nation in miniature. Establish the mechanism first with this owner's sequence: a cultural hearth generates a trait, diffusion carries it along rivers, roads, markets and labour corridors, an overlap zone forms where two traditions coexist, a mixed borderland develops shared practice, and a new regional identity emerges at the margin. Then classify the pockets by the process that produced them. Metropolitan and industrial cities are the principal mixing zones, because corridor-based migrant communities from specific source regions cluster there in occupational and residential niches. Port and frontier towns mix because they sit where routes and boundaries meet. Linguistic border districts and bilingual belts are pockets by position rather than by migration, since cores are clear while margins are mixed and no administrative boundary is a clean linguistic line. Pilgrimage centres are functional pockets, drawing populations from across formal regions and creating interaction regions that cut across them. Hill and forest tracts preserve distinct communities through relative isolation from plains state formation, which is a historical and political explanation rather than a natural one. Add the qualification that lifts the answer: pockets are not evidence of homogenisation, because regional cores in language, religion, livelihood and habitat persist alongside them, so the cultural map is being layered rather than dissolved. Conclude in graded terms that the recurrence of small mixed spaces is the spatial signature of a mobile society with durable regional cores, and refuse any speaker count or community share from memory.",
        ),
        (
            "2025",
            "GS-I Q17 (Discuss, 15 marks, 250 words)",
            "Discuss population distribution and density in the Ganga basin.",
            "Verified routed demand from the audited Mains routing ledger for 2024-2025, routed to this owner as the owning topic. No official answer key exists for a Mains question, and none is implied.",
            "Thesis: the Ganga basin is the standard Indian case of exceptional density because every control on population distribution reinforces the same outcome there, and the examinable value lies in the convergence and in the internal variation it conceals. Separate the two terms the question names: distribution is the spatial arrangement of people, while density is a ratio, and physiological density measured against cultivable area is the ratio that reveals the pressure arithmetic figures hide. Establish the convergence next. The basin is an extensive level alluvial plain in which almost the entire surface is cultivable and traversable; its deep alluvium is renewable, with khadar tracts restored by annual deposition; its rivers are perennial and snow-fed in a way seasonal peninsular rivers are not; its shallow, highly productive aquifers permit tube-well irrigation and multiple cropping; monsoon rainfall is adequate and rises eastward, supporting rice in the east and irrigated wheat in the west; and long historical continuity of settlement, urbanism, state formation and trade means present density is partly an inherited pattern. A dense transport network on level ground completes the picture. Then supply the internal variation a strong answer requires: density rises broadly from the drier west toward the wetter middle and lower basin; the tarai and northern fringe face different constraints from the central plain; the deltaic and flood-prone lower basin combines extremely high rural density with flood and erosion risk; and urban-industrial nodes create peaks that agriculture does not explain. Close with the consequence chain and its qualification: fragmenting holdings, limited investable surplus, groundwater over-abstraction, floodplain exposure and out-migration link local pressure to national food security, yet high density is not itself poverty, since the outcome depends on agrarian employment structure and non-farm absorption. Quote no density, population or growth figure from memory.",
        ),
    ],
    [
        "https://censusindia.gov.in/",
        "https://tribal.nic.in/",
        "https://pib.gov.in/",
        "https://mospi.gov.in/",
    ],
    (
        "The only dated current anchor used is the Ministry of Tribal Affairs state-wise list of "
        "Particularly Vulnerable Tribal Groups, dated 9 July 2024 in the repository owner, and it is "
        "used solely to show that vulnerable communities continue to be mapped region by region for "
        "policy. The folder's census-currency rule is applied throughout: the last completed "
        "all-India Census is the baseline, and any newer figure would have to be attributed to a "
        "named survey with its date. No density figure, state population, decadal growth rate, "
        "urbanisation share, literacy rate, sex ratio, language speaker count, or religious or tribal "
        "population share is quoted from memory anywhere in this package."
    ),
)






