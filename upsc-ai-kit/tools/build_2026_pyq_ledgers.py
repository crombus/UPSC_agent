"""Build the 2026 UPSC PYQ routing ledgers (Prelims GS-I and CSAT).

These Markdown ledgers are the controlling question-to-owner maps for the 2026 cycle,
mirroring the 2018-2023 and 2024-2025 ledger format so that `propagate_2026_pyqs.py`
can parse them. Prelims GS-I question wording was read from the official Set-A scan
(`books/prelima_question_paper_answers/2026-GS1-Set A.pdf`, English text layer,
column-reconstructed) and visually verified against the English page scans; nothing was
reconstructed from memory or aggregators. CSAT family classification and neutral type are
read verbatim from the audited `knowledge/CSAT/00_Question-Audit-Ledger.md` (2026 section).

The official 2026 Prelims and CSAT keys held locally are PROVISIONAL; no answer letter is
recorded or inferred in either ledger.

Run:  python tools/build_2026_pyq_ledgers.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
CSAT_AUDIT = KNOWLEDGE / "CSAT" / "00_Question-Audit-Ledger.md"

# Source status strings (kept accurate per requirement: 2026 keys are provisional).
PRELIMS_KEY = ("Provisional 2026 Set-A key present locally (`Ans-2026-GS1-Provisional`); "
               "key is provisional - no answer letter recorded or inferred here")
CSAT_KEY = ("Provisional 2026 Set-A key present locally (scan headed `CS (P) Exam 2026 "
            "[Prov. Ans. Key]`); family/neutral type per CSAT/00_Question-Audit-Ledger; "
            "key is provisional - no answer letter recorded or inferred here")

# Questions without a dedicated Core owner are recorded here rather than hidden behind
# a loose route. The 2026 review closed every initially identified gap.
CORE_GAP = {}

CSAT_FAMILY_FILE = {
    "01": "CSAT/basic/01_Reading-Comprehension.md",
    "02": "CSAT/basic/02_Number-Systems-and-Number-Sense.md",
    "03": "CSAT/basic/03_Arithmetic-and-Commercial-Math.md",
    "04": "CSAT/basic/04_Rates-Motion-Time-and-Geometry.md",
    "05": "CSAT/basic/05_Algebra-Inequalities-and-Data-Sufficiency.md",
    "06": "CSAT/basic/06_Logical-Reasoning-Coding-Counting-and-DI.md",
}


def link(path: str) -> str:
    label = path[:-3] if path.endswith(".md") else path
    return f"[{label}]({path})"


def links(paths) -> str:
    if isinstance(paths, str):
        paths = [paths]
    return " \u00b7 ".join(link(p) for p in paths)


def cell(text: str) -> str:
    return text.replace("|", r"\|").strip()


# ---------------------------------------------------------------------------
# CSAT: parse the audited question ledger (2026 section only).
# ---------------------------------------------------------------------------
def parse_csat() -> list:
    text = CSAT_AUDIT.read_text(encoding="utf-8")
    rows = []
    year = None
    for line in text.splitlines():
        h = re.match(r"^##\s+(20\d\d)\s*$", line.strip())
        if h:
            year = int(h.group(1))
            continue
        if year != 2026:
            continue
        m = re.match(r"^\|\s*(\d{1,3})\s*\|\s*(\d{2})\s*\|\s*(.+?)\s*\|\s*([A-D])\s*\|\s*([SP])\s*\|\s*$", line)
        if not m:
            continue
        q, fam, neutral, key, status = m.groups()
        rows.append((2026, int(q), neutral, fam, CSAT_FAMILY_FILE[fam], CSAT_KEY))
    return rows


# ---------------------------------------------------------------------------
# PRELIMS 2026 data: (q, theme, subject, route, is_core_gap)
# Themes read from the official 2026 GS-I Set-A scan (English text layer),
# visually verified against the English page images; no answer is recorded.
# ---------------------------------------------------------------------------
PRELIMS_2026 = [
    (1, "Carnatic and Hindustani raga equivalence in Indian classical music traditions", "Indian Art and Culture", "Indian-Art-and-Culture/basic/08_Indian-Music.md", False),
    (2, "Hilton-Young Commission rupee-sterling exchange rate and British fiscal rationale", "Modern History", "Modern-Indian-History/basic/07_Economic-Impact-of-British-Rule.md", False),
    (3, "Jain classification of the four principal forms of existence", "Ancient History", "Ancient-Indian-History/basic/10_Jainism-and-Buddhism.md", False),
    (4, "Nagara-style shikhara among early Indian temple architecture examples", "Indian Art and Culture", "Indian-Art-and-Culture/basic/03_Temple-Architecture-and-Chandella-Khajuraho.md", False),
    (5, "Hallisalasya painting and iconographic subject in the Bagh Caves", "Indian Art and Culture", "Indian-Art-and-Culture/basic/07_Painting-Traditions.md", False),
    (6, "Pali textual and archaeological evidence for coins and money economy", "Ancient History", "Ancient-Indian-History/basic/19_Crafts-Commerce-Urban-Growth.md", False),
    (7, "Place-value notation in Indian epigraphic and Southeast Asian inscriptions", "Indian Art and Culture", "Indian-Art-and-Culture/basic/11_Languages-Scripts-Literature-and-Manuscripts.md", False),
    (8, "Harappan household artefacts, weights, construction, and social inferences", "Ancient History", "Ancient-Indian-History/basic/06_Harappan-Civilization.md", False),
    (9, "Eka Movement and Bardoli Satyagraha: agrarian grievances and organisation", "Modern History", "Modern-Indian-History/basic/20_Non-Cooperation-and-Khilafat-Movement.md", False),
    (10, "Rigvedic irrigation, wells, draught animals, and supporting textual evidence", "Ancient History", "Ancient-Indian-History/basic/08_Rig-Vedic-Age.md", False),
    (11, "Pleistocene shifts in Yamuna, Sutlej, Ganga, and Indus drainage", "Geography", "Geography/basic/05_Landforms-by-Running-Water.md", False),
    (12, "Empty seat symbolism in early Buddhist visual and sacred iconography", "Indian Art and Culture", "Indian-Art-and-Culture/basic/06_Sculpture-Pottery-and-Iconography.md", False),
    (13, "Amaravati Stupa location, scale, sculpture school, and external influence", "Indian Art and Culture", "Indian-Art-and-Culture/basic/02_Mauryan-Buddhist-Jain-and-Rock-Cut-Heritage.md", False),
    (14, "Early historical Tamilakam rulers and Chera, Chola, Pandya dynasties", "Ancient History", "Ancient-Indian-History/basic/18_Sangam-Age-Deep-South.md", False),
    (15, "Vedic river names and their modern river identifications", "Ancient History", "Ancient-Indian-History/basic/08_Rig-Vedic-Age.md", False),
    (16, "Formation of Forward Bloc and Congress political alignments in 1939", "Modern History", "Modern-Indian-History/basic/23_Left-Peasant-Workers-and-States-Peoples-Movements.md", False),
    (17, "British revenue policy towards Awadh taluqdars after annexation", "Modern History", "Modern-Indian-History/basic/11_The-Revolt-of-1857.md", False),
    (18, "Montagu-Chelmsford reforms, separate electorates, and community-based political alliances", "Modern History", "Modern-Indian-History/basic/18_WWI-Home-Rule-and-Lucknow-Pact.md", False),
    (19, "Pandit Mallikarjun Mansur and Hindustani classical music gharanas", "Indian Art and Culture", "Indian-Art-and-Culture/basic/08_Indian-Music.md", False),
    (20, "Vedic textual origin and usage of the term kshetra-patni", "Ancient History", "Ancient-Indian-History/basic/08_Rig-Vedic-Age.md", False),
    (21, "India's LT-LEDS, BUR-4, net-zero pathway, and climate resilience", "Environment and Ecology", "Environment-and-Ecology/basic/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md", False),
    (22, "Western hoolock gibbon conservation status, habitat, and arboreal adaptation", "Environment and Ecology", "Environment-and-Ecology/basic/05_IUCN-Red-List-and-Endemism.md", False),
    (23, "Mangrove ecosystem services for coastal climate resilience and livelihoods", "Environment and Ecology", "Environment-and-Ecology/basic/24_Coastal-and-Marine-Ecology-CRZ-Blue-Economy.md", False),
    (24, "Vizhinjam International Seaport and India's trans-shipment logistics strategy", "Economy", "Economy/basic/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md", False),
    (25, "Indian subcontinent river identified through antecedence, course, origin, and distributaries", "Geography", "Geography/basic/05_Landforms-by-Running-Water.md", False),
    (26, "Indian State boundaries, international borders, and interstate adjacency", "Geography", "Geography/basic/35_Indian-Political-Geography-Boundaries-and-Neighbours.md", False),
    (27, "Amur Falcon migration to Doyang Lake and community-based conservation", "Environment and Ecology", "Environment-and-Ecology/basic/10_CMS-Bonn-Convention-Migratory-Species.md", False),
    (28, "Rainfed Area Development objectives under sustainable agriculture mission", "Economy", "Economy/basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md", False),
    (29, "Oeko-Tex certification for Eri silk and eco-conscious textile markets", "Indian Art and Culture", "Indian-Art-and-Culture/basic/12_Crafts-Textiles-Folk-and-Tribal-Traditions.md", False),
    (30, "Strait of Hormuz and West Asian maritime access to Indian Ocean", "International Relations", "International-Relations/basic/06_West-Asia-Energy-Security-and-Connectivity.md", False),
    (31, "Tungurahua Volcano UNESCO Global Geopark and its national location", "Geography", "Geography/basic/03_Vulcanism-and-Earthquakes.md", False),
    (32, "Madhav National Park, tiger reserve status, and Sakhya Sagar", "Environment and Ecology", "Environment-and-Ecology/basic/06_Protected-Area-Network-India.md", False),
    (33, "Andaman and Nicobar climate, monsoon rainfall, and seasonal precipitation", "Geography", "Geography/basic/16_Tropical-Monsoon-and-Marine-Climate.md", False),
    (34, "Tectonic and geomorphic characteristics of India's Peninsular Block", "Geography", "Geography/basic/02_The-Earths-Crust-Rocks.md", False),
    (35, "Sagarmala Programme, port-led development, and maritime innovation strategy", "Economy", "Economy/basic/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md", False),
    (36, "Foxtail orchid distribution, epiphytic habit, and State-flower status", "Environment and Ecology", "Environment-and-Ecology/basic/28_Species-and-Current-Affairs-Tracker.md", False),
    (37, "Tai-Ahom Moidams, royal burial practices, and UNESCO heritage status", "Indian Art and Culture", "Indian-Art-and-Culture/basic/14_Heritage-Conservation-Institutions-and-UNESCO.md", False),
    (38, "FAO Blue Transformation and sustainable fisheries and aquaculture framework", "Economy", "Economy/basic/30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries.md", False),
    (39, "Lake Turkana geography, desert-lake status, and UNESCO heritage", "Geography", "Geography/basic/09_Lakes.md", False),
    (40, "Plan Vivo certified REDD+ projects and community forest carbon conservation", "Environment and Ecology", "Environment-and-Ecology/basic/12_Forest-Governance-CAMPA-and-Green-India-Mission.md", False),
    (41, "Genetic medicines, gene delivery vectors, and therapeutic DNA modification", "Science and Technology", "Science-and-Technology/basic/13_Biotechnology-Fundamentals-and-DBT-Missions.md", False),
    (42, "Large language models, probabilistic prediction, optimization, and output bias", "Science and Technology", "Science-and-Technology/basic/09_Artificial-Intelligence-Governance-and-IndiaAI.md", False),
    (43, "Stealth technology, radar cross-section, absorbing materials, and detection", "Science and Technology", "Science-and-Technology/basic/06_Defence-RandD-DRDO-and-Missile-Systems.md", False),
    (44, "Aircraft black-box recorders, underwater detection, and crash-survivable memory", "Science and Technology", "Science-and-Technology/basic/21_General-Science-Physics-Fundamentals.md", False),
    (45, "Green hydrogen production pathways and India's National Green Hydrogen Mission", "Environment and Ecology", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md", False),
    (46, "Private-sector participation, IN-SPACe mandate, and Indian space startup achievements", "Science and Technology", "Science-and-Technology/basic/01_Space-Programme-ISRO-Launch-Vehicles.md", False),
    (47, "Drone swarm communication, autonomous coordination, and electronic countermeasure techniques", "Science and Technology", "Science-and-Technology/basic/19_Drones-UAVs-and-Robotics-Policy.md", False),
    (48, "GenomeIndia Project funding, institutional role, and Indian genetic diversity", "Science and Technology", "Science-and-Technology/basic/13_Biotechnology-Fundamentals-and-DBT-Missions.md", False),
    (49, "National Quantum Mission, quantum-computing targets, and thematic hubs", "Science and Technology", "Science-and-Technology/basic/10_National-Quantum-Mission-and-Quantum-Tech.md", False),
    (50, "India's Deep Ocean Mission, Samudrayaan, Matsya-6000, and implementing ministry", "Environment and Ecology", "Environment-and-Ecology/basic/24_Coastal-and-Marine-Ecology-CRZ-Blue-Economy.md", False),
    (51, "Public-service accountability when confronting compromised vaccine distribution quality", "Governance", "Governance/basic/08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md", False),
    (52, "Participatory resolution of tribal land, waste management, and environmental conflict", "Governance", "Governance/basic/14_Participatory-Governance.md", False),
    (53, "Transparency and integrity in public procurement with confidential adverse information", "Governance", "Governance/basic/08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md", False),
    (54, "Constitutional definition of law under Article 13 and customary law", "Polity", "Polity/basic/Fundamental-Rights.md", False),
    (55, "Constitutional provisions on title, repeal, and commencement date", "Polity", "Polity/basic/Making-of-the-Constitution.md", False),
    (56, "Disability rights law, accessibility mission, and disability development corporation", "Social Justice", "Social-Justice/basic/11_Persons-with-Disabilities.md", False),
    (57, "Constitutional safeguards, schedules, taxation, and local representation for SCs and STs", "Polity", "Polity/basic/Scheduled-and-Tribal-Areas.md", False),
    (58, "Starred and unstarred questions and supplementary questions in Parliament", "Polity", "Polity/basic/Parliament.md", False),
    (59, "Parliamentary Committee on Welfare of Scheduled Castes and Scheduled Tribes", "Polity", "Polity/basic/Parliament.md", False),
    (60, "Mission Sudarshan Chakra and India's integrated air and missile defence", "Science and Technology", "Science-and-Technology/basic/06_Defence-RandD-DRDO-and-Missile-Systems.md", False),
    (61, "India's cross-border bridges with Bangladesh, Myanmar, and Nepal", "International Relations", "International-Relations/basic/02_India-and-the-Neighbourhood.md", False),
    (62, "Zero FIR under BNSS and police jurisdiction for reported offences", "Internal Security", "Internal-Security/basic/01_Internal-Security-Foundations-and-Governance.md", False),
    (63, "Government investigative and economic-intelligence bodies and their statutory functions", "Polity", "Polity/basic/CVC-and-CBI.md", False),
    (64, "India's ratification status of major international labour and humanitarian conventions", "International Relations", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md", False),
    (65, "AI Impact Summit 2026 framework, declaration, and governance principles", "Science and Technology", "Science-and-Technology/basic/09_Artificial-Intelligence-Governance-and-IndiaAI.md", False),
    (66, "India-ASEAN connectivity through regional multimodal transport infrastructure projects and corridors", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (67, "Indian development-assistance projects matched with neighbouring partner countries and locations", "International Relations", "International-Relations/basic/02_India-and-the-Neighbourhood.md", False),
    (68, "Indian manufacture of fighter aircraft, tanks, and submarines", "Science and Technology", "Science-and-Technology/basic/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md", False),
    (69, "Migration cooperation platforms and their binding or consultative character", "International Relations", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md", False),
    (70, "United Nations agencies awarded the Nobel Prize on multiple occasions", "International Relations", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md", False),
    (71, "United Nations peacekeeping operations matched with their operational periods", "International Relations", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md", False),
    (72, "BIMSTEC institutional centres matched with their respective geographic locations", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (73, "Indian Army Corps formations matched with their operational headquarters locations", "Internal Security", "Internal-Security/basic/12_Security-Forces-Intelligence-Coordination-and-Rights.md", False),
    (74, "Revamped Rashtriya Gram Swaraj Abhiyan objectives, duration, and funding", "Governance", "Governance/basic/12_Local-Governance-and-Service-Delivery.md", False),
    (75, "European Union membership status among selected European nation-states", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (76, "INTERPOL notice categories and their distinct international investigative purposes", "Internal Security", "Internal-Security/basic/11_Organised-Crime-Narco-Terrorism-and-Trafficking.md", False),
    (77, "NIRANTAR environmental research platform, thematic verticals, and lead institutions", "Environment and Ecology", "Environment-and-Ecology/basic/27_Environmental-Institutions-MoEFCC-CPCB-NBA-WII.md", False),
    (78, "India-Germany bilateral visit outcomes, cooperation, and Indo-Pacific dialogue", "International Relations", "International-Relations/basic/03_India-China-Major-Powers-and-Resilient-Supply-Chains.md", False),
    (79, "DHRUV64 processor, DIR-V programme, and indigenous computing capability", "Science and Technology", "Science-and-Technology/basic/11_Semiconductor-Mission-and-Electronics-Manufacturing.md", False),
    (80, "BIS bomb-disposal standard, interoperability, and technology development collaboration", "Science and Technology", "Science-and-Technology/basic/06_Defence-RandD-DRDO-and-Missile-Systems.md", False),
    (81, "2025 Nobel Prize recipient identified through biographical and professional clues", "Science and Technology", "Science-and-Technology/basic/26_Scientific-Discoveries-Nobel-Prizes-and-Scientists.md", False),
    (82, "Grand Slam tennis governance, eligibility, and wild-card participation rules", "Governance", "Governance/basic/16_Sports-Governance-Institutions-and-Major-Tournaments.md", False),
    (83, "Indian semiconductor plants and their announced state-level manufacturing locations", "Science and Technology", "Science-and-Technology/basic/11_Semiconductor-Mission-and-Electronics-Manufacturing.md", False),
    (84, "Bharat Forecast System's resolution objective and developing institution", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (85, "Film Boong, BAFTA recognition, director, and Indian cinema milestone", "Indian Art and Culture", "Indian-Art-and-Culture/basic/15_Indian-Cinema-Film-Institutions-and-Awards.md", False),
    (86, "Blockchain database replication, immutability, stakeholder access, and consortium models", "Science and Technology", "Science-and-Technology/basic/25_Computing-Fundamentals-Hardware-Software-Networks-and-Cloud.md", False),
    (87, "Dropshipping model and third-party order fulfilment in e-commerce", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (88, "ONDC interoperability objective and competition among digital-commerce platform networks", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (89, "UPI and digital rupee transaction, settlement, and liability characteristics", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (90, "Real-world asset tokenization using blockchain and investment access", "Economy", "Economy/basic/08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md", False),
    (91, "RBI Financial Inclusion Index sub-indices and measurement dimensions", "Economy", "Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md", False),
    (92, "Sustainability bonds financing combined environmental and social projects", "Economy", "Economy/basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md", False),
    (93, "Mixchange role in MSME invoice and bill discounting finance", "Economy", "Economy/basic/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md", False),
    (94, "Fiscal-policy crowding-out effect through government borrowing and interest rates", "Economy", "Economy/basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md", False),
    (95, "Rare earth elements, critical minerals, and India's self-reliance mission", "Science and Technology", "Science-and-Technology/basic/20_Emerging-Materials-Rare-Earths-and-Critical-Minerals.md", False),
    (96, "Aviation hull insurance and airline liability under Montreal Convention", "Economy", "Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md", False),
    (97, "Crowdfunding platforms and financing access for small and medium enterprises", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (98, "Indian financial-sector reform committees and their institutional sponsors", "Economy", "Economy/basic/04_RBI-Monetary-Policy-and-Liquidity-Management.md", False),
    (99, "NBFC deposits, RBI registration, payment systems, and deposit insurance", "Economy", "Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md", False),
    (100, "Multidimensional Poverty Index methodology, indicators, and institutional comparison", "Economy", "Economy/basic/02_Growth-Development-HDI-IHDI-and-MPI.md", False),
]


HEADER_NOTE = (
    "> ## Scope and honesty rules\n"
    ">\n"
    "> **Controlling routing/provenance record for the 2026 cycle.** Each row records where a\n"
    "> printed question already belongs in this knowledge base. A row is a pointer, not an\n"
    "> answer key. Prelims GS-I wording was read from the official 2026 Set-A scan (English text\n"
    "> layer, column-reconstructed) and visually verified against the English page images;\n"
    "> nothing was reconstructed from memory, coaching sites or aggregators.\n"
    ">\n"
    "> **Neutral labels.** The theme column names the subject matter in neutral words and does\n"
    "> not resolve the item (no option letters, no verdicts).\n"
    ">\n"
    "> **Provisional keys.** The 2026 Prelims and CSAT keys held locally are provisional; this\n"
    "> ledger records no answer letter and infers none. Every routed owner is an existing\n"
    "> Basic/Core owner (never routed exclusively to Advanced).\n"
    ">\n"
    "> **Verification.** Every 2026 Prelims row was verified against the official Set-A scan\n"
    "> page-by-page; year/number/wording and each route are confirmed, so no row carries a\n"
    "> residual OCR-uncertainty warning.\n"
)


def prelims_ledger() -> str:
    lines = [
        "# UPSC Prelims General Studies Paper I - PYQ Routing Ledger, 2026",
        "",
        HEADER_NOTE,
        "",
        "> ## Key status: `Provisional key available locally`",
        ">",
        "> The official 2026 Prelims Set-A answer key held in this repository",
        "> (`knowledge-export/Prelims PYQ/Ans-2026-GS1-Provisional`) is **provisional**. This",
        "> ledger records **no answer letter** and infers none: routing is linkage metadata only.",
        "",
        "| Year | Q | Topic / theme (neutral) | Subject / family | Route(s) | Integration note / status |",
        "|---:|---:|---|---|---|---|",
    ]
    for q, theme, subject, route, gap in PRELIMS_2026:
        note = PRELIMS_KEY
        if gap:
            note = note + f"; CORE-GAP: {CORE_GAP[q]}"
        lines.append(
            f"| 2026 | {q} | {cell(theme)} | {cell(subject)} | {links(route)} | {cell(note)} |"
        )
    return "\n".join(lines) + "\n"


def csat_ledger() -> str:
    rows = parse_csat()
    lines = [
        "# UPSC CSAT (General Studies Paper II) - PYQ Routing Ledger, 2026",
        "",
        HEADER_NOTE,
        "",
        "> ## Family classification source",
        ">",
        "> The six-family classification and neutral type for every 2026 CSAT question is taken",
        "> verbatim from the audited [`CSAT/00_Question-Audit-Ledger`](CSAT/00_Question-Audit-Ledger.md),",
        "> which read the 2026 Set-A scan directly. Only families 01-06 occur; every route targets",
        "> an existing Basic owner (Topics 01-06) and the CSAT Topic 07/08 architecture is left",
        "> untouched. The 2026 Set-A key is provisional; **no answer letter is recorded here.**",
        "",
        "| Year | Q | Neutral type | Family | Route(s) | Integration note / status |",
        "|---:|---:|---|:---:|---|---|",
    ]
    for year, q, neutral, fam, route, note in rows:
        lines.append(
            f"| {year} | {q} | {cell(neutral)} | {fam} | {links(route)} | {cell(note)} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    outputs = {
        KNOWLEDGE / "_PYQ-ROUTING-PRELIMS-2026.md": prelims_ledger(),
        KNOWLEDGE / "_PYQ-ROUTING-CSAT-2026.md": csat_ledger(),
    }
    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path.name} ({text.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
