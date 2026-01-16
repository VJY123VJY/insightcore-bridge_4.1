from app.decision_engine import decide
from app.telemetry import log_event
from app.replay_cache import ReplayCache

def handle_request(token, request_id, actor_key):
    # Replay protection
    if not ReplayCache.check_and_store(request_id):
        log_event("replay_detected", {"request_id": request_id})
        return {"status": "rejected"}

    decision = decide(actor_key)
    log_event("decision_made", {"decision": decision})
    return {"status": decision}
