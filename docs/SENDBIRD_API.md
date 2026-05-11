# Sendbird REST API (Chat Infrastructure)

Hinge uses Sendbird for all chat functionality. The REST API is accessible with the session key.

## Base URL
`https://api-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9.sendbird.com`

## Auth

**Session-Key auth works (JWT does NOT):**
```
Session-Key: {sendbird_session_key}
Content-Type: application/json
```

The `Api-Token` header (used with Sendbird JWT) returns 400. Use `Session-Key` instead.

## Working Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | `/v3/users/{uid}` | User info (nickname, online status, created_at) |
| GET | `/v3/users/{uid}/my_group_channels?show_member=true&limit=100` | **Match list** (group channels = conversations) |
| GET | `/v3/users/{uid}/unread_channel_count` | Unread conversation count |
| GET | `/v3/users/{uid}/unread_message_count` | Unread message count |
| GET | `/v3/users/{uid}/push_preference` | Push notification settings |
| GET | `/v3/users/{uid}/metadata` | User metadata (empty on this account) |
| GET | `/v3/users/{uid}/block` | Blocked users list |

## User Response
```json
{
  "user_id": "3852749922507949139",
  "nickname": "",
  "profile_url": "",
  "require_auth_for_profile_image": false,
  "metadata": {},
  "access_token": "",
  "created_at": 1773504768,
  "discovery_keys": [],
  "is_hide_me_from_friends": false,
  "session_tokens": [],
  "is_online": false,
  "last_seen_at": -1,
  "is_active": true,
  "has_ever_logged_in": true,
  "preferred_languages": [],
  "locale": ""
}
```

## Group Channels (Matches)

Each match in Hinge creates a Sendbird group channel. The channel list endpoint returns all matches with their messages.

```json
{
  "channels": [
    // Each channel = one match
    // Contains: channel_url, members[], last_message, unread_message_count, etc.
  ],
  "next": "",  // pagination cursor
  "ts": 1774379262800  // server timestamp
}
```

**Note:** This account has no matches yet, so channels array is empty. When matches exist, each channel will contain:
- `channel_url` — unique channel identifier
- `members[]` — array of user objects in the conversation
- `last_message` — most recent message object
- `unread_message_count` — per-channel unread count
- `created_at` — when the match was made
- `data` — custom JSON data (Hinge may store match metadata here)

## Push Preferences
```json
{
  "do_not_disturb": false,
  "start_hour": 0,
  "start_min": 0,
  "end_hour": 0,
  "end_min": 0,
  "timezone": "UTC",
  "push_sound": "default",
  "push_trigger_option": "all",
  "snooze_enabled": false,
  "block_push_from_bots": false,
  "enable_push_for_replies": true
}
```

## Additional Sendbird Endpoints to Explore (with matches)

These are standard Sendbird REST API endpoints that should work:
- `GET /v3/group_channels/{channel_url}` — channel details
- `GET /v3/group_channels/{channel_url}/messages` — message history
- `POST /v3/group_channels/{channel_url}/messages` — send message
- `GET /v3/group_channels/{channel_url}/members` — channel members
- `PUT /v3/users/{uid}/push_preference` — update push settings
- `PUT /v3/group_channels/{channel_url}/hide` — hide conversation
- `DELETE /v3/group_channels/{channel_url}/messages/{message_id}` — delete message

## Key Insight

Since Sendbird is standard 3rd-party infrastructure with well-documented APIs, we can:
1. List all matches (group channels)
2. Read full message history
3. Send messages programmatically
4. Get read receipts and typing indicators
5. Manage push notifications
6. Block/unblock users at the chat level

This is much more accessible than Bumble's proprietary Comet SSE system.
