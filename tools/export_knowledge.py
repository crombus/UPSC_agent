"""
Export the Qdrant `upsc_static` collection into portable, structured knowledge files
(Markdown + JSON), organised by Subject -> Book. NO Azure / embeddings needed — pure
payload scroll. The resulting files can be fed directly to Gemini / Claude / ChatGPT as
context, or compiled to PDF.

Usage:
    python tools/export_knowledge.py                 # export everything
    python tools/export_knowledge.py --only "Laxmikant"   # sources whose name contains substring
    python tools/export_knowledge.py --subject "Indian Polity"
    python tools/export_knowledge.py --list          # just list sources, no export

Output:
    knowledge-export/
        _catalog.md / _catalog.json      -> index of everything
        <Subject>/<BookName>.md          -> full reassembled text
        <Subject>/<BookName>.json        -> metadata + full text + chunk list
"""

import sys, os, json, argparse, re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
OUT  = ROOT / "knowledge-export"
COLLECTION = "upsc_static"

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass


def connect():
    from qdrant_client import QdrantClient
    # server first (complete data), then static file backup
    try:
        c = QdrantClient(host="localhost", port=6333, timeout=30)
        c.get_collection(COLLECTION)
        return c, "server:6333"
    except Exception:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            c = QdrantClient(path=str(ROOT / "vectordb" / "static"))
        c.get_collection(COLLECTION)
        return c, "local-file"


def safe_name(s: str) -> str:
    s = re.sub(r"\.pdf$|\.epub$", "", s, flags=re.I)
    s = re.sub(r"[^\w\s\-\.]", "_", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:150]


def append_dedup(acc: str, nxt: str, max_overlap: int = 500) -> str:
    """Concatenate nxt onto acc, removing the overlapping region produced by the chunker."""
    if not acc:
        return nxt
    m = min(len(acc), len(nxt), max_overlap)
    for k in range(m, 25, -1):
        if acc[-k:] == nxt[:k]:
            return acc + nxt[k:]
    return acc + "\n" + nxt


def fetch_all(client):
    """Return {source: {'subject','book_title','total_chunks','chunks':[(idx,text)]}}"""
    books = defaultdict(lambda: {"subject": "", "book_title": "", "total_chunks": 0, "chunks": []})
    off = None
    while True:
        batch, off = client.scroll(COLLECTION, limit=3000, with_payload=True,
                                   with_vectors=False, offset=off)
        for p in batch:
            pl = p.payload
            src = pl.get("source", "?")
            b = books[src]
            b["subject"] = pl.get("subject", "")
            b["book_title"] = pl.get("book_title", "")
            b["total_chunks"] = pl.get("total_chunks", 0)
            b["chunks"].append((pl.get("chunk_index", 0), pl.get("text", "")))
        if off is None:
            break
    return books


def reassemble(chunks):
    chunks = sorted(chunks, key=lambda x: x[0])
    acc = ""
    for _, t in chunks:
        acc = append_dedup(acc, t)
    return acc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="substring filter on source filename")
    ap.add_argument("--subject", default="", help="exact subject filter")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    client, mode = connect()
    print(f"[export] connected [{mode}]  — fetching payloads ...")
    books = fetch_all(client)
    print(f"[export] {len(books)} sources fetched")

    catalog = []
    OUT.mkdir(exist_ok=True)
    exported = 0
    for src in sorted(books):
        b = books[src]
        if args.only and args.only.lower() not in src.lower():
            continue
        if args.subject and b["subject"] != args.subject:
            continue

        subject = b["subject"] or "Uncategorised"
        text = reassemble(b["chunks"])
        entry = {
            "source": src,
            "book_title": b["book_title"],
            "subject": subject,
            "chunks_stored": len(b["chunks"]),
            "total_chunks": b["total_chunks"],
            "char_count": len(text),
        }
        catalog.append(entry)

        if args.list:
            print(f"  [{subject:22}] {len(b['chunks']):6d} chunks  {len(text):9d} chars  {src}")
            continue

        subdir = OUT / safe_name(subject)
        subdir.mkdir(parents=True, exist_ok=True)
        base = safe_name(src)

        md = subdir / f"{base}.md"
        md.write_text(
            f"# {b['book_title'] or base}\n\n"
            f"**Subject:** {subject}  \n"
            f"**Source file:** {src}  \n"
            f"**Chunks:** {len(b['chunks'])}  |  **Characters:** {len(text):,}\n\n"
            f"> Exported from Qdrant `upsc_static` — reassembled in document order, overlap-deduped.\n\n"
            f"---\n\n{text}\n",
            encoding="utf-8",
        )
        js = subdir / f"{base}.json"
        js.write_text(json.dumps({**entry, "text": text}, ensure_ascii=False, indent=2),
                      encoding="utf-8")
        exported += 1
        print(f"  wrote {subject}/{base}  ({len(text):,} chars)")

    # catalog
    catalog.sort(key=lambda e: (e["subject"], e["source"]))
    (OUT / "_catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Knowledge Export Catalog\n",
             f"Total sources: {len(catalog)}  |  Exported this run: {exported}\n",
             "| Subject | Chunks | Chars | Source |", "|---|---:|---:|---|"]
    by_sub = defaultdict(int)
    for e in catalog:
        by_sub[e["subject"]] += e["char_count"]
        lines.append(f"| {e['subject']} | {e['chunks_stored']} | {e['char_count']:,} | {e['source']} |")
    lines.append("\n## Totals by subject\n")
    lines.append("| Subject | Total chars |\n|---|---:|")
    for s in sorted(by_sub):
        lines.append(f"| {s} | {by_sub[s]:,} |")
    (OUT / "_catalog.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[export] catalog written -> {OUT/'_catalog.md'}")
    print(f"[export] done. exported={exported}")


if __name__ == "__main__":
    main()
