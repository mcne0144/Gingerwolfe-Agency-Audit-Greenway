# KPI_FRAMEWORK.md — Per-Store, Per-Channel KPI & Measurement Framework for Organic Social

**Status:** INTERNAL DRAFT — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Reporting Analyst)
**Applies to:** Greenway Auto Group pilot — 5 rooftops (Store 01–05) × 6 channels each
(Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile)

---

## 0. What this document is

This is the team's measurement framework for the six-month organic social pilot. It defines:

1. **The KPI set** — every number we track, what it means, how it is measured, and where the data comes from.
2. **What matters most to a dealership General Manager** — the handful of numbers the monthly report leads with.
3. **Measurement cadence** — which KPIs are checked weekly, monthly, and quarterly.
4. **Guardrails** — only real, verifiable numbers go into reports; data gaps are flagged, never guessed.

**The unit of measurement is one store × one channel — never the group.** Every KPI is defined and reported per store (Store 01–05) and per channel (Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile). There is no "Greenway average" in any report; a number that applies to one store is stated for that store.

**No real store data exists yet.** Until Shannon McNeil provides the items in `CLIENT.md` §8 (handles, account access, ownership, goals), every store-specific figure in the tracking sheets and reports is marked:

> **TO VERIFY — request from client via Shannon McNeil**

This framework is the machine that turns real data into GM-readable reports once that data arrives.

---

## 1. Guardrails — how we treat numbers (non-negotiable)

These rules apply to every KPI, dashboard cell, and report line in the pilot:

1. **Only real, verifiable numbers go in reports.** A number in a report must come from (a) platform-native insights pulled directly by the team, (b) a public page captured with a date and screenshot, or (c) the store via Shannon McNeil. Nothing else.
2. **Data gaps are flagged, never guessed.** If a number cannot be obtained this month, the cell says **TO VERIFY — request from client via Shannon McNeil** (or "Not available — access pending"), and it goes on the report's request list. An estimate is never substituted for a missing number — not even a labeled one.
3. **Every number carries a capture date and a source.** Follower counts, ratings, and reach change daily. The dashboard's notes column and the report's appendix record when each number was pulled and from where (e.g., "Meta Business Suite, captured 2026-09-01").
4. **Per store, per channel — no group blur.** KPIs are reported for one store on one channel. Aggregating across stores (or summing followers across channels) creates a number no single dealership can act on and is not used.
5. **Benchmarks are directional, not pass/fail.** We compare a store's numbers to `audit/BENCHMARKS.md` and to its own history and goals — never to a pass/fail line. Context always accompanies a comparison (e.g., small-market follower base, platform-wide engagement decline).
6. **House targets are labeled as house rules.** Where no published benchmark exists, the team sets a target (e.g., respond to 100% of new reviews within 2 business days). Such targets are labeled **house target — for Shannon to confirm**, never presented as research. See §8.
7. **Trend beats single snapshot.** One month means nothing; the pilot's 6-month arc is the measure. Movement is always reported with the previous month's number and the platform trend where relevant.
8. **No invented metrics.** Every KPI below maps to a real, measurable platform signal. If we can't measure it, we don't report it — we flag it as a data gap.

---

## 2. KPI set at a glance

Every KPI in the framework. Full definitions in §3–§4; data sources in §7; cadence in §6.

