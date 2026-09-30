"""Compile a paper with figure stubs and report, then optionally verify by PDF extraction.

Usage:  python3 build.py <paper>.tex [dir] [--probe "string"] [--probe "other"]

Figure stubs: every \\includegraphics target is created as a 1x1 PNG. For compile
purposes only, `.pdf` graphics are rewritten to `.png` in the TEST COPY -- the shipped
file in /home/user/papers is never touched.

This harness exists because the corpus has no figure files in the workspace; tectonic
raises "Unable to load picture or PDF file" and produces no PDF, which masks every other
error in the log.
"""
import io, os, re, subprocess, sys

PNG = bytes.fromhex(
    '89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489'
    '0000000a49444154789c63000100000500010d0a2db40000000049454e44ae426082')
TECTONIC = '/home/user/tools/tectonic'


def build(tex, outdir='/tmp/build', probes=None):
    os.makedirs(outdir, exist_ok=True)
    stem = os.path.basename(tex)[:-4]
    dst = os.path.join(outdir, stem + '.tex')
    s = io.open(tex, encoding='utf-8', errors='replace').read()
    s = re.sub(r'(\\includegraphics(?:\[[^\]]*\])?\{[^}]*?)\.pdf\}', r'\1.png}', s)
    io.open(dst, 'w', encoding='utf-8').write(s)
    for f in set(re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', s)):
        d = os.path.dirname(f)
        if d:
            os.makedirs(os.path.join(outdir, d), exist_ok=True)
        io.open(os.path.join(outdir, f), 'wb').write(PNG)
    try:
        os.chmod(TECTONIC, 0o755)
    except OSError:
        pass
    subprocess.run([TECTONIC, '-X', 'compile', '--outdir', outdir, '--keep-logs',
                    dst], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1500)
    log = os.path.join(outdir, stem + '.log')
    lt = io.open(log, encoding='utf-8', errors='replace').read() if os.path.exists(log) else ''
    m = re.findall(r'\((\d+) pages', lt)
    pdf = os.path.join(outdir, stem + '.pdf')
    em = re.search(r'^!', lt, re.M)
    first_error = ''
    if em:
        seg = lt[em.start():em.start() + 600]
        cut = seg.find('\n\n')
        first_error = (seg[:cut] if cut > 0 else seg).strip()[:400]
    st = dict(pages=int(m[-1]) if m else None,
              err=len(re.findall(r'^!', lt, re.M)),
              undef=len(re.findall(r'undefined', lt)),
              size=os.path.getsize(pdf) if os.path.exists(pdf) else 0,
              first_error=first_error)
    print("%-50s pages=%-5s err=%-4s undef=%-4s %d B"
          % (stem, st['pages'] or 'NO-PDF', st['err'], st['undef'], st['size']))
    if st['first_error']:
        print("  " + st['first_error'].replace('\n', '\n  '))
    if probes and os.path.exists(pdf):
        from pypdf import PdfReader
        t = re.sub(r'\s+', ' ', "\n".join((p.extract_text() or '')
                                          for p in PdfReader(pdf).pages))
        for p in probes:
            ok = p in t
            print("   %-52s %s" % (p[:52], 'OK' if ok else 'MISSING'))
    return st


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    probes = [sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == '--probe']
    tex = args[0]
    d = args[1] if len(args) > 1 else '/tmp/build'
    st = build(tex, d, probes)
    sys.exit(0 if st['err'] == 0 and st['pages'] else 1)
