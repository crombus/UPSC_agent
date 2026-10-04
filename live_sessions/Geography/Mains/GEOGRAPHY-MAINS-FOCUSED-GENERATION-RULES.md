# Geography Mains-Focused Generation Rules

These rules supplement the repository live-session generation, validation and release rules.
The stricter rule applies where requirements overlap.

## Scope

1. Preserve every comprehensive Geography package and learning session unchanged.
2. Create a separate Mains-focused edition for each of the 37 canonical Geography topics.
3. Integrate the world/general Basic owner with its India-applied Advanced companion.
4. Size lessons dynamically from syllabus ownership, verified PYQs, causal dependencies,
   mapwork and answer-writing value.
5. Use Advanced material only where it adds analytical depth, India application or marks.
6. Retain Prelims facts only when they support mechanisms, maps or high-value traps.

## Source order

1. Canonical Basic and Advanced Markdown owners.
2. OCR-searchable or page-rendered local books.
3. Verified official current-affairs sources.
4. Qdrant only as an optional, non-blocking fallback.

Coverage packages and archived learning sessions are ordering and coverage maps, not controlling
sources.

## Lesson contract

Every lesson must include:

- a progress line and fully delimited pre-teach checklist;
- a visual-first map, derivation, causal flow, comparison or argument tree;
- plain-language intuition before technical terminology;
- the complete causal chain, assumptions and limits;
- at least one India-centric example with its limitation;
- a comparison, objection, reply and unresolved residual where applicable;
- explicit syllabus, verified PYQ, trap and answer-use guidance;
- 8-15 revision points;
- exactly one concept check, model answer and misconception note;
- one original Mains question, complete model and unique quantified rubric.

## Size and presentation

- Lesson-local 10-mark models: no more than 150 words.
- Final 15- and 20-mark models: no more than 250 words.
- Use distinct visual grammars and lesson-specific internal structures.
- Include maps, derivations and argument trees across the topic; do not rely only on tables.
- Date volatile facts and distinguish book-era data from current official figures.
- Do not infer objective answer keys that are absent from verified ledgers.

## Topic contract

- Preserve definitions, mechanisms, causal logic, map reasoning, major objections and balanced
  conclusions.
- Correct obsolete science, terminology and superseded statistics explicitly.
- Delegate legal, institutional, environmental, economic and disaster-management depth to the
  correct subject owners rather than duplicating it.
- Use only genuine, verified current linkages and disclose source-access limitations.
- Use concept-check mode; do not create a compiled four-option MCQ corpus.
- Retain the standard final eight-H1 arc required by `tools\validate_live_session.py`.
- Keep consolidated register notes as the final teaching section.
- Validate and independently review every exact hash before indexing or release.

## Output and release

- Save editions under `live_sessions\Geography\Mains\<topic-folder>\Mains-Focused-Live-Edition.md`.
- Index them only in `live_sessions\Geography\Mains\INDEX.md`.
- Never add Geography Mains rows to `live_sessions\INDEX.md`.
- Require UTF-8, LF-only line endings, balanced fences, no trailing whitespace and exactly one
  final newline.
- Release sequentially with an empty staging area and require remote parity `0/0`.
