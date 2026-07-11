"""
UPSC Agent — The Hindu Newspaper Analyser
=========================================
Reads PDF(s) from newspapers/the-hindu/, extracts full text, and performs
a structured UPSC CA analysis using the Azure chat model.

FOLDER STRUCTURE:
  newspapers/the-hindu/          ← drop new PDFs here
  newspapers/the-hindu/done/     ← processed PDFs moved here automatically
  newspapers/the-hindu/analysed/ ← raw extracted text saved here for reference

WORKFLOW (run once after dropping a PDF):
  python tools/analyze_hindu.py
  python tools/analyze_hindu.py --file "TheHindu_2026-06-12.pdf"
  python tools/analyze_hindu.py --date 2026-06-12
  python tools/analyze_hindu.py --no-move   (keep PDF in inbox after analysis)
  python tools/analyze_hindu.py --save-notes (also generate register PDF)

OUTPUT:
  1. Master List (HIGH / MEDIUM / LOW relevance table)
  2. Deep analysis per item (interactive: type Item N / Next / All)
  3. Optionally: Register-style PDF via upsc_register_pdf.py

ANALYSIS FORMAT per item:
  ✅ FACTS | 📘 FULL FORMS | ⚠️ STATIC CONCEPT | 🔁 DIMENSION SHIFT
  🎯 PRELIMS TRAP | 📝 MAINS THEME | ❓ PROBABLE QUESTION
  📚 STATIC TEACHING LINK | 🔻 UPSC RELEVANCE
  + MCQ Loop (2-3 MCQs anti-bias A→B→C→D)
  + Register Notes (inline structured notes)
"""

import os
import sys
import re
import json
import argparse
import shutil
from pathlib import Path
from datetime import datetime

# Fix Windows console Unicode
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
load_dotenv(ROOT / ".env")

INBOX   = ROOT / "newspapers" / "the-hindu"
DONE    = INBOX / "done"
ARCHIVE = INBOX / "analysed"

# ── Dependency check ──────────────────────────────────────────────────────────

def _check_deps():
    missing = []
    try:
        import fitz  # noqa: F401
    except ImportError:
        missing.append("PyMuPDF (pip install pymupdf)")
    if missing:
        print("❌ Missing dependencies:")
        for m in missing:
            print(f"   pip install {m}")
        sys.exit(1)

# ── PDF extraction ────────────────────────────────────────────────────────────

def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF using PyMuPDF."""
    import fitz
    doc = fitz.open(str(pdf_path))
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text("text")
        if text.strip():
            pages.append(f"[Page {i+1}]\n{text.strip()}")
    doc.close()
    return "\n\n".join(pages)


def chunk_text(text: str, max_chars: int = 12000) -> list[str]:
    """Split text into chunks that fit within model context."""
    chunks = []
    while len(text) > max_chars:
        split_at = text.rfind("\n", 0, max_chars)
        if split_at == -1:
            split_at = max_chars
        chunks.append(text[:split_at])
        text = text[split_at:]
    if text.strip():
        chunks.append(text)
    return chunks

# ── LLM helpers ──────────────────────────────────────────────────────────────

def get_llm():
    from agent.azure_auth import get_chat_model
    return get_chat_model(temperature=0.1, max_tokens=8192)


MASTER_LIST_PROMPT = """You are an expert UPSC CA analyst. Analyse the following text extracted from The Hindu newspaper.

Extract ALL news items that are relevant for UPSC Civil Services Examination (Prelims + Mains GS1/GS2/GS3/GS4 + Optional).

For each item output a JSON array with objects:
{{
  "id": <integer>,
  "headline": "<short 5-10 word headline>",
  "gs_paper": "<GS1/GS2/GS3/GS4/Prelims/CSAT>",
  "relevance": "<HIGH/MEDIUM/LOW>",
  "topic_tags": ["<tag1>", "<tag2>"],
  "one_liner": "<one sentence summary>",
  "full_article_snippet": "<2-3 key sentences from the article>"
}}

Relevance criteria:
- HIGH: Direct exam question possible, multi-dimensional GS linkage, scheme/policy/constitutional/international significance
- MEDIUM: Factual or thematic value, may appear as supporting context
- LOW: General awareness, unlikely direct question but worth noting

Newspaper text:
{text}

Return ONLY valid JSON array, nothing else.
"""

DEEP_ANALYSIS_PROMPT = """You are a senior UPSC faculty member. Give a FULL deep-dive analysis of this news item in the exact format below.