| # | KPI | Channel(s) | Plain-language meaning | Data source |
|---|---|---|---|---|
| K1 | **Reach** | FB, IG, TikTok, YouTube | How many different accounts saw the store's content | Native insights |
| K2 | **Impressions** | FB, IG, TikTok, YouTube | How many times content was shown (one account can count many times) | Native insights |
| K3 | **Engagement rate** | FB, IG, TikTok, YouTube | Share of impressions that turned into an interaction (like, comment, share, save) | Computed from native insights |
| K4 | **Follower growth** | All 6 | How many people chose to follow/subscribe during the month (net) | Native insights + public counts |
| K5 | **Posts published** | FB, IG, TikTok, YouTube, GBP | How much content went out, vs. the plan in the content calendar | Calendar + native insights |
| K6 | **Saves** | FB, IG, TikTok | People bookmarking content to come back — a strong intent signal | Native insights |
| K7 | **Shares** | FB, IG, TikTok, YouTube | Forwards of content to others | Native insights |
| K8 | **Comments** | FB, IG, TikTok, YouTube, Reddit | Public conversation under the store's content; comments with intent (price, availability, hours) are lead signals | Native insights / public pages |
| K9 | **DMs / messages received** | FB, IG, TikTok, Reddit | Private conversations — often real sales or service inquiries | Native inbox (access via Shannon) |
| K10 | **Message response (rate/time)** | FB, IG, TikTok, Reddit | Whether the store answers messages, and how fast | Native inbox (Meta reports this directly) |
| K11 | **Profile visits** | FB, IG, TikTok, YouTube | People who clicked into the profile after seeing content | Native insights |
| K12 | **Link taps** | FB, IG, TikTok | Clicks on the bio/page link (to website, inventory, or booking) | Native insights |
| K13 | **Views** | TikTok, YouTube | Times video content was watched | Native insights |
| K14 | **Watch time** | YouTube | Total hours viewers spent watching the channel's videos | YouTube Studio |
| K15 | **Subscribers** | YouTube | Channel subscribers (end of month + net new) | YouTube Studio |
| K16 | **Participation health** | Reddit | Whether the store participates genuinely, fits subreddit norms, and avoids removals | Manual/public tracking; removal data needs mod access |
| K17 | **Profile views (GBP)** | Google Business Profile | Times people viewed the profile on Google Search and Maps | GBP Insights |
| K18 | **Direction requests** | Google Business Profile | "Get directions" clicks — intent to visit the lot | GBP Insights |
| K19 | **Calls** | Google Business Profile | Phone calls placed from the profile | GBP Insights |
| K20 | **Website clicks** | Google Business Profile | Clicks to the store's website from the profile | GBP Insights |
| K21 | **Review volume & rating** | Google Business Profile | New reviews received and the average star rating | Public profile + GBP Insights |
| K22 | **Review & Q&A response** | Google Business Profile | Whether the store responds to reviews and profile questions, and how fast | GBP Insights / manual |
| K23 | **Photos added** | Google Business Profile | Fresh visual proof (lot, showroom, service) added during the month | Public profile |

KPI numbers match the column names in `DASHBOARD_TEMPLATE.md` and the rows in `REPORTING_TEMPLATE.md`, so a number is defined once and flows everywhere.

---

## 3. Core KPIs — cross-channel definitions

Applies to Facebook, Instagram, TikTok, and YouTube unless a row says otherwise.

### K1 — Reach
- **What it is:** the number of different accounts that saw the store's content in the month (platform-defined; duplicates removed).
- **How measured:** read directly from native insights (Meta Business Suite, TikTok Analytics, YouTube Studio).
- **Why it matters to a GM:** awareness — how many people in (and beyond) the store's market the channel touched. The number the store can grow with consistent posting and real local content.

### K2 — Impressions
- **What it is:** total times content was shown; one account can count multiple impressions.
- **How measured:** read directly from native insights.
- **Why it matters:** reach × frequency. Impressions rising faster than reach usually means the same people are being shown more content (loyal audience) rather than new people seeing the store.

### K3 — Engagement rate
- **What it is:** the share of people who saw a post and interacted with it.
- **Formula (matches `audit/BENCHMARKS.md` §1):** (total interactions ÷ impressions) × 100. Interactions = likes/reactions + comments + shares + saves (YouTube: likes + comments + shares).
- **How measured:** computed from native-insight numbers in the dashboard; the denominator (impressions, or reach where impressions are unavailable) is recorded in the notes column.
- **Why it matters:** the best single read on whether content *resonates* with the audience. **Read as a trend, not a number** — engagement rates fell year-over-year on every major platform (Facebook −36%, Instagram −16%, TikTok −34% — Rival IQ 2025, `BENCHMARKS.md` §1.1), so a static or gently declining rate is normal. No automotive-specific engagement medians are published; Retail is the closest labeled proxy (`BENCHMARKS.md` §1.2, §7).

