"""HLTV provider contracts reserved for Phase 3 implementation."""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any


class HLTVClient(ABC):
    """Asynchronous HLTV access boundary."""

    @abstractmethod
    async def iter_players(self) -> AsyncIterator[Any]:
        """Yield player records from HLTV."""

    @abstractmethod
    async def iter_teams(self) -> AsyncIterator[Any]:
        """Yield team records from HLTV."""
