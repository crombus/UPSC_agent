"""Authored learner-v2 data for Science and Technology Topic 17."""

from __future__ import annotations

import generate_science_and_technology_common as common
from science_and_technology_data_helpers import panel


LIVE_SOURCE_ATTEMPTS = [
    (
        "https://ipindia.gov.in/basics-of-patents - fetched 2026-09-04; "
        "substantive IP India text confirmed the limited statutory patent "
        "right, product-or-process scope, novelty, inventive step, industrial "
        "application and the section 3/4 exclusion boundary. It supplied no "
        "filing, grant, commercialisation or litigation count."
    ),
    (
        "https://ipindia.gov.in/pages/patents/chapter - fetched 2026-09-04; "
        "the official page identified the Patents Act, 1970 and warned that "
        "Gazette text prevails over the e-version. No unverified amendment "
        "effect, current form deadline or procedural statistic was imported."
    ),
    (
        "https://ipindia.gov.in/storage/uploads/docs-operator/73b5bf10-b04e-"
        "4f45-abef-87ff117315dc.pdf - attempted 2026-09-04; the official PDF "
        "was retrievable only as raw PDF bytes through the live tool. Exact "
        "section propositions are therefore retained only where already "
        "supported by the audited Basic and Advanced owners."
    ),
    (
        "https://www.wipo.int/en/web/pct-system/faqs/faqs - fetched "
        "2026-09-04; substantive WIPO text confirmed that the PCT is an "
        "international application route, publication normally follows the "
        "18-month point, national or regional offices control grant, and "
        "patents remain territorial. No 'world patent' claim was imported."
    ),
    (
        "https://www.wto.org/english/tratop_e/trips_e/intel2_e.htm - fetched "
        "2026-09-04; substantive WTO text confirmed TRIPS minimum standards, "
        "enforcement and WTO dispute-settlement architecture across named IP "
        "fields. TRIPS was not described as a filing office or patent grant."
    ),
    (
        "https://www.tkdl.res.in/tkdl/langdefault/common/Abouttkdl.asp - "
        "attempted 2026-09-04; retrieval failed at the transport layer. The "
        "CSIR-Ministry of Ayush defensive-prior-art proposition is retained "
        "from the audited owner, with no database-size or patent-outcome count."
    ),
]


