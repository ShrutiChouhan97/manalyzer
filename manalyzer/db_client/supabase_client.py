from __future__ import annotations
from supabase import Client, create_client
from manalyzer.config import get_db_config


_supabase_client = None

def get_db_client() -> Client:
    global _supabase_client

    if _supabase_client is None:
        config = get_db_config()
        _supabase_client = create_client(config["supabase_url"], config["supabase_key"])

    return _supabase_client