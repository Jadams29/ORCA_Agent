import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agents import OrcaAgent

load_dotenv()

# --- Main Execution ---
if __name__ == "__main__":
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY environment variable not set.")

    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)

    # Instantiate the agent and get the compiled graph
    orca_agent = OrcaAgent(llm)
    app = orca_agent.get_graph()

    # Define the initial problem
    # Using the example from the blueprint
    initial_prompt_example = "Write about our new shoes."
    user_goal_example = "Make this a good prompt for generating exciting social media posts for Instagram."

    # Set up the initial state
    initial_state = {
        "initial_prompt": initial_prompt_example,
        "user_goal": user_goal_example,
        "decomposed_goals": [],
        "evaluation_criteria": [],
        "prompt_candidates": [],
        "iteration_count": 0,
        "final_prompt": "",
        "final_rationale": {}
    }

    print("--- STARTING ORCA AGENT ---")
    # Run the agent
    final_state = app.invoke(initial_state)

    print("\n\n--- ORCA AGENT FINISHED ---")
    print("\n--- FINAL REPORT ---")
    print(f"\nOptimized Prompt:\n{'-' * 20}\n{final_state['final_rationale']['final_prompt']}")
    print(f"\nExecutive Summary:\n{'-' * 20}\n{final_state['final_rationale']['executive_summary']}")
    print(f"\nDetailed Rationale:\n{'-' * 20}")
    for criterion_id, justification in final_state['final_rationale']['detailed_rationale'].items():
        print(f"- {criterion_id.replace('_', ' ').title()}: {justification}")
