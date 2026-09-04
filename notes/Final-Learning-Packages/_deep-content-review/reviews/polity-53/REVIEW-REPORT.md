# Deep Content Review — polity-53

## Locked baseline

- Identity: `polity-53:learner-v2:g2`
- Lock/recheck: `g2-identity-lock.json`, `g2-identity-recheck.json`
- Initial score: **68/100**
- Approval: false

## Baseline findings

| Artifact | Finding |
|---|---|
| Learning session | Broad Part XVI map, but generated prose contained replacement/truncation artefacts and the canonical owner falsely treated 16 April 2026 as commencement of the 106th Amendment. The section 1(2) commencement gate was missing. |
| Workbook | Four PYQs were paraphrased, models were formulaic, answer-specific Why/How/compression was absent, and 48 keys were not strict A-B-C-D. |
| Graphical flow | Nine Core stages plus stale “g2 repaired in place” provenance; commencement, delimitation, EWS and Davinder boundaries were compressed. |
| ASCII flow | Nine panels omitted the complete five-gate 106th-Amendment chain and an executable source-selection decision tree. |

## Required repair

Preserve g2. Correct the Core owner, create a fresh reviewed source, reproduce exact PYQs, add
marks-worthy original answers and hard strict-rotation MCQs, expand both flows to twelve agreeing
Core stages, regenerate all four artifacts and keep approval false.

## Revalidation

Immutable successor `polity-53:learner-v2:g3` passed at **98/100** (39/40, 29/30, 15/15, 15/15). All hard gates passed; approval remains false.
