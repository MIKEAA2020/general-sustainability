# `uploads/p3 prompt response.txt` adjudicated, line by line — and what it changed in v38

The file carries **16 `Disagreement` markers over 8 distinct issues** (it renders the same review twice: a
prose pass at lines 2–860 and a "Conventions used below" pass at 861–3060, whose markers are prefixed
"Disagreement — not established"). Every one was checked against v37's text, not against my memory of it. The
file's own conventions (quotient incidence, the (P)/(D) LP pair, "failure of a certificate search is never
evidence of danger") were treated as claims to test, not instructions.

## Closed before this round (shipped in v35–v37, verified present)

| marker | issue | where the article now carries it |
|---|---|---|
| 109, 1263 | merging "distinct moieties" is not the exact condition; a tuple's lift needs its own rank test | Proposition 36 — "the conserved quantities of the composition are exactly the pairs of part-wise left-null vectors that agree on every identified compartment… the lift is injective and need not be onto" |
| 320, 1411, 1419 | the sign of $\pi_\varphi$ flips under the draining-side/donor-outflow convention; $\pi^{+}\bar vT \ne (-\pi)^{+}\bar vT$ | Definition 35 — the budget is quoted as the magnitude $\lvert\pi_\varphi\rvert \bar v_\varphi T$, "the sign only decides which side pays", and "no claim of a free interface can rest on the sign of $\pi_\varphi$ alone" |
| 352 | reversing the physical direction | same clause of Definition 35 (reversal "leaves that magnitude unchanged and moves the charge to the partner ledger") |
| 386, 1624 | a finite box bounds every finite $L$; $L \le 0.30$ is arithmetic, not an iff; no declared cutoff | the iff and the cutoff were removed in v35; the surviving statements are bounds conditional on a declared target or budget |
| 381 | zero-charge condition under the source-minus-recipient convention | the converse was withdrawn in v35 (no "free $\Leftrightarrow \pi \le 0$") |
| 523 | the fibre must be nonempty and connected, $\tau$ continuous, compact for endpoints attained | stated with those hypotheses, plus "where the declared set is non-convex the fibre can split, in which case the same two programmes bound the value set from outside instead of recovering it" |
| 540 | convex superlevel sets give level-set feasibility, not automatically LPs; monotonicity of $\tau$ is neither needed nor true | "Monotonicity of the event time along the fibre is neither needed nor true in general — an exit time is typically the minimum of several monotone branch functions" |
| 657 | drift brackets bound the *means*, not the support | §7.1: "a bracket on the drift of a selected set does not transfer to a bracket on its support or on its exit time, so no drift bound in this section is a deterministic hitting time, and the surrogate means are means" |
| 741 | the stationary capacity LP does not fix $\delta_m$: the lag-return rule is extra input | Definitions 21–22 read $\kappa_m$ at a *declared* $\tau_{\mathrm{use}}$, and the article states the deficit share is not a free parameter |
| 776 (second half), 1737 | the interior maximum of $\min_j$ over the fibre; the asserted $L_{\max}$ equality | v35 withdrew the exact-equality assertion; the instance is stated as $[0, \log 50]$ with the supremum at $(50,50)$ |
| 2120 | Definition 21 is not among the supplied assumptions; hypergraph reachability is a necessary path condition, not a characterization | no hypergraph characterization is claimed anywhere (the word does not occur in the article); compensation is Definition 40's programme |
| (convention) | "failure of a certificate search is never evidence of danger" | Remark 34 closes with exactly that: "a search restricted to diagonal multipliers and sums of squares can miss a certificate that exists, and that failure is no evidence of unsafety" |

## Live gaps this file exposed, now fixed in **v38** (9 logged edits)

1. **`funding-declaration`** — the article had Data availability, Code availability and a competing-interest
   statement, and no funding line. Added in the house form the sibling articles use (`## Funding` / "None
   declared."), placed ahead of the competing-interest statement in both formats.
2. **`quotient-versus-rows`** — this is the file's "specification gap" item (line 12), and it was *right about
   our text*: Definition 34 said the composition is the ledger "on the quotient compartment set (disjoint
   union modulo $J$) whose incidence is the block-diagonal $\mathrm{diag}(S_1,S_2)$ **extended by the
   identification rows**" — naming both operations in one sentence as if they were one. v38 gives both
   explicitly: the rows construction (keep every coordinate, add $x_a^1 = x_b^2$ as constraint rows, boxes
   stay on columns) and the quotient construction ($R_{Ca} = 1 \iff a \in C$, $x_C = R x_0$,
   $S_C = R[\mathrm{diag}(S_1,S_2)\ E]$, $B_C = R B_0$, $E_\varphi = -e_a + e_b$, classes by connected
   components), says which one the article uses and why, states that the quotient form is meaningful only when
   types and units agree **throughout each class** rather than pair by pair (now decidable, because Definition
   47 gave "type" a definition in v37), and records that neither form descends certificates on its own — that
   is Proposition 36's condition.
3. **`compensation-verdict`** — the file's §8.4 replacement predicate was already shipped as Definition 40, but
   the article never said *what the three outcomes are*. Now it does: feasible establishes steady-rate
   compensation under the declared inputs; infeasible establishes failure of that programme and carries its own
   witness row ($0 \le -1$, the alternative read in the failure direction); an incomplete declaration yields
   *not established*, "a statement about the declaration and not about the ledger". Plus the scope the file
   insisted on: the programme "establishes no dynamic safety, no exit-time bound and no corridor invariance",
   and a positive interface charge prices compensation rather than prohibiting it — which is why the charge sits
   in Definition 34's budgets and not in its admissibility conditions.
