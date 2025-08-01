An Agentic Framework for Automated Prompt Optimization: The ORCA Architecture
I. The Imperative for Advanced Prompt Engineering: From Manual Craft to Agentic Optimization
Introduction: The Centrality of the Prompt
In the landscape of modern artificial intelligence, the Large Language Model (LLM) has emerged as a transformative technology, with its capabilities being harnessed across countless domains. The primary interface for interacting with these powerful models is the prompt. This seemingly simple text input is, in reality, a complex instrument that dictates the entirety of the model's subsequent behavior. The quality, precision, and structure of a prompt are the most significant factors determining the quality, relevance, and utility of the generated output. Consequently, the discipline of prompt engineering has become a cornerstone of effective AI implementation. It is the art and science of designing inputs that elicit desired responses from an LLM, transforming a general-purpose model into a specialized tool for a specific task.   

The Evolution of Prompting
The methods for interacting with LLMs have evolved significantly, mirroring the rapid advancement of the models themselves. Early interactions were often limited to simple, zero-shot prompts, where the model was expected to perform a task without any prior examples. The next leap came with few-shot prompting, where providing a few examples of the desired input-output format within the prompt dramatically improved performance. A more profound development was the advent of Chain-of-Thought (CoT) prompting, a technique that encourages the model to "think step by step" by deconstructing a problem into intermediate reasoning stages before arriving at a final answer. This method was groundbreaking, as it not only improved performance on complex reasoning tasks but also made the model's reasoning process more transparent. This progression from simple instructions to complex, structured reasoning templates illustrates a clear trend: as models become more capable, the sophistication required to effectively steer them also increases.   

The Challenge: The Cognitive Load of Manual Optimization
Despite these advancements, prompt engineering remains a significant bottleneck. The process of creating a high-quality prompt is often a manual, iterative, and cognitively demanding task. It requires a unique blend of domain expertise, linguistic creativity, and an intuitive understanding of the target LLM's behavior. Crafting an optimal prompt involves cycles of writing, testing, and refining, a process that is both time-consuming and difficult to scale. It is more of an art than a systematic science, relying heavily on the skill and experience of the individual engineer. This manual approach presents a fundamental challenge to the widespread, efficient deployment of LLM-based solutions, as the quality of the final application is inextricably linked to the artisanal skill of the prompt designer.

The Solution: Agentic AI as a Metacognitive Partner
To overcome the limitations of manual prompt engineering, a new paradigm is required. This report proposes leveraging autonomous agentic systems not merely as consumers of prompts but as active partners in their creation and optimization. An autonomous agent is a system that utilizes an LLM as its core reasoning engine, enabling it to plan, use tools, and execute multi-step tasks to achieve a goal. By tasking such an agent with the specific goal of prompt improvement, the problem is reframed from a manual craft into an automated, intelligent process. The agent acts as a metacognitive partner, applying structured reasoning, systematic planning, and self-correction to the very task of prompt design.   

This approach holds a powerful, recursive potential. The behavior of an autonomous agent is itself defined by a set of core prompts that dictate its persona, its reasoning patterns, and how it uses its tools. An agent designed to improve prompts could, in theory, be turned inward to optimize its own operational instructions. For instance, the prompt that defines the agent's evaluation capabilities could be fed back into the agent as an input, with the goal of "improving this evaluation prompt to be more rigorous and provide more actionable feedback." The agent would then execute its optimization process, generating a superior version of its own logic. This improved logic could then be deployed in the next iteration of the agent, creating a pathway for self-improving systems. This concept aligns with emerging research in automated agent design, where "meta-agents" are used to discover and program more powerful agentic systems, demonstrating significant performance gains over hand-designed counterparts. This self-referential optimization loop represents a significant step towards more sophisticated and capable AI.   

II. A Critical Review of Foundational Agent Architectures
An agentic framework is a structured methodology that enables an LLM to transcend simple text generation, empowering it to engage in complex, multi-step activities that involve strategic planning, interaction with external tools, and the use of memory. To construct a robust agent for prompt optimization, it is essential to first analyze the strengths and weaknesses of existing foundational paradigms. This review examines three influential architectures: ReAct, the OODA loop, and the PDCA cycle.   

A. The ReAct Paradigm: Fusing Thought and Action
Core Principle
The ReAct (Reason+Act) framework is a paradigm for building LLM-based agents that seamlessly combines verbal reasoning with task-oriented actions. The core principle is to prompt an LLM to generate both a reasoning trace (a "thought") and a corresponding action in an interleaved manner. This process creates a human-like, interpretable trajectory where the agent "thinks aloud" about what it needs to do, performs an action using an external tool, observes the result, and then uses that observation to inform its next thought and action. This tight synergy between reasoning and acting allows the agent to create, maintain, and adjust plans dynamically while interacting with its environment.   

