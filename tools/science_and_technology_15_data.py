"""Authored learner-v2 data for Science and Technology Topic 15."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://cdsco.gov.in/opencms/opencms/en/Acts-and-rules/New-Drugs/ "
        "- fetched 2026-09-04; the official CDSCO page listed the New Drugs "
        "and Clinical Trials Rules, 2019 and subsequent amendments. It "
        "supports the trial-and-new-drug framework but was not used to infer "
        "approval, efficacy, safety or present availability of any product."
    ),
    (
        "https://cdsco.gov.in/opencms/opencms/en/biologicals/Vaccines/ - "
        "fetched 2026-09-04; the official page identified CDSCO as India's "
        "National Regulatory Authority and exposed vaccine guidance material. "
        "No product-specific approval, trial result or procurement status was "
        "imported from the page."
    ),
    (
        "https://cdsco.gov.in/opencms/resources/UploadCDSCOWeb/2018/"
        "UploadAlertsFiles/BiosimilarGuideline2016.pdf - official-domain "
        "search and retrieval attempted 2026-09-04; the joint CDSCO-DBT "
        "Guidelines on Similar Biologics, 2016 were located. The dated "
        "comparability framework was retained without assuming that every "
        "biologic copy is approved, interchangeable or currently marketed."
    ),
    (
        "https://birac.nic.in/cfp_view.php?id=67&scheme_type=37 - fetched "
        "2026-09-04; the official BIRAC page confirmed DBT's Mission COVID "
        "Suraksha and BIRAC's Mission Implementation Unit role, including "
        "support for clinical-development and testing capacity. Historical "
        "call language was not converted into a current product approval, "
        "manufacturing output, procurement total or access outcome."
    ),
    (
        "https://birac.nic.in/desc_new.php?id=89 - fetched 2026-09-04; the "
        "official mandate page identified BIRAC as a DBT-set-up not-for-profit "
        "Section 8, Schedule B public sector enterprise and industry-academia "
        "interface. Translation support was not rewritten as regulation or "
        "proof of company, product or commercial success."
    ),
    (
        "https://ipc.gov.in/PvPI/about.html - fetched 2026-09-04; the page "
        "returned only a sparse legacy shell. Official-domain search located "
        "IPC Pharmacovigilance Programme of India reporting, guidance and "
        "safety-alert pages, but no adverse-event count, causal conclusion or "
        "product-specific safety claim was imported."
    ),
    (
        "https://dbtindia.gov.in/regulations-guidelines/guidelines - "
        "attempted 2026-09-04; DNS resolution failed. No DBT guideline text "
        "or current institutional claim was reconstructed from the failed "
        "request; the repository owner's dated DBT boundaries were preserved."
    ),
]


def _topic_15() -> dict[str, object]:
    facts = [
        (
            "Antigen-antibody boundary",
            "An antigen is a molecular structure recognised by an antibody or "
            "T-cell receptor, while an antibody is a B-cell-lineage "
            "immunoglobulin that binds a specific epitope; antigen, immunogen, "
            "antibody and pathogen are related but non-interchangeable terms.",
        ),
        (
            "Active-passive-antiviral boundary",
            "Vaccination presents antigen or antigen instructions so the "
            "recipient develops active immunity and memory, whereas a "
            "monoclonal antibody supplies a ready-made targeted protein for "
            "passive prophylaxis or therapy; an antiviral instead inhibits a "
            "step of viral replication.",
        ),
        (
            "Adaptive-immune mechanism",
            "Antigen presentation activates appropriate lymphocytes; B cells "
            "can become antibody-secreting plasma cells and memory B cells, "
            "while helper and cytotoxic T-cell functions support or execute "
            "cellular responses. Antibody titre alone is not the whole immune "
            "response or a universal correlate of protection.",
        ),
        (
            "Whole-pathogen platform boundary",
            "Live-attenuated vaccines use a weakened replicating organism and "
            "inactivated vaccines use a killed organism; both expose multiple "
            "antigens, but attenuation, replication, contraindications, "
            "boosting and manufacture must not be treated as identical.",
        ),
        (
            "Subunit-toxoid-VLP-conjugate boundary",
            "Subunit vaccines present selected components, toxoids present "
            "inactivated bacterial toxins, virus-like particles are "
            "non-infectious protein assemblies without a viral genome, and "
            "conjugate vaccines link a weak polysaccharide antigen to a protein "
            "carrier to strengthen T-cell-dependent response and memory.",
        ),
        (
            "Vector-mRNA-DNA boundary",
            "A recombinant viral vector delivers antigen code through an "
            "engineered carrier, mRNA is translated in the cytoplasm after "
            "delivery such as by lipid nanoparticles, and DNA must reach the "
            "nucleus for transcription; all induce active immunity but their "
            "delivery, stability and manufacturing implications differ.",
        ),
        (
            "Adjuvant-and-formulation boundary",
            "An adjuvant enhances or shapes an immune response to antigen, "
            "whereas stabilisers, preservatives and delivery systems perform "
            "different formulation functions; the presence of an adjuvant "
            "does not itself establish efficacy, safety or duration.",
        ),
        (
            "Monoclonal-antibody mechanism",
            "A monoclonal antibody is selected for binding to one epitope or "
            "defined target and can neutralise, block signalling, recruit "
            "immune effector functions or carry a payload; targeted binding "
            "does not guarantee clinical benefit or absence of adverse effects.",
        ),
        (
            "Hybridoma-recombinant-production boundary",
            "Classical hybridoma technology fuses an antibody-producing B cell "
            "with an immortal myeloma cell to create a clone, while modern "
            "therapeutic antibodies are commonly sequence-engineered and "
            "expressed in recombinant mammalian cell culture; discovery clone, "
            "production cell line and final medicine are separate stages.",
        ),
        (
            "Antibody-engineering boundary",
            "Chimeric, humanised and fully human antibodies describe different "
            "degrees or routes of human-sequence content intended partly to "
            "manage immunogenicity; suffix conventions are historical naming "
            "aids, not proof of mechanism, safety, approval or effectiveness.",
        ),
        (
            "Biopharma-manufacturing chain",
            "Biologics manufacture proceeds through cell-bank and raw-material "
            "control, upstream culture or fermentation, harvest, downstream "
            "purification, formulation, sterile fill-finish, testing and batch "
            "release; process control is part of product quality because living "
            "systems generate complex and variable molecules.",
        ),
        (
            "Quality-and-scale-up boundary",
            "Identity, purity, potency, sterility, contamination control, "
            "consistency and validated storage are distinct quality dimensions; "
            "laboratory expression, pilot production, validated commercial "
            "manufacture and released batches are separate capability rungs.",
        ),
        (
            "Cold-chain boundary",
            "Cold chain is temperature-controlled storage and transport from "
            "manufacturer through delivery, supported by monitoring and "
            "contingency systems; a platform's nominal storage range alone does "
            "not establish last-mile integrity, coverage, equity or field impact.",
        ),
        (
            "Clinical-development ladder",
            "Preclinical studies precede human trials; Phase I primarily examines "
            "initial safety and dose, Phase II expands dose, safety and immune or "
            "therapeutic evidence, Phase III tests benefit and safety in larger "
            "populations, and Phase IV/post-marketing surveillance follows "
            "authorised use. Phase labels do not substitute for protocol details.",
        ),
        (
            "CDSCO-NDCTR boundary",
            "CDSCO under the Ministry of Health and Family Welfare is India's "
            "national drug regulatory authority, with the DCGI/Central Licensing "
            "Authority operating under the Drugs and Cosmetics framework and "
            "NDCTR 2019 for new drugs and clinical trials; regulator review is "
            "distinct from research, funding, procurement and immunisation delivery.",
        ),
        (
            "DBT-BIRAC-ICMR boundary",
            "DBT provides biotechnology policy, mission and research support, "
            "BIRAC is the DBT-set-up Section 8 public sector translation and "
            "industry-academia interface, and ICMR is a biomedical research and "
            "evidence institution; none replaces CDSCO's market-approval role.",
        ),
        (
            "Mission-and-policy status boundary",
            "Mission COVID Suraksha was a DBT-led, BIRAC-implemented mission-mode "
            "vaccine-development support architecture, while BioE3 places "
            "precision biotherapeutics in a wider biomanufacturing frame; a "
            "mission, policy, call or supported facility is not a product approval "
            "or evidence of current output and access.",
        ),
        (
            "Biosimilar-generic boundary",
            "A generic small-molecule medicine is expected to be chemically "
            "identical to its reference and can rely heavily on bioequivalence, "
            "whereas a biosimilar is highly similar to a reference biologic and "
            "requires a stepwise comparability exercise across quality and "
            "appropriate non-clinical, clinical and pharmacovigilance evidence.",
        ),
        (
            "Pharmacovigilance-and-AEFI boundary",
            "Pharmacovigilance detects, assesses, understands and helps prevent "
            "adverse effects or other medicine-related problems after and around "
            "use; an adverse event following immunisation is temporally associated "
            "with vaccination but is not automatically caused by the vaccine.",
        ),
        (
            "Efficacy-effectiveness-access firewall",
            "Trial efficacy, real-world effectiveness, regulatory authorisation, "
            "manufacturing capacity, batch release, procurement, availability, "
            "affordability, uptake and population impact are separate evidence "
            "rungs; each product claim needs its own dated authoritative source.",
        ),
    ]
    traps = [
        "Do not merge antigen, immunogen, pathogen, epitope and antibody.",
        "Do not call monoclonal antibodies vaccines or antivirals passive vaccines.",
        "Do not reduce adaptive immunity to antibodies while omitting B-cell memory and T cells.",
        "Do not merge live-attenuated and inactivated vaccine replication or contraindications.",
        "Do not treat subunit, toxoid, VLP and conjugate platforms as synonyms.",
        "Do not say viral-vector, mRNA and DNA vaccines deliver antigen in the same compartment.",
        "Do not treat adjuvant, preservative, stabiliser and delivery vehicle as one ingredient class.",
        "Do not infer clinical benefit merely from monoclonal target binding.",
        "Do not merge hybridoma discovery with recombinant commercial production.",
        "Do not infer safety or approval from chimeric, humanised or fully human naming.",
        "Do not equate laboratory expression, pilot scale and validated batch release.",
        "Do not turn a stated storage range into proof of an intact last-mile cold chain.",
        "Do not treat Phase I, II, III and IV as interchangeable or as automatic approval.",
        "Do not make ICMR, DBT or BIRAC the statutory market-approval authority.",
        "Do not equate efficacy, effectiveness, authorisation, procurement, access and impact.",
    ]
    titles = [
        "Antigens epitopes antibodies immunogens and immune recognition",
        "Active immunity passive antibodies and antiviral distinction",
        "B cells T cells plasma cells and immune memory",
        "Live attenuated and inactivated vaccine platforms",
        "Subunit toxoid VLP and conjugate vaccine logic",
        "Viral vector mRNA DNA delivery and cellular location",
        "Adjuvants formulation and platform choice",
        "Monoclonal antibody targets actions and limits",
        "Hybridoma recombinant cell lines and antibody engineering",
        "Biopharma upstream downstream fill-finish and batch quality",
        "Cold chain monitoring stability and equitable reach",
        "Preclinical Phase I II III IV and regulatory evidence",
        "CDSCO DCGI NDCTR DBT BIRAC ICMR role separation",
        "Biosimilars comparability and pharmacovigilance",
        "Routed PYQs access firewall and biopharma answer spine",
    ]
    routes = [
        "Define each immune object before tracing recognition and response.",
        "Compare who supplies the response, onset, memory and therapeutic purpose.",
        "Trace antigen presentation to humoral, cellular and memory outcomes.",
        "Compare replication state, immune breadth, handling and contraindication logic.",
        "Identify the antigen form and explain why a carrier or adjuvant may be needed.",
        "Follow code delivery to nucleus or cytoplasm, antigen expression and active immunity.",
        "Separate immune enhancement from preservation, stabilisation and delivery.",
        "Move from epitope binding to mechanism, indication evidence and safety limits.",
        "Trace clone creation, sequence engineering, production cell line and purification.",
        "Follow cell bank to upstream culture, downstream purification, fill-finish and release.",
        "Connect stability requirement to monitoring, contingency, last mile and access.",
        "Preserve the purpose of each stage and separate trial evidence from authorisation.",
        "Route research, mission support, translation, regulation and delivery institutions correctly.",
        "Compare reference biologic and similar biologic, then add post-market learning.",
        "Answer audited demands through mechanism, platform, regulation, manufacture and access.",
    ]
    panels = [
        panel("Immune-object recognition map", "concept-map", [
            "PATHOGEN / PRODUCT -> contains or presents ANTIGEN",
            "EPITOPE -> specific recognised part of antigen",
            "B-CELL RECEPTOR / ANTIBODY -> binds epitope",
            "T-CELL RECEPTOR -> recognises presented antigen fragment",
            "IMMUNOGEN -> antigen capable of provoking an immune response",
        ], [facts[0][0], facts[2][0]]),
        panel("Active passive antiviral triad", "three-way-comparison", [
            "VACCINE -> antigen/code -> endogenous response -> memory",
            "mAb -> ready-made antibody -> direct binding -> temporary effect",
            "ANTIVIRAL -> replication-step inhibition -> pharmacological action",
            "ONSET / DURATION / PURPOSE -> compare, never merge",
        ], [facts[1][0], facts[7][0]]),
        panel("Adaptive immunity process rail", "process-rail", [
            "ANTIGEN PRESENTATION -> lymphocyte activation",
            "B CELL -> plasma cell -> antibodies",
            "B / T CELL -> memory populations",
            "HELPER T CELL -> coordination; CYTOTOXIC T CELL -> cellular killing",
            "RULE -> antibody titre is not the entire immune response",
        ], [facts[2][0]]),
        panel("Vaccine platform taxonomy", "branch-matrix", [
            "WHOLE PATHOGEN -> live attenuated | inactivated",
            "SELECTED MATERIAL -> subunit | toxoid | VLP | conjugate",
            "GENETIC CODE -> viral vector | mRNA | DNA",
            "COMPARE -> antigen form | replication | cell location | manufacture",
            "DO NOT IMPORT -> product approval, efficacy or present availability",
        ], [facts[3][0], facts[4][0], facts[5][0]]),
        panel("Genetic-platform cellular map", "cell-compartment-map", [
            "VIRAL VECTOR -> engineered carrier delivers antigen code",
            "mRNA + LNP -> CYTOPLASM -> translation",
            "DNA -> NUCLEUS -> transcription -> mRNA",
            "ANTIGEN EXPRESSION -> B/T response -> memory",
            "TRAP -> active immunity does not mean identical delivery",
        ], [facts[5][0], facts[6][0]]),
        panel("Monoclonal antibody production chain", "assembly-chain", [
            "B CELL + MYELOMA -> HYBRIDOMA CLONE",
            "OR SEQUENCE DISCOVERY -> ANTIBODY ENGINEERING",
            "RECOMBINANT MAMMALIAN CELL LINE -> EXPRESSION",
            "HARVEST -> PURIFICATION -> FORMULATION -> FILL-FINISH",
            "TARGET BINDING != PROVEN CLINICAL BENEFIT",
        ], [facts[7][0], facts[8][0], facts[9][0]]),
        panel("Biopharma manufacturing quality system", "systems-map", [
            "MASTER / WORKING CELL BANK + RAW MATERIAL CONTROL",
            "UPSTREAM -> culture / fermentation / bioreactor",
            "DOWNSTREAM -> capture / purification / clearance",
            "FILL-FINISH -> sterile product and packaging",
            "RELEASE -> identity / purity / potency / sterility / consistency",
        ], [facts[10][0], facts[11][0]]),
        panel("Cold-chain integrity loop", "control-loop", [
            "VALIDATED STORAGE -> monitored transport -> delivery point",
            "DATA LOGGER / INDICATOR -> deviation detection",
            "EXCURSION -> quarantine / assessment / disposition",
            "CONTINGENCY -> power, equipment, route and stock response",
            "OUTCOME -> integrity enables access; it does not prove uptake",
        ], [facts[12][0], facts[19][0]]),
        panel("Clinical and regulatory ladder", "status-ladder", [
            "PRECLINICAL -> laboratory and animal evidence",
            "PHASE I -> initial safety / dose",
            "PHASE II -> expanded dose, safety and response evidence",
            "PHASE III -> larger-population benefit and safety",
            "AUTHORISATION -> MANUFACTURE / RELEASE -> PHASE IV SURVEILLANCE",
        ], [facts[13][0], facts[14][0], facts[18][0]]),
        panel("Indian institution router", "institution-map", [
            "DBT -> biotech policy, missions and research support",
            "BIRAC -> translation, enterprise and mission implementation",
            "ICMR -> biomedical research and evidence",
            "CDSCO / DCGI -> trials and new-drug / biologic regulation",
            "IPC / PvPI -> pharmacovigilance coordination and safety learning",
        ], [facts[14][0], facts[15][0], facts[16][0], facts[18][0]]),
        panel("Biosimilar comparability pyramid", "evidence-pyramid", [
            "FOUNDATION -> extensive analytical and quality comparability",
            "NEXT -> functional and appropriate non-clinical comparison",
            "NEXT -> justified clinical PK/PD, efficacy, safety, immunogenicity",
            "AFTER USE -> pharmacovigilance and traceability",
            "RULE -> BIOSIMILAR != GENERIC != AUTOMATIC INTERCHANGEABILITY",
        ], [facts[17][0], facts[18][0]]),
        panel("Biopharma claim and answer firewall", "answer-spine", [
            "DEFINE -> immune mechanism and product category",
            "CLASSIFY -> platform / mAb / biosimilar",
            "TRACE -> trial + regulation + manufacturing + cold chain",
            "MAP -> CDSCO / DBT / BIRAC / ICMR / PvPI",
            "QUALIFY -> efficacy != effectiveness != approval != access != impact",
        ], [facts[0][0], facts[14][0], facts[15][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2020, 2021 and 2022", "Prelims GS-I",
            "Assess pneumococcal conjugate-vaccine logic, recombinant-vector "
            "vaccine development and the distinctions among mRNA, vector and "
            "inactivated COVID-19 vaccine platforms.",
            "Three audited routed objective demands are consolidated in one "
            "representative card. The locally unavailable official keys are "
            "not reconstructed, and no answer option or letter is asserted.",
            [3, 4, 5, 19],
        ),
        common.make_pyq_solution(
            facts, "2018 and 2022", "GS-III",
            "Discuss biotechnology activity and biopharma-sector benefits in "
            "India, and explain vaccine-development principles and Indian "
            "COVID-19 vaccine approaches.",
            "Two verified routed Mains demands are consolidated in one card. "
            "The route covers mechanism, platform choice, institutions, trial "
            "stages, manufacturing and access without inventing a UPSC model answer.",
            [1, 3, 5, 10, 13, 14, 15, 16, 19],
        ),
        common.make_pyq_solution(
            facts, "2025", "Prelims GS-I",
            "Assess the routed statements concerning monoclonal antibodies.",
            "Representative audited card for 2025 Q48. The official Set-A key "
            "is locally available in the repository, but no answer, option or "
            "letter is recorded or inferred in this authoring file.",
            [7, 8, 9, 17, 19],
        ),
    ]
    return common.topic(
        15,
        "Vaccines, Monoclonal Antibodies and Biopharma",
        "15_Vaccines-Monoclonal-Antibodies-and-Biopharma",
        facts,
        traps,
        [
            (10, "Distinguish antigen, antibody, active immunisation, passive immunisation and antiviral action.", [0, 1, 2]),
            (10, "Compare live-attenuated, inactivated, subunit, toxoid, VLP and conjugate vaccines.", [3, 4, 6]),
            (15, "Explain viral-vector, mRNA and DNA vaccine mechanisms and their delivery and cold-chain implications.", [5, 6, 12]),
            (15, "Trace monoclonal-antibody development from hybridoma or sequence discovery to recombinant manufacture and clinical use.", [7, 8, 9, 10, 11]),
            (20, "Examine India's vaccine and biologics pathway through clinical stages, CDSCO regulation, DBT-BIRAC support and pharmacovigilance.", [13, 14, 15, 16, 18, 19]),
            (20, "Evaluate India's biopharma capability through manufacturing quality, biosimilars, cold chain, affordability, access and status discipline.", [10, 11, 12, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "antigen", "epitope", "immunogen", "antibody", "B cell",
            "plasma cell", "memory B cell", "helper T cell", "cytotoxic T cell",
            "active immunisation", "passive immunisation", "antiviral",
            "live-attenuated vaccine", "inactivated vaccine", "subunit vaccine",
            "toxoid", "virus-like particle", "VLP", "conjugate vaccine",
            "polysaccharide", "protein carrier", "adjuvant", "viral vector",
            "mRNA", "lipid nanoparticle", "cytoplasm", "DNA vaccine", "nucleus",
            "monoclonal antibody", "hybridoma", "myeloma", "recombinant",
            "mammalian cell culture", "chimeric", "humanised", "fully human",
            "cell bank", "upstream culture", "bioreactor",
            "downstream purification", "purification", "fill-finish",
            "identity", "purity", "potency", "sterility", "batch release",
            "cold chain", "stability", "preclinical", "Phase I",
            "Phase II", "Phase III", "Phase IV", "CDSCO", "DCGI", "NDCTR 2019",
            "Drugs and Cosmetics", "DBT", "BIRAC", "Section 8", "ICMR",
            "Mission COVID Suraksha", "BioE3", "precision biotherapeutics",
            "biosimilar", "reference biologic", "comparability",
            "pharmacovigilance", "PvPI", "IPC", "AEFI", "immunogenicity",
            "efficacy", "effectiveness", "affordability", "access",
        ],
        (
            "Three representative audited cards cover the 2020 PCV, 2021 "
            "recombinant-vector and 2022 COVID-platform objective demands; the "
            "2018 biopharma and 2022 vaccine-development GS-III demands; and "
            "the 2025 monoclonal-antibody objective demand. No unavailable "
            "objective key is invented, and the available 2025 key is not "
            "recorded or inferred."
        ),
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        (
            "Official CDSCO, BIRAC, IPC/PvPI and DBT pages were fetched, "
            "searched or attempted on 2026-09-04. They preserve the NDCTR "
            "framework, CDSCO regulatory role, BIRAC translation and Mission "
            "COVID Suraksha implementation role, similar-biologics framework "
            "and pharmacovigilance boundary. They do not establish current "
            "product approvals, efficacy, trial outcomes, batch output, "
            "procurement, availability, price, coverage or population impact."
        ),
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
            "basic/13_Biotechnology-Fundamentals-and-DBT-Missions.md",
            "advanced/13_Biotechnology-Fundamentals-and-DBT-Missions.md",
            "basic/23_General-Science-Biology-and-Physiology.md",
            "advanced/23_General-Science-Biology-and-Physiology.md",
        ],
        register_headings=(
            "IMMUNE RECOGNITION AND VACCINE-PLATFORM MAP",
            "MONOCLONAL-ANTIBODY AND BIOPHARMA-MANUFACTURING CHAIN",
            "TRIAL, REGULATOR, BIOSIMILAR AND SAFETY-SURVEILLANCE FIREWALL",
            "COLD-CHAIN, ACCESS, PYQ AND STATUS-DISCIPLINE SPINE",
        ),
        register_answer_spine=[
            "DEFINE ANTIGEN EPITOPE ANTIBODY IMMUNOGEN AND PATHOGEN",
            "SEPARATE ACTIVE VACCINATION PASSIVE mAb AND ANTIVIRAL ACTION",
            "TRACE ANTIGEN PRESENTATION B CELLS T CELLS PLASMA CELLS AND MEMORY",
            "CLASSIFY LIVE INACTIVATED SUBUNIT TOXOID VLP CONJUGATE VECTOR mRNA DNA",
            "LOCATE mRNA IN CYTOPLASM AND DNA TRANSCRIPTION IN NUCLEUS",
            "TRACE HYBRIDOMA OR SEQUENCE DISCOVERY TO RECOMBINANT CELL CULTURE",
            "MAP CELL BANK UPSTREAM DOWNSTREAM FILL-FINISH TESTING AND RELEASE",
            "CONNECT COLD-CHAIN MONITORING TO LAST-MILE INTEGRITY AND ACCESS",
            "SEQUENCE PRECLINICAL PHASE I II III AUTHORISATION AND PHASE IV",
            "ROUTE CDSCO DCGI DBT BIRAC ICMR IPC AND PvPI BY FUNCTION",
            "DISTINGUISH BIOSIMILAR COMPARABILITY FROM GENERIC BIOEQUIVALENCE",
            "SEPARATE AEFI TEMPORAL ASSOCIATION FROM CAUSAL ATTRIBUTION",
            "CONCLUDE EFFICACY EFFECTIVENESS APPROVAL CAPACITY ACCESS AND IMPACT ARE DISTINCT",
        ],
    )


TOPIC_15 = _topic_15()
