from pathlib import Path

from requirements_agent.cli import parse_args, resolve_project_path
from requirements_agent.config import Config, validate_config
from requirements_agent.services.analyzer import analyze_notes
from requirements_agent.services.clarifier import collect_clarification_answers
from requirements_agent.services.exporter import (
    refined_analysis_to_markdown,
    write_json,
    write_markdown,
)
from requirements_agent.services.ingest import read_input_file
from requirements_agent.services.refiner import refine_analysis


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    args = parse_args()
    validate_config()

    input_path = resolve_project_path(PROJECT_ROOT, args.input)
    output_dir = resolve_project_path(PROJECT_ROOT, args.output_dir)

    print("Requirements Agent")
    print(f"Model: {Config.MODEL_NAME}")
    print(f"Input file: {input_path}")
    print(f"Output directory: {output_dir}")

    file_contents = read_input_file(str(input_path))

    print("\n--- INPUT FILE CONTENTS ---\n")
    print(file_contents)

    initial_analysis = analyze_notes(file_contents)

    print("\n--- INITIAL STRUCTURED ANALYSIS ---\n")
    print(initial_analysis.model_dump_json(indent=2))

    initial_output_path = write_json(
        initial_analysis,
        output_dir / "initial_analysis.json",
    )
    print(f"\nSaved initial analysis to: {initial_output_path}")

    clarification_answers = collect_clarification_answers(
        initial_analysis,
        max_questions=args.max_questions,
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

    refined_json_path = write_json(
        refined_analysis,
        output_dir / "refined_analysis.json",
    )

    refined_markdown_path = write_markdown(
        refined_analysis_to_markdown(refined_analysis),
        output_dir / "refined_analysis.md",
    )

    print(f"\nSaved refined JSON to: {refined_json_path}")
    print(f"Saved refined Markdown to: {refined_markdown_path}")


if __name__ == "__main__":
    main()