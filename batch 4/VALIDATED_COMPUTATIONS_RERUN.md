# VALIDATED_COMPUTATIONS_RERUN — Independent Reproduction of Part II Artifacts

**Scope.** The remaining citation gate on `research_program/validated_computations/`: every Part II row was still `NONE` for independent rerun. A second agent, on a different machine and toolchain, cloned the committed tree and ran the reproduction commands from `PROOF_MANIFEST.md` Part II.

**Toolchain.** Python 3.13.14, numpy 2.3.5, scipy 1.17.1, mpmath 1.3.0. The pinned original environment was Python 3.12.13 / numpy 2.1.3 / scipy 1.14.1 / mpmath 1.3.0. Same mpmath; newer CPython / numpy / scipy.

**Headline: the five committed certificates reproduce, three of them byte-identically.** Hopf, E5, and the dt=0.25 monodromy enclosure (JSON + NPZ) are hash-identical to the pinned artifacts. The K=80 Krawczyk and the off-grid residual re-solve Newton on this toolchain and therefore land at a nearby centre (`|ΔP| = 4.5e-12`); both still certify the same discrete-level claims. The A025 fold pipeline was **not** rebuilt (still `NOT REBUILT`). No Wave E gate is closed.

Reproducible checks:

- `REPO="$(pwd)" python3 reaudit/verify_consistency.py` — tree-side grep; post-repair reading of 10 defect-gone failures, documented below.
- `REPO="$(pwd)" python3 reaudit/verify_manuscript_sweep.py` — the same check run over `revised_articles/`.
- `REPO="$(pwd)" python3 reaudit/verify_validated_computations.py` — pinned-hash + rerun-claim checks.

Saved logs: `reaudit/validated_computations_rerun/`.

---

## 1. Script execution — 5/5 clean

Working directory: `research_program/validated_computations/`. Exact Part II commands.

| Artifact | Command | Exit | Wall time | Result |
|---|---|---|---|---|
| A025 Hopf | `python3 a025_fold/a025_interval_hopf.py` | 0 | <1 s | byte-identical JSON |
| C4 orbit Krawczyk | `python3 a021_c4/c4_orbit_krawczyk.py` | 0 | 0.5 s | `krawczyk_ok=True`, margin 1271 (committed 1186) |
| C4 off-grid residual v2 | `python3 a021_c4/c4_offgrid_interval_v2.py` | 0 | 42 s | residuals same order; A 6 % higher |
| C4 monodromy dt=0.25 | `python3 a021_c4/c4_monodromy.py` | 0 | 84 s | byte-identical JSON + NPZ |
| E5 module admission | `python3 e5_admission.py` | 0 | <1 s | byte-identical JSON |

`a025_fold/a025_fold_pipeline.py` was **not** treated as a certified reproduction command (Part II: `NOT REBUILT`; the Moore–Spence stage has a live `want_jac` signature bug). `c4_offgrid_interval.py` (v1, float64+ulp) is superseded and was not rerun.

Committed artifacts were snapshotted before the run and restored whenever a script rewrote a non-identical file, so the pinned hashes in Part II are unchanged. The new Krawczyk / off-grid outputs are archived under `reaudit/validated_computations_rerun/new_artifacts/`.

---

## 2. Hash verification

| File | Pinned SHA-256 | Independent rerun |
|---|---|---|
| `a025_fold/a025_interval_hopf.json` | `eda36cd1…95b3b2` | **MATCH** |
| `E5_NUMBERS.json` | `5670bcc8…236e72db` | **MATCH** |
| `a021_c4/c4_monodromy_enclosure.json` | `01d8c253…dbaef76` | **MATCH** |
| `a021_c4/c4_monodromy_dt0p25.npz` | `f3dc5445…a7ca5f` | **MATCH** (`M` and `lam` array-equal) |
| `a021_c4/c4_orbit_krawczyk_certificate.json` | `5e8df633…65ab133` | **DIFF** (claim reproduced; see §3) |
| `a021_c4/c4_orbit_krawczyk_box.npz` | `85f72c76…7ba4c69` | **DIFF** (`max‖Δu‖ = 4.3e-11`) |
| `a021_c4/c4_offgrid_residual_interval.json` | `2a4a5e82…1c74a7f4` | **DIFF** (claim reproduced; see §4) |

This is stronger than the Wave E caveat (“hash identity is not guaranteed across machines”) for three of the five certificates, and weaker — honestly — for the two that re-solve a 645-dimensional Newton problem.

---

## 3. Krawczyk — claim reproduced, Newton centre toolchain-dependent

| Quantity | Committed | This rerun | Difference |
|---|---|---|---|
| Period \(P\) | 370.93117783942597 | 370.93117783943046 | \(4.49\times 10^{-12}\) |
| Newton \(\|F\|_\infty\) | \(5.06\times 10^{-11}\) | \(1.28\times 10^{-10}\) | same order |
| Radii \((u,P)\) | \(10^{-8}\) | \(10^{-8}\) | — |
| `krawczyk_ok` | True | True | — |
| Margin | 1185.98 | 1270.86 | both \(\gg 1\) |
| Box \(\|u_{\mathrm{new}}-u_{\mathrm{old}}\|_\infty\) | — | — | \(4.29\times 10^{-11}\) |

