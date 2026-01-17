# Security Notes

This document outlines the security assumptions and enforcement rules
used in this project. These rules are mandatory for correct operation.

---

## 1. Secret Management

All sensitive values (tokens, keys, secrets) are loaded **only from
environment variables**.

Examples:
- API secrets
- Signing keys
- Internal trust tokens

❌ Secrets are **never**:
- Hardcoded in source code
- Stored in config files
- Committed to the repository

---

## 2. Missing Secrets Behavior

If any required environment variable is missing at startup:

- The application **fails fast**
- Startup is aborted immediately
- No fallback or default values are used

This ensures the system never runs in a partially secure state.

---

## 3. Replay Protection Logic

Each request is validated using:
- A unique request ID
- A strict time-based replay window

Requests are rejected if:
- The request ID was already seen
- The timestamp is outside the allowed replay window

This prevents:
- Token replay attacks
- Delayed or duplicated requests
- Abuse via captured payloads

Replay state is tracked server-side and enforced before any business
logic executes.

---

## 4. Fail-Closed Principle

All security checks are **fail-closed**:
- Any validation error results in rejection
- No request proceeds on partial validation
- Trust is never assumed from the client

---

## Summary

Security is enforced at the gateway level.
If validation fails, execution stops.
No insecure defaults exist by design.
