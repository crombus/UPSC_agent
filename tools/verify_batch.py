"""
Batch verification helper — loads the local model ONCE and runs many queries
against philosophy_local, printing top passages per query. Feeds the note
verify/enrich pass without paying the model-load cost per query.

Usage:
    python tools/verify_batch.py queries.txt [--limit 3]
    # queries.txt: one query per line; blank lines and #comments ignored
"""
import sys, argparse, warnings
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass

ROOT       = Path(__file__).parent.parent
PERSIST    = ROOT / "vectordb" / "philosophy_local"
COLLECTION = "philosophy_local"
MODEL_NAME = "BAAI/bge-small-en-v1.5"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries_file")
    ap.add_argument("--limit", "-n", type=int, default=3)
    ap.add_argument("--chars", "-c", type=int, default=500)
    a = ap.parse_args()

    qs = [l.strip() for l in Path(a.queries_file).read_text(encoding="utf-8").splitlines()
          if l.strip() and not l.strip().startswith("#")]

    from sentence_transformers import SentenceTransformer
    from qdrant_client import QdrantClient
    model = SentenceTransformer(MODEL_NAME, device="cpu")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        client = QdrantClient(path=str(PERSIST))

    for q in qs:
        vec = model.encode(f"query: {q}", normalize_embeddings=True).tolist()
        res = client.query_points(collection_name=COLLECTION, query=vec,
                                  limit=a.limit, with_payload=True).points
        print("\n" + "=" * 90)
        print(f"Q: {q}")
        print("=" * 90)
        for i, r in enumerate(res, 1):
            src = r.payload.get("source", "?")[:45]
            txt = " ".join(r.payload.get("text", "").split())[:a.chars]
            print(f"[{i}] ({round(r.score,3)}) {src}\n    {txt}\n")


if __name__ == "__main__":
    main()
