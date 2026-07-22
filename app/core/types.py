"""Shared type aliases and provider-neutral records for architecture boundaries."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any, NewType

EntityId = NewType("EntityId", str)
ExternalId = NewType("ExternalId", str)


class ProviderName(StrEnum):
    """Known external data providers supported by the architecture."""

    HLTV = "hltv"
    LIQUIPEDIA = "liquipedia"


@dataclass(slots=True, frozen=True)
class ExternalRecord:
    """Provider-neutral data envelope crossing adapter boundaries.

    The payload remains intentionally unmodeled in Phase 1. Later phases will
    introduce validated DTOs per provider and domain concept.
    """

    provider: ProviderName
    external_id: ExternalId
    payload: dict[str, Any] = field(default_factory=dict)
