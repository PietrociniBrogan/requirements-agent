import json

from openai import RateLimitError

from requirements_agent.config import Config
from requirements_agent.llm.client import get_openai_client
from requirements_agent.llm.prompts import (
    ANALYSIS_SYSTEM_PROMPT,
    build_analysis_prompt,
)
from requirements_agent.models.requirements import RequirementAnalysis


def analyze_notes(notes: str) -> RequirementAnalysis:
    """
    Send notes to the model and return a validated structured analysis.
    """
    client = get_openai_client()
    prompt = build_analysis_prompt(notes)

    try:
        response = client.responses.create(
            model=Config.MODEL_NAME,
            instructions=ANALYSIS_SYSTEM_PROMPT,
            input=prompt,
        )
    except RateLimitError as exc:
        raise RuntimeError(
            "OpenAI API request failed due to quota or billing limits. "
            "Verify your Platform billing, credits, and usage limits."
        ) from exc

    output_text = response.output_text
    if not output_text:
        raise ValueError("Model returned no output.")

    try:
        data = json.loads(output_text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Model returned invalid JSON. Raw output:\n{output_text}"
        ) from exc

    return RequirementAnalysis.model_validate(data)