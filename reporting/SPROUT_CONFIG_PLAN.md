# SPROUT_CONFIG_PLAN.md — Sprout Social Configuration Plan (Month 2, Greenway Auto Group Pilot)

**Status:** INTERNAL DRAFT — planning work only. NOT client-facing. Nothing is published, launched, or touched in any live account. Shannon McNeil approves before anything leaves the team.
**Owner:** Bright Matter LLC agency operations team (Reporting Analyst)
**Date:** 2026-08-22 (plan written; every connection state below is TO VERIFY)
**Applies to:** Month 2 — Strategy & Build (mid-Sep – mid-Oct) of the six-month organic pilot across 5 rooftops.

> **Read this first (operating boundary):** This is a **plan only**. No account is created, no profile is connected, no approval workflow is enforced on a live system, and **no agent ever publishes.** A human on the Greenway/Shannon side operates Sprout and does all publishing. Agents draft, feed, and analyze content; they never hold publish rights and never touch a live account without the operator's explicit confirmation. Every line below marked **TO VERIFY** stays TO VERIFY until Shannon McNeil (and Shawn Vink for admin/access) confirms it.

---

## 1. Purpose & Scope

### 1.1 What Sprout is configured to do for the pilot
Sprout Social is the single **human-operated** publishing-and-measurement hub for the pilot's organic social channels. The operator has confirmed (2026-08-22) that Sprout access is available and that **most profiles/pages across the five rooftops are already connected.** Because accounts are largely already connected, **Month 2 Sprout work is configuration, not fresh connection:**

1. **Verify** what is actually connected in Sprout right now (nothing has been logged yet — see §2).
2. **Organize** the connected profiles by pilot store/rooftop so each store is isolated (see §3).
3. **Configure** per-store publishing queues, the approval workflow, and reporting so they match the pilot (see §4, §5).
4. **Document** the human-operated workflow that a store employee can eventually run without Bright Matter (see §6).

Sprout is used for **active-publishing channels: Facebook, Instagram, TikTok** (primary), plus **YouTube** (support). Reddit is **monitor-only** (no pilot rooftop publishes on Reddit). Google Business Profile is **back-burnered** this phase (no GBP publishing/config priority).

### 1.2 In-scope vs out-of-scope (the explicit line)
**IN SCOPE (what this plan covers):**
- Verifying which profiles are already connected in Sprout and recording them per store.
- Organizing connected profiles into per-store groups so each rooftop is isolated with its own queue.
- Configuring publishing queues, the approval workflow, and reporting/tagging to match the pilot.
- Documenting the human-operated workflow and a store-employee runbook (train-the-trainer).
- Preparing reporting/tagging conventions so Sprout data feeds the existing KPI framework and per-store dashboards.

