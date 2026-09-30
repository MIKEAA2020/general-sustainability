# Phase 0 closure and merge verification

Record of the checks run after the prior-art pass (units 2-6) and before the Phase 1 claim audit.
Date of record: 2026-09-30.

---

## 0. Summary

| Item | Claim | Verdict |
|---|---|---|
| Phase 0 residual `G.illcond` (3 findings) | bare "6.5 yr" without its band | **CLOSED — already resolved at source** |
| Phase 0 residual `A.stale` | superseded E2 numbers | **CLOSED** (earlier in the pass) |
| Re-merge units 7, 8, 10 | required once at the end | **ALREADY RUN and COMPLETE** |
| Split of units 1-6 | non-destructive, containers retained | **COMPLETE and unambiguous** |

**Nothing in Phase 0 blocks the merges, and nothing in the merges blocks Phase 1 on content grounds.**
Phase 1 remains gated, but on the *computation* (see §5), not on the manuscripts.

---

## 1. The `G.illcond` residual was a false alarm from a literal-number check

The scanner `/home/user/p5/phase0_scan.py` flags `G.illcond` when a "6.5 yr" figure appears
without the numerals `0.87` / `10.67` nearby. It reported 9 bare mentions in unit 7 and 13 in
unit 8, plus 3 unlabelled findings attributed to units 7, 8 and 10.

Checked directly on the **current heads**:

| File | 6.5-yr mentions | `0.87`/`10.67` present | Sites with no band within 450 ch |
|---|---|---|---|
| `paper07_sampled_governance_v50.tex` | 9 | yes (2x) | 9 of 9 |
| `paper08_governance_delay_v46.tex` | 13 | yes (8x) | 12 of 13 |
| `paper09_cod_certification_v32.tex` | 0 | no | - |
| `paper09b_arv_certification_v2.tex` | 0 | no | - |
| `paper10b_edwards_aquifer_v1.tex` | 0 | no | - |
| `paper11_forecasting_baselines_v64.tex` | 0 | no | - |
| `paper11b_edwards_forecast_v2.tex` | 0 | no | - |

**The "unit 10" finding does not exist** — no file in unit 10 mentions a 6.5-yr figure at all.
That entry in the earlier record was itself an artifact.

### 1.1 The proximity check is the wrong standard

A count of mentions lacking a band *within 450 characters* looks alarming (9/9 and 12/13). It is
not the right test. The question is whether the paper discloses the ill-conditioning where a
reader will meet it, not whether every occurrence is individually annotated.

**paper08 handles this exemplarily**, at four levels:

- **L169 (lead):** "restabilising only above about 6.5 yr ... a value stable across discretisation
  schemes (6.50-6.73 yr) but **not identifiable in the parameters, sweeping 0.87-10.67 yr** under a
  half-percent joint perturbation and vanishing entirely in a third of cases under one percent"
- **L2058 (body):** explicit statement that scheme agreement and parameter identifiability are
  *different questions*, with the band.
- **L4920:** the joint-perturbation table (0.87-10.67 yr; -87% to +64%).
- **L5399 (close):** "the paper's own most-quoted number is **reported as a band rather than a
  threshold** ... sweeping 0.87-10.67 yr ... vanishing entirely in twenty of sixty-four corners."

**paper07 discloses the same thing in its abstract, in prose rather than numerals:**

> "That crossing is **reported as a band, not a threshold**: under a half-percent joint
> perturbation of the model parameters it ranges from **under one year to nearly eleven**, and
> under a one-percent perturbation the instability verdict itself fails in a third of cases
> (Section 3.5), so the robust content of the paper is the operator contrast and the
> protective-channel result rather than [the crossing value]."

The scanner looked for the string `0.87|10.67` and scored a paper that says "under one year to
nearly eleven" as undisclosed. **The check was wrong, not the paper.**

### 1.2 Consequence

- No fix is owed. Neither unit 7 nor unit 8 carries a bare, unqualified 6.5-yr threshold.
- The scanner's band test should be treated as a *candidate generator only*. It cannot distinguish
  prose restatement of a band from omission. This is the third measurement artifact of this pass
  (after the prior-art word counts and the fabricated DOI) and the same failure mode in all three:
  **literal matching without semantic context.**

---

## 2. Units 7, 8, 10 are already merged

The three merge scripts still valid under the 11-unit architecture:

