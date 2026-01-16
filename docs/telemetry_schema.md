version: 1.0

fields:
- event_name: string
- timestamp: unix_ms
- decision: accepted | rejected
- replay_cache_size: number
- rate_limit_hits: number

rules:
- NO jwt
- NO actor ids
- NO secrets
