# Learner-v2 Section Manifests

Section manifests are the machine-readable plan for subject-wise, section-wise generation. Create
or approve the manifest **before** generating a section. It records the complete planned topic
list, official-syllabus mapping, Markdown owners, thematic/PYQ supplements and any legacy-v2
compatibility paths.

## Controlling completeness rule

Markdown is the primary content source, but no single Markdown file proves completeness. Every
topic must be reconciled against:

1. the official UPSC syllabus;
2. the Basic or canonical owner;
3. relevant cross-topic/thematic Markdown;
4. available verified PYQs and answer-practice owners;
5. the Advanced owner, taught only after the complete Basic/practice sequence.

OCR-searchable PDFs and live sources supplement this chain. They do not replace its Markdown
owners or official-syllabus boundary.

## Schema and naming

- Schema: [`section-manifest.schema.json`](section-manifest.schema.json)
- Copyable template: [`section-manifest.template.json`](section-manifest.template.json)
- Recommended filename: `<subject-slug>--<section-key>.json`
- `topic_key` values must be unique and stable.
- Use repository-relative paths. Either slash style is accepted; generated indexes display
  Windows paths and use portable relative Markdown links.
- `scope: "pilot"` plus `complete_syllabus_section: false` must be used for a pilot subset.
- Existing learner-v2 pilot paths may be stated explicitly in `assembled_markdown`, `notes_pdf`
  and `workbook_pdf`. Do not move or duplicate those files.

## Preferred future layout

```text
notes\<Subject>\learning-session-v2\<section-key>\
  notes\<topic-key>_Learning-Session_<date>.pdf
  workbooks\<topic-key>_Solved-Workbook_<date>.pdf
  indexes\TOPIC-COVERAGE-INDEX.md
  indexes\NOTES-PDF-INDEX.md
  indexes\WORKBOOK-PDF-INDEX.md

upsc-ai-kit\knowledge\<Subject>\learning-sessions\v2\<section-key>\
  <topic-key>_Learning-Session.md
```

Existing topic-folder pilots remain valid legacy-v2 compatibility paths and are indexed in place.

## Commands

When a README or syllabus index defines one unambiguous section boundary:

```powershell
python tools\generate_v2_section_indexes.py `
  --subject Geography `
  --section-key human-economic-and-regional-geography `
  --section-name "Part B — Human, Economic and Regional Geography" `
  --write-manifest upsc-ai-kit\manifests\v2\geography--human-economic-and-regional-geography.json
```

When discovery is ambiguous, copy the template, fill the complete topic list, then run:

```powershell
python tools\generate_v2_section_indexes.py `
  --manifest upsc-ai-kit\manifests\v2\<subject-slug>--<section-key>.json
```

After one generated topic has passed validation and its exact tracker record is ready:

```powershell
python tools\finalize_v2_topic.py `
  --manifest upsc-ai-kit\manifests\v2\<subject-slug>--<section-key>.json `
  --record-file <validated-topic-record.json>
```

That helper validates the known topic outputs, upserts only the supplied tracker identity, refreshes
the global export command index, and refreshes the three section indexes. It does not generate
teaching content.