### K4 — Follower growth
- **What it is:** followers/subscribers at month end, and the net change during the month.
- **How measured:** end-of-month count minus end-of-previous-month count, both captured on the same day from native insights/public profile.
- **Why it matters:** the audience the store can reach organically in future — an asset. Growth is compared to content output (more posts → more chances to be followed) and to the platform trend.

### K5 — Posts published
- **What it is:** count of posts/videos/stories (as applicable) published in the month.
- **How measured:** from the content calendar (`content/calendars/store-XX/`) reconciled with native insights.
- **Why it matters:** cadence is the input the team controls. Compared against the house-default cadence (`content/CONTENT_STRATEGY_FRAMEWORK.md` §8; `BENCHMARKS.md` §2) and against the monthly content-mix check.

### K6 — Saves (FB, IG, TikTok)
- **What it is:** times people saved/bookmarked a post.
- **How measured:** native insights.
- **Why it matters:** saving is a private, deliberate act — "I want to find this again" (a car, a price, a service tip). Saves are the strongest engagement signal the audit framework treats as intent (`AUDIT_FRAMEWORK.md` §4.2).

### K7 — Shares
- **What it is:** times content was forwarded/shared.
- **How measured:** native insights.
- **Why it matters:** free word-of-mouth reach — one share shows the post to people the store hasn't reached.

### K8 — Comments
- **What it is:** public comments received during the month.
- **How measured:** native insights; intent comments (price, availability, trade-in, hours) flagged manually in the dashboard notes.
- **Why it matters:** public conversation, and a lead channel — a comment asking "how much?" or "is this still available?" is a real inquiry. Every comment should get a reply (see K10 and `BENCHMARKS.md` §3).

### K9 — DMs / messages received (FB, IG, TikTok, Reddit)
- **What it is:** private messages received during the month (page inbox on FB/IG, TikTok messages, Reddit messages).
- **How measured:** native inbox. **Access to inboxes is TO VERIFY — request from client via Shannon McNeil.**
- **Why it matters:** the closest thing to a direct lead number on social. 55% of consumers use Facebook to contact brands (Sprout Social, `BENCHMARKS.md` §3.1) — messages are a sales channel, not a chore.

### K10 — Message response (rate and time)
- **What it is:** share of messages answered and typical response time.
- **How measured:** Meta Business Suite reports response rate and average response time directly; TikTok/Reddit tracked manually from the inbox.
- **Why it matters:** responsiveness converts inquiries. Meta pages that respond to ≥90% of messages can earn a "Very responsive" badge (`BENCHMARKS.md` §3.1). House rule: answer messages the same business day.

### K11 — Profile visits
- **What it is:** times people clicked into the profile page after seeing content.
- **How measured:** native insights.
- **Why it matters:** the step between "saw content" and "checking the store out" — a consideration signal.

### K12 — Link taps (FB, IG, TikTok)
- **What it is:** clicks on the profile link (bio link, website button).
- **How measured:** native insights.
- **Why it matters:** the path from social to the store's website/inventory. Requires a working, current link on the profile (audit dimension D2, `AUDIT_FRAMEWORK.md` §3).

### K13–K15 — YouTube: views, watch time, subscribers
- See §4.4. These are the YouTube-specific KPIs the pilot tracks (views, watch time in hours, subscribers end-of-month and net new).

---

## 4. Channel-specific KPIs

### 4.1 Facebook
Core KPIs K1–K12 apply. Channel notes:
- **Reach & impressions** from Meta Business Suite page insights.
- **Messages:** page inbox; Meta reports response rate and average response time (K9–K10). Target ≥90% response for the responsiveness badge (`BENCHMARKS.md` §3.1).
- **Photo posts are the standout format** — Rival IQ 2025 measured photo posts driving roughly 5× the median engagement rate on top-form platforms (`BENCHMARKS.md` §1.3). The report notes when strong engagement coincides with photo content.
- **Link taps** = clicks on the page's website/CTA button.

