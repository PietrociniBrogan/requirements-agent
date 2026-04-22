SYSTEM_PROMPT = """
You are a business systems analyst and solution design assistant.

Your task is to analyze business notes or workflow descriptions and produce a clear,
implementation-oriented analysis.

Return only valid JSON.
Do not include markdown fences.
Do not include commentary outside the JSON.
Do not invent platform-specific implementation details unless supported by the notes.
If something is uncertain, place it under assumptions, missing_information, or clarifying_questions.
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