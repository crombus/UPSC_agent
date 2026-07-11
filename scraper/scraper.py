"""
UPSC Agent — Dynamic Vector DB Scraper
Fetches live current affairs from:
  - PIB (English): https://www.pib.gov.in/Allrel.aspx?reg=3&lang=1
  - MEA:           https://www.mea.gov.in/news.htm  → newsdetail1.htm articles
  - Vajiram & Ravi: https://vajiramandravi.com/current-affairs/upsc-prelims-current-affairs/
Uses Qdrant UPSERT keyed by article URL — same article updates in place,
new articles are added. Runs on daily cron schedule.
"""

import os
import uuid
import yaml
import hashlib
import requests
import schedule
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from agent.azure_auth import get_embedding_model

load_dotenv()

COLLECTION_NAME = "upsc_dynamic"
VECTOR_DIM      = 3072
HEADERS         = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


def load_config():
    config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def init_qdrant() -> QdrantClient:
    dynamic_dir = Path(__file__).parent.parent / "vectordb" / "dynamic"
    dynamic_dir.mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=str(dynamic_dir))
    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME not in existing:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_DIM, distance=Distance.COSINE),
        )
        print(f"✅ Created collection: {COLLECTION_NAME}")
    return client


def point_id(url: str, chunk_index: int) -> str:
    key = f"{url}::{chunk_index}"
    return str(uuid.UUID(hashlib.md5(key.encode()).hexdigest()))


def _is_english(text: str) -> bool:
    clean = text.replace(" ", "").replace("\n", "")
    if not clean:
        return False
    return sum(1 for c in clean if ord(c) < 128) / len(clean) > 0.6


# ── PIB: English press releases ───────────────────────────────────────────────

def scrape_pib(max_articles: int) -> list[dict]:
    """English PIB press releases — reg=3 (national), lang=1 (English)."""
    articles = []
    try:
        resp = requests.get(
            "https://www.pib.gov.in/Allrel.aspx?reg=3&lang=1",
            headers=HEADERS, timeout=15
        )
        soup = BeautifulSoup(resp.text, "html.parser")
        hrefs = [
            a["href"] for a in soup.find_all("a", href=True)
            if "PRID=" in a.get("href", "")
        ][:max_articles * 3]
    except Exception as e:
        print(f"⚠️  PIB listing failed: {e}")
        return []

    fetched = 0
    for href in hrefs:
        if fetched >= max_articles:
            break
        art_url = ("https://pib.gov.in" + href) if href.startswith("/") else href
        try:
            r = requests.get(art_url, headers=HEADERS, timeout=10)
            s = BeautifulSoup(r.text, "html.parser")
            title_tag = s.find("h2")
            body_div  = s.find("div", class_="innner-page-main-about-us-content-right-part")
            if not (title_tag and body_div):
                continue
            title_txt = title_tag.get_text(strip=True)
            content   = body_div.get_text(separator="\n", strip=True)
            # Require English title (>70% ASCII) and body (>50% ASCII)
            t_clean = title_txt.replace(" ", "")
            b_clean = content.replace(" ", "").replace("\n", "")
            if not t_clean or sum(1 for c in t_clean if ord(c) < 128) / len(t_clean) < 0.70:
                continue
            if not b_clean or sum(1 for c in b_clean if ord(c) < 128) / len(b_clean) < 0.50:
                continue
            articles.append({
                "title":      title_txt,
                "content":    content,
                "source":     "PIB",
                "url":        art_url,
                "scraped_at": datetime.utcnow().isoformat(),
            })
            fetched += 1
        except Exception:
            continue
    return articles


# ── Vajiram & Ravi: UPSC Prelims current affairs ─────────────────────────────

# Category/nav slugs to exclude from Vajiram listing
_VAJIRAM_SKIP = {
    "upsc-prelims-current-affairs", "upsc-mains-current-affairs",
    "daily-editorial-analysis", "upsc-syllabus-in-hindi",
    "economic-survey-2026", "economic-survey-2025",
}

