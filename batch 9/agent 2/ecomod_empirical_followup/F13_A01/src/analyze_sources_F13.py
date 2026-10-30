#!/usr/bin/env python3
"""Source-pinned national analyses. No raster or provider PDF redistribution.
French bands cover sampling uncertainty, conditional on a comparable estimand;
Canadian labelled intervals are not assigned a confidence level by this code.
"""
import argparse,csv,hashlib,io,json,math,re,sys,zipfile
from pathlib import Path
from statistics import NormalDist
import numpy as np
import pandas as pd
import openpyxl
import pymupdf
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT.parent/'.cache/F13/raw'

def require(ok,message):
    if not ok: raise ValueError(message)

def source(name):
    registry=json.loads((ROOT/'metadata/source_registry_F13.json').read_text())
    p=CACHE/name;b=p.read_bytes();r=registry[name]
    require(len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256'],'Source identity drift: '+name)
    return p

def dump(out,name,obj):
    (out/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n')

def french_band(v0,h0,v1,h1,round_unit=1.0,mode='union90',endpoint_family=2):
    """Full published unit allowance per value/halfwidth, no independence.
    For normal95 only, interpret h as 1.95996 SE then use endpoint Bonferroni.
    Family=4 makes all three contrasts against the last of four endpoints
    simultaneously approximately 95% under the same marginal normal model.
    """
    require(all(math.isfinite(v)for v in [v0,h0,v1,h1,round_unit]),'Nonfinite operand')
    require(h0>=0 and h1>=0 and round_unit>=0,'Negative uncertainty')
    scale=1.0
    if mode=='normal95':
        scale=NormalDist().inv_cdf(1-.05/(2*endpoint_family))/NormalDist().inv_cdf(.975)
    else:require(mode=='union90','Unknown band mode')
    radius=scale*(h0+h1+2*round_unit)+2*round_unit
    delta=v1-v0
    return dict(delta_Mm3=delta,lower_Mm3=delta-radius,upper_Mm3=delta+radius,
                radius_Mm3=radius,positive_sign=(delta-radius)>0,
                confidence_label=('at least 90% per contrast, inherited marginal coverage'if mode=='union90'else'approximate 95%, conditional marginal-normal model'),
                endpoint_family=endpoint_family,CI_rescaling_factor=scale,
                full_unit_rounding_allowance=round_unit,
                differential_bias_B_widens_each_side=True,
                positive_sign_differential_bias_budget_Mm3=max(0.,delta-radius))

def parse_french_workbook(name):
    with zipfile.ZipFile(source(name))as z:
        matches=[n for n in z.namelist()if n.endswith('_Volume.xlsx')]
        require(len(matches)==1,'Unique French volume workbook required')
        with io.BytesIO(z.read(matches[0]))as buf:
            wb=openpyxl.load_workbook(buf,read_only=True,data_only=True)
            try:
                sh=wb['BV Propriété'];declared=sh.calculate_dimension();sh.reset_dimensions();rows=list(sh.values)
                total=[r for r in rows if r[0]=='Total'];require(len(total)==1,'French national Total absent')
                sh=wb['Lisez-moi'];sh.reset_dimensions();notes=' '.join(str(r[0])for r in sh.values if r and r[0])
                require('95 %'in notes and 'forêt de production'in notes and '7,5 cm'in notes,'French estimand/CI definition missing')
                row=total[0];require(len(row)>=7,'Truncated French XLSX dimensions')
                return dict(source=name,member=matches[0],sheet='BV Propriété',source_row='Total',
                            volume_Mm3=float(row[1]),halfwidth95_Mm3=float(row[3]),density_m3_ha=float(row[4]),
                            declared_dimension=declared,reset_dimensions_applied=True,actual_columns=len(rows[0]),
                            period=re.search(r'(20\d\d)-(20\d\d)',matches[0]).group(),
                            quantity='living bois fort tige, bark included, DBH >=7.5 cm, production forest',
                            geography='metropolitan/hexagonal France including Corsica; not overseas France',
                            exact_2015_2023_AGB=False)
            finally:wb.close()

def france(out):
    with pymupdf.open(source('FRA_memento_2018.pdf'))as doc:
        text=doc[15].get_text();require('Quelques données régionales'in text,'Historic French source page changed')
        block=re.split(r'(?m)^France\s*$',text,maxsplit=1)[1].split('Régions\n',1)[0]
        nums=[float(n.replace(' ',''))for n in re.findall(r'\d[\d ]*',block)]
        require(len(nums)>=12,'Historic national table extraction failed')
        old=dict(source='FRA_memento_2018.pdf',PDF_page=16,printed_pages='28–29',source_row='France',
                 period='2013-2017',volume_Mm3=nums[4],halfwidth95_Mm3=nums[5],density_m3_ha=nums[6],
                 geography='metropolitan France including Corsica',quantity='living bois fort tige on production forest',exact_2015_2023_AGB=False)
    rows=[old]+[parse_french_workbook(n)for n in ['FRA_2018_2022_national.zip','FRA_2019_2023_national.zip','FRA_2021_2025_national.zip']]
    pd.DataFrame(rows).to_csv(out/'FRA_inventory_endpoints_F13.csv',index=False,float_format='%.10f')
    last=rows[-1];bands=[]
    for row in rows[:-1]:
        for mode,family in [('union90',2),('normal95',2),('normal95',4)]:
            d=french_band(row['volume_Mm3'],row['halfwidth95_Mm3'],last['volume_Mm3'],last['halfwidth95_Mm3'],mode=mode,endpoint_family=family)
            bands.append(dict(initial_cycle=row['period'],final_cycle=last['period'],mode=mode,**d))
    pd.DataFrame(bands).to_csv(out/'FRA_volume_change_bounds_F13.csv',index=False,float_format='%.10f')
    dump(out,'FRA_scope_and_bias_F13.json',dict(original_primary_AGB_admission=False,source_rows=len(rows),
        sampling_only=True,unknown_differential_method_bias_not_bounded=True,
        old_protocol=dict(source='FRA_method_2013_2017.pdf',pages=[5,9,16,17],
            five_campaign_average_not_exact_endpoint=True,production_forest_includes_poplar=True,
            unusable_wood_rebut_deducted=True,protocol_changes_in_2014_2015_documented=True),
        current_workbooks_define_same_nominal_stock_and_production_forest=True,
        retrospective_cubage_and_rebut_harmonization_not_certified=True,
        changed_accessibility_and_planted_forest_categories_not_compared=True,
        four_cycles_retained_and_all_three_comparisons_to_latest_reported=True,
        confidence_intervals_not_total_measurement_error_bounds=True))
    return rows,bands

def nfi_csv(name):
    with source(name).open()as f:
        title=f.readline().strip();d=pd.read_csv(f).set_index('Forest type')
    require(d.index.is_unique and 'Subtotal'in d.index and 'Total'in d.columns,'NFI CSV schema changed')
    return title,d

def canada(out):
    for name in ['CAN_NFI_change_html.html','CAN_NFI_change_CI_html.html','CAN_NFI_change_RSE_html.html']:
        text=BeautifulSoup(source(name).read_text(),'html.parser').get_text(' ',strip=True)
        require('Version 3.1, November 2025'in text and '262,189.89'in text,'NFI change representation/version note changed')
    records=[];checks=[]
    for kind,suffix in [('stock',''),('annual_change','_change')]:
        pre='CAN_NFI_ca_t17_forage20_biom'+suffix
        tables=[nfi_csv(pre+tail+'_en.csv')for tail in ['', '_sep','_intv']]
        estimate,rse,ci=[d for _,d in tables]
        for group in estimate.index:
            v=float(estimate.loc[group,'Total']);r=float(rse.loc[group,'Total']);h=float(ci.loc[group,'Total'])
            ru=.001;rh=.0001
            implied=abs(v)*r/100
            ratio=h/implied if implied else None
            records.append(dict(kind=kind,forest_type=group,estimate=v,RSE_label_percent=r,
                provider_interval_halfwidth=h,provider_interval_lower=v-h,provider_interval_upper=v+h,
                outward_interval_lower=v-h-ru-rh,outward_interval_upper=v+h+ru+rh,
                units='Mt'if kind=='stock'else'Mt/year',
                CI_to_usual_RSE_SE_ratio=ratio,
                confidence_level_for_current_change_export_independently_established=False,
                original_primary_AGB_admission=False))
        sum_types=float(estimate.loc[estimate.index!='Subtotal','Total'].sum());total=float(estimate.loc['Subtotal','Total'])
        checks.append(dict(kind=kind,sum_component_totals=sum_types,reported_total=total,difference=sum_types-total,
                           within_CSV_rounding=abs(sum_types-total)<=.005))
    pd.DataFrame(records).to_csv(out/'CAN_NFI_biomass_intervals_F13.csv',index=False,float_format='%.10f')
    dump(out,'CAN_NFI_scope_audit_F13.json',dict(version='3.1, November 2025',
        reported_stock_period='first remeasurement 2007–2017',
        change_source='combined remeasured 2007–2017 and projected 2006–2017 data; strong artificial-change indicators filtered',
        pure_paired_field_census=False,exact_2015_2023_change=False,
        not_inventoried_area_thousand_ha=262189.89,
        omitted_regions=['Arctic Cordillera','Northern Arctic','Southern Arctic','Nunavut portions of Taiga Plains and Hudson Plains'],
        no_zero_biomass_assumption_for_omitted_support=True,
        estimation_document=dict(source='CAN_NFI_estimation_procedures_v1.13.pdf',relevant_PDF_pages=[5,7,8,11,39,40],
            default_alpha=.05,national_critical_value_approximately=2,
            not_a_current_change_export_implementation_specification=True,
            photo_interpretation_and_measurement_error_assumed_negligible=True),
        uncertainty_tables_carry_matching_version_3_1_labels=True,
        simple_labelled_version_mismatch_does_not_resolve_discrepancy=True,
        change_RSE_and_interval_not_reconciled_under_usual_RSE_definition=True,
        no_change_SE_inferred_from_RSE_table=True,no_independent_calibration_claim=True,
        all_four_forest_type_totals_and_overall_total_retained=True,
        totals_checks=checks,original_primary_AGB_admission=False))
    return records

def congo(out):
    with zipfile.ZipFile(source('COD_C1_wide_csv.zip'))as z:
        frames={k:pd.read_csv(z.open(next(n for n in z.namelist()if '_'+k+'_'in n)))for k in ['country','biome','province']}
    rows=[];audit=[]
    for level,d in frames.items():
        require(not d.duplicated(['territory_name','class_id','year']).any(),'Duplicated COD key')
        require(d.area.notna().all() and np.isfinite(d.area).all() and (d.area>=0).all(),'Invalid COD area')
        require(set(d.year)==set(range(2000,2026)),'Incomplete COD years')
        totals=d.groupby('year').area.sum()
        audit.append(dict(level=level,territories=d.territory_name.nunique(),rows=len(d),
                          annual_footprint_min_ha=float(totals.min()),annual_footprint_max_ha=float(totals.max())))
        for name,ids in [('source_forest_group',[3,4,5]),('dense_forest_and_mangrove',[3,5]),('dense_forest',[3]),('woodland',[4]),('mangrove',[5]),('agriculture_pasture',[21]),('forest_plantation',[9]),('shrub_savanna',[66])]:
            for territory,g in d.groupby('territory_name',sort=True):
                series=g[g.class_id.isin(ids)].groupby('year').area.sum().reindex(range(2000,2026),fill_value=0)
                # Absence of a class row is zero in the exported legend, not an unobserved-region claim.
                v0,v1=float(series.loc[2015]),float(series.loc[2023]);delta=v1-v0
                for year,value in series.items():rows.append(dict(level=level,territory=territory,group=name,classes=';'.join(map(str,ids)),year=year,area_ha=float(value)))
    annual=pd.DataFrame(rows);annual.to_csv(out/'COD_C1_extent_annual_F13.csv',index=False,float_format='%.10f')
    changes=[]
    for key,g in annual.groupby(['level','territory','group','classes'],sort=True):
        s=g.set_index('year').area_ha;v0,v1=s.loc[2015],s.loc[2023];delta=v1-v0
        changes.append(dict(zip(['level','territory','group','classes'],key),area2015_ha=v0,area2023_ha=v1,
                            delta_ha=delta,percent_change=100*delta/v0 if v0 else None,
                            symmetric_endpoint_net_area_error_sign_threshold_ha=abs(delta)/2))
    pd.DataFrame(changes).to_csv(out/'COD_C1_extent_changes_F13.csv',index=False,float_format='%.10f')
    pd.DataFrame(audit).to_csv(out/'COD_C1_support_audit_F13.csv',index=False,float_format='%.10f')
    # Independent administrative aggregations are NOT assumed to partition national support.
    national=frames['country'].groupby('year').area.sum()
    gaps=[]
    for level in ['biome','province']:
        a=frames[level].groupby('year').area.sum()
        for y in range(2000,2026):gaps.append(dict(level=level,year=y,national_minus_subunit_total_ha=float(national[y]-a[y])))
    pd.DataFrame(gaps).to_csv(out/'COD_C1_subunit_footprint_differences_F13.csv',index=False,float_format='%.10f')
    d=frames['country'];label=d[['class_id','class_level1','class_level2']].drop_duplicates().sort_values('class_id')
    label.to_csv(out/'COD_C1_class_crosswalk_F13.csv',index=False)
    dump(out,'COD_C1_interpretation_F13.json',dict(source_country_footprint_mean_ha=float(national.mean()),
        country_table_rows=len(d),classes=len(label),year_count=26,source_zip_folder_name_wide_but_CSV_schema_is_long=True,
        class_4_is_source_woodland_not_Brazil_savanna=True,
        area_unit_evidence='SHA-pinned statistics/01_getAreas.js: ee.Image.pixelArea().divide(10000)',
        source_class_area_rounding_digits=2,
        subunits_not_certified_partition_of_country=True,constant_exported_label_footprint_not_complete_valid_observation_or_geometry_certificate=True,
        ATBD_source='COD_C1_ATBD.pdf',ATBD_relevant_pages=[16,17,18,19,20],
        ecotone_corridor_width_km_each_side=60,ecotone_training_from_temporally_stable_map_labels=True,
        known_class_confusion_and_temporal_irregularities_disclosed=True,
        compatible_2015_2023_design_based_change_CI_not_established=True,
        no_biomass_change_or_conversion_causality_inferred=True,original_primary_AGB_admission=False))
    return changes,audit

def run(output):
    output.mkdir(parents=True,exist_ok=True)
    fr,bands=france(output);ca=canada(output);cod,audit=congo(output)
    dump(output,'source_analysis_summary_F13.json',dict(original_primary_AGB_admissions=0,
        france_longest_cycle_delta_Mm3=bands[0]['delta_Mm3'],france_longest_cycle_union90=[bands[0]['lower_Mm3'],bands[0]['upper_Mm3']],
        france_longest_cycle_normal95=[bands[1]['lower_Mm3'],bands[1]['upper_Mm3']],
        canada_annual_change_total=[r for r in ca if r['kind']=='annual_change'and r['forest_type']=='Subtotal'][0],
        congo_country_changes=[r for r in cod if r['level']=='country'],
        confidence_intervals_are_not_generic_error_bounds=True,
        exploratory_continuation_after_prior_results_known=True))
    print(json.dumps(dict(output=str(output),numerical_files=len(list(output.iterdir())),primary_AGB_admissions=0),indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'data');run(p.parse_args().output)
