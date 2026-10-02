from crewai import Agent
from groq_config import get_llm


def create_market_researcher():

    return Agent(
        role="Market Researcher",

        goal="Analyze a business market briefly and clearly.",

        backstory="You are a business market researcher.",

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
