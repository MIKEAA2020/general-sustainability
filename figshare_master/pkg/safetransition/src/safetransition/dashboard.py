"""Static dashboard rendering (single-file HTML, inline SVG/CSS).

The dashboard is fully self-contained: no external stylesheets,
scripts, fonts, or images. Floats appear only in SVG coordinates; all
displayed quantities are rendered from exact rationals via
``safetransition.rational.fmt``.
"""
from fractions import Fraction as Q

import hashlib
import json as _json
import os

from . import __version__
from .rational import fmt, fmtf


def _polyline(points, x_range, y_range, box, color, dash="", width=2.2):
    (x0, x1), (y0, y1) = x_range, y_range
    (bx, by, bw, bh) = box
    px = lambda t: bx + (float(t) - x0) / (x1 - x0) * bw
    py = lambda v: by + bh - (float(v) - y0) / (y1 - y0) * bh
    pts = " ".join(f"{px(t):.1f},{py(v):.1f}" for t, v in points)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polyline points="{pts}" fill="none" stroke="{color}" '
            f'stroke-width="{width}"{d} stroke-linejoin="round" '
            f'stroke-linecap="round"/>')


def _circles(points, x_range, y_range, box, color, r=3.2):
    (x0, x1), (y0, y1) = x_range, y_range
    (bx, by, bw, bh) = box
    px = lambda t: bx + (float(t) - x0) / (x1 - x0) * bw
    py = lambda v: by + bh - (float(v) - y0) / (y1 - y0) * bh
    return "".join(f'<circle cx="{px(t):.1f}" cy="{py(v):.1f}" r="{r}" fill="{color}"/>'
                   for t, v in points)


def _panel_a(data, W=(500, 270)):
    ts = data["t"]
    xs = (Q(0), Q(1))
    ys = (Q(-2), Q(3))
    box = (52, 14, W[0] - 70, W[1] - 52)
    g = [f'<svg width="{W[0]}" height="{W[1]}" viewBox="0 0 {W[0]} {W[1]}" role="img" '
         f'aria-label="Composite index versus ecological floor">']
    # floor band and zero line
    py0 = box[1] + box[3] - (0 - float(ys[0])) / (float(ys[1]) - float(ys[0])) * box[3]
    g.append(f'<rect x="{box[0]}" y="{py0}" width="{box[2]}" height="{box[1] + box[3] - py0}" '
             f'fill="#f6d9d4" opacity="0.55"/>')
    g.append(f'<line x1="{box[0]}" y1="{py0:.1f}" x2="{box[0] + box[2]}" y2="{py0:.1f}" '
             f'stroke="#555" stroke-width="1" stroke-dasharray="5,4"/>')
    g.append(f'<text x="{box[0] + 4}" y="{py0 - 4:.1f}" font-size="10" fill="#c0392b">floor s = 0</text>')
    s1a = list(zip(ts, data["s1_adverse"]))
    s1b = list(zip(ts, data["s1_benign"]))
    idx = list(zip(ts, data["index_w11"]))
    g.append(_polyline(s1b, xs, ys, box, "#c0392b", dash="6,4", width=1.6))
    g.append(_polyline(s1a, xs, ys, box, "#c0392b"))
    g.append(_circles(s1a, xs, ys, box, "#c0392b"))
    g.append(_polyline(idx, xs, ys, box, "#2e8b57"))
    g.append(_circles(idx, xs, ys, box, "#2e8b57"))
    g.append(f'<text x="{box[0] + box[2] - 150}" y="{box[1] + 16}" font-size="10.5" fill="#2e8b57">'
             f'composite index w&#183;s (w = (1,1)): min {fmt(min(data["index_w11"]))} &gt; 0</text>')
    g.append(f'<text x="{box[0] + box[2] - 190}" y="{box[1] + 31}" font-size="10.5" fill="#c0392b">'
             f'ecological margin s1 (heatwave): min {fmt(min(data["s1_adverse"]))} &lt; 0</text>')
    # axes
    g.append(f'<line x1="{box[0]}" y1="{box[1] + box[3]}" x2="{box[0] + box[2]}" '
             f'y2="{box[1] + box[3]}" stroke="#333" stroke-width="1"/>')
    for frac_t, lab in ((0, "0"), (0.5, "1/2"), (1, "1")):
        x = box[0] + frac_t * box[2]
        g.append(f'<line x1="{x:.1f}" y1="{box[1] + box[3]}" x2="{x:.1f}" '
                 f'y2="{box[1] + box[3] + 4}" stroke="#333"/>')
        g.append(f'<text x="{x:.1f}" y="{box[1] + box[3] + 15}" font-size="10" '
                 f'text-anchor="middle">{lab}</text>')
    g.append(f'<text x="{box[0] + box[2] / 2}" y="{W[1] - 2}" font-size="10.5" '
             f'text-anchor="middle" fill="#333">time within the review period (yr)</text>')
    g.append("</svg>")
    return "".join(g)


