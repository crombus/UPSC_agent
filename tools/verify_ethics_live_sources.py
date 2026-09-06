"""Create the dated authoritative live-source audit for all Ethics topics."""

from __future__ import annotations

import concurrent.futures
import hashlib
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
    / f"ethics-authoritative-live-source-audit-{DATE}.json"
)
ALLOWED_DOMAINS = (
    "dopt.gov.in",
    "darpg.gov.in",
    "cbc.gov.in",
    "igotkarmayogi.gov.in",
    "pib.gov.in",
    "static.pib.gov.in",
    "nidm.gov.in",
    "culture.gov.in",
    "indiaai.gov.in",
    "impact.indiaai.gov.in",
    "cag.gov.in",
    "cvc.gov.in",
    "cic.gov.in",
    "lokpal.gov.in",
    "cbi.gov.in",
    "pfms.nic.in",
    "doe.gov.in",
    "gem.gov.in",
    "bidplus.gem.gov.in",
    "pgportal.gov.in",
    "rti.dopt.gov.in",
    "indiacode.nic.in",
    "legislative.gov.in",
    "sci.gov.in",
    "api.sci.gov.in",
    "sansad.in",
    "rajyasabha.nic.in",
    "cms.rajyasabha.nic.in",
    "meity.gov.in",
    "unodc.org",
    "businessintegrity.unodc.org",
    "un.org",
    "unesco.org",
    "ohchr.org",
    "oecd.org",
    "unfccc.int",
    "plato.stanford.edu",
    "gandhiheritageportal.org",
    "drambedkarwritings.gov.in",
    "ethics.ncdirindia.org",
    "icmr.gov.in",
    "cpib.gov.sg",
    "sso.agc.gov.sg",
    "icac.org.hk",
    "transparency.org",
    "korruptiontorjunta.fi",
    "nacc.go.th",
)
COMMON = (
    "https://darpg.gov.in/sites/default/files/ethics4.pdf",
    "https://dopt.gov.in/acts/central-civil-services-conduct-rules-1964-updated-0",
    "https://www.indiacode.nic.in/handle/123456789/2065",
)
FALLBACKS = {
    1: COMMON,
    2: (
        "https://www.gandhiheritageportal.org/",
        "https://www.drambedkarwritings.gov.in/",
        COMMON[0],
    ),
    3: (
        "https://nidm.gov.in/PDF/Modules/SBCFacilitatorGuide_2026.pdf",
        COMMON[0],
    ),
    4: COMMON,
    5: (
        "https://cbc.gov.in/karmayogi-competency-model-kcm",
        COMMON[0],
    ),
    6: (
        "https://www.gandhiheritageportal.org/",
        "https://www.drambedkarwritings.gov.in/",
        COMMON[0],
    ),
    7: (
        "https://plato.stanford.edu/entries/aristotle-ethics/",
        "https://plato.stanford.edu/entries/kant-moral/",
        "https://plato.stanford.edu/entries/rawls/",
    ),
    8: (
        "https://plato.stanford.edu/entries/ethics-deontological/",
        "https://plato.stanford.edu/entries/consequentialism/",
        "https://plato.stanford.edu/entries/ethics-virtue/",
        "https://plato.stanford.edu/entries/feminism-ethics/",
    ),
    9: COMMON,
    10: (
        "https://www.indiacode.nic.in/handle/123456789/2065",
        COMMON[1],
        COMMON[0],
    ),
    11: (
        "https://cag.gov.in/en/audit-report/audit-report-list",
        "https://www.cvc.gov.in/",
        COMMON[0],
    ),
    12: (
        "https://www.unodc.org/unodc/en/corruption/uncac.html",
        "https://www.oecd.org/corporate/",
        "https://www.ohchr.org/en/business-and-human-rights",
    ),
    13: (
        "https://www.unesco.org/en/artificial-intelligence/recommendation-ethics",
        "https://unfccc.int/process-and-meetings/the-paris-agreement",
        "https://www.meity.gov.in/",
    ),
    14: (
        "https://www.cvc.gov.in/",
        "https://gem.gov.in/resources/pdf/Integrity-pact-guidelines.pdf",
        COMMON[0],
    ),
    15: (
        "https://www.indiacode.nic.in/handle/123456789/2065",
        "https://cic.gov.in/",
        "https://rti.dopt.gov.in/",
    ),
    16: (
        COMMON[1],
        "https://cms.rajyasabha.nic.in/UploadedFiles/CommitteeSection/CommitteeRules/1626363812501.54_CommitteOnEthics.pdf",
        COMMON[0],
    ),
    17: (
        "https://www.darpg.gov.in/relatedlinks/sevottam",
        "https://pgportal.gov.in/",
        COMMON[0],
    ),
    18: (
        "https://cag.gov.in/en/page-performance-audit",
        "https://pfms.nic.in/SitePages/about-Verticals-GIFMIS.aspx",
        "https://doe.gov.in/orders-circulars/31",
    ),
    19: (
        "https://www.indiacode.nic.in/handle/123456789/1558",
        "https://api.sci.gov.in/supremecourt/2018/40618/40618_2018_4_1501_67544_Judgement_13-Jan-2026.pdf",
        "https://api.sci.gov.in/supremecourt/2022/34619/34619_2022_1_301_56563_Judgement_18-Oct-2024.pdf",
    ),
    20: (
        "https://www.cvc.gov.in/",
        "https://lokpal.gov.in/",
        "https://cbi.gov.in/",
    ),
    21: (
        "https://www.cvc.gov.in/",
        "https://www.indiacode.nic.in/handle/123456789/2128",
        COMMON[1],
    ),
    22: (
        "https://cbc.gov.in/amrit-gyaan-kosh",
        "https://upsc.gov.in/examinations/previous-question-papers",
        COMMON[0],
    ),
    23: (
        "https://www.indiacode.nic.in/handle/123456789/18898",
        "https://ethics.ncdirindia.org/asset/pdf/ICMR_National_Ethical_Guidelines.pdf",
        "https://www.icac.org.hk/en/about/struct/index.html",
    ),
}
CLAIM_CLASSES = {
    1: "ethics, morality, propriety, public power and constitutional morality",
    2: "value formation, verified leaders, teachings and quotation integrity",
    3: "attitude structure, persuasion, manipulation, coercion and behaviour",
    4: "civil-service competencies, foundational values and conduct",
    5: "emotional intelligence models, limits and administrative application",
    6: "Indian ethical thought, primary attribution and bounded application",
    7: "Western moral thinkers, doctrines, objections and quotation integrity",
    8: "deontology, consequences, virtue, care, justice and plural testing",
    9: "public-service values, discretion, conflicts and ethical dilemmas",
    10: "constitutional, statutory, rule-based and conscience guidance",
    11: "answerability, audit, vigilance, grievance and social accountability",
    12: "corporate integrity, international ethics, human rights and UNCAC",
    13: "AI, privacy, technology, environment and climate-justice ethics",
    14: "probity, propriety, integrity controls and public-office-as-trust",
    15: "RTI provisions, exemptions, appeals, penalties and data protection",
    16: "codes of ethics/conduct, service rules and legislative ethics",
    17: "Citizens' Charters, Sevottam, CPGRAMS and accessible service delivery",
    18: "public-fund lifecycle, propriety, audit, procurement and corruption",
    19: "Prevention of Corruption Act provisions and current judicial status",
    20: "CVC, CBI, Lokpal, Lokayuktas and anti-corruption mandates",
    21: "honest-official safeguards, PIDPI, whistleblowing and vigilance",
    22: "case-study method, stakeholder/options testing and institutional reform",
    23: "named cases, comparative institutions, professional codes and legal status",
}