The new centre sits well inside the committed \(10^{-8}\) box. Uniqueness of a collocation zero in that box is therefore confirmed by a second Newton/Krawczyk pair, not merely re-read. Status string identical: *VALIDATED: existence and local uniqueness of a collocation zero in the box (discrete K=80 level)*.

The hash difference is the expected BLAS / lstsq drift of a 645-dimensional Newton iteration between numpy 2.1.3 and 2.3.5. It is not a failed certificate.

---

## 4. Off-grid residual — same order; \(A\) 6 % higher

The v2 script calls `solve_orbit()` itself, so it certifies the interpolant of *this* toolchain's Newton centre, not the committed centre.

| Component | Committed | This rerun |
|---|---|---|
| N | \(6.5709\times 10^{-8}\) | \(6.5705\times 10^{-8}\) |
| A | \(1.0406\times 10^{-9}\) | \(1.1093\times 10^{-9}\) |
| Z | \(8.2846\times 10^{-7}\) | \(8.2846\times 10^{-7}\) |
| E | \(2.8491\times 10^{-6}\) | \(2.8491\times 10^{-6}\) |
| Period | 370.93117783942597 | 370.93117783943046 |
| Grid | 256 | 256 |

N, Z, E match to four significant figures. A is 6 % higher and slightly above the manifest row's rounded “\(A\le 1.0\times 10^{-9}\)”, but well inside the Part IV citation form “continuum residual \(\le 3\times 10^{-6}\)”. Both runs remain interval-certified (mpmath, no float64 fallback).

**Runtime dps note.** The script sets `miv.dps = 40`, then imports `c4_orbit_krawczyk` → `interval_lib` which resets `miv.dps = 50`. The written `"arithmetic": "… dps=50"` field is therefore what the process actually used, on both the original run and this one. The source comment “dps=40” is stale; the artifact is honest.

**Part IV grid note.** The register's citation form still said “512-point grid”. The committed v2 script evaluates 256 points. Corrected in this pass.

---

## 5. Every certified prose number reproduces

**Hopf (Candidate A), committed = rerun.**

- \(\tau_-\in[3.66614901427411348\ldots,\,3.66614901427411348\ldots]\) (width \(\sim 4\times 10^{-32}\)), crossing *left (stabilising)*.
- \(\tau_+\in[150.35847731014138\ldots,\,150.35847731014138\ldots]\), crossing *right (destabilising)*.
- Both \(x=\omega^2\) roots simple. Displayed manuscript intervals \([3.6661490142739,\,3.6661490142743]\) and \([150.3584773101408,\,150.3584773101421]\) contain the certified intervals.

**Monodromy \(\Delta t=0.25\), committed = rerun (byte-identical).**

- 1484 steps = 371.00 yr, dimension 76, ball \(1.313\times 10^{-4}\).
- Phase \(1.0048009793249175\), `simple_neutral_certified=True`.
- Dominant nontrivial \(0.6876430781740369\), disc \(0.06947\), `below_one_certified=True`.
- `all_nontrivial_strictly_inside_unit_disc=True`.
- \(\sigma_{\min}\) contour at radius 0.97 does **not** exceed the ball (`exceeds_ball=False`, 60 000 SVDs). Hyperbolicity is carried by the individual discs, not by the contour. The committed artifact already recorded this; the rerun confirms it.

**E5 (linear A001 §§6–10 toy), committed = rerun.**

- Three kernel conditions hold with outward-rounded margins \(0.40\), \(1.00\), \(4.00\).
- Joint face margin \(\alpha=0.20\), \(L=0.20\), erosion \(r=0.05\), \(\Delta_{\max}=0.18\).
- Verdict unchanged: *ADMITTED WITH NUMBERS (linear resource-sink, declared scope)*. No real-system transfer.

---

## 6. Tree-side grep (`verify_consistency.py`)

`REPO="$(pwd)" python3 reaudit/verify_consistency.py` exits 1 with **exactly the documented post-repair 10 failures** (reaudit README: C1×2, C2, C3, C4×3, C5, C6×2). Section A (discipline that holds) is 11/11 OK, including all five Part-V forbidden claims, the E5 transfer prohibition, TCS-1.1, `.docx`/`.md` sync, and item-1 containment.

The ten `[FAIL]`s are *defect-gone* checks: the suite still asserts the *presence* of the pre-repair defects. After the bucket-B / C4 / C6 / C7 repairs those phrases are absent, so the checks fail. That is the expected reading, not a new inconsistency.

C7's “no crosswalk exists” check is still `[OK]` only because it greps for `crosswalk|mapping table` *on the same line as* `Numerical proposition`; Part VII's table puts those strings in different cells. The crosswalk is in the register; the check is stale. Not acted on here.

---

