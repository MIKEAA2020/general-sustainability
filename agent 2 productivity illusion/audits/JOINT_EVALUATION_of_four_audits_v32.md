# Joint Evaluation of the Four Audits of ECOMOD v32

**Audits evaluated jointly:** (1) Gemini, (2) Grok, (3) GPT, (4) the line-level audit
(`AUDIT_v32_line_level.md`). All four read `IMPLEMENTED_revision_ECOMOD_v32.md` at commit `ca70b4d`.

**Method.** Each claim was **verified, not taken on face value**, against the model code
(`model_sims/char_eq.py`, `r1_basin.py`, `corrected.py`), the registered JSON results, the manuscript
equations, and (for the empirical/citation items) the original published sources. Where a claim needed a
number, I recomputed it in-memory with a *robust* method rather than trusting a reported value — and, in a
few cases, found that the audits and my own prior verification tables were wrong in ways that only a
re-computation exposes.

**Overall read.** The four audits are strikingly concordant on the *substance* and discordant only on
*tone and severity*. The weight of the evidence is that v32 has a small number of **genuinely load-bearing
mathematical contradictions** (not stylistic nits) plus a large residue of **notational, scope, and
records** problems. The scientific core is real and, in my view, survives — but only after a handful of
corrections, one of which is a parameter-identification problem that, left unfixed, undermines the
central "structural instability" result as *currently framed*.

---

## Part 1 — The single most serious finding (all three model audits converge here)

### F1. `b_G = 0.8` is inconsistent with the manuscript's own `V = 20–100 yr` (Grok §2; GPT §6; line-level B‑adjacent)

This is not a typo. It is an internal contradiction between a **physical identification** and a
**numerical value**, and it is the one that most threatens the paper.

The manuscript says (v32 §2.2, §4.1, §4.3):
- "`γ = 1/b_G = 1/V`, the orchard's salvage value (`V` = standing biomass ÷ annual production, ≈ 20–100 yr)"
- "`b_G` the standing-stock value (20–100 yr)"
- baseline `b_G = 0.8`, `b = 0.5`.

The model's bookkeeping gives the turnover time as `V = b_G / b` (standing-stock value `b_G·A` ÷ annual
flow `b·A`). I verified this by hand and in code:

| Quantity at baseline | Value |
|---|---|
| `V = b_G/b` | **1.60 yr** (not 20–100) |
| `1/V = b/b_G` | **0.625 yr⁻¹** |
| reported leading eigenvalue `Re λ` | **+0.625** |

So the manuscript's own relationship gives `1/V = b/b_G`, **not** `1/b_G`. The paper conflates the harvest
coefficient `γ_b = 1/b_G` (units `ha·gha⁻¹`) with the turnover/population-growth rate `b/b_G` (units
`yr⁻¹`). And, numerically, the baseline `b_G = 0.8` implies a **1.6-year** turnover — a fast, crop-like
system — *not* the 20–100-year forest the text invokes everywhere (the orchard, forests, soils, fisheries).

**Why this matters (re-computed, not asserted).** The central result — "monotone instability, a positive
real eigenvalue for every delay, no Hopf" — is a direct consequence of `S = b/b_G + G′(A*) > r`, and at
baseline `S = 0.6083`, driven almost entirely by `b/b_G = 0.625`. I re-ran the zero-delay eigenvalues and the
delayed real-axis roots with a physical turnover `V` (i.e. `b_G = b·V`):

| Turnover `V` | `b_G = b·V` | `S = b/b_G + G′(A*)` | `S − r` | positive real root? |
|---:|---:|---:|---:|:--:|
| 1.6 yr (baseline) | 0.80 | +0.6083 | +0.5883 | **yes** (`+0.625`) |
| 20 yr | 10.0 | +0.0333 | +0.0133 | marginal |
| 50 yr | 25.0 | +0.0033 | −0.0167 | **none** |
| 100 yr | 50.0 | −0.0067 | −0.0267 | **none** |

For `V ≳ 30 yr` the "vicious cycle" (positive real eigenvalue) **vanishes**; the system is no longer
monotonically unstable. So the headline result is an **artifact of the unphysical fast-turnover baseline**, and
as written it is *not* the result the paper claims to be about (forests/soils, `V`~decades).

**Both fixes are legitimate; pick one:**
1. **Treat `b_G = 0.8` as a dimensionless, scaled coefficient and drop the `V = 20–100 yr` identification**
   (i.e. stop claiming `γ = 1/b_G = 1/V` and stop calling `b_G` "the standing-stock value (20–100 yr)").
   Then the structural result holds — but only as a statement about this *scaled* fast-turnover system, and
   the manuscript should say so and drop the ecological-anchoring language that implies a forest.
2. **Set `b_G` from a real turnover time** (`b_G = b·V`, `V ≈ 20–100` ⟹ `b_G ≈ 10–50`) and **recompute** the
   whole spectrum, the delay cliff, and the recover fractions. Under `V = 50–100` the result changes
   qualitatively (no positive real root). This is the honest option if the paper wants to claim to be about
   forests/soils — but it likely reverses the headline finding.

This is the item I would fix first, and it is the only one that can change the *conclusion* rather than the
*wording*. (For reference, the paper is a stylised model and is entitled to use a fast-turnover illustrative
baseline; it is *not* entitled to use `b_G = 0.8` and simultaneously call it a 20–100 yr salvage value.)

Grok put the same point sharply: *"the central dynamical story is not yet shown to be about orchards,
forests, or footprints; it is shown to be about a scaled liquidation gain `b/b_G ≈ 0.63 yr⁻¹ ≫ r`."* I agree.

---

## Part 2 — Genuine mathematical contradictions (high confidence; corroborated by ≥2 audits, and I re-derived them)

### F2. `det = r·ρ·A*/A_max > 0 (never a saddle)` contradicts the neutral continuum — §4.3, §S3.4  (Gemini §1.2; Grok §1.1; GPT §1; line-level B2)

Verified. On the full-harvest family `P = B(A)/e` the Jacobian is **exactly singular**: I re-derived
`det J = (r/b_G)[B′(A*) − b − b_G G′(A*)] = 0`, and `D(0) = 0` is stated in the very next paragraph of the
*same section*. The zero-delay roots are `{0, S − r}`, and "never a saddle / det > 0" is a leftover from the
gross-harvest (Schaefer) model. **The `det > 0` line is wrong; delete it.** The *conclusion* (`a₁₁ < r` for the
non-neutral mode) is right, but the determinant line misstates the structure. (Note: my v31/v32 work added the
`S > r` sufficiency condition but **kept** this erroneous `det > 0` line — so it is still live, and all four
audits correctly flagged it.)

