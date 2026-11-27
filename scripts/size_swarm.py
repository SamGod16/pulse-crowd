#!/usr/bin/env python3
"""
Adaptive Swarm Sizing Engine for pulse-crowd.

Determines the appropriate virtual persona population (always >= 1,000) based on
project complexity drivers (segments, product model, geography, pricing tiers,
regulatory risk, lifecycle stage, UX journey depth, and evaluation depth) BEFORE
launching any virtual crowd simulation.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

MIN_TOTAL_POPULATION = 1000
DEFAULT_MAX_POPULATION = 25000

PRODUCT_TYPE_WEIGHTS = {
    "developer_tool": 100,
    "website_funnel": 150,
    "b2b_saas": 200,
    "b2c_consumer": 300,
    "mobile_app": 350,
    "community_network": 450,
    "ecommerce_brand": 500,
    "dropshipping_store": 600,
    "two_sided_marketplace": 650,
    "regulated_platform": 850,
    "custom_project": 300,
}

GEOGRAPHIC_SCOPE_WEIGHTS = {
    "single_city": 0,
    "regional": 500,
    "national": 1300,
    "multi_country": 2600,
}

REGULATORY_RISK_WEIGHTS = {
    "low": 0,
    "medium": 400,
    "high": 1050,
}

LIFECYCLE_MULTIPLIERS = {
    "concept": 0.85,
    "mvp": 1.0,
    "pre_launch": 1.25,
    "growth_scale": 1.55,
}

DEPTH_MULTIPLIERS = {
    "standard": 1.0,
    "thorough": 1.35,
    "stress_test": 1.85,
}


def compute_sizing_plan(
    project: dict[str, Any],
    *,
    population_override: int | None = None,
    max_population: int = DEFAULT_MAX_POPULATION,
) -> dict[str, Any]:
    """Compute an adaptive virtual population sizing plan >= 1,000."""
    project_name = str(project.get("project_name") or "Unnamed Project")
    product_type = str(project.get("product_type", "b2b_saas"))
    lifecycle_stage = str(project.get("lifecycle_stage", "mvp"))
    geographic_scope = str(project.get("geographic_scope", "regional"))
    regulatory_risk = str(project.get("regulatory_risk", "medium"))
    evaluation_depth = str(project.get("evaluation_depth", "standard"))

    if product_type not in PRODUCT_TYPE_WEIGHTS:
        raise ValueError(f"Unsupported product_type: {product_type}")
    if geographic_scope not in GEOGRAPHIC_SCOPE_WEIGHTS:
        raise ValueError(f"Unsupported geographic_scope: {geographic_scope}")
    if regulatory_risk not in REGULATORY_RISK_WEIGHTS:
        raise ValueError(f"Unsupported regulatory_risk: {regulatory_risk}")
    if lifecycle_stage not in LIFECYCLE_MULTIPLIERS:
        raise ValueError(f"Unsupported lifecycle_stage: {lifecycle_stage}")
    if evaluation_depth not in DEPTH_MULTIPLIERS:
        raise ValueError(f"Unsupported evaluation_depth: {evaluation_depth}")

    cohorts = project.get("cohorts") or []
    ux_journey = project.get("ux_journey") or []
    target_segments = int(project.get("target_segments") or max(len(cohorts), 2))
    pricing_tiers = int(project.get("pricing_tiers", 2))
    acquisition_channels = int(project.get("acquisition_channels", 2))

    if target_segments < 1:
        raise ValueError("target_segments must be >= 1")
    if pricing_tiers < 0:
        raise ValueError("pricing_tiers must be >= 0")
    if acquisition_channels < 1:
        raise ValueError("acquisition_channels must be >= 1")

    segment_component = max(0, target_segments - 2) * 220
    pricing_component = pricing_tiers * 150
    channel_component = max(0, acquisition_channels - 1) * 140
    journey_component = max(0, len(ux_journey) - 4) * 90

    if population_override is not None:
        if population_override < MIN_TOTAL_POPULATION:
            raise ValueError(
                f"population_override ({population_override}) cannot be below the minimum floor of {MIN_TOTAL_POPULATION}."
            )
        recommended_population = min(int(population_override), max_population)
        raw_estimate = recommended_population
    else:
        additive_score = (
            MIN_TOTAL_POPULATION
            + PRODUCT_TYPE_WEIGHTS[product_type]
            + GEOGRAPHIC_SCOPE_WEIGHTS[geographic_scope]
            + REGULATORY_RISK_WEIGHTS[regulatory_risk]
            + segment_component
            + pricing_component
            + channel_component
            + journey_component
        )
        raw_estimate = int(
            round(
                additive_score
                * LIFECYCLE_MULTIPLIERS[lifecycle_stage]
                * DEPTH_MULTIPLIERS[evaluation_depth]
            )
        )
        # Round up cleanly to nearest 50 and enforce hard >= 1,000 floor.
        rounded = int(math.ceil(raw_estimate / 50.0) * 50)
        recommended_population = max(MIN_TOTAL_POPULATION, min(rounded, max_population))

    if recommended_population <= 1600:
        complexity_tier = "lean_1k"
    elif recommended_population <= 4000:
        complexity_tier = "moderate_2k_4k"
    elif recommended_population <= 8000:
        complexity_tier = "complex_4k_8k"
    else:
        complexity_tier = "enterprise_8k_plus"

    allocated_cohorts = allocate_cohorts(cohorts, recommended_population) if cohorts else []

    return {
        "project_name": project_name,
        "minimum_population_floor": MIN_TOTAL_POPULATION,
        "recommended_population": recommended_population,
        "complexity_tier": complexity_tier,
        "sizing_factors": {
            "product_type": product_type,
            "product_weight": PRODUCT_TYPE_WEIGHTS[product_type],
            "geographic_scope": geographic_scope,
            "geography_weight": GEOGRAPHIC_SCOPE_WEIGHTS[geographic_scope],
            "regulatory_risk": regulatory_risk,
            "regulatory_weight": REGULATORY_RISK_WEIGHTS[regulatory_risk],
            "target_segments": target_segments,
            "segment_weight": segment_component,
            "pricing_tiers": pricing_tiers,
            "pricing_weight": pricing_component,
            "acquisition_channels": acquisition_channels,
            "channel_weight": channel_component,
            "ux_journey_steps": len(ux_journey),
            "journey_weight": journey_component,
            "lifecycle_stage": lifecycle_stage,
            "lifecycle_multiplier": LIFECYCLE_MULTIPLIERS[lifecycle_stage],
            "evaluation_depth": evaluation_depth,
            "depth_multiplier": DEPTH_MULTIPLIERS[evaluation_depth],
            "raw_estimate_before_floor": raw_estimate,
        },
        "cohort_allocations": allocated_cohorts,
    }


def allocate_cohorts(cohorts: list[dict[str, Any]], total_population: int) -> list[dict[str, Any]]:
    """
    Distribute total_population across cohorts proportionally using Largest Remainder
    allocation while guaranteeing every defined cohort receives a usable sample size.
    """
    if not cohorts:
        raise ValueError("cohorts list cannot be empty")
    if total_population < MIN_TOTAL_POPULATION:
        raise ValueError(f"total_population must be >= {MIN_TOTAL_POPULATION}")

    shares = [float(c.get("share", 1.0)) for c in cohorts]
    if any(s <= 0 for s in shares):
        raise ValueError("All cohort share values must be > 0")
    total_share = sum(shares)
    normalized = [s / total_share for s in shares]

    # Ensure each cohort gets at least min_per_cohort (default max(25, 1.5% of total))
    # unless there are so many cohorts that smaller equal floor is needed.
    min_per_cohort = min(max(25, int(total_population * 0.015)), total_population // len(cohorts))
    remaining = total_population - min_per_cohort * len(cohorts)

    exact_extras = [remaining * w for w in normalized]
    floor_extras = [int(math.floor(x)) for x in exact_extras]
    deficit = remaining - sum(floor_extras)

    remainders = sorted(
        [(exact_extras[i] - floor_extras[i], i) for i in range(len(cohorts))],
        reverse=True,
    )
    for _, idx in remainders[:deficit]:
        floor_extras[idx] += 1

    allocations = []
    for i, cohort in enumerate(cohorts):
        count = min_per_cohort + floor_extras[i]
        allocations.append(
            {
                "id": str(cohort["id"]),
                "name": str(cohort.get("name", cohort["id"])),
                "role": str(cohort.get("role", "user")),
                "target_share": round(normalized[i], 4),
                "allocated_personas": count,
            }
        )
    return allocations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Compute adaptive >=1,000 virtual persona swarm size before running a simulation."
    )
    parser.add_argument("--spec", required=True, help="Path to project specification JSON.")
    parser.add_argument("--out", help="Optional path to write sizing_plan.json.")
    parser.add_argument("--population", type=int, help="Optional override (must be >= 1000).")
    parser.add_argument(
        "--max-population",
        type=int,
        default=DEFAULT_MAX_POPULATION,
        help=f"Upper safety cap (default {DEFAULT_MAX_POPULATION}).",
    )
    args = parser.parse_args(argv)

    spec_path = Path(args.spec)
    if not spec_path.exists():
        print(f"Error: spec file not found: {spec_path}", file=sys.stderr)
        return 1

    project = json.loads(spec_path.read_text(encoding="utf-8"))
    plan = compute_sizing_plan(
        project,
        population_override=args.population,
        max_population=args.max_population,
    )
    rendered = json.dumps(plan, ensure_ascii=False, indent=2)
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
