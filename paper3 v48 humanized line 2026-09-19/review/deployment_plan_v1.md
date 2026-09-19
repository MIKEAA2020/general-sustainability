# Cross-batch deployment plan — the nine audits, one register, three destinations

**Date:** 2026-09-15 · **Inputs:** `review/ledger_audits_verified_v1.md` (batch 1: A1–A4 in `uploads/ledger upgrade.txt`, 13,707 words, audited against the v2 baseline) and `review/five_audits_joint_verified_v1.md` (batch 2: astra/opus/sol/fable/kimi in `uploads/p3 profound upgrades.txt`, 13,247 words, audited against `work/paper3.txt` + `revision/v4/paper3_v4.md`) · **Manuscript of record:** `revision/v4/paper3_v4.md` (body 103,311 chars, whole file 108,043 chars / 108,311 bytes, 15,016 words; `verify_v4.py` 34 checks, 0 failed) · **No manuscript text was altered in producing this plan.**

---

## 0. The three answers, short

1. **Effect of batch 2 on batch 1:** it does not overturn batch 1 — it *re-bases* it. Batch 1 was a design review of a larger project aimed at the v2 rewrite; batch 2 was a review of the current manuscript. Where the two agree (and they agree on the three structural gaps), the item stops being an auditor preference and becomes a finding, so it moves from "consider" to "should not be submitted without". Where batch 2 found nothing matching a batch-1 charge, that charge is either discharged by v3/v4 or was about the rewrite's losses, not the paper. Two batch-1 items change price materially and one can be closed outright (§1). Batch 2 also independently *confirms the distrust rule* batch 1 established: 3 of the batch-2 auditors' central claims are wrong, in the same ways batch 1's were (strong forms — "iff", "only", "no X exists" — and uncited references).
2. **Best employment:** one register, three destinations, by a single test — *a point belongs in the body if it changes what a definition in this article guarantees; in the supplementary if it changes what a reader can compute; in a companion if it requires an object this article does not define.* Under that test: **11 blocks to the body of v5** (wording plus the cheap verified theorems), **9 exhibits to a new supplementary file** (which the article currently promises and which does not exist), **1 companion paper** carrying the identifiability-and-certificate calculus, and **the project apparatus stays out** (both batches).
3. **Follow-up or all-here:** **both, split as above** — and not on taste grounds. The body can absorb the 11 blocks (≈ +2,200 words → ~17,200) without touching a single sentence; it cannot absorb the procedure, the estimator and the worked ledger (≈ +5,000–6,000 words including proofs and tables) without a subtraction, and "nothing subtracted" is a standing constraint. There is also precedent in the manuscript's own reference list: three companion Zenodo records, each DOI-resolved and each cited by its function ("Companion delay-dynamics study", "Companion review-screen study", "Companion assessment-separation study").

---

## 1. Item-by-item re-scoring of batch 1 against batch 2 and against v4

`hits` = case-insensitive count in `revision/v4/paper3_v4.md`, measured this turn.

### 1.1 Batch-1 bucket T (framing only, no new mathematics) — still unapplied, still free

