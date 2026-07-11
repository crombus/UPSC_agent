"""
fix_ocr.py — Repair scanned/corrupt books in the Qdrant static DB.

For each broken book:
  1. OCR every page in parallel (16-core pool), cache full text to ocr_cache/.
  2. Delete any existing (garbage/watermark) points for that source from Qdrant.
  3. Chunk + embed (Azure text-embedding-3-large) + upsert fresh points.
  4. Update checkpoint.json, manifest.json, and a fix log.

Resumable: OCR text is cached per book; re-running skips finished OCR and
skips books already marked done in fix_state.json.

Usage:
  python ingestion/fix_ocr.py            # OCR + re-embed all broken books
  python ingestion/fix_ocr.py --ocr-only
  python ingestion/fix_ocr.py --embed-only
"""
import os, sys, json, time, uuid, argparse, io
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
BOOKS      = ROOT / "books"
DB_PATH    = ROOT / "vectordb" / "static"
OCR_CACHE  = ROOT / "ingestion" / "ocr_cache"
FIX_STATE  = DB_PATH / "fix_state.json"
COLLECTION = "upsc_static"
VECTOR_DIM = 3072
DPI        = 300
OCR_WORKERS = 12

# Books identified as scanned/corrupt by diagnose.py
BROKEN = [
    "A-Critical-History-of-Greek-Philosophy.pdf",
    "ANCIENT HISTORY OF INDIA -- RAMSHARAN SHARMA -- ENGLISH ##.pdf",
    "Challenges_to_Internal_Security_of_India_Ashok_kumar_singh.pdf",
    "Chatterjeedatta_introductionToIndianPhilosophy.pdf",
    "D.R.Khullar.pdf",
    "Economics Optional B-01 Vajiram & Ravi.pdf",
    "GC Leong - Certificate Physical and human Geography.pdf",
    "HistoryPhilosophy1.pdf",
    "Indian & World Geography - Husain, Majid_Compressed.pdf",
    "Indian Philosophy Vol. 2 by Radhakrishnan.pdf",
    "Indian-geography-majid-hussain.pdf",
]

SUBJECT_KEYWORDS = {
    "polity": "Indian Polity", "laxmikant": "Indian Polity",
    "geography": "Geography", "leong": "Geography", "khullar": "Geography",
    "hussain": "Geography", "husain": "Geography",
    "history": "History", "bipin": "History", "sharma": "History",
    "economy": "Economy", "ramesh": "Economy", "economic": "Economy",
    "ethics": "Ethics",
    "security": "Internal Security", "disaster": "Disaster Management",
    "foreign": "International Relations", "tharoor": "International Relations",
    "philosophy": "Philosophy",
    "vision": "Current Affairs", "vajiram": "Economy",
}

def infer_subject(filename: str) -> str:
    name = filename.lower()
    for kw, subj in SUBJECT_KEYWORDS.items():
        if kw in name:
            return subj
    return "General Studies"

def safe_name(fname: str) -> str:
    return "".join(c if c.isalnum() else "_" for c in fname)[:120]

# ── OCR worker (one per process; opens its own doc handle) ────────────────────
_W = {}
def _ocr_init(pdf_path: str):
    import fitz, pytesseract
    pytesseract.pytesseract.tesseract_cmd = TESSERACT
    os.environ["OMP_THREAD_LIMIT"] = "1"
    _W["doc"] = fitz.open(pdf_path)
    _W["pt"] = pytesseract

def _ocr_page(page_no: int):
    import fitz
    from PIL import Image
    doc = _W["doc"]; pt = _W["pt"]
    try:
        pix = doc[page_no].get_pixmap(dpi=DPI)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        txt = pt.image_to_string(img)
        return page_no, txt
    except Exception as e:
        return page_no, f""

def ocr_book(fname: str) -> str:
    import fitz
    cache = OCR_CACHE / (safe_name(fname) + ".txt")
    if cache.exists() and cache.stat().st_size > 500:
        print(f"     OCR cache hit ({cache.stat().st_size//1024} KB)")
        return cache.read_text(encoding="utf-8")
    pdf_path = str(BOOKS / fname)
    n = fitz.open(pdf_path).page_count
    print(f"     OCR {n} pages with {OCR_WORKERS} workers @ {DPI}dpi...")
    results = [""] * n
    t0 = time.time()
    done = 0
    with ProcessPoolExecutor(max_workers=OCR_WORKERS,
                             initializer=_ocr_init, initargs=(pdf_path,)) as ex:
        for page_no, txt in ex.map(_ocr_page, range(n), chunksize=2):
            results[page_no] = txt
            done += 1
            if done % 25 == 0 or done == n:
                el = time.time() - t0
                print(f"       {done}/{n} pages  ({el:.0f}s, {el/done:.1f}s/pg)", end="\r")
    print()
    full = "\n\n".join(t.strip() for t in results if t.strip())
    OCR_CACHE.mkdir(parents=True, exist_ok=True)
    cache.write_text(full, encoding="utf-8")
    print(f"     OCR done: {len(full)} chars -> {cache.name}")
    return full

