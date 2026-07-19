# Philosophy Optional Visual Notes - AI Playbook

This file is a portable instruction set and copy-ready prompt for generating
topic-wise UPSC Philosophy Optional PDFs on any AI platform that can read local
files and run Python.

For a standalone prompt that can be pasted directly into another AI platform,
use `PHILOSOPHY_PDF_CREATION_PROMPT.md`. The mandatory content-depth standard is
defined in `PHILOSOPHY_PDF_CONTENT_AND_VISUAL_STANDARD.md`.

## 1. Objective

Create one visually attractive, revision-friendly PDF for each UPSC Philosophy
Optional syllabus topic. Every PDF must:

- remain faithful to the official UPSC syllabus;
- be grounded directly in the available local books and PYQs;
- explain arguments rather than merely list definitions;
- contain mind maps, causal flows, concept links and memory aids;
- prepare the learner for 10-mark, 15-mark and 20-mark answers;
- distinguish doctrine, criticism, comparison and evaluation;
- avoid fabricated facts, quotations, dates and source claims.

## 2. Workspace

Default project root:

```text
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent
```

Important paths:

```text
Books:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\books\philosphy_books

Official syllabus and PYQs:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\books\philosophy_optional

Existing Philosophy knowledge files:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\upsc-ai-kit\knowledge\Philosophy

PDF generator:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\tools\upsc_register_pdf.py

Final notes:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent\notes\Philosophy
```

## 3. UPSC Philosophy Structure

Organize the complete optional into four categories:

1. Western Philosophy
2. Indian Philosophy
3. Socio-Political Philosophy
4. Philosophy of Religion

Use the formal UPSC label **Socio-Political Philosophy**, not merely
"Political Philosophy."

### Indian Philosophy topic order

1. Carvaka
2. Jainism
3. Schools of Buddhism
4. Nyaya-Vaisesika
5. Samkhya
6. Yoga
7. Mimamsa
8. Schools of Vedanta
9. Sri Aurobindo

Output folder:

```text
notes\Philosophy\Indian-Philosophy\
```

Suggested filenames:

```text
01_Carvaka.pdf
02_Jainism.pdf
03_Buddhism.pdf
04_Nyaya-Vaisesika.pdf
05_Samkhya.pdf
06_Yoga.pdf
07_Mimamsa.pdf
08_Vedanta.pdf
09_Sri-Aurobindo.pdf
```

## 4. Source Rules

### Mandatory source priority

1. Official UPSC syllabus PDF.
2. Local Philosophy book PDFs.
3. Local UPSC Philosophy Optional PYQ PDFs.
4. Existing verified knowledge files in `upsc-ai-kit\knowledge\Philosophy`.
5. General model knowledge only for explanation or synthesis, clearly treated
   as analysis rather than a sourced fact.

### Local PDF rule

When the relevant PDF exists locally, analyze the PDF directly. Do not replace
direct book analysis with Qdrant or another RAG summary.

### Core Indian Philosophy sources

- C. D. Sharma, *A Critical Survey of Indian Philosophy*
- S. C. Chatterjee and D. M. Datta, *An Introduction to Indian Philosophy*
- Other available Indian Philosophy reference PDFs
- UPSC Philosophy Paper I PYQs

### Accuracy rules

- Never invent quotations.
- Avoid exact dates when the source does not establish them.
- Do not treat an opponent's description as a neutral primary account.
- Mention source limitations where original school texts are unavailable.
- Paraphrase book arguments; do not reproduce long copyrighted passages.
- Separate the school's position from later criticism.

## 5. Required Analysis Before PDF Creation

For each topic:

1. Research current educational-information-design ideas before choosing the
   layout. Look specifically for comprehension-led patterns such as argument
   maps, conceptual landscapes, comparison matrices, layered timelines,
   Socratic question chains and visual metaphors.
2. Read the exact syllabus line.
3. Identify the relevant chapters or pages in at least two core books when
   available.
4. Read all available PYQs for the topic.
5. Identify recurring UPSC demand:
   - exposition;
   - argument reconstruction;
   - criticism;
   - comparison;
   - statement evaluation;
   - application of doctrine.
