# Solved PYQ Execution Queue

## Queue status

**Complete — no release batch is pending.**

| Batch | Scope | State |
|---:|---|---|
| 1 | All eleven 2026 papers | **Complete — release PASS** |
| 2 | All eleven 2025 papers | **Complete — release PASS** |
| 3 | All eleven 2024 papers | **Complete — release PASS** |
| 4 | All eleven 2023 papers | **Complete — release PASS** |
| 5 | All eleven 2022 papers | **Complete — release PASS** |
| 6 | All eleven 2021 papers | **Complete — release PASS** |
| 7 | All eleven 2020 papers | **Complete — release PASS** |
| 8 | All eleven 2019 papers | **Complete — release PASS** |
| 9 | 2018 historical merit tier: nine papers, excluding Hindi/English | **Complete — release PASS** |
| 10 | 2017 historical merit tier: nine papers, excluding Hindi/English | **Complete — release PASS** |
| 11 | 2016 historical merit tier: nine papers, excluding Hindi/English | **Complete — release PASS** |
| 12 | 2015 historical merit tier: nine papers, excluding Hindi/English | **Complete — release PASS** |
| 13 | 2014 historical merit tier: nine papers, excluding Hindi/English | **Complete — release PASS** |
| 14 | 2013 historical merit tier: nine papers, excluding Hindi/English | **Complete — release PASS** |
| 15 | Whole-catalogue concentration and final integrity audit | **Complete — PASS** |

## Final release gates

| Gate | Result |
|---|:---:|
| 142 paper files and 142 review records | **PASS** |
| 5,381 answerable units and 5,565 routed anchors | **PASS** |
| 357 canonical topics with exact reverse links | **PASS** |
| Paper-, year-, subject- and topic-index rebuild | **PASS** |
| Complete concentration analysis from question metadata | **PASS** |
| Key-provenance and dropped/multiple-answer preservation | **PASS** |
| 142 year × family answer-quality spot checks | **PASS** |
| Relative Markdown links and explicit anchors | **PASS** |
| Historical source slots and SHA-256 hashes | **PASS — 65/65** |
| Generator idempotence | **PASS — second pass unchanged** |
| Duplicate-solution, orphan-link and residue scans | **PASS** |
| Mandatory post-pass review | **PASS** |

## Maintenance mode

Future work is maintenance only: correct a defect when supported by source evidence, then rerun
`python solved_pyqs/build_release_catalogue.py --generate` and the mandatory post-pass review.
Never promote the 2026 provisional keys without an authenticated official-final source.
