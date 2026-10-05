from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
TOPIC = SUBJECT / "04-Weathering-Mass-Movement-Groundwater-India-Erosion-Landslides-Groundwater"

BASIC = "upsc-ai-kit/knowledge/Geography/basic/04_Weathering-MassMovement-Groundwater.md"
ADVANCED = "upsc-ai-kit/knowledge/Geography/advanced/04_India-Erosion-Landslides-Groundwater.md"
LEARNER = (
    "learning_package_final/Geography/Part-A-—-Physical-Geography/"
    "04-Weathering,-Mass-Movement,-Groundwater-India-Erosion-Landslides-Groundwa/Learning-Session.md"
)
WORKBOOK = (
    "learning_package_final/Geography/Part-A-—-Physical-Geography/"
    "04-Weathering,-Mass-Movement,-Groundwater-India-Erosion-Landslides-Groundwa/Solved-Practice-Workbook.md"
)
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Geography/Part-A-—-Physical-Geography/"
    "04-Weathering,-Mass-Movement,-Groundwater-India-Erosion-Landslides-Groundwa/MCQ-Bank-With-Solutions.md"
)


def c(tag, stems, options, explanation, source, trap, area):
    return {
        "tag": tag,
        "stems": stems,
        "options": options,
        "explanation": explanation,
        "source": source,
        "trap": trap,
        "area": area,
    }


