#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wave-6 E3 build: paperE3_edwards_forecast_ladder_v13.md from v12.

Owner directive (wave 6 / Task 76): deep, systematic, granular sentence-level
normalised diff scan of the five preceding versions of each paper (E3: v7-v11
vs final v12) to find anything from those versions worth implementing in the
final.  Scan artefacts: wave6/scan/paperE3_edwards_forecast_ladder.md +
SUMMARY.csv.

Scan verdict for E3 -- exactly ONE unregistered drop worth restoring:

  * Definition 4.1 declares two secondary scores: MAE and "the Brier score
    for 1{H < 660}, interpreted only for origins at or after 2007".  Since
    the v11 restructure the MAE values are printed (Table 4's MAE column and
    the 10.72/10.73 tie) but the Brier values are not printed ANYWHERE --
    a declared score left dangling.  v9/v10 carried them in Section 5.3's
    post-2007 paragraph ("The 660-ft Brier scores are 0.31 (persist), 0.25
    (M1), and 0.19 (oracle)"), which v11's restructure dropped wholesale
    without listing it in the v11 version log (the log lists seven items;
    the post-2007 paragraph is not among them).  The external audits had
    verified exactly these values (grok: "Brier for 1{H<660} only after
    2007. persist 0.31, M1 0.25, oracle 0.19. Secondary, not retention. ...
    Fine."; claude: "small n=16; do not over-read").

  Restored as one paragraph in Section 5.3 (after the M1-retention
  paragraph, before 5.3.1): the Brier values with the misclassification-rate
  naming and the small-n caveat (both already the definition's own), the
  unchanged one-year post-2007 RMSE ranking, the h = 5 subsample reversal
  disclosed "without changing the one-year retention statement" (v10's exact
  honest framing), and the pointer to the committed record.  Every value is
  quoted from the committed results file and matches the v9/v10 frozen
  print; this script re-verifies them against the committed CSV.

Everything else dropped across v7-v12 is a recorded docket edit (v11's
logged restructure items, v12's comparator-kink resolution), an audit-driven
correction, or content preserved elsewhere (the full-sample correlations in
the abstract, the climate table as Table 7, the karst limitations, the
0.986 rating-curve statement).

Non-destructive: one paragraph added; all tables byte-identical; no frozen
verdict, score, or table value changes; the abstract is untouched; v13's
version log is appended after v12's (the stacking convention this file
already follows: v11's log is retained above v12's).
"""
import csv
import hashlib
import sys

SRC = "arena agent 1/paper rewrites/paperE3_edwards_forecast_ladder_v12.md"
DST = "arena agent 1/paper rewrites/paperE3_edwards_forecast_ladder_v13.md"
CSV = "wave_e_edwards/results/rolling_modern_2007.csv"

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
# 0. Data verification (fail-loud, from the committed post-2007 record)
# ---------------------------------------------------------------------------
rows = list(csv.DictReader(open(CSV, "r", encoding="utf-8")))
rec = {(r["model"], int(r["horizon"])): r for r in rows}
def near(a, b, tol=5e-3):
    return abs(float(a) - b) <= tol
check(near(rec[("naive_persist", 1)]["rmse"], 13.09), "persist h1 rmse != 13.09")
check(near(rec[("M1", 1)]["rmse"], 12.16), "M1 h1 rmse != 12.16")
check(near(rec[("M2", 1)]["rmse"], 13.31), "M2 h1 rmse != 13.31")
check(near(rec[("M2_oracle", 1)]["rmse"], 8.03), "oracle h1 rmse != 8.03")
check(near(rec[("naive_persist", 1)]["brier_660"], 0.3125, 1e-9), "persist brier != 0.3125 (0.31)")
check(near(rec[("M1", 1)]["brier_660"], 0.25, 1e-9), "M1 brier != 0.25")
check(near(rec[("M2_oracle", 1)]["brier_660"], 0.1875, 1e-9), "oracle brier != 0.1875 (0.19)")
check(near(rec[("M1", 5)]["rmse"], 17.16), "M1 h5 rmse != 17.16")
check(near(rec[("naive_persist", 5)]["rmse"], 25.10), "persist h5 rmse != 25.10")
check(int(rec[("M1", 1)]["n"]) == 16 and int(rec[("M1", 5)]["n"]) == 12,
      "post-2007 n != 16/12")

# ---------------------------------------------------------------------------
# Edit 1: append v13's version log after v12's (stacking convention of this
# file: v11's log retained at L5, v12's at L7).
# ---------------------------------------------------------------------------
OLD1 = "The v11 narrative remains available as the baseline.\n\n## Abstract"
NEW_LOG = (
    "*Version log (v13).* Wave-6 owner-directed sentence-level diff scan of the five preceding "
    "versions (v7\u2013v12) against this final: every dropped sentence classified against the recorded "
    "version logs and wave records. One unregistered drop found and restored \u2014 a v11 restructure "
    "casualty absent from the v11 log's seven listed items: Section 5.3 regains the post-2007 "
    "secondary-score record that Definition 4.1 declares but that no version since v11 has printed \u2014 "
    "the 660-ft Brier scores $0.31$ (persistence), $0.25$ (M1), and $0.19$ (the oracle) on the $n = 16$ "
    "post-2007 one-year origins, with the one-year RMSE ranking unchanged ($13.09$, $12.16$, $13.31$, "
    "$8.03$ ft) and the $h = 5$ subsample reversal ($17.16$ versus $25.10$ ft) reported without "
    "changing the one-year retention statement, the misclassification-rate and small-$n$ caveats "
    "stated, and the pointer to the committed record "
    "(`wave_e_edwards/results/rolling_modern_2007.csv`) \u2014 every value quoted from that committed "
    "file, identical to the v9/v10 frozen print the external audit verified, and re-verified against "
    "the committed CSV by the build script. All other drops across v7\u2013v12 are recorded docket "
    "edits, audit-driven corrections, or content preserved elsewhere (the full-sample correlations in "
    "the abstract, the climate table as Table 7, the karst limitations, the rating-curve redundancy "
    "statement). No frozen verdict, score, or table value changes; Tables 1\u20138 byte-identical; one "
    "paragraph added, nothing removed; the abstract is untouched."
)
NEW1 = ("The v11 narrative remains available as the baseline.\n\n" + NEW_LOG + "\n\n## Abstract")
out = sub1(src, OLD1, NEW1, "version log append")

# ---------------------------------------------------------------------------
# Edit 2: the restored post-2007 paragraph in Section 5.3, inserted after the
# M1-retention paragraph (which carries the MAE tie) and before 5.3.1.
# ---------------------------------------------------------------------------
OLD2 = ("not separated from zero at this sample size.\n\n"
        "### 5.3.1 Uncertainty on the retention margins (post-freeze layer)")
NEW2 = (
    "not separated from zero at this sample size.\n\n"
    "**The post-2007 secondary-score record.** Definition 4.1's second secondary score is scoped to "
    "the post-2007 origins, where the 660-ft Stage I rule is in force. On those origins ($n = 16$ at "
    "$h = 1$) the committed records give 660-ft Brier scores of $0.31$ (persistence), $0.25$ (M1), and "
    "$0.19$ (the oracle), with the one-year RMSE ranking unchanged ($13.09$, $12.16$, $13.31$, and "
    "$8.03$ ft); at $h = 5$ ($n = 12$) the M1\u2013persistence ordering reverses on the subsample "
    "($17.16$ versus $25.10$ ft), reported without changing the one-year retention statement. The "
    "Brier values are misclassification rates of a coarse annual-mean proxy for the Authority's "
    "10-day rule on a small subsample, reported from the archived records and not over-read; the full "
    "post-2007 sub-sample record ($h = 1$ and $h = 5$) is archived with the analysis code "
    "(`wave_e_edwards/results/rolling_modern_2007.csv`).\n\n"
    "### 5.3.1 Uncertainty on the retention margins (post-freeze layer)"
)
out = sub1(out, OLD2, NEW2, "post-2007 paragraph")

# ---------------------------------------------------------------------------
# Mechanical checks
# ---------------------------------------------------------------------------
body = "\n".join(l for l in out.splitlines() if not l.startswith("*Version log"))
check(body.count("**The post-2007 secondary-score record.**") == 1,
      "restored paragraph lead not present exactly once in body")
for tok in ["$0.31$ (persistence)", "$0.25$ (M1)", "$0.19$ (the oracle)",
            "($13.09$, $12.16$, $13.31$, and $8.03$ ft)",
            "($17.16$ versus $25.10$ ft)",
            "`wave_e_edwards/results/rolling_modern_2007.csv`",
            "misclassification rates of a coarse annual-mean proxy"]:
    check(body.count(tok) == 1, "token not exactly once in body: %r" % tok)
check(body.count("reported without changing the one-year retention statement") == 1,
      "reversal caveat not exactly once")
check("Secondary scores are mean absolute error and the Brier score" in body,
      "Definition 4.1 declaration no longer present")
check("MAE is a tie (10.72 versus 10.73 ft)" in body,
      "the MAE tie statement no longer present")

src_lines = src.splitlines()
out_lines = out.splitlines()
check(len(out_lines) == len(src_lines) + 4,
      "line count %d -> %d (expected +4: blank, log, blank, paragraph+blank)" %
      (len(src_lines), len(out_lines)))

def table_lines(text):
    return [l for l in text.splitlines() if l.lstrip().startswith("|")]

check(table_lines(src) == table_lines(out), "markdown table rows not byte-identical")

# the only insertions: the v13 version-log line and the restored paragraph line
# (blank separator lines are set-indistinguishable from v12's blanks and excluded)
inserted = [l for l in out_lines if l.strip() and l not in set(src_lines)]
check(len(inserted) == 2,
      "expected 2 new non-blank lines (v13 log, restored paragraph), got %d: %r" %
      (len(inserted), [l[:60] for l in inserted]))
removed = [l for l in src_lines if l.strip() and l not in set(out_lines)]
check(len(removed) == 0, "non-blank lines removed from v12: %r" % ([l[:60] for l in removed[:5]],))

check(out.startswith("# Does a one-pool water-balance model improve forecasts"),
      "title header lost")

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)

with open(DST, "r", encoding="utf-8") as f:
    dst = f.read()
check(hashlib.md5(dst.encode("utf-8")).hexdigest() ==
      hashlib.md5(out.encode("utf-8")).hexdigest(), "write/read mismatch")
print("OK: wrote %s (%d lines, %d words)" % (DST, len(out_lines), len(out.split())))
print("     md5 = %s" % hashlib.md5(out.encode("utf-8")).hexdigest())
print("     inserted lines: %d (log + paragraph); removed: 0" % len(inserted))
