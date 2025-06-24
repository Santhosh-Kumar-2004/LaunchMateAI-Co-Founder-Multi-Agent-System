from google.adk.agents import Agent

class LaunchGuideAgent(Agent):
    def __init__(self):
        super().__init__(
            name="launch_guide",
            description="Recommends tools, platforms, and domain setup advice for launching.",
            instruction="Guide the user through launching their idea online: recommend tools, domains, and platform choices."
        )

    def run(self, input_data: str) -> str:
        return "🛠️ I will suggest launch tools, domain names, and tech platforms."
