# Zenodo v2 — new version of record 24092131 (concept 24092130)

**Status: package built and verified. Not published — Zenodo needs an API token I do not have.**

## What is ready

`ECOMOD_v46_reproduction_package.zip` — **6,022,109 B**, md5 `4db04f070990eeed33cb46cb6794c320`

Built as a new version of record **24092131** (concept DOI `10.5281/zenodo.24092130`), so the citation
chain stays intact: the concept DOI resolves to the latest version, and v1.0 remains retrievable.

### What changed from v1.0
- `manuscript/` → v46 main (40 pp) and SI (31 pp)
- `README.md` and `zenodo/zenodo_metadata.json` → new title, version "2.0 (ECOMOD v46)", date 2026-11-13
- `zenodo_metadata.json` related identifiers → added `10.5281/zenodo.24092131` as **isNewVersionOf**
- **code/ and data/ unchanged**; no recomputation, no re-derivation

### Verified before upload
- all three reproduction scripts run offline, exit 0, from the repacked zip
- the package contains the merged v46 manuscript (title, orchard/hen prose, identifiability sentence
  confirmed present in the shipped `.tex`)
- decimal-number diff of the manuscript vs C20: **none removed**, only `0.548` / `0.231` added
  (the rounded abstract forms; exact values remain in §3.6)

## Publish it — web route (2 minutes)

1. Open https://zenodo.org/records/24092131 → **New version**
2. Delete the old file; upload `ECOMOD_v46_reproduction_package.zip`
3. Set **Version:** `2.0 (ECOMOD v46)` ; **Publication date:** `2026-11-13`
4. Title (paste):
   `Reproduction package for: Rising biocapacity, falling ecological capital: how aggregation conceals composition`
5. Keep the same creators, licence (CC BY 4.0), keywords, description and the three existing related
   identifiers; the `isNewVersionOf` link is added automatically by Zenodo on a new version.
6. **Publish**, then copy the new version DOI.

## Publish it — API route

Requires a Zenodo personal access token with `deposit:write` (and `deposit:actions`):

```bash
export ZENODO_TOKEN=...            # do not commit
# 1. open a new version of the existing record
NEW=$(curl -s -X POST -H "Authorization: Bearer $ZENODO_TOKEN" \
  https://zenodo.org/api/deposit/depositions/24092131/actions/newversion)
DEP=$(echo "$NEW" | python3 -c "import json,sys;print(json.load(sys.stdin)['links']['latest_draft'].rsplit('/',1)[1])")
# 2. clear v1 files
for f in $(curl -s -H "Authorization: Bearer $ZENODO_TOKEN" \
   https://zenodo.org/api/deposit/depositions/$DEP/files | python3 -c "import json,sys;[print(x['id']) for x in json.load(sys.stdin)]"); do
  curl -s -X DELETE -H "Authorization: Bearer $ZENODO_TOKEN" https://zenodo.org/api/deposit/depositions/$DEP/files/$f
done
# 3. upload the new package
curl -s -X POST -H "Authorization: Bearer $ZENODO_TOKEN" \
  -F "file=@ecomod_zenodo_v2/ECOMOD_v46_reproduction_package.zip" \
  "https://zenodo.org/api/deposit/depositions/$DEP/files?name=ECOMOD_v46_reproduction_package.zip"
# 4. metadata
curl -s -X PUT -H "Authorization: Bearer $ZENODO_TOKEN" -H "Content-Type: application/json" \
  -d @ecomod_zenodo_v2/zenodo_metadata_api.json \
  https://zenodo.org/api/deposit/depositions/$DEP
# 5. publish
curl -s -X POST -H "Authorization: Bearer $ZENODO_TOKEN" \
  https://zenodo.org/api/deposit/depositions/$DEP/actions/publish
```

`zenodo_metadata_api.json` in this folder is already shaped for that PUT (`metadata` wrapper, no
`prereserve_doi`).

## Two things to decide before publishing

1. **Preprint.** The record points to `10.20944/preprints202611.0852.v1`, which is C20. If v46 becomes
   the manuscript of record, that relation should point at the v46 preprint version, and the
   `isSupplementTo` link needs updating in the same edit — otherwise the dataset claims to supplement a
   manuscript whose abstract it no longer matches.
2. **Version label.** "2.0" is used here to mean *second deposited version*. If you would rather keep
   the deposit at 1.x because the code and data are unchanged and only the manuscript moved, say so and
   I will relabel to `1.1 (ECOMOD v46)` — but 2.0 is defensible, since the packaged manuscript changed.
