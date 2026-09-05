# HydraDB Recovery — Bounded Repair, Then Stop

**Date:** 5 September 2026

---

## The Situation

Multiple independent faults compound into "Hydra is haunted":

- `qdw-workbench` runs `ghcr.io/hydra-db/hydradb:latest` — semantics change without code change
- QDW client written around obsolete assumptions (MERGE/MATCH+SET don't work — they do now)
- `_SELF` hack creates two physical nodes with same ID, only deletes edge
- Helpers create fresh copies for every relationship — multi-hop traversal broken
- Read query `HAS_VERSION` backwards
- `get_pool_win_rate()` uses undirected relationship (HydraDB rejects this)
- `HydraProjector.rebuild()` can append new ledger events while replaying
- `LabController` bypasses ledger, writes directly to Hydra
- `clear_all()` stale label list
- Integration tests only assert counts `>= 1`

**Plus:** local filesystem backend + `--restart unless-stopped` = reads work but writes fail silently.

## The Invariant

```
Ledger + artifacts + Git = canonical
HydraDB = disposable derived projection
```

## Emergency Unblock

```bash
cd /root/private-lab
./scripts/hydradb-setup.sh stop
docker rm hydradb 2>/dev/null || true
mv /root/hydradb-data/store "/root/hydradb-data/store.bad.$(date +%s)" 2>/dev/null || true
mkdir -p /root/hydradb-data/store /root/hydradb-data/cache
./scripts/hydradb-setup.sh start
python scripts/hydradb-capabilities.py
```

## Stop Condition

```
[ ] Hydra image pinned
[ ] credential rotated
[ ] capability probe passes
[ ] no _SELF production writes
[ ] no endpoint ID parameter collisions
[ ] one physical node per logical entity
[ ] directed topology queries pass
[ ] multi-hop Finding→Experiment→Studio works
[ ] projector cannot mutate ledger
[ ] rebuild twice gives identical graph
[ ] clear_projection removes all QDW graph state
[ ] non-QDW sentinel survives clear
[ ] controller has one injected ledger
[ ] controller does not write canonical facts directly to Hydra
[ ] Hydra disabled mode works
[ ] Dogcasso does not depend on Hydra
```

## Then Freeze

No new graph ontology, vector retrieval, GraphRAG, temporal algorithms, agent memory, dashboards.

Return to: DOGCASSO → OPS → BOOK → Etsy live experiment.
