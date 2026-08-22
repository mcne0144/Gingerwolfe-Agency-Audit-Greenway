# PAID_MEDIA_FRAMEWORK.md — Per-Store, Per-Channel Paid Media Strategy (Greenway Auto Group)

**Status: INTERNAL DRAFT — not client-facing until Shannon McNeil approves**
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Paid Media Specialist)
**Applies to:** Greenway Auto Group pilot — 5 rooftops (Store 01–05). Paid is a PROPOSAL layer on top of the six-month ORGANIC pilot. The signed SOW is organic-only.

---

## 0. THE HARD LINE (non-negotiable — read before anything else)

> **No agent launches, funds, modifies, or manages live ad spend, and no agent touches any existing Greenway ad account (including Facebook paid, where Greenway-side contact Brennan has an informal role) without the operator's explicit confirmation that scope has expanded and access has been granted.**
>
> Every step in this workspace that would touch a live account or spend carries the gate:
> **"BLOCKED until operator confirms scope expansion + access."**
>
> The client retainer ($10,000/month flat, $2,000/rooftop) is the **SERVICE FEE**, not media spend. **Every budget in this file is a PROPOSAL for Shannon's and the client's approval — never presented as real spend, never quoted to a GM as a fact.** No agent ever pitches or prices services to anyone at Greenway (`OPERATING_RULES.md` §2.4). Openings go into the Expansion Signals log; the operator decides what gets raised, when, and with whom.

---

## 1. What this document is

The team's paid-media strategy for Greenway Auto Group: how paid would layer onto the organic pilot, per store and per channel (Meta = Facebook + Instagram, TikTok, Reddit, YouTube/Google). It contains:

1. The layering model — how paid plugs into the organic machine (§2)
2. Campaign objectives mapped to dealer goals (§3)
3. Per-store, per-channel paid strategy with per-store geo-targeting (§4)
4. Audience and creative test plans (§5)
5. TikTok and Reddit channel-entry analyses (§6, §7)
6. YouTube/Google entry notes (§8)
7. Budget pacing framework — **PROPOSAL-ONLY** (§9)
8. The combined paid+organic reporting view (§10)
9. Guardrails and drift flags (§11)
10. Sources and verification status (§12)

**Nothing here is live.** No store has run, is running, or will run a paid campaign through this team until Shannon McNeil confirms expanded scope and access. Every store-specific number that needs client data is marked **TO VERIFY — request from client via Shannon McNeil**.

**Relationship to the workspace:** organic content (`content/`) feeds ad creative; the KPI framework (`reporting/`) measures results; budgets flow to Shannon for approval; nothing runs without her sign-off; openings from this analysis go into `expansion-signals.md` via the operator.

---

## 2. The layering model — how paid sits on top of the organic pilot

Paid is not a separate machine. It amplifies what the organic pilot already produces. Five layers, in the order they should be tested (all **PROPOSAL** — nothing runs without scope expansion + access):

| Layer | What it is | Organic input it uses | Ad objective (platform) | GM-visible outcome it feeds |
|---|---|---|---|---|
| 1. **Boost the winners** | Amplify the store's top-performing organic posts (by saves, shares, intent comments) to a wider local radius | The store's own proven content — no new creative needed | Engagement (Meta), Video views (TikTok Spark Ads) | Reach (K1), engagement (K3), saves (K6) |
| 2. **Local reach extension** | Show the store's real posts to people within the store's market who have not organically seen them | Calendar content: inventory, service, community posts | Awareness/Reach (Meta, TikTok, Reddit, YouTube) | Reach (K1), profile visits (K11), GBP profile views (K17) |
| 3. **GBP action ads** | Drive calls, directions, and website clicks from the store's Google Business Profile | Real store proof: rating, reviews, photos, address | Local actions (Meta), Local campaigns (Google) | Calls (K19), directions (K18), website clicks (K20) |
| 4. **Lead forms** | Capture name + phone/email in-app for service appointments and sales inquiries | Service reminders, inventory spotlights with real (TO VERIFY) vehicles | Leads (Meta Lead Ads, TikTok Lead Gen, Reddit, YouTube) | New inquiry stream — aligns with DMs (K9), calls (K19); conversion to sale is the store's data (TO VERIFY) |
| 5. **Retargeting (later phase)** | Re-show ads to people who visited the store's site or engaged with its posts | Site visitors (pixel — **BLOCKED**: pixel install needs scope + access) | Traffic/Conversions (Meta, Google) | Website clicks (K20), leads |

**Sequencing logic:** Layers 1–2 start first (cheap, reuse organic content, low risk). Layer 3 follows once GBP access confirms the store's listing health. Layer 4 needs a lead-handling answer from the store (who answers the form, how fast — `BENCHMARKS.md` §3: response speed converts). Layer 5 is gated on pixel installation and site access — **BLOCKED** until expanded scope.

