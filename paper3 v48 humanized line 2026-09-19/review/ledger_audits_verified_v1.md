# The four audits in `uploads/ledger upgrade.txt` — joint evaluation and verification

**Date:** 2026-09-14 · **Objects reviewed:** the four documents concatenated in `ledger upgrade.txt` (98,760 chars, 1,342 lines), evaluated against `work/paper3.txt` (source of truth, 137,046 chars) and against my own `review/weaknesses_and_upgrades_v1.md` (19+ items) and `humanized/v1/` (the nine-part plain-language rendering). **No prose of the article was rewritten in this file.**

| Audit | Lines | Voice / form | Length |
|---|---|---|---|
| **A1** "The decisive upgrade: certify an actionable safety claim" | 1–720 | 9 numbered upgrades + revised thesis sentence | 45k chars |
| **A2** "Typed Depletion Ledgers v2 — an upgrade memo" | 721–980 | "where v1 stops" (8) → seven primitives → upgrades A–N → theorem set T1–T15 → pilots → attacks | 20k |
| **A3** "Proof-Carrying Sustainability Accounting" | 981–1204 | architectural compression → new mathematics T1–T10 → instruments → micro-example → falsifiers | 14k |
| **A4** "Profound Upgrades: … Self-Verifying Public Infrastructure" | 1205–1342 | numbered items 35–70 in seven groups | 8k |

---

## 0. The finding that frames everything else: **they are not auditing this article**

All four refer, in their opening moves, to objects the v32 article does not contain. Verified counts in the source text (case-insensitive):

