# Structure register - paper3_material_ledgers_v36

Built from v35 by `build_v36_kernel.py` (v35 and v34 unchanged on disk). Gate
`verify_v36_build.py` -> ALL CHECKS PASS. PDF 52 pages (v35: 51, v34: 48). tex pure ASCII,
no doubled backslashes, balanced math delimiters.

## What v36 changed relative to v35 (8 logged edits)

1. `def45-46-prop41-rem35`: `These three statements are the calculus the article's own citations ha` -> `**Definition 45 (Latest safe intervention time).** Let a critical supp`
2. `cert-parameter-status`: `each entry taking one of three values: established, not established, a` -> `each entry taking one of three values: established, not established, a`
3. `remark33-convention-cited`: `Which convention a reported premium uses is a property of the accounts` -> `Which rows enter the ratio set is fixed by the accounts, not by this c`
4. `guidebook-reference`: `Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mat` -> `Gale, D., 1957. A theorem on flows in networks. Pacific Journal of Mat`
5. `companion-precision`: `(Abaee, 2026, doi:10.5281/zenodo.22554217; eq. (1) and Section 2.4 of ` -> `(Abaee, 2026, doi:10.5281/zenodo.22554217; its eq. (1), where the memo`
6. `numbering-range-46`: `runs on the single 1–44 sequence counter` -> `runs on the single 1–46 sequence counter`
7. `numbering-added-46`: `Definitions 21–23 and 34–35 and 38 and 40–44, Lemma 4, Theorem 24, and` -> `Definitions 21–23 and 34–35 and 38 and 40–46, Lemma 4, Theorem 24, and`
8. `companion-precision-2`: `(under review; eq. (1) and Section 2.4 of that analysis), not an objec` -> `(under review; its eq. (1), the gated three-state core, and its Sectio`

## Statements added by this batch

- **Definition 45 (Latest safe intervention time)**
- **Proposition 41 (The deadline has a closed form, and it is not the horizon)**
- **Definition 46 (Supportable-output envelope)**
- **Remark 35 (What a non-displacement gate can say on this apparatus)**

## Verification actually run for this batch

- Independent re-derivation of the deadline numerics (`repo_audits`, scipy grid LP): minimise `int d dt`
  subject to `d = d_0` on `[0,tau]`, `dot d >= -rho`, `d >= 0`, `d(T) = 0`. Values 70.0088 / 22.7474 /
  27.9970 against the closed forms `d_0 tau + d_0^2/(2 rho)` = 70 / 22.75 / 28 (grid tolerance), and
  `t_last` = 3 yr / 2.4643 yr / -0.75 yr. So Proposition 41's formula is checked, not quoted.
- Reversal: undoing the 8 logged edits reproduces v35 byte-exactly in both formats (md 197,296 chars;
  tex 213,666 chars), modulo whitespace and the display-underscore convention introduced in v35.
- Labels: 54 (v35) -> 58 (v36); md set identical to tex set; no type+number pair repeated; maxima
  Definition 46, Proposition 41, Theorem 24, Remark 35, Lemma 4, Corollary 19; numbering note reads
  "1-46 sequence counter" with the extended added-label list in both formats.
- Dialect: no non-ASCII character in the tex, no `$`, no doubled backslash command (`\\mathrm`-class
  defect, which the first v36 build did have, is gone — the block file was normalised and rebuilt).
- Companion pointer checked against the deposited `paper4_delay_dynamics_v30.pdf` (Zenodo 22554217):
  eq. (1) is the gated three-state core `N' = S(N) - qEN`, `Z' = (1/tau_m)[Phi_k(qEN - S(N)) - Z]` with the
  delayed effort law, and Section 2.4 is "The four-state working core and its relation to (1)".
- Carbon convention checked against the NFA Guidebook (2021 ed., Section 9.1.2) plus the 2019 workbook note;
  overshoot-day formula and annual recomputation checked against GFN's published method notes; 2022's
  announced date (28 July = day 209) reconciled with the 213 d computed from the 2025 accounts.
- PDF text extraction: "Latest safe intervention time", "Supportable-output envelope", "non-displacement
  gate", the Guidebook sentence and reference entry all present; literal underscores in math down to the two
  in the e-mail address.

## Deliberately not shipped, with reasons (full discussion: review/open_items_v4_closed.md)

- The mechanism-design umbrella **as a theorem**: its third hypothesis is a declared MDV field the article
  does not define, and its "boundary-shift invariance" step now conflicts with Proposition 36 unless the
  compatibility condition is carried along. The article keeps Proposition 28, Proposition 29,
  Proposition 36 and Definition 40 per case.
- `LNS(S_T)` / a new "left null space" definition: already Lemma 3's moiety covectors and Proposition 36's
  `(U_1 + U_2) cap ker D_J^T`, and it is not what "LSIT" meant.
- The superlevel-set "alternate proof" of Proposition 29: its two inclusions are the printed proof.
- MDV and the per-parameter status *table*: one supplementary batch, not the body.
- The memo's optional strict-barrier variant of Proposition 41: the article's corridor is closed, so
  `A >= A_min` is fixed once rather than offered as a choice.

## Post-review addition to Proposition 41

The closed form is stated with $H^{\mathrm{loc}}$ attributed to **Proposition 26** (where the article defines
it as $(A_0-A_{\min})/\varphi(A_0)$) and read on the support pool as in Definition 22, and it carries a
direction-only clause: substituting the true horizon $T$ for $H^{\mathrm{loc}}$ moves the deadline later and
never earlier when the depletion law is nondecreasing in the stock, with no equality claimed. The v35 and v36
files were rebuilt together with this addition; the block file `v36_block_deadlines.md` is its source and the
gate compares the manuscript against it, so the linkage is checked, not asserted.

## Author items still outstanding

- D4 wording, and with it the decision whether an umbrella invariance statement enters the article.
- Uploading the code archive `revision/v5/code/` to the deposit record (its contents are on disk locally).
- Whether to publish the non-carbon-restricted premium variant next to the published-components figure in
  Remark 33; the convention itself is now cited rather than assumed.
