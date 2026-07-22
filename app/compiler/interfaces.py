"""EMDB compiler contracts reserved for reverse engineering phases."""

from abc import ABC, abstractmethod
from pathlib import Path


class EMDBReader(ABC):
    """Boundary for reading `.emdb` files."""

    @abstractmethod
    async def read(self, path: Path) -> bytes:
        """Read raw EMDB bytes."""


class EMDBWriter(ABC):
    """Boundary for writing `.emdb` files."""

    @abstractmethod
    async def write(self, path: Path, content: bytes) -> None:
        """Write raw EMDB bytes."""
