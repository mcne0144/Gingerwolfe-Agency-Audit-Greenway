# Store 05 — Greenway Ford Kansas City — Store Profile & Channel Inventory
**Status:** INTERNAL — store identity VERIFIED (2026-08-12); channel inventory PROVIDED (operator, 2026-08-22); **Sprout connectivity PROVIDED (operator, 2026-08-25)**
**Last updated:** 2026-08-25 (Sprout-connectivity reconciliation added)
**Owner:** Bright Matter LLC agency operations team
---
## Store identity
| Field | Value |
|---|---|
| Store name | Greenway Ford Kansas City (VERIFIED 2026-08-12) |
| Location / market | Raytown, MO (VERIFIED 2026-08-12) |
| General Manager | Shane Silvey (VERIFIED 2026-08-12) |
| Offerings | CONFIRMED priority mix (GM Shane Silvey, via operator note 2026-08-24): **service and used** (store sells ~3 used per new; service contributes more to bottom line). Full new/used/service offering list still TO VERIFY. |
| Audience notes | TO VERIFY — request from client via Shannon McNeil |
| Brand name to use | **Greenway Ford of KC** (CONFIRMED decision, GM via operator note 2026-08-24); drop Raytown framing; legacy "Dick Smith Ford" traces flagged for cleanup |

## Channel inventory (source: operator 2026-08-22)
Confirmed from `_source/channel-inventory_shannon_2026-08-22.csv` (tags: sheet = Shannon's own record; web-2026-08-22 = our team's research dated today). Status is conservative — records observed/known state only; no account created or touched.
| Channel | Handle / URL | Status | Source |
|---|---|---|---|
| Website | https://www.greenwayfordkc.com/ | Active | sheet |
| Facebook | https://www.facebook.com/greenwayfordraytown | Active | sheet |
| YouTube | https://www.youtube.com/@GreenwayFordofKansasCity-zw6sj | Active | sheet |
| DealerRater | https://www.dealerrater.com/dealer/Greenway-Ford-review-29227/ | Active (recorded) | sheet |
| Instagram | NO ACCOUNT FOUND | No account | web-2026-08-22 |
| TikTok | NO ACCOUNT FOUND | No account | web-2026-08-22 |
| Reddit | Not in source file | TO VERIFY | — |
| Google Business Profile | Not in source file | TO VERIFY | — |

## Channel inventory (original 6-channel view)
Status values: **Active / No account / Duplicate / TO VERIFY** (lowercased in matrix).
| Channel | Handle / URL | Active? | Posting cadence | Follower count | Last post |
|---|---|---|---|---|---|
| Facebook | https://www.facebook.com/greenwayfordraytown | Active (confirmed 2026-08-22) | TO VERIFY | TO VERIFY | TO VERIFY |
| Instagram | NO ACCOUNT FOUND | No account (web-2026-08-22) | — | — | — |
| TikTok | NO ACCOUNT FOUND | No account (web-2026-08-22) | — | — | — |
| YouTube | https://www.youtube.com/@GreenwayFordofKansasCity-zw6sj | Active (confirmed 2026-08-22) | TO VERIFY | TO VERIFY | TO VERIFY |
| Reddit | Not in source file | TO VERIFY | — | — | — |
| Google Business Profile | Not in source file | TO VERIFY | — | — | — |

## GM interview findings (source: operator Wispr note 2026-08-24 — GM Shane Silvey; see `audit/gm-interviews/store-05_SILVEY.md`)
- **CONFIRMED — Branding:** standardize on **Greenway Ford of KC**; legacy **'Dick Smith Ford'** still surfaces in service emails, backlinks (Nextdoor), website image links — cleanup flagged.
- **CONFIRMED — Listings:** Apple Maps shows **Hertz Rent-A-Car**; Copilot/DuckDuckGo return wrong address *(GM-reported; independent re-verify TO VERIFY)*.
- **CONFIRMED — Facebook:** currently only static ads via Conquest; **Instagram** to be spun up and cross-posted (Phase 1). Matches inventory (no current IG/TikTok).
- **CONFIRMED — TikTok:** viable if a personality-hire creates content; candidate = **Shane Silvey's daughter** *(consent/usage TO VERIFY before use)*; steer away from insider sales humor toward self-deprecating sales humor.
- **CONFIRMED — Content direction:** service-department educational shorts (oil change, wiper tips, staff Q&A); repurpose LocalIQ walk-around videos; AI serial concept (e.g., recurring alien characters) to test.
- **CONFIRMED — Measurement:** Sprout dashboard planned; pull in GA4, organic + paid analytics, review sites.
- **CONFIRMED — Competitor set (GM-named):** Bob Sight, Rob Sight, Blue Springs Ford, Metro Ford.
- **CONFIRMED — Content focus:** brand awareness & engagement, not price/discount posts.
- **CONFIRMED — Access item:** Shane to ask Conquest to grant Shannon Meta ad-account access before Conquest relationship ends.
## Sprout connectivity (operator-provided 2026-08-25; source: `_source/channel-sprout-connectivity_shannon_2026-08-25.md`)
| Channel | Sprout status |
|---|---|
| Facebook (`greenwayfordraytown`) | **CONNECTED** |
| GA4 — "Ford Dick Smith" | **CONNECTED — MISLABELED.** This is actually Greenway Ford of Raytown under the wrong name (operator 2026-08-25). Relabel to **Greenway Ford of KC** to match the GM rebrand (Silvey 08-24; also `STRATEGY.md` rev 3 + `audit/gm-interviews/store-05_SILVEY.md`). |
| Instagram | N/A — no account (Phase-1 stand-up per operator 2026-08-22) |
| TikTok | N/A — no account (Phase-1 stand-up per operator 2026-08-22) |
| YouTube (`@GreenwayFordofKansasCity-zw6sj`) | NOT connected / not listed (support/search home; active baseline) |

**Not-connected list:** none among live social accounts — FB is connected and the only connected GA4 is the mislabeled "Ford Dick Smith". No IG/TikTok accounts exist yet (Phase-1 stand-up). YouTube is live but not listed in Sprout.

## Account-hygiene notes (INTERNAL)
- **No Instagram account** found as of 2026-08-22 (web research) — Phase-1 stand-up, not a live slot (operator-confirmed 2026-08-22).
- **No TikTok account** found as of 2026-08-22 (web research) — Phase-1 stand-up, not a live slot (operator-confirmed 2026-08-22).
- **GA4 mislabel:** "Ford Dick Smith" GA4 is connected but carries the pre-rebrand name; relabeling to Greenway Ford of KC is part of the brand-cleanup flagged in the GM interview (Silvey 08-24).

## Known gaps
- **Access unknown.** No account access, ownership, or permission details confirmed for any channel.
- **Active-state detail unknown.** Cadence, follower counts, and last-post dates still TO VERIFY per channel.
- **Reddit & GBP** handles not in the source file — TO VERIFY via Shannon McNeil.
- **Audit blockers.** A full account & performance audit still needs access confirmation via Shannon McNeil (checklist: `CLIENT.md` §8).
