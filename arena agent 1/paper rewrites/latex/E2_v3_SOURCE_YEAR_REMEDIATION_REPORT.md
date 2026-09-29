# E2 remediation on the v3 (source-year) basis — status

Basis is **ratified and closed**. v3 = source-year. The hybrid v2 is not a
convention and is not used anywhere.

Second pass complete (this session): the paper has been read end-to-end, eight
surviving v2-basis *derived* constants and three prose defects were found and
corrected, the certified-layer criterion was found to be wrong and was
recomputed, the convention is now declared in the paper, the provenance chain
names the v3 scripts, and the battery is 301 checks strong with a 97/97
sabotage record run behind a green-control. The paper compiles cleanly
(tectonic 0.17, 22 pages, no errors, no overfull boxes).

---

## 1. State of the tree

### Reverted (moved to `src/superseded_v2/`, banner + README)

| artifact | what it was | status |
|---|---|---|
| `wave_e_cod/src/run_families_v2.py` | "Regenerate E2 Table 1 on the registered (v2) basis" | **SUPERSEDED**, moved aside |
| `wave_e_cod/src/results/e2_families_v2.csv` | its output, 45 rows on the hybrid block | **SUPERSEDED**, moved aside |
| the v28 tex campaign | 372 changed lines, overwhelmingly basis-forced | **abandoned** — v29 built from v27 instead |
| the 123-check v28 battery | pinned the hybrid | **not used**; rebuilt as `v29_battery.py` |

### Created / regenerated on the v3 basis

| artifact | contents |
|---|---|
| `src/run_intervention_v3.py` | promoted source-year runner; honest docstring stating the convention, the evidence, and the consequences |
| `results/intervention_results_v3.json` | SD 114.91, UC = −328.97 / −287.36 / −80.87 |
| `results/intervention_boundaries_v3.csv` | kernel boundaries on the v3 classes |
| `src/run_families_v3.py` → `results/e2_families_v3.csv` | Table 1 families (A φ=0.25/0.5/0.75, B graded2/3) |
| `src/campaign_e2_elevation_v3.py` → `src/results_srcyear_v3/` | K-grid, stochastic, finite floors, bootstrap, residuals |
| `src/campaign_e2_depensation_v3.py` | §3.6 Allee free refit (r, K, s₀ all free) |
| `src/campaign_e2_allee_declared_v3.py` | §3.6 declared-strength row — s₀ **fixed**, (r, K) refitted, which is what the paper's row actually says |
| `src/campaign_e2_fox_form_v3.py` | §3.6 Fox row, Schaefer reference computed not hardcoded |
| `src/results_forms_v3/` | outputs of all three form campaigns |
| `src/make_figs_v17.py` → `src/figs_e2_v3/` | Figures 1–7; bit-identical to `make_figs_v16.py` output (md5-verified), v17 only repoints the provenance at the v3 runner and inputs |
| `fam/e2/paperE2_cod_intervention_v29.tex` | the paper, rebuilt from v27 on v3 |
| `v29_battery.py` | 213-check battery, sabotage-tested 49/49 behind a green-control |
| `basis_audit.py` | 157 declared quantities, 0 on the v2 basis |

All three form campaigns and their outputs are archived in the repo next to the
runner (`repo/wave_e_cod/src/`), and were re-executed there, so the paths named
in the paper's Data-availability section resolve.

### Two campaign defects found and fixed

- `campaign_srcyear.py` hardcoded `REPO = Path("/home/user/git_repo")` (could
  not be imported off that machine) and froze the constructive bound at the
  registered 114.85 while resampling the source-year pool.
