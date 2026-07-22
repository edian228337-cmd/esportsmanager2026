"""Application-wide exception hierarchy for EMDB Studio."""


class EMDBStudioError(Exception):
    """Base class for all expected EMDB Studio exceptions."""


class ConfigurationError(EMDBStudioError):
    """Raised when application configuration is invalid or incomplete."""


class DependencyResolutionError(EMDBStudioError):
    """Raised when a dependency cannot be resolved from the container."""
