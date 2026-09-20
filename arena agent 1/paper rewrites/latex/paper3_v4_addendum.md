# Paper 3 v4 — change summary (v3 and earlier preserved unchanged)

v4 = v3 + corrections from the joint external audit (grok + gemini), each
re-verified against the artifacts before fixing. Full claim-by-claim
verdicts in `paper3_audit_verification_v1.md`.

## Manuscript fixes (11 edits)

1. §2.1 grammar: the datum "comprises" a phase state (not "is" one).
2. §2.1: the typed-endpoint operator placed in the hierarchy
   (E_typ ⊆ E_end,typ ⊆ E_end); E_end disambiguated.
3. §2.2: belief glossed as a set of states consistent with the observations;
   update target stated as the reachable label set.
4. §2.3: Farkas normalization specified (sum to one; certificate
   scale-invariant; margin defined by the normalization).
5. §3.1: the `rational` module named in the prose (nine modules, now nine
   listed).
6. §4.1: rescue threshold truncation stated (κ* = max(0, 1 − x)).
7. §4.2: coordinate-namespace note for the (x, κ*(x)) pairs.
8. Abstract: "no third-party runtime dependencies" (133 words).
9. §6/AI declaration heading: "in the research process".
10. Reference 2026a: duplicate deposit sentence removed; figshare DOI cited
    once (Deposit2026).
11. Header comment: v4 provenance.

## Figure fix (shipped in v4 and package 1.1.2)

Fig. 2(a) licensing regions relabelled to exclusive/both form:
"only SLOW licensed (r < ρ₁)", "both licensed for ρ₁ ≤ r ≤ ρ₂",
"only FAST licensed (r > ρ₂)". Pipeline synced into the package
(figure_code/), package bumped 1.1.2, SHA256SUMS regenerated,
`run_all.sh` passes end-to-end.

## Refuted audit claims (documented, not changed)

- "§4.1 assigns x = 3/2 to the false-positive witness" — line-break misparse.
- "Fig. 1(a) green curve is the benign index mislabelled as s1" — colour
  misread; the deposited figure's legend and geometry are consistent.

## QA

v4: exit 0; 9 pp; 0 `??`; overfull baseline only; abstract 133 ≤ 150;
single DOI occurrence; all insertions verified in the rendered PDF.
