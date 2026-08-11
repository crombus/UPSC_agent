# PYQ Routing Index

> **Scope:** These ledgers are the controlling routing/provenance records for UPSC PYQs.
> Their rows are propagated into destination owner files as *separate* generated
> PYQ-demand sections - a `2018-2023` block, a `2024-2025` block and a `2026` block - which
> never overwrite each other. No Prelims/CSAT answer letter is ever recorded or inferred in
> any ledger.

---

## A. Older cycle: 2018-2023

- **Unique printed questions:** 1,560
- **Question-to-owner assignments:** 2,247
- **Owner files updated:** 419
- **Missing route targets:** 0
- **Key status:** Prelims/CSAT 2018-2023 keys are **not held locally** and are never inferred.
- **Subject/topic residual audit:**
  [`PYQ-INTEGRATION-AUDIT-2018-2023.md`](PYQ-INTEGRATION-AUDIT-2018-2023.md)
- **Reproducible propagator:** `../tools/propagate_historical_pyqs.py`

### Question-level routing (2018-2023)

| Paper | Coverage | Ledger |
|---|---:|---|
| Prelims GS-I | 2018-2023 | [Question routing](./_PYQ-ROUTING-PRELIMS-2018-2023.md) |
| CSAT | 2018-2023 | [Six-family routing](./_PYQ-ROUTING-CSAT-2018-2023.md) |
| Mains GS-I, GS-II and Essay | 2018-2023 | [Question routing](./_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md) |
| Mains GS-III and GS-IV | 2018-2023 | [Question routing](./_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md) |

### Unique questions by paper (2018-2023)

| Paper | Questions |
|---|---:|
| Prelims GS-I | 600 |
| CSAT | 480 |
| Mains GS-I | 120 |
| Mains GS-II | 120 |
| Mains GS-III | 120 |
| Mains GS-IV | 72 |
| Essay | 48 |
| **Total** | **1,560** |

---

## B. Recent cycle: 2024-2025

- **Unique printed questions:** 520
- **Question-to-owner assignments:** 547
- **Owner files updated:** 206
- **Missing route targets:** 0
- **OCR/manual-verification flags:** 0 questions (every 2024-2025 Prelims row was verified
  against the official Set-A scans page-by-page; year/number/wording and every route are
  confirmed, so no row carries a residual OCR-uncertainty warning)
- **Key status:** The official **2024 and 2025 Prelims Set-A keys are present locally**
  (`../../knowledge-export/Prelims PYQ/Ans-2024-GS1`, `Ans-2025-GS1`), and CSAT Set-A keys
  are supplied; even so, **no answer letter is recorded or inferred** in these ledgers.
- **Subject/topic residual audit:**
  [`PYQ-INTEGRATION-AUDIT-2024-2025.md`](PYQ-INTEGRATION-AUDIT-2024-2025.md)
- **Reproducible builder + propagator:** `../tools/build_recent_pyq_ledgers.py`,
  `../tools/propagate_recent_pyqs.py`

### Question-level routing (2024-2025)

| Paper | Coverage | Ledger |
|---|---:|---|
| Prelims GS-I | 2024-2025 | [Question routing](./_PYQ-ROUTING-PRELIMS-2024-2025.md) |
| CSAT | 2024-2025 | [Six-family routing](./_PYQ-ROUTING-CSAT-2024-2025.md) |
| Mains GS-I, GS-II and Essay | 2024-2025 | [Question routing](./_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2024-2025.md) |
| Mains GS-III and GS-IV | 2024-2025 | [Question routing](./_PYQ-ROUTING-MAINS-GS3-GS4-2024-2025.md) |

### Unique questions by paper (2024-2025)

| Paper | Questions |
|---|---:|
| Prelims GS-I | 200 |
| CSAT | 160 |
| Mains GS-I | 40 |
| Mains GS-II | 40 |
| Mains GS-III | 40 |
| Mains GS-IV | 24 |
| Essay | 16 |
| **Total** | **520** |

---

## C. Current cycle: 2026

- **Unique printed questions:** 180
- **Question-to-owner assignments:** 180
- **Owner files updated:** 82
- **Missing route targets:** 0
- **OCR/manual-verification flags:** 0 questions (every 2026 Prelims GS-I row was read from
  the official Set-A scan English text layer and visually verified against the English page
  images; year/number/wording and every route are confirmed, so no row carries a residual
  OCR-uncertainty warning)
- **Core-owner gaps:** 4 Prelims questions (Q50 Deep Ocean Mission, Q81 Nobel-laureate
  identification, Q82 Grand Slam governance, Q85 cinema/BAFTA) have no dedicated Core owner;
  each is routed to the closest existing Core owner and recorded explicitly in the audit,
  never hidden behind the loosely related route.
- **Key status:** The official **2026 Prelims and CSAT Set-A keys held locally are
  provisional** (`../../knowledge-export/Prelims PYQ/Ans-2026-GS1-Provisional`,
  `../../knowledge-export/CSAT PYQ/Ans-2026-CSAT-GS2-Provisional`); **no answer letter is
  recorded or inferred** in these ledgers.
- **Subject/topic residual audit:**
  [`PYQ-INTEGRATION-AUDIT-2026.md`](PYQ-INTEGRATION-AUDIT-2026.md)
- **Reproducible builder + propagator:** `../tools/build_2026_pyq_ledgers.py`,
  `../tools/propagate_2026_pyqs.py`

### Question-level routing (2026)

| Paper | Coverage | Ledger |
|---|---:|---|
| Prelims GS-I | 2026 | [Question routing](./_PYQ-ROUTING-PRELIMS-2026.md) |
| CSAT | 2026 | [Six-family routing](./_PYQ-ROUTING-CSAT-2026.md) |

### Unique questions by paper (2026)

| Paper | Questions |
|---|---:|
| Prelims GS-I | 100 |
| CSAT | 80 |
| **Total** | **180** |

---

## Combined totals

| Cycle | Unique questions | Owner-route assignments | Owner files updated |
|---|---:|---:|---:|
| 2018-2023 | 1,560 | 2,247 | 419 |
| 2024-2025 | 520 | 547 | 206 |
| 2026 | 180 | 180 | 82 |
| **All cycles (2018-2026)** | **2,260** | **2,974** | - |

> Owner-file counts are not additive because many owners carry a 2018-2023, a 2024-2025
> and/or a 2026 generated block.

---

## Direct-source exports

- Prelims Markdown/JSON: `knowledge-export/Prelims PYQ/`
- CSAT Markdown/JSON: `knowledge-export/CSAT PYQ/`
- Mains Markdown/JSON: `knowledge-export/Mains PYQ/`
- Export provenance catalog: `knowledge-export/_catalog.md`

The 2024-2025 routing was derived directly from these local exports; Qdrant was not used.
CSAT 2024-2025 family classification is read verbatim from the audited
[`CSAT/00_Question-Audit-Ledger`](CSAT/00_Question-Audit-Ledger.md).

The 2026 Prelims GS-I routing was read from the official 2026 GS-I Set-A scan (English text
layer, column-reconstructed and visually verified against the English page images); the 2026
CSAT family classification is read verbatim from the same audited
[`CSAT/00_Question-Audit-Ledger`](CSAT/00_Question-Audit-Ledger.md) (2026 section). The 2026
Prelims and CSAT keys held locally are provisional and are never inferred.
