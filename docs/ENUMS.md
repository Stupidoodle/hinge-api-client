# Hinge APK Decompiled Enums & Constants

Extracted from Hinge APK v9.x (co.hinge.app) via jadx decompilation.
Source: `defpackage/qoh.java` (preference choice renderer), `defpackage/omc.java` (attribute enum),
`defpackage/cqi.java` (zodiac), `defpackage/kz6.java` (gender preference), `R.java` (string resources),
`ApiProfileJsonAdapter.java`, `ApiSubjectProfileJsonAdapter.java`, and various API service interfaces.

## Preference Attributes (omc enum)

The `omc` enum defines all preference/filter attribute types. Ordinal values map to switch cases in `qoh.b()`.

| Ordinal | Name | Category | Dealbreaker? |
|---|---|---|---|
| 0 | GenderPreference | Basic (pmc.a) | No (lnc.a) |
| 1 | Location | Basic | No |
| 2 | MaxDistance | Advanced (pmc.c) | No |
| 3 | GenderedAge | Advanced | No |
| 4 | Ethnicities | Advanced | Yes (lnc.b) |
| 5 | Religions | Advanced | Yes |
| 6 | RelationshipTypes | Advanced | Yes |
| 7 | GenderedHeight | Premium (pmc.b) | Yes |
| 8 | DatingIntentions | Premium | Yes |
| 9 | Children | Premium | Yes |
| 10 | FamilyPlans | Premium | Yes |
| 11 | Drugs | Premium | Yes |
| 12 | Smoking | Premium | Yes |
| 13 | Marijuana | Premium | Yes |
| 14 | Drinking | Premium | Yes |
| 15 | Politics | Premium | Yes |
| 16 | EducationAttained | Premium | Yes |

Special API IDs:
- `-1` = "Open to All" (no preference set)
- `0` = "Prefer Not to Say"

## Gender Preference (kz6 enum)

| Value | Name | API String |
|---|---|---|
| 0 | Men | "Men" |
| 1 | Women | "Women" |
| 2 | Everyone | "Everyone" |
| 3 | Nonbinary | "Nonbinary" |

## Ethnicities (ordinal 4)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Native American | native_american |
| 2 | Black / African Descent | black_african_descent |
| 3 | East Asian | east_asian |
| 4 | Hispanic / Latino | hispanic_latino |
| 5 | Middle Eastern | middle_eastern |
| 6 | Pacific Islander | pacific_islander |
| 7 | South Asian | south_asian |
| 8 | White / Caucasian | white_caucasian |
| 9 | Other | other |
| 10 | Southeast Asian | southeast_asian |

## Religion (ordinal 5)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Buddhist | buddhist |
| 2 | Catholic | catholic |
| 3 | Christian | christian |
| 4 | Hindu | hindu |
| 5 | Jewish | jewish |
| 6 | Muslim | muslim |
| 7 | Spiritual | spiritual |
| 8 | Agnostic | agnostic |
| 9 | Atheist | atheist |
| 10 | Other | other |
| 11 | Sikh | sikh |

## Relationship Type (ordinal 6)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Monogamy | monogamy |
| 2 | Non-Monogamy | non_monogamy |
| 3 | Figuring Out Relationship Type | figuring_out_their_relationship_type |
| 4 | Friends First | profile_relationshipTypeOptions_friendsFirst |

## Dating Intentions (ordinal 8)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Life Partner | life_partner |
| 2 | Long-Term Relationship | long_term |
| 3 | Long-Term, Open to Short | long_term_open_to_short_term |
| 4 | Short-Term, Open to Long | short_term_open_to_long_term |
| 5 | Short-Term Fun | short_term |
| 6 | Figuring Out Dating Goals | figuring_out_their_dating_goals |

## Children (ordinal 9)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Don't Have Children | kids_do_not_have_children |
| 2 | Have Children | kids_have_children |

## Family Plans (ordinal 10)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Doesn't Want Children | family_plans_does_not_want |
| 2 | Wants Children | family_plans_wants |
| 3 | Open to Children | family_plans_open_to |
| 4 | Not Sure Yet | not_sure_yet |

## Drinking / Drugs / Smoking / Marijuana (ordinals 11-14)

All four share the same value mapping:

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Yes | yes |
| 2 | Sometimes | onboarding_sometimes |
| 3 | No | no |

## Politics (ordinal 15)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | Liberal | politics_liberal |
| 2 | Moderate | politics_moderate |
| 3 | Conservative | politics_conservative |
| 4 | Other | other |
| 5 | Not Political | not_political |

## Education Attained (ordinal 16)

| API ID | Value | String Resource |
|---|---|---|
| -1 | Open to All | preferences_open_to_all |
| 0 | Prefer Not to Say | — |
| 1 | High School | education_attained_high_school |
| 2 | Undergraduate | education_attained_undergraduate |
| 3 | Post-Graduate | education_attained_post_graduate |

## Zodiac Signs (cqi enum)

| Ordinal | Name | API String Value |
|---|---|---|
| 0 | Aries | "1" |
| 1 | Taurus | "2" |
| 2 | Gemini | "3" |
| 3 | Cancer | "4" |
| 4 | Leo | "5" |
| 5 | Virgo | "6" |
| 6 | Libra | "7" |
| 7 | Scorpio | "8" |
| 8 | Sagittarius | "9" |
| 9 | Capricorn | "10" |
| 10 | Aquarius | "11" |
| 11 | Pisces | "12" |

## Gender Identity (from R.string resources)

48 distinct gender identities supported. IDs are server-configured via `VitalsConfig.genderIdentities` list.
Grouped into 3 groups via `GenderIdentityGroupsConfig` (group0, group1, group2 — each a `List<Integer>`).

| String Resource Key | Display Value |
|---|---|
| gender_identity_agender | Agender |
| gender_identity_androgyne | Androgyne |
| gender_identity_androgynous | Androgynous |
| gender_identity_bigender | Bigender |
| gender_identity_cisgender_man | Cisgender Man |
| gender_identity_cisgender_woman | Cisgender Woman |
| gender_identity_demiboy | Demiboy |
| gender_identity_demifemale | Demifemale |
| gender_identity_demigirl | Demigirl |
| gender_identity_demiguy | Demiguy |
| gender_identity_demimale | Demimale |
| gender_identity_demiman | Demiman |
| gender_identity_demiwoman | Demiwoman |
| gender_identity_female_to_male | Female-to-Male |
| gender_identity_femme | Femme |
| gender_identity_gender_fluid | Gender Fluid |
| gender_identity_gender_questioning | Gender Questioning |
| gender_identity_gender_variant | Gender Variant |
| gender_identity_genderqueer | Genderqueer |
| gender_identity_hijra | Hijra |
| gender_identity_intersex | Intersex |
| gender_identity_intersex_man | Intersex Man |
| gender_identity_intersex_person | Intersex Person |
| gender_identity_intersex_woman | Intersex Woman |
| gender_identity_male_to_female | Male-to-Female |
| gender_identity_man | Man |
| gender_identity_masc | Masc |
| gender_identity_neither | Neither |
| gender_identity_neutrois | Neutrois |
| gender_identity_non_binary | Non-Binary |
| gender_identity_non_binary_man | Non-Binary Man |
| gender_identity_non_binary_woman | Non-Binary Woman |
| gender_identity_non_gendered | Non-Gendered |
| gender_identity_pangender | Pangender |
| gender_identity_polygender | Polygender |
| gender_identity_third_gender | Third Gender |
| gender_identity_trans | Trans |
| gender_identity_trans_man | Trans Man |
| gender_identity_trans_person | Trans Person |
| gender_identity_trans_woman | Trans Woman |
| gender_identity_transfeminine | Transfeminine |
| gender_identity_transgender | Transgender |
| gender_identity_transgender_female | Transgender Female |
| gender_identity_transgender_male | Transgender Male |
| gender_identity_transgender_man | Transgender Man |
| gender_identity_transgender_person | Transgender Person |
| gender_identity_transgender_woman | Transgender Woman |
| gender_identity_transmasculine | Transmasculine |
| gender_identity_transsexual | Transsexual |
| gender_identity_transsexual_female | Transsexual Female |
| gender_identity_transsexual_male | Transsexual Male |
| gender_identity_transsexual_man | Transsexual Man |
| gender_identity_transsexual_person | Transsexual Person |
| gender_identity_transsexual_woman | Transsexual Woman |
| gender_identity_two_spirit | Two-Spirit |
| Enbygender_identity_enby | Enby |

