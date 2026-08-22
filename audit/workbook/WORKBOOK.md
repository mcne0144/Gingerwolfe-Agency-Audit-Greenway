# GREENWAY AUTO GROUP — MONTH 1 AUDIT WORKBOOK (INTERNAL WORKING FILE)

**Status:** INTERNAL — audit working file. Not client-facing. No agent contacts the client; Shannon McNeil is the only client-facing voice.
**Audit date:** 2026-08-12 · **Prepared by:** Audit & Research Analyst (Bright Matter LLC agency operations team)
**Structure:** one tab per rooftop (Store 01–05) × six buckets. Every cell is either (a) a populated, sourced finding (citation in brackets → Sources appendix) or (b) a named blocker with owner and what is needed to unblock. No empty cells; nothing invented.
**Conventions:** “TO VERIFY — request from client via Shannon McNeil” = store data needed via Shannon McNeil. “manual verification needed — 2026-08-12” = platform blocked automated retrieval on the audit date (a failed fetch is not evidence an account does not exist — OPERATING_RULES §3.7).
**Cross-refs:** audit/AUDIT_FRAMEWORK.md, audit/BENCHMARKS.md, CLIENT.md §8–9, engagement-state.md, BLOCKERS.md (one-page), SOURCES.md (appendix).

---

## TAB — Store 01: Greenway Kia West Palm Beach

| Field | Value |
|---|---|
| Market | West Palm Beach, FL |
| General Manager | Mike Wangle |
| Address (Google Maps listing) | 735 S Military Trl Ste C, West Palm Beach, FL 33415 ([S01]) |
| Phone / Website | (561) 433-1511 / greenwaykiawestpalmbeach.com ([S01]) |
| GM background | GM identity verified from owner (client master record [S03]); public-source corroboration: search engines (Google/Bing/DDG) and DealerRater were blocked from the research environment on 2026-08-12, so a second independent public source could not be retrieved this session — TO VERIFY — request from client via Shannon McNeil (two-source rule, OPERATING_RULES §3.5). |

### Bucket 1 — Accounts & Access Inventory

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google Business Profile (GBP) | OBSERVED (public): Google Maps listing exists for “Greenway Kia West Palm Beach” with a live GBP owner-post stream (latest: Owner post on GBP listing: “Mid-Year Mega Sales Event Happening at Greenway Kia West Palm Beach!” — Jun 18, 2026). This shows listing-owner access is active on GBP, but does not confirm who holds it (store staff vs vendor) or tool used. TO VERIFY — request from client via Shannon McNeil. |
| Facebook | BLOCKER — Facebook page existence/ownership. Owner: Shannon McNeil. Needed: FB page URL + admin list (Meta Business Manager). FB blocks automated fetch — manual verification needed — 2026-08-12. |
| Instagram | BLOCKER — Instagram handle/ownership. Owner: Shannon McNeil. Needed: IG handle + access. IG blocks automated fetch — manual verification needed — 2026-08-12. |
| TikTok | BLOCKER — TikTok account/ownership. Owner: Shannon McNeil. Needed: TikTok handle + access. TikTok blocks automated fetch — manual verification needed — 2026-08-12. |
| YouTube | BLOCKER — YouTube channel/ownership. Owner: Shannon McNeil. Needed: channel URL + Studio access. Channel-level data requires Studio/API — manual verification needed — 2026-08-12. |
| Reddit | BLOCKER — Reddit presence/ownership. Owner: Shannon McNeil. Needed: any store-controlled u/ or r/ accounts. Reddit blocked automated search from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Cross-channel access & vendor split | BLOCKER — accounts & access inventory. Owner: Shannon McNeil (store data/access, per CLIENT.md §8.1) and Shawn Vink (corporate IT/admin access where applicable). Needed: per-channel handles/URLs, active/inactive status, login access and admin-role list per account (Meta Business Manager, Google Business Profile, TikTok, YouTube, Reddit), and the split between store staff and outside vendors. This is the biggest Month 1 timeline risk; until it clears, no performance or ownership cell below can be verified. Public-page review only is possible without access. |

### Bucket 2 — Performance Baselines (per channel)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| All 6 channels — reach/impressions/engagement baselines | BLOCKER — performance baselines. Owner: Shannon McNeil. Needed: native-insights access per channel (Meta Business Suite for FB/IG, TikTok Analytics, YouTube Studio, GBP Insights) granted per-account; corporate access via Shawn Vink where applicable. Platform notes: TikTok and Facebook block automated retrieval manual verification needed — 2026-08-12; YouTube channel-level data requires Studio/API access; GBP Insights requires listing-owner access. A failed fetch is not evidence an account does not exist. |
| Public-visible baseline (GBP) | OBSERVED (public): GBP listing rating 4.5/5 at audit date; full review count and Insights (searches, calls, direction requests) require listing-owner access — TO VERIFY — request from client via Shannon McNeil. |
| Public-visible baseline (YouTube/FB/IG/TikTok) | Follower/subscriber counts are public on YouTube, but channel-level data is blocked from automated fetch — manual verification needed — 2026-08-12. FB/IG/TikTok counts also blocked — manual verification needed — 2026-08-12. No numbers stated rather than inventing them. |

