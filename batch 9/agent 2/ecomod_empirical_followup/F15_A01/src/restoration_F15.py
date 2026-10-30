#!/usr/bin/env python3
"""Restore inherited numerical families that F14 left only in source workbooks.

No source value is recomputed or promoted to a new estimand. All tables are generated
from byte-pinned F12 CSV files; the functions below perform formatting and placement.
"""
import csv
from pathlib import Path

COUNTRIES=['BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS']
DOMAINS=['total','terrestrial_excluding_fishing','excluding_built',
         'terrestrial_excluding_built','forest_component','per_person_total']
COMPONENTS=['crop','grazing','forest','fishing','built']
PERIODS=[('2010','2020'),('2015','2022'),('2015','2023')]

def rows(root,name):
    with (root/'data'/name).open(newline='') as f:
        return list(csv.DictReader(f))

def number(x,digits=3,sign=False):
    v=float(x)
    if abs(v)<0.5*10**(-digits):v=0.0
    return f'{v:{ "+" if sign else "" }.{digits}f}'

def domain_table(rr,start,end,label,caption,table):
    body=[]
    for code in COUNTRIES:
        vals=[]
        for domain in DOMAINS:
            r=next(r for r in rr if r['ISO3']==code and r['start']==start
                   and r['end']==end and r['domain']==domain)
            vals.append(number(r['percent_change'],2,True))
        body.append([code]+vals)
    return table(label,caption,
                 ['ISO','Total','No fishing','No built','Neither','Forest','Per person'],
                 body,'lrrrrrr')

def account_tables(root,table):
    rr=rows(root,'accounts_candidate_changes_F12.csv')
    out=domain_table(rr,'2010','2020','tab:SI_account_sensitivity_2010_2020',
        'Inherited secondary account-domain sensitivity, 2010--2020 (percentage change). The cohort contains 182 eligible members of the primary cohort; South Sudan lacks an admissible 2010 endpoint. These remain account quantities.',table)
    out+=domain_table(rr,'2015','2022','tab:SI_account_sensitivity_2015_2022',
        'Additional account-domain sensitivity, 2015--2022 (percentage change). This separately retained window does not supersede the inherited 2010--2020 comparison. No column is independently observed physical forest change.',table)
    cc=rows(root,'accounts_component_contributions_F12.csv')
    body=[]
    for code in COUNTRIES:
        vals=[]
        for component in COMPONENTS:
            r=next(r for r in cc if r['ISO3']==code and r['start']=='2015'
                   and r['end']=='2023' and r['component']==component)
            vals.append(number(r['contribution_percentage_points_of_initial_total'],4,True))
        total=next(r for r in rr if r['ISO3']==code and r['start']=='2015'
                   and r['end']=='2023' and r['domain']=='total')
        body.append([code]+vals+[number(total['percent_change'],4,True)])
    out+=table('tab:SI_component_contributions',
        'All five account-component contributions, 2015--2023 (percentage points of each initial national total). The forest column is not the forest-component percentage change in the domain table: its denominator is initial total biocapacity. Contributions sum to the total up to source rounding.',
        ['ISO','Crop','Grazing','Forest','Fishing','Built','Sum'],body,'lrrrrrr')
    dd=rows(root,'accounts_forest_component_decomposition_F12.csv')
    body=[]
    for code in COUNTRIES:
        for start,end in PERIODS:
            r=next(r for r in dd if r['ISO3']==code and r['start']==start and r['end']==end)
            body.append([code,start+'--'+end,
                number(float(r['forest_account_difference_gha'])/1e6,3,True),
                number(float(r['area_contribution_gha'])/1e6,3,True),
                number(float(r['factor_contribution_gha'])/1e6,3,True),
                number(r['factor_start_gha_per_ha'],4)+'$\\rightarrow$'+number(r['factor_end_gha_per_ha'],4)])
    out+=table('tab:SI_forest_decomposition',
        'Forest-account area-by-factor decomposition for every retained account window. Forest change, area contribution and factor contribution are in million gha; the final column is the implied accounting factor in gha/ha. These are internal account-lineage terms, not independently observed physical forest area, productivity or biomass.',
        ['ISO','Window','$\\Delta B_f$','Area','Factor','$f_0\\rightarrow f_1$'],body,'llrrrX')
    return out

