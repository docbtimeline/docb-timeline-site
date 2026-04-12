#!/usr/bin/env python3
"""Post X thread for DocB Timeline — 'Your 3.5% Amazon Surcharge Began in a Texas Control Room'"""
import os
import tweepy
import time

env_path = os.path.expanduser("~/.openclaw/.env")
creds = {}
with open(env_path) as f:
    for line in f:
        line = line.strip()
        if line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        creds[key.strip()] = val.strip().strip('"')

client = tweepy.Client(
    consumer_key=creds["X_API_KEY"],
    consumer_secret=creds["X_API_SECRET"],
    access_token=creds["X_ACCESS_TOKEN"],
    access_token_secret=creds["X_ACCESS_TOKEN_SECRET"],
)

thread = [
    "The escape valve runs through the chokepoint. The chokepoint runs through the production base. The production base runs through the political commitment.",

    "Diesel just hit $8/gallon in parts of California. Truckers are parking rigs. Amazon sellers are watching a new 3.5% surcharge eat their margins alive. The cause is not what you think.",

    "A refinery explosion in Texas destroyed the unit that turns crude diesel into usable fuel. Normally that's a local story. But US refineries were running at 98% capacity. There was no spare anywhere. One trucking fleet reported $50,000/week in extra fuel costs overnight.",

    "So the missing diesel has to come by tanker through the Strait of Hormuz. But Lloyd's of London just priced war-risk insurance at 7.5% of hull value — $11.25 million per trip on a $150M tanker. Maersk and Hapag-Lloyd slapped emergency surcharges on everything. The strait isn't…",

    "The military workaround — drone escorts through the strait — depends on Ukrainian drone production. That depends on Western funding. That funding is threatened by the same political instability insurers are pricing. The escape valve runs through the chokepoint.",

    "Watch three things: Lloyd's premiums staying above 5% through July even if a ceasefire hits. Valero announcing no restart date by June 15. Amazon's 3.5% FBA surcharge still in place by Q3. If all three hold, this isn't a spike. It's the new structure.",

    "The surcharge doesn't know it started as an explosion and an actuary's spreadsheet.\n\nhttps://docbtimeline.com/posts/amazon-surcharge-texas-control-room/",
]

prev_id = None
for i, text in enumerate(thread):
    print(f"Posting tweet {i+1}/{len(thread)} ({len(text)} chars)...")
    try:
        resp = client.create_tweet(
            text=text,
            in_reply_to_tweet_id=prev_id,
        )
        prev_id = resp.data["id"]
        print(f"  Posted: https://x.com/DocbFuture/status/{prev_id}")
        if i < len(thread) - 1:
            time.sleep(2)
    except Exception as e:
        print(f"  FAILED on tweet {i+1}: {e}")
        break

if prev_id:
    print(f"\nDone. Thread live on @DocbFuture")
