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


def add_relation(client: NotionBuilderClient, source_ds_id: str, prop_name: str,
                 target_ds_id: str, *, dual: bool = False) -> bool:
    """Add a relation property on source data source → target data source.

    Both ids are DATA SOURCE ids (2025-09-03 API). Idempotent: if the relation
    property already exists, it is left as-is. Returns True on success/exists.
    """
    if relation_exists(client, source_ds_id, prop_name):
        return True
    try:
        client.update_data_source(source_ds_id, properties={
            prop_name: db_create.relation(target_ds_id, dual=dual)
        })
        return True
    except Exception:
        return False


def relation_exists(client: NotionBuilderClient, ds_id: str, prop_name: str) -> bool:
    try:
        ds = client.retrieve_data_source(ds_id)
        prop = ds.get("properties", {}).get(prop_name)
        return bool(prop) and prop.get("type") == "relation"
    except Exception:
        return False
