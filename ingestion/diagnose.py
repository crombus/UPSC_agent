"""
Diagnostic: cross-reference each PDF in books/ against what is actually
stored in Qdrant, and measure the text-layer quality of each PDF.

Classifies every book as:
  GOOD      - rich text layer, enough chunks in DB
  CORRUPT   - in DB but with too few chunks for its page count (bad extraction)
  SCANNED   - little/no text layer -> needs OCR
  MISSING   - not in DB at all
"""
import sys, json
from pathlib import Path
import fitz
from qdrant_client import QdrantClient

ROOT = Path(__file__).parent.parent
BOOKS = ROOT / "books"
COLLECTION = "upsc_static"

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass


def qdrant_counts():
    """Return {source: chunk_count} from Qdrant.

    Tries the running Docker server (localhost:6333) first — this is the DB that
    ingest.py writes to and query_books.py reads from. Falls back to local-file
    mode only when the server is unreachable (the file is locked while the
    container runs, so local-file mode cannot be used concurrently)."""
    import warnings
    client = None
    try:
        c = QdrantClient(host="localhost", port=6333, timeout=5)
        c.get_collection(COLLECTION)              # ping
        client = c
        print("Connected to Qdrant server localhost:6333")
    except Exception:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            client = QdrantClient(path=str(ROOT / "vectordb" / "static"))
        print("Using local-file Qdrant DB (server not reachable)")
    counts = {}
    next_off = None
    while True:
        points, next_off = client.scroll(
            collection_name=COLLECTION,
            limit=1000,
            offset=next_off,
            with_payload=["source"],
            with_vectors=False,
        )
        for p in points:
            src = p.payload.get("source", "?")
            counts[src] = counts.get(src, 0) + 1
        if next_off is None:
            break
    return counts


def pdf_quality(path: Path):
    """Return (pages, total_text_chars, chars_per_page, pct_pages_with_text)."""
    try:
        doc = fitz.open(str(path))
    except Exception as e:
        return (-1, 0, 0, 0.0, f"OPEN_FAIL: {e}")
    pages = doc.page_count
    total = 0
    pages_with_text = 0
    sample = min(pages, 40)
    step = max(1, pages // sample)
    sampled = 0
    for i in range(0, pages, step):
        try:
            t = doc[i].get_text("text").strip()
        except Exception:
            t = ""
        total += len(t)
        if len(t) >= 50:
            pages_with_text += 1
        sampled += 1
    doc.close()
    cpp = total / sampled if sampled else 0
    pct = pages_with_text / sampled if sampled else 0
    return (pages, total, round(cpp), round(pct, 2), "ok")


def main():
    counts = qdrant_counts()
    rows = []
    for pdf in sorted(BOOKS.rglob("*.pdf")):
        pages, total, cpp, pct, status = pdf_quality(pdf)
        chunks = counts.get(pdf.name, 0)
        # classification
        if status.startswith("OPEN_FAIL"):
            cls = "OPEN_FAIL"
        elif pct < 0.30 or cpp < 200:
            cls = "SCANNED"          # no real text layer -> needs OCR
        elif chunks == 0:
            cls = "MISSING"
        elif pages > 0 and chunks < pages * 0.5 and chunks < 60:
            cls = "CORRUPT"          # has text but far too few chunks stored
        else:
            cls = "GOOD"
        rows.append({
            "file": pdf.name, "pages": pages, "chars_per_page": cpp,
            "pct_text_pages": pct, "chunks_in_db": chunks, "class": cls,
            "note": status,
        })

    rows.sort(key=lambda r: (r["class"] != "GOOD", r["class"]))
    print(f"{'CLASS':<10}{'CHUNKS':>7}{'PAGES':>7}{'C/PG':>7}{'TXT%':>6}  FILE")
    print("-" * 100)
    for r in rows:
        print(f"{r['class']:<10}{r['chunks_in_db']:>7}{r['pages']:>7}"
              f"{r['chars_per_page']:>7}{r['pct_text_pages']:>6}  {r['file'][:55]}")
    total_chunks = sum(counts.values())
    print("-" * 100)
    print(f"TOTAL chunks in DB: {total_chunks}  |  books in books/: {len(rows)}  |  sources in DB: {len(counts)}")
    bad = [r for r in rows if r["class"] in ("SCANNED", "CORRUPT", "MISSING", "OPEN_FAIL")]
    print(f"Books needing fix: {len(bad)}")
    (ROOT / "vectordb" / "static" / "diagnosis.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Saved -> vectordb/static/diagnosis.json")


if __name__ == "__main__":
    main()
