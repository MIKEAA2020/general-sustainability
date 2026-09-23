# Joint Evaluation — v2 addendum: newly-examined places & remaining audit points
## Answers the two questions: (1) remaining points to add before implementing; (2) places not previously examined.

This addendum extends `paper2_joint_audit_evaluation_v1.md`. It records the results of a
**second sweep of places not previously examined**, cross-checked against paper 2 v20.

---

# Part E — Places examined for the first time (with results)

| Place | What it is | Result for paper 2 |
|---|---|---|
| `/home/user/errorbound.txt` | Fabian–Henrion–Kruger–Outrata (2010), *Set-Valued Analysis* — full text | **Paper-1** material (error-bound modulus). Not a paper-2 source. |
| `/home/user/formal_bridge_rescue_threshold.md` | Rescue-threshold κ\* / error-bound bridge for paper 1 | **Paper-1** material. Not paper-2. (Its *conclusion* — "a bridge that trivializes to a constant is decorative" — is the same sharp test I've applied to paper 2's g(B) direction.) |
| `/home/user/aubin2002.txt` | Aubin & Catté (2002), *Set-Valued Analysis* **10**, 379–416 — full text | **Paper-2-relevant and never cross-checked.** See finding E.1 below. |
| `/home/user/landmark_articles_svva.md` | SVVA journal-fit reading notes (5 landmark papers) | Confirms Aubin–Catté (2002) is "the journal's canonical statement of the structural/algebraic side of viability kernels and capture basins" and adds **Aubin (2001, SIAM J. Control Optim. 40)**. |
| GitHub repo root (never listed before) | ~40 files + 20 directories | Contains a **parallel audit campaign** (`batch 7 (audits of agent arena 1 paper rewrites)`) that audited *this same paper* at the markdown stage — see E.2. Also a **second corpus** (`papers/paper2_theorem_atlas`, agent-2 "theorem atlas") that is a *different* Paper 2 — not ours; excluded from this evaluation. |
| `/home/user/cover_letter.md` | Paper-1 cover letter template | Paper-1. Not paper-2. |
| `/tmp` snapshots | cover letter v1 + build_paper2_v15.py | No longer present (already consumed and recorded in session memory). |

---

# E.1 NEW finding — Aubin & Catté (2002) / Aubin (2001): a merited, missing formal bridge

**The paper's obstruction calculus is a calculus of certificates for the complement of the
(epistemic) viability kernel — and it never cites the set-valued literature that is *about*
that complement.**

- Aubin & Catté (2002) records **Poincaré's "shadow"** — "the set of initial points of K from
  which (all) solutions leave K in finite time … equal to the complement K∖Viab(K) of the
  viability kernel" — plus **capture basins**, **discriminating kernels** (the Cardaliaguet
  game-theoretic object), and the **bilateral/minimax fixed-point** characterization of these
  objects under discrete systems, differential inclusions, and dynamical games.
- Aubin (2001, *SIAM J. Control Optim.* **40**, 853–871), "Viability kernels and capture basins
  of sets under differential inclusions," is the direct predecessor of that formalism.
- Both are in the paper's target-journal lineage (Set-Valued Analysis / SVVA).

**Why merited (not decorative), under the user's own filter** ("add related work/formal bridges
only if genuinely merited"): the obstruction calculus answers the question the
capture-basin/discriminating-kernel program poses — *what happens on the failure side* — and a
Set-Valued Analysis referee will expect exactly this positioning. The bridge is a 2–3 sentence
paragraph in §1.3 (or §6.3) + two reference entries: the finite-time exit certificate is the
full-information "shadow" statement; the delayed-information/timing obstruction is its
observation-constrained analogue; the discriminating-kernel minimax form is the game-theoretic
skeleton of the Isaacs-order certificates.

**Disposition: implement (cheap, high-value).** Recommendation: §1.3 related-work sentence + 2
citations. No new mathematics.

---

# E.2 NEW finding — the "batch 7" parallel campaign: full paper-2 docket cross-check

A parallel audit campaign (`batch 7 (audits of agent arena 1 paper rewrites)/`) audited *this
paper* at the markdown stage (v5→v12) with its own docket, records, and apply-scripts
(`wave4/p2_record.md`, `wave5/p2_record.md`, `wave7/apply_batch7_wave7_p2.py`,
`wave8/apply_batch7_wave8_p2.py`, and `JOINT_AUDIT_EVALUATION.md`).

### E.2.1 Batch-7 items already implemented — ALL verified present in v20 ✓

