# Governance paper v42 / supplementary material v9 — P01

Author: Amin Abaee · [ORCID](https://orcid.org/0000-0002-0019-1842)  
Revision date: 29 October 2026

## Read first

- **Main manuscript:** `manuscript/paper4_delay_dynamics_v42.pdf` — 49 pages.
- **Supplement:** `manuscript/paper4_supplementary_v9.pdf` — 14 pages; source `.md` and `.tex` included.
- **Assessment and deletion/change account:** `ELEVATION_REPORT_P4_v42_P01.md`.
- **Sources:** main TeX, `theorems_v42.tex`, supplement extension source and PDF metadata header in `manuscript/`.
- **Evidence:** versioned JSON/CSV/NPZ outputs in `data/`; scripts and 64 tests in `src/`.

This is an additive revision of the governance v41 source pinned at commit `2efaa62083f2007dec3446c15c475af88f0925f3`. Original source snapshots and inherited numerical evidence are in `inherited/`. Earlier published revisions and **ECOMOD C17 are not modified**. No deposit DOI or C17 version-specific citation is replaced.

## What is substantively new

1. Explicit RFDE second/third derivatives and interval verification of the classical nonlinear Hopf hypotheses for gated A and ungated B, covering the four reported cubic signs. All eight scalar crossing delays across both candidates/gating variants are enclosed separately.
2. An analytical impulse-response/small-gain theorem proving protective local stability for every fixed finite deployment delay and every positive exact/native review cadence, with an explicit adjustment-rate-independent margin and mathematical parameter box.
3. A nonlinear invariant-region theorem protecting a stock floor, including between reviews, on a stated admissible operating region. The exact nonlinear quota review realizes the linear review factor, rather than importing a bound from a different controller.
4. An eventual-stability theorem for a specified contractive class of review rules, replacing the invalid consistency-only inference.
5. An interval-validated mixed-channel counterexample outside the weighted small-gain region.
6. A 131-point odd-grid interior-coordinate continuation connecting the upper stable arm to two independently observed waveform captures; six 1025-node refinements and Floquet timestep checks. The noncapturing history is retained.
7. A corrected exact tether equilibrium criterion and a fully parameterized four-state Allee/bistability example certified at zero delay by interval scalar roots and Routh tests. Extinction-face attraction is distinguished from instability to positive-stock perturbations.
8. A source-traceable herring institutional-event dataset: eight events and five dependent clocks from two distinct episodes. This is temporal evidence, **not dynamic field calibration or an empirical delay distribution**.

The manuscript is a scientific account; change assessment and execution details belong to the separate report and ledgers.

## Reproduction

Python package versions are pinned in `requirements_v42.txt`. The recorded environment uses Python 3.13. TeX Live with `pdflatex`, `pandoc`, and standard recommended LaTeX packages are additionally needed for PDFs. Use one BLAS thread for the large dense Newton systems.

From this package directory:

```bash
export OPENBLAS_NUM_THREADS=1
python src/local_verification_v42.py
python src/mixed_delay_v42.py
python src/hopf_cubic_v42.py
python src/all_scalar_hopf_v42.py
python src/protective_all_cadences_v42.py
python src/tether_equilibria_v42.py
python src/empirical_events_v42.py

# Full floating continuation campaign (overwrites only this v42 output set):
python src/continue_upper_arm_v42.py data/upper_arm_inherited_seed_v42.npz 155
python src/floquet_v42.py
python src/refine_branch_v42.py
python src/nonlinear_capture_v42.py

python src/figures_v42.py
python src/build_manuscript_v42.py
python src/build_supplement_v9.py
python src/build_pdfs_v42.py
python -m unittest discover -s src -p 'test_*v42.py' -v
python -O -m unittest discover -s src -p 'test_*v42.py' -v
```

The heavy continuation/Floquet steps can be omitted when building the manuscripts from the supplied evidence files. Arnoldi starting vectors are fixed. Small platform-dependent floating differences and runtime fields are expected; they are not interval enclosures. The PDF build uses a fixed source date, and its intermediate files remain in an excluded `.cache/` directory. The manuscript builders are tested to reproduce the source files byte for byte.

`local_results_v42.json` describes what the local-spectrum script alone does not rerun; the nonlinear cubic, branch and capture calculations are performed by their separate scripts. The two inherited fold-certificate pipelines are not newly rerun in this revision. Unprefixed nonlinear-tail NPZ files preserve the initial H2 trials; the six H1/H2-prefixed tails correspond to the final six-case comparison JSON.

## Certification boundaries

- **Classical nonlinear Hopf theorem:** verified hypotheses, not a constructive finite branch-radius enclosure.
- **All-cadences/protective stock floor:** analytical results on explicitly stated model/initial-state classes; no empirical parameter confidence region is implied.
- **Global folds:** inherited finite-dimensional m=64 collocation certificates, not continuous-DDE fold certificates.
- **Periodic branch/Floquet/capture:** floating numerical convergence evidence, not validated continuum existence, full infinite-dimensional spectral enclosure, uniqueness, or complete basins.
- **Herring:** interval-censored event timing from named sources, not a fitted latent institutional controller.
- **Tether:** illustrative auxiliary parameters, not field estimates or transport of untethered thresholds.

The approved declaration appears in the main manuscript: “Arena.ai Agent Mode was used to assist with computational methods and literature review.” Prior disclosures are retained.

## Provenance and publication

`data/source_registry_v42.json` records pinned sources and hashes. Third-party full-text PDFs are **not redistributed**. `MANIFEST_GOVERNANCE_P4_v42_P01.json` hashes every published artifact except itself. The one-shot additive publisher requires an explicit `--publish` and an external credential file; no credential is included. It checks fresh main HEAD, refuses an existing version path, preserves every prior non-tree path/mode/hash, uses non-force updates, and byte-verifies the new files before publishing a separate receipt. Do not rerun an already completed publication.
