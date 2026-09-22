# Cross-Platform Upload Guide

Use the portable kit with ChatGPT/OpenAI, Gemini, Claude, GitHub Copilot, or another AI tool that
supports file attachments.

## Live lesson: minimum attachment set

For one topic, attach:

1. `guides/portable-guided-tutor-prompt.md`
2. the topic's complete canonical Markdown owner;
3. the verified PYQ ledger covering that topic through the latest available year.

Optional attachments:

4. relevant book chapters or OCR-searchable PDFs;
5. `UPSC-PROGRESS-TRACKER.md`;
6. the latest printed `SESSION CHECKPOINT` when resuming in another conversation or tool.

Do not upload the whole repository when the platform has a limited context window. A smaller,
topic-specific attachment set is more likely to be read completely.

## Platform setup

### ChatGPT / OpenAI

- Use a Project, Custom GPT, or conversation with file uploads.
- Paste `system-prompt.md` into project/custom instructions where supported.
- Upload `skills/study/SKILL.md`, the portable tutor prompt, and the topic files.
- Enable web browsing for the six-month current-affairs check.

### Gemini

- Use a Gem or a conversation with attached files.
- Paste `system-prompt.md` into Gem instructions.
- Attach the study skill, portable tutor prompt, and topic files.
- Enable Google Search grounding where available.

### Claude

- Use a Project.
- Paste `system-prompt.md` into Project instructions.
- Add `skills/study/SKILL.md`, the portable prompt, and topic files as Project knowledge.
- Enable web search where available.

### GitHub Copilot

- Add the prompt and topic files to the working context or repository.
- Use the portable prompt as the session instruction.
- Keep the printed checkpoint in a tracked or local Markdown file when the conversation may be
  restarted.

## Continuity rule

Never rely only on a platform's hidden memory. Copy the latest visible `SESSION CHECKPOINT` when
moving to a new conversation or tool. The receiving tutor must resume from that checkpoint
without restarting completed subtopics or resetting mastery counts.
