#!/usr/bin/env python3
"""Read-only Sprout Social API pull helper.

Handles auth, pagination, and per-profile aggregation so a session doesn't
re-derive them. Token comes from the SPROUT_TOKEN env var or --token-file;
it is never printed and never written anywhere by this script.

Subcommands:
  verify                       GET /v1/metadata/client (returns customer_id)
  profiles  --customer ID      GET /v1/{cid}/metadata/customer -> profiles JSON
  analytics --customer ID --profiles 1,2,3 --start YYYY-MM-DD --end YYYY-MM-DD
            [--metrics m1,m2] [--out file.json]
            POST /v1/{cid}/analytics/profiles, all pages, prints per-profile
            aggregates and writes raw daily rows to --out
  posts     --customer ID --profiles 1,2,3 --start YYYY-MM-DD --end YYYY-MM-DD
            [--out file.json]
            POST /v1/{cid}/analytics/posts, all pages, writes post rows to --out

Default analytics metrics include the organic/paid impression split, which is
the load-bearing number for this engagement (see SKILL.md).
"""
import argparse, json, os, sys, urllib.request

API = "https://api.sproutsocial.com/v1"

def token(args):
    t = os.environ.get("SPROUT_TOKEN", "")
    if args.token_file:
        t = open(args.token_file).read().strip()
    if not t:
        sys.exit("No token: set SPROUT_TOKEN or pass --token-file")
    return t

def call(tok, path, body=None):
    req = urllib.request.Request(API + path,
        data=json.dumps(body).encode() if body else None,
        headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
        method="POST" if body else "GET")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def paged(tok, path, body):
    rows, page = [], 1
    while True:
        body["page"] = page
        d = call(tok, path, body)
        rows += d.get("data", [])
        if page >= d.get("paging", {}).get("total_pages", 1):
            return rows
        page += 1

DEFAULT_METRICS = ["impressions", "impressions_organic", "impressions_paid",
                   "impressions_unique", "engagements", "video_views",
                   "net_follower_growth", "posts_sent_count",
                   "lifetime_snapshot.followers_count"]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["verify", "profiles", "analytics", "posts"])
    p.add_argument("--token-file")
    p.add_argument("--customer")
    p.add_argument("--profiles")
    p.add_argument("--start")
    p.add_argument("--end")
    p.add_argument("--metrics")
    p.add_argument("--out")
    args = p.parse_args()
    tok = token(args)

    if args.cmd == "verify":
        print(json.dumps(call(tok, "/metadata/client"), indent=1))
        return
    if not args.customer:
        sys.exit("--customer required")
    if args.cmd == "profiles":
        d = call(tok, f"/{args.customer}/metadata/customer")
        out = args.out or "sprout_profiles.json"
        json.dump(d, open(out, "w"), indent=1)
        for pr in d.get("data", []):
            print(pr.get("customer_profile_id"), "|", pr.get("network_type"),
                  "|", pr.get("name"), "|", pr.get("link"))
        print(f"({len(d.get('data', []))} profiles -> {out})")
        return

    ids = args.profiles.replace(" ", "")
    if args.cmd == "analytics":
        metrics = args.metrics.split(",") if args.metrics else DEFAULT_METRICS
        rows = paged(tok, f"/{args.customer}/analytics/profiles", {
            "filters": [f"customer_profile_id.eq({ids})",
                        f"reporting_period.in({args.start}...{args.end})"],
            "metrics": metrics})
        if args.out:
            json.dump(rows, open(args.out, "w"))
        agg = {}
        for row in rows:
            pid = row["dimensions"]["customer_profile_id"]
            a = agg.setdefault(pid, {})
            for k, v in row["metrics"].items():
                if v is None:
                    continue
                if k == "lifetime_snapshot.followers_count":
                    a["followers_latest"] = v  # snapshot, keep last, never sum
                else:
                    a[k] = a.get(k, 0) + v
        print(json.dumps(agg, indent=1))
        print(f"({len(rows)} daily rows{' -> ' + args.out if args.out else ''})",
              file=sys.stderr)
        return

    if args.cmd == "posts":
        rows = paged(tok, f"/{args.customer}/analytics/posts", {
            "filters": [f"customer_profile_id.eq({ids})",
                        f"created_time.in({args.start}T00:00:00..{args.end}T00:00:00)"],
            "fields": ["created_time", "perma_link", "text", "post_type"],
            "metrics": ["lifetime.impressions", "lifetime.impressions_unique",
                        "lifetime.engagements", "lifetime.video_views",
                        "lifetime.likes", "lifetime.comments_count",
                        "lifetime.shares_count"],
            "timezone": "America/New_York"})
        out = args.out or "sprout_posts.json"
        json.dump(rows, open(out, "w"))
        print(f"{len(rows)} posts -> {out}")

if __name__ == "__main__":
    main()
