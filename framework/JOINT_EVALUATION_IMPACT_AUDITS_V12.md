# Joint Evaluation — Novelty/Impact Audits (V12) → verification + adjudication (2026-09-13)

Two audits received (`uploads/framework impact.txt`): **Qwen** (novelty assessment,
limitations 2a–2f, improvements 3.1–3.10) and **GPT** (highest-priority changes,
~23 items). Evaluated jointly against v25_restructured and the archives. Every
claim is verified (CONFIRMED / DUPLICATE / PARTIALLY / CONTRADICTS); every
contradiction is adjudicated before any implementation; the implementable
remainder is phased in the merged plan (venue V12).

## 1. Verification of audit claims against the paper and archives

| Audit item | Verification | Status |
|---|---|---|
| Qwen 2a — no template/checklist/schema/software exists | TRUE: the paper has the algorithm box and the Table 2b audit template, but no standalone spec, fillable checklist, certificate schema, or software | CONFIRMED |
| Qwen 2b — T=71 n=10; M3/M4 never truth; DGPs in-class + 2 amendments | TRUE and disclosed ("10 replicates per cell"; "M3 and M4 were never simulated as generating truth") | CONFIRMED (already disclosed; O4/O5 registered) |
| Qwen 2c — IC dominates 0.509/0.992 vs 0.373/0.973; one-step only | TRUE (archived §6.5 row; the IC is one-step; h=5 IC never computed) | CONFIRMED |
| Qwen 2e — calibration executed for cod only; Edwards deferred | TRUE (Phase K: cod frontier, 5% retained; Edwards draft sheet) | CONFIRMED |
| Qwen 2d/2f — two domains thin; density | TRUE; §9 discloses the domain limit; main text ~10.7k words + supplement | CONFIRMED |
| Qwen 3.6 — MCS mentioned in one sentence only | TRUE ("a model confidence set never eliminates persistence…", §6.5) | CONFIRMED |
| GPT 1 — standard vs worked rule conflated | PARTIALLY FALSE: §1 already states "the rule is the worked example; the standard is the deliverable" and the one-page standard separates the three layers | DUPLICATE (remainder: a required-fields list → folded into O18) |
| GPT 2 — tension between prediction-license and M2m decline | REAL tension worth one clarifying sentence; the two-axis taxonomy is new | PARTIALLY / proposal |
| GPT 5 — "silently retain 5%" when no band qualifies | NOT silent: §8 reports the frontier and the 5% fallback; Phase K executed it | COUNTER-VERIFIED (fallback is disclosed, not silent) |
| GPT 8 — "domain-free" overstatement | §1 has "portable and domain-free" once (about the obligations); §9 already limits the demonstration to two domains | PARTIALLY (one wording fix) |
| GPT 8 — "same rule unchanged" without the rule-version disclosure | ALREADY DONE (v22, NEW-4a): §4 states the companion's h=1 point rule retained M1, the unified rule withholds it, "a recorded rule-version difference, not a data difference" | DUPLICATE (only the abstract lacks the parenthetical) |
| GPT 8 — DM results consume space without strengthening | TRUE; already labelled "descriptive", verdicts "do not rest on DM statistics"; moving them to the supplement = O16 territory | PARTIALLY covered |
| GPT 4.3 — should say "proposed" standard | ALREADY: the abstract says the article "proposes one and demonstrates it" | DUPLICATE (title tweak only, owner-gated) |
| Both — IC hybrid on the existing archive | FEASIBLE NOW: the pinned-seed archive carries per-replicate per-module h=1 AND h=5 RMSEs (sim_retention_power_20260913.csv) — IC at h=5, multi-horizon penalised criteria, and IC+gates hybrids computable without any refitting | CONFIRMED feasible |
| GPT 2.2 — Monte Carlo uncertainty missing | TRUE: rates are point estimates; exact counts + binomial (Wilson) intervals computable from the archive | CONFIRMED |
| GPT 2.4 — identification decomposition | Components exist in the archive (truth-best rates, conditional gate removal shares) — the formal decomposition is computable | CONFIRMED feasible |
| GPT 6 — abstract too detailed | TRUE (full-findings abstract is a lineage design choice; no audit ever adjudicated shrinking it) | CONFIRMED (owner-gated) |
| Qwen/GPT — M3/M4, T=71 200 reps, further compression | Already O4/O5/O16 (owner-excluded by directive 2026-09-13) | DUPLICATE of registered items |

## 2. Adjudications (contradictions resolved BEFORE implementation)

