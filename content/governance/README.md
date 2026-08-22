# governance/ — Content Governance, Salesperson Content Framework & Train-the-Trainer Playbook

**Status:** INTERNAL DRAFT — not client-facing until Shannon McNeil approves
**Last updated:** 2026-08-13
**Owner:** Bright Matter LLC agency operations team (Content Strategist)

---

## What this folder is

The governance layer for **Greenway Auto Group's six-month organic social pilot** (5 rooftops × 6 channels). It answers three questions the content foundation does not:

1. **Who decides what gets posted, and how?** — `GOVERNANCE_MODEL.md`
2. **What about salespeople posting from personal accounts?** — `SALESPERSON_CONTENT_FRAMEWORK.md`
3. **How does a store eventually run social without Bright Matter?** — `TRAIN_THE_TRAINER_PLAYBOOK.md`

All three are frameworks with per-store application. Every store-specific field is **TO VERIFY — request from client via Shannon McNeil**. Nothing about the stores is assumed or invented.

## Files in this folder

| File | What it is | Use it when |
|---|---|---|
| `GOVERNANCE_MODEL.md` | The content governance model for the pilot: who drafts, the approval chain (specialist → team lead → Shannon → published by Shannon via Sprout), rejected-draft feedback loop, brand guardrails and OEM compliance (TO VERIFY per brand), content-sourcing rules, per-store posting roles, escalation path for sensitive findings (one-on-one only), and how the model trains in-house staff over Months 3–6 | Any question about who may create, approve, or publish content; what binds a post; how sensitive findings get raised |
| `SALESPERSON_CONTENT_FRAMEWORK.md` | Month 2 draft policy skeleton for salesperson-generated content on personal accounts: encouraged, prohibited, required disclosures (TO VERIFY per platform), personal-brand vs dealership-brand boundaries, monitoring without surveillance, store-team training checklist. Introduced one-on-one with each GM, never as a group rollout; opportunity + risk-management framing | When Shannon prepares the Month 2 one-on-one with any GM |
| `TRAIN_THE_TRAINER_PLAYBOOK.md` | The handoff playbook: curriculum (draft, schedule via Sprout, respond, report), weekly operating rhythm, checklists per role, what stays with the agency vs what transfers, the 6-month progression (Month 3 observe → Month 4 co-create → Month 5 own drafts under review → Month 6 run with agency support), and the Month 6 readiness check | When a store names a trainee; when the team plans Months 3–6 training |
| `README.md` (this file) | How the governance files fit the rest of the workspace | Orientation |

## How the governance files relate to the rest of the workspace

```
greenway/
├── OPERATING_RULES.md         <- canonical: approval gates, Sprout human-operated,
│                                 sensitive findings one-on-one, absence framing,
│                                 writing style. Wins over every file here.
├── CLIENT.md                  <- master record; §6 long-term objective (train-the-
│                                 trainer); §8.2 the compliance/data checklist
├── WORKFLOW.md                <- approval pipeline: draft → team lead → Shannon → client
├── content/
│   ├── CONTENT_STRATEGY_FRAMEWORK.md  <- pillars, voice, cadence (the "what")
│   ├── CONTENT_CALENDAR_TEMPLATE.md   <- calendar + approval tracker (the "when")
│   ├── CREATIVE_BRIEF.md              <- brief + brand guardrails (the "spec")
│   ├── governance/                    <- THIS FOLDER: the "who and under what rules"
│   │   ├── GOVERNANCE_MODEL.md
│   │   ├── SALESPERSON_CONTENT_FRAMEWORK.md
│   │   ├── TRAIN_THE_TRAINER_PLAYBOOK.md
│   │   └── README.md
│   └── strategies/, calendars/, briefs/  <- per-store outputs (future)
└── reporting/
    ├── GM_KPI_FRAMEWORK.md     <- what gets measured; the monthly cycle governance
    │                             works alongside
    └── dashboards/, reports/   <- per-store tracking (future)
```

1. **Governance gates the calendar pipeline.** Every calendar item (`CONTENT_CALENDAR_TEMPLATE.md`) moves through the approval chain defined in `GOVERNANCE_MODEL.md` §3: specialist drafts → team lead reviews → Shannon McNeil approves → published by Shannon via Sprout. The calendar's approval tracker (§5) is the working record; the governance model is the rulebook. No item posts before `Approved`, and an item that comes back for edits re-enters the pipeline — never posted in a rejected state.
2. **Governance does not set strategy.** Pillars, voice, mix, and cadence come from `CONTENT_STRATEGY_FRAMEWORK.md` and the store's `STRATEGY.md`. Governance says who handles each piece and what rules bind it. The two meet in the creative brief: `CREATIVE_BRIEF.md` §8 (brand guardrails) is the per-piece application of the governance guardrails.
3. **The salesperson framework is a Month 2 one-on-one deliverable.** It is the one piece of this folder written for Shannon to introduce per GM, never in a group. It sits alongside the governance model: official pages follow `GOVERNANCE_MODEL.md`; personal accounts follow `SALESPERSON_CONTENT_FRAMEWORK.md`. A salesperson post that crosses into acting as the store escalates through `GOVERNANCE_MODEL.md` §8.
4. **The playbook is the train-the-trainer endgame.** `CLIENT.md` §6 says every deliverable should be written so a store employee could eventually run it without Bright Matter. The playbook is the mechanism; `GOVERNANCE_MODEL.md` §9 is the approval-side rule that governs it (approval never transfers during the pilot). The reporting layer (`reporting/GM_KPI_FRAMEWORK.md`) is the trainee's textbook — they learn to read the dashboard and the monthly report, never to invent numbers.
5. **Approval flows through Shannon per `WORKFLOW.md`.** Nothing in this folder changes the pipeline: no agent contacts the client, no agent publishes from Sprout, and every file here is an internal draft until Shannon approves its client-facing use.
6. **Sensitive handling is inherited from `OPERATING_RULES.md` §4.** Reputation findings, staff dependency, and salesperson-content issues go one-on-one to the relevant GM, framed as absence and opportunity — never a group setting, never a complaint list.

## When real data arrives from Shannon McNeil

1. Fill the TO VERIFY fields in the relevant file: per-store contacts and trainees (all three files), OEM rules per brand (governance §5.1, salesperson §10), platform disclosure requirements (salesperson §5), store capacity (playbook §9).
2. Shannon adapts `SALESPERSON_CONTENT_FRAMEWORK.md` per store and introduces it one-on-one with each GM; adopted versions are recorded per store.
3. When a store names a trainee, create `training/store-XX/TRAINING_LOG.md` (per `TRAIN_THE_TRAINER_PLAYBOOK.md` §6) and start the Month 3 observe stage.
4. Route any client-facing use of these files: team lead review → Shannon McNeil approval → client. No agent contacts the client.

## Current state

- All three governance files are drafted and internally consistent with the workspace.
- All store-specific fields are TO VERIFY; no store has adopted anything yet; no trainee is named; nothing is client-facing.
