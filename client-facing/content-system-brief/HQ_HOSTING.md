# Hosting this brief on Bright Matter HQ

Goal: the brief lives on HQ (hq.brightmattersocial.com), stays private now, and goes live with one flip when ready. Run these from the Mac that holds the app repo (`~/Claude Code Macbook/bright-matter-hq/`) — the code and Fly access are not reachable from the cloud workspace.

## Stage now (private)

1. Copy `index.html` and `details.html` from this folder into the app repo as `public/greenway-content-brief/index.html` and `public/greenway-content-brief/details.html` (they link to each other by relative path, so keep them in one folder; same hosting pattern as the audit report).
2. In the admin app, add a card for it (a `dashboards` entry pointing at `/greenway-content-brief/`) and leave **visible off**. Portal roles never see `visible=0` rows, so only Shannon sees the card.
3. `fly deploy` from the app repo.

## Go live (when ready)

Flip the card's visible toggle in the admin app. The flip is audit-logged in `visibility_log` like every other publish.

## Caveat worth knowing

Static files under `public/` are served without login — the `visible` flag hides the *card* from GMs and corporate, but the raw URL answers for anyone who has it. If that matters before launch, hold steps 1 and 3 until go-live and only add the private card now; the brief itself then ships in the same deploy that makes it live.

The brief is self-contained (two HTML files, Google Fonts only, no build step), so no other app changes are needed.