### Bucket 3 — Reputation (Reddit, Google, DealerRater, Cars.com, Edmunds, Yelp)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google reviews | OBSERVED (public): Google rating 4.5/5 on the store's Google Maps listing at audit date. Review count and review-response behavior not visible in Google Maps' limited view — require listing-owner access or manual review — TO VERIFY — request from client via Shannon McNeil/manual verification needed — 2026-08-12. |
| DealerRater | BLOCKED — DealerRater rating/review count/response count. DealerRater returned HTTP 403 (CloudFront) from this environment on 2026-08-12 — manual verification needed — 2026-08-12. DealerRater presence/absence is NOT confirmed either way. |
| Cars.com | BLOCKED — Cars.com rating/review count. Cars.com blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Edmunds | BLOCKED — Edmunds rating/review count. Edmunds blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Yelp | BLOCKED — Yelp rating/review count. Yelp blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Reddit | ABSENCE-OBSERVED (framed as absence, not complaints): no organic Reddit footprint for “Greenway Kia West Palm Beach” was retrievable programmatically — Reddit blocked automated search on 2026-08-12 (manual verification needed — 2026-08-12). Per operator context, four of five rooftops have no organic Reddit footprint and zero dealership responses to public complaints — to be confirmed per-store via manual Reddit check + Apify scraper once MCP access is granted. |
| Review-response pattern | STRUCTURAL FINDING (operator context, confirm in audit): named individual staff drive nearly all positive reviews at every rooftop — a dependency on staff members, not the store brand (CLIENT.md §9). Hold for one-on-one GM conversation; frame as absence, not complaint list. |

### Bucket 4 — Search Presence

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Exact brand+market query | OBSERVED (public): searching Google Maps for the store name “Greenway Kia West Palm Beach” returns the store's own listing as the top/only business result with address, phone, and website — the store surfaces for its exact brand + market on Google Maps. [S01] |
| Generic category query (map pack) | Generic query test (e.g., “Kia dealer near [market]”) blocked — Google web search returned an anti-bot page from this environment on 2026-08-12 (manual verification needed — 2026-08-12). Map-pack position for generic category queries: TO VERIFY via manual search or a research tool (Exa/Apify) once granted. |
| Website | Website from listing: greenwaykiawestpalmbeach.com (verified on the Google Maps listing panel). Website/site-search standing TO VERIFY — Google search blocked this session (manual verification needed — 2026-08-12). |

### Bucket 5 — Competitive Benchmarking (local market)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Competitor set (per-market) | BLOCKED this session — Google/Bing/DDG web search all returned anti-bot or captcha pages from this environment on 2026-08-12 (manual verification needed — 2026-08-12); DealerRater also blocked (HTTP 403). Competitor list for West Palm Beach, FL (Kia dealers in the Palm Beach metro for Store 01; Kia dealers in the Jacksonville metro for Store 02; Kia dealers in the Nashville metro for Stores 03–04; Ford dealers in the Kansas City metro for Store 05) and their Google ratings are TO VERIFY — request research re-run with Exa/Apify MCP once granted, or manual check. |
| Benchmark context | Benchmarks for scoring are ready in audit/BENCHMARKS.md (BrightLocal 2026 review study; Rival IQ 2025 engagement trends — [S04]). These are directional, not pass/fail. |

### Bucket 6 — Current Operations Workflow

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Current poster(s), tool(s), cadence | BLOCKER — operations workflow (who posts today, with what tool, on what cadence). Owner: Shannon McNeil. Needed: store answers (per CLIENT.md §8) on current poster(s), tool(s) (Sprout/other scheduler or native app), posting cadence per channel, and whether a vendor currently manages any account. |
| Public signal (GBP posting) | OBSERVED (public): the GBP listing for “Greenway Kia West Palm Beach” has recent owner posts (latest: Owner post on GBP listing: “Mid-Year Mega Sales Event Happening at Greenway Kia West Palm Beach!” — Jun 18, 2026), which means someone with listing-owner access posts to Google regularly. Who posts, with what tool (Sprout or other), and on what cadence per channel — TO VERIFY — request from client via Shannon McNeil. |

---

## TAB — Store 02: Greenway Kia at the Avenues

| Field | Value |
|---|---|
| Market | Jacksonville, FL |
| General Manager | Emre Sevinir |
| Address (Google Maps listing) | 10564 Philips Hwy, Jacksonville, FL 32256 ([S01]) |
| Phone / Website | (904) 650-2999 / greenwaykiaattheavenues.com ([S01]) |
| GM background | GM identity verified from owner (client master record [S03]); public-source corroboration: search engines (Google/Bing/DDG) and DealerRater were blocked from the research environment on 2026-08-12, so a second independent public source could not be retrieved this session — TO VERIFY — request from client via Shannon McNeil (two-source rule, OPERATING_RULES §3.5). |

