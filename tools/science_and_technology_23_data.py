"""Authored learner-v2 data for Science and Technology Topic 23."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.nobelprize.org/prizes/medicine/2024/press-release/ - "
        "fetched 2026-09-04; the official Nobel release confirmed the joint "
        "award to Victor Ambros and Gary Ruvkun for microRNA and its role in "
        "post-transcriptional gene regulation. The citation was used to anchor "
        "gene regulation, not to infer a diagnostic, therapy or policy outcome."
    ),
    (
        "https://www.nobelprize.org/prizes/medicine/2025/press-release/ - "
        "fetched 2026-09-04; the official release confirmed the award to Mary "
        "E. Brunkow, Fred Ramsdell and Shimon Sakaguchi for discoveries "
        "concerning peripheral immune tolerance, including regulatory T cells "
        "and Foxp3. Clinical-trial references were not rewritten as approved "
        "treatments, population benefit or Indian programme outcomes."
    ),
    (
        "https://www.who.int/news/item/08-10-2024-elimination-of-trachoma-as-a-"
        "public-health-problem-in-india - fetched 2026-09-04; WHO confirmed "
        "validation of India's elimination of trachoma as a public-health "
        "problem, the bacterial cause, transmission routes and SAFE strategy. "
        "Validation was not presented as eradication of the organism or as an "
        "end to post-validation surveillance."
    ),
    (
        "https://www.who.int/publications/m/item/india-polio-transition-"
        "snapshot - fetched 2026-09-04; WHO confirmed that India's transition "
        "approach seeks to sustain polio-free status and reuse the eradication "
        "network for immunization, surveillance and emergency response. The "
        "page supplied no basis for a new coverage or disease-incidence claim."
    ),
    (
        "https://www.who.int/teams/immunization-vaccines-and-biologicals/"
        "immunization-analysis-and-insights/global-monitoring/immunization-"
        "coverage/who-unicef-estimates-of-national-immunization-coverage - "
        "fetched 2026-09-04; WHO confirmed that estimates use Member-State and "
        "other reviewed data, are updated annually, and then reflected data "
        "reported through 21 June 2026. No country percentage was imported."
    ),
]


def _topic_23() -> dict[str, object]:
    facts = [
        (
            "Cell organisation and organelle boundary",
            "A cell is the basic structural and functional unit of life; prokaryotes lack a membrane-bound nucleus and membrane-bound organelles, whereas eukaryotes possess them. The nucleus stores most genetic material, ribosomes synthesize protein, mitochondria support aerobic ATP generation, the endoplasmic reticulum and Golgi system process and move products, lysosomes contain hydrolytic enzymes, and plant cells additionally possess a cellulose wall, chloroplasts and a large vacuole.",
        ),
        (
            "Biomolecules and enzyme specificity",
            "Carbohydrates commonly supply or store energy and provide structures such as cellulose, lipids store energy and form membranes, proteins perform structural, transport, receptor and catalytic roles, and nucleic acids store or express information. Enzymes are biological catalysts whose activity depends on substrate fit and conditions such as temperature and pH; a biomolecule class does not establish one universal function.",
        ),
        (
            "Membrane transport and water balance",
            "Diffusion moves particles down a concentration gradient, osmosis is net water movement across a selectively permeable membrane, and active transport uses cellular energy to move substances against a gradient. Tonicity describes the effect of an external solution on cell water balance, so swelling, plasmolysis and normal volume require the membrane and concentration context.",
        ),
        (
            "Mitosis meiosis and variation",
            "Mitosis is one division producing two genetically similar daughter cells for growth and repair, while meiosis consists of two divisions producing four haploid products for sexual reproduction; crossing over and independent assortment generate variation. Neither process should be described as gene editing, and chromosome number must be tracked relative to the starting cell.",
        ),
        (
            "DNA RNA gene expression and microRNA",
            "DNA replication copies hereditary material, transcription produces RNA from a DNA template, and translation uses messenger RNA, transfer RNA and ribosomes to build protein from codons. RNA also has regulatory roles: microRNA can bind complementary messenger RNA and reduce protein production or promote RNA degradation, so DNA storage, RNA regulation and protein function are distinct stages.",
        ),
        (
            "Inheritance mutation and sex linkage",
            "A gene is a functional hereditary unit on DNA; alleles are alternative forms, segregation separates allele pairs into gametes and independent assortment applies to appropriately unlinked genes. Mutations may be point, frameshift or chromosomal changes and supply variation without guaranteeing benefit; human XX-XY sex determination and X-linked recessive inheritance explain why haemophilia or red-green colour blindness can show sex-biased patterns.",
        ),
        (
            "Digestion absorption and nutrition",
            "Digestion converts food into absorbable molecules: salivary amylase begins starch digestion, pepsin works in acidic stomach conditions, bile emulsifies fat without acting as an enzyme, pancreatic and intestinal enzymes continue digestion, and the small intestine is the principal absorption site. Vitamins, minerals, protein and energy have different roles; deficiency, absorption failure and excess are separate nutritional problems.",
        ),
        (
            "Blood heart and double circulation",
            "Blood contains plasma, red cells carrying haemoglobin, immune white cells and platelets involved in clotting; the four-chambered human heart supports pulmonary and systemic circuits. Arteries carry blood away from the heart and veins return it, so oxygenation is not the defining rule; ABO and Rh compatibility, gas transport and clotting must be treated as different functions.",
        ),
        (
            "Respiration gas exchange and cellular energy",
            "Ventilation moves air, alveolar gas exchange moves oxygen and carbon dioxide across thin surfaces, blood transports gases, and cellular respiration releases usable energy from nutrients. Haemoglobin binds oxygen while carbon monoxide can disrupt transport through stronger binding; breathing, gas exchange and ATP-producing respiration are linked but not synonymous.",
        ),
        (
            "Kidney nephron and homeostasis",
            "The nephron filters blood at the glomerulus and then selectively reabsorbs and secretes substances along its tubule to regulate water, electrolytes, acid-base balance and wastes. Dialysis can replace selected filtration functions when kidneys fail but does not reproduce every endocrine and regulatory role of healthy kidneys.",
        ),
        (
            "Nervous endocrine and feedback control",
            "Neurons transmit rapid electrical signals and communicate chemically at synapses, reflex arcs permit fast automatic responses, and the brain and spinal cord coordinate wider activity. Endocrine glands release hormones into blood for target-dependent effects that are often slower and longer-lasting; neural and hormonal control interact through feedback rather than operating as isolated systems.",
        ),
        (
            "Hormones metabolism and internal stability",
            "Insulin lowers elevated blood glucose by promoting uptake and storage while glucagon supports its rise, thyroid hormones influence metabolism, parathyroid hormone helps regulate calcium, adrenal hormones mediate stress responses and pituitary signals coordinate several glands. Homeostasis is dynamic regulation around a range, not an unchanging value; hormone deficiency, resistance and gland failure are different mechanisms.",
        ),
        (
            "Innate adaptive and tolerance architecture",
            "Innate immunity includes barriers, phagocytes, natural killer cells, complement, interferons, inflammation and fever; adaptive immunity uses antigen-specific B and T lymphocytes and can form memory. B-cell lineages produce antibodies, T cells perform coordinating, cytotoxic or regulatory roles, and peripheral immune tolerance including regulatory T cells limits attack on self; immunity is not antibodies alone.",
        ),
        (
            "Pathogen transmission vector and zoonosis map",
            "Bacteria are cellular organisms, viruses are acellular and depend on host-cell machinery, fungi are eukaryotes, protozoa are single-celled eukaryotes and helminths are multicellular parasites. Transmission may be respiratory, faeco-oral, blood-borne, sexual, vector-borne, fomite-linked or zoonotic; a vector such as Aedes, Anopheles, Culex or sandfly carries a pathogen but is not the disease itself.",
        ),
        (
            "Antibiotic antiviral and AMR boundary",
            "Antibiotics target susceptible bacteria rather than viruses, while antivirals interfere with virus-specific replication stages. Antimicrobial resistance is selection and spread of resistant microorganisms under pressures including misuse, incomplete treatment, agricultural use and environmental residues; the microbe or population becomes resistant, not the patient's body.",
        ),
        (
            "Biofilms microbiome probiotics and extremophiles",
            "A biofilm is a surface-associated microbial community embedded in a matrix that can alter persistence and treatment response; the human microbiome contributes to digestion, vitamin production, immune development and pathogen exclusion. Probiotics are live microorganisms intended to confer a benefit in an adequate amount, while thermophiles, psychrophiles and acidophiles are classified by environmental tolerance; none of these labels proves safety or effectiveness in every context.",
        ),
        (
            "Plant physiology transport and stress response",
            "Photosynthesis stores light energy in chemical form while plants also respire continuously; xylem conducts water and minerals and phloem translocates organic food. Stomata regulate gas exchange and water loss, transpiration contributes to upward water movement, and auxin, gibberellin, cytokinin, abscisic acid and ethylene have distinct growth or stress roles; C3, C4 and CAM are different carbon-fixation strategies.",
        ),
        (
            "Routed taxonomy and organism-form distinctions",
            "Groundnut, horse-gram and soybean are routed pea-family examples; cicada, froghopper and pond skater are insects; poisonous species occur in multiple animal groups, so a broad group name does not prove toxicity. Cassava is a woody shrub, ginger a rhizomatous herb, Malabar spinach a climbing vine, mint a herb and papaya a large herb; mushrooms can have species-specific edible, medicinal, psychoactive, insect-pathogenic or bioluminescent properties.",
        ),
        (
            "Cellulose decomposition route",
            "Cellulose is a structural plant polysaccharide; decomposer fungi and bacteria secrete cellulases that hydrolyse it into smaller sugars, after which microbial metabolism returns carbon through soil and food-web processes. Moisture, temperature, oxygen, lignin and community composition constrain the rate, and natural decomposition is not proof of an industrially viable biofuel process.",
        ),
        (
            "Health institution and evidence-status firewall",
            "ICMR performs and supports biomedical research, NCDC and the IDSP or IHIP network support surveillance and outbreak response under MoHFW, State systems deliver programmes, and CDSCO regulates drugs and vaccines; DBT, CSIR-CCMB and CSIR-IGIB occupy different research roles. A biological mechanism, association, surveillance signal, WHO validation, elimination as a public-health problem, regulatory approval and eradication are separate evidence rungs.",
        ),
    ]
    traps = [
        "Do not merge prokaryotic and eukaryotic cells or assign every organelle to every cell.",
        "Do not give every carbohydrate, lipid, protein or enzyme one universal function.",
        "Do not confuse diffusion, osmosis and energy-dependent active transport.",
        "Do not merge mitosis with meiosis or crossing over with gene editing.",
        "Do not reduce RNA to a passive messenger or equate transcription with translation.",
        "Do not treat a mutation, gene association or sex-linked pattern as deterministic destiny.",
        "Do not call bile an enzyme or the stomach the principal site of nutrient absorption.",
        "Do not define arteries and veins by oxygen content.",
        "Do not use breathing, alveolar gas exchange and cellular respiration as synonyms.",
        "Do not claim dialysis reproduces every kidney function.",
        "Do not merge a neural impulse, neurotransmitter, enzyme and hormone.",
        "Do not describe homeostasis as a perfectly fixed internal value.",
        "Do not equate immunity with antibodies alone or an antigen with an antibody.",
        "Do not treat bacteria, viruses, fungi, protozoa, helminths and vectors as one category.",
        "Do not route vaccine platforms, monoclonal antibodies or gene-editing mechanisms into this fundamentals owner.",
    ]
    titles = [
        "Cell types organelles biomolecules and enzymes",
        "Membranes diffusion osmosis active transport and tonicity",
        "Mitosis meiosis chromosomes and biological variation",
        "DNA RNA replication transcription translation and microRNA",
        "Mendelian inheritance mutation sex determination and sex linkage",
        "Digestion absorption nutrients vitamins and deficiency logic",
        "Blood circulation heart gas transport and clotting",
        "Respiration excretion nephron and homeostasis",
        "Nervous control reflex arcs endocrine glands and feedback",
        "Innate adaptive humoral cellular and tolerance pathways",
        "Pathogens transmission vectors zoonoses and disease classes",
        "Antibiotics antivirals antimicrobial resistance and biofilms",
        "Microbiome probiotics extremophiles and microbial context",
        "Plant physiology photosynthesis transport hormones and adaptation",
        "Routed organisms cellulose institutions PYQs and evidence status",
    ]
    routes = [
        "Move from cell type to organelle, biomolecule, function and condition-specific limitation.",
        "Fix the membrane, gradient, water or solute and energy requirement before predicting movement.",
        "Track division count, chromosome state, product number and source of variation.",
        "Trace information from DNA through RNA to protein while preserving regulatory RNA roles.",
        "Define gene and allele, apply segregation carefully and qualify mutation or sex-linked inference.",
        "Follow food breakdown to enzyme condition, absorption site, nutrient function and deficiency mechanism.",
        "Separate blood component, vessel direction, heart circuit, gas carriage and clotting role.",
        "Distinguish ventilation, gas exchange, cellular energy, filtration and whole-body regulation.",
        "Map receptor, signal route, effector and negative feedback across neural and hormonal control.",
        "Classify barrier, cell, antibody, memory and tolerance before making a public-health claim.",
        "Name the agent, reservoir, route, vector and prevention layer without category drift.",
        "Match the drug class to the organism and explain resistance as microbial selection.",
        "State community, host or environmental context before inferring benefit, hazard or treatment response.",
        "Trace light, carbon, water, transport tissue, stomatal control and stress strategy.",
        "Route each printed demand to the exact taxonomy, decomposition or institution distinction and stop at the last verified status.",
    ]
    panels = [
        panel("Cell and organelle map", "nested-cell-map", [
            "PROKARYOTE -> no membrane-bound nucleus or organelles",
            "EUKARYOTE -> nucleus + compartmental organelles",
            "RIBOSOME -> protein | MITOCHONDRION -> ATP",
            "ER + GOLGI -> processing and movement",
            "PLANT -> cellulose wall + chloroplast + large vacuole",
        ], [facts[0][0], facts[1][0]]),
        panel("Membrane transport decision tree", "transport-tree", [
            "SOLUTE DOWN GRADIENT -> diffusion",
            "WATER + SELECTIVE MEMBRANE -> osmosis",
            "AGAINST GRADIENT + ENERGY -> active transport",
            "EXTERNAL TONICITY -> cell water response",
            "TRAP -> movement depends on membrane and gradient",
        ], [facts[2][0]]),
        panel("Cell division comparison", "two-column-division", [
            "MITOSIS -> one division -> two similar cells",
            "ROLE -> growth and repair",
            "MEIOSIS -> two divisions -> four haploid products",
            "ROLE -> gametes + variation",
            "CROSSING OVER != gene editing",
        ], [facts[3][0]]),
        panel("Gene-expression rail", "information-rail", [
            "DNA --replication--> DNA",
            "DNA --transcription--> mRNA",
            "mRNA + tRNA + RIBOSOME --translation--> protein",
            "microRNA -> post-transcriptional regulation",
            "PROTEIN -> cell structure / enzyme / receptor / signal",
        ], [facts[4][0], facts[5][0]]),
        panel("Nutrition and digestion route", "organ-route", [
            "MOUTH -> amylase",
            "STOMACH -> acid + pepsin",
            "LIVER / BILE -> fat emulsification",
            "PANCREAS + INTESTINE -> digestion completion",
            "SMALL INTESTINE -> principal absorption",
        ], [facts[6][0]]),
        panel("Transport respiration excretion loop", "physiology-loop", [
            "LUNGS -> alveolar gas exchange",
            "BLOOD -> gases + nutrients + hormones + wastes",
            "HEART -> pulmonary + systemic circulation",
            "CELLS -> ATP-producing respiration",
            "NEPHRON -> filtration + reabsorption + secretion",
        ], [facts[7][0], facts[8][0], facts[9][0]]),
        panel("Control and feedback ladder", "feedback-ladder", [
            "RECEPTOR -> change detected",
            "NERVOUS -> rapid wired response",
            "ENDOCRINE -> blood-borne hormone response",
            "TARGET -> physiological adjustment",
            "NEGATIVE FEEDBACK -> restores regulated range",
        ], [facts[10][0], facts[11][0]]),
        panel("Immunity architecture", "layered-defence", [
            "BARRIERS + PHAGOCYTES + COMPLEMENT -> innate",
            "B CELL -> antibody / memory",
            "T CELL -> helper / cytotoxic / regulatory roles",
            "REGULATORY T CELL + Foxp3 -> peripheral tolerance",
            "SELF-REACTIVITY CONTROL != no immune response",
        ], [facts[12][0]]),
        panel("Disease transmission grid", "agent-route-grid", [
            "BACTERIUM | VIRUS | FUNGUS | PROTOZOAN | HELMINTH",
            "AIR | WATER/FOOD | BLOOD | CONTACT | VECTOR",
            "VECTOR -> carries pathogen, is not disease",
            "ZOONOSIS -> animal-human interface",
            "PREVENTION -> mechanism-specific layers",
        ], [facts[13][0], facts[14][0]]),
        panel("Microbial ecology and resistance", "selection-ecology-map", [
            "ANTIMICROBIAL PRESSURE -> selection",
            "RESISTANT MICROBE -> survival + spread",
            "BIOFILM -> matrix-protected community",
            "MICROBIOME / PROBIOTIC -> context-dependent roles",
            "EXTREMOPHILE LABEL -> tolerance, not universal safety",
        ], [facts[14][0], facts[15][0]]),
        panel("Plant function flow", "plant-flow", [
            "ROOT -> water + mineral uptake",
            "XYLEM -> upward transport",
            "LEAF -> stomata + photosynthesis + transpiration",
            "PHLOEM -> food translocation",
            "C3 | C4 | CAM -> different carbon-fixation strategies",
        ], [facts[16][0]]),
        panel("PYQ and evidence-status rail", "status-rail", [
            "TAXON / PLANT FORM / SPECIES PROPERTY -> exact classification",
            "CELLULOSE -> cellulase -> sugars -> microbial metabolism",
            "RESEARCH -> SURVEILLANCE -> PROGRAMME DELIVERY -> REGULATION",
            "WHO VALIDATION != pathogen eradication",
            "MECHANISM / ASSOCIATION / APPROVAL / OUTCOME -> separate rungs",
        ], [facts[17][0], facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018-2023", "Prelims GS-I",
            "Assess routed distinctions on plant adaptations, cell structure, pathogens, artificial culture, viral genomes, ACE2, biofilms, probiotics, B and T cells, mushrooms and extremophiles.",
            "Representative historical objective card covering thirteen routed demands; official keys are unavailable locally, so no option, answer letter or inferred key is supplied.",
            [0, 12, 13, 14, 15, 17],
        ),
        common.make_pyq_solution(
            facts, "2024-2025", "Prelims GS-I",
            "Assess routed organism-family, insect, poisonous-species, nitric-oxide, plant-form and virus-host distinctions.",
            "Representative recent objective card covering six routed demands; official Set-A keys exist locally but no option, answer letter or objective key is reproduced.",
            [11, 13, 17],
        ),
        common.make_pyq_solution(
            facts, "2022", "GS-III",
            "Discuss the natural processes through which cellulose undergoes decomposition on the Earth's surface.",
            "Verified routed Mains demand at 10 marks and 150 words; the response supplies a mechanism-first answer route and qualification, not an official model answer.",
            [1, 15, 18],
        ),
    ]
    return common.topic(
        23,
        "General Science: Biology and Physiology",
        "23_General-Science-Biology-and-Physiology",
        facts,
        traps,
        [
            (10, "Distinguish cell types, organelles, biomolecules and membrane-transport mechanisms.", [0, 1, 2]),
            (10, "Explain how cell division, gene expression, inheritance and mutation generate biological continuity and variation.", [3, 4, 5]),
            (15, "Analyse digestion, circulation, respiration and excretion as an integrated physiological system.", [6, 7, 8, 9]),
            (15, "Explain how nervous, endocrine and immune systems maintain regulated internal function.", [10, 11, 12]),
            (20, "Examine disease transmission, antimicrobial resistance, biofilms and microbiome interactions through a One Health and public-health lens.", [13, 14, 15, 19]),
            (20, "Discuss plant physiology, organism classification and cellulose decomposition while preserving biotechnology and vaccine owner boundaries.", [16, 17, 18]),
        ],
        titles,
        routes,
        panels,
        [
            "prokaryotes", "eukaryotes", "ribosomes", "mitochondria",
            "cellulose wall", "biomolecules", "enzymes", "diffusion",
            "osmosis", "active transport", "mitosis", "meiosis",
            "crossing over", "DNA replication", "transcription",
            "translation", "microRNA", "post-transcriptional gene regulation",
            "alleles", "segregation", "mutation", "small intestine",
            "bile emulsifies", "haemoglobin", "double circulation",
            "alveolar gas exchange", "cellular respiration", "nephron",
            "homeostasis", "reflex arcs", "endocrine glands", "insulin",
            "glucagon", "innate immunity", "adaptive immunity", "B and T lymphocytes",
            "regulatory T cells", "peripheral immune tolerance", "Foxp3",
            "bacteria", "viruses", "fungi", "protozoa", "helminths",
            "vector-borne", "zoonotic", "antibiotics", "antivirals",
            "antimicrobial resistance", "biofilm", "microbiome", "probiotics",
            "thermophiles", "psychrophiles", "acidophiles", "xylem",
            "phloem", "stomata", "C3, C4 and CAM", "cicada",
            "froghopper", "pond skater", "cassava", "Malabar spinach",
            "cellulases", "ICMR", "NCDC", "IDSP or IHIP", "CDSCO",
            "elimination as a public-health problem", "eradication",
        ],
        "Audited ledgers route thirteen historical Prelims demands from 2018-2023, six Prelims demands from 2024-2025 and the 2022 GS-III cellulose-decomposition demand to this owner. Three representative cards preserve historical objective, recent objective and Mains routes without reproducing answer keys. Vaccine-platform, monoclonal-antibody and gene-editing demands remain with Topics 15 and 14.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source checks on 2026-09-04 retained the 2024 microRNA citation, the 2025 peripheral-immune-tolerance citation, WHO's trachoma validation and polio-transition boundaries, and WHO/UNICEF's annual estimate methodology. No therapy approval, vaccine-platform claim, coverage percentage, eradication claim, medical advice or PYQ key was invented.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "CELL, BIOMOLECULE, GENETICS AND MEMBRANE RAPID MAP",
            "HUMAN PHYSIOLOGY, HOMEOSTASIS AND IMMUNITY SYSTEM GRID",
            "DISEASE, MICROBE, PLANT AND ROUTED-PYQ FIREWALLS",
            "PUBLIC-HEALTH INSTITUTION, STATUS AND ANSWER-WRITING SPINE",
        ),
        register_answer_spine=[
            "IDENTIFY CELL TYPE ORGANELLE BIOMOLECULE MEMBRANE AND GRADIENT",
            "TRACE DNA REPLICATION TRANSCRIPTION RNA REGULATION TRANSLATION AND PROTEIN",
            "SEPARATE MITOSIS MEIOSIS MUTATION VARIATION AND GENE EDITING",
            "FOLLOW DIGESTION ABSORPTION CIRCULATION GAS EXCHANGE RESPIRATION AND EXCRETION",
            "MAP NEURAL SIGNAL HORMONE TARGET FEEDBACK AND HOMEOSTATIC RANGE",
            "CLASSIFY INNATE ADAPTIVE HUMORAL CELLULAR MEMORY AND TOLERANCE",
            "NAME PATHOGEN RESERVOIR TRANSMISSION ROUTE VECTOR AND PREVENTION LAYER",
            "EXPLAIN AMR AS MICROBIAL SELECTION AND BIOFILM AS A COMMUNITY STATE",
            "CONNECT PHOTOSYNTHESIS XYLEM PHLOEM STOMATA HORMONES AND STRESS STRATEGY",
            "ROUTE TAXONOMY PLANT FORM NITRIC OXIDE VIRUS AND CELLULOSE PYQS WITHOUT KEYS",
            "KEEP ICMR NCDC STATE DELIVERY CDSCO DBT AND CSIR ROLES DISTINCT",
            "STOP AT MECHANISM ASSOCIATION SURVEILLANCE VALIDATION APPROVAL OR OUTCOME",
        ],
    )


TOPIC_23 = _topic_23()
