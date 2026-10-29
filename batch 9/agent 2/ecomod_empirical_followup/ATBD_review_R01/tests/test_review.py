from pathlib import Path
import json,hashlib,unittest,csv,sys
from unittest.mock import patch
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P/'src'))
from verify_official_text import RangeReader
class ReviewChecks(unittest.TestCase):
 def test_chunk_pages_exact_cover(self):
  rows=json.loads((P/'metadata/source_registry.json').read_text())['chunks'];pages=[i for r in rows for i in range(r['start_page'],r['end_page']+1)];self.assertEqual(sorted(pages),list(range(1,139)));self.assertEqual(len(rows),12)
 def test_all_chunk_release_digests(self):
  a={r['name']:r for r in json.loads((P/'metadata/release_assets.json').read_text())['assets']}
  for r in json.loads((P/'metadata/source_registry.json').read_text())['chunks']:self.assertEqual('sha256:'+r['sha256'],a[r['filename']]['digest']);self.assertEqual(r['bytes'],a[r['filename']]['size'])
 def test_missing_upload_range_recovered(self):
  rows=json.loads((P/'metadata/source_registry.json').read_text())['chunks'];names={x['filename']for x in rows};expected=json.loads((P/'metadata/review_scope.json').read_text())['parts_missing_from_uploads_recovered_from_release'];self.assertEqual(expected,['106-110.pdf','111-115.pdf','116-120.pdf']);self.assertTrue(set(expected)<=names)
 def test_text_comparison_scope(self):
  d=json.loads((P/'metadata/official_text_comparison.json').read_text());self.assertEqual(len(d['page_text_comparisons']),138);self.assertTrue(all(x['same_whitespace_normalized_text']for x in d['page_text_comparisons']));self.assertLessEqual(d['distinct_bytes_accessed'],25000000);self.assertFalse(d['whole_file_downloaded']);self.assertFalse(d['images_compared']);self.assertTrue(d['range_cap_encountered_in_optional_object_reads'])
 def test_no_manuscript_or_admission_changes(self):
  d=json.loads((P/'metadata/review_scope.json').read_text());self.assertTrue(d['no_F09_manuscript_created']);self.assertTrue(d['all_8_national_admissions_unchanged_on_hold'])
 def test_f08_baseline_unchanged(self):
  root=P.parent/'ecomod_followup_F08'
  if not root.exists():root=P.parent/'ecomod_empirical_followup/F08'
  if not root.exists():self.skipTest('Published F08 baseline package not supplied alongside review')
  m=json.loads((root/'artifact_manifest.json').read_text())
  for x in m['files']:self.assertEqual(hashlib.sha256((root/x['path']).read_bytes()).hexdigest(),x['sha256'])
 def test_evidence_page_mapping(self):
  with (P/'EVIDENCE_MATRIX_R01.csv').open()as f:rows=list(csv.DictReader(f))
  self.assertEqual(len(rows),14)
  for r in rows:self.assertTrue(r['source_asset_urls']);self.assertTrue(all(1<=int(i)<=138 for i in r['original_PDF_pages'].split(';')))
 def test_no_source_pdf_redistribution(self):self.assertFalse(list(P.rglob('*.pdf')));self.assertFalse((P/'pages.json').exists())
 def test_reader_cache_seek_and_slice(self):
  r=RangeReader('https://example.invalid',10,'etag');r.blocks[0]=b'0123456789';self.assertEqual(r.read(3),b'012');r.seek(-2,2);self.assertEqual(r.read(),b'89');self.assertEqual(r.tell(),10)
 def test_reader_range_cap_fails_before_request(self):
  r=RangeReader('https://example.invalid',100000,'etag',cap=10)
  with patch.object(r.s,'get',side_effect=RuntimeError('Should not request'))as get:
   with self.assertRaises(ValueError):r.read(1)
   get.assert_not_called();self.assertTrue(r.cap_encountered)
if __name__=='__main__':unittest.main()