### Bucket 1 — Accounts & Access Inventory

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google Business Profile (GBP) | OBSERVED (public): Google Maps listing exists for “Greenway Kia at The Avenues” with a live GBP owner-post stream (latest: Owner post on GBP listing: “Check out These Amazing Offers at Greenway Kia at The Avenues” — posted ~6 days before audit date (Aug 6, 2026)). This shows listing-owner access is active on GBP, but does not confirm who holds it (store staff vs vendor) or tool used. TO VERIFY — request from client via Shannon McNeil. |
| Facebook | BLOCKER — Facebook page existence/ownership. Owner: Shannon McNeil. Needed: FB page URL + admin list (Meta Business Manager). FB blocks automated fetch — manual verification needed — 2026-08-12. |
| Instagram | BLOCKER — Instagram handle/ownership. Owner: Shannon McNeil. Needed: IG handle + access. IG blocks automated fetch — manual verification needed — 2026-08-12. |
| TikTok | BLOCKER — TikTok account/ownership. Owner: Shannon McNeil. Needed: TikTok handle + access. TikTok blocks automated fetch — manual verification needed — 2026-08-12. |
| YouTube | BLOCKER — YouTube channel/ownership. Owner: Shannon McNeil. Needed: channel URL + Studio access. Channel-level data requires Studio/API — manual verification needed — 2026-08-12. |
| Reddit | BLOCKER — Reddit presence/ownership. Owner: Shannon McNeil. Needed: any store-controlled u/ or r/ accounts. Reddit blocked automated search from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Cross-channel access & vendor split | BLOCKER — accounts & access inventory. Owner: Shannon McNeil (store data/access, per CLIENT.md §8.1) and Shawn Vink (corporate IT/admin access where applicable). Needed: per-channel handles/URLs, active/inactive status, login access and admin-role list per account (Meta Business Manager, Google Business Profile, TikTok, YouTube, Reddit), and the split between store staff and outside vendors. This is the biggest Month 1 timeline risk; until it clears, no performance or ownership cell below can be verified. Public-page review only is possible without access. |

### Bucket 2 — Performance Baselines (per channel)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| All 6 channels — reach/impressions/engagement baselines | BLOCKER — performance baselines. Owner: Shannon McNeil. Needed: native-insights access per channel (Meta Business Suite for FB/IG, TikTok Analytics, YouTube Studio, GBP Insights) granted per-account; corporate access via Shawn Vink where applicable. Platform notes: TikTok and Facebook block automated retrieval manual verification needed — 2026-08-12; YouTube channel-level data requires Studio/API access; GBP Insights requires listing-owner access. A failed fetch is not evidence an account does not exist. |
| Public-visible baseline (GBP) | OBSERVED (public): GBP listing rating 4.6/5 at audit date; full review count and Insights (searches, calls, direction requests) require listing-owner access — TO VERIFY — request from client via Shannon McNeil. |
| Public-visible baseline (YouTube/FB/IG/TikTok) | Follower/subscriber counts are public on YouTube, but channel-level data is blocked from automated fetch — manual verification needed — 2026-08-12. FB/IG/TikTok counts also blocked — manual verification needed — 2026-08-12. No numbers stated rather than inventing them. |

### Bucket 3 — Reputation (Reddit, Google, DealerRater, Cars.com, Edmunds, Yelp)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google reviews | OBSERVED (public): Google rating 4.6/5 on the store's Google Maps listing at audit date. Review count and review-response behavior not visible in Google Maps' limited view — require listing-owner access or manual review — TO VERIFY — request from client via Shannon McNeil/manual verification needed — 2026-08-12. |
| DealerRater | BLOCKED — DealerRater rating/review count/response count. DealerRater returned HTTP 403 (CloudFront) from this environment on 2026-08-12 — manual verification needed — 2026-08-12. DealerRater presence/absence is NOT confirmed either way. |
| Cars.com | BLOCKED — Cars.com rating/review count. Cars.com blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Edmunds | BLOCKED — Edmunds rating/review count. Edmunds blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Yelp | BLOCKED — Yelp rating/review count. Yelp blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Reddit | ABSENCE-OBSERVED (framed as absence, not complaints): no organic Reddit footprint for “Greenway Kia at The Avenues” was retrievable programmatically — Reddit blocked automated search on 2026-08-12 (manual verification needed — 2026-08-12). Per operator context, four of five rooftops have no organic Reddit footprint and zero dealership responses to public complaints — to be confirmed per-store via manual Reddit check + Apify scraper once MCP access is granted. |
| Review-response pattern | STRUCTURAL FINDING (operator context, confirm in audit): named individual staff drive nearly all positive reviews at every rooftop — a dependency on staff members, not the store brand (CLIENT.md §9). Hold for one-on-one GM conversation; frame as absence, not complaint list. |

### Bucket 4 — Search Presence

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Exact brand+market query | OBSERVED (public): searching Google Maps for the store name “Greenway Kia at The Avenues” returns the store's own listing as the top/only business result with address, phone, and website — the store surfaces for its exact brand + market on Google Maps. [S01] |
| Generic category query (map pack) | Generic query test (e.g., “Kia dealer near [market]”) blocked — Google web search returned an anti-bot page from this environment on 2026-08-12 (manual verification needed — 2026-08-12). Map-pack position for generic category queries: TO VERIFY via manual search or a research tool (Exa/Apify) once granted. |
| Website | Website from listing: greenwaykiaattheavenues.com (verified on the Google Maps listing panel). Website/site-search standing TO VERIFY — Google search blocked this session (manual verification needed — 2026-08-12). |

