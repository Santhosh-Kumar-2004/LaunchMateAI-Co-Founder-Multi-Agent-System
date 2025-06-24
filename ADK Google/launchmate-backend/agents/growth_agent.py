from google.adk.agents import Agent

class GrowthConsultantAgent(Agent):
    def __init__(self):
        super().__init__(
            name="growth_consultant",
            description="Advises on growth hacks, early traction, and potential funding paths.",
            instruction="Suggest how the startup can gain early traction and explore funding or partnerships."
        )

    def run(self, input_data: str) -> str:
        return "🚀 I will suggest early growth strategies and funding options."
