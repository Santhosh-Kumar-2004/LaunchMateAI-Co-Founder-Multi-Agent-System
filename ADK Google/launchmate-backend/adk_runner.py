# from agents.strategist_agent import strategist_agent

# def main():
#     user_input = "I want to start an eco-friendly T-shirt brand for college students."

#     print("🧠 Running Startup Strategist Agent...\n")
#     response = strategist_agent.start(user_input)
#     print(response.text)

# if __name__ == "__main__":
#     main()



from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.messages import UserMessage # <--- RE-ENABLE THIS IMPORT
from agents.strategist_agent import strategist_agent
import asyncio

async def main():
    raw_user_input = "I want to start an eco-friendly T-shirt brand for college students."

    # Use the UserMessage object as intended by the ADK
    user_message = UserMessage(text=raw_user_input) # <--- Use UserMessage here

    # Initialize a session service
    session_service = InMemorySessionService()

    # Define user_id, session_id, and app_name
    user_id = "user_abc_123"
    session_id = "session_xyz_456"
    app_name = "startup_launchmate"

    # Explicitly create the session before using it with the runner
    print(f"🔄 Creating session: app_name='{app_name}', user_id='{user_id}', session_id='{session_id}'")
    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )
    print(f"✅ Session created successfully.")

    # Create a Runner instance, associating it with your agent
    runner = Runner(
        agent=strategist_agent,
        app_name=app_name,
        session_service=session_service
    )

    print("🧠 Running Startup Strategist Agent...\n")

    # Pass the UserMessage object to new_message
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=user_message # <--- Pass the UserMessage object here
    )

    final_response_text = ""
    async for event in events:
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            else:
                final_response_text = "Agent completed, but no text content found in final response."
            break
        elif event.is_tool_code_execution():
            print(f"🔵 Tool executed: {event.tool_code_execution.tool_name}")
            if event.tool_code_execution.output:
                print(f"   Tool output: {event.tool_code_execution.output}")
        elif event.is_model_response() and event.model_response.text:
            print(f"🟡 Model thought: {event.model_response.text[:100]}...")

    print(f"✅ Strategist Output:\n{final_response_text}")

if __name__ == "__main__":
    asyncio.run(main())