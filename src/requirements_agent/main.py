from requirements_agent.config import Config, validate_config
from requirements_agent.services.ingest import read_input_file


DEFAULT_INPUT_PATH = "sample_data/inputs/meeting_notes_01.txt"


def main() -> None:
    validate_config()

    print("Project setup is working.")
    print(f"Model: {Config.MODEL_NAME}")

    file_contents = read_input_file(DEFAULT_INPUT_PATH)

    print("\n--- INPUT FILE CONTENTS ---\n")
    print(file_contents)


if __name__ == "__main__":
    main()