- The two *form* campaigns imported `run_intervention_srcyear.py` (docstring a
  verbatim copy of v2's, outputs to `results_srcyear/`) and self-checked against
  `intervention_results.json` — the **registered** artifact. The Fox campaign
  additionally hardcoded the v2 constructive bound 57.61.

---

## 2. The `2219.6` purge is reverted

**All 12 sites restored.** Verified: `tex.count("2219.6") == 12`, and the
battery asserts exactly 12. `2070.9` (zero-catch q05 T=∞) restored too.

`2219.6` was never a Fox artifact. It is the source-year q05 BAU kernel at
T=∞.

The no-dominance verdict stands as v23–v27 had it: at q05/T=∞ every
positive-catch rule is empty while BAU's is nonempty (2219.6) and zero-catch is
more protective still (2070.9).

---

## 3. Second migration pass — what the first pass missed

The first pass migrated the **class values** (−460.0/−318.8/−114.9 →
−329.0/−287.4/−80.9) and the constructive bound (57.61 → 91.59). It did not
reach every **worked line built out of** a class value. `172.46 − 318.76 =
−146.3` is not a class value; it is arithmetic on one, and a token sweep for
class values walks straight past it. Eight such lines survived into v29.

| where | v2 (found) | v3 (corrected) |
|---|---|---|
| §3.3 q05 arithmetic | `172.46 − 318.76 = −146.3` | `172.46 − 287.36 = −114.9` |
| §3.3 worst arithmetic | `(−287.6)` | `172.46 − 328.97 = −156.5` |
| Result 3.4 φ threshold | `1 − 114.85/296.09 = 0.612` | `1 − 80.87/296.09 = 0.727` |
| Result 3.4 φ=0.25/0.5/0.75 | `107.2 / 33.2 / −40.8` | `141.2 / 67.2 / −6.8` |
| §3.7 K=1000 constructive | `−62.9` | `−28.87` |
| §3.10 bootstrap F′(K\*) | median `1.134`, `[1.001, 1.177]` | median `1.142`, `[1.010, 1.179]` |
| Abstract bootstrap interval | `[0, 84.8]` | `[0, 121.1]` |
| Abstract + conclusions survival | `0.87 → 0.58` (`0.95 → 0.74`) | `0.91 → 0.65` (`0.95 → 0.77`) |

Conclusions item 5 also had the 60-kt claim **backwards**: it said the
source-year convention "leaves the 60-kt rules outside the robust set (their
T=∞ boundary is 900.3 kt)". 900.3 is the **v2** boundary; on v3 it is 884.6,
i.e. the rules sit *on* the reference point and hold the whole safe set, which
is what §3.1 and Table 1 say. Corrected, with the v2 figure retained as the
comparison.

### The certified layer was wrong, not merely stale

Result 3.5 located the certified horizon with the criterion
`K* + r_T < K`. Direct evaluation of the runner's own `kernel()` at the shifted
threshold shows that criterion is neither necessary nor sufficient:

| class | last nonempty T | empty from | at the last horizon (BAU) |
|---|---|---|---|
| perpetual-worst (−329.0) | **T = 6** | T = 7 | [5132.9, 10⁴] |
| 5th percentile (−287.4) | **T = 6** | T = 7 | [4593.2, 10⁴] |
| 10th percentile (−80.9) | **T = 7** | T = 8 | [4560.3, 10⁴] |

At T = 7 the shifted threshold (4560.3 kt) is still below K = 5000 kt, yet the
certified kernel is empty under the two harsher floors: the BAU closed loop has
no worst-case fixed point there, so every trajectory declines, and from the
domain ceiling it reaches 4689.6 kt after five steps and 4424.5 kt after six —
it clears the six-year threshold but not the seven-year one. Under the
informative floor there *is* an attracting fixed point (4606.5 kt), which is
why the horizon is one year longer there. Result 3.5 now states the horizon
per class, and the paper no longer asserts the naive criterion.

Note also that the archived artifact's `certified_horizon_nonempty` field says
5 for every policy and class. That is a **grid artifact**: `HORIZONS` skips 6
and 7, so 5 is merely the last declared horizon tested. The battery recomputes
6 and 7 explicitly rather than reading that field.

The convention shift lengthens the horizon by **one year at every class**
(T = 5→6 and T = 6→7), not the two years the manuscript claimed.

### Three further prose corrections

- §3.8: 0.8455 was reported as `0.84` (truncation where the section rounds).
- §3.6: "The 120-kt rule's kernel is empty" is unqualified and false under the
  Fox form — its 10th-percentile T=1 boundary is 922.7 kt. Qualified.
- §3.6: the declared-strength row was said to "bracket the identified row from
  the milder side"; the cells do not support that (it is lower at two cells and
  higher at one). Replaced by the actual maximum divergence, 12 kt (≈1%).

---

## 4. Basis-aware systematic numeric audit (`basis_audit.py`)

Every quantity the paper prints is declared with **both** its v2 and its v3
value, read from the regenerated artifacts. A number that is correct on one
basis is indistinguishable from the same number on the wrong basis unless you
know which basis produced it.