## Sexual Orientation (from R.string resources)

21 orientations. IDs are server-configured via `VitalsConfig.sexualOrientations`.

| String Resource Key | Display Value |
|---|---|
| sexual_orientation_allosexual | Allosexual |
| sexual_orientation_androsexual | Androsexual |
| sexual_orientation_asexual | Asexual |
| sexual_orientation_autosexual | Autosexual |
| sexual_orientation_bicurious | Bicurious |
| sexual_orientation_bisexual | Bisexual |
| sexual_orientation_demisexual | Demisexual |
| sexual_orientation_fluid | Fluid |
| sexual_orientation_gay | Gay |
| sexual_orientation_graysexual | Graysexual |
| sexual_orientation_gynesexual | Gynesexual |
| sexual_orientation_lesbian | Lesbian |
| sexual_orientation_monosexual | Monosexual |
| sexual_orientation_omnisexual | Omnisexual |
| sexual_orientation_pansexual | Pansexual |
| sexual_orientation_polysexual | Polysexual |
| sexual_orientation_queer | Queer |
| sexual_orientation_questioning | Questioning |
| sexual_orientation_skoliosexual | Skoliosexual |
| sexual_orientation_spectrasexual | Spectrasexual |
| sexual_orientation_straight | Straight |

## Pets (from R.string resources)

| String Resource Key | Display Value |
|---|---|
| pets_bird | Bird |
| pets_cat | Cat |
| pets_dog | Dog |
| pets_fish | Fish |
| pets_reptile | Reptile |

## Rating Actions (PendingRating$Rating enum)

| Ordinal | Name | API Constant |
|---|---|---|
| 0 | Block | "block" |
| 1 | Like | "like" |
| 2 | Note | "note" |
| 3 | Skip | "skip" |
| 4 | Report | "report" |

## Subscription Tiers

| Name | Level | Constant String |
|---|---|---|
| One (Hinge+) | 1 | "1tier" |
| Two (HingeX) | 2 | "2tier" |

## Subscription Providers

From `co.hinge.domain.models.store.SubscriptionProvider`:
- Google Play
- Apple App Store
- Stripe (web)

## Subscription Periods

From `co.hinge.domain.models.subscription.SubscriptionPeriod`:
- Weekly, Monthly, Quarterly, Semi-Annual, Annual

## VitalsConfig Fields

Server-configurable lists of valid IDs for each vital. Returned from config endpoint.
From `VitalsConfig.toString()`:

| Field | Type | Description |
|---|---|---|
| children | List<Int> | Valid children status IDs |
| covidVax | List<Int> | Valid COVID vaccination status IDs |
| ethnicities | List<Int> | Valid ethnicity IDs |
| familyPlans | List<Int> | Valid family plan IDs |
| genderIdentities | List<Int> | Valid gender identity IDs |
| genderIdentityGroups | GenderIdentityGroupsConfig | 3 groups of gender identity IDs |
| genders | List<Int> | Valid gender IDs |
| lastActive | List<Int> | Valid last-active status IDs |
| pronouns | List<Int> | Valid pronoun IDs |
| sexualOrientations | List<Int> | Valid sexual orientation IDs |
| datingIntentions | List<Int> | Valid dating intention IDs |
| zodiac | List<Int> | Valid zodiac sign IDs |
| pets | List<Int> | Valid pet IDs |

## Profile Fields (from JSON adapters)

### Own Profile (ApiProfile — `/user/v2`)

Full field list from `ApiProfileJsonAdapter`:

```
userId, firstName, lastName, birthday, email, phone, emailVerified, matchNote,
answers, genderId, genderIdentity, genderIdentityId, pronouns, sexualOrientations,
age, height, location, firstCompleted, children, drinking, drugs, educationAttained,
educations, educationsText, ethnicities, ethnicitiesText, familyPlans, hometown,
jobTitle, jobTitleText, marijuana, politics, politicsText, religions, religionsText,
smoking, works, covidVax, pets, zodiac, datingIntention, datingIntentionText,
languagesSpoken, languagesSpokenText, relationshipTypes, relationshipTypesText,
photos, photoSmartOrder,
childrenVisible, drinkingVisible, drugsVisible, educationAttainedVisible,
educationsVisible, genderIdentityVisible, pronounsVisible, sexualOrientationsVisible,
ethnicitiesVisible, familyPlansVisible, hometownsVisible, jobTitleVisible,
marijuanaVisible, politicsVisible, religionsVisible, smokingVisible, worksVisible,
covidVaxVisible, petsVisible, zodiacVisible, datingIntentionVisible,
didJustJoin, lastActiveStatusId, languagesSpokenVisible, relationshipTypesVisible,
selfieVerified
```

### Subject Profile (ApiSubjectProfile — other users)

```
age, children, covidVax, datingIntention, datingIntentionText, didJustJoin,
drinking, drugs, educationAttained, educations, ethnicities, ethnicitiesText,
familyPlans, firstName, genderIdentity, genderIdentityId, height, hometown,
jobTitle, languagesSpoken, lastActiveStatusId, location, marijuana, matchNote,
pets, politics, pronouns, relationshipTypeIds, relationshipTypesText, religions,
selfieVerified, sexualOrientations, smoking, works, zodiac, circleMember
```

### Profile Patch Request (PlayerProfilePatchRequest)

```
birthday, children, covidVax, datingIntention, datingIntentionText, drinking,
drugs, educationAttained, educations, ethnicities, ethnicitiesText, familyPlans,
firstName, genderId, genderIdentityId, height, hometown, jobTitle, languagesSpoken,
lastName, location, marijuana, matchNote, pets, politics, pronouns,
relationshipTypeIds, relationshipTypesText, religions, sexualOrientations,
smoking, works, zodiac
```

---

# API Endpoints (Complete from APK Decompilation)

Base URL: `https://prod-api.hingeaws.net/`

HTTP method annotations (obfuscated):
- `@kwb` = **POST**
- `@lwb` = **PUT**
- `@fwb` = **PATCH**
- `@vx6` = **GET**

## Auth & Identity

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `identity/install` | jed | Register device |
| POST | `auth/sms` | jed | Legacy SMS auth |
| POST | `auth/sms/v2/initiate` | sef | Send SMS OTP (v2) |
| POST | `auth/sms/v2` | sef | Submit OTP → Bearer token |
| PUT | `auth/sms/v2` | tef | Update SMS auth (v2) |
| PUT | `auth/sms` | eme | Legacy SMS update |
| POST | `auth/lookup` | jed | Auth lookup |
| POST | `auth/google` | jed | Google OAuth sign-in |
| PUT | `auth/google` | eme | Link Google account |
| POST | `auth/conflict` | eme | Resolve auth conflict |
| GET | `auth/settings` | qi0 | Get auth settings |
| GET | `auth/refresh` | eme | Refresh auth token |
| GET | `auth/logout` | eme | Logout |
| POST | `auth/device/validate` | ml4 | Device 2FA validation |
| GET | `authz/permissions` | eme | Get auth permissions |

## User Profile

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `user/v3` | luh | Get own profile (v3) |
| PATCH | `user/v3` | luh | Update own profile |
| PUT | `user/v2/profile/email` | luh | Update email |
| GET | `user/v3/public` | eme | Get public profiles (by IDs) |
| POST | `user/v3/public` | eme | Get public profiles (POST variant) |
| POST | `user/export` | eme | Request data export (GDPR) |
| GET | `user/export` | eme | Get data export download |
| GET | `user/export/status` | eme | Check export status |
| POST | `user/pause` | i4c | Pause account |
| GET | `user/repeat` | eme | Recycle seen profiles |
| GET | `user/circle/progress` | il2 | Get Circle progress |

## User Traits (NEW — not in web API)

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `user/v2/traits` | luh | Get user traits |
| POST | `user/v2/traits` | luh | Create user traits |
| PATCH | `user/v2/traits` | luh | Update user traits |
| POST | `user/v2/traits/evaluate` | luh | Evaluate trait (AI feedback) |
| POST | `user/v2/traits/eval` | luh | Evaluate trait (short alias) |

## DLP (Data Loss Prevention)

| Method | Path | Interface | Description |
|---|---|---|---|
| PATCH | `dlp/user` | luh | Update DLP user settings |

## Content

