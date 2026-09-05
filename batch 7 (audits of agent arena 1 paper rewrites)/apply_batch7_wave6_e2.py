#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wave-6 E2 build: paperE2_cod_intervention_v19.md from v18.

Owner directive (wave 6 / Task 76): deep, systematic, granular sentence-level
normalised diff scan of the five preceding versions of each paper (E2: v13-v17
vs final v18) to find anything from those versions worth implementing in the
final.  Scan artefacts: wave6/scan/paperE2_cod_intervention.md + SUMMARY.csv.

Scan verdict for E2 -- exactly ONE unregistered drop worth restoring:

  * Result 3.4's Reason prints the supply-replay values ("BAU 5 kt, S1 10.0
    kt, the cascade 16.3 kt, ...") but, since the v14->v15 source-year
    restructure, no longer says WHY the critical-zone rule's mean is so low
    (its above-LRP cap is 60 kt, its mean is 10.0 kt).  The v13/v14 papers
    carried the explanation: the cut is active in 83% of observed years
    because the stock sat below the LRP for almost the entire training
    window -- a fact about the collapsed-era estimation window, not about the
    rule's post-recovery supply properties.  The drop is not listed in any
    version log or wave record (v13-v16 carry none; v17/v18 logs do not
    mention it).  The arithmetic is re-verified against the committed DFO-2016
    series inside this script: exactly 4 of the 24 replay states (1985,
    1987, 1988, 1989) sit at or above 884.6 kt, so the mean is 60 x 4/24 =
    10.0 kt as printed and the below-LRP share is 20/24 = 83%.

Everything else dropped across v13-v18 is either a recorded docket edit
(v17's dominance-partial-order restructure, v18's MSE relabelling), a
superseded pre-correction number (the v14->v15 source-year correction and the
v15->v16 floor corrections -- restoring them would restore errors), or
content preserved elsewhere in the file (the supply-replay values themselves,
the companion contrasts, the family declarations, the residual description).

