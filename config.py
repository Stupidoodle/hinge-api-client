"""Settings for the application."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # --- Constants & Configuration ---
    # You didn't think I'd hardcode this shit, did you?
    BASE_URL = "https://prod-api.hingeaws.net"
    SENDBIRD_API_URL = "https://api-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9.sendbird.com"
    SENDBIRD_WS_URL = "wss://ws-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9.sendbird.com"
    SENDBIRD_APP_ID = "3CDAD91C-1E0D-4A0D-BBEE-9671988BF9E9"
