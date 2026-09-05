# v19 — Rejected‑Insights Evaluation (Negative Results & Structural Properties)

**Revision:** v19 (`revision=19`, `master=4`) · live via `data/IMPLEMENTED_revision_ECOMOD.md → revisions/IMPLEMENTED_revision_ECOMOD_v19.md`
**Task:** Evaluate each previously‑rejected insight; classify as (a) modified into a valid positive result, (b) reframed as a useful negative result, or (c) discarded as unproductive; recommend manuscript presentation.
**Disposition decided at the v19 mint:** none discarded; four reframed as structural/negative results, one already resolved.

---

## 1. What the user directed

> Most rejected insights are scientifically valuable as **negative results** — keep them as
> limitations/structural properties in §13 (or a new "Model limitations and negative results"
> subsection). For each, state what the model does **not** do and why that matters. Explicitly
> contrast the **τ_g cliff** (basin‑boundary crisis, no CSD) with the **fixed‑liability E‑fold**
> (true fold, CSD present). Consider a short table of tested‑but‑absent phenomena and their
> implications. **Do not modify the model** (Allee/stochasticity/seasonal forcing = future‑work only).

## 2. Per‑insight disposition (verified)

| # | Rejected insight | Verdict | How presented now |
|---|---|---|---|
| 1 | Critical slowing down / early warning (CSD‑EWS) | **(b) Negative result** | §13(9) row 1: no CSD before the τ_g cliff (basin‑boundary crisis) — `Re λ ≈ +0.62` constant, no eigenvalue crossing zero, `P`‑relaxation return time flat ≈150 yr then vanishes abruptly at τ_g≈19–20. |
| 2 | Hysteresis / path dependence in the threshold | **(b) Negative result** | §13(9) row 3: `A_c(E)` single‑valued; no bistability per fixed `E`; threshold identical up and down. Asymmetry is in *time*, not threshold. |
| 3 | Endogenous boom–bust limit cycle | **(b) Negative result** | §13(9) row 4: the overshoot‑recollapse is a **single recovery‑overshoot pulse** (2 crossings of `0.5·A_max`), not a cycle; consistent with the monotone (no‑Hopf) leading eigenvalue. |
| 4 | Allee‑type rescue threshold | **(b) Negative result, policy‑relevant** | §13(9) row 5: collapse at τ_g=30 is **domain‑wide** (every A₀ 0.02–1.00 collapses, incl. healthy A₀=1.0); rescue zone is a **measure‑zero strip** at A₀=A_max. Cannot rescue by starting higher — must shorten the lag. |
| 5 | "50 % anchor ⇒ fast full recovery" | **Already resolved (positive)** | v18 recovery‑time asymmetry + rate/lag decoupling (not a new v19 item). |

**Directive satisfied:** "no CSD precursor" is kept explicitly *not* as a missing‑tool gap but as a
verified structural claim; the τ_g cliff vs E‑fold contrast is made **regime‑scoped** (see §3).

## 3. The corrected τ_g‑cliff vs E‑fold contrast (regime‑scoped)

This is the one place a v18 over‑claim was corrected, and it must be stated as **regime‑scoped**.

- **τ_g cliff (baseline):** first‑order **basin‑boundary crisis**. Constant `Re λ ≈ +0.62` (no eigenvalue
  crossing zero), no CSD precursor, `P`‑relaxation flat ≈150 yr then the attractor vanishes abruptly.
  Not a fold.
- **Fixed‑liability E‑fold:** is a **genuine saddle‑node = MSY**, but only in the **increment‑dominated**
  regime (`b_Gρ > b`). There `B′(A*)=0` exactly and two opposite‑sign‑`B′` fixed points merge at the
  threshold → the textbook Scheffer‑type catastrophic shift, with a real CSD precursor.
- **At baseline** (`b_Gρ = 0.04 < b = 0.5`): `B(A)` is **monotone increasing** on `[0, A_max]`, `B′(A_max)=+0.46`,
  and `B′(A)=0` only at `A=8.1` (outside the physical domain) → **no interior saddle‑node, no fold / no CSD.**
  The stable object is the boundary `A_max`.

**Verified numbers (v19):** baseline — `B′(A)=0` at `A=8.1 ∉ [0, A_max]`, `B′(A_max)=+0.46`, range 0.0→0.6.
Increment‑dominated (`b=0.02`) — interior MSY `A*=0.900`, `B_max=0.027`, `B′(A*)=0` exactly; at `E=0.026`
two fixed points `[0.699, 1.101]` with `B′=[+0.0134, −0.0134]` (one unstable, one stable) meeting at the
saddle‑node.

> **Guardrail (do not re‑assert):** do **not** present the baseline E‑fold as a realized fold/CSD case.
> "True fold / CSD present" applies **only** to `b_Gρ > b`. §4.2 is rewritten accordingly.

## 4. §13(9) — Structural properties and negative results (added)

New subsection placed after §13(8)(vii) (recovery‑overshoot block) and before the "Companion‑study
discipline" paragraph, so the negative‑results block sits at the end of the reasoned caveats. It carries the
tested‑but‑absent table and a closing paragraph:

> the corrected model's collapse is *robust but not predictable from a single scalar*: driven by the
> regeneration lag (finite‑amplitude basin erosion), **not** by a fold, **not** by Allee low‑density
> dynamics, and it carries **no generic CSD precursor**. This is *more* informative than a set of positive
> results: it tells a manager which levers **don't exist** (no rescue‑by‑stock, no early‑warning signal)
> and which **do** (shorten the lag; and, only for the increment‑dominated E‑fold, watch for slowing).

Model **extensions** raised by the negative results — stochasticity, seasonal forcing (to test for induced
cycles), explicit Allee term (to test for a rescue route) — are stated as **future‑work directions**, not
changes to the current (deliberately minimal, deterministic, Allee‑free) model. Constraint honoured.

## 5. Cross‑link from §8

The collapse sentence in §8 ("not merely a one‑time basin loss…") now explicitly notes that the τ_g
transition is a **basin‑boundary crisis, not a fold**, that it carries **no CSD/early‑warning precursor**,
and points to §13(9), so the reader is not left expecting a smooth warning signal.

## 6. Verification (v19)

- **Scan:** 21 covered / 0 partial / 1 superseded (12A.1, expected) / 0 ambiguous / 0 missing.
- **Eval:** Recall@1 0.82, Recall@3 0.95 on 22 claims; only miss `12B.6` (unchanged from v18).
- **Tests:** 34 passed.
- **Figures:** all resolved refs OK (only intentional shorthand ellipses and the "not referenced" Euler figure).
- **§13 numbering:** clean (1)–(9), no duplicate.

---

### Files
- Revision: `data/revisions/IMPLEMENTED_revision_ECOMOD_v19.md` (+ live symlink).
- Findings record: `reports/v19_rejected_insights_evaluation.md` (this file).
- v18 record: `reports/v18_recovery_ecology_insights.md`.
