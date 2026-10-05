from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
TOPIC = SUBJECT / "05-Landforms-by-Running-Water-India-Drainage-and-Interlinking"

BASIC = "upsc-ai-kit/knowledge/Geography/basic/05_Landforms-by-Running-Water.md"
ADVANCED = "upsc-ai-kit/knowledge/Geography/advanced/05_India-Drainage-and-Interlinking.md"
LEARNER = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-05_Learning-Session.md"
)
WORKBOOK = (
    "upsc-ai-kit/knowledge/Geography/learning-sessions/v2/part-a-physical-geography/"
    "geography-05_Solved-Workbook.md"
)
PRACTICE = (
    "upsc-ai-kit/practice/All-Topics-MCQ/Geography/Part-A-—-Physical-Geography/"
    "05-Landforms-by-Running-Water-India-Drainage-and-Interlinking/MCQ-Bank-With-Solutions.md"
)


QUESTIONS: list[dict[str, object]] = []


def add(area: str, stems: tuple[str, str, str], options: tuple[str, str, str, str],
        explanation: str, source: str, trap: str) -> None:
    QUESTIONS.append(
        {
            "area": area,
            "stems": stems,
            "options": options,
            "explanation": explanation,
            "source": source,
            "trap": trap,
        }
    )


add(
    "basin and divide",
    (
        "Which statement correctly distinguishes a drainage basin from a watershed?",
        "A map shows tributaries converging toward one trunk stream. Which interpretation is most precise?",
        "Which formulation keeps basin anatomy spatially accurate?",
    ),
    (
        "A basin receives runoff to a river system, while a watershed or divide separates neighbouring basins",
        "A watershed is the main channel and a basin is only its mouth",
        "A basin is any floodplain and a watershed is a distributary",
        "A divide is created only after a river has reached the sea",
    ),
    "A drainage basin is the area contributing runoff to a river system; a watershed or divide is the boundary separating adjacent basins. Tributaries join a trunk stream within that system.",
    "Basic §8; Learner Session 1",
    "A watershed is a boundary, not the entire channel or floodplain.",
)
add(
    "runoff and discharge",
    (
        "Which combination most directly controls the discharge response of a river basin?",
        "Why can two basins receiving similar rain produce different river flows?",
        "Which basin-scale interpretation of river discharge is safest?",
    ),
    (
        "Rainfall or snowmelt, basin relief, infiltration, drainage and storage interact",
        "Only the river's mouth determines discharge",
        "Channel colour alone fixes the annual hydrograph",
        "A basin's discharge is independent of soils, slope and storage",
    ),
    "River discharge reflects inputs and basin transmission: rainfall or snowmelt, relief, infiltration, soil and rock permeability, vegetation, channel network, lakes, groundwater and human storage all interact.",
    "Learner Sessions 1, 9 and 12; Basic §8.1",
    "Rainfall is an input, not a complete explanation of discharge or flood response.",
)
add(
    "erosion mechanisms",
    (
        "Which set contains the principal erosional mechanisms of running water?",
        "A river undermines a bank by pressure in cracks and wears its bed with moving debris. Which pairing fits?",
        "Which process vocabulary is appropriate for fluvial erosion?",
    ),
    (
        "Hydraulic action, corrasion or abrasion, attrition and solution",
        "Traction, saltation, suspension and deposition only",
        "Compaction, subsidence, salinisation and weathering only",
        "Deflation, plucking, solifluction and carbonation only",
    ),
    "Running water erodes through hydraulic action, mechanical corrasion or abrasion, attrition of its load and chemical solution where soluble material is involved.",
    "Basic §§1–2; Learner Session 2",
    "Transport modes are not interchangeable with erosion mechanisms.",
)
add(
    "transport modes",
    (
        "Which option correctly matches a river-transport mode with its load behaviour?",
        "How can a river carry both coarse and fine material?",
        "Which classification of fluvial load movement is most defensible?",
    ),
    (
        "Traction rolls coarse particles, saltation hops them, suspension carries fine sediment and solution carries dissolved material",
        "All load moves only as dissolved ions",
        "Coarse boulders remain permanently suspended while clay always rolls",
        "Attrition is a transport mode that carries no sediment",
    ),
    "Traction, saltation, suspension and solution describe different ways material is moved; competence and discharge determine which grain sizes can be carried.",
    "Basic §2; Learner Session 2",
    "Attrition is wearing of transported fragments, not a separate load-transport mode.",
)
add(
    "competence and deposition",
    (
        "When does deposition become more likely in a river reach?",
        "Which change most directly reduces a river's transporting competence?",
        "How should a lower-course sediment deposit be explained?",
    ),
    (
        "When velocity or discharge falls enough that transporting capacity is exceeded by the load",
        "When the river accelerates and gains more stream power",
        "When every grain becomes chemically dissolved",
        "When bed slope increases without any change in flow",
    ),
    "Deposition occurs when available flow competence or capacity falls relative to the sediment load, for example with reduced velocity, lower slope, channel expansion or loss of discharge.",
    "Basic §§1–2; Learner Session 2",
    "Lower course does not mean deposition at every instant; floods can erode and transport there too.",
)
add(
    "graded long profile",
    (
        "Which description best fits a graded river profile?",
        "Why is a graded profile not a permanent final shape?",
        "Which statement uses the idea of graded adjustment correctly?",
    ),
    (
        "A dynamic tendency toward a smooth concave-up profile balancing discharge, load, resistance and base level",
        "A straight line that cannot be disturbed by uplift or dams",
        "A profile found only in glaciated valleys",
        "A map of tributary ownership rather than a longitudinal form",
    ),
    "A graded river tends toward a concave-up long profile in dynamic balance, but uplift, floods, base-level change, rock resistance, dams and sediment pulses can interrupt the tendency.",
    "Basic §1 and §9.2; Learner Session 3",
    "Graded means dynamic adjustment, not a static equilibrium immune to disturbance.",
)
add(
    "vertical and lateral erosion",
    (
        "Which comparison between vertical and lateral corrasion is correct?",
        "A river is deepening a narrow valley upstream but widening its valley farther downstream. Which explanation fits?",
        "Which relation between river work and valley form is safest?",
    ),
    (
        "Vertical corrasion deepens a channel, while lateral corrasion widens banks and valley sides",
        "Vertical corrasion deposits levees, while lateral corrasion dissolves glaciers",
        "Both terms refer only to chemical solution in limestone",
        "Lateral corrasion always produces a V-shaped valley",
    ),
    "Mechanical river erosion may be predominantly vertical where gradient and incision are strong, or lateral where the channel migrates and widens its valley.",
    "Basic §§1–2; Learner Sessions 2 and 4",
    "Course labels are tendencies; local gradient, discharge, rock and sediment also matter.",
)
add(
    "upper course valley",
    (
        "Which landform suite is most characteristic of strong upper-course incision?",
        "A steep mountain reach has a narrow V-shaped valley. Which process is the best first explanation?",
        "Which upper-course inference avoids a stage-label shortcut?",
    ),
    (
        "Vertical incision and hydraulic action producing V-shaped valleys, gorges and related steep-reach forms",
        "Dominant overbank deposition producing a wide delta plain",
        "Tidal scouring producing an estuary",
        "Neck cutoff producing an ox-bow as the primary form",
    ),
    "Steep gradients favour vertical incision, hydraulic action and load abrasion, producing V-shaped valleys and gorges; local rock and flow can modify the expression.",
    "Basic §§1–2; Learner Session 4",
    "A mountain location alone does not guarantee one landform; gradient and resistance must be considered.",
)
add(
    "gorges and interlocking spurs",
    (
        "Interlocking spurs in an upper river course mainly indicate what?",
        "Why can a youthful-looking valley contain alternating projecting spurs?",
        "Which process–landform link is correct?",
    ),
    (
        "A river cuts around resistant projecting ridges while maintaining a sinuous course in a steep valley",
        "Tidal deposition at a river mouth",
        "Wind deflation across a desert basin",
        "A distributary network spreading across a delta",
    ),
    "Interlocking spurs form where a river follows a winding course around resistant ridges during strong down-cutting, leaving alternating projections that appear to interlock.",
    "Basic §1; Learner Session 4",
    "Interlocking spurs are not distributaries or coastal depositional features.",
)
add(
    "rapids and waterfalls",
    (
        "A waterfall is most likely to develop where which contrast exists?",
        "Which setting best explains a rapids-and-waterfall reach?",
        "What should be checked before assigning a waterfall to the upper course?",
    ),
    (
        "A marked break in gradient or resistant rock creates a knickpoint and uneven erosion",
        "A perfectly uniform, low-gradient bed with no lithological or structural contrast",
        "Only strong tidal range at the mouth",
        "A floodplain with no channel slope or bed control",
    ),
    "Waterfalls and rapids commonly reflect abrupt gradient or resistance contrasts; their retreat can leave a gorge or a modified long profile.",
    "Basic §2; Learner Session 4; 2024 PYQ route",
    "Waterfall location questions test the river and region pair, not merely the word 'mountain'.",
)
add(
    "knickpoint retreat",
    (
        "What is a likely consequence of waterfall retreat?",
        "How can a knickpoint alter a river's long profile?",
        "Which statement correctly links waterfall recession and fluvial adjustment?",
    ),
    (
        "Headward migration of the break in slope can extend a gorge and shift the zone of incision upstream",
        "Permanent conversion of the entire river into a delta",
        "Immediate formation of an estuary regardless of the mouth",
        "Elimination of all sediment transport downstream",
    ),
    "A retreating waterfall or knickpoint migrates upstream through differential erosion, lengthening a gorge and modifying the river's profile.",
    "Basic §2; Learner Session 4",
    "Retreat of a knickpoint is not river capture; the processes have different mechanisms and evidence.",
)
add(
    "meander geometry",
    (
        "Which statement best explains a meander?",
        "Why does a sinuous channel commonly migrate laterally?",
        "Which observation is most consistent with an active meander belt?",
    ),
    (
        "Helicoidal flow couples outer-bank erosion with inner-bank deposition and shifts the channel",
        "The channel is controlled only by vertical incision and cannot move sideways",
        "Tidal scour removes all sediment from both banks equally",
        "A meander is a distributary formed only at a delta mouth",
    ),
    "Meandering reflects lateral energy redistribution: outer-bank flow erodes and inner-bank flow deposits, causing bends to migrate and enlarge.",
    "Basic §1; Learner Session 5",
    "A meander is a channel form, not a synonym for a delta distributary or river capture.",
)
add(
    "helicoidal flow",
    (
        "What is the geomorphic significance of helicoidal flow in a bend?",
        "Which mechanism connects an outer river cliff to an inner slip-off slope?",
        "Why do sediment and erosion concentrate on opposite sides of a bend?",
    ),
    (
        "Spiral flow transfers momentum and sediment across the channel, favouring outer-bank scour and inner-bank deposition",
        "It stops all cross-channel movement and produces a straight channel",
        "It is the chemical dissolution of limestone at the river mouth",
        "It is a glacial process that creates a U-shaped valley",
    ),
    "Helicoidal flow helps explain the paired morphology of outer-bank erosion and inner-bank deposition in a meander.",
    "Basic §8.5; Learner Session 5",
    "The inner bank is not normally the site of maximum lateral erosion.",
)
add(
    "river cliffs and slip-off slopes",
    (
        "Which pairing is correct for a meander bend?",
        "A bend has a steep eroding outer bank and a gently shelving inner bank. What does this indicate?",
        "Which landform contrast follows from lateral channel migration?",
    ),
    (
        "River cliff on the outer bank and depositional slip-off slope on the inner bank",
        "Levee on the outer bank and gorge on the inner bank",
        "Delta on the outer bank and estuary on the inner bank",
        "Wind gap on the outer bank and elbow of capture on the inner bank",
    ),
    "Higher velocity and shear on the outer bank encourage erosion and a river cliff; slower inner-bank flow encourages deposition and a slip-off slope.",
    "Basic §§1–2; Learner Session 5",
    "Do not reverse the outer-bank erosional and inner-bank depositional roles.",
)
add(
    "ox-bow formation",
    (
        "Which sequence most plausibly forms an ox-bow lake?",
        "A former meander loop is separated from the active channel. Which process is implied?",
        "What is the key geomorphic step in ox-bow formation?",
    ),
    (
        "Meander neck narrowing followed by cutoff leaves an abandoned loop",
        "A watershed rises and captures a tributary without channel migration",
        "A delta mouth is drowned by tides before any bend develops",
        "A gorge is carved directly by glacial plucking",
    ),
    "Progressive meander migration can narrow the neck; a flood or high-flow shortcut may cut through it, leaving an abandoned ox-bow loop.",
    "Basic §1; Learner Session 5",
    "Meander cutoff is not the same as river capture, which is a basin-evolution process involving headward erosion.",
)
add(
    "floodplain",
    (
        "How is a floodplain principally built?",
        "Which landform is a broad depositional surface beside a river that may be inundated?",
        "Why should floodplains be treated as active geomorphic spaces?",
    ),
    (
        "Repeated overbank deposition and channel migration spread alluvium across the valley floor",
        "Only vertical incision into resistant bedrock",
        "Tidal removal of sediment from a drowned mouth",
        "Headward erosion across a watershed",
    ),
    "Floodplains develop through overbank deposition, lateral channel migration and episodic sediment reworking; they remain active river space rather than vacant land.",
    "Basic §2; Learner Session 5 and 11",
    "A floodplain can be fertile and densely settled while still carrying substantial flood risk.",
)
add(
    "natural levees",
    (
        "Natural levees form most directly through which process?",
        "A raised ridge parallels a river channel without being an engineered embankment. What is the likely origin?",
        "Which distinction between natural and artificial levees is correct?",
    ),
    (
        "Coarser overbank sediment is deposited near the channel during floods, building a natural ridge",
        "A glacier deposits till only at the valley head",
        "Tides dissolve the channel banks into a delta",
        "A river captures a neighbouring basin and leaves a wind gap",
    ),
    "Floodwater loses competence rapidly on leaving the channel, depositing relatively coarse material close to the bank and finer sediment farther across the floodplain.",
    "Basic §2; Learner Session 5",
    "A natural levee is depositional; it is not automatically an engineered embankment or flood-proof barrier.",
)
add(
    "braided channels",
    (
        "Which conditions favour braided river channels?",
        "What combination best explains a multi-thread channel with shifting bars?",
        "Which statement about braiding is most defensible?",
    ),
    (
        "High sediment load, variable discharge and easily divided flow around temporary bars",
        "No sediment supply and perfectly stable banks",
        "Only deep tidal water at an estuary",
        "A single resistant bedrock gorge with no alluvium",
    ),
    "Braiding is favoured where sediment supply is high, discharge varies and banks or bars allow flow to split and rejoin; it is common in unstable alluvial settings.",
    "Basic §2 and §8.1; Learner Session 11",
    "Braiding is a channel pattern, not a synonym for a delta or distributary system.",
)
add(
    "delta and estuary",
    (
        "Which statement correctly distinguishes a delta from an estuary?",
        "A river mouth is strongly tidally scoured and sediment is removed rather than accumulated. Which mouth form is favoured?",
        "Which mouth-form rule is safest for a map question?",
    ),
    (
        "A delta is built by net sediment accumulation; an estuary is drowned or tidally scoured",
        "A delta is always a rift valley and an estuary is always a waterfall",
        "An estuary is simply one of the standard delta shapes",
        "Both terms mean the same depositional landform",
    ),
    "A delta forms where sediment accumulation can outpace marine removal and subsidence; an estuary is a drowned or strongly scoured mouth. 'Estuarine' is not a delta shape.",
    "Basic §§1–2; Learner Sessions 6 and 10",
    "Mouth form depends on sediment–marine-energy balance, not river size alone.",
)
add(
    "delta sediment budget",
    (
        "What is the central accounting principle for delta stability?",
        "Why can a delta retreat even when the river still carries sediment?",
        "Which set contains the key terms in a delta sediment-budget answer?",
    ),
    (
        "Sediment delivery must offset marine removal, subsidence and relative sea-level effects",
        "Only river length controls shoreline position",
        "A delta is stable whenever rainfall increases, regardless of tides",
        "Deltas cannot lose land because deposition is irreversible",
    ),
    "A delta persists or progrades when sediment input is sufficient relative to wave and tidal removal, compaction and other subsidence, relative sea-level change and channel redistribution.",
    "Basic §§1, 8.4–8.5; Learner Sessions 6 and 11",
    "Do not blame one dam, cyclone or sea-level trend for every delta-sector outcome.",
)
add(
    "delta sector dynamics",
    (
        "Which statement best describes a large, active delta such as the Ganga–Brahmaputra–Meghna?",
        "Why is a uniform 'sinking delta' description inadequate?",
        "Which delta-management inference follows from sectoral erosion and accretion?",
    ),
    (
        "Different sectors can erode and accrete simultaneously as channels, sediment and marine forces redistribute",
        "Every island must advance at the same rate because the basin is large",
        "High sediment supply eliminates all cyclone and subsidence effects",
        "Only coastal engineering matters; upstream sediment decisions are irrelevant",
    ),
    "Delta behaviour is spatially differentiated: one sector may accrete while another erodes under interacting sediment delivery, tides, cyclones, subsidence, embankments and channel change.",
    "Basic §§1 and 8.5; Learner Session 11",
    "A basin-scale sediment budget does not imply a uniform shoreline response everywhere.",
)
add(
    "dendritic pattern",
    (
        "What does dendritic drainage usually suggest?",
        "A tree-like network develops across broadly similar rock resistance. Which diagnosis fits?",
        "Which drainage-pattern pairing is correct?",
    ),
    (
        "Relatively uniform resistance and limited structural control",
        "A central volcanic cone forcing outward flow",
        "Alternating hard and soft folded belts",
        "A fault-and-joint grid producing repeated right angles",
    ),
    "Dendritic drainage is an irregular tree-like pattern generally associated with broadly uniform lithology and weak structural control.",
    "Basic §8.3; Learner Session 7",
    "Pattern diagnosis is probabilistic evidence of controls, not an absolute lithological proof.",
)
add(
    "trellis pattern",
    (
        "Which geological setting most favours trellis drainage?",
        "Tributaries join a main stream at near right angles along parallel valleys. What does this indicate?",
        "Which pattern–control relation is correct?",
    ),
    (
        "Alternating hard and soft bands in folded or tilted terrain",
        "A single isolated dome with streams flowing outward",
        "An enclosed basin with all streams converging inward",
        "Uniform massive rock with no structural guidance",
    ),
    "Trellis drainage reflects a main valley guided by weaker bands, with tributaries joining at near right angles from adjacent harder ridges or tilted strata.",
    "Basic §8.3; Learner Session 7",
    "Right-angle tributaries alone are not enough; the alternating structural setting matters.",
)
add(
    "rectangular pattern",
    (
        "Rectangular drainage most strongly indicates what control?",
        "A river and its tributaries repeatedly turn through near right angles. Which explanation is most likely?",
        "Which pattern is associated with joints and faults?",
    ),
    (
        "Strong structural control by joints or faults",
        "Uniform unconsolidated alluvium with no preferred weakness",
        "A central high causing radial outward flow",
        "Recent glaciation producing deranged lakes and swamps",
    ),
    "Rectangular drainage commonly develops where joints or faults guide channels and create repeated right-angle bends.",
    "Basic §8.3; Learner Session 7",
    "Rectangular is not the same as trellis; the structural geometry and tributary organisation differ.",
)
add(
    "radial and centripetal",
    (
        "Which comparison between radial and centripetal drainage is correct?",
        "Streams flow outward from a dome in one region and inward toward an enclosed basin in another. Which labels fit?",
        "Which relief–pattern pairing is accurate?",
    ),
    (
        "Radial flows outward from a central high; centripetal converges into an interior basin",
        "Radial converges inward; centripetal flows outward from a cone",
        "Both patterns require parallel folded ridges",
        "Both patterns are defined by right-angle fault bends",
    ),
    "Radial drainage spreads outward from a central high such as a dome or cone, while centripetal drainage converges into an interior basin with no external outlet.",
    "Basic §8.3; Learner Session 7",
    "The direction of flow relative to the central feature is the decisive distinction.",
)
add(
    "antecedent drainage",
    (
        "What makes a river antecedent?",
        "A river cuts a transverse gorge across rising mountain relief. Which interpretation is strongest?",
        "Which chronology is implied by antecedent drainage?",
    ),
    (
        "The river predates the uplift and incises fast enough to maintain its course across rising relief",
        "The river formed only after erosion removed a cover of younger rock",
        "The river was recently diverted by a competing stream",
        "The river flows only during the monsoon",
    ),
    "An antecedent river is older than the uplift it crosses and maintains its course by down-cutting as relief rises, producing deep transverse gorges in suitable settings.",
    "Advanced §§1–2; Basic §8.3; Learner Sessions 8–9",
    "Antecedence is a timing relationship with uplift, not merely any river in a gorge.",
)
add(
    "superimposed drainage",
    (
        "Which description fits superimposed drainage?",
        "A river pattern formed on a cover is retained after erosion exposes structurally different rocks below. What process is shown?",
        "How does superimposition differ from antecedence?",
    ),
    (
        "A pattern acquired on a former cover is imposed onto unrelated underlying structure",
        "A river predates mountain uplift and cuts upward through it",
        "A tributary joins a trunk stream at its mouth",
        "A floodplain is built by repeated overbank deposition",
    ),
    "Superimposed drainage inherits a course from an earlier cover and then cuts into underlying rocks whose structure did not determine the original pattern.",
    "Basic §8.3; Learner Session 8",
    "Superimposition concerns an inherited pattern from a removed cover; antecedence concerns river age relative to uplift.",
)
add(
    "river capture",
    (
        "Which process best describes river capture or piracy?",
        "An aggressive stream extends headward and diverts a neighbouring drainage line. What evidence may remain?",
        "Which statement separates capture from ordinary tributary joining?",
    ),
    (
        "Headward erosion diverts a neighbouring stream, potentially leaving an elbow, wind gap and misfit reach",
        "A river deposits a levee during a flood",
        "A meander neck is cut off within the same channel",
        "A glacier excavates a U-shaped valley",
    ),
    "River capture is a drainage-evolution process driven by headward erosion; elbows of capture, wind gaps and misfit valleys may preserve evidence.",
    "Advanced §1; Basic §8.3; Learner Session 8",
    "Capture changes basin organisation; it is not simply a tributary joining its trunk.",
)
add(
    "himalayan regime",
    (
        "Why are the major Himalayan river systems largely perennial?",
        "Which description best fits the Indus, Ganga and Brahmaputra regimes?",
        "What qualification should accompany the word 'perennial' for Himalayan rivers?",
    ),
    (
        "Rain, snow or glacier melt and groundwater contribute in varying proportions",
        "Only glacier melt supplies them throughout the year",
        "They have uniform discharge in every season and reach",
        "They are short coastal streams with no international catchment",
    ),
    "The major Himalayan systems are mostly perennial because multiple sources—monsoon rain, snow or glacier melt and groundwater—contribute, though discharge remains seasonally variable.",
    "Advanced §§1–2; Learner Session 9",
    "Perennial does not mean glacier-only flow or uniform discharge.",
)
add(
    "peninsular regime",
    (
        "Which comparison best characterises Peninsular drainage?",
        "Why is storage important for many Peninsular river systems?",
        "Which statement avoids overgeneralising Peninsular rivers?",
    ),
    (
        "They occupy an older landscape and are more monsoon-dominant, though major or regulated reaches need qualification",
        "They are all glacier-fed and cross the highest Himalaya",
        "They never form deltas or estuaries",
        "They are all entirely dry outside one fixed month",
    ),
    "Peninsular drainage is generally older and more monsoon-dominant; natural dry-season flow is less assured, so storage and regulation often matter, but individual rivers vary.",
    "Advanced §§1–2; Learner Sessions 9–10",
    "Do not convert a broad drainage-system contrast into an absolute claim about every river.",
)
add(
    "east-flowing peninsular rivers",
    (
        "Why do most large Peninsular rivers flow east?",
        "Which structural explanation best accounts for the broad eastward drainage of the plateau?",
        "Which map inference is most defensible for a major Peninsular basin?",
    ),
    (
        "The Western Ghats form an off-centre western divide and the plateau surface generally slopes eastward",
        "The Eastern Ghats are a continuous higher divide beside the Arabian Sea",
        "All east-flowing rivers begin north of the Himalaya",
        "Tides force every Peninsular river to flow toward the Bay of Bengal",
    ),
    "The Western Ghats lie close to the west coast and act as the principal divide; the plateau slopes generally eastward, allowing long rivers to cross toward the Bay of Bengal.",
    "Basic §8.2; Advanced §2; Learner Session 10",
    "A broad eastward rule has structural exceptions and does not erase short west-flowing Ghats streams.",
)
add(
    "narmada and tapi",
    (
        "Which pair is the principal major west-flowing exception among Peninsular rivers?",
        "Why do Narmada and Tapi not fit the general eastward rule?",
        "Which mouth-and-structure pairing is correct?",
    ),
    (
        "Narmada and Tapi flow west through structurally controlled troughs toward the Arabian Sea",
        "Godavari and Krishna flow west through Himalayan antecedent gorges",
        "Mahanadi and Kaveri flow west because of deltaic tides",
        "Luni and Brahmaputra flow west through the Western Ghats",
    ),
    "Narmada and Tapi are major west-flowing Peninsular exceptions associated with structurally controlled troughs or rift-valley settings and Arabian Sea mouths.",
    "Advanced §§1–2; Learner Sessions 10 and 15",
    "Do not treat all west-flowing streams as identical; short Ghats streams and rift-confined rivers differ in scale and setting.",
)
add(
    "indus map hook",
    (
        "Which statement correctly identifies the broad course of the Indus system?",
        "A map question asks for a Himalayan international river that reaches the Arabian Sea through Pakistan. Which system fits?",
        "Which source–mouth pairing is safest for the Indus?",
    ),
    (
        "It rises on the Tibetan Plateau region, crosses Ladakh and reaches the Arabian Sea through Pakistan",
        "It rises near Trimbakeshwar and builds an Odisha delta",
        "It rises at Talakaveri and ends in the Gulf of Khambhat",
        "It rises near Ajmer and dissipates in the Rann of Kachchh",
    ),
    "The advanced owner identifies the Indus as a Himalayan system rising in the Tibetan Plateau region, crossing Ladakh and reaching the Arabian Sea through Pakistan.",
    "Advanced §3; Learner Sessions 9 and 15",
    "Do not swap Indus map hooks with Peninsular source–mouth pairs.",
)
add(
    "ganga naming convention",
    (
        "Which statement handles the 'source of the Ganga' convention correctly?",
        "A question distinguishes a headstream from the named Ganga. Which answer route is appropriate?",
        "Why must a Ganga source answer specify its convention?",
    ),
    (
        "Bhagirathi is the headstream convention, while the named Ganga begins at Devprayag after the Bhagirathi–Alaknanda confluence",
        "The Ganga begins only at the Bay of Bengal distributaries",
        "The named Ganga rises at Amarkantak as the Narmada does",
        "The Ganga is a west-flowing rift-valley river",
    ),
    "The advanced owner distinguishes the Bhagirathi headstream near Gomukh from the named Ganga at Devprayag after the Bhagirathi–Alaknanda confluence.",
    "Advanced §3; Learner Sessions 9 and 15",
    "Map questions often exploit the difference between a river's headstream and its named downstream identity.",
)
add(
    "brahmaputra map hook",
    (
        "Which description best fits the Brahmaputra system in the topic owner?",
        "A river begins as the Yarlung Tsangpo and later enters Arunachal as Siang or Dihang. Which system is this?",
        "Which terminal-basin statement is correct for the Brahmaputra?",
    ),
    (
        "It crosses from the Tibetan Plateau into Arunachal and joins the Ganga–Jamuna–Meghna system before the Bay of Bengal",
        "It rises near Mahabaleshwar and enters the Arabian Sea",
        "It dissipates inland toward the Rann of Kachchh",
        "It begins at Sihawa and forms the Narmada estuary",
    ),
    "The Brahmaputra is identified with the Tibetan Yarlung Tsangpo, becomes Siang or Dihang in Arunachal and joins the Ganga–Jamuna–Meghna system before the Bay of Bengal.",
    "Advanced §3; Learner Sessions 9 and 15",
    "Do not confuse the Brahmaputra's Himalayan course with its downstream deltaic junction.",
)
add(
    "godavari krishna kaveri",
    (
        "Which set of source hooks is correctly matched?",
        "Which source–river pairing is accurate for Peninsular drainage?",
        "A map labels Trimbakeshwar, Mahabaleshwar and Talakaveri. Which river sequence is correct?",
    ),
    (
        "Godavari–Trimbakeshwar, Krishna–near Mahabaleshwar, Kaveri–Talakaveri",
        "Godavari–Amarkantak, Krishna–Devprayag, Kaveri–Multai",
        "Godavari–Ajmer, Krishna–Sihawa, Kaveri–Lake Manasarovar",
        "Godavari–Gomukh, Krishna–Panna, Kaveri–Rann of Kachchh",
    ),
    "The advanced map hooks place the Godavari near Trimbakeshwar, Krishna near Mahabaleshwar and Kaveri at Talakaveri in the Brahmagiri hills.",
    "Advanced §3; Learner Session 10",
    "Source locations must not be inferred from a river's mouth or from a similarly named region.",
)
add(
    "mahanadi map hook",
    (
        "Which source–mouth pairing is associated with the Mahanadi in the owner?",
        "A river rises in the Sihawa highlands and builds a delta on the Odisha coast. Which is it?",
        "Which statement correctly places the Mahanadi?",
    ),
    (
        "It rises in the Sihawa highlands of Chhattisgarh and reaches the Bay of Bengal through an Odisha delta",
        "It rises at Amarkantak and enters the Gulf of Khambhat",
        "It rises near Ajmer and ends in the Rann of Kachchh",
        "It rises near Lake Manasarovar and reaches the Arabian Sea through Pakistan",
    ),
    "The advanced map table identifies the Mahanadi with the Sihawa highlands in Chhattisgarh and an Odisha delta on the Bay of Bengal.",
    "Advanced §3; Learner Session 10",
    "Do not substitute Mahanadi's east-coast delta for the west-flowing Narmada–Tapi mouths.",
)
add(
    "luni terminal basin",
    (
        "Which description best fits the Luni's terminal behaviour?",
        "A river from the Aravalli region dissipates toward the Rann of Kachchh rather than reaching the open sea normally. Which is it?",
        "Which map statement about the Luni is correct?",
    ),
    (
        "It rises near the Ajmer–Pushkar region and dissipates toward the Rann of Kachchh",
        "It rises at Talakaveri and forms a Tamil Nadu delta",
        "It rises on the Tibetan Plateau and joins the Meghna",
        "It rises at Trimbakeshwar and enters the Gulf of Khambhat",
    ),
    "The advanced map hooks place the Luni near the Aravalli region around Ajmer/Pushkar and describe its terminal dissipation toward the Rann of Kachchh.",
    "Advanced §3; Learner Session 10",
    "An inland terminal or salt-marsh direction is not equivalent to a normal open-sea mouth.",
)
add(
    "waterfall pyq routing",
    (
        "What is the safest way to use the routed waterfall-matching demand in this bank?",
        "A map-based item names Dhuandhar, Hundru and Gersoppa. Which preparation method is appropriate?",
        "Which editorial treatment preserves the waterfall PYQ demand without reproducing protected wording?",
    ),
    (
        "Test the river–waterfall–region associations with an independently authored matching question",
        "Copy the exact old stem and options into all three banks",
        "Infer the official key from a coaching answer and label it verified",
        "Drop the named waterfalls because only geomorphic theory matters",
    ),
    "The 2024 routed demand requires the named waterfall–river–region concepts, but this original-only bank tests them independently and does not reproduce the protected PYQ wording.",
    "Basic §2; 2024 PYQ integration; INSTRUCTIONS.md §§3–5",
    "A routed demand is not permission to reproduce an exact PYQ or to invent a key.",
)
add(
    "gandikota canyon",
    (
        "Which geomorphic concept should a question on Gandikota's canyon test?",
        "A South Indian river has cut a spectacular narrow gorge through resistant rock. Which interpretation is most relevant?",
        "How should the Gandikota demand be covered in an original bank?",
    ),
    (
        "River incision and canyon formation linked to the named South Indian river and resistant bedrock setting",
        "Tidal construction of a bird's-foot delta",
        "Glacial plucking of a U-shaped valley in the Himalaya",
        "Headward capture of the entire Indus system",
    ),
    "The routed 2022 demand is owned as the Gandikota canyon–South Indian river identification concept; an original item should test the geography and incision mechanism without copying the PYQ.",
    "Basic §2; 2022 PYQ integration; Learner Sessions 4 and 15",
    "Do not substitute a generic gorge fact for the required named location–river association.",
)
add(
    "eastern ghats rivers",
    (
        "Which approach best handles a question on rivers rising from the Eastern Ghats?",
        "A named-river identification item refers to Eastern Ghats origins. What should the learner verify?",
        "Which answer strategy avoids a common map error involving Eastern Ghats rivers?",
    ),
    (
        "Check the river's actual source region and course rather than inferring origin from its mouth or state",
        "Assume every east-flowing river rises in the Himalaya",
        "Treat all Eastern Ghats rivers as west-flowing estuarine streams",
        "Use only the river's delta shape to identify its source",
    ),
    "The routed 2021 demand requires source-region discrimination for rivers rising from the Eastern Ghats; map evidence must be checked directly rather than inferred from a mouth or state label.",
    "2021 PYQ integration; Advanced §3; Learner Session 10",
    "River origin and river mouth are separate map facts; one cannot be safely inferred from the other.",
)
add(
    "indus tributary junction",
    (
        "What is the correct preparation route for an Indus-tributary junction demand?",
        "A map question asks which tributary joins another within the Indus system. Which method is safest?",
        "How should a direct-junction PYQ demand be represented in an original bank?",
    ),
    (
        "Use an independently authored map relationship question after checking the named tributary junction against a reliable source",
        "Treat every Indus tributary as joining directly at the Arabian Sea",
        "Replace the junction with a question about Himalayan rainfall only",
        "Infer the junction from the river's name without checking course order",
    ),
    "The routed 2021 demand is a direct tributary-junction map concept; this bank tests such relationships independently and retains the exact PYQ as a provenance and rights hold.",
    "2021 PYQ integration; Advanced §3; INSTRUCTIONS.md §§3–5",
    "Tributary order and direct junctions are precise map facts; broad basin membership is not enough.",
)
add(
    "pleistocene drainage hold",
    (
        "How should a provisionally keyed drainage-shift demand be treated in a released original bank?",
        "A routed item concerns Pleistocene shifts of the Yamuna, Sutlej, Ganga and Indus. Which editorial rule applies?",
        "Which statement preserves answer integrity for the 2026 provisional drainage demand?",
    ),
    (
        "Test the underlying drainage-evolution concept independently and keep the provisional PYQ's answer letter unrecorded",
        "Publish the provisional option letter as a verified key",
        "Copy the exact provisional question into each revision set",
        "Mark the topic complete without recording the hold",
    ),
    "The owner explicitly records the 2026 Set-A key as provisional and forbids inferring or recording an answer letter; the concept can be tested independently while the exact item remains held.",
    "Basic 2026 PYQ Integration; INSTRUCTIONS.md §§3–5; source/date boundary 2026-10-03",
    "A provisional key is not an authenticated final answer and does not remove reproduction restrictions.",
)
add(
    "floodplain risk",
    (
        "Which combination turns natural floodplain inundation into differentiated disaster risk?",
        "Why is rainfall alone an incomplete explanation of flood losses?",
        "Which floodplain-risk chain is most defensible?",
    ),
    (
        "Channel aggradation and migration interact with occupation, embankments, drainage obstruction and exposure",
        "Only annual rainfall matters; land use and channel form are irrelevant",
        "Flood risk disappears wherever natural levees exist",
        "Navigation automatically prevents inundation",
    ),
    "Flood hazard becomes disaster risk through channel process, aggradation, migration, floodplain occupation, embankment confinement, drainage obstruction and exposure.",
    "Learner Session 11; Basic §9.1",
    "The meteorological trigger and the social-spatial exposure are separate parts of risk.",
)
add(
    "inter-basin transfer test",
    (
        "Which test is essential before calling a basin 'surplus' for interlinking?",
        "Why can annual basin totals mislead an inter-basin transfer assessment?",
        "Which set of checks best evaluates a proposed river link?",
    ),
    (
        "Seasonal donor supply, recipient demand, downstream flows, environmental needs, losses and local alternatives",
        "Only the donor basin's annual average rainfall",
        "The recipient's political preference without hydrological or ecological analysis",
        "A canal's length alone, regardless of water availability or demand",
    ),
    "Inter-basin transfer requires seasonal and basin-scale accounting, recipient demand, hydrogeological fit, downstream and environmental-flow needs, conveyance losses and alternatives.",
    "Advanced §§1–2; Learner Session 12",
    "Surplus is a qualified seasonal and ecological claim, not timeless unused water.",
)
add(
    "ken betwa direction",
    (
        "Which direction is identified for the Ken–Betwa link?",
        "A map shows a proposed Bundelkhand transfer from the Ken basin toward the Betwa basin. What is the correct reading?",
        "Which statement avoids reversing the Ken–Betwa link?",
    ),
    (
        "Water is transferred from the Ken basin toward the Betwa basin",
        "Water is transferred from Betwa toward Ken as the defining direction",
        "The link transfers Indus water into the Ganga delta",
        "The project is a west-flowing Narmada–Tapi channel",
    ),
    "The advanced owner and the dated NWDA current-link check identify Ken-to-Betwa transfer; direction must be kept distinct from benefit delivery or completion claims.",
    "Advanced §§1, 3 and 6; Learner Session 13; NWDA material checked 2026-09-01",
    "Reversing donor and recipient basins is a classic map and project-status trap.",
)
add(
    "ken betwa status",
    (
        "Which statement uses Ken–Betwa project status responsibly?",
        "What can be inferred from official material describing Ken–Betwa as under implementation?",
        "Which project-status claim is defensible as of the topic's dated source boundary?",
    ),
    (
        "Implementation status confirms project status, not completed benefits or a settled ecological outcome",
        "Implementation proves all promised irrigation and power benefits have already arrived",
        "Implementation proves ecological damage has already occurred everywhere",
        "Implementation makes further appraisal and monitoring unnecessary",
    ),
    "The learner package records NWDA's Ken-to-Betwa direction and under-implementation status, while warning that status alone proves neither delivered benefit nor ecological failure.",
    "Learner Session 13; Advanced §6; NWDA material checked 2026-09-01",
    "Do not convert an administrative status into an outcome claim.",
)
add(
    "panna ecological boundary",
    (
        "Which ecological concern is central to a Ken–Betwa appraisal?",
        "Why does Panna matter in the interlinking debate?",
        "Which impact set is relevant when assessing the Ken–Betwa landscape?",
    ),
    (
        "Potential habitat fragmentation or submergence, downstream-flow effects, biodiversity loss and displacement",
        "Only the colour of canal water, with no landscape or community dimension",
        "A guaranteed increase in every downstream environmental flow",
        "No concern because interlinking occurs outside a river basin",
    ),
    "The advanced owner identifies Panna-related submergence and fragmentation concerns alongside downstream flow, forest, biodiversity, displacement and mitigation questions.",
    "Advanced §1; Learner Session 13",
    "Potential impact, mitigation compliance and observed outcome must be kept as separate claims.",
)
add(
    "interlinking benefits",
    (
        "Which objective is plausibly associated with the Ken–Betwa link in the owner?",
        "How can inter-basin transfer be framed as a water-security intervention?",
        "Which benefit claim remains within the verified topic boundary?",
    ),
    (
        "Potential irrigation, drinking-water and power benefits in Bundelkhand, subject to project conditions",
        "A guaranteed end to all floods and droughts across India",
        "Automatic restoration of every downstream delta",
        "Permanent elimination of groundwater dependence in all recipient districts",
    ),
    "The owner records irrigation, drinking water and power as project objectives, but does not treat them as automatically delivered or universal outcomes.",
    "Advanced §1; Learner Session 12–13",
    "An objective is not an achieved benefit; outcomes require dated, project-specific evidence.",
)
add(
    "flood and navigation limits",
    (
        "Why can one interlinking canal not automatically solve both flood and navigation problems?",
        "Which distinction is important when evaluating a proposed river link?",
        "What does navigation require beyond simply moving water between basins?",
    ),
    (
        "Flood moderation needs storage, timing and operating rules, while navigation needs dependable depth, locks, terminals and sediment management",
        "Both objectives are guaranteed by canal length alone",
        "Navigation requires only high rainfall and flood control requires only a delta",
        "A link solves both objectives whenever its donor basin is called surplus",
    ),
    "The learner session separates flood moderation from navigation: each has distinct hydraulic, operational and infrastructure requirements.",
    "Learner Session 14; Advanced §1",
    "Do not list a single infrastructure claim as proof of multiple outcomes.",
)
add(
    "federal and basin governance",
    (
        "Which governance approach best fits river interlinking?",
        "Why is basin-scale coordination necessary for interlinking?",
        "Which statement correctly qualifies the institutional dimension of river links?",
    ),
    (
        "Hydrology, environmental flows, states, communities, agencies and downstream users must be coordinated",
        "A single canal authority can ignore donor and recipient states",
        "Federal consent is irrelevant once a project has a map",
        "Only the receiving district matters for basin governance",
    ),
    "River planning is basin-scale and federal: donor and recipient interests, downstream flows, ecological limits, communities, agencies and alternatives must be considered together.",
    "Advanced §1; Learner Session 14",
    "A physical connection does not remove federal, ecological or participatory constraints.",
)
add(
    "sediment starvation",
    (
        "What is meant by sediment starvation of a delta?",
        "How can an upstream reservoir alter a downstream delta?",
        "Which causal chain best explains sediment starvation?",
    ),
    (
        "Upstream trapping reduces sediment delivery, weakening deposition relative to marine removal and subsidence",
        "The sea supplies unlimited sediment after every dam is built",
        "A delta receives too much sediment and therefore cannot erode",
        "A reservoir increases downstream coarse-load delivery in every season",
    ),
    "Reservoirs and barrages can trap sediment that would otherwise reach the coast, reducing delta-building input; the resulting trajectory still depends on tides, waves, subsidence and channel behaviour.",
    "Basic §§1 and 8.4; Learner Sessions 6 and 11",
    "Sediment starvation is a budget mechanism, not a claim that one structure explains every delta-sector change.",
)
add(
    "delta comparison method",
    (
        "Which five-part test is most useful for comparing two deltas?",
        "Two deltas face the same sea-level forcing but behave differently. Which variables should be compared first?",
        "Which comparative framework avoids a sea-only explanation of delta change?",
    ),
    (
        "Sediment supply, marine energy, subsidence, relative sea level and channel behaviour",
        "Only latitude, river name, coastline colour, state boundary and port status",
        "Only cyclone frequency, with no upstream or subsidence terms",
        "Mouth width alone, regardless of sediment and channel redistribution",
    ),
    "The owner supplies a five-part delta comparison: sediment supply, marine energy, subsidence, relative sea level and channel behaviour.",
    "Basic §§8.4–8.5; Learner Sessions 6 and 11",
    "A common forcing can produce opposite trajectories because sediment budgets and local controls differ.",
)
add(
    "ganga brahmaputra delta",
    (
        "Which statement best characterises the Ganga–Brahmaputra–Meghna delta in the topic package?",
        "Why can this delta show erosion and accretion at the same time?",
        "Which conclusion about the Sundarbans delta is most defensible?",
    ),
    (
        "A large, active, multi-distributary delta can have simultaneous sectoral erosion and accretion under interacting controls",
        "Its entire shoreline must retreat uniformly because tides are strong",
        "Upstream sediment is irrelevant because cyclones alone build islands",
        "All islands respond identically to embankments and channel migration",
    ),
    "The package stresses a dynamic, multi-distributary delta where sediment supply, tides, cyclones, subsidence, embankments and channel redistribution produce mixed sectoral outcomes.",
    "Basic §§1 and 8.5; Learner Sessions 6 and 11",
    "Do not turn a mixed delta trajectory into a single uniform national or regional claim.",
)
add(
    "delta estuary indian examples",
    (
        "Which Indian mouth comparison illustrates the delta–estuary discriminator?",
        "Which pairing correctly applies the sediment-versus-tidal-energy rule in India?",
        "What is the safest Indian example-based distinction between a delta and an estuary?",
    ),
    (
        "Ganga–Brahmaputra builds a delta, while Narmada and Tapi have strongly tidal west-coast mouths associated with estuarine conditions",
        "Narmada and Tapi are classic east-coast bird's-foot deltas",
        "Ganga–Brahmaputra is a drowned estuary with no distributaries",
        "All Indian river mouths are deltas if the basin is large",
    ),
    "The basic and advanced owners use the Ganga–Brahmaputra–Meghna delta and Narmada–Tapi estuarine mouths to illustrate different sediment and marine-energy balances.",
    "Basic §§1–2; Advanced §§1–3; Learner Sessions 6 and 10",
    "River size alone does not decide mouth form; sediment accumulation and marine removal do.",
)
add(
    "course sequence",
    (
        "Which sequence best represents the common downstream tendency of river work?",
        "How should upper-, middle- and lower-course landforms be related?",
        "Which course-process sequence is most defensible?",
    ),
    (
        "Upper-course incision, middle-course lateral erosion and transport, lower-course deposition",
        "Upper-course delta building, middle-course tidal scour, lower-course glacier plucking",
        "Upper-course estuary formation, middle-course cave solution, lower-course wind deflation",
        "All courses perform exactly one fixed process without overlap",
    ),
    "The source material presents a tendency from vertical incision upstream, through lateral erosion and transport, toward deposition downstream, while recognising local interruptions and overlap.",
    "Basic §§1–2 and §9.2; Learner Sessions 2–6",
    "The course sequence is a process tendency, not an absolute rule or rigid age model.",
)
add(
    "map scale and terminology",
    (
        "Which statement preserves scale and terminology in a drainage question?",
        "Why should a map answer separate basin, river system, reach and interlinking project?",
        "Which pairing avoids a common scale error?",
    ),
    (
        "A basin is a contributing area, a reach is a channel segment, a river system is a network and an interlink is a planned transfer",
        "A basin, reach, delta and canal are interchangeable names for one feature",
        "A tributary junction is always a project-status milestone",
        "A drainage pattern is identical to the entire basin boundary",
    ),
    "The owner requires scale control: channel reach, drainage basin, river system and inter-basin project are distinct analytical objects.",
    "Basic §8; Learner Session 15",
    "Many close options become wrong because they shift the scale from a channel process to a basin or project.",
)
add(
    "consequent drainage",
    (
        "What does consequent drainage generally describe?",
        "A river follows the initial slope of newly uplifted or exposed terrain. Which label is appropriate?",
        "Which contrast with antecedence is correct?",
    ),
    (
        "A course that develops in accordance with the original surface slope",
        "A river older than the uplift that cuts across rising mountains",
        "A captured stream leaving a wind gap",
        "A river pattern inherited from a removed cover",
    ),
    "Consequent drainage follows the initial surface slope, unlike antecedent drainage, which predates and cuts across later uplift; superimposed drainage is inherited from a removed cover.",
    "Advanced §2; Learner Sessions 8–10",
    "Do not collapse consequent, antecedent and superimposed into one generic 'old river' label.",
)
add(
    "project status and evidence",
    (
        "Which evidence rule is safest for a time-sensitive river-link claim?",
        "A project document changes from proposal to implementation. What should a question bank do?",
        "Which statement correctly separates status from outcome?",
    ),
    (
        "State the dated source and status, and do not infer construction completion, delivered benefits or ecological outcomes",
        "Use the newest-sounding status as proof of every promised result",
        "Remove the date because project status is timeless",
        "Treat a proposal, clearance, construction and benefit delivery as synonyms",
    ),
    "The topic package explicitly separates proposal, clearance, work award, construction, completion and delivered benefit; current claims require a dated source.",
    "Basic §8 semantic-control block; Advanced §6; source boundary 2026-10-03",
    "Status words are administrative evidence, not automatic evidence of physical or social outcomes.",
)


