from app.scoring import update_score
from datastore.db import get_db

def test_score_persistence():
    update_score("actor1", 5)
    db = get_db()
    row = db.execute(
        "SELECT score FROM scores WHERE actor='actor1'"
    ).fetchone()
    assert row[0] >= 5
