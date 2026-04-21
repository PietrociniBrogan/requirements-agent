from pathlib import Path


ALLOWED_EXTENSIONS = {".txt", ".md"}


def read_input_file(file_path: str) -> str:
    """
    Read a supported text file and return its contents.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {path.suffix}. Supported types: {ALLOWED_EXTENSIONS}"
        )

    return path.read_text(encoding="utf-8").strip()