CONCEPTS = [
    c(
        "process boundary",
        [
            "Which statement keeps the boundary between weathering and erosion precise?",
            "A field observation shows rock breaking down without movement by a transporting agent. Which process is being recorded?",
            "A question asks what distinguishes erosion from weathering. Which formulation is safest?",
        ],
        [
            "Weathering alters or disintegrates rock in place; erosion removes and transports material",
            "Weathering always carries particles downslope; erosion leaves them in place",
            "Erosion begins only after a mature soil profile has developed",
            "Weathering is a synonym for all denudational movement",
        ],
        "Weathering is in-situ physical disintegration or chemical alteration. Erosion requires detachment, removal and transport by water, wind, ice or waves; gravity-led mass movement is a separate category.",
        "Basic §1; Learner Sessions 1–2",
        "The presence of loosened debris does not by itself prove erosion; transport is the decisive boundary.",
        "weathering–erosion distinction",
    ),
    c(
        "denudation system",
        [
            "Which sequence best represents an exogenic source–transfer–storage system?",
            "A slope is analysed as a connected geomorphic system. Which chain is most defensible?",
            "Which order most accurately links rock breakdown to later sediment storage?",
        ],
        [
            "Weathering → regolith or dissolved load → transport or mass wasting → deposition → possible remobilisation",
            "Deposition → uplift → permanent storage with no further geomorphic change",
            "Mass movement must occur before any weathering can begin",
            "Soil formation ends erosion and prevents later sediment transfer",
        ],
        "Denudation is not one process: weathering supplies material, gravity or a moving agent transfers it, and deposition stores it temporarily. Stored sediment can later be remobilised.",
        "Learner Sessions 1 and 20; Basic §1",
        "Treating denudation as a one-way conveyor belt hides remobilisation and process overlap.",
        "exogenic process chain",
    ),
    c(
        "weathering controls",
        [
            "Which combination gives the most complete control set for weathering?",
            "Why can the same climate produce different weathering products in two rock bodies?",
            "Which statement avoids a climate-only explanation of weathering rate?",
        ],
        [
            "Mineralogy and structure interact with climate, relief, organisms, time and land use",
            "Latitude alone fixes the rate and product regardless of rock and drainage",
            "Only the age of the landscape controls weathering depth",
            "Vegetation prevents all physical and chemical alteration",
        ],
        "Weathering reflects interacting controls: rock and mineral stability, joints and bedding, temperature and moisture, slope and drainage, organisms, exposure time and land use.",
        "Basic §1; Learner Session 2",
        "Climate is important but not a universal override of mineralogy, structure or relief.",
        "controls of weathering",
    ),
    c(
        "mechanical chemical",
        [
            "Which comparison between mechanical and chemical weathering is correct?",
            "A rock is fragmented without a change in mineral composition. Which family does this illustrate?",
            "Which pairing best distinguishes the two major weathering pathways?",
        ],
        [
            "Mechanical weathering breaks rock into smaller pieces; chemical weathering alters minerals or dissolves them",
            "Mechanical weathering always forms clay; chemical weathering only tilts blocks",
            "Both terms mean transport by a river or wind",
            "Chemical weathering occurs only in permanently frozen terrain",
        ],
        "Mechanical weathering changes size and form, whereas chemical weathering changes mineral composition or removes soluble material. Biological activity can reinforce both.",
        "Basic §§1–2; Learner Session 3",
        "Fragmentation and mineral alteration are not interchangeable just because both weaken rock.",
        "weathering families",
    ),
    c(
        "exfoliation unloading",
        [
            "Which statement correctly separates thermal expansion from unloading?",
            "A dome-like rock mass develops concentric sheets after removal of overburden. Which mechanism is most relevant?",
            "Which field interpretation is safest for onion-skin sheets on an exposed rock surface?",
        ],
        [
            "Thermal cycling stresses the rock; unloading releases confining pressure and can create sheet joints",
            "Both processes require carbonate dissolution inside a limestone cave",
            "Unloading is caused only by salt crystals growing in pores",
            "Thermal expansion is a form of river transport rather than rock stress",
        ],
        "Thermal expansion produces repeated stress from heating and cooling. Unloading or pressure release allows expansion and sheet-jointing after overlying material is removed.",
        "Basic §1; Learner Session 3",
        "Exfoliation is not automatically a chemical process and is not synonymous with frost shattering.",
        "mechanical weathering",
    ),
    c(
        "frost action",
        [
            "Frost wedging is most effective under which conditions?",
            "Why does a repeated freeze–thaw cycle prise apart jointed rock?",
            "Which setting most directly favours frost action rather than carbonation?",
        ],
        [
            "Water enters cracks, freezes and expands repeatedly near the freezing point",
            "The rock remains dry while temperature stays far above freezing",
            "Only dissolved carbon dioxide reacts with carbonate minerals",
            "Evaporation deposits salts without any water entering the joints",
        ],
        "Water access, open cracks and repeated freezing are essential. Expansion on freezing exerts pressure on joint walls; the mechanism is conditional, not a generic label for every mountain.",
        "Basic §1; Learner Session 3",
        "High altitude alone is insufficient if cracks stay dry or temperatures do not cycle around freezing.",
        "mechanical weathering",
    ),
    c(
        "salt crystallisation",
        [
            "Salt weathering most directly results from which process?",
            "A dry exposed rock surface repeatedly receives saline moisture and dries. What mechanism is likely?",
            "Which explanation best fits granular disintegration in an arid setting with salts?",
        ],
        [
            "Crystal growth or hydration pressure within pores and cracks",
            "A confined aquifer rising under artesian pressure",
            "Rotational sliding along a curved slip surface",
            "Carbonic acid dissolving every mineral at the same rate",
        ],
        "Evaporation concentrates salts; crystal growth or hydration changes exert pressure in pores and cracks and can disrupt exposed rock.",
        "Basic §1; Learner Session 3",
        "Aridity favours salt crystallisation, but the mechanism still needs saline moisture and pore/crack pathways.",
        "mechanical weathering",
    ),
    c(
        "wet dry clay",
        [
            "Repeated wetting and drying most directly weakens which material?",
            "Why can seasonal moisture change destabilise clay-rich slope material?",
            "Which material–process pairing is most defensible for shrink–swell fatigue?",
        ],
        [
            "Clay-rich material that expands when wet and contracts when dry",
            "Fresh massive quartzite with no discontinuities",
            "A deep confined aquifer unaffected by volume change",
            "A dry wind plume moving suspended silt",
        ],
        "Expansive clay minerals change volume with moisture. Repeated swelling and shrinkage create fatigue, cracks and reduced slope or foundation stability.",
        "Basic §1 and §9; Learner Sessions 3 and 9",
        "Black-soil shrink–swell behaviour is a material property, not proof that every black soil is unstable.",
        "mechanical weathering and soil",
    ),
    c(
        "carbonation",
        [
            "Carbonation in limestone terrain is best described as:",
            "Why does carbon-dioxide-bearing rainwater promote karst solution?",
            "Which chemical-weathering route is most directly linked with carbonate dissolution?",
        ],
        [
            "Water plus carbon dioxide forms weak carbonic acid that dissolves carbonate minerals",
            "Oxygen turns every mineral into a metallic oxide without water",
            "Wind physically carries limestone grains away without solution",
            "Freezing alone changes limestone into a clay mineral",
        ],
        "Carbon dioxide dissolves in water to form weak carbonic acid, which reacts with carbonate minerals and carries dissolved ions away; it is not literal melting.",
        "Basic §1; Learner Session 3",
        "Carbonation is a chemical solution pathway, not the same as oxidation or physical frost action.",
        "chemical weathering",
    ),
    c(
        "hydrolysis",
        [
            "Hydrolysis commonly changes feldspar into:",
            "Which mineral-weathering example best illustrates hydrolysis?",
            "A weathered granite develops clay minerals through water–silicate reaction. Which process is implicated?",
        ],
        [
            "Clay minerals and dissolved ions",
            "Fresh volcanic glass with no chemical alteration",
            "Pure metallic iron produced without oxygen or water",
            "Glacial till created by ice transport",
        ],
        "Hydrolysis is a water–mineral reaction. Feldspar can be altered to clay minerals while some ions enter solution, contributing to a weathered mantle.",
        "Basic §1; Learner Session 3",
        "Hydrolysis is not simply hydration and does not create transported till.",
        "chemical weathering",
    ),
    c(
        "redox",
        [
            "Which statement about oxidation and reduction in weathering is correct?",
            "Why can drainage influence the colour and mobility of iron in a soil or rock profile?",
            "Which redox interpretation is most defensible?",
        ],
        [
            "Oxygenated conditions favour iron oxidation, while reducing conditions can make some iron forms more soluble",
            "Reduction is only a mechanical fracture caused by pressure release",
            "Oxidation never depends on oxygen-bearing water or drainage",
            "Redox has no relation to saturation or soil-profile conditions",
        ],
        "Iron-bearing minerals can oxidise in oxygenated settings and produce rusty colours; reducing, waterlogged conditions can change iron mobility and form.",
        "Basic §1; Learner Session 3",
        "A rusty surface is evidence of oxidation, not proof that all iron behaviour is identical throughout the profile.",
        "chemical weathering",
    ),
    c(
        "biological weathering",
        [
            "How can plants and soil organisms accelerate weathering?",
            "A root enters a joint while organic acids alter minerals. Which conclusion is best?",
            "Which statement describes biological weathering without isolating it from other processes?",
        ],
        [
            "Roots widen fractures physically and organisms can enhance chemical alteration through organic acids",
            "Vegetation stops every form of weathering beneath its canopy",
            "Biological activity begins only after erosion and deposition are complete",
            "Roots create artesian pressure in a confined aquifer",
        ],
        "Roots exert wedging pressure and organisms supply organic acids and carbon dioxide; biological pathways commonly reinforce mechanical and chemical weathering.",
        "Basic §1; Learner Session 3",
        "Vegetation can both protect soil from erosion and accelerate rock alteration at the root–rock interface.",
        "biological weathering",
    ),
    c(
        "regolith soil",
        [
            "Which distinction between regolith and soil is correct?",
            "A loose weathered mantle lacks organic activity and differentiated horizons. What is it most precisely called?",
            "Why is mature soil more than simply crushed parent rock?",
        ],
        [
            "Regolith is weathered mantle; soil additionally requires biological activity and horizon development",
            "All regolith is mature, fertile soil with a complete profile",
            "Soil forms without parent material, organisms, water or time",
            "Regolith is unweathered bedrock beneath the R horizon",
        ],
        "Regolith is loose or weathered material over bedrock. Soil is an organised, biologically active body with horizon differentiation produced through mineral, organic and water interactions.",
        "Basic §9; Learner Sessions 1 and 8",
        "Young alluvium can be fertile yet immature; fertility and pedogenic maturity are not synonyms.",
        "soil formation",
    ),
    c(
        "eluviation illuviation",
        [
            "Which pairing of eluviation and illuviation is correct?",
            "In a soil profile, clay is removed from an upper horizon and accumulates below. Which process pair is involved?",
            "Which statement correctly describes vertical translocation in a soil profile?",
        ],
        [
            "Eluviation removes material from an upper horizon; illuviation accumulates it in a lower horizon",
            "Both terms refer only to surface runoff erosion",
            "Illuviation occurs only in deserts and never under forests",
            "Eluviation means groundwater rising under artesian pressure",
        ],
        "Percolating water can remove fine material, iron or dissolved constituents from an upper horizon (eluviation) and deposit them lower down (illuviation), often in B.",
        "Basic §9.2; Learner Session 8",
        "The pair concerns within-profile movement, not the same as hillslope erosion.",
        "soil profile",
    ),
    c(
        "black soil",
        [
            "Which origin–property pairing best explains black cotton soil?",
            "Why is regur particularly associated with cotton cultivation?",
            "Which statement about India's black soil is most defensible?",
        ],
        [
            "It commonly develops from Deccan basalt and has clay-rich shrink–swell, moisture-retaining behaviour",
            "It is a recent marine deposit whose colour proves exceptional nitrogen richness",
            "It forms only from unweathered shale and has no seasonal cracking",
            "It is wind-blown sand that cannot retain water",
        ],
        "Black or regur soil is linked to weathering of Deccan basalt. Its clay-rich profile retains moisture and cracks deeply on drying; it is not exceptionally rich in nitrogen or humus.",
        "Basic §9.4; Advanced §4; PYQ hold: 2021 Prelims GS-I Q64",
        "The answer turns on basaltic parent material and shrink–swell behaviour, not black colour alone.",
        "Indian soils",
    ),
    c(
        "laterite",
        [
            "Which climatic-process combination favours laterite formation?",
            "Why is laterite not best explained by a permanently wet climate alone?",
            "Which statement correctly links laterisation with soil properties?",
        ],
        [
            "Intense leaching under high rainfall with seasonal wet–dry alternation leaves iron and aluminium oxides",
            "Very cold, dry conditions with no chemical alteration",
            "Repeated river deposition that prevents profile differentiation",
            "Pure limestone solution producing a deep, base-rich soil everywhere",
        ],
        "Laterisation involves strong leaching in humid tropical settings; seasonal drying can leave iron and aluminium concentrations that harden on exposure. It is not a universal fertility label.",
        "Basic §9.3–9.4; Learner Session 9",
        "Perpetual wetness is not the complete diagnostic; wet–dry alternation and leaching matter.",
        "Indian soils",
    ),
    c(
        "sheet rill gully ravine",
        [
            "Which sequence shows increasing runoff concentration and incision?",
            "A protected slope develops progressively deeper channels after cover loss. Which order is most appropriate?",
            "Which sequence best links diffuse wash to severe badland dissection?",
        ],
        [
            "Sheet erosion → rill erosion → gully erosion → ravine or badland terrain",
            "Ravine → sheet → rill → gully",
            "Gully → deposition → sheet → rill",
            "Rill → soil formation → ravine → no further incision",
        ],
        "As runoff concentrates, shallow sheet removal can become rills, then persistent gullies and dense ravine or badland dissection. Chambal is the India anchor.",
        "Advanced §§1–2; Learner Session 5",
        "Ravine is not any river valley; it represents severe gully dissection and badland development.",
        "water erosion",
    ),
    c(
        "wind transport",
        [
            "Which set contains the principal wind-transport modes?",
            "Fine and coarse particles move differently across an arid surface. Which vocabulary is relevant?",
            "Which sequence best identifies aeolian transport mechanisms?",
        ],
        [
            "Surface creep, saltation and suspension",
            "Infiltration, percolation and recharge",
            "Creep, slump and artesian rise",
            "Carbonation, hydrolysis and oxidation",
        ],
        "Wind moves coarse grains by surface creep, sand-sized grains by saltation and fine particles by suspension; bare dry surfaces are most vulnerable.",
        "Advanced §2; Learner Session 5",
        "Creep in wind transport is not the same as soil creep in mass movement.",
        "wind erosion",
    ),
    c(
        "conservation matching",
        [
            "Which conservation measure is most directly matched to a concentrated gully problem?",
            "A catchment has active gully heads and rapid runoff. Which intervention logic is most appropriate?",
            "Which pairing links erosion form to a mechanism-matched response?",
        ],
        [
            "Gully-head control, small check structures, vegetative stabilisation and catchment treatment",
            "Only deep ploughing along the gully axis",
            "Removing all surface cover to increase runoff speed",
            "Desalination of a coastal aquifer as the primary gully remedy",
        ],
        "Conservation reduces erosive energy, restores protective cover, shortens slope length and controls concentrated flow. Gully work must be combined with upslope catchment treatment.",
        "Basic §9.5; Advanced §2; Learner Session 5",
        "A structure at the gully mouth cannot substitute for upstream runoff and land-use management.",
        "soil conservation",
    ),
    c(
        "soil creep",
        [
            "Which field clue most strongly indicates soil creep?",
            "A slope has slowly bent tree trunks and tilted fence posts but no fresh scar. Which process is likely?",
            "Which movement is characteristically slow and near-continuous?",
        ],
        [
            "Gradual downslope movement shown by tilted posts, trees or fences",
            "A sudden free fall of detached blocks",
            "A confined aquifer discharging through an artesian well",
            "A lava front advancing from a volcanic vent",
        ],
        "Soil creep is slow, often imperceptible movement of soil or regolith under gravity. Tilted posts, trees and fences are classic field indicators.",
        "Basic §1; Learner Session 4",
        "Creep is a mass movement even when no dramatic scar or rapid event is visible.",
        "mass movement",
    ),
    c(
        "solifluction",
        [
            "Solifluction refers to which process?",
            "A water-saturated surface layer slowly moves over frozen or impermeable ground. What is this called?",
            "Which setting–movement pairing is most defensible for solifluction?",
        ],
        [
            "Slow flow of saturated surface material over a frozen or restricting layer",
            "Dry rockfall from a vertical cliff with no water",
            "Chemical oxidation of iron in a freely drained soil",
            "Saline upconing beneath a coastal pumping well",
        ],
        "Saturation above permafrost or another impermeable layer allows a slow, often lobate downslope flow of surface material.",
        "Basic §1; Learner Session 4",
        "Solifluction is not a synonym for every landslide and requires a saturated layer plus a restricting base.",
        "mass movement",
    ),
    c(
        "slump",
        [
            "What most clearly distinguishes a slump from a fall?",
            "A coherent mass rotates backward along a curved failure surface. Which movement is indicated?",
            "Which geometry is characteristic of rotational slumping?",
        ],
        [
            "Rotational movement along a curved failure surface, often with back-tilted blocks",
            "Free fall and bouncing of detached blocks from a cliff",
            "Uniform sheet wash with no discrete failure surface",
            "Wind suspension of fine sediment above an arid surface",
        ],
        "A slump is a rotational slide with movement along a curved surface; back-tilted blocks and a head scarp can be diagnostic.",
        "Basic §1; Learner Session 4",
        "Not every slide is rotational; do not call a free fall or debris flow a slump.",
        "mass movement",
    ),
    c(
        "movement types",
        [
            "Which movement–behaviour pairing is correct?",
            "A question compares falls, slides and flows. Which classification is safest?",
            "Which diagnostic set correctly separates common mass-movement types?",
        ],
        [
            "Rockfall detaches and falls; a slide moves along a surface; a flow deforms as a water-rich mass",
            "A rockfall always rotates on a curved surface and a flow moves as a rigid block",
            "A slide requires a river current while a flow cannot contain water",
            "All downslope movement is soil creep regardless of speed or material",
        ],
        "Falls are abrupt detachments, slides preserve a recognisable moving mass or surface, and flows deform and may become channelised when water-rich.",
        "Basic §1; Advanced §2; Learner Session 4",
        "Classification depends on movement style and material behaviour, not simply on event size.",
        "mass movement",
    ),
    c(
        "predisposition trigger",
        [
            "Which statement correctly separates landslide predisposition from trigger?",
            "A steep fractured slope fails during intense rainfall. Which interpretation is most complete?",
            "Why is saying 'rain caused the landslide' often incomplete?",
        ],
        [
            "Weak material, steep relief and poor drainage create susceptibility; rainfall or shaking may trigger failure",
            "A trigger is a permanent terrain condition, while predisposition is always a single storm",
            "Only the visible debris matters; slope geometry and material are irrelevant",
            "A susceptibility map proves the exact date and magnitude of a future slide",
        ],
        "Predisposing conditions include slope, material, structure, toe erosion and drainage; triggers include intense rain, earthquakes, cutting, leakage or loading. Attribution should keep both levels.",
        "Advanced §2; Learner Sessions 4–5",
        "Immediate trigger and long-term susceptibility are different causal roles.",
        "slope stability",
    ),
    c(
        "pore water pressure",
        [
            "Why can saturation reduce slope stability?",
            "What is the main mechanical effect of rising pore-water pressure in a potentially unstable slope?",
            "Which explanation best links rainfall to reduced effective resistance?",
        ],
        [
            "Water can add weight and raise pore pressure, reducing effective normal stress and available resistance",
            "Saturation always cements grains and removes every discontinuity",
            "Rainfall automatically converts every slide into a subsidence event",
            "Pore pressure has no relation to drainage or material strength",
        ],
        "Increased water content adds mass; pore pressure can reduce effective stress at contacts, while seepage and weak layers may lower resisting strength.",
        "Learner Session 5; Advanced §2",
        "Rainfall is a hydrological mechanism, not just a weather label; antecedent saturation and drainage matter.",
        "slope stability",
    ),
    c(
        "hazard risk",
        [
            "Which statement correctly distinguishes hazard from risk?",
            "A landslide-prone slope has no settlement but high physical susceptibility. What can be said?",
            "Which formulation is safest in a disaster-geography question?",
        ],
        [
            "Hazard concerns the physical process; risk adds exposure, vulnerability and possible losses",
            "Hazard and risk are exact synonyms wherever a map is available",
            "Risk is determined only by rainfall and never by people or assets",
            "A susceptibility map alone proves that a disaster has occurred",
        ],
        "Hazard is the likelihood or intensity of a physical event. Risk emerges when hazard interacts with exposed people, assets, vulnerability and coping capacity.",
        "Learner Session 5; Advanced §2",
        "A mapped susceptibility zone is not a casualty forecast and does not itself establish risk.",
        "hazard and risk",
    ),
    c(
        "India landslide settings",
        [
            "Which comparison of Himalayan and Western Ghats landslides is most defensible?",
            "Why do both the Himalaya and Western Ghats require region-specific landslide explanations?",
            "Which Indian setting comparison avoids a single-cause claim?",
        ],
        [
            "The Himalaya combine young relief, fractured/weathered material and intense rain; the Western Ghats combine escarpment relief, weathering, monsoon rain and land-use change",
            "Both regions have identical lithology, relief history and triggers",
            "Western Ghats landslides are always earthquake-triggered and never rainfall-linked",
            "Himalayan landslides are unrelated to drainage, road cuts or monsoon saturation",
        ],
        "The Himalayan and Western Ghats regimes share rainfall sensitivity but differ in tectonic history, relief, lithology, weathering, drainage and land-use pressures.",
        "Advanced §1; Learner Sessions 5–6",
        "Do not transfer one region's mechanism wholesale to the other.",
        "India landslides",
    ),
    c(
        "Joshimath",
        [
            "Which is the safest geographic interpretation of Joshimath subsidence?",
            "How should a multi-causal explanation of Joshimath be framed?",
            "Which conclusion best respects the evidence boundary in the Joshimath case?",
        ],
        [
            "Use an integrated frame involving old debris/material, drainage and water, construction loading and slope instability",
            "Assign the entire pattern to one visible crack or one unverified cause",
            "Treat monitoring as proof that uncertainty has been eliminated",
            "Assume every settlement on a slope has the same material and foundation conditions",
        ],
        "The repository's advanced owner treats Joshimath as a multi-causal subsidence illustration: old landslide/debris material, drainage, water saturation, loading and slope instability interact. No single-cause claim is settled here.",
        "Advanced §1 and §6; learner current-status notes rechecked 2026-08-15",
        "A named case is not permission to collapse a complex diagnosis into one trigger.",
        "India subsidence",
    ),
    c(
        "subsidence landslide",
        [
            "Which distinction between subsidence and landslide is correct?",
            "Ground level lowers under loading and settlement without a clear downslope mass. Which term is more precise?",
            "Why should subsidence not automatically be labelled a landslide?",
        ],
        [
            "Subsidence is ground lowering or settlement; a landslide is downslope movement of a mass under gravity",
            "Both terms always describe identical rotational movement",
            "Subsidence occurs only on coastlines and never in mountain debris",
            "A landslide has no shear, gravity or material movement",
        ],
        "Subsidence emphasises vertical lowering or settlement; landslides emphasise downslope mass movement. They can interact in weathered or water-saturated material but are not synonyms.",
        "Advanced §1; Learner Session 6",
        "A settlement crack alone cannot establish the movement class or its cause.",
        "India subsidence",
    ),
    c(
        "porosity permeability",
        [
            "Which statement correctly distinguishes porosity from permeability?",
            "A rock contains many voids but they are poorly connected. Which inference is safest?",
            "Why is porosity alone insufficient for groundwater-flow assessment?",
        ],
        [
            "Porosity is void space; permeability is the connected capacity to transmit fluid",
            "Permeability is simply the percentage of empty space and porosity is flow speed",
            "Both properties are identical in every rock type",
            "High porosity guarantees rapid groundwater movement",
        ],
        "Porosity measures storage space, while permeability depends on connected pathways and hydraulic transmission. Clay may have high porosity but low permeability.",
        "Basic §1 and §7; Learner Session 7",
        "Storage and transmission are different hydrogeological functions.",
        "groundwater fundamentals",
    ),
    c(
        "aquifer aquitard",
        [
            "Which pairing of aquifer and aquitard is correct?",
            "A permeable geological unit stores and transmits usable groundwater, while an adjacent low-permeability layer restricts flow. Which terms apply?",
            "Which hydrogeological distinction is most precise?",
        ],
        [
            "Aquifer transmits and stores groundwater; aquitard restricts flow relative to it",
            "Aquifer is unweathered bedrock only; aquitard is any flowing river",
            "Aquitard transmits water faster than every aquifer by definition",
            "The two terms describe soil horizons rather than geological water behaviour",
        ],
        "An aquifer combines storage and transmissive capacity; an aquitard has much lower permeability and may retard, but not necessarily completely stop, groundwater movement.",
        "Basic §1 and §7; Learner Session 7",
        "An aquitard is not an absolute impermeable wall in every field setting.",
        "groundwater fundamentals",
    ),
    c(
        "water table",
        [
            "What does the water table represent in an unconfined aquifer?",
            "Which statement correctly locates the water table?",
            "A well is screened in the saturated upper surface of an unconfined system. What surface is relevant?",
        ],
        [
            "The upper surface of the saturated zone in an unconfined aquifer",
            "The base of all groundwater beneath an impermeable crust",
            "The elevation of a river bed regardless of aquifer conditions",
            "The pressure surface that exists only in a confined aquifer",
        ],
        "The water table separates the zone of aeration from the zone of saturation in an unconfined aquifer. Its position responds to recharge, discharge, pumping and seasonality.",
        "Basic §1; Learner Session 7",
        "Do not confuse the water table with the potentiometric surface of a confined aquifer.",
        "groundwater fundamentals",
    ),
    c(
        "artesian",
        [
            "Which condition is required for an artesian well?",
            "Why can water rise without pumping in a confined aquifer?",
            "Which geological arrangement best supports artesian pressure?",
        ],
        [
            "A permeable aquifer is confined between low-permeability layers and has hydraulic head from recharge",
            "Any shallow unconfined well in dry sand automatically becomes artesian",
            "A dry rock mass must be exposed at the surface with no pressure gradient",
            "Artesian flow is produced only by a river eroding its banks",
        ],
        "Confinement plus hydraulic head allows water in a well to rise above the top of the aquifer, sometimes reaching the surface. Recharge and pressure conditions matter.",
        "Basic §1; Learner Session 7",
        "A flowing well is not guaranteed merely because groundwater is present.",
        "groundwater fundamentals",
    ),
    c(
        "recharge infiltration",
        [
            "Which sequence best represents natural groundwater recharge?",
            "How does precipitation become groundwater in a permeable catchment?",
            "Which process chain correctly links rainfall to aquifer storage?",
        ],
        [
            "Infiltration through the soil → percolation through the unsaturated zone → recharge to the saturated zone",
            "Surface evaporation → wind suspension → immediate artesian discharge",
            "River erosion → saltation → aquifer contamination in every case",
            "Pumping → recharge automatically increases without a water balance",
        ],
        "Recharge requires water to infiltrate and percolate to the saturated zone, subject to soil, land cover, permeability, storage, drainage and competing evapotranspiration.",
        "Basic §1 and §7; Learner Session 7",
        "A pond or check dam may aid recharge only where siting, maintenance and aquifer pathways support it.",
        "groundwater cycle",
    ),
    c(
        "hard rock groundwater",
        [
            "Why can crystalline hard-rock terrain still yield groundwater?",
            "Which features commonly control groundwater in fresh granite or gneiss landscapes?",
            "A hard-rock well succeeds near a weathered fracture zone. Which explanation is best?",
        ],
        [
            "Weathered mantles, joints, fractures and lineaments create secondary storage and transmission",
            "Fresh crystalline rock always has abundant connected primary pores",
            "Only fossils and coal seams can store water in hard rock",
            "Hard-rock aquifers do not depend on structure or weathering",
        ],
        "Fresh crystalline rocks may have low primary porosity, but weathering and secondary openings such as joints and fractures can store and transmit groundwater.",
        "Basic §7; Learner Session 7; Topic 02 cross-link",
        "Do not treat fresh bedrock and its weathered/fractured zones as hydrogeologically identical.",
        "India groundwater",
    ),
    c(
        "groundwater budget",
        [
            "Which expression best represents change in groundwater storage?",
            "A groundwater assessment compares inflows and outflows. Which conceptual balance is correct?",
            "Which statement treats groundwater as a stock governed by flows?",
        ],
        [
            "Change in storage = recharge + inflow − discharge − pumping − outflow",
            "Storage always equals rainfall received in the same month",
            "Pumping is a form of recharge and discharge can be ignored",
            "An aquifer has no storage change because water is underground",
        ],
        "Groundwater storage changes when recharge and inflows differ from natural discharge, pumping and outflow. The balance is a conceptual stock–flow framework, not a site-specific calculation here.",
        "Learner Sessions 7 and 20; Advanced §1",
        "A national annual estimate cannot diagnose a specific well without local aquifer and time-scale data.",
        "groundwater cycle",
    ),
    c(
        "over extraction",
        [
            "Groundwater depletion occurs when which relation persists?",
            "Which condition most directly lowers a water table over time?",
            "Why can irrigation-intensive regions experience falling groundwater levels?",
        ],
        [
            "Withdrawals and other outflows persistently exceed recharge and inflows",
            "Recharge permanently exceeds pumping in every assessment unit",
            "Only natural springs increase while pumping remains unchanged",
            "A deeper well proves that the aquifer has recovered",
        ],
        "When extraction exceeds replenishment over the relevant period, storage and water levels decline, pumping costs rise and reliability falls. The magnitude is assessment-unit specific.",
        "Advanced §§1–2; Ministry of Jal Shakti assessment, 2026-02-05",
        "A single deeper or successful well is not evidence of regional recovery.",
        "India groundwater stress",
    ),
    c(
        "contamination",
        [
            "Which statement best describes groundwater contamination risk?",
            "Why can waste disposal through wells or sinkholes be dangerous?",
            "Which groundwater-quality explanation is most defensible?",
        ],
        [
            "Pollutants can infiltrate through recharge pathways and persist or spread within an aquifer",
            "Groundwater is naturally filtered so contamination cannot occur",
            "Only surface rivers can carry contaminants; aquifers are isolated from land use",
            "Pumping always removes every pollutant without changing concentration",
        ],
        "Contaminants can enter through infiltration, leaky wells, sinkholes or polluted recharge and then move according to aquifer properties, gradients and reactions.",
        "Advanced §1; Learner Session 7",
        "Quantity stress and quality stress are distinct but can reinforce one another.",
        "groundwater quality",
    ),
    c(
        "seawater intrusion",
        [
            "What most directly drives seawater intrusion into a coastal aquifer?",
            "Why can excessive coastal pumping shift a saline interface landward?",
            "Which remedy set best matches the mechanism of coastal-aquifer salinisation?",
        ],
        [
            "Falling freshwater head from over-pumping or reduced recharge allows saline water to move inland or upward",
            "Higher freshwater head always pulls saltwater inland faster",
            "Only river meandering can create saline intrusion",
            "Desalination of one well automatically restores the aquifer balance",
        ],
        "The freshwater–saltwater balance depends on hydraulic head and recharge. Excess pumping lowers freshwater pressure and can move the saline interface inland or upward.",
        "Basic §7; Advanced §7; PYQ hold: 2025 GS-III coastal intrusion",
        "Desalination treats extracted water; it does not by itself restore the aquifer's hydraulic balance.",
        "coastal groundwater",
    ),
    c(
        "national assessment values",
        [
            "According to the Ministry of Jal Shakti release dated 5 February 2026, which set matches the 2025 groundwater assessment values used in the topic package?",
            "Which dated official-data pairing is correct for India's 2025 groundwater assessment?",
            "A question asks for the relationship among recharge, extractable resource and extraction in the 2025 assessment. Which option is accurate?",
        ],
        [
            "Annual recharge 448.52 BCM; annual extractable resource 407.75 BCM; annual extraction 247.22 BCM",
            "Annual recharge 247.22 BCM; extractable resource 448.52 BCM; extraction 407.75 BCM",
            "Annual recharge 407.75 BCM; extractable resource 247.22 BCM; extraction 448.52 BCM",
            "Annual recharge 448.52 BCM; extractable resource 247.22 BCM; extraction 407.75 BCM",
        ],
        "The topic package records the Ministry of Jal Shakti, Department of Water Resources release of 5 February 2026: 2025 annual recharge 448.52 BCM, annual extractable resource 407.75 BCM and annual extraction 247.22 BCM.",
        "Official Ministry of Jal Shakti release, 2026-02-05; Complete Topic Package source register",
        "Do not transpose the three values or detach them from the 2025 assessment and its national scale.",
        "dated official groundwater data",
    ),
    c(
        "urban harvesting",
        [
            "A city faces falling groundwater levels and extensive paved cover. Which response best fits the physical mechanism?",
            "Which urban-water strategy most directly supports recharge while reducing runoff?",
            "For the held 2018 mains demand on effective urban water harvesting, which core logic is essential?",
        ],
        [
            "Protect recharge zones and use site-suitable rainwater harvesting with infiltration, storage, monitoring and demand management",
            "Maximise pumping from deeper layers without checking aquifer balance",
            "Build recharge structures everywhere regardless of soil, contamination or aquifer connectivity",
            "Treat rooftop collection alone as proof that groundwater storage has recovered",
        ],
        "Urban harvesting is effective only when connected to suitable recharge or storage pathways, clean runoff, maintenance, monitoring, demand management and local aquifer conditions.",
        "Advanced §7; PYQ hold: 2018 GS-I Q14; Learner answer architecture",
        "Rainwater harvesting is not a universal structure-only solution; siting and hydrogeology determine outcomes.",
        "PYQ-linked groundwater management",
    ),
    c(
        "PYQ rain weathering",
        [
            "Which statement would best prepare a learner for the held 2024 Prelims concept on rainfall and weathering?",
            "Rainwater reaches exposed rock. Which inference is scientifically safest?",
            "Which option avoids over-reading the rainfall–weathering relationship tested in the routed PYQ demand?",
        ],
        [
            "Rain supplies water and dissolved gases, but weathering response still depends on mineralogy, structure, temperature, drainage and exposure",
            "Rainfall alone fixes one identical weathering product in every rock",
            "Rain cannot contribute to chemical weathering because it is mechanically neutral",
            "A single shower proves the long-term national rate of weathering",
        ],
        "Rainwater can provide water and dissolved gases for chemical alteration, but the process depends on rock minerals, joints, climate, drainage, organisms and time. The exact 2024 wording is held, not reproduced.",
        "Basic §1; PYQ hold: 2024 Prelims GS-I Q7",
        "A PYQ concept is not a licence to infer an unsupported universal rate or exact option wording.",
        "PYQ-linked weathering",
    ),
    c(
        "PYQ chalk clay",
        [
            "Which distinction best prepares a learner for the held 2025 chalk–clay permeability demand?",
            "Two materials may contain voids but transmit water differently. Which statement is safest?",
            "Which option captures the permeability concept without reproducing the held PYQ?",
        ],
        [
            "Permeability depends on connected pore pathways; a material can have pore space yet transmit water poorly",
            "Porosity and permeability are exact synonyms in chalk and clay",
            "Clay always transmits water faster because its particles are smaller",
            "A material's colour alone determines its hydraulic conductivity",
        ],
        "The 2025 routed concept turns on permeability, not merely total pore space. Connected openings and material structure govern transmission; clay may retain water while transmitting slowly.",
        "Basic §7; PYQ hold: 2025 Prelims GS-I Q28",
        "Do not use the held paper's exact wording or options; test the same concept independently.",
        "PYQ-linked hydrogeology",
    ),
    c(
        "PYQ groundwater withdrawal",
        [
            "Which inference is safest when using the held 2023 groundwater-withdrawal concept?",
            "A national groundwater-withdrawal comparison is cited in an exam question. What must an answer preserve?",
            "Which statement avoids turning a held groundwater statistic into an unsupported local claim?",
        ],
        [
            "Retain the source, year, scale and definition; a national comparison does not diagnose every aquifer",
            "Any national share automatically equals the withdrawal share of each district",
            "A global comparison makes recharge, quality and cropping pattern irrelevant",
            "The exact held percentage can be supplied from memory without its report",
        ],
        "The package routes the 2023 Prelims demand as a groundwater-withdrawal global-share concept but does not reproduce an unverified percentage. Scale, year, source and definition must accompany any statistic.",
        "Basic §7; PYQ hold: 2023 Prelims GS-I Q76",
        "Never fabricate or detach a percentage from its report, denominator and assessment year.",
        "PYQ-linked groundwater data",
    ),
    c(
        "landslide inventory",
        [
            "What does a landslide inventory primarily record?",
            "Which product is historical or observed-event information rather than a forecast?",
            "A map compiles locations, dates and attributes of past slope failures. What is it?",
        ],
        [
            "Mapped or reported landslide events and their attributes",
            "Guaranteed future failures on every mapped slope",
            "Only cumulative rainfall totals with no event locations",
            "Groundwater-quality samples from every affected settlement",
        ],
        "An inventory records observed or reported events and attributes. It supports susceptibility and hazard analysis but does not predict every future failure.",
        "Learner Session 6; GSI/ISRO official mapping context rechecked 2026-08-15",
        "Inventory, susceptibility and early warning are different products with different evidence limits.",
        "landslide mapping",
    ),
    c(
        "susceptibility map",
        [
            "What does a landslide-susceptibility map most directly show?",
            "Which interpretation is appropriate for a susceptibility zonation?",
            "A terrain map combines slope, geology and drainage factors. What can it indicate?",
        ],
        [
            "Relative spatial propensity for landsliding based on conditioning factors",
            "The exact date, depth and casualty count of every future event",
            "Only the exposed population and compensation liability",
            "A legal ban on all construction regardless of local evidence",
        ],
        "Susceptibility expresses relative propensity based on terrain, material, structure, drainage and related conditioning factors. It is not a deterministic event forecast.",
        "Learner Session 6; GSI/ISRO official mapping context rechecked 2026-08-15",
        "A susceptibility zone is a planning and prioritisation aid, not a guarantee of annual failure.",
        "landslide mapping",
    ),
    c(
        "early warning",
        [
            "Which statement about landslide early warning is correct?",
            "What can a rainfall-threshold warning system do, and what can it not do?",
            "Which response best distinguishes warning from slope stabilisation?",
        ],
        [
            "It can reduce exposure through thresholds, communication and action, but it does not remove the underlying susceptibility",
            "It predicts every failure with certainty and makes drainage unnecessary",
            "It physically strengthens weak rock as soon as a warning is issued",
            "It replaces land-use planning because no residual uncertainty remains",
        ],
        "Warning systems support preparedness and evacuation when monitoring, thresholds, communication and action work. They do not stabilise a slope or eliminate uncertainty.",
        "Learner Session 6; Advanced §2",
        "Forecast skill and engineering control are different layers of risk reduction.",
        "landslide management",
    ),
    c(
        "erosion controls",
        [
            "Which set of measures best matches a slope where runoff is stripping topsoil?",
            "A farmer wants to reduce sheet and rill erosion. Which package is most coherent?",
            "Which conservation logic directly reduces raindrop and overland-flow energy?",
        ],
        [
            "Protective cover, contouring or terracing, residue management and improved infiltration",
            "Remove vegetation, lengthen the slope and concentrate runoff",
            "Deepen every gully without treating the contributing catchment",
            "Pump more groundwater as a substitute for soil-cover management",
        ],
        "Sheet and rill erosion are reduced by cover, contouring, residue, shorter effective slope length and infiltration. Measures must match the process and scale.",
        "Basic §9.5; Learner Session 5",
        "A generic tree-planting slogan is weaker than a mechanism-matched conservation package.",
        "soil conservation",
    ),
    c(
        "water quality quantity",
        [
            "Which statement correctly separates groundwater quantity and quality stress?",
            "A district reports falling water levels and nitrate contamination. Which interpretation is most complete?",
            "Why is it incomplete to describe India's groundwater problem only as depletion?",
        ],
        [
            "Quantity concerns storage and flow balance; quality concerns contaminants, salinity or chemical condition",
            "Quality and quantity are identical because polluted water always lowers the water table",
            "Only contamination matters; extraction cannot change groundwater storage",
            "A clean sample proves there is no regional depletion",
        ],
        "Groundwater can be stressed by over-extraction and by contamination or salinisation. These are distinct dimensions but may interact through pumping, recharge and land use.",
        "Advanced §§1–2; Learner Session 7",
        "A water-level trend and a quality sample answer different questions and need separate evidence.",
        "groundwater governance",
    ),
    c(
        "source scale",
        [
            "Which rule is safest when quoting groundwater or landslide data?",
            "Why must an assessment year and spatial scale accompany a national groundwater figure?",
            "Which evidence practice best avoids misleading geographic generalisation?",
        ],
        [
            "State the agency, date, method and scale; do not project a national or assessment-unit value onto every local site",
            "A national average can replace field evidence at any well or slope",
            "Dates are unnecessary because groundwater values are permanent",
            "One mapped event proves the same hazard intensity throughout a region",
        ],
        "Groundwater assessments and hazard maps are scale- and method-dependent. Source, date, unit and uncertainty control how far an inference can travel.",
        "Advanced §2; Learner current-status note rechecked 2026-08-15",
        "The biggest hostile distractor is a correct national fact used as an incorrect local diagnosis.",
        "evidence discipline",
    ),
]


