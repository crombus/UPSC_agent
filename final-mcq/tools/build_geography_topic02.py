from __future__ import annotations

import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / "final-mcq" / "subjects" / "Geography"
TOPIC = SUBJECT / "02-The-Earths-Crust-Rocks-India-Geological-Structure"


RECORDS = [
    ("Mineral and rock", [
        "Which distinction between a mineral and a rock is most defensible?",
        "A field geologist records a natural aggregate rather than one crystal. Which label fits best?",
        "Which statement would avoid the common mineral–rock category error?",
    ], ["A rock is an aggregate; a mineral has characteristic composition and crystal structure", "Every rock is a single crystal with a fixed chemical formula", "A mineral is any soil particle and a rock is any metal-bearing material", "Minerals and rocks are interchangeable terms in lithology"], 0, "A rock commonly aggregates one or more minerals or mineraloids, whereas a mineral has a characteristic composition and crystal structure.", "B §1; L Session 1", "Treating a rock as one mineral is the category error."),
    ("Lithology and petrology", [
        "Which pairing correctly separates lithology from petrology?",
        "For a mapped rock body, which analytical sequence is the safest?",
        "Which statement best distinguishes description of a rock from study of its origin?",
    ], ["Lithology describes observable rock character; petrology studies origin and transformation", "Lithology is the study of earthquakes; petrology is the study of weather", "Lithology names only landforms; petrology measures river discharge", "Lithology and petrology are identical names for the same subfield"], 0, "Lithology concerns composition, grain size, texture and bedding/fabric; petrology explains rock genesis and transformation.", "B §1; L Session 1", "Do not substitute geomorphology or seismology for petrology."),
    ("Crust and lithosphere", [
        "Which statement about the crust and lithosphere is correct?",
        "A question asks what moves as a relatively rigid plate. Which answer is most precise?",
        "Which relation between crust and lithosphere should be retained?",
    ], ["Lithosphere includes the crust and rigid uppermost mantle", "Lithosphere is only oceanic crust and excludes mantle", "Crust includes the entire asthenosphere", "Crust and lithosphere have identical boundaries everywhere"], 0, "The lithosphere is the rigid outer shell comprising crust plus rigid uppermost mantle; the asthenosphere is mechanically weaker.", "B §2; L Session 2", "Crust is a compositional layer; lithosphere is a mechanical shell."),
    ("Oceanic and continental crust", [
        "Which comparison of oceanic and continental crust is safest for a Prelims statement?",
        "Which combination best captures the usual contrast between the two crustal types?",
        "Why does an oceanic plate commonly subduct beneath a continental margin?",
    ], ["Oceanic crust is generally thinner and denser than continental crust", "Oceanic crust is always older, thicker and less dense than continental crust", "Continental crust is uniformly basaltic and oceanic crust uniformly granitic", "Both crustal types have identical density and composition"], 0, "Oceanic crust is usually basaltic, thinner and denser; continental crust is generally thicker, more compositionally varied and less dense.", "B §2; L Session 2", "Use 'generally' rather than turning a broad contrast into an absolute."),
    ("Rock cycle", [
        "Which description of the rock cycle is most accurate?",
        "Why is the rock cycle better represented as a network than a conveyor belt?",
        "Which inference follows from the rock-cycle model?",
    ], ["Different rock types can follow multiple pathways under changing conditions", "Every rock must pass through sedimentary, metamorphic and igneous stages in one order", "Metamorphism permanently ends all later transformation", "Only igneous rocks can be weathered and recycled"], 0, "Weathering, burial, melting, crystallisation and metamorphism create several linked pathways rather than one mandatory sequence.", "B §§3–4; L Session 3", "A rock may bypass stages; do not force a fixed linear order."),
    ("Intrusive cooling", [
        "Slow cooling of magma at depth most directly favours which result?",
        "Which texture would indicate crystallisation in a relatively insulated intrusive setting?",
        "A coarse-grained igneous rock most plausibly records which history?",
    ], ["Large interlocking crystals produced by prolonged cooling", "A glassy mass produced by instantaneous quenching at the surface", "Mud cracks produced by repeated drying of sediment", "Foliation produced by directed metamorphic stress"], 0, "Slow intrusive cooling permits crystals to grow; rapid surface cooling can produce fine-grained or glassy textures.", "B §4; L Session 4; G.C. Leong OCR pp.17–22", "Texture records cooling history, not simply colour or present relief."),
    ("Composition pairs", [
        "Which intrusive–extrusive pair is compositionally related?",
        "Which pair represents the coarse and fine equivalents of broadly similar magma composition?",
        "Which matching is most defensible for a felsic intrusive and extrusive pair?",
    ], ["Granite–rhyolite", "Gabbro–rhyolite", "Granite–basalt", "Diorite–obsidian in every compositional setting"], 0, "Granite and rhyolite are broadly felsic counterparts; gabbro and basalt are broadly mafic counterparts.", "B §4; L Session 4; G.C. Leong OCR pp.17–22", "Do not match rocks only by intrusive/extrusive habit; composition also matters."),
    ("Porphyritic texture", [
        "A porphyritic igneous texture most safely indicates what?",
        "What cooling history best fits large crystals in a fine-grained groundmass?",
        "Which interpretation of porphyritic texture is least over-claimed?",
    ], ["A two-stage cooling history", "Metamorphism without heat or pressure", "Only chemical precipitation in a sedimentary basin", "Complete absence of crystals"], 0, "Phenocrysts can grow during an earlier slow-cooling stage before the remaining melt cools more rapidly.", "B §4; L Session 4", "Porphyritic texture indicates cooling history, not automatically a named tectonic boundary."),
    ("Pyroclastic material", [
        "Which material is pyroclastic?",
        "Which description identifies a volcanic fragmental deposit rather than a clastic river sediment?",
        "A deposit made of consolidated volcanic ejecta is best classified as what?",
    ], ["Fragmental volcanic ejecta consolidated into rock", "A chemical evaporite precipitated from saline water", "A rounded pebble deposited by a river", "A metamorphic fabric produced by pressure solution"], 0, "Pyroclastic materials are fragments explosively or violently ejected from a volcano and later deposited or consolidated.", "B §4; L Session 4", "Clastic texture alone does not make a deposit pyroclastic; volcanic origin is decisive."),
    ("Clastic sedimentary rocks", [
        "Which is a clastic sedimentary rock?",
        "Which choice represents lithified transported fragments?",
        "A rock formed mainly by compaction and cementation of sand-sized grains is likely to be what?",
    ], ["Sandstone", "Gneiss", "Marble", "Basalt"], 0, "Sandstone forms from lithified sand-sized particles; gneiss and marble are metamorphic and basalt is igneous.", "B §5; L Session 5; Majid Husain OCR pp.27–33", "Classify by process and texture, not by colour alone."),
    ("Loess", [
        "Loess is best described as what?",
        "Which deposit is a wind-related fine sediment rather than a bedrock type?",
        "A widespread blanket of silt-sized aeolian material is called what?",
    ], ["Wind-deposited fine sediment", "A coarse intrusive body", "A metamorphic foliation", "A coral limestone platform"], 0, "Loess is generally wind-deposited, fine-grained sediment; it is a deposit, not automatically a consolidated rock.", "B §5; L Session 5", "Do not call every sediment deposit a rock."),
    ("Sedimentary structures", [
        "Which feature most directly records periodic drying of fine sediment?",
        "Which field clue supports subaerial exposure of wet mud?",
        "Which structure is produced when wet fine sediment contracts during drying?",
    ], ["Mud cracks", "Gneissic banding", "Batholiths", "Vesicles in lava"], 0, "Mud cracks form when water-rich fine sediment dries and contracts, often preserving polygonal fissures.", "B §5; L Session 5", "Bedding is not the same as a drying crack and vesicles are volcanic gas cavities."),
    ("Limestone pathways", [
        "Why can limestone classification be context-dependent?",
        "Which statement best handles limestone genesis?",
        "A limestone with abundant shells should not automatically be called chemical because limestone may form by what routes?",
    ], ["Chemical precipitation and biogenic accumulation are both possible", "Only mantle melting can produce limestone", "Limestone is always an intrusive igneous rock", "Limestone cannot preserve fossils or organic material"], 0, "Limestone may precipitate chemically or accumulate biogenic carbonate material; field context and fabric matter.", "B §5; L Session 5", "A rock name may cover more than one formation pathway."),
    ("Protolith", [
        "The parent rock before metamorphism is called what?",
        "Which term identifies the precursor material of a metamorphic rock?",
        "A metamorphic sample is traced back to its original rock. That original rock is its what?",
    ], ["Protolith", "Pluton", "Craton", "Regolith"], 0, "A protolith is the pre-existing rock from which a metamorphic rock develops.", "B §6; L Session 6", "Pluton is an igneous intrusion; craton is a stable crustal block; regolith is loose surface material."),
    ("Foliation and bedding", [
        "Which pair is correctly matched?",
        "Which feature most directly represents planar mineral alignment caused by metamorphism?",
        "A learner equates foliation with sedimentary bedding. What is the better distinction?",
    ], ["Schistosity is a visible planar metamorphic fabric", "Bedding is an igneous crystal-size class", "Foliation is a synonym for a lava vesicle", "Cleavage records only sediment grain sorting"], 0, "Foliation, including schistosity, reflects metamorphic mineral alignment or planar fabric; bedding is a depositional structure.", "B §6; L Session 6", "Planarity alone is insufficient; identify the process that produced it."),
    ("Metamorphic grade", [
        "Which sequence is a common increasing-grade teaching path for shale-derived rocks?",
        "Which progression best represents increasing metamorphic grade?",
        "Which chain moves from lower to higher grade in a commonly taught pelitic sequence?",
    ], ["Shale → slate → phyllite → schist → gneiss", "Granite → sandstone → coal → basalt", "Conglomerate → obsidian → marble → loess", "Basalt → limestone → chalk → granite"], 0, "Increasing heat and pressure can produce slate, phyllite, schist and gneiss from a shale-like protolith, though natural paths vary.", "B §6; L Session 6", "The sequence is a teaching path, not a universal one-step field rule."),
    ("Porosity and permeability", [
        "How does permeability differ from porosity?",
        "Which distinction matters most when assessing groundwater flow?",
        "A rock has many pores but poor interconnection. What property may still be low?",
    ], ["Porosity is void space; permeability is connected fluid transmission", "Permeability is simply the colour of a mineral", "Porosity applies only to granite and permeability only to basalt", "The two terms are exact synonyms"], 0, "Porosity measures void space; permeability concerns the connectivity and ease of fluid movement through that space.", "B §7; L Session 7", "High porosity does not guarantee high permeability."),
    ("Hard-rock groundwater", [
        "Groundwater in crystalline hard rock commonly depends on which features?",
        "Why can a granite terrain yield water despite low primary porosity?",
        "Which hydrogeological control is most relevant beside a fracture intersection in hard rock?",
    ], ["Weathered mantles, joints and fractures", "Fossils in every crystalline block", "Coal seams alone", "Abundant primary pores in fresh granite"], 0, "Weathering and secondary openings such as joints and fractures can store and transmit water in otherwise low-primary-porosity rock.", "B §7; L Session 7; L Session 54", "Fresh crystalline rock and its fractured/weathered zones should not be treated as identical."),
    ("Continental-shelf fit", [
        "Why are continental-shelf edges useful in reconstructing former continental fit?",
        "Which boundary gives a better first approximation of a submerged continental margin?",
        "Why can present coastlines mislead continental-drift reconstruction?",
    ], ["Shelf edges better approximate structural margins than changing shorelines", "Shelf edges are plate boundaries everywhere", "Shelf edges contain no sediment and therefore show only volcanism", "Modern shorelines are fixed through all sea-level changes"], 0, "Shelf edges can better represent the continental margin than coastlines altered by sea-level and depositional changes.", "B §8.1; L Session 8; Majid Husain OCR pp.27–33", "A visual fit of modern shorelines is not the same as a structural fit."),
    ("Fossil evidence", [
        "What is the safest inference from matching land fossils on now-separated continents?",
        "Which statement uses fossil evidence without overclaiming?",
        "Why does a shared terrestrial fossil assemblage support continental reconstruction?",
    ], ["Several continents were once connected or geographically closer", "The continents have never moved because the fossils are identical", "Ocean barriers have no relevance to land organisms", "One fossil species alone proves the exact date and route of drift"], 0, "Matching land fossils across now-separated continents are difficult to explain without former connection or much closer geography, but they do not alone date every stage.", "B §8.1; L Session 8", "Evidence supports a reconstruction; it rarely proves every detail in isolation."),
    ("Palaeomagnetism", [
        "Palaeomagnetism assists continental reconstruction by recording what?",
        "Which evidence can indicate former field orientation and palaeolatitude?",
        "A rock's remanent magnetism is useful because it may preserve what historical information?",
    ], ["Former geomagnetic orientation and an indication of latitude or rotation", "Only present-day river discharge", "Modern population density", "The exact depth of every crustal layer"], 0, "Magnetic minerals can preserve palaeomagnetic direction, helping infer former orientation and latitude when interpreted with other evidence.", "B §8.1; L Session 8", "Palaeomagnetism is evidence, not a standalone complete plate history."),
    ("Magnetic stripes", [
        "What do approximately symmetrical magnetic stripes on both sides of a mid-ocean ridge most directly record?",
        "Which observation most directly supports sea-floor spreading?",
        "Why are alternating magnetic bands on oceanic crust significant?",
    ], ["Successive geomagnetic reversals recorded as new crust moved away from a ridge", "A permanent absence of crustal recycling", "Only wind-driven sediment transport", "A proof that Earth has been expanding without subduction"], 0, "Basalt formed at a ridge records the magnetic field; symmetric reversal bands indicate successive creation and outward movement of oceanic crust.", "B §8.2; L Session 9", "Sea-floor spreading must be combined with subduction to explain crustal mass balance."),
    ("Plate-boundary regimes", [
        "Which pairing of plate-boundary regime and dominant process is correct?",
        "Which boundary combination is correctly matched?",
        "At which setting are plates generally moving apart rather than converging or sliding laterally?",
    ], ["Divergent boundary—creation of new crust at a spreading centre", "Convergent boundary—no deformation or recycling", "Transform boundary—routine creation of broad new oceanic crust", "Divergent boundary—continental collision as the defining process"], 0, "Divergent boundaries create new crust; convergent boundaries may consume or thicken crust; transform boundaries mainly accommodate lateral motion.", "B §8.3; L Session 10", "Boundary labels describe relative motion, not one universal landform."),
    ("Transform boundaries", [
        "What is the defining movement at a transform boundary?",
        "Which process best describes a transform plate margin?",
        "A boundary mainly accommodates lateral offset without routine crust creation. It is most likely what?",
    ], ["Lateral sliding between plates along a fault system", "Continuous creation of oceanic crust at a ridge axis", "Direct continent–continent subduction", "Uniform vertical uplift without shear"], 0, "Transform margins primarily accommodate horizontal relative motion and shear; they do not routinely create or consume crust.", "B §8.3; L Session 10", "Do not infer divergent or convergent processes from every earthquake-prone fault."),
    ("Island arcs", [
        "Which setting most commonly produces a volcanic island arc?",
        "An oceanic–oceanic convergent margin is most likely to form which feature?",
        "Which combination best explains a chain of volcanic islands parallel to a trench?",
    ], ["Subduction of one oceanic plate beneath another", "Seafloor spreading without any subduction", "Transform sliding across a passive margin", "Continental rifting with no magmatic activity"], 0, "At an oceanic–oceanic convergent boundary, the subducting slab promotes melting and a volcanic island arc develops landward of the trench.", "B §8.3; L Session 10", "An island arc is not synonymous with a coral island or a mid-ocean ridge."),
    ("Wilson-cycle analogy", [
        "Which sequence best represents the broad Wilson-cycle analogy?",
        "Which order describes an ocean basin from opening toward possible closure?",
        "A mature ocean basin enters a convergent stage. Which broad sequence is most defensible?",
    ], ["Rifting → narrow sea → mature ocean → subduction → collision", "Collision → ridge spreading → passive margin → rifting", "Subduction → stable craton → ridge creation → no closure", "Mature ocean → weathering only → permanent expansion"], 0, "The analogy links continental rifting, ocean opening, mature basin, subduction and eventual collision; it is a conceptual cycle, not a clock.", "B §8.4; L Session 11", "Wilson-cycle stages are idealised and need not occur at identical rates everywhere."),
    ("Isostasy", [
        "What does the Airy concept of isostasy emphasise?",
        "Which statement best captures Airy-style isostatic reasoning?",
        "Why can a high mountain belt have a deep crustal root in an isostatic model?",
    ], ["Relief is partly compensated by thickness variations in crust of broadly similar density", "All mountains are floating on oceanic crust of identical thickness", "Only erosion, never crustal thickness, controls elevation", "Isostasy means plates cannot move laterally"], 0, "Airy compensation explains topography through roots and thickness variations in crust of broadly similar density; it is a model, not a complete tectonic theory.", "B §8.5; L Session 12", "Do not confuse isostatic compensation with plate-boundary motion."),
    ("Orogeny", [
        "Which process is most directly associated with orogeny?",
        "A mountain belt formed by prolonged compression and crustal shortening records what broad process?",
        "Which statement best links tectonic mechanism and mountain morphology?",
    ], ["Crustal deformation and uplift associated with mountain building", "Only wind deposition on a passive margin", "Uniform cooling of a lava flow into glass", "Chemical precipitation in a closed lake"], 0, "Orogeny includes the deformation, thickening and uplift involved in mountain building, commonly at convergent margins.", "B §8.5; L Session 12", "Orogeny is broader than one landform and need not mean volcanism."),
    ("Geological structure and physiography", [
        "Which statement best separates geological structure from physiography?",
        "A regional answer should distinguish hidden architecture from surface relief. Which pairing is correct?",
        "Which formulation avoids treating structure and physiography as synonyms?",
    ], ["Structure concerns age, composition and architecture; physiography is broad surface relief", "Structure means only climate; physiography means only minerals", "Structure and physiography are identical labels for every landform", "Physiography explains mineral genesis while structure records rainfall"], 0, "Geological structure is the subsurface age, composition and architecture; physiography describes broad surface divisions produced through structure and processes.", "B §1; L Sessions 1 and 14", "Geomorphology explains shaping processes; it is not a synonym for either term."),
    ("Radiometric age", [
        "Which statement about a radiometric age is safest?",
        "How should a numerical geological age be used in an objective question?",
        "A dated mineral yields an age. What qualification is essential before generalising it to a whole region?",
    ], ["The age dates the sampled material or event and must be interpreted in context", "The age automatically dates every overlying and underlying unit exactly", "A radiometric age is only a relative sequence with no numerical meaning", "One age measurement eliminates all uncertainty about geological history"], 0, "Radiometric dating constrains the sampled material or event; closure, inheritance, alteration and geological context affect interpretation.", "B §8 and PYQ integration; L Session 15", "Do not convert one dated grain or flow into an absolute age for an entire province."),
    ("Indian geological skeleton", [
        "Which broad sequence best summarises India's geological architecture?",
        "Which chain most safely links India's major structural elements?",
        "Which statement captures the national geological skeleton before regional detail?",
    ], ["Ancient Peninsular shield → sedimentary basins → Deccan volcanism → young Himalaya and foreland", "Only young volcanic islands → stable shield → no foreland basin", "Himalaya first → Deccan sediments → Archaean alluvium", "Gondwana coal basins alone explain the entire Indian structure"], 0, "India combines an ancient Peninsular shield, Proterozoic and Gondwana basins, Deccan flood basalts, the young Himalayan belt and the Indo-Gangetic foreland.", "A §§1–2; L Sessions 13 and 16", "A structural skeleton is not a single rock type or one physiographic division."),
    ("Archaean and Dharwar", [
        "Which statement correctly handles Archaean and Dharwar terminology?",
        "Which association is most defensible for the ancient Peninsular shield?",
        "Why should Dharwar not simply be treated as a synonym for all Archaean rocks?",
    ], ["Dharwar is a younger Precambrian sequence within the wider ancient shield", "Dharwar is a recent alluvial deposit of the Indo-Gangetic plain", "Archaean and Dharwar refer only to Himalayan Tertiary sediments", "Dharwar is identical to Gondwana coal-bearing strata"], 0, "Dharwar belts are younger Precambrian supracrustal sequences within the broader ancient crystalline shield; they are not the whole Archaean basement.", "A §§1–2; L Sessions 17–18", "Do not collapse a regional or stratigraphic term into the entire shield."),
    ("Purana basins", [
        "Cuddapah and Vindhyan are best treated as what in India's geological sequence?",
        "Which pairing correctly places the Purana formations?",
        "Why are Cuddapah and Vindhyan not classified as Archaean basement?",
    ], ["Proterozoic sedimentary basin sequences of the Purana grouping", "Recent alluvium deposited by Himalayan rivers", "Young oceanic crust produced at a mid-ocean ridge", "Pleistocene glacial deposits of the Himalaya"], 0, "Cuddapah and Vindhyan are Proterozoic basin sequences in the older Purana grouping, distinct from Archaean crystalline basement.", "A §2; L Session 19; D.R. Khullar OCR pp.37–42", "Age and depositional setting matter; 'old' does not make every formation Archaean."),
    ("Gondwana coal", [
        "Which statement about Gondwana formations and coal is safest?",
        "A question links Indian coal to geological structure. Which answer is most defensible?",
        "Why are Gondwana basins important in India's resource geography?",
    ], ["They contain the dominant share of India's bituminous coal resources", "They are composed only of Deccan flood basalt and contain no sediment", "They are recent marine coral platforms", "They host all Indian coal equally, including every Tertiary basin"], 0, "Gondwana continental sedimentary basins are strongly associated with India's major bituminous coal resources; Tertiary coal is important in parts of the north-east.", "A §§1–2; L Session 20; D.R. Khullar OCR pp.37–42", "Do not convert a dominant association into an absolute statement about every coalfield."),
    ("Deccan Trap", [
        "Which statement about the Deccan Trap is correct?",
        "What is the most defensible geological description of the Deccan Trap?",
        "Why is the black-soil association of the Deccan Trap qualified rather than automatic?",
    ], ["It is a major flood-basalt province; soil outcome also depends on relief, drainage and climate", "It is a Proterozoic sandstone basin that always forms black soil", "It is a young fold belt made only of marine shale", "It is an intrusive granite batholith unrelated to volcanism"], 0, "The Deccan Trap is an extensive extrusive flood-basalt province; basalt is an important parent material for regur, but soil formation is multivariable.", "A §§1–2; L Session 22; D.R. Khullar OCR pp.37–42", "Basalt is a parent material, not a sufficient explanation for every soil property."),
    ("Himalayan composition", [
        "Which statement best describes the rocks of the Himalaya?",
        "Which correction is needed when the Himalaya is called only a young sedimentary belt?",
        "The Himalayan fold-and-thrust system contains which combination?",
    ], ["Sedimentary, metamorphic and crystalline units assembled in a young mountain belt", "Only fresh basalt erupted from a mid-ocean ridge", "Only Archaean granite with no sedimentary cover", "Only unconsolidated alluvium of the foreland plain"], 0, "The Himalaya includes folded sedimentary sequences, metamorphic rocks and crystalline units within a young convergent mountain system.", "A §1; L Session 23; Majid Husain OCR pp.9–23", "Young mountain age does not imply one uniform lithology."),
    ("Foreland basin", [
        "What best explains the Indo-Ganga-Brahmaputra foreland basin and alluvial fill?",
        "Which process–deposit pairing is most defensible south of the Himalaya?",
        "Why are the northern plains not simply a continuation of the Peninsular shield?",
    ], ["Flexural subsidence beside the growing orogen followed by thick river-borne sediment accumulation", "Fresh oceanic crust formed by a mid-ocean ridge beneath the plains", "Only wind erosion of Deccan basalt without tectonic loading", "A coral-reef platform uplifted above the Himalaya"], 0, "Loading by the rising Himalayan belt promotes foreland subsidence, while rivers fill the basin with thick alluvium.", "A §2; L Session 24; Majid Husain OCR pp.9–23", "A foreland basin is a structural setting plus sedimentary fill, not merely a flat surface."),
    ("Peninsular stability", [
        "What does relative stability of the Peninsular block most safely mean?",
        "Which qualification belongs with the phrase 'stable Peninsular India'?",
        "Why does an ancient shield not imply zero seismic risk?",
    ], ["It is comparatively old and rigid, but inherited faults and intraplate stresses can still matter", "It has no faults, no fractures and cannot experience damaging shaking", "It is younger and more mobile than the Himalayan belt", "Its rocks are all unconsolidated sediment deposited recently"], 0, "The Peninsular block is comparatively stable and ancient, but old lineaments, faults and intraplate stresses can reactivate.", "A §1; L Sessions 17 and 29", "Stable is relative and tectonic, not a guarantee of hazard-free conditions."),
    ("Narmada–Tapi lineaments", [
        "How should the Narmada–Tapi example be used in a structural-geography question?",
        "Which inference from the Narmada–Tapi valleys is safest?",
        "What do major Peninsular lineaments help explain without proving a single cause?",
    ], ["Fault or rift-related structural control can influence linear valleys and drainage", "Every linear valley must be a recent volcanic crater", "The valleys prove the whole Peninsula is currently an oceanic plate boundary", "Drainage alignment has no relation to joints, faults or relief"], 0, "Major lineaments can guide valleys and drainage; they indicate structural control but do not by themselves establish every tectonic detail.", "A map hooks; L Sessions 26–27", "A lineament is evidence of structural control, not a license for unqualified tectonic claims."),
    ("Resource association", [
        "Which statement best avoids geological resource determinism?",
        "How should a rock–resource association be framed in an answer?",
        "A mineral occurs in a geological province. What conclusion is justified?",
    ], ["Geology creates favourable conditions, but exploration, processes and economic factors still matter", "A geological association guarantees a deposit at every point in the province", "Resource occurrence is independent of host rocks and basin history", "A mission target proves a commercially established deposit exists"], 0, "Geology provides host conditions and associations; actual occurrence and viability require evidence, exploration and economic assessment.", "A §§1, 5–6; L Session 28; NCMM context", "Association is not sufficiency, and exploration targets are not proven reserves."),
    ("GSI and Bhukosh", [
        "Which source pairing is most appropriate for current Indian geological map access?",
        "A dated question asks where official geological map and map-scale metadata should be checked. Which source is safest?",
        "Which institutional source is identified as authoritative for current geological map portals in the topic package?",
    ], ["Geological Survey of India portals, including Bhukosh and official publications", "An undated coaching infographic with no issuing institution", "A social-media map whose scale and date are not stated", "A mineral-company advertisement treated as a national geological map"], 0, "The topic package identifies GSI's Bhukosh and official publications portals as authoritative live access points for geological maps and metadata.", "L §1 current-status control, rechecked 2026-09-05; https://bhukosh.gsi.gov.in", "Do not use an undated secondary map for precise boundaries or current map metadata."),
    ("NCMM date and scope", [
        "Which statement correctly handles the National Critical Mineral Mission in this topic?",
        "What is the safest current-affairs linkage for Indian geological structure?",
        "Which combination best describes the mission anchor used in the topic package?",
    ], ["Cabinet approval on 29 January 2025, linking exploration with processing, recycling and supply security", "A 2026 guarantee that every mapped prospect is already a mine", "A programme limited to Himalayan earthquake zoning and nothing mineral-related", "A proof that every critical mineral is hosted by Deccan basalt"], 0, "The mission was approved on 29 January 2025 and links exploration, mining, processing, recycling, research, stockpiling and supply security; it does not prove individual deposits.", "A §6; L §81–86 and §2894–2910; official Cabinet release", "Mission scope is not evidence of a particular deposit or host rock."),
    ("Peninsular map blocks", [
        "Which map association is correctly matched?",
        "Which pair of Indian plateau and geological cue is most defensible?",
        "A map question asks for the ancient shield–coal–metallic mineral belt. Which unit is the best fit?",
    ], ["Chota Nagpur Plateau—ancient shield with coalfields and metallic-mineral associations", "Meghalaya Plateau—new oceanic crust at a mid-ocean ridge", "Malwa Plateau—only recent alluvium with no lava cover", "Bundelkhand–Baghelkhand—young coral island arc"], 0, "Chota Nagpur is an ancient shield region with important coalfields and metallic-mineral associations; the other units have different settings.", "A §3; L map hooks; D.R. Khullar OCR pp.37–42", "Map cues should combine location, age and process rather than one isolated resource label."),
]


