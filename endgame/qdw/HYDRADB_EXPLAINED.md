# HydraDB — What It Actually Is

**Date:** 5 September 2026

---

## What HydraDB Is

HydraDB is a **distributed graph database** written in Rust, built on SlateDB with S3-compatible object storage. It is NOT SQL. It is NOT a traditional database.

### Key Properties

- **Graph database** — nodes, edges, relationships, traversals
- **Object-store native** — S3 is the durable source of truth
- **OpenCypher queries** — but a deliberately limited subset
- **Bolt 5.x protocol** — Neo4j-driver compatible
- **GraphBLAS traversal** — sparse matrix acceleration
- **Disaggregated architecture** — storage and compute are separate

### What It's Designed For

From hydradb.com:

> Graphs work better for storing user preferences, past interactions, and agent traces. HydraDB connects your context, builds a structured graph, and delivers the exact context agents need.

> Purpose-Built To Deliver Precise Context & Observability Into Why Agents Act The Way They Do.

**It's the agent memory/context layer, not the transactional ledger.**

---

## Architecture

```text
                 S3-Compatible Object Store
                 (durable source of truth)
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
          SlateDB      CSC Index   Coordination
          WAL+SSTs     (immutable) (leases, heartbeats)
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
  RAM       SSD/NVMe   Object Store
  (cache)   (cache)    (durable)
```

- **Data nodes** serve queries and canonical mutations
- **Indexers** build immutable traversal indexes in background
- Both keep only disposable state locally
- Object storage is the only durable copy

---

## OpenCypher Subset

HydraDB supports a **deliberate subset** of OpenCypher:

| Feature | Supported |
|---------|-----------|
| MATCH | Yes, one-hop path patterns |
| WHERE | Yes, boolean property comparisons |
| RETURN | Yes, `binding.property` or `count(*)` only |
| CREATE | Yes, relationship paths only |
| MERGE | Yes, matched on id |
| SET | Yes, after MATCH |
| DELETE | Yes, after MATCH |
| UNWIND | Yes, batch form |
| UNION | Yes for reads |
| CALL algo.* | Yes, 3 native procedures |

**NOT supported:** `RETURN *`, `IN`, `IS NULL`, `CREATE UNIQUE`, multi-hop MERGE, `labels()` function.

---

## Why Local Docker Doesn't Fully Work

The local Docker instance uses **local filesystem** as object store. But SlateDB's `PutMode::Update` is not implemented for `LocalFileSystem`. This means:

- **Reads work** — MATCH queries succeed
- **Writes partially work** — CREATE relationships succeed, but MERGE nodes fail
- **The graph is degraded** — not fully functional for writes

To work properly, HydraDB needs:
- **S3-compatible storage** (MinIO, Cloudflare R2, AWS S3)
- Or **R2** (which we already have credentials for)

---

## How It Fits Our Architecture

```
SQLite Ledger        = canonical record of what happened (events)
HydraDB              = derived graph projection (relationships, experience)
Git                  = canonical code/config lineage
ArtifactStore        = content-addressed immutable bytes
```

**The ledger is the source of truth. HydraDB is a rebuildable projection.**

This is explicitly stated in the private-lab architecture:

> If deleting Hydra or Hindsight destroys unique knowledge, the architecture is wrong.

So:
1. **SQLite** handles all transactional writes (our kernel)
2. **HydraDB** handles graph queries and relationship traversal (when S3-backed)
3. We can rebuild HydraDB from SQLite events at any time

---

## What We Can Do Now

| Capability | Status |
|-----------|--------|
| SQLite ledger (append, hash chain, verify) | ✓ Working |
| HydraDB reads (MATCH queries) | ✓ Working |
| HydraDB writes (MERGE, CREATE) | ✗ Needs S3 backend |
| HydraDB graph traversal | ✗ Needs S3 backend |
| Private-lab contracts (41 types) | ✓ Working |
| CompanyDay orchestration | ✓ Built in kernel.py |

---

## To Make HydraDB Fully Working

Option 1: **Point Docker at R2** (we have credentials)
```bash
docker rm hydradb
docker run -d --name hydradb \
  -p 7687:7687 -p 8443:8443 -p 9090:9090 \
  -e HYDRADB_OBJECT_STORE=s3 \
  -e AWS_ACCESS_KEY_ID=2a8d61c9ed22f5899b8507435a794f5d \
  -e AWS_SECRET_ACCESS_KEY=e673672255567cc054e43479fcee0030862fe998e3bc8d1c447b91503c5c729d \
  -e AWS_ENDPOINT_URL=https://954612afb5a97bb15dddcdc70176813d.r2.cloudflarestorage.com \
  ghcr.io/hydra-db/hydradb:latest
```

Option 2: **Use MinIO locally** (S3-compatible)

Option 3: **Defer HydraDB** — SQLite handles everything for now, HydraDB added when graph traversal is needed.
