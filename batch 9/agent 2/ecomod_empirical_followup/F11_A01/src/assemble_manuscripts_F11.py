#!/usr/bin/env python3
"""Create additive F11 sources without changing inherited F10 bytes."""
import difflib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'inherited_F10'
OLD_TITLE='a boundary-matched test of composition masking'
NEW_TITLE='a boundary-matched test of biomass-change identifiability'
ROUNDING='All difference bounds were calculated from unrounded endpoint bounds; displayed endpoints and differences are rounded independently.'

def once(text, old, new):
    if text.count(old)!=1:
        raise ValueError(f'Expected unique source span: {old[:80]!r}; found {text.count(old)}')
    return text.replace(old,new,1)

def main():
    originals={s:(BASE/f'followup_F10_{s}.tex').read_text()for s in ('main','SI')}
    main=originals['main'];si=originals['SI']
    for which,text in [('main',main),('SI',si)]:
        text=text.replace(OLD_TITLE,NEW_TITLE)
        text=once(text,r'\usepackage[T1]{fontenc}',r'\usepackage{cmap}'+'\n'+r'\usepackage[T1]{fontenc}'+'\n'+r'\usepackage{lmodern}')
        text=text.replace(r'\input{results/availability_numbers.tex}',
                          '\\input{inherited_F10/results/availability_numbers.tex}\n\\input{results/numbers_F11.tex}')
        text=text.replace('/ecomod_empirical_followup/F10}', '/ecomod_empirical_followup/F11_A01}')
        if which=='main':main=text
        else:si=text
    main=once(main,r'\graphicspath{{results/}}',r'\graphicspath{{results/}{inherited_F10/results/}}')
    start=main.index('\\begin{abstract}');end=main.index('\\end{abstract}',start)+len('\\end{abstract}')
    abstract=r'''\begin{abstract}
Biocapacity accounts and physical ecological assets describe distinct quantities. Testing composition masking therefore requires matched observation domains and an identifiable physical comparison. We assess national account availability and test what matched biomass and mapped-cover observations identify within a fixed Brazilian footprint. Of \CountryIDs\ country and territory identifiers, \AccountPass\ satisfy the 2015--2023 account criteria; all eight countries selected for physical screening pass those criteria, but none is admitted to a national physical-change comparison. On the 61,830 ha local footprint, the auxiliary whole-cell biomass point-map total increases by $\MapNet\times10^3$ Mg, while positive and negative local differences sum to $\MapGain\times10^3$ and $\MapLoss\times10^3$ Mg: $\MapCancellation\%$ of absolute local differences cancels in the aggregate. Constructive allocations preserve every observed native-cell total and mapped fraction yet permit either positive or negative group-specific change. The coherent joint set for the nested groups intersects all four strict sign quadrants. Comparing nine nested mass-observation scales on identical support, native-cell information narrows the unrestricted difference-set width by $\ReductionForm\%$ for mapped formations and $\ReductionSav\%$ for the separately defined formations-plus-savanna domain, but identifies neither sign. A density-contrast sensitivity family loses strict positive-sign identification at assumed within-cell ratio bounds of \RatioForm\ and \RatioSav, respectively; neither bound is empirically established. These data-anchored identification and aggregation results condition on the point maps, not calibrated ecological change. Inspected reference artifacts do not provide compatible paired local endpoints. The results specify why increasing aggregates are insufficient and what additional allocation information could help; they do not establish national account--asset divergence, conversion associations or the occurrence of ecological composition masking.
\end{abstract}'''
    main=main[:start]+abstract+main[end:]
    start=main.index('\\Needspace{15\\baselineskip}')
    end=main.index('\\section{Materials and methods}',start)
    questions=r'''\Needspace{15\baselineskip}
The ecological hypothesis motivates a sequence of measurement and inference requirements. The present study tests whether the available information identifies the required physical sign, through four questions:
\begin{enumerate}
\item Which national account comparisons satisfy availability criteria, and which physical-support or reference requirements remain unmet?
\item Within a matched local footprint, can an increasing whole-cell biomass point-map total rule out a decline in a separately defined mapped-cover group?
\item How do spatial aggregation and restoration of native-cell mass information change observable offsets and the width or sign of group-change identification sets on identical support?
\item Within an explicit density-contrast sensitivity family, what additional allocation restriction would identify a positive group-change sign?
\end{enumerate}
The account analysis retains all directions of account change, and the local footprint is selected by geometry rather than outcomes. The broader comparisons of independently validated forest stocks, account--asset divergence, conversion associations and reporting accuracy remain subsequent ecological questions, with their admission requirements specified in the Supplementary Information. They are not inferred from conditional point-map arithmetic.

'''
    main=main[:start]+questions+main[end:]
    main=once(main,r'\subsection{Uncertainty, validation and information comparisons}',
              '\\input{src/methods_addition_F11.tex}\n\n'+r'\subsection{Uncertainty, validation and information comparisons}')
    caption='Entries are compatible allocations under nonnegativity and unrestricted component density, not statistical confidence intervals or validated forest-stock changes.'
    main=once(main,caption,caption+' '+ROUNDING)
    main=once(main,r'\section{Discussion}', '\\input{src/results_addition_F11.tex}\n\n'+r'\section{Discussion}')
    old='The evidence comprises account availability, geographic-domain screening, local mapped-cover endpoints, conditional allocation sets, product definitions and the analytical design. It does not estimate national forest-stock trends, account--asset divergence, conversion associations or reporting-rule accuracy.'
    new='The evidence distinguishes arithmetic cancellation in delivered point maps, mapped-group non-identification, and ecological composition masking. The first is quantified on common support, and the second is established by constructive allocations with opposite signs. The third requires independently supported account--asset outcomes and is not demonstrated by either result. The matched-information comparison measures identification-set narrowing, not reporting-rule accuracy. National forest-stock trends, account--asset divergence and conversion associations are not estimated.'
    main=once(main,old,new)
    main=once(main,'No forest-only biomass estimate is obtained by multiplying native density by mapped forest fraction.',
              'Multiplying native density by mapped forest fraction identifies no forest-only biomass estimate without an allocation assumption; the homogeneous sensitivity endpoint supplies such an assumption, not independent evidence.')
    old='The computed allocation sets quantify one part of the identification problem while conditioning on uncertain point maps; they do not supply a calibrated change-resolution rule.'
    new=old+' The contrast boundaries make an additional information requirement explicit: within this family, positive-sign identification requires a uniformly small enough density contrast in all mixed cells and at both endpoints. Independent measurements or defensible ecological constraints could test such a restriction, but neither increased map detail nor an assumed contrast substitutes for paired change validation.'
    main=once(main,old,new)
    start=main.index('\\section{Conclusions}');end=main.index('\\section*{Data and code availability}',start)
    conclusion=r'''\section{Conclusions}
National biocapacity data for 2015--2023 satisfy the specified availability criteria for \AccountPass\ of \CountryIDs\ identifiers, while all eight screened national physical comparisons remain on hold. In the matched Brazilian footprint, an increasing whole-cell biomass point-map total coexists with offsetting local differences and with both signs of mapped-group change under the unrestricted allocation model. Native-cell mass information narrows identification sets substantially but does not identify a sign. Conditional density-contrast boundaries identify a possible auxiliary-information route to sign identification without asserting that the requisite bounds hold. These results establish limits and increments of identification from the available observations, not measured national composition masking. Boundary matching, independently justified change uncertainty and paired reference evidence remain necessary for the broader ecological account--asset test.

'''
    main=main[:start]+conclusion+main[end:]
    main=once(main,'Conditional allocation summaries and topological intersection counts are also supplied;',
              'Conditional allocation summaries, topological intersection counts, matched-scale comparisons, aggregate witness certificates and density-contrast sensitivity results are also supplied;')
    old='Zero counts differ across windows and endpoints and are supplied separately in the coverage table.'
    new=r'''Zero counts differ across windows and endpoints and are given in Table~\ref{tab:nativecoverage}, reproduced from \path{data/native_probe_coverage_F11.csv}. The identical inherited source is \path{inherited_F10/data/support/native_probe_coverage.csv}. The supplemental CSV is available at \url{https://github.com/MIKEAA2020/general-sustainability/blob/main/batch%209/agent%202/ecomod_empirical_followup/F11_A01/data/native_probe_coverage_F11.csv}.'''
    si=once(si,old,new)
    anchor='A separate 1-degree geographic index records polygon intersections for download planning.'
    si=once(si,anchor,'\\input{results/coverage_table_F11.tex}\n\n'+anchor)
    anchor='The two formations allocation sets are'
    si=once(si,anchor,ROUNDING+'\n\n'+anchor)
    si=once(si,r'\section*{Source attribution and availability}',
            '\\input{src/SI_addition_F11.tex}\n\n'+r'\section*{Source attribution and availability}')
    for kind,text in [('main',main),('SI',si)]:
        (ROOT/f'followup_F11_A01_{kind}.tex').write_text(text)
        diff=''.join(difflib.unified_diff(originals[kind].splitlines(True),text.splitlines(True),
                                         fromfile=f'inherited_F10/followup_F10_{kind}.tex',
                                         tofile=f'followup_F11_A01_{kind}.tex'))
        (ROOT/'metadata'/f'source_changes_{kind}_F11.patch').write_text(diff)
    print('Created additive F11 main and SI; inherited files unchanged.')

if __name__=='__main__':main()
