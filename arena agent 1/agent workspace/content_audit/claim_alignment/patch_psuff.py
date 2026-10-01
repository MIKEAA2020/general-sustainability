#!/usr/bin/env python3
"""Aligned psuff draft: exact one-step, sensor optimum and aligned deadline."""
from pathlib import Path
from difflib import unified_diff
import re
root=Path('/home/user');b=root/'content_audit/claim_alignment';src=root/'papers/paper02_probabilistic_sufficiency_v12.tex';old=src.read_text();s=old
abstracts=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',old,re.S);assert len(abstracts)==1
(b/'original_abstracts').mkdir(parents=True,exist_ok=True)
(b/'original_abstracts'/(src.stem+'.txt')).write_text(abstracts[0])
def change(a,z):
 global s
 assert s.count(a)==1,(s.count(a),a[:95]);s=s.replace(a,z,1)
change('\\(V^{\\rho}\\) is the exact \\(\\rho\\)-mixture of the two, recovering\nexpectation at \\(\\rho = 0\\) and the worst-case reading at\n\\(\\rho = 1\\), with an exact closed form on the delayed class',
       'the one-stage contaminated expectation is exact at every radius,\nrecovering expectation at \\(\\rho=0\\) and the worst-case reading at\n\\(\\rho=1\\); a separate prior-contamination model has an exact\nclosed form on the declared delayed hold class')
change('probe law, and the general additive deadline law: the threshold is the\nfloor plus the probe excursion plus drift times deadline, verified on two\ninstances.',
       'probe law, and an additive deadline formula for aligned worst-loss\nhold--probe instances, verified on two specific parameter settings.')
change('the deficit is \\(\\varepsilon\\) for every prior; at',
       'the reading-own policy loses \\(\\varepsilon\\) at every prior,\nwhile for \\(0<\\varepsilon<1/2\\) the optimized deficit is\n\\(\\min\\{\\varepsilon,b(x_1),b(x_2)\\}\\); at')
change('and no map\ndoes better: one of the two actions is fatal at each state whichever\nreading carries it with positive probability. Hence\n\\(\\Delta_{1}(b) = \\varepsilon\\) at every prior, and at',
       'but a constant reading-to-action map may do better at a skew prior.\nEnumerating the four deterministic maps for \\(0<\\varepsilon<1/2\\)\ngives \\(\\Delta_1(b)=\\min\\{\\varepsilon,b(x_1),b(x_2)\\}\\).\nThe reading-own map is optimal at the symmetric prior, and at')
change('for every action \\(a\\) and\nobservation \\(y\\),',
       'for every action \\(a\\) and observation \\(y\\) with\npositive probability under \\(b,a\\) (or with unnormalized zero-mass\nposteriors assigned empty support),')
change('The expected and adversarial readings of Remark \\ref{rem:operators} are\nthe two ends of one exact family.',
       'Remark \\ref{rem:operators} supplies the expected and adversarial\nendpoints; one-stage contamination has an exact inner expectation formula,\nnot in general an affine interpolation of multi-stage values.')
change('\\begin{proposition}[contamination interpolation]\\label{prop:dr}',
       '\\begin{proposition}[one-stage contamination and scope]\\label{prop:dr}')
change('(ii) \\(V^{\\rho}_{k}(b) = (1 - \\rho)\\, V^{\\,0}_{k}(b) + \\rho\\,\nV^{\\,1}_{k}(b)\\) at every stage: the interpolation is pointwise exact,\nwith \\(\\rho = 0\\) the expected value of Definition \\ref{def:value}\nand \\(\\rho = 1\\) the adversarial reading;\n(iii) \\(V^{\\rho}_{k}\\) is concave and piecewise linear in \\(b\\) at\nevery \\(\\rho\\), so the exact-arithmetic discipline of Proposition\n\\ref{prop:pl} carries over verbatim.',
       '(ii) the identity in (i) need not interpolate multistage values:\nunder repeated contamination, continuation values themselves depend on\n\\(\\rho\\);\n(iii) no general concavity claim follows. At \\(\\rho=0\\) the\nnominal finite-action belief value is convex and piecewise linear in\n\\(b\\) as in Proposition \\ref{prop:pl}.')