| tex | declared quantities | on the v2 basis | unexplained |
|---|---|---|---|
| v28 (before) | 85 | **72** | — |
| v29, end of pass 1 | 85 | 0 | 7 (rounding false alarms) |
| **v29, end of pass 2** | **106** | **0** | **0** |

Two refinements were needed to make the audit truthful rather than merely green:

- **§2.3 prints v2 values on purpose.** Once the convention section quoted the
  destination-year classes for comparison, a whole-document absence check
  reported a false positive on every class value. All counts now run against
  the text with that block removed.
- **Legitimate comparisons need an exemption.** `460.0` (§3.4) and `900.3`
  (conclusions) are quoted as registered-convention comparisons. Declarations
  carry an `allow` list of contexts; occurrences excused by one are not
  reported as migration defects.

The 21 declarations added in pass 2 are exactly the derived quantities of §3
above, plus the stochastic, certified-layer and 60-kt entries.

---

## 5. Battery: 301 checks, sabotage 97/97

`python3 v29_battery.py [path/to/tex]` (defaults to v29). Sections:

- **R9** Section 2 residual summary, plus the new §2.3 convention block:
  definition, the three grounds, the provenance admission, the four
  sensitivity quantities, and the recomputed in-sample MSE pair (12,772 vs
  17,873 kt², 28.5%).
- **R10** classes, vacuity, the restored no-dominance mechanism.
- **R11** all six tables parsed into rows and compared **cell by cell** against
  the artifacts, with a one-grid-step tolerance (0.05 kt) where the number
  comes from the 0.05 kt grid. 12 + 4 + 10 + 4 + 6 + 2 rows.
- **R12** constructive bound and the certified layer — the ladder and the
  per-class horizons are **recomputed** with the runner's own `kernel()`, not
  grepped for.
- **R13** §3.6 form rows, from the three regenerated form campaigns.
- **R14** stochastic, bootstrap, and the abstract/conclusions echoes.
- **R15** provenance, figures, declarations.

**Sabotage: 97 mutations, 0 holes** — every number and provenance string the
battery claims to protect was corrupted one site at a time, including the §2.3
deletion, the figure-directory revert, all three provenance de-promotions, and
the reinstatement of the naive certified criterion.

**The harness runs a control first, and that matters.** An intermediate version
of the battery had two checks that failed *permanently* (a Section 2.3 substring
test that kept the LaTeX delimiters in the needle). The sabotage harness then
reported 47/47 CAUGHT — because a battery that is never green turns red on every
mutation, caught or not. The harness now runs the battery on the unmutated file
first and aborts if it is not green. With the control in place, six genuine
holes surfaced immediately:

| hole | fix |
|---|---|
| `91.59 → 57.61` invisible: the guard `57\.6(?!\d)` cannot match `57.61` | check 57.6, 57.61, 57.62 separately |
| `-80.9 → -114.9` invisible: the v2 q10 class is `-114.8` to Python and `-114.9` to round-half-up | check both 1-dp renderings |
| `−6.8 → −40.8` invisible: `40.8` was missing from the absence list | added |
| Table 3 `r` column: one 0.05 kt tolerance let a 2% error in r through | per-column tolerances |
| Fox `r = 0.1044` and Allee `g_max = 372.4` recur, so presence checks cannot see a single-site flip | scoped prose test + exact site counts |

One further collision is recorded rather than "fixed", because it is real:
`-114.9` is *both* the v2 q10 class and the v3 §3.3 arithmetic
`172.46 − 287.36 = −114.90`. The class check therefore takes an allowed context
(the arithmetic sentence) instead of a bare absence test.

Design rules the battery is built on (each one earned):

- **Presence checks are defeated by repetition.** Values that recur are scoped
  *and* given near-miss guards (91.58/91.60/114.8/115.0 …).
- **Context-free tokens collide.** `0.65` is the v2 autocorrelation *and* a
  legitimate rounding of the v3 120-kt survival (0.6466). `0.87` is the v2
  abstract survival *and* a substring of `80.87`. Both are scoped.
- **Rows wrap and carry `\textbf{}`.** Tables are parsed into cells; the naive
  `\textbf{` strip leaves a stray `}` and breaks matching.
- **A row label carries annotations.** `1769.2 (\(=2K^*\))`, `5000 (registered)`
  — label matching is a normalised prefix test.
