"""Session database model."""

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from backend.app.models.base import Base


class Session(Base):
    """Session database model."""

    __tablename__ = "sessions"  # noqa

    id = Column(Integer, primary_key=True, autoincrement=True)

    phone_number = Column(String, nullable=False, unique=True, index=True)
    device_id = Column(PG_UUID, nullable=False)
    installed = Column(Boolean, nullable=False, default=False)
    install_id = Column(PG_UUID, nullable=False)
    session_id = Column(PG_UUID, nullable=True)
    hinge_token = Column(String, nullable=True)
    hinge_token_exp = Column(DateTime, nullable=True)
    identity_id = Column(String, nullable=True)
    sendbird_token = Column(String, nullable=True)
    sendbird_token_exp = Column(DateTime, nullable=True)
    sendbird_session_key = Column(String, nullable=True)

    name = Column(String, nullable=True)