| Batch-7 item | v20 evidence |
|---|---|
| R9 notation unification (ℐ/𝒥/𝔅, `proj_∃`); H-labels (H1.1–H1.2, H3.1–H3.3, H4.1–H4.3) | all eight labels present; counts match |
| R10 IRViab one-line definition (Defined-not-theorem) | `IRViab` ×4, one-line def |
| Consensus 1: Theorem 4 (H4.2) open-loop-on-blind-window restatement | present |
| Consensus 2: Theorem 1/3 closed-loop existence (H1.2)/(H3.3) + convexified reading | present (convexified ×5) |
| Consensus 3: Theorem 2 reframed as admissibility register | present (Proposition 1) |
| Consensus 5: Definition 1 / EViab contrast class | present |
| Consensus 7: Corollary 6 single-floor repair | present (Corollary 1) |
| §1.2 exhibit sentence scoped by mechanism | present (rewritten in v19/v20) |
| §6.4 "most-constrained" (not "least-constrained") | present (`least-constrained` = 0) |
| §6.4 coarseness as "exposure" + "refinement never harmful" | present (L1439: "refinement is never harmful (a finer observation merges nothing…)") |
| A.2 Lyapunov letter `W` (not `U`) | present (×3) |
| Notation one-letter-one-sort (P2: U/K/a/ε/d) | verified single-duty in v20 (further fixed by v16.1's λ→μ, α→λ, η→ζ, γ→κ) |
| "a fortiori" hyphenation | present (unhyphenated ×1, fixed v16) |
| wave-7 classification/CE-compression/meta-narration drops; wave-8 abstract/version-log/keywords | absorbed in v15→v16 |

**Conclusion: the batch-7 theorem-level docket is fully carried into v15→v20.** No residual from
the *implemented* set.

### E.2.2 Batch-7 items DECLINED there — remaining candidates, disposition now

| Item | Batch-7 status | v20 status | Disposition |
|---|---|---|---|
| **Singleton-belief sanity lemma** (ERViab = RViab for singleton beliefs under injective O; claude A8) | DECLINED ("new mathematics, needs owner-adjudicated proof review") | **absent** (the 3 "singleton" hits are prose, not the lemma) | **Candidate.** A two-line sanity check that the framework degenerates correctly (a singleton belief under an injective observation is full information). Merited only if stated as a one-sentence remark, not a numbered lemma. |
| **§5(c) observer citation** ("standard arguments in the observer-based control literature" cites nothing) | DECLINED ("a literature item, cannot be invented here") | **absent** — §5(c) observer-and-buffer transfer has no citation | **Candidate.** A real, verifiable citation exists (Veliov 1993 is already the output-feedback anchor; the ISS/observer-and-buffer argument is textbook — e.g. Sontag 1998 or Khalil). Only add after confirming the author's intended source; do not invent. |
| **Marchaud standing-assumption pass** (§2.1/§2.2; claude A7/E4) | left as residual | partial — "Marchaud" ×1 (L505, existence clause) | **Low priority.** §2.1 already states compact-valued/continuous/linear-growth-type conditions; naming them "Marchaud conditions" once, at the standing assumption, would be the complete pass. Cosmetic rigor. |
| **§5(d) / Appendix A relocation** (grok restructure) | left | Appendix A still at end | **Defer.** Relocation is presentation-only; earlier judgment (v3 synthesis: "relabel/move; do not silently delete") already resolved to keep-in-place. Not merited now. |
| **Theorem-2 plant replacement** (grok) | declined in favour of the admissibility register | n/a (register implemented) | **Closed.** |
| **Theorem-2 domain extension below S=1 + `B_t = Φ_t(B_0)∩V` presumption** (claude §3.2) | registered as residual | flagged text **absent** in v20's Proposition 1 | **Appears resolved** in the v15+ rewrite (no "S≥1" restriction, no `B_t = Φ_t(B_0)` presumption found). One-time verification recommended before submission, not an edit. |

---

# Part F — Answer to the two questions

## F.1 Remaining audit points to incorporate BEFORE implementing (the delta over v1)

The v1 joint evaluation was complete over the **8 local audit artifacts**, but **missed three
sources now examined**. The following are the genuinely new remaining points:

1. **Aubin & Catté (2002) + Aubin (2001) related-work bridge** (E.1) — **merited; implement.**
   The obstruction calculus is a calculus for the kernel's complement, and the paper does not
   cite the set-valued literature whose subject is exactly that complement.
2. **Singleton-belief sanity remark** (E.2.2) — candidate; one sentence, owner's call.
3. **§5(c) observer citation** (E.2.2) — candidate; needs the author's intended source confirmed.
4. **Marchaud standing-assumption naming** (E.2.2) — low priority; cosmetic.
5. **Theorem-2 domain presumption** — verify once, then close.

Plus the two still-pending items from v1's Part D that have **not yet been implemented**:
- **D1 — abstract polish** (soften "has lacked a comparable instrument"; "closed-form elsewhere" → safer; optional "necessary conditions" gloss).
- **D2 — one-sentence recourse-insufficiency pointer in §6.5** (blind-window vs post-observation recourse).

## F.2 Verdict on scope

Nothing in the newly-examined places contradicts any prior verdict. Specifically:
- The batch-7 campaign's *implemented* docket is fully present in v20 (verified item-by-item above).
- The agent-2 "theorem atlas" corpus is a **different** Paper 2 and is out of scope here.
- The Aubin–Catté bridge is the only newly-found item that clearly merits implementation; the
  other three (singleton remark, observer citation, Marchaud naming) are small and owner-gated.

**Suggested next action:** implement **D1 + D2 + the Aubin–Catté/Aubin(2001) bridge** in one
micro-revision (v21); then present the singleton remark / observer citation / Marchaud naming as
a 3-item owner decision list.