### 4.2 Instagram
Core KPIs K1–K12 apply. Channel notes:
- **Saves** carry extra weight on Instagram — the audit framework treats saves as intent (`AUDIT_FRAMEWORK.md` §4.2).
- **Reach/impressions, profile visits, link taps** from the Instagram professional dashboard (requires a Professional account — **account type TO VERIFY via Shannon**).
- **Stories engagement** (polls, question stickers, replies) is tracked in the notes column; story reach is captured with the monthly snapshot (story insights have short lookback windows — see §7 capture discipline).

### 4.3 TikTok
Core KPIs K1–K12 apply (K13 views also applies). Channel notes:
- **Views** are TikTok's headline number; engagement rate uses views as the impression base where impressions are not separately reported.
- **Follower growth and profile visits** from TikTok Analytics (business account required — **account type TO VERIFY via Shannon**).
- **Messages** from the TikTok inbox (access TO VERIFY).

### 4.4 YouTube
- **K15 — Subscribers:** end-of-month subscriber count and net new (YouTube Studio).
- **K13 — Views:** total video views in the month (YouTube Studio).
- **K14 — Watch time:** total hours watched in the month (YouTube Studio). Watch time is the metric YouTube's algorithm rewards and the best read on whether walkarounds/explainers actually help shoppers.
- **K2 — Impressions:** how many times video thumbnails were shown in recommendations/search; paired with views it shows how often thumbnails get clicked (click-through).
- **K3 — Engagement rate:** (likes + comments + shares) ÷ impressions × 100.
- **K8 — Comments** and **K7 — Shares** from Studio.
- **K11 — Channel visits** from Studio.
- **Format note:** Shorts are the discovery format, long-form the depth format; no platform-published Shorts reach statistic exists — house rules apply (`BENCHMARKS.md` §6).

### 4.5 Reddit — participation health (no vanity metrics)
Reddit publishes **no engagement-rate or posting-frequency benchmarks** (`BENCHMARKS.md` §5, §7). Reddit's value is participation, not broadcast: Reddiquette requires far more participating than promoting (`BENCHMARKS.md` §5). The KPIs therefore measure **health of participation**, not reach:
- **K16a — Participations:** comments + posts the store account made during the month (house cadence: 2–4 genuine participations/week, only after subreddit fit is confirmed — `content/CONTENT_STRATEGY_FRAMEWORK.md` §6.5).
- **K16b — Replies received:** how often the account's contributions got replies (a sign the contribution was useful, not spam).
- **K16c — Upvotes received:** public upvote total on the account's contributions (approximate, captured with date).
- **K16d — Removals:** contributions removed by moderators (removal data requires moderator access — **TO VERIFY via Shannon**). Zero removals is the target; a removal is a red flag to investigate.
- **K16e — Subreddit fit maintained:** the account still participates only in subreddits whose rules permit it; fit is re-confirmed at each audit round.
- **K16f — Mentions of the store:** earned, non-promotional mentions of the store by others (manually noted; **manual tracking — TO VERIFY whether the store wants this tracked**).
- **K9/K10 — Messages:** Reddit messages received/responded (access TO VERIFY).

### 4.6 Google Business Profile (GBP)
The most direct lead-and-reputation channel a dealership has. KPIs:
- **K17 — Profile views:** views of the profile on Google Search and Maps, split into Search vs Maps in the dashboard.
- **K18 — Direction requests:** "Get directions" clicks — intent to visit the lot.
- **K19 — Calls:** phone calls placed from the profile.
- **K20 — Website clicks:** clicks to the store's website from the profile.
- **K21 — Review volume & rating:** new reviews received in the month, total review count, and current average star rating (public, captured with date). Context: 97% of consumers read reviews for local businesses; 47% won't use a business with fewer than 20 reviews; 31% will only use one rated 4.5★ or higher; 74% only consider reviews from the last 3 months (BrightLocal, `BENCHMARKS.md` §4.1).
- **K22 — Review & Q&A response:** share of new reviews responded to, typical response time, and whether profile questions (Q&A) got answered. Context: 89% of consumers expect a response to their review; 80% are more likely to use a business that responds to all reviews; templated replies put off 50% (BrightLocal, `BENCHMARKS.md` §3.2). **House target: respond to 100% of new reviews and answer every Q&A within 2 business days, genuinely, not by template.**
- **K23 — Photos added:** new photos added during the month (lot, showroom, service). House rule from `BENCHMARKS.md` §4.2: keep the profile stocked with current, real photos.
- **Data source:** GBP Insights (owner access required — **TO VERIFY via Shannon**). Insights show ~6 months of history; capture monthly so nothing is lost.