### Bucket 5 — Competitive Benchmarking (local market)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Competitor set (per-market) | BLOCKED this session — Google/Bing/DDG web search all returned anti-bot or captcha pages from this environment on 2026-08-12 (manual verification needed — 2026-08-12); DealerRater also blocked (HTTP 403). Competitor list for Jacksonville, FL (Kia dealers in the Palm Beach metro for Store 01; Kia dealers in the Jacksonville metro for Store 02; Kia dealers in the Nashville metro for Stores 03–04; Ford dealers in the Kansas City metro for Store 05) and their Google ratings are TO VERIFY — request research re-run with Exa/Apify MCP once granted, or manual check. |
| Benchmark context | Benchmarks for scoring are ready in audit/BENCHMARKS.md (BrightLocal 2026 review study; Rival IQ 2025 engagement trends — [S04]). These are directional, not pass/fail. |

### Bucket 6 — Current Operations Workflow

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Current poster(s), tool(s), cadence | BLOCKER — operations workflow (who posts today, with what tool, on what cadence). Owner: Shannon McNeil. Needed: store answers (per CLIENT.md §8) on current poster(s), tool(s) (Sprout/other scheduler or native app), posting cadence per channel, and whether a vendor currently manages any account. |
| Public signal (GBP posting) | OBSERVED (public): the GBP listing for “Greenway Kia at The Avenues” has recent owner posts (latest: Owner post on GBP listing: “Check out These Amazing Offers at Greenway Kia at The Avenues” — posted ~6 days before audit date (Aug 6, 2026)), which means someone with listing-owner access posts to Google regularly. Who posts, with what tool (Sprout or other), and on what cadence per channel — TO VERIFY — request from client via Shannon McNeil. |

---

## TAB — Store 03: Greenway Kia Rivergate

| Field | Value |
|---|---|
| Market | Madison, TN |
| General Manager | James Galuszka |
| Address (Google Maps listing) | 1536 Gallatin Pike N, Madison, TN 37115 ([S01]) |
| Phone / Website | (615) 806-7213 / greenwaykiarivergate.com ([S01]) |
| GM background | GM identity verified from owner (client master record [S03]); public-source corroboration: search engines (Google/Bing/DDG) and DealerRater were blocked from the research environment on 2026-08-12, so a second independent public source could not be retrieved this session — TO VERIFY — request from client via Shannon McNeil (two-source rule, OPERATING_RULES §3.5). |

### Bucket 1 — Accounts & Access Inventory

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google Business Profile (GBP) | OBSERVED (public): Google Maps listing exists for “Greenway Kia of Rivergate” with a live GBP owner-post stream (latest: Owner post on GBP listing: “Used 2024 Kia Sorento LX … Finance for $352/mo” — posted ~4 days before audit date (Aug 8, 2026)). This shows listing-owner access is active on GBP, but does not confirm who holds it (store staff vs vendor) or tool used. TO VERIFY — request from client via Shannon McNeil. |
| Facebook | BLOCKER — Facebook page existence/ownership. Owner: Shannon McNeil. Needed: FB page URL + admin list (Meta Business Manager). FB blocks automated fetch — manual verification needed — 2026-08-12. |
| Instagram | BLOCKER — Instagram handle/ownership. Owner: Shannon McNeil. Needed: IG handle + access. IG blocks automated fetch — manual verification needed — 2026-08-12. |
| TikTok | BLOCKER — TikTok account/ownership. Owner: Shannon McNeil. Needed: TikTok handle + access. TikTok blocks automated fetch — manual verification needed — 2026-08-12. |
| YouTube | BLOCKER — YouTube channel/ownership. Owner: Shannon McNeil. Needed: channel URL + Studio access. Channel-level data requires Studio/API — manual verification needed — 2026-08-12. |
| Reddit | BLOCKER — Reddit presence/ownership. Owner: Shannon McNeil. Needed: any store-controlled u/ or r/ accounts. Reddit blocked automated search from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Cross-channel access & vendor split | BLOCKER — accounts & access inventory. Owner: Shannon McNeil (store data/access, per CLIENT.md §8.1) and Shawn Vink (corporate IT/admin access where applicable). Needed: per-channel handles/URLs, active/inactive status, login access and admin-role list per account (Meta Business Manager, Google Business Profile, TikTok, YouTube, Reddit), and the split between store staff and outside vendors. This is the biggest Month 1 timeline risk; until it clears, no performance or ownership cell below can be verified. Public-page review only is possible without access. |

### Bucket 2 — Performance Baselines (per channel)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| All 6 channels — reach/impressions/engagement baselines | BLOCKER — performance baselines. Owner: Shannon McNeil. Needed: native-insights access per channel (Meta Business Suite for FB/IG, TikTok Analytics, YouTube Studio, GBP Insights) granted per-account; corporate access via Shawn Vink where applicable. Platform notes: TikTok and Facebook block automated retrieval manual verification needed — 2026-08-12; YouTube channel-level data requires Studio/API access; GBP Insights requires listing-owner access. A failed fetch is not evidence an account does not exist. |
| Public-visible baseline (GBP) | OBSERVED (public): GBP listing rating 4.4/5 at audit date; full review count and Insights (searches, calls, direction requests) require listing-owner access — TO VERIFY — request from client via Shannon McNeil. |
| Public-visible baseline (YouTube/FB/IG/TikTok) | Follower/subscriber counts are public on YouTube, but channel-level data is blocked from automated fetch — manual verification needed — 2026-08-12. FB/IG/TikTok counts also blocked — manual verification needed — 2026-08-12. No numbers stated rather than inventing them. |

