# `uploads/open.txt` evaluated, and the remaining open items closed

Method: every claim in `open.txt` was checked against the repo (the memo files, the manuscript, my earlier
verification records) and, where the claim needed an external source, against the primary source on the web.
Then each closed item was either implemented in **v36** or recorded as deliberately not implemented.

| # | open.txt says | verdict | evidence |
|---|---|---|---|
| 1 | no literal "LSIT" in the text | **TRUE, repo-wide** | `grep -rI "lsit"` over the workspace hits only `uploads/open.txt`, my own register, and `review/joint_master_assessment_v1.md` — never a memo |
| 1b | "so the acronym is almost certainly `LS_T` = left null space of `S_T`; use `LNS(S_T)`" | **FALSE — refuted** | `LS_T=0` at `uploads/p3 profound upgrades.txt:430` is not an acronym: the display reads `LS_T=0, \dot x = S_T v + b` *imply* `L\dot x = L b`, i.e. the product `L S_T = 0` for a conservation covector `L`, inside the section "A. Separate proof obligations". The acronym is the memo's own §3 heading, line 293: "**Make the central decision object the latest safe intervention time**", whose formulas run to line 418 and whose illustration heading is line 387 — the very line my register pointed at |
| 1c | "that open item is closed: replace LSIT with left null space" | **would have been a regression** | the left-null space of `S_T` is already the article's object (Lemma 3, the moiety covectors; and since v35, Proposition 36's `(U_1 ⊕ U_2) ∩ \ker D_J^{\top}`). Adopting the advice adds a duplicate definition and deletes the deadline object the memos asked for three times |
| 2 | the numeric anchor `m_0=100`, `d_0=10 /yr`, `τ=2`, `ρ=1 /yr²`, `L_max = 10−2−5 = 3` exists, and "is not an anchor for the supportable-output envelope" | **numbers TRUE (memo lines 393–400); the second half misjudged** | I re-derived the anchor rather than trusting it: a grid linear programme minimising `∫d dt` subject to `d ≡ d_0` on `[0,τ]`, `\dot d ≥ -ρ`, `d ≥ 0`, `d(T)=0` returns 70.0088 against the closed form `d_0τ + d_0^2/(2ρ) = 70` (discretisation tolerance), and 22.7474 vs 22.75 and 27.9970 vs 28 on two further parameter sets. The same instance *is* the envelope's anchor, because the envelope's frozen-rate corner is `H^{loc} = m_0/d_0 = 10` yr — the third case (`m_0=25, d_0=4, τ=3, ρ=0.5`) gives horizon 6.25 yr and deadline −0.75 yr, i.e. feasible-looking stock, infeasible transition |
| 3 | use opus' "Upgrade 9" wording as the mechanism-design umbrella, including "Theorem (invariance). Under typing, interface matching, and declared MDV, the set of reports … is invariant to boundary redrawing and to reclassification at declared elasticity" | **quote accurate (lines 909–917) — DO NOT implement as a theorem** | the memo itself hedges it ("Partial results suffice: boundary-shift invariance follows from Upgrade 2's composition theorem"), and one of those two premises is now known to fail as stated: v35's Proposition 36 shows conserved quantities do *not* compose across an identification unless they are compatible on the classes, so "invariance to boundary redrawing" is not a corollary of the composition calculus but a conditional on the same compatibility. The hypothesis "declared MDV" is also a certificate field the article does not define (MDV sits in the declined/project list per `review/deployment_plan_v1.md` rows R and 18) |
| 4 | identifiability status field: `established | not established | refuted`; MDV alongside it | **right object, wrong vocabulary; MDV stays out of the article** | the article's `Cert` vector (§3.1) already takes three values — "established, not established, and **not applicable** to this object. The third value is not a failure and the second is not a refutation" — and *refutation* is a separate act in the article (refute-only predicate transport). Using open.txt's triple would have collided with that. Implemented the per-parameter field in the article's own three values, per readout, tied to Proposition 39. MDV: supplementary/project field, unchanged |
| 5 | "Prop 29's superlevel-set proof, carbon convention, companion pointer, code archive, Def 22, D4, non-displacement gate are not answerable from the file" | **correct that the file cannot answer them — all but D4 and the upload are answerable from the repo and the web, and were** | below |

## Closed from the repo

- **Definition 22 (closure deficit)** was quoted from the manuscript rather than guessed: `κ_m(τ;Θ)`,
  `δ_m = 1 − κ_m(τ_use;Θ)`, `∫liquidation ≥ δ̄∫g_m dt`, `T ≤ m_0/(δ̄ g_m)`. That is what makes the
  **non-displacement / additionality gate** statable without a counterfactual model, and it is shipped as
  **Remark 35**: the gate compares the deficit of the *composition* of project block and host ledger with the
  deficit of the host alone, it is checkable from declarations, it fails on relabelling (a re-labelled
  mobilisation leaves the composed deficit where it was), and it is not additive across a shared compartment —
  the Proposition 36 warning, restated for deficits.