def national_tables(root,table):
    rr=rows(root,'IDN_C41_extent_changes_F12.csv')
    labels=[('forest_formation','C4.1 Forest Formation'),('mangrove','C4.1 mangrove'),
            ('peat_swamp_forest','C4.1 peat swamp forest'),('mapped_forest','C4.1 combined forest'),
            ('oil_palm','C4.1 oil palm (separate)')]
    body=[]
    for group,label in labels:
        r=next(r for r in rr if r['level']=='national' and r['group']==group)
        body.append([label,number(float(r['area_start_ha'])/1e6,6),
                     number(float(r['area_end_ha'])/1e6,6),
                     number(r['difference_ha'],3,True),number(r['percent_change'],4,True)])
    c3=rows(root,'IDN_C3_national_extent_sensitivity_F12.csv')
    a,b=c3[0],c3[1]
    delta=float(b['forest_area_ha'])-float(a['forest_area_ha'])
    body.append(['C3 level-one Forest',number(float(a['forest_area_ha'])/1e6,6),
                 number(float(b['forest_area_ha'])/1e6,6),number(delta,3,True),
                 number(100*delta/float(a['forest_area_ha']),4,True)])
    out=table('tab:SI_Indonesia_classes',
        'Exact Indonesian mapped class and collection/support sensitivities, 2015--2023. Areas at each endpoint are million ha; changes are ha and percentage of the initial class area. C3 and C4.1 do not have certified identical support, so their contrast is not a pure version effect or an uncertainty interval.',
        ['Source/class','2015 (Mha)','2023 (Mha)','Change (ha)','Change (\\%)'],body,'lrrrr')
    ev=rows(root,'national_mapped_transition_event_sums_F12.csv')
    body=[]
    for code,group,label in [('BRA','formations','Brazil formations'),('IDN','mapped_forest','Indonesia forest')]:
        outflow=next(r for r in ev if r['ISO3']==code and r['group']==group and r['event']=='TOTAL_OUTFLOW_EVENTS')
        inflow=next(r for r in ev if r['ISO3']==code and r['group']==group and r['event']=='TOTAL_INFLOW_EVENTS')
        net=float(inflow['sum_annual_event_area_ha'])-float(outflow['sum_annual_event_area_ha'])
        body.append([label+' (all destinations)',number(float(outflow['sum_annual_event_area_ha'])/1e6,6),
                     number(float(inflow['sum_annual_event_area_ha'])/1e6,6),number(net/1e6,6,True)])
    oil=next(r for r in ev if r['ISO3']=='IDN' and r['event']=='to_oil_palm')
    body.append(['Indonesia forest, direct to oil palm',number(float(oil['sum_annual_event_area_ha'])/1e6,6),'--','--'])
    out+=table('tab:SI_transition_events',
        'Annual mapped transition-event sums, 2015--2023 (million hectare-events). Repetition across years and intermediate paths is allowed. These are not unique endpoint-cohort areas, calibrated conversion or causal effects.',
        ['Group/event','Outflow','Inflow','Inflow $-$ outflow'],body,'lrrr')
    co=rows(root,'national_mapped_regional_compensation_F12.csv')
    body=[]
    for r in co:
        body.append([r['ISO3'],r['partition']+' ('+r['units']+')',r['mapped_declining_units'],
            r['mapped_increasing_units'],number(-float(r['sum_negative_unit_net_changes_ha'])/1e6,6,True),
            number(float(r['sum_positive_unit_net_changes_ha'])/1e6,6,True),number(float(r['national_net_ha'])/1e6,6,True)])
    out+=table('tab:SI_regional_compensation',
        'Mapped subnational net-change compensation, 2015--2023 (million ha). Negative and positive sums are over states/provinces, not annual gross transition events. They are descriptive classifications, not independent observations or confidence-resolved ecological gains and losses.',
        ['ISO','Partition','Declining','Increasing','Negative sum','Positive sum','National net'],body,'llrrrrr')
    return out

def finland_ledger(root,table):
    body=[]
    for r in rows(root,'FIN_forest_account_stock_flow_balance_F12.csv'):
        body.append([r['year'],number(r['opening_Mm3']),number(r['closing_Mm3']),
            number(r['reported_stock_change_Mm3'],3,True),
            number(r['net_increment_minus_removals_and_losses_Mm3'],3,True),
            number(r['reclassification_and_balancing_Mm3'],3,True)])
    return table('tab:SI_FIN_stock_flow',
        'Finnish forest-account timber-stock reconciliation (million m$^3$). The final displayed component combines reclassification and balancing. In 2023, the opening-to-closing change is $-4.185$ despite net increment minus removals/losses of $+20.802$, because that component is $-24.987$. This partly inventory-derived account is neither independent biomass validation nor AGB mass.',
        ['Year','Opening','Closing','Stock change','Increment $-$ removals','Reclass./balancing'],body,'lrrrrr')

