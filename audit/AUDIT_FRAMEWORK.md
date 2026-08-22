# AUDIT_FRAMEWORK.md — Month 1 Audit Methodology (Six Buckets, Per Store)

**Status:** INTERNAL — audit working methodology. Not client-facing; nothing here ships until Shannon McNeil approves (WORKFLOW.md).
**Last updated:** 2026-08-13 (rescoped to the operator's six-bucket Month 1 audit structure)
**Owner:** Bright Matter LLC agency operations team (Audit & Research Analyst)
**Applies to:** Greenway Auto Group pilot — 5 rooftops (Store 01–05) × 6 channels each
(Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile)

**Working files — read these alongside this methodology:**
- `workbook/WORKBOOK.md` — the **working implementation** of this framework: one tab per rooftop (Store 01–05) × the six buckets below. Every cell is either a sourced finding (citation in brackets → `workbook/SOURCES.md`) or a named blocker with owner and what is needed to unblock. No empty cells; nothing invented.
- `gm-interviews/BASELINE_QUESTIONNAIRE.md` — the **data-collection instrument**: the 38-question GM one-on-one set, each question mapped to a bucket and to `CLIENT.md` §8. One completed copy per rooftop.
- `workbook/BLOCKERS.md` — one-page blockers summary with owners, written to lift into `engagement-state.md` §4.

---

## 0. What this document is

This is the methodology the team uses to run the **Month 1 audit** for Greenway Auto Group. The operator defined the audit as **six buckets**; the workbook implements that structure, and this document explains how each bucket is run. The audit always runs **store-by-store** (one rooftop at a time, never the group as a whole). Within Buckets 1–4, the work is still per channel — one store's presence on one channel at a time — using `stores/store-XX/STORE.md` (the store's profile and channel inventory) and `channel-matrix.csv` as the starting point. Buckets 5 and 6 run at store/market level.

**No store facts exist yet.** Until Shannon McNeil provides the data listed in `CLIENT.md` §8, every field in a completed audit is marked:
> **TO VERIFY — request from client via Shannon McNeil**

A real audit can only begin once handles/URLs and account access are confirmed via Shannon. This framework is the machine that will run as soon as that data arrives.

---

## 1. The six buckets at a glance

| # | Bucket | What it answers | Data comes from | Blocked on (owner) | Questionnaire |
|---|---|---|---|---|---|
| 1 | **Accounts & Access Inventory** | Who holds admin on Meta Business Manager, Google Business Profile, TikTok, and YouTube — split between store staff and outside vendors. **The single biggest Month 1 timeline risk.** | Store + corporate IT, per `CLIENT.md` §8.1 | BLOCKERS #1 — Shannon McNeil (store data/access); Shawn Vink (corporate IT/admin) | Part 1 (Q1–8) |
| 2 | **Performance Baselines (per channel)** | Reach, impressions, engagement, follower counts, last-post dates per channel; the store's goals and KPIs. | Native insights (Meta Business Suite, TikTok Analytics, YouTube Studio, GBP Insights) + public counts + store goals | BLOCKERS #2 (native-insights access — Shannon McNeil; Shawn Vink where corporate; Reporting Analyst consumes) and #4 (goals/KPIs — Shannon McNeil) | Part 2 (Q9–14), Part 4 inputs (Q21–24) |
| 3 | **Reputation** | Reddit, Google reviews, DealerRater, Cars.com, Edmunds, Yelp — ratings, review counts, and response behavior. | Public review pages + store answers | BLOCKERS #5 (reputation platforms — Shannon McNeil / MCP grant or manual) and #6 (Reddit presence — Shannon McNeil, Apify) | Part 5 (Q25–27), Q36 |
| 4 | **Search Presence** | Whether the store surfaces when shoppers search: exact brand+market query, generic category query (map pack), website standing, NAP consistency. | Observation (Google Maps/web) + store answers | No dedicated blocker row; generic-query tests blocked 2026-08-12 — manual verification needed — 2026-08-12 | Q37 |
| 5 | **Competitive Benchmarking (local market)** | The store's real local competitors (same-brand dealers in its market) and how the store compares (ratings, presence, benchmarks). | Per-market research + store answers | BLOCKERS #8 — Audit & Research re-run once Exa MCP granted; Shannon McNeil for MCP grant | Q38 |
| 6 | **Current Operations Workflow** | Who posts today, with what tool, on what cadence; who answers comments/messages; content-plan maturity; weekly effort. | Store answers | BLOCKERS #3 — Shannon McNeil | Part 3 (Q15–20) |