- **Recompute what is cheap to recompute.** The certified horizon was wrong for
  two years precisely because it was asserted, not computed.

---

## 6. Re-deposit question — answered

**Correct and re-deposit as new versioned files. Leave v1/v2 untouched.**

Done: `intervention_results_v3.json`, `intervention_boundaries_v3.csv`,
`e2_families_v3.csv`, `results_srcyear_v3/`, `results_forms_v3/`,
`figs_e2_v3/`. v1 and v2 are unmodified.

Why not overwrite v2: (1) audit trail — a silently rewritten deposit no longer
shows what was there when anyone cited it; (2) project precedent — v2 itself
wrote `_v2` files so the audited artifacts stay untouched; (3) referee-facing —
a reviewer should be able to diff v2 against v3 and see one thing change.

Provenance note drafted for the deposit record:

> v1 and v2 evaluate the one-step residual as
> `S_{j+1} − (S_j + g(S_j) − C_{j+1})`, while the estimator `fit_params`
> minimises `S_{j+1} − (S_j + g(S_j) − C_j)`. v1/v2 therefore combine
> parameters fitted under the source-year convention with disturbance classes
> measured under the destination-year convention. v3 corrects the residual
> convention to match the estimator. The v1/v2 artifacts are retained for the
> audit trail and are not cited.

---

## 7. What the paper now says (v29)

| | v28 (hybrid) | v29 (v3) |
|---|---|---|
| classes worst/q05/q10 | −460.0 / −318.8 / −114.9 | **−329.0 / −287.4 / −80.9** |
| §2 SD / mean / max / acf | 134.96 / −20.44 / +179.76 / 0.652 | **114.91 / −10.88 / +206.55 / 0.554** |
| vacuous classes | 2 of 3 | **1 of 3** (worst only) |
| q05 BAU kernel T=∞ | empty | **2219.6** |
| constructive bound | 57.61 | **91.59** |
| maximal robust flat catch | 57.62 | **91.59** |
| certified horizon | T = 6 | **T = 6** (worst, q05) / **T = 7** (q10) |
| certified set at the horizon | [4942.7, 10⁴] | **[5132.9 / 4593.2 / 4560.3, 10⁴]** |
| bootstrap r / g(K*) / constructive / frac | 0.207 / 150.5 / 35.6 / 71.3% | **0.219 / 159.6 / 78.7 / 88.2%** |
| 60-kt rules, q10 T=∞ | 900.3 | **884.6** (hold the safe set) |

New in pass 2: **§2.3 The catch-timing convention** — the residual written as
`e_t = S_{t+1} − (S_t + g(S_t) − C_{t+δ})` with δ = 0 (source-year) adopted on
three grounds (coherence with the estimator that produced (r, K); better fit in
and out of sample and lower residual autocorrelation; and no interior optimum
when the blended catch `w·C_t + (1−w)·C_{t+1}` is refitted over w, the MSE
being monotone with its optimum at the boundary w = 1). It states plainly that
nothing in the archived source documentation records whether the SSB column is
pre- or post-fishery, that the March–May spawning of Northern cod means neither
pure convention is mechanistically exact, and that the convention is therefore
adopted on statistical and coherence grounds rather than provenance. It lists
the four quantities that move materially and points at the retained
registered-convention artifacts.

Also corrected in pass 2: §3.11 no longer says the xteNCAM row was "refitted in
the registered convention" (its own source uses the source-year catch at t) —
it now says "the same source-year convention as the primary object"; and the
"fully deterministic (no random components)" claim is replaced by a
reproducibility statement naming the fixed seeds and draw budgets.

Figures: all seven regenerated by `make_figs_v17.py` into `figs_e2_v3/`,
bit-identical to the v16 output (md5-verified) — the change is provenance, not
pixels. `fam/figs_e2_v3/` carries the copies the tex resolves.

---

## 8. Still open — status after this pass

### 8.1 LaTeX compilation — **closed**

`tectonic 0.17.0` was installed at `/home/user/tools/tectonic` (musl build,
outside the snapshot-excluded `.local`). The paper compiles:

```
Output written on paperE2_cod_intervention_v29.xdv (25 pages)
Writing `paperE2_cod_intervention_v29.pdf` (994 KiB)
```

