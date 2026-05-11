# Live API Discovery Session — 2026-03-24

Results from probing the Hinge API with a live authenticated session.

## Endpoint Test Results

### Working Endpoints (45+ confirmed)

#### Auth & Session
| Method | Path | Response |
|---|---|---|
| GET | `/auth/refresh` | 201 — new token (⚠️ kills old token immediately!) |
| GET | `/auth/logout` | 200 — kills session (⚠️ DO NOT CALL) |
| GET | `/authz/permissions` | 200 — 51 permission strings |
| GET | `/login/config` | 200 — auth methods: apple, google, sms v2 |
| GET | `/message/status` | 200 — `{"status": "ok"}` |
| GET | `/status` | 200 — empty (health check) |

#### Recommendations & Discovery
| Method | Path | Response |
|---|---|---|
| POST | `/rec/v2` | 200 — 4 feed origins: compatibles (20), active_lately, nearby, new_here |
| GET | `/standouts` | 200 — 10 standouts (flat list) |
| GET | `/standouts/v2` | 200 — splits into `free[]` (10) and `paid[]` (0) |
| GET | `/standouts/v3` | 200 — same as /standouts |
| GET | `/like/v2` | 200 — "Likes You" with sorts: Recent, Your type, Last active, Nearby |
| GET | `/connection/v2` | 200 — match list (empty on this account) |
| GET | `/user/repeat` | 200 — recycles skipped profiles |

#### User Profiles
| Method | Path | Response |
|---|---|---|
| GET | `/user/v2` | 200 — own profile (66 fields, inline photos/answers/AI feedback) |
| GET | `/user/v3` | 200 — own profile (39 fields, cleaner schema) |
| GET | `/user/v2/public?ids=` | 200 — other profiles (full, with photos/answers) |
| GET | `/user/v3/public?ids=` | 200 — other profiles (subset) |
| POST | `/user/v3/public` | 200 — same as GET but POST variant |
| GET | `/user/v2/traits` | 200 — personality traits: about_me, interests, looking_for |
| GET | `/user/circle/progress` | 200 — Circle eligibility + 6 criteria |
| GET | `/user/export/status` | 200 — `{"status": "none"}` |

#### Content
| Method | Path | Response |
|---|---|---|
| GET | `/content/v1` | 200 — prompt polls |
| GET | `/content/v2` | 200 — photos + answers |
| GET | `/content/v2/public?ids=` | 200 — other users' content |
| POST | `/content/v2/public` | 200 — POST variant |
| GET | `/content/v1/settings` | 200 — smartPhoto + convoStarters opt-in |

#### Preferences & Config
| Method | Path | Response |
|---|---|---|
| GET | `/preference/v2/selected` | 200 — full preferences with dealbreakers |
| GET | `/config/v3` | 200 — **SERVER CONFIG** with all valid enum IDs! |
| GET | `/config/v3/preferences` | 200 — age/height/distance ranges |
| GET | `/config/safetyarticles` | 200 — safety article URLs |

#### Profile State
| Method | Path | Response |
|---|---|---|
| GET | `/profilestate/profile` | 200 — 100% complete (6 photos + 3 answers) |
| GET | `/profilestate/basics/missing` | 200 — `{"soloFacePhoto": false}` |
| GET | `/freshstart/eligible` | 200 — `{"eligible": true}` |

#### Store & Billing
| Method | Path | Response |
|---|---|---|
| GET | `/likelimit` | 200 — 7 likes, 1 superlike, 1 free superlike (expires 3/29) |
| GET | `/store/v2/account` | 200 — free account, never purchased |
| GET | `/store/v2/product` | 200 — subscription SKUs + boost pricing ($9.99-$39.99) |
| POST | `/store/v6/product` | 200 — consumables: boost, superboost, superlike (rose) |
| GET | `/store/boost` | 200 — `{"remaining": 0}` |
| GET | `/boost` | 200 — `{}` |
| GET | `/boost/status` | 200 — `{"status": "ok"}` |

#### Notifications
| Method | Path | Response |
|---|---|---|
| GET | `/notification/v1/settings` | 200 — push + email toggles |
| GET | `/notification/v1/inbox` | 200 — empty |
| GET | `/notification/v1/settings/chats` | 200 — `{"chatSettings": []}` |
| GET | `/inappnotifications/v1/views` | 200 — Liking + PromptFeedback views |

