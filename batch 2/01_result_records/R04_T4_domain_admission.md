# Result Record R04 — Docket T4: Domain Admission and Projectability Certificate

## Field 1 — Result ID and target docket item

`R04` (R04.Thm1 exact-admission certificate; R04.Cor2 approximate admission; R04.Tab3 classification of the included domain modules). Target: **T4** ("state necessary and sufficient conditions for exact admission; otherwise provide an approximation theorem … theorem/certificate that can classify groundwater, phosphorus, or fisheries models without verbal analogy").

## Field 2 — Verdict

**Proved at the structural level.** The certificate theorem is proved with both directions; the classification table instantiates it on the three included domain families (groundwater A005, phosphorus A004, fisheries A001/A012/A018/A014) using only their source-declared objects, with the open items flagged exactly as the live error register records them. Empirical calibration is explicitly out of scope (packet README, excluded priorities).

## Field 3 — Exact statement

### R04.Thm1 (exact admission certificate)

Let `𝕄` be a domain model with declared objects: state space `X_𝕄`, solution concept `𝔖_𝕄` (with disturbance class `𝒟_𝕄` and admissible control/action correspondence `U_𝕄`), constraint registry generating safe set `K_𝕄 ⊆ X_𝕄`, and judgment family `J_𝕄` (any of the eight `TCS-1.0` §4 judgments). Let `𝔄_q` be a `TCS-1.0` architecture realization. Say **`𝕄` is exactly admitted into `𝔄_q`** if there exist:

1. **type/unit map** `τ`: a bijection between the declared stocks/fluxes/units of `𝕄` and typed blocks of `𝖹_q` (moieties preserved; donor/recipient roles preserved);
2. **phase-space map** `φ: X_𝕄 → 𝖹_q`, injective, with `φ^{-1}` defined on `φ(X_𝕄)` and both maps respecting the declared block structure;
3. **dynamics correspondence**: for every `(x, u, d)`, the solution sets correspond:
   `φ(Sol_{𝔖_𝕄}(x, u, d)) = Sol_{𝔖_q}(φ(x), τ_U(u), τ_D(d)) ∩ φ(X_𝕄)`, and the disturbance/control classes correspond under `τ_U, τ_D`;
4. **safe-set correspondence**: `φ(K_𝕄) = 𝕂_{q,Ω} ∩ φ(X_𝕄)`;
5. **policy/information correspondence**: the causal information structures correspond (every `𝕄`-policy lifts to a `𝖯_q`-policy with identical information, and conversely on `φ(X_𝕄)`).

*Then every canonical judgment transfers exactly: for every `J` in the judgment family and every compatible horizon,*

```
x ∈ J_𝕄(𝕄)  ⟺  φ(x) ∈ J(𝔄_q),
```

*and the kernels correspond: `φ(J-kernel of 𝕄) = (J-kernel of 𝔄_q) ∩ φ(X_𝕄)`.* Conversely, if the phase-space map or the safe-set correspondence or the solution correspondence fails, there exist instantiations of the same signature in which kernel equality fails (Fields 8, 9), so no judgment transfer is possible without the certificate; the failure mode identifies which map is missing.

### R04.Cor2 (approximate admission)

If the dynamics correspond only up to defect `‖f_𝕄 − f_q∘φ‖ ≤ ε` on a compact domain, all other maps exact, then on horizon `T` the trajectories deviate by at most `(ε/L)(e^{LT} − 1)` (Grönwall, `L` the joint Lipschitz constant), and kernel claims transfer only through the erosion conversion of R03.Cor5 (`K_{−r}`, `(L_G c + C)ε ≤ α`) — approximate admission is an `APPROXIMATION` mapping with explicit error, horizon, and safety erosion, never an `EXACT_SPECIALIZATION`.

### R04.Tab3 (classification; summary — full table in Field 8)

