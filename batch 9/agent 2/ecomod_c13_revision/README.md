# ECOMOD — C13 working revision

**29 October 2026 · Separate revision from pinned C12 · M1 + M2 only**

## Read first

- **Main manuscript:** [ecomod_continued_13_revision_draft_20261029.pdf](ecomod_continued_13_revision_draft_20261029.pdf)
- **Supplementary Information:** [ecomod_continued_13_revision_draft_20261029_SI.pdf](ecomod_continued_13_revision_draft_20261029_SI.pdf)
- Matching `.tex` sources and baseline-to-C13 `.patch` files are supplied.
- [Change log](CHANGELOG_C13.md), [provenance](PROVENANCE.json), and [validation/build report](VALIDATION_REPORT.md).

This is an **AI-assisted working revision requiring author verification and approval**, not a statement of submission, acceptance, or complete validation. C12 and the earlier/submitted documents are not overwritten. C12 was read at commit `65c8464a3cf83d9aef525cb6695668898de18ac6` on its existing working branch; that branch was not merged.

## What changed

**M1 — quantitative static identification.** New main Section 3.5 / Proposition 4 / Table 3, and SI S9, give sharp compatible-area intervals under stated independently known yield and land restrictions. An exact model-scale example narrows the interval from `[0.05, 1.658163…]` ha using B alone to `[0.606061…, 0.8]` ha when fast-land area is independently known, and to one feasible point when quality is independently known. The intervals are deterministic static sets: not confidence intervals, dynamic reachability sets, or physical-stock estimates from NFA.

**M2 — actually computed integrated budgets.** New main Section 3.6 / Table 4 and SI S10 / Tables S15–S17 integrate five signed RHS channels in four existing cases: frozen demand (F100), endogenous recovery (R400), and the existing no-wave/wave pair (N250/W250). Fast-yield change is additionally split into technology and debt. Seven nested timesteps from `0.05` through `0.00078125` yr produce 28 runs. Independent trapezoidal RHS integrals are compared with endpoint changes, without balancing adjustments. All 28 trajectories were also recomputed in memory by the verification script and matched the supplied outputs.

| Case | Endpoint ΔB (gha) | Signed closure residual (gha) | Absolute relative residual |
|---|---:|---:|---:|
| F100 | 0.231310094 | 0.000080398 | 0.0348% |
| R400 | 0.312763632 | 0.000196547 | 0.0628% |
| N250 | 0.068790534 | 0.000009860 | 0.0143% |
| W250 | 0.217024564 | 0.000008251 | 0.00380% |

Residual = endpoint change minus sum of independently integrated channels. These are finite-step numerical checks, not rigorous trajectory error bounds. The initial five-step ladder failed the chosen 0.1% relative closure tolerance in F100/R400; two further halvings were run and all steps are disclosed.

**No M3:** no new delay/history experiment, controller, empirical proxy, physical-stock claim, parameter intervention, or new horizon. Existing cap-degeneracy and delay-history qualifications remain. Numerical refinement of existing cases is not a history-robustness claim.

## Reproduce the new calculations

Python 3 with NumPy and Matplotlib is needed for computation; pypdf supports PDF inspection.

```sh
python -m pip install -r requirements.txt
python code/compute_c13.py
python code/verify_c13.py --full
```

Run these from the package root. The first command regenerates M1 outputs, all 28 M2 integrations, six TeX row fragments, reporting-grid trajectories, and the existing S8 wave illustration. The verifier checks algebra, witnesses, CSV consistency, endpoint/cumulative exports, guards, closure refinement, and the original printed wave peaks; `--full` additionally recomputes all 28 trajectories without replacing their CSV files. This reconstruction is **not recovered original author simulator code**.

The quadrature uses every simulation node. The trajectory CSV is only a `0.05` yr reporting-grid export (20,004 data rows across four cases). Full-precision budget components, signed closure errors, cap/guard diagnostics, nested-grid differences and execution-library versions are in `data/`. The fine-step time convention, common no-wave prehistory, and quality projection/clipping are stated in SI S10 and the code. No network access or external dataset is needed for these new calculations.

Recomputation should reproduce numerical results within floating-point tolerance, not necessarily byte-identical PDFs: PDF timestamps and TeX/font versions can change binary hashes. The manifest authenticates the delivered files, not future compilations.

## Compile the manuscripts

A working TeX installation with `latexmk`, `elsarticle`, `amsmath`, `booktabs`, `graphicx`, `natbib`, `hyperref`, `enumitem`, `longtable`, `placeins`, and the usual recommended fonts is needed. The build used TeX Live 2025 plus CM-Super fonts. On a Debian-based system the relevant packages are `texlive-latex-extra texlive-publishers texlive-fonts-recommended cm-super latexmk`.

```sh
bash code/build.sh
```

All eight figure dependencies are supplied locally. Compiled deliverables are 40 pages (main) and 27 pages (SI). No unresolved citations/references, missing assets, or overfull boxes remain in the final logs. Four inherited nonfatal author-metadata PDF-string warnings remain in the main build; see the validation report.

## Inherited material and evidence limits

Seven figure assets were recovered from an exact repository file or embedded images in released PDFs, with file hashes, page/image-object identifiers, and origin commit/release recorded in `PROVENANCE.json`. The four one-stock images retain their existing comparator role and were not newly simulated. The eighth figure, the already specified S8 technology-wave illustration, was freshly rendered from the new reconstruction at its original `0.05` yr step and reproduces its printed peak values.

**Compilation completeness is not comprehensive validation of inherited research.** The empirical NFA/OWID analyses, their historical claims, the full old parameter grids, other restoration experiments, and all inherited figures were not rerun as part of C13. M2 is within-model bookkeeping, not empirical causal attribution. All earlier evidence-scope restrictions remain.

## Integrity and publication

`artifact_manifest.json` records SHA-256 and byte size for every supplied package file except itself. The publication adds only this new directory under `batch 9/agent 2` on repository `main`, without merging the C12 branch or rewriting existing paths. Scratch downloads, prior release archives, credentials, TeX intermediates, and caches are not part of this package.