NEWS ITEM:
Headline: {headline}
Article snippet: {snippet}
GS Paper: {gs_paper}

Follow this EXACT format (all sections mandatory, use emojis exactly as shown):

🔹 {headline}

✅ FACTS (only from the article):
  - Key actors/institutions:
  - Date/timeline:
  - Key provisions/features (numbered list):
  - Numerical data (if any):

📘 FULL FORMS:
  (List every abbreviation used in the analysis with its full form. This section is MANDATORY even if there is only one abbreviation.)

🏛️ FOUNDING / ESTABLISHMENT:
  - Year created/established:
  - Created by / under which Act / authority:
  - Original mandate vs current role (if evolved):

⚠️ STATIC CONCEPT LINKED:
  - Base constitutional / governance / IR / economy / geography concept:
  - Relevant articles / provisions / chapters:

🔁 DIMENSION SHIFT TABLE:
  | GS Paper | Angle |
  |----------|-------|
  | GS-I     | ...   |
  | GS-II    | ...   |
  | GS-III   | ...   |
  | GS-IV    | ...   |

❌ WHAT UPSC WILL NOT ASK:
  - (irrelevant decorative facts to skip)

🎯 PRELIMS TRAP:
  - Close-option logic and framing pitfalls (2-3 traps):

📝 MAINS THEME:
  - One-line analytical angle for essay / GS answer:

❓ PROBABLE QUESTIONS:
  Prelims: <one MCQ-style question>
  Mains 10-mark: <directive word + question + "150 words">
  Mains 20-mark: <directive word + question + "250 words">

📚 STATIC TEACHING LINK:
  - Subject: <subject>
  - Chapter/Topic: <chapter>
  - Study command: Start <Subject> <Topic>

🔻 UPSC RELEVANCE: HIGH / MEDIUM / LOW

════════════════════════════════════════

📝 REGISTER NOTES:
Title: {headline}
GS Paper: {gs_paper}
Key Facts: (5-7 bullet points)
Timeline: (year → event)
Must-Know Numbers: (if any)
UPSC Traps: (2-3 wrong → correct pairs)
Mains Angle: (one line)
Static Link: (Subject → Chapter → Concept)

════════════════════════════════════════

❓ MCQ LOOP (2 MCQs — anti-bias: alternate correct options, never consecutive same letter):

Q1. <stem>
A) ...
B) ...
C) ...
D) ...
[Correct: X | Explanation: ...]

