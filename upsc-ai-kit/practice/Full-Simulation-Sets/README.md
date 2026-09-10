# Full UPSC Simulation Sets

Four deterministic simulation sets cover Prelims GS-I, CSAT, Essay, Mains GS-I-IV, and Philosophy Optional Papers I-II. Question papers contain no keys or hints; every paper has a separate detailed answer-key PDF.

**Current-affairs cutoff:** 2026-09-10. No later event is used.

## Difficulty standard

- **Overall:** Above typical recent UPSC difficulty, while fair, syllabus-relevant and unambiguous.
- **Prelims:** Multi-statement elimination, close conceptual distinctions, cross-subject integration, map/institution/application reasoning and balanced plausible distractors; no niche fact dumping.
- **CSAT:** Moderately harder than the recent qualifying level through dense passages, time pressure and multi-step reasoning; every item remains uniquely solvable without gratuitous calculation.
- **Mains:** Synthesis, critique, competing viewpoints, constitutional/institutional or evidence-based analysis, qualification and current-static integration.
- **Philosophy:** Textual and doctrinal precision, argument reconstruction, objections and strongest replies, and comparisons across thinkers or schools.

## Regeneration

From the repository root run:

```powershell
python tools\build_full_upsc_simulations.py --all
```

The script reads tracked `learning_package_final` workbooks for static Prelims items, uses checked deterministic CSAT generation, writes four JSON and Markdown source editions, renders all PDFs, and recreates the manifest and validation reports.

Current claims are admitted only from repository-verified source records or directly retrieved official PIB/MEA/RBI/ministry/constitutional sources. Generic web-search summaries are not source evidence; when official retrieval is blocked or thin, the sets use static-current conceptual linkage instead of asserting an unsupported event.

Static Prelims provenance is also gated: Polity, Economy and Ancient History reuse only workbook questions having four explicit option explanations that agree with the key; Art and Culture uses the independently accepted general-explanation banks with regenerated option-specific reasons; all other GS categories use original deterministic questions built from exact facts and misconception-correction pairs in `upsc-ai-kit\knowledge\<Subject>\basic`.

Descriptive papers are source-grounded rather than directive-substitution templates. GS-I, GS-II and GS-III each use 80 distinct questions across the four sets. GS-IV uses quotation, application and case-study formats. Philosophy answers follow mark-sensitive depth bands. Validation rejects identical topic sequences, near-duplicate question wording, repeated long sentences and any 12-word answer n-gram occurring in more than six independently identified answers.

## Structure

- `Set-01.json` ... `Set-04.json`: authoritative structured sources.
- `Set-01.md` ... `Set-04.md`: human-readable reusable editions with solutions.
- `curated-prelims-bank.json`: reusable source-grounded original bank for categories whose workbook keys are not admitted.
- `curated-descriptive-bank.json`: GS, Ethics, Essay and Philosophy source data used to rebuild the descriptive papers.
- `descriptive-sample-review.json` and `DESCRIPTIVE-SAMPLE-REVIEW.md`: recorded review of three samples from every descriptive paper in every set.
- `manifest.json`: output inventory, counts, hashes and cutoff.
- `validation-report.json`: machine-readable structural and PDF checks.
- `VALIDATION.md`: human summary.

Model answers and essay frameworks are practice simulations, not official UPSC answers.
