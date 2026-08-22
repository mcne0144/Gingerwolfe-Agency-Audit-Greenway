# audit/ — Per-Store, Per-Channel Audit Framework & Report Template

**Status:** INTERNAL DRAFT — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-12
**Owner:** Bright Matter LLC agency operations team (Audit & Research Analyst)

---

## What this folder is

The audit foundation for **Greenway Auto Group's six-month organic social pilot** (5 dealership rooftops × 6 channels each: Facebook, Instagram, TikTok, YouTube, Reddit, Google Business Profile). It defines **how** the team audits one store's presence on one channel — with the same 1–5 scoring everywhere — and **what** a completed audit looks like when it goes to a dealership General Manager.

**No store facts are assumed.** Every deliverable here is a framework/template ready to be filled store-by-store. Unknowns are marked "TO VERIFY — request from client via Shannon McNeil."

## Files in this folder

| File | What it is | Use it when |
|---|---|---|
| `AUDIT_FRAMEWORK.md` | The methodology: the operator's six-bucket Month 1 audit structure (accounts & access, performance baselines, reputation, search presence, competitive benchmarking, operations workflow), what gets checked per bucket and per channel, what data to collect, the 1–5 scoring rubric, the four-step process (gather → verify → score → report), and how to use benchmarks. Working implementation: `workbook/WORKBOOK.md`; data-collection instrument: `gm-interviews/BASELINE_QUESTIONNAIRE.md` | Running any audit; scoring any channel |
| `BENCHMARKS.md` | Source-verified reference numbers per channel: engagement trends, posting-cadence guidance, response-time expectations, Google review benchmarks, Reddit norms, YouTube format guidance — every entry cited | Scoring "performance vs. benchmark" and writing findings |
| `AUDIT_REPORT_TEMPLATE.md` | The GM-ready report form: executive summary, scorecard, per-channel findings, ranked opportunities, next steps with owner and timing, data-sources appendix | Producing a completed audit for one store |
| `gm-interviews/GM_INTERVIEW_GUIDE.md` | How the operator runs each GM one-on-one: pre-interview checklist, flow, timing, sensitive-findings handling, note template, post-interview steps | Running the Month 1 GM interviews (operator only) |
| `gm-interviews/BASELINE_QUESTIONNAIRE.md` | The 38-question baseline set, mapped to the six audit buckets and `CLIENT.md` §8 | The question set the operator reads in each interview |
| `README.md` (this file) | How the audit folder fits the rest of the workspace | Orientation |

## How the audit files relate to the rest of the workspace

```
greenway/
├── CLIENT.md              <- master record; §5 = the exact data to request from
│                             Shannon McNeil before audits can start
├── WORKFLOW.md            <- approval pipeline: draft → team lead → Shannon → client
├── channel-matrix.csv     <- 5×6 status matrix; feeds the audit's account-status gate
├── stores/store-01..05/STORE.md
│                          <- per-store profile + channel inventory; the audit's
│                             starting point for handles, status, and gaps
└── audit/
    ├── AUDIT_FRAMEWORK.md       <- how to run the audit (this folder)
    ├── BENCHMARKS.md            <- what "typical/good" looks like (cited)
    ├── AUDIT_REPORT_TEMPLATE.md <- what a completed audit looks like
    └── reports/store-XX/AUDIT_REPORT.md  <- completed per-store reports (created
        (future)                          when real data arrives)
```

- **`stores/store-XX/STORE.md` feeds the audit.** The store profile (identity, 6-channel inventory, known gaps) is the audit's starting data. If a handle is TO VERIFY there, the audit's account-status dimension is TO VERIFY too.
- **`channel-matrix.csv` feeds the audit.** Its per-channel status (Active/Inactive/Unknown) is the account-status gate in the framework. After an audit confirms statuses, the matrix and the store's `STORE.md` are updated to match.
- **A completed audit fills `AUDIT_REPORT_TEMPLATE.md` per store.** One report per rooftop (`audit/reports/store-XX/AUDIT_REPORT.md`), covering all 6 channels of that store. Reports stay internal drafts until Shannon McNeil approves them (per `WORKFLOW.md`).
- **`BENCHMARKS.md` is the scoring context.** Findings like "engagement is below typical" must cite a benchmark from this file or say no published benchmark exists — nothing is invented.

## When real data arrives from Shannon McNeil

1. Confirm handles/statuses in `channel-matrix.csv` and `stores/store-XX/STORE.md` (this is the audit's gate).
2. Run the audit per `AUDIT_FRAMEWORK.md` (gather → verify → score → report), re-checking `BENCHMARKS.md` against its sources first.
3. Fill `AUDIT_REPORT_TEMPLATE.md` for the store → `audit/reports/store-XX/AUDIT_REPORT.md`, with screenshots in `audit/reports/store-XX/evidence/`.
4. Route the draft: team lead review → Shannon McNeil approval → client. No agent contacts the client.

## Current state

- Framework, benchmarks, and report template are drafted and internally consistent with the workspace.
- All five stores remain unfilled templates (everything TO VERIFY); no completed audits exist yet; nothing is client-facing.
