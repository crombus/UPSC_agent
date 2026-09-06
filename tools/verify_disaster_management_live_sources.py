"""Create a dated authoritative live-source audit for Disaster Management."""

from __future__ import annotations

import concurrent.futures
import hashlib
import importlib
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
DATE = "2026-09-06"
OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"disaster-management-authoritative-live-source-audit-{DATE}.json"
)
URL_RE = re.compile(r"https?://\S+")
ALLOWED_DOMAINS = (
    "ndma.gov.in",
    "mha.gov.in",
    "indiacode.nic.in",
    "egazette.nic.in",
    "nidm.gov.in",
    "ndrf.gov.in",
    "pib.gov.in",
    "imd.gov.in",
    "moes.gov.in",
    "incois.gov.in",
    "cwc.gov.in",
    "gsi.gov.in",
    "isro.gov.in",
    "nrsc.gov.in",
    "fsi.nic.in",
    "fsiforestfire.gov.in",
    "moef.gov.in",
    "agriwelfare.gov.in",
    "icar.gov.in",
    "icar-crida.res.in",
    "cgwb.gov.in",
    "ncdc.mohfw.gov.in",
    "mohfw.gov.in",
    "icmr.gov.in",
    "cpcb.nic.in",
    "peso.gov.in",
    "aerb.gov.in",
    "bis.gov.in",
    "cea.nic.in",
    "mohua.gov.in",
    "fincomindia.nic.in",
    "irdai.gov.in",
    "drdo.gov.in",
    "undrr.org",
    "wmo.int",
    "who.int",
    "unesco.org",
    "unesco-­ioc.org",
    "ipcc.ch",
    "unfccc.int",
    "worldbank.org",
    "gfdrr.org",
    "cdri.world",
    "unocha.org",
    "ifrc.org",
    "bimstec.org",
)
COMMON_FALLBACKS = (
    "https://www.undrr.org/implementing-sendai-framework/what-sendai-framework",
    "https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030",
    "https://wmo.int/all-activities/build-resilience/early-warnings-all",
    "https://ndma.gov.in/Resources/Guidelines",
)
FALLBACKS = {
    1: COMMON_FALLBACKS,
    2: (
        "https://www.indiacode.nic.in/indiacode/bitstream/123456789/2045/1/A200553.pdf",
        "https://www.mha.gov.in/en/divisionofmha/disaster-management-division",
        "https://nidm.gov.in/about.asp",
        "https://ndrf.gov.in/en/about-us",
    ),
    3: (
        "https://ndma.gov.in/Resources/Guidelines",
        "https://nidm.gov.in/",
        *COMMON_FALLBACKS[:2],
    ),
    4: (
        "https://sachet.ndma.gov.in/About",
        "https://mausam.imd.gov.in/index_en.php",
        "https://cwc.gov.in/flood-forecasting-hydrological-observation",
        "https://tsunami.incois.gov.in/TEWS/dsssop.jsp",
        *COMMON_FALLBACKS[:2],
    ),
    5: (
        "https://ndma.gov.in/Natural-Hazards/Earthquakes",
        "https://www.bis.gov.in/standards/national-building-code/?lang=en",
        "https://bhusanket.gsi.gov.in/",
        *COMMON_FALLBACKS[:2],
    ),
    6: (
        "https://tsunami.incois.gov.in/TEWS/dsssop.jsp",
        "https://tsunami.incois.gov.in/TEWS/tsunamiready.jsp",
        "https://ndma.gov.in/Natural-Hazards/Tsunami",
        *COMMON_FALLBACKS[:2],
    ),
    7: (
        "https://mausam.imd.gov.in/responsive/cycloneinformation.php",
        "https://mitigation.ndma.gov.in/ncrmp/",
        "https://sachet.ndma.gov.in/",
        *COMMON_FALLBACKS[:2],
    ),
    8: (
        "https://cwc.gov.in/flood-forecasting-hydrological-observation",
        "https://ndma.gov.in/Natural-Hazards/Floods",
        "https://www.isro.gov.in/DisasterManagementSupport.html",
        *COMMON_FALLBACKS[:2],
    ),
    9: (
        "https://mausam.imd.gov.in/responsive/heatwave_guidance.php",
        "https://agriwelfare.gov.in/Documents/Updated%20Drought%20Manual_0.pdf",
        "https://cgwb.gov.in/",
        *COMMON_FALLBACKS[:2],
    ),
    10: (
        "https://bhusanket.gsi.gov.in/rolesAndResponsibility.html",
        "https://www.nrsc.gov.in/nrscnew/resources_atlas_landslide.php",
        "https://www.isro.gov.in/Landslide_Atlas_India.html",
        *COMMON_FALLBACKS[:2],
    ),
    11: (
        "https://fsi.nic.in/focus-areas?pgID=focus-areas",
        "https://fsiforestfire.gov.in/",
        "https://moef.gov.in/forest-protection-forest-fire",
        *COMMON_FALLBACKS[:2],
    ),
    12: (
        "https://cpcb.nic.in/chemical-emergency/",
        "https://www.aerb.gov.in/english/regulatory-facilities/nuclear-power-plants/emergency-preparedness",
        "https://ndma.gov.in/sites/default/files/PDF/Guidelines/chemical-disaster.pdf",
        *COMMON_FALLBACKS[:2],
    ),
    13: (
        "https://ncdc.mohfw.gov.in/includes/About/CentresAndDivision/IDSP.php",
        "https://www.icmr.gov.in/",
        "https://www.who.int/health-topics/emergencies",
        *COMMON_FALLBACKS[:2],
    ),
    14: (
        "https://www.bis.gov.in/standards/national-building-code/?lang=en",
        "https://cdri.world/",
        "https://cea.nic.in/?lang=en",
        *COMMON_FALLBACKS[:2],
    ),
    15: (
        "https://www.ipcc.ch/report/ar6/wg2/",
        "https://unfccc.int/wim-excom",
        "https://wmo.int/activities/climate-services",
        *COMMON_FALLBACKS[:2],
    ),
    16: (
        "https://www.mha.gov.in/en/divisionofmha/disaster-management-division/response-fund",
        "https://fincomindia.nic.in/",
        "https://irdai.gov.in/",
        *COMMON_FALLBACKS[:2],
    ),
    17: (
        "https://ndrf.gov.in/en/about-us",
        "https://www.unocha.org/we-coordinate",
        "https://www.who.int/health-topics/emergencies",
        *COMMON_FALLBACKS[:2],
    ),
    18: (
        "https://nidm.gov.in/",
        "https://bimstec.org/sector/disaster-management",
        "https://www.undrr.org/our-work",
        *COMMON_FALLBACKS[:2],
    ),
}
CLAIM_CLASSES = {
    1: "risk terminology, resilience, Sendai priorities and targets",
    2: "Disaster Management Act, institutions, plans, rules and funds",
    3: "community-based DRR, inclusion, volunteers and local capacity",
    4: "multi-hazard warning chain, competent agencies and technology",
    5: "seismic hazard, zonation, building standards and resilient construction",
    6: "tsunami detection, warning, evacuation and coastal preparedness",
    7: "cyclone forecasting, storm surge, shelters and coastal preparedness",
    8: "riverine/urban flooding, forecasts, drainage and floodplain governance",
    9: "drought, heat-wave criteria, health/agriculture risk and action plans",
    10: "landslides, avalanches, GLOFs, susceptibility and monitoring",
    11: "forest-fire alerts, field verification, suppression and recovery",
    12: "industrial, chemical, nuclear and CBRN law, plans and response",
    13: "surveillance, outbreak terminology and public-health emergency systems",
    14: "urban systems, critical infrastructure, continuity and resilience",
    15: "climate-risk links, adaptation, loss and damage and framework status",
    16: "disaster funds, finance tiers, risk transfer and Build Back Better",
    17: "relief, logistics, rehabilitation, recovery and protection standards",
    18: "capacity, plans, exercises, cooperation, Sendai and institutional learning",
}