| Module | Phase-space map | Model class / mapping type | Blocking items (live error register) | Admission verdict |
|---|---|---|---|---|
| Groundwater (A005) | identity on `(H_f, H_s, M_q, σ_sal, χ)`; storage via constitutive `A_i = 𝒜_i(H_i)` (DAE block) | sampled_hybrid + DAE; `EXACT_SPECIALIZATION` once open fields close | B.5 items: `V-A005-04` (route/remove `q_rel`), `V-A005-05` (leakage limiter), `V-A005-06` (total storage + jump identities), `V-A005-07` (donor/recipient positivity), `V-A005-11` (compatible-state topology) | **conditionally admissible** — certificate fields (1),(3),(5) completable after B.5; reduction to head-space dynamics is *constitutive*, not a `PROJECTABLE_REDUCTION` claim |
| Phosphorus (A004) | identity on soil-P pools | hybrid (ODE + jump balance); `EXACT_SPECIALIZATION` once open fields close | B.4 items: `V-A004-03` (hybrid jump balance), `V-A004-05` (define `χ`, functional dynamics), `V-A004-06` (upper soil-P bound), `V-A004-08` (trade routing/delay/conservation), `V-A004-09` (compatible-state topology) | **conditionally admissible** — same structure as A005; the jump balance is the decisive missing object for map (3) |
| Fisheries — resource–sink (A001 §§6–10) | identity on `(S, K)` blocks | ODE; `EXACT_SPECIALIZATION` — **complete** (no blocking items: the A001 corrections B.1 are proof-wording repairs, not missing objects) | none for admission | **admitted** |
| Fisheries — C3/C4 RFDE (A012/A018) | `(N_t, Z_t, E_t)` resp. `(N_t, A_t, Z_t, E_t)` history spaces | RFDE; `EMBEDDING` into `C([−τ,0], ℝ^n)` with corrected `05`'s phase-state declarations and model-version tags (`NV-012`, `NV-013`) | version discipline only (gated/ungated, working/QSS) | **admitted at exact model-version scope** |
| Fisheries — cod (A014) | scalar phase line | ODE; `EXACT_SPECIALIZATION` of the corrected scalar-autonomous obstruction (error register B.11) | B.11 corrections (nonautonomous `C(t)`, threshold-trichotomy demotion) | **admitted at corrected status** |

## Field 4 — State and phase space

