from datastore.db import get_db
import os

def startup_check():
    db = get_db()
    if not db:
        raise SystemExit("FAIL CLOSED: DB unavailable")

    # Initialize Schema
    migration_path = os.path.join(os.path.dirname(__file__), "../datastore/migrations.sql")
    with open(migration_path, "r") as f:
        db.executescript(f.read())