def _topic_17() -> dict[str, object]:
    facts = [
        (
            "Patent bargain and criteria",
            "A patent is a limited statutory exclusion granted in exchange for disclosure; the claimed invention must be novel, involve an inventive step, be capable of industrial application and avoid the exclusions in sections 3 and 4.",
        ),
        (
            "Invention-discovery boundary",
            "Patent law protects a qualifying new product or process, not a bare discovery; finding a natural fact, known property or known use does not by itself establish an invention, and Section 3(d) supplies a specific known-substance filter.",
        ),
        (
            "Product-process boundary",
            "A product patent protects the claimed product, whereas a process patent protects the claimed method; India used process-only protection for pharmaceuticals, food and chemicals from 1970 to 2004 and restored product patents from 1 January 2005.",
        ),
        (
            "Term-territoriality boundary",
            "The patent term is 20 years from filing and is not indefinitely renewable; protection is territorial, so an Indian grant is not a world right and foreign protection requires national or regional routes.",
        ),
        (
            "Application-publication-examination-grant ladder",
            "Filing creates an application, publication discloses it, examination occurs on request, opposition may test it, and grant follows only if the legal requirements are met; application, publication, examination and grant are not interchangeable status verbs.",
        ),
        (
            "Controller and Patent Office roles",
            "The Controller General of Patents, Designs and Trade Marks is the administrative apex for patents, designs, trade marks and GIs, while the Indian Patent Office handles patent administration; CGPDTM does not administer copyright or plant-variety rights.",
        ),
        (
            "Compulsory-licensing boundary",
            "Section 84 permits an application after three years from grant where public requirements are unmet, the invention is not reasonably affordable or it is not worked in India; Section 92 covers notified emergency, extreme-urgency or public non-commercial-use circumstances.",
        ),
        (
            "Section 3(d) two-limb filter",
            "Section 3(d) treats a new property or new use of a known substance as no invention and allows a new form of a known substance only where it differs significantly in properties with regard to efficacy; enhanced efficacy does not rescue a mere new-use claim.",
        ),
        (
            "Bolar and research discipline",
            "Section 107A permits acts solely and reasonably related to developing and submitting regulatory information and also covers the owner-supported parallel-import limb; the Bolar route must not be inflated into an unlimited exemption for every activity labelled research.",
        ),
        (
            "PCT-WIPO boundary",
            "The Patent Cooperation Treaty is administered by WIPO and provides a common international filing, search, publication and optional preliminary-examination route; national or regional offices retain control over substantive grant.",
        ),
        (
            "TRIPS-WTO boundary",
            "TRIPS is the WTO minimum-standards and flexibilities framework for intellectual property, backed by WTO monitoring and dispute settlement; it neither receives ordinary patent applications nor grants patents.",
        ),
        (
            "Traditional knowledge and TKDL",
            "The Traditional Knowledge Digital Library, built by CSIR with the Ministry of Ayush, makes codified traditional medicinal knowledge available as searchable prior art for defensive protection against wrongful patent claims; it is not a patent over the knowledge.",
        ),
        (
            "IP-instrument boundary",
            "Patents protect qualifying inventions, copyright protects original expression rather than ideas, trademarks identify commercial source, GIs protect collective origin-linked goods, and designs protect visual appearance rather than technical function.",
        ),
        (
            "Life-material patentability boundary",
            "Section 3(j) excludes plants and animals in whole or part other than micro-organisms, including seeds, varieties, species and essentially biological processes; plant varieties follow the PPV&FR Act, 2001 sui-generis route rather than ordinary patent ownership.",
        ),
        (
            "Software-claim discipline",
            "The audited owners link software ecosystems to IPR but do not support a blanket proposition that every software-labelled claim is patentable or unpatentable; classify the claimed technical subject matter under the applicable patent criteria and exclusions before concluding.",
        ),
        (
            "Access-innovation balance",
            "Patents can support disclosure, investment and technology transfer, while Section 3(d), compulsory licensing, opposition, Bolar use and TRIPS flexibilities protect competition, public health and access; neither maximal exclusivity nor routine override is a complete policy.",
        ),
        (
            "Commercialisation-chain boundary",
            "A filing or grant is only an input: commercialisation also requires market validation, proof of concept, technology-transfer capacity, pilot and scale-up finance, industry absorption, regulatory pathways and enforceable licensing arrangements.",
        ),
        (
            "Opposition-revocation-status boundary",
            "Pre-grant opposition under Section 25(1), post-grant opposition under Section 25(2) and revocation are challenge routes with different timing and legal consequences; none should be confused with rejection, expiry, lapse, compulsory licence or voluntary licensing.",
        ),
        (
            "IPAB date discipline",
            "The Intellectual Property Appellate Board was a statutory appellate body when the 2019 Prelims question was asked, but the Tribunals Reforms Act, 2021 abolished specified appellate bodies including IPAB and transferred functions to courts; answer old questions at their date.",
        ),
        (
            "Evidence and status firewall",
            "Application, publication, examination request, opposition, grant, working statement, licence, commercialisation, revocation and expiry are separate evidence rungs; no patent count, case outcome, market success or current legal status should be inferred from another rung.",
        ),
    ]
    traps = [
        "Do not treat novelty, inventive step and industrial applicability as optional alternatives.",
        "Do not call a discovery patentable merely because it is useful.",
        "Do not merge product protection with a protected manufacturing process.",
        "Do not call a 20-year territorial patent perpetual or global.",
        "Do not convert filing, publication or examination into grant.",
        "Do not make CGPDTM the administrator of copyright or plant varieties.",
        "Do not describe compulsory licensing as automatic cancellation of the patent.",
        "Do not apply enhanced-efficacy language to rescue a mere new use under Section 3(d).",
        "Do not turn the Bolar provision into an unlimited general research defence.",
        "Do not call the PCT a world patent or WIPO a national granting office.",
        "Do not make TRIPS a WIPO treaty or a patent-filing route.",
        "Do not describe TKDL as ownership of all traditional knowledge.",
        "Do not treat GI, trademark, copyright, design and patent as interchangeable.",
        "Do not patent-label every life material; apply Section 3(j) and the PPV&FR route.",
        "Do not assert a blanket software-patent rule beyond the audited owners.",
        "Do not equate stronger exclusion in every case with better innovation.",
        "Do not infer commercialisation from filing or grant counts.",
        "Do not merge opposition, revocation, expiry and compulsory licensing.",
        "Do not answer the 2019 IPAB question using only its post-2021 status.",
        "Do not invent an objective key, case result, patent count or current status.",
    ]
    titles = [
        "Patent bargain novelty inventive step and industrial application",
        "Invention discovery product and process boundaries",
        "Patent term territoriality and international protection choices",
        "Application publication examination opposition and grant",
        "Controller General Indian Patent Office and institutional routing",
        "Compulsory licensing Sections 84 and 92",
        "Section 3(d) evergreening and known-substance claims",
        "Bolar regulatory use parallel import and research limits",
        "PCT WIPO national phase and territorial grant",
        "TRIPS WTO Doha flexibilities and institutional separation",
        "Traditional knowledge biopiracy and TKDL defensive prior art",
        "Patent GI copyright trademark and design boundaries",
        "Biotechnology life materials software and excluded subject matter",
        "Access innovation commercialisation and technology transfer",
        "Opposition revocation IPAB PYQ and status discipline",
    ]
    routes = [
        "Open with the disclosure-for-exclusion bargain and apply all three criteria.",
        "Classify discovery, product and process before discussing legal protection.",
        "State term and territoriality before selecting direct, Paris or PCT routes.",
        "Move through every procedural rung without upgrading the status verb.",
        "Separate policy, administration, registry and appellate functions.",
        "State trigger, timing and grounds before evaluating public-interest use.",
        "Apply the new-use and new-form limbs separately and preserve efficacy logic.",
        "Tie permitted conduct to regulatory submission and reject an unlimited research claim.",
        "Explain filing, search, publication and national phase without inventing global grant.",
        "Separate WTO obligations and flexibilities from WIPO treaty administration.",
        "Trace prior-art documentation to defensive protection and benefit-sharing concerns.",
        "Match each asset to the correct right, holder, duration logic and statute.",
        "Classify plants, micro-organisms, varieties and software claims without blanket rules.",
        "Follow filing through technology transfer, scale-up, regulation, market and access.",
        "Answer at the PYQ date and distinguish every challenge and terminal status.",
    ]
    panels = [
        panel("Patentability decision tree", "decision-tree", [
            "CLAIMED SUBJECT MATTER -> product or process?",
            "NOVELTY -> absent from prior art",
            "INVENTIVE STEP -> non-obvious technical advance / economic significance",
            "INDUSTRIAL APPLICATION -> capable of being made or used in industry",
            "SECTIONS 3 / 4 -> excluded subject matter still fails",
        ], [facts[0][0], facts[1][0]]),
        panel("Discovery invention product process matrix", "comparison-matrix", [
            "DISCOVERY -> finding; not automatically an invention",
            "INVENTION -> qualifying new product or process",
            "PRODUCT PATENT -> claimed thing",
            "PROCESS PATENT -> claimed method",
            "INDIA PHARMA / FOOD / CHEMICALS -> process-only 1970-2004; product from 01 JAN 2005",
        ], [facts[1][0], facts[2][0]]),
        panel("Term and territoriality map", "territorial-map", [
            "FILING DATE -> 20-YEAR TERM CLOCK",
            "INDIAN GRANT -> enforceable territorial Indian right",
            "DIRECT / PARIS ROUTE -> selected foreign filings",
            "PCT ROUTE -> common international application procedure",
            "NATIONAL / REGIONAL OFFICE -> final grant decision",
        ], [facts[3][0], facts[9][0]]),
        panel("Indian patent procedure rail", "process-rail", [
            "APPLICATION FILED",
            "        -> PUBLICATION",
            "        -> EXAMINATION ON REQUEST",
            "        -> OPPOSITION / COMPLIANCE TEST",
            "        -> GRANT OR REFUSAL; NEVER UPGRADE AN EARLIER RUNG",
        ], [facts[4][0], facts[17][0], facts[19][0]]),
        panel("Institution and forum router", "institution-map", [
            "DPIIT / CIPAM -> policy and implementation support",
            "CGPDTM -> administrative apex",
            "INDIAN PATENT OFFICE -> patent administration",
            "WIPO -> PCT and treaty cooperation; WTO -> TRIPS",
            "IPAB -> existed at 2019 PYQ date; abolished in 2021",
        ], [facts[5][0], facts[9][0], facts[10][0], facts[18][0]]),
        panel("Public-interest safeguard ladder", "safeguard-ladder", [
            "SECTION 3(d) -> patentability quality filter",
            "SECTION 25 -> pre-grant / post-grant opposition",
            "SECTION 84 -> three-year timing plus three grounds",
            "SECTION 92 -> notified emergency / urgency / public non-commercial use",
            "SECTION 107A -> regulatory-information use; not unlimited research",
        ], [facts[6][0], facts[7][0], facts[8][0], facts[17][0]]),
        panel("Section 3(d) twin-limb gate", "two-limb-gate", [
            "KNOWN SUBSTANCE",
            "BRANCH A -> new property / new use -> not an invention",
            "BRANCH B -> new form -> test significant efficacy difference",
            "THERAPEUTIC CONTEXT -> owner records therapeutic-efficacy reading",
            "TRAP -> never transfer the new-form exception to a new-use claim",
        ], [facts[7][0]]),
        panel("PCT WIPO TRIPS WTO split", "four-corner-comparison", [
            "PCT -> international patent-application procedure",
            "WIPO -> administers PCT and other IP treaties",
            "TRIPS -> minimum standards plus flexibilities",
            "WTO -> monitoring and member-to-member dispute settlement",
            "NONE -> automatic universal patent grant",
        ], [facts[9][0], facts[10][0]]),
        panel("Traditional knowledge protection chain", "defensive-chain", [
            "CODIFIED MEDICINAL KNOWLEDGE",
            "        -> TKDL DOCUMENTATION",
            "        -> SEARCHABLE PRIOR ART FOR PATENT OFFICES",
            "        -> RESIST WRONGFUL NOVELTY CLAIMS / BIOPIRACY",
            "LIMIT -> defensive disclosure is not a patent or automatic benefit sharing",
        ], [facts[11][0]]),
        panel("IP boundary wheel", "instrument-wheel", [
            "PATENT -> invention / technical function",
            "COPYRIGHT -> original expression, not idea",
            "TRADEMARK -> commercial-source identifier",
            "GI -> collective place-linked goods",
            "DESIGN -> visual appearance, not technical function",
        ], [facts[12][0]]),
        panel("Life material and software filter", "classification-filter", [
            "PLANTS / ANIMALS / SEEDS / VARIETIES -> Section 3(j) exclusion",
            "PLANT VARIETY -> PPV&FR sui-generis route",
            "MICRO-ORGANISM -> not inside the stated plant-animal exclusion",
            "SOFTWARE-LABELLED CLAIM -> apply criteria and exclusions; no blanket rule here",
            "RULE -> classify claimed subject matter before policy argument",
        ], [facts[13][0], facts[14][0]]),
        panel("Innovation access and status spine", "answer-spine", [
            "INCENTIVE -> disclosure + investment + licensing",
            "TRANSLATION -> validation + TTO + pilot + finance + regulation + market",
            "ACCESS -> Section 3(d) + CL + opposition + Bolar + TRIPS flexibilities",
            "STATUS -> filed != published != examined != granted != commercialised",
            "VERDICT -> quality rights, credible safeguards and translation capacity",
        ], [facts[15][0], facts[16][0], facts[19][0]]),
    ]
    pyqs = [
        common.make_pyq_solution(
            facts,
            "2019",
            "Prelims GS-I",
            "Assess the routed statements concerning the Indian Patents Act and the Intellectual Property Appellate Board.",
            "The official objective key is unavailable locally. The card preserves the PYQ-date distinction: IPAB existed in 2019 but was abolished in 2021; no option letter is asserted.",
            [5, 18, 19],
        ),
        common.make_pyq_solution(
            facts,
            "2019",
            "GS-III",
            "Discuss how India protects traditional knowledge of medicine from pharmaceutical patenting.",
            "Verified routed Mains demand, 15 marks and 250 words; the route connects prior art, TKDL, patent-quality filters, institutions, limits and benefit-sharing concerns without inventing a case outcome.",
            [1, 7, 11, 15, 19],
        ),
        common.make_pyq_solution(
            facts,
            "2024",
            "GS-III",
            "Explain the world scenario of IPR for life materials and the reasons for low commercialisation of Indian patents.",
            "Verified routed Mains demand, 10 marks and 150 words; the question's filing-rank premise is not repeated as a verified current statistic, and no patent count is supplied.",
            [13, 14, 16, 19],
        ),
    ]
    return common.topic(
        17,
        "Intellectual Property Rights and Patents",
        "17_Intellectual-Property-Rights-and-Patents",
        facts,
        traps,
        [
            (10, "Explain the patentability criteria and distinguish an invention from a discovery.", [0, 1]),
            (10, "Differentiate product and process patents and trace the application-to-grant ladder.", [2, 4]),
            (15, "Examine Section 3(d), compulsory licensing and the Bolar provision as calibrated public-interest safeguards.", [6, 7, 8, 15]),
            (15, "Distinguish patents, GIs, copyright, trademarks and designs, and explain TKDL's defensive role.", [11, 12]),
            (20, "Analyse patentability and governance issues concerning life materials, biotechnology and software-labelled claims in India.", [0, 13, 14, 15, 19]),
            (20, "Evaluate India's IPR architecture through innovation incentives, access, technology commercialisation, opposition, revocation and institutional status discipline.", [5, 15, 16, 17, 18, 19]),
        ],
        titles,
        routes,
        panels,
        [
            "patent",
            "invention",
            "discovery",
            "novelty",
            "inventive step",
            "industrial application",
            "product patent",
            "process patent",
            "20 years from filing",
            "territoriality",
            "application",
            "publication",
            "examination",
            "grant",
            "CGPDTM",
            "Indian Patent Office",
            "compulsory licence",
            "Section 84",
            "Section 92",
            "Section 3(d)",
            "efficacy",
            "evergreening",
            "Section 107A",
            "Bolar exemption",
            "parallel import",
            "PCT",
            "WIPO",
            "national phase",
            "TRIPS",
            "WTO",
            "Doha Declaration",
            "traditional knowledge",
            "TKDL",
            "prior art",
            "biopiracy",
            "geographical indication",
            "copyright",
            "trademark",
            "industrial design",
            "Section 3(j)",
            "micro-organism",
            "PPV&FR Act, 2001",
            "software",
            "access to medicines",
            "technology transfer",
            "commercialisation",
            "pre-grant opposition",
            "post-grant opposition",
            "revocation",
            "IPAB",
            "Tribunals Reforms Act, 2021",
            "PYQ-date distinction",
        ],
        (
            "Audited ledgers route the 2019 Prelims demand on the Indian "
            "Patents Act and IPAB, the 2019 GS-III traditional-knowledge "
            "protection demand and the 2024 GS-III life-material IPR and "
            "commercialisation demand to this owner. Three representative "
            "cards preserve those routes without inventing an objective key, "
            "a patent count or a case outcome."
        ),
        pyqs,
        LIVE_SOURCE_ATTEMPTS,
        (
            "Official IP India, WIPO, WTO and TKDL-source attempts were made "
            "on 2026-09-04. They confirm the patentability criteria, limited "
            "territorial patent bargain, PCT-national-phase boundary and "
            "TRIPS-WTO architecture where substantive text was retrieved. "
            "Exact section claims remain owner-bounded; no filing/grant count, "
            "commercialisation rate, case outcome or blanket software rule is asserted."
        ),
        extra=[
            "00_Master-Framework.md",
            "ANSWER-WORTHINESS-AUDIT.md",
            "REVISION-CHART_Principles-Applications-and-Distinctive-Features.md",
            "../Economy/basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md",
            "../Polity/basic/Statutory-Regulatory-and-Quasi-Judicial-Bodies.md",
        ],
        register_headings=(
            "PATENTABILITY, INVENTION AND PROCEDURAL STATUS MAP",
            "PUBLIC-INTEREST SAFEGUARDS AND IP-INSTRUMENT FIREWALLS",
            "IPR, ACCESS AND COMMERCIALISATION ANSWER SPINE",
            "LIFE MATERIALS, PYQ-DATE ROUTES AND LIVE-SOURCE BOUNDARY",
        ),
        register_answer_spine=[
            "DEFINE THE DISCLOSURE-FOR-LIMITED-EXCLUSION PATENT BARGAIN",
            "TEST NOVELTY INVENTIVE STEP INDUSTRIAL APPLICATION AND EXCLUSIONS",
            "SEPARATE DISCOVERY INVENTION PRODUCT PATENT AND PROCESS PATENT",
            "STATE 20-YEAR TERM TERRITORIALITY AND APPLICATION-TO-GRANT LADDER",
            "ROUTE CGPDTM PATENT OFFICE WIPO WTO AND DATE-SENSITIVE IPAB",
            "APPLY SECTION 3(d) SECTION 84 SECTION 92 SECTION 107A AND OPPOSITIONS",
            "DISTINGUISH PCT FROM GRANT AND WIPO FROM WTO TRIPS",
            "USE TKDL AS DEFENSIVE PRIOR ART NOT OWNERSHIP OF TRADITIONAL KNOWLEDGE",
            "SEPARATE PATENT GI COPYRIGHT TRADEMARK DESIGN AND PLANT-VARIETY RIGHTS",
            "CLASSIFY LIFE MATERIAL AND SOFTWARE CLAIMS WITHOUT BLANKET RULES",
            "TRACE PATENT TO VALIDATION TTO PILOT FINANCE REGULATION MARKET AND ACCESS",
            "CONCLUDE WITH PATENT QUALITY PUBLIC-INTEREST BALANCE AND STATUS DISCIPLINE",
        ],
    )


TOPIC_17 = _topic_17()