| Method | Path | Interface | Description |
|---|---|---|---|
| PUT | `content/v1/answers` | luh | Update prompt answers |
| GET | `content/v2` | eme | Get own content (photos + answers) |
| GET | `content/v2/public` | eme | Get other users' content |
| POST | `content/v2/public` | eme | Get other users' content (POST) |
| POST | `content/v1/prompt_poll` | eme | Create prompt poll |
| POST | `content/v1/video_prompt` | eme | Upload video prompt |
| PUT | `content/v1/photos` | eme | Update photos |
| POST | `content/v1/date_idea` | eme | Create date idea prompt |
| POST | `/content/v1/answer/evaluate` | eme | AI answer evaluation |
| GET | `/content/v1/settings` | eme | Get content settings |
| PATCH | `/content/v1/settings` | eme | Update content settings |
| GET | `/content/v1/tips` | zk3 | Get content tips |

## Recommendations & Rating

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `rec/v2` | eme | Get recommendation feed |
| POST | `rate/v2/initiate` | eme | Like/skip/note/block/report |
| POST | `rate/v1/match` | eme | Match rating |
| POST | `rate/v2/respond` | eme | Respond to a rating |

## Likes & Standouts

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `like/v2` | eme | Get likes received (Likes You) |
| GET | `like/v2/matchnote/{subjectId}` | nt9 | Get match note for a like |
| POST | `like/v2/hidden/feedback` | eme | Hidden likes feedback |
| GET | `standouts/v3` | eme | Get standouts feed (v3!) |

## Connections (Matches)

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `connection/v2` | eme | Get all connections/matches |
| GET | `connection/subject/{subjectId}` | eme | Get specific connection |
| GET | `connection/v2/matchnote/{subjectId}` | nt9 | Get match note for connection |
| PATCH | `connection/phonenumber` | eme | Exchange phone number |
| PUT | `connection/hide` | eme | Hide a connection |
| PUT | `connection/unhide` | eme | Unhide a connection |
| GET | `connection/unmatchreporting/unmatches` | i2c | Get unmatch reports |
| POST | `connection/unmatchreporting/remove` | i2c | Remove unmatch report |

## Chat & Messaging

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `message/authenticate` | eme | Get Sendbird JWT |
| POST | `message/send` | eme | Send message (server-side) |
| POST | `message/voicenote/transcription` | eme | Voice note transcription |
| POST | `message/v2/harmfulreview` | eme | Review harmful message |
| POST | `message/v2/harmfulreview/unmute` | eme | Unmute harmful review |

## Preferences

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `preference/v2/selected` | eme | Get current preferences |
| PATCH | `preference/v2/selected` | eme | Update preferences |

## Boost

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `boost` | eme | Get boost info |
| GET | `boost/bystart` | eme | Get boost by start time |
| POST | `store/boost/activate` | eme | Activate a boost |
| GET | `store/boost` | eme | Get boost store info |

## Store & Billing

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `store/v6/product` | ra1 | Get products/pricing |
| POST | `store/v2/subscription/android` | ra1 | Submit subscription receipt |
| POST | `store/receipt` | ra1 | Submit purchase receipt |
| POST | `store/receipt-consumable` | ra1 | Submit consumable receipt |
| POST | `store/v1/product/offercode/android` | pjb | Redeem offer code |
| POST | `store/v1/customer/portal` | eme | Open customer portal |
| GET | `store/v2/account` | eme | Get subscription account |
| GET | `likelimit` | eme | Get daily like/rose limits |

## Offers

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `/offers/eligible` | fkb | Check offer eligibility |
| POST | `/offers/v2/eligible` | fkb | Check offer eligibility (v2) |
| PUT | `/offers/activate` | fkb | Activate an offer |

## Notifications

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `notification/v1/settings` | luh | Update notification settings |
| GET | `notification/v1/settings` | eme | Get notification settings |
| GET | `notification/v1/inbox` | j08 | Get notification inbox |
| GET | `/notification/v1/settings/chats` | eme | Get chat notification settings |
| POST | `/notification/v1/settings/chat` | eme | Update chat notification settings |
| POST | `notifications/v1/interaction` | j08 | Log notification interaction |
| GET | `/inappnotifications/v1/views` | j08 | Get in-app notification views |
| POST | `/inappnotifications/v1/view` | j08 | Create/update in-app notification view |

## Moderation & Safety

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `report/` | eme | Submit report |
| GET | `report/config` | eme | Get report configuration |
| POST | `flag/textreview` | w70 | Pre-flight text moderation |
| GET | `/flag/config` | w70 | Get flag configuration |
| POST | `flag/hiddenword/add` | fk7 | Add hidden word |
| POST | `flag/hiddenword/remove` | fk7 | Remove hidden word |
| GET | `flag/hiddenword` | fk7 | Get hidden words list |
| GET | `flag/settings` | fk7 | Get flag settings |
| PATCH | `flag/settings` | fk7 | Update flag settings |

## Selfie Verification

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `selfieverification` | ope | Get selfie verification status |
| POST | `selfieverification/consent` | ope | Submit verification consent |
| GET | `selfieverification/eligibility` | ope | Check eligibility |
| GET | `selfieverification/facetec/session` | ope | Get FaceTec session |
| GET | `selfieverification/facetec/clientkeys` | ope | Get FaceTec client keys |
| POST | `selfieverification/liveness-check` | ope | Submit liveness check |
| POST | `selfieverification/submit` | ope | Submit verification photo |

## ID Verification

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `/idverification/status` | xu7 | Get ID verification status |
| GET | `/idverification/link` | xu7 | Get verification link |
| POST | `/idverification/link` | xu7 | Create verification link |

## Email Verification

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `codeval/email/resend` | ln5 | Resend email verification |
| POST | `codeval/email/validate` | ln5 | Validate email code |
| POST | `codeval/device/resend` | ml4 | Resend device verification |

## Fresh Start

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `/freshstart/eligible` | eme | Check Fresh Start eligibility |
| POST | `/freshstart` | eme | Initiate Fresh Start (account reset?) |

## We Met

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `wemet/survey` | eme | Submit We Met survey |
| GET | `wemet/surveystatus` | eme | Get survey status |
| GET | `wemet/config` | eme | Get We Met config |

## Profile State

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `profilestate/basics/missing` | luh | Get missing profile basics |
| GET | `profilestate/profile` | luh | Get profile completeness |

## What Works (Dating Guides)

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `whatworks/v1/guides` | eme | Get dating guides/tips |

## Appeals & Statements

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `appeal` | s50 | Get appeal status |
| POST | `appeal` | s50 | Submit appeal |
| GET | `statement/copy` | s50 | Get statement copy |
| POST | `/appeal/removedcontent` | te3 | Appeal removed content |
| GET | `/statement/removedcontent` | te3 | Get removed content statement |
| POST | `/statement/removedcontent/acknowledge` | te3 | Acknowledge removed content |
| POST | `/statement/removedcontent/acknowledge/batch` | te3 | Batch acknowledge |

## Reviews

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `review/request` | x30 | Get app review request |
| POST | `review/request` | x30 | Submit app review |

## LSP (Like-Send-Prompt?) Feedback

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `/lsp/feedback` | eme | Submit LSP feedback |

## Config

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `config/v3` | eme | Get app configuration |
| GET | `config/v3/preferences` | eme | Get preference configuration |
| GET | `config/safetyarticles` | eme | Get safety articles |
| GET | `login/config` | jed | Get login configuration |

## CDN & Media

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `cdn/token` | eme | Get CDN upload token |
| POST | `cdn/v1/token/connection-asset-url` | eme | Get connection asset CDN URL |
| POST | `image/upload` | k72 | Upload image |
| POST | `video/upload` | k72 | Upload video (3 variants) |

## Metrics & Telemetry

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `metric/v2` | eme | Submit authenticated metrics |
| POST | `metric/v3/noauth` | uoh | Submit unauthenticated metrics |
| POST | `metric/analytics/v1` | knh | Submit analytics metrics |
| POST | `signal/v1` | eme | Submit signal data |
| POST | `/clienttelemetryauth/token` | eme | Get telemetry auth token |

## Flow Service (Onboarding Flows)

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `flow` | hj6 | Get/create flows |
| POST | `flow/{flowName}` | hj6 | Get specific flow |
| PATCH | `flow` | hj6 | Update flow state |
| PATCH | `flow/position` | hj6 | Update flow position |

## Consent

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `consent/user/message` | b93 | Get consent messages |
| POST | `consent/user/update` | b93 | Update consent |
| GET | `consent/user/blocking` | b93 | Get blocking consent |
| POST | `consent/user/blocking` | b93 | Update blocking consent |
| POST | `consent/user/message` | b93 | Submit consent message |
| POST | `consent/user/get` | b93 | Get user consent |

