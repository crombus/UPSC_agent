# Geography final-MCQ continuation pipeline

**Queue:** Follow the Geography source catalogue in
`upsc-ai-kit/manifests/v2/topic-catalog.json` in catalogue order. Complete exactly one
topic per continuation. Do not open or author a later Geography topic while the active
topic has unresolved release work.

At the start and end of every continuation:

1. Read `AGENT_MEMORY.md`, `AGENTS.md`, `final-mcq/INSTRUCTIONS.md`, this pipeline,
   `final-mcq/INDEX.md`, the Geography `INDEX.md`, and the active topic's coverage ledgers.
2. Read the active topic's complete Basic owner, Advanced owner, learner package, solved
   workbook, practice atlas and mandated local OCR/PDF sources before authoring or auditing.
3. Build three independent original banks. Each bank requires answer-free `QUESTIONS.md`,
   a separate `ANSWERS.md` with the key, evidence, four option-specific rationales and
   examiner traps, and its own `COVERAGE.md`.
4. Keep exact PYQs out unless same-paper/key provenance and reproduction permission are both
   documented. Record unresolved PYQ census, provenance and rights as explicit holds.
5. Run structural and hostile audits. Repair every actionable finding before updating the
   subject index; the pipeline is a gate, not a substitute for source or editorial review.
6. Update the Geography index only after the active topic's original banks pass clean audit,
   then run `python final-mcq/tools/geography_pipeline.py` as the final repository action.
   Report the exact completed title/counts and the next pending catalogue topic.

The read-only helper is `python final-mcq/tools/geography_pipeline.py`.
