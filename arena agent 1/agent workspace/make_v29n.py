#!/usr/bin/env python3
"""v29n: carry Figure 10 (the cadence figure) into the paper.

The horizon-in-catch invariance is the paper's most applied result and it was
carried by a nine-row table alone. A figure states it in one glance: the
horizon is flat across the whole admissible range including a moratorium, and
one year of margin growth dwarfs the entire catch range.

N1  insert the figure after Table 2, in Section 3.4;
N2  name its generator in Data availability;
N3  mention it in the Discussion sentence that draws the management
    consequence, so the figure is not an orphan.
"""
import io
import shutil

TEX = "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"
shutil.copy(TEX, "/tmp/v29m_before_fig10.tex")
tex = io.open(TEX, encoding="utf-8").read()
log = []


def sub1(tag, old, new):
    global tex
    n = tex.count(old)
    assert n == 1, "%s: anchor matched %d times, need exactly 1" % (tag, n)
    tex = tex.replace(old, new, 1)
    log.append(tag)


FIG = """
\\begin{figure}[htbp]
\\centering
\\includegraphics[width=\\linewidth]{figs_e2_v3/fig10_cadence.png}
\\caption{The certified horizon is not a property of the policy. (a) The exact
crossing of Proposition 2.4 against the constant catch, under each declared
floor class, at 1-kt resolution: the horizon is \\(6\\) years under the
perpetual-worst and 5th-percentile floors and \\(7\\) under the informative one
for every catch in the shaded admissible range, a moratorium included, and it
shortens only outside the constructive bound (\\(C_{\\mathrm{vac}} = 215.2\\)
kt). Every declared reactive and graded rule lies on the same plateau. Grey
band: the admissible range \\([0, C^*]\\). (b) Why: the erosion margin grows by
\\(379\\)--\\(773\\) kt a year, so a single year's growth exceeds the whole
admissible catch range (\\(C^* = 91.59\\) kt, dashed) by a factor of four at its
smallest. Bars are the growth from year \\(T-1\\) to year \\(T\\), computed from
the same closed form as (a); the horizon curve reproduces all \\(30\\) archived
(catch, floor) pairs exactly. Figure \\ref{}: not used.}
\\end{figure}
"""

# ---------------------------------------------------------------- N1
sub1("N1 Figure 10 inserted after Table 2",
     "215.2 (\\(C_{\\mathrm{vac}}\\)) & 5 & 6 & 6 \\\\\n\\end{longtable}\n",
     "215.2 (\\(C_{\\mathrm{vac}}\\)) & 5 & 6 & 6 \\\\\n\\end{longtable}\n" + FIG)

# ---------------------------------------------------------------- N2
sub1("N2 the generator of Figure 10 is named in Data availability",
     "provenance --- it imports the v3 runner and reads the v3 elevation\n"
     "outputs --- and its output is\n"
     "identical. The structural constants",
     "provenance --- it imports the v3 runner and reads the v3 elevation\n"
     "outputs --- and its output is\n"
     "identical. Figure 10 is produced by\n"
     "\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v19.py}; it re-derives the\n"
     "horizon curve from the same closed form and refuses to write the panel\n"
     "unless every tabulated catch reproduces the archived cadence campaign,\n"
     "so the figure cannot silently drift from the table. The structural\n"
     "constants")

# ---------------------------------------------------------------- N3
sub1("N3 the Discussion consequence points at the figure",
     "Table 2 shows the shelf life cannot be",
     "Table 2 and Figure 10 show the shelf life cannot be")

io.open(TEX, "w", encoding="utf-8").write(tex)
print("\n".join("  " + x for x in log))
print("lines: %d" % tex.count("\n"))
