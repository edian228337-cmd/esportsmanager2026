"""Database boundary abstractions."""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any


class UnitOfWork(ABC):
    """Transaction boundary for repositories."""

    @abstractmethod
    async def __aenter__(self) -> "UnitOfWork":
        """Enter a transaction scope."""

    @abstractmethod
    async def __aexit__(self, exc_type: type[BaseException] | None, exc: BaseException | None, tb: Any) -> None:
        """Exit a transaction scope, committing or rolling back as appropriate."""


class DatabaseSessionProvider(ABC):
    """Boundary for asynchronous database sessions."""

    @abstractmethod
    def session(self) -> AsyncIterator[Any]:
        """Return an asynchronous session iterator."""
