from app.rate_limiter import check_rate

def test_rate_limit():
    for _ in range(100):
        assert check_rate("actor_restart") is True
