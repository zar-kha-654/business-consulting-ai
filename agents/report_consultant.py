from crewai import Agent
from groq_config import get_llm


def create_report_consultant():

    return Agent(
        role="Senior Business Report Consultant",

        goal=(
            "Create a professional, structured business strategy report using "
            "the research and analysis produced by the other consultants."
        ),

        backstory=(
            "You are a senior consulting report writer. "
            "You synthesize complex research into clear executive-level "
            "business reports."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False,
    )