Non-destructive: one sentence appended inside Result 3.4's Reason; all tables
byte-identical; no frozen verdict, score, kernel, boundary, or table value
changes; the abstract is untouched; the version log is replaced in place.
"""
import csv
import hashlib
import sys

SRC = "arena agent 1/paper rewrites/paperE2_cod_intervention_v18.md"
DST = "arena agent 1/paper rewrites/paperE2_cod_intervention_v19.md"
DATA = "wave_e_cod/data/ncam_2016_table_a2.csv"

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


# ---------------------------------------------------------------------------
# 0. Data verification (fail-loud, from the committed series)
# ---------------------------------------------------------------------------
rows = list(csv.DictReader(open(DATA, "r", encoding="utf-8")))
vals = {int(r["year"]): float(r["ssb_kt"]) for r in rows}
LRP = 884.6
above_1983_2006 = sorted(y for y in range(1983, 2007) if vals[y] >= LRP)
above_1984_2007 = sorted(y for y in range(1984, 2008) if vals[y] >= LRP)
check(above_1983_2006 == [1985, 1987, 1988, 1989],
      "above-LRP states 1983-2006 = %r" % (above_1983_2006,))
check(above_1984_2007 == [1985, 1987, 1988, 1989],
      "above-LRP states 1984-2007 = %r (convention-robustness)" % (above_1984_2007,))
check(len(above_1983_2006) == 4 and 60 * 4 / 24 == 10.0,
      "S1 mean arithmetic 60*4/24 != 10.0")
check(24 - len(above_1983_2006) == 20 and abs(100 * 20 / 24 - 83.33) < 0.01,
      "below-LRP share != 83%")

# ---------------------------------------------------------------------------
# Edit 1: version log (replaced in place, single-log convention as in v17->v18)
# ---------------------------------------------------------------------------
OLD_LOG_HEAD = "*Version log (v18).* Fixes the registered residual"
NEW_LOG = (
    "*Version log (v19).* Wave-6 owner-directed sentence-level diff scan of the five preceding "
    "versions (v14\u2013v18) against this final: every dropped sentence classified against the recorded "
    "version logs and wave records. One unregistered drop found and restored \u2014 a casualty of the "
    "v14\u2192v15 source-year restructure, never listed in any log: Result 3.4's Reason regains one "
    "explanatory sentence beside the printed supply-replay values, saying why the critical-zone rule's "
    "mean allowed catch (10.0 kt) is so low \u2014 the cut is active in 20 of the 24 replay years (the "
    "stock sat below the reference point in all but the 1985 and 1987\u20131989 states, $83\\%$ of the "
    "window), a fact about the collapsed-era estimation window rather than about the rule's "
    "post-recovery supply properties, with the two regimes not mixed; the arithmetic is re-verified "
    "against the committed DFO-2016 series ($60 \\times 4/24 = 10.0$ kt). All other drops across "
    "v14\u2013v18 are recorded docket edits, superseded pre-correction numbers (the source-year and "
    "floor corrections), the recorded v17 dominance-partial-order restructure, the recorded v18 MSE "
    "relabelling, or content preserved elsewhere in the file (the supply-replay values, the companion "
    "contrasts, the family declarations, the residual description). No frozen verdict, score, kernel, "
    "boundary, or table value changes; Tables 1\u20135 byte-identical; one sentence added, nothing "
    "removed; the abstract is untouched."
)
check(src.count(OLD_LOG_HEAD) == 1, "v18 version-log head not found exactly once")
log_line = next(l for l in src.splitlines() if l.startswith(OLD_LOG_HEAD))
out = sub1(src, log_line, NEW_LOG, "version log")

# ---------------------------------------------------------------------------
# Edit 2: the restored gloss, appended to the supply-replay sentence in
# Result 3.4's Reason (the sentence that prints S1 10.0 kt).
# ---------------------------------------------------------------------------
OLD2 = (
    "and the surplus-proportional family $7.4$/14.7/$22.1$ kt at "
    "$\\phi = 0.25/0.50/0.75$. \u25a1"
)
NEW2 = (
    "and the surplus-proportional family $7.4$/14.7/$22.1$ kt at "
    "$\\phi = 0.25/0.50/0.75$. The critical-zone rule's low mean is a property of the window, "
    "not of the rule: the cut is active in 20 of the 24 replay years (the stock sat below the "
    "reference point in all but the 1985 and 1987\u20131989 states, $83\\%$ of the window), a fact "
    "about the collapsed-era estimation window rather than about the rule's post-recovery supply "
    "properties, and the two regimes are not mixed. \u25a1"
)
out = sub1(out, OLD2, NEW2, "supply-replay gloss")

# ---------------------------------------------------------------------------
# Mechanical checks
# ---------------------------------------------------------------------------
body = "\n".join(l for l in out.splitlines() if not l.startswith("*Version log"))
check(body.count("The critical-zone rule's low mean is a property of the window") == 1,
      "restored gloss not present exactly once in body")
check(body.count("20 of the 24 replay years") == 1, "'20 of the 24 replay years' count != 1")
check(body.count("$83\\%$ of the window") == 1, "'$83\\%$ of the window' count != 1")
check(body.count("1985 and 1987\u20131989 states") == 1, "year token count != 1")
check(body.count("the two regimes are not mixed") == 1, "'two regimes are not mixed' count != 1")
check("S1 $10.0$ kt" in body, "printed supply value S1 10.0 kt no longer present")
check(out.count("\u25a1") == src.count("\u25a1"), "proof-end marker count changed")

src_lines = src.splitlines()
out_lines = out.splitlines()
check(len(src_lines) == len(out_lines),
      "line count changed %d -> %d (expected equal: gloss joins its paragraph)" % (len(src_lines), len(out_lines)))
changed = [i for i, (a, b) in enumerate(zip(src_lines, out_lines), 1) if a != b]
check(changed == [5, 123],
      "unexpected changed lines: %r (expected [5, 123])" % (changed,))

def table_lines(text):
    return [l for l in text.splitlines() if l.lstrip().startswith("|")]

check(table_lines(src) == table_lines(out), "markdown table rows not byte-identical")

check(out.startswith("# Robust viability of the 2J3KL limit reference point"),
      "title header lost")

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)

# re-run idempotence-with-verification
with open(DST, "r", encoding="utf-8") as f:
    dst = f.read()
check(hashlib.md5(dst.encode("utf-8")).hexdigest() ==
      hashlib.md5(out.encode("utf-8")).hexdigest(), "write/read mismatch")
print("OK: wrote %s (%d lines, %d words)" % (DST, len(out_lines), len(out.split())))
print("     md5 = %s" % hashlib.md5(out.encode("utf-8")).hexdigest())
print("     changed lines: %r (version log + the one restored sentence)" % (changed,))
