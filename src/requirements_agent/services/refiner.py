import json

from openai import RateLimitError

from requirements_agent.config import Config
from requirements_agent.llm.client import get_openai_client
from requirements_agent.llm.prompts import (
    REFINEMENT_SYSTEM_PROMPT,
    build_refinement_prompt,
)
from requirements_agent.models.refinement import (
    ClarificationAnswer,
    RefinedRequirementAnalysis,
)
from requirements_agent.models.requirements import RequirementAnalysis


def refine_analysis(
    notes: str,
    initial_analysis: RequirementAnalysis,
    clarification_answers: list[ClarificationAnswer],
) -> RefinedRequirementAnalysis:
    """
    Refine the initial structured analysis using clarification answers.
    """
    client = get_openai_client()

    prompt = build_refinement_prompt(
        notes=notes,
        initial_analysis=initial_analysis.model_dump(),
        clarification_answers=[answer.model_dump() for answer in clarification_answers],
    )

    try:
        response = client.responses.create(
            model=Config.MODEL_NAME,
            instructions=REFINEMENT_SYSTEM_PROMPT,
            input=prompt,
        )
    except RateLimitError as exc:
        raise RuntimeError(
            "OpenAI API request failed due to quota or billing limits. "
            "Verify your Platform billing, credits, and usage limits."
        ) from exc

    output_text = response.output_text
    if not output_text:
        raise ValueError("Model returned no output during refinement.")

    try:
        data = json.loads(output_text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Model returned invalid JSON during refinement. Raw output:\n{output_text}"
        ) from exc

    return RefinedRequirementAnalysis.model_validate(data)