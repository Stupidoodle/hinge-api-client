# Hinge API Security Findings

## Summary

Hinge's API has minimal server-side validation. The app relies heavily on client-side validation, which can be bypassed entirely via direct API calls.

## Critical Findings

### 1. Stored XSS in Profile Fields (CRITICAL)

**Endpoint:** `PATCH /user/v2`

The `firstName` field accepts arbitrary HTML/JavaScript:
```json
[{"profile": {"firstName": "<script>alert(1)</script>"}}]
```
**Response:** 202 (accepted)
**Stored value:** `<script>alert(1)</script>` — persisted in the database

**Impact:** If any Hinge admin dashboard, internal tool, web view, or partner integration renders profile names without HTML escaping, this is a stored XSS vulnerability affecting Hinge staff and potentially other users.

### 2. No Profile Field Validation (HIGH)

All profile fields accept any value without server-side validation:

| Field | Test | Accepted? |
|---|---|---|
| `height` | 300 (9'10") | Yes |
| `height` | 0 | Yes |
| `height` | -1 | Untested |
| `firstName` | Empty string | Yes |
| `firstName` | HTML/JS payload | Yes |
| `location` | Any lat/lng worldwide | Yes |
| Preference enums | Any integer | Yes |

### 3. Free Location Spoofing (HIGH)

**Endpoint:** `PATCH /user/v2` with `profile.location`

No premium subscription required. Any user can teleport to any location by sending lat/lng coordinates. See `LOCATION_SPOOFING.md` for details.

### 4. No Server-Side Rate Limiting (MEDIUM)

- No rate limit response headers (`X-RateLimit-*`, `Retry-After`)
- Rate limiting is client-side only (APK contains "NETWORK SPAM DETECTED" logic)
- Direct API calls bypass all client-side rate limiting
- Could enable automated profile scraping, mass swiping, etc.

### 5. No SSL Certificate Pinning (MEDIUM)

The Hinge iOS app has no SSL certificate pinning on `prod-api.hingeaws.net`. Any MITM proxy (mitmproxy, Charles, Burp) can intercept all API traffic without any bypass tools (Frida, Objection, etc.).

### 6. FaceTec Selfie Verification Keys Exposed (MEDIUM)

**Endpoint:** `GET /selfieverification/facetec/clientkeys`

Returns:
- `appKey` — FaceTec application key
- `sdkPublicEncryptionKey` — SDK public encryption key (with expiry date)
- `facescanPublicEncryptionKey` — RSA public key for face scan data

These keys could potentially be used to research the selfie verification process.

### 7. No Enum Validation (LOW)

**Endpoint:** `PATCH /preference/v2/selected`

All enum fields (religion, ethnicity, politics, etc.) accept any integer value. Sending `religion: [999]` returns 202. The server stores whatever the client sends.

### 8. User ID Leak in Response Headers (LOW)

Every authenticated API response includes:
```
x-user-id: 3852749922507949139
x-auth-state-id: standard_1
x-auth-state-permissions-checksum: cebd58b6f6c14e5e46c746ab17186645
```

### 9. Deleted Account Enumeration (LOW)

`GET /user/v3/public?ids={id}` returns `null` for deleted/banned accounts vs `[]` for never-existed IDs. This allows confirming whether a specific user ID was once active.

### 10. Auth Token Refresh Kills Session (INFO)

`GET /auth/refresh` immediately invalidates the current token and returns a new one. If the client fails to save the new token (network error, crash), the user is locked out and must re-authenticate via SMS OTP.

## Recommendations for Hinge

1. **Sanitize all profile text fields** — strip HTML, limit character sets
2. **Validate profile numeric fields** — enforce height range 92-214 (from their own config)
3. **Add server-side rate limiting** — don't rely on client-side enforcement
4. **Implement SSL certificate pinning** — at minimum for auth endpoints
5. **Gate location changes behind verification** — require GPS confirmation or premium
6. **Validate enum values server-side** — reject values not in the config
7. **Don't expose FaceTec keys** — require a verification session before returning crypto keys

### 11. Fresh Start Has No Confirmation (HIGH)

**Endpoint:** `POST /freshstart`

Sending an empty JSON body `{}` immediately triggers an algorithm reset. No confirmation payload, no "are you sure" field, no undo. The `eligible` flag flips to `false` after use.

**Impact:** Any app or script with a valid Bearer token can silently reset a user's dating algorithm. Fresh Start is supposed to be a deliberate, one-time decision.

### 12. Offer Activation Without Purchase (MEDIUM)

**Endpoint:** `PUT /offers/activate`

Sending `{"offerId": "boost1-50off"}` returns 200 with a 1-hour activation window. The server doesn't verify the offer was presented through the UI flow or that the user is eligible. The offer doesn't grant free product — it activates a discounted purchase window — but the lack of validation means any offer ID can be activated on demand.

### 13. pHash Leak on Other Users' Photos (MEDIUM)

**Endpoint:** `GET /content/v2/public?ids=`

Returns perceptual hash (`pHash`) values for other users' photos. These 64-bit hashes can be used for:
- Cross-platform de-anonymization (match photos across Tinder, Bumble, etc.)
- Reverse image search correlation
- Catfish detection (same pHash = same photo)

Interestingly, `GET /user/v2/public?ids=` does NOT return pHash — only the content endpoint leaks it.

### 14. reCAPTCHA Not Enforced (MEDIUM)

The full SMS auth flow (initiate + submit OTP + email 2FA) works without any reCAPTCHA token. The `NO_RECAPTCHA` fallback string from the APK is accepted/ignored on all tested endpoints. This enables:
- Automated account creation at scale
- Programmatic auth without CAPTCHA solving

### 15. Attestation Endpoint Returns 410 Gone (LOW)

`POST /attestation/v1/android/verify` returns 410 for all payloads including `clientError` variants. The service appears deprecated/disabled. Device integrity is not verified.

## Testing Notes

- All findings confirmed on live API with authenticated session
- Profile mutations (height, name, location) were restored; birthday change was irreversible (one-time)
- Fresh Start was accidentally triggered (algorithm reset, profile preserved)
- No likes were consumed during testing
- No other users were affected