- **Proposition 29 (the certifying aggregator is unique)**: the proposed "superlevel-set representation"
  `r ≥ c·1 ⟺ A(r) ≥ c` is *not* an alternative proof — its two inclusions are exactly the two lines of the
  printed proof (certification at `c = A(r)`, then monotonicity plus calibration). Closed as a **no-op**;
  recorded so it is not proposed a third time. No manuscript change.
- **Yield inflation / supportable-output envelope**: shipped as **Definition 46**, whose three readings are the
  ones the register asked for (decreasing in the horizon by restriction; a scalar quote is a *selection*, and
  Proposition 29 says which selections are certifying; the frozen-rate corner is Definition 22's horizon, so a
  published "years of supply" measures the declared drawdown path together with the barrier). **Definition 45
  and Proposition 41** ship the deadline object: the infimum-loss statement, the exact feasibility
  equivalence, the closed form, the strictly-later-than-deadline relation, and the negative-deadline case.
  The article's barrier convention (`A ≥ A_min`, closed corridor) is used, so the memo's optional strict
  variant ("if touching counts as failure") is settled rather than left dangling.
- **Per-parameter identifiability status** shipped in §3.1 next to `Cert`.
- The claimed **code archive** has its content on disk (`revision/v5/code/outputs.txt` carries the indicator ×
  predicate table, `Cert` columns included); only the deposit is missing, which is an author action.

## Closed from the web (primary sources)

- **Carbon convention, Remark 33.** *Working Guidebook to the National Footprint and Biocapacity Accounts*
  (2021 edition), §9.1.2: "There is no biocapacity figure for carbon uptake… NFA assumes all carbon uptake as a
  demand on forest land biocapacity. Therefore, including carbon dioxide biocapacity in addition to forest land
  biocapacity would lead to double counting" — and the 2019 edition's workbook note "biocapacity for every land
  use type **except carbon** (currently assigned a biocapacity of zero)"
  (footprint.info.yorku.ca/files/2021/12/NFA-Guidebook_2021_final.pdf; footprintnetwork.org 2019 Guidebook).
  So the zero row is the accounts' convention, not a modelling choice: it makes `τ_min = 0` identically, hence
  the premium equals the aggregate date *by construction rather than by dispersion* — a sharper statement than
  the one v35 shipped, and now cited. Excluding the carbon *demand* instead is a different object (non-carbon
  components only). This removes the item from "the author's call"; what remains for the author is only
  whether to publish the restricted variant next to the published one.
- **Overshoot-day arithmetic and vintage.** Earth Overshoot Day is computed as
  (biocapacity ÷ Footprint) × 365 (366 in leap years) — the `τ_agg` construction of Remark 33, confirmed —
  and GFN states the whole 1961→ series is recomputed at each release, with the current year nowcast from
  additional sources. 2022's announced date was 28 July (the 209th day) against the 213 d obtained here from
  the 2025 accounts' 2022 world row, so the four-day gap is vintage and nowcasting, not arithmetic; that
  sentence is now in Remark 33.
- **The companion pointer, verified against the deposited object.** Zenodo 22554217 holds
  `paper4_delay_dynamics_v30.pdf` (39 pp) and `paper4_supplementary_v4.md`; in that PDF, **eq. (1)** is the
  gated three-state core `Ṅ = S(N) − qEN`, `Ż = (1/τ_m)[Φ_k(qEN − S(N)) − Z]` with the delayed effort law for
  `Ė`, and **Section 2.4** is "The four-state working core and its relation to (1)". The article's bare
  pointer was therefore already correct — and it is correct *only* as a pair of pointers, since eq. (1) uses
  `S(N)` while the article's `qEN − R(N,A)` form is the working four-state core of §2.4. Both mentions in the
  article (Section 4.1 and the Section 2 hand-off paragraph) now name what they point at, so the reference is
  checkable without opening the companion.

## What open.txt got right that changed my plan

Two things. Its `d_0 τ + d_0²/(2ρ)` anchor pushed me to re-derive the deadline numerics instead of leaving the
LSIT item as "statement only, no numerics" — v36 ships the closed form *and* two instances, one of them the
negative case. And its "one supplementary batch, both fields" framing is why the identifiability field went in
next to `Cert` in §3.1 rather than as a new table.

## Still open after this pass

- **D4 wording** — recorded here as "the author's; not in the repo". **That was wrong.** The sentence has been
  in §1.5 since v5, and `revision/v5/README_v5.md` logs it as drafted wording awaiting sign-off, not as an
  unwritten item; what was outstanding was its substance, which was verifiable and is now verified and
  rewritten (v37). Full correction and the source quotations: `review/open_items_v5_d4_mdv.md`.
- **MDV as a supplementary table**, and the per-parameter status column in that same supplementary table. Both
  are drafted in `revision/v7/supplementary_v9_candidate.md` (S11, S12); the article body gained the object
  MDV needs in order to be checkable at all (Definition 47, Proposition 42, Remark 36) and still does not
  assert the valuation thesis.
- **Uploading `revision/v5/code/`** to the deposit record.
- The Tier-3 project items (compiler, certificate expiry, passports, pilots, dashboards) — out of the article
  by the standing triage, unchanged.