def _panel_b(data, W=(500, 270)):
    ts = data["t"]
    xs = (Q(0), Q(1))
    ys = (Q(-1), Q(14))
    box = (52, 14, W[0] - 70, W[1] - 52)
    g = [f'<svg width="{W[0]}" height="{W[1]}" viewBox="0 0 {W[0]} {W[1]}" role="img" '
         f'aria-label="Plan schedules">']
    y_of = lambda v: box[1] + box[3] - (float(v) - float(ys[0])) / (float(ys[1]) - float(ys[0])) * box[3]
    # strike band
    bx = box[0] + 0.48 * box[2]
    bw = 0.04 * box[2]
    g.append(f'<rect x="{bx:.1f}" y="{box[1]}" width="{bw:.1f}" height="{box[3]}" '
             f'fill="#e08a1e" opacity="0.25"/>')
    g.append(f'<text x="{bx + bw / 2:.1f}" y="{box[1] + 11}" font-size="9.5" fill="#a06010" '
             f'text-anchor="middle">heatwave strike</text>')
    fast = list(zip(ts, data["H_fast"]))
    sy = [(ts[0], data["H_sy"]), (ts[2], data["H_sy"])]
    staged = [(ts[0], data["H_staged"][0]), (ts[1], data["H_staged"][1]), (ts[2], data["H_staged"][1])]
    fund = list(zip(ts, data["fund"]))
    g.append(_polyline(sy, xs, ys, box, "#555", dash="8,3,2,3", width=1.6))
    g.append(_polyline(staged, xs, ys, box, "#2e8b57"))
    g.append(_circles(staged, xs, ys, box, "#2e8b57", r=2.8))
    g.append(_polyline(fast, xs, ys, box, "#1f6fb2"))
    g.append(_circles(fast, xs, ys, box, "#1f6fb2"))
    fp = [(t, v * 9.5) for t, v in fund]  # fund on the same scale, dotted, right axis
    g.append(_polyline(fp, xs, ys, box, "#e08a1e", dash="2,3", width=1.8))
    g.append(f'<text x="{box[0] + 6}" y="{y_of(data["H_fast"][0]) - 6:.1f}" font-size="10" fill="#1f6fb2">'
             f'FAST: pulse {fmt(data["H_fast"][0])} + closed season</text>')
    g.append(f'<text x="{box[0] + 6}" y="{y_of(data["H_sy"]) - 6:.1f}" font-size="10" fill="#555">'
             f'SLOW / NO-SWITCH: sustained yield sigma(16/5) = {fmt(data["H_sy"])}</text>')
    g.append(f'<text x="{box[0] + box[2] - 150}" y="{y_of(data["H_staged"][1]) - 6:.1f}" font-size="10" '
             f'fill="#2e8b57">STAGED: below yield, rebuild to 69/20</text>')
    g.append(f'<text x="{box[0] + 6}" y="{y_of(fp[0][1]) - 6:.1f}" font-size="9.5" fill="#a06010">'
             f'fund x(t) (STAGED, scaled)</text>')
    g.append(f'<line x1="{box[0]}" y1="{box[1] + box[3]}" x2="{box[0] + box[2]}" '
             f'y2="{box[1] + box[3]}" stroke="#333" stroke-width="1"/>')
    for frac_t, lab in ((0, "0"), (0.5, "1/2"), (1, "1")):
        x = box[0] + frac_t * box[2]
        g.append(f'<line x1="{x:.1f}" y1="{box[1] + box[3]}" x2="{x:.1f}" '
                 f'y2="{box[1] + box[3] + 4}" stroke="#333"/>')
        g.append(f'<text x="{x:.1f}" y="{box[1] + box[3] + 15}" font-size="10" '
                 f'text-anchor="middle">{lab}</text>')
    g.append(f'<text x="{box[0] + box[2] / 2}" y="{W[1] - 2}" font-size="10.5" '
             f'text-anchor="middle" fill="#333">time within the review period (yr); '
             f'quota H*(t) (kt/yr)</text>')
    g.append("</svg>")
    return "".join(g)


