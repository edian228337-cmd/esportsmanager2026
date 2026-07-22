"""Architecture boundary tests for Phase 1."""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE_DIR = ROOT / "app" / "core"
FORBIDDEN_CORE_IMPORTS = {
    "app.cache",
    "app.compiler",
    "app.converter",
    "app.database",
    "app.hltv",
    "app.images",
    "app.liquipedia",
    "app.logos",
    "app.services",
    "app.ui",
}


def test_core_does_not_import_infrastructure_modules() -> None:
    violations: list[str] = []

    for path in CORE_DIR.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported = [node.module]
            else:
                continue

            for module in imported:
                if any(
                    module == forbidden or module.startswith(f"{forbidden}.")
                    for forbidden in FORBIDDEN_CORE_IMPORTS
                ):
                    violations.append(f"{path.relative_to(ROOT)} imports {module}")

    assert violations == []
