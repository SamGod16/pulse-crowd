#!/usr/bin/env python3
"""
Adaptive 1,000+ Virtual Crowd Simulator for mirofish-crowd-sim.

Pure Python 3 stdlib agent-based crowd simulation modeling:
  1. Adaptive population sizing (hard floor >= 1,000 virtual personas via size_swarm.py).
  2. Stratified individual persona generation across project cohorts.
  3. Round 1: Onboarding & discovery friction + direct value fit.
  4. Round 2: Asymmetric social contagion (peer clusters, skeptic negativity bias,
     influencer/legal amplifier spillovers).
  5. Round 3: Operational liquidity match, pricing/tier fairness, retention outcomes,
     B2B payment willingness, and Monte Carlo confidence intervals across runs.

NOTE: Outputs are synthetic scenario-sensitivity metrics derived from the provided
project assumptions and calibrated cohorts; they are NOT real-world user telemetry.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from size_swarm import DEFAULT_MAX_POPULATION, MIN_TOTAL_POPULATION, compute_sizing_plan  # noqa: E402


def clamp(val: float, low: float, high: float) -> float:
    return max(low, min(high, val))


def validate_spec(spec: dict[str, Any]) -> None:
    cohorts = spec.get("cohorts")
    if not isinstance(cohorts, list) or len(cohorts) < 2:
        raise ValueError("Project spec must define at least 2 cohorts in 'cohorts'.")
    seen_ids = set()
    for idx, c in enumerate(cohorts):
        cid = c.get("id")
        if not cid or not isinstance(cid, str):
            raise ValueError(f"Cohort index {idx} must include a non-empty string 'id'.")
        if cid in seen_ids:
            raise ValueError(f"Duplicate cohort id: {cid}")
        seen_ids.add(cid)
        if float(c.get("share", 0)) <= 0:
            raise ValueError(f"Cohort '{cid}' share must be > 0.")


def _spawn_individuals(
    cohorts: list[dict[str, Any]],
    allocations: list[dict[str, Any]],
    rng: random.Random,
) -> list[dict[str, Any]]:
    cohort_by_id = {c["id"]: c for c in cohorts}
    individuals: list[dict[str, Any]] = []
    counter = 0

    for alloc in allocations:
        cid = alloc["id"]
        c = cohort_by_id[cid]
        count = int(alloc["allocated_personas"])

        base_value = float(c.get("value_fit", 0.45))
        base_trust = float(c.get("initial_trust", 0.25))
        onboarding_friction = clamp(float(c.get("onboarding_friction", 0.2)), 0.0, 1.0)
        regulatory_risk = clamp(float(c.get("regulatory_blocker_risk", 0.1)), 0.0, 1.0)
        pricing_fairness = clamp(float(c.get("pricing_fairness", 0.2)), -1.0, 1.0)
        local_liquidity = clamp(float(c.get("local_liquidity", 0.65)), 0.0, 1.0)
        liquidity_dep = clamp(float(c.get("liquidity_dependence", 0.5)), 0.0, 1.0)
        susceptibility = clamp(float(c.get("social_susceptibility", 0.45)), 0.0, 1.0)
        voice_weight = max(0.2, float(c.get("social_voice_weight", 1.0)))
        is_buyer = bool(c.get("is_b2b_buyer", False))
        pro_fit = clamp(float(c.get("pro_value_fit", 0.35)), 0.0, 1.0)
        skeptic_bias = float(c.get("skepticism_bias", 0.0))

        for _ in range(count):
            counter += 1
            # Heterogeneous traits around cohort anchor
            ind_value = clamp(rng.gauss(base_value, 0.16), -1.0, 1.0)
            ind_trust = clamp(rng.gauss(base_trust, 0.16), -1.0, 1.0)
            privacy_sensitivity = clamp(rng.gauss(0.5 + 0.35 * regulatory_risk, 0.18), 0.05, 1.0)
            patience = clamp(rng.gauss(0.65 - 0.25 * onboarding_friction, 0.18), 0.05, 1.0)
            price_sensitivity = clamp(rng.gauss(0.55 - 0.25 * pricing_fairness, 0.18), 0.05, 1.0)
            ind_liquidity = clamp(rng.gauss(local_liquidity, 0.14), 0.05, 1.0)

            individuals.append(
                {
                    "persona_id": f"{cid}_{counter:05d}",
                    "cohort_id": cid,
                    "cohort_name": alloc["name"],
                    "role": alloc["role"],
                    "is_b2b_buyer": is_buyer,
                    "ind_value": ind_value,
                    "ind_trust": ind_trust,
                    "onboarding_friction": onboarding_friction,
                    "regulatory_risk": regulatory_risk,
                    "pricing_fairness": pricing_fairness,
                    "liquidity_dep": liquidity_dep,
                    "ind_liquidity": ind_liquidity,
                    "privacy_sensitivity": privacy_sensitivity,
                    "patience": patience,
                    "price_sensitivity": price_sensitivity,
                    "susceptibility": susceptibility,
                    "voice_weight": voice_weight,
                    "pro_fit": pro_fit,
                    "skeptic_bias": skeptic_bias,
                }
            )
    return individuals


def simulate_single_run(
    spec: dict[str, Any],
    sizing_plan: dict[str, Any],
    seed: int,
) -> dict[str, Any]:
    rng = random.Random(seed)
    cohorts = spec["cohorts"]
    allocations = sizing_plan["cohort_allocations"]
    individuals = _spawn_individuals(cohorts, allocations, rng)

    cohort_ids = [a["id"] for a in allocations]
    r1_by_cohort: dict[str, list[float]] = {cid: [] for cid in cohort_ids}
    friction_reasons: dict[str, int] = {}

    # --- ROUND 1: Discovery, Onboarding & Policy Gates ---
    r1_records = []
    global_reg_exposures = 0

    for p in individuals:
        # Onboarding stall check
        friction_hit = p["onboarding_friction"] * (1.25 - 0.65 * p["patience"])
        reg_hit = p["regulatory_risk"] * (0.7 + 0.8 * p["privacy_sensitivity"])
        pricing_effect = 0.22 * p["pricing_fairness"]

        r1_sent = clamp(
            0.46 * p["ind_value"]
            + 0.36 * p["ind_trust"]
            + pricing_effect
            - 0.65 * friction_hit
            - 0.72 * reg_hit
            - 0.25 * p["skeptic_bias"]
            + rng.gauss(0.0, 0.06),
            -1.0,
            1.0,
        )

        # Primary friction categorization
        if reg_hit > 0.35 and reg_hit >= friction_hit:
            reason = "regulatory_or_privacy_barrier"
            global_reg_exposures += 1
        elif friction_hit > 0.32:
            reason = "onboarding_or_verification_friction"
        elif p["pricing_fairness"] < -0.1:
            reason = "pricing_limits_or_pay_to_rank"
        elif p["ind_liquidity"] < 0.48 and p["liquidity_dep"] > 0.45:
            reason = "regional_cold_start_liquidity"
        else:
            reason = "minor_or_phase2_backlog"
        friction_reasons[reason] = friction_reasons.get(reason, 0) + 1

        if r1_sent >= 0.42:
            intent = "sign_up_immediately"
        elif r1_sent >= 0.05:
            intent = "curious_cautious"
        elif r1_sent >= -0.35:
            intent = "skeptical_observer"
        else:
            intent = "reject_immediately"

        r1_by_cohort[p["cohort_id"]].append(r1_sent)
        r1_records.append({**p, "r1_sent": r1_sent, "r1_intent": intent, "top_friction": reason})

    # Compute weighted social discourse signal for Round 2
    weighted_pos = 0.0
    weighted_neg = 0.0
    total_voice = 0.0
    for rec in r1_records:
        w = rec["voice_weight"]
        total_voice += w
        if rec["r1_sent"] >= 0:
            weighted_pos += w * rec["r1_sent"]
        else:
            weighted_neg += w * abs(rec["r1_sent"])

    pos_signal = weighted_pos / max(total_voice, 1.0)
    neg_signal = weighted_neg / max(total_voice, 1.0)
    reg_defect_rate = global_reg_exposures / max(len(individuals), 1)
    # Negativity bias amplifies unresolved systemic/regulatory complaints
    net_social_field = pos_signal * 0.85 - neg_signal * (1.35 + 0.8 * reg_defect_rate)

    cohort_r1_mean = {cid: statistics.fmean(vals) for cid, vals in r1_by_cohort.items()}

    # --- ROUND 2: Cross-Persona Social Contagion ---
    r2_records = []
    r2_by_cohort: dict[str, list[float]] = {cid: [] for cid in cohort_ids}
    for rec in r1_records:
        peer_delta = (cohort_r1_mean[rec["cohort_id"]] - rec["r1_sent"]) * 0.18
        social_shift = rec["susceptibility"] * (peer_delta + 0.42 * net_social_field)
        r2_sent = clamp(
            rec["r1_sent"] + social_shift + rng.gauss(0.0, 0.045),
            -1.0,
            1.0,
        )
        r2_by_cohort[rec["cohort_id"]].append(r2_sent)
        r2_records.append({**rec, "r2_sent": r2_sent})

    # --- ROUND 3: Week-2 Market Liquidity, Pricing & Equilibrium ---
    outcomes: dict[str, int] = {
        "vocal_advocate": 0,
        "active_user": 0,
        "stalled_in_onboarding": 0,
        "churned_low_liquidity": 0,
        "rejected_distrust": 0,
    }
    paying: dict[str, int] = {
        "yes_pro": 0,
        "yes_basic": 0,
        "no_free_user_only": 0,
        "never": 0,
    }
    cohort_stats_acc: dict[str, dict[str, Any]] = {
        cid: {
            "r1": [],
            "r2": [],
            "r3": [],
            "outcomes": {},
            "paying": {},
            "is_b2b_buyer": False,
        }
        for cid in cohort_ids
    }

    r3_records = []
    b2b_total = 0
    b2b_paid = 0

    for rec in r2_records:
        # Experienced match quality vs regional expectation
        liquidity_gap = max(0.0, 0.62 - rec["ind_liquidity"]) * rec["liquidity_dep"]
        liquidity_bonus = max(0.0, rec["ind_liquidity"] - 0.62) * 0.24
        fairness_bonus = 0.14 * rec["pricing_fairness"]

        r3_sent = clamp(
            0.78 * rec["r2_sent"]
            + 0.22 * rec["ind_value"]
            + liquidity_bonus
            + fairness_bonus
            - 0.85 * liquidity_gap
            + rng.gauss(0.0, 0.05),
            -1.0,
            1.0,
        )

        # Determine Day-14 final outcome
        hard_stall_prob = clamp(
            0.65 * rec["onboarding_friction"] * (1.1 - rec["patience"])
            + 0.35 * rec["regulatory_risk"],
            0.0,
            0.95,
        )
        cold_start_churn_prob = clamp(liquidity_gap * 2.1, 0.0, 0.85)
        if r3_sent < -0.20 or (rec["regulatory_risk"] * rec["privacy_sensitivity"] > 0.50 and r3_sent < 0.12):
            outcome = "rejected_distrust"
        elif hard_stall_prob > 0.34 and r3_sent < 0.28 and rng.random() < hard_stall_prob:
            outcome = "stalled_in_onboarding"
        elif cold_start_churn_prob > 0.12 and r3_sent < 0.45 and rng.random() < cold_start_churn_prob:
            outcome = "churned_low_liquidity"
        elif r3_sent >= 0.72 and rng.random() < 0.26:
            outcome = "vocal_advocate"
        elif r3_sent >= 0.06:
            outcome = "active_user"
        elif cold_start_churn_prob > 0.05:
            outcome = "churned_low_liquidity"
        else:
            outcome = "stalled_in_onboarding"

        # Determine willingness to pay (realistic B2B SaaS adoption hurdle)
        if outcome in ("rejected_distrust", "stalled_in_onboarding") and r3_sent < 0.0:
            pay_choice = "never" if outcome == "rejected_distrust" else "no_free_user_only"
        elif not rec["is_b2b_buyer"]:
            pay_choice = "never" if outcome == "rejected_distrust" else "no_free_user_only"
        else:
            b2b_total += 1
            budget_readiness = rng.uniform(0.0, 1.0)
            utility = (
                0.42 * (r3_sent + 1.0) / 2.0
                + 0.28 * clamp((rec["pricing_fairness"] + 1.0) / 2.0, 0.0, 1.0)
                + 0.20 * rec["ind_liquidity"]
                - 0.28 * rec["price_sensitivity"]
            )
            if outcome in ("active_user", "vocal_advocate") and utility >= 0.52 and rec["pro_fit"] >= 0.52 and budget_readiness >= 0.42:
                pay_choice = "yes_pro"
                b2b_paid += 1
            elif outcome in ("active_user", "vocal_advocate") and utility >= 0.40 and budget_readiness >= 0.25:
                pay_choice = "yes_basic"
                b2b_paid += 1
            elif outcome == "rejected_distrust":
                pay_choice = "never"
            else:
                pay_choice = "no_free_user_only"

        outcomes[outcome] += 1
        paying[pay_choice] += 1

        c_acc = cohort_stats_acc[rec["cohort_id"]]
        c_acc["is_b2b_buyer"] = rec["is_b2b_buyer"]
        c_acc["r1"].append(rec["r1_sent"])
        c_acc["r2"].append(rec["r2_sent"])
        c_acc["r3"].append(r3_sent)
        c_acc["outcomes"][outcome] = c_acc["outcomes"].get(outcome, 0) + 1
        c_acc["paying"][pay_choice] = c_acc["paying"].get(pay_choice, 0) + 1

        r3_records.append({**rec, "r3_sent": r3_sent, "outcome": outcome, "would_pay": pay_choice})

    total_n = len(r3_records)
    avg_r1 = statistics.fmean(r["r1_sent"] for r in r3_records)
    avg_r2 = statistics.fmean(r["r2_sent"] for r in r3_records)
    avg_r3 = statistics.fmean(r["r3_sent"] for r in r3_records)

    active_share = (outcomes["active_user"] + outcomes["vocal_advocate"]) / total_n
    reject_stall_share = (outcomes["rejected_distrust"] + outcomes["stalled_in_onboarding"]) / total_n
    distrust_share = outcomes["rejected_distrust"] / total_n
    b2b_conv_rate = (b2b_paid / b2b_total) if b2b_total > 0 else active_share

    # Transparent weighted readiness score (0-100): 65%+ Day-14 B2B paid rate hits full B2B sub-score
    norm_sentiment = clamp((avg_r3 + 1.0) / 2.0, 0.0, 1.0)
    b2b_subscore = clamp(b2b_conv_rate / 0.65, 0.0, 1.0) if b2b_total > 0 else active_share
    raw_score = 100.0 * (
        0.40 * norm_sentiment
        + 0.25 * active_share
        + 0.20 * b2b_subscore
        + 0.15 * clamp(1.0 - reject_stall_share, 0.0, 1.0)
    )
    if distrust_share > 0.15:
        raw_score = min(raw_score, 45.0)
    readiness_score = round(clamp(raw_score, 0.0, 100.0), 1)

    cohort_breakdown = []
    for alloc in allocations:
        cid = alloc["id"]
        acc = cohort_stats_acc[cid]
        cohort_breakdown.append(
            {
                "id": cid,
                "name": alloc["name"],
                "role": alloc["role"],
                "is_b2b_buyer": acc["is_b2b_buyer"],
                "personas": len(acc["r3"]),
                "avg_r1": round(statistics.fmean(acc["r1"]), 3),
                "avg_r2": round(statistics.fmean(acc["r2"]), 3),
                "avg_r3": round(statistics.fmean(acc["r3"]), 3),
                "outcomes": acc["outcomes"],
                "paying": acc["paying"],
            }
        )

    # Stratified sample across cohorts (up to 48 representative virtual personas)
    sample_records = []
    per_cohort_sample = max(2, 48 // max(len(allocations), 1))
    by_cid: dict[str, list[dict[str, Any]]] = {cid: [] for cid in cohort_ids}
    for rec in r3_records:
        by_cid[rec["cohort_id"]].append(rec)
    for cid in cohort_ids:
        sorted_c = sorted(by_cid[cid], key=lambda x: x["r3_sent"])
        picks = [sorted_c[0], sorted_c[len(sorted_c) // 2], sorted_c[-1]] if len(sorted_c) >= 3 else sorted_c
        for item in picks[:per_cohort_sample]:
            sample_records.append(
                {
                    "persona_id": item["persona_id"],
                    "cohort_id": item["cohort_id"],
                    "role": item["role"],
                    "r1_sentiment": round(item["r1_sent"], 3),
                    "r2_sentiment": round(item["r2_sent"], 3),
                    "r3_sentiment": round(item["r3_sent"], 3),
                    "r1_intent": item["r1_intent"],
                    "top_friction": item["top_friction"],
                    "outcome": item["outcome"],
                    "would_pay": item["would_pay"],
                }
            )

    return {
        "seed": seed,
        "total_population": total_n,
        "avg_r1": avg_r1,
        "avg_r2": avg_r2,
        "avg_r3": avg_r3,
        "readiness_score": readiness_score,
        "active_retention_rate": round(active_share, 4),
        "b2b_buyer_count": b2b_total,
        "b2b_paying_count": b2b_paid,
        "b2b_conversion_rate": round(b2b_conv_rate, 4) if b2b_total > 0 else None,
        "outcomes": outcomes,
        "paying": paying,
        "friction_reasons": friction_reasons,
        "cohort_breakdown": cohort_breakdown,
        "personas_sample": sample_records,
    }


def run_simulation(
    spec: dict[str, Any],
    *,
    population_override: int | None = None,
    max_population: int = DEFAULT_MAX_POPULATION,
    seed: int = 42,
    runs: int = 3,
) -> dict[str, Any]:
    validate_spec(spec)
    if runs < 1:
        raise ValueError("runs must be >= 1")

    sizing_plan = compute_sizing_plan(
        spec,
        population_override=population_override,
        max_population=max_population,
    )
    if sizing_plan["recommended_population"] < MIN_TOTAL_POPULATION:
        raise ValueError(f"Population must be >= {MIN_TOTAL_POPULATION}")

    run_outputs = [simulate_single_run(spec, sizing_plan, seed + i) for i in range(runs)]
    scores = [r["readiness_score"] for r in run_outputs]
    r3_vals = [r["avg_r3"] for r in run_outputs]

    mean_score = round(statistics.fmean(scores), 1)
    std_score = round(statistics.stdev(scores), 2) if runs > 1 else 0.0
    ci95_half_score = round(1.96 * std_score / math.sqrt(runs), 2) if runs > 1 else 0.0

    mean_r3 = round(statistics.fmean(r3_vals), 3)
    mean_r1 = round(statistics.fmean(r["avg_r1"] for r in run_outputs), 3)
    mean_r2 = round(statistics.fmean(r["avg_r2"] for r in run_outputs), 3)

    if mean_score >= 78.0 and run_outputs[0]["outcomes"]["rejected_distrust"] / sizing_plan["recommended_population"] <= 0.08:
        verdict = "GO (Conditional or Phase-1 Launch Ready)"
    elif mean_score >= 58.0:
        verdict = "CONDITIONAL HOLD (Remediate Top Frictions Before Launch)"
    else:
        verdict = "NO-GO (Critical Blockers Trigger Rejection Spiral)"

    primary = run_outputs[0]
    metrics = {
        "project_name": spec.get("project_name", "Unnamed Project"),
        "simulation_disclaimer": (
            "Synthetic scenario-sensitivity simulation derived from grounded project "
            "assumptions and calibrated cohorts; not empirical live-user telemetry."
        ),
        "sizing_plan": sizing_plan,
        "monte_carlo": {
            "runs": runs,
            "base_seed": seed,
            "mean_readiness_score": mean_score,
            "score_ci95_half_width": ci95_half_score,
            "mean_avg_r1": mean_r1,
            "mean_avg_r2": mean_r2,
            "mean_avg_r3": mean_r3,
            "verdict": verdict,
        },
        "primary_run_summary": {
            "seed": primary["seed"],
            "total_population": primary["total_population"],
            "avg_sentiment_r1": round(primary["avg_r1"], 3),
            "avg_sentiment_r2": round(primary["avg_r2"], 3),
            "avg_sentiment_r3": round(primary["avg_r3"], 3),
            "readiness_score": primary["readiness_score"],
            "active_retention_rate": primary["active_retention_rate"],
            "b2b_buyer_count": primary["b2b_buyer_count"],
            "b2b_paying_count": primary["b2b_paying_count"],
            "b2b_conversion_rate": primary["b2b_conversion_rate"],
            "outcomes": primary["outcomes"],
            "paying": primary["paying"],
            "friction_reasons": primary["friction_reasons"],
        },
        "cohort_breakdown": primary["cohort_breakdown"],
        "personas_sample": primary["personas_sample"],
    }
    return metrics


def write_outputs(metrics: dict[str, Any], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "sizing_plan.json").write_text(
        json.dumps(metrics["sizing_plan"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out_dir / "personas_sample.json").write_text(
        json.dumps(metrics["personas_sample"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    clean_metrics = {k: v for k, v in metrics.items() if k != "personas_sample"}
    (out_dir / "metrics.json").write_text(
        json.dumps(clean_metrics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    csv_path = out_dir / "cohorts_summary.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "cohort_id",
                "name",
                "role",
                "is_b2b_buyer",
                "personas",
                "avg_r1",
                "avg_r2",
                "avg_r3",
                "vocal_advocate",
                "active_user",
                "stalled_in_onboarding",
                "churned_low_liquidity",
                "rejected_distrust",
                "yes_pro",
                "yes_basic",
            ]
        )
        for c in metrics["cohort_breakdown"]:
            o = c["outcomes"]
            pay = c["paying"]
            writer.writerow(
                [
                    c["id"],
                    c["name"],
                    c["role"],
                    c["is_b2b_buyer"],
                    c["personas"],
                    c["avg_r1"],
                    c["avg_r2"],
                    c["avg_r3"],
                    o.get("vocal_advocate", 0),
                    o.get("active_user", 0),
                    o.get("stalled_in_onboarding", 0),
                    o.get("churned_low_liquidity", 0),
                    o.get("rejected_distrust", 0),
                    pay.get("yes_pro", 0),
                    pay.get("yes_basic", 0),
                ]
            )

    mc = metrics["monte_carlo"]
    prim = metrics["primary_run_summary"]
    lines = [
        f"# Simulation Report: {metrics['project_name']}",
        "",
        f"> **Disclaimer:** {metrics['simulation_disclaimer']}",
        "",
        "## Executive Verdict",
        f"- **Verdict:** `{mc['verdict']}`",
        f"- **Readiness Score:** `{mc['mean_readiness_score']} / 100` (±{mc['score_ci95_half_width']} 95% CI across {mc['runs']} Monte Carlo runs)",
        f"- **Adaptive Swarm Size:** `{prim['total_population']:,}` virtual personas (`{metrics['sizing_plan']['complexity_tier']}` tier, floor `{MIN_TOTAL_POPULATION:,}`)",
        f"- **Sentiment Trajectory:** R1 `{mc['mean_avg_r1']:+.3f}` -> R2 `{mc['mean_avg_r2']:+.3f}` -> R3 `{mc['mean_avg_r3']:+.3f}`",
        f"- **Active / Advocate Retention:** `{prim['active_retention_rate'] * 100:.1f}%`",
        f"- **B2B Paid Conversion (among B2B cohorts):** `{prim['b2b_paying_count']}/{prim['b2b_buyer_count']}` (`{(prim['b2b_conversion_rate'] or 0) * 100:.1f}%`)",
        "",
        "## Cohort Breakdown (Primary Run)",
        "| Cohort | Personas | R1 | R2 | R3 | Active+Advocate | Pro | Basic |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for c in metrics["cohort_breakdown"]:
        act = c["outcomes"].get("active_user", 0) + c["outcomes"].get("vocal_advocate", 0)
        lines.append(
            f"| {c['name']} | {c['personas']} | {c['avg_r1']:+.3f} | {c['avg_r2']:+.3f} | {c['avg_r3']:+.3f} | "
            f"{act} | {c['paying'].get('yes_pro', 0)} | {c['paying'].get('yes_basic', 0)} |"
        )
    lines.extend(["", "## Primary Friction Signals"])
    for reason, count in sorted(prim["friction_reasons"].items(), key=lambda kv: -kv[1]):
        lines.append(f"- `{reason}`: {count} personas")

    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run adaptive >=1,000 virtual persona crowd simulation for a project spec."
    )
    parser.add_argument("--spec", required=True, help="Path to project spec JSON.")
    parser.add_argument("--out-dir", default="sim_output", help="Directory to save simulation outputs.")
    parser.add_argument("--population", type=int, help="Optional override (must be >= 1000).")
    parser.add_argument(
        "--max-population",
        type=int,
        default=DEFAULT_MAX_POPULATION,
        help=f"Upper safety cap (default {DEFAULT_MAX_POPULATION}).",
    )
    parser.add_argument("--seed", type=int, default=42, help="Base deterministic RNG seed.")
    parser.add_argument("--runs", type=int, default=3, help="Number of Monte Carlo runs (>= 1).")
    args = parser.parse_args(argv)

    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"Error: spec file not found: {spec_path}", file=sys.stderr)
        return 1

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    metrics = run_simulation(
        spec,
        population_override=args.population,
        max_population=args.max_population,
        seed=args.seed,
        runs=args.runs,
    )
    out_dir = Path(args.out_dir)
    write_outputs(metrics, out_dir)
    summary = {
        "project_name": metrics["project_name"],
        "recommended_population": metrics["sizing_plan"]["recommended_population"],
        "complexity_tier": metrics["sizing_plan"]["complexity_tier"],
        "monte_carlo": metrics["monte_carlo"],
        "out_dir": str(out_dir),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