| Batch-1 item | What it asked for | v4 state now | Effect of batch 2 | Verdict |
|---|---|---|---|---|
| **T1** | restate non-compensation as *anti-compensatory, not anti-scalar* ("no compensating weighting certifies; the vector, or a min with the binding component named, does") | `anti-compensatory` **0**, `compensating weighting` **0**; §7.2's theorem is stated as an existence claim over weights `w ≥ 0, w ≠ 0` | batch 2 supplied the *mathematics* the slogan needs: opus U1a (`(M)+(I)+(NC) ⇒ A = min`, 3 lines) and the compensation premium `Π ≥ 0`; sol §3D's exact statement agrees with what §7.1 proves | **Apply, and now it is two sentences instead of one** — the slogan plus the premium that makes it a measurement rather than a posture (staged S6 + body wording) |
| **T2** | alarm-vs-certificate asymmetry | `alarm` **0** | batch 2's opus U2 verified the one-directional half independently ("coarse accounts refute but never certify") and gave it a theorem-shaped form (EOD premium, one-signed optimistic) | **Apply** — and it is no longer just framing: U2 makes it quantitative for end-of-draw dates (staged S8) |
| **T3** | add the word "identifiability" where the paper already does the work | the term appears **1×** ("not identifiable from an anomaly series", §8.1); the *substance* (shift-invariance argument) is present | batch 2's astra identification sets `T_±` (0 hits in v4) and fable T1(b) are the same predicate, formalised | **Apply in §1.4 and §3** — this is the item where batch 2 *raises* the ask from "name it" to "define the identification set", which is a supplementary exhibit, not a word |
| **T4** | distinguish loss of safety from loss of assurance | `assurance` **1** | nobody in batch 2 raised it | **Apply** — one sentence in §10.3, unchanged from batch 1, still the answer to the "your framework is gamed by silence" attack |
| **T5** | antecedent humility: one paragraph stating the delta against MFA data reconciliation, SEEA/green accounting, viability theory, composite indicators (4/4 unanimous in batch 1) | `data reconciliation` **0**; `reconciliation` **2** (§3.4, different sense); `viability` **3**, all in the reference list; `SEEA` **0**, `SNA` **0** — and 0 in `work/paper3.txt` too | batch 2 never looked at positioning; but it *added the anchor* for the composition half (Baez–Li–Libkind–Osgood–Patterson, EPTCS 380 (2023) 77–96) and the LP/feasibility half (Gale 1957) | **Apply, and it is now the highest-priority item in this table** — see §2: the manuscript cites 14 of its own antecedents in the reference list and never mentions them in the body, so this is a structural defect, not a modesty request |
| **T6** | "the probability is already joint, because `τ_exit` is a minimum over moieties and both barrier signs" | `already joint` **0** | batch 2's min-uniqueness item (S6) is the same observation with a proof obligation attached | **Apply together with S6** — one display, one sentence |

### 1.2 Batch-1 bucket P (needed new proofs → author decision) — re-priced

