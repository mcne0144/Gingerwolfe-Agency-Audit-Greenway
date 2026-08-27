# LISTENING_TOPIC_PLAN.md — Sprout Social Listening Topic Setup (Greenway Auto Group Pilot)

**Status:** INTERNAL DRAFT — planning work only. NOT client-facing. Nothing is configured in the live Sprout account by an agent. Shannon McNeil operates Sprout and builds every Topic herself (or grants a limited role at her discretion).
**Owner:** Bright Matter LLC agency operations team (Reporting Analyst drafts; Audit & Research Analyst supplies competitor sets)
**Date:** 2026-08-27
**Companion to:** `reporting/SPROUT_CONFIG_PLAN.md` (Month 2 configuration plan). This file covers the **Listening** module only.

> **Read this first (operating boundary):** Sprout Listening is a **paid add-on** on top of the pilot's Sprout plan. Per `CLIENT.md` §4, Sprout licensing is billed separately at cost — **whether the Listening add-on is licensed at all is a Shannon McNeil / Shawn Vink purchasing decision, and this plan does not price or provision it** (see §7 open item 1). Everything below is the query spec to hand Shannon so that, if/when Listening is available, the Topics can be built in one sitting. Agents never touch the live Sprout account (`OPERATING_RULES.md` §2).

---

## 1. What Listening does for this pilot (and what it must NOT do)

Sprout Listening collects **public conversations that match a query** — including from people who never tag, follow, or message the stores. That fills three gaps the rest of the reporting stack cannot:

1. **Reddit monitor-only mandate.** `CLIENT.md` §6a: Reddit is monitor-only — "monitor Reddit for mentions of the pilot dealerships." Listening is the mechanism that actually does this. Reddit is a first-class Sprout Listening network, and the operator has reported four of five rooftops have **zero** organic Reddit footprint and zero responses to public complaints (`CLIENT.md` §9). A Brand Health topic makes that absence measurable and catches new complaints as they appear.
2. **Reputation signal outside owned channels.** Named individual staff drive nearly all positive reviews (`CLIENT.md` §9); Listening surfaces unsolicited praise/complaints that reviews and owned-channel comments miss.
3. **Share of voice vs. each store's competitive set** (`competitors/COMPETITOR_SETS.md`), per market — a baseline number for the Month 6 readout.

**What Listening is NOT used for in this pilot:**
- **Not publishing or engagement.** No one replies to a discovered mention without Shannon's explicit approval — a discovered Reddit complaint is an **escalation item to Shannon**, never a reply action (§5).
- **Not a group rollup.** Findings are reported per store, never blurred into one Greenway number (`KPI_FRAMEWORK.md` §1.4 discipline applies here too).
- **Not a substitute for the KPI dashboard.** Listening feeds the monthly report's narrative and the Reddit line (K16); it does not replace native metrics.

---

## 2. Topic architecture — what to build

Sprout licenses Listening by **active Topic allotment** (the number included depends on the contract — **TO VERIFY**, §7 item 2). The architecture below assumes a small allotment and degrades gracefully:

| Priority | Topic | Template (Sprout) | Covers |
|---|---|---|---|
| 1 | **Greenway Pilot — Brand Health** | Brand Health | All 5 rooftops in ONE topic, segmented per store by keyword group (§3). This is the topic that satisfies the Reddit monitor-only mandate. |
| 2 | **Nashville Market — Competitive** | Competitive Analysis | Stores 03+04 (one shared market, one shared GM-provided set) vs. Murfreesboro Kia, Wyatt Johnson Kia Clarksville (§4) |
| 3 | **Jacksonville Market — Competitive** | Competitive Analysis | Store 02 vs. Kia on Atlantic, Kia of Orange Park, Kia Jax, Family Kia (§4) |
| 4 | **Kansas City Market — Competitive** | Competitive Analysis | Store 05 vs. Bob Sight, Rob Sight, Blue Springs Ford, Metro Ford (§4) |
| 5 | **West Palm Beach Market — Competitive** | Competitive Analysis | Store 01 — **BLOCKED: no competitor set yet** (GM Mike Wangle has not provided names, `COMPETITOR_SETS.md`). Build only after the set exists. |

