#!/usr/bin/env python3
"""
Etsy Market Scraper — pulls listings, reviews, shop data via API.
Saves to CSV + JSON for time-series analysis.
"""

import csv
import json
import time
import sys
import os
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError

API_KEY = os.environ.get("ETSY_API_KEY", "")
SHARED_SECRET = os.environ.get("ETSY_SHARED_SECRET", "os.environ.get("ETSY_SHARED_SECRET", "")")
BASE = "https://openapi.etsy.com/v3/application"

HEADERS = {
    "x-api-key": f"{API_KEY}:{SHARED_SECRET}"
}

def api_get(path, params=None):
    url = f"{BASE}{path}"
    if params:
        url += "?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except HTTPError as e:
        if e.code == 429:
            print(f"  Rate limited, sleeping 5s...")
            time.sleep(5)
            with urlopen(req, timeout=15) as resp:
                return json.loads(resp.read())
        raise

def search_listings(keyword, limit=100):
    """Search active listings, returns up to limit results."""
    data = api_get("/listings/active", {
        "keywords": keyword,
        "limit": min(limit, 100),
        "fields": "listing_id,title,price,num_favorers,tags,creation_timestamp,url,shop_id,views"
    })
    return data.get("results", []), data.get("count", 0)

def get_reviews(listing_id, limit=10):
    """Get reviews for a listing."""
    data = api_get(f"/listings/{listing_id}/reviews", {"limit": limit})
    return data.get("results", []), data.get("count", 0)

def get_shop(shop_id):
    """Get shop details."""
    return api_get(f"/shops/{shop_id}")

def scrape_keyword(keyword, max_listings=200, get_shop_data=True, get_review_data=True):
    """Full scrape for a keyword: listings + shops + reviews."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_kw = keyword.replace(" ", "_")[:40]
    
    listings = []
    shops_seen = {}
    offset = 0
    
    print(f"\n{'='*60}")
    print(f"SCRAPING: '{keyword}'")
    print(f"Target: {max_listings} listings")
    print(f"{'='*60}")
    
    while offset < max_listings:
        batch, total = search_listings(keyword, limit=100)
        if not batch:
            break
        
        print(f"  Offset {offset}: got {len(batch)} listings (total available: {total})")
        
        for listing in batch:
            row = {
                "scrape_timestamp": timestamp,
                "keyword": keyword,
                "listing_id": listing["listing_id"],
                "title": listing["title"],
                "price_amount": listing["price"]["amount"] / listing["price"]["divisor"],
                "price_currency": listing["price"]["currency_code"],
                "num_favorers": listing.get("num_favorers", 0),
                "views": listing.get("views", 0),
                "shop_id": listing.get("shop_id"),
                "tags": "|".join(listing.get("tags", [])),
                "url": listing.get("url", ""),
            }
            
            # Reviews
            if get_review_data:
                try:
                    reviews, review_count = get_reviews(listing["listing_id"], limit=10)
                    row["review_count"] = review_count
                    if reviews:
                        row["avg_review_rating"] = sum(r["rating"] for r in reviews) / len(reviews)
                        row["latest_review_date"] = reviews[0].get("created_timestamp", 0)
                    else:
                        row["avg_review_rating"] = 0
                        row["latest_review_date"] = 0
                    time.sleep(0.3)  # Be polite on review endpoints
                except Exception as e:
                    row["review_count"] = 0
                    row["avg_review_rating"] = 0
                    row["latest_review_date"] = 0
            
            # Shop data (once per shop)
            shop_id = listing.get("shop_id")
            if get_shop_data and shop_id and shop_id not in shops_seen:
                try:
                    shop = get_shop(shop_id)
                    shops_seen[shop_id] = {
                        "shop_name": shop.get("shop_name", ""),
                        "total_sales": shop.get("transaction_sold_count", 0),
                        "review_average": shop.get("review_average", 0),
                        "review_count": shop.get("review_count", 0),
                        "num_favorers": shop.get("num_favorers", 0),
                        "listing_active_count": shop.get("listing_active_count", 0),
                    }
                    time.sleep(0.3)
                except:
                    pass
            
            if shop_id and shop_id in shops_seen:
                row["shop_name"] = shops_seen[shop_id]["shop_name"]
                row["shop_total_sales"] = shops_seen[shop_id]["total_sales"]
                row["shop_review_average"] = shops_seen[shop_id]["review_average"]
                row["shop_review_count"] = shops_seen[shop_id]["review_count"]
                row["shop_favorers"] = shops_seen[shop_id]["num_favorers"]
                row["shop_active_listings"] = shops_seen[shop_id]["listing_active_count"]
            
            listings.append(row)
        
        offset += len(batch)
        if offset >= total:
            break
        time.sleep(1.2)  # Respect rate limit
    
    # Save
    outdir = f"/root/StallShark/tool/data/{safe_kw}"
    os.makedirs(outdir, exist_ok=True)
    
    # JSON (full data)
    json_path = f"{outdir}/{timestamp}.json"
    with open(json_path, "w") as f:
        json.dump(listings, f, indent=2)
    
    # CSV (flat, for analysis)
    csv_path = f"{outdir}/{timestamp}.csv"
    if listings:
        keys = list(listings[0].keys())
        with open(csv_path, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(listings)
    
    print(f"\n  Results: {len(listings)} listings, {len(shops_seen)} shops")
    print(f"  Saved: {json_path}")
    print(f"  Saved: {csv_path}")
    
    return listings, shops_seen


if __name__ == "__main__":
    keywords = sys.argv[1:] if len(sys.argv) > 1 else [
        "personalized football gift",
        "scored winning goal gift",
        "personalized birthday video",
        "football birthday gift dad",
        "personalized sports gift",
    ]
    
    all_listings = []
    all_shops = {}
    
    for kw in keywords:
        listings, shops = scrape_keyword(kw, max_listings=200)
        all_listings.extend(listings)
        all_shops.update(shops)
        time.sleep(2)
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {len(all_listings)} listings, {len(all_shops)} unique shops")
    print(f"{'='*60}")
