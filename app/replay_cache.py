import time

class ReplayCache:
    _cache = {}
    MAX_SIZE = 10000
    TTL = 300  # seconds

    @classmethod
    def check_and_store(cls, rid):
        now = time.time()

        # TTL eviction
        cls._cache = {
            k: v for k, v in cls._cache.items()
            if now - v < cls.TTL
        }

        if rid in cls._cache:
            return False

        if len(cls._cache) >= cls.MAX_SIZE:
            return False  # FAIL CLOSED

        cls._cache[rid] = now
        return True
