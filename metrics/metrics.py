from app.replay_cache import ReplayCache

def metrics():
    return {
        "replay_cache_size": len(ReplayCache._cache)
    }
