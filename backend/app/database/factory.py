"""Database session factory module."""

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)

from backend.app.database.config import DatabaseConfig


def build_session_factory(config: DatabaseConfig) -> async_sessionmaker[AsyncSession]:
    """Create an async session factory.

    Args:
        config: Database configuration object.

    Returns:
        async_sessionmaker[AsyncSession]: Session factory.

    """
    async_engine = create_async_engine(
        url=config.url,
        pool_size=config.pool_size,
        max_overflow=config.max_overflow,
        pool_timeout=config.pool_timeout,
        pool_pre_ping=True,
    )

    return async_sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
