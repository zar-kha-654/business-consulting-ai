from crewai import Agent
from groq_config import get_llm


def create_financial_analyst():

    return Agent(
        role="Business Model and Financial Analyst",

        goal=(
            "Analyze the proposed business model, revenue streams, pricing logic, "
            "major cost categories, unit economics, financial assumptions, "
            "and basic feasibility."
        ),

        backstory=(
            "You are a business finance consultant who evaluates business models "
            "and translates strategic ideas into understandable financial assumptions."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
