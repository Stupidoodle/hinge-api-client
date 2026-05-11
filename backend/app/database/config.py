"""Database configuration schema."""

from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseConfig:
    """Database configuration class."""

    url: str
    pool_size: int
    max_overflow: int
    pool_timeout: int
