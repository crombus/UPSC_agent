# UPSC Consolidated Transfer Index

Generated: `2026-09-22T11:17:42+05:30`

This folder is a **non-destructive navigation and transfer layer**. It contains indexes only; it does not replace, copy, approve, or alter authoritative learning assets.

## Status semantics

- **Completed-validated (resource):** the latest learner-v2 record exists, its Markdown/notes/workbook paths exist, and recorded validation state is `passed`.
- **Completed / in-progress (study):** copied only from [Study progress](<../UPSC-PROGRESS-TRACKER.md>).
- **Unverified:** no matching explicit evidence was found. It does not mean not started.
- **Unapproved:** explicit `approved: false`; generation/validation never implies learner approval.

## Snapshot

| Metric | Count |
|---|---|
| Subjects | 23 |
| Catalogue topics | 516 |
| Source-ready topics | 516 |
| Learner-v2 completed + validated | 516 |
| Explicitly approved learner-v2 topics | 0 |
| Explicitly unapproved learner-v2 topics | 516 |
| Quick-glance topics completed | 479 |
| Study completed (explicit tracker evidence) | 26 |
| Study in progress (explicit tracker evidence) | 10 |
| Study unverified/no matching topic record | 480 |

## Consolidation files

- [Subject inventory](SUBJECT-INVENTORY.csv) — one row per catalogue subject.
- [Topic inventory](TOPIC-INVENTORY.csv) — 516 source-ready topics with resource, approval, study, and authoritative paths.
- [Transfer checklist](TRANSFER-CHECKLIST.md) — safe staged copy and post-copy verification.
- [Environment setup](ENVIRONMENT-SETUP.md) — commands found in repository documentation/scripts, with secret handling.
- [Directory map](DIRECTORY-MAP.md) — authority boundaries and folder purposes.
- [Integrity manifest](INTEGRITY-MANIFEST.json) — directory size/count/mtime rollups and SHA-256 only for critical controls/scripts.

## Authoritative control/status sources

- [Repository README](<../README.md>)
- [Agent instructions](<../AGENTS.md>)
- [Saved workflow](<../AGENT_MEMORY.md>)
- [Study progress](<../UPSC-PROGRESS-TRACKER.md>)
- [Export status](<../EXPORT-PDF-STATUS.json>)
- [V2 topic catalogue](<../upsc-ai-kit/manifests/v2/topic-catalog.json>)
- [Quick-glance status](<../quick_galance/TREE-CHART-STATUS.json>)

## Transfer priorities

1. **P0 core:** `learning_package_final`, `upsc-ai-kit\knowledge`, `quick_galance`, `tools`, `ingestion`, this consolidation folder, and root control/status files.
2. **P1 state/output:** `notes`, `exams`, `attempts`. `notes` is authoritative and very large; copy it after P0 if bandwidth is constrained.
3. **P2 optional-large:** `books` and `vectordb`. Books are original source PDFs; vector data is optional for Markdown/OCR-first study but expensive to rebuild.

The optional `simple_learnning` interface was not built, indexed as authoritative, or modified in this task.

## Validation

- Overall: **PASS**
- CSV: 23 unique subjects; 516 unique topics.
- JSON: integrity manifest parsed successfully.
- Markdown local links checked: 26; missing: 0.
- Topic authoritative path fields missing: 0.
