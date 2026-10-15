"""The finite-horizon recursively viable selector (exact, parameter-passing).

Ported verbatim from the programme's verified implementations
(`paper2_selector_concordance_v1_verify.py`, checks C3/C4/C5; the calculus's
Theorem 1). The no-repeat codex is threaded as a parameter — the round-six
lesson: never a global.
"""
from itertools import product


def _parts(B, info):
    p = {}
    for x in B:
        p.setdefault(info(x), set()).add(x)
    return p


def _cell_actions(sys, c, last, alt):
    cu = [u for u in sys.actions
          if u != sys.null and all(sys.is_safe(sys.step(x, u)) for x in c)]
    if alt:
        cu = [u for u in cu if u != last]
    return cu


def viable(sys, B, info, h, last=None, alt=False) -> bool:
    """Read-then-act winning recursion at horizon h.

    B:     belief (frozenset of states)
    info:  observation map state -> cell key (the fibres)
    alt:   enforce the institutional no-repeat codex u != last choice
    """
    if h == 0:
        return all(sys.is_safe(x) for x in B)
    cells = _parts(B, info)
    acts = []
    for c in cells.values():
        cu = _cell_actions(sys, c, last, alt)
        if not cu:
            return False
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for c, u in zip(cells.values(), choice):
            succ |= {sys.step(x, u) for x in c}
        ps = [frozenset(p) for p in _parts(succ, info).values()]
        if all(viable(sys, p, info, h - 1, choice[0], alt) for p in ps):
            return True
    return False


def verdict(sys, B, info, H=12, alt=False) -> bool:
    """The audited two-horizon verdict (H and H-2)."""
    return viable(sys, B, info, H, None, alt) and viable(sys, B, info, H - 2, None, alt)


def kernel(sys, info, pairs, H=12, alt=False):
    """The viable subset of `pairs` under (info, alt)."""
    return frozenset(B for B in pairs if verdict(sys, B, info, H, alt))


def witness(sys, B, info, h, alt=False):
    """A witnessing per-fibre first action vector, or None if not viable.

    Returns a list of (cell_key, action) in fibre-sorted order; exactness
    follows from the recursion (the witness exists iff `viable` holds).
    """
    if h == 0:
        return [] if all(sys.is_safe(x) for x in B) else None
    cells = _parts(B, info)
    keys = sorted(cells, key=repr)
    acts = []
    for k in keys:
        cu = _cell_actions(sys, cells[k], None, alt)
        if not cu:
            return None
        acts.append(cu)
    for choice in product(*acts):
        succ = set()
        for k, u in zip(keys, choice):
            succ |= {sys.step(x, u) for x in cells[k]}
        ps = [frozenset(p) for p in _parts(succ, info).values()]
        if all(viable(sys, p, info, h - 1, choice[0], alt) for p in ps):
            return list(zip(keys, choice))
    return None
