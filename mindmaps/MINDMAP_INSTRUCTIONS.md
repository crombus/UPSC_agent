# 📐 Mindmap Generation Instructions & Blueprint

This document defines the authoritative standard, structural architecture, visual grammar, and content requirements for generating high-yield, examiner-grade **UPSC Philosophy Mindmaps** in Markdown format.

---

## 1. Core Principles

1. **Examiner-Grade Density over Fluff**
   - No generic summaries or superficial lists.
   - Every node must contain concrete examinable content: exact Sanskrit/IAST terms, doctrines, causal mechanisms, debate pivots, and evidence.
2. **English-First Terminology Standard**
   - Always lead with the clear English concept, followed by the accurate Sanskrit/Pali IAST term in parentheses/gloss.
   - *Example:* `dependent origination (pratītyasamutpāda)`, `body-self identity (dehātmavāda)`.
3. **Epistemology Drives Metaphysics**
   - In Indian philosophy, ontological commitments directly stem from accepted means of knowledge (*pramāṇa*). Every mindmap must trace this causal chain clearly.
4. **Visual Diversity & Terminal/Render Compatibility**
   - Use clean, standard Mermaid syntax (`mindmap`, `flowchart TD`, `flowchart LR`).
   - Quote labels with special characters to prevent rendering syntax errors.
   - Complement diagrams with comparative markdown tables, alert callouts, and quote blocks.

---

## 2. Standard 15-Section Architecture

Every topic mindmap created in the `mindmaps/` directory must follow this comprehensive modular blueprint:

```
mindmaps/
  ├── <Topic>_Mindmap.md
  └── MINDMAP_INSTRUCTIONS.md
```

### Module Breakdown:

