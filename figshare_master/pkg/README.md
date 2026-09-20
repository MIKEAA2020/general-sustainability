# Master Deposit — "Aggregate Indices and Transition Safety"

**Author:** Amin Abaee (ORCID 0000-0002-0019-1842)
**Deposit (figshare):** https://doi.org/10.6084/m9.figshare.33764023
**Deposited for:** *Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility* (manuscript under journal submission). Shared master deposit: the `safetransition/` subtree additionally archives the software-description submission *SafeTransition: exact rational certification of transition safety for sustainability assessment* (Environmental Modelling & Software submission; package 1.3.0). The
`manuscripts/` directory holds that submission's venue-agnostic master
manuscript, from which venue-specific versions derive.

This is the single, venue-independent master deposit for the article. It
contains all data and code generated and analysed during the study: the
exact-arithmetic verification artifact for the paper's finite rational
instance, the complete figure and graphical-abstract pipelines, the deposited
image files, and the preserved novelty-search strings. It is structured to
satisfy the data- and code-availability norms of control, systems and
operations research, and environmental modelling journals alike.

## Contents

```
verification/                                exact-arithmetic machine artifact
  typed_false_positive_instantiation.py      exact-integer verifier (25 checks)
  typed_false_positive_instantiation.json    committed results file (execution of
                                             2026-08-28; all 25 checks pass; scale 40)
  typed_false_positive_instantiation_report.md  human-readable report of the run

figure_code/                                 complete generation pipeline
  make_fig1_v40.py                           Figure 1 (floor-margin view)
  make_fig2_v35.py                           Figure 2 (weight-interval view)
  make_figures_v31.py                        Figure 3 (path view); also contains an
                                             earlier Figure 2 routine retained for provenance
  make_graphical_abstract.py                 graphical abstract (PDF + PNG)
  make_graphical_abstract_tif.py             graphical abstract TIFF (LZW, 300 dpi)
  make_benchmark_v44.py                      resource-transition benchmark: verifies
                                             the manuscript's fishery instantiation
                                             (24 exact-rational checks) and draws
                                             its figure

figures/                                     the manuscript figures (Figures 1-3 and
                                             the Section 6.3 benchmark figure)
graphical_abstract/                          graphical abstract (PDF/PNG/TIFF)
novelty_searches/                            q1..q12: companion manuscript's twelve
                                             preserved search records (the package
                                             ships its own six-query set, q1..q6)
run_all.sh                                   one-command reproduction + integrity check
SHA256SUMS                                   integrity manifest (SHA-256)
requirements.txt                             verified library versions
CITATION.cff                                 citation metadata
LICENSE.txt                                  CC BY 4.0 notice
manuscripts/                                venue-agnostic master manuscripts
  paper1_safetransition_master_v2.pdf/.tex  software description, master version
                                            (venue-neutral)
  paper1_safetransition_ems_supplementary_v6.md  supplementary material (S1-S12, incl.
                                            the 25 exact grid checks of the
                                            assessment paper's verifier)
safetransition/                             SafeTransition library, v1.3.0
  check_safe_transition_cert.py             independent stdlib-only certificate checker
  src/safetransition/                       9 modules (exact operators, recursions,
                                            certificates, indicators, dashboard)
  tests/                                    59 tests incl. certificate protocol
  examples/, figure_code/, novelty_searches/, docs/
  run_all.sh, SHA256SUMS, CITATION.cff, pyproject.toml
```

## One-command reproduction

Requirements: Python 3.9+ with the pinned versions in `requirements.txt`
(verified on numpy 2.3.5 / matplotlib 3.10.9 / Pillow 12.3.0). From the
deposit root:

```
bash run_all.sh
```

The script (i) checks the environment, (ii) verifies the SHA-256 integrity of
every deposited file, (iii) re-runs the exact-arithmetic verifier, and (iv)
regenerates every figure and the graphical abstract, comparing each output
byte-for-byte against the deposited copies. Expected conclusion:
`ALL REPRODUCTION CHECKS PASS`.

Manual equivalents:

