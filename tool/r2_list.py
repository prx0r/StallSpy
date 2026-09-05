#!/usr/bin/env python3
"""List and download files from Cloudflare R2 bucket."""

import boto3
import json
import os

# R2 credentials
R2_ENDPOINT = "https://954612afb5a97bb15dddcdc70176813d.r2.cloudflarestorage.com"
R2_ACCESS_KEY = "2a8d61c9ed22f5899b8507435a794f5d"
R2_SECRET_KEY = "e673672255567cc054e43479fcee0030862fe998e3bc8d1c447b91503c5c729d"
R2_ACCOUNT_ID = "954612afb5a97bb15dddcdc70176813d"

def get_client():
    return boto3.client(
        "s3",
        endpoint_url=R2_ENDPOINT,
        aws_access_key_id=R2_ACCESS_KEY,
        aws_secret_access_key=R2_SECRET_KEY,
        region_name="auto",
    )

def list_buckets():
    client = get_client()
    resp = client.list_buckets()
    return [b["Name"] for b in resp.get("Buckets", [])]

def list_objects(bucket, prefix="", max_keys=1000):
    client = get_client()
    objects = []
    paginator = client.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix, PaginationConfig={"MaxItems": max_keys}):
        for obj in page.get("Contents", []):
            objects.append({"key": obj["Key"], "size": obj["Size"], "modified": str(obj["LastModified"])})
    return objects

def download_file(bucket, key, local_path):
    client = get_client()
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    client.download_file(bucket, key, local_path)
    return local_path

if __name__ == "__main__":
    print("Buckets:")
    for b in list_buckets():
        print(f"  {b}")
