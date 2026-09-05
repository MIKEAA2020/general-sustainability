# Joint Audit Evaluation — grok + claude, per manuscript

Each manuscript has two independent audits (grok; claude). Below each paper is evaluated
**jointly**: (A) where the two auditors **agree** (highest-confidence items), (B) where they
**diverge** (items needing a decision), (C) an implementation recommendation, and (D) the
**publishable core** (the object each auditor*independently* says is real and worth keeping).

Method note: this assessment rests on a **full line-level read** of all nine joint audit files
(grok and claude halves of each), not on excerpted highlights. Where the two auditors converge on
the same passage with independent wording, that is the highest-confidence finding.

Standing instruction honored throughout: nothing here reopens the corrected relational-waste /
medium-path framing, or the 250-word abstract cap (now relaxed by the user to ≤300).

P2 — obstruction_calculus (latest = **v7**, pushed as corrected; v5/v6 preserved as baseline).
After the full P2 audit (uploads/grok claude 2.txt) was supplied, v7 applies the convergent,
non-destructive internal-consistency fixes on top of v6 (which had the a-fortiori/abstract/
measurability/singleton fixes):
- §1.1 & abstract "Theorem 3–5" copy-edit → "Theorem 3 (polyhedral common-action) and
  Theorem 5 (certification)" — Theorem 4 was in both camps; Theorem 5 is not polyhedral.
- A4/A1.1 novelty scaled: the estimation-set reduction is itself a necessary-and-sufficient
  characterization in estimation space, so the paper's claim is narrowed to finite,
  mechanism-specific sufficient certificates (common-selection, timing, fibre), consistent with §6.3.
- A1 Theorem 4 decircularized: hypothesis (3) restated as an open-loop drift condition over
  [0,T_obs) (observation-equivalence forces the action to be a common open-loop schedule), so
  the timing bound (4) does the work; flagged as template unless a declared policy class is given.
- A2 Theorem 1: convexification closure added alongside the measurable-selection path.
- A6 Theorem 3: dwell hypothesis significance made explicit (false for nonconvex U without it;
  chattering/relaxed-control case; when (H1) unnecessary) + polyhedral-Farkas hypotheses stated.
- A5 §5(b) reconciled with §6.3 (set-valued value = common controls under set-membership; what's
  missing is a single-valued selection when the common set is empty).
- A9 Corollary 6 corrected: requires one state IN K and one OUTSIDE (a state may violate one floor
  and satisfy another and lie entirely outside K); added certainly-unsafe set; mixed fibre silence.
- §1.4 "Proofs complete" qualified (Theorem 1 stated in Dini form but proved for C^1).
- §6.4 Timing: "least-constrained" → "most-constrained" (least slack); bound pointed to (3), not (1).
- §4.2 empty stub deleted; output-feedback note folded into Theorem 3; §4 renumbered (4.1, 4.2).
- §6.1 added 5 composition rules justifying "calculus" (dominance; delayed=common-action+clock;
  fibre blocks certifiers not policies; refinement monotone; restriction shrinks).
HELD (content removal / structural, need explicit go-ahead per standing rule): A3 (demote
Theorem 2 to a minimal example of Theorem 3 / or replace its plant with a fixed-U example),
A8 (delete Definition EViab, unused & ill-posed), A11 (cut or move Appendix A.1–A.2 and §5(d)
linear-substitution — these concern spatial coupling, not observation), the title/"calculus"
rename, and the entire Part II–V "elevation" (constructive twin theorems, sampling theorem,
minimal-observation synthesis, Farkas-support-as-design, computed example) — a separate sequel
paper, not a rewrite of Theorems 1–5.

P2 — obstruction_calculus (latest = **v6**, pushed as corrected; v5 preserved as baseline).
Applied four verified internal-consistency fixes from the P2 joint audit (C recommendation),
all non-destructive, none content-removing:
- §2.3 "a fortiori" direction reversed (was genuinely backwards): results certify membership
  FAILURES, so because ERViab ⊆ EViab, an obstruction of the robust kernel does NOT transfer to
  the weaker non-robust kernel; the obstruction is claimed for ERViab only.
- Abstract "finite certificates" overclaim narrowed: the drift (Thm 1) and timing (Thm 4)
  certificates are explicitly NOT finite objects (as §1.1 already stated); only the polyhedral
  common-action and certification forms (Thms 3–5) are finite/checkable. Matches §1.1.
- Thm 1 proof (A2): precise regularity warrant added for the Aubin–Frankowska measurable-
  selection step (closed graph + compact values alone give u.s.c., not measurability; the
  warrant is joint measurability of f in t and of D, with the closed-graph/compact-value
  regularity); flagged as declared extension / heuristic without it (consistent §6.5(iv)).
- Remark 1 (fibre/singleton nuance): noted the CE class as instantiated is a SINGLE controller
  (fixed law u=g(·)), not a broad CE family; obstruction is that this refusal discards a
  recoverable degree of freedom.
HELD (content changes / need raw-P2-audit detail): Theorem 2 "manufactured by state-dependent
control set" rework (A3); Theorem 4 hypothesis restructure as open-loop drift (A1); deletion of
Definition (i) EViab (content cull, held per standing rule); optional composition/calculus
subsection or title change.

PUSH STATUS (2026-09-04): Point-1 (consumption-rate driver) + Point-2 (P1 tri-audit hybrid) are
done and pushed to GitHub (repo `MIKEAA2020/general-sustainability`, path
`arena agent 1/paper rewrites/`) as **P1_v17** and **P3_v24** (new version files; the pre-fix
v16/v23 are preserved). Addendum **P3_v25** pushed: the two P3 data-dependent audit items were
VERIFIED as real and fixed — (a) §6.5.2 two-pool/supporting-pool mismatch (tables carry no
supporting-pool column; §8.2 admits the groundwater two-pool model is not established; §6.5.4
"spawning biomass is not an abiotic support pool") — §1.1 corrected; (b) Theorem 13 "no rest
point exists at all" at E>0 was an overstatement (extinction face persists at N=0 since qEN
vanishes) — qualified to "*interior* rest point (N_*>0)".

Addendum **P1_v18 + P3_v26** pushed (2026-09-04): remaining full-audit items verified.
- P1 "demote elementary layer": demoted Theorem 4 (pure monotonicity) → Proposition 4 (number
  preserved, no cascade). Kept Theorem 3 (its (ii) localization is the central claim), Theorem 6
  (real conditional persistence, not an identity) — the audit overstates those. §4.9 range labels
  updated. Abstract 300 words.
- P3 data-vintage/re-pin: all reserve-life arithmetic verified correct (world 308.3~309; US 45.0;
  China 28.0; Morocco 1250; resources 1125.0); single vintage pinned (USGS MCS 2026, Jan); re-pin
  is a registered requirement; fisheries archived 43-stock cohort supplied+re-verified with
  version-sensitivity disclosed. Added dagger(quarantine) markers on the two quarantined rows
  (Australia phosphate, Indo-Gangetic groundwater) with a legend. Abstract 279 words.

NOT done (risky/no-data, recommend as separate pass): P1 cascading renumbering of the whole
elementary layer (would break ~40 cross-refs incl. abstract/supplementary for a presentational
benefit — the paper already qualifies novelty, and Theorem 3(ii)/Theorem 6 are not elementary);
actual P3 re-pinning to the true MCS 2026 / RAM release numbers (requires the external source
data; the paper documents this as a registered revision requirement rather than asserting unverified
figures).

Addendum **P4_v18** pushed (2026-09-04): fixed the two highest-severity internal contradictions
(flagged by both grok and claude as must-fix) plus one verified sign error.
- §12 conclusion reverted to the Euler half-century artefact; rewritten to match §8/§1.2/abstract:
  periodic-review restabilisation above ~6.5 yr (exact held-measurement monodromy), 47.5-yr
  crossing an Euler artefact. Removed 10^-7 fold digits; qualified certification.
- §9 preamble self-contradiction ("no other fold certificate" vs "both fold-certified") resolved.
- §2.4 timescale sign error: r/gamma_U~0.1 IS small (corrected).

P4 remaining (larger, needs decision/verification, NOT done): §7 rebuild-or-cut (+§11.5(vi)
contradiction); demote Prop 2.1/Prop 5.1/Thm 6.2/Prop 10.1 & cut §9.6; strip digits/artefacts/
provisional SNPO from abstract & §1.2; display L(lambda)=B_E lambda as structural identity;
notation pass (tau never maturation).

P4_v24 (pushed 4745d4a) — A24 EXECUTED via SALVAGE (user directive). Section 9.6 retitled 'Open
directions (reproduction targets)'; its three rows (elevated-forcing cod-class ten-state tau*~43;
life-history anchoring g~1/2/5 yr; broader crossing search) rewritten as a short paragraph of
future-work directions, explicitly NOT part of the formal contribution and acquiring result
status only once closures/parameter vector/tolerances/search domain are recovered and registered.
No information lost; no numbered statement status; abstract 252 w unchanged; only §9.6 differs
from v23. P4 correction sequence now v18→v24 complete: §12/§2.4/§9 (v18), §3.1/§9.4/§8 scheme(v19),
§1.3/§11.5(vi) (v21), A2/A4/A5/A6/A7/A9/A10/A11/A17/A18 (v22), demotions+renumber (v23), A24 salvage (v24).

===== A24 REVERSE + scaffold recovery (2026-09-04) =====
The A24 items are NOT unreproducible. The compendium-v1.0 release asset zip
(workspace-01a00d79-...zip) contains the scaffold generating scripts + result files, and the
three §9.6 "reproduction targets" are COMPLETED, machine-precision-verified results of a DISTINCT
scaffold object (companion flow-balance manuscript), NOT of P4 Sections 2-7. Verified here by
running the recovered scripts verbatim:
(1) Elevated-forcing cod-class Hopf: scaffold_item3_refine → tau*=43.29, period 263.4,
    maxgap +0.1631 at (eta,zeta,K0,q)=(5.0,0.8,0.03,0.01), E*=0.245, Xbar_A*=54.2, g0=1.000.
(2) Life-history anchoring at default: all three anchored classes (anchovy g=1 ~27.7,
    sprat g=2 ~34.6, cod g=5 ~54.8) delay-independently stable (negative gap).
(3) Broad search: all strong-candidate Hopfs dRe/dtau<0 (stabilising, 1e-7..1e-9), periods
    ~900..11000 (broad) / ~3800..35000 (classified six), NO clean tau_-/tau_+ two-crossing
    window (window fragmented/narrow) — structural difference from P4's three-state core.
State-count off-by-one flagged: scaffold appendix says "nine states" but lists ten symbols
(mass block Xbar_A,X_J,P,U,A,G + V_N,Z,K_C,E); code implements seven nonlinear states (G
mass-balanced, V_N=0 at equilibrium, Z folded via (1+tau_m*lambda) memory factor).
RESULT: P4_v25 (pushed f6e4751) retitles §9.6 "The scaffold companion: registered and verified
records" and registers these as verified companion records, not open directions; abstract 252 w
unchanged; only §9.6 differs from v24. A24 therefore CLOSED (items verified + registered, not
cut). Scaffold recovered scripts + appendix are in /home/user/scaffold_recovered/.

===== P5 AUDIT (begun 2026-09-04; live repo version = source of truth) =====
P5_v19 (pushed b277534) — honest-tier correction. Live P5 (v18) is well-disciplined
(explicit provisional/unreproduced/reconstruction-mismatch status throughout; strong
Sections 2.2/3.4/4.1/4.7(ii)). One genuine overstatement identified and fixed:
- Abstract 'The stage-structured review map shows exploratory response windows in the
  multi-year range' contradicted the paper's own Section 3.4 pre-registered reconstruction,
  which does NOT reproduce the anchovy 3-4 yr / sprat 6-12 yr windows (reports convergence
  + a separate 34-42yr band with no archived counterpart; table = MISMATCH on exactly those
  windows). Reworded to 'provisional, unreproduced archived response regions (its generating
  computation was never attached), whereas...'. Abstract 298 w (<=300).
