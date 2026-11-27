#!/usr/bin/env python3
"""
Interactive & CLI Business Spec Scaffolder for pulse-crowd.

Helps users or AI coding agents quickly generate a grounded, schema-valid
PulseCrowd specification tailored to their exact business vertical:
  - dropshipping   (Shopify/WooCommerce, paid social ads, shipping windows)
  - ecommerce      (DTC brand, repeat buyers, express checkout)
  - future_app     (Pre-code mobile/web app idea & planned UX journey)
  - future_website (Landing page, waitlist, booking funnel, info-product)
  - b2b_saas       (SaaS / dev-tool pricing tiers, auth & team buyers)
  - marketplace    (Two-sided or regulated platform with liquidity & compliance)

Pure Python 3.9+ standard library (zero external dependencies).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

VALID_BUSINESS_TYPES = (
    "dropshipping",
    "ecommerce",
    "future_app",
    "future_website",
    "b2b_saas",
    "marketplace",
)


def build_spec(
    business_type: str,
    *,
    project_name: str = "My Project",
    stage: str = "concept",
    scope: str = "national",
    regulatory_risk: str = "low",
    aov_usd: float = 49.0,
    margin_pct: float = 65.0,
    estimated_cpc_usd: float = 0.85,
    shipping_days_max: int = 14,
    hidden_shipping: bool = False,
    return_policy_days: int = 14,
    forced_signup_early: bool = False,
    heavy_popups: bool = False,
    pricing_fairness: float = 0.35,
) -> dict[str, Any]:
    """Generate a tailored spec template calibrated for the chosen business audience."""
    if business_type not in VALID_BUSINESS_TYPES:
        raise ValueError(f"Unsupported business_type: {business_type}. Choose from {VALID_BUSINESS_TYPES}.")

    if business_type == "dropshipping":
        shipping_hit = max(0.0, (shipping_days_max - 6) * 0.025)
        trust_gap_base = min(0.85, 0.22 + shipping_hit + (0.14 if return_policy_days < 14 else 0.0))
        distraction_cart = 0.72 if heavy_popups else 0.25
        friction_account = 0.72 if forced_signup_early else 0.16
        surprise_checkout = 0.74 if hidden_shipping else 0.08

        return {
            "project_name": project_name,
            "product_type": "dropshipping_store",
            "lifecycle_stage": stage,
            "geographic_scope": scope,
            "regulatory_risk": regulatory_risk,
            "evaluation_depth": "standard",
            "target_segments": 4,
            "pricing_tiers": 2,
            "acquisition_channels": 3,
            "commerce_profile": {
                "store_model": "dropshipping",
                "aov_usd": round(aov_usd, 2),
                "gross_margin_pct": round(margin_pct, 1),
                "estimated_cpc_usd": round(estimated_cpc_usd, 2),
                "shipping_days_min": max(1, shipping_days_max // 2),
                "shipping_days_max": shipping_days_max,
                "free_shipping_threshold_usd": round(aov_usd * 1.25, 0),
                "hidden_shipping_at_checkout": hidden_shipping,
                "return_policy_days": return_policy_days,
            },
            "ux_journey": [
                {
                    "id": "ad_landing_pdp",
                    "name": "Mobile Ad Landing & Product Page",
                    "component_or_route": "sections/product-hero",
                    "step_friction": 0.12,
                    "distraction_load": 0.55 if heavy_popups else 0.16,
                    "confusion_risk": 0.24,
                    "trust_gap": trust_gap_base,
                    "surprise_cost": 0.0,
                    "value_clarity_gain": 0.20,
                },
                {
                    "id": "cart_drawer",
                    "name": "Cart Drawer & Upsells",
                    "component_or_route": "snippets/cart-drawer",
                    "step_friction": 0.25 if heavy_popups else 0.10,
                    "distraction_load": distraction_cart,
                    "confusion_risk": 0.28 if heavy_popups else 0.12,
                    "trust_gap": trust_gap_base * 0.85,
                    "surprise_cost": 0.08,
                    "value_clarity_gain": 0.08,
                },
                {
                    "id": "account_or_shipping",
                    "name": "Account & Shipping Info Step",
                    "component_or_route": "checkout/contact-shipping",
                    "step_friction": friction_account,
                    "distraction_load": 0.18,
                    "confusion_risk": 0.22,
                    "trust_gap": trust_gap_base * 0.8,
                    "surprise_cost": 0.0,
                    "value_clarity_gain": 0.05,
                },
                {
                    "id": "final_checkout",
                    "name": "Checkout & Final Payment Total",
                    "component_or_route": "checkout/payment",
                    "step_friction": 0.30 if forced_signup_early else 0.14,
                    "distraction_load": 0.15,
                    "confusion_risk": 0.22,
                    "trust_gap": trust_gap_base,
                    "surprise_cost": surprise_checkout,
                    "value_clarity_gain": 0.0,
                },
            ],
            "cohorts": [
                {
                    "id": "impulse_tiktok_shoppers",
                    "name": "Impulse Social Ad Visitors (TikTok / Meta)",
                    "role": "Mobile Impulse Buyer",
                    "share": 0.45,
                    "is_commerce_buyer": True,
                    "value_fit": 0.45,
                    "initial_trust": 0.12,
                    "onboarding_friction": 0.42 if forced_signup_early else 0.18,
                    "regulatory_blocker_risk": 0.05,
                    "pricing_fairness": pricing_fairness,
                    "local_liquidity": 0.85,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.70,
                    "social_voice_weight": 1.1,
                },
                {
                    "id": "price_comparators",
                    "name": "Amazon / AliExpress Price Checkers",
                    "role": "Price-Sensitive Comparator",
                    "share": 0.25,
                    "is_commerce_buyer": True,
                    "value_fit": 0.22,
                    "initial_trust": -0.05,
                    "onboarding_friction": 0.28,
                    "regulatory_blocker_risk": 0.08,
                    "pricing_fairness": pricing_fairness - 0.20,
                    "local_liquidity": 0.80,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.42,
                    "social_voice_weight": 1.4,
                    "skepticism_bias": 0.25,
                },
                {
                    "id": "trust_skeptic_buyers",
                    "name": "Shipping & Return Policy Skeptics",
                    "role": "Trust-Focused Buyer",
                    "share": 0.20,
                    "is_commerce_buyer": True,
                    "value_fit": 0.35,
                    "initial_trust": 0.05 if return_policy_days >= 30 else -0.18,
                    "onboarding_friction": 0.30,
                    "regulatory_blocker_risk": 0.15,
                    "pricing_fairness": pricing_fairness - 0.10,
                    "local_liquidity": 0.75,
                    "liquidity_dependence": 0.08,
                    "social_susceptibility": 0.50,
                    "social_voice_weight": 1.6,
                    "skepticism_bias": 0.24,
                },
                {
                    "id": "ad_comment_critics",
                    "name": "Ad Comment Critics & Scam Watchers",
                    "role": "Social Amplifier",
                    "share": 0.10,
                    "is_commerce_buyer": False,
                    "value_fit": 0.10,
                    "initial_trust": -0.25,
                    "onboarding_friction": 0.22,
                    "regulatory_blocker_risk": 0.18,
                    "pricing_fairness": pricing_fairness - 0.25,
                    "local_liquidity": 0.75,
                    "liquidity_dependence": 0.0,
                    "social_susceptibility": 0.30,
                    "social_voice_weight": 2.1,
                    "skepticism_bias": 0.32,
                },
            ],
        }

    if business_type == "ecommerce":
        return {
            "project_name": project_name,
            "product_type": "ecommerce_brand",
            "lifecycle_stage": stage,
            "geographic_scope": scope,
            "regulatory_risk": regulatory_risk,
            "evaluation_depth": "standard",
            "target_segments": 4,
            "pricing_tiers": 2,
            "acquisition_channels": 3,
            "commerce_profile": {
                "store_model": "dtc_brand",
                "aov_usd": round(aov_usd, 2),
                "gross_margin_pct": round(margin_pct, 1),
                "estimated_cpc_usd": round(estimated_cpc_usd, 2),
                "shipping_days_min": max(1, min(shipping_days_max, 3)),
                "shipping_days_max": shipping_days_max,
                "free_shipping_threshold_usd": round(aov_usd * 0.75, 0),
                "hidden_shipping_at_checkout": hidden_shipping,
                "return_policy_days": return_policy_days,
            },
            "ux_journey": [
                {
                    "id": "pdp_landing",
                    "name": "Mobile Product Page (Specs, Reviews & Shipping ETA)",
                    "component_or_route": "app/products/[slug]",
                    "step_friction": 0.09,
                    "distraction_load": 0.42 if heavy_popups else 0.10,
                    "confusion_risk": 0.10,
                    "trust_gap": 0.08 if return_policy_days >= 30 else 0.24,
                    "surprise_cost": 0.0,
                    "value_clarity_gain": 0.28,
                },
                {
                    "id": "slide_cart",
                    "name": "Cart Drawer",
                    "component_or_route": "components/CartDrawer",
                    "step_friction": 0.10,
                    "distraction_load": 0.45 if heavy_popups else 0.12,
                    "confusion_risk": 0.08,
                    "trust_gap": 0.06,
                    "surprise_cost": 0.0,
                    "value_clarity_gain": 0.14,
                },
                {
                    "id": "express_checkout",
                    "name": "Express Guest / Wallet Checkout",
                    "component_or_route": "app/checkout",
                    "step_friction": 0.55 if forced_signup_early else 0.10,
                    "distraction_load": 0.06,
                    "confusion_risk": 0.08,
                    "trust_gap": 0.06,
                    "surprise_cost": 0.60 if hidden_shipping else 0.0,
                    "value_clarity_gain": 0.10,
                },
            ],
            "cohorts": [
                {
                    "id": "core_brand_buyers",
                    "name": "Core Brand & Repeat Buyers",
                    "role": "Primary DTC Buyer",
                    "share": 0.50,
                    "is_commerce_buyer": True,
                    "value_fit": 0.70,
                    "initial_trust": 0.52,
                    "onboarding_friction": 0.12,
                    "regulatory_blocker_risk": 0.04,
                    "pricing_fairness": pricing_fairness,
                    "local_liquidity": 0.90,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.42,
                    "social_voice_weight": 1.1,
                },
                {
                    "id": "social_discovery_buyers",
                    "name": "Social Discovery Shoppers",
                    "role": "Mobile Buyer",
                    "share": 0.25,
                    "is_commerce_buyer": True,
                    "value_fit": 0.60,
                    "initial_trust": 0.40,
                    "onboarding_friction": 0.14,
                    "regulatory_blocker_risk": 0.05,
                    "pricing_fairness": pricing_fairness,
                    "local_liquidity": 0.88,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.62,
                    "social_voice_weight": 1.0,
                },
                {
                    "id": "detail_researchers",
                    "name": "Spec & Return-Policy Evaluators",
                    "role": "High-Trust Buyer",
                    "share": 0.15,
                    "is_commerce_buyer": True,
                    "value_fit": 0.58,
                    "initial_trust": 0.35,
                    "onboarding_friction": 0.15,
                    "regulatory_blocker_risk": 0.06,
                    "pricing_fairness": pricing_fairness - 0.05,
                    "local_liquidity": 0.85,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.35,
                    "social_voice_weight": 1.3,
                },
                {
                    "id": "community_critics",
                    "name": "Review Forum Critics",
                    "role": "Public Amplifier",
                    "share": 0.10,
                    "is_commerce_buyer": False,
                    "value_fit": 0.42,
                    "initial_trust": 0.22,
                    "onboarding_friction": 0.10,
                    "regulatory_blocker_risk": 0.05,
                    "pricing_fairness": pricing_fairness - 0.10,
                    "local_liquidity": 0.82,
                    "liquidity_dependence": 0.0,
                    "social_susceptibility": 0.25,
                    "social_voice_weight": 1.7,
                    "skepticism_bias": 0.15,
                },
            ],
        }

    if business_type in ("future_app", "future_website"):
        is_web = business_type == "future_website"
        auth_friction = 0.64 if forced_signup_early else 0.14
        distraction = 0.52 if heavy_popups else 0.14
        return {
            "project_name": project_name,
            "product_type": "website_funnel" if is_web else "mobile_app",
            "lifecycle_stage": stage,
            "geographic_scope": scope,
            "regulatory_risk": regulatory_risk,
            "evaluation_depth": "standard",
            "target_segments": 4,
            "pricing_tiers": 2,
            "acquisition_channels": 2,
            "ux_journey": [
                {
                    "id": "first_impression",
                    "name": "Hero Headline & Value Hook" if is_web else "App Store / First Screen Value Hook",
                    "component_or_route": "src/app/page.tsx",
                    "step_friction": 0.08,
                    "distraction_load": distraction,
                    "confusion_risk": 0.16,
                    "trust_gap": 0.12,
                    "surprise_cost": 0.0,
                    "value_clarity_gain": 0.25,
                },
                {
                    "id": "signup_or_form",
                    "name": "Lead / Booking Form" if is_web else "Account & Permission Gate",
                    "component_or_route": "src/components/OnboardingGate",
                    "step_friction": auth_friction,
                    "distraction_load": 0.12,
                    "confusion_risk": 0.18,
                    "trust_gap": 0.18 if regulatory_risk != "low" else 0.10,
                    "surprise_cost": 0.0,
                    "value_clarity_gain": 0.10,
                },
                {
                    "id": "core_action_or_offer",
                    "name": "Offer & Pricing Reveal" if is_web else "First Core Action & Paywall",
                    "component_or_route": "src/app/pricing",
                    "step_friction": 0.16,
                    "distraction_load": 0.14,
                    "confusion_risk": 0.14,
                    "trust_gap": 0.12,
                    "surprise_cost": 0.45 if pricing_fairness < 0 else 0.05,
                    "value_clarity_gain": 0.15,
                },
            ],
            "cohorts": [
                {
                    "id": "early_adopters",
                    "name": "High-Intent Early Adopters",
                    "role": "Primary Target User",
                    "share": 0.40,
                    "is_b2b_buyer": is_web,
                    "value_fit": 0.65,
                    "initial_trust": 0.42,
                    "onboarding_friction": auth_friction * 0.6,
                    "regulatory_blocker_risk": 0.12 if regulatory_risk != "low" else 0.05,
                    "pricing_fairness": pricing_fairness,
                    "local_liquidity": 0.85,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.40,
                    "social_voice_weight": 1.1,
                    "pro_value_fit": 0.52,
                },
                {
                    "id": "impatient_visitors",
                    "name": "Impatient First-Time Visitors",
                    "role": "Cold Traffic User",
                    "share": 0.32,
                    "is_b2b_buyer": False,
                    "value_fit": 0.40,
                    "initial_trust": 0.22,
                    "onboarding_friction": auth_friction,
                    "regulatory_blocker_risk": 0.10,
                    "pricing_fairness": pricing_fairness - 0.10,
                    "local_liquidity": 0.85,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.58,
                    "social_voice_weight": 1.0,
                },
                {
                    "id": "privacy_cautious",
                    "name": "Privacy & Trust-Cautious Evaluators",
                    "role": "Cautious User",
                    "share": 0.18,
                    "is_b2b_buyer": False,
                    "value_fit": 0.45,
                    "initial_trust": 0.20,
                    "onboarding_friction": 0.28,
                    "regulatory_blocker_risk": 0.35 if regulatory_risk == "high" else 0.12,
                    "pricing_fairness": pricing_fairness,
                    "local_liquidity": 0.80,
                    "liquidity_dependence": 0.05,
                    "social_susceptibility": 0.45,
                    "social_voice_weight": 1.4,
                    "skepticism_bias": 0.16,
                },
                {
                    "id": "public_critics",
                    "name": "Product Hunt / Reddit Critics",
                    "role": "Public Commentator",
                    "share": 0.10,
                    "is_b2b_buyer": False,
                    "value_fit": 0.28,
                    "initial_trust": 0.12,
                    "onboarding_friction": 0.18,
                    "regulatory_blocker_risk": 0.18,
                    "pricing_fairness": pricing_fairness - 0.15,
                    "local_liquidity": 0.80,
                    "liquidity_dependence": 0.0,
                    "social_susceptibility": 0.25,
                    "social_voice_weight": 1.8,
                    "skepticism_bias": 0.24,
                },
            ],
        }

    # b2b_saas or marketplace
    is_mkt = business_type == "marketplace"
    return {
        "project_name": project_name,
        "product_type": "two_sided_marketplace" if is_mkt else "b2b_saas",
        "lifecycle_stage": stage,
        "geographic_scope": scope,
        "regulatory_risk": regulatory_risk,
        "evaluation_depth": "standard",
        "target_segments": 6 if is_mkt else 4,
        "pricing_tiers": 3,
        "acquisition_channels": 3,
        "ux_journey": [
            {
                "id": "landing_discovery",
                "name": "Landing & Value Fit",
                "component_or_route": "src/app/page.tsx",
                "step_friction": 0.08,
                "distraction_load": 0.35 if heavy_popups else 0.10,
                "confusion_risk": 0.14,
                "trust_gap": 0.10,
                "surprise_cost": 0.0,
                "value_clarity_gain": 0.25,
            },
            {
                "id": "auth_onboarding",
                "name": "Account & Verification Flow",
                "component_or_route": "src/app/onboarding",
                "step_friction": 0.58 if forced_signup_early else 0.16,
                "distraction_load": 0.12,
                "confusion_risk": 0.16,
                "trust_gap": 0.24 if regulatory_risk == "high" else 0.10,
                "surprise_cost": 0.0,
                "value_clarity_gain": 0.12,
            },
            {
                "id": "core_activation",
                "name": "Workspace / Marketplace Match",
                "component_or_route": "src/app/dashboard",
                "step_friction": 0.18,
                "distraction_load": 0.15,
                "confusion_risk": 0.18,
                "trust_gap": 0.10,
                "surprise_cost": 0.05,
                "value_clarity_gain": 0.20,
            },
            {
                "id": "upgrade_gate",
                "name": "Paid Tier / Upgrade Prompt",
                "component_or_route": "src/app/billing",
                "step_friction": 0.14,
                "distraction_load": 0.10,
                "confusion_risk": 0.12,
                "trust_gap": 0.10,
                "surprise_cost": 0.40 if pricing_fairness < 0 else 0.06,
                "value_clarity_gain": 0.05,
            },
        ],
        "cohorts": [
            {
                "id": "primary_end_users",
                "name": "Primary End Users / Supply" if is_mkt else "Solo & Power Users",
                "role": "Primary User",
                "share": 0.45,
                "is_b2b_buyer": not is_mkt,
                "value_fit": 0.65,
                "initial_trust": 0.45,
                "onboarding_friction": 0.24 if forced_signup_early else 0.14,
                "regulatory_blocker_risk": 0.22 if regulatory_risk == "high" else 0.06,
                "pricing_fairness": pricing_fairness,
                "local_liquidity": 0.62 if is_mkt else 0.88,
                "liquidity_dependence": 0.68 if is_mkt else 0.10,
                "social_susceptibility": 0.45,
                "social_voice_weight": 1.1,
                "pro_value_fit": 0.55,
            },
            {
                "id": "team_or_b2b_buyers",
                "name": "B2B Buyers / Organizers",
                "role": "B2B Paid Buyer",
                "share": 0.30,
                "is_b2b_buyer": True,
                "value_fit": 0.66,
                "initial_trust": 0.46,
                "onboarding_friction": 0.18,
                "regulatory_blocker_risk": 0.12,
                "pricing_fairness": pricing_fairness,
                "local_liquidity": 0.72 if is_mkt else 0.88,
                "liquidity_dependence": 0.55 if is_mkt else 0.10,
                "social_susceptibility": 0.35,
                "social_voice_weight": 1.3,
                "pro_value_fit": 0.68,
            },
            {
                "id": "compliance_critics",
                "name": "Compliance Auditors & Community Critics",
                "role": "Risk & Trust Amplifier",
                "share": 0.25,
                "is_b2b_buyer": False,
                "value_fit": 0.35,
                "initial_trust": 0.20,
                "onboarding_friction": 0.20,
                "regulatory_blocker_risk": 0.35 if regulatory_risk == "high" else 0.12,
                "pricing_fairness": pricing_fairness - 0.10,
                "local_liquidity": 0.68,
                "liquidity_dependence": 0.20,
                "social_susceptibility": 0.30,
                "social_voice_weight": 1.9,
                "skepticism_bias": 0.20,
            },
        ],
    }


def _prompt_choice(prompt: str, options: list[tuple[str, str]], default_idx: int = 0) -> str:
    print(f"\n{prompt}")
    for i, (_, label) in enumerate(options, start=1):
        marker = " (default)" if i - 1 == default_idx else ""
        print(f"  {i}. {label}{marker}")
    raw = input("> ").strip()
    if not raw:
        return options[default_idx][0]
    try:
        idx = int(raw) - 1
        if 0 <= idx < len(options):
            return options[idx][0]
    except ValueError:
        pass
    for key, _ in options:
        if raw.lower() == key.lower():
            return key
    return options[default_idx][0]


def _prompt_float(prompt: str, default: float) -> float:
    raw = input(f"{prompt} [{default}]: ").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _prompt_int(prompt: str, default: int) -> int:
    raw = input(f"{prompt} [{default}]: ").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _prompt_bool(prompt: str, default: bool) -> bool:
    hint = "Y/n" if default else "y/N"
    raw = input(f"{prompt} ({hint}): ").strip().lower()
    if not raw:
        return default
    return raw in ("y", "yes", "s", "si", "sí", "1", "true")


def run_interactive(lang: str = "es") -> dict[str, Any]:
    es = lang.startswith("es")
    btype = _prompt_choice(
        "¿Qué tipo de negocio o proyecto quieres simular?" if es else "What kind of business or project are you simulating?",
        [
            ("dropshipping", "Tienda Dropshipping (Shopify/Meta/TikTok Ads)" if es else "Dropshipping Store (Paid Social Ads)"),
            ("ecommerce", "Marca E-Commerce / DTC Propia" if es else "E-Commerce / Own DTC Brand"),
            ("future_app", "Futura Aplicación Móvil o Web (Idea / Pre-código)" if es else "Future Mobile or Web App (Concept / Pre-Code)"),
            ("future_website", "Futura Web / Landing / Funnel de Leads o Reservas" if es else "Future Website / Landing Page / Lead Funnel"),
            ("b2b_saas", "SaaS B2B o Herramienta para Desarrolladores" if es else "B2B SaaS or Developer Tool"),
            ("marketplace", "Marketplace Bilateral o Plataforma Regulada" if es else "Two-Sided Marketplace or Regulated Platform"),
        ],
    )
    name = input(("Nombre del proyecto o tienda [Mi Proyecto]: " if es else "Project or store name [My Project]: ")).strip() or "My Project"
    stage = _prompt_choice(
        "¿En qué fase está?" if es else "What stage is it in?",
        [
            ("concept", "Idea futura (sin código aún)" if es else "Concept / Future Idea (Pre-Code)"),
            ("mvp", "MVP / Prototipo funcional" if es else "MVP / Working Prototype"),
            ("pre_launch", "Listo para lanzar / Campaña inminente" if es else "Pre-Launch / Ready for Traffic"),
            ("growth_scale", "En producción / Escalando" if es else "Growth / Live Traffic"),
        ],
        default_idx=0,
    )
    scope = _prompt_choice(
        "Alcance geográfico:" if es else "Geographic scope:",
        [
            ("single_city", "Una ciudad" if es else "Single city"),
            ("regional", "Regional / Varias provincias" if es else "Regional"),
            ("national", "Nacional" if es else "National"),
            ("multi_country", "Internacional / Varios países" if es else "Multi-country"),
        ],
        default_idx=2,
    )

    kwargs: dict[str, Any] = {"project_name": name, "stage": stage, "scope": scope}
    if btype in ("dropshipping", "ecommerce"):
        kwargs["aov_usd"] = _prompt_float("Ticket medio / Precio producto (USD/EUR)" if es else "Average Order Value (USD)", 49.0 if btype == "dropshipping" else 79.0)
        kwargs["margin_pct"] = _prompt_float("Margen bruto % antes de anuncios" if es else "Gross margin % before ad spend", 62.0 if btype == "dropshipping" else 68.0)
        kwargs["estimated_cpc_usd"] = _prompt_float("CPC estimado de tus anuncios" if es else "Estimated ad CPC (USD)", 0.85)
        kwargs["shipping_days_max"] = _prompt_int("Días máximos de entrega" if es else "Max shipping delivery days", 15 if btype == "dropshipping" else 4)
        kwargs["hidden_shipping"] = _prompt_bool("¿El coste de envío se descubre recién al final del checkout?" if es else "Are shipping fees revealed only at checkout?", btype == "dropshipping")
        kwargs["return_policy_days"] = _prompt_int("Días de garantía / devolución" if es else "Return policy window (days)", 14 if btype == "dropshipping" else 30)
        kwargs["heavy_popups"] = _prompt_bool("¿Tiene popups (ruleta/descuento) o varios upsells agresivos?" if es else "Does it use spin-wheel popups or aggressive upsells?", False)
        kwargs["forced_signup_early"] = _prompt_bool("¿Obliga a crear cuenta antes de pagar?" if es else "Does checkout force account creation?", False)
    else:
        kwargs["regulatory_risk"] = _prompt_choice(
            "Riesgo legal / datos sensibles (menores, salud, pagos/KYC, RGPD):" if es else "Regulatory / privacy risk:",
            [("low", "Bajo" if es else "Low"), ("medium", "Medio" if es else "Medium"), ("high", "Alto" if es else "High")],
        )
        kwargs["forced_signup_early"] = _prompt_bool("¿Obliga a registrarse / KYC antes de probar el valor principal?" if es else "Does it require signup/KYC before users experience core value?", False)
        kwargs["heavy_popups"] = _prompt_bool("¿La interfaz actual/planeada tiene varios banners, modales o menús que compiten?" if es else "Are there competing banners, modals, or extra distractions?", False)

    return build_spec(btype, **kwargs)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Generate a business-tailored PulseCrowd spec (dropshipping, e-commerce, future app, future website, SaaS, marketplace)."
    )
    parser.add_argument("--interactive", action="store_true", help="Launch guided Q&A wizard in terminal.")
    parser.add_argument("--lang", default="es", help="Prompt language for --interactive (es or en).")
    parser.add_argument("--business-type", choices=VALID_BUSINESS_TYPES, default="dropshipping")
    parser.add_argument("--name", default="My Project")
    parser.add_argument("--stage", choices=("concept", "mvp", "pre_launch", "growth_scale"), default="concept")
    parser.add_argument("--scope", choices=("single_city", "regional", "national", "multi_country"), default="national")
    parser.add_argument("--regulatory-risk", choices=("low", "medium", "high"), default="low")
    parser.add_argument("--aov", type=float, default=49.0)
    parser.add_argument("--margin-pct", type=float, default=65.0)
    parser.add_argument("--cpc", type=float, default=0.85)
    parser.add_argument("--shipping-days-max", type=int, default=14)
    parser.add_argument("--hidden-shipping", action="store_true")
    parser.add_argument("--return-days", type=int, default=14)
    parser.add_argument("--forced-signup-early", action="store_true")
    parser.add_argument("--heavy-popups", action="store_true")
    parser.add_argument("--out", help="Optional path to write the generated spec JSON.")
    args = parser.parse_args(argv)

    if args.interactive:
        spec = run_interactive(lang=args.lang)
    else:
        spec = build_spec(
            args.business_type,
            project_name=args.name,
            stage=args.stage,
            scope=args.scope,
            regulatory_risk=args.regulatory_risk,
            aov_usd=args.aov,
            margin_pct=args.margin_pct,
            estimated_cpc_usd=args.cpc,
            shipping_days_max=args.shipping_days_max,
            hidden_shipping=args.hidden_shipping,
            return_policy_days=args.return_days,
            forced_signup_early=args.forced_signup_early,
            heavy_popups=args.heavy_popups,
        )

    rendered = json.dumps(spec, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
