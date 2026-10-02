#!/usr/bin/env python3
"""Editorial/source-checked second pass on the six newly versioned heads only."""
from pathlib import Path
P=Path('/home/user/papers')
D={'02':P/'paper02_probabilistic_sufficiency_v15.tex','03':P/'paper03_computational_certification_v19.tex','04':P/'paper04_minimax_dual_certificates_v19.tex','05':P/'paper05_exact_belief_computation_v19.tex','06':P/'paper06_assessment_separation_v70.tex','09':P/'paper09_cod_certification_v35.tex'}
S={k:p.read_text() for k,p in D.items()}
def fix(k,a,b,n=1):
 assert S[k].count(a)==n,(k,S[k].count(a),a[:150]);S[k]=S[k].replace(a,b)
# 02: words reporting scope of the exact sensor/timing law
fix('02','bound\'s exponent vanishes with \\(\\varepsilon\\).','bound\'s exponential \\emph{base} tends to zero with \\(\\varepsilon\\).')
# 03: prevent a root of one schedule being described as all-controls optimal.
fix('03','the printed blind-window controls are\nexactly the optimal shared-braking programs.', 'the printed blind-window controls attain the instantaneous max--min\nshared-braking authorities; no all-horizon optimality of their pair\nschedules is inferred.')
fix('03','(\\tau = \\tfrac6{25}\\) and\n\\(\\tau = \\tfrac{39}{100}\\)).','(\\tau = \\tfrac6{25}\\) and\n\\(\\tau = \\tfrac{39}{100}\\)); those checks alone do not\ncover every real delay below the respective ceiling roots.')
# 04: move abstract and discussion off the invalid global viability and product assertions
fix('04','$Y^{*} = \\tfrac{27}{5}$: aggregate-yield fibres are viable exactly up to', '$Y^{*} = \\tfrac{27}{5}$: aggregate-yield fibres admit a common first-order tangent action exactly up to')
fix('04','the product coupling certified here; and the information-state recursion', 'a single consistent joint coupling (product only for the displayed instance); and the information-state recursion')
fix('04','so the calculus\'s recourse\ncertificate is the envelope\'s $K$-node tree read at depth one.', 'only when the pathwise functional is actually the same weighted\nfacet margin as in the recourse certificate. A formal bridge for more\ngeneral contact-set functionals is not asserted.')
fix('04','--- it is simultaneously what makes kernels convex and what makes measure duality sound.', '--- it is needed for the converse direction of the common-action measure dual, not for the soundness of an already negative average. Kernel convexity requires separate assumptions.')
fix('04','$\\rho$',r'$\rho$',n=0) if False else None
S['04']=S['04'].replace(r'\\rho',r'\rho')
fix('04','Eight exact-rational check families verify the declared finite','Six labelled check families (G1--G6) are listed for the finite')
# dynamic toy: F is pathwise, expectation only outside G
fix('04','F \\;=\\; \\mathbb{E}_{s}\\bigl[\\, 2 - |z_{2}(s)| \\,\\bigr],','G(s,d_1,d_2;u_1,u_2) \\;=\\; 2 - |z_{2}|,')
# eliminate duplicate pathwise-payoff definition left by first pass
fix('04','with the expectation taken under the declared joint law; the pathwise\npayoff is $G(s,d_1,d_2;u_1,u_2)=2-|z_2|$.', 'with the expectation taken under the declared joint law.')
# 05: fixed-point vs downset, counterfactual counts, Lean honesty
fix('05','whereas there is no fixed point here:\nthe object is a complete classification of one finite instance by exhaustive exact enumeration.', 'whereas the four-cube census is a finite enumeration and the five-cube\nindefinite-survival question admits the finite-dimensional drift criterion\nof Theorem~\\ref{scale-thm:global-drift}. Neither a generic safety-game\nfixed point nor the full power set was enumerated for the five-cube.')
fix('05','are \\emph{measured costs of exhaustive exact\nclassification at this size}, offered as cost figures;', 'are \\emph{representation ratios to a hypothetical full subset lattice}, not\nmeasured enumeration operations, runtime costs, or algorithmic speedups;')
fix('05','--- the enlargement that Section~\\ref{scale-scope} previously left open.', '--- the finite enlargement considered here.')
fix('05','Where this text previously attributed a result to simulation\nor enumeration alone, the attribution above governs.', 'The analytic, finite-enumeration and sampled-simulation claims above have\ndistinct proof obligations.') if 'Where this text previously attributed a result' in S['05'] else None
fix('05','A source count limited to lines opening with \\texttt{theorem}\nit omitted four','A source count limited to lines opening with \\texttt{theorem}\nomits four')
# 06: restore careful empirical vs mathematical reporting
fix('06','Per-floor reporting alongside aggregate reporting is\nnecessary for detecting this class of discrepancy.', 'Componentwise path minima, reserve and the assessment protocol, reported\nalongside the aggregate, are sufficient to reconstruct this class of\ndiscrepancy. Floors alone are not sufficient: two states may have the\nsame floors but different resource reserve.')
fix('06','an aggregate\nindex alone cannot distinguish the rescue region from the impossibility region.', 'an aggregate index without reserve and path data does not reconstruct the\ntyped verdict on the witness family.')
fix('06','mandatory reporting', 'component-resolved reporting') if 'mandatory reporting' in S['06'] else None
# 09: restrict invariant domain and certify only proved comparisons
fix('09','the \\(T=\\infty\\) kernel is\n\\([b_\\infty, \\infty)\\)', 'the \\(T=\\infty\\) kernel within the declared finite stock domain\n\\([K^*,S_{\\mathrm{hi}}]\\) is\n\\([b_\\infty, S_{\\mathrm{hi}}]\\) when the map is increasing on\nthat domain, \\(F(b_\\infty)\\ge b_\\infty\\), and\n\\(b_\\infty\\le F(S_{\\mathrm{hi}})\\le S_{\\mathrm{hi}}\\)')
fix('09','From any state above the smaller root the\ntrajectory increases towards the larger and so never falls below the smaller;\nfrom any state below it the trajectory declines.', 'The logistic drift changes sign at the two roots. On the declared\nbounded domain, monotonicity of \\(F\\) and the endpoint inequalities\nensure invariance of \\([b_\\infty,S_{\\mathrm{hi}}]\\); a state\nabove the larger root can initially decline, so monotone increase of\n\\emph{every} safe trajectory is not a valid argument. Outside a domain\nwhere these endpoint tests hold no unbounded-half-line kernel follows.')
fix('09','1074.8', '1091.8',n=2)
fix('09','\\(\\phi=0.60\\) in\nTable 1 exhibits this nonempty proper kernel.', '\\(\\phi=0.60\\) in\nTable 1 exhibits this nonempty proper kernel. Its q10 perpetual lower\nroot from the displayed Schaefer coefficients solves\n\\(0.4rS(1-S/K)=80.87\\) kt and is approximately \\(1091.84\\) kt;\nthe displayed one-decimal table cell is calculated from these rounded\ncoefficients, and needs a source-parameter precision cross-check.')
fix('09','That identity makes\nthe no-dominance verdict \\emph{structural, not empirical}: a reactive rule cannot out-supply a flat\ncap it matches in protection.', 'That identity compares catch and margin \\emph{at the reference point};\nit does not rank catch on other state distributions or prove a global\nno-dominance verdict without a matched replay comparison.')
fix('09','That identity makes the no-dominance verdict\nstructural, not empirical: a reactive rule cannot out-supply a flat cap it\nmatches in protection.', 'At the reference point this is a local protection--harvest budget,\nnot an ordering of total supply for rules evaluated on different state\ndistributions.')
# Scoped cod ceiling certificate, not field-operational shelf life
fix('09','The certified horizon is not a property of the policy.', 'The plotted horizon is a property of the declared capped conversion\nfor the tested constant-catch band; it is not an expiration time for an observed stock.')
# decouple a specific floor and source-year post-freeze claims without modifying the untouched row
fix('09','under the mildest floor class: their supply margins', 'under the drought-of-record protection floor: their supply margins')
fix('09','(nominally, under the mildest floor class)', '(nominally, against the drought-of-record protection floor)')
fix('09','selection at the physical threshold under the mildest floor class', 'selection at the physical threshold against the drought-of-record protection floor')
fix('09','Nominal, physical threshold, mildest floor class:', 'Nominal, physical threshold, drought-of-record protection floor:')
# Never transform a percentile sensitivity into an unavailable bootstrap
anchor='\\textbf{Definition 2.3 (Disturbance classes).}'
assert anchor in S['09']
S['09']=S['09'].replace(anchor,r'''\noindent\textbf{Percentile convention and model-form scope.} Quantile
values below use the declared linear-interpolation convention.
With the finite source-year residual pool, other standard 5th-percentile
conventions can move the estimated floor past the maximum surplus; the
5th-percentile nonvacuity verdict is therefore estimator-sensitive.
The separate Allee refit has a lower recorded in-sample loss but a
boundary-pinned growth parameter. Its biological adequacy cannot be
selected by that single loss alone; the model-form comparisons below
are sensitivities, not identification of a true recruitment mechanism.

'''+anchor,1)
for k,p in D.items(): p.write_text(S[k]); print(k, p.stat().st_size)
# Mathematical supplementary content was not changed; keep a version-matched copy so
# the source reference in 03 is resolvable. No new proof is attributed to this copy.
a=P/'paper03_computational_certification_v18_supplementary.tex'; b=P/'paper03_computational_certification_v19_supplementary.tex'
assert not b.exists();b.write_bytes(a.read_bytes());print('03 supplement copy',b.stat().st_size)
