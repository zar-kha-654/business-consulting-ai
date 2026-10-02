from crewai import Crew, Process

from agents.market_researcher import create_market_researcher
from agents.customer_analyst import create_customer_analyst
from agents.competitor_analyst import create_competitor_analyst
from agents.financial_analyst import create_financial_analyst
from agents.strategy_consultant import create_strategy_consultant
from agents.report_consultant import create_report_consultant

from tasks import create_tasks


def run_business_consulting(business_context):

    market_agent = create_market_researcher()
    customer_agent = create_customer_analyst()
    competitor_agent = create_competitor_analyst()
    financial_agent = create_financial_analyst()
    strategy_agent = create_strategy_consultant()
    report_agent = create_report_consultant()

    tasks = create_tasks(
        market_agent,
        customer_agent,
        competitor_agent,
        financial_agent,
        strategy_agent,
        report_agent,
        business_context,
    )

    crew = Crew(
        agents=[
            market_agent,
            customer_agent,
            competitor_agent,
            financial_agent,
            strategy_agent,
            report_agent,
        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=True,
    )

    result = crew.kickoff()

    return result
