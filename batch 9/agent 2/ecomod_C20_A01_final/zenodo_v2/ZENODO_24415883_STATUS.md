# Zenodo 24415883 — verified against the published record

**Concept DOI** `10.5281/zenodo.24092130` → resolves to **24415883** (latest)
**Version DOI** `10.5281/zenodo.24415883` · **superseded** `10.5281/zenodo.24092131` (v1.0, marked "newer version" by Zenodo)

## File: correct

| | ours | published |
|---|---|---|
| name | `ECOMOD_v46_reproduction_package.zip` | same |
| size | 6,022,335 B | 6,022,335 B |
| md5 | `6425f8a2bae6af83e2423fae12e0a992` | `6425f8a2bae6af83e2423fae12e0a992` |

The exact package that was audited is what is deposited. Reference the **concept DOI** in the
manuscript — that is the stable citation, and it now resolves to 24415883.

## Four metadata defects (metadata only — the file and its DOI are unaffected)

1. **Title still v1.0.** `Reproduction package for: A rising biocapacity total can mask ecological-capital land drawdown: a two-land model`
   → should be `…for: Rising biocapacity, falling ecological capital: how aggregation conceals composition`.
   Zenodo copies the parent title on "New version" unless it is overwritten.
2. **No version number.** Field is empty; should read `2.0 (ECOMOD v46)`.
3. **Description is broken HTML.** It was pasted pre-escaped, so the page renders visible markup:
   `<p><span class="objectBox objectBox-string">&lt;p&gt;&lt;strong&gt;…` — the opening tags appear as
   text, and an anchor is nested inside another anchor's `href`, which mislinks the Preprints.org URL.
   It also still says the manuscript is **38 pp**; v46 is **40 pp**.
4. **Duplicate provenance links.** `isNewVersionOf` appears twice — once to `24092131` (correct) and
   once to `22554480` (the v35 preprint, wrong relation). **`isRelatedTo` is not a Zenodo relation
   at all** — the vocabulary returned by `/api/vocabularies/relationtypes` has 34 terms and it is not
   among them. Remove the row; there is no replacement link needed.
   `isSupplementTo` also still points at the **C20** preprint `10.20944/preprints202611.0852.v1`;
   that is fine if the preprint is not being revised, but it should be a conscious choice.

## Fix — web route (record is published; metadata edits are allowed without a new version)

Open https://zenodo.org/records/24415883 → **Edit** → paste from
`zenodo_metadata_CORRECTION_24415883.json`:
- Title, Version `2.0 (ECOMOD v46)`, Publication date `2026-11-21`
- Description: use the text in `DESCRIPTION_CORRECTED_24415883.html` (clean HTML, 6 paragraphs, 40 pp)
- Related identifiers: three rows —
  `isNewVersionOf → 10.5281/zenodo.24092131` (Dataset),
  `isSupplementTo → 10.20944/preprints202611.0852.v1` (**Preprint**),
  `isIdenticalTo → https://github.com/MIKEAA2020/general-sustainability` (**Software**).
  Delete the second `isNewVersionOf → 22554480` row outright.
- **Save** (do not "Publish new version").

## Fix — API route

```bash
export ZENODO_TOKEN=...
DEP=24415883
curl -s -X PUT -H "Authorization: Bearer $ZENODO_TOKEN" -H "Content-Type: application/json" \
  -d @ecomod_zenodo_v2/zenodo_metadata_CORRECTION_24415883.json \
  https://zenodo.org/api/deposit/depositions/$DEP
```
Then confirm with `curl -s https://zenodo.org/api/records/24415883` and check that
`metadata.description` contains no `&lt;`.

## Optional: replace the file too

The deposited zip is complete and internally consistent, but it was built **before** two later edits:
the §1 sentence fix ("The bookkeeping is that of any productive stock") and the Data-availability
line now citing the concept DOI + 24415883. So the zip's manuscript is one sentence behind the
current build. If you want the deposit to match the working tree exactly, upload
`ECOMOD_v46_reproduction_package.zip` from this folder as a replacement file
(**md5 `fa07bf70b8e0a57565de965fb6c5ba99`**, 6,022,558 B, 61/61 checksums verified).
Not required — metadata-only fixes leave a self-consistent record.
