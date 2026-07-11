"""
UPSC Agent — Web Search Module
Provides AI-powered web search via LangChain community tools,
plus direct live fetching of approved CA sources by date.

Priority:
  1. Tavily  (AI-powered, citations) — set TAVILY_API_KEY in .env
  2. DuckDuckGo (free, no key needed) — automatic fallback

Usage:
  from agent.web_search import web_search, fetch_ca_live
  results = web_search("UPSC current affairs June 2026 India PIB")
  ca_text = fetch_ca_live("2026-06-05")
"""

import os
import re
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

_TAVILY_KEY = os.getenv("TAVILY_API_KEY", "")
_HEADERS    = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
_TIMEOUT = 12


# ─── Direct CA source fetchers ────────────────────────────────────────────────

def fetch_ca_live(date_str: str, source_filter: str = "") -> str:
    """
    Directly fetch current affairs content for a specific date from approved sources.
    Returns combined text ready to inject as LLM context.

    source_filter: '' (all) | 'PIB' | 'MEA' | 'Vajiram' | 'Vision IAS'
    """
    from bs4 import BeautifulSoup

    parts   = []
    sf      = source_filter.strip().lower()

    def _fetch(url: str, label: str, css_selectors: list[str], max_chars: int = 3000) -> str:
        """Fetch a URL and extract text from the first matching CSS selector."""
        try:
            r    = requests.get(url, headers=_HEADERS, timeout=_TIMEOUT)
            soup = BeautifulSoup(r.text, "html.parser")
            for sel in css_selectors:
                el = soup.select(sel)
                if el:
                    text = "\n".join(e.get_text(" ", strip=True) for e in el)
                    return f"[{label} | {url}]\n{text[:max_chars]}"
            # Fallback: body text
            body = soup.get_text(" ", strip=True)
            return f"[{label} | {url}]\n{body[:max_chars]}"
        except Exception as exc:
            return f"[{label}] Fetch error: {exc}"

    # ── Vision IAS (date-specific URL) ────────────────────────────────────────
    if sf in ("", "vision ias", "visionias"):
        url  = f"https://visionias.in/current-affairs/news-today/{date_str}/"
        text = _fetch(url, f"Vision IAS — {date_str}",
                      ["article", "section.news", ".current-affairs-content",
                       ".ca-content", "main", "#content"])
        parts.append(text)

    # ── PIB (listing page, filter by date in text) ─────────────────────────────
    if sf in ("", "pib"):
        # PIB listing for the date (by year/month path if available)
        try:
            dt   = datetime.strptime(date_str, "%Y-%m-%d")
            # PIB has a date-filtered view via search
            url  = (
                f"https://www.pib.gov.in/indexd.aspx?reg=3&lang=1"
            )
            r    = requests.get(url, headers=_HEADERS, timeout=_TIMEOUT)
            soup = BeautifulSoup(r.text, "html.parser")
            # Get all headline links and their text
            headlines = soup.select("ul.rel-list li a, .content-area a, h3 a, h2 a")
            items     = [a.get_text(" ", strip=True) for a in headlines if a.get_text(strip=True)]
            if items:
                text = "\n".join(f"• {it}" for it in items[:40])
                parts.append(f"[PIB listing | {url}]\n{text}")
            else:
                parts.append(f"[PIB] No headlines extracted from listing page.")
        except Exception as exc:
            parts.append(f"[PIB] Fetch error: {exc}")

    # ── MEA (press releases listing) ──────────────────────────────────────────
    if sf in ("", "mea"):
        url  = "https://www.mea.gov.in/press-releases.htm"
        text = _fetch(url, f"MEA Press Releases",
                      [".releaseList li", ".press-list li", "ul.list li", "main"])
        parts.append(text)

    # ── Vajiram (CA daily listing) ─────────────────────────────────────────────
    if sf in ("", "vajiram"):
        url  = "https://vajiramandravi.com/current-affairs/upsc-prelims-current-affairs/"
        text = _fetch(url, "Vajiram & Ravi CA",
                      [".ca-list article", ".article-card", ".post-title",
                       ".entry-title", "article h2 a", "h2.entry-title"])
        parts.append(text)

    combined = "\n\n" + ("=" * 60) + "\n\n".join(parts)
    return combined if combined.strip() else ""


# ─── Web search (general) ─────────────────────────────────────────────────────

def web_search(query: str, max_results: int = 5) -> str:
    """
    Search the web using Tavily (if key set) or DuckDuckGo (free fallback).
    Returns formatted snippets ready to inject into LLM context.
    """
    if _TAVILY_KEY:
        return _tavily_search(query, max_results)
    return _ddg_search(query, max_results)


def _tavily_search(query: str, max_results: int) -> str:
    """Tavily — AI-powered search with citations."""
    try:
        from langchain_community.tools.tavily_search import TavilySearchResults
        tool    = TavilySearchResults(max_results=max_results, tavily_api_key=_TAVILY_KEY)
        results = tool.invoke(query)
        if not results:
            return ""
        lines = []
        for r in results:
            title   = r.get("title", "")[:80]
            url     = r.get("url", "")
            content = r.get("content", "")[:500]
            lines.append(f"[Tavily: {title}]\nURL: {url}\n{content}")
        return "\n\n".join(lines)
    except Exception as e:
        return _ddg_search(query, max_results)


def _ddg_search(query: str, max_results: int) -> str:
    """DuckDuckGo — free fallback, no API key required."""
    try:
        from langchain_community.tools import DuckDuckGoSearchResults
        tool    = DuckDuckGoSearchResults(num_results=max_results)
        results = tool.invoke(query)
        return str(results) if results else ""
    except Exception as e:
        return f"[Web search unavailable: {e}]"


def search_backend() -> str:
    """Return which backend is active."""
    return "Tavily (AI-powered)" if _TAVILY_KEY else "DuckDuckGo (free fallback)"
