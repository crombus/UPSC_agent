# Older PYQ Routing Index, 2018–2023

> **Scope:** These ledgers remain the controlling routing/provenance records.
> Their rows have now been propagated into the destination owner files as
> generated PYQ-demand sections. Prelims and CSAT keys for 2018–2023 are not
> held locally and are never inferred.

## Integration status

- **Unique printed questions:** 1,560
- **Question-to-owner assignments:** 2,190
- **Owner files updated:** 409
- **Missing route targets:** 0
- **Subject/topic residual audit:**
  [`PYQ-INTEGRATION-AUDIT-2018-2023.md`](PYQ-INTEGRATION-AUDIT-2018-2023.md)
- **Reproducible propagator:** `../tools/propagate_historical_pyqs.py`

## Question-level routing

| Paper | Coverage | Ledger |
|---|---:|---|
| Prelims GS-I | 2018–2023 | [Question routing](./_PYQ-ROUTING-PRELIMS-2018-2023.md) |
| CSAT | 2018–2023 | [Six-family routing](./_PYQ-ROUTING-CSAT-2018-2023.md) |
| Mains GS-I, GS-II and Essay | 2018–2023 | [Question routing](./_PYQ-ROUTING-MAINS-GS1-GS2-ESSAY-2018-2023.md) |
| Mains GS-III and GS-IV | 2018–2023 | [Question routing](./_PYQ-ROUTING-MAINS-GS3-GS4-2018-2023.md) |

## Direct-source exports

- Searchable page text: `attempts/_pyq_text/`
- Prelims Markdown/JSON: `knowledge-export/Prelims PYQ/`
- CSAT Markdown/JSON: `knowledge-export/CSAT PYQ/`
- Mains Markdown/JSON: `knowledge-export/Mains PYQ/`
- Export provenance catalog: `knowledge-export/_catalog.md`
- Reproducible exporter: `tools/integrate_previous_papers.py`

The direct-source exports were produced from
`books/more_previous_papers/`; Qdrant was not used.
