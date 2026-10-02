#!/usr/bin/env python3
"""Source-specific scientific revisions using exact-parameter replay and interval stress operator."""
from pathlib import Path
import csv,json
P=Path('/home/user/papers');s=(P/'paper09_cod_certification_v35.tex').read_text()
A=Path('/home/user/content_audit/revision_pair_cod_2026-10-02')
cod=list(csv.DictReader(open(A/'COD_EXACT_TABLE.csv')))
K=list(csv.DictReader(open(A/'COD_K_SENSITIVITY.csv')))
U=json.load(open(A/'COD_UNCERTAINTY.json'))
E=json.load(open(A/'EDW_ROBUST_INTERVALS.json'))
def fix(a,b,n=1):
 global s
 assert s.count(a)==n,(s.count(a),a[:145]);s=s.replace(a,b)
# Consistent identifications: exact-parameter source-year fit, not rounded printed r.
fix('approximately \\(1091.84\\) kt;\nthe displayed one-decimal table cell is calculated from these rounded\ncoefficients, and needs a source-parameter precision cross-check.', 'approximately \\(1092.04\\) kt using the fitted\n\\(r=0.236869402778272\\), \\(K=5000\\) kt and source-year\n\\(e_{q10}=-80.86977895283727\\) kt. Rounded coefficients alone\nproduce \\(1091.84\\) kt; all reported table cells below use the\nunrounded fitted values.')
fix('1091.8 \\\\', '1092.0 \\\\')
fix('[1091.8, 10^4]', '[1092.0, 10^4]')
# Entire smooth feedback family table: the historical interval runner approximated
# state-dependent phi*g by a piecewise constant catch, not the defined policy.
family=[('0.25','1064.7','1027.3','884.6','1064.7','1027.0','884.6'),('0.50','1111.3','1071.7','884.6','1111.2','1072.2','884.6'),('0.60','1131.2','1091.0','895.2','1130.7','1091.1','895.8'),('0.75','1161.0','1119.9','920.2','1160.8','1120.5','921.0')]
for phi,worst,q05,q10,nworst,nq05,nq10 in family:
 # row spans multiple lines in source; target numeric triples only inside row
 prefix='Family A, \\(\\phi\\)='+phi+' & '
 a=s.index(prefix);b=s.index('\\\\',a)+2;row=s[a:b]
 new=row.replace(worst+' &',nworst+' &').replace(q05+' &',nq05+' &').replace(q10+' &',nq10+' &')
 assert new!=row and new.count('Family A')==1,(phi,row)
 s=s[:a]+new+s[b:]
# Table 4 originally fixed source-year q10 across refits; changing headline to refit
# would silently change the estimand, so show both as distinct columns/results.
fix('with the kernel scored against each refit\'s own\nsource-year 10th-percentile floor.', 'with a fixed registered source-year q10 floor for the displayed\nTable 4, and with each refit\'s own q10 floor in the paired sensitivity\nanalysis immediately below it. These are different estimands.')
fix('convention: \\(r\\) refit at fixed \\(K\\), kernel scored against that\nrefit\'s own corrected 10th-percentile floor.', 'convention: \\(r\\) refit at fixed \\(K\\), kernel scored against the\n\\emph{registered fixed} source-year 10th-percentile floor\n\\(-80.86977895\\) kt. A refit-specific-floor companion follows.')
# Add reproducible refit-specific table with actual independent values.
anchor='\\textbf{Result 3.7 (Carrying-capacity grid: three readings).}'
rows=[]
for v in K:
 kk=float(v['K']); c=float(v['Cstar_refit']); e=float(v['floor_q10_refit']);t1='empty' if not v['T1_refit'] else f"{float(v['T1_refit']):.1f}";ti='empty' if not v['Tinf_refit'] else f"{float(v['Tinf_refit']):.1f}"
 rows.append(f"{kk:g} & {e:.2f} & {c:.2f} & {t1} & {ti} \\\\")
