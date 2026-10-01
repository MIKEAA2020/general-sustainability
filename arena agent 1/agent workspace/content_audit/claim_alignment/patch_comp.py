#!/usr/bin/env python3
"""Comp claim boundaries; main and existing supplementary are separate source-specific drafts."""
from pathlib import Path
from difflib import unified_diff
import re
r=Path('/home/user');b=r/'content_audit/claim_alignment';src=r/'papers/paper03_computational_certification_v16.tex';old=src.read_text();s=old
abs0=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',s,re.S);assert len(abs0)==1
(b/'original_abstracts').mkdir(exist_ok=True,parents=True);(b/'original_abstracts'/(src.stem+'.txt')).write_text(abs0[0])
def change(a,z):
 global s
 assert s.count(a)==1,(s.count(a),a[:110]);s=s.replace(a,z,1)
change('advancing observation buys margin at rate\none, dilating post-revelation braking authority buys half a unit of delay\ntolerance per unit, and shared-window authority and the velocity budget buy\nexactly nothing; belief-cell rows extend the sandwich to partial and noisy\nobservation with margins radius-bounded on both the witness and the\ncertificate side.',
       'the audited \\(a=1\\) observation-time margin changes at unit rate;\npost-revelation authority plots are algebraic expressions, not proved\noptimized delay sensitivities. Belief-cell rows yield conditional\none-sided obstructions; an upper sandwich and two-sided margins require\nseparately verified full label and held-policy errors.')
change('the induced pair-delay hierarchy, and the exact redesign sensitivities',
       'the induced pair-delay hierarchy, and the scoped redesign witness')
change('Then:\n\\end{theorem}\n\n\\noindent\\emph{(i) Certified value sandwich.}',
       'Then the following value and sign statements hold under (H1)--(H6):\n\n\\noindent\\emph{(i) Certified value sandwich.}')
change('\\rho_{\\mathcal{H},G} \\le J_{\\mathcal{I}}(T) \\le \\rho_{\\mathcal{H},G}\n+ \\max_{a \\in \\mathscr{S}_G} \\bar{e}_a + \\delta_\\beta + L h_t.\n\\tag{8}\n\\]',
       '\\rho_{\\mathcal{H},G} \\le J_{\\mathcal{I}}(T) \\le \\rho_{\\mathcal{H},G}\n+ \\max_{a \\in \\mathscr{S}_G} \\bar{e}_a + \\delta_\\beta + L h_t.\n\\tag{8}\n\\]\nHere \\(\\delta_\\beta\\) must independently bound the full stored-label\ndiscrepancy in (H6), including any cell-label optimism; a cell position\nradius alone does not supply this bound.')
# The theorem ends after its three clauses, not before them.
change('input model in which the coefficients are exact rational or\ninterval-enclosed piecewise-polynomial data with certified integration,',
       'input model in which the coefficients are exact rational or\ninterval-enclosed piecewise-polynomial data with certified integration,') if False else None
# insert end just before the following proof (anchor checked separately)
start=s.index('\\begin{proposition}[belief-cell certificates]\\label{prop:beliefcells}')
end=s.index('\\end{proof}',start)+len('\\end{proof}')
oldblock=s[start:end]
newblock=r'''\begin{proposition}[conditional belief-cell certificates]\label{prop:beliefcells}
Let each cell label be an explicitly verified outer row enclosure for
its compatible mode--state pairs. With the original bridge's (H6)
checked for these labels, including a separate bound on the full
label discrepancy, the corresponding finite program is linear (or
conic for certified cell support functions) and the lower bound and
positive-margin obstruction of Theorem~\ref{thm:bridge} apply to the
cell-filtration policy class. An upper sandwich requires the same
separately verified (H6) budget and an implementable held-policy
comparison; it does not follow from a cell radius alone. Splitting
cells can change both the row labels and the control-kernel grouping,
so (12) accounts for the latter term only. A safety-margin claim for
a primal witness requires its \emph{actual} held-policy row slack and
an enclosure error no greater than that slack; a dual margin survives
only after all enclosure errors charged by its normalized weights
remain smaller than the margin.
\end{proposition}

\begin{proof}
Every real compatible pair obeys a valid one-sided outer row bound,
so its policy supplies a feasible relaxation; a positive relaxed
optimum obstructs the actual cell-adapted policy class. To turn the
relaxation into an upper value bound, apply the bridge's held-policy
comparison with an independently checked (H6) discrepancy. Splitting
a cell also replaces its label by subcell labels, independently of
any control-kernel subadditivity. For example, with \(\dot x=0\),
\(x\in C=[0,1/2]\), upper facet \(x\le1\), and
\(\beta_x=1-x\), the label \(\sup_C\beta_x+1/4=5/4\)
becomes \(1/2\) on the singleton \(\{1/2\}\) even though the
control kernel is zero. This changes the label term by \(3/4\)
while the kernel term in (12) stays zero. The margin conditions follow
by the row-wise enclosure inequality and nonnegative normalized
dual weights, not by an unverified radius identification.
\end{proof}'''
s=s[:start]+newblock+s[end:]
change('Noisy state cells price in the same units: at \\(\\tau = \\tfrac15\\) the\npair viability witnesses tolerate cell radius up to their worst row slacks\n\\(\\tfrac{31}{1250}\\) and \\(\\tfrac{81}{1250}\\), and the triple\'s\nobstruction certificate survives any state-cell radius \\(\\delta_C <\n\\Gamma(\\tfrac15) = \\tfrac3{50}\\), the margin moving to\n\\(\\tau - \\tfrac7{50} - \\delta_C\\). On the exact-computation companion\'s\ndeadline instance the same law is exact: the radius-\\(\\delta_C\\) cell\ninherits the viability verdict precisely for\n\\(\\delta_C \\le z_0 - (1 + T/2)\\), with the boundary cells zero-slack\n(joint check archived; Abaee, 2026, Exact belief-state computation at scale II).',
       'The audited instance has pair-policy row slacks \\(31/1250\\) and\n\\(81/1250\\) at \\(\\tau=1/5\\) and a triple dual margin \\(3/50\\).\nFor a proposed noisy state cell these numbers can be used as budgets\nonly after its actual held-policy slack and full row-label errors are\nenclosed separately; a nominal position radius is not itself a proof\nof the needed error bound. The companion deadline threshold concerns\nits stated exact-state schedule, not arbitrary noisy state cells.')
