"""F10 scientific scope/preservation checks, not ecological validation."""
from pathlib import Path
import csv,hashlib,json,unittest
ROOT=Path(__file__).resolve().parents[1]
def load(n):return json.loads((ROOT/n).read_text())
class NewEvidenceF10Tests(unittest.TestCase):
 def test_f09_inherited_paths_unchanged(self):
  for rel,sha in load('metadata/inherited_unchanged_files_F10.json').items():self.assertEqual(hashlib.sha256((ROOT/rel).read_bytes()).hexdigest(),sha,rel)
 def test_original_f09_manifest_when_present(self):
  base=ROOT.parent/'ecomod_followup_F09'
  if not base.exists():self.skipTest('Protected F09 not present')
  for r in json.loads((base/'artifact_manifest_F09.json').read_text())['files']:self.assertEqual(hashlib.sha256((base/r['path']).read_bytes()).hexdigest(),r['sha256'])
 def test_all_f09_data_identical_when_present(self):
  base=ROOT.parent/'ecomod_followup_F09/data'
  if not base.exists():self.skipTest('Protected F09 not present')
  for p in base.rglob('*'):
   if p.is_file():self.assertEqual(p.read_bytes(),(ROOT/'data'/p.relative_to(base)).read_bytes())
 def test_sd_counts_csv_and_audit_agree(self):
  with (ROOT/'data/reference/native_sd_summary_R03.csv').open()as f:rows=list(csv.DictReader(f))
  self.assertEqual([int(r['positive_agb_zero_sd'])for r in rows],[1032,946])
  for a,r in zip(load('metadata/native_sd_audit_R03.json')['rows'],rows):self.assertEqual(a['year'],int(r['year']))
 def test_reference_four_rows_not_paired(self):
  with (ROOT/'data/reference/local_reference_candidate_R03.csv').open()as f:rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),4);self.assertTrue(all(r['eligible_primary_2015_2023']=='no'for r in rows));self.assertEqual(rows[-1]['Year'],'')
 def test_main_records_findings_without_zero_error_claim(self):
  t=(ROOT/'followup_F10_main.tex').read_text()
  for s in ['1,032','946','44,021','not evidence of zero true error','Biomass-reference eligibility','not a compatible paired 2015--2023 sample']:self.assertIn(s,t)
 def test_si_retains_quantization_uncertainty(self):
  t=(ROOT/'followup_F10_SI.tex').read_text()
  for s in ['no unverified SD floor','more than one plot','original census dates','not assigned a 2023 epoch']:self.assertIn(s,t)
 def test_correct_reference_author_and_status(self):
  t=(ROOT/'followup_F10_main.tex').read_text();self.assertIn('Araza, A., Herold, M., Avitabile, V.',t);self.assertIn('Bielig, C.',t);self.assertIn('preprint, posted 9 January 2026',t);self.assertNotIn('Naraza',t)
 def test_declared_source_guards_not_full_zip_claim(self):
  a=load('metadata/reference_archive_inspection_R03.json');self.assertEqual(a['unique_source_bytes_represented'],22551986);self.assertFalse(a['whole_archive_md5_verified']);self.assertFalse(a['new_reference_admitted'])
 def test_author_controls(self):
  t=(ROOT/'followup_F10_main.tex').read_text();self.assertIn(r'\href{https://orcid.org/0000-0002-0019-1842}',t)
  self.assertIn('Agent Mode was used to assist with computational methods and literature review.',t)
  self.assertEqual(len(load('configs/study_design.json')['keywords']),7)
 def test_no_source_access_diary_in_manuscripts(self):
  for part in ['main','SI']:
   t=(ROOT/f'followup_F10_{part}.tex').read_text()
   for forbidden in ['22,551,986','HTTP 403','Content-Range','Git-blob','R03','printed-equation inconsistencies']:self.assertNotIn(forbidden,t)
 def test_no_new_covariance_or_admission(self):
  a=load('metadata/native_sd_audit_R03.json')
  for k in ['new_error_covariance_estimated','confidence_intervals','zero_origin_verified','country_admissions_changed']:self.assertFalse(a[k])
if __name__=='__main__':unittest.main()
