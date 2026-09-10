#!/usr/bin/env python3
"""v3 gate checks — implements the `deepseek e3 and e4.txt` review (rev 5).

STRICT DISCIPLINE: reads ONLY already-computed J-17/J-27 results. Computes NO
statistic on the Barton Springs / Lovelady pool. Enumerates the v3 multiplicity
grid and re-derives the M1-loss erratum exactly.
"""
import json, os
from itertools import product

R = os.path.join(os.path.dirname(__file__), '..', 'results')
load = lambda n: json.load(open(os.path.join(R, n)))
ctl, exp, sch = load('j27_controls_strengthening.json'), load('j27_exploratory.json'), load('claim_schema_results.json')
out = {}

# --- 1. Erratum (review §5.4): M1's edge over persistence vs head AC(1) -------
rho = {'J-17': sch['pools']['J-17']['claims']['E3_mechanism']['rho_H_head_persistence'],
       'Uvalde': sch['pools']['Uvalde']['claims']['E3_mechanism']['rho_H_head_persistence']}
j17f, j17m = ctl['C1_j17_window']['full'], ctl['C1_j17_window']['matched_1941']
uv = exp['runs']['primary_Basin1+2']['rmse']
rows = [('J-17 (full window)',      rho['J-17'],   j17f['persist'], j17f['M1']),
        ('J-17 (matched 1941-)',    rho['J-17'],   j17m['persist'], j17m['M1']),
        ('Uvalde (native window)',  rho['Uvalde'], uv['naive_persist']['1'], uv['M1']['1'])]
out['erratum_M1_edge'] = [
    {'pool': n, 'head_ac1': round(r, 5), 'persist_h1': round(p, 4), 'M1_h1': round(m, 4),
     'M1_edge': round(p - m, 4), 'M1_wins': bool(p - m > 0)} for n, r, p, m in rows]
# monotone in AC(1)? (2 J-17 windows share rho, so compare across pools)
edges = {n: p - m for n, r, p, m in rows}
out['erratum_monotone_in_ac1'] = bool(min(edges['J-17 (full window)'], edges['J-17 (matched 1941-)']) > edges['Uvalde (native window)'])

# --- 2. H1/H2 decision table (review §4.3) -----------------------------------
out['H_failure_rules'] = {
    'H1_fails_a_ge_1':  'SCOPE EXCLUSION — H*0 undefined; pool is not a valid test object. Report, do not score.',
    'H2_fails_gamma_ge_0': 'SCOPE EXCLUSION — lemma void; pumping does not lower the fixpoint. Report, do not score.',
    'H1_H2_hold_sign_wrong': 'FALSIFICATION — the v3 prediction is refuted.',
    'H1_H2_hold_sign_right': 'CORROBORATION — one confirmatory instance.',
    'margin_knife_edge_abs_m_le_2ft': 'INDETERMINATE — reported, scored as neither (record §4 rule 1).'}

# --- 3. Multiplicity enumeration (review §5.3) -------------------------------
# Rev 3: thresholds are now the DECLARED BSEACD trigger levels established by gate 2
# (Smith et al. 2013 DTM; Mgmt Plan 2022 Table 1-1) plus the two GMA-10 DFCs.
grid = {'thresholds': ['DFC_6.5cfs', 'DFC_49.7cfs', 'StageIII_Critical_20cfs',
                       'StageIV_Exceptional_14cfs', 'ERP_10cfs'],
        'floors': ['drought_of_record', 'q05', 'q10'],
        'driver_defs': ['recharge_primary', 'recharge_alt', 'springflow_lag0', 'springflow_lag1'],
        'specifications': ['springflow_units(primary)', 'Lovelady_head(conditional)']}
cells = list(product(*grid.values()))
n = len(cells)
out['multiplicity'] = {
    'grid': {k: len(v) for k, v in grid.items()},
    'n_primary_comparisons': n,
    'n_with_2_horizons': n * 2,
    'note': 'Margin sign is a derived readout of each cell, not an extra multiplier.',
    'correction': 'Holm-Bonferroni within family; family = one specification x all thresholds x floors x drivers.',
    'family_size': n // len(grid['specifications']),
    'alpha_family': 0.05,
    'alpha_per_test_bonferroni': round(0.05 / (n // len(grid['specifications'])), 5)}

print(json.dumps(out, indent=2))
json.dump(out, open(os.path.join(R, 'v3_gate_checks.json'), 'w'), indent=2)