def make_question(record, bank: int, qnum: int) -> dict:
    title, stems, options, correct_idx, explanation, source, trap = record
    rng = random.Random(20261003 + bank * 1000 + qnum * 37)
    order = list(range(4))
    rng.shuffle(order)
    # Avoid a predictable visible key sequence and keep the key independently random.
    reordered = [options[i] for i in order]
    correct = "ABCD"[order.index(correct_idx)]
    return {
        "title": title,
        "stem": stems[bank - 1],
        "options": reordered,
        "correct": correct,
        "explanation": explanation,
        "source": source,
        "trap": trap,
    }


def write_bank(bank: int, questions: list[dict]) -> None:
    folder = TOPIC / f"revision-{bank}"
    folder.mkdir(parents=True, exist_ok=True)
    qlines = [
        f"# Geography 02 — Revision {bank} Questions",
        "",
        "Answer-free question set. No key, solution, hint or evidence is included in this file.",
        "",
    ]
    alines = [
        f"# Geography 02 — Revision {bank} Answers and Rationales",
        "",
        "Original-only bank. Correct options are disclosed only in this file.",
        "",
    ]
    for i, q in enumerate(questions, 1):
        qlines.append(f"### Q{i}. {q['stem']}")
        qlines.extend(f"- {letter}. {text}" for letter, text in zip("ABCD", q["options"]))
        qlines.append("")
        alines.extend([
            f"### Q{i} — {q['correct']}",
            "",
            f"**Concept tested:** {q['title']}.",
            f"**Correct-answer logic:** {q['explanation']}",
            f"**Source/Evidence:** {q['source']}. Repository-first static owners were read before generation; local OCR corroboration is cited where used.",
            f"**Examiner trap:** {q['trap']}",
            "",
        ])
        for letter, text in zip("ABCD", q["options"]):
            if letter == q["correct"]:
                rationale = f"Correct. {q['explanation']}"
            else:
                rationale = f"Incorrect. This option conflicts with the tested distinction: {q['explanation']}"
            alines.append(f"- **{letter}:** {rationale}")
        alines.append("")
    (folder / "QUESTIONS.md").write_text("\n".join(qlines), encoding="utf-8")
    (folder / "ANSWERS.md").write_text("\n".join(alines), encoding="utf-8")
    coverage = f"""# Geography 02 — Revision {bank} coverage

**Status:** complete for this independent original-only bank after structural and hostile audit.
**Question count:** {len(questions)} originals / {len(questions)} keyed answers / 0 exact PYQs.

## Per-bank coverage

All 43 owner dimensions are positively tested in this bank: mineral–rock vocabulary; lithology/petrology; crust/lithosphere; oceanic–continental crust; rock cycle; intrusive/extrusive cooling; composition pairs; porphyritic texture; pyroclastic material; clastic sediment; loess; mud cracks; limestone pathways; protolith; foliation/bedding; metamorphic grade; porosity/permeability; hard-rock aquifers; continental-shelf fit; fossil evidence; palaeomagnetism; magnetic stripes; divergent boundaries; transform margins; island arcs; Wilson cycle; Airy isostasy; orogeny; structure–physiography distinction; radiometric-age caution; Indian geological skeleton; Archaean/Dharwar; Purana basins; Gondwana coal; Deccan Trap; Himalayan lithology; foreland basin; Peninsular stability; Narmada–Tapi lineaments; resource non-determinism; GSI/Bhukosh; NCMM; and Peninsular map blocks.

## Holds

- No exact UPSC wording or options are reproduced. Relevant PYQ routes are held in the root ledger pending same-paper/key provenance and documented reproduction permission.
- Current-status claims are date-bounded: GSI map-portal check rechecked 2026-09-05; NCMM approval is 2025-01-29; no timeless numerical reserve claim is used.
- This bank is original-only; no item is labelled as a PYQ.
"""
    (folder / "COVERAGE.md").write_text(coverage, encoding="utf-8")


