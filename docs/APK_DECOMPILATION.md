# Hinge APK Decompilation Methodology

## Overview

Reverse engineering of the Hinge Android APK to extract enum values, API endpoints, and internal constants.

## Tools

- **apkeep** v0.18.0 — APK downloader from Google Play (Rust, installed via `cargo install apkeep`)
- **jadx** v1.5.5 — Dex to Java decompiler (installed via `brew install jadx`)

## Download

```bash
# Install tools
brew install jadx
cargo install apkeep  # requires rust toolchain

# Download APK from Google Play
apkeep -a co.hinge.app /tmp/
# Downloads as XAPK (split APK bundle): co.hinge.app.xapk (~46MB)

# Extract base APK from XAPK
mkdir /tmp/hinge-xapk
unzip /tmp/co.hinge.app.xapk -d /tmp/hinge-xapk/
# Contents:
#   co.hinge.app.apk       (39MB - base APK with all code)
#   config.armeabi_v7a.apk  (5MB - native libs)
#   config.mdpi.apk         (3MB - resources for mdpi)
#   manifest.json
#   icon.png
```

## Decompilation

```bash
# Decompile base APK (skip resources for speed)
jadx -d /tmp/hinge-decompiled /tmp/hinge-xapk/co.hinge.app.apk --no-res

# Result: ~20,956 classes, 93 decompilation errors (normal for R8-obfuscated code)
```

## App Structure

### Package: `co.hinge.*`

Non-obfuscated Hinge code. Feature-organized:

```
co.hinge/
├── app/                    # Application class, R.java (string resources)
├── api/models/products/    # Billing/product models (ProductsResponse, Consumables)
├── billing/models/network/ # Receipt, ProductsV6Request/Response
├── boost/ui/              # Boost feature UI
├── circle/impl/data/      # Circle social feature (CircleStore, CircleProgressResponse)
├── common/storage/db/     # Room database (Database_Impl — 62 tables)
├── content_takedown/      # Content removal/appeal system
├── core/serialization/    # JSON serialization (MetricsData)
├── design/                # UI components (BoostButton, RoundedImageView, etc.)
├── domain/
│   ├── entities/          # PendingRating (Block/Like/Note/Skip/Report)
│   ├── models/
│   │   ├── accounts/      # ApiProfile, ApiSubjectProfile, PreferencesRequest, Photo
│   │   ├── auth/          # Auth models (AddCredentials, ConflictDecision, SendBirdToken)
│   │   ├── boost/         # BoostActivateResponse, BoostCountResponse, BoostStatusResponse
│   │   ├── configs/       # VitalsConfig, GenderIdentityGroupsConfig, prompts/
│   │   ├── notifications/ # NotificationSettingsPayload
│   │   ├── profile/       # ProfileStatusResponse, MissingProfileStateBasicsResponse
│   │   ├── store/         # SubscriptionTier (One/Two), SubscriptionProvider, SubscriptionManagementPage
│   │   ├── subscription/  # SubscriptionPeriod
│   │   ├── subjects/      # StandoutsResponse
│   │   └── whatworks/     # WhatWorksGuide/Tip/Image
│   └── dto/               # ContentSettingsRequest, DateIdeasPromptRequest, HideRequest, etc.
├── edit_media/models/     # VideoTrimmer errors
├── editpreferences/       # Preference editing UI
├── features/profile/basics/
│   ├── virtues/           # Religion, Politics, EducationAttained, RelationshipType, DatingIntention
│   └── vitals/            # Ethnicities, FamilyPlans, Gender, SexualOrientations, Zodiac, Pets, Location, CovidVaccine
├── flowService/impl/      # Onboarding flow service (FlowResponse, PatchFlowRequest)
├── foundation/
│   ├── realtime/impl/     # gRPC realtime (RealtimeSubscriptionStore)
│   └── ube/domain/        # UBE analytics (SubEventType, UbeContentType, AppBootType, etc.)
├── geocoding/models/      # Google geocoding (Geometry, GoogleLocation, Viewport)
├── inappnotifications/    # In-app notification banners (BannerTypeV1Schema, BannerPlacementV1Schema)
├── likesyou/              # Likes You feature UI
├── matchnote/logic/       # SubjectMatchNoteResponse
├── metrics/impl/          # Metric sending workers
├── offercodes/models/     # Offer code system
├── offers/models/network/ # Offer eligibility
├── onboarding/            # Onboarding screens (PhotoTips, ProfileMedia, etc.)
├── pause/                 # Account pause feature
├── preferences/           # Preference UI (DatingPreferences, PrivacyPreferences)
├── privacy_preferences/   # Privacy/tracker settings
├── profile/ui/            # Profile hub
├── selfie/                # Selfie verification (FaceTec integration)
├── sendbird/models/       # Sendbird chat (FileMessageMetadata)
├── settings/              # Settings UI, MissingSMSAuthException
├── standouts/             # Standouts feature (StandoutsRepository)
├── subsystem/
│   ├── circle/            # Circle hub UI
│   └── idverification/    # ID verification (Jumio/external)
├── unmatched_reporting/   # Unmatch reporting
├── upgrade/               # Subscription upgrade UI
├── user/api/models/       # User traits (GetUserTraitsResponse, TraitRequest, TraitResponse, TraitEvaluationResponse)
├── utils/                 # PaywallPlacement enum
├── videotrimmer/          # Video trimmer UI
└── we_met/                # We Met survey feature
```

