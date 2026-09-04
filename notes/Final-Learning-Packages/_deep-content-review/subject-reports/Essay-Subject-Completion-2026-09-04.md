# Essay Subject Completion — Deep Review

## Distinct Essay structure

Essay deliberately does not use the ordinary GS learning-session/MCQ architecture. Each topic has three primary artifacts:

1. indexed complete Knowledge Guide;
2. indexed question-only Practice Workbook;
3. separate indexed Practice Solutions.

A workflow-atlas PNG and matching ASCII workflow are integrated learning aids. In the final library they are published under `04-Integrated-Workflow-Atlas`; they are not renamed as a Cārvāka poster or standalone ASCII PDF.

## Live scope

- Authoritative Essay catalogue: 16 topics.
- Completed learner-v2 topic packages reviewed now: 4 (`essay-01` to `essay-04`).
- Approval remains false for every successor.

## Defects found and fixed

- The live final library selected obsolete session-style generations instead of the completed Essay-specific guide generations.
- The question-only workbooks contained only two or three full-topic prompts and no outline, introduction, conclusion, paragraph-repair, transition, thesis-correction or evidence-selection practice.
- The model essays were roughly 500-650 words, repeated one generic opening, and omitted explicit why-it-earns-marks and improvement guidance.
- The Essay-specific PDFs were rendered through the legacy mode and therefore had neither an internal contents page nor PDF bookmarks.
- The final library forced Essay into Session/Workbook/Graphical/ASCII folder names even though the authoritative contract is Guide/Question-only Workbook/Separate Solutions with integrated workflow visuals.
- The first immutable successors exposed literal `&#8203;` text inside PDF table cells because a shared renderer escaped its line-break hint; those intermediate generations were retained, failed and superseded.

## Generation transitions

| Topic | Baseline | Successor | Score | Gates |
|---|---|---|---:|---:|
| `essay-01` | `essay-01:learner-v2:g4` | `essay-01:learner-v2:g5` | 98 | 0 |
| `essay-02` | `essay-02:learner-v2:g3` | `essay-02:learner-v2:g4` | 98 | 0 |
| `essay-03` | `essay-03:learner-v2:g3` | `essay-03:learner-v2:g4` | 98 | 0 |
| `essay-04` | `essay-04:learner-v2:g3` | `essay-04:learner-v2:g4` | 98 | 0 |

## Additional completed identities discovered

- `essay-01:learner-v2:g3` — completed but absent from live EXPORT tracker (`upsc-ai-kit\manifests\exports\essay-01-learner-v2-g3-2026-09-04-essay-guide-record.json`).
- `essay-02:learner-v2:g2` — completed but absent from live EXPORT tracker (`upsc-ai-kit\manifests\exports\essay-02-learner-v2-g2-2026-09-04-essay-guide-record.json`).
- `essay-03:learner-v2:g2` — completed but absent from live EXPORT tracker (`upsc-ai-kit\manifests\exports\essay-03-learner-v2-g2-2026-09-04-essay-guide-record.json`).
- `essay-04:learner-v2:g2` — completed but absent from live EXPORT tracker (`upsc-ai-kit\manifests\exports\essay-04-learner-v2-g2-2026-09-04-essay-guide-record.json`).
- `essay-subject-wide-master:learner-v2:g1` — completed auxiliary subject-wide identity; not a catalogue topic and not added to the final topic library (`upsc-ai-kit\manifests\exports\essay-subject-wide-master-learner-v2-g1-2026-09-04-record.json`).

## Complete generation history

- `essay-01`: `essay-01:legacy-v1:g1` (historical) -> `essay-01:learner-v2:g2` (passed) -> `essay-01:learner-v2:g3` (passed) -> `essay-01:learner-v2:g4` (failed) -> `essay-01:learner-v2:g5` (passed)
- `essay-02`: `essay-02:learner-v2:g1` (passed) -> `essay-02:learner-v2:g2` (passed) -> `essay-02:learner-v2:g3` (failed) -> `essay-02:learner-v2:g4` (passed)
- `essay-03`: `essay-03:learner-v2:g1` (passed) -> `essay-03:learner-v2:g2` (passed) -> `essay-03:learner-v2:g3` (failed) -> `essay-03:learner-v2:g4` (passed)
- `essay-04`: `essay-04:learner-v2:g1` (passed) -> `essay-04:learner-v2:g2` (passed) -> `essay-04:learner-v2:g3` (failed) -> `essay-04:learner-v2:g4` (passed)

## Validation

- Full-library topics: **483**.
- Tests passed: **7/7**.
- Canonical Basic/Advanced owners changed: **no**.
- Identity mismatches: **0**.
- Hard-gate failures: **0**.
- Approval: **false**.
