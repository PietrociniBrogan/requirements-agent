import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


def validate_config() -> None:
    if not Config.OPENAI_API_KEY:
        raise ValueError("Missing OPENAI_API_KEY in .env")