6. Build a doctrine map:
   - epistemology;
   - metaphysics;
   - self or consciousness;
   - ethics or soteriology;
   - criticism;
   - inter-school comparison.
7. Check technical Sanskrit terms and transliteration.
8. Create answer frameworks before writing the final data file.
9. Select visuals only after matching each visual to a learning problem.

Do not begin PDF generation until this analysis is complete.

## 6. Visual Learning Standard

Every topic PDF must contain:

- at least one central mind map;
- at least one causal or argumentative flow diagram;
- one key-data or doctrine table;
- one concept-link table connecting other syllabus schools;
- one memory hook or mnemonic;
- one must-know-facts versus UPSC-traps panel;
- one PYQ table;
- one high-scoring answer flow.

Use visuals for genuine learning value, not decoration.

Venn diagrams are only one option. Never force a Venn diagram where a
comparison matrix, argument tree, causal chain, concept landscape or layered
timeline explains the topic better.

### Best visual for each purpose

| Learning need | Required visual |
|---|---|
| Whole doctrine | Central mind map |
| Argument sequence | Vertical flow diagram |
| School comparison | Three-column comparison table |
| Technical vocabulary | Term-meaning-exam-use table |
| Recall | Short mnemonic or memory chain |
| Answer writing | Define-Reconstruct-Apply-Debate-Evaluate flow |
| Cross-topic integration | Core concept-linked concept-exam use table |
| Multi-axis comparison | Comparison matrix |
| Claim-objection-reply | Argument or dialectic tree |
| Influence and intellectual proximity | Conceptual landscape |
| Branching philosophical inquiry | Socratic question chain |
| Abstract doctrine needing a memory anchor | Topic-specific visual metaphor |

### Non-breaking layout rules

- Never split a table, facts panel, UPSC-traps panel, memory hook, diagram,
  Mains-angle panel or Study-link panel across pages.
- If the complete block does not fit, start it on the next page.
- Never leave a heading isolated at the bottom of a page.
- Keep every diagram label within a measured node, card or bounded legend.
- Use remaining cover or opening-page space for a topic-specific explanatory
  visual, not unrelated decoration.
- Whitespace is acceptable when it improves hierarchy, but accidental gaps
  caused by broken pagination must be corrected.

## 7. Content Architecture

A strong topic PDF normally contains three or four cards:

### Card 1 - Master map

- identity and place in the syllabus;
- central thesis;
- complete doctrine mind map;
- one causal chain;
- source caution;
- memory hook;
- cross-school links.

### Card 2 - Core doctrine

- detailed explanation of the principal syllabus demand;
- technical vocabulary table;
- argument flow;
- examples and analogies;
- must-know facts;
- traps.

### Card 3 - Remaining dimensions

- metaphysics, self, ethics, liberation or other topic-specific dimensions;
- comparison with relevant Indian schools;
- criticism and defence.

### Card 4 - PYQs and answer writing

- recent PYQ routes;
- 10-mark and 15/20-mark structures;
- opponent's arguments;
- balanced evaluation;
- conclusion formula.

## 8. PDF Data Schema

The generator loads a Python module containing a top-level `DATA` dictionary.

```python
DATA = {
    "title": "Indian Philosophy: Topic Name",
    "meta": [
        "UPSC Philosophy Optional | Paper I | Indian Philosophy",
        "Visual learning edition: maps, flows, links and PYQ frameworks",
        "Syllabus: exact syllabus line",
    ],
    "topics": [
        {
            "title": "Card title",
            "relevance": "HIGH",
            "gs_paper": "Paper I",
            "subject": "Philosophy",
            "intro": "Clear doctrinal introduction.",
            "origin": "Source history or interpretive caution.",
            "timeline": [
                {"year": "Stage", "event": "Development or source event"}
            ],
            "concept_map": {
                "title": "Mind Map Title",
                "center": "CENTRAL THESIS",
                "branches": [
                    {"title": "Branch 1", "text": "Short explanation"},
                    {"title": "Branch 2", "text": "Short explanation"},
                ],
            },
            "table": {
                "headers": ["Term", "Meaning", "Exam Use"],
                "rows": [
                    ["Term 1", "Meaning", "Why UPSC may test it"]
                ],
            },
            "flow_diagram": {
                "title": "Argument Flow",
                "steps": [
                    {"title": "Step 1", "text": "Explanation"},
                    {"title": "Step 2", "text": "Explanation"},
                ],
            },
            "static_theory": [
                "**Concept:** explanation",
                "**Argument:** explanation",
            ],
            "memory_hook": "A short and meaningful recall chain.",
            "must_know_facts": [
                "Fact 1",
                "Fact 2",
            ],
            "traps": [
                {
                    "wrong": "Common incorrect claim",
                    "correct": "Accurate correction",
                }
            ],
            "link_map": {
                "title": "Concept Links",
                "headers": [
                    "Core Concept",
                    "Linked Concept",
                    "Why It Matters",
                ],
                "rows": [
                    [
                        "Topic concept",
                        "Related school or philosopher",
                        "Comparison or answer-writing value",
                    ]
                ],
            },
            "mains_angle": "One analytical judgment for the conclusion.",
            "static_link": "Syllabus and PYQ revision link.",
        }
    ],
}
```

