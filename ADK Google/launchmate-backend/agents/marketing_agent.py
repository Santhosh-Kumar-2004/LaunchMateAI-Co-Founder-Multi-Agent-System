from google.adk.agents import Agent

def marketing_content_tool(input_data: str) -> dict:
    prompt = f"""
    You're a marketing assistant. Based on:
    {input_data}

    Provide:
    - One Instagram caption (with emojis)
    - A Google/Facebook ad headline
    - A short email subject line
    """
    return {"status": "success", "report": prompt}

marketing_agent = Agent(
    name="digital_marketer",
    model="gemini-2.0-flash",
    description="Generates marketing content.",
    instruction="Generate social media and ad campaigns using the tool prompt.",
    tools=[marketing_content_tool]
)
