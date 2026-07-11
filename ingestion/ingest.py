"""
UPSC Agent — Static Vector DB Ingestion Pipeline
Reads all PDFs from books/, chunks them, embeds via Azure Foundry,
and stores in Qdrant (local on-disk) as a permanent static knowledge base.

Why Qdrant:
  - Real-time CRUD for dynamic DB (upsert by URL = no duplicates)
  - Hybrid search (vector + keyword metadata filter)
  - Rust-based, fast, Docker-native, production-ready
  - Static collection = written once, read-only forever after
"""

import os
import sys
import json
import yaml
import uuid
import time
import fitz                          # PyMuPDF
from pathlib import Path

# Fix Windows console Unicode issues (emoji in print statements)
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from datetime import datetime
from tqdm import tqdm
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, PointStruct, PayloadSchemaType
)
sys.path.insert(0, str(Path(__file__).parent.parent))
from agent.azure_auth import get_embedding_model

load_dotenv()

COLLECTION_NAME = "upsc_static"
VECTOR_DIM      = 3072


# ── Rate-limited embed with retry ─────────────────────────────────────────────

def embed_with_retry(embed_model, texts: list, max_retries: int = 6) -> list:
    """Embed with exponential backoff on rate limit (429)."""
    for attempt in range(max_retries):
        try:
            result = embed_model.embed_documents(texts)
            time.sleep(1)           # polite pause between calls
            return result
        except Exception as e:
            if "429" in str(e) or "RateLimitReached" in str(e):
                wait = 60 * (attempt + 1)
                print(f"\n  ⏳ Rate limit — waiting {wait}s (attempt {attempt+1}/{max_retries})")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("Embedding failed after max retries")# text-embedding-3-large dimension


# ── Load config ───────────────────────────────────────────────────────────────

def load_config():
    config_path = Path(__file__).parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


# ── PDF text extraction ───────────────────────────────────────────────────────

# Point pytesseract at the installed binary (it is often not on PATH on Windows).
# Without this, OCR silently fails and scanned PDFs get ingested as empty/garbage.
import shutil
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
        pix      = page.get_pixmap(dpi=300)
        img_path = Path(f"C:/Windows/Temp/upsc_page_{page_num}.png")
        pix.save(str(img_path))
        text = pytesseract.image_to_string(str(img_path))
        img_path.unlink(missing_ok=True)
        return text
    except Exception as e:
        print(f"  ⚠️  OCR failed on page {page_num}: {e}")
        return ""


def extract_text(pdf_path: Path) -> str:
    doc = fitz.open(str(pdf_path))

    # Pass 1: native text layer
    native = [page.get_text("text").strip() for page in doc]
    avg_chars = (sum(len(t) for t in native) / len(native)) if native else 0

    # If the whole document is effectively scanned (thin/garbage text layer,
    # e.g. watermark-only pages), OCR every page instead of trusting the layer.
    if avg_chars < 200:
        if not _TESSERACT:
            print("  ⚠️  Document looks scanned but Tesseract not found — install it.")
        print(f"  🔎 Scanned PDF detected (avg {avg_chars:.0f} chars/pg) — OCR all pages")
        pages = []
        for page_num, page in enumerate(doc):
            t = _ocr_page(page, page_num).strip()
            if t:
                pages.append(t)
        doc.close()
        return "\n\n".join(pages)

    # Otherwise use native text, OCR only the occasional empty page
    pages = []
    for page_num, page in enumerate(doc):
        text = native[page_num]
        if len(text) < 50:
            text = _ocr_page(page, page_num).strip()
        if text.strip():
            pages.append(text)

    doc.close()
    return "\n\n".join(pages)


# ── Embedding model ───────────────────────────────────────────────────────────

def get_embeddings():
    return get_embedding_model()


# ── Qdrant setup ──────────────────────────────────────────────────────────────

