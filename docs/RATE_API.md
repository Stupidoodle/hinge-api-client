# Rate / Like / Skip API

The rating system is how you interact with profiles — like, skip, or send a note (like with comment).

## Endpoint

`POST /rate/v2/initiate`

## Rating Types

| Rating | Description | Uses Like? |
|---|---|---|
| `skip` | Pass on this profile | No |
| `like` | Like a specific photo or prompt | Yes (1 daily like) |
| `note` | Like with a comment attached | Yes (1 daily like) |

## Skip Payload (Working)

```json
{
  "ratingId": "UUID (uppercase)",
  "sessionId": "{session_id}",
  "ratingToken": "{from recommendation subject}",
  "subjectId": "{subject user id}",
  "rating": "skip",
  "hasPairing": false,
  "origin": "compatibles",
  "created": "2026-03-24T19:10:42Z"
}
```

**Response:** `200 {"limit": null}`

## Like Payload (Photo)

```json
{
  "ratingId": "UUID (uppercase)",
  "sessionId": "{session_id}",
  "ratingToken": "{from recommendation subject}",
  "subjectId": "{subject user id}",
  "rating": "like",
  "hasPairing": false,
  "origin": "compatibles",
  "initiatedWith": "standard",
  "created": "2026-03-24T19:10:42Z",
  "content": {
    "photo": {
      "contentId": "{photo content_id}",
      "url": "{photo CDN url}",
      "cdnId": "{photo cdn_id}"
    }
  }
}
```

## Like Payload (Prompt/Answer)

```json
{
  "ratingId": "UUID (uppercase)",
  "sessionId": "{session_id}",
  "ratingToken": "{from recommendation subject}",
  "subjectId": "{subject user id}",
  "rating": "like",
  "hasPairing": false,
  "origin": "compatibles",
  "initiatedWith": "standard",
  "created": "2026-03-24T19:10:42Z",
  "content": {
    "prompt": {
      "answer": "{prompt response text}",
      "contentId": "{answer content_id}",
      "question": "{prompt question text}"
    }
  }
}
```

## Note Payload (Like with Comment)

Same as like but:
- `"rating": "note"` instead of `"like"`
- Add `"comment": "your message"` inside `content`
- **Requires text review first:** POST `/flag/textreview` with `{"text": "...", "receiverId": "{subject_id}"}` → returns `{"hcmRunId": "..."}`, then include `hcmRunId` in the rate payload

```json
{
  "ratingId": "UUID",
  "hcmRunId": "{from text review}",
  "sessionId": "{session_id}",
  "ratingToken": "...",
  "subjectId": "...",
  "rating": "note",
  "content": {
    "comment": "your comment here",
    "photo": { ... }
  },
  "initiatedWith": "standard",
  ...
}
```

## SuperLike Payload

Same as like but `"initiatedWith": "superlike"` instead of `"standard"`.

## Response

**Success:** `200 {"limit": {"likesLeft": N, "superlikesLeft": N}}`
**Skip:** `200 {"limit": null}` (skips don't count against limit)

## Bug in Existing Code

The `rate_user()` method in `hinge_client.py` has a bug where `CreateRateContent` passes a full Pydantic `PhotoContent` object as the `photo` field instead of a simple dict with just `contentId`, `url`, `cdnId`. The server likely rejects the extra fields (boundingBox, pHash, etc.).

**Fix:** The content.photo in the rate payload should be a minimal object:
```python
{
    "contentId": photo.content_id,
    "url": photo.url,
    "cdnId": photo.cdn_id,
}
```
Not the full `PhotoContent.model_dump()`.

## Origin Values

| Origin | Source |
|---|---|
| `compatibles` | Main recommendation feed |
| `standouts` | Standouts feed |
| `active_lately` | Recently active users feed |
| `nearby` | Nearby users feed |
| `new_here` | New users feed |

## Important Notes

- Each `ratingToken` is a **JWE** (encrypted JWT) that's single-use and tied to the subject
- `ratingId` should be a fresh UUID for each rating
- `created` timestamp must be ISO 8601 in UTC with `Z` suffix
- `hasPairing` purpose unknown — always `false`
- Skip does NOT consume a daily like
- Free account gets 8 likes/day + 1 superlike
