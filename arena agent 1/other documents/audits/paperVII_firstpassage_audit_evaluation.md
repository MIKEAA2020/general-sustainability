# Evaluation of the external audit: "Paper VII abstract/Eq (1) writes H_F = B/[H]_+" (2026-09-03)

**Discipline:** evaluate, verify, don't take at face value. Every claim below was checked
against the actual files — the original program's sources
(`A024_paper_VII_first_passage.txt`, `A018_manuscript.txt`) and our latest rewrites
(P3 v14, which carries both the ADH tables and the first-passage theorems).

## 1. The central "verified quantitative flaw" — does not exist

The audit asserts that Paper VII's abstract and Equation (1) write

$$H_F = \frac{B}{[H]_+} \quad \text{(pure-decay fisheries form)}$$

and that this is "a leftover from an earlier draft that used a different yield proxy."
**The quoted equation appears nowhere.** Verified by grep across the original sources,
the closure packet, `uploads/`, and every rewrite:

- **A024 (Paper VII), Equation (1)** (`eq:model-hitting`) is the model hitting time
  $T^{\mathrm{dep}} = \inf\{t>0 : A^\bullet(t) \le \varepsilon A^\bullet(0)\}$ — not a
  formula for $H_F$.
- **A024's fisheries equation** (`eq:fish-proxy`) is the *correct* definition:
  $H_F = F^{-1}\log(B_0/B_{\lim})$, $B_0 = \mathrm{SSB}_{\mathrm{now}}$,
  $B_{\lim} = 0.2\max(\mathrm{SSB})$, "with $\dot B = -FB$ by construction. If the stock
  is already at or below the reference, the reported value is zero."
- **A024's abstract** contains no $H_F$ formula at all; its characterization is correct:
  "The fisheries logarithmic horizon is the deterministic first-passage time of the
  pure-decay model used to define it."
- **A018's fisheries table caption** (`tab:adh-fish`) — the audit's own quoted
  "actual definition" — is $H_F = F^{-1}\ln(\mathrm{SSB}_{\mathrm{now}}/(0.2\max\mathrm{SSB}))$,
  "or 0 if already at or below the reference," with the zeros-included median ≈1.8 yr.
  (The audit's "Table 5" numbering is imprecise; the definition is exactly the one it cites.)

The pattern $B/[H]$, $B/H$, or $1/F$ does not occur in any of these files or in our
rewrites. The audit's arithmetic ($B/H = 1/F$ when $H = FB$, "a reciprocal fishing
mortality, not a hitting time") is trivially true but targets a formula nobody wrote.
Its proposed fix — "replace $H_F = B/[H]_+$ with
$H_F = F^{-1}\ln(\mathrm{SSB}_{\mathrm{now}}/B_{\lim})$" — would replace correct text
with the same correct text. **No fix is needed; no paper change is made.** (Adding
text to answer a formula that does not occur would itself create a phantom point.)

## 2. The audit's sound observations — already true, already implemented

| Audit claim | Verified status |
|---|---|
| "Theorem 4 correctly recovers the log-ratio hitting time" | True. A024's GBM section: $dB = -hB\,dt + \sigma B\,dW_t$, $T_{\mathrm{fish}} \sim \mathrm{IG}(\nu_F, \lambda_F)$ with $\nu_F = \log(B_0/B_{\min})/(h+\sigma^2/2)$. Our P3 Theorem 20 reproduces this and adds the honesty note the audit would want: the $\sigma^2/2$ shortening is the Itô convention choice, "not a property of the physical process." |
| "Theorem 1: Inverse Gaussian hitting time — correct" | True. Our P3 Theorem 18: $T_{\mathrm{GW}} \sim \mathrm{IG}(\nu, \lambda)$, $\mathbb{E}[T_{\mathrm{GW}}] = \nu = H^{\mathrm{win}}_{\mathrm{GW}}$ — the mean equals the tabled trend-to-window-minimum ratio, the precise sense in which the table is a surrogate first-passage mean. |
| "Corollary: median < mean — correct" | True. Our P3 Corollary 19: $m < \nu$, $F_T(\nu) = \tfrac12 + e^{2\lambda/\nu}\Phi(-2\sqrt{\lambda/\nu}) > \tfrac12$, "the inequality must not be inverted." |
| "Proposition (No invented barrier) — honest" | True. A024's abstract: "The groundwater barrier is the 2002–2023 observational minimum, not an independent ecological floor"; our P3 §7.7 carries the explicit non-claims. |
| "M6 caveat consistency (ADH tables are not computed hitting times)" | True and implemented: our P3 states "none of the reported numbers is a computed instance of any model's first-hitting time — the groundwater column is a trend-to-window-minimum extrapolation, the phosphate column a reserve-life ratio, and the fisheries column a pure-decay proxy with recruitment omitted." |
| "Already-at-min section is thin; not a new theorem" | Fair as a characterization. Our P3 handles the boundary through Corollary 19's zero-noise limit and the stated boundary hypotheses ($F>0$, $\mathrm{SSB}_{\mathrm{now}} > B_{\lim}$); it is not claimed as a theorem. |
| "No direct tie to the DDE/stage/sample-and-hold" | In our P3 there *is* the declared interface contract with the delay-based dynamics ("five reasons the closed ledger does not reduce to the open working system"); the audit's point is orthogonal either way and creates no issue. |

## 3. The one place the trap could arise — and how our text already guards it

The plausible source of the audit's phantom is a misreading of the net-rate horizon family:
$\mathcal H^{\mathrm{act,net}} = (A^{\mathrm{act}} - A^{\mathrm{act,min}})/[-\dot A^{\mathrm{act}}]_+$
(A024 `eq:model-diagnostics`) and its biomass analogue
$H_B^{\mathrm{loc}} = (B - B_{\lim})/[-\dot B]_+$. Under pure decay $[-\dot B]_+ = FB$,
so a careless substitution would give $H_B^{\mathrm{loc}} = (B-B_{\lim})/(FB) =
F^{-1}(1 - B_{\lim}/B)$ — the first-order Taylor of the log hitting time, valid only
near the reference, and collapsing to $1/F$-type expressions under further sloppiness.
Our P3 refuses the substitution by construction: the local ratio is named as a
*different* object that "would require a compatible net $\dot B$ estimate," and the
tabled ADH is stated to be the log-ratio form alone. The distinction the audit demands
is already drawn in the text it claims to audit.

## 4. Verdict

**Does not apply.** The flaw is a phantom: the quoted equation exists in no version of
Paper VII, in no version of Paper I's table, and in none of our rewrites. The sound
parts of the audit (IG/GBM correctness, median inequality, no-invented-barrier, M6
consistency) were already satisfied in the original sources and remain satisfied in
P3 v14. No manuscript change is made; this evaluation is the disposition record.