## Prompts

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `/prompts` | luh | Get all prompt templates (419 prompts, 14 categories) |

## BPYK (Contacts/People You Know)

| Method | Path | Interface | Description |
|---|---|---|---|
| POST | `bpyk` | wd1 | Submit BPYK data |
| GET | `bpyk` | wd1 | Get BPYK data |

## Geocoding

| Method | Path | Interface | Description |
|---|---|---|---|
| GET | `geocode/json` | z07 | Geocode address (2 variants) |

---

# Infrastructure Endpoints (Non-API)

| URL | Purpose |
|---|---|
| `https://prod-api.hingeaws.net/` | Main REST API |
| `https://{region}.hingeprod.net:50051` | gRPC realtime service (push notifications, live updates) |
| `https://prod-ue1-cloudinary-webhook.hingeprod.net/cdn/voiceprompt` | Voice prompt CDN webhook |
| `https://prod-ue1-cloudinary-webhook.hingeprod.net/cdn/voicenote` | Voice note CDN webhook |
| `https://client-telemetry.hingeprod.net` | Client telemetry (authenticated) |
| `https://client-telemetry-preauth.hingeprod.net` | Client telemetry (pre-auth) |
| `https://media.hingenexus.com/` | Media CDN (photos, videos) |

## gRPC Realtime Service

Hinge uses **gRPC over HTTP/2** (port 50051) for real-time features — this is separate from Sendbird chat.
Proto definitions found: `realtime/v1/realtime.proto`

Messages:
- `realtime.v1.OpenRequest` — Open realtime connection
- `realtime.v1.OpenResponse` — Realtime connection response
- `realtime.v1.Subscribe` — Subscribe to channels
- `realtime.v1.ChannelSpec` — Channel specification

---

# Notification Channels

From `App.java`, registered notification channels:
- `likesyou` — Likes You notifications
- `features` — Feature announcements
- `connections` — New matches
- `recommendations` — New recommendations
- `reminders` — Engagement reminders
- `insidertips` — Dating tips
- `chat` — Chat messages
- `boost` — Boost notifications
- `videocalls` — Video call notifications
- `dataexport` — Data export ready

---

# Local Database Tables

From `Database_Impl.java` — 62 tables:

```
abuse_report_configuration, abuse_report, backstories, basic_choices, branding,
channels, chat_messages, chat_message_attempt, chat_specific_notifications,
chat_voice_note_audio_transcript, consents, consent_categories, block_list,
discover_batch, discover_subject, discover_preview_subject, flow_service_progress,
flow_service_states, hidden_words, metrics, offer_states, text_prompt_feedback,
ube_events, ube_session_events, ube_base_ui_elements, ube_button_ui_elements,
ube_checkbox_ui_elements, ube_generic_button_ui_elements, ube_icon_button_ui_elements,
ube_list_view_ui_elements, ube_list_item_ui_elements, ube_screen_ui_elements,
ube_slider_ui_elements, ube_ui_element_events, discover_filter, draft_messages,
impressions, liked_content, likes_you_sort, matches, match_messages,
pending_ratings, pending_reactions, player_answers, player_media,
potentially_harmful_messages, preference_choices, profiles, prompts,
prompt_categories, second_chance_data, sorted_hidden_likes_profiles,
likes_you_profile_feeds, standouts_content, subject_answers, subject_media,
surveys, what_works_guides, what_works_guides_tips, removed_player_answers,
removed_player_media, conversation_tips
```

---

# Interesting Findings

## Fresh Start Feature
- Endpoint: `GET /freshstart/eligible` + `POST /freshstart`
- Allows users to reset their account/algorithm. Could be interesting to test what "reset" actually means server-side.

## BPYK (Block People You Know)
- Endpoint: `POST/GET bpyk`
- Contacts upload feature for blocking people you know IRL.

## Circle Feature
- Endpoint: `GET user/circle/progress`
- New social feature, `circleMember` field on profiles. Appears to be a friend/social circle integration.

## User Traits System (NEW)
- Full CRUD: `GET/POST/PATCH user/v2/traits`
- AI evaluation: `POST user/v2/traits/evaluate` and `user/v2/traits/eval`
- Separate from profile vitals — likely personality/behavioral traits.

## Standouts v3
- Endpoint updated to `GET standouts/v3` (was just `GET /standouts`).

## AI Content Evaluation
- `POST /content/v1/answer/evaluate` — AI evaluates prompt answers before submission.
- Uses `TraitEvaluationResponse` — suggests AI scoring of profile content quality.

## Rate v2 Respond
- `POST rate/v2/respond` — Respond to a rating. Not documented before. Could be for responding to SuperLikes/Notes.

## Hidden Likes Feedback
- `POST like/v2/hidden/feedback` — Feedback mechanism for hidden likes. Has `sorted_hidden_likes_profiles` table.

## Second Chance
- Local table `second_chance_data` — Profiles you can reconsider after skipping.

## DLP (Data Loss Prevention)
- `PATCH dlp/user` — Suggests server-side data loss prevention for user data.

## Voice Note Transcription
- `POST message/voicenote/transcription` — Server-side voice note transcription.

## Harmful Message Review
- `POST message/v2/harmfulreview` — Review potentially harmful messages.
- `POST message/v2/harmfulreview/unmute` — Unmute after harmful review.
- Local table: `potentially_harmful_messages`

## Network Spam Detection
- Code reference: `"NETWORK SPAM DETECTED: Endpoint '...' called ... times in the last ..."` — Client-side rate limiting.

---

# Wire-Format JSON Field Names (from Moshi JsonAdapters)

These are the EXACT field names sent over the wire. Extracted from `bf8.a(...)` calls in `*JsonAdapter.java` files.
This is critical for building API clients — field names are case-sensitive and must match exactly.

## Rating System

### InitiateRatingRequest (`POST rate/v2/initiate`)

Used for swiping on recommendations (Like/Skip/Note/Block).

```json
{
  "ratingId": "uuid",
  "ratingToken": "JWE token from /rec/v2",
  "subjectId": "target user ID",
  "sessionId": "uuid",
  "rating": "like|skip|note|block",
  "origin": "string (e.g. 'compatibles', 'standouts')",
  "hasPairing": false,
  "topPhotoContentId": "uuid or null",
  "content": { /* ApiLikedContent — see below */ },
  "created": "ISO-8601 timestamp",
  "data": { /* arbitrary metadata map */ },
  "initiatedWith": "string (e.g. 'like', 'rose', 'note')",
  "hcmRunId": "string or null (harmful content model run ID)"
}
```

**Allowed ratings**: Like, Skip, Note, Block (validated client-side, throws if Report passed).

### RespondRatingRequest (`POST rate/v2/respond`)

Used for responding to incoming likes (Likes You screen). Accept or block someone who liked you.

```json
{
  "ratingId": "uuid",
  "subjectId": "target user ID",
  "sessionId": "uuid",
  "rating": "like|block",
  "origin": "string",
  "hasPairing": false,
  "content": { /* ApiLikedContent or null */ },
  "created": "ISO-8601 or null",
  "data": { /* map or null */ },
  "initiatedWith": "string",
  "sortType": "string or null"
}
```

**Allowed ratings**: Like, Block only (not Skip or Note — you can only accept or block incoming likes).

### MatchRatingRequest (`POST rate/v1/match`)

Used for acting on existing matches (block from chat/match screen).

```json
{
  "ratingId": "uuid",
  "subjectId": "target user ID",
  "sessionId": "uuid",
  "rating": "block",
  "origin": "string",
  "hasPairing": false,
  "content": { /* ApiLikedContent or null */ },
  "created": "ISO-8601 or null",
  "data": { /* map or null */ },
  "initiatedWith": "string",
  "secondChanceEligible": true|false|null
}
```

**Allowed ratings**: Block only (the only action available on a match is to unmatch/block).
**Note**: `secondChanceEligible` — if true, the unmatched user gets a "Second Chance" to re-appear.

### ApiLikedContent (nested in rating requests)

When liking with a comment, photo, or voice note:

```json
{
  "comment": "text comment or null",
  "video": { /* video content */ },
  "photo": { "cdnId": "...", "contentId": "...", "url": "...", "boundingBox": {...}, "caption": "...", "location": "...", "promptId": "...", "promptText": "..." },
  "prompt": { /* prompt answer liked */ },
  "voicePrompt": { /* voice prompt liked */ },
  "videoPrompt": { /* video prompt liked */ },
  "promptPoll": { /* prompt poll liked */ },
  "dateIdea": { /* date idea liked */ }
}
```

