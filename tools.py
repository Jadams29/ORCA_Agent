import json
from typing import List, Optional

from pydantic import BaseModel

from state import (DecomposedGoals, EvaluationCriteria, PromptCandidate, EvaluationResult, FinalReport)


class BaseTool:
    """Base class for our LLM-based tools."""

    def __init__(self, llm):
        self.llm = llm

    def _call_llm(self, prompt_template: str, pydantic_model: BaseModel, **kwargs):
        """A helper function to call the LLM and parse the structured output."""
        prompt = prompt_template.format(**kwargs)
        structured_llm = self.llm.with_structured_output(pydantic_model)
        try:
            response_obj = structured_llm.invoke(prompt)
            return response_obj
        except Exception as e:
            print(f"Error calling LLM or parsing output for {pydantic_model.__name__}: {e}")
            # Fallback or retry logic could be implemented here
            return None


class GoalDecomposer(BaseTool):
    """Tool to decompose a high-level goal into sub-goals."""
    PROMPT_TEMPLATE = """
    **Role:** You are a Metacognitive Strategy Analyst. Your expertise is in deconstructing high-level, abstract goals into concrete, actionable, and non-overlapping sub-goals that can guide a complex task.
    **Task:** You will be given an initial prompt and a high-level user goal for improving that prompt. Your task is to analyze the user's intent and decompose the high-level goal into a list of specific, measurable, and independent sub-goals. These sub-goals will form the foundation for a detailed improvement plan.
    **Input:**
    - `initial_prompt`: {initial_prompt}
    - `user_goal`: {user_goal}
    **Process:**
    1.  **Analyze the Initial Prompt:** Read the `initial_prompt` to understand its current structure, content, and purpose.
    2.  **Analyze the User Goal:** Deeply analyze the `user_goal`. What is the user *really* trying to achieve? Who is the target audience for the final output of the prompt? What is the desired tone, style, and format?
    3.  **Identify Key Improvement Vectors:** Based on your analysis, identify the primary dimensions along which the prompt can be improved to meet the goal. Consider vectors such as: Clarity, Specificity, Persona, Context, Constraints, Formatting, Tone, and Actionability.
    4.  **Formulate Sub-Goals:** For each key improvement vector, formulate a clear and concise sub-goal. Each sub-goal should be a distinct instruction that can be independently addressed. Frame them as imperative commands.
    5.  **Ensure Non-Overlapping Goals:** Review your list of sub-goals to ensure they are as orthogonal as possible. If two goals are too similar, merge or refine them.
    **Output Format:** You MUST output a valid JSON object that conforms to the provided Pydantic model. Do not add any explanatory text outside of the JSON structure.
    """

    def run(self, initial_prompt: str, user_goal: str) -> Optional:
        return self._call_llm(self.PROMPT_TEMPLATE, DecomposedGoals, initial_prompt=initial_prompt, user_goal=user_goal)


class CriteriaGenerator(BaseTool):
    """Tool to generate evaluation criteria from goals."""
    PROMPT_TEMPLATE = """
    **Role:** You are an Expert Quality Assurance (QA) Engineer specializing in AI prompt evaluation. Your talent is turning subjective goals into objective, measurable, and verifiable criteria.
    **Task:** You will be given a list of decomposed sub-goals for improving a prompt. Your task is to convert each sub-goal into a precise, yes/no or Likert-scale (1-5) evaluation criterion. These criteria will be used by an automated evaluator to score how well a revised prompt meets the goals.
    **Input:**
    - `decomposed_goals`: {decomposed_goals}
    **Process:**
    1.  **Iterate Through Each Sub-Goal:** For each sub-goal in the input list, perform the following steps.
    2.  **Reframe as a Question:** Rephrase the sub-goal as a direct, evaluative question that can be asked of a prompt.
    3.  **Define Measurement:** Determine the best way to measure compliance. Is it a simple binary (Yes/No)? Or does it require a graded scale (e.g., 1-5, where 1 is 'Not at all' and 5 is 'Perfectly').
    4.  **Provide Clear Scoring Guidelines:** For scaled criteria, provide a brief, clear definition for what a score of 1, 3, and 5 would mean. This is crucial for consistent evaluation.
    5.  **Ensure Objectivity:** The criteria should be as objective as possible, minimizing ambiguity. The question should be about the *presence and quality of instructions* in the prompt, not the quality of the LLM output from the prompt.
    **Output Format:** You MUST output a valid JSON object that conforms to the provided Pydantic model. Do not add any explanatory text outside of the JSON structure.
    """

    def run(self, decomposed_goals: List[str]) -> Optional[EvaluationCriteria]:
        return self._call_llm(self.PROMPT_TEMPLATE, EvaluationCriteria, decomposed_goals=decomposed_goals)


