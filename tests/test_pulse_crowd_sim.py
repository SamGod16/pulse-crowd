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
from validate_skill import validate_repo  # noqa: E402


class PulseCrowdSimTests(unittest.TestCase):
    def setUp(self) -> None:
        self.minimal_spec = json.loads(
            (ROOT / "examples" / "minimal-b2b-cli.json").read_text(encoding="utf-8")
        )
        self.complex_spec = json.loads(
            (ROOT / "examples" / "regulated-marketplace.json").read_text(encoding="utf-8")
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

    def test_write_outputs_and_cli_execution(self) -> None:
        metrics = run_simulation(self.minimal_spec, seed=7, runs=2)
        with tempfile.TemporaryDirectory() as tmpdir:
            out_dir = Path(tmpdir) / "sim"
            write_outputs(metrics, out_dir)
            for name in ("sizing_plan.json", "metrics.json", "personas_sample.json", "cohorts_summary.csv", "report.md"):
                self.assertTrue((out_dir / name).exists(), f"Missing output file {name}")

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
