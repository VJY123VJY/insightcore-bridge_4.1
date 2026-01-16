from datastore.db import get_db

def check_rate(actor_key):
    db = get_db()
    if not db:
        raise RuntimeError("DB down")  # FAIL-CLOSED

    cursor = db.execute(
        "SELECT count FROM rate_limits WHERE actor = ?",
        (actor_key,)
    )
    row = cursor.fetchone()

    if row and row[0] > 100:
        return False

    db.execute(
        """
        INSERT INTO rate_limits(actor, count)
        VALUES(?, 1)
        ON CONFLICT(actor)
        DO UPDATE SET count = count + 1
        """,
        (actor_key,)
    )
    db.commit()
    return True