### RatingResponse (server response to `rate/v2/initiate`)

```json
{
  "limit": { /* RatingLimit */ }
}
```

## Traits System (NEW)

### TraitRequest / TraitResponse

```json
{
  "id": "trait ID string",
  "userInput": "user's text input for the trait"
}
```

### TraitEvaluationResponse (`POST user/v2/traits/evaluate`)

```json
{
  "status": "string (e.g. 'approved', 'rejected', 'warning')",
  "detail": "string or null (explanation of evaluation)"
}
```

### GetUserTraitsResponse (`GET user/v2/traits`)

```json
{
  "traits": [ { "id": "...", "userInput": "..." }, ... ],
  "traitMaxCharLimit": 150
}
```

### PostUserTraitsRequest (`POST user/v2/traits`)

```json
{
  "traits": [ { "id": "...", "userInput": "..." }, ... ]
}
```

### PostUserTraitsErrorResponse (when rejected)

```json
{
  "traits": [ { "id": "...", "type": "error_type" }, ... ]
}
```

## Recommendations

### RecommendationRequest (`POST rec/v2`)

```json
{
  "playerId": "own user ID",
  "activeToday": true,
  "newHere": false,
  "genderPrefId": 0
}
```

### RecommendationResponse

```json
{
  "feeds": [
    {
      "id": "string",
      "origin": "compatibles|standouts|etc",
      "permission": "string",
      "subjects": [ /* Potential[] */ ],
      "preview": { "permission": "...", "subjects": [...] },
      "viewToken": "string"
    }
  ],
  "activePills": [ /* ActivePill[] */ ]
}
```

### Potential (individual recommendation)

```json
{
  "subjectId": "user ID",
  "ratingToken": "JWE token (required for rating)",
  "recId": "recommendation ID",
  "pairing": "pairing info",
  "enhancements": { "secondChance": { "secondChanceSource": "string" } }
}
```

### Impression (recommendation you've seen)

```json
{
  "subjectId": "user ID",
  "created": "ISO-8601",
  "rating": "like|skip|note|block",
  "pairing": "string",
  "showMatchNote": true|false,
  "expires": "ISO-8601 or null",
  "source": "string",
  "initiatedWith": "string",
  "hidden": true|false,
  "enhancements": { /* Enhancements */ }
}
```

## Likes You

### LikesResponse (`GET like/v2`)

```json
{
  "likes": [ /* IncomingRating[] */ ],
  "sorts": [ /* SortLikesCategory[] */ ],
  "sortedLikes": [ { "sortID": "string", "data": { "id": "..." } } ],
  "hiddenLikes": [ { "id": "...", "reason": "..." } ],
  "viewToken": "string"
}
```

### IncomingRating

```json
{
  "content": { /* ApiLikedContent — what they liked on your profile */ }
}
```

## Connections (Matches)

### ConnectionsResponse (`GET connection/v2`)

```json
{
  "connections": [ /* Match[] */ ],
  "yourTurnMatchLimit": 10,
  "viewToken": "string"
}
```

### Match

```json
{
  "initiatorId": "who liked first",
  "subjectId": "the other user's ID",
  "receivedTime": "ISO-8601",
  "sentTime": "ISO-8601",
  "sentContent": "what was sent",
  "showMatchNote": true|false,
  "pairing": "string",
  "phoneNumberExchanged": true|false,
  "socialMediaExchangedTimestamp": "ISO-8601 or null",
  "isHidden": true|false,
  "source": "string",
  "initiatedWith": "string",
  "enhancements": { /* Enhancements */ },
  "viewToken": "string"
}
```

## Preferences

### SelectedPreferences (`GET/PATCH preference/v2/selected`)

```json
{
  "ageRange": { "min": 18, "max": 35 },
  "genderedAgeRanges": { /* per-gender age ranges */ },
  "children": [1, 2],
  "dealbreakers": { /* DealBreakers */ },
  "drinking": [1, 2, 3],
  "drugs": [1, 2, 3],
  "educationAttained": [1, 2, 3],
  "ethnicities": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  "familyPlans": [1, 2, 3, 4],
  "genderPreferences": [0, 1],
  "genderPreferenceId": 0,
  "heightRange": { "min": 150, "max": 200 },
  "genderedHeightRanges": { /* per-gender height ranges */ },
  "marijuana": [1, 2, 3],
  "maxDistance": 50,
  "politics": [1, 2, 3, 4, 5],
  "religions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
  "smoking": [1, 2, 3],
  "userId": "own user ID",
  "updated": "ISO-8601",
  "datingIntentions": [1, 2, 3, 4, 5, 6],
  "relationshipTypes": [1, 2, 3, 4]
}
```

## Config

### ConfigResponse (`GET config/v3`)

```json
{
  "voicePromptsContextualNudge": { /* VoicePromptContextualNudgeConfig */ },
  "vitalBadges": { /* VitalBadgesConfig */ },
  "metrics": { /* MetricConfig */ },
  "matchNote": { /* MatchNoteConfig */ },
  "vices": { "drinking": [...], "drugs": [...], "marijuana": [...], "smoking": [...] },
  "virtues": { "datingIntentions": [...], "educationAttained": [...], "politics": [...], "religions": [...], "languagesSpoken": [...], "relationshipTypes": [...] },
  "vitals": { "children": [...], "covidVax": [...], "ethnicities": [...], "familyPlans": [...], "genderIdentities": [...], "genderIdentityGroups": { "0": [...], "1": [...], "2": [...] }, "genders": [...], "lastActive": [...], "pronouns": [...], "sexualOrientations": [...], "datingIntentions": [...], "zodiac": [...], "pets": [...] },
  "geographicRestrictions": { /* geographic restrictions */ },
  "geographicAgeRestrictions": { /* age-based geographic restrictions */ }
}
```

**KEY**: The `config/v3` endpoint returns all valid enum IDs for every vital/vice/virtue. This is the authoritative source for what IDs are valid.

## Auth

### NewAuthResponse (`POST auth/sms/v2`)

```json
{
  "identityId": "uuid",
  "token": "Bearer token",
  "expires": "ISO-8601 expiration",
  "migratedUser": true|false
}
```

## Like Limits

### LikeLimitResponse (`GET likelimit`)

```json
{
  "freeSuperlikeExpiration": "ISO-8601 or null",
  "freeSuperlikesLeft": 1,
  "likesLeft": 8,
  "superlikesLeft": 0
}
```

## Boost

### BoostActivateResponse (`POST store/boost/activate`)

```json
{
  "start": "ISO-8601",
  "end": "ISO-8601",
  "remaining": 2
}
```

## Fresh Start

### FreshStartEligibilityResponse (`GET /freshstart/eligible`)

```json
{
  "eligible": true|false
}
```

## Report

### Report (`POST report/`)

```json
{
  "subjectId": "target user ID",
  "reason": "string or null",
  "selection": { /* AbuseReportSelection or null */ },
  "type": "string (e.g. 'chat', 'profile')",
  "detail": "free-text detail",
  "hasPairing": false,
  "timestamp": "ISO-8601",
  "entry": "Report",
  "ratingToken": "string or null"
}
```

## Photo Model

```json
{
  "url": "CDN URL",
  "source": "string",
  "sourceId": "string",
  "width": 1080,
  "height": 1350,
  "boundingBox": { "topLeft": { "x": 0, "y": 0 }, "bottomRight": { "x": 1, "y": 1 } },
  "cdnId": "cloudinary ID",
  "contentId": "uuid",
  "videos": [ /* Video[] */ ],
  "videoUrl": "CDN video URL or null",
  "promptId": "prompt ID if photo is for a prompt",
  "caption": "photo caption or null",
  "location": "location string or null",
  "pHash": "perceptual hash string",
  "selfieVerified": true|false
}
```

## Harmful Message Review

### PotentiallyHarmfulMessageReviewRequest (`POST message/v2/harmfulreview`)

```json
{
  "messageSenderID": "sender user ID",
  "messageID": "sendbird message ID",
  "action": "string (e.g. 'review', 'dismiss')"
}
```

### PotentiallyHarmfulMessageReviewResponse

```json
{
  "muted": true|false,
  "muteValidForDays": 7
}
```

---

# Call Chain: How Rating Works End-to-End

## Like Flow (Swipe Right)

