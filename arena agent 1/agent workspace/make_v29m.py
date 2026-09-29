#!/usr/bin/env python3
"""v29m: three prose defects the cadence pass left behind.

M1  Data availability declares generators for Figures 1--7 only, but the
    paper includes nine; Figures 8 and 9 are written by make_figs_v18.py.
    The cadence insertion also orphaned the "it supersedes make_figs_v16.py"
    clause, which now reads as if it described the cadence campaign.

M2  The mechanism sentence says the margin's year-on-year increments exceed
    the admissible catch range "from the fourth year".  Every one of them
    does, the smallest (379 kt) by a factor of four over 91.59 kt, so the
    sentence understates the result it is explaining.

M3  The paper prints "33 (catch, class) pairs".  The campaign tries 30
    constant-catch pairs and 18 declared-rule pairs: 48 in total.
"""
import io
import shutil

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
shutil.copy(TEX, "/tmp/v29l_before_prose.tex")
tex = io.open(TEX, encoding="utf-8").read()
log = []


def sub1(tag, old, new):
    global tex
    n = tex.count(old)
    assert n == 1, "%s: anchor matched %d times, need exactly 1" % (tag, n)
    tex = tex.replace(old, new, 1)
    log.append(tag)


# ---------------------------------------------------------------- M1
sub1("M1a orphaned 'supersedes' clause restored to the figure sentence",
     "Figures 1--7 are produced by\n"
     "\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v17.py};\n"
     "the structural constants of Section 2.4",
     "Figures 1--9 are produced by\n"
     "\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v18.py}, which adds the two\n"
     "structural panels to the seven of\n"
     "\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v17.py} without changing them;\n"
     "\\texttt{v17} superseded \\texttt{make\\_figs\\_v16.py} only in\n"
     "provenance --- it imports the v3 runner and reads the v3 elevation\n"
     "outputs --- and its output is\n"
     "identical. The structural constants of Section 2.4")
sub1("M1b the orphaned tail removed from the cadence clause",
     "(outputs in \\texttt{src/results\\_cadence\\_v3/}); it supersedes\n"
     "\\texttt{make\\_figs\\_v16.py} only in provenance --- it imports the v3\n"
     "runner and reads the v3 elevation outputs --- and its output is\n"
     "identical. The three Section 3.6 form rows",
     "(outputs in \\texttt{src/results\\_cadence\\_v3/}). The three Section 3.6\n"
     "form rows")

# ---------------------------------------------------------------- M2
sub1("M2 the mechanism says what is true of every increment",
     "kt, so from the fourth year a single year's growth\n"
     "exceeds the entire admissible catch range \\([0, 91.59]\\) kt. Certified",
     "kt, so every one of them exceeds the entire\n"
     "admissible catch range \\([0, 91.59]\\) kt --- the smallest by a factor\n"
     "of four --- and no reduction inside that range can add a certified year.\n"
     "Certified")

# ---------------------------------------------------------------- M3
sub1("M3 the pair count corrected to the 48 the campaign tries",
     "the same \\(33\\) (catch, class) pairs confirm the crossing against the\n"
     "committed kernel computation.",
     "the crossing agrees with the committed kernel computation at all\n"
     "\\(48\\) (rule, class) pairs the campaign tries --- \\(30\\) constant\n"
     "catches and \\(18\\) declared rules.")

io.open(TEX, "w", encoding="utf-8").write(tex)
print("\n".join("  " + x for x in log))
print("lines: %d" % tex.count("\n"))
