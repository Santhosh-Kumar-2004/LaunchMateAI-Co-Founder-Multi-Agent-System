from google.adk.agents import Agent

class ProgressTrackerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="progress_tracker",
            description="Tracks the startup’s progress and generates next-step checklists.",
            instruction="Analyze progress so far and generate an actionable checklist for what to do next."
        )

    def run(self, input_data: str) -> str:
        return "📊 I will generate a startup checklist and track the next steps."
