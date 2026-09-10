# UPSC Answer-Writing Toolkit

This folder contains a portable answer-writing and evaluation system that can
be used with ChatGPT, Gemini, GitHub Copilot, or another AI model capable of
reading documents and handwritten-answer images. It does not depend on Agency.

## Included files

| File | Purpose |
|---|---|
| `ANSWER-EVALUATION-PROMPT.md` | Reusable instructions for strict, source-grounded UPSC evaluation |
| `ANSWER-WRITING-TRACKER.csv` | Excel-compatible progress tracker |

## Material to use

The repository separates factual knowledge, teaching and practice:

| Location | Purpose |
|---|---|
| `upsc-ai-kit\knowledge\` | Core and advanced subject knowledge |
| `learning_package_final\<Subject>\...\Learning-Session.md` | Verified teaching sequence |
| `learning_package_final\<Subject>\...\Solved-Practice-Workbook.md` | Questions and model solutions |
| `notes\Final-Learning-Packages\` | Final PDFs, diagrams and revision material |
| `attempts\` | Private working area for handwritten answers |

## Standard workflow

1. Select a question from a solved-practice workbook or question paper.
2. Write the answer by hand under timed conditions.
3. Scan or photograph every answer page clearly.
4. Upload the question, answer images, relevant knowledge or Learning Session
   file, and model solution to the chosen AI platform.
5. Copy the prompt from `ANSWER-EVALUATION-PROMPT.md`.
6. Review the transcription before accepting the evaluation.
7. Enter the returned tracker row in `ANSWER-WRITING-TRACKER.csv`.
8. Rewrite weak answers without looking at the model answer.
9. Record the rewrite score and schedule the next revision.

## Recommended time limits

| Question | Word limit | Initial practice target |
|---|---:|---:|
| 10 marks | 150 words | 7 minutes |
| 15 marks | 250 words | 11 minutes |
| 20 marks | 250 words | 14 minutes |

Use the exact limit printed on the question paper when it differs from this
practice table.

## Using ChatGPT or Gemini

Create a separate project or notebook for each subject. Upload only the
question and relevant topic files instead of the entire knowledge library.

For each evaluation, provide:

1. Question and maximum marks.
2. Handwritten answer image or PDF.
3. Relevant knowledge or Learning Session file.
4. Solved Practice Workbook or model solution, if available.
5. The portable evaluation prompt.

## Using GitHub Copilot CLI

Start Copilot from the repository:

```powershell
Set-Location C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent
copilot
```

Attach known files with `@`, or ask Copilot to locate the corresponding topic
under `learning_package_final` and `upsc-ai-kit\knowledge`.

Example:

```text
Evaluate my attached handwritten answer using
@upsc-ai-kit\answer-writing\ANSWER-EVALUATION-PROMPT.md and the relevant
Learning Session and Solved Practice Workbook. Do not use unsupported facts.
```

## Scoring system

Every answer is standardised to 100:

| Dimension | Weight |
|---|---:|
| Content accuracy and demand fulfilment | 50 |
| Structure and presentation | 20 |
| Analysis, balance and multidimensionality | 15 |
| Evidence, examples and current-affairs application | 15 |

Calculations:

```text
Total_100 = Content_50 + Structure_20 + Analysis_15 + Evidence_15
UPSC_Marks = Total_100 * Marks_Max / 100
```

AI marks are estimates, not official UPSC marks. Use the same prompt and,
where possible, the same model so that trends remain comparable.

## Measuring progress

The primary indicator is the rolling average of the latest 10 timed answers.
Do not judge progress from one unusually high or low score.

| Indicator | Personal readiness benchmark |
|---|---:|
| Latest 10-answer average | At least 55/100 |
| Directive correctly addressed | At least 90% |
| Answers completed within time | At least 80% |
| Improvement after rewrite | At least 10 points |
| Recurring weakness tags | Declining each month |

A topic is provisionally ready when:

1. Two timed first attempts score at least 55/100.
2. A rewrite scores at least 65/100.
3. The directive and word limit are satisfied.
4. No major factual error or `KNOWLEDGE_GAP` remains.

## Weakness tags

Use consistent tags to make monthly analysis possible:

```text
KNOWLEDGE_GAP
DEMAND_MISREAD
WEAK_INTRO
WEAK_CONCLUSION
POOR_STRUCTURE
LOW_ANALYSIS
NO_BALANCE
FEW_EXAMPLES
FACTUAL_ERROR
NO_CA_LINK
WORD_LIMIT
TIME_OVERRUN
PRESENTATION
```

At the end of each month, count each tag. The three most frequent tags become
the next month's priority drills.

## Recommended weekly cycle

| Day | Work |
|---|---|
| Monday-Friday | One timed answer each day |
| Saturday | Three-answer sectional test |
| Sunday | Rewrite the two weakest answers |
| Every fourth week | Full GS or Optional test and tracker review |

## File organisation

Recommended attempt folder:

```text
attempts\YYYY-MM-DD_<TestName>\
```

Recommended image name:

```text
YYYY-MM-DD_Paper_Subject_Topic_Q01_Page01.jpg
```

Move evaluated attempts to:

```text
attempts\done\
```

The `attempts` directory is intentionally excluded from Git because it can
contain private handwritten work. Keep a separate encrypted or private backup
if those scans must be retained when changing computers.

## Monthly review

Record:

1. Number of timed answers and rewrites.
2. Latest 10-answer average.
3. Subject-wise average.
4. Time-compliance and directive-compliance percentages.
5. Three most frequent weakness tags.
6. Best improvement after rewrite.
7. Topics requiring renewed study from the Learning Session.

Progress should mean better timed performance and fewer recurring weaknesses,
not merely a larger number of completed answers.