Strengths
The ReAct architecture offers several distinct advantages. First and foremost is its transparency and debuggability. Because the agent's thought process is externalized into a readable format, developers and users can easily follow the logical steps that lead to a particular outcome. This transparency is crucial for debugging, understanding agent behavior, and building trust in the system.   

Second, ReAct is highly effective at reducing hallucination. A common failure mode for LLMs operating in a pure Chain-of-Thought mode is the generation of factually incorrect or fabricated information. ReAct mitigates this by grounding the agent's reasoning in reality through tool use. By interacting with external information sources like a Wikipedia API or a web search tool, the agent can verify facts and incorporate real-time data into its reasoning process, leading to more accurate and trustworthy outputs.   

Finally, ReAct is well-suited for handling complexity. The iterative, step-by-step nature of the Thought-Action-Observation loop enables the agent to tackle dynamic and unpredictable tasks that require adaptation based on intermediate results. This makes it a powerful choice for complex problem-solving, such as answering multi-hop questions or executing intricate workflows.   

Weaknesses
Despite its strengths, the ReAct paradigm has notable weaknesses. Its primary limitation is its linear reasoning process, which can lead to the agent "getting stuck." ReAct's thinking is sequential; if an initial thought is flawed, the subsequent action is likely to be incorrect. The framework lacks a native, higher-level mechanism for strategic re-evaluation. Research has shown that once a ReAct agent commits to a thought, it seldom re-evaluates its core assumptions, which can lead to it pursuing a flawed line of reasoning or getting trapped in a repetitive action loop.   

Another weakness is its potential for inefficiency. For simple, straightforward tasks, the full Thought -> Action -> Observation cycle can be computationally expensive and token-inefficient. A task that could be accomplished with a single, direct function call might require multiple LLM calls and significant overhead in a ReAct framework, making it overkill for less complex problems.   

Lastly, ReAct lacks a mechanism for strategic oversight. The framework is fundamentally tactical, excelling at determining and executing the next best step. However, it does not have a built-in process for maintaining a global, long-term strategy or ensuring that all components of a complex, multi-faceted goal are being addressed systematically.   

B. The OODA Loop: A Framework for Strategic Agility
Core Principle
The OODA (Observe-Orient-Decide-Act) loop is a decision-making framework developed by military strategist Colonel John Boyd to function in chaotic and confusing environments. Its application to AI is transformative, shifting systems from being purely reactive to prompts to becoming proactive entities that continuously engage with their environment to make rapid, context-aware decisions. The core of the OODA loop is its iterative nature, allowing an agent to continuously adapt to changing circumstances.   

Phases in an AI Context
In an agentic AI context, the four phases of the OODA loop are re-imagined:

Observe: The agent actively and continuously gathers data from all available sources. This includes not only direct user input but also sensor feeds, internal knowledge bases, and feedback from previous actions. This proactive sensing creates a real-time, comprehensive picture of the operational environment.   

Orient: This is the most critical phase for strategic thinking. Here, the agent analyzes, synthesizes, and contextualizes the data collected during the Observe phase. It involves filtering out noise, identifying key patterns, and leveraging machine learning models to build a deep and current understanding of the situation. This is where the agent forms its "worldview" and situational awareness.   

Decide: Based on the rich understanding developed during the Orient phase, the agent evaluates potential courses of action. It simulates scenarios and selects the most effective and appropriate response to achieve its desired outcome.   

Act: The agent executes the chosen decision. This action's outcome is then immediately fed back into the Observe phase, creating a continuous feedback loop that allows the agent to learn from its interactions and refine its future behavior.   

Strengths
The primary strength of the OODA loop is its emphasis on adaptability and speed. The continuous cycling through the four phases enables an agent to respond rapidly to new information, changing user needs, and dynamic scenarios. Furthermore, the explicit    

Orient phase promotes enhanced situational awareness. By forcing the agent to build a comprehensive understanding of the context before making a decision, the framework leads to more robust, refined, and effective actions.   

Weaknesses
The main weakness of the OODA loop is its strategic abstraction. It is a high-level conceptual framework that describes what an agent should do (Observe, Orient, etc.) but provides little guidance on how to perform those actions. It lacks the granular, tactical execution model found in a framework like ReAct. Some critics have argued that, when applied at a strategic level without sufficient nuance, the loop can be an oversimplification of complex decision-making processes. It provides the "why" but not the tactical "what."   

C. The PDCA Cycle: A Blueprint for Continuous Improvement
Core Principle
The Plan-Do-Check-Act (PDCA) cycle, also known as the Deming cycle, is a systematic, iterative methodology designed for continuous process improvement and quality control. Its power is derived from its structured, data-driven approach to problem-solving, which emphasizes testing and validating changes in a controlled manner before full-scale implementation. In an AI context, it provides a formal mechanism for an agent to improve its own outputs through self-correction.   

