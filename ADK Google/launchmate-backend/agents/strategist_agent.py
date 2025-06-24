# from google.adk.agents import Agent

# def suggest_startup_tool(input_data: str) -> dict:
#     prompt = f"""
#     You're a startup strategist. Given:
#     {input_data}

#     Please output:
#     1. Business model idea
#     2. Two to three product ideas
#     3. A branding direction
#     4. A catchy startup name
#     """
#     return {"status": "success", "report": prompt}

# strategist_agent = Agent(
#     name="startup_strategist",
#     model="gemini-2.0-pro",
#     description="Suggests startup ideas and branding.",
#     instruction="Use the tool to provide startup concept, products, branding, and name.",
#     tools=[suggest_startup_tool]
# )


from google.adk.agents import Agent
from google.adk.tools.function_tool import FunctionTool # Import FunctionTool

def suggest_startup_logic(input_data: str) -> dict:
    """
    This function defines the actual logic for generating startup suggestions.
    It will be called by the LLM when the Agent decides to use this tool.
    """
    prompt = f"""
    You're a startup strategist. Given the business goal or idea:
    "{input_data}"

    Please provide:
    1. A viable business model
    2. Two to three product ideas
    3. A branding approach
    4. A creative and catchy startup name
    """
    # In a real scenario, you'd call an LLM here or generate a structured response.
    # For now, we'll just return the prompt as a "report".
    # The ADK agent will then use this "report" to formulate its final response.
    return {"status": "success", "report": prompt}

# Wrap your function with FunctionTool so the ADK recognizes it as a callable tool
suggest_startup_tool = FunctionTool(
    # name="suggest_startup", # A unique name for your tool
    # description="Provides startup ideas, business models, product concepts, branding, and names.",
    # function=suggest_startup_logic # The actual Python function to execute
    func=suggest_startup_logic, # The function to call
)

strategist_agent = Agent(
    name="startup_strategist",
    model="gemini-2.0-pro", # You can also use "gemini-2.0-flash" for faster responses
    description="Suggests comprehensive startup ideas and branding strategies.",
    instruction="Given a user's business goal or idea, use the 'suggest_startup' tool to generate a detailed startup concept, including business model, product ideas, branding direction, and a catchy name. Ensure the output is well-structured and creative.",
    tools=[suggest_startup_tool] # Pass the wrapped FunctionTool here
)