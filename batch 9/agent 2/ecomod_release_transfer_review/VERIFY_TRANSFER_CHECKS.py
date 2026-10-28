"""Bounded release-transfer checks; no model fitting, network calls or manuscript edits.

Usage:
  python VERIFY_TRANSFER_CHECKS.py --out CHECK_RESULTS.json
  python VERIFY_TRANSFER_CHECKS.py --release-zip /path/to/workspace-edwards.framework.2nd.zip --out CHECK_RESULTS.json

Archive checks reaggregate stored scores/flags, not independently rerun their models.
Algebraic examples are synthetic model illustrations, not ecological observations.
"""
import argparse
import csv
import hashlib
import io
import json
import math
import zipfile
from collections import defaultdict
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--release-zip', type=Path)
    ap.add_argument('--out', type=Path, default=Path('CHECK_RESULTS.json'))
    args = ap.parse_args()
    out = {'scope': 'Algebra checks and optional stored-artifact reaggregation only; no empirical validation, forecast rerun or proof audit.'}

    # C12 illustrative account/area relation, using its declared baseline parameters.
    bf, total, amin, lo, hi, B, C = .85, 2.5, .05, .05, .066, .825, .04
    Af = (B - C) / bf
    aggregate_upper = min(total, B / lo, (bf * total - B) / (bf - hi))
    area_bounds = [max(amin, C / hi), min(total - Af, C / lo)]
    assert area_bounds[0] < .7 < area_bounds[1]  # Arbitrary illustrative cut, NOT ecological threshold.
    endpoints = []
    for ac, u, q in [(area_bounds[0], hi, .5), (area_bounds[1], lo, 1.)]:
        ar = total - Af - ac
        assert ar >= 0 and abs(bf * Af + u * ac - B) < 1e-12
        assert abs((.05 + .8 * .08 * q * (1 - q)) - u) < 1e-12
        endpoints.append({'Ac_ha': ac, 'Af_ha': Af, 'Ar_ha': ar, 'q': q, 'Ups_gha_per_ha': u, 'B_gha': bf * Af + u * ac})
    u_q09 = .05 + .8 * .08 * .9 * .1
    out['C12_partial_identification_example'] = {
        'kind': 'Instantaneous model-compatible states, not observed forest data or dynamic reachability',
        'inputs': {'bf': bf, 'A_total': total, 'Ac_min': amin, 'Ups_range': [lo, hi], 'B': B, 'capital_contribution_C': C},
        'B_only_Ac_bounds_ha': [amin, aggregate_upper],
        'B_plus_independent_Af_Ac_bounds_ha': area_bounds,
        'independent_Af_ha': Af,
        'endpoint_witnesses': endpoints,
        'known_q09_implies_Ac_ha': C / u_q09,
        'illustrative_cut_ha': .7,
        'cut_is_ecological_threshold': False,
        'claim': 'Independent Af narrows but does not eliminate area ambiguity; known q and baseline parameters identify area in this toy observation equation.'}

    rho = .08
    caps = {str(q): 1 / (rho * q) for q in [.1, .5, .9]}
    assert caps['0.9'] < 20 < 40 and caps['0.1'] > 40
    out['constant_history_delay_screen'] = {
        'formula': 'For qmax=1 and constant 0<q0<1, t_cap=1/(rho*q0), provided tau>=t_cap. Until tau, delayed input is constant; after the imposed cap, q stays fixed.',
        'rho_per_year': rho,
        'candidate_t_cap_years': caps,
        'interpretation': 'For q0=.9, delays 20 and 40 both exceed t_cap and are structurally indistinguishable on this quality trajectory. For q0=.1 this particular pre-delay-cap argument does not apply at 20/40; no new trajectory simulation was performed.'}

    # Full C12 bookkeeping identity, checked at an illustrative admissible state.
    af, ac, ar, q, debt = .6, 1.5, .4, .3, .2
    alpha, eta, tb, tb_dot = .03, .05, .15, .01
    bfast = (.85 + tb) * math.exp(-alpha * debt)
    ups = .05 + .8 * .08 * q * (1-q)
    Bnow, E = bfast * af + ups * ac, .5
    shortfall = max(E - .5 * Bnow, 0)  # Reserved-share extension, not baseline.
    uc = min(shortfall / bfast, ac - .05)
    restoration = .1 * ar * max(Bnow - E, 0)
    M = .06 * ar - .05 * af
    dq = .08 * .2 * .8  # Delayed q=.2, current q=.3; cap inactive.
    dD = max(E - Bnow, 0) - eta * debt
    dbf = math.exp(-alpha * debt) * tb_dot - alpha * bfast * dD
    ups_prime = .8 * .08 * (1 - 2*q)
    terms = {'conversion': (bfast-ups)*uc, 'maintenance_retirement': bfast*M,
             'restoration': ups*restoration, 'quality': ups_prime*ac*dq, 'fast_yield': af*dbf}
    direct = bfast*(uc+M) + af*dbf + ups*(-uc+restoration) + ac*ups_prime*dq
    assert abs(sum(terms.values()) - direct) < 1e-12
    out['full_C12_account_derivative_identity'] = {
        'kind': 'Synthetic instantaneous algebra check, not an integrated trajectory or empirical attribution',
        'units': 'All derivative terms are gha per year',
        'terms': terms, 'direct_chain_rule': direct, 'closure_error': sum(terms.values())-direct,
        'scope': 'Reserved-share extension permits simultaneous conversion/restoration in this example; no claim that these are baseline-run quantities.'}

    # A005 caution: internal exchange cancels in capacity-weighted storage, not head sum.
    cL, dF, Cf, gap = .4, .2, 1., 10.
    Cs = cL * Cf / dF
    dhf, dhs = -cL * gap, dF * gap
    assert abs(Cf * dhf + Cs * dhs) < 1e-12 and abs(dhf + dhs) > 1
    out['two_pool_head_vs_storage_check'] = {
        'kind': 'Synthetic algebraic counterexample to unweighted-head cancellation',
        'inputs': {'cL': cL, 'dF': dF, 'Cf': Cf, 'Cs': Cs, 'head_gap': gap},
        'unweighted_head_sum_change': dhf + dhs,
        'weighted_storage_change': Cf * dhf + Cs * dhs,
        'scope': 'Internal leakage terms only; external fluxes, constants and own-persistence terms omitted deliberately. Not a rerun or full audit of A005.'}

    baseline_errors = [1., 10.]
    naive_all = math.sqrt(sum(x*x for x in baseline_errors) / 2)
    out['paired_support_example'] = {
        'kind': 'Synthetic missing-case illustration, not a release empirical result',
        'baseline_rmse_both_cases': naive_all,
        'candidate_rmse_easy_case_only': 1.,
        'baseline_rmse_same_easy_case': 1.,
        'interpretation': 'Apparent improvement from dropping the difficult case disappears on identical support; coverage must be reported separately.'}

    if args.release_zip:
        expected = 'workspace-edwards.framework.2nd.zip'
        archive_sha = hashlib.sha256(args.release_zip.read_bytes()).hexdigest()
        if archive_sha != '3de14e2086ff4f92144882e4f60cae249d18f7f48af07410a0fc207a869d8922':
            raise ValueError('Release ZIP hash differs from the reviewed asset; obtain the pinned asset or review the changed archive separately.')
        source_hashes = {}
        with zipfile.ZipFile(args.release_zip) as z:
            def readcsv(name):
                data = z.read(name)
                source_hashes[name] = hashlib.sha256(data).hexdigest()
                return list(csv.DictReader(io.StringIO(data.decode())))
            rows = readcsv('wave_e_edwards/results/twopool_fixed_window_scores.csv')
            grouped = defaultdict(list)
            for r in rows:
                grouped[r['window']].append(r)
            scores = []
            for window, rs in grouped.items():
                h = next(r for r in rs if r['model'] == 'H1_two_pool')
                base = min((r for r in rs if r['model'] != 'H1_two_pool'), key=lambda r: float(r['rmse']))
                scores.append({'window': window, 'H1_RMSE_ft': float(h['rmse']), 'best_baseline': base['model'], 'best_baseline_RMSE_ft': float(base['rmse']), 'wins_5pct_margin': float(h['rmse']) <= .95 * float(base['rmse'])})
            assert len(scores) == 4 and not any(x['wins_5pct_margin'] for x in scores)
            rows = readcsv('wave_e_cod/results/sim_retention_power.csv')
            structural = defaultdict(list)
            null = defaultdict(dict)
            for r in rows:
                yes = r['retained'] == 'True'
                if r['module'] == r['truth']:
                    structural[(r['dgp'], r['sigma'])].append(yes)
                if r['dgp'].startswith('D5'):
                    key = (r['dgp'], r['sigma'])
                    null[key][r['rep']] = null[key].get(r['rep'], False) or yes
            powers = [{'dgp': k[0], 'sigma': float(k[1]), 'replicates': len(v), 'stored_truth_retained_fraction': sum(v)/len(v)} for k,v in sorted(structural.items())]
            specs = [{'dgp': k[0], 'sigma': float(k[1]), 'replicates': len(v), 'stored_none_retained_fraction': 1-sum(v.values())/len(v)} for k,v in sorted(null.items())]
            rows = readcsv('wave_e_cod/results/sim_misspecified_D6D7.csv')
            grouped = defaultdict(dict)
            for r in rows:
                key = (r['cell'], r['sigma'])
                grouped[key][r['rep']] = grouped[key].get(r['rep'], False) or r['retained'] == 'True'
            miss = [{'cell': k[0], 'sigma': float(k[1]), 'replicates': len(v), 'stored_any_retained_fraction': sum(v.values())/len(v)} for k,v in sorted(grouped.items())]
        out['release_artifact_checks'] = {'expected_asset_name': expected, 'asset_sha256': archive_sha, 'input_member_sha256': source_hashes, 'two_pool_scores': scores, 'in_class_power_flags_reaggregated': powers, 'null_specificity_flags_reaggregated': specs, 'misspecification_flags_reaggregated': miss, 'limitation': 'Stored scores and retention flags only. Does not validate model fits, simulate truths again, establish registration timing, or independently reconstruct the retention rule.'}
    else:
        out['release_artifact_checks'] = {'status': 'Not run; pass --release-zip to inspect stored CSV artifacts.'}
    args.out.write_text(json.dumps(out, indent=2) + '\n')
    print('Checks passed; wrote', args.out)

if __name__ == '__main__':
    main()
