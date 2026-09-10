#!/usr/bin/env python3
"""
Machine-checkable claim schema for the generalization of E3 and E4.

Implements the generalization protocol:
  * E3-mechanism*  : portable (near-white recharge + persistent head)
  * E3-verdict*    : portable only under a pre-declared CONJUNCTION
  * E4-constructive*      : scoped to pools with a physical threshold AND m < 0
  * E4-negative*          : holds when the institutional threshold has m > 0

Central object: the **attractor-to-threshold margin**

        m(P, K, F) = K - H*_0(P, F),      H*_0 = (alpha + beta*F) / (1 - a)

the zero-pumping fixpoint under recharge floor F.

Every claim below is a statement about a POOL, indexed by a WELL. No pooling.

Run:  python3 src/claim_schema.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_j27_exploratory as R      # noqa: E402
import run_j27_intervention as I     # noqa: E402

OUT = R.OUT
DOMAIN = {"J-17": (610.0, 710.0), "Uvalde": (820.0, 900.0)}


# ------------------------------------------------------------------ the lemma
def check_lemma_conditions(fit) -> dict:
    """Hypotheses for the emptiness lemma.

    H1 0 < a < 1              (contraction: monotone convergence)
    H2 gamma < 0              (pumping reduces the fixpoint, so P = 0 maximises it)
    """
    return {"H1_contraction": bool(0.0 < fit["a"] < 1.0),
            "H2_gamma_negative": bool(fit["gamma"] < 0),
            "both_hold": bool(0.0 < fit["a"] < 1.0 and fit["gamma"] < 0)}


def H_fixpoint(fit, F, P) -> float:
    """Fixpoint of H_{t+1} = a*H + alpha + beta*F + gamma*P."""
    return (fit["alpha"] + fit["beta"] * F + fit["gamma"] * P) / (1.0 - fit["a"])


def H_star_0(fit, F) -> float:
    """Zero-pumping fixpoint: the MAXIMUM achievable long-run attractor (needs gamma<0)."""
    return H_fixpoint(fit, F, 0.0)


def margin(fit, K, F) -> float:
    """m = K - H*_0.  m > 0  =>  no policy in ANY family with P >= 0 can hold K."""
    return float(K - H_star_0(fit, F))


def critical_floor(fit, K) -> float:
    """F*(K): the recharge floor at which m = 0 exactly (m increases as F falls)."""
    return float((K * (1.0 - fit["a"]) - fit["alpha"]) / fit["beta"])


def time_to_emptiness(fit, K, F, P=0.0, H_top=None) -> float:
    """Analytic horizon at which the trajectory from the top of the domain crosses K.

        H_t - H* = a^t (H_0 - H*), so  t* = ln((K - H*)/(H_0 - H*)) / ln(a)

    With H_0 = H_top this is the LATEST crossing time, i.e. the horizon beyond
    which the T-year kernel is empty. Returns inf if the fixpoint clears K.
    """
    Hs = H_fixpoint(fit, F, P)
    if Hs >= K:
        return float("inf")
    if H_top is None or H_top <= K or H_top <= Hs:
        return float("nan")
    return float(np.log((K - Hs) / (H_top - Hs)) / np.log(fit["a"]))


# --------------------------------------------------------- claim-schema rules
def classify(pool_name, fit, panel, K_phys, K_inst, floors, policies) -> dict:
    """Classify a pool against the four generalized claim schemas."""
    lem = check_lemma_conditions(fit)
    hi = DOMAIN[pool_name][1]
    out = {"pool": pool_name, "lemma": lem, "thresholds": {}, "claims": {}}

    for label, K in (("K_phys", K_phys), ("K_inst", K_inst)):
        if K is None:
            out["thresholds"][label] = None
            continue
        row = {}
        for fn, F in floors.items():
            m = margin(fit, K, F)
            tstar = time_to_emptiness(fit, K, F, 0.0, hi)
            nonempty = [n for n, p in policies.items()
                        if I.kernel(p, fit, F, K, "inf") is not None]
            row[fn] = {"F": float(F), "m_ft": m, "F_star": critical_floor(fit, K),
                       "T_star_zero_pumping": tstar,
                       "predicted": "empty" if m > 0 else "constructive-possible",
                       "observed_nonempty": nonempty}
        out["thresholds"][label] = {"K": float(K), "floors": row}

    # ---- E4-negative*: holds if m(K_inst, F) > 0 for the floor of interest
    ki = out["thresholds"].get("K_inst")
    inst = {}
    if ki:
        for fn, r in ki["floors"].items():
            inst[fn] = {"m_ft": r["m_ft"], "E4_negative_holds": bool(r["m_ft"] > 0)}
    out["claims"]["E4_negative_institutional"] = inst

    # ---- E4-constructive*: needs a physical threshold AND m(K_phys,F) < 0
    kp = out["thresholds"].get("K_phys")
    if kp is None:
        out["claims"]["E4_constructive"] = {
            "in_scope": False,
            "reason": "no physical threshold exists for this pool -> claim not definable "
                      "(scope condition, not a numerical result)"}
    else:
        cs = {}
        for fn, r in kp["floors"].items():
            cs[fn] = {"m_ft": r["m_ft"], "in_scope": bool(r["m_ft"] < 0),
                      "observed_nonempty": r["observed_nonempty"]}
        out["claims"]["E4_constructive"] = cs

    # ---- E3-mechanism*: near-white recharge + persistent head
    def ac1(x):
        x = np.asarray(x, float); x = x[np.isfinite(x)]
        return float(np.corrcoef(x[1:], x[:-1])[0, 1])
    rho_R = ac1(panel["R"].to_numpy(float))
    rho_H = ac1(panel["H"].to_numpy(float))
    out["claims"]["E3_mechanism"] = {
        "rho_R_recharge_whiteness": rho_R, "rho_H_head_persistence": rho_H,
        "near_white": bool(abs(rho_R) < 0.30),
        "persistent_head": bool(rho_H > 0.50),
        "in_scope": bool(abs(rho_R) < 0.30 and rho_H > 0.50)}
    return out


# ------------------------------------------------------------------- driver
def main():
    print("=" * 78)
    print("CLAIM SCHEMA — machine check across both pools")
    print("=" * 78)

    j17 = pd.read_csv(R.DATA / "annual_panel.csv")
    j17 = j17[j17.year.between(1934, 2023)][["year", "H_mean", "R_total", "P_wells"]] \
              .dropna().reset_index(drop=True)
    p17 = j17.rename(columns={"R_total": "R_uv_12", "P_wells": "P_uv"})
    fit_sa = I.fit_affine(p17)
    tr = p17[p17.year <= 1990]; Pbar_sa = float(tr.P_uv.mean())
    fl_sa = {"drought": float(tr.R_uv_12.min()),
             "q05": float(np.percentile(tr.R_uv_12, 5)),
             "q10": float(np.percentile(tr.R_uv_12, 10))}
    pane_sa = pd.DataFrame({"H": p17.H_mean, "R": p17.R_uv_12})
    pol_sa = I.make_policies(Pbar_sa)

    j27 = R.build_j27_panel()
    uv = (j27.merge(R.load_recharge_uv(), on="year", how="left")
             .merge(R.load_pumpage_uv(), on="year", how="left"))
    uv = uv[uv.H_mean.notna() & uv.R_uv_12.notna() & uv.P_uv.notna()].reset_index(drop=True)
    fit_uv = I.fit_affine(uv)
    tru = uv[uv.year <= 1990]; Pbar_uv = float(tru.P_uv.mean())
    fl_uv = {"drought": float(tru.R_uv_12.min()),
             "q05": float(np.percentile(tru.R_uv_12, 5)),
             "q10": float(np.percentile(tru.R_uv_12, 10))}
    pane_uv = pd.DataFrame({"H": uv.H_mean, "R": uv.R_uv_12})
    pol_uv = I.make_policies(Pbar_uv)

    results = {}
    for name, fit, pane, Kp, Ki, fl, pol in [
            ("J-17", fit_sa, pane_sa, 618.0, 660.0, fl_sa, pol_sa),
            ("Uvalde", fit_uv, pane_uv, None, 840.0, fl_uv, pol_uv)]:
        I.H_LO, I.H_HI = DOMAIN[name]
        c = classify(name, fit, pane, Kp, Ki, fl, pol)
        # re-run kernels with this pool's domain (make_policies already bound)
        for label in ("K_phys", "K_inst"):
            if c["thresholds"][label] is None:
                continue
            K = c["thresholds"][label]["K"]
            for fn, F in fl.items():
                ne = [n for n, p in pol.items() if I.kernel(p, fit, F, K, "inf") is not None]
                c["thresholds"][label]["floors"][fn]["observed_nonempty"] = ne
        if label := ("E4_constructive" if Kp else None):
            pass
        if Kp:
            for fn, F in fl.items():
                ne = [n for n, p in pol.items() if I.kernel(p, fit, F, Kp, "inf") is not None]
                c["claims"]["E4_constructive"][fn]["observed_nonempty"] = ne
        results[name] = c
        # normalize keys: J-17 K_phys first
        c["thresholds"]["K_phys"], c["thresholds"]["K_inst"] = \
            c["thresholds"]["K_phys"], c["thresholds"]["K_inst"]

        print(f"\n### {name}  (lemma hypotheses: {c['lemma']})")
        for label in ("K_phys", "K_inst"):
            t = c["thresholds"][label]
            if t is None:
                print(f"  {label}: NONE (no physical threshold — scope condition)")
                continue
            for fn, r in t["floors"].items():
                print(f"  {label} K={r and t['K']:.0f} {fn:8s} F={r['F']:6.2f} "
                      f"H*_0={t['K']-r['m_ft']:7.2f} m={r['m_ft']:+6.2f} "
                      f"F*={r['F_star']:6.2f} T*={r['T_star_zero_pumping']:5.1f} "
                      f"| {r['predicted']:20s} | observed={r['observed_nonempty'] or 'NONE'}")
        e4c = c["claims"]["E4_constructive"]
        print(f"  E3-mechanism* in scope: {c['claims']['E3_mechanism']['in_scope']} "
              f"(rho_R={c['claims']['E3_mechanism']['rho_R_recharge_whiteness']:.3f}, "
              f"rho_H={c['claims']['E3_mechanism']['rho_H_head_persistence']:.3f})")
        if isinstance(e4c, dict) and "in_scope" in e4c:
            print(f"  E4-constructive* in scope: {e4c['in_scope']} — {e4c['reason']}")
        else:
            print("  E4-constructive* in scope: "
                  + ", ".join(f"{k}={v['in_scope']}" for k, v in e4c.items()))
        print("  E4-negative* holds: "
              + ", ".join(f"{k}={v['E4_negative_holds']} (m={v['m_ft']:+.2f})"
                          for k, v in c["claims"]["E4_negative_institutional"].items()))

    # ---- the analytic lemma check vs exhaustive policy search
    print("\n" + "=" * 78)
    print("LEMMA CHECK: m>0  =>  kernel empty for every policy of the declared family")
    print("=" * 78)
    viol = 0; tot = 0
    for name, fit, pane, Ks, fl, pol in [
            ("J-17", fit_sa, pane_sa, [618.0, 660.0], fl_sa, pol_sa),
            ("Uvalde", fit_uv, pane_uv, [835.0, 840.0, 845.0], fl_uv, pol_uv)]:
        I.H_LO, I.H_HI = DOMAIN[name]
        for K in Ks:
            for fn, F in fl.items():
                m = margin(fit, K, F)
                ne = [n for n, p in pol.items() if I.kernel(p, fit, F, K, "inf") is not None]
                tot += 1
                if m > 0 and ne:
                    viol += 1
                    print(f"  VIOLATION {name} K={K} {fn}: m={m:+.2f} but nonempty={ne}")
    print(f"  cases tested={tot}  violations of the lemma={viol}")

    with open(OUT / "claim_schema_results.json", "w") as f:
        json.dump({"status": "EXPLORATORY_NOT_FROZEN",
                   "lemma_violations": viol, "cases_tested": tot,
                   "pools": results}, f, indent=2, default=str)
    print(f"\nwritten: {OUT/'claim_schema_results.json'}")


if __name__ == "__main__":
    main()
