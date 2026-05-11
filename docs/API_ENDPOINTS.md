# Hinge API Endpoints

Reverse-engineered endpoint map. Base URL: `https://prod-api.hingeaws.net`

## Auth

| Method | Path | Purpose | Status |
|---|---|---|---|
| POST | `/identity/install` | Register device (409 = already registered, OK) | Working |
| POST | `/auth/sms/v2/initiate` | Send SMS OTP | Working |
| POST | `/auth/sms/v2` | Submit OTP → get Bearer token (412 = email 2FA required) | Working |
| POST | `/auth/device/validate` | Submit email 2FA code | Working |
| POST | `/message/authenticate` | Get Sendbird JWT for chat | Working |
| GET | `/auth/refresh` | Refresh Bearer token without re-auth (201 = new token) | **NEW** — Working |
| GET | `/message/status` | Sendbird health check | **NEW** — Returns `{"status": "ok"}` |

**⚠️ Auth Refresh:** `GET /auth/refresh` returns a fresh `{identityId, token, expires}` with 201 status (60-day expiry). **Immediately invalidates the old token.** You MUST update your Bearer token in-place and regenerate headers before making any subsequent request. If you keep using stale headers after calling this, every call will 401. Hinge rate-limits SMS OTP aggressively (24h lockout), so don't burn sessions.

## Recommendations & Rating

| Method | Path | Purpose | Status |
|---|---|---|---|
| POST | `/rec/v2` | Get recommendation feed (multiple origins) | Working |
| GET | `/standouts` | Get standouts feed (flat list) | **NEW** — Working |
| GET | `/standouts/v2` | Standouts split into `free[]` and `paid[]` arrays | **NEW** — Working |
| GET | `/standouts/v3` | Same as `/standouts` (flat list) | **NEW** — Working |
| POST | `/rate/v2/initiate` | Like/skip/note a profile | Skip works, like broken |
| GET | `/user/repeat` | Recycle previously seen profiles | Working |

### Recommendation Feed Origins

POST `/rec/v2` returns multiple feeds with different origins:

| Origin | Description |
|---|---|
| `compatibles` | Main recommendation feed (20 subjects typically) |
| `active_lately` | Recently active users (may be empty) |
| `nearby` | Geographically close users (may be empty) |
| `new_here` | New users on the platform (may be empty) |

### Standouts Response Structure
```json
{
  "status": "VALID",
  "expiration": "2026-03-25T03:00:00Z",
  "standouts": [
    {
      "subjectId": "...",
      "ratingToken": "...(JWE)...",
      "content": {
        "photo": {
          "url": "https://media.hingenexus.com/image/upload/...",
          "boundingBox": {"bottomRight": {"x": 1, "y": 1}, "topLeft": {}},
          "contentId": "uuid",
          "promptId": "..." // optional
        }
      }
    }
  ]
}
```

## User Profiles

| Method | Path | Purpose | Status |
|---|---|---|---|
| GET | `/user/v2` | Own profile (FULL — 66 profile fields, inline photos/answers) | **NEW** — Working |
| GET | `/user/v3` | Own profile (39 profile fields, wrapped objects) | Working |
| PATCH | `/user/v2` | Update own profile | Working |
| GET | `/user/v2/public?ids=` | Other users' profiles (FULL — inline photos/answers) | **NEW** — Working |
| GET | `/user/v3/public?ids=` | Other users' profiles (subset) | Working |

### `/user/v2` vs `/user/v3` Schema Comparison

**v2 top-level keys (13):** `identityId`, `created`, `registered`, `completedScreens`, `notifications`, `modified`, `experience`, `source`, `campaign`, `isPaused`, `isWhatWorksSub`, `isLastActiveOptIn`, `profile`

**v3 top-level keys (7):** `userId`, `created`, `registered`, `modified`, `paused`, `lastActiveOptIn`, `profile`

**v2 profile fields (66):** All of v3 plus:
- `answers[]` — prompt answers with AI feedback (evaluation, detail, feedbackToken)
- `photos[]` — full photo objects with CDN URLs, pHash, bounding boxes, video URLs
- `appleAuthed` — whether account uses Apple Sign-In
- `completed` — profile completion status
- `didJustJoin` — new user flag
- `lastActiveStatus` — human-readable ("Active now")
- `lastActiveStatusId` — numeric (1=active now, 2=recently active)
- `*Visible` flags (19 total) — per-field visibility toggles:
  `childrenVisible`, `datingIntentionVisible`, `drinkingVisible`, `drugsVisible`, `educationsVisible`, `ethnicitiesVisible`, `familyPlansVisible`, `genderIdentityVisible`, `hometownsVisible`, `jobTitleVisible`, `languagesSpokenVisible`, `marijuanaVisible`, `petsVisible`, `politicsVisible`, `pronounsVisible`, `relationshipTypesVisible`, `religionsVisible`, `sexualOrientationsVisible`, `smokingVisible`, `worksVisible`, `zodiacVisible`

