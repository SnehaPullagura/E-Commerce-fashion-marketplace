"""
Pydantic Schemas for Hardened Application Pipeline with Strict Validation.
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator, ConfigDict


class ApplicationCreateRequest(BaseModel):
    user_id: str = Field(..., description="Unique applicant user ID")
    job_id: str = Field(..., description="Target job requisition ID")
    content: str = Field(..., min_length=50, description="Application narrative / cover letter")
    idempotency_key: Optional[str] = Field(None, max_length=128, description="Client idempotency key")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)

    @field_validator("content")
    @classmethod
    def validate_content_not_whitespace(cls, v: str) -> str:
        trimmed = v.strip()
        if len(trimmed) < 50:
            raise ValueError("Application content must contain at least 50 non-whitespace characters")
        return trimmed


class ApplicationResponse(BaseModel):
    id: str
    user_id: str
    job_id: str
    status: str
    content: str
    idempotency_key: Optional[str] = None
    created_at: str

    model_config = ConfigDict(from_attributes=True)