### F3. "`b_G ρ ⋚ b` (equivalently `ψ ⋚ 1/2`)" — §4.1, §S2  (Gemini §1.4; Grok §1.2; GPT §5; line-level B1)

Verified. The manuscript's own closed form `ψ* = 2/(1 + b_Gρ/b)` gives:
- `b_Gρ = b` ⟹ `ψ* = 1` (the marginal/boundary case, where `G(A_max) = 0`); **not** `1/2`.
- `ψ* = 1/2` ⟹ `b_Gρ = 3b`.

So the reading `b_Gρ = b ⟺ ψ = 1/2` is false; the boundary case is `ψ = 1`. Fix to `ψ ⋚ 1` (with `ψ → 1` at the
marginal/boundary case), or drop the parenthetical. Fix both §4.1 and SI §S2.

### F4. `t₅₀ ≈ 145/ρ yr` is a factor-of-20 blunder — §12.2, Prediction 7, §6  (Gemini §1.3; GPT §20-adjacent; line-level B5)

Verified. The reported points `(ρ, t₅₀)` = (0.03, 203), (0.05, 142), (0.08, 105), (0.12, 82) give
`t₅₀·ρ ≈ 6.1, 7.1, 8.4, 9.8` — i.e. `t₅₀ ≈ C/ρ` with `C ≈ 6–10`, **not** `C ≈ 145`. `145/0.05 = 2900 yr`,
which is ~20× the printed 142 yr. The author put the baseline *value* (142 ≈ 145) into the numerator instead
of the dimensionless constant `C ≈ 7.1`. Fix to `t₅₀ ≈ C/ρ`, `C ≈ 6–10` (empirically `≈ 7.1/ρ`).

### F5. "Three delayed states `(A,P,D)`" — §5  (Grok §1.4)

Verified. The model section is careful that delays enter **only** in `G(A(t−τ_g))` and `K(t−τ_p)` and that debt
(7) and harvest act on current values. `D` is a state, not a *delayed* state. The §5 phrasing undoes that
distinction. Fix to "three states; two are delayed" (or similar).

### F6. `b = B/A` contradicts Eq. (2)  (Grok §1.5)

Verified. `B/A = b + b_G G(A)/A ≠ b`. The identifiability *point* (physical hectares, not gha) is valid; the
formula `b = B/A` is not. The audits' suggested fix is right: "a yield coefficient `b` is definable, hence the
two-term split is identifiable." (Or drop the `=` and keep the identifiability argument.)

---

## Part 3 — Genuine model/accounting issues (≥2 audits; some nuance, but real)

### F7. The `σ < 1` "equilibrium locus `P = (σbA + b_G G(A))/e`" is not a *coupled* equilibrium — §2.2, §4.3, §9  (Gemini §1.5; Grok §1.6; GPT §2)

Verified (and this is partly my own v31/v32 wording). In the deficit region at `σ < 1`:
- `dA/dt = 0` gives `E = σbA + b_G G(A)` (the A-nullcline), **so** `P = (σbA + b_G G(A))/e`.
- But Eq. (5) with `K = B/e` (uncapped) requires `P = K = B/e` at a population equilibrium.
- Since `(σbA + b_G G(A))/e < B/e` for `σ < 1`, `dP/dt = rP(1 − P/K) > 0`, so **the population does not stay**
  at that locus; it grows toward `B/e`, and then `dA/dt < 0`.

So the locus is the A-nullcline, not a stationary point of the coupled system, **unless** the carrying
capacity is itself capped at `K_σ = (σbA + b_G G(A))/e` (as §9 does in the Half-Earth/reservation policy).
The manuscript conflates "reserving flow" with "capping population." Fix by either (a) defining `K_σ` and
rewriting Eq. (5) under reservation, or (b) explicitly framing the `σ < 1` locus as a policy-induced
nullcline, not an equilibrium of the baseline model. This is genuine and affects §2.2/§4.3 phrasing and my
v31 verification record's "the true locus is `P = (σbA + b_G G(A))/e`" statement.

### F8. `R_B = 1` is an equilibrium identity, not a trajectory-level stock-decline boundary — §4.5, §6.8, §12.1  (GPT §3; Grok §4)

Verified. In the deficit region `dA/dt = (B̃ − E)/b_G` with `B̃ = bA + b_G G(A(t−τ_g))`, so
`dA/dt < 0 ⟺ E > B̃`, **not** `E > B = bA + b_G G(A(t))`. At a constant equilibrium `B̃ = B`, so `R_B = 1` is
the balance point; along a trajectory with `τ_g > 0`, `R_B = 1` is neither sufficient nor (for a meaningful
minority of collapsing ICs) necessary — which the paper already knows (§12.1, silent collapse) but still
states as the trigger in §4.5. Fix the wording: "`R_B = 1` at equilibrium / zero delay; `R_B` is not the
instantaneous decline boundary along a trajectory when `τ_g > 0`."

### F9. Well-posedness / clamps (`A ≥ A_ext`, `K_min`, `A > A_max` overshoot) are not in the model equations — §2.2, §8, §12  (GPT §7, §8, §27; Grok §7 §9)

Verified and real. Because `G(A) = ρA(1 − A/A_max) < 0` for `A > A_max`, `B = bA + b_G G(A)` can fall below `bA`,
even nonpositive, and `K = B/e` can be nonpositive, so Eq. (5) is undefined on the simulated domain. The `K_min`
floor and the `A ≥ A_ext` clamp (and the softplus `ramp`) are numerical/clamped systems, not Eq. (4)–(6). The
manuscript uses them to produce results that are then claimed for the nominal model. The fix is to state the
admissible domain and the clamp/projection explicitly as a *constrained* system, and to label any result from
a clamped run as such. This does not necessarily change the qualitative picture, but it is a fair
well-posedness objection.

### F10. The recover-vs-collapse outcome is stated twice, incompatibly — §8 vs §12.2  (Grok §1.3; GPT §20, §22; line-level B7)

Verified. §8's delay-response sweep says recover fraction is **flat `0.0529` for all `τ_g ∈ [20,60]`**.
§12.2 says the recover fraction has a deep minimum at `τ_g = 30` (≈0.03) and *re-opens* to ≈0.21 (40), 0.30 (50),
0.32 (60), "real, not a grid artifact." These are two different curves. The reconciliation appears to be that
the §8 flat table is at `τ_p = 25` while the §12.2 re-opening is at `τ_p = 0`. The manuscript never says this,
so Prediction 6 ("collapse whenever `τ_g > 20`") and §8's "field-supported band lies entirely in the collapse
regime" are contradicted by §12.2's own numbers. **Fix:** label which `τ_p` each curve is at; reconcile the two
tables; and soften Prediction 6 to state the *non-monotone* recovery probability (a drop near 18–20 yr, then
re-opening at 40–60 yr for `τ_p = 0`). This is exactly the "reconcile the tables" point GPT §20 and the
line-level audit make.

