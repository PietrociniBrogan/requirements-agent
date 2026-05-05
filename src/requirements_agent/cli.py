import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the requirements agent.
    """
    parser = argparse.ArgumentParser(
        description="Analyze workflow notes and produce structured requirements outputs."
    )

    parser.add_argument(
        "--input",
        "-i",
        default="sample_data/inputs/meeting_notes_01.txt",
        help="Path to the input .txt or .md file.",
    )

    parser.add_argument(
        "--output-dir",
        "-o",
        default="outputs",
        help="Directory where output files should be saved.",
    )

    parser.add_argument(
        "--max-questions",
        "-q",
        type=int,
        default=3,
        help="Maximum number of clarifying questions to ask.",
    )

    return parser.parse_args()


def resolve_project_path(project_root: Path, path_value: str) -> Path:
    """
    Resolve a user-provided path relative to the project root unless it is already absolute.
    """
    path = Path(path_value)

    if path.is_absolute():
        return path

    return project_root / path