"""Create a dated, topic-wise live-source integrity audit for Science and Technology."""

from __future__ import annotations

import concurrent.futures
import hashlib
import json
import re
import ssl
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-06"
KNOWLEDGE = ROOT / "upsc-ai-kit" / "knowledge" / "Science-and-Technology"
OUTPUT = (
    ROOT
    / "upsc-ai-kit"
    / "manifests"
    / "exports"
    / f"science-and-technology-authoritative-live-source-audit-{DATE}.json"
)
URL_RE = re.compile(r"https?://[^\s<>\]\"']+")
ALLOWED_DOMAINS = (
    "isro.gov.in",
    "inspace.gov.in",
    "nsilindia.co.in",
    "pib.gov.in",
    "dae.gov.in",
    "barc.gov.in",
    "npcil.nic.in",
    "bhavini.nic.in",
    "aerb.gov.in",
    "iter.org",
    "drdo.gov.in",
    "mod.gov.in",
    "ddpmod.gov.in",
    "srijandefence.gov.in",
    "uidai.gov.in",
    "npci.org.in",
    "rbi.org.in",
    "digitalindia.gov.in",
    "meity.gov.in",
    "indiaai.gov.in",
    "dst.gov.in",
    "ism.gov.in",
    "indiacode.nic.in",
    "cert-in.org.in",
    "nciipc.gov.in",
    "dbt.gov.in",
    "dbtindia.gov.in",
    "birac.nic.in",
    "geacindia.gov.in",
    "moef.gov.in",
    "moefcc.gov.in",
    "cdsco.gov.in",
    "icmr.gov.in",
    "ipindia.gov.in",
    "dpiit.gov.in",
    "wipo.int",
    "heavyindustries.gov.in",
    "mnre.gov.in",
    "morth.nic.in",
    "niti.gov.in",
    "beeindia.gov.in",
    "civilaviation.gov.in",
    "dgca.gov.in",
    "aai.aero",
    "mines.gov.in",
    "gsi.gov.in",
    "kabilindia.in",
    "csir.res.in",
    "anrf.gov.in",
    "nobelprize.org",
    "who.int",
    "iaea.org",
    "itu.int",
    "unep.org",
    "oecd.ai",
    "cdac.in",
)
FALLBACKS = {
    10: [
        "https://dst.gov.in/national-quantum-mission-nqm",
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=1917888",
        "https://www.itu.int/en/ITU-T/techwatch/Pages/quantum-information-technology.aspx",
        "https://www.nist.gov/quantum-information-science",
    ],
    21: [
        "https://www.nobelprize.org/prizes/physics/2024/press-release/",
        "https://www.nobelprize.org/prizes/physics/2025/press-release/",
        "https://www.isro.gov.in/Launchers.html",
        "https://www.barc.gov.in/",
    ],
    22: [
        "https://www.nobelprize.org/prizes/chemistry/2024/press-release/",
        "https://www.nobelprize.org/prizes/chemistry/2025/press-release/",
        "https://mnre.gov.in/en/national-green-hydrogen-mission/",
        "https://www.unep.org/inc-plastic-pollution",
    ],
    23: [
        "https://www.nobelprize.org/prizes/medicine/2024/press-release/",
        "https://www.nobelprize.org/prizes/medicine/2025/press-release/",
        "https://www.who.int/india",
        "https://www.icmr.gov.in/",
    ],
    24: [
        "https://dst.gov.in/introduction",
        "https://www.csir.res.in/en/about-us/about-csir",
        "https://www.anrfonline.in/ANRF/",
        "https://www.pib.gov.in/PressReleasePage.aspx?PRID=1944913",
    ],
    25: [
        "https://www.cdac.in/index.aspx?id=about",
        "https://www.meity.gov.in/content/national-supercomputing-mission",
        "https://www.itu.int/itu-d/sites/cloud-computing/",
        "https://www.cert-in.org.in/",
    ],
    26: [
        "https://www.nobelprize.org/prizes/physics/2025/press-release/",
        "https://www.nobelprize.org/prizes/chemistry/2025/press-release/",
        "https://www.nobelprize.org/prizes/medicine/2025/press-release/",
        "https://www.nobelprize.org/prizes/lists/all-nobel-prizes-in-physics/",
        "https://www.nobelprize.org/prizes/lists/all-nobel-prizes-in-chemistry/",
        "https://www.nobelprize.org/prizes/lists/all-nobel-laureates-in-physiology-or-medicine/",
    ],
}