### Bucket 3 — Reputation (Reddit, Google, DealerRater, Cars.com, Edmunds, Yelp)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google reviews | OBSERVED (public): Google rating 4.4/5 on the store's Google Maps listing at audit date. Review count and review-response behavior not visible in Google Maps' limited view — require listing-owner access or manual review — TO VERIFY — request from client via Shannon McNeil/manual verification needed — 2026-08-12. |
| DealerRater | BLOCKED — DealerRater rating/review count/response count. DealerRater returned HTTP 403 (CloudFront) from this environment on 2026-08-12 — manual verification needed — 2026-08-12. DealerRater presence/absence is NOT confirmed either way. |
| Cars.com | BLOCKED — Cars.com rating/review count. Cars.com blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Edmunds | BLOCKED — Edmunds rating/review count. Edmunds blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Yelp | BLOCKED — Yelp rating/review count. Yelp blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Reddit | ABSENCE-OBSERVED (framed as absence, not complaints): no organic Reddit footprint for “Greenway Kia of Rivergate” was retrievable programmatically — Reddit blocked automated search on 2026-08-12 (manual verification needed — 2026-08-12). Per operator context, four of five rooftops have no organic Reddit footprint and zero dealership responses to public complaints — to be confirmed per-store via manual Reddit check + Apify scraper once MCP access is granted. |
| Review-response pattern | STRUCTURAL FINDING (operator context, confirm in audit): named individual staff drive nearly all positive reviews at every rooftop — a dependency on staff members, not the store brand (CLIENT.md §9). Hold for one-on-one GM conversation; frame as absence, not complaint list. |

### Bucket 4 — Search Presence

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Exact brand+market query | OBSERVED (public): searching Google Maps for the store name “Greenway Kia of Rivergate” returns the store's own listing as the top/only business result with address, phone, and website — the store surfaces for its exact brand + market on Google Maps. [S01] |
| Generic category query (map pack) | Generic query test (e.g., “Kia dealer near [market]”) blocked — Google web search returned an anti-bot page from this environment on 2026-08-12 (manual verification needed — 2026-08-12). Map-pack position for generic category queries: TO VERIFY via manual search or a research tool (Exa/Apify) once granted. |
| Website | Website from listing: greenwaykiarivergate.com (verified on the Google Maps listing panel). Website/site-search standing TO VERIFY — Google search blocked this session (manual verification needed — 2026-08-12). |

### Bucket 5 — Competitive Benchmarking (local market)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Competitor set (per-market) | BLOCKED this session — Google/Bing/DDG web search all returned anti-bot or captcha pages from this environment on 2026-08-12 (manual verification needed — 2026-08-12); DealerRater also blocked (HTTP 403). Competitor list for Madison, TN (Kia dealers in the Palm Beach metro for Store 01; Kia dealers in the Jacksonville metro for Store 02; Kia dealers in the Nashville metro for Stores 03–04; Ford dealers in the Kansas City metro for Store 05) and their Google ratings are TO VERIFY — request research re-run with Exa/Apify MCP once granted, or manual check. |
| Benchmark context | Benchmarks for scoring are ready in audit/BENCHMARKS.md (BrightLocal 2026 review study; Rival IQ 2025 engagement trends — [S04]). These are directional, not pass/fail. |

### Bucket 6 — Current Operations Workflow

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Current poster(s), tool(s), cadence | BLOCKER — operations workflow (who posts today, with what tool, on what cadence). Owner: Shannon McNeil. Needed: store answers (per CLIENT.md §8) on current poster(s), tool(s) (Sprout/other scheduler or native app), posting cadence per channel, and whether a vendor currently manages any account. |
| Public signal (GBP posting) | OBSERVED (public): the GBP listing for “Greenway Kia of Rivergate” has recent owner posts (latest: Owner post on GBP listing: “Used 2024 Kia Sorento LX … Finance for $352/mo” — posted ~4 days before audit date (Aug 8, 2026)), which means someone with listing-owner access posts to Google regularly. Who posts, with what tool (Sprout or other), and on what cadence per channel — TO VERIFY — request from client via Shannon McNeil. |

---

## TAB — Store 04: Greenway Kia Hickory Hollow

| Field | Value |
|---|---|
| Market | Antioch, TN |
| General Manager | James Galuszka |
| Address (Google Maps listing) | 5406 Target Dr, Antioch, TN 37013 ([S01]) |
| Phone / Website | (615) 206-3017 / greenwaykiahickoryhollow.com ([S01]) |
| GM background | GM identity verified from owner (client master record [S03]); public-source corroboration: search engines (Google/Bing/DDG) and DealerRater were blocked from the research environment on 2026-08-12, so a second independent public source could not be retrieved this session — TO VERIFY — request from client via Shannon McNeil (two-source rule, OPERATING_RULES §3.5). |

