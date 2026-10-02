import streamlit as st

from crew import run_business_consulting


st.set_page_config(
    page_title="Business Strategy Intelligence",
    page_icon="📊",
    layout="wide",
)


st.title("📊 Business Strategy Intelligence Team")

st.write(
    "A multi-agent AI consulting team powered by CrewAI and Groq."
)

st.divider()


st.subheader("Business Information")


business_name = st.text_input(
    "Business / Startup Name"
)


business_idea = st.text_area(
    "Describe your business idea",
    height=150,
    placeholder=(
        "Example: I want to launch a healthy packaged food "
        "brand targeting university students."
    ),
)


target_market = st.text_input(
    "Target Market",
    placeholder="Example: Pakistan"
)


budget = st.text_input(
    "Available Budget",
    placeholder="Example: PKR 5 million"
)


goals = st.text_area(
    "Business Goals",
    height=100,
    placeholder=(
        "Example: Launch MVP, acquire first 1,000 customers, "
        "and reach profitability."
    ),
)


generate = st.button(
    "🚀 Generate Business Strategy",
    type="primary",
)


if generate:

    if not business_idea.strip():

        st.error("Please describe your business idea.")

        st.stop()


    business_context = f"""
    Business Name:
    {business_name}

    Business Idea:
    {business_idea}

    Target Market:
    {target_market}

    Budget:
    {budget}

    Goals:
    {goals}
    """


    with st.spinner(
        "🤖 AI consulting team is working..."
    ):

        try:

            result = run_business_consulting(
                business_context
            )

            st.success(
                "Business strategy completed!"
            )

            st.divider()

            st.markdown(
                str(result)
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )
