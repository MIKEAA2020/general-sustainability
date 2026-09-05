"""Labelled eval harness for the master->revision matcher.

Measures the matcher against a small, human-checked gold set (`scan/gold.py`):

  * **Retrieval** — does the matcher place a gold paragraph at rank 1 (Recall@1)
    and within the top 3 (Recall@3), for all 22 master claims?
  * **Pair classification** — over gold positives + hard negatives, at a given
    match threshold, does it separate genuine matches from lookalikes?

Anchors are distinctive SUBSTRINGS resolved to paragraphs at run time, so the gold
set is robust to re-numbering / edits (line-number anchors broke once the revision
was edited). The backend is swappable: default offline TF-IDF+BM25, or an opt-in
embedding model via --embedding-model (SPECTER / all-mpnet) to compare.
"""
import json
import argparse
from pathlib import Path

import numpy as np

from .gold import GOLD_PHRASES, HARD_NEG_PHRASES
from .parser import parse_master, parse_revision
from .matcher import SemanticMatcher, _bm25


import re as _re


def _norm(s):
    """Collapse whitespace runs to a single space (parser joins indented lines
    into extra spaces) and lowercase, so substring anchors survive formatting."""
    return _re.sub(r"\s+", " ", s.lower())


def _resolve(revision_claims, phrases):
    """Return the set of revision paragraphs containing any of `phrases` (case-insensitive,
    whitespace-normalised)."""
    nph = [_norm(p) for p in phrases]
    hits = []
    for c in revision_claims:
        low = _norm(c.text)
        for ph in nph:
            if ph in low:
                hits.append(c)
                break
    # dedupe, preserve order
    seen, out = set(), []
    for c in hits:
        if c.line_number not in seen:
            seen.add(c.line_number); out.append(c)
    return out


def _score_matrix(matcher, master_claims, revision_claims):
    rev_texts = [c.text for c in revision_claims]
    master_texts = [c.text for c in master_claims]
    if not rev_texts:
        return np.zeros((len(master_claims), 0))
    cos = matcher._cosine(master_texts, rev_texts)
    bm = _bm25(master_texts, rev_texts)
    cos = (cos - cos.min()) / (cos.max() - cos.min() + 1e-9)
    return matcher.sem_weight * cos + matcher.bm25_weight * bm


