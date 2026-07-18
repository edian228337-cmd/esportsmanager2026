"""Liquipedia provider contracts reserved for Phase 4 implementation."""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any


class LiquipediaClient(ABC):
    """Asynchronous Liquipedia access boundary."""

    @abstractmethod
    async def iter_pages(self, namespace: str) -> AsyncIterator[Any]:
        """Yield pages for a Liquipedia namespace."""
