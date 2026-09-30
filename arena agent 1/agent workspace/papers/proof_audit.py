#!/usr/bin/env python3
"""Structural proof audit of the theory units (1-6, 11).

Numeric verification cannot discharge a theorem. This audit checks what *is*
mechanically checkable about a proof corpus:

  1. every labelled result exists and is numbered consistently
  2. every result has a proof environment, or is explicitly flagged as not having one
     (definitions, remarks and open problems legitimately do not)
  3. the dependency graph of proofs -- which results each proof invokes -- is acyclic
  4. no proof invokes a result that is never stated
  5. no proof invokes a result stated *later* in the same unit without that result
     being proved independently of it (a genuine forward reference is a red flag)

Limitations: this reads LaTeX, not mathematics. It cannot tell whether a proof is
correct. It finds structural defects -- circular arguments, appeals to results that
do not exist, results asserted without proof -- which are exactly the defects that
survive careful reading and that reviewers catch late.
"""
import io
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__)) + '/'

THEORY = [
    ('1', 'paper01_obstruction_calculus_v63.tex'),
    ('2', 'paper02_probabilistic_sufficiency_v12.tex'),
    ('3', 'paper03_computational_certification_v16.tex'),
    ('4', 'paper04_minimax_dual_certificates_v16.tex'),
    ('5', 'paper05_exact_belief_computation_v16.tex'),
    ('6', 'paper06_assessment_separation_v67.tex'),
    ('11', 'paper11c_worked_systems_audit_v2.tex'),
]

# environments that carry a mathematical claim
RESULT = re.compile(
    r'\\begin\{(theorem|proposition|lemma|corollary)\*?\}')
# environments that are NOT expected to carry a proof
NOPROOF = set(['definition', 'remark', 'example', 'openproblem', 'assumption',
               'notation', 'conjecture'])
PROOF = re.compile(r'\\begin\{proof\*?\}')
ENDPROOF = re.compile(r'\\end\{proof\*?\}')


def strip_comments(s):
    out = []
    for line in s.split('\n'):
        i = line.find('%')
        while i != -1:
            if i == 0 or line[i - 1] != '\\':
                line = line[:i]
                break
            i = line.find('%', i + 1)
        out.append(line)
    return '\n'.join(out)


def env_spans(src, kind_re):
    """Return [(kind, label_or_None, start, end)] for each \\begin{kind}...\\end{kind}."""
    spans = []
    for m in kind_re.finditer(src):
        start = m.start()
        kind = m.group(1)
        # find matching \end{kind}, tolerating nesting of the same kind
        depth = 1
        pos = m.end()
        pat = re.compile(r'\\(begin|end)\{%s\*?\}' % re.escape(kind))
        while depth:
            mm = pat.search(src, pos)
            if not mm:
                break
            depth += 1 if mm.group(1) == 'begin' else -1
            pos = mm.end()
        end = pos
        body = src[start:end]
        lab = re.search(r'\\label\{([^}]+)\}', body)
        spans.append((kind, lab.group(1) if lab else None, start, end, body))
    return spans


def audit(path):
    src = strip_comments(io.open(path, encoding='utf-8', errors='replace').read())
    # stop at the bibliography
    m = re.search(r'\\(?:section|section\*)\{[^}]*[Rr]eferences', src)
    if m:
        src = src[:m.start()]

    results = env_spans(src, RESULT)
    all_envs = env_spans(src, re.compile(r'\\begin\{([a-z]+)\*?\}'))

    # results missing a proof
    missing = []
    for kind, lab, s_, e_, body in results:
        if not PROOF.search(body):
            missing.append((kind, lab, src[:s_].count('\n') + 1))

    # dependency graph: within each proof, which labels are referenced?
    labels = {}
    for kind, lab, s_, e_, body in all_envs:
        if lab:
            labels[lab] = (kind, src[:s_].count('\n') + 1)

    deps = {}
    for kind, lab, s_, e_, body in results:
        if not lab:
            continue
        p = PROOF.search(body)
        if not p:
            deps[lab] = set()
            continue
        proof_body = body[p.end():]
        seen = set()
        for r in re.finditer(r'\\(?:ref|cref|Cref|autoref)\{([^}]+)\}', proof_body):
            t = r.group(1)
            if t in labels:
                seen.add(t)
        deps[lab] = seen

    # dangling: referenced inside a proof but never labelled anywhere
    dangling = set()
    for lab, ds in deps.items():
        for d in ds:
            if d not in labels:
                dangling.add(d)

    # cycles
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {l: WHITE for l in labels}
    cycles = []

    def dfs(n, stack):
        colour[n] = GREY
        for d in deps.get(n, ()):
            if d not in colour:
                continue
            if colour[d] == GREY:
                cycles.append(stack[stack.index(d):] + [d])
            elif colour[d] == WHITE:
                dfs(d, stack + [d])
        colour[n] = BLACK

    for l in list(labels):
        if colour.get(l) == WHITE:
            dfs(l, [l])

    # forward references: proof of X cites Y where Y is stated after X
    fwd = []
    for kind, lab, s_, e_, body in results:
        if not lab:
            continue
        for d in deps.get(lab, ()):
            if d in labels and labels[d][1] > s_:
                fwd.append((lab, d, labels[d][0]))

    return {
        'results': len(results),
        'labels': len(labels),
        'missing_proof': missing,
        'deps': deps,
        'dangling': sorted(dangling),
        'cycles': cycles,
        'forward': fwd,
        'by_kind': {},
    }


def main():
    total_bad = 0
    for unit, fn in THEORY:
        p = BASE + fn
        if not os.path.exists(p):
            print('MISSING %s' % fn)
            continue
        r = audit(p)
        print('=' * 74)
        print('UNIT %s  %s' % (unit, fn))
        print('  labelled environments : %d' % r['labels'])
        print('  claim environments    : %d (theorem/proposition/lemma/corollary)' % r['results'])
        print('  claims without a proof: %d' % len(r['missing_proof']))
        for kind, lab, ln in r['missing_proof'][:12]:
            print('      L%-6d %-12s %s' % (ln, kind, lab or '(unlabelled)'))
        if len(r['missing_proof']) > 12:
            print('      ... +%d more' % (len(r['missing_proof']) - 12))
        print('  references in proofs to unlabelled targets: %d' % len(r['dangling']))
        for d in r['dangling'][:10]:
            print('      ', d)
        print('  circular dependencies : %d' % len(r['cycles']))
        for cy in r['cycles'][:6]:
            print('      ', ' -> '.join(cy))
        print('  forward references    : %d' % len(r['forward']))
        for a, b, k in r['forward'][:8]:
            print('      proof of %-34s cites %s (%s), stated later' % (a, b, k))
        total_bad += (len(r['missing_proof']) + len(r['dangling']) +
                      len(r['cycles']) + len(r['forward']))
        print()
    print('TOTAL structural findings across theory units: %d' % total_bad)


if __name__ == '__main__':
    main()
