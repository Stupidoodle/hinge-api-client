"""Authentication service module."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import httpx

from backend.app.core.config import Settings, get_settings
from backend.app.core.logging_config import logger as log
from backend.app.models.session import Session as SessionModel
from backend.app.schemas.auth import SessionCreate


class AuthService:
    """Authentication service class."""

    client: httpx.AsyncClient
    hinge_db: AsyncSession
    settings: Settings

    def __init__(
        self,
        hinge_db: AsyncSession,
        client: httpx.AsyncClient,
        settings: Settings | None = None,
    ) -> None:
        """Initialise the AuthService.

        Args:
            client (httpx.AsyncClient): HTTP client for making requests.
            hinge_db (AsyncSession): Database session for Hinge.
            settings (Settings | None): Application settings.

        """
        self.client = client
        self.hinge_db = hinge_db
        self.settings = settings or get_settings()

    async def get_session_from_name_or_id(
        self, session_id: int | None = None, session_name: str | None = None
    ) -> int | None:
        """Get session by name or ID.

        Args:
            session_id (int | None): Session ID.
            session_name (str | None): Session name.

        Returns:
            int | None: Session ID if found, else None.

        """
        if not session_id and not session_name:
            log.warning("auth.get_session_from_name_or_id.missing_params")
            return None

        stmt = select(SessionModel)

        if session_id:
            stmt = stmt.where(SessionModel.id == session_id)
        else:
            stmt = stmt.where(SessionModel.name == session_name)

        result = await self.hinge_db.execute(stmt)

        session = result.scalars().first()

        return int(session.id) if session else None

    async def get_session_headers(self, session_id: int) -> dict[str, str]:
        """Get headers for a session.

        Args:
            session_id (int): Session ID.

        Returns:
            dict[str, str]: Headers for the session ID.

        """
        headers = {
            "X-Device-Platform": "iOS",
            "User-Agent": f"Hinge/{self.settings.HINGE_BUILD_NUMBER} "
            f"CFNetwork/3857.100.1 Darwin/25.0.0",
            "Accept": "*/*",
            "Accept-Language": "en-GB",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json",
            "X-Device-Model-Code": "iPhone16,1",
            "X-Device-Model": "unknown",
            "X-Device-Region": "FR",
            "X-App-Version": self.settings.HINGE_APP_VERSION,
            "X-Build-Number": self.settings.HINGE_BUILD_NUMBER,
            "X-OS-Version": self.settings.OS_VERSION,
        }

        db_session = await self.hinge_db.execute(
            select(SessionModel).where(SessionModel.id == session_id)
        )

        session = db_session.scalars().first()

        if session is None:
            log.error(
                "auth.get_session_headers.session_not_found", session_id=session_id
            )
            return headers

        headers.update(
            {
                "X-Session-Id": str(session.session_id),
                "X-Device-Id": str(session.device_id),
                "X-Install-Id": str(session.install_id),
            }
        )

        if session.hinge_token:
            headers["Authorization"] = f"Bearer {session.hinge_token}"

        return headers

    async def create_session(self, payload: SessionCreate) -> None:
        """Create a new session.

        Args:
            payload (SessionCreate): Payload for creating a session.

        Raises:
            Exception: If session creation fails.

        """
        db_session = SessionModel(**payload.model_dump())

        try:
            self.hinge_db.add(db_session)
            await self.hinge_db.commit()
            await self.hinge_db.refresh(db_session)
            log.info("auth.create_session.success", session_id=db_session.id)
        except Exception as e:
            raise e

    async def authenticate_session(
        self, session_id: int | None, session_name: str | None
    ) -> None:
        """Authenticate a session by ID or name.

        Args:
            session_id (int | None): Session ID.
            session_name (str | None): Session name.

        """
