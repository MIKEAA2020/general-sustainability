# Paper 2 — Joint Audit of the "Nonstandard Obstruction Calculus" Proposals

**Input:** `uploads/obstruction calculus nonstandard.txt` — two stacked proposal documents:
- **Doc 1** (`gpt:`, §§1–14): *Recourse-aware continuous-to-finite nonviability certification* — a continuous-time theorem package (adjoint safety rows, finite obstruction certificate Γ, moment-approximation LP with value sandwich, atomic duality, sparsity law), a sharp limitation result (§8: the m+1 bound fails for blind control functions), a refinement-erosion identity (§9.1), an oracle-recourse sound extension (§9.2), a four-dimensional three-branch worked instance (§11) with explicit finite LP, Farkas certificate and mesh study (§12), and venue advice (§14: SCL; "does not yet justify an Automatica claim").
- **Doc 2** (§§1–8, truncated): *Robust Viability Under Partial Observation* — a re-derivation of paper 2's spine in the paper's own notation, claiming three nonstandard survivals: sparse dual obstruction (Thm 3), uniform adverse margin with explicit exit bound (Thm 6), blind-window timing certificate with exact LP reduction (Thm 7 + Lemma 6.1).

**Method:** every checkable number and inequality was re-derived independently in exact
rational arithmetic (`paper2_nonstandard_verification.py`, **51/51 checks pass**), and every
claimed-novel item was mapped against the v42 source. Neither document's code was trusted:
doc 1's §12.2 verifier was executed *and* the same facts re-derived from scratch (V-0 vs V-1).

## Verdict summary