def init_qdrant(persist_dir: Path) -> QdrantClient:
    """
    Connect to the Qdrant SERVER (localhost:6333) so new books land in the same
    collection that query_books reads. Falls back to local-file mode only if the
    server is unreachable (start it with the docker run command in the README).
    """
    persist_dir.mkdir(parents=True, exist_ok=True)
    try:
        client = QdrantClient(host="localhost", port=6333, timeout=10)
        client.get_collections()                      # ping
        print("🔌 Connected to Qdrant server localhost:6333")
    except Exception:
        print("⚠️  Qdrant server not reachable — falling back to local-file mode.\n"
              "    For a single shared DB, start the server first:\n"
              "    docker start qdrant-upsc")
        client = QdrantClient(path=str(persist_dir))

    existing = [c.name for c in client.get_collections().collections]
    if COLLECTION_NAME not in existing:
        client.create_collection(
            collection_name = COLLECTION_NAME,
            vectors_config  = VectorParams(size=VECTOR_DIM, distance=Distance.COSINE),
        )
        # Index payload fields for fast metadata filtering
        client.create_payload_index(COLLECTION_NAME, "source",     PayloadSchemaType.KEYWORD)
        client.create_payload_index(COLLECTION_NAME, "book_title", PayloadSchemaType.KEYWORD)
        client.create_payload_index(COLLECTION_NAME, "subject",    PayloadSchemaType.KEYWORD)
        print(f"✅ Created Qdrant collection: {COLLECTION_NAME}")
    else:
        print(f"ℹ️  Collection already exists: {COLLECTION_NAME} — appending")

    return client


# ── Infer subject from filename ───────────────────────────────────────────────

SUBJECT_KEYWORDS = {
    "polity": "Indian Polity", "laxmikant": "Indian Polity",
    "geography": "Geography", "leong": "Geography", "khullar": "Geography",
    "history": "History", "bipin": "History", "sharma": "History",
    "economy": "Economy", "ramesh": "Economy", "economic survey": "Economy",
    "ethics": "Ethics",
    "security": "Internal Security", "disaster": "Disaster Management",
    "foreign": "International Relations", "tharoor": "International Relations",
    "philosophy": "Philosophy",
    "ncert": "NCERT",
    "vision": "Current Affairs",
    "vajiram": "Current Affairs",
}

def infer_subject(pdf_path) -> str:
    """
    Infer the subject tag for a PDF.

    Previous-year question papers (PYQs) live in dedicated subfolders, so the
    parent folder is the most reliable signal — filenames like
    "02 UPSC 2024 Paper-II.pdf" carry no subject word. Distinct PYQ tags keep
    them queryable for difficulty / question-style calibration. Books in the
    books/ root fall back to filename-keyword inference (unchanged behaviour).
    """
    p      = Path(pdf_path)
    name   = p.name.lower()
    parent = p.parent.name.lower()

    if parent == "mains":
        return "Mains PYQ"
    if parent.startswith("philosophy"):
        return "Philosophy PYQ"
    if parent.startswith("prelim"):
        return "CSAT PYQ" if "csat" in name else "Prelims PYQ"

    for keyword, subject in SUBJECT_KEYWORDS.items():
        if keyword in name:
            return subject
    return "General Studies"


# ── Main ingestion ────────────────────────────────────────────────────────────

