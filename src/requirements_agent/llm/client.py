from openai import OpenAI

from requirements_agent.config import Config


def get_openai_client() -> OpenAI:
    """
    Create and return an OpenAI client.
    """
    return OpenAI(api_key=Config.OPENAI_API_KEY)