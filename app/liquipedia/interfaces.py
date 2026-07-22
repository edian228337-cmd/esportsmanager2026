"""Liquipedia provider contracts reserved for Phase 4 implementation."""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from app.core.types import ExternalRecord


class LiquipediaClient(ABC):
    """Asynchronous Liquipedia access boundary.

    Page parsing and normalization are deferred to Phase 4; Phase 1 only defines
    the adapter seam.
    """

    @abstractmethod
    async def iter_pages(self, namespace: str) -> AsyncIterator[ExternalRecord]:
        """Yield pages for a Liquipedia namespace."""