### F11. The "field-supported band lies entirely in the collapse regime" clashes with the core band 10–40 yr — §8, line-level B4  (line-level B4; GPT §22)

Verified. Core band is 10–40 yr; extended 5–60 yr. The collapse regime is `τ_g ≳ 20`. So the band does **not**
lie entirely in the collapse regime (10–18 yr recovers). Fix to a per-source mapping (as GPT §22's table
proposes) rather than one blanket claim. This is a real internal inconsistency, and it is partly in my v32
§8 wording.

---

## Part 4 — Empirical / citation items (line-level; I re-verified the citations against the sources)

### F12. Neubauer et al. (2013) reference entry is wrong  (line-level A6) — confirmed

The actual paper is **Neubauer, P., Jensen, O. P., Hutchings, J. A. & Baum, J. K. (2013). "Resilience and
recovery of overexploited marine populations." *Science*, 340(6130), 347–349** (DOI 10.1126/science.1230441).
The manuscript entry "(2013). *Resilience of recovering fish populations*. *Fish and Fisheries*, 14(3)" is
wrong in title and journal. Fix the reference.

### F13. The Hutchings & Reynolds "29 % recovered to 50 % within 5–15 yr" is a paraphrase, not the source's headline  (line-level A6) — partly confirmed

Hutchings & Reynolds (2004) *BioScience* 54(4):297–309: "5 years after collapse, 41 % of the 90 populations
continued to decline, 51 % exhibited some recovery, and 8 % had fully recovered;" its *Table 3* gives the
probability of recovery to 50 % of `N₀` over 5–15 yr (e.g. 29 % for all species with ≥50 % decline). So a 29 %
figure does exist but is a table-derived probability, and I should not present it as the abstract's headline
without qualification. **Fix:** cite the table/statistic precisely or soften ("probability of recovery to 50 %
within 5–15 yr ≈ 29 %").

### F14. "Primary forests" is the wrong term — line-level A2 — confirmed

In my v32 Prediction 6 I wrote "with **primary forests** at the top of that range." Poorter et al. (2016) is
about **secondary-forest** regrowth (and a *delay* to 90 % of old-growth, median 66 yr). Also, the band is
built from soils (17–23 yr → 25–33 yr) and fisheries (~20 → ~29 yr); the forest statistic (66 yr to 90 %)
maps to ~95 yr under the same 1.44× heuristic, which is *beyond*, not "at the top of," 25–33. So my clause
mislabeled the source and mis-described the band. **Fix:** rewrite from the SI table; call it secondary
forest; note the 66-yr/95-yr tail is beyond the band.

---

## Part 5 — Notational, over-claim, and register items (real, but lower severity)

### F15. Undefined / drifting symbols  (Gemini §2.3; Grok §5; GPT §19, §30; line-level B10)
Undefined where used: `r_opt`, `q`, `f` (used as both `E = f·bA` and `e/r_opt`), `χ`, `Λ`, `θ`, `Ω`, `τ_e`
(Prediction 4), `A_ref`, `K_min`, `g`, `p`, Scenarios A–E, `T_b` (listed as a parameter but is a prescribed
function of `Δb, κ, t_wave`). In particular `r_opt` has already caused a units error (§9 had to correct
`0.5 B/r_opt` to `0.5 B/e`). **Fix:** define every symbol in §2.1/§4.4 or remove it; add a complete
dimensionless-group table. GPT §19 and the SI symbol table are the right home.

### F16. `R_B` vs `Ω`; two basin numbers unreconciled  (Gemini §2.3, §2.5, §8; GPT §30)
`Ω` appears in §8 but is `R_B` elsewhere (the manuscript itself says "Reconcile the 'max Ω not reported'
footnote"). The two basin/fold numbers `0.506 → 0.042` (full model, continuous) and `39.9 % → 5.3 %` (S0,
208-cell grid) are never reconciled. **Fix:** rename `Ω → R_B`; label which model/grid each basin number is from.

### F17. Over-claimed / conditional results stated as theorems  (Grok §7; GPT §11, §25, §26, §36; line-level B11)
- "debt compounds without bound while technology saturates" — true under multiplicative (8) + bounded `T_b`,
  but not a model-independent theorem. (GPT §11) — condition it.
- "no rescue-by-stock" — §12.1 reports a recovery strip at `A₀ = A_max`, so it is grid/parameter-conditional, not
  structural. (GPT §25). Condition it.
- "measure-zero strip" — a finite-grid single row is not Lebesgue measure zero; the line-level audit
  re-verified 11/208 cells at `A₀ = A_max`. Say "unresolved at grid resolution / concentrated near `A_max`."
  (GPT §26).
- "May (1973) inversion" — rhetoric; May is about random high-dim Jacobians, not this. (Grok §7; GPT §36).
- "`Re λ` independent of `ρ`" — true only at long delay (`e^{−sτ}` kills the `G′` term); at short delay the
  zero-delay root `S − r = b/b_G + G′(A*) − r` does move with `ρ`. State the delay at which the table holds.
  (Grok §7).
- "unboundedly negative `d ln A/dt`" — `A ≥ A_ext` (or 0). The mask is transient because a bounded `T_b` cannot
  offset one-way stock loss, not because the loss is unbounded. (Grok §7). Also `d ln B/dt = d ln b/dt + d ln A/dt`
  assumes `B = bA` and drops `b_G G(A)` (GPT §23).

### F18. Register / "self-instruction" / revision-note tone  (Grok §8; GPT §44; Gemini §3)
Many phrases read as unfinished work: "State `dt`, history functions…", "Analyse the trivial equilibrium…",
"Reconcile the 'max Ω not reported' footnote", "Honesty caveat", "Fit-defect disclosure", "we do not justify
it", "Interval discipline", "must be stated", "report". Convert to completed method / limitations prose or
delete. History functions for the DDE are never actually given — a reproducible-reproducibility gap.

### F19. The two formulations (gross-harvest comparator vs deficit-driven) are mixed under one narrative — GPT §18, §46; Grok §3; line-level B-adjacent
The `χ`/`Λ` fast–slow Hopf classification, `τ_g* ≈ 85 yr`, `τ_p* ≈ 231` (elsewhere `≈ 225`), `π/(2r) = 78.5 yr`,
Prediction 1–2, and the "baseline sits at a knife-edge because `ρ = 3q`" all belong to the gross-harvest
comparator, not the deficit-driven model — which the paper elsewhere says produces no imaginary-axis
crossing. The comparison table is the clearest object in the paper; the surrounding prose should be tagged
`G` (gross-harvest) vs `D` (deficit-driven) and the `χ` classification should move to a clearly-labelled
"what we are not claiming" appendix. Also, §4.1 assigns the §4.3 stability classification to the
*capital-dominated* regime while the numerical `Re λ ≈ +0.62` is computed at the *flow-dominated* `A* = 0.8`,
and at interior MSY (`dB/dA = 0 ⟹ a₁₁ = 0`) `S = 0 < r`, so the sufficiency condition for a delay-independent
unstable root **fails exactly at MSY**. Tag and scope all of this.

### F20. `τ_p*` is stated as two different numbers (231 vs 225) — line-level B6
Unify. Line-level says compare 231 vs 225; I found `≈ 231` (§4.3/§8) and `τ_p* ≈ 225` (§8/§12 comparison table).
This is a real numeric inconsistency in the comparator material.

---

## Part 6 — What the audits got right about **my own** v32 deliverables (and I verify it)

The line-level audit flagged three *v32-specific* problems that I introduced in the v31/v32 revisions, and on
re-computation **it is correct about all three**:

### F21. [data-integrity] The coarse-grid recover-fraction table in `VERIFICATION_of_tau_g_anchoring.md` and SI §S5.1 does not reproduce and contradicts the registered result  (line-level A1)

The verification record and SI §S5.1 state "coarse grid 0.54 at `τ_g = 18` → 0.21 at `τ_g = 20` → 0.00 at
`τ_g ≥ 25`". I re-ran the registered tools:
- documented 13×16 grid (`r1_basin`, dt 0.5 / T 1200): 0.394 (18), 0.240 (19), 0.0529 (≥20).
- 6×8 `COARSE_GRID` (dt 0.5 / T 1200): 0.4167 (18), 0.2500 (19), 0.1042 (≥20).
- `corrected_basin_fraction` default: 0.4115 (18), 0.1894 (19), 0.0326 (20).

**None** reproduce 0.54 / 0.51 / 0.21 / 0.00. And "recover = 0.00 at `τ_g ≥ 25`" directly contradicts the
manuscript's own registered result (`frac_recover = 0.0529` at `τ_g = 30`, the 11-cell `A₀ = A_max` rescue
strip, in `topdown_results.json` `rescue_set`). The audit is right, and this is a real defect in my v32
deliverable: I generated those numbers with an ad-hoc grid/`dt`/`T` in an earlier turn and quoted them into the
verification record and the SI without registering the configuration. **Fix:** re-generate from a stated grid
with the registered code, or delete the coarse numbers from SI §S5.1 and the verification record and keep only
the fine/registered values (`0.399/0.394/0.240/0.0529`).

