# Repository Instruction Registry

This directory stores the user's approved, durable generation and validation
instructions for future reference.

## Registration rule

When the user approves a new durable workflow, quality, generation, validation or
delivery instruction:

1. record it in the relevant file under `instructions\`;
2. update this registry when a new instruction file or category is created;
3. update the affected authoritative standard when the instruction changes its
   behaviour;
4. avoid competing copies with different wording or requirements;
5. preserve every existing requirement unless the user explicitly replaces it.

Conversation summaries and assistant memory are continuity aids, not substitutes for
these repository instruction files.

## Instruction index

| Area | Instruction file | Scope |
|---|---|---|
| Generation optimization and integrity | `instructions\GENERATION-OPTIMIZATION-AND-INTEGRITY.md` | All new UPSC generation workflows |
| PDF learning sessions | `instructions\pdf-learning-session\PDF-LEARNING-SESSION-STANDARD.md` | PDF sessions, topic packages and visual revision packages |
| Live learning sessions | `live_sessions\LIVE-SESSION-GENERATION-RULES.md` | Interactive/live Markdown generation and validation |

The live-session rules remain at their established path because existing sessions and
automation reference it. This registry makes that authority discoverable from the
central `instructions` directory without maintaining a conflicting duplicate.
