# Modern History MCQ continuation pipeline

**Queue:** Complete catalogue topics strictly in `INDEX.md` order. Original-bank completion and the official-PYQ census are separate tracks: a topic may have complete corroborated originals while exact PYQs, same-series keys or reproduction rights remain explicitly held.

At the start of every continuation:

1. Read `AGENT_MEMORY.md`, `final-mcq/INSTRUCTIONS.md`, this file and the active topic's root/revision coverage ledgers. Run `python final-mcq/tools/modern_pipeline.py`; obey its `NEXT` topic. If the topic is pending, read its full Basic owner, Advanced owner, complete topic package, solved workbook, practice atlas, then relevant OCR books and primary/statutory evidence before authoring.
2. Work only on the active catalogue topic. Preserve boundaries recorded by adjacent-topic owners, but do not inspect a later topic's content merely to anticipate it.
3. Each revision must independently cover the owner with original questions. Every live item requires one answer-free stem, exactly four A–D options, one separate key, a precise source/evidence line, four option-specific rationales and an examiner trap.
4. Audit exact and near-duplicate stems, repeated keyed decisions within and across revisions, duplicate/high-similarity options, answer runs/cycles, keyed-option length or qualification cues, leakage, filler, unsupported clauses/dates/personnel and owner leakage. A mechanical one-to-one mapping is necessary but never sufficient for release.
5. Do not force disputed facts into a key. Record the hold, avoid relying on it in live items and cover the owner through other reliable decisions. Do not invent personnel rosters, statutory wording or PYQ keys.
6. Exact official PYQs require an authenticated same-series official paper, its matching final scoring key and documented reproduction permission. Otherwise keep exact wording outside the live banks and use clearly original concept routes.
7. Mark original banks complete only when all three revisions have zero actionable source, coverage, duplicate, option-quality, leakage and boundary findings. Keep independent historical/PYQ holds explicit in the ledgers and index; they do not become resolved merely because original banks are released.

The pipeline is read-only. It reports the first catalogue topic not indexed `complete` and, where a linked bank exists, checks only structural mapping. It cannot certify factual accuracy, editorial difficulty, source sufficiency, PYQ provenance or reproduction rights.
