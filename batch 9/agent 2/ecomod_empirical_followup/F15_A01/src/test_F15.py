import unittest,csv,json,re,hashlib
from pathlib import Path
from build_F15 import ROOT,expand
class EditorialIntegration(unittest.TestCase):
 @classmethod
 def setUpClass(c):
  c.main=(ROOT/'integrated_F15_A01_main.tex').read_text();c.full=expand(ROOT/'integrated_F15_A01_main.tex');c.si=expand(ROOT/'integrated_F15_A01_SI.tex');c.links=json.loads((ROOT/'metadata/SI_linkage_F15.json').read_text());c.plot=json.loads((ROOT/'metadata/plot_values_F15.json').read_text())
 def test_01_six_main_figures(self):self.assertEqual(self.full.count('\\begin{figure}'),6)
 def test_02_two_main_tables(self):self.assertEqual(self.full.count('\\begin{table}'),2)
 def test_03_five_results_sections(self):self.assertEqual(self.main.split('\\section{Results}')[1].split('\\section{Discussion}')[0].count('\\subsection{'),5)
 def test_04_SI_item_counts(self):self.assertEqual((sum(k.startswith('fig:')for k in self.links['labels']),sum(k.startswith('tab:')for k in self.links['labels'])),(2,25))
 def test_05_every_SI_item_cited(self):self.assertEqual(set(self.links['labels']),set(self.links['main_citations']))
 def test_06_no_SI_discussion_or_workplan(self):self.assertNotIn('\\section{Discussion}',self.si);self.assertNotIn('Primary national AGB target and remaining evidence requirements',self.si)
 def test_07_abstract_limit(self):self.assertLessEqual(len(re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}',self.main,re.S)[1].split()),250)
 def test_08_seven_keywords(self):self.assertEqual(len(re.search(r'\\textbf\{Keywords:\}([^\n]+)',self.main)[1].split(';')),7)
 def test_09_exact_AI_declaration(self):self.assertIn('Arena.ai Agent Mode was used to assist with computational methods and literature review.',self.main.replace(r'\href{http://Arena.ai}{Arena.ai}','Arena.ai'))
 def test_10_ORCID(self):self.assertIn('orcid.org/0000-0002-0019-1842',self.main)
 def test_11_complete_case_set(self):
  for country in ['Brazil','Indonesia','DR Congo','Cameroon','Canada','Finland','France','Australia']:self.assertIn(country,self.main)
 def test_12_seven_cohort_ranges(self):self.assertEqual(len(self.plot['endpoint_cohorts']),7)
 def test_13_cohorts_match_original_values(self):
  with (ROOT/'data/endpoint_conversion_path_bounds_F12.csv').open()as f:rows=[r for r in csv.DictReader(f)if r['constraint_level']=='finest_reported_geography']
  for r,p in zip(rows,self.plot['endpoint_cohorts']):self.assertEqual(float(r['lower_unique_endpoint_area_ha'])/1e6,p['lower_Mha']);self.assertEqual(float(r['upper_unique_endpoint_area_ha'])/1e6,p['upper_Mha'])
 def test_14_Finnish_assumptions_visible(self):
  rr=[r for r in self.plot['inventory_intervals']if 'Finland'in r['panel']];self.assertGreater(rr[0]['lower'],0);self.assertLess(rr[1]['lower'],0)
 def test_15_France_coverage_not_conflated(self):
  rr=[r for r in self.plot['inventory_intervals']if 'France'in r['panel']];self.assertEqual(len(rr),2);self.assertTrue(any('90%'in r['label']and r['lower']==104 for r in rr));self.assertTrue(any('95%'in r['label']for r in rr))
 def test_16_Canada_not_assigned_95_percent(self):
  r=next(r for r in self.plot['inventory_intervals']if 'Canada'in r['panel']);self.assertNotIn('95',r['label']);self.assertEqual((r['lower'],r['upper']),(-21.279,56.557))
 def test_17_completion_is_not_sign_resolution(self):self.assertIn('Completion is distinct from sign resolution',self.main);self.assertIn('None of the eight calibrated national 2015--2023 forest-AGB analyses is complete',self.main)
 def test_18_account_values_match_original(self):
  with (ROOT/'data/accounts_candidate_changes_F12.csv').open()as f:d={(r['ISO3'],r['domain']):float(r['percent_change'])for r in csv.DictReader(f)if r['start']=='2015'and r['end']=='2023'}
  for r in self.plot['account_values']:self.assertEqual(d[r['country'],r['domain']],r['percent_change'])
 def test_19_all_prior_files_unchanged(self):
  for package in json.loads((ROOT/'metadata/protected_prior_identity_F15.json').read_text()):
   p=ROOT.parent/package['folder']
   if not p.exists():p=ROOT.parent/re.search(r'F\d+_A01',package['folder'])[0]
   for r in package['files']:self.assertEqual(hashlib.sha256((p/r['path']).read_bytes()).hexdigest(),r['sha256'])
 def test_20_no_reporting_accuracy_claim(self):self.assertIn('not the same as demonstrating improved reporting accuracy',self.main);self.assertIn('not calibrated ecological change',self.full)
 def test_21_secondary_account_windows_restored(self):
  with (ROOT/'data/accounts_candidate_changes_F12.csv').open()as f:rr=list(csv.DictReader(f))
  domains=['total','terrestrial_excluding_fishing','excluding_built','terrestrial_excluding_built','forest_component','per_person_total']
  for start,end,label in [('2010','2020','tab:SI_account_sensitivity_2010_2020'),('2015','2022','tab:SI_account_sensitivity_2015_2022')]:
   segment=self.si.split('\\label{'+label+'}',1)[1].split('\\end{table}',1)[0]
   for code in ['BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS']:
    vals=[next(float(r['percent_change'])for r in rr if r['ISO3']==code and r['start']==start and r['end']==end and r['domain']==d)for d in domains]
    row=code+' & '+' & '.join(f'{v:+.2f}'for v in vals)+r'\\'
    self.assertIn(row,segment)
 def test_22_all_five_primary_component_contributions(self):
  with (ROOT/'data/accounts_component_contributions_F12.csv').open()as f:rr=list(csv.DictReader(f))
  segment=self.si.split('\\label{tab:SI_component_contributions}',1)[1].split('\\end{table}',1)[0]
  for code in ['BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS']:
   for component in ['crop','grazing','forest','fishing','built']:
    value=next(float(r['contribution_percentage_points_of_initial_total'])for r in rr if r['ISO3']==code and r['start']=='2015' and r['end']=='2023' and r['component']==component)
    self.assertIn(f'{value:+.4f}',segment)
  self.assertIn('+1.186',self.main);self.assertIn('+1.505',self.main)
 def test_23_complete_forest_account_decomposition(self):
  with (ROOT/'data/accounts_forest_component_decomposition_F12.csv').open()as f:rr=list(csv.DictReader(f))
  segment=self.si.split('\\label{tab:SI_forest_decomposition}',1)[1].split('\\end{table}',1)[0]
  selected=[r for r in rr if r['ISO3']in['BRA','IDN','COD','CMR','CAN','FIN','FRA','AUS']]
  self.assertEqual(len(selected),24)
  for r in selected:
   for key in ['forest_account_difference_gha','area_contribution_gha','factor_contribution_gha']:
    self.assertIn(f'{float(r[key])/1e6:+.3f}',segment)
  self.assertIn('+2.502',self.main);self.assertIn('-0.505',self.main)
 def test_24_Indonesia_definition_and_collection_signs(self):
  self.assertIn('Forest Formation alone increases by 3,019 ha',self.main)
  self.assertIn('peat swamp forest decreases by 693,961 ha',self.main)
  self.assertIn('2.403 million-ha difference',self.main)
  with (ROOT/'data/IDN_C41_extent_changes_F12.csv').open()as f:rr=list(csv.DictReader(f))
  peat=next(r for r in rr if r['level']=='national' and r['group']=='peat_swamp_forest')
  self.assertAlmostEqual(float(peat['difference_ha']),-693961.3329118285)
 def test_25_event_and_regional_compensation_results(self):
  self.assertIn('707,004 hectare-events',self.main)
  self.assertIn('20 of 27 Brazilian states decline',self.main)
  self.assertIn('14 of 38 Indonesian provinces decline',self.main)
  with (ROOT/'data/national_mapped_regional_compensation_F12.csv').open()as f:rr=list(csv.DictReader(f))
  self.assertEqual(len(rr),2)
  for r in rr:
   self.assertEqual(r['ecological_uncertainty_assessed'],'False')
   self.assertAlmostEqual(-float(r['sum_negative_unit_net_changes_ha'])+float(r['sum_positive_unit_net_changes_ha']),float(r['national_net_ha']),places=5)
 def test_26_method_definitions_repaired(self):
  for text in ['D_t=Q_t/A_t','\\Delta Q_{\\mathrm{extent}}','G=\\sum_i[\\Delta Q_i]_+','K=1-|G-L|/(G+L)']:
   self.assertIn(text,self.si)
  self.assertIn('\\Delta\\widehat V\\pm\\sqrt{20}(s_0+s_1)',self.si)
 def test_27_Finnish_bias_and_ledger_retained(self):
  self.assertIn('17.293 million m$^3$ would exhaust',self.main)
  self.assertIn('-24.987',self.si)
  with (ROOT/'data/FIN_forest_account_stock_flow_balance_F12.csv').open()as f:rr=list(csv.DictReader(f))
  self.assertEqual(len(rr),2)
  for r in rr:self.assertAlmostEqual(float(r['opening_Mm3'])+float(r['net_increment_minus_removals_and_losses_Mm3'])+float(r['reclassification_and_balancing_Mm3']),float(r['closing_Mm3']),places=7)
 def test_28_restoration_lineage_and_audit(self):
  names=['accounts_component_contributions_F12.csv','accounts_forest_component_decomposition_F12.csv','national_mapped_transition_event_sums_F12.csv','national_mapped_regional_compensation_F12.csv','IDN_C41_extent_changes_F12.csv','IDN_C3_national_extent_sensitivity_F12.csv','FIN_forest_account_stock_flow_balance_F12.csv']
  for name in names:
   original=ROOT.parent/'ecomod_empirical_closure_F12_A01/data'/name
   self.assertEqual(hashlib.sha256((ROOT/'data'/name).read_bytes()).hexdigest(),hashlib.sha256(original.read_bytes()).hexdigest())
  audit=(ROOT/'CONTENT_COVERAGE_AUDIT_F15_A01.md').read_text()
  for phrase in ['Regional compensation','direct forest-to-oil-palm','Forest-account decomposition','Finnish stock–flow ledger','Deliberate specialist compression']:
   self.assertIn(phrase,audit)
if __name__=='__main__':unittest.main(verbosity=2)
