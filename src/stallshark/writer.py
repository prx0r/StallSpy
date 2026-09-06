"""
CorpusWriter — single canonical write path for all records.

Strict validation → invariant checks → canonical serialization → hash → append.
"""
from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .schemas import Record, ValidationResult, ValidationStatus, validate_schema, validate_temporal

ROOT = Path("/root/StallShark")
LEDGER_DB = ROOT / "data" / "corpus_ledger.db"

class CorpusWriter:
    """Single canonical write path. No agent gets raw DB access."""

    def __init__(self, db_path: str = None):
        self.db_path = db_path or str(LEDGER_DB)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.conn = sqlite3.connect(self.db_path, timeout=10, check_same_thread=False)
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA busy_timeout=5000")
        self._init_db()

    def _init_db(self):
        self.conn.executescript("""
            CREATE TABLE IF NOT EXISTS canonical_records (
                record_id TEXT PRIMARY KEY,
                kind TEXT NOT NULL,
                schema_version TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                payload_sha256 TEXT NOT NULL,
                previous_hash TEXT NOT NULL,
                record_hash TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_kind ON canonical_records(kind);
            CREATE INDEX IF NOT EXISTS idx_day ON canonical_records(
                json_extract(payload_json, '$.company_day_id'));
        """)
        self.conn.commit()

    def append(self, record: Record) -> dict:
        """Append a record with full validation."""
        # Gate 1: Schema validation
        schema_result = validate_schema(record)
        if schema_result.status == ValidationStatus.FAIL:
            raise ValueError(f"Schema validation failed: {schema_result.details}")

        # Gate 3: Temporal validation
        temporal_result = validate_temporal(record)
        if temporal_result.status == ValidationStatus.FAIL:
            raise ValueError(f"Temporal validation failed: {temporal_result.details}")

        # Serialize
        payload = json.loads(record.model_dump_json())
        payload_json = json.dumps(payload, sort_keys=True)
        payload_hash = hashlib.sha256(payload_json.encode()).hexdigest()

        # Hash chain
        cur = self.conn.execute("SELECT record_hash FROM canonical_records ORDER BY rowid DESC LIMIT 1")
        prev = cur.fetchone()
        prev_hash = prev[0] if prev else "genesis"

        record_data = f"{record.id}{record.kind}{payload_json}{prev_hash}"
        record_hash = hashlib.sha256(record_data.encode()).hexdigest()

        # Append
        self.conn.execute(
            "INSERT INTO canonical_records VALUES (?,?,?,?,?,?,?,?)",
            (str(record.id), record.kind, record.schema_version,
             payload_json, payload_hash, prev_hash, record_hash,
             datetime.now(timezone.utc).isoformat())
        )
        self.conn.commit()

        return {
            "record_id": str(record.id),
            "kind": record.kind,
            "record_hash": record_hash,
            "validations": [schema_result.gate, temporal_result.gate],
        }

    def verify_chain(self) -> bool:
        """Verify hash chain integrity."""
        cur = self.conn.execute(
            "SELECT record_id, kind, payload_json, previous_hash, record_hash FROM canonical_records ORDER BY rowid"
        )
        prev = "genesis"
        for row in cur.fetchall():
            record_id, kind, payload_json, previous_hash, record_hash = row
            if previous_hash != prev:
                return False
            expected = hashlib.sha256(f"{record_id}{kind}{payload_json}{previous_hash}".encode()).hexdigest()
            if record_hash != expected:
                return False
            prev = record_hash
        return True

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM canonical_records").fetchone()[0]

    def get_by_kind(self, kind: str, limit: int = 100) -> list:
        cur = self.conn.execute(
            "SELECT payload_json FROM canonical_records WHERE kind=? ORDER BY rowid LIMIT ?",
            (kind, limit)
        )
        return [json.loads(row[0]) for row in cur.fetchall()]
