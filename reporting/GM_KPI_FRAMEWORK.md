# GM_KPI_FRAMEWORK.md — Distilled KPI Framework: GM View + COO Rollup

**Status:** INTERNAL DRAFT — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Reporting Analyst)
**Source documents:** `reporting/KPI_FRAMEWORK.md` (full KPI set; this file distills it, not a rewrite), `reporting/REPORTING_TEMPLATE.md`, `audit/workbook/BLOCKERS.md`, `CLIENT.md`
**Applies to:** Greenway Auto Group pilot — 5 rooftops × 6 channels. Two audiences, always distinguished: the store-level view for each GM, the group rollup for Casey Coffey (COO).

---

## 0. What this document is

The GM-facing distillation of the full KPI framework: one number per row, five rows per rooftop, one rollup table for the COO. Every metric below is already defined in `KPI_FRAMEWORK.md` (K-numbers cited). Nothing here invents a metric, and nothing here is filled with real data yet. Every cell that needs access the team does not have stays **TO VERIFY — request from client via Shannon McNeil**, with the blocker owner named.

The sponsor's stated operating problem is gaining visibility across many dealerships at once. This file answers it with two views that never mix:

1. **Per-rooftop scorecard (the GM view)** — what one store's GM reads on a phone between customers.
2. **Group rollup (the COO view)** — five named rows, one per rooftop, never one anonymous number.

## 1. The five core metrics

Five metrics repeat across rooftops with store-specific notes (per-store specificity, not a group template). They map to `KPI_FRAMEWORK.md` K-numbers and `REPORTING_TEMPLATE.md` rows.

| # | Metric (plain name) | K-number | Where the number comes from |
|---|---|---|---|
| 1 | Calls from Google | K19 | GBP Insights |
| 2 | Directions from Google | K18 | GBP Insights |
| 3 | Social messages (DMs) | K9 (+ response K10) | Meta Business Suite inbox (FB, IG), TikTok inbox, Reddit messages |
| 4 | New Google reviews and rating | K21 (+ response K22) | GBP Insights + public profile |
| 5 | Store-specific fifth metric | K5 / K20 / K1 | see each store's table |

Why these five: a GM's business runs on inquiries (calls, directions, messages), reputation (reviews, rating), and the freshness of the store's presence (posts, clicks, reach). Everything else the pilot tracks (saves, shares, watch time, Reddit participation health) explains why these move and stays in the dashboard, not on the GM scorecard (`KPI_FRAMEWORK.md` §5).

## 2. The GM view — per rooftop

