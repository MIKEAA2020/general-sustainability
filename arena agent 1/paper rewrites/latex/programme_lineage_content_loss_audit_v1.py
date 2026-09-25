#!/usr/bin/env python3
"""
Lineage content-loss audit: seed/intermediate -> current.
Extracts structural units from each version and flags anything present in an
older version but absent from the current one:
  - titled environments (theorem/proposition/lemma/corollary/definition/remark/example/conjecture/assumption)
  - section/subsection headings
  - figure/table captions
  - bibliography entries (author-year tokens)
  - distinctive exact constants (tfrac/frac tokens, decimals, big integers)
Output: one line per (lineage, missing unit) for manual adjudication.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

LINEAGES = {
    "minimax": (["minimax_dual_certificates_v%d.tex" % i for i in range(1, 8)], 7),
    "comp-main": (["paper2_computational_certification_v%d.tex" % i for i in range(1, 16)], 15),
    "comp-supp": (["paper2_computational_certification_v%d_supplementary.tex" % i for i in range(1, 6)]
                  + ["paper2_computational_certification_supplementary_v6.tex"], 6),
    "ws": (["paper2_worked_systems_v%d.tex" % i for i in range(1, 16)], 15),
    "ebc": (["paper2_exact_belief_computation_v%d.tex" % i for i in range(1, 7)], 6),
    "ARV": (["applied_regime_viability_v%d.tex" % i for i in range(1, 7)], 6),
    "E1": (["paperE1_cod_forecast_ladder_v%d.tex" % i for i in range(49, 57)], 56),
    "P1": (["paper2_obstruction_calculus_v50_Automatica_routes.tex",
            "paper2_obstruction_calculus_v51_Automatica_routes.tex",
            "paper2_obstruction_calculus_v52_Automatica_routes.tex",
            "paper2_obstruction_calculus_v53_Automatica_routes.tex"], 53),
    "P3": (["paper2_probabilistic_sufficiency_v%d.tex" % i for i in range(1, 9)], 8),
}

ENVS = ("theorem", "proposition", "lemma", "corollary", "definition",
        "remark", "example", "conjecture", "assumption", "observation")

ENV_RE = re.compile(r"\\begin\{(%s)\}\s*(?:\[[^\]]*\])?\s*\[([^\]]+)\]" % "|".join(ENVS))
ENV_PLAIN_RE = re.compile(r"\\begin\{(%s)\}\s*(?:\[[^\]]*\])?" % "|".join(ENVS))
SEC_RE = re.compile(r"\\(section|subsection)\*?\{([^}]*)\}")
CAP_RE = re.compile(r"\\caption\{([^}]*)\}")


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def strip_comments(t):
    out = []
    for ln in t.split("\n"):
        i = ln.find("%")
        if i >= 0 and (i == 0 or ln[i-1] != "\\"):
            ln = ln[:i]
        out.append(ln)
    return "\n".join(out)


def units(t):
    """all structural units of a version"""
    t = strip_comments(t)
    envs = [("env", e, norm(title)) for e, title in ENV_RE.findall(t)]
    secs = [("sec", norm(h), h) for _, h in SEC_RE.findall(t)]
    caps = [("cap", norm(c)[:60], c[:80]) for c in CAP_RE.findall(t)]
    return envs, secs, caps


def bib_tokens(t):
    """author-year tokens from the references block"""
    t = strip_comments(t)
    i = t.rfind("\\section*{References}")
    if i < 0:
        i = t.rfind("\\begin{thebibliography}")
    if i < 0:
        return set()
    block = t[i:]
    block = re.sub(r"\\url\{[^}]*\}", " ", block)
    block = re.sub(r"\\emph\{([^}]*)\}", r"\1", block)
    toks = set()
    for m in re.finditer(r"([A-Z][A-Za-z'\-]+(?:,? (?:[A-Z]\.|et al\.))*)[, ]*\(?(1[89]\d\d|20\d\d)\)?", block):
        name = norm(m.group(1))[:10]
        if name:
            toks.add(name + "@" + m.group(2))
    return toks


def constants(t):
    """distinctive exact numbers"""
    t = strip_comments(t)
    t = re.sub(r"(caption|label|ref|url)\{[^}]*\}", " ", t)
    c = set()
    c.update(m.group(1) for m in re.finditer(r"\\t?frac\{(\d+)\}\{(\d+)\}", t))
    c.update(m.group(0) for m in re.finditer(r"\d+\.\d+", t))
    c.update(m.group(0) for m in re.finditer(r"\d{3,}", t))
    return {x for x in c if len(x) >= 2}


def main():
    for fam, (files, cur_n) in LINEAGES.items():
        paths = [os.path.join(HERE, f) for f in files]
        texts = {}
        for f, p in zip(files, paths):
            if os.path.exists(p):
                texts[f] = open(p, encoding="utf-8").read()
        if len(texts) < 2:
            print(f"== {fam}: insufficient versions, skipped")
            continue
        cur_file = files[-1]
        cur = texts[cur_file]
        cur_norm = norm(strip_comments(cur))
        cur_envs, cur_secs, cur_caps = units(cur)
        cur_env_titles = {(e, ti) for _, e, ti in cur_envs}
        cur_all_titles = {ti for _, e, ti in cur_envs if ti}
        cur_bib = bib_tokens(cur)
        cur_const = constants(cur)

        print(f"== {fam}: {len(texts)} versions, current={cur_file}")
        for f in files[:-1]:
            if f not in texts:
                continue
            t = texts[f]
            envs, secs, caps = units(t)
            miss_env = [(e, ti) for _, e, ti in envs if ti and (e, ti) not in cur_env_titles and ti not in cur_all_titles and norm(ti) not in cur_norm]
            # sections that vanished entirely
            miss_sec = [h for _, sh, h in secs if sh not in {s for _, s, _ in [(0, norm(x), x) for x in []]} and norm(h) not in cur_norm]
            miss_cap = [c for _, ch, c in caps if ch not in cur_norm]
            bt = bib_tokens(t) - cur_bib
            ct = constants(t) - cur_const
            for e, ti in miss_env:
                print(f"  [{f}] MISSING-ENV {e}: {ti[:90]}")
            for h in miss_sec:
                print(f"  [{f}] MISSING-SEC {h[:90]}")
            for c in miss_cap:
                print(f"  [{f}] MISSING-CAP {c[:90]}")
            if bt:
                print(f"  [{f}] BIB-DROPPED ({len(bt)}): {sorted(bt)[:12]}")
            if ct:
                print(f"  [{f}] CONST-DROPPED ({len(ct)}): {sorted(ct)[:24]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
