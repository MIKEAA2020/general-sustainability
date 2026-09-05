# v18 — Verified recovery-ecology insights (additional ecological insights)

Commit after `29f9cc0` (v17) → v18. `VERSION revision=18`. Live pointer → `data/revisions/IMPLEMENTED_revision_ECOMOD_v18.md`. v1–v17 preserved.

**What was asked:** do the work's ecological insights merit *additional, non-decorative, non-superficial* content? Rather than assert, I proposed candidate insights and ran them **computationally**. Three were found to be real and added; several were tested and **rejected** (including two that are tempting but wrong).

---

## Added (each verified by simulation)

### 1. Regeneration *rate* vs *lag* are two decoupled levers — the headline insight
Sweeping `ρ` (rate) and `τ_g` (lag) independently from the extinction floor:
- **`ρ` sets HOW LONG recovery takes.** Time-to-50 % of `A_max` scales roughly inversely with `ρ` (t50 ≈ 145/ρ yr).
- **`τ_g` sets WHETHER recovery happens at all.** Recovered at `τ_g ≤ 18`, collapsed at `τ_g ≥ 20`, **for every `ρ`**.

| `ρ` (yr⁻¹) | `τ_g=10` (recovers) | `τ_g=30` (collapses) |
|:--|:--:|:--:|
| 0.03 | t50 ≈ 162 yr | 203 yr |
| 0.05 | 106 | 142 |
| 0.08 | 74 | 105 |
| 0.12 | 56 | 82 |

**Non-decorative because it is policy-actionable and disambiguates two levers a manager could pull:**
accelerate the regeneration *rate* (shorten recovery time) vs. *shorten the regeneration lag* (change the
recovery *outcome*). **Raising `ρ` cannot rescue a long-`τ_g` trajectory** — it only makes it recover to
50 % faster before collapsing. Added as §13(8)(vi) and as a new §6 falsifiable prediction (#7); abstract
count reconciled to **seven**.

### 2. Recovery *overshoots* `A_max` (catch-up rebound pulse)
A recovering system rises **past** the old `A_max` before relaxing: `A_peak` = 1.21 (`τ_g=10`), 1.25 (15),
1.28 (18) — up to `+0.08` beyond `A_max`. This is the Hutchinson-style overshoot on the *recovery* side —
a transient, not a new stable overshoot (and distinct from the §10 collapse-regime overshoot that ends in
liquidation). Added as §13(8)(vii) with the figure.

### 3. Scoping correction to v17's Scheffer framing (important honesty fix)
The `τ_g` cliff is **not** a catastrophic-shift fold with a critical-slowing-down (CSD) precursor. R2 finds a
**constant positive-real eigenvalue (`Re λ ≈ +0.62`) for every `τ_g`** — no eigenvalue crosses zero as
`τ_g → 20`, so there is **no slowing**. Verified: the `P`-relaxation return time is **flat ≈150 yr** for
`τ_g = 0–18`, then the attractor vanishes **abruptly** at `τ_g ≈ 19–20` rather than slowing. So the delay
transition is a **finite-amplitude basin-boundary crisis**, whereas the **fixed-liability `E`-fold of §4.2**
(where `A_c(E) → B_max`) is the genuine fold that admits a CSD precursor. This distinguishes the two
transitions and prevents an over-claim — exactly the kind of non-decorative scoping v17's Scheffer reference
needed. Added to §4.2.

### Figure: `scans/eco_recovery_insight.png`
Two panels: (left) density-dependent, sigmoidal recovery trajectories (slow near the floor, `G≈ρA`) from
`A_ext`, with the 50 %/95 % lines; (right) time-to-50 % vs `ρ` for `τ_g=10` (recovers) vs `τ_g=30`
(collapses), showing the rate/lag decoupling. Referenced in §8 and the "Accompanying files" note.

---

## Rejected (tested — tempting but the model does not produce them)

- **Critical slowing down as an early-warning signal.** Rejected — see #3. The return-time probe is *flat*
  until the attractor vanishes; there is no smooth slowing. (This is precisely why I could NOT add a
  "CSD predicts the collapse" claim, despite it being tempting given the Scheffer framing.)
- **Hysteresis loop in the fixed-liability threshold.** `A_c(E)` is single-valued in `E` (a fold, not a
  loop). A genuine hysteresis/alternative-stable-state *loop* requires the separatrix to differ on the way
  up vs the way down; here it does not. Rejected.
- **A sustained boom–bust limit cycle in the full S0.** The regrow-overshoot-recollapse is a *transient*
  (2 crossings of `0.5·A_max`), not a cycle. Described as "absorbing," not oscillatory. (The full `(6′)`
  model can show damped transients, but that is already noted.)
- **An Allee-style rescue threshold.** No Allee term; the collapse at `τ_g=30` is **domain-wide** (every
  `A₀` from 0.02 to 1.00 collapses — "every starting stock, even a healthy A=1.0, collapses"). The recover
  set is a **measure-zero strip** (`A₀=A_max` exactly recovers; 1.19 and 1.21 both collapse). So a "rescue
  level" claim would be wrong — there is no minimum viable stock; the delay makes the *whole* basin collapse.
- **The ≈50 % anchor implies fast full recovery.** Rejected as a standalone reading: t50/t95 is only
  ≈0.59–0.77 across `τ_g=0–18`, so 50 % is *not* "most of the way there" — reaching 90–95 % takes
  substantially longer. (This is consistent with, and slightly strengthens the v13 caveat that `τ_g` is a
  lumped proxy; it does not change the cliff location.)

---

## Verification (v18, live pointer)
- scan `21 / 0 / 1 / 0 / 0` · eval `R@1 0.82 / R@3 0.95` (unchanged, only known `12B.6` miss) ·
  numerics `12A.3/12G.2/12G.4/12G.5` PASS, `12A.1/12G.7` SUPERSEDED · `34` tests pass
- all ten referenced `.png` verified on disk; abstract count now "seven predictions"; no stale "six"
- all new values are ECOMOD's own (none imported from companions); the Scheffer/CSD points are frames and
  *scoping corrections*, not imported results.

*Discipline: two new insights verified and added, two tempting-but-false readings rejected, one scoping
correction made so the delay transition and the fixed-liability fold are not conflated.*
