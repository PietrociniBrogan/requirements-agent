import pytest

from requirements_agent.services.ingest import read_input_file


def test_read_input_file_reads_txt_file(tmp_path):
    input_file = tmp_path / "notes.txt"
    input_file.write_text("These are workflow notes.", encoding="utf-8")

    result = read_input_file(str(input_file))

    assert result == "These are workflow notes."


def test_read_input_file_reads_md_file(tmp_path):
    input_file = tmp_path / "notes.md"
    input_file.write_text("# Workflow Notes", encoding="utf-8")

    result = read_input_file(str(input_file))

    assert result == "# Workflow Notes"


def test_read_input_file_raises_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        read_input_file(str(missing_file))


def test_read_input_file_raises_for_unsupported_file_type(tmp_path):
    input_file = tmp_path / "notes.pdf"
    input_file.write_text("Fake PDF content", encoding="utf-8")

    with pytest.raises(ValueError):
        read_input_file(str(input_file))