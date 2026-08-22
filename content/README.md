# content/ — Per-Store Content Strategy, Calendar & Creative Briefs

**Status:** INTERNAL DRAFT — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Content Strategist)

---

## What this folder is

The content foundation for **Greenway Auto Group's six-month organic social pilot** (5 dealership rooftops × 6 channels each: Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile). It defines **how** the team builds one store's content strategy, lays out its six-month posting calendar, and specifies each piece of content before any copy is written.

**No store facts are assumed.** Everything here is a framework or template ready to be filled store-by-store. Unknowns are marked "TO VERIFY — request from client via Shannon McNeil."

## Files in this folder

| File | What it is | Use it when |
|---|---|---|
| `CONTENT_STRATEGY_FRAMEWORK.md` | The methodology: how to turn a store's audit into content pillars, voice & tone, a channel-by-channel plan for all 6 channels (with benchmark citations), content-mix ratios, posting cadence, and the per-store process end to end | Building any store's strategy (`strategies/store-XX/STRATEGY.md`) |
| `CONTENT_CALENDAR_TEMPLATE.md` | The fill-in six-month calendar: per-store, per-month, week-by-week grids (date, channel, content type, pillar, topic/slot, asset, copy status, approval status, posted?), plus the monthly content-mix check and the approval tracker | Producing `calendars/store-XX/MONTH-01.md` … `MONTH-06.md` |
| `CREATIVE_BRIEF.md` | The one-page brief for a single piece of content: goal, audience, message, hook, copy sketch, CTA, asset specs, brand guardrails, review/approval box | Producing `briefs/store-XX/<content-id>.md` for every calendar slot |
| `README.md` (this file) | How the content files fit the rest of the workspace | Orientation |

## How the content files relate to the rest of the workspace

```
greenway/
├── CLIENT.md              <- master record; §5 = the exact data to request from
│                             Shannon McNeil before content planning can start
├── WORKFLOW.md            <- approval pipeline: draft → team lead → Shannon → client
├── channel-matrix.csv     <- 5×6 status matrix; which channels exist per store
├── stores/store-01..05/STORE.md
│                          <- per-store profile + channel inventory; the content
│                             plan's starting point for identity and gaps
├── audit/
│   ├── AUDIT_FRAMEWORK.md       <- how to audit a store's channels (gather →
│   │                              verify → score → report)
│   ├── BENCHMARKS.md            <- source-verified per-channel benchmarks (cited)
│   ├── AUDIT_REPORT_TEMPLATE.md <- GM-ready audit report form
│   └── reports/store-XX/AUDIT_REPORT.md  <- completed audits (future)
└── content/
    ├── CONTENT_STRATEGY_FRAMEWORK.md  <- how to build one store's strategy
    ├── CONTENT_CALENDAR_TEMPLATE.md   <- how to build one store's 6-month calendar
    ├── CREATIVE_BRIEF.md              <- how to specify one piece of content
    ├── strategies/store-XX/STRATEGY.md  <- per-store strategy (future)
    ├── calendars/store-XX/MONTH-01..06.md  <- per-store, per-month calendars (future)
    └── briefs/store-XX/<content-id>.md  <- one brief per piece of content (future)
```

- **Audit findings feed pillars.** `audit/reports/store-XX/AUDIT_REPORT.md` tells the strategy which channels are active, what content already gets engagement, and what is broken. The strategy's pillar choices, mix, and cadence must respond to that evidence (`CONTENT_STRATEGY_FRAMEWORK.md` §1–2).
- **`audit/BENCHMARKS.md` sets the boundaries.** Every cadence, format, and response claim in the content files cites a benchmark from that file or is labeled a team house default — never an invented number (`BENCHMARKS.md` §7 lists what was deliberately not included).
- **`stores/store-XX/STORE.md` and `channel-matrix.csv` are the identity layer.** If a handle is TO VERIFY there, the corresponding channel's plan is TO VERIFY too. When data arrives, `STORE.md` and the matrix are updated first, then strategies and calendars.
- **The calendar drives execution.** Each month's calendar (`calendars/store-XX/MONTH-0X.md`) lists every scheduled item with copy/approval/posted status and an approval tracker matching `WORKFLOW.md` exactly: specialist drafts → team lead reviews → **Shannon McNeil approves** → posted.
- **Briefs precede copy.** Every calendar slot gets a brief (`briefs/store-XX/<content-id>.md`) before copy is written — the brief is the contract between the plan and the post.

## When real data arrives from Shannon McNeil

1. Update `CLIENT.md` §8 checklist items and the matching fields in `stores/store-XX/STORE.md` and `channel-matrix.csv`.
2. Run the store audit per `audit/AUDIT_FRAMEWORK.md` → `audit/reports/store-XX/AUDIT_REPORT.md` (internal draft → team lead → Shannon → client).
3. Build the store's strategy per `CONTENT_STRATEGY_FRAMEWORK.md` → `content/strategies/store-XX/STRATEGY.md` (same approval route).
4. Build Month 01 of the calendar per `CONTENT_CALENDAR_TEMPLATE.md` → `content/calendars/store-XX/MONTH-01.md`; write a brief per slot per `CREATIVE_BRIEF.md`; draft copy; move items through the approval tracker.
5. Repeat month by month. At month end, run the monthly content-mix check and feed results into the next month and the next audit round.
6. Shannon McNeil approves every client-facing artifact. No agent contacts the client.

## Current state

- Strategy framework, calendar template, and creative brief template are drafted and internally consistent with the workspace.
- All five stores remain unfilled templates (everything TO VERIFY); no strategies, calendars, or briefs exist yet; nothing is client-facing.
