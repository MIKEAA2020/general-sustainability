"""Build an additive v42 from the immutable C17-cited v41 source.
Every targeted replacement is checked and recorded in a separate change ledger.
Earlier manuscripts, C17, author identity and prior declarations are preserved.
"""
from pathlib import Path
import json,difflib
ROOT=Path(__file__).resolve().parents[1]
BASE=(ROOT/'inherited/paper4_delay_dynamics_v41_pinned_2efaa.tex').read_text();text=BASE[BASE.index('\\documentclass'):];ledger=[]
def replace(old,new,reason):
    global text
    if old not in text:raise ValueError('Missing replacement: '+reason)
    count=text.count(old);text=text.replace(old,new);ledger.append({'reason':reason,'occurrences':count,'old_chars':len(old),'new_chars':len(new)})
def block(start,end,new,reason):
    global text
    a=text.index(start);b=text.index(end,a);old=text[a:b];text=text[:a]+new+text[b:];ledger.append({'reason':reason,'old_chars':len(old),'new_chars':len(new)})
replace('\\date{September 6, 2026}','\\date{October 29, 2026}','Version date')
replace('\\graphicspath{{../}}','\\graphicspath{{../figures/}}','Self-contained figures')
replace('figs_p4/fig2_five_regime_topology_v2.png','fig1_archived_topology_v42.png','Preserve archived topology figure bytes')
abstract=r'''\begin{abstract}
Governance delay links observed resource decline to deployed effort. A
stock--memory--effort model compares a mobilising rule, which escalates
extraction, with a protective quota tracker. At the declared mobilising
parameters, intermediate deployment delay stabilises the equilibrium:
two nondegenerate subcritical Hopf crossings near 3.7 and 150 years are
verified through interval bounds on frequencies, transversality and the
nonlinear cubic coefficients. Under periodic review, the exact
held-measurement and native signal-hold operators restabilise near 6.50
and 6.73 years; a theorem identifies a wider contractive review class
with eventual stability, rather than inferring it from consistency alone.

For the protective law, an exact impulse-response bound proves local
stability at every deployment delay and review cadence, for every
positive adjustment rate at the common equilibrium. A nonlinear
invariant-region theorem additionally preserves a stock floor under
admissible initial effort and a bounded quota, including between reviews.
These guarantees have an explicit parameter-box margin. They do not
extend to arbitrary mixtures: a validated mixed-channel counterexample
shows protective-delay dependence outside the weighted small-gain region.

Odd-grid continuation in log-stock and logit-effort coordinates connects
the upper stable arm to the captured large cycle, supported by mesh,
Floquet and nonlinear waveform checks. Both global fold certificates
remain discrete-collocation results, without a continuous-delay lift.
Within-stock herring event records distinguish advice, restrictive
implementation and closure, constraining temporal interpretation without
constituting a fitted delay distribution. Response law, deployment delay
and review cadence are distinct design coordinates; their field
identification remains separate from the model's mathematical guarantees.
\end{abstract}

'''
block('\\begin{abstract}','\\textbf{Keywords:}',abstract,'Elevated abstract: proved margins, nonlinear floor, connected branch and empirical clock evidence')
block('\\textbf{Keywords:}','\\subsection{1. Introduction}',r'''\textbf{Keywords:} delay differential equations; institutional feedback;
sampled-data control; small-gain stability; harvested stocks;
Hopf bifurcation; regime shifts

''','Seven discoverability keywords')
replace('The classic\nresults all place the delay inside the ecology itself:','Related mechanisms span ecological recruitment and economic supply response:','Correct the literature compartment classification')
replace('gave the canonical stability\n  analysis of the single-species delayed logistic equation.','analysed delayed recruitment in Nicholson\'s blowfly model.','Correct Gurney model attribution')
block('The stable returning arm of the\n  upper branch','\\end{enumerate}',r'''  The upper stable arm is continued in invariant interior coordinates
  from $\tau=64.438$ through the capture region to $155$ yr. Mesh
  refinement, nontrivial Floquet multipliers and independently integrated
  waveforms support one connected stable family (Section 8.2). This is
  numerical branch evidence, not a continuum fold certificate or a
  proof of basin completeness.
''','Replace the open branch connection with new continuation evidence')
replace('and cannot be produced by decreasing \\(\\tau_p\\) alone.','and cannot be produced by changing \\(\\tau_p\\) while remaining inside that certified weight region.','Scope the Corollary 5.1 proof')
replace('it cannot be produced by\ndecreasing \\(\\tau_p\\) alone.','within this certified weight region it cannot be produced by changing \\(\\tau_p\\) alone.','Scope the Corollary 5.1 statement')
block('For institutional design this says that, on the interpolated','\\begin{center}\\rule',r'''The sufficient region excludes onset below its boundary; failure of the
bound above it does not imply onset. For the explicit calibrated
interpolation the sufficient-bound boundary is numerically
$\chi_m\approx0.99815977$, whereas the undelayed Routh boundary is
$\chi_m\approx0.99896519$. Neither is an empirical critical weight.

\textbf{Example 5.1 (Protective-delay dependence outside the certificate).}
Set $\chi_m=0.9988$, $\chi_p=0.0012$, $\eta_p=0.914$ and $\tau_M=0$.
The zero-delay cubic is interval-verified Hurwitz. With all coefficients
fixed, changing only $\tau_p$ from $0$ to $110$ yr produces a root in the
right half-plane, near
$6.28594815\times10^{-6}+0.02789563101i$; a two-dimensional Krawczyk
inclusion encloses it strictly with positive real part. The weighted gain
is about $1.006606$, outside (10). Thus the pure-protective theorem and
the weighted certificate remain valid, but neither implies
protective-delay independence in a near-critical mixed loop. The
counterexample is mathematical, not a calibrated institutional timeline.

''','Replace the wrong onset direction with an interval-validated mixed-channel result')
replace('so\ninstability --- if present --- must originate in parameter regions where\nthe mobilising weight is large, and is independent of the protective\ndelay there.','so a delay-induced instability must lie outside the certified region.\nExample 5.1 shows that the protective delay can matter outside it.','Correct Corollary 6.1 without weakening its valid conditional clause')
replace('The policy-scope reading, instantiated: faster protective governance is\nnot the hazard --- the mobilising sign is.','The pure-channel contrast is a contrast of complete response laws. In a\nmixed loop, the weight, damping and phase placement must be checked jointly.','Prevent the mixed-channel policy overreach')
replace('\\arg\\bigl(C_Z L(i\\omega)\\bigr) - \\omega\\tau','\\arg\\bigl(C_Z L(i\\omega)\\bigr) + \\omega\\tau','Correct phase-sign proof identity')
replace('loop gain \\(1.016 > 1\\)','loop gain \\(1.01922 > 1\\)','Recompute the sign-flip loop gain')
block('For the ordering comparison:\n','\\textbf{What Theorem 7.1 says.}',r'''For the ordering comparison, write the full update factor as
$R(T_r)=I+T_rR_0$, not the rank-one row $R_0$. The products $RF$ and
$FR$ have the same characteristic polynomial by the AB--BA determinant
identity; since $F=e^{A_{\rm hold}T_r}$ is invertible, they are also
similar. This equality concerns their linear spectra, not equality of
the nonlinear reviewed maps. \ensuremath{\square}

''','Repair the rank-one invertibility argument')
replace('0.9928','0.98381948','Correct both native protective annual-radius entries')
block('The \\emph{qualitative} conclusion is not scheme-dependent,','\\textbf{The consolidated sampled-data record',r'''Theorem 7.3 identifies a class for which eventual stability follows
analytically. Consistency alone fixes the small-interval limit, not the
large-interval controller. On the registered constants the exact
held-measurement map crosses at $T_r=6.50129495$ yr, its
start-of-period assessment realization has the same crossing, and the
native hold crosses at $6.72785007$ yr, with multipliers approximately
$0.9855\pm0.1699i$. This tight band concerns those selected exact
realizations; the consistent Euler review instead has its stable window
near $(47.536,79.143)$ yr. The native protective annual radius is
$0.98381948$; Theorem 7.2 proves its all-cadences stability rather than
extrapolating a finite scan. The native mobilising radius falls to about
$0.242$, $0.0165$ and below $10^{-6}$ at $200$, $500$ and $2000$ yr,
consistent with the nilpotent limiting map derived in Theorem 7.3.

''','Replace the unsupported universal scheme argument with a proved implementation class')
# New theorems are kept in a separately inspectable formal source file.
replace('\\subsection{8. Global Numerics at Declared Certification',r'''\input{theorems_v42.tex}

\subsection{8. Global Numerics at Declared Certification''','Add all-cadences stability, review-class and nonlinear stock-floor theorems')
# Classical local Hopf verification is separate from constructive branch-radius validation.
block('The certification tier is scoped precisely.','The pair is registered',r'''The scalar enclosures certify the local imaginary spectrum. In
addition, Theorem 5.1 verifies the classical nondegenerate RFDE Hopf
hypotheses at gated Candidate A by interval bounds on the characteristic
derivative and nonlinear cubic. This is distinct from a
radii-polynomial construction of an explicit branch neighbourhood in the
sense of Church and Lessard (2022) and Church and Queirolo (2024); such a
constructive neighbourhood is not supplied. No continuous-delay fold
certificate follows from these local results. ''','Elevate Candidate A from scalar frequency checks to verified nonlinear Hopf hypotheses')
replace('under unit\nHermitian normalisation of the right eigenvector \\(v\\) and its adjoint\n\\(w\\), with the normalisation','under unit\nHermitian normalisation of the right eigenvector \\(v\\), with the adjoint\nrow normalised by','Make the right/left eigenvector convention unambiguous')
replace('These are numerical evaluations of the\ncoefficient formulas at declared parameter points --- computational\nresults, stated as such.','The physical-time convention is $\\ell_1=\\mathrm{Re}(G_{21})/2$;\nrescaling time to unit Hopf frequency divides this number by $\\omega$.\nThe Candidate B numbers are high-precision evaluations. At Candidate A,\nthe signs are additionally verified with outward interval arithmetic.','State the cubic time convention and upgraded certification')
marker='\\subsubsection{5.3 '
idx=text.index(marker)
new=r'''\textbf{Theorem 5.1 (Nondegenerate Candidate A Hopf points).}
\emph{At the exact registered gated Candidate A vector, both fundamental
crossings are nondegenerate subcritical Hopf bifurcations of the smooth
retarded equation.}

\emph{Proof.} The two validated positive roots of the cubic exhaust its
positive roots: the remaining cubic root is negative because its
constant coefficient is positive. The zero root is excluded. The lower
frequency's first recurrence is beyond $253$ yr, so the two fundamental
crossings have no coincident second imaginary family. Outward interval
bounds give $|\partial_\lambda\Delta|^2>0$, crossing derivatives inside
$[-9.484,-9.482]\times10^{-5}$ and
$[5.509,5.510]\times10^{-6}$, and physical-time cubic coefficients inside
$[5.7478,5.7480]\times10^{-5}$ and
$[3.5491,3.5493]\times10^{-4}$. The exact second/third derivative and
homological formulas are in Supplementary S13. Smoothness near the
interior equilibrium and the classical RFDE Hopf theorem then give the
local periodic branches; positive cubics make them subcritical. This
verifies the local theorem's hypotheses, not a finite-amplitude branch
radius or either global fold. \ensuremath{\square}

'''
text=text[:idx]+new+text[idx:];ledger.append({'reason':'New interval verification of classical nonlinear RFDE Hopf hypotheses','new_chars':len(new)})
replace('5.57 < \\tau < 148.3','5.6 < \\tau < 148.3','Exclude the documented lower-window capture from the interior-search range')
# Replace only the formerly unclosed connection paragraph, preserving archived fold evidence.
block('which no campaign could\nFourier-collocate','\\subsubsection{8.3 The registered numerical',r'''which was not resolved by the archived low-order collocation. An
interior-coordinate continuation now connects the stable returning arm
to that captured family and beyond it (Figure 2). It uses
$u=\log N$ and $v=\log[E/(E_{\max}-E)]$, with $Z$ unchanged, so no
boundary clipping is required. Across 131 corrected records from
$64.4382854$ to $155$ yr, odd grids of 129, 257 and 513 nodes carry the
branch continuously through the previously unresolved interval. The
largest computed dominant nontrivial multiplier is $0.9436$; the phase
multiplier is identified by its tangent alignment rather than removed
by assumption.

Six selected delays are independently corrected on 257, 513 and 1025
nodes. Their 513/1025 periods agree within $10^{-9}$ yr; 4097-point
physical off-grid defects are below $1.3\times10^{-11}$ in every
component. Floquet steps of $0.04$, $0.02$ and $0.01$ yr show convergence.
At $\tau=149.5$ the orbit has period $156.828958$ yr and
$N\in[37.9751,80.7124]$; at $155$ its period is $162.239393$ yr and
$N\in[37.2373,81.4369]$. Fresh log/logit method-of-steps runs match the
full waveforms with a single phase shift, without amplitude or period
fitting: H1 at $149.5$ after $10^5$ yr, and H2 at $155$ after
$4\times10^4$ yr. Halving the step from $0.04$ to $0.02$ yr reduces
the already small mismatch; the normalized RMS at the finer step is
below $8.4\times10^{-8}$. H2 at $149.5$ is not captured within
$4\times10^4$ yr, preserving the history-specific interpretation.
The connection is thus resolved at the numerical continuation tier,
not promoted to a continuum fold proof or a complete basin theorem.
The captured orbit rides close to, but not on, the effort-ceiling face.

\begin{figure}[htbp]
\centering
\includegraphics[width=\linewidth]{fig2_upper_branch_v42.png}
\caption{The upper returning periodic family. (a) Stock extrema and the
equilibrium; (b) period; (c) positive distance from the effort ceiling;
(d) dominant nontrivial multiplier at the 131 continuation records.
The shaded interval is the archived finite-history capture bracket
$148.6$--$149.5$ yr; the dotted line is the upper local Hopf point.
Lines connect numerical records and do not constitute interval
continuum enclosures. Mesh and timestep checks are in Supplementary S15.}
\end{figure}

''','Resolve the upper stable-arm connection using new invariant-coordinate computations')
# Empirical support is an event-level constraint, not an unsupported cross-domain distribution.
block('The \\(g=2\\) window\nlies inside the documented','A mesh-range caveat',r'''The $g=2$ window is a model prediction to compare with
stock-specific institutional timing. The within-stock herring records
of Section 11.4 show both multi-year delays to restrictive action and
rapid in-year protective intervention. These observations motivate a
joint biological--institutional test, not automatic exposure of all
fast-maturing small pelagics.

''','Replace the unsupported 2--13 distribution with stock-specific evidence')
replace('the stage-analysis bands of Section 9.3, whose\n\\(g=2\\) \\(\\tau\\)-window lies inside the documented \\(2\\)--\\(13\\) yr\ngovernance-lag distribution (Hocherman, Trop, and Ghermandi, 2025).','the stage-analysis bands of Section 9.3. The event-level herring\ncomparison below distinguishes timing definitions within one stock\nrather than assuming a cross-domain governance-lag distribution.','Correct the discussion evidence chain')
block('  yr; \\(g=5\\): \\((9.9,20.3)\\) yr --- and the \\(g=2\\) window is the one','At the slow end the question inverts:',r'''  yr; $g=5$: $(9.9,20.3)$ yr. Exposure is a joint predicate:
  independently estimated biology, response law and institutional timing
  must match the same band. The herring event comparison shows that a
  small pelagic institution can also respond within a year, outside
  these particular institutional-delay windows. ''','Replace an unsupported exposed-class claim with a testable joint predicate')