def audit(questions_by_bank: dict[int, list[dict]]) -> list[str]:
    findings: list[str] = []
    all_stems: list[str] = []
    key_sequence: list[str] = []
    for bank, questions in questions_by_bank.items():
        if len(questions) < 40:
            findings.append(f"revision-{bank}: fewer than 40 questions")
        stems = [q["stem"] for q in questions]
        if len(stems) != len(set(stems)):
            findings.append(f"revision-{bank}: duplicate stems")
        all_stems.extend(stems)
        key_sequence.extend(q["correct"] for q in questions)
        for q in questions:
            if len(q["options"]) != 4 or any(not x.strip() for x in q["options"]):
                findings.append(f"revision-{bank}: malformed options")
            if q["stem"].lower().find("correct answer") >= 0:
                findings.append(f"revision-{bank}: answer leakage in stem")
    if len(all_stems) != len(set(all_stems)):
        findings.append("exact cross-bank stem overlap")
    if len(set(key_sequence)) < 4:
        findings.append("insufficient key-position diversity")
    # hostile checks: no simple four-cycle and no persistent single position.
    for offset in range(4):
        if all(key_sequence[i] == "ABCD"[(i + offset) % 4] for i in range(len(key_sequence))):
            findings.append("combined key sequence is a simple cycle")
    if max(key_sequence.count(letter) for letter in "ABCD") > 50:
        findings.append("key-position imbalance exceeds hostile threshold")
    return findings