| Batch-1 item | Re-priced by batch 2? | New state |
|---|---|---|
| **P7** — curvature number `κ` for depletion-trajectory shape (A3 T2; I verified M1–M3 correct, "4 lines of calculus") | **No.** Nothing in batch 2 touches trajectory curvature (`curvature` 0, `ddot` 0 in v4) | Unchanged: cheap, self-contained, needs the `S̈` data requirement stated or it collides with §8.1's own caveat. Still the best value/effort ratio batch 1 produced |
| **P8** — generalise non-compensation from linear weights to all continuous strictly monotone `f` (A4 item 40 / M6) | **Yes, and it changes the statement.** fable T1(b) proves there is *no* continuous strictly-increasing aggregator that is both faithful and complete; kimi §6's stronger claim ("none exists / locally dictatorial") is **false** because `s(b) = Σᵢ min(0,bᵢ)` is continuous, monotone, faithful, complete and non-dictatorial (verified) | **Re-scope:** do not generalise the theorem to strictly monotone `f` — that is now a *no-go* half-theorem. State instead the axiom pair (faithful + complete) and the uniqueness-up-to-calibration corollary, with `Σmin` as the counterexample that keeps the paper honest. Cheaper than P8 as proposed, and stronger |
| **P9** — half-space remark / "intervention windows instead of distance-to-kernel" (A1 §3, A2 T4 / M4) | **Yes, superseded.** astra's critical-margin budget (verified: `∃λ ≥ 0: λᵗGS_T + cᵗ ≤ 0 ⇒ ∫₀^T y ≤ V(x₀) + ∫λᵗGb`, and `T ≤ V₀/(y_req − β)`) is the same content with an LP certificate and it subsumes the article's Theorem 14 | **Close P9 by adopting S3** rather than writing a half-space remark. `half-space` and `intervention window` are 0-hit in v4, so nothing to reconcile |
| **P10** — review-interval bound beside §9's institutional-delay sentence (A3 T5 / M7) | **Yes, and its cost collapsed.** v4 mentions `review interval` **only** in the reference list; the batch-2 pass verified the companion record live (`doi:10.5281/zenodo.22554217`, Abaee 2026, posted 2026-09-06), which contains the certified figures: Hopf crossings near 3.7 and 150 yr, and mobilising-review restabilisation above ≈6.5 yr | **Now one sentence plus a DOI**, with the displacement-bound hypothesis stated. It also retires `qwen p3 upgrade2.txt`'s invented "review interval longer than 3 years" — contradicted by the registered companion, not merely unsourced |
| **P11** — certificate-completeness framing (barrier certificates as SOS/SDP) | Corroborated externally: Prajna–Jadbabaie HSCC 2004 477–492 and Prajna–Jadbabaie–Pappas IEEE TAC 52 (2007) 1415–1428 verified this turn (the 2007 paper is the stochastic case, i.e. the one relevant to §9's surrogates) | Keep as a §9 positioning sentence + the SOS remark in the supplementary, not as new theory here |
| **R** — reject for the article, keep in the project proposal (passports, dashboards, ratchet rules, certificate expiry, engine/compiler, pilots, claim linter, gold corpus, the 78%/2.8×/+38%/14-yr figures) | **Partially overturned — two items move.** sol §2's certificate vector (three truth values, `?` ≠ `⊥`) and sol §3D's worst-concealed-deficit LP are the *content* of two R items with none of the apparatus: no schema, no engine, no pilots | Move `certificate vector` → **body §3.1** (staged S11) and `worst concealed deficit` → **supplementary exhibit + one body sentence** (staged S10). Everything else in R stays in R; that was and remains the correct call (batch 2's project proposals — Lean 4, JSON schema, time-expanded checker, MDV, five standards amendments, pilots — are non-article claims, declined in the batch-2 review) |

### 1.3 What batch 1 caught that batch 2 did not, and vice versa

| Caught by batch 1 only | Caught by batch 2 only | Caught by both |
|---|---|---|
| the slogan `Σ_m` vs `min` falsifiability (→ N7); abstract↔Lemma 3 direction mismatch; the ε label on the resources row; the "2026 pinned source" vintage rows; **zero figures and zero numbered tables**; no code/repository for computational claims; the 43-stock cohort's non-reproducibility by either public RAM release | residual bound on `∫ℓᵗCd_x` (**no bound in v4 — 6 hits for `d_x`, none bounding the statistical discrepancy**, which voids the conservation predicate as stated); right-null space / closure cone (0 hits); Liebig/`min_i` framing absent; identification sets `T_±`; latest-safe-intervention LP; `O_p(σ/β)` anomaly-index result; EOD one-signed optimism; sign law and `η ≷ ½gτ` | **no certificate procedure** (batch 1: A3's whole architecture; batch 2: 4/5 audits, closure cone); **no worked empirical ledger** (batch 1: A1 §9/A4; batch 2: 5/5); **identifiability as the next layer, un-named** (batch 1: 3 audits; batch 2: astra + fable T1(b)); **LP/Farkas duality as the audit mechanism** (batch 1: A3; batch 2: 5/5 — note `Farkas` is still 0-hit in v4 while `linear programme` appears 2×) |

Nine audits in two batches, and the intersection of the two "caught by both" column is exactly the three things I would defend as *the* remaining agenda: a certificate procedure, one worked ledger, and the identifiability layer named as such.

---

## 2. A defect neither batch stated, found while cross-checking them (this turn, measured)

The batch-1 charge "positioning is missing" (N2/T5) is stronger than they wrote it. Of the reference entries in v4 whose first author I could resolve and count against the body, **14 are never mentioned in the body at all**: Aubin (viability theory), Blomqvist et al. (footprint critique), Chhikara–Folks (inverse Gaussian), Ekins et al. (critical natural capital), Illakwahhi et al. (phosphate), Lin et al. (national footprint accounts), Martinez-Alier et al. (weak comparability of values), Meadows et al. (Limits to Growth), Munda–Nardo (non-compensatory composite indicators — the direct antecedent of §7), Neumayer (weak vs strong), Øksendal (SDEs), Redner (first-passage), Tilton 2003 and Tilton–Lagos 2007 (the reserve-life literature §8.2 classifies). Ten are mentioned: Abaee, Brunner, Daly, Eurostat, Feinberg, Fischer-Kowalski, Güntner, Jacquez–Simon, Ricard et al., Tapley et al.

Three of the fourteen (Redner, Chhikara–Folks, Øksendal) are the *technical basis of §9*; two (Tilton ×2) are the object of §8.2; one (Munda–Nardo) is the non-compensation literature §7 answers. A referee in an accounting or ecological-economics venue reads that pattern as a paper that knows its literature only through its bibliography. This, not auditor preference, is why T5 must be applied — and it costs one paragraph in §1.2/§1.3 plus three in-text anchors in §7.2, §8.2, §9.6.

Two adjacent, verifiable submission-readiness gaps found in the same way:
- **The supplementary file does not exist.** §Declarations promises "the ten-state admissibility template and its three audited negative witnesses, the registered identification ladders …, the split-assignment mechanism table, the statement inventory …" — the workspace contains no such file (`find . -iname "*supp*"` → 0 results). Every surviving point about *what a reader can compute* has a home, and it is empty.
- **No code-availability statement.** Declarations carries Data availability, Supplementary material, competing interest, AI declaration — four items, none of them code, in a paper whose remaining agenda is a set of linear programs and a Monte-Carlo argument (fable T7, which I confirmed by simulation: index ≈ 0.2 yr at every record length from `n = 10²` to `10⁵`, 400 reps, `β = σ = 1`).

## 3. The trust rule both batches teach (one line, and why)

Batch 1: 7 of its auditors' theses were wrong as stated (M11–M17), and they cited a Claim Passport, a dashboard, a compiler and a "78% regenerative" figure that do not exist anywhere in the article. Batch 2: 3 of 23 wrong (fable T10's sign slip, kimi §6's false non-existence, opus U5's "iff"), plus one invented reference (*Compositional Resource Flow Accounting* — verified absent this turn, after I nearly recommended it). **Rule: an audit's *objects* are claims to verify, never facts to paste** — its mathematics gets re-derived, its strong forms ("iff", "only", "no X exists") get a counterexample search, and its citations get resolved before they appear in any file of ours.

