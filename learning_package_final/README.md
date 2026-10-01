# Final Learning Packages

This folder provides one browsable location for the final Markdown learning sessions
and solved-practice workbooks selected by `notes/Final-Learning-Packages/MASTER-TRACKER.json`.
The original source files remain unchanged in their canonical locations.

Essay, Qualifying English, and Qualifying Hindi use their final subject-wide
guide/workbook/solutions packages instead of artificial topic learning sessions.

## Inventory

| Subject | Final topics | Markdown files |
|---|---:|---:|
| Ancient History | 27 | 54 |
| Disaster Management | 18 | 36 |
| Economy | 31 | 62 |
| Environment and Ecology | 28 | 56 |
| Ethics | 23 | 46 |
| Geography | 37 | 74 |
| Governance | 16 | 32 |
| Indian Art and Culture | 15 | 30 |
| Indian Society | 15 | 30 |
| Internal Security | 12 | 24 |
| International Relations | 12 | 24 |
| Medieval History | 25 | 50 |
| Modern History | 38 | 76 |
| Philosophy Optional | 40 | 80 |
| Political Theory | 23 | 46 |
| Polity | 55 | 110 |
| Science and Technology | 26 | 52 |
| Social Justice | 17 | 34 |
| World History | 21 | 42 |
| Essay | Subject-wide package | 3 |
| Qualifying English | Subject-wide package | 3 |
| Qualifying Hindi | Subject-wide package | 3 |

Standard final topics: **479**
Total copied Markdown files: **967**

See `MANIFEST.json` for every destination, canonical source path, file size,
and SHA-256 checksum.

## Repository-wide review and repair scope

For the sequential topic-by-topic review, use this active flow:

1. Read canonical evidence from `upsc-ai-kit\knowledge\<Subject>\basic` and `advanced`.
2. Verify PYQs through the routing ledgers and official locally held papers.
3. Repair only `learning_package_final`:
   - Learning-session Markdown
   - Solved-practice workbook Markdown
4. Repair only the matching `quick_galance` artifact:
   - Quick-glance tree-flowchart Markdown

Canonical knowledge and official papers are read-only evidence. Ignore PDFs,
`notes\Final-Learning-Packages`, graphical/ASCII master-flow packages, manifests, trackers,
historical generation folders and other duplicate artifacts unless explicitly requested.
Repair existing Markdown files in place; do not create suffixed parallel packages.

### Review gates

- After completing and validating each topic, stop and notify the user so the repaired
  package can be reviewed. Do not begin the next topic automatically.
- After completing a subject, provide the complete list of subjects that remain.
- Wait for the user to select the next subject before continuing.

The full mandatory source hierarchy, artifact checks and pass/fail completion
record are maintained in `REVIEW-AND-REPAIR-INSTRUCTIONS.md`. Read that file
before every topic review and do not mark a topic complete while any mandatory
check remains unresolved.
