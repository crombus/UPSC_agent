# Philosophy Optional 01–03 Flow Learning Report

- Status: **PASSED**
- Topic folders: **3**
- Subject/topic counts: **Philosophy Optional: 3**
- Subject page totals: **Philosophy Optional: 30**
- Flow PDFs / TXTs / READMEs: **3 / 3 / 3**
- Total Flow PDF pages: **30**
- Source/output PDF hashes equal: **True**
- Source/output TXT hashes equal: **True**
- Combined exported PDF/TXT hash-list SHA-256: `74dc71aca74f6fc5d282d9fc65bc97a2e84bdbf00604f7f69ffb5a741d3406cf`
- Navigation links checked: **31**, broken: **0**
- Tracker SHA-256: `ff35ece772d0d396e55dac1498d6f4cb9de9961ae69b98212e1615d82fbba541` — unchanged: **True**
- Topic catalogue SHA-256: `325123df1911cd00ed885cf242af965a153119b3ac76ab0fd68352bc25ec7c07` — unchanged: **True**
- Final-Learning-Packages aggregate SHA-256: `ef646f84fd25cfea8835a434c135f4ff72c501a2e503585b67b2892881669cd4` — unchanged: **True**
- Exact latest validated learner-v2 inventory: **True**
- Derived / expected topic count: **3 / not fixed**; difference: **None**
- Polity case-year compliance: **True**
- Other-subject date/year retention: **True**

## Inventory and metadata resolution

- Inventory is derived dynamically from the highest-generation passed `learner-v2` tracker record for each topic key.
- Each tracker identity must map to exactly one Final-Learning-Packages folder with the same source record ID and generation.
- If an exact catalogue entry is absent, metadata is accepted only from the clean-package README plus its numbered subject/section/folder location; titles are not guessed from topic keys.
- Catalogue-fallback topics: None

## Navigation rule

Start with Flow Learning for first understanding and rapid revision. Use the Complete Learning Session only for deeper explanation/evidence. Use the Solved Workbook for practice. Flow Learning does not replace or reduce the full reference.

## Per-topic validation

| Subject | Section | # | Topic | Record / generation | Panels | Pages | PDF SHA-256 | TXT SHA-256 | Case years | Date/year retention | Master | PDF layout | Status |
|---|---|---:|---|---|---:|---:|---|---|---|---|---|---|---|
| Philosophy Optional | Philosophy Paper I — Western Philosophy | 01 | Plato and Aristotle | `philosophy-paper-i-western-philosophy-01:learner-v2:g2` / g2 | 10 | 10 | `a2af4709a6590ad2f6a886e4748e270dca7f8d6ef5aa38c5123e38bb5e3401af` | `0cb66be33bb23f945bc05c87737b3eb89bb794bc599a088d6bdae6a6219e7082` | PASS (0) | PASSED | PASSED | PASSED | PASSED |
| Philosophy Optional | Philosophy Paper I — Western Philosophy | 02 | Rationalism | `philosophy-paper-i-western-philosophy-02:learner-v2:g2` / g2 | 10 | 10 | `32cd433e6f0115d3178398b2294a32283a86216ac697717dd2e1efdc77c92083` | `25bfee2a7ca6a1517d50386f51796e4a58dd9c96edff4cf827de93c7c5dccc81` | PASS (0) | PASSED | PASSED | PASSED | PASSED |
| Philosophy Optional | Philosophy Paper I — Western Philosophy | 03 | Empiricism | `philosophy-paper-i-western-philosophy-03:learner-v2:g2` / g2 | 10 | 10 | `aa9c39a9651639ad71a78bfb15edff73d8a883bcbd8da06f2c0acb1431f99926` | `ad21be42d0bbbbae98ee57400f4810a50ebffef1c911d3533e45868ce00e7fbe` | PASS (0) | PASSED | PASSED | PASSED | PASSED |

## PDF evidence

- Every exported PDF was opened and compared with its matching TXT through the existing ASCII PDF validator.
- Blank, clipped and replacement-glyph page lists are empty for every topic.
- Current repaired-source evidence was reused from `upsc-ai-kit\manifests\exports\polity-flowchart-case-year-repair-2026-08-24-validation.json`, including contact-sheet/preview review.

## Tests

- Command: `python -m unittest tools.test_v2_export_foundation tools.test_carvaka_flowchart plus 6 isolated export tests`
- Tests passed: **40**
- Status: **PASSED**

## Exceptions

- None.