def run_eval(master_path, revision_path, thresholds=(0.2, 0.55, 0.75),
             model_name=None, topk=3):
    master = parse_master(master_path)
    rev = parse_revision(revision_path)
    if model_name:
        try:
            import sentence_transformers  # noqa: F401
        except Exception as e:
            raise RuntimeError(
                f"--embedding-model {model_name} requires `sentence-transformers` "
                f"(and the model's weights). Not installed/importable: {e!r}. "
                f"Re-run without --embedding-model to use the offline default.") from e
    matcher = SemanticMatcher(model_name=model_name)
    S = _score_matrix(matcher, master, rev)
    claim_ids = [c.id for c in master]
    idx = {c.id: i for i, c in enumerate(master)}
    by_line = {c.line_number: i for i, c in enumerate(rev)}

    # ---- retrieval: top-1 / top-k against the resolved gold paragraphs ----
    recall1 = recall3 = 0
    hard = []
    diagnostics = []
    gold_scores = []
    for cid in claim_ids:
        i = idx[cid]
        gold_paras = _resolve(rev, GOLD_PHRASES.get(cid, []))
        gold_lines = {p.line_number for p in gold_paras}
        order = np.argsort(-S[i]).tolist()
        top_lines = [rev[j].line_number for j in order[:topk]]
        top1 = rev[order[0]].line_number if order else None
        best_gold = max((float(S[i, by_line[p.line_number]]) for p in gold_paras), default=0.0)
        gold_scores.append(best_gold)
        if top1 in gold_lines:
            recall1 += 1
        if any(l in gold_lines for l in top_lines):
            recall3 += 1
        else:
            hard.append(cid)
            diagnostics.append({
                "claim": cid, "gold_lines": sorted(gold_lines),
                "best_gold_score": round(best_gold, 3),
                "top1_line": top1, "top1_text": rev[order[0]].text[:70] if order else ""})
    n = len(claim_ids)
    gold_scores = np.array(gold_scores) if gold_scores else np.zeros(1)

    # ---- pair classification over gold positives + hard negatives ----
    pairs = []
    gold_para_set = {}
    for cid in claim_ids:
        i = idx[cid]
        gold_paras = _resolve(rev, GOLD_PHRASES.get(cid, []))
        gold_para_set[cid] = {p.line_number for p in gold_paras}
        for p in gold_paras:
            pairs.append((cid, p, True, float(S[i, by_line[p.line_number]])))
    added = set()
    for cid in claim_ids:
        i = idx[cid]
        neg_paras = _resolve(rev, HARD_NEG_PHRASES.get(cid, []))
        for p in neg_paras:
            if p.line_number in gold_para_set.get(cid, set()):
                continue
            if (cid, p.line_number) in added:
                continue
            if not any(_norm(ph) in _norm(p.text) for ph in HARD_NEG_PHRASES.get(cid, [])):
                continue
            added.add((cid, p.line_number))
            pairs.append((cid, p, False, float(S[i, by_line[p.line_number]])))
    # top lookalikes that aren't gold but score highest where no explicit negative exists
    for cid in claim_ids:
        i = idx[cid]
        for j in np.argsort(-S[i])[:5]:
            line = rev[j].line_number
            if line in gold_para_set.get(cid, set()) or (cid, line) in added:
                continue
            if not any(ph.lower() in rev[j].text.lower() for ph in HARD_NEG_PHRASES.get(cid, [])):
                continue
            added.add((cid, line))
            pairs.append((cid, rev[j], False, float(S[i, j])))

    results = {"backend": ("embedding:" + model_name) if model_name else "tfidf+bm25 (offline)",
               "n_claims": n, "recall@1": round(recall1 / n, 4),
               "recall@%d" % topk: round(recall3 / n, 4),
               "gold_best_score": {"mean": round(float(gold_scores.mean()), 4),
                                   "min": round(float(gold_scores.min()), 4),
                                   "max": round(float(gold_scores.max()), 4)},
               "hard_cases": hard, "diagnostics": diagnostics, "thresholds": {}}
    for t in thresholds:
        pos = [1 if p[2] else 0 for p in pairs]
        pred = [1 if p[3] >= t else 0 for p in pairs]
        tp = sum(1 for a, b in zip(pos, pred) if a == 1 and b == 1)
        fp = sum(1 for a, b in zip(pos, pred) if a == 0 and b == 1)
        fn = sum(1 for a, b in zip(pos, pred) if a == 1 and b == 0)
        prec = tp / (tp + fp) if (tp + fp) else 0.0
        rec = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        results["thresholds"][str(t)] = {
            "n_pos": sum(pos), "n_neg": len(pos) - sum(pos),
            "precision": round(prec, 4), "recall": round(rec, 4), "f1": round(f1, 4)}
    return results


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="scan_revision eval",
        description="Evaluate the master->revision matcher against the labelled gold set.")
    p.add_argument("--master", "-m", default="data/MASTER_joint_assessment_and_implementation_plan.md")
    p.add_argument("--revision", "-r", default="data/IMPLEMENTED_revision_ECOMOD.md")
    p.add_argument("--embedding-model", default="",
                   help="OPT-IN sentence-transformers model (e.g. allenai/specter). "
                        "Requires sentence-transformers + model weights. "
                        "Default is the offline TF-IDF+BM25 backend.")
    p.add_argument("--out", "-o", default="eval/results.json")
    p.add_argument("--thresholds", default="0.15,0.2,0.3,0.45,0.6")
    p.add_argument("--topk", type=int, default=3)
    a = p.parse_args(argv)
    th = tuple(float(x) for x in a.thresholds.split(","))
    res = run_eval(a.master, a.revision, thresholds=th,
                   model_name=a.embedding_model or None, topk=a.topk)

    from rich.console import Console
    from rich.table import Table
    con = Console()
    con.print(f"[bold]Matcher eval — backend:[/bold] {res['backend']}")
    rk = f"recall@{a.topk}"
    con.print(f"Recall@1: {res['recall@1']:.2f}   {rk}: {res.get(rk, 0):.2f} "
              f"on {res['n_claims']} claims")
    con.print(f"Gold best-match score: mean {res['gold_best_score']['mean']:.2f} "
              f"(min {res['gold_best_score']['min']:.2f}, max {res['gold_best_score']['max']:.2f})")
    t = Table(title="Pair classification")
    t.add_column("Threshold"); t.add_column("Precision"); t.add_column("Recall"); t.add_column("F1")
    for k, v in res["thresholds"].items():
        t.add_row(k, f"{v['precision']:.2f}", f"{v['recall']:.2f}", f"{v['f1']:.2f}")
    con.print(t)
    if res["hard_cases"]:
        con.print(f"[yellow]Recall misses (top-{a.topk} not gold):[/yellow] {res['hard_cases']}")
        for d in res["diagnostics"]:
            con.print(f"  {d['claim']}: gold@{d['gold_lines']} (score {d['best_gold_score']}) "
                      f"but top1=L{d['top1_line']} \"{d['top1_text']}\"")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=2))
    con.print(f"[green]Wrote {out}[/green]")
    return res


if __name__ == "__main__":
    main()
