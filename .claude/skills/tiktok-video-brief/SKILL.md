---
name: tiktok-video-brief
description: Watch a public TikTok (or other short vertical video) frame-by-frame and write a reshootable INTERNAL creative brief in the Bright Matter house style, with shot-by-shot timing, why-it-worked mechanics, a numbered reshoot template, and mapping to the pilot-store playbook. Use this whenever the task is to analyze, break down, "watch", reverse-engineer, or write a brief from a specific social video URL — a sibling-store post, a competitor's viral clip, a format reference the operator sends — even if the user only asks "why did this work" or "can we copy this". Also use when a batch of video URLs needs one brief each.
---

# TikTok video breakdown → reshootable creative brief

Turn a video URL into a brief a store could actually reshoot, without ever fabricating what cannot be observed.

## Why this skill exists

yt-dlp's TikTok extractor breaks routinely, and "watching" a video as an agent means frames + metadata, not audio. This skill bundles a downloader that parses the video page's own embedded JSON (metadata, public stats, on-screen sticker text, play URL) and extracts evenly spaced frames. The brief format was validated against five Greenway sibling posts (see `content/success-models/briefs/` for finished examples worth imitating).

## Workflow

### 1. Download and frame the video

```bash
bash .claude/skills/tiktok-video-brief/scripts/watch_tiktok.sh <url> <scratch-dir>/<slug> [nframes]
```

Pick nframes by duration: 12 for under 10s, 14 for 10–45s, 16 above. Run it once per URL. If it fails on the embedded-JSON step, the page served a captcha or the video is private; report that rather than guessing at content.

### 2. Read the evidence

1. Read `meta.json` first: caption, duration, public stats (plays, likes, comments, shares, saves), and `sticker_text` (TikTok's own record of on-screen overlay text, often the hook).
2. Read the frames in order with the Read tool (they are images). Read every frame for short clips; for longer ones read every other frame first and fill gaps where the structure is unclear.
3. Note per frame: who is in frame, framing (wide/medium/macro), location, visible on-screen text, and what changed since the previous frame. Scene changes between adjacent frames mark the edit points.

### 3. Honesty boundaries (these make the brief credible)

- Audio is not transcribed. Never quote dialogue. Isolated caption words visible in single frames may be listed as exactly that. Say explicitly in the brief that audio was not transcribed.
- Only claim what frames or metadata show. Uncertain counts get "at least N". Public stats are quoted with their retrieval date.
- If observation contradicts an existing analysis doc, say so in the brief and add a short amendment note to the doc rather than silently diverging.

### 4. Write the brief

One file per video. For this repo: `content/success-models/briefs/BRIEF_NN_<slug>.md`, and add a row to that directory's README index. Use this structure (match the register of the existing briefs):

```markdown
# BRIEF NN — <short name> (<duration>)
**Status:** INTERNAL creative brief. Reshoot template, not client-facing.
**Source:** <url>
**Caption:** "<verbatim>"  (+ **Sticker text** if any)
**Duration / Retrieved <date>:** plays, likes, comments, shares, saves
## 1. What actually happens (from frames)   ← shot-by-shot table with time ranges
## 2. Why it worked                          ← numbered mechanics, tied to the metric pattern
## 3. Reshootable template                   ← numbered steps: cast, rig/gear, location, shot list, on-screen text, caption pattern, length, compliance
## 4. Pilot-store mapping                    ← per store, citing the strategy doc rows it feeds
## 5. Verification notes                     ← what was not verifiable, stat drift, source-specific facts not to reuse
```

Section 2 must explain the mechanism (why shares/saves/comments moved), not just praise the video. Section 3 must be executable by a store employee with a phone: name the number of camera setups, the exact overlay text pattern, and the caption pattern. Compliance lines that recur in this engagement: vehicle verifiably on the lot, real offers with full disclaimer in caption, two-source rule before naming staff, no forward-model titles, no hype copy.

## House rules that always apply here

INTERNAL label on every brief; no client contact; formats are copied but footage never is; no em-dash-heavy prose (write with periods, commas, colons); sibling stores are benchmarks, never framed as rivals. See `OPERATING_RULES.md` and `CLIENT.md` when working in this repo; outside it, keep the honesty boundaries and the brief structure.