**Sequence:** Bucket 1 is the gate. Until accounts and access are confirmed, no ownership or performance cell in Buckets 2–6 can be verified; public-page review is the only work possible without access. Buckets 2–6 can then run in any order; the workbook keeps all six per store in one place.

---

## 2. Bucket detail — what gets checked, what data to collect, where it maps

### Bucket 1 — Accounts & Access Inventory

**What gets checked.** For each of the 6 channels (Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile): does the account exist, is it active (Active / Inactive / not yet claimed), who controls access, and who holds admin roles. The split between **store staff** and **outside vendors** is the core question — vendor-held admin is the biggest Month 1 timeline risk and the hardest thing to recover once the pilot starts.

**What data to collect.** Handle/URL per channel, active status, login access and admin-role list per account (Meta Business Manager for FB/IG, Google Business Profile, TikTok, YouTube, Reddit), GBP verification status, any orphaned or abandoned accounts where nobody at the store can log in, and who keeps the master login list (corporate IT is Shawn Vink — confirm).

**Where it maps.** BLOCKERS #1 (owner: Shannon McNeil for store data/access; Shawn Vink for corporate IT/admin) · questionnaire Part 1 (Q1–8) · `CLIENT.md` §8.1. Public-visible signals (e.g., a live GBP owner-post stream) are recorded as observed but never used to infer who holds access — that stays TO VERIFY.

### Bucket 2 — Performance Baselines (per channel)

**What gets checked.** Per channel: follower/subscriber count (audit date), last-post date, 90-day post count, reach/impressions, engagement (likes, comments, shares, saves, views), message/comment response metrics, and trend vs. the benchmarks in §6 (`BENCHMARKS.md`). Also the store's own pilot goals and the KPIs it already tracks — the baseline means nothing without the store's definition of good.

**What data to collect.** Native-insights data per channel (Meta Business Suite for FB/IG, TikTok Analytics, YouTube Studio, GBP Insights), public counts with the audit date recorded next to each, and the store's goals/KPIs/content assets/brand rules (questionnaire Parts 2 and 4). Platform blocks: TikTok and Facebook block automated retrieval — manual verification needed — [date]; YouTube channel-level data requires Studio or the Data API; GBP Insights requires listing-owner access. A failed fetch is not evidence an account does not exist (OPERATING_RULES §3.7).

**Where it maps.** BLOCKERS #2 (per-account native-insights access; Reporting Analyst consumes the output) and #4 (goals/KPIs) · questionnaire Part 2 (Q9–14) with Part 4 inputs (Q21–24) · `CLIENT.md` §8.1–8.2 · scoring dimensions D1–D8 and the per-channel checklists in §5.

### Bucket 3 — Reputation (Reddit, Google, DealerRater, Cars.com, Edmunds, Yelp)

**What gets checked.** Ratings and review counts on Google, DealerRater, Cars.com, Edmunds, and Yelp; whether the store responds to reviews (volume responded, average response time); the store's Reddit footprint (any organic presence, complaints, responses). Framing rules apply: reputation findings are an **absence problem, not a complaint list** (OPERATING_RULES §10), sensitive findings are held for one-on-one GM conversations (§9), and the structural pattern of named staff driving nearly all positive reviews is a finding, not a footnote (§11).

**What data to collect.** Star rating + review count (audit date), review-response behavior per platform, Reddit search results per store name + street address (Apify Reddit scraper once MCP access is granted, manual check as fallback). DealerRater/Edmunds/Yelp/Cars.com presence is NOT confirmed either way until retrieved — blockers #5 and #6 record the status.

**Where it maps.** BLOCKERS #5 (reputation platforms — re-run via Exa/Apify MCP once granted, or manual check) and #6 (Reddit presence) · questionnaire Part 5 (Q25–27) and Q36 (absence-framed) · `CLIENT.md` §9 operator context · the staff-review structural finding stays in the workbook per store.

### Bucket 4 — Search Presence

**What gets checked.** Exact brand+market query (does the store's own listing surface?), generic category query (map-pack position, e.g., "Kia dealer near [market]"), website standing (does the store's site surface, is it current?), and NAP consistency (name, address, phone identical across profile, website, and listings — flag mismatches; this matters for local search).

