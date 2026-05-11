"""Pydantic models for auth related stuff."""

from pydantic import BaseModel, Field, UUID4
from pydantic_extra_types.phone_numbers import PhoneNumber
import uuid


class SessionCreate(BaseModel):
    """Schema for creating a session."""

    phone_number: PhoneNumber
    device_id: UUID4 = Field(default_factory=uuid.uuid4)
    install_id: UUID4 = Field(default_factory=uuid.uuid4)
    session_id: UUID4 = Field(default_factory=uuid.uuid4)

    name: str | None = None