| # | Module Name | Primary Format | Key Requirements |
|---|-------------|----------------|------------------|
| **0** | **Master Overview** | Mermaid `mindmap` | Root node branching into all major thematic pillars (Identity, Epistemology, Metaphysics, Causation, Ethics, Debates). |
| **1** | **Identity, Lineage & Doxography** | Mermaid `flowchart TD` + Text | Canonical names, orthodox (*āstika*) vs unorthodox (*nāstika*) classification, founder traditions, lost/extant primary sources, opponent doxographies. |
| **2** | **Theory of Knowledge (Epistemology)** | Mermaid `flowchart` + Step Tables | Accepted *pramāṇas* (*pratyakṣa*, *anumāna*, *śabda* etc.), internal vs external perception, critique of rival pramāṇas, invariable concomitance (*vyāpti*), hidden conditions (*upādhi*), self-refutation analysis. |
| **3** | **Dialectical Wings & Sceptical Refinements** | Mermaid `flowchart TD` | Radical/critical branches (e.g., Jayarāśi Bhaṭṭa's *Tattvopaplavasiṃha*, Madhyamaka *prasaṅga*, subtle vs crude schools). |
| **4** | **Metaphysics & Ontology** | Mermaid `flowchart LR` & `TD` | Admitted elements/substances (*bhūtas*, *dravyas*), excluded elements (e.g. *ākāśa* rejection), theory of self (*dehātmavāda*, *anātman*, or *ātman*), consciousness mechanism (*bhūta-caitanya*, emergence analogies). |
| **5** | **Rejection / Affirmation of Transcendent Realities** | Mermaid `flowchart TD` | Stand on *karma*, *saṃsāra* (rebirth), *adṛṣṭa*, *Īśvara* (creator God), *mokṣa* (liberation), and Vedic authority. |
| **6** | **Explanatory & Causal Principles** | Mermaid `flowchart LR` | Naturalism (*svabhāvavāda*), chance (*yadṛcchāvāda*), *satkāryavāda*, *asatkāryavāda*, or *pratītyasamutpāda*. Differentiate natural order from chance. |
| **7** | **Ethics & Human Goals (Puruṣārthas)** | Mermaid `flowchart TD` | Hierarchy of *kāma*, *artha*, *dharma*, *mokṣa*. Differentiate crude hedonism/fatalism from refined/prudential formulations. |
| **8** | **Inter-School Comparative Matrices** | Markdown Table + Flowcharts | Comprehensive multi-axis matrix (Pramāṇas, Self, Consciousness, Karma, Causation, Release) contrasting with Nyāya, Buddhism, Jainism, Advaita, Sāṃkhya. |
| **9** | **Criticisms & Reconstructed Replies** | Mermaid `flowchart TD` | The top 4–5 philosophical objections (e.g. self-refutation, induction collapse, ethical nihilism) paired with school replies and objective critical assessment. |
| **10** | **Controlled Western Comparisons** | Comparison Table + Guardrail Callout | Parallels (Hume, Ayer, Epicurus, Kant, Spinoza, Pyrrho) strictly accompanied by decisive disanalogies. Alert warning against false equivalences. |
| **11** | **Diagnostic Deep-Dives for High-Frequency Themes** | Flowchart / Structured Analysis | Dedicated breakdown for recurring complex exam questions (e.g. Positivism question, Syllogistic validity vs warrant, Ākāśa & Transmigration pairing). |
| **12** | **PYQ Routing Ledger (Recent 8–10 Years)** | Markdown Table | All verified UPSC Mains question parts with year, question number, marks (10/15/20), and exact core demand. |
| **13** | **Top 10 UPSC Exam Traps** | Mermaid `flowchart TD` | 10 high-frequency traps and misconceptions examiners use to penalize superficial answers. |
| **14** | **Technical Vocabulary & IAST Bank** | Markdown Table | Key philosophical terms with accurate IAST transliteration, English gloss, and doctrinal status (✅ canonical, ⚠️ analytical, ❓ contested). |
| **15** | **Graded Verdict & Answer Architectures** | Mermaid `flowchart LR` + Carousel/Cards | Strong, Weak, and Contested axes. Ready 10-mark, 15-mark, and 20-mark structural templates with exact examiner-winning anchor sentences. |

---

## 3. Mermaid Diagram Syntax Standards

To ensure Mermaid diagrams render cleanly in all editors, Markdown viewers, and PDF converters:

1. **Mindmap Syntax:**
   ```mermaid
   mindmap
     root((TOPIC))
       BRANCH 1
         Sub-branch A
         Sub-branch B
       BRANCH 2
         Sub-branch C
   ```
2. **Flowcharts:**
   - Always use standard directions: `flowchart TD` (top-down) or `flowchart LR` (left-to-right).
   - Enclose node text containing spaces, punctuation, quotes, or HTML tags inside double quotes:
     ```mermaid
     flowchart TD
       NodeA["Concept: Label (IAST)"] --> NodeB["Detailed Mechanism"]
     ```
   - Avoid unsupported shapes or non-standard diagram types (stick to `mindmap`, `flowchart TD`, `flowchart LR`).

---

## 4. Markdown Formatting & Typography Rules

- **Alerts:** Use standard GitHub-style blockquotes strategically:
  - `> [!IMPORTANT]` for syllabus placement and core theses.
  - `> [!WARNING]` for critical traps and fatal exam mistakes.
  - `> [!TIP]` for mnemonic bridges and high-yield scoring hooks.
  - `> [!NOTE]` for contextual nuances or textual controversies.
- **Evidence Keys:**
  - ✅ **Canonical doctrine:** securely established in primary/doxographical consensus.
  - ⚠️ **Analytical synthesis:** rational reconstruction or interpretive framework.
  - ❓ **Contested / uncertain:** disputed textual attribution or hostile doxographical exaggeration.
- **Answer Architecture Quotes:** Include exact verbatim quotes or concluding lines suitable for scoring full marks in 10, 15, and 20-mark questions.

---

## 5. Step-by-Step Generation Workflow

When instructed to generate a mindmap for a given syllabus item:

1. **Source Discovery:**
   - Locate the canonical topic owner in `upsc-ai-kit/knowledge/Philosophy/`.
   - Inspect primary coverage, pūrvapakṣa-siddhānta ledgers, presupposition tables, and recent PYQs.
2. **Extract Key Axes:**
   - Epistemic root (*pramāṇa*).
   - Metaphysical inventory (what is real vs unreal).
   - Causal mechanism.
   - Human condition & ethics.
   - Opponents' attacks & self-defense.
3. **Build Complete Document:**
   - Apply all 15 modules without truncating or taking shortcuts.
   - Save directly into `mindmaps/<Topic_Name>_Mindmap.md`.
4. **Git Sync & Audit:**
   - Verify file syntax and links.
   - Commit and push to repository as requested.