# Insert the event-level evidence and structural identifiability before the cadence literature.
replace('The review cadence, likewise, is an actively managed design parameter',r'''\textbf{Within-stock institutional-event evidence.} North Sea herring
provides a comparison within a small-pelagic stock, rather than between
unrelated environmental domains. Simmonds (2007, Table 1) reconstructs
effort-reduction advice in 1965, specific TAC advice in 1970, the first
restrictive TAC in force in 1976, and directed closure in 1977. Nichols
(1999) records October 1995 reduction advice, urgent additional advice in
May 1996, and emergency implementation during 1996. Retaining the date
precision reported by the sources gives:

\begin{center}\small
\begin{tabular}{p{0.65\linewidth}r}
\toprule
Event clock & Years, outward rounded\\
\midrule
1965 general effort advice to 1976 restrictive TAC & 10.0--12.0\\
1970 specific TAC advice to 1976 restrictive TAC & 5.0--7.0\\
1970 specific TAC advice to 1977 closure & 6.0--8.0\\
October 1995 advice to 1996 emergency implementation & 0.50--1.26\\
May 1996 urgent advice to 1996 implementation & 0--0.67\\
\bottomrule
\end{tabular}
\end{center}

These bounds propagate calendar precision, not sampling uncertainty.
They are five dependent clocks from two episodes, not a delay
distribution, five independent institutions, or estimates of a constant
DDE feedback lag. The $5$--$7$-yr clock is compatible with the model's
$g=2$ window $(2.6,7.8)$ yr; the 1996 urgent-response clock is not.
Thus biological membership alone does not establish exposure. Advice,
restrictive implementation, compliance and reopening cannot be merged
into one clock. The different retrospective TAC values and assessment
vintages in the two sources are not pooled into a stock time series.

A further identification restriction is exact: observations of $N$ and
catch $qEN$ alone are invariant under
$E\mapsto sE$, $q\mapsto q/s$, $E_{\max}\mapsto sE_{\max}$,
$\delta_0\mapsto s\delta_0$ and $E_0\mapsto sE_0$, for $s>0$.
Consequently effort units and catchability cannot be separately fitted
from those observations alone. Spawning-stock biomass also requires an
observation mapping before it can represent this model's total stock.
The event table closes a temporal-evidence link; dynamic field
validation still requires effort/process observations and that mapping
(Supplementary S16).

The review cadence, likewise, is an actively managed design parameter''','Add provenance-rich empirical timing constraints and structural identifiability')
replace('annual review.\n\\end{itemize}','every review cadence under the exact/native implementations, together\nwith an invariant stock floor on the operating region of Theorem 7.4.\n\\end{itemize}','Elevate the discussion with the nonlinear protective guarantee')
replace('and --- under the exact held-measurement update (Proposition 7.1) --- at\nevery tested review interval.','and, by Theorem 7.2, at every positive interval under the exact and\nnative operators. Theorem 7.4 additionally provides a nonlinear\ninter-review stock-floor guarantee on a stated admissible operating region.','Replace finite scans with all-cadences proof in discussion')
replace('frequent assessment and\nrapid response is destabilising','frequent assessment and\nrapid response fail to stabilise the already unstable equilibrium','Correct causal interpretation of annual-review instability')
replace('whose global boundaries are two certified folds at the discrete','whose global boundaries are two certified folds at the discrete','Retain global certificate tier')
replace('stability under annual review, and\nan instability threshold that is provably an artefact of the\ndiscretisation.','stability at every cadence for the exact/native operators, a nonlinear\nstock-floor guarantee on an admissible operating region, and an Euler\ninstability threshold that belongs to the discretisation.','Elevate the conclusion with proved review and safety properties')
replace('the Church--Lessard upgrade\nof the Hopf certificates (Section 11.5\'s first stated open task, taken\ntogether with the continuum off-grid residual stage of both folds)','a constructive radii-polynomial neighbourhood for the local Hopf\nbranches, beyond the verified classical hypotheses of Theorem 5.1,\nand the continuum lift of both fold systems','Distinguish a proved local Hopf theorem from remaining constructive/global validation')
replace('A third stated open\ntask is parameter-box certification:','For mobilising thresholds a further open\ntask is parameter-box certification:','Keep mobilising box validation distinct from the new protective box theorem')
replace('is the upgrade that would carry the threshold statements from arithmetic\nprecision to the policy robustness that Section 11.5 reserves to a\nsensitivity layer.','would carry those threshold statements from point arithmetic\nprecision to robustness. The protective inequalities of Theorems 7.2\nand 7.4 already supply a separate parameter-box result, without\ncertifying the mobilising crossing locations across that box.','Record the newly closed protective robustness gap')
replace('are not\n  certificates of the bifurcation in the sense of Church and Lessard\n  (2022); upgrading them to that standard is a stated open task.','are supplemented at Candidate A by the interval-verified classical\n  nonlinear Hopf hypotheses of Theorem 5.1. A constructive\n  radii-polynomial branch neighbourhood in the sense of Church and\n  Lessard (2022) remains distinct and is not supplied.','Update certification-level summary')
replace('GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.','GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.\nArena.ai Agent Mode was used to assist with computational methods and literature review.','Preserve prior contribution disclosure and append the approved Arena declaration')
replace('paper4\\_supplementary\\_v8.md','paper4\\_supplementary\\_v9.pdf','Versioned supplementary reference')
replace('material. The recovered stage-analysis machinery','material. The additional interval Hopf cubic,\nall-cadences and nonlinear stock-floor bounds, odd-grid continuation,\nFloquet/time-step checks, nonlinear waveform comparisons and herring\nevent table are provided in the versioned v42 computational package at\n\\url{https://github.com/MIKEAA2020/general-sustainability/tree/main/batch%209/agent%202/governance_elevation/P4_v42_P01}.\nThe stage-analysis machinery','Add availability of the new evidence package without moving old deposits')
# New verified references.
replace('Ostrom, E., 1990.',r'''Nichols, J.H., 1999. Saving North Sea herring. CEFAS Lowestoft,
4 pp. \url{https://www.cefas.co.uk/data-and-publications/publications/list/publication-abstract/?id=12671}.

Simmonds, E.J., 2007. Comparison of two periods of North Sea herring
stock management: success, failure, and monetary value. ICES J. Mar.
Sci. 64, 686--692. doi:10.1093/icesjms/fsm045.

Ostrom, E., 1990.''','Add checked event-evidence references')
# Explicitly keep the local/safety distinction in management cautions.
replace('which is not certified here.','which is not certified for the mobilising controller here; the separate\nprotective invariant-region result is Theorem 7.4.','Update the inter-review safety boundary where applicable')
# A short current certification summary avoids stale descriptions of S3.
replace('the transversality and curvature\nconditions, and the continuous-delay lift','the continuum transversality and curvature\nconditions, and the continuous-delay lift','Keep discrete nondegeneracy distinct from the continuum fold gap')
block('  The certification tier is stated precisely: the enclosures certify the','\\item',r'''  These spectral enclosures are supplemented by verified transversality
  and cubic signs, establishing the classical nonlinear Hopf conclusions
  at Candidate A (Theorem 5.1). A constructive radii-polynomial branch
  neighbourhood is a separate stronger deliverable, not claimed here.
''','Update the introductory local-Hopf certification claim')
block('\\emph{The design conclusion is not, however, an artefact of the update:', '\\textbf{Proposition 7.1 (Exact held-measurement monodromy).}', r'''The small-interval instability follows from consistency. Eventual
stability additionally follows for the exact and contractive review
class of Theorem 7.3, and separately for the native hold; it does not
follow from consistency alone. The Euler stable window demonstrates why
crossing locations cannot be assigned to periodic review independently
of its command operator.

''','Remove the remaining consistency-only large-cadence inference')
replace('attractor classification, and the Lyapunov coefficients are numerical', 'attractor classification and the Candidate B Lyapunov coefficients are numerical','Distinguish interval-certified Candidate A cubics from point Candidate B evaluations')
replace('loop-gain exclusions.','loop-gain exclusions; Theorem 5.1 verifies the classical nonlinear\n  Hopf hypotheses, while Theorems 7.2--7.4 establish all-cadences\n  stability, an eventual-stability review class and a nonlinear stock floor.','Include the new substantive theorems in certification summary')
replace('criterion not certified here. Throughout this section the','criterion not certified for the mobilising law here. The protective\noperating-region guarantee is Theorem 7.4. Throughout this section the','Keep the safety limitation conditional on controller class')
replace('The Candidate B numbers are high-precision evaluations. At Candidate A,\nthe signs are additionally verified with outward interval arithmetic.','All four reported numbers are high-precision evaluations whose signs\nare additionally verified with outward interval arithmetic for gated A\nand ungated B (Supplementary S13).','Extend nonlinear cubic interval verification to all four published coefficients')
replace('attractor classification and the Candidate B Lyapunov coefficients are numerical','attractor classification and periodic waveforms are numerical','Place both verified cubic pairs at the interval tier')
replace('both remaining local Hopfs','both simple transverse imaginary-axis crossings','State the iso-gain reversal as the linear diagnostic actually specified')
replace('The phase\nmultiplier is identified by its tangent alignment rather than removed\nby assumption.','The multiplier nearest one is retained, and its phase identity is\nchecked through alignment with the orbit tangent.','Match the Floquet phase-identification description to the algorithm') if 'The phase\nmultiplier is identified by its tangent alignment rather than removed\nby assumption.' in text else None
block('The full interval-enclosure table (enclosures for both candidates and','\\section*{Declarations}',r'''The supplementary material, \texttt{paper4\_supplementary\_v9.pdf},
contains scalar frequency/phase enclosures for both candidates and both
gating variants; the archived collocation and discrete-fold formulation;
the remaining continuum fold requirements (S3); the response-sign frame
and a fully specified interval-verified tether bistability example (S4);
macro-reduction hypotheses, the open-problem register and model
comparisons (S5--S12); the verified nonlinear Hopf formulas (S13);
protective all-cadences and nonlinear viability details (S14); numerical
branch/refinement/capture evidence (S15); and the institutional-event
extraction and identification protocol (S16). Numerical and interval
tiers are stated separately for every result.

''','Replace the stale pre-rebuild status note with the integrated current supplement contents')
block('The three records that entered the archive as unreproducible','here verbatim. The scaffold',r'''The three comparison records below concern a distinct research object:
the \textbf{scaffold} model of the companion flow-balance framework,
with its own implemented equations and parameter set. Their numerical
results are reported ''','Remove reconstruction diary while preserving scaffold comparison results')
replace('of\nwhich the appendix prose calls the classical scaffold ``nine states\'\'\nand lists ten symbols),','with seven implemented nonlinear states),','Describe the actual scaffold state dimension instead of a drafting discrepancy')
replace('--- seven implemented nonlinear states, with seven implemented nonlinear states),','--- seven implemented nonlinear states),','Avoid duplicate state-dimension wording') if '--- seven implemented nonlinear states, with seven implemented nonlinear states),' in text else None
block('is the recovered stage-analysis code of the companion empirical study,','\\subsubsection{9.1 The registered system}',r'''is the archived stage-analysis code of the companion empirical study,
with its declared equations and parameter units. The records below
provide a model-specific delayed-recruitment comparison to the
scalar-logistic system and to the scaffold of Section 8.6.

''','Replace code-recovery narration with the scientific stage-model comparison')
replace('generating code and result files have been recovered and are reproduced','generating code and result files are archived and reproduced','Formal computational provenance') if 'generating code and result files have been recovered and are reproduced' in text else None
for old,new in [('recovered compute','implemented compute'),('recovered scripts','archived scripts'),('recovered stage','archived stage'),('recovered code','archived code'),('recovered integrators','implemented integrators'),('The recovered batch','The archived batch'),('the recovered\nreadme','the archived\nreadme'),('the recovered readme','the archived readme'),('recovered, declared','declared'),('the rebuilt\n','the implemented\n'),('the rebuilt ','the implemented '),("fold's rebuilt ","fold's ")]:
    if old in text:replace(old,new,'Formal methods wording: '+old)
