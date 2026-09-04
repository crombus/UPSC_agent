# Deep content review — polity-32 CAG

## Locked baseline
- Identity: `polity-32:learner-v2:g2`; 45 files locked in `g2-identity-lock.json`.
- Initial score: **72/100**; approval false.
- PDFs: session 61, workbook 17, poster 1, tiled 4, ASCII 9 pages.

## Baseline issues
- **High:** no answer-specific improvement/compression guidance across 13 model answers.
- **High:** legacy Basic/Advanced owners overstated “agent/responsible only to Parliament”, froze a three-report taxonomy, and used unsafe historical entity exclusion lists.
- **Medium:** nine-panel flows compressed accounts-after-1976, entity-specific coverage, local-body variation and PAC/CoPU consequences.
- **Medium:** generated source retained two ellipses and did not use strict reviewed H2 ordering.
- **Low:** current digital and reform claims required clearer proposal/status labels.

## Repairs applied before immutable generation
Canonical and tier owners now separate constitutional, statutory and entity-specific rules; the reviewed source contains complete Core before Optional Advanced, 48 strict MCQs, 13 guidance pairs and 12 matching Core flows.

## Immutable regeneration and final review
- `g3`: **96/100**, preserved but failed the prose-integrity hard gate (`cAG` and ellipsis truncation in Session 11).
- `g4`: **98/100**, passed every hard gate after a targeted semantic override.
- 12 Core sessions; 48 MCQs (`ABCD ×12`); 13 guidance pairs; five verified direct/adjacent PYQ routes.
- 12 matching Core flows plus Optional; ASCII width 91; zero ellipses/replacement glyphs.
- PDFs: session 59; workbook 21; poster 1; tiled 4; ASCII 12 pages. Tests: **38 passed**.
- 37 immutable g2 files hash-verified unchanged; approval remains false.
