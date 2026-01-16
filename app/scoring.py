from datastore.db import get_db

def update_score(actor_key, delta):
    db = get_db()
    if not db:
        raise RuntimeError("DB unavailable")  # HARD FAIL

    db.execute(
        "INSERT INTO scores(actor, score) VALUES (?, ?) "
        "ON CONFLICT(actor) DO UPDATE SET score = score + ?",
        (actor_key, delta, delta)
    )