def ingest(pdf_dir: str = None):
    config   = load_config()
    pdf_dir  = Path(pdf_dir) if pdf_dir else Path(__file__).parent.parent / "books"
    persist_dir = Path(__file__).parent.parent / "vectordb" / "static"
    checkpoint_file = persist_dir / "checkpoint.json"

    pdf_files = list(pdf_dir.rglob("*.pdf"))
    if not pdf_files:
        print(f"❌ No PDFs found in {pdf_dir}")
        sys.exit(1)

    # Load checkpoint — skip already-ingested books on resume
    done_files = set()
    if checkpoint_file.exists():
        with open(checkpoint_file) as f:
            done_files = set(json.load(f).get("done", []))
        print(f"♻️  Resuming — {len(done_files)} books already done, skipping them")

    pending = [p for p in pdf_files if p.name not in done_files]
    print(f"\n📚 {len(pdf_files)} total PDFs | {len(done_files)} done | {len(pending)} to process")
    print(f"📦 Qdrant DB → {persist_dir}\n")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size    = config["embedding"]["chunk_size"],
        chunk_overlap = config["embedding"]["chunk_overlap"],
        separators    = ["\n\n", "\n", ". ", " "],
    )

    embed_model = get_embeddings()
    client      = init_qdrant(persist_dir)
    manifest    = []
    total_chunks = 0

    for pdf_path in tqdm(pending, desc="Ingesting books"):
        try:
            size_mb = round(pdf_path.stat().st_size / 1_048_576, 1)
            print(f"\n  📖 {pdf_path.name} ({size_mb} MB)")

            print(f"     Extracting text...")
            raw_text = extract_text(pdf_path)

            if not raw_text.strip():
                print(f"  ⚠️  Skipped (no extractable text)")
                manifest.append({"file": pdf_path.name, "status": "skipped"})
                done_files.add(pdf_path.name)
                continue

            chunks  = splitter.split_text(raw_text)
            subject = infer_subject(pdf_path)
            print(f"     {len(chunks)} chunks | Subject: {subject}")

            # Embed in micro-batches of 3 (S0 rate limit friendly)
            micro_batch = 3
            all_vectors = []
            for i in range(0, len(chunks), micro_batch):
                batch_texts = chunks[i:i+micro_batch]
                batch_vecs  = embed_with_retry(embed_model, batch_texts)
                all_vectors.extend(batch_vecs)
                if (i // micro_batch) % 10 == 0:
                    print(f"     Embedded {min(i+micro_batch, len(chunks))}/{len(chunks)} chunks...", end="\r")
            print()

            points = [
                PointStruct(
                    id      = str(uuid.uuid4()),
                    vector  = all_vectors[i],
                    payload = {
                        "text":        chunks[i],
                        "source":      pdf_path.name,
                        "book_title":  pdf_path.stem,
                        "subject":     subject,
                        "chunk_index": i,
                        "total_chunks": len(chunks),
                    }
                )
                for i in range(len(chunks))
            ]

            # Batch upsert in groups of 100
            batch_size = 100
            for i in range(0, len(points), batch_size):
                client.upsert(collection_name=COLLECTION_NAME, points=points[i:i+batch_size])

            total_chunks += len(chunks)
            done_files.add(pdf_path.name)
            manifest.append({
                "file":        pdf_path.name,
                "subject":     subject,
                "status":      "ingested",
                "chunks":      len(chunks),
                "ingested_at": datetime.utcnow().isoformat(),
            })
            print(f"  ✅ {pdf_path.name} — {len(chunks)} chunks stored")

            # Save checkpoint after every book so we can resume if interrupted
            persist_dir.mkdir(parents=True, exist_ok=True)
            with open(checkpoint_file, "w") as f:
                json.dump({"done": list(done_files)}, f)

        except Exception as e:
            print(f"  ❌ {pdf_path.name}: {e}")
            manifest.append({"file": pdf_path.name, "status": "error", "reason": str(e)})

    # Write manifest
    manifest_data = {
        "total_books":       len(pdf_files),
        "total_chunks":      total_chunks,
        "created_at":        datetime.utcnow().isoformat(),
        "embedding_model":   os.environ.get("AZURE_EMBEDDING_DEPLOYMENT", "unknown"),
        "vector_db":         "qdrant",
        "collection":        COLLECTION_NAME,
        "books":             manifest,
    }
    manifest_path = persist_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest_data, f, indent=2)

    info = client.get_collection(COLLECTION_NAME)
    print(f"\n{'─'*55}")
    print(f"✅ Ingestion complete!")
    print(f"   Books      : {len(pdf_files)}")
    print(f"   Chunks     : {total_chunks}")
    print(f"   Vectors    : {info.points_count}")
    print(f"   DB path    : {persist_dir}")
    print(f"   Manifest   : {manifest_path}")
    print(f"{'─'*55}\n")


if __name__ == "__main__":
    ingest(sys.argv[1] if len(sys.argv) > 1 else None)

