# ECOMOD continuation 3 — verified change record

- **Parent derivative:** `/home/user/ecomod_v45/output_v45_ecomod_continued_2_20261026/` (35-page main / 20-page SI, itself based on the 35-page final-QA source). This new directory is separate; prior files were not overwritten.
- **Title applied to main and SI:** `Rising biocapacity total can mask ecological-capital land drawdown: a two-land model`.
- **ORCID:** linked in both main and SI to `https://orcid.org/0000-0002-0019-1842`.
- **Verified locator correction:** the Paper3 v50 PDF at the unchanged commit pin `2efaa62083f2007dec3446c15c475af88f0925f3` defines the weak/strong operating regimes in §1.1 (not §1.2); its §10.1 states the weighted-sum/componentwise-adequacy distinction. The main-text locator was updated to §§1.1 and 10.1. The commit pin and manuscript citation-key mapping remain unchanged (`2026a` governance, `2026b` assessment, `2026c` ledger).
- Paper06 v71 Theorem 4(iii) was checked verbatim in the pinned PDF: for every positive elasticity it gives a false-certification interval on diagonal gap states of the witness datum, and it concludes no positive elasticity is uniformly safe **on that witness gap region**. The current manuscript wording is scoped accordingly.
- Half-Earth remains explicitly distinguished as a spatial conservation target from the model's annual human-available-flow reservation. No broad coupled-system boom–bust or “no Allee threshold other than the floor” claim was added; SI §S4 documents the near-floor degraded equilibrium with both restoration gates inactive at balance.
- Table 2(a) was raster-checked on main PDF page 17: `E_{\mathrm{ceil}}` renders legibly. The current SI drawdown Table S4 row (`A_{c0}=0.40`, `P_0=3.5`) is `0.050`; the deposited CSV gives `0.050000000006867766`, so no pattern edit was made.
- Current SI source checks: `b_{G,c}` and `Y_c=\Upsilon_c(q)A_c` are correct; Poeplau is spelled correctly; the main-equation reference is Eq. (18); the Table S2 sensitivity reference is explicitly tied to SI §S3; previously reported truncations are complete; the main text states `\phi_0=0.128647` (about 12.86%). SI contains no `Abaee2026c` citation, so no extra SI reference was needed.
- The Paper3 metadata caveat remains: at the pin, v50 PDF is present, the manifest lists v49 article files and omits v50, the dated README gives no explicit v49/v50 label, and the v50 TeX header points to v48 Markdown.
- No Table S4 data, checksums, root sources, previous PDFs, or baseline files were modified. No archive/package was created.

Build with Tectonic 0.17.0 from this directory:

```sh
tectonic --reruns 2 --outdir . ecomod_continued_3.tex
tectonic --reruns 2 --outdir . ecomod_continued_3_SI.tex
```
