"""
migrate_to_server.py — Copy the full static collection from local-file Qdrant
into the native Qdrant server (Docker, localhost:6333) so server mode works and
queries are fast. Also corrects subject tags for mis-classified books.
"""
import sys, warnings, time
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

from qdrant_client import QdrantClient
from qdrant_client.models import (Distance, VectorParams, PointStruct,
                                  PayloadSchemaType)

COLLECTION = "upsc_static"
VECTOR_DIM = 3072
DB_PATH = ROOT / "vectordb" / "static"

# Subject corrections applied during migration
SUBJECT_FIX = {
    "A-Critical-History-of-Greek-Philosophy.pdf": "Philosophy",
    "HistoryPhilosophy1.pdf": "Philosophy",
}

def main():
    warnings.simplefilter("ignore")
    print("Opening local-file source DB...")
    src = QdrantClient(path=str(DB_PATH))
    total_src = src.get_collection(COLLECTION).points_count
    print(f"  source points: {total_src}")

    print("Connecting to Qdrant server localhost:6333...")
    dst = QdrantClient(host="localhost", port=6333, timeout=60)

    if COLLECTION in [c.name for c in dst.get_collections().collections]:
        dst.delete_collection(COLLECTION)
    dst.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=VECTOR_DIM, distance=Distance.COSINE),
    )
    for field in ("source", "book_title", "subject"):
        dst.create_payload_index(COLLECTION, field, PayloadSchemaType.KEYWORD)
    print("  created collection + payload indexes on server")

    moved = 0
    fixed = 0
    next_off = None
    t0 = time.time()
    while True:
        points, next_off = src.scroll(
            collection_name=COLLECTION, limit=512, offset=next_off,
            with_payload=True, with_vectors=True)
        if not points:
            break
        out = []
        for p in points:
            payload = dict(p.payload)
            new_subj = SUBJECT_FIX.get(payload.get("source"))
            if new_subj and payload.get("subject") != new_subj:
                payload["subject"] = new_subj
                fixed += 1
            out.append(PointStruct(id=p.id, vector=p.vector, payload=payload))
        dst.upsert(collection_name=COLLECTION, points=out, wait=False)
        moved += len(out)
        if moved % 5120 == 0:
            el = time.time() - t0
            print(f"  migrated {moved}/{total_src} ({el:.0f}s)", end="\r")
        if next_off is None:
            break
    print()
    src.close()

    # wait for server to finish indexing then verify
    time.sleep(3)
    final = dst.get_collection(COLLECTION).points_count
    print(f"\nMigration complete in {time.time()-t0:.0f}s")
    print(f"  source: {total_src}  ->  server: {final}")
    print(f"  subject re-tags applied: {fixed}")
    if final != total_src:
        print("  WARNING: count mismatch!")

if __name__ == "__main__":
    main()