4. **`price-is-certificate-relative`** — the file's $\lambda = (2,1)$ versus $(1,2)$ example (line 776) is a
   real dependency the article had not owned: the interface price is certificate-relative, so it is now reported
   with the certificate that produced it, while admissibility is stated to be certificate-free. Same place, the
   multiplier reading: at a kink the capacity price is a *set*. Verified rather than quoted — for the
   two-cycle programme $\max\{r_1 + r_2 : r_i \le 1,\ r_1 + r_2 \le k\}$, computed on a grid,
   $V(k) = \min(2,k)$ with left slope $1.000$ and right slope $0.000$ at $k = 2$, and the optimal capacity
   multiplier solves to the interval $[0, 1]$ (two LPs over the optimal dual face). So the article says
   "a supergradient of the value function rather than the shadow value of the capacity" and does not attribute
   the file's $[0, 1/2]$ range, which belongs to a differently-constrained example.
5. **A mathematical error the file circled but did not state** — found by checking its §6 items against our
   text. The shipped proof of the fibre proposition asserted "the extrema of a continuous function over a
   polytope are attained at vertices, which is what the two programmes compute", which is false in general and
   is contradicted *by the instance printed two sentences earlier*. Recomputed: for
   $\tau = \min(\log y, \log(100 - y))$ on the fibre $y \in [1, 99]$, the maximum is $3.912023$ at $y = 50.0$
   — interior, not a vertex — and the minimum is $0$ at an end. v38 replaces the assertion with the correct
   polyhedral case (upper endpoint = the single LP with $r \le a_j^{\top} x + b_j$ for all $j$; lower endpoint =
   minimum over vertices, because a minimum of affine functions is concave and a concave function attains its
   minimum at an extreme point), and states plainly that no such reduction holds for an arbitrary continuous
   event time.
6. **`ram-vintage-pinned`** — see the next section; the file's §4.1 "the supplied numerical instance is
   incomplete" is the same class of problem, and the article now names the release instead of pointing at a
   repository the reader cannot open.

## The two author cells, closed from the branch and the deposit

Checked `MIKEAA2020/general-sustainability` at `refs/tags/edwards-framework-e1` (blob-filtered, sparse
checkout of `arena agent 1/paper rewrites`, read-only; nothing in the remote was touched):

- **v4.66 exists and the label is right.** `extracts/paper3/paper3_supp.md:163` prints
  "v4.66 (2024, Zenodo **14043031**) | 454 | 69 | 3.39", and the deposit record itself returns
  *title "RAM Legacy Stock Assessment Database v4.66", version field v4.66, publication date 2024-11-06,
  CC-BY-4.0, file "RAMLDB v4.66.zip"*. v4.65 is the immediately prior release (record 11995054, 2024-06-17).
  My previous-round flag ("no v4.66 in the listing") was an artefact of a paginated Zenodo search and is
  withdrawn; v4.44's row (record 2542919, 2018-12-22) is likewise correct as printed.
- **The pull cell does not need the author either.** The same record identifies the extract — "RAM Legacy v4.66
  extract `fisheries_adh.csv`" — and Proposition S5.1 *verifies* its vintage from the file's own contents: four
  of six published $F$ values reproduce the v4.66 release exactly (Adriatic anchovy 1.0026 vs 1.00; North Sea
  herring 0.2274 vs 0.23; W. Baltic herring 0.193 vs 0.19; Argentine anchovy south 0.0114 vs 0.011), while two
  example stocks no longer carry series in public releases v4.64–v4.66. S5.3 recomputes the cohort: 43 stocks,
  8 zeros, median 1.7902 yr (2.8578 yr over the 35 positive rows), maximum 201.1797 yr, and row-by-row
  agreement with $\mathrm{ADH} = F^{-1}\log(\mathrm{SSB}/B_{\lim})$ to relative error below $10^{-9}$.
  A dated release plus row-level anchors is a stronger vintage claim than a pull date, so the article now makes
  that one (main text §6.5.2 and Data availability), and the last `[author]` cell in the supplementary table is
  gone.
- Housekeeping: the branch's `latex/` directory still carries paper3 only to **v32**, so the v33→v38 line in
  `revision/v7/` remains the most advanced version and nothing needs rebasing.

## What was *not* implemented, with reasons

- The file's proposed orientation-covariant bookkeeping (store the column $e_\varphi$, the signed feasible set
  $F_\varphi$, and use $w^{\top} e_\varphi$) is a **replacement** of Definition 35's convention, not an
  addition to it, and the article's present form already immunises the only claim that depends on it (magnitudes
  budgeted, signs reported). Adopting it would relabel every $\pi$ in the composition section for no change in
  content. Recorded as declined.
- Naming Farkas explicitly: the article's alternative is stated in words with its witness row, and the cut
  condition already cites Gale (1957); adding a second attribution for the same theorem of the alternative would
  invite a question about which name is right for a network-flow result. Recorded as declined.
- A "weak/strong sustainability predicate" in the certificate vector: the file says none was supplied and the
  article does not claim one; paper 1 owns that vocabulary.
