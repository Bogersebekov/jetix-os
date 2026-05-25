"""Cross-database relations — add a relation property to an existing DB.

A relation links rows of one database to rows of another. We add relations
AFTER both target databases exist (Phase 7), via databases.update with a new
relation property. Idempotent: if the property already exists, update is a
no-op on Notion's side.

STANDALONE / opt-in mandate: relations are additive links, never auto-merges.
A user of one layer alone is unaffected; relations only light up when both
layers are present.
"""

from __future__ import annotations

from typing import Optional

from . import db_create
from .client import NotionBuilderClient


def add_relation(client: NotionBuilderClient, source_db_id: str, prop_name: str,
                 target_db_id: str, *, dual: bool = False) -> bool:
    """Add (or reconcile) a relation property `prop_name` on source_db → target_db.

    Returns True on success, False on failure (logged by caller).
    """
    try:
        client.update_database(source_db_id, properties={
            prop_name: db_create.relation(target_db_id, dual=dual)
        })
        return True
    except Exception:
        return False


def relation_exists(client: NotionBuilderClient, db_id: str, prop_name: str) -> bool:
    try:
        db = client.retrieve_database(db_id)
        prop = db.get("properties", {}).get(prop_name)
        return bool(prop) and prop.get("type") == "relation"
    except Exception:
        return False