**v3 has but v2 doesn't:** `ethnicitiesText`, `firstCompletedDate`, `genderIdentityId`, `relationshipTypeIds`, `zodiac`

### Experience Field (Feature Flags)

Format: `KEY1-VALUE:KEY2-VALUE:...` (colon-separated key-value pairs)

Example: `NST-C:PHS-T:RT-T:SP1-T:TP-T:VPU-T:VX-T`

Unknown what each flag means — likely onboarding/feature completion states.

### Other User Profile Fields (v2/public)

Public profiles return a subset (no email, phone, visibility flags):
- `identityId`, `profile.age`, `profile.firstName`, `profile.lastName`
- `profile.genderId` (0=men, 1=women, 3=non-binary)
- `profile.height`, `profile.hometown`, `profile.jobTitle`, `profile.works`
- `profile.location.name`
- `profile.lastActiveStatus`, `profile.lastActiveStatusId`
- `profile.selfieVerified`
- `profile.didJustJoin`
- `profile.answers[]` with `contentId`, `position`, `questionId`, `type`, `response`
- `profile.photos[]` with `cdnId`, `contentId`, `source`, `sourceId`, `boundingBox`, `url`, `width`, `height`, `pHash`, `videos[]`
- Enum fields: `children`, `datingIntention`, `drinking`, `drugs`, `educations`, `ethnicities`, `familyPlans`, `languagesSpoken`, `marijuana`, `politics`, `pronouns`, `relationshipTypes`, `religions`, `sexualOrientations`, `smoking`

## Content

| Method | Path | Purpose | Status |
|---|---|---|---|
| GET | `/content/v1` | Own content (prompt polls only) | **NEW** — Working |
| GET | `/content/v2` | Own content (photos + answers) | Working |
| GET | `/content/v2/public?ids=` | Other users' content | Working |
| PUT | `/content/v1/answers` | Update own prompt answers | Working |

### Content v2 Public Response
```json
{
  "userId": "...",
  "content": {
    "photos": [...],  // PhotoContent objects with pHash, selfieVerified
    "answers": [...]   // AnswerContent objects
  }
}
```

## Preferences

| Method | Path | Purpose | Status |
|---|---|---|---|
| GET | `/preference/v2/selected` | Get preferences (dealbreakers, ranges, filters) | Working |
| PATCH | `/preference/v2/selected` | Update preferences (accepts ANY int values — no server-side enum validation!) | Working |

### Preference Response Structure
```json
{
  "children": [-1],          // -1 = open to all
  "datingIntentions": [-1],
  "dealbreakers": {
    "children": false,
    "maxDistance": false,
    "genderedAge": {"0": false, "1": true, "3": false},
    "genderedHeight": {"0": false, "1": false, "3": false},
    ...
  },
  "drinking": [-1],
  "ethnicities": [3, 7, 10],  // specific values = filtered
  "genderPreferences": [1],   // 0=men, 1=women, 3=non-binary
  "genderPreferenceId": 1,
  "maxDistance": 100,
  "genderedAgeRanges": {
    "0": {"min": 19, "max": 29},
    "1": {"min": 19, "max": 29},
    "3": {"min": 19, "max": 29}
  },
  "genderedHeightRanges": {
    "0": {"min": 92, "max": 214},
    "1": {"min": 92, "max": 214},
    "3": {"min": 92, "max": 214}
  },
  "updated": "2026-03-14T16:23:55Z"
}
```

**Note:** Gender keys in gendered ranges are `"0"` (men), `"1"` (women), `"3"` (non-binary).

## Prompts

| Method | Path | Purpose | Status |
|---|---|---|---|
| POST | `/prompts` | Get all prompt templates (420 prompts, 14 categories, 6 content types) | Working |

### Prompt Categories (14)
| Slug | Name |
|---|---|
| `video-first` | Video-first |
| `about-me` | About me |
| `my-type` | My type |
| `recommended` | Recommended |
| `popular` | Popular |
| `getting-personal` | Getting personal |
| `storytime` | Story time |
| `self-care` | Self-care |
| `your-world` | Your World |
| `lets-chat-about` | Let's chat about |
| `poll` | Poll |
| `date-vibes` | Date vibes |
| `lgbtq` | LGBTQIA+ |
| `take-the-mic` | Voice-first |

### Content Types (6)
| Type | Count |
|---|---|
| `text` | 287 |
| `video` | 294 |
| `voice` | 276 |
| `poll` | 199 |
| `media` | 92 |
| `idea` | 1 |

## Limits & Balance

| Method | Path | Purpose | Status |
|---|---|---|---|
| GET | `/likelimit` | Daily likes + superlikes remaining | Working |
| GET | `/boost/status` | Boost status | **NEW** — Returns `{"status": "ok"}` |
| GET | `/boost` | Boost info | **NEW** — Returns `{}` (empty on free) |

