# `uploads/qwen p3 upgrade2.txt` — verified evaluation against the four `ledger upgrade.txt` audits

**Date:** 2026-09-15 · **Object:** `qwen p3 upgrade2.txt` (34,189 bytes · 4,615 words · 1,355 lines): three header "corrections", 27 numbered items in four Pillars, a priority ranking, a language-convention table, a 12-clause "should not do" list, a revised novelty narrative, a final recommendation.
**Judged against:** `work/paper3.txt` (source of record, 137,046 characters) and the two manuscript versions now in the workspace — `revision/v3/paper3_v3.md` and `revision/v4/paper3_v4.md` — and against the dispositions recorded in `review/ledger_audits_verified_v1.md` (buckets T / P / R) and `review/starting_point_audits_verified_v1.md`.
**All counts below are greps I ran this turn on those four files** (case-insensitive; `A` = source of record).

---

## 0. Verdict

The file is a **programme document for the infrastructure project, not a repair list for the article**. That is not a defect — it is a category fact that decides how to use it. Of its 27 items: **none** is a needed mathematical repair; **12** are addressed to objects the article does not contain (verified, counts in `A`): `passport` 0, `dashboard` 0, `pilot` 0, `engine` 0, `monitoring` 0, `shadow price` 0, `stranded` 0, `greenwash/water-neutral` 0, proof assistants 0, `curvature` 0, `SEEA` 0, `identifiab*` 0; **8** restate what the manuscript already proves; **4** would subtract or soften claims; and the **four cheap genuine upgrades the four audits verified (bucket P) are absent from it** — no curvature number, no strictly-monotone generalisation of the non-compensation theorem, no half-space one-liner, no review-interval bound with its displacement hypothesis.

What it did accomplish, and at no cost to fidelity: its own mentions of `thermodynamic admissibility`, `recoverability` and the audit vocabulary led me back to nine passages that the starting point had dropped and I had not caught. Those are now restored in `revision/v4/` (§5 below).

---

## 1. Attribution audit — every "the latest rewrite defines/states X" it makes

