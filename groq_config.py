import os
from crewai import LLM


MODEL_NAME = "openai/gpt-oss-120b"


def get_llm():
    return LLM(
        model=MODEL_NAME,
        custom_openai=True,
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2,
    )