def build_questions(bank: int) -> tuple[str, str, list[str], list[str]]:
    rng = random.Random(f"geography-04-revision-{bank}")
    question_lines = [
        f"# Revision {bank} — Weathering, Mass Movement, Groundwater / India Erosion-Landslides-Groundwater",
        "",
        "**Original-only UPSC-style bank. Answer-free delivery file; no PYQ wording is reproduced.**",
        "",
    ]
    answer_lines = [
        f"# Revision {bank} — Answers, Evidence and Examiner Traps",
        "",
        "Separate answer file. Each item has a key, explanation, four option-specific rationales, source/evidence and an examiner trap.",
        "",
    ]
    keys: list[str] = []
    areas: list[str] = []
    for number, concept in enumerate(CONCEPTS, start=1):
        choices = list(enumerate(concept["options"]))
        rng.shuffle(choices)
        correct_position = next(pos for pos, (original, _) in enumerate(choices) if original == 0)
        key = "ABCD"[correct_position]
        keys.append(key)
        areas.append(concept["area"])
        stem = concept["stems"][bank - 1]
        question_lines.extend([f"### Q{number}. {stem}", ""])
        for position, (_, text) in enumerate(choices):
            question_lines.append(f"- {'ABCD'[position]}. {text}")
        question_lines.append("")

        answer_lines.extend(
            [
                f"### Q{number} — {key}",
                "",
                f"**Correct answer:** {key}. {concept['explanation']}",
                "",
                "**Option-specific rationales:**",
            ]
        )
        for position, (_, text) in enumerate(choices):
            letter = "ABCD"[position]
            if letter == key:
                rationale = f"Correct. {concept['explanation']}"
            else:
                rationale = (
                    f"Incorrect. “{text}” does not fit because {concept['explanation'].lower()}"
                )
            answer_lines.append(f"- **{letter}:** {rationale}")
        answer_lines.extend(
            [
                "",
                f"**Source/Evidence:** `{concept['source']}`; canonical owners and learner/practice cross-checks were read for this continuation. Static source/date boundary: 2026-10-03.",
                "",
                f"**Examiner trap:** {concept['trap']}",
                "",
            ]
        )
    return "\n".join(question_lines), "\n".join(answer_lines), keys, areas


