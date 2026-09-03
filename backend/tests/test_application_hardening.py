"""
Comprehensive Prevention Test Suite for Hardened Application Generation & Ingestion Pipeline.
Validates all 4 vulnerability mitigations:
1. Anti-runaway bounded pagination & scheduler distributed lock (50K+ prevention).
2. Anti-whitespace & empty AI generation validator.
3. High lexical diversity & non-robotic prompt synthesis.
4. Database unique constraint deduplication & idempotency key replay.
"""

import pytest
import asyncio
from typing import Dict, Any

from app.applications.ingestion_service import JobIngestionService
from app.applications.scheduler_service import SchedulerService, DistributedLock
from app.applications.ai_generation_service import (
    AIGenerationService,
    PromptBuilder,
    ApplicationGenerationValidationError
)
from app.applications.schemas import ApplicationCreateRequest
from app.applications.repository import ApplicationRepository
from app.core.exceptions import ConflictException


# ==============================================================================
# TEST 1: Bounded Pagination Terminates on Empty Page & Hard Max Pages Cap
# ==============================================================================
def test_pagination_terminates_on_empty_and_max_pages():
    call_count = 0

    def mock_infinite_feed_generator(page: int, token: str):
        nonlocal call_count
        call_count += 1
        # Upstream feed returns 10 items per page with infinite next tokens
        return {
            "items": [{"job_id": f"JOB_{page}_{i}"} for i in range(10)],
            "next_token": f"cursor_token_{page+1}",
            "has_more": True
        }

    # Execute with max_pages=10 to guarantee hard stop
    results = JobIngestionService.sync_feed(mock_infinite_feed_generator, max_pages=10)
    assert len(results) == 100
    assert call_count == 10  # Stopped strictly at max_pages=10, preventing 50,000 runaway calls

    # Test early termination on empty page
    def mock_early_empty_feed(page: int, token: str):
        if page == 3:
            return {"items": [], "next_token": "empty_cursor", "has_more": True}
        return {"items": [{"job_id": f"JOB_{page}"}], "next_token": f"cursor_{page+1}", "has_more": True}

    empty_results = JobIngestionService.sync_feed(mock_early_empty_feed, max_pages=100)
    assert len(empty_results) == 2  # Pages 1 and 2 ingested, broke on page 3


# ==============================================================================
# TEST 2: Scheduler Distributed Mutex Lock Prevents Multi-Replica Duplicate Runs
# ==============================================================================
def test_scheduler_distributed_lock_prevents_duplicate_runs():
    DistributedLock.reset_all()

    execution_counter = 0

    def mock_cron_task():
        nonlocal execution_counter
        execution_counter += 1
        return "SUCCESS"

    # Replica 1 triggers the cron job
    resp1 = SchedulerService.trigger_bulk_run("sync_hourly_applications", mock_cron_task, lock_ttl_seconds=30, replica_id="replica-pod-1")
    assert resp1["status"] == "SUCCESS"
    assert resp1["executed"] is True
    assert execution_counter == 1

    # Simulate Replica 2 attempting to run concurrently while lock is active
    lock_key = "cron_lock:sync_hourly_applications"
    # Manually re-acquire to simulate mid-execution hold
    DistributedLock.acquire(lock_key, ttl_seconds=30, owner_id="replica-pod-1")

    resp2 = SchedulerService.trigger_bulk_run("sync_hourly_applications", mock_cron_task, lock_ttl_seconds=30, replica_id="replica-pod-2")
    assert resp2["status"] == "SKIPPED_LOCK_HELD"
    assert resp2["executed"] is False
    assert execution_counter == 1  # Replica 2 was prevented from running duplicates