---

## 5. What matters most to a dealership General Manager

The monthly report leads with a short scorecard (see `REPORTING_TEMPLATE.md` §3). These are the numbers a GM can act on, in priority order. Each is reported per store and per channel — never combined across stores.

| # | KPI (and channel) | Why a GM cares | What healthy movement looks like |
|---|---|---|---|
| 1 | **Calls** (GBP) | Phone calls are the most direct demand signal — people ready to talk | More calls month over month; note when a content push or review response precedes a jump |
| 2 | **Direction requests** (GBP) | Intent to physically visit the lot | Steady or rising; falling direction requests while reach grows = content reaching people outside the service area |
| 3 | **Website clicks** (GBP) | Consideration — shoppers researching inventory before visiting | Rising; pair with link taps on social channels |
| 4 | **DMs / messages received** (FB, IG, TikTok) | Private inquiries are the closest thing to a social lead | Volume is informative; response rate/time is the action item (K10) |
| 5 | **Comments with intent** (FB, IG, TikTok, YouTube) | Public price/availability questions are leads the whole market can see being answered | More intent comments; every one answered within a business day |
| 6 | **Review volume + rating** (GBP) | Reputation is the gate shoppers use first — 97% read reviews (`BENCHMARKS.md` §4.1) | New reviews monthly; rating stable or rising; 100% responded |
| 7 | **Follower growth** (all channels) | The store's owned audience — future reach it doesn't pay for | Net positive; growth explained by content output |
| 8 | **Reach** (FB, IG, TikTok, YouTube) | Awareness in the store's market | Rising with consistent posting; read with context (market size, paid vs organic is out of scope here) |
| 9 | **Engagement rate** (FB, IG, TikTok, YouTube) | Whether content resonates — the team's main creative feedback loop | **Read as a trend vs the store's own history and the platform trend**, not a static number; engagement is falling platform-wide (`BENCHMARKS.md` §1.1) |
| 10 | **Watch time** (YouTube) | Depth content (walkarounds, explainers) actually helping shoppers research | Rising hours = content earning attention, not just clicks |

**Not on the GM scorecard but still tracked:** saves, shares, profile visits, link taps, posts published, Reddit participation health, GBP photos/Q&A — they explain *why* the headline numbers move and live in the per-channel tables and dashboard.

**Attribution caveat:** the pilot measures social and profile activity, not closed sales. Whether calls/DMs convert to sales is the store's data — whether the store tracks it is **TO VERIFY — request from client via Shannon McNeil** (`CLIENT.md` §8.2). If the store shares conversion data, the report adds a conversion note; until then, the report says what the numbers are and does not claim sales outcomes.

---

## 6. Measurement cadence

| KPI | Weekly (operational check) | Monthly (dashboard + report) | Quarterly (trend & re-check) |
|---|---|---|---|
| Reach / Impressions (K1–K2) | | ✔ | ✔ |
| Engagement rate (K3) | | ✔ | ✔ |
| Follower growth (K4) | | ✔ | ✔ |
| Posts published vs plan (K5) | ✔ (cadence check vs calendar) | ✔ (incl. content-mix check) | ✔ |
| Saves / Shares (K6–K7) | | ✔ | ✔ |
| Comments (K8) | ✔ (scan for intent + unanswered) | ✔ | ✔ |
| DMs / messages (K9) | ✔ (unanswered count) | ✔ | ✔ |
| Message response rate/time (K10) | ✔ | ✔ | ✔ |
| Profile visits / Link taps (K11–K12) | | ✔ | ✔ |
| TikTok/YouTube views (K13) | | ✔ | ✔ |
| YouTube watch time (K14) | | ✔ | ✔ |
| YouTube subscribers (K15) | | ✔ | ✔ |
| Reddit participation health (K16) | ✔ (removals, fit) | ✔ | ✔ |
| GBP views / directions / calls / clicks (K17–K20) | | ✔ | ✔ |
| GBP reviews volume + rating (K21) | ✔ (new reviews + responses due) | ✔ | ✔ |
| GBP review/Q&A response (K22) | ✔ (response check) | ✔ | ✔ |
| GBP photos (K23) | | ✔ | ✔ |
| Benchmark re-verification (`BENCHMARKS.md` §0) | | | ✔ (before quarterly report) |
| Re-audit (per `AUDIT_FRAMEWORK.md`) | | | ✔ (every ~90 days) |

