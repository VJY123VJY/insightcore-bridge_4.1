from fastapi import FastAPI
from app.startup_checks import startup_check
from app.gateway import handle_request

app = FastAPI()

@app.on_event("startup")
def on_startup():
    startup_check()
    print("InsightBridge v4.1 started (FAIL-CLOSED MODE)")

@app.post("/gateway")
def gateway(token: str, request_id: str, actor_key: str):
    return handle_request(token, request_id, actor_key)
