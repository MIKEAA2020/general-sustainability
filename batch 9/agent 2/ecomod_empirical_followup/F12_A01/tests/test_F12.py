import collections,csv,json,math,sys,unittest,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from accounts_F12 import require
from finland_change_bounds_F12 import bounds
from transition_path_bounds_F12 import solve,SCALE

def rows(name):
 with (ROOT/'data'/name).open()as f:return list(csv.DictReader(f))
def load(name):return json.loads((ROOT/'metadata'/name).read_text())

class F12Tests(unittest.TestCase):
 def test_primary_cohort_and_directions(self):
  j=load('accounts_analysis_F12.json');self.assertEqual(j['eligible_identifiers'],183);self.assertEqual(j['primary_total_directions'],{'increase':91,'decrease':92})
 def test_annual_complete(self):
  r=rows('accounts_annual_183_F12.csv');self.assertEqual(len(r),1647);self.assertTrue(all(n==9 for n in collections.Counter(x['ISO3']for x in r).values()));self.assertTrue(all(x['flag']in {'+++','++','+'}for x in r))
 def test_account_rounding(self):
  self.assertTrue(all(abs(float(r['component_sum_minus_total_gha']))<=3.000001 for r in rows('accounts_annual_183_F12.csv')))
 def test_component_contributions(self):
  acc={(r['ISO3'],r['start'],r['end']):float(r['difference_gha'])for r in rows('accounts_changes_183_F12.csv')if r['domain']=='total'};tot=collections.Counter()
  for r in rows('accounts_component_contributions_F12.csv'):tot[r['ISO3'],r['start'],r['end']]+=float(r['difference_gha'])
  self.assertEqual(set(tot),set(acc));self.assertTrue(all(abs(v-acc[k])<=6.000001 for k,v in tot.items()))
 def test_forest_account_decomposition(self):
  self.assertTrue(all(abs(float(r['area_contribution_gha'])+float(r['factor_contribution_gha'])-float(r['forest_account_difference_gha']))<1e-5 for r in rows('accounts_forest_component_decomposition_F12.csv')))
 def test_candidates_all_windows(self):
  r=rows('accounts_candidate_changes_F12.csv');self.assertEqual(set(x['ISO3']for x in r),{'BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS'});self.assertEqual(len(r),144)
 def test_secondary_not_substituted(self):
  j=load('accounts_analysis_F12.json');self.assertEqual(j['inherited_secondary_window'],[2010,2020]);self.assertEqual(j['secondary_comparable_identifiers'],182);self.assertEqual(j['secondary_exclusions'][0]['ISO3'],'SSD')
 def test_cameroon_domain_sensitivity(self):
  r={x['domain']:x['direction']for x in rows('accounts_candidate_changes_F12.csv')if x['ISO3']=='CMR'and x['start']=='2015'and x['end']=='2023'};self.assertEqual(r['total'],'increase');self.assertEqual(r['excluding_built'],'decrease')
 def test_canada_domain_sensitivity(self):
  r={x['domain']:x['direction']for x in rows('accounts_candidate_changes_F12.csv')if x['ISO3']=='CAN'and x['start']=='2015'and x['end']=='2023'};self.assertEqual(r['total'],'increase');self.assertEqual(r['terrestrial_excluding_fishing'],'decrease')
 def test_national_typed_comparisons(self):
  r=rows('national_account_mapped_cover_comparisons_F12.csv');self.assertEqual(len(r),2);self.assertTrue(all(x['validated_physical_sign_discordance']=='False'for x in r));self.assertTrue(all(float(x['mapped_area_change_ha'])<0 for x in r))
 def test_brazil_not_increasing_account_example(self):
  r=next(x for x in rows('national_account_mapped_cover_comparisons_F12.csv')if x['ISO3']=='BRA');self.assertLess(float(r['account_total_change_pct']),0)
 def test_indonesia_definition_detail(self):
  r={x['group']:float(x['difference_ha'])for x in rows('IDN_C41_extent_changes_F12.csv')if x['level']=='national'};self.assertGreater(r['forest_formation'],0);self.assertLess(r['peat_swamp_forest'],0);self.assertAlmostEqual(r['mapped_forest'],sum(r[k]for k in ['forest_formation','mangrove','peat_swamp_forest']),places=5)
 def test_error_thresholds_not_confidence_bounds(self):
  for r in rows('national_account_mapped_cover_comparisons_F12.csv'):self.assertAlmostEqual(float(r['conditional_symmetric_endpoint_area_error_break_even_ha']),abs(float(r['mapped_area_change_ha']))/2);self.assertEqual(r['physical_error_budget_measured'],'False')
 def test_provider_geographic_partitions(self):
  for tag,levels in [('BRA_C11',['state','biome']),('IDN_C41',['island','province'])]:
   data=rows(tag+'_extent_annual_F12.csv')
   for y in range(2015,2024):
    n=next(float(r['area_ha'])for r in data if r['level']=='national'and r['group']=='all_classes'and int(r['year'])==y)
    for level in levels:self.assertAlmostEqual(sum(float(r['area_ha'])for r in data if r['level']==level and r['group']=='all_classes'and int(r['year'])==y),n,places=3)
 def test_margin_and_stock_flow_balances(self):
  for tag,key in [('BRA_C11','max_state_biome_class_residual_ha'),('IDN_C41','max_island_province_class_residual_ha')]:
   j=load(tag+'_analysis_F12.json');self.assertTrue(all(x[key]<.01 for x in j['margin_audits']));self.assertLess(j['max_group_balance_residual_ha'],.01)
 def test_event_areas_not_unique(self):
  self.assertTrue(all(r['unique_endpoint_conversion']=='False'for r in rows('national_mapped_transition_event_sums_F12.csv')))
 def test_reference_counts_and_vintage(self):
  j=load('BRA_reference_compatibility_F12.json');self.assertEqual(j['point_count'],85152);self.assertEqual(j['diagnostics']['paired_nonblank'],4053);self.assertFalse(j['reference_collection_compatible']);self.assertFalse(j['accuracy_or_area_estimate_computed'])
 def test_nonblank_not_usable_truth(self):
  j=load('BRA_reference_compatibility_F12.json');self.assertLess(j['diagnostics']['paired_observed_nontraining'],4053);self.assertLessEqual(j['diagnostics']['paired_observed_nontraining_nonedge_both'],j['diagnostics']['paired_observed_nontraining'])
 def test_training_discrepancy_not_silently_harmonized(self):
  j=load('BRA_reference_compatibility_F12.json');self.assertEqual(j['token_counts']['AMOSTRAS']['Treinamento'],9999);self.assertEqual(load('validation_design_assessment_F12.json')['BRA']['document_training_points_removed'],10000)
 def test_indonesia_legend_frozen(self):
  self.assertEqual(load('IDN_C41_analysis_F12.json')['forest_classes'],[3,5,76]);self.assertNotIn(9,load('IDN_C41_analysis_F12.json')['forest_classes'])
 def test_collection_sensitivity_not_pure_version_effect(self):
  j=load('IDN_collection_sensitivity_F12.json');self.assertFalse(j['pure_version_effect_estimated']);self.assertFalse(j['statistical_uncertainty_interval']);self.assertEqual(j['excluded_nonstandard_island_tokens'],{'Island buffered 20 km':25});self.assertLess(j['C3_forest_difference_ha'],j['C41_forest_difference_ha'])
 def test_volume_source_cells(self):
  r=rows('FIN_inventory_volume_SE_source_cells_F12.csv');self.assertEqual([x['volume_cell']for x in r],['N61','N60']);self.assertEqual([float(x['SE_million_m3'])for x in r],[13.001,13.534])
 def test_finnish_inference_no_independence(self):
  j=load('FIN_cycle_volume_inference_F12.json');self.assertFalse(j['independence_assumed']);self.assertGreater(j['approx_95pct_simultaneous_endpoint_difference_interval_Mm3'][0],0);self.assertLess(j['moment_only_95pct_two_sided_sensitivity_interval_Mm3'][0],0);self.assertFalse(j['primary_2015_2023_AGB_hold_lifted'])
 def test_bonferroni_formula(self):
  lo,hi,z=bounds(77,13,14);self.assertAlmostEqual(lo,77-z*27);self.assertAlmostEqual(hi,77+z*27);self.assertGreater(z,1.96)
 def test_bounds_monotonicity(self):
  self.assertLess(bounds(77,20,14)[0],bounds(77,13,14)[0]);self.assertLess(bounds(77,13,14,.01)[0],bounds(77,13,14,.05)[0])
 def test_invalid_uncertainty_rejected(self):
  for a in [(-1,2,.05),(1,2,0),(1,2,1)]:
   with self.assertRaises(ValueError):bounds(0,*a)
 def test_zero_variance(self):
  self.assertEqual(bounds(4,0,0)[:2],(4,4))
 def test_bias_sensitivity_not_measured(self):
  r={int(x['differential_bias_bound_Mm3']):x for x in rows('FIN_cycle_volume_bias_sensitivity_F12.csv')};self.assertEqual(r[15]['positive_under_assumptions'],'True');self.assertEqual(r[20]['positive_under_assumptions'],'False');self.assertEqual(r[0]['bias_budget_measured'],'False')
 def test_forest_account_balancing_not_biomass_loss(self):
  r=next(x for x in rows('FIN_forest_account_stock_flow_balance_F12.csv')if x['year']=='2023');self.assertAlmostEqual(float(r['reported_stock_change_Mm3']),-4.185);self.assertGreater(float(r['net_increment_minus_removals_and_losses_Mm3']),0);self.assertEqual(r['observational_ecological_loss_inferred'],'False')
 def test_all_production_lp_witnesses_audited(self):
  j=load('transition_witness_audit_F12.json');self.assertEqual(j['saved_primal_dual_witnesses_independently_checked'],634);self.assertTrue(j['all_pass']);self.assertFalse(j['solver_called'])
 def test_marked_flow_identified_toy(self):
  f={(2015,3,35):1.,(2015,13,13):1.}
  for y in range(2016,2023):f[y,35,35]=1.;f[y,13,13]=1.
  self.assertAlmostEqual(solve(f,{3},{35},False)[0],1);self.assertAlmostEqual(solve(f,{3},{35},True)[0],1)
 def test_marked_flow_ambiguity_toy(self):
  f={(2015,3,13):1.,(2015,13,13):1.,(2016,13,35):1.,(2016,13,13):1.}
  for y in range(2017,2023):f[y,35,35]=1.;f[y,13,13]=1.
  self.assertAlmostEqual(solve(f,{3},{35},False)[0],0);self.assertAlmostEqual(solve(f,{3},{35},True)[0],1)
 def test_geographic_refinement(self):
  r=rows('endpoint_conversion_path_bounds_F12.csv');groups=collections.defaultdict(dict)
  for x in r:groups[x['country'],x['initial_group'],x['final_target']][x['constraint_level']]=x
  self.assertEqual(len(groups),7)
  for g in groups.values():
   a,b=g['national_aggregate'],g['finest_reported_geography'];self.assertGreaterEqual(float(b['raw_lower_objective_ha'])+.02*float(b['spatial_units']),float(a['raw_lower_objective_ha']));self.assertLessEqual(float(b['raw_upper_objective_ha'])-.02*float(b['spatial_units']),float(a['raw_upper_objective_ha']))
 def test_endpoint_conversion_set_error_requirement(self):
  r=next(x for x in rows('endpoint_conversion_set_error_requirements_F12.csv')if x['ISO3']=='IDN'and x['final_target']=='oil_palm');self.assertGreater(float(r['combined_endpoint_class_set_error_break_even_ha']),111000);self.assertTrue(r['budget_is_symmetric_difference_of_class_sets_not_just_net_area_error']=='True');self.assertEqual(r['measured_error_budget_available'],'False')
 def test_original_primary_admissions_unchanged(self):
  r=rows('national_evidence_status_all_eight_F12.csv');self.assertEqual(len(r),8);self.assertTrue(all(x['original_primary_2015_2023_validated_AGB_admitted']=='False'and x['permanent_exclusion']=='False'for x in r))
 def test_source_transfer_caps(self):
  j=load('source_registry_F12.json');self.assertTrue(all(r['bytes']<=r['cap_bytes']==25000000 and not r['raw_redistributed']for r in j.values()))
 def test_no_pdf_provider_bodies_deposited(self):
  self.assertFalse(any(p.name.startswith(('BRA_C11_accuracy','IDN_C41_ATBD','FIN_NFI13_paper'))for p in ROOT.rglob('*.pdf')))
 def test_guards_survive_optimization(self):
  with self.assertRaises(ValueError):require(False,'intentional negative check')
 def test_dag_topological_order(self):
  seen=set()
  for node in load('WORK_DAG_F12.json')['nodes']:self.assertTrue(set(node['depends_on'])<=seen);self.assertNotIn(node['id'],seen);seen.add(node['id'])
 def test_numerical_reproducibility(self):
  self.assertTrue(load('numerical_reproducibility_F12.json')['normal_and_optimized_bytes_identical'])

if __name__=='__main__':unittest.main(verbosity=2)