1. **Get recommendations**: `POST rec/v2` → `RecommendationResponse` with `feeds[].subjects[]`
2. Each `Potential` has `subjectId` + `ratingToken` (JWE, server-issued, required for rating)
3. **Load profile**: `GET user/v3/public?ids={subjectId}` + `GET content/v2/public?ids={subjectId}`
4. **Rate**: `POST rate/v2/initiate` with `rating: "like"`, `ratingToken`, `subjectId`
   - Can include `content.comment` (note), `content.photo` (liked photo), `content.prompt` (liked prompt answer)
   - `initiatedWith`: `"like"` for normal, `"rose"` for SuperLike
5. **Response**: `RatingResponse` with `limit` (remaining likes)
6. **Client stores**: Impression saved to local `impressions` table, PendingRating to `pending_ratings`

## Respond to Like Flow (Likes You)

1. **Get likes**: `GET like/v2` → `LikesResponse` with `likes[]`, `sortedLikes[]`
2. Each incoming like has `content` showing what they liked
3. **Respond**: `POST rate/v2/respond` with `rating: "like"` (match!) or `rating: "block"`
4. If matched → appears in `GET connection/v2`

## Unmatch/Block from Match

1. **Get matches**: `GET connection/v2` → `ConnectionsResponse` with `connections[]`
2. **Block**: `POST rate/v1/match` with `rating: "block"`, `secondChanceEligible: true/false`

## Key Insight: ratingToken

The `ratingToken` is a server-issued JWE (JSON Web Encryption) token bundled with each recommendation.
It's opaque to the client and required for every rating call. This prevents:
- Rating users you haven't been shown
- Replay attacks (token is single-use)
- Bypassing the recommendation algorithm

Without a valid `ratingToken`, the server rejects the rating. You can only rate users the server has shown you.

---

# Obfuscation Reference Table

Quick-reference for future decompilation work. Maps obfuscated class names to real purpose.

