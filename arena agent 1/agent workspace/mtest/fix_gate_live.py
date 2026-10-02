import io
import re

P = '/home/user/p5/phase0_scan.py'
s = io.open(P, encoding='utf-8').read()

# ---------------------------------------------------------------- helpers
ANCHOR = "def report_gate(hits, what):"
assert ANCHOR in s

HELPERS = r'''# --------------------------------------------------------------------------
# live-head classification
#
# Merging always writes a NEW version, so an old version is never re-merged
# and nobody will ever repair it. Counting it as a gate failure is how a gate
# trains people to ignore it: the same handful of dead files fail on every run,
# forever. Superseded files are reported as INFORMATIONAL and never counted.
VERSIONED = re.compile(r'^(paper\d+[a-z]*_[a-z_]+)_v(\d+)\.tex$')


def live_heads(files):
    """-> set of the newest version of each paper family.

    Files that do not match the versioned pattern (supplementary .tex, and
    any other unversioned artifact) are treated as live, since nothing
    supersedes them.
    """
    best = {}
    for f in files:
        m = VERSIONED.match(f)
        if not m:
            continue
        fam, ver = m.group(1), int(m.group(2))
        if fam not in best or ver > best[fam][0]:
            best[fam] = (ver, f)
    return set(v[1] for v in best.values())


def classify(files):
    """-> [(filename, 'live' | 'superseded'), ...]"""
    live = live_heads(files)
    out = []
    for f in files:
        m = VERSIONED.match(f)
        out.append((f, 'superseded' if (m and f not in live) else 'live'))
    return out


'''

s = s.replace(ANCHOR, HELPERS + ANCHOR, 1)

# ---------------------------------------------------------------- --gate
old_gate = '''    if gate_only:
        # merge output gate: H-L only, non-zero exit if anything fires
        bad = 0
        for f in files:
            hits = merge_gate(PAPERS + f)
            if not hits:
                if not quiet:
                    print("  %-46s structural gate OK" % f)
                continue
            print("  %-46s STRUCTURAL GATE FAILED — %d" % (f, len(hits)))
            for kind, hit, why, ln in hits:
                print("      [%-26s] %-14s %-6s %s"
                      % (kind, str(hit)[:14], 'L%s' % ln if ln else '-', why))
            bad += len(hits)
        print("\\nGATE: %d structural failure(s)" % bad)
        sys.exit(1 if bad else 0)
'''

new_gate = '''    if gate_only:
        # merge output gate: H-L only.
        #
        # Two things this used to get wrong, both of which made the number
        # untrustworthy:
        #   1. it counted FINDINGS but printed them as "failure(s)", so a run
        #      reporting "32" and a count of "12 failing files" looked like a
        #      contradiction when they were different units. Both are printed.
        #   2. it failed on superseded versions, which nobody will ever fix.
        #      Only LIVE HEADS count toward the exit status now.
        rows = []
        for f, status in classify(files):
            hits = merge_gate(PAPERS + f)
            if hits:
                rows.append((f, status, hits))

        for f, status, hits in rows:
            tag = ('STRUCTURAL GATE FAILED' if status == 'live'
                   else 'informational (superseded, not counted)')
            print("  %-46s %s — %d finding(s)" % (f, tag, len(hits)))
            for kind, hit, why, ln in hits:
                print("      [%-26s] %-14s %-6s %s"
                      % (kind, str(hit)[:14], 'L%s' % ln if ln else '-', why))

        live_rows = [r for r in rows if r[1] == 'live']
        dead_rows = [r for r in rows if r[1] == 'superseded']
        live_files = len(live_rows)
        live_findings = sum(len(r[2]) for r in live_rows)
        dead_files = len(dead_rows)
        dead_findings = sum(len(r[2]) for r in dead_rows)

        print()
        print("LIVE HEADS failing  : %d file(s), %d finding(s)   <-- exit status"
              % (live_files, live_findings))
        print("superseded, ignored : %d file(s), %d finding(s)"
              % (dead_files, dead_findings))
        print("scanned             : %d file(s)" % len(files))
        sys.exit(1 if live_findings else 0)
'''

assert old_gate in s, '--gate block not found'
s = s.replace(old_gate, new_gate, 1)

io.open(P, 'w', encoding='utf-8').write(s)
print('gate: live-head-only failure, files AND findings both reported')
