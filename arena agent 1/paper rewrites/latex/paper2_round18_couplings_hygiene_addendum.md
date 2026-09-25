# Round 18 — Envelope Couplings, Dedup Pass, Table Hygiene (with a correction on record)

**Date:** 2026-09-26. **Base:** `6e2e607` (round 17 final). **Scope:** the three actionable open items of roadmap v36; item 4 (venue submission) remains an owner action.

## Item 1 — The review-sequence envelope: exact couplings (minimax v3)

New final section in the corrected-envelope paper, fully certified (**20/20** checks; chains v2's 24, which chain v1's static 8):

**Instance** (two windows, one hidden branch): branch s ∈ {+1,−1}, z₀ = 2, controls u ∈ {−2,0,2} per review, adversarial disturbances d ∈ {−1,1} under the product prior, review observes z₁ exactly; safety functional F = E_s[2 − |z₀ + s(u₁+u₂) + d₁+d₂|] (bounded; bridge lemma applies verbatim).

**Certified results:**
- **Consistent coupling + tower identity** (Prop.): the one-step priors couple to the product measure; path enumeration = iterated-conditional evaluation for **all 81 policy trees**; per-policy conditional-expectation processes are martingales along the review filtration; Q₀ = Φ²g equals the tree supremum = **1/2**.
- **Information design and recourse strictly pay** (Prop.): Q₀ = 1/2 at u₁ = −2 with recourse u₂(z₁) = (0, −2, +2, +2) at z₁ = (−1, 1, 3, 5); every open-loop policy and do-nothing attain only **0** — the strict gap ½ > 0 is the correction's certified content: the first action designs the information (separates the branch), the second exploits it (brakes the revealed branch); z₁ = 5 is unrecoverable (cell value −1).
- **Refinement is monotone** (Prop.): matching toy — Q(coarse) = Q(mid) = −1/3 < 0 = Q(fine); every coarse-measurable policy is fine-measurable; the monotone bounded family is the direction the refinement limit must take.
- The residue conjecture now reads sharper: the continuous-time coupling law must reduce to the product coupling on finite review sequences, and the recursion must converge along refinements with this monotonicity.

4 pp, 0 overfull, no "??". Register clean (v2's leftovers already swept).

## Item 2 — Supp dedup pass (v49)

No verbatim duplication existed (the one-step instance and ex:hidden-mode are distinct forms; ladder/figure refs already pointed correctly). Executed as targeted cross-referencing: the delegated Farkas block now points forward to the worked two-floor certificate (λ = (1/2,1/2), margin 1/10), and the worked-certificates section points back to the S1 complete-discussion block. 20 pp, 0 overfull, no "??".

## Item 3 — E1 table hygiene (v53) — and a correction on record

- All 22 pandoc minipage header cells collapsed to plain cells across the longtables.
- **Defect discovered and corrected:** round 17's v52 fraction retune had **destroyed the DM table's `@{}}` preamble closer** — the v52 tex does not build (halt at the preamble), and the **pushed v52.pdf was stale** (the 44-overfull intermediate PDF from the first, pre-retune build; the "overfull=0" report after the retune was a stale-log false read — the halt check was skipped; the earlier v51 lesson repeated). Corrections: (i) v53 restores the closer and re-tunes the DM columns (Spec .055 / h .05 / Module .085 / Comparator .14 / five numeric .095–.10 / CI .105 / p .06); (ii) build health now checked explicitly (exit code + halt grep + fresh-PDF compare) at every build; (iii) v53 verifies **47/47**, 35 pp, **0 overfull**, no "??", and its shipped PDF is byte-verified against a fresh build.
- v52 stands superseded (tex and pdf both); the addendum records it; supersession map v7 carries the row.

## Status table (round-18 editions)

| Artifact | Edition | Checks | Pages | Overfull | Build |
|---|---|---|---|---|---|
| minimax dual certificates | v3 | 20/20 (chained 24/24, 8/8) | 4 | 0 | exit 0 verified |
| P1 supplementary | v49 | probes (2 cross-refs, ?? absent) | 20 | 0 | exit 0 verified |
| E1 cod forecast ladder | v53 | 47/47 | 35 | 0 | exit 0 verified |
| (unchanged) P1 v51, P3 v7, comp v11, ws v11, ebc v4, ARV v2 | round-16/17 editions | 8/8 probe, 30/30, 39/39, 46/46, 19/19, 61/61 | — | 0 | — |

## Alignment

minimax v3's numbers come from the same exact identities as v2's (Γ_h identification untouched); supp v49 differs from v48 by the two cross-reference sentences only; E1 v53 differs from v52 by the preamble repair + header collapse + column retune, with the verifier green.
