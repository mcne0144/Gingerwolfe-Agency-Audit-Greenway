# SPROUT_API_PULL_2026-08-29.md — First owned-data pull: connections, August analytics, public-data reconciliation

**Status:** INTERNAL — owned analytics working file, not client-facing. Nothing goes to a GM or the client without Shannon McNeil's approval.
**Prepared:** 2026-08-29 (Reporting Analyst lane). All data retrieved 2026-08-29 via the Sprout Social API (read-only), customer "Greenway", customer_id 2885225.
**Method:** operator-supplied API token used for GET metadata and POST analytics/profiles + analytics/posts only. No publishing action taken or possible via these endpoints. The token is not stored in this repository and the operator has been asked to rotate it after this session.
**Reporting window:** 2026-08-01 through 2026-08-28 (daily granularity, America/New_York for post times).

Headline: the Sprout account holds 46 connected profiles spanning the whole Greenway group, all three Orlando sibling stores reconcile almost exactly against the public numbers in `content/success-models/SIBLING_SOCIAL_ANALYSIS_2026-08-29.md`, and the single biggest new fact is that nearly all Facebook impression volume at the pilot rooftops is paid, not organic.

---

## 1. What is connected (and what is not)

46 profiles total: 42 Facebook pages (group-wide, most rooftops outside the pilot), 4 Instagram accounts, 1 TikTok (the operator's personal @shannon50000), 0 YouTube.

### 1.1 Pilot rooftops

| Store | Facebook | Instagram | TikTok |
|---|---|---|---|
| 01 West Palm Beach | **NOT CONNECTED** | **NOT CONNECTED** | not connected |
| 02 Avenues (Jax) | ✓ 7668833 "Greenway Kia At The Avenues" | not connected | not connected |
| 03 Rivergate | ✓ 7668849 | ✓ 7679631 @greenwaykiarivergate | not connected (no account exists) |
| 04 Hickory Hollow | ✓ 7668847 | not connected | not connected |
| 05 Ford Raytown | ✓ 7668837 "Greenway Ford of Raytown" | not connected (no account exists) | not connected (no account exists) |

**Store 01 is the only pilot rooftop with zero Sprout connections.** This contradicts the working assumption in `SPROUT_CONFIG_PLAN.md` §1.1 that "most profiles are already connected" as applied to Store 01, and it is the first item for the Month 2 connection-verification pass. No pilot-store TikTok and no pilot-store YouTube is connected anywhere; TikTok/YouTube connection is a Month 2 action (via Shannon/Shawn, agents connect nothing).

### 1.2 Sibling benchmark stores (Orlando)

| Store | Facebook | Instagram | TikTok |
|---|---|---|---|
| Kia North | ✓ **TWO pages**: 7668819 /GreenwayKiaNorth (the real page) AND 7668829 "Greenway Kia North" fb.com/109475951790496 | not connected (IG dormant since 2024) | not connected |
| Kia West | ✓ 7668848 | ✓ 7673987 @greenway_kia_west | not connected |
| Kia East | ✓ 7668851 | ✓ 7673986 @greenway_kia_east | not connected |

The second North page (7668829) has 104 followers, posted 0 times in August, earned 0 engagements, and still delivered 196,514 impressions of which 196,210 were paid. It is functioning as an ads-delivery page. This is a new account-hygiene finding (logged in `expansion-signals.md`), and it means "Kia North Facebook" is ambiguous inside Sprout: reporting must always pin profile IDs, which is exactly the near-identical-names risk `OPERATING_RULES.md` §3.8 warns about.

**No sibling TikTok is connected**, so the TikTok numbers in the sibling analysis (the growth engine) remain public-data only. Sprout cannot currently refine them.

## 2. August owned analytics, organic vs paid (2026-08-01 to 08-28)

| Profile | Impressions | Organic | Paid | Engagements | Posts | Net follower growth | Followers (Aug 28) |
|---|---|---|---|---|---|---|---|
| Kia North FB (main) | 11,128 | 11,128 | **0** | 195 | 11 | +10 | 1,611 |
| Kia North FB (2nd page) | 196,514 | 304 | 196,210 | 0 | 0 | 0 | 104 |
| Kia West FB | 245,082 | 5,136 | 239,946 | 94 | 12 | +6 | 1,298 |
| Kia East FB | 254,640 | 7,792 | 246,848 | 130 | 17 | +3 | 3,639 |
| Kia West IG | 64,638 | 23,174 | 39,145 | 804 | 12 | +13 | 571 |
| Kia East IG | 69,387 | 19,791 | 45,973 | 575 | 11 | +22 | 424 |
| S02 Avenues FB | 95,804 | 1,652 | 94,152 | 7 | 1 | +2 | 490 |
| S03 Rivergate FB | 359,616 | 2,952 | 356,664 | 19 | 1 | +21 | 1,126 |
| S03 Rivergate IG | 67,110 | 250 | 66,723 | 1 | 1 | +3 | 20 |
| S04 Hickory Hollow FB | 445,709 | 4,784 | 440,925 | 25 | 1 | +31 | 1,478 |
| S05 Ford Raytown FB | 58,928 | 1,280 | 57,648 | 11 | 2 | +4 | 2,641 |

Reach (impressions_unique) is exposed only for Instagram: West IG 57,399, East IG 66,846, Rivergate IG 44,871 for the window. Facebook reach returns null at this API tier.

### What this table says

1. **Paid delivery dominates every Facebook page except Kia North's main page**, which is the group's only 100% organic FB surface in this set. The pilot rooftops are running (or having run for them) substantial Meta ad delivery right now: Hickory Hollow 440.9K paid impressions, Rivergate 356.7K, Avenues 94.2K, Ford Raytown 57.6K in four weeks, against 1 to 2 organic posts each and single-to-low-double-digit engagements.
2. **The pilot's true organic baseline is tiny and now precisely known:** 1,280 to 4,784 organic FB impressions per pilot store for the month. This is the honest "before" number for the KPI framework, and it makes attribution discipline mandatory: GM reporting must never let paid impressions inflate the organic pilot's story. `GM_KPI_FRAMEWORK.md` targets should key on organic impressions, organic engagements, and follower growth, with paid shown separately if ever shown at all.
3. **Engagement lives where the content model is right, not where impressions are:** Hickory Hollow bought 445K impressions and earned 25 engagements; Kia West IG earned 804 engagements on 64K. The engagement-per-impression gap between the sibling content engine and the pilot pages is roughly two orders of magnitude, which is the pilot's pitch in one row.
4. **Rivergate's IG (20 followers, 1 post, 250 organic impressions) is connected but effectively unused**, while its paid line still pushed 66.7K impressions. Confirms the §7 plan to treat Store 03 as min-viable FB+IG Reels with formats that need no talent.
5. Follower counts above fill part of the "pilot-store follower baselines TO VERIFY" item in the sibling analysis §9 (FB side plus Rivergate IG).

## 3. Reconciliation: Sprout owned data vs the public numbers in the sibling analysis

Post-level August owned metrics match the public counts pulled via Apify on 2026-08-29 almost exactly, which validates the sibling analysis dataset:

| Post (analysis doc ref) | Public (doc) | Sprout owned (lifetime) | Verdict |
|---|---|---|---|
| East IG "ENDLESS SPECIALS" 08-19 | 7,171 plays / 198 likes | 7,161 impressions / 197 likes | MATCH |
| East IG Sorento listicle 08-26 | 4,209 / 140 | 4,188 / 139 | MATCH |
| West IG fuel-efficiency tips 08-12 | 3,922 / 87 | 3,922 / 87 | EXACT |
| West IG Nicole intro 08-21 | 3,701 / 102 | 3,701 / 102 (plus 82 shares, not publicly visible) | EXACT |
| East IG Spanish decision Reel 08-06 | 1,724 / 20 | 1,724 / 20 | EXACT |
| East IG EV6 $0-down 08-28 | 1,391 / 43 | 1,385 / 43 | MATCH |
| East IG team vox-pop 08-21 | 705 / 21 | 705 / 21 | EXACT |
| North FB wrestling Reel 08-08 | 900 views / 14 shares | 900 impressions / 16 shares | MATCH |
| East FB Sorento listicle 08-26 | **6,425 views / 86 reactions** | **1,261 impressions / 464 video views / 10 likes / 18 engagements** | **DISCREPANCY** |

### The East FB listicle discrepancy, and the answer to the doc's boost question

The sibling analysis §2.3 called this "the best organic Facebook post observed" and flagged "whether it was boosted" as TO VERIFY. Sprout now shows: (a) East's FB page ran 246.8K paid impressions in August against 7.8K organic; (b) the listicle post's owned organic-side metrics are 1,261 impressions and 464 video views, nowhere near the 6,425 the public player shows. The public Facebook reel view counter and Sprout's per-post impressions are different measurements, and paid delivery of the same creative is the plausible gap, but the API tier used here does not expose per-post paid spend, so this stays short of proof. What is settled either way: **the 6.4K public figure cannot be used as organic evidence, and the "best organic FB post" claim is withdrawn** (amendment noted in the sibling doc §2.3/§9). The format lesson (listicles are East's strongest FB format relative to its own feed) survives on the owned data: it is still the page's top organic post of August after the "2027 Sportage" post, which itself carries a forward-model title the pilot will not copy.

