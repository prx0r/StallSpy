#!/usr/bin/env python3
"""
StallShark Storage — local artifact store + R2 backup with verification.

Storage acceptance test:
1. create synthetic file
2. SHA-256 it
3. store locally
4. upload R2
5. download it
6. SHA downloaded bytes
7. exact equality
8. write receipt
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from dotenv import load_dotenv

# Load .env
load_dotenv(Path(__file__).parent.parent / ".env")

ROOT = Path("/root/StallShark")
PRIVATE_DIR = ROOT / "private"
ARTIFACTS_DIR = PRIVATE_DIR / "artifacts" / "sha256"
MANIFESTS_DIR = PRIVATE_DIR / "manifests"
SPOOL_DIR = PRIVATE_DIR / "spool"

def ensure_dirs():
    for d in [PRIVATE_DIR, ARTIFACTS_DIR, MANIFESTS_DIR, SPOOL_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def store_artifact(data: bytes, name: str, media_type: str = "application/octet-stream") -> dict:
    """Store artifact locally with content-addressing."""
    ensure_dirs()
    
    digest = sha256_bytes(data)
    # Content-addressed path: sha256/XX/YYYY...
    artifact_dir = ARTIFACTS_DIR / digest[:2] / digest[2:6]
    artifact_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = artifact_dir / digest
    
    with open(artifact_path, "wb") as f:
        f.write(data)
    
    # Write metadata sidecar
    meta = {
        "digest": digest,
        "name": name,
        "media_type": media_type,
        "size_bytes": len(data),
        "stored_at": datetime.now().isoformat(),
    }
    meta_path = artifact_path.with_suffix(".meta.json")
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    
    return {
        "digest": digest,
        "local_path": str(artifact_path),
        "name": name,
        "size": len(data),
        "stored_at": meta["stored_at"],
    }

def upload_to_r2(local_path: str, r2_key: str) -> dict:
    """Upload to R2 and verify."""
    import boto3
    
    r2 = boto3.client("s3",
        endpoint_url=os.environ["R2_ENDPOINT"],
        aws_access_key_id=os.environ["R2_ACCESS_KEY"],
        aws_secret_access_key=os.environ["R2_SECRET_KEY"],
        region_name="auto",
    )
    
    # Upload
    r2.upload_file(local_path, "stallshark", r2_key)
    
    # Verify
    head = r2.head_object(Bucket="stallshark", Key=r2_key)
    remote_size = head["ContentLength"]
    local_size = os.path.getsize(local_path)
    
    assert remote_size == local_size, f"Size mismatch: local={local_size}, remote={remote_size}"
    
    return {
        "r2_key": r2_key,
        "remote_size": remote_size,
        "local_size": local_size,
        "verified": True,
        "uploaded_at": datetime.now().isoformat(),
    }

def verify_storage() -> dict:
    """Run storage acceptance test."""
    print("=== Storage Acceptance Test ===\n")
    
    # 1. Create synthetic file
    test_data = b"StallShark storage test " + str(time.time()).encode()
    print(f"1. Created: {len(test_data)} bytes")
    
    # 2. SHA it
    digest = sha256_bytes(test_data)
    print(f"2. SHA-256: {digest[:16]}...")
    
    # 3. Store locally
    result = store_artifact(test_data, "storage_test.bin")
    print(f"3. Local: {result['local_path']}")
    
    # 4. Upload R2
    r2_result = upload_to_r2(result["local_path"], f"test/{digest[:16]}.bin")
    print(f"4. R2: {r2_result['r2_key']}")
    
    # 5. Download from R2
    import boto3
    r2 = boto3.client("s3",
        endpoint_url=os.environ["R2_ENDPOINT"],
        aws_access_key_id=os.environ["R2_ACCESS_KEY"],
        aws_secret_access_key=os.environ["R2_SECRET_KEY"],
        region_name="auto",
    )
    download_path = PRIVATE_DIR / "spool" / "download_test.bin"
    r2.download_file("stallshark", f"test/{digest[:16]}.bin", str(download_path))
    
    # 6. SHA downloaded
    downloaded_digest = sha256_file(download_path)
    print(f"5-6. Downloaded SHA: {downloaded_digest[:16]}...")
    
    # 7. Verify equality
    assert digest == downloaded_digest, f"Digest mismatch: {digest} != {downloaded_digest}"
    print(f"7. Verified: SHA match ✓")
    
    # 8. Write receipt
    receipt = {
        "test": "storage_acceptance",
        "digest": digest,
        "r2_key": r2_result["r2_key"],
        "verified": True,
        "timestamp": datetime.now().isoformat(),
    }
    receipt_path = MANIFESTS_DIR / "storage_acceptance.json"
    with open(receipt_path, "w") as f:
        json.dump(receipt, f, indent=2)
    print(f"8. Receipt: {receipt_path}")
    
    # Cleanup test artifacts
    os.remove(str(download_path))
    
    print("\n=== STORAGE ACCEPTANCE TEST PASSED ===")
    return receipt


if __name__ == "__main__":
    verify_storage()
