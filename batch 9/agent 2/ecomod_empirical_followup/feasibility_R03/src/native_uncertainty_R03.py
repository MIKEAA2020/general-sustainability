"""Descriptive SD/zero audit on the unchanged, SHA-pinned Brazilian window.
No stock changes, error correlations, confidence intervals or admissions are estimated.
"""
from pathlib import Path
import csv, hashlib, json, re
import numpy as np
import requests

ROOT = Path(__file__).resolve().parents[1]
CAP = 25_000_000
SHAPE = (256, 256)


def parse_ascii(text, shape=SHAPE):
    separator = '---------------------------------------------'
    if text.count(separator) != 1:
        raise ValueError('Missing/duplicate DAP separator')
    arrays, current, lines = {}, None, {}
    for line in text.split(separator, 1)[1].splitlines():
        line = line.strip()
        if not line:
            continue
        header = re.fullmatch(r'(agb|agb_sd)\[1\]\[(\d+)\]\[(\d+)\]', line)
        if header:
            current = header.group(1)
            if current in arrays or tuple(map(int, header.groups()[1:])) != shape:
                raise ValueError('Duplicate array or wrong declared shape')
            arrays[current], lines[current] = [], 0
            continue
        row = re.fullmatch(r'\[0\]\[(\d+)\],\s*(.*)', line)
        if current is None or row is None or int(row.group(1)) != lines[current]:
            raise ValueError('Unexpected/misordered DAP row')
        tokens = [s.strip() for s in row.group(2).split(',')]
        if len(tokens) != shape[1] or any(re.fullmatch(r'-?\d+', t) is None for t in tokens):
            raise ValueError('Invalid DAP numeric row')
        values = [int(t) for t in tokens]
        if any(v < -32768 or v > 32767 for v in values):
            raise ValueError('Int16 overflow')
        arrays[current].append(values)
        lines[current] += 1
    if set(arrays) != {'agb', 'agb_sd'} or any(lines[k] != shape[0] for k in arrays):
        raise ValueError('Incomplete DAP arrays')
    return {k: np.asarray(v, dtype=np.int32) for k, v in arrays.items()}


def acquire(row, cache):
    path = cache / row['cache_filename']
    if not path.exists():
        count = 0
        with requests.get(row['url'], stream=True, timeout=(20, 120)) as response:
            response.raise_for_status()
            with path.open('wb') as stream:
                for chunk in response.iter_content(262144):
                    count += len(chunk)
                    if count > min(CAP, row['bytes']):
                        raise ValueError('Frozen native transfer cap exceeded')
                    stream.write(chunk)
    data = path.read_bytes()
    if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
        raise ValueError('Pinned original native payload changed; do not decode')
    return parse_ascii(data.decode())


def summarize(arrays, year):
    agb, sd = arrays['agb'], arrays['agb_sd']
    valid_agb = (agb >= 0) & (agb <= 10000)
    valid_sd = (sd >= 0) & (sd <= 10000)
    joint = valid_agb & valid_sd
    positive = joint & (agb > 0)
    zero = joint & (agb == 0)
    pz = positive & (sd == 0)
    q = np.quantile(sd[positive], [0, .25, .5, .75, 1]).tolist() if positive.any() else [None] * 5
    return {'year': year, 'cells': int(agb.size), 'joint_valid': int(joint.sum()),
            'agb_fill': int((agb == -32768).sum()), 'sd_fill': int((sd == -32768).sum()),
            'zero_agb': int(zero.sum()), 'zero_sd': int((joint & (sd == 0)).sum()),
            'zero_agb_positive_sd': int((zero & (sd > 0)).sum()),
            'positive_agb_zero_sd': int(pz.sum()),
            'positive_agb_at_zero_sd_min_Mg_ha': int(agb[pz].min()) if pz.any() else None,
            'positive_agb_at_zero_sd_max_Mg_ha': int(agb[pz].max()) if pz.any() else None,
            'positive_agb_sd_min_Mg_ha': q[0], 'positive_agb_sd_q25_Mg_ha': q[1],
            'positive_agb_sd_median_Mg_ha': q[2], 'positive_agb_sd_q75_Mg_ha': q[3],
            'positive_agb_sd_max_Mg_ha': q[4]}


def run(cache):
    cache.mkdir(parents=True, exist_ok=True)
    registry = json.loads((ROOT / 'metadata/native_payload_registry_R03.json').read_text())
    arrays = {r['year']: acquire(r, cache) for r in registry}
    rows = [summarize(arrays[y], y) for y in [2015, 2023]]
    with (ROOT / 'data/native_sd_summary_R03.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    zero_states = []
    for z0 in [True, False]:
        for z1 in [True, False]:
            n = int((((arrays[2015]['agb'] == 0) == z0) & ((arrays[2023]['agb'] == 0) == z1)).sum())
            zero_states.append({'2015_stored_agb_zero': z0, '2023_stored_agb_zero': z1, 'cells': n})
    result = {'rows': rows, 'zero_estimate_endpoint_states': zero_states,
              'fixed_rows': [105890, 106145], 'fixed_columns': [146433, 146688],
              'original_payloads_full_SHA256_matched': True, 'maps_recalculated': False,
              'new_error_covariance_estimated': False, 'confidence_intervals': False,
              'zero_origin_verified': False, 'country_admissions_changed': False,
              'interpretation': 'Stored point-map/SD diagnostics, not physical forest changes or calibrated uncertainty'}
    (ROOT / 'metadata/native_sd_audit_R03.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache', type=Path, required=True)
    print(json.dumps(run(parser.parse_args().cache), indent=2))
