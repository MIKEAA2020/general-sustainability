# v43 — joint-audit implementation (recourse certificate, scoping, robustness)

## Provenance

Implements the accepted items of the joint audit of the two "nonstandard
obstruction calculus" proposal documents (`paper2_nonstandard_joint_audit.md`).
All checkable mathematics in the proposals was re-verified independently in
exact rational arithmetic (`paper2_nonstandard_verification.py`, 51/51 checks
pass) before any of it entered the manuscript.

## Changes (main text)

1. **New Section 3.7 — "A recourse certificate for the post-observation
   mode."** Proposition (oracle-recourse obstruction): for branches
   observation-equivalent on [0, τ) and dynamics affine in the control, a
   finite weighted adjoint-kernel certificate Γ(λ) > 0 — with the bracket
   infimized over admissible disturbance realizations — excludes every
   measurable information-adapted policy, including arbitrary post-observation
   recourse per branch (oracle relaxation; sound, generally incomplete, stated
   as such). Proof by pooling: the pre-τ term pools through one common signal,
   the post-τ terms separate per branch, with φ_U superadditivity measuring
   the relaxation loss. Worked instance (three branches, delayed recourse):
   full-information viability of every branch (93/50 < 2), blind-window
   safety of u ≡ 0, and Γ(τ) = τ − 7/50 giving the exact delay threshold
   τ_max = 7/50; every pair viable at τ = 1/5 (critical positions 2469/1250
   and 2419/1250), so six of seven priors are viable where the triple is not;
   discrete no-certificate analogue in Supplementary A.3.
2. **Section 3.4 scoping remark.** The m+1 sparse-witness count governs
   instantaneous common actions; for blind window-policies the governing
   count is the information–time rank, with the q+1-branch scalar-input
   construction (block-indicator kernels of rank q, all q+1 branches
   necessary) as counterexample to any m+1 = 2 claim.
3. **Section 3.2 remark (numerical robustness of the polyhedral
   certificate).** Graceful degradation under bounded data perturbation
   (μ⊤(b+Δb) ≤ −μ₀ + ‖μ‖₁ε; normalized multipliers maximize the tolerable
   perturbation); the residual-tolerant infeasibility test
   c + h_U(−r) < 0 without exact stationarity; the orientation rule that
   uncertain row data must be relaxed toward the controller.
4. **Section 6.5(ii)** rewritten: the post-observation mode is now certified
   in continuous time (sound, oracle-relaxed), with completeness still open;
   **6.5(i)** certificate range extended to 3.5–3.7; **Section 1.4
   (Organization)** announces the new certificate.

## Changes (supplementary)

- A.3 gains a closing pointer to the main text's Section 3.7 as the
  continuous-time counterpart of the discrete no-certificate instance.

## Not adopted (deferred to a companion paper, per the audit)

The full continuous-to-finite LP theorem package (value sandwich, exact
atomic duality, moment-error budget), the averaging/held-control LP lemma,
and a solver-backed mesh study. These match the proposals' own venue
assessment (theorem-package scale, SCL-type) and would not fit the
Automatica article's scope.

## QA

- Compile: main and supplementary both exit 0 (tectonic).
- Main: 17 pages (was 16), 4 images, 0 `??`, **0 overfull**, 42 warnings
  (below the v42 baseline of 48); abstract unchanged at 262 words
  (byte-identical to v42).
- Supplementary: 13 pages, 3 images, 0 `??`, 0 overfull.
- All numbers in the new section were verified exactly before inclusion
  (see the audit's verification section).