def authoritative(url: str) -> bool:
    host = (urlparse(url).hostname or "").casefold()
    return any(host == domain or host.endswith("." + domain) for domain in ALLOWED_DOMAINS)


def configured_urls(number: int) -> list[str]:
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    import generate_ethics_topic_v2 as generator

    urls = []
    for value in (*generator.TOPICS[number].data.CURRENT_SOURCE_URLS, *FALLBACKS[number]):
        url = str(value).strip().rstrip("`.,;:)]}")
        if authoritative(url) and url not in urls:
            urls.append(url)
    return urls[:10]


def probe(url: str) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 UPSC-ethics-source-audit/1.0",
            "Accept": "text/html,application/pdf;q=0.9,*/*;q=0.8",
            "Range": "bytes=0-524287",
        },
    )
    try:
        with urllib.request.urlopen(
            request, timeout=35, context=ssl.create_default_context()
        ) as response:
            body = response.read(524288)
            text = body.decode("utf-8", errors="ignore")
            title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
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
                    if title_match
                    else None
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
    topics = {number: configured_urls(number) for number in range(1, 24)}
    work = [(number, url) for number, urls in topics.items() for url in urls]
    results = {number: [] for number in topics}
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(probe, url): number for number, url in work}
        for future in concurrent.futures.as_completed(futures):
            results[futures[future]].append(future.result())

    rows = []
    failures = []
    for number in range(1, 24):
        attempts = sorted(results[number], key=lambda item: str(item["url"]))
        retrieved = sum(bool(item.get("substantive")) for item in attempts)
        passed = len(attempts) >= 2 and retrieved >= 1
        if not passed:
            failures.append(
                f"ethics-{number:02d}: {retrieved} substantive retrievals "
                f"from {len(attempts)} attempts"
            )
        rows.append(
            {
                "topic_key": f"ethics-{number:02d}",
                "access_date": DATE,
                "verification_scope": CLAIM_CLASSES[number],
                "attempted": len(attempts),
                "substantive_retrievals": retrieved,
                "status": "passed" if passed else "failed",
                "sources": attempts,
                "claim_control": (
                    "Retrieval verifies publisher availability and source integrity only. "
                    "Each source supports only propositions stated in its substantive text; "
                    "failed/thin attempts support no claim. Ethical analysis and inference "
                    "remain expressly separate from sourced legal or institutional fact."
                ),
            }
        )
    payload = {
        "schema_version": 1,
        "subject": "Ethics",
        "access_date": DATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "topic_count": 23,
        "result": "failed" if failures else "passed",
        "policy": {
            "authoritative_or_primary_academic_domains_only": True,
            "minimum_attempts_per_topic": 2,
            "minimum_substantive_retrievals_per_topic": 1,
            "failed_intermediates_preserved": True,
            "facts_and_inference_separated": True,
            "quotation_and_thinker_attribution_requires_primary_or_academic_support": True,
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
