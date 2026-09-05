#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wave-5 E1 build: paperE1_cod_forecast_ladder_v12.md from v11.

Owner directive (wave 5): evaluate the registered follow-ups left behind the
owner gate.  Two of E1's registered methodological asks are re-opened because
their recorded decline reason ("new computations/analyses, not corrections;
they need a scored campaign, not an edit") is mis-stated for them -- each is a
presentation-layer collection of values the article already prints:

  1. (claude priority 5) the parameter table: "fitted r, K, s, phi and which
     bounds were hit" -- implemented in the P5-Table-3 pattern: a table of the
     fitted values AS PRINTED (source sections named), with the unprinted
     members (per-origin rolling fits, M3's per-window b, M4's setting)
     explicitly marked as archive items.  New Section 3.6 + Table 10 + a
     Section 2.2 pointer.
  2. (claude A7, the constructive half that v10's label fix left buried) the
     positive reading of the M4-vs-persistence decomposition: the one-year
     information delay costs 86.4 kt at h=1 on Specification A -- more than the
     entire structural cost of any delay-free module (23/17/46/37 kt over
     timely persistence, one-line subtractions of Table 4's printed values) and
     more than M4's own structure-given-delay cost of 11.1 kt; the stale
     control 184.4 kt still beats only the delay-carrying M4.  One sentence
     added to Section 4's decomposition paragraph.

Still registered (reasons still valid): the drift/damped-trend baseline, the
leave-one-origin-out influence, the Table-6 forecast explanation, the M3/M4
609/586 deterioration explanation (all new computations); the log-RMSE
demotion (the v11 floor disclosure answers it without dropping a recorded
score column from frozen Table 4).

Non-destructive: all pre-existing tables byte-identical; the abstract
untouched (300 words pinned); Table 10 quotes only values already printed.
"""
import hashlib
import re
import sys

SRC = "arena agent 1/paper rewrites/paperE1_cod_forecast_ladder_v11.md"
DST = "arena agent 1/paper rewrites/paperE1_cod_forecast_ladder_v12.md"

with open(SRC, "r", encoding="utf-8") as f:
    src = f.read()


def sub1(text, old, new, tag):
    n = text.count(old)
    if n != 1:
        sys.exit("FAIL [%s]: anchor occurs %d times (expected 1): %r" % (tag, n, old[:80]))
    return text.replace(old, new, 1)


def check(cond, msg):
    if not cond:
        sys.exit("FAIL [check]: " + msg)


# ---------------------------------------------------------------- Edit 1: §2.2 pointer
OLD1 = (
    "The reported fits attain the upper endpoint ($K = 5000$ kt) where the data "
    "prefer an unbounded carrying capacity; M1b's recovery-window $K = 105.9$ kt "
    "is a valid interior fit, not a bound violation."
)
NEW1 = (
    "The reported fits attain the upper endpoint ($K = 5000$ kt) where the data "
    "prefer an unbounded carrying capacity; M1b's recovery-window $K = 105.9$ kt "
    "is a valid interior fit, not a bound violation. Every fitted-parameter "
    "value this article prints, with the window it belongs to and the bound it "
    "attains, is collected in Table 10; the per-origin rolling fits and the "
    "parameters the article does not print are archive items, marked there as "
    "such."
)

# ---------------------------------------------------------------- Edit 2: §3.6 + Table 10
OLD2 = "\n## 4. Discussion\n"
S36 = """
### 3.6 Fitted parameters as printed (post-freeze presentation layer)

This section collects in one place every fitted-parameter value the article prints, the window or treatment it belongs to, and the bound it attains. It is a presentation layer over values already printed at their source sites — nothing is recomputed, no value is new, and quantities the article does not print (the per-origin rolling fits of every module, the index module's per-window exponent $b$, and the one-year delay module's structural setting) are marked as archive items rather than invented. The collection exists so the identification record — bounds attained, interior fits, the flat valley — can be read at a glance.

**Table 10.** Fitted parameters as printed (source sites in parentheses; values quoted verbatim from the text).

| Module | Window / treatment | Values as printed | Bound / identification status |
|---|---|---|---|
| M1 | Collapse, Specification A (train 1983–1990) (§1, §4) | $r = 1.935$, $K = 1032.7$ kt, constant catch $240$ kt; repeller $144$ kt, attractor $889$ kt, monotone below $783$ kt, $F'(S^*) \\approx -0.39$ | §3.1 records the collapse-window fitted $r$ as saturating at the upper bound ($\\approx 2$), quoted as printed |
| M1 | Recovery, annual landings (§3.2) | $r = 0.458$, constant catch $3.19$ kt (the 1995–2007 landings mean); training SSE $128.35$ kt² | $K$ pinned at its lower bound, $500.0$ kt |
| M1 | Recovery, coarse catch regime (§3.2) | $r = 0.370$, constant catch $5.0$ kt (the training mean); training SSE $127.84$ kt² | $K$ pinned at its upper bound, $5000.0$ kt |
| M1b | Recovery, annual landings (§2.2, §3.2) | $K = 105.9$ kt | $r$ pinned at its upper bound in both treatments; $K$ a valid interior fit |
| M1b | Recovery, coarse catch regime (§3.2) | $K = 129.8$ kt | (same row's treatment) |
| M1b | Recovery-stall, Specification B (train 1995–2012) (§3.3) | $\\mathfrak{s} = 5.3\\times10^{-3}$, $K = 500$ kt, training-window maximum $117$ kt | declared identification fragility: $\\mathfrak{s}$ small, $K$ extrapolated far beyond the training range |
| M3 | Rolling, Specification A (§3.1) | $\\phi = 0.95$ (AR(1) residual coefficient) | printed value; the per-window rolling $\\phi$ values are archive items |
| M3 | Index module (§3.4) | $r$, $K$, $b$ fitted jointly by one-step least squares | fitted values not printed (archive); degrees-of-freedom note at $n = 8$ training years |
| M1 / M1b | Flat-valley sweep, recovery window (§3.2) | $K$ fixed anywhere on $[60, 5000]$ kt moves the one-step training objective only from MSE $127.4$ to $149.9$ kt² (training RMSE $11.29$–$12.24$ kt) while $r$ compensates over $[0.435, 0.773]$ | the $(r, K)$ pair is not identified on this window; the ordering of valley variants is not a robust ranking |
| M4 | Rolling, all specifications | no fitted parameters; the one-year assessment delay is structural | archive: the module carries no fitted values to print |
| All modules | Per-origin rolling fits | archive items (not printed); M1b's Specification B rolling Allee optimum is environment-sensitive at the ±17 kt level (§Data availability) | — |

Bounds, as declared in Section 2.2: $r \\in (0.001, 2]$; $K$ optimised on $[\\max_{\\mathrm{train}} S + 10, 5000]$ kt with $500$ kt the multi-start initialiser rather than the lower bound, and $K$ constrained above the training-window maximum throughout. The table's rows quote the source sections' own phrasing where the two differ (Section 2.2's bound declaration and Section 3.2's pinned-fit record are both as printed; neither is reconciled here).

## 4. Discussion
"""

# ---------------------------------------------------------------- Edit 3: §4 constructive finding
OLD3 = (
    "at $h = 1$ the surplus model's own penalty is only about 11 kt — the "
    "delay, not the structure, separates M4 from persistence — while at $h = 5$ "
    "on Specification B the model's own cost dominates (694 of 713 kt)."
)
NEW3 = (
    "at $h = 1$ the surplus model's own penalty is only about 11 kt — the "
    "delay, not the structure, separates M4 from persistence — while at $h = 5$ "
    "on Specification B the model's own cost dominates (694 of 713 kt). Read "
    "constructively, the same printed arithmetic says the value of a timely "
    "assessment exceeds the value of any structure tested: the one-year "
    "information delay costs $86.4$ kt at $h = 1$ on Specification A — more "
    "than the entire structural cost of any delay-free module (M1 $23$ kt, "
    "M1b $17$ kt, M2 $46$ kt, M3 $37$ kt over timely persistence, each a "
    "one-line subtraction of Table 4's printed values) and more than M4's own "
    "structure-given-delay cost of $11.1$ kt — and the stale-persistence "
    "control, $184.4$ kt, still loses at $h = 1$ to every delay-free module "
    "while beating only the delay-carrying M4 ($195.6$ kt)."
)

# ---------------------------------------------------------------- Version log
m = re.search(r"^\*Version log \(v11\)\.\*.*$", src, re.M)
if not m:
    sys.exit("FAIL [log]: v11 version log line not found")
VLOG = (
    "*Version log (v12).* Wave-5 owner-directed re-open pass (the registered "
    "follow-ups behind the owner gate, re-evaluated). Two items re-opened "
    "because their recorded reason — new computations needing a scored "
    "campaign — is mis-stated for them; both are presentation-layer "
    "collections of values already printed. (1, claude priority 5: the "
    "parameter table) New Section 3.6 + Table 10 collect every "
    "fitted-parameter value the article prints, with its window and the bound "
    "it attains, quoting the source sections verbatim; the unprinted members "
    "(per-origin rolling fits, the index module's per-window $b$, M4's "
    "structural setting) are marked as archive items — the P5-Table-3 pattern; "
    "a Section 2.2 pointer routes to it. (2, claude A7's constructive half, "
    "which v10's label fix left unstated) Section 4's decomposition paragraph "
    "gains one sentence: the one-year information delay costs $86.4$ kt at "
    "$h=1$ on Specification A — more than any delay-free module's entire "
    "structural cost over timely persistence ($23$/$17$/$46$/$37$ kt, one-line "
    "subtractions of Table 4's printed values) and more than M4's own "
    "structure-given-delay cost of $11.1$ kt — and the stale-persistence "
    "control ($184.4$ kt) still loses at $h=1$ to every delay-free module "
    "while beating only M4 ($195.6$ kt). Still registered with their recorded "
    "reasons: the drift/damped-trend baseline, the leave-one-origin-out "
    "influence, the Table-6 forecast explanation, and the M3/M4 deterioration "
    "explanation (all new computations); the log-RMSE demotion stays declined "
    "(the v11 floor-and-hit-count disclosure answers it without dropping a "
    "recorded score column from frozen Table 4). No frozen verdict, score, "
    "kernel, or table value changes: Tables 1–9 are byte-identical, Table 10 "
    "is the new presentation layer, and the abstract is untouched at 300 "
    "words."
)

out = src
out = sub1(out, OLD1, NEW1, "s2.2-pointer")
out = sub1(out, OLD2, S36, "s3.6-table10")
out = sub1(out, OLD3, NEW3, "s4-constructive")
out = sub1(out, m.group(0), VLOG, "vlog")

# ---------------------------------------------------------------- Checks
def body_of(t):
    return "\n".join(l for l in t.split("\n") if not l.startswith("*Version log"))


src_body, out_body = body_of(src), body_of(out)

# additions block (for expected-count computation)
ADDED = NEW1.replace(OLD1, "") + S36.replace("## 4. Discussion", "") + \
    NEW3.replace(OLD3, "")

check(out_body.count("### 3.6 Fitted parameters as printed") == 1,
      "Section 3.6 header missing or duplicated")
check(out_body.count("**Table 10.**") == 1, "Table 10 caption missing or duplicated")
check(out_body.count("collected in Table 10") == 1, "Section 2.2 pointer missing")
check(out_body.count("Read constructively, the same printed arithmetic") == 1,
      "constructive sentence missing")
check(out_body.count("archive items") >= 3, "archive-item markers missing")
# every v11 table line survives byte-identically; Table 10 adds exactly 13 lines
src_tbl = [l for l in src.split("\n") if l.strip().startswith("|")]
out_tbl = [l for l in out.split("\n") if l.strip().startswith("|")]
missing = [l for l in src_tbl if l not in out_tbl]
check(not missing, "v11 table line lost: %r" % (missing[:1],))
check(len(out_tbl) == len(src_tbl) + 13,
      "table line count %d -> %d (expected +13)" % (len(src_tbl), len(out_tbl)))
# abstract byte-identical (text without the Keywords line, 300 words pinned)
def abstract_of(t):
    a = t.split("## Abstract", 1)[1].split("\n##", 1)[0]
    return a, " ".join(l for l in a.split("\n")
                       if l.strip() and not l.strip().startswith("**Keywords:**"))
a_src, a_txt = abstract_of(src)
a_out, b_txt = abstract_of(out)
check(a_src == a_out, "abstract changed")
check(len(a_txt.split()) == 300, "abstract word count %d != 300" % len(a_txt.split()))
# printed-value needles: expected = src count + additions count (fail-loud both ways)
NEEDLES = ["1.935", "1032.7", "105.9", "129.8", "5000.0", "500.0", "0.458",
           "0.370", "128.35", "127.84", "149.9", "11.29", "12.24", "0.435",
           "0.773", "3.19", "5.0 kt", "86.4", "184.4", "195.6", "11.1",
           "127.4"]
for n in NEEDLES:
    a, b, d = src_body.count(n), out_body.count(n), ADDED.count(n)
    check(b == a + d, "needle %r: %d -> %d (added %d, expected %d)"
          % (n, a, b, d, a + d))
# frozen verdict rows / DM table intact
for n in ["**Table 9.**", "**Table 4.**", "**Table 6.**", "1898",
          "$\\varepsilon_{\\mathrm{log}} = 10^{-3}$"]:
    check(out.count(n) >= 1, "frozen anchor lost: " + n)
# no stray "Table 11"
check(out.count("Table 11") == 0, "unexpected Table 11")
# section order: 3.6 sits between 3.5 and 4
i35, i36, i4 = (out.find("### 3.5 Uncertainty"), out.find("### 3.6 Fitted"),
                out.find("\n## 4. Discussion\n"))
check(0 < i35 < i36 < i4, "section order broken (%d, %d, %d)" % (i35, i36, i4))

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)

md5 = hashlib.md5(out.encode("utf-8")).hexdigest()
print("OK  wrote %s (%d lines, %d words, md5 %s)"
      % (DST, out.count("\n") + 1, len(out.split()), md5))