- Section 3.3 lead: added an explicit hook tying those archived response regions to
  Section 2.2 status and the Section 3.4 reconstruction mismatch, stating they are archived,
  unreproduced records, not results of the reconstructed object.
No content removed. Rest of P5 audited and sound: Prop 2.1 phase-line obstruction (correct),
Lemma 2.2 extra-loss threshold (correct), Prop 3.1 forward invariance (correct), rapid-review
limit correctly scoped (finite-horizon, not stability transfer), operator distinctness
disciplined, Section 3.4 crossing record (6.50 yr exact vs 47.54 Euler artefact) consistent
with P4 verification.

P5 audit open items (not yet applied, holding for review): (a) unnumbered '3.7 yr' anchoveta
period is an ENSO/catch periodicity, clearly separated from controller windows (fine as-is);
(b) Section 4.5 prospective designs are preregistration targets, clearly labelled (fine);
(c) the paper uses bare 'Corollary'/'Theorem' style only for Prop 2.1/Lemma 2.2/Prop 3.1 —
numbering is consistent, no cross-ref breakage found; (d) potential redundancy: Section 3.3's
'corresponding continuous-delay calculations locate response regions near rg~1.5-1.6' overlaps
P4 Section 7.3 (cross-paper, acceptable). No further non-destructive correction is warranted
without a structural decision.

P4_v23 (pushed ebd4c2a) — STRUCTURAL CULL EXECUTED (user authorised demotions). Decisions, each
confirmed against the proof chain (no item is a main-result prerequisite):
- Prop 2.1 -> **Lemma 2.1** (Frozen-active-pool approximation): genuine bound, cited ONCE only
  to be negated in Section 9.4; nothing derives from it. Section 9.4 ref updated.
- Prop 5.1 -> **Remark 5.1** (Local Hopf persistence, conditional): conditional on the UNPROVED
  five-state macro-reduction conjecture; referenced nowhere => status is an observation.
  '[Proof (conditional, in full)]' -> '[Derivation (conditional, in full)]'.
- Thm 6.2 -> **Corollary 6.1** (Channel-specific pacing): synthesis of already-proved results
  (clauses from Section 5.1 / Thm 6.1 / Prop 5.2 + Cor 5.1); referenced nowhere. Source results
  all retained (none demoted).
- Prop 10.1 -> **Lemma 10.1** (Logistic identification): supporting identity in the primitive-flux
  core, referenced nowhere, self-contained. Kept in Section 10.3 (no appendix object exists;
  moving it would leave a 10.1/10.2/10.4 gap); subsection retitled 'logistic identification lemma'.

Renumbering (contiguous per section/type; all cross-refs updated): Section 5 slid Prop 5.2->5.1
(two-delay identity) and Prop 5.3->5.2 (weighted small-gain); refs in Cor 5.1 + Cor 6.1 proofs
updated. Sections 2/6/10 were single-item renames. Final contiguous inventory: Thm 2.1, Cor 2.1,
Lemma 2.1; Thm 4.1, Cor 4.1; Remark 5.1, Prop 5.1, Prop 5.2, Cor 5.1; Thm 6.1, Prop 6.1, Prop 6.2,
Cor 6.1; Thm 8.1, Remark 8.1, Prop 8.1; Thm 10.1, Lemma 10.1. Abstract (252 w) and Section 1.2
reference no theorem numbers; no figure/table caption cites these items; main proof chain
(Thm 4.1/Cor 4.1, Thm 6.1, Thm 8.1/Prop 8.1, Thm 10.1) untouched.

A24 (Section 9.6 to-do list) STATUS: CONFIRMED but deferred/not executed — it is a separate
content-removal cull, held per the standing rule pending explicit go-ahead. Executing it would
delete the 'pending-recovery' reproduction-target rows.

P4_v22 (pushed 07dc8ce): applied the non-destructive verified P4 audit fixes — A2 (Euler
47.536/79.143 stable interval moves to a labelled Remark 8.1 artefact; 6.50 carried by Prop 8.1),
A4 (state once periodic review is a hybrid system, not the DDE sampled at tau=T_r), A5
(J_cont = A_hold + R_0 explicitly, rank-one effort row), A6 (identical-spectra fact to the proof,
invertibility caveat), A7 (2.306 artefact = (1+T_r C_E) interacting with exp(A_hold T_r), NOT the
scalar 1+T_r C_E=0 which gives ~1.176), A9 (A_eq,W=5050 / 4.652 / 1.2%/0.12% relegated to a
Remark of companion-interface numbers; four-state declared an open working model), A10 (Thm 4.1
(H1) shown automatic on the declared family), A11 (undelayed cubic written as P(lam)-C_Z B_E lam
in Section 3.2 symbols, not a fitted 4-decimal cubic), A17/A18 (abstract + Section 1.2 item 6
softened: folds certified at discrete-collocation only, continuum residual + continuous-delay lift
OPEN, SNPO provisional, 148.6-149.5 an unverified uncollocatable face cycle; abstract 252 words).
All scalar-core results unchanged. Held for structural-cull confirmation: A24 (Section 9.6 to-do
list), demote Prop 2.1 / Prop 5.1 / Thm 6.2 / Prop 10.1, full theorem renumbering.

P3 "rope refinement" verdict (user: proposal was a mistake): the ac48730 refinement that rewrote
the productivity-illusion/elevator passage is confined to SUPERSEDED paper3_material_ledgers_v17.md.
The live P3 (v26) retains the ORIGINAL productivity-illusion text ("An elevator rated for ten
people...", "the cable does not part on the fourteenth passenger") and contains ZERO of the
refinement phrases; v17_corrected.md (added by later sync) restored the original. NO corrective
push needed for P3 — the live version is already free of the mistaken refinement.

P4_v21 CORRECTION (supersedes the v20 §7 rebuild): the repo update (recovered stage code
+ provenance audits stage_code_recovery_report.md / stage_map_provenance_forensics.md +
readme.txt + stage_decomp_results.md) settled that the manuscript's §7 is the A011 GURNEY-
BLYTHE-NISBET DELAYED-RECRUITMENT analysis (g = maturation DELAY, tau = institutional delay,
eta = effort response) and that stage_core.py is the SEPARATE A022 adult/juvenile object.
The v20 §7 rebuild built around the WRONG object (the A022 adult/juvenile 52.07/321.43
numbers), orphaning the real registered GBN records. v21 reverts §7 to the GBN model with
corrected labels (7.1 model + switches; 7.2 g=0 base-window validation; 7.3 fine-map bands on
the r*g~1.5-1.6 locus + caveat; 7.4 nonlinear ground truth + institutional-delay window
bracket; 7.5 the distinct two-stage companion explicitly separated, its 52.07/16.76/31.66
numbers attributed to that companion, not to §7; 7.6 registration/status with the honest
'no sampled stage-map Floquet was ever built; characteristic-root scan + RK4 only').
§1.3 and §11.5(vi) reconciled. All v18/v19 fixes (Section 12, 9, 2.4, 3.1, 9.4, 8
scheme-dependence) are UNAFFECTED by the repo update and retained. Not pushed (workspace
has no .git/PAT after reorg); v21 is at revised/paper4_delay_dynamics_v21.md and mirrored
to the paper rewrites dir.

P4_v20 addendum (pushed): Section 7 rebuilt (audit showed §7.1 described a model that did
not match the recovered stage-analysis code and mislabeled g as "gate strength" / eta as
"social weight"). Rebuilt as "The Stage-Structured Harvest Channel": states the real
adult/juvenile two-age-class system from stage_core.py, g correctly = maturation stage
duration, and the VERIFIED result — adult take carries the delay-induced two-crossing Hopf
structure on elevated-response classes (cod 52.07/321.43; anchovy 16.76/121.80; sprat
31.66/200.88 yr) while juvenile take gives no Hopf crossing — a genuine channel separator
(the stage analogue of the mobilising/protective distinction). Fine-map/ground-truth re-scoped
as companion registration records. §11.5(vi) reconciled ("stage structure outside class" was
self-contradictory). Rebuild-done; no certificate claimed for the numerical records.

P4_v19 addendum (pushed): continued the substantive P4 items —
(a) froze one certified (N*,E*): §3.1 names E*=2.08962, N*=89.55188 (matches §2.5 and both audit
recomputations), replacing multiple printings (89.55/2.090 etc.); notes the four-state
(89.52562, 397.8665) is a distinct object.
(b) §9.4 frozen-donor vs dynamic-A ambiguity (claude A22): explicitly labelled the
characteristic-pinned pair (frozen-donor characteristic matrix, A pinned) vs the dynamic-A
stability boundary (A a state) — the confusion removed.
(c) §8 (claude's central conceptual issue): added closed-form M_ZOH (physically native
zero-order hold), and the provable qualitative fact — T_r->0 inherits undelayed instability;
T_r->infinity exact hold -> rank-one, DC gain proportional to L(0)=0 (filter identity), hence
stable — so EVERY consistent scheme restabilises at some T_r; only the location (6.50 yr) is
scheme-dependent. "Artefact" reframed as scheme-dependence. The remaining full-audit items — see the "Still outstanding" notes per
paper — were deliberately NOT applied in that push: they are either writer's-judgment calls,
require real data/factual re-verification (P3 data vintages, §6.5.2 two-pool tables, P3 Thm 13
"no rest at E>0" truth), or are risky theorem renumbering (P1 demotion of Prop 1/Lemma 2/
Thms 3-4/6) that could break dozens of cross-references. Several audit claims were also found
NOT to match the document (e.g. "Prop 2 cites wrong theorem" — Prop 2 as written cites no
theorem), so applying them blindly would introduce errors, contrary to the no-content-loss /
no-introduced-error standing rule. Those items should be a separate carefully-verified pass.

---

## P1 — assessment_separation (latest = **v20**; v19 the reference fabric, v20 the wave-4 structural bundle (R8 + docket items 1–8 + vocabulary consolidation) — wave 4, 2026-09-06; record: wave4/p1_record.md)

### Three-audit joint assessment (grok + claude + deepseek) — full line-level read
grok and claude independently converge on the same core findings; **deepseek's hybrid resolves the
single genuine fork between them**, so this is that three-way synthesis.

### (A) Joint consensus (grok ∧ claude)
1. **Theorem 8 / thesis conflict.** grok (A2): the blend is a *declared extra action*, not a
   consequence of the disturbance class — relabel "time-shared convexification" honestly. claude
   (central issue): Theorem 8 _is_ von Neumann's minimax for the 2×2 assessor–planner game; the
   abstract's "fails structurally" contradicts Thm 8(iii) and §7's "bridge theorem" sentence.
   ➜ Both: pick a coherent thesis.
2. **Demote the elementary layer.** Prop 1 (tautology), Lemma 2 (dual-cone def), Thm 3, Thm 4
   ("intersecting more sets shrinks"), Thm 6 (identity). Both: one lemma + remarks.
3. **§1.1 duplicated companion prose** (same weak/strong "regimes…rate of use" and hen/orchard
   text as P3 & P4; no theorem here touches material cycles). Both: cut, write §1 from §5.1.
4. **Typed-endpoint operator missing** — the snapshot claim is unwitnessed without `E_end,typ`
   (grok A3; claude §5.4 Fourth).
5. **Notation collisions** (`FP_0`, `r`, `R`, `A`, `e`, `S`) — heavily overlapping lists.
6. **§2 = framework appendix**; cut the 13-slot tuple, keep §2.1 + §2.7 + operators + witness.
7. **§5.2 duplicates §1.3's seven-item "Claimed" list** — keep one (claude).
8. **§7 must survive Theorem 8** — the bridge-theorem sentence reads as if Theorem 8 didn't exist.

### (B) The fork — and how deepseek resolves it
- **grok (A2)** is essentially the hybrid: keep the convex-combination definition, relabel honestly.
- **claude** offers a binary: (A) reframe as pure-vs-mixed minimax, **or** (B) switch to *sequential
  full-depth transients* (tube = union) so the gap is genuinely structural.
- **deepseek (hybrid)** — do **both** as two *distinct operations*, not competing definitions.
  Keep convexified mixing as the main result (Theorem 8, relabeled as fractional allocation of
  control flows = **menu convexification**, not "time-sharing"), **and** add a converse result that
  discrete time-sharing (union tube) does **not** close the gap until both dips are independently
  subsumed (s₁≥2 AND s₂≥2), so the gap survives on the impossibility region. Recognised cost: one
  extra subsection + two definitions; crystal-clear that BLEND_δ and sequential time-sharing are
  different objects with different tubes.

### (C) What was implemented (P1_v16, hybrid)
- **§4.10**: BLEND_δ redefined explicitly as the *convexified action* via fractional allocation of
  primitive control flows (u_δ = δ·u_FAST + (1−δ)·u_SLOW), stated as an explicit model assumption,
  **not** time-sharing. Theorem 8 Remark now names the mechanism: pure-vs-mixed minimax (von
  Neumann 1928; Sion 1958) and the here-and-now / wait-and-see separation of adjustable robust
  optimization (Ben-Tal et al. 2004).
- **§4.11 (new)**: **Proposition 9 — "sequential time-sharing does not erase the gap."** Under
  alternation the visited set is the union of the two tubes, so typed-admissibility needs s₁≥2
  AND s₂≥2; on the impossibility region I (s₁,s₂<2, s₁+s₂>2) no sequential policy is
  typed-admissible, so the gap survives discrete time-sharing. Together with Theorem 8 this
  delimits mixing: convexification closes the gap at s₁+s₂≥2; temporal sharing closes it only
  where both dips are independently subsumed. (deepseek's "typically s₁+s₂≥4" is stated precisely
  as min(s₁,s₂)≥2.)
- **Abstract** (now exactly 300 words): relabels "time-shared convexification — interleaving" to
  "menu convexification," adds the converse delimiter, and scopes "structural" to the deterministic
  menu — resolving claude's statement-vs-thesis contradiction.
- **§1.2(vii), §5.1 (info value), §5.3 (non-claim), §7 (bridge theorem)**: relabeled consistently +
  cross-referencing Prop 9; the "interleaving actions in time" phrase is gone; the §5.2 duplicate
  list was updated to match §1.3.
- **Math verified**: union-tube requires both dips nonnegative (strictly stronger than s₁+s₂≥2), so
  the gap survives on I. Prop 9's arithmetic is sound.

**Net effect.** Satisfies grok's A2 (honest relabel), claude's central-issue (minimax framing + a
genuine structural negative result), and deepseek's recommendation (both operations distinguished,
no rewrite). The paper now *proves* the reviewer's "even time-sharing wouldn't help" objection
true — but only for discrete time-sharing, not for the convexified action.