Phases in an AI Context
The four phases of the PDCA cycle are directly applicable to an autonomous agent's workflow:

Plan: The agent clearly defines the problem, analyzes its root causes, and establishes a concrete plan with specific, measurable objectives. For a prompt-improvement agent, this would involve creating a detailed plan for how to revise a given prompt to meet a user's goal.   

Do: The agent implements the plan on a small, controlled scale. In our context, this corresponds to the agent generating a new, candidate version of the prompt based on its plan.   

Check: This is arguably the most critical phase for building a robust agent. Here, the results of the Do phase are rigorously and objectively evaluated against the goals and metrics established in the Plan phase. This introduces a formal verification and self-correction mechanism that is absent in the standard ReAct framework. The agent must analyze data to see if the change was actually an improvement.   

Act: Based on the analysis from the Check phase, the agent determines the next steps. If the change was successful, it is standardized (e.g., the new prompt is adopted). If the results fell short, the agent uses the lessons learned to adjust its approach and returns to the Plan phase for another iteration. This closes the loop and drives continuous improvement.   

Strengths
The PDCA cycle's greatest strength is its framework for structured problem-solving and self-correction. The explicit Check phase provides a formal opportunity for the agent to evaluate its own work, identify its flaws, and learn from its mistakes, making the overall system significantly more robust and reliable. This cyclical process also    

minimizes risk, as potential solutions are tested on a small scale before being finalized, preventing the commitment to a flawed approach. Finally, the framework inherently promotes    

data-driven decisions, as the Act phase is directly informed by the objective analysis conducted in the Check phase.   

Weaknesses
The primary weakness of the PDCA cycle is its methodical pace. The structured, four-phase nature can be slower and more deliberate than the rapid, tactical execution of a framework like ReAct. Additionally, PDCA is fundamentally process-oriented. It excels at improving an existing process but is less focused on the initial high-level strategy formation, which is the core strength of the OODA loop's Orient phase.

A deeper consideration reveals that these three architectural frameworks—ReAct, OODA, and PDCA—are not mutually exclusive competitors. Instead, they represent complementary layers of cognition required for an advanced agentic system. An agent tasked with a complex problem like prompt optimization must operate on all three levels. It first requires a high-level strategic understanding of the user's goal and the current state of the prompt; this is the function of the OODA loop's Observe and Orient phases. Once oriented, the agent needs a structured methodology for making improvements, which is perfectly supplied by the PDCA cycle's iterative loop of planning, doing, checking, and acting. Finally, within the Do and Check phases of the PDCA cycle, the agent must perform concrete, tactical sub-tasks, such as researching prompt design principles or drafting a new version of the prompt. This is where the ReAct framework's Thought -> Action -> Observation loop becomes the engine that drives execution. This creates a nested, hierarchical model where OODA provides the strategic "why," PDCA provides the iterative "how," and ReAct provides the tactical "what," with each framework compensating for the inherent weaknesses of the others.

III. The ORCA Framework: A Hybrid Architecture for Prompt Optimization
Introducing ORCA: Orient-Refine-Construct-Act
To address the multifaceted challenge of automated prompt improvement, this report introduces a novel hybrid architecture: the Orient-Refine-Construct-Act (ORCA) framework. The name is chosen to evoke the intelligence, depth, and systematic nature of the agent's process. ORCA is explicitly designed as a synthesis of the strongest elements from ReAct, OODA, and PDCA, structured to maximize robustness, goal-alignment, and the quality of the final output. It is architected to overcome the limitations of any single framework by integrating their complementary strengths into a single, cohesive workflow.

Architectural Philosophy
The core philosophy of ORCA is to guide the agent through a logical progression that moves from high-level strategic comprehension down to iterative, quality-controlled construction, and finally to a decisive conclusion. This is achieved through four distinct phases:

Orient (from OODA): The process begins with the agent establishing complete situational awareness. It ingests the user's initial prompt and their high-level goal, dedicating its initial resources to fully understanding the context, constraints, and desired end-state. This phase directly incorporates the strategic strength of the OODA loop's Observe and Orient stages, ensuring that all subsequent actions are grounded in a deep and accurate understanding of the task.