Per module as in Tab3 — the theorem is precisely the discipline that *forces* the phase-space declaration: an admission record is incomplete until `φ`, `X_𝕄`, `𝖹_q` and the solution concepts are named (A005 declares `Z = (H_f, H_s, M_q, σ_sal, χ)` with `A_i = 𝒜_i(H_i)`; A004's pool vector; A001's `(S,K)`; A018's history states per corrected `05`).

## Field 5 — Quantifier order and information pattern

The certificate requires judgment-quantizer *alignment*: the `∃π ∀w ∀φ` chains of `𝕄` and `𝔄_q` must correspond under the lift of map (5); measured/hidden disturbance splits and observation fibres must be carried by `τ_D` and the information correspondence. A domain module whose policy class observes more than the canonical chain permits is not admitted without enlarging the architecture's `𝖮_q/𝖯_q` declarations (the `A005/A004` compatible-state items are exactly this requirement).

## Field 6 — Assumptions, including existence/completeness

Maps (1)–(5) exist (that is the certificate); solution concepts well-posed on both sides (existence/uniqueness or the set-valued declared concept); `K_𝕄` closed; horizons compatible. For Cor2: compact domain, joint Lipschitz `L`, defect `ε` uniform on the domain.

## Field 7 — Mapping type

The certificate *is* the machine that decides mapping types: exact admission → `EXACT_SPECIALIZATION` or `EMBEDDING` (per `φ`'s codomain); defective dynamics → `APPROXIMATION` (Cor2); claimed-but-failed reduction → `REJECTED_MAPPING` (Field 9); verbal-only similarity → `ANALOGY_ONLY` (excluded from transfer by the theorem).

## Field 8 — Self-contained proof

### Proof of R04.Thm1 (sufficiency)

Fix a horizon and a judgment `J` with quantifier pattern `∃π ∀w ∀φ` (robust chain; the other patterns are identical with the obvious quantifier relabeling). 

*Trajectory correspondence.* By map (3), for every `x, π-lift, w`: `φ` maps `𝔖_𝕄`-solutions from `(x, u, w)` onto the `𝔖_q`-solutions from `(φ(x), τ_U(u), τ_D(w))` that remain in `φ(X_𝕄)`. By map (5), the policy classes correspond: every `𝕄`-policy `π_𝕄` lifts to `π_q` with `π_q(φ-history) = τ_U(π_𝕄(history))` and conversely. Consequently the closed-loop solution sets correspond exactly:

```
φ(Sol_{𝔖_𝕄}(x, π_𝕄, w)) = Sol_{𝔖_q}(φ(x), π_q, τ_D(w)).
```

*Safe-set correspondence.* Map (4): a trajectory stays in `K_𝕄` iff its image stays in `𝕂_{q,Ω}` (on `φ(X_𝕄)`).

*Judgment transfer.* The `𝕄`-statement "`∃π_𝕄 ∀w ∀φ_𝕄: φ_𝕄([0,T]) ⊆ K_𝕄`" translates, under the two correspondences above, symbol-by-symbol into the `𝔄_q`-statement with `π_q`, `τ_D(w)`, and `𝕂_{q,Ω}`: same quantifiers, corresponding domains. Hence truth values coincide at `x` ↔ `φ(x)`, and the kernel (the set of states where the statement holds) corresponds. The argument is uniform over the judgment family because it never touches judgment-specific structure beyond the quantifier pattern. ∎

### Proof of R04.Thm1 (necessity direction, by failure-mode witnesses)

- **Solution correspondence fails** (same state space, different dynamics): `X = ℝ`, `K = [0,1]`, model A: `ẋ = u`, `u ∈ [−1,1]`; model B: `ẋ = u + 1`. With `φ = id` and identical constraint/control declarations, the viability kernel of A contains `1/2` (hold `u = 0`), while B's kernel within `K` is empty (persistent drift `+1`: every trajectory exits in finite time; at `x = 1` exit is immediate under all controls). Same types, same units, same safe set — no judgment transfer: map (3) is indispensable.
- **Safe-set correspondence fails:** two models differing only by one additional component constraint (e.g., an upper soil-P bound, `V-A004-06`): kernels differ by exactly that constraint's erosion; transfer without map (4) silently imports the extra constraint (or drops it) — both directions fail.
- **Policy/information correspondence fails:** the common-action obstruction (R02.Prop4 / A001 Example 4.1): a domain policy class that observes a hidden mode has a nonempty kernel where the canonical chain without that observation has an empty one — no transfer without map (5).

Hence each map's absence is *witnessed* by a pair of same-signature instantiations with different kernels: the certificate is necessary in the strong sense that every missing field is independently load-bearing. ∎

### Proof of R04.Cor2

Standard Grönwall comparison on the compact domain: two solutions with vector fields differing by `≤ ε` and common Lipschitz `L` deviate by `‖x_𝕄(t) − φ^{-1}(x_q(t))‖ ≤ (ε/L)(e^{Lt} − 1)` on `[0,T]`. A trajectory certified to keep distance `≥ r` from `∂K` with `(L_G c + C)ε ≤ α` (R03.Cor5 budget with trajectory error in place of the perturbation budget) keeps the true state in `K`. The mapping is therefore `APPROXIMATION` with error `(ε/L)(e^{LT}−1)`, horizon `T`, erosion `r` — and never exact. ∎

### Classification evidence (Tab3 justification)

- **A005 groundwater** (`sources/full/A005_Paper_III_Groundwater_Module.txt`): declares boundary/units (§2), state `Z = (H_f, H_s, M_q, σ_sal, χ)`, constitutive storage `A_i = 𝒜_i(H_i)`, `C_i = d𝒜_i/dH_i > 0` (a DAE block per `TCS-1.0` §2.2), sampled pumping/recharge controls, compatible-state uncertainty, and explicitly frames itself as "an admissible model template … not yet a calibrated case study" — exactly the admission-certificate posture. The open error-register items B.5 (`V-A005-04/05/06/07/11`) each block one certificate field: storage/jump identities block map (4)'s closure; compatible-state topology blocks map (5). Verdict: conditionally admissible; the conditions are enumerable, not verbal.
- **A004 phosphorus** (`sources/full/A004_Paper_IV_Phosphorus_Module.txt`): pool vector and ledger structure declared; the missing hybrid jump balance (`V-A004-03`) blocks map (3) at event branches; undefined `χ`/functional dynamics (`V-A004-05`) block map (2)'s block structure; trade routing and compatible-state topology (`V-A004-08/09`) block maps (3)/(5).
- **A001 §§6–10 fisheries**: closed equations, declared constraint sets, proven kernels (Theorems 6.2–6.5, 10.2) — all five maps are identities or explicit correspondences already present in the source; admitted.
- **A012/A018 C3/C4**: history-state phase spaces and model-version discipline are already fixed by corrected `05` and the notation registry (`NV-012/013`); admitted at tagged version scope (the `DYN-C4-WORKING` vs `DYN-C4-QSS` separation is enforced, never merged).
- **A014 cod**: admitted at the corrected scalar-autonomous status (error register B.11: the sound exact result is the phase-line obstruction; the finite-time threshold trichotomy is demoted).

## Field 9 — Counterexample showing necessity or failure outside scope

The three failure-mode witnesses inside the necessity proof (dynamics mismatch; safe-set mismatch; information mismatch) *are* the counterexamples. Additional scope note: the A018 seam (corrected `05`) is the standing example of a *rejected* dynamic admission (`LEDGER-PRIM-CLOSED-v1 ↛ DYN-C4-WORKING`, `REJECTED_MAPPING` with reasons 1–5 recorded there): the present theorem generalizes that discipline from one seam to all domain admissions.

## Field 10 — Interface producer/consumer contract

- **Producer:** the admission certificate (five maps + verdict + blocking list) as a per-module record.
- **Consumers:** the empirical case selection (E1: the readiness comparison becomes "which module closes its blocking list soonest"); Papers 3–5 (each domain instantiation must cite its admission record, not verbal similarity); the concordance (`01_canonical_concordance_A001_A025.csv` gains an admission-verdict column per domain row).
- **Failure condition:** any cross-module theorem transfer citing a module whose blocking list is nonempty without an `APPROXIMATION` row carrying Cor2's triple — reviewer-enforceable rejection.

## Field 11 — Error, horizon, and safety erosion for approximations

Cor2: error `(ε/L)(e^{LT}−1)`; horizon `T` explicit (exponential growth in `T` — no uniform-in-time claim); safety erosion `r = cε` via R03.Cor5 with the feasible-interval caveat. Exact admission carries no error and no horizon restriction beyond the judgment's own.

## Field 12 — Selector and implementation regularity

The certificate is selector-agnostic (judgment transfer is at the policy-class level); implementation regularity enters only through map (5)'s correspondence of implementation branches — an `𝖨_q` declaration must exist for modules claiming institutional judgments (A004/A005 do not yet declare one — flagged in their blocking lists implicitly through map (5)).

## Field 13 — Stochastic/hybrid/RFDE qualifications

Hybrid modules (A004, A005) require map (3) to include event branches (jump balances — hence the decisive role of `V-A004-03`); RFDE modules (A012/A018) require history-space `φ` (identity on histories; the translated-history closure conditions of corrected `08` apply to any filter claim); stochastic domain laws would require the QF-2 support declaration — none of the three included modules declares one, so no chance-level admission is claimed.

## Field 14 — Novelty status with exact references

Internal: the docket demands exactly this certificate ("type/unit map; phase-space map; projectability; policy/information map; error bound; horizon; safety erosion; artifact/version identity"); no packet record states the necessity direction with per-map witnesses; corrected `05` is the single-instance precedent. External: admission/classification certificates of this form are standard practice in formal modelling (model-class embeddings, morphism-based specification frameworks); **the specific five-map formulation tied to the TCS judgment family is, to internal knowledge, new packaging; external literature check outstanding**; no bibliographic claim made.

## Field 15 — Publication destination

Paper 1 (admission standards section — the certificate as the theory's domain gate); Paper 2 (Thm1's short proof in the mapping-types section); monograph (the classification table as the standing domain appendix).

## Field 16 — Remaining obligations and revocation triggers

Obligations: close the A004/A005 blocking lists (the error-register actions already registered); instantiate the certificate rows in the concordance; select and execute the empirical case (E1). Revocation triggers: any silent change of a module's declared objects (version identity axiom 7); a claimed admission whose map (3) omits event branches or history structure.

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R04",
  "target": "T4",
  "depends_on": [
    "corrected_theorems/09_A002_reduction_diagnostic_audit.md (projectability criterion — governs any PROJECTABLE_REDUCTION claim inside map (2))",
    "corrected_theorems/05_A018_ledger_dynamics_interface.md (single-instance precedent + REJECTED_MAPPING discipline)",
    "R02 (map (5) information correspondence pattern)",
    "R03.Cor5 (erosion conversion for Cor2)"
  ],
  "unblocks": ["empirical case selection E1", "Papers 3–5 domain instantiation discipline", "concordance admission-verdict column"],
  "status": {"R04.Thm1": "proved", "R04.Cor2": "proved", "R04.Tab3": "proved classification at declared status"},
  "mapping_type": "EXACT_SPECIALIZATION / EMBEDDING / APPROXIMATION (the certificate decides per module)",
  "novelty": "packaging internal-new; external check outstanding"
}
```
