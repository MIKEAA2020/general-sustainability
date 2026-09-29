#!/usr/bin/env python3
"""v29j -- the cadence pass.

The certified horizon was reported in the paper as a property of the
conversion's expansive form and then set aside.  It is the paper's most usable
applied result and it was being wasted, because the natural question was never
asked: can a manager buy certified years by fishing less?  Under a contraction
the answer would be yes without bound.  Here it is no --

  the horizon is 6 years under the perpetual-worst and 5th-percentile floors
  and 7 under the informative one, for EVERY constant catch from zero to
  150 kt, the moratorium included, and for every declared reactive and graded
  rule as well.  Catches above 150 kt shorten it (6 years under the
  informative floor from 180 kt; 5 under the perpetual-worst floor from
  200 kt); no policy lengthens it.

because the erosion margin's year-on-year increments (379, 437, 504, 582,
671, 773 kt) exceed the whole admissible catch range from the fourth year on.
A robustness certificate therefore has a shelf life that cannot be extended by
conservation, and any interval at which the reference point is re-assessed has
to sit inside it.  That is stated here and anchored to two real institutional
cadences (the IWC's six-year Implementation Reviews; NOAA's management-track
cycles, which for some stocks run to a decade).

J1  Section 2.4: the constants are not Schaefer-specific (verified on the Fox
    and both Allee rows of Section 3.6).
J2  Section 3.4: the horizon is invariant to the catch.
J3  Discussion: what that means for the review interval.
J4  Abstract and conclusions: the same claim, once each.
J5  Data availability: the campaign that establishes it.
"""
import io
import sys

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
BAK = "/tmp/v29i_before_cadence.tex"
B = chr(92)

tex = io.open(TEX, encoding="utf-8").read()
orig = tex
EDITS = []

# ---------------------------------------------------------------- J1
EDITS.append((
    "The crossing reproduces the computed horizons exactly --- "
    + B + "(T^* = 6" + B + ") under",
    """Nothing in this subsection uses the Schaefer form. The only properties
invoked are that the surplus is unimodal with its peak above the reference
point and that the safe set lies on the increasing branch, so the constants
travel to any surplus function with those two properties. They do: on the
Fox row of Section 3.6 the formula \\(C^* = g(K^*) - |e|\\) gives
\\(79.1\\) kt against the tabulated \\(79.05\\), with
\\(C_{\\mathrm{vac}} = 111.2\\) kt and \\(g_{\\max} = 192.0\\) kt; on the
two Allee rows it gives \\(123.27\\) kt (declared \\(s_0\\)) and
\\(115.19\\) kt (data-preferred), both reproducing the tabulated constructives
exactly. The Schaefer numbers of Section 3.3 are one instance of a statement
that holds across the forms the paper fits.

The crossing reproduces the computed horizons exactly --- """
    + B + "(T^* = 6" + B + ") under"))

# ---------------------------------------------------------------- J2
EDITS.append((
    'while leaving ' + B + '(a_{\\max}' + B + ') unchanged.',
    """The horizon is not a property of the policy, and that is the second
thing the crossing shows. Table 8 gives \\(T^*\\) against the constant catch.
It is 6 years under the perpetual-worst and 5th-percentile floors and 7 under
the informative one for every catch from zero to \\(150\\) kt --- the
moratorium included --- and for every declared reactive and graded rule as
well; the same \\(33\\) (catch, class) pairs confirm the crossing against the
committed kernel computation. Only catches outside the constructive bound
shorten it: \\(6\\) years under the informative floor from \\(180\\) kt and
\\(5\\) under the perpetual-worst floor from \\(200\\) kt. No declared policy
lengthens it. The reason is the one the formula exposes: the margin's
year-on-year increments are \\(379\\), \\(437\\), \\(504\\), \\(582\\),
\\(671\\) and \\(773\\) kt, so from the fourth year a single year's growth
exceeds the entire admissible catch range \\([0, 91.59]\\) kt. Certified years
cannot be bought with conservation; the horizon is set by the expansion rate
at the reference point and by nothing the manager chooses.

\\textbf{Table 8.} The certified horizon \\(T^*\\) by constant catch, under
each declared floor class.

\\begin{longtable}[]{@{}
  >{\\raggedright\\arraybackslash}p{(\\columnwidth - 6\\tabcolsep) * \\real{0.2500}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 6\\tabcolsep) * \\real{0.2500}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 6\\tabcolsep) * \\real{0.2500}}
  >{\\raggedleft\\arraybackslash}p{(\\columnwidth - 6\\tabcolsep) * \\real{0.2500}}@{}}
\\toprule\\noalign{}
\\begin{minipage}[b]{\\linewidth}\\raggedright
Constant catch (kt)
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
perpetual-worst
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
5th pct.
\\end{minipage} & \\begin{minipage}[b]{\\linewidth}\\raggedleft
10th pct.
\\end{minipage} \\\\
\\midrule\\noalign{}
\\endhead
\\bottomrule\\noalign{}
\\endlastfoot
0 (moratorium) & 6 & 6 & 7 \\\\
5 (BAU) & 6 & 6 & 7 \\\\
60 (flat cap) & 6 & 6 & 7 \\\\
91.59 (\\(C^*\\)) & 6 & 6 & 7 \\\\
120 & 6 & 6 & 7 \\\\
150 & 6 & 6 & 7 \\\\
180 & 6 & 6 & 6 \\\\
200 & 5 & 6 & 6 \\\\
215.2 (\\(C_{\\mathrm{vac}}\\)) & 5 & 6 & 6 \\\\
\\end{longtable}

while leaving \\(a_{\\max}\\) unchanged."""))

