from crewai import Agent
from groq_config import get_llm


def create_market_researcher():

    return Agent(
        role="Market Research Specialist",

        goal=(
            "Research the target industry, market trends, demand conditions, "
            "growth opportunities, market barriers, and relevant business conditions."
        ),

        backstory=(
            "You are an experienced market research consultant. "
            "You analyze industries objectively and distinguish facts, "
            "assumptions, and uncertainties."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
