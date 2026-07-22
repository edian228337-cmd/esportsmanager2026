"""Reusable base classes for Phase 1 architecture skeleton."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class Entity:
    """Base immutable domain entity.

    Domain-specific attributes are deliberately deferred to later phases.
    """

    id: str


@dataclass(slots=True)
class ValueObject:
    """Marker base class for immutable concepts without identity."""


@dataclass(slots=True)
class UseCaseResult:
    """Standard result envelope for application use cases."""

    success: bool
    message: str
    details: dict[str, Any] = field(default_factory=dict)
