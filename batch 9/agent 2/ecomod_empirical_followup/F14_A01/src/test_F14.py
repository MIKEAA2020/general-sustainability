import unittest,csv,json,re,hashlib
from pathlib import Path
from build_F14 import ROOT,expand
class EditorialIntegration(unittest.TestCase):
 @classmethod
 def setUpClass(c):
  c.main=(ROOT/'integrated_F14_A01_main.tex').read_text();c.full=expand(ROOT/'integrated_F14_A01_main.tex');c.si=expand(ROOT/'integrated_F14_A01_SI.tex');c.links=json.loads((ROOT/'metadata/SI_linkage_F14.json').read_text());c.plot=json.loads((ROOT/'metadata/plot_values_F14.json').read_text())
 def test_01_six_main_figures(self):self.assertEqual(self.full.count('\\begin{figure}'),6)
 def test_02_two_main_tables(self):self.assertEqual(self.full.count('\\begin{table}'),2)
 def test_03_five_results_sections(self):self.assertEqual(self.main.split('\\section{Results}')[1].split('\\section{Discussion}')[0].count('\\subsection{'),5)
 def test_04_SI_item_counts(self):self.assertEqual((sum(k.startswith('fig:')for k in self.links['labels']),sum(k.startswith('tab:')for k in self.links['labels'])),(2,17))
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
  for package in json.loads((ROOT/'metadata/protected_prior_identity_F14.json').read_text()):
   p=ROOT.parent/package['folder']
   if not p.exists():p=ROOT.parent/re.search(r'F\d+_A01',package['folder'])[0]
   for r in package['files']:self.assertEqual(hashlib.sha256((p/r['path']).read_bytes()).hexdigest(),r['sha256'])
 def test_20_no_reporting_accuracy_claim(self):self.assertIn('not the same as demonstrating improved reporting accuracy',self.main);self.assertIn('not calibrated ecological change',self.full)
if __name__=='__main__':unittest.main(verbosity=2)