| upgrade2 item | What it attributes | Verified basis | Verdict |
|---|---|---|---|
| 1 (Passport) | eight-predicate list: accounting consistency, conservation consistency, barrier safety, gross turnover intensity, frozen-rate ratio, scenario-conditioning, pressure scale, statistical index | all eight strings occur in the manuscript (Definitions 1–5, §6.1, §8.1–8.3) | **accurate**, though it is a *reporting* list, not the article's predicate lattice (which is Prop 1, Prop 2, Thm 5) |
| 2 (Engine) | "the five double-counting rules from the paper" | §7.3 enumerates exactly five rules (One balance per moiety · Explicit stoichiometry · Yield routing · No ghost sinks · Classification labels stay out of the columns) | **accurate count**; "ghost sink" `A:2`, "phantom" `A:2` |
| 2 (Engine) | LP/convex certificate `min/max S_m(t)` over the admissible flux polytope | the manuscript already states it: "the tight certificate is the linear programme over that polytope, and the box envelope above is its auditing relaxation — the box is what is audited, the polytope what is realizable" (§3.6) | **already in the article**; the item is the software, not the theorem |
| 3 (Maintainability) | `K_maint = {x : ∃ an admissible continuation satisfying all barriers for t ≥ T}` | character-for-character match with §6.3, including "This is the viability kernel of the barrier set under the admissible controls" (`viability` A:5) | **accurate quotation** |
| 3 (proposed diagnostic) | "maintainability **distance**"; "distance to maintainability boundary under declared controls"; "maintainability horizon" | `maintainability horizon|distance` A:0 · v3:0 · v4:0 | **new object**, and its top-ranked upgrade is *formally exposed*: a boundary distance is a compensatory scalar over the state, which the article's Theorem (Universal failure of weighted certification) and the min-margin verdict (§7.2) forbid as a certificate. Admissible only as the min margin over moieties reported with the name of the binding component — the article's own repair, which this file does not invoke |
| 4 (Support provenance) | `\(\alpha_{\text{reg}}(\bar s;x,t)=\sup\{\alpha\in[0,1]:\alpha\bar s\in\Gamma_{\text{reg}}(x,t)\}\)` | exact match with §5.3 (`Γ_reg` A:6 in unicode form) | **accurate**; the "liquidation fraction 1−α_reg" is the article's own "directional support gap" renamed — a labelling change, and it loses the `(1−α_reg)s̄` vector form for a scalar, so it must not be adopted as written |
| 5 (Observation assimilation) | "the latest rewrite correctly separates declared stochastic surrogates from the deterministic ledger" | §9.2/§9.7 non-claims; "no stochastic completion" (`A` has the sentence in §1.2's non-claim block) | **accurate** |
| 8 / 9 / 10 | the three application classifications, quoted exactly ("a statistical anomaly index with units of time", "arithmetic on an economic classification", "a pressure scale") | verbatim in §8.1–8.3 | **accurate** |
| 10 (Tier 2) | `H_B^loc=(B−B_lim)/[−Ḃ]_+` with the reported "Pressure scale: **2.9 years**" | the article's `H_A^loc` is defined on the active pool; 2.9 is *the median of the 35-stock qualifying sub-cohort* (§8.4), not a per-stock pressure-scale example | **misattribution of a number of record** — see §2 |
| 12 | `T_A(x_0;\pi,d)=\inf\{t\ge0:A_{\pi,d}(t;x_0)\le A_{\min}\}`; fourfold robust classes (nominal · worst-case · probabilistic · scenario-conditioned); "no number promoted across classes without a declared map" | exact match with Definition 5 and §6.4, including `worst-case` A:1 and `Pr[τ_exit>T]≥1−ε` | **accurate**, but it drops the article's `T_A=+∞` convention and its `τ_exit = min_m{τ_m^-,τ_m^+}` joint-min construction |
| 13 (Barrier protocol) | barrier types: physical exhaustion · functional failure · resilience threshold · economic accessibility floor · service-supporting minimum · sink ceiling · equity floor | the article's enumeration is five: physical exhaustion `S_m=0`, functional failure `S_m=B^func_m`, a resilience or regime-shift threshold, an economically recoverable reserve, a minimum service-supporting stock — **and it was missing from v3** | **partly new** (sink ceiling, equity floor are new); fixed in v4 by restoring the article's own taxonomy plus "the term exhaustion is reserved for `S_m=0`" |
| 15 (Financial shadow ledger) | "prices and demand do not appear in the six right-hand sides" | §10.1 carries the specialization clause; `shadow price` A:0, `stranded` A:0 | the *principle* is the article's; the five readouts are new instruments with no proof behind them |
| 16 (Control interface) | "the exact shared object `qEN−R=−Ṅ`" and `\(\Lambda(t)=[-\dot N]_+\)` | both present (v3: `qEN-R=-\dot N` 2 hits, `\Lambda(t)` 3) | **accurate**; its "review interval longer than 3 years increases the probability…" is invented (§2) |
| 17 (Corridors) | "the latest rewrite defines service balances `b_i(t)=s_i(t)−d_i(t)`" and `\(\mathcal C(t)=\{x:\underline B_m(t)\le C_m x\le\overline B_m(t),\ s_i\ge d_i\}\)` | the `b_i` identity is verbatim from §5.1–5.2; the corridor set is **new** (`equity|justice|safe-and-just` A:0) | first half **accurate**; second half new scope, needing a proof and a source for the floors |
| 21 | "Turn the paper's double-counting discipline into a named audit product" — phantom-mass/ghost-sink checks | the eight listed checks restate §7.3 rules (i)–(v) plus "impossible backward recharge" (Theorem 11 donor limitation) and "diagnostic labels rerouting mass" (§2.5 typing) | **faithful restatement**; the product is project work |
| 26 | componentwise alternative to scalar overshoot dates | §7.2's verdict (min margin with binding component) + §8.4 Non-example 1 | already the article's position; the item adds no argument |
| Narrative | "Each indicator carries the question it answers, the assumptions it requires, and the certificate it can support" | matches §1.4/§6.1 | accurate; the second narrative sentence ("claim passports, certification engines, … governance dashboards") describes objects that exist only in this file |

**Novelty claim checked:** its "Revised Novelty Narrative" first paragraph reproduces the article's own claims faithfully (typed stock–flow layer, conservation from incidence structure, positivity from donor limitation, services as readouts, predicate separation) and keeps the slogan "Scalar summaries may rank and communicate; certification requires the vector." The second paragraph, beginning "This work extends typed sustainability accounting … to auditable decision infrastructure", would claim six artefacts the article does not contain. **Do not adopt the second paragraph.**

---

## 2. Numbers it puts in report-format examples (fidelity hazard)

Its tables are formatted like the article's applied records, which is exactly how figures get laundered. Checked against `A`:

| figure in upgrade2 | status |
|---|---|
| `Anomaly persistence index: 9.5 years` | **genuine** — Central Valley, §8.1 (window 2002-04–2023-09) |
| `Reserve-life ratio: 309 years` | **genuine** — §8.2, USGS MCS 2026 vintage |
| `Pressure scale: 2.9 years` | **misattributed**: 2.9 is the median of the qualifying positive 35-stock sub-cohort, not one stock's pressure scale; the cohort median is 1.8 over 43 |
| `Probability of crossing barrier B by 2040: 0.32 · median 17 years · 90% interval 9–31` | **invented** — no such posterior exists in the article or the source |
| `the system remains inside the maintainability kernel for 12 years` | **invented** (language-discipline example) |
| `a review interval longer than 3 years increases the probability of leaving the maintainability kernel above the declared threshold` | **invented**, and it contradicts the article's registered scale ordering (τ₊≈150 yr frozen-donor cycle; the companion's delay family sits far below `G₀/c≈2×10⁶ yr`) |
| `An index built on it therefore cannot distinguish…` quoted in its item 8 | genuine, and now restored in v4 |

