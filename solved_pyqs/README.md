# UPSC Solved PYQ Catalogue

This workspace is the released paper-wise and topic-wise solved-PYQ library for the complete
**2019–2026** corpus plus the **2013–2018 historical merit tiers**.

## Final release coverage

- **142 paper files**: 88 complete-corpus papers (2019–2026) plus fifty-four 2013–2018 historical merit papers.
- **142 paper-specific review records**, all with final release status **PASS**.
- **5,381 answerable solved questions/parts**.
- **5,565 routed stable anchors**, plus 480 preserved 2013–2018 CSAT transcription anchors and one
  preserved 2026 English source-fidelity note.
- **357 canonical topic pages** with exact paper-anchor links and no duplicated full solutions.
- **48,800 represented Mains/Philosophy marks**; attempted-paper totals remain separately stated.
- **65 hash-verified historical source records**: 54 merit question papers and 11 final Prelims
  key records; no historical qualifying-language paper is expected.
- **Idempotent generation**: a second complete generation produces zero changed paths.

## Navigation

- [Years index](catalogue/YEARS-INDEX.md)
- [Paper-wise index](catalogue/PAPERWISE-INDEX.md)
- [Subject index](catalogue/SUBJECT-INDEX.md)
- [Topic index](catalogue/TOPIC-INDEX.md)
- [Concentration analysis](catalogue/CONCENTRATION-ANALYSIS.md)
- [Answer-quality spot checks](catalogue/QUALITY-SPOT-CHECKS.md)
- [Machine-readable question metadata](catalogue/CORPUS-METADATA.json)
- [Machine-readable corpus audit](catalogue/CORPUS-AUDIT.json)
- [Coverage status](STATUS.md)
- [Review log](REVIEW-LOG.md)
- [Final release report](FINAL-RELEASE-REPORT.md)
- [Historical-expansion changed-path manifest](HISTORICAL-EXPANSION-FILE-CHANGES.txt)
- [Mains answer-writing philosophy](answer-writing-philosophy.md)
- [Answer-philosophy alignment review instructions](ANSWER-PHILOSOPHY-ALIGNMENT-INSTRUCTIONS.md)

Full solutions live only in `papers/<year>/`. Topic pages contain concentration metadata and
direct links to canonical paper answers.

## Key-provenance discipline

- 2013–2025 released Prelims keys remain official-final, including every recorded drop or
  multiple-answer outcome.
- Both repository-held 2026 keys remain explicitly **provisional**.
- 2026 Prelims GS-I Q64 remains dropped (`X`) in the provisional key.
- No provisional or independently inferred answer is promoted to official-final status.

## Definitive audit command

Run `python solved_pyqs/build_release_catalogue.py --idempotence`. The command regenerates twice,
requires the second pass to be unchanged, verifies the complete paper/review inventory, exact
counts and marks, stable anchors, canonical topic slugs, bidirectional links, all local Markdown
file/anchor targets, and the historical source-validation hashes.

## Completion rule

A paper is complete only after source, transcription, solution, evidence, classification, count,
bidirectional-link and mandatory post-pass reviews all succeed under [INSTRUCTIONS.md](INSTRUCTIONS.md).
