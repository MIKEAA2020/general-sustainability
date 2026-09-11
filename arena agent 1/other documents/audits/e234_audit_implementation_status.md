# E2/E3/E4 Joint-Audit Implementation Status and Residual Fixes (2026-09-11)

The owner supplied four attachments — `JOINT_AUDIT_EVALUATION.md` and `grok claude e2/e3/e4.txt`
(grok and claude line-level audits) — as the audits "left to be implemented," and reported
that `arena agent 1/paper rewrites` had been updated. This record reports what happened and
what was implemented this pass.

## 1. What happened: the chains had already implemented nearly the entire audit

The four attachments audit E2 at v14, E3 at v8, E4 at v9. The repo has since advanced through
eight or more waves per paper (pull of 2026-09-11: **E2 v22, E3 v16, E4 v14**, plus P1 v23,
P2 v13, P3 v32, P4 v30, P5 v26, E1 v15, newer supplementaries, and `E1_TIER3_RESTRUCTURING_PLAN.md`).
Line-level verification against the current versions shows the audit content is already
implemented, item by item:

**E2 v22** — scope-first abstract ("every statement scoped to that map"); the single-convention
(source-year) recompute adopted (SD 135→114.9, ε 460→329, constructive 57.6→**91.6 kt**, only
the perpetual-worst class vacuous, certified horizon T=7); retention replaced by a dominance
partial order with the no-dominance verdict; the vacuous-class identity demoted to a
definitional note; expansion stated as generic (F′>1 for every admissible K≥2K*, not a
pinned-K artifact); K=5000 flagged "a declared fit defect" with the 940.75-kt training maximum;
SSE/MSE labelling reconciled (MSE 12,772.2 / 7690.1 / 13,873.1 / 18,028 kt²); Table 1 gained
the harsh-class T=∞ columns; post-freeze layers tagged; companions cited; re-execution
verified byte-for-byte.

**E3 v16** — abstract rebuilt around the white-recharge mechanism (corr(R_t,R_{t−1})=0.17 vs
corr(ΔH_t,R_t)=0.74 in the abstract); M1 restated as a coin-flip retention (MAE tie, h=5 loss,
bootstrap interval covering zero); the M2m kink resolved against the frozen document (the
climate gate is persistence+M1; M2m margins kept as a nested-baseline reading; M2m's decline
recorded as a protocol choice outside Definition 4.2, with the deviation listed); the
nowcast/forecast/contemporaneous trio installed and the word "certificate" retired; a
post-freeze Diebold–Mariano + moving-block bootstrap uncertainty layer (Table 6) attaches
intervals to every load-bearing margin; the Comal tail claim corrected (the channel predicts
non-cessation; it never predicts cessation where cessation occurred); §5.6 corrected
(20%-cut path is the closest by 7.19 vs 8.56 ft, an artefact of the map running high — not
near-optimal pumpage; 5.2 not 5.1; the coefficient comparison now states "larger per unit but
acting on a range", γ flagged as simultaneity-contaminated, not a policy lever); M4 kept only
as a labelled symmetry control; M1's status settled (output-only in the protocol; the Darcy
reading restricted to discussion); companions cited.

**E4 v14** — the three-verdict structure (nominal at 618 ft under UC-min / nothing certified /
nothing at 660 ft) leads the abstract; the hybrid nature of the +3.3%/+0.4% margins stated in
the first results sentence and the Impact Statement; BAU relabelled training-mean pumping
(282.16 × 10³ acre-ft, "not the historical path and not current use") with the current-mean
baseline arithmetic added (382.16 → securing cut ≈31.5%, Stage I not securing); the comparator
table reports kernel-matched (flat-90%) AND attractor-twin (flat-80%/60%) AND 1%-grid AND
interpolated-7.2% margins; the 660-ft reading reframed as a design observation about scoring a
trigger against its own level (not a deficiency of the rules — the cascade's purpose is
springflow protection near 618 ft); kernel emptiness stated as ceiling-relative with Table 2
giving boundaries by horizon; the certified layer rewritten (affine intercept-only policies
make the contraction rate policy-independent, (F4) exact; the trigger-band mechanism for the
reactive collapse; the per-step tube K*+r_t noted as the tighter, correct form); the
out-of-sample defect (21.81 > 15.41) stated as making the certified bound optimistic; the
0.88-ft flat-90% clearance flagged as unresolved by the fit bootstrap; table numbering runs
1–7 without the earlier gap.

**Freeze dates.** The audits' "future-dated freeze" objections (2026-08-25/26) are moot as of
today (2026-09-11): those dates are now in the past, so the frozen-protocol claims are
auditable-in-principle past-dated statements. No edit made for this; noted for the venue pass.

## 2. Residual items found and implemented this pass

1. **E2 (grok §5 / claude A10 / joint (D)):** the xteNCAM specification disagreement was still
   confined to §3.11 as a "labelled sensitivity" — not in the abstract or conclusions.
   **E2 v23:** one abstract sentence and one conclusions sentence (added to finding (5)) state
   it: the two specifications agree on the expansion classification and the kernel ordering
   but disagree on the reference point's self-viability (the 2024 stock 342 kt between the
   one-year 309 kt and five-year 368 kt zero-catch boundaries). Wording mirrors §3.11 exactly;
   no number imported beyond what the section carries.
2. **E4 (claude A8):** "the registered twenty-column analysis panel" was undefined.
   **E4 v15:** the §2.1 object sentence now defines it as the companion forecast evaluation's
   fixed analysis dataset (measured head, constructed recharge and pumpage, and the service
   and derived series declared there), of which only the head, recharge, and pumpage columns
   enter this analysis.
3. **E3:** no residual found — every joint-consensus and line-level item verified as applied
   in v16 (including Definition 4.2's stated horizon, the Comal tail correction, the §5.6
   arithmetic, and the uncertainty layer).

## 3. The P5 screen-materials question ("do we have these files?")

Checked workspace and repo for the P5 spectral-screen materials named in the owner's excerpt
(RAM stock identifiers + eligibility table; processed spectral series and routines; AR(1)/null
calibration code + Monte Carlo seeds; power-simulation code + seeds; case-screening table +
query log). **None of them exist** in this workspace or anywhere in the repository — no
`*screen*`, `*spectral*`, `*eligib*`, or Lomb–Scargle implementation is present; the only P5
artifacts in the repo are the *paper-editing* scripts of other agents' waves
(`batch 7 …/apply_batch7_wave8_p5.py` etc.), which rewrite the manuscript, not the screen data.
The RAM material that does exist is the ADH cohort (`analysis/ram_adh_fisheries/`, pushed to
`other documents/analysis/`) — the fisheries table the screen's 42-stock selection draws on,
but not the screen's own code, stock-ID list, null-calibration, or query log. So the excerpt's
conclusion is confirmed from this side: the screen materials were never deposited by any
agent; the cheapest write-up that can still be supplied is the §3.7 case-screening table and
query log, which is a text record rather than code.

## 4. Files issued this pass

| New version | Built from | Changes |
|---|---|---|
| `paperE2_cod_intervention_v23.md` | v22 | xteNCAM specification disagreement promoted to abstract + conclusions (2 edits) |
| `paperE4_edwards_intervention_v15.md` | v14 | twenty-column analysis panel defined (1 edit) |

Local copies of `paper1_supplementary_v2.md`, `paper3_supplementary_v7.md`,
`paper4_supplementary_v4.md` were re-synced to the remote's newer content (the remote had
appended wave sections S6/S11 and notation renames) so that no push could clobber them.
