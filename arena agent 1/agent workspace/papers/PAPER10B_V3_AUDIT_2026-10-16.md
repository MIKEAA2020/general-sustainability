# Paper10b v3 version, analysis, and reproducibility audit

- Date: 2026-10-16
- Base edition: preserved `paper10b_edwards_aquifer_v2.tex`
- Intended destination: `e2-v3-source-year`, under `arena agent 1/agent workspace/papers/`
- Base branch head at pre-numbering scan: `248e8b9f7969`

## Version currency and lineage

Before finalizing the edition number, a blob-filtered, shallow, no-checkout scan inspected all 8 current refs: six branches (`archive/paper3-v48-workspace`, `e2-v3-source-year`, `edwards-framework-e1`, `edwards-framework-e1-audit-implementation`, `lean-audit-v4`, `main`) and two tags (`compendium-v1.0`, `edwards-framework-e1`). The only Paper10b-named manuscript paths were v1 and v2 on `e2-v3-source-year`; no v3 existed on any scanned ref. The current `VERSION_CURRENCY.md`, `PAPER10_SPLIT_AND_PRIOR_ART.md`, and v2 audit were reviewed. The same-study E4 v16 lineage and the v1-to-v2 split history remain as previously documented. V2 is preserved unchanged; v3 is the next edition. Release ZIP payloads were not unpacked or audited in this check.

## V3 changes

- Adds a post-freeze coefficient-sensitivity extension to Section 3.7 and Table 7 at the 660-ft institutional threshold. It does not modify the frozen protocol or re-score the retention rule.
- Extends the existing residual-bootstrap policy table to report refit shares above both 618 ft and 660 ft. Flat-60% and CPM are now reported separately because their bootstrap spreads differ even though their point attractors coincide.
- Reframes the 660-ft result as a point-fit theorem application whose positive-margin premise is not robust to the coefficient bootstrap. The algebraic comparison theorem itself remains conditional and exact; the bootstrap does not estimate field-safety probabilities, recompute viability kernels, test the live 10-day CPM algorithm, or exhaust all possible state-dependent pumping sequences.
- Tightens the prior-art/novelty language: the contribution is framed as the applied, protocol-frozen comparison and its declared geometry, not as a new viability theorem or a blanket claim that earlier work ignored trigger geometry.
- Adds a reproducible source package with the annual panel, runner, README, and generated CSV summaries.

## Reproduced sensitivity

The source script follows the existing E4 audit method: OLS of annual head on an intercept, recharge, pumping, and lagged head for the 1934–1990 training transitions; iid resampling of fitted residuals; 5,000 refits; seed `20260905`; fixed UC-min recharge `R=43.7`; and the existing 500-step policy iteration from 650 ft.

For zero pumping, the point-fit attractor is 647.32 ft (12.68-ft margin below 660). Across the 5,000 refits, the attractor's 5th/50th/95th percentiles are 628.99/647.33/661.16 ft; 344/5,000 (0.0688) are at or above 660 ft. The existing 618-ft share reproduces at 4,947/5,000 (0.9894). All refits are contractive (`0<a<1`) and have negative pumping coefficients (`gamma<0`). For BAU, flat-90/80/70/60/50, S1, and CPM, the tested iterated attractor is at or above 660 ft in 0/5,000 refits; zero pumping is the only tested policy with a nonzero share.

These are conditional bootstrap shares under the fitted structure, selected training window, iid residual resampling, and fixed floor—not probabilities of actual aquifer outcomes. The positive-margin hypothesis at 660 ft is therefore not coefficient-robust under this sensitivity. This does not change the frozen, point-fit retention score.

## Reproducibility package

Directory: `paper10b_edwards_aquifer_v3_src/`

- `annual_panel.csv` — source panel copied from `wave_e_edwards/data/annual_panel.csv`; SHA-256 `d6d725db57af5c820d3f62506aa2d5fcd862da3206824d0fa8beb06478706019`.
- `verify_660_attractor_bootstrap.py` — reruns the bootstrap and asserts the key result and the existing 618-ft cross-check.
- `policy_attractor_bootstrap_660.csv` — one row per policy with point attractor, bootstrap moments/quantiles, and shares above both thresholds.
- `zero_pumping_660_bootstrap.csv` — focused zero-pumping summary, including panel hash and scope note.
- `README.md` — method, invocation, outputs, and limitations.

Running `python verify_660_attractor_bootstrap.py` twice reproduced byte-identical CSV outputs. The manuscript Table 7's nine policy rows were checked against the generated policy CSV.

## Static verification and limitations

- Python syntax check passed.
- LaTeX static checks passed: one document skeleton, 18 unique labels, no unresolved explicit references, balanced environments/braces/math delimiters, one Table 7, and nine table rows matching the bootstrap CSV.
- No TeX engine is installed in the workspace; no PDF compilation is claimed.
- The post-freeze sensitivity is not part of the dated intervention protocol and does not alter its retention result.
