"""Small authoring helpers for Science and Technology learner-v2 topics."""

from __future__ import annotations


def panel(
    title: str,
    structural_type: str,
    lines: list[str],
    source_references: list[str],
) -> tuple[str, str, str, list[str]]:
    """Return one manually authored ASCII/graphical panel definition."""

    return title, structural_type, "\n".join(lines), source_references


SPACE_LIVE_ATTEMPTS = [
    (
        "https://www.isro.gov.in/Launchers.html — attempted 2026-09-03; "
        "direct retrieval returned only the page title, so no vehicle status, "
        "stage, propellant or payload-capacity claim was imported."
    ),
    (
        "https://www.isro.gov.in/Navigation.html — attempted 2026-09-03; "
        "direct retrieval returned only the page title, so no constellation, "
        "signal, coverage, accuracy or operational-status claim was imported."
    ),
    (
        "https://www.isro.gov.in/Gaganyaan.html — attempted 2026-09-03; "
        "direct retrieval returned only the page title, so no crew, schedule, "
        "test or mission-status claim was imported."
    ),
]


NUCLEAR_LIVE_ATTEMPTS = [
    (
        "https://dae.gov.in/prototype-fast-breeder-reactor-at-kalpakkam-"
        "tamil-nadu-attains-first-criticality/ — attempted 2026-09-03; "
        "substantive DAE text confirmed PFBR first criticality on 6 April "
        "2026, its 500 MWe rating, IGCAR design, BHAVINI execution, MOX fuel, "
        "U-238 blanket and the explicit boundary that criticality is the start "
        "of a controlled chain reaction. It was not rewritten as grid "
        "synchronisation, commercial operation or completion of Stage 2."
    ),
]


FUSION_LIVE_ATTEMPTS = [
    (
        "https://www.iter.org/fusion-energy/what-will-iter-do — attempted "
        "2026-09-03; substantive ITER text confirmed the experimental Q=10 "
        "design objective of 500 MW fusion power from 50 MW injected heating, "
        "that ITER will not convert that heat to electricity, and that it will "
        "test integrated technologies and tritium-breeding concepts. These "
        "claims were not converted into plant-wide or commercial breakeven."
    ),
]


DEFENCE_RD_LIVE_ATTEMPTS = [
    (
        "https://drdo.gov.in/drdo/en/organisation/technology-cluster/"
        "missiles-and-strategic-systems — fetched 2026-09-03; substantive "
        "DRDO text confirmed the MSS cluster's design-and-development role, "
        "five named laboratories and technology areas including propulsion, "
        "guidance, homing, launch and command-and-control. It supplied no "
        "missile range, payload, warhead, deployment or test-status claim."
    ),
]


DEFENCE_PRODUCTION_LIVE_ATTEMPTS = [
    (
        "https://www.ddpmod.gov.in/node/355 — attempted 2026-09-03; the page "
        "redirected to the Hindi DDP node and exposed the official Defence "
        "Acquisition Procedure 2020 title and language alternate, but the "
        "retrieved body was stylesheet-heavy. No category threshold, contract "
        "value, positive-list item or implementation timeline was imported."
    ),
]


DIGITAL_LIVE_ATTEMPTS = [
    (
        "https://uidai.gov.in/en/about-uidai/unique-identification-authority-"
        "of-india.html — attempted 2026-09-03 and returned 404. Official-domain "
        "search surfaced the current /en/about-uidai page and Aadhaar Act "
        "documents; no coverage or authentication total was imported."
    ),
    (
        "https://www.npci.org.in/product/upi/product-statistics — official-domain "
        "search attempted 2026-09-03; the authoritative product-statistics page "
        "was located, but no monthly volume or value was imported without a "
        "direct, month-specific table retrieval."
    ),
]


AI_LIVE_ATTEMPTS = [
    (
        "https://indiaai.gov.in/article/report-on-ai-governance-guidelines-"
        "development — fetched 2026-09-03; substantive IndiaAI text confirmed "
        "the Advisory Group, governance subcommittee, whole-of-government "
        "recommendations and consultation closure on 27 February 2025. The "
        "report remains a consultation/governance instrument, not an AI Act."
    ),
]


QUANTUM_LIVE_ATTEMPTS = [
    (
        "https://dst.gov.in/national-quantum-mission-nqm — attempted "
        "2026-09-03; direct retrieval returned only the official page title. "
        "Official-domain search surfaced the mission page and Cabinet page, "
        "but no new qubit achievement, communication distance, operational "
        "system or revised timeline was inferred from search snippets."
    ),
]
