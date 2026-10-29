"""Document/inheritance and analytic-identity checks, not ecological validation."""
import csv
import hashlib
import json
import math
from pathlib import Path
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text())


class ScientificScopeF09Tests(unittest.TestCase):
    def test_inherited_files_unchanged(self):
        for rel, expected in load('metadata/inherited_unchanged_files_F09.json').items():
            self.assertEqual(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest(), expected, rel)

    def test_original_F08_remains_unchanged_when_present(self):
        baseline = ROOT.parent / 'ecomod_followup_F08'
        if not baseline.exists():
            self.skipTest('Original F08 not present in standalone package')
        manifest = json.loads((baseline / 'artifact_manifest.json').read_text())
        for item in manifest['files']:
            self.assertEqual(hashlib.sha256((baseline / item['path']).read_bytes()).hexdigest(), item['sha256'], item['path'])

    def test_original_numerical_data_identical(self):
        baseline = ROOT.parent / 'ecomod_followup_F08/data'
        if not baseline.exists():
            self.skipTest('Original F08 not present')
        for p in baseline.rglob('*'):
            if p.is_file():
                self.assertEqual(p.read_bytes(), (ROOT / 'data' / p.relative_to(baseline)).read_bytes())

    def test_eight_holds_unchanged(self):
        with (ROOT / 'data/support/physical_admission_F08.csv').open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(r['admission'] == 'hold_not_admitted' for r in rows))

    def test_four_source_identities_under_guard(self):
        rows = load('metadata/companion_review_F09/source_registry_F09.json')['documents']
        self.assertEqual({r['key'] for r in rows}, {'E3UB', 'PVIR', 'PVP', 'ADPC'})
        self.assertEqual(sum(r['pages'] for r in rows), 202)
        for r in rows:
            self.assertLessEqual(r['bytes'], 25000000)
            self.assertEqual(len(r['sha256']), 64)
            self.assertIn('/media/documents/', r['final_url'])
            self.assertTrue(r['full_download_success'])

    def test_review_scope_does_not_claim_complete_review_or_validation(self):
        r = load('metadata/companion_review_F09/review_scope_F09.json')
        for k in ['all_pages_closely_reviewed', 'raw_source_pdf_text_or_images_redistributed',
                  'new_paired_reference_acquired', 'provider_executable_implementation_verified',
                  'local_covariance_estimated', 'local_change_coverage_calibrated', 'national_admission_changed']:
            self.assertFalse(r[k], k)
        self.assertEqual(r['visually_opened_pdf_pages']['E3UB'], [23, 24, 25, 26, 28])

    def test_evidence_matrix_complete_distinct(self):
        with (ROOT / 'EVIDENCE_MATRIX_F09.csv').open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 22)
        self.assertEqual(len({r['id'] for r in rows}), 22)
        self.assertTrue(all(r['limit'] and r['pdf_pages'] for r in rows))

    def test_provider_examples_are_unpaired_stock_summaries(self):
        with (ROOT / 'data/reference/provider_stock_examples_F09.csv').open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 16)
        self.assertEqual({r['map_year'] for r in rows}, {'2015', '2023'})
        self.assertTrue(all(r['paired_change_observations'] == 'no' for r in rows))
        for r in rows:
            self.assertEqual((r['source_table'], r['source_pdf_page']), ('66', '64') if r['map_year'] == '2015' else ('74', '67'))
        self.assertTrue(any(float(r['reported_MD_Mg_ha']) < 0 for r in rows))
        self.assertTrue(any(float(r['reported_MD_Mg_ha']) > 0 for r in rows))

    def test_average_independent_equal_variances(self):
        for n in [1, 2, 5, 10]:
            w = np.ones(n) / n
            covariance = np.eye(n) * 4
            self.assertAlmostEqual(float(w @ covariance @ w), 4 / n)
            self.assertAlmostEqual(float(covariance.sum() / n**2), 4 / n)

    def test_perfect_spatial_dependence_does_not_gain_independent_precision(self):
        for n in [1, 2, 5]:
            w = np.ones(n) / n
            self.assertAlmostEqual(float(w @ np.full((n, n), 4.) @ w), 4.)

    def test_total_and_average_have_distinct_normalization(self):
        c = np.diag([4., 4.])
        w = np.array([.5, .5])
        area = np.array([2., 2.])
        self.assertAlmostEqual(float(w @ c @ w), 2.)
        self.assertAlmostEqual(float(area @ c @ area), 32.)

    def test_endpoint_covariance_sign_changes_difference_variance(self):
        contrast = np.array([-1., 1.])
        for correlation in [-1., -.5, 0., .5, 1.]:
            c = np.array([[4., 4. * correlation], [4. * correlation, 4.]])
            self.assertGreaterEqual(np.linalg.eigvalsh(c).min(), -1e-12)
            self.assertAlmostEqual(float(contrast @ c @ contrast), 8. - 8. * correlation)

    def test_general_spatiotemporal_block_identity(self):
        m = np.array([[1., 0., 1., 0.], [0., 2., 0., 1.], [1., 0., 2., 1.], [0., 1., 0., 3.]])
        joint = m @ m.T
        a = np.array([2., 3.])
        contrast = np.r_[-a, a]
        blocks = joint[2:, 2:] + joint[:2, :2] - joint[2:, :2] - joint[:2, 2:]
        self.assertAlmostEqual(float(contrast @ joint @ contrast), float(a @ blocks @ a))

    def test_prior_variogram_equations_imply_decay_not_increase(self):
        nugget, sill, rate = 2., 10., .0445
        for distance in [0., 1., 10., 100.]:
            v = nugget * math.exp(-rate * distance) + sill * (1 - math.exp(-rate * distance))
            r = 1 - (v - nugget) / (sill - nugget)
            self.assertAlmostEqual(r, math.exp(-rate * distance))
        self.assertEqual(1 - math.exp(0), 0)

    def test_systematic_difference_not_removed_by_random_covariance(self):
        area = np.array([2., 3.])
        b0, b1 = np.array([1., 1.]), np.array([2., 0.])
        self.assertAlmostEqual(float(area @ (b1 - b0)), -1.)

    def test_new_journal_text_acknowledges_stock_validation(self):
        main = (ROOT / 'followup_F09_main.tex').read_text()
        self.assertIn('stock validation includes the primary endpoint years', main)
        self.assertIn('within-stack correlation assumption of 0.5 is not an estimate', main)
        self.assertIn('absence of such a model here is not a claim', main)
        self.assertIn('ATBD2025', main)
        self.assertIn('PVIR2026', main)

    def test_equation_discrepancy_log_stays_external(self):
        report = (ROOT / 'SOURCE_REVIEW_F09.md').read_text()
        self.assertIn('3-19', report)
        self.assertIn('1/N', report)
        for name in ['main', 'SI']:
            text = (ROOT / f'followup_F09_{name}.tex').read_text()
            self.assertNotIn('printed-equation inconsistencies', text)
            self.assertNotIn('independent reconstruction', text)
            self.assertNotIn('computational verification', text)

    def test_no_full_provider_documents_or_text_redistributed(self):
        for filename in ['E3UB.pdf', 'PVIR.pdf', 'PVP.pdf', 'ADPC.pdf',
                         'E3UB_pages.json', 'PVIR_pages.json', 'PVP_pages.json', 'ADPC_pages.json']:
            self.assertEqual(list(ROOT.rglob(filename)), [])


if __name__ == '__main__':
    unittest.main()
