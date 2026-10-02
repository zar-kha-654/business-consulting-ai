from crewai import Agent

from groq_config import get_llm
from tools.web_research_tool import WebResearchTool


def create_market_researcher():

    return Agent(

        role="Market Research Specialist",

        goal=(
            "Research the target industry and identify "
            "important market opportunities and risks."
        ),

        backstory=(
            "You are an experienced market research consultant."
        ),

        llm=get_llm(),

        tools=[
            WebResearchTool()
        ],

        verbose=True,

        allow_delegation=False,
    )