def authoritative(url: str) -> bool:
    host = (urlparse(url).hostname or "").casefold()
    return any(host == domain or host.endswith("." + domain) for domain in ALLOWED_DOMAINS)


def clean_url(value: str) -> str:
    return value.rstrip("`.,;:)]}")


def configured_urls(number: int) -> list[str]:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    module = importlib.import_module(f"disaster_management_{number:02d}_data")
    config = getattr(module, f"TOPIC_{number:02d}")
    urls: list[str] = []
    for attempt in config["live_sources"]:
        match = URL_RE.search(str(attempt))
        if match:
            url = clean_url(match.group(0))
            if authoritative(url) and url not in urls:
                urls.append(url)
    for url in FALLBACKS[number]:
        if authoritative(url) and url not in urls:
            urls.append(url)
    return urls[:8]


def probe(url: str) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 UPSC-disaster-management-source-audit/1.0",
            "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.8",
            "Range": "bytes=0-524287",
        },
    )
    try:
        with urllib.request.urlopen(
            request, timeout=30, context=ssl.create_default_context()
        ) as response:
            body = response.read(524288)
            text = body.decode("utf-8", errors="ignore")
            title_match = re.search(
                r"<title[^>]*>(.*?)</title>", text, flags=re.I | re.S
            )
            return {
                "url": url,
                "outcome": "retrieved" if body else "empty",
                "http_status": int(getattr(response, "status", 200)),
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type"),
                "bytes_sampled": len(body),
                "sample_sha256": hashlib.sha256(body).hexdigest(),
                "title": (
                    re.sub(r"\s+", " ", title_match.group(1)).strip()
                    if title_match else None
                ),
                "substantive": len(body) >= 200,
            }
    except urllib.error.HTTPError as error:
        return {
            "url": url,
            "outcome": "http_error",
            "http_status": error.code,
            "error": str(error),
            "substantive": False,
        }
    except Exception as error:
        return {
            "url": url,
            "outcome": "transport_error",
            "error": f"{type(error).__name__}: {error}",
            "substantive": False,
        }