---

## 4. The consolidated register: every surviving point, with destination and cost

Destination test, applied throughout: **BODY** changes what a definition guarantees · **SUPP** changes what a reader can compute · **COMPANION** needs an object this paper does not define · **PROJECT** is not an article claim · **PARKED** is an audit error unless restated.

| # | Surviving point | Source(s) | Destination | Cost | Staged? |
|---|---|---|---|---|---|
| 1 | Anti-compensatory-not-anti-scalar, plus joint-probability sentence and `Σmin` caveat | B1 T1/T6, B2 opus U1a, sol §3D, kimi §6 corrected | BODY §7.1–7.2 | ~180 w | S6 |
| 2 | Compensation premium `Π = A − min ≥ 0` and worst-concealed-deficit LP `δ*_j(z)` | B2 opus U1, sol §3D | BODY sentence + SUPP recipe | ~90 w + 1 LP listing | S6, S10 |
| 3 | Accumulated-liquidation proposition `A(0)−A(T) ≥ α∫Y − ∫r` | B2 sol §3C | BODY §5.4 | ~120 w, 1-line proof | S9 |
| 4 | Critical-margin budget + `T ≤ V₀/(y_req − β)`, λ by LP (closes B1 P9) | B2 astra, subsumes Thm 14 | BODY statement, SUPP LP mechanics | ~240 w | S3 |
| 5 | Sign law for readout monotonicity and the `η ≷ ½gτ` threshold | B2 opus U3a/b | BODY §6.2/6.4 | ~150 w | S7 |
| 6 | `O_p(σ/β)` anomaly-index result (with my simulation as the check) | B2 fable T7 | BODY §8.1 (status: illustrative) | ~110 w | S5 |
| 7 | EOD premium `365 Σ wᵢ(rᵢ − r_min)`, one-signed optimism | B2 opus U2, B1 T2 | BODY §7.3/§8.2 | ~130 w | S8 |
| 8 | Closure cone / right-null space, and `δ_m = 1 − κ_m(τ_use)` with the *one-sided* horizon bound | B1 A3, B2 4/5 audits; opus U5 corrected | BODY definitions (2 short displays) + SUPP proofs | ~300 w | S2, S2′ |
| 9 | **Residual bound on the statistical discrepancy** `∫ℓᵗCd_x` — currently unbounded, which voids the conservation predicate as stated | B2 (unique to it; verified by grep: 6 hits, no bound) | BODY §3.4/§3.5 — *a defect in the article's own statement* | ~140 w | S1 |
| 10 | Certificate vector over `{established, not established, not applicable}` with the scope clause ("separately certified, not pairwise independent; the implications that hold are Propositions 1–2") | B1 A3 §1, B2 sol §2, astra 4A | BODY §3.1 (table) | ~1 table | S11 |
| 11 | Identification sets `T_±`, Witness B (`ẋᵢ = −kxᵢ`, `ẇᵢ = kxᵢ`, `(2,98)` vs `(50,50)`, identical aggregate `Z = 100e^{−kt}`, barriers at `log2/k` vs `log50/k`), and the non-existence of a faithful+complete strictly-increasing aggregator | B1 T3, B2 astra + fable T1(b) | SUPP (construction + table); BODY gets the one-line consequence | ~250 w supp | S4 |
| 12 | Promotion-rule table (`R/P`, `Δz/[−ż]₊`, `log(B/B_min)/F` and the four/three conditions each) | B1 A1/A2, B2 sol §3A + astra 4A | SUPP (consolidation of §8.1–8.3 prose) — this is the answer to "diagnoses without repairs" | 1 table | not yet staged |
| 13 | Müller–Kamke comparison for the monotonicity claims, stated with the cooperative/quasi-monotone hypothesis | B2 fable T5 | BODY §6.2 remark + citation (Smith 1995) | ~60 w | folded in S7 |
| 14 | Antecedent positioning: one paragraph (MFA reconciliation, SEEA/green accounting, viability, composite indicators, stock-flow composition) + 3 in-text anchors; SEEA/2025-SNA sentence | B1 N2/T5 (4/4), this turn's §2 finding | BODY §1.2/1.3, §7.2, §8.2, §9.6 | ~260 w | not staged — needs the author's factual sign-off on SEEA wording |
| 15 | Review-interval sentence with the verified companion figures (3.7 / 150 yr; ≈6.5 yr) and `doi:10.5281/zenodo.22554217` in place of "in review" | B1 P10, this turn's citation work | BODY §9/§10 | ~70 w | S8 adjacency |
| 16 | Worked ledger, end to end: typed primitive ledger → certificate vector → LP checks → the three classifications reproduced | B1 4/4, B2 5/5 | **SUPP exhibit** (with the code), cited from §8 | 2,000–3,000 w | not article text |
| 17 | Composition calculus (ledger morphism, pushforward of certificates across ports; conservation composes, positivity under donor-limited kinetics, safety needs an interface contract) | B2 3/5 (opus U2, sol §3E/§4, kimi §5) | **COMPANION** | new object | S12 note only |
| 18 | Gate theorems, ratchet rules, passports, expiry, dashboards, pilots, Lean 4, JSON schema, time-expanded checker, MDV, standards amendments, claim linter, "78%/2.8×/+38%/14-yr" | B1 R + B2 declined list | **PROJECT** | — | correctly out |
| 19 | fable T10 recycling identity as printed; kimi §6 non-existence; opus U5 "iff"; opus U6 replacing Definition 5; fable T9's `σ`; `certified` as a status label | — | **PARKED** (each has a corrected restatement; only the restatements are admissible) | — | — |