| Object the audits treat as existing | in `paper3.txt` | verdict |
|---|---|---|
| "the existing **Claim Passport**" (A1 §1, A2 P4, A3 §4, A4 item 35) | **0** | not in the article |
| "**dashboard**" (A1 §8 "replace the enormous dashboard"; A2 "dashboards therefore get exactly one certified scalar") | **0** | not in the article |
| "**pilot**s" (A1 §9, A2 §4, A3 "3 pilots", A4 item 63) | **0** | the article has three *application classifications*, not pilots |
| "reference **architecture**", "the **engine**", "the compiler" (A1 §7) | **0** | not in the article |
| "**34 modules**" / "thirty-four modules, no generating core" (A2 §0.8) | **0** (module: 2 hits, both "physical module") | the article has no module inventory |
| "**type system** / **dependent type** / type algebra" (A2 §2A, A3 §1) | **0** | the article's "typed" = unit-and-identity discipline, §2.1 |
| "**identifiability**" (A1 §5, A2 §2E, A3 T6) | **0** | the article says "identification", "registered identification requirements", "does not by itself identify process noise" — the substance, not the term |
| "Farkas", "sum-of-squares", "Nyquist", "credal", "ratchet", "expiry", "additionality", "**78%** regenerative yield" (A1 §6, A3 §8) | **0** each | none of these appears; "78%" is **invented** (it is not one of the article's numbers) |
| "SEEA" (A2 §2N "position as a rigor layer on UN SEEA") | **0** | correct that the article is silent — and this is already item **N2** of my review |

What *is* in the article (counts): "certificate" 14 (the barrier-certificate corollary), "quarantine" 6, "registered" 23, "conditional" 13, "record-relative" 9, "non-example" 2, "banned" 1, "illustrative" 2, "polytope" (the box-vs-polytope line in §3.5), the min over both signs and all moieties in §6.3.

**Consequence.** A1, A2, A3 and A4 are a *design review of a larger project* (a standard/framework with a passport, an engine, pilots and a dashboard) that the author evidently also has. Read as advice for the article in hand, a large fraction of their content is (a) already implemented, or (b) addressed to software and institutions that do not yet exist in the manuscript. That is not a criticism of the audits — it is the reason their recommendations cannot be adopted indiscriminately in a v2 *of the paper*.

---

## 1. Method

1. **Object existence:** the table above, by `grep -o … | wc -l` against the source extraction.
2. **Verbatim-phrase checks:** 50 discipline strings tested in three files (source A / Gemini F / Qwen Q) — results in §4 below, because they also settle the state of the *baseline for v2*.
3. **Recomputed arithmetic:** every number the audits attribute to the paper or derive in an example (11 recomputations, all printed in §2).
4. **Independent derivation** of the four claims that are theses rather than numbers: A3 T2 (curvature), A2 T4 (half-space vs orthant), A3 T5 (frozen-control kernel inclusion), A4 item 40 (strictly monotone scalarization), plus A1 §2C's joint-risk charge and A2 §0.6's "laundering" charge against the paper's own definitions.
5. **Cross-audit agreement matrix** and **overlap with my own review**, so nothing is bought twice.

---

## 2. Verified mathematics — what I re-derived, and what it returned

| # | Audit claim | My check | Verdict |
|---|---|---|---|
| M1 | **A3 T2**: for $\dot u=-cu^p$, the curvature number $\kappa=u\ddot u/\dot u^2=p$, and $T^*=T_{\mathrm{frozen}}/(1-\kappa)$, with $T^*<\infty\iff\kappa<1$ | $\ddot u=c^2pu^{2p-1}$ ⇒ $\kappa=u\cdot c^2pu^{2p-1}/c^2u^{2p}=p$ ✓. $T=\int_0^{u_0}du/(cu^p)=u_0^{1-p}/(c(1-p))$ and $T_{\mathrm{frozen}}=u_0/(cu_0^p)=u_0^{1-p}/c$ ⇒ $T=T_{\mathrm{frozen}}/(1-p)$ ✓. For $p\ge1$ the integral diverges ✓ | **CORRECT, and it is the best single new result in all four audits.** It converts the paper's "different question" framing (§6.1) into a *known bias factor* |
| M2 | A3 micro-example: $u=40$ km³, $|\dotS|=1.6$ ⇒ frozen horizon 25 yr; $\kappa=+0.6$ ⇒ 62 yr; $\kappa=-0.4$ ⇒ 18 yr | 40/1.6 = **25** ✓; 25/(1−0.6) = **62.5** → "62" ✓; 25/1.4 = **17.86** → "18" ✓ | **Arithmetic reproduces exactly.** Caveat: $\kappa$ needs $\ddot S$; the article's own §6.5.1 says the anomaly series cannot supply even $\dot A$ physically — so it is admissible as theory, quarantined as applied rule |
| M3 | A3: "stock-proportional harvest (κ=1) … barrier-hitting time exceeds the frozen estimate by $\ln(S_0/b)/(1-b/S_0)$, ≈1.4× at 0.5, ≈2.6× at 0.1" | $\ln2/0.5=1.386$ ✓; $\ln10/0.9=2.558$ ✓ | **CORRECT** |
| M4 | **A2 T4**: $f$ certifies box safety iff $\{f\ge c\}\subseteq \mathcal B+\mathbb R^M_+$; for $M\ge2$ no half-space lies in a shifted orthant ⇒ no weighted sum certifies | The iff is the definition ✓. A non-trivial half-space contains whole lines; $B+\mathbb R^M_+$ contains no line ⇒ impossible for $M\ge2$; for $M=1$ a half-space *is* a shifted ray, so the $M\ge2$ hypothesis is genuinely needed ✓ | **CORRECT and a one-line simplification** of the paper's constructive proof — but *weaker in reach*: it proves global impossibility, whereas the paper's theorem is domain-relative and therefore also tells you *when* an aggregate is admissible. Adopt as a remark, not as a replacement |
| M5 | A2's Corollary (alarm/certificate asymmetry): with $w>0$, an aggregate **deficit** implies some component deficit | Contrapositive of $\forall m,b_m\ge0\Rightarrow w^{\top}b\ge0$ ✓ | **CORRECT.** And the paper is *compatible with it already*: it forbids *non-negative weightings as certificates*, not the min-functional. Note $\min_m b_m$ is a scalar that **does** certify — which is exactly why A1 §2A is right that "anti-scalar" is the wrong target |
| M6 | **A4 item 40**: for $n\ge2$ no *continuous strictly monotone* scalarization certifies | Take $x_i=B_i-\varepsilon$, $x_j$ large: strict monotonicity gives $f(x)>f(B)$ while $x$ violates ✓ | **CORRECT, and it generalizes the paper** (the paper's theorem covers $w\ge0$ linear weights only). Requires no new machinery — a two-line proof |
| M7 | **A3 T5** (Nyquist): $K^{\tau}\subseteq K^{0}$, monotone in $\tau$, $K^{\tau}\supseteq K^{0}\ominus\tau L$, hence $\tau\le \mathrm{dist}(x,\partial K^0)/L$ | Freezing controls removes admissible policies ⇒ kernel shrinks ✓ direction correct. If $\mathrm{dist}(x,\partial K^0)>\tau L$ then $x$ stays in $K^0$ through the freeze ⇒ $x\in K^\tau$ ✓ | **CORRECT modulo hypotheses** it does not state ($L$ must bound reachable-set displacement, not merely $\sup\|f\|$ along one trajectory; and $K^0$ needs regularity for the distance identity). The paper already says the quantitative thing in words — "both scales sit far above the institutional delays of the companion family" — so this is a formalization of an existing sentence |
| M8 | A3 T9 (non-detection): $n\gtrsim(\sqrt{12}\,z\sigma_{\mathrm{eff}}/|\beta|)^{2/3}$, $\sigma_{\mathrm{eff}}=\sigma\sqrt{(1+\rho)/(1-\rho)}$ | $\mathrm{Var}(\hat\beta)=12\sigma^2/(\Delta^2n^3)$ ⇒ $n\ge(12z^2\sigma^2/(\beta^2\Delta^2))^{1/3}=(\sqrt{12}z\sigma/(\beta\Delta))^{2/3}$ ✓ — the $2/3$ exponent is the $1/3$ applied to a squared ratio, and the AR(1) inflation factor is standard | **CORRECT as written, with $\Delta=1$ implicit.** The micro-example's "24 yr vs 12 yr record" is asserted, not derived from those symbols |
| M9 | A1 §2C: "each component has 95% probability" ≠ "all components jointly" | The paper never makes that inference: §6.4 defines the probabilistic class as $\Pr[\tau_{\mathrm{exit}}>T]\ge1-\varepsilon$ with $\tau_{\mathrm{exit}}=\min_m\{\tau_m^-,\tau_m^+\}$ — the joint event by construction | **MISDIAGNOSIS.** The paper is already right; at most it should *say* so in a sentence |
| M10 | A1 §2B: $\forall i\,\exists\pi_i\not\Rightarrow\exists\pi\,\forall i$ | True as a general warning; the paper's $K_{\mathrm{maint}}=\{x:\exists$ an admissible continuation satisfying **all** barriers$\}$ already puts $\exists$ outside the conjunction, and §2.4's empty-kernel mechanism is exactly the phenomenon | **ALREADY IMPLEMENTED**, missing only as a stated remark |
| M11 | A3 §1: "the **only** implication in the lattice is P7 ⇒ P4" | The paper's **Proposition 1** proves Layer 2 ⇒ Layer 1 (conservation ⇒ accounting consistency for the conserved quantities), and donor limitation is what yields positivity (Thms 10–11) | **WRONG AS STATED** — A3's own lattice contains two more implications the article has already proved |
| M12 | A4 item 41: "species/genomes: **mass balance does not apply**; extinction is an annihilation with no sink pool" | Atoms are not annihilated; the paper's Proposition (Depletion is compartmental) and §3.6 list "destruction of the relevant function" as one of four exhaustion mechanisms, with mass still conserved | **CONTRADICTS the physics the paper proves.** The useful content (functional loss ≠ mass loss) is already in the paper and is better stated there |
| M13 | A4 item 42: "$\eta$ = per-cycle retention ⇒ primary requirement $(1-\eta)T$, displacement factor $1/(1-\eta)$" | With per-cycle retention $\eta$ and throughput $T$, losses per cycle are $(1-\eta)T/\eta$ ⇒ primary input $(1-\eta)T/\eta$, not $(1-\eta)T$; $1/(1-\eta)$ is the multiplier only if $\eta$ is the *recycled share of throughput* | **INTERNALLY INCONSISTENT** (definition ≠ formula). Fixable by one sentence choosing the second definition |
| M14 | A2 T15: "corridor emptiness ⇒ the Farkas witness **names** which floors conflict with which barriers" | A Farkas certificate gives multipliers on the whole system; minimal conflict identification needs an irreducible infeasible subset (IIS/e-limited) | **OVERSTATED MECHANISM** — right product, wrong tool named |
| M15 | A2 T14: "delay bound $a\tau<1$ (P), $<2$ (PD)" | For $\dot x=-kx(t-\tau)$, stability iff $k\tau<\pi/2\approx1.57$; $a\tau<1$ is the usual P-only rule of thumb; I could not reproduce "<2 (PD)" from a standard criterion | **UNVERIFIED — needs a citation and a plant definition** |
| M16 | A1 §7's seven LP caveats; A2 §2A "coercions are morphisms with obligations" | Every caveat is correct (relaxation spuriousness, non-anticipativity, grid-vs-continuous, tolerance, one-sided conclusions). But the paper's §3.5 already states the two that matter for *this* article: box-vs-polytope, and "when the fluxes are state-dependent, the declared box must additionally be forward-invariant" | **CORRECT, MOSTLY ALREADY THERE** |
| M17 | A4 item 37: certified margin $B_{\mathrm{eff}}=B+m$, $m=\max[\text{drift}\cdot(\delta_{\mathrm{det}}+\delta_{\mathrm{act}})+z_\alpha\sigma\sqrt\delta+\text{irreversibility surcharge}+\text{ambiguity surcharge}]$ | The first two terms are stock units; "surcharge" terms have no units given ⇒ not a dimensionally closed expression as written | **RIGHT SHAPE, NOT YET WELL-FORMED.** The paper would demand a declared disturbance class before stating it, and §6.3's $K_{\mathrm{maint}}$ is the honest substitute |

---

## 3. Where the audits are right that *my* review was not (and vice versa)

**They catch something I did not list.** A1 §2A + A2 §2C + A4 item 40, taken together, hit a real imprecision in the paper's own words: "**Scalar summaries may rank and communicate; certification requires the vector**" (§1.1, §10.1). Strictly, $\min_m(S_m-B_m)$ is a scalar that certifies, and the paper's own conjunctive criterion *is* a min. The claim survives for *weightings* (that is what the theorem proves), but the slogan is falsifiable by a referee with one line. Addendum needed, not retraction. My `weaknesses_and_upgrades_v1.md` has no item for it → new item **N7** there when we next revise.

**They miss things I flag.** None of the four mentions: the abstract↔Lemma 3 direction mismatch (my E-list/D11, verified: the abstract says fluxes-from-stocks, the proof integrates fluxes to reconstruct readouts); the ε label on the resources row (E4); the five "in review" placeholders naming three works (E8); the pre-2026 vintage rows under a "2026 pinned source" (E6); zero figures and zero numbered tables (E1); no code or repository for a paper whose claims are computational (E7); the non-reproducibility of the 43-stock cohort by either public RAM release (that is §6.5.2's own disclosure, which A1/A2 quote selectively). **Coverage: the audits are v2 design reviews; mine is a submission-readiness review.** They are complementary, not competing — which is why §5 keeps them in separate buckets.

---

## 4. The state of the v2 baseline (`uploads/qwen's p3 rewrite.txt`)

Same verification method as I applied to the Gemini file. 49,853 chars · 7,127 words · 1,517 lines · markdown.

**Structure (genuinely good for your novelty-first rule):** it re-cuts the article into 11 sections and *moves non-compensation up* (§7) with the double-counting discipline attached to it, keeps §3 as the certification layer, and gives the applications their own section (§8) after the theory. It has no chat residue, no duplicated abstract, and a clean Declarations block.

**Fidelity (unacceptable as it stands):**

| Check | Result |
|---|---|
| Numeric tokens | **144 of the source's 186 dropped.** Of 32 numbers-of-record tested: **0 present** (no 89.526 / 397.87 / 2.090 / 4.652133 / 0.535; no 4.44 / 415 / 2.57 / 4.66 / 454 / 1.79; no ψ = 0.85/0.25/0.70/0.20; no 1,125 / 5,050 / 0.130; the whole G3P and phosphate tables gone) |
| Discipline phrases | **3 of 50 present** ("declared, not computed", "algebraic cancellation alone does not establish invariance", "not a member of the"). Missing: "Banned unless donor-limited", "must not be reused", "must not be taken at face value", "routing is never determined", "never determines physical destination", "42 of the 43", "archived pull", "leakage terms may not absorb", "inadmissible as certification", "permanent mathematics", "must not be inverted", "not a regular perturbation", "cancellation is cheap" (title phrase, 1 hit only in a different form), "not promoted to a forecast", "no cohort statistic is quoted", "nothing empirical about any named resource system", "not shown to be inverse Gaussian", "does not by itself identify process noise", "the scale must name its flux", "no basal mortality", … |
| Sections deleted outright | §2.4 four-stock/sink obstructions, **§2.5 mechanism typing** (the "routing is never determined by diagnostic labels" result — a *novel* item, not background), §2.6 support saturation (Thm 1/Rem 2, so its 12 "Theorem" hits are inherited), §4.7–4.9 (integrability is kept as 4.6 but the hybrid Theorem 15 and "cancellation is cheap" are gone), §6.4 robust semantics, §6.5.2 applied tables + quarantine note, §6.5.3–6.5.4 vintage and cohort disclosures, §7.7 seven non-claims, §7.8 uncertainty, §8 domain templates (all three), §10.3 negative content, **§10.4 limitations (i)–(viii)**, References, Supplementary pointer |
| Statement inventory | Definitions 6/15, Remarks 0/5, Non-examples 0/2, Corollary 1/2, proofs 19/29 |
| What it keeps | the abstract's own wording, the three-quantity taxonomy, Props 1/2/6, Thm 5 + worked envelope, Thms 7/8/10/12/13/14, the two no-certification results with proofs, the non-reduction theorem, record-relative discipline, the AI/competing-interest declarations, keywords |

**Bottom line for v2:** Qwen's file is a *compression*, not a humanization — it removes the paper's load-bearing honesty apparatus along with its background. Use it as the **frame** (section order, paragraph rhythm, sentence length: mean 21–25 w where the source is 32.7) and as ready-made background prose; restore every status-bearing sentence and every number of record from `work/paper3.txt`. My `humanized/v1/` already carries a verified rendering of all eleven sections, so it is the right donor for the restored material — that is the assembly rule I applied in `revision/v2/` (see its README).

---

## 5. Joint disposition — what v2 should take, and from whom

Bucket **T (take now; wording/framing only, no new mathematics):**

1. Restate the non-compensation result as **anti-compensatory, not anti-scalar** (A1 §2A + A2 §2C + A4 item 40): "no *compensating* weighting certifies; a non-compensatory map — the vector, or $\min_m$ with the binding component named — does." One sentence in §1.1, one in §10.1, one in §11.
2. **Alarm vs certificate asymmetry** (A2 T5-corollary): aggregates are valid alarms, invalid certificates. One clause; it *widens* the paper's coalition (it is what lets §6.5.2's Non-example 1 stay in the text as a communication device without apology).
3. **Add the word "identifiability"** where the paper already does the work (A1 §5, A2 §2E, A3 T6): §7.8 and §8.2 say the substance; naming it makes the discipline searchable and closes the referee's "so what is this actually preventing?" question. The anomaly-shift argument in A1 §5 (the $S\to S+a$, $c\to c+a$ invariance) is **sound and directly on point** for §6.5.1 — worth a two-line remark with the paper's own caveat that geometry × storage coefficient is the "absolute anchor".
4. **Distinguish loss of safety from loss of assurance** (A1 §5, last subsection): the paper's §10.3 ("negative and boundary content is first-class") is the natural home; it is one sentence and it answers the standard "your framework will be gamed by silence" attack.
5. **Antecedent humility, 4/4 unanimous** (A1 §9, A2 §3's "T1–T2, T11, T14 are imports", A4 item 38's "acknowledge the reconciliation lineage", and my N1/N2): state the delta against MFA data reconciliation, SEEA/green accounting, viability theory and composite-indicator literature in one paragraph. Highest-confidence adoption in the whole set.
6. **Joint-probability sentence** (A1 §2C): not because the paper is wrong (M9: it isn't) but because the *min* construction is easy to miss — add "the probability is already joint, because $\tau_{\mathrm{exit}}$ is a minimum over moieties and both barrier signs" to §6.4.

Bucket **P (needs new proofs → author decision, cannot be smuggled into a humanization):**

7. **A3 T2 curvature number** (M1–M3: verified correct, cheap: 4 lines of calculus + one worked example). Best value/effort in the whole audit set. Restrict to the power-law family and state the $\ddot S$ data requirement, or it collides with the paper's own §6.5.1.
8. **A4 item 40's generalization** (M6: correct, 2-line proof, and it upgrades the paper's theorem from linear weights to all continuous strictly monotone $f$). Its "false-safe volume" metric needs a declared measure — and without one, the paper's own "declared, not computed" rule forbids publishing it.
9. **A2 T4's one-line global proof** (M4) as a Remark, keeping the domain-relative theorem as the load-bearing version.
10. **A3 T5 review-interval bound** (M7) — belongs next to §9's institutional-delay sentence; needs the displacement-bound hypothesis stated.
11. **A1 §3 "intervention windows" instead of distance-to-kernel** — sound, but the paper never proposes distance-to-kernel (0 hits), so this is *new scope*, not a fix.

Bucket **R (reject for the article; keep in the project proposal):** everything addressed to the non-existent objects — passport fields, ratchet rules, certificate expiry and dependency management, the compiler/engine architecture, the one-page decision card and dashboard, pilots and their decision-performance metrics, the claim linter, the gold corpus, human-factors trials, "78% regenerative", the 2.8× / +38% / 14-yr figures in A3 §8 (illustrative at best; **not** to be reproduced as findings). And reject M11, M12, M13, M14-as-worded, M15, M17 as they stand.

**Conflict to settle before writing:** A2 §0.6 accuses v1 of letting "a GRACE anomaly get laundered into a '9.5 years' forecast". The paper's §6.5.1 says the opposite in terms ("a statistical anomaly index with units of time — not the physical stock ratio… not a forecast of aquifer exhaustion"), and §7.7 non-claim 5 forbids reading surrogate means as physical depletion. So the accusation is **false as an error report and true as a risk report**: the paper never launders it, but it never proves the impossibility either (M-identifiability is asserted, not derived). v2's fix is to add the one-line invariance remark (T3 above), not to accept the charge.

---

## 6. Corrections to my own earlier claims, forced by this pass

The verbatim-phrase audit (50 strings × 3 files) also tested quotes I had used in `review/joint_evaluation_v1.md`. Three of them are **my paraphrases, not the paper's words**, and I have corrected them there: "τ = min over all moieties m" (source has the display $\tau_{\mathrm{exit}}=\min_m\{\tau_m^-,\tau_m^+\}$; no such sentence), "the one-way valve" (source: "the positive-part convention $[\cdot]_+$, read as a one-way valve at a nonpositive target" — my short form was mine), "the eight zeros are a convention" (source: "the zero convention of the source table's caption, which the median includes"). Verified-present originals I kept: "already at minimum" (1), "42 of the 43" (1), "archived pull" (5), "row-by-row re-verification" (1), "transfer principle" (1), "must not be reused" (1), "declared, not computed" (1), "banned unless donor-limited" (1), "routing is never determined" (1).
