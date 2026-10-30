#!/usr/bin/env python3
"""Typed synthesis. Numerical accounting identities are not physical validation."""
import collections,csv,json
from pathlib import Path
from accounts_F12 import require,save,CANDIDATES
ROOT=Path(__file__).resolve().parents[1]

def rows(name):
 with (ROOT/'data'/name).open()as f:return list(csv.DictReader(f))
def j(name):return json.loads((ROOT/'metadata'/name).read_text())

def run():
 acc=rows('accounts_changes_183_F12.csv');primary={(r['ISO3'],r['domain']):r for r in acc if r['start']=='2015'and r['end']=='2023'}
 cross=collections.Counter((primary[iso,'total']['direction'],primary[iso,'forest_component']['direction'])for iso,domain in primary if domain=='total')
 status=[]
 for iso in CANDIDATES:
  status.append(dict(ISO3=iso,primary_account_computed=True,primary_account_percent_change=float(primary[iso,'total']['percent_change']),national_provider_mapped_extents_computed=iso in {'BRA','IDN'},annual_mapped_transition_events_computed=iso in {'BRA','IDN'},endpoint_conversion_partial_identification_computed=iso in {'BRA','IDN'},inventory_cycle_biomass_summaries_computed=iso=='FIN',secondary_inventory_volume_inference_computed=iso=='FIN',original_primary_2015_2023_validated_AGB_admitted=False,permanent_exclusion=False,remaining_status='National map summaries and conditional conversion bounds available; national AGB aggregation, common account/physical support and reference-error calibration remain incomplete.'if iso in {'BRA','IDN'}else'National inventory including Åland acquired; covariance-independent secondary volume inference completed; exact primary endpoint AGB, cross-account territory match and total measurement-error calibration remain incomplete.'if iso=='FIN'else'Physical national analysis not executed in F12; not evidence of irreparable data unavailability.'))
 save('data/national_evidence_status_all_eight_F12.csv',status)
 comparisons=[];events=[];regional=[]
 for iso,tag,country,group,regional_level in [('BRA','BRA_C11','Brazil','formations','state'),('IDN','IDN_C41','Indonesia','mapped_forest','province')]:
  extent=rows(tag+'_extent_changes_F12.csv');r=next(x for x in extent if x['level']=='national'and x['group']==group)
  comparisons.append(dict(ISO3=iso,country=country,start=2015,end=2023,account_total_change_pct=float(primary[iso,'total']['percent_change']),account_excluding_fishing_change_pct=float(primary[iso,'terrestrial_excluding_fishing']['percent_change']),account_excluding_fishing_built_change_pct=float(primary[iso,'terrestrial_excluding_built']['percent_change']),account_forest_component_change_pct=float(primary[iso,'forest_component']['percent_change']),mapped_group=group,mapped_area_start_ha=float(r['area_start_ha']),mapped_area_end_ha=float(r['area_end_ha']),mapped_area_change_ha=float(r['difference_ha']),mapped_area_change_pct=float(r['percent_change']),conditional_symmetric_endpoint_area_error_break_even_ha=float(r['symmetric_endpoint_error_break_even_ha']),conditional_symmetric_endpoint_area_error_break_even_pct_territory=float(r['symmetric_endpoint_error_break_even_pct_total']),comparison_type='Descriptive national published-account and published-map summaries; not calibrated same-support biomass change',physical_error_budget_measured=False,validated_physical_sign_discordance=False))
  event=collections.Counter()
  for x in rows(tag+'_annual_transition_events_F12.csv'):
   if x['level']=='national'and(iso=='IDN'or x['group']==group):event[x['event']]+=float(x['transition_event_area_ha'])
  out=sum(v for k,v in event.items()if k.startswith('to_'));inc=sum(v for k,v in event.items()if k.startswith('inflow_'))
  require(abs(inc-out-float(r['difference_ha']))<.01,'National event balance fails')
  for name,v in sorted(event.items()):events.append(dict(ISO3=iso,group=group,event=name,start=2015,end=2023,sum_annual_event_area_ha=v,unique_endpoint_conversion=False,reference_validated=False))
  events.append(dict(ISO3=iso,group=group,event='TOTAL_OUTFLOW_EVENTS',start=2015,end=2023,sum_annual_event_area_ha=out,unique_endpoint_conversion=False,reference_validated=False));events.append(dict(ISO3=iso,group=group,event='TOTAL_INFLOW_EVENTS',start=2015,end=2023,sum_annual_event_area_ha=inc,unique_endpoint_conversion=False,reference_validated=False))
  sub=[float(x['difference_ha'])for x in extent if x['level']==regional_level and x['group']==group];loss=-sum(v for v in sub if v<0);gain=sum(v for v in sub if v>0)
  regional.append(dict(ISO3=iso,partition=regional_level,units=len(sub),mapped_declining_units=sum(v<0 for v in sub),mapped_increasing_units=sum(v>0 for v in sub),sum_negative_unit_net_changes_ha=loss,sum_positive_unit_net_changes_ha=gain,national_net_ha=gain-loss,ecological_uncertainty_assessed=False))
 save('data/national_account_mapped_cover_comparisons_F12.csv',comparisons);save('data/national_mapped_transition_event_sums_F12.csv',events);save('data/national_mapped_regional_compensation_F12.csv',regional)
 error=[]
 for r in rows('endpoint_conversion_path_bounds_F12.csv'):
  if r['constraint_level']!='finest_reported_geography':continue
  lo,hi=float(r['lower_unique_endpoint_area_ha']),float(r['upper_unique_endpoint_area_ha']);total=850644939.9939615 if r['country']=='BRA'else 189044390.24458277
  error.append(dict(ISO3=r['country'],initial_group=r['initial_group'],final_target=r['final_target'],map_conditional_lower_endpoint_area_ha=lo,map_conditional_upper_endpoint_area_ha=hi,combined_endpoint_class_set_error_break_even_ha=lo,symmetric_endpoint_class_set_error_break_even_ha=lo/2,symmetric_error_break_even_pct_territory=100*lo/(2*total),budget_is_symmetric_difference_of_class_sets_not_just_net_area_error=True,measured_error_budget_available=False))
 save('data/endpoint_conversion_set_error_requirements_F12.csv',error)
 summary=dict(all_183_primary_account_directions=j('accounts_analysis_F12.json')['primary_total_directions'],inherited_secondary_2010_2020_comparable_identifiers=j('accounts_analysis_F12.json')['secondary_comparable_identifiers'],account_only_total_vs_forest_component_cross_tab=[dict(total=a,forest_component=b,count=n)for(a,b),n in sorted(cross.items())],national_mapped_cover_cases=2,raw_map_sign_discordance_cases=sum(r['account_total_change_pct']>0 and r['mapped_area_change_ha']<0 for r in comparisons),raw_discordance_not_validated_error_rate=True,original_primary_national_AGB_admissions=0,secondary_inventory_volume_inferences=1,LP_count=j('transition_path_inference_F12.json')['LP_count'],conversion_association_or_causal_effect_estimated=False,reporting_accuracy_against_independent_physical_truth_estimated=False)
 (ROOT/'metadata/synthesis_F12.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':run()
