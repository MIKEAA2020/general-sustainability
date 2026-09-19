#!/usr/bin/env python3
"""Measure whether an article can be split, instead of guessing from its length.

Method. Every numbered statement (Definition/Proposition/Theorem/Corollary/Lemma/Remark) is a node,
attributed to the section its heading sits under. An edge A -> B exists when the text of B cites A's
label. A split along a section boundary is clean only if no edge crosses it in either direction *and*
the two halves still each carry their own results; that is equivalent to the section-level graph being
disconnected. So: count the mutually reachable section pairs, and check whether any proper subset of
result-bearing sections is closed under the edges.

Usage: python3 split_graph_v1.py <article.md> [...]
"""
import re
import sys
from collections import defaultdict

KIND = r'Definition|Proposition|Theorem|Corollary|Lemma|Remark'


def sections(md):
    """[(num, title, start, end)] for '## n. Title' headings."""
    out = []
    for m in re.finditer(r'^## (\d+)\. (.+)$', md, re.M):
        out.append([m.group(1), m.group(2).strip(), m.start(), None])
    for i in range(len(out) - 1):
        out[i][3] = out[i + 1][2]
    out[-1][3] = md.index('\n## References') if '\n## References' in md else len(md)
    return out


def graph(path):
    md = open(path, encoding='utf-8').read()
    secs = sections(md)
    lab = re.compile(r'\*\*(' + KIND + r')\s+(\d+)')
    nodes = []                                          # (kind, num, section_idx)
    for si, (num, title, a, b) in enumerate(secs):
        for m in lab.finditer(md[a:b]):
            nodes.append((m.group(1), int(m.group(2)), si))
    home = {n[:2]: n[2] for n in nodes}
    edges = defaultdict(set)
    for si, (num, title, a, b) in enumerate(secs):
        body = md[a:b]
        for m in re.finditer(r'\b(' + KIND + r')\s+(\d+)\b', body):
            k = (m.group(1), int(m.group(2)))
            if k in home and home[k] != si:
                edges[si].add(home[k])                  # si cites home[k]
    return md, secs, nodes, home, edges


def scc(adj, keys):
    """Tarjan, iterative."""
    index, low, onstk, stk = {}, {}, set(), []
    cnt = [0]
    out = []

    def strong(v0):
        work = [(v0, iter(sorted(adj.get(v0, ()))))]
        path = []
        while work:
            v, it = work[-1]
            if v not in index:
                index[v] = low[v] = cnt[0]
                cnt[0] += 1
                stk.append(v)
                onstk.add(v)
                path.append(v)
            advanced = False
            for w in it:
                if w not in adj or w not in index:
                    if w in index:
                        pass
                    work.append((w, iter(sorted(adj.get(w, ())))))
                    advanced = True
                    break
                if w in onstk:
                    low[v] = min(low[v], index[w])
            if advanced:
                continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stk.pop()
                    onstk.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                out.append(comp)
            work.pop()
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    for k in sorted(keys):
        if k not in index:
            strong(k)
    return out


def report(path):
    md, secs, nodes, home, edges = graph(path)
    print(f'\n=== {path} ===')
    print(f'{len(md.split())} words | {len(nodes)} numbered statements | {len(secs)} numbered sections\n')
    print(f'{"sec":>4} {"title":38} {"words":>6} {"stmts":>6} cites->')
    for si, (num, title, a, b) in enumerate(secs):
        body = md[a:b]
        n = sum(1 for k in nodes if k[2] == si)
        c = sorted(secs[j][0] for j in edges.get(si, ()))
        print(f'{num:>4} {title[:38]:38} {len(body.split()):>6} {n:>6} {",".join(c) or "-"}')
    # reverse adjacency (cited-by)
    radj = defaultdict(set)
    for u, vs in edges.items():
        for v in vs:
            radj[v].add(u)
    adj = {u: edges.get(u, set()) | {u} for u in range(len(secs))}
    comps = scc(adj, list(range(len(secs))))
    big = [c for c in comps if len(c) > 1]
    keys = [secs[i][0] for i in sorted(big[0])] if big else []
    print(f'\nstrongly connected components with >1 section: {[sorted(secs[i][0] for i in c) for c in big]}')
    print(f'largest component = sections {keys} | total labels in it: '
          f'{sum(1 for k in nodes if secs[k[2]][0] in keys)} of {len(nodes)}')
    # pairwise mutual reachability inside the largest component
    if big:
        comp = set(big[0])
        reach = {v: set() for v in comp}
        for s in comp:
            seen, stack = set(), [s]
            while stack:
                x = stack.pop()
                for y in edges.get(x, ()):
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
            reach[s] = seen
        tot = len(comp) * (len(comp) - 1) // 2
        mut = sum(1 for i, s in enumerate(sorted(comp)) for t in sorted(comp)[i + 1:]
                  if t in reach[s] and s in reach[t])
        print(f'mutually reachable section pairs: {mut}/{tot} (a clean split needs 0 of {tot})')
    cross = sum(len(v) for v in edges.values())
    # how many *statements* are cited from another section
    incited = set()
    for si, (num, title, a, b) in enumerate(secs):
        for m in re.finditer(r'\b(' + KIND + r')\s+(\d+)\b', md[a:b]):
            k = (m.group(1), int(m.group(2)))
            if k in home and home[k] != si:
                incited.add(k)
    inst = sum(1 for si, (num, title, a, b) in enumerate(secs)
               for m in re.finditer(r'\b(' + KIND + r')\s+(\d+)\b', md[a:b])
               if (m.group(1), int(m.group(2))) in home and home[(m.group(1), int(m.group(2)))] != si)
    print(f'distinct cross-section section-pair edges: {cross} | cross-section citation instances: {inst}')
    print(f'statements cited from outside their home section: {len(incited)} of {len(nodes)}')
    print(f'sections with words but zero statements (demotion candidates): '
          f'{[secs[i][0] for i in range(len(secs)) if not any(n[2] == i for n in nodes) and len(md[secs[i][2]:secs[i][3]].split()) > 300]}')


if __name__ == '__main__':
    for a in sys.argv[1:] or ['/home/user/revision/v7/paper3_material_ledgers_v39.md']:
        report(a)
