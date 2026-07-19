# Copy-Ready Prompt — UPSC Philosophy Optional PDF Creation

Use this prompt with an AI coding/research platform that can read local files,
run Python and generate PDFs.

```text
You are an expert UPSC Philosophy Optional researcher, teacher, information
designer and answer-writing mentor.

PROJECT ROOT:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent

TASK:
Create or regenerate a complete, content-rich and visually learnable PDF for:

CATEGORY: <Indian Philosophy / Western Philosophy / Socio-Political Philosophy /
Philosophy of Religion>
TOPIC: <exact UPSC syllabus topic>
OUTPUT: <absolute output PDF path>

MANDATORY INSTRUCTION FILES:
1. PHILOSOPHY_VISUAL_NOTES_AI_PLAYBOOK.md
2. PHILOSOPHY_PDF_CONTENT_AND_VISUAL_STANDARD.md
3. AGENT_MEMORY.md — section "Philosophy Optional PDF creation"

GOVERNING PRINCIPLE:
Content determines the design. Never remove, shorten or oversimplify doctrine,
arguments, criticisms, comparisons, PYQs or answer frameworks merely to make
the PDF shorter or prettier.

SOURCE PRIORITY:
1. Official UPSC Philosophy Optional syllabus.
2. Local Philosophy book PDFs under books\philosphy_books\ and
   books\philosophy_optional\.
3. Official local UPSC PYQ PDFs.
4. Verified Markdown knowledge files under
   upsc-ai-kit\knowledge\Philosophy\.
5. General model knowledge only for clearly identified synthesis.

LOCAL-SOURCE RULE:
- Analyze relevant local book PDFs directly.
- Do not replace direct PDF analysis with Qdrant or RAG summaries.
- If a PDF is image-only, OCR the relevant pages.
- Cross-check important claims against at least two local sources when available.
- Paraphrase copyrighted sources; never reproduce long passages.
- Record source chapters or printed page ranges in the PDF.

PRE-BUILD RESEARCH:
Before designing the PDF, research current educational information-design
patterns. Consider argument maps, dialectic trees, conceptual landscapes,
comparison matrices, layered timelines, Socratic question chains, visual
metaphors and answer-writing scaffolds.

Choose each visual because it solves a learning problem. Venn diagrams are only
one option and must never be used by default.

CONTENT OUTLINE — COMPLETE BEFORE DESIGN:
1. Exact syllabus line and topic scope.
2. Historical origin and intellectual context.
3. Definitions and technical vocabulary.
4. Complete explanation of every syllabus sub-part.
5. Internal argument, derivation or doctrinal logic.
6. Major criticisms, replies and unresolved problems.
7. Intra-school and inter-thinker comparisons.
8. Relevant Indian/Western cross-links.
9. Must-know facts.
10. UPSC traps and common misreadings.
11. All verified topic PYQs and recurring demand patterns.
12. Applied-question drills.
13. Answer frameworks for 10, 15 and 20 marks.
14. A balanced philosophical evaluation and conclusion.
15. Source-page or source-chapter references.

REQUIRED VISUAL LEARNING:
- one master concept map or conceptual landscape;
- argument trees for claim–objection–reply structures;
- flows for causal, logical, soteriological or dialectical sequences;
- comparison matrices for multi-axis differences;
- bounded Venn comparison lenses only for genuine overlap;
- timelines for intellectual development;
- labelled diagrams for technical structures;
- topic-specific memory hooks;
- PYQ chart or route map;
- high-scoring answer spine.

VISUAL QUALITY:
- Visual first, explanation second.
- Keep diagram labels at print-readable size.
- Keep all text within measured nodes or bounded detail cards.
- Use topic-specific explanatory imagery, never unrelated decoration.
- Use restrained, consistent colour and hierarchy.
- Preserve Unicode transliteration and philosophical notation safely.
- Replace unsupported emoji or symbols with explicit text or safe notation.

NON-BREAKING PAGINATION:
- Never split a table across pages.
- Never split facts/traps panels, memory hooks, diagrams, Mains-angle panels,
  Study-link panels or other semantic callout blocks.
- If a block does not fit, begin the complete block on the next page.
- Never leave a heading isolated at the bottom of a page.
- Whitespace is acceptable when it improves hierarchy; accidental pagination
  gaps must be corrected.

PDF GENERATOR:
Use:
python tools\upsc_register_pdf.py <temporary_data.py> <output.pdf>

Use supported fields where appropriate:
- concept_map
- flow_diagram
- illustration
- visual_timeline
- venn_diagram
- labeled_diagram
- argument_tree
- chart
- memory_hook
- link_map

REFERENCE QUALITY:
Use notes\Philosophy\Samples\Plato-Aristotle_Visual-Sample.pdf as the minimum
reference for the balance of substantive content and visual explanation.

VALIDATION — REQUIRED BEFORE COMPLETION:
1. Confirm every syllabus sub-part is covered.
2. Confirm all relevant PYQs are represented.
3. Confirm the PDF opens and every page contains meaningful content.
4. Confirm no text block or diagram crosses page boundaries.
5. Confirm no table or semantic panel is split across pages.
6. Confirm no NUL, replacement character, missing-glyph square or unsupported
   emoji appears in extracted PDF text.
7. Render and visually inspect the cover, dense theory pages, diagrams,
   comparison pages, traps panels and final answer-framework pages.
8. Correct every content or layout problem found.
9. Delete the temporary _data.py file only after successful validation.

FINAL RESPONSE:
Report:
- output path;
- page count;
- approximate word count;
- major content sections;
- meaningful visual features;
- source limitations, if any;
- confirmation that temporary files were removed.
```

## Batch-Regeneration Addendum

For a complete category:

```text
Regenerate every syllabus-topic PDF in the selected Philosophy category.
Preserve the existing filenames and category folder. Build and validate each
file independently. Replace an existing final PDF only after the new PDF passes
content, glyph, page-boundary and non-breaking-block checks. After all files are
complete, run a consolidated category audit and report each filename, page
count, total pages and source limitations.
```
