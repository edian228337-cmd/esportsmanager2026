"""Core architecture contracts shared across bounded contexts.

The interfaces in this module intentionally define behavior but do not implement
business logic. Concrete implementations are introduced in later phases.
"""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator, Mapping
from pathlib import Path
from typing import Any, Generic, Protocol, TypeVar

TEntity = TypeVar("TEntity")
TIdentity = TypeVar("TIdentity")


class AsyncService(ABC):
    """Lifecycle contract for asynchronous infrastructure services."""

    @abstractmethod
    async def start(self) -> None:
        """Start the service and allocate required resources."""

    @abstractmethod
    async def stop(self) -> None:
        """Stop the service and release allocated resources."""


class Repository(Protocol, Generic[TEntity, TIdentity]):
    """Generic persistence boundary used by application services."""

    async def get(self, identity: TIdentity) -> TEntity | None:
        """Return one entity by identity, or ``None`` when it does not exist."""

    async def save(self, entity: TEntity) -> None:
        """Persist an entity."""


class DataProvider(ABC, Generic[TEntity]):
    """Source adapter contract for external data providers."""

    @abstractmethod
    async def iter_entities(self) -> AsyncIterator[TEntity]:
        """Yield provider entities without leaking provider-specific transport details."""


class BinaryAssetStore(Protocol):
    """Storage boundary for binary images, logos, and generated EMDB artifacts."""

    async def put(self, path: Path, content: bytes, metadata: Mapping[str, Any]) -> None:
        """Store binary content with metadata."""

    async def get(self, path: Path) -> bytes | None:
        """Return stored binary content, or ``None`` when it does not exist."""