def scrape_vajiram(max_articles: int) -> list[dict]:
    """Vajiram & Ravi daily UPSC Prelims Pointers (individual topic articles)."""
    articles = []
    listing_url = "https://vajiramandravi.com/current-affairs/upsc-prelims-current-affairs/"
    try:
        resp = requests.get(listing_url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")
        seen = set()
        hrefs = []
        for a in soup.find_all("a", href=True):
            href = a.get("href", "")
            txt  = a.get_text(strip=True)
            if "/current-affairs/" not in href or len(txt) < 10:
                continue
            slug = href.rstrip("/").split("/")[-1]
            if slug in _VAJIRAM_SKIP or href in seen:
                continue
            seen.add(href)
            hrefs.append(href)
    except Exception as e:
        print(f"⚠️  Vajiram listing failed: {e}")
        return []

    fetched = 0
    for art_url in hrefs[:max_articles * 2]:
        if fetched >= max_articles:
            break
        try:
            r = requests.get(art_url, headers=HEADERS, timeout=10)
            s = BeautifulSoup(r.text, "html.parser")
            title_tag = s.find("h1") or s.find("h2")
            body_div  = s.find("div", class_=lambda c: c and "content" in c.lower())
            if not (title_tag and body_div):
                continue
            content = body_div.get_text(separator="\n", strip=True)
            if len(content) < 150:
                continue
            articles.append({
                "title":      title_tag.get_text(strip=True),
                "content":    content,
                "source":     "Vajiram & Ravi",
                "url":        art_url,
                "scraped_at": datetime.utcnow().isoformat(),
            })
            fetched += 1
        except Exception:
            continue
    return articles


# ── MEA: latest news from news.htm ───────────────────────────────────────────

def scrape_mea(max_articles: int) -> list[dict]:
    """MEA latest news — newsdetail1.htm articles from the News section."""
    articles = []
    try:
        resp = requests.get("https://www.mea.gov.in/news.htm", headers=HEADERS, timeout=15)
        soup = BeautifulSoup(resp.text, "html.parser")
        # News section links → newsdetail1.htm?{id}/
        news_links = [
            a["href"] for a in soup.find_all("a", href=True)
            if "newsdetail1.htm" in a.get("href", "")
        ][:max_articles * 2]
    except Exception as e:
        print(f"⚠️  MEA listing failed: {e}")
        return []

    for href in news_links[:max_articles]:
        art_url = href if href.startswith("http") else "https://www.mea.gov.in/" + href.lstrip("/")
        try:
            r = requests.get(art_url, headers=HEADERS, timeout=10)
            s = BeautifulSoup(r.text, "html.parser")
            title_tag = s.find("h1") or s.find("h2")
            body_div  = s.find("div", class_=lambda c: c and "content" in c.lower())
            if not (title_tag and body_div):
                continue
            content = body_div.get_text(separator="\n", strip=True)
            if len(content) < 100:
                continue
            articles.append({
                "title":      title_tag.get_text(strip=True),
                "content":    content,
                "source":     "MEA",
                "url":        art_url,
                "scraped_at": datetime.utcnow().isoformat(),
            })
        except Exception:
            continue
    return articles


# ── Vision IAS: daily current affairs ────────────────────────────────────────

def scrape_vision_ias(max_articles: int) -> list[dict]:
    """Vision IAS daily current affairs — news-today pages for recent days."""
    articles = []
    fetched  = 0

    for days_back in range(0, 14):
        if fetched >= max_articles:
            break
        date_str  = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y-%m-%d")
        page_url  = f"https://visionias.in/current-affairs/news-today/{date_str}/"
        try:
            resp = requests.get(page_url, headers=HEADERS, timeout=15)
            if resp.status_code != 200:
                continue
            soup = BeautifulSoup(resp.text, "html.parser")

            # Each article section is an <article> or a heading block
            sections = soup.find_all(["article", "section"], limit=max_articles * 2)
            if not sections:
                # Fallback: treat whole page body as one article
                body = soup.find("main") or soup.find("div", class_=lambda c: c and "content" in c.lower())
                if not body:
                    continue
                text = body.get_text(separator="\n", strip=True)
                if len(text) < 200:
                    continue
                articles.append({
                    "title":      f"Vision IAS CA — {date_str}",
                    "content":    text[:4000],
                    "source":     "Vision IAS",
                    "url":        page_url,
                    "scraped_at": datetime.utcnow().isoformat(),
                })
                fetched += 1
                continue

            for sec in sections:
                if fetched >= max_articles:
                    break
                title_tag = sec.find(["h1", "h2", "h3"])
                if not title_tag:
                    continue
                title_txt = title_tag.get_text(strip=True)
                content   = sec.get_text(separator="\n", strip=True)
                if len(content) < 150:
                    continue
                articles.append({
                    "title":      title_txt,
                    "content":    content,
                    "source":     "Vision IAS",
                    "url":        page_url,
                    "scraped_at": datetime.utcnow().isoformat(),
                })
                fetched += 1
        except Exception as e:
            print(f"⚠️  Vision IAS {date_str} failed: {e}")
            continue

    return articles


# ── Main ──────────────────────────────────────────────────────────────────────

def run_scraper():
    config      = load_config()
    max_art     = config["scraper"]["max_articles_per_source"]
    embed_model = get_embedding_model()
    client      = init_qdrant()
    splitter    = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    source_map = {
        "pib":        (scrape_pib,        config["sources"].get("pib",        False)),
        "mea":        (scrape_mea,        config["sources"].get("mea",        False)),
        "vajiram":    (scrape_vajiram,    config["sources"].get("vajiram",    config["sources"].get("drishti_ias", False))),
        "vision_ias": (scrape_vision_ias, config["sources"].get("vision_ias", False)),
    }

    total_upserted = 0
    print(f"\n🌐 Scraper started — {datetime.utcnow().isoformat()}")

    for name, (fn, enabled) in source_map.items():
        if not enabled:
            print(f"  ⏭️  {name}: disabled")
            continue
        print(f"  Scraping {name}...")
        articles = fn(max_art)

        for article in articles:
            chunks  = splitter.split_text(article["content"])
            if not chunks:
                continue
            vectors = embed_model.embed_documents(chunks)
            points  = [
                PointStruct(
                    id      = point_id(article["url"], i),
                    vector  = vectors[i],
                    payload = {
                        "text":       chunks[i],
                        "source":     article["source"],
                        "title":      article["title"],
                        "url":        article["url"],
                        "scraped_at": article["scraped_at"],
                        "chunk":      i,
                    },
                )
                for i in range(len(chunks))
            ]
            client.upsert(collection_name=COLLECTION_NAME, points=points)
            total_upserted += len(points)

        print(f"    ✅ {name}: {len(articles)} articles → {total_upserted} total vectors")

    print(f"\n✅ Done — total vectors in dynamic DB: "
          f"{client.get_collection(COLLECTION_NAME).points_count}\n")


if __name__ == "__main__":
    cfg = load_config()
    run_scraper()
    cron   = cfg["scraper"].get("schedule", "0 6 * * *").split()
    hh, mm = cron[1].zfill(2), cron[0].zfill(2)
    t      = f"{hh}:{mm}"
    schedule.every().day.at(t).do(run_scraper)
    print(f"⏰ Scheduled daily at {t}. Ctrl-C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)
