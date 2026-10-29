#!/usr/bin/env python3
"""Exploratory, fixed-support point-map identification analysis; not change validation.
No native arrays are redistributed. Reacquisition is bounded and hash-guarded by
unchanged inherited code. All primary intervals retain unrestricted allocation.
"""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'inherited_F10'
sys.path.insert(0, str(BASE / 'src'))
from allocation_envelopes import native, ROOT as INHERITED_ROOT

GROUPS = ('forest_formations', 'formations_plus_savanna')
SCALES = (1, 2, 4, 8, 16, 32, 64, 128, 256)
CONTRASTS = (1., 1.5, 2., 3., 5., 10., 100., math.inf)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def block_sum(a, side):
    a = np.asarray(a)
    require(a.ndim == 2 and isinstance(side, (int, np.integer)) and side > 0,
            'Positive integer block size and two-dimensional array required')
    n, m = a.shape
    require(n % side == 0 and m % side == 0, 'Blocks must exactly partition support')
    return a.reshape(n // side, side, m // side, side).sum(axis=(1, 3))


def topology_bounds(q, counts, totals, side=1):
    """Sharp endpoints conditional on observing only each block's total mass.
    Counts certify positive-area overlap; no floating fraction tolerance is used.
    At coarse scales mass can move inside a block, not between blocks.
    """
    q, counts, totals = np.asarray(q), np.asarray(counts), np.asarray(totals)
    require(q.shape == counts.shape == totals.shape, 'Arrays must align')
    require(np.isfinite(q).all() and (q >= 0).all(), 'Finite nonnegative mass required')
    require((totals > 0).all() and (counts >= 0).all() and (counts <= totals).all(),
            'Invalid intersection counts')
    require(np.issubdtype(counts.dtype, np.integer) and np.issubdtype(totals.dtype, np.integer),
            'Topology must use integer intersection counts')
    mass = block_sum(q, side)
    c, n = block_sum(counts, side), block_sum(totals, side)
    return float(mass[c == n].sum()), float(mass[c > 0].sum())


def canonical_fractions(raw, counts, totals):
    """Set only integer-certified pure/absent fractions to their exact values.
    No tolerance decides membership. Mixed fractions remain strictly interior.
    """
    f = np.asarray(raw, dtype=float).copy()
    counts, totals = np.asarray(counts), np.asarray(totals)
    require(f.shape == counts.shape == totals.shape and np.isfinite(f).all(),
            'Invalid fraction alignment')
    require(np.issubdtype(counts.dtype, np.integer) and np.issubdtype(totals.dtype, np.integer)
            and (totals > 0).all() and (counts >= 0).all() and (counts <= totals).all(),
            'Invalid integer geometry')
    absent, pure = counts == 0, counts == totals
    require(np.all(np.abs(f[absent]) <= 1e-12) and np.all(np.abs(f[pure] - 1) <= 1e-12),
            'Certified endpoint disagrees with area fraction')
    f[absent], f[pure] = 0., 1.
    require(((f[~(absent | pure)] > 0) & (f[~(absent | pure)] < 1)).all(),
            'Mixed support must have strictly interior computed area fraction')
    return f


def contrast_fractions(f, ratio):
    """Exact feasible group-mass fractions for density contrast bounded by ratio.
    Both densities nonnegative and d_g <= ratio*d_h, d_h <= ratio*d_g.
    Pure and absent cells are handled separately. Infinity is the PRIMARY model.
    """
    f = np.asarray(f, dtype=float)
    require(np.isfinite(f).all() and ((f >= 0) & (f <= 1)).all(), 'Invalid fractions')
    require(not math.isnan(ratio) and ratio >= 1, 'Contrast ratio must be >= 1')
    lo, hi = np.zeros_like(f), np.zeros_like(f)
    pure, mixed = f == 1, (f > 0) & (f < 1)
    lo[pure] = hi[pure] = 1
    if math.isinf(ratio):
        hi[mixed] = 1
    else:
        z = f[mixed]
        lo[mixed] = z / (z + ratio * (1 - z))
        hi[mixed] = ratio * z / (ratio * z + 1 - z)
    return lo, hi


def contrast_interval(q0, q1, f0, f1, ratio):
    bounds = []
    for q, f in ((q0, f0), (q1, f1)):
        q = np.asarray(q, dtype=float)
        require(np.isfinite(q).all() and (q >= 0).all() and q.shape == np.shape(f),
                'Finite aligned nonnegative mass required')
        lo, hi = contrast_fractions(f, ratio)
        bounds.append((float(np.sum(q * lo)), float(np.sum(q * hi))))
    return bounds[1][0] - bounds[0][1], bounds[1][1] - bounds[0][0]


def cancellation(q0, q1, side):
    d = block_sum(q1, side) - block_sum(q0, side)
    gains, losses = float(d[d > 0].sum()), float(-d[d < 0].sum())
    total = gains + losses
    net = gains - losses
    return dict(net_Mg=net, gains_Mg=gains, losses_Mg=losses,
                total_variation_Mg=total,
                cancellation=None if total == 0 else 1 - abs(net) / total)


def witness(q0, q1, c0, c1, n0, n1, direction):
    """Construct exact extremal per-cell group allocations; return certificates only.
    Do not serialize q or cell allocations (provider native arrays are not republished).
    """
    require(direction in ('minimum', 'maximum'), 'Unknown witness direction')
    arrays = []
    for index, (q, c, n) in enumerate(((q0, c0, n0), (q1, c1, n1))):
        lower = direction == 'minimum' if index == 1 else direction != 'minimum'
        x = np.where(c == n, q, 0.) if lower else np.where(c > 0, q, 0.)
        require((x >= 0).all() and (x <= q).all(), 'Nonnegative partition failed')
        require((x[c == 0] == 0).all() and (x[c == n] == q[c == n]).all(),
                'Geometry constraint failed')
        arrays.append(x)
    return dict(direction=direction, mass_2015_Mg=float(arrays[0].sum()),
                mass_2023_Mg=float(arrays[1].sum()),
                difference_Mg=float(arrays[1].sum() - arrays[0].sum()),
                cell_constraints_satisfied=True, cells_per_endpoint=int(q0.size),
                native_cell_totals_unchanged=True,
                extra_density_cap_or_temporal_constraint=False)


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run(cache, offline=False):
    require(INHERITED_ROOT == BASE, 'Wrong inherited source loaded')
    provenance = json.loads((BASE / 'metadata/native_probe_provenance.json').read_text())
    native_rows = [r for r in provenance['native_payloads'] if r['ISO3'] == 'BRA']
    require({r['year'] for r in native_rows} == {2015, 2023}, 'Unexpected endpoint set')
    a = {r['year']: native(r, cache, offline) for r in native_rows}
    support = np.load(BASE / 'data/brazil/BRA_F05_support_fractions.npz')
    topology = np.load(BASE / 'data/allocation/overlap_certificates_F07.npz')
    area = support['cell_area_ha']
    require(area.shape == (256, 256) and np.isfinite(area).all() and (area > 0).all(),
            'Wrong fixed support')
    q = {year: area * a[year]['agb'] for year in (2015, 2023)}
    for year in (2015, 2023):
        require(a[year]['agb'].shape == area.shape and a[year]['agb_sd'].shape == area.shape,
                'Wrong native source dimensions')
        require(np.isfinite(a[year]['agb']).all() and (a[year]['agb'] >= 0).all(),
                'Invalid or missing AGB; no imputation allowed')
    sd_rows = []
    for year in (2015, 2023):
        agb, sd = a[year]['agb'], a[year]['agb_sd']
        valid = (agb >= 0) & (agb <= 10000) & (sd >= 0) & (sd <= 10000)
        atzero = agb[(agb > 0) & (sd == 0)]
        positive_sd = sd[agb > 0]
        quantiles = np.quantile(positive_sd, [0, .25, .5, .75, 1])
        sd_rows.append(dict(year=year, cells=int(agb.size), joint_valid=int(valid.sum()),
            agb_fill=int((agb == -32768).sum()), sd_fill=int((sd == -32768).sum()),
            zero_agb=int((agb == 0).sum()), zero_sd=int((sd == 0).sum()),
            zero_agb_positive_sd=int(((agb == 0) & (sd > 0)).sum()),
            positive_agb_zero_sd=int(atzero.size),
            positive_agb_at_zero_sd_min_Mg_ha=float(atzero.min()),
            positive_agb_at_zero_sd_max_Mg_ha=float(atzero.max()),
            positive_agb_sd_min_Mg_ha=float(quantiles[0]),
            positive_agb_sd_q25_Mg_ha=float(quantiles[1]),
            positive_agb_sd_median_Mg_ha=float(quantiles[2]),
            positive_agb_sd_q75_Mg_ha=float(quantiles[3]),
            positive_agb_sd_max_Mg_ha=float(quantiles[4])))
    write_csv(ROOT / 'data/native_sd_reproduction_F11.csv', sd_rows)
    scale_rows, contrast_rows, certificates, thresholds, curve_rows = [], [], [], [], []
    for group in GROUPS:
        cs = {y: topology[f'{group}_intersections_{y}'] for y in (2015, 2023)}
        ns = {y: topology[f'total_intersections_{y}'] for y in (2015, 2023)}
        fs = {y: support[f"{'forest_plus_savanna' if group == 'formations_plus_savanna' else group}_{y}"] for y in (2015, 2023)}
        for y in (2015, 2023):
            fs[y] = canonical_fractions(fs[y], cs[y], ns[y])
        for side in SCALES:
            b0 = topology_bounds(q[2015], cs[2015], ns[2015], side)
            b1 = topology_bounds(q[2023], cs[2023], ns[2023], side)
            lower, upper = b1[0] - b0[1], b1[1] - b0[0]
            scale_rows.append(dict(group=group, block_side_native_cells=side,
                                   blocks=(256 // side) ** 2,
                                   lower_2015_Mg=b0[0], upper_2015_Mg=b0[1],
                                   lower_2023_Mg=b1[0], upper_2023_Mg=b1[1],
                                   difference_lower_Mg=lower, difference_upper_Mg=upper,
                                   width_Mg=upper - lower,
                                   sign_identified=lower > 0 or upper < 0))
        for ratio in CONTRASTS:
            lower, upper = contrast_interval(q[2015], q[2023], fs[2015], fs[2023], ratio)
            contrast_rows.append(dict(group=group, max_density_ratio=ratio,
                                      difference_lower_Mg=lower, difference_upper_Mg=upper,
                                      width_Mg=upper-lower, sign_identified=lower > 0 or upper < 0,
                                      empirically_validated_ratio=False))
        for ratio in np.geomspace(1., 10., 121):
            lower, upper = contrast_interval(q[2015], q[2023], fs[2015], fs[2023], float(ratio))
            curve_rows.append(dict(group=group, max_density_ratio=float(ratio),
                                   difference_lower_Mg=lower, difference_upper_Mg=upper))
        for direction in ('minimum', 'maximum'):
            certificates.append(dict(group=group, **witness(q[2015], q[2023], cs[2015], cs[2023],
                                                            ns[2015], ns[2023], direction)))
        lo1, hi1 = contrast_interval(q[2015], q[2023], fs[2015], fs[2023], 1.)
        loinf, hiinf = contrast_interval(q[2015], q[2023], fs[2015], fs[2023], math.inf)
        axis = 0 if lo1 > 0 else (1 if hi1 < 0 else None)
        root = None
        if axis is not None:
            def fun(log_ratio):
                return contrast_interval(q[2015], q[2023], fs[2015], fs[2023],
                                         math.exp(log_ratio))[axis]
            # Search in log space; the unrestricted interval straddles zero here.
            upper_log = 1.
            while fun(0) * fun(upper_log) > 0 and upper_log < 32:
                upper_log *= 2
            if fun(0) * fun(upper_log) <= 0:
                root = math.exp(brentq(fun, 0, upper_log, xtol=1e-13))
        thresholds.append(dict(group=group, homogeneous_difference_Mg=lo1,
                               positive_sign_boundary_ratio=root if axis == 0 else None,
                               negative_sign_boundary_ratio=root if axis == 1 else None,
                               ratio_is_assumed_not_measured=True,
                               primary_unrestricted_lower_Mg=loinf,
                               primary_unrestricted_upper_Mg=hiinf))
    cancellation_rows = [dict(block_side_native_cells=s, blocks=(256 // s) ** 2,
                              **cancellation(q[2015], q[2023], s)) for s in SCALES]
    out = ROOT / 'data'
    write_csv(out / 'resolution_frontier_F11.csv', scale_rows)
    write_csv(out / 'density_contrast_sensitivity_F11.csv', contrast_rows)
    write_csv(out / 'density_contrast_curve_F11.csv', curve_rows)
    write_csv(out / 'cancellation_by_scale_F11.csv', cancellation_rows)
    write_csv(out / 'extremal_witness_certificates_F11.csv', certificates)
    write_csv(out / 'density_contrast_sign_boundaries_F11.csv', thresholds)
    from scipy import __version__ as scipy_version
    summary = dict(analysis='Exploratory fixed-support point-map identification',
                   years=[2015, 2023], footprint_cells=65536, footprint_area_ha=float(area.sum()),
                   full_cell_mass_Mg={str(y):float(q[y].sum()) for y in q},
                   source_rows=native_rows,
                   numpy_version=np.__version__, scipy_version=scipy_version,
                   validated_change=False, national_inference=False,
                   all_eight_national_holds_retained=True,
                   primary_model_has_no_finite_density_contrast_cap=True,
                   ratio_sensitivity_is_not_calibration=True,
                   no_error_covariance_assumed_or_estimated=True,
                   raw_arrays_redistributed=False,
                   input_sha256={str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in [BASE/'data/brazil/BRA_F05_support_fractions.npz',
                                           BASE/'data/allocation/overlap_certificates_F07.npz']})
    (ROOT/'metadata/analysis_F11.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('Sign boundaries:', thresholds)
    print('Native cancellation:', cancellation_rows[0])


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cache', type=Path, default=ROOT/'.cache/native')
    p.add_argument('--offline', action='store_true')
    args = p.parse_args()
    run(args.cache, args.offline)
