"""Authored Geography learner-v2 data for Topics 23-25."""

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
# TOPIC 23 — Cool Temperate Continental (Siberian) Climate
# Basic owner: basic/23_Cool-Temperate-Continental-Siberian.md
# Advanced owner: advanced/23_India-Subalpine-Alpine-Belt.md
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_23 = common.topic(
    23,
    "Cool Temperate Continental Siberian",
    "23_Cool-Temperate-Continental-Siberian.md",
    "23_India-Subalpine-Alpine-Belt.md",
    "23_India-Subalpine-Alpine-Belt_Complete-Topic-Package.md",
    [
        ("Northern Hemisphere exclusivity", "The Cool Temperate Continental or Siberian climate is experienced only in the Northern Hemisphere, where the continents at high latitudes have a broad east-west spread; the Southern Hemisphere has no land broad enough at those latitudes to produce this climate."),
        ("Poleward and equatorward boundaries", "On its poleward side the Siberian climate merges into the Arctic tundra of Canada and Eurasia near the Arctic Circle; southwards it becomes less severe and fades into the temperate Steppe climate."),
        ("Bitterly cold long winter", "Winters are bitterly cold and long, often described as sub-Arctic, with a very large annual temperature range; summers are short and cool with a brief warm growing season."),
        ("Low rainfall with summer maximum", "Rainfall is low to moderate and generally has a summer maximum from frontal and convectional sources; winter precipitation is mostly light snow, making the climate semi-arid in character."),
        ("Taiga coniferous belt", "The predominant vegetation is evergreen coniferous forest forming a great continuous belt across North America, Europe and Asia; the greatest single band is the taiga in Siberia, and Sweden and Finland share this forest in Europe."),
        ("Taiga meaning", "Taiga is the Russian word for coniferous forest; it is applied specifically to the vast boreal coniferous belt of Siberia and by extension to the entire Northern Hemisphere boreal forest."),
        ("Softwood conifer adaptations", "Softwood conifers such as pine, spruce, fir and larch have a conical shape to shed snow, needle leaves to reduce transpiration and moisture loss, and shallow root systems suited to thin active soil above permafrost."),
        ("Softwood economic role", "The taiga is the world's greatest softwood source, supplying timber, pulp and paper, matches and furniture; the uniform low-diversity stands of a few conifer species are commercially tractable for mechanised extraction."),
        ("Fur trapping and mining", "The boreal zone also supports fur trapping as a traditional livelihood, and mining and energy extraction in Siberia and Canada are superimposed on the forest economy."),
        ("Biological poverty as advantage", "The taiga's low species diversity is an economic advantage: vast stands of a few conifer species produce uniform timber ideal for industrial pulp, paper and sawn-timber processing, unlike the species-rich but commercially difficult tropical forests."),
        ("Winter haulage and river floating", "Frozen ground and rivers in winter provide natural haulage surfaces for timber transport; spring thaw permits river floating of logs to downstream mills, making the severe climate a seasonal transport asset."),
        ("Carbon storage mechanism", "Cold temperatures slow decomposition far more than they slow growth, so organic matter accumulates in boreal soils, peat and permafrost over long periods; the boreal zone's carbon is held disproportionately below ground, unlike tropical forests' above-ground biomass."),
        ("Fire and permafrost feedback", "Warming lengthens the fire season and thaws frozen ground; combustion releases stored carbon directly and thaw allows previously frozen organic matter to decompose, creating a self-reinforcing feedback that may turn the boreal zone from a carbon sink into a source."),
        ("Permafrost engineering consequence", "Thawing permafrost destroys the bearing capacity of ground beneath roads, pipelines, railways and buildings across the entire settled Arctic and sub-Arctic, converting a cryospheric process into an engineering and public-finance problem."),
        ("India has no continental taiga", "India has no continental taiga, but the upper Himalayan coniferous and alpine belt is its altitudinal analogue of the cold-continental softwood forest, capped by alpine pastures above the treeline."),
        ("Himalayan altitudinal zonation", "The Himalaya show vertical or altitudinal zonation of vegetation from humid tropical through coniferous forest to alpine pastures; at the highest altitudes are the alpine pastures called mergs or bugyals used by tribals to graze cattle in summer."),
        ("Key Himalayan conifers", "Silver-fir or Abies occurs at about 2200 to 3000 metres in the NW and NE Himalaya and is used for planking, wood-pulp, paper and matchsticks; spruce or Picea smithiana occupies the high wet-temperate belt; deodar or Cedrus deodara is a durable conifer timber of the western Himalayan temperate belt."),
        ("Chir pine and fire", "Chir pine is a resinous conifer of the subtropical montane belt receiving 100 to 200 centimetres of rain at 15 to 22 degrees Celsius; it is fire-prone and its prevalence indicates a disturbance-maintained ecosystem."),
        ("Treeline and alpine ecology", "Above the coniferous belt lie alpine scrub and meadows called bugyals or mergs, then snow; the treeline marks the ecological limit of trees and is an indicator of climate change when it shifts upward."),
        ("Transparent PYQ boundary", "The audited routing ledgers contain no direct question owned by Geography Topic 23; taiga and boreal concepts may be tested through adjacent climate-vegetation cross-owner questions but no solved PYQ is fabricated."),
    ],
    [
        "Do not claim the Siberian climate occurs in both hemispheres.",
        "Do not call taiga deciduous broadleaf forest.",
        "Do not assign a summer-dry or winter-rain regime to this climate.",
        "Do not confuse taiga with tundra vegetation.",
        "Do not attribute treelessness above the treeline to poor soil alone.",
        "Do not call deodar and silver-fir broadleaf trees.",
        "Do not equate alpine mergs or bugyals with forests.",
        "Do not quote a specific boreal carbon-stock figure from memory.",
        "Do not ignore the fire-permafrost positive feedback.",
        "Do not present the jet-stream link as settled science.",
        "Do not apply one altitude range for deodar across the whole Himalaya.",
        "Do not invent a direct PYQ for this topic.",
    ],
    [
        (10, "Explain why the taiga is confined to the Northern Hemisphere and identify its key economic value.", "The taiga exists only in the Northern Hemisphere because southern continents are too narrow at the relevant latitudes; its economic value rests on uniform softwood stands ideal for mechanised pulp, paper and timber extraction.", [0, 4, 7]),
        (10, "Compare the taiga's low species diversity with tropical forests from a commercial standpoint.", "The taiga's biological poverty is its commercial strength: few conifer species produce uniform timber for industrial processing, while tropical forests' high diversity makes selective extraction difficult and costly.", [9, 7, 10]),
        (15, "Discuss how the boreal forest functions as a carbon store and why warming threatens to convert it into a carbon source.", "Cold slows decomposition more than growth, accumulating carbon below ground in soils, peat and permafrost; warming lengthens fire seasons and thaws permafrost, releasing stored carbon in a self-reinforcing feedback loop.", [11, 12, 13]),
        (15, "Assess the Himalayan altitudinal zonation as India's analogue of the Siberian boreal belt.", "India lacks continental taiga but the Himalayan coniferous belt from subtropical chir pine through temperate deodar and silver-fir to alpine pastures mirrors the boreal sequence altitudinally; the economic role of softwood and the alpine pastoral economy parallel the taiga.", [14, 15, 16, 18]),
        (20, "Analyse why the same climatic severity that limits settlement in the boreal zone creates a globally significant carbon store and timber economy.", "Extreme cold limits decomposition, accumulating carbon below ground and producing uniform softwood stands; frozen surfaces provide winter haulage; but warming threatens both the carbon store through fire-thaw feedback and the infrastructure through permafrost loss.", [3, 11, 12, 13, 10]),
        (20, "Design a conservation strategy for the Himalayan subalpine-alpine belt using the boreal-zone carbon and treeline lessons.", "The boreal lesson shows that warming converts a carbon sink into a source through fire and thaw; apply this to the Himalayan treeline shift, alpine pastoral disruption and permafrost-slope hazards by integrating cryosphere monitoring, fire management and pastoral adaptation.", [12, 18, 15, 14, 17]),
    ],
    [
        plan("Northern Hemisphere exclusivity and boundaries", [0, 1], "Do not claim this climate occurs in both hemispheres.", "Locate the belt and explain the land-distribution reason for its hemispheric restriction."),
        plan("Climate character", [2, 3], "Do not reverse the rainfall regime to winter-maximum.", "Explain bitterly cold long winters, short cool summers and light summer-maximum rainfall."),
        plan("Taiga identity and extent", [4, 5], "Taiga means coniferous forest in Russian, not tundra.", "Map the continuous coniferous belt across three continents."),
        plan("Conifer adaptations", [6], "Needle leaves reduce transpiration, not photosynthesis.", "Explain conical shape, needle leaves and shallow roots as cold-climate adaptations."),
        plan("Softwood economic value", [7, 8], "Do not reduce the economy to timber alone.", "Trace softwood from extraction through pulp, paper and furniture to fur and mining."),
        plan("Biological poverty as commercial advantage", [9, 10], "Low diversity is an advantage, not a deficiency.", "Invert the expected answer: uniform stands are commercially tractable."),
        plan("Carbon storage mechanism", [11], "Do not quote a carbon-stock figure from memory.", "Explain the cold-decomposition-accumulation chain that stores carbon below ground."),
        plan("Fire-thaw feedback and sink-to-source risk", [12], "This is a self-reinforcing feedback, not a prediction.", "Trace fire and thaw to carbon release and further warming."),
        plan("Permafrost engineering consequence", [13], "Permafrost is infrastructure, not merely a soil condition.", "Connect thaw to loss of bearing capacity beneath roads, pipelines and buildings."),
        plan("India has no continental taiga", [14], "India's analogue is altitudinal, not latitudinal.", "Preserve global Basic versus India Advanced ownership."),
        plan("Himalayan altitudinal zonation", [15, 16], "Altitude ranges are approximate ecological ranges, not contour lines.", "Map the vertical sequence from tropical to alpine."),
        plan("Chir pine and fire ecology", [17], "Chir pine is fire-prone and disturbance-maintained.", "Identify the subtropical montane fire-disturbance regime."),
        plan("Treeline and alpine ecology", [18], "Treeline shift is an indicator, not a proven prediction.", "Explain bugyals/mergs as alpine pastures above the ecological tree limit."),
        plan("Savanna-steppe-taiga comparison", [4, 9], "Three biomes share grassland or forest but differ in mechanism and latitude.", "Distinguish the taiga from the steppe and savanna by vegetation, soil and economy."),
        plan("PYQ boundary and answer spine", [19], "No direct PYQ is owned by this topic.", "Close with the transparent zero-direct-PYQ audit."),
    ],
    [
        panel("Siberian climate world distribution", "spatial-map", [
            "SIBERIA -> largest single taiga band, continental interior",
            "CANADA -> boreal belt from Rockies to Atlantic coast",
            "SCANDINAVIA -> Sweden and Finland share the European taiga",
            "SOUTHERN HEMISPHERE -> absent: no land broad enough at these latitudes",
        ], ["Northern Hemisphere exclusivity and boundaries"]),
        panel("Climate character profile", "comparison-table", [
            "WINTER -> bitterly cold, long, sub-Arctic; very large annual range",
            "SUMMER -> short, cool; brief warm growing season",
            "RAINFALL -> low to moderate; light summer maximum",
            "PRECIPITATION TYPE -> mostly snow in winter; frontal and convectional in summer",
        ], ["Climate character"]),
        panel("Conifer adaptation chain", "process-flow", [
            "CONICAL SHAPE -> sheds snow load, prevents branch breakage",
            "NEEDLE LEAVES -> reduced surface area minimises transpiration loss",
            "SHALLOW ROOTS -> exploit thin active layer above permafrost",
            "RESULT -> conifers dominate where broadleaf trees cannot survive",
        ], ["Conifer adaptations"]),
        panel("Softwood economic chain", "institutional-ladder", [
            "UNIFORM LOW-DIVERSITY STANDS -> mechanised extraction feasible",
            "LONG-FIBRE SOFTWOOD -> ideal for pulp and paper manufacture",
            "FROZEN GROUND AND RIVERS -> natural winter haulage surfaces",
            "SPRING THAW -> river floating of logs to downstream mills",
        ], ["Softwood economic value", "Biological poverty as commercial advantage"]),
        panel("Carbon storage mechanism", "causal-system", [
            "COLD SLOWS DECOMPOSITION -> organic matter accumulates in soil and peat",
            "PERMAFROST -> locks carbon in frozen ground for millennia",
            "BELOW-GROUND CARBON -> disproportionately large compared to above-ground",
            "RESULT -> boreal zone is a globally significant carbon reservoir",
        ], ["Carbon storage mechanism"]),
        panel("Fire-thaw feedback loop", "hazard-flow", [
            "WARMING -> lengthens fire season and thaws permafrost",
            "FIRE -> releases stored carbon directly through combustion",
            "THAW -> exposes frozen organic matter to decomposition",
            "FEEDBACK -> released carbon causes further warming (self-reinforcing)",
        ], ["Fire-thaw feedback and sink-to-source risk"]),
        panel("Permafrost engineering impact", "hazard-flow", [
            "THAWING PERMAFROST -> ground loses bearing capacity",
            "ROADS AND RAILWAYS -> subsidence, cracking, realignment needed",
            "PIPELINES -> stress fractures and leak risk",
            "BUILDINGS -> foundation failure across settled sub-Arctic",
        ], ["Permafrost engineering consequence"]),
        panel("Himalayan altitudinal zonation", "spatial-map", [
            "SUBTROPICAL -> chir pine belt, 100-200 cm rain, fire-prone",
            "TEMPERATE -> deodar, spruce in western Himalaya",
            "SUBALPINE -> silver-fir (Abies) at 2200-3000 m, NW and NE",
            "ALPINE -> bugyals/mergs: treeless pastures above treeline",
        ], ["Himalayan altitudinal zonation", "Chir pine and fire ecology"]),
        panel("Himalayan conifer identification", "comparison-table", [
            "SILVER-FIR (Abies) -> 2200-3000 m; planking, pulp, paper, matches",
            "SPRUCE (Picea smithiana) -> high wet-temperate belt; softwood",
            "DEODAR (Cedrus deodara) -> western Himalaya; durable timber",
            "CHIR PINE -> subtropical montane; resinous, fire-prone",
        ], ["Key Himalayan conifers", "Chir pine and fire ecology"]),
        panel("Treeline and alpine pastures", "process-flow", [
            "CONIFEROUS FOREST -> gives way at the treeline altitude",
            "ALPINE SCRUB -> dwarf shrubs in transition zone",
            "BUGYALS/MERGS -> open grassy meadows for summer grazing",
            "SNOWLINE -> permanent snow above the pastoral belt",
        ], ["Treeline and alpine ecology"]),
        panel("Biome comparison strip", "comparison-table", [
            "TAIGA -> high-latitude coniferous, below-ground carbon, softwood economy",
            "STEPPE -> mid-latitude grassland, chernozem soil, mechanised grain",
            "SAVANNA -> tropical grassland, laterised soil, pastoral subsistence",
            "DISTINGUISHER -> latitude, rainfall regime, soil type and economic system",
        ], ["Savanna-steppe-taiga comparison"]),
        panel("Siberian climate answer spine", "answer-spine", [
            "DEFINE -> Northern Hemisphere boreal coniferous belt with extreme continental range",
            "LOCATE -> Siberia, Canada, Scandinavia; absent in Southern Hemisphere",
            "EXPLAIN -> cold-adaptation, softwood economy, carbon storage, fire-thaw feedback",
            "QUALIFY -> India's altitudinal analogue; transparent zero-direct-PYQ boundary",
        ], ["PYQ boundary and answer spine"]),
    ],
    [
        "taiga", "boreal", "coniferous", "softwood", "permafrost",
        "carbon sink", "fire-thaw feedback", "altitudinal zonation",
        "silver-fir", "deodar", "bugyals", "mergs",
        "Picea smithiana", "chir pine",
    ],
    (
        "The audited routing ledgers contain no direct question owned by "
        "Geography Topic 23. Taiga and boreal concepts may be tested "
        "through adjacent climate-vegetation cross-owner questions, but no "
        "solved PYQ or fabricated answer key is included."
    ),
    [],
    [
        "https://www.noaa.gov/arctic",
        "https://www.fsi.nic.in/",
    ],
    (
        "NOAA Arctic monitoring and FSI forest reports are used only to "
        "establish taiga fire seasons and Himalayan forest cover as live "
        "current anchors. No volatile extent, fire-area or carbon figure "
        "is quoted without a dated official source."
    ),
)