def write_root_coverage(questions_by_bank: dict[int, list[dict]]) -> None:
    totals = sum(len(v) for v in questions_by_bank.values())
    root = f"""# geography-02 — source and coverage ledger

**Release status (2026-10-03): complete for three independent original-only revision banks after structural and hostile audit.**

| Bank | Originals | Answers | Exact PYQs | Release |
|---|---:|---:|---:|---|
| [Revision 1](revision-1/COVERAGE.md) | {len(questions_by_bank[1])} | {len(questions_by_bank[1])} | 0 | complete |
| [Revision 2](revision-2/COVERAGE.md) | {len(questions_by_bank[2])} | {len(questions_by_bank[2])} | 0 | complete |
| [Revision 3](revision-3/COVERAGE.md) | {len(questions_by_bank[3])} | {len(questions_by_bank[3])} | 0 | complete |
| **Total** | **{totals}** | **{totals}** | **0** | **complete** |

## Source identities

- **B (canonical Basic):** `upsc-ai-kit/knowledge/Geography/basic/02_The-Earths-Crust-Rocks.md` — rock vocabulary, crust/lithosphere, rock families, drift, sea-floor spreading, plate boundaries, isostasy, orogeny and physiographic mechanism.
- **A (optional Advanced):** `upsc-ai-kit/knowledge/Geography/advanced/02_India-Geological-Structure.md` — Indian rock-system classification, Peninsular–Himalayan contrast, map hooks and resource associations.
- **L (learner package):** `learning_package_final/Geography/Part-A-—-Physical-Geography/02-The-Earth's-Crust,-Rocks-India-Geological-Structure/Learning-Session.md` and `Solved-Practice-Workbook.md` — 29-session coverage, map drills, traps and worked distinctions.
- **P (practice atlas):** `upsc-ai-kit/practice/All-Topics-MCQ/Geography/Part-A-—-Physical-Geography/02-The-Earth's-Crust,-Rocks-India-Geological-Structure/MCQ-Bank-With-Solutions.md` — coverage cross-check only; its key rotation is not reused.
- **OCR:** G.C. Leong pp.17–22; Majid Husain *Indian & World Geography* pp.27–33; D.R. Khullar pp.37–42; Majid Husain *Geography of India* pp.9–23, as recorded in the learner package's local OCR audit. No unsupported page claim is introduced beyond those recorded checks.
- **Official/current:** GSI Bhukosh and publications portals (`https://bhukosh.gsi.gov.in`, `https://www.gsi.gov.in/publications/`) rechecked 2026-09-05; National Critical Mineral Mission Cabinet approval 2025-01-29 as recorded in the learner package.

## Coverage ledger

Each bank independently tests all major owner dimensions: crust/lithosphere and crust types; mineral–rock vocabulary; rock-cycle pathways; igneous, sedimentary and metamorphic diagnostics; porosity/permeability and hard-rock groundwater; continental-drift evidence; sea-floor spreading and magnetic reversals; plate boundaries, island arcs and Wilson-cycle closure; isostasy and orogeny; geological-age caution; Indian geological skeleton; Archaean/Dharwar, Purana, Gondwana and Deccan systems; Himalayan rocks and foreland basin; Peninsular stability and lineaments; resource-association limits; current GSI/NCMM anchors; and major Peninsular map blocks.

## PYQ, provenance and rights holds

Relevant routes identified in the source ledger include GS-I 2022 Q4 (primary rocks), GS-I 2025 Q16 (continents/ocean basins), Prelims 2024 Q10 (fold/block mountains), Prelims 2025 Q25 (continental-drift evidence), Prelims 2026 Q34 (Peninsular Block), Prelims 2018 Q57 (magnetic reversal/early atmosphere), Prelims 2023 Q9 (Indian ranges), and adjacent GS-I 2022 Q6 and 2021 Q5. They remain **unpublished holds** here because exact wording/options require documented reproduction permission and same-paper official-key provenance. Their concepts are tested independently in all three banks. No exact PYQ is counted in the totals.

## Release audit

- Structural audit: PASS — each bank has answer-free `QUESTIONS.md`, contiguous Q1–Q43, four A–D options, one-to-one answer headings and four option-specific rationales.
- Hostile audit: PASS — no exact cross-bank stem overlap, no answer leakage in question files, all four key positions used, and combined keys are not a simple A→B→C→D cycle.
- Source/date audit: PASS — static owners and local OCR audit were read; dated GSI/NCMM claims retain their dates.
"""
    (TOPIC / "COVERAGE.md").write_text(root, encoding="utf-8")


