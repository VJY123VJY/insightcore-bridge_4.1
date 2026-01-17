# Insight Bridge v4.1

## Overview

Insight Bridge v4.1 is a **security-first API gateway and validation bridge** designed to safely process incoming requests using strict authentication, replay protection, and rate-limiting principles. The project focuses on **clean architecture, defensive design, and auditability**, making it suitable for demos, security reviews, and production hardening exercises.

This version emphasizes **repository hygiene**, **explicit security behavior**, and **predictable failure modes**.

---

## Key Features

* 🔐 **Token-based authentication** (environment-driven secrets)
* ♻️ **Replay attack protection** (request ID + time window)
* 🚦 **Rate limiting** to prevent abuse
* 🧱 **Clear request validation layer**
* 📜 **Structured logging for audits and demos**
* ❌ **Fail-fast startup if security prerequisites are missing**

---

## Project Structure

```
insight_bridge_v4_1/
│
├── app/
│   ├── main.py            # Application entry point
│   ├── gateway/           # Auth, validation, bridge logic
│   ├── models/            # Request / response schemas
│   └── utils/             # Helpers (time, hashing, logging)
│
├── datastore/
│   └── state_store.py     # Replay / token state handling
│
├── tests/                 # Unit and security tests
├── docs/                  # Design notes and demo artifacts
│
├── requirements.txt
├── SECURITY_NOTES.md
├── README.md
└── .gitignore
```

---

## Security Model (High Level)

1. **Secrets** are never hard-coded
2. Tokens are validated on every request
3. Each request must include a unique `request_id`
4. Replayed or expired requests are rejected
5. Rate limits are enforced before business logic

If any mandatory security dependency is missing, the application **refuses to start**.

---

## Environment Variables

The following environment variables are required:

```
INSIGHTBRIDGE_SECRET_KEY
INSIGHTBRIDGE_TOKEN_ISSUER
INSIGHTBRIDGE_REPLAY_WINDOW_SECONDS
```

> ⚠️ The service will fail at startup if these are not set.

---

## Installation

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Request Requirements

Each protected request must include:

* `Authorization` header (Bearer token)
* `request_id` (unique per request)
* Valid timestamp within replay window

Invalid, replayed, or rate-limited requests return appropriate HTTP error codes.

---

## Testing

```bash
pytest
```

Tests cover:

* Token validation
* Replay protection
* Rate limiting behavior
* Failure modes

---

## Demo Notes

* Only **one** screenshot or video is retained for demo purposes
* Logs are intentionally verbose for security inspection
* Replay and expired-token simulations are supported

---

## Design Philosophy

> *Assume the network is hostile.*

Insight Bridge is built with the assumption that:

* Requests can be replayed
* Tokens can leak
* Attackers will brute-force edge cases

Every layer exists to **fail safely and visibly**.

---

## Version

**Insight Bridge v4.1**

---

## License

This project is provided for educational and demonstration purposes.