### Package: `defpackage/` (Obfuscated)

R8/ProGuard obfuscated classes. Key findings:

| Obfuscated Class | Real Purpose | How Identified |
|---|---|---|
| `omc` | Preference attribute enum (17 values) | toString() returns attribute names |
| `kz6` | Gender preference enum (Men/Women/Everyone/Nonbinary) | Static init with string names |
| `cqi` | Zodiac sign enum (12 signs → API string IDs) | Static init with names + string values |
| `qoh` | UiPreferenceChoice — renders preference values | Giant switch statement maps ordinal→string resource |
| `pmc` | Preference category (Basic/Premium/Advanced) | Referenced by `omc` constructor |
| `lnc` | Dealbreaker flag (can/cannot be dealbreaker) | Referenced by `omc` constructor |
| `eme` | Main API service interface (~50+ endpoints) | Contains @kwb/@vx6/@lwb/@fwb annotations |
| `luh` | User/profile API service interface | 14 endpoints for user/profile/traits |
| `ra1` | Billing API service interface | store/receipt, store/product endpoints |
| `sef`/`tef` | Auth SMS v2 service interfaces | auth/sms/v2 endpoints |
| `jed` | Auth/identity service interface | auth/sms, identity/install, auth/google |
| `nt9` | Match note service interface | like/connection match note endpoints |
| `ope` | Selfie verification service interface | 7 selfie verification endpoints |
| `fk7` | Hidden words/flag service interface | flag/hiddenword, flag/settings |
| `hj6` | Flow service interface | flow CRUD for onboarding |
| `b93` | Consent service interface | consent/user endpoints |
| `k72` | Media upload service interface | image/video upload |
| `xu7` | ID verification service interface | idverification endpoints |
| `bx3` | API client builder | Contains base URL: `https://prod-api.hingeaws.net/` |
| `t54` | gRPC client builder | Contains `{region}.hingeprod.net:50051` |
| `kwb` | @POST annotation (Retrofit) | Usage: creating/sending data |
| `lwb` | @PUT annotation (Retrofit) | Usage: full updates |
| `fwb` | @PATCH annotation (Retrofit) | Usage: partial updates |
| `vx6` | @GET annotation (Retrofit) | Usage: fetching data |
| `kg1` | @Body annotation (Retrofit) | Used on request body parameters |
| `c3c` | @Path annotation (Retrofit) | Used on URL path parameters |
| `yc8` | @Json (Moshi) | JSON field name annotation |
| `id8` | @JsonClass (Moshi) | JSON class annotation |

### Obfuscation Details

- **Obfuscator**: R8 (Google's code shrinker/obfuscator for Android)
- **Map ID**: `r8-map-id-e4d33ad71fd021bec081baa6af5b0f130b1acca5c1ab406a80727ca80b29c8ed`
- **Impact**: All non-public classes have 2-3 character names, enum patterns broken (jadx can't restore most enums)
- **Kotlin metadata preserved**: `@Metadata(d2 = {...})` annotations contain original class/method/field names
- **Moshi adapters preserved**: `*JsonAdapter.java` classes contain all JSON field names as plaintext strings
- **String resources preserved**: `R.java` contains all string resource keys (gender identities, sexual orientations, etc.)

### Key Insight: How to Find Enum Values

The enum integer IDs are NOT stored as constants in the APK. They come from the server via `VitalsConfig`.
However, the **rendering logic** in `qoh.b()` contains a massive switch statement that maps:
`(attribute_ordinal, api_id) → R.string.resource_name`

This is the definitive source for all preference enum value mappings.

## Serialization

- **JSON**: Moshi (not Gson) — `@id8` = `@JsonClass`, `@yc8` = `@Json`
- **Network**: Retrofit2 (obfuscated annotations: kwb=POST, lwb=PUT, fwb=PATCH, vx6=GET)
- **Database**: Room (SQLite) — 62 tables
- **gRPC**: Wire protocol buffers for realtime service
- **Analytics**: Custom UBE (User Behavior Events) system

## Security Observations

1. **No certificate pinning detected** — OkHttp client uses default trust manager
2. **Bearer token auth** — No request signing (unlike Bumble's MD5 pingback)
3. **Client-side rate limiting** — Spam detection message found but no server-side enforcement visible
4. **FaceTec selfie verification** — Uses third-party liveness detection (client keys endpoint exposed)
5. **gRPC on port 50051** — Separate from REST API, could have different auth/rate-limiting
6. **Telemetry pre-auth endpoint** — `client-telemetry-preauth.hingeprod.net` accepts metrics before authentication
7. **Data export** — Full GDPR data export via `user/export` (request → status check → download)
