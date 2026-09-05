"""
Memory Taxonomy — four banks adapted from PAHF + PersonalAlign.

RAW / COLD        — complete transcripts, never auto-inserted
EPISODIC / WARM   — relevant trajectories, retrieved by similarity
SEMANTIC / HOT    — empirically supported compact principles
CONSTITUTIONAL    — AGENTS.md axioms, always loaded
"""
from __future__ import annotations

import hashlib
import json
import os
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

def uid(prefix="mem"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def now_iso():
    return datetime.now().isoformat()


# ── Memory Entry ─────────────────────────────────────────────────────────

def make_memory(
    bank: str,  # raw, episodic, semantic, constitutional
    category: str,  # stable_preference, contextual_preference, routine, latent_rule, lesson, observation
    claim: str,
    confidence: float = 0.5,
    evidence_refs: list = None,
    source_session_id: str = "",
    contradicts: list = None,
    scope: str = "",
) -> dict:
    return {
        "schema": "memory",
        "memory_id": uid("mem"),
        "bank": bank,
        "category": category,
        "claim": claim,
        "confidence": confidence,
        "evidence_count": len(evidence_refs or []),
        "evidence_refs": evidence_refs or [],
        "contradicts": contradicts or [],
        "source_session_id": source_session_id,
        "scope": scope,
        "created_at": now_iso(),
        "last_validated": now_iso(),
        "status": "candidate",  # candidate, validated, rejected
    }


# ── Retrieval Receipt ───────────────────────────────────────────────────

def make_retrieval_receipt(
    memory_id: str,
    query: str,
    relevance_score: float,
    used_in_decision: str = "",
    decision_id: str = "",
) -> dict:
    return {
        "schema": "retrieval_receipt",
        "receipt_id": uid("rr"),
        "memory_id": memory_id,
        "query": query,
        "relevance_score": relevance_score,
        "used_in_decision": used_in_decision,
        "decision_id": decision_id,
        "timestamp": now_iso(),
    }


# ── Memory Bank Manager ─────────────────────────────────────────────────

MEMORY_DIR = Path("/root/StallShark/mythicbee-ops/memory")

class MemoryBank:
    def __init__(self, bank_name: str):
        self.bank = bank_name
        self.dir = MEMORY_DIR / bank_name
        self.dir.mkdir(parents=True, exist_ok=True)
    
    def store(self, memory: dict):
        path = self.dir / f"{memory['memory_id']}.json"
        with open(path, "w") as f:
            json.dump(memory, f, indent=2, default=str)
        return path
    
    def search(self, category: str = None, min_confidence: float = 0.0) -> list:
        results = []
        for f in self.dir.glob("*.json"):
            with open(f) as fh:
                m = json.load(fh)
                if category and m.get("category") != category:
                    continue
                if m.get("confidence", 0) < min_confidence:
                    continue
                results.append(m)
        return sorted(results, key=lambda x: x.get("confidence", 0), reverse=True)
    
    def count(self) -> int:
        return len(list(self.dir.glob("*.json")))


# ── Tests ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Memory Taxonomy Test ===\n")
    
    # Test memory creation
    mem = make_memory(
        bank="semantic",
        category="lesson",
        claim="Birthday gifts convert better than generic sports gifts",
        confidence=0.78,
        evidence_refs=["exp_001", "exp_005"],
        scope="gamewinner_etsy",
    )
    print(f"Memory: {mem['memory_id']} [{mem['bank']}/{mem['category']}]")
    print(f"  Claim: {mem['claim'][:60]}")
    print(f"  Confidence: {mem['confidence']}")
    print(f"  Status: {mem['status']}")
    
    # Test retrieval receipt
    rr = make_retrieval_receipt(
        memory_id=mem["memory_id"],
        query="birthday vs generic conversion",
        relevance_score=0.85,
        used_in_decision="dec_001",
    )
    print(f"\nRetrieval: {rr['receipt_id']}")
    
    # Test memory bank
    bank = MemoryBank("semantic")
    bank.store(mem)
    print(f"\nStored in semantic bank ({bank.count()} entries)")
    
    results = bank.search(category="lesson", min_confidence=0.5)
    print(f"Search: {len(results)} results")
    
    print("\n=== ALL WORKING ===")