| ID | Conflict | Adjudication |
|---|---|---|
| NEW-10 | GPT 5: replace the 5% band with a decision/calibration-based margin now, vs AD4 (owner) + executed Phase K (band calibration is the prospective replacement; 5% frozen for reported verdicts; the §8 fallback reports the frontier — not silent) | AD4 binds — no band change. Adopted instead: the epistemic-consequence sentence ("non-retention is descriptive rather than evidential for the affected classes") sharpened in §6.4/§8, and the decision-based margin recorded in §8 as an admissible alternative basis. → O29 |
| NEW-11 | GPT 2: replace the three-way output with a two-axis taxonomy, vs the frozen pre-registered output vocabulary {retained, not retained, declined on class grounds} (AD2 precedent) | Output labels frozen. The two-axis taxonomy enters as a reading guide (predictive result × structural interpretation), exactly as "Row measures" did in Phase B; one clarifying sentence states that the M2m decline is a ladder-membership verdict and its predictive margin remains reported (Table 5). → O27 |
| NEW-12 | GPT 2.1: remove M3/M4 from the ladder, vs the frozen ladder (pre-registered; Amendment discipline) | Rejected — ladder frozen. M3/M4-as-truth remains O4 (owner-excluded). |
| NEW-13 | Qwen 3.2: formalise class-grounds with a quantitative criterion, vs the pre-registration ("substantive, declared with reasons, not a threshold") | Reported verdicts keep the declared judgement. A quantitative criterion may be proposed prospectively (like the band); do not retrofit. → O19 |
| NEW-14 | GPT 4.1: tiered requirements, vs the paper's mandatory-OC component | Consistent, not conflicting: tiers are an adoption ladder, and the evidential tier is exactly the paper's own "minimum accompanying evidence" stance. Adopted as a §9 guidance paragraph. → O33 |
| NEW-15 | GPT 5/6 + Qwen 3.8: split further / compress abstract, vs the Phase J owner decision (structure done; further compression = O16) | Phase J stands. Abstract compression (O36) and further supplement movement remain owner-gated/O16. |
| NEW-16 | GPT 8: rename "power" to "selection sensitivity" | Rejected — "power" is explicitly defined in §6.1 (true-class retention rate, adequacy thresholds); a rename would churn frozen language. Three-quantity terminology sentence adopted instead. → O39 |
| NEW-17 | GPT 8: DM rows to supplement | Remainder of O16 (owner-excluded); the descriptive label and non-verdict status already in place. No action now. |

## 3. Merged open items (O18–O39) and phases

- **Phase L — text + specification artifacts (feasible now):** O18 standalone two-page specification + checklist (both audits' #1 practical item); O22 register the third-domain requirements prospectively (§8, text); O24 negative-certificate scoping — N0–N3 claim-strength taxonomy + expiry/invalidation conditions (both audits); O25 decision-context paragraph per domain; O27 two-axis reading guide + M2m clarifying sentence; O29 §6.4/§8 epistemic-consequence sentence + decision-based margin option; O33 tiered adoption guidance; O37 "domain-free" moderation; O38 abstract "worked unchanged" parenthetical; O39 three-quantity terminology sentence.
- **Phase M — archive computations (feasible now, zero new simulation):** O20 IC instruments on the existing archive (IC at h=5; multi-horizon penalised criterion; IC ranking + rule gates hybrid — both audits' #1 technical item); O30 exact counts + binomial (Wilson) intervals for every published rate; O32 formal identification decomposition P(retain) = P(rank 1) × P(baseline|rank 1) × P(gates|…) from the archived components.
- **Phase N — reference artifacts (feasible now):** O26 minimal reproduction package (one script: archived data → rule → gate decomposition + 20 D1/D5 replicates); O28 reference implementation of the gates + YAML certificate schema.
- **Phase O — literature positioning (citations verified at edit time):** O23 paragraph + comparison table (White 2000; Hansen 2005; Hansen–Lunde–Nason 2011; Giacomini–White 2006; Clark–West 2007; equivalence/non-inferiority testing; multiple-testing control).
- **Owner-gated / event / excluded:** O19 (class-grounds criterion, prospective only); O21/O31 (new DGPs: threshold/regime/non-stationary); O34 (independent third-party application); O35 ("proposed" in the title); O36 (abstract compression); O4/O5/O16 (as before).

## 4. Bottom line (joint)

Both audits converge on the same three highest-leverage actions, all feasible
without contradicting any owner decision or frozen element: **the standalone
specification (O18), the IC-hybrid comparison on the existing archive (O20), and
the certificate/claim-strength formalization (O24)**. Everything the audits ask
that would change a reported verdict, a frozen label, or the executed band
calibration was adjudicated against the pre-registration and rejected or
redirected to the prospective channel — the standard's own discipline, applied
to its critics.
