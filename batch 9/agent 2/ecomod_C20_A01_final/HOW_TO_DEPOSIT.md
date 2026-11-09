# Zenodo deposit — decision and instructions

**Short answer: create a NEW, standalone dataset record. Do not version record 22554480, and do not update it to the current manuscript.**

## Why not a new version of 22554480

Record 22554480 is an existing **Preprint** record holding the superseded **v35** files (`manuscript_ECOMOD_v35.tex/.pdf`, `figures.tar.gz`, dated 6 September 2026). Publishing a new version of it would:

- make the reproduction package the "latest version" of a **preprint**, while the manuscript of record is the Preprints.org deposit — the mismatch you identified;
- mix two different objects (a manuscript and a data/code package) under one concept DOI;
- imply that the Zenodo preprint is still the manuscript, competing with `10.20944/preprints202611.0852.v1`.

A separate **Dataset** record avoids all three. It is a distinct object with its own DOI, typed as data rather than as a preprint, and it links *out* to the Preprints.org record instead of claiming to be it. It also keeps 22554480 historically honest: that record remains the earlier preprint upload, with no silent substitution of its files.

What this record exists to do is narrow and sufficient: **satisfy the journal's Option C research-data requirement and make the analysis re-runnable.** It does not need to be, and is not presented as, the manuscript.

Optional tidying, your call: add a note or "is related to" link on record 22554480 pointing to the new dataset record and to the Preprints.org DOI. Zenodo allows metadata edits on a published record without creating a version, so this does not break anything.

## Which files go where

- **Manuscript of record:** Preprints.org, `10.20944/preprints202611.0852.v1`. Nothing is duplicated there by this deposit except the PDFs bundled inside the package for convenience.
- **Data and code:** the new dataset record (this package).
- **Journal submission:** the EM upload set in `ecomod_C20_EM_upload/`, with the dataset DOI pasted into the data-availability field.

## Option A — web interface (~5 minutes)

1. Sign in at https://zenodo.org and click **New upload** (not "New version").
2. Upload `ECOMOD_C20_A01_reproduction_package.zip` (6.0 MB), or unzip and upload the tree if you prefer browsable files.
3. Fill in from `ECOMOD_C20_A01_reproduction_package/zenodo/zenodo_metadata.json`:
   - **Title:** Reproduction package for: A rising biocapacity total can mask ecological-capital land drawdown: a two-land model
   - **Upload type:** Dataset
   - **Publication date:** 2026-10-31
   - **Version:** 1.0 (ECOMOD C20 A01)
   - **Creators:** Abaee, Amin — ORCID 0000-0002-0019-1842 — Independent Researcher, Tehran, Iran
   - **Keywords:** biocapacity; ecological footprint; land-use conversion; aggregation; identifiability; delay differential equations; reproducibility
   - **Licence:** CC BY-SA 4.0 (the package embeds NFA-derived data under that licence)
   - **Related identifiers:** `10.20944/preprints202611.0852.v1` → *is supplement to*; `10.5281/zenodo.22554480` → *is related to*; `https://github.com/MIKEAA2020/general-sustainability` → *is identical to*
   - **Description:** the HTML in the metadata file
4. **Publish** and copy the DOI.

## Option B — API (one command)

```bash
cd /home/user/ecomod_zenodo_deposit/ECOMOD_C20_A01_reproduction_package
export ZENODO_TOKEN=...      # zenodo.org/account/settings/applications/ , scope deposit:write
python zenodo/upload_to_zenodo.py --package-root . --dry-run   # lists files and metadata
python zenodo/upload_to_zenodo.py --package-root .
```

The script creates a standalone deposit, uploads with relative paths, applies metadata and publishes. It never touches record 22554480. Use `--sandbox` to rehearse.

## After publishing

Send me the dataset DOI. I will add it to the manuscript's Data availability statement alongside the Preprints.org DOI, rebuild, and refresh the EM upload set, the source ZIP and the Zenodo package so every artifact carries the same identifiers.

## What is in the package

59 files, 8.1 MB uncompressed, 6.0 MB zipped: manuscript (38 pp) and SI (31 pp) sources and PDFs, 8 figure PDFs, 9 table fragments, 3 analysis scripts, pinned requirements, 26 numerical outputs, the frozen NFA Edition 2026 workbook and OWID series, one historical v44 drawdown CSV, the C17 budget solver, README, `CITATION.cff`, `SHA256SUMS.txt` and the attribution notice.

**Verified for this deposit:** all three scripts ran in a clean copy of the package and regenerated the 26 deposited data files **byte-for-byte (26/26)**; both documents compile with zero LaTeX warnings (38 and 31 pages).
