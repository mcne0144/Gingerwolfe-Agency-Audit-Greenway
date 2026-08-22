# Greenway Auto Group — Pilot Workspace

**Status:** INTERNAL WORKING DOCUMENT — draft, not client-facing
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team

---

## What this workspace is

The shared operating foundation for **Greenway Auto Group's six-month organic social pilot**: 5 dealership rooftops × 6 channels each (Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile).

Shannon McNeil is the only client-facing voice. Everything in this workspace is an internal draft; nothing goes to the client without her sign-off (see `WORKFLOW.md`).

**Nothing about the stores is known yet.** No facts about Greenway's dealerships have been invented. Every unknown is marked "TO VERIFY — request from client via Shannon McNeil".

## Structure

```
greenway/
├── README.md           <- this file: how the workspace fits together
├── CLIENT.md           <- client master record: who we are, the client, the
│                          engagement, the approval gate, and the data checklist
│                          to request from Shannon McNeil
├── WORKFLOW.md         <- operating workflow: drafts → team lead review →
│                          Shannon McNeil approval → client
├── channel-matrix.csv  <- 5×6 channel matrix: status of every store × channel
│                          pair (default: Unknown) + handle/URL columns
├── stores/
│   ├── store-01/STORE.md   <- Store 01 profile & channel inventory (template)
│   ├── store-02/STORE.md   <- Store 02 profile & channel inventory (template)
│   ├── store-03/STORE.md   <- Store 03 profile & channel inventory (template)
│   ├── store-04/STORE.md   <- Store 04 profile & channel inventory (template)
│   └── store-05/STORE.md   <- Store 05 profile & channel inventory (template)
├── audit/
    ├── README.md               <- how the audit files fit the workspace
    ├── AUDIT_FRAMEWORK.md      <- per-store, per-channel audit methodology + 1–5
    │                              scoring rubric (gather → verify → score → report)
    ├── BENCHMARKS.md           <- source-verified per-channel benchmarks (all cited)
    ├── AUDIT_REPORT_TEMPLATE.md<- GM-ready per-store audit report template
    └── reports/                <- completed per-store reports (created when data
        (future)                   arrives: reports/store-XX/AUDIT_REPORT.md)
├── content/
    ├── README.md                       <- how the content files fit the workspace
    ├── CONTENT_STRATEGY_FRAMEWORK.md   <- per-store strategy methodology: pillars,
    │                                      voice, channel plans, mix, cadence
    ├── CONTENT_CALENDAR_TEMPLATE.md    <- per-store, per-month 6-month calendar
    │                                      template + mix check + approval tracker
    ├── CREATIVE_BRIEF.md               <- one-page brief template per piece of content
    └── strategies/, calendars/, briefs/ <- per-store outputs (created when data
        (future)                           arrives: content/strategies/store-XX/…,
                                           content/calendars/store-XX/…,
                                           content/briefs/store-XX/…)
└── reporting/
    ├── README.md                       <- how the reporting files fit the workspace
    ├── KPI_FRAMEWORK.md                <- KPI set, data sources, GM priorities,
    │                                      cadence, guardrails (per store × channel)
    ├── REPORTING_TEMPLATE.md           <- GM-ready monthly report template +
    │                                      quarterly variant
    ├── DASHBOARD_TEMPLATE.md           <- per-store, per-channel 6-month tracking
    │                                      sheet (KPI columns × month rows)
    ├── dashboards/
    │   └── store-XX/DASHBOARD.csv      <- one blank tracking sheet per store
    └── reports/                        <- completed monthly/quarterly reports
        (future)                           (created when data arrives:
                                           reporting/reports/store-XX/…)
```

## How the files relate