**OUT OF SCOPE (explicitly NOT covered — do not do in Month 2):**
- **No account/page creation.** Creating a new Facebook, Instagram, TikTok, or YouTube account is out of scope. Any store missing a channel (Store 03/05 TikTok; Store 05 IG; Store 03 YouTube attribution) is an **absence/attribution item for governance or GM discussion — not a connection action** and never a unilateral "let's create/merge it."
- **No live publishing by agents.** Agents never publish. Publishing is done by a human on the Greenway/Shannon side.
- **No enforcement of approvals on a live, client-visible system this month.** The approval configuration is *designed* here; it goes live as part of Month 3 execution after Shannon signs off.
- **No paid spend, no touching any existing ad account** (including Facebook paid / Brennan's informal role). The SOW is organic-only. `OPERATING_RULES.md` §3 hard line applies.
- **No Reddit publishing and no GBP priority work.** Reddit stays monitor-only; GBP stays back-burnered for this phase.

### 1.3 Cost / commercial scope note (for the record)
Per `CLIENT.md` §4 commercial terms: the flat **$10,000/month** is the engagement fee. **Sprout Social licensing is billed separately at cost** (via Shawn Vink, corporate IT, routed through Shannon). So:
- Sprout **configuration, queue/approval setup, reporting setup, and the runbook** — part of the $10k/mo flat (Month 2 build work). **In scope of the flat.**
- Sprout **license fees** (per-seat/per-profile) — **out of the flat, billed at cost** to the client. **This plan does not price or provision licenses**; that is a Shannon/Shawn purchasing decision. It only defines how whatever licenses exist are organized.
- No Sprout, GBP (Local), or additional product purchase is proposed or priced here.

---

## 2. Verify-Connected Checklist (per store × channel — all TO VERIFY)

> **No one has logged what is actually connected in Sprout.** Every row below is **TO VERIFY** until Shannon (and Shawn Vink for corporate admin) confirms what is connected today. This checklist is the **Step 1 verification** to run against the live Sprout account — it cross-references `channel-matrix.csv` and each `stores/store-NN/STORE.md` (the canonical source of truth) and does **not** invent any handle.

**Status key:** `TO VERIFY` = confirm connected/unconnected in Sprout. `CONNECT` = connect if present (active-publish or support channel). `DO NOT CONNECT` = keep out of Sprout (hygiene/duplicate/dead). `ABSENCE ITEM` = store has no such account — a governance/GM-discussion item, **not** a connection action. `MONITOR-ONLY` = Reddit. `BACK-BURNERED` = GBP.

### Store 01 — Greenway Kia West Palm Beach (GM Mike Wangle, West Palm Beach, FL) — `channel-matrix.csv` row 2
| Channel | Sprout action | Connection status (log after verification) |
|---|---|---|
| Facebook — primary `facebook.com/GreenwayKiaWestPalmBeach` (Active) | **CONNECT** (primary) | TO VERIFY |
| Facebook — duplicate `facebook.com/greenwaykiawpb` | **DO NOT CONNECT** — hygiene item; duplicate page recorded for GM one-on-one | TO VERIFY (confirm it is disconnected; if currently connected, flag) |
| Instagram — `instagram.com/greenwaykiawpb/` (Active) | **CONNECT** | TO VERIFY |
| TikTok — `tiktok.com/@greenwaykiawestpalmbeach` (Active) | **CONNECT** | TO VERIFY |
| YouTube — `youtube.com/@greenwaykiawestpalmbeach9572` (Active, operator-confirmed 2026-08-22) | **CONNECT (support)** | TO VERIFY |
| Reddit | **MONITOR-ONLY** (no pilot publishing) | TO VERIFY (any connected sub/listen surface) |
| Google Business Profile | **BACK-BURNERED** this phase | OUT (deferred) |

### Store 02 — Greenway Kia at the Avenues (GM Emre Sevinir, Jacksonville, FL) — `channel-matrix.csv` row 3
| Channel | Sprout action | Connection status (log after verification) |
|---|---|---|
| Facebook — `facebook.com/GreenwayKiaAtTheAvenues/` (Active) | **CONNECT** | TO VERIFY |
| Instagram — `instagram.com/greenwaykiajax/` (Active) | **CONNECT** | TO VERIFY |
| Instagram — duplicate `instagram.com/greenwaykia.jax/` (**INACTIVE**, operator-confirmed 2026-08-22) | **DO NOT CONNECT** — hygiene/cleanup item for GM one-on-one (confirm disconnected; never publish to it) | TO VERIFY |
| TikTok — `tiktok.com/@greenwaykiajax` (Active) | **CONNECT** | TO VERIFY |
| YouTube — `youtube.com/@greenwaykiaattheavenues-b6h` (CONFLICT RESOLVED as the real channel, operator 2026-08-22) | **CONNECT (support)** | TO VERIFY |
| Reddit | **MONITOR-ONLY** | TO VERIFY |
| Google Business Profile | **BACK-BURNERED** | OUT (deferred) |

### Store 03 — Greenway Kia Rivergate (GM James Galuszka, Madison, TN) — `channel-matrix.csv` row 4
| Channel | Sprout action | Connection status (log after verification) |
|---|---|---|
| Facebook — `facebook.com/greenwaykiarivergate` (Active) | **CONNECT** | TO VERIFY |
| Instagram — `instagram.com/greenwaykiarivergate/` (Active) | **CONNECT** | TO VERIFY |
| TikTok | **ABSENCE ITEM** — no account found (web 2026-08-22). NOT a connection action; recorded for GM discussion. | TO VERIFY (confirm no TikTok to connect) |
| YouTube — currently on old `youtube.com/@universalkia` handle (attribution **UNCLEAR**, operator 2026-08-22) | **FLAG / DO NOT resolve unilaterally** — governance & cleanup item. Confirm with Shannon which channel(s) should be connected for Store 03 before connecting. | TO VERIFY (conflict) |
| Reddit | **MONITOR-ONLY** | TO VERIFY |
| Google Business Profile | **BACK-BURNERED** | OUT (deferred) |

### Store 04 — Greenway Kia Hickory Hollow (GM James Galuszka, Antioch, TN) — `channel-matrix.csv` row 5
| Channel | Sprout action | Connection status (log after verification) |
|---|---|---|
| Facebook — `facebook.com/greenwaykiahickoryhollow/` (Active) | **CONNECT** | TO VERIFY |
| Facebook — legacy `facebook.com/universalkiahickoryhollow` (dead) | **DO NOT CONNECT** — hygiene item | TO VERIFY |
| Instagram — `instagram.com/greenwaykiahh/` (Active) | **CONNECT** | TO VERIFY |
| Instagram — legacy `instagram.com/universalkiahh/` (dead) | **DO NOT CONNECT** — hygiene item | TO VERIFY |
| TikTok — `tiktok.com/@greenwaykia.hicko` (Active) | **CONNECT** | TO VERIFY |
| YouTube — `youtube.com/@greenwaykiahickoryhollow` (Active, operator-confirmed) | **CONNECT (support)** | TO VERIFY |
| YouTube — `@universalkia` shared/current with Store 03 (attribution UNCLEAR) | **FLAG / DO NOT silently attribute** — governance & cleanup item; confirm which rooftop owns/publishes it | TO VERIFY (conflict) |
| Reddit | **MONITOR-ONLY** | TO VERIFY |
| Google Business Profile | **BACK-BURNERED** | OUT (deferred) |

### Store 05 — Greenway Ford Kansas City (GM Shane Silvey, Raytown, MO) — `channel-matrix.csv` row 6
| Channel | Sprout action | Connection status (log after verification) |
|---|---|---|
| Facebook — `facebook.com/greenwayfordraytown` (Active) | **CONNECT** | TO VERIFY |
| YouTube — `youtube.com/@GreenwayFordofKansasCity-zw6sj` (Active) | **CONNECT (support)** | TO VERIFY |
| Instagram | **ABSENCE ITEM** — no account found (web 2026-08-22). Not a connection action. | TO VERIFY |
| TikTok | **ABSENCE ITEM** — no account found (web 2026-08-22). Not a connection action. | TO VERIFY |
| Reddit | **MONITOR-ONLY** | TO VERIFY |
| Google Business Profile | **BACK-BURNERED** | OUT (deferred) |

### 2.1 Explicit hygiene callouts (things that should NOT be connected or must be flagged)
These are **account-hygiene / governance items**, held for GM one-on-ones (never group settings) per `OPERATING_RULES.md`. None is a connection or cleanup action on the live Sprout account by an agent:
- **Store 01:** duplicate FB page `facebook.com/greenwaykiawpb` — do not connect; flag if currently connected.
- **Store 02:** inactive duplicate IG `instagram.com/greenwaykia.jax` (operator-confirmed inactive 2026-08-22) — do not connect; unauthorized-account cleanup for GM Emre Sevinir one-on-one.
- **Store 04:** legacy dead "Universal Kia" accounts (FB `universalkiahickoryhollow`, X `x.com/UniversalKiahh`, IG `universalkiahh`) — do not connect.
- **Store 03/Store 04:** YouTube `@universalkia` attribution is **UNCLEAR** — flag, do not resolve or attribute unilaterally (governance/cleanup item for GM one-on-ones and the governance model, per `CLIENT.md` §8.1).
- **Store 03 / Store 05 missings** (03 TikTok; 05 IG + TikTok) are **absence items**, not connection items.

---

## 3. Recommended Sprout Structure

**Organize Sprout by rooftop, not by channel type.** Configure one **Sprout Group per pilot store** (Store 01–05) in the platform (Sprout's Groups let you segment profiles, queues, calendars, and approvals). Each group holds **that store's own active profiles** and **nothing else.**

- **Group name = store** (e.g., `Greenway Kia West Palm Beach`), so the GM sees their own store, not a group template.
- Each group gets its **own Publishing queue, its own calendar view, and its own approval workflow** — never a shared group queue where five store-specific deliverables collide.
- Reddit listen surfaces are attached **at the account/admin level as monitor-only** (or a single shared listen stream), not to a store's publishing group — no store publishes on Reddit.
- GBP is **not assigned to a publishing group** this phase (back-burnered). If Sprout's Local/GBP product is licensed later, it lands here — see §7 open item 8.

**Why per-store groups:** each rooftop is its own market with its own GM, competitive set, and content voice (`CLIENT.md` §3). A store employee must eventually run *their* store; an isolated group per store is what makes that handoff possible. One shared queue would force a group template — explicitly disallowed.

**Structure to build after verification (concrete):**

| Sprout Group | Active profiles connected | Publish channels | Support/monitor |
|---|---|---|---|
| Group 01 — Greenway Kia West Palm Beach | FB (primary) · IG (@greenwaykiawpb) · TikTok | FB, IG, TikTok | YouTube (support) |
| Group 02 — Greenway Kia at the Avenues | FB · IG (@greenwaykiajax) · TikTok | FB, IG, TikTok | YouTube (support) |
| Group 03 — Greenway Kia Rivergate | FB · IG | FB, IG | YouTube attribution TO VERIFY |
| Group 04 — Greenway Kia Hickory Hollow | FB · IG (@greenwaykiahh) · TikTok | FB, IG, TikTok | YouTube (support) |
| Group 05 — Greenway Ford Kansas City | FB | FB | YouTube (support) |

*(All inner cells still subject to §2 verification; YouTube for 01/02/05 confirmed, 03/04 attribution TO VERIFY.)*

---

## 4. Publishing Queues & Approval Workflow

### 4.1 The human-in-the-loop model (who does what)
Agents (Bright Matter) **draft and feed**; Shannon **reviews and approves**; a **store/Greenway human publishes in Sprout**. Agents never publish.

| Swimlane | Who | Sprout role | Where the work lives |
|---|---|---|---|
| **Draft** | Bright Matter agents (Content Strategist drafts; Reporting Analyst sets measurement) | None required — content is prepared **off-platform** in the team workspace (calendar → brief → ready copy + media) and handed to Shannon. **Whether agents get a draft-only Sprout login is a Shannon decision (TO VERIFY); until granted, agents stay off-platform.** | Team workspace: `content/CONTENT_CALENDAR_TEMPLATE.md`, `content/CREATIVE_BRIEF.md`, per-store calendar |
| **Review / Approve** | Shannon McNeil | **Approver/Admin** — loads approved content into Sprout as `Approved` and schedules (or grants a limited schedule role to the store human). | Sprout |
| **Publish** | Store/Greenway human (at Shannon's direction) | **Publisher** — hits publish on `Approved`/scheduled items; handles phone-native Stories at Shannon's direction | Sprout + native apps |

**Hard rule (repeat):** `OPERATING_RULES.md` §2 — agents never hold publish rights to Sprout and never publish. The approval pipeline (`WORKFLOW.md`) — specialist drafts → team lead reviews → Shannon approves → client/publish — holds in Sprout exactly as it does outside.

### 4.2 Queue naming & posting cadence
**Queue naming — one queue per store, named by store:** `[S01] Greenway Kia West Palm Beach · FB/IG/TikTok`, `[S02] Greenway Kia at the Avenues`, `[S03] Greenway Kia Rivergate`, `[S04] Greenway Kia Hickory Hollow`, `[S05] Greenway Ford Kansas City`. Keep the store number prefix so the queue maps 1:1 to `store-NN` folders and dashboards.

**Approval status → Sprout state mapping** (from `TRAIN_THE_TRAINER_PLAYBOOK.md` Module 4):
- Only `Approved` items are scheduled/published.
- `Draft`, `Lead review`, and `Edits needed` items are **never** scheduled.

**Posting cadence — house default (from `KPI_FRAMEWORK.md` §8 / `CONTENT_STRATEGY_FRAMEWORK.md` §8), applied per store, to be confirmed with Shannon:**
- Facebook: 3–5 posts/week
- Instagram: 3–5 feed posts + 3–5 Stories/week
- TikTok: 3–5 videos/week
- YouTube (support): 1 Short/week + 1 long-form/month
- *(Reddit: monitor-only — no cadence; GBP: none this phase.)*

**Content pillar mix — LOCKED 2026-08-22 (operator sign-off). Configure Sprout and the KPI baseline against these, not against the rev-1 default.**

> The 30/20/15/20/15 figure this section previously carried was the **rev-1 group default**, with rev-1 pillar names (Service & Trust, People & Place). It is superseded. The locked targets are **per store and per channel**, counted over **Tier A/B posts only** — Tier C (per-VIN walkarounds, static offer and compliance graphics, hours and milestone posts) is published but **never fills a mix slot**, so it must be excluded from mix reporting or every store will read as off-target.

| Store | Instagram (1b/2/3/4/5b) | TikTok (1b/2/3/4/5b) | Facebook (1b/2/3/4/5b) |
|---|---|---|---|
| 01 West Palm Beach — full | 35 / 25 / 20 / 10 / 10 | 30 / 15 / 40 / 10 / 5 | 30 / 25 / 5 / 25 / 15 |
| 02 at the Avenues — full | 35 / 25 / 20 / 10 / 10 | 30 / 15 / 40 / 10 / 5 | 30 / 25 / 5 / 25 / 15 |
| 03 Rivergate — minimum viable | 40 / 30 / 10 / 10 / 10 | *no TikTok account* | 33 / 27 / 5 / 25 / 10 |
| 04 Hickory Hollow — minimum viable | 40 / 30 / 10 / 10 / 10 | 45 / 30 / 10 / 10 / 5 | 33 / 27 / 5 / 25 / 10 |
| 05 Ford Kansas City — asset-led | *pending Phase-1 stand-up* | *pending Phase-1 stand-up* | 30 / 20 / 15 / 18 / 17 |

**Three configuration consequences.** (a) **Store 05's mix is Facebook-only** — it has no Instagram or TikTok account today, and those slot targets are deliberately unset pending 30 days of real baseline after stand-up. Do not fill them with the group default. (b) **Store 03 has no TikTok** — leave the column empty rather than defaulting it. (c) **Community (P4) is gated at 10%** on the personality channels at Stores 01–04 and rises to 20% only when that store's local hook list is confirmed; build the target as a variable, not a constant.

**Baseline caveat — carry this into the dashboard build.** The mixes are locked for calendar and production planning but are **provisional as a measurement baseline** until account consolidation completes at Stores 01, 03 and 04. Per pilot brief kill criterion 5, a rooftop still running duplicate accounts at day 30 is reported as a **blocked baseline, not underperformance**. Configure now; flag those three stores' attribution as provisional until their canonical handles are confirmed and duplicates retired.

### 4.3 The approval steps (in Sprout, once live in Month 3)
1. Shannon loads the agents' ready content package into the store's Sprout group as a **draft** (agents have prepared copy + media + intended slot + CTA off-platform).
2. Shannon reviews against the creative brief and pillar mix; **approves** or returns **edits needed** (fed back to agents for revision).
3. Approved items move to the store's queue with the planned date/time; the **store/Greenway human publishes** at the scheduled time (or Shannon schedules on their behalf).
4. Reddit: no publishing — only monitor/listen in the admin-level stream; GBP: not in the publishing flow this phase.

---

## 5. Reporting Configuration

### 5.1 How Sprout reporting feeds the existing framework
Sprout is **one source among several** for the KPI framework (`KPI_FRAMEWORK.md` §7). It pulls platform-native metrics into one place and adds per-post tagging. It does **not** replace native tools: message/DM response lives in native inboxes, Reddit has no native analytics (manual), and GBP is separate. Reporting setup:

- **One Sprout report per store group** (Group 01–05), so numbers stay per store × channel — **never** a group rollup that blurs stores (`KPI_FRAMEWORK.md` §1.4).
- **Pull cadence:** capture all monthly numbers from Sprout on the **same fixed day every month** (date TO VERIFY — e.g., the 1st), then fill the store's `dashboards/store-NN/DASHBOARD.csv` row and produce the GM report via `REPORTING_TEMPLATE.md`. Screenshot the Sprout report as capture evidence (mirror audit evidence practice). Match native-insight lookback windows at first capture (TO VERIFY).
- Sprout supplies or corroborates: K1 Reach, K2 Impressions, K3 Engagement rate (computed from interactions/impressions on post level), K4 Follower growth, K5 Posts published (+ mix check), K6 Saves, K7 Shares, K8 Comments, K11 Profile visits, K12 Link taps, K13 TikTok/YouTube views, K14 YouTube watch time, K15 YouTube subscribers.
- **Still from native tools, not Sprout:** K9/K10 DMs & message response (native inboxes), K16 Reddit (manual), K17–K23 GBP (back-burnered / later), and any metric Sprout's connection doesn't surface (flag as a gap rather than guess).

### 5.2 Tagging / labeling conventions (critical for the monthly report)
Apply **Sprout tags/labels to every published post** so each post can be attributed to *store, channel, and pillar* for the monthly content-mix check (K5) and "what's working" analysis (`REPORTING_TEMPLATE.md` §4). **Three required tags on every post:**

1. **Store tag:** `store-01` … `store-05` (matches `stores/store-NN` and `dashboards/store-NN`).
2. **Channel tag:** `fb` · `ig` · `tt` · `yt` (matches DASHBOARD column prefixes).
3. **Pillar tag:** `pillar-1-inventory` · `pillar-2-service-trust` · `pillar-3-people-place` · `pillar-4-community-local` · `pillar-5-reviews-proof` (matches `content/pillars/PILLARS.md` §3).

**Why:** the monthly report needs (a) per-store × per-channel numbers (dashboard columns), and (b) the **content-mix check** (did the store post roughly its pillar mix?) which only works if every post carries a pillar tag. Without tags, the mix check and "what's working" become manual guesses. Tag structure TO VERIFY against the live Sprout tag system (names may differ); the *semantics* above are the spec.

### 5.3 Reporting flow to the GM report
Per store per month: extract Sprout report → map to `KPI_FRAMEWORK.md` KPIs → fill `DASHBOARD.csv` row (TO VERIFY cells stay TO VERIFY) → build `MONTHLY_REPORT-<period>.md` via `REPORTING_TEMPLATE.md` → quarterly variant at end of Months 3 and 6. GM/COO views follow `GM_KPI_FRAMEWORK.md` (per-rooftop five-core-metric view + COO one-page rollup with **five named rows**, never an opaque group number).

---

## 6. Onboarding & Train-the-Trainer (runbook so a store employee can operate it without Bright Matter)

This section is the **Sprout-specific runbook**; it aligns with and extends `content/governance/TRAIN_THE_TRAINER_PLAYBOOK.md` (Module 4 — Scheduling and publishing). A store employee (trainee) learns to read and run **their own store's group only.**

1. **Orientation — how the pipeline works.** The approval chain (agents draft → Shannon approves → store human publishes in Sprout). The trainee learns the calendar and the creative brief (Modules 1–3 of the playbook).
2. **Sprout access.** Shannon controls all Sprout access and grants the store trainee at most a **limited scheduling role** (or draft-only) in *their store's* group. Agents never hold publish rights. Trainees learn what Shannon allows and never publish outside their own store's group.
3. **The store group — learn it cold.** The trainee names their store's group, its connected profiles (§2), and confirms the hygiene items are NOT connected (no duplicate/legacy accounts in the queue).
4. **Scheduling within approved items only.** Only `Approved` items are scheduled. `Draft` / `Lead review` / `Edits needed` are never scheduled. Trainee learns the approval-status → Sprout-state mapping (Module 4).
5. **Posting cadence & pillar mix.** Trainee learns their store's cadence (FB/IG/TikTok numbers from §4.2) and the pillar mix check — tags every approved post and checks the store's mix against its target (30/20/15/20/15 as starting default, per-store confirmed).
6. **Publishing and phone-native content.** Trainee uses Sprout for scheduled posts; Instagram Stories shot on a phone are used at Shannon's direction and logged in the calendar. The trainee never publishes Reddit; they know Reddit is monitor-only and GBP is back-burnered this phase.
7. **Responding & reporting.** Trainee learns comment/DM response flow (sensitive items escalate to Shannon, never the trainee's discretion alone), and reads their store's monthly dashboard — they learn **to read it, not to invent numbers** (Module 5). They run the fixed monthly capture day in Sprout, map to the dashboard, and hand the raw capture to the Reporting Analyst / Shannon.
8. **Handoff progression.** Observe (Months 1–2) → co-create (Month 3) → own (Month 4) → run (Month 5–6), per the playbook's six-month progression. **Month 6 readiness** = the store employee can run the queue, approvals they're granted, and reporting capture without Bright Matter in the loop daily.

**Training gatekeep:** a trainee only operates the parts they've been *explicitly granted* by Shannon. Cadence and access are Shannon-approved capacity decisions per store (TO VERIFY), never promises.

---

## 7. Open Items / To Verify

Everything below needs confirmation before this plan becomes a live configuration. None is assumed.

1. **[HARD BLOCKER] What is actually connected in Sprout right now** — the entire §2 checklist returns `TO VERIFY`. **Needs Shannon/Shawn Vink to confirm** what is connected today (per store × channel), so the plan can mark `CONNECT` / `DO NOT CONNECT` actuals. This is the first action in Month 2.
2. **Who holds Sprout admin access / roles.** Admin, approver, and publisher role holders — **Shannon + Shawn Vink (corporate IT)** to confirm. Determines the §4 swimlanes and whether agents ever get a draft-only login (a decision only Shannon makes — until granted, agents stay off-platform).
3. **Store 03/04 YouTube attribution.** Whether `@universalkia` is the shared/primary current channel for both Rivergate & Hickory Hollow vs Store 04's own `@greenwaykiahickoryhollow`, and which should be connected to which Sprout group. **Governance/cleanup item — do not resolve unilaterally** (`CLIENT.md` §8.1). Needs Shannon (and GMs via her) to confirm.
4. **Hygiene-item resolutions.** Store 01 dup FB, Store 02 inactive dup IG, Store 04 legacy dead Universal Kia — confirm each is (or remains) **disconnected** from Sprout and take the resolution forward as GM-discussion findings, not agent cleanup actions.
5. **Absence items.** Store 03 TikTok, Store 05 IG + TikTok — confirm no Sprout connection is expected; record as GM discussion items (not connection actions).
6. **Posting cadence + monthly capture date.** Per-store cadence (`KPI_FRAMEWORK.md` §8 defaults) and the fixed monthly reporting/capture day — **Shannon to confirm**.
7. **Pillar mix — RESOLVED 2026-08-22.** The per-store, per-channel targets are **locked by operator sign-off** (see the pillar-mix section above and each `stores/store-0X/STRATEGY.md` §3). No longer an open item. What remains open is narrower: the **Community gate** per store (10% → 20% on hook confirmation), **Store 05's IG/TikTok slot targets** (held pending 30 days post-stand-up), and the **provisional-baseline flag** on Stores 01, 03 and 04 until duplicates are retired.
8. **Sprout Local / GBP product in scope?** GBP is back-burnered this phase, so Sprout's Local/GBP product is **likely out for now** — **Shannon to confirm** whether any GBP-connected product/license exists or should be deferred. If deferred, GBP has no Sprout placement this phase (§3 keeps it out of publishing groups).
9. **Sprout license scope (billing).** What licenses/profiles are provisioned and the **at-cost** billing arrangement (`CLIENT.md` §4) — **Shannon + Shawn Vink** to confirm. This plan configures existing licenses only; it provisions nothing and prices nothing.
10. **Tag-system names.** Sprout's actual tag/label fields — verify against the live system so the §5.2 tag spec maps cleanly (semantics are fixed; labels are TO VERIFY).
11. **Reddit listen surface.** Confirm what Reddit monitor/listen surface exists (or will be added) at the admin level — **Shannon/Shawn** to confirm; no publishing on Reddit regardless.

---

## 8. Relationship to the rest of the workspace
- **Source of truth for channels:** `channel-matrix.csv` + `stores/store-01..05/STORE.md` (do not invent handles).
- **Commercial terms / pilot scope:** `CLIENT.md` §4, §6a, §8.3.
- **Approval pipeline:** `WORKFLOW.md`; operating rules in `OPERATING_RULES.md` (esp. §2 no-agent-publish, §3 live-paid hard line).
- **Content inputs:** `content/pillars/PILLARS.md` (§3 mix), `content/CONTENT_STRATEGY_FRAMEWORK.md` (§7–8 cadence), `content/CONTENT_CALENDAR_TEMPLATE.md`.
- **Reporting outputs:** `reporting/KPI_FRAMEWORK.md` (§6–7), `reporting/GM_KPI_FRAMEWORK.md`, `reporting/DASHBOARD_TEMPLATE.md` + `reporting/dashboards/store-NN/DASHBOARD.csv`, `reporting/REPORTING_TEMPLATE.md`.
- **Handoff:** `content/governance/TRAIN_THE_TRAINER_PLAYBOOK.md` (Module 4) and `content/governance/GOVERNANCE_MODEL.md`.

*End of plan — all connection states unverified and marked TO VERIFY; nothing executed, created, or published.*