**Weekly** checks are operational and live in the team's working notes (they feed the monthly report, they are not client-facing): are comments/DMs/reviews answered, any Reddit removals, is posting on pace with the calendar.

**Monthly** is the report cycle: on a fixed day each month (e.g., the 1st — date **TO VERIFY** with Shannon), pull every KPI into the store's dashboard row, then fill `REPORTING_TEMPLATE.md` → `reporting/reports/store-XX/MONTHLY_REPORT-<period>.md`.

**Quarterly** (end of Months 3 and 6): the shorter quarterly variant of the report (`REPORTING_TEMPLATE.md` §8), including benchmark re-verification and a re-audit recommendation.

---

## 7. Data sources & access — platform-native insights

Every KPI above is measured from the platform's own native insights, pulled by the team with confirmed account access. **Access to every tool below is TO VERIFY — request from client via Shannon McNeil** (`CLIENT.md` §8.1: login access / roles for each account, granted per account permissions). No access, no numbers — the cells stay TO VERIFY.

| Channel | Native insights tool | Key metrics it provides | Access required |
|---|---|---|---|
| Facebook | Meta Business Suite — Page insights | Reach, impressions, engagement, follower growth, profile visits, link clicks, message response rate & time | Page access via Shannon — **TO VERIFY** |
| Instagram | Instagram professional dashboard (via Business Suite) | Reach, impressions, engagement, saves, shares, profile visits, link taps, follower growth | Professional account + access — **TO VERIFY** |
| TikTok | TikTok Analytics | Video views, reach, profile views, likes/comments/shares/saves, follower growth, messages | Business account + access — **TO VERIFY** |
| YouTube | YouTube Studio — Analytics | Views, watch time, subscribers, impressions, click-through, comments, channel visits | Channel access — **TO VERIFY** |
| Reddit | **No native analytics** — manual tracking | Participations, replies, upvotes (public); removals (needs moderator access) | Account access; removal data — **TO VERIFY** |
| Google Business Profile | GBP Insights | Profile views (Search/Maps), direction requests, calls, website clicks, review activity; Q&A and review data are public | Profile owner access via Shannon — **TO VERIFY** |

