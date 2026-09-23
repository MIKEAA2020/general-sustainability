# Joint Evaluation & Verification — ALL paper-2 audits (8 prior + 2 new attachments)
## Verified against paper 2 v20 (current manuscript). Every claim tagged; math in the new files spot-checked computationally.

**Sources jointly evaluated (in chronological order of the session):**
1. `paper2_v15_readability_humanization_audit.md` (Tiers 1–4)
2. `paper2_generalization_merged_synthesis.md` (Parts A–E)
3. `paper2_generalization_merged_synthesis_v2.md` (complete-base; Part F register)
4. `paper2_generalization_merged_synthesis_v3.md` (G.1–G.6, H.1–H.3)
5. `paper2_approximate_certificate_verdict_v1.md` (statistical-certification exclusion)
6. `paper2_v17_merit_evaluation.md` (spine + computational merit test)
7. `paper2_v18_selector_framework_verdict.md` (selector-framework attachment)
8. `paper2_v20_deep_review_report.md` (5-question deep review)
9. **NEW:** `uploads/qwen journals.txt` (journal fit + abstract critique + SCL/Automatica elevation)
10. **NEW:** `uploads/obstruction calculus nonstandard.txt` (recourse-aware continuous-to-finite theorem package; kimi stub truncated)

**Tag legend:** ✓ done in v16–v20 · ≈ already present in v15 · ✗ wrong · ⚠ journal-conditional judgment · → deferred (companion paper) · ⭘ excluded (fails the non-decorative test).

---

# Part A — Joint verification of the two NEW files

## A.1 Cross-file relationship
The two attachments are **different layers of the same recommendation**, and they agree with each other and with the paper's current state:

| Point | qwen journals | nonstandard | Paper v20 |
|---|---|---|---|
| "Six mechanisms" is a weak identity | says stop presenting six coequal mechanisms | says belief recursion is background, not the contribution | already fixed — selector principle + ladder + summary table (v18/v20) |
| Fix policy/disturbance semantics | yes (§12.1–12.2) | yes (quantifier order, §2.3) | already fixed — semantic-conventions ¶ (v17) |
| Uniform margin | yes (§12.3) | yes | already fixed — Prop 2 (v17) |
| Value-function σ\* | yes (§12.4) | yes (blind-window σ\*) | already fixed — Remark 2 (v18) |
| Belief recursion is standard | yes (gpt: "standard relative to safety games") | yes ("cite as background, not re-proved") | already scoped honestly (Thm 4 + §6.5) |
| Farkas/dual certificates are the publishable core | yes | yes — and it *builds the missing theorem* | paper has the static Farkas case only (v17/v19) |
| Helly / finite-witness / sparsity | gpt proposes it | **proves it, then sharpens it** (m+1 is false for blind controls) | **not in paper** → genuinely new |
| Continuous-to-finite bridge with error bounds | — | **the main new theorem** | **not in paper** → genuinely new |
| Where does it belong | journal choice depends on rework | "SCL-shaped narrow paper"; Automatica needs more | — |

**Conflict:** none substantive. One tension: qwen journals *implies* the paper should be reorganized for a broader venue; the nonstandard file *implies* the real gap is a new theorem, not reorganization. Both are right about different questions: qwen is answering "where to send it," nonstandard is answering "what theorem would actually carry it at a top venue."

## A.2 Math verification of `obstruction calculus nonstandard.txt` (computational spot-checks — ALL PASS)

| Claim | Check | Result |
|---|---|---|
| Sharp limitation: with scalar input `u∈[0,1]` and `q+1` indistinguishable modes, every proper sub-belief is viable but the full belief is not, and every certificate needs all `q+1` witnesses | verified the forced-sum contradiction (`q ≤ q−ε`) and both sub-belief recovery policies for q=1,2,5 | **correct** |
| Hence the Helly bound `m+1` is **false for blind control functions**; the correct count is information–time rank | the construction defeats any `m+1`-witness bound (m=1, needs q+1) | **correct** — a genuinely nonstandard, sharp result |
| 4D example: `Σ λⱼ nⱼ = 0` for λ=(3/8, 5/16, 5/16) | computed `(0,0)` exactly | **correct** |
| Full-information critical position 93/50 = 1.86 < 2 | computed | **correct** |
| Exact delay threshold `τ_max = 2 − 34/25 − 1/2 = 7/50 = 0.14` | computed | **correct** |
| `Γ(τ) = τ − 7/50`, so `Γ(0.2) = 0.06 > 0` | computed | **correct** |
| Blind-window test **misses** the obstruction: `u=0` keeps all branches safe at τ=0.2 (margin 39/25 = 1.56 < 2) | computed | **correct** — this is the key gap the package fills |
| Mesh study `ρ(h) = 0.06 − 0.3h` (0, 0.03, 0.045, 0.054, 0.057) | computed | **correct** |
| `e = 3h²`, β = −14/25, β+e = −53/100, Farkas contradiction −3/100 < 0 | computed | **correct** |

The package's central example is internally consistent and its sharp lower bound is correct. **This is the first external input in the session that contains a genuinely new, correct theorem** (the earlier statistical-certification direction failed the sharp test; this one passes it).