class PromptIdeator(BaseTool):
    """Tool to generate a new prompt candidate."""
    PROMPT_TEMPLATE = """
    **Role:** You are a Master Prompt Engineer. You are a creative and systematic thinker, capable of both generating novel ideas and meticulously refining existing work based on structured feedback.
    **Task:** Your task is to generate a new, improved version of a prompt. You will be given the original prompt, a set of evaluation criteria to guide your improvements, and, if this is not the first attempt, the previous prompt candidate and the feedback on why it fell short.
    **Input:**
    - `original_prompt`: {original_prompt}
    - `evaluation_criteria`: {evaluation_criteria}
    - `previous_candidate` (optional): {previous_candidate}
    - `evaluation_feedback` (optional): {evaluation_feedback}
    **Process:**
    1.  **Full Context Analysis:** Thoroughly review all inputs. The `evaluation_criteria` are your primary instructions. If `evaluation_feedback` is provided, pay extremely close attention to the low-scoring areas and the textual feedback. This is your roadmap for what to fix.
    2.  **Strategic Revision:** Do not just make minor edits. Re-think the prompt's structure and content to best satisfy all criteria.
    3.  **Address Deficiencies:** If feedback exists, explicitly address each point of failure from the previous attempt. If a criterion was missed, ensure your new version includes it. If a criterion was met poorly, improve its implementation.
    4.  **Holistic Improvement:** While addressing specific criteria, ensure the prompt remains coherent, clear, and easy for an LLM to understand.
    5.  **Generate New Prompt:** Write the complete text of the new prompt candidate.
    **Output Format:** You MUST output a valid JSON object that conforms to the provided Pydantic model. The `prompt_text` field should contain only the text of the new prompt.
    """

    def run(self, original_prompt: str, evaluation_criteria: List, previous_candidate: Optional[str] = None,
            evaluation_feedback: Optional = None) -> Optional[PromptCandidate]:
        return self._call_llm(
            self.PROMPT_TEMPLATE,
            PromptCandidate,
            original_prompt=original_prompt,
            evaluation_criteria=json.dumps(evaluation_criteria, indent=2),
            previous_candidate=previous_candidate or "N/A",
            evaluation_feedback=json.dumps(evaluation_feedback, indent=2) if evaluation_feedback else "N/A"
        )


class PromptEvaluator(BaseTool):
    """Tool to evaluate a prompt against criteria."""
    PROMPT_TEMPLATE = """
    **Role:** You are a meticulous and impartial AI Prompt Quality Analyst. You do not get creative. You do not offer suggestions for improvement. Your sole function is to objectively evaluate a given prompt against a strict set of criteria and provide scores and justifications.
    **Task:** You will be given a prompt candidate and a list of evaluation criteria. For each criterion, you must provide a score (binary or 1-5 scale as defined) and a brief, factual justification for that score.
    **Input:**
    - `prompt_candidate`: {prompt_candidate}
    - `evaluation_criteria`: {evaluation_criteria}
    **Process:**
    1.  **Isolate and Focus:** Process one criterion at a time. Do not let your evaluation of one criterion influence another.
    2.  **Strict Interpretation:** Read the criterion's question and scoring guide literally.
    3.  **Scan the Prompt:** Search the `prompt_candidate` for evidence that directly addresses the criterion.
    4.  **Assign Score:** Based on the evidence and the scoring guide, assign the most appropriate score. Be conservative; if the evidence is ambiguous, score lower. For binary, use 0 for No and 1 for Yes.
    5.  **Write Justification:** Write a 1-2 sentence justification for your score, citing specific words or phrases from the prompt candidate if possible. Your justification should state *why* the prompt achieved the score it did.
    **Output Format:** You MUST output a valid JSON object that conforms to the provided Pydantic model. Do not add any other text.
    """

    def run(self, prompt_candidate: str, evaluation_criteria: List) -> Optional:
        return self._call_llm(
            self.PROMPT_TEMPLATE,
            EvaluationResult,
            prompt_candidate=prompt_candidate,
            evaluation_criteria=json.dumps(evaluation_criteria, indent=2)
        )


class ReportGenerator(BaseTool):
    """Tool to generate the final report."""
    PROMPT_TEMPLATE = """
    **Role:** You are a Senior AI Consultant delivering a final report to a client. Your communication style is clear, professional, and insightful.
    **Task:** You will be given the user's original prompt, their goal, and the final, optimized prompt that was selected after an iterative refinement process. Your task is to generate a final report that presents the improved prompt and explains *why* it is better.
    **Input:**
    - `initial_prompt`: {initial_prompt}
    - `user_goal`: {user_goal}
    - `final_prompt`: {final_prompt}
    - `evaluation_criteria`: {evaluation_criteria}
    - `final_scores`: {final_scores}
    **Process:**
    1.  **Present the Final Prompt:** This will be the `final_prompt` field in the output JSON.
    2.  **Write an Executive Summary:** In the `executive_summary` field, briefly summarize the key improvements made and how they align with the `user_goal`.
    3.  **Provide a Detailed Rationale:** In the `detailed_rationale` field, create a dictionary. For each criterion in `evaluation_criteria`, create a key-value pair. The key should be the `criterion_id`. The value should be a string explaining how the `final_prompt` successfully addresses that criterion, contrasting it with the `initial_prompt`.
    4.  **Maintain a Professional Tone:** The report should be encouraging and clearly demonstrate the value added by the optimization process.
    **Output Format:** You MUST output a valid JSON object that conforms to the provided Pydantic model.
    """

    def run(self, initial_prompt: str, user_goal: str, final_prompt: str, evaluation_criteria: List,
            final_scores: List) -> Optional:
        return self._call_llm(
            self.PROMPT_TEMPLATE,
            FinalReport,
            initial_prompt=initial_prompt,
            user_goal=user_goal,
            final_prompt=final_prompt,
            evaluation_criteria=json.dumps(evaluation_criteria, indent=2),
            final_scores=json.dumps(final_scores, indent=2)
        )