**When NOT to boost:** never boost a post that has not earned organic traction (below the store's own median engagement), never boost posts with unverified inventory or offers, and never boost into a radius wider than the store's actual service area without operator approval (`OPERATING_RULES.md` §9–10 — store findings stay one-on-one; a boost that surfaces sensitive material publicly would violate this).

---

## 3. Campaign objectives mapped to dealer goals

Store-level goals for the pilot are **TO VERIFY — request from client via Shannon McNeil** (`CLIENT.md` §8.2). Until they arrive, this table is the mapping the team will apply once goals are known. Objectives are stated in plain language, then matched to platform objectives.

| Dealer goal (TO VERIFY per store) | Platform objective to choose | Ad KPI it drives | Maps to existing KPI |
|---|---|---|---|
| More calls to the store | Local actions / Calls (Meta, Google Local) | Calls, call-through rate | K19 Calls (GBP) |
| More people walking in | Directions (Meta, Google) | Direction requests | K18 Direction requests |
| More service appointments | Leads (Meta Lead Ads, TikTok Lead Gen), Messages | Leads, DMs | K9 DMs / messages |
| More sales inquiries / inventory views | Traffic to website, Leads | Link clicks, CTR, CPC | K12 Link taps, K20 Website clicks |
| Awareness in the local market | Awareness/Reach (all platforms) | Impressions, reach, CPM | K1 Reach, K2 Impressions |
| Deeper engagement with existing audience | Engagement (Meta), Video views (TikTok) | CTR, engagement rate | K3 Engagement rate, K13 Views |
| More Google reviews (proof) | Traffic to GBP (Meta Local/Promote-to-profile) | Profile actions, review velocity (contextual) | K17 Profile views, K21 Review volume |

**Attribution caveat (unchanged from `KPI_FRAMEWORK.md` §5):** the pilot measures social and profile activity, not closed sales. Paid extends the same discipline: the report shows what the ads produced (reach, clicks, leads, calls, directions) and never claims sales outcomes. Whether the store tracks lead-to-sale conversion is **TO VERIFY**.

---

## 4. Per-store, per-channel paid strategy

**Rule: per-store campaigns, never one national group campaign.** Each rooftop gets its own ad account structure (or its own campaign set within a client-level Business Manager — decision **TO VERIFY** with Shannon/Shawn Vink once access exists), its own geo-targeting around its own address, its own budget proposal, and its own creative built from its own content.

Geo-targeting baseline (house default — a proposal, not a sourced claim): a **25-mile radius around the store's street address**, tightened or widened after the audit shows where the store's customers actually come from (GBP Insights direction requests, once access lands — **TO VERIFY**). Store 03 and Store 04 are separate rooftops, separate addresses, same GM — **separate campaigns with distinct radius sets**; overlap handling (mutual exclusion vs. shared delivery) is a **TO VERIFY** decision with the operator, since the same GM reads both scorecards.

Store context below uses **observed public data only** from `audit/workbook/` (2026-08-12). No store facts are invented.

### 4.1 Store 01 — Greenway Kia West Palm Beach (GM Mike Wangle, West Palm Beach, FL)

- **Observed context:** GBP 4.5★; listing owner posts observed through Jun 18, 2026, then quiet at audit (`GM_KPI_FRAMEWORK.md` §2.1). Address: 735 S Military Trl Ste C, West Palm Beach, FL 33415.
- **First paid layer (proposal):** Layer 2 — local reach extension, then Layer 1 boosts as organic content resumes. The store's own listing presence went quiet; paid reach buys back visibility while the organic calendar restarts. **Do not boost anything until the organic calendar is live again** — boosting silence is wasted money.
- **Meta:** Awareness/Reach, 25-mile radius around 735 S Military Trl. Audience: 25–60, interests in Kia + comparable brands (interests **TO VERIFY** against Business Manager audience sizes once access exists). Creative: real local photos (photo posts are the standout Facebook format — `BENCHMARKS.md` §1.3).
- **TikTok:** entry test (see §6) with the store's own authentic video once the store produces any (cadence house default 3–5/wk — `CONTENT_STRATEGY_FRAMEWORK.md` §6.3).
- **Reddit:** entry test (see §7) only after subreddit fit is confirmed for the Palm Beach metro — fit is **TO VERIFY** via manual Reddit search/Apify (BLOCKERS.md #6).
- **GBP actions (Layer 3):** once GBP owner access confirms the listing, a Local-actions campaign to the 4.5★ listing. Freshness gap is the one-on-one framing for the GM (`OPERATING_RULES.md` §10), not a paid complaint.
- **Store-specific gate:** no creative with inventory/offers until the store provides a verified inventory feed (`CLIENT.md` §8.2 — **TO VERIFY**).

### 4.2 Store 02 — Greenway Kia at the Avenues (GM Emre Sevinir, Jacksonville, FL)

- **Observed context:** GBP 4.6★ — highest of the five; listing posts current (Aug 6, 2026) (`GM_KPI_FRAMEWORK.md` §2.2). Address: 10564 Philips Hwy, Jacksonville, FL 32256.
- **First paid layer (proposal):** Layer 4 lead forms for service + sales, layered on a store with an actively managed listing and the pilot's best rating — the strongest starting reputation for paid. Also Layer 3 GBP actions.
- **Meta:** Leads (service appointment + sales inquiry), 25–30-mile radius around 10564 Philips Hwy. Jacksonville is a dense metro; a wider radius is justifiable once GBP Insights shows where directions come from (**TO VERIFY**).
- **TikTok:** entry test — Jacksonville skews younger than the pilot's Ford store; the Avenues' current posting discipline gives Spark Ads content to work with.
- **Reddit:** entry test after subreddit fit check for the Jacksonville metro (**TO VERIFY**).
- **Lead-handling prerequisite (TO VERIFY via Shannon):** who answers lead-form submissions and how fast. Response speed is the conversion lever (`BENCHMARKS.md` §3.1 — 55% of consumers contact brands via Facebook; Meta's responsiveness badge rewards ≥90% response).

### 4.3 Store 03 — Greenway Kia Rivergate (GM James Galuszka, Madison, TN)

- **Observed context:** GBP 4.4★; listing posts current (Aug 8, 2026). Nashville metro is the pilot's busiest market (`GM_KPI_FRAMEWORK.md` §2.3). Address: 1536 Gallatin Pike N, Madison, TN 37115.
- **First paid layer (proposal):** Layer 2 awareness + Layer 4 leads. Biggest metro = the best awareness math; competitive Kia market means paid presence here fights for map-pack share.
- **Meta:** Awareness + Leads, 25-mile radius around 1536 Gallatin Pike N.
- **TikTok:** entry test — Nashville's demographic skew supports it; the store's own short video once cadence is live.
- **Reddit:** r/Nashville-type fit check (**TO VERIFY** — subreddit fit must be confirmed before any Reddit activity, paid or organic — `BENCHMARKS.md` §5).
- **Sister-store note:** Store 03 and Store 04 share a GM but are separate markets (Madison vs Antioch). Keep campaigns separate; the GM reads both scorecards side by side.

### 4.4 Store 04 — Greenway Kia Hickory Hollow (GM James Galuszka, Antioch, TN)

- **Observed context:** GBP 4.3★ — lower end of the pilot band; listing posts observed through Jul 14, 2026, then quiet at audit (`GM_KPI_FRAMEWORK.md` §2.4). Address: 5406 Target Dr, Antioch, TN 37013.
- **First paid layer (proposal):** Layer 1 boosts once the organic calendar is live, plus Layer 3 GBP actions to the 4.3★ listing. Reputation framing is absence, not complaint (`OPERATING_RULES.md` §10): paid here carries the store's real proof (reviews, delivery stories) rather than price hype.
- **Meta:** Engagement + Local actions, 25-mile radius around 5406 Target Dr.
- **TikTok/Reddit:** entry tests only after the store's organic presence is consistently live — do not pay for reach on channels where the store has no organic footing yet (freshness gap first, one-on-one with the GM).
- **Store-specific gate:** no ad creative that could read as compensating for the quiet listing period; ads amplify the new organic rhythm only.

### 4.5 Store 05 — Greenway Ford Kansas City (GM Shane Silvey, Raytown, MO)

- **Observed context:** GBP 4.3★; listing posts current (Aug 10, 2026 — most recent of the five). Only Ford rooftop — different OEM, different buyer base (`GM_KPI_FRAMEWORK.md` §2.5). Split, likely unmanaged second Google listing "Greenway Ford Service" (4.1★, 436 reviews) beside the main listing (`expansion-signals.md`). Address: 9505 E 350 Hwy, Raytown, MO 64133.
- **First paid layer (proposal):** Layer 3 GBP actions + Layer 2 local reach on **Meta (Facebook first) and Google/YouTube** — Ford's buyer base skews older than Kia's, so Facebook and Google are the primary paid surfaces; TikTok is the last channel for this store, not the first (`GM_KPI_FRAMEWORK.md` §2.5).
- **Meta:** Local actions + Reach, 25–30-mile radius around 9505 E 350 Hwy (Raytown is a suburb — the Kansas City metro spread justifies the wider end; **TO VERIFY** once GBP Insights lands).
- **Google/YouTube:** see §8 — local search volume for "Ford dealer Kansas City" type queries is **TO VERIFY** via keyword research (Google Ads Keyword Planner needs account access — **BLOCKED**).
- **Reddit:** r/kansascity fit check (**TO VERIFY**); lower priority than Meta/Google for this buyer base.
- **Store-specific note:** the split "Greenway Ford Service" listing is a reviews/reputation signal already logged (`expansion-signals.md`) — paid ads pointing at a fragmented listing risk splitting the proof; listing consolidation is the Reviews & reputation priority, paid follows it.

---

## 5. Audience and creative test plans

**Testing discipline (house rules):** one variable per test, minimum two weeks per cell, budgets as proposals only, decisions on trend not snapshot (`KPI_FRAMEWORK.md` §1.7), and every test labeled in the report as a proposal test with its dates. Nothing is a "winner" on one day.

### 5.1 Audience test plan

| # | Test | Platform | Structure (proposal) | Decision rule (read after ≥2 wks) |
|---|---|---|---|---|
| A1 | Radius width | Meta, TikTok | Same creative, two ad groups: 15-mile vs 25-mile radius around store address | Keep the radius whose cost-per-valuable-action (call, direction, lead, or CTR on link ads) is better; report both |
| A2 | Age band | Meta, TikTok | Same creative: 25–44 vs 45–65 | Keep the band with better CTR/engagement; note this decides TikTok (younger) vs Facebook (older) weight per store |
| A3 | Interest vs broad local | Meta | Same creative: interest stack (model/brand interests — **TO VERIFY** sizes) vs no interests, geo-only | Keep the one with lower CPM at equal CTR; broad-local often wins for dealerships but must be tested per store |
| A4 | Community + keyword | Reddit | Same ad: r/[city] + [city/car] keywords vs keywords only | Keep the targeting with better CTR and lower negative sentiment (comments matter on Reddit) |
| A5 | Spark vs standard video | TikTok | Same video, two ad groups: Spark Ad (boosts store's organic post) vs standard in-feed | Spark usually wins on engagement (social proof) — confirm per store |

All audience sizes and interest names must be **TO VERIFY** at build time inside the real ad accounts (access **BLOCKED** until scope expansion). No audience numbers are stated here because none can be verified without account access — the audit's per-market research (`audit/workbook/` Bucket 5, blocked this session) will fill competitor and market context when re-run.

### 5.2 Creative test plan

**Creative source rule:** ad creative is built from the store's OWN organic content (`content/` calendar + creative briefs). No stock photography passed off as the lot, no invented offers, no unverified vehicles (`CONTENT_STRATEGY_FRAMEWORK.md` §4: honest first; inventory must be verifiably on the lot).

| # | Test | Hook type | Format | Platform | Measure |
|---|---|---|---|---|---|
| C1 | Photo vs video | "Real lot today" vs "30-second walkaround" | Photo post vs Reel/Spark video | Meta, TikTok | CTR, engagement rate, saves (K6) |
| C2 | Service tip vs inventory | "When to rotate tires in [market]" vs "[Model] on the lot" | Video (≤30s) | TikTok, YouTube Shorts, Meta | Saves (K6), views (K13), watch time (K14), lead forms |
| C3 | People vs product | Staff face/delivery-day vs car-only | Video | Meta, TikTok | CTR, comments (K8) — intent comments flagged |
| C4 | Proof vs price | Review/delivery story vs price-led (price **TO VERIFY**) | Image/carousel | Meta, Reddit | CTR, directions (K18), calls (K19) |
| C5 | CTA test | "Call the store" vs "Get directions" vs "Send us a message" | Same creative, 3 CTA variants | Meta (Local ads) | Calls (K19) vs directions (K18) vs DMs (K9) |

**Boost rule (Layer 1):** only boost posts that cleared the store's own organic median for saves/shares/intent comments in the prior 14 days. A post that did not earn organic traction is not worth paying to show twice.

---

## 6. TikTok channel-entry analysis

### 6.1 Why dealership presence is thin on TikTok

- **Organic:** most dealership TikTok accounts are dormant or reposted Facebook content; the platform rewards authentic short video, which dealerships historically do not produce at cadence. Platform-wide engagement is falling (TikTok −34% YoY — Rival IQ 2025, `BENCHMARKS.md` §1.1), which has discouraged casual entrants while concentrating attention on consistent creators.
- **Paid:** TikTok for Business exists and is well-documented, but dealership ad budgets have historically followed Meta and Google. The result is thinner paid competition in most local markets — the core reason the operator prioritized TikTok for this pilot.
- **Verification note:** dealership-specific TikTok ad statistics could not be sourced from a reputable named study at time of writing. **No dealership-specific TikTok numbers are stated here** (same discipline as `BENCHMARKS.md` §7). What follows is platform-documented capability and a house test plan, not industry benchmarks.

### 6.2 Entry cost and fit considerations

- **Budget floors (third-party study citing TikTok's enforced minimums, fetched live 2026-08-12):** TikTok Ads Manager requires a **campaign minimum of $50/day (or lifetime total) and an ad-group minimum of $20/day** — Sprout Social, "How much do TikTok ads cost," https://sproutsocial.com/insights/tiktok-ads/ (label: third-party marketing content citing platform guidance — re-verify against TikTok's own help at build time, as the help center blocked automated fetch on 2026-08-12).
  - Implication for a store-level test: TikTok tests must be planned as **short bursts** (e.g., $50/day × 6 days = $300) or a lifetime budget ≥ $50 spread over days, not as dribs and drabs. This is a proposal-planning fact, not a spend commitment.
- **Ad formats that fit a dealership (platform-documented, via Sprout Social, same URL):**
  - **Spark Ads** — sponsor the store's OWN organic video and run it as an ad; it keeps the author's handle and existing engagement visible. This is the direct paid-on-organic bridge for the pilot: the store posts organically, the top-performing organic video becomes the Spark Ad.
  - **In-feed video ads** — standard vertical video; entry format.
  - **Keyword-based (Search) ads** — show when users search car-related terms; captures high-intent, but requires keyword planning (**TO VERIFY** inside TikTok Ads Manager — **BLOCKED** until access).
  - TikTok **Lead Gen** for form capture (service appointments) — fits Layer 4.
- **Fit per store:** strongest for the four Kia stores (younger-skewing buyer base) and weakest for Store 05 Ford (older buyer base — `GM_KPI_FRAMEWORK.md` §2.5). Nashville (Store 03/04) and Jacksonville (Store 02) metros have the demographic fit; West Palm Beach (Store 01) is a retirement-heavy market — TikTok test size smaller, decision on evidence.
- **Creative reality check:** TikTok ads are video; a store with no organic video cadence yet has nothing worth sponsoring. Entry is gated on the organic calendar being live (house default 3–5 videos/wk per store — `CONTENT_STRATEGY_FRAMEWORK.md` §8).

### 6.3 What a first TikTok test looks like (PROPOSAL — nothing runs without scope expansion + access)

1. Store produces organic videos per its calendar for ≥3 weeks (its own phone video, sound-on captions, on-screen text — `CONTENT_STRATEGY_FRAMEWORK.md` §6.3).
2. Team picks the top organic video by saves/views (evidence, not vibes).
3. Proposal to Shannon: one Spark Ad, 25-mile radius around the store address, age band per store's audience test (A2), **$50/day × 6 days = $300 lifetime** (proposal only).
4. Objective: Video views / Engagement first (learn), not Leads (conviction requires data).
5. Read after 14 days: views (K13), engagement (K3), profile visits (K11), CTR, CPM — vs the same store's organic baseline. Decide scale/hold/kill on trend.
6. **Every live step BLOCKED until operator confirms scope expansion + access.**

---

## 7. Reddit channel-entry analysis

### 7.1 Why dealership presence is thin on Reddit

- **Organic:** Reddit's Reddiquette is explicit — far more participating than promoting; "it's not okay to be a website with a redditor account" (`BENCHMARKS.md` §5). A dealership account that posts offers in local/car subreddits gets removed and can hurt the store. Most dealerships never attempt it, or attempt it once, get removed, and leave. Four of five pilot rooftops have no organic Reddit footprint (operator context, confirm per-store — BLOCKERS.md #6).
- **Paid:** Reddit Ads is a smaller, younger ad surface than Meta/Google, and local businesses rarely use it. The operator's thesis — competition is thin, entry cost is low — holds for paid as well, with one caveat: Reddit users are advertisement-averse and will say so in the comments. The cost of entry is not money; it is the discipline to advertise in Reddit's native voice (community-first, useful, no hype).
- **Verification note:** no reputable independent study of dealership-level Reddit ad performance could be cited at time of writing. **No dealership-specific Reddit numbers are stated here** (`BENCHMARKS.md` §7 discipline). Platform facts below are labeled by source type.

### 7.2 Entry cost and fit considerations

- **Platform scale (platform-published marketing site, fetched live 2026-08-12):** Reddit reports **490M+ weekly active users** and **100,000+ active communities**; ad types include **Carousel, Image, Video, and Conversations Ads**; targeting is **layered (communities, keywords, interests)**; and Reddit Pro (free) offers profile/keyword tracking for engagement — Reddit for Business, https://www.redditforbusiness.com/ (label: platform-published marketing content — treat audience claims as vendor claims, not independent research; re-verify at build time).
- **Budget floors:** Reddit's official budget FAQ (https://support.reddithelp.com/hc/en-us/articles/360062135032-Ad-budget-and-billing-faqs) is **Cloudflare-blocked from this environment — manual verification needed — 2026-08-12**. Reddit's own site advertises ad-credit programs (e.g., credit tiers tied to spend, per redditforbusiness.com fetched 2026-08-12 — terms **TO VERIFY** at build). **No minimum-budget figure is stated here** until the official page is read; the pilot's proposal is deliberately built small regardless (see §9).
- **The right ad for a dealership:** a **Conversations Ad** (an ad that looks like a Reddit post, with a discussion underneath) or a **community-targeted carousel**, not a banner. The first test's creative should read like a genuinely useful local answer ("what Kia service customers in [metro] ask us most"), not an ad. This mirrors the organic voice rules (`CONTENT_STRATEGY_FRAMEWORK.md` §6.5).
- **Fit per store:** r/[metro] subreddits exist for the pilot's markets, but **subreddit fit must be confirmed before ANY Reddit activity, paid or organic** (`BENCHMARKS.md` §5) — which subreddits exist for each metro, their rules on promotion, and their car-specific communities. This is **TO VERIFY** via manual search + Apify scraper (BLOCKERS.md #6) — Reddit blocked automated search on 2026-08-12.

### 7.3 What a first Reddit test looks like (PROPOSAL — nothing runs without scope expansion + access)

1. Confirm subreddit fit per metro (**TO VERIFY**): r/[city] subs for West Palm Beach, Jacksonville, Nashville, Kansas City + car communities; read each sub's rules on ads/promotion.
2. Proposal to Shannon: one campaign, community + keyword targeting (city + car terms), a Conversations-style ad written in Reddit's voice, budget **$150–$250/month per store (proposal only)**, 25-mile-relevant targeting where Reddit's geo options allow (Reddit targets by location — confirm options **TO VERIFY** at build).
3. Objective: reach + engagement (upvotes/comments are the scoreboard), NOT hard lead capture at first.
4. Read after 14 days: CTR, comments and upvotes, negative sentiment (Reddit users will say if it is an ad-flop), K16 participation health (if the store's organic account is involved, removals must be zero — `KPI_FRAMEWORK.md` §4.5).
5. **Every live step BLOCKED until operator confirms scope expansion + access.** Also: Reddit ads run from a Reddit business/ads account, separate from any organic u/ account; account structure decision **TO VERIFY** with Shannon.

---

## 8. YouTube / Google entry notes

- **Role:** YouTube is the depth channel in the organic pilot (Shorts for discovery, long-form for value — `BENCHMARKS.md` §6). Paid on Google/YouTube makes sense where the store's market searches — "Kia dealer near me," "[model] service [city]" — and where the store has video worth amplifying.
- **Formats:** YouTube in-stream (skippable) video ads built from the store's real walkarounds; **Google Local campaigns** for store visits/actions (calls, directions) — the paid counterpart to GBP actions; Search ads only after keyword research shows volume (**TO VERIFY** — Google Ads Keyword Planner requires account access, **BLOCKED**).
- **Existing-account risk (hard line):** Greenway-side contact Brennan has an informal role in Facebook paid, and the group may hold existing Google Ads or Meta ad accounts. **No agent touches any existing account** — including pausing, editing, or "peeking" at campaigns — without explicit operator confirmation of scope expansion + access. Any drift flag goes to the operator (§11).
- **Priority per store:** Store 05 (Ford, older buyer base) — Google/YouTube before TikTok. Store 02 and Store 03 — YouTube Shorts amplification once the stores produce Shorts (1 Short/wk house default — `CONTENT_STRATEGY_FRAMEWORK.md` §8).
- **Budget proposal:** Google/YouTube tests are a later-phase proposal (after Meta/TikTok/Reddit layers prove out), sized per store — see §9.

---

## 9. Budget pacing framework — **PROPOSAL-ONLY**

**Every figure in this section is a PROPOSAL for Shannon's and the client's approval. Nothing here is real spend, and the retainer is not media spend.** Budgets are never quoted to a GM as facts; the expansion conversation at Month 6 is the place where the operator decides what a store's paid budget might be (`OPERATING_RULES.md` §2.4).

### 9.1 Pacing principles

1. **Test small, scale on evidence.** Start every store at a test budget; scale only after 14-day trend reads.
2. **Platform minimums shape the plan, not the reverse.** TikTok's $50/day campaign floor (third-party citing TikTok — §6.2) means TikTok tests are bursts, not drips. Reddit's floor is **TO VERIFY** (official page blocked — §7.2). Meta has no published daily minimum (house note: practical floor is a few dollars/day; confirm in the platform at build).
3. **The organic machine must be live first.** Paid amplifies organic; it does not replace it. No paid test on a channel where the store has no organic rhythm (decision discipline per store in §4).
4. **All money labels are PROPOSAL / PROJECTION.** Monthly readouts label spend as "proposed test budget" until real campaigns exist, then as "platform-reported spend" (only after scope expansion + access).

### 9.2 Worked example — one store's monthly paid budget proposal (PROPOSAL ONLY)

Hypothetical shape for **one** store once the operator confirms scope expansion + access. Not a quote, not an invoice — a planning example Shannon could take to a GM. Sizes are house proposals; the actual number is Shannon's call with the client.

| Line | Layer | Platform | Monthly proposal | Notes |
|---|---|---|---|---|
| 1 | Boost winners | Meta | $400 | 2–3 boosted top organic posts/wk |
| 2 | Local reach | Meta | $200 | Reach extension, 25-mile radius |
| 3 | Entry test | TikTok | $300 | 1 Spark Ad, $50/day × 6 days (platform floor) |
| 4 | Entry test | Reddit | $200 | Community + keyword, Conversations-style |
| 5 | Contingency | — | $100 | Only for scaling a proven cell; never spent by default |
| | **Total/store/month** | | **$1,200 (PROPOSAL)** | = 60% of the store's $2,000/month service fee — deliberately modest relative to the retail value of even one sale or a handful of service visits; grows only on evidence |

**Pacing calendar (proposal):** Month 1 of any paid expansion = lines 1–2 only (boost + local reach on Meta, where the stores already have organic footing). Month 2 = add TikTok burst (line 3) where store video exists, and Reddit test (line 4) where subreddit fit is confirmed. Month 3 = scale or kill each line on 14-day trend reads; contingency (line 5) only for proven cells.

**Read-and-respond cadence (aligned to `GM_KPI_FRAMEWORK.md` §4):** weekly internal pacing check (team working notes: spend pace vs proposal, any drift), monthly in the GM report (paid+organic combined view — §10), quarterly trend view (end of Months 3 and 6).

---

## 10. The combined paid+organic reporting view

**Goal:** one page where the operator can show a GM the FULL traction of a campaign — what organic did and what paid added — without mixing the two numbers into a false single figure.

### 10.1 Combined view per store per month (GM-readable table)

| Row (plain language) | Organic (K-number) | Paid (ad KPI) | Combined note |
|---|---|---|---|
| People who saw the store's content | K1 Reach (native insights) | Paid reach (platform reports) | Report side by side, never summed as one reach number (overlap unknown until platform dedup; **TO VERIFY** tooling) |
| Times content was shown | K2 Impressions | Paid impressions | Same |
| Interactions | K3 Engagement rate; K6 saves; K7 shares; K8 comments | Ad CTR, engagement (boosts/Spark) | CTR = clicks ÷ impressions (platform-standard, defined at first capture — **TO VERIFY** in-platform) |
| Inquiries | K9 DMs/messages | Lead-form leads (LD-1), ad clicks-to-message | Family of inquiry signals — reported as a group, each labeled by source; never blended into "total leads" without Shannon's sign-off on definitions |
| Calls | K19 Calls (GBP) | Ad calls (call ads) | Both labeled by source; GBP Insights vs platform call reporting may double-count — flag, don't guess |
| Directions / visits intent | K18 Direction requests | Ad "get directions" actions | Same caution |
| Website clicks | K20 Website clicks (GBP), K12 link taps | CPC, ad link clicks | Cost per click is a budget-efficiency number, not a result |
| Proof | K21 Review volume & rating | Review-related ad views (contextual only) | Ads never promise reviews; they surface the store's real proof |
| Cost efficiency | — | CPM, CPC, cost per lead (proposed) | Labeled PROPOSAL/actual-by-platform; only real after scope expansion |

**New ad-side metric definitions (house, to be confirmed with the Reporting Analyst — they extend, never replace, the K-number set):**
- **CTR** = ad link clicks ÷ ad impressions × 100 (standard platform definition; used with K12).
- **CPM** = ad cost ÷ ad impressions × 1,000 (budget efficiency; pairs with K2).
- **CPC** = ad cost ÷ ad link clicks (budget efficiency; pairs with K12/K20).
- **LD-1 Leads** = lead-form submissions (Meta Lead Ads, TikTok Lead Gen) — an inquiry signal in the K9 family.
- **GBP actions from ads** = calls/directions/website clicks attributed to paid in platform reporting — reconciled against K19/K18/K20 with a note on double-count risk.

**Guardrails for the combined view (same as `GM_KPI_FRAMEWORK.md` §5):** real numbers only with capture date and source; cells that cannot be captured stay TO VERIFY; no blended totals without approved definitions; no group averages; no sales claims; every number labeled organic vs paid vs proposal-projection.

### 10.2 The story a GM can read

1. **"Here is what the store posted organically and what it earned."** (K1–K8 rows)
2. **"Here is what paid added on top."** (paid rows)
3. **"Here is what came in: calls, directions, messages, lead forms."** (inquiry family)
4. **"Here is what we spent — a proposal, your call."** (budget row, PROPOSAL label)
5. **"Here is what we learned."** (which creative/audience/CTA to scale, hold, or kill)

---

## 11. Guardrails and drift flags

### 11.1 The hard line (restated — `OPERATING_RULES.md` §3, `CLIENT.md` §9)

- No agent launches, funds, modifies, or manages live ad spend.
- No agent touches any existing Greenway ad account (Meta, Google, TikTok, Reddit, or any other) without the operator's explicit confirmation that scope has expanded and access has been granted. This includes Facebook paid (Brennan's informal role — scope not defined; the hard line applies).
- Every step that would touch a live account or spend carries: **"BLOCKED until operator confirms scope expansion + access."**
- The retainer is the SERVICE FEE. Every budget is a PROPOSAL. Nothing is presented as real spend or as a result.

### 11.2 Drift flags — escalate to the operator immediately

1. Anyone at Greenway asks to "just boost this post" or "throw $X at Facebook" — even a GM's own initiative. Route to Shannon; do not execute, do not draft the boost.
2. Brennan or anyone on the client side proposes coordinating paid with the team. Refer to Shannon; no coordination, no account access discussions.
3. Any agent or teammate is asked to log into an existing ad account, pause/scale an existing campaign, or install a pixel. **BLOCKED** — scope expansion + access only via Shannon (pixel install also touches the store website — separate access via Shawn Vink where applicable).
4. An "auto-applied" campaign appears (Meta/Google occasionally auto-apply recommendations). Flag; never accept, never dismiss silently.
5. A proposed budget starts being discussed with a GM before Shannon has approved the proposal. Stop; budgets are proposals for Shannon's approval, and agents never price services to the client (§9.1).
6. Any inclination to "just run a small test to see" without the gate. The gate is unconditional.

---

## 12. Sources and verification status

All benchmark claims in this document are labeled by source type per `OPERATING_RULES.md` §3.6. Where a page could not be read on 2026-08-12, it is marked **manual verification needed — 2026-08-12**.

| # | Source | Cited for | Type | Verification |
|---|---|---|---|---|
| 1 | Sprout Social, "How much do TikTok ads cost" — https://sproutsocial.com/insights/tiktok-ads/ | TikTok campaign min $50/day, ad group min $20/day (as enforced by TikTok); Spark Ads; keyword/search ads; TikTok Promote | Third-party marketing content citing platform guidance | **Verified live 2026-08-12** (page fetched and read) |
| 2 | Reddit for Business — https://www.redditforbusiness.com/ | 490M+ weekly active users; 100k+ active communities; ad types (Carousel, Image, Video, Conversations); layered community/keyword targeting; Reddit Pro; ad-credit program | Platform-published marketing content (vendor claims) | **Verified live 2026-08-12** (page fetched and read) |
| 3 | Reddit Help, "Ad budget and billing FAQs" — https://support.reddithelp.com/hc/en-us/articles/360062135032-Ad-budget-and-billing-faqs | Reddit minimum budgets (not stated here pending read) | Platform-published | **Blocked (Cloudflare) — manual verification needed — 2026-08-12** |
| 4 | TikTok For Business, "Ad specifications" — https://ads.tiktok.com/business/help/article/tiktok-ad-specifications | Ad specs (formats, duration) | Platform-published | **Blocked (403 from this environment) — manual verification needed — 2026-08-12; re-verify at build time** |
| 5 | Meta Business Help Center — https://www.facebook.com/business/help/ | Responsiveness badge (≥90% messages); page messaging | Platform-published | Canonical doc — re-verify before client use (`BENCHMARKS.md` §8) |
| 6 | `audit/BENCHMARKS.md` | Organic engagement trends (Rival IQ 2025), review norms (BrightLocal 2026), Reddit Reddiquette, YouTube format rules | Source-verified benchmark file (see its §8) | Verified 2026-08-12 (see file) |
| 7 | `reporting/KPI_FRAMEWORK.md`, `reporting/GM_KPI_FRAMEWORK.md` | K-number definitions, GM/COO view, cadence, guardrails | Team working docs | Current 2026-08-12 |
| 8 | `audit/workbook/` (store-01..05 audit.csv, BLOCKERS.md) | Observed store context: GBP ratings, listing-post dates, addresses | Observed public data | 2026-08-12 (see workbook) |

**Explicit non-findings (nothing invented):** no dealership-specific TikTok or Reddit ad benchmarks exist in a verifiable, reputable named study at time of writing — none are stated here. Reddit's minimum budget is not stated (official page blocked). TikTok ad specs are not restated beyond what Sprout verified (official specs page 403'd). Where this document needed a number and none could be verified, it set a **house default** labeled as such (radius widths, budget sizes, cadence) — these are proposals for Shannon to approve, never research.

**Re-verify at execution:** platform minimums, ad formats, and targeting options change. Before any build (post-scope-expansion), re-check the cited pages and confirm limits inside the real ad accounts.

---

*End of framework. INTERNAL DRAFT — nothing here runs, and nothing leaves the team, until Shannon McNeil approves. No one on the Bright Matter team contacts the store directly.*
