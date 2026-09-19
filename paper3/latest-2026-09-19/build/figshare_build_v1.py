#!/usr/bin/env python3
"""Prepare a Figshare-ready full-length deposit without modifying the v49 archive.

The zip contains the full-length four-document line, the source and analysis records, and the new
journal variants. It deliberately does not copy the 16 MB third-party GFN NFA tables; their source
manifest and checksums are carried instead. The zip digest is written to a sidecar outside the zip.
"""
from __future__ import annotations
import hashlib, json, os, shutil, zipfile
from pathlib import Path

ROOT = Path('/home/user')
V7 = ROOT / 'revision/v7'
JV = ROOT / 'revision/journal_variants'
OUT = ROOT / 'revision/figshare_deposit'
NAME = 'paper3_full_length_figshare_v1'
STAGE = OUT / NAME
ZIP = OUT / f'{NAME}.zip'
SIDECAR = OUT / f'{NAME}.sha256'

if STAGE.exists(): shutil.rmtree(STAGE)
if ZIP.exists(): ZIP.unlink()
if SIDECAR.exists(): SIDECAR.unlink()
for d in ('manuscript','code','analysis/nfa_tau','journal_variants/assets','journal_variants/route_c_prototype'):
    (STAGE/d).mkdir(parents=True, exist_ok=True)

# Full-length four-document source and compiled surfaces.
for base in ('paper3_material_ledgers_v49','paper3_supplementary_v18',
             'companionA_certification_procedure_v9','companionB_standards_horizon_v9'):
    for ext in ('.md','.tex','.pdf'):
        shutil.copy2(V7/f'{base}{ext}', STAGE/'manuscript'/f'{base}{ext}')
shutil.copy2(V7/'paper3_supplementary_v18.ascii.md', STAGE/'manuscript')

# Reproduction code and its own run record.
for p in (V7/'code').iterdir():
    if p.is_file(): shutil.copy2(p, STAGE/'code'/p.name)

# Analysis record, excluding the third-party source tables themselves.
AN = V7/'analysis/nfa_tau'
for name in ('README.md','README_v2.md','checksums.txt','edition_delta.csv','recompute_tau.py',
             'results.txt','tau_by_year_2017edition.csv','tau_by_year_2018edition.csv'):
    shutil.copy2(AN/name, STAGE/'analysis/nfa_tau'/name)
(STAGE/'analysis/nfa_tau'/'source').mkdir()
shutil.copy2(AN/'source/MANIFEST.md', STAGE/'analysis/nfa_tau/source/MANIFEST.md')

# Target-specific cuts and the new figure/prototype.
for name in ('README.md','paper3_JIE_submission_v1.md','paper3_EE_submission_v1.md',
             'technical_supplement_v1.md','validate_journal_variants.py','journal_variants_validation.json',
             'render_variants_v1.py','JOURNAL_VARIANTS_IMPLEMENTATION_v1.md'):
    shutil.copy2(JV/name, STAGE/'journal_variants'/name)
(STAGE/'journal_variants/rendered').mkdir(parents=True, exist_ok=True)
for p in (JV/'rendered').glob('paper3_*_submission_v1.*'):
    if p.suffix in {'.pdf', '.tex'}:
        shutil.copy2(p, STAGE/'journal_variants/rendered'/p.name)
for name in ('typed_ledger_readout.svg','typed_ledger_readout.png'):
    shutil.copy2(JV/'assets'/name, STAGE/'journal_variants/assets'/name)
for name in ('README.md','typed_ledger.py','test_typed_ledger.py','pyproject.toml'):
    shutil.copy2(JV/'route_c_prototype'/name, STAGE/'journal_variants/route_c_prototype'/name)