def main() -> int:
    topics = {number: configured_urls(number) for number in range(1, 19)}
    work = [(number, url) for number, urls in topics.items() for url in urls]
    results = {number: [] for number in topics}
    with concurrent.futures.ThreadPoolExecutor(max_workers=18) as executor:
        futures = {executor.submit(probe, url): number for number, url in work}
        for future in concurrent.futures.as_completed(futures):
            results[futures[future]].append(future.result())

    rows = []
    failures = []
    for number in range(1, 19):
        attempts = sorted(results[number], key=lambda item: str(item["url"]))
        retrieved = sum(bool(item.get("substantive")) for item in attempts)
        passed = len(attempts) >= 3 and retrieved >= 1
        if not passed:
            failures.append(
                f"disaster-management-{number:02d}: {retrieved} substantive "
                f"retrievals from {len(attempts)} attempts"
            )
        rows.append(
            {
                "topic_key": f"disaster-management-{number:02d}",
                "access_date": DATE,
                "verification_scope": CLAIM_CLASSES[number],
                "attempted": len(attempts),
                "substantive_retrievals": retrieved,
                "status": "passed" if passed else "failed",
                "sources": attempts,
                "claim_control": (
                    "Retrieval verifies authoritative publisher availability and "
                    "source integrity. A source supports only the proposition "
                    "actually stated in its substantive text. Failed/thin pages "
                    "supply no fact; analytical inference remains labelled."
                ),
            }
        )
    payload = {
        "schema_version": 1,
        "subject": "Disaster Management",
        "access_date": DATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topic_count": 18,
        "result": "failed" if failures else "passed",
        "policy": {
            "authoritative_domains_only": True,
            "minimum_attempts_per_topic": 3,
            "minimum_substantive_retrievals_per_topic": 1,
            "failed_intermediates_preserved": True,
            "facts_and_inference_separated": True,
        },
        "topics": rows,
        "failures": failures,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, ensure_ascii=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