## 9. Generator Command

From the project root:

```powershell
python tools\upsc_register_pdf.py `
  notes\Philosophy\Indian-Philosophy\NN_Topic_data.py `
  notes\Philosophy\Indian-Philosophy\NN_Topic.pdf
```

After successful generation:

```powershell
Remove-Item notes\Philosophy\Indian-Philosophy\NN_Topic_data.py
```

The temporary `_data.py` file must be deleted only after the PDF is created
successfully.

## 10. Validation

Before declaring completion, verify:

1. The PDF exists at the correct path.
2. It contains no empty pages.
3. All required headings occur in extracted PDF text.
4. Mind maps and flow diagrams fit inside page boundaries.
5. Tables do not overlap or cut text.
6. No unsupported icons appear as missing-glyph squares.
7. No table, traps panel, facts panel, callout or diagram is split across pages.
8. Every Venn or comparison visual keeps its complete text inside bounded cards.
9. Opening-page whitespace contains a relevant concept visual where useful.
7. The topic covers the exact syllabus line.
8. Relevant PYQs are represented accurately.
9. Criticism does not overwhelm exposition.
10. The temporary data file has been removed.

Recommended technical check:

```python
import fitz

doc = fitz.open("notes/Philosophy/Indian-Philosophy/NN_Topic.pdf")
text = "\n".join(page.get_text() for page in doc)

print("Pages:", len(doc))
print("Empty pages:", [
    index + 1
    for index, page in enumerate(doc)
    if len(page.get_text().strip()) < 20
])
```

Render representative pages as PNG files and visually inspect:

- cover page;
- mind-map page;
- table or comparison page;
- final PYQ and answer-writing page.

## 11. Writing Rules

- Teach visually first and explain second.
- Use short, precise paragraphs.
- Explain every technical term on first use.
- Prefer arguments and relations over encyclopedic listing.
- Use examples only when they clarify a philosophical claim.
- Avoid decorative current-affairs sections for static Philosophy topics.
- Do not add an artificial "news trigger."
- Every criticism must identify the opponent or logical basis.
- Every comparison must include both similarity and difference.
- Conclusions must make a reasoned judgment.
- Avoid reducing a school to a slogan.
- Use restrained colour and consistent visual hierarchy.

## 12. Answer-Writing Formula

Use this five-stage framework:

```text
DEFINE
  |
  v
RECONSTRUCT THE ARGUMENT
  |
  v
APPLY AN EXAMPLE
  |
  v
PRESENT THE DEBATE
  |
  v
EVALUATE AND CONCLUDE
```

Mnemonic: **D-R-A-D-E**

For 10 marks:

- 2-line introduction;
- three or four core points;
- one criticism;
- one balanced conclusion.

For 15 or 20 marks:

- define the doctrine;
- explain its internal logic;
- provide technical detail and an example;
- introduce the strongest opponent;
- offer defence or qualification;
- deliver a reasoned final assessment.

## 13. Copy-Ready Master Prompt

Copy the following prompt into another AI platform:

