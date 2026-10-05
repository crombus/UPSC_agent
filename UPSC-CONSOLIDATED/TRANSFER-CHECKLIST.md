# Transfer Checklist

## 1. Before copying

- [ ] Close the UPSC CLI, PDF generators, editors, Qdrant/Chroma containers, and ingestion jobs.
- [ ] Keep the source tree unchanged; use copy commands only. Do not use `Move-Item`, rename, delete, or `robocopy /MIR`.
- [ ] Confirm destination free space. Observed scope: P0 `2.44 GiB`, P1 `37.42 GiB`, optional P2 `8.90 GiB`.
- [ ] Keep `.env` out of shared media; create it locally from `.env.example` after transfer.

## 2. Copy in priority order

```powershell
$Source = 'C:\Users\pulkitkundra\Downloads\pk-workspace\upsc-agent'
$Dest = '<DESTINATION>\upsc-agent'
New-Item -ItemType Directory -Force -Path $Dest | Out-Null
```

### P0 — core learning/control layer

```powershell
$P0 = @('UPSC-CONSOLIDATED','learning_package_final','upsc-ai-kit\knowledge','quick_galance','tools','ingestion')
foreach ($Rel in $P0) { robocopy (Join-Path $Source $Rel) (Join-Path $Dest $Rel) /E /COPY:DAT /DCOPY:DAT /R:2 /W:2 /XJ /L }
# Review dry-run output, then rerun the same command without /L.
```

Copy root controls without `.env`:

```powershell
$Controls = @('README.md','AGENTS.md','AGENT_MEMORY.md','UPSC-PROGRESS-TRACKER.md','EXPORT-PDF-STATUS.json','EXPORT-PDF-COMMAND-INDEX.md','V2-SUBJECT-SECTION-COMMAND-INDEX.md','requirements.txt','docker-compose.yml','config.yaml','.env.example')
foreach ($Name in $Controls) { Copy-Item (Join-Path $Source $Name) (Join-Path $Dest $Name) -Force }
```

### P1 — generated output and learner state

```powershell
$P1 = @('notes','exams','attempts')
foreach ($Rel in $P1) { robocopy (Join-Path $Source $Rel) (Join-Path $Dest $Rel) /E /COPY:DAT /DCOPY:DAT /R:2 /W:2 /XJ /L }
# Review, then rerun without /L. Copy notes last if bandwidth/free space is tight.
```

### P2 — optional large local data

```powershell
$P2 = @('books','vectordb')
foreach ($Rel in $P2) { robocopy (Join-Path $Source $Rel) (Join-Path $Dest $Rel) /E /COPY:DAT /DCOPY:DAT /R:2 /W:2 /XJ /L }
# Review, then rerun without /L only for the folders you need.
```

- `books`: `2.39 GiB`; retain when original PDFs are not safely available elsewhere.
- `vectordb`: `6.51 GiB`; optional for Markdown/OCR-first study and rebuildable only with required model/service access.
- `notes`: `37.34 GiB`; large but not optional because it contains authoritative generated outputs.

## 3. Verify after copying

- [ ] Open `UPSC-CONSOLIDATED\MASTER-INDEX.md` and resolve every linked authoritative path.
- [ ] Parse both CSV files and verify unique keys: 23 subjects and 516 topics.
- [ ] Parse `INTEGRITY-MANIFEST.json` and compare directory file counts/bytes to the destination.
- [ ] Recompute SHA-256 for every existing `critical_files` entry and compare it to the manifest.
- [ ] Confirm latest learner-v2 artifacts: 516 completed/validated, 516 explicitly unapproved, 0 approved.
- [ ] Confirm quick-glance status: 479 completed, 0 pending.
- [ ] Create a fresh `.env`; never copy credentials from transfer media.
- [ ] Run the smoke tests in `ENVIRONMENT-SETUP.md`.
- [ ] If `books` or `vectordb` was omitted, record that locally; do not mark affected data approved or missing.

## 4. Integrity comparison snippet

```powershell
$Root = '<DESTINATION>\upsc-agent'
$Manifest = Get-Content (Join-Path $Root 'UPSC-CONSOLIDATED\INTEGRITY-MANIFEST.json') -Raw | ConvertFrom-Json
$Manifest.critical_files | Where-Object exists | ForEach-Object {
  $Actual = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $Root $_.path)).Hash.ToLower()
  [pscustomobject]@{ Path=$_.path; Match=($Actual -eq $_.sha256) }
}
```
