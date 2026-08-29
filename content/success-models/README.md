# README.md — How the Success-Model Research Feeds the Content Strategy

**Status:** INTERNAL — not client-facing. This folder is a research + strategy package that informs `../CONTENT_STRATEGY_FRAMEWORK.md` and the per-store strategies (`../strategies/store-XX/STRATEGY.md`).
**Prepared by:** Bright Matter LLC agency operations team (Content Strategist)
**Observation date:** 2026-08-22

---

## 1. What this folder is

`success-models/` researches **real, observed** successful auto-dealership social accounts — including sibling Greenway Auto Group stores (West, North, East, a Greenway Ford) and two external dealerships — and turns those observations into reusable content models for the five pilot rooftops.

| File | What it is |
|---|---|
| `SUCCESS_ACCOUNTS_RESEARCH.md` | The account catalog: what each account posts, on which channels, at what cadence, and whether each observation is CONFIRMED (dated) or TO VERIFY / manual-verification-needed. |
| `CONTENT_MODELS.md` | Five reusable content models (Offer Promo, Per-Vehicle Inventory Line, Model Review Depth, Department/Service & Trust, Local/Community & People), each mapped to channels, pillars, cadence, and Kia-vs-Ford per-store notes, with evidence labels. |
| `SIBLING_SOCIAL_ANALYSIS_2026-08-29.md` | Full FB + IG (Reels) + TikTok analysis of sibling rooftops Greenway Kia North, West, and East (retrieved 2026-08-29 via Apify/Exa): account inventory, post-level engagement data, what works and what does not, cadence, pillar read-through, and a per-pilot-store repurposing playbook with specific posts and adaptations. Closes (for these three stores) the FB/IG/TikTok verification gap in §4 below. |
| `README.md` (this file) | How the research feeds the strategy, and which models still need verification. |

---

## 2. How it feeds the content strategy

1. **Pillar definitions.** The five pillars already in `CONTENT_STRATEGY_FRAMEWORK.md` §3 (Inventory, Service, Community/Local, Behind-the-Scenes, Reviews & Proof) stay the same. What this research adds is **format-level evidence** for *how* winning accounts fill each pillar: e.g., the Per-Vehicle Inventory Line (Model B) is a proven, reproducible way to fill the **Inventory** pillar; the Department/Service & Trust model (Model D) is a proven way to fill **Service** and **Reviews & Proof**; the Local/Community model (Model E) fills **Community/Local** and **Behind-the-Scenes**. The Offer model (Model A) and Depth model (Model C) both serve **Inventory** in different flavors.
2. **Channel plan.** Each model's channel mapping slots straight into the per-channel plan in `CONTENT_STRATEGY_FRAMEWORK.md` §6 and the cadence table in §8 (which itself is benchmark-sourced from `audit/BENCHMARKS.md`). No new cadence numbers were invented — the models reuse the framework's house cadence.
3. **Per-store strategy.** When a store's strategy (`strategies/store-XX/STRATEGY.md`) is built, the GM picks models by goal using the "Model selection guidance" table in `CONTENT_MODELS.md` §5, then fills the calendar (`CONTENT_CALENDAR_TEMPLATE.md`) with the chosen model formats.

---

## 3. Which models are safe to use now vs. which need verification

| Model | Evidence status | Can it go into a client-facing calendar now? |
|---|---|---|
| A — Offer & Incentive Promo | OBSERVED format (West, East, Galpin). Hype tone deliberately excluded. | **Format + cadence only.** Every offer amount/incentive is TO VERIFY with the store before posting (no-fabrication rule). |
| B — Per-Vehicle Inventory Line | OBSERVED (Greenway Ford, Longo, West). | **Yes as a format**, but every vehicle posted must come from the store's real inventory feed (TO VERIFY via Shannon McNeil). |
| C — Model Review Depth | OBSERVED (North long-form, West short). Forward-model claim on North = caution, not to copy. | **Yes as a format**; review only vehicles the store can actually sell (TO VERIFY). |
| D — Department/Service & Trust | OBSERVED (Greenway Ford, Longo). | **Yes as a format**; store-specific service facts are TO VERIFY. |
| E — Local/Community & People | OBSERVED hooks (West local-sports + bilingual; Galpin showroom). | **Needs per-market verification** — local hooks, sports ties, language split all TO VERIFY via Shannon/GMs; named staff need two sources (OPERATING_RULES §3.5). |

**Bottom line:** Models B, C, and D are ready as **formats**; Models A and E are ready as formats but depend most heavily on confirmed store facts (real offers, real local ties) before any client-facing use.

---

## 4. What is still open (must be verified before the operator builds a client-facing calendar)

1. **Facebook / Instagram / TikTok / Reddit content** for every account in the catalog — manual verification needed — 2026-08-22 (Meta/TikTok block automated fetch; this environment could only observe YouTube). **UPDATE 2026-08-29: retrieved via Apify for Greenway Kia North, West, and East (FB + IG + TikTok) — see `SIBLING_SOCIAL_ANALYSIS_2026-08-29.md`.** Still open for the external accounts (Longo, Galpin), the competitor sets, and Reddit. Current-account and follower data for the pilot stores is still per `CLIENT.md` §8 / `channel-matrix.csv` (TO VERIFY via Shannon).
2. **A citable third-party "best dealership social accounts / awards" list** — manual verification needed — 2026-08-22 (web search blocked). Until found, the external-dealer "well-regarded" characterization is my selection, not a cited award.
3. **Rooftop-to-street-address attribution** of sibling Greenway channels — 2026-08-29: North (625 N US Hwy 17-92, Longwood FL) and East (8701 E Colonial Dr, Orlando FL) CONFIRMED; West = Orlando confirmed, street address still TO VERIFY; Greenway Ford channels still TO VERIFY (OPERATING_RULES §3.8).
4. **Store 05 and Stores 01/03/04 current channels** — manual verification needed — 2026-08-22.

---

## 5. Updates

Review this folder each time a new sibling/competitor account is observed or the blocked platforms become retrievable; re-date every new observation. Nothing here is client-facing until Shannon McNeil approves.