_CSS = """
body{font-family:Georgia,'Times New Roman',serif;margin:0;background:#f4f3ef;color:#1c1c1c}
.wrap{max-width:1060px;margin:0 auto;padding:26px 30px 48px}
header h1{font-size:25px;margin:0 0 2px;letter-spacing:.2px}
header .sub{color:#555;font-size:13.5px;margin-bottom:14px}
.badges span{display:inline-block;background:#1c1c1c;color:#f4f3ef;border-radius:3px;
 padding:3px 9px;font-size:11px;margin-right:6px;letter-spacing:.4px}
.badges .pass{background:#2e8b57}.badges .warn{background:#c0392b}
.grid{display:flex;flex-wrap:wrap;gap:12px;margin:16px 0}
.card{background:#fff;border:1px solid #ddd8cc;border-radius:6px;padding:13px 16px;flex:1 1 220px}
.card h3{margin:0 0 6px;font-size:12px;letter-spacing:.8px;text-transform:uppercase;color:#776;
 font-family:Helvetica,Arial,sans-serif}
.card .big{font-size:21px;margin:2px 0}
.card .note{font-size:12px;color:#555;line-height:1.45}
table{border-collapse:collapse;width:100%;background:#fff;font-size:13px;margin:10px 0;
 border:1px solid #ddd8cc}
th,td{border-bottom:1px solid #eee7d8;padding:7px 10px;text-align:left}
th{background:#efece3;font-family:Helvetica,Arial,sans-serif;font-size:11.5px;
 letter-spacing:.4px;text-transform:uppercase;color:#554}
.pass{color:#2e8b57;font-weight:bold}.fail{color:#c0392b;font-weight:bold}
.alarm{background:#c0392b;color:#fff;border-radius:6px;padding:12px 16px;margin:14px 0;
 font-size:14px}
.alarm b{letter-spacing:.5px}
.footer{margin-top:26px;font-size:12px;color:#666;border-top:1px solid #ddd8cc;
 padding-top:12px;line-height:1.55}
code{background:#efece3;padding:1px 5px;border-radius:3px;font-size:12px}
.panel{background:#fff;border:1px solid #ddd8cc;border-radius:6px;padding:10px 12px;margin:10px 0}
.panel h3{font-size:12px;letter-spacing:.8px;text-transform:uppercase;color:#776;margin:2px 0 6px;
 font-family:Helvetica,Arial,sans-serif}
"""


def default_provenance(certificates_json=None, datum_id=None):
    """Verification-provenance record for the audit-delivery dashboard.

    Returns a deterministic dictionary embedding: the library version, the
    independent checker's version and invocation, the datum identifier, and
    -- for each ``(name, certificate_dict)`` in ``certificates_json`` -- the
    exact JSON serialization, its SHA-256 hash, and the re-run command for
    the independent checker. Rendering embeds this record verbatim, so the
    dashboard is an audit-delivery mechanism tied to the certificate
    schema, and regenerating it from the same inputs is byte-identical.
    """
    if datum_id is None:
        from .datum import describe_state, witness_state
        datum_id = "witness datum: " + describe_state(witness_state(1, 2, 2))
    checker_path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))),
        "check_safe_transition_cert.py")
    checker_version = "unknown"
    if os.path.exists(checker_path):
        import re
        m = re.search(r'CHECKER_VERSION\s*=\s*"([^"]+)"',
                      open(checker_path, encoding="utf-8").read())
        if m:
            checker_version = m.group(1)
    items = []
    for name, cert in (certificates_json or []):
        ser = _json.dumps(cert, sort_keys=True, separators=(",", ":"))
        digest = hashlib.sha256(ser.encode("utf-8")).hexdigest()
        items.append({"name": name, "sha256": digest, "json": ser})
    return {
        "library_version": __version__,
        "checker_version": checker_version,
        "checker_command": "python3 check_safe_transition_cert.py cert.json",
        "datum_id": datum_id,
        "certificates": items,
        "arithmetic": "exact rational (fractions.Fraction); floats only in SVG geometry",
    }


