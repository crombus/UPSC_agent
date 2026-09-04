# Learner-v2 Refreshed — Three-Topic Pilot Report

- Refresh ID: `learner-v2-refreshed-2026-08-22`
- Tracker mutation: **none**
- Selection: Notions of God + deterministic first completed Polity + deterministic first completed History/Geography topic

| Topic key | Generation | Sessions | Main pages | Workbook pages | Validation |
|---|---:|---:|---:|---:|---|
| `ancient-indian-history-01` | g6 | 10 | 145 | 39 | PASS |
| `philosophy-paper-ii-philosophy-of-religion-01` | g7 | 13 | 109 | 40 | PASS |
| `polity-01` | g9 | 17 | 74 | 16 | PASS |

## Deliverables

### `ancient-indian-history-01`

- Markdown: `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Ancient-Indian-History\Subject-Wide-Syllabus\learning-sessions\ancient-indian-history-01\ancient-indian-history-01_Complete-Learning-Session_2026-08-22.md`
- Workbook Markdown: `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Ancient-Indian-History\Subject-Wide-Syllabus\learning-sessions\ancient-indian-history-01\ancient-indian-history-01_Solved-Practice-Workbook_2026-08-22.md`
- Main PDF: `notes\Learner-v2-Refreshed\Ancient-Indian-History\Subject-Wide-Syllabus\learning-sessions\ancient-indian-history-01\ancient-indian-history-01_Complete-Learning-Session_2026-08-22.pdf`
- Workbook PDF: `notes\Learner-v2-Refreshed\Ancient-Indian-History\Subject-Wide-Syllabus\learning-sessions\ancient-indian-history-01\ancient-indian-history-01_Solved-Practice-Workbook_2026-08-22.pdf`
- Flowchart package: `notes\Learner-v2-Refreshed\Ancient-Indian-History\Subject-Wide-Syllabus\flowcharts\ancient-indian-history-01\carvaka-g6`

### `philosophy-paper-ii-philosophy-of-religion-01`

- Markdown: `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Philosophy\Philosophy-of-Religion\learning-sessions\Notions-of-God\Notions-of-God_Complete-Learning-Session_2026-08-22.md`
- Workbook Markdown: `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Philosophy\Philosophy-of-Religion\learning-sessions\Notions-of-God\Notions-of-God_Solved-Practice-Workbook_2026-08-22.md`
- Main PDF: `notes\Learner-v2-Refreshed\Philosophy\Philosophy-of-Religion\learning-sessions\Notions-of-God\Notions-of-God_Complete-Learning-Session_2026-08-22.pdf`
- Workbook PDF: `notes\Learner-v2-Refreshed\Philosophy\Philosophy-of-Religion\learning-sessions\Notions-of-God\Notions-of-God_Solved-Practice-Workbook_2026-08-22.pdf`
- Flowchart package: `notes\Learner-v2-Refreshed\Philosophy\Philosophy-of-Religion\flowcharts\Notions-of-God\carvaka-g7`

### `polity-01`

- Markdown: `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Polity\Subject-Wide-Syllabus\learning-sessions\polity-01\polity-01_Complete-Learning-Session_2026-08-22.md`
- Workbook Markdown: `upsc-ai-kit\knowledge\Learner-v2-Refreshed\Polity\Subject-Wide-Syllabus\learning-sessions\polity-01\polity-01_Solved-Practice-Workbook_2026-08-22.md`
- Main PDF: `notes\Learner-v2-Refreshed\Polity\Subject-Wide-Syllabus\learning-sessions\polity-01\polity-01_Complete-Learning-Session_2026-08-22.pdf`
- Workbook PDF: `notes\Learner-v2-Refreshed\Polity\Subject-Wide-Syllabus\learning-sessions\polity-01\polity-01_Solved-Practice-Workbook_2026-08-22.pdf`
- Flowchart package: `notes\Learner-v2-Refreshed\Polity\Subject-Wide-Syllabus\flowcharts\polity-01\carvaka-g9`

## Remaining migration commands

```powershell
python tools\refresh_all_v2_learning_sessions.py generate --remaining-after-pilot --no-tracker-update
python tools\refresh_all_v2_learning_sessions.py validate --all
python tools\refresh_all_v2_learning_sessions.py stage-records --all
python tools\refresh_all_v2_learning_sessions.py finalize --all --commit
```