#### Moderation & Safety
| Method | Path | Response |
|---|---|---|
| GET | `/report/config` | 200 — full report reason tree (19 nodes) |
| GET | `/flag/config` | 200 — `{"areYouSureTimeoutMs": 500}` |
| GET | `/flag/settings` | 200 — harmful comment auto-filter ON |
| GET | `/flag/hiddenword` | 200 — empty token list |

#### Verification
| Method | Path | Response |
|---|---|---|
| GET | `/selfieverification/eligibility` | 200 — needs 1 verified photo |
| GET | `/selfieverification/facetec/session` | 200 — FaceTec session token |
| GET | `/selfieverification/facetec/clientkeys` | 200 — FaceTec app key + public encryption keys |

#### Social Features
| Method | Path | Response |
|---|---|---|
| GET | `/bpyk` | 200 — Block People You Know (empty) |
| GET | `/wemet/config` | 200 — "We Met" survey flow configuration |
| GET | `/wemet/surveystatus` | 200 — no surveys pending |
| GET | `/whatworks/v1/guides` | 200 — 8KB of dating guides/tips |
| GET | `/appeal` | 200 — Bryan's ban appeal (id: 2562833, status: closed, decision: accepted) |
| GET | `/connection/unmatchreporting/unmatches?limit=10` | 200 — empty unmatches, 30-day range |

#### Consent & Legal
| Method | Path | Response |
|---|---|---|
| GET | `/consent/user/blocking` | 200 — no blocking consent needed |
| GET | `/consent/user/message` | 200 — no consent needed |
| GET | `/statement/removedcontent` | 200 — no removed content |

#### Flows
| Method | Path | Response |
|---|---|---|
| POST | `/flow/onboarding` | 200 — full 35-screen onboarding flow (all completed) |
| POST | `/signal/v1` | 200 — integrity check token |

### 405 Method Not Allowed (exist but wrong HTTP method)
- `POST /standouts` — GET only
- `GET /content/v1/date_idea` — POST only
- `GET /flow` — POST only
- `GET /lsp/feedback` — POST only
- `GET /metric/v2` — POST only
- `GET /content/v1/photos` — PUT only
- `GET /rate/v1/initiate` — POST only

### 400 Bad Request (exist but need correct payload)
- `POST /user/v2/traits/evaluate` — needs correct trait format
- `POST /content/v1/answer/evaluate` — needs correct answer format
- `POST /cdn/token` — needs content type specification
- `GET /content/v1/tips` — might need query params
- `GET /boost/bystart` — needs start time param

### 433 Forbidden
- `GET /statement/copy` — forbidden for this user

### 500 Internal Server Error
- `GET /idverification/status` — server error (might be region-specific)

## Key Findings

### 1. "Likes You" Endpoint Found
`GET /like/v2` returns likes with 4 sort options and supports hidden likes. This is the beeline equivalent — no premium required to hit the endpoint (content may be gated).

### 2. Match List Without Sendbird
`GET /connection/v2` returns matches server-side. Don't need to go through Sendbird for the match list.

### 3. Server-Side Enum Config
`GET /config/v3` returns authoritative lists of all valid enum IDs:
- `vitals.children`, `vitals.ethnicities`, `vitals.familyPlans`
- `vices.drinking/drugs/marijuana/smoking`
- `virtues.religions`, `virtues.politics`, `virtues.educationAttained`, `virtues.datingIntentions`, `virtues.relationshipTypes`, `virtues.languagesSpoken` (144 languages!)

### 4. User Traits System
New `about_me`, `interests`, `looking_for` traits at `GET /user/v2/traits`. Separate from prompts — likely AI-generated personality summaries.

### 5. Circle Social Feature
`GET /user/circle/progress` shows eligibility criteria:
- selfie_verification (required)
- thoughtful_likes, responsive_to_likes, meaningful_chats, date_confirmation, intentional_browsing (optional, need 4 of 6)

### 6. Full Onboarding Flow
35 screens in order: communityEdu → fullName → email → emailVerification → birthday → pushNotifications → compatibilityEdu → profileLocation → pronouns → gender → sexualOrientations → orientation → relationshipType → datingIntention → profileHeight → profileEthnicities → children → family → hometown → workplace → jobTitle → school → educationLevel → profileReligions → politics → drinking → smoking → marijuana → drugs → privacyPreferences → storyEdu → ...

### 7. Store Pricing (Switzerland)
- **Boost:** 1 for $9.99, 3 for $26.99 (save 10%), 5 for $39.99 (save 20%)
- **Superlike (Rose):** 3, 12, or 50 packs
- **Superboost:** 1 pack
- **Hinge+ (tier1):** 1 week, 1 month, 3 months (recommended), 6 months
- **HingeX (tier2):** same intervals

