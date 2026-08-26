# E1 — Language Completeness (A1 Representation, A2 Relative Completeness)

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 3; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). The proof below is complete as stated; independent line-by-line re-verification remains an open obligation.

**Schema scope:** the judgment inventory referenced throughout is the **TCS-1.0 §4** frozen list of eight canonical judgment families (see `control/01_canonical_system_schema_TCS_1_0.md`). TCS-1.1 is a frozen, unapplied diff and controls nothing here (see `04_open_problems/TCS_1_1_FREEZE.md`, controlling-schema header).

---

## A1 — Representation theorem

### A1.Statement

Fix a TCS-1.0 architecture realization `𝔄_q` with its canonical execution chain

```
physical/history state —O_q→ observation —B_q→ information state —π∈P_q→ prescription —I_q→ realized action —M_q→ trajectory/event law,
```

and let

```
Z = X_phys × H_harm × B_info × U_held × G_gen
```

be the extended typed product of (i) the physical/history state block `X_phys` (states, or histories `C([−τ,0],ℝⁿ)` in the RFDE case), (ii) the cumulative-harm block `H_harm`, (iii) the information-state block `B_info`, (iv) the held/pending-action block `U_held` (implementation queue), and (v) the generation/epoch block `G_gen`.

Then each of the eight TCS-1.0 §4 canonical judgments — (1) controlled viability, (2) robust viability, (3) fixed-policy safety, (4) epistemic viability, (5) institutional viability, (6) chance viability, (7) recoverability, (8) transformability — is **definitionally equivalent** to a typed viability statement on `Z`: i.e., to membership of the initial extended state in the viability kernel (or capture basin, for families (7)–(8)) of an explicitly constructed closed constraint set `𝕂_J ⊆ Z` under an explicitly constructed augmented dynamics `F_J` on `Z`, with the policy class the admissible causal policies read on the extended state.

Moreover, **each block is load-bearing**: for four of the five blocks there is a packet-proved counter-model in which deleting the block (projecting the judgment onto the remaining blocks) changes the truth value of some canonical judgment at some state.

### A1.Phase space and constructions (Field 4)

For each family the augmented system is obtained by the same three moves:

- **Move 1 (adversary promotion).** A `∀w ∀φ` (robust) quantifier is eliminated by promoting the disturbance to a block of the state governed by the declared disturbance dynamics (or leaving it as an input to `F_J`, in which case the viability statement is the *robust* viability statement — kernel under all disturbance realizations). **The two readings define the same set iff the promoted block's admissible trajectories coincide exactly with the declared disturbance class** — a *matching hypothesis* on the promotion (complete: exactly the admissible inputs, no extra ODE constraint that thins the class, no Filippov enlargement that thickens it), not a definitional identity (corrected per `batch 4/PROOF_ELEVATION.md` Finding 20: without the matching hypothesis, adversary promotion can strictly shrink or enlarge the kernel, and the move is a modelling choice). Under the matching hypothesis — which the declared construction satisfies — the eight-family representation below is unaffected.
- **Move 2 (information completion).** An observation-based policy quantifier is eliminated by adding the information block `B_info` with the filter update `b⁺ = B_q(b, O_q(x⁺))`; policies are then state-feedback on `Z`, and the epistemic judgment is ordinary viability on `Z` restricted to policies that factor through `b` alone — a typed constraint on the policy class, not on the dynamics.
- **Move 3 (bookkeeping completion).** Horizon/event/generation structure is carried by `H_harm` (cumulative harm so far, nondecreasing along trajectories), `G_gen` (generation/epoch index with the declared reset maps), `U_held` (the implementation queue realizing `I_q`, e.g. `u(t) = q(t − θ)` for a delay-θ implementation map).

Per family:

| # | Judgment | Constraint set `𝕂_J` on `Z` | Augmented dynamics `F_J` |
|---|---|---|---|
| 1 | Controlled viability | `𝕂_{q,Ω} × H × B × U × G` (identity on nonphysical blocks, unconstrained) | `M_q` on `X_phys`; identity/completion on the other blocks |
| 2 | Robust viability | same as (1) | disturbance-augmented `M_q` (Move 1) |
| 3 | Fixed-policy safety | same as (1) | the closed-loop field with `π` frozen (policy class = {π}) |
| 4 | Epistemic viability | `𝕂_{q,Ω}` read on the `X_phys`-component; policies constrained to factor through `B_info` | `M_q` + filter update (Move 2) |
| 5 | Institutional viability | `𝕂_{q,Ω}` on `X_phys`; realized-action feasibility carried by `U_held` | `M_q∘I_q` via the queue block (Move 3) |
| 6 | Chance viability | path-safety event `E ⊆ Z^{[0,T]}` with declared probability `p`; `𝕂_J` = the p-quantile constraint (see below) | as (2), with the law declared on the disturbance block |
| 7 | Recoverability | envelope `E ⊆ Z` as state constraint, target `C` as terminal set; `𝕂_J = E`, capture form | as (2), with `C` absorbing |
| 8 | Transformability | per-epoch safe sets `𝕂_{q(g)}` read through the typed translation maps; `G_gen` indexes the epoch | switched dynamics with the declared reset/translation maps on `G_gen`-transitions |

