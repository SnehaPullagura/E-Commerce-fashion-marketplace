"""
Scheduler Service with Distributed Lock (SETNX / Mutex) and Dead Letter Queue (DLQ).
"""

import time
import uuid
import logging
from typing import Optional, Dict, Any, Callable, List

logger = logging.getLogger(__name__)


class DistributedLockAcquisitionError(Exception):
    pass


class DistributedLock:
    """
    In-memory / Redis simulated distributed lock implementing SETNX pattern with TTL
    to prevent duplicate cron/scheduler job executions across container replicas.
    """
    _locks: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def acquire(cls, lock_key: str, ttl_seconds: int = 60, owner_id: Optional[str] = None) -> Optional[str]:
        now = time.time()
        owner = owner_id or str(uuid.uuid4())

        # Clean expired lock
        if lock_key in cls._locks:
            if now > cls._locks[lock_key]["expires_at"]:
                del cls._locks[lock_key]

        # SETNX atomic simulation
        if lock_key not in cls._locks:
            cls._locks[lock_key] = {
                "owner": owner,
                "expires_at": now + ttl_seconds
            }
            return owner

        return None

    @classmethod
    def release(cls, lock_key: str, owner_id: str) -> bool:
        if lock_key in cls._locks and cls._locks[lock_key]["owner"] == owner_id:
            del cls._locks[lock_key]
            return True
        return False

    @classmethod
    def reset_all(cls):
        cls._locks.clear()


class DeadLetterQueue:
    """Stores permanently failed tasks after max retries are exhausted."""
    def __init__(self, max_retries: int = 3):
        self.max_retries = max_retries
        self.dlq_storage: List[Dict[str, Any]] = []

    def handle_failed_task(self, task_payload: Dict[str, Any], attempt_count: int, error_reason: str) -> bool:
        if attempt_count >= self.max_retries:
            self.dlq_storage.append({
                "task": task_payload,
                "attempts": attempt_count,
                "error": error_reason,
                "timestamp": time.time(),
                "status": "SENT_TO_DLQ"
            })
            logger.error(f"Task sent to Dead Letter Queue after {attempt_count} attempts: {error_reason}")
            return True  # Moved to DLQ, stop re-queuing
        return False  # Eligible for retry


class SchedulerService:
    """
    Guarded Scheduler Runner enforcing single-execution mutex and DLQ retry isolation.
    """
    dlq = DeadLetterQueue(max_retries=3)

    @classmethod
    def trigger_bulk_run(
        cls,
        job_name: str,
        execution_fn: Callable[[], Any],
        lock_ttl_seconds: int = 60,
        replica_id: Optional[str] = None
    ) -> Dict[str, Any]:
        lock_key = f"cron_lock:{job_name}"
        token = DistributedLock.acquire(lock_key, ttl_seconds=lock_ttl_seconds, owner_id=replica_id)

        if not token:
            logger.warning(f"Scheduler job '{job_name}' skipped: distributed lock already held by another replica.")
            return {
                "status": "SKIPPED_LOCK_HELD",
                "job": job_name,
                "executed": False
            }

        try:
            result = execution_fn()
            return {
                "status": "SUCCESS",
                "job": job_name,
                "executed": True,
                "result": result
            }
        finally:
            DistributedLock.release(lock_key, token)
