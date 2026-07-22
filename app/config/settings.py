"""Configuration primitives for EMDB Studio.

The Phase 1 settings model is dependency-free so architectural imports and tests
work before third-party packages are installed. Phase 2 can adapt the same
boundary to Pydantic Settings without changing consumers.
"""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True, frozen=True)
class PathSettings:
    """Filesystem locations used by the application."""

    data_dir: Path = Path(".emdb-studio")

    @property
    def cache_dir(self) -> Path:
        """Return the provider/cache storage directory."""

        return self.data_dir / "cache"

    @property
    def image_dir(self) -> Path:
        """Return the image asset storage directory."""

        return self.data_dir / "images"

    @property
    def export_dir(self) -> Path:
        """Return the generated EMDB export directory."""

        return self.data_dir / "exports"


@dataclass(slots=True, frozen=True)
class DatabaseSettings:
    """Database connection configuration boundary."""

    url: str = "sqlite+aiosqlite:///.emdb-studio/emdb-studio.sqlite3"
    echo_sql: bool = False


@dataclass(slots=True, frozen=True)
class ProviderSettings:
    """External provider policy knobs shared by future adapters."""

    request_timeout_seconds: float = 30.0
    max_retries: int = 3
    requests_per_second: float = 1.0


@dataclass(slots=True, frozen=True)
class AppSettings:
    """Root application settings passed through dependency injection."""

    app_name: str = "EMDB Studio"
    environment: str = "development"
    log_level: str = "INFO"
    paths: PathSettings = field(default_factory=PathSettings)
    database: DatabaseSettings = field(default_factory=DatabaseSettings)
    providers: ProviderSettings = field(default_factory=ProviderSettings)

    @property
    def data_dir(self) -> Path:
        """Backward-compatible shortcut for the root data directory."""

        return self.paths.data_dir

    @property
    def cache_dir(self) -> Path:
        """Return the default cache directory."""

        return self.paths.cache_dir

    @property
    def image_dir(self) -> Path:
        """Return the default image directory."""

        return self.paths.image_dir
