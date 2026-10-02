from crewai import Agent
from groq_config import get_llm


def create_strategy_consultant():

    return Agent(
        role="Senior Business Strategy Consultant",

        goal=(
            "Transform market, customer, competitor, and financial findings "
            "into a coherent business strategy with positioning, priorities, "
            "risks, opportunities, and execution steps."
        ),

        backstory=(
            "You are a senior strategy consultant experienced in turning "
            "research into practical business decisions."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
