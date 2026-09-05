#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wave-5 P2 build: paper2_obstruction_calculus_v10.md from v9.

Owner directive (wave 5): evaluate the registered follow-ups left behind the owner
gate; re-open the ones whose decline reason is outdated.  For P2 the wave-4 record
explicitly left three claude one-line fixes "awaiting the next registered wave":

  1. (claude §1.2) The Section 1.2 sentence "Each theorem exhibits the violating
     constraint, the admissible disturbance, and the quantitative bound ..." is
     false for Theorem 2 (a construction, no bound) and Theorem 5 (a converse-side
     characterization) — and Theorem 3 exhibits the incompatible admissible
     controls, not a disturbance/bound pair.  Scoped honestly.
  2. (claude §6.4) "the least-constrained compatible state" should read "most
     constrained": the inf-q state has least constraint slack.
  3. (claude §6.4) "coarse indicators are admissible exactly when they are constant
     on the safe-control partition ... and no finer" — finer observation never
     hurts, and "exactly when" overstates Theorem 3 (viability can fail for other
     reasons even when fibres stay inside classes).

Non-destructive: three one-line body edits + the version-log splice.  No frozen
result, proof, display, or number changes.
"""
import hashlib
import re
import sys

SRC = "arena agent 1/paper rewrites/paper2_obstruction_calculus_v9.md"
DST = "arena agent 1/paper rewrites/paper2_obstruction_calculus_v10.md"

with open(SRC, "r", encoding="utf-8") as f:
    src = f.read()


def sub1(text, old, new, tag):
    n = text.count(old)
    if n != 1:
        sys.exit("FAIL [%s]: anchor occurs %d times (expected 1): %r" % (tag, n, old[:80]))
    return text.replace(old, new, 1)


# ---------------------------------------------------------------- Edit 1: §1.2
OLD1 = (
    'Throughout, "obstruction" means a *certified* failure. Each theorem exhibits '
    "the violating constraint, the admissible disturbance, and the quantitative "
    "bound that make failure inevitable, for every policy in the declared class."
)
NEW1 = (
    'Throughout, "obstruction" means a *certified* failure. Theorems 1 and 4 each '
    "exhibit the violating constraint, an admissible disturbance, and the "
    "quantitative bound that make failure inevitable, for every policy in the "
    "declared class; Theorems 2 and 3 exhibit the incompatible admissible "
    "controls — the merged observation whose incompatible safe controls certify "
    "emptiness — with no quantitative bound claimed there; and Theorem 5 is the "
    "converse-side characterization of the certification limit itself, not a "
    "failure exhibit."
)

# ---------------------------------------------------------------- Edit 2: §6.4 Timing
OLD2 = (
    "A review interval longer than the worst-case time from the least-constrained "
    "compatible state to constraint violation is an information structure under "
    "which the violation is undetectable in time, whatever the review then "
    "concludes."
)
NEW2 = (
    "A review interval longer than the worst-case time from the most-constrained "
    "compatible state — the minimum-$q$ state, which has the least constraint "
    "slack — to constraint violation is an information structure under which the "
    "violation is undetectable in time, whatever the review then concludes."
)

# ---------------------------------------------------------------- Edit 3: §6.4 Coarseness
OLD3 = (
    "The design consequence is that the observation must separate safety classes, "
    "not states: coarse indicators are admissible exactly when they are constant "
    "on the safe-control partition of the state space, and no finer."
)
NEW3 = (
    "The design consequence is that the observation must separate safety classes, "
    "not states: an indicator is exposed to Theorem 3's obstruction when some "
    "observation fibre crosses the safe-control partition of the state space — "
    "merging states whose safe controls differ is what the theorem certifies — "
    "and keeping every fibre within a single class is what removes that "
    "exposure; finer observation never hurts (it merges nothing the coarser one "
    "did not), though Theorem 3 claims no benefit beyond the removal, and other "
    "mechanisms may still certify nonviability on a finer partition."
)

# ---------------------------------------------------------------- Version log
m = re.search(r"^\*Version log \(v9\)\.\*.*$", src, re.M)
if not m:
    sys.exit("FAIL [log]: v9 version log line not found")
VLOG = (
    "*Version log (v10).* Implements the three one-line fixes that the v9 record's "
    "decline section left \u201cregistered as follow-ups \u2026 awaiting the next "
    "registered wave\u201d \u2014 the owner opened that gate in wave 5; nothing else "
    "changes. (1, claude \u00a71.2) The Section 1.2 sentence \u201cEach theorem "
    "exhibits the violating constraint, the admissible disturbance, and the "
    "quantitative bound \u2026\u201d was false for Theorem 2 (a construction, no "
    "bound), Theorem 3 (the exhibit is the incompatible admissible controls), and "
    "Theorem 5 (a converse-side characterization); it is now scoped by mechanism \u2014 "
    "Theorems 1 and 4 carry the full triple, Theorems 2 and 3 exhibit the "
    "incompatible admissible controls with no quantitative bound claimed, and "
    "Theorem 5 is the certification limit itself, not a failure exhibit. (2, claude "
    "\u00a76.4) The Section 6.4 Timing sentence's \u201cleast-constrained compatible "
    "state\u201d read backwards: the inf-$q$ state has the least constraint slack and "
    "is therefore the most constrained; the phrase is corrected with the gloss. "
    "(3, claude \u00a76.4) The Section 6.4 Coarseness sentence's \u201cadmissible "
    "exactly when they are constant on the safe-control partition \u2026 and no "
    "finer\u201d overstated Theorem 3 in two ways (finer observation never hurts, and "
    "fibre-within-class does not by itself guarantee viability); it is restated as "
    "exposure-to-the-obstruction wording: a fibre crossing the safe-control "
    "partition is what Theorem 3 certifies, keeping fibres within classes removes "
    "that exposure, finer observation merges nothing the coarser one did not, and "
    "other mechanisms may still certify nonviability. All three edits are "
    "presentation-layer wording fixes on Section 1.2 and Section 6.4 prose; no "
    "theorem statement, hypothesis, proof step, display, or number changes."
)

out = src
out = sub1(out, OLD1, NEW1, "s1.2-scope")
out = sub1(out, OLD2, NEW2, "s6.4-timing")
out = sub1(out, OLD3, NEW3, "s6.4-coarseness")
out = sub1(out, m.group(0), VLOG, "vlog")

# ---------------------------------------------------------------- Checks
def check(cond, msg):
    if not cond:
        sys.exit("FAIL [check]: " + msg)


# body = everything after the version log line (log quotes old phrasings)
body = out.split("\n", 3)[3] if out.count("\n") >= 3 else out

check(body.count("least-constrained") == 0,
      "'least-constrained' survives in body (%d)" % body.count("least-constrained"))
check(body.count("most-constrained") == 1,
      "'most-constrained' count != 1 (%d)" % body.count("most-constrained"))
check(body.count("and no finer") == 0,
      "'and no finer' survives in body (%d)" % body.count("and no finer"))
check(body.count("Each theorem exhibits") == 0,
      "'Each theorem exhibits' survives in body")
check(body.count("Theorems 1 and 4 each exhibit") == 1,
      "new §1.2 scoping sentence absent")
check(body.count("exposed to Theorem 3's obstruction") == 1,
      "new coarseness wording absent")
check(body.count("minimum-$q$ state") == 1, "minimum-q gloss absent")
# Theorem 5's own true "exactly when" (abstract + statement) must be untouched
check(out.count("exists exactly when") == 1,
      "Theorem-5 'exists exactly when' count changed (%d)" % out.count("exists exactly when"))
check(out.count("exactly when safe-set membership is constant") == 1,
      "abstract Theorem-5 characterization changed")
# frozen needles: body (excluding version-log lines) counts must equal v9's
import re as _re
def body_of(t):
    return "\n".join(l for l in t.split("\n") if not l.startswith("*Version log"))
src_body, out_body = body_of(src), body_of(out)
for needle in ["(H4.2)", "(H4.1)", "(H4.3)", "EViab", "IRViab", "(H1.2)", "(H1.1)",
               "(H3.3)", "(H3.1)", "\\mathcal{J}", "\\mathcal{I}", "ERViab"]:
    a, b = src_body.count(needle), out_body.count(needle)
    check(a == b, "frozen needle %r body count %d -> %d" % (needle, a, b))
check(out.count("**Theorem 5 (observation-fibre criterion).**") == 1,
      "Theorem 5 header changed")
for hdr in ["**Theorem 1 (finite-time exit certificate).**",
            "**Theorem 2 (epistemic emptiness by admissibility — minimal construction).**",
            "**Theorem 3 (common-action obstruction).**",
            "**Theorem 4 (delayed-information obstruction).**"]:
    check(out.count(hdr) == 1, "header changed: " + hdr)
check(out.startswith("# ") or out.startswith("**"), "file head damaged")

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)

md5 = hashlib.md5(out.encode("utf-8")).hexdigest()
print("OK  wrote %s (%d lines, %d words, md5 %s)"
      % (DST, out.count("\n") + 1, len(out.split()), md5))
