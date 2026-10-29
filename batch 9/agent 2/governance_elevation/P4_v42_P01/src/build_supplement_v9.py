from pathlib import Path
import json,difflib
ROOT=Path(__file__).resolve().parents[1]
base=(ROOT/'inherited/paper4_supplementary_v8_pinned_2efaa.md').read_text();s=base;ledger=[]
def replace(old,new,why):
    global s
    if old not in s:raise ValueError(why)
    s=s.replace(old,new);ledger.append(why)
def block(start,end,new,why):
    global s
    a=s.index(start);b=s.index(end,a);s=s[:a]+new+s[b:];ledger.append(why)
block(s.splitlines()[0],'**Notation.**',r'''# Supplementary Material: Governance Delay and Institutional Feedback

**Amin Abaee** · [ORCID 0000-0002-0019-1842](https://orcid.org/0000-0002-0019-1842)  
Governance manuscript v42; supplementary material v9 · 29 October 2026

This supplement gives the equations, proofs, numerical protocols and evidence supporting the main article. Local nonlinear Hopf hypotheses and protective review/viability inequalities are distinguished from finite-dimensional fold certificates, floating periodic-orbit evidence and observational event-clock constraints. S1--S12 contain the core methods and model comparisons; S13--S16 give the nonlinear normal-form derivation, all-cadences and stock-floor details, connected-branch evidence and institutional-event protocol.

''','Formal versioned front matter')
replace('the protective capital $Z$','the institutional memory $Z$','Correct memory versus capital')
replace('The delay $\\tau$ is the institutional review interval.','The delay $\\tau$ is deployment latency; $T_r$ is periodic review cadence. Governance capital, when introduced in S4.4, is $K_{\\mathrm{cap}}$, not $Z$.','Separate latency, memory and cadence')
block('**Scope (S1.3).**','---',r'''**Scope (S1.3).** Scalar frequency/phase enclosures alone establish the local imaginary spectrum. S13 additionally verifies the classical nonlinear RFDE Hopf hypotheses for gated A and ungated B using explicit second/third derivatives, interval simplicity/transversality checks, nonzero cubic coefficients and separation from all other imaginary frequencies. A constructive radii-polynomial branch neighbourhood and both continuum fold lifts remain separate. No numerical delay threshold is calibrated to a named fishery.

''','Update classical Hopf certification scope')
block('## S3. The Fold-Certificate Gap','## S4.',r'''## S3. Discrete Fold Certificates and Continuum Requirements

For the phase-fixed $m=64$ collocation map $F(w,\tau)$, with $w=(Y,T)\in\mathbb R^{193}$, the Moore--Spence system is
$$\mathcal M(w,\tau,v)=(F(w,\tau),D_wF(w,\tau)v,\ell^\top v-1)=0.$$
It has 387 equations and unknowns. An interval Krawczyk inclusion establishes a unique zero in the finite-dimensional box. The archived lower and upper fold certificates respectively enclose
$$\tau_f\in[5.587236198689235,5.587236198690484],$$
$$\tau_{f2}\in[64.40232720336789,64.40232720337167].$$
The left-nullvector contractions give the lower-fold constants $w^\top F_\tau\in[0.3132662,0.3148219]$ and $w^\top D^2F[v,v]\in[5.6923,5.8943]\times10^{-5}$, and the upper-fold constants $w^\top F_\tau\in[0.2579355,0.2607498]$ and $w^\top D^2F[v,v]\in[-5.88663,-5.87702]\times10^{-4}$. Thus the free-delay finite-dimensional system and its discrete fold nondegeneracy are certified. The exact certificate JSONs are preserved in the package's inherited evidence directory; these are archived certificates, not newly rerun fold pipelines.

A continuum result requires a bordered infinite-dimensional fold construction with controlled off-grid/truncation errors and continuum nondegeneracy. The nonlinear tail of $f(U,SU)$ does not vanish when $U$ has finite Fourier support: softplus and rational terms generate infinitely many modes. Neither a small floating off-grid residual nor a periodic-orbit certificate without the bordered fold equations supplies this lift. The continuous-delay saddle-node theorem remains open. No fold statement transfers to a different turnover, tether, stage-structured or spatial model without fresh analysis.

---

''','Integrate the actual discrete certificates and remove contradictory pre-certificate status prose')
block('One caveat disciplines the empirical reading of the delay parameter:','**Definition S4.2**',r'''Empirical clocks require separately dated endpoints. Hocherman, Trop and Ghermandi (2025) synthesise 101 heterogeneous studies, not an identified 2--13-year implementation-lag distribution. The within-stock event protocol of S16 preserves advice, action and compliance distinctions and does not identify the constant model delay from calendar differences.

''','Replace the unsupported empirical distribution and universal dataset-absence claim')
block('**Definition S4.4**','## S5.',r'''### S4.4 Thermodynamic tether: positivity, exact equilibrium criterion and an explicit Allee example

For physical effort with an energetic cost, introduce governance capital $C=K_{\mathrm{cap}}$, distinct from carrying capacity $K$:
$$\dot C=qEN-C(\delta_K+c_EE),$$
$$\dot E=(1-E/E_{\max})(1-e^{-C/K_0})\mathcal B(E,Z_\tau)-\mu_EE,$$
where $\mathcal B(E,Z)=\eta E(Z-E/E_{\max})+\delta_0Z/(Z_{\rm ref}+Z)$ at unit deficit reference, and all auxiliary coefficients are positive. The integrating-factor formula for $C$ and nonnegative input $qEN$ prove $C(t)\ge0$. The effort interval $[0,E_{\max}]$ is invariant. Both the exponential gate and $C/(C+K_0)$ are regular on this physical capital region; a negative-capital pole is not a physical-state mechanism.

**Proposition S4.1 (Exact positive-equilibrium criterion).** Put $E_b=\min\{E_{\max},r/q\}$, $N^*(E)=K(1-qE/r)$, $Z^*(E)=\delta$, and
$$C^*(E)=\frac{qEN^*(E)}{\delta_K+c_EE},\quad G(E)=\frac{(1-E/E_{\max})(1-e^{-C^*(E)/K_0})\mathcal B(E,\delta)}{E}.$$
Extend $G$ continuously to $[0,E_b]$. Then
$$G(0)=\alpha=\frac{qK\delta_0\delta}{K_0\delta_K(Z_{\rm ref}+\delta)},\qquad G(E_b)=0.$$
For $\mu_E>0$, positive interior equilibria are exactly the roots $G(E)=\mu_E$. In particular $\mu_E<\alpha$ is sufficient, not necessary, for existence. Define $\mu_{\max}=\max_{[0,E_b]}G$. No positive equilibrium exists above $\mu_{\max}$. Every $0<\mu_E<\mu_{\max}$ has at least one; if $\alpha<\mu_E<\mu_{\max}$, there are at least two. An interior nondegenerate maximum ($G'=0$, $G''<0$) is a fold of the equilibrium set. A dynamical saddle-node theorem additionally requires the corresponding RFDE spectral nondegeneracy.

*Proof.* Steady stock and memory equations give $N^*,Z^*$; steady capital gives $C^*$. The remaining equation is $E[G(E)-\mu_E]=0$. The endpoint at zero follows by $1-e^{-C/K_0}=C/K_0+O(C^2)$. At $E_b$, either the effort gate or the yield/capital factor vanishes. Compactness and the intermediate value theorem give the stated root counts. The fold follows from the quadratic expansion at a strict nondegenerate maximum. Positive-equilibrium full-delay stability does not follow from root ordering alone.

The zero-effort equilibrium is $(K,\delta,0,0)$. Its characteristic polynomial factors into $(\lambda+r)(\lambda+d)$ and
$$\lambda^2+(\mu_E+\delta_K)\lambda+\delta_K(\mu_E-\alpha).$$
The delayed-memory derivative in the effort row vanishes there. Consequently this rest is stable for $\mu_E>\alpha$ independently of delay, and unstable for $\mu_E<\alpha$.

**Proposition S4.2 (Extinction-face scope).** On $N=0$, capital and effort decay to zero, yielding the rest $(0,\delta,0,0)$. In the full system this rest has stock eigenvalue $+r$ and is unstable to inward stock perturbations. Attraction on the invariant extinction face is not attraction from positive-stock initial conditions.

**An explicit interval-checked Allee example.** Use the Candidate A ecological/memory/bracket coefficients and auxiliary values $\delta_K=0.1$, $c_E=0.01$, $K_0=0.1$, $\mu_E=0.02$, with $\tau=0$. Here $\alpha\approx0.00648216<\mu_E$. Scalar interval endpoint and derivative tests enclose positive equilibria near $E_1=0.0261223656$, $N_1=99.8693882$, and $E_2=1.4058385649$, $N_2=92.9708072$. Interval Routh tests of the full four-state Jacobian give exactly one right-half-plane eigenvalue at the lower root and no right-half-plane eigenvalues at the upper root. Together with the stable zero-effort rest this provides genuine local bistability for this fully specified example. It does not prove a complete global basin separator. The analytic Jacobian agrees with independent high-precision differentiation to below $6\times10^{-88}$; full root boxes and Hurwitz minors are in `tether_equilibria_v42.json`.

These auxiliary parameters are illustrative mathematical choices, not field estimates. No universal ratio between $\mu_{\max}$ and $\alpha$ is asserted. The tether changes the equilibrium and can change Hopf/fold thresholds; the untethered thresholds do not transfer automatically.

---

''','Repair the tether at the mathematical root: exact criterion, zero-effort stability, extinction-face eigenvalue and fully specified certified bistability example')
replace("$1.019$ (the paper's $1.016$; both exceed 1, and only the strict inequality is load-bearing)","$1.01922$",'Consistent sign-flip gain')
replace('both shifted crossings are simple and transverse','both shifted imaginary-axis crossings are simple and transverse','Linear-diagnostic terminology')
replace('which is what "both remaining local Hopfs" means in the proposition.','which establishes a linear spectral diagnostic, not a nonlinear constitutive law for the reversed-gain institution.','Distinguish the sign-flip diagnostic from a nonlinear quota model')
# Replace the final editorial label/status section with a scientific cross-reference table.
a=s.index('## S12. Status and Label Notes');s=s[:a]+'''## S12. Statement Cross-References

The main article and this supplement use the same substantive statements: the cubic modulus theorem is main Theorem 4.1; weighted delay exclusion is Proposition 5.2 and Corollary 5.1; the iso-gain spectral diagnostic is Proposition 6.1; the reviewed-map identities are Theorem 7.1 and Proposition 7.1. Classical nonlinear Hopf verification is Theorem 5.1/S13; cadence-independent protective stability, the contractive review class and nonlinear stock-floor protection are Theorems 7.2--7.4/S14. The discrete folds and continuum requirements are S3, and numerical branch/capture evidence is S15.

''';ledger.append('Remove drafting-status diary and give current theorem cross-references')
# Scientific terminology, not reconstruction history.
for old,new in [('rebuilt fold pipeline','fold pipeline'),('recovered compute core','compute core'),('recovered integrators','implemented integrators'),('recovered stage','archived stage'),('recovered scripts','archived scripts'),('recovered, declared','declared')]:s=s.replace(old,new)
s=s.replace('Corollary 3','Corollary 5.1').replace('Proposition 5','Proposition 6.1').replace('Theorem 2 of the main article','Theorem 4.1 of the main article')
ext=(ROOT/'manuscript/supplement_extensions_v9.md').read_text()
r=json.loads((ROOT/'data/all_scalar_hopf_v42.json').read_text())['records'];table='| Candidate | Gate | Fundamental delay enclosure (years; displayed outer rounding) |\n|---|---|---|\n'
from decimal import Decimal,ROUND_FLOOR,ROUND_CEILING
for x in r:
 q=Decimal('0.000000001');lo=Decimal(x['tau_enclosure'][0]).quantize(q,rounding=ROUND_FLOOR);hi=Decimal(x['tau_enclosure'][1]).quantize(q,rounding=ROUND_CEILING);table+=f"| {x['candidate']} | {'gated'if x['gated']else'ungated'} | [{lo}, {hi}] |\n"
ext=ext.replace('SCALAR_TABLE_PLACEHOLDER',table)
r=json.loads((ROOT/'data/upper_arm_refinement_v42.json').read_text())['records'];table='| Delay (yr) | Period (yr), 1025 nodes | Dominant nontrivial modulus |\n|---:|---:|---:|\n'
for x in r:table+=f"| {x['tau']:.6f} | {x['meshes'][-1]['period']:.9f} | {x['floquet_steps'][-1]['dominant_nontrivial_modulus']:.9f} |\n"
ext=ext.replace('REFINEMENT_TABLE_PLACEHOLDER',table)
r=json.loads((ROOT/'data/nonlinear_capture_check_v42.json').read_text())['records'];table='| History | Delay | Horizon | Step | Normalized RMS | Waveform match |\n|---|---:|---:|---:|---:|---|\n'
for x in r:table+=f"| {x['history'][:2]} | {x['tau']} | {x['horizon_years']:.0f} | {x['dt']} | {x['normalised_waveform_rms']:.6g} | {'yes'if x['capture_waveform_supported']else'no'} |\n"
ext=ext.replace('CAPTURE_TABLE_PLACEHOLDER',table)
s+=ext
s=s.replace('at which the gated Candidate A equilibrium loses linear stability','at which the gated Candidate A equilibrium changes linear stability')
s=s.replace('Interval Newton applied to the interval-enclosed coefficient representation certifies','Outward endpoint-sign and monotonic-derivative tests on the interval-enclosed coefficients certify')
s=s.replace('□',r'$\square$')
import re
s=re.sub(r'`([^`\n]+/[^`\n]+)`',lambda m:r'\path{'+m.group(1)+'}',s)
(ROOT/'manuscript/paper4_supplementary_v9.md').write_text(s)
(ROOT/'data/supplement_change_ledger_v42.json').write_text(json.dumps(ledger,indent=2)+'\n')
(ROOT/'data/supplement_v8_to_v9.diff').write_text(''.join(difflib.unified_diff(base.splitlines(True),s.splitlines(True),fromfile='pinned_SIv8.md',tofile='SIv9.md')))
print('Built SI:',len(s),'characters')
