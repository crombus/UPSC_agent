# International Relations final-MCQ continuation pipeline

**Queue:** Follow `upsc-ai-kit/manifests/v2/topic-catalog.json` in catalogue order. Complete
exactly one topic per continuation; do not open a later topic while the active topic has
unresolved release work.

At the start and end of each continuation:

1. Read `AGENT_MEMORY.md`, `AGENTS.md`, `final-mcq/INSTRUCTIONS.md`, this pipeline,
   `MCQ-COMPLIANCE-INSTRUCTIONS.md`, both IR indexes, and the active topic ledgers.
2. Read the complete Basic and Advanced owners, the master framework, relevant practice
   material, and authoritative local/OCR sources before authoring.
3. Require three independent banks with answer-free questions, detailed separate answers,
   and revision-level coverage ledgers.
4. Keep exact PYQs out unless same-paper/key provenance and reproduction permission are
   documented. Preserve explicit holds for unresolved census, key, and rights questions.
5. Run structural, option-balance, answer-leakage, cross-revision distinctness, and hostile
   source/status audits. Repair every actionable finding.
6. Update the IR subject index only after all three banks pass clean audit, then run:
   `python final-mcq/tools/international_relations_pipeline.py`
   as the final repository action.

The pipeline is a release gate, not a substitute for substantive source review.