# ---------------------------------------------------------------- J3
EDITS.append((
    "Two layers of negative content must be kept distinct.",
    """The horizon has a management consequence that is easy to miss while it
is being read as a limitation of the method. A robustness certificate for a
reference point has a shelf life, and Table 8 shows the shelf life cannot be
extended by fishing less: it is six or seven years for every admissible
catch, including none at all. Any interval at which the reference point is
re-assessed therefore has to sit inside it, or the certificate on which the
reference point's defence rests has already expired when it is consulted.
Two real cadences bracket that. The IWC schedules an Implementation Review of
its Revised Management Procedure ``normally'' every six years, and its
aboriginal subsistence strike limits are set in six-year blocks; NOAA's
management-track assessments run on cycles of one to three years for many
stocks, but for others ``a decade may pass before an assessment is
conducted.'' A decadal cadence is outside the horizon computed here; a
six-year one sits exactly at it, and only a cycle shorter than six years is
comfortably inside. The same arithmetic says what would move the horizon:
it is set by the expansion rate \\(F'(K^*)\\), so neither better data about
the disturbance nor a more cautious catch extends it --- only a reference
point low enough that the governed map contracts there, or a policy that
changes the map's shape rather than its level.

Two layers of negative content must be kept distinct."""))

# ---------------------------------------------------------------- J4
EDITS.append((
    "overtakes the worst-case trajectory. (4) Carrying capacity",
    """overtakes the worst-case trajectory, and which no catch reduction
extends: it is the same for every admissible catch, including none at all.
(4) Carrying capacity"""))

EDITS.append((
    "\\item\n  The comparison is governed by an identity rather than by a tabulation:",
    "\\item\n  The certificate has a shelf life, and it cannot be bought. The\n"
    "  certified horizon is six or seven years for every declared policy and\n"
    "  every constant catch from zero to " + B + "(150" + B + ") kt --- the\n"
    "  moratorium included --- because the erosion margin's annual growth\n"
    "  exceeds the whole admissible catch range from the fourth year on. A\n"
    "  review interval longer than that horizon is consulting an expired\n"
    "  certificate.\n"
    "\\item\n  The comparison is governed by an identity rather than by a tabulation:"))

# ---------------------------------------------------------------- J5
# The data-availability anchor carries an \allowbreak{} breakpoint, so it is
# matched on the parenthesised output clause instead of on the path.
EDITS.append((
    "(outputs in " + B + "texttt{src/results" + B + "_ident" + B + "_v3/});",
    "(outputs in " + B + "texttt{src/results" + B + "_ident" + B + "_v3/}); the "
    "horizon-in-catch invariance of Table 8 and the form-generality of "
    "Section 2.4 by\n" + B + "texttt{wave" + B + "_e" + B + "_cod/src/" + B
    + "allowbreak{}campaign" + B + "_e2" + B + "_cadence" + B + "_v3.py} "
    "(outputs in " + B + "texttt{src/results" + B + "_cadence" + B + "_v3/});"))

for i, (old, new) in enumerate(EDITS, 1):
    n = tex.count(old)
    if n == 0 and " ".join(new.split()) in " ".join(tex.split()):
        print("J%d already applied -- skipped" % i)
        continue
    if n != 1:
        sys.exit("J%d: anchor matched %d times (expected 1); aborting" % (i, n))
    tex = tex.replace(old, new, 1)
    print("J%d applied" % i)

if tex == orig:
    print("nothing to do")
    sys.exit(0)
io.open(BAK, "w", encoding="utf-8").write(orig)
io.open(TEX, "w", encoding="utf-8").write(tex)
print("backup ->", BAK)
print("lines %d -> %d" % (orig.count("\n") + 1, tex.count("\n") + 1))
