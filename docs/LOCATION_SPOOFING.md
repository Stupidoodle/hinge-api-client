# Location Spoofing (Free Travel Mode)

Hinge allows changing your location via profile PATCH — no premium subscription required.

## Endpoint

`PATCH /user/v2`

## Payload

```json
[{
  "profile": {
    "location": {
      "name": "Zürich",
      "latitude": 47.3769,
      "longitude": 8.5417
    }
  }
}]
```

**Response:** `202 {"genderId": 0}` (generic acknowledgment)

## Behavior

- Location change is **immediate** — new encounters will be from the target location
- No premium/subscription required
- No cooldown or rate limit observed
- The server geocodes the coordinates and fills in `metroArea`, `adminArea1Long`, etc.
- Works with any valid lat/lng worldwide (haven't tested restricted countries)

## Confirmed Working

| From | To | Coords | Result |
|---|---|---|---|
| St. Gallen, CH | Zürich, CH | 47.3769, 8.5417 | Instant change |
| Zürich, CH | St. Gallen, CH | 47.4158, 9.3610 | Instant restore |

## Comparison with Bumble

| Feature | Hinge | Bumble |
|---|---|---|
| Method | PATCH profile location | MSG 4 (update location) + MSG 309 (confirm city) |
| Premium required? | **No** | Yes (Travel Mode) |
| Cooldown? | None observed | Unknown |
| Geocoding | Server-side (fills metro area etc.) | Server confirms city name |

## Security Note

This is a significant finding — Hinge doesn't gate location changes behind premium, and there's no apparent rate limiting. A user could:
1. Swipe in multiple cities without moving
2. Appear local to users in any target city
3. Automate location rotation for maximum exposure

## Usage in Client

```python
async def teleport(client, name, lat, lng):
    payload = [{"profile": {"location": {"name": name, "latitude": lat, "longitude": lng}}}]
    r = await client.client.patch("/user/v2", json=payload, headers=client._get_default_headers())
    return r.status_code == 202
```
