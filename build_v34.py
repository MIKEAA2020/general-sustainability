#!/usr/bin/env python3
"""Build paper1_assessment_separation_v34.tex from v33:
flow/humanization + remnant fixes + one safe displacement (data requirements -> supplement S9)."""
import sys

src = open('/home/user/paper1_assessment_separation_v33.tex', encoding='utf-8').read()
def rep(old, new, label):
    global src
    n = src.count(old)
    if n != 1:
        print(f"FAIL [{label}]: found {n}, expected 1")
        sys.exit(1)
    src = src.replace(old, new)
    print(f"ok   [{label}]")

# ---- remnant / spelling fixes ----
rep(r"The masking formalised here is the following:",
    r"The masking formalized here is the following:", "formalised")
rep(r"liabilities, floors; The compensation principles are rarely stated as",
    r"liabilities, floors; the compensation principles are rarely stated as", "capital-the")

# ---- redundancy: drop 5th restatement of losslessness ----
bullet = (r"\item" + "\n" +
          r"  \textbf{No aggregate blindness at fixed trajectories.} By Remark 2, at a fixed trajectory the full-cone aggregate is lossless." + "\n")
rep(bullet, "", "lossless-dedup")

# ---- readability: split the long opening paragraph ----
rep(r"critical natural capital whose loss cannot be compensated at any price" + "\n"
    r"(Daly, 1990; Ekins et al., 2003). Its foundation statement in ecological",
    r"critical natural capital whose loss cannot be compensated at any price" + "\n"
    r"(Daly, 1990; Ekins et al., 2003)." + "\n\n"
    r"Its foundation statement in ecological", "intro-split")

# ---- readability: split the long "Established" paragraph ----
rep(r"that the typed operator formalizes here. Static scalarization",
    r"that the typed operator formalizes here." + "\n\n"
    r"Static scalarization", "established-split")

# ---- shorten Figure 1 caption (boundary minutiae already in Section 4.6) ----
caption_old = (r"\caption{The discrepancy region \(\mathcal{Q}\) is the portion of the square \(0 \le s_1, s_2 \le 2\) lying on or above \(s_1 + s_2 = 2\): the closed upper-right triangle with vertices \((0,2)\), \((2,0)\), \((2,2)\), minus the two legs \(s_1 = 2\) and \(s_2 = 2\) (strict boundaries); the vertices themselves are outside \(\mathcal{Q}\), and the axis vertices \((0,2)\), \((2,0)\) are not even limit points of it along the axes. Its interior is \(0 < s_1, s_2 < 2\) with \(s_1 + s_2 > 2\). \textbf{Panel A (\(x < 1\), shown at \(x = 0\)):} the region is the genuine impossibility region \(I = \mathrm{FP}_{\mathrm{agg}}\); the interior witness \((s_1, s_2) = (6/5, 6/5)\) is marked. \textbf{Panel B (\(x \ge 1\), shown at \(x = 1\)):} the same aggregate-versus-floor region is the rescue set \(R\), witnessed by STAGED. The threshold curves \(\rho_1, \rho_2\) are drawn only on the open subregion where \(s_1 > 0\), \(s_2 > 0\) and \(s_2 < 2\) (\(\rho_2 = 0\) when \(s_1 = 0\)). The point \((x, s_1, s_2) = (\tfrac12, \tfrac1{10}, \tfrac1{10})\), which lies outside the \(s\)-plane section, is annotated in Panel A. The region is the rescue set at \(x \ge 1\) and the impossibility region at \(x < 1\); only the latter is a false positive.}")
caption_new = (r"\caption{The discrepancy region \(\mathcal{Q}\) in the floor plane: the closed upper-right triangle above \(s_1 + s_2 = 2\), minus the legs \(s_1 = 2\) and \(s_2 = 2\) (boundary conventions as in Section 4.6). \textbf{Panel A (\(x < 1\), shown at \(x = 0\)):} \(\mathcal{Q}\) is the impossibility region \(I = \mathrm{FP}_{\mathrm{agg}}\), with the interior witness \((s_1, s_2) = (6/5, 6/5)\) marked. \textbf{Panel B (\(x \ge 1\), shown at \(x = 1\)):} the same region is the rescue set \(R\), served by STAGED. The threshold curves \(\rho_1, \rho_2\) bound the FAST-only / both / SLOW-only endorsement zones; the point \((x, s_1, s_2) = (\tfrac12, \tfrac1{10}, \tfrac1{10})\), outside the \(s\)-plane section, is annotated in Panel A.}")
rep(caption_old, caption_new, "fig1-caption")