## A.3 What the two files contribute that is genuinely new (vs. v20)
1. **Recourse-aware nonviability certificates** — finite LPs whose infeasibility certifies failure of *every measurable information-adapted controller*, with an explicit error sandwich `ρ ≤ J ≤ ρ + R_U V_U h_u + δ_β + L h_t`, finite termination, and completeness under refinement. This is the rigorous, error-bounded guarantee the user's sharp test demanded — the *deterministic* analogue the paper's certificates lack beyond finite systems.
2. **Post-observation recourse insufficiency** — a failure mode the paper's current certificates (Thm 1–4, σ\*) structurally cannot detect: blind-window trajectories safe, but no post-observation recovery exists. The 4D example proves σ\*-type tests are strictly weaker here.
3. **Information–time sparsity law** + the sharp `m+1`-is-false counterexample — corrects the naive Helly intuition.
4. **Semi-infinite/vertex-reduction handles** for continuously parameterized beliefs — upgrades the static Farkas case to scalable computation.

---

# Part B — Consolidated register of ALL audit claims (master table)

## B.1 Prior audits 1–8 (status vs. v20)

| Claim (source) | Status |
|---|---|
| Claim reframe "necessity side" → sound sufficient certificates (A#1, v2, v3 G.5) | ✓ v16; cover letter v2 |
| Semantic conventions subsection (v2 D.1.2) | ✓ v17 |
| Demote Thm 5→Prop, Thm 2→construction; `amsthm`+`\ref` (v2 D.1.3, v3 G.1) | ✓ v16 |
| Full meta-commentary cut, zero-grep pass (v2 D.1.4, v3 G.4) | ✓ v16; re-verified clean in v20 scan |
| Hedging consolidation (v2 D.1.5) | ✓ v16/v16.2 |
| Symbol renames + collision audit (v2 D.1.6) | ✓ v16 → collision bug → fixed v16.1 |
| Prose surgery: em-dashes, word tics, §1.1 essay (v2 D.1.7–8) | ✓ v16.2 (em-dashes 157→130; optional further pass ⚠) |
| Abstract ≤265 words (v2 D.1.8) | ✓ 264 words |
| Housekeeping: "companion", code-availability, Zenodo (v2 D.1.9) | ✓ v16/v17 |
| Finite-horizon completeness + obstruction tree (v2 D.2.11; the one new theorem) | ✓ v17 Thm 4 + one-step instance v20 |
| σ\* timing threshold, corrected `sup_u inf` quantifiers (v2 D.2.13; conflict C) | ✓ v18 Remark 2 |
| Uniform-margin lemma (v2 D.2.14) | ✓ v17 Prop 2 |
| Farkas elevation + worked example + normalization + margin (v2 D.3.15–16) | ✓ v17 example; margin v19 |
| Monotonicity partial order (v2 D.3.19) | ✓ v18 Prop 5 |
| Witsenhausen bridge (v2 #5, v3) | ✓ v19 |
| Figures: fibre / common-action / timing / CE (v2 D.3.18; Qwen §4.5) | ✓ v17 Fig 1–3; v20 Fig 4 |
| §4.2 stub delete (v3 G.2) | ✓ v16 |
| a-fortiori hyphenation (v3 G.3) | ✓ v16 |
| Cover-letter claim sync (v3 G.5) | ✓ v16 |
| Supplementary (v3 G.6) | ⭘ v20 verdict: not merited (self-contained, no code) |
| Belief-space Nagumo unification (v3 H.1) | → companion (would re-derive the cited estimation-tube reduction) |
| Optimal-coarsening design theorem (v3 H.2) | ≈ static part in Cor 1 + minimal-refinement rule (v17); full theorem → companion |
| Two-regulator example (v3 H.3) | → companion |
| Statistical/approximate certification (verdict #5) | ⭘ excluded (Doob–Dynkin/Blackwell restatement; fails necessity/rigor test) — **reconfirmed, and note this is distinct from the NEW deterministic LP package** |
| g(B) full margin theory, rescue budget (v2 D.3.16; v17 eval) | ⭘ excluded (duplicative of Thm 1/3 bounds + Prop 2); Farkas-margin reading kept (v19) |
| Cost-min design problem (v2 D.3.19) | ⭘ excluded (formulation without theorem) |
| Distance-to-viability suite (v2 D.3.20) | ⭘ excluded (definitions without theorems; T_max = σ\* already Remark 2) |
| Algorithm box (v2 D.3.17; qwen-fu §14–15) | ≈ partial: one-step tree instance (v20); full algorithm → companion (now supplied by the nonstandard file) |
| A–E taxonomy (v2 D.2.12) | ✓ via ladder + summary table (v18/v20), without a reader's-guide layer list |
| Integrated multi-layer example (v2 D.3.17) | ⭘ excluded (Farkas example already carries the payoff) |

## B.2 NEW: qwen journals.txt

| Claim | Status |
|---|---|
| Broad-journal abstract rewrites (EMA-style) | ⚠ journal-conditional — not merited on the technical track; use only if pivoting to EMA |
| Journal ranking: EMA (broad) / SVVA (math) / EJC (control) / JEDC (economic) / Ecological Modelling / ESP (policy) | ⚠ judgment, **consistent** with the session's earlier EMA-scope + JEDC-editor vetting; v20 sits squarely on the SVVA track the cover letter targets |
| "has lacked a comparable instrument" is too sweeping → "has received less systematic treatment" | ✓ **actionable, merited** (abstract + conclusion, 2 spots) |
| "closed-form elsewhere" is risky (not every non-polyhedral case has closed form) | ✓ **actionable, merited** (abstract) |
| "necessary conditions … " needs a one-clause gloss | ✓ **minor, merited** (abstract, optional) |
| Abstract enumerates too many mechanisms | ≈ mostly fixed by selector framing; the enumeration can be trimmed one clause — optional |
| Terminology: "epistemic kernel" → "observation-based viability kernel" | ⚠ journal-conditional — keep for SVVA (set-valued tradition); change only for SCL/Automatica |
| Remove sustainability rhetoric / Appendix A / six-mechanism taxonomy | ⚠ journal-conditional — for control venues only; keep for SVVA/EMA/JEDC |
| Add belief dynamics, value function, uniform margin, computational section | ✓ already done (v17/v18) except the computational LP section → companion |
| Helly / finite-witness / vertex reduction / semi-infinite duality | → **new; supplied by the nonstandard file** (companion) |
| Numerical study with timings | → companion |
| gpt: "belief recursion is standard relative to safety games; be conservative about novelty" | ✓ **correct and already honored** (Thm 4 scoped; §1.3 + §6.5) |

## B.3 NEW: obstruction calculus nonstandard.txt

| Claim | Status |
|---|---|
| Recourse-aware continuous-to-finite certificate (main theorem: LP bridge, error sandwich, completeness, sparsity) | → **companion paper** (SCL-shaped). Verified correct. NOT v21 — different model class (affine conditional dynamics, polytopic data, exogenous partitions) and paper-scale content |
| `m+1`-is-false sharp limitation | → companion (paper 2 never claims Helly, so no correction needed in the paper) |
| 4D three-branch example (every pair viable, triple not; blind test misses it) | → companion |
| Oracle-recourse sound extension (post-blackout sensing) | → companion |
| Rational checker + mesh study + algorithm | → companion |
| kimi `CERTIFY-NONVIABILITY` stub | truncated mid-algorithm; duplicates Thm 4's recursion — nothing new to evaluate |

---

# Part C — Joint bottom line

**1. All 8 prior audits are fully accounted.** Every claim is either ✓ done in v16–v20, ≈ already present, ⚠ journal-conditional, → deferred to a companion, or ⭘ excluded with a recorded reason. Re-verified against v20 source. No audit item is silently dropped.

**2. qwen journals.txt** is a journal-strategy document, mostly already honored by v20 on the technical track. Its two genuinely actionable points are abstract polish ("lacked a comparable instrument" → softer; "closed-form elsewhere" → safer), plus an optional gloss on "necessary conditions." It does **not** mandate a rewrite for the SVVA track the paper currently targets.

**3. obstruction calculus nonstandard.txt** is the session's first genuinely new, correct mathematics. It passes the user's sharp test *exactly where the statistical-certification direction failed*: it is necessary (exact duality), rigorous (error sandwich proved), and useful (bounds that matter to safety-critical referees). But it is a **different model class and paper-scale** — the right disposition is a **companion paper**, not a v21 fold-in.

**4. One merited honesty pointer for paper 2 (cheap, high-value):** the σ\* threshold (Remark 2) is a *blind-window* test, and §6.5's limitation list does not currently name the failure mode the nonstandard file proves is strictly beyond it — **post-observation recourse insufficiency** (blind trajectories safe, recovery impossible). One sentence in §6.5 makes the scope boundary explicit and tees up the companion.

---

# Part D — Updated prioritization (decision points)

| # | Action | Effort | Verdict |
|---|---|---|---|
| D1 | **Abstract polish (v21, micro):** soften "has lacked a comparable instrument" → "has received less systematic treatment" (abstract + conclusion); "closed-form elsewhere" → "analytic drift-and-timing conditions elsewhere"; optional "necessary conditions" gloss | one script pass | **recommended** |
| D2 | **One-sentence recourse pointer in §6.5** (blind-window vs post-observation recourse insufficiency) | trivial | **recommended** |
| D3 | **Companion paper** from the nonstandard package ("Finite Nonviability Certificates under Delayed Information," SCL-shaped) | new manuscript | **recommended as the next major project**, if you want to pursue it |
| D4 | Cover-letter sync to v20 (selector framework, summary table, Witsenhausen, finite-horizon completeness) | short | recommended before submission |
| D5 | Optional em-dash pass (145 remaining) | medium, stylistic only | user's call |
| D6 | Pivot to EMA / JEDC / EJC (broad rewrite) | large | only if you change the journal target — SVVA track needs none of it |

**Immediate recommendation:** apply D1 + D2 as a micro-revision (v21), do D4, and treat D3 as a separate manuscript decision. Say the word and I'll execute D1 + D2 (+ D4), or start scoping D3.