### A1.Proof (Field 8)

**Definitional equivalence.** Fix a family `J` and its row in the table above — **under the matching hypothesis of Move 1** (the promoted disturbance block realises exactly the admissible input class of the robust reading; this is the hypothesis under which "by construction" and "by definition" below hold). By construction, an admissible trajectory of `F_J` on `[0,T]` staying in `𝕂_J` is *by definition* a pair (causal policy, disturbance realization) whose underlying physical trajectory satisfies exactly the quantifier chain of `J`: Move 1 makes the `∀w` quantifier part of the kernel computation ("for all disturbance blocks"), Move 2 makes the `π` quantifier range over exactly the observation-based policies (a policy on `Z` factoring through `b` *is* a causal observation-based policy, and conversely every causal observation-based policy lifts to one on `Z` by composition with the filter), and Move 3 makes horizon, implementation, and generation structure part of the state, so the horizon/event bookkeeping in `J`'s quantifier chain is reproduced step-for-step. Since kernel membership is "there exists an admissible policy keeping every trajectory in `𝕂_J`", the truth value of `J` at the initial state equals membership of the initial extended state in the kernel of `(𝕂_J, F_J)`. No inequality, approximation, or hypothesis is used: the two statements have the same quantifier string applied to the same sets. (For family (7) the object is the capture basin `Capt_{F_J}(𝕂_J, C)` — reach-avoid-maintain is the capture form of viability, again by definition of the basin. For family (8) the object is the viability kernel of the switched system on the epoch-indexed product, which is the Operator II object restated on `Z`.)

**Family (6) honesty note.** For chance viability the "kernel" is the *probabilistic* viability kernel `{z₀ : ∃π, P(safety on [0,T]) ≥ p}`. This is a viability statement on `Z` by the same definition (the constraint is the measurable path event); the *deterministic computation* of that kernel is not definitional and is exactly the B9 restricted theorem (chance-kernel recursion under support alignment). A1 claims only the representational equivalence, not computability.

**Block-necessity (Field 9).** Four packet-proved counter-models witness that no block can be deleted from `Z` in general:

