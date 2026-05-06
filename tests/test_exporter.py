import json

from requirements_agent.models.refinement import RefinedRequirementAnalysis
from requirements_agent.services.exporter import (
    refined_analysis_to_markdown,
    write_json,
    write_markdown,
)


def make_sample_refined_analysis() -> RefinedRequirementAnalysis:
    return RefinedRequirementAnalysis(
        workflow_summary="A refined workflow summary.",
        confirmed_requirements=[
            "Requests must be submitted through a form.",
            "Manager approval is required.",
        ],
        actors=["Submitter", "Manager"],
        entities=["Request"],
        stages_statuses=["Submitted", "Approved"],
        business_rules=["Only approved requests move to fulfillment."],
        automation_opportunities=["Send approval notifications."],
        assumptions=["Notifications are sent by email."],
        unresolved_questions=["What are the SLA targets?"],
        implementation_next_steps=["Define the request form fields."],
    )


def test_write_json_creates_json_file(tmp_path):
    analysis = make_sample_refined_analysis()
    output_path = tmp_path / "refined_analysis.json"

    result_path = write_json(analysis, output_path)

    assert result_path == output_path
    assert output_path.exists()

    data = json.loads(output_path.read_text(encoding="utf-8"))

    assert data["workflow_summary"] == "A refined workflow summary."
    assert data["confirmed_requirements"] == [
        "Requests must be submitted through a form.",
        "Manager approval is required.",
    ]


def test_refined_analysis_to_markdown_formats_sections():
    analysis = make_sample_refined_analysis()

    markdown = refined_analysis_to_markdown(analysis)

    assert "# Refined Requirements Analysis" in markdown
    assert "## Workflow Summary" in markdown
    assert "A refined workflow summary." in markdown
    assert "## Confirmed Requirements" in markdown
    assert "- Requests must be submitted through a form." in markdown
    assert "## Implementation Next Steps" in markdown


def test_write_markdown_creates_markdown_file(tmp_path):
    output_path = tmp_path / "refined_analysis.md"

    result_path = write_markdown("# Test Markdown\n", output_path)

    assert result_path == output_path
    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == "# Test Markdown\n"