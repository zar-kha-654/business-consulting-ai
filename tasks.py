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
Analyze this business:

{business_context}

Identify:
- market
- trends
- demand
- opportunities
- barriers
- assumptions
""",

        expected_output="""
A concise market analysis containing:
- Industry overview
- Market trends
- Demand drivers
- Opportunities
- Barriers
- Important assumptions
- Research limitations

Keep the analysis concise and under 800 words.
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
A concise customer analysis containing:
- Customer segments
- Customer needs
- Pain points
- Motivations
- Objections
- Buying behavior
- Value proposition

Keep the analysis concise and under 800 words.
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
A concise competitive analysis containing:
- Direct competitors
- Indirect competitors
- Positioning
- Pricing where available
- Strengths
- Weaknesses
- Differentiation opportunities

Keep the analysis concise and under 800 words.
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
- break-even assumptions
- financial risks

Do not invent precise financial facts.
Clearly label estimates and assumptions.
""",

        expected_output="""
A concise business-model and financial analysis containing:
- Revenue streams
- Pricing logic
- Cost categories
- Unit economics assumptions
- Customer acquisition considerations
- Break-even assumptions
- Financial risks

Clearly label estimates and assumptions.
Keep the analysis concise and under 800 words.
""",

        agent=financial_agent,
    )


    strategy_task = Task(
        description="""
Develop a business strategy using the outputs from the
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
A concise business strategy containing:
- Strategic priorities
- Positioning
- Differentiation
- Growth opportunities
- Major risks
- Mitigation strategies
- Recommended experiments
- 90-day execution plan

Keep the analysis concise.
""",

        agent=strategy_agent,
    )


    report_task = Task(
        description="""
Create the final business strategy report using the
outputs from all previous consultants.

Include:

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
Clearly distinguish facts, assumptions, and recommendations.
Make the report practical and readable.
""",

        expected_output="""
A polished professional business strategy report in Markdown.

Keep the final report concise enough to avoid unnecessary
token usage while still covering all required sections.
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
