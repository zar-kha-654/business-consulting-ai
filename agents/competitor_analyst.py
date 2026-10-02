from crewai import Agent
from groq_config import get_llm


def create_competitor_analyst():

    return Agent(
        role="Competitive Intelligence Analyst",

        goal=(
            "Identify relevant competitors, their products, pricing, positioning, "
            "distribution strategies, strengths, weaknesses, and market gaps."
        ),

        backstory=(
            "You are a competitive intelligence specialist. "
            "You compare businesses objectively and identify opportunities "
            "for differentiation."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
