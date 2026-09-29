# Paper 2 (probabilistic sufficiency) — prior art added, 2026-09-29

## Measurement first (re-measured, because the bar verdict predated the re-source)

The bar assessment's "prior art: no" for paper 2 was measured on the stale v10. Re-measured
on v11, and the verdict **holds**: papers 2, 3 and 4 have bibliographies but **no prior-art
section**, against paper 1's dedicated section.

| paper | words | ref-section chars | years | author-initials | prior-art section |
|---|---|---|---|---|---|
| 1 | 23,582 | 6,197 | 38 | 72 | **yes** |
| 2 | 12,753 | 2,729 | 12 | 21 | **no** |
| 3 | 12,160 | 2,908 | 15 | 23 | **no** |
| 4 | 6,508 | 2,194 | 10 | 10 | **no** |

## The four references named in the earlier TODO: all verified, all absent

The header TODO listed Veliov, Doyen, Åström, Cardaliaguet/Quincampoix/Saint-Pierre.
Verified against publisher records before use:

- **Veliov, V.M., 1993.** "Sufficient conditions for viability under imperfect measurement."
  *Set-Valued Analysis* **1**, 305–317. DOI 10.1007/BF01027640. Gives a **sufficient**
  condition for an output feedback regulation map; equivalent to Haddad's viability
  condition when measurement is perfect.
- **Luc Doyen, 2000.** "Guaranteed output feedback control for uncertain systems under
  control and state constraints." *Set-Valued Analysis* **8**, 149–162. **Necessary and
  sufficient** — but only over **Lipschitz, memoryless closed loops** `u(h(x,w))`, for
  **exact maintenance of a closed domain**.
- **Cardaliaguet, Quincampoix & Saint-Pierre, 2007.** "Differential games through viability
  theory: old and recent results." *Advances in Dynamic Game Theory*, Ann. ISDG **9**, 3–35.
- **Åström, 1965** — already present in the bibliography.

All three of the missing ones were **absent** from paper 2's bibliography; now added.

## A trap avoided

The bibliography already contained a "Doyen" — **Laurent Doyen**, co-author with Chatterjee
and Henzinger (2009) on qualitative POMDPs. That is a **different person** from **Luc
Doyen**, the viability theorist of the 2000 paper. Both are now cited, and the text
distinguishes them explicitly with a parenthetical warning. Merging them would have been a
visible error.

## The position

The two viability neighbours delimit the contribution precisely:

- **vs Veliov (1993)**: his condition is sufficient only, so its failure is inconclusive.
  Paper 2's is necessary as well as sufficient, so failure is informative.
- **vs Luc Doyen (2000)**: he already has necessary and sufficient, so exactness alone is
  not the delta. The delta is twofold: (i) his loops are Lipschitz and **memoryless**, while
  the recursion here admits **history-dependent** policies, with the feedback/blind
  distinction strict (`rem:feedback-strict`); (ii) his criterion is **exact maintenance** of
  a closed domain, while the safety value here is **quantitative**, with the deficit bound
  `1 − V_k(b) ≥ min b(x)`.

## What is claimed (five items, plus an explicit not-claimed list)

1. Exact sufficiency where the nearest sufficient condition is only sufficient
   (`thm:support`).
2. Admission of history-dependent policies, feedback/blind strict
   (`rem:feedback-strict`) — and the mechanized support identity is checked on the
   *repaired* statement.
3. A quantitative deficit rather than a binary verdict (`prop:deficit`).
4. The α-vector structural identification as Sperner-bounded antichains
   (`prop:antichain`), the class lattice with realized gaps (`thm:lattice`), parametric
   closed forms.
5. Machine-checking in Lean 4 (support identity, freeze count and frozen value, α-vector
   rationality), with the Sperner bound of `prop:antichain`(iii) **cited, not formalized**.

Not claimed: the belief-state reduction (Åström), the α-vector representation as such
(Smallwood & Sondik), the qualitative complexity landscape (Chatterjee, Laurent Doyen &
Henzinger), or the hardness results (Papadimitriou & Tsitsiklis; Lovejoy).

## Checks run

- All 38 `\ref` targets resolve; 46 labels defined, zero missing.
- Every cited label verified to exist: `thm:support`, `rem:feedback-strict`,
  `prop:deficit`, `prop:antichain`, `thm:lattice`, `priorart`.

## Result

`paper02_probabilistic_sufficiency_v12.tex`: 12,753 → 14,155 words.

## Next

Papers 3 and 4 remain, both without prior-art sections. Paper 4 is the thinnest (6,508
words, 10 years, 10 author-initials) and is the higher risk of the two.
