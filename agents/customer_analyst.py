from crewai import Agent
from groq_config import get_llm


def create_customer_analyst():

    return Agent(
        role="Customer and Consumer Analyst",

        goal=(
            "Identify the target customer segments, customer needs, pain points, "
            "buying motivations, objections, preferences, and purchasing behavior."
        ),

        backstory=(
            "You are a customer research consultant specializing in segmentation, "
            "consumer behavior, customer problems, and value propositions."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