### Bucket 1 — Accounts & Access Inventory

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google Business Profile (GBP) | OBSERVED (public): Google Maps listing exists for “Greenway Kia of Hickory Hollow” with a live GBP owner-post stream (latest: Owner post on GBP listing: “Check Out This Month’s New Vehicle Specials at Greenway Kia Hickory Hollow!” — Jul 14, 2026). This shows listing-owner access is active on GBP, but does not confirm who holds it (store staff vs vendor) or tool used. TO VERIFY — request from client via Shannon McNeil. |
| Facebook | BLOCKER — Facebook page existence/ownership. Owner: Shannon McNeil. Needed: FB page URL + admin list (Meta Business Manager). FB blocks automated fetch — manual verification needed — 2026-08-12. |
| Instagram | BLOCKER — Instagram handle/ownership. Owner: Shannon McNeil. Needed: IG handle + access. IG blocks automated fetch — manual verification needed — 2026-08-12. |
| TikTok | BLOCKER — TikTok account/ownership. Owner: Shannon McNeil. Needed: TikTok handle + access. TikTok blocks automated fetch — manual verification needed — 2026-08-12. |
| YouTube | BLOCKER — YouTube channel/ownership. Owner: Shannon McNeil. Needed: channel URL + Studio access. Channel-level data requires Studio/API — manual verification needed — 2026-08-12. |
| Reddit | BLOCKER — Reddit presence/ownership. Owner: Shannon McNeil. Needed: any store-controlled u/ or r/ accounts. Reddit blocked automated search from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Cross-channel access & vendor split | BLOCKER — accounts & access inventory. Owner: Shannon McNeil (store data/access, per CLIENT.md §8.1) and Shawn Vink (corporate IT/admin access where applicable). Needed: per-channel handles/URLs, active/inactive status, login access and admin-role list per account (Meta Business Manager, Google Business Profile, TikTok, YouTube, Reddit), and the split between store staff and outside vendors. This is the biggest Month 1 timeline risk; until it clears, no performance or ownership cell below can be verified. Public-page review only is possible without access. |

### Bucket 2 — Performance Baselines (per channel)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| All 6 channels — reach/impressions/engagement baselines | BLOCKER — performance baselines. Owner: Shannon McNeil. Needed: native-insights access per channel (Meta Business Suite for FB/IG, TikTok Analytics, YouTube Studio, GBP Insights) granted per-account; corporate access via Shawn Vink where applicable. Platform notes: TikTok and Facebook block automated retrieval manual verification needed — 2026-08-12; YouTube channel-level data requires Studio/API access; GBP Insights requires listing-owner access. A failed fetch is not evidence an account does not exist. |
| Public-visible baseline (GBP) | OBSERVED (public): GBP listing rating 4.3/5 at audit date; full review count and Insights (searches, calls, direction requests) require listing-owner access — TO VERIFY — request from client via Shannon McNeil. |
| Public-visible baseline (YouTube/FB/IG/TikTok) | Follower/subscriber counts are public on YouTube, but channel-level data is blocked from automated fetch — manual verification needed — 2026-08-12. FB/IG/TikTok counts also blocked — manual verification needed — 2026-08-12. No numbers stated rather than inventing them. |

### Bucket 3 — Reputation (Reddit, Google, DealerRater, Cars.com, Edmunds, Yelp)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google reviews | OBSERVED (public): Google rating 4.3/5 on the store's Google Maps listing at audit date. Review count and review-response behavior not visible in Google Maps' limited view — require listing-owner access or manual review — TO VERIFY — request from client via Shannon McNeil/manual verification needed — 2026-08-12. |
| DealerRater | BLOCKED — DealerRater rating/review count/response count. DealerRater returned HTTP 403 (CloudFront) from this environment on 2026-08-12 — manual verification needed — 2026-08-12. DealerRater presence/absence is NOT confirmed either way. |
| Cars.com | BLOCKED — Cars.com rating/review count. Cars.com blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Edmunds | BLOCKED — Edmunds rating/review count. Edmunds blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Yelp | BLOCKED — Yelp rating/review count. Yelp blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Reddit | ABSENCE-OBSERVED (framed as absence, not complaints): no organic Reddit footprint for “Greenway Kia of Hickory Hollow” was retrievable programmatically — Reddit blocked automated search on 2026-08-12 (manual verification needed — 2026-08-12). Per operator context, four of five rooftops have no organic Reddit footprint and zero dealership responses to public complaints — to be confirmed per-store via manual Reddit check + Apify scraper once MCP access is granted. |
| Review-response pattern | STRUCTURAL FINDING (operator context, confirm in audit): named individual staff drive nearly all positive reviews at every rooftop — a dependency on staff members, not the store brand (CLIENT.md §9). Hold for one-on-one GM conversation; frame as absence, not complaint list. |