- **`B_info` is load-bearing** — R02.Prop3 (repaired witness): the exact-observation filter is viable while the non-separating coarsened filter `q(z,θ) = 1_{z≥4}` is not, at the same physical state. Any projection of the judgment onto `X_phys` alone (deleting the information block) erases the distinction and changes the truth value of the epistemic judgment (4).
- **`H_harm` is load-bearing** — R08.Ex2(e) (hierarchy-completion converse): the nested cumulative-harm bookkeeping cannot be removed without changing a hierarchy-completion judgment's truth; the counter-model separates the judgment with and without the harm block.
- **`U_held` is load-bearing** — R07.Cor6: with the implementation convention stated there, the generation-indexed continuation judgment changes truth value when the held-action structure is projected away (the implementation map's delay/queue structure is what the convention quantifies over).
- **`G_gen` is load-bearing** — R07.Thm4 (alternating-disjoint impossibility): continuous evolution cannot cross between disjoint specifications; the generation/epoch block is exactly what carries the discontinuous translation, and deleting it flips the transformability judgment (8) from true to false in the witnessed instance.

(`X_phys` is trivially load-bearing: every family quantifies over physical trajectories.) ∎

### A1.Scope and limits (Fields 16/17)

- The theorem is *representational*: it does not compute kernels and does not claim the extended system is finite-dimensional in the RFDE case (`X_phys` is the history space; `Z` is then a product of histories with finite-dimensional bookkeeping blocks).
- Dependencies: R02.Prop3, R08.Ex2(e), R07.Cor6, R07.Thm4 (witnesses); TCS-1.0 §3–§4 (chain and judgment inventory). Consumers: E2 (selectors act on correspondences over `Z`), A3 (the variable-event kernel is stated on the history block), C-a (decidability is for the TCS-1.0 language represented here).

---

## A2 — Relative completeness

### A2.Statement

(a) The five inference rules — **R-QM** (quantifier monotonicity), **R-MC** (mapping contracts), **R-EG** (empty-solution guard), **R-SM** (status monotonicity), **R-KR** (kernel recursions) — are sound for the TCS-1.0 judgment language: whenever the premises hold, the conclusion holds.

(b) The five universal conditional laws **U1–U5** (conservation, monotonicity, noncompensation, status discipline, kernel recursion) are derivable in the calculus; the six independence items **M1–M6** are refuted (each by an axiom-consistent witness pair).

(c) **Completeness is relative to the registered claim inventory** — a maintenance clause, not a logical completeness theorem: every *registered* claim is decided by the calculus; nothing is claimed about unregistered sentences.

### A2.Proof

**(a) Soundness.** Each rule is a packet theorem or a definitional guard re-read at the inference-rule level:

- **R-QM** is Operator I's monotonicity calculus (packet `corrected_theorems/01_*.md`, Props 1–8): weakening the disturbance class, enlarging the safe set, or shortening the horizon preserves truth of robust-viability judgments. Soundness is exactly those propositions.
- **R-MC** is R04.Thm1 re-read: from an admitted five-map contract, infer the transferred judgment; soundness is R04's Field-8 proof (symbol-by-symbol quantifier translation under the correspondences).
- **R-EG** is the well-posedness guard: from `Sol(x,u,d) = ∅` infer no viability judgment (of any family) at `x` — soundness is immediate, since every family's quantifier chain presupposes nonempty solution sets; the rule blocks vacuous truth.
- **R-SM** is TCS-1.0 §9 axiom 5 (status monotonicity: integration cannot strengthen proof/evidence status) read as an inference rule on the status component of the official assessment tuple `J_Ω = (P,F,N,R,E; status, scope)`.
- **R-KR** is the kernel-recursion family: the Operator II backward recursion (packet `04_*.md`), the filter recursion (R02.Lem2), and the horizon-limit identity (R03.Lem4, Hausdorff-continuity hypothesis) each license the corresponding recursion inference. Soundness is the corresponding packet/record proof.

**(b) Derivability of U1–U5 and refutation of M1–M6.** Each U-item's derivation is the corresponding record's proof re-read at the axiom level (R09.Thm1 Part U: the conservation telescoping is B6's typed ledger identity; monotonicity is R-QM's Props; noncompensation is TCS-1.0 §9 axiom 4 confirmed by B6's Farkas separation; status discipline is R-SM; kernel recursion is R-KR). Each M-item carries its axiom-consistent witness pair in R09.Thm1 Part M (Fields 8–9 of that record), which *is* the refutation: a rule deriving M_i would contradict the witness pair, so no sound rule derives M_i. The post-audit repairs (M1's global root-locus completion, M3's affine instantiation with scope lock, M5's forward-complete field) are incorporated; they strengthen the witnesses, not the derivations.

**(c) Maintenance clause.** The calculus decides exactly the sentences in the registered inventory (the packet's theorem set plus the batch-2 records plus the session theorems E/A/B/C). It is complete *relative to that inventory*: for every registered sentence, either the sentence, its negation, or its explicit conditional form is decided by the rules above. No claim is made about sentences outside the inventory — in particular, no compactness/decidability theorem for the full second-order language is claimed (that boundary is C-a's business, and C-a.Thm2 decidability is at fixed finite data, a strictly weaker statement than logical completeness). ∎

### A2.Scope and limits

- Logical completeness: **not claimed** (the maintenance clause is the honesty boundary).
- Dependencies: packet B7 (Operator I props), B6 (conservation/Farkas), B3 (Operator II recursion), R02 (filter), R03.Lem4 (horizon limit), R04 (transfer), R09 (U/M inventory). Consumers: C-a (the decidability theorem decides the language this calculus governs).

---

## Status

- **A1: PROVEN** (full proof in this file; witnesses cross-referenced to packet-proved records).
- **A2: PROVEN** (relative completeness with the maintenance clause; soundness proofs are the cited packet/record proofs re-read — each citation is to a file containing its own proof).

**Record-format note:** this is an internal theorem document, not a batch-2 docket record; of the 17 record fields, Fields 1–4, 6–9, 16–17 are carried above (statement, phase space, assumptions, proof, counterexamples, obligations, dependency edges); Fields 5, 10–15 (publication destination, interfaces, novelty register) are N/A for internal elevation theorems and live in the packet's master review.