Refine (from PDCA's 'Plan'): The agent does not immediately begin generating new prompts. Instead, it first refines the user's abstract goal into a concrete, actionable plan. Critically, this phase translates the decomposed goals into a set of measurable evaluation criteria. This step is a direct implementation of the PDCA cycle's Plan phase and is essential for the Check phase to function objectively. By creating a clear, explicit rubric for success before any construction begins, the agent establishes a non-negotiable standard of quality.

Construct (from PDCA's 'Do-Check-Act' loop, powered by ReAct): This is the core engine of the framework. The agent enters an iterative loop where it generates a prompt candidate (Do), rigorously evaluates that candidate against the predefined criteria (Check), and then uses the feedback from the evaluation to inform the next generation (Act on the feedback to re-plan). The complex sub-tasks within this loop, such as generating the prompt text or performing the evaluation, can themselves be executed using ReAct-style Thought -> Action -> Observation sequences, allowing for dynamic, tool-assisted execution within a structured, self-correcting cycle.

Act (Finalization): Once the Construct loop has produced a prompt that meets the quality threshold, the agent moves to the final phase. Here, it makes a definitive decision, selecting the highest-scoring prompt candidate. It then generates a comprehensive report for the user, presenting the final prompt and providing a detailed rationale that explains why the new prompt is superior, linking the improvements directly back to the user's original goal and the established criteria.

Comparative Analysis of Agent Architectures
The following table provides a comparative analysis of the foundational architectures and the proposed ORCA framework. It highlights how ORCA systematically integrates the strengths of its predecessors to create a more comprehensive and robust system for the specific task of prompt optimization.

Feature	ReAct (Reason + Act)	OODA Loop	PDCA Cycle	ORCA Framework (Proposed)
Primary Goal	Task completion via interleaved thought and action.	Rapid, adaptive decision-making in dynamic environments.	Continuous process improvement and quality control.	High-quality, goal-aligned prompt generation through iterative refinement.
Core Loop	Thought -> Action -> Observation	Observe -> Orient -> Decide -> Act	Plan -> Do -> Check -> Act	Orient -> Refine -> Construct -> Act
Key Strength	
Transparency; handling complex, multi-step tactical tasks.   

Situational awareness; strategic adaptability.   

Self-correction; structured problem-solving; risk minimization.   

Integrates strategic planning (Orient), explicit quality criteria (Refine), and robust self-evaluation within an iterative loop (Construct).
Key Weakness	
Can get stuck in loops; lacks strategic oversight.   

Lacks tactical execution details; can be too abstract.   

Can be slow/methodical; less focused on initial strategy.   

Higher initial complexity and potential for more LLM calls, but yields a more robust and reliable final product.
Role in Prompt Optimization	Executes specific sub-tasks like searching for information or drafting a prompt component.	Provides the overall strategic direction for the prompt improvement task.	Provides the iterative loop for testing and improving prompt versions.	Provides a complete, end-to-end system for prompt optimization.
As the table illustrates, ORCA is not merely another alternative but a synthesis. It addresses ReAct's lack of strategic oversight with the Orient phase, it gives OODA's abstract strategy a concrete execution path with the Refine and Construct phases, and it elevates PDCA's process-improvement loop by powering it with ReAct's tactical capabilities and guiding it with OODA's strategic intent. This results in a system that is designed to be more reliable, goal-focused, and capable of producing verifiably high-quality outputs.

IV. An Extensive Blueprint for the ORCA Prompt-Improvement Agent
System Overview
The ORCA agent is designed as a stateful graph, ideally implemented using a framework like LangGraph. The agent's process is modeled as a series of nodes, where the state of the task is passed from one node to the next. This state is a comprehensive data structure that tracks all aspects of the prompt optimization process, from initial inputs to the final output.

Agent State
The agent's state will be managed by a Pydantic model to ensure data integrity and structure throughout the workflow. The AgentState will contain the following fields:

initial_prompt: str - The original prompt provided by the user.

user_goal: str - The high-level objective for the prompt's improvement.

decomposed_goals: List[str] - A list of specific, actionable sub-goals derived from the user_goal.

evaluation_criteria: List - A structured list of objective criteria for judging prompt quality, derived from the decomposed_goals.

prompt_candidates: List - A log of all generated prompt versions, each with its full text, evaluation scores, and feedback.

iteration_count: int - A counter for the number of cycles through the Construct loop.

final_prompt: str - The highest-scoring prompt selected at the end of the process.

final_rationale: str - A comprehensive report explaining the improvements made.

Tool Definitions
The agent will have access to a suite of specialized, LLM-based tools. Each tool is designed to perform a specific, well-defined sub-task within the ORCA workflow. These tools are the "actions" that the agent can invoke to manipulate the state. The primary tools are: GoalDecomposer, CriteriaGenerator, PromptIdeator, PromptEvaluator, and ReportGenerator.

Phase 1: Orient Node
Purpose: This initial node serves to process the user's inputs (initial_prompt, user_goal) and establish a deep, foundational understanding of the task. It directly implements the Observe and Orient phases of the OODA loop, ensuring that the agent's entire process is built upon a solid strategic foundation.

Tool(s) Used: GoalDecomposer (LLM-based tool).

Process:

The Orient node is the entry point to the graph, receiving the initial state containing the user's inputs.

It invokes the GoalDecomposer tool, passing the initial_prompt and user_goal.

The tool's responsibility is to deconstruct the user's potentially vague or abstract goal into a list of specific, concrete, and actionable sub-goals. For instance, a high-level goal like "make this prompt better for a marketing copywriter" would be decomposed into distinct sub-goals such as "Incorporate a persuasive and brand-aligned persona," "Specify the target demographic as Gen Z consumers," "Mandate a call-to-action," and "Define the output format as three distinct ad variations."

The output from the tool, a list of these decomposed goals, is used to update the decomposed_goals field in the agent's state.

LLM Prompt for GoalDecomposer Tool:

Role: You are a Metacognitive Strategy Analyst. Your expertise is in deconstructing high-level, abstract goals into concrete, actionable, and non-overlapping sub-goals that can guide a complex task.

Task: You will be given an initial prompt and a high-level user goal for improving that prompt. Your task is to analyze the user's intent and decompose the high-level goal into a list of specific, measurable, and independent sub-goals. These sub-goals will form the foundation for a detailed improvement plan.

Input:

initial_prompt: The original prompt provided by the user.

user_goal: The high-level objective for the prompt's improvement.

Process:

Analyze the Initial Prompt: Read the initial_prompt to understand its current structure, content, and purpose.

Analyze the User Goal: Deeply analyze the user_goal. What is the user really trying to achieve? Who is the target audience for the final output of the prompt? What is the desired tone, style, and format?

Identify Key Improvement Vectors: Based on your analysis, identify the primary dimensions along which the prompt can be improved to meet the goal. Consider vectors such as: Clarity, Specificity, Persona, Context, Constraints, Formatting, Tone, and Actionability.

Formulate Sub-Goals: For each key improvement vector, formulate a clear and concise sub-goal. Each sub-goal should be a distinct instruction that can be independently addressed. Frame them as imperative commands.

Ensure Non-Overlapping Goals: Review your list of sub-goals to ensure they are as orthogonal as possible. If two goals are too similar, merge or refine them.

Example:

initial_prompt: "Write about our new shoes."

user_goal: "Make this a good prompt for generating exciting social media posts."

Your Ideal Output (as a Pydantic object):
json
{
"decomposed_goals":
}


Output Format: You MUST output a valid JSON object that conforms to the provided Pydantic model for DecomposedGoals. Do not add any explanatory text outside of the JSON structure.

Phase 2: Refine Node
Purpose: This node executes the Plan phase of the PDCA cycle. Its function is to transform the qualitative decomposed_goals into a set of objective, quantitative, and verifiable evaluation_criteria. This step is crucial because it creates the official rubric against which all future prompt candidates will be judged, enabling the objective Check phase of the Construct loop.

Tool(s) Used: CriteriaGenerator (LLM-based tool).

Process:

The Refine node receives the agent state, which now contains the decomposed_goals.

It invokes the CriteriaGenerator tool.

The tool iterates through each sub-goal and translates it into a precise evaluation criterion. This involves reframing the goal as a question and defining a clear metric (e.g., binary Yes/No, or a 1-5 Likert scale). For example, the sub-goal "Incorporate a persuasive and brand-aligned persona" might be translated into two criteria: 1) "Does the prompt explicitly define a persona? (Binary: Yes/No)" and 2) "How well does the persona's description align with 'persuasive and brand-aligned'? (Scale: 1-5)."