### 8. FaceTec Keys Exposed
Selfie verification uses FaceTec SDK. The `appKey` and `sdkPublicEncryptionKey` are returned from the API — potential for selfie verification bypass research.

### 9. Ban Appeal Data
Bryan's previous ban appeal is visible: id 2562833, submitted appeal text, status closed, decision accepted.

### 10. No Server-Side Enum Validation
The preference PATCH endpoint accepts ANY integer for enum fields. Server trusts the client completely.

### 11. Gender Pool Switching
`genderPrefId` param in `/rec/v2` switches the recommendation pool:
- `0` (men): 20 subjects
- `1` (women): 20 subjects
- `2` (everyone): 20 subjects
- `3` (non-binary): 11 subjects (smaller pool)

### 12. Standouts v2 Free/Paid Split
`GET /standouts/v2` separates standouts into `free[]` (10 profiles) and `paid[]` (0 on free account). Premium users see additional standouts.

### 13. Server Infrastructure
- **Cloudflare** CDN + bot management (`__cf_bm` cookie)
- **Envoy** internal proxy (`x-envoy-upstream-service-time` header)
- **No CORS headers** — API designed for mobile only, not browser
- **No server-side rate limit headers** — rate limiting is client-side only
- **Region detection via IP**, not `X-Device-Region` header (header is ignored for routing)

### 14. Response Header Leaks
Every response includes:
- `x-user-id: {your_numeric_id}` — your identity in every response
- `x-auth-state-id: standard_1` — permission tier
- `x-auth-state-permissions-checksum` — permission state hash
- `x-hinge-region-request: CH` — detected country from IP

### 15. Deleted Account Returns `null`
`GET /user/v3/public?ids={deleted_user_id}` returns `null` (not 404). Can be used to check if an account was deleted/banned.

### 16. rec/v2 Strict Payload Validation
Adding any unknown fields (`limit`, `count`, `maxResults`, `feeds`) causes the endpoint to return empty feeds. The server validates the payload strictly.

### 17. Additional Working Endpoints (Second Sweep)
| Endpoint | Finding |
|---|---|
| `GET /auth/settings` | Auth providers linked: `{smsAuthed: true, appleAuthed: false, ...}` |
| `POST /flag/hiddenword/add` | Add words to hide from chat — working |
| `POST /flag/hiddenword/remove` | Remove hidden words — working |
| `PUT /user/v2/profile/email` | Update email — working (⚠️ actually changes it!) |
| `POST /codeval/email/resend` | Resend email verification — working |
| `POST /codeval/email/validate` | Validate email code — working |
| `POST /review/request` | Submit app review — 201 |
| `POST /metric/analytics/v1` | Submit analytics — 202 accepted |
| `POST /signal/v1` | Integrity check — returns ICG token |
| `POST /flow/onboarding` | Full 35-screen onboarding flow |
| `POST /wemet/survey` | Submit We Met survey — 200 |
| `PATCH /dlp/user` | DLP settings — 433 Forbidden |
| `POST /content/v1/date_idea` | Create date idea — 433 Forbidden |

### 18. Onboarding Flow (35 Screens)
Complete order: communityEdu → fullName → email → emailVerification → birthday → pushNotifications → compatibilityEdu → profileLocation → pronouns → gender → sexualOrientations → orientation → relationshipType → datingIntention → profileHeight → profileEthnicities → children → family → hometown → workplace → jobTitle → school → educationLevel → profileReligions → politics → drinking → smoking → marijuana → drugs → privacyPreferences → storyEdu → ... (35 total)

### 19. In-App Notification Tracking
Hinge tracks when you view specific UI elements:
- `Liking` — viewed 2026-03-14T16:18:19Z
- `PromptFeedback` — viewed 2026-03-24T17:17:23Z
- `Selfie` — viewed 2026-03-14T16:27:12Z

### 20. Server-Side Enum Config (`config/v3`)
The crown jewel — `GET /config/v3` returns authoritative enum ID lists:
- 56 gender identities, 3 gender identity groups
- 23 sexual orientations
- 30 pronouns (including -2 as special value)
- 144 languages
- 13 zodiac signs (1-12 + 0 for "prefer not to say")
- 6 pets (1-5 + 0)
- All vices/virtues/vitals with valid ID arrays
