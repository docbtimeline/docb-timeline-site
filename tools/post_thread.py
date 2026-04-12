#!/usr/bin/env python3
"""Post X thread for DocB Timeline article via tweepy."""
import os
import tweepy
import time

# Load creds from .env file
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
    "European energy bills this winter may spike to 2022 crisis levels \u2014 not because of a war, but because of a engineering flaw hiding inside the green transition itself.",

    "EU gas storage is at 33.5% \u2014 up to 14 points below the five-year average. LNG injections collapsed 77% in April. Asian buyers are outbidding Europe for cargoes during the exact months Europe needs to refill. The buffer is nearly empty.",

    "The Iberian blackout knocked out power for 50 million people in under 90 seconds. Solar was providing half of Spain\u2019s electricity when thousands of inverters disconnected at once. The grid was designed for coal plants, not distributed solar. Every failure spins up a gas turbine.",

    "Here\u2019s the trap: every time solar glitches and gas turbines fire up to stabilise the grid, they burn the fuel Europe should be injecting into storage for winter. The backup system depletes the buffer it depends on. One crisis feeds the other.",

    "What to watch: EU gas storage via GIE AGSI+. If it\u2019s below 55% by August 1, Europe needs injection rates it has never sustained. Prediction: EU storage won\u2019t hit its own 90% target by November and may struggle to clear 70%.",

    "Europe built a grid that needs gas to stabilise the renewables meant to replace gas \u2014 and the gas is running out.\n\nhttps://docbtimeline.com/posts/europes-storage-gamble/",
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