**Capture discipline (protects against data loss):**
- Native insight windows are limited (some granular data goes back only ~28 days; GBP up to ~6 months). Exact per-platform lookback windows are **TO VERIFY at first capture** — check each analytics page when access is granted.
- Therefore: capture all monthly numbers on the **same day every month**, screenshot the insights pages as evidence (screenshots live with the store's report, mirroring `audit/reports/store-XX/evidence/`), and never rely on pulling two months at once.
- Record the capture date and tool in the dashboard notes column and the report appendix.

---

## 8. Benchmark alignment — where targets come from

All benchmark claims cite `audit/BENCHMARKS.md` (source-verified; full source list in `BENCHMARKS.md` §8). Benchmarks are **directional context**, never pass/fail. House targets are team defaults **for Shannon to confirm**, never presented as research.

| KPI / decision | Reference point | Source (BENCHMARKS.md) | Type |
|---|---|---|---|
| Engagement-rate interpretation | Engagement fell YoY on every major platform (FB −36%, IG −16%, TikTok −34%); no automotive medians published — Retail is the closest proxy | §1.1, §1.2, §7 | Benchmark (directional) |
| Posting cadence vs plan | House-default cadence per channel (FB 3–5/wk; IG 3–5 feed + 3–5 Stories/wk; TikTok 3–5/wk; YouTube 1 Short/wk + 1 long-form/mo; Reddit 2–4 participations/wk; GBP 2–4 posts/mo) | §2, §6 + `content/CONTENT_STRATEGY_FRAMEWORK.md` §8 | House default — confirm with Shannon |
| Message response | Meta "Very responsive" badge: respond to ≥90% of messages with fast response time | §3.1 | Platform guidance (directional) |
| Review/Q&A response | Respond to 100% of new reviews within 2 business days, genuine replies; answer every Q&A within 2 business days | §3.2 | House target built on BrightLocal evidence |
| Review volume & rating | 20+ recent reviews, 4.0★+ average, new reviews monthly (ask at delivery/service) | §4.1 | House target built on BrightLocal evidence |
| Reddit posture | Participation over promotion; confirm subreddit fit before any activity; no hard-selling | §5 | Platform norm (canonical doc) |
| YouTube formats | Shorts for discovery, long-form for depth; no unexplained gap > 2–3 weeks; real thumbnails; playlists | §6 | Platform guidance + house rules |

**Re-verify before each quarter:** `BENCHMARKS.md` §0 requires re-checking sources before each audit round; the reporting cycle does the same before each quarterly report (§6).

---

## 9. Master TO VERIFY list (everything that blocks real numbers)

Every item below must come from Shannon McNeil before the corresponding KPI can be filled with real data:

- [ ] **Access to native insights** for each store × channel: Meta Business Suite (FB + IG), TikTok Analytics, YouTube Studio, GBP Insights — granted via Shannon per account permissions (`CLIENT.md` §8.1). *Blocks K1–K15, K17–K23.*
- [ ] **Professional/business account status** where required (Instagram Professional, TikTok Business) — `CLIENT.md` §8.1. *Blocks IG/TikTok insights.*
- [ ] **Reddit account access** and whether any moderator access exists for removal data — `CLIENT.md` §8.1. *Blocks K16d.*
- [ ] **Store-level goals and KPIs the client already tracks** (leads, calls, service appointments, awareness) — `CLIENT.md` §8.2. *Sets which scorecard rows matter most per store.*
- [ ] **Whether the store tracks call/DM-to-sale conversion** — `CLIENT.md` §8.2. *Determines whether the report can add a conversion note.*
- [ ] **Pilot start/end dates and monthly reporting date** (e.g., capture on the 1st) — `CLIENT.md` §8.3. *Labels dashboard months and report periods.*
- [ ] **Real store names/markets** for report headers — `CLIENT.md` §3.
- [ ] **Exact native-insight lookback windows** per platform — check at first capture. *Protects history.*
- [ ] **Follower counts and rating baselines** as of audit day — `CLIENT.md` §8.1 + first audit. *The dashboard's Baseline row.*

---

## 10. Sources & maintenance

- All benchmark claims cite `audit/BENCHMARKS.md`, which holds the source-verified numbers and full URL list (`BENCHMARKS.md` §8). Named sources referenced here: Rival IQ 2025 Social Media Industry Benchmark Report (engagement trends), Sprout Social (cadence, messaging), BrightLocal Local Consumer Review Survey 2026 (reviews/response), Meta Business Help Center (responsiveness badge), Google Business Profile Help, Reddit Help (Reddiquette), YouTube Help/Creator Academy.
- **Explicit non-findings honored (not invented):** no automotive-specific engagement medians; no Reddit engagement/frequency benchmarks; no GBP posting-frequency number; no verified YouTube Shorts reach statistic (`BENCHMARKS.md` §7). Where this framework needed a number and none existed, it set a **house default** labeled as such — never research.
- **Re-verify at each quarter:** platforms change and studies refresh; re-check cited pages per `BENCHMARKS.md` §0 before each quarterly report.
- This framework stays aligned with `DASHBOARD_TEMPLATE.md` (column names) and `REPORTING_TEMPLATE.md` (report rows). If a KPI is added, changed, or dropped, all three files change together.

---

*End of framework. Everything here is an internal draft until Shannon McNeil approves it for client delivery. No one on the Bright Matter team contacts the store directly.*
