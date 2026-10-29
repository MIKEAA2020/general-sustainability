# Typed Flux Ledgers — v51 reproduction package

This directory accompanies main-text **Version 51 (29 October 2026)** and
supplementary **v19**. It does not replace or overwrite the v50/v18 files.

## Manuscripts

The manuscript sources are in the sibling `../manuscript/` directory:

- `paper3_material_ledgers_v51.md`
- `paper3_material_ledgers_v51.tex`
- `paper3_material_ledgers_v51.pdf` (compiled main text, 64 pages)
- `paper3_supplementary_v19.md`
- `paper3_supplementary_v19.tex`
- `paper3_supplementary_v19.pdf` (compiled supplementary material, 19 pages)
- `paper3_material_ledgers_v51_graphical_abstract.png` (300-dpi raster)
- `paper3_material_ledgers_v51_graphical_abstract.svg` (editable vector)
- `paper3_material_ledgers_v51_graphical_abstract.pdf` (vector, used by the TeX source)

The graphical abstract is merited because the paper's central distinction is
structural and visual: it contrasts scalar compression with a typed
stock–flow ledger, separate certification layers, and three
non-interchangeable meanings of “depletion time”. Its editable source is
`code/make_graphical_abstract_v51.py`; it is a schematic, not an additional
data claim.

Compiled PDFs are included beside the TeX sources. The sandbox used for the
final build had no system TeX installation, so the PDFs were compiled with
GlyphTeX (Tectonic/XeTeX compiled to WebAssembly; npm package
`glyphtex-engine` 0.1.0). The build used that package's TeX bundle/packs,
with TeX Live 2022 `xurl.sty` and `hyphenat.sty` and AMS/CM font-support
files supplied to the compiler's virtual filesystem. The TeX sources
themselves keep the normal unconditional `\usepackage{xurl}`; a standard TeX
Live installation containing `xurl` and `hyphenat` should build them
directly. The corresponding build logs are
`outputs/paper3_material_ledgers_v51_build.log` and
`outputs/paper3_supplementary_v19_build.log`; both builds completed with no
TeX error lines (warnings and over/underfull boxes remain in the logs).

## Environment

Outputs in `outputs/` were captured with:

- Python 3.11.2;
- NumPy 2.4.6 and SciPy 1.17.1 for the two numerical exhibits that need them;
- Matplotlib 3.10.7 for the graphical abstract.

Install the pinned third-party dependencies with:

```bash
python3 -m pip install -r requirements.txt
```

The curvature/crossover and fisheries scripts use only the Python standard
library. `certification_lp_v51.py` uses SciPy/HiGHS when available and an
exact vertex enumeration for its two-component exhibit otherwise.

## Reproduce the captured outputs

Run from this package's `code/` directory:

```bash
cd code
python3 curvature_and_crossover_v51.py
python3 fisheries_cohorts_v51.py
python3 persistence_index_simulation_v51.py
python3 certification_lp_v51.py
python3 make_graphical_abstract_v51.py
```

The corresponding captured standard outputs are:

- `outputs/curvature_and_crossover_v51.txt` — Propositions 26–28 and the
  per-row MCS 2026 reserve-life ratios;
- `outputs/fisheries_cohorts_v51.txt` — cohort sizes, ADH zero counts and
  medians; the archived formula check; the v4.66 taxonomic summary and
  identifier overlap; and the exact finite-population random-draw benchmark;
- `outputs/persistence_index_simulation_v51.txt` — the Gaussian exhibit for
  the proved Proposition 32 limiting law (400 replicates, seed 7);
- `outputs/certification_lp_v51.txt` — the Proposition 30 concealed-deficit
  exhibit, Proposition 31 witness, and certificate-vector record;
- `outputs/graphical_abstract_v51.txt` — the graphical-abstract build log.
  The figure itself is written beside the manuscripts in PNG, SVG, and PDF
  formats;
- `outputs/paper3_material_ledgers_v51_build.log` and
  `outputs/paper3_supplementary_v19_build.log` — LaTeX build logs for the
  compiled PDFs listed above.

## Data provenance

### USGS phosphate table

`data/usgs_mcs2026_phosphate_used.csv` contains only the rows used in the
main text, transcribed from the USGS *Mineral Commodity Summaries 2026*
phosphate-rock table:

<https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-phosphate.pdf>

Values are thousand metric tons. The two Australia reserve conventions are
kept as separate rows: the tabulated reserves and the footnote's
JORC-compliant-or-equivalent reserves. The report's separate world-resources
statement is not encoded as a reserves row.

### Fisheries cohort files

The three CSVs in `data/` are byte-identical copies of cohort files already
tracked in this repository:

- `fisheries_adh_archived_43.csv` — archived 43-stock cohort; ADH column
  `ADH_yr`;
- `ram_legacy_v444_adh_cohort.csv` — RAM Legacy v4.44 cohort extract; ADH
  column `ADH`;
- `ram_legacy_v466_adh_cohort.csv` — RAM Legacy v4.66 broad-cohort extract;
  ADH column `ADH`.

Their SHA-256 hashes are listed in `CHECKSUMS.sha256`. The v51 script checks
summary arithmetic on these files only.

## Explicit non-reproduction boundary

No script in this package:

1. re-derives the G3P basin rows from product masks;
2. rebuilds a fisheries cohort from a RAM Legacy source database release; or
3. recomputes National Footprint and Biocapacity Accounts edition tables.

Those are retained and labelled as source/provenance records in the main text
and supplementary S5, S5.4, and S17. They must not be described as reproduced
by this code package.

## Checksum verification

`MANIFEST.md` lists the package contents. `CHECKSUMS.sha256` uses paths
relative to the parent `paper3/latest-2026-09-19/` directory. Verify with:

```bash
cd paper3/latest-2026-09-19
sha256sum -c v51/CHECKSUMS.sha256
```

The checksum file itself is conventionally excluded from its own list.

## Principal v51 repairs

Relative to the audited v50, this revision:

- separates late return/pipeline stock from ultimate non-return in
  Definition 22 and downstream horizon statements;
- replaces the invalid first-order reserve-life crossover at large
  \(g\tau\) with the exact threshold and pins the phosphate example to one
  MCS 2026 record;
- makes the residual/conservation formulation use one total
  \(b=B_{\mathcal T}u_\partial+d_x\) with dimensionally consistent covectors;
- rebuilds ledger composition as disjoint coupling followed, when applicable,
  by a shared-stock quotient with selector initial state and donor-limited
  exchange;
- scopes Proposition 42 to typed scalar conservation readouts while allowing
  explicitly separate untyped numerical aggregates;
- separates stationary cycle closure from weak/strong assessment semantics
  and states only the proved one-way stationary bridge;
- states Proposition 30 on the nonempty feasible slice at the published
  aggregate;
- proves Proposition 32's limiting law rather than treating simulation as the
  proof;
- makes §9 closure conditional on Interface Hypothesis I and limits the
  non-reduction theorem to the defined coordinate-preserving/regular classes;
  and
- refreshes the supplementary inventory, proof-obligation pointers,
  reproduction boundary, data files, captured outputs, and checksums; and
- adds a reproducible graphical abstract in PNG, SVG, and PDF formats; and
- compiles the main and supplementary PDFs with unconditional `xurl`.