Rough totals: BODY ≈ 2,200 words added to 15,016 → ~17,200; SUPP ≈ 4,500–6,000 words (it starts empty); COMPANION ≈ 6,000–8,000 words; nothing removed from anywhere.

---

## 5. Should there be a follow-up paper? — the recommendation and its boundary

**Yes, one, and only one.** The nine audits do not point at two missing papers; they point at one missing *second layer* (a procedure: how to certify, compose and identify) sitting on top of a first layer that is complete and, in its own terms, finished (a semantics: what the objects mean and what they cannot do). Concretely:

**Keep here (this paper, v5).** All of rows 1–15. Each changes what a definition guarantees, and each is short. The paper's §1.4 already lists seven contributions, all of them semantic; rows 1–15 keep that character and make the semantics *sharper* (a bounded residual, a premium, a deficit LP, a third truth value, a named identification failure). Rows 9 and 14 are the two I would not let go: the first is a hole in the article's own claim, the second is what a specialist referee looks for first.

**Move to supplementary (rows 11–12, 16).** Everything that changes what a reader can compute: the LP listings for `λ` and `δ*_j`, the closure-cone and right-null proofs, Witness B's full construction and the identification-set table, the promotion-rule table, and the worked ledger with its code. The Declarations paragraph already promises this file — the only work is to write it, and the surviving points fill it in the order the paragraph lists them.

