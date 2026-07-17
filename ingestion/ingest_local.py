"""
LOCAL (API-FREE) Philosophy ingestion — mirrors ingest.py but uses a local
sentence-transformers model instead of the Azure embedding API.

- Embeddings: BAAI/bge-small-en-v1.5 (384-dim, CPU, offline after 1st download)
- Store:      Qdrant local-file DB at vectordb/philosophy_local
- Collection: philosophy_local  (kept SEPARATE from the 3072-dim upsc_static)
- Order:      text-layer books first (fast), scanned books (OCR) last
- Resumable:  per-book checkpoint.json

Usage:
    python ingestion/ingest_local.py            # ingest books/philosphy_books
    python ingestion/ingest_local.py <folder>   # custom folder
"""

import sys, json, uuid, time, shutil
from pathlib import Path
from datetime import datetime

import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, PayloadSchemaType

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT        = Path(__file__).parent.parent
DEFAULT_DIR = ROOT / "books" / "philosphy_books"
PERSIST_DIR = ROOT / "vectordb" / "philosophy_local"
COLLECTION  = "philosophy_local"
MODEL_NAME  = "BAAI/bge-small-en-v1.5"
VECTOR_DIM  = 384
CHUNK_SIZE, CHUNK_OVERLAP = 700, 80

# ── Tesseract for scanned PDFs ────────────────────────────────────────────────
_TESSERACT = next((p for p in [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    shutil.which("tesseract"),
] if p and Path(p).exists()), None)


def _ocr_page(page, page_num: int) -> str:
    try:
        import pytesseract
        if _TESSERACT:
            pytesseract.pytesseract.tesseract_cmd = _TESSERACT
        pix = page.get_pixmap(dpi=300)
        img = Path(f"C:/Windows/Temp/upsc_phil_{page_num}.png")
        pix.save(str(img))
        text = pytesseract.image_to_string(str(img))
        img.unlink(missing_ok=True)
        return text
    except Exception as e:
        print(f"    OCR failed p{page_num}: {e}")
        return ""


def extract_text(pdf_path: Path):
    """Return (text, mode). mode in {'text','ocr','empty'}."""
    doc = fitz.open(str(pdf_path))
    native = [p.get_text("text").strip() for p in doc]
    avg = (sum(len(t) for t in native) / len(native)) if native else 0

    if avg < 200:  # scanned
        pages = []
        for i, page in enumerate(doc):
            t = _ocr_page(page, i).strip()
            if t:
                pages.append(t)
            if i % 25 == 0:
                print(f"      OCR {i+1}/{doc.page_count}...", end="\r")
        doc.close()
        print()
        joined = "\n\n".join(pages)
        return joined, ("ocr" if joined.strip() else "empty")

    pages = []
    for i, page in enumerate(doc):
        t = native[i]
        if len(t) < 50:
            t = _ocr_page(page, i).strip()
        if t.strip():
            pages.append(t)
    doc.close()
    joined = "\n\n".join(pages)
    return joined, ("text" if joined.strip() else "empty")


def priority(p: Path):
    """Text-layer/core first (small key), scanned giants last (large key)."""
    try:
        doc = fitz.open(str(p)); n = doc.page_count
        sample = list(range(0, n, max(1, n // 10)))[:10]
        avg = sum(len(doc[i].get_text("text").strip()) for i in sample) / max(1, len(sample))
        doc.close()
    except Exception:
        n, avg = 9999, 0
    scanned = 1 if avg < 200 else 0
    return (scanned, n)


def init_qdrant() -> QdrantClient:
    PERSIST_DIR.mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=str(PERSIST_DIR))
    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION not in existing:
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(size=VECTOR_DIM, distance=Distance.COSINE),
        )
        client.create_payload_index(COLLECTION, "source", PayloadSchemaType.KEYWORD)
        client.create_payload_index(COLLECTION, "book_title", PayloadSchemaType.KEYWORD)
        print(f"Created collection {COLLECTION}")
    else:
        print(f"Collection {COLLECTION} exists — appending")
    return client


def main(folder=None):
    pdf_dir = Path(folder) if folder else DEFAULT_DIR
    pdfs = sorted(pdf_dir.glob("*.pdf"), key=priority)
    if not pdfs:
        print(f"No PDFs in {pdf_dir}"); sys.exit(1)

    ckpt = PERSIST_DIR / "checkpoint.json"
    done = set()
    if ckpt.exists():
        done = set(json.loads(ckpt.read_text()).get("done", []))
        print(f"Resuming — {len(done)} books already done")
    pending = [p for p in pdfs if p.name not in done]
    print(f"{len(pdfs)} books | {len(done)} done | {len(pending)} to go\n")

    print(f"Loading local model {MODEL_NAME} (one-time download if absent)...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(MODEL_NAME, device="cpu")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " "])
    client = init_qdrant()

    PERSIST_DIR.mkdir(parents=True, exist_ok=True)
    for pdf in pending:
        t0 = time.time()
        mb = round(pdf.stat().st_size / 1_048_576, 1)
        print(f"\n== {pdf.name[:55]} ({mb} MB) ==")
        try:
            text, mode = extract_text(pdf)
            if mode == "empty":
                print("  SKIP: no extractable text (corrupt/empty)")
                done.add(pdf.name); ckpt.write_text(json.dumps({"done": list(done)}))
                continue
            chunks = splitter.split_text(text)
            print(f"  mode={mode} | {len(chunks)} chunks | embedding on CPU...")
            vecs = model.encode(
                [f"passage: {c}" for c in chunks],
                batch_size=64, normalize_embeddings=True,
                show_progress_bar=True, convert_to_numpy=True)
            points = [
                PointStruct(id=str(uuid.uuid4()), vector=vecs[i].tolist(),
                            payload={"text": chunks[i], "source": pdf.name,
                                     "book_title": pdf.stem, "subject": "Philosophy",
                                     "mode": mode, "chunk_index": i})
                for i in range(len(chunks))]
            for i in range(0, len(points), 128):
                client.upsert(collection_name=COLLECTION, points=points[i:i+128])
            done.add(pdf.name)
            ckpt.write_text(json.dumps({"done": list(done)}))
            print(f"  OK {len(chunks)} chunks in {time.time()-t0:.0f}s")
        except Exception as e:
            print(f"  ERROR: {e}")

    cnt = client.get_collection(COLLECTION).points_count
    print(f"\nDONE. Collection {COLLECTION} now has {cnt} vectors.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
