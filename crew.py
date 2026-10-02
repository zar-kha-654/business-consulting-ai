from crewai import Crew, Process

from agents.market_researcher import create_market_researcher


def run_business_consulting(business_context):

    market_agent = create_market_researcher()

    task = {
        "description": f"""
Analyze this business:

{business_context}

Give a short market analysis covering:
- target market
- major trends
- opportunities
- risks

Keep the response under 500 words.
""",
        "expected_output": "A concise market analysis under 500 words.",
    }

    from crewai import Task

    market_task = Task(
        description=task["description"],
        expected_output=task["expected_output"],
        agent=market_agent,
    )

    crew = Crew(
        agents=[market_agent],
        tasks=[market_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()

    return result