The structured list of criteria is then used to update the evaluation_criteria field in the agent state.

LLM Prompt for CriteriaGenerator Tool:

Role: You are an Expert Quality Assurance (QA) Engineer specializing in AI prompt evaluation. Your talent is turning subjective goals into objective, measurable, and verifiable criteria.

Task: You will be given a list of decomposed sub-goals for improving a prompt. Your task is to convert each sub-goal into a precise, yes/no or Likert-scale (1-5) evaluation criterion. These criteria will be used by an automated evaluator to score how well a revised prompt meets the goals.

Input:

decomposed_goals: A list of specific sub-goals.

Process:

Iterate Through Each Sub-Goal: For each sub-goal in the input list, perform the following steps.

Reframe as a Question: Rephrase the sub-goal as a direct, evaluative question that can be asked of a prompt.

Define Measurement: Determine the best way to measure compliance. Is it a simple binary (Yes/No)? Or does it require a graded scale (e.g., 1-5, where 1 is 'Not at all' and 5 is 'Perfectly').

Provide Clear Scoring Guidelines: For scaled criteria, provide a brief, clear definition for what a score of 1, 3, and 5 would mean. This is crucial for consistent evaluation.

Ensure Objectivity: The criteria should be as objective as possible, minimizing ambiguity and subjective interpretation. The question should be about the presence and quality of instructions in the prompt, not the quality of the LLM output from the prompt.

Example:

decomposed_goals:

Your Ideal Output (as a Pydantic object):

JSON

{
  "evaluation_criteria":
}
Output Format: You MUST output a valid JSON object that conforms to the provided Pydantic model for EvaluationCriteria. Do not add any explanatory text outside of the JSON structure.