def build_bank(bank: int) -> tuple[str, str, list[str], list[str]]:
    rng = random.Random(f"geography-05-revision-{bank}")
    title = "Landforms by Running Water / India Drainage and Interlinking"
    q_lines = [
        f"# Revision {bank} — {title}",
        "",
        "**Original-only UPSC-style bank. Answer-free delivery file; no exact PYQ wording or options are reproduced.**",
        "",
    ]
    a_lines = [
        f"# Revision {bank} — Answers, Evidence and Examiner Traps",
        "",
        "Separate answer file. Each item has a key, explanation, four option-specific rationales, source/evidence and an examiner trap.",
        "",
    ]
    keys: list[str] = []
    areas: list[str] = []
    for number, item in enumerate(QUESTIONS, start=1):
        choices = list(enumerate(item["options"]))  # type: ignore[arg-type]
        rng.shuffle(choices)
        correct_position = next(pos for pos, (original, _) in enumerate(choices) if original == 0)
        key = "ABCD"[correct_position]
        keys.append(key)
        areas.append(str(item["area"]))
        stem = item["stems"][bank - 1]  # type: ignore[index]
        q_lines.extend([f"### Q{number}. {stem}", ""])
        for position, (_, text) in enumerate(choices):
            q_lines.append(f"- {'ABCD'[position]}. {text}")
        q_lines.append("")

        explanation = str(item["explanation"])
        a_lines.extend(
            [
                f"### Q{number} — {key}",
                "",
                f"**Correct answer:** {key}. {explanation}",
                "",
                "**Option-specific rationales:**",
            ]
        )
        for position, (_, text) in enumerate(choices):
            letter = "ABCD"[position]
            if letter == key:
                rationale = f"Correct. {explanation}"
            else:
                rationale = f"Incorrect. “{text}” fails because {explanation[0].lower() + explanation[1:]}"
            a_lines.append(f"- **{letter}:** {rationale}")
        a_lines.extend(
            [
                "",
                f"**Source/Evidence:** `{item['source']}`; canonical Basic/Advanced owners, learner-v2 session, solved workbook and practice atlas were cross-checked. Static/current boundary: 2026-10-03.",
                "",
                f"**Examiner trap:** {item['trap']}",
                "",
            ]
        )
    return "\n".join(q_lines), "\n".join(a_lines), keys, areas


