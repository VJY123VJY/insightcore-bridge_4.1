from app.rate_limiter import check_rate
from app.scoring import update_score

def decide(actor_key):
    if not check_rate(actor_key):
        update_score(actor_key, -5)
        return "rejected"

    update_score(actor_key, +1)
    return "accepted"