**What data to collect.** Search/Google Maps observations with audit date; the store's own answers on what shoppers see when they search (Q37); GBP listing data (category, NAP fields, verification) from the §5.6 checklist feeds this bucket.

**Where it maps.** No dedicated blocker row in BLOCKERS.md — exact-brand queries were observed (store surfaces on Google Maps); generic-query map-pack tests were blocked from the research environment on 2026-08-12 — manual verification needed — 2026-08-12 · questionnaire Q37 · `CLIENT.md` §8.1 (GBP verification/completeness).

### Bucket 5 — Competitive Benchmarking (local market)

**What gets checked.** The store's real local competitor set — the dealers shoppers cross-shop against in its market (Kia dealers in the Palm Beach, Jacksonville, and Nashville metros; Ford dealers in the Kansas City metro) — and how the store compares: competitor Google ratings, presence, and content patterns. Benchmarks from `BENCHMARKS.md` are the scoring context; they are directional, not pass/fail.

**What data to collect.** Competitor names + their Google ratings (audit date) per market, verified via research re-run (Exa/Apify MCP once granted) or manual check; the store's own competitor list from the GM (Q38) is the ground truth for who shoppers actually cross-shop.

**Where it maps.** BLOCKERS #8 (Audit & Research re-run once Exa MCP granted; Shannon McNeil for MCP grant) · questionnaire Q38 (fills the per-market competitor row in the workbook) · `BENCHMARKS.md` for scoring context.

### Bucket 6 — Current Operations Workflow

**What gets checked.** Who posts today (names or roles), with what tool (a scheduler such as Sprout, or direct in each app), on what cadence per channel; who answers comments and messages and how quickly; whether a content plan or calendar exists; how much time the current poster spends on social each week; and whether a vendor currently manages any account.

**What data to collect.** Store answers per `CLIENT.md` §8 on poster(s), tool(s), cadence, and vendor-managed accounts; public signals (e.g., a live GBP owner-post stream) are recorded as observed evidence that someone posts, never as proof of who or with what tool.

**Where it maps.** BLOCKERS #3 (owner: Shannon McNeil — store answers) · questionnaire Part 3 (Q15–20) · `CLIENT.md` §8.1.

---

## 3. The four-step process (per store, per channel)

### Step 1 — GATHER (what data to collect)
Pull the raw evidence for the store × channel pair. Collect, do not judge:

| Data group | What to capture | Source |
|---|---|---|
| Account identity | Handle/URL, display name, profile photo, cover/banner, bio, links (website, phone, map pin) | Public account page |
| Account status | Active / Inactive / Not claimed / Suspended; verification badge (blue check) if applicable | Public account page + client |
| Access & ownership | Who owns logins; admin roles; prior vendor access; passwords stored where | **TO VERIFY — request from client via Shannon McNeil** |
| Follower/subscriber count | As of audit date | Public account page / native analytics |
| Content sample | Last 12 weeks of posts (or last 30 posts if heavier): date, type (photo/video/Reel/Shorts/Story/live/text), caption, link, hashtags | Public account page |
| Engagement per post | Likes, comments, shares, saves (and views for video) | Public account page / native analytics |
| Messages & comments | Unanswered comments; DM volume; response time; auto-replies | Native inbox (with client access) |
| Channel-specific data | See §5 per-channel checklists (GBP: category, NAP, reviews, photos, Q&A; Reddit: subreddit fit, post history; YouTube: Shorts vs long-form, thumbnails, playlists) | Public pages + native analytics |
| Performance history | Reach, impressions, profile visits, follower growth over last 90 days | Native analytics (Meta Business Suite, TikTok Analytics, YouTube Studio, GBP Insights) |
| Store goals & KPIs | Pilot goals for this store and channel | **TO VERIFY — request from client via Shannon McNeil** |

**Rule:** capture the evidence first. Never score from memory or from a single post. Each bucket in §2 names which rows of this table it consumes.