Note the improvement over the earlier audit set: **no "78% regenerative yield", no 2.8× / +38% / 14-yr figures** — the fabrications I recorded in `review/ledger_audits_verified_v1.md` (M2, bucket R) are not reproduced here. Nothing in this file may be quoted into the manuscript as a result; only the two genuine figures above are numbers of record.

---

## 3. Its three header "corrections", assessed against itself and against the article

1. **"No unsupported prevalence claims."** The file complies: its 3 occurrences of `routinely|typically|often` sit in the *Avoid* column of its own language table. But applied to the article it deletes a claim the author made and supported: `A` has "…are four different predicates, and the literature **routinely** slides between them" (1 hit), and the composite-indicator/weak-comparability lineage it rests on is cited (`composite indicator` A:2, Munda & Nardo, Neumayer, Martinez-Alier). **Declined for the manuscript** under the standing rule that nothing is subtracted or softened; v4 restores the sentence as written.
2. **"No apologetic meta-commentary … states what the framework does rather than repeatedly saying what it is not."** Not self-applied: the file itself carries a 12-clause "should not do" list and a passport field-group of four `does not establish …` entries. And it collides with the article's structure, where the negations *are* results (§10.3 "Negative and boundary content is first-class", the seven non-claims of §9.7, the non-reduction theorem). I applied the **opposite**: v4 adds back the source's `**What is not claimed.**` block in §1.5. This correction is declined as a manuscript rule.
3. **"Preservation of the paper's scope discipline."** True, and verifiable in all four parts: barriers declared (5 mentions in-file), surrogates not completions, closed ledger not reducible to the open working system, templates registered not established ("registered open gap; not established" in its item 8 report format). This is the one correction that both describes the article and survives adoption.

---

## 4. Coverage against the four audits' live buckets

