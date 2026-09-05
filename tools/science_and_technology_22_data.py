"""Authored learner-v2 data for Science and Technology Topic 22."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.nobelprize.org/prizes/chemistry/2024/press-release/ - "
        "fetched 2026-09-04; substantive official text confirmed that the "
        "2024 Chemistry prize concerned computational protein design and "
        "protein-structure prediction. It was used only as a biomolecule and "
        "functional-structure linkage, not to infer a medical, commercial or "
        "regulatory outcome."
    ),
    (
        "https://mnre.gov.in/en/national-green-hydrogen-mission/ - fetched "
        "2026-09-04; substantive official text confirmed mission components "
        "for regulations and standards, infrastructure and a public-private "
        "R&D framework. It was used only to anchor electrolysis, catalysis and "
        "industrial electrochemistry; no hydrogen output, cost, emissions "
        "saving or deployment result was inferred."
    ),
    (
        "https://www.unep.org/inc-plastic-pollution/session-5/documents - "
        "fetched 2026-09-04; the official page exposed INC-5 agenda, scenario "
        "and draft-text documents for an international legally binding "
        "instrument on plastic pollution. Document availability was not "
        "rewritten as an agreed treaty, binding obligation, chemical ban or "
        "national regulatory status."
    ),
]


def _topic_22() -> dict[str, object]:
    facts = [
        (
            "Atomic identity and isotope boundary",
            "An atom contains protons and neutrons in its nucleus and electrons outside it; atomic number is the proton count that fixes elemental identity, mass number is protons plus neutrons, isotopes share atomic number but differ in mass number, isobars share mass number but differ in atomic number, and isotones share neutron number.",
        ),
        (
            "Periodic trends and qualified comparison",
            "The modern periodic table is ordered by atomic number; across a period atomic size generally decreases while ionisation energy and electronegativity generally increase and metallic character generally decreases, whereas down a group atomic size generally increases. These are trends with contextual exceptions, not licence to rank every pair without electronic-structure evidence.",
        ),
        (
            "Ionic covalent metallic and intermolecular distinction",
            "Ionic bonding arises from electron transfer and attraction between oppositely charged ions, covalent bonding from shared electron pairs, and metallic bonding from positive metal centres with delocalised electrons; hydrogen bonding and van der Waals forces are intermolecular or interparticle attractions and must not be relabelled as the primary bond inside every substance.",
        ),
        (
            "Mole and stoichiometric accounting",
            "The mole is the amount-of-substance unit used to connect chemical entities with measurable mass; stoichiometry follows a balanced equation to relate reactants and products, the limiting reagent caps the theoretical product, and percentage yield compares actual with theoretical yield. No numerical constant, purity or yield may be assumed unless the question supplies it.",
        ),
        (
            "States phase change and intermolecular forces",
            "Solid, liquid and gas differ in particle arrangement, mobility and separation; melting, freezing, vaporisation, condensation and sublimation are physical changes of state, while stronger intermolecular attraction generally raises the energy needed for separation. A phase change does not by itself create a new chemical substance.",
        ),
        (
            "Solutions concentration and solubility boundary",
            "A solution contains solute dispersed at the molecular or ionic scale in a solvent; concentration describes how much solute is present by a stated basis such as amount, mass, volume or proportion, whereas solubility is the equilibrium limit under specified conditions. Dilute is not synonymous with weak, and concentrated is not synonymous with strong.",
        ),
        (
            "Acids bases neutralisation and pH",
            "An acid can donate protons and a base can accept them, while the aqueous school-level definitions refer to hydrogen and hydroxide ions; pH is logarithmic and tracks hydrogen-ion activity, neutralisation reduces acidic and basic character and often forms salt and water, and acid strength must be kept separate from concentration.",
        ),
        (
            "Buffers salts and neutral-point boundary",
            "A buffer resists pH change when limited acid or base is added, salts may produce acidic, basic or neutral solutions depending on their constituent ions, and neutral pH is not universally fixed at the familiar school value because water self-ionisation varies with temperature. A buffer resists change; it does not make pH immutable.",
        ),
        (
            "Oxidation reduction and electrochemical cells",
            "Oxidation is electron loss or an increase in oxidation number and reduction is electron gain or a decrease; the paired half-processes can convert chemical energy to electrical energy in a galvanic or voltaic cell, while an electrolytic cell uses electrical energy to drive a non-spontaneous chemical change. Electrode signs depend on cell type, but oxidation remains at the anode and reduction at the cathode.",
        ),
        (
            "Reaction rate catalyst and equilibrium boundary",
            "Reaction rate depends on effective collisions and can change with concentration, temperature, surface area and catalysts; a catalyst provides a lower-activation-energy pathway and speeds forward and reverse reactions without shifting the equilibrium position. Equilibrium is dynamic equality of forward and reverse rates, not cessation of molecular change.",
        ),
        (
            "Organic functional-group classification",
            "A functional group is the reactive structural feature used to classify organic compounds, including alcohol, aldehyde, ketone, carboxylic-acid, amine and ester families; compounds sharing a functional group can show related reaction patterns, but a label alone does not establish exposure, toxicity, biodegradability or regulatory status.",
        ),
        (
            "Polymer structure and processing classes",
            "Polymers are macromolecules built from repeating units; addition polymerisation joins monomers without eliminating a small molecule, condensation polymerisation forms links while eliminating a small molecule, thermoplastics soften on reheating, and thermosets form networks that do not simply remelt. Biodegradable and compostable remain condition-dependent categories.",
        ),
        (
            "Carbon allotropes alloys and material properties",
            "Diamond, graphite, graphene, fullerenes and carbon nanotubes are carbon allotropes whose different structures produce different properties; an alloy combines a metal with other elements to alter strength, corrosion resistance or workability. Material performance follows structure and processing, not element name alone.",
        ),
        (
            "Fuels combustion and gasification boundary",
            "Combustion is oxidation that releases energy, whereas gasification converts a carbonaceous feedstock under controlled conditions into a gas mixture that can include carbon monoxide and hydrogen; complete and incomplete combustion, calorific usefulness, pollutants and lifecycle burden are separate evaluative axes. Gasification must not be presented as ordinary burning or as automatically clean.",
        ),
        (
            "Environmental chemistry compartment map",
            "Stratospheric ozone absorbs harmful ultraviolet radiation while ground-level ozone is a secondary pollutant; greenhouse gases, ozone-depleting substances, acids, nutrients and persistent chemicals operate through different atmospheric, water or soil mechanisms. The same molecule can have different significance by location, concentration, exposure and reaction pathway.",
        ),
        (
            "Measurement exposure and category firewall",
            "pH, concentration, oxidation number, reaction rate, yield, dose, exposure, persistence and emission are different measurements or categories; labels such as natural, organic, biodegradable, antimicrobial, fuel, solvent or pollutant do not independently prove safety, hazard, performance or legal status. State the measured quantity, basis, conditions and evidence boundary.",
        ),
        (
            "Hydrogel polymer-network route",
            "A hydrogel is a cross-linked hydrophilic polymer network that absorbs and retains water; routed applications include dressings, contact lenses, controlled release and water-management contexts. It is neither merely a liquid nor a universal water-purification material, and an application category does not prove performance in every formulation.",
        ),
        (
            "Water polarity BPA and triclosan boundaries",
            "Water's molecular polarity supports dissolution of many ionic and polar substances but does not make it a literal universal solvent; bisphenol A is associated with manufacture of some polycarbonate and epoxy materials, while triclosan is a synthetic antimicrobial used in some personal-care products. Presence, exposure, product coverage, safety and regulation require separate dated evidence.",
        ),
        (
            "Coal-gasification routed product boundary",
            "Coal gasification uses controlled reaction with oxygen or steam to produce synthesis gas chiefly containing carbon monoxide and hydrogen, with composition and by-products dependent on process and feedstock. A possible product stream is not evidence of plant efficiency, carbon capture, commercial viability or lower lifecycle emissions.",
        ),
        (
            "Chemistry-to-policy evidence ladder",
            "Atomic or molecular principle leads to material property, then process choice, industrial system, application and governance consequence; CSIR-NCL, CSIR-CECRI and the metallurgical research ecosystem illustrate distinct chemistry, electrochemistry and materials roles. A research mandate, mission page, negotiating document or named application does not prove deployment, outcome, hazard or regulation.",
        ),
    ]
    traps = [
        "Do not merge atomic number, mass number, isotopes, isobars and isotones.",
        "Do not turn periodic trends into exception-free rankings.",
        "Do not confuse primary chemical bonds with intermolecular forces.",
        "Do not perform stoichiometry without a balanced equation and limiting-reagent check.",
        "Do not call every phase change a chemical reaction.",
        "Do not equate concentration with solubility or acid strength.",
        "Do not treat strong and concentrated acids as synonyms.",
        "Do not claim a buffer fixes pH permanently or every salt is neutral.",
        "Do not reverse oxidation and reduction or assume electrode signs are identical in every cell.",
        "Do not claim a catalyst changes the equilibrium position or is necessarily consumed.",
        "Do not infer hazard or regulation from an organic functional-group name.",
        "Do not merge addition, condensation, thermoplastic, thermoset and biodegradable categories.",
        "Do not explain allotrope properties by different elemental composition.",
        "Do not equate gasification with combustion or with a zero-emission fuel pathway.",
        "Do not call ozone uniformly beneficial or uniformly harmful without its atmospheric compartment.",
    ]
    titles = [
        "Atomic structure isotopes and periodic trends",
        "Ionic covalent metallic bonding and force hierarchy",
        "Mole concept balanced equations and limiting reagent",
        "States of matter phase change and intermolecular forces",
        "Solutions concentration dilution and solubility",
        "Acids bases pH buffers salts and neutralisation",
        "Redox bookkeeping galvanic cells and electrolysis",
        "Reaction rate activation energy catalysis and equilibrium",
        "Organic functional groups and classification limits",
        "Polymerisation thermoplastics thermosets and hydrogels",
        "Carbon materials alloys fuels and combustion",
        "Environmental chemistry ozone gases nutrients and pollutants",
        "Measurement exposure product labels and safety boundaries",
        "Routed water BPA triclosan and hydrogel distinctions",
        "Coal gasification institutions PYQs and evidence ladder",
    ]
    routes = [
        "Fix particle identity and electron-pattern trends before predicting chemical behaviour.",
        "Classify electron transfer, electron sharing, delocalisation and weaker attractions separately.",
        "Balance first, identify the limiting reagent and state every supplied basis before calculating.",
        "Trace particle arrangement and energy change without converting a physical transition into a reaction.",
        "Name solvent, solute, concentration basis, conditions and saturation status.",
        "Separate strength, concentration, pH, neutralisation, salt hydrolysis and buffer action.",
        "Track oxidation numbers and half-processes, then identify the energy-conversion direction.",
        "Separate kinetic speed from thermodynamic equilibrium and explain what a catalyst can and cannot change.",
        "Use functional groups to classify reactivity while withholding unsupported hazard and legal claims.",
        "Classify polymer formation, reheating behaviour, network structure and condition-dependent degradation.",
        "Connect structure to material property, then distinguish combustion from gasification and lifecycle appraisal.",
        "Locate the chemical in atmosphere, water or soil before judging its environmental role.",
        "State quantity, unit or category, conditions, exposure route and last verified evidence rung.",
        "Route each objective demand to the exact molecular or polymer distinction without supplying an answer key.",
        "Move from chemical principle to process, application, institution and qualified policy conclusion.",
    ]
    panels = [
        panel("Atom and periodic identity map", "nested-hierarchy", [
            "NUCLEUS -> protons + neutrons",
            "ATOMIC NUMBER -> protons -> element identity",
            "MASS NUMBER -> protons + neutrons",
            "ISOTOPE / ISOBAR / ISOTONE -> different comparison axes",
            "PERIODIC TABLE -> atomic number + recurring properties",
        ], [facts[0][0], facts[1][0]]),
        panel("Bond and force ladder", "ranked-ladder", [
            "IONIC -> electron transfer + ion attraction",
            "COVALENT -> shared electron pair",
            "METALLIC -> delocalised electrons",
            "HYDROGEN BOND / VAN DER WAALS -> weaker interparticle forces",
            "TRAP -> do not collapse bond and force categories",
        ], [facts[2][0]]),
        panel("Stoichiometric accounting rail", "process-flow", [
            "WRITE SPECIES -> BALANCE EQUATION",
            "CONVERT SUPPLIED QUANTITIES -> MOLES",
            "COMPARE STOICHIOMETRIC REQUIREMENT",
            "IDENTIFY LIMITING REAGENT -> THEORETICAL PRODUCT",
            "ACTUAL / THEORETICAL -> YIELD, only with supplied data",
        ], [facts[3][0]]),
        panel("State and solution matrix", "comparison-table", [
            "SOLID / LIQUID / GAS -> arrangement + mobility + separation",
            "PHASE CHANGE -> physical identity retained",
            "SOLUTION -> molecular/ionic dispersion",
            "CONCENTRATION -> amount on a stated basis",
            "SOLUBILITY -> equilibrium limit under stated conditions",
        ], [facts[4][0], facts[5][0]]),
        panel("Acid base buffer control loop", "feedback-loop", [
            "ACID DONATES H+ <-> BASE ACCEPTS H+",
            "pH -> logarithmic activity measure",
            "NEUTRALISATION -> acidic/basic character reduced",
            "BUFFER -> consumes limited added acid/base",
            "SALT SOLUTION -> acidic / basic / neutral depends on ions",
        ], [facts[6][0], facts[7][0]]),
        panel("Electrochemical two-cell map", "split-path", [
            "OXIDATION -> anode | REDUCTION -> cathode",
            "GALVANIC CELL -> chemical energy to electrical energy",
            "ELECTROLYTIC CELL -> electrical energy drives chemistry",
            "CORROSION / PLATING / EXTRACTION -> applied routes",
            "SIGN TRAP -> cell type changes signs, not reaction locations",
        ], [facts[8][0]]),
        panel("Kinetics versus equilibrium", "two-axis-map", [
            "RATE AXIS -> collisions + activation energy",
            "CATALYST -> alternative lower-energy pathway",
            "EQUILIBRIUM AXIS -> forward rate equals reverse rate",
            "CATALYST -> faster approach in both directions",
            "NO SHIFT -> equilibrium position unchanged",
        ], [facts[9][0]]),
        panel("Organic and polymer family tree", "branch-map", [
            "FUNCTIONAL GROUPS -> alcohol | aldehyde | ketone | acid | amine | ester",
            "ADDITION POLYMER -> no small-molecule elimination",
            "CONDENSATION POLYMER -> small molecule eliminated",
            "THERMOPLASTIC <-> THERMOSET -> reheating boundary",
            "HYDROGEL -> cross-linked hydrophilic network",
        ], [facts[10][0], facts[11][0], facts[16][0]]),
        panel("Materials structure-property wheel", "portfolio-wheel", [
            "DIAMOND -> tetrahedral network",
            "GRAPHITE -> layered structure",
            "GRAPHENE / FULLERENE / NANOTUBE -> distinct carbon architectures",
            "ALLOY -> composition + processing alter properties",
            "RULE -> same element can yield different material behaviour",
        ], [facts[12][0]]),
        panel("Fuel conversion fault tree", "fault-tree", [
            "COMBUSTION -> oxidation + useful heat + possible pollutants",
            "INCOMPLETE COMBUSTION -> different product burden",
            "GASIFICATION -> controlled oxygen/steam conversion",
            "SYNGAS -> carbon monoxide + hydrogen dominant route",
            "OUTCOME FIREWALL -> product is not efficiency or climate proof",
        ], [facts[13][0], facts[18][0]]),
        panel("Environmental compartment map", "compartment-map", [
            "STRATOSPHERE -> ozone protective role",
            "TROPOSPHERE -> ozone pollutant role",
            "WATER / SOIL -> nutrients, acids, salts, persistent chemicals",
            "EXPOSURE -> concentration + route + duration + conditions",
            "LABEL -> not safety, hazard or regulation evidence",
        ], [facts[14][0], facts[15][0]]),
        panel("PYQ and policy evidence ladder", "status-ladder", [
            "WATER POLARITY -> many ionic/polar solutes, not every substance",
            "BPA / TRICLOSAN -> presence differs from exposure and regulation",
            "HYDROGEL -> material class differs from universal performance",
            "PRINCIPLE -> PROCESS -> APPLICATION -> INSTITUTION",
            "PAGE / DOCUMENT -> not deployment, outcome, hazard or law",
        ], [facts[16][0], facts[17][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2024", "Prelims GS-I",
            "Assess the routed statements on uses of hydrogels.",
            "Verified routed demand covering 2024 Q36; the official Set-A key is available locally but no option, answer letter or objective answer key is reproduced.",
            [11, 16],
        ),
        common.make_pyq_solution(
            facts, "2025", "Prelims GS-I",
            "Assess the routed statements on what coal-gasification technology can produce.",
            "Verified routed demand covering 2025 Q45; the official Set-A key is available locally but no option, answer letter or objective answer key is reproduced.",
            [13, 18],
        ),
        common.make_pyq_solution(
            facts, "2021", "Prelims GS-I",
            "Assess the routed distinctions involving water's dipolar solvent character, bisphenol A in material manufacture and triclosan in personal-care products.",
            "Representative routed card covering 2021 Q71, Q74 and Q75; official keys are unavailable locally and no option, answer letter, product list, safety conclusion or regulatory status is inferred.",
            [5, 10, 15, 17],
        ),
    ]
    return common.topic(
        22,
        "General Science: Chemistry Fundamentals",
        "22_General-Science-Chemistry-Fundamentals",
        facts,
        traps,
        [
            (10, "Explain how atomic structure and periodic trends guide comparison of elemental properties.", [0, 1]),
            (10, "Distinguish ionic, covalent and metallic bonding and relate intermolecular forces to states and solutions.", [2, 4, 5]),
            (15, "Explain mole-based stoichiometry, limiting reagent and yield as a disciplined chemical-accounting framework.", [3, 15]),
            (15, "Analyse acids, bases, pH, buffers, redox cells, reaction rates, catalysis and equilibrium through their correct category boundaries.", [6, 7, 8, 9]),
            (20, "Discuss how functional groups, polymers, carbon allotropes, alloys, fuels and gasification connect molecular structure with industrial application.", [10, 11, 12, 13, 16, 18]),
            (20, "Critically examine how chemistry fundamentals inform environmental governance, consumer-product assessment, water technologies and evidence-based technology policy.", [14, 15, 17, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "atomic number", "mass number", "isotope", "isobar", "isotone",
            "ionisation energy", "electronegativity", "ionic bond",
            "covalent bond", "metallic bond", "hydrogen bonding",
            "van der Waals forces", "mole", "stoichiometry",
            "limiting reagent", "theoretical yield", "states of matter",
            "phase change", "solution", "solute", "solvent", "concentration",
            "solubility", "acid", "base", "pH", "neutralisation", "buffer",
            "salt hydrolysis", "oxidation number", "redox", "anode",
            "cathode", "galvanic cell", "electrolytic cell", "electrolysis",
            "activation energy", "catalyst", "dynamic equilibrium",
            "functional group", "addition polymer", "condensation polymer",
            "thermoplastic", "thermoset", "hydrogel", "allotrope",
            "graphite", "graphene", "alloy", "combustion", "gasification",
            "synthesis gas", "stratospheric ozone", "ground-level ozone",
            "exposure", "persistence", "bisphenol A", "triclosan",
            "CSIR-NCL", "CSIR-CECRI", "National Green Hydrogen Mission",
            "INC-5", "evidence boundary",
        ],
        "Audited ledgers route the 2024 hydrogel objective demand, the 2025 coal-gasification objective demand and the 2021 water-polarity, bisphenol-A and triclosan objective demands to this owner. Three representative answer-free cards preserve all five routed objective demands. The 2024 GS-III freshwater question remains primarily owned by Environment and Ecology; this topic supplies only the bounded chemistry of membranes, phase change, ions, concentration, disinfection and by-products.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source attempts on 2026-09-04 preserve only a Nobel biomolecule anchor, MNRE's mission-level electrochemistry and standards linkage, and UNEP's INC-5 document-process boundary. No volatile production figure, numerical chemical constant, chemical hazard, product-wide exposure claim, treaty outcome, regulatory status, answer key or technology-performance result is asserted.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "OFFICIAL-UPSC-SYLLABUS-MAPPING.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "ATOMS, PERIODICITY, BONDING AND QUANTITATIVE CHEMISTRY",
            "REACTIONS, MATERIALS, FUELS AND ENVIRONMENTAL BOUNDARIES",
            "CHEMISTRY-TO-APPLICATION ANSWER SPINE",
            "ROUTED PYQS, LIVE-SOURCE LIMITS AND RAPID-RECALL FIREWALL",
        ),
        register_answer_spine=[
            "FIX ATOMIC NUMBER MASS NUMBER ISOTOPE ISOBAR ISOTONE AND PERIODIC TREND",
            "CLASSIFY IONIC COVALENT METALLIC AND INTERMOLECULAR INTERACTIONS",
            "BALANCE THE EQUATION THEN APPLY MOLE LIMITING-REAGENT AND YIELD LOGIC",
            "SEPARATE STATE PHASE CHANGE SOLUTION CONCENTRATION AND SOLUBILITY",
            "DISTINGUISH ACID STRENGTH CONCENTRATION pH NEUTRALISATION BUFFER AND SALT",
            "TRACE OXIDATION AT ANODE REDUCTION AT CATHODE AND CELL ENERGY DIRECTION",
            "SEPARATE REACTION RATE ACTIVATION ENERGY CATALYSIS AND DYNAMIC EQUILIBRIUM",
            "MAP FUNCTIONAL GROUP POLYMER CLASS ALLOTROPE ALLOY AND STRUCTURE-PROPERTY LINK",
            "DISTINGUISH COMBUSTION GASIFICATION SYNGAS PRODUCT AND LIFECYCLE OUTCOME",
            "LOCATE ENVIRONMENTAL CHEMISTRY BY COMPARTMENT CONCENTRATION EXPOSURE AND PERSISTENCE",
            "ROUTE HYDROGEL WATER POLARITY BPA TRICLOSAN AND COAL-GASIFICATION PYQS WITHOUT KEYS",
            "CONCLUDE AT THE LAST VERIFIED PRINCIPLE PROCESS APPLICATION INSTITUTION OR DOCUMENT RUNG",
        ],
    )


TOPIC_22 = _topic_22()