Store context lines cite observed public data from `audit/workbook/` (Google Maps listing, 2026-08-12). Account ownership (BLOCKERS.md #1), performance baselines (#2), and who posts today (#6) are blocked on **Shannon McNeil** (corporate/admin access via **Shawn Vink** where applicable).

### 2.1 Store 01 — Greenway Kia West Palm Beach (GM Mike Wangle, West Palm Beach, FL)

**Store context (observed 2026-08-12, workbook store-01/audit.csv):** GBP rating 4.5★. Listing owner posts observed through Jun 18, 2026, then quiet at audit. Full review count and GBP Insights: TO VERIFY.

| # | Metric | Why it matters to this store (1 line) | Data source | Access status |
|---|---|---|---|---|
| 1 | Calls from Google | The most direct demand signal a listing produces — a caller is ready to talk. | GBP Insights | TO VERIFY — Shannon McNeil (GBP owner access) |
| 2 | Directions from Google | Shows whether the listing pulls people toward 735 S Military Trl. | GBP Insights | TO VERIFY — Shannon McNeil |
| 3 | Social messages (DMs) | Inquiries people did not want to make by phone — likely uncounted leads today. | Meta Business Suite / TikTok inbox | TO VERIFY — Shannon McNeil (BLOCKERS #1/#2) |
| 4 | New Google reviews and rating | At 4.5★ the store clears the bar many shoppers set (`BENCHMARKS.md` §4.1) — hold it and grow the flow. | GBP Insights + public profile | Rating observed 2026-08-12; count + insights TO VERIFY |
| 5 | Google posts published vs plan | Listing posts went quiet after Jun 18, 2026 (observed) — freshness is this store's gap to close. | Content calendar + GBP | Calendar team-owned; GBP access TO VERIFY |

### 2.2 Store 02 — Greenway Kia at the Avenues (GM Emre Sevinir, Jacksonville, FL)

**Store context (observed 2026-08-12, workbook store-02/audit.csv):** GBP rating 4.6★ — highest of the five. Listing posts current (Aug 6, 2026). Review count and insights: TO VERIFY.

| # | Metric | Why it matters to this store (1 line) | Data source | Access status |
|---|---|---|---|---|
| 1 | Calls from Google | The pilot's highest-rated store — calls are the payoff this reputation earns. | GBP Insights | TO VERIFY — Shannon McNeil (GBP owner access) |
| 2 | Directions from Google | Jacksonville shoppers navigate to 10564 Philips Hwy; taps = intent to visit. | GBP Insights | TO VERIFY — Shannon McNeil |
| 3 | Social messages (DMs) | Dense metro — shoppers message before they visit; reply speed converts them. | Meta Business Suite / TikTok inbox | TO VERIFY — Shannon McNeil (BLOCKERS #1/#2) |
| 4 | New Google reviews and rating | 4.6★ is the pilot's top rating — the job is volume: more new reviews while holding the score. | GBP Insights + public profile | Rating observed 2026-08-12; count + insights TO VERIFY |
| 5 | Website clicks from Google | The consideration step — shoppers tapping through to research inventory before the lot. | GBP Insights | TO VERIFY — Shannon McNeil (GBP owner access) |

### 2.3 Store 03 — Greenway Kia Rivergate (GM James Galuszka, Madison, TN)

**Store context (observed 2026-08-12, workbook store-03/audit.csv):** GBP rating 4.4★. Listing posts current (Aug 8, 2026). Same GM also runs Store 04 — the two Nashville scorecards are read side by side. Review count and insights: TO VERIFY.

| # | Metric | Why it matters to this store (1 line) | Data source | Access status |
|---|---|---|---|---|
| 1 | Calls from Google | Nashville metro is the pilot's busiest market — call volume should run high here. | GBP Insights | TO VERIFY — Shannon McNeil (GBP owner access) |
| 2 | Directions from Google | Gallatin Pike depends on map discovery; directions measure the pull. | GBP Insights | TO VERIFY — Shannon McNeil |
| 3 | Social messages (DMs) | Reading message volume here vs Store 04 shows which storefront's content pulls inquiries. | Meta Business Suite / TikTok inbox | TO VERIFY — Shannon McNeil (BLOCKERS #1/#2) |
| 4 | New Google reviews and rating | 4.4★ at audit; competitive Kia market — review flow is the differentiator. | GBP Insights + public profile | Rating observed 2026-08-12; count + insights TO VERIFY |
| 5 | Reach across social | Biggest metro in the pilot — awareness is the first job; reach shows how many local accounts the store touches. | Meta Business Suite / TikTok Analytics / YouTube Studio | TO VERIFY — Shannon McNeil (BLOCKERS #2) |

### 2.4 Store 04 — Greenway Kia Hickory Hollow (GM James Galuszka, Antioch, TN)

**Store context (observed 2026-08-12, workbook store-04/audit.csv):** GBP rating 4.3★. Listing posts observed through Jul 14, 2026, then quiet at audit. Same GM as Store 03. Review count and insights: TO VERIFY.

| # | Metric | Why it matters to this store (1 line) | Data source | Access status |
|---|---|---|---|---|
| 1 | Calls from Google | Direct demand read for the Antioch storefront. | GBP Insights | TO VERIFY — Shannon McNeil (GBP owner access) |
| 2 | Directions from Google | Antioch shoppers navigate to Target Dr; taps = intent to visit. | GBP Insights | TO VERIFY — Shannon McNeil |
| 3 | Social messages (DMs) | Sister store to Store 03 — message trends here vs Rivergate tell which storefront needs attention. | Meta Business Suite / TikTok inbox | TO VERIFY — Shannon McNeil (BLOCKERS #1/#2) |
| 4 | New Google reviews and rating | 4.3★ sits at the lower end of the pilot's band — new reviews are the lever. | GBP Insights + public profile | Rating observed 2026-08-12; count + insights TO VERIFY |
| 5 | Google posts published vs plan | Listing posts went quiet after Jul 14, 2026 (observed) — freshness is this store's gap to close. | Content calendar + GBP | Calendar team-owned; GBP access TO VERIFY |

### 2.5 Store 05 — Greenway Ford Kansas City (GM Shane Silvey, Raytown, MO)

**Store context (observed 2026-08-12, workbook store-05/audit.csv):** GBP rating 4.3★. Listing posts current (Aug 10, 2026 — most recent of the five). Only Ford rooftop — different OEM, different buyer base. Review count and insights: TO VERIFY.

| # | Metric | Why it matters to this store (1 line) | Data source | Access status |
|---|---|---|---|---|
| 1 | Calls from Google | The only Ford rooftop in the pilot — calls are its direct demand read. | GBP Insights | TO VERIFY — Shannon McNeil (GBP owner access) |
| 2 | Directions from Google | Raytown shoppers use the listing to find 9505 E 350 Hwy; taps = intent to visit. | GBP Insights | TO VERIFY — Shannon McNeil |
| 3 | Social messages (DMs) | Ford buyers skew older — Facebook Messenger is likely the biggest message channel; reply speed matters. | Meta Business Suite inbox | TO VERIFY — Shannon McNeil (BLOCKERS #1/#2) |
| 4 | New Google reviews and rating | 4.3★ at audit; Ford shoppers read reviews heavily before choosing a dealer — flow and response both count. | GBP Insights + public profile | Rating observed 2026-08-12; count + insights TO VERIFY |
| 5 | Facebook + Google reach | Ford's buyer base skews older than Kia's — Facebook and Google are the primary surfaces; reach there counts more than TikTok. | Meta Business Suite + GBP Insights | TO VERIFY — Shannon McNeil (BLOCKERS #2) |

**Note on the freshness observations (Stores 01 and 04):** these are internal context for GM one-on-ones, framed as absence or freshness, never as a complaint list (`OPERATING_RULES.md` §9–10).

## 3. The COO view — group rollup

### 3.1 The monthly scorecard — one table, five named rows

Same five columns for every rooftop, five rows, one per rooftop. Every cell is that store's own monthly number from its GM report — never summed, never averaged. The store-specific fifth metric (posts published, website clicks, reach) stays in each store's GM report and is summarized qualitatively in the narrative.

| Rooftop | Calls (GBP) | Directions (GBP) | Messages (FB/IG/TikTok) | New reviews (GBP) | Rating (GBP) |
|---|---|---|---|---|---|
| Greenway Kia West Palm Beach | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | 4.5★ (observed 2026-08-12) |
| Greenway Kia at the Avenues | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | 4.6★ (observed 2026-08-12) |
| Greenway Kia Rivergate | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | 4.4★ (observed 2026-08-12) |
| Greenway Kia Hickory Hollow | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | 4.3★ (observed 2026-08-12) |
| Greenway Ford Kansas City | TO VERIFY | TO VERIFY | TO VERIFY | TO VERIFY | 4.3★ (observed 2026-08-12) |

Once access lands (BLOCKERS.md #1/#2 — owners Shannon McNeil, Shawn Vink), each TO VERIFY cell is replaced by the store's number with a capture date. A cell that cannot be filled stays TO VERIFY; it is never estimated.

### 3.2 What the COO needs to see each month (one page)

The readout is the table above plus the six numbered sections below, each 1–3 lines:

1. **The five-store scorecard.** Five named rows with month-over-month change in every cell. This is the visibility Casey Coffey asked for: one page, every dealership, the same five numbers.
2. **Where demand is moving.** One line per store on calls, directions, and messages, with direction of movement. Name the store with the biggest move and, when there is one, the action behind it (a content push, a review-response run, a posting-rhythm change). Falling directions while reach grows means content is reaching people outside the store's service area (`KPI_FRAMEWORK.md` §5).
3. **Where reputation is moving.** New reviews and rating per store, named. Flag any store below the 4.5★ bar many shoppers set (`BENCHMARKS.md` §4.1) and any store not responding to 100% of new reviews within 2 business days (house target — for Shannon to confirm; `KPI_FRAMEWORK.md` §4.6).
4. **What the team is doing about it.** Up to three numbered actions, each tied to a number in the table. Example shape: "1. Answer the 9 unanswered messages at Greenway Kia Hickory Hollow. 2. Restart weekly Google posts at West Palm Beach. 3. Keep the delivery-time review ask running at the Avenues." Owners are the store, Shannon McNeil, or the Bright Matter team — never an agent contacting the store.
5. **Data gaps.** Any cell still TO VERIFY, with the owner who can unblock it (Shannon McNeil; corporate/admin via Shawn Vink). Visibility is only as good as access — the readout names what is missing and who holds the key.
6. **Never an average.** The group view is five named rows. A "Greenway average" is not reported (`KPI_FRAMEWORK.md` §1.4) — it hides the store that is winning and the store that is slipping.

## 4. Cadence

Aligned to `KPI_FRAMEWORK.md` §6 and the phase timeline (Month 1 audit → Month 2 strategy & build → Months 3–6 execution & coaching → Month 6 transition). Pilot start date and the fixed monthly capture day: **TO VERIFY — request from client via Shannon McNeil** (`CLIENT.md` §8.3).

Weekly checks are internal only (team working notes, not client-facing): they feed the monthly report. Monthly is the report cycle. Quarterly (end of Months 3 and 6) is the trend view for both audiences.

| Metric | Weekly (internal ops) | Monthly — GM report | Monthly — COO readout | Quarterly — both |
|---|---|---|---|---|
| Calls from Google | — | ✔ | ✔ | ✔ |
| Directions from Google | — | ✔ | ✔ | ✔ |
| Social messages received | ✔ (unanswered count) | ✔ | ✔ | ✔ |
| Message response rate/time | ✔ | ✔ | ✔ (gap flag) | ✔ |
| New Google reviews | ✔ (new + responses due) | ✔ | ✔ | ✔ |
| Rating | — | ✔ | ✔ | ✔ |
| Review response | ✔ (response check) | ✔ | ✔ (gap flag) | ✔ |
| Website clicks (Store 02) | — | ✔ | narrative only | ✔ |
| Google posts published vs plan (Stores 01, 04) | ✔ (pace vs calendar) | ✔ | narrative only | ✔ |
| Reach (Stores 03, 05) | — | ✔ | narrative only | ✔ |

**The monthly reporting cycle (numbered):**

1. On the fixed capture day, pull every metric into the store's dashboard row (`reporting/dashboards/store-XX/DASHBOARD.csv`) and screenshot the insights pages as evidence (`KPI_FRAMEWORK.md` §7).
2. Fill the GM report from the dashboard row (`REPORTING_TEMPLATE.md` — one file per store at `reporting/reports/store-XX/MONTHLY_REPORT-<period>.md`). Cells that could not be captured stay TO VERIFY and go on the request list.
3. Team lead reviews all five GM reports.
4. Shannon McNeil approves before anything reaches a GM or the COO.
5. The GM report goes to the store's GM via Shannon — one-on-one when it carries sensitive findings.
6. The COO readout (§3.1 table + §3.2 page) is assembled from the five approved GM reports and goes to Casey Coffey via Shannon, named per rooftop.

**Quarterly** (end of Months 3 and 6): the shortened quarterly variant per store (`REPORTING_TEMPLATE.md` §6), plus a five-row quarterly trend table for the COO (Baseline → Months 1–3 → Months 4–6, change vs baseline). Benchmarks are re-verified before each quarterly report (`KPI_FRAMEWORK.md` §6, §8).

## 5. Guardrails

1. **Real numbers only.** A number in either view comes from native insights pulled with confirmed access, a public page captured with a date, or the store via Shannon McNeil (`KPI_FRAMEWORK.md` §1.1). Nothing else.
2. **Where access is missing, the cell stays TO VERIFY** — request from client via Shannon McNeil; corporate/admin access via Shawn Vink where applicable (BLOCKERS.md #1/#2/#6). An estimate is never substituted, not even a labeled one (`KPI_FRAMEWORK.md` §1.2).
3. **Never guess, never invent.** Every metric above maps to a K-number in `KPI_FRAMEWORK.md`. If the team cannot measure it, it is flagged, not reported.
4. **The two views never mix.** The GM report is one store. The COO readout is five named rows. No group averages, no summed follower counts, no blended ratings (`KPI_FRAMEWORK.md` §1.4).
5. **Every number carries a capture date and source** (`KPI_FRAMEWORK.md` §1.3). Observed public data (e.g., the GBP ratings above) is labeled observed with its date.
6. **Benchmarks are directional context, never pass/fail** (`KPI_FRAMEWORK.md` §1.5). House targets are labeled for Shannon to confirm (§1.6, §8).
7. **No sales claims.** The pilot measures social and profile activity, not closed sales. Whether stores track call/DM-to-sale conversion is TO VERIFY (`KPI_FRAMEWORK.md` §5). Until then, reports say what the numbers are.
8. **Sensitive findings stay one-on-one.** Negative review patterns, Reddit complaints, and fee issues go to GM one-on-ones, never group settings or the COO readout (`OPERATING_RULES.md` §9). Reputation is framed as absence, not complaint lists (§10).
9. **A number that looks wrong gets investigated, not published** (`OPERATING_RULES.md` §14). A trend that contradicts the store's own experience is a question to resolve before it enters a report.

## 6. Data sources & access (named)

Every metric is measured from platform-native insights (`KPI_FRAMEWORK.md` §7). Access to all of the following is **TO VERIFY — request from client via Shannon McNeil** (per-account permissions; corporate/admin via Shawn Vink where applicable — BLOCKERS.md #1/#2):

| Metric | Tool | Access needed |
|---|---|---|
| Calls, directions, website clicks, review count, rating, review response | GBP Insights | GBP owner access |
| Messages and response rate/time (FB, IG) | Meta Business Suite inbox | Page access |
| Messages (TikTok) | TikTok inbox | Account access |
| Messages (Reddit) | Reddit messages | Account access |
| Reach (FB, IG, TikTok, YouTube) | Meta Business Suite / TikTok Analytics / YouTube Studio | Per-channel access |
| Posts published | Content calendar (team) + native insights | Calendar team-owned; reconciliation needs access |

**TO VERIFY items that block real numbers, with owners named:**

- Native-insights access per store × channel — Shannon McNeil (BLOCKERS.md #2)
- Accounts & access inventory, admin roles, vendor split — Shannon McNeil; corporate admin via Shawn Vink (BLOCKERS.md #1)
- Who posts today, with what tool, on what cadence — Shannon McNeil (BLOCKERS.md #6)
- Store goals and KPIs the store already tracks — Shannon McNeil (`CLIENT.md` §8.2)
- Whether the store tracks call/DM-to-sale conversion — Shannon McNeil (`CLIENT.md` §8.2)
- Pilot start/end dates and fixed monthly capture day — Shannon McNeil (`CLIENT.md` §8.3)
- GBP review counts and full insights — GBP owner access via Shannon McNeil
- Follower/subscriber baselines — native-insights access per channel

## 7. Relationship to the full framework

This file distills `KPI_FRAMEWORK.md`; it does not replace it. The full framework defines every K-number, the dashboard columns, and the report rows; this file picks the handful that land on a GM's phone and on the COO's one-pager. If a metric changes here, the change flows back to `KPI_FRAMEWORK.md`, `DASHBOARD_TEMPLATE.md`, and `REPORTING_TEMPLATE.md` together (`KPI_FRAMEWORK.md` §10).

---

*End of framework. Internal draft until Shannon McNeil approves it for client delivery. No one on the Bright Matter team contacts the store directly.*