## 7. Manuscript-side sweep (`verify_manuscript_sweep.py`)

The same Part-V / E5 / TCS / refutation greps, scoped to `revised_articles/` (24 files), plus the C3-style “computations labelled `PROVEN`” check and a fold-overclaim check.

**Before citation edits:** A025 still said the Hopf pipeline “does not yet contain an independently reproduced … pipeline” — the remaining gate. No manuscript used reserved `PROVEN` for a computation. No manuscript asserted a certified fold. A021 correctly refused a continuum monodromy enclosure.

**After citation edits (this pass):** A025, A018, A020, A021, and `revised_articles/INDEX.md` now cite the independently reproduced Part II artifacts with the Part IV citation forms (discrete / interval-verified, not proved; fold still not certified; continuum lift still open). The sweep exits 0.

A021's *shooting* Floquet table (phase \(0.98688\) / dominant \(0.68775\) at \(\Delta t=0.25\)) is a different computation from the validated enclosure (phase \(1.00480\) / dominant \(0.68764\)). The manuscript now says so explicitly. The shooting table was not overwritten.

---

# Findings

## V1 — Independent rerun is no longer `NONE` for the five committed certificates

This pass is a second agent, second machine, second CPython, second numpy/scipy. Three artifacts hash-match; two re-certify the same claim at a nearby Newton centre. That discharges Issue 1 of the former `HONEST_DISCLOSURE.md` (removed from the public release in the v1.0 curation; its content is consolidated in `PROOF_MANIFEST.md` → "Reproducibility status") for these five rows. It does **not** discharge Wave E Part III (every support row remains `NOT CONFIRMED`), the A025 fold rebuild, or the dt=0.1 monodromy. The Wave E scored trees already have their own independent rerun (`WAVE_E_RERUN.md`); `INDEPENDENT_RERUN_NONE` is false for those trees.

## V2 — Krawczyk / off-grid hashes are not toolchain-stable (expected)

`solve_orbit` uses `numpy.linalg.lstsq` on a 645×645 Jacobian. Changing numpy 2.1.3 → 2.3.5 moves the Newton centre by \(4\times 10^{-12}\) in \(P\) and \(4\times 10^{-11}\) in \(u\). The Krawczyk test is a *sufficient* condition around whatever centre it is given; both centres pass with margin \(>1000\). Anyone pinning these two hashes should pin the *claim* (unique zero in a \(10^{-8}\) box; residual \(\le 3\times 10^{-6}\)), not expect byte identity across BLAS.

## V3 — Part IV over-claimed the off-grid grid and the monodromy mesh

- Off-grid citation form said “512-point grid”; v2 evaluates **256** points.
- Monodromy citation form said “two mesh levels”; only **dt=0.25** is rebuilt (`dt=0.1` is `NOT REBUILT`).

Both corrected in `PROOF_MANIFEST.md` this pass. No numerical claim changes.

## V4 — A025's “not yet independently reproduced” sentence is now false, and was the citation blocker

`revised_articles/A025_interval_folds_corrected.tex` made the Hopf certificate *conditional* on an unreproduced pipeline. That sentence is updated. A018 / A020 / A021 now cite the same independent rerun. The fold statements are untouched (still numerical evidence).

## V5 — A021's shooting Floquet table is not the validated enclosure

The table in Numerical Result `num:c4-cycle` (phase \(0.98688\)) matches the older `c4_floquet_dt0p25.json`, not `c4_monodromy_enclosure.json` (phase \(1.00480\)). Promoting the shooting numbers as “the” validated multipliers would have been a C3-class defect. The new paragraph cites the enclosure as a *separate* discrete object.

---

# What this does *not* do

- Does not close any Wave E Part III row.
- Does not rebuild the A025 fold Moore–Spence / Krawczyk pipeline, the m=96/128 resolution checks, or C4 monodromy at dt=0.1.
- Does not prove a continuum orbit, a continuum Floquet enclosure, or continuum bunching (Part V still forbids those claims).
- Does not transfer E5 to 2J3KL or Edwards (R04 certificate still not constructed).
- Does not upgrade any `PROVEN (reconstructed)` theorem row.
- Does not re-execute the Wave E scored trees (already done in `WAVE_E_RERUN.md`; those labels are `INDEPENDENT_RERUN`, not `NONE`).
- Does not re-verify the reconstructed theorem files line-by-line.

---

# Substantive conclusion

The five committed discrete-level certificates in `research_program/validated_computations/` can now be cited, with the Part IV wording, as independently reproduced:

- Hopf delays: interval Newton, hash-identical.
- K=80 collocation orbit: unique in a \(10^{-8}\) box, discrete.
- Off-grid interpolant residual \(\le 3\times 10^{-6}\) on the 256-point grid, interval arithmetic.
- Floquet enclosure at dt=0.25: phase simple+neutral, dominant \(0.68764+0.069<1\), hash-identical.
- E5: linear toy admission, hash-identical, no real-system transfer.

The fold, the continuum lift, and every Wave E support row stay exactly where the register already put them.
