# UPSC Agent Repository Instructions

`AGENT_MEMORY.md` is the repository's authoritative saved workflow. Read and follow it before
teaching, generating exams, or creating PDFs. If another instruction conflicts with it, use the
newer rule in `AGENT_MEMORY.md`.

## Complete Topic Package

Triggers:

- `Create Topic Package: <Subject> — <Topic>`
- `Export PDF` for the current topic/session

For either trigger:

1. Use sources in this order: Markdown knowledge files, OCR-searchable PDFs, live current
   affairs, then Qdrant only as an optional fallback.
2. Build the complete multi-subtopic learning session even if it was not previously taught
   interactively.
3. Create a detailed main PDF containing all teaching, innovative diagrams, terminology,
   examples, criticisms/replies, advanced refinements, solved PYQs, MCQ/remedial loops, and
   solved Mains practice.
4. End the main PDF with complete consolidated register notes covering every subtopic.
5. Create a separate workbook with all relevant solved PYQs, MCQs covering nearly every
   subtopic, remedial MCQs, and original 10/15/20-mark Mains questions with model solutions.
6. Rotate MCQ keys strictly A → B → C → D.
7. Save a cleaned reusable Markdown edition in the relevant
   `upsc-ai-kit\knowledge\<Subject>\` area.
8. Validate coverage, layout, glyphs, answers, rotation, and final register-note placement.
9. Record all three deliverable paths in `EXPORT-PDF-STATUS.json`, regenerate
   `EXPORT-PDF-COMMAND-INDEX.md`, and mark `approved: true` only after explicit user approval.

Do not apply the quick `Notes` rule that excludes MCQs to a complete topic package or
`Export PDF`.
