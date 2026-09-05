"""`scan_revision` CLI. Run: `scan_revision scan --master ... --revision ...`.

Uses argparse (robust, zero-quirk) rather than a framework. The pipeline stages
are kept in the library modules so they can be reused and tested directly.
"""
import argparse, json, logging, re
from pathlib import Path
from datetime import datetime

from .parser import parse_master, parse_revision
from .classifier import classify_all
from .matcher import SemanticMatcher
from .numeric import run_all_numeric_checks
from .consistency import ConsistencyChecker
from .risk import compute_risk
from .report import (generate_html_report, generate_json_report, generate_csv_report,
                     generate_audit_summary)
from .models import ScanReport
from .utils import load_config, ensure_dir

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("scan_revision")

def _sentences(text):
    text = text.replace("\n", " ")
    parts = re.split(r'(?<=[.!?;:])\s+', text)
    return [p.strip() for p in parts if len(p.strip()) > 25]

def run_scan(master, revision, config="config.yaml", report_dir="reports",
             embedding_model="", nli_model="", skip_numeric=False, skip_consistency=False):
    cfg = load_config(config) if Path(config).exists() else {}
    ensure_dir(report_dir)
    log.info("Parsing master checklist ...")
    master_claims = parse_master(master)
    log.info("  %d numbered items", len(master_claims))
    log.info("Parsing revision for paragraph targets ...")
    revision_claims = parse_revision(revision)
    log.info("  %d paragraphs", len(revision_claims))

    master_claims = classify_all(master_claims)

    matcher = SemanticMatcher(model_name=embedding_model or cfg.get("embedding_model"),
                              semantic_threshold=cfg.get("semantic_threshold", 0.75),
                              partial_threshold=cfg.get("partial_threshold", 0.55))
    matches = matcher.match_claims(master_claims, revision_claims)

    # item 3: actionable items run the *execute* pipeline (need evidence/computation),
    # informational items need only *presence* in the revision.
    try:
        from .curated import (OVERRIDES, ORIGINAL_MODEL_IDS, CORRECTED_MODEL_IDS,
                              CURATED_DECISIONS, NOT_SUPERSEDED)
    except Exception:
        (OVERRIDES, ORIGINAL_MODEL_IDS, CORRECTED_MODEL_IDS,
         CURATED_DECISIONS, NOT_SUPERSEDED) = {}, set(), set(), {}, set()
    # two-tier confidence: the hybrid score is a RANKING score, not a probability
    retrieval_t = cfg.get("retrieval_threshold", 0.20)
    auto_covered_t = cfg.get("auto_covered_threshold", 0.60)
    for m in matches:
        m.pipeline = "execute" if m.master_claim.type == "actionable" else "presence"
        m.model_version = ("original" if m.master_claim.id in ORIGINAL_MODEL_IDS
                           else ("corrected (1\u2034)" if m.master_claim.id in CORRECTED_MODEL_IDS
                                 else "original (see note)"))
        m.auto_tier = ("auto-covered" if m.score >= auto_covered_t
                       else ("candidate" if m.score >= retrieval_t else "none"))

    numeric = []
    if not skip_numeric:
        log.info("Verifying numerical claims ...")
        numeric = run_all_numeric_checks(master_claims, cfg)
        log.info("  %d verifications", len(numeric))

    # supersession is decided AFTER numeric verification (numeric SUPERSEDED verdict or
    # explicit markers) — never from a low score (refined-scan item 1).
    from .status import apply_superseded
    apply_superseded(matches, [n.model_dump() for n in numeric])

    # authoritative curated overrides; keep auto status + score as evidence
    for m in matches:
        m.auto_status = m.status
        if m.master_claim.id in OVERRIDES:
            st, note = OVERRIDES[m.master_claim.id]
            m.status = st if st in ("covered", "partial", "superseded", "missing", "ambiguous") else "covered"
            # documented human decision, if any (keeps future scans consistent)
            if m.master_claim.id in CURATED_DECISIONS and m.auto_status != m.status:
                note = CURATED_DECISIONS[m.master_claim.id][1]
                m.note = note
            m.note = note
            m.auto_note = (f"AUTO said '{m.auto_status}', tier '{m.auto_tier}' "
                           f"(score {m.score:.2f}); differs from curated verdict — see note."
                           ) if m.auto_status != m.status else ""

    consistency = []
    if not skip_consistency:
        log.info("Checking internal consistency ...")
        checker = ConsistencyChecker(model_name=nli_model or cfg.get("nli_model"))
        with open(revision) as f:
            sentences = _sentences(f.read())
        consistency = checker.find_contradictions(sentences, cfg.get("consistent_terms"))

    risk = compute_risk(matches, cfg, numeric)
    # refined-scan item 3: filter the register by a risk threshold (default 0.3);
    # keep all items so the report can show what was dropped.
    risk_threshold = cfg.get("risk", {}).get("threshold", 0.3)
    from .risk import filter_risk
    risk_in, risk_dropped = filter_risk(risk, risk_threshold)

    report = ScanReport(master_path=master, revision_path=revision,
                        timestamp=datetime.utcnow().isoformat() + "Z", config=cfg,
                        matches=matches, numeric=numeric, consistency=consistency, risk=risk_in)
    generate_html_report(report, str(Path(report_dir) / "traceability.html"),
                         dropped_risk=len(risk_dropped))
    generate_json_report(report, str(Path(report_dir) / "scan_report.json"))
    generate_csv_report(report, str(Path(report_dir) / "traceability.csv"))
    generate_audit_summary(report, str(Path(report_dir) / "audit_summary.md"))
    # replayable pipeline log
    provenance = [{"id": m.master_claim.id, "source_file": m.master_claim.source_file,
                   "line": m.master_claim.line_number, "section": m.master_claim.section,
                   "type": m.master_claim.type, "pipeline": m.pipeline,
                   "method": m.method, "status": m.status, "score": m.score,
                   "revision_line": m.revision_claim.line_number if m.revision_claim else None}
                  for m in matches]
    with open(Path(report_dir) / "scan_log.json", "w") as f:
        json.dump({"tool": "scan_revision", "version": "0.1.0",
                   "pipeline": "parse->classify->match->numeric->consistency->risk->report->review",
                   "master": master, "revision": revision, "config": cfg,
                   "report_dir": report_dir, "timestamp": report.timestamp,
                   "parameters": {"semantic_threshold": cfg.get("semantic_threshold"),
                                  "partial_threshold": cfg.get("partial_threshold"),
                                  "numeric_tolerance": 0.02,
                                  "embedding_model": embedding_model or cfg.get("embedding_model"),
                                  "nli_model": nli_model or cfg.get("nli_model")},
                   "counts": {"master_items": len(master_claims),
                              "covered": sum(1 for m in matches if m.status == "covered"),
                              "partial": sum(1 for m in matches if m.status == "partial"),
                              "missing": sum(1 for m in matches if m.status == "missing"),
                              "superseded": sum(1 for m in matches if m.status == "superseded"),
                              "ambiguous": sum(1 for m in matches if m.status == "ambiguous"),
                              "numeric_verified": len(numeric),
                              "consistency_issues": len(consistency)},
                   "provenance": provenance,
                   "replay": f"scan_revision scan --master {master} --revision {revision} "
                             f"--config {config} --report-dir {report_dir}"},
                  f, indent=2)
    # console summary
    from rich.console import Console
    from rich.table import Table
    con = Console(); t = Table(title="Scan summary")
    for st in ["covered", "partial", "superseded", "ambiguous", "missing"]:
        t.add_row(st, str(sum(1 for m in matches if m.status == st)))
    con.print(t)
    con.print(f"[green]Reports:[/green] {report_dir}/traceability.html, scan_report.json, traceability.csv")
    triggers = [m.master_claim.id for m in matches if m.status in ("missing", "superseded")]
    if triggers:
        con.print(f"[yellow]Re-check triggers:[/yellow] {triggers}")
    return report