readme = '''# Full-length Figshare-ready deposit

**Working package:** paper3 full-length line, with journal-specific cuts and a route-C prototype.
**Source line:** v49, 2026-09-19. **License:** CC BY 4.0 for the author's manuscript and accompanying
original code, subject to the third-party notices and source restrictions recorded below.

## Contents

- `manuscript/`: the four full-length documents, each in Markdown, LaTeX and PDF where applicable;
- `code/`: the executable reproduction exhibits, manifests and recorded outputs;
- `analysis/nfa_tau/`: the overshoot-date recomputation, derived tables, checksums and source manifest;
- `journal_variants/`: the 6,000-word JIE cut, 8,000-word Ecological Economics cut, technical proof
  supplement, diagram and route-C prototype;
- `metadata.json`: proposed Figshare metadata;
- `CHECKSUMS.sha256`: checksums of every file in this deposit.

## Boundaries and omissions

This deposit preserves the full-length article and its provenance. The 16 MB third-party National
Footprint and Biocapacity Accounts source tables are **not copied**. Their source manifest and checksums
remain in `analysis/nfa_tau/source/`; the publisher's licence and retrieval conditions are recorded in
the analysis README and the full-length data-availability statement. No third-party table is silently
redistributed here.

The route-C implementation is a tested reference prototype, not yet a supported software package. It
implements typed declarations, incidence construction, balance residuals, componentwise barriers and a
non-compensation witness. It does not claim the complete eight-predicate solver or a production API.

The journal cuts are derived working surfaces. The full-length v49 manuscript remains the authoritative
complete article. A journal-specific mathematical edit must be made in the full-length source first and
then re-extracted and re-verified.

## Reproduction

The full-length build record and current v49 archive remain in the workspace. The code exhibits run with
the environment recorded in `code/MANIFEST.md`. The journal-variant gate is rerun with:

```sh
python3 journal_variants/validate_journal_variants.py
python3 -m pytest -q journal_variants/route_c_prototype/test_typed_ledger.py
```

The zip digest belongs in the Figshare record or the sidecar next to the downloadable zip, not in a file
inside the zip.
'''
(STAGE/'README.md').write_text(readme)
meta = {
    'title': 'Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the Semantics of Depletion Horizons',
    'version': 'full-length v49 with journal-specific submission variants v1',
    'date': '2026-09-19',
    'authors': [{'name': 'Amin Abaee', 'orcid': '0000-0002-0019-1842'}],
    'description': 'A typed stock-flow accounting framework separating material conservation, componentwise barriers, service readouts and three non-interchangeable depletion quantities. The deposit includes the full-length article, supplementary and companion documents, executable reproduction records, target-specific journal cuts and a tested route-C reference prototype.',
    'keywords': ['material flow accounting','stock-flow ledger','ecological economics','industrial ecology','depletion indicators','componentwise sustainability','conservation laws','first-passage semantics'],
    'license': {'name': 'Creative Commons Attribution 4.0 International', 'spdx': 'CC-BY-4.0', 'url': 'https://creativecommons.org/licenses/by/4.0/'},
    'figshare_note': 'Metadata is prepared for deposit; no upload or DOI assignment was attempted in the workspace.',
    'third_party_note': 'GFN National Footprint and Biocapacity Accounts source tables are omitted; source manifest and checksums are retained.',
}
(STAGE/'metadata.json').write_text(json.dumps(meta, indent=2, ensure_ascii=False)+'\n')

# Stable manifest/checksums, excluding zip and sidecar.
files = sorted(p for p in STAGE.rglob('*') if p.is_file())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
lines=[]
for p in files:
    lines.append(f'{sha(p)}  {p.relative_to(STAGE).as_posix()}')
(STAGE/'CHECKSUMS.sha256').write_text('\n'.join(lines)+'\n')

with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(x for x in STAGE.rglob('*') if x.is_file()):
        z.write(p, NAME+'/'+p.relative_to(STAGE).as_posix())
zipsha=hashlib.sha256(ZIP.read_bytes()).hexdigest()
SIDECAR.write_text(f'{zipsha}  {ZIP.name}\n{len(files)} files inside the deposit tree\n')
print('staged files:',len(files))
print('zip records:',len(zipfile.ZipFile(ZIP).infolist()),'bytes:',ZIP.stat().st_size)
print('sha256:',zipsha)
print('sidecar:',SIDECAR)
