from pathlib import Path

from pydantic import BaseModel

from requirements_agent.models.refinement import RefinedRequirementAnalysis


def write_json(model: BaseModel, output_path: str | Path) -> Path:
    """
    Write a Pydantic model to a JSON file.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        model.model_dump_json(indent=2),
        encoding="utf-8",
    )

    return path


def write_markdown(content: str, output_path: str | Path) -> Path:
    """
    Write markdown content to a file.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(content, encoding="utf-8")

    return path


def _format_list_section(title: str, items: list[str]) -> str:
    """
    Format a markdown section from a list of strings.
    """
    if not items:
        return f"## {title}\n\n_No items provided._\n"

    lines = [f"## {title}", ""]

    for item in items:
        lines.append(f"- {item}")

    lines.append("")
    return "\n".join(lines)


def refined_analysis_to_markdown(analysis: RefinedRequirementAnalysis) -> str:
    """
    Convert a refined requirements analysis into a human-readable markdown document.
    """
    sections = [
        "# Refined Requirements Analysis",
        "",
        "## Workflow Summary",
        "",
        analysis.workflow_summary,
        "",
        _format_list_section("Confirmed Requirements", analysis.confirmed_requirements),
        _format_list_section("Actors", analysis.actors),
        _format_list_section("Entities", analysis.entities),
        _format_list_section("Stages / Statuses", analysis.stages_statuses),
        _format_list_section("Business Rules", analysis.business_rules),
        _format_list_section("Automation Opportunities", analysis.automation_opportunities),
        _format_list_section("Assumptions", analysis.assumptions),
        _format_list_section("Unresolved Questions", analysis.unresolved_questions),
        _format_list_section("Implementation Next Steps", analysis.implementation_next_steps),
    ]

    return "\n".join(sections).strip() + "\n"