### F22. SI §S5.1's "reported fine values 0.399 → 0.240 → 0.0529" misquotes §S4.3's four-value table  (line-level A5)
§S4.3 has **four** values: 0.399 (≤17), **0.394 (18)**, 0.240 (19), 0.0529 (≥20). My three-value sequence
omits 0.394@18, so juxtaposed against the coarse (18,20,≥25) it implies fine@18 = 0.399. Fix: quote all four in
column alignment. (Small, but it is a misquotation of the paper's own figure.)

### F23. SI §S5.1's rate/lag caveat rests on "`1/ρ = 20 yr`", but the paper's own measurement is ~142 yr  (line-level A4)
Re-run from the extinction floor at `ρ = 0.05`: `t₅₀ ≈ 141 yr` (the paper's table: 142). The e-folding `1/ρ =
20 yr` is *not* the model's recovery time; it understates the `ρ`-lever's actual timescale by ~7×. Fix: state
the measured `t₅₀ ≈ 105–142 yr` at `ρ = 0.05` alongside `1/ρ`, or drop the `= 20 yr` gloss. (This also
interacts with F4: the correct scaling is `t₅₀ ≈ C/ρ`, `C ≈ 7.1`, so `t₅₀ ≈ 7.1/0.05 = 142 yr` ✓.)

---

## Part 7 — Where I push back / where the audits over-reach

To be balanced, not every claim is a v33 must-fix. I would **not** adopt, or would substantially soften, the
following, on re-examination:

- **Gemini §1.1 (Debt `D` units `gha·yr` → `gha`).** This is a real, genuine dimension question, but it is subtle
  and the manuscript's "`gha·yr` stock" framing is a *deliberate* convention (the flow/stock reconciliation added
  in v30 to address the reviewer's units comment). Gemini is *right* that `∫(gha·yr⁻¹)dt = gha`, not `gha·yr` —
  i.e. integrating a rate over years does not multiply units by years in the way the manuscript's "therefore
  carries `gha·yr`" asserts. This deserves a correct reconciliation (and the "debt ≈ gha·yr" statement does
  need tightening), but I would solve it by clarifying the convention, not by wholesale re-labelling both `D`
  and `α`, because (a) the constraint that `η D` be commensurable with `[E−B]₊` forces `D` to `gha` (so the
  `α` unit must become `gha⁻¹`), and (b) the reviewer-facing v30 response already committed to the flow/stock
  split. **Net:** correct "`D = gha` (and `α = gha⁻¹`) or restate the convention so the integral and the rate
  equation are dimensionally consistent" — treat as genuine but lower priority than F1–F4.
- **Grok §2's "the instability may be an artefact of `b_G`"** — I agree with the *content* (it is F1) but not
  with the framing that it is the *only* reading. The paper is entitled to a stylised, fast-turnover, scaled
  baseline. The error is **not** that `b_G = 0.8` is unphysical; the error is that the manuscript *claims* it is
  a 20–100-yr salvage value while using a value that implies 1.6 yr. So the fix is to pick one identification.
- **Gemini §2.1 (orchard "inverse" wording).** The two phrases are indeed effectively synonyms and cannot be
  "opposites"; the underlying point (Scenario B/C = stock recovers, humans collapse, vs §1's illusion = humans
  sustained, orchard liquidated) is fine. Reword, don't restructure.
- **GPT §32 (no-hysteresis vs fold).** A single-valued threshold for a fixed parameter is not evidence *against*
  hysteresis under parameter cycling, so the "No hysteresis" table row should be scoped — but this is a
  wording/scope point, not a mathematical contradiction, and the paper is consistent within the fixed-liability
  no-delay reading.
- **GPT §4, §24 (ψ as a variable; technology doesn't automatically raise P and E).** These are correct
  *cautions* — `ψ` does vary with state, and `dP`, `dE` are trajectory-dependent. But the manuscript states them
  as *leading/ordering* relations (relative timing of `R_A` vs `R_B` crossings), which is defensible as an
  equilibrium/ratio ordering, not as a full trajectory forecast. Scope them, don't discard them.
- **GPT §21 (the `1.44·t₅₀` conversion is not a legitimate pure-delay estimate).** This re-states exactly the
  rate-vs-lag caveat I already added in v32 (SI §S5.1), plus the F14 correction. It is correct and I have it
  partially; I would keep the empirical anchoring but label the literature values as "scenario ranges" / an
  *effective* timescale (as I did) and make explicit that it is not a pure-delay estimate.

None of these four audits is "wrong"; they just sometimes assign *critical* severity to things that are
moderate, and they occasionally over-reach on scope. The three model audits are especially strong, and the
line-level audit is the most carefully *verified* (it actually re-ran the code) — I independently reproduced
every numeric claim it makes, and found it right including on my own v32 defects.

---

## Part 8 — The two places the four audits disagree with themselves / each other

1. **Grok (F1) and GPT (F6) vs the v30 units reconciliation.** Grok/GPT argue `b_G`/`γ`/`V` are inconsistent
   (and I agree: `1/V = b/b_G`, not `1/b_G`). But the v30 reviewer-response claimed `γ = 1/b_G` as the harvest
   coefficient and the "`b_G` value of one hectare of standing stock." Both are defensible *separately*; the
   error is the manuscript writing `γ = 1/b_G = 1/V`, which links two distinct quantities. The audits are right
   to split them; the response document should too.
2. **Severity of F14/F21 vs tone.** The line-level audit is the most severe on the *verification-record*
   numbers (A1), and I agree it is legitimately the highest-priority *data-integrity* item — but it is an
   artifact of my v32 write-up, not of the model. The model audits (Grok/GPT) are more severe about F1, which I
   judge the more consequential *scientific* issue. Both matter; they are different kinds of "critical."

---

## Part 9 — Recommended v33 fix list, priority-ordered

**Scientific / load-bearing (could change the conclusion):**
1. **Resolve F1 (`b_G` vs `V`).** Either (a) treat `b_G = 0.8` as a dimensionless scaled coefficient and **drop**
   the `V = 20–100 yr` identification (and the "γ = 1/b_G = 1/V" link), or (b) set `b_G = b·V` and recompute the
   spectrum/cliff/recover fractions. Re-verify the `S > r` and "positive real eigenvalue for every delay"
   claims *under the chosen identification*. This is non-negotiable before submission.

**Mathematical/consistency corrections (verified wrong):**
2. Delete `det = r·ρ·A*/A_max > 0 (never a saddle)` (§4.3, §S3.4); state `det J = 0`, roots `{0, S−r}`. (F2)
3. Fix `ψ ⋚ 1/2` → `ψ ⋚ 1`/drop (§4.1, §S2); fix the marginal-row labels. (F3)
4. Fix `t₅₀ ≈ 145/ρ` → `t₅₀ ≈ C/ρ, C ≈ 6–10 (≈ 7.1/ρ)` (§12.2, Prediction 7, §6). (F4)
5. Reconcile the §8 flat `0.0529` (τ_p=25) vs §12.2 non-monotone re-opening (τ_p=0) tables; label `τ_p`; soften
   Prediction 6 to non-monotone recovery probability. (F10)
6. Resolve `σ < 1`: define `K_σ = (σbA + b_G G(A))/e` and rewrite Eq. (5) under reservation, *or* frame the
   locus as a policy nullcline. (F7)
7. Scope `R_B = 1` as equilibrium/zero-delay identity, not trajectory boundary (§4.5, §6.8). (F8)
8. "Three delayed states" → "two delayed"; `b = B/A` → identifiability phrasing. (F5, F6)
9. Unify `τ_p*` (231 vs 225); rename `Ω → R_B`; label the two basin numbers. (F20, F16)
10. State the admissible domain and the clamps (`A ≥ A_ext`, `K_min`, `A > A_max`) as a constrained system;
   label clamped-run results as such. (F9)

**Correct the two empirical readings I introduced and the baseline-restated values:**
11. Fix the Neubauer citation (F12); qualify the H&R 29 % (F13); "secondary forests" + the 66-yr/95-yr tail
    beyond the band (F14). Re-verify the τ_g anchor's rate/lag caveat against `t₅₀ ≈ 142 yr`, not `1/ρ = 20 yr`
    (F23), and quote all four fine values (F22).

**Data-integrity (my own v32 write-up):**
12. **Regenerate or delete the unreproducible coarse-grid table in `VERIFICATION_of_tau_g_anchoring.md` and
    SI §S5.1** (F21). Use the registered grid/code and re-verify, or keep only the registered fine values.

**Notation / scope / register:**
13. Define/remove `r_opt, q, f, χ, Λ, θ, Ω, τ_e, g, p, A_ref, K_min` (§2.1, §4.4); add a dimensionless-group
    table. (F15)
14. Tag `G` (gross-harvest) vs `D` (deficit-driven); move the `χ`/Hopf classification to "what we are not
    claiming"; scope the MSY/regime statements and the "`Re λ` independent of `ρ`" (state the delay). (F19)
15. Condition the "theorem / no-rescue / measure-zero / May / compounding" claims. (F17)
16. Remove revision-note register ("history functions," "interval discipline," "we do not justify it," etc.); state
    the history functions explicitly. (F18)

**Records / package hygiene (would not affect the science but affect submission):**
17. Re-point the live symlink `data/IMPLEMENTED_revision_ECOMOD.md` (11 revisions stale, → v32). (line-level C1)
18. Append CHANGELOG v20–v32. (line-level C2)
19. Regenerate `supplementary/ABSTRACT_submission.tex` from the v32 abstract (it is v30, unscoped 300-word, and
    asserts the very claim v31 corrected); fix the "300 words" description. (line-level C3)
20. Commit `demo_unified.py`/`mask_rk4.py` or re-point the §10/Reproducibility drivers (two don't exist). (line-level C4)
21. Add the Zenodo deposit sentence to the md (currently only in the tex). (line-level C5)

---

## Bottom line for the author

The four audits are **not noise**. They converge on a real set of issues, and after re-deriving every
load-bearing one I find the following claims **true and worth fixing before submission**:
- F1 (`b_G`/`V`), F2 (`det > 0`), F3 (`ψ ⋚ 1/2`), F4 (`t₅₀ ≈ 145/ρ`), F10/F11 (recover-table and empirical-band
  reconciliation), F7 (`σ < 1`), F8 (`R_B` trajectory), F12–F14 (empirical/citation), and F21–F23 (my own v32
  verification-record defects).

The single most consequential is **F1**: a parameter-identification error that makes the headline "structural
vicious cycle" depend on a fast-turnover coefficient the manuscript simultaneously claims is a 20–100-yr
salvage value. That one can change the conclusion and must be resolved first.

What is **not** needed is a rewrite of the model: the deficit-driven family `P = B(A)/e`, the `R_B`/`R_A`
ratio split, the delay-driven basin crisis, and the transient masking window are all verified sound, and the
audits agree the scientific core is real. The required work is precision and one honest choice about what
`b_G` means.

*Verified read-only. All numbers above were recomputed with the registered model code or the original
published sources; no claim was taken on face value from any of the four audits.*

---

## Part 10 — Addendum: remaining audit points worth including (as-is / modified / corrected)

This addendum answers "are there any points from the four audits still worth adding?" It lists the items I
did **not** already carry into Parts 1–9, with a verdict on each: **[AS-IS]** = include as written,
**[MODIFIED]** = include after correction, **[VETTED]** = verified against the model/source before including,
**[ALREADY-HANDLED]** = the manuscript already addresses it, so only a note is needed, **[OMIT]** = drop or
reduce to a one-liner (I disagree with the severity or it does not survive scrutiny).

### R1. [VETTED — MODIFIED] "No imaginary-axis crossing" must exclude the permanent zero root (GPT §16)

GPT is correct and this refines my own v31/v32 wording. Because `D(0)=0` on the equilibrium family *for every
delay*, the claim "the exact `s=iω` crossing-curve scan finds zero imaginary-axis crossings" is literally false
if `ω=0` is included. **Include, modified:** say "**no nonzero** imaginary-axis crossings (Hopf) were found;
the zero root `s=0` persists for every delay due to the equilibrium continuum." This is a precision fix to the
no-Hopf claim and should be applied wherever the phrase appears (v32 md lines ~406, ~628, ~707, ~785, ~1100).

### R2. [VETTED — MODIFIED] The three-fold accounting fusion (flow yield / surplus production / standing stock) — Grok §6

Grok identifies a real conceptual fusion I under-weighted. The manuscript repeatedly conjoins three distinct
quantities: (1) flow yield `bA` (fruit), (2) surplus production `b_G G(A)` (increment/MSY harvest), (3) standing
stock `A` (the trees). Eq. (2) puts (1)+(2) into `B`; Eq. (4) subtracts harvest above (1) from (3) **net of**
(2). Consequences Grok correctly draws:
- `bA < E < B` does **not** "leave capital growth untouched" — it harvests part of the increment and the stock
  still rises.
- capital growth is **not** "removable only by liquidating the base" (that phrase describes the stock, not the
  increment).
- true liquidation (`dA/dt < 0`) is `E > B̃` (taking more than (1)+(2)).
- the orchard fruit/trees story matches **only** the flow-dominated limit (`ψ → 1`, baseline).

**Include, modified:** reword the "leaves capital growth untouched" and "removable only by liquidating the
base" passages; state up front that the orchard metaphor is the flow-dominated/baseline regime and that the
interior-MSY/fold/Scheffer language is a different, largely-un-numericked regime. Verified: with
`b_Gρ < b` (baseline) the fruit/flow story is exact; at `b_Gρ > b` (capital-dominated) it is not.

### R3. [VETTED — MODIFIED] The equilibrium family is a *degeneracy* of the chosen closed-loop equations, not a generic property — GPT §39

GPT is right, and this recontextualises the "one-parameter family `P = B(A)/e`" result that v31/v32 emphasise.
The continuum arises because `dP/dt = 0` forces `P = K = B/e` exactly, **and** `E = eP = B` makes the stock
equation balance identically. That is a structural degeneracy of defining demand through a logistic population
equation whose equilibrium is exactly the algebraic carrying capacity — **not** a general property of stock-flow
systems. **Include, modified:** add one sentence: "The equilibrium continuum is a consequence of defining
demand through a logistic population equation whose equilibrium is exactly the algebraic carrying capacity; it
is not a generic property of stock–flow systems."

### R4. [VETTED — MODIFIED] The fixed-liability root displayed is only the minus root; the plus (stable) branch is essential — GPT §13

Verified. The quadratic `B(A) = E` has two roots
`A_± = A_max/(2 b_Gρ) [ (b+b_Gρ) ± √((b+b_Gρ)² − 4 b_Gρ E/A_max) ]`; the manuscript (v32 §4.2, `A_c(E)`) displays
only `A_−`. In the capital-dominated regime there are genuinely two fixed points — the minus root has
`B'(A) > 0` (unstable), the plus root `B'(A) < 0` (stable). But the plus root is **admissible only when it lies
inside the stock domain**: I verified that at `b_Gρ = 0.64, b = 0.5`, `A_+ = 1.31 > A_max = 1.2` at `E = 0.95 B_max`
(so the "stable" branch falls outside the domain), whereas at `b_Gρ = 1.25`, `A_+ = 1.03 < 1.2` (in-domain).
**Include, modified:** display both roots and state that the plus/stable branch is the fix only when it lies in
`(0, A_max)`, which holds once `b_Gρ` is large enough; the "two fixed points, one stable one unstable" claim
should be scoped to that regime.

### R5. [MODIFIED] Nested delayed-state dependence in `K(t−τ_p)` — GPT §29

GPT flags that `K(t−τ_p) = B(t−τ_p)/e` needs to state whether the delay applies to `A` only or to `b`, `D`, and
`A` together (since `b = (b₀+T_b)e^{−αD}` depends on the delay-time debt if evaluated consistently). The
manuscript states the delay enters through `K(t−τ_p)` but does not spell out the nested state dependence.
**Include, modified:** add one line — "`K(t−τ_p) = B(t−τ_p)/e` where, on the constant-parameter S0, `b` and `D`
are held constant so `B(t−τ_p) = b A(t−τ_p) + b_G G(A(t−τ_p))`; in the full model the delayed `B` is evaluated at
the time-`(t−τ_p)` state." This is a reproducibility/clarity point.

### R6. [MODIFIED] Add a single baseline registry — GPT §30

The manuscript uses several parameter sets (`b_G=0.8`, `b₀`, `r_opt`, gross-harvest comparator, policy-cap
`0.5B/e`, `E=0.15/0.30/0.50`) without one registry. GPT asks that every numerical result carry: model
formulation, active equations, parameter vector, delays, initial history, solver, termination rule. **Include,
modified:** a compact registry/table in §8 (or the SI) binding each headlined number to its formulation
(`D0` constant-b, `D` full, `M` mask, `G` gross-harvest, `R` reservation). This subsumes F15/F16/F19 and is the
cheapest way to pre-empt the "which model is this number from?" objection.

### R7. [MODIFIED] §4.1's opening is immediately contradicted — GPT §12

Verified. v32 line ~294 states unqualified "the sustainable equilibrium is interior (`A* < A_max`), not
`A_max`", then lines ~300–303 state "the baseline sustainable state is the boundary `A_max`" (because
`b_Gρ = 0.04 < b = 0.5`). The first is the capital-only case introduced as if general; the second is the
qualified one. **Include, modified:** scope the interior formula with "when `b_Gρ > b`" before presenting it, and
state the flow-dominated/boundary case as the baseline. (This reinforces F19/R2's regime-scoping.)

### R8. [MODIFIED] CSD / return-time needs an explicit definition and is delicate near a zero eigenvalue — GPT §33

The manuscript states the `P`-relaxation return time is flat ≈150 yr then disappears, but does not define the
perturbation amplitude, direction, observable, fitting window, or how return time is defined when the
equilibrium is unstable; and because the family has a zero eigenvalue, a neutral tangent direction can produce
apparent slow recovery unrelated to a saddle-node. **Include, modified:** define the return-time observable and
separate transverse-return-time from tangent-to-manifold drift; scope the "no critical slowing down" claim
accordingly. (This is a fair caveat on the CSD/early-warning discussion.)

### R9. [MODIFIED] Intro wording / minor prose — Gemini §3, Grok §9

- "trees **regrow** fruit" → "trees **bear** fruit" (Gemini; a genuine biological slip).
- "the system is therefore a **delay differential equation**" → "we therefore model it as **coupled delay
  differential equations**" (category error).
- "early-warning signal is an observational indicator, not an intervention **lever**" (Gemini §3 P9) — scope the
  "nonexistent levers" sentence.
- "repayed" → "repaid"; "`dP/dt` diverges" → "the right-hand side is undefined at `K=0` and `→ −∞` as `K ↓ 0`"
  (Grok §8/§9).
**Include** as a low-severity prose round.

### R10. [VETTED — MODIFIED] §12.3's `b_G` sweep is too narrow to test the physical meaning; and `D = ∫[E−B]₊dt` should say "modulo repayment" — Grok §2

Grok's supporting evidence for F1 is worth making explicit: the §12.3 `b_G` sweep (0.4–1.2) never reaches the
physically-motivated decade, so it cannot test the turnover inconsistency. And `D = ∫[E−B]₊dt` (as stated in
§2.1) ignores `η` in (7) — add "modulo repayment" or "when `η=0`". **Include, modified:** state that the `b_G`
sweep is confined to the fast-turnover range and does not probe the `V = 20–100 yr` identification; and correct
the `D` integral phrasing.

### R11. [MODIFIED] "Protective institutional stance" / "stabilising sign is protective" are not modelled controllers — GPT §40, §42

The conclusion recommends "adopt the protective, effort-reducing institutional stance" and refers to a
"stabilising sign is protective," but the baseline model has no effort-control/governance variable — it has a
population state and `E = eP`, with the reservation imposed as a cap, not a feedback controller. **Include,
modified:** label these policy extensions/control interpretations, not baseline-model results.

### R12. [MODIFIED] Several §6 "predictions" are restatements of assumptions or outputs — GPT §41

Prediction 3 (`t_peak` follows from any simulation), Prediction 4 (`τ_e` vs `f` is not mathematically defined),
Prediction 7 (rate/lag decoupled because they are separately placed), and Prediction 8 (`R_B=1` is an algebraic
identity) are not yet falsifiable as stated. **Include, modified:** for the ones kept, add an estimand and an
intervention/null/sign — e.g. for Prediction 4, `∂J/∂τ_e` vs `∂J/∂f` for a declared outcome `J`.

### R13. [ALREADY-HANDLED] Exact-switch vs softplus mixing — GPT §28

On re-reading, the manuscript **already** handles this: §8 requires the exact `[·]₊` switch ("never a smooth ramp,
because a softplus ramp leaks depletion when `E < bA`") and §10 explicitly labels the mask demo as the "well-posed
smooth-ramp solver" with `w = 0.05` and states insensitivity to `w`. So GPT §28 is **not** a live defect. Include
**only** as a one-line confirmation: "state which results use the exact switch (collapse/cliff/S0) vs the smooth
ramp (mask window), which §8 and §10 largely do." Do not treat this as a v33 must-fix.

### R14. [MODIFIED] Consolidate repeated claims and tag the parallel formulations — GPT §45, §46; Grok §3

`R_B = 1`, the `τ_g ≈ 20` cliff, no-Hopf, `+0.62`, the neutral continuum, the narrow mask window, "no
rescue-by-stock," and the protective sign each recur across §4, §5, §6, §8, §12, §13, §14 — not always under the
same assumptions. And the manuscript mixes several models (full delayed-debt; constant-`b` S0; reduced mask with
softplus; gross-harvest comparator; reservation policy). **Include, modified:** consolidate each claim into one
statement and refer back; tag the formulations (`D`, `D0`, `M`, `G`, `R`). This is the structural fix that makes
all of F19/GroK-§3/GPT-§46 actionable.

### R15. [MODIFIED] Make the silent-collapse fraction a figure — Grok §7

The 36.5 % (72/197) silent-collapse figure is useful and consistent (94.7 % collapse); Grok recommends it become
a figure rather than a prose number. **Include** as low-severity presentation.

### R16. [OMIT — reduce to a scoping line] Phase-line argument & "no path memory" — GPT §34, §35

GPT §34 (import the cod-style phase-line logic) and §35 ("a fixed scalar autonomous equation has no path memory")
refer to a *different* (cod) analysis not in this paper and overstate a general point. I would **omit** §34, and
reduce §35 to a one-liner already implied by GPT §32/R14: "for the fixed-liability one-dimensional reduction the
threshold is single-valued; hysteresis under parameter cycling was not analysed." No separate action.

---

*The read-only verification above recomputed R2 (accounting), R3 (degeneracy), R4 (fixed-liability roots) and
R7 (§4.1) directly; R13 was checked against §8/§10 text; R16 was judged on scope rather than re-derived.*

---

## Part 11 — Further remaining audit points (verified before adding)

Recapturing the rest of the four audits, these are the items not yet carried into Parts 1–10. The `[VETTED]`
ones were checked against the model equations/sources or the manuscript text before they were included.

### S1. [VETTED] "`η` decides whether an equilibrium exists" is too broad — GPT §10; §3 assumption (7)

Verified. Eq. (7) `dD/dt = [E−B]₊ − ηD`:
- **No overshoot** (`E ≤ B`): `[E−B]₊ = 0`, so `dD/dt = −ηD`, `D → 0` **regardless of η**, including `η = 0`.
  The σ=1 continuum `P = B(A)/e` is exactly of this `E ≤ B` form, so η does **not** decide whether *these*
  equilibria exist.
- **Persistent overshoot** (`E > B`): `D* = (E*−B*)/η`, so `η > 0` gives a **finite** steady debt.

So "the full overshoot model has an equilibrium only because of η" (§5) and "η is primary (it decides whether an
equilibrium exists)" (§3) are too broad. Manuscript line ~1119 does already qualify ("where η decides whether an
equilibrium exists … a reader setting η = 0 deliberately removes…"). **Include, modified:** narrow the claim to
"`η > 0` provides a finite steady debt for an equilibrium that persistently consumes capital (`E* > B*`); it is
not required for the `E ≤ B` continuum." This is a real, verified overstatement that three places should share one
statement.

### S2. [VETTED] The `d ln B = d ln b + d ln A` identity holds only for the flow component, and `d ln A/dt` is not unbounded — GPT §23; Grok §7

Verified. With `B = bA + b_G G(A)`:
- `d ln B/dt = (1/B)(ḃA + bȦ + b_G G′(A)Ȧ)`, which **is not** `d ln b/dt + d ln A/dt` unless `B = bA` (flow
  component only).
- `d ln A/dt = Ȧ/A` is **bounded below** because `A ≥ A_ext > 0` (not "unboundedly negative").

So §6's "why the illusion is necessarily transient" argument rests on a missing `b_G G(A)` term and on an
"unboundedly negative" rate that is in fact bounded by the extinction floor; the mask is transient because the
bounded logistic `T_b(t)` cannot offset the one-way stock loss `A₀ − A_ext`, not because the log-rate diverges.
**Include, modified:** carry the argument on the flow component `bA` only (or derive the correct total derivative),
and replace "unboundedly negative" with "bounded below by the extinction floor." This also reinforces R3 (the
degeneracy framing) and F17/R16 (scope).

### S3. [VETTED] `R_B` is defined on `B` but derived on `B̃` — operating-trigger notation ambiguity — Gemini §2.4; Grok §4; GPT §3

Verified. The manuscript defines `R_B = E/B` (current biocapacity, md line 458) but derives the balance point as
`R_B = E/B̃ = 1` (line 382), where `B̃ = bA + b_G G(A(t−τ_g))`. These are **different quantities** for `τ_g > 0`.
This is the same family of issue as F8 (trajectory vs equilibrium) but specifically about **which `B` the ratio is
built on**. **Include, modified:** state the operating trigger on `B` (the monitored/accounting quantity) and note
that the *dynamic* stock-decline boundary uses `B̃`, so `R_B = 1` on `B` is the balance point only at equilibrium /
zero delay. This makes the "watch `R_B`" advice (F8/R-monitor) internally consistent.

### S4. [MODIFIED] The eigenvalue `0.608–0.625` range is correct but under-labelled — GPT §17

Verified: `0.608` and `0.625` are the **same leading root at different `τ_g`** (at `τ_g=0` the non-neutral root is
`S−r = 0.5883`; it rises to `0.625` as `τ_g` grows), and `S = 0.6083` (the sufficiency value) is not itself an
eigenvalue. So this is **not a contradiction**; GPT is right only that each eigenvalue should carry its
`(τ_g, τ_p)`. **Include, modified:** add "(at `(τ_g,τ_p)`)" to each eigenvalue and, in §4.3/§8, note that the
"`Re λ = +0.625` across the plane" is the large-`τ_g` plateau while the `0.608/0.5917` values are at smaller delay
(the same root). This turns what reads as a discrepancy into a single labelled function.

### S5. [MODIFIED] Numerical claims are more precise than the stated verification — GPT §31

Values such as "balanced accuracy 99.2 %", "36.5 % (72 of 197)", "recover fraction 0.0529", "`Re λ = +0.625`",
"critical deficit ≈0.075", and "overshoot exponent 4.84" are presented to 3–4 significant figures. The line-level
audit already found most of these **reproduce exactly**; the issue is that they should each carry their grid,
tolerance, classification threshold, and time horizon (a registry, R6). **Include, modified:** attach a
`(grid, tolerance, threshold, T)` block to the headline numbers, or state their uncertainty explicitly. This is a
presentation/precision point, not an error.

### S6. [MODIFIED] The empirical programme needs an observation model — GPT §43

`R_B = 1` is derived from the model's accounting identity, but actual NFA biocapacity does not observe `A`, `b`, or
`G(A)` directly. To test the model, one needs an observation model `(A, b, D) → (B, E)`. The manuscript's §11
"flux reconstruction" already gestures at this; **include, modified:** state explicitly that the empirical
programme can test *association*, not the model's *causal* threshold, unless the observation link is specified.
(Relates to F8/F17 and Grok §4's "advising a policy-maker to watch `R_B` needs an operational series for the
surplus-production term.")

### S7. [MODIFIED] `γ` should be added to the symbol table as its own entry; `A_ref`, `K_min` undefined — Gemini §4 table; GPT §19

Gemini's master parameter reconciliation table lists `γ = 1/b_G` (the liquidation coefficient, `ha·gha⁻¹`) as
needing a formal symbol-table entry, and `A_ref`, `K_min` as undefined. **Include, modified:** add `γ` to Table 2.1
distinct from the turnover rate `b/b_G` (this is the substance of F1/F6 — the two must not share a symbol); define or
remove `A_ref` and `K_min`. This consolidates F6, F15, and Grok §2.

### S8. [MODIFIED] §7 "Presentation" mixes thesis + figure caption + style rules; §9's controller language is off-register — Grok §8

Grok notes §7 mixes a thesis restatement, a figure caption, a literature paragraph, and style rules; and §9's
"certified kernel / typed floor / exact-tube semantics / observation operator" is a different discipline's voice.
**Include, modified:** move the style rules out of §7 (into a submitted "notes on presentation" or the SI), move the
literature connections to §1 or a dedicated subsection, and render §9's policy content in ecological language (the
usable content — protective vs extractive sign; reservation as a population cap; don't transfer DDE stability to
sample-and-hold — survives translation). Relates to F18.

### S9. [MODIFIED] The "classification describes fast–slow reduction, not the model" should not sit beside the model's own results — GPT §18

GPT asks that the `χ`/`Λ` gross-harvest Hopf classification be moved to a separate, labelled
"gross-harvest comparator" subsection so the deficit-driven result is not read as arising from it. This is largely
**already the intent** in §4.3 (the manuscript says "this Hopf classification is **not** realised"), but the
placement and the predictions (1–2) still invite the misreading. **Include, modified:** a subsection header
"Gross-harvest comparator (not the deficit-driven model)" and a short "what we are not claiming" note. Consolidates
F19/Grok §3 into one action.

### S10. [OMIT or one-line] "Phase-line / no path memory" (GPT §34–§35) — same as R16; and "`B` vs `B̃` in §4.5" is folded into S3.

No new action beyond R16/S3; noted to avoid repeated flagging.

---

*The `[VETTED]` items in this part were verified against the model equations (S1, S2, S3), the registered code (S4),
or the manuscript text (S5–S9). No claim was added on face value.*
