from pydantic import BaseModel, Field


class RequirementAnalysis(BaseModel):
    workflow_summary: str = Field(description="High-level workflow summary")
    actors: list[str] = Field(default_factory=list)
    entities: list[str] = Field(default_factory=list)
    stages_statuses: list[str] = Field(default_factory=list)
    business_rules: list[str] = Field(default_factory=list)
    automation_opportunities: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    missing_information: list[str] = Field(default_factory=list)
    clarifying_questions: list[str] = Field(default_factory=list)