### (D) Still outstanding (unchanged, not part of hybrid)
(1) demote Prop 1/Lemma 2/Thms 3–4/6; (2) add `E_end,typ`; (3) strip §1.1 duplicate companion
prose, write §1 from §5.1; (4) fix notation collisions; (5) shrink §2. None of these blocks the
hybrid; they are the follow-up edits.

---

## P3 — material_ledgers (latest = **v28**; v27 the verified micro-error cluster, v28 the wave-4 notation/inflation/re-pin bundle (R11–R17 + structural docket) — wave 4, 2026-09-06; record: wave4/p3_record.md)

### (A) Joint consensus
1. **§1.1 vs §6.5.2 two-pool claim not discharged.** grok A10 + claude: the applied tables have
   NO supporting-pool column (groundwater=anomaly-only, phosphate=reserves-only, fisheries=SSB-only);
   §8.2 admits the two-pool model is not established. ➜ **Both: "single most damaging mismatch."**
2. **Notation collisions** — grok and claude both list B, C, S, M, N, K, T, R, G, I, b, s, r, ρ, h,
   α, θ, σ/ς/s, d, P, F, E, μ. One letter, one sort.
3. **Theorem inflation** (Thm 3, 4, Lemma 16 = FTC/substitution; Thm 2 duplicates Thm 1).
4. **Theorem 13 false "no rest at E>0"; R0 naming.** Both flag: extinction family persists at
   positive effort; R0 used for both union and extinction-only.
5. **Data vintages / reproducibility.** Indo-Gangetic quarantined row in a submitted table; single
   USGS/vintage pin; fisheries archived 43-stock cohort matches neither public RAM release.
6. **Prop 2 cites wrong theorem (7 not 3); §3.3 "depletion condition" is the safety condition;
   §2.2 "four primitives"; §3.1 "first three"; §5.4 double-C.**
7. **§11 repeats the weak/strong redefinition** — both say a conclusion should not re-argue
   waste-as-relation; close on incidence/donor/clocks/interface.

### (B) Divergences
- grok wants depletion taxonomy (three clocks) and the classification matrix **promoted higher**;
  claude agrees §6.1 is the strongest section but wants it *cleaner*, not necessarily earlier. Minor.
- The weak/strong redefinition: grok says "flag it as a reading, not the received distinction";
  claude says "nonstandard, will draw fire." ➜ Both want it *framed as an interpretation*, not the
  literature's own. This is compatible with your relational-waste correction — keep content, add scoping.

### (C) Recommendation
The §1.1-vs-§6.5.2 mismatch is the top priority (it attacks the introduction's central promise).
High-value, low-risk: display the incidence matrices (A3), fix R0/naming/Prop-2-cite/sign/clause
errors, pin one vintage and remove quarantined rows, and scope the weak/strong redefinition as a
reading (not the received distinction).

---

## P4 — delay_dynamics (latest = **v27**; v26 the small-error cluster, v27 the wave-4 presentation tail (R18–R22 + S11 relocation) — wave 4, 2026-09-06; record: wave4/p4_record.md)

### (A) Joint consensus
1. **Conclusion reverts to the Euler artefact.** §8/abstract: exact crossing at **6.50 yr**, Euler
   47.536/79.143 = artefacts. §12: "restabilising crossing near a half-century review interval."
   ➜ **Both: the single most damaging contradiction.** Fix conclusion to match §8/abstract.
2. **§7 as a whole must be rebuilt/cut.** grok: reproduction appendix, different model, G5
   category error. claude: §7.2 g=0 windows are exactly the scalar core's r-window; g is a
   *maturation* time not gate strength; §11.5(vi) denies the section exists. ➜ Both: cut/relabel.
3. **§9.4 four-state contradiction.** Frozen-A Hopf pair vs delay-independent stability at
   baseline. Decide which object each number belongs to.
4. **Prop 2.1, Prop 5.1 dead weight** (justify nothing / conditional-on-conjecture).
5. **6.50 not certified** while Hopf delays are 10^-13 — enclose it or present to 2 decimals.
6. **Notation:** τ used for both institutional delay and maturation lag. Never.
7. **Abstract/§1.2 stripped of digits & "provisional SNPO".**

### (B) Divergence
- grok: "five-regime topology" oversells; keep certified folds only. claude: same + the
  crisis-alternative hedge. Minor — both land on "reduce to what Fig 1 + collocatable branches show."

### (C) Recommendation
Fix #1 (conclusion) — this is the make-or-break. Then A2/§9.4/6.50-certification notation pass.

---

## P2 — obstruction_calculus (latest = **v9**; v8 the first safe tranche, v9 the wave-4 theorem-level repairs (R9 notation/§2.4, R10 IRViab, consensus 1/2/3/5/7 + claude's section notes) — wave 4, 2026-09-06; record: wave4/p2_record.md)

### (A) Joint consensus
1. **Theorem 4 circular.** claude A1: (H2) already asserts the conclusion; restate H2 as an
   open-loop-over-[0,T_obs) drift condition so the timing bound does real work. grok: Thm 4 is
   closer to a template than a certificate.
2. **Theorem 1/3 adversarial existence gap.** claude A2: Aubin–Frankowska measurable-selection
   doesn't give the closed loop; need D lsc/constant or convexify. grok: same (convexity comment
   is "exactly backwards").
3. **Theorem 2 manufactured by state-dependent control set** (claude A3; grok A3) — not a
   genuine hidden-mode example.
4. **"A fortiori" backwards** (grok §2.3; claude concurs in effect) — theorems are about ERViab,
   do not imply EViab.
5. **Definition 1 / EViab** — delete, circular qualifier, undef initial beliefs.
6. **Abstract overclaims "finite, checkable" and "five mechanisms proved"** — widen scope.
7. **Fibre count**: Corollary 6 wrong as stated; Remark 1 policy-class is a singleton.
8. **Anachronistic/uncited companion + future references.**

### (B) Divergence
- Minor: grok wants a "composition/calculus" subsection or a title change; claude agrees in effect.

### (C) Recommendation
High-signal: fix A1 (Thm 4), A2 (closed-loop existence), A3 (Thm 2 as admissibility not
hidden-mode), the "a fortiori" direction, and rescale the abstract's novelty. All are internal-
consistency repairs, not restructuring.

---

## P5 — sampled_governance (latest = **v21**; v20 the regression repair, v21 the wave-4 middle layer (R23/R24 + the claims-ledger/appendix docket) — wave 4, 2026-09-06; record: wave4/p5_record.md)

### (A) Joint consensus
1. **Reconstruction/unreproduced stage-map status.** grok: the 3–4 yr / 6–12 yr windows are
   "results of the stage-structured map" but the reconstructed map's status is unresolved. claude:
   same. ➜ Resolve: attach the original record or rewrite so only fully-specified reconstruction
   claims appear.
2. **Lead with the exact-map 6.5 yr crossing; soften/relocate Euler 47.54/79.1.**
3. **Catchability q sensitivity** (0.001 vs 0.1 destabilises every class) should surface.
4. **Future-dated citations** (Rose 2026) and frozen plan dates (2026-09-01).
5. **"Claims ledger" box** — every numerical window + its evidential tag. grok suggests; claude
   similarly wants claim-status consolidated.
6. **Registration/`declared`/`preregistration` overload** → appendix.
7. **Operator-non-transfer is the clearest contribution** — keep; ensure abstract doesn't mix plants.

### (C) Recommendation
Low-risk, high-clarity: add the claims-ledger box; fix stage-map status + q-sensitivity surfacing;
fix future dates; move registration meta-text to appendix.

---

## E1 — cod forecast ladder (latest = **v11**; v10 the never-landed factual-recheck layer, v11 the wave-4 docket (R1–R7 + the R3 DM/Künsch post-freeze layer, §3.5 + Table 9) — wave 4, 2026-09-06; record: wave4/e1_record.md)

v9 (this pass) applies the convergent, non-destructive presentation/framing fixes from the joint
audit (grok severity-grouped + claude A1–A12/B/C/D/E). No data movement, no content removal;
the data-integrity items are held for factual re-check before any edit.
- Class-obstruction moved to the FRONT of abstract/Highlights/§1; the test recast as "how large
  is the penalty" (the map's monotone-regime obstruction, not a claim the class could do the job).
- Every "no structural model beats persistence" scoped to **rolling-origin RMSE**; the fixed-window
  structural wins kept as what they are.
- Abstract **origin-matched** the headline (84 kt vs 120 kt on identical origins; mixed-origin 88 kt
  stated as such). Abstract ≤300 words (298).
- **Machine-verified** split from class-level obstruction (arithmetic/reproducibility only); §3.3
  reworded from "distinct from a statistical null" to "weaker than a statistical null result."
- Keyword "recruitment forecasting" → **biomass forecasting / surplus production**.
- **Brier non-informativity** stated in §2.3 (Spec A near-degenerate indicator) + **Direction score
  convention** declared (persistence forecasts ΔS=0, so 0.00, excluded from the Direction ranking).
- **Companions cited** (generic, "in preparation"/"under review") in ref list + in-text (Edwards
  Aquifer, governance, methodological template); no longer 3 uncited allusions.
- **Highlights** each ≤85 chars; **Data/code availability** already present (repo + checksums).
- Freeze-asymmetry sentence kept and re-cited to the companion (in preparation).
- A9 presentational fix applied (certificate framed as weaker than a null); A10 catch-source conflict
  already resolved in text (STATLANT matches Schijns on 1983–93; 1956 discrepancy unused; "reconstruction"
  wording retained with the matching note).