# ==============================================================================
# TEST 3: Validation Rejects Blank, Whitespace, or Below-Threshold Applications
# ==============================================================================
def test_reject_blank_or_whitespace_applications():
    # 1. Reject pure empty string
    with pytest.raises(ApplicationGenerationValidationError) as exc:
        AIGenerationService.generate_and_validate(simulated_response="")
    assert "below minimum required threshold" in str(exc.value)

    # 2. Reject pure whitespace and newlines
    with pytest.raises(ApplicationGenerationValidationError):
        AIGenerationService.generate_and_validate(simulated_response="   \n\n\t  \n   ")

    # 3. Reject short content (< 50 chars)
    with pytest.raises(ApplicationGenerationValidationError):
        AIGenerationService.generate_and_validate(simulated_response="Hi, I want this job. Thanks!")

    # 4. Pydantic schema validator rejects whitespace payload
    with pytest.raises(ValueError):
        ApplicationCreateRequest(
            user_id="usr_001",
            job_id="job_123",
            content="                                                  "  # 50 spaces
        )


# ==============================================================================
# TEST 4: AI Content Filter & Safety Refusal Fallback Isolation
# ==============================================================================
def test_ai_generation_content_filter_fallback():
    with pytest.raises(ApplicationGenerationValidationError) as exc:
        AIGenerationService.generate_and_validate(finish_reason="content_filter")
    assert "LLM safety filter triggered" in str(exc.value)


# ==============================================================================
# TEST 5: Lexical Diversity & Context Injection Eliminates Repetitive Bot Output
# ==============================================================================
def test_diversity_score_across_generated_applications():
    res1 = AIGenerationService.generate_and_validate(
        candidate_name="Elena Rostova",
        target_role="Principal Fashion Architect",
        company_name="Noir Couture",
        key_skills=["Anthropometric Sizing", "3D Drape Simulation", "FastAPI"],
        experience_summary="Over 8 years scaling high-fashion digital marketplaces and real-time CAD sizing."
    )
    assert res1["status"] == "GENERATED"
    assert res1["char_count"] >= 50
    assert res1["diversity_score"] >= 0.70  # High vocabulary entropy (>70% unique tokens)

    # Test PromptBuilder constructs high-entropy prompt with temperature=0.7
    prompt_pkg = PromptBuilder.build_prompt(
        candidate_name="Arjun Mehta",
        target_role="Lead Supply Chain Optimizer",
        company_name="Vogue Omnichannel",
        key_skills=["Geofenced Routing", "Linear Programming", "Inventory Graph"],
        experience_summary="Directed multi-node fulfillment networks cutting split-shipments by 40%."
    )
    assert prompt_pkg["hyperparameters"]["temperature"] == 0.7
    assert prompt_pkg["hyperparameters"]["presence_penalty"] == 0.4
    assert "Lead Supply Chain Optimizer" in prompt_pkg["system_prompt"]
    assert "Geofenced Routing" in prompt_pkg["system_prompt"]


# ==============================================================================
# TEST 6 & 7: Atomic Deduplication & Idempotency Key Replay
# ==============================================================================
@pytest.mark.asyncio
async def test_prevent_duplicate_application_under_concurrency_and_idempotency(db_session):
    user_id = "user_test_applicant_999"
    job_id = "job_req_lead_designer_001"
    idemp_key = "idemp_trans_uuid_abcdef123456"

    valid_content = "I am exceptionally well qualified for the Lead Designer position at your fashion house with 7 years of haute couture experience."

    req1 = ApplicationCreateRequest(
        user_id=user_id,
        job_id=job_id,
        content=valid_content,
        idempotency_key=idemp_key
    )

    # First creation succeeds
    app1 = await ApplicationRepository.create_application_atomic(db_session, req1)
    assert app1.id is not None
    assert app1.user_id == user_id
    assert app1.job_id == job_id

    # Second creation with SAME idempotency key returns exact same application (replay safe)
    app2 = await ApplicationRepository.create_application_atomic(db_session, req1)
    assert app2.id == app1.id

    # Third creation with DIFFERENT idempotency key but SAME (user_id, job_id) is blocked with ConflictException
    req_duplicate = ApplicationCreateRequest(
        user_id=user_id,
        job_id=job_id,
        content=valid_content,
        idempotency_key="idemp_another_key_999"
    )
    with pytest.raises(ConflictException) as exc:
        await ApplicationRepository.create_application_atomic(db_session, req_duplicate)
    assert "already exists for user" in str(exc.value)