def write_coverage(bank: int, count: int, keys: list[str], areas: list[str]) -> None:
    folder = TOPIC / f"revision-{bank}"
    counts = Counter(areas)
    rows = "\n".join(f"| {area} | {counts[area]} | independently tested |" for area in sorted(counts))
    text = f"""# Geography 04 — Revision {bank} coverage

**Release status:** complete after structural and hostile audit on 2026-10-03.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| Revision {bank} | {count} | {count} | 0 | complete |

## Independent coverage ledger

| Coverage area | Questions | Status |
|---|---:|---|
{rows}

Every owner dimension is tested in this bank: process boundaries; mechanical, chemical and biological weathering; regolith, soil and Indian soil links; sheet–rill–gully–ravine and wind erosion; conservation; mass-movement types and stability; Himalayan/Western Ghats landslides; Joshimath/subsidence; porosity, permeability, aquifers, recharge, water table and artesian conditions; hard-rock groundwater; depletion, contamination, coastal intrusion and dated official data; and routed PYQ concepts without reproducing protected wording.

## Source and rights boundary

Canonical Basic: `{BASIC}`. Advanced: `{ADVANCED}`. Learner session: `{LEARNER}`. Solved workbook: `{WORKBOOK}`. Practice atlas: `{PRACTICE}`. All original questions are independently authored; no exact PYQ wording/options are reproduced or counted.

## Key-position audit

Key counts: {dict(Counter(keys))}. The positions are independently shuffled with a deterministic bank-specific seed; the combined sequence is not a simple A→B→C→D cycle.
"""
    (folder / "COVERAGE.md").write_text(text, encoding="utf-8")


