# UPSC Agent

An AI-powered UPSC mentor — visual-first, current-affairs-linked, ruthlessly rigorous.

> 📌 **Agent rules & saved preferences live in [`AGENT_MEMORY.md`](./AGENT_MEMORY.md)** — the portable
> single source of truth for exam format, Qdrant/ingestion workflows, CA analysis rules, and verified
> facts. It is updated every time the user says "save".

## Quick Start

### 1. Setup
```bash
cp .env.example .env
# Fill in your Azure Foundry endpoint + API key in .env
```

### 2. Ingest your books (one-time)
```bash
cd ingestion
pip install -r requirements.txt
python ingest.py "C:\path\to\your\upsc-pdfs"
```

### 3. Run the agent
```bash
# CLI (interactive)
python cli.py

# With subject/topic directly
python cli.py --subject Polity --topic "Constitutional Bodies"

# As API server
python cli.py --serve --port 8080

# Full stack (all services)
docker compose up
```

## Navigation Commands
| Command | Action |
|---|---|
| `Start` | Begin first subtopic |
| `Next` | Move to next subtopic |
| `Repeat` | Repeat current subtopic |
| `Deeper` | Dive deeper into current concept |
| `Diagram` | Show visual/diagram |
| `MCQs` | Generate MCQ practice |
| `PYQ` | Show previous year questions |
| `CA-Daily: <date>` | Current affairs for a date |
| `Progress` | Show your progress tracker |
| `Export PDF` | Export full session notes |

## Architecture
```
Static DB (books)  ──┐
                     ├──► RAG Engine ──► LLM ──► Teaching Output
Dynamic DB (news)  ──┘
```

## Configuration
Edit `config.yaml` to set model provider, sources, teaching style.
