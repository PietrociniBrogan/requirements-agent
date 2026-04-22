from openai import RateLimitError

from requirements_agent.config import Config
from requirements_agent.llm.client import get_openai_client
from requirements_agent.llm.prompts import SYSTEM_PROMPT, build_analysis_prompt


def analyze_notes(notes: str) -> str:
    """
    Analyze business notes with the configured model and return plain-text output.
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
            "OpenAI API request failed due to quota or billing limits. "
            "Verify your Platform billing, credits, and usage limits."
        ) from exc

    output_text = response.output_text
    if not output_text:
        raise ValueError("Model returned no output.")

    return output_text.strip()