| Bucket item (from `review/ledger_audits_verified_v1.md`) | in upgrade2? | state in the manuscript |
|---|---|---|
| T1 anti-compensatory, not anti-scalar | partly (item 14 "avoid one sustainability score") | **applied** in v3 §1.1/§7.2/§11 with the min-margin exception |
| T2 alarm vs certificate asymmetry | yes, in vocabulary ("communication-only aggregate") | **applied** (v3 §7.2, §8.4 Non-example 1) |
| T3 name "identifiability" | **no** (`identifiab` 0 hits) | v3/v4 already carry the substance *and* the word in one place (A has 0 for both — the term is ours, not the source's) |
| T4 loss of safety vs loss of assurance | **no** (`assurance` 0) | **applied** in v3 §10.3; `A:0` — this is a genuine addition the audits supplied |
| T5 antecedent humility (MFA reconciliation · SEEA · viability · composite indicators) | **no** (`reconcil` 0, `SEEA` 0, `viability` 0, `composite` 0) | **partly applied now**: the Brunner–Rechberger reconciliation counterpart restored in v4 §3.6; `viability` 3, `composite indicator` 3 in the manuscript; **still open** — no SEEA sentence (facts verified this session: SEEA Central Framework adopted 2012; revision drafting 2026–27, adoption slated March 2028; §3.37–38 rests physical supply-and-use tables on conservation of mass and energy) |
| T6 joint-probability sentence | **no** | **applied** in v3 §6.4 |
| P7 curvature number κ (M1–M3, verified correct) | **no** | not applied — new mathematics, author decision |
| P8 strictly-monotone generalisation (A4 item 40) | **no** | not applied — author decision; it would *strengthen* the §7 theorem and is 2 lines |
| P9 half-space one-liner as a Remark | **no** | not applied |
| P10 review-interval bound with displacement hypothesis | gestured at ("review-interval stability margin") with **no bound stated** | not applied |
| P11 intervention windows instead of distance-to-kernel | yes, as item 18's map + item 3's distance | map = project work; the **distance** variant is what the article forbids as a certificate |
| R (reject: passports, engines, dashboards, pilots, expiry, ratchets, 78%) | this file is largely *that* material | unchanged — belongs in a proposal, not a paper |

---

## 5. What this file changed in the manuscript (v4), verified before and after

Nine restorations, each copied from `work/paper3.txt` and anchored by unique string (9 applied, 0 skipped; `python3 revision/v4/verify_v4.py` → 34 checks, 0 failed; v3 re-verified 30 checks, 0 failed):

| # | Where | Restored | `A` → v3 → v4 |
|---|---|---|---|
| 1 | §1.1 | MFA/Feinberg lineage + "Bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, and sustainability safety are **four different predicates**… a mass-balanced ledger can be chemically impossible…" | `four different predicates` 1 → 0 → 1 |
| 2 | §1.2 | "Every such pool is regenerative on some timescale… overlapping readings of the same pool… recoverable **only insofar as** the pool regenerates faster than it is taken; otherwise it is still liquidation" | `recoverab` 8 → 1 → 6 |
| 3 | §1.3 | the Daly rate condition — "neither consumption nor population grows faster than the productivity that supports them, and the drawdown must not be recoverable only on a timescale longer than it is taken" | — |
| 4 | §1.5 | `**What is not claimed.**` block (no stochastic completion · no thermodynamic admissibility · no identification of the two-pool hypothesis, "registered in Section 8.1, not discharged" · no empirical finding beyond the descriptive status) | `thermodynamic` 5 → 0 → 4 |
| 5 | §3.3 Prop 2 | "Thermodynamic admissibility — energy conservation, entropy-production non-negativity, reaction feasibility — implies accounting consistency, but the converse does not hold…" | new in v4 |
| 6 | §3.3 proof | "presupposes a mass balance, but a mass-balanced flux decomposition need not satisfy energy or entropy constraints…" (QED marks still 24, none duplicated) | new in v4 |
| 7 | §3.6 | "the interval-arithmetic counterpart … of the **data-reconciliation practice of material flow analysis** (Brunner and Rechberger, 2004)" | `reconcil` 2 → 0 → 2 |
| 8 | §6.3 | two disciplines that attach to exit times: equality-at-hitting-time needs continuity of `S_m` and `B_m`; the five-way threshold taxonomy (physical exhaustion · functional failure · regime-shift · economically recoverable reserve · minimum service-supporting stock) with "the term exhaustion is reserved for `S_m=0`" | `regime-shift` 1 → 0 → 1 |
| 9 | §8.1 | "cannot distinguish a drawdown … recoverable on the recharge timescale from one that is not — although heavy over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, in which case it is **not recoverable at all**" | `recoverab` (see #2) |

Sizes: v4 = 108,043 characters / 15,016 words (v3 = 103,963 / 14,438).

---

## 6. Declined for the manuscript, with the reason in each case

* Items 1, 2, 5, 8, 9, 10, 11, 13, 14, 19, 20, 21, 22, 23, 24, 25, 26, 27 as **objects**: passports, engines, dashboards, pilots, registries, metrology, debt vocabulary, shadow ledgers, corridors, observation assimilation, formal-proof artefacts, minimum viable ledger. They are artefacts, not claims; the article's rule is "recorded obligations, not results". Keep them in the project proposal; nothing about the article's truth-content changes by writing them here.
* Item 3's **maintainability distance/horizon**: admissible only as the min margin over moieties with the binding component named; as a distance it is the compensatory scalar the §7 theorem forbids. Not added.
* Item 4's **liquidation fraction** as a scalar: would replace the article's vector `(1−α_reg)s̄`; declined as a substitution, acceptable as an *additional* reported summary only if the vector is retained.
* Item 1's status vocabulary `certified / descriptive / conditional / record-relative / quarantined`: `certified` as an item-level label is not the article's status system (`certificate` A:14, `certified` A:0); certification is a componentwise, vector-valued property. Declined.
* The **seven invented figures** in §2 above: declined absolutely; two of them (0.32, "3 years") would also contradict registered scale statements.
* Header **corrections 1 and 2**: declined as rules for the article (they subtract claims and delete the non-claim apparatus).

## 7. Still open, author decisions

1. **SEEA / split-asset lineage** — one sentence in §1.1 or §2.1; the article currently cites Munda & Nardo, Neumayer, Daly, Ayres-lineage and Brunner & Rechberger but no standard.
2. **Curvature number κ** (P7) — four lines of calculus plus one worked example; would need the `\ddot S` data requirement stated, or it collides with §8.1's identifiability clause.
3. **Strictly-monotone generalisation** (P8) — two lines, upgrades §7 from linear weights to all continuous strictly monotone maps.
4. Whether to cite the 2025 SNA's adoption of SEEA's depletion treatment as a precedent for the ledger's "depletion as a cost" framing (verified this session; would be the strongest external anchor for §1.1).
