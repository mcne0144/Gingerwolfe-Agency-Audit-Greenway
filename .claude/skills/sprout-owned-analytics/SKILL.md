---
name: sprout-owned-analytics
description: Pull owned social analytics from the Sprout Social API (read-only) and turn them into the INTERNAL reporting the Greenway pilot uses — connection inventory, per-profile organic vs paid splits, post-level metrics, reconciliation against public scrape numbers, and KPI baselines. Use this whenever a Sprout API token is provided or mentioned, whenever the task involves owned analytics, impressions, reach, "what's connected in Sprout", organic vs paid attribution, or verifying public social numbers against owned data — even if the user just pastes a token with no instructions, or asks a one-off question like "how many impressions did store X get". Also use for analyzing previously cached Sprout API JSON when no live token is available.
---

# Sprout owned-analytics pull and report

Read-only analytics from the Greenway Sprout account (or cached pulls of it), reported the way this engagement needs them: organic separated from paid, always.

## Token hygiene (non-negotiable)

1. The token is a paste-in secret. Write it only to a chmod-600 file in the session scratchpad, or export it as `SPROUT_TOKEN` per-command. Never into the repo, a commit, a report, or printed output.
2. Before any commit after a Sprout session, grep the staged tree for the token's first characters.
3. Delete the scratchpad copy when the pull is done, and remind the operator to rotate the token.
4. Everything here is read-only (GET metadata, POST analytics queries). No publishing endpoint is ever called; agents never publish.

## Workflow

The bundled script handles auth, pagination, and aggregation:

```bash
export SPROUT_TOKEN=<token>   # or --token-file <path>
S=.claude/skills/sprout-owned-analytics/scripts/sprout_pull.py
python3 $S verify                                   # -> customer_id (Greenway = 2885225)
python3 $S profiles  --customer 2885225 --out profiles.json
python3 $S analytics --customer 2885225 --profiles 7668848,7668851 \
        --start 2026-08-01 --end 2026-08-28 --out daily.json
python3 $S posts     --customer 2885225 --profiles 7668848,7668851 \
        --start 2026-08-01 --end 2026-08-28 --out posts.json
```

With no live token, do the same analysis from cached JSON (the raw rows the script writes with `--out`); say clearly in the report that the data is a cached pull and give its retrieval date.

## Reading the data correctly (lessons already paid for)

1. **Organic vs paid is the load-bearing split.** In the 2026-08 baseline, paid was 96–99% of impressions on every Facebook page except Kia North's main page. A total-impressions number without the split misleads every downstream reader. Pilot KPI baselines and GM reporting use organic columns only; paid may be shown separately, labeled.
2. **Profile identity is by ID, never by name.** The account holds near-identical names ("Greenway Kia North" exists twice: 7668819 is the real page, 7668829 is an ads-only duplicate; "Greenway Kia West" is the Orlando sibling, NOT pilot Store 01 West Palm Beach). Pin `customer_profile_id` in every table.
3. **Known mappings (2026-08-29):** pilot — S02 Avenues FB 7668833, S03 Rivergate FB 7668849 + IG 7679631, S04 Hickory Hollow FB 7668847, S05 Ford Raytown FB 7668837, S01 WPB not connected. Siblings — North FB 7668819 (+dup 7668829), West FB 7668848 + IG 7673987, East FB 7668851 + IG 7673986. No dealership TikTok or YouTube connected. Re-verify with the `profiles` subcommand each session; connections change in Month 2.
4. **Metric quirks:** `impressions_unique` (reach) is null for Facebook at this API tier, real for Instagram. `lifetime_snapshot.followers_count` is a snapshot (the script keeps the latest, never sums). FACEBOOK_AD post rows return zero/null owned metrics. Public Facebook reel "views" counters are not comparable to owned per-post impressions and must never be cited as organic evidence.
5. **Reconciliation is the validation.** Owned IG Reel impressions matched public play counts almost exactly in the 2026-08 pull (often to the digit). When owned and public disagree by multiples on Facebook, suspect paid delivery, and say the gap is unproven without Ads Manager rather than asserting a cause.

## Report format

Write an INTERNAL markdown report (in this repo: `reporting/SPROUT_API_PULL_<date>.md`; `SPROUT_API_PULL_2026-08-29.md` is the exemplar). Structure:

1. Header: status INTERNAL, retrieval date, window, method line stating read-only use and that the token is not stored and rotation was requested.
2. **What is connected / not connected** per pilot store and benchmark store, with gaps called out.
3. **Per-profile table** for the window: impressions, organic, paid, engagements, posts, net follower growth, followers. Then a short "what this table says" list.
4. **Reconciliation vs public data** where public numbers exist, as a MATCH/DISCREPANCY table.
5. **Actions triggered** (config-plan updates, KPI baselines, expansion signals) and a verification log (CONFIRMED / TO VERIFY / not fabricated).

Findings that belong to other docs get amendments there, not just a mention here: connection facts into `reporting/SPROUT_CONFIG_PLAN.md`, paid-media and hygiene observations into `expansion-signals.md` (parked per the live-spend hard line), corrections into the doc they correct.

House rules: INTERNAL only, no client contact, organic-only SOW means paid data is observed and parked, never acted on; no em-dash-heavy prose; every number is an API-returned value or labeled TO VERIFY. See `OPERATING_RULES.md` and `CLIENT.md`.
