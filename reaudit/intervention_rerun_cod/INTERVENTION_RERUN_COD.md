# Independent rerun — cod intervention-selection leg (2026-08-26)

**Scope.** The cod intervention artifacts committed in the Task-35 session (`wave_e_cod/src/run_intervention.py`, `results/intervention_results.json`, `results/intervention_boundaries.csv`) were **first-run** with independent-rerun status NONE. This record documents their rerun by a second agent session: a fresh execution of the committed runner on a clean process, verifying that the committed code deterministically reproduces the committed artifacts. The cod-side analogue of `reaudit/intervention_rerun/` (Edwards).

**Environment.** Python 3.12.13 / numpy 2.1.3 / pandas 2.2.3, x86_64 Linux (`environment.txt`) — the SAME machine, interpreter, and library versions as the original Task-35 run. **Honest scope note:** this is a second-session rerun in the same environment, not a cross-toolchain rerun (the Task-29 standard for the Part II certificates used Python 3.13.14 / numpy 2.3.5 on a different toolchain). What it verifies: committed-code reproducibility, determinism, and freedom from uncommitted state. What it does not verify: numerical stability across library versions. Given the byte-identity result and the deterministic (no-randomness) runner, the artifact claim is reproduced; the cross-toolchain standard remains available to a future rerun if the owner wants it. (The Edwards leg's rerun in `reaudit/intervention_rerun/` carries the identical scope correction — see commit 65cb597.)

**Procedure.**

1. Committed artifacts snapshotted and hashed before execution (`committed/`, hashes below).
2. `cd wave_e_cod && python3 src/run_intervention.py` executed fresh (`rerun_console.log`, exit 0, ~1.9 s, deterministic — no randomness anywhere in the runner).
3. The regenerated artifacts compared byte-for-byte against the committed snapshot.

**Result: BYTE-IDENTICAL (hash-identical) on both artifacts** (same-environment second-session rerun; see the scope note above).

| Artifact | SHA-256 (committed = rerun) |
|---|---|
| `results/intervention_results.json` | `76f31745a67120b959679190798b8115aa15e0117ea151b395dc64a8ac2be80f` |
| `results/intervention_boundaries.csv` | `cd8e97cbd967edf1398a5cf944caf306ed8cb25fc79a07d75e37126294c91d3d` |

**Headline verdicts re-observed on the rerun** (console log): fit r = 0.2369, K = 5000.0 (bound-pinned, disclosed); ε train max 460.0 kt (year 1992); OOS audit max 47.1 kt, not exceeded; UC floors −460.0 / −318.8 / −114.8 kt/yr; the erosion conversion is EXPANSIVE (contractive = False, a_max = 1.1531 > 1 — F′(K\*) > 1 at the LRP, the contraction form inapplicable), r_1 = 460.03 kt, r_5 = 3120.51 kt; the productivity negative certificate re-observed (no positive fixed point for any catch level, zero included, under UC-min/q05 — every infinite-horizon kernel empty); maximal robust flat catch 57.62 kt at UC-q10 only (0 under the harsher classes); NO POLICY RETAINED (S1/cpm strictly less protective than BAU at the boundary, nominal and certified — the mirror image of the Edwards positive result); certified horizons T = 5 across all policies and classes (beyond which the expansive erosion empties every certified kernel); every stress replay exits the LRP (min S 366.25 / 4.71 / 307.27 / 294.71 / 392.46 kt, all < 884.6); the kernel lower boundaries reproduce exactly (e.g. BAU UC-min T1 = 1141.032; S1/cpm UC-q10 T1 = 886.668, Tinf = 900.251).

**What this does and does not close.**

- CLOSED: the "first run / independent rerun NONE" limitation on the cod intervention artifacts. The runner, results, and boundary table are now `INDEPENDENT_RERUN 2026-08-26 (byte-identical, same-env second session)`. With this, **both scored systems' intervention legs are rerun-verified** — the cross-system retention-verdict contrast (Edwards positive / cod negative) is now reproduced on fresh executions of both committed runners.
- NOT CLOSED: Wave E itself (Part III paper-support rows remain NOT CONFIRMED); the APPROXIMATION status of the cod admission row (K bound-pinned; the residual's shock/model-error conflation; the expansive-form first-use boundary); the two-pool exact specialization (A005 blockers); the defect-reduction route on the Edwards side.

Files: `committed/` (pre-run snapshot), `rerun_console.log`, `rerun_hashes.txt`, `environment.txt`.
