# ECOMOD C19 A01 — companion DOIs and editorial main/SI division

**Main manuscript:** [ecomod_C19_A01_main.pdf](ecomod_C19_A01_main.pdf) — 39 pages  
**Supplementary Information:** [ecomod_C19_A01_SI.pdf](ecomod_C19_A01_SI.pdf) — 31 pages  
**Placement rationale and complete change account:** [EDITORIAL_DIVISION_C19_A01.md](EDITORIAL_DIVISION_C19_A01.md)  
**Data attribution:** [DATA_LICENSE_C19_A01.md](DATA_LICENSE_C19_A01.md)

C19 is an additive editorial revision of published C18 A01. C18, C17, unrelated companions, numerical evidence, and all earlier versions remain unchanged.

## What changed

- Replaced the cited companion working-paper records with DOI links:
  - `Abaee2026a` → `10.20944/preprints202610.3095.v1`
  - `Abaee2026b` → `10.20944/preprints202610.2983.v1`, including its new posted title
  - `Abaee2026c` → `10.20944/preprints202610.3123.v1`
- Updated the three main records and the two cited SI records. No unused SI record was added for `Abaee2026c`.
- Replaced older working-version theorem/section locators with content-based companion locators; claim scope is unchanged.
- Made all **18 SI tables and 5 SI figures** explicitly cited at relevant main-text points.
- Kept every core model equation, proposition, essential numerical result, empirical finding, conclusion, and limitation in the main.
- Removed the duplicated main yield-sweep panel while retaining all values in SI Table S3; replaced four duplicated main proofs with concise sketches while retaining full SI derivations; compressed repeated numerical diagnostics and Discussion numbers without deleting evidence.
- Kept comparator experiments, full grids, sensitivities, endpoint witnesses, full budgets/refinement, and operational protocols in SI. No new SI results or extended discussion were introduced.

The main has three multi-panel figures (eight panels) and six tables. Auxiliary comparator/control figures were not promoted merely to increase the main figure count.

## Provenance and package scope

`inherited_C18/` holds the exact frozen C18 sources used by the deterministic transform. Source diffs are in `evidence/source_diff_{main,SI}_C19_A01.patch`.

This is deliberately a lean package, not another 27 MB copy of the complete C18 historical archive. It contains the required executable inputs, selected C17 dependencies, current numerical outputs, figure assets, and numerical evidence. `metadata/inherited_artifact_provenance_C19_A01.json` verifies **66 inherited files** byte-for-byte against published C18 commit `688701d6053ea1d89a37b9c708ef29c9b2e8ddf5`. The complete C18 archive remains preserved at its original local and remote paths.

C18 filenames on numerical scripts, data, and figures are intentional: those artifacts are byte-inherited. C19 document/build/test files use the C19 suffix. `requirements_C19_A01.txt` adds `pypdf` for actual PDF checks. `DATA_LICENSE_C19_A01.md` corrects package-specific paths while preserving attribution.

The full legacy 28-trajectory budget-rerun workflow remains in C18. C19 preserves its PASS evidence and tests it, but does not duplicate the full C17 archive merely to rerun an already completed check.

## Reproduce offline

Install `requirements_C19_A01.txt` in your own environment. LaTeX compilation requires `pdflatex`, `elsarticle`, and the standard packages used in the sources (`texlive-latex-extra` and `texlive-publishers` on Debian).

### Numerical pipelines

```sh
python code/reproduce_empirical_C18_A01.py
python code/reproduce_two_land_C18_A01.py
python code/reproduce_comparator_C18_A01.py
```

To test all three in a disposable copy without altering the frozen package outputs:

```sh
python code/verify_reproduction_C19_A01.py
```

The completed C19 check passed: **26/26 numerical data files byte-identical**, **3/3 PNG figures byte-identical**, and **7/7 PDF figures matched in geometry and extracted content**. PDF container hashes may change because generation metadata changes.

### Documents and tests

```sh
bash code/build_documents_C19_A01.sh
python code/test_revision_C19_A01.py
python -O code/test_revision_C19_A01.py
```

The build applies exact-anchor transformations to the frozen C18 sources and runs three LaTeX passes per document. The tests cover inherited hashes, numerical expectations, DOI mapping, content-based locators, main/SI placement, all SI-float citations, actual PDF pages/text/URI links, LaTeX logs, and live-reproduction evidence.

Final result: **60/60 tests pass in normal mode and 60/60 in optimized mode**. Main/SI have zero LaTeX warnings, zero overfull boxes, and no unresolved references or citations.

## Scientific boundary

The editorial revision does not change the study’s scientific boundary. NFA/OWID calculations reproduce account decompositions; they do not identify a global ecological-capital stock or validate the coupled ecological dynamics. Model parameters remain representative rather than fitted. No physical-stock composite, field validation, causal identification, or new empirical claim is introduced.

NFA inputs and NFA-derived outputs retain **CC BY-SA 4.0** attribution to Lo et al. (2026); OWID/FAOSTAT attribution and provider terms are retained. No provider endorsement is implied.

No cleanup, deletion, branch merge, or change to companion manuscripts/deposits is part of C19. The C19 publisher is a one-shot additive tool: **do not rerun it after successful publication**; the separately archived receipt is the publication record.
