from typing import List, Dict, Literal, Optional

from pydantic import BaseModel, Field
from typing_extensions import TypedDict


class DecomposedGoals(BaseModel):
    """Structured output for decomposed goals."""
    decomposed_goals: List[str] = Field(description="A list of specific, actionable sub-goals.")


class EvaluationCriterion(BaseModel):
    """A single criterion for evaluating a prompt."""
    criterion_id: str = Field(description="A unique identifier for the criterion.")
    question: str = Field(description="The evaluative question to ask of the prompt.")
    metric_type: Literal["binary", "scale_1_5"] = Field(description="The type of metric for evaluation.")
    scoring_guide: Optional[str] = Field(
        default=None,
        description="Clear guidelines for 1-5 scale scoring (e.g., '1: Poor, 3: Average, 5: Excellent')."
    )


class EvaluationCriteria(BaseModel):
    """Structured output for a list of evaluation criteria."""
    evaluation_criteria: List[EvaluationCriterion] = Field(description="A list of objective evaluation criteria.")


class PromptCandidate(BaseModel):
    """A generated prompt candidate."""
    prompt_text: str = Field(description="The full text of the new prompt candidate.")


class ScoredCriterion(BaseModel):
    """A single criterion with its score and justification."""
    criterion_id: str
    score: float
    justification: str


class EvaluationResult(BaseModel):
    """The full evaluation result for a prompt candidate."""
    results: List[ScoredCriterion]


class FinalReport(BaseModel):
    """The final report delivered to the user."""
    final_prompt: str = Field(description="The full text of the final, optimized prompt.")
    executive_summary: str = Field(description="A brief summary of the key improvements.")
    detailed_rationale: Dict[str, str] = Field(
        description="A dictionary mapping criterion ID to a detailed justification of the improvement.")


class AgentState(TypedDict):
    """Represents the state of our graph."""
    initial_prompt: str
    user_goal: str
    decomposed_goals: List[str]
    evaluation_criteria: List[EvaluationCriterion]
    prompt_candidates: List  # List of dicts with 'text', 'scores', 'avg_score'
    iteration_count: int
    final_prompt: str
    final_rationale: Dict