```text
You are an expert UPSC Philosophy Optional notes architect and a careful
research assistant.

Your task is to create one complete, topic-wise, visually learnable PDF for:

CATEGORY: <Indian Philosophy / Western Philosophy / Socio-Political Philosophy /
Philosophy of Religion>
TOPIC: <topic name>
SYLLABUS LINE: <exact UPSC syllabus line>
OUTPUT FILE: <absolute output PDF path>

PROJECT ROOT:
C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent

SOURCE LOCATIONS:
- books\philosphy_books
- books\philosophy_optional
- upsc-ai-kit\knowledge\Philosophy

PDF GENERATOR:
tools\upsc_register_pdf.py

NON-NEGOTIABLE SOURCE RULES:
1. Read the official syllabus first.
2. Analyze the relevant local PDF chapters directly. Do not substitute Qdrant
   or another RAG summary when the source PDFs are available.
3. Use at least two core books where relevant and available.
4. Read all available UPSC PYQs for the topic.
5. Use existing knowledge files only as a cross-check and synthesis aid.
6. Do not fabricate quotations, dates, doctrines, arguments or PYQ wording.
7. Paraphrase sources and avoid long copyrighted extracts.
8. If the original texts are lost or the doctrine is reconstructed through
   opponents, state that limitation.

REQUIRED PDF CONTENT:
- master doctrine map;
- central mind map;
- causal or argumentative flow diagram;
- technical-term table;
- concept-link and cross-school comparison table;
- memory hook or mnemonic;
- must-know facts;
- UPSC traps;
- strongest criticism and strongest defence;
- recent PYQ routes;
- 10-mark and 15/20-mark answer frameworks;
- balanced final evaluation.

REQUIRED LEARNING DESIGN:
- visual first, explanation second;
- short, readable blocks;
- consistent navy, blue, teal, purple, green, red and amber hierarchy;
- no decorative visuals without learning value;
- research innovative educational-information-design patterns before selecting
  visuals for the topic;
- choose the best visual for the reasoning task rather than defaulting to Venn
  diagrams;
- keep all tables, callouts, facts/traps panels and diagrams intact on one page;
- use topic-specific conceptual imagery to make useful opening-page whitespace;
- no unsupported emoji or missing-glyph squares;
- no blank pages;
- no clipped or overlapping text.

WORKFLOW:
1. Inspect the syllabus, local sources, existing knowledge file and PYQs.
2. Prepare a doctrine and PYQ coverage map.
3. Create a temporary Python data module using the DATA schema supported by
   tools\upsc_register_pdf.py.
4. Include optional visual fields:
   concept_map, flow_diagram, memory_hook and link_map.
5. Generate the PDF:
   python tools\upsc_register_pdf.py <data.py> <output.pdf>
6. Validate page count, extracted headings, empty pages and visual layout.
7. Fix any layout or content problem.
8. Delete the temporary _data.py file only after successful generation.

QUALITY STANDARD:
The notes must be suitable for repeated revision and for writing a high-quality
UPSC Philosophy Optional answer. Do not produce a generic summary. Show how the
doctrine works, why it is defended, how it is criticized, how it compares with
other schools and how UPSC frames questions around it.

At completion, report only:
- topic completed;
- page count;
- meaningful visual features;
- final PDF path.
```

## 14. Short Per-Topic Prompt

Use this after the master instructions are already loaded:

```text
Create the next Philosophy Optional visual PDF.

Category: Indian Philosophy
Topic: <TOPIC>
Syllabus: <EXACT SYLLABUS LINE>
Sequence number: <NN>

Analyze the local books directly, reconcile the doctrine with all available
PYQs, build mind maps, argument flows, concept links, mnemonics, comparisons,
criticism and answer frameworks, generate the PDF with
tools\upsc_register_pdf.py, validate it visually and technically, and delete
the temporary data module after success.

Save as:
notes\Philosophy\Indian-Philosophy\<NN>_<TOPIC>.pdf
```

## 15. Continuation Protocol

When the user says `Next`, continue to the next syllabus topic in order.

Before generating it:

- confirm the next topic from the sequence;
- inspect its local source chapters and PYQs;
- reuse the visual design system, not the previous topic's substantive content;
- create topic-specific diagrams and comparisons;
- avoid copying generic criticism across schools.

The next Indian Philosophy topic after Carvaka is **Jainism**.