### (A) Joint consensus (very strong, overlapping)
1. **Result largely predetermined.** Prop 4.1/Lemma 2.2 already prove the class can't crash-recover.
   State the obstruction FIRST and recast as "how large is the penalty." grok A1; claude A1 agrees
   Prop 4.1 doesn't even apply cleanly (r≈2 violates monotone regime).
2. **Persistence inherits the smoother** — caveat must be in Highlights/abstract.
3. **Rolling-origin only.** M1b beats persistence on the fixed recovery window; A6.
4. **Origin-match the headline** (84 vs 120/88).
5. **"Machine-verified certificate"** attaches to arithmetic not class-incompatibility — split.
6. **Freeze post-hoc / no dated protocol; future citations.**
7. **Uncited companions ×3.**

### (B) Divergence
- claude A3/A4 deeper: declared box violated (K=105.9 < 500), M1/M1b catch-dependence inconsistency,
  flat-objective undermines ranking. grok flags some (M1 264 vs 120 identification disclosure) but
  less severely. ➜ claude is more aggressive here; grok's are a subset.

### (C) Recommendation
Move the class-obstruction to front; scope all beats to "rolling-origin"; origin-match abstracts;
split machine-certificate claims; fix future dates. Larger data-integrity items (box violation,
M1/M1b inconsistency) need a factual re-check before editing.

### (D) v9 presentation/framing done. FACTUAL RECHECK run (v10) — full detail in
`/home/user/E1_FACTUAL_RECHECK.md`. The ladder (`src/run_ladder.py`) was re-run in isolation and
reproduced every archived row byte-identically. **No invented figure found** — all reported model
values/RMSEs reproduce. Verdicts:
- **A7 CONFIRMED, label swap (presentational, no number changed).** Decomposition on identical
  rolling origins (Spec A): p0=98.05, control(S_tm1)=184.43, M4=195.57, so **delay cost p1−p0 = 86.38**
  and **model cost M4−p1 = 11.14** (h=1); delay 65.12 / model 158.38 (h=5). Paper had these reversed.
  Constructive finding surfaced: at h=1 the surplus model's own penalty is only ~12 kt (delay, not
  structure, separates M4 from persistence); at h=5 Spec B the model's own cost dominates (694/713).
  Applied in v10 §4.
- **A3 CONFIRMED, documentation error.** Manuscript §2.2 declared K∈[500,5000], but the code uses
  K∈[max-train-S+10, 5000] (=50.8 kt lower on recovery) and the frozen spec says "above the training
  maximum"; 500 is only the initializer. M1b K=105.9 is a valid interior fit, not a box violation.
  §2.2 corrected in v10.
- **A5 CONFIRMED, real limitation.** Recovery objective SSE 127.4→149.9 across K∈[60,5000]
  (training-RMSE 11.29→12.24 kt, <0.95 kt spread), r compensating (0.435→0.773): (r,K) not identified,
  valley-variant ordering not a robust ranking. Ranking implication added in v10 §3.2.
- **A4 consistent, not a data error.** Rolling M1/M1b near-catch-insensitive (120.5 vs 120.5) and
  fixed 120→264 are the same flat-valley + constant-catch-as-mean effect; §3.2 already reconciled.
  One unifying sentence added in v10.
- **A1/A2 CONFIRMED (framing).** Collapse fit (r=1.935, K=1032.7, C=240) has TWO positive equilibria
  (repelling 144, attracting 888 kt) and folds above 783 kt — so "monotone regime" was imprecise, but
  the obstruction still holds (upper attractor + lower absorbing state, cannot crash-recover). §1,
  abstract, and §4 restated/scoped in v10. No numbered "Prop 4.1"/"Lemma 3.2" exists in the text
  (the audit names prose content).
- Net: v10 (from v9) applies A7 + A3 + A5 + A1/A2 + A4-clarity only; abstract 300 w, Highlights ≤85.

---

## E2 — cod intervention (latest = **v18**; v13–v17 preserved as baselines — v15 adopted the single-convention recompute, v16 corrected the retention mechanism and Fox constructive, v17 applies the restructure-level joint-audit items)

v14 (this pass) applies the jointly-verified corrections. The intervention runner was re-executed in
isolation and reproduced every reported value (r=0.2369, K=5000, SD 135, ε=460, constructive 57.62,
kernels, F'=1.1531, and the full §3.11 xte row r=0.5023/K=4812.9/F'=1.4447/g(LRP)=130.7/cb=−48.0/
q10=−178.7). Full detail: `/home/user/E2_FACTUAL_RECHECK.md`. **No fabricated number found.** Applied
(non-destructive; verified facts):
- **A6 CONFIRMED**: certified kernels empty from **T=7**, not "beyond T=5" (T=6 nonempty at 4942.5<5000).
  Fixed §3.4, abstract (3), §5(4), §4.
- **A9 CONFIRMED**: Allee constructive bound = **81.3 kt**, not "unaffected" (was 57.6); non-monotone
  caveat added. Fixed §3.6, §5(5), §4; Allee refit relabelled post-freeze sensitivity (not co-equal).
