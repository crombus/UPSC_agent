# Deep content review — polity-35 NHRC and SHRC

## Identity and outcome
- Baseline `polity-35:learner-v2:g2`; 49 hashes locked; **76/100**; approval false.
- Preserved `polity-35:learner-v2:g3`; **94/100**; failed manual prose-integrity review.
- Preserved `polity-35:learner-v2:g4`; **97/100**; failed manual acronym-integrity review.
- Final `polity-35:learner-v2:g5`; **98/100**; all hard gates passed; approval remains false.

## Substantive repairs
- Corrected “retired judge only” shorthand: current sections 3/21 use persons who have held the judicial office, with statutory CJI consultation for sitting judicial appointees.
- Replaced claims of an independently “own” investigation staff with the exact sections 11/14 government-supplied staff and consensual agency-support architecture.
- Removed unsupported Consolidated-Fund independence and “binding advice” language; stated the Supreme Court inquiry/report removal route precisely.
- Clarified that Human Rights Courts are enabling State notifications, not automatic functioning courts in every district.
- Preserved section 19 armed-forces procedure, section 36 bars, section 18 recommendatory effect, reporting routes, SHRC adaptations, Paris Principles/GANHRI status discipline and case-law limits.
- Added ten answer-specific improvement/compression instructions and expanded both flows from nine to twelve Core stages.

## Final validation
- 16 sessions; two direct Mains PYQs plus one qualified supporting Prelims route; 48 MCQs in strict `ABCD x12`; ten guidance pairs.
- PDFs: 70/21/1/4/12 pages; complete ASCII maximum width 99.
- Zero ellipses, replacement glyphs or malformed NHRC/SHRC acronyms; graphical and ASCII rails agree.
- `python -m pytest -q tools\test_refresh_all_v2_learning_sessions.py`: **38 passed**.
- 41 immutable g2 hashes checked outside the mutable final-library destination; zero mismatches.

## Export
`notes\Final-Learning-Packages\Polity\Subject-wide Syllabus\35-NHRC-and-SHRC`