### Like Limit Response
```json
{
  "likesLeft": 7,
  "superlikesLeft": 1,
  "freeSuperLikesLeft": null,
  "freeSuperLikeExpiration": null
}
```

## Moderation

| Method | Path | Purpose | Status |
|---|---|---|---|
| POST | `/flag/textreview` | Pre-flight text moderation → returns `hcmRunId` | Working |

### AI Prompt Feedback

The server provides AI-generated feedback on prompt answers (visible in `/user/v2` own profile):
```json
{
  "feedback": {
    "evaluation": "MEDIUM",  // quality rating
    "detail": "You've made a sweet connection...",
    "feedbackToken": "...(JWT)..."
  }
}
```

## System

| Method | Path | Purpose | Status |
|---|---|---|---|
| GET | `/status` | Health check (empty 200) | **NEW** |
| GET | `/identity` | Identity info (405 Method Not Allowed) | **NEW** |

## Server-Side Enum Validation

**CRITICAL FINDING:** The preference PATCH endpoint accepts ANY integer values for enum fields — there is NO server-side validation. Sending `religion: [999]` returns 202 just like `religion: [2]`. This means:
- Enum values can only be discovered from the iOS/Android app binary
- The server trusts the client completely for enum value validation
- This is a potential data integrity issue

## NOT Found (404)

These endpoints do NOT exist:
- `/matches`, `/conversations`, `/inbox` — chat is entirely on Sendbird
- `/likes/received`, `/likes/sent`, `/who-liked-me`, `/likers` — no beeline equivalent
- `/visitors`, `/views`, `/profile/views` — no visitor tracking
- `/settings`, `/config`, `/enums`, `/metadata` — no server-side config
- `/subscription`, `/payment`, `/billing` — no billing endpoints
- `/analytics`, `/stats`, `/insights` — no self-analytics
- `/notifications` — not as endpoint (boolean flag in `/user/v2` response)
- `/location` — part of profile update, not standalone
- `/discover`, `/feed`, `/home`, `/daily` — not found
- `/report`, `/block`, `/unmatch` — not found as GET or POST (may use different patterns)
- `/openapi.json`, `/swagger`, `/docs` — no API documentation exposed

## CDN

- Photos: `https://media.hingenexus.com/image/upload/{cdnId}.jpg`
- Videos: `https://media.hingenexus.com/video/upload/f_mp4,w_720,c_limit/{cdnId}.mp4`
- Video thumbnails: `https://media.hingenexus.com/video/upload/so_0p/{cdnId}.jpeg`

Uses Cloudinary under the hood (image/upload URL pattern).

## Chat (Sendbird)

Hinge uses Sendbird as a 3rd-party chat service. No REST chat endpoints on `prod-api.hingeaws.net`.

- App ID: `3CDAD91C-1E0D-4A0D-BBEE-9671988BF9E9`
- API: `https://api-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9.sendbird.com`
- WebSocket: `wss://ws-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9.sendbird.com`

### Chat Auth Flow
1. POST `/message/authenticate` with `{"refresh": false}` → Sendbird JWT
2. WebSocket connect with `SENDBIRD-WS-TOKEN` header + `user_id={identity_id}&ai={app_id}`
3. Receive `LOGI{...}` → extract `key` (session key)

## Headers Required

```
X-Device-Platform: iOS
User-Agent: Hinge/{build_number} CFNetwork/3857.100.1 Darwin/25.0.0
X-Device-Model-Code: iPhone16,1
X-Device-Model: unknown
X-Device-Region: FR (or CH, US, etc.)
X-Session-Id: {uuid}
X-Device-Id: {uuid}
X-Install-Id: {uuid}
X-App-Version: 9.82.0
X-Build-Number: 11616
X-OS-Version: 26.0
Authorization: Bearer {hinge_token}
Content-Type: application/json
Accept: */*
Accept-Language: en-GB
Accept-Encoding: gzip, deflate, br
```

## Key Differences from Bumble API

| Aspect | Hinge | Bumble |
|---|---|---|
| Protocol | REST (JSON) | Custom RPC (protobuf-like JSON) |
| Auth | Bearer token (SMS OTP) | Session cookies + X-Pingback (MD5 hash) |
| SSL Pinning | None | None (web API) |
| Chat | Sendbird (3rd-party WebSocket) | Comet SSE (in-house) |
| Endpoints | Clean REST paths with versioning | Single `mwebapi.phtml` with message types |
| Rate limiting | 8 likes/day (free), 1 superlike | No visible limit |
| Standouts | Separate `/standouts` endpoint | No equivalent (Spotlight is boost) |
| Enum validation | None (server accepts any int) | Unknown |
| Profile versions | v2 (full) vs v3 (clean) | Single model with projection fields |
| Photo CDN | Cloudinary (`media.hingenexus.com`) | Custom CDN |