def run_review(report_path, reviewer_fn=None, out_dir="reports"):
    from .review import review
    from .models import ScanReport
    rep = ScanReport.model_validate_json(Path(report_path).read_text())
    passes = review(rep, reviewer_fn)
    from rich.console import Console
    from rich.table import Table
    con = Console(); t = Table(title="LLM peer review (multi-pass)")
    t.add_column("Pass"); t.add_column("Score /5"); t.add_column("Findings")
    for p in passes:
        t.add_row(p["pass"], f"{p['score']:.2f}", p["findings"][:160])
    con.print(t)
    out = Path(out_dir) / "review_report.json"
    json.dump({"source": report_path, "timestamp": datetime.utcnow().isoformat() + "Z",
               "passes": passes}, open(out, "w"), indent=2)
    con.print(f"[green]Review written:[/green] {out}")
    return passes


def run_diff(old_report, new_report):
    from .semantic_diff import diff_versions
    from .models import ScanReport
    old = ScanReport.model_validate_json(Path(old_report).read_text())
    new = ScanReport.model_validate_json(Path(new_report).read_text())
    d = diff_versions(old.matches, new.matches)
    from rich.console import Console
    from rich.table import Table
    con = Console()
    con.print(f"[bold]Semantic diff[/bold] — {d['summary']['n_status_changed']} status "
              f"change(s), {d['summary']['n_semantic_shifts']} semantic shift(s)")
    t = Table(title="Status map"); t.add_column("ID"); t.add_column("Old")
    t.add_column("New"); t.add_column("Change")
    for cid, o, n, label in d["status_map"]:
        if o != n:
            t.add_row(cid, o, n, label)
    con.print(t)
    if d["semantic_changes"]:
        t2 = Table(title="Semantic shifts"); t2.add_column("ID"); t2.add_column("Old text")
        t2.add_column("New text"); t2.add_column("sim")
        for s in d["semantic_changes"]:
            t2.add_row(s["claim_id"], s["old"], s["new"], f"{s['similarity']:.2f}")
        con.print(t2)
    return d