### Notes from the August post pull (73 posts across the connected set)

1. Cadence confirms the public read: East FB 17 posts, West FB 12, North FB 11, West IG 12, East IG 11 for the window.
2. The one-pipeline pattern is visible in owned data too: identical captions posting across East/West/North FB and IG on the same days.
3. Four FACEBOOK_AD objects appear (Labor Day and trade-in creatives on pilot-side pages) with zero or null owned metrics at this tier, consistent with ads being managed outside the page's organic surface.
4. North FB's 08-23 "2027 Kia Telluride" post (1,775 impressions) confirms forward-model titling is still in active use at the siblings. The no-copy rule stands.

## 4. Actions this pull triggers

1. **Month 2 Sprout connection list is now concrete** (feeds `SPROUT_CONFIG_PLAN.md` §2): connect Store 01 FB+IG+TikTok, Store 02 IG+TikTok, Store 04 IG (if the store confirms its handle) and TikTok, Store 05 nothing to add until accounts exist; connect pilot YouTube where wanted; decide with Shannon whether sibling TikToks (@greenwaykianorth, @greenwaykiawest) get connected so benchmark reporting can use owned data. All connections are Shannon/Shawn actions, never agents.
2. **KPI baselines:** use §2 organic columns as the pre-pilot August baseline per store. Do not benchmark pilot stores against sibling paid-inflated totals.
3. **Attribution guard in every GM readout:** organic and paid stated separately, always. The combined paid+organic view the operator wants for GMs is buildable from this same endpoint (impressions_organic vs impressions_paid) once reporting starts.
4. **Expansion signal logged** (paid media already running at scale on pilot rooftops; North duplicate ads-page hygiene): see `expansion-signals.md`. Parked per the live-spend hard line; the operator decides what gets raised.
5. **Token rotation:** the operator should rotate the API token now that this pull is complete.

## 5. Verification log

**CONFIRMED (2026-08-29, Sprout API):** everything in §1 and §2; the §3 match column.
**Still TO VERIFY:** who operates the paid campaigns behind the pilot-store pages (Brennan's informal role is the known lead; do not contact him, route via Shannon); whether the East listicle's public view gap is paid delivery (needs Ads Manager access, out of scope); Store 04 IG handle; FB reach (not exposed at this API tier).
**Not fabricated:** every number above is an API-returned value for the stated window; nothing is estimated.
