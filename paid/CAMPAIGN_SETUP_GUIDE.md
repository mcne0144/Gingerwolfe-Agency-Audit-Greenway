# CAMPAIGN_SETUP_GUIDE.md — Step-by-Step Campaign Build Checklist (Greenway Auto Group)

**Status: INTERNAL DRAFT — not client-facing until Shannon McNeil approves**
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Paid Media Specialist)
**Applies to:** Greenway Auto Group pilot — per-store campaign builds on Meta, TikTok, Google Ads/YouTube (Reddit via Reddit Ads Manager). Companion to `PAID_MEDIA_FRAMEWORK.md` and `AD_COPY_TEMPLATE.md`.

---

## 0. THE HARD LINE (restated — applies to every step in this file)

> **No agent launches, funds, modifies, or manages live ad spend, and no agent touches any existing Greenway ad account (including Facebook paid, where Greenway-side contact Brennan has an informal role) without the operator's explicit confirmation that scope has expanded and access has been granted.**
>
> Every step below that would touch a live account, create a campaign, set a budget, or install tracking carries the gate:
> **"BLOCKED until operator confirms scope expansion + access."**
>
> The retainer is the SERVICE FEE, not media spend. Every budget is a PROPOSAL for Shannon's approval. This checklist is a **draft-and-prepare** guide: the team can build the plan, the naming convention, the checklist, and the assets — but **nothing is created inside a live ad platform** until the gate opens.

---

## 1. Pre-flight: the access gate (TO VERIFY — request from client via Shannon McNeil)