- **`CLIENT.md`** is the master record. It defines the engagement, the approval gate, and — in §5 — the complete checklist of data Shannon McNeil must provide.
- **`stores/store-01` … `store-05`** hold one profile per rooftop. Each `STORE.md` is a consistent template: store identity, a 6-channel inventory table, and known gaps. Until data arrives, every field is TO VERIFY.
- **`channel-matrix.csv`** is the one-glance 5×6 matrix. Rows are the 5 stores; each channel has a status column (Active / Inactive / Unknown — default Unknown) plus a handle/URL column (TO VERIFY). It mirrors the per-store channel tables so statuses stay consistent between files.
- **`WORKFLOW.md`** governs how all of the above move: drafts are produced in this workspace, reviewed by the team lead, approved by Shannon McNeil, and only then sent to the client.
- **`audit/`** is the audit foundation. `AUDIT_FRAMEWORK.md` defines how to audit one store on one channel (what to check, what data to collect, the 1–5 scoring rubric); `BENCHMARKS.md` holds the source-verified reference numbers used when scoring; `AUDIT_REPORT_TEMPLATE.md` is the GM-ready report form a completed audit fills per store. The store profiles (`stores/`) and the channel matrix (`channel-matrix.csv`) feed the audit — a completed audit updates them in return. See `audit/README.md`.
- **`content/`** is the content foundation. `CONTENT_STRATEGY_FRAMEWORK.md` turns a store's audit findings into content pillars, voice, channel-by-channel plans, mix, and cadence; `CONTENT_CALENDAR_TEMPLATE.md` is the per-store, per-month 6-month calendar (week-by-week grids + monthly mix check + approval tracker); `CREATIVE_BRIEF.md` specifies each piece of content before copy is written. Audit findings feed the strategy; the calendar feeds execution; every artifact clears the same approval pipeline. See `content/README.md`.
- **`reporting/`** is the measurement foundation. `KPI_FRAMEWORK.md` defines what the pilot measures per store × channel and where each number comes from (platform-native insights — access TO VERIFY); `DASHBOARD_TEMPLATE.md` plus the per-store `dashboards/store-XX/DASHBOARD.csv` files accumulate real data month over month across the 6-month pilot; `REPORTING_TEMPLATE.md` turns a month's dashboard row into a GM-ready monthly report (with a quarterly variant). `audit/BENCHMARKS.md` anchors the targets the reports compare against; the content calendar sets the plan the reports measure; every report clears the same approval pipeline. See `reporting/README.md`.

## When data arrives from Shannon McNeil

1. Update `CLIENT.md` §8 checklist items (mark them confirmed).
2. Update the matching fields in the affected `stores/store-XX/STORE.md` file(s).
3. Update `channel-matrix.csv` statuses and handles for the affected store(s).
4. Run the audit for that store per `audit/AUDIT_FRAMEWORK.md` and fill `audit/AUDIT_REPORT_TEMPLATE.md` → `audit/reports/store-XX/AUDIT_REPORT.md` (internal draft → team lead review → Shannon McNeil approval → client).
5. Build the store's content strategy per `content/CONTENT_STRATEGY_FRAMEWORK.md` → `content/strategies/store-XX/STRATEGY.md`, then its 6-month calendar per `content/CONTENT_CALENDAR_TEMPLATE.md` → `content/calendars/store-XX/MONTH-01.md` … `MONTH-06.md`, with one brief per slot per `content/CREATIVE_BRIEF.md` (same approval pipeline).
6. Reporting follows once content is live: fill the store's dashboard row per `reporting/DASHBOARD_TEMPLATE.md` → `reporting/dashboards/store-XX/DASHBOARD.csv`, then produce monthly (and quarterly) reports per `reporting/REPORTING_TEMPLATE.md` → `reporting/reports/store-XX/` (same approval pipeline). Monthly content-mix checks feed the next month's calendar and the reports.

## Current state

- All five store profiles are unfilled templates (everything TO VERIFY).
- All 30 store × channel pairs in the matrix are status `Unknown` with handles TO VERIFY.
- The audit foundation (`audit/` — framework, source-verified benchmarks, GM-ready report template) is drafted as an internal working document.
- The content foundation (`content/` — strategy framework, 6-month calendar template, creative brief template) is drafted as an internal working document.
- The reporting foundation (`reporting/` — KPI framework, GM-ready monthly report template with quarterly variant, per-store 6-month tracking sheets) is drafted as an internal working document.
- No client-facing artifact has been produced or approved yet.