| Class | Package | Purpose | Key Method/Field |
|---|---|---|---|
| `omc` | defpackage | PreferenceAttribute enum (17 values) | `d-t` = static enum values |
| `kz6` | defpackage | GenderPreference enum | `c-f` = Men/Women/Everyone/Nonbinary |
| `cqi` | defpackage | ZodiacSign enum | `a` field = API string ID |
| `qoh` | defpackage | UiPreferenceChoice renderer | `b()` = giant switch for display strings |
| `pmc` | defpackage | PreferenceCategory (Basic/Premium/Advanced) | `a,b,c` = enum values |
| `lnc` | defpackage | DealBreakerFlag | `a,b` = can/cannot be dealbreaker |
| `eme` | defpackage | Main API service (~50 endpoints) | Methods a-z with annotations |
| `luh` | defpackage | User/Profile API (14 endpoints) | Methods a-n |
| `ra1` | defpackage | Billing API (4 endpoints) | store/* paths |
| `sef` | defpackage | Auth SMS v2 (2 endpoints) | auth/sms/v2/* |
| `tef` | defpackage | Auth SMS v2 PUT | PUT auth/sms/v2 |
| `jed` | defpackage | Auth/Identity (5 endpoints) | identity/install, auth/* |
| `nt9` | defpackage | Match notes (2 endpoints) | like/connection matchnote |
| `ope` | defpackage | Selfie verification (7 endpoints) | selfieverification/* |
| `fk7` | defpackage | Hidden words/flags (5 endpoints) | flag/* |
| `hj6` | defpackage | Flow service (4 endpoints) | flow/* |
| `b93` | defpackage | Consent service (6 endpoints) | consent/user/* |
| `k72` | defpackage | Media upload (4 endpoints) | image/video upload |
| `xu7` | defpackage | ID verification (3 endpoints) | idverification/* |
| `fkb` | defpackage | Offers (3 endpoints) | /offers/* |
| `j08` | defpackage | Notifications (6 endpoints) | notification/v1/* |
| `i2c` | defpackage | Unmatch reporting (2 endpoints) | connection/unmatchreporting/* |
| `i4c` | defpackage | Account pause (1 endpoint) | user/pause |
| `il2` | defpackage | Circle progress (1 endpoint) | user/circle/progress |
| `ml4` | defpackage | Device validation (2 endpoints) | codeval/device/*, auth/device/* |
| `ln5` | defpackage | Email validation (2 endpoints) | codeval/email/* |
| `s50` | defpackage | Appeals (3 endpoints) | appeal, statement/copy |
| `te3` | defpackage | Removed content (4 endpoints) | /appeal/removedcontent, /statement/* |
| `w70` | defpackage | Text review/moderation (2 endpoints) | flag/textreview, /flag/config |
| `x30` | defpackage | App review (2 endpoints) | review/request |
| `wd1` | defpackage | BPYK contacts (2 endpoints) | bpyk |
| `qi0` | defpackage | Auth settings (1 endpoint) | auth/settings |
| `z07` | defpackage | Geocoding (2 variants) | geocode/json |
| `zk3` | defpackage | Content tips (1 endpoint) | /content/v1/tips |
| `uoh` | defpackage | Unauthenticated metrics | metric/v3/noauth |
| `knh` | defpackage | Analytics metrics | metric/analytics/v1 |
| `pjb` | defpackage | Offer codes (1 endpoint) | store/v1/product/offercode/* |
| `bx3` | defpackage | API client builder | Base URL: prod-api.hingeaws.net |
| `t54` | defpackage | gRPC client builder | hingeprod.net:50051 |
| `kwb` | defpackage | @POST annotation | Retrofit HTTP POST |
| `lwb` | defpackage | @PUT annotation | Retrofit HTTP PUT |
| `fwb` | defpackage | @PATCH annotation | Retrofit HTTP PATCH |
| `vx6` | defpackage | @GET annotation | Retrofit HTTP GET |
| `kg1` | defpackage | @Body annotation | Retrofit request body |
| `c3c` | defpackage | @Path annotation | Retrofit URL path param |
| `yc8` | defpackage | @Json annotation | Moshi JSON field name |
| `id8` | defpackage | @JsonClass annotation | Moshi class annotation |
| `bf8` | defpackage | JsonReader.Options factory | `bf8.a("field1","field2",...)` |
| `ti3` | defpackage | Kotlin Continuation | Coroutine continuation type |
| `tp5` | defpackage | Collections utility | `tp5.a` = emptyList() |
| `ir` | defpackage | Error/assertion utility | `ir.n("message")` = throw |
| `a3g` | defpackage | String utility | `a3g.p()` = string concat |
| `bb3` | defpackage | Hash utility | Used in hashCode() impls |
| `flc` | defpackage | StringBuilder utility | `flc.r()` = append multiple |

---

# Deep Dive: Additional Models & Wire Formats

## Chat: HingeSendMessageRequest (`POST message/send`)

```json
{
  "subjectId": "target user ID",
  "matchMessage": true|false,
  "origin": "string",
  "dedupId": "uuid (deduplication)",
  "messageData": {
    "message": "text content",
    "fileUrl": "CDN URL for voice/media or null",
    "fileMetadata": {
      "cdnId": "cloudinary ID",
      "durationSeconds": 15.0,
      "waveform": [0.1, 0.5, 0.8, ...]
    }
  },
  "messageType": "string (e.g. 'text', 'voice', 'video')",
  "ays": false
}
```

**`ays` = "Are You Sure"** — `performAreYouSureCheck` boolean. When true, the server may trigger a safety check before delivering the message. Found in `HingeSendMessageRequest` with `@Json(name = "ays")`.

**Header**: Requires `X-Session-Id` header (passed separately from body).

### HingeSendMessageResponse

```json
{
  "messageId": "sendbird message ID string",
  "createdAt": 1234567890
}
```

## Unmatch Reporting (Past Matches)

### GET `connection/unmatchreporting/unmatches`

```json
{
  "unmatches": [
    {
      "subjectId": "user ID",
      "firstName": "Name",
      "unmatchedAt": "ISO-8601",
      "rating": { /* rating details */ }
    }
  ],
  "nextCursor": "pagination cursor or null",
  "hasNext": true|false,
  "timeRangeDays": 90
}
```

### POST `connection/unmatchreporting/remove`

```json
{
  "subjectId": "user ID to remove from past matches"
}
```

## Account Pause

### POST `user/pause`

```json
{
  "isPaused": true|false,
  "pausedHours": 24
}
```

## Phone Number Exchange

### PATCH `connection/phonenumber`

```json
{
  "subjectId": "match user ID",
  "exchanged": true|false
}
```

## Hide/Unhide Connection

### PUT `connection/hide` / PUT `connection/unhide`

```json
{
  "subjectId": "match user ID"
}
```

## We Met Survey

### POST `wemet/survey`

```json
{
  "subjectId": "user ID",
  "lastCardId": "card ID"
}
```

### WeMetCardResponse (survey tree structure)

```json
{
  "cardType": "string",
  "cardId": "string",
  "reportSubjectOpt": true|false,
  "isComplete": true|false,
  "isRoot": true|false,
  "leftChild": "card ID or null",
  "rightChild": "card ID or null",
  "middleChild": "card ID or null"
}
```

## Offers System

### POST `/offers/v2/eligible`

```json
{
  "discountReason": "string (e.g. 'new_customer', 'lapsed')"
}
```

### Response

```json
{
  "discountReason": "string",
  "duration": "string",
  "endTime": "ISO-8601",
  "id": "offer ID"
}
```

### GET `/offers/eligible` (v1)

```json
{
  "newCustomerOffers": [ /* Offer[] */ ],
  "existingCustomerOffers": [ /* Offer[] */ ]
}
```

## Offer Codes

### POST `store/v1/product/offercode/android`

```json
{
  "storefrontRegion": "US",
  "offerCode": "PROMO123"
}
```

### Response

```json
{
  "offerID": "string",
  "subscriptions": [ /* Subscription[] */ ]
}
```

## Products & Billing (store/v6/product)

### Request

```json
{
  "storefrontRegion": "US"
}
```

### Response Structure

```json
{
  "subscriptions": {
    "tier1": [ /* Hinge+ plans */ ],
    "tier2": [ /* HingeX plans */ ]
  },
  "consumables": {
    "boost": [ /* Boost packages */ ],
    "superboost": [ /* Superboost packages */ ],
    "superlike": [ /* Rose packages */ ]
  }
}
```

Each subscription plan:
```json
{
  "units": 1,
  "unitType": "month|week|quarter|...",
  "offers": [
    {
      "id": "offer ID",
      "providerDetails": {
        "google": { "externalID": "play-store-offer-id" },
        "stripe": { "couponId": "stripe-coupon" }
      },
      "personalized": true|false,
      "savingsCopyFormat": "string"
    }
  ],
  "providerDetails": {
    "google": { "sku": "play-store-sku" },
    "stripe": { "id": "stripe-price-id" }
  },
  "savingsCopyFormat": "Save X%",
  "new": true|false,
  "default": true|false,
  "valid": true|false,
  "bundle": {
    "addons": [ { "type": "boost|superlike", "units": 5 } ],
    "providerDetails": {
      "google": { "sku": "bundle-sku" },
      "stripe": { "id": "bundle-stripe-id" }
    }
  }
}
```

## Subscription Status

Sealed class with two variants:
- `None` — No subscription
- `Subscription` — Active sub with: `tier` (One/Two), `providerId`, `startDate`, `endDate`, `billingStartDate`, `units`, `unitType` (SubscriptionPeriod), `isAutoRenew`, `bundle` (addons list)

### Account History

```json
{
  "previousSubscriber": true|false,
  "previousBoostPurchaser": true|false,
  "previousSuperboostPurchaser": true|false,
  "previousSuperlikePurchaser": true|false
}
```

### Store Account

```json
{
  "subscription": { /* SubscriptionData */ },
  "account": { /* AccountHistoryData */ },
  "accountUUID": "uuid"
}
```

### SubscriptionData

```json
{
  "name": "Hinge+",
  "start": "ISO-8601",
  "end": "ISO-8601",
  "billingCycleStart": "ISO-8601",
  "trial": true|false,
  "tier": "tier1|tier2",
  "provider": "google|apple|stripe",
  "autoRenew": true|false,
  "units": 1,
  "unitType": "month",
  "bundle": { "addons": [ { "type": "boost", "units": 5 } ] }
}
```

## Priority Likes Upsell

```json
{
  "start": "ISO-8601",
  "triggerTime": "ISO-8601",
  "views": 10,
  "billingStart": "ISO-8601",
  "billingCycleViews": 50
}
```

## Auth Flow Wire Formats

### POST `identity/install`

```json
{ "installId": "uuid" }
```

### POST `auth/sms/v2` Response

```json
{
  "identityId": "uuid",
  "token": "Bearer JWT",
  "expires": "ISO-8601",
  "migratedUser": false
}
```

### POST `auth/lookup`

```json
{ "exists": true|false }
```

### POST `auth/conflict`

```json
{
  "selection": "string",
  "token": "string",
  "googleIdToken": "string"
}
```

### UntrustedDeviceResponse (412 during auth)

```json
{
  "email": "masked-email@domain.com",
  "caseId": "string"
}
```

### POST `message/authenticate` Response

```json
{
  "token": "sendbird JWT",
  "expires": "ISO-8601"
}
```

## Metrics

### POST `metric/v2`

```json
[
  {
    "id": "uuid",
    "subjectId": "related user ID or null",
    "referrerId": "referrer ID or null",
    "ts": "ISO-8601 timestamp",
    "eventType": "string (e.g. 'view_profile', 'send_like')",
    "data": { /* arbitrary event data */ },
    "crmAttributionId": "string or null"
  }
]
```

Requires `X-Session-Id` header.

## Signal

### POST `signal/v1` Response

```json
{
  "icg": "string (internal config/gate value)"
}
```

## Data Export (GDPR)

### POST `user/export`

```json
{ "type": "string (e.g. 'full')" }
```

### GET `user/export/status`

```json
{ "status": "string (e.g. 'pending', 'ready', 'expired')" }
```

---

# PaywallPlacement Enum (76 Values)

Every place in the app where a paywall can be triggered. Useful for understanding monetization touchpoints.

| Ordinal | Name | Description |
|---|---|---|
| 0 | Account | Account settings |
| 1 | AllLikesUsedDiscoverBottomSheet | Out of likes (bottom sheet) |
| 2 | AllLikesUsedDiscoverDirect | Out of likes (direct) |
| 3 | AllLikesUsedStandouts | Out of likes on Standouts |
| 4 | Banner | Generic banner upsell |
| 5 | BoostAgain | Boost again prompt |
| 6 | ChurnAlcUpsellBoost | Anti-churn boost upsell |
| 7 | ChurnAlcUpsellRose | Anti-churn rose upsell |
| 8 | DeepLink | Deep link paywall |
| 9 | DeepLinkEmail | Email deep link |
| 10 | DeepLinkPush | Push notification deep link |
| 11 | DeleteFlow | Account deletion flow |
| 12 | DiscoverFeeds | Discover feed upsell |
| 13 | DiscoverFilterActiveLately | "Active Lately" filter |
| 14-16 | DiscoverFilterDatingIntentions* | Dating intentions filter (Direct/HalfSheet/YouPick3) |
| 17-19 | DiscoverFilterHeight* | Height filter (Direct/HalfSheet/YouPick3) |
| 20 | DiscoverFilterNewHere | "New Here" filter |
| 21 | EmptyMoreStandoutsFree | Empty standouts (free tier) |
| 22 | EnhancedDiscoverDirect | Enhanced discover |
| 23 | InApp | Generic in-app |
| 24 | LastCardMoreStandoutsFree | Last standout card (free) |
| 25 | LikesYouBoost | Boost from Likes You |
| 26 | LikesYouContextualPaywall | Contextual paywall on Likes You |
| 27 | LikesYouEmptyBoost | Empty Likes You → Boost |
| 28 | LikesYouEmptyUpsell | Empty Likes You → Subscribe |
| 29 | LikesYouLockedBanner | Locked banner on Likes You |
| 30 | LikesYouLockedPhoto | Locked/blurred photo |
| 31 | LikesYouOfferFloater | Floating offer on Likes You |
| 32-34 | LikesYouSort* | Sort Likes You (Direct/HalfSheet/Type) |
| 35-36 | MatchListEmptyState* | Empty match list |
| 37 | MatchesOfferFloater | Floating offer on matches |
| 38 | MoreStandouts | More standouts |
| 39 | OfferCodeSubmitted | After offer code |
| 40 | OfferInterstitial | Offer interstitial |
| 41 | OnboardingPreferredCTA | Onboarding CTA |
| 42 | OnboardingUpsell | Onboarding upsell |
| 43-48 | OneStep* | One-step purchase flows |
| 49 | PaymentRequired | Payment required gate |
| 50 | Preferences | Preferences screen |
| 51 | PreferencesYouPickX | You Pick X preferences |
| 52 | PriorityLikesBottomSheet | Priority likes upsell |
| 53-58 | ProfileHub* | Profile hub placements (Banner/Button/OfferCard/PersistentButton/Tip/Upsell) |
| 59 | RoseEdu | Rose education |
| 60-61 | SendLike* | Send like / discover direct |
| 62 | Settings | Settings page |
| 63 | SettingsBoost | Settings → Boost |
| 64 | SettingsRestore | Settings → Restore purchase |
| 65 | SkipProfileDiscoverDirect | Skip profile upsell |
| 66 | SkipTheLineBanner | Skip the line banner |
| 67-71 | Standouts* | Standouts placements (Carousel/LikeModal/Profile/ProfileLikeModal/RoseSent) |
| 72 | TierOneEdu | Tier 1 education |
| 73 | EditProfile | Edit profile |
| 74 | EditPreferences | Edit preferences |
| 75 | Unknown | Unknown/fallback |

---

# gRPC Realtime Protocol (Wire/Proto3)

Source file: `realtime/v1/realtime.proto`
Library: Square Wire (protobuf for Kotlin/Java)

## Messages

### OpenRequest (trb)

```protobuf
message OpenRequest {
  oneof action {
    Subscribe subscribe = 1;   // a7g
    Unsubscribe unsubscribe = 2; // krh
  }
}
```

**Constraint**: At most one of `subscribe` or `unsubscribe` may be set (enforced client-side).

### OpenResponse (vrb)

```protobuf
message OpenResponse {
  Envelope envelope = 1;  // rt5
}
```

### Subscribe (a7g)

```protobuf
message Subscribe {
  ChannelSpec channel = 1;  // hb2
  int64 field2 = 2;         // unknown purpose (sequence?)
  int64 field3 = 3;         // unknown purpose (timestamp?)
}
```

### ChannelSpec (hb2, decoded from gb2 adapter)

```protobuf
message ChannelSpec {
  string name = 1;                    // channel name
  map<string, string> metadata = 2;   // channel metadata key-value pairs
}
```

## Connection Flow

1. App builds gRPC client to `https://{region}.hingeprod.net:50051`
2. Opens bidirectional streaming call
3. Sends `OpenRequest { subscribe: { channel: { name: "...", metadata: {...} } } }`
4. Receives `OpenResponse { envelope: { ... } }` with realtime events
5. To disconnect: sends `OpenRequest { unsubscribe: { ... } }`