# ── Embedding ────────────────────────────────────────────────────────────────
def embed_with_retry(embed_model, texts, max_retries=6):
    for attempt in range(max_retries):
        try:
            r = embed_model.embed_documents(texts)
            time.sleep(0.2)
            return r
        except Exception as e:
            if "429" in str(e) or "RateLimit" in str(e):
                wait = 30 * (attempt + 1)
                print(f"\n     rate limit, wait {wait}s ({attempt+1}/{max_retries})")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("embed failed")

def reembed_book(client, embed_model, splitter, fname: str, text: str):
    from qdrant_client.models import (PointStruct, Filter, FieldCondition,
                                      MatchValue, FilterSelector)
    subject = infer_subject(fname)
    chunks = splitter.split_text(text)
    print(f"     {len(chunks)} chunks | subject={subject} | purging old points...")
    client.delete(collection_name=COLLECTION, points_selector=FilterSelector(
        filter=Filter(must=[FieldCondition(key="source", match=MatchValue(value=fname))])))
    batch = 16
    vectors = []
    for i in range(0, len(chunks), batch):
        vectors.extend(embed_with_retry(embed_model, chunks[i:i+batch]))
        print(f"       embedded {min(i+batch,len(chunks))}/{len(chunks)}", end="\r")
    print()
    points = [PointStruct(id=str(uuid.uuid4()), vector=vectors[i], payload={
        "text": chunks[i], "source": fname, "book_title": Path(fname).stem,
        "subject": subject, "chunk_index": i, "total_chunks": len(chunks),
    }) for i in range(len(chunks))]
    for i in range(0, len(points), 100):
        client.upsert(collection_name=COLLECTION, points=points[i:i+100])
    return len(chunks), subject

# ── State helpers ────────────────────────────────────────────────────────────
def load_state():
    if FIX_STATE.exists():
        return json.loads(FIX_STATE.read_text())
    return {"ocr_done": [], "embed_done": [], "results": {}}

def save_state(s):
    FIX_STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")

# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ocr-only", action="store_true")
    ap.add_argument("--embed-only", action="store_true")
    ap.add_argument("--only", default="", help="substring filter to process one book")
    args = ap.parse_args()

    state = load_state()
    books = [b for b in BROKEN if args.only.lower() in b.lower()] if args.only else BROKEN
    print(f"Broken books to fix: {len(books)}")

    # Phase 1: OCR (cache to disk)
    if not args.embed_only:
        for fname in books:
            print(f"\n[OCR] {fname}")
            if fname in state["ocr_done"]:
                print("     already OCR'd, skip"); continue
            ocr_book(fname)
            state["ocr_done"].append(fname); save_state(state)

    if args.ocr_only:
        print("\nOCR phase complete."); return

    # Phase 2: re-embed into Qdrant (local-file mode; Docker must be stopped)
    import warnings
    from qdrant_client import QdrantClient
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from agent.azure_auth import get_embedding_model
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", ". ", " "])
    embed_model = get_embedding_model()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        client = QdrantClient(path=str(DB_PATH))

    for fname in books:
        print(f"\n[EMBED] {fname}")
        if fname in state["embed_done"]:
            print("     already embedded, skip"); continue
        cache = OCR_CACHE / (safe_name(fname) + ".txt")
        if not cache.exists():
            print("     no OCR cache, run OCR first"); continue
        text = cache.read_text(encoding="utf-8")
        if len(text.strip()) < 500:
            print(f"     WARNING: OCR text too short ({len(text)}), skipping"); continue
        n, subj = reembed_book(client, embed_model, splitter, fname, text)
        state["embed_done"].append(fname)
        state["results"][fname] = {"chunks": n, "subject": subj,
                                   "fixed_at": datetime.utcnow().isoformat()}
        save_state(state)
        print(f"  OK {fname}: {n} chunks")

    print(f"\nDONE. Fixed {len(state['embed_done'])}/{len(BROKEN)} books.")

if __name__ == "__main__":
    main()
