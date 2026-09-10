# Journal-Zip Compilation — Findings & Deliverables

**Date:** 10 Sep 2026
**Scope:** `arena agent 1` papers, `MIKEAA2020/general-sustainability@main`
**Source tree:** `/home/user/gs_clone/arena agent 1/paper rewrites/`
**Deliverable zips:** `/home/user/journal_submission_zips/*.zip`

---

## 1. Is there a newer Paper 1 figure? Should the reference change? — **NO.**

The reference is **correct as-is** and should **not** be changed.

- `paper1_assessment_separation_v23.tex` line 894 references `figs_p1/fig1_witness_v22.png`.
- **No newer figure exists.** The only two files in `figs_p1/` are:
  - `fig1_witness.png` (1920×880, older / pre-regeneration)
  - `fig1_witness_v22.png` (1906×865, **newer** — this is the one referenced)

  The `v22` suffix marks the regenerated version. Git history confirms it: commit `d56b297` (Batch-8, "nine new versions … + three regenerated figures … P1 fig1_witness_v22") explicitly lists **`P1 fig1_witness_v22`** as the *regenerated* figure. The un-versioned `fig1_witness.png` is the superseded predecessor. There is **no** `fig1_witness_v23`+ on disk or in history.

- So the reference is pointing at the **newest** figure. Keep line 894 as `figs_p1/fig1_witness_v22.png`.

For completeness, the other versioned figures were also checked — all references point to the **newest** variant:
| Paper | Referenced | Other(s) on disk | Latest? |
|---|---|---|---|
| p5 | `figs_p5/fig1_crossing_record_v25.png` | `…_v24.png`, `…_v25.png`, plain `…_v25`? | v25 is newest (commit `a75021e2` added it) |
| e2 | `figs_e2/fig2_kernel_vs_catch_v21.png` | plain `fig2_kernel_vs_catch.png` | v21 is newest |
| p4 | `figs_p4/fig2_five_regime_topology_v2.png` | plain `…_topology.png`, `.py` | v2 is newest |

No reference points to a stale figure.

---

## 2. Does the zipped latex+figures compile? — **YES, it already works.**

The `\graphicspath{{../}}` + `figs_pX/…` structure is **not broken**. Two facts:

1. **The original "figure not found" was a missing-file-on-disk error**, not a LaTeX source error. The repo contains every referenced figure; it compiles clean.
2. **`\graphicspath{{../}}` is robust in the journal layout.** Even when the `.tex` sits at the zip root with `figs_p1/` as a sibling (a "flattened" layout), LaTeX's search still finds `figs_p1/…` because the current working directory is always searched as a fallback. Verified: all 7 papers compile (rc=0) in **both** layouts.

**Conclusion:** no edit to the `.tex` is required. The existing `\graphicspath{{../}}` works whether the journal compiles from the repo structure (`latex/` + sibling `figs_*`) or from a flattened zip (`tex` + sibling `figs_*`).

> Optional hardening (not required): changing `\graphicspath{{../}}` → `\graphicspath{{./}{../}}` would make the search explicit in both layouts with zero downside, for journals that strip the working-directory fallback. Left as-is since the default already works.

---

## 3. Do p2, p5, e1, e2, e3, e4 compile? — **ALL YES (rc=0).**

Every target paper compiles clean from the faithful repo tree, with the correct number of embedded figures:

| Paper | tex | pages | embedded figures |
|---|---|---|---|
| p1 | `paper1_assessment_separation_v23` | 23 | 1 |
| p2 | `paper2_obstruction_calculus_v13` | 21 | 0 (no figures by design) |
| p5 | `paper5_sampled_governance_v26` | 29 | 1 |
| e1 | `paperE1_cod_forecast_ladder_v15` | 20 | 4 |
| e2 | `paperE2_cod_intervention_v22` | 19 | 7 |
| e3 | `paperE3_edwards_forecast_ladder_v16` | 16 | 5 |
| e4 | `paperE4_edwards_intervention_v14` | 14 | 1 |

Each figure count matches its `\includegraphics` count exactly — **no missing figures, no broken paths, no "figure not found" errors.**

---

## Deliverable: ready-to-submit zips

`/home/user/journal_submission_zips/` — one zip per paper, each containing the `.tex` at the zip root plus **only the figures it references** (stale figures like the pre-regeneration `fig1_witness.png` were excluded):

```
paper1_assessment_separation_v23.zip   (172K)
paper2_obstruction_calculus_v13.zip    ( 32K)  — tex only, no figures
paper5_sampled_governance_v26.zip      (104K)
paperE1_cod_forecast_ladder_v15.zip    (348K)
paperE2_cod_intervention_v22.zip       (580K)
paperE3_edwards_forecast_ladder_v16.zip(468K)
paperE4_edwards_intervention_v14.zip   (124K)
```

**Every zip was unzipped to a fresh directory and recompiled with tectonic → exit 0**, page counts and embedded-figure counts as above. They are submission-ready.

---

## Summary of actions
- Cloned authoritative repo into `/home/user/gs_clone` (full figure tree).
- Enumerated all `\includegraphics` and `\graphicspath` across 7 papers; cross-checked every reference against figures on disk — **all resolve**.
- Confirmed the P1 reference already targets the newest figure (`fig1_witness_v22`), with git-history proof; **no change needed**.
- Compiled all 7 papers in the faithful repo layout AND in a flattened zip layout (tectonic, rc=0), and verified embedded-figure counts via pymupdf.
- Built trimmed, submission-ready per-paper zips and re-verified each after a clean unzip.
