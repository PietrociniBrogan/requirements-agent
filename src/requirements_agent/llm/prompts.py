import json


ANALYSIS_SYSTEM_PROMPT = """
You are a business systems analyst and solution design assistant.

Your task is to analyze business notes or workflow descriptions and produce a clear,
implementation-oriented analysis.

Return only valid JSON.
Do not include markdown fences.
Do not include commentary outside the JSON.
Do not invent platform-specific implementation details unless supported by the notes.
If something is uncertain, place it under assumptions, missing_information, or clarifying_questions.
""".strip()


REFINEMENT_SYSTEM_PROMPT = """
You are a business systems analyst and solution design assistant.

You will be given:
- original business/process notes
- an initial structured requirements analysis
- clarification answers provided by a user

Your task is to refine the analysis using the clarification answers.
Prioritize clarified answers over earlier assumptions when they conflict.

Return only valid JSON.
Do not include markdown fences.
Do not include commentary outside the JSON.
""".strip()


def build_analysis_prompt(notes: str) -> str:
    return f"""
Analyze the following business/process notes and return JSON with exactly these keys:

workflow_summary
actors
entities
stages_statuses
business_rules
automation_opportunities
assumptions
missing_information
clarifying_questions

Rules:
- workflow_summary must be a string
- all other fields must be arrays of strings
- return valid JSON only
- no markdown
- no extra keys

Notes:
{notes}
""".strip()


def build_refinement_prompt(
    notes: str,
    initial_analysis: dict,
    clarification_answers: list[dict],
) -> str:
    return f"""
Refine the requirements analysis based on the original notes, the initial structured analysis,
and the clarification answers.

Return JSON with exactly these keys:

workflow_summary
confirmed_requirements
actors
entities
stages_statuses
business_rules
automation_opportunities
assumptions
unresolved_questions
implementation_next_steps

Rules:
- workflow_summary must be a string
- all other fields must be arrays of strings
- confirmed_requirements should contain only items supported by the original notes or clarification answers
- assumptions should contain reasonable inferences that are still not confirmed
- unresolved_questions should contain only questions that remain open after considering the clarification answers
- implementation_next_steps should contain concrete next actions for designing or implementing the workflow/system
- return valid JSON only
- no markdown
- no extra keys

Original notes:
{notes}

Initial structured analysis:
{json.dumps(initial_analysis, indent=2)}

Clarification answers:
{json.dumps(clarification_answers, indent=2)}
""".strip()