### Bucket 4 — Search Presence

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Exact brand+market query | OBSERVED (public): searching Google Maps for the store name “Greenway Kia of Hickory Hollow” returns the store's own listing as the top/only business result with address, phone, and website — the store surfaces for its exact brand + market on Google Maps. [S01] |
| Generic category query (map pack) | Generic query test (e.g., “Kia dealer near [market]”) blocked — Google web search returned an anti-bot page from this environment on 2026-08-12 (manual verification needed — 2026-08-12). Map-pack position for generic category queries: TO VERIFY via manual search or a research tool (Exa/Apify) once granted. |
| Website | Website from listing: greenwaykiahickoryhollow.com (verified on the Google Maps listing panel). Website/site-search standing TO VERIFY — Google search blocked this session (manual verification needed — 2026-08-12). |

### Bucket 5 — Competitive Benchmarking (local market)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Competitor set (per-market) | BLOCKED this session — Google/Bing/DDG web search all returned anti-bot or captcha pages from this environment on 2026-08-12 (manual verification needed — 2026-08-12); DealerRater also blocked (HTTP 403). Competitor list for Antioch, TN (Kia dealers in the Palm Beach metro for Store 01; Kia dealers in the Jacksonville metro for Store 02; Kia dealers in the Nashville metro for Stores 03–04; Ford dealers in the Kansas City metro for Store 05) and their Google ratings are TO VERIFY — request research re-run with Exa/Apify MCP once granted, or manual check. |
| Benchmark context | Benchmarks for scoring are ready in audit/BENCHMARKS.md (BrightLocal 2026 review study; Rival IQ 2025 engagement trends — [S04]). These are directional, not pass/fail. |

### Bucket 6 — Current Operations Workflow

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Current poster(s), tool(s), cadence | BLOCKER — operations workflow (who posts today, with what tool, on what cadence). Owner: Shannon McNeil. Needed: store answers (per CLIENT.md §8) on current poster(s), tool(s) (Sprout/other scheduler or native app), posting cadence per channel, and whether a vendor currently manages any account. |
| Public signal (GBP posting) | OBSERVED (public): the GBP listing for “Greenway Kia of Hickory Hollow” has recent owner posts (latest: Owner post on GBP listing: “Check Out This Month’s New Vehicle Specials at Greenway Kia Hickory Hollow!” — Jul 14, 2026), which means someone with listing-owner access posts to Google regularly. Who posts, with what tool (Sprout or other), and on what cadence per channel — TO VERIFY — request from client via Shannon McNeil. |

---

## TAB — Store 05: Greenway Ford Kansas City

| Field | Value |
|---|---|
| Market | Raytown, MO |
| General Manager | Shane Silvey |
| Address (Google Maps listing) | 9505 E 350 Hwy, Raytown, MO 64133 ([S01]) |
| Phone / Website | (816) 353-1495 / greenwayfordkc.com ([S01]) |
| GM background | GM identity verified from owner (client master record [S03]); public-source corroboration: search engines (Google/Bing/DDG) and DealerRater were blocked from the research environment on 2026-08-12, so a second independent public source could not be retrieved this session — TO VERIFY — request from client via Shannon McNeil (two-source rule, OPERATING_RULES §3.5). |

### Bucket 1 — Accounts & Access Inventory

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google Business Profile (GBP) | OBSERVED (public): Google Maps listing exists for “Greenway Ford” with a live GBP owner-post stream (latest: Owner post on GBP listing: “The Ford Summer Sales Event is happening now at Greenway Ford of Raytown! …” — posted ~2 days before audit date (Aug 10, 2026)). This shows listing-owner access is active on GBP, but does not confirm who holds it (store staff vs vendor) or tool used. TO VERIFY — request from client via Shannon McNeil. |
| Facebook | BLOCKER — Facebook page existence/ownership. Owner: Shannon McNeil. Needed: FB page URL + admin list (Meta Business Manager). FB blocks automated fetch — manual verification needed — 2026-08-12. |
| Instagram | BLOCKER — Instagram handle/ownership. Owner: Shannon McNeil. Needed: IG handle + access. IG blocks automated fetch — manual verification needed — 2026-08-12. |
| TikTok | BLOCKER — TikTok account/ownership. Owner: Shannon McNeil. Needed: TikTok handle + access. TikTok blocks automated fetch — manual verification needed — 2026-08-12. |
| YouTube | BLOCKER — YouTube channel/ownership. Owner: Shannon McNeil. Needed: channel URL + Studio access. Channel-level data requires Studio/API — manual verification needed — 2026-08-12. |
| Reddit | BLOCKER — Reddit presence/ownership. Owner: Shannon McNeil. Needed: any store-controlled u/ or r/ accounts. Reddit blocked automated search from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Cross-channel access & vendor split | BLOCKER — accounts & access inventory. Owner: Shannon McNeil (store data/access, per CLIENT.md §8.1) and Shawn Vink (corporate IT/admin access where applicable). Needed: per-channel handles/URLs, active/inactive status, login access and admin-role list per account (Meta Business Manager, Google Business Profile, TikTok, YouTube, Reddit), and the split between store staff and outside vendors. This is the biggest Month 1 timeline risk; until it clears, no performance or ownership cell below can be verified. Public-page review only is possible without access. |

