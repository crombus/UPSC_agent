"""Authored learner-v2 data for Science and Technology Topic 26."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://www.nobelprize.org/prizes/physics/2025/press-release/ and "
        "https://www.nobelprize.org/prizes/physics/2025/clarke/facts/ - fetched "
        "2026-09-04; official pages confirmed the laureates, 7 October 2025 "
        "citation, superconducting-circuit mechanism, John Clarke's birthplace "
        "and award-time affiliation. Opportunities for quantum technologies "
        "were not rewritten as a commercial computer, deployment or policy result."
    ),
    (
        "https://www.nobelprize.org/prizes/chemistry/2025/press-release/ - "
        "fetched 2026-09-04; the official release confirmed Susumu Kitagawa, "
        "Richard Robson and Omar M. Yaghi and the citation for development of "
        "metal-organic frameworks. Listed possible uses were retained as "
        "material capabilities or applications, not proven commercialization."
    ),
    (
        "https://www.nobelprize.org/prizes/medicine/2025/press-release/ - "
        "fetched 2026-09-04; the official release confirmed Mary E. Brunkow, "
        "Fred Ramsdell and Shimon Sakaguchi and the citation concerning "
        "peripheral immune tolerance. Regulatory T cells, Foxp3 and clinical-"
        "trial references were not converted into approved therapies or outcomes."
    ),
    (
        "https://www.nobelprize.org/prizes/medicine/2024/press-release/ - "
        "fetched 2026-09-04; the official release confirmed Victor Ambros and "
        "Gary Ruvkun and the citation for microRNA and post-transcriptional "
        "gene regulation. Discovery significance was kept separate from a "
        "diagnostic, medicine, commercial product or public-health outcome."
    ),
    (
        "https://www.nobelprize.org/prizes/physics/1930/raman/facts/ - fetched "
        "2026-09-04; the official page confirmed C. V. Raman's prize, Calcutta "
        "University affiliation, scattering-of-light citation and Raman-effect "
        "mechanism. Later analytical use was not inserted into the citation."
    ),
    (
        "https://www.nobelprize.org/prizes/medicine/1968/khorana/facts/ and "
        "https://www.nobelprize.org/prizes/chemistry/2009/ramakrishnan/facts/ - "
        "fetched 2026-09-04; official pages confirmed Har Gobind Khorana's "
        "genetic-code citation and Venkatraman Ramakrishnan's ribosome citation, "
        "with their award-time affiliations. Birthplace, affiliation, field and "
        "national identity were not collapsed into one biographical label."
    ),
]


def _topic_26() -> dict[str, object]:
    facts = [
        (
            "Minimum prize evidence card",
            "A reliable prize card records exact prize category and year, official laureate spelling, official motivation or citation, plain-language mechanism, birthplace only when stated, award-time affiliation, direct India link if sourced and verification date. A remembered field, employer or popular headline cannot replace any missing field.",
        ),
        (
            "Discovery invention theory and observation",
            "A theory explains and predicts, an observation records a phenomenon, an experiment tests under controlled conditions, a discovery establishes a phenomenon or relation, and an invention creates a device or process. A Nobel citation may recognise a discovery, development or method, so the awarded verb and object must be preserved exactly.",
        ),
        (
            "Nobel category architecture",
            "The Nobel categories connect Physics, Chemistry, Physiology or Medicine, Literature and Peace to Alfred Nobel's original framework, while the Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel was established later. Awarding institutions differ, and Peace can recognise organisations; the word Nobel alone does not establish category, recipient type or scientific field.",
        ),
        (
            "Laureate institution nationality boundary",
            "Birthplace, citizenship or nationality, education, research location and affiliation at the time of award are different biographical facts. A prize can be shared among laureates at different institutions, and an institution supplies a research environment without becoming an automatic co-recipient or author of every contribution.",
        ),
        (
            "Citation-to-policy evidence ladder",
            "The official citation identifies the awarded contribution; the underlying discovery explains the mechanism; a possible application shows technical relevance; engineering validation tests reproducibility and performance; commercialization requires production and adoption; and a policy outcome requires measured social effect. None of these rungs proves the next.",
        ),
        (
            "Chronology and attribution discipline",
            "Scientific progress often spans prior theory, enabling instruments, decisive experiments, independent replication and later engineering by many teams. Prize year is the award year rather than automatically the discovery, publication, patent, product or deployment year; credit should follow the specific official citation and named contribution.",
        ),
        (
            "Replication uncertainty and mature evidence",
            "A single result, preprint, company announcement or prize does not eliminate measurement error, boundary conditions or scaling constraints. Strong scientific reasoning asks whether the effect was independently reproduced, whether alternative explanations were tested, what population or operating range applies and which institution verified each later claim.",
        ),
        (
            "Physics 2025 award citation",
            "The 2025 Nobel Prize in Physics was awarded to John Clarke, Michel H. Devoret and John M. Martinis for the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit. The official award date was 7 October 2025, and the citation is narrower than the broad label quantum computing.",
        ),
        (
            "Physics 2025 mechanism",
            "The laureates used a superconducting electrical circuit with a Josephson junction and showed a collective macroscopic state escaping a zero-voltage condition through quantum tunnelling and absorbing or emitting specific energy amounts. The experiment demonstrated macroscopic quantum behaviour; it did not itself constitute a fault-tolerant general-purpose quantum computer.",
        ),
        (
            "John Clarke biographical route",
            "The official facts page records John Clarke as born in Cambridge, United Kingdom, in 1942 and affiliated at the time of the award with the University of California, Berkeley. Birthplace and United States institutional affiliation are separate clues, while his one-third prize share identifies neither sole authorship nor nationality.",
        ),
        (
            "Chemistry 2025 award citation",
            "The 2025 Nobel Prize in Chemistry was awarded on 8 October 2025 to Susumu Kitagawa, Richard Robson and Omar M. Yaghi for the development of metal-organic frameworks. The citation concerns a material architecture, not one environmental policy, company, product or country.",
        ),
        (
            "Metal-organic framework mechanism",
            "Metal-organic frameworks use metal ions as nodes linked by organic molecules into porous crystalline structures with cavities; changing building blocks can tune capture, storage, transport, catalysis or conductivity. Official examples include water harvesting, carbon-dioxide capture, toxic-gas storage and chemical reactions, but capability does not prove scale, lifecycle benefit or commercial deployment.",
        ),
        (
            "Medicine 2025 award citation",
            "The 2025 Nobel Prize in Physiology or Medicine was awarded on 6 October 2025 to Mary E. Brunkow, Fred Ramsdell and Shimon Sakaguchi for discoveries concerning peripheral immune tolerance. The contribution concerns how the immune system is kept from attacking the body's own tissues.",
        ),
        (
            "Peripheral tolerance mechanism",
            "Shimon Sakaguchi identified regulatory T cells, while Brunkow and Ramsdell linked autoimmune vulnerability to Foxp3 and Sakaguchi connected Foxp3 to regulatory-T-cell development. These discoveries explain a control layer beyond central tolerance; references to cancer, autoimmunity or transplantation research and clinical trials do not prove approved treatment or population outcome.",
        ),
        (
            "Medicine 2024 microRNA anchor",
            "The 2024 Nobel Prize in Physiology or Medicine jointly recognised Victor Ambros and Gary Ruvkun for discovery of microRNA and its role in post-transcriptional gene regulation. The mechanism shows that small RNAs can bind complementary messenger RNA and inhibit protein production or promote RNA degradation; it does not turn every RNA association into a therapy.",
        ),
        (
            "Raman prize and mechanism",
            "C. V. Raman received the 1930 Nobel Prize in Physics for work on scattering of light and discovery of the effect named after him, with Calcutta University as award-time affiliation. The Raman effect involves a small fraction of scattered light changing wavelength through energy exchange with molecules and supports material analysis; later use is distinct from the original citation.",
        ),
        (
            "Khorana genetic-code prize",
            "Har Gobind Khorana shared the 1968 Nobel Prize in Physiology or Medicine for interpretation of the genetic code and its function in protein synthesis, with the University of Wisconsin as award-time affiliation and Raipur, India, as birthplace on the official page. His experimental contribution used constructed RNA chains to help map codons to amino acids.",
        ),
        (
            "Ramakrishnan ribosome prize",
            "Venkatraman Ramakrishnan shared the 2009 Nobel Prize in Chemistry for studies of the structure and function of the ribosome, with the MRC Laboratory of Molecular Biology in Cambridge as award-time affiliation and Chidambaram, Tamil Nadu, India, as birthplace. X-ray crystallography mapped ribosomal structure; antibiotic relevance is a later application rather than the citation itself.",
        ),
        (
            "Routed PYQ mechanism-first use",
            "The direct 2026 routed demand identifies a 2025 laureate from biographical and professional clues, while the 2018 Bose-Einstein-statistics and 2021 blue-LED Mains demands remain with Topic 21. Topic 26 supplies citation, attribution and discovery-to-application discipline but must not displace the specialist physics explanation.",
        ),
        (
            "Prize claim and current-status firewall",
            "Nomination, announcement, award citation, laureate biography, scientific mechanism, possible application, clinical trial, patent, licensed product, manufacturing scale, market adoption and policy outcome are distinct statuses. The 2026 prizes had not been announced by 4 September 2026, so recent anchors stop at official 2025 awards rather than inventing future laureates.",
        ),
    ]
    traps = [
        "Do not identify a laureate from a remembered field without matching category, year, citation and biography.",
        "Do not use discovery, invention, theory, observation and application as synonyms.",
        "Do not call the Economic Sciences prize one of Alfred Nobel's original five.",
        "Do not infer nationality from birthplace or award-time affiliation.",
        "Do not rewrite a later application into the official prize citation.",
        "Do not treat prize year as automatically the discovery, publication, patent or deployment year.",
        "Do not claim a Nobel Prize proves replication, scale, affordability or policy success.",
        "Do not reduce the 2025 Physics citation to the generic phrase quantum computing.",
        "Do not call the superconducting-circuit experiment a deployed fault-tolerant quantum computer.",
        "Do not infer sole authorship from one laureate's biography in a shared prize.",
        "Do not convert metal-organic-framework capability into commercialization or environmental outcome.",
        "Do not turn peripheral immune tolerance or clinical trials into an approved therapy claim.",
        "Do not turn microRNA association into a diagnostic or medicine without evidence.",
        "Do not collapse Raman, Khorana or Ramakrishnan birthplace, affiliation, category and contribution.",
        "Do not invent 2026 laureates before official announcements.",
    ]
    titles = [
        "Prize evidence cards categories years citations and sources",
        "Discovery invention theory observation experiment and attribution",
        "Laureate birthplace nationality institution affiliation and prize sharing",
        "Citation discovery application commercialization and policy ladder",
        "Chronology replication uncertainty and evidence maturity",
        "Physics 2025 laureates citation and quantum-circuit question",
        "Josephson junction tunnelling and energy quantisation mechanism",
        "John Clarke biography affiliation and 2026 PYQ clue matching",
        "Chemistry 2025 laureates citation and MOF architecture",
        "MOF porosity tunability applications and scale boundary",
        "Medicine 2025 laureates citation and peripheral tolerance",
        "Regulatory T cells Foxp3 central and peripheral tolerance",
        "Medicine 2024 microRNA and post-transcriptional regulation",
        "Raman Khorana Ramakrishnan India-linked evidence cards",
        "Bose-Einstein blue-LED PYQ support and future-award firewall",
    ]
    routes = [
        "Write the exact category, year, spelling, citation, mechanism and award-time affiliation before interpretation.",
        "Identify whether the source recognises explanation, observation, discovery, method, development or invention.",
        "Keep birthplace, citizenship, education, workplace, affiliation and prize share in separate fields.",
        "Move from citation to mechanism, application, engineering, commercialization and measured policy effect without skipping rungs.",
        "Date theory, experiment, replication, award and later technology separately and qualify uncertainty.",
        "Preserve the Physics citation and all three laureates before using the quantum-technology link.",
        "Explain superconductivity, Josephson junction, collective state, tunnelling and quantised energy in sequence.",
        "Match Cambridge birthplace and Berkeley affiliation without treating either as nationality proof.",
        "Preserve the Chemistry citation and distinguish material architecture from one use case.",
        "Connect metal nodes, organic linkers, pores and tunability, then stop before unsupported scale claims.",
        "Preserve the Medicine citation and identify the self-tolerance problem before naming applications.",
        "Trace regulatory T cells and Foxp3 while separating central from peripheral tolerance and trial from approval.",
        "Explain microRNA action after transcription and before protein output without therapeutic overreach.",
        "Build separate prize cards for Raman, Khorana and Ramakrishnan with category, affiliation and mechanism.",
        "Keep direct and cross-owner PYQ routes distinct and stop before unannounced 2026 prizes.",
    ]
    panels = [
        panel("Minimum prize evidence card", "evidence-card", [
            "CATEGORY + YEAR",
            "OFFICIAL LAUREATE SPELLING",
            "OFFICIAL CITATION / MOTIVATION",
            "MECHANISM + AWARD-TIME AFFILIATION",
            "BIRTH / INDIA LINK / STATUS DATE -> only if sourced",
        ], [facts[0][0], facts[3][0]]),
        panel("Scientific contribution classifier", "contribution-tree", [
            "THEORY -> explanation and prediction",
            "OBSERVATION -> recorded phenomenon",
            "EXPERIMENT -> controlled test",
            "DISCOVERY -> established phenomenon or relation",
            "INVENTION / DEVELOPMENT -> device, process or method",
        ], [facts[1][0]]),
        panel("Nobel category map", "category-map", [
            "PHYSICS | CHEMISTRY | PHYSIOLOGY OR MEDICINE",
            "LITERATURE | PEACE -> original framework",
            "ECONOMIC SCIENCES -> later memorial prize",
            "AWARDING INSTITUTION -> category-specific",
            "PEACE -> person or organisation possible",
        ], [facts[2][0]]),
        panel("Citation-to-outcome staircase", "status-staircase", [
            "OFFICIAL CITATION",
            "DISCOVERY / MECHANISM",
            "POSSIBLE APPLICATION",
            "ENGINEERING + COMMERCIALIZATION",
            "MEASURED POLICY / SOCIAL OUTCOME",
        ], [facts[4][0], facts[6][0], facts[19][0]]),
        panel("Attribution and chronology rail", "chronology-rail", [
            "PRIOR THEORY -> INSTRUMENT -> EXPERIMENT",
            "PUBLICATION -> REPLICATION -> AWARD",
            "PATENT / PRODUCT / DEPLOYMENT -> later and separate",
            "LAUREATE != institution",
            "AWARD YEAR != discovery year automatically",
        ], [facts[3][0], facts[5][0]]),
        panel("Physics 2025 quantum-circuit map", "mechanism-map", [
            "SUPERCONDUCTING CIRCUIT + JOSEPHSON JUNCTION",
            "COLLECTIVE MACROSCOPIC STATE",
            "BARRIER -> quantum tunnelling",
            "SPECIFIC ENERGY AMOUNTS -> quantisation",
            "DEMONSTRATION != fault-tolerant quantum computer",
        ], [facts[7][0], facts[8][0]]),
        panel("John Clarke clue resolver", "clue-resolver", [
            "BORN -> Cambridge, United Kingdom",
            "AFFILIATION -> University of California, Berkeley",
            "CATEGORY / YEAR -> Physics 2025",
            "SHARE -> one-third with Devoret and Martinis",
            "MATCH ALL CLUES -> then identify",
        ], [facts[9][0], facts[18][0]]),
        panel("Chemistry 2025 MOF architecture", "material-architecture", [
            "METAL IONS -> nodes",
            "ORGANIC MOLECULES -> linkers",
            "POROUS CRYSTAL -> cavities",
            "BUILDING-BLOCK CHANGE -> tunable function",
            "CAPABILITY / APPLICATION != commercialization",
        ], [facts[10][0], facts[11][0]]),
        panel("Medicine 2025 tolerance pathway", "immune-pathway", [
            "CENTRAL TOLERANCE -> thymic control layer",
            "REGULATORY T CELLS -> peripheral control",
            "Foxp3 -> regulatory-T-cell development",
            "SELF-TISSUE PROTECTION -> mechanism",
            "CLINICAL TRIAL != approved therapy",
        ], [facts[12][0], facts[13][0]]),
        panel("MicroRNA regulation rail", "gene-regulation-rail", [
            "DNA --transcription--> mRNA",
            "microRNA -> complementary mRNA binding",
            "PROTEIN PRODUCTION -> inhibited",
            "mRNA DEGRADATION -> possible route",
            "DISCOVERY != diagnostic or medicine",
        ], [facts[14][0]]),
        panel("India-linked scientist cards", "three-card-grid", [
            "RAMAN 1930 -> light scattering / Raman effect",
            "KHORANA 1968 -> genetic code / protein synthesis",
            "RAMAKRISHNAN 2009 -> ribosome structure and function",
            "BIRTHPLACE != award-time affiliation",
            "CITATION != every later application",
        ], [facts[15][0], facts[16][0], facts[17][0]]),
        panel("PYQ and future-status firewall", "pyq-status-rail", [
            "2026 Q81 -> direct biographical prize route",
            "BOSE-EINSTEIN / BLUE LED -> Topic 21 direct science owner",
            "TOPIC 26 -> attribution + citation + maturity support",
            "2025 OFFICIAL AWARDS -> latest completed science anchors",
            "4 SEP 2026 -> no invented 2026 laureates",
        ], [facts[18][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2026", "Prelims GS-I",
            "Identify the 2025 Nobel Prize recipient by matching biographical and professional clues to the official category, citation and award-time affiliation.",
            "Verified direct routed objective demand covering 2026 Q81; the locally held Set-A key is provisional, so no option, answer letter or inferred key is supplied.",
            [0, 3, 7, 9, 18],
        ),
        common.make_pyq_solution(
            facts, "2018", "GS-III",
            "Use citation and discovery-attribution discipline while discussing the contribution of Bose-Einstein statistics to physics.",
            "Cross-owner supporting card: Topic 21 retains the substantive statistics and physics answer; Topic 26 contributes attribution, chronology and discovery-to-application boundaries without claiming a Nobel citation for the routed concept.",
            [1, 4, 5, 18],
        ),
        common.make_pyq_solution(
            facts, "2021", "GS-III",
            "Explain the everyday-life impact of the blue LED invention recognised by the 2014 Nobel Prize while separating award citation, mechanism, application and outcome.",
            "Cross-owner supporting card: Topic 21 retains semiconductor and LED physics; Topic 26 supplies prize-citation, invention, application and commercialization discipline rather than an official model answer.",
            [1, 4, 5, 6, 18],
        ),
    ]
    return common.topic(
        26,
        "Scientific Discoveries, Nobel Prizes and Scientists",
        "26_Scientific-Discoveries-Nobel-Prizes-and-Scientists",
        facts,
        traps,
        [
            (10, "Explain the minimum evidence needed to identify a Nobel laureate and distinguish biographical clues.", [0, 2, 3]),
            (10, "Distinguish theory, observation, experiment, discovery, invention and development in prize attribution.", [1, 5, 6]),
            (15, "Analyse the 2025 Physics prize through its official citation, superconducting-circuit mechanism and technology boundary.", [7, 8, 9]),
            (15, "Discuss the 2025 Chemistry and Medicine prizes by separating awarded discoveries from possible applications and commercialization.", [10, 11, 12, 13]),
            (20, "Examine how recent Nobel anchors in quantum physics, metal-organic frameworks, immune tolerance and microRNA reveal the path from basic science to application.", [7, 8, 10, 11, 12, 13, 14]),
            (20, "Evaluate discovery attribution and Indian scientific relevance through Raman, Khorana, Ramakrishnan and routed PYQs.", [15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "prize category and year", "official motivation or citation",
            "award-time affiliation", "discovery", "invention", "theory",
            "observation", "experiment", "Sveriges Riksbank Prize",
            "birthplace", "prize share", "commercialization",
            "policy outcome", "replication", "award year",
            "John Clarke", "Michel H. Devoret", "John M. Martinis",
            "macroscopic quantum mechanical tunnelling",
            "energy quantisation in an electric circuit",
            "7 October 2025", "superconducting electrical circuit",
            "Josephson junction", "zero-voltage", "fault-tolerant",
            "University of California, Berkeley", "Susumu Kitagawa",
            "Richard Robson", "Omar M. Yaghi", "8 October 2025",
            "metal-organic frameworks", "metal ions", "organic molecules",
            "porous crystalline", "water harvesting", "carbon-dioxide capture",
            "Mary E. Brunkow", "Fred Ramsdell", "Shimon Sakaguchi",
            "6 October 2025", "peripheral immune tolerance",
            "regulatory T cells", "Foxp3", "central tolerance",
            "clinical trials", "Victor Ambros", "Gary Ruvkun",
            "microRNA", "post-transcriptional gene regulation",
            "C. V. Raman", "Raman effect", "Calcutta University",
            "Har Gobind Khorana", "genetic code", "University of Wisconsin",
            "Venkatraman Ramakrishnan", "ribosome",
            "MRC Laboratory of Molecular Biology", "Bose-Einstein statistics",
            "blue LED", "4 September 2026",
        ],
        "The audited ledgers route 2026 Prelims Q81 directly to this owner. The 2018 Bose-Einstein-statistics and 2021 blue-LED Mains demands remain directly owned by Topic 21 and appear only as cross-owner examples of attribution and citation-to-application discipline. Three representative cards preserve that boundary and reproduce no objective answer.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official Nobel Prize pages checked on 2026-09-04 confirmed completed 2025 Physics, Chemistry and Medicine awards, the 2024 microRNA award and the Raman, Khorana and Ramakrishnan evidence cards. Award citations, mechanisms, possible applications, trials, commercialization and policy outcomes remain explicitly separated; no 2026 laureate or prize outcome was invented before announcement.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "PRIZE CATEGORY, LAUREATE, CITATION AND BIOGRAPHY EVIDENCE CARDS",
            "2025 PHYSICS, CHEMISTRY AND MEDICINE MECHANISM MAP",
            "RAMAN, KHORANA, RAMAKRISHNAN AND MICRO-RNA RAPID RECALL",
            "PYQ ATTRIBUTION, APPLICATION-MATURITY AND FUTURE-AWARD FIREWALL",
        ),
        register_answer_spine=[
            "WRITE CATEGORY YEAR OFFICIAL SPELLING CITATION AND AWARD-TIME AFFILIATION",
            "SEPARATE BIRTHPLACE NATIONALITY EDUCATION WORKPLACE AND PRIZE SHARE",
            "CLASSIFY THEORY OBSERVATION EXPERIMENT DISCOVERY INVENTION OR DEVELOPMENT",
            "DATE DISCOVERY PUBLICATION REPLICATION AWARD PATENT PRODUCT AND DEPLOYMENT SEPARATELY",
            "TRACE CITATION MECHANISM APPLICATION ENGINEERING COMMERCIALIZATION AND POLICY OUTCOME",
            "EXPLAIN PHYSICS 2025 THROUGH SUPERCONDUCTING CIRCUIT JOSEPHSON JUNCTION AND TUNNELLING",
            "EXPLAIN CHEMISTRY 2025 THROUGH METAL NODES ORGANIC LINKERS PORES AND TUNABILITY",
            "EXPLAIN MEDICINE 2025 THROUGH REGULATORY T CELLS Foxp3 AND PERIPHERAL TOLERANCE",
            "LINK MICRO-RNA TO POST-TRANSCRIPTIONAL REGULATION WITHOUT THERAPY OVERREACH",
            "BUILD DISTINCT RAMAN KHORANA AND RAMAKRISHNAN PRIZE CARDS",
            "KEEP BOSE-EINSTEIN AND BLUE-LED SUBSTANTIVE SCIENCE WITH TOPIC 21",
            "STOP AT THE LATEST OFFICIALLY ANNOUNCED PRIZE AND LAST VERIFIED MATURITY RUNG",
        ],
    )


TOPIC_26 = _topic_26()