start=s.index('\\begin{proposition}[redesign sensitivities]\\label{prop:redesign}')
end=s.index('\\end{proof}',start)+len('\\end{proof}')
s=s[:start]+r'''\begin{proposition}[what the printed redesign witness establishes]\label{prop:redesign}
On the audited \(a=1\) instance the delay threshold is
\(\tau_{\max}=7/50\), with a separate viable equality witness.
The original dual's pooled pre-window kernel vanishes because
\(\sum_j\lambda_j n_j=0\); thus its pre-window dual expression
is insensitive to a shared-control-set enlargement. Its velocity-row
multipliers are zero. These are properties of that certificate, not
an exact viability sensitivity law for arbitrary redesigns.
For \(a>1\), the extrapolated expression
\(\Gamma_a(\tau)=\tau-7/50-(a-1)/2\) and its zero locus are
only algebraic plots of the selected expression, not an optimized
viability threshold or a valid finite-horizon certificate on all
plotted rungs. In particular, the equality-viable assertion for
\(a=2,\tau=16/25\) is false at the fixed horizon \(T=6/5\).
\end{proposition}

\begin{proof}
The \(a=1\) identities and primal equality policy are the original
instance's audited witnesses. For the dilated counterexample, let
\(\lambda=(3/8,5/16,5/16)\); the weighted critical position is
\(34/25+t\) throughout every common-control blind window because
the weighted normals cancel. At \(\tau=16/25\) it equals the
safety ceiling \(2\). For \(s=1/10\) after revelation, even granting
each branch independent control in \(2U\), its weighted position is
at least \(34/25+37/50-2(1/10)^2/2=209/100>2\), at time
\(37/50<T\). Thus some branch exits before the declared horizon.
The former proof's \(\max_{u\in aU}\langle u,n_j\rangle=-a\)
is false (the \emph{minimum} is \(-a\)), and scaling both sides
of \(Fu\le f\) to \(aF u\le af\) leaves \(U\) unchanged; a
representation of \(aU\) instead uses \(Fu\le af\).
\end{proof}'''+s[end:]
change('The rates order the redesign options exactly: observation timing at one,\npost-revelation authority at one half, shared-window authority and the\nvelocity budget at zero.',
       'These formal expression rates must not be interpreted as exact\nredesign effects on the optimized viability boundary.')
change('\\caption{The delay hierarchy under authority dilation:',
       '\\caption{Zeros of the selected algebraic dilation expression, not\ncertified viability thresholds under authority dilation:')
change('(rate one in \\(\\tau\\), rate one half in\n\\(a\\)); the pair delay thresholds',
       '(formal rates only; the \\(a>1\\) equality points are not\nviable under the stated full horizon); the pair delay thresholds')
change('Same assertion\nscript.',
       'The original assertion script checks the plotted expression,\nnot these dilated systems\' optimized thresholds.')
# Balance the theorem after all five statements and before its prose proof.
pos=s.index('\\emph{Proof (the complete steps are Steps 1--6',s.index('\\begin{theorem}[continuous-to-finite]'))
s=s[:pos]+'\\end{theorem}\n\n'+s[pos:]
out=b/'drafts'/src.name;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(s)
(b/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)
# Source-specific companion correction, not a claim about all norm/moment classes.
sup=r/'papers/paper03_computational_certification_v16_supplementary.tex';orig=sup.read_text();d=orig
needle='(the display uses the two-sided moment estimate\nof Step 1, \\( |A_a v - \\int k_a^\\top u^\\pi| \\le \\bar e_a\\), and'
# Locate exactly in original before changing.
assert 'the display uses the two-sided moment estimate\nof Step 1' in d
d=d.replace('the display uses the two-sided moment estimate\nof Step 1, \\(|A_a v - \\int k_a^\\top u^\\pi| \\le \\bar e_a\\), and\n\\(\\beta_a^{+} \\ge \\beta_a\\))',
'''the display needs only the one-sided bound from (3),
\\(A_a v - \\int k_a^\\top u^\\pi \\le \\bar e_a\\), and
\\(\\beta_a^{+} \\ge \\beta_a\\). The reflected error can be larger
than \\(\\bar e_a\\), so an absolute-value bound is not inferred)''',1)
o=b/'drafts'/sup.name;o.write_text(d)
(b/'diffs'/(sup.stem+'.diff')).write_text(''.join(unified_diff(orig.splitlines(True),d.splitlines(True),fromfile=str(sup),tofile=str(o))))
print(o)
