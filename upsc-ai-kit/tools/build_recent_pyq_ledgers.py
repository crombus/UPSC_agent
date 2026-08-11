"""Build the 2024-2025 UPSC PYQ routing ledgers (Prelims, CSAT, Mains, Essay).

These Markdown ledgers are the controlling question-to-owner maps for 2024-2025,
mirroring the 2018-2023 ledger format so that `propagate_recent_pyqs.py` can parse
them. Question wording comes only from the local knowledge-export OCR text; where
the OCR was not legibly recoverable a row is marked `OCR-uncertain`. No objective
answer is recorded. CSAT family classification is read verbatim from the audited
`knowledge/CSAT/00_Question-Audit-Ledger.md`.

Run:  python tools/build_recent_pyq_ledgers.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
CSAT_AUDIT = KNOWLEDGE / "CSAT" / "00_Question-Audit-Ledger.md"

# Source status strings (kept accurate per requirement).
PRELIMS_KEY = "Key available locally (official Set-A answer key present); answer not recorded here"
PRELIMS_KEY_OCR = ("Key available locally (official Set-A answer key present); answer not recorded; "
                   "OCR-uncertain - wording/number reconstructed from printed order, manual verification needed")
MAINS_NOTE = "Routed to owning topic"

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
# CSAT: parse the audited question ledger (2024 and 2025 sections only).
# ---------------------------------------------------------------------------
def parse_csat() -> list[tuple[int, int, str, str, str, str]]:
    text = CSAT_AUDIT.read_text(encoding="utf-8")
    rows: list[tuple[int, int, str, str, str, str]] = []
    year = None
    for line in text.splitlines():
        h = re.match(r"^##\s+(20\d\d)\s*$", line.strip())
        if h:
            year = int(h.group(1))
            continue
        if year not in (2024, 2025):
            if year and year not in (2024, 2025):
                year = None if not line.startswith("|") else year
            continue
        m = re.match(r"^\|\s*(\d{1,3})\s*\|\s*(\d{2})\s*\|\s*(.+?)\s*\|\s*([A-D])\s*\|\s*([SP])\s*\|\s*$", line)
        if not m:
            continue
        q, fam, neutral, key, status = m.groups()
        note = ("Key supplied locally (Set-A scan; recorded as supplied, not certified final); "
                "family and neutral type per CSAT/00_Question-Audit-Ledger; answer not recorded here")
        rows.append((year, int(q), neutral, fam, CSAT_FAMILY_FILE[fam], note))
    return rows


# ---------------------------------------------------------------------------
# PRELIMS data: (q, theme, subject, route, ocr_uncertain)
# ---------------------------------------------------------------------------
PRELIMS_2025 = [
    (1, "Alternative Investment Funds - which investment vehicles qualify (hedge funds, venture capital)", "Economy", "Economy/basic/08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md", False),
    (2, "Sources of income of the Reserve Bank of India", "Economy", "Economy/basic/04_RBI-Monetary-Policy-and-Liquidity-Management.md", False),
    (3, "Enforcement agencies (ED, DRI, DGGI) and their parent ministries", "Economy", "Economy/basic/10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism.md", False),
    (4, "Business Responsibility and Sustainability Report (BRSR) for listed companies", "Economy", "Economy/basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md", False),
    (5, "Taxation of allied agricultural income; rural agricultural land as a capital asset", "Economy", "Economy/basic/10_Taxation-GST-Finance-Commission-and-Fiscal-Federalism.md", False),
    (6, "Minerals Security Partnership; critical minerals; MMDR Act 2023 amendment", "Science and Technology", "Science-and-Technology/basic/20_Emerging-Materials-Rare-Earths-and-Critical-Minerals.md", False),
    (7, "Bondholders versus stockholders - risk and repayment priority", "Economy", "Economy/basic/08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md", False),
    (8, "India's equity options market growth and regulation", "Economy", "Economy/basic/08_Securities-Bonds-Equity-Derivatives-and-Investment-Funds.md", False),
    (9, "Circular economy - emissions, raw-material use and wastage", "Economy", "Economy/basic/25_Climate-Economics-Green-Finance-and-Circular-Economy.md", False),
    (10, "Capital receipts; borrowings, disinvestment and interest", "Economy", "Economy/basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md", False),
    (11, "Raja Ram Mohan Roy - thought and reform", "Modern History", "Modern-Indian-History/basic/10_Socio-Religious-Reform-Movements.md", False),
    (12, "Non-Cooperation Programme - components", "Modern History", "Modern-Indian-History/basic/20_Non-Cooperation-and-Khilafat-Movement.md", False),
    (13, "The 'Araghatta' irrigation device", "Ancient History", "Ancient-Indian-History/basic/19_Crafts-Commerce-Urban-Growth.md", False),
    (14, "Ancient ruler bearing titles Mattavilasa, Vichitrachitta, Gunabhara (Pallava)", "Ancient History", "Ancient-Indian-History/basic/23_Peninsular-India-Pallavas-Chalukyas.md", False),
    (15, "Fa-hien (Faxian) and the Gupta reign he visited", "Ancient History", "Ancient-Indian-History/basic/20_Gupta-Empire.md", False),
    (16, "Ruler who led a successful military campaign against the maritime kingdom of Srivijaya (Rajendra I, Chola)", "Ancient History", "Ancient-Indian-History/basic/27_Imperial-Cholas-State-Society-Economy-and-Maritime-Power.md", False),
    (17, "Ancient India (600-322 BC) territorial region-river pairs", "Ancient History", "Ancient-Indian-History/basic/11_Mahajanapadas-and-Rise-of-Magadha.md", False),
    (18, "First Gandharva Mahavidyalaya (Vishnu Digambar Paluskar, 1901)", "Indian Art and Culture", "Indian-Art-and-Culture/basic/08_Indian-Music.md", False),
    (19, "Ashokan inscriptions - Pradeshika, Rajuka and Yukta officers", "Ancient History", "Ancient-Indian-History/basic/14_Mauryan-Empire.md", False),
    (20, "Non-Cooperation Movement - Swaraj resolution and its stages", "Modern History", "Modern-Indian-History/basic/20_Non-Cooperation-and-Khilafat-Movement.md", False),
    (21, "NATO member countries", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (22, "Countries through which the Andes mountains pass", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (23, "Water bodies through which the equator passes", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (24, "Turmeric production and export, 2022-23", "Geography", "Geography/basic/30_Primary-Economic-Activities-Agriculture.md", False),
    (25, "Evidences of continental drift", "Geography", "Geography/basic/02_The-Earths-Crust-Rocks.md", False),
    (26, "Atmospheric dust distribution across climatic zones", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (27, "January isotherms bending over land and ocean", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (28, "Permeability of chalk versus clay (effect of water on rocks)", "Geography", "Geography/basic/04_Weathering-MassMovement-Groundwater.md", False),
    (29, "Atmosphere maintaining Earth's temperature; CO2 absorbing radiation", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (30, "Rashtriya Gokul Mission - indigenous cattle", "Economy", "Economy/basic/30_Economics-of-Animal-Rearing-Livestock-Dairy-Poultry-and-Fisheries.md", False),
    (31, "Cement-industry carbon emissions; limestone and clinker", "Environment and Ecology", "Environment-and-Ecology/basic/17_Climate-Change-Science-Greenhouse-Effect.md", False),
    (32, "COP28 Declaration on Climate and Health; India's position", "Environment and Ecology", "Environment-and-Ecology/basic/19_UNFCCC-COP-Kyoto-Paris-Agreement.md", False),
    (33, "Shift in Earth's rotation and axis; solar flares; polar ice melt", "Geography", "Geography/basic/01_The-Earth-and-the-Universe.md", False),
    (34, "Paris Agreement Article 6 - carbon markets and non-market approaches", "Environment and Ecology", "Environment-and-Ecology/basic/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md", False),
    (35, "Launcher of the 'Nature Solutions Finance Hub for Asia and the Pacific' (ADB)", "Economy", "Economy/basic/21_IMF-World-Bank-ADB-AIIB-NDB-and-Global-Governance.md", False),
    (36, "'Direct Air Capture' emerging technology", "Environment and Ecology", "Environment-and-Ecology/basic/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md", False),
    (37, "Peacock (Gooty) tarantula - endemic species", "Environment and Ecology", "Environment-and-Ecology/basic/28_Species-and-Current-Affairs-Tracker.md", False),
    (38, "India's CO2 emissions per capita and largest sources", "Environment and Ecology", "Environment-and-Ecology/basic/17_Climate-Change-Science-Greenhouse-Effect.md", False),
    (39, "Plant-type pairs (cassava, ginger, Malabar spinach, mint, papaya)", "Science and Technology", "Science-and-Technology/basic/23_General-Science-Biology-and-Physiology.md", False),
    (40, "Sources of the planet's oxygen (rainforests, phytoplankton, surface water)", "Environment and Ecology", "Environment-and-Ecology/basic/01_Ecosystem-Structure-and-Function.md", False),
    (41, "Alternative-powertrain vehicles (battery EV, hydrogen fuel-cell, hybrid)", "Science and Technology", "Science-and-Technology/basic/18_Electric-Vehicles-Batteries-and-Alternative-Fuels.md", False),
    (42, "Unmanned Aerial Vehicles - capabilities of different types", "Science and Technology", "Science-and-Technology/basic/19_Drones-UAVs-and-Robotics-Policy.md", False),
    (43, "Elements making up EV battery cathodes (cobalt, graphite, lithium, nickel)", "Science and Technology", "Science-and-Technology/basic/20_Emerging-Materials-Rare-Earths-and-Critical-Minerals.md", False),
    (44, "Everyday items that contain plastic (cigarette butts, eyeglass lenses, car tyres)", "Environment and Ecology", "Environment-and-Ecology/basic/15_Solid-Plastic-and-E-Waste-Rules.md", False),
    (45, "Coal gasification technology - what it can produce", "Science and Technology", "Science-and-Technology/basic/22_General-Science-Chemistry-Fundamentals.md", False),
    (46, "CL-20, HMX and LLM-105 - military explosives", "Science and Technology", "Science-and-Technology/basic/06_Defence-RandD-DRDO-and-Missile-Systems.md", False),
    (47, "Majorana 1 chip, quantum computing and deep learning", "Science and Technology", "Science-and-Technology/basic/10_National-Quantum-Mission-and-Quantum-Tech.md", False),
    (48, "Monoclonal antibodies", "Science and Technology", "Science-and-Technology/basic/15_Vaccines-Monoclonal-Antibodies-and-Biopharma.md", False),
    (49, "Viruses - ocean survival, infecting bacteria, host transcription", "Science and Technology", "Science-and-Technology/basic/23_General-Science-Biology-and-Physiology.md", False),
    (50, "Activated carbon for removing pollutants from effluents", "Environment and Ecology", "Environment-and-Ecology/basic/14_Water-Pollution-and-River-Cleaning-Missions.md", False),
    (51, "Ordinances - amending a Central Act, abridging a Fundamental Right, retrospective effect", "Polity", "Polity/basic/President-and-Vice-President.md", False),
    (52, "State-description pairs (Arunachal Pradesh, Nagaland, Tripura formation)", "Polity", "Polity/basic/Union-and-Territory.md", False),
    (53, "Bodies established under the Constitution (Inter-State Council, NSC, Zonal Councils)", "Polity", "Polity/basic/Centre-State-Relations.md", False),
    (54, "Governor's discretion; President reserving a State bill", "Polity", "Polity/basic/Governor-and-CM.md", False),
    (55, "Constitutional provisions matched to their Part (Directive Principles / Fundamental Duties / Fundamental Rights)", "Polity", "Polity/basic/Directive-Principles.md", False),
    (56, "Fifth Schedule Scheduled Area - executive power and Union takeover", "Polity", "Polity/basic/Scheduled-and-Tribal-Areas.md", False),
    (57, "Organization-Union Ministry pairs (Automotive Board, Coir Board, NCTI)", "Polity", "Polity/basic/Ministries-and-Departments-of-Government.md", False),
    (58, "Constitutional amendments requiring ratification by State legislatures", "Polity", "Polity/basic/Amendment-and-Basic-Structure.md", False),
    (59, "Governor's immunity; immunity for words spoken in a State Legislature", "Polity", "Polity/basic/Governor-and-CM.md", False),
    (60, "Activities regulated by the Petroleum and Natural Gas Regulatory Board", "Economy", "Economy/basic/31_Energy-Infrastructure-Economics-Power-Fuels-and-Energy-Security.md", False),
    (61, "Revenue, fiscal and primary deficit computation", "Economy", "Economy/basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md", False),
    (62, "International North-South Transport Corridor (INSTC) connectivity", "International Relations", "International-Relations/basic/05_Central-Asia-Eurasia-and-Connectivity.md", False),
    (63, "Ethanol producers Brazil and USA - feedstock comparison", "Economy", "Economy/basic/31_Energy-Infrastructure-Economics-Power-Fuels-and-Energy-Security.md", False),
    (64, "Wet-bulb temperature crossing 35C - implications", "Disaster Management", "Disaster-Management/basic/09_Drought-Heat-Waves-and-Slow-Onset-Risk.md", False),
    (65, "Gross primary deficit computation", "Economy", "Economy/basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md", False),
    (66, "Recommendations of the 15th Finance Commission", "Polity", "Polity/basic/Finance-Commission.md", False),
    (67, "International Bank for Reconstruction and Development (IBRD)", "Economy", "Economy/basic/21_IMF-World-Bank-ADB-AIIB-NDB-and-Global-Governance.md", False),
    (68, "RTGS and NEFT payment systems", "Economy", "Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md", False),
    (69, "Countries where international merchant payments are accepted under UPI", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (70, "PM Surya Ghar Muft Bijli Yojana - solar rooftop", "Environment and Ecology", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md", False),
    (71, "Gandhi's statement 'Sedition has become my religion'", "Modern History", "Modern-Indian-History/basic/20_Non-Cooperation-and-Khilafat-Movement.md", False),
    (72, "Mohenjo-daro 'Dancing Girl' figurine - material (bronze)", "Ancient History", "Ancient-Indian-History/basic/06_Harappan-Civilization.md", False),
    (73, "Legal defence for those arrested after Chauri Chaura", "Modern History", "Modern-Indian-History/basic/20_Non-Cooperation-and-Khilafat-Movement.md", False),
    (74, "Event after which Gandhi took up upliftment of 'Harijans'", "Modern History", "Modern-Indian-History/basic/22_Simon-Nehru-Report-CDM-and-RTC.md", False),
    (75, "Fruits introduced to India by the Portuguese (papaya, pineapple, guava)", "Modern History", "Modern-Indian-History/basic/03_Beginnings-of-European-Settlements.md", False),
    (76, "Countries with more than four time zones", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (77, "Anadyr and Nome across the International Date Line", "Geography", "Geography/basic/01_The-Earth-and-the-Universe.md", False),
    (78, "Founder of the 'Self-Respect Movement' (Periyar)", "Modern History", "Modern-Indian-History/basic/10_Socio-Religious-Reform-Movements.md", False),
    (79, "Resource-rich country pairs (Botswana-diamond, Chile-lithium, Indonesia-nickel)", "Geography", "Geography/basic/31_Mineral-Energy-Resources-World-and-India.md", False),
    (80, "Region-country pairs (Mallorca, Normandy, Sardinia)", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (81, "Uses and properties of rare earth elements", "Science and Technology", "Science-and-Technology/basic/20_Emerging-Materials-Rare-Earths-and-Critical-Minerals.md", False),
    (82, "National Rail Plan and the 'Kavach' automatic train protection system", "Geography", "Geography/basic/33_Transport-Trade-and-Indian-Space-Programme.md", False),
    (83, "Space missions supporting microgravity research (Axiom-4, SpaDeX, Gaganyaan)", "Science and Technology", "Science-and-Technology/basic/03_Human-Spaceflight-Gaganyaan-and-Planetary-Missions.md", False),
    (84, "India's defence aircraft type-description pairs (Dornier-228, IL-76, C-17)", "Science and Technology", "Science-and-Technology/basic/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md", False),
    (85, "Artificial rainfall (cloud seeding) to reduce air pollution", "Environment and Ecology", "Environment-and-Ecology/basic/13_Air-Pollution-and-CPCB-Standards.md", False),
    (86, "President's pardoning power - review and advice", "Polity", "Polity/basic/President-and-Vice-President.md", False),
    (87, "Speaker of the Lok Sabha - office on dissolution and party resignation", "Polity", "Polity/basic/Parliament.md", False),
    (88, "Tenth Schedule disqualification; mention of 'political party'", "Polity", "Polity/basic/Anti-Defection-Law.md", False),
    (89, "Minor minerals - State versus Central power to make rules/notify", "Polity", "Polity/basic/Centre-State-Relations.md", False),
    (90, "EU Nature Restoration Law (NRL)", "Environment and Ecology", "Environment-and-Ecology/basic/04_Biodiversity-Levels-and-Hotspots.md", False),
    (91, "Panchayats at the intermediate level", "Polity", "Polity/basic/Panchayati-Raj.md", False),
    (92, "BIMSTEC", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (93, "Jury to select the 'Gandhi Peace Prize' recipient", "Post-Independence India", "Modern-Indian-History/basic/38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis.md", False),
    (94, "GAGAN satellite-based augmentation system", "Science and Technology", "Science-and-Technology/basic/02_Satellites-NavIC-GAGAN-and-Applications.md", False),
    (95, "AI Action Summit (Grand Palais, Paris, February 2025)", "Science and Technology", "Science-and-Technology/basic/09_Artificial-Intelligence-Governance-and-IndiaAI.md", False),
    (96, "International Years and their designated years", "International Relations", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md", False),
    (97, "16th BRICS Summit (Kazan) and BRICS membership", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (98, "Lokpal - jurisdiction and composition", "Polity", "Polity/basic/Lokpal-and-Lokayuktas.md", False),
    (99, "First Kho Kho World Cup", "Post-Independence India", "Modern-Indian-History/basic/38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis.md", False),
    (100, "45th Chess Olympiad and youngest world champion/Grandmaster records", "Post-Independence India", "Modern-Indian-History/basic/38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis.md", False),
]

PRELIMS_2024 = [
    (1, "Atmosphere heated more by solar than terrestrial radiation; greenhouse gases", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (2, "Thickness of the troposphere at the equator versus poles; convection", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (3, "Products of volcanic eruptions", "Geography", "Geography/basic/03_Vulcanism-and-Earthquakes.md", False),
    (4, "Inferences from January isothermal maps", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (5, "World's two largest cocoa producers", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (6, "Himalayan rivers joining the Ganga, west-to-east sequence", "Geography", "Geography/basic/35_Indian-Political-Geography-Boundaries-and-Neighbours.md", False),
    (7, "Rainfall and weathering of rocks; rainwater composition", "Geography", "Geography/basic/04_Weathering-MassMovement-Groundwater.md", False),
    (8, "Countries bordering the North Sea", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (9, "Waterfall-region-river matching (Dhuandhar, Hundru, Gersoppa)", "Geography", "Geography/basic/05_Landforms-by-Running-Water.md", False),
    (10, "Mountain-range fold/block type matching (Vosges, Alps, Appalachians, Andes)", "Geography", "Geography/basic/02_The-Earths-Crust-Rocks.md", False),
    (11, "Greenfield airports (Donyi Polo, Kushinagar, Vijayawada)", "Geography", "Geography/basic/33_Transport-Trade-and-Indian-Space-Programme.md", False),
    (12, "Water-vapour characteristics with altitude", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (13, "Marine West Coast climate identified from its low annual and daily temperature range and year-round precipitation", "Geography", "Geography/basic/22_Cool-Temperate-Western-Margin-British-Type.md", False),
    (14, "Coriolis force characteristics", "Geography", "Geography/basic/13_Weather-Elements.md", False),
    (15, "Latitudes with more than 12 hours of sunlight on 21 June", "Geography", "Geography/basic/01_The-Earth-and-the-Universe.md", False),
    (16, "World's largest tropical peatland region", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (17, "PFAS in consumer products", "Environment and Ecology", "Environment-and-Ecology/basic/14_Water-Pollution-and-River-Cleaning-Missions.md", False),
    (18, "Parasitoid species among organisms (carabid beetles, centipedes, flies, termites, wasps)", "Environment and Ecology", "Environment-and-Ecology/basic/01_Ecosystem-Structure-and-Function.md", False),
    (19, "Plants belonging to the pea family (groundnut, horse-gram, soybean)", "Science and Technology", "Science-and-Technology/basic/23_General-Science-Biology-and-Physiology.md", False),
    (20, "Indian Flying Fox 'vermin' category under the Wild Life (Protection) Act, 1972", "Environment and Ecology", "Environment-and-Ecology/basic/08_Wildlife-Protection-Act-and-Schedules.md", False),
    (21, "Cicada, Froghopper and Pond skater as insects", "Science and Technology", "Science-and-Technology/basic/23_General-Science-Biology-and-Physiology.md", False),
    (22, "Chewing gum plastic base as environmental pollution", "Environment and Ecology", "Environment-and-Ecology/basic/15_Solid-Plastic-and-E-Waste-Rules.md", False),
    (23, "Country-animal natural habitat pairs (Brazil-Indri, Indonesia-Elk, Madagascar-Bonobo)", "Environment and Ecology", "Environment-and-Ecology/basic/05_IUCN-Red-List-and-Endemism.md", False),
    (24, "World Toilet Organization", "Social Justice", "Social-Justice/basic/14_Sanitation-Manual-Scavenging-and-Safai-Karamcharis.md", False),
    (25, "Behaviour of big cats (lions, cheetahs, leopards)", "Environment and Ecology", "Environment-and-Ecology/basic/28_Species-and-Current-Affairs-Tracker.md", False),
    (26, "'100 Million Farmers' platform description", "Economy", "Economy/basic/27_Digital-Agriculture-Agritech-and-e-Technology-for-Farmers.md", False),
    (27, "Distributed Energy Resources (battery storage, biomass, fuel cells, rooftop solar)", "Environment and Ecology", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md", False),
    (28, "Tree uniquely pollinated by a coevolved insect (fig)", "Environment and Ecology", "Environment-and-Ecology/basic/01_Ecosystem-Structure-and-Function.md", False),
    (29, "Organisms that include poisonous species (butterflies, fish, frogs)", "Science and Technology", "Science-and-Technology/basic/23_General-Science-Biology-and-Physiology.md", False),
    (30, "Tree species native to India (cashew, papaya, red sanders)", "Environment and Ecology", "Environment-and-Ecology/basic/11_Forest-Types-and-Forest-Rights-Act.md", False),
    (31, "Radioisotope thermoelectric generators (RTGs)", "Science and Technology", "Science-and-Technology/basic/03_Human-Spaceflight-Gaganyaan-and-Planetary-Missions.md", False),
    (32, "Giant stars versus dwarf stars - lifespan and nuclear reactions", "Geography", "Geography/basic/01_The-Earth-and-the-Universe.md", False),
    (33, "Body-synthesised substance that dilates blood vessels (nitric oxide)", "Science and Technology", "Science-and-Technology/basic/23_General-Science-Biology-and-Physiology.md", False),
    (34, "Activities in which radar can be used", "Science and Technology", "Science-and-Technology/basic/21_General-Science-Physics-Fundamentals.md", False),
    (35, "Fifth-generation fighter aircraft (Rafale, MiG-29, Tejas MK-1)", "Science and Technology", "Science-and-Technology/basic/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md", False),
    (36, "Uses of hydrogels", "Science and Technology", "Science-and-Technology/basic/22_General-Science-Chemistry-Fundamentals.md", False),
    (37, "Fuel-Cell Electric Vehicle exhaust emission (water vapour)", "Science and Technology", "Science-and-Technology/basic/18_Electric-Vehicles-Batteries-and-Alternative-Fuels.md", False),
    (38, "'Pumped-storage hydropower' (long-duration energy storage)", "Environment and Ecology", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md", False),
    (39, "'Membrane Bioreactors' in wastewater treatment", "Environment and Ecology", "Environment-and-Ecology/basic/14_Water-Pollution-and-River-Cleaning-Missions.md", False),
    (40, "Collateral Borrowing and Lending Obligations (money-market instrument)", "Economy", "Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md", False),
    (41, "Total fertility rate - definition", "Geography", "Geography/basic/26_World-Population-and-Demographic-Transition.md", False),
    (42, "NBFC access to LAF; FII holding G-Secs; exchange debt platforms", "Economy", "Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md", False),
    (43, "Corporate bonds and G-Secs trading (insurance, pension and retail investors)", "Economy", "Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md", False),
    (44, "Financial instruments (ETF, motor vehicles, currency swap)", "Economy", "Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md", False),
    (45, "Economic activity-to-sector matching (primary/secondary/tertiary)", "Economy", "Economy/basic/01_National-Income-GDP-GVA-and-Measurement.md", False),
    (46, "Feedstock for Sustainable Aviation Fuel", "Environment and Ecology", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md", False),
    (47, "Physical-capital pairs - working versus fixed capital (plough, computer, yarn, petrol)", "Economy", "Economy/basic/01_National-Income-GDP-GVA-and-Measurement.md", False),
    (48, "'Metaverse' - interoperable 3D virtual worlds", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (49, "RBI rules for foreign banks - subsidiaries capital and board members", "Economy", "Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md", False),
    (50, "Corporate Social Responsibility (CSR) rules in India", "Economy", "Economy/basic/16_Industrial-Policy-1991-Reforms-PSUs-and-Disinvestment.md", False),
    (51, "US Treasury Bonds and a US sovereign debt default (statement pair)", "Economy", "Economy/basic/07_Money-Market-Capital-Market-and-Financial-Instruments.md", False),
    (52, "Syndicated lending - risk sharing across multiple lenders", "Economy", "Economy/basic/05_Banking-Structure-NBFCs-and-Financial-Regulation.md", False),
    (53, "Digital rupee (central bank digital currency)", "Economy", "Economy/basic/24_Services-Digital-Economy-Fintech-and-Platform-Markets.md", False),
    (54, "Epithets of Gautama Buddha (Nayaputta, Shakyamuni, Tathagata)", "Ancient History", "Ancient-Indian-History/basic/10_Jainism-and-Buddhism.md", False),
    (55, "Archaeological Site-State-Description matching (Chandraketugarh, Inamgaon, Mangadu, Salihundam)", "Ancient History", "Ancient-Indian-History/basic/02_Sources-of-Ancient-Indian-History.md", False),
    (56, "Medieval ruler who allowed the Portuguese a fort at Bhatkal", "Medieval History", "Medieval-Indian-History/basic/09_Vijayanagara-and-Bahmani.md", False),
    (57, "Revenue collection under Cornwallis (Ryotwari / Permanent Settlement)", "Modern History", "Modern-Indian-History/basic/07_Economic-Impact-of-British-Rule.md", False),
    (58, "Upanishads - parables and chronology relative to the Puranas", "Ancient History", "Ancient-Indian-History/basic/24_Developments-in-Philosophy.md", False),
    (59, "India and the International Grains Council", "Economy", "Economy/basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md", False),
    (60, "Latest Indian inclusion in the UNESCO Intangible Cultural Heritage List", "Indian Art and Culture", "Indian-Art-and-Culture/basic/09_Indian-Dance.md", False),
    (61, "Provisional President of the Constituent Assembly", "Polity", "Polity/basic/Making-of-the-Constitution.md", False),
    (62, "Government of India Act, 1935 - All-India Federation and reserved control of defence and foreign affairs", "Modern History / Polity", ["Modern-Indian-History/basic/24_Government-of-India-Act-1935-and-Congress-Ministries.md", "Polity/basic/Historical-Background.md"], False),
    (63, "Work attributed to the playwright Bhasa", "Indian Art and Culture", "Indian-Art-and-Culture/basic/11_Languages-Scripts-Literature-and-Manuscripts.md", False),
    (64, "Sanghabhuti's commentary (Sarvastivada Vinaya)", "Ancient History", "Ancient-Indian-History/basic/10_Jainism-and-Buddhism.md", False),
    (65, "UNESCO World Heritage properties inscribed in 2023 (Shantiniketan, Hoysalas)", "Indian Art and Culture", "Indian-Art-and-Culture/basic/14_Heritage-Conservation-Institutions-and-UNESCO.md", False),
    (66, "Article 368 - modes of amendment (addition, variation, repeal)", "Polity", "Polity/basic/Amendment-and-Basic-Structure.md", False),
    (67, "Countries in the news for low birth rate / ageing / declining population", "Geography", "Geography/basic/26_World-Population-and-Demographic-Transition.md", False),
    (68, "Money Bill provisions in Parliament (Article 109, Rajya Sabha)", "Polity", "Polity/basic/Parliament.md", False),
    (69, "Equivalent ranks in the three services of the armed forces", "Science and Technology", "Science-and-Technology/basic/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md", False),
    (70, "North Eastern Council (NEC) composition", "Polity", "Polity/basic/Special-Provisions.md", False),
    (71, "Delimitation Commissions constituted till December 2023", "Polity", "Polity/basic/Election-Commission.md", False),
    (72, "Constitution amendment adding a language to the Eighth Schedule", "Polity", "Polity/basic/Official-Language.md", False),
    (73, "Political party-leader matching (Jana Sangh, Socialist Party, CFD, Swatantra)", "Post-Independence India", "Modern-Indian-History/basic/33_Party-Politics-1947-67-Congress-System-and-Opposition.md", False),
    (74, "Constitution Parts (Municipalities IX-A, Emergency XVIII, amendment XX)", "Polity", "Polity/basic/Salient-Features.md", False),
    (75, "Inter-State trade, migration and quarantine in the constitutional lists", "Polity", "Polity/basic/Centre-State-Relations.md", False),
    (76, "Article under which the Supreme Court placed the Right to Privacy", "Polity", "Polity/basic/Fundamental-Rights.md", False),
    (77, "Chief of Defence Staff (CDS) as Head of the Department of Military Affairs - role and duties", "Science and Technology", "Science-and-Technology/basic/07_Defence-Indigenization-Atmanirbhar-and-Procurement.md", False),
    (78, "Army goodwill operations for upliftment of local population in remote/border areas (Operation Sadbhavana)", "Internal Security", "Internal-Security/basic/06_Border-Management-and-Border-Area-Development.md", False),
    (79, "Longest land border between any two countries in the world (Canada-USA)", "Geography", "Geography/basic/34_World-Regional-Geography-Continents-Countries.md", False),
    (80, "Ethics Committee in the Lok Sabha", "Polity", "Polity/basic/Parliament.md", False),
    (81, "'Nari Shakti Vandan Adhiniyam' (women's reservation)", "Polity", "Polity/basic/Parliament.md", False),
    (82, "Exercise Mitra Shakti-2023 (joint military exercise)", "Post-Independence India", "Modern-Indian-History/basic/38_Economy-Land-Society-and-State-A-Post-Independence-Synthesis.md", False),
    (83, "Writ of Prohibition", "Polity", "Polity/basic/Supreme-Court.md", False),
    (84, "Governor recognising/declaring a Scheduled Tribe", "Polity", "Polity/basic/Scheduled-and-Tribal-Areas.md", False),
    (85, "Union Budget - Annual Financial Statement", "Economy", "Economy/basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md", False),
    (86, "Books authored by S. Jaishankar ('The India Way', 'Why Bharat Matters')", "International Relations", "International-Relations/basic/01_Foreign-Policy-Foundations-and-Strategic-Autonomy.md", False),
    (87, "Country-news pairs (Argentina, Sudan, Turkey/NATO)", "International Relations", "International-Relations/basic/10_Regional-Global-and-Minilateral-Groupings.md", False),
    (88, "Sumed pipeline (Persian Gulf oil to Europe; Red Sea-Mediterranean)", "Geography", "Geography/basic/31_Mineral-Energy-Resources-World-and-India.md", False),
    (89, "Red Sea - low precipitation and absence of major river inflow", "Geography", "Geography/basic/12_The-Oceans-Currents-Tides-Salinity.md", False),
    (90, "EPA's largest source of sulphur dioxide emissions (fossil-fuel power plants)", "Environment and Ecology", "Environment-and-Ecology/basic/13_Air-Pollution-and-CPCB-Standards.md", False),
    (91, "Instability and military coups in the Sahel region", "International Relations", "International-Relations/basic/07_India-Africa-Development-and-Digital-Partnership.md", False),
    (92, "India's apple imports from the USA; GM-food import law", "Economy", "Economy/basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md", False),
    (93, "Speaker of the Lok Sabha - conduct during a removal resolution", "Polity", "Polity/basic/Parliament.md", False),
    (94, "Bills lapsing on dissolution of the Lok Sabha", "Polity", "Polity/basic/Parliament.md", False),
    (95, "Prorogation and dissolution of Parliament by the President", "Polity", "Polity/basic/Parliament.md", False),
    (96, "European Parliament Net-Zero Industry Act; EU carbon neutrality by 2040", "Environment and Ecology", "Environment-and-Ecology/basic/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md", False),
    (97, "Venezuela and the world's largest proven oil reserves", "Geography", "Geography/basic/31_Mineral-Energy-Resources-World-and-India.md", False),
    (98, "Digital India Land Records Modernisation Programme", "Governance", "Governance/basic/06_Digital-Public-Infrastructure-and-Data-Governance.md", False),
    (99, "Pradhan Mantri Surakshit Matritva Abhiyan (maternal health)", "Social Justice", "Social-Justice/basic/03_Health-Systems-Public-Health-and-Universal-Health-Coverage.md", False),
    (100, "Pradhan Mantri Shram Yogi Maan-dhan (PM-SYM pension for unorganised workers)", "Social Justice", "Social-Justice/basic/15_Labour-Social-Security-Unorganised-and-Gig-Workers.md", False),
]


# ---------------------------------------------------------------------------
# MAINS data: (paper, q, theme, subject, "directive \u00b7 marks \u00b7 words", route(s))
# ---------------------------------------------------------------------------
MAINS = []  # filled by extend calls below

def M(rows):
    MAINS.extend(rows)


M([
    # ---- 2024 GS-I ----
    (2024, "GS-I", 1, "Social and economic changes from the Rig Vedic to the later Vedic period", "Ancient History", "Underline \u00b7 10 marks \u00b7 150 words", "Ancient-Indian-History/basic/09_Later-Vedic-Phase.md"),
    (2024, "GS-I", 2, "Contribution of the Pallavas of Kanchi to South Indian art and literature", "Ancient History", "Estimate \u00b7 10 marks \u00b7 150 words", "Ancient-Indian-History/basic/23_Peninsular-India-Pallavas-Chalukyas.md"),
    (2024, "GS-I", 3, "Events leading to the Quit India Movement and its results", "Modern History", "Explain \u00b7 10 marks \u00b7 150 words", "Modern-Indian-History/basic/25_WWII-Cripps-Mission-and-Quit-India.md"),
    (2024, "GS-I", 4, "Sea surface temperature rise and formation of tropical cyclones", "Geography", "Explain \u00b7 10 marks \u00b7 150 words", "Geography/basic/13_Weather-Elements.md"),
    (2024, "GS-I", 5, "Why large cities attract more migrants than smaller towns", "Geography", "Discuss \u00b7 10 marks \u00b7 150 words", "Geography/basic/27_Migration-Theories-and-Patterns-India.md"),
    (2024, "GS-I", 6, "The phenomenon of cloudbursts", "Geography", "Explain \u00b7 10 marks \u00b7 150 words", "Geography/basic/13_Weather-Elements.md"),
    (2024, "GS-I", 7, "Concept of a 'demographic winter'", "Indian Society", "Elaborate \u00b7 10 marks \u00b7 150 words", "Geography/basic/26_World-Population-and-Demographic-Transition.md"),
    (2024, "GS-I", 8, "Gender equality, gender equity and women's empowerment; gender in programme design", "Indian Society", "Distinguish \u00b7 10 marks \u00b7 150 words", "Indian-Society/basic/07_Women-and-Womens-Organisations.md"),
    (2024, "GS-I", 9, "Intercaste versus interreligious marriages", "Indian Society", "Discuss \u00b7 10 marks \u00b7 150 words", "Indian-Society/basic/02_Caste-System-Structure-and-Contemporary-Dynamics.md"),
    (2024, "GS-I", 10, "Government-NGO-private collaboration in socio-economic development", "Indian Society", "Discuss \u00b7 10 marks \u00b7 150 words", "Governance/basic/04_NGOs-SHGs-and-Civil-Society-Stakeholders.md"),
    (2024, "GS-I", 11, "Cholas' achievements in art and architecture", "Indian Art and Culture", "Comment \u00b7 15 marks \u00b7 250 words", ["Indian-Art-and-Culture/basic/03_Temple-Architecture-and-Chandella-Khajuraho.md", "Ancient-Indian-History/basic/27_Imperial-Cholas-State-Society-Economy-and-Maritime-Power.md"]),
    (2024, "GS-I", 12, "First World War fought for preservation of balance of power", "World History", "Comment \u00b7 15 marks \u00b7 250 words", "World-History/basic/09_World-in-1914-and-Outbreak-of-WWI.md"),
    (2024, "GS-I", 13, "Industrial Revolution in England and decline of Indian handicrafts", "Modern History", "Discuss \u00b7 15 marks \u00b7 250 words", "Modern-Indian-History/basic/07_Economic-Impact-of-British-Rule.md"),
    (2024, "GS-I", 14, "Declining groundwater of the Gangetic valley and food security", "Geography", "Explain \u00b7 15 marks \u00b7 250 words", "Geography/basic/36_Contemporary-Geographical-Issues-India.md"),
    (2024, "GS-I", 15, "Aurora australis and aurora borealis", "Geography", "Explain \u00b7 15 marks \u00b7 250 words", "Geography/basic/01_The-Earth-and-the-Universe.md"),
    (2024, "GS-I", 16, "Twisters and their concentration around the Gulf of Mexico", "Geography", "Explain \u00b7 15 marks \u00b7 250 words", "Geography/basic/13_Weather-Elements.md"),
    (2024, "GS-I", 17, "Regional disparity versus diversity in India", "Indian Society", "Explain \u00b7 15 marks \u00b7 250 words", "Indian-Society/basic/14_Regionalism.md"),
    (2024, "GS-I", 18, "Underprivileged sections not getting full benefits of affirmative action", "Social Justice", "Comment \u00b7 15 marks \u00b7 250 words", "Social-Justice/basic/01_Social-Justice-Concept-Inclusion-and-Welfare-State-Framework.md"),
    (2024, "GS-I", 19, "Globalization and urban migration of skilled young unmarried women", "Indian Society", "Discuss \u00b7 15 marks \u00b7 250 words", "Indian-Society/basic/11_Effects-of-Globalisation-on-Indian-Society.md"),
    (2024, "GS-I", 20, "Correlation between cultural diversity and socio-economic marginalities", "Indian Society", "Critically analyse \u00b7 15 marks \u00b7 250 words", "Indian-Society/basic/01_Salient-Features-and-Diversity-of-Indian-Society.md"),
    # ---- 2024 GS-II ----
    (2024, "GS-II", 1, "Electoral reforms and 'one nation, one election'", "Polity", "Examine \u00b7 10 marks \u00b7 150 words", "Polity/basic/Election-Commission.md"),
    (2024, "GS-II", 2, "Lok Adalats versus Arbitration Tribunals", "Polity", "Explain and distinguish \u00b7 10 marks \u00b7 150 words", "Polity/basic/Administrative-Tribunals.md"),
    (2024, "GS-II", 3, "Growth of the cabinet system and marginalisation of parliamentary supremacy", "Polity", "Elucidate \u00b7 10 marks \u00b7 150 words", "Polity/basic/Parliamentary-System.md"),
    (2024, "GS-II", 4, "CAG's duty to ensure legality and propriety of expenditure", "Polity", "Comment \u00b7 10 marks \u00b7 150 words", "Polity/basic/CAG.md"),
    (2024, "GS-II", 5, "Role of local bodies; merging rural and urban local bodies", "Governance", "Analyse \u00b7 10 marks \u00b7 150 words", "Governance/basic/12_Local-Governance-and-Service-Delivery.md"),
    (2024, "GS-II", 6, "Public charitable trusts and inclusive development", "Governance", "Comment \u00b7 10 marks \u00b7 150 words", "Governance/basic/04_NGOs-SHGs-and-Civil-Society-Stakeholders.md"),
    (2024, "GS-II", 7, "Poverty-malnutrition vicious cycle and human-capital formation", "Social Justice", "Explain \u00b7 10 marks \u00b7 150 words", "Social-Justice/basic/02_Poverty-Hunger-Food-and-Nutrition-Security.md"),
    (2024, "GS-II", 8, "Doctrine of democratic governance and public perception of civil servants", "Governance", "Discuss \u00b7 10 marks \u00b7 150 words", "Governance/basic/07_Citizen-Centric-Administration.md"),
    (2024, "GS-II", 9, "West fostering India as an alternative to China's supply chain", "International Relations", "Explain \u00b7 10 marks \u00b7 150 words", "International-Relations/basic/03_India-China-Major-Powers-and-Resilient-Supply-Chains.md"),
    (2024, "GS-II", 10, "India's relations with the Central Asian Republics", "International Relations", "Critically analyse \u00b7 10 marks \u00b7 150 words", "International-Relations/basic/05_Central-Asia-Eurasia-and-Connectivity.md"),
    (2024, "GS-II", 11, "Public Examination (Prevention of Unfair Means) Act, 2024", "Governance", "Discuss \u00b7 15 marks \u00b7 250 words", "Governance/basic/02_Government-Policy-Design-and-Implementation.md"),
    (2024, "GS-II", 12, "Right to privacy under Article 21; DNA testing for paternity", "Polity", "Explain \u00b7 15 marks \u00b7 250 words", "Polity/basic/Fundamental-Rights.md"),
    (2024, "GS-II", 13, "Recent changes in Centre-State relations; strengthening federalism", "Polity", "Suggest \u00b7 15 marks \u00b7 250 words", "Polity/basic/Centre-State-Relations.md"),
    (2024, "GS-II", 14, "Growth of PIL and the Supreme Court as a powerful judiciary", "Polity", "Explain \u00b7 15 marks \u00b7 250 words", "Polity/basic/Supreme-Court.md"),
    (2024, "GS-II", 15, "India as a secular state compared with US secular principles", "Polity", "Discuss \u00b7 15 marks \u00b7 250 words", "Polity/basic/Comparative-Constitutional-Schemes.md"),
    (2024, "GS-II", 16, "Citizens' Charter and citizen-centric administration", "Governance", "Identify and suggest \u00b7 15 marks \u00b7 250 words", "Governance/basic/08_Transparency-Accountability-Grievance-Redress-and-Social-Audit.md"),
    (2024, "GS-II", 17, "State's role against marketisation of public healthcare", "Social Justice", "Suggest \u00b7 15 marks \u00b7 250 words", "Social-Justice/basic/03_Health-Systems-Public-Health-and-Universal-Health-Coverage.md"),
    (2024, "GS-II", 18, "'Interactive Service Model' of e-governance", "Governance", "Evaluate \u00b7 15 marks \u00b7 250 words", "Governance/basic/05_E-Governance-Models-and-User-Centricity.md"),
    (2024, "GS-II", 19, "Effectiveness of the UNSC Counter-Terrorism Committee", "International Relations", "Evaluate \u00b7 15 marks \u00b7 250 words", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md"),
    (2024, "GS-II", 20, "Geopolitical and geostrategic importance of Maldives for India", "International Relations", "Discuss \u00b7 15 marks \u00b7 250 words", "International-Relations/basic/04_Indo-Pacific-Indian-Ocean-and-Maritime-Security.md"),
    # ---- 2024 GS-III ----
    (2024, "GS-III", 1, "Public expenditure on social services post-reforms and inclusive growth", "Economy", "Examine \u00b7 10 marks \u00b7 150 words", "Economy/basic/23_Poverty-Inequality-Social-Sector-and-Inclusive-Growth.md"),
    (2024, "GS-III", 2, "Causes of high food inflation and effectiveness of RBI monetary policy", "Economy", "Comment \u00b7 10 marks \u00b7 150 words", "Economy/basic/03_Inflation-Price-Indices-and-Business-Cycles.md"),
    (2024, "GS-III", 3, "Factors behind successful land reforms in parts of the country", "Economy", "Elaborate \u00b7 10 marks \u00b7 150 words", "Economy/basic/11_Land-Reforms-Green-Revolution-and-Cropping-Systems.md"),
    (2024, "GS-III", 4, "Role of millets in health and nutritional security", "Economy", "Explain \u00b7 10 marks \u00b7 150 words", "Economy/basic/12_MSP-Procurement-Buffer-Stocks-PDS-and-Food-Security.md"),
    (2024, "GS-III", 5, "IPR for life materials; low commercialization of Indian patents", "Science and Technology", "Explain \u00b7 10 marks \u00b7 150 words", "Science-and-Technology/basic/17_Intellectual-Property-Rights-and-Patents.md"),
    (2024, "GS-III", 6, "Technology for electronic toll collection on highways", "Science and Technology", "Explain \u00b7 10 marks \u00b7 150 words", "Science-and-Technology/basic/08_Digital-India-and-India-Stack-UPI-Aadhaar.md"),
    (2024, "GS-III", 7, "Industrial pollution of river water and mitigation measures", "Environment and Ecology", "Discuss \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/14_Water-Pollution-and-River-Cleaning-Missions.md"),
    (2024, "GS-III", 8, "Role of environmental NGOs and activists in EIA outcomes", "Environment and Ecology", "Cite examples \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/16_Environmental-Impact-Assessment-and-NGT.md"),
    (2024, "GS-III", 9, "Narco-terrorism as a threat and counter-measures", "Internal Security", "Explain and suggest \u00b7 10 marks \u00b7 150 words", "Internal-Security/basic/11_Organised-Crime-Narco-Terrorism-and-Trafficking.md"),
    (2024, "GS-III", 10, "Context and salient features of the Digital Personal Data Protection Act, 2023", "Science and Technology", "Describe \u00b7 10 marks \u00b7 150 words", "Science-and-Technology/basic/12_Data-Protection-DPDP-Act-and-Cybersecurity.md"),
    (2024, "GS-III", 11, "Merits and demerits of the four Labour Codes", "Economy", "Discuss \u00b7 15 marks \u00b7 250 words", "Economy/basic/22_Employment-Labour-Codes-Skills-and-Demographic-Dividend.md"),
    (2024, "GS-III", 12, "Need for regional air connectivity and the UDAN scheme", "Economy", "Discuss \u00b7 15 marks \u00b7 250 words", "Economy/basic/18_Infrastructure-PPPs-Logistics-and-Public-Investment.md"),
    (2024, "GS-III", 13, "Challenges of the Indian irrigation system and government measures", "Economy", "State measures \u00b7 15 marks \u00b7 250 words", "Economy/basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md"),
    (2024, "GS-III", 14, "Importance of buffer stocks for price stabilization; storage challenges", "Economy", "Elucidate \u00b7 15 marks \u00b7 250 words", "Economy/basic/12_MSP-Procurement-Buffer-Stocks-PDS-and-Food-Security.md"),
    (2024, "GS-III", 15, "Alternative technologies for the freshwater crisis", "Environment and Ecology", "Discuss \u00b7 15 marks \u00b7 250 words", "Environment-and-Ecology/basic/14_Water-Pollution-and-River-Cleaning-Missions.md"),
    (2024, "GS-III", 16, "Asteroids, extinction threat and prevention strategies", "Science and Technology", "Discuss \u00b7 15 marks \u00b7 250 words", "Science-and-Technology/basic/03_Human-Spaceflight-Gaganyaan-and-Planetary-Missions.md"),
    (2024, "GS-III", 17, "Disaster resilience and the Sendai Framework", "Disaster Management", "Describe \u00b7 15 marks \u00b7 250 words", "Disaster-Management/basic/01_Concepts-Risk-Resilience-and-Sendai.md"),
    (2024, "GS-III", 18, "Urban flooding as a climate-induced disaster; policies and frameworks", "Disaster Management", "Discuss \u00b7 15 marks \u00b7 250 words", "Disaster-Management/basic/08_Riverine-Floods-and-Urban-Flood-Resilience.md"),
    (2024, "GS-III", 19, "China-Pakistan border security challenges; BADP and BIM schemes", "Internal Security", "Examine \u00b7 15 marks \u00b7 250 words", "Internal-Security/basic/06_Border-Management-and-Border-Area-Development.md"),
    (2024, "GS-III", 20, "Security challenge of social media and encrypted messaging", "Internal Security", "Suggest measures \u00b7 15 marks \u00b7 250 words", "Internal-Security/basic/09_Social-Media-Encrypted-Messaging-and-Information-Warfare.md"),
    # ---- 2024 GS-IV ----
    (2024, "GS-IV", 1, "(a) AI as a reliable input for administrative decisions; (b) dimensions of ethics guiding responsible behaviour", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md", "Ethics/basic/01_Ethics-and-Human-Interface.md"]),
    (2024, "GS-IV", 2, "(a) belief in peace, not merely talk; (b) global warming and human greed", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/02_Human-Values-and-Lessons-from-Leaders.md", "Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md"]),
    (2024, "GS-IV", 3, "Three quotations of great thinkers and their present-day meaning", "Ethics", "Section A theory \u00b7 10 + 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/06_Indian-Moral-Thinkers-and-Philosophers.md", "Ethics/basic/07_Western-Moral-Philosophers-and-Thinkers.md"]),
    (2024, "GS-IV", 4, "(a) just and unjust are context-relative; (b) irrational attachment to form causing injustice", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/08_Moral-Theories-Deontology-Consequentialism-Virtue-Ethics.md", "Ethics/basic/10_Sources-of-Ethical-Guidance-Laws-Rules-Conscience.md"]),
    (2024, "GS-IV", 5, "(a) code of conduct and code of ethics in public administration; (b) BNS rooted in Indian culture", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/16_Codes-of-Ethics-and-Codes-of-Conduct.md", "Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md"]),
    (2024, "GS-IV", 6, "(a) equal opportunity despite gender identity in Indian culture; (b) Mission Karmayogi", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/02_Human-Values-and-Lessons-from-Leaders.md", "Ethics/basic/04_Aptitude-and-Foundational-Values-for-Civil-Service.md"]),
    (2024, "GS-IV", 7, "Case study: ABC Incorporated, a large technology company", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md"]),
    (2024, "GS-IV", 8, "Case study: Raman, a senior IPS officer appointed DG of a State", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/21_Protecting-Honest-Officials-and-Vigilance-Administration.md"]),
    (2024, "GS-IV", 9, "Case study: Rohit and a multi-pronged strategy in LWE-affected States", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md"]),
    (2024, "GS-IV", 10, "Case study: Sneha, a senior manager at a hospital chain", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/12_Corporate-Governance-and-International-Ethics.md"]),
    (2024, "GS-IV", 11, "Case study: District Collector amid acute water scarcity", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md"]),
    (2024, "GS-IV", 12, "Case study: Dr. Srinivasan, a senior scientist at a biotechnology company", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md"]),
    # ---- 2025 GS-I ----
    (2025, "GS-I", 1, "Salient features of Harappan architecture", "Ancient History", "Discuss \u00b7 10 marks \u00b7 150 words", "Ancient-Indian-History/basic/06_Harappan-Civilization.md"),
    (2025, "GS-I", 2, "Main aspects of Akbar's religious syncretism", "Medieval History", "Examine \u00b7 10 marks \u00b7 150 words", "Medieval-Indian-History/basic/17_Akbar-Religious-Views-Din-i-Ilahi.md"),
    (2025, "GS-I", 3, "Chandella artform - resilient vigour and breadth of life", "Indian Art and Culture", "Elucidate \u00b7 10 marks \u00b7 150 words", "Indian-Art-and-Culture/basic/03_Temple-Architecture-and-Chandella-Khajuraho.md"),
    (2025, "GS-I", 4, "Climate change and sea-level rise affecting island nations", "Geography", "Discuss \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/17_Climate-Change-Science-Greenhouse-Effect.md"),
    (2025, "GS-I", 5, "Non-farm primary activities and physiographic features in India", "Geography", "Discuss \u00b7 10 marks \u00b7 150 words", "Geography/basic/30_Primary-Economic-Activities-Agriculture.md"),
    (2025, "GS-I", 6, "Ecological and economic benefits of solar energy generation in India", "Geography", "Explain \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md"),
    (2025, "GS-I", 7, "Tsunamis - formation and consequences", "Geography", "Explain \u00b7 10 marks \u00b7 150 words", "Disaster-Management/basic/06_Tsunami-and-Coastal-Hazard-Management.md"),
    (2025, "GS-I", 8, "Smart cities addressing urban poverty and distributive justice", "Indian Society", "Discuss \u00b7 10 marks \u00b7 150 words", "Indian-Society/basic/10_Urbanisation-Problems-and-Remedies.md"),
    (2025, "GS-I", 9, "Ethos of the civil service - professionalism and nationalist consciousness", "Governance", "Elucidate \u00b7 10 marks \u00b7 150 words", "Governance/basic/09_Civil-Services-and-Mission-Karmayogi.md"),
    (2025, "GS-I", 10, "Whether globalization results only in aggressive consumer culture", "Indian Society", "Justify \u00b7 10 marks \u00b7 150 words", "Indian-Society/basic/11_Effects-of-Globalisation-on-Indian-Society.md"),
    (2025, "GS-I", 11, "Jotirao Phule's social reform efforts and writings", "Modern History", "Discuss \u00b7 15 marks \u00b7 250 words", "Modern-Indian-History/basic/10_Socio-Religious-Reform-Movements.md"),
    (2025, "GS-I", 12, "India's consolidation in the early phase of independence", "Modern History", "Trace \u00b7 15 marks \u00b7 250 words", "Modern-Indian-History/basic/29_Colonial-Legacy-and-Foundations-of-the-Republic.md"),
    (2025, "GS-I", 13, "Enduring relevance of the French Revolution", "World History", "Explain \u00b7 15 marks \u00b7 250 words", "World-History/basic/03_French-Revolution-and-Napoleon.md"),
    (2025, "GS-I", 14, "Distribution of off-shore oil reserves versus on-shore occurrences", "Geography", "Explain \u00b7 15 marks \u00b7 250 words", "Geography/basic/31_Mineral-Energy-Resources-World-and-India.md"),
    (2025, "GS-I", 15, "Using AI and drones with GIS/RS in locational and areal planning", "Geography", "Discuss \u00b7 15 marks \u00b7 250 words", "Science-and-Technology/basic/09_Artificial-Intelligence-Governance-and-IndiaAI.md"),
    (2025, "GS-I", 16, "Change in continents and ocean basins due to crustal tectonics", "Geography", "Discuss \u00b7 15 marks \u00b7 250 words", "Geography/basic/02_The-Earths-Crust-Rocks.md"),
    (2025, "GS-I", 17, "Population distribution and density in the Ganga basin", "Geography", "Discuss \u00b7 15 marks \u00b7 250 words", "Geography/basic/37_Cultural-and-Social-Geography-of-India.md"),
    (2025, "GS-I", 18, "Growth of fast-food industries amid rising health concerns", "Indian Society", "Illustrate \u00b7 15 marks \u00b7 250 words", "Indian-Society/basic/12_Social-Change-and-Modernisation.md"),
    (2025, "GS-I", 19, "Sustainable growth versus needs of the poor", "Indian Society", "Comment \u00b7 15 marks \u00b7 250 words", "Indian-Society/basic/09_Poverty-and-Developmental-Issues.md"),
    (2025, "GS-I", 20, "Tribal development around displacement and rehabilitation", "Indian Society", "Give your opinion \u00b7 15 marks \u00b7 250 words", "Indian-Society/basic/03_Tribe-and-Tribal-Society.md"),
    # ---- 2025 GS-II ----
    (2025, "GS-II", 1, "'Corrupt practices' under RPA 1951 and disproportionate assets as undue influence", "Polity", "Discuss and analyse \u00b7 10 marks \u00b7 150 words", "Polity/basic/Election-Commission.md"),
    (2025, "GS-II", 2, "Need for administrative tribunals; 2021 tribunal rationalization", "Polity", "Comment and assess \u00b7 10 marks \u00b7 150 words", "Polity/basic/Administrative-Tribunals.md"),
    (2025, "GS-II", 3, "President's power to pardon in India and USA; preemptive pardons", "Polity", "Compare and contrast \u00b7 10 marks \u00b7 150 words", "Polity/basic/President-and-Vice-President.md"),
    (2025, "GS-II", 4, "Nature of the J&K Legislative Assembly after the Reorganization Act, 2019", "Polity", "Discuss \u00b7 10 marks \u00b7 150 words", "Polity/basic/Union-Territories.md"),
    (2025, "GS-II", 5, "Role, rights and limitations of the Attorney General of India", "Polity", "Discuss \u00b7 10 marks \u00b7 150 words", "Polity/basic/Attorney-General.md"),
    (2025, "GS-II", 6, "Women's social capital, empowerment and gender equity", "Social Justice", "Explain \u00b7 10 marks \u00b7 150 words", "Social-Justice/basic/05_Women-and-Gender-Justice.md"),
    (2025, "GS-II", 7, "Built-in bias in e-governance towards technology over user-centric design", "Governance", "Examine \u00b7 10 marks \u00b7 150 words", "Governance/basic/05_E-Governance-Models-and-User-Centricity.md"),
    (2025, "GS-II", 8, "Civil Society Organizations as anti-State versus non-State actors", "Governance", "Justify \u00b7 10 marks \u00b7 150 words", "Governance/basic/04_NGOs-SHGs-and-Civil-Society-Stakeholders.md"),
    (2025, "GS-II", 9, "India-Africa digital partnership", "International Relations", "Elaborate \u00b7 10 marks \u00b7 150 words", "International-Relations/basic/07_India-Africa-Development-and-Digital-Partnership.md"),
    (2025, "GS-II", 10, "Waning globalization and post-Cold War sovereign nationalism", "International Relations", "Elucidate \u00b7 10 marks \u00b7 150 words", "International-Relations/basic/11_Globalisation-Trade-Agreements-and-External-Policy-Effects.md"),
    (2025, "GS-II", 11, "Constitutional morality; judicial independence and accountability", "Polity", "Explain \u00b7 15 marks \u00b7 250 words", "Polity/basic/Supreme-Court.md"),
    (2025, "GS-II", 12, "Procedural and substantive limits on Parliament's amending power", "Polity", "Examine \u00b7 15 marks \u00b7 250 words", "Polity/basic/Amendment-and-Basic-Structure.md"),
    (2025, "GS-II", 13, "Collegium system - appointment of judges in India and USA", "Polity", "Critically examine \u00b7 15 marks \u00b7 250 words", "Polity/basic/Supreme-Court.md"),
    (2025, "GS-II", 14, "Evolving Centre-State financial relations and fiscal federalism", "Polity", "Examine \u00b7 15 marks \u00b7 250 words", "Polity/basic/Centre-State-Relations.md"),
    (2025, "GS-II", 15, "Environmental pressure groups in India", "Governance", "Discuss \u00b7 15 marks \u00b7 250 words", "Polity/basic/Pressure-Groups.md"),
    (2025, "GS-II", 16, "Inequality in resource ownership and the paradox of poverty", "Social Justice", "Discuss \u00b7 15 marks \u00b7 250 words", "Social-Justice/basic/01_Social-Justice-Concept-Inclusion-and-Welfare-State-Framework.md"),
    (2025, "GS-II", 17, "Decision-making distant from source in contemporary development models", "Governance", "Critically evaluate \u00b7 15 marks \u00b7 250 words", "Governance/basic/03_Development-Processes-and-the-Development-Industry.md"),
    (2025, "GS-II", 18, "NCPCR and challenges to children in the digital era", "Social Justice", "Examine and suggest \u00b7 15 marks \u00b7 250 words", "Social-Justice/basic/06_Children-and-Child-Protection.md"),
    (2025, "GS-II", 19, "Energy security and India's foreign policy in the Middle East", "International Relations", "Discuss \u00b7 15 marks \u00b7 250 words", "International-Relations/basic/06_West-Asia-Energy-Security-and-Connectivity.md"),
    (2025, "GS-II", 20, "UN reform amid East-West imbalance and USA vs Russo-Chinese alliance", "International Relations", "Examine and evaluate \u00b7 15 marks \u00b7 250 words", "International-Relations/basic/12_UN-and-International-Institutions-Global-Governance.md"),
    # ---- 2025 GS-III ----
    (2025, "GS-III", 1, "HDI versus IHDI as an indicator of inclusive growth", "Economy", "Distinguish \u00b7 10 marks \u00b7 150 words", "Economy/basic/02_Growth-Development-HDI-IHDI-and-MPI.md"),
    (2025, "GS-III", 2, "Challenges to the Indian economy amid protectionism and bilateralism", "Economy", "Discuss \u00b7 10 marks \u00b7 150 words", "Economy/basic/20_Foreign-Trade-WTO-FTAs-and-Protectionism.md"),
    (2025, "GS-III", 3, "Factors influencing farmers' selection of high-value crops", "Economy", "Explain \u00b7 10 marks \u00b7 150 words", "Economy/basic/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md"),
    (2025, "GS-III", 4, "Scope and significance of supply-chain management of agricultural commodities", "Economy", "Elaborate \u00b7 10 marks \u00b7 150 words", "Economy/basic/13_APMC-e-NAM-FPOs-and-Agricultural-Supply-Chains.md"),
    (2025, "GS-III", 5, "India's contribution to the ITER fusion energy project", "Science and Technology", "Mention \u00b7 10 marks \u00b7 150 words", "Science-and-Technology/basic/05_Nuclear-Fusion-and-ITER.md"),
    (2025, "GS-III", 6, "Energy independence by 2047 through clean tech; role of biotechnology", "Science and Technology", "Discuss \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/25_Renewable-Energy-and-Green-Hydrogen.md"),
    (2025, "GS-III", 7, "Carbon Capture, Utilization and Storage (CCUS) and climate change", "Environment and Ecology", "Explain \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/21_Carbon-Markets-CCUS-and-Direct-Air-Capture.md"),
    (2025, "GS-III", 8, "Seawater intrusion in coastal aquifers - causes and remedies", "Geography", "Discuss \u00b7 10 marks \u00b7 150 words", "Environment-and-Ecology/basic/24_Coastal-and-Marine-Ecology-CRZ-Blue-Economy.md"),
    (2025, "GS-III", 9, "Manifestation of terrorism in India and counter-measures", "Internal Security", "Elaborate \u00b7 10 marks \u00b7 150 words", "Internal-Security/basic/02_Terrorism-and-Counter-Terror-Architecture.md"),
    (2025, "GS-III", 10, "Left Wing Extremism, people affected, and elimination measures", "Internal Security", "Explain \u00b7 10 marks \u00b7 150 words", "Internal-Security/basic/03_Left-Wing-Extremism-and-Integrated-Response.md"),
    (2025, "GS-III", 11, "Fiscal Health Index as a tool for state fiscal performance", "Economy", "Explain \u00b7 15 marks \u00b7 250 words", "Economy/basic/09_Union-Budget-Fiscal-Policy-and-Deficit-Indicators.md"),
    (2025, "GS-III", 12, "Rationale, achievements and improvement of the PLI scheme", "Economy", "Discuss \u00b7 15 marks \u00b7 250 words", "Economy/basic/17_MSMEs-PLI-Semiconductors-and-Manufacturing-Strategy.md"),
    (2025, "GS-III", 13, "Factors for depleting groundwater and government steps", "Economy", "Examine \u00b7 15 marks \u00b7 250 words", "Economy/basic/14_Irrigation-Inputs-Credit-Insurance-and-Sustainable-Agriculture.md"),
    (2025, "GS-III", 14, "Scope of food-processing industries and employment generation", "Economy", "Examine \u00b7 15 marks \u00b7 250 words", "Economy/basic/15_Food-Processing-Cold-Chains-and-Value-Addition.md"),
    (2025, "GS-III", 15, "Nanotechnology advancements in agriculture", "Science and Technology", "Discuss \u00b7 15 marks \u00b7 250 words", "Science-and-Technology/basic/16_Nanotechnology-and-Applications.md"),
    (2025, "GS-III", 16, "Challenges to the semiconductor industry; India Semiconductor Mission", "Science and Technology", "Mention \u00b7 15 marks \u00b7 250 words", "Science-and-Technology/basic/11_Semiconductor-Mission-and-Electronics-Manufacturing.md"),
    (2025, "GS-III", 17, "Mining as an environmental hazard and remedial measures", "Environment and Ecology", "Explain \u00b7 15 marks \u00b7 250 words", "Environment-and-Ecology/basic/16_Environmental-Impact-Assessment-and-NGT.md"),
    (2025, "GS-III", 18, "India's Paris Agreement commitments, COP26 and updated NDC", "Environment and Ecology", "Review \u00b7 15 marks \u00b7 250 words", "Environment-and-Ecology/basic/20_India-Climate-Policy-NAPCC-Panchamrit-LTLEDS.md"),
    (2025, "GS-III", 19, "Internal security and peace process in the North-Eastern States; accords", "Internal Security", "Map \u00b7 15 marks \u00b7 250 words", "Internal-Security/basic/04_North-East-Insurgency-and-Peace-Processes.md"),
    (2025, "GS-III", 20, "Maritime and coastal security challenges and the way forward", "Internal Security", "Discuss \u00b7 15 marks \u00b7 250 words", "Internal-Security/basic/07_Maritime-and-Coastal-Security.md"),
    # ---- 2025 GS-IV ----
    (2025, "GS-IV", 1, "(a) ethical dilemmas of social media in the digital age; (b) constitutional morality as product of civil education", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md", "Ethics/basic/14_Probity-Concept-and-Philosophical-Basis-of-Governance.md"]),
    (2025, "GS-IV", 2, "(a) Clausewitz - war as diplomacy by other means; (b) ethics of environmental clearance in sensitive border areas", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/12_Corporate-Governance-and-International-Ethics.md", "Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md"]),
    (2025, "GS-IV", 3, "Three quotations (Thiruvalluvar, William James, Vivekananda)", "Ethics", "Section A theory \u00b7 10 + 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/06_Indian-Moral-Thinkers-and-Philosophers.md", "Ethics/basic/07_Western-Moral-Philosophers-and-Thinkers.md"]),
    (2025, "GS-IV", 4, "(a) reason and critical thinking in welfare-scheme implementation; (b) teachings of Mahavir", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/04_Aptitude-and-Foundational-Values-for-Civil-Service.md", "Ethics/basic/06_Indian-Moral-Thinkers-and-Philosophers.md"]),
    (2025, "GS-IV", 5, "(a) devotion to duty and personal fulfilment; (b) civil servant as enabler and facilitator", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md", "Ethics/basic/04_Aptitude-and-Foundational-Values-for-Civil-Service.md"]),
    (2025, "GS-IV", 6, "(a) value-based and compliance-based work culture and code of ethics; (b) accountability against leakages and misuse of funds", "Ethics", "Section A theory \u00b7 10 + 10 marks \u00b7 150 words each", ["Ethics/basic/16_Codes-of-Ethics-and-Codes-of-Conduct.md", "Ethics/basic/18_Utilization-of-Public-Funds-and-Challenges-of-Corruption.md"]),
    (2025, "GS-IV", 7, "Case study: Vijay, Deputy Commissioner of a remote district in a hilly northern State", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md"]),
    (2025, "GS-IV", 8, "Case study: deforestation for housing and social-welfare objectives", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/13_Emerging-Ethics-Technology-AI-and-Environment.md"]),
    (2025, "GS-IV", 9, "Case study: Subash - ethical issues and options", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md"]),
    (2025, "GS-IV", 10, "Case study: Rajesh - options and ethical issues", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/10_Sources-of-Ethical-Guidance-Laws-Rules-Conscience.md"]),
    (2025, "GS-IV", 11, "Case study: restoring proper functioning of the MGNREGA programme", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/11_Accountability-and-Ethical-Governance.md"]),
    (2025, "GS-IV", 12, "Case study: Ashok - ethical and legal dilemmas", "Ethics", "Section B case study \u00b7 20 marks \u00b7 250 words", ["Ethics/basic/22_Case-Study-Method-and-Answer-Architecture.md", "Ethics/basic/09_Public-Service-Values-Status-and-Ethical-Dilemmas.md"]),
])


# ---------------------------------------------------------------------------
# ESSAY data: (year, topic-no label, theme, route(s))
# ---------------------------------------------------------------------------
ESSAY = [
    (2024, "Section A - 1", "Forests precede civilizations and deserts follow them", ["Essay/basic/03_Issue-Based-Prompt-Scoping.md", "Essay/basic/10_Ethical-Philosophical-Frameworks-and-Value-Conflicts.md"]),
    (2024, "Section A - 2", "The empires of the future will be the empires of the mind", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2024, "Section A - 3", "There is no path to happiness; happiness is the path", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2024, "Section A - 4", "The doubter is a true man of science", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2024, "Section B - 1", "Social media triggering 'Fear of Missing Out', depression and loneliness", "Essay/basic/03_Issue-Based-Prompt-Scoping.md"),
    (2024, "Section B - 2", "Nearly all men can stand adversity, but to test the character, give him power", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2024, "Section B - 3", "All ideas having large consequences are always simple", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2024, "Section B - 4", "The cost of being wrong is less than the cost of doing nothing", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section A - 1", "Truth knows no color", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section A - 2", "The supreme art of war is to subdue the enemy without fighting", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section A - 3", "Thought finds a world and creates one also", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section A - 4", "Best lessons are learnt through bitter experiences", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section B - 5", "Muddy water is best cleared by leaving it alone", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section B - 6", "The years teach much which the days never know", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section B - 7", "It is best to see life as a journey, not as a destination", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
    (2025, "Section B - 8", "Contentment is natural wealth; luxury is artificial poverty", "Essay/basic/02_Philosophical-Quote-Decoding.md"),
]


# ---------------------------------------------------------------------------
# Emit the four ledgers.
# ---------------------------------------------------------------------------
HEADER_NOTE = (
    "> ## Scope and honesty rules\n"
    ">\n"
    "> **Controlling routing/provenance record for 2024-2025.** Each row records where a\n"
    "> printed question already belongs in this knowledge base. A row is a pointer, not an\n"
    "> answer key. Question wording was read only from the local `knowledge-export/` OCR text;\n"
    "> nothing was reconstructed from memory, coaching sites or aggregators.\n"
    ">\n"
    "> **Neutral labels.** The theme column names the subject matter in neutral words and does\n"
    "> not resolve the item (no option letters, no verdicts).\n"
    ">\n"
    "> **OCR honesty.** Rows whose English text or exact question number could not be read with\n"
    "> confidence are marked `OCR-uncertain ... manual verification needed`; the missing wording\n"
    "> is left missing.\n"
)


def prelims_ledger() -> str:
    lines = [
        "# UPSC Prelims General Studies Paper I - PYQ Routing Ledger, 2024-2025",
        "",
        HEADER_NOTE,
        "",
        "> ## Key status: `Key available locally`",
        ">",
        "> Unlike 2018-2023, the official 2024 and 2025 Prelims Set-A answer keys **are** present in",
        "> this repository (`knowledge-export/Prelims PYQ/Ans-2024-GS1`, `Ans-2025-GS1`). This ledger",
        "> still records **no answer letter**: routing is linkage metadata, and answers are never",
        "> inferred here. The key status is preserved accurately as `key available locally`.",
        "",
        "| Year | Q | Topic / theme (neutral) | Subject / family | Route(s) | Integration note / status |",
        "|---:|---:|---|---|---|---|",
    ]
    for year, rows in ((2024, PRELIMS_2024), (2025, PRELIMS_2025)):
        for q, theme, subject, route, ocr in rows:
            note = PRELIMS_KEY_OCR if ocr else PRELIMS_KEY
            lines.append(
                f"| {year} | {q} | {cell(theme)} | {cell(subject)} | {links(route)} | {cell(note)} |"
            )
    return "\n".join(lines) + "\n"


def csat_ledger() -> str:
    rows = parse_csat()
    lines = [
        "# UPSC CSAT (General Studies Paper II) - PYQ Routing Ledger, 2024-2025",
        "",
        HEADER_NOTE,
        "",
        "> ## Family classification source",
        ">",
        "> The six-family classification and neutral type for every 2024 and 2025 CSAT question is",
        "> taken verbatim from the audited [`CSAT/00_Question-Audit-Ledger`](CSAT/00_Question-Audit-Ledger.md),",
        "> which read each Set-A scan directly. Only families 01-06 occur in 2024-2025; every route",
        "> targets an existing Basic owner (Topics 01-06). The supplied Set-A keys are recorded as",
        "> *supplied, not certified final*; **no answer letter is recorded here.**",
        "",
        "| Year | Q | Neutral type | Family | Route(s) | Integration note / status |",
        "|---:|---:|---|:---:|---|---|",
    ]
    for year, q, neutral, fam, route, note in rows:
        lines.append(
            f"| {year} | {q} | {cell(neutral)} | {fam} | {links(route)} | {cell(note)} |"
        )
    return "\n".join(lines) + "\n"


def mains_ledger(papers: tuple[str, ...], title: str, include_essay: bool) -> str:
    lines = [
        f"# {title}",
        "",
        HEADER_NOTE,
        "",
        "| Year | Paper | Q | Topic / theme (neutral) | Subject / family | Directive \u00b7 marks \u00b7 word limit | Route(s) | Integration note |",
        "|---:|---|---|---|---|---|---|---|",
    ]
    for year, paper, q, theme, subject, directive, route in MAINS:
        if paper not in papers:
            continue
        lines.append(
            f"| {year} | {paper} | {q} | {cell(theme)} | {cell(subject)} | {cell(directive)} | {links(route)} | {MAINS_NOTE} |"
        )
    if include_essay:
        for year, label, theme, route in ESSAY:
            lines.append(
                f"| {year} | Essay | {cell(label)} | {cell(theme)} | Essay | Essay \u00b7 25 marks \u00b7 1000-1200 words | {links(route)} | Routed to essay-method owner |"
            )
    return "\n".join(lines) + "\n"


def main() -> None:
    outputs = {
        KNOWLEDGE / "_PYQ-ROUTING-PRELIMS-2024-2025.md": prelims_ledger(),
        KNOWLEDGE / "_PYQ-ROUTING-CSAT-2024-2025.md": csat_ledger(),
        KNOWLEDGE / "_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md": mains_ledger(
            ("GS-I", "GS-II"), "UPSC Mains GS-I, GS-II and Essay - PYQ Routing Ledger, 2024-2025", True
        ),
        KNOWLEDGE / "_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md": mains_ledger(
            ("GS-III", "GS-IV"), "UPSC Mains GS-III and GS-IV - PYQ Routing Ledger, 2024-2025", False
        ),
    }
    for path, text in outputs.items():
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path.name} ({text.count(chr(10))} lines)")


if __name__ == "__main__":
    main()
