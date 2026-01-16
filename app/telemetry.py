import time

def log_event(event: str, data: dict = None):
    entry = {
        "event": event,
        "timestamp": int(time.time() * 1000)
    }
    if data:
        entry.update(data)

    print(entry)
