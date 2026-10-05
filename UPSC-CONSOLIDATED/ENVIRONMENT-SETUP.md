# Environment Setup

## Secret policy

- Do **not** transfer `.env` through this index or commit it.
- Transfer `.env.example`, then create a fresh `.env` on the destination laptop and enter credentials locally.
- No credential values are present in this consolidation layer.

## Commands already documented in the repository

From [Repository README](<../README.md>):

```text
cp .env.example .env
cd ingestion
pip install -r requirements.txt
python ingest.py "C:\path\to\your\upsc-pdfs"
python cli.py
python cli.py --subject Polity --topic "Constitutional Bodies"
python cli.py --serve --port 8080
docker compose up
```

From [Saved workflow](<../AGENT_MEMORY.md>):

```text
python tools/query_books.py "<topic>" --subject "<Subject>" --limit 5
```

## Windows destination setup

```powershell
Set-Location '<TRANSFER_ROOT>\upsc-agent'
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r ingestion\requirements.txt
Copy-Item .env.example .env
# Edit .env locally; never paste secrets into transfer logs.
```

## Optional OCR and vector features

- OCR fallback in `ingestion\ingest.py` searches for Tesseract under `C:\Program Files\Tesseract-OCR` or on `PATH`.
- Current ingestion/query scripts use Qdrant; `tools\query_books.py` first tries `localhost:6333`, then local file mode.
- `docker-compose.yml` currently defines Chroma services, while current ingestion/query scripts reference Qdrant. Treat this as a configuration difference to verify, not as evidence that either service is running.
- Markdown + OCR PDFs remain usable without `vectordb`; Qdrant is optional for learning sessions.

## Smoke tests after dependencies are installed

```powershell
python -c "import json,csv,yaml; print('core imports ok')"
python tools\query_books.py "Fundamental Rights Article 19" --subject "Indian Polity" --limit 1
python cli.py --help
```

A failed vector query does not invalidate the transferred Markdown/notes corpus; verify it separately only if `vectordb` was copied.
