from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Literal


class NormalizeRequest(BaseModel):
    text: Optional[str] = None
    image: Optional[str] = None
    document: Optional[str] = None


class AdapterOutput(BaseModel):
    source_type: Literal["text", "image", "document"]
    content: str


class ExtractedContent(BaseModel):
    aggregated_content: str
    source_types: List[str]
    text_summary: str
    image_summary: str
    document_summary: str


class RefinedIntent(BaseModel):
    primary_goal: str
    problem_statement: str
    target_user: str
    requirements: List[dict]
    technical_constraints: List[str]
    business_constraints: List[str]
    design_constraints: List[str]
    deliverables: List[str]
    output_format: str
    open_questions: List[str]
    confidence_score: float


class FunctionalRequirement(BaseModel):
    id: str
    description: str
    priority: Literal["must", "should", "optional"]


class Meta(BaseModel):
    source_types: List[str]
    confidence_score: float = Field(ge=0.0, le=1.0)
    ambiguities_detected: bool


class Intent(BaseModel):
    primary_goal: str
    problem_statement: str
    target_user: str


class Constraints(BaseModel):
    technical: List[str]
    business: List[str]
    design: List[str]


class InputsProvided(BaseModel):
    text_summary: str
    image_summary: str
    document_summary: str


class ExpectedOutputs(BaseModel):
    deliverables: List[str]
    format: str


class RefinedPromptSchema(BaseModel):
    meta: Meta
    intent: Intent
    functional_requirements: List[FunctionalRequirement]
    constraints: Constraints
    inputs_provided: InputsProvided
    expected_outputs: ExpectedOutputs
    open_questions: List[str]
    rejection_reason: Optional[str] = None

    @field_validator("functional_requirements")
    @classmethod
    def validate_requirements(cls, v):
        if not v:
            raise ValueError("At least one functional requirement required")
        return v


class RejectionResponse(BaseModel):
    rejection_reason: str
