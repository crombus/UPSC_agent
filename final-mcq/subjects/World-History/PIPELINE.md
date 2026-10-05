# World History MCQ continuation pipeline

**Queue:** Follow `subjects/World-History/INDEX.md` in catalogue order. Existing
`in_progress` topics retain their own holds; the next catalogue row explicitly marked
`pending` is the only new topic eligible for generation. Do not open or author later topics.

At the start and end of every continuation:

1. Read `AGENT_MEMORY.md`, `AGENTS.md`, `final-mcq/INSTRUCTIONS.md`, this pipeline,
   `final-mcq/INDEX.md`, the subject `INDEX.md`, and the active topic's coverage ledgers.
2. Read the complete Basic owner, Advanced owner, complete package, solved workbook/practice
   atlas and mandated OCR source before authoring.
3. Build three distinct original banks. Each bank needs answer-free `QUESTIONS.md`, a separate
   `ANSWERS.md` with the key, evidence, four option-specific rationales and traps, and its own
   `COVERAGE.md`.
4. Keep exact PYQs out unless same-paper/key provenance and reproduction permission are both
   documented. Record unresolved PYQ census and rights as explicit holds.
5. Run structural and hostile audits. Repair every actionable finding before updating the subject
   index. The pipeline is a gate, not a substitute for factual or editorial review.
6. Update the subject index only after the active topic's original banks pass clean audit, then run
   the pipeline again as the final repository action. Report the next pending topic.

The read-only helper is `python final-mcq/tools/world_pipeline.py`.