### Step 2 — VERIFY (check the evidence is real and current)
- **Verify identity:** is this the store's real account? Check for lookalike handles, wrong phone numbers, stale logos, old addresses. Flag impersonation risk.
- **Verify access:** confirm (via Shannon) that the account is controlled by the store, not a previous vendor. This is a hard gate for anything beyond public-page review (Bucket 1).
- **Verify numbers:** pull follower counts and last-post dates directly from the live account on audit day. Record the audit date next to every number.
- **Mark unknowns:** anything not confirmed by direct observation or by Shannon is written as **TO VERIFY — request from client via Shannon McNeil**. Never estimate a follower count, a review rating, or a last-post date.
- **Spot-check with screenshots:** save a dated screenshot of the profile and 2–3 representative posts as evidence. Screenshots are the evidence trail the team lead and Shannon review before approval.

### Step 3 — SCORE (apply the rubric in §4)
- Score each dimension 1–5 using the plain-language anchors in §4.
- Score **only what is observed**. If access is missing and a dimension cannot be observed, record the dimension as **Not scored — TO VERIFY** rather than guessing.
- Compute the overall channel score: **average of the scored dimensions** (round to 1 decimal). The score sheet is a table per channel (see `AUDIT_REPORT_TEMPLATE.md`).
- Compare against benchmarks in `BENCHMARKS.md` and against the store's own pilot goals (once provided). Benchmarks are directional, not pass/fail.
- Bucket-level findings (reputation, search, competitive, operations) are recorded as workbook rows with evidence, scored only where a rubric dimension applies.

### Step 4 — REPORT (produce the GM-ready deliverable)
- Fill the per-store report from `AUDIT_REPORT_TEMPLATE.md` (one report per store, covering all 6 channels).
- Every claim in the report carries evidence (a number, a date, a screenshot reference, or a cited benchmark).
- The report ends with **ranked opportunities (impact × effort)** and **next steps with owner and timing**.
- The completed report is an **internal draft**: specialist → team lead review → Shannon McNeil approval → client (per `WORKFLOW.md`). Nothing is sent without Shannon's sign-off.

---

## 4. Scoring rubric — 1–5 with plain-language anchors

Same rubric for every dimension on every channel. One scale, so a GM can compare channels without decoding different systems.

| Score | Anchor (plain language) |
|---|---|
| **5 — Best practice** | Looks maintained by a professional team. Nothing missing, nothing broken. Would make a shopper feel confident and take the next step (call, visit, follow, message). |
| **4 — Strong** | Essentially complete with minor gaps (e.g., one stale link, occasional late reply). Small effort would make it a 5. |
| **3 — Acceptable baseline** | Functional but uninspired or inconsistent: profile mostly complete, posting happens but irregularly, engagement is occasional. Clear room to improve. |
| **2 — Weak** | Noticeable problems: outdated info, very sparse posting (weeks/months of silence), unanswered comments or messages, obvious mismatch with other channels. |
| **1 — Broken / absent** | Account unclaimed, suspended, or abandoned (no post in 90+ days); wrong or misleading info; no response mechanism in use. |
| **NS — Not scored** | Could not be observed because access/data are missing. Always paired with **TO VERIFY — request from client via Shannon McNeil**. |

### Dimensions scored on every channel

| # | Dimension | What good looks like (5) |
|---|---|---|
| D1 | **Account status & ownership** | Claimed, verified where the platform offers it, and owned by the store (not a former vendor); logins documented with Shannon. (Bucket 1) |
| D2 | **Profile completeness & branding** | Name, handle, logo, cover/banner, bio, contact info, and links all present, current, and consistent with the store's branding across all 6 channels. |
| D3 | **Content quality & value** | Posts inform or entertain a real shopper in this store's market: inventory that's actually there, service tips, local relevance. No spam, no stock-photo filler. |
| D4 | **Cadence & recency** | Posts on a rhythm (see `BENCHMARKS.md`) with no unexplained gaps; last post within the expected window for the channel. (Bucket 6) |
| D5 | **Format mix (evergreen vs timely)** | Healthy mix of formats the channel rewards (photo, video, Stories/Shorts/Reels as appropriate) and a balance of evergreen content (walkaround, hours, services) with timely content (new arrivals, events, seasonal). |
| D6 | **Engagement** | Real audience interaction: comments, shares, saves, direct messages — and engagement rates in a reasonable band for the channel/industry (see `BENCHMARKS.md`). (Bucket 2) |
| D7 | **Community management & response** | Comments, DMs, and reviews get a genuine reply within the response-time expectation for the channel (see `BENCHMARKS.md`). No long-unanswered threads. (Buckets 3 and 6) |
| D8 | **Performance vs benchmark** | Reach, impressions, and follower growth trend reasonably vs. channel/industry benchmarks and the store's own pilot goals. (Bucket 2) |

