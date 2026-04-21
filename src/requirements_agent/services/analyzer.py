from openai import RateLimitError

from requirements_agent.config import Config
from requirements_agent.llm.client import get_openai_client
from requirements_agent.llm.prompts import SYSTEM_PROMPT, build_analysis_prompt


def analyze_notes(notes: str) -> str:
    """
    Send notes to the model and return a first-pass analysis as text.
    """
    client = get_openai_client()
    prompt = build_analysis_prompt(notes)

    try:
        response = client.responses.create(
            model=Config.MODEL_NAME,
            instructions=SYSTEM_PROMPT,
            input=prompt,
        )
    except RateLimitError as exc:
        raise RuntimeError(
            "OpenAI API request failed due to quota/billing limits. "
            "Check your Platform billing, credits, and API usage limits."
        ) from exc

    if not response.output_text:
        raise ValueError("Model returned no output.")

    return response.output_text.strip()