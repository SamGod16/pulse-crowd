#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from size_swarm import MIN_TOTAL_POPULATION, compute_sizing_plan  # noqa: E402
from simulate_crowd import run_simulation, write_outputs  # noqa: E402
from scaffold_spec import VALID_BUSINESS_TYPES, build_spec  # noqa: E402
from validate_skill import validate_repo  # noqa: E402


class PulseCrowdSimTests(unittest.TestCase):
    def setUp(self) -> None:
        self.minimal_spec = json.loads(
            (ROOT / "examples" / "minimal-b2b-cli.json").read_text(encoding="utf-8")
        )
        self.complex_spec = json.loads(
            (ROOT / "examples" / "regulated-marketplace.json").read_text(encoding="utf-8")
        )
        self.dropship_spec = json.loads(
            (ROOT / "examples" / "dropshipping-store.json").read_text(encoding="utf-8")
        )
        self.dtc_spec = json.loads(
            (ROOT / "examples" / "ecommerce-dtc-brand.json").read_text(encoding="utf-8")
        )

    def test_minimum_floor_enforced(self) -> None:
        plan = compute_sizing_plan(self.minimal_spec)
        self.assertGreaterEqual(plan["recommended_population"], MIN_TOTAL_POPULATION)

        with self.assertRaises(ValueError):
            compute_sizing_plan(self.minimal_spec, population_override=12)

    def test_adaptive_sizing_scales_with_complexity(self) -> None:
        minimal_plan = compute_sizing_plan(self.minimal_spec)
        complex_plan = compute_sizing_plan(self.complex_spec)

        self.assertLess(
            minimal_plan["recommended_population"],
            complex_plan["recommended_population"],
        )
        self.assertEqual(
            sum(c["allocated_personas"] for c in minimal_plan["cohort_allocations"]),
            minimal_plan["recommended_population"],
        )
        self.assertEqual(
            sum(c["allocated_personas"] for c in complex_plan["cohort_allocations"]),
            complex_plan["recommended_population"],
        )

    def test_simulation_generates_at_least_1000_personas_deterministically(self) -> None:
        res_a = run_simulation(self.minimal_spec, seed=100, runs=3)
        res_b = run_simulation(self.minimal_spec, seed=100, runs=3)

        self.assertEqual(res_a["monte_carlo"], res_b["monte_carlo"])
        self.assertGreaterEqual(res_a["primary_run_summary"]["total_population"], 1000)
        cohort_sum = sum(c["personas"] for c in res_a["cohort_breakdown"])
        self.assertEqual(cohort_sum, res_a["primary_run_summary"]["total_population"])

    def test_v1_specs_preserve_exact_baseline_without_ux_journey(self) -> None:
        min_res = run_simulation(self.minimal_spec, seed=42, runs=3)
        reg_res = run_simulation(self.complex_spec, seed=42, runs=3)

        self.assertEqual(min_res["sizing_plan"]["recommended_population"], 1500)
        self.assertEqual(min_res["monte_carlo"]["mean_readiness_score"], 90.0)
        self.assertNotIn("ux_funnel", min_res)
        self.assertNotIn("commerce_kpis", min_res)

        self.assertEqual(reg_res["sizing_plan"]["recommended_population"], 6750)
        self.assertEqual(reg_res["monte_carlo"]["mean_readiness_score"], 92.3)
        self.assertNotIn("ux_funnel", reg_res)

    def test_simulation_sensitivity_to_defects(self) -> None:
        broken_spec = json.loads(json.dumps(self.complex_spec))
        for cohort in broken_spec["cohorts"]:
            cohort["onboarding_friction"] = 0.72
            cohort["regulatory_blocker_risk"] = 0.78
            cohort["pricing_fairness"] = -0.65

        healthy_res = run_simulation(self.complex_spec, seed=42, runs=2)
        broken_res = run_simulation(broken_spec, seed=42, runs=2)

        self.assertGreater(
            healthy_res["monte_carlo"]["mean_readiness_score"],
            broken_res["monte_carlo"]["mean_readiness_score"] + 25.0,
        )
        self.assertEqual(
            broken_res["monte_carlo"]["verdict"],
            "NO-GO (Critical Blockers Trigger Rejection Spiral)",
        )

    def test_ux_journey_identifies_stuck_distracted_lost_bottlenecks(self) -> None:
        spec = json.loads(json.dumps(self.minimal_spec))
        spec["ux_journey"] = [
            {
                "id": "landing",
                "name": "Landing Page",
                "component_or_route": "src/app/page.tsx",
                "step_friction": 0.05,
                "distraction_load": 0.05,
                "confusion_risk": 0.05,
                "trust_gap": 0.02,
            },
            {
                "id": "cluttered_onboarding",
                "name": "Mandatory Form & Popup Clutter",
                "component_or_route": "src/app/onboarding/page.tsx",
                "step_friction": 0.85,
                "distraction_load": 0.70,
                "confusion_risk": 0.40,
                "trust_gap": 0.15,
            },
            {
                "id": "workspace",
                "name": "First Project Setup",
                "component_or_route": "src/app/workspace/page.tsx",
                "step_friction": 0.10,
                "distraction_load": 0.10,
                "confusion_risk": 0.10,
                "trust_gap": 0.05,
            },
        ]

        res = run_simulation(spec, seed=42, runs=2)
        self.assertIn("ux_funnel", res)
        ux = res["ux_funnel"]
        self.assertEqual(ux["total_entered"], res["primary_run_summary"]["total_population"])
        self.assertEqual(ux["biggest_bottleneck"]["id"], "cluttered_onboarding")
        self.assertEqual(ux["biggest_bottleneck"]["component_or_route"], "src/app/onboarding/page.tsx")
        self.assertGreater(ux["drop_breakdown"]["stuck"], 100)
        self.assertGreater(ux["drop_breakdown"]["distracted"], 50)

        for step in ux["steps"]:
            self.assertEqual(step["entered"], step["completed"] + step["dropped"])
            self.assertEqual(step["dropped"], sum(step["drop_reasons"].values()))

    def test_ecommerce_and_dropshipping_unit_economics(self) -> None:
        drop_res = run_simulation(self.dropship_spec, seed=42, runs=3)
        dtc_res = run_simulation(self.dtc_spec, seed=42, runs=3)

        self.assertIn("commerce_kpis", drop_res)
        self.assertIn("commerce_kpis", dtc_res)
        self.assertGreater(
            dtc_res["monte_carlo"]["mean_readiness_score"],
            drop_res["monte_carlo"]["mean_readiness_score"] + 40.0,
        )
        self.assertGreater(
            dtc_res["commerce_kpis"]["simulated_conversion_rate"],
            drop_res["commerce_kpis"]["simulated_conversion_rate"] * 3.0,
        )
        self.assertFalse(drop_res["commerce_kpis"]["profitable_at_assumed_cpc"])
        self.assertTrue(dtc_res["commerce_kpis"]["profitable_at_assumed_cpc"])
        self.assertEqual(drop_res["ux_funnel"]["biggest_bottleneck"]["id"], "shipping_shock_checkout")

    def test_invalid_ux_journey_rejected(self) -> None:
        bad_spec = json.loads(json.dumps(self.minimal_spec))
        bad_spec["ux_journey"] = [{"id": "only_one", "name": "Single Step"}]
        with self.assertRaises(ValueError):
            run_simulation(bad_spec, seed=42, runs=1)

    def test_scaffold_spec_covers_all_business_audiences(self) -> None:
        for btype in VALID_BUSINESS_TYPES:
            spec = build_spec(
                btype,
                project_name=f"Test {btype}",
                stage="concept",
                hidden_shipping=(btype == "dropshipping"),
                forced_signup_early=(btype == "future_app"),
            )
            res = run_simulation(spec, seed=42, runs=1)
            self.assertGreaterEqual(res["primary_run_summary"]["total_population"], MIN_TOTAL_POPULATION)
            self.assertIn("ux_funnel", res)

        web_ex = json.loads((ROOT / "examples" / "website-lead-funnel.json").read_text(encoding="utf-8"))
        web_res = run_simulation(web_ex, seed=42, runs=2)
        self.assertEqual(web_res["sizing_plan"]["sizing_factors"]["product_type"], "website_funnel")
        self.assertIn("ux_funnel", web_res)

    def test_write_outputs_and_cli_execution(self) -> None:
        metrics = run_simulation(self.dropship_spec, seed=7, runs=2)
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir) / "sim"
            write_outputs(metrics, out_dir)
            for name in ("sizing_plan.json", "metrics.json", "personas_sample.json", "cohorts_summary.csv", "report.md"):
                self.assertTrue((out_dir / name).exists(), f"Missing output file {name}")

            report_text = (out_dir / "report.md").read_text(encoding="utf-8")
            self.assertIn("In-App UX Journey Funnel", report_text)
            self.assertIn("E-Commerce & Dropshipping Unit Economics Sensitivity", report_text)

            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "size_swarm.py"),
                    "--spec",
                    str(ROOT / "examples" / "regulated-marketplace.json"),
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            cli_plan = json.loads(proc.stdout)
            self.assertGreaterEqual(cli_plan["recommended_population"], 1000)

    def test_skill_validator_clean(self) -> None:
        errors = validate_repo(ROOT)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