Before ANY build inside a platform, confirm these with Shannon (corporate/admin access via **Shawn Vink** where applicable — BLOCKERS.md #1). Until they are answered, the build stops at the platform boundary.

| # | Access item | Owner | Status |
|---|---|---|---|
| 1 | Meta Business Manager exists? Who are the admins (store staff vs vendors vs Brennan)? | Shannon McNeil (+ Shawn Vink for corporate admin) | TO VERIFY — request from client via Shannon McNeil |
| 2 | Would new paid campaigns run in a NEW ad account (recommended) or an existing one? **Existing accounts: no agent touches them, period.** | Shannon McNeil decision | TO VERIFY — request from client via Shannon McNeil |
| 3 | TikTok Ads Manager / business account exists or needs creating? | Shannon McNeil (+ store) | TO VERIFY — request from client via Shannon McNeil |
| 4 | Google Ads account exists? (Group may hold one — no agent touches it without the gate.) New account under expanded scope? | Shannon McNeil (+ Shawn Vink) | TO VERIFY — request from client via Shannon McNeil |
| 5 | Reddit ads account (separate from any organic u/ account) — exists or needs creating? | Shannon McNeil | TO VERIFY — request from client via Shannon McNeil |
| 6 | Pixel / conversion tracking: Meta Pixel, TikTok Pixel, Google tag — do any exist on the store website? Who owns the website (vendor)? | Shannon McNeil (+ Shawn Vink; website vendor if any) | TO VERIFY — request from client via Shannon McNeil. **Pixel install touches the store website and is BLOCKED until the gate.** |
| 7 | Store website URLs and landing pages for ad destinations (inventory page, service page, GBP listing URL) | Shannon McNeil (+ store) | TO VERIFY — request from client via Shannon McNeil |
| 8 | Billing: which payment method and who authorizes it? (Retainer is NOT media spend — media budget is separate and client-funded.) | Shannon McNeil + client decision | TO VERIFY — request from client via Shannon McNeil |
| 9 | Lead handling: who answers lead-form submissions and how fast? | Shannon McNeil + store | TO VERIFY — request from client via Shannon McNeil (`PAID_MEDIA_FRAMEWORK.md` §4.2) |
| 10 | OEM/brand compliance rules for advertising (Kia, Ford) | Shannon McNeil (`CLIENT.md` §8.2) | TO VERIFY — request from client via Shannon McNeil |

**Rule:** a "BLOCKED" item is never worked around. If access is missing, the build plan proceeds on paper and stops at the platform boundary.

---

## 2. Build sequence (what the team CAN do now, on paper)

1. Fill the creative brief + ad copy per `AD_COPY_TEMPLATE.md` for the store's first test slot (from its approved content calendar).
2. Assemble media assets: the store's own photo/video (from `content/` — real lot, real staff, real service bay; TO VERIFY content assets with Shannon — `CLIENT.md` §8.2).
3. Draft the campaign structure per §3 (naming, hierarchy, budgets as PROPOSAL).
4. Draft the pixel/attribution plan per §4 (paper only).
5. Submit the full package to team lead → Shannon McNeil approval.
6. **STOP.** If Shannon confirms scope expansion + access, execute §5 checklists in-platform. Otherwise the package is a proposal on file.

---

## 3. Naming conventions and account structure (paper plan)

**Campaign naming (one scheme across platforms so reports line up):**
`[STORE]-[PLATFORM]-[OBJECTIVE]-[AUDIENCE]-[DATE-YYYYMM]`

Examples (paper only — nothing created):
- `S01-META-REACH-R25-A2534-2026MM`
- `S02-TIKTOK-LEADS-R25-SPARK-2026MM`
- `S03-REDDIT-ENGAGE-COMM-KW-2026MM`
- `S05-GOOGLE-LOCAL-R30-2026MM`

Key: store code (S01–S05), platform (META/TIKTOK/REDDIT/GOOGLE), objective (REACH/ENGAGE/TRAFFIC/LEADS/LOCAL), audience shorthand (R15/R25 = radius miles, A2534 = age band, SPARK, COMM-KW = community+keyword), and the month. Every ad set and ad appends its own suffix (e.g., `-AS1`, `-AD1`) per platform convention.

**Account structure rules (per-store specificity — `OPERATING_RULES.md`):**
1. **One store = one campaign set** (or one campaign per objective within that store's account/business portfolio). Never a group campaign mixing five stores — a GM must never see another store's spend in their report.
2. Store 03 and Store 04 are separate campaigns (separate addresses, separate budgets) even though they share a GM.
3. If the group prefers a single Business Manager/Ads account shell with five child structures, that decision is Shannon's + Shawn Vink's (**TO VERIFY**) — the REPORTING view stays per store regardless.
4. Existing accounts (Brennan's Facebook paid work, any group Google Ads): **not touched, not renamed, not paused, not read** without the gate.

---

## 4. Conversion / pixel / attribution setup notes (paper plan — all BLOCKED)

Attribution is where paid either earns trust or creates confusion. House rules:

1. **Pixel/tag install is a website change.** Meta Pixel, TikTok Pixel, Google tag all modify the store's website. Install requires: (a) the gate (scope expansion + access), (b) website access — owner TO VERIFY (store vendor vs Shawn Vink), (c) consent/compliance review with Shannon (OEM rules, privacy).
2. **What to install first (proposal):** Meta Pixel (PageView + Lead + Contact events), TikTok Pixel (PageView), Google tag (for Local campaigns + YouTube). One source of truth per store website — no duplicate tags from multiple vendors without Shannon's sign-off.
3. **Attribution windows (set once, documented, never silently changed):** house default 7-day click / 1-day view for Meta and TikTok; Google's default windows confirmed in-platform at build. Report the window on every ad report (`reporting/` notes column).
4. **Double-count discipline:** calls can come from GBP Insights and from ad platforms; direction requests likewise. The combined report (`PAID_MEDIA_FRAMEWORK.md` §10) presents these side by side, labeled by source, with a note — never blended silently.
5. **Lead forms vs website leads:** lead-form submissions (LD-1) are platform-native; website form leads need pixel events (BLOCKED until tag install). Until the tag exists, lead-form counts are reported as platform-reported only.
6. **No attribution = no scale claim.** If a pixel is not installed, the team reports reach/engagement/CTR (platform-reported) and does not claim website-driven outcomes.

---

## 5. Platform build checklists (execute ONLY after the gate opens)

Each checklist starts with the gate line. The team's current authorization is: **plan and draft only.**

### 5.1 Meta Ads Manager (Facebook + Instagram)

**Gate: BLOCKED until operator confirms scope expansion + access.**

1. Confirm access: Business Manager role, page access, ad account created under expanded scope (or confirmed safe to use the NEW account only). [Access TO VERIFY — Shannon/Shawn Vink]
2. Confirm billing setup on the ad account (client payment method; retainer NOT used). [TO VERIFY]
3. Set up the Meta Pixel or confirm existing tag (website access needed — BLOCKED until gate). [TO VERIFY]
4. Create campaign: objective (Reach / Engagement / Traffic / Leads / Local — per `PAID_MEDIA_FRAMEWORK.md` §3), name per §3.
5. Ad set: geo = 25-mile radius around the store address (house default — §4 of framework); age band per audience test A2; interests per test A3 (sizes TO VERIFY in-platform); budget = PROPOSAL amount; schedule aligned to the calendar.
6. Ad: media from the store's own content; primary text/headline/description/CTA per `AD_COPY_TEMPLATE.md` §4.1; destination URL or lead form (lead form template + response routing TO VERIFY with store).
7. Review pass: verification that every factual field is filled (no placeholders), OEM compliance check, approval trail logged.
8. Launch — **performed by Shannon or the store via Shannon's direction, never by an agent directly into the client's account without explicit operator confirmation.** (Agents may prepare the full build spec; the click belongs to the operator-approved process.)
9. First-week check: delivery, CTR, CPM vs proposal assumptions; any anomaly flagged to the operator.

### 5.2 TikTok Ads Manager

**Gate: BLOCKED until operator confirms scope expansion + access.**

1. Confirm TikTok for Business account exists (or create under expanded scope — account creation is a live action; BLOCKED until gate). [Access TO VERIFY — Shannon]
2. Confirm billing and the $50/day campaign floor / $20/day ad-group floor (third-party citing TikTok, verified 2026-08-12 — re-verify in-platform; `PAID_MEDIA_FRAMEWORK.md` §6.2). Budget proposal must respect the floor: bursts or lifetime budgets ≥ $50.
3. Pixel: TikTok Pixel on the store website (BLOCKED until gate + website access). [TO VERIFY]
4. Campaign: objective (Video views / Engagement first, Leads later — framework §6.3), name per §3.
5. Ad group: geo radius, age band, placement (TikTok feed), budget (burst or lifetime, respecting floors).
6. Ad: **Spark Ad** (authorize the store's organic video — requires the organic post to exist and the ad account to hold the authorization; TO VERIFY workflow in-platform) or standard in-feed video; caption + on-screen text per `AD_COPY_TEMPLATE.md` §4.2.
7. Review pass: no placeholders, sound-on captions present, OEM compliance.
8. Launch — operator-approved process only.
9. First-week check: views (K13), engagement, CPM, profile visits (K11).

### 5.3 Google Ads / YouTube

**Gate: BLOCKED until operator confirms scope expansion + access. Existing Greenway Google Ads account: not touched, ever, without the gate.**

1. Confirm account: NEW Google Ads account under expanded scope (recommended) vs existing (BLOCKED). [Access TO VERIFY — Shannon/Shawn Vink]
2. Confirm billing, conversion tracking plan (Google tag — website access BLOCKED until gate). [TO VERIFY]
3. **Keyword research** (Keyword Planner needs account access — BLOCKED): "Kia/Ford dealer [market]," "[model] [market]," "[market] car service." Volume and CPC reality checked in-platform before any proposal number is quoted.
4. Campaign types (proposal): **Local campaigns** for Store 05 (calls/directions) and **YouTube in-stream** built from the store's real walkarounds/Shorts (Stores 02, 03, 05 priority per framework §8). Search campaigns only after keyword research supports them.
5. Assets: headlines/descriptions per `AD_COPY_TEMPLATE.md` §4.4; video from the store's own footage.
6. Review pass: destinations verified (website/GBP — TO VERIFY), no placeholders, compliance.
7. Launch — operator-approved process only.
8. First-week check: impressions, CTR, call/direction actions, CPC vs proposal.

### 5.4 Reddit Ads Manager

**Gate: BLOCKED until operator confirms scope expansion + access.**

1. Confirm Reddit ads account (separate from any organic u/ account — structure TO VERIFY with Shannon). [Access TO VERIFY]
2. **Subreddit fit check FIRST** (BLOCKERS.md #6 — manual search/Apify; Reddit blocked automated search on 2026-08-12): which subreddits exist per metro, their rules on promotion. No Reddit activity (organic or paid) before fit is confirmed (`BENCHMARKS.md` §5).
3. Confirm billing and minimum-budget facts (official FAQ Cloudflare-blocked — manual verification needed — 2026-08-12; `PAID_MEDIA_FRAMEWORK.md` §7.2). [TO VERIFY]
4. Campaign: objective (Reach/Engagement first), targeting = community + keyword per fit check, geo options confirmed in-platform (TO VERIFY).
5. Ad: Conversations-style (title/body per `AD_COPY_TEMPLATE.md` §4.3) or carousel/image; copy in Reddit's voice; no hype.
6. Review pass: does this read like a useful local answer, not a billboard? Removal-safety check (zero-removal target — `KPI_FRAMEWORK.md` §4.5).
7. Launch — operator-approved process only.
8. First-week check: CTR, comments/upvotes, sentiment scan, spend pace.

---

## 6. TO VERIFY master list for account access (via Shannon; corporate via Shawn Vink)

- [ ] Meta Business Manager admin list + vendor split (Brennan's role definition included) — BLOCKERS.md #1
- [ ] Whether paid runs in NEW ad accounts (recommended) — Shannon decision
- [ ] TikTok for Business account status — Shannon
- [ ] Google Ads account status — Shannon/Shawn Vink
- [ ] Reddit ads account status — Shannon
- [ ] Website ownership + access for pixel/tag install (vendor vs Shawn Vink) — Shannon
- [ ] Pixel/tag existence on store websites — Shannon (or website vendor)
- [ ] Destination URLs (inventory page, service page, GBP listing) — Shannon/store
- [ ] Billing arrangement for media budgets (client-funded, separate from retainer) — Shannon/client
- [ ] Lead-handling owner + response-time target per store — Shannon/store
- [ ] OEM advertising compliance rules — Shannon (`CLIENT.md` §8.2)
- [ ] Store content assets for ad creative (photos/video/inventory feed) — Shannon (`CLIENT.md` §8.2)
- [ ] Platform minimums re-verified in-platform at build (TikTok floors, Reddit budget FAQ, Meta specs) — build-time
- [ ] Attribution window decisions per platform — team + Shannon
- [ ] Pilot start date (for scheduling all proposals) — Shannon (`CLIENT.md` §8.3)

---

## 7. Drift flags (repeat from framework §11 — escalate to operator)

1. Any request to "just boost" a post, spend money, or log into an existing ad account.
2. Any auto-applied campaign or recommendation accepted without review.
3. Any budget figure discussed with a GM before Shannon approves the proposal.
4. Any attempt to coordinate with Brennan on Facebook paid.
5. Any agent creating, modifying, pausing, or funding a live campaign. The gate is unconditional: **"BLOCKED until operator confirms scope expansion + access."**

---

*End of guide. INTERNAL DRAFT — the team's current authorization is plan-and-draft. Nothing is created inside a live ad platform, no pixel is installed, and no money moves until Shannon McNeil confirms expanded scope and access.*