# ═══════════════════════════════════════════════════════════════════════════════
# TOPIC 24 — Cool Temperate Eastern Margin (Laurentian) Climate
# Basic owner: basic/24_Cool-Temperate-Eastern-Margin-Laurentian.md
# Advanced owner: advanced/24_India-Eastern-Himalaya-Temperate.md
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_24 = common.topic(
    24,
    "Cool Temperate Eastern Margin Laurentian",
    "24_Cool-Temperate-Eastern-Margin-Laurentian.md",
    "24_India-Eastern-Himalaya-Temperate.md",
    "24_India-Eastern-Himalaya-Temperate_Complete-Topic-Package.md",
    [
        ("Intermediate climate type", "The Cool Temperate Eastern Margin or Laurentian climate is an intermediate type between the British maritime and Siberian continental types, combining features of both: cold dry winters from continental air and warm summers with a summer rainfall maximum from ocean easterlies."),
        ("Two-region restriction", "The Laurentian type occurs in only two regions and is absent from the Southern Hemisphere: NE North America including eastern Canada, the Maritime Provinces, New England and Newfoundland; and eastern Asia including eastern Siberia, North China, Manchuria, Korea and northern Japan."),
        ("Cold dry winter mechanism", "Cold dry winters result from Westerly winds blowing outward from the chilled continental interior; these carry dry, frigid air to the eastern margins, creating the type's most distinctive winter character."),
        ("Warm summer rainfall maximum", "Warm summers receive about two-thirds of the total 30 to 60 inches of precipitation from easterly winds off the oceans, giving a distinct summer rainfall maximum that is the reverse of the British type's autumn-winter rain."),
        ("Oyashio-Kuroshio convergence", "Off northern Japan the cold Oyashio current meets the warm Kuroshio, producing fog and mist and making north Japan a second Newfoundland; the convergence zone is a major fishing ground supported by nutrient mixing over shallow shelves."),
        ("Grand Banks mechanism", "Off Newfoundland the cold Labrador Current meets warmer Atlantic water over the shallow Grand Banks, favouring fog; fish productivity depends on shelf mixing, nutrient supply and management, not merely on warm-cold current meeting alone."),
        ("Fishing economy", "Fishing replaces agriculture as the main occupation in many Laurentian coastlands; the convergence of warm and cold currents over broad shallow shelves creates the physical basis for world-historic fishing grounds."),
        ("Cool temperate mixed forest", "The predominant natural vegetation is cool temperate forest of mixed coniferous-deciduous character, a transition between the deciduous British type forest and the coniferous Siberian taiga, favoured by heavy rain, warm summers and damp air."),
        ("Southern Hemisphere absence", "The Laurentian type is absent in the Southern Hemisphere because the continents are narrow or absent at the relevant latitudes, so no continental interior exists to generate the defining cold dry winter air mass."),
        ("Fog as hazard and resource indicator", "Fog at current convergence zones is simultaneously a navigational hazard and a biological indicator of nutrient-rich mixing waters; the same process that creates poor visibility creates high marine productivity."),
        ("Eastern Himalaya as India analogue", "India lacks a true Laurentian climate, but the Eastern Himalaya including Darjeeling, Sikkim and Arunachal Pradesh is the country's cool, humid, eastern-facing temperate zone with a summer monsoon rainfall maximum and persistent hill fog."),
        ("Eastern Himalaya warm perhumid ecoregion", "Khullar classes the Eastern Himalayas as a warm perhumid ecoregion with brown-and-red soils and a growing period exceeding 210 days; the region includes Sikkim, Arunachal Pradesh and the hilly areas of Assam."),
        ("Teesta drainage", "Sikkim is drained chiefly by the Teesta and its tributaries; the Teesta joins the Brahmaputra system in Bangladesh, not the Ganga, which is a common UPSC trap."),
        ("Darjeeling tea economy", "Darjeeling's aromatic GI-protected orthodox tea grows on estates at about 900 to 1800 metres elevation in a climate with approximately 300 centimetres annual rainfall; it is a low-yield premium tea contrasting with the Brahmaputra valley's bulk production."),
        ("Hill versus valley tea distinction", "The Brahmaputra Valley is a bulk-tea belt producing high volumes, while the Darjeeling hills produce low-yield premium GI tea; this hill-versus-valley distinction in quality, yield and market mirrors the Laurentian pattern of altitude-controlled economic specialisation."),
        ("Teesta basin hazards", "The 2023 South Lhonak GLOF, recurring landslides, hydropower infrastructure concentration and repeated NH-10 disruption illustrate the Teesta basin's interaction of steep relief, sediment load, extreme monsoon rain and corridor concentration."),
        ("Polar vortex and cold outbreaks", "Stratospheric disruptions can alter mid-latitude cold outbreak risk in Laurentian-type regions, but the links to Arctic sea-ice loss remain actively debated and event attribution must be cautious."),
        ("Current convergence as economic foundation", "The Laurentian type's economic foundation is built on the sea rather than the land because the same current configuration that produces harsh foggy climate also produces exceptional marine productivity on broad shallow shelves."),
        ("Fishery governance constraint", "The physical basis of the fishery is a potential, not a guarantee: heavily exploited stocks such as the Grand Banks cod have collapsed despite unchanged oceanography, so the constraint is governance, not geography."),
        ("Transparent PYQ boundary", "The audited routing ledgers contain no direct question owned by Geography Topic 24; Laurentian and Eastern Himalaya concepts may be tested through adjacent climate or regional geography questions but no solved PYQ is fabricated."),
    ],
    [
        "Do not assign a winter rainfall maximum to the Laurentian type.",
        "Do not claim the Laurentian type occurs in the Southern Hemisphere.",
        "Do not say Grand Banks fisheries arise simply because two currents meet.",
        "Do not confuse the Teesta as a tributary of the Ganga.",
        "Do not call Darjeeling a bulk-tea producer.",
        "Do not equate fog with poor fishing conditions.",
        "Do not apply the Laurentian label to the Southern Hemisphere.",
        "Do not attribute Laurentian cold winters to latitude alone.",
        "Do not treat the polar-vortex cold-outbreak link as settled.",
        "Do not ignore governance as a constraint on fishery productivity.",
        "Do not claim India has a true Laurentian climate.",
        "Do not invent a direct PYQ for this topic.",
    ],
    [
        (10, "Explain why the Laurentian climate has cold dry winters and a summer rainfall maximum.", "Continental Westerlies blow dry frigid air from the interior in winter while easterly ocean winds bring moisture-laden summer rain; this reverses the British type's seasonal pattern and is the Laurentian type's defining character.", [2, 3, 0]),
        (10, "Account for the formation of the world's great fishing grounds off the Laurentian coasts.", "Warm and cold currents converge over broad shallow shelves producing nutrient mixing and high plankton productivity; the same convergence generates persistent fog that is both a navigational hazard and a biological indicator.", [4, 5, 6]),
        (15, "Compare the Laurentian and British climate types in terms of rainfall regime, winter character and economic orientation.", "The Laurentian type has a summer rainfall maximum from ocean easterlies and cold dry winters from continental air, while the British type has autumn-winter rain and mild wet winters from maritime Westerlies; the Laurentian economy is sea-based while the British economy is land-based.", [0, 3, 7, 17]),
        (15, "Assess how the Eastern Himalaya serves as India's Laurentian-type analogue in terms of climate and economy.", "The Eastern Himalaya shares summer-maximum rainfall, persistent hill fog and a specialised agricultural economy with the Laurentian type; Darjeeling's premium tea mirrors the altitude-controlled economic specialisation while the Teesta basin faces GLOF and landslide hazards.", [10, 11, 13, 15]),
        (20, "Analyse why the same current configuration produces both a hazard and a resource on the Laurentian coasts, and why physical endowment alone cannot sustain the fishery.", "Warm-cold current convergence over shallow shelves generates fog as a navigational hazard and nutrient mixing as a productivity base simultaneously; however, the Grand Banks cod collapse shows that governance, not geography, determines whether the physical potential persists.", [4, 5, 9, 18, 6]),
        (20, "Design a sustainable development strategy for the Eastern Himalayan Laurentian-analogue belt integrating the lessons of fishery governance failure.", "Apply the Grand Banks governance lesson to the Teesta basin: physical endowment sets the possibility but management determines sustainability; integrate GLOF early-warning, hydropower carrying-capacity assessment, premium-tea GI protection and monsoon-infrastructure resilience.", [15, 18, 13, 14, 16]),
    ],
    [
        plan("Intermediate type identity", [0], "This is intermediate, not a simple average of British and Siberian.", "Locate the type between the British maritime and Siberian continental extremes."),
        plan("Two-region restriction", [1, 8], "No Southern Hemisphere land exists at the relevant latitudes.", "Map NE North America and East Asia as the only two regions."),
        plan("Cold dry winter mechanism", [2], "Continental Westerlies, not latitude, cause the cold dry winters.", "Trace the continental air outflow that defines the winter character."),
        plan("Warm summer rainfall maximum", [3], "Summer maximum is the reverse of the British type.", "Explain the two-thirds summer share of 30-60 inches annual rainfall."),
        plan("Oyashio-Kuroshio convergence", [4], "Convergence produces fog and fish, not just one.", "Map northern Japan's current meeting and its dual economic effect."),
        plan("Grand Banks and Labrador-Atlantic meeting", [5, 9], "Fish productivity requires shelf, mixing and management, not just currents.", "Trace the Newfoundland mechanism from current convergence through fog to fishery."),
        plan("Fishing economy and current foundation", [6, 17], "The economy is built on the sea, not the land.", "Connect the physical oceanographic base to the Laurentian economic identity."),
        plan("Cool temperate mixed forest", [7], "A transition forest, not purely coniferous or deciduous.", "Place the mixed forest between the British deciduous and Siberian coniferous."),
        plan("Fog as dual-purpose phenomenon", [9], "Fog is a hazard and a resource indicator simultaneously.", "Explain why the same process creates poor visibility and high marine productivity."),
        plan("Fishery governance constraint", [18], "Physical basis is a potential, not a guarantee.", "Use the Grand Banks cod collapse to qualify physical-determinist arguments."),
        plan("Eastern Himalaya as India analogue", [10, 11], "India has no true Laurentian climate; the analogue is altitudinal.", "Map Darjeeling-Sikkim-Arunachal as the cool humid eastern-facing temperate zone."),
        plan("Teesta drainage and hazards", [12, 15], "The Teesta joins the Brahmaputra, not the Ganga.", "Identify the GLOF, landslide and corridor-concentration risks."),
        plan("Darjeeling premium tea", [13, 14], "Darjeeling is premium low-yield, not bulk.", "Contrast hill premium with valley bulk production."),
        plan("Polar vortex and mid-latitude linkage", [16], "The polar-vortex cold-outbreak link is actively debated.", "Present stratospheric disruption as a hypothesis, not a settled mechanism."),
        plan("PYQ boundary and answer spine", [19], "No direct PYQ is owned by this topic.", "Close with the transparent zero-direct-PYQ audit."),
    ],
    [
        panel("Laurentian climate world distribution", "spatial-map", [
            "NE NORTH AMERICA -> eastern Canada, Maritime Provinces, New England, Newfoundland",
            "EAST ASIA -> eastern Siberia, North China, Manchuria, Korea, northern Japan",
            "SOUTHERN HEMISPHERE -> absent: continents too narrow at relevant latitudes",
            "INTERMEDIATE -> between British maritime (west) and Siberian continental (east)",
        ], ["Two-region restriction"]),
        panel("Seasonal rainfall mechanism", "process-flow", [
            "WINTER -> continental Westerlies blow dry frigid air from interior",
            "SUMMER -> easterly ocean winds bring moisture-laden rainfall",
            "RESULT -> distinct summer maximum: two-thirds of 30-60 inches total",
            "CONTRAST -> reverse of British type's autumn-winter rain pattern",
        ], ["Cold dry winter mechanism", "Warm summer rainfall maximum"]),
        panel("Current convergence and fishing", "causal-system", [
            "OYASHIO (cold) + KUROSHIO (warm) -> convergence off northern Japan",
            "LABRADOR (cold) + ATLANTIC (warm) -> convergence over Grand Banks shelf",
            "NUTRIENT MIXING -> plankton bloom on broad shallow shelves",
            "RESULT -> world-historic fishing grounds plus persistent fog",
        ], ["Oyashio-Kuroshio convergence", "Grand Banks and Labrador-Atlantic meeting"]),
        panel("Fog as dual phenomenon", "comparison-table", [
            "FOG AS HAZARD -> poor visibility, navigational danger, shipping risk",
            "FOG AS INDICATOR -> biological marker of nutrient-rich mixing waters",
            "MECHANISM -> warm moist air chilled from below by cold current contact",
            "EXAM USE -> same process creates hazard and resource simultaneously",
        ], ["Fog as dual-purpose phenomenon"]),
        panel("Mixed forest transition strip", "spatial-map", [
            "BRITISH MARGIN -> deciduous broadleaf forest (mild, wet winters)",
            "LAURENTIAN ZONE -> mixed coniferous-deciduous transition forest",
            "SIBERIAN INTERIOR -> evergreen coniferous taiga (cold, dry winters)",
            "GRADIENT -> maritime to continental controls the forest composition",
        ], ["Cool temperate mixed forest"]),
        panel("Fishery governance lesson", "decision-tree", [
            "PHYSICAL BASE -> current convergence + shallow shelf + nutrient mixing",
            "INITIAL OUTCOME -> one of the world's most productive fisheries",
            "OVEREXPLOITATION -> Grand Banks cod stocks collapsed despite same oceanography",
            "CONCLUSION -> governance, not geography, determines sustainability",
        ], ["Fishery governance constraint"]),
        panel("Eastern Himalaya analogue map", "spatial-map", [
            "DARJEELING-SIKKIM -> cool humid eastern-facing temperate belt",
            "ARUNACHAL PRADESH -> warm perhumid ecoregion, growing period > 210 days",
            "MONSOON RAINFALL -> summer maximum parallels Laurentian pattern",
            "HILL FOG -> persistent mist mirrors Newfoundland-Japan fog zones",
        ], ["Eastern Himalaya as India analogue"]),
        panel("Teesta basin profile", "hazard-flow", [
            "STEEP RELIEF -> rapid runoff, high sediment load",
            "EXTREME MONSOON RAIN -> triggers landslides and GLOF events",
            "CORRIDOR CONCENTRATION -> NH-10, hydropower on narrow valley floor",
            "2023 SOUTH LHONAK GLOF -> illustrates combined relief-rain-infrastructure risk",
        ], ["Teesta drainage and hazards"]),
        panel("Darjeeling tea economy", "comparison-table", [
            "DARJEELING HILLS -> low-yield, premium, GI-protected orthodox tea",
            "BRAHMAPUTRA VALLEY -> bulk-tea belt, high-volume production",
            "ELEVATION -> estates at 900-1800 m; too cold above, too warm below",
            "DISTINCTION -> hill quality versus valley quantity mirrors altitude control",
        ], ["Darjeeling premium tea"]),
        panel("British-Laurentian comparison", "comparison-table", [
            "RAINFALL -> British: autumn-winter max | Laurentian: summer max",
            "WINTER -> British: mild, wet (maritime) | Laurentian: cold, dry (continental)",
            "ECONOMY -> British: land-based agriculture | Laurentian: sea-based fishing",
            "FOREST -> British: deciduous broadleaf | Laurentian: mixed transitional",
        ], ["Intermediate type identity"]),
        panel("Polar-vortex hypothesis", "process-flow", [
            "STRATOSPHERIC DISRUPTION -> weakens polar vortex containment",
            "COLD ARCTIC AIR -> spills southward into mid-latitudes",
            "LAURENTIAN REGIONS -> experience severe cold outbreaks",
            "STATUS -> actively debated link to Arctic sea-ice loss; not settled science",
        ], ["Polar vortex and mid-latitude linkage"]),
        panel("Laurentian answer spine", "answer-spine", [
            "DEFINE -> intermediate type between British maritime and Siberian continental",
            "LOCATE -> NE North America and East Asia only; absent in Southern Hemisphere",
            "EXPLAIN -> cold dry winters, summer rain maximum, current convergence, fog-fishery",
            "QUALIFY -> India Eastern Himalaya analogue; transparent zero-direct-PYQ boundary",
        ], ["PYQ boundary and answer spine"]),
    ],
    [
        "Laurentian", "Oyashio", "Kuroshio", "Grand Banks",
        "Labrador Current", "Newfoundland", "Darjeeling",
        "Teesta", "GI-protected", "perhumid", "GLOF",
        "mixed coniferous-deciduous", "summer rainfall maximum",
        "continental Westerlies",
    ],
    (
        "The audited routing ledgers contain no direct question owned by "
        "Geography Topic 24. Laurentian and Eastern Himalaya concepts may "
        "be tested through adjacent climate or regional geography questions, "
        "but no solved PYQ or fabricated answer key is included."
    ),
    [],
    [
        "https://www.teaboard.gov.in/",
        "https://www.cwc.gov.in/",
    ],
    (
        "Tea Board and CWC sources are used only to establish Darjeeling "
        "GI tea and Teesta basin flood management as live current anchors. "
        "No volatile production, yield or GLOF claim is quoted without a "
        "dated official source."
    ),
)