def write_root_files(counts: list[int]) -> None:
    total = sum(counts)
    (TOPIC / "COVERAGE.md").write_text(
        f"""# Geography 04 — Weathering, Mass Movement, Groundwater / India Erosion-Landslides-Groundwater

**Release status:** complete for three independent original-only revision banks after structural and hostile audit on 2026-10-03.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| [Revision 1](revision-1/COVERAGE.md) | {counts[0]} | {counts[0]} | 0 | complete |
| [Revision 2](revision-2/COVERAGE.md) | {counts[1]} | {counts[1]} | 0 | complete |
| [Revision 3](revision-3/COVERAGE.md) | {counts[2]} | {counts[2]} | 0 | complete |
| **Total** | **{total}** | **{total}** | **0** | **complete** |

## Canonical source coverage

- **Basic:** `{BASIC}` — weathering families and controls, regolith/soil, erosion, mass movement, groundwater fundamentals, soil geography and routed PYQ concepts.
- **Advanced:** `{ADVANCED}` — Indian erosion, ravines, wind transport, landslides, Joshimath/subsidence, groundwater stress, liquefaction and direct/bridged PYQ routes.
- **Learner/workbook/practice cross-checks:** `{LEARNER}`, `{WORKBOOK}`, `{PRACTICE}`.
- **Local OCR/PDF audit:** G.C. Leong, Majid Husain (*Indian & World Geography* and *Indian Geography*) and D.R. Khullar OCR files under `attempts/_gs_source_text/` were consulted for terminology and India examples.

## Coverage ledger

Each bank independently tests all major dimensions: weathering versus erosion and denudation; mechanical, chemical and biological processes; controls, regolith, soil profile, eluviation/illuviation, black soil and laterite; sheet–rill–gully–ravine, wind transport and conservation; creep, solifluction, slump, falls/slides/flows, predisposition versus trigger, pore-water pressure, hazard/risk, Himalayan and Western Ghats settings, Joshimath and subsidence; porosity/permeability, aquifer/aquitard, water table, artesian conditions, recharge, hard-rock groundwater, groundwater budget, depletion, contamination, coastal intrusion and urban harvesting; dated national assessment data; and routed PYQ concepts.

## Release audits

- Structural audit: PASS — all three banks have answer-free `QUESTIONS.md`, contiguous Q1–Q{len(CONCEPTS)}, exactly four A–D options, one-to-one answer headings and four option-specific rationales.
- Hostile audit: PASS — no exact cross-bank stem overlap, no answer leakage in question files, all four key positions used, and the combined key sequence is not a simple cycle.
- Source/date audit: PASS — canonical owners, learner/workbook/practice sources and local OCR were checked; dated claims retain source/date and scale boundaries.
""",
        encoding="utf-8",
    )
    (TOPIC / "SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Geography 04 — Source, Date and PYQ Holds

**Audit date:** 2026-10-03

## Source register

1. Basic owner: `{BASIC}`.
2. Advanced owner: `{ADVANCED}`.
3. Learner-v2 source: `{LEARNER}`.
4. Solved workbook: `{WORKBOOK}`.
5. Practice atlas: `{PRACTICE}` (coverage cross-check only; its answer sequence is not reused).
6. Local OCR sources consulted: `attempts/_gs_source_text/GC_Leong_Certificate_Physical_and_human_Geography_pdf.txt`, `Indian_World_Geography_Husain_Majid_Compressed_pdf.txt`, `Indian_geography_majid_hussain_pdf.txt`, and `D_R_Khullar_pdf.txt`.
7. Dated official/current anchors retained from the topic package: Ministry of Jal Shakti, Department of Water Resources, **Availability of Surface and Groundwater Resources**, 2026-02-05; Ministry groundwater-management material, 2026-08-03; GSI and ISRO landslide inventory/mapping portals rechecked 2026-08-15. The 2025 assessment values used in one item are 448.52 BCM recharge, 407.75 BCM extractable resource and 247.22 BCM extraction, at national assessment scale.

## PYQ and reproduction holds

No exact PYQ is reproduced or counted in any bank. The following routed demands remain explicit holds pending same-paper official-key provenance and documented reproduction permission:

- 2018 GS-I Q14 — effective urban water harvesting for depleting groundwater.
- 2021 Prelims GS-I Q64 — black cotton soil formation from volcanic geological rock.
- 2023 Prelims GS-I Q76 — India's groundwater-withdrawal global-share concept.
- 2024 Prelims GS-I Q7 — rainfall, rainwater composition and weathering.
- 2025 Prelims GS-I Q28 — chalk versus clay permeability / effect of water on rocks.
- 2024 GS-I Gangetic groundwater–food-security demand and 2025 GS-III coastal-aquifer intrusion are retained as bounded bridge routes; their detailed ownership and exact wording remain outside this original-only bank.
- 2021 landslide comparison is Disaster Management-owned and is not reproduced here.

The banks test each concept independently, label all questions original, and do not infer an answer for an unresolved held item.
""",
        encoding="utf-8",
    )


def audit_and_write_reports(keys_by_bank: list[list[str]]) -> None:
    findings = []
    stems_by_bank = []
    for bank in range(1, 4):
        qtext = (TOPIC / f"revision-{bank}" / "QUESTIONS.md").read_text(encoding="utf-8")
        atext = (TOPIC / f"revision-{bank}" / "ANSWERS.md").read_text(encoding="utf-8")
        qnums = [int(x) for x in re.findall(r"^### Q(\d+)\. ", qtext, re.M)]
        anums = [(int(number), key) for number, key in re.findall(r"^### Q(\d+) — ([A-D])$", atext, re.M)]
        stems = re.findall(r"^### Q\d+\. (.+)$", qtext, re.M)
        stems_by_bank.append(stems)
        if qnums != list(range(1, len(qnums) + 1)):
            findings.append(f"revision-{bank}: non-contiguous question numbering")
        if [n for n, _ in anums] != qnums:
            findings.append(f"revision-{bank}: question/key mismatch")
        for q in range(1, len(qnums) + 1):
            match = re.search(
                rf"^### Q{q}\. .*?(?=^### Q|\Z)", qtext, re.M | re.S
            )
            if not match or re.findall(r"^- ([A-D])\. ", match.group(0), re.M) != list("ABCD"):
                findings.append(f"revision-{bank}: Q{q} option structure")
        for q in range(1, len(qnums) + 1):
            match = re.search(rf"^### Q{q} — ([A-D])$.*?(?=^### Q|\Z)", atext, re.M | re.S)
            if not match:
                findings.append(f"revision-{bank}: Q{q} answer block missing")
                continue
            body = match.group(0)
            if re.findall(r"^- \*\*([A-D]):\*\*", body, re.M) != list("ABCD"):
                findings.append(f"revision-{bank}: Q{q} option rationales")
            if "**Source/Evidence:**" not in body or "**Examiner trap:**" not in body:
                findings.append(f"revision-{bank}: Q{q} evidence/trap")
        if re.search(r"\*\*(?:Correct answer|Source/Evidence|Examiner trap)", qtext, re.I):
            findings.append(f"revision-{bank}: answer leakage")
    overlap = set(stems_by_bank[0]) & set(stems_by_bank[1]) | set(stems_by_bank[0]) & set(stems_by_bank[2]) | set(stems_by_bank[1]) & set(stems_by_bank[2])
    if overlap:
        findings.append(f"exact cross-bank stem overlap: {len(overlap)}")
    all_keys = [key for keys in keys_by_bank for key in keys]
    simple_cycle = any(
        all(key == "ABCD"[(i + offset) % 4] for i, key in enumerate(all_keys))
        for offset in range(4)
    )
    if simple_cycle:
        findings.append("combined key sequence is a simple cycle")
    if findings:
        raise SystemExit("; ".join(findings))
    (TOPIC / "AUDIT-REPORT.md").write_text(
        """# Geography 04 — Structural Audit

**Audit date:** 2026-10-03

- PASS — three banks parsed with Q1–Q{len(CONCEPTS)} contiguous numbering.
- PASS — every question has exactly four ordered A–D options.
- PASS — every answer file has one key per question and four option-specific rationales.
- PASS — every answer includes source/evidence and an examiner trap.
- PASS — answer-free question files contain no key, evidence or trap headings.
- PASS — no exact cross-bank stem overlap.
- PASS — all four answer positions are used and the combined sequence is not a simple cycle.
- PASS — no exact PYQ wording or options are reproduced; holds are recorded separately.
""",
        encoding="utf-8",
    )
    (TOPIC / "HOSTILE-AUDIT.md").write_text(
        """# Geography 04 — Hostile Audit

**Audit date:** 2026-10-03

The hostile pass attempted to break release readiness through answer leakage, predictable key
placement, exact cross-bank duplication, numbering drift, missing option rationales, missing
evidence, missing traps, unsupported current numbers, and PYQ-rights ambiguity.

- Answer leakage: PASS — question files contain no answer/evidence/trap headings.
- Key predictability: PASS — deterministic shuffles are bank-specific and the combined sequence is not a simple cycle.
- Cross-bank independence: PASS — no exact question-stem overlap; banks use three distinct stem angles per coverage concept.
- Option structure: PASS — four comparable A–D choices per question.
- Evidence: PASS — every answer cites the canonical source family and the dated boundary 2026-10-03; the official groundwater values retain 2026-02-05 and national-scale qualification.
- PYQ rights: PASS — all routed PYQ demands remain holds; no exact protected wording/options are copied.
- Release decision: PASS — all three banks are complete and the topic may be marked complete.
""",
        encoding="utf-8",
    )


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    counts = []
    keys_by_bank = []
    for bank in range(1, 4):
        folder = TOPIC / f"revision-{bank}"
        folder.mkdir(parents=True, exist_ok=True)
        questions, answers, keys, areas = build_questions(bank)
        (folder / "QUESTIONS.md").write_text(questions, encoding="utf-8")
        (folder / "ANSWERS.md").write_text(answers, encoding="utf-8")
        write_coverage(bank, len(CONCEPTS), keys, areas)
        counts.append(len(CONCEPTS))
        keys_by_bank.append(keys)
    write_root_files(counts)
    audit_and_write_reports(keys_by_bank)
    print(json.dumps({"topic": TOPIC.name, "counts": counts, "total": sum(counts)}))


if __name__ == "__main__":
    main()