Phase 3: Construct Loop (Iterative Refinement)
This phase is not a single node but a self-contained sub-graph that implements the PDCA cycle for prompt improvement. It consists of three components: an Ideate node (Do), an Evaluate node (Check), and a conditional edge named Decide which directs the flow, embodying the Act principle of choosing the next step. The agent will loop through this sub-graph a set number of times or until a quality threshold is met.

A. Ideate Node (Do)
Purpose: To generate a new candidate version of the prompt. This node is the creative engine of the agent, responsible for synthesizing all available information into an improved artifact.

Tool(s) Used: PromptIdeator (LLM-based tool).

Process: This node's behavior adapts based on the iteration. On the first pass, it takes the initial_prompt and the newly created evaluation_criteria as its primary inputs. On all subsequent passes, it also receives the previously generated candidate and its associated evaluation_feedback, allowing it to learn from its prior mistakes and make targeted improvements.

LLM Prompt for PromptIdeator Tool:

Role: You are a Master Prompt Engineer. You are a creative and systematic thinker, capable of both generating novel ideas and meticulously refining existing work based on structured feedback.
Task: Your task is to generate a new, improved version of a prompt. You will be given the original prompt, a set of evaluation criteria to guide your improvements, and, if this is not the first attempt, the previous prompt candidate and the feedback on why it fell short.
Input:

original_prompt: The starting point.

evaluation_criteria: The full list of criteria your new prompt must satisfy.

previous_candidate (optional): The last prompt you generated.

evaluation_feedback (optional): The scores and critiques of the previous_candidate.

Process:

Full Context Analysis: Thoroughly review all inputs. The evaluation_criteria are your primary instructions. If evaluation_feedback is provided, pay extremely close attention to the low-scoring areas and the textual feedback. This is your roadmap for what to fix.

Strategic Revision: Do not just make minor edits. Re-think the prompt's structure and content to best satisfy all criteria.

Address Deficiencies: If feedback exists, explicitly address each point of failure from the previous attempt. If a criterion was missed, ensure your new version includes it. If a criterion was met poorly, improve its implementation.

Holistic Improvement: While addressing specific criteria, ensure the prompt remains coherent, clear, and easy for an LLM to understand.

Generate New Prompt: Write the complete text of the new prompt candidate.

Output Format: You MUST output a valid JSON object that conforms to the provided Pydantic model for PromptCandidate. The prompt_text field should contain only the text of the new prompt.

B. Evaluate Node (Check)
Purpose: To perform the critical Check phase of the PDCA cycle. This node acts as an impartial judge, scoring the newly generated prompt candidate from the Ideate node against the objective evaluation_criteria established in the Refine phase.

Tool(s) Used: PromptEvaluator (LLM-based tool).

Process: The node is given the text of the new prompt_candidate and the list of evaluation_criteria. It invokes the PromptEvaluator tool, which systematically goes through each criterion, assigns a score, and provides a brief, factual justification for that score. The output is a structured list of these evaluations, which is then appended to the log in the prompt_candidates state field.

LLM Prompt for PromptEvaluator Tool:

Role: You are a meticulous and impartial AI Prompt Quality Analyst. You do not get creative. You do not offer suggestions for improvement. Your sole function is to objectively evaluate a given prompt against a strict set of criteria and provide scores and justifications.
Task: You will be given a prompt candidate and a list of evaluation criteria. For each criterion, you must provide a score (binary or 1-5 scale as defined) and a brief, factual justification for that score.
Input:

prompt_candidate: The prompt text to be evaluated.

evaluation_criteria: The list of criteria to evaluate against, including their metric type and scoring guides.

Process:

Isolate and Focus: Process one criterion at a time. Do not let your evaluation of one criterion influence another.

Strict Interpretation: Read the criterion's question and scoring guide literally.

Scan the Prompt: Search the prompt_candidate for evidence that directly addresses the criterion.

Assign Score: Based on the evidence and the scoring guide, assign the most appropriate score. Be conservative; if the evidence is ambiguous, score lower.

Write Justification: Write a 1-2 sentence justification for your score, citing specific words or phrases from the prompt candidate if possible. Your justification should state why the prompt achieved the score it did. Example: "Score: 2/5. Justification: The prompt mentions a 'positive tone' but does not use the specified keywords 'trendy' or 'energetic', failing to fully align with the persona."

Output Format: You MUST output a valid JSON object that conforms to the provided Pydantic model for EvaluationResult. It should be a list of scored criteria. Do not add any other text.

C. Decide Conditional Edge
Purpose: This is the logic gate that controls the Construct loop. After each evaluation, it inspects the results and determines the next step in the graph, embodying the Act part of the PDCA cycle.

Process:

The edge's logic calculates an aggregate quality score for the most recent prompt candidate based on the results from the Evaluate node.

It then checks a series of conditions to route the agent:

Condition 1 (Success): If the aggregate score surpasses a predefined quality threshold (e.g., 95% of the maximum possible score) OR if the score has plateaued (failed to improve over the last N iterations), the loop is considered complete. The agent is routed to the final Act node.

Condition 2 (Continue): If the score is still below the threshold but is showing improvement, and the maximum number of iterations (e.g., 5) has not been reached, the agent is routed back to the Ideate node to begin another cycle of refinement.

Condition 3 (Failure): If the maximum number of iterations is reached and the score remains below the quality threshold, the process is terminated to prevent infinite loops. The agent proceeds to the Act node, but the final report may indicate that an optimal solution was not found within the operational constraints.

Phase 4: Act Node
Purpose: This is the final node in the ORCA workflow. Its purpose is to conclude the process by selecting the best-performing prompt and communicating the results and rationale back to the user in a clear and professional manner.

Tool(s) Used: ReportGenerator (LLM-based tool).

Process:

The Act node receives the final state from the Construct loop. Its first task is to programmatically identify the highest-scoring prompt from the prompt_candidates list.

It then invokes the ReportGenerator tool, providing it with all the necessary context: the initial prompt, the user's goal, the final selected prompt, and its evaluation scores and criteria.

The tool generates a comprehensive final report, which is then used to update the final_prompt and final_rationale fields in the agent's state, completing the process.

LLM Prompt for ReportGenerator Tool:

Role: You are a Senior AI Consultant delivering a final report to a client. Your communication style is clear, professional, and insightful.

Task: You will be given the user's original prompt, their goal, and the final, optimized prompt that was selected after an iterative refinement process. Your task is to generate a final report that presents the improved prompt and explains why it is better.

Input:

initial_prompt: The user's starting point.

user_goal: The user's stated objective.

final_prompt: The best prompt generated by the agent.

evaluation_criteria: The criteria used to judge the prompts.

final_scores: The evaluation scores for the final prompt.

Process:

Present the Final Prompt: Clearly display the full text of the final_prompt.

Write an Executive Summary: Briefly summarize the key improvements made and how they align with the user_goal.

Provide a Detailed Rationale: Create a "Changes and Justification" section. Go through the evaluation_criteria. For each criterion, explain how the final_prompt successfully addresses it, contrasting it with the initial_prompt. Use a before-and-after style of explanation. For example: "You asked for a more persuasive tone. The original prompt was neutral, while the final prompt incorporates a specific 'expert consultant' persona and uses persuasive language like 'unlock the potential' and 'drive success'."

Maintain a Professional Tone: The report should be encouraging and clearly demonstrate the value added by the optimization process.

Output Format: You MUST output a valid JSON object that conforms to the provided Pydantic model for FinalReport.

V. Python Implementation with LangGraph
This section provides the complete Python implementation of the ORCA agent as described in the blueprint. The code is structured into logical components corresponding to the state, tools, and graph definition. It utilizes the Google Gemini Pro model, LangGraph for orchestration, and Pydantic for structured data handling, strictly avoiding the use of LangChain Expression Language (LCEL) as per the requirements.

Python

# main.py - Entry point and execution logic

import os
import json
from typing import List, Dict, Literal, Optional, Annotated
from typing_extensions import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END

# To run this code, you must have an environment variable named GOOGLE_API_KEY
# set to your Google API key.
# Example: os.environ = "YOUR_API_KEY"

# --- Configuration ---
MAX_ITERATIONS = 4
QUALITY_THRESHOLD = 0.95 # 95% of max possible score

# --- 1. State Definition (state.py) ---

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
    results: List

class FinalReport(BaseModel):
    """The final report delivered to the user."""
    final_prompt: str = Field(description="The full text of the final, optimized prompt.")
    executive_summary: str = Field(description="A brief summary of the key improvements.")
    detailed_rationale: Dict[str, str] = Field(description="A dictionary mapping criterion ID to a detailed justification of the improvement.")

class AgentState(TypedDict):
    """Represents the state of our graph."""
    initial_prompt: str
    user_goal: str
    decomposed_goals: List[str]
    evaluation_criteria: List
    prompt_candidates: List # List of dicts with 'text', 'scores', 'avg_score'
    iteration_count: int
    final_prompt: str
    final_rationale: Dict

# --- 2. Tool Definition (tools.py) ---

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
    def run(self, original_prompt: str, evaluation_criteria: List, previous_candidate: Optional[str] = None, evaluation_feedback: Optional] = None) -> Optional[PromptCandidate]:
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
    def run(self, initial_prompt: str, user_goal: str, final_prompt: str, evaluation_criteria: List, final_scores: List) -> Optional:
        return self._call_llm(
            self.PROMPT_TEMPLATE,
            FinalReport,
            initial_prompt=initial_prompt,
            user_goal=user_goal,
            final_prompt=final_prompt,
            evaluation_criteria=json.dumps(evaluation_criteria, indent=2),
            final_scores=json.dumps(final_scores, indent=2)
        )