# ═══════════════════════════════════════════════════════════════════════════════
# TOPIC 25 — Arctic or Polar Climate
# Basic owner: basic/25_Arctic-or-Polar-Climate.md
# Advanced owner: advanced/25_India-Cold-Desert-and-Poles.md
# PYQ: 2021 GS-I Q15 — Melting Arctic ice and Antarctic glaciers
# ═══════════════════════════════════════════════════════════════════════════════

TOPIC_25 = common.topic(
    25,
    "Arctic or Polar Climate",
    "25_Arctic-or-Polar-Climate.md",
    "25_India-Cold-Desert-and-Poles.md",
    "25_India-Cold-Desert-and-Poles_Complete-Topic-Package.md",
    [
        ("Polar climate location", "The polar type of climate and vegetation is found mainly north of the Arctic Circle in the Northern Hemisphere, with two subdivisions: ice-cap covering Greenland and high-latitude highlands under permanent snow, and tundra covering lowlands with a few ice-free months."),
        ("Tundra distribution", "Tundra covers coastal Greenland, the barren grounds of northern Canada and Alaska, and the Arctic seaboard of Eurasia; these lowlands have a few months above freezing when snow melts and vegetation appears."),
        ("Temperature character", "Mean annual temperature is very low; the warmest month in June or July seldom exceeds about 10 degrees Celsius; no more than about four months rise above freezing and winters are long and severe, colder in the interior."),
        ("Cold desert precipitation", "Precipitation is low and mostly snow, making the polar climate a cold desert; blizzards are wind-and-snow events caused by wind redistributing existing snow into drifts, not simply heavy snowfall."),
        ("Tundra vegetation", "Tundra is treeless; in sheltered spots stunted birches, dwarf willows and undersized alders survive; coastal lowlands carry hardy grasses and reindeer moss which is actually a lichen providing the only pasturage for reindeer."),
        ("Brief summer flowering", "In the brief polar summer snow melts and berry-bushes and Arctic flowers bloom briefly before the return of continuous cold; this short growing season controls the entire ecological calendar."),
        ("Arctic-Antarctic asymmetry", "The Arctic is an ocean surrounded by continents while Antarctica is a continent surrounded by ocean; the Arctic carries mainly floating sea ice plus the Greenland ice sheet, while Antarctica holds a vast grounded ice sheet with floating ice shelves at its margins."),
        ("Ice-albedo feedback mechanism", "Arctic amplification works through the ice-albedo feedback: as warming causes sea ice and snow to retreat, bright high-albedo surfaces are replaced by dark ocean and bare ground, absorbing far more solar radiation and causing further warming in a self-reinforcing loop."),
        ("Permafrost thaw and carbon", "Permafrost thaw releases stored carbon as carbon dioxide under dry conditions and methane under waterlogged conditions; this creates a second self-reinforcing feedback loop alongside the ice-albedo mechanism."),
        ("Sea-level rule", "Floating sea-ice melt does not raise sea level; only grounded ice loss from Greenland and Antarctica transfers mass to the ocean; ice-shelf loss removes buttressing and can accelerate grounded-ice discharge."),
        ("Arctic shipping prospects", "Retreating summer sea ice lengthens the navigable season along Arctic coasts on routes shorter than Suez or Panama between NE Asia and NW Europe, but practical constraints including mobile ice, incomplete charting, thin rescue capacity, costly insurance and sparse ports limit near-term traffic to resource export and destination shipping."),
        ("Arctic governance", "Coastal states' rights over the Arctic seabed depend on maritime law including continental-shelf extensions on geological evidence; regional cooperation operates through a state-led forum with observer participation by non-Arctic states including India."),
        ("India cold desert Ladakh", "India's cold-desert analogue is Ladakh and adjoining trans-Himalayan valleys; the Greater Himalaya blocks the southwest monsoon creating a rain-shadow, while high altitude produces intense insolation by day and sharp radiative cooling by night."),
        ("Ladakh cold desert mechanism", "Ladakh is a desert because of rain-shadow plus high altitude, not because it is hot; winter western disturbances bring the light snow that is the main precipitation; Husain classes it with the cold desert biome alongside the Sierra Nevada and the Andes."),
        ("Ladakh land use", "In the cold deserts of Ladakh and Spiti, priority goes to irrigated agriculture and animal husbandry with water-harvesting devices; the Changpa rear pashmina goats and yak on high pastures, and allied activities include milk, poultry and horticulture."),
        ("India polar research stations", "India's polar research is coordinated by NCPOR in Goa; Antarctic stations are Maitri at Schirmacher Oasis since 1989 and Bharati at Larsemann Hills since 2012; Dakshin Gangotri was the first station from 1983 but was later decommissioned."),
        ("India Arctic and Himalayan stations", "India's Arctic station is Himadri at Ny-Alesund in Svalbard since 2008; the Himalayan station Himansh in Spiti, Himachal Pradesh conducts glacier studies; Dakshin Gangotri is not operational."),
        ("India polar legal framework", "India acceded to the Antarctic Treaty in 1983, has the Indian Antarctic Act 2022 and an Arctic Policy 2022 with six pillars; the research focus is on teleconnections between Arctic sea-ice loss and disruption of the Indian monsoon."),
        ("Arctic Indigenous peoples", "Arctic Indigenous communities include the Inuit in Greenland, Canada and Alaska, the Sami in northern Fennoscandia and the Nenets and other peoples in Arctic Russia; these communities have diverse livelihoods adapted to the polar environment."),
        ("2021 GS-I PYQ ownership", "The 2021 GS-I Q15 demand on melting Arctic ice and Antarctic glaciers and weather patterns is the only verified PYQ owned by this topic; it requires the Arctic-Antarctic distinction, the amplification mechanism and four transmission channels with confidence grading."),
    ],
    [
        "Do not claim polar regions get heavy precipitation.",
        "Do not say tundra has coniferous forest.",
        "Do not equate ice-cap and tundra as the same.",
        "Do not merge floating sea-ice melt with grounded-ice sea-level rise.",
        "Do not treat the two poles as equivalent in governance or ice type.",
        "Do not call Ladakh arid because it is hot.",
        "Do not identify Bharati as an Arctic station.",
        "Do not claim Dakshin Gangotri is operational.",
        "Do not assert the jet-stream-Arctic link as settled science.",
        "Do not quote sea-ice extent minima or mass-loss rates from memory.",
        "Do not announce the Arctic as an open sea lane.",
        "Do not invent PYQ demands beyond the verified 2021 GS-I Q15.",
    ],
    [
        (10, "Explain why the tundra is treeless and why the polar climate is classified as a cold desert.", "The tundra is treeless because of the short growing season with the warmest month below about 10 degrees Celsius, permafrost preventing deep rooting, poor drainage and wind; precipitation is low and mostly snow, making the polar zone a cold desert by rainfall criteria.", [2, 4, 3]),
        (10, "Distinguish between ice-cap and tundra subdivisions of the polar climate.", "Ice-cap areas such as Greenland are permanently snow-covered with no vegetation; tundra lowlands have a few ice-free months when mosses, lichens and dwarf shrubs appear, providing grazing for reindeer; the distinction is the presence of a brief growing season.", [0, 4, 5]),
        (15, "Discuss the effects of melting Arctic ice and Antarctic glaciers on weather patterns, distinguishing the mechanisms and their confidence levels.", "Arctic amplification through the ice-albedo feedback accelerates regional warming; sea-level contribution comes from grounded ice only; permafrost thaw adds a carbon feedback; the hypothesised jet-stream weakening and blocking link is the least certain channel and must be presented as actively debated.", [7, 8, 9, 19]),
        (15, "Assess Ladakh as India's cold-desert analogue and explain the mechanisms that make it arid.", "Ladakh is a cold desert because the Greater Himalaya blocks the southwest monsoon creating a rain-shadow while high altitude causes intense radiative cooling; winter western disturbances bring light snow; the Changpa pastoral economy and water-harvesting adapt to these constraints.", [12, 13, 14]),
        (20, "Analyse the geopolitical significance of the opening Arctic, integrating the practical constraints on shipping and the governance architecture.", "Retreating sea ice creates shorter routes between NE Asia and NW Europe, but mobile ice, incomplete charting, thin rescue capacity and sparse ports limit traffic to resource export; maritime-law continental-shelf claims, the Arctic forum and India's observer role form the governance layer.", [10, 11, 17, 18]),
        (20, "Design a comprehensive framework linking India's polar research programme, Himalayan cryosphere monitoring and Ladakh cold-desert sustainability.", "India's polar stations at Maitri, Bharati and Himadri track teleconnections between Arctic change and Indian monsoon disruption; connect this to Himalayan glacier monitoring at Himansh and to Ladakh cold-desert sustainability through water-harvesting, pastoral adaptation and infrastructure resilience.", [15, 16, 17, 14, 12]),
    ],
    [
        plan("Polar climate location and subdivisions", [0, 1], "Ice-cap and tundra are not the same subdivision.", "Map the polar zone north of the Arctic Circle and distinguish ice-cap from tundra."),
        plan("Temperature and precipitation character", [2, 3], "Polar climate is a cold desert with low precipitation, not heavy snowfall.", "Explain the sub-10-degree warmest month and low snow precipitation."),
        plan("Tundra vegetation and ecology", [4, 5], "Tundra is treeless; reindeer moss is a lichen, not a moss.", "Describe the stunted vegetation, lichen pasture and brief summer flowering."),
        plan("Arctic-Antarctic asymmetry", [6], "Arctic is an ocean; Antarctica is a continent.", "Open any polar answer with the fundamental asymmetry."),
        plan("Ice-albedo feedback mechanism", [7], "This is a self-reinforcing loop, not a one-time event.", "Trace the feedback from ice retreat through albedo change to further warming."),
        plan("Permafrost carbon feedback", [8], "Dry conditions release CO2, waterlogged conditions release methane.", "Explain the second feedback loop alongside the albedo mechanism."),
        plan("Sea-level grounded-ice rule", [9], "Floating sea-ice melt does not raise sea level.", "Distinguish grounded from floating ice and explain the buttressing role of ice shelves."),
        plan("Arctic shipping and practical constraints", [10], "Do not present the Arctic as an accomplished trade route.", "Balance the shorter-route advantage against the severe practical limitations."),
        plan("Arctic governance and India", [11], "India has observer status, not territorial claims.", "Map maritime-law claims, the Arctic forum and India's role."),
        plan("Indigenous peoples", [18], "Use Inuit, Sami and Nenets, not older exonyms.", "Identify Arctic Indigenous communities and their diverse livelihoods."),
        plan("India cold desert Ladakh", [12, 13], "Ladakh is arid due to rain-shadow and altitude, not heat.", "Explain the rain-shadow and radiative-cooling mechanism."),
        plan("Ladakh land use and Changpa", [14], "Irrigated agriculture and pastoral economy are the priorities.", "Map water-harvesting, pashmina goats and yak herding."),
        plan("India polar research programme", [15, 16], "Dakshin Gangotri is decommissioned; Bharati and Maitri are Antarctic.", "Enumerate stations with correct locations and operational status."),
        plan("India polar legal framework", [17], "Antarctic Treaty 1983, Antarctic Act 2022, Arctic Policy 2022.", "Connect the legal-policy framework to the teleconnection research focus."),
        plan("2021 PYQ demand and answer spine", [19], "This is the only verified PYQ owned by this topic.", "Close with the verified PYQ demand and the four-channel answer spine."),
    ],
    [
        panel("Polar climate world distribution", "spatial-map", [
            "ICE-CAP -> Greenland and high-latitude highlands, permanent snow cover",
            "TUNDRA -> coastal Greenland, N. Canada, Alaska, Eurasian Arctic seaboard",
            "SOUTHERN POLE -> Antarctica: continent under ice, no indigenous population",
            "NORTHERN POLE -> Arctic: ocean basin surrounded by continental land masses",
        ], ["Polar climate location and subdivisions"]),
        panel("Temperature-precipitation profile", "comparison-table", [
            "WARMEST MONTH -> seldom exceeds about 10 degrees C (June/July)",
            "MONTHS ABOVE FREEZING -> no more than about four per year",
            "PRECIPITATION -> low, mostly snow; polar climate = cold desert",
            "BLIZZARDS -> wind redistributing existing snow, not heavy snowfall events",
        ], ["Temperature and precipitation character"]),
        panel("Tundra vegetation belt", "process-flow", [
            "PERMAFROST -> prevents deep rooting, impedes drainage",
            "SHORT GROWING SEASON -> warmest month below 10 degrees C",
            "STUNTED PLANTS -> dwarf willows, birches, alders in sheltered spots",
            "LICHEN GROUND COVER -> reindeer moss provides grazing for reindeer herds",
        ], ["Tundra vegetation and ecology"]),
        panel("Arctic-Antarctic asymmetry", "comparison-table", [
            "ARCTIC -> ocean surrounded by continents; mainly floating sea ice",
            "ANTARCTIC -> continent surrounded by ocean; vast grounded ice sheet",
            "WARMING -> Arctic amplification much faster; Antarctic more complex",
            "GOVERNANCE -> Arctic: sovereign states + forum | Antarctic: treaty regime",
        ], ["Arctic-Antarctic asymmetry"]),
        panel("Ice-albedo feedback loop", "causal-system", [
            "SEA ICE AND SNOW RETREAT -> bright surface replaced by dark ocean/ground",
            "ALBEDO DROPS -> far more solar radiation absorbed instead of reflected",
            "SURFACE WARMING -> further ice and snow retreat (self-reinforcing)",
            "REINFORCING FACTORS -> thin polar atmosphere, ocean heat escape, poleward transport",
        ], ["Ice-albedo feedback mechanism"]),
        panel("Permafrost carbon feedback", "hazard-flow", [
            "WARMING -> thaws frozen ground containing ancient organic matter",
            "DRY CONDITIONS -> decomposition releases carbon dioxide",
            "WATERLOGGED CONDITIONS -> decomposition releases methane (stronger GHG)",
            "FEEDBACK -> released GHGs cause further warming, further thaw",
        ], ["Permafrost carbon feedback"]),
        panel("Sea-level grounded-ice rule", "decision-tree", [
            "FLOATING SEA ICE MELTS -> sea level does NOT rise (already displacing water)",
            "GROUNDED ICE MELTS -> mass transferred to ocean, sea level RISES",
            "ICE SHELVES LOST -> removes buttressing, accelerates grounded-ice discharge",
            "EXAM RULE -> always distinguish floating from grounded in any polar answer",
        ], ["Sea-level grounded-ice rule"]),
        panel("Arctic shipping constraints", "comparison-table", [
            "ADVANTAGE -> routes shorter than Suez/Panama between NE Asia and NW Europe",
            "MOBILE ICE -> unpredictable, hazardous despite retreat trend",
            "RESCUE AND CHARTING -> thin capacity, incomplete surveys",
            "NEAR-TERM TRAFFIC -> resource export and destination, not transit container",
        ], ["Arctic shipping and practical constraints"]),
        panel("India cold desert Ladakh", "spatial-map", [
            "RAIN-SHADOW -> Greater Himalaya blocks SW monsoon, Trans-Himalaya stays arid",
            "HIGH ALTITUDE -> intense insolation by day, sharp radiative cooling by night",
            "WINTER PRECIPITATION -> light snow from western disturbances",
            "BIOME CLASS -> cold desert, same as Sierra Nevada (USA) and Andes (Argentina)",
        ], ["India cold desert Ladakh"]),
        panel("India polar stations", "institutional-ladder", [
            "DAKSHIN GANGOTRI (1983) -> first station, now decommissioned/buried in ice",
            "MAITRI (1989) -> Schirmacher Oasis, Antarctica; operational",
            "BHARATI (2012) -> Larsemann Hills, Antarctica; operational",
            "HIMADRI (2008) -> Ny-Alesund, Svalbard; Arctic; HIMANSH -> Spiti, HP",
        ], ["India polar research programme"]),
        panel("India polar legal framework", "process-flow", [
            "ANTARCTIC TREATY 1959 -> India acceded 1983; consultative party",
            "INDIAN ANTARCTIC ACT 2022 -> domestic legislation for polar activities",
            "ARCTIC POLICY 2022 -> six pillars; observer in Arctic forum",
            "RESEARCH FOCUS -> teleconnections: Arctic ice loss to Indian monsoon disruption",
        ], ["India polar legal framework"]),
        panel("Polar climate answer spine", "answer-spine", [
            "DEFINE -> cold desert north of Arctic Circle; ice-cap vs tundra subdivisions",
            "DISTINGUISH -> Arctic ocean vs Antarctic continent; floating vs grounded ice",
            "EXPLAIN -> ice-albedo feedback, permafrost carbon, four transmission channels",
            "QUALIFY -> India's Ladakh analogue, polar research, 2021 PYQ four-channel spine",
        ], ["2021 PYQ demand and answer spine"]),
    ],
    [
        "tundra", "ice-cap", "permafrost", "Arctic amplification",
        "ice-albedo feedback", "cold desert", "reindeer moss",
        "Ladakh", "rain-shadow", "Changpa", "NCPOR",
        "Maitri", "Bharati", "Himadri",
    ],
    (
        "The 2021 GS-I Q15 demand on melting Arctic ice and Antarctic glaciers "
        "and weather patterns is the only verified PYQ owned by Geography "
        "Topic 25. It requires the Arctic-Antarctic distinction, the "
        "amplification mechanism and four transmission channels graded by "
        "confidence. No additional PYQ is fabricated."
    ),
    [
        (
            "2021",
            "GS-I",
            "Discuss the effects of melting Arctic ice and Antarctic glaciers on weather patterns.",
            "Verified from _PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md",
            "The polar regions transmit change through four channels: (1) Sea-level — "
            "only grounded ice loss raises sea level; ice-shelf loss accelerates discharge "
            "by removing buttressing. (2) Atmospheric and oceanic circulation — reduced "
            "equator-to-pole temperature gradient may weaken and meander the jet stream, "
            "but this is an active research question, not settled science. (3) Carbon — "
            "permafrost thaw creates a second self-reinforcing feedback releasing CO2 and "
            "methane. (4) Access — retreating sea ice opens routes and resource shelves. "
            "The Arctic-Antarctic asymmetry (ocean versus continent; sea ice versus "
            "grounded ice) must open the answer. Confidence declines from sea-level through "
            "carbon to the weather-pattern link, and an answer that grades this uncertainty "
            "is stronger than one that asserts all four equally.",
        ),
    ],
    [
        "https://www.noaa.gov/arctic-report-card",
        "https://nsidc.org/arcticseaicenews/",
        "https://ncpor.res.in/",
    ],
    (
        "NOAA Arctic Report Card, NSIDC Sea Ice News and NCPOR expedition "
        "data are used only to establish Arctic amplification and India's "
        "polar research as live current anchors. No specific sea-ice extent, "
        "mass-loss rate or warming multiple is quoted without a dated source."
    ),
)