change('at a vertex \\(r = \\delta_{y^{*}}\\), giving (i); (ii) follows by\ninduction with (i) at every stage, since the adversary\'s optimal\ncontamination is stage-wise; concavity is preserved under pointwise\nmixtures of concave piecewise-linear functions. On the delayed class',
       'at a vertex \\(r = \\delta_{y^{*}}\\), giving (i). Neither a\nBellman maximization nor repeated contaminated backups distributes over\nthe endpoint mixture: with one safe state, transition survival \\(1/2\\),\na revealing safe/exit observation, one action and \\(k=2\\), stagewise\n\\(\\rho=1/2\\) gives survival \\(1/16\\) rather than the\nendpoint interpolation \\(1/8\\). The nominal two-floor value\n\\(V_1^0(b)=\\max(b_1,b_2)\\) is convex, not concave: its midpoint\nis \\(1/2\\) and both endpoint values are \\(1\\).\nIn the \\emph{different}, prior-contamination setup on the delayed class')
change('\\end{proof} This proposition is the formal home of worst-case\nwording: an ambiguity-minded reviewer may read every expected value here\nat any \\(\\rho\\), and every table carries the \\(\\rho = 0\\) column of\na one-parameter family.',
       '\\end{proof} The one-stage operator and the specific prior-contamination\nexample distinguish expected from adversarial readings; no untested\nclaim is made that every table is an affine multistage \\(\\rho\\)-mixture.')
change('\\begin{proposition}[general additive deadline law]\\label{prop:additivelaw}',
       '\\begin{proposition}[additive deadline with aligned worst losses]\\label{prop:additivelaw}')
change('\\(e_{p} = \\max_{\\theta}(-d(u_{p}, \\theta))\\). Then indefinite\nviability holds exactly when',
       '\\(e_{p} = \\max_{\\theta}(-d(u_{p}, \\theta))\\). Assume the\nhold and probe each take the stated durations (\\(T\\ge0\\) and one\nunit), \\(d_0,e_p\\ge0\\), and a \\(\\theta^*\\) attains both\nloss maxima. Then indefinite viability holds exactly when')
change('the floor plus drift times deadline plus probe excursion; after the\nlearned act the positive drift \\(\\mu\\) preserves safety forever, so\nthe deadline identity is the whole answer.',
       'the floor plus the aligned worst losses. Without a common\nmaximizer, the exact threshold for this fixed schedule is instead\n\\(1+\\max_{\\theta}\\max\\{0,-T d(u_0,\\theta),\n-T d(u_0,\\theta)-d(u_p,\\theta)\\}\\);\npositive post-learning drift preserves safety thereafter.')
change('Necessity: some \\(\\theta\\) realizes the hold displacement \\(d_{0}\\)\nand the probe excursion \\(e_{p}\\) at the adversarial stages (the maxima\nare attained), dropping the state to',
       'Necessity under the stated aligned-maximizer condition: the same\n\\(\\theta^*\\) realizes both the hold loss \\(d_0\\) and probe\nexcursion \\(e_p\\), dropping the state to')
change('fails. Sufficiency: every \\(\\theta\\) keeps the state at or above the\nfloor through hold and probe, and the learned drift \\(\\mu > 0\\) then',
       'fails. Sufficiency follows from the nonnegative worst-loss bounds\non both prefix endpoints (and the linear stock path within each phase);\nthe learned drift \\(\\mu > 0\\) then')
change('formalization of the closed forms --- and is now complete:\nthe support identity, the freeze count and its frozen value,\nand the rationality of the \\(\\alpha\\)-vectors are machine-checked',
       'formalization of selected combinatorial statements --- and now\ncovers the deterministic support identity under its declared kernel\nhypotheses, the freeze value for its specified action families, and\nrationality of the declared \\(\\alpha\\)-vectors. These are machine-checked')
change('the general learning-deadline law for additively entering\nhidden parameters, are the natural next steps.',
       'extensions of the learning-deadline law to misaligned worst-loss\nhidden parameters, are the natural next steps.')
out=b/'drafts'/src.name;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(s)
(b/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)
