# DASHBOARD_TEMPLATE.md — Per-Store, Per-Channel KPI Tracking Sheet (6-Month Pilot)

**Status:** INTERNAL DRAFT TEMPLATE — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Reporting Analyst)
**Applies to:** Greenway Auto Group pilot — one tracking sheet per store (Store 01–05)

---

## 1. What this is

The working sheet where real performance data accumulates month over month, **one file per store**, at:

```
reporting/dashboards/store-XX/DASHBOARD.csv
```

Each store's dashboard is a single table: **rows = the 6 months of the pilot (plus a Baseline row), columns = one KPI per column, grouped by channel.** At the end of every month, the Reporting Analyst fills that month's row from platform-native insights (see `KPI_FRAMEWORK.md` §7 for sources and access). The monthly report (`REPORTING_TEMPLATE.md`) is then filled from this sheet — the dashboard is the source of truth, the report is the communication.

**Every cell is currently blank-but-marked: every value reads "TO VERIFY — request from client via Shannon McNeil" until real data is captured.** Nothing about the stores has been assumed. (The illustration tables in §4 abbreviate the marker for readability — the CSVs carry the full text.)

---

## 2. Structure

- **Rows:** `Baseline (Month 0 — audit day)` then `Month 01` … `Month 06` (six-month pilot). Replace "Month NN" labels with actual calendar months (e.g., "2026-09") once the pilot start date is confirmed — **TO VERIFY — request from client via Shannon McNeil** (`CLIENT.md` §8.3).
- **Columns:** `month`, then the KPI columns grouped per channel (prefixes `fb_`, `ig_`, `tt_`, `yt_`, `rd_`, `gbp_`), then `notes`.
- **Baseline row:** the starting values captured at the store's first audit (followers, rating, review count, etc.) — the point every month is compared to. Baseline data comes from the audit (`audit/reports/store-XX/AUDIT_REPORT.md`) and the store (via Shannon) — **TO VERIFY** until the first audit runs.
- **Per store, per channel:** the sheet tracks one store only. Channel columns never get summed or averaged into a group number; each column is reported as itself.

**Full column list (76 columns):**

`month · fb_reach · fb_impressions · fb_interactions · fb_engagement_rate_pct · fb_followers_end · fb_followers_new · fb_posts · fb_saves · fb_shares · fb_comments · fb_dms_received · fb_dms_responded · fb_profile_visits · fb_link_taps · ig_reach · ig_impressions · ig_interactions · ig_engagement_rate_pct · ig_followers_end · ig_followers_new · ig_posts · ig_saves · ig_shares · ig_comments · ig_dms_received · ig_dms_responded · ig_profile_visits · ig_link_taps · tt_reach · tt_impressions · tt_interactions · tt_engagement_rate_pct · tt_followers_end · tt_followers_new · tt_videos · tt_saves · tt_shares · tt_comments · tt_dms_received · tt_dms_responded · tt_profile_visits · tt_link_taps · yt_subscribers_end · yt_subscribers_new · yt_videos · yt_views · yt_watch_time_hours · yt_impressions · yt_interactions · yt_engagement_rate_pct · yt_comments · yt_shares · yt_channel_visits · rd_participations · rd_replies_received · rd_upvotes_received · rd_removals · rd_subreddits_active · rd_mentions_of_store · rd_messages_received · rd_messages_responded · gbp_views_search · gbp_views_maps · gbp_direction_requests · gbp_calls · gbp_website_clicks · gbp_reviews_total · gbp_reviews_new · gbp_rating_avg · gbp_review_responses · gbp_qa_total · gbp_qa_answered · gbp_posts · gbp_photos_added · notes`

---

## 3. Column dictionary (what each column means and where it comes from)

### Shared columns

| Column | Plain meaning | Source |
|---|---|---|
| `month` | Month label: `Baseline`, `Month 01`…`Month 06` (actual dates TO VERIFY) | — |
| `notes` | Free text: capture dates, screenshots taken, denominator used for engagement rate, intent comments flagged, anomalies, gaps | Reporting Analyst |

### Facebook (`fb_` prefix) — source: Meta Business Suite (access TO VERIFY — request from client via Shannon McNeil)