extra=r'''\noindent\textbf{Refit-specific-floor counterpart (source-year).} At each
fixed $K$, re-estimate $r$ and recompute the 24 source-year residuals,
then take the linear-interpolation q10 of \emph{that} pool rather than
reuse the registered residual class. The two ways of scoring the profile
agree at $K=5000$ only; reporting both avoids silently switching the
uncertainty class while varying the map. Values below follow the same
one-step source-year data and closed-form constant-catch preimage, with
no inference of biological identification.
\begin{center}\small
\begin{tabular}{rrrrr}\toprule
$K$ (kt)&refit q10 (kt)&$C^*$ (kt)&BAU $T=1$ (kt)&BAU $T=\infty$ (kt)\\
\midrule
'''+ '\n'.join(rows)+r'''
\bottomrule\end{tabular}\end{center}

'''
assert s.count(anchor)==1;s=s.replace(anchor,extra+anchor)
# Add raw-vs-clipped and method/biological-vs-statistical sensitivity; percentages
# are empirical fractions of archived seeded replicate ensembles, not probabilities
# of real-world protection.
anchor='Refitting \\(r\\) alone at \\(K = 5000\\) kt is the narrower of the two'
addition=r'''\noindent\textbf{Raw versus censored bound.} Reconstructing the raw
constructive margin from each of the 2,000 stored fixed-$K$ refits as
$g_{r_b,K}(K^*)-|e_{q10}|$ gives the signed 5th/50th/95th
percentiles $(-69.29,78.70,121.07)$ kt. Clipping at zero changes these
to $(0,78.70,121.07)$ kt; 235/2,000 (11.75\%) raw replicates are
nonpositive. Thus a zero lower endpoint in the clipped interval is a
point mass created by the reporting rule, not an estimated zero raw
margin. In the separately archived 2,000 joint $(r,K)$ refits the raw
corresponding percentiles are $(-89.38,73.72,125.66)$ kt; 7.45\% of
these draws place $K<K^*$. These are conditional parametric-bootstrap
summaries of the declared Schaefer fit and resampling scheme, not
frequentist coverage guarantees across model forms. Under four common
sample-quantile definitions the q05 residual is respectively
$-287.36$ kt (linear interpolation), $-323.51$ kt (inverted CDF),
$-325.15$ kt (Hazen) and $-327.61$ kt (Weibull); only the first lies
above $-g_{\max}\simeq-296.09$ kt. Consequently q05
infinite-horizon nonvacuity is a quantile-convention-sensitive conclusion.

'''
assert s.count(anchor)==1;s=s.replace(anchor,addition+anchor)
# Replace qualitative F4 statement with directly computable and proved piecewise
# robust recursion; the declared residual floor and an independent additional
# defect must be distinguished to avoid using the same error twice as physical evidence.
anchor='\\subsection{3. Results}\\label{edw-results}'
interval=r'''\noindent\textbf{Direct bounded-error feedback kernel.} For a fixed
recharge floor $R_-$, a policy $P$ and an independently declared
additive error bound $|\xi_t|\le\varepsilon$, put
$f_P(H)=aH+\alpha+\beta R_-+\gamma P(H)$ on $D=[610,710]$.
At a threshold $K_0\in\{618,660\}$ start with
$W_0=[K_0,710]$ and define
\[
W_{t+1}=\{H\in W_0:
[f_P(H)-\varepsilon,f_P(H)+\varepsilon]\subseteq W_t\}.
\]
For a finite union of closed target intervals $W_t=\bigcup_j[L_j,U_j]$
and a piece of the policy with constant pumping $p$, a connected
one-step error interval must lie inside one target component. Therefore
its preimage on that policy piece is the intersection of $W_0$ and
\[
\left[\frac{L_j+\varepsilon-\alpha-\beta R_--\gamma p}{a},
\frac{U_j-\varepsilon-\alpha-\beta R_--\gamma p}{a}\right].
\]
Taking the union over pieces and components gives the \emph{exact set
recursion} under this separately declared bounded-error model, with
endpoint inclusion determined by the policy's trigger convention. It
does not substitute the within-regime slope for a global feedback
Lipschitz constant. The numerical interval implementation reproduces
the deposited zero-error three-step boundaries of BAU, flat-90\%,
flat-80\%, S1 and CPM on both thresholds before adding error.
Under the UC-min floor and $\varepsilon=15.4108458$ ft, its
$T=1,2,3$ lower boundaries at 618 ft are, respectively:
BAU $(639.43,668.16,706.66)$; flat-90\%
$(638.36,665.64,702.21)$; S1 $(637.28,665.27,702.80)$; and CPM
$(635.67,663.11,699.90)$ ft. All four sets are empty at $T=4$
within the 710-ft ceiling. Using the observed out-of-sample maximum
$\varepsilon=21.8105683$ ft as an alternative hypothetical bound makes
each of those sets empty by $T=3$. These are computed conditional on a
\emph{new, independent} additive error budget; when the very same
empirical residual is used both to define the recharge/productivity
floor and to fund $\varepsilon$, the computation is a double-stress
scenario rather than a calibrated physical-coverage probability.
Stepwise error, recharge-floor persistence, fitting uncertainty and
recorded head measurement error are not interchangeable.

'''
assert s.count(anchor)==1;s=s.replace(anchor,interval+anchor)
# Abstract/conclusion scope: conditional operational claims only.
fix('the same shape of limitation. A certified verdict is therefore','a conditional, model-and-domain-dependent comparison. A certified verdict is therefore') if 'the same shape of limitation. A certified verdict is therefore' in s else None
# Source-review meta phrasing not allowed in a submission manuscript; preserve
# established declaration of post-freeze deviations without diary-style remarks.
out=P/'paper09_cod_certification_v36.tex';assert not out.exists();out.write_text(s)
print(out,'bytes',out.stat().st_size,'extra K rows',len(rows))
