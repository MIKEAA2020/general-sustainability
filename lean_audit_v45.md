# Lean audit — v45

Branch `lean-audit-v4`. Build unchanged: **rc = 0, 60 jobs**, zero
warnings, zero `sorry`, zero axioms.

This turn is verification of the *other* papers' empirical and
verification apparatus — the supplementary material cited by ECOMOD,
then the remaining papers' own batteries.

---

## 1. ECOMOD SI §S5.3b — run, not just read

The manuscript's §Model scope claims two empirically anchored
quantities, the second being *"the cropland-book calibration from NFA
biocapacity and the crop-yield index (SI §S5.3b)"*. Rather than read the
SI, I fetched the calibration script
(`model_sims/calibrate_bf_af_provisioning_leg.py`) and its four data
files and **ran it**.

It reproduces the SI table. Every load-bearing figure matches:

| quantity | SI §S5.3b | script | |
|---|---|---|---|
| cropland biocapacity 1961 | 1.251e9 gha | 1.2511e+09 | ✓ |
| `A_f` 1961 | 1.34e9 ha | 1.3392e+09 | ✓ |
| `b_f`(1961), absolute | 0.93 gha/ha/yr | 0.9342 | ✓ |
| `A_f` growth | 1.17× | 1.17× | ✓ |
| `b_f` growth, NFA units | 2.43× | 2.43× | ✓ |
| **cropland `B_f` growth** | **2.85×** | **2.85×** | ✓ |
| `d ln b_f` (cereal) | +1.128 | +1.1285 | ✓ |
| `d ln B_f` | +1.048 | +1.0478 | ✓ |
| aggregate total | +23% | +23.0% | ✓ |
| land-type total | +24.5% | +24.5% | ✓ |
| cropland share of growth | ≈97% / ≈103% | 97% / 103% | ✓ |
| non-cropland `d ln` | ±0.01 | +0.0083 / −0.0088 | ✓ |

The manuscript's abstract claims (biocapacity **+23%**; cropland
**2.85×**; non-cropland **flat**) are therefore backed by code that
runs.

### One internal inconsistency in the SI

The cereal-sentinel row reports growth **3.11×** but its own log-change
**+1.128**. Those disagree: `e^1.128 = 3.089`. The script confirms
**3.09×** (`d ln = +1.1285`). The SI's 3.11× appears to come from
dividing rounded endpoints (4.21 / 1.353 = 3.112) rather than from the
series.

**The manuscript does not carry the error** — it cites neither 3.11,
3.09 nor 4.21 (grep: zero occurrences). So the defect is contained in
the SI table and does not reach the paper's claims. It is still worth
correcting, since the table's purpose is to report measured values, and
it is the only figure in the section that fails to reproduce.

## 2. P3 — 32/32, and a version gap

`paper2_probabilistic_sufficiency_v11_verification.py` run against
`…_v11.tex` with its full dependency chain:

```
verification: 32/32 checks pass (chained seeds: 16/16 + 21 nested, 15/15, 6/6)
```

Getting there required fetching six missing siblings — three chained
scripts and three `.tex` files, nested two levels deep
(`belief_state_v2` → `stochastic_selector_v2.tex`, and
`hidden_parameter_learning_v1.tex`), plus five figure PDFs from
`figs_bs2/`. **Every failure was a missing asset; none was a content
defect.** Two chained scripts pass standalone (15/15 and 6/6).

**A real gap, and it is not environmental.** There is **no
`paper2_probabilistic_sufficiency_v12_verification.py`** in the repo.
The newest battery is **v11**, while the paper is at v12 — and at v13
after my v43 edit. So the P3 paper's current version has **no
verification script at its own version number**. I first mistook the
404 response for a 141-byte stub, because `curl -o` wrote the error
body to disk; worth remembering that `-o` swallows HTTP errors
silently.

## 3. comp — 54 pass, 1 fail, and the failure is a missing package

`paper2_computational_certification_v18_verification.py` against
`…_v18.tex`, after fetching the supplementary `.tex` and two chained
scripts:

```
verification: 48/49 checks pass      (54 PASS, 1 FAIL)
FAIL chain viacert selftest green (12/12)
```

The single failure is `ModuleNotFoundError: No module named 'viacert'`
— the solver package is not installed in this sandbox. The repo ships
`SafeTransition_*` archives and a `safetransition/` directory, so it is
presumably available to the author; **I did not verify that it passes**,
and am not claiming it does.

Note also that comp is at **v19** after my v43 edit, while its battery
is **v18** — the same version skew as P3, and the added mechanized-layer
paragraph is not yet covered by any needle.

## 4. Titles

All four current, and consistent with how companion papers cite them:

| paper | title |
|---|---|
| P1 v63 | Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility |
| comp v19 | Computational Viability Certification under Incomplete Observation: A Continuous-to-Finite Bridge… |
| P3 v13 | Probabilistic Sufficiency for the Obstruction Calculus: Belief-State Safety Values under Partial Observation |
| EBC v12 | Exact Belief-State Computation at Scale II: The Four-Parameter Cube and the Antichain Census |

## 5. Summary of defects found this turn

| defect | severity | fixed |
|---|---|---|
| SI §S5.3b cereal growth 3.11× contradicts its own +1.128 | minor, contained to SI | no — recommended |
| P3 paper at v12/v13, verifier only at v11 | **moderate — a coverage gap** | no — author action |
| comp paper at v19, verifier at v18 | minor — same skew | no |
| comp `viacert` not installed here | environmental | n/a |

**Not defects:** every failure encountered in the P3 and comp batteries
traced to a missing file or package. No paper content failed a check.

## 6. Caveats

* No `pdflatex`; no paper compiled anywhere in this audit.
* `viacert` selftest unverified.
* Abstracts were scanned for the ECOMOD manuscript only; the four
  papers' abstracts have not been read line by line against their
  batteries.