---

# Hardcoded CDN URLs & Sample Content

```
# Voice prompt samples (per locale):
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-en-US.aac
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-en-rGB.aac
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-fr.aac
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-de.aac
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-it.aac
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-pt-br.aac
https://media.hingenexus.com/video/upload/hinge_app/20230828/sample-voice-prompt-es.aac

# Video prompt sample:
https://media.hingenexus.com/video/upload/hinge_app/20230828/video-prompt-sample.mp4
```

---

# Interesting: `If-None-Match` Header (ETags)

Both `rec/v2` and `standouts/v3` accept an `@Header("If-None-Match")` parameter.
This means the server supports **HTTP caching with ETags** for recommendations.
The response type is wrapped in `m5e<T>` which is likely a `Response<T>` wrapper that can return 304 Not Modified.

This is a significant discovery — it means:
1. Recommendations have stable ETags
2. Clients can cache and only fetch when new recommendations are available
3. The `standouts/v3` endpoint similarly supports caching

---

# Config/v3: Country Parameter

`GET config/v3` takes a `@Query("country")` parameter. The config response varies by country, suggesting:
- Different enum values per country (e.g., different religions available in different markets)
- Geographic restrictions on features
- Age-based geographic restrictions (GDPR, age of consent laws)

The `geographicRestrictions` and `geographicAgeRestrictions` fields in the response confirm this.

---

# Discover Feed Filters (mt0 enum)

| Ordinal | Name | Filter ID | Sort Priority | Subscription? | Display |
|---|---|---|---|---|---|
| 0 | Gender | 5 | 0 | Free | "Gender" |
| 1 | GenderedAge | 0 | 1 | Free | "Age" |
| 2 | GenderedHeight | 1 | 2 | Premium | "Height" |
| 3 | DatingIntentions | 2 | 3 | Premium | "Dating Intentions" |
| 4 | ActiveLately | 3 | 4 | Toggle | "Active Today" |
| 5 | NewHere | 4 | 5 | Toggle | "New Here" |

## Discover Feed SQL (from tu2.java)

```sql
SELECT profiles.*, origin, ratingToken, recommendationSource, recId
FROM discover_subject
INNER JOIN discover_batch ON discover_subject.batchId = discover_batch.id
INNER JOIN profiles USING (userId)
WHERE
    discover_batch.expiresAt > ?    -- batch not expired
    AND discover_batch.feedId = ?    -- correct feed
    AND discover_batch.filters = ?   -- matching filter set
    AND profiles.state = 1           -- active profile
    AND NOT EXISTS (
        SELECT 1 FROM pending_ratings
        WHERE discover_subject.userId = pending_ratings.subjectId
        AND (sentTime IS NULL OR sentTime > ?)
    )
ORDER BY discover_batch.id ASC, positionInBatch ASC
LIMIT ?
```

Recommendations are cached locally in `discover_batch` + `discover_subject` tables with TTL-based expiration.

## Likes You SQL (from lnd.java)

```sql
SELECT *, '' as ratingToken
FROM profiles
INNER JOIN impressions ON profiles.userId = impressions.subjectId
INNER JOIN likes_you_profile_feeds USING(userId)
WHERE feedId = ?
    AND userId NOT IN (SELECT subjectId FROM pending_ratings WHERE rating != 'skip')
    AND NOT EXISTS (SELECT 1 FROM sorted_hidden_likes_profiles WHERE profiles.userId = sorted_hidden_likes_profiles.userId)
ORDER BY sortOrder
```

**Key**: `ratingToken` empty for Likes You (uses `rate/v2/respond`). Skipped profiles reappear. Hidden likes filtered via separate table with `reason` field.

---

# Network Security

## No Certificate Pinning

All three network clients use default trust managers:
- **REST API** (`dhi.java`): connectTimeout=10s, readTimeout=0 (unlimited), no cert pinning
- **gRPC** (`t54.java`): connectTimeout=30s, readTimeout=0, pingInterval=25s, no cert pinning
- **Sendbird** (`hhi.java`): connectTimeout=10s, default OkHttpClient, no cert pinning

MITM proxies work out of the box on rooted devices.

## Client-Side Spam Detection (NOT Server-Side Enforcement)

From `wlf.java`: Tracks endpoint call counts per time window. When threshold exceeded, logs `"spam_detected"` telemetry event with `endpoint`, `count`, `threshold` — but does **NOT** block the request. Server may use these metrics to flag accounts.

---

# Database: Profiles Table (55 columns)

```sql
CREATE TABLE profiles (
    userId TEXT NOT NULL PRIMARY KEY,
    state INTEGER NOT NULL,         -- 1 = active
    firstName TEXT, lastName TEXT, height INTEGER, age INTEGER,
    gender INTEGER, genderIdentity TEXT, genderIdentityId INTEGER,
    pronouns TEXT, sexualOrientations TEXT, hometown TEXT, location TEXT,
    religion TEXT, religionText TEXT, ethnicity TEXT, ethnicitiesText TEXT,
    educationHistory TEXT, educationHistoryText TEXT, employmentHistory TEXT,
    smoking TEXT, marijuana TEXT, familyPlans TEXT,
    jobTitle TEXT, jobTitleText TEXT, didJustJoin INTEGER,
    covidVax TEXT, pet TEXT, zodiacSign TEXT,
    languagesSpoken TEXT, languagesSpokenText TEXT,
    drinking TEXT, drugs TEXT, kids TEXT,
    politics TEXT, politicsText TEXT, educationAttained TEXT,
    created INTEGER NOT NULL, updated INTEGER NOT NULL,
    compatibility INTEGER NOT NULL,  -- SERVER-ASSIGNED SCORE
    lastActiveStatusId INTEGER,
    datingIntention TEXT, datingIntentionText TEXT,
    relationshipType TEXT, relationshipTypeText TEXT,
    selfieVerified INTEGER NOT NULL DEFAULT false,
    circleMember INTEGER, photoSmartOrder TEXT
);
```

`compatibility` is a server-assigned integer score stored locally. The sorting algorithm is server-side but the score persists on device.
