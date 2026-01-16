from app.replay_cache import ReplayCache

def test_replay_duplicate():
    assert ReplayCache.check_and_store("abc") is True
    assert ReplayCache.check_and_store("abc") is False
