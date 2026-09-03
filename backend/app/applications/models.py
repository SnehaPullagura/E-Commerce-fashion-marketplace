"""
Hardened Application Domain Models with Compound Constraints and Validation.
"""

import uuid
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, Text, DateTime, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import declarative_base

from app.core.database import Base


class ApplicationStatus(str, Enum):
    PENDING = "PENDING"
    GENERATING = "GENERATING"
    GENERATED = "GENERATED"
    SUBMITTED = "SUBMITTED"
    FAILED_VALIDATION = "FAILED_VALIDATION"
    REJECTED_DUPLICATE = "REJECTED_DUPLICATE"


class Application(Base):
    __tablename__ = "applications"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), nullable=False, index=True)
    job_id = Column(String(100), nullable=False, index=True)
    idempotency_key = Column(String(128), unique=True, nullable=True, index=True)
    status = Column(String(30), default=ApplicationStatus.PENDING.value, nullable=False)
    content = Column(Text, nullable=False)
    generation_metadata = Column(Text, nullable=True)  # JSON metadata: model, temperature, diversity_score
    submission_receipt = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "job_id", name="uq_user_job_application"),
        CheckConstraint("length(trim(content)) >= 50", name="chk_application_content_non_empty"),
    )