| Column | Plain meaning | Feeds report |
|---|---|---|
| `fb_reach` | Different accounts that saw page content this month | §3.1 |
| `fb_impressions` | Times page content was shown | §3.1 |
| `fb_interactions` | Likes + comments + shares + saves this month | §3.1 (computes engagement rate) |
| `fb_engagement_rate_pct` | (interactions ÷ impressions) × 100; if impressions unavailable, use reach and say so in `notes` | §3.1, §2 scorecard |
| `fb_followers_end` | Page followers at month end | §3.1, §2 scorecard |
| `fb_followers_new` | Net new followers this month (end − previous end) | §3.1 |
| `fb_posts` | Posts published this month (vs calendar plan) | §3.1 |
| `fb_saves` | Times posts were saved | §3.1 |
| `fb_shares` | Times posts were shared | §3.1 |
| `fb_comments` | Comments received this month; intent comments flagged in `notes` | §3.1, §2 scorecard |
| `fb_dms_received` | Messages received in the page inbox | §3.1, §2 scorecard |
| `fb_dms_responded` | Messages answered (→ response rate vs ≥90% band, `BENCHMARKS.md` §3.1) | §3.1 |
| `fb_profile_visits` | Times people opened the page | §3.1 |
| `fb_link_taps` | Clicks on the page's website/CTA button | §3.1 |

### Instagram (`ig_` prefix) — source: Instagram professional dashboard via Meta Business Suite (professional account + access TO VERIFY)

*Identical set to Facebook (`ig_reach`, `ig_impressions`, `ig_interactions`, `ig_engagement_rate_pct`, `ig_followers_end`, `ig_followers_new`, `ig_posts`, `ig_saves`, `ig_shares`, `ig_comments`, `ig_dms_received`, `ig_dms_responded`, `ig_profile_visits`, `ig_link_taps`).* Saves carry extra weight on Instagram (intent — `AUDIT_FRAMEWORK.md` §4.2). Stories reach/polls are tracked in `notes` (short lookback windows).

### TikTok (`tt_` prefix) — source: TikTok Analytics (business account + access TO VERIFY)

| Column | Plain meaning | Feeds report |
|---|---|---|
| `tt_reach` | Accounts that saw the store's videos this month | §3.3 |
| `tt_impressions` | Times videos were shown (views); used as engagement-rate base where impressions aren't separately reported | §3.3 |
| `tt_interactions` | Likes + comments + shares + saves | §3.3 |
| `tt_engagement_rate_pct` | (interactions ÷ impressions/views) × 100; denominator in `notes` | §3.3 |
| `tt_followers_end` / `tt_followers_new` | Followers at month end / net new | §3.3, §2 scorecard |
| `tt_videos` | Videos published this month | §3.3 |
| `tt_saves` / `tt_shares` / `tt_comments` | Bookmarks / forwards / comments | §3.3 |
| `tt_dms_received` / `tt_dms_responded` | Messages received / answered | §3.3 |
| `tt_profile_visits` | Times people opened the profile | §3.3 |
| `tt_link_taps` | Clicks on the bio link | §3.3 |

### YouTube (`yt_` prefix) — source: YouTube Studio (channel access TO VERIFY)

| Column | Plain meaning | Feeds report |
|---|---|---|
| `yt_subscribers_end` / `yt_subscribers_new` | Subscribers at month end / net new | §3.4, §2 scorecard |
| `yt_videos` | Videos published (Shorts vs long-form noted) | §3.4 |
| `yt_views` | Total video views this month | §3.4 |
| `yt_watch_time_hours` | Total hours watched — the depth-content measure | §3.4, §2 scorecard |
| `yt_impressions` | Times thumbnails were shown (recommendations/search) | §3.4 |
| `yt_interactions` | Likes + comments + shares | §3.4 |
| `yt_engagement_rate_pct` | (interactions ÷ impressions) × 100 | §3.4 |
| `yt_comments` / `yt_shares` | Comments / shares | §3.4 |
| `yt_channel_visits` | Times people opened the channel page | §3.4 |

### Reddit (`rd_` prefix) — source: manual tracking; no native analytics exist (`BENCHMARKS.md` §5, §7). Account access TO VERIFY; removal data needs moderator access.

| Column | Plain meaning | Feeds report |
|---|---|---|
| `rd_participations` | Comments + posts made this month (house cadence 2–4/wk after subreddit fit confirmed) | §3.5 |
| `rd_replies_received` | Replies to the account's contributions (usefulness signal) | §3.5 |
| `rd_upvotes_received` | Public upvotes on contributions (approximate; capture date in `notes`) | §3.5 |
| `rd_removals` | Contributions removed by moderators (0 is the target; red flag if any) | §3.5 |
| `rd_subreddits_active` | Subreddits the account participates in (fit re-confirmed each audit) | §3.5 |
| `rd_mentions_of_store` | Earned, non-promotional mentions of the store by others | §3.5 |
| `rd_messages_received` / `rd_messages_responded` | Reddit messages received / answered | §3.5 |

### Google Business Profile (`gbp_` prefix) — source: GBP Insights (owner access TO VERIFY) + public profile

