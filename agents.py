import json
import os
from typing import Literal

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from state import AgentState
from tools import (GoalDecomposer, CriteriaGenerator, PromptIdeator, PromptEvaluator, ReportGenerator)

# Example: os.environ = "YOUR_API_KEY"
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Configuration ---
MAX_ITERATIONS = 4
QUALITY_THRESHOLD = 0.95  # 95% of max possible score


class OrcaAgent:
    def __init__(self, llm):
        self.goal_decomposer = GoalDecomposer(llm)
        self.criteria_generator = CriteriaGenerator(llm)
        self.prompt_ideator = PromptIdeator(llm)
        self.prompt_evaluator = PromptEvaluator(llm)
        self.report_generator = ReportGenerator(llm)

    # --- Node Functions ---
    def orient(self, state: AgentState) -> AgentState:
        print("--- PHASE: ORIENT ---")
        initial_prompt = state["initial_prompt"]
        user_goal = state["user_goal"]

        decomposed_goals_obj = self.goal_decomposer.run(initial_prompt, user_goal)
        if not decomposed_goals_obj:
            raise ValueError("Failed to decompose goals.")

        print(f"Decomposed Goals: {decomposed_goals_obj.decomposed_goals}")

        return {
            **state,
            "decomposed_goals": decomposed_goals_obj.decomposed_goals,
            "iteration_count": 0,
            "prompt_candidates": []
        }

    def refine(self, state: AgentState) -> AgentState:
        print("--- PHASE: REFINE ---")
        decomposed_goals = state["decomposed_goals"]

        criteria_obj = self.criteria_generator.run(decomposed_goals)
        if not criteria_obj:
            raise ValueError("Failed to generate criteria.")

        criteria_list = [c.dict() for c in criteria_obj.evaluation_criteria]
        print(f"Generated Criteria: {json.dumps(criteria_list, indent=2)}")

        return {**state, "evaluation_criteria": criteria_list}

    def ideate(self, state: AgentState) -> AgentState:
        print(f"\n--- CONSTRUCT LOOP: ITERATION {state['iteration_count'] + 1} (IDEATE) ---")

        previous_candidate = None
        evaluation_feedback = None
        if state["prompt_candidates"]:
            last_candidate = state["prompt_candidates"][-1]
            previous_candidate = last_candidate["text"]
            evaluation_feedback = last_candidate["scores"]

        new_prompt_obj = self.prompt_ideator.run(
            original_prompt=state["initial_prompt"],
            evaluation_criteria=state["evaluation_criteria"],
            previous_candidate=previous_candidate,
            evaluation_feedback=evaluation_feedback
        )
        if not new_prompt_obj:
            raise ValueError("Failed to generate a new prompt candidate.")

        print(f"Generated new prompt candidate:\n{new_prompt_obj.prompt_text}")

        # Add placeholder for evaluation
        new_candidates = state["prompt_candidates"] + [{"text": new_prompt_obj.prompt_text,
                                                        "scores": "",
                                                        "avg_score": 0.0}]

        return {**state, "prompt_candidates": new_candidates}

    def evaluate(self, state: AgentState) -> AgentState:
        print(f"--- CONSTRUCT LOOP: ITERATION {state['iteration_count'] + 1} (EVALUATE) ---")

        current_candidate_text = state["prompt_candidates"][-1]["text"]
        evaluation_criteria = state["evaluation_criteria"]

        eval_result_obj = self.prompt_evaluator.run(current_candidate_text, evaluation_criteria)
        if not eval_result_obj:
            raise ValueError("Failed to evaluate the prompt candidate.")

        scores_list = [r.dict() for r in eval_result_obj.results]

        # Calculate average score
        total_score = 0
        max_score = 0
        for criterion, score_data in zip(evaluation_criteria, scores_list):
            if criterion['metric_type'] == 'binary':
                total_score += score_data['score']
                max_score += 1
            elif criterion['metric_type'] == 'scale_1_5':
                total_score += score_data['score']
                max_score += 5

        avg_score = total_score / max_score if max_score > 0 else 0.0

        print(f"Evaluation results: {json.dumps(scores_list, indent=2)}")
        print(f"Normalized Score for this iteration: {avg_score:.2f}")

        # Update the last candidate in the list with its scores
        updated_candidates = state["prompt_candidates"][:]
        updated_candidates[-1]["scores"] = scores_list
        updated_candidates[-1]["avg_score"] = avg_score

        return {**state, "prompt_candidates": updated_candidates, "iteration_count": state["iteration_count"] + 1}

    def act(self, state: AgentState) -> AgentState:
        print("--- PHASE: ACT ---")

        # Find the best prompt
        best_candidate = max(state["prompt_candidates"], key=lambda x: x["avg_score"])
        final_prompt_text = best_candidate["text"]
        final_scores = best_candidate["scores"]

        print(f"Selected best prompt with score {best_candidate['avg_score']:.2f}")

        report_obj = self.report_generator.run(
            initial_prompt=state["initial_prompt"],
            user_goal=state["user_goal"],
            final_prompt=final_prompt_text,
            evaluation_criteria=state["evaluation_criteria"],
            final_scores=final_scores
        )
        if not report_obj:
            raise ValueError("Failed to generate the final report.")

        return {
            **state,
            "final_prompt": report_obj.final_prompt,
            "final_rationale": report_obj.dict()
        }

    # --- Conditional Edge Function ---
    def decide(self, state: AgentState) -> Literal["ideate", "act"]:
        print("--- CONSTRUCT LOOP: (DECIDE) ---")
        iteration_count = state["iteration_count"]

        if iteration_count >= MAX_ITERATIONS:
            print("Decision: Max iterations reached. Proceeding to Act.")
            return "act"

        current_score = state["prompt_candidates"][-1]["avg_score"]
        if current_score >= QUALITY_THRESHOLD:
            print(f"Decision: Quality threshold ({QUALITY_THRESHOLD}) met. Proceeding to Act.")
            return "act"

        print("Decision: Continuing to next iteration.")
        return "ideate"

    def get_graph(self) -> StateGraph:
        """Builds and returns the LangGraph StateGraph."""
        workflow = StateGraph(AgentState)

        # Add nodes
        workflow.add_node("orient", self.orient)
        workflow.add_node("refine", self.refine)
        workflow.add_node("ideate", self.ideate)
        workflow.add_node("evaluate", self.evaluate)
        workflow.add_node("act", self.act)

        # Define edges
        workflow.set_entry_point("orient")
        workflow.add_edge("orient", "refine")
        workflow.add_edge("refine", "ideate")

        # The construct loop
        workflow.add_edge("ideate", "evaluate")
        workflow.add_conditional_edges(
            "evaluate",
            self.decide,
            {
                "ideate": "ideate",
                "act": "act"
            }
        )

        workflow.add_edge("act", END)

        return workflow.compile()