**Why one Brand Health topic, not five:** the five rooftop names are distinct enough to segment inside one topic (per-store keyword groups + Sprout's filter/tag tools), and Topic allotments are scarce. Per-store isolation is enforced **at the reporting layer** — every extract from the topic is filtered to one store's keyword group before it enters that store's report. If the allotment turns out to be generous (≥8 active topics), split Brand Health into five per-store topics instead — cleaner segmentation, same queries.

**Why competitive topics are per market, not per store:** a share-of-voice comparison only makes sense inside one geographic market, and Stores 03/04 explicitly share ONE set (`COMPETITOR_SETS.md` — never invent a differing set for either rooftop).

---

## 3. Topic 1 — Brand Health: the query spec

### 3.1 The naming-collision problem (read before building)

"Greenway" is a hostile keyword on its own. Three collision classes force every include-term to be either a **full store name** or a **short name AND-ed with location/context terms**:

1. **Greenway Auto Group's own non-pilot rooftops.** Several Orlando-metro rooftops carry near-identical names (`CLIENT.md` §9 — distinguish by street address/market, never by store name alone). Critically, there is Orlando-area "Greenway Ford" presence that will pollute Store 05 ("Greenway Ford Kansas City") queries unless geo-guarded.
2. **Greenway Health** — a large healthcare-software company with heavy conversation volume.
3. **Generic "greenway"** — trails, parks, cycling routes ("the greenway", "greenway trail").

### 3.2 Include keywords (per-store keyword groups)

Build these as five labeled keyword groups inside the topic. Quoted strings are exact phrases; `AND` groups mean Sprout's "and contains" pairing in the Query Builder.

**Store 01 — Greenway Kia West Palm Beach**
- `"Greenway Kia West Palm Beach"`
- `"greenwaykiawpb"` (IG handle — catches handle-style mentions)
- (`"Greenway Kia"` AND [`"West Palm"` OR `"WPB"` OR `"Palm Beach"`])

**Store 02 — Greenway Kia at the Avenues**
- `"Greenway Kia at the Avenues"` · `"Greenway Kia Avenues"`
- `"greenwaykiajax"` (IG/TikTok handle)
- (`"Greenway Kia"` AND [`"Jacksonville"` OR `"Jax"` OR `"Avenues"`])

**Store 03 — Greenway Kia Rivergate**
- `"Greenway Kia Rivergate"`
- (`"Greenway Kia"` AND [`"Rivergate"` OR `"Madison TN"` OR `"Madison, TN"`])

**Store 04 — Greenway Kia Hickory Hollow**
- `"Greenway Kia Hickory Hollow"`
- (`"Greenway Kia"` AND [`"Hickory Hollow"` OR `"Antioch"`])
- **Legacy-name catch:** `"Universal Kia Hickory Hollow"` — the rooftop's pre-rebrand name; locals still use it. Unambiguous, so it can be a bare phrase.

**Stores 03/04 shared legacy-name catch (flag, don't attribute):**
- (`"Universal Kia"` AND [`"Nashville"` OR `"Madison"` OR `"Antioch"` OR `"Rivergate"` OR `"Hickory Hollow"` OR `"TN"`]) — mentions of the old name that don't specify a rooftop **cannot be attributed to 03 vs 04 unilaterally** (mirrors the `@universalkia` YouTube attribution flag, `CLIENT.md` §8.1). Tag these `store-0304-unattributed` and hold for the GM/governance discussion; never silently assign them to one store's report.

**Store 05 — Greenway Ford Kansas City**
- `"Greenway Ford Kansas City"` · `"Greenway Ford of Kansas City"`
- (`"Greenway Ford"` AND [`"Kansas City"` OR `"Raytown"` OR `"KC"` OR `"Missouri"` OR `"MO"`])
- **Never** bare `"Greenway Ford"` — it collides with the Orlando rooftop of the same name (collision class 1).

**Group-level catch (attribute manually):**
- `"Greenway Auto Group"` — group-level mentions; route to the store named in context, else keep as group-level narrative only (never counted in a store's numbers).

### 3.3 Exclude keywords (apply to the whole topic)

- `"Greenway Health"` · `"greenwayhealth"` — healthcare software company
- `"greenway trail"` · `"greenway park"` · `"bike greenway"` · `"the greenway"` (test this last one in Preview first — see §3.5 — and drop it if it kills real mentions)
- Orlando-rooftop guard: `"Orlando"` **unless** paired with a pilot-store phrase — in Sprout terms, add `"Greenway Dodge"`, `"Greenway Kia East"`, `"Greenway Kia North"` and other known non-pilot rooftop full names as excludes rather than excluding "Orlando" wholesale (an exact non-pilot store name is a safer exclude than a city). **The definitive non-pilot rooftop name list is TO VERIFY with the operator** (§7 item 4) — do not guess it into the live query.
- Hyundai guard is **not needed as an exclude** here (Brand Health tracks our stores, not Hyundai), but see §4 for the competitive topics.

### 3.4 Network / source settings

- **Networks on:** X/Twitter, **Reddit** (the mandate surface), YouTube, Tumblr, web/news/blogs, plus Facebook & Instagram to the extent Sprout's Meta coverage allows.
- **Reddit:** do NOT restrict to specific subreddits at first — dealer complaints surface in r/askcarsales, r/Kia, r/Ford, r/nashville, r/jacksonville, r/kansascity, r/whatcarshouldIbuy and one-off local subs. Run broad for the first month, then narrow if noise demands it.
- **Language:** English. **Geo filters:** leave OFF at the query level (geo data is sparse and would silently drop mentions); location precision comes from the AND-ed location keywords instead.
- **Date range:** set the topic's backfill to the maximum the license allows (typically up to 13 months of historical data on activation — **TO VERIFY** per contract) so the Month 1 audit period is covered retroactively.

### 3.5 Build-and-tune procedure (for Shannon, ~45 min)

1. In Listening → Query Builder, create the topic from the **Brand Health** template, name it `Greenway Pilot — Brand Health`.
2. Enter the §3.2 include groups and §3.3 excludes.
3. **Run Preview before saving.** Sprout shows a sample of matching messages. Check: (a) are pilot-store mentions present? (b) is the sample polluted by Greenway Health / trails / Orlando rooftops? Tune excludes until the sample is ≥ roughly 80% relevant. Do not chase 100% — over-excluding silently drops real complaints, which is worse than hand-skimming some noise.
4. Save/activate; confirm the backfill window loaded.
5. After 7 days, re-check volume: if a store's keyword group returns zero mentions, that is a **finding (absence), not a broken query** — it corroborates the operator's zero-footprint report and goes in the monthly narrative as such.

---

## 4. Topics 2–5 — Competitive Analysis: the query specs

One topic per market, built from the **Competitive Analysis** template so Sprout computes **share of voice** automatically. Include-side = that market's pilot-store group(s) from §3.2 reused verbatim. Competitor-side per market:

### 4.1 Nashville Market (Stores 03 + 04 — ONE shared topic)
| Brand in topic | Keywords |
|---|---|
| Greenway (ours) | Store 03 + Store 04 groups from §3.2 (incl. Universal Kia legacy catches) |
| Murfreesboro Kia | `"Murfreesboro Kia"` — **name TO VERIFY with GM before any client-facing use** (transcript read "Murphy's Brew Kia"; near-certain but unconfirmed, `COMPETITOR_SETS.md`) |
| Wyatt Johnson Kia | `"Wyatt Johnson Kia"` · (`"Wyatt Johnson"` AND `"Kia"`) |

**Exclusions & rules:** **Greenway Kia Franklin is NOT in this topic** — sibling benchmark, never a competitor, excluded from any competitive framing (`COMPETITOR_SETS.md` open question). Add `"Greenway Kia Franklin"` as an explicit exclude on the ours-side keyword group so its mentions don't inflate our share of voice. **No Hyundai or Kia+Hyundai dealership appears in any competitive topic, any market** (operator directive 2026-08-22 — overriding and permanent).

### 4.2 Jacksonville Market (Store 02)
| Brand in topic | Keywords |
|---|---|
| Greenway (ours) | Store 02 group from §3.2 |
| Kia on Atlantic | `"Kia on Atlantic"` · `"Southside Kia"` (former name — locals still use it) |
| Kia of Orange Park | `"Kia of Orange Park"` · (`"Kia"` AND `"Orange Park"`) |
| Kia Jax | `"Kia Jax"` · `"kiajax"` (group site; also catches "Kia Stores of Jacksonville" umbrella — tag these group-level, ownership structure TO VERIFY) |
| Family Kia | (`"Family Kia"` AND [`"Jacksonville"` OR `"Jax"` OR `"St. Augustine"`]) — "Family Kia" is too generic to run bare |

### 4.3 Kansas City Market (Store 05)
| Brand in topic | Keywords |
|---|---|
| Greenway (ours) | Store 05 group from §3.2 (geo-guarded — never bare "Greenway Ford") |
| Bob Sight | `"Bob Sight"` (Ford/Kia dealer family name — distinctive enough to run bare; verify in Preview) |
| Rob Sight | `"Rob Sight"` · `"Rob Sight Ford"` |
| Blue Springs Ford | `"Blue Springs Ford"` |
| Metro Ford | (`"Metro Ford"` AND [`"Kansas City"` OR `"KC"` OR `"Missouri"`]) — "Metro Ford" exists in many cities; must be geo-guarded |

### 4.4 West Palm Beach Market (Store 01) — DO NOT BUILD YET
No competitor set exists (`COMPETITOR_SETS.md` — needs GM Mike Wangle or the operator). Building a competitive topic from invented names would violate the no-invented-facts rule. **Blocked until the set is provided**; Store 01 is still fully covered by the Brand Health topic in the meantime.

---

## 5. Alerts, escalation, and who touches what

- **Spike alert ON** for the Brand Health topic (Sprout's message-spike alert): a sudden volume spike at a single rooftop is the early-warning for a local reputation event. Alert recipient: **Shannon McNeil only** (agents hold no Sprout access).
- **Negative-sentiment review cadence:** Shannon (or a store trainee she grants read access, per `TRAIN_THE_TRAINER_PLAYBOOK.md` gatekeeping) skims new negative-sentiment mentions **weekly minimum**. Any complaint that names a store, a staff member, or a safety/legal issue escalates to Shannon the same day.
- **Nobody replies from Listening.** Discovered mentions — Reddit complaints included — are escalation/analysis items. Any public response is Shannon's call, drafted through the normal pipeline (specialist drafts → lead reviews → Shannon approves), and on Reddit the standing rule is stronger: **monitor-only, no pilot participation** without an explicit operator decision (`CLIENT.md` §6a).
- **Sentiment corrections:** Sprout auto-sentiment misreads sarcasm and dealer-speak ("they killed it" = positive). Whoever runs the weekly skim reclassifies obvious misreads so the monthly sentiment trend is honest; note in the report that sentiment is auto-classified with manual spot correction.

---

## 6. How Listening feeds the monthly report

- **K16 Reddit (currently "manual"):** the Brand Health topic's Reddit slice **becomes the K16 source** — mention count + link log per store per month, replacing ad-hoc manual searching. Zero mentions is recorded as zero (absence finding), not blank.
- **Monthly capture:** on the same fixed capture day as everything else (`SPROUT_CONFIG_PLAN.md` §5.1, date TO VERIFY), export per-store: mention volume, sentiment split, top-3 mentions by potential reach, and (per market) share of voice. Screenshot the Topic Insights view as capture evidence, mirroring audit evidence practice.
- **Where it lands:** the store's `MONTHLY_REPORT-<period>.md` narrative ("what people are saying") + the share-of-voice number in the competitive section. **Never a group rollup** — five stores, five slices; Nashville SoV is reported to Stores 03 and 04 as their shared market number, labeled as shared.
- **Baseline for the Month 6 readout:** capture the activation-month numbers (volume, sentiment split, SoV per market) as the pilot baseline the February 2027 readout compares against.

---

## 7. Open items / TO VERIFY (none assumed)

1. **[GATE] Is the Listening add-on licensed?** Listening is a separate paid Sprout add-on, billed at cost like all Sprout licensing (`CLIENT.md` §4). **Shannon + Shawn Vink** decide/confirm. If not licensed, this entire plan waits — the only fallback for the Reddit mandate is continued manual Reddit search (current K16 method).
2. **Active Topic allotment** in the contract — determines whether Brand Health stays consolidated (§2) or splits per store.
3. **Historical backfill window** on activation (assumed up to ~13 months — verify per contract) — determines whether the audit period is covered retroactively.
4. **Definitive list of non-pilot Greenway rooftop names** (Orlando metro etc.) for the §3.3 exclude list — request via Shannon; do not guess.
5. **"Murfreesboro Kia" name confirmation** with GM James Galuszka before the Nashville topic goes anywhere client-facing.
6. **Store 01 competitor set** from GM Mike Wangle — unblocks §4.4.
7. **Universal Kia unattributed-mention handling** — confirm with Shannon how `store-0304-unattributed` mentions are presented to the shared GM (ties to the `@universalkia` YouTube attribution governance item).
8. **Who runs the weekly negative-sentiment skim** — Shannon, or a trainee she grants read-only Listening access (her call, per training gatekeeping).
9. **Topic tag labels** (`store-01`…`store-05`, `store-0304-unattributed`) against the live Sprout tag system — semantics fixed, labels TO VERIFY (same caveat as `SPROUT_CONFIG_PLAN.md` §5.2).

---

## 8. Relationship to the rest of the workspace

- **Companion config:** `reporting/SPROUT_CONFIG_PLAN.md` (groups, queues, approvals, tagging — this file adds the Listening module only).
- **Competitor keywords:** `competitors/COMPETITOR_SETS.md` (source of truth; per-store, never group-blurred; Hyundai/dual-brand permanently out of scope; Franklin = sibling benchmark, never competitor).
- **Reddit mandate & reputation leads:** `CLIENT.md` §6a, §9.
- **KPI hookup:** `reporting/KPI_FRAMEWORK.md` (K16 Reddit), `reporting/REPORTING_TEMPLATE.md` §4, `reporting/GM_KPI_FRAMEWORK.md` (per-rooftop views).
- **Operating rules:** `OPERATING_RULES.md` §2 (no agent touches Sprout), §3 (source labeling — every external claim in a client-facing report carries its verification status).

*End of plan — nothing configured, licensed, or published; every live-system fact marked TO VERIFY.*