| Proposal item | Verdict | Action |
|---|---|---|
| D1 §11–12 three-branch instance + Farkas + mesh study | **Correct** (all values verified exactly) | **Accepted → v43 §3.7** (compressed instance) |
| D1 §9.2 oracle-recourse certificate | **Correct, sound, incomplete** (as stated) | **Accepted → v43 §3.7** (proposition) |
| D1 §8 "m+1 is false for blind control functions" | **Correct** (rank q verified; all q+1 witnesses necessary) | **Accepted → v43 remark in §3.4** (scoping caveat) |
| D1 §9.1 refinement-erosion identity | **Correct** (φ_U superadditivity verified on 3,240 rational pairs) | Deferred (companion) — the identity belongs to the LP certificate functional, which the main text does not carry |
| D1 §§2–5, 10, 12.3 full continuous-to-finite package | **Correct internally** (sizes and error laws verified; ρ(h) values match the closed-form lower bound; *LP optimality not independently certified — no solver run*) | **Deferred to companion paper** (matches Doc 1's own §14 venue assessment) |
| D2 Thm 3 (sparse dual, m_u+1, Farkas, robustness lemma) | Statement+proof overlap **v42 §3.2/prop:helly**; the **robustness lemma is new** | **Robustness lemma accepted → v43 remark in §3.2**; rest: already present |
| D2 Thm 6 (uniform margin ⇒ explicit exit bound) | **Already in v42, stronger**: `thm:exit` gives t_exit ≤ q(x₀)/ε ≤ a/ε on a strip (not just a tube ball) plus the comparison-function refinement `rem:comparison` | No action (overlap recorded) |
| D2 Thm 7 + Lemma 7.1 (timing certificate) | **Already in v42**: `thm:delayed` + `rem:sigma` (σ* threshold) | No action; 7(c)'s set-inclusion erosion is a notational variant of the §6.5 discussion |
| D2 Lemma 6.1 (averaging ⇒ held-control polyhedron) | Sound; new relative to v42 | Deferred (companion; it is Doc 1 §5's noiseless special case) |
| D2 Thms 1–2, 4–5 (recursion, trees, DAG, nesting) | Standard/already present (`§3.1`, `prop:ladder`; v42 also already flags worst-case exponential complexity at §3.1) | No action |
| D2 §8 algorithm/complexity | Truncated in the attachment; no actionable content beyond what v42 states | No action |

## Verification results (highlights)

- **Doc 1 §11–12 (V-0 to V-2).** λ = (3/8, 5/16, 5/16) sums to 1 with Σλ_j n_j = 0; the
  input-facet multipliers satisfy F⊤η_j = −n_j, f⊤η_j = 1; Γ(τ) = τ − 7/50 exactly;
  τ_max = 7/50 with the converse policy's worst violation equal to Γ (so J(τ+1) = τ − 0.14);
  pair critical positions 2469/1250 and 2419/1250 at τ = 1/5 (six of seven priors viable);
  Farkas contradiction −3/100; and the mesh table is internally consistent:
  mQ and Ms(N_t+1)+p_U·Q reproduce all five dimension counts, and ρ(h) = 0.06 − Th/4
  reproduces all five values (the §12 text value e = 12h²/4 is the h = 1/10 instance of the
  same law, since T/h = 12 there).
- **Doc 1 §8 (V-3).** For every q tested: the full q+1-mode system is infeasible, every
  proper subset is viable, and the kernel rank is exactly q — the Helly count for blind
  window-policies is information–time rank (q+1 witnesses), not input dimension (m+1 = 2).
- **Doc 1 §9.1 (V-4).** φ_U(g₁+g₂) ≥ φ_U(g₁)+φ_U(g₂) on 3,240 deterministic rational pairs
  for the hexagonal U: refinement erodes the certificate by the stated exact gap.
- **Doc 1 error bounds (V-6).** Both (4) and the Step-2 control bound survive adversarial
  checking (variation concentrated inside one mesh interval). They are valid as stated, with
  a factor-2 sharpness margin in the concentrated case (constant 1/2 available).
- **Doc 2 (V-5).** The tangency↛tube counterexample verified (q(t) = 0.1t − t² strictly
  negative on (0.1, 1]); the robustness lemma verified on rational data (the hypothesis
  μ ≤ −λᵀc is part of the statement); Thm 7(c) is the contrapositive of (b).

## Defects and corrections

1. **Doc 2's novelty labels are overstated against v42.** Thm 6 ("NEW") is dominated by
   v42's `thm:exit` + `rem:comparison`; Thm 7 ("NEW") by `thm:delayed` + `rem:sigma`; Thm 3's
   core by §3.2 + `prop:helly`. The audit table above gives the exact mapping. What survives
   as new: the robustness lemma, Lemma 6.1, and (from Doc 1) the recourse certificate and its
   instance.
2. **Doc 1's mesh study claims "exact LP values" without a solver run.** The values match the
   closed-form lower bound ρ(h) = 0.06 − Th/4 and all dimension counts verify exactly, but
   optimality of the LP values was not independently certified here. Doc 1 itself flags this
   honestly; a companion implementation must run the LPs.
3. **Doc 2 Lemma 7.1 says "a.s. constant"** in a deterministic model; the correct reading is
   plain constancy (measurability w.r.t. the trivial σ-field). Cosmetic.
4. **Doc 1's completeness claim (iii) needs the effective-computability caveat it states**
   (meshes with errors tending to zero); v42's §3.1 already carries the matching honesty
   about exponential worst-case complexity, so nothing further is required in the main text.
5. **No defect found in Doc 1's arithmetic.** Two suspicion leads were checked and *cleared*
   during verification: the h_d factor in eq. (4) is correct (the per-interval bound
   ∫‖w−avg‖ ≤ |J|·TV absorbs the interval length), and "min of finitely many AC functions"
   in Doc 2's Thm 6 proof is genuine (min of AC functions is AC).

## What v43 implements (and why it is merited)

v42's §6.5(ii) concedes: *"no continuous-time certificate for it is supplied here"* for the
**insufficient post-observation recourse** mode (blind-window safety, post-observation
failure), exhibiting only a discrete no-certificate instance (Supplementary A.3). Doc 1's
§9.2 + §11 fill precisely this gap, and Doc 1's own venue analysis (§14: SCL-scale package)
says the *full* LP program is companion material. v43 therefore adopts the minimal
Automatica-scoped subset:

1. **New §3.7 "A recourse certificate for the post-observation mode"**: the oracle-relaxed
   recourse proposition (sound against every measurable information-adapted policy;
   generally incomplete, stated as such) + the compressed three-branch instance with the
   exact threshold τ_max = 7/50 and certificate Γ(τ) = τ − 7/50.
2. **§3.4 scoping remark**: the m+1 sparse-witness bound is instantaneous; window-policies
   are governed by information–time rank, with Doc 1's q+1 scalar-input construction as the
   one-paragraph counterexample.
3. **§3.2 remark**: graceful degradation and the residual-tolerant Farkas test
   (λᵀ(c+Δc) ≤ −μ + ‖λ‖₁ε; c + Σ_j h_U(−r_j) < 0).
4. **§6.5(ii) limitation rewritten** to credit the new certificate while keeping the
   completeness gap open; **Organization (§1.4) updated**; **Supplementary A.3 aligned**
   with a pointer to §3.7.

**Deferred (companion paper, recorded here and in the addendum, not in the article):**
the full continuous-to-finite LP theorem (value sandwich, atomic duality, error budget),
Lemma 6.1, the refinement-erosion identity as a standalone result, and a solved mesh study.