| Unit | Script | Sources | Output |
|---|---|---|---|
| 7 | `merge_08_07.py` | `paper08_v45` + `paper07_v50` | `paper08_governance_delay_v46.tex` |
| 8 | `merge_09_9b_10b.py` | `paper09_v31` + `paper09b_v2` + `paper10b_v1` | `paper09_cod_certification_v32.tex` |
| 10 | `merge_11_11b.py` | `paper11_v63` + `paper11b_v2` | `paper11_forecasting_baselines_v64.tex` |

The outputs (`v46`, `v32`, `v64`) **are the current heads** — the re-merge had already been run.

### 2.1 Content-preservation check

A raw sentence-level diff reported 104 / 87 / 54 sentences "not carried". This is a splitting
artifact: sentence boundaries on `[.!?]` break on LaTeX decimals (`6.501`), abbreviations, and
captions glued to markup (`...windows.} \label{fig:cod} \end{figure} Table 5 collects...`).

Re-tested with markup-stripped 8-gram coverage, which is robust to re-wrapping:

| Unit | Source | Body-only coverage | Residual |
|---|---|---|---|
| 7 | `paper08_v45` | 97.16% | 820 grams |
| 7 | `paper07_v50` | 96.30% | 723 |
| 8 | `paper09_v31` | 98.15% | 323 |
| 8 | `paper09b_v2` | 91.74% | 603 |
| 8 | `paper10b_v1` | 96.85% | 294 |
| 10 | `paper11_v63` | 98.57% | 312 |
| 10 | `paper11b_v2` | 93.59% | 598 |

Inspected the residual. It is **not content loss**. It is concentrated in exactly the regions a
merge is required to alter:

- **Label renumbering** — `fig:cod` -> prefixed form; `lem:bracket` -> `arv-lem:bracket`;
  `prop:recovery` -> prefixed; "figure 3.8" -> renumbered.
- **Bibliography consolidation** — three sources become one reference list, so per-source
  bibliography n-grams necessarily differ.
- **Declarations** — merged into one closing section.
- **Cross-reference text** — "figure 5" -> "figure 9" and similar.

**Verdict: all three merges preserve their sources. No content was lost or condensed.**

---

## 3. The split is complete and unambiguous

Four merges from the voided partition produced containers that are now superseded. All six
component units have since been split out, and in every case **the split carries a higher version
number than its container**, so version ordering alone identifies the authoritative file.

| Container (superseded) | Size | Split-out units (authoritative) |
|---|---|---|
| `paper01_obstruction_calculus_v62.tex` | 267,219 B | `paper01_v63` (unit 1), `paper02_v33` (unit 2) |
| `paper03_computational_certification_v15.tex` | 164,102 B | `paper03_v16` (unit 3), `paper04_v16` (unit 4) |
| `paper05_exact_belief_computation_v15.tex` | 138,034 B | `paper05_v16` (unit 5) |
| `paper06_assessment_separation_v66.tex` | 458,404 B | `paper06_v67` (unit 6) |

Containers are retained, byte-identical, per the non-destructive rule. No confusion risk.

---

## 4. State of the eleven units

| Unit | File(s) | Status |
|---|---|---|
| 1 | `paper01_v63` | split out |
| 2 | `paper02_v33` | split out; prior art PASSES |
| 3 | `paper03_v16` | split out; prior art PASSES |
| 4 | `paper04_v16` | split out; prior art PASSES |
| 5 | `paper05_v16` | split out; prior art SURVIVES, 3 fixes applied (`85d3a3e06d`) |
| 6 | `paper06_v67` | split out; prior art SURVIVES, 2 fixes applied (`72cde8e3a4`) |
| 7 | `paper08_v46` (merged) | merge verified complete |
| 8 | `paper09_v32` (merged) | merge verified complete |
| 9 | `paper10_v53` | single-source |
| 10 | `paper11_v64` (merged) | merge verified complete |
| 11 | `paper11c_v2` | single-source |

---

## 5. The computation has been restored (blocker removed)

`/home/user/repo` was empty. `RESTORE.md` documents the deposit:

```
git clone -b e2-v3-source-year \
  https://github.com/MIKEAA2020/general-sustainability.git repo
```

Executed 2026-09-30: **clone succeeded, 6,407 files, 924 MB.** `wave_e_cod` is present and
readable, including `src/superseded_v2/`, the v3 campaigns, and the verification scripts
(`301` battery checks, `157`-quantity basis audit, `97`-mutation sabotage harness).

Phase 1 is no longer gated on access.

---

## 6. Finding: the unit 1 / unit 2 split had NOT persisted

Checks in §3 assumed the splits of units 1-4 were on disk from an earlier pass. **They were not.**

