"""HLTV provider contracts reserved for Phase 3 implementation."""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from app.core.types import ExternalRecord


class HLTVClient(ABC):
    """Asynchronous HLTV access boundary.

    Methods expose provider-neutral records in Phase 1. Typed provider DTOs will
    be introduced with parser implementations in Phase 3.
    """

    @abstractmethod
    async def iter_players(self) -> AsyncIterator[ExternalRecord]:
        """Yield player records from HLTV."""

    @abstractmethod
    async def iter_teams(self) -> AsyncIterator[ExternalRecord]:
        """Yield team records from HLTV."""