Q2. <stem>
A) ...
B) ...
C) ...
D) ...
[Correct: X | Explanation: ...]
"""

# ── Core analysis flow ────────────────────────────────────────────────────────

def extract_master_list(llm, text: str, pdf_name: str) -> list[dict]:
    """Run master list extraction over text chunks, merge results."""
    from langchain_core.messages import HumanMessage, SystemMessage

    # Use large chunks (60k chars) — GPT-5.x supports 128k+ context
    chunks = chunk_text(text, max_chars=60000)
    all_items = []
    seen_headlines = set()

    print(f"\n📄 Extracting from {len(chunks)} chunk(s)...")

    for i, chunk in enumerate(chunks, 1):
        print(f"   Chunk {i}/{len(chunks)} — analysing...", end=" ", flush=True)
        prompt = MASTER_LIST_PROMPT.format(text=chunk)
        msgs = [
            SystemMessage(content="You are a UPSC CA expert. Output ONLY valid JSON arrays."),
            HumanMessage(content=prompt)
        ]
        try:
            resp = llm.invoke(msgs)
            raw = resp.content.strip()
            # Strip markdown code fences if present
            raw = re.sub(r"^```(?:json)?\s*", "", raw)
            raw = re.sub(r"\s*```$", "", raw)
            items = json.loads(raw)
            new_items = 0
            for item in items:
                hl = item.get("headline", "").strip().lower()
                if hl and hl not in seen_headlines:
                    seen_headlines.add(hl)
                    item["id"] = len(all_items) + 1
                    all_items.append(item)
                    new_items += 1
            print(f"{new_items} items found")
        except Exception as e:
            print(f"⚠️ Error: {e}")

    return all_items


def print_master_list(items: list[dict], pdf_name: str, pub_date: str):
    """Print the prioritised master list table."""
    high   = [i for i in items if i.get("relevance") == "HIGH"]
    medium = [i for i in items if i.get("relevance") == "MEDIUM"]
    low    = [i for i in items if i.get("relevance") == "LOW"]

    print("\n" + "="*72)
    print(f"  📋 THE HINDU CA ANALYSIS — {pub_date}")
    print(f"  Source: {pdf_name}")
    print("="*72)

    def _table(section_items, icon):
        if not section_items:
            return
        for it in section_items:
            tags = ", ".join(it.get("topic_tags", []))
            print(f"  {icon} [{it['id']:>2}] {it['headline']}")
            print(f"        {it.get('gs_paper','?')} | {tags}")
            print(f"        {it.get('one_liner','')}")
            print()

    print(f"\n🔴 HIGH UPSC RELEVANCE ({len(high)} items)")
    print("  " + "-"*68)
    _table(high, "🔴")

    print(f"🟡 MEDIUM UPSC RELEVANCE ({len(medium)} items)")
    print("  " + "-"*68)
    _table(medium, "🟡")

    print(f"🟢 LOWER RELEVANCE ({len(low)} items)")
    print("  " + "-"*68)
    _table(low, "🟢")

    print("="*72)
    print(f"  Total: {len(items)} exam-relevant items extracted")
    print("="*72)
    print("\n💡 Commands: Item <N>  |  Next  |  Top5  |  GS2 only  |  All  |  Quit\n")


def do_deep_analysis(llm, item: dict):
    """Run and print deep analysis for one item."""
    from langchain_core.messages import HumanMessage, SystemMessage

    print(f"\n{'='*72}")
    print(f"  🔍 Deep Analysis — Item {item['id']}: {item['headline']}")
    print(f"{'='*72}\n")

    prompt = DEEP_ANALYSIS_PROMPT.format(
        headline=item.get("headline", ""),
        snippet=item.get("full_article_snippet", item.get("one_liner", "")),
        gs_paper=item.get("gs_paper", ""),
    )
    msgs = [
        SystemMessage(content=(
            "You are a senior UPSC faculty member. Follow the exact analysis format. "
            "All sections are mandatory. Every abbreviation MUST appear in FULL FORMS section."
        )),
        HumanMessage(content=prompt)
    ]
    try:
        resp = llm.invoke(msgs)
        print(resp.content)
    except Exception as e:
        print(f"❌ Analysis failed: {e}")

    print(f"\n{'─'*72}")
    print("  Next item? Type  Next  |  Item <N>  |  All  |  Quit")
    print(f"{'─'*72}\n")

# ── Interactive session loop ──────────────────────────────────────────────────

def interactive_loop(llm, items: list[dict]):
    """Allow user to pick items for deep analysis interactively."""
    idx = 0  # pointer for Next

    while True:
        try:
            cmd = input(">> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Session ended.")
            break

        if not cmd:
            continue

        cmd_lower = cmd.lower()

        if cmd_lower in ("quit", "exit", "q"):
            print("👋 Session ended.")
            break

        elif cmd_lower == "next":
            if idx < len(items):
                do_deep_analysis(llm, items[idx])
                idx += 1
            else:
                print("✅ All items covered.")

        elif cmd_lower == "top5":
            high = [i for i in items if i.get("relevance") == "HIGH"][:5]
            for it in high:
                do_deep_analysis(llm, it)

        elif cmd_lower.startswith("gs"):
            filter_gs = cmd.upper()
            matched = [i for i in items if filter_gs in i.get("gs_paper", "").upper()]
            if not matched:
                print(f"No items tagged {filter_gs}")
            else:
                print(f"  {len(matched)} items for {filter_gs}")
                for it in matched:
                    print(f"  [{it['id']}] {it['headline']}")

        elif cmd_lower == "all":
            for it in items:
                do_deep_analysis(llm, it)
            print("✅ All items analysed.")
            break

        elif cmd_lower.startswith("item "):
            try:
                n = int(cmd_lower.split()[1])
                matched = [i for i in items if i["id"] == n]
                if matched:
                    do_deep_analysis(llm, matched[0])
                    idx = n  # update pointer
                else:
                    print(f"❌ Item {n} not found.")
            except (IndexError, ValueError):
                print("Usage: Item <number>")

        elif cmd_lower == "list":
            print_master_list(items, "", "")

        else:
            print("❓ Unknown command. Try: Item <N> | Next | Top5 | GS2 | All | Quit")

# ── Main entry ────────────────────────────────────────────────────────────────

def find_pdf(args) -> Path | None:
    """Resolve which PDF to analyse."""
    if args.file:
        p = INBOX / args.file
        if not p.exists():
            p = Path(args.file)
        if not p.exists():
            print(f"❌ File not found: {args.file}")
            return None
        return p

    if args.date:
        # Try common naming patterns
        candidates = [
            INBOX / f"TheHindu_{args.date}.pdf",
            INBOX / f"the-hindu-{args.date}.pdf",
            INBOX / f"Hindu_{args.date}.pdf",
        ]
        for c in candidates:
            if c.exists():
                return c
        # Fall back to listing
        pdfs = sorted(INBOX.glob("*.pdf"))
        for pdf in pdfs:
            if args.date in pdf.name:
                return pdf
        print(f"❌ No PDF found for date {args.date}")
        return None

    # Auto-pick latest PDF in inbox
    pdfs = sorted(INBOX.glob("*.pdf"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not pdfs:
        print(f"\n❌ No PDFs found in: {INBOX}")
        print(f"   Drop The Hindu PDF(s) into that folder and run again.")
        return None

    print(f"📰 Auto-selected: {pdfs[0].name}")
    return pdfs[0]


def infer_date(pdf_path: Path) -> str:
    """Try to extract a date from filename, else use today."""
    name = pdf_path.stem
    match = re.search(r"(\d{4}[-_]\d{1,2}[-_]\d{1,2})", name)
    if match:
        return match.group(1).replace("_", "-")
    match = re.search(r"(\d{1,2}[-_]\d{1,2}[-_]\d{4})", name)
    if match:
        parts = re.split(r"[-_]", match.group(1))
        return f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
    return datetime.now().strftime("%Y-%m-%d")


def main():
    parser = argparse.ArgumentParser(description="Analyse The Hindu newspaper for UPSC")
    parser.add_argument("--file",       help="Specific PDF filename (in newspapers/the-hindu/)")
    parser.add_argument("--date",       help="Date string to match (e.g. 2026-06-12)")
    parser.add_argument("--no-move",    action="store_true", help="Keep PDF in inbox after analysis")
    parser.add_argument("--save-notes", action="store_true", help="Generate register PDF notes")
    parser.add_argument("--list-only",  action="store_true", help="Print master list only, skip deep dive")
    args = parser.parse_args()

    _check_deps()

    pdf_path = find_pdf(args)
    if pdf_path is None:
        sys.exit(1)

    pub_date = infer_date(pdf_path)

    print(f"\n📰 THE HINDU ANALYSER — UPSC Edition")
    print(f"   File    : {pdf_path.name}")
    print(f"   Date    : {pub_date}")
    print(f"   Started : {datetime.now().strftime('%H:%M:%S')}")
    print("─" * 60)

    # 1. Extract text
    print("\n📑 Extracting text from PDF...", flush=True)
    text = extract_text_from_pdf(pdf_path)
    print(f"   Extracted {len(text):,} characters from {pdf_path.name}")

    # 2. Save raw text for reference
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    archive_txt = ARCHIVE / f"{pdf_path.stem}_extracted.txt"
    archive_txt.write_text(text, encoding="utf-8")
    print(f"   Raw text saved: {archive_txt.name}")

    # 3. Load LLM
    print("\n🤖 Loading AI model...", flush=True)
    llm = get_llm()

    # 4. Master list
    items = extract_master_list(llm, text, pdf_path.name)

    if not items:
        print("\n⚠️ No UPSC-relevant items extracted. Check the PDF quality.")
        sys.exit(1)

    print_master_list(items, pdf_path.name, pub_date)

    # 5. Move PDF to done/ unless --no-move
    if not args.no_move:
        dest = DONE / pdf_path.name
        shutil.move(str(pdf_path), str(dest))
        print(f"✅ PDF moved to: newspapers/the-hindu/done/{pdf_path.name}")

    # 6. Interactive loop (skip if --list-only)
    if not args.list_only:
        interactive_loop(llm, items)

    # 7. Optional notes PDF
    if args.save_notes:
        print("\n📄 Generating register notes PDF... (feature: run Notes command in CA session)")
        print("   Tip: After analysis, use the Notes command in a CA session to generate PDF.")

    print(f"\n🎯 Analysis complete — {pub_date}")


if __name__ == "__main__":
    main()