**Move to a companion (row 17).** Title candidate: *Composing certificates: an identifiability and certification calculus for typed resource ledgers*. Thesis: ledgers are objects of a category whose morphisms preserve typed flux structure; conservation certificates compose along ports carrying equal-and-opposite moiety fluxes, positivity composes under donor-limited interface kinetics, and barrier safety composes only under a declared interface contract — so a portfolio of individually safe ledgers can be jointly unsafe, and the obstruction is computable. Contents: the morphism/pushforward definition (the object this paper does not have), the composition theorems with proofs, the observer/identification layer (aggregate dynamics vs component event times, `T_±`, the non-existence theorem for strictly-increasing faithful-and-complete aggregators), the checker as a worked exhibit, and the verified anchors: Baez–Li–Libkind–Osgood–Patterson EPTCS 380 (2023) 77–96 (open stock-flow diagrams, decorated cospans), Baez–Pollard arXiv:1704.02051 and Anand–Pollard–Breiner–Nolan–Subrahmanian 2019 for the adjacency batch 2 mis-cited, Gale Pacific J. Math. 7 (1957) 1073–1082 for the cut condition, Prajna–Jadbabaie (2004) and Prajna–Jadbabaie–Pappas (2007) for certificates as semidefinite obligations, Ahuja–Magnanti–Orlin (1993) for the bounds form. **What must not move:** §7 (non-compensation), §8's classifications, and the identifiability *consequence* sentence in row 11 — a companion that removes the paper's negative results leaves both papers weaker, which is the mistake batch 2's opus cut-list would have made.

**Why not "all in this paper plus supplementary".** Measured: body 103,311 chars; §5 is 3,327 chars and §7 is 4,369, so rows 1–10 land comfortably and *improve* the balance against §2 (15,864) and §8 (12,283). Rows 16–17 do not: a worked ledger plus an estimator plus a composition calculus is 7,000–9,000 words, which puts the article past 22,000 and — because §4, §8 and §9 are all load-bearing and nothing may be subtracted — there is no way to make it fit that doesn't cut a status-bearing paragraph. Two papers of 17k and 7k words are each publishable; one of 24k with an 8k appendix is a paper under revision forever.

**Why not "two supplementary files instead of a companion".** The composition results need a definition (ledger morphism) that no existing section of this paper states; putting a new definition in an appendix of a semantics paper reads as a scope change, and it strands the novelty where no one will cite it. The three DOI-resolved companions in the reference list show the working convention for exactly this case: one registered record per distinct object, cited by function.

---

## 6. Build order, once decisions are back