# --- 3. Graph Definition (graph.py) ---

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
            "prompt_candidates":
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
        new_candidates = state["prompt_candidates"] + [{"text": new_prompt_obj.prompt_text, "scores":, "avg_score": 0.0}]
        
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


# --- Main Execution ---
if __name__ == "__main__":
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY environment variable not set.")

    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.1)

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
        "decomposed_goals":,
        "evaluation_criteria":,
        "prompt_candidates":,
        "iteration_count": 0,
        "final_prompt": "",
        "final_rationale": {}
    }

    print("--- STARTING ORCA AGENT ---")
    # Run the agent
    final_state = app.invoke(initial_state)

    print("\n\n--- ORCA AGENT FINISHED ---")
    print("\n--- FINAL REPORT ---")
    print(f"\nOptimized Prompt:\n{'-'*20}\n{final_state['final_rationale']['final_prompt']}")
    print(f"\nExecutive Summary:\n{'-'*20}\n{final_state['final_rationale']['executive_summary']}")
    print(f"\nDetailed Rationale:\n{'-'*20}")
    for criterion_id, justification in final_state['final_rationale']['detailed_rationale'].items():
        print(f"- {criterion_id.replace('_', ' ').title()}: {justification}")
VI. Conclusion: The Future of Agent-Driven Metacognition
Summary of Contributions
This report has introduced the Orient-Refine-Construct-Act (ORCA) framework, a novel hybrid architecture for autonomous agents specifically designed for the complex task of prompt optimization. ORCA represents a deliberate synthesis of the strongest attributes of existing agentic paradigms. It integrates the strategic situational awareness of the OODA loop, the structured, self-correcting methodology of the PDCA cycle, and the tactical, tool-using prowess of the ReAct framework. By structuring the agent's workflow into a logical progression from high-level understanding (Orient) to the establishment of objective quality standards (Refine), and then into an iterative, self-evaluating generation loop (Construct), ORCA provides a robust and reliable solution to a critical bottleneck in the practical application of LLMs. The final Act phase ensures that the agent's work is not only completed but also clearly communicated, delivering a high-quality, optimized prompt along with a detailed rationale for its improvements.

Limitations and Future Work
While the ORCA framework provides a powerful and structured approach, it is not without limitations, which themselves point toward avenues for future research and development.

Tool Reliability: The entire system is heavily dependent on the ability of the core LLM to consistently follow instructions and produce valid, parsable JSON outputs for each tool. While modern models are increasingly reliable in this regard, failures can still occur. Future work should focus on building more robust error-handling and fallback mechanisms, such as implementing retry logic with modified prompts or even having a secondary, simpler model attempt to "fix" malformed JSON before failing the step.   

Cost Optimization: The iterative nature of the Construct loop, with its multiple LLM calls for ideation and evaluation, can be computationally expensive and lead to high token consumption. This is a significant consideration for practical applications. Future research could explore cost-optimization strategies, such as using smaller, potentially fine-tuned models for the more constrained tasks like PromptEvaluator, reserving the larger, more powerful model for the creative PromptIdeator task. Caching mechanisms could also be employed to avoid redundant computations.   

Expanding the Toolset: The current blueprint focuses on a core set of LLM-based tools. The framework's power could be significantly enhanced by expanding this toolset. For instance, a WebSearchTool could be added to the Ideate phase, allowing the agent to research examples of high-performing prompts within a specific domain (e.g., "find examples of effective prompts for legal document summarization"). For prompts that generate code, a CodeExecutionTool could be integrated into the Evaluate phase to run the generated code and check for correctness, adding an empirical layer to the evaluation process.

Broader Implications: Towards Self-Improving Systems
The development of agents capable of optimizing their own foundational instructions has profound implications for the future of artificial intelligence. The ORCA framework, while designed for the external task of improving a user's prompt, serves as a proof of concept for more advanced metacognitive systems. The same logic that allows the agent to refine a user's prompt could be directed inward, targeting the very prompts that define its own behavior.

This opens the door to a future of truly self-improving systems. An agent could be tasked with optimizing its own PromptEvaluator logic to become a more discerning critic, or its PromptIdeator logic to become more creative. This creates a recursive improvement loop, where each generation of the agent is built upon a slightly more refined set of internal instructions, developed by its predecessor. This aligns directly with cutting-edge research into "Meta Agent Search," where agents are used to automatically discover novel and more effective agentic system designs, leading to substantial performance improvements over manually designed systems. The journey from manually crafting prompts to deploying agents that optimize them is the first step. The next, more transformative step is deploying agents that can optimize themselves, accelerating the evolution of AI capabilities in a structured, measurable, and increasingly autonomous fashion. 
