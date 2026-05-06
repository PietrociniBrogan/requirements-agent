from requirements_agent.models.refinement import (
    ClarificationAnswer,
    RefinedRequirementAnalysis,
)
from requirements_agent.models.requirements import RequirementAnalysis


def test_requirement_analysis_defaults_to_empty_lists():
    analysis = RequirementAnalysis(
        workflow_summary="A workflow summary."
    )

    assert analysis.workflow_summary == "A workflow summary."
    assert analysis.actors == []
    assert analysis.entities == []
    assert analysis.clarifying_questions == []


def test_clarification_answer_stores_question_and_answer():
    answer = ClarificationAnswer(
        question="What fields are required?",
        answer="Requester, approver, and due date."
    )

    assert answer.question == "What fields are required?"
    assert answer.answer == "Requester, approver, and due date."


def test_refined_requirement_analysis_defaults_to_empty_lists():
    refined = RefinedRequirementAnalysis(
        workflow_summary="Updated workflow summary."
    )

    assert refined.workflow_summary == "Updated workflow summary."
    assert refined.confirmed_requirements == []
    assert refined.unresolved_questions == []
    assert refined.implementation_next_steps == []