"""Authored learner-v2 data for Science and Technology Topic 13."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


BIOTECH_LIVE_ATTEMPTS = [
    (
        "https://dbt.gov.in/data-view?name=press-release — fetched "
        "2026-09-04; the official DBT press-release index listed Bio-RIDE "
        "(19 September 2024), completion of sequencing of 10,000 Indian "
        "genomes (28 February 2024), and a GenomeIndia translational-research "
        "call. Listing and call status were not rewritten as funded outputs, "
        "clinical validation, commercial products or population-wide coverage."
    ),
    (
        "https://birac.nic.in/desc_new.php?id=89 — fetched 2026-09-04; "
        "the official BIRAC mandate page identified BIRAC as a not-for-profit "
        "Section 8, Schedule B public sector enterprise set up by DBT and as "
        "an industry-academia interface for innovation, risk capital, "
        "technology transfer, IP management and commercialisation. It was not "
        "treated as a regulator or as proof of firm-level success."
    ),
    (
        "https://birac.nic.in/biomanufacturing.php — fetched 2026-09-04; "
        "the official BIRAC page confirmed Cabinet approval of BioE3 on "
        "24 August 2024 and access to shared pilot and pre-commercial "
        "biomanufacturing infrastructure. Policy approval and infrastructure "
        "intent were not converted into installed capacity, funded-project "
        "totals, production, emissions reduction or market deployment."
    ),
]


def _topic_13() -> dict[str, object]:
    facts = [
        (
            "Biotechnology-platform boundary",
            "Biotechnology uses genes, cells, tissues, enzymes or organisms "
            "together with engineering and processing to create knowledge, "
            "services or products; it includes recombinant DNA, diagnostics, "
            "culture and fermentation and therefore cannot be reduced to GM crops.",
        ),
        (
            "Central-dogma boundary",
            "The core information rail is DNA --transcription--> RNA "
            "--translation--> protein; a technique must be located on this rail, "
            "while reverse transcription is an explicit RNA-to-DNA operation and "
            "not a reversal of every biological information flow.",
        ),
        (
            "Recombinant-DNA chain",
            "Recombinant DNA work joins DNA from different sources through a "
            "chain of target identification, restriction-endonuclease cutting, "
            "vector insertion, DNA-ligase joining, host transformation, marker "
            "selection and expression; a vector is a carrier, not the desired gene.",
        ),
        (
            "PCR-RT-PCR boundary",
            "PCR amplifies target DNA through denaturation, primer annealing and "
            "thermostable-polymerase extension; reverse-transcription PCR first "
            "converts RNA to complementary DNA, whereas real-time PCR describes "
            "signal measurement during amplification and is a different axis.",
        ),
        (
            "Fermentation-bioprocess chain",
            "Industrial bioprocessing controls organism or cell line, nutrients, "
            "temperature, pH, oxygen and contamination in a bioreactor, followed "
            "by downstream recovery, purification and quality control; "
            "fermentation is not confined to alcohol production.",
        ),
        (
            "Tissue-culture-totipotency boundary",
            "Tissue culture grows cells or explants aseptically on controlled "
            "media; plant micropropagation rests on totipotency, the capacity of "
            "a suitable somatic cell to regenerate a whole plant, but clonal "
            "propagation does not itself mean genetic engineering.",
        ),
        (
            "Stem-cell-potency boundary",
            "Stem cells self-renew and differentiate: embryonic stem cells are "
            "pluripotent, many adult stem cells are tissue-restricted or "
            "multipotent, and induced pluripotent stem cells are reprogrammed "
            "somatic cells; pluripotent does not mean totipotent.",
        ),
        (
            "Gene-therapy boundary",
            "Gene therapy adds, replaces, silences or edits a disease-relevant "
            "sequence in selected cells using delivery systems such as engineered "
            "viral vectors or lipid nanoparticles; somatic treatment is not "
            "heritable germline modification and does not rewrite an entire genome.",
        ),
        (
            "Molecular-diagnostics boundary",
            "Molecular diagnostics detect nucleic-acid, protein or other molecular "
            "signatures through validated sampling, extraction, amplification or "
            "detection and interpretation; detecting a marker is not by itself "
            "proof of viable pathogen, disease severity or clinical outcome.",
        ),
        (
            "DBT-BIRAC boundary",
            "DBT is the central biotechnology department under the Ministry of "
            "Science and Technology for policy, research support and missions, "
            "whereas BIRAC is the DBT-set-up not-for-profit Section 8 public "
            "sector enterprise and industry-academia translation interface; "
            "neither description makes BIRAC a biosafety or drug regulator.",
        ),
        (
            "Institutional-router boundary",
            "DBT, ICMR, CSIR and ICAR support or perform research in different "
            "administrative domains, BIRAC supports translation and enterprise, "
            "CDSCO regulates drugs and vaccines, and GEAC appraises environmental "
            "release of regulated GM organisms; funding, research and approval "
            "functions are not interchangeable.",
        ),
        (
            "BioE3-six-sector boundary",
            "BioE3, approved on 24 August 2024, organises high-performance "
            "biomanufacturing around six sectors: bio-based chemicals and enzymes; "
            "functional foods and smart proteins; precision biotherapeutics; "
            "climate-resilient agriculture; carbon capture and its utilisation; "
            "and futuristic marine and space research.",
        ),
        (
            "Bio-RIDE boundary",
            "Bio-RIDE, approved on 19 September 2024, is DBT's umbrella scheme "
            "for biotechnology research, innovation, entrepreneurship and a "
            "biomanufacturing component; scheme approval is not expenditure, "
            "project completion, installed capacity or commercial adoption. The "
            "National Biotechnology Development Strategy 2021-2025 is an elapsed "
            "historical frame, and no successor may be assumed without a source.",
        ),
        (
            "GenomeIndia boundary",
            "DBT announced completion of sequencing of 10,000 genomes from the "
            "Indian population on 28 February 2024; the resulting population "
            "reference can support variant interpretation and research, but a "
            "reference dataset is not a clinical diagnosis or a complete map of "
            "every Indian community and it retains consent, equity and data duties.",
        ),
        (
            "Biofoundry-scale-up boundary",
            "A biofoundry supports iterative design-build-test-learn work, while "
            "pilot and pre-commercial facilities test whether a laboratory "
            "process can be controlled and reproduced at larger scale; shared "
            "infrastructure access does not establish commercial-scale production.",
        ),
        (
            "Biopharma-translation boundary",
            "Recombinant proteins, diagnostics, cell systems and bioprocesses can "
            "support biopharma and social applications; recombinant human insulin "
            "and Ti-plasmid plant transformation are standard mechanism examples, "
            "while the National Biopharma Mission and BioNEST illustrate DBT-BIRAC "
            "translation support. Research achievement must still pass validation, "
            "regulation, manufacturing quality, affordability, procurement and access.",
        ),
        (
            "Microbes-biofuel boundary",
            "Microorganisms can support anaerobic digestion to biogas, "
            "fermentation-derived fuels and enzyme-enabled conversion of biomass "
            "or waste, but energy value depends on feedstock, land and water use, "
            "collection, conversion efficiency, lifecycle emissions and scale.",
        ),
        (
            "Objective-biotech-concepts boundary",
            "DNA barcoding uses short standard markers with reference databases "
            "for identification; aquaculture biofilters rely on attached microbial "
            "communities; Wolbachia approaches alter mosquito-vector dynamics; and "
            "aerial metagenomics detects airborne DNA without automatically proving "
            "that an organism is alive, abundant or pathogenic.",
        ),
        (
            "Clean-tech-contribution boundary",
            "Biotechnology can complement clean-energy independence through "
            "biofuels, waste and biomass conversion, enzymes, bio-based chemicals "
            "and carbon-use pathways, but it cannot substitute for renewables, "
            "efficiency, storage, grids or lifecycle and ecological safeguards.",
        ),
        (
            "Status-and-number firewall",
            "Discovery, proof of concept, proposal, funded project, pilot, "
            "pre-commercial validation, regulatory approval, manufacturing and "
            "market adoption are separate rungs; dates, proposal counts, genome "
            "counts, capacities, outcomes and objective answer keys require their "
            "own dated authoritative evidence.",
        ),
    ]
    traps = [
        "Do not reduce biotechnology to genetic engineering or GM crops.",
        "Do not treat central dogma as forbidding reverse transcription.",
        "Do not confuse a vector, inserted gene, host and expressed product.",
        "Do not use RT-PCR as an unqualified synonym for real-time PCR.",
        "Do not reduce fermentation to alcohol or ignore downstream processing.",
        "Do not merge tissue culture, cloning and recombinant DNA.",
        "Do not equate pluripotency with totipotency or iPSCs with embryos.",
        "Do not turn somatic gene therapy into heritable germline editing.",
        "Do not infer infection, viability or severity from marker detection alone.",
        "Do not make BIRAC, DBT, CDSCO and GEAC interchangeable.",
        "Do not omit or rename any of BioE3's six official sectors.",
        "Do not upgrade approval, calls, proposals, pilots or sequencing into impact.",
    ]
    titles = [
        "Biotechnology platform and central dogma",
        "Recombinant DNA tools vectors hosts and expression",
        "PCR reverse transcription and real-time detection",
        "Fermentation bioreactors and downstream processing",
        "Tissue culture micropropagation and totipotency",
        "Stem-cell potency embryonic adult and iPSC distinctions",
        "Gene therapy delivery somatic and germline boundaries",
        "Molecular diagnostics validation and interpretation",
        "DBT BIRAC and the translation architecture",
        "Research funding and regulatory institution router",
        "BioE3 policy and its six biomanufacturing sectors",
        "Bio-RIDE umbrella and programme-status discipline",
        "GenomeIndia reference data uses and safeguards",
        "Biofoundries pilot scale and commercial scale-up",
        "Routed PYQs clean-tech synthesis and answer spine",
    ]
    routes = [
        "Define biotechnology broadly, then place intervention on DNA-RNA-protein.",
        "Trace cut, join, carry, transform, select and express without merging roles.",
        "Separate template conversion, amplification chemistry and signal timing.",
        "Follow upstream control through downstream recovery and quality assurance.",
        "Link aseptic culture to plant totipotency without claiming transgenesis.",
        "Compare source and potency, then state the pluripotent-totipotent limit.",
        "Map therapeutic action, carrier, target cells and heritability boundary.",
        "Move from sample to marker to interpretation with validation caveats.",
        "Assign mission design to DBT and translation support to BIRAC.",
        "Route research, enterprise support, drug approval and GMO release correctly.",
        "Name all six sectors and connect policy to high-performance biomanufacturing.",
        "Preserve the distinction between umbrella approval and realised outcomes.",
        "State the 10,000-sequence milestone, research use and data safeguards.",
        "Explain why reproducibility at pilot scale is the translation bottleneck.",
        "Answer audited demands through mechanism, application, institution and limit.",
    ]
    panels = [
        panel("Biotechnology information rail", "process-rail", [
            "BIOLOGICAL INPUT -> gene / cell / tissue / enzyme / organism",
            "DNA --TRANSCRIPTION--> RNA --TRANSLATION--> PROTEIN",
            "INTERVENTIONS -> rDNA / PCR / culture / diagnostics / bioprocess",
            "OUTPUT -> knowledge / service / regulated product",
            "RULE -> biotechnology is broader than genetic engineering",
        ], [facts[0][0], facts[1][0]]),
        panel("Recombinant DNA assembly chain", "assembly-chain", [
            "TARGET GENE -> restriction endonuclease cut",
            "VECTOR -> plasmid / bacteriophage / Ti-plasmid carrier",
            "DNA LIGASE -> recombinant construct",
            "HOST TRANSFORMATION -> marker selection -> expression",
            "TRAP -> vector, insert, host and product are different",
        ], [facts[2][0]]),
        panel("PCR distinction matrix", "comparison-matrix", [
            "PCR CORE -> denaturation -> annealing -> extension",
            "THERMOSTABLE POLYMERASE -> repeated DNA copying",
            "REVERSE-TRANSCRIPTION PCR -> RNA first converted to cDNA",
            "REAL-TIME PCR -> fluorescence measured during amplification",
            "RULE -> template conversion and detection timing are separate axes",
        ], [facts[3][0], facts[8][0]]),
        panel("Bioprocess scale rail", "scale-up-rail", [
            "STRAIN / CELL LINE + MEDIUM -> upstream preparation",
            "BIOREACTOR -> pH / temperature / oxygen / sterility control",
            "HARVEST -> downstream recovery and purification",
            "QUALITY CONTROL -> identity / purity / reproducibility",
            "LAB SUCCESS != PILOT != COMMERCIAL MANUFACTURE",
        ], [facts[4][0], facts[14][0], facts[19][0]]),
        panel("Culture and potency map", "branch-map", [
            "PLANT EXPLANT -> sterile medium -> callus / shoots / roots",
            "TOTIPOTENCY -> suitable cell can regenerate whole plant",
            "EMBRYONIC STEM CELL -> pluripotent",
            "ADULT STEM CELL -> usually multipotent / tissue-restricted",
            "iPSC -> somatic cell reprogrammed to pluripotency",
        ], [facts[5][0], facts[6][0]]),
        panel("Gene therapy and diagnostics twin rail", "dual-rail", [
            "THERAPY -> add / replace / silence / edit disease-relevant sequence",
            "DELIVERY -> engineered viral vector or lipid nanoparticle",
            "DIAGNOSTIC -> sample -> extraction -> marker detection -> interpretation",
            "SOMATIC != GERMLINE; MARKER != CLINICAL OUTCOME",
            "RULE -> mechanism, delivery, validation and status all matter",
        ], [facts[7][0], facts[8][0]]),
        panel("Biotechnology institution router", "institution-map", [
            "DBT / MINISTRY OF S&T -> policy, missions and research support",
            "BIRAC -> industry-academia translation and enterprise support",
            "ICMR / CSIR / ICAR -> domain-specific research systems",
            "CDSCO -> drugs and vaccines; GEAC -> GMO environmental release",
            "RULE -> funder, performer, interface and regulator are distinct",
        ], [facts[9][0], facts[10][0]]),
        panel("BioE3 six-sector wheel", "six-sector-wheel", [
            "1 BIO-BASED CHEMICALS AND ENZYMES",
            "2 FUNCTIONAL FOODS AND SMART PROTEINS",
            "3 PRECISION BIOTHERAPEUTICS",
            "4 CLIMATE-RESILIENT AGRICULTURE",
            "5 CARBON CAPTURE AND ITS UTILISATION",
            "6 FUTURISTIC MARINE AND SPACE RESEARCH",
        ], [facts[11][0]]),
        panel("Bio-RIDE and GenomeIndia timeline", "timeline", [
            "28 FEB 2024 -> DBT announces 10,000 GenomeIndia sequences complete",
            "24 AUG 2024 -> Cabinet approves BioE3",
            "19 SEP 2024 -> Cabinet approves Bio-RIDE",
            "GENOME DATA -> reference and research potential plus safeguards",
            "APPROVAL / COMPLETION VERB -> preserve exact object and status",
        ], [facts[12][0], facts[13][0], facts[19][0]]),
        panel("Research-to-impact funnel", "translation-funnel", [
            "DISCOVERY -> proof of concept",
            "BIRAC / INCUBATOR -> translation and enterprise support",
            "BIOFOUNDRY / PILOT -> reproducibility and process optimisation",
            "REGULATION / QUALITY / MANUFACTURE -> adoption gateway",
            "SOCIAL BENEFIT -> affordability, access and fit still required",
        ], [facts[14][0], facts[15][0], facts[19][0]]),
        panel("PYQ applications matrix", "comparison-matrix", [
            "BIOPHARMA -> rDNA + culture + bioprocess + quality + access",
            "MICROBES / FUEL -> digestion + fermentation + biomass conversion",
            "OBJECTIVE CONCEPTS -> barcode / biofilter / Wolbachia / air DNA",
            "CLEAN TECH -> bounded contribution to wider energy transition",
            "2026 -> genetic medicine and GenomeIndia; no provisional key asserted",
        ], [facts[15][0], facts[16][0], facts[17][0], facts[18][0]]),
        panel("Biotechnology answer spine", "answer-spine", [
            "DEFINE -> platform and biological information level",
            "EXPLAIN -> mechanism from laboratory to bioprocess",
            "MAP -> DBT / BIRAC / research bodies / regulators",
            "APPLY -> health / agriculture / industry / environment / energy",
            "QUALIFY -> biosafety, data, scale, affordability and status",
        ], [facts[0][0], facts[9][0], facts[10][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018 and 2021", "GS-III",
            "Discuss biotechnology activity and biopharma benefits in India, and "
            "identify applied biotechnology R&D achievements with potential for "
            "social upliftment.",
            "Two verified routed Mains demands are consolidated in one "
            "representative card. The answer distinguishes scientific achievement "
            "from validated, affordable and accessible social outcomes.",
            [0, 2, 4, 9, 15, 19],
        ),
        common.make_pyq_solution(
            facts, "2023", "GS-III and Prelims GS-I",
            "Explain how microorganisms can address fuel shortages and distinguish "
            "routed objective concepts including biofilters, Wolbachia-based "
            "vector control and aerial metagenomics.",
            "The verified 2023 Mains fuel demand and routed objective biotechnology "
            "concepts are represented together; the unavailable objective answer "
            "letters are neither recorded nor inferred.",
            [16, 17, 4, 8, 19],
        ),
        common.make_pyq_solution(
            facts, "2025 and provisional 2026", "GS-III and Prelims GS-I",
            "Assess biotechnology's contribution to clean-technology energy "
            "independence and distinguish genetic medicines, delivery vectors, "
            "therapeutic DNA modification and GenomeIndia institutional claims.",
            "The verified 2025 Mains demand is combined with the provisional 2026 "
            "routed concepts. No provisional option letter or answer key is "
            "recorded, inferred or used as evidence for a proposition.",
            [7, 13, 18, 19],
        ),
    ]
    return common.topic(
        13,
        "Biotechnology Fundamentals and DBT Missions",
        "13_Biotechnology-Fundamentals-and-DBT-Missions",
        facts,
        traps,
        [
            (10, "Explain the central dogma and the basic recombinant-DNA workflow.", [1, 2]),
            (10, "Differentiate PCR, RT-PCR and molecular diagnostic interpretation.", [3, 8]),
            (15, "Examine fermentation, tissue culture and stem-cell platforms as distinct biotechnology tools.", [4, 5, 6]),
            (15, "Analyse the roles of DBT, BIRAC and sectoral regulators in biotechnology translation.", [9, 10, 15]),
            (20, "Evaluate BioE3, Bio-RIDE and GenomeIndia as pillars of India's biotechnology strategy.", [11, 12, 13, 14, 19]),
            (20, "Discuss biotechnology's contribution to health, social upliftment and clean-energy security while preserving scale, safety and status boundaries.", [7, 8, 15, 16, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "central dogma",
            "transcription",
            "translation",
            "reverse transcription",
            "recombinant DNA",
            "restriction endonuclease",
            "DNA ligase",
            "vector",
            "transformation",
            "PCR",
            "RT-PCR",
            "Taq polymerase",
            "fermentation",
            "bioreactor",
            "downstream processing",
            "tissue culture",
            "totipotency",
            "micropropagation",
            "stem cells",
            "pluripotent",
            "multipotent",
            "induced pluripotent stem cells",
            "gene therapy",
            "somatic",
            "germline",
            "viral vector",
            "lipid nanoparticle",
            "molecular diagnostics",
            "DBT",
            "Ministry of Science and Technology",
            "BIRAC",
            "Section 8",
            "ICMR",
            "CSIR",
            "ICAR",
            "CDSCO",
            "GEAC",
            "BioE3",
            "bio-based chemicals and enzymes",
            "functional foods and smart proteins",
            "precision biotherapeutics",
            "climate-resilient agriculture",
            "carbon capture and its utilisation",
            "futuristic marine and space research",
            "Bio-RIDE",
            "National Biotechnology Development Strategy 2021-2025",
            "GenomeIndia",
            "10,000 genomes",
            "biofoundry",
            "pilot scale",
            "pre-commercial",
            "National Biopharma Mission",
            "BioNEST",
            "recombinant human insulin",
            "Ti plasmid",
            "DNA barcoding",
            "biofilter",
            "Wolbachia",
            "aerial metagenomics",
            "biopharma",
            "biofuels",
        ],
        (
            "Three representative audited cards cover the 2018 and 2021 GS-III "
            "biotechnology and biopharma demands; the 2023 microorganisms-and-fuel "
            "Mains demand plus routed objective biotechnology concepts; and the "
            "2025 clean-technology biotechnology demand plus provisional 2026 "
            "genetic-medicine and GenomeIndia concepts. No objective answer letter "
            "or provisional key is invented."
        ),
        pyqs,
        BIOTECH_LIVE_ATTEMPTS,
        (
            "Official DBT and BIRAC sources were attempted or fetched on "
            "2026-09-04. They support the DBT-BIRAC institutional distinction, "
            "BioE3 approval and pilot/pre-commercial infrastructure intent, "
            "Bio-RIDE's dated listing, and GenomeIndia's 10,000-sequence "
            "completion announcement. They do not establish disbursement, "
            "installed capacity, product approval, commercial output, clinical "
            "utility, emissions reduction or population-wide representativeness."
        ),
        extra=["00_Master-Framework.md", "ANSWER-WORTHINESS-AUDIT.md"],
        register_headings=(
            "MOLECULAR TOOLKIT: DOGMA, rDNA, PCR AND DIAGNOSTICS",
            "CELL, TISSUE AND BIOPROCESS PLATFORMS",
            "DBT-BIRAC MISSIONS, REGULATORS AND SIX-SECTOR BIOE3 MAP",
            "GENOME, SCALE-UP, PYQ AND STATUS FIREWALL",
        ),
        register_answer_spine=[
            "DEFINE BIOTECHNOLOGY AS A GENE-CELL-TISSUE-BIOPROCESS PLATFORM",
            "PLACE THE TECHNIQUE ON DNA-RNA-PROTEIN OR CELLULAR PROCESS RAIL",
            "TRACE rDNA CUT-JOIN-VECTOR-HOST-SELECTION-EXPRESSION",
            "SEPARATE PCR REVERSE TRANSCRIPTION REAL-TIME SIGNAL AND DIAGNOSIS",
            "MAP CULTURE POTENCY FERMENTATION BIOREACTOR AND DOWNSTREAM PROCESSING",
            "ROUTE DBT BIRAC ICMR CSIR ICAR CDSCO AND GEAC BY FUNCTION",
            "NAME ALL SIX BIOE3 SECTORS AND LOCATE BIO-RIDE",
            "USE GENOMEINDIA AS A REFERENCE-DATA MILESTONE WITH SAFEGUARDS",
            "MOVE FROM DISCOVERY TO PILOT REGULATION MANUFACTURE ACCESS AND IMPACT",
            "ANSWER AUDITED PYQS WITHOUT INVENTING OBJECTIVE OR PROVISIONAL KEYS",
            "CONCLUDE ON SAFE AFFORDABLE SCALABLE AND VERIFIED BIOMANUFACTURING",
        ],
    )


TOPIC_13 = _topic_13()