def apply(main,si,ns,root,table):
    old=('We calculate endpoint changes, component contributions, exclusions of fishing and built land, and separately labelled per-person changes. '
         'The 2010--2020 account sensitivity includes 182 members of the primary cohort. Full sensitivities appear in Supplementary Table~\\SIref{tab:SI_account_sensitivity}.')
    new=('We calculate endpoint changes, all five component contributions, exclusions of fishing and built land, and separately labelled per-person changes. '
         'The 2010--2020 account sensitivity includes 182 members of the primary cohort; the additional 2015--2022 sensitivity does not supersede it. '
         'Primary and secondary domain values appear in Supplementary Tables~\\SIref{tab:SI_account_sensitivity}, \\SIref{tab:SI_account_sensitivity_2010_2020} and \\SIref{tab:SI_account_sensitivity_2015_2022}; all five primary component contributions and the forest-account area-by-factor decomposition appear in Tables~\\SIref{tab:SI_component_contributions} and \\SIref{tab:SI_forest_decomposition}.')
    assert old in main
    main=main.replace(old,new)
    old='Domain choice matters: Canada and Cameroon change total-account direction under some component exclusions. All eight candidates, not only nominally discordant ones, remain in the comparison (Table~\\ref{tab:nationalcases}).'
    new=('Domain choice matters: Canada and Cameroon change total-account direction under some component exclusions. '
         'Canada\'s fishing component contributes $+1.186$ percentage points of its initial total, while its forest component contributes $-0.644$; Cameroon\'s crop and built components contribute $+1.505$ and $+0.749$, while forest contributes $-1.689$ (Supplementary Table~\\SIref{tab:SI_component_contributions}). '
         'Within the forest account\'s own lineage, France combines a $+2.502$ million-gha area contribution with a $-0.655$ factor contribution, whereas Australia combines $+0.339$ with $-0.505$; these are accounting terms, not independent physical area or productivity measurements (Supplementary Table~\\SIref{tab:SI_forest_decomposition}). '
         'All eight candidates, not only nominally discordant ones, remain in the comparison (Table~\\ref{tab:nationalcases}).')
    assert old in main
    main=main.replace(old,new)
    old='The Indonesian earlier-collection forest decline is 3.106 million ha, but its footprint is 43,130 ha larger; the collection-and-support sensitivity is substantial (Supplementary Figure~\\SIref{fig:SI_Indonesia}).'
    new=('The combined Indonesian result is definition-sensitive: Forest Formation alone increases by 3,019 ha ($+0.0032\\%$), mangrove decreases by 11,620 ha, and peat swamp forest decreases by 693,961 ha ($-6.35\\%$). '
         'The earlier collection reports a 3.106 million-ha forest decline, but its footprint is 43,130 ha larger. The resulting 2.403 million-ha difference between net changes cannot be attributed solely to version processing. Both collections give a negative combined change, but differ materially in magnitude and support (Supplementary Figure~\\SIref{fig:SI_Indonesia} and Table~\\SIref{tab:SI_Indonesia_classes}).')
    assert old in main
    main=main.replace(old,new)
    old='These are requirements on unknown errors, not measured uncertainty budgets. Cover and biomass remain distinct.'
    new=('These are requirements on unknown errors, not measured uncertainty budgets. Cover and biomass remain distinct. '
         'Spatial netting also matters: 20 of 27 Brazilian states decline and seven increase, with negative and positive state changes summing to $-11.017$ and $+0.155$ million ha; 14 of 38 Indonesian provinces decline and 24 increase, with sums of $-1.303$ and $+0.601$ million ha. '
         'These are descriptive mapped compensation patterns, not confidence-resolved losses and gains (Supplementary Table~\\SIref{tab:SI_regional_compensation}).')
    assert old in main
    main=main.replace(old,new,1)
    old='The positive Indonesian oil-palm lower bound survives every aggregate-compatible intervening class path, but not arbitrary reference error.'
    new=('Direct annual forest-to-oil-palm transitions total 707,004 hectare-events, which is not the unique endpoint cohort bounded below (Supplementary Table~\\SIref{tab:SI_transition_events}). '
         'The positive Indonesian oil-palm lower bound survives every aggregate-compatible intervening class path, but not arbitrary reference error.')
    assert old in main
    main=main.replace(old,new)
    old='The second-moment sensitivity is $[-41.896,195.440]$ million m$^3$, unresolved. An unbounded differential systematic bias is not covered by either result.'
    new=('The second-moment sensitivity is $[-41.896,195.440]$ million m$^3$, unresolved. A differential-bias budget of 17.293 million m$^3$ would exhaust the positive lower sampling bound; that budget is unmeasured. An unbounded differential systematic bias is not covered by either result.')
    assert old in main
    main=main.replace(old,new)
    old='Stock validation is not change validation:'
    new=('The separate Finnish 2022--2023 forest-account stock--flow reconciliation, including its balancing item, is retained in Supplementary Table~\\SIref{tab:SI_FIN_stock_flow}; it is partly inventory-derived and not independent physical validation. Stock validation is not change validation:')
    assert old in main
    main=main.replace(old,new,1)

    marker='\\section{Biomass products, units and spatial support}'
    assert marker in si
    si=si.replace(marker,account_tables(root,table)+'\n'+marker,1)
    old='For positive forest areas, expanding the symmetric terms gives'
    new=('For positive forest areas $A_t$ and compatible stocks $Q_t$, define mean forest density $D_t=Q_t/A_t$. The symmetric terms are $\\Delta Q_{\\mathrm{extent}}=(A_1-A_0)(D_1+D_0)/2$ and $\\Delta Q_{\\mathrm{density}}=(D_1-D_0)(A_1+A_0)/2$. Expanding them gives')
    assert old in si
    si=si.replace(old,new,1)
    old='For local net stock changes, $G-L=\\sum_i\\Delta Q_i$ and $G+L=\\sum_i|\\Delta Q_i|$. Consequently, $0\\le K\\le1$ when $G+L>0$.'
    new=('For local net stock changes $\\Delta Q_i$, define $G=\\sum_i[\\Delta Q_i]_+$ and $L=\\sum_i[-\\Delta Q_i]_+$, so that $G-L=\\sum_i\\Delta Q_i$ and $G+L=\\sum_i|\\Delta Q_i|$. For $G+L>0$, the cancellation fraction is $K=1-|G-L|/(G+L)$. Consequently, $0\\le K\\le1$.')
    assert old in si
    si=si.replace(old,new,1)

    marker='\\section{Sharp endpoint-cohort bounds and independent numerical certificates}'
    assert marker in ns
    ns=ns.replace(marker,national_tables(root,table)+'\n'+marker,1)
    old='The approximate normal Bonferroni difference band, including source rounding, is $[17.293137220,136.250862780]$ million m$^3$. A worst-covariance second-moment sensitivity gives $[-41.896127566,195.440127566]$ million m$^3$, conditional on unbiased errors with the stated error variances. Both exclude unbounded differential bias.'
    new=('The approximate normal Bonferroni difference band, including source rounding, is $[17.293137220,136.250862780]$ million m$^3$. A differential-bias budget of 17.293137220 million m$^3$ would exhaust its positive lower bound. Separately, $\\Delta\\widehat V\\pm\\sqrt{20}(s_0+s_1)$ is a worst-covariance second-moment sensitivity: the worst-variance standard deviation is bounded by $s_0+s_1$, and the $\\sqrt{20}$ multiplier is the nominal 95\\% Chebyshev form. It gives $[-41.896127566,195.440127566]$ million m$^3$, conditional on unbiased errors and reported standard errors equal to true error standard deviations. Exact coverage is not asserted for estimated variances. Both constructions exclude unbounded differential bias.')
    assert old in ns
    ns=ns.replace(old,new,1)
    old='The Finnish biomass API reports 1,744 and 1,786 Mt for total living trees including below-ground components. Independently rounded stems plus branches/foliage sum to 1,350 and 1,384 Mt. No biomass standard error is inferred from volume error.'
    new='The Finnish biomass API reports 1,744 and 1,786 Mt for total living trees including below-ground components. Independently rounded stems plus branches/foliage sum to 1,350 and 1,384 Mt; independently rounded components can differ from the published total by approximately one million tonnes. No biomass standard error is inferred from volume error.'
    assert old in ns
    ns=ns.replace(old,new,1)
    marker='\\section{Canadian biomass change and uncertainty representations}'
    assert marker in ns
    ns=ns.replace(marker,finland_ledger(root,table)+'\n'+marker,1)
    return main,si,ns