### Channel-specific dimensions (scored in addition to D1–D8)

| Channel | Extra dimensions |
|---|---|
| **Facebook** | Page roles & settings hygiene (who can post, admin list — Bucket 1); local relevance of page info (address, hours, phone, website); use of platform features (events, offers, reviews). |
| **Instagram** | Bio + link strategy (single link, link-in-bio); Reels/Stories presence; saves are tracked (saves = intent). |
| **TikTok** | Use of trends/sounds appropriate to a dealership; sound-on captions; authentic (not overproduced) style; bio link + contact path. |
| **YouTube** | **Shorts vs long-form balance**; **thumbnail quality** (clear, readable, honest); **playlists** organization; channel banner/trailer; **posting rhythm** consistency; video titles/descriptions with searchable keywords. |
| **Reddit** | **Community norms fit** (posts match subreddit culture); **no hard-selling** (Reddit's self-promotion norms, see `BENCHMARKS.md`); subreddit relevance (does a dealership-relevant subreddit even exist and does the store belong?); comment karma/history quality; u/ vs r/ usage — is the store posting as a user or a brand account, and what does the community expect? |
| **Google Business Profile** | **Category** accuracy; **NAP consistency** (name, address, phone identical everywhere — profile, website, social, citations); **reviews volume + rating**; **photos** count/quality/recentcy; **Q&A** (are questions answered, and are they real?); verification status; services/products listings; posts/offers; booking/call buttons. (Buckets 1, 3, and 4) |

---

## 5. Per-channel checklists — what to check, what to collect

These are the channel-by-channel working checklists. They feed Buckets 1 (status/ownership), 2 (content and performance baselines), 3 (reviews/community), and 4 (search/NAP for GBP).

### 5.1 Facebook
- **Profile completeness:** page name, category (dealership vs. auto-related), logo, cover photo, bio/about, address, hours, phone, website, map. Buttons (Call, Message, Directions).
- **Branding consistency:** matches the store's other channels (same name, logo, tone).
- **Content audit:** last 12 weeks — cadence, format mix (photo, video, Reels, live, links), evergreen vs timely, local relevance, spam signal.
- **Engagement audit:** likes/comments/shares per post; response rate and time on messages (Meta reports this in Business Suite); unanswered comments; review replies.
- **Performance vs benchmark:** reach/impressions per post, follower growth vs `BENCHMARKS.md`.
- **Collect:** follower count (audit date), last post date, 90-day post count, post-level engagement, message response metrics, page roles (via client access — Bucket 1).

### 5.2 Instagram
- **Profile completeness:** handle, name, bio (what the store is + location), link, profile photo (logo), category, contact buttons (call, email, directions), highlights.
- **Content audit:** last 12 weeks — feed post mix (photo vs Reel vs carousel), Stories/Highlights usage, hashtags, captions with local relevance.
- **Engagement audit:** likes/comments/saves/shares per post; DM response behavior; comment replies.
- **Performance vs benchmark:** reach/impressions, profile visits, follower growth vs `BENCHMARKS.md`.
- **Collect:** follower count, last post date, 90-day post count, per-post engagement, DM response metrics (via client access).

### 5.3 TikTok
- **Profile completeness:** handle, bio, link, avatar, pinned videos.
- **Content audit:** last 12 weeks — video volume, style (authentic vs corporate), use of trending sounds (appropriate for a dealership), captions/on-screen text, hashtags.
- **Engagement audit:** views/likes/comments/shares per video; comment replies; DM behavior.
- **Performance vs benchmark:** view-to-follower dynamics, follower growth vs `BENCHMARKS.md`.
- **Collect:** follower count, last post date, 90-day video count, per-video views/engagement, comment response behavior (via client access).

### 5.4 YouTube
- **Shorts vs long-form:** what mix exists; are Shorts used for discovery and long-form for depth (walkarounds, reviews, how-tos)?
- **Thumbnails:** clear, readable, honest — not clickbait.
- **Playlists:** do videos get organized (e.g., "New Arrivals", "Service Tips")?
- **Channel polish:** banner, trailer, about section, links to website/socials.
- **Posting rhythm:** gaps longer than a month? Bursts then silence?
- **Engagement & performance:** views, watch time (via YouTube Studio), comments, subscriber growth, top-performing videos.
- **Collect:** subscriber count, last upload date, 90-day upload count, per-video views/comments, top 3 videos by views, playlist inventory, channel URL.

### 5.5 Reddit
- **Community norms fit:** which subreddits would a dealership plausibly appear in? Does the store's posting style match each subreddit's culture (local city subreddits, car-related subs)? Is the content the kind that community tolerates?
- **No hard-selling:** does the account avoid direct sales pitches and follow Reddit's self-promotion norms (see `BENCHMARKS.md` §Reddit)?
- **Account posture:** posting as a person (u/username) vs a brand account; comment history quality; karma; whether the account reads as genuine participation or as spam.
- **Collect:** Reddit handle (u/ or r/), posting/commenting history sample (last 30 items), karma if visible, subreddits where active, any removals (if access allows). Bucket 3 framing applies: absence, not complaint lists.

### 5.6 Google Business Profile
- **Category:** is the primary category right (e.g., "Car dealer" vs "Used car dealer" vs "Auto repair")?
- **NAP consistency:** name, address, phone identical across profile, website, and the store's other listings/socials. Flag mismatches — this matters for local search (Bucket 4).
- **Reviews:** volume, average star rating, recency of reviews, and whether the store responds (volume responded, average response time). Compare vs `BENCHMARKS.md` (BrightLocal data). (Bucket 3)
- **Photos:** count, quality, recency (are there photos from this year?).
- **Q&A:** are there questions on the profile, and are they answered? (Unanswered questions are a red flag for shoppers.)
- **Verification status & ownership:** verified? Who manages it (store staff vs prior vendor)? Via Shannon. (Bucket 1)
- **Additional:** services/products sections, booking/call buttons, posts/offers, business hours accuracy, attributes (e.g., "in-store shopping").
- **Collect:** profile URL, category, exact NAP fields, star rating + review count (audit date), photo count + latest photo date, Q&A list with answer status, verification status (via client), Google Business Profile Insights if accessible.

---

## 6. How to use benchmarks (BENCHMARKS.md)

- `BENCHMARKS.md` holds the reference numbers per channel: engagement-rate norms, cadence guidance, response-time expectations, review benchmarks, and format guidance.
- **Directional, not pass/fail.** Benchmarks describe what typical or platform-advised performance looks like; they are not guarantees and they vary by market, audience size, and content quality. A small-market store with 200 followers will not match a national median engagement rate — the audit says "below the industry median" and then explains why, in the store's context.
- **Platform-published vs third-party study:** the file labels each benchmark's source type. Platform-published guidance (Meta, Google, YouTube, TikTok, Reddit docs) is what the platform itself says; third-party studies (Rival IQ, BrightLocal, Sprout Social) are independent measurements. Both are directional.
- **Always re-check at audit time.** Benchmarks rot (platforms change; studies refresh annually). Before each audit round, confirm the cited sources are current.
- **Never invent a benchmark.** If a number isn't in `BENCHMARKS.md` and can't be sourced, the report says "no published benchmark — TO VERIFY / treat as house rule," it does not make one up.

---

## 7. Outputs and hand-offs

| Output | File | Who consumes it |
|---|---|---|
| Completed per-store audit report (6 channels, six-bucket findings) | `audit/reports/store-XX/AUDIT_REPORT.md` (one per store, filled from the template) | Team lead → Shannon McNeil → client |
| Channel score sheet | Embedded in the report (per-channel score tables) | GM |
| Evidence (screenshots, dated captures) | `audit/reports/store-XX/evidence/` | Team lead review |
| Six-bucket working rows (sourced findings + blockers) | `audit/workbook/WORKBOOK.md` (per store, per bucket) | All specialists; feeds engagement-state via `workbook/BLOCKERS.md` |
| Data-collection instrument | `audit/gm-interviews/BASELINE_QUESTIONNAIRE.md` (one completed copy per rooftop) | Operator (Shannon McNeil) |
| Updated statuses after audits | Feed back into `channel-matrix.csv` and `stores/store-XX/STORE.md` | All specialists |

**Approval pipeline:** Audit & Research Analyst drafts → team lead reviews → Shannon McNeil approves → client. No agent contacts the client. All outputs stay **INTERNAL** until approval.
