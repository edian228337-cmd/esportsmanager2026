"""Minimal dependency container contract for Phase 1.

The container records factories and singleton instances without constructing
phase-specific services. It is intentionally small and explicit.
"""

from collections.abc import Callable
from typing import Any, TypeVar, cast

from app.core.exceptions import DependencyResolutionError

T = TypeVar("T")
Factory = Callable[["Container"], Any]


class Container:
    """Simple dependency injection container used at composition roots."""

    def __init__(self) -> None:
        self._factories: dict[type[Any], Factory] = {}
        self._singletons: dict[type[Any], Any] = {}

    def register_factory(self, contract: type[T], factory: Callable[["Container"], T]) -> None:
        """Register a factory for a contract."""

        self._factories[contract] = factory

    def register_singleton(self, contract: type[T], instance: T) -> None:
        """Register an already-created singleton instance for a contract."""

        self._singletons[contract] = instance

    def resolve(self, contract: type[T]) -> T:
        """Resolve a contract or raise a descriptive architecture error."""

        if contract in self._singletons:
            return cast(T, self._singletons[contract])
        if contract in self._factories:
            return cast(T, self._factories[contract](self))
        raise DependencyResolutionError(f"No dependency registered for {contract.__qualname__}")
