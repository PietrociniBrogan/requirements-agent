from pathlib import Path

from requirements_agent.config import Config, validate_config
from requirements_agent.services.ingest import read_input_file
from requirements_agent.services.analyzer import analyze_notes


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "sample_data" / "inputs" / "meeting_notes_01.txt"


def main() -> None:
    validate_config()

    print("Project setup is working.")
    print(f"Model: {Config.MODEL_NAME}")

    file_contents = read_input_file(str(DEFAULT_INPUT_PATH))

    print("\n--- INPUT FILE CONTENTS ---\n")
    print(file_contents)

    analysis = analyze_notes(file_contents)

    print("\n--- AI ANALYSIS ---\n")
    print(analysis)


if __name__ == "__main__":
    main()