#!/usr/bin/env python3
"""
Etsy Sales Prediction Model
Uses the 10K shops dataset to predict sales from reviews, favorites, ratings, listings.
"""

import csv
import json
import os
from datetime import datetime

# Load data
DATA_DIR = "/root/StallSpy/tool/ml/etsy-sales-prediction"

def load_data():
    with open(os.path.join(DATA_DIR, "Etsy_top10000shops.csv"), encoding="latin-1") as f:
        rows = list(csv.DictReader(f))
    
    X = []
    y = []
    meta = []
    
    for r in rows:
        try:
            sold = int(r["sold_count"])
            reviews = int(r["total_rating_count"])
            favs = int(r["favorites_count"])
            rating = float(r["average_rating"])
            active = int(r["active_listing_count"]) if r["active_listing_count"] else 0
            digital = int(r["digital_listing_count"]) if r["digital_listing_count"] else 0
            
            # Features
            X.append({
                "reviews": reviews,
                "favorites": favs,
                "rating": rating,
                "active_listings": active,
                "digital_listings": digital,
                "review_favorite_ratio": reviews / max(favs, 1),
                "reviews_per_listing": reviews / max(active, 1),
                "has_customization": 1 if r.get("additional_customization") == "TRUE" else 0,
            })
            y.append(sold)
            meta.append({"shop_name": r["shop_name"], "sold": sold})
        except (ValueError, ZeroDivisionError):
            continue
    
    return X, y, meta

def train_simple_model(X, y):
    """Train a basic gradient boosting model without sklearn dependency."""
    # Convert to numeric arrays
    import array
    
    features = ["reviews", "favorites", "rating", "active_listings", 
                "digital_listings", "review_favorite_ratio", "reviews_per_listing",
                "has_customization"]
    
    n = len(X)
    n_features = len(features)
    n_train = int(n * 0.8)
    
    # Simple decision stump ensemble (gradient boosting lite)
    preds = [0.0] * n
    learning_rate = 0.1
    n_estimators = 100
    
    for t in range(n_estimators):
        # Compute residuals
        residuals = [y[i] - preds[i] for i in range(n)]
        
        # Find best split for each feature
        best_feature = 0
        best_threshold = 0
        best_left_mean = 0
        best_right_mean = 0
        best_improvement = float("inf")
        
        for fi in range(n_features):
            # Sort by this feature
            vals = [(X[i][features[fi]], residuals[i]) for i in range(n)]
            vals.sort(key=lambda x: x[0])
            
            # Try median splits
            for split_idx in [n//4, n//2, 3*n//4]:
                left = [r for _, r in vals[:split_idx]]
                right = [r for _, r in vals[split_idx:]]
                if left and right:
                    left_mean = sum(left) / len(left)
                    right_mean = sum(right) / len(right)
                    improvement = sum((r - left_mean)**2 for r in left) + \
                                  sum((r - right_mean)**2 for r in right)
                    if improvement < best_improvement:
                        best_improvement = improvement
                        best_feature = fi
                        best_threshold = vals[split_idx][0]
                        best_left_mean = left_mean
                        best_right_mean = right_mean
        
        # Update predictions
        for i in range(n):
            if X[i][features[best_feature]] <= best_threshold:
                preds[i] += learning_rate * best_left_mean
            else:
                preds[i] += learning_rate * best_right_mean
    
    return preds, features

def evaluate(y_true, y_pred):
    """Compute R², MAE, RMSE."""
    n = len(y_true)
    mean_y = sum(y_true) / n
    
    ss_res = sum((y_true[i] - y_pred[i])**2 for i in range(n))
    ss_tot = sum((y_true[i] - mean_y)**2 for i in range(n))
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    
    mae = sum(abs(y_true[i] - y_pred[i]) for i in range(n)) / n
    rmse = (ss_res / n) ** 0.5
    
    return {"r2": r2, "mae": mae, "rmse": rmse}

if __name__ == "__main__":
    print("Loading data...")
    X, y, meta = load_data()
    print(f"Loaded {len(X)} shops")
    
    print("Training model...")
    preds, features = train_simple_model(X, y)
    
    metrics = evaluate(y, preds)
    print(f"\nModel Performance:")
    print(f"  R²:    {metrics['r2']:.4f}")
    print(f"  MAE:   {metrics['mae']:,.0f}")
    print(f"  RMSE:  {metrics['rmse']:,.0f}")
    
    # Feature importance (rough)
    print(f"\nFeatures used: {features}")
    
    # Show some predictions
    print(f"\nSample predictions vs actual:")
    indices = [0, len(y)//4, len(y)//2, 3*len(y)//4, len(y)-1]
    for i in indices:
        print(f"  {meta[i]['shop_name']}: predicted={preds[i]:,.0f}, actual={y[i]:,}")
    
    # Save results
    results = {
        "timestamp": datetime.now().isoformat(),
        "n_samples": len(y),
        "metrics": metrics,
        "features": features,
        "sample_predictions": [
            {"shop": meta[i]["shop_name"], "actual": y[i], "predicted": round(preds[i])}
            for i in indices
        ]
    }
    
    outpath = "/root/StallSpy/tool/ml/model_results.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {outpath}")