def _provenance_html(prov):
    if not prov:
        return ""
    rows = [f"<tr><td>library version</td><td>{prov['library_version']}</td></tr>",
            f"<tr><td>independent checker</td><td>v{prov['checker_version']}; "
            f"re-run: <code>{prov['checker_command']}</code></td></tr>",
            f"<tr><td>datum identifier</td><td>{prov['datum_id']}</td></tr>",
            f"<tr><td>arithmetic</td><td>{prov['arithmetic']}</td></tr>"]
    for it in prov["certificates"]:
        rows.append(f"<tr><td>certificate: {it['name']}</td>"
                    f"<td>sha256 <code>{it['sha256']}</code></td></tr>")
    pre = "".join(
        '<details><summary style="cursor:pointer">' + it["name"]
        + ' (exact input serialization)</summary><pre style="white-space:pre-wrap;'
          'font-size:10.5px">' + it["json"] + '</pre></details>'
        for it in prov["certificates"])
    return ('<h3 style="font-size:13px;font-family:Helvetica,Arial,sans-serif;'
            'letter-spacing:.6px;text-transform:uppercase;color:#776">'
            'Verification provenance</h3>'
            '<table><tr><th>Field</th><th>Value</th></tr>' + "".join(rows)
            + '</table>' + pre)


