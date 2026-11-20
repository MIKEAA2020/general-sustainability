# v46 → EM: what still has to change, and what does not

Status of v46: main **40 pp**, SI **31 pp**, portal-safe main **39 pp**, 0 errors, 0 undefined
references. Methods-onward byte-identical to C20. Numbers removed: none.

## A. Requires re-upload (5 items of the 13)

| # | File | Change | Note |
|---|---|---|---|
| 1 | `Manuscript_ECOMOD_v46_portalsafe.tex` | new title, new 238-word abstract, merged §1 | portal-safe verified at **39 pp** with no assets |
| 2 | `ecomod_v46_main.pdf` | **40 pp** (was 38) | re-check the portal's own PDF if it recompiles |
| 3 | `ecomod_v46_SI.pdf` | **31 pp**, unchanged length | SI title line now matches the new main title; a one-line diff |
| 4 | `Supplementary_Information_..._portalsafe.tex` | **needs regeneration** if the SI title line is to match in the portal build — the only SI change is that one line | not yet generated as portal-safe |
| 5 | `Highlights_v46.txt` | 5 bullets, max 80 chars | one bullet now names the identifiability result |

## B. Unchanged — do not re-upload

`Figure_1–3.pdf`, `Figure_S1–S5.pdf` (all figures identical), cover letter, response to reviewers,
declaration of competing interests, GA `.tiff`, DATA_AVAILABILITY, REPRODUCTION_GUIDE,
FIGURE_CAPTIONS, `LaTeX_dependencies/`.

## C. Requires a decision, not a file

**Zenodo.** The deposit `10.5281/zenodo.24092131` reproduces **C20**, whose title/abstract differ from
v46. Options:
1. **New version of the same record** (recommended if v46 is accepted): the concept DOI stays
   `10.5281/zenodo.24092131`, the version DOI increments. Scripts and data are unchanged, so only the
   packaged manifest/README and the title need refreshing.
2. New standalone record: correct but fragments the citation trail for a paper that is one revision
   away from its deposit.
3. Leave as is: honest only if the paper of record stays C20.

**Preprint.** Still `10.20944/preprints202611.0852.v1` (C20). A v46 preprint version is a separate
decision; the "doi takes a few days" rule applies to any new version DOI.

## D. Caveat that must be stated, not discovered later

**The falsifiable content of v46 is in SI §S11, not in the main text.** v42 carried a compact
prediction list in the main body; C20 moved it to SI Table S18 + SI §S11 and kept only a summary line
in §4.5. v46 keeps C20's arrangement (restoring the predictions to main would change Methods-onward,
which I held fixed). If you want them back in the main text, that is a deliberate structural change
and a separate build.

## E. Also not done, by design

- No recompiled PDF with the figures present at final size (portal build tested with and without).
- No change to `CHANGE_RECORD_C20_A01.md`, `artifact_manifest_C20_A01.json`, or the Zenodo
  `SHA256SUMS.txt` — all three describe C20 and become stale only when v46 is actually submitted.
- No replacement of `ecomod_C20_preprints_source_20261031.zip`: it is the C20 source archive and should
  stay as the record of what was posted.