# ---- displacement: compress data-requirements checklist to a summary ----
dr_old = (r"\textbf{Data requirements for empirical application.} The theorem is a" + "\n"
          r"result about assessment operators on a specified datum. Empirical" + "\n"
          r"application requires, in addition to the typed floors, disturbance set," + "\n"
          r"action set, tube model, and destination maintainability witness of" + "\n"
          r"Section 4.5, the following additional specifications:" + "\n\n"
          r"\begin{enumerate}" + "\n"
          r"\def\labelenumi{\arabic{enumi}.}" + "\n"
          r"\tightlist" + "\n"
          r"\item" + "\n"
          r"  \textbf{Action-set completeness status.} A negative certificate over a" + "\n"
          r"  finite action set proves impossibility only relative to that set. The" + "\n"
          r"  application must state whether \(\mathcal{A}\) is exhaustive, a listed policy menu, a sampled subset, or an inner approximation. If incomplete, the verdict is ``no safe transition exists among the listed actions,'' not ``no safe transition exists.''" + "\n"
          r"\item" + "\n"
          r"  \textbf{Calibration and identifiability data.} Parameter estimates," + "\n"
          r"  uncertainty sets, structural alternatives, validation data," + "\n"
          r"  observation error, model discrepancy, missing-data treatment," + "\n"
          r"  disturbance dependence. A specified disturbance set is necessary but not sufficient; it must be justified, or the verdict marked conditional on model credibility." + "\n"
          r"\item" + "\n"
          r"  \textbf{Policy and authority data.} Who may select each action, what" + "\n"
          r"  information they possess, decision timing, enforcement assumptions," + "\n"
          r"  compliance uncertainty, strategic responses, resource and legitimacy" + "\n"
          r"  constraints." + "\n"
          r"\item" + "\n"
          r"  \textbf{Threshold-uncertainty semantics.} A physical or normative" + "\n"
          r"  floor is rarely known exactly. Distinguish the deterministic floor" + "\n"
          r"  \(s_i(z) \ge 0\) from robust threshold safety \(s_i(z;\theta) \ge 0\)" + "\n"
          r"  for all \(\theta \in \Theta\), and from probabilistic or" + "\n"
          r"  confidence-level versions if admitted." + "\n"
          r"\item" + "\n"
          r"  \textbf{Destination maintainability status.} Whether the destination maintainability witness is established physically, by simulation, or by assumption." + "\n"
          r"\end{enumerate}")
dr_new = (r"\textbf{Data requirements for empirical application.} The theorem is a" + "\n"
          r"result about assessment operators on a specified datum. Empirical" + "\n"
          r"application requires, in addition to the typed floors, disturbance set," + "\n"
          r"action set, tube model, and destination maintainability witness of" + "\n"
          r"Section 4.5, five further specifications: the completeness status of the" + "\n"
          r"action set (whether \(\mathcal{A}\) is exhaustive or merely a listed" + "\n"
          r"menu), calibration and identifiability data, policy and authority data," + "\n"
          r"the threshold-uncertainty semantics, and the destination" + "\n"
          r"maintainability status. The itemized requirements are given in the" + "\n"
          r"Supplementary Material (S9).")
rep(dr_old, dr_new, "data-req-displace")

# ---- update the supplementary pointer to mention S9 ----
rep(r"which also enumerates the machine artifact's 25 checks (S8).",
    r"which also enumerates the machine artifact's 25 checks (S8) and the itemized data requirements for empirical application (S9).",
    "supp-pointer-S9")

# ---- header rev ----
rep(r"% Amin Abaee. Revision v33 (JEDC/elsarticle; editorial scan fixes). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v34 (JEDC/elsarticle; flow, humanization, displacement). Compiles with tectonic, pdflatex, or xelatex.",
    "header-rev")

out = '/home/user/paper1_assessment_separation_v34.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")