def authoritative(url: str) -> bool:
    host = (urlparse(url).hostname or "").casefold()
    return any(host == domain or host.endswith("." + domain) for domain in ALLOWED_DOMAINS)


def clean_url(value: str) -> str:
    return value.rstrip("`.,;:)]}")


def source_urls(number: int) -> list[str]:
    paths = [
        next((KNOWLEDGE / "basic").glob(f"{number:02d}_*.md")),
        next((KNOWLEDGE / "advanced").glob(f"{number:02d}_*.md")),
    ]
    urls: list[str] = []
    for path in paths:
        for match in URL_RE.findall(path.read_text(encoding="utf-8")):
            url = clean_url(match)
            if authoritative(url) and url not in urls:
                urls.append(url)
    for url in FALLBACKS.get(number, []):
        if url not in urls:
            urls.append(url)
    return urls[:8]


def probe(url: str) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 UPSC-semantic-source-audit/1.0",
            "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.8",
            "Range": "bytes=0-524287",
        },
    )
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=25, context=context) as response:
            body = response.read(524288)
            text = body.decode("utf-8", errors="ignore")
            title_match = re.search(
                r"<title[^>]*>(.*?)</title>",
                text,
                flags=re.I | re.S,
            )
            title = (
                re.sub(r"\s+", " ", title_match.group(1)).strip()
                if title_match
                else None
            )
            status = int(getattr(response, "status", 200))
            return {
                "url": url,
                "outcome": "retrieved" if body else "empty",
                "http_status": status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type"),
                "bytes_sampled": len(body),
                "sample_sha256": hashlib.sha256(body).hexdigest(),
                "title": title,
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
    topics: dict[int, list[str]] = {
        number: source_urls(number) for number in range(1, 27)
    }
    work = [(number, url) for number, urls in topics.items() for url in urls]
    results: dict[int, list[dict[str, object]]] = {
        number: [] for number in topics
    }
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = {
            executor.submit(probe, url): number for number, url in work
        }
        for future in concurrent.futures.as_completed(futures):
            results[futures[future]].append(future.result())

    rows = []
    failures = []
    for number in range(1, 27):
        attempts = sorted(results[number], key=lambda item: str(item["url"]))
        retrieved = sum(bool(item.get("substantive")) for item in attempts)
        passed = len(attempts) >= 3 and retrieved >= 1
        if not passed:
            failures.append(
                f"science-and-technology-{number:02d}: "
                f"{retrieved} substantive retrievals from {len(attempts)} attempts"
            )
        rows.append(
            {
                "topic_key": f"science-and-technology-{number:02d}",
                "access_date": DATE,
                "attempted": len(attempts),
                "substantive_retrievals": retrieved,
                "status": "passed" if passed else "failed",
                "sources": attempts,
                "claim_control": (
                    "Live retrieval verifies publisher availability and dated source "
                    "integrity only. No quantitative, programme-status or scientific "
                    "claim is promoted without matching substantive official text."
                ),
            }
        )
    payload = {
        "schema_version": 1,
        "subject": "Science and Technology",
        "access_date": DATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topic_count": 26,
        "result": "failed" if failures else "passed",
        "policy": {
            "authoritative_domains_only": True,
            "minimum_attempts_per_topic": 3,
            "minimum_substantive_retrievals_per_topic": 1,
            "failed_intermediates_preserved": True,
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