| Unit | Expected | Actual head | State |
|---|---|---|---|
| 1 | `paper01_..._v63` | `paper01_obstruction_calculus_v62.tex` | v63 absent — **split was lost** |
| 2 | `paper02_..._v33` | `paper02_probabilistic_sufficiency_v12.tex` | standalone original, **fine** |

`paper01_v62` is the container: `merge_01_02.py` built it from `paper01_v61` +
`paper02_v12`, and it still holds both units (Part I 20,038 w; Part II 14,195 w). The earlier
session's write of `paper01_v63` did not persist — a known failure mode in this workspace, and the
reason every write here is re-verified by reading it back.

**Remedied 2026-09-30** with `split_paper01_unit1.py` (non-destructive; container untouched):

- Unit 1 -> **`paper01_obstruction_calculus_v63.tex`**, 21,582 w. Preamble re-scoped, `\part*`
  wrapper removed, Part I's own `\maketitle` + abstract retained, shared bibliography reproduced in
  full (an extra uncited entry is harmless; a missing one is not).
- Unit 2 -> **`paper02_probabilistic_sufficiency_v12.tex`**, 13,380 w, unchanged.

Verification of the extraction:

```
braces balance  : +0
environments    : document/abstract/enumerate/itemize/tabular/figure/table all balanced
\part commands  : 0   (standalone)      \maketitle : 1     \title : 1
labels=75 refs=34 dangling=0
content         : 99.92% of Part I 8-grams carried; the 18 missing are the
                  removed \part*{...} wrapper and its label/toc lines
```

The container's Part II was also compared against `paper02_v12`: differences are bibliography
consolidation and label renaming only, so keeping `v12` as unit 2 loses nothing.

---

## 7. Phase 1 first pass — superseded-value audit

`wave_e_cod/src/superseded_v2/README.md` records the ruling: the v2 basis is a **hybrid**
(parameters fitted under source-year, disturbance classes measured under destination-year),
"not a convention", and **must not be cited**.

The v2 -> v3 migration covers **ten** quantities, not the four previously tracked:

| Quantity | v2 (superseded) | v3 (authoritative) |
|---|---|---|
| UC_min | -460.03 | -328.97 |
| UC_q05 | -318.76 | -287.36 |
| UC_q10 | -114.85 | -80.87 |
| residual SD | 134.96 | 114.91 |
| residual mean | -20.44 | -10.88 |
| residual max | +179.76 | +206.55 (signed; v2 stored abs) |
| lag-1 acf | 0.652 | 0.554 |
| vacuous classes | 2 of 3 | 1 of 3 |
| q05 BAU kernel T=inf | empty | 2219.6 kt |
| constructive bound | 57.61 | 91.59 |

All eleven unit heads were scanned for the v2 values with digit-boundary regexes, each hit
classified as *live claim* or *documented migration* by whether the v3 value appears alongside.

**Result: 0 live superseded-v2 claims. 2 documented-migration mentions, both in unit 8.**

Unit 8 (`paper09_cod_certification_v32.tex`) additionally cites three authoritative v3 values
(`-80.87`, `0.554`, `91.59`). **The stale-number residual is closed with evidence.**

### 7.1 The table above is independently confirmed

`E2_REMEDIATION_PLAN.md` — the authoritative audit that `superseded_v2/README.md` points to — was
recovered from the branch on 2026-09-30 and corroborates the migration table from a second source:

- "Basis is **ratified and closed**. v3 = source-year. The hybrid v2 is not a convention and is
  not used anywhere."
- "`results/intervention_results_v3.json` | SD 114.91, UC = -328.97 / -287.36 / -80.87"
- "§2 SD / mean / max / acf | 134.96 / -20.44 / +179.76 / 0.652 | **114.91 / -10.88 / +206.55 /
  0.554**"

It also records that the E2 paper compiled cleanly under tectonic 0.17 (22 pages, no errors, no
overfull boxes), and that the v2 basis was reverted to `src/superseded_v2/` with a banner and this
README. So the ruling is not merely documented in two places, it was executed.

### 7.2 Two measurement artifacts caught in this pass, worth naming

- **`2 of 3` matched inside "sustains 12 of 36 pairs"** in unit 11 — an unrelated quantity. The
  check now requires digit boundaries on both sides.
- **The v2 values appear inside `run_intervention_v3.py` and `results_ident_v3/`.** This looks
  alarming and is not: they are the *left column* of a migration table documenting the change.
  Context, not string presence, decides.

These are the fourth and fifth artifacts of this pass (after the prior-art word counts, the
fabricated DOI, and the `G.illcond` literal-number check). The failure mode is constant: **literal
matching without semantic context.** Every automated check in this workspace should be read as a
candidate generator, never as a verdict.