def main(argv=None):
    p = argparse.ArgumentParser(prog="scan_revision",
                                description="Master->revision gap scan (repeatable, auditable).")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="run the gap scan")
    s.add_argument("--master", "-m", required=True, help="master/checklist markdown")
    s.add_argument("--revision", "-r", required=True, help="revision markdown")
    s.add_argument("--config", "-c", default="config.yaml", help="config YAML")
    s.add_argument("--report-dir", "-o", default="reports", help="output directory")
    s.add_argument("--embedding-model", default="", help="optional sentence-transformers model name")
    s.add_argument("--nli-model", default="", help="optional transformers NLI model name")
    s.add_argument("--skip-numeric", action="store_true", help="skip numerical verification")
    s.add_argument("--skip-consistency", action="store_true", help="skip consistency check")
    rv = sub.add_parser("review", help="run multi-pass rubric peer review on a scan report")
    rv.add_argument("--report", "-j", default="reports/scan_report.json", help="report JSON")
    df = sub.add_parser("diff", help="semantic diff of two versions' structured statements")
    df.add_argument("--old", required=True, help="previous scan_report.json")
    df.add_argument("--new", required=True, help="current scan_report.json")
    cv = sub.add_parser("eval", help="evaluate the matcher against the labelled gold set")
    cv.add_argument("--master", "-m", default="data/MASTER_joint_assessment_and_implementation_plan.md")
    cv.add_argument("--revision", "-r", default="data/IMPLEMENTED_revision_ECOMOD.md")
    cv.add_argument("--embedding-model", default="", help="OPT-IN embedding model (SPECTER/all-mpnet)")
    cv.add_argument("--out", "-o", default="eval/results.json")
    cv.add_argument("--thresholds", default="0.55,0.75")
    a = p.parse_args(argv)
    if a.cmd == "scan":
        run_scan(a.master, a.revision, a.config, a.report_dir,
                 a.embedding_model, a.nli_model, a.skip_numeric, a.skip_consistency)
    elif a.cmd == "review":
        run_review(a.report)
    elif a.cmd == "diff":
        run_diff(a.old, a.new)
    elif a.cmd == "eval":
        from .eval import main as eval_main
        eval_main(["--master", a.master, "--revision", a.revision,
                   "--embedding-model", a.embedding_model, "--out", a.out,
                   "--thresholds", a.thresholds])

if __name__ == "__main__":
    main()