**No errors, no overfull boxes.** Four underfull hboxes remain (badness
1033–2884), all in the Data-availability paragraph, which is full of
unbreakable 40-character paths; that is looser-than-ideal spacing, not text in
the margin, and the same paragraph previously produced *both* underfull boxes
and two overfull ones (29 pt and 45 pt). Getting there took: a `	exttt{}`
break opportunity at the two paths that actually overhung, and shortening one
adjacent pair ("writes `intervention_results_v3.json` and
`intervention_boundaries_v3.csv` in `results/`") rather than inserting a
dozen breakpoints — 21 breakpoints removed every overfull box but replaced
them with badness-10000 lines, which is the worse trade.

Table 3 and Table 6 headers were re-flowed ("Constructive (kt)" → "Constr. /
bound (kt)"), which cleared the last overfull box (2.72 pt).

The archived copy in `repo/arena agent 1/paper rewrites/latex/` compiles
standalone there too (same 0 overfull / 4 underfull), so the deposit is
self-contained.

### 8.2 Commit to the archive repo — **blocked, with everything ready**

`git commit` fails in the workspace copy:

```
error: invalid object 100644 0a7254ef... for
       'arena agent 1/paper rewrites/latex/COVER_LETTER_..._v1.md'
error: Error building trees
```

The checkout is **partial**: of 5,981 objects tracked in HEAD, 4,892 are
absent from `.git/objects` (only `arena agent 1/` and `wave_e_cod/` were
materialised; `research_program/`, `agent 2 productivity illusion/` and 20
other top-level trees have no blobs). Git must build a tree over every tracked
file, so no commit is possible until the objects are present. This is a
workspace limitation, not a problem with the files.

Everything else is done and staged (51 files, index shows `A` for all):

| file | what |
|---|---|
| `E2_V3_COMMIT_MANIFEST.txt` | the exact 51 paths, grouped |
| `E2_V3_COMMIT_MESSAGE.txt` | the commit message |
| `commit_e2_v3.sh` | `bash commit_e2_v3.sh /path/to/full/clone` — creates `e2-v3-source-year`, stages by path, refuses if anything tracked would be deleted, commits, does not push |

The paper, PDF and the three verification scripts were **refreshed again
after the prose read** (v29g), so re-copy them into the clone before running
the script — it stages by path, so it picks up whatever is in the working tree.

The three verification scripts are archived beside the paper (the project's
`*_verification.py` convention) and were **run from there**: 261 checks / 0
failed, 157 quantities / 0 on v2, 97 mutations / 0 holes. Each resolves its
input beside itself, with a workspace fallback, so the archived copies are
runnable without editing.

The Zenodo deposit still needs a human: no remote is configured and no API
token is available here. Note for the deposit: v1/v2 stay as they are, v3 is a
new version, and the provenance note of §6 goes in the description.

### 8.3 Table 2's s₀ rounding — **closed (declared)**

Section 3.6 now carries a reproducibility note: `s_0 = 642.3` kt is a rounding
of the fitted `642.3296` kt; the worst-class T=∞ boundary is 1098.75 kt at the
rounded value and 1098.8 kt at the fitted one (the q05 T=∞ boundary moves
1020.9 → 1020.95 kt, which prints identically). Every other cell is unchanged
and the published cells are those of the rounded value. Gated by battery
check R13d4.

### 8.4 Grid vs interval engine — **closed (declared)**

The same note records that the Allee and Fox rows come from the 0.05 kt state
grid while the registered row comes from the committed interval-arithmetic
engine, that a grid boundary can sit up to 1 kt below the interval-arithmetic
one next to the repelling boundary (2218.75 vs 2219.649; 2070.30 vs
2070.884), and that the two are not to be compared at 0.1 kt resolution
(the campaign declares TOL_KT = 1.0 kt). Gated by R13d4.

---

## 9. Three failure modes worth recording

Each of these cost real time and would recur.

1. **`index(end_marker)` finds the wrong occurrence.** Twice this session a
   block was delimited with `start = text.index(A)` and
   `end = text.index(B)` where `B` also occurred earlier in the file. The
   second time it duplicated 1,112 lines of the paper (§2.3 through
   References) because `end < start` makes the slice empty and the splice
   `text[:start] + block + text[end:]` then re-emits the middle. **Always
   search the end marker from the start position.** The repair was verified by
   re-running the 213-check battery, which is the reason the battery covers
   the whole document rather than one section.
2. **A regex replacement template is not a literal.** `re.sub` processed
   `\allowbreak{}` in the replacement as `\a` (BELL) + `llowbreak{}`, silently
   writing three control characters into the source. XeTeX then halted with
   "Text line contains an invalid character"; nothing in the numeric checks
   would ever have noticed. Battery check R16a now asserts that the source
   contains no non-printable characters.
3. **A suppressed compiler hides failure.** `tectonic ... > /dev/null 2>&1`
   followed by `grep Overfull` on a stale-looking log read as "0 warnings,
   clean" while the engine had actually aborted; the log from a *halted* run
   contains no warnings. Check the exit status (or the "Writing `<name>.pdf`"
   line) before trusting a warning count.
4. **A backslash written into a source file is one level of escaping away from
   the one you meant.** The sabotage harness's whitespace-flexible splice was
   written as `r"\\s+"`, so the pattern matched a literal backslash followed by
   `s` instead of a line break. Five mutations silently reported "pattern not
   found" for two full runs, and the harness still printed a plausible score.
   It is the same trap as failure mode 2 in a quieter form: nothing raises, the
   check just never fires. Write such patterns as `chr(92) + "s+"`.
5. **A patch script's stored text has to track later re-edits of its own
   output.** The prose patch (`make_v29g.py`) is idempotent — an edit whose
   anchor is gone and whose result is already present is skipped. Three of its
   entries were later reworded by later entries *and* re-wrapped to the
   source's 72 columns, so the stored result no longer matched byte-for-byte
   and the script aborted on a file that was already correct. The idempotence
   test now compares whitespace-collapsed text, and a "nothing to do" run
   exits 0 instead of asserting a change.

## 10. The end-to-end prose read (this pass)

Item 1 of the open list was "v29 has not been read end-to-end for prose
coherence — the numbers are verified, but sentences were patched, not
rewritten." That read is done, and it was not cosmetic: it found five
statements that were **false on the v3 basis**, all of them survivors of the
v2 → v3 migration that a numeric sweep walks straight past, because every
number in them was a correct v3 number.

| # | where | the statement | the truth |
|---|---|---|---|
| 1 | §3.8 | "The \(P \ge 0.9\) bar is not attained by any tested constant catch under i.i.d. or block resampling" | True on v2 (ceiling 0.868), **false on v3**: zero catch is 0.906 and the interpolated i.i.d. crossing is 13.5 kt. Under blocks it is genuinely unattained (ceiling 0.852). |
| 2 | §3.8 | "the constructive bound of 91.59 kt puts the worst-case reading of the boundary **below** the 60-kt flat-cap family" | The v2 sentence had 57.6 < 60. On v3 the bound is 91.59 **> 60**, so the 60-kt rules are robust in the worst case. The number was swapped, the direction was not. |
| 3 | §3.8 | "capping i.i.d. survival at 0.906 and block survival at 0.849" | 0.906 is Table 4's seed; 0.849 is the *crossing sweep's* seed (0.852 in Table 4). Both are now stated, with the 0.003 Monte-Carlo difference named. |
| 4 | §3.8 | the mechanism for the ceiling ("the 1992 draw recurs with probability 1/24 per year, capping…") | Does not follow: a 1/24 recurrence over 20 years would cap survival at (23/24)²⁰ = 0.427, not 0.906. The measured mechanism replaced it: 2 of 24 residuals are worse than −172.5 kt (fatal from the LRP under zero catch), which is why failure is concentrated in the first year (immediate-breach probability 0.083 of a total 0.094), and the same draw is harmless once the stock has grown past ~1020 kt. |
| 5 | §2.3, §3.6, Code availability | "the whole analysis was also computed under δ = 1"; Fox cells quoted as if tabulated; the constructive bound called "unaffected" without a value; Code availability naming the **v24** verification script | Only the primary runner and its outputs are archived that way. The three Fox cells are real but are *not* in Table 2 — now labelled. The Allee constructive rises (196.06 − 80.87 = 115.2 kt; 123.3 kt on the declared-strength row), so 91.59 holds a fortiori. The script is `..._v29_verification.py`. |

Two smaller coherence repairs: the 20-year survival at the constructive bound
was printed **twice** in one paragraph, once as 0.84 and once as 0.85 (it is
0.844 → 0.84; the conclusions echoed the 0.85), and the abstract said the
class-vacuity reading "reverses" where the rest of the paper says it
"narrows". Also corrected: the grid-vs-interval note's "every other cell
agrees to about 0.03 kt" — measured, the 72 finite-horizon cells differ by at
most 0.055 kt and the four non-trivial \(T = \infty\) cells differ by 0.14,
0.30, 0.58 and 0.90 kt; and the note now says it reproduces the registered row
on the same grid, which is what makes the two engines comparable at all.

**Every repaired claim is now recomputed, not asserted** — 33 new battery
checks (R17/R18) read the campaign CSVs back and check *both* directions
(artifact → printed value, and printed value → artifact). The one-sided
version of that test was caught by the sabotage harness: mutating "at most
0.06 kt" to "at most 0.6 kt" stayed green, because "measured ≤ stated" is
satisfied by a stated value that is far too loose.

Current state: battery **261 / 0**; basis audit **124 declared, 0 on v2, 0
unexplained**; sabotage **78 mutations / 0 holes** behind a green control;
compiles at 22 pages with 0 overfull boxes (the same 4 underfull hboxes in the
Data-availability paragraph). All three scripts were re-run from the archived
copy in `repo/arena agent 1/paper rewrites/latex/`.

## 11. The consolidation pass -- merits, novelty, impact, presentation

What remained after the prose read was not cosmetics. Chasing one reasoning
error turned the paper from a computed case study into a characterised one,
and that is what separates a specialist-journal report from a general one.

### 11.1 The defect that started it

Result 3.4 stated the criterion for the surplus-proportional family holding the
whole safe set as \((1-\phi)g_{\max} > |e|\), i.e. \(\phi < 0.727\). That is the
criterion for the kernel being **nonempty**, not for it being the **whole safe
set**; the latter is \((1-\phi)g(K^*) \ge |e|\), i.e. \(\phi \le 0.531\). The
margins are therefore 48.5 / 5.4 / −37.8 kt, not 141.2 / 67.2 / −6.8 kt: at
\(\phi = 0.50\) the family holds the LRP by **5.4 kt, not 67.2 kt**, a
twelve-fold overstatement of the one number that made the reactive family look
comfortable.

Every printed verdict was correct, which is why 261 numeric checks missed it:
no member of the declared family \(\{0.25, 0.50, 0.75\}\) falls in the band
\(0.531 < \phi < 0.727\). The family is now extended by \(\phi = 0.60\), whose
informative kernel is \([1074.8, 10^4]\) kt --- viable, but not from the
reference point --- so Table 1 exhibits all three regimes. The correction is
stated in the paper, not silently applied.

### 11.2 Novelty: the table is now a theorem

On the increasing branch of the surplus curve (the only branch the safe set
occupies, since \(K^* < K/2\)) the entire kernel table reduces to three
constants. New Section 2.4 states them as four propositions with one-line
proofs, each verified cell by cell against the committed artifacts by
`campaign_e2_structure_v3.py` (23/23):

| what | statement | verification |
|---|---|---|
| **C\*** | \(g(K^*) - |e| = 91.59\) kt: the largest catch holding the LRP from itself; **any** rule's protection margin is exactly \(C^* - C(K^*)\) | the T=1 boundary is 884.6 exactly when the margin is ≥ 0, checked at eight catches including the knife edge 91.594 (margin 0.00) |
| **C_vac** | \(g_{\max} - |e| = 215.2\) kt, with \(b_\infty = \max(K^*, s_-(C))\): the largest constant catch whose \(T=\infty\) kernel is nonempty | reproduces all six of Table 1's flat-cap cells to 0.1 kt in closed form |
| **three regimes** | reactive family: whole safe set iff \(\phi \le 0.531\); nonempty iff \(\phi < 0.727\) | the five-member sweep matches the closed form at every \(\phi\) |
| **T\*** | \(\max\{T : F^T(S_{hi}) \ge K^* + r_T\}\) | reproduces 6 / 6 / 7 exactly for both policies and all three classes |

The second column of the first row is the one that matters for the paper's
argument. **At the reference point, harvest and protection are one budget.**
The no-dominance verdict therefore stops being an empirical finding about five
tabulated rules and becomes structural: a reactive rule cannot out-supply a
flat cap it matches in protection, because at that point the two are the same
quantity. That is the difference between "no rule won" and "no rule can win".

### 11.3 Merits: the pinned-K objection, answered rather than declared

`campaign_e2_identification_v3.py` (all checks green) does four things:

1. **Profile likelihood over K**, refitting \(r\) in closed form at each \(K\)
   and extending the grid to 50,000 kt *because* the committed value sits on
   the box. The 95% profile set runs from 1500 kt to the top of the grid:
   **K is not identified from above at all**, and the pin costs 2.7% of the
   criterion (SSE ratio 1.027). But across the set, \(g(K^*) \in [148.8,
   176.1]\) kt and \(C^* \in [67.9, 95.2]\) kt --- the functionals are
   identified to ±15% by data that do not determine K --- and \(F' > 1\) for
   every set member at or above \(2K^* = 1769.2\) kt (smallest expansive grid
   value 1775 kt), which is the condition Table 3 already declares.
2. **Joint (r, K) bootstrap**: the published band conditions the pin away by
   refitting \(r\) alone; the joint band is wider (\(C^* = 88.1\) kt
   \([-5.6, 130.6]\) in the expansive regime) and \(F' > 1\) throughout it.
3. **Observation error made quantitative** (the paper's own declared
   conflation): \(C^* = 91.6 \to 112.1\) kt as the observation share goes
   0 → 0.5, so the reported bound is the conservative end.
4. **Recent windows** (impact, below).

### 11.4 Impact: the question the paper had left open

The fit window spans the 1992 collapse, so \(r\) averages two productivity
regimes. New Section 3.12 and Table 7 refit the same object on post-moratorium
windows:

| window | n | r | K | g(LRP) | C\* | worst-floor C\* | F′ |
|---|---|---|---|---|---|---|---|
| 1983–2007 (frozen) | 24 | 0.237 | 5000 (ub) | 172.5 | 91.6 | −156.5 | 1.153 |
| NCAM 1995–2015 | 20 | 0.273 | 5000 (ub) | 198.9 | 171.4 | 166.4 | 1.176 |
| NCAM 1995–2007 | 12 | 0.390 | 5000 (ub) | 284.0 | 274.0 | 271.2 | 1.252 |
| xteNCAM 1995–2024 | 29 | 0.431 | 472 (lb) | 49.4 | 8.0 | −38.8 | 0.927 |
| xteNCAM 2005–2024 | 19 | 0.444 | 472 (lb) | 50.9 | −7.7 | −37.9 | 0.925 |

**Self-viability is regime-dependent**: comfortable on the assessment series
after the moratorium (171 kt, and still 166 kt under that window's worst
floor --- the post-moratorium decline was smooth, so the one-step residual SD
falls from 114.9 to 18.9 kt), and at best marginal on the modern series
(\(0 \pm 8\) kt, negative under its worst floor). The expansion
classification moves with it (\(F' = 0.925 < 1\): on the modern series in its
recent state the loop *contracts* at the reference point and the contraction
form of the certified-layer conversion is the applicable one).

The caveats are stated in the paper rather than buried: the windows are short
(12–29 transitions) and in three of the four K sits at a bound, so these are
regime readings, not productivity estimates.

### 11.5 Presentation

* Title re-cut around the result: *A harvest--protection budget at the limit
  reference point: robust viability of Northern cod (NAFO 2J3KL) under
  persistent productivity shocks.*
* Abstract re-cut the same way, and shortened from 324 to 299 words.
* Two new figures (`make_figs_v18.py`; Figures 1–7 regenerated byte-identical):
  Figure 8 shows the budget line with every policy on it and the three reactive
  regimes; Figure 9 shows the K profile and the identified functionals.
* The paper grew from 22 to 25 pages.

### 11.6 Verification after the pass

Battery **301 / 0**; basis audit **157 declared, 0 on v2, 0 unexplained**;
sabotage **97 mutations / 0 holes** behind a green control; compiles with
0 overfull boxes (the same four underfull hboxes in the Data-availability
paragraph). All three scripts re-run green from the archived copy.

Two holes the sabotage harness found in the new checks are worth recording,
because both are general: (i) a value printed at two or more sites survives a
single-site corruption under a presence test --- 215.2 appears four times, so
the check pins the arithmetic, the caption phrase **and** the site count;
(ii) `"\pm 8"` is a substring of `"\pm 80"`, so a raw `in` test is not a
number test --- `has()` carries the digit boundaries.

### 11.7 What is still open

The commit (§8.2). The manifest is updated to 66 files and the commit message
carries this pass; both need a full clone as before.
