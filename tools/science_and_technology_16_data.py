"""Authored learner-v2 data for Science and Technology Topic 16."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://dst.gov.in/scientific-programmes/mission-nano-science-and-"
        "technology-nano-mission - attempted 2026-09-04; direct retrieval "
        "returned only the official National Programme on Nano Science and "
        "Technology page title. No funding amount, project count, outcome, "
        "deployment or current programme-performance claim was imported."
    ),
    (
        "https://dst.gov.in/callforproposals/call-proposals-advanced-materials-"
        "under-npnst - attempted 2026-09-04; direct retrieval returned only "
        "the official advanced-materials call title. The owner's dated "
        "01-30 September 2024 call-window evidence was retained, but a closed "
        "call was not rewritten as an award, funded project or deployment."
    ),
    (
        "https://inst.ac.in/about-us - fetched 2026-09-04; substantive official "
        "text confirmed INST's DST-autonomous status, Nano Mission origin, "
        "1-100 nm definition, quantum/surface-area basis and research links "
        "to agriculture, healthcare, energy, environment, water and devices. "
        "Institutional aims were not converted into achieved performance."
    ),
    (
        "https://www.csir.res.in/en/csir-labs-unit - attempted 2026-09-04; "
        "retrieval exposed only a Central Electronics Engineering Research "
        "Institute title rather than a complete laboratory-network account. "
        "No laboratory output, product, approval or deployment was inferred."
    ),
    (
        "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2115965 - "
        "attempted 2026-09-04; direct retrieval returned HTTP 403. The owner's "
        "dated 27 March 2025 Nano Electronics Roadshow event reference was "
        "retained only as an event-held boundary, not proof of indigenous IP, "
        "startup success, fabrication capability or commercial deployment."
    ),
]


def _topic_16() -> dict[str, object]:
    facts = [
        (
            "Nanoscale and object boundary",
            "Nanotechnology deliberately studies, engineers and applies matter at about 1-100 nm, where size-dependent behaviour becomes functionally important; a nanoparticle has all three external dimensions in that range, a nanotube or nanofibre has two, and a nanosheet or nanoplate has one, while nanomaterial is the broader class.",
        ),
        (
            "Surface-area mechanism",
            "Shrinking a material raises its surface-area-to-volume ratio and the fraction of atoms at or near the surface, which can alter adsorption, catalytic activity, chemical reactivity and dissolution; greater reactivity is an application opportunity and a possible exposure concern, not an automatic performance or safety verdict.",
        ),
        (
            "Quantum-size mechanism",
            "At sufficiently small dimensions quantum confinement can change allowed electronic states, band gap, optical emission, conductivity or magnetic response; the effect depends on material and size, so every nanoscale material does not acquire the same property.",
        ),
        (
            "Top-down fabrication",
            "Top-down methods pattern or remove material from a bulk starting point through routes such as lithography, etching and milling; they can offer positional control but may introduce waste, defects or minimum-feature constraints, and a named method does not itself prove scalable manufacture.",
        ),
        (
            "Bottom-up fabrication",
            "Bottom-up methods assemble structures from atoms, molecules or precursors through routes such as self-assembly, sol-gel processing and chemical vapour deposition; they can exploit chemical control and parallel formation but still face nucleation, aggregation, uniformity, purification and scale-up challenges.",
        ),
        (
            "Carbon-form and nanoparticle distinction",
            "Nanoparticles are three-dimensionally nanoscale objects, carbon nanotubes are cylindrical carbon nanostructures, and graphene is a single-atom-thick hexagonal carbon sheet; related carbon chemistry does not make a particle, tube and sheet geometrically or functionally interchangeable.",
        ),
        (
            "Quantum-dot and nanocomposite distinction",
            "A quantum dot is a semiconductor nanocrystal with strongly size-dependent optical and electronic behaviour, whereas a nanocomposite uses a nanoscale phase to modify a bulk matrix; fullerenes, dendrimers and nanoemulsions are additional distinct families rather than synonyms for quantum dots.",
        ),
        (
            "Microscopy and structure characterization",
            "SEM commonly maps surface morphology, TEM can examine internal structure and nanoscale dimensions, AFM traces surface topography with a probe, and XRD helps identify crystalline phases and infer structural scale; each technique answers a different question and no single image establishes composition, dispersion, stability and safety.",
        ),
        (
            "Dispersion and surface characterization",
            "Dynamic light scattering estimates an ensemble hydrodynamic-size distribution in a dispersion, zeta potential is used as an indicator related to colloidal stability, and spectroscopy or surface analysis can examine composition and functionalisation; measured size can differ by method because physical, hydrodynamic and aggregated states differ.",
        ),
        (
            "Nanomedicine delivery boundary",
            "Nanocarriers such as liposomes, polymeric particles or dendrimer-like systems can protect cargo, alter circulation, control release or use passive and ligand-mediated targeting, but delivery to a tissue is not proof of cellular uptake, therapeutic superiority, approval, clinical adoption or long-term safety.",
        ),
        (
            "Agricultural application map",
            "Agricultural nanotechnology includes nano-fertilisers, nano-formulated crop-protection inputs, controlled-release carriers, nano-sensors, seed coatings or nano-priming, water treatment and post-harvest coatings or packaging; each application needs crop-, formulation-, dose- and field-specific evidence.",
        ),
        (
            "Farmer-uplift and product-status boundary",
            "Possible farmer benefits run through input-use efficiency, lower handling burden, earlier stress detection, reduced spoilage and better net realisation, but affordability, credit, extension, device access, residue testing and field efficacy determine distribution; the owner records nano urea and nano DAP as FCO-notified marketed products, which is not proof of yield equivalence, universal safety or socio-economic uplift.",
        ),
        (
            "Water and environmental application",
            "Nano-enabled membranes, adsorbents, photocatalysts and sensors can support filtration, contaminant capture, degradation or detection, but laboratory removal efficiency must not be converted into field deployment because fouling, selectivity, regeneration, energy use, spent-material recovery and secondary release remain system questions.",
        ),
        (
            "Electronics energy and materials application",
            "Graphene, carbon nanotubes, quantum dots and nanocomposites are studied for sensors, flexible electronics, coatings, catalysts, electrodes, batteries, supercapacitors, solar interfaces and high-strength lightweight materials; a favourable material property is not equivalent to a certified device, manufacturable process or commercial product.",
        ),
        (
            "Indian institution and programme boundary",
            "DST's National Programme on Nano Science and Technology, earlier Nano Mission, supplies a public R&D architecture; INST Mohali is a DST autonomous institution established under that umbrella, while CSIR laboratories and MeitY-linked nanoelectronics efforts form cross-institutional capability routes. A live page, call or event proves activity or institutional continuity, not outcomes.",
        ),
        (
            "Nanotoxicology boundary",
            "Nanotoxicology evaluates biological effects through material-specific variables including size, shape, surface chemistry, coating, solubility, aggregation, dose and exposure route; inhalation, ingestion, dermal, occupational and medical exposure cannot be collapsed into one universal safe-or-toxic label.",
        ),
        (
            "Ecotoxicology and lifecycle boundary",
            "Ecotoxicity assessment follows release during production, use and disposal and examines transformation, dissolution, persistence, mobility, food-web transfer and bioaccumulation across soil, water and organisms; natural occurrence or a smaller material dose does not establish environmental harmlessness.",
        ),
        (
            "Regulation standards and metrology boundary",
            "Nano-enabled products remain subject to their relevant chemical, food, fertiliser, medical-device, drug, consumer-product or environmental routes, while nanospecific standards, reference materials, metrology, labelling, test protocols and lifecycle evidence may still be needed; research permission, standardisation, product notification and market approval are distinct decisions.",
        ),
        (
            "Evidence and status ladder",
            "Material synthesis, characterization, laboratory function, animal or greenhouse study, field or clinical study, regulatory review, product notification or approval, manufacture, marketing, adoption and monitored outcome are separate evidence rungs; no earlier rung establishes the later ones without a dated responsible authority.",
        ),
        (
            "Cross-topic and additive-manufacturing boundary",
            "Nanoelectronics connects this topic to semiconductors and quantum devices, advanced nanomaterials connect it to critical-mineral and manufacturing strategy, and nanosensors connect it to AI-enabled systems; 3D printing is additive manufacturing from a digital model and is not intrinsically nanotechnology merely because nano-enabled feedstocks can sometimes be used.",
        ),
    ]
    traps = [
        "Do not define nanotechnology as miniaturisation without the 1-100 nm and property-change boundary.",
        "Do not turn high surface area into automatic efficiency or harmlessness.",
        "Do not claim every nanomaterial exhibits the same quantum effect.",
        "Do not merge top-down removal with bottom-up assembly.",
        "Do not call graphene, carbon nanotubes, nanoparticles and quantum dots the same object.",
        "Do not use one microscopy image as complete material characterization.",
        "Do not treat hydrodynamic size, physical diameter and aggregate size as interchangeable.",
        "Do not convert targeted delivery into approved or superior therapy.",
        "Do not convert nano-input notification or marketing into proven yield or farmer-income gains.",
        "Do not convert laboratory contaminant removal into field deployment.",
        "Do not convert a material property into device certification or commercial manufacture.",
        "Do not generalise one toxicity result across materials, coatings, doses or exposure routes.",
        "Do not infer environmental safety from natural occurrence or lower mass alone.",
        "Do not merge research, standards, notification, approval, marketing, adoption and outcome.",
        "Do not classify all 3D printing as nanotechnology.",
    ]
    titles = [
        "Nanoscale definition nano-objects and surface-area effects",
        "Quantum confinement and size-dependent properties",
        "Top-down lithography etching and milling routes",
        "Bottom-up self-assembly sol-gel and deposition routes",
        "Nanoparticles nanotubes graphene and geometry",
        "Quantum dots nanocomposites and microscopy characterization",
        "Dispersion surface chemistry and measurement boundaries",
        "Nanomedicine carriers targeting and delivery evidence",
        "Agricultural nano-inputs sensors and controlled release",
        "Farmer socio-economic pathways and product-status boundaries",
        "Water environment electronics energy and advanced materials",
        "DST NPNST INST CSIR and nanoelectronics architecture",
        "Nanotoxicology dose material and exposure pathways",
        "Ecotoxicology lifecycle regulation standards and metrology",
        "Evidence ladder cross-topic routes and PYQ synthesis",
    ]
    routes = [
        "Define the scale, classify the nano-object and trace the surface mechanism before naming an application.",
        "Explain confinement as material- and size-dependent rather than a universal nanoscale effect.",
        "Trace bulk-patterning steps and qualify precision with waste, defect and scale limits.",
        "Trace atomic or molecular assembly and qualify it with uniformity, purification and aggregation.",
        "Classify each morphology before linking geometry to a possible property or use.",
        "Separate optical nanocrystals, bulk-matrix modification and technique-specific characterization.",
        "Name what each measurement observes and preserve physical-versus-hydrodynamic size distinctions.",
        "Move from carrier function to biological barrier, evidence rung, regulation and safety qualification.",
        "Organise agriculture by delivery, sensing, seed, water and post-harvest mechanisms.",
        "Build the farmer chain from field evidence and cost to extension, access and net realisation.",
        "Link property to system application, then test regeneration, integration, certification and lifecycle.",
        "Map DST, INST, CSIR and MeitY-linked roles without turning activity into demonstrated capability.",
        "Assess hazard and exposure through material, dose, route and susceptible-system variables.",
        "Follow the particle lifecycle and separate sectoral regulation, standards, metrology and approval.",
        "Decode the routed PYQ, use the evidence ladder and conclude without technology determinism.",
    ]
    panels = [
        panel("Nanoscale taxonomy and property gateway", "branch-map", [
            "1-100 nm -> functional size-dependent behaviour",
            "3 NANOSCALE DIMENSIONS -> nanoparticle",
            "2 NANOSCALE DIMENSIONS -> nanotube / nanofibre",
            "1 NANOSCALE DIMENSION -> nanosheet / nanoplate",
            "GATEWAY -> surface-area effect + possible quantum effect",
        ], [facts[0][0], facts[1][0], facts[2][0]]),
        panel("Surface-area and quantum twin engine", "dual-mechanism", [
            "SMALLER SIZE -> larger relative surface -> adsorption / catalysis / reactivity",
            "SUFFICIENT CONFINEMENT -> altered states / band gap -> optical or electronic shift",
            "MATERIAL + SIZE + SURFACE CHEMISTRY -> actual behaviour",
            "TRAP -> nano is neither an automatic benefit nor safety verdict",
        ], [facts[1][0], facts[2][0]]),
        panel("Fabrication route comparison", "comparison-table", [
            "TOP-DOWN -> bulk -> lithography / etching / milling -> patterned structure",
            "BOTTOM-UP -> atoms / molecules -> self-assembly / sol-gel / CVD -> formed structure",
            "TOP-DOWN LIMIT -> waste / defects / feature constraint",
            "BOTTOM-UP LIMIT -> aggregation / uniformity / purification",
            "COMMON TEST -> reproducibility and scale-up",
        ], [facts[3][0], facts[4][0]]),
        panel("Nanomaterial geometry atlas", "morphology-atlas", [
            "PARTICLE -> three nanoscale external dimensions",
            "CNT -> cylindrical carbon nanostructure",
            "GRAPHENE -> single-atom-thick hexagonal carbon sheet",
            "QUANTUM DOT -> size-tunable semiconductor nanocrystal",
            "NANOCOMPOSITE -> nanoscale phase modifies bulk matrix",
        ], [facts[5][0], facts[6][0]]),
        panel("Characterization decision tree", "decision-tree", [
            "SURFACE MORPHOLOGY? -> SEM",
            "INTERNAL STRUCTURE / NANOSCALE DIMENSION? -> TEM",
            "PROBE-TRACED TOPOGRAPHY? -> AFM",
            "CRYSTALLINE PHASE? -> XRD",
            "DISPERSION SIZE / STABILITY? -> DLS + zeta potential",
        ], [facts[7][0], facts[8][0]]),
        panel("Nanomedicine barrier rail", "barrier-rail", [
            "CARGO -> encapsulation / protection",
            "CARRIER -> circulation and release profile",
            "TARGETING -> passive accumulation or ligand interaction",
            "BIOLOGICAL BARRIERS -> tissue -> cell -> intracellular site",
            "STATUS -> delivery evidence != approval / superiority / safety",
        ], [facts[9][0]]),
        panel("Agriculture value chain", "farm-value-chain", [
            "NANO-INPUT / SENSOR / SEED COATING -> farm decision or delivery",
            "FIELD EVIDENCE -> dose, crop, soil, weather and formulation",
            "COST + EXTENSION + CREDIT -> adoption boundary",
            "INPUT LOSS / SPOILAGE / STRESS DETECTION -> possible income channel",
            "VERDICT -> socio-economic uplift must be demonstrated",
        ], [facts[10][0], facts[11][0]]),
        panel("Water and environment treatment loop", "treatment-loop", [
            "CONTAMINANT -> detection / adsorption / membrane / photocatalysis",
            "SYSTEM TEST -> selectivity + fouling + energy",
            "RECOVERY -> regeneration or spent-material capture",
            "LIFECYCLE CHECK -> secondary nanoparticle release",
            "BOUNDARY -> lab removal != field deployment",
        ], [facts[12][0], facts[16][0]]),
        panel("Electronics energy materials matrix", "application-matrix", [
            "GRAPHENE / CNT -> conductive and structural research",
            "QUANTUM DOT -> optical / display / sensing research",
            "NANOCOMPOSITE -> coatings and lightweight-strength modification",
            "NANOSTRUCTURED ELECTRODE -> storage and conversion interfaces",
            "BOUNDARY -> property != certified manufacturable product",
        ], [facts[13][0], facts[19][0]]),
        panel("Indian nano institution map", "institution-map", [
            "DST NPNST / EARLIER NANO MISSION -> public R&D architecture",
            "INST MOHALI -> DST autonomous nanoscience institution",
            "CSIR LABS -> cross-sector translational capability route",
            "MeitY-LINKED NANOELECTRONICS -> device / semiconductor bridge",
            "FIREWALL -> page / call / event != programme outcome",
        ], [facts[14][0]]),
        panel("Toxicity and ecotoxicity exposure web", "exposure-web", [
            "MATERIAL -> size + shape + coating + solubility + aggregation",
            "EXPOSURE -> dose + route + duration + susceptible system",
            "ENVIRONMENT -> transformation + mobility + persistence",
            "ECOLOGY -> organism effects + food-web transfer + bioaccumulation",
            "RULE -> material- and use-specific evidence",
        ], [facts[15][0], facts[16][0]]),
        panel("Regulatory and evidence status ladder", "status-ladder", [
            "SYNTHESIS -> CHARACTERIZATION -> LAB FUNCTION",
            "ANIMAL / GREENHOUSE -> FIELD / CLINICAL STUDY",
            "SECTORAL REVIEW -> STANDARD / NOTIFICATION / APPROVAL",
            "MANUFACTURE -> MARKETING -> ADOPTION",
            "MONITORED OUTCOME -> only dated evidence supports this rung",
        ], [facts[17][0], facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2025", "GS-III",
            "Discuss how nanotechnology offers significant advancements in agriculture and how it can help uplift farmers' socio-economic status.",
            "Verified routed Q15 demand, 15 marks and 250 words; the route covers delivery, sensing, seed, water and post-harvest uses, then tests field evidence, affordability, extension, toxicity and distribution. No official model answer is claimed.",
            [1, 10, 11, 15, 16, 17, 18],
        ),
        common.make_pyq_solution(
            facts, "2020", "GS-III",
            "Explain the concept of nanotechnology and describe its applications in the health sector.",
            "Verified routed Mains demand, 10 marks and 150 words; the route defines nanoscale property change and evaluates nanocarriers, diagnostics and evidence boundaries without claiming clinical approval or superiority.",
            [0, 1, 2, 5, 6, 9, 15, 18],
        ),
        common.make_pyq_solution(
            facts, "2018 / 2020 / 2022", "Prelims GS-I",
            "Assess the routed objective concepts concerning 3D-printing applications, carbon-nanotube uses and nanoparticles' natural occurrence, cosmetics use and safety.",
            "Representative composite card for 2018 Q84, 2020 Q41 and 2022 Q98; official keys are unavailable locally, so it supplies concept and close-option boundaries without an option verdict or answer letter.",
            [0, 5, 9, 13, 15, 16, 19],
        ),
    ]
    return common.topic(
        16,
        "Nanotechnology and Applications",
        "16_Nanotechnology-and-Applications",
        facts,
        traps,
        [
            (10, "Explain why materials can behave differently at the nanoscale.", [0, 1, 2]),
            (10, "Distinguish top-down and bottom-up nanomaterial fabrication methods.", [3, 4]),
            (15, "Classify major nanomaterial forms and explain how they are characterized.", [5, 6, 7, 8]),
            (15, "Examine nanomedicine and nano-enabled water treatment with their evidence and safety boundaries.", [9, 12, 15, 16, 18]),
            (20, "Discuss nanotechnology's agricultural advances and its conditional pathway to farmers' socio-economic uplift.", [1, 10, 11, 15, 16, 17, 18]),
            (20, "Evaluate India's nanotechnology ecosystem across institutions, electronics, materials, regulation, metrology and lifecycle governance.", [13, 14, 15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "1-100 nm", "nanoparticle", "nanotube", "nanosheet",
            "surface-area-to-volume ratio", "quantum confinement",
            "top-down", "bottom-up", "lithography", "etching", "milling",
            "self-assembly", "sol-gel", "chemical vapour deposition",
            "carbon nanotube", "graphene", "quantum dot", "nanocomposite",
            "fullerene", "dendrimer", "nanoemulsion", "SEM", "TEM", "AFM",
            "XRD", "dynamic light scattering", "zeta potential",
            "nanocarrier", "targeted delivery", "nano-fertiliser",
            "nano-sensor", "controlled release", "nano-priming",
            "adsorbent", "photocatalyst", "nanoelectronics",
            "nanotoxicology", "ecotoxicity", "bioaccumulation",
            "lifecycle", "metrology", "labelling", "NPNST", "INST",
            "Fertiliser (Control) Order", "3D printing",
        ],
        "Audited ledgers route the 2025 GS-III agriculture-and-farmer demand, the 2020 GS-III health-sector demand, and the 2018, 2020 and 2022 objective concepts on additive manufacturing, carbon nanotubes and nanoparticle occurrence, use and safety. Three representative cards preserve those routes; no objective answer key or option letter is supplied.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source attempts on 2026-09-04 confirmed INST's institutional and 1-100 nm conceptual account while preserving strict boundaries for DST programme pages, the closed 2024 call, the 2025 nanoelectronics event and sector-specific product status. No funding, efficacy, approval, deployment, adoption, safety or farmer-income conclusion was inferred.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
            "basic/10_National-Quantum-Mission-and-Quantum-Tech.md",
            "basic/11_Semiconductor-Mission-and-Electronics-Manufacturing.md",
            "basic/20_Emerging-Materials-Rare-Earths-and-Critical-Minerals.md",
        ],
        register_headings=(
            "NANOSCALE PROPERTY, FABRICATION AND MATERIAL-FORM MAP",
            "CHARACTERIZATION, APPLICATION AND EXPOSURE FIREWALLS",
            "AGRICULTURE, HEALTH, WATER AND ADVANCED-MATERIAL ANSWER SPINE",
            "INDIAN INSTITUTIONS, REGULATION, PYQ ROUTES AND STATUS LADDER",
        ),
        register_answer_spine=[
            "DEFINE 1-100 NM AND CLASSIFY PARTICLE TUBE SHEET DOT AND COMPOSITE",
            "TRACE SURFACE-AREA AND QUANTUM-CONFINEMENT PROPERTY CHANGES",
            "COMPARE TOP-DOWN WITH BOTTOM-UP FABRICATION AND SCALE-UP LIMITS",
            "MATCH SEM TEM AFM XRD DLS AND ZETA POTENTIAL TO THE QUESTION MEASURED",
            "ROUTE APPLICATIONS THROUGH MEDICINE AGRICULTURE WATER ELECTRONICS ENERGY AND MATERIALS",
            "MAP DST NPNST INST CSIR AND MeitY-LINKED NANOELECTRONICS WITHOUT OUTCOME INFERENCE",
            "TEST SIZE SHAPE COATING DOSE ROUTE PERSISTENCE BIOACCUMULATION AND LIFECYCLE RELEASE",
            "SEPARATE LAB RESULT FIELD OR CLINICAL EVIDENCE NOTIFICATION APPROVAL MARKETING ADOPTION AND OUTCOME",
            "CONCLUDE WITH MATERIAL-SPECIFIC TESTING METROLOGY LABELLING MONITORING ACCESS AND AFFORDABILITY",
        ],
    )


TOPIC_16 = _topic_16()
