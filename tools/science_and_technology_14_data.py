"""Authored learner-v2 data for Science and Technology Topic 14."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "http://www.geacindia.gov.in/about-geac-india.aspx - fetched "
        "2026-09-04; substantive GEAC text confirmed its MoEF&CC location "
        "and environmental appraisal role for large-scale use, release and "
        "experimental field trials. It supplied no commercial-cultivation "
        "status for GM mustard."
    ),
    (
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=1842778 - "
        "attempted 2026-09-04; direct retrieval returned HTTP 403. "
        "Official-domain search located the 2022 SDN-1/SDN-2 exemption "
        "release, but no proposition beyond the dated owner evidence was "
        "imported from the blocked page."
    ),
    (
        "https://pib.gov.in/PressReleseDetailm.aspx?PRID=1897008 - attempted "
        "2026-09-04; direct retrieval returned HTTP 403. Official-domain "
        "search located the 7 February 2023 DMH-11 release concerning "
        "environmental release for seed production and testing; it was not "
        "rewritten as commercial cultivation or settled legality."
    ),
    (
        "https://pib.gov.in/PressReleasePage.aspx?PRID=2042234 - attempted "
        "2026-09-04; direct retrieval returned HTTP 403. Official-domain "
        "search located the 6 August 2024 statement that Bt cotton was the "
        "only GM crop approved for commercial cultivation; no 2026 "
        "restatement was inferred."
    ),
    (
        "https://api.sci.gov.in/supremecourt/2004/661/661_2004_11_1501_"
        "54013_Judgement_23-Jul-2024.pdf - fetched 2026-09-04 as an official "
        "PDF; the repository owner's audited split-verdict account remains "
        "the operative boundary. No later order settling DMH-11 legality was "
        "located or inferred."
    ),
    (
        "https://icar.gov.in/en/union-agriculture-minister-shri-shivraj-"
        "singh-chouhan-announces-two-genome-edited-rice-varieties - "
        "attempted 2026-09-04; direct retrieval failed at the transport "
        "layer. The dated owner evidence for the 4 April 2025 announcement "
        "was retained without inferring seed availability or cultivation "
        "area."
    ),
    (
        "https://comments.fssai.gov.in/Bestviewwl.aspx?NOTIFICATION_ID=4128 "
        "- fetched 2026-09-04; substantive draft-regulation text confirmed "
        "Food Authority safety assessment and approval functions and the "
        "separate GEAC environmental-clearance input. Draft text was not "
        "presented as a final notified regulation."
    ),
]


def _topic_14() -> dict[str, object]:
    facts = [
        ("Engineering-breeding boundary", "Genetic engineering deliberately changes genetic material through laboratory methods, whereas conventional hybrid breeding combines parental genomes through sexual crossing; a hybrid is not automatically genetically engineered, although DMH-11 is both a hybrid and transgenic."),
        ("Transgenic-cisgenic-intragenic boundary", "Transgenic constructs use DNA from a sexually incompatible organism, cisgenic constructs transfer an intact gene from the same or a sexually compatible gene pool, and intragenic constructs rearrange regulatory or coding elements from that compatible gene pool; source and construct design must not be merged."),
        ("Bt-cotton mechanism", "Bt cotton expresses cry proteins derived from Bacillus thuringiensis against specified lepidopteran bollworms; insect resistance is distinct from herbicide tolerance, and stacked cry genes delay but do not eliminate resistance evolution or refuge stewardship."),
        ("DMH-11 mechanism-status boundary", "DMH-11 uses the barnase-barstar male-sterility and fertility-restoration system, with bar as a selectable marker, to enable mustard hybridisation; reviewed official material concerns conditional environmental release for seed production and testing, not established commercial cultivation."),
        ("CRISPR targeting boundary", "In CRISPR-Cas9 editing, a guide RNA provides sequence recognition, Cas9 is the nuclease, and cleavage requires an adjacent PAM such as NGG for commonly used SpCas9; guide matching without a compatible PAM does not establish cutting."),
        ("Repair-outcome boundary", "A Cas9 double-strand break is repaired mainly by error-prone non-homologous end joining, which creates small insertions or deletions, or by homology-directed repair using a donor template for a defined substitution or insertion; the repair route determines the edit."),
        ("Base-prime editing boundary", "Base editing chemically converts a target base without a double-strand break, while prime editing uses a reverse-transcriptase-linked editor and prime-editing guide RNA to write a specified short change; neither should be described as ordinary NHEJ."),
        ("SDN-category boundary", "SDN-1 makes a template-free small edit, SDN-2 uses a short homologous template for a defined small change, and SDN-3 inserts a gene-sized sequence at a targeted site; SDN-3 DNA may be cisgenic or transgenic and remains outside India's lighter exemption."),
        ("Six-tier biosafety architecture", "The Rules, 1989 create a six-tier structure: RDAC advises, IBSC oversees work within institutions, RCGM reviews research and contained activity, GEAC appraises environmental release and large-scale use, and SBCC plus DLC monitor at state and district levels."),
        ("GEAC-RCGM-FSSAI split", "RCGM under DBT addresses research and contained stages, GEAC under MoEF&CC appraises environmental release, and FSSAI addresses food-safety assessment, approval and labelling under the food-law track; no one body substitutes for the others."),
        ("Rules-1989 boundary", "The Manufacture, Use, Import, Export and Storage of Hazardous Micro-organisms, Genetically Engineered Organisms or Cells Rules, 1989 under the Environment Protection Act, 1986 are India's core GMO biosafety framework, not a crop-commercialisation certificate."),
        ("2022 exemption-guideline boundary", "MoEF&CC's 30 March 2022 office memorandum exempted SDN-1 and SDN-2 genome-edited plants free of exogenously introduced DNA from Rules 7 to 11, while DBT's 17 May 2022 safety-assessment guidelines and related oversight still preserve category and biosafety checks."),
        ("Bt-brinjal moratorium boundary", "The 9 February 2010 Bt brinjal decision was a moratorium pending further independent long-term safety evidence, not a permanent statutory ban, commercial approval or proof that every later GM-food proposal has the same status."),
        ("GM-mustard legal-status boundary", "The Supreme Court delivered a split verdict on 23 July 2024 concerning DMH-11: the judges differed on the challenged approvals and the divided issue was placed before the Chief Justice for an appropriate Bench; commercial cultivation and settled legality must not be claimed."),
        ("Genome-edited-rice status", "ICAR announced DRR Rice 100 Kamla and Pusa DST Rice 1 on 4 April 2025 as genome-edited rice varieties developed without adding foreign DNA; announcement of varieties does not establish seed availability, cultivated area or farmer outcomes."),
        ("Resistance-and-refuge mechanism", "Continuous selection pressure can increase resistant pest alleles, so structured refuges preserve susceptible insects and gene stacking can slow resistance; Bt technology does not make resistance management unnecessary."),
        ("Gene-flow and non-target mechanism", "Pollen or seed movement can transfer traits to compatible relatives or neighbouring crops, while exposure pathways may affect non-target organisms; risk assessment must examine crop biology, receiving environment and trait rather than treating every event identically."),
        ("Off-target-characterisation boundary", "CRISPR off-target changes arise when a nuclease acts at sufficiently similar sequences; guide design, high-fidelity enzymes, segregation and sequencing can reduce or identify them, but targeted editing is not synonymous with consequence-free editing."),
        ("Farmer-livelihood boundary", "Biotechnology can affect yield stability, pesticide exposure, labour, seed cost, resistance management and market access, so farmer welfare depends on trait performance, stewardship, extension, competition and local agro-ecology rather than the technique label alone."),
        ("Approval-monitoring firewall", "Laboratory result, contained research permission, confined field trial, environmental release, food approval, crop-variety release, seed availability, commercial cultivation and post-release monitoring are separate evidence rungs that require their own dated authorities."),
    ]
    traps = [
        "Do not treat hybrid, transgenic, cisgenic and intragenic as synonyms.",
        "Do not describe Bt insect resistance as herbicide tolerance.",
        "Do not call bar the agronomic purpose of DMH-11.",
        "Do not omit guide RNA, Cas9 or PAM from CRISPR targeting.",
        "Do not claim NHEJ produces a chosen precise substitution.",
        "Do not merge base editing or prime editing with double-strand-break repair.",
        "Do not extend the 2022 exemption to SDN-3 or edits retaining exogenous DNA.",
        "Do not place GEAC under DBT or give RCGM environmental-release authority.",
        "Do not make FSSAI the environmental biosafety regulator.",
        "Do not turn the Rules, 1989 into proof of commercial approval.",
        "Do not call the Bt brinjal moratorium a permanent ban.",
        "Do not claim GM mustard commercial cultivation or settled legality.",
        "Do not convert announced genome-edited rice varieties into cultivation totals.",
        "Do not claim targeted editing eliminates off-target or ecological questions.",
        "Do not infer farmer livelihood gains from laboratory efficacy alone.",
    ]
    titles = [
        "Genetic engineering conventional breeding and hybrid boundaries",
        "Transgenic cisgenic intragenic and construct-source distinctions",
        "Bt cotton cry proteins resistance and refuge stewardship",
        "DMH-11 barnase barstar hybridisation and status",
        "CRISPR guide RNA Cas9 PAM and target recognition",
        "NHEJ HDR base editing and prime editing",
        "SDN-1 SDN-2 SDN-3 and exogenous-DNA classification",
        "Rules 1989 and the six-tier biosafety architecture",
        "RCGM GEAC FSSAI and crop-release role separation",
        "The 2022 exemption and genome-edited plant guidelines",
        "Bt brinjal moratorium and decision-status vocabulary",
        "GM mustard split verdict and unsettled legal position",
        "Genome-edited rice and announcement-to-adoption ladder",
        "Gene flow non-target effects off-target edits and monitoring",
        "Farmer livelihoods PYQ synthesis and approval firewall",
    ]
    routes = [
        "Define the intervention before assigning a legal or biological category.",
        "Classify DNA source and construct architecture separately.",
        "Trace cry expression to pest specificity, resistance and refuge.",
        "Explain hybridisation purpose before stating the bounded approval status.",
        "Follow recognition from guide RNA through PAM-dependent Cas9 cleavage.",
        "Map each repair or editing tool to its actual molecular outcome.",
        "Use template, edit size and foreign-DNA status to classify SDN outcomes.",
        "Map all six institutions from advice and laboratory oversight to monitoring.",
        "Separate research, environmental, food-safety and agronomic decisions.",
        "Quote the exact categories, dates and Rules 7 to 11 boundary.",
        "Use moratorium, ban and approval as non-interchangeable status terms.",
        "State both judicial positions and conclude that the issue is unresolved.",
        "Separate variety announcement from seed access, cultivation and impact.",
        "Organise biosafety by exposure pathway, evidence and mitigation.",
        "Link trait performance to costs, institutions, markets and farmer choice.",
    ]
    panels = [
        panel("Breeding and engineering taxonomy", "branch-map", [
            "CONVENTIONAL CROSS -> parental genomes recombine sexually",
            "HYBRID -> offspring of selected parental lines",
            "TRANSGENIC -> sexually incompatible donor DNA",
            "CISGENIC -> intact compatible-pool gene",
            "INTRAGENIC -> rearranged compatible-pool elements",
        ], [facts[0][0], facts[1][0]]),
        panel("Bt cotton mechanism and stewardship", "causal-chain", [
            "CRY GENE -> plant expresses Bt protein",
            "SPECIFIC BOLLWORM FEEDING -> toxic action in susceptible larvae",
            "SELECTION PRESSURE -> resistant alleles can increase",
            "REFUGE + STACKING -> slow resistance evolution",
            "TRAP -> insect resistance is not herbicide tolerance",
        ], [facts[2][0], facts[15][0]]),
        panel("DMH-11 construct and status", "systems-map", [
            "BARNASE -> male sterility in one parent",
            "BARSTAR -> fertility restoration in hybrid",
            "BAR -> selectable marker",
            "PURPOSE -> enable hybridisation in mustard",
            "STATUS -> no commercial-cultivation or settled-legality claim",
        ], [facts[3][0], facts[13][0]]),
        panel("CRISPR targeting rail", "process-flow", [
            "GUIDE RNA -> sequence recognition",
            "TARGET DNA + PAM -> permitted binding context",
            "CAS9 -> double-strand cleavage",
            "CELLULAR REPAIR -> creates final edit",
            "RULE -> targeting tool and repair outcome are distinct",
        ], [facts[4][0], facts[5][0]]),
        panel("Editing-outcome matrix", "comparison-table", [
            "NHEJ -> template-free indels and knockout",
            "HDR -> donor-template substitution or insertion",
            "BASE EDITING -> chemical base conversion without DSB",
            "PRIME EDITING -> templated short writing without DSB",
            "TRAP -> precision mechanisms are not interchangeable",
        ], [facts[5][0], facts[6][0]]),
        panel("SDN classification ladder", "status-ladder", [
            "SDN-1 -> no template; small edit",
            "SDN-2 -> short template; defined small edit",
            "SDN-3 -> gene-sized targeted insertion",
            "2022 LIGHTER TRACK -> SDN-1/2 free of exogenous DNA",
            "FULL SCRUTINY -> SDN-3 remains outside exemption",
        ], [facts[7][0], facts[11][0]]),
        panel("Six-tier biosafety institution map", "institution-map", [
            "RDAC -> recombinant-DNA advice",
            "IBSC -> institutional day-to-day oversight",
            "RCGM / DBT -> research and contained stages",
            "GEAC / MoEF&CC -> environmental release and large-scale use",
            "SBCC + DLC -> state and district monitoring",
        ], [facts[8][0], facts[9][0]]),
        panel("Law and regulator split", "comparison-table", [
            "RULES 1989 -> core GMO biosafety framework",
            "RCGM -> research / contained work",
            "GEAC -> environmental appraisal",
            "FSSAI -> GM-food safety approval and labelling track",
            "ICAR / CROP SYSTEM -> agronomic evaluation and variety processes",
        ], [facts[9][0], facts[10][0], facts[19][0]]),
        panel("Indian decision timeline", "timeline", [
            "09 FEB 2010 -> Bt brinjal moratorium",
            "30 MAR 2022 -> SDN-1/2 exemption OM",
            "17 MAY 2022 -> DBT genome-edited plant guidelines",
            "23 JUL 2024 -> Supreme Court DMH-11 split verdict",
            "04 APR 2025 -> two genome-edited rice varieties announced",
        ], [facts[11][0], facts[12][0], facts[13][0], facts[14][0]]),
        panel("Biosafety mechanism map", "causal-chain", [
            "TARGET PEST PRESSURE -> resistance evolution",
            "POLLEN / SEED MOVEMENT -> gene-flow exposure",
            "TRAIT EXPRESSION -> non-target exposure pathway",
            "SIMILAR DNA SITES -> possible off-target edit",
            "RESPONSE -> characterisation, mitigation and monitoring",
        ], [facts[15][0], facts[16][0], facts[17][0]]),
        panel("Farmer-livelihood evaluation", "answer-spine", [
            "TRAIT -> intended agronomic constraint",
            "FIELD PERFORMANCE -> yield stability and input effect",
            "FARM ECONOMICS -> seed cost, labour, pesticide and risk",
            "INSTITUTIONS -> extension, competition, stewardship and markets",
            "VERDICT -> context-specific welfare, not technique determinism",
        ], [facts[18][0]]),
        panel("Approval and claim firewall", "status-ladder", [
            "LAB RESULT -> bounded molecular proposition",
            "CONTAINED / FIELD PERMISSION -> trial stage",
            "ENVIRONMENTAL / FOOD APPROVAL -> separate regulators",
            "VARIETY RELEASE / SEED ACCESS / CULTIVATION -> separate evidence",
            "POST-RELEASE MONITORING -> resistance, ecology and farmer outcomes",
        ], [facts[19][0], facts[3][0], facts[14][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts, "2018", "Prelims GS-I",
            "Assess the routed statements on Indian GM mustard genes and properties together with CRISPR-Cas9 classification.",
            "Audited routed objective demands covering 2018 Q63 and the CRISPR portion of Q64; the official key is unavailable locally, so no option or answer letter is asserted.",
            [3, 4, 13],
        ),
        common.make_pyq_solution(
            facts, "2019", "Prelims GS-I",
            "Assess the routed concepts of artificial chromosomes, RNA interference and Cas9 function in molecular biology.",
            "Representative routed card covering 2019 Q93, Q96 and Q99; it distinguishes related molecular tools without asserting an objective answer key.",
            [4, 5, 6, 19],
        ),
        common.make_pyq_solution(
            facts, "2019", "GS-III",
            "Discuss how biotechnology applications can improve farmers' living standards.",
            "Verified routed Mains demand, 15 marks and 250 words; the model route evaluates trait, field performance, costs, stewardship, markets and qualification rather than promising automatic gains.",
            [2, 15, 18, 19],
        ),
    ]
    return common.topic(
        14,
        "Genetic Engineering: GM Crops and CRISPR",
        "14_Genetic-Engineering-GM-Crops-and-CRISPR",
        facts,
        traps,
        [
            (10, "Distinguish transgenic, cisgenic, intragenic and hybrid crops.", [0, 1, 3]),
            (10, "Explain CRISPR-Cas9 targeting and the role of guide RNA, Cas9 and PAM.", [4, 5]),
            (15, "Compare NHEJ, HDR, base editing, prime editing and SDN categories.", [5, 6, 7, 11]),
            (15, "Map India's six-tier biosafety architecture and separate GEAC, RCGM and FSSAI roles.", [8, 9, 10, 19]),
            (20, "Critically examine India's regulation of GM crops and genome-edited plants after the 2022 exemption.", [7, 9, 10, 11, 12, 13, 19]),
            (20, "Evaluate agricultural biotechnology through Bt cotton, DMH-11, genome-edited rice, biosafety and farmer livelihoods.", [2, 3, 13, 14, 15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "genetic engineering", "hybrid", "transgenic", "cisgenic",
            "intragenic", "Bt cotton", "cry protein", "refuge",
            "DMH-11", "barnase", "barstar", "bar", "guide RNA", "Cas9",
            "PAM", "NHEJ", "HDR", "base editing", "prime editing", "SDN-1",
            "SDN-2", "SDN-3", "RDAC", "IBSC", "RCGM", "GEAC", "SBCC",
            "DLC", "FSSAI", "Rules 1989", "Rules 7 to 11",
            "Bt brinjal moratorium", "split verdict", "genome-edited rice",
            "gene flow", "off-target", "farmer livelihoods",
        ],
        "Audited ledgers route the 2018 GM-mustard and CRISPR objective demands, the 2019 artificial-chromosome, RNA-interference and Cas9 demands, and the 2019 GS-III farmer-livelihood question to this owner. Three representative cards preserve those routes; no objective answer key or option letter is supplied.",
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        "Official-source attempts on 2026-09-04 confirm GEAC's environmental role and preserve dated boundaries for the 2022 exemption, Bt cotton, Bt brinjal, DMH-11 litigation, genome-edited rice and draft GM-food regulation. GM mustard is not described as commercially cultivated or legally settled.",
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
        ],
        register_headings=(
            "GENETIC-INTERVENTION AND EDITING-MECHANISM MAP",
            "CROP, BIOSAFETY AND LEGAL-STATUS FIREWALLS",
            "GM AND GENE-EDITING ANSWER SPINE",
            "INDIAN DECISIONS, PYQ ROUTES AND LIVE-SOURCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE GENETIC ENGINEERING AND SEPARATE HYBRID TRANSGENIC CISGENIC INTRAGENIC",
            "TRACE BT CRY ACTION OR GUIDE RNA PAM CAS9 AND REPAIR",
            "CLASSIFY NHEJ HDR BASE PRIME AND SDN-1 SDN-2 SDN-3",
            "MAP RDAC IBSC RCGM GEAC SBCC DLC AND FSSAI",
            "STATE RULES 1989 AND THE EXACT 2022 EXEMPTION",
            "USE BT COTTON DMH-11 BT BRINJAL AND GENOME-EDITED RICE WITH DATED STATUS",
            "TEST GENE FLOW NON-TARGET OFF-TARGET RESISTANCE AND FARMER-LIVELIHOOD EFFECTS",
            "CONCLUDE WITH TRAIT-SPECIFIC REVIEW MONITORING TRANSPARENCY AND FARMER CHOICE",
        ],
    )


TOPIC_14 = _topic_14()
