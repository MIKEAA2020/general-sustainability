# `revision/v4` — what changed from v3, and why

**Deliverable:** `revision/v4/paper3_v4.md` — 108,043 characters / 15,016 words (v3: 103,963 / 14,438).
**Built by:** `python3 revision/v4/build_v4.py`, which reads `revision/v3/paper3_v3.md` (untouched) and applies 9 anchor-guarded restorations (9 applied, 0 skipped).
**Checked by:** `python3 revision/v4/verify_v4.py revision/v4/paper3_v4.md` → **34 invariant checks, 0 failed**. v3 re-checked: `revision/v3/verify_v3.py` → 30 checks, 0 failed.
**Trigger:** `uploads/qwen p3 upgrade2.txt`, evaluated in `review/upgrade2_verified_v1.md`. Its mentions of `thermodynamic admissibility`, `recoverability` and the double-counting audit vocabulary led to greps against `work/paper3.txt` that found nine source passages v3 had dropped; all nine are restored verbatim-modulo-cross-reference here. Nothing new was invented for this version.

## The nine restorations

| # | Where | Content | Why it matters |
|---|---|---|---|
| 1 | §1.1 | MFA lineage (Brunner & Rechberger, Eurostat, Fischer-Kowalski; Feinberg sign pattern) and the **four-predicate** sentence: bookkeeping balance, stoichiometric conservation, thermodynamic admissibility, sustainability safety, with the three failure illustrations and "the literature routinely slides between them" | the article's typing claim, and the antecedent-humility lineage the audits asked for (bucket T5) |
| 2 | §1.2 | overlapping readings (natural capital / stock / flow of services); every pool regenerative on some timescale; recoverable **only insofar as** renewal outruns use, else still liquidation | the recoverability headline, v3 carried 1 of the source's 8 `recoverab` sentences, now 6 |
| 3 | §1.3 | Daly's rate condition (neither consumption nor population grows faster than the productivity that supports them; not recoverable only on a longer timescale) + Definition 5 as the horizon object | ties weak/strong regimes to a rate test rather than a stock test |
| 4 | §1.5 | `**What is not claimed.**` block — no stochastic completion, no thermodynamic admissibility, no identification of the two-pool hypothesis (registered in §8.1, not discharged), no empirical finding beyond the descriptive status of tabulated indicators | the four negations the starting point deleted; `thermodynamic` 0 → 4 |
| 5 | §3.3, Prop 2 | thermodynamic admissibility implies accounting consistency, converse fails; article establishes the three layers without claiming the fourth | makes the predicate lattice complete and non-cherry-picked |
| 6 | §3.3, proof | mass-balanced decompositions need not satisfy energy/entropy constraints; establishing them needs structure outside the scope | the proof of #5, restored so the statement is not bare |
| 7 | §3.6 | the envelope as interval-arithmetic counterpart of MFA **data reconciliation**: reconciliation solves unmeasured fluxes under an imposed balance, the envelope bounds them without solving them | answers "so what does this prevent?" by naming the practice it generalises |
| 8 | §6.3 | two disciplines attaching to exit times: equality at the hitting time needs continuity of `S_m` and `B_m` (jumps can cross without equality), and the five-way lower-barrier taxonomy with "the term exhaustion is reserved for `S_m=0`" | the taxonomy that §3.7's "every exhaustion statement must name its referent" depends on |
| 9 | §8.1 | an anomaly-built index cannot separate recharge-timescale-recoverable drawdown from unrecoverable — and over-extraction can make the loss permanent through compaction, subsidence or saline intrusion, "in which case it is not recoverable at all" | the permanence clause; also the sentence a reviewer would test against the groundwater literature |

## Not taken from upgrade2 (see the review for the full list and the counts)

The twelve project objects (passport, engine, dashboards, pilots, registries, metrology, shadow ledger, corridor, observation assimilation, formal-proof artefacts, minimum viable ledger, audit product); the maintainability *distance/horizon* (a compensatory scalar that §7 forbids as a certificate — the min margin with the binding component named is the admissible form); the *liquidation fraction* as a replacement for the article's directional support gap vector; the status label `certified`; and the seven invented figures in its report-format examples (0.32 · median 17 yr · 9–31 yr · 12 yr · "longer than 3 years" · "2.9 years" as a pressure-scale example · 2040/2035 barrier-crossing dates). Its header correction 1 ("no prevalence claims") and 2 ("no negation-shaped content") are declined: the standing rule is that nothing is subtracted or softened, and the non-claim apparatus is load-bearing.

## Still open (author decisions)

1. One SEEA / 2025 SNA lineage sentence.
2. Bucket P mathematics, if wanted: curvature number κ (verified correct in the audits, 4 lines), the strictly-monotone generalisation of the non-compensation theorem (2 lines), the half-space one-liner as a Remark, the review-interval bound with its displacement hypothesis stated.
3. Citation format of the companion ("in review" vs the three Zenodo records) and `.bib` regeneration at LaTeX time.