replace('generating code and result files have been recovered and are reproduced','generating code and result files are archived and reproduced','Formal source wording') if 'generating code and result files have been recovered and are reproduced' in text else None
replace('recovery audit and the 21-gate registration campaign that certifies the','source provenance and the 21-gate numerical verification campaign for the','Keep source provenance outside the manuscript narrative')
# Layout adjustments are explicit and separate from scientific changes.
replace('\\(\\bar Z = \\max\\{ \\sup_{[-\\tau,0]} Z,\\ \\Phi_k(qE_{\\max}K) \\}\\). Then','\\[\\bar Z = \\max\\{ \\sup_{[-\\tau,0]} Z,\\ \\Phi_k(qE_{\\max}K) \\}.\\]\nThen','Break the bounded-memory definition at a display boundary')
from decimal import Decimal,ROUND_FLOOR,ROUND_CEILING
scalar=json.loads((ROOT/'data/all_scalar_hopf_v42.json').read_text())['records'];table=r'''The complete scalar modulus search, with separate simplicity and
transversality checks, gives the following outward-rounded delay bounds.
Each pair of columns lists the lower and upper endpoint of an enclosure;
the exact decimal parameters, not field uncertainty, are being enclosed.

\begin{center}\scriptsize
\begin{tabular}{llrrrr}
\toprule
Candidate & Gate & $\tau_-$ lower & $\tau_-$ upper & $\tau_+$ lower & $\tau_+$ upper\\
\midrule
'''
for cand,gate in [('A',False),('A',True),('B',False),('B',True)]:
    rr=[r for r in scalar if r['candidate']==cand and r['gated']==gate];vals=[]
    for r in rr:
        vals.extend([str(Decimal(r['tau_enclosure'][0]).quantize(Decimal('1e-13'),rounding=ROUND_FLOOR)),str(Decimal(r['tau_enclosure'][1]).quantize(Decimal('1e-13'),rounding=ROUND_CEILING))])
    table+=cand+' & '+('gated'if gate else'ungated')+' & '+' & '.join(vals)+r'\\'+'\n'
table+='\\bottomrule\n\\end{tabular}\n\\end{center}\n\n'
block('The complete cubic search (Theorem 4.1) with separately verified','The interval certificates are interval-Newton',table,'Supply all eight independently enclosed scalar delays in a readable table')
replace('The interval certificates are interval-Newton enclosures of the simple','The interval certificates are sign/derivative enclosures of the simple','Describe the implemented endpoint-sign and monotonic-derivative scalar proof')
replace('the phase\nmultiplier is identified by its tangent alignment rather than removed\nby assumption.','the multiplier nearest one is retained, and its phase identity is\nchecked through alignment with the orbit tangent.','State the actual phase-multiplier selection and validation')
old=r'''\[\tau_-^{\mathrm{fl}} = \tau_- + \frac{\pi}{\omega_1} = 3.666149 + \frac{\pi}{0.0251915} = 128.374, \qquad \tau_+^{\mathrm{fl}} = \tau_+ - \frac{\pi}{\omega_2} = 150.358477 - \frac{\pi}{0.0394366} = 70.697,\]'''
new=r'''\[\begin{aligned}
\tau_-^{\mathrm{fl}}&=\tau_-+\pi/\omega_1\approx128.374\ \mathrm{yr},\\
\tau_+^{\mathrm{fl}}&=\tau_+-\pi/\omega_2\approx70.697\ \mathrm{yr}.
\end{aligned}\]'''
replace(old,new,'Wrap the exact sign-flip formulas without changing their numerical content')
old=r'''\((\mathcal{M}, \mu, K_A, d, c, \gamma_U, q, E_{\max}, \eta, \delta_0, \Delta_{\mathrm{ref}}, \tau_m) = (100, 0.340, 24.5, 0.072, 0.00995, 0.388, 0.0384, 35.8, 2.23, 0.0118, 2.29, 5.13)\)'''
new=r'''\[\begin{aligned}
(\mathcal M,\mu,K_A,d,c,\gamma_U)&=(100,0.340,24.5,0.072,0.00995,0.388),\\
(q,E_{\max},\eta,\delta_0,\Delta_{\rm ref},\tau_m)&=(0.0384,35.8,2.23,0.0118,2.29,5.13)
\end{aligned}\]'''
replace(old,new,'Wrap the primitive-flux parameter vector without dropping values')
replace('--- hence no lower\nfold for that class --- with','--- a local supercritical onset, which does not exclude distant folds --- with','Remove the invalid inference from local Hopf criticality to global fold absence')
replace('the three-state ungated Candidate B has no lower fold (its\nlower crossing is supercritical, Section 5.2) and an upper fold','the three-state ungated Candidate B has a supercritical lower crossing\n(Section 5.2), with no lower fold reported by the registered search, and an upper fold','Separate the registered negative search from a global nonexistence theorem')
block('Multiple far-from-equilibrium\nseeds failed to reach a large cycle','The inferred subcritical',r'''Finite searches from the archived histories found no large cycle over
$5.6<\tau<148.3$ yr, but this is not a monostability test over the
whole interval: the stable upper family now continues across
$64.438<\tau<148.3$ with nontrivial multipliers below one. Together
with the stable equilibrium, it supports bistability there even when
those histories settle. Regime (iii), below the second fold, retains
only a search-based absence of another attractor. The 131-point
continuation and waveform connection remove the former branch-identity
gap without claiming complete basins. ''','Use the connected stable family to resolve the apparent finite-history monostability contradiction')
replace('whose basin boundary lies between the two folds\nrather than at either','whose observed upper capture bracket lies inside the upper bistable\nwindow rather than at a fold','Correct the relative ordering: upper capture lies above the second fold')
replace('fig1_archived_topology_v42.png','fig1_global_topology_v42.png','Regenerate a journal-quality topology figure from archived CSVs and the new connected arm')
block('\\caption{The five-regime attractor topology','\\end{figure}',r'''\caption{Periodic families and finite-history outcomes. (a) The lower
unstable/stable arms meet at the discretely certified fold near
$5.5872362$ yr; (b) the upper unstable arm turns at the discretely
certified fold near $64.4023272$ yr, with the stable arm continued to
$155$ yr; (c) lower-family real multipliers; (d) archived basin outcomes,
with circles/squares distinguishing the two campaign grids. Red and
blue branch curves denote computed instability/stability, not complete
continuum spectral enclosures. The shaded upper capture bracket is
history/horizon-specific; it is not a fold location. The new upper-arm
resolution and refinement are shown separately in Figure 2 and S15.}
''','Make the topology figure and caption agree and remove cropped process-history headings')
# The finite-horizon capture evidence supports a basin interpretation, not an exact basin theorem.
replace('the capture onset in \\([148.6, 149.5]\\) yr is a basin\nboundary inside this window, not a fold.','the observed capture onset in \\([148.6,149.5]\\) yr is consistent with a\nhistory-specific basin transition inside this window, not a fold.','Scope the finite-history capture bracket') if 'the capture onset in \\([148.6, 149.5]\\) yr is a basin\nboundary inside this window, not a fold.' in text else None
replace('interior monostability are open.','complete basin classification in regime (iii) remains open.','Use the precise remaining global classification problem')
if 'from the recovered\n' in text:replace('from the recovered\n','from the archived\n','Formal source-provenance wording')
replace('certified by interval Newton iteration on the\n  cubic with outward rounding','certified by validated scalar-root tests on the\n  cubic with outward rounding','Identify the implemented scalar enclosure method')
replace('interval-Newton certificates of the local spectrum of the cubic','outward-rounded certificates of the local spectrum of the cubic','Consistent certification-method terminology')
replace('\\begin{document}',r'''\hypersetup{pdftitle={Governance delay and the stability of harvested stocks},pdfauthor={Amin Abaee},pdfsubject={Mobilising and protective feedback rules, and review cadence},pdfkeywords={delay differential equations, institutional feedback, sampled-data control, small-gain stability, harvested stocks, Hopf bifurcation, regime shifts}}
\begin{document}''','Searchable PDF author, title and seven-keyword metadata')
replace('enclosed by interval Newton iteration with outward\nrounding','enclosed by outward-rounded scalar-root and phase tests','Make the certification definition agree with the actual endpoint-sign method')
(ROOT/'manuscript/paper4_delay_dynamics_v42.tex').write_text('% Governance v42: additive revision of the pinned v41; prior source preserved.\n'+text)
(ROOT/'data/manuscript_change_ledger_v42.json').write_text(json.dumps(ledger,indent=2)+'\n')
(ROOT/'data/manuscript_v41_to_v42.diff').write_text(''.join(difflib.unified_diff(BASE.splitlines(True),text.splitlines(True),fromfile='pinned_v41.tex',tofile='v42.tex')))
print('Built manuscript:',len(text),'characters;',len(ledger),'recorded operations')
