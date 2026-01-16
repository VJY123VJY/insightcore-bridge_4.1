from app.scoring import update_score

def test_db_failure_rejects(monkeypatch):
    monkeypatch.setattr("datastore.db.get_db", lambda: None)

    try:
        update_score("actor1", 1)
        assert False
    except RuntimeError:
        assert True
