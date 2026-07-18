"""Smoke tests for the Phase 1 architecture skeleton."""

from app.config.settings import AppSettings
from app.core.container import Container
from app.core.exceptions import DependencyResolutionError


def test_settings_exposes_derived_directories() -> None:
    settings = AppSettings()

    assert settings.cache_dir.name == "cache"
    assert settings.image_dir.name == "images"


def test_container_resolves_registered_singleton() -> None:
    container = Container()
    settings = AppSettings(environment="test")

    container.register_singleton(AppSettings, settings)

    assert container.resolve(AppSettings) is settings


def test_container_reports_missing_dependency() -> None:
    container = Container()

    try:
        container.resolve(AppSettings)
    except DependencyResolutionError as exc:
        assert "AppSettings" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("Expected missing dependency to raise")
