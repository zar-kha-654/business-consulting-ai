from crewai import Task


def create_tasks(
    market_agent,
    customer_agent,
    competitor_agent,
    financial_agent,
    strategy_agent,
    report_agent,
    business_context,
):

    market_task = Task(
        description=f"""
        Analyze the market for the following business:

        {business_context}

        Research:
        - industry conditions
        - market trends
        - demand drivers
        - opportunities
        - barriers
        - important assumptions
        - uncertainties

        Clearly distinguish facts from assumptions.
        """,

        expected_output="""
        A structured market analysis containing:
        1. Industry overview
        2. Market trends
        3. Demand drivers
        4. Opportunities
        5. Barriers
        6. Important assumptions
        7. Research limitations
        """,

        agent=market_agent,
    )

    customer_task = Task(
        description=f"""
        Analyze the target customers for this business:

        {business_context}

        Identify:
        - customer segments
        - primary target customer
        - customer needs
        - pain points
        - buying motivations
        - objections
        - purchasing behavior
        - potential value proposition
        """,

        expected_output="""
        A structured customer analysis with customer segments,
        pain points, motivations, objections, buying behavior,
        and potential value propositions.
        """,

        agent=customer_agent,
    )

    competitor_task = Task(
        description=f"""
        Conduct competitive analysis for:

        {business_context}

        Identify:
        - direct competitors
        - indirect competitors
        - competitor positioning
        - pricing approaches where available
        - strengths
        - weaknesses
        - differentiation opportunities
        """,

        expected_output="""
        A structured competitive landscape analysis with
        competitors, positioning, strengths, weaknesses,
        and potential differentiation opportunities.
        """,

        agent=competitor_agent,
    )

    financial_task = Task(
        description=f"""
        Analyze the business model and financial logic for:

        {business_context}

        Evaluate:
        - revenue streams
        - pricing logic
        - major cost categories
        - unit economics assumptions
        - customer acquisition considerations
        - break-even assumptions where possible
        - financial risks

        Do not invent precise financial facts.
        Clearly label estimates and assumptions.
        """,

        expected_output="""
        A structured business-model and financial analysis
        containing revenue streams, pricing logic, cost
        categories, assumptions, risks, and feasibility considerations.
        """,

        agent=financial_agent,
    )

    strategy_task = Task(
        description="""
        Develop a business strategy using the outputs of the
        market, customer, competitor, and financial analysts.

        Create:
        - strategic priorities
        - positioning
        - differentiation
        - growth opportunities
        - major risks
        - mitigation approaches
        - recommended experiments
        - 90-day execution plan
        """,

        expected_output="""
        A coherent business strategy containing strategic priorities,
        positioning, differentiation, opportunities, risks,
        mitigation strategies, experiments, and a 90-day plan.
        """,

        agent=strategy_agent,
    )

    report_task = Task(
        description="""
        Create the final business strategy report using all previous
        consultant outputs.

        The report must contain:

        1. Executive Summary
        2. Business Overview
        3. Market Analysis
        4. Customer Analysis
        5. Competitive Landscape
        6. Business Model
        7. Financial Considerations
        8. SWOT Analysis
        9. Strategic Priorities
        10. Risks and Mitigation
        11. 90-Day Action Plan
        12. Key Assumptions
        13. Research Limitations

        Do not present uncertain information as established fact.
        Make the report practical and readable.
        """,

        expected_output="""
        A polished professional business strategy report in Markdown.
        """,

        agent=report_agent,
    )

    return [
        market_task,
        customer_task,
        competitor_task,
        financial_task,
        strategy_task,
        report_task,
    ]
