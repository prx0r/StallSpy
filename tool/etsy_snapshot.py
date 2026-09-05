#!/usr/bin/env python3
"""
Etsy Snapshot — capture current shop/listing metrics from Etsy API.
"""
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).parent))
from book_schemas import make_metric_snapshot, save_record, now_iso, DATA_ROOT

API_KEY = os.environ.get("ETSY_API_KEY", "5c7ipvkesppg7z54plt6ev3k")
SHARED_SECRET = os.environ.get("ETSY_SHARED_SECRET", "mbb9u861jg")

def etsy_get(path, params=None):
    from urllib.parse import urlencode
    url = f"https://openapi.etsy.com/v3/application{path}"
    if params:
        url += "?" + urlencode(params)
    req = Request(url, headers={"x-api-key": f"{API_KEY}:{SHARED_SECRET}"})
    try:
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def snapshot_listings(keywords=None, limit=20):
    """Snapshot current listings for given keywords."""
    if not keywords:
        keywords = [
            "personalized football gift",
            "dogcasso",
            "personalized birthday video",
            "football birthday gift dad",
            "personalized sports gift",
        ]
    
    listings = []
    for kw in keywords:
        data = etsy_get("/listings/active", {
            "keywords": kw,
            "limit": min(limit, 100),
            "fields": "listing_id,title,price,num_favorers,tags,url,views,shop_id"
        })
        
        if "results" in data:
            for r in data["results"]:
                listings.append({
                    "keyword": kw,
                    "listing_id": r["listing_id"],
                    "title": r["title"][:80],
                    "price": r["price"]["amount"] / r["price"]["divisor"],
                    "currency": r["price"]["currency_code"],
                    "favorites": r.get("num_favorers", 0),
                    "views": r.get("views", 0),
                    "shop_id": r.get("shop_id"),
                    "url": r.get("url", ""),
                })
        
        time.sleep(0.3)  # Rate limit
    
    return listings

def run_snapshot(keywords=None):
    """Take a full Etsy snapshot."""
    print("Taking Etsy snapshot...")
    
    listings = snapshot_listings(keywords)
    
    # Aggregate
    total_favorites = sum(l["favorites"] for l in listings)
    total_views = sum(l["views"] for l in listings)
    unique_shops = len(set(l["shop_id"] for l in listings if l.get("shop_id")))
    
    shop_metrics = {
        "total_listings_scanned": len(listings),
        "total_favorites": total_favorites,
        "total_views": total_views,
        "unique_competitor_shops": unique_shops,
        "keywords_scanned": len(set(l["keyword"] for l in listings)),
    }
    
    listing_metrics = []
    for l in listings[:20]:  # Top 20
        listing_metrics.append({
            "listing_id": l["listing_id"],
            "title": l["title"],
            "keyword": l["keyword"],
            "impressions": l["views"],
            "views": l["views"],
            "favorites": l["favorites"],
            "orders": 0,
            "revenue": 0,
        })
    
    snap = make_metric_snapshot(
        shop_metrics=shop_metrics,
        listing_metrics=listing_metrics,
        reviews={"count": 0, "average": 0},
        operations={"open_orders": 0, "failed_renders": 0, "rerolls": 0},
    )
    
    path = save_record(snap, "snapshots")
    
    print(f"\nSnapshot: {snap['snapshot_id']}")
    print(f"  Listings scanned: {len(listings)}")
    print(f"  Total favorites: {total_favorites}")
    print(f"  Total views: {total_views}")
    print(f"  Competitor shops: {unique_shops}")
    print(f"  Saved: {path}")
    
    return snap

if __name__ == "__main__":
    run_snapshot()