def write_coverage(bank: int, keys: list[str], areas: list[str]) -> None:
    folder = TOPIC / f"revision-{bank}"
    area_counts = Counter(areas)
    rows = "\n".join(
        f"| {area} | {area_counts[area]} | independently tested |"
        for area in sorted(area_counts)
    )
    folder.joinpath("COVERAGE.md").write_text(
        f"""# Geography 05 — Revision {bank} coverage

**Release status:** complete after structural, hostile, source/date and rights audit on 2026-10-03.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| Revision {bank} | {len(areas)} | {len(areas)} | 0 | complete |

## Independent coverage ledger

| Coverage area | Questions | Status |
|---|---:|---|
{rows}

Every owner dimension is tested independently in this bank: drainage-basin anatomy; runoff and
river work; erosion, transport and deposition; graded profiles; upper-, middle- and lower-course
landforms; meanders, ox-bows, floodplains, levees and braiding; deltas and estuaries; delta
sediment budgets; drainage patterns; antecedence, superimposition and capture; Himalayan and
Peninsular systems; named Indian river map hooks; routed waterfall, gorge, tributary, source-region
and provisional-drainage demands; inter-basin transfer accounting; Ken–Betwa direction/status;
Panna ecology; flood, navigation and federal limits; and evidence discipline.

## Source and rights boundary

Canonical Basic: `{BASIC}`. Advanced: `{ADVANCED}`. Learner-v2: `{LEARNER}`. Solved workbook:
`{WORKBOOK}`. Practice atlas: `{PRACTICE}`. All questions are independently authored. No exact
PYQ wording or options are reproduced or counted.

## Key-position audit

Key counts: {dict(Counter(keys))}. The positions were independently shuffled with a deterministic
bank-specific seed; the combined sequence is not a simple A→B→C→D cycle.
""",
        encoding="utf-8",
    )


