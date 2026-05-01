from pathlib import Path

from requirements_agent.config import Config, validate_config
from requirements_agent.services.analyzer import analyze_notes
from requirements_agent.services.clarifier import collect_clarification_answers
from requirements_agent.services.ingest import read_input_file
from requirements_agent.services.refiner import refine_analysis


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "sample_data" / "inputs" / "meeting_notes_01.txt"


def main() -> None:
    validate_config()

    print("Project setup is working.")
    print(f"Model: {Config.MODEL_NAME}")

    file_contents = read_input_file(str(DEFAULT_INPUT_PATH))

    print("\n--- INPUT FILE CONTENTS ---\n")
    print(file_contents)

    initial_analysis = analyze_notes(file_contents)

    print("\n--- INITIAL STRUCTURED ANALYSIS ---\n")
    print(initial_analysis.model_dump_json(indent=2))

    clarification_answers = collect_clarification_answers(
        initial_analysis,
        max_questions=3,
    )

    if not clarification_answers:
        print("\nNo clarification answers were provided. Skipping refinement.")
        return

    refined_analysis = refine_analysis(
        notes=file_contents,
        initial_analysis=initial_analysis,
        clarification_answers=clarification_answers,
    )

    print("\n--- REFINED ANALYSIS ---\n")
    print(refined_analysis.model_dump_json(indent=2))


if __name__ == "__main__":
    main()