"""Construct additive C18 sources from immutable C17; no deletion of scientific sections.
All substitutions are explicit here. Original files and historical outputs remain intact.
"""
from pathlib import Path
import json,re,csv,difflib
R=Path(__file__).resolve().parents[1]
def replace(s,old,new):
    if old not in s:raise ValueError('Missing exact source fragment: '+old[:90])
    return s.replace(old,new,1)
def residuals(s,default):
    # C gets a distinguishing superscript; existing time subscripts remain valid.
    # Apply only to math segments, never author initials, labels, or bibliography.
    patt=r'\$[^$]*\$|\\begin\{(?:equation\*?|align\*?)\}.*?\\end\{(?:equation\*?|align\*?)\}|\\\[.*?\\\]'
    return re.sub(patt,lambda m:re.sub(r'(?<![A-Za-z_\\])C(?![A-Za-z])',lambda _:r'C^{\mathrm{'+default+'}}',m.group()),s,flags=re.S)
def main():
    main=(R/'inherited_C17/ecomod_C17_main.tex').read_text();si=(R/'inherited_C17/ecomod_C17_SI.tex').read_text()
    main=main.replace(r'\graphicspath{{./}{figures/}}',r'\graphicspath{{figures/}{inherited_C17/figures/}}')
    si=si.replace(r'\graphicspath{{./}{figures/}}',r'\graphicspath{{figures/}{inherited_C17/figures/}}')
    # The baseline bounds/budget tables remain the exact, fully rerun C17 artifacts.
    main=main.replace(r'\input{tables/',r'\input{inherited_C17/tables/')
    si=si.replace(r'\input{tables/',r'\input{inherited_C17/tables/')
    for n in ['fig1_model_dynamics','fig2_nfa_aggregation_face','fig3_composition_attribution']:main=main.replace('{'+n+'}','{'+n+'_C18_A01}')
    for n in ['si_onestock_full_trajectory','si_onestock_mask_window','si_onestock_delay_examples','si_onestock_basin']:si=si.replace('{'+n+'}','{'+n+'_C18_A01}')
    first='This effective state changes the modeled annual contribution per hectare; it is not a direct measurement of biomass density, soil integrity, or ecological health.'
    main=replace(main,first,first+' Larger $q$ need not imply a larger annual account contribution: $q$ is a regeneration/readout state, and the growth-linked part of the observation function is non-monotone.')
    quality=r'''\paragraph{State versus annual readout.} The term $b_{G,c}G_c(q)$ values a logistic growth flow, not a stock level. Consequently, $\Ups(q)=\Ups(q_{\max}-q)$: two distinct interior states can have the same per-hectare account value. Above $q_{\max}/2$, the state can increase while this growth-linked readout falls; at the cap only the direct-yield term $b_c$ remains. For the baseline path, $q$ rises from $0.9$ to $1$, whereas $\Ups$ falls from $0.05576$ to $0.05$\,gha\,ha$^{-1}$. This is an intentional growth-flow observation rule, not evidence that improved ecological condition reduces physical production. A physical interpretation of $q$ would require independent condition measurements and validation of this observation rule.

'''
    main=replace(main,r'\subsection{When conversion raises the total as capital land declines}\label{sec:mask}',r'\subsection{When conversion raises the total as capital land declines}\label{sec:mask}'+'\n\n'+quality)
    marker=r'\subsection{Numerical implementation}\label{sec:numerics}'
    main=replace(main,marker,marker+r'''

\paragraph{Fixed-demand intervention.} In the controlled fixed-demand runs, we override $E=eP$ with $E(t)=\bar E$ and set $R_{rc}=0$. Population still follows its displayed demographic equation, but no longer determines demand in that intervention. Thus fixed demand and restoration-off are two explicit scenario settings, not consequences of demographic equilibrium. Endogenous-demand restoration runs retain $E=eP$ and the stated restoration gate.''')
    main=replace(main,'Finally, we derive five testable empirical predictions.','Finally, we derive five conditional predictions and specify their observation requirements and rejection criteria (SI~\\S S11). The imposed-cap comparison is an internal consistency test rather than an ecological generalization.')
    main=replace(main,'The model yields five testable predictions.','The model yields five conditional predictions, with an operational test map in SI~\\S S11.')
    marker='\\clearpage\n\\section{Discussion}'
    main=replace(main,marker,r'''\paragraph{Empirical test design.} P1 requires an independently mapped area transition and yield contrast; rising account totals alone do not establish its conversion mechanism. P2--P3 require local response experiments or identified interventions across demand levels, not a trend test on global $B$. P4 tests the specified projection and history against an exact path; its failure in ecological data would reject that mapping, not establish a universal delay threshold. P5 requires measured capital-area return flows and matched demand changes. The SI specifies independent observables, fitted quantities, conditional nulls, rejection outcomes, and uncertainty treatment before validation data are inspected. None of the NFA accounting identities is presented as an independent test of these dynamics.
\clearpage
\section{Discussion}''')
    main=main.replace('2/ecomod_c17}', '2/ecomod_audit_remediation_C18_A01}')
    main=replace(main,'Source versions and file hashes are provided in the accompanying metadata.','The package includes frozen NFA Edition 2026 and OWID inputs with attribution and hashes, a 1961--2023 annual joined series, executable endpoint/component/proxy transformations, and figure-generating code. The supplementary drawdown, gate-sign and one-stock experiments have versioned code and numerical outputs. Source versions and file hashes are provided in the accompanying metadata; the NFA workbook and NFA-derived data retain CC BY-SA 4.0 attribution.')
    main=replace(main,'All entries are account values, not physical-stock measurements.}', 'All entries are account values, not physical-stock measurements. Individually rounded contributions need not sum to the independently rounded total.}')
    # Residuals: model default, empirical paragraphs selected by their actual subject.
    chunks=main.split('\n\n');out=[]
    for ch in chunks:
        if '\\bibitem' in ch:out.append(ch);continue
        empirical=any(x in ch for x in ['Auxiliary cropland proxy','The external cropland-area and cereal-yield series','The auxiliary proxy residual','No common-boundary global physical-stock series was assembled'])
        out.append(residuals(ch,'emp' if empirical else 'mod'))
    main='\n\n'.join(out)
    # Additional explicit distinction avoids relying on analogous algebra alone.
    main=replace(main,r'SI~\S S5 reports the proxy and its calibration sensitivity.',r'SI~\S S5 reports the proxy and its calibration sensitivity. We denote this empirical remainder by $C^{\mathrm{emp}}$, distinct from the model observation residual $C^{\mathrm{mod}}=B-b_fA_f=\Ups(q)A_c$.')
    si=replace(si,r'$q$ & uncalibrated, model-defined capital-land quality index',r'$q$ & uncalibrated regeneration/readout state (quality index)')
    si=replace(si,r'The quality index $q$ is uncalibrated and model-defined.',r'The quality index $q$ is an uncalibrated regeneration/readout state. Larger $q$ does not imply larger $\Ups(q)$: the latter values a growth flow, peaks at $q_{\max}/2$, and returns to $b_c$ at $q_{\max}$. This observation rule is not a monotone physical-condition index.')
    si=replace(si,r'\texttt{si\_drawdown\_depth.csv}',r'\texttt{data/si\_drawdown\_depth\_C18\_A01.csv}')
    si=replace(si,r'$2.387$ and $2.955$\,cap at',r'$2.387$ and $2.954$\,cap at')
    note=r'''\noindent Values printed as $0.050$\,ha in Tables~\ref{tab:si_drawdown}--\ref{tab:si_recovery} are rounded values above the floor, not finite-time floor hits. The full-precision CSV reports $\min A_c-\Acmin$ explicitly. For example, at $A_{c0}=1$\,ha and $P_0=3$, the minimum exceeds the floor by $4.60\times10^{-7}$\,ha; finite arithmetic can eventually remove still smaller gaps. The asymptotic statement concerns the continuous conversion law, not exact preservation of arbitrarily small positive gaps by floating-point arithmetic.

'''
    si=replace(si,r'\subsection{Recovery metric and the role of the restoration flow}',note+r'\subsection{Recovery metric and the role of the restoration flow}')
    # Replace existing table bodies by generated, versioned row inputs, not hand transcription.
    for label,filename in [('tab:si_drawdown','drawdown_rows'),('tab:si_recovery','recovery_rows'),('tab:si_gates','gate_rows')]:
        start=si.index('\\label{'+label+'}');begin=si.index('\\midrule',start)+len('\\midrule');end=si.index('\\bottomrule',begin)
        si=si[:begin]+'\n\\input{tables/'+filename+'_C18_A01.tex}\n'+si[end+len('\\bottomrule'):]
    gnote=r'''\paragraph{Policy implementation and numerical refinement.} The gate experiment uses the selected projected delayed-quality law, $\Delta t=0.1$\,yr, and constant initial-state histories over both delays. Reference states are obtained from no-restoration runs to $3000$\,yr with $(A_{c0},P_0)=(0.9,1.2)$ and $(0.9,2.5)$; their reference values are held fixed when the policy integration step is refined. The target rule limits restoration by the remaining target gap per step. Conversion-freeze rows set $u_c=0$ independently of the gate. Full state extrema include $t=0$. The versioned output reports all nine policies at $\Delta t=0.1,0.05,0.025$\,yr, including the separate final $B$ and $E$ rather than enforcing their equality. Refinement quantifies numerical sensitivity; it is not field validation.

'''
    si=replace(si,r'\subsection{Regime table}',gnote+r'\subsection{Regime table}')
    nfanote=r'''\paragraph{Annual transformation and precision.} The offline pipeline selects exactly one world observation for each year 1961--2023 and joins the two external world series by year, with missing or duplicate records rejected. The annual extract includes population in persons, account components, indices, log changes, $X$, and the empirical residual. Source values are not rebalanced: the largest absolute difference between the sum of the five supplied components and the supplied total is $2$\,gha across the annual series (relative discrepancy below $2\times10^{-10}$), consistent with integer rounding in the source workbook. Individual percentage-point contributions are rounded independently; consequently the printed 2022 components sum to $24.5451$ rather than the independently rounded $24.5450$ total. Figures~2--3 in the main article use this same annual pipeline. NFA inputs and NFA-derived numerical outputs retain the source's CC BY-SA 4.0 attribution; external physical area and cereal yield retain OWID/FAOSTAT attribution and provider terms.

'''
    si=replace(si,r'\subsection{Divisia decomposition, sensitivity to the base-year share and level fallback}',nfanote+r'\subsection{Divisia decomposition, sensitivity to the base-year share and level fallback}')
    op=r'''\paragraph{Two distinct observation operators.} The comparator separates immediately available fast output $\sigma bA$ from the broader reported account $B=bA+b_GG(A)$. Its conversion operator responds to the unmet fast-output gap $[E-\sigma bA]_+$; the growth-linked term is valued in the aggregate but is not an additional immediately available fast output in that operator. Debt instead accumulates only the total-account gap $[E-B]_+$. Hence, even at $\sigma=1$, conversion can be active while $E\le B$; for $A<A_{\max}$ an equilibrium can balance positive regeneration against positive depletion with zero debt input. This is a structural convention of the comparator, not an empirical allocation rule. It differs from baseline two-land conversion driven by $[E-B]_+$, so their conversion thresholds and recovery paths are not interchangeable. When $A>A_{\max}$, logistic $G$ is negative, and neither its growth-linked account term nor this equilibrium interpretation should be described as a positive provisioning flow.

'''
    si=replace(si,r'The numerical implementation enforces $A\ge A_{\mathrm{ext}}$',op+r'The numerical implementation enforces $A\ge A_{\mathrm{ext}}$')
    si=replace(si,'RK4 integration uses linear interpolation of delayed states.','RK4 integration evaluates delayed stock and account histories separately at each RK substage, using linear interpolation; the reported account always uses current $G(A)$, not the delayed regeneration input. For a zero delay the corresponding stage state is used directly.')
    si=replace(si,r'Figures~\ref{fig:si_onestock_full}--\ref{fig:si_onestock_basin} show conditional runs of the comparator.',r'''Figures~\ref{fig:si_onestock_full}--\ref{fig:si_onestock_basin} show conditional runs of the comparator. Full-trajectory floor-contact times are $720.800$, $720.750$, and $720.725$\,yr at $\Delta t=0.1,0.05,0.025$\,yr; peak-debt values are $21.8074$, $21.6377$, and $21.5539$\,gha\,yr, respectively. The floor-contact and debt extrema remain timestep-sensitive, so more digits are numerical diagnostics, not ecological precision. The $0.5$\,yr classification grid has 83 high and 125 low endpoints without regeneration delay, and 11 high and 197 low endpoints at $\tau_g=30$\,yr, out of 208 cells each; no cells are intermediate under the stated cutoffs.''')
    # Empirical residual superscript throughout S1--S8; model residual in S9--S10.
    cut=si.index(r'\section{Sharp static identification bounds and witnesses}')
    si=residuals(si[:cut],'emp')+residuals(si[cut:],'mod')
    si=replace(si,r'$S$ & shortfall',r'$C^{\mathrm{mod}}$ & model observation residual $B-b_fA_f=\Ups(q)A_c$, distinct from the empirical residual & gha & model-derived \\'+'\n'+r'$S$ & shortfall')
    si=replace(si,r'\section*{Supplementary references}',(R/'code/prediction_map_C18_A01.tex').read_text()+'\n'+r'\section*{Supplementary references}')
    # Add a compact executable artifact map without turning the paper into an audit diary.
    availability=r'''\subsection{Executable data and observation specifications}\label{si:execution}
The companion package provides an offline implementation: \texttt{reproduce\_empirical\_C18\_A01.py} generates annual observations, endpoint and component tables, proxy sensitivities and main empirical figures; \texttt{reproduce\_two\_land\_C18\_A01.py} generates the drawdown, recovery, threshold, and gate-sign outputs; and \texttt{reproduce\_comparator\_C18\_A01.py} generates the one-stock trajectories, finite-grid classifications, characteristic roots and supplementary figures. Input hashes, release metadata, source URLs and attribution are supplied with the data. All scripts run relative to their own package root, without a network request. The current-quality sensitivity is named separately from the selected delayed-quality specification.

'''
    si=replace(si,r'\section{Operational prediction and falsification map}',availability+r'\section{Operational prediction and falsification map}')
    # Availability is part of S10, preceding the new S11, so earlier section numbers are retained.
    (R/'ecomod_C18_A01_main.tex').write_text(main);(R/'ecomod_C18_A01_SI.tex').write_text(si)
    for label,name in [('main','ecomod_C17_main.tex'),('SI','ecomod_C17_SI.tex')]:
        new=(R/('ecomod_C18_A01_'+label+'.tex')).read_text();old=(R/'inherited_C17'/name).read_text()
        diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name,tofile='ecomod_C18_A01_'+label+'.tex'))
        (R/'evidence'/('source_diff_'+label+'_C18_A01.patch')).write_text(diff)
    # Table fragments from unrounded outputs. Math typography is intentionally compact.
    def rows(n):return list(csv.DictReader((R/'data'/(n+'_C18_A01.csv')).open()))
    g=rows('si_drawdown_depth');r=rows('si_recovery');p=rows('si_gate_sign')
    draw=[]
    for Ac in [.4,.7,1.,1.18]:
        z=[next(float(v['minimum_Ac_ha']) for v in g if float(v['Ac0_ha'])==Ac and float(v['P0_cap'])==P and float(v['chi'])==.1) for P in [1.,1.5,2.,2.5,2.8,3.,3.5,4.]]
        draw.append(f'${Ac:g}$ & '+' & '.join(f'{v:.3f}' for v in z)+r' \\')
    (R/'tables/drawdown_rows_C18_A01.tex').write_text('\n'.join(draw)+'\n'+r'\bottomrule'+'\n')
    rec=[]
    for v in r:
        z={k:float(w) for k,w in v.items()};rec.append(f'${z["P0"]:.1f}$ & ${z["E0"]:.3f}$ & ${z["minimum_Ac"]:.3f}$ & ${z["time_min"]:.1f}$ & ${z["final_Ac_no_restoration"]:.3f}$ & ${z["final_Ac_restoration"]:.3f}$ & ${z["Rc"]:.2f}$'+r' \\')
    (R/'tables/recovery_rows_C18_A01.tex').write_text('\n'.join(rec)+'\n'+r'\bottomrule'+'\n')
    names=['none ($R_{rc}=0$)',r'surplus-gated, $\chi_r=0.02$',r'surplus-gated, $\chi_r=0.05$',r'surplus-gated, $\chi_r=0.10$',r'surplus, $\chi_r=0.10$, target cap $A_c^*=0.8225$',r'surplus, $\chi_r=0.10$, conversion frozen',r'deficit-gated, $\chi_r=0.05$',r'deficit-gated, $\chi_r=0.10$',r'deficit, $\chi_r=0.10$, conversion frozen']
    gate=[]
    for name,v in zip(names,[v for v in p if float(v['dt_yr'])==.1]):
        fields=[('Rc100',2),('Rc900',2),('final_Ac',3),('final_Af',3),('final_Ar',3),('final_B',3),('P_ratio',2),('minimum_Ar',3),('maximum_Ac',3),('peak_D',3)]
        gate.append(name+' & '+' & '.join(f'${float(v[k]):.{n}f}$' for k,n in fields)+r' \\')
    (R/'tables/gate_rows_C18_A01.tex').write_text('\n'.join(gate)+'\n'+r'\bottomrule'+'\n')
if __name__=='__main__':main()
