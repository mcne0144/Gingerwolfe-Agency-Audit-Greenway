# reporting/ — KPI Framework, GM-Ready Reports & Per-Store Tracking Dashboards

**Status:** INTERNAL DRAFT — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Reporting Analyst)

---

## What this folder is

The measurement and reporting foundation for **Greenway Auto Group's six-month organic social pilot** (5 dealership rooftops × 6 channels each: Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile). It defines **what** we measure for one store on one channel, **how** those numbers get tracked month over month, and **what** a completed monthly (or quarterly) report looks like when it goes to a dealership General Manager.

**No store facts are assumed.** No real performance data exists yet. Every KPI is defined and tracked per store × channel; every unknown is marked "TO VERIFY — request from client via Shannon McNeil." Nothing is invented, and data gaps are flagged, never guessed.

## Files in this folder

| File | What it is | Use it when |
|---|---|---|
| `KPI_FRAMEWORK.md` | The measurement framework: the full KPI set (reach/impressions, engagement rate, follower growth, saves/shares, DMs/comments-leads, plus channel-specific KPIs for GBP, Reddit, and YouTube), how each KPI is measured and where its data comes from, what matters most to a dealership GM, weekly/monthly/quarterly cadence, and the no-fabrication guardrails | Defining any number, before a report or dashboard is touched |
| `REPORTING_TEMPLATE.md` | The GM-ready monthly report template: store header, plain-language executive summary, headline scorecard with trend vs previous month, per-channel tables, what's working / what's not (evidence-based), recommendations with owner + timing, data-sources & gaps appendix, plain-language glossary — plus a shorter quarterly variant | Producing `reports/store-XX/MONTHLY_REPORT-<period>.md` (and quarterly) |
| `DASHBOARD_TEMPLATE.md` | The per-store, per-channel tracking sheet design: KPI columns × month rows across the full 6-month pilot, with the column dictionary and the monthly fill routine | Building/maintaining the tracking sheets |
| `README.md` (this file) | How the reporting files fit the rest of the workspace | Orientation |
| `dashboards/store-01…05/DASHBOARD.csv` | One blank tracking sheet per store (all cells TO VERIFY), ready to accumulate real data month over month | Filling at each month end |

## How the reporting files relate to the rest of the workspace

```
greenway/
├── CLIENT.md              <- master record; §5 = the exact data to request from
│                             Shannon McNeil before any real number can be captured
├── WORKFLOW.md            <- approval pipeline: draft → team lead → Shannon → client
├── channel-matrix.csv     <- 5×6 status matrix; which channels exist per store
├── stores/store-01..05/STORE.md
│                          <- per-store profile + channel inventory (identity layer)
├── audit/
│   ├── AUDIT_FRAMEWORK.md       <- how to audit a store's channels (gather →
│   │                              verify → score → report)
│   ├── BENCHMARKS.md            <- source-verified per-channel benchmarks (cited)
│   ├── AUDIT_REPORT_TEMPLATE.md <- GM-ready audit report form
│   └── reports/store-XX/…       <- completed audits (future)
├── content/
│   ├── CONTENT_STRATEGY_FRAMEWORK.md  <- pillars, voice, channel plans, cadence
│   ├── CONTENT_CALENDAR_TEMPLATE.md   <- 6-month calendar + monthly content-mix check
│   └── calendars/store-XX/…           <- per-store calendars (future)
└── reporting/                    <- this folder
    ├── KPI_FRAMEWORK.md          <- what we measure, and why
    ├── DASHBOARD_TEMPLATE.md     <- how the numbers accumulate
    ├── REPORTING_TEMPLATE.md     <- how the numbers become a GM report
    ├── dashboards/store-XX/DASHBOARD.csv  <- one tracking sheet per store (blank)
    └── reports/store-XX/…        <- completed monthly/quarterly reports (future)
```

- **`audit/BENCHMARKS.md` anchors the targets.** Every benchmark claim in the reporting files cites that file (e.g., engagement-trend context §1.1, response expectations §3.1–3.2, review volume/rating §4.1, Reddit norms §5, YouTube format rules §6). Benchmarks are directional context, never pass/fail; where no benchmark exists, the reporting files set a labeled **house target for Shannon to confirm** — never an invented number.
- **`stores/store-XX/STORE.md` and `channel-matrix.csv` are the identity layer.** If a handle or status is TO VERIFY there, the corresponding channel's KPI row is TO VERIFY here too. When data arrives, those files update first, then dashboards and reports.
- **The audit feeds the baseline.** The store's first audit (`audit/reports/store-XX/AUDIT_REPORT.md`) supplies the dashboard's `Baseline` row (followers, rating, review count, cadence) — the point every month is compared to.
- **The content calendar sets the plan.** `content/CONTENT_CALENDAR_TEMPLATE.md` defines the posting cadence and the monthly content-mix check; the dashboard's `posts published` columns and the report's cadence notes are measured against that plan (`content/CONTENT_STRATEGY_FRAMEWORK.md` §8).
- **Native platform insights feed the KPIs.** Every KPI is read from platform-native insights (Meta Business Suite, TikTok Analytics, YouTube Studio, GBP Insights) or captured publicly with a date — **access to all of them is TO VERIFY via Shannon** (`CLIENT.md` §8.1). No access, no number: the cell stays marked TO VERIFY and lands on the report's request list.
- **The dashboard accumulates; the report communicates.** Each month the store's `DASHBOARD.csv` row is filled, then `REPORTING_TEMPLATE.md` is filled from it → `reports/store-XX/MONTHLY_REPORT-<period>.md`. The report is **one store only** — never aggregated across stores — and stays an internal draft through the pipeline: team lead review → **Shannon McNeil approval** → client (`WORKFLOW.md`).

## When real data arrives from Shannon McNeil

1. Update `CLIENT.md` §8 checklist items and the matching fields in `stores/store-XX/STORE.md` and `channel-matrix.csv`.
2. Run the store audit per `audit/AUDIT_FRAMEWORK.md` → `audit/reports/store-XX/AUDIT_REPORT.md`. The audit supplies the dashboard's **Baseline** row.
3. Confirm access to native insights per channel (via Shannon, per account permissions) — the prerequisite for every real number.
4. At each month end, fill the store's dashboard row (`dashboards/store-XX/DASHBOARD.csv`) per `DASHBOARD_TEMPLATE.md` §5 — capture on a fixed day, screenshot as evidence, mark gaps TO VERIFY.
5. Fill `REPORTING_TEMPLATE.md` from the dashboard → `reports/store-XX/MONTHLY_REPORT-<period>.md` (internal draft → team lead → Shannon → client).
6. At the ends of Months 3 and 6, produce the quarterly variant (`REPORTING_TEMPLATE.md` §6), re-verifying `BENCHMARKS.md` sources first and confirming whether a re-audit is due.

## Current state

- KPI framework, report template (with quarterly variant), dashboard template, and the five blank per-store tracking sheets are drafted and internally consistent with the workspace.
- All five dashboards are fully marked TO VERIFY; no real data, no completed reports, and nothing client-facing exists yet.
- The report pipeline cannot produce a real number until Shannon McNeil provides the access and data listed in `CLIENT.md` §8.
