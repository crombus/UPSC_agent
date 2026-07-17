"""
LOCAL (API-FREE) query over the philosophy_local Qdrant collection.
Uses the same BAAI/bge-small-en-v1.5 model as ingest_local.py.

Usage:
    python tools/query_books_local.py "<query>" [--limit N] [--book <substr>] [--json]
"""

import sys, json, argparse, warnings
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT       = Path(__file__).parent.parent
PERSIST    = ROOT / "vectordb" / "philosophy_local"
COLLECTION = "philosophy_local"
MODEL_NAME = "BAAI/bge-small-en-v1.5"

_model = None
def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer(MODEL_NAME, device="cpu")
    return _model


def query(q, limit=5, book=None, as_json=False):
    from qdrant_client import QdrantClient
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        client = QdrantClient(path=str(PERSIST))
    vec = _get_model().encode(f"query: {q}", normalize_embeddings=True).tolist()

    flt = None
    if book:
        from qdrant_client.models import Filter, FieldCondition, MatchText
        flt = Filter(must=[FieldCondition(key="book_title", match=MatchText(text=book))])

    res = client.query_points(collection_name=COLLECTION, query=vec,
                              limit=limit, query_filter=flt, with_payload=True).points
    if as_json:
        return json.dumps([{"score": round(r.score, 4),
                            "source": r.payload.get("source", ""),
                            "text": r.payload.get("text", "")} for r in res],
                          ensure_ascii=False, indent=2)
    out = [f"## Philosophy book context — {len(res)} passages\n"]
    for i, r in enumerate(res, 1):
        out.append(f"### [{i}] {r.payload.get('source','?')}  |  score {round(r.score,3)}")
        out.append(r.payload.get("text", "").strip())
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--limit", "-n", type=int, default=5)
    ap.add_argument("--book", "-b", default=None)
    ap.add_argument("--json", "-j", action="store_true")
    a = ap.parse_args()
    print(query(a.query, limit=a.limit, book=a.book, as_json=a.json))
