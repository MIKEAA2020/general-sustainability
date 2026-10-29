import unittest,json,hashlib,xml.etree.ElementTree as ET
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parent/'governance_elevation_P4_v43_P02'
class GraphicalAbstractTests(unittest.TestCase):
 def setUp(self):self.claims=json.loads((ROOT/'data/graphical_abstract_claims_v43_GA01.json').read_text());self.svg=ET.parse(ROOT/'figures/graphical_abstract_governance_v43_GA01.svg').getroot();self.text=' '.join(self.svg.itertext())
 def test_source_hashes(self):
  for n,r in self.claims['sources'].items():self.assertEqual(hashlib.sha256((BASE/'data'/n).read_bytes()).hexdigest(),r['sha256'])
 def test_registered_window_scope(self):
  a=self.claims['mobilising_axis'];self.assertEqual(a['candidate'],'A');self.assertTrue(a['gated']);self.assertEqual(len(a['all_stable_windows_years']),2);self.assertIn('A, gated',self.text)
 def test_correct_interval_labels(self):
  for a,b in self.claims['mobilising_axis']['all_stable_windows_years']:self.assertIn(f'{a:.2f}–{b:.2f}',self.text)
 def test_gain_displays_conservative(self):
  self.assertLess(float(self.claims['protective']['point_gain_upper']),.475);self.assertLess(float(self.claims['protective']['box_gain_upper']),.687);self.assertIn('E₀ < M, qE₀ < r and Γ < 1',self.text)
 def test_field_result_and_limit_visible(self):self.assertIn('only 0.47%',self.text);self.assertIn('joint DDE validation is not achieved',self.text);self.assertFalse(self.claims['field']['joint_DDE_validation'])
 def test_fold_limit_visible(self):self.assertIn('≠ an existence certificate',self.text);self.assertFalse(self.claims['continuum_fold_existence_certified'])
 def test_png_resolution(self):
  with Image.open(ROOT/'figures/graphical_abstract_governance_v43_GA01.png')as im:self.assertEqual(im.size,(3600,2320))
 def test_vector_and_no_external_assets(self):
  self.assertGreater(len(list(self.svg.iter('{http://www.w3.org/2000/svg}text'))),20);self.assertEqual(len(list(self.svg.iter('{http://www.w3.org/2000/svg}image'))),0)
 def test_pdf_available(self):self.assertEqual((ROOT/'figures/graphical_abstract_governance_v43_GA01.pdf').read_bytes()[:5],b'%PDF-')
 def test_caption_implementation_scope(self):
  s=(ROOT/'CAPTION_graphical_abstract_v43_GA01.md').read_text();self.assertIn('does not transfer to Euler',s);self.assertIn('non-confirmatory',s);self.assertIn('not fishery-calibrated',s)
if __name__=='__main__':unittest.main()