| Column | Plain meaning | Feeds report |
|---|---|---|
| `gbp_views_search` / `gbp_views_maps` | Profile views on Google Search / Maps | §3.6 |
| `gbp_direction_requests` | "Get directions" clicks — intent to visit | §3.6, §2 scorecard |
| `gbp_calls` | Phone calls from the profile | §3.6, §2 scorecard |
| `gbp_website_clicks` | Clicks to the store's website | §3.6, §2 scorecard |
| `gbp_reviews_total` | Total review count (running) | §3.6 |
| `gbp_reviews_new` | New reviews this month (monthly flow is the goal) | §3.6, §2 scorecard |
| `gbp_rating_avg` | Current average star rating (capture date in `notes`) | §3.6, §2 scorecard |
| `gbp_review_responses` | New reviews responded to this month (vs 100%-within-2-days house target) | §3.6 |
| `gbp_qa_total` / `gbp_qa_answered` | Profile questions total / answered | §3.6 |
| `gbp_posts` | Profile posts published | §3.6 |
| `gbp_photos_added` | New photos added | §3.6 |

---

## 4. What the sheet looks like (illustration — per store)

*Each of the 6 channel groups below is one block of columns in the store's CSV. Cells are abbreviated to `TO VERIFY` here for readability; every real cell reads "TO VERIFY — request from client via Shannon McNeil" until filled.*

### Facebook block

| month | Reach | Impressions | Interactions | Eng. rate % | Followers end | New followers | Posts | Saves | Shares | Comments | DMs rec'd | DMs resp. | Profile visits | Link taps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 01 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 02 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 03 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 04 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 05 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 06 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |

### Instagram block — identical columns to Facebook (reach, impressions, interactions, eng. rate %, followers end, new followers, posts, saves, shares, comments, DMs rec'd, DMs resp., profile visits, link taps), all TO VERIFY, same 7 rows.

### TikTok block — reach, impressions, interactions, eng. rate %, followers end, new followers, videos, saves, shares, comments, DMs rec'd, DMs resp., profile visits, link taps — all TO VERIFY, same 7 rows.

### YouTube block

| month | Subs end | New subs | Videos | Views | Watch time (hrs) | Impressions | Interactions | Eng. rate % | Comments | Shares | Channel visits |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 01–06 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |

### Reddit block

| month | Participations | Replies rec'd | Upvotes rec'd | Removals | Active subreddits | Mentions | Msgs rec'd | Msgs resp. |
|---|---|---|---|---|---|---|---|---|
| Baseline | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 01–06 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |

### Google Business Profile block

| month | Views — Search | Views — Maps | Direction req. | Calls | Website clicks | Reviews total | New reviews | Rating avg | Reviews resp. | Q&A total | Q&A answered | Posts | Photos added |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baseline | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |
| Month 01–06 | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY |

---

## 5. How to use it (monthly routine)

1. **Fixed capture day every month** (e.g., the 1st — date TO VERIFY with Shannon, `CLIENT.md` §8.3). Pull every number from the native tools listed in §3 — never from memory.
2. **Fill the month's row** in `reporting/dashboards/store-XX/DASHBOARD.csv`, replacing the TO VERIFY marker with the real value. Screenshot each insights page as evidence (store with the report, mirroring `audit/reports/store-XX/evidence/`).
3. **Record context in `notes`:** capture dates, which denominator was used for engagement rate, intent comments, anomalies (e.g., a viral post, an outage), anything a future reader needs to interpret the number.
4. **If a number can't be captured** (no access, account inactive, window expired), leave the marker and list it in the month's report appendix (`REPORTING_TEMPLATE.md` §7) — the gap becomes a request to Shannon. Never estimate.
5. **End of month:** fill `REPORTING_TEMPLATE.md` from this sheet → `reporting/reports/store-XX/MONTHLY_REPORT-<period>.md` → team lead review → Shannon McNeil approval → client (`WORKFLOW.md`).
6. **Quarter ends (Months 3 and 6):** produce the quarterly variant (`REPORTING_TEMPLATE.md` §6) using the accumulated rows, after re-verifying benchmarks (`BENCHMARKS.md` §0).

**Alignment rules:** column names here match `KPI_FRAMEWORK.md` §2–§4 and the report tables. If a KPI changes, update this file, the framework, and the report template together.

---

## 6. Files (one per store)

Blank working copies already exist for all five stores:

```
reporting/dashboards/store-01/DASHBOARD.csv
reporting/dashboards/store-02/DASHBOARD.csv
reporting/dashboards/store-03/DASHBOARD.csv
reporting/dashboards/store-04/DASHBOARD.csv
reporting/dashboards/store-05/DASHBOARD.csv
```

Each is identical (all cells marked TO VERIFY — request from client via Shannon McNeil). When real data arrives, fill the matching store's file only; never copy numbers between stores.

---

*End of template. Everything here is an internal draft until Shannon McNeil approves it for client delivery. No one on the Bright Matter team contacts the store directly.*