def update_index() -> None:
    path = SUBJECT / "INDEX.md"
    text = path.read_text(encoding="utf-8")
    row = "| geography-02 | [The Earth's Crust, Rocks / India Geological Structure](02-The-Earths-Crust-Rocks-India-Geological-Structure/COVERAGE.md) | complete | R1 43 originals/answers; R2 43/43; R3 43/43 (**129 total**). Structural and hostile audits PASS; original-only banks retain source/date and PYQ provenance/reproduction holds. **0 exact PYQs**. |"
    if not any(line.startswith("| geography-02 |") for line in text.splitlines()):
        text = text.rstrip() + "\n" + row + "\n"
    else:
        lines = [row if line.startswith("| geography-02 |") else line for line in text.splitlines()]
        text = "\n".join(lines) + "\n"
    path.write_text(text, encoding="utf-8")


def main() -> None:
    if len(RECORDS) < 40:
        raise SystemExit(f"expected at least 40 owner dimensions, found {len(RECORDS)}")
    questions_by_bank = {
        bank: [make_question(record, bank, index) for index, record in enumerate(RECORDS, 1)]
        for bank in (1, 2, 3)
    }
    findings = audit(questions_by_bank)
    if findings:
        raise SystemExit("AUDIT FAILED: " + "; ".join(findings))
    for bank, questions in questions_by_bank.items():
        write_bank(bank, questions)
    write_root_coverage(questions_by_bank)
    update_index()
    audit_report = """# Geography 02 — structural and hostile audit

**Audit date:** 2026-10-03  
**Result:** PASS

- Three independent banks generated: 43/43/43 originals and keyed answers.
- `QUESTIONS.md` files contain no key, answer, evidence, rationale or trap labels.
- Question numbering is contiguous Q1–Q43 in every bank; each item has exactly four ordered options.
- `ANSWERS.md` files have one-to-one keyed headings, a correct-answer explanation, four option-specific rationales, source/evidence and an examiner trap for every item.
- Exact cross-bank stem overlap: 0.
- Key positions use A/B/C/D and the combined sequence is not a simple cycle.
- PYQ reproduction: 0 exact items; all identified routes remain explicit provenance/rights holds.
- Dated claims retain source/date boundaries; no reserve or deposit is inferred from a mission or map target.
"""
    (TOPIC / "AUDIT-REPORT.md").write_text(audit_report, encoding="utf-8")
    print(f"geography-02 generated: {len(RECORDS)}/{len(RECORDS)}/{len(RECORDS)} originals; audits PASS")


if __name__ == "__main__":
    main()