### Bucket 2 — Performance Baselines (per channel)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| All 6 channels — reach/impressions/engagement baselines | BLOCKER — performance baselines. Owner: Shannon McNeil. Needed: native-insights access per channel (Meta Business Suite for FB/IG, TikTok Analytics, YouTube Studio, GBP Insights) granted per-account; corporate access via Shawn Vink where applicable. Platform notes: TikTok and Facebook block automated retrieval manual verification needed — 2026-08-12; YouTube channel-level data requires Studio/API access; GBP Insights requires listing-owner access. A failed fetch is not evidence an account does not exist. |
| Public-visible baseline (GBP) | OBSERVED (public): GBP listing rating 4.3/5 at audit date; full review count and Insights (searches, calls, direction requests) require listing-owner access — TO VERIFY — request from client via Shannon McNeil. |
| Public-visible baseline (YouTube/FB/IG/TikTok) | Follower/subscriber counts are public on YouTube, but channel-level data is blocked from automated fetch — manual verification needed — 2026-08-12. FB/IG/TikTok counts also blocked — manual verification needed — 2026-08-12. No numbers stated rather than inventing them. |

### Bucket 3 — Reputation (Reddit, Google, DealerRater, Cars.com, Edmunds, Yelp)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Google reviews | OBSERVED (public): Google rating 4.3/5 on the store's Google Maps listing at audit date. Review count and review-response behavior not visible in Google Maps' limited view — require listing-owner access or manual review — TO VERIFY — request from client via Shannon McNeil/manual verification needed — 2026-08-12. |
| DealerRater | BLOCKED — DealerRater rating/review count/response count. DealerRater returned HTTP 403 (CloudFront) from this environment on 2026-08-12 — manual verification needed — 2026-08-12. DealerRater presence/absence is NOT confirmed either way. |
| Cars.com | BLOCKED — Cars.com rating/review count. Cars.com blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Edmunds | BLOCKED — Edmunds rating/review count. Edmunds blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Yelp | BLOCKED — Yelp rating/review count. Yelp blocked automated fetch from this environment on 2026-08-12 — manual verification needed — 2026-08-12. |
| Reddit | ABSENCE-OBSERVED (framed as absence, not complaints): no organic Reddit footprint for “Greenway Ford” was retrievable programmatically — Reddit blocked automated search on 2026-08-12 (manual verification needed — 2026-08-12). Per operator context, four of five rooftops have no organic Reddit footprint and zero dealership responses to public complaints — to be confirmed per-store via manual Reddit check + Apify scraper once MCP access is granted. |
| Review-response pattern | STRUCTURAL FINDING (operator context, confirm in audit): named individual staff drive nearly all positive reviews at every rooftop — a dependency on staff members, not the store brand (CLIENT.md §9). Hold for one-on-one GM conversation; frame as absence, not complaint list. |

### Bucket 4 — Search Presence

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Exact brand+market query | OBSERVED (public): searching Google Maps for the store name “Greenway Ford” returns the store's own listing as the top/only business result with address, phone, and website — the store surfaces for its exact brand + market on Google Maps. [S01] |
| Generic category query (map pack) | Generic query test (e.g., “Kia dealer near [market]”) blocked — Google web search returned an anti-bot page from this environment on 2026-08-12 (manual verification needed — 2026-08-12). Map-pack position for generic category queries: TO VERIFY via manual search or a research tool (Exa/Apify) once granted. |
| Website | Website from listing: greenwayfordkc.com (verified on the Google Maps listing panel). Website/site-search standing TO VERIFY — Google search blocked this session (manual verification needed — 2026-08-12). |

### Bucket 5 — Competitive Benchmarking (local market)

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Competitor set (per-market) | BLOCKED this session — Google/Bing/DDG web search all returned anti-bot or captcha pages from this environment on 2026-08-12 (manual verification needed — 2026-08-12); DealerRater also blocked (HTTP 403). Competitor list for Raytown, MO (Kia dealers in the Palm Beach metro for Store 01; Kia dealers in the Jacksonville metro for Store 02; Kia dealers in the Nashville metro for Stores 03–04; Ford dealers in the Kansas City metro for Store 05) and their Google ratings are TO VERIFY — request research re-run with Exa/Apify MCP once granted, or manual check. |
| Benchmark context | Benchmarks for scoring are ready in audit/BENCHMARKS.md (BrightLocal 2026 review study; Rival IQ 2025 engagement trends — [S04]). These are directional, not pass/fail. |

### Bucket 6 — Current Operations Workflow

| Item | Finding / Blocker (owner · what's needed) |
|---|---|
| Current poster(s), tool(s), cadence | BLOCKER — operations workflow (who posts today, with what tool, on what cadence). Owner: Shannon McNeil. Needed: store answers (per CLIENT.md §8) on current poster(s), tool(s) (Sprout/other scheduler or native app), posting cadence per channel, and whether a vendor currently manages any account. |
| Public signal (GBP posting) | OBSERVED (public): the GBP listing for “Greenway Ford” has recent owner posts (latest: Owner post on GBP listing: “The Ford Summer Sales Event is happening now at Greenway Ford of Raytown! …” — posted ~2 days before audit date (Aug 10, 2026)), which means someone with listing-owner access posts to Google regularly. Who posts, with what tool (Sprout or other), and on what cadence per channel — TO VERIFY — request from client via Shannon McNeil. |

---