"""
UPSC Book Context Query Tool
Queries the local Qdrant vector DB (58K+ chunks from 35 books) and returns
relevant passages for a given query. Called by Copilot CLI before teaching/exam sessions.

Usage:
    python tools/query_books.py "<query>" [--subject <subject>] [--limit <n>] [--json]

Connection priority:
    1. Qdrant Docker server at localhost:6333  (concurrent access, recommended)
    2. Local file mode (only works when NO other process has the DB open)

Start Qdrant server once with Docker:
    docker run -d --name qdrant-upsc -p 6333:6333 ^
        -v C:\\Users\\pulkitkundra\\Downloads\\pk-workspace\\upsc-agent\\vectordb\\qdrant_storage:/qdrant/storage ^
        qdrant/qdrant

Examples:
    python tools/query_books.py "Fundamental Rights Article 19" --subject "Indian Polity" --limit 5
    python tools/query_books.py "WPI base year inflation" --limit 3
    python tools/query_books.py "Vasco da Gama geographical discoveries" --subject "History"
"""

import sys, os, json, argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from dotenv import load_dotenv
load_dotenv(ROOT / ".env")

COLLECTION = "upsc_static"


def _connect_qdrant():
    """
    Try Qdrant server (localhost:6333) first, then fall back to local file mode.
    Returns (client, mode_label) or (None, None) on failure.
    """
    from qdrant_client import QdrantClient
    import warnings

    # 1. Try Docker/server mode
    try:
        client = QdrantClient(host="localhost", port=6333, timeout=3)
        client.get_collection(COLLECTION)          # ping test
        return client, "server:6333"
    except Exception:
        pass

    # 2. Fall back to local file mode (requires exclusive lock)
    db_path = ROOT / "vectordb" / "static"
    if not db_path.exists():
        _err(f"Vector DB not found at {db_path}")
        return None, None
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            client = QdrantClient(path=str(db_path))
        client.get_collection(COLLECTION)
        return client, "local-file"
    except Exception as e:
        if "already accessed" in str(e):
            _err(
                "Qdrant DB is locked by another process.\n"
                "  Fix: start Qdrant Docker server (run once):\n"
                "  docker run -d --name qdrant-upsc -p 6333:6333 "
                "-v C:\\Users\\pulkitkundra\\Downloads\\pk-workspace\\upsc-agent\\vectordb\\qdrant_storage:/qdrant/storage "
                "qdrant/qdrant"
            )
        else:
            _err(f"Could not open Qdrant DB: {e}")
        return None, None


def query_books(query: str, subject: str = "", limit: int = 4, as_json: bool = False) -> str:
    try:
        from qdrant_client import QdrantClient
    except ImportError:
        _err("qdrant-client not installed — run: pip install qdrant-client")
        return ""

    client, mode = _connect_qdrant()
    if client is None:
        return ""

    # Embed the query
    try:
        from agent.azure_auth import get_embedding_model
        embed_model = get_embedding_model()
        enriched    = f"{subject} {query}".strip() if subject else query
        vector      = embed_model.embed_query(enriched)
    except Exception as e:
        _err(f"Embedding failed: {e}")
        return ""

    # Search
    try:
        filter_condition = None
        if subject:
            from qdrant_client.models import Filter, FieldCondition, MatchValue
            filter_condition = Filter(
                must=[FieldCondition(key="subject", match=MatchValue(value=subject))]
            )
        results = client.query_points(
            collection_name = COLLECTION,
            query           = vector,
            limit           = limit,
            query_filter    = filter_condition,
            with_payload    = True,
        ).points
    except Exception as e:
        _err(f"Qdrant search failed: {e}")
        return ""

    if not results:
        return ""

    if as_json:
        data = [
            {
                "score":   round(r.score, 4),
                "source":  r.payload.get("source", ""),
                "subject": r.payload.get("subject", ""),
                "chunk":   r.payload.get("chunk_index", 0),
                "text":    r.payload.get("text", ""),
            }
            for r in results
        ]
        return json.dumps(data, ensure_ascii=False, indent=2)

    lines = [f"## Book Context [{mode}] — {len(results)} passages\n"]
    for i, r in enumerate(results, 1):
        src   = r.payload.get("source", "unknown")
        subj  = r.payload.get("subject", "")
        score = round(r.score, 3)
        text  = r.payload.get("text", "").strip()
        lines.append(f"### [{i}] {src}  |  {subj}  |  relevance: {score}")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


def _err(msg: str):
    print(f"[query_books] {msg}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--subject", "-s", default="")
    parser.add_argument("--limit",   "-n", type=int, default=4)
    parser.add_argument("--json",    "-j", action="store_true")
    args = parser.parse_args()

    result = query_books(args.query, subject=args.subject, limit=args.limit, as_json=args.json)
    if result:
        print(result)
    sys.exit(0)

