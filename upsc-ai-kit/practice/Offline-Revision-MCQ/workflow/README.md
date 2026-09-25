# Offline Package Workflow Controls

`offline_workflow.py` implements shared, integrity-preserving controls. It does not replace any
topic validator, content audit, independent review, negative test, or release gate.

## Required pass start

Before every development, repair, review, boundary, release, commit, or push pass:

```powershell
python workflow\offline_workflow.py begin-pass `
  --topic <topic-directory> `
  --pass-id <stable-pass-id> `
  --pass-type focused-repair `
  --coverage-frozen `
  --pyqs-current `
  --surfaces-preserved `
  --no-skip-compression `
  --coverage-derived-mcqs
```

This reads and hashes both controlling instruction files and writes `PASS-MANIFEST.json`.

## Shared optimization controls

```powershell
# Reuse parsed evidence only while every source hash and byte count remains identical.
python workflow\offline_workflow.py freeze-evidence --topic <topic-directory>

# Create a bounded independent-review packet from current changes and frozen counts.
python workflow\offline_workflow.py review-packet --topic <topic-directory> `
  --scope "changed semantic mappings only" `
  --obligation <ID> `
  --frozen-surface "PYQ and Mains coverage"

# Run fast semantic-risk checks before a full build.
python workflow\offline_workflow.py semantic-lint --topic <topic-directory> --strict

# Reject validator dependencies on builder expectations, question banks, or renderers.
python workflow\offline_workflow.py validator-contract --topic <topic-directory>

# Select focused copied-package tests during repair; the full suite remains mandatory at the
# final development gate.
python workflow\offline_workflow.py negative-plan --topic <topic-directory> `
  --invariant "authority|source|representation"

# Register an approved source with its exact bytes, hash, provenance, rights, role, and scope.
python workflow\offline_workflow.py register-source `
  --source-id <stable-id> `
  --topic-name <topic> `
  --role <formal|canonical|verified-pyq|user-approved-primary> `
  --scope <permitted-use> `
  --file <local-immutable-file> `
  --provenance <source-description> `
  --rights <rights-description>

# Import all currently hash-bound source snapshots from a topic audit.
python workflow\offline_workflow.py sync-sources --topic <topic-directory>
```

## Integrity invariants

- A cache hit never bypasses validation; it only avoids reparsing unchanged hash-bound evidence.
- A focused review never reopens frozen surfaces unless direct contradictory evidence appears.
- Semantic lint is an early failure gate, not a substitute for the production validator.
- Focused negative tests accelerate repair; the complete suite is mandatory before release.
- The source registry cannot expand a source's authority beyond its recorded permitted scope.
- `PASS-MANIFEST.json`, `EVIDENCE-CACHE.json`, review packets, lint reports, independence reports,
  and negative-test plans are machine-readable evidence, not learner content.