```
python3 verification/typed_false_positive_instantiation.py   # [25/25 checks passed]
python3 figure_code/make_fig1_v40.py                         # fig1_witness_v40.png
python3 figure_code/make_fig2_v35.py                         # fig2_weight_intervals_v35.png
python3 figure_code/make_figures_v31.py                      # fig2_weight_intervals_v31.png (legacy Figure 2 output)
                                                             # fig3_path_view_v31.png
python3 figure_code/make_graphical_abstract.py               # graphical_abstract.pdf/.png
python3 figure_code/make_graphical_abstract_tif.py           # graphical_abstract.tif
```

## Determinism and what the artifact guarantees

- The verifier uses deterministic exact integer arithmetic (no floating
  point, tolerances, or randomness). Re-execution reproduces the committed
  `typed_false_positive_instantiation.json` exactly in every field except the
  wall-clock `elapsed_seconds` entry. Expected output: `[25/25 checks passed]`,
  exit code 0.
- The verifier is the single source of the witness datum: witness state
  (x, s1, s2) = (1/2, 6/5, 6/5); per-weight licensing thresholds
  rho_1 = 2/3 and rho_2 = 3/2 (with rho_1 = (2 - s1)/s2 and
  rho_2 = s1/(2 - s2) at the witness floors); worst-case dip depth 2;
  gain vector e = (1/4, 1/4); bridging cost c = 1; action menu
  {NO-SWITCH, FAST, SLOW, STAGED}.
- All figures and the graphical abstract regenerate byte-identically in the
  pinned environment (the reproduction script pins the timestamp source for
  PDF metadata). `OUT` paths in the scripts are relative; run them from any
  working directory.

## Mapping to the article

- `verification/` is the "accompanying software artifact" of the manuscript's
  *Machine verification* subsection: it checks the finite rational instance of
  Proposition 3, Proposition 4, Theorem 5, and Remark 6 — the action
  classifications, the region identities, and the accepted-set identities on
  the 31^3 = 29,791-state grid over (x, s1, s2), with a finite verification
  set containing rho_1, rho_2, and their midpoint for every enumerated grid
  state — and all 25 checks pass. The check-by-check enumeration is Section S8
  of the article's Supplementary Material; the artifact's internal labels for
  the checked statement groups are "Theorems A, B(1)–(7), C". (Section numbers
  may shift slightly across manuscript versions; the section titles are
  stable.)
- `figure_code/` + `figures/` reproduce Figures 1–3 of the manuscript;
  `figure_code/make_graphical_abstract*.py` + `graphical_abstract/` reproduce
  the graphical abstract.
- `figure_code/make_benchmark_v44.py` + `figures/fig_benchmark_v44.png` are
  the manuscript's resource-transition benchmark (the section titled "A
  resource-transition benchmark"): running the script re-verifies, in exact
  rational arithmetic, every quota, stock, margin, index, and fund value
  quoted there, and regenerates its figure byte-identically.
- `safetransition/` is the SafeTransition library (v1.3.0) of the software-description
  manuscript *SafeTransition: exact rational certification of transition safety for
  sustainability assessment* (Environmental Modelling & Software submission): typed
  operators on exact or certified conservative tubes, state and belief recursions,
  serializable Farkas certificates verified by an independent checker importing no
  library modules, the complete weight-partition certificate, belief-failure
  certificates, and the twenty-four exact benchmark checks re-deriving
  `figure_code/make_benchmark_v44.py`'s values. Its `run_all.sh` (seven steps:
  tests, benchmark, certificate protocol, examples, quick scaling sweep,
  adversarial exactness instance, figures) reproduces all of it; see its README.
- `manuscripts/` holds the venue-agnostic master manuscript of the
  software description and its supplementary material; venue-specific
  submission payloads derive from it.
- `novelty_searches/` documents the systematic searches behind the
  related-work assessment (queries, sources, dates); they are also suitable
  for separate preservation on searchRxiv.

## How to cite this deposit

Abaee, A. (2026). *Verification code and figure pipeline for Aggregate
Indices and Transition Safety: A Quantifier-Order Separation Between
Scalarized and Coordinate-Wise Feasibility*. figshare.
https://doi.org/10.6084/m9.figshare.33764023

For the `safetransition/` subtree: Abaee, A. (2026). *SafeTransition:
exact rational certification of transition safety for sustainability
assessment* (software description). Archived in the same deposit,
https://doi.org/10.6084/m9.figshare.33764023.

## License

CC BY 4.0 — see `LICENSE.txt`.
