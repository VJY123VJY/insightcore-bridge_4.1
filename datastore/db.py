import sqlite3

_DB = None

def get_db():
    global _DB
    try:
        if not _DB:
            _DB = sqlite3.connect("state.db", check_same_thread=False)
        return _DB
    except Exception:
        return None