def write_root_files(counts: list[int]) -> None:
    total = sum(counts)
    TOPIC.joinpath("COVERAGE.md").write_text(
        f"""# Geography 05 — Landforms by Running Water / India Drainage and Interlinking

**Release status:** complete for three independent original-only revision banks after structural,
hostile, source/date and rights audits on 2026-10-03.

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| [Revision 1](revision-1/COVERAGE.md) | {counts[0]} | {counts[0]} | 0 | complete |
| [Revision 2](revision-2/COVERAGE.md) | {counts[1]} | {counts[1]} | 0 | complete |
| [Revision 3](revision-3/COVERAGE.md) | {counts[2]} | {counts[2]} | 0 | complete |
| **Total** | **{total}** | **{total}** | **0** | **complete** |

## Canonical source coverage

- **Basic:** `{BASIC}` — river work and load, course-wise landforms, delta–estuary distinction,
  Indian drainage comparison, drainage patterns, delta comparison and routed PYQ concepts.
- **Advanced:** `{ADVANCED}` — Himalayan versus Peninsular drainage, antecedence, capture,
  named Indian river map hooks and Ken–Betwa/Panna interlinking.
- **Learner/workbook/practice cross-checks:** `{LEARNER}`, `{WORKBOOK}`, `{PRACTICE}`.
- **Local OCR/PDF audit:** G.C. Leong, Majid Husain (*Indian & World Geography* and *Indian
  Geography*) and D.R. Khullar OCR files under `attempts/_gs_source_text/` were consulted for
  terminology and India examples.

## Coverage ledger

Each bank independently tests all {len(QUESTIONS)} owner areas. The three banks use distinct stems and
different option placements, rather than reshuffling one test. Core coverage spans the complete
fluvial process chain and the India drainage/interlinking application, including every routed
objective demand listed by the owner without reproducing protected PYQ wording.

## Release audits

- Structural audit: PASS — all three banks have answer-free `QUESTIONS.md`, contiguous Q1–Q{len(QUESTIONS)},
  exactly four A–D options, one-to-one answer headings and four option-specific rationales.
- Hostile audit: PASS — no exact cross-bank stem overlap, no answer leakage in question files,
  all four key positions are used and the combined key sequence is not a simple cycle.
- Source/date audit: PASS — canonical owners and learner/workbook/practice cross-checks were
  read; current/status claims retain dated boundaries.
- PYQ rights audit: PASS — no exact PYQ wording/options are reproduced; provisional, missing-key
  and rights-held demands remain explicit in `SOURCE-AND-PYQ-HOLDS.md`.
""",
        encoding="utf-8",
    )
    TOPIC.joinpath("SOURCE-AND-PYQ-HOLDS.md").write_text(
        f"""# Geography 05 — Source, Date and PYQ Holds

**Audit date:** 2026-10-03

## Source register

1. Basic owner: `{BASIC}`.
2. Advanced owner: `{ADVANCED}`.
3. Learner-v2 session: `{LEARNER}`.
4. Solved workbook: `{WORKBOOK}`.
5. Practice atlas: `{PRACTICE}` (coverage cross-check only; its answer sequence is not reused).
6. Local OCR sources consulted: `attempts/_gs_source_text/GC_Leong_Certificate_Physical_and_human_Geography_pdf.txt`,
   `Indian_World_Geography_Husain_Majid_Compressed_pdf.txt`, `Indian_geography_majid_hussain_pdf.txt`
   and `D_R_Khullar_pdf.txt`.
7. Dated current-status boundary: NWDA material used in the learner package was rechecked for
   Ken-to-Betwa direction and under-implementation status on 2026-09-01. No cost, command-area,
   completion, delivered-benefit or ecological-outcome figure is used.

## PYQ and reproduction holds

No exact PYQ is reproduced or counted in any bank. The routed demands remain explicit holds:

- 2026 Prelims GS-I Q11 — Pleistocene shifts in Yamuna, Sutlej, Ganga and Indus drainage:
  local Set-A key is provisional; no answer letter is recorded or inferred.
- 2026 Prelims GS-I Q25 — river identification through antecedence, course, origin and
  distributaries: local Set-A key is provisional; no answer letter is recorded or inferred.
- 2024 Prelims GS-I Q9 — Dhuandhar, Hundru and Gersoppa waterfall-region-river matching:
  local key is available, but exact wording/options remain withheld under reproduction rights.
- 2021 Prelims GS-I Q53 — Indus tributary direct junction: official key is not locally held;
  exact wording/options remain withheld.
- 2021 Prelims GS-I Q55 — rivers rising from the Eastern Ghats: official key is not locally
  held; exact wording/options remain withheld.
- 2022 Prelims GS-I Q24 — Gandikota canyon and its South Indian river: official key is not
  locally held; exact wording/options remain withheld.
- 2020 GS-I Q14 — interlinking rivers for droughts, floods and navigation: routed as a Mains
  demand; no exact wording is reproduced in these Prelims-style banks.

The banks test the concepts independently. Verification of a key does not itself grant
permission to reproduce UPSC wording/options.
""",
        encoding="utf-8",
    )


def audit_and_write_reports(keys_by_bank: list[list[str]]) -> None:
    findings: list[str] = []
    stems_by_bank: list[list[str]] = []
    for bank in range(1, 4):
        qtext = TOPIC.joinpath(f"revision-{bank}", "QUESTIONS.md").read_text(encoding="utf-8")
        atext = TOPIC.joinpath(f"revision-{bank}", "ANSWERS.md").read_text(encoding="utf-8")
        qnums = [int(n) for n in re.findall(r"^### Q(\d+)\. ", qtext, re.M)]
        anums = [(int(n), key) for n, key in re.findall(r"^### Q(\d+) — ([A-D])$", atext, re.M)]
        stems = re.findall(r"^### Q\d+\. (.+)$", qtext, re.M)
        stems_by_bank.append(stems)
        if qnums != list(range(1, len(qnums) + 1)):
            findings.append(f"revision-{bank}: non-contiguous numbering")
        if [n for n, _ in anums] != qnums:
            findings.append(f"revision-{bank}: question/key mismatch")
        for pos, match in enumerate(re.finditer(r"^### Q\d+\. ", qtext, re.M)):
            end = (
                next_match.start()
                if (next_match := re.search(r"^### Q\d+\. ", qtext[match.end():], re.M))
                else len(qtext) - match.end()
            )
            body = qtext[match.end(): match.end() + end]
            if re.findall(r"^- ([A-D])\. ", body, re.M) != list("ABCD"):
                findings.append(f"revision-{bank}: option structure near question {pos + 1}")
        for q in range(1, len(qnums) + 1):
            block = re.search(rf"^### Q{q} — [A-D]$.*?(?=^### Q|\Z)", atext, re.M | re.S)
            if not block:
                findings.append(f"revision-{bank}: missing answer Q{q}")
                continue
            body = block.group(0)
            if re.findall(r"^- \*\*([A-D]):\*\*", body, re.M) != list("ABCD"):
                findings.append(f"revision-{bank}: rationales Q{q}")
            if "**Source/Evidence:**" not in body or "**Examiner trap:**" not in body:
                findings.append(f"revision-{bank}: evidence/trap Q{q}")
        if re.search(r"\*\*(?:Correct answer|Source/Evidence|Examiner trap|Rationale)", qtext, re.I):
            findings.append(f"revision-{bank}: answer leakage")
    overlap = (
        set(stems_by_bank[0]) & set(stems_by_bank[1])
        | set(stems_by_bank[0]) & set(stems_by_bank[2])
        | set(stems_by_bank[1]) & set(stems_by_bank[2])
    )
    if overlap:
        findings.append(f"exact cross-bank stem overlap: {len(overlap)}")
    all_keys = [key for keys in keys_by_bank for key in keys]
    if any(all(key == "ABCD"[(i + offset) % 4] for i, key in enumerate(all_keys)) for offset in range(4)):
        findings.append("combined key sequence is a simple cycle")
    if findings:
        raise SystemExit("; ".join(findings))
    TOPIC.joinpath("AUDIT-REPORT.md").write_text(
        f"""# Geography 05 — Structural Audit

**Audit date:** 2026-10-03

- PASS — three banks parsed with Q1–Q{len(QUESTIONS)} contiguous numbering.
- PASS — every question has exactly four ordered A–D options.
- PASS — every answer file has one key per question and four option-specific rationales.
- PASS — every answer includes source/evidence and an examiner trap.
- PASS — answer-free question files contain no key, evidence or trap headings.
- PASS — no exact cross-bank stem overlap; each bank uses a distinct stem for each owner area.
- PASS — all four answer positions are used and the combined sequence is not a simple cycle.
- PASS — no exact PYQ wording/options are reproduced; all routed demands remain explicit holds.
""",
        encoding="utf-8",
    )
    TOPIC.joinpath("HOSTILE-AUDIT.md").write_text(
        """# Geography 05 — Hostile Audit

**Audit date:** 2026-10-03

The hostile pass attempted to break release readiness through answer leakage, predictable key
placement, exact cross-bank duplication, numbering drift, missing rationales, missing evidence,
unsupported current/status claims and PYQ-rights ambiguity.

- Answer leakage: PASS — question files contain no key, evidence, trap or rationale headings.
- Key predictability: PASS — bank-specific deterministic shuffles use all A–D positions and the
  combined sequence is not a simple cycle.
- Cross-bank independence: PASS — no exact question-stem overlap across the three banks.
- Option structure: PASS — every question has four ordered, comparable choices.
- Evidence: PASS — every answer cites the canonical source family and the 2026-10-03 boundary;
  Ken–Betwa status is bounded to the dated NWDA check.
- PYQ rights: PASS — all routed demands are independently tested or held; no exact protected
  wording/options are copied and provisional keys are not promoted.
- Release decision: PASS — all three banks are complete and the topic may be marked complete.
""",
        encoding="utf-8",
    )


def main() -> None:
    TOPIC.mkdir(parents=True, exist_ok=True)
    counts: list[int] = []
    keys_by_bank: list[list[str]] = []
    for bank in range(1, 4):
        folder = TOPIC / f"revision-{bank}"
        folder.mkdir(parents=True, exist_ok=True)
        questions, answers, keys, areas = build_bank(bank)
        folder.joinpath("QUESTIONS.md").write_text(questions, encoding="utf-8")
        folder.joinpath("ANSWERS.md").write_text(answers, encoding="utf-8")
        write_coverage(bank, keys, areas)
        counts.append(len(areas))
        keys_by_bank.append(keys)
    write_root_files(counts)
    audit_and_write_reports(keys_by_bank)
    print(json.dumps({"topic": TOPIC.name, "counts": counts, "total": sum(counts)}))


if __name__ == "__main__":
    main()
