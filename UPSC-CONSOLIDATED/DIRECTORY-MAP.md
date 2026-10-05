# Directory Map

All paths are relative to the `upsc-agent` repository root. Existing spelling is preserved; notably, `quick_galance` is authoritative and must not be renamed during transfer.

## Authoritative roots

| Path | Priority | Optional | Files | Size | Purpose |
|---|---|---|---|---|---|
| learning_package_final | P0-core | no | 1505 | 237.85 MiB | Final learning-package artifacts |
| upsc-ai-kit\knowledge | P0-core | no | 18565 | 2.14 GiB | Canonical Markdown knowledge |
| quick_galance | P0-core | no | 482 | 11.09 MiB | Quick-glance atlas and indexes |
| tools | P0-core | no | 2056 | 46.76 MiB | Generation and validation scripts |
| ingestion | P0-core | no | 24 | 11.05 MiB | Book ingestion pipeline |
| notes | P1-large | no | 66558 | 37.34 GiB | Generated notes, workbooks, flowcharts and PDFs |
| exams | P1-user-state | no | 105 | 2.75 MiB | Question papers and answer keys |
| attempts | P1-user-state | no | 128 | 77.46 MiB | User attempts and evaluation history |
| books | P2-optional-large | yes | 274 | 2.39 GiB | Source PDFs; optional only if available elsewhere |
| vectordb | P2-optional-large | yes | 850 | 6.51 GiB | Local vector data; can be omitted when Qdrant is not required |

## Knowledge and subject structure

- Canonical authored knowledge: [upsc-ai-kit/knowledge](<../upsc-ai-kit/knowledge>)
- Final package outputs: [learning_package_final](<../learning_package_final>)
- Generated notes/PDFs: [notes](<../notes>)
- Quick-glance atlas: [quick_galance](<../quick_galance>)
- Catalogue subjects (23): Ancient-Indian-History, Medieval-Indian-History, Modern-Indian-History, World-History, Indian-Art-and-Culture, Geography, Indian-Society, Polity, Governance, Social-Justice, International-Relations, Economy, Environment-and-Ecology, Science-and-Technology, Internal-Security, Disaster-Management, Ethics, Political-Theory, Essay, CSAT, Qualifying-English, Qualifying-Hindi, Philosophy
- A root-level `knowledge` directory was not found; references to “knowledge” in this consolidation mean `upsc-ai-kit\knowledge`.

## Control plane

- Catalogue: [V2 topic catalogue](<../upsc-ai-kit/manifests/v2/topic-catalog.json>)
- Export tracker: [Export status](<../EXPORT-PDF-STATUS.json>)
- Study tracker: [Study progress](<../UPSC-PROGRESS-TRACKER.md>)
- Quick-glance tracker: [Quick-glance status](<../quick_galance/TREE-CHART-STATUS.json>)
- Tooling: [tools](<../tools>) and [ingestion](<../ingestion>)

## Excluded from consolidation authority

Scratch/cache/staging folders and the existing `simple_learnning` tree are not promoted by these indexes. Their presence is not interpreted as completion or approval.
