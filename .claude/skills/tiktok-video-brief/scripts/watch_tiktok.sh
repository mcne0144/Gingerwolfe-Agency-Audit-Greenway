#!/bin/bash
# Fetch a public TikTok video page, extract metadata + play URL, download the mp4,
# and extract N evenly spaced frames for review.
#
# usage: watch_tiktok.sh <tiktok-video-url> <output-dir> [nframes]
#   nframes default 14; use 12 for clips under 10s, 16 for clips over 45s.
#
# Produces in <output-dir>:
#   meta.json    caption, createTime, duration, public stats, sticker (on-screen) text
#   video.mp4    the video
#   fNN_TTT.Ts.jpg  frames named by index and timestamp
#
# Works without yt-dlp (whose TikTok extractor breaks often): the page's embedded
# __UNIVERSAL_DATA_FOR_REHYDRATION__ JSON carries everything, and the play URL
# downloads with the page cookies + a browser UA + tiktok.com referer.
set -e
URL="$1"; D="$2"; N="${3:-14}"
if [ -z "$URL" ] || [ -z "$D" ]; then echo "usage: watch_tiktok.sh <url> <output-dir> [nframes]"; exit 1; fi
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
mkdir -p "$D"
curl -s --max-time 40 -A "$UA" -c "$D/cookies.txt" "$URL" -o "$D/page.html"
python3 - "$D" <<'EOF'
import json, re, sys, html as h
d = sys.argv[1]
html = open(d + '/page.html').read()
m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>', html, re.S)
if not m:
    sys.exit("No embedded JSON found. The page may be a captcha/login wall; retry, or try a different network egress.")
data = json.loads(m.group(1))
detail = data['__DEFAULT_SCOPE__'].get('webapp.video-detail')
if not detail or 'itemInfo' not in detail:
    sys.exit("Page JSON has no video detail (video may be private, deleted, or region-blocked).")
item = detail['itemInfo']['itemStruct']
v = item['video']
meta = {
    'url_author': item['author']['uniqueId'],
    'desc': item['desc'],
    'createTime': item['createTime'],
    'duration_s': v['duration'],
    'stats': item['stats'],
    'sticker_text': [s.get('stickerText') for s in item.get('stickersOnItem', [])],
}
json.dump(meta, open(d + '/meta.json', 'w'), indent=1)
open(d + '/playurl.txt', 'w').write(h.unescape(v.get('playAddr') or v.get('downloadAddr') or ''))
print('metadata ok: duration', v['duration'], 's, plays', item['stats'].get('playCount'))
EOF
PLAY=$(cat "$D/playurl.txt")
[ -z "$PLAY" ] && { echo "No play URL in page JSON"; exit 1; }
curl -s --max-time 120 -A "$UA" -b "$D/cookies.txt" -e "https://www.tiktok.com/" -o "$D/video.mp4" "$PLAY"
SIZE=$(wc -c < "$D/video.mp4")
[ "$SIZE" -lt 50000 ] && { echo "Download too small ($SIZE bytes) — likely blocked. Inspect $D/video.mp4"; exit 1; }
echo "video: $SIZE bytes"
DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$D/video.mp4")
python3 - "$D/video.mp4" "$DUR" "$N" "$D" <<'EOF'
import subprocess, sys
vid, dur, n, out = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
for i in range(n):
    t = dur * (i + 0.5) / n
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", vid,
                    "-frames:v", "1", "-vf", "scale=540:-1", "-y",
                    f"{out}/f{i:02d}_{t:05.1f}s.jpg"], check=True)
print("frames extracted:", n)
EOF
rm -f "$D/page.html" "$D/cookies.txt" "$D/playurl.txt"
ls "$D"