1. **Nothing applied yet, deliberately:** `revision/v4/paper3_v4.md` stays the manuscript of record until the §7 list below is answered.
2. `revision/v5/build_v5.py` — replay from v4 by unique-anchor insertions only (the v4 method: `build_v4.py` semantics, no hand-editing of the markdown), for rows 1–15 as accepted.
3. `revision/v5/verify_v5.py` — new checks on top of the 34: every v4 sentence-unit must appear verbatim in v5 (the set-comparison method, not reconstruction); `\square` count unchanged except inside new proofs; counter monotonicity for Prop 21–32 on the shared main counter; no banned phrase reintroduced; the 14 body-absent citations now ≥ 1 body mention for the three anchors chosen.
4. `revision/v5/paper3_v5_supplementary.md` — create the promised file, ordered as its own Declarations paragraph lists it, then rows 11–12 and 16.
5. `revision/v5/code/` — LP recipes + the `O_p(σ/β)` simulation + ledger exhibit; add the **Code availability** line to Declarations (currently absent).
6. `work/paper3.txt` untouched; `review/*` untouched except appended corrections.
7. Companion: `paper5/composition_certificates_v1.md` drafted from S12 + rows 11/17, with the citation list above already verified.

## 7. Decisions needed (each with the default I recommend)

| # | Decision | Default |
|---|---|---|
| D1 | Accept rows 1–10 as v5 body insertions? | Yes — all verified this turn or last; row 9 is not optional in my view (it is a hole in the paper's own statement) |
| D2 | P7 curvature `κ` (row absent from B2, cheap from B1) | Include, power-law family only, with the `S̈` data requirement stated |
| D3 | P8 re-scoped to the axiom-pair form (not the strictly-monotone generalisation) | Include as re-scoped; do **not** publish the "false-safe volume" metric without a declared measure |
| D4 | SEEA/2025-SNA sentence + positioning paragraph (row 14) | Include — and it needs your wording for the standards claim; I have the facts (SEEA CF adopted 2012; the revision's adoption slated March 2028; the 2025 SNA adopting depletion-as-cost-of-production) but the sentence is yours |
| D5 | Worked ledger: supplementary exhibit vs companion exhibit | Supplementary here, companion gets the checker — so the paper gains an exhibit without a scope change |
| D6 | Companion paper now (between v5 and submission) or after v5 is submitted? | After submission of v5 — v5 does not depend on it, and the composition results do not need to be in hand before the semantics paper is fixed |
| D7 | Replace §10.1's "in review" placeholder with `doi:10.5281/zenodo.22554217` | Yes (verified live, correct author and date) — and the other two companion DOIs should be spot-checked at submission, as `22554297` / `22545740` sit in the same numbering family but I did not resolve them |
| D8 | Code availability statement | Add it |

*This plan adds no claim to the manuscript and softens none: rows 1–19 are dispositions, not edits. `verify_v4.py` re-run during the cross-check: 34 checks, 0 failed.*

---

## 8. Status: applied at the recommended defaults (2026-09-15)

Rows 1–10 of §4 and rows 14–15 were applied to **`revision/v5/paper3_v5.md`** as Definitions 21–23,
Theorem 24, Propositions 25–32, Remark 33 and six unnumbered passages (25 logged insertions + 3
logged replacements; `verify_v5.py` 65 checks, 0 failed; insert-only reconstruction byte-identical to
v4). Row 11's Witness B was promoted from supplementary to **Proposition 31** in the body; rows 12
and 16 went to **`revision/v5/supplementary_v5_additions.md`** with the exhibit code in
`revision/v5/code/` (D5, D8); row 17 remains staged for the companion, unbuilt (D6). Three
corrections to this plan are recorded in `revision/v5/README_v5.md` §2: batch-1 T4 was already
discharged in v4 §10.3; T1/T2 were half-discharged by §7.2's closing sentence; and Proposition 32's
figures were restated from a re-run (median 0, mean 0.21–0.25 yr, q90 0.81–1.00 yr) rather than the
single "≈0.2 yr" quoted here. Rows 18–19 unchanged: still project deliverables and still parked.
