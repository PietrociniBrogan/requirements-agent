from pydantic import BaseModel, Field


class ClarificationAnswer(BaseModel):
    question: str
    answer: str


class RefinedRequirementAnalysis(BaseModel):
    workflow_summary: str = Field(description="Updated workflow summary")
    confirmed_requirements: list[str] = Field(default_factory=list)
    actors: list[str] = Field(default_factory=list)
    entities: list[str] = Field(default_factory=list)
    stages_statuses: list[str] = Field(default_factory=list)
    business_rules: list[str] = Field(default_factory=list)
    automation_opportunities: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    unresolved_questions: list[str] = Field(default_factory=list)
    implementation_next_steps: list[str] = Field(default_factory=list)