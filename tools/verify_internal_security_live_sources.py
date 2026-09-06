"""Create a dated authoritative live-source audit for Internal Security."""

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
    / f"internal-security-authoritative-live-source-audit-{DATE}.json"
)
URL_RE = re.compile(r"https?://\S+")
ALLOWED_DOMAINS = (
    "mha.gov.in",
    "pib.gov.in",
    "indiacode.nic.in",
    "legislative.gov.in",
    "nia.gov.in",
    "i4c.mha.gov.in",
    "cert-in.org.in",
    "nciipc.gov.in",
    "meity.gov.in",
    "fiuindia.gov.in",
    "enforcementdirectorate.gov.in",
    "rbi.org.in",
    "sebi.gov.in",
    "narcoticsindia.nic.in",
    "bsf.gov.in",
    "itbpolice.nic.in",
    "assamrifles.gov.in",
    "indiancoastguard.gov.in",
    "indiannavy.nic.in",
    "ndma.gov.in",
    "fatf-gafi.org",
    "un.org",
    "unodc.org",
    "interpol.int",
)
FALLBACKS = {
    1: (
        "https://www.mha.gov.in/en/divisionofmha/internal-security-i-division",
        "https://www.mha.gov.in/en/divisionofmha/centre-state-division",
        "https://legislative.gov.in/constitution-of-india/",
    ),
    2: (
        "https://www.mha.gov.in/en/divisionofmha/counter-terrorism-and-counter-radicalization-division",
        "https://www.nia.gov.in/about-us",
        "https://www.un.org/securitycouncil/ctc/",
    ),
    3: (
        "https://www.mha.gov.in/en/divisionofmha/left-wing-extremism-division",
        "https://www.mha.gov.in/",
        "https://www.pib.gov.in/",
    ),
    4: (
        "https://www.mha.gov.in/en/divisionofmha/north-east-division",
        "https://www.mha.gov.in/",
        "https://www.pib.gov.in/",
    ),
    5: (
        "https://www.mha.gov.in/en/divisionofmha/jammu-kashmir-and-ladakh-affairs",
        "https://www.mha.gov.in/",
        "https://www.indiacode.nic.in/",
    ),
    6: (
        "https://www.mha.gov.in/en/divisionofmha/border-management-i-division",
        "https://www.mha.gov.in/en/divisionofmha/border-management-ii-division",
        "https://www.bsf.gov.in/",
        "https://www.itbpolice.nic.in/",
    ),
    7: (
        "https://indiancoastguard.gov.in/",
        "https://www.indiannavy.nic.in/",
        "https://www.mha.gov.in/en/divisionofmha/border-management-ii-division",
    ),
    8: (
        "https://www.cert-in.org.in/",
        "https://www.nciipc.gov.in/",
        "https://i4c.mha.gov.in/",
        "https://www.meity.gov.in/",
    ),
    9: (
        "https://www.meity.gov.in/",
        "https://i4c.mha.gov.in/",
        "https://www.cert-in.org.in/",
    ),
    10: (
        "https://www.fatf-gafi.org/en/publications/Mutualevaluations/India-MER-2024.html",
        "https://fiuindia.gov.in/",
        "https://enforcementdirectorate.gov.in/what-we-do",
        "https://www.rbi.org.in/",
    ),
    11: (
        "https://www.mha.gov.in/en/commoncontent/narco-coordination-centre-ncord",
        "https://narcoticsindia.nic.in/",
        "https://www.unodc.org/unodc/en/organized-crime/intro/UNTOC.html",
        "https://www.interpol.int/Crimes/Organized-crime",
    ),
    12: (
        "https://www.mha.gov.in/en/commoncontent/intelligence-bureau",
        "https://www.nia.gov.in/about-us",
        "https://www.bsf.gov.in/",
        "https://www.itbpolice.nic.in/",
        "https://www.assamrifles.gov.in/",
    ),
}
CLAIM_CLASSES = {
    1: "constitutional allocation, MHA governance and federal coordination",
    2: "counter-terror law, designation, investigation and multilateral control",
    3: "LWE policy, affected-area status, violence trends and integrated response",
    4: "insurgency, ceasefire/accord status, implementation and peace outcomes",
    5: "Jammu and Kashmir legal status, governance and cross-border attribution",
    6: "border typology, guarding mandates, infrastructure and area development",
    7: "maritime zones, Navy/Coast Guard/coastal-police mandates and coordination",
    8: "cyber incident reporting, CII protection, cybercrime and data governance",
    9: "platform rules, encrypted communications, disinformation and safeguards",
    10: "PMLA process, FIU/ED/RBI roles, FATF status and terror financing",
    11: "organised crime, narcotics, trafficking, seizures and terror linkages",
    12: "force/agency mandates, intelligence coordination, special powers and rights",
}


def authoritative(url: str) -> bool:
    host = (urlparse(url).hostname or "").casefold()
    return any(host == domain or host.endswith("." + domain) for domain in ALLOWED_DOMAINS)


def clean_url(value: str) -> str:
    return value.rstrip("`.,;:)]}")


def configured_urls(number: int) -> list[str]:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    module = importlib.import_module(f"internal_security_{number:02d}_data")
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
            "User-Agent": "Mozilla/5.0 UPSC-internal-security-source-audit/1.0",
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
    topics = {number: configured_urls(number) for number in range(1, 13)}
    work = [(number, url) for number, urls in topics.items() for url in urls]
    results = {number: [] for number in topics}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(probe, url): number for number, url in work}
        for future in concurrent.futures.as_completed(futures):
            results[futures[future]].append(future.result())

    rows = []
    failures = []
    for number in range(1, 13):
        attempts = sorted(results[number], key=lambda item: str(item["url"]))
        retrieved = sum(bool(item.get("substantive")) for item in attempts)
        passed = len(attempts) >= 3 and retrieved >= 1
        if not passed:
            failures.append(
                f"internal-security-{number:02d}: {retrieved} substantive "
                f"retrievals from {len(attempts)} attempts"
            )
        rows.append(
            {
                "topic_key": f"internal-security-{number:02d}",
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
                "safety_control": (
                    "Policy, law, institutions and public outcomes only; no "
                    "classified detail, tactical vulnerability or attack-enabling "
                    "procedure is inferred or reproduced."
                ),
            }
        )
    payload = {
        "schema_version": 1,
        "subject": "Internal Security",
        "access_date": DATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topic_count": 12,
        "result": "failed" if failures else "passed",
        "policy": {
            "authoritative_domains_only": True,
            "minimum_attempts_per_topic": 3,
            "minimum_substantive_retrievals_per_topic": 1,
            "public_policy_safe_non_actionable": True,
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
