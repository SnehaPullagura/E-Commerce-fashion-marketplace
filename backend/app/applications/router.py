"""
REST API Router for Hardened Application Generation and Management.
"""

from typing import List
from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.applications.schemas import ApplicationCreateRequest, ApplicationResponse
from app.applications.repository import ApplicationRepository
from app.applications.ai_generation_service import AIGenerationService, PromptBuilder

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
async def submit_application(
    req: ApplicationCreateRequest,
    idempotency_key: str = Header(None, alias="Idempotency-Key"),
    db: AsyncSession = Depends(get_db)
):
    if idempotency_key:
        req.idempotency_key = idempotency_key

    app = await ApplicationRepository.create_application_atomic(db, req)
    return app


@router.get("/user/{user_id}", response_model=List[ApplicationResponse])
async def list_user_applications(
    user_id: str,
    db: AsyncSession = Depends(get_db)
):
    return await ApplicationRepository.list_by_user(db, user_id)