def render(readings, benchmark=None, certificates=None, data=None, title=None,
           provenance=None):
    """Render the dashboard HTML string.

    ``readings`` is a :class:`safetransition.indicators.Readings`;
    ``benchmark`` an optional :class:`safetransition.benchmark.BenchmarkResult`;
    ``certificates`` an optional list of ``(name, verdict_str, holds_bool)``;
    ``data`` the verified schedule values (default: the benchmark module's);
    ``provenance`` an optional provenance record (see
    :func:`default_provenance`) embedded as a verification-provenance table.
    Rendering is deterministic: the output is a pure function of the inputs,
    with no timestamps, so re-rendering from the same inputs is
    byte-identical and hash-checkable.
    """
    if data is None:
        from .benchmark import schedule_data
        data = schedule_data()
    if title is None:
        title = "SafeTransition — transition-safety dashboard"
    prov = provenance
    badge = (f'<div class="badges"><span>EXACT RATIONAL ARITHMETIC</span>'
             + (f'<span class="pass">BENCHMARK {benchmark.passed}/{benchmark.total}</span>'
                if benchmark and benchmark.all_pass else
                (f'<span class="warn">BENCHMARK {benchmark.passed}/{benchmark.total}</span>'
                 if benchmark else ""))
             + ('<span class="warn">INDEX-BLINDNESS ALARM</span>' if readings.blind_alarm else "")
             + "</div>")
    alarm = ('<div class="alarm"><b>ALARM — composite blindness.</b> ' + readings.notes[0]
             + "</div>" if readings.blind_alarm else "")
    rows = []
    for plan, mins in readings.tube_minima.items():
        rows.append(
            f"<tr><td><b>{plan}</b></td>"
            f"<td>{fmt(mins['s1'])}</td><td>{fmt(mins['s2'])}</td></tr>")
    lic_rows = "".join(
        f'<tr><td>{name}</td><td>{("licensed" if v else "not licensed")}</td>'
        f'<td class="{"pass" if v else "fail"}">{"&#10003;" if v else "&#10007;"}</td></tr>'
        for name, v in readings.licensed.items())
    cert_rows = ""
    if certificates:
        cert_rows = "".join(
            f'<tr><td>{n}</td><td>{v}</td>'
            f'<td class="{"pass" if h else "fail"}">{"&#10003; verified" if h else "&#10007;"}</td></tr>'
            for n, v, h in certificates)
    x, s1v, s2v = readings.state[1], readings.state[2], readings.state[3]
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{_CSS}</style></head><body><div class="wrap">
<header><h1>SafeTransition</h1>
<div class="sub">Exact transition-safety assessment &mdash; witness datum, resource-transition benchmark (Schaefer realization)</div>
{badge}</header>
<div class="grid">
<div class="card"><h3>Witness state</h3><div class="big">({fmt(x)}, {fmt(s1v)}, {fmt(s2v)})</div>
<div class="note">fund x; floors s1 (ecological), s2 (income). Gain e = (1/4, 1/4); rescue cost c = 1.</div></div>
<div class="card"><h3>Licensing thresholds</h3>
<div class="big">&rho;<sub>1</sub> = {fmt(readings.rho1)} &nbsp;&middot;&nbsp; &rho;<sub>2</sub> = {fmt(readings.rho2)}</div>
<div class="note">FAST licensed for w2/w1 &ge; &rho;<sub>1</sub>; SLOW for w2/w1 &le; &rho;<sub>2</sub>;
at r in [{fmt(readings.rho1)}, {fmt(readings.rho2)}] both. Witness-formula cross-check:
{"exact match" if readings.threshold_crosscheck_ok else "MISMATCH"}.</div></div>
<div class="card"><h3>Rescue threshold</h3><div class="big">&kappa;* = {fmt(readings.kappa_star)}</div>
<div class="note">Financing shortfall (1 &minus; x) on the non-typed-viable region at this state.</div></div>
<div class="card"><h3>Aggregate @ w = ({fmt(readings.weight[0])}, {fmt(readings.weight[1])})</h3>
<div class="big">min w&middot;s = {fmt(readings.index_min)}</div>
<div class="note">floor minimum along the same plan: {fmt(readings.floor_min)}</div></div>
</div>
{alarm}
<div class="panel"><h3>(a) What the index sees vs what the floor does</h3>{_panel_a(data)}</div>
<div class="panel"><h3>(b) The plan menu as management schedules</h3>{_panel_b(data)}</div>
<h3 style="font-size:13px;font-family:Helvetica,Arial,sans-serif;letter-spacing:.6px;
 text-transform:uppercase;color:#776">Tube minima by plan (characteristic disturbance)</h3>
<table><tr><th>Plan</th><th>min s1</th><th>min s2</th></tr>{''.join(rows)}</table>
<h3 style="font-size:13px;font-family:Helvetica,Arial,sans-serif;letter-spacing:.6px;
 text-transform:uppercase;color:#776">Licensing at the current weight</h3>
<table><tr><th>Plan / reading</th><th>Verdict</th><th>Status</th></tr>{lic_rows}</table>
{('<h3 style="font-size:13px;font-family:Helvetica,Arial,sans-serif;letter-spacing:.6px;'
  'text-transform:uppercase;color:#776">Certificates</h3>'
  '<table><tr><th>Certificate</th><th>Detail</th><th>Status</th></tr>' + cert_rows + '</table>')
  if cert_rows else ""}
{_provenance_html(prov)}
<div class="footer"><b>SafeTransition {__version__}</b> &mdash; exact rational certification of transition
safety. Mathematical basis: the typed assessment-operator framework and the obstruction-calculus
certificate family of the companion manuscripts (A. Abaee). Verified values: benchmark deposit
<a href="https://doi.org/10.6084/m9.figshare.33764023">10.6084/m9.figshare.33764023</a>.
All quantities on this page are computed in exact rational arithmetic; floats appear only in
SVG geometry.</div>
</div></body></html>"""
    return html


def write(readings, path, **kw):
    html = render(readings, **kw)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return path
