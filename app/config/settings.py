"""Configuration primitives for EMDB Studio.

This module provides a dependency-free configuration model for Phase 1 so the
architecture can be imported and validated before third-party packages are
installed. Later phases may adapt this boundary to Pydantic Settings.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True, frozen=True)
class AppSettings:
    """Root application settings shared across infrastructure components."""

    app_name: str = "EMDB Studio"
    environment: str = "development"
    data_dir: Path = Path(".emdb-studio")
    database_url: str = "sqlite+aiosqlite:///.emdb-studio/emdb-studio.sqlite3"
    log_level: str = "INFO"

    @property
    def cache_dir(self) -> Path:
        """Return the default cache directory."""

        return self.data_dir / "cache"

    @property
    def image_dir(self) -> Path:
        """Return the default image directory."""

        return self.data_dir / "images"
