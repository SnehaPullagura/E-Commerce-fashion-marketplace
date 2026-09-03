"""
Application Repository with Atomic Deduplication and Idempotency Guardrails.
"""

from typing import Optional, Dict, Any, List
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.applications.models import Application, ApplicationStatus
from app.applications.schemas import ApplicationCreateRequest
from app.core.exceptions import ConflictException, ValidationException

logger = logging.getLogger(__name__)


class ApplicationRepository:
    """
    Transactional data access repository enforcing database-level compound unique constraints
    (user_id, job_id) and client idempotency key replay safety.
    """

    @staticmethod
    async def create_application_atomic(
        db: AsyncSession,
        req: ApplicationCreateRequest
    ) -> Application:
        # Check idempotency replay first
        if req.idempotency_key:
            idemp_stmt = select(Application).where(Application.idempotency_key == req.idempotency_key)
            idemp_res = await db.execute(idemp_stmt)
            existing_idemp = idemp_res.scalar_one_or_none()
            if existing_idemp:
                logger.info(f"Idempotent request replayed: returning existing application {existing_idemp.id}")
                return existing_idemp

        # Check existing application for (user_id, job_id)
        existing_stmt = select(Application).where(
            Application.user_id == req.user_id,
            Application.job_id == req.job_id
        )
        existing_res = await db.execute(existing_stmt)
        if existing_res.scalar_one_or_none():
            raise ConflictException(f"Application already exists for user '{req.user_id}' on job '{req.job_id}'")

        application = Application(
            user_id=req.user_id,
            job_id=req.job_id,
            content=req.content,
            idempotency_key=req.idempotency_key,
            status=ApplicationStatus.GENERATED.value
        )

        try:
            db.add(application)
            await db.commit()
            await db.refresh(application)
            return application
        except IntegrityError as exc:
            await db.rollback()
            logger.error(f"Integrity error on application creation: {exc}")
            raise ConflictException("Duplicate application prevented by database uniqueness constraint.")

    @staticmethod
    async def get_by_id(db: AsyncSession, application_id: str) -> Optional[Application]:
        stmt = select(Application).where(Application.id == application_id)
        res = await db.execute(stmt)
        return res.scalar_one_or_none()

    @staticmethod
    async def list_by_user(db: AsyncSession, user_id: str) -> List[Application]:
        stmt = select(Application).where(Application.user_id == user_id).order_by(Application.created_at.desc())
        res = await db.execute(stmt)
        return list(res.scalars().all())
