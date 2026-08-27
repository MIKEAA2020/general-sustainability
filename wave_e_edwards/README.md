# Wave E — Edwards Aquifer, San Antonio Pool

Second empirical gate of the general theory (§15 / closure Wave E).
Primary \(z\): J-17 annual-mean head. Persistence is the beating target.

```
python3 src/build_panel.py
python3 src/run_ladder.py
python3 src/make_figures.py
```

Protocol (frozen before scores): `protocol.md`.
Retention is decided only on \(z\). Comal is a post-selection fibre.
Do not pool this \(\Omega\) with Northern cod or with any phosphorus catchment.

**Frozen specification:** `SPECIFICATION.md` (Ω_SA Pass 1 + Pass 2 + the intervention-leg object; no pooling, no transfer — machine-verified at the artifact level by `reaudit/verify_wave_e_spec_match.py`, 36 checks).

**Pass 1:** persist 13.23; M1 12.84 (thin); M2m 12.28 — **beats persistence at both horizons** (17.44 vs 21.11 at h=5) but collapses to AR(1) under constant fluxes, so the win is declined on class grounds (demoted: "not extra structure"; see manuscript §5); M2 persist-\((R,P)\) 14.70 (reject); oracle 7.55.

**Pass 2:** causal \(R\) from SON Niño 3.4 / lagged CD rain / AR. Listed vs M1 by 0.02–0.13 ft; worse than persist at \(h=5\); not retained as structure. Rain oracle 10.56 (excluded). Machine-readable record: `results/pass2_meta.json` `listed_by_point_rule` vs `retained_as_structure` (the latter is empty).

**Intervention leg** (§15 intervention selection; `protocol_intervention.md`, locked before scores; `python3 src/run_intervention.py`): governance operators (BAU / flat caps / Stage-I reactive / CPM cascade) scored by robust viability kernels under declared persistent recharge floors, with the Cor2 erosion conversion invoked for the first time on a real system (`admission/R04_Cor2_edwards_kernel.md`). Verdicts: **S1 and cpm retained** (nominal, drought-floor/physical reading — reactive matches flat-cap protection at +3.3% to +50.6% water); BAU not robustly viable beyond ~14 yr under the perpetual-1956 floor (a 7.2% mean cut restores invariance); **negative certificate at the institutional threshold** (every declared policy ≡ BAU there; even zero pumping empties by T≈6–11); **certified kernels defect-bound to T ≤ 3 yr** (ε = 15.4 ft train max, exceeded OOS at 21.8 — the information-layer rent again). Independent rerun 2026-08-26: byte-identical (`reaudit/intervention_rerun/`).