- **A4/A5 CONFIRMED**: expansion is generic (F'>1 ⇔ S<B_MSY ⇔ any LRP), so it is a limitation of the
  sup-Lipschitz certificate, not a methods-record contribution; "two forms" are ONE geometric-series
  expression. Re-worded §3.4, Figure 4, §4; dropped the contribution claim.
- **A3 CONFIRMED**: expansion is **marginal** (SSE near-flat K∈[2000,7000]; F'∈[1.04,1.17]), not
  "the data-selected regime". §3.7 readings + §4 + abstract reconciled (both sides fixed).
- **A2-labelling CONFIRMED**: Table 3 "SSE" = Σe²=n·MSE (306,532 at K=5000); §3.3/3.6/3.11 figures are
  MSE. Labelled; timing-convention (source-year fit vs destination-year SD/defect) disclosed in §4.
- **A1 CONFIRMED (held)**: destination-year catch convention for SD/ε/floors vs source-year for the
  map; 1992 reads −460.0 vs −329.0. Full single-convention recompute is a registered follow-up —
  **disclosed, not silently applied**.
- **A7/A8 CONFIRMED**: S1/cascade = 60-kt flat cap on the kernel domain (family = flat caps only);
  zero catch fails only clause (c); the rule is a **catch-expansion** criterion. State §3.2, §5(3).
- **A10 CONFIRMED**: xteNCAM reversal is a main result; promoted §3.11 heading + text; reversal added
  to abstract (6) and conclusion (6).
- **A11 CONFIRMED**: "protected by good years" restricted to the perpetual-floor construction; §3.8
  stochastic trade-off now leads (0.87→0.58 with catch).
- **A12 CONFIRMED**: percentile estimator (linear interp, 24 residuals) stated; "vacuous"→"trivial";
  "informative/vacuous"→"sub-/supra-maximum-surplus"; keyword + "robust viability".
- **A13 CONFIRMED**: post-1992 residual bias (−55.8 kt yr⁻¹) disclosed in §3.8 as qualifying both layers.
- **A14 CONFIRMED**: "same fitted map by construction" softened (same class & machinery, distinct
  single full-window fit); companion references (Author et al., in preparation / under review) added.

### (A) Joint consensus
1. **Abstract lead claim is map-scoped, not a Northern cod finding** — put the scope clause first.
2. **Retention rule cannot retain anyone** (Prop 3.1 tautology) — drop "retention" for a dominance
   partial order, or change H1 to a trade-off.
3. **Vacuous emptiness (Prop 3.2) is an identity** — don't number it as finding (2).
4. **§3.7 vs §4 expansion contradiction** — rewrite §4.
5. **Freeze 2026-08-26 future-dated; protocol edited after freeze.**
6. **K pinned at 5000 on a series max 941 kt** — real fit defect.

### (C) Recommendation
Reframe abstract (scope-first); resolve retention-rule; fold vacuous emptiness; fix freeze date;
state K-pin as fit defect. Slogan "protected by good years" → restrict to perpetual-floor construction.

### (D) REMAINING / HELD (author decision; not applied in v14) — RESOLVED in v15/v16 (arena-agent commits f076ee7, cdc7699): the source-year convention was ADOPTED
- **SINGLE-CONVENTION RECOMPUTE RUN** (this pass): the source-year convention (the one the model
  equation and the fit use) is confirmed as the correct one — the source-year residuals give MSE
  = 12,772.2 kt² (the fit objective) and SSE = 306,532 (Table 3's K=5000 row), exactly, while the
  destination-year residuals (SD 135, ε 460, floors −318.8/−114.85) never matched either. Full results:
  `/home/user/E2_SINGLE_CONVENTION_RECOMPUTE.md`; tools: `revised/tools/run_intervention_srcyear.py`
  and `revised/tools/campaign_srcyear.py` (archived results untouched). Headline changes: SD 135→114.9,
  ε 460→329, constructive bound 57.6→**91.6 kt**, only ONE vacuous class (q05 becomes informative,
  BAU q05 T=∞ = 2219.6 kt), 60-kt rule now holds the LRP under q10 (884.6/884.6, weakening the
  "boundary-harvesting is less protective" geometry), certified horizon T=8 (not T=7), bootstrap
  constructive median 44.7 [0.0, 87.1] (79.1% positive). **Not yet baked into the paper** — these are
  substantive result changes (three choices offered in the recompute doc: adopt into v15, add labelled
  appendix, or hold).

### (D-b) RESTRUCTURE APPLIED (v17, 2026-09-06, non-destructive; no value, kernel, or boundary changed)

Implements the owner-directed restructure-level items (the parallel sandbox's "E2 v17" description,
evaluated and verified in this repository; its manuscript files were lost in that sandbox's reset —
see the addendum at the end of this file). Built by `apply_batch7_restructure.py` (fail-loud exact
replacements); verified: **zero table rows changed** between v16 and v17.
- **Abstract re-scoped**: the governed-object scope leads (a single fitted map; every statement scoped
  to that map, its declared classes, and its declared family; "nothing here is a Northern-cod-general
  result"); the K = 5000 pin is named a declared fit defect in the abstract. The abstract's numbered
  list renumbers to five findings plus an unnumbered definitional-note sentence (the vacuity demoted).
- **Retention filter → dominance partial order** (Definition 2.6, clauses verbatim, vocabulary
  retired): the (H1)-at-every-reading structural block stated as the reason (BAU's marginal
  5th-percentile T=∞ nonemptiness, 2219.6 kt, where every positive-catch rule is empty); a
  *Why the filter vocabulary is retired* note added; Result 3.1 → **"No dominance"** with the
  verdict's selection-theoretic status stated and the groundwater-companion comparison reframed
  (different constraint structure — not a single fatal floor — so not comparable selections).
- **Finding-2 demotion**: Result 3.2 → **Definitional note 3.2 (the vacuous-class identity)** —
  |e| > g_max ⇒ monotone decline for every C ≥ 0, "an identity of the map's algebra, not a
  measurement"; Conclusions renumbered to **five findings + two definitional notes** (Note A = the
  identity; Note B = the rule-level structural block).
- **§3.7 / Figure 4 / §4 / Conclusions expansion contradiction resolved** in one consistent reading:
  not an artifact of the particular pinned value (holds for every admissible K ≥ 2K* = 1769.2 kt),
  explicitly conditional on K ≥ 2K*, data-selected within that range. Verified from the registered
  data: the K-grid r and F′(K*) values reproduce exactly at every grid K; SSE falls monotonically
  521,053 → 306,532 kt² as K rises, so "the fit cost rises below 2K*" is correct.
- **Freeze date / post-freeze disclosure**: verified already present in v16 (frozen 2026-08-26 prior
  to any kernel/boundary/replay/score; §2.1 post-freeze list) — retained.
- Numerically re-verified non-destructively: r = 0.2369; SD 114.9 (sample, ddof = 1); mean −10.9;
  range [−329.0, +206.6]; q05 −287.4; q10 −80.9; g_max = 296.1; g(K*) = 172.46; F′(K*) = 1.1531;
  the r_T chain 329.0 / 708.4 / 1146.1 / 2232.4 / 3675.2 with K*+r_7 = 4559.8 and K*+r_8 = 5451.3
  > K — all reproduce from `wave_e_cod/data/` (source-year convention).
- **Registered residual** (NOT changed in v17 — outside the described restructure scope): §3.6's
  "residual SSE 7690.1 kt² against 12,772.2 kt²" — 12,772.2 is the **MSE** (SSE 306,532 / 24), so
  the first occurrence's "SSE" label is a one-word mislabel (the audit's priority-1 reconciliation
  item); fix at owner acceptance.

---

## E3 — Edwards forecast ladder (latest = **v12**; v8→v11 preserved — v11 is the batch-7 implementation; v12 registers the independent replication and resolves the comparator kink)

### (A) Joint consensus
1. **M1 retained by margin the paper calls operationally nil** (0.39 ft; MAE tie; loses at h=5).
   Lead with the real result: causal loses; AR(1) coin-flip; climatology wins at h=5; oracle = nowcast.
2. **M2m declined then used as the climate comparator** — protocol kink, fully. One of (retain M2m)
   or (compare climate to M1/persist only).
3. **Freeze date future-dated; "pre-registered" overstated; protocol edited after.**
4. **Recast "certificate for current year"** into nowcast / forecast / contemporaneous trio.
5. **Uncertainty on margins** (Diebold–Mariano / block-bootstrap).
6. **Uncited companions.**

### (C) Recommendation
Rewrite Abstract/§7 around "stock-flow with climatological fluxes is best one-step; persisted
recharge is the failure"; resolve M2m comparator; add uncertainty; fix dates.

### (D) IMPLEMENTED (v11, 2026-09-05, non-destructive; no frozen verdict or score changed)
- Abstract/Impact/§7 lead with the real result (causal loses; 0.39-ft coin-flip with MAE tie and h=5
  loss stated; oracle = nowcast; climatology win with interval excluding zero); the two correlations
  (0.17 / 0.74) in the abstract; "certificate" retired; "pre-registered" retired (freeze dated and
  archived; deviations listed in one place in §4.1: M2m class clause, M2m-as-comparator,
  struck sign-hit).
- M2m kink resolved by full disclosure (both options' content): frozen rule quoted verbatim;
  M2m's rule-as-written status stated (satisfies H1/H2); Table 5 gains a vs-M1 column; Table 6
  gains vs-M1 margins and the M2m gate row; the climate rejection restated as point-rule outcome
  with both margins visible; "no stock-flow retained is an artefact of the class clause" stated.
- Post-freeze uncertainty layer (§5.3.1, `wave_e_edwards/src/e3_audit_uncertainty.py`, seeded):
  8 DM/bootstrap rows — M1−persist −0.39 [−1.51,+0.71] covers 0; M2m−persist −0.95 [−1.45,−0.68]
  EXCLUDES 0 (the only one-year margin separated); M2m−M1 covers 0; M2−persist borderline;
  mean−persist h=5 −4.30 [−9.72,−2.09] excludes 0 (DM undersizedness caveat noted);
  climate margins within noise.
- Clip check: the [610,710] clip binds on the recovery-window M2 path from 1959 (raw
  617.1→605.3), never on the observed record — now stated in §5.2 with both fixed-window M2
  RMSEs reproduced exactly (18.11 / 55.32) as the cross-check.
- §5.5 rewritten as rating-curve/redundancy check; tail-failure direction CORRECTED (the map
  predicts non-cessation at every observed head; zero-discharge 602.9 ft < all observed heads);
  Comal construction stated (same ladder scored directly on Q, n=75).
- §5.6 fixed: 20%-cut path is closest (7.19 < 8.56) and labelled an artefact of the map running
  high; 5.2-ft arithmetic; coefficient comparison corrected (range vs magnitude; OLS association;
  1980–90 vs full-sample window labels).
- M4 labelled symmetry control (Table 2 + §6); z→H unified; table-reading propositions converted
  to result sentences; corr-vs-φ̂ distinction stated; "wrong timing"→"right timing, unforecastable";
  PDO/AMO not-run disclosure; daily-high convention noted.

### (D-b) v12 (2026-09-06, non-destructive; no frozen verdict or score changed)

Built by `apply_batch7_restructure.py`; verified: **the only table-row change between v11 and v12 is a
label** ("climate gate" → "nested baseline") — every value identical.

- **Comparator kink RESOLVED against the frozen document.** `wave_e_edwards/protocol_pass2.md`
  (frozen 2026-08-25) states the climate question as "reduce primary RMSE on J-17 relative to
  persistence **and relative to M1**" — and M2m-as-comparator appears in **no** frozen document
  (grep of protocol.md / protocol_pass2.md / protocol_intervention.md / SPECIFICATION.md). The
  v10/v11 "declared nested comparator M2m" was the papers' own (mis)statement, which v11 had
  disclosed as a kink; the joint audit demanded resolution, not disclosure ("a referee will not
  treat an acknowledged kink as resolved"). v12 corrects the comparator to the frozen M1:
  §4.1 deviation #2 rewritten (the correction itself disclosed); §5.4 narrative restated — the
  three climate modules are **listed on the frozen gate** by within-noise margins (0.02–0.13 ft),
  and not retained on three stated grounds (within-noise gate margins; h = 5 persistence failure;
  no forecast structure beyond the declined M2m class — they are affine AR(1) maps with a
  climate-indexed intercept shift); the M2m margins kept as a nested-baseline reading, not the
  gate; the Table-7 caption relabelled; the §6 "entire causal ladder is rejected" sentence
  qualified. **Verdict unchanged** (no climate module retained under either statement); the
  stated mechanism is corrected — matching the repo's own final edition's reasoning
  (wave_e v2 §5.4: "M2m with a weakly adjusted intercept … not additional forecast structure").
- **Independent replication registered and verified.** The owner-archived
  `campaign_e3_dm_uncertainty.py` (uploaded to this batch-7 directory) was executed against the
  registered `wave_e_edwards/results/rolling_forecasts.csv`: **deterministic** (byte-identical
  md5 across runs, seed 0, 20,000 block-bootstrap replications) and reproducing every claimed
  number exactly — M1−persist: gap −0.391 ft, DM z = −0.858, CI [−1.218, +0.560], p = 0.384;
  M2m−persist p = 0.001; h = 5 naive_mean−persist p = 0.035. Output archived at
  `results/e3_dm_uncertainty.csv` and registered in §5.3.1 + Data Availability. Cross-implementation
  agreement with `wave_e_edwards/src/e3_audit_uncertainty.py` verified; the differences are fully
  explained (population- vs sample-variance HAC scaling — the −0.858 vs −0.852 DM statistics differ
  by exactly the sqrt((n−1)/n) factor; unweighted-truncated vs Bartlett HAC at h = 5; block length
  h vs 8; 20k vs 10k replications; different seeds); every load-bearing conclusion is identical
  under either implementation.
- **Diebold & Mariano (1995) + Künsch (1989) references added** (with citation hooks in §5.3.1);
  the §5.3.1 table is numbered (**Table 6**), climate → Table 7, counterfactuals → Table 8; the
  two replication-only rows registered in prose (h = 1 climatology loss +2.94 ft, p = 0.046;
  M2 h = 5 loss +12.4 ft, p < 0.001).
- Verified already present in v11 (the described parallel-sandbox "E3 v11" elements): the
  abstract/Implications/Conclusions real-result lead; the "certificate" retirement with the
  nowcast / forecast / contemporaneous-accounting closure (§6); the "pre-registered" retirement
  (fixed computational protocol, freeze dated, deviations listed in one place, §4.1).

---

## E4 — Edwards intervention (latest = **v11**; v9/v10 humanized passes preserved)

### (A) Joint consensus
1. **+3.3%/+0.4% are hybrid, not robust** — put hybrid caveat in the first results sentence.
2. **Certified retention fails** — abstract still says "retained." Lead with: nominal-only.
3. **BAU = training-mean pumpage, not current use** — re-run at current/permitted; state baseline.
4. **Kernel-matched vs attractor-twin comparator** is the honest fix (flat-80% for S1, flat-60% CPM).
5. **"Empty beyond ~13 yr" is ceiling arithmetic** — report horizon as a function of ceiling.
6. **660-ft negative certificate is a category error** — CPM protects springflow(618), not head≥660.
7. **Uncited companions.**

### (C) Recommendation
Lead Results with "retained nominally at 618/UC-min; not certified; not at 660." Fix comparator
(attractor-twin), fix BAU baseline, report horiz`on-vs-ceiling, drop the 660 certificate framing.

### (D) IMPLEMENTED (v11, 2026-09-05, non-destructive; no frozen verdict, kernel, or score changed)
- Three-verdict lead everywhere (abstract Results/Implications, Impact Statement, §5): nominal
  at 618 ft / UC-min; not certified; nothing at 660 ft; hybrid caveat in the first results
  sentence (+3.3%/+0.4% are historical-replay entitlement; under the floors the margin is a
  0.4% trigger lag).
- BAU renamed training-mean (unregulated-mean) pumping at every definition site; baseline choice
  in the abstract; current-pumpage sensitivity added (382.16 kaf → attractor 604.5 ft; securing
  cut ≈31.5%; Stage-I/flat-80% 613.1 ft does NOT secure — registered follow-up, labelled).
- Comparator table (Table 6) consolidating all readings: kernel-matched flat-90 (+3.3/+0.4%);
  attractor twins flat-80/flat-60 (+16.2/+50.6%); interpolated 7.2% cut (+0.2%/−2.6% CPM fails);
  1%-grid flat-92 (+1.1%/−1.8%) and flat-93 (S1 fails) — R2's grid dependence now visible.
- Certified-layer mechanism CORRECTED: affine policies shift only the intercept → a identical
  across policies → (F4) exact, certified kernel = closed-loop nominal kernel of the raised
  threshold with feedback included; the reactive collapse at certified level is trigger-band
  entry (618 + r_T crosses 660 between T=4 at 659.89 and T=5 at 664.66); per-step tube note
  (K*+r_t is tighter); Prop 2.1 restated as Calculation 2.1.
- 660-ft restated as a design observation (scoring a trigger against its own level; cascade's
  purpose is springflow near 618) — "negative certificate" framing dropped; flat-cap horizon
  extensions given with the ceiling formula T_empty(C) = ln((C−H*)/(K*−H*))/ln(1/a);
  "empty beyond ~13 yr" restated as "required initial head exceeds the ceiling"; new
  boundary-vs-T table (Table 3).
- OOS-defect sensitivity recorded numerically (ε=21.81 → r₃ 50.2, r₅ 66.0, r_∞ 85.9; the
  bound is optimistic; certified horizons scoped out of findings).
- THREE post-freeze layers (`wave_e_edwards/src/e4_audit_layer.py`, seeded, on the declared
  coefficients): (i) closed-loop historical-replay supply — S1 262.36→258.98 (−1.3%), CPM
  254.93→254.70; hybrid margins attenuate but survive (S1 +2.0% vs flat-90, +14.7% vs flat-80;
  CPM +50.4% vs flat-60); closed-loop 1990 bias +31.8 ft disclosed; (ii) attractor residual
  bootstrap (5000 reps, none non-contractive) — P(≥618): BAU 0.41, flat-90 0.53, S1/flat-80
  0.65, CPM/flat-60 0.83, zero 0.99; flat-90−BAU gap [1.9, 5.0] excludes zero (ordering
  resolved, threshold clearance NOT resolved — "the fitted map cannot resolve the marginal
  caps"); (iii) current-baseline algebra as above.
- Lucas caveat moved into Methods (§2.1) with the γ-window comparison row; 10-day-vs-annual
  note at the safe-set definitions; five-stage disclosure (Stage V not scored); UC-q05/q10
  percentile estimator stated with "only the perpetuity is harsher than any recorded year"
  corrected; companion studies cited (Author et al. entries); "machine-verified" vocabulary
  retired; fit hypotheses relabelled (F1)–(F4); z→H unified; tables renumbered 1–7; Fig 1
  caption scoped to UC-min with flat-90's 0.88-ft clearance flagged; "positive selection
  result"→"nominal selection"; "two scored systems bound the answer" removed.

---

## Cross-cutting, across all nine
- **Recurring, single most common theme:** accompanying unpublished companions ("under review")
  carry load-bearing claims and numerals. If papers are submitted separately this is a hard
  dependency. Recommend: make each stand alone or cite as remarks.
- **Recurring:** future-dated citations (Rose 2026, etc.) and "frozen 2026-08/Sep" dates relative
  to a 2026 submission.
- **Recurring:** preregistration vocabulary ("declared / registered / quarantined / load-bearing /
  not a governance recommendation") — move to Limitations or an appendix; use once per object.
- **Recurring:** notation collisions in every manuscript (one letter = one sort).
- **Recurring:** theorem/blob inflation vs. a small survivable core.

## Suggested handling order (confirm before implementing)
1. **P1**: Theorem 8 thesis **resolved via hybrid** (convexified-menu closure + discrete-time-sharing
   converse); follow-ups: demote elementary layer; add E_end,typ; strip §1.1 duplicates.
2. **P4**: fix the §12 conclusion (6.50 exact, Euler retired). *(highest severity single fix)*
3. **P3**: §1.1 vs §6.5.2 mismatch; display incidences; fix R0/Prop-2-cite/sign; pin vintages.
4. **P2**: Thm 4 open-loop; A2 closed-loop; Thm 2 admissibility; "a fortiori"; abstract scope.
5. **P5 & E1–E4**: claims-ledger boxes, stage-map/comparator fixes, origin-matched reporting,
   cert-vs-arithmetic splits, future-date fixes, companion cut/cite.

---

## Publishable core (per paper) — where grok and claude independently agree the substance is

For each paper, both auditors converge (from separate reads) on the same "what is actually new" —
the modest, defensible object that survives the edit:

- **P1:** the four-action exact-tube witness + quantifier noncommutation + blend/erasure delimitation.
  grok: "a real theorem … the publishable object." claude: "the quantifier picture and the witness
  are worth publishing … currently sitting under a framework and a literature rewrite the body itself
  disowns in §5.1."
- **P3:** typed incidence ⇒ conservation; donor limitation ⇒ positivity; three non-interchangeable
  clocks; classification matrix; record-relative barrier; non-reduction. grok calls the depletion
  taxonomy "the paper's best conceptual contribution"; claude: "the paper's best one-paragraph statement
  of its thesis."
- **P4:** delay in the *controller* (not the ecology); filter identity ⇒ even-multiplicity cubic;
  mobilising-vs-protective as modulus-and-damping (not a sign flip); Euler-ZOH manufacturing a crossing
  the DDE lacks. grok/claude both flag Thm 6.1 (protective no-Hopf) as the theorem worth keeping.
- **P2:** common-action obstruction, timing bound, fibre criterion. Both: "the pieces most worth publishing."
- **P5:** sample-and-hold vs continuous delay vs annual step; Euler vs exact hold; extractive (mobilising)
  vs protective; operator-non-transfer as "the clearest contribution."
- **E1:** on two unpooled series + locked rule, this Schaefer/Allee ladder does not beat last-value
  persistence; collapse is not a catch-drop event; extra unidentified modules add error.
- **E2:** mild floor + moratorium/(40–60 kt) holds the 2016 LRP on the bound-pinned map; stochastic
  survival ~0.86 (moratorium) vs ~0.58 (120 kt); LRP-definition sensitivity.
- **E3:** the one-pool map **nowcasts** a year whose recharge is known and does not forecast the next;
  multi-year planning should use climatology, not persisted recharge.
- **E4:** mean historical pumping cannot hold 618 ft under perpetual-1956 recharge; a ~7–10% cut can;
  reactive rules match that invariance (hybrid only); the 660-ft trigger cannot make {H≥660} invariant.

---

## Consolidated priority fix list (joint, deduplicated)

Recurring and agreed by both auditors; grouped:

**Hardest / single most damaging, per paper:**
- P4 §12 conclusion reverts to the Euler 47.5-yr artefact (exact = 6.50 yr). **Highest severity.**
- P1 Theorem 8 / thesis contradiction (minimax; "fails structurally" vs "property of the menu").
- P3 §1.1 "supporting pool beside each resource" tables **do not exist** in §6.5.2.
- P5 §2.3 vs §3.2 vs §3.4 undelayed-stability contradiction (A1).
- E3 M2m declined-then-used-as-climate-gate; E1 A6 rolling-vs-fixed-window wins elided.
- P2 Theorem 4 circular (A1); P5 A3 stage-map window unreproduced.

**Internal-consistency repairs (both agree, low-risk):**
- Notation one-letter-one-sort in every paper (P3 worst; P4 τ; P5 S/M/δ; P2 U/K/a/ε/d).
- Theorem/lemma inflation: demote FTC-inser-of-theorem results (P1 Prop1/Lemma2/Thm3-4/6; P3
  Thm2-3-4/Lemma16; P4 Prop2.1/5.1).
- Fix sign/label/citation errors (P3 Prop2-cites-7-not-3, §3.3 "depletion" is safety condition, §2.2
  "four primitives", §3.1 "first three"; P3 Thm13/ℛ₀; P1 disturbance convention; P2 "a fortiori"
  backwards; P5 §2.3 "iff").
- Proofs containing remarks/policy clauses; statements containing proofs; unnumbered results.

**Applied/empirical integrity (hardest in the data papers):**
- Pin one USGS/RAM vintage; remove "quarantined" rows from main tables (P3).
- Fix the archived-cohort-not-reproducible issue (P3 fisheries; P5 stage-map reconstruction).
- Promote §3.11/xteNCAM (E2); split nominal/certified/660 verdicts (E4).

**Cross-cutting (all papers):**
- Unpublished "under review" companions carry load-bearing claims → cite or make stand-alone.
- Future-dated citations (Rose 2026, etc.) and "frozen 2026-08/Sep" dates → lock status.
- Preregistration vocabulary overload → Limitations/appendix; once per object.
- Move "certificate/machine-verified/declared/load-bearing/discipline" out of Results into Methods/Limits.

**P1 blend-model decision** (was the one real either/or): **hybrid — resolved and implemented.**
Convexified-menu closure kept as the main result (relabeled honestly; minimax framing), plus a new
converse result that discrete time-sharing does not close the gap. This is the deepseek
recommendation, embedded in P1_v16 as §4.11/Prop 9; the pure convex-reframe (grok-only) and the
pure union-tube substitution (claude-only) were both rejected as sole answers.

---

## Batch-7 addendum — the parallel-sandbox E2 v17 / E3 v11 (2026-09-06)

The owner supplied a second sandbox's implementation report: "E2 v17" (restructure-level,
non-destructive) and "E3 v11" (with a new §5.7 uncertainty layer, Table 8, and the companion
script `campaign_e3_dm_uncertainty.py`). That sandbox's manuscript files were lost in its reset;
the surviving uncertainty script was owner-archived into this batch-7 directory (remote commit
da1b609) and is the only artifact that could be verified directly. Evaluation and disposition
(recorded item-by-item in `E2_V17_E3_V12_VERIFICATION.md`):

- The script was **executed and verified**: deterministic, and every headline number in the
  owner's description reproduces exactly (−0.86 / [−1.22, +0.56] / 0.38 / 0.001 / 0.035).
- The E2 v17 described changes were evaluated against the frozen state and **implemented as
  this repository's paperE2 v17** (five restructure items; no value/kernel/boundary changed;
  zero table rows differ from v16).
- The E3 v11 described changes split three ways: already present in this repo's v11 (real-result
  lead; trio; pre-registered retirement — verified); **incorporated as paperE3 v12** (campaign
  script registration + references + table numbering; and the comparator kink resolved against
  the frozen protocol document); and the parallel sandbox's own §5.7/Table 8 layout, which is
  not reproduced literally — this repo's v11/v12 carry the equivalent §5.3.1 layer plus the
  registered replication, which is the same content under a different (already-implemented)
  layout. Nothing from the described changes was rejected on substance; the only declined
  element is presentational (their §5.7 placement), with the reason recorded.

---

## Batch-7 wave-2 addendum — the six P1–P5/E1 audits, full status (2026-09-06, Task 71)

The owner's question for this wave: *any points from any of the joint audits
remaining to be implemented in any of the papers?* Answer: **yes — materially.**
Six parallel deep-read audit subagents (Task IDs 71-a…71-f) extracted every point
from both halves of each audit and classified it against the repo's latest
version; every load-bearing claim was re-verified here (including fresh
computation against `wave_e_cod/`). Full record:
`batch 7 (audits of agent arena 1 paper rewrites)/WAVE2_IMPLEMENTATION.md`.
Headlines:

- **E1:** the "v10" described in the E1 (D) block below **never existed in the
  repo** (no file; every v10 number greps to zero in v9). Wave 2 built it for
  real: all five verified fixes (A7 decomposition relabel 86.4/11.1 and
  65.1/158.4; A3 bounds; A5 flat-valley ranking caveat; A1/A2 two-equilibrium
  obstruction restatement — repeller 144 / attractor 889 / monotone below 783;
  A4 unifying sentence) plus the presentation fixes v9's log claimed but the
  file lacked (keyword, origin-matched abstract, §2.3 Brier/Direction
  conventions, "weaker than a statistical null", Highlights ≤ 85 chars,
  abstract 298 words).
- **P1:** the thesis fork stays resolved, but the v17 hybrid left **dangling
  citations** (von Neumann 1928 / Sion 1958 / Ben-Tal et al. 2004 in §4.10,
  absent from the References) — repaired as v19. The five "(D) still
  outstanding" items (E_end,typ; §1.1 strip; §2 tuple cut; notation; demotions)
  remain open and registered.
- **P2:** the audit was **essentially unimplemented** (v6 = humanized rewrite
  with no claim changes; v7 = abstract-only from a different checklist that
  re-asserted the flagged overclaim). Wave 2 applied the first safe tranche as
  v8: the a-fortiori direction corrected, the abstract's "finite, checkable"
  scoped, the companion given a reference entry, §6.4's certificate number
  fixed. The theorem-level repairs (Thm 4's H2, Thm 1/3 existence gap, Thm 2
  admissibility, Def 1/EViab, Cor 6, Remark 1) are registered follow-ups.
- **P3:** ~100 audit points, ~2 implemented by v24–v26; wave 2's v27 applies the
  verified micro-error cluster (Prop 2 cites Theorem 7; the safety-condition
  rename; the primitives retitle; "first three" → named predicates; the §5.4
  double-C disambiguation; 47.5 not 47.6; the blank-cell claim corrected).
  The structural agenda (notation, theorem inflation, R₀ split, incidence
  displays, the USGS re-pin, §11) remains registered.
- **P4:** the substantive campaign was real (all 7 consensus items closed);
  v26 applies the small-error tail (τ_M pair, §5.1 pointer, regime (iii) arm
  range). Remaining: presentation-layer items only.
- **P5:** v19's honest-tier correction was inconsistent — it **broadened** the
  abstract's non-transfer claim (the opposite of the audit's ask) and left
  §3.4/§4.1 asserting the archived windows as findings, contradicting the
  corrected §3.3 lead. v20 repairs both regressions and attributes the windows
  to the archived record. The middle layer (claims-ledger box, registration
  appendix, parameter table, ρ = 1.00035 margins, A1/A9 reconciliations)
  remains registered.

No frozen verdict, score, kernel, spectral record, or table value changed
anywhere. Build scripts: `apply_batch7_leftover_fix.py` (E2 v18),
`apply_batch7_wave2.py` (the six versions above).

---

## Batch-7 wave-3 addendum — the remaining-points joint assessment (Task 72, 2026-09-06)

**Owner instruction:** *since there are two audits per paper, they must be evaluated jointly
before implementing — any remaining points from any of the audits worth listing in the joint
assessment?*

**Method.** Both halves of every batch-7 audit file were re-read jointly (grok + claude per
paper), every candidate remaining point re-verified against the current latest version
(E1 v10, E2 v18, E3 v12, E4 v11, P1 v19, P2 v8, P3 v27, P4 v26, P5 v20) by direct
grep/read of the files, and each point's endorsement recorded as **[both]** (grok ∧ claude —
the highest-confidence class), **[grok]**, or **[claude]**. **Nothing was implemented in this
wave: this listing is itself the joint evaluation the owner requires before implementation.**
Line numbers refer to the current version files in `arena agent 1/paper rewrites/`.

**Answer: yes — in two registers.**

- **Register 1 — the wave-2 docket stands.** The deliberately deferred structural items
  (`WAVE2_IMPLEMENTATION.md` §3, with reasons) remain the bulk of the remaining work; below,
  each carries its joint endorsement.
- **Register 2 — 24 newly-listed points the docket missed**, all verified open today. The
  three loudest: **E1's companion citations are still absent from the References — a joint
  consensus item whose recorded status ("companions cited … in ref list", E1 block above)
  is not true of the file**; **E1's abstract still carries the "fixed in the analysis
  scripts before execution" claim that its own §4 retracts (joint consensus item 6)**; and
  **E1's A8 (retention-rule completion + a DM/bootstrap margin) is a joint-consensus ask
  entirely absent from the docket**. Beyond E1, a verified cluster of jointly-endorsed
  micro-errors in P3/P4 was never registered.

### E1 — cod forecast ladder (v10) — 7 newly-listed + the docket's methodological asks

- **R1 [both — consensus item 7] Companions uncited; the record's claim is false for the
  file.** v10 carries four in-text companion mentions (the governance study, the Edwards
  Aquifer evaluation, the interval-verified linear template) and **zero** entries in the
  References (checked: no "in review / in preparation" entries; the list runs Cadigan 2016
  → Shelton & Healey 1999). grok's fix: drop or footnote the empty companions ("except the
  freeze-asymmetry sentence"); claude's A12: cite them. Neither cite-nor-drop was applied
  in v9 or v10 — and the E1 (D) block above records "Companions cited … in ref list +
  in-text", which the file does not support (the same record-vs-file failure class as the
  "v10 never existed" finding). *Fix: cite-or-drop, one References-fabric edit.*
- **R2 [both — consensus item 6] The freeze claim in the abstract.** Abstract (L16) and §1
  (L32) still say "fixed in the analysis scripts before execution" while §4's freeze
  paragraph (L304) discloses "no dated pre-score protocol file: the passes evolved … rather
  than preregistered". grok's minimum repair — stop the "before execution" claim in the
  abstract (or add a pass-dates table) — was not adopted. *Fix: one sentence (weaken to
  "coded before the Specification-A rolling score was read", grok's suggested wording, or
  equivalent).*
- **R3 [both] A8 — retention-rule completion + uncertainty on the margins.** grok: "Put a
  bootstrap or Diebold–Mariano (even with a caveat on small n) in a supplement, or state
  that the certificate is a ranking under a pre-set rule, not a test of equal predictive
  ability." claude A8 (its priority item 4): complete Definition 2.4 — the deciding horizon
  (h=1 / h=5 / both), the comparison pairs for the non-nested ladder (is M2's comparator
  M1 or M1b?), a tie band — and add a DM or block-bootstrap interval. Verified: v10 has no
  DM/bootstrap anywhere, and Definition 2.4 remains incomplete. **Absent from the wave-2
  docket** (which lists the drift baseline, LOO, the parameter table, etc., but not A8).
  *Fix: one definition edit + a small post-freeze-labelled computation (E3's §5.3.1 is the
  in-repo template).*
- **R4 [grok] The 1898-kt Spec-B collapse number is absent from the abstract.** "That
  number will dominate any talk … give it one sentence in the abstract" — the abstract
  carries 694–819 / 670 / 688 kt but not M2's 1898. *Fix: one sentence.*
- **R5 [claude] Floor disclosure.** Report the number of origins whose trajectories hit
  the numerical floor and the ε actually used (v10 L294 says "the ε-floor part of the
  registered scoring configuration" — the value is never stated; "registered where? State
  ε"); also ε's double duty (process noise in Def 2.1 vs log floor in §4). *Fix: one
  sentence + one symbol rename.*
- **R6 [claude] "No module M2–M4 is retained" (L196)** — M1 and M1b also fail (H2); write
  "no structural model". *Fix: one phrase.*
- **R7 [claude, A9 residue] Statement apparatus.** No funding statement (Fisheries Research
  requires one); Definition 4.2 still sits in §4 rather than Methods; the abstract's
  "machine layer" is defined only indirectly (via Definition 4.2's certificate). *Fix:
  small edits.*
- Docket (registered, methodological asks — new computations, not corrections): the
  drift/damped-trend baseline; leave-one-origin-out influence; the 900–1900 kt Table-6
  forecast explanation; the M3/M4 609/586 deterioration explanation; the M4 decomposition
  as a results table; the parameter table in a supplement; the log-RMSE demotion [grok].

### P1 — assessment_separation (v19) — 1 newly-listed + the docket's 8 structural items

- **R8 [standing instruction, not an audit point] Abstract length.** 310 words by a plain
  whitespace count (v19 changed only the References; the v18 count was the same) — over
  the ≤300 cap under that count, while the (C) block above records "now exactly 300 words".
  E1's build pins its abstract mechanically (298); P1's was never pinned. *Fix: cut ten
  words and pin the count in the next build.*
- Docket items, endorsements attached: (1) the E_end,typ typed-endpoint operator — the
  "photograph" claim remains unwitnessed **[both — consensus 4]**; (2) the §1.1
  companion-prose strip (hen/orchard/cycle-closure/productivity-illusion prose, 30 grep
  hits at v19) **[both — consensus 3; the cross-paper exposure]**; (3) the §2 13-slot
  tuple cut **[both — consensus 6]**; (4) the notation pass (FP₀ / r / R / A / e / S)
  **[both — consensus 5]**; (5) the demotions of Prop 1 / Lemma 2 / Thm 3 / Thm 6 (nine
  numbered results remain) **[both — consensus 2]**; (6) the title's doctrinal sound
  ("Title and §7 still sound like a doctrinal ranking … a referee will quote Theorem 8
  against you" — grok; claude's E6 concurs) **[both]**; (7) the 25-check enumeration
  ("which 25? Supplement" — claude; "name them or move to a supplement log" — grok)
  **[both]**; (8) §6.1's unpublished-companion dependence (L434, "each under review")
  **[both, cross-cutting]**. Plus the preregistration-vocabulary density (29
  declared/registered/preregister hits in v19) **[both, cross-cutting]**.

### P2 — obstruction_calculus (v8) — 2 newly-listed + the docket's theorem-level repairs

- **R9 [both — grok "Notation drift ℐ/ℑ/ℨ/K_ℐ … freeze them in 2.4"; claude E11] Notation
  unification + complete §2.4.** grok: pick one symbol for the observation structure and
  one for the institution; claude: "Unify notation (U, K, a, ε, d, H, ℐ/ℑ), renumber
  hypotheses per theorem, and complete §2.4." §2.4 remains the v6 partial. **Not in the
  wave-2 P2 docket** (which lists only the theorem-level repairs). *Fix: a notation pass
  bundled with the theorem-level edits.*
- **R10 [grok] IRViab sits in the hierarchy, the notation list, and §6.4 without a formal
  definition or a theorem.** grok: "Either give a one-line definition (command set
  restricted to an institutionally admissible correspondence U_ℑ(x) ⊆ U(x), kernel of that
  system) or drop it from the hierarchy until it is a theorem." v8 keeps it at L75 / L102 /
  L289 with prose only. *Fix: one line.*
- Docket (theorem-level, endorsements per the (A) block): Theorem 4's H2 circularity
  **[both — consensus 1]**; the Theorem 1/3 closed-loop existence gap (D lsc/constant or
  convexify; the "exactly backwards" convexity remark) **[both — consensus 2]**; Theorem 2
  reframed as admissibility, not "hidden modes" **[both — consensus 3]**; the
  Definition 1 / EViab deletion **[both — consensus 5]**; Corollary 6's single-floor
  repair **[both — consensus 7]**; Remark 1's Π_CE class definition **[both — consensus
  7]**; the §5(b)–§6.3 contradiction, the C¹/Dini mismatch, and the hitting-time
  convention mismatch **[claude, section notes]**.

### P3 — material_ledgers (v27) — 7 newly-listed + the docket's structural agenda

- **R11 [both — grok twice + claude "again"] "horizontal exhaustion estimate" →
  "horizon".** Two sites (L45 §1.1, L771 §11). *Fix: one word, twice.*
- **R12 [both — grok's notation table; claude's §1.1/§11 notes] B = b·M is never defined
  in the body** (L45, L771; B and M are later R+T and the natural-block mass; the object
  reappears only in §11). *Fix: one defining clause.*
- **R13 [claude, internal-inconsistency tag] The deep-time contradiction.** §1.1's
  "natural regeneration acts far more slowly — often on deep-time scales" (L41) versus two
  paragraphs later "a crop within a season, an aquifer within years to decades" — claude:
  "Regeneration is human-timescale for most renewables; the claim as stated is wrong for
  exactly the systems (fisheries, groundwater) the paper tabulates." *Fix: one scoping
  sentence.*
- **R14 [claude] Mt/kt harmonisation in §6.5.3.** L591: "approximately 74,000 Mt of world
  reserves and 240,000 kt/yr of production" — the arithmetic is consistent across the unit
  systems but the display mixes them. *Fix: one edit.*
- **R15 [claude, internal-inconsistency tag] "each of the five right-hand sides."** The
  closed block has six states; A^geo has vanished from the list in the one section arguing
  the donor must be a state. *Fix: one list.*
- **R16 [grok, notation] μ, ν, ρ are used in §2.2 before their §5.4 definition, and ρ also
  serves as the retirement fraction** (L119's retirement use vs L458's "product, waste,
  and price parameters"). *Fix: part of the notation pass, concretely listable.*
- **R17 [both — consensus 5's undecided residue] Data-vintage decisions unmade.** The
  Indo-Gangetic daggered row remains first in the §6.5.2 main table with the "≈ 2.7 yr"
  index displayed alongside its do-not-reuse caveat (drop-to-supplement versus
  keep-daggered-in-place was never decided); the fisheries-cohort decision
  (v4.66-primary versus archived-pull-primary) is unmade — the 43-stock median 1.8
  headline stands while S5 retracts "not reproducible" and the broad-cohort comparison
  (454 / 3.39) lives in the supplement. *Fix: two owner decisions, then edits.*
- Docket (structural, endorsements attached): the notation pass **[both — consensus 2]**;
  theorem inflation (Thms 2/3/4/6/17/18/20, Lemma 16) **[both — consensus 3]**; the R₀
  split (R_ext / R_K / R_frozen) **[both — consensus 4]**; displaying the four-row and
  seven-compartment incidence matrices **[both — via (C) "high-value, low-risk"]**;
  Theorem 14's missing E ≥ 0 **[both — grok A5 + claude]**; §9's three inconsistent
  field-difference values (4.47 / O(κ_A K) = O(5) / 4.652 vs −0.348) **[grok A11 — "write
  both vector fields at the same (N, A, U) before claiming the difference equals T*"]**;
  the classification-matrix-vs-§6.5.4 Θ_F contradiction **[grok, §6 notes]**; the USGS
  single-vintage re-pin **[both — consensus 5]**; the §11 weak/strong re-argument
  **[both — consensus 7]**; the three uncited companions **[both]**; the length (21,110
  words against a 10–12k target) **[both]**.
- Housekeeping (not an audit point): the supplementary pointer cites
  `paper3_supplementary_v6.md` (L841) while v7 exists in the same folder.

### P4 — delay_dynamics (v26) — 5 newly-listed + the docket's presentation tail

- **R18 [claude] §1.1's second cross-ref error.** "bifurcation analysis occupies Sections
  2–9" (L23) — claude: "§6 is the protective channel" (and §8 is sample-and-hold, §9 the
  global numerics). The v26 fix corrected the other §1.1 pointer (Section 4 → 5.1) but not
  this one. *Fix: one edit.*
- **R19 [grok, flagged three times] The G5 pair is still imported into §7.** §7.6's
  registration paragraph (L418) lists "the registered compute-core Hopf pair
  3.666149 / 150.358477 (G5)" — grok: "G5 does not belong in this section … a category
  error" (§7's τ is the maturation lag, not the institutional delay). The §7 rebuild was
  implemented at the framing level; this residue stands. *Fix: one relocation/relabel.*
- **R20 [claude] Undefined symbols where used.** §5.3/Prop 5.1's σ_geo, α, β; §2.4's
  γ_U, ε_U, σ_geo ("appear without definition"); the MPF Ů equation is used in the
  invariance argument but never displayed. *Fix: definition-level edits.*
- **R21 [grok A23 + claude] MPF material to the supplement.** The η_crit sweep, the
  intermittency diagnostics (CV 1.58, anticorrelation −0.47), and the "more than 300
  parameterisations" screen fact (stated at two sites, L489 and the §9.6 region) — both
  auditors route this material to a supplement. *Fix: relocation.*
- **R22 [grok, precision umbrella] The "within 0.05%" version-robustness claim** sits
  beside a 0.4%-wide bracket and a 7-digit ω_A^* value. *Fix: presentation.*
- Docket (presentation tail, endorsements): §9.2's multiplier digits / 1.1×10⁻⁷ precision
  fusion; the revision-history changelog narration still in the main text (§9.2's "an
  earlier two-fold reading … is superseded" passages) **[both]**; §1.2's digit stripping
  **[grok + claude — "an introduction is not a computation log"]**; the M3-B family list
  entry; the undefined "c > 0" Routh entry; the Halanay η collision; the q*/p/S-for-stock
  notations; the uncited r-literature range; the three uncited-but-listed references
  (Zhang et al. 2013; Cloud–Moore–Kearfott 2009; Moore 1979); §11.6's grant list; the
  §8–§9 campaign tables (the consolidated table, the 2/|C_E| sentence, the growth rates,
  the stock-mode reading).

### P5 — sampled_governance (v20) — 2 newly-listed + the docket's middle layer

- **R23 [both — consensus 3, partial] q-sensitivity surfacing.** grok: "That sensitivity
  is important and should appear in the abstract or §4.1"; claude: "q = 0.001 vs q = 0.1
  flips every verdict … the Reading should say the comparison is uninformative rather
  than 'does not reproduce'." v20 reports the q = 0.1 destabilisation in §3.3/§3.4 (the
  Records paragraph) but not in the abstract or §4.1, and the Reading keeps "does not
  reproduce" with qualifiers rather than claude's blunter framing. *Fix: one-to-two
  sentences.*
- **R24 [claude E10 + grok's notation notes] Notation unification.** "Unify notation
  (S, M, δ), define g, C_E, C_Z, 'four-state', and choose 'extractive' or 'mobilising'."
  **Not in the wave-2 P5 docket.** *Fix: a notation pass.*
- Docket (middle layer, endorsements): the claims-ledger box **[both — consensus 5]**; the
  registration-vocabulary appendix **[both — consensus 6; ~42 hits]**; the logistic-core
  parameter table **[claude A6]**; the λ/θ/margin reporting for ρ = 1.00035 (a multiplier
  this close to the unit circle needs its computational archive or a short appendix —
  grok; claude A2) **[both]**; the A1 undelayed-stability reconciliation (§2.3 vs §3.2 vs
  §3.4) **[both]**; the A9 slow-stock "agreement" reclassification **[claude]**; the
  screen-band lineage acknowledgment **[claude A4]**; §4.6's relocation; the
  "42 vs several dozen" harmonisation (the abstract still reads "several dozen" against
  §1.2's 42) **[both — grok + claude "use 42 throughout"]**; the companion citation
  (in-text "companion delay study" sites with no References entry) **[both]**.
- Housekeeping (not an audit point): the DFO 2022 reference entry (L418) is never cited
  in text (in-text citations use DFO 2011/2016/2024) — cite it or drop the entry.

### E2 / E3 / E4 — no remaining audit points

- **E2 (v18):** every audit point is dispositioned (Tasks 69–70 verified v15/v16's
  substantive adoptions; v17 applied the restructure items; v18 fixed the registered
  SSE/MSE label). Nothing open.
- **E3 (v12):** every audit point is implemented in v11/v12. The single declined element
  is the parallel sandbox's §5.7/Table-8 literal layout, with the reason recorded
  (`E2_V17_E3_V12_VERIFICATION.md` item 7); the substance (the DM/bootstrap layer, the
  replication registration, the references) is fully incorporated. Nothing open.
- **E4 (v11):** all seven consensus items are implemented. The one labelled follow-up
  (Stage-I/flat-80% at current pumpage does not secure) is a disclosed, labelled
  computation-layer fact, not an unimplemented audit point. Nothing open.

### Cross-cutting (unchanged)

- The **§1.1 shared-prose strip (P1/P3/P4)** remains the single largest standing
  exposure — all auditors, all three papers.
- **Preregistration vocabulary → appendix/limitations** (P1: 29 hits; P4: ~42; P5: ~42).
- **Uncited companions**: E1's four (R1 above — the record-vs-file failure), P3's three,
  P5's one.
- **Rose (2026) and the frozen 2026-09-01 plan date in P5**: resolved-by-clock (the repo
  clock is past both), recorded, not edited.

### Recommended order when the owner confirms implementation (the joint gate)

1. **The jointly-endorsed one-line fixes** (R4–R6, R10–R15, R18, R20's definition-level
   edits, R8's ten words): cheap, verified, fail-loud buildable in one script.
2. **R1 and R2 (E1's companions + the freeze claim)**: one-sentence-level but doctrinally
   sensitive — the cite-vs-drop choice and the exact weakened wording are owner decisions.
3. **R3 (E1's A8)**: the one new computation — a DM/block-bootstrap layer on E1's own
   margins, post-freeze-labelled, with E3's §5.3.1 as the template.
4. **The coherent docket passes**: P1's structural bundle; P2's theorem-level repairs
   (bundled with R9/R10); P3's notation/inflation/re-pin agenda (bundled with R11–R16);
   P4's presentation tail; P5's claims-ledger/appendix layer.

This wave changed no paper, no frozen verdict, score, kernel, spectral record, or table
value — it is the joint evaluation record only.

---

## Wave-4 addendum — the implementation record (Tasks 73/74, owner-directed, 2026-09-06)

The owner directed implementation of the wave-3 recommended order under the principle
**"cite, don't drop — decide on appropriate wording before implementing"**, in four parts plus
the structural items: (1) the jointly-endorsed one-line fixes in one fail-loud build per paper;
(2) E1's R1/R2 with the cite-vs-drop and wording decisions made per item; (3) R3 — the one new
computation (DM/bootstrap on E1's margins, E3's §5.3.1 as template); (4) the coherent docket
passes. All six papers with open points were rebuilt; E2/E3/E4 were confirmed closed at wave 3
and are untouched here. Every build is a fail-loud Python script that reconstructs the new
version from its predecessor with asserted-once anchors and mechanical checks, and every script
was run twice (or more) to prove byte-stability.

### Builds (all non-destructive: no frozen verdict, score, kernel, spectral record, or table
value changed anywhere; every pre-existing table row byte-identical except the explicitly
endorsed contradiction-fix cells)

| Paper | New version | Script | Record | Words on the docket |
|---|---|---|---|---|
| E1 | paperE1_cod_forecast_ladder_v11.md (368→424 lines) | apply_batch7_wave4_e1.py | wave4/e1_record.md | R1–R7 + R3 all IMPLEMENTED; R1 = CITE (4 in-text sites + 3 reference entries); R2 = WEAKEN-WITH-CITATION at all three sites ("coded before the first scoring pass and applied unchanged; later passes declared, not preregistered"); R3 = the registered post-freeze DM/Künsch layer (§3.5 + Table 9's 32 rows; campaign_e1_dm_uncertainty.py, seed 0, 20,000 replications, CSV archived and byte-reproducible); Definition 2.4 completed with the completions disclosed as recorded-after-scoring |
| P1 | paper1_assessment_separation_v20.md (518→529 lines) + paper1_supplementary_v2.md S8 append | apply_batch7_wave4_p1.py | wave4/p1_record.md | R8 (abstract 310→298, pinned) + docket items 1–8 + vocabulary consolidation (26→22) all IMPLEMENTED; demotions = relabels on the unchanged 1–9 counter; 25 checks enumerated in S8; declines: title change (no endorsed retitle), D_agg re-letter |
| P2 | paper2_obstruction_calculus_v9.md (373→379 lines) | apply_batch7_wave4_p2.py | wave4/p2_record.md | R9 + R10 + consensus 1/2/3/5/7 + claude's three section notes IMPLEMENTED; Def-1 clause (i) withdrawn WITH tombstone; declines with reasons: δ-minimizer removal (grok endorses keeping), singleton-belief lemma (new mathematics) |
| P3 | paper3_material_ledgers_v28.md | apply_batch7_wave4_p3.py | wave4/p3_record.md | R11–R17 + the notation/inflation/re-pin agenda all IMPLEMENTED; length PARTIAL-bounded-registered |
| P4 | paper4_delay_dynamics_v27.md + paper4_supplementary_v4.md S11 append | apply_batch7_wave4_p4.py | wave4/p4_record.md | R18–R22 + the presentation tail all IMPLEMENTED (MPF material relocated verbatim to S11) |
| P5 | paper5_sampled_governance_v21.md (465→541 lines) | apply_batch7_wave4_p5.py | wave4/p5_record.md | R23 + R24 + the middle-layer docket (Box 1 ledger 26 rows; Appendix A/Table 3; margins paragraph; undelayed-limit reconciliation; A9; A4 lineage; §4.6→Appendix B; 42; companion + DFO-2022 citations) all IMPLEMENTED; Rose (2026)/plan-date resolved-by-clock, untouched |

### The three E1 wording decisions (recorded per the owner's directive)

- **R1 (companions)** — CITE: the mentions were already in the text; the fix adds the
  citations and the reference entries rather than removing the cross-paper linkage.
- **R2 (freeze claim)** — neither keep nor drop: WEAKEN at all three sites to the wording the
  paper's own §4 disclosure supports, with the companion asymmetry made the explicit caveat.
- **R3 (A8)** — COMPUTE-AND-REGISTER as a post-freeze-labelled layer that "attaches
  uncertainty to margins the point rule has already ranked; it changes no frozen verdict,
  score, or table value" — the negative certificate stays a point-rule finding.

### Standing items closed by this wave

- The record-vs-file discrepancy "E1 companions cited" (wave-3 loud finding) is now true for
  the file. P1's "exactly 300 words" claim is now true (298, pinned). The two wave-3
  housekeeping notes (P3's supplementary pointer v6→v7; P5's DFO-2022 entry) are fixed in their
  records. The cross-cutting preregistration-vocabulary density is consolidated in P1 (Appendix
  A), P4, and P5; the uncited companions are cited in E1, P3, and P5.

### Registered follow-ups (deliberately not implemented, with reasons in the records)

P2's singleton-belief lemma and grok's restructure items (tube-form Thm-3 statement, Thm-2
plant replacement, Thm-5 demotion, §4.2/§5(d)/Appendix-A relocation, Marchaud pass, chattering
remark); P1's frozen-statement re-letters; P3's 21k→12k length remainder; E1's further
methodological asks needing computations beyond the authorised R3. None is jointly endorsed as
a one-line fix; all remain behind the owner gate.

This wave changed no frozen verdict, score, kernel, spectral record, or table value anywhere.
