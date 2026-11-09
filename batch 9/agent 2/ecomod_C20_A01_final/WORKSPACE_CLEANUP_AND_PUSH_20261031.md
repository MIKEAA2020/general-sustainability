# Push-before-delete record — 31 October 2026

**Rule applied:** every creation pushed and byte-verified on the remote before any local deletion; only reclonable duplicates removed; frozen roots untouched.

## 1. Pushed

- Repository: `MIKEAA2020/general-sustainability`, branch `main`, path `batch 9/agent 2/ecomod_C20_A01_final/`
- Commit: `b26504d95a7ca7fcd5336a8c225cdfd30dcaa993`
- Files: **86**, total 10,870,846 bytes
  - `em_upload/` — complete Editorial Manager set, including the two portal-safe `.tex` files, figures, graphical abstract, cover letter, response, data availability, reproduction guide, captions, code, LaTeX dependencies
  - `c20_package/` — C20 A01 package: sources, PDFs, manifests, diffs, change record
  - `ecomod_C20_preprints_source_20261031.zip` and its verification JSON
  - `ECOMOD_C20_A01_reproduction_package.zip` (the Zenodo payload)
  - `HOW_TO_DEPOSIT.md`
- **Verification:** all 86 remote git blob SHAs compared against locally computed blob SHAs — **86 verified, 0 missing, 0 mismatched**.

## 2. Independently anchored elsewhere

| Artifact | Where | Verification |
|---|---|---|
| Reproduction package | Zenodo dataset, DOI 10.5281/zenodo.24092131 | handle resolves; record typed Dataset; file size 6,021,179 bytes; **local md5 `8a51345b76609063d10c8a282c1b8387` equals the Zenodo-reported checksum** |
| Source archive | GitHub commit above, plus Zenodo payload | 24-file manifest verified on clean extraction; rebuilds to 38/31 pages |
| Manuscript PDF | EM set, C20 package, Zenodo payload | hash-identical across all three |

## 3. Deleted (reclonable)

| Removed | Size | Why it is safe |
|---|---|---|
| `ecomod_C19_preprints_source_20261031/` and `.zip` | 504 KB + 228 KB | Superseded by C20; the frozen `ecomod_editorial_division_C19_A01/` root is untouched and still rebuilds both documents, so the C19 staging copy is regenerable |
| `ecomod_zenodo_deposit/ECOMOD_C20_A01_reproduction_package/` | 7.9 MB | Byte-identical to the published Zenodo record (md5 matched) and to the retained `ECOMOD_C20_A01_reproduction_package.zip`; re-downloadable from the DOI |
| `__pycache__`, transient LaTeX build dirs | small | Regenerated on demand |

**Freed: 8,785,029 bytes.** Workspace: 111,163,654 → 102,378,625 bytes.

## 4. Retained deliberately

- `ecomod_C20_EM_upload/` — the live submission set (includes the portal-safe sources)
- `ecomod_C20_preprints_source_20261031.zip` — the Preprints.org source archive
- `ecomod_zenodo_deposit/ECOMOD_C20_A01_reproduction_package.zip` — the exact deposited payload
- `ecomod_deposit_doi_C20_A01/` — C20 package with manifests, diffs and the change record
- Frozen roots: `ecomod_editorial_division_C19_A01/`, `ecomod_audit_remediation_C18_A01/`, F11–F16, R01/R02, governance packages. None edited, none deleted.

## 5. Restore commands

```bash
# reproduction package, from the DOI
curl -L -o ECOMOD_C20_A01_reproduction_package.zip https://zenodo.org/records/24092131/files/ECOMOD_C20_A01_reproduction_package.zip
# or from the local retained zip
unzip ECOMOD_C20_A01_reproduction_package.zip

# C19 staging source package, if ever needed again
cp -r ecomod_editorial_division_C19_A01 <staging>/ && rebuild with three pdflatex passes
```
