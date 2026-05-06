from pathlib import Path

from requirements_agent.cli import resolve_project_path


def test_resolve_project_path_returns_absolute_path_unchanged(tmp_path):
    absolute_path = tmp_path / "notes.txt"

    result = resolve_project_path(tmp_path, str(absolute_path))

    assert result == absolute_path


def test_resolve_project_path_resolves_relative_path_from_project_root(tmp_path):
    result = resolve_project_path(tmp_path, "sample_data/inputs/notes.txt")

    expected = tmp_path / "sample_data" / "inputs" / "notes.txt"

